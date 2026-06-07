# Use statistical machine learning to detect nutrient thresholds in Microcystis blooms and microcystin management 

Article

Accepted Version
Creative Commons: Attribution-Noncommercial-No Derivative Works 4.0

Shan, K., Wang, X., Yang, H. ORCID: https://orcid.org/0000-0001-9940-8273, Zhou, B., Song, L. and Shang, M. (2020) Use statistical machine learning to detect nutrient thresholds in Microcystis blooms and microcystin management. Harmful algae, 94. 101807. ISSN 1878-1470 doi:
https://doi.org/10.1016/j.hal.2020.101807 Available at https://centaur.reading.ac.uk/90391/

It is advisable to refer to the publisher's version if you intend to cite from the work. See Guidance on citing.

To link to this article DOI: http://dx.doi.org/10.1016/j.hal.2020.101807
Publisher: Elsevier

All outputs in CentAUR are protected by Intellectual Property Rights law, including copyright law. Copyright and IPR is retained by the creators or other copyright holders. Terms and conditions for use of this material are defined in the End User Agreement.

# CentAUR 

Central Archive at the University of Reading
Reading's research outputs online

# Use statistical machine learning to detect nutrient thresholds in Microcystis blooms and microcystin management 

Kun Shan ${ }^{\mathrm{a}, \mathrm{b}^{*}}$, Xiaoxiao Wang ${ }^{\mathrm{b}, \mathrm{c}}$, Hong Yang ${ }^{\mathrm{d}}$, Botian Zhou ${ }^{\mathrm{a}, \mathrm{b}}$, Lirong Song ${ }^{\mathrm{c}, \mathrm{e}}$, Mingsheng Shang ${ }^{\mathrm{a}, \mathrm{b}}$<br>${ }^{a}$ Chongqing Key Laboratory of Big Data and Intelligent Computing, Chongqing Institute of Green and Intelligent Technology, Chinese Academy of Sciences, Chongqing 400714, China<br>${ }^{b}$ CAS Key Lab on Reservoir Environment, Chongqing Institute of Green and Intelligent Technology, Chinese Academy of Sciences, Chongqing 400714, China<br>${ }^{c}$ State Key Laboratory of Freshwater Ecology and Biotechnology, Institute of Hydrobiology, Chinese Academy of Sciences, Wuhan 430072, China<br>${ }^{d}$ Department of Geography and Environmental Science, University of Reading, Whiteknights, Reading, RG6 6AB, UK<br>${ }^{e}$ University of Chinese Academy of Sciences, Beijing 100049, China

[^0]
[^0]:    * Corresponding author.

#### Abstract

The frequency of toxin-producing cyanobacterial blooms has increased in recent decades due to nutrient enrichment and climate change. Because Microcystis blooms are related to different environmental conditions, identifying potential nutrient control targets can facilitate water quality managers to reduce the likelihood of microcystins (MCs) risk. However, complex biotic interactions and field data limitations have constrained our understanding of the nutrient-microcystin relationship. This study develops a Bayesian modelling framework with intracellular and extracellular MCs that characterize the relationships between different environmental and biological factors. This model was fit to the across-lake dataset including three bloom-plagued lakes in China and estimated the putative thresholds of total nitrogen (TN) and total phosphorus (TP). The lake-specific nutrient thresholds were estimated using Bayesian updating process. Our results suggested dual N and P reduction in controlling cyanotoxin risks. The total Microcystis biomass can be substantially suppressed by achieving the putative thresholds of TP $(0.10 \mathrm{mg} / \mathrm{L})$ in Lakes Taihu and Chaohu, but a stricter TP target ( 0.05 $\mathrm{mg} / \mathrm{L}$ ) in Dianchi Lake. To maintain MCs concentrations below $1.0 \mu \mathrm{~g} / \mathrm{L}$, the estimated TN threshold in three lakes was $1.8 \mathrm{mg} / \mathrm{L}$, but the effect can be counteracted by the increase of temperature. Overall, the present approach provides an efficient way to integrate empirical knowledge into the data-driven model and is helpful for the management of water resources.

Keywords: Bayesian modelling; eutrophication; nutrient thresholds; cyanobacterial blooms; Microcystis; microcystin

# 1. Introduction 

The harmful cyanobacterial blooms have been exacerbated across the world in the last decades with the growing threat from human activities and climate change (Harke et al., 2016; O'Neil et al., 2012). One of the cosmopolitan cyanobacterium genera is Microcystis, which has been reported to form blooms in more than 257 countries and territories, particularly in large lake ecosystems (Jankowiak et al., 2019). Blooms by Microcystis often cause serious environmental problems, such as degradation of water quality and illness or even death of other eukaryotic organisms, animals, and humans (MacKintosh et al., 1990; Singh et al., 2015), due to the production of hepatotoxic microcystins (MCs). As a result, identifying specific environmental conditions under which MCs in water columns can exceed the provisional World Health Organization (WHO) Guideline of $1.0 \mathrm{ug} / \mathrm{L}$ is of great importance for lake managers (Burch, 2008; WHO, 1998).

Previous studies have revealed that prevailing environmental conditions can result in high MCs events, including low nitrogen-phosphorus ratios (N:P) (Orihel et al., 2012), an imbalance in cellular carbon-nitrogen ratios (C:N) (Beversdorf et al., 2015), warm temperature (Bui et al., 2018), photosynthetically active radiation limitation (Wiedner et al., 2003), and iron limitation (Alexova et al., 2011). Compared to other environmental factors, N and P concentrations are more amenable to control. Furthermore, extensive cyanobacterial blooms and high MCs events are most prevalent in eutrophic and hypereutrophic lakes (Rigosi et al., 2015). Spatiotemporal patterns and ecophysiology of toxigenic Microcystis blooms are likely influenced by the distribution

of nutrients inside the lake (Otten et al., 2012). In this context, establishing nutrient thresholds or criteria for controlling an abrupt change or regime shift of toxic cyanobacterial blooms is a quantifiable and attractive approach (Xu et al., 2014; Zhang et al., 2006).

Setting nutrient control targets which are often being supported by scenario analysis using mechanistic models has been a challenge for lake managers (Recknagel et al., 2017). These process-based approaches can give insights into the biogeochemical cycling which are crucial to simulate how environmental conditions affect the composition and growth of phytoplankton (Reynolds and Irish, 1997). However, cyanotoxin production is highly variable in space and time and cannot be accurately predicted from cyanobacterial composition and abundance (Huisman et al., 2018). For instance, cyanobacterial blooms in natural water are often comprised of toxic and nontoxic strains, and changes in strain composition can, therefore, lead to major alterations in the toxin content (Kardinaal et al., 2007). It has also been reported that cyanotoxin production among taxa or even within strains of the same species is triggered by different environmental factors (Beaver et al., 2018; Davis et al., 2009). Complicating the prediction is that the majority of MCs remain intracellular in intact cells, and they are released into water columns when cells are lysed or damaged (Daly et al., 2007). Owing to the complex interaction between physical, chemical and biological factors, the capacity of mechanistic models to simulate the MCs dynamics remains poor.

In the last several years, data-intensive statistical models, have received increasing attention and several advanced methods have been developed to simulate MCs

concentrations. For example, the hierarchical zero-altered model (Taranu et al., 2017), the hierarchical Bayesian model (Yuan et al., 2017), and the Bayesian network (Yuan et al., 2019) have been fit to USEPA National Lake data and provided estimates of the potential relationships between different lake characteristics. Due to the large difference between areas, local water management teams want to explore lake-specific criteria. Therefore, a major challenge is to estimate the specific relationship for a lake from the limited samples. Bayesian inferential methods perform well when dealing with small sample sizes and limited data, leading to some ecological applications (Link and Barker, 2009). For instance, Kelly et al. (2019) estimated the environmental conditions associated with the probability of exceedance MCs levels in a eutrophic lake and the results help predict MCs risk. However, these approaches could not characterize the relationships between taxon-specific biomass and MCs production at the same time.

To remove the limitations, the present study presents a continuous variable Bayesian networks model, which develops from the basic model-developing strategy by Qian and Miltner (2015). The main research aim is to estimate the relationships between nutrient concentrations and potential MCs thresholds. Emphasis is given to the causal diagram, which combines cell-bound and dissolved MCs with different biotic and abiotic factors. To leverage knowledge from macro-scale data to enhance understanding of specific lakes, the Bayesian computation was applied to develop the across-lake model based on data from specific lakes. To showcase the modelling framework, this study applied data from three cyanobacterial bloom-plagued lakes in China and evaluated whether the nutrient control targets could be affected by warming

in the future.

# 2. Methods 

### 2.1 Dataset description

Three typical cyanobacterial bloom-dominated lakes in China, including Lake Taihu $\left(30^{\circ} 56^{\prime} \sim 31^{\circ} 33^{\prime} \mathrm{N}, \quad 119^{\circ} 55^{\prime} \sim 120^{\circ} 54^{\prime} \mathrm{E}\right)$, Lake Chaohu $\left(30^{\circ} 25^{\prime} \sim 31^{\circ} 43^{\prime} \mathrm{N}\right.$, $117^{\circ} 17^{\prime} \sim 117^{\circ} 52^{\prime} \mathrm{E}$ ), and Lake Dianchi ( $24^{\circ} 29^{\prime} \sim 25^{\circ} 28^{\prime} \mathrm{N}, 102^{\circ} 29^{\prime} \sim 103^{\circ} 01^{\prime} \mathrm{E}$ ), were selected for examination in this study. More detailed descriptions of sampling and laboratory methods are available in the study of Shan et al. (2019b). The following environmental variables were determined and included in this study: water temperature (WT, in ${ }^{\circ} \mathrm{C}$ ), dissolved oxygen (DO, in $\mathrm{mg} / \mathrm{L}), \mathrm{pH}$, electrical conductivity (EC, in $\mathrm{S} / \mathrm{m}$ ), Secchi disk (SD, in cm ), wind speed (WS, in $\mathrm{m} / \mathrm{s}$ ), total P (TP in $\mathrm{mg} / \mathrm{L}$ ), dissolved inorganic P (DIP, in $\mathrm{mg} / \mathrm{L}$ ), total N (TN, in $\mathrm{mg} / \mathrm{L}$ ), and dissolved inorganic N (DIN = ammonium $\left(\mathrm{NH}_{4}^{+}\right)+$nitrate $\left(\mathrm{NO}_{3}^{-}\right)+$nitrite $\left(\mathrm{NO}_{2}^{-}\right)$, in $\left.\mathrm{mg} / \mathrm{L}\right)$. The following biological variables were measured and included: chlorophyll- $a$ (Chl- $a$, in $\mu \mathrm{g} / \mathrm{L}$ ), cyanobacterial biomass ( $\mathrm{B}_{\text {cya }}$, in $\mathrm{mg} / \mathrm{L}$ ), total biomass of Microcystis ( $\mathrm{B}_{\mathrm{M}}$, in $\mathrm{mg} / \mathrm{L}$ ), and the taxonspecific biomass of Microcystis aeruginosa ( $\mathrm{B}_{\mathrm{MA}}$, in $\mathrm{mg} / \mathrm{L}$ ). The MCs concentrations were measured across 17 sampling transects encompassing the entire lakes. Dissolved microcystins ( dMCs , in $\mu \mathrm{g} / \mathrm{L}$ ) were measured by 96 wells filled for enzyme-linked immunosorbent assays. Cell-bound microcystins (cMCs, in $\mathrm{mg} / \mathrm{g}$ dry weight) were extracted with $90 \%(\mathrm{v} / \mathrm{v})$ aqueous methanol, and extracts have seeped through Sep Pak C18 cartridges. Finally, cell-bound MCs were eluted in solutions with $1 \mathrm{~mL} 50 \%(\mathrm{v} / \mathrm{v})$

chromatographic pure methanol (Thermo Fisher Scientific, Waltham, MA, USA) and stored at $-20{ }^{\circ} \mathrm{C}$ for HPLC analysis. The details of cell counting and MCs measurements are available in the study of Hu et al. (2016) and Wu et al. (2014).

# 2.2 Model development 

A Bayesian modelling framework was developed to link environmental factors, phytoplankton-related biomass, and MCs concentrations in the across-lake dataset. The steps of model development were summarized in Fig. 1.

### 2.2.1 LASSO regression

A regression model with the least absolute shrinkage and selection operator (LASSO) was used to build empirical regressions for developing the conceptual model of the Bayesian network (Tibshirani, 1996). Given a linear regression with predictor variable $x_{i}$ and response variable $y_{i}$, the LASSO solves the $l_{1}$-penalized regression problem of finding $\beta=\left\{\beta_{j}\right\}$ to minimize the formula as follows:

$$
\sum_{i=1}^{n}\left(y_{i}-\beta_{0}-\boldsymbol{x}_{i} \boldsymbol{\beta}\right)^{2}+\lambda \sum_{j=1}^{p}\left|\beta_{j}\right|
$$

where $\beta_{0}$ and $\boldsymbol{\beta}$ are the regression coefficients, and $p$ corresponds to the number of covariates in the model. LASSO identifies parsimonious predictive models by gradually shrinking the absolute value of regression coefficients so that the sum of all coefficients is less than a prespecified threshold $\left(\sum_{j=1}^{p}\left|\beta_{j}\right| \leq s\right)$ (Yuan et al., 2014). In LASSO regression, shrinkage and variable selection are achieved simultaneously because the coefficients are linearly shrunk to exactly zero, thereby avoiding overestimation of

variables. Given collinear variables and limited observations for MCs, concepts of parameter shrinkage by penalized estimation can be used to fit interpretable models with reliable predictions (Dahlgren et al., 2010; Hooten and Hobbs, 2015).

All physical-chemical (WT, EC, SD, DO, pH, WS, TN, DIN, TP, DIP, TN:TP, and DIN:TP) and biological (phytoplankton-related) variables were log-transformed before further analyze. Explanatory variables in LASSO regression were all standardized with zero as mean value and one as standard deviation. Given that $\lambda$ controls the amount of shrinkage induced, different values of $\lambda$ produced various models. The explanatory variables contributing to the model decrease with the increase in the value of $\lambda$. This study used a 10 -fold cross-validation procedure to calculate the standard error of models along the gradient of $\lambda$ and selected the value of $\lambda$ based on the "one-standard-error" rule (Breiman et al., 1984). The "glmnet" package in the R library was used to implement LASSO regression (Friedman et al., 2010).

# 2.2.2 Bayesian network 

Based on the results of LASSO, three following regressions can be linked together as a directed acyclic diagram (DAG) of the Bayesian network (BN) model (Fig. 2a). To deal with continuous variables, the initial DAG model was revised to connect data and unknow parameters (Fig. 2b). The first model was a regression for predicting Microcystis biomass, where WT, TP, DIN, SD, and pH were used as predictors. The second model was for predicting cell-bound MCs concentrations using the biomass of Microcystis and environmental variables including WT, DIN, and DIP. The third model

was for predicting dissolved MCs using cell-bound MCs concentrations and environmental variables including pH, WS, and TN. All these regression models were briefly summarized.

# (1) The Microcystis biomass model 

The Microcystis biomass model can be written as follow:
$\log \left(B_{M}\right)=\beta_{0}^{c}+\beta_{1}^{c} \log (S D)+\beta_{2}^{c} \log (T P)+\beta_{3}^{c} \log (W T)+\beta_{4}^{c} \log (D I N)+$ $\beta_{5}^{c} \log (p H)+\varepsilon^{c}$.

This model can be replaced with the probability distribution of $\log \left(B_{M}\right)$, and that is $\log \left(B_{M}\right) \sim \mathrm{N}\left(\mu_{M}, \sigma_{M}^{2}\right)$
$\mu_{M}=\beta_{0}^{c}+\beta_{1}^{c} \log (S D)+\beta_{2}^{c} \log (T P)+\beta_{3}^{c} \log (W T)+\beta_{4}^{c}$
(2) The Cell-bound MCs model

The cell-bound MCs model can be expressed as follow:
$\log (c M C s)=\beta_{0}^{d}+\beta_{1}^{d} \log (W T)+\beta_{2}^{d} \log (D I N)+\beta_{3}^{d} \log (D I P)+\beta_{4}^{d} \mu_{M}+\varepsilon^{d}$
This model can be changed with the probability distribution of $\log (c M C s)$, and that is $\log (c M C s) \sim \mathrm{N}\left(\mu_{c M C s}, \sigma_{c}^{2}\right)$
$\mu_{c}=\beta_{0}^{d}+\beta_{1}^{d} \log (W T)+\beta_{2}^{d} \log (D I N)+\beta_{3}^{d} \log (D I P)+\beta_{4}^{d} \mu_{M}$
(3) The Dissolved MCs model

The dissolved MCs model can be listed as follow:
$\log (d M C s)=\beta_{0}^{e}+\beta_{1}^{e} \log (p H)+\beta_{2}^{e} \log (W S)+\beta_{3}^{e} \log (T N)+\beta_{4}^{e} \mu_{c}+\varepsilon^{e}$

This model can be revised with the probability distribution of $\log (d M C s)$, and that is
$\log (d M C s) \sim \mathrm{N}\left(\mu_{d}, \sigma_{d}^{2}\right)$
$\mu_{d}=\beta_{0}^{\kappa}+\beta_{1}^{\kappa} \log (p H)+\beta_{2}^{\kappa} \log (W S)+\beta_{3}^{\kappa} \log (T N)+\beta_{4}^{\kappa} \mu_{c}$

# 2.2.3 Gibbs sampler 

Once these empirical models are established, they can be linked to form the joint probabilistic distribution of all parameters. The purpose of our Bayesian approach is to replace the conditional probability tables in traditional BN with a set of conditional probability distributions (Qian and Miltner, 2015). Estimating all unknown parameters result in the following likelihood function:

$$
\begin{aligned}
& \mathrm{L}\left(\log \left(B_{M}\right), \log (c M C s), \log (d M C s) \mid \theta\right) \\
& =\frac{1}{\left(2 \pi \sigma_{M}^{2}\right)^{\frac{3}{2}}} e^{-\frac{\left(\mu_{M}-\beta_{0}^{\kappa}-\beta_{1}^{\kappa} \log (S D)-\beta_{2}^{\kappa} \log (T P)-\beta_{3}^{\kappa} \log (W T)-\beta_{4}^{\kappa} \log (D I N)-\beta_{5}^{\kappa} \log (p H)\right)}{2 \pi \sigma_{M}^{2}}} \\
& \times \frac{1}{\left(2 \pi \sigma_{c}^{2}\right)^{\frac{3}{2}}} e^{-\frac{\left(\mu_{c}-\beta_{0}^{\phi}-\beta_{1}^{\phi} \log (W T)-\beta_{2}^{\phi} \log (D I N)-\beta_{3}^{\phi} \log (D I P)-\beta_{4}^{\phi} \mu_{M}\right)}{2 \pi \sigma_{c}^{2}}} \\
& \times \frac{1}{\left(2 \pi \sigma_{d}^{2}\right)^{\frac{3}{2}}} e^{-\frac{\left(\mu_{d}-\beta_{0}^{\kappa}-\beta_{1}^{\kappa} \log (p H)-\beta_{2}^{\kappa} \log (W S)-\beta_{3}^{\kappa} \log (T N)-\beta_{4}^{\kappa} \mu_{c}\right)}{2 \pi \sigma_{C}^{2}}}
\end{aligned}
$$

where $\theta$ represents a set of regression parameters. All model coefficients were defined in Equations 2, 5, and 8. Model coefficients were estimated simultaneously by the Gibbs sampler which was implemented using the Bayesian inference software JAGS (Plummer, 2003; Qian, 2016).

### 2.2.4 Monte Carlo simulations

Random variates as the model inputs (e.g., SD, TP, WT, DIN, DIP, TN, pH, and WS) were considered to follow log-transformation normal distributions. Based on the Pearson correlation coefficients, two nutrient groups (TP and DIP, TN and DIN) were assumed to follow the bivariate normal distributions. After the joint distribution of all coefficients was estimated by the Gibbs sampler, the statistical inference could subsequently be made through Monte Carlo simulations (Whitehead and Young, 1979). According to the management targets of Microcystis biomass and MCs concentrations (Table 1), the conditional distributions of TN and TP that were associated with acceptable low risks of toxic cyanobacterial blooms and be derived.

# 2.2.5 Bayesian updating 

Using the Bayesian updating method, the across-lake model was updated using data from specific lakes. In this present work, the estimated distributions of the coefficient from the across-lake model were applied as the prior distributions of coefficients from a lake-specific model. Qian and Reckhow (2007) suggested that improvement could be achieved by the Bayesian updating process if a priori parameter distribution across similarly sampling sites is known. Those updated models would be lake-specific and provide an insight into water quality management for local government.

### 2.3 Statistical analysis

To address the high spatiotemporal variation of dissolved and cell-bound MCs

concentrations, this study identified four components of the variation by intercept-only model: (1) inter-lake variation or variation in concentrations between different lakes; (2) inter-site within-lake variation or variation in concentrations collected at different sites in the same lake; (3) intra-year variation or variation in concentrations between different sampling months; and (4) residual error which includes variation due to measurement error and others.

The concentration of MCs in response to different forms of nutrient was assessed using generalized additive models (GAM). To examine the potential interactions between nitrogen and phosphorus, GAM models were applied using the combination of TN and TP, or DIN and DIP as two continuous explanatory variables:
$\log \left(M C_{i j}+1\right)=\alpha_{j}+S_{j}\left(\right.$ Nitrogen $\left._{i}, \quad\right.$ Phosphorus $\left._{i}\right)+\varepsilon_{i j}, \varepsilon_{i j} \sim N\left(0, \sigma^{2}\right)$
where $i$ and $j$ are indices for the observations (monthly MCs and nutrient concentrations) and the studied lakes, respectively. The smoothing function $\left(S_{j}\right)$ is the covariates between nitrogen and phosphorus. For two forms of MCs, the contour plots were used to visualize the function $S_{j}$. The "mgcv" package was used to implement GAM by optimizing the amount of cubic spline smoothing (Wood, 2001).

# 3. Results 

### 3.1 Spatiotemporal variation of MC and development of the BN conceptual model

This study identified four components by the intercept-only model to compare the spatiotemporal variation in MCs distribution (Table 2). Considering the cell-bound MCs, the standard deviation from sampling month variation was 0.249 , accounting for

the largest proportion of variance ( $75.6 \%$ ). The standard deviations from inter- and intra-lake variations were 0.09 and 0.057 , which accounted for $9.8 \%$ and $3.6 \%$ of the total variation in cell-bound MCs, respectively. Change in cell-bound MCs would be expected to exhibit regularly temporal trends due to that variation from inter-lake was likely stronger than that from intra-lake. By contrast, the standard deviation from sampling month variation was 0.049 , which took up $38 \%$ of the total variation in dissolved MCs. The standard deviations of inter- and intra-lake variations accounted for the remaining $14.6 \%$ and $9.2 \%$ of the dissolved MCs variation, respectively. The residual variation implied uncertainty in predicting dissolved MCs (38.2\%), which was considerably larger than that in predicting cell-bound MCs ( $11 \%$ ).

LASSO regression was applied in exploring the relationship among a subset of abiotic and biotic variables and MCs concentrations to develop the conceptual linkage (Fig. S1). First, $\mathrm{B}_{\mathrm{M}}$ achieved higher predictive accuracy than other biological factors, including Chl- $a, \mathrm{~B}_{\text {cya }}$, and $\mathrm{B}_{\mathrm{MA}}$. Utilizing cross-validation, the best model for predicting $\mathrm{B}_{\mathrm{M}}$, balancing parsimony, and predictive accuracy was the group of environmental variables including pH, TP, WT, DIN, and SD (Table 3). Second, relationships between cell-bound MCs and environmental factors were tested under the condition of combining different biotic factors (Table 4). When the model selected the variables including $\mathrm{B}_{\mathrm{M}}$, WT, DIN, and DIP, it achieved an accurate prediction of cell-bound MCs concentrations (MSPE $=0.037$ ). Third, the best predictive model for dissolved MCs was achieved (MSPE $=0.109$ ) with selected variables including cell-bound MCs, TN, pH , and WS. Based on the aforementioned results, a four-layer structure BN model was

constructed to incorporate different biotic and abiotic variables for predicting the risk of MCs.

# 3.2 Effects of environmental and biological factors on MC concentrations 

The coefficients of the fitted joint models were presented in Tables S1-S3. When the variables are log-transformed, the slop represents a change in the response variable under per unit change in the predictor. For instance, the estimated $\beta_{3}^{c}$ was 0.56 (Table S1) which represented an approximately $0.56 \%$ increase in $\mathrm{B}_{\mathrm{M}}$ for a $1 \%$ increase in TP. When TP had a $1 \%$ increase, $\mathrm{B}_{\mathrm{M}}$ increased by $0.59 \%, 0.55 \%$, and $0.54 \%$ in Lakes Taihu, Chaohu, and Dianchi, respectively. When TN had a $1 \%$ increase, dissolved MC concentrations increased by $0.24 \%, 0.16 \%$, and $0.15 \%$ in Lakes Taihu, Chaohu, and Dianchi, respectively, which were reflected by the value of $\beta_{3}^{e}$ in Table S3.

The effect of nutrients on MCs was considered to change via network structure (Table 5). Given the increase in P concentrations from the $25^{\text {th }}$ to the $75^{\text {th }}$ percentile, $\mathrm{B}_{\mathrm{M}}$ was predicted to increase by $91.8 \%$, whereas cell-bound MCs and dissolved MCs concentrations decreased by $7.5 \%$ and $4.4 \%$, respectively. When N concentrations increased from the $25^{\text {th }}$ to the $75^{\text {th }}$ percentile, the cell-bound MCs concentrations decreased from 0.312 to 0.276 , whereas dissolved MCs increased from 0.676 to 0.713 . The concentration of MCs in response to N and P was assessed using the GAM approach (Fig. 3). The model results suggested that MCs concentrations depended heavily on the interaction between TP and TN. More specifically, cell toxin quota was sensitive to the conditions of low DIN concentrations and high TN:TP ratios, whereas

the probability of dissolved MCs was higher at the increase of TN and SRP than that of TP.

# 3.3 Evaluation of nutrient control targets 

Monte Carlo simulation was repeated until 10,000 TP and TN values were accepted. Given the condition of $\mathrm{B}_{\mathrm{M}}<0.6 \mathrm{mg} / \mathrm{L}$ and $\mathrm{MCs}<0.4 \mu \mathrm{~g} / \mathrm{L}$, a histogram of the discrete distribution indicated that the means of TN and TP in conditional distribution were lower than those in marginal distribution, although both had similar variance (Fig. 4). If this calculated conditional distribution can be considered as the "reference" distribution, the U.S. EPA's recommendation can be set as the nutrient criterion at the $75^{\text {th }}$ percentile (U.S. EPA, 2000). The criterion was $0.16 \mathrm{mg} / \mathrm{L}$ for TP (marginal: 0.24 $\mathrm{mg} / \mathrm{L}$ ) and $3.12 \mathrm{mg} / \mathrm{L}$ for TN (marginal: $3.78 \mathrm{mg} / \mathrm{L}$ ), respectively. Alternatively, the U.S. EPA also recommends that the $25^{\text {th }}$ percentile in all sampling data can be accepted as the nutrient criterion when "reference" distributions are unavailable. The TN criterion in our data had a $25^{\text {th }}$ percentile of $1.8 \mathrm{mg} / \mathrm{L}$, and the TP criterion had a $25^{\text {th }}$ percentile of $0.1 \mathrm{mg} / \mathrm{L}$. This threshold of TP is close to the empirical value in eutrophication management. However, the significant difference in the estimated values from a $75^{\text {th }}$ percentile and a $25^{\text {th }}$ percentile may largely be attributed to the large spatiotemporal variations in $\mathrm{B}_{\mathrm{M}}$ and MCs in the studied lakes.

Furthermore, the goal of setting a single nutrient criterion for different bloom dominated lakes is likely impractical. After the process of Bayesian updating, those updated models could be used to evaluate lake-specific nutrient thresholds by achieving

the management targets (e.g., $\mathrm{B}_{\mathrm{M}}<0.6 \mathrm{mg} / \mathrm{L}$ or $\mathrm{MCs}<1.0 \mu \mathrm{~g} / \mathrm{L}$ in Fig. 5). Despite a considerable interaction that exists, the models responded to changes of P more rapidly than changes of N , and they predicted the high probabilities of achieving water quality objectives at low nutrients concentrations. However, Microcystis biomass or MCs concentrations in the three lakes differed in their response to nutrients. The probability of meeting the $\mathrm{B}_{\mathrm{M}}$ objectives of $0.6 \mathrm{mg} / \mathrm{L}$ at the target TP concentration $(0.10 \mathrm{mg} / \mathrm{L})$ in Lake Dianchi was approximately 0.3 , while the probabilities in Lakes Taihu and Chaohu were nearly close to 1.0 (Fig. 5a). At a stricter TP target ( $0.05 \mathrm{mg} / \mathrm{L}$ ), the probability in Lake Dianchi increased to 0.6 . On the other hand, the probability of meeting the MCs objectives at the target TN concentration in Lake Dianchi was higher than those in the other two lakes. When the estimated TN target was set to $1.8 \mathrm{mg} / \mathrm{L}$, the probabilities of meeting the provisional guidelines of $\mathrm{WHO}(\mathrm{MCs}<1.0 \mu \mathrm{~g} / \mathrm{L})$ in three studied lakes were above 0.8 (Fig. 5b).

Nutrients in water are not the only key factors influencing the proliferation of Microcystis and the production of MCs. Thus, other factors, such as water temperature, were considered to achieve the desired water quality goals. Updated model coefficients were used to estimate the probability of $\mathrm{B}_{\mathrm{M}}<1.5 \mathrm{mg} / \mathrm{L}$ and $\mathrm{MCs}<1.0 \mu \mathrm{~g} / \mathrm{L}$ as a function of both TN or TP and WT, with all other variables taken their respective observed means (Fig. 6). Simulated scenarios of nutrient enrichment and temperature warming suggested that toxic cyanobacterial blooms may be more sensitive to synergistic effects rather than individual effects alone. For instance, the effects of interactions between TP and WT were evident when WT exceeded $20^{\circ} \mathrm{C}$. On the

contrary, the effect of TN will be counteracted by the fluctuations of water temperature when separating the joint effects of different forms of N and P .

# 4. Discussion 

### 4.1 The potential factors influencing the spatiotemporal variations in MCs

The key challenge for the risk management of MCs is the large spatiotemporal variation, lack of sufficient field measurement, and complicated relationships between different forms of nutrients. From the results of the intercept-only model, most variations in observed MCs were quite dependent upon the temporal sampling scale. Thus, seasonal variation in environmental conditions should be considered when setting the targets of nutrient control (Tong et al., 2019). Variations from inter-lake were likely stronger than those from different sites inside the lake, which indicated the importance of the regional effect. However, the variations from inter-lake in predicting dissolved MCs were likely stronger than those in predicting intracellular MCs. This was in line with the previous study in the Midwestern US that found a positive association between MCs and lake latitude (Graham et al., 2004).

Insights gained from linkage among multiple variables could be sharpened by considering the simultaneous effects of biotic and abiotic conditions. The LASSO regression may provide more accurate predictions of MCs concentrations under the conditions of collinearity (Yuan et al., 2014). When all environmental variables were considered together, the total biomass of Microcystis was the best biological variable for predicting toxin quota; thereby implying that all detected MC-producing genotypes

were likely to belong to the cyanobacterium Microcystis (Ye et al., 2009). In addition, the biomass of toxic Microcystis aeruginosa did not achieve the same prediction accuracy as the total Microcystis biomass. It is reasonable to infer that other morphospecies such as Microcystis viridis might also produce considerable amounts of MCs (Shan et al., 2019a; Wu et al., 2017).

Because of multiple sampling sites within lakes, causal relationships between environmental drivers and MCs showed stronger evidence than analyses of a single lake or a snapshot sampling. The biomass of Microcystis was found to be positively correlated with TP and negatively with DIN, buttressing previous findings in San Francisco Bay by Lehman et al. (2013). On the other hand, the trends from multivariate analysis also reinforced that the tradeoff between the costs and benefits of MCs production as N -rich secondary metabolites reduced disproportionately under N limitation (Horst et al., 2014; Monchamp et al., 2014). In agreement with results from the analysis of the US continental-scale data, TN contributed a higher proportion of the variation in MCs in water columns than TP (Beaver et al., 2014; Yuan et al., 2017). There is, however, strong evidence that the relationships between MCs and nutrients were more complex rather than a hypothesized linear response due to the variations in strain within species (Shan et al., 2019a).

# 4.2 Rationality and limitations of the proposed framework 

It is usually difficult to imitate the dynamics of MCs in situ by mathematical equations, because of their complicated fate in the aquatic environment (Wörmer et al.,

2011). In this study, a Bayesian modelling framework that accommodates rigorous uncertainty analysis was proposed to quantify the risk of MCs. The iterative nature of the Bayesian theorem can incorporate existing knowledge and update the joint distribution as new information, thereby developing a site-specific model using a local dataset (Arhonditsis et al., 2008; Cha et al., 2014). Our proposed model was developed based on the across-lake dataset and therefore achieve the necessary statistical purpose by increasing the sample size (Malve and Qian, 2006). Multi-lake data are incorporated into empirical models to broaden the sample size and stabilize the inference, while the resulting model may not be very relevant to anyone lake.

Biotic and abiotic variables are constantly numeric, and discretizing continuous variables into a finite set of states is a key step in implementing the Bayesian network. In previous studies, the discretization of a continuous variable has relied on expert experience, recognized thresholds, and frequency distribution of response nodes (Lucena-Moya et al., 2015). Because the conclusions may rely on the choice of discretization method, Nojavan et al. (2017) suggested that the discretization of continuous variables should be avoided if possible. This study took advantage of a series of conditional probability distributions to replace the conditional probability tables, to avoid discretizing continuous variables (Qian and Miltner, 2015).

For heuristic purposes, this study established a Bayesian network that represents the hypothesized causal connections among environmental factors, biological biomasses, and MCs concentrations. However, this approach has a limitation that empirical regression allows variables to be modelled with linear relationships. The

Bayesian inferential method provides an entire predictive distribution for the response variables over which inference can be made instead of using a point estimate, such as the mean value (Stow et al, 2006). In addition, a stereotype of the method without considering lake-specific environmental gradients could lead to some problems (Taranu et al., 2012), because the structure of the DAG model is a dominant source of uncertainty. Hence, the repetition of the building process in other lakes may be preferable to the indiscriminate use of it.

# 4.3 Implications for future research and water quality management 

Water pollution in China poses a huge threat to the environment and human health (Yang et al., 2013). The Chinese government has invested a large amount of money on it. For example, $\sim 100$ billion RMB ( US $\$ 14$ billion) has been invested in Lake Taihu ecosystem restoration. However, nutrient concentrations and cyanobacterial blooms have not been mitigated as quickly as expected (Qin et al., 2019). Long-term nutrient trends confirmed that TP concentrations were relatively stable or has possibly increased over the last decade, despite the decline of TN concentrations (Xu et al., 2017). Considering the long hydraulic residence time in three studied lakes, a legacy of the internal loading, especially P , is a formidable problem for the rapid recovery of water quality (Shan et al., 2014). In general, TP concentration was the principal force driving cyanobacteria's contribution to total algal biomass (Wagner and Adrian, 2009). Our results reinforced the viewpoint that P is the main element regulating Microcystis biomass, whereas N may influence the overall toxicity of blooms. We recommend the

importance of dual N and P reduction in the future management of toxic cyanobacterial blooms.

Furthermore, prudent sustainable management of MCs will require the consideration of the background of limnologic conditions and effect of increasing water temperature, due to that the efforts of nutrient reductions in controlling toxic cyanobacterial blooms may be counteracted by the effect of increasing temperature (Lürling et al., 2017; Richardson et al., 2018). This partly conforms to the field observations in Grand Lake St. Marys, western Ohio, U.S. (Walls et al., 2018) and field survey in 137 European lakes (Mantzouki et al., 2018). Monte Carlo simulation indicated that the highly hazardous risk of Microcystis and microcystins were controlled by achieving the TN and TP thresholds at below $0.8 \mathrm{mg} / \mathrm{L}$ and $0.05 \mathrm{mg} / \mathrm{L}$, which were previously estimated by a nutrient dilution bioassay in Lake Taihu (Xu et al., 2014). Nevertheless, managing all lakes to a single TN and TP concentration is infeasible. Due to differences between lake ecoregions in China, effective management strategies require a good understanding of the influence of nutrients in different regions (Liang et al., 2019).

In contrast to the effect of TN on MCs, TP thresholds under a range of possible windows exhibited significant differences between Lake Dianchi and the other two lakes. The simulation results indicated that it was important to implement stricter control objectives of TP in Lake Dianchi. In comparison, the low concentrations of dissolved MCs in Lake Dianchi might be attributed to the photodegradation under high UV radiation; however, toxigenic genera could form the MC-protein complexes that

prevent proteolytic degradation within the cell (Melssner et al., 2013; Su et al., 2019). Our results suggested controlling toxic cyanobacterial blooms in lakes within low latitudes should strictly control nutrients and focus on the cell quota instead of extracellular toxin in water columns alone.

# 5. Conclusions 

In this study, a Bayesian modelling framework incorporating biotic and abiotic factors was proposed to predict the risk of MCs. Using data from three bloomdominated lakes in China, our approach can aid in understanding the causal link between key factors and MCs concentrations, by which researchers and decisionmakers can partly infer and predict future MCs scenarios. The results demonstrate the estimated TP thresholds are crucial for reducing the biomass of Microcystis. More importantly, the estimated TN thresholds for controlling cyanotoxin can be counteracted by the effect of increasing temperature.

## Acknowledgements

This work was supported by National Natural Science Foundation of China (No.51609229; 41701247; 51979262), Chongqing Science and Technology Commission (No. cstc2017jcyjAX0241; cstc2018jscx-msyb1133) and National Key Scientific and Technological Project of China (2014ZX07104-006). The field data in three studied lakes of China was financed by the National Basic Research Program of China (2008CB418006).
