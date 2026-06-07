# Safety Analysis of Offshore Decommissioning Operation through Bayesian Network 

Ahmed O. Babaleye and Rafet E. Kurt<br>Department of Naval Architecture, Ocean and Marine Engineering, University of Strathclyde, Glasgow, G4 0LZ, United Kingdom

## Corresponding author

ahmed.babaleye@strath.ac.uk
$+44(0) 1415484776$
ORCID ID: https://orcid.org/0000-0002-4104-956X


#### Abstract

Decommissioning of offshore platforms is becoming increasingly popular. The removal of these heavy steel structures is characterised by high risks that may compromise personnel safety and loss of assets. The removal operation relies on dedicated barges and heavy lift vessels that may descent or capsize because of mechanical or structural failure. The knowledge of associated hazards is driven by experience and failure data are often obtained empirically through analogous operations, which further introduces uncertainty to the risk analysis. This paper proposes an integrated safety analysis approach for conducting decommissioning risk analysis of offshore installations. The approach incorporates hierarchical Bayesian analysis (HBA) with Bayesian network (BN) to assess the accident causations leading to futile decommissioning operation. First, the overall system failure of a lifting vessel was reviewed with emphasis on where safety issues arise. In addition, the failure data obtained from expert judgements were aggregated through statistical distribution based on HBA. The aggregated failure data are then used to conduct dynamic safety analysis using BN, to assess and evaluate the risks of offshore jacket removal operations. The accident model is illustrated with a case study from Brent Alpha decommissioning technical document to demonstrate the capability of incorporating HBA with BN to conduct risk analysis.


Keywords: Bayesian networks; decommissioning; safety analysis; offshore jacket structures; hierarchical Bayesian analysis.

Subject classification codes: decommissioning; risk analysis

## 1. Introduction

The decommissioning of offshore oil and gas facility is attracting attention around the world resulting in demands for increased lifting vessels' performance. As a result, heavy lift vessels

(HLVs) or dedicated lifting barges are often required. These HLVs and lifting barges may descent or capsize if all inherent and external hazards are not fully captured or during unplanned severe weather conditions leading to accidents such as collision or loss of stability.

Some notable lifting operational accidents have been recorded in recent times. For example, On 20th August 1990, the West Gamma accommodation jack-up rig also capsized while being transported from the Norwegian continental shelf to the German sector. Severe weather caused the rig to drift towards the German coast and descent eventually. While lives were not lost, structural failure, loss of towline and flooding were identified as the main causes of the accident (Vinnem, 2007).

More recently, a typhoon experienced during the CNOOC Offshore Oil 298 project during transportation resulted to 68 fatalities in 2006 (Fang and Duan, 2014). Due to these technical and environmental challenges associated with heavy lifting operations, it is important to ensure highlevel of safety during decommissioning. However, one major issue is the sparsity of failure data on near misses, incidents and accidents related to offshore decommissioning operations. Where there are such data, their usage is limited due to vagueness caused by irregular inspection records while operational and management of change.

Many of the risk analysis conducted on already completed decommissioning activities are experience-driven and failure data used for such analysis are often obtained from expert judgements or from analogous activities such as mining, nuclear and aerospace decommissioning domain. The data collected from these sources can only yield desirable outcomes when aggregated. In addition, the complete hazard identification and operability analysis on lifting operation incorporating offshore jacket removal and HLVs/barges have not been given much attention. Although Abdussamie et al. (2018) studied the offshore barges transportation problem with focus on hazard identification and fuzzy set theory, the work focused on semi-quantitative risk assessment. However, quantitative risk assessment capable of quantifying the risks of decommission in its entirety is necessary (Wang and Pedersen, 2007).

Offshore lifting operation performance measures include collision (or drifting), loss of stability (or buoyancy) and ascent (or descent). This performance measures represent important inputs during decommissioning planning phase and the ability to predict the risk tolerance level for which a futile decommissioning operation is imminent have continue to be desirable, especially for HLVs and barges (Van Hoorn, 2008). While the safety of conventional offshore lifting operations has been addressed in literature, those relating to decommissioning have not been explored thus far. For instance, the Joint Industrial Projects (JIP) studies conducted on safety cultural assessment of decommissioning offshore installations in the UK continental shelf between 2005 and 2015 (Fig.

1), indicated that there have been no fatalities recorded in the North Sea decommissioning projects till date but most of the recorded incidents identified structural damage as the predominant cause. Therefore, it is necessary to develop a systematic safety approach based on realistic data collection and analysis to conduct quantitative risk assessment for this challenging activity.

Figure 1: Decommissioning incidents from 2005-2015 (OGUK 2015).

The safety of decommissioning operation is relative, and the context can vary between regions due to different weather conditions and associated hazards, making it one of accident-prone rare events. The lifting barge and the aged jacket structure to be lifted both present unique hazards. For example, the remaining useful life (RUL) of the jacket structure cannot be ascertained and its lifting nodes, hidden flaws, flooded members and accumulated hazardous materials inside the columns and bracings are all variables of uncertainties. Due to these potential unknowns, the probability of futile decommissioning failure would require statistical distribution of data obtained from different sources including expert opinions. To achieve this, Hierarchical Bayesian analysis (HBA) where all failure data can be aggregated and presented as a mean of a distribution is required to successfully predict and mitigate overall failure. Many authors have studied the safety challenges of decommissioning offshore oil and gas installations and assessed the associated risks using variants of quantitative risk analysis (QRA) techniques such as fuzzy reliability theory within fault tree analysis to address subjectivity of failure data (Lavasani et al., 2015; Purba, 2014; Deshpande, 2011); event tree analysis and its bow-tie extension (Ferdous et al., 2013); Safety critical task approach (Bradbeer et al., 2009; Kierans et al., 2004).

While the conventional QRA techniques have been extensively used in the installation, production, drilling and operational risk assessments, their capability to handle systems with uncertain failure data have limited their applicability. Moreover, the results obtained from such techniques cannot be flexibly adapted or updated when new evidence becomes available as the decommissioning operation progresses. To address these limitations, an integrated hierarchical Bayesian analysis (HBA) with Bayesian Network (BN) model of the failure analysis is proposed. The HBA can aggregate the data obtained from different sources (called, source-to-source variability) and expert judgements in the form of a mean value over a distribution (El-Gheriani et al, 2017a). Recently, Mishra et al (2018) applied HBA model to predict the remaining useful life of Lithium-ion batteries through prognosis. El-Gheriani et al (2017b) developed an HBA model to assess the risks of rare events with focus on process systems safety and found that the application of HBA is, especially, suitable for handling uncertainties associated with source-to-source

variability of data. The main justification for adopting HBA in this study is due to its potential to account for both component- and system-level variations in data. In addition, HBA can work with sparse failure data to produce reasonable probability estimates up to $95 \%$ credible interval (Kruschke, 2014; Gelman and Hill, 2007; Gelman et al., 2004).

BN can provide an up-to-date assessment of the decommissioning operation, making the proposed methodology robust for conducting probabilistic risk analysis. The BN is capable of assessing and reassessing risk through updating prior failure probabilities of primary (causation) events whenever one or more uncertainties have been mitigated, or when new knowledge of the risk becomes available (Faber et al., 2002). Recently, Babaleye et al. (2018) tested accident precursor data within BN to investigate the most probable cause of a futile decommissioning operation using experiential learning methodology. More discussions on the advantages, capabilities and applications of dynamic quantitative risk analysis including methodologies to obtain and validate probabilistic data can be found in (Golam et al., 2016; Rathnayaka et al., 2013; Khakzad et al., 2011; Rathnayaka et al., 2011; Bearfield and Marsh, 2005). It is worth mentioning that none of the above-mentioned studies examined the risks of offshore decommissioning such as jacket structures removal.

The present paper aims to analyse the hazards inherent in a complete offshore jacket removal operational sequence using hierarchical Bayesian analysis (HBA) incorporated with Bayesian networks to conduct probabilistic risk assessment. The data consists of key failure frequencies obtained from similar operations such as mining, aerospace and nuclear decommissioning and experts judgements based on their field experience. The case study presented in this paper illustrates the application of the HBA model for aggregating the failure data to provide reasonable estimates of the occurrence probability for each accident causation leading to a futile decommissioning operation.

This paper is organised as follows: Section 2 emphasises the critical nature of decommissioning aged offshore platforms while Section 3 introduces the case study used in this study based on Brent Alpha technical documentation. The safety assessment methodology which incorporates the HBA to aggregate failure data with BN to conduct risk analysis is presented in Section 4. Section 5 presents the model safety analysis and Section 6 reviews the summary of the study.

# 2. Critical nature of aged platforms 

The uncertainties associated with all aged offshore structures vary depending on a number of factors such as location, weather conditions, and technicalities of the design, among others. However, these structures share many other safety issues such as unknown material strength,

technical background and experience level of the decommissioning personnel. Therefore, a safety framework must be developed that would be able to capture all uncertainties and reasonably estimate their failure probabilities from small data size. A typical example used as a case study in this paper is the Brent Alpha jacket (BAJ). Redpath Dorman Long built BAJ in Scotland and installed in the Brent Field within the UK continental shelf, by Heerema Limited in May 1976. At the time of removal, knowledge of its current condition was limited. Like many of the old structures built in the 1970s and 1980s, its future removal from the seabed was not considered and this, especially, contributed to the variables of uncertainty during decommissioning phase. For instance, during the jackets operating life, many of the conductors have been repaired, including, some that have undergone modifications. These modifications added to the safety challenges during the end-of-life planning phase. In addition, there were 28 self-supporting and laterally restrained conductors driven approximately 100 m into the seabed, which further contributed to the increase in jacket weight over time. The design life was 30 years, but the jacket was in service for 41 years, until removal in 2017. Therefore, the remaining useful life (RUL) of the jacket structure was not known due to accumulated fatigue loads and corrosion. In addition, a number of caissons, clamps and other appurtenances have been incorporated or dismembered during its service life (Shell, 2017).

The main processes of the complete removal operation of a steel jacket structure from the fixed position offshore to a recycling yard onshore using lifting barges or HLVs is as shown in Fig. 2. More information about the safety issues on the lifting barges and HLVs can be found in the works of Abdussamie et al. (2018) and Tan et al. (2018). It is worth mentioning that only the decommissioning hazards relating to the steel jacket structure is considered in this paper.

Figure 2. Main process of steel jacket decommissioning operation.
At each stage of this process, several hazards are identified and experts' opinion on the failure frequencies are obtained from source-to-source and recorded.

# 3. Safety Model Description 

The safety analysis of decommissioning steel piled jacket (SPJ) structures for complete removal operations is identified and analysed according to literature reviews (Kierans et al., 2004; Bradbeer et al., 2009; BP,2011; OGUK, 2015) and hazard identification conducted on the operational sequence from decommissioning professionals based on their field experience. To determine the risk of decommissioning offshore jacket structures, all the potential accident

scenarios have to be captured, analysed and assessed in an integrated manner. Therefore, fault tree (FT) is developed to represent the accident causations of complete removal of SPJs.

# 3.1 Operational steps involved in decommissioning 

Step 1. A route survey is first conducted to determine the locations to position and sever the jacket sections including the transportation route. The survey also identifies uncharted things underwater such as ship wreck, oyster beds etc.

Step 2. The topside is removed, and piles and conductors severed. The SPJ is the cut and removed in sections that the dedicated HLV can sustain. The SPJ may be made buoyant or deballasted to reduce the bottom weight. A suitable severance method is selected based on the technical capabilities available and carried out underwater by divers or remotely operated vehicles.

Step 3. The HLV is then rigged to individual module previously severed, removes each SPJ module and loads it to the barge until the SPJ is completely removed. It is worth mentioning that these steps can vary depending on factors such as platform age, location and water depth, platform type and configuration, weight of the lifts and soil strength, among others.

### 3.2 Model hazards identification

Collision or drift. The collision or drift between the jacket and lifting barge can lead to a futile jacket decommissioning operation as it may result in fire and explosion. Typically, the risk increases when either the lifting barge moves farther from the payload or, both the lifting barge and the payload collide. The lack of decommissioning historic data has necessitated the adoption of hierarchical Bayesian analysis integrated with Bayesian network, which is a proven risk analysis tool for estimating the failure probabilities of abnormal events under uncertainty.

Loss of stability. The overall effect of this collision alone is independent of whether the lifting vessel capsize due to the misalignment of the jacket's center of gravity (CoG) and its center of buoyancy $(\mathrm{CoB})$. Improper cutting of the pile in the footings can lead to the differential sticking of pile or stuck-pipe and consequently results to capsize.

Ascent or descent. A cut performed in accordance with recommended practice may help to prevent descent or capsize of the lifting vessel; hence, it is situated beside the CoB and CoG in the fault tree in Figure 3, which considers the complete jacket removal activity including footings and pile severance. The exact calculation of CoG can be difficult due to the presence of marine growth, unknown residual anode thickness and corrosion thinning. The residual anode may be replaced prior to jacket removal to reduce the number of uncertain variables. Internal and external corrosion thinning are independent events, and the presence of either of them can pose a technical challenge. Grouting prevents the occurrence of flooding in the inner walls of the jacket and pontoon legs. It is, therefore, an important requirement to ascertain the grout's integrity against deterioration and

consequently, prevents internal corrosion thinning. Cathodic protection and coating of such an aged jacket structure are expected to have deteriorated or fail at the instant of removal. They both prevent external corrosion thinning by absorbing soil corrosion effect on the external surface.

Structural damage. The structural failure caused by accumulated cyclic load, lifting point failure, bulk explosion and structural loading on the jacket is capable of initiating collision even in the absence of overloading of the lifting crane or barge operational failure (Zhao et al., 2015; Gerwick, 2002). This is particularly due to the breakage of a lifting node on the structure during lifting. The lifting node breakage is imminent if its residual strength is unknown or calculated incorrectly.

To overcome the occurrence of crane overload, the rigging and initial lift-off force due to soil adhesion calculations must be accurate.

Figure 3. Fault tree representation of accident model.

# 4. Proposed QRA Methodology 

### 4.1 Hazard Identification and Modelling

The system failure during the steel jacket removal operation is analysed through hazard identification (HAZID) procedure described in section 3.2. HAZID is conducted with industry experts from mid- to senior engineers and academic professionals with considerable decommissioning operational knowledge. The process involves subdividing the removal and lifting operation as shown in Table 1. In this paper, emphasis is placed on the lifting safety issues associated with collision (or drifting), loss of stability (or buoyancy) and ascent (or descent). These failures and their causes are used to construct the Bayesian networks used for the risk assessment.

Table 1. Hazard identification during offshore jacket removal.

### 4.2 Data Collection and Processing

Pursuant to the system failure identification and the relationships between the primary events and their child event(s), failure data are then collected from source-to-source as shown in Table 2. As these data are sparse, the distribution is assumed to follow the Gaussian formalism with known mean and variance (Kelly and Smith, 2011). The distribution represents what is known about the failure event and is called informative prior. The aggregated failure probability can be obtained as follow:

$$
p\left(x_{i}\right)=\operatorname{bin}\left(p_{i}, n_{i}\right)
$$

$$
\begin{gathered}
p_{\text {avg }}\left(p_{i}\right)=\text { beta }(\alpha, \beta) \\
\alpha=\text { gampdf }(\mu, \sigma) \\
\beta=\text { gampdf }(\mu, \sigma)
\end{gathered}
$$

where $x_{i}=$ number of failures
$p_{i}=$ parameter of interest e.g. failure rate or failure probability
$n_{i}=$ number of trials or demands
$\alpha=$ shape parameter
$\beta=$ scale parameter
$\mu, \sigma=$ mean and standard deviation, both assumed to equal 1.00e-4.

# 4.3 Analysing overall probability within BN 

Bayesian network (BN) is a very important probabilistic tool broadly used where uncertainty in accident modelling exists. It utilises a robust computation engine to handle risks in both qualitative and quantitative manner. The BN is capable of handling insufficient failure data as it can be updated when new knowledge or evidence become available (Khakzad et al, 2013). Bobbio et al (2001) proposed a comprehensive method, which can be used for converting accident causes in form of a fault tree (FT) into BN. This conversion algorithm maps all primary, intermediate and top events into corresponding root, intermediate and pivot (or leaf) nodes, respectively. The computation in a BN is based on Bayes' theorem and the d-separation norm (Jensen and Nielsen, 2007). The dependency between the nodes is defined by the conditional probability table (CPT). Consider Fig. 4 with the conditional dependency of discrete variables, the BN represents the joint probability distribution $P(U)$ of variables $U=\left\{Y_{1}, \ldots, Y_{n}\right\}$, given by:

$$
P(U)=\prod_{i=1}^{n} P\left(Y_{i} \mid P a\left(Y_{i}\right)\right)
$$

where $P a\left(Y_{i}\right)=$ parents of variable $Y_{i}$
$Y_{i}=$ nodes of the network,
$P(U)=$ Joint failure probability of the network
Figure 4. A typical BN with 5 nodes.

### 4.4 Updating belief with new evidence

A BN can be used to execute a forward (or predictive) and backward (or diagnostic) analysis. In the predictive analysis, the prior probabilities of intermediate and leaf nodes are computed from

the marginal prior probabilities of root nodes (causations) and the conditional probabilities of intermediate nodes obtained based on leaky noisy-OR logic within the CPT. The probability distribution obtained through HBA will be assigned as the marginal prior probability distribution for each root node in the BN and updating is performed to obtain the posterior probability. When new data become available for selected nodes, the nodes will be updated, and the overall failure probability can be reassessed. For the diagnostic analysis, the futile decommissioning operation, modelled as the top event must be set to either safe or fail state to update the probability of the root nodes. In both cases of forward or backward propagation, Eq. (3) is used to compute the probability updating.

$$
P(U \mid E)=\frac{\mathrm{P}(U, E)}{\mathrm{P}(E)}=\frac{\mathrm{P}(U, E)}{\sum_{U} P(U, E)}
$$

where $P(U \mid E)=$ probability of accident given new evidence $E$
$\mathrm{P}(E)=$ probability of new evidence
$\sum_{U} P(U, E)=$ normalising factor

One way to obtain new evidence for the accident causations is through Eq. (4) and the updated probability is computed using Eq. (5).

$$
\begin{aligned}
x_{i}^{+} & =N_{i} \cdot p\left(x_{i}\right) \\
p\left(x_{i}^{+}\right) & =\frac{\alpha_{\mu}+x_{i^{+}}}{\alpha_{\mu}+\beta_{\mu}+N_{i}}
\end{aligned}
$$

where $x_{i}^{+}=$expected number of accident causation occurrence
$N_{i}=$ Number of demands (e.g. number of lifting operation)
$p\left(x_{i}\right)=$ obtained predictive posterior probability from distribution
$\alpha_{\mu}, \beta_{\mu}=$ mean values of the shape and scale hyper parameters, respectively

# 5. Model Safety Analysis 

Figure 3 presents the FT model for the complete decommissioning operation of SPJs, while Figure 6 depicts the corresponding BN based on similitude mapping techniques discussed in section 4.3. In this study, the BN is developed and analysed using GeNIe 2.1 (http://genie.sis.pitt.edu).

# 5.1 Obtaining failure probabilities hierarchically 

Data sparsity for quantifying risk is a major concern in the offshore decommissioning industry and risk analysis has been driven by experience. Therefore, the prior failure probabilities assigned to the root nodes described in this model are obtained from 10 data points assumed to have been obtained from analogous operations and distributed over a gamma function with $95 \%$ confidence level, as presented in Table 2. The prior failure probabilities represent the mean value of the distribution, making the estimated values credible. The number of occurrences for each primary event is modelled hierarchically as described in Eq. (1) to provide a distribution for the occurrence probability. The HBA formulation is coded in MATLAB as shown in Fig. 5 and Fig. 6 represents the estimated occurrence probabilities of each causation events.

Table 2. Primary events source-to-source failure data.
Figure 5. MATLAB algorithm for estimating occurrence probabilities.
Figure 6. Estimated occurrence probabilities for individual causations.

### 5.2 Calculating overall failure probability

One of the benefits of estimating uncertainties using BN in terms of CPTs is because the dependencies among interacting events can be represented. In addition, the weak links and the safety critical events contributing to the overall failure can be identified. The occurrence probability of each primary event is assigned to the BN (Fig. 7) taking into consideration the dependencies based on leaky noisy-OR logic (Adedigba et al., 2016), as shown in Fig. 8.

Figure 7. BN model for futile decommissioning operation.
Figure 8. Conditional dependency table for node 22.
Running the analysis yields an overall occurrence probability of a futile decommissioning operation of 0.6333 , caused by $27.2 \%$ occurrence probability of capsize/descent of the lifting barge and $19.2 \%$ occurrence probability of the collision/drift.

### 5.3 Probability updating Analysis

The updating analysis is performed by feeding the causation events with new evidence obtained through the predictive posteriors discussed in section 4.4, Eq. (4). Assuming an observed evidence of $X_{4}$ (equipment failure), $X_{5}$ (human error), $X_{19}$ (installation flooding) and $X_{26}$ (marine growth effect) events occurrences over 18 number of lifting operations during the decommissioning activity. Eq. (5) will be used to obtain the mean distribution of these events and feed into BN to recalculate the top event occurrence probability. The top event (futile decommissioning operation failure probability) occurrence probability is updated in the BN to be

0.0820. For example, given $\alpha_{\mu}=\beta_{\mu}=1$, the new occurrence probability of equipment failure would be $p^{+}\left(x_{4}\right)=(0.0412 * 18) * 1 /(1+1+18)=0.0371$. The updated probability (Table 3) is attributed to the potential of the HBA technique to provide valuable information with credible level where measurable failure data are not available during the decommissioning planning phase.

Table 3. Updated probability of causations with new evidence.

# 5.4 Diagnostic Safety Analysis 

The diagnostic analysis (backward propagation) is performed by setting the top event occurrence probability node to a "failed" state to obtain posterior probability for each root node i.e. $p($ root events $\mid$ top event $=\{f$ ail $\})$. The backward analysis provides a comprehensive way for estimating real-time information of causations when one or more of the uncertainties have been reduced or a new evidence is known. The posterior probabilities obtained for the primary events are the most probable values at the instance the observed accident occurs. In Table 3, it can be observed that flooded members and uneven flooding are the causations with the highest ratios, contributing to the overall failure by $12 \%$ and $15 \%$, respectively. For the human error contributions, jammed cutter, cutting procedure, drill cutting debris and cutting time error all contributed similar amount ( $4 \%$ ). To a lesser degree, external cutting problem and misalignment of the CoB have increased risk levels of $2 \%$ and $1 \%$ respectively.

Re-running the analysis with barge capsize $\left(I E_{23}\right)$ set to failed state, a backward analysis is performed within the BN to assess the most probable cause (MPC) of barge capsize, as shown in Fig. 9. The MPCs are the primary events with the highest posterior to prior failure probability ratios. The intermediate events associated with the capsize/descent of the jacket structure and/or lifting barge are the stuck-pipe $\left(I E_{18}\right)$, center of gravity miscalculation $\left(I E_{21}\right)$ and center of buoyancy misalignment $\left(I E_{22}\right)$. The MPCs are the flooded members, residual anode weight, the uneven flooding and the improper cutting procedure of the jacket legs. The posterior probabilities of these primary events leading to capsize are found to be significantly larger than their prior failure probabilities by varying multiple factors (Table 3, column 6).

Figure 9. Diagnostic analysis of capsize/descent scenario.

The diagnosis of the capsize likelihood further showed that approximately $84 \%$ of the failure is due to the corrosion thinning effect on the walls of the jacket legs, caused by the effects

of internal (52\%) and external thinning (16\%). This makes internal thinning a critical event in the safe estimation of the appropriate center of gravity.

The higher the probability ratios, the more critical the components or events is to cause the lifting barge to capsize or descent. Therefore, it is required that these safety-critical events are prioritised and properly managed to prevent the occurrence of capsizing.

# 5. Conclusion 

This study introduces an integrated safety analysis technique to assess the most probable causes of a futile decommissioning operation. The risk model developed is based on combining the capabilities of hierarchical Bayesian analysis with Bayesian networks to conduct probabilistic risk analysis. This work addresses the major challenge of failure data sparsity in the offshore decommissioning industry. The operation is presently driven by experience, and data used in the risk assessment has been based on expert judgements and source-to-source data collection from analogous activities. The hazards associated with steel piled jackets removal from severance to lifting were analysed through hazard identification technique, data were collected and aggregated through HBA to provide predictive posterior distributions of the probabilities. The following conclusions were made from the results obtained:

Hazard identification. HAZID is conducted to assess the operational challenges of the jacket removal sequence and to identify where safety issues arise. The sequence of operation is analysed with 11 industry experts from mid- to senior engineers and academic professionals having considerable decommissioning operational knowledge. The process involves subdividing the removal and lifting operation. While the number of experts' opinions collected for this study is limited to 11, practical application would require large samples of opinions to capture enough hazards and data. For instance, this paper identifies collision, loss of stability and descent as the safety issues associated with lifting operation. In practice, the decommissioning hazards can be more depending on location and weather conditions.

Hierarchical Bayesian analysis. The HBA model used its non-informative priors and likelihood function to provide a reasonable estimate of failure probability over a distribution. HBA adopts statistical functions such as normal (Gaussian), Beta and Gamma distributions. The Gamma distribution was especially useful in this study due to its conjugate pair properties. In addition, the

HBA can account for both component and systems-level variations and obtain better estimate from sparse failure data.

Bayesian networks. The BNs is suitable for estimating probabilities under uncertainty. Based on the occurrence probability obtained from HBA, the BN results showed that overall occurrence probability of a futile decommissioning operation of 0.6333 is caused by $27.2 \%$ occurrence probability of capsize/descent of the lifting barge and $19.2 \%$ occurrence probability of the collision/drift. In addition, the BN used the Bayes' theorem to update the failure probability of causations through predictive analysis using the predictive posteriors obtained from the HBA model. A diagnostic analysis of the top event showed that In Table 3, it can be observed that flooded members and uneven flooding are the causations with the highest ratios, contributing to the overall failure by $12 \%$ and $15 \%$, respectively. For the human error contributions, jammed cutter, cutting procedure, drill cutting debris and cutting time error all contributed similar amount (4\%). To a lesser degree, external cutting problem and misalignment of the CoB have increased risk levels of $2 \%$ and $1 \%$ respectively.

Detailed diagnosis. Based on the detail diagnosis analysis conducted on barge capsize, the most probable causes of failure were found to be flooded members, residual anode weight, the uneven flooding and the improper cutting procedure of the jacket legs. The results showed that $84 \%$ of the failure is due to the corrosion thinning effect on the walls of the jacket legs, caused by the effects of internal ( $52 \%$ ) and external thinning ( $16 \%$ ). Therefore, it is recommended that internal thinning likelihoods be thoroughly assessed prior to the jacket removal operation.

Going forward. This study identifies the need for further research in investigating the uncertainties associated with the data source and the assumptions built into the HBA model; conducting sensitivity analysis to investigate the contribution of each causations to the overall failure and finally; incorporating the HBA with time-dependencies to account for the changes that can significantly increase the hazards over time.

# Acknowledgements 

The authors thankfully acknowledge all the experts for their valuable inputs on the accident analysis description; the financial support provided by the John Blackburn Main IMarEST Fellowship; Engineering the future body; and the Department of Naval, Ocean and Marine Engineering, of the University of Strathclyde.

Declaration of Interest: We declare that there is no conflict of interest of any kind related to this work.

# ORCID 

Ahmed Babaleye https://orcid.org/0000-0002-4104-956X
Rafet Emek Kurt https://orcid.org/0000-0002-5923-0703

# Figures 

![img-0.jpeg](img-0.jpeg)

Figure 1
![img-1.jpeg](img-1.jpeg)

Figure 2

![img-2.jpeg](img-2.jpeg)

Figure 3
![img-3.jpeg](img-3.jpeg)

Figure 4

Objective function $f(x), x=\left(x_{1}, \ldots, x_{k}\right)^{T}$
Initialise a population of causations $x_{i}(i=1,2, \ldots, n)$
for $i=1: n$ all $n$ source-to-source data points
for $j=1: k$ all $k$ primary events
List the number of removal operations $N_{i}$ recorded
$\mu=\operatorname{mean}\left(x_{i} \cdot N_{i} / \operatorname{sum}\left(N_{i}\right)\right) \quad \%$ Estimate the mean parametrically
$\sigma=\operatorname{std}\left(x_{i} \cdot N_{i} / \operatorname{sum}\left(N_{i}\right)^{2}\right) \quad \%$ Estimate the standard parametrically
$(\alpha, \beta)=\operatorname{gampdf}(\mu, \sigma) \quad \%$ Estimate the shape \& scale parameters
end
Obtain the mean probability from the distribution
end
Post-process results and visualisation
Figure 5

![img-4.jpeg](img-4.jpeg)

Figure 6

![img-5.jpeg](img-5.jpeg)

Figure 7

- Node properties: IE22


Figure 8

![img-6.jpeg](img-6.jpeg)

Figure 9

# List of Figure captions 

Figure 1. Decommissioning incidents from 2005-2015 (Oil \& Gas UK. 2015)
Figure 2. Main process of steel jacket decommissioning operation.
Figure 3. Fault tree representation of accident model.
Figure 4. A typical representation of Bayesian network.
Figure 5. MATLAB algorithm for estimating occurrence probabilities.
Figure 6. Estimated occurrence probabilities for individual causation.
Figure 7. BN model for futile decommissioning operation.
Figure 8. Conditional probability table for node 22.
Figure 9. Diagnostic analysis of capsize/descent scenario.