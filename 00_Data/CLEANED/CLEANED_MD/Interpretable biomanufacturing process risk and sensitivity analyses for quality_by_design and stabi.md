# Interpretable Biomanufacturing Process Risk and Sensitivity Analyses for Quality-by-Design and Stability Control 

Wei Xie ${ }^{1}$ | Bo Wang ${ }^{1}$ | Cheng $\mathrm{Li}^{2}$ | Dongming Xie ${ }^{3}$<br| Jared Auclair ${ }^{4}$

${ }^{1}$ Department of Mechanical and Industrial Engineering, Northeastern University, Boston, MA 02115, USA
${ }^{2}$ Department of Statistics and Applied Probability, National University of Singapore, Singapore
${ }^{3}$ Department of Chemical Engineering, University of Massachusetts Lowell, Lowell, MA 01854, USA
${ }^{4}$ Department of Chemistry and Chemical Biology, Northeastern University, Boston, MA 02115, USA

## Correspondence

Wei Xie, Department of Mechanical and Industrial Engineering, Northeastern University, Boston, MA 02115, USA Email: w.xie@northeastern.edu

While biomanufacturing plays a significant role in supporting the economy and ensuring public health, it faces critical challenges, including complexity, high variability, lengthy lead time, and very limited process data, especially for personalized new cell and gene biotherapeutics. Driven by these challenges, we propose an interpretable semantic bioprocess probabilistic knowledge graph and develop a game theory based risk and sensitivity analyses for production process to facilitate quality-by-design and stability control. Specifically, by exploring the causal relationships and interactions of critical process parameters and quality attributes (CPPs/CQAs), we create a Bayesian network based probabilistic knowledge graph characterizing the complex causal interdependencies of all factors. Then, we introduce a Shapley value based sensitivity analysis, which can correctly quantify the variation contribution from each input factor on the outputs (i.e., productivity, product quality). Since the bioprocess model coefficients are learned from limited process observations, we derive the Bayesian posterior distribution to quantify model uncertainty and further develop the Shapley value based sensitivity analysis to evaluate the impact of estimation uncertainty from each set of model co-

efficients. Therefore, the proposed bioprocess risk and sensitivity analyses can identify the bottlenecks, guide the reliable process specifications and the most informative data collection, and improve production stability.

KEYWORDS
Bioprocess risk analysis, sensitivity analysis, manufacturing process stability control, Bayesian network, process causal interdependence

# 1 | INTRODUCTION 

Biomanufacturing is growing rapidly and playing an increasingly significant role in supporting the economy and ensuring public health. For example, the biopharmaceutical industry generated more than $\$ 300$ billion in revenue in 2019 and more than $40 \%$ of the drug products in the development pipeline were biopharmaceuticals (Rader and Langer, 2019). However, drug shortages have occurred at unprecedented rates over the past decade. The current systems are unable to rapidly produce new drugs to meet urgent needs in the presence of a major public health emergency. The COVID-19 pandemic is having a profound impact globally and caused over 111 millions confirmed cases by February, 2021. Even COVID-19 vaccines are discovered, developing the production process and manufacturing the billions of doses needed to immunize the world's population will be extremely time-consuming using existing technologies, thus lengthening the time period of human and economic distress. It is critically important to speed up the bioprocess development and ensure product quality consistency.

However, biomanufacturing faces several critical challenges, including high complexity and variability, and lengthy lead time (Kaminsky and Wang, 2015). Biomanufacturing is based on living cells whose biological processes are very complex and have highly variable outputs. The productivity and product critical quality attributes (CQAs) are determined by the interactions of hundreds of critical process parameters (CPPs), including raw materials, media compositions, feeding strategy, and process operational conditions, such as pH and dissolved oxygen in the bioreactor. As new biotherapeutics (e.g., cell and gene therapies) become more and more "personalized", the production, regulation procedure, and analytical testing time required by biopharmaceuticals of complex molecular structure is lengthy, and the historical observations are relatively limited in particular for drugs in early stages of production process development.

Therefore, it is crucial to integrate all sources of data and mechanism information, provide the risk- and science-based understanding of the complex bioprocess CPPs/CQAs causal interdependencies, and identify and control the key factors contributing the most to the output variation. This study can accelerate the development of productive and reliable biomanufacturing, facilitate building the quality into the production process or quality-by-design ( QbD ), support realtime monitoring and release, and reduce the time to market.

Various Process Analytical Technologies (PAT) and methodologies have been proposed to improve the bioprocess understanding and guide the process development, decision making, and risk control; see the review in Steinwandter et al. (2019). Most PATs are based on multivariate data analysis; see Section 2. Ordinary or partial differential equations (ODEs/PDEs) based mechanistic models are developed for simulating individual biomanufacturing unit operations; see for example Kyriakopoulos et al. (2018). On the other hand, various operations research/management (OR/OM) methods are also proposed for biomanufacturing system analytics and decision-making; see the review (Kaminsky and Wang, 2015). Overall, existing methodologies have the key limitations: (1) the multivariate statistics based PAT and

OR/OM approaches focus on developing general methodologies without incorporating the bioprocess causal relationship and structural mechanism information, which limits their performance, interpretability, and adoption, especially with limited data; and (2) the mechanistic models are usually deterministic and focus on individual unit operations without providing an reliable integrated bioprocess learning and risk management framework.

Driven by the critical challenges in the biomanufacturing industry, in this paper, we propose a bioprocess semantic probabilistic knowledge graph, characterizing the risk- and science-based understanding of integrated production process, which can integrate all sources of heterogeneous data and leverage the information from existing mechanism models and historical data. Then, we introduce comprehensive and rigorous bioprocess risk and sensitivity analyses, accounting for model risk, which can guide the process specifications and most informative data collection to facilitate the learning and improve the production reliability and stability (e.g., product quality consistency).

The key contributions of this paper are three fold. First, by exploring the causal relationships and interactions of many factors within and between operation units (i.e., CPPs/CQAs), such as raw materials, production process parameters, and product quality, we consider a bioprocess ontology based data integration and develop a Bayesian network (BN) based bioprocess probabilistic knowledge graph, characterizing the process inherent stochastic uncertainty and causal interdependencies of all input and output factors. Second, building on the process knowledge graph, we introduce a game theory - Shapley value (SV) - based sensitivity analysis (SA), considering the complex bioprocess interdependencies, which can correctly quantify the contribution and criticality of each random input factor on the variance of outputs (i.e., productivity and product CQAs), identify the bottlenecks, and accelerate the reliable bioprocess specifications. Third, since the coefficients of interpretable bioprocess model or probabilistic knowledge graph are estimated from limited real-world process data, which induces model uncertainty (MU) or model risk (MR), we further propose Bayesian uncertainty quantification and Shapley value based model uncertainty sensitivity analysis to support process learning and faithfully assess the impact of estimation uncertainty from each set of model coefficients. Thus, our study can: (1) identify the bottlenecks of bioprocess; (2) accelerate the reliable process specifications and development to improve the production process stability and facilitate QbD; and (3) support the most "informative" data collection to reduce the model risk of process probabilistic knowledge graph and improve the bioprocess understanding.

This paper is organized as follows. In Section 2, we review the related literature on biomanufacturing process modeling and PATs, Bayesian network, and process sensitivity analysis. In Section 3, we present the problem description and summarize the proposed framework. In Section 4, we develop the Bayesian network (BN) based bioprocess probabilistic knowledge graph to characterize the risk- and science-based process understanding. We derive the Shapley value (SV) based bioprocess sensitivity analysis in Section 5 to support the process specifications, improve the production stability, and ensure product quality consistency. We further introduce the process model coefficient uncertainty quantification and Shapley value based sensitivity analysis studying the impact of each model coefficient estimation uncertainty on process risk analysis and CPPs/CQAs criticality assessment in Section 6. We conduct the empirical study on the performance of our proposed framework in both simulation and real data analysis in Section 7, and then conclude with some discussion in Section 8.

# 2 | BACKGROUND 

The Process Analytical Technologies (PAT) are defined as "a system for designing, analyzing and controlling manufacturing through timely measurements of critical quality and performance attributes of raw and in-process materials and processes, with the goal of ensuring final product quality"; see Pharmaceutical Current Good Manufacturing Practices (CGMPs) (2004). With the established process sensors and analyzers, such as near infrared spectroscopy, Raman

spectrocopy, and multiwavelength fluorescence, various multivariate data analysis approaches have been used for bioprocess PATs, including principal component analysis (PCA) (Ayech et al., 2012), partial least squares (PLS) (De Lira et al., 2010), clustering (Prinsloo et al., 2008), multilinear regression (Wechselberger et al., 2012), artificial neural network (ANN) (Li and Venkatasubramanian, 2018), genetic algorithm (Sokolov et al., 2018), elastic net (Severson et al., 2015), support vector machines (Li and Yuan, 2006), and root cause analysis (Borchert et al., 2019); see an overview in Rathore et al. (2010). However, existing PAT approaches are usually based on generalized multivariate "black-box" approaches quantifying the input-output relationship without incorporating the bioprocess mechanism information.

On the other hand, OR/OM methodology development for biomanufacturing analysis and decision making is still in its infancy (Kaminsky and Wang, 2015). Mixed integer linear programming (Lakhdar et al., 2007; Leachman et al., 2014), dynamic lot size model (Fleischhacker and Zhao, 2011), and queueing network and simulation models (Lim et al., 2004; Kulkarni, 2015) have been developed to study resource planning, scheduling and material consumption in biomanufacturing. Those approaches focus on developing general methodologies without fully exploring the bio-technology domain knowledge (e.g., causal relationship, structural information of the bioprocess). Some recent works, e.g., Martagan et al. (2016, 2017, 2018), account for physical-chemical characteristics and biology-induced randomness in either fermentation or chromatography stage, and develop Markov decision models to optimize the corresponding operational policies.

For complex systems, Bayesian network (BN) can be used to combine the expert knowledge with data and facilitate data integration and process analysis in various applications. For example, Wang et al. (2018) proposed a BN based knowledge management system for additive manufacturing. Troyanskaya et al. (2003) introduced a BN that combines evidence from gene co-expression and experimental data to predict whether two genes are functionally related. Moullec et al. (2013) provided a BN approach for system architecture generation and evaluation, and Telenko and Seepersad (2014) applied probabilistic graphical model to study how the usage context factors, including human factors, situational factors, and product design factors, impact on the energy consumption of the lightweight vehicle to guide usage scenarios and vehicle designs. Furthermore, Bayesian posterior and belief propagation based risk assessment has been studied in information system security (Feng et al., 2014), water mains failure (Kabir et al., 2015), and supply chain (Ojha et al., 2018). Motivated by these studies, we propose a Bayesian network for modeling the complex interdependence of production process parameters and bio-drug properties, which can fully utilize the structural knowledge and causal relationship, and integrate the data from end-to-end bioprocess.

Finally, we briefly discuss the related literature on sensitivity analysis; see the review (Borgonovo and Plischke, 2016). The existing sensitivity analysis studies associated with Bayesian network tend to systematically vary one of network's parameter at a time while fixing the other parameters and then obtain analytic expressions for the sensitivity functions (Van der Gaag et al., 2007; Castillo et al., 1997). In our case, we are interested in stochastic uncertainty contributed by each factor, which is closely related to global probabilistic sensitivity analysis. Existing literature on global sensitivity analysis can be divided into several categories, including: (1) regression based methods, e.g., Helton (1993), which use the standardized regression coefficients as sensitivity measure; (2) variance based methods (Wagner, 1995; Sobol, 1993) which assess the contribution of each random input based on expected reduction in model output variance; (3) functional ANOVA decomposition (Rabitz and Aliş, 1999) which provides variance decomposition under independence through high dimensional model representation theory; (4) density-based methods (Zhai et al., 2014) that directly quantify the output density without reference to a particular moment. Since the commonly used variance-based sensitivity measures (i.e., first-order effects and total effects) fail to adequately account for probabilistic dependence of inputs and process structural interactions or interdependencies, Owen (2014) introduced a new sensitivity measure based on the game theory, called the Shapley Value (SV). Song et al. (2016) further analyzed this measure and proposed a Monte Carlo algorithm for the estimation of Shapley values. Lundberg and Lee (2017) pro-

posed Shapley value based unified framework for interpreting predictions. Inspired by these studies, building on the proposed BN-based bioprocess knowledge graph characterizing the process causal interdependencies, we introduce SV-based probabilistic sensitivity analysis to assess the contribution or criticality of each random input (e.g., CPP and CQA ) on the output variance, while accounting for the impact of model estimation uncertainty associated with each set of model coefficients.

# 3 PROBLEM DESCRIPTION AND PROPOSED FRAMEWORK 

We create a probabilistic graph model characterizing the risk- and science-based understanding of causal interdependencies between bioprocess CPPs/CQAs, and then propose risk and sensitivity analyses for integrated biomanufacturing process, accounting for model uncertainty. This study can: (1) provide a reliable guidance on process specification, CPPs/CQAs monitoring, and most informative data collection; (2) facilitate production stability control and quality-by-design (QbD); and (3) accelerate real-time release, speed up the time to market, and reduce the drug shortage.

An illustration of biomanufacturing process is provided in Fig. 1 with a fish bone representation of bioprocess input factors introduced in each unit operation impacting on the outputs. The biomanufacturing process typically has several main unit operations, including: (1) media preparation, (2) inoculum fermentation, (3) main fermentation, (4) centrifugation(s), (5) chromatography/purification, (6) filtration, (7) fill and finish, and (8) quality control. Steps (1)-(3) belong to upstream cell culture, Steps (4)-(6) belong to downstream target protein purification, and Steps (7)-(8) are for finished drug filling/formulation and final product quality control testing.

The interactions of many factors impact the variability of outputs (e.g., drug quality, productivity). They can be divided into CPPs and CQAs in general; see the definitions of CPPs/CQAs in ICH Q8(R2) Guideline et al. (2009).

CPP: At each process unit operation, CPPs are defined as critical process parameters whose variability impacts on product CQAs, and therefore should be monitored and controlled to ensure the process produces the desired quality.
CQA: A physical, chemical, biological, or microbiological property that should be within an appropriate limit, range, or distribution to ensure the desired product quality.

Since the raw material attributes are outputs of release materials, they should be considered along with CPPs as impacting process variability.

We represent the system output (e.g., product CQAs, productivity) with a random variable, denoted by $Y$, which depends on CPPs/CQAs inputs, denoted by $\mathbf{X}$, and other uncontrolled/uncontrollable input variables (e.g., contamination), modeled by residuals $\mathbf{e}$. We represent the impact of complex interactions of input factors $(\mathbf{X}, \mathbf{e})$ throughout the production process on the response by $Y=g(\mathbf{X}, \mathbf{e} \mid \boldsymbol{\theta})$, where the unknown function $g(\mathbf{X}, \mathbf{e} \mid \boldsymbol{\theta})$, specified by model coefficients $\boldsymbol{\theta}$, models the complex interactions of integrated bioprocess and characterizes the impact of random inputs $(\mathbf{X}, \mathbf{e})$ on the output $Y$. For notation simplification, we consider the unit-variate response/output in the paper, and the proposed framework can be naturally extended to a vector of responses.

To provide the risk- and science-based production process understanding and guide the reliable process development, we need to correctly quantify all sources of uncertainties. There are two types of uncertainty: (1) bioprocess inherent stochastic uncertainty from CPPs/CQAs and other uncontrolled variables (i.e., randomness of $\mathbf{X}$ and $\mathbf{e}$ ), which can be reduced by the identification of missed CPPs and tighter specification of selected CPPs; and (2) model uncertainty (MU) (i.e., the estimation uncertainty of bioprocess model coefficients $\boldsymbol{\theta}$ ), which can be reduced by collecting

![img-0.jpeg](img-0.jpeg)

FIGURE 1 An illustration of general biomanufacturing process and fish-bone representation (Walsh, 2013).
"most informative" process observations. Correctly quantifying all sources of uncertainty can facilitate learning, guide risk elimination/control, and improve robust, automatic, and reliable bioprocess decision making.

# 3.1 | Review of Game Theory based Sensitivity Measure - Shapley Value 

In game theory, the Shapley value (SV) was originally introduced to evaluate the contribution of a player in a cooperative game Shapley (1953). A cooperative game is defined as a set of players $\mathcal{K}=\{1,2, \ldots, K\}$, with a function $c(\cdot)$ that maps a subset of players to its corresponding payoff, $c: \mathbb{Z}^{\mathcal{K}} \rightarrow \mathbb{R}$ with $c(\varnothing)=0$, where $\mathbb{Z}^{\mathcal{K}}$ denotes the power set of $\mathcal{K}$ (i.e., the set of all subsets of $\mathcal{K}$ ). Thus, $c(\mathcal{J})$ characterizes the total gain that the players in subset $\mathcal{J} \subset \mathcal{K}$ can obtain by cooperation. The SV of player $k \in \mathcal{K}$ with respect to $c(\cdot)$ is defined by

$$
\operatorname{Sh}_{k}=\sum_{\mathcal{J} \subset \mathcal{K} /\{k\}} \frac{(K-|\mathcal{J}|-1)!|\mathcal{J}|!}{K!}[c(\mathcal{J} \cup\{k\})-c(\mathcal{J})]
$$

where $K=|\mathcal{K}|$ is the total number of players and $|\mathcal{J}|$ is the size of subset $\mathcal{J}$ from $\mathcal{K} /\{k\}$. This SV can be interpreted as the average incremental payoff by including player $k$ over all possible cooperation group formations, i.e., $\mathcal{J} \subset \mathcal{K} /\{k\}$, and $S h_{k}$ can be used to measure the contribution of the player $k$. This assessment approach satisfies the "efficiency property" that the sum of the SVs of all players equals the gain of the grand coalition, i.e., $c(\mathcal{K})=\sum_{k=1}^{K} S h_{k}$.

The Shapley value was recently introduced for global sensitivity analysis to measure the variance of output contributed by each random input (Owen, 2014). Denote the set of inputs as $\mathbf{U}_{\mathcal{K}}=\left\{U_{1}, U_{2}, \ldots, U_{K}\right\}$, and model the output $V=\eta\left(\mathbf{U}_{\mathcal{K}}\right)$ as a function $\eta(\cdot)$ of the inputs, accounting for their interactions. Two most commonly used variance-based sensitivity measures are: (1) the first-order effect $O_{k} \equiv \operatorname{Var}(V)-\mathrm{E}\left[\operatorname{Var}\left(V \mid U_{k}\right)\right]$ that considers the variance reduction when we fix $U_{k}$; and (2) the total effect $T_{k} \equiv \mathrm{E}\left[\operatorname{Var}\left(V \mid \mathbf{U}_{-k}\right)\right]$ that considers the expected remaining variance when all other factors, denoted by $\mathbf{U}_{-k}$, are fixed. However, both measures fail to appropriately quantify

the sensitivity or variance contribution when there exist probabilistic interdependence among inputs and process structural interaction (Song et al., 2016).

Built on the SV from game theory, given a cooperative game with inputs $\mathbf{U}_{\mathcal{K}}$ as the players and the payoff as the incremental variance in output $V$ induced by any index subset $\mathcal{J} \subset \mathcal{K}$, one can define the payoff function as

$$
c(\mathcal{J})=\operatorname{Var}(V)-\mathrm{E}\left[\operatorname{Var}\left[V \mid \boldsymbol{U}_{\mathcal{J}}\right]\right] \text { or } c(\mathcal{J})=\mathrm{E}\left[\operatorname{Var}\left[V \mid \boldsymbol{U}_{-\mathcal{J}}\right]\right]
$$

Thus, Owen (2014) introduced a new SV-based sensitivity measure, with $\operatorname{Sh}_{U_{k}, V}$ computed by Equations (1) and (2). In this paper, we use $c(\mathcal{J})=\mathrm{E}\left[\operatorname{Var}\left[V \mid \boldsymbol{U}_{-\mathcal{J}}\right]\right]$ in Equation (1), which can simplify the computation of the contribution from any random input $U_{k}$ on the output variance $\operatorname{Var}(V), \operatorname{Sh}_{U_{k}, V}=\operatorname{Sh}_{k}$. The SV-based sensitivity analysis overcomes the limitations of first-order effect and total effect measures by accounting for the interdependence of inputs and process interactions. The variance of output $V$ can be decomposed into the contribution from each random input $U_{k}$ and we can define the criticality as the proportion of $\operatorname{Var}(V)$ contributed from $U_{k}$, denoted by $p_{U_{k}, V}$,

$$
\operatorname{Var}(V)=\sum_{k=1}^{K} \operatorname{Sh}_{U_{k}, V} \text { and } p_{U_{k}, V}=\frac{\operatorname{Sh}_{U_{k}, V}}{\operatorname{Var}(V)}
$$

The main benefits of SV over first-order and total effect sensitivity measures include: (1) the uncertainty contributions sum up to total variance of output; and (2) SV can automatically account for probabilistic dependence and structural interactions occurring in the complex production process.

# 3.2 | Summary of Proposed Interpretable Bioprocess Model, Risk and Sensitivity Analyses for Integrated Bioprocess Stability Control 

Fig. 2 provides the flowchart of proposed risk and sensitivity analyses framework, which can accelerate learning of the end-to-end production process and guide the development of stable biomanufacturing. Parts I and II focus on modeling and reducing of process stochastic uncertainty. Part III focuses on analyzing and controlling the model risk. By exploring the causal relationships and interactions of CPPs/CQAs of raw materials/in-process materials/product within and between different process modules, in Section 4, we develop ontology based data integration and create an interpretable Bayesian network (BN) based bioprocess semantic probabilistic knowledge graph, specified by the model coefficients $\boldsymbol{\theta}$. This knowledge graph can characterize the risk- and science-based understanding of integrated bioprocess and quantify the causal interdependencies of inputs ( $\mathbf{X}, \mathbf{e}$ ) and output $Y$. It is interpretable and extendable, which can support flexible process modular design, incorporate the existing mechanisms from different modules and operation units, quantify the bioprocess causal interdependencies, and greatly reduce the dimensionality of bioprocess design space to guide the decision making.

Building on this interpretable probabilistic knowledge graph, in Section 5, we develop the SV-based process risk and sensitivity analyses studying stochastic uncertainty, and derive variance decomposition to quantify the contribution from each random input,

$$
\operatorname{Var}(Y \mid \boldsymbol{\theta})=\sum_{X_{k}} \operatorname{Sh}_{X_{k}, Y}(\boldsymbol{\theta})+\sum_{e_{k}} \operatorname{Sh}_{e_{k}, Y}(\boldsymbol{\theta})
$$

where Shapley values, $\operatorname{Sh}_{X_{k}, Y}(\boldsymbol{\theta})$ and $\operatorname{Sh}_{e_{k}, Y}(\boldsymbol{\theta})$, measure the contributions from any CPP/CQA, $X_{k} \in \mathbf{X}$, and residual factor, $e_{k} \in \mathbf{e}$ (representing the impact of remaining uncontrolled factors on the CQA $X_{k}$ ), to the output variance

![img-1.jpeg](img-1.jpeg)

FIGURE 2 The flowchart of proposed biomanufacturing process risk and sensitivity analyses framework.
$\operatorname{Var}(Y \mid \boldsymbol{\theta})$. For any input factor $W_{k}$ (i.e., either $X_{k}$ or $e_{k}$ ), the criticality, $p_{W_{k}, Y}(\boldsymbol{\theta}) \equiv \operatorname{Sh}_{W_{k}, Y}(\boldsymbol{\theta}) / \operatorname{Var}(Y \mid \boldsymbol{\theta})$, can be used to identify the bottlenecks that contribute the most to $\operatorname{Var}(Y)$, and guide the process specifications to efficiently improve production process stability. The CPPs/CQAs $X_{k}$ with high criticality requires more restrict stability control, while the residual $e_{k}$, with high impact on the output variance, can guide us to identify the ignored CPPs. Since the Shapley value (SV) based sensitivity analysis is developed based on game theory, its combination with bioprocess probabilistic knowledge graph, accounting for the complex causal interdependencies, can correctly assess the risk effect from each set of random input factors on the output variation.

The "correct" process model coefficients, denoted by $\boldsymbol{\theta}^{c}$, characterizing the bioprocess underlying probabilistic interdependence, is unknown and estimated by using the real-world process data, denoted by $X$. Given limited historical process data, the model risk or estimation uncertainty can have a large impact on the bioprocess risk and sensitivity analyses. Since the estimation uncertainty of model coefficients at different parts of bioprocess can be different and interdependent, the model uncertainty (MU) is quantified with the joint posterior distribution $p(\boldsymbol{\theta} \mid X)$. We further develop the SV-based sensitivity analysis to study the impact of model uncertainty from each part of process in Section 6, which can guide the "most informative" data collection to reduce the impact from model risk and efficiently improve the accuracy of bioprocess risk analysis and critiality assessment, especially for those factors contributing the most to the output variance. For any random input $W_{k}$, the Shapley value $\operatorname{Sh}_{W_{k}, Y}$ is estimated with error, which can be contributed by the model coefficients located along the paths propagating the uncertainty of $W_{k}$ to the output $Y$, denoted by $\boldsymbol{\theta}\left(W_{k}, Y\right)$. We introduce the BN-SV-MU sensitivity analysis to provide the comprehensive study over the impact of model uncertainty,

$$
\operatorname{Var}^{c}\left[\operatorname{Sh}_{W_{k}, Y} \mid X\right]=\sum_{\theta_{f} \in \boldsymbol{\theta}\left(W_{k}, Y\right)} \operatorname{Sh}_{\theta_{f}}^{c}\left[\operatorname{Sh}_{W_{k}, Y}\left(\overline{\boldsymbol{\theta}}\left(W_{k}, Y\right)\right) \mid X\right]=\sum_{\theta_{f} \in \boldsymbol{\theta}\left(W_{k}, Y\right)} \operatorname{Sh}_{\theta_{f}}^{c}\left[\operatorname{Sh}_{W_{k}, Y} \mid X\right]
$$

where the subscript " $*$ " represents any measure calculated based on the posterior $p(\boldsymbol{\theta} \mid \mathcal{X})$ and $\operatorname{Sh}_{\theta_{\ell}}^{*}[\cdot \mid \mathcal{X}]$ measures the contribution from coefficient estimation uncertainty of $\theta_{\ell} \in \boldsymbol{\theta}\left(W_{k}, Y\right)$. In the proposed interpretable bioprocess model, $\theta_{\ell}$ can be interpreted as certain mechanistic coefficients (e.g., cell growth rate in the cell culture). Thus, the decomposition in (3) provides the detailed information on how the model uncertainty of each part of integrated production process influences the estimation uncertainty of $\mathrm{Sh}_{W_{k}, Y}$.

To illustrate the key ideas of the proposed bioprocess risk and sensitivity analyses, we use a simplified monoclonal antibody (mAbs) drug substance production example, including main fermentation, centrifuge, chromatograph, and filtration; see the interactions in Fig. 3. We consider the dominant CPPs/CQAs in each step, while the impacts of remaining factors are included in $\mathbf{e}$. We are interested in the variance contribution (or criticality) from each CPP to drug substance protein content $Y=X_{20}$, and also account for the impact of model uncertainty on criticality assessment.
![img-2.jpeg](img-2.jpeg)

FIGURE 3 An example illustration visualization of the integrated bioprocess sensitivity framework for criticality assessment and model uncertainty.

The results of risk and sensitivity analyses can be visualized along the graph model for this bioprocess example; see Fig. 3. The process knowledge graph model is specified by coefficients, $\boldsymbol{\theta}=\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)$, where $\boldsymbol{\mu}$ and $\boldsymbol{v}^{2}$ are the mean and variance vectors of all factors (listed in the table), and $\boldsymbol{\beta}$ quantifies the effects from parents' nodes on each child node. The darkness of nodes indicates the criticality level of process factors, which can guide the better bioprocess specification. The results show that $X_{4}$ contributes to $55 \%$ variance of $X_{20}$. In addition, the darkness of directed edges and circle boundaries indicates the distribution of model uncertainty in the process. For instance, the variance of dissolved oxygen in bioreactor, $v_{4}^{2}$, has dominant model uncertainty impact on the estimation uncertainty of criticality $p_{X_{4}, Y}$, which suggests additional data should be collected to improve the estimation of $v_{4}^{2}$. We will revisit this example and use it to study the performance of proposed framework in Section 7.1.

# 4 | INTERPRETABLE BIOPROCESS PROBABILISTIC MODEL DEVELOPMENT 

We develop an interpretable bioprocess probabilistic model, which can be extendable to end-to-end biomanfacturing supply chain and support evidence-based biopharmaceutical production process development. The model can incorporate the existing mechanism models from each module and unit operation, and facilitate the learning from distributed and heterogeneous process data. In this section, we develop a Bayesian network (BN) based interpretable

bioprocess probabistic knowledge graph, which can characterize the complex CPPs/CQAs causal interdependencies and support flexible modular biomanfuacturing development.

By exploring the causal relationships and interactions, we consider bioprocess ontology-based data integration, which can connect all distributed and heterogeneous data collected from bioprocess; see more description in Online Appendix A. This relational graph can enable the connectivity of end-to-end process. Nodes represent factors (i.e., CPPs/CQAs, media feed, bioreactor operating conditions, other uncontrolled factors) impacting the process outputs, and the directed edges model the causal relationships. Within each module, which can be each phase of cell culture process (such as cell growth and production phases) or each unit operation, we can model complex interactions, e.g., biological/physical/chemical interactions. In the relational graph, the shaded nodes represent the variables with real-world observations, including the testing and sensor monitoring data of CPPs/CQAs for raw materials, operation conditions, and intermediate/final drug products. The unshaded nodes represent variables without observations and residuals, including quality status of intermediate and final drug products, and other uncontrollable factors (e.g., contamination) introduced during the process unit operations. Since bio-products have very complex structures, we cannot observe the underlying complete quality status and the monitoring of CQAs can carry partial information. Building on the bioprocess relational graph, we develop a BN based probabilistic graphical model composing of random CPPs/CQAs/residuals factors and their conditional dependencies via directed edges. It can characterize the probabilistic causal interdependencies among all factors of integrated bioprocess.

To make it easy to follow, we first provide a simple illustration example of cell culture process, including two phases, to present the key ideas of modular bioprocess modeling, and then develop the complete probabilistic knowledge graph model for general integrated bioprocess. Specifically, we use a simple bioreactor fermentation example with two phases (i.e., cell growth and production phases; see Fig. 4) to illustrate the probabilistic graphical model development. It is based on the causal relationships and interactions between CPPs and CQAs. Each node represents a CPP/CQA with a random variable $X$ modeling its variability. Each directed edge represents the causal impact of parent node $X_{i}$ on child node $X_{j}$. The pattern-fill nodes $\left(X_{1}, X_{2}, X_{3}\right)$ represent the CPPs. The solid fill nodes $\left(X_{6}, X_{7}\right)$ represent the monitored CQAs of intermediate materials and drug products. The nodes $X_{4}$ and $X_{5}$ represent the underlying status of working cells after cell growth phase and the protein/impurity structure after cell production phase. The CQAs $X_{6}$ and $X_{7}$ represent the partial information of quality variables $X_{4}$ and $X_{5}$. Except the CPPs $X_{1}, X_{2}, X_{3}$, the impacts from other uncontrolled factors introduced during two phases of cell culture are modeled through $e_{4}^{\prime}$ and $e_{5}^{\prime}$.
![img-3.jpeg](img-3.jpeg)

FIGURE 4 Left: knowledge relational graph; Right: simplified knowledge graph.

Since it is hard to uniquely specify the underlying cells/proteins with very complex structures, $X_{4}$ and $X_{5}$ are

hidden, which can lead to an identification issue. Typically, the non-identifiable BN with hidden nodes is transformed to the equivalent BN by structural simplification to avoid analytical issues (see Chapter 19 in Koller and Friedman (2009)). Thus, we simplify and transform the relational graphical model to a graph without hidden nodes, depicted in the right panel of Fig. 4. The new residual $e_{6}$ in updated graph accounts for both original residual $e_{4}^{\prime}$ and also the uncertainty of underlying cell health status, $X_{4}$, impacting on CQA $X_{6}$, similar for new residual $e_{7}$. According to the right plot in Fig. 4, the sources of bioprocess stochastic uncertainty impacting on the variability of $X_{7}$ include CPPs, $\left(X_{1}, X_{2}, X_{3}\right)$, and other factors with the impact represented by residuals ( $e_{6}, e_{7}$ ). Thus, we have CPPs $X_{1}, X_{2}$ as inputs and CQA $X_{6}$ as output for the first cell growth phase, and have CQA $X_{6}$ and CPP $X_{3}$ as inputs and $X_{7}$ as output for the second protein production phase. To study the impact of each CPP on the CQA of interest (i.e., $X_{6}$ and $X_{7}$ ), we can decompose the variance of $X_{6}$ and $X_{7}$ into the contributions from $X_{1}, X_{2}$ and $X_{3}$, and remaining parts coming from $e_{6}$ and $e_{7}$; see the process risk and sensitivity analyses in Section 5. In this way, we can identify the main sources of uncertainty and quantify their impacts, which can guide the CPPs/CQAs specifications and the quality control to improve the product quality stability.

Now we describe the BN-based bioprocess model for general situations. Suppose that the integrated bioprocess can be represented by a probabilistic graphical model with $m+1$ nodes: $m$ process factors (denoted by $\mathbf{X}$ ) and a single response, denoted by $Y$, such as the impurity concentration or protein content. Let the first $m^{p}$ nodes representing CPPs $\boldsymbol{X}^{p}=\left\{X_{1}, X_{2}, \ldots, X_{m^{p}}\right\}$, the next $m^{a}$ nodes representing CQAs $\boldsymbol{X}^{a}=\left\{X_{m^{p}+1}, X_{m^{p}+2}, \ldots, X_{m}\right\}$, and the last node representing the response $Y \triangleq X_{m+1}$ with $m=m^{p}+m^{a}$. The modular bioprocess probabilistic knowledge graph can be modeled by marginal and conditional distributions of each node as follows:

$$
\begin{aligned}
X_{k} & \sim N\left(\mu_{k}, v_{k}^{2}\right) \text { for } \mathrm{CPP} X_{k} \text { with } k=1,2, \ldots, m^{p} \\
X_{k} & =f\left(P a\left(X_{k}\right) ; \boldsymbol{\theta}_{k}\right)+e_{k} \text { for } \mathrm{CQA} X_{k} \text { with } k=m^{p}+1, \ldots, m+1
\end{aligned}
$$

where $N\left(u, v^{2}\right)$ denotes the normal distribution with mean $u$ and variance $v^{2}$, and $P a\left(X_{k}\right)$ denotes the parent nodes of $X_{k}$. By applying central limit theory (CLT), we assume that the residual $e_{k} \sim N\left(0, v_{k}^{2}\right)$ with the conditional variance $v_{k}^{2} \equiv$ $\operatorname{Var}\left[X_{k} \mid P a\left(X_{k}\right)\right]$. Since the amount of real-world bioprocess batch data is often very limited, Gaussian distribution is used to model the variability of each variable or node, which is often used in the existing biopharmaceutical studies (see for example Coleman and Block (2006)). It also makes the process risk and sensitivity analyses tractable.

The proposed probabilistic knowledge graph is a hybrid model of integrated bioprocess, which can leverage the existing mechanisms and learn from real-world process data. Basically, the prior of the function $f(\cdot)$ in a generalized regression model (5) can be specified based on the existing knowledge on underlying bioprocess mechanisms (e.g., biophysicochemical kinetics) within each module of bioprocess; see for example Kyriakopoulos et al. (2018); Lu et al. (2018); Doran (1995). The unknown model coefficients $\boldsymbol{\theta}_{k}$ (e.g., cell growth rate, media consumption rate) need be estimated from process data. In this paper, we consider linear function accounting for the main effects, i.e.,

$$
X_{k}=\mu_{k}+\sum_{X_{j} \in P a\left(X_{k}\right)} \beta_{j k}\left(X_{j}-\mu_{j}\right)+e_{k} \text { for CQA } X_{k} \text { with } k=m^{p}+1, \ldots, m+1
$$

where the coefficient $\beta_{j k}$ can be used to measure the effect from the parent node $X_{j}$ to child node $X_{k}$.
Here, we use some illustrative examples to briefly show how the proposed Bayesian network based process probabilistic model allows us to incorporate the existing bioprocess mechanisms. We first consider the cell exponential growth mechanism for the fermentation step, $x=x_{0} e^{\mu t}$, where $x_{0}$ and $x$ denote the starting and ending cell densities, and $\mu$ is the unknown growth rate. This is a commonly used mechanism model in biomanufacturing industry; see more

information in Doran (2013). Suppose that there is a fixed cell culture duration $t$. By doing the log transformation and setting $X_{k}=\log \left(x_{0}\right), X_{k+1}=\log (x)$ and $\beta_{0}=\mu t$, we can take the exponential growth mechanism as prior and get the hybrid probabilistic model for the exponential growth phase in fermentation or cell culture process, $X_{k+1}=\beta_{0}+X_{k}+e_{k}$, where $e_{k}$ represents the residual term characterizing the integrated effect from many other factors and it follows a Gaussian distribution by following CLT. Notice that it is a special case of BN-based process model (6). The similar idea can be applied to the situations where we have PDE/ODE-based bioprocess kinetics mechanism models,

$$
\frac{d}{d t} x(t)=f\left(x(t) ; \theta_{t}\right) \approx \frac{x\left(t_{k+1}\right)-x\left(t_{k}\right)}{t_{k+1}-t_{k}}=f\left(x\left(t_{k}\right) ; \theta_{t_{k}}\right)
$$

where $x(t)$ can represent the concentrations of protein and metabolite waste at time $t$ and $\theta_{t}$ can denote the nonstationary growth rate. We can take the existing mechanism model as the prior knowledge of production process. By applying the finite difference on the gradient $d x(t) / d t$ and first-order Taylor approximation on function $f(\cdot)$, we can construct a probabilistic hybrid model matching with the formula in Equation (6), which can leverage the information from existing PDE/ODE-based bioprocess kinetics mechanism models. This approximation can be very accurate if the data are collected from real-time production process sensor monitoring with high sampling frequency.

The complex bioprocess CPPs/CQAs causal interdependencies are characterized by the BN-based probabilistic knowledge graph. Given the model parameters $\boldsymbol{\theta}=\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)$ with mean $\boldsymbol{\mu}=\left(\mu_{1}, \ldots, \mu_{m+1}\right)^{\top}$, conditional variance $\boldsymbol{v}^{2}=\left(v_{1}^{2}, \ldots, v_{m+1}^{2}\right)^{\top}$, and linear coefficients $\boldsymbol{\beta}=\left\{\beta_{j k} ; k=m^{p}+1, \ldots, m+1\right.$ and $\left.X_{j} \in P a\left(X_{k}\right)\right\}$, the conditional distribution for each CQA node $X_{k}$ becomes,

$$
p\left(X_{k} \mid P a\left(X_{k}\right)\right)=N\left(\mu_{k}+\sum_{X_{j} \in P a\left(X_{k}\right)} \beta_{j k}\left(X_{j}-\mu_{j}\right), v_{k}^{2}\right) \text { for } k=m^{p}+1 \ldots, m+1
$$

For any CPP node $X_{k}$ without parent nodes, $P a\left(X_{k}\right)$ is an empty set and $P\left(X_{k} \mid P a\left(X_{k}\right)\right)$ is just the marginal distribution $P\left(X_{k}\right)$ in (4). Therefore, the joint distribution characterizing the interdependencies of CPPs and CQAs involved in the production process can be written as $p\left(X_{1}, X_{2}, \ldots, X_{m+1}\right)=\prod_{k=1}^{m+1} p\left(X_{k} \mid P a\left(X_{k}\right)\right)$.

# 5 | PROCESS RISK AND SENSITIVITY ANALYSES 

Given the bioprocess probabilistic knowledge graph specified by the coefficients $\boldsymbol{\theta}=\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)$, we develop the BN-SV based sensitivity analysis for integrated production process and quantify the criticality of each random input factor measuring its contribution to the output variance $\operatorname{Var}\left(X_{m+1}\right)$. This study can guide the CPPs/CQAs specification and improve the production process stability. To make it easy to follow, we start with a simple illustration example, provide the general process risk and sensitivity analyses, and then present the algorithm at the end of this section.

We again use the simple example in Fig. 4 to illustrate the results of proposed BN-SV based bioprocess risk and sensitivity analyses, which can decompose the output variance of protein/impurity concentration $X_{7}$ after fermentation process to each random input - including $X_{1}, X_{2}, X_{3}, e_{6}, e_{7}$ - as

$$
\operatorname{Var}\left(X_{7} \mid \boldsymbol{\theta}\right)=\underbrace{\left(\beta_{16} \beta_{67}\right)^{2} v_{1}^{2}}_{\text {contribution from } X_{1}}+\underbrace{\left(\beta_{26} \beta_{67}\right)^{2} v_{2}^{2}}_{\text {contribution from } X_{2}}+\underbrace{\beta_{37}^{2} v_{3}^{2}}_{\text {contribution from } X_{3}}+\underbrace{\beta_{67}^{2} v_{6}^{2}}_{\text {contribution from } e_{6}}+\underbrace{v_{7}^{2}}_{\text {contribution from } e_{7}}
$$

The variance contribution from each random input, denoted by $W_{k}$ (i.e., $X_{1}, X_{2}, X_{3}, e_{6}, e_{7}$ ), depends on its variance $v_{k}^{2}$

and the product of coefficients $\boldsymbol{\beta}$ located along the paths propagating the uncertainty from $W_{k}$ to the output $X_{7}$; see Fig. 5. The darker blue filled node (i.e., cell growth phase CPP $X_{2}$, feed rate) contributes more to the output variance and has higher criticality. Thus, to efficiently reduce the output variance, it requires more restrictive stability control. The high impact of $e_{7}$ (with darker color) can guide us to identify unrecognized or missed CPPs.
![img-4.jpeg](img-4.jpeg)

FIGURE 5 A simple example to illustrate BN-SV based process risk and sensitivity analysis.

This simple example illustrates that the proposed production process BN-SV risk and sensitivity analyses and the CPPs/CQAs criticality assessment are based on the bioprocess probabilistic knowledge graph, characterizing the complex CPPs/CQAs causal interdependencies and accounting for all sources of process inherent uncertainty, which can (1) guide the process specifications; (2) improve the product quality consistency and bioprocess stability; and (3) advance the risk- and science-based understanding on bioprocess.

Now we present the general process risk and sensitivity analyses. We first derive the Shapley value (SV) quantifying the contribution of each random input factor from CPPs $\mathbf{X}^{p}$ and other factors e to $\operatorname{Var}\left(X_{m+1}\right)$, which accounts for cases with dependent input factors. According to the Gaussian BN model presented in (4) and (6), we can write

$$
X_{m+1}=\mu_{m+1}+\sum_{k=1}^{m^{p}} \gamma_{k, m+1}\left(X_{k}-\mu_{k}\right)+\sum_{k=m^{p}+1}^{m+1} \gamma_{k, m+1} e_{k}
$$

where the weight coefficient of any CPP $X_{k}$ to CQA $X_{n}$ with $k \leq m^{p}<n \leq m+1$,

$$
\gamma_{k n}=\beta_{k n}+\sum_{m^{p}<t<n} \beta_{k t} \beta_{t n}+\sum_{m^{p}<t_{1}<t_{2}<n} \beta_{k t_{1}} \beta_{t_{1} t_{2}} \beta_{t_{2} n}+\ldots+\beta_{k, m^{p}+1} \beta_{m^{p}+1, m^{p}+2} \ldots \beta_{n-1, n}
$$

the weight coefficient of any $e_{k}$ to a CQA node $X_{n}$ with $m^{p}<k<n \leq m+1$,

$$
\gamma_{k n}=\beta_{k n}+\sum_{k<t<n} \beta_{k t} \beta_{t n}+\sum_{k<t_{1}<t_{2}<n} \beta_{k t_{1}} \beta_{t_{1} t_{2}} \beta_{t_{2} n}+\ldots+\beta_{k, k+1} \beta_{k+1, k+2} \ldots \beta_{n-1, n}
$$

and $\gamma_{n n}=1$ for any $n$; see the derivation for (8) in Appendix B. The weight coefficient $\gamma_{k n}$ is the product sum of $\boldsymbol{\beta}$ located along the paths from node $X_{k}$ to node $X_{n}$ in the graph model. Let $\boldsymbol{W}=\left\{X_{1}, \ldots, X_{m^{p}}, e_{m^{p}+1}, \ldots, e_{m+1}\right\} \triangleq$ $\left\{W_{1}, W_{2}, \ldots, W_{m+1}\right\}$ represent all random input factors, with the index set $\mathcal{K}=\{1,2, \ldots, m+1\}$. Then, the SV for the $k$-th factor $W_{k}$ is,

$$
\operatorname{Sh}_{W_{k}, X_{m+1}}=\sum_{\mathcal{J} \subset \mathcal{K} /\{k\}} \frac{(m-|\mathcal{J}|)!|\mathcal{J}|!}{(m+1)!}[c(\mathcal{J} \cup\{k\})-c(\mathcal{J})]
$$

Based on (8), we compute the cost function,

$$
c(\mathcal{J})=\mathrm{E}\left[\operatorname{Var}\left[X_{i} \mid \boldsymbol{W}_{-\mathcal{J}}\right]\right]=\sum_{k \in \mathcal{J}} \gamma_{k, m+1}^{2} \operatorname{Var}\left(W_{k}\right)+2 \sum_{k_{1}<k_{2} \in \mathcal{J}} \gamma_{k_{1}, m+1} \gamma_{k_{2}, m+1} \operatorname{Cov}\left(W_{k_{1}}, W_{k_{2}}\right)
$$

The random input factors, $\boldsymbol{W}=\left(X_{1}, \ldots, X_{m^{p}}, e_{m^{p}+1}, \ldots, e_{m+1}\right)$, including CPPs and residual terms introduced at each CQA nodes, are often independent as the real biomanufacturing process specification is often based on each CPP or CQA. To make the proposed framework general, we consider the potential interdependence between some inputs $W_{k_{1}}$ and $W_{k_{2}}$ with $k_{1} \neq k_{2}$, and the covariance $\operatorname{Cov}\left(W_{k_{1}}, W_{k_{2}}\right)$ can be estimated by using the process data.

Then, for each $W_{k}$ and $\mathcal{J} \subset \mathcal{K} /\{k\}$, we can obtain

$$
c(\mathcal{J} \cup\{k\})-c(\mathcal{J})=\gamma_{k, m+1}^{2} \operatorname{Var}\left(W_{k}\right)+2 \sum_{\ell \in \mathcal{J}} \gamma_{k, m+1} \gamma_{\ell, m+1} \operatorname{Cov}\left(W_{k}, W_{\ell}\right)
$$

Given the BN-based bioprocess knowledge graph model parameters $\boldsymbol{\theta}$, by applying (1), we can derive the Shapley value, $\operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta})$, characterizing the contribution from any input factor $W_{k}$ to the output variance,

$$
\operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta})=\gamma_{k, m+1}^{2} \operatorname{Var}\left(W_{k}\right)+\sum_{\ell \neq k} \gamma_{k, m+1} \gamma_{\ell, m+1} \operatorname{Cov}\left(W_{k}, W_{\ell}\right)
$$

The derivation of (11) is provided in Appendix C. Therefore, we can decompose the variance of output $X_{m+1}$ and estimate the contribution from each random input from $\mathbf{X}^{p}$ and $\mathbf{e}$,

$$
\operatorname{Var}\left(X_{m+1} \mid \boldsymbol{\theta}\right)=\sum \operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta})=\sum_{k=1}^{m^{p}} \operatorname{Sh}_{X_{k}, X_{m+1}}(\boldsymbol{\theta})+\sum_{k=m^{p}+1}^{m+1} \operatorname{Sh}_{e_{k}, X_{m+1}}(\boldsymbol{\theta})
$$

Equation (12) can be used to identify the dominant factors in $\mathbf{X}^{p}$ and $\mathbf{e}$ contributing the most to the output variance, which can guide the CPPs identification and process specification to improve the process stability and quality consistency. As a result, the criticality of any input factor $W_{k}$ can be calculated as $p_{W_{k}, X_{m+1}}(\boldsymbol{\theta}) \equiv \operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta}) / \operatorname{Var}\left(X_{m+1} \mid \boldsymbol{\theta}\right)$. Notice that for any independent input factor $W_{k}$, the SV in Equation (11) is reduced to $\operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta})=\gamma_{k, m+1}^{2} v_{k}^{2}$. Under the case that all input factors $\boldsymbol{W}$ are mutually independent, the variance decomposition Equation (12) can be written as $\operatorname{Var}\left(X_{m+1} \mid \boldsymbol{\theta}\right)=\sum \gamma_{k, m+1}^{2} v_{k}^{2}$, which gives the example results in Equation (7).

This risk and sensitivity analyses can be applied to any part of production process including one or multiple modules. Under this situation, the input factors $\boldsymbol{W}$ include those nodes without parent node within the considered range of production (i.e., CPPs, CQAs or uncontrolled factors), and output of interest $X_{i}$ is certain CQA at the end of the procedure. For example, in Fig. 5, we consider the subgraph, including $\left\{X_{3}, X_{6}, X_{7}\right\}$, for cell production phase with the starting CQA $X_{6}$ carrying the information from previous cell growth phase. We can study the impacts of $X_{6}$ and CPP $X_{3}$ on the variability of CQA $X_{7}$. The SV of any input $W_{k}$ and the variance decomposition of $X_{i}$, still follow Equations (11) and (12) by replacing the output $X_{m+1}$ with $X_{i}$. The criticality of $W_{k}$ on $X_{i}$ can be measured by proportion $p_{W_{k}, X_{i}}(\boldsymbol{\theta})=\operatorname{Sh}_{W_{k}, X_{i}}(\boldsymbol{\theta}) / \operatorname{Var}\left(X_{i} \mid \boldsymbol{\theta}\right)$.

Given the BN parameters $\boldsymbol{\theta}$, we summarize the procedure for production process BN-SV based sensitivity analysis in Algorithm 1, in which we consider several consecutive operation steps, and our objective is to quantify the contribution of each random factor in $\boldsymbol{W}$ to $\operatorname{Var}\left(X_{i} \mid \boldsymbol{\theta}\right)$.

```
Algorithm 1: Procedure for Production Process BN-SV based Sensitivity Analysis
    Input: BN parameters \(\boldsymbol{\theta}\), group of input factors \(\boldsymbol{W}\), response node \(X_{m+1}\).
    Output: Variance decomposition of \(X_{i}\) in terms of all random inputs within \(\boldsymbol{W}\).
    (1) Calculate the Shapley value \(\operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta})\) by using Equation (11), which measures the contribution from \(W_{k}\) to the
    variance of response CQA \(X_{m+1}\);
    (2) Provide the variance decomposition of \(\operatorname{Var}\left(X_{m+1} \mid \boldsymbol{\theta}\right)\) by using Equation (12), and obtain the criticality of \(W_{k}\) on the
    variance of \(X_{m+1}: p_{W_{k}, X_{m+1}}(\boldsymbol{\theta})=\operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta}) / \operatorname{Var}\left(X_{m+1} \mid \boldsymbol{\theta}\right)\).
```


# $6 \mid$ SENSITIVITY ANALYSIS FOR MODEL RISK REDUCTION 

Since the underlying true process model coefficients $\boldsymbol{\theta}^{c}$ are unknown, given finite real-world data $\mathcal{X}$, there exists the model uncertainty (MU) characterizing our limited knowledge on the probabilistic interdependence of integrated bioprocess. To study the impact of MU on the production process risk and sensitivity analyses for stochastic uncertainty and further assess CPPs/CQAs criticality, we propose the BN-SV-MU based uncertainty quantification and sensitivity analysis, which can guide the process monitoring and "most informative" data collection. In Section 6.1, we develop the posterior $p(\boldsymbol{\theta} \mid \mathcal{X})$ and a Gibbs sampler to generate posterior samples, $\overline{\boldsymbol{\theta}}^{(b)} \sim p(\boldsymbol{\theta} \mid \mathcal{X})$ with $b=1,2, \ldots, B$, quantifying the model uncertainty, and then we quantify the overall impact of model uncertainty on the process risk analysis and CPPs/CQAs criticality assessment. In Section 6.2, we propose the BN-SV-MU based sensitivity analysis, which can study the impact of each model coefficient(s) estimation uncertainty on the process risk analysis and criticality assessment; see the result visualization in Fig. 3.

### 6.1 | Bayesian Learning and Model Uncertainty Quantification

We consider the case with $R$ batches of complete production process data, denoted as $\mathcal{X}=\left\{\left(x_{1}^{(r)}, x_{2}^{(r)}, \ldots, x_{m+1}^{(r)}\right), r=\right.$ $1,2, \ldots, R\}$. Without strong prior information, we consider the following conjugate (vague) prior (with initial hyperparameters giving relatively flat density),

$$
p\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)=\prod_{i=1}^{m+1} p\left(\mu_{i}\right) p\left(v_{i}^{2}\right) \cdot \prod_{i \neq j} p\left(\beta_{i j}\right)
$$

with $p\left(\mu_{i}\right)=N\left(\mu_{i}^{(0)}, \sigma_{i}^{(0) 2}\right), p\left(v_{i}^{2}\right)=\operatorname{Inv}-\Gamma\left(\frac{x_{i}^{(0)}}{2}, \frac{x_{i}^{(0)}}{2}\right)$ and $p\left(\beta_{i j}\right)=N\left(\theta_{i j}^{(0)}, \tau_{i j}^{(0) 2}\right)$, where Inv- $\Gamma$ denotes the inversegamma distribution. Given the data $\mathcal{X}$, by applying the Bayes' rule, we can obtain the posterior distribution

$$
p\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta} \mid \mathcal{X}\right) \propto \prod_{r=1}^{R}\left[\prod_{i=1}^{m+1} p\left(x_{i}^{(r)} \mid x_{p_{\boldsymbol{\beta}}\left(X_{j}\right)}^{(r)}\right)\right] p\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)
$$

quantifying the model uncertainty.
Then, we develop a Gibbs sampler to generate the posterior samples from (14) quantifying the model uncertainty. We derive the conditional posterior for each parameter in $\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)$. Let $\boldsymbol{\mu}_{. . i}, \boldsymbol{v}_{. . j}^{2}$ and $\boldsymbol{\beta}_{. . i j}$ denote the collection of parameters $\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}$ excluding the $i$-th or $(i, j)$-th element. Let $S\left(X_{i}\right)$ denote the set of direct succeeding or child

nodes of node $X_{i}$. We first derive the conditional posterior for the coefficient $\beta_{i j}$,

$$
p\left(\beta_{i j} \mid X, \boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}_{-i j}\right)=N\left(\theta_{i j}^{(R)}, \tau_{i j}^{(R) 2}\right)
$$

where $\theta_{i j}^{(R)}=\frac{\tau_{i j}^{(0) 2} \sum_{r=1}^{R} \alpha_{i}^{(r)} m_{i j}^{(r)}+v_{i}^{2} \theta_{i j}^{(0)}}{\tau_{i j}^{(0) 2} \sum_{r=1}^{R} \alpha_{i}^{(r) 2}+v_{j}^{2}} \quad$ and $\quad \tau_{i j}^{(R) 2}=\frac{\tau_{i j}^{(0) 2} v_{j}^{2}}{\tau_{i j}^{(0) 2} \sum_{r=1}^{R} \alpha_{i}^{(r) 2}+v_{j}^{2}}$ with $\alpha_{i}^{(r)}=x_{i}^{(r)}-\mu_{i}$ and $m_{i j}^{(r)}=$ $\left(x_{j}^{(r)}-\mu_{j}\right)-\sum_{X_{k} \in P \#\left(X_{j}\right) /\left\{X_{i}\right\}} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)$. Then, we derive the conditional posterior for $v_{i}^{2}=\operatorname{Var}\left[X_{i} \mid P \#\left(X_{i}\right)\right]$ with $i=1,2, \ldots, m+1$,

$$
p\left(v_{i}^{2} \mid X, \boldsymbol{\mu}, \boldsymbol{v}_{-i}^{2}, \boldsymbol{\beta}\right)=\operatorname{Inv}-\Gamma\left(\frac{\kappa_{i}^{(R)}}{2}, \frac{\lambda_{i}^{(R)}}{2}\right)
$$

where $\kappa_{i}^{(R)}=\kappa_{i}^{(0)}+R, \lambda_{i}^{(R)}=\lambda_{i}^{(0)}+\sum_{r=1}^{R} u_{i}^{(r) 2}$ and $u_{i}^{(r)}=\left(x_{i}^{(r)}-\mu_{i}\right)-\sum_{X_{k} \in P \#\left(X_{i}\right)} \beta_{k i}\left(x_{k}^{(r)}-\mu_{k}\right)$. After that, we derive the conditional posterior for the mean parameter $\mu_{i}$ with $i=1,2, \ldots, m+1$ for any CPP/CQA,

$$
p\left(\mu_{i} \mid X, \boldsymbol{\mu}_{-i}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right) \propto p\left(\mu_{i}\right) \prod_{r=1}^{R}\left[p\left(x_{i}^{(r)} \mid x_{P \#\left(X_{j}\right)}^{(r)}\right) \prod_{j \in S\left(X_{i}\right)} p\left(x_{j}^{(r)} \mid x_{P \#\left(X_{j}\right)}^{(r)}\right)\right]=N\left(\mu_{i}^{(R)}, \sigma_{i}^{(R) 2}\right)
$$

where $\mu_{i}^{(R)}=\sigma_{i}^{(R) 2}\left[\frac{\mu_{i}^{(0)}}{\sigma_{i}^{(0) 2}}+\sum_{r=1}^{R} \frac{a_{i}^{(r)}}{v_{i}^{2}}+\sum_{r=1}^{R} \sum_{X_{j} \in S\left(X_{i}\right)} \frac{\beta_{i j} c_{i j}^{(r)}}{v_{j}^{2}}\right]$ and $\frac{1}{\sigma_{i}^{(R) 2}}=\frac{1}{\sigma_{i}^{(0) 2}}+\frac{R}{v_{i}^{2}}+\sum_{X_{j} \in S\left(X_{i}\right)} \frac{R \beta_{i j}^{2}}{v_{j}^{2}}$ with $a_{i}^{(r)}=x_{i}^{(r)}-\sum_{X_{k} \in P \#\left(X_{i}\right)} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)$ and $c_{i j}^{(r)}=\beta_{i j} x_{i}^{(r)}-\left(x_{j}^{(r)}-\mu_{j}\right)+\sum_{X_{k} \in P \#\left(X_{j}\right) /\left\{X_{i}\right\}} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)$. The Gibbs sampler iteratively draws the posterior samples of $\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)$ by applying the conditional posterior distributions given in (15), (16), and (17) until convergence (Gelman et al., 2004).

Besides the case with complete production data, we often have additional incomplete batch data. Since the lead time for biopharmaceutical production is lengthy (Otto et al., 2014), we can have some batches in the middle of production. In addition, the bio-drug quality requirements are restricted, especially for human drugs. Following the quality control, we could discard some batches after main fermentation or even in the middle of downstream purification. Thus, we provide the Gibbs sampler (see Algorithm 3) for both cases with complete or mixing data in Appendix D.2.

Next, we study the impact model uncertainty on the bioprocess risk and sensitivity analyses and CPPs/CQAs criticality assessment. Based on Section 5, the contribution from any random input factor $W_{k}$ to the output variance $\operatorname{Var}\left(X_{m+1}\right)$ is measured by the Shapley value, $\operatorname{Sh}_{W_{k}, X_{m+1}}\left(\boldsymbol{\theta}^{c}\right)$. The unknown parameters $\boldsymbol{\theta}^{c}$ specifying the underlying process probabilistic model are estimated by using limited real-world data $\mathcal{X}$. Thus, the estimation uncertainty of the contribution from factor $W_{k}$ can be quantified by the posterior distribution, $\operatorname{Sh}_{W_{k}, X_{m+1}}(\widehat{\boldsymbol{\theta}})$ with $\widehat{\boldsymbol{\theta}} \sim p(\boldsymbol{\theta} \mid \mathcal{X})$. We can use the posterior mean to estimate the expected variance contribution and criticality, $\mathrm{E}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right] \equiv \mathrm{E}_{p(\boldsymbol{\theta} \mid \mathcal{X})}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}}(\widehat{\boldsymbol{\theta}}) \mid \mathcal{X}\right]$ and $\mathrm{E}^{*}\left[p_{W_{k}, X_{m+1}} \mid \mathcal{X}\right] \equiv \mathrm{E}_{p(\boldsymbol{\theta} \mid \mathcal{X})}^{*}\left[p_{W_{k}, X_{m+1}}(\widehat{\boldsymbol{\theta}}) \mid \mathcal{X}\right]$, where $p_{W_{k}, X_{m+1}}(\widehat{\boldsymbol{\theta}})=\operatorname{Sh}_{W_{k}, X_{m+1}}(\widehat{\boldsymbol{\theta}}) / \operatorname{Var}\left(X_{m+1} \mid \widehat{\boldsymbol{\theta}}\right)$. The posterior variance is used to quantify the overall estimation uncertainty induced by model uncertainty, $\operatorname{Var}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right] \equiv \operatorname{Var}_{p(\boldsymbol{\theta} \mid \mathcal{X})}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}}(\widehat{\boldsymbol{\theta}}) \mid \mathcal{X}\right]$ and $\operatorname{Var}^{*}\left[p_{W_{k}, X_{m+1}} \mid \mathcal{X}\right] \equiv$ $\operatorname{Var}_{p(\boldsymbol{\theta} \mid \mathcal{X})}^{*}\left[p_{W_{k}, X_{m+1}}(\widehat{\boldsymbol{\theta}}) \mid \mathcal{X}\right]$.

Since we do not have the closed form solutions, we can estimate the posterior mean and variance of $\operatorname{Sh}\left(W_{k}\right)$ and $p_{W_{k}, X_{m+1}}$ through the sampling approach. By applying the Gibbs sampler in Appendix D, we can generate posterior samples $\widetilde{\boldsymbol{\theta}}^{(b)} \sim p(\boldsymbol{\theta} \mid \mathcal{X})$ with $b=1,2, \ldots, B$. At any $\widetilde{\boldsymbol{\theta}}^{(b)}$, we can compute $\operatorname{Sh}_{W_{k}, X_{m+1}}\left(\widetilde{\boldsymbol{\theta}}^{(b)}\right)$ following the descrip-

tion in Section 5. The expected contribution from $W_{k}$ to the variance of $X_{m+1}$ is estimated by $\widehat{\mathrm{E}}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid X\right]=$ $\operatorname{Sh}_{W_{k}, X_{m+1}}(X)=\frac{1}{B} \sum_{b=1}^{B} \operatorname{Sh}_{W_{k}, X_{m+1}}\left(\widehat{\boldsymbol{\theta}}^{(b)}\right)$. And the overall estimation uncertainty can be estimated by sample variance,

$$
\widehat{\operatorname{Var}}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid X\right]=\frac{1}{B-1} \sum_{b=1}^{B}\left[\operatorname{Sh}_{W_{k}, X_{m+1}}\left(\widehat{\boldsymbol{\theta}}^{(b)}\right)-\operatorname{Sh}_{W_{k}, X_{m+1}}(X)\right]^{2}
$$

Similarly, we can estimate the expected criticality by $\widehat{\mathrm{E}}^{*}\left[p_{W_{k}, X_{m+1}} \mid X\right]=\bar{p}_{W_{k}, X_{m+1}}=\frac{1}{B} \sum_{b=1}^{B} p_{W_{k}, X_{m+1}}\left(\widehat{\boldsymbol{\theta}}^{(b)}\right)$ and estimate the overall estimation uncertainty by

$$
\widehat{\operatorname{Var}}^{*}\left[p_{W_{k}, X_{m+1}} \mid X\right]=\frac{1}{B-1} \sum_{b=1}^{B}\left[p_{W_{k}, X_{m+1}}\left(\widehat{\boldsymbol{\theta}}^{(b)}\right)-\bar{p}_{W_{k}, X_{m+1}}\right]^{2}
$$

# 6.2 | Sensitivity Study for Model Uncertainty 

Since there is often limited process data in biomanufacturing, model uncertainty tends to be large. We propose the BN-SV-MU based sensitivity analysis studying the effect of estimation uncertainty of each model coefficient, which can guide the process monitoring and "most informative" data collection. We provide the CPPs/CQAs criticality estimation uncertainty quantification and BN-SV-MU based sensitivity analysis in Algorithm 2. Specifically, Steps (1)(3) evaluate $\operatorname{Var}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid X\right]$ quantifying the overall estimation uncertainty of $\operatorname{Sh}_{W_{k}, X_{m+1}}$. Steps (4)-(13) further study the impact from each model coefficient estimation uncertainty.

Here we use $\operatorname{Var}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid X\right]$ for illustration and the similar procedure can be applied to CPPs/CQAs criticality assessment $\operatorname{Var}^{*}\left[p_{W_{k}, X_{m+1}} \mid X\right]$. Let $\boldsymbol{\theta}\left(W_{k}, X_{m+1}\right) \subset \boldsymbol{\theta}$ represent the subset of model coefficients that impacts on $\operatorname{Sh}\left(W_{k} \mid \boldsymbol{\theta}\right)$ estimation. Notice that $\boldsymbol{\mu}$ has no impact on $\operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta})$. Since SV can account for the probabilistic dependence of model coefficient estimation uncertainty, characterized by the joint posterior distribution $p(\boldsymbol{\theta} \mid X)$, and bioprocess structural interactions, we can measure the contribution from any parameter $\theta_{\ell} \in \boldsymbol{\theta}\left(W_{k}, X_{m+1}\right)$ through the posterior variance decomposition,

$$
\operatorname{Var}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid X\right]=\sum_{\theta_{\ell} \in \boldsymbol{\theta}\left(W_{k}, X_{m+1}\right)} \operatorname{Sh}_{\theta_{\ell}}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}}(\widetilde{\boldsymbol{\theta}}) \mid X\right]=\sum_{\theta_{\ell} \in \boldsymbol{\theta}\left(W_{k}, X_{m+1}\right)} \operatorname{Sh}_{\theta_{\ell}}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid X\right]
$$

The proposed BN-SV-MU sensitivity analysis can provide the comprehensive and interpretable understanding on how model uncertainty impacts on the process risk analysis and identify those parameters $\theta_{\ell}$ contributing the most on the estimation uncertainty of $\operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta})$.

Then, we derive SV measuring the estimation uncertainty contribution from each $\theta_{\ell}$,

$$
\operatorname{Sh}_{\theta_{\ell}}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid X\right]=\sum_{\mathcal{J} \subset \mathcal{L}_{k} /\{\ell\}} \frac{\left(L_{k}-|\mathcal{J}|-1\right)!|\mathcal{J}|!}{L_{k}!}[c(\mathcal{J} \cup\{\ell\})-c(\mathcal{J})]
$$

Denote the size of relevant parameters by $L_{k}=\left|\boldsymbol{\theta}\left(W_{k}, X_{m+1}\right)\right|$ and denote the index set by $\mathcal{L}_{k}, \boldsymbol{\theta}\left(W_{k}, X_{m+1}\right)=$ $\boldsymbol{\theta}_{\mathcal{L}_{k}}$. We further denote any subset by $\boldsymbol{\theta}_{\mathcal{J}} \subset \boldsymbol{\theta}\left(W_{k}, X_{m+1}\right)$ with size $J=\left|\boldsymbol{\theta}_{\mathcal{J}}\right|$ and the corresponding index set $\mathcal{J}=\{\mathcal{J}(1), \mathcal{J}(2), \ldots, \mathcal{J}(J)\} \subset \mathcal{L}_{k}$. For any $\mathcal{J} \subset \mathcal{L}_{k}$, the cost function is given as,

$$
c(\mathcal{J})=\mathrm{E}_{p\left(\boldsymbol{\theta}_{\mathcal{L}_{k}}-\mathcal{J} \mid X\right)}^{*}\left[\operatorname{Var}_{p\left(\boldsymbol{\theta}_{\mathcal{J}}\right) \boldsymbol{\theta}_{\mathcal{L}_{k}}-\mathcal{J}, X\right)}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}\right]\right]
$$

# Algorithm 2: Procedure for the BN-SV-MU Based UQ and SA 

Input: BN structure $G(\mathbf{N} \mid \boldsymbol{\theta})$, data $\mathcal{X}$, number of samples $N_{\pi}, B, B_{O}$ and $B_{f}$, index subset $\mathcal{L}_{k}$.
Output: Return $\overline{\operatorname{Sh}}_{\theta_{\ell}}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$ and $\overline{\operatorname{Sh}}_{\theta_{\ell}}^{*}\left[p_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$ for any $W_{k} \in \boldsymbol{W}=\left\{\boldsymbol{X}^{p} \cup \boldsymbol{X}^{\pi} \cup \mathbf{e}\right\}$.
(1) Call Algorithm 3 in Appendix D. 3 to obtain the posterior samples $\widetilde{\boldsymbol{\theta}}^{(b)}=\left(\widetilde{\boldsymbol{\mu}}^{(b)}, \widetilde{\boldsymbol{v}}^{(b) 2}, \widetilde{\boldsymbol{\beta}}^{(b)}\right)$ with $b=1,2, \ldots, B$ for UQ and $\widetilde{\boldsymbol{\theta}}^{(b, r)}=\left(\widetilde{\boldsymbol{\mu}}^{(b, r)}, \widetilde{\boldsymbol{v}}^{(b, r) 2}, \widetilde{\boldsymbol{\beta}}^{(b, r)}\right)$ with $b_{O}=1,2, \ldots, B_{O}$ for SA;
(2) Call Algorithm 1 to compute $\operatorname{Sh}_{W_{k}, X_{m+1}}\left(\widetilde{\boldsymbol{\theta}}^{(b)}\right)$ and criticality $p_{W_{k}, X_{m+1}}\left(\widetilde{\boldsymbol{\theta}}^{(b)}\right)$ for $b=1,2, \ldots, B$;
(3) Calculate the overall estimation uncertainty by using $\widehat{\operatorname{Var}}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$ and $\widehat{\operatorname{Var}}\left[p_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$ in Equations (18) and (19);
(4) Randomly generate $N_{\pi}$ permutations, $\pi_{n} \sim \Pi\left(\mathcal{L}_{k}\right)$ with $n=1, \ldots, N_{\pi}$;
for Each $\pi_{n}$ do
(5) Set $\widetilde{c}\left(P_{\pi_{n}(1)}\left(\pi_{n}\right)\right)=0$;
for $\ell=1, \ldots, L_{k}$ do
if $\ell<L_{k}$ then
for $b_{O}=1, \ldots, B_{O}$ do
(7) Set initial value $\boldsymbol{\theta}_{\mathcal{J}}^{(b, 0)}=\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b, 0)}$ with $\mathcal{J}=P_{\pi_{n}(\ell+1)}\left(\pi_{n}\right)$;
for $t=1, \ldots, T$ do
(8) For each $\theta_{\mathcal{J}(\ell)} \in \boldsymbol{\theta}_{\mathcal{J}}$, generate $\theta_{\mathcal{J}(\ell)}^{(b, t)} \sim p\left(\theta_{\mathcal{J}(\ell)} \mid \mathcal{X}, \widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b, t)}, \theta_{\mathcal{J}(1)}^{(b, t)}, \ldots, \theta_{\mathcal{J}(\ell-1)}^{(b, t)}, \theta_{\mathcal{J}(\ell+1)}^{(b, t-1)}\right.$, $\left.\ldots, \theta_{\mathcal{J}(t)}^{(b, t-1)}\right)$ by applying Equations (15)/(16)/(17) for the case with complete data or Equations (34)/(35)/(36) for cases with mixing data (see Appendix D). Obtain the new sample $\boldsymbol{\theta}_{\mathcal{J}}^{(b, t)}$;
(9) Set $\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b, b, b)}=\boldsymbol{\theta}_{\mathcal{J}}^{(b, t, b_{2}-1) b+1)}$ with some constant integer $h$ to reduce the correlation between consecutive samples;
(10) Compute $\widetilde{c}\left(P_{\pi_{n}(\ell+1)}\left(\pi_{n}\right)\right)$ by Equations (23) and (25);
else
(11) Set $\widetilde{c}\left(P_{\pi_{n}(\ell+1)}\left(\pi_{n}\right)\right)=\widehat{\operatorname{Var}}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$ and $\widehat{\operatorname{Var}}\left[p_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$;
(12) Compute $\Delta_{\pi_{n}(\ell)} c\left(\pi_{n}\right)=\widetilde{c}\left(P_{\pi_{n}(\ell+1)}\left(\pi_{n}\right)\right)-\widetilde{c}\left(P_{\pi_{n}(\ell)}\left(\pi_{n}\right)\right)$;
(13) Estimate $\overline{\overline{\operatorname{Sh}}_{\theta_{\ell}}}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$ and $\overline{\operatorname{Sh}}_{\theta_{\ell}}^{*}\left[p_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$ by using Equations (24) and (26).
where $\boldsymbol{\theta}_{\mathcal{L}_{k}-\mathcal{J}}=\boldsymbol{\theta}_{\mathcal{L}_{k}} \backslash \mathcal{J}$. Denote a permutation of $\mathcal{L}_{k}$ as $\pi$ and define the set $P_{\ell}(\pi)$ as the index set preceding $\ell$ in $\pi$. The SV can be rewritten as,

$$
\operatorname{Sh}_{\theta_{\ell}}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]=\sum_{\pi \in \Pi\left(\mathcal{L}_{k}\right)} \frac{1}{L_{k}!}\left[c\left(P_{\ell}(\pi) \cup\{\ell\}\right)-c\left(P_{\ell}(\pi)\right)\right]
$$

where $\Pi\left(\mathcal{L}_{k}\right)$ denotes the set of all $L_{k}$ ! permutations of $\mathcal{L}_{k}$.

The number of all possible subsets $\mathcal{J}$ could grow exponentially as $L_{k}$ increase. To address this computational issue, we use the Monte Carlo sampling approximation, ApproShapley, suggested by Song et al. (2016); Castro et al. (2009), which estimates the Shapley value in (21) by

$$
\overline{\operatorname{Sh}}_{\theta_{\ell}}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]=\frac{1}{N_{\pi}} \sum_{n=1}^{N_{\pi}}\left[c\left(P_{\ell}\left(\pi_{n}\right) \cup\{\ell\}\right)-c\left(P_{\ell}\left(\pi_{n}\right)\right)\right] \triangleq \frac{1}{N_{\pi}} \sum_{n=1}^{N_{\pi}} \Delta_{\ell} c\left(\pi_{n}\right)
$$

where $N_{\pi}$ denotes the number of permutations $\pi_{1}, \ldots, \pi_{N_{\pi}}$ randomly generated from $\Pi\left(\mathcal{L}_{k}\right)$ and $\Delta_{\ell} c\left(\pi_{n}\right)=c\left(P_{\ell}\left(\pi_{n}\right) \cup\right.$ $\{\ell\})-c\left(P_{\ell}\left(\pi_{n}\right)\right)$ is the incremental posterior variance $\operatorname{Var}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid \mathcal{X}\right]$ induced by including the $\ell$-th model pa-

rameter in $P_{\ell}\left(\pi_{n}\right)$.
As $c(\mathcal{J})$ in (20) is analytically intractable, we develop Monte Carlo sampling estimation. However, since the posterior samples obtained from the Gibbs sampler in Appendix D. 3 cannot be directly used to estimate $\mathrm{E}_{p\left(\boldsymbol{\theta}_{\mathcal{L}_{k}-\mathcal{J}} \mid \mathcal{X}\right)}^{*}\left[\operatorname{Var}_{p\left(\boldsymbol{\theta}_{\mathcal{J}}: \boldsymbol{\theta}_{\mathcal{L}_{k}-\mathcal{J}}, \mathcal{X}\right)}^{*}\left[\operatorname{Sh}_{W_{k}, x_{m+1}}\left|\tilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}\right|\right]\right]$, we introduce a nested Gibbs sampling approach. For the "outer" samples used to estimate $\mathrm{E}_{p\left(\boldsymbol{\theta}_{\mathcal{L}_{k}-\mathcal{J}} \mid \mathcal{X}\right)}^{*}[-]$, the posterior samples $\widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}$ with $b_{O}=1, \ldots, B_{O}$ can be directly obtained by applying the Gibbs sampling in Appendix D.3. We generate $\widetilde{\boldsymbol{\theta}}^{(b_{O})} \sim p(\boldsymbol{\theta} \mid \mathcal{X})$ and keep components with index $\mathcal{L}_{k}-\mathcal{J}$. Then, at each $\widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}$, a conditional sampling is further developed to generate samples from $p\left(\boldsymbol{\theta}_{\mathcal{J}} \mid \widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}, \mathcal{X}\right)$. More specifically, we set the initial value $\boldsymbol{\theta}_{\mathcal{J}}^{(b_{O}, 0)}=\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b_{O})}$. In each $t$-th MCMC iteration, given the previous sample $\boldsymbol{\theta}_{\mathcal{J}}^{(b_{O}, t-1)}$, we apply the Gibbs sampling to sequentially generate one sample from the conditional posterior for each $\theta_{\mathcal{J}(\ell)} \in \boldsymbol{\theta}_{\mathcal{J}}$ with $\ell=1, \ldots,|\mathcal{J}|$,

By repeating this procedure, we can get samples $\boldsymbol{\theta}_{\mathcal{J}}^{(b_{O}, t)}$ with $t=0, \ldots, T$. We keep one for every $h$ samples to reduce the correlations between consecutive samples. Consequently, we obtain "inner" samples $\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b_{O}, b_{I})}$ with $b_{I}=1, \ldots, B_{I}$ to estimate $\operatorname{Var}_{p\left(\boldsymbol{\theta}_{\mathcal{J}}: \boldsymbol{\theta}_{\mathcal{L}_{k}-\mathcal{J}}, \mathcal{X}\right)}^{*}\left[\operatorname{Sh}_{W_{k}, x_{m+1}}\left|\tilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}\right|\right]$.

Thus, this nested Gibbs sampling can generate $B_{O} \cdot B_{I}$ samples $\left\{\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b_{O}, b_{I})}, \widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right): b_{O}=1, \ldots, B_{O}\right.$ and $b_{I}=$ $1, \ldots, B_{I}\}$ to estimate $c(\mathcal{J})$ in (20). For any $\mathcal{J} \subset \mathcal{L}_{k}$, the cost function can be estimated as,

$$
\widetilde{c}(\mathcal{J})=\frac{1}{B_{O}} \sum_{b_{O}=1}^{B_{O}}\left\{\frac{1}{B_{I}-1} \sum_{b_{I}=1}^{B_{I}}\left[\operatorname{Sh}_{W_{k}, x_{m+1}}\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b_{O}, b_{I})}, \widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right)-\operatorname{Sh}_{W_{k}, x_{m+1}}\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right)\right]^{2}\right\}
$$

where $\operatorname{Sh}_{W_{k}, x_{m+1}}\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right)=\sum_{b_{I}=1}^{B_{I}} \operatorname{Sh}_{W_{k}, x_{m+1}}\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b_{O}, b_{I})}, \widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right) / B_{I}$. By plugging $\widetilde{c}(\mathcal{J})$ into Equation (22), we can quantify the estimation uncertainty contribution from each model coefficient $\theta_{\ell} \in \boldsymbol{\theta}_{\mathcal{L}_{k}}$,

$$
\widetilde{\operatorname{Sh}}_{\theta_{\ell}}^{*}\left[\operatorname{Sh}_{W_{k}, x_{m+1}}[X]=\frac{1}{N_{\pi}} \sum_{n=1}^{N_{\pi}} \Delta_{\ell} \widetilde{c}\left(\pi_{n}\right)\right.
$$

where $\Delta_{\ell} \widetilde{c}\left(\pi_{n}\right)=\widetilde{c}\left(P_{\ell}\left(\pi_{n}\right) \cup\{\ell\}\right)-\widetilde{c}\left(P_{\ell}\left(\pi_{n}\right)\right)$ for all $\ell=1, \ldots, L_{k}$. Similarly, for CPP/CQA criticality assessment, we can estimate the cost function,

$$
\widetilde{c}^{\prime}(\mathcal{J})=\frac{1}{B_{O}} \sum_{b_{O}=1}^{B_{O}}\left\{\frac{1}{B_{I}-1} \sum_{b_{I}=1}^{B_{I}}\left[p_{W_{k}, x_{m+1}}\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b_{O}, b_{I})}, \widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right)-\bar{p}_{W_{k}, x_{m+1}}\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right)\right]^{2}\right\}
$$

where $\bar{p}_{W_{k}, x_{m+1}}\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right)=\sum_{b_{I}=1}^{B_{I}} p_{W_{k}, x_{m+1}}\left(\widetilde{\boldsymbol{\theta}}_{\mathcal{J}}^{(b_{O}, b_{I})}, \widetilde{\boldsymbol{\theta}}_{\mathcal{L}_{k}-\mathcal{J}}^{(b_{O})}\right) / B_{I}$. Then, we estimate the estimation uncertainty contribution from $\theta_{\ell}$ on the criticality assessement,

$$
\widetilde{\operatorname{Sh}}_{\theta_{\ell}}^{*}\left[p_{W_{k}, x_{m+1}}[X]=\frac{1}{N_{\pi}} \sum_{n=1}^{N_{\pi}} \Delta_{\ell} \widetilde{c}^{\prime}\left(\pi_{n}\right)\right.
$$

More real-world data can reduce the impact of process model coefficient estimation uncertainty and improve the criticality estimation accuracy of input factors, say $W_{k}$, that contribute the most to the variance of output $X_{m+1}$.

This study can guide the "most informative" data collection. Basically, we can focus on the dominant criticality measurements with high estimation uncertainty induced by model uncertainty, assessed by variance $\widehat{\operatorname{Var}}^{*}\left[\operatorname{Sh}_{W_{k}, X_{m+1}} \mid X\right]$ in Equation (18), or $\widehat{\operatorname{Var}}^{*}\left[p_{W_{k}, X_{m+1}} \mid X\right]$ in Equation (19). Given the real-world data $X$, the proportion of estimation uncertainty contributed from each coefficient $\theta_{\ell} \in \boldsymbol{\theta}\left(W_{k}, X_{m+1}\right)$ can be estimated by,

By ranking the proportional contribution, we can find the coefficient $\theta_{\ell}$ with the highest contribution, which can guide the collection of the most informative data to control the impact of model estimation uncertainty and support production process risk analysis. We will study the impact of additional data collection and provide a systematic and rigorous approach to guide efficient data collection in the future research.

# 7 | EMPIRICAL STUDY 

To assess the performance of proposed risk and sensitivity analyses, we first consider an integrated biomanufacturing process with simulated data in Section 7.1. Then, we study the performance by utilizing the real-world process data collected from a cell culture process with multiple stages in Section 7.2. Even though there are many factors impacting on the biomanufacturing outputs, the amount of real-world bioprocess observations is often very limited. Therefore, it is important to explore the causal relationships of the biopharmaceutical production process, which can reduce the model uncertainty, increase the interpretability for process sensitivity analysis, and guide the decision making to improve the production stability.

## 7.1 | Study the Performance of Proposed Framework with Simulation Data

We revisit the example described at the end of Section 3.2 in Fig. 3. In total, the process graph model includes 20 nodes, consisting of 10 CPPs ( $\left.\boldsymbol{X}^{p}\right)$ and 8 CQAs $\left(\boldsymbol{X}^{q}\right)$ for intermediate product and 2 CQAs $(\boldsymbol{Y})$ for the final drug substance. The size of coefficients $\boldsymbol{\theta}$ is 84 , including $20 \mu_{i}{ }^{\prime} s, 20 v_{i}{ }^{\prime}$ s, and $44 \beta_{i j}$ 's coefficients. To study the performance of the proposed framework, we generate the simulated production process data $X$, which mimics the real-world data collection. The BN-based probabilistic knowledge graph with parameters $\boldsymbol{\theta}^{c}=\left(\boldsymbol{\mu}^{c},\left(\boldsymbol{v}^{2}\right)^{c}, \boldsymbol{\beta}^{c}\right)$, characterizing the underlying bioprocess risk behaviors and CPPs/CQAs interdependencies, is used for data generation, which is built on the biomanufacturing domain knowledge; see the detailed setting in Appendix E. To assess the performance of the proposed framework, we assume that the true parameter values are unknown. We empirically study the convergence of process model parameter inference in Appendix F. In Sections 7.1.1 and 7.1.3, we show the capabilities of the proposed process risk and sensitivity analyses by studying both process inherent stochastic uncertainty and model uncertainty.

### 7.1.1 | Bioprocess Sensitivity Analysis and CPPs/CQAs Criticality Assessment

We generate the data $X$ with the number of batch $R=30$ to study the performance of the proposed risk and sensitivity analyses. For any intermediate and final product CQA output $X_{i}$ of interest, at each posterior sample $\widetilde{\boldsymbol{\theta}}$, we follow Algorithm 1 to assess the criticality of any input factor $W_{k}$ (i.e., CPPs/CQAs, residual factors). Specifically, in the $h$ -

th macro-replication of simulation, we first generate the "real-world" batch data $\mathcal{X}^{(h)}$ with $h=1,2, \ldots, H$, which is used to mimic the process data collection. Considering the criticality of input $W_{k}$ to the output variance $p_{W_{k}, X_{i}}(\tilde{\boldsymbol{\theta}})=$ $\operatorname{Sh}_{W_{k}, X_{i}}(\tilde{\boldsymbol{\theta}}) / \operatorname{Var}\left(X_{i} \mid \tilde{\boldsymbol{\theta}}\right)$, we estimate the expected value $\mathrm{E}\left[p_{W_{k}, X_{i}}\right]=\iint p_{W_{k}, X_{i}}(\boldsymbol{\theta}) d P(\boldsymbol{\theta} \mid \mathcal{X}) d P\left(\mathcal{X} \mid \boldsymbol{\theta}^{\circ}\right) \times 100 \%$ by using $\widetilde{\mathrm{E}}\left[p_{W_{k}, X_{i}}\right]=\frac{1}{H B} \sum_{h=1}^{H} \sum_{b=1}^{B} p_{W_{k}, X_{i}}\left(\tilde{\boldsymbol{\theta}}^{(h, b)}\right) \times 100 \%$ with $\tilde{\boldsymbol{\theta}}^{(h, b)} \sim p\left(\boldsymbol{\theta} \mid \mathcal{X}^{(h)}\right)$ for $h=1, \ldots, H$ and $b=1, \ldots, B$, with $H=20$ and $B=1000$, and then record the results in terms of percentage (\%) in Tables 1 and 2. Each row records the criticality for each CPP, CQA, or residual input factor $W_{k}$, and each column corresponds to an intermediate or final product CQA output $X_{i}$.

TABLE 1 The estimated criticality level $\widetilde{\mathrm{E}}\left[p_{W_{k}, X_{i}}\right]$ and standard deviation $\widetilde{\operatorname{SD}}\left[p_{W_{k}, X_{i}}\right]$ (in \%) of any input CPP or other factor $W_{k}$ impacting on the variance of intermediate or final product CQA $X_{i}$.


TABLE 2 The estimated criticality level $\widetilde{\mathrm{E}}\left[p_{W_{k}, X_{i}}\right]$ and standard deviation $\widetilde{\operatorname{SD}}\left[p_{W_{k}, X_{i}}\right]$ (in \%) of any input CQA $W_{k}$ on the variance of intermediate or final product CQA $X_{i}$.


The process model uncertainty is characterized by the posterior $p(\boldsymbol{\theta} \mid \mathcal{X})$ and the overall impact on the CPPs/CQAs criticality assessment can be quantified by the posterior standard deviation (SD), $S D^{*}\left[p_{W_{k}, X_{i}}(\widetilde{\boldsymbol{\theta}}) \mid \mathcal{X}\right]$. Based on the results from $H$ macro-replications, we compute the expected SD for criticality estimation, $\operatorname{SD}\left[p_{W_{k}, X_{i}}\right]=\sqrt{\mathrm{E}\left[\operatorname{Var}^{*}\left(p_{W_{k}, X_{i}}(\widetilde{\boldsymbol{\theta}}) \mid \mathcal{X}\right)\right]} \times$ $100 \%$, with the estimate,

$$
\widetilde{\operatorname{SD}}\left[p_{W_{k}, X_{i}}\right]=\sqrt{\frac{1}{H(B-1)} \sum_{h=1}^{H} \sum_{b=1}^{B}\left[p_{W_{k}, X_{i}}\left(\widetilde{\boldsymbol{\theta}}^{(h, b)}\right)-\bar{p}_{W_{k}, X_{i}}^{(h)}\right]^{2}} \times 100 \%
$$

where $\bar{p}_{W_{k}, X_{i}}^{(h)}=\frac{1}{B} \sum_{b=1}^{B} p_{W_{k}, X_{i}}\left(\widetilde{\boldsymbol{\theta}}^{(h, b)}\right)$. In Tables 1 and 2, we record the results of SD in terms of percentage (\%) in the bracket.

For each CQA output $X_{i}$, we record the criticality with the estimated mean $\widetilde{E}\left[p_{W_{k}, X_{i}}\right]$ and standard deviation $\widetilde{\mathrm{SD}}\left[p_{W_{k}, X_{i}}\right]$ from any CPP or other factor $W_{k}$ in Table 1. Under the example setting, we can see that the variations in $X_{4}$ (dissolved oxygen in main fermentation) and $X_{13}$ (temperature in chromatography) have the dominant impact on both intermediate and final product CQAs' variance. Compared with main fermentation and chromatography, the other two operation units (i.e., centrifuge and filtration) have relatively small impact on the final product quality variation. Based on the process risk and sensitivity analyses, we also provide the result visualization; see for example Fig. 3.

By studying the subplots of the bioprocess probabilistic knowledge graph illustrated in Fig. 3, we can study the contributions from the dependent CQAs of intermediate products as inputs to the variance of final drug substance CQAs outputs, i.e., nodes $\left\{X_{19}, X_{20}\right\}$. We consider the subplots: (1) starting from the end of main fermentation with $\left\{X_{5}, X_{6}, X_{7}\right\}$; (2) starting from the end of centrifuge with $\left\{X_{10}, X_{11}\right\}$; and (3) starting from the end of chromatography with $\left\{X_{14}, X_{15}, X_{16}\right\}$. The results of process sensitivity analysis are recorded in Table 2. The CQAs after main fermentation, i.e., $\left\{X_{5}, X_{6}, X_{7}\right\}$, together account for about $50 \%$ variance of final output $X_{19}$ or $X_{20}$; and CQAs after chromatography, i.e., $\left\{X_{14}, X_{15}, X_{16}\right\}$ together account for about $90 \%$ of final output variation. Thus, the CQAs of intermediate product close to the end of production process provides better explanation of the variation of final drug substance CQAs and we can predict more accurate on its productivity and quality. This information can be used to guide the production process quality control and support the real-time release.

# 7.1.2 | Criticality Assessment Estimation Performance Comparison 

In this section, we use the same example studied in Section 7.1.1 to compare the performance of criticality assessment obtained by the proposed BN-SV approach (denoted by $p_{W_{k}, X_{20}}^{B N-S V}$ ) with an existing approach, which uses multiple linear regression and Morris sensitivity analysis (represented by ML-M); see Hassan et al. (2013); Zi (2011); Helton (1993). Basically, we first fit the multiple linear regression to the random inputs (i.e., $W_{k}=X_{i}$ listed in the first column of Table 1) and output $X_{20}$, and then use Morris sensitivity analysis to measure the criticality of each input $W_{k}$. Here, we use the same experiment setting with that used in Section 7.1.1. With the underlying parameters setting $\boldsymbol{\theta}^{c}=\left(\boldsymbol{\mu}^{c},\left(\boldsymbol{v}^{2}\right)^{c}, \boldsymbol{\beta}^{c}\right)$ given in Appendix E, the true criticality of any input factor $W_{k}$ can be calculated with $p_{W_{k}, X_{20}}^{c}=\operatorname{Sh}_{W_{k}, X_{20}}\left(\boldsymbol{\theta}^{c}\right) / \operatorname{Var}\left(X_{20} \mid \boldsymbol{\theta}^{c}\right)$, where $\operatorname{Sh}_{W_{k}, X_{20}}\left(\boldsymbol{\theta}^{c}\right)$ and $\operatorname{Var}\left(X_{20} \mid \boldsymbol{\theta}^{c}\right)$ are obtained by applying Equations (11) and (12). Then, suppose the underlying process model coefficients are unknown, and we can compare the criticality assessment performance of both approaches. In Table 3, we record the mean and SD of criticality estimates obtained from LM-M and proposed BN-SV approaches with $H=30$ macro-replications and $R=30$ batches. The mean absolute

error (MAE) is calculated by,

$$
M A E\left(p_{W_{k}, X_{20}}^{y}\right)=\frac{1}{H B} \sum_{h=1}^{H} \sum_{b=1}^{B}\left|p_{W_{k}, X_{20}}^{y}\left(\overline{\boldsymbol{\theta}}^{(h, b)}\right)-p_{W_{k}, X_{20}}^{z}\right| \times 100 \%
$$

where $y$ is ML-M or BN-SV. The results in Table 3 show that the proposed BN-SV sensitivity analysis provides better criticality assessment of critical inputs.

TABLE 3 The CPPs criticality estimation results obtained by BN-SV sensitivity analysis and existing multiple regression based sensitivity analysis.


# 7.1.3 | Sensitivity Analysis for Model Uncertainty 

Here we consider the product protein content $X_{20}$ in Fig. 3 as the output to study the performance of sensitivity analysis for model uncertainty. Based on the results in Table 1, the CPPs $X_{4}$ and $X_{13}$ have the dominant contributions to the variance of output $X_{20}$, and the estimates of $p_{W_{k}, X_{i}}$ also have the high estimation uncertainty. Thus, we conduct the BN-SV-MU sensitivity analysis to study how the estimation uncertainty of each model coefficient impacts on the criticality assessment for $p_{X_{4}, X_{20}}$ and $p_{X_{13}, X_{20}}$.

Given the data $\mathcal{X}$, we provide the posterior variance decomposition studying the criticality estimation uncertainty induced by the MU, $\operatorname{Var}_{p(\boldsymbol{\theta} \mid \mathcal{X})}^{*}\left[p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}|=\sum_{\theta_{\ell} \in \boldsymbol{\theta}\left(W_{k}, X_{i}\right)} \operatorname{Sh}_{\theta_{\ell}}^{*}\left|p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}|\right.\right.$. Then, we can estimate the expected relative contribution from each model coefficient $\theta_{\ell} \in \boldsymbol{\theta}\left(W_{k}, X_{i}\right)$ with $\operatorname{EP}_{\theta_{\ell}}\left(p_{W_{k}, X_{i}}\right) \equiv \mathrm{E}\left[\frac{\operatorname{Sh}_{\theta_{\ell}}^{*}\left|p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}|}{V_{\ell} p(\boldsymbol{\theta} \mid \mathcal{X})}\right] p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}|}{p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}|}\right]$. In the $h$-th macro-replication, given the data $\mathcal{X}^{(h)}$, we can estimate the contribution from each $\theta_{\ell}$ by using $\widehat{\operatorname{Sh}}_{\theta_{\ell}}\left|p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}^{(h)}|\right.$ and $\left.\widehat{\operatorname{Var}}_{p(\boldsymbol{\theta} \mid \mathcal{X})}\left|p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}^{(h)}|\right.$ following Equations (24) and (19), which is estimated by using $N_{\pi}=500, B_{O}=5$ and $B_{I}=20$; see Song et al. (2016) for the selection of sampling parameter setting. Thus, we have the estimation uncertainty proportion $\widehat{\mathrm{EP}}_{\theta_{\ell}}\left(p_{W_{k}, X_{i}}\right) \equiv \frac{1}{H} \sum_{h=1}^{H} \frac{\widehat{\operatorname{Sh}}_{\theta_{\ell}}^{*}\left|p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}^{(h)}|\right.}{\widehat{\operatorname{Var}}_{p(\boldsymbol{\theta} \mid \mathcal{X})}\left|p_{W_{k}, X_{i}}(\overline{\boldsymbol{\theta}})|\mathcal{X}^{(h)}|\right.}$ with $H=20$.

The coefficients contributing to the estimation of $\operatorname{Sh}_{X_{4}, X_{20}}$ include $v_{4}^{2}$ and 18 linear coefficients $\boldsymbol{\beta}$ on the paths from node $X_{4}$ to node $X_{20}$. The coefficients contributing to the estimation of $\operatorname{Sh}_{X_{13}, X_{20}}$ include $v_{13}^{2}$ and 6 linear coefficients $\boldsymbol{\beta}$ located on the paths from $X_{13}$ to $X_{20}$. Due to the space limit, we only present the top five coefficients contributing most to the estimation uncertainty of criticality $p_{X_{4}, X_{20}}$ and $p_{X_{13}, X_{20}}$, and aggregate the results for remaining coefficients. The sensitivity analysis results, $\widehat{\mathrm{EP}}_{\theta_{\ell}}\left(p_{W_{k}, X_{i}}\right) \pm \operatorname{SE}\left[\widehat{\mathrm{EP}}_{\theta_{\ell}}\left(p_{W_{k}, X_{i}}\right)\right]$, for $p_{X_{4}, X_{20}}$ and $p_{X_{13}, X_{20}}$ are

shown in Table 4, where SE stands for the standard error (SE). Notice that the coefficients that contribute the most to the estimation error of the criticality $p_{X_{4}, X_{20}}$ and $p_{X_{13}, X_{20}}$ are the variance coefficients of CPPs $\left(v_{4}^{2}\right.$ and $\left.v_{13}^{2}\right)$. The estimation uncertainty of linear coefficients have similar and relatively small contributions. Similar information can be presented through the sample visualization of the integrated bioprocess sensitivity analysis in Fig. 3. The darkness of directed edges and circle boundaries indicates the seriousness of model uncertainty from corresponding model coefficients $\boldsymbol{\beta}$ and $\boldsymbol{v}$. Thus, this information can guide the process monitoring and data collection to efficiently reduce the impact of model uncertainty and facilitate learning and systematic risk control for integrated biomanufacturing system.

TABLE 4 The estimated relative contribution of each BN parameter estimation uncertainty (in terms of \%) on criticality assessment $\widehat{\mathrm{EP}}_{\theta_{Z}}\left(p_{W_{8}, X_{i}}\right) \pm \mathrm{SE}\left[\widehat{\mathrm{EP}}_{\theta_{Z}}\left(p_{W_{8}, X_{i}}\right)\right]$ for $p_{X_{4}, X_{20}}$ and $p_{X_{13}, X_{20}}$.


# 7.2 | Real Case Study for Multiple Phase Cell Culture Process Risk and Sensitivity Analyses 

To study the performance of proposed bioprocess risk and sensitivity analyses, in this section, we consider the fedbatch fermentation process of Yarrowia lipolytica yeast for citrate or citric acid (CA) production. This multiple-phase cell culture process includes seed culture, cell growth and production processes. In the seed culture, the thawed seed vial solution of $Y$. lipolytica strain is transferred to a shake flask containing seed culture medium, and then grown at $30^{\circ} \mathrm{C}$ and 280 rpm until cell concentration reaches around $2-5$ in OD600 (optical density measured at a wavelength of 600 nm ), which usually takes 18-24h (hours). In the Fed-Batch Fermentation, the seed culture ( 50 mL ) is first transferred to the bioreactor, which contains the initial fermentation medium ( 600 mL ) and initial substrate (here we use $35 \mathrm{~g} / \mathrm{L}$ soybean oil). The feeding starts when the substrate concentration decreases below $20 \mathrm{~g} / \mathrm{L}$, while the rate is adjusted to maintain the concentration of substrate about $20 \mathrm{~g} / \mathrm{L}$. During the fermentation, the dissolved oxygen level, denoted by $\mathrm{pO}_{2}$, is set around $30 \%$ of air saturation by cascade controls of agitation speed between 500 and $1,400 \mathrm{rpm}$, and the aeration rate is fixed at $0.3 \mathrm{~L} / \mathrm{min}$. The pH is controlled at 6.0 during $0-12 \mathrm{~h}$, then increased to 7.0 in 6 hours, and maintained at 7.0 in the remainder of run by feeding KOH (i.e., feed of base). The temperature is maintained at $30^{\circ} \mathrm{C}$ for the entire run. At several middle points of each run, the bioreactor state is estimated by using $\mathrm{pH} / \mathrm{pO}_{2}$ probes and off-line sample measurement for residual substrate, which can guide the adjustment of operation decisions (i.e., feed rate).

In this real case study, we focus on the critical CPPs during the fed-batch fermentation, including cell concentration after seed culture process, feed rate, dissolved oxygen $\left(\mathrm{pO}_{2}\right)$, and residual oil. We consider main CQAs related to cell (i.e., total cell biomass) and productivity (i.e., total CA production). Experiments are conducted in Dr. Dongming Xie's Lab to generate process data generate the data $\mathcal{X}$ with $R=8$ batches during 140 hours; see the data in Fig. 6. We want to study how the CPPs at different time contribute to the variation of intermediate and final CQAs outputs, while evaluating the impact from model uncertainty.

Based on the interactions of CPPs/CQAs, we develop the BN-based bioprocess probabilistic model with 62 nodes; see the illustration in Fig. 7. We first estimate the expected criticality $\mathrm{E}\left[p_{W_{8}, X_{i}}\right]$ by using $B$ posterior samples of model

coefficients, $\widetilde{\mathrm{E}}\left[p_{W_{k}, X_{i}}\right]=\frac{1}{B} \sum_{b=1}^{B} p_{W_{k}, X_{i}}\left(\overline{\boldsymbol{\theta}}^{(b)}\right) \times 100 \%$ with $\overline{\boldsymbol{\theta}}^{(b)} \sim p(\boldsymbol{\theta} \mid X)$ for $b=1, \ldots, B$, with $B=1000$. We record the results in terms of percentage (\%) in Tables 5 and 6 for cell biomass and CA production respectively with each row and column corresponding to random input $W_{k}$ and output $X_{i}$. In addition, the overall impact of model uncertainty on the CPPs/CQAs criticality assessment can be quantified by the posterior standard deviation (SD), which can be estimated by, $\widehat{\operatorname{SD}}\left[p_{W_{k}, X_{i}}\right]=\sqrt{\frac{1}{(B-1)} \sum_{b=1}^{B}\left[p_{W_{k}, X_{i}}\left(\overline{\boldsymbol{\theta}}^{(b)}\right)-\bar{p}_{W_{k}, X_{i}}\right]^{2}} \times 100 \%$, where $\bar{p}_{W_{k}, X_{i}}=\frac{1}{B} \sum_{b=1}^{B} p_{W_{k}, X_{i}}\left(\overline{\boldsymbol{\theta}}^{(b)}\right)$. The results of SD are recorded in the bracket in Tables 5 and 6. Due to the space limit, we only provide the dominant (high criticality level) part of time points. We also study the subplots and assess the impact from intermediate CQAs (biomass and CA amount) as inputs on the following output variation in Table 7.
![img-5.jpeg](img-5.jpeg)

FIGURE 6 Data of citric acid fed-batch fermentation case study.
![img-6.jpeg](img-6.jpeg)

FIGURE 7 BN model for citric acid fed-batch fermentation case study.

Differing with the simulation study in Section 7.1, there is no macro-replication in the real case study. Notice that the posterior standard deviation (SD) can measure the overall model uncertainty, i.e., the variation of criticality estimates cross different posterior samples characterizing the model coefficient estimation uncertainty. Based on the sample average of $B$ posterior samples $\bar{p}_{W_{k}, X_{i}}=\frac{1}{B} \sum_{b=1}^{B} p_{W_{k}, X_{i}}\left(\overline{\boldsymbol{\theta}}^{(b)}\right) \times 100 \%$, the estimation accuracy of criticality $\bar{p}_{W_{k}, X_{i}}$ is measured by the standard error (SE) with $\operatorname{SE}\left(\bar{p}_{W_{k}, X_{i}}\right)=\operatorname{SD}\left(\bar{p}_{W_{k}, X_{i}}\right) / \sqrt{B}$.

TABLE 5 The estimated criticality level $\widehat{\mathrm{E}}\left[\rho_{W_{k}, X_{i}}\right]$ and standard error $\widehat{\mathrm{SD}}\left[\rho_{W_{k}, X_{i}}\right]$ (in \%) of any input CPP or other factor $W_{k}$ impacting on the variance of intermediate or final biomass $X_{i}$.


TABLE 6 The estimated criticality level $\widehat{\mathrm{E}}\left[\rho_{W_{k}, X_{i}}\right]$ and standard error $\widehat{\mathrm{SD}}\left[\rho_{W_{k}, X_{i}}\right]$ (in \%) of any input CPP or other factor $W_{k}$ impacting on the variance of intermediate or final CA amount $X_{i}$.


TABLE 7 The estimated criticality level $\widehat{\mathrm{E}}\left[\rho_{W_{k}, X_{i}}\right]$ and standard error $\widehat{\mathrm{SD}}\left[\rho_{W_{k}, X_{i}}\right]$ (in \%) of any input CQA $W_{k}$ impacting on the variance of intermediate or final biomass or CA amount $X_{i}$.


The results in Tables 5 and 6 show that the variations of residual oil and feed rate in the cell growth phase (about from time $t=23 h$ to $28 h$ ) have dominant impact on both intermediate and final cell biomass and CA productivity. As fermentation time further increases, the criticality level of input factors $W_{k}$ on the output $X_{i}$, CA production, tends to decrease. It matches well with the data in Fig. 6, the cell growth and production both become slower and more stable. This observation suggests that controlling the CPPs (i.e., feed rate and residual oil) to ensure the good cell growth stage is more important in order to improve the process stability. For the cell total biomass output in Table 5, since the residual oil generates the scattering particles impacting on OD600 and cell biomass measurement accuracy, this effect becomes larger as the residual oil increases, which explains the high contribution of residual oil at the end of process (i.e., rOil_102) to the final cell biomass measurement variation.

By studying the subplots, we study the impact of middle step CQAs (i.e., cell biomass and CA amount in the cell growth and production phases) on the final output variation. We record the results in Table 7. As the fermentation time $t$ increases, the explained variations of final biomass and CA by current values increase. They reach to around $70 \%$ for biomass and $90 \%$ for CA at time $t=95 h$. This observation is consistent with the data in Fig. 6 and the growth of biomass/CA is relative slow in the periods after it. However, compared with CA, biomass has relatively larger prediction variation even in the later stages of production, which can be explained by the measurement errors of Cell OD induced by large amount of residual oil. In terms of biomass impacting on final CA (or CA impacting on

biomass), the most critical part is biomass at time $t=34 h$ (or CA amount at $t=47.5 h$ ). Since cell growth needs nitrogen, the production phase usually starts when nitrogen concentration becomes small. During those periods (around 30h to 50 h ), nitrogen from the initial medium is consumed and both intracellular lipid (which becomes part of biomass) accumulation and extracellular CA production are induced by nitrogen limitation. It can be also observed in Fig. 6, where the sudden increase of CA total slopes happens around 30 h to 50 h , whose variations have critical contribution to final CA output uncertainty.

We also conduct the sensitivity analysis studying the impact of model uncertainty on the CPPs/CQAs criticality assessment. Here we focus on criticality assessment estimation of $p_{r O i I _28, C A \_140}$ and $p_{r O i I \_102, B M \_140}$, which have high criticality and overall model uncertainty; see Tables 5 and 6 . The model coefficients contributing to the estimation of $p_{r O i I \_28, C A \_140}$ include $v_{r O i I \_28}^{2}$ and 32 linear coefficients $\boldsymbol{\beta}$ on the paths from node $r O i I \_28$ to node $C A \_140$, whereas coefficients contributing to the estimation of $p_{F e e d \_23, C A \_140}$ include $v_{F e e d \_23}^{2}$ and 36 linear coefficients $\boldsymbol{\beta}$. We present the top five coefficients contributors to the estimation uncertainty of criticality $p_{r O i I \_28, C A \_140}$ and $p_{F e e d \_23, C A \_140}$, and aggregate the results for remaining coefficients in Table 8. From the results, the estimation uncertainty of variance coefficients of $\mathrm{CPPs}\left(v_{r O i I \_28}^{2}\right.$ and $\left.v_{F e e d \_23}^{2}\right)$ have the largest contribution to the estimation uncertainty of the criticality $p_{r O i I \_28, C A \_140}$ and $p_{F e e d \_23, C A \_140}$. The estimation uncertainty of coefficients $\boldsymbol{\beta}$ in both sets $\boldsymbol{\theta}(r O i I \_28, C A \_140)$ and $\boldsymbol{\theta}\left(F e e d \_23, C A \_140\right)$ have similar and relative lower contributions.

TABLE 8 The estimated relative contribution of each BN parameter estimation uncertainty (in terms of \%) on criticality assessment $\widehat{\mathrm{EP}}_{\theta_{f}}\left(p_{W_{k}, X_{j}}\right)$ for $p_{F e e d \_20, C A \_140}$.


# 8 | CONCLUSIONS 

Driven by the critical challenges in biomanufacturing, we create an integrated bioprocess knowledge graph and propose interpretable risk and sensitivity analyses, which can provide the production process risk- and science-based understanding, guide the CPPs/CQAs specifications and production stability control, and facilitate the process development. Since hundreds of factors can impact on the product quality and productivity, and also the amount of process observations is often very limited, we explore the process interactions and causal relationships, and then develop a Bayesian network (BN) based probabilistic knowledge graph characterizing the causal interdependencies of production process CPPs/CQAs. Building on the knowledge graph, we propose the BN-SV based sensitivity analysis to assess the criticality of each random input factor on the variance of intermediate/final product quality attributes by using the Shapley value (SV), which can correctly account for input interdependencies and process structural interactions. We further introduce the BN-SV-MU sensitivity analysis, which can provide the comprehensive understanding on how the estimation uncertainty of each part of process model coefficients impacts on the production risk analysis and CPPs/CQAs criticality assessment. It can guide bioprocess sensor monitoring and "most informative" data collection to facilitate bioprocess learning and model uncertainty reduction. Both simulation and real case studies are used to demonstrate the promising performance of proposed bioprocess risk and sensitivity analyses.

# ACKNOWLEDGEMENTS 

The authors are grateful for constructive comments from Dr. Barry Nelson (Northeastern University), Peter Baker (Green Mountain Quality Assurance, LLC), help from Hua Zheng (NEU) on the development of bioprocess knowledge graph visualization, and help from Na Liu (UMass Lowell) conducting lab experiments.

# A | ONTOLOGY BASED DATA AND PROCESS INTEGRATION 

By exploring the causal relationships and interactions in the production processes, we introduce bioprocess ontologybased data integration, which can connect all distributed and heterogeneous data collected from bioprocess. This relational graph can enable the connectivity of end-to-end process from drug development to patient response; see Fig. 8 for a simplified illustration of integrated biopharmaceutical manufacturing supply chain. Nodes represent factors (i.e., CPPs/CQAs, media feed, bioreactor operating conditions, other uncontrolled factors) impacting the process outputs, and the directed edges model the causal relationships. Each dashed block could represent a module, which can be each phase or each unit operation. In this relational graph, the shaded nodes represent the variables with real-world observations, including the testing and sensor monitoring data of CPPs/CQAs for raw materials, operation conditions, and intermediate/final drug products. The unshaded and dashed nodes represent variables without observations and residuals, including the complete quality status of intermediate and final drug products, and other uncontrollable factors (e.g., contamination) introduced during the process unit operations.
![img-7.jpeg](img-7.jpeg)

FIGURE 8 Biopharmaceutical production process ontology based causal relationships.

## B | DETAILED DERIVATION OF EQUATION (8)

In order to show Equation (8), we consider more general results as following,

$$
X_{n}=\mu_{n}+\sum_{k=1}^{m^{p}} \gamma_{k, n}\left(X_{k}-\mu_{k}\right)+\sum_{k=m^{p}+1}^{n} \gamma_{k, n} e_{k}
$$

for $n=m^{p}+1, \ldots, m+1$, where $\gamma_{k, n}$ is given as Equations (9) and (10). Notice according to linear Gaussian model (6), we can write $X_{m^{p}+1}=\mu_{m^{p}+1}+\sum_{k=1}^{m^{p}} \beta_{k, m^{p}+1}\left(X_{k}-\mu_{k}\right)+e_{m^{p}+1}$, where $\beta_{k, m^{p}+1}=0$ for $k \notin P a\left(X_{m^{p}+1}\right)$. Suppose

Equation (28) holds for all $n=m^{p}+1, \ldots, n_{0}$. For $n=n_{0}+1$, by applying linear Gaussian model, we have

$$
\begin{aligned}
& X_{n_{0}+1}=\mu_{n_{0}+1}+\sum_{k=1}^{n_{0}} \beta_{k, n_{0}+1}\left(X_{k}-\mu_{k}\right)+e_{n_{0}+1} \\
& =\mu_{n_{0}+1}+\sum_{k=1}^{m^{p}} \beta_{k, n_{0}+1}\left(X_{k}-\mu_{k}\right)+\sum_{\ell=m^{p}+1}^{n_{0}} \beta_{\ell, n_{0}+1}\left[\sum_{k=1}^{m^{p}} \gamma_{k, \ell}\left(X_{k}-\mu_{k}\right)+\sum_{k=m^{p}+1}^{\ell} \gamma_{k, \ell} e_{k}\right]+e_{n_{0}+1} \\
& =\mu_{n_{0}+1}+\sum_{k=1}^{m^{p}}\left[\beta_{k, n_{0}+1}+\sum_{\ell=m^{p}+1}^{n_{0}} \gamma_{k, \ell} \beta_{\ell, n_{0}+1}\right]\left(X_{k}-\mu_{k}\right)+\sum_{k=m^{p}+1}^{n_{0}}\left[\sum_{\ell=k}^{n_{0}} \gamma_{k, \ell} \beta_{\ell, n_{0}+1}\right] e_{k}+e_{n_{0}+1} \\
& =\mu_{n_{0}+1}+\sum_{k=1}^{m^{p}} \gamma_{k, n_{0}+1}\left(X_{k}-\mu_{k}\right)+\sum_{k=m^{p}+1}^{n_{0}+1} \gamma_{k, n_{0}+1} e_{k}
\end{aligned}
$$

Step (29) follows by applying (28). Step (30) follows by applying Equations (9) and (10). By mathematical induction, we can conclude that Equation (28) holds for all $n=m^{p}+1, \ldots, m+1$.

# C | DETAILED DERIVATION OF EQUATION (11) 

We consider $W_{k}$ and $\mathcal{J} \subset \mathcal{K} /\{k\}$. For $\mathcal{J}=\varnothing$, we have

$$
\frac{(m-|\mathcal{J}|)!\mid \mathcal{J}!)}{(m+1)!}[c(\mathcal{J} \cup\{k\})-c(\mathcal{J})]=\frac{1}{m+1} \gamma_{k, m+1}^{2} \operatorname{Var}\left(W_{k}\right)
$$

For $|\mathcal{J}|=m^{\prime}$ with $m^{\prime}=1, \ldots, m$, we have

$$
\begin{aligned}
& \sum_{\{\mathcal{J} \mid|\mathcal{J}|=m^{\prime}\}} \frac{(m-|\mathcal{J}|)!\mid \mathcal{J}!}{(m+1)!}[c(\mathcal{J} \cup\{k\})-c(\mathcal{J})] \\
= & \sum_{|\mathcal{J}| \mid \mathcal{J}|=m^{\prime}\rangle} \frac{\left(m-m^{\prime}\right)!m^{\prime}!}{(m+1)!}\left[\gamma_{k, m+1}^{2} \operatorname{Var}\left(W_{k}\right)+2 \sum_{\ell \in \mathcal{J}} \gamma_{k, m+1} \gamma_{\ell, m+1} \operatorname{Cov}\left(W_{k}, W_{\ell}\right)\right] \\
= & \frac{\left(m-m^{\prime}\right)!m^{\prime}!}{(m+1)!}\left\{\binom{m}{m^{\prime}} \gamma_{k, m+1}^{2} \operatorname{Var}\left(W_{k}\right)\right. \\
& \left.+2 \sum_{\ell \in \mathcal{K} /\{k\}}\left[\sum_{|\mathcal{J}| \mid \mathcal{J}|=m^{\prime} \text { and } \ell \in \mathcal{J}}\right] \gamma_{k, m+1} \gamma_{\ell, m+1} \operatorname{Cov}\left(W_{k}, W_{\ell}\right)\right]\right\} \\
= & \frac{1}{m+1} \gamma_{k, m+1}^{2} \operatorname{Var}\left(W_{k}\right)+2 \frac{\left(m-m^{\prime}\right)!m^{\prime}!}{(m+1)!}\binom{m-1}{m^{\prime}-1} \sum_{\ell \in \mathcal{K} /\{k\}} \gamma_{k, m+1} \gamma_{\ell, m+1} \operatorname{Cov}\left(W_{k}, W_{\ell}\right) \\
= & \frac{1}{m+1} \gamma_{k}^{2} \operatorname{Var}\left(W_{k}\right)+\frac{2 m^{\prime}}{m(m+1)} \sum_{\ell \in \mathcal{K} /\{k\}} \gamma_{k, m+1} \gamma_{\ell, m+1} \operatorname{Cov}\left(W_{k}, W_{\ell}\right)
\end{aligned}
$$

Step (31) holds because the number of all subsets $\mathcal{J}$ with size $m^{\prime}$ is $\binom{m}{m^{\prime}}$. In Step (32), we shift the order of sums over $\mathcal{J}$ and $\ell$. Then, Step (33) holds because given $W_{\ell}$, the number of subset $\{\mathcal{J}:|\mathcal{J}|=m^{\prime}$ and $\ell \in \mathcal{J}\}$ is $\binom{m-1}{m^{\prime}-1}$. So, we get the Shapley value,

$$
\operatorname{Sh}_{W_{k}, X_{m+1}}(\boldsymbol{\theta})=\sum_{\mathcal{J} \subset \mathcal{K} /\{k\}} \frac{(m-|\mathcal{J}|)!\mid \mathcal{J}!}{(m+1)!}[c(\mathcal{J} \cup\{k\})-c(\mathcal{J})]
$$

$$
\begin{aligned}
& =\sum_{m^{\prime}=0}^{m}\left[\frac{1}{m+1} \gamma_{k_{1}}^{2} \operatorname{Var}\left(W_{k}\right)+\frac{2 m^{\prime}}{m(m+1)} \sum_{\ell \in \mathcal{K} /\{k\}} \gamma_{k, m+1} \gamma_{\ell, m+1} \operatorname{Cov}\left(W_{k}, W_{\ell}\right)\right] \\
& =\gamma_{k, m+1}^{2} \operatorname{Var}\left(W_{k}\right)+\sum_{\ell \in \mathcal{K} /\{k\}} \gamma_{k, m+1} \gamma_{\ell, m+1} \operatorname{Cov}\left(W_{k}, W_{\ell}\right)
\end{aligned}
$$

# D | DERIVATION AND PROCEDURE FOR BN LEARNING AND GIBBS SAMPLER 

We derive the posterior distribution of BN model parameters $p(\boldsymbol{\theta} \mid \mathcal{X})$ and introduce a Gibbs sampling approach to generate the posterior samples, $\overline{\boldsymbol{\theta}}^{(b)}-p(\boldsymbol{\theta} \mid \mathcal{X})$ with $b=1,2, \ldots, B$ quantifying the model uncertainty. In Section D.1, we first provide the derivation for conditional posterior distribution with complete production process data described in Section 6.1. Considering the situations where we could have some additional incomplete batch data (e.g., batches in the middle of production or thrown away at certain production step based on the quality control strategy), we further extend the Bayesian learning approach to cases with mixing data in Section D.2. Then, we provide the Gibbs sampling procedure to generate the posterior samples $\overline{\boldsymbol{\theta}}^{(b)}$ with $b=1,2, \ldots, B$ in Section D.3.

## D. 1 | Knowledge Learning for Cases with Complete Production Process Data

Following Section 6.1, we first derive the conditional posterior distribution for the weight coefficient $\beta_{i j}$,

$$
\begin{aligned}
& p\left(\beta_{i j} \mid \mathcal{X}, \boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}_{-i j}\right) \propto\left[\prod_{r=1}^{R} p\left(x_{j}^{(r)} \mid x_{P_{\theta}\left(X_{j}\right)}^{(r)}\right)\right] p\left(\beta_{i j}\right) \\
& \propto \exp \left\{-\sum_{r=1}^{R} \frac{1}{2 v_{j}^{2}}\left[\left(x_{j}^{(r)}-\mu_{j}\right)-\beta_{i j}\left(x_{i}^{(r)}-\mu_{i}\right)-\sum_{k \in P_{\theta}(j) /\{i\}} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)\right]^{2}\right. \\
& \left.-\frac{1}{2 \tau_{i j}^{(0) 2}}\left(\beta_{i j}-\theta_{i j}^{(0)}\right)^{2}\right\} \\
& \propto \exp \left\{-\frac{1}{2 v_{j}^{2}} \sum_{r=1}^{R}\left(\alpha_{i}^{(r)} \beta_{i j}-m_{i j}^{(r)}\right)^{2}-\frac{1}{2 \tau_{i j}^{(0) 2}}\left(\beta_{i j}-\theta_{i j}^{(0)}\right)^{2}\right\} \\
& \propto \exp \left\{-\frac{\beta_{i j}^{2}}{2}\left(\sum_{r=1}^{R} \frac{\alpha_{i}^{(r) 2}}{v_{j}^{2}}+\frac{1}{\tau_{i j}^{(0) 2}}\right)+\beta_{i j}\left(\sum_{r=1}^{R} \frac{\alpha_{i}^{(r)} m_{i j}^{(r)}}{v_{j}^{2}}+\frac{\theta_{i j}^{(0)}}{\tau_{i j}^{(0) 2}}\right)\right\}=N\left(\theta_{i j}^{(R)}, \tau_{i j}^{(R) 2}\right)
\end{aligned}
$$

where $\theta_{i j}^{(R)}=\frac{\tau_{i j}^{(0) 2} \sum_{r=1}^{R} \alpha_{i}^{(r)} m_{i j}^{(r)}+v_{j}^{2} \theta_{i j}^{(0)}}{\tau_{i j}^{(0) 2} \sum_{r=1}^{R} \alpha_{i}^{(r) 2}+v_{j}^{2}}$ and $\tau_{i j}^{(R) 2}=\frac{\tau_{i j}^{(0) 2} v_{j}^{2}}{\tau_{i j}^{(0) 2} \sum_{r=1}^{R} \alpha_{i}^{(r) 2}+v_{j}^{2}}$ with $\alpha_{i}^{(r)}=x_{i}^{(r)}-\mu_{i}, \quad$ and $\quad m_{i j}^{(r)}=$ $\left(x_{j}^{(r)}-\mu_{j}\right)-\sum_{X_{k} \in P_{\theta}\left(X_{j}\right) /\{X_{i}\}} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)$.

Second, we derive the conditional posterior distribution for the variance coefficient $v_{i}^{2}=\operatorname{Var}\left[X_{i} \mid P_{\theta}\left(X_{i}\right)\right]$ with $i=1,2, \ldots, m+1$,

$$
p\left(v_{i}^{2} \mid \mathcal{X}, \boldsymbol{\mu}, \boldsymbol{v}_{-i}^{2}, \boldsymbol{\beta}\right) \propto\left[\prod_{r=1}^{R} p\left(x_{i}^{(r)} \mid x_{P_{\theta}\left(X_{i}\right)}^{(r)}\right)\right] p\left(v_{i}^{2}\right)
$$

$$
\begin{aligned}
& \propto\left(v_{i}^{2}\right)^{-R / 2-\kappa_{i}^{(0)} / 2-1} \exp \left\{-\frac{1}{2 v_{j}^{2}} \sum_{r=1}^{R}\left[\left(x_{i}^{(r)}-\mu_{i}\right)-\sum_{X_{k} \in P a\left(X_{i}\right)} \beta_{k i}\left(x_{k}^{(r)}-\mu_{k}\right)\right]^{2}\right\} \\
& \propto \quad\left(v_{i}^{2}\right)^{-R / 2-\kappa_{i}^{(0)} / 2-1} \exp \left\{-\frac{1}{2 v_{j}^{2}} \sum_{r=1}^{R} u_{i}^{(r) 2}-\frac{\lambda_{i}^{(0)}}{2 v_{j}^{2}}\right\}=\operatorname{Inv}-\Gamma\left(\frac{\kappa_{i}^{(R)}}{2}, \frac{\lambda_{i}^{(R)}}{2}\right)
\end{aligned}
$$

where $\kappa_{i}^{(R)}=\kappa_{i}^{(0)}+R, \lambda_{i}^{(R)}=\lambda_{i}^{(0)}+\sum_{r=1}^{R} u_{i}^{(r) 2}$ and $u_{i}^{(r)}=\left(x_{i}^{(r)}-\mu_{i}\right)-\sum_{X_{k} \in P a\left(X_{i}\right)} \beta_{k i}\left(x_{k}^{(r)}-\mu_{k}\right)$.
Third, we derive the conditional posterior distribution of mean coefficient $\mu_{i}$ with $i=1,2, \ldots, m+1$ for any CPP and CQA,

$$
\begin{aligned}
& p\left(\mu_{i} \mid X, \boldsymbol{\mu}_{-i}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right) \propto p\left(\mu_{i}\right) \int_{r=1}^{R}\left[p\left(x_{i}^{(r)} \mid x_{P a\left(X_{i}\right)}^{(r)}\right) \prod_{j \in S\left(X_{i}\right)} p\left(x_{j}^{(r)} \mid x_{P a\left(X_{j}\right)}^{(r)}\right)\right] \\
& \propto \exp \left\{-\frac{1}{2 v_{i}^{2}} \sum_{r=1}^{R}\left[\left(x_{i}^{(r)}-\mu_{i}\right)-\sum_{X_{k} \in P a\left(X_{i}\right)} \beta_{k i}\left(x_{k}^{(r)}-\mu_{k}\right)\right]^{2}\right. \\
& \left.-\sum_{r=1}^{R} \sum_{X_{j} \in S\left(X_{i}\right)} \frac{1}{2 v_{j}^{2}}\left[\left(x_{j}^{(r)}-\mu_{j}\right)-\sum_{X_{k} \in P a\left(X_{j}\right)} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)\right]^{2}-\frac{1}{2 \sigma_{i}^{(0) 2}}\left(\mu_{i}-\mu_{i}^{(0)}\right)^{2}\right\} \\
& \propto \exp \left\{-\frac{1}{2 v_{i}^{2}} \sum_{r=1}^{R}\left(\mu_{i}-a_{i}^{(r)}\right)^{2}-\sum_{r=1}^{R} \sum_{X_{j} \in S\left(X_{i}\right)}-\frac{1}{2 v_{j}^{2}}\left(\beta_{i j} \mu_{i}-c_{i j}^{(r)}\right)^{2}\right. \\
& \left.-\frac{1}{2 \sigma_{i}^{(0) 2}}\left(\mu_{i}-\mu_{i}^{(0)}\right)^{2}\right\} \\
& \propto \exp \left\{-\frac{\mu_{i}^{2}}{2}\left(\frac{R}{v_{i}^{2}}+\sum_{X_{j} \in S\left(X_{i}\right)} \frac{R \beta_{i j}^{2}}{v_{j}^{2}}+\frac{1}{\sigma_{i}^{(0) 2}}\right)+\mu_{i}\left(\sum_{r=1}^{R} \frac{a_{i}^{(r)}}{v_{i}^{2}}+\sum_{r=1}^{R} \sum_{X_{j} \in S\left(X_{i}\right)} \frac{\beta_{i j} c_{i j}^{(r)}}{v_{j}^{2}}\right.\right. \\
& \left.\left.+\frac{\mu_{i}^{(0)}}{\sigma_{i}^{(0) 2}}\right)\right\}=N\left(\mu_{i}^{(R)}, \sigma_{i}^{(R) 2}\right)
\end{aligned}
$$

where $\mu_{i}^{(R)}=\sigma_{i}^{(R) 2}\left[\frac{\mu_{i}^{(0)}}{\sigma_{i}^{(0) 2}}+\sum_{r=1}^{R} \frac{a_{i}^{(r)}}{v_{i}^{2}}+\sum_{r=1}^{R} \sum_{X_{j} \in S\left(X_{i}\right)} \frac{\beta_{i j} c_{i j}^{(r)}}{v_{j}^{2}}\right]$ and $\frac{1}{\sigma_{i}^{(R) 2}}=\frac{1}{\sigma_{i}^{(0) 2}}+\frac{R}{v_{i}^{2}}+\sum_{X_{j} \in S\left(X_{i}\right)} \frac{R \beta_{i j}^{2}}{v_{j}^{2}}$, with $a_{i}^{(r)}=x_{i}^{(r)}-\sum_{X_{k} \in P a\left(X_{i}\right)} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)$ and $c_{i j}^{(r)}=\beta_{i j} x_{i}^{(r)}-\left(x_{j}^{(r)}-\mu_{j}\right)+\sum_{X_{k} \in P a\left(X_{j}\right) /\{X_{i}\}} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)$.

# D. 2 | Knowledge Learning for Cases with Mixing Data 

Except the case with complete production data discussed in Section D.1, we consider the cases with additional incomplete data corresponding to certain "Top Sub-Graph", denoted by $G\left(\mathbf{N}^{\prime} \mid \boldsymbol{\theta}\left(\mathbf{N}^{\prime}\right)\right)$ with $\mathbf{N}^{\prime} \subseteq \mathbf{N}$, such that any CQA node $X_{j} \in \mathbf{N}^{\prime}$ has $P a\left(X_{j}\right) \subset \mathbf{N}^{\prime}$. Since batch data collected from biopharmaceutical production process are usually limited, we want to fully utilize both complete and incomplete data to estimate the BN model coefficients and improve our knowledge of production process.

Without loss of generality, we consider the real-world data including two data sets $\mathcal{X}=\left\{\mathcal{X}_{1}, \mathcal{X}_{2}\right\}$ with the complete data $\mathcal{X}_{1}=\left\{\left(x_{1}^{\left(r_{1}\right)}, x_{2}^{\left(r_{1}\right)}, \ldots, x_{m+1}^{\left(r_{1}\right)}\right)\right.$ for $\left.r_{1}=1,2, \ldots, R_{1}\right\}$ and the incomplete data $\mathcal{X}_{2}=\left\{\left(x_{i}^{\left(r_{2}\right)}: X_{i} \in \mathbf{N}^{\prime}\right)\right.$ for $\left.r_{2}=R_{1}+1, R_{1}+2, \ldots, R\right\}$, where $R=R_{1}+R_{2}$. Our approach can be easily extended to cases with multiple in-

complete data sets. We use the same prior distribution $p\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)$ as shown in Equation (13). Given the mixing data $\mathcal{X}=\left\{\mathcal{X}_{1}, \mathcal{X}_{2}\right\}$, we can derive the posterior distribution of $\boldsymbol{\theta}$,

$$
p\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta} \mid \mathcal{X}\right) \propto \prod_{r_{1}=1}^{R_{1}}\left[\prod_{i=1}^{m+1} p\left(x_{i}^{\left(r_{1}\right)}\left|x_{P \#\left(X_{i}\right)}^{(r_{1})}\right)\right] \prod_{r_{2}=R_{1}+1}^{R}\left[\prod_{X_{i} \in \mathbf{N}^{\prime}} p\left(x_{i}^{\left(r_{2}\right)}\left|x_{P \#\left(X_{i}\right)}^{(r_{2})}\right)\right] p\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)\right.
$$

For $\beta_{i j}$ with $X_{j} \notin \mathbf{N}^{\prime}$ or $v_{i}^{2}$ and $\mu_{i}$ with node $X_{i} \notin \mathbf{N}^{\prime}$, the conditional posterior is the same as complete data case and we can utilize Equations (15), (16) and (17) by replacing $\mathcal{X}$ with $\mathcal{X}_{1}$.

Thus, to derive the full Gibbs sampler, we only need to provide the updated conditional posterior accounting for those nodes included in the incomplete data set $\mathcal{X}_{2}$. We first derive the conditional posterior distribution for weight coefficient $\beta_{i j}$ with $X_{j} \in \mathbf{N}^{\prime}$.

$$
\begin{aligned}
& p\left(\beta_{i j} \mid \mathcal{X}, \boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}_{-i j}\right) \propto\left[\prod_{r=1}^{R_{1}+R_{2}} p\left(x_{j}^{(r)}\left|x_{P \#\left(X_{j}\right)}^{(r)}\right)\right] p\left(\beta_{i j}\right) \\
& \propto \exp \left\{-\sum_{r=1}^{R_{1}+R_{2}} \frac{1}{2 v_{j}^{2}}\left[\left(x_{j}^{(r)}-\mu_{j}\right)-\beta_{i j}\left(x_{i}^{(r)}-\mu_{i}\right)-\sum_{k \in P \#(j) /(i)} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)\right]^{2}\right. \\
& \left.-\frac{1}{2 \tau_{i j}^{(0) 2}}\left(\beta_{i j}-\theta_{i j}^{(0)}\right)^{2}\right\} \\
& \propto \exp \left\{-\frac{1}{2 v_{j}^{2}} \sum_{r=1}^{R_{1}+R_{2}}\left(\alpha_{i}^{(r)} \beta_{i j}-m_{i j}^{(r)}\right)^{2}-\frac{1}{2 \tau_{i j}^{(0) 2}}\left(\beta_{i j}-\theta_{i j}^{(0)}\right)^{2}\right\} \\
& \propto \exp \left\{-\frac{\beta_{i j}^{2}}{2}\left(\sum_{r=1}^{R_{1}+R_{2}} \frac{\alpha_{i}^{(r) 2}}{v_{j}^{2}}+\frac{1}{\tau_{i j}^{(0) 2}}\right)+\beta_{i j}\left(\sum_{r=1}^{R_{1}+R_{2}} \frac{\alpha_{i}^{(r)} m_{i j}^{(r)}}{v_{j}^{2}}+\frac{\theta_{i j}^{(0)}}{\tau_{i j}^{(0) 2}}\right)\right\} \\
& =N\left(\theta_{i j}^{\left(R_{1}+R_{2}\right)}, \tau_{i j}^{\left(R_{1}+R_{2}\right) 2}\right)
\end{aligned}
$$

where $\theta_{i j}^{\left(R_{1}+R_{2}\right)}=\frac{\tau_{i j}^{(0) 2} \sum_{r=1}^{R_{1}+R_{2}} \alpha_{i}^{(r)} m_{i j}^{(r)}+v_{j}^{2} \theta_{i j}^{(0)}}{x_{i j}^{(0) 2} \sum_{r=1}^{R_{1}+R_{2}} \alpha_{i}^{(r) 2}+v_{j}^{2}}$ and $\tau_{i j}^{\left(R_{1}+R_{2}\right) 2}=\frac{\tau_{i j}^{(0) 2} v_{j}^{2}}{\tau_{i j}^{(0) 2} \sum_{r=1}^{R_{1}+R_{2}} \alpha_{i}^{(r) 2}+v_{j}^{2}}$ with $\alpha_{i}^{(r)}=x_{i}^{(r)}-\mu_{i}$ and $m_{i j}^{(r)}=\left(x_{j}^{(r)}-\mu_{j}\right)-\sum_{X_{k} \in P \#\left(X_{j}\right) /\left\{X_{i}\right\}} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right)$ for $r=1,2, \ldots, R$.

Then, we derive the conditional posterior distribution for $v_{i}^{2}$ with $X_{i} \in \mathbf{N}^{\prime}$,

$$
\begin{aligned}
& p\left(v_{i}^{2} \mid \mathcal{X}, \boldsymbol{\mu}, \boldsymbol{v}_{-i}^{2}, \boldsymbol{\beta}\right) \propto\left[\prod_{r=1}^{R_{1}+R_{2}} p\left(x_{i}^{(r)}\left|x_{P \#\left(X_{i}\right)}^{(r)}\right)\right] p\left(v_{i}^{2}\right) \\
& \propto \quad\left(v_{i}^{2}\right)^{-\left(R_{1}+R_{2}\right) / 2-\epsilon_{i}^{(0)} / 2-1} \exp \left\{-\frac{1}{2 v_{j}^{2}} \sum_{r=1}^{R_{1}+R_{2}}\left[\left(x_{i}^{(r)}-\mu_{i}\right)-\sum_{X_{k} \in P \#\left(X_{i}\right)} \beta_{k i}\left(x_{k}^{(r)}-\mu_{k}\right)\right]^{2}\right\} \\
& \propto \quad\left(v_{i}^{2}\right)^{-\left(R_{1}+R_{2}\right) / 2-\epsilon_{i}^{(0)} / 2-1} \exp \left\{-\frac{1}{2 v_{j}^{2}} \sum_{r=1}^{R_{1}+R_{2}} u_{i}^{(r) 2}-\frac{\lambda_{i}^{(0)}}{2 v_{j}^{2}}\right\} \\
& =\operatorname{Inv}-\Gamma\left(\frac{\epsilon_{i}^{\left(R_{1}+R_{2}\right)}}{2}, \frac{\lambda_{i}^{\left(R_{1}+R_{2}\right)}}{2}\right)
\end{aligned}
$$

where $\kappa_{i}^{\left(R_{1}+R_{2}\right)}=\kappa_{i}^{(0)}+R$ and $\lambda_{i}^{\left(R_{1}+R_{2}\right)}=\lambda_{i}^{(0)}+\sum_{r=1}^{R} u_{i}^{(r) 2}$ with $u_{i}^{(r)}=\left(x_{i}^{(r)}-\mu_{i}\right)-\sum x_{k} \in P_{a\left(X_{i}\right)} \beta_{k i}\left(x_{k}^{(r)}-\mu_{k}\right)$ for $r=1,2, \ldots, R$.

After that, we derive the conditional posterior for mean coefficient $\mu_{i}$ with $X_{i} \in \mathbf{N}^{\prime}$,

$$
\begin{aligned}
& p\left(\mu_{i} \mid \mathcal{X}, \boldsymbol{\mu}_{-i}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right) \propto p\left(\mu_{i}\right) \prod_{r=1}^{R_{1}+R_{2}} p\left(x_{i}^{(r)} \mid x_{P_{a\left(X_{i}\right)}^{(r)}}^{(r)}\right) \prod_{r_{1}=1}^{R_{1}} \prod_{X_{j} \in S\left(X_{i}\right)} p\left(x_{j}^{\left(r_{1}\right)} \mid x_{P_{a\left(X_{j}\right)}^{(r)}}^{(r)}\right) \\
& \cdot \prod_{r_{2}=R_{1}+1}^{R_{1}+R_{2}} \prod_{X_{j} \in S\left(X_{i}\right) \cap \mathbf{N}^{\prime}} p\left(x_{j}^{\left(r_{2}\right)} \mid x_{P_{a\left(X_{j}\right)}^{(r)}}^{(r)}\right), \\
& \propto \exp \left\{-\frac{1}{2 v_{i}^{2}} \sum_{r=1}^{R_{1}+R_{2}}\left[\left(x_{i}^{(r)}-\mu_{i}\right)-\sum_{X_{k} \in P_{a\left(X_{i}\right)}} \beta_{k i}\left(x_{k}^{(r)}-\mu_{k}\right)\right]^{2}\right. \\
& \left.-\sum_{r_{1}=1}^{R_{1}} \sum_{X_{j} \in S\left(X_{i}\right)} \frac{1}{2 v_{j}^{2}}\left[\left(x_{j}^{\left(r_{1}\right)}-\mu_{j}\right)-\sum_{X_{k} \in P_{a\left(X_{j}\right)}} \beta_{k j}\left(x_{k}^{\left(r_{1}\right)}-\mu_{k}\right)\right]^{2}\right. \\
& \left.-\sum_{r_{2}=R_{1}+1}^{R_{1}+R_{2}} \sum_{X_{j} \in S\left(X_{i}\right) \cap \mathbf{N}^{\prime}} \frac{1}{2 v_{j}^{2}}\left[\left(x_{j}^{\left(r_{2}\right)}-\mu_{j}\right)-\sum_{X_{k} \in P_{a\left(X_{j}\right)}} \beta_{k j}\left(x_{k}^{\left(r_{2}\right)}-\mu_{k}\right)\right]^{2}\right. \\
& \left.-\frac{1}{2 \sigma_{i}^{(0) 2}}\left(\mu_{i}-\mu_{i}^{(0)}\right)^{2}\right\} \\
& \propto \exp \left\{-\frac{\mu_{i}^{2}}{2}\left(\frac{R_{1}+R_{2}}{v_{i}^{2}}+\sum_{X_{j} \in S\left(X_{i}\right)} \frac{R_{1} \beta_{i j}^{2}}{v_{j}^{2}}+\sum_{X_{j} \in S\left(X_{i}\right) \cap \mathbf{N}^{\prime}} \frac{R_{2} \beta_{i j}^{2}}{v_{j}^{2}} \frac{1}{\sigma_{i}^{(0) 2}}\right)\right. \\
& \left.+\mu_{i}\left(\sum_{r=1}^{R_{1}+R_{2}} \frac{a_{i}^{(r)}}{v_{i}^{2}}+\sum_{r_{1}=1}^{R_{1}} \sum_{X_{j} \in S\left(X_{i}\right)} \frac{\beta_{i j} c_{i j}^{\left(r_{1}\right)}}{v_{j}^{2}}+\sum_{r_{2}=R_{1}+1}^{R} \sum_{X_{j} \in S\left(X_{i}\right) \cap \mathbf{N}^{\prime}} \frac{\beta_{i j} c_{i j}^{\left(r_{2}\right)}}{v_{j}^{2}}+\frac{\mu_{i}^{(0)}}{\sigma_{i}^{(0) 2}}\right)\right\}, \\
& =N\left(\mu_{i}^{\left(R_{1}+R_{2}\right)}, \sigma_{i}^{\left(R_{1}+R_{2}\right) 2}\right) \\
& \mu_{i}^{\left(R_{1}+R_{2}\right)}=\sigma_{i}^{\left(R_{1}+R_{2}\right) 2}\left[\frac{\mu_{i}^{(0)}}{\sigma_{i}^{(0) 2}}+\sum_{r=1}^{R_{1}+R_{2}} \frac{a_{i}^{(r)}}{v_{i}^{2}}+\sum_{r_{1}=1}^{R_{1}} \sum x_{j} \in S\left(X_{i}\right) \frac{\beta_{i j} c_{i j}^{\left(r_{1}\right)}}{v_{j}^{2}}+\right. \\
& \left.\sum_{r_{2}=R_{1}+1}^{R} \sum x_{j} \in S\left(X_{i}\right) \cap \mathbf{N}^{\prime} \frac{\beta_{i j} c_{i j}^{\left(r_{2}\right)}}{v_{j}^{2}}\right], \text { and } \frac{1}{\sigma_{i}^{\left(R_{1}+R_{2}\right) 2}}=\frac{1}{\sigma_{i}^{(0) 2}}+\frac{R_{1}+R_{2}}{v_{i}^{2}}+\sum x_{j} \in S\left(X_{i}\right) \frac{R_{1} \beta_{i j}^{2}}{v_{j}^{2}}+\sum x_{j} \in S\left(X_{i}\right) \cap \mathbf{N}^{\prime} \frac{R_{2} \beta_{i j}^{2}}{v_{j}^{2}} \text { with } \\
& a_{i}^{(r)}=x_{i}^{(r)}-\sum x_{k} \in P_{a\left(X_{i}\right)} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right) \text { and } c_{i j}^{(r)}=\beta_{i j} x_{i}^{(r)}-\left(x_{j}^{(r)}-\mu_{j}\right)+\sum x_{k} \in P_{a\left(X_{j}\right) /\left(X_{i}\right)} \beta_{k j}\left(x_{k}^{(r)}-\mu_{k}\right) \text { for } r=1,2, \ldots, R \text {. }
\end{aligned}
$$

Here for illustration, we have only provided the conditional posteriors with two datasets $\mathcal{X}_{1}$ and $\mathcal{X}_{2}$. These derivations can be easily extended to similar cases with multiple datasets collected from complete graph and different top subgraphs.

# D. 3 | Gibbs Sampling Procedure for BN Model Bayesian Inference 

Based on the derived conditional posterior distributions in Sections D. 1 and D.2, we provide the Gibbs sampling procedure in Algorithm 3 to generate posterior samples $\widehat{\boldsymbol{\theta}}^{(b)} \sim p(\boldsymbol{\theta} \mid \mathcal{X})$ with $\widehat{\boldsymbol{\theta}}^{(b)}=\left(\widehat{\boldsymbol{\mu}}^{(b)}, \widehat{\boldsymbol{v}}^{(b) 2}, \widehat{\boldsymbol{\beta}}^{(b)}\right)$ and $b=$ $1, \ldots, B$. We first set the vague prior $p(\boldsymbol{\theta})=p\left(\boldsymbol{\mu}, \boldsymbol{v}^{2}, \boldsymbol{\beta}\right)$ as Equation (13), and generate the initial point $\boldsymbol{\theta}^{(0)}=$ $\left(\boldsymbol{\mu}^{(0)}, \boldsymbol{v}^{(0) 2}, \boldsymbol{\beta}^{(0)}\right)$ by sampling from the prior. Within each $t$-th iteration of Gibbs sampling, given the previous sample $\boldsymbol{\theta}^{(t-1)}=\left(\boldsymbol{\mu}^{(t-1)}, \boldsymbol{v}^{(t-1) 2}, \boldsymbol{\beta}^{(t-1)}\right)$, we sequentially compute and generate one sample from the conditional posterior dis-

tribution for each coefficient $\beta_{i j}, v_{i}^{2}$ and $\mu_{i}$. By repeating this procedure, we can get samples $\boldsymbol{\theta}^{(t)}=\left(\boldsymbol{\mu}^{(t)}, \boldsymbol{v}^{(t) 2}, \boldsymbol{\beta}^{(t)}\right)$ with $t=1, \ldots, T$. To reduce the initial bias and correlations between consecutive samples, we remove the first $T_{0}$ samples and keep one for every $h$ samples. Consequently, we obtain the posterior samples $\widetilde{\boldsymbol{\theta}}^{(b)} \sim p(\boldsymbol{\theta} \mid \mathcal{X})$ with $b=1, \ldots, B$.

```
Algorithm 3: Gibbs Sampling Procedure for BN Model Uncertainty Quantification
    Input: the prior \(p(\boldsymbol{\theta})\) and real-world data \(X\).
    Output: Posterior samples \(\widetilde{\boldsymbol{\theta}}^{(b)}=\left(\widetilde{\boldsymbol{\mu}}^{(b)}, \widetilde{\boldsymbol{v}}^{(b) 2}, \widetilde{\boldsymbol{\beta}}^{(b)}\right) \sim p(\boldsymbol{\theta} \mid \mathcal{X})\) with \(b=1, \ldots, B\).
    (1) Set the initial value \(\boldsymbol{\theta}^{(0)}=\left(\boldsymbol{\mu}^{(0)}, \boldsymbol{v}^{(0) 2}, \boldsymbol{\beta}^{(0)}\right)\) by sampling from prior \(p(\boldsymbol{\theta})\);
    for \(t=1,2, \ldots, T\) do
        (2) Given the previous sample \(\boldsymbol{\theta}^{(t-1)}=\left(\boldsymbol{\mu}^{(t-1)}, \boldsymbol{v}^{(t-1) 2}, \boldsymbol{\beta}^{(t-1)}\right)\);
        (3) For each \(\beta_{i j}\), generate \(\beta_{i j}^{(t)} \sim p\left(\beta_{i j} \mid \mathcal{X}, \beta_{i 2}^{(t)}, \ldots, \beta_{i, j-1}^{(t)}, \beta_{i, j+1}^{(t-1)}, \ldots, \beta_{m, m+1}^{(t-1)}, \boldsymbol{\mu}^{(t-1)}, \boldsymbol{v}^{(t-1) 2}\right)\) through Equation (15) for
        complete data or (34) for mixing data;
        (4) For each \(v_{i}^{2}\), generate \(v_{i}^{(t) 2} \sim p\left(v_{i}^{2} \mid \mathcal{X}, \boldsymbol{\beta}^{(t)}, v_{i}^{(t) 2}, \ldots, v_{i-1}^{(t) 2}, v_{i+1}^{(t-1) 2}, \ldots, v_{m+1}^{(t-1) 2}, \boldsymbol{\mu}^{(t-1)}\right)\) ) through Equation (16) for
        complete data or (35) for mixing data;
        (5) For each \(\mu_{i}\), generate \(\mu_{i}^{(t)} \sim p\left(\mu_{i} \mid \mathcal{X}, \boldsymbol{\beta}^{(t)}, \boldsymbol{v}^{(t) 2}, \mu_{1}^{(t)}, \ldots, \mu_{i-1}^{(t)}, \mu_{i+1}^{(t-1)}, \ldots, \mu_{n}^{(t-1)}\right)\) through Equation (17) for
        complete data or (36) for mixing data;
        (6) Obtain a new posterior sample \(\boldsymbol{\theta}^{(t)}=\left(\boldsymbol{\mu}^{(t)}, \boldsymbol{v}^{(t) 2}, \boldsymbol{\beta}^{(t)}\right)\);
```

(7) Set $\widetilde{\boldsymbol{\theta}}^{(b)}=\boldsymbol{\theta}\left(T_{0}+(b-1) h+1\right)$ with some constant integer $T_{0}$ and $h$, to reduce the initial bias and correlation between consecutive samples.

# E | SIMULATED BIOPHARMACEUTICAL PRODUCTION DATA 

To study the performance of proposed framework, we generate the simulated production process data $\mathcal{X}$, which mimics the "real-world data collection." The BN with coefficients $\boldsymbol{\theta}^{c}$ characterizing the underlying production process interdependence is used for data generation, which is built according to the biomanufacturing domain knowledge. The ranges of CPPs/CQAs are listed Table 9. For each CPP $X_{j} \in \mathbf{X}^{p}$ with range $\left[x_{j}^{\text {low }}, x_{j}^{u p}\right]$, we can specify the marginal distribution $X_{j} \sim N\left(\mu_{j}^{c},\left(v_{j}^{c}\right)^{2}\right)$ with mean $\mu_{j}^{c}=\left(x_{j}^{\text {low }}+x_{j}^{u p}\right) / 2$ and standard deviation $v_{j}^{c}=\left(x_{j}^{u p}-x_{j}^{\text {low }}\right) / 4$. For each CQA $X_{i} \in\left\{\mathbf{X}^{p} \cup \mathbf{Y}\right\}$ with range $\left[x_{i}^{\text {low }}, x_{i}^{u p}\right]$, we have mean $\mu_{i}^{c}=\left(x_{i}^{\text {low }}+x_{i}^{u p}\right) / 2$ and marginal variance $\operatorname{Var}\left(X_{i}\right)=\left[\left(x_{i}^{u p}-x_{i}^{\text {low }}\right) / 4\right]^{2}$. Based on Equation (12), the corresponding coefficient $v_{i}^{c}$ can be computed through back-engineering. For the complex interdependence, Table 10 provides the relative associations with levels (i.e., high, median, low) between input CPPs/CQAs with output CQAs in each operation unit, which is built based on the "cause-and-effect matrix" in Mitchell (2013). For the high, median and low association between $X_{i}$ to $X_{j}$, we set the coefficient $\beta_{i j}^{c}=0.9,0.6,0.3$ respectively. Thus, we can specify the underlying true coefficients $\boldsymbol{\theta}^{c}=\left(\boldsymbol{\mu}^{c},\left(\boldsymbol{v}^{2}\right)^{c}, \boldsymbol{\beta}^{c}\right)$. To mimic the "real-world" data collection, we generate the production batch data $\mathcal{X}$ using the BN model with $\boldsymbol{\theta}^{c}$. Then, to assess the performance of proposed framework, we assume that the true coefficient values are unknown.

## F | STUDY THE BAYESIAN LEARNING AND INFERENCE

To evaluate the accuracy and efficiency of proposed Bayesian learning, we empirically study the convergence of BN coefficient inference. In each $k$-th macro-replication, we first mimic the "real-world" production batch data collection through generating $\mathcal{X}^{(k)}=\left\{\mathbf{X}_{1}^{(k)}, \ldots, \mathbf{X}_{R}^{(k)}\right\}$ with $\mathbf{X}_{i}^{(k)} \sim F\left(\mathbf{X} \mid \boldsymbol{\theta}^{c}\right)$ for $i=1, \ldots, R$ and $k=1, \ldots, K$. Then, we generate

TABLE 9 Range of CPPs/CQAs in the production procedure.


$B$ posterior samples $\overline{\boldsymbol{\theta}}^{(k, b)} \sim p\left(\boldsymbol{\theta} \mid X^{(k)}\right)$ with $b=1,2, \ldots, B$. For the Gibbs sampler in Algorithm 3 provided in online Appendix D.3, we set the initial warm-up length $T_{0}=500$ and step-size $h=10$. With different size of complete "real-world" batch data $R=30,100,500$, we compute the mean squared error (MSE) for each coefficient $\theta_{\ell} \in \boldsymbol{\theta}$ : $\operatorname{MSE}\left(\theta_{\ell}\right)=\iint\left(\theta_{\ell} \sim \theta_{\ell}^{c}\right)^{2} d P\left(\theta_{\ell} \mid X\right) d P\left(X \mid \boldsymbol{\theta}^{c}\right)$. Based on $K=20$ macro-replications and $B=1000$ posterior samples of BN coefficients, we estimate $\operatorname{MSE}\left(\theta_{\ell}\right)$ with $\widetilde{\operatorname{MSE}}\left(\theta_{\ell}\right)=\frac{1}{K B} \sum_{k=1}^{K} \sum_{b=1}^{B}\left(\widetilde{\theta}_{\ell}^{(k, b)} \sim \theta_{\ell}^{c}\right)^{2}$. Since the total number of coefficients is large, we further group coefficients by mean $\boldsymbol{\mu}$, conditional variance $\boldsymbol{v}^{2}$ and linear coefficients $\boldsymbol{\beta}$, and take average of the sample MSE respectively: $\widetilde{\operatorname{MSE}}(\boldsymbol{\mu})=\frac{1}{|\boldsymbol{\mu}|} \sum_{\theta_{\ell} \in \boldsymbol{\mu}} \widetilde{\operatorname{MSE}}\left(\theta_{\ell}\right), \widetilde{\operatorname{MSE}}\left(\boldsymbol{v}^{2}\right)=\frac{1}{\left|\boldsymbol{v}^{2}\right|} \sum_{\theta_{\ell} \in \boldsymbol{v}^{2}} \widetilde{\operatorname{MSE}}\left(\theta_{\ell}\right)$, and $\widetilde{\operatorname{MSE}}(\boldsymbol{\beta})=\frac{1}{|\boldsymbol{\beta}|} \sum_{\theta_{\ell} \in \boldsymbol{\beta}} \widetilde{\operatorname{MSE}}\left(\theta_{\ell}\right)$. The corresponding results are reported in Table 11. As the size of real-world data $R$ increases, the average MSE decreases, which implies the posterior samples obtained by Gibbs sampling procedure can converge to the true coefficients.

TABLE 10 Relative association between input CPPs/CQAs with output CQAs in each process unit operation.


TABLE 11 The MSE of $\boldsymbol{\mu}, \boldsymbol{v}^{2}$ and $\boldsymbol{\beta}$ esimated by using the Gibbs sampling.
