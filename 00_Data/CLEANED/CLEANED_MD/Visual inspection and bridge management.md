# Visual Inspection and Bridge Management 

Lucy Quirk BE (Hons)

Thesis submitted for the Degree of Research Masters
![img-0.jpeg](img-0.jpeg)

National University of Ireland, Cork School of Engineering
$29^{\text {th }}$ October 2020

Head of School: Prof Liam Marnane

Supervisors: Dr Vikram Pakrashi

Dr Jimmy Murphy

# Table of Contents 

List of Figures ..... iv
List of Tables ..... v
Declaration ..... vi
Abstract. ..... vii
List of Abbreviations ..... viii
1 Introduction ..... 1
1.1 Background ..... 1
1.2 Aim of Study ..... 5
1.3 Dissertation Overview ..... 7
1.4 Research Output ..... 7
2 Literature Review ..... 8
3 Value of Information (VoI) Analysis ..... 13
3.1 Value of Information (VoI) Theory ..... 15
3.1.1 Prior Analysis ..... 15
3.1.2 The Value of Perfect Information ..... 16
3.1.3 The Value of Imperfect Information ..... 17
3.2 Modelling the VoI: Bayesian Networks and Influence Diagrams ..... 20
3.2.1 Bayesian Network ..... 20
3.2.2 Influence Diagrams ..... 24
3.3 Conclusions ..... 27
4 Value of Visual Inspection Information to an Individual Decision Maker Managing a Single Bridge ..... 26

4.1 Vol Calculation ..... 27
4.1.1 Prior Analysis ..... 29
4.1.2 Calculating the Value of Perfect Information ..... 31
4.1.3 Calculating the Value of Imperfect Information ..... 31
4.2 Conclusions ..... 38
5 Value of Visual Inspection to Infrastructure Asset Managers Operating a BMS for a Bridge Network ..... 39
5.1 Variables Involved in the Model ..... 42
5.1.1 Bridge State ..... 42
5.1.2 Condition Rating ..... 42
5.1.3 Decision Alternatives ..... 44
5.1.4 Cost Matrix ..... 44
5.2 Results ..... 45
5.3 Factor Influencing the Value Provided by Visual Inspection ..... 46
5.3.1 Condition Rating Accuracy and Precision ..... 46
5.3.2 Prior Bridge State ..... 50
5.3.3 Uncertainty in the Condition Rating Scale ..... 53
6 Conclusions ..... 53
6.1 Limitations ..... 55
6.2 Opportunities for Further Work ..... 56
References ..... 58

# List of Figures 

Figure 3.1 A simple Bayesian network describing the overall bridge condition rating (CR), which is a parent to the major element condition ratings - deck CR and support CR. 21
Figure 3.2 A simple influence diagram outlining a BMS whereby the cost (utility node) of maintaining a bridge is dependent on the bridge state (chance node) and the maintenance action chosen (decision node) 25

Figure 3.3 POMPD Model, shaded nodes represent observed variables e.g.: condition ratings from visual inspection. 26

Figure 4.1 Influence Diagrams modelling the repair decision for a bridge i, in a bridge network: (a) no information; (b) perfect information; (c) imperfect information about the condition state of bridge i. 28

Figure 4.2 Expected cost of imperfect information conditional on the accuracy of visual inspection. 34

Figure 4.3 Expected value of imperfect information (VoII) conditional on the accuracy of visual inspection. 34

Figure 4.4 Expected cost conditional on the probability of failure, $\mathrm{P}_{\mathrm{F}}$. 35
Figure 4.5 Expected VoI conditional on the probability of failure, $\mathrm{P}_{\mathrm{F}}$. 36
Figure 5.1 IDs modelling maintenance strategies for a bridge i, in a bridge network: (a) Timebased maintenance strategy which portrays the prior case; (b) Condition-based maintenance strategy which portrays the pre-posterior case. 41

Figure 5.2 Investigation of the VoI as a function of visual inspection accuracy 48
Figure 5.3 Investigation of the VoI as a function of visual inspection precision 50
Figure 5.4 Impact of the prior bridge state on the VoI. 51

Figure 5.5 Effect of the prior bridge state on the estimates of VoI for different bridge stocks 52

Figure 5.6 Effect of condition rating scale on VoI 53

# List of Tables 

Table 4.1 Cost matrix for maintenance action alternatives (represented in multiples of $€ 1000$ ) ..... 28
Table 4.2 Likelihood matrix ..... 29
Table 4.3 LIMID outputs for each case. ..... 33
Table 5.1 Condition rating descriptions (NRA, 2008) ..... 39
Table 5.2 Distribution of condition ratings. ..... 40
Table 5.3 Probability distributions for prior bridge state. ..... 50
Table 5.4 Distribution of condition ratings for different road types. ..... 51

# Declaration 

I, Lucy Quirk, certify that this thesis is my own work and has not been submitted for another degree at University College Cork or elsewhere.
![img-1.jpeg](img-1.jpeg)

Lucy Quirk

#### Abstract

This thesis estimates the impact of visual inspection prior to its implementation in a Bridge Management System (BMS) using Value of Information (VoI). Visual inspection is the principal assessment method for bridge structures, whereby a condition rating is assigned reflecting the structural condition of a bridge, based on the judgements of a trained inspector. The impact of data collected from visual inspection is contingent on its ability to guide towards optimal maintenance decisions throughout the lifecycle to maximise network performance. The VoI concept from Bayesian pre- posterior analysis is defined as the quantification of the reduction of uncertainty in a decision-making problem, after new information is received. This concept has seen multifaceted applications in the optimisation of Structural Health Monitoring techniques, typically focussing on the ability to monitor a specific parameter to determine the degradation rate and condition of a single asset. The merits of visual inspection data have been largely overlooked thus far. This work outlines and applies a framework to put a measure on the impact that visual inspection provides to infrastructure asset managers operating a BMS, and to illustrate how this is influenced by the underlying uncertainties of the model parameters.

# List of Abbreviations 


# 1 Introduction 

### 1.1 Background

Successful infrastructure management is fundamental to economic growth and international competitiveness (ASCE, 2013). Managing and maintaining these assets, ensuring both their reliability and consistency of service is an integral element in delivering a prosperous economy and ensuring safety for all users. Bridges age over time, often exceed their design life and have a much longer service life than typical national assets. Inadequate and poorly planned maintenance actions can lead to an accumulation of unnecessary costs over a bridges' lifecycle. It is essential for bridge management agencies to extend the useful life of a bridge, while maintaining a high standard of safety. Thus, devising a Bridge Management System (BMS) that provides value in balancing the cost of inspection and maintenance against the risk of failure is necessary to enable the user to plan for, and reduce the impact of such events. Comprehensive BMSs facilitate owners in inspecting, maintaining and rehabilitating deteriorating bridge stock within the limitations of financial resources (Mirzaei et al., 2014). A BMS refers to a set of decisions, in relation to design, construction, maintenance; and structural intervention, made by infrastructure management over time, to maximise performance (Sánchez-Silva et al., 2016). Uncertainties of either epistemic or aleatory nature complicate such decision problems and may lead to suboptimal actions or even actions with catastrophic consequences (Der Kiureghian and Ditlevsen, 2007). Information is fundamental to reduce uncertainties; information about the state of bridges and its components, and about the consequences of various decision alternatives (Konakli et al., 2015).

Information gathering practices (O'Brien et al., 2005) are central to the success of a BMS, and can be broadly categorised under three main levels - visual inspection; principal inspection; and special inspection. Visual inspection is typically the first step in a BMS, whereby each bridge is visually evaluated and assigned a pre-defined condition rating, providing a condition assessment of the selected stock of bridges (Chase et al., 2016). These condition ratings can be and are often used to predict the future condition state of elements (Zanini et al., 2016), to determine if maintenance or structural intervention is to be carried out, commonly using the Markovian deterioration model (Wellalage et al., 2014, Li et al., 1996). Otherwise, condition ratings are simply used to identify areas for future evaluation; either through structural assessment (Saydam et al., 2013) or further inspection via principal inspection (NRA, 2008), special inspection (Browne et al., 2010, Duffy, 2004) or emerging technologies (Vaghef et al., 2011, Washer and Fuchs, 2015, Zink and Lovelace, 2015). In this regard, a risk-based metric can be adopted. While principal inspections refer to visual assessments, special inspections (O'Connor et al., 2012) can involve significant mechanical and chemical testing of the structure as per the requirements. Additionally, the cost of special inspections can be significantly higher than principal inspections and variable based on the requirement of tests and the size of the bridge.

Effective and reliable condition assessment is an important part in evaluating and maintaining bridge structures. Visual inspection is the predominant method of inspection for bridges worldwide. It is likely that a hybrid inspection technique that adopts both visual inspection and other non-destructive testing could optimise efficiency of condition assessment and ultimately lead to better decision making

would lead to more appropriate and economical decision making regarding the possible rehabilitation or replacement of bridge members or the entire structure (Weninger-Vycudil et al., 2015). To get this process moving forward, the Value of Information (VoI) that both visual inspection and other non-destructive testing provides must be determined, so that the correct balance of their use can be deduced. The two methods are distinct but not mutually exclusive and each method has specific capabilities and challenges. Both methods provide different information of varying accuracy and have various associated costs. By evaluating the VoI that they contribute, the most appropriate method or combination of inspection methods can be determined. VoI provides a mathematical framework, to quantify the benefit of collecting additional information to reduce uncertainty in a decision-making problem. It enables a decision maker to choose what information they require, if any, and to rank alternative information gathering strategies based on a common utility metric (Raiffa, and Schlaifer, 1961). Research has been conducted on the value of other non-destructive testing methods such as Structural Health Monitoring technologies (Straub 2014, Straub, 2009, Pozzi and Der Kiureghian, 2011). However, the value of visual inspection information has yet to be investigated in a BMS context.

There is a lack of understanding of the estimated benefit of visual inspection information since explicit information regarding the mechanical properties of the material or structural components is unavailable. Empirical attempts have been made with limited success to use visual inspection results to update reliability analysis of bridges using conservative assumptions (Estes et al., 2004, Wang, 2010). Visual inspection data can be incomplete and is uncertain in comparison to testing and

monitoring involving emerging technologies. A specific defect or parameter is usually updated by monitoring at optimum time intervals and can be used to directly update the reliability of a structure (Luque and Straub, 2015). Assigning a quantitative value to the reduction of uncertainty via condition rating information is essential in bridge management to ensure that there is a correct basis for allocating resources (Weninger- Vycudil et al., 2015) to visual inspection strategies (Deshmukh and Sanford Bernhardt, 2000). Srinivasan and Kumar (2013) provided a methodology to compare the merits of different condition monitoring approaches, one being visual inspection, for underground tunnels. However, in bridge management, focus has centred on the accuracy of visual inspection data, rather than benefit estimates (Graybeal et al., 2002, Moore et al., 2001). Probabilistic models exist for condition rating (Attoh-Okine and Bowers, 2006, Gattulli and Chiaramonte, 2005, Pozzi et al., 2010, Rafiq et al., 2015) but the VoI concept is significantly unexplored.

# 1.2 Aim of Study 

The aim of this paper is to addresses the gap in the knowledge that exists, which is to provide an organised representation of the value of visual inspection, measured through the VoI within a BMS framework. The VoI concept, is a key concept in preposterior analysis, which represents the difference between expected benefits evaluated with and without a piece of information (Konakli et al., 2015). This concept has been used extensively in determining the value of monitoring and inspection in the field of infrastructure management, as it allows the decision maker to determine the expected value an inspection strategy will provide prior to its implementation (Pozzi and Der Kiureghian, 2011, Straub, 2014, Thöns et al., 2015). A significant number of operational bridges have been used in this paper to provide a useful representation. The impact of the variation in inspection accuracy and precision have been considered. The impact of the current bridge state and the variations that occur from using different BMS have also been considered. Collectively, the results assess visual inspection for an individual BMS and allow infrastructure managers of other BMSs to assess their bridge stock and take decisions on inspection based on their method, accuracy and precision - thereby ensuring the portability of the method and findings to a range of disparate situations.

A graphical framework is proposed to quantify the VoI of visual inspection by use of Bayesian networks and influence diagrams (Jensen and Nielsen, 2007, Koller and Friedman, 2009). Bayesian networks are efficient and intuitive graphical tools for the representation and assessment of systems under uncertainty. They provide a framework for updating and the assessment of component/system performance in light of uncertain information. Bayesian networks can be extended with utility and

decision nodes in the form of an influence diagram, thus providing a decision tool for ranking alternatives based on expected utility, allowing for an ideal platform for linking interdisciplinary modules to provide a comprehensive decision support framework (Bensi, 2010). A cohort of bridges is often comprised of deterministic and random factors that interact with each other; dependencies occur naturally and are important to account for (Biondini and Frangopol, 2016). Although a probabilistic model is a logical format, where the state of an infrastructure system is represented via a joint distribution, even in the simplest case, the explicit solution of this joint distribution is unmanageable due to computational demands and statistical data requirements (Koller and Friedman, 2009). Bayesian networks can represent high dimensional distributions by exploiting conditional independence, (Koller and Friedman, 2009) and can be quantified through physical variables linked to the degradation process in an intuitive way through expert judgement combined with field measurements. Firstly, the condition-based maintenance strategies must be modelled, taking into account the decision alternatives and associated utilities in the form of an influence diagram. This model must describe the condition- based deterioration and allow for updating based on a sample of visual inspection results (Memarzadeh and Pozzi, 2015), so that a revised expected life-cycle management cost (after inspection results are observed) can be deduced. Bayesian inference allows updating of the probabilities when observations, such as bridge condition ratings, become available (Bensi et al., 2013, Kosgodagan et al., 2015a). Dynamic Bayesian networks, Bayesian networks with a time-indexed sequence of nodes, can be used to analyse problems with time-varying domains, including inspection and monitoring (Bensi et al., 2013, Straub, 2009). The type of deterioration examined in this study, relating to concrete and masonry arch bridges, is more varied and is

commonly assessed through condition indicators, which have complex interdependencies. Attoh-Okine \& Bowers (2006) and Rafiq et al. (2015) have presented condition based deterioration models of such bridge structures, using both Bayesian network and dynamic Bayesian network models.

# 1.3 Dissertation Overview 

Chapter 2 presents a background on the VoI concept and its applications with focus on the bridge network management domain. The mathematical framework is presented in Chapter 3, which outlines the characteristics and challenges of using Bayesian networks and influence diagrams. This is followed by an application of the VoI of visual inspection for an individual decision maker managing a single bridge in Chapter 4. This is extended to the value that visual inspection provides to infrastructure asset managers operating a BMS using Irish and Portuguese datasets for a regional road area (Chapter 5). Numerical investigations demonstrate how the decision problem is influenced by the assumed probabilistic models. The thesis concludes with a summary of the main findings and a discussion in Chapter 6.

### 1.4 Research Output

The following publication represents the primary dissemination of the research contained in this thesis:

Quirk, L., Matos, J., Murphy, J., Pakrashi, V. (2017). Visual Inspection and Bridge Management. Journal of Structures and Infrastructure Engineering, 13:1-13.

# 2 Literature Review 

Decision theory provides a rational framework for solving an extensive range of decision problems in civil engineering. In bridge network management examples include choice of maintenance, rehabilitation and replacement actions; type of inspection to be carried out; timing of inspections; and the priority of such actions. All of these options have an associated cost and benefit. For example, costs associated with replacing a bridge structure include design, management, labour, materials, along with the indirect costs of route detours and traffic disruption. The benefit of the bridge replacement decision is a longer service life. Decision theory is essential to provide the decision maker with a rational framework for weighing the costs and benefits for a set of decision alternatives (Koller and Friedman, 2009). However, in bridge network management, the costs and benefits associated with decision alternatives are not deterministic. For example, a bridge pier can be replaced after it has been undermined by scour, however there is no guarantee that that this pier will not also be subject to scour damage at a future date. Decision making in the field of bridge network management is carried out under uncertainty. Several theories provide solutions to decision making under uncertainty, of which the common consensus is that the optimal decision is the one which provides the maximum expected utility. This is in line with the VoI theory, which will be utilised in this study. The VoI concept quantifies the benefit a decision maker obtains from acquiring more information before making a decision (Raiffa and Schlaifer, 1961).

VoI (Lindley, 1956, Raiffa and Schlaifer, 1961, DeGroot, 1984), typically calculated as the difference between the prior and pre-posterior analysis and

represented in terms of maximum expected utility (Von Neumann and Morgenstern, 1953), is a powerful tool for assessing the merits of an inspection technique prior to implementation, and for choosing the optimal inspection strategy among possible alternatives (Pozzi and Der Kiureghian, 2012). The VoI concept was derived from Bayesian statistical decision theory and was first introduced in the seminal work of Lindley (1956), later formalised by Raiffa and Schlaifer (1961), and DeGroot (1984). The concept proceeded to have vast applications in the scientific community in the field of artificial intelligence (Russell and Norvig, 2003), informatics (Krause and Guestrin, 2009), economics (Eeckhoudt and Godfroid, 2000), medical decisionmaking (Strong and Oakley, 2013), geoscience (Bhattacharjya et al., 2010) and environmental risk management (Yokota and Thompson, 2004).

In the late 1970s, the VoI was introduced in the field of civil and structural engineering (Benjamin and Cornell, 1970, Ang and Tang, 1975). Tang (1973) was one of the earliest to realise the potential of the VoI in optimising decision making practices in the field of engineering. He studied Bayesian updating of probabilistic models with inspection results, which provided the basis to optimise inspections via pre-posterior analysis in aircraft and offshore structures subject to fatigue deterioration (Madsen et al., 1989, Sørensen and Thoft-Christensen, 1986). This was one of the primary examples, whereby the VoI was used to optimise information gathering practices in industry. A similar method based on Markovian deterioration models was employed in the transportation infrastructure management (Madanat, 1993).

In the last 20 years, the explicit use of the VoI concept has increased in popularity in the optimization of bridge network management, generating optimal

strategies for inspection and prediction of deterioration rates. Recent research has focussed on the value of deterministic information, albeit imperfect or uncertain, and the ability of this information to directly update the prior belief of the degradation state or reliability of a structural component or system (Konakli et al., 2015). As a result, visual inspection, being uncertain in nature has been mostly overlooked thus far. In the field of civil engineering, especially in relation to bridge management, the VoI theory has had applications in terms of structural reliability methods, structural health monitoring and in the field of natural hazards.

Structural reliability methods can be used to effectively model the VoI (Straub, 2014) by measuring the evolution of structural performance as a support to maintenance interventions (Pozzi and Der Kiureghian, 2011, Goulet et al., 2015, Straub and Faber, 2005).

In the optimisation of structural health monitoring practices, VoI analysis has had widespread applications (Malings and Pozzi, 2015, Pozzi et al., 2010, Goulet and Smith, 2013, Thöns et al., 2015), such as the optimization of sensor placement (Krause, 2008), investigating the benefit of long term structural health monitoring (Pozzi and Der Kiureghian, 2011) and the comparison of alternative structural health monitoring methods (Pozzi and Der Kiureghian, 2012). The impact of structural health monitoring on decision making, in economic terms, has also been quantified (Zonta et al., 2014). In the field of geotechnical engineering, which is heavily dependent on monitoring, the quality of information gathered, has been investigated with the VoI concept (Zhang et al., 2009).

In the area of natural hazards, the VoI has had extensive applications. It has been utilised to prioritise post-earthquake bridge inspections (Bensi et al., 2015,

Bensi, 2010). De Leon et al. (2015) used the VoI to develop economic strategies to reduce the expected number of fatalities and losses for bridge sites exposed to hurricane risk. The VoI has also been used for quantifying the value of improved climate models in the design of offshore structures, especially those exposed to extreme wave loads (Garré and Friis-Hansen 2014).

The decisions regarding maintenance and management for an individual bridge or bridge network are guided by safety and commercial decisions. As safety aspects are mandatory, the commercial decisions provide variation while respecting the safety constraints (Pakrashi et al., 2011). Thus, a quantification of the VoI for different inspection, testing or intervention options is important. Bridge maintenance and management is a hierarchical process (O'Connor et al., 2012) and information is available at different qualities, amounts and precision at different levels (Pakrashi et al., 2012). Therefore, the VoI of bridge visual inspection is a relevant aspect to investigate and the interest around this topic is growing.

There is limited information on the estimated benefit of visual inspection information since definitive information regarding the mechanical properties of the material or structural components are unattainable. Empirical attempts have been made to use visual inspection results to update reliability analysis of bridges using conservative assumptions with limited success (Estes et al., 2004; Wang, 2010). Visual inspection data can be incomplete and is uncertain when compared to testing and monitoring involving emerging technologies. A specific defect or parameter is usually updated by monitoring at optimum time intervals and can be used to directly update the reliability of a structure (Luque \& Straub, 2015).

However, in bridge maintenance and management, the emphasis is on the accuracy of visual inspection data, rather than the benefit (Graybeal et al., 2002; Moore et al., 2001). Probabilistic models exist for condition rating (Attoh-Okine \& Bowers, 2006; Gattulli \& Chiaramonte, 2005; Pozzi et al., 2010; Rafiq et al., 2015) but the VoI concept is significantly unexplored.

Existing research has focused on determining the value of monitoring or inspecting a particular parameter to determine the degradation rate and condition of a bridge. For example, the viability of monitoring stress and vibration using sensors (Oukhellou et al., 2008, Malings and Pozzi, 2015, Papadimitriou, 2000). Additionally, the majority of research determines the VoI at the component level, rather than at bridge level or bridge network level (Straub, 2004). Condition rating data and the data that visual inspection provides at a network level, has been largely overlooked thus far.

# 3 Value of Information (VoI) Analysis 

This chapter presents an outline of VoI analysis. A key concept in pre-posterior analysis is the VoI, which provides a mathematical framework, to quantify the benefit of collecting additional information to reduce uncertainty in a decision making problem (Raiffa and Schlaifer, 1961). The VoI concept enables a rational decision maker to choose what information to acquire, if any, and to rank alternative information gathering strategies based on a common utility metric (Von Neumann and Morgenstern, 1953). The optimal information gathering strategy i.e. inspection strategy or monitoring system, is the one that maximises the VoI minus the cost of the strategy. To illustrate this concept, consider a classical decision problem under uncertainty where (i) the action alternative chosen will depend on the state of an uncertain variable, (ii) the true state is unknown, but (iii) it is possible at a cost to obtain information about the state of the uncertain variable through an information gathering strategy (Raiffa and Schlaifer, 1961), where

- $a \in A$ is an action chosen from space $A$
- $x \in X$ is an uncertain variable in space $X$
- $y \in Y$ an observed sample composed of n observations $\left\{y_{1}, \ldots, y_{n}\right\}$
- $u(a, x)$ is the utility function of $a$ and $x$

According to the principles of decision theory, the optimal action is the one that maximises the expected utility (Von Neumann and Morgenstern, 1953). $E_{x}$ denotes the expectation with respect to $X$. Argmax is an operation that finds the argument that

gives the maximum value. The action $a$ which a rational agent should choose is that which maximises the agent's expected utility. and is given by
$a_{o p t}=\underset{a \in A}{\arg \max } E_{X}[u(a, X)]$
The corresponding expected utility is given by
$U=E_{X}\left[u\left(a_{o p t}, X\right)\right]$

Information can be gathered prior to making a decision in the form of an information gathering (inspection) strategy, $s$. The revised decision problem is to find the combination of information gathering strategies s and action alternatives $a$, that maximise utility. To provide an overview, consider the following three cases of engineering decision analysis:

1. Prior analysis: the optimal decision is chosen based on existing knowledge of the system prior to the acquisition of any additional information; represented as a prior probability distribution $p(x)$.
2. Posterior analysis: the optimal decision is determined by updating probabilities based on information received from an inspection strategy i.e. information is known before making a decision. The posterior distribution is defined as the probability of an unknown parameter conditional on the information obtained, given as $\mathrm{p}(\mathrm{x} \mid \mathrm{y})=\mathrm{p}(\mathrm{y} \mid \mathrm{x}) \mathrm{p}(\mathrm{x})$. This directly contrasts with the likelihood function, which is the probability of the information $y$ given the parameter $x, p(y \mid x)$. The two functions are related via Bayes rule, given as

$$
p(x \mid y)=\frac{p(y \mid x) p(x)}{p(y)}
$$

Where $p(y)=\int p(y \mid x) p(x) d x$
3. Pre-posterior analysis: the optimal decision is determined by updating probabilities based on expected information prior to implementation of an inspection strategy. In pre-posterior analysis, the potential of additional information to improve decision making is assessed before the inspection strategy is carried out. This is fundamentally different to posterior analysis, where the benefit of additional information to improve decision making is assessed after the information has been received. The pre-posterior distribution is defined as the distribution for future expected information based on the information that has already been seen. It does not depend on the unknown parameter as in the posterior case, as the unknown parameter has been integrated out. The pre-posterior distribution is given as $p(y)$, the denominator in Eq. (3.3).

# 3.1 Value of Information (VoI) Theory 

### 3.1.1 Prior Analysis

In the prior analysis, the optimal decision is determined based on existing knowledge of the system i.e. with no information from inspection (Raiffa and Schlaifer, 1961), given by

$$
a_{o p t}=\underset{a \in A}{\arg \max } E_{X}[u(a, X)]=\underset{a \in A}{\arg \max } \int_{X} u(a, x) f_{X}(x) d x
$$

Where $f_{X}(x)$ is the prior probability density function (PDF) of $X$ and $u(a, x)$ is the utility associated with a given set of actions $a$ and realizations $x . E_{X}$ denotes the expectation with respect to $X$. Argmax is an operation that finds the argument that gives the maximum value. The corresponding prior expected utility is given by
$U_{\text {prior }}=E_{X}\left[u\left(a_{\text {opt }}, X\right)\right]=\int_{X} u\left(a_{\text {opt }}, x\right) f_{X}(x) d x$

# 3.1.2 The Value of Perfect Information 

Data is considered as perfect, if it is directly informative of the parameter of interest. A decision problem with perfect information is the unrealistic situation, in which there is no uncertainty on $X$. For a given $x$, the decision maker can always choose the optimal action, denoted as
$a_{\text {opt }}^{*}(x)=\underset{a \in A}{\arg \max } u(a, X)$

### 3.1.2.1 Conditional Value of Perfect Information

The conditional value of perfect information (CVPI) is the value of an information gathering strategy, after the information has been received. This is a form of posterior analysis, as the CVPI can be evaluated only conditionally, or after the fact (Raiffa \& Schlaifer, 1961). The CVPI is a measure of the value contained in $x$ computed as the difference between the posterior and prior expected utilities given as

$$
\operatorname{CVPI}(x)=u\left(a_{\text {opt }}^{*}(x), x\right)-u\left(a_{\text {opt }}, x\right)
$$

The CVPI is always greater than or equal to zero.

### 3.1.2.2 Expected Value of Perfect Information

A-priori, the true value of $X$ is not known. However, it is possible to calculate the expected value of perfect information (EVPI) before the fact. The EVPI is the expected increase in utility that the decision maker obtains from gaining access to a sample of perfect observations, before making a decision. This is a form of preposterior analysis, defined as the expected value of the CVPI (Raiffa and Schlaifer, 1961).

$$
\begin{aligned}
& E V P I=E_{X}[C V P I(X)]=\int_{X}\left[u\left(a_{o p t}^{*}(x), x\right)-u\left(a_{o p t}, x\right)\right] f_{X}(x) d x \\
& E V P I=\int_{X} \max _{a \in A} u(a, x) f_{X}(x) d x-U_{\text {prior }}
\end{aligned}
$$

The EVPI is the difference in expected utility with perfect information a-priori and the expected utility in the prior case. This measure represents the upper bound of the value that any information gathering strategy can have. Thus, if the cost of an inspection strategy is greater than is EVPI, the strategy is deemed inefficient.

# 3.1.3 The Value of Imperfect Information 

If data is measured with noise, it is considered imperfect. Information gathering strategies, such as visual inspection, provide imperfect information on the true state $X$. In the posterior analysis, imperfect information is received and stored in the vector $y$ (Raiffa and Schlaifer, 1961). The probabilistic description of $X$ is updated based on this information. The optimal action is given by

$$
a_{o p t \mid y}=\underset{a \in A}{\arg \max } E_{x \mid y}[u(a, X)]=\underset{a \in A}{\arg \max } \int_{X} u(a, x) f_{X \mid y}(x \mid y) d x
$$

Where $f_{x \mid y}(x \mid y)$ is the joint PDF of $X$ conditioned on $y$ (posterior PDF) obtained from Bayes' rule. The corresponding posterior expected utility is a function of $y$, given as

$$
U_{\text {posterior }}(y)=E_{X}\left\{u\left[a_{\text {opti } y}, X\right]\right\}
$$

# 3.1.3.1 Conditional Value of Imperfect Information 

The difference between the posterior and prior expected utility is a measure of the VoI contained in $y$, termed the conditional value of imperfect information (CVII) and denoted by

$$
\operatorname{CVII}(y)=U_{\text {posterior }}(y)-U_{\text {prior }}
$$

The $\operatorname{CVII}(y)$ is zero if the posterior optimal decision $a_{\text {opty }}$ is the same as the prior optimal decision $a_{\text {opt }}$ and positive otherwise. In the context of a BMS, the $\operatorname{CVII}(y)$ has limited benefits. Once an observation $y$ is made i.e. through an inspection strategy, it is futile to compare $U_{\text {posterior }}(y)$ to the results of the original prior utility $U_{\text {prior }}$, which only answers questions after the fact, such as 'What was the least expensive maintenance strategy employed last year?' The interest of this paper is in the VoI contained in $y$, before the imperfect information is received i.e. before a costly inspection strategy is implemented. This is known as the expected value of imperfect information (EVII).

### 3.1.3.2 Expected Value of Imperfect Information

The expected value of imperfect information (EVII) is the expected value of the CVII with respect to all possible measurements outcomes. The information is

modelled via a random vector $Y$, where the pre-posterior distribution $f_{y}(y)$ defines all measurement outcomes.

$$
E V I I=E_{Y}[C V I(Y)]=E_{Y}\left[U_{\text {posterior }}(y)\right]-U_{\text {prior }}
$$

Substituting in values for $U_{\text {prior }}$ and $U_{\text {posterior }}(y)$ gives

$$
\begin{aligned}
& E V I I=E_{Y}\left\{\max _{a \in A} E_{X \mid Y}[u(a, X)]\right\}-\max _{a \in A} E_{X}[u(a, X)] \\
& E V I I=\int_{Y}\left[\max _{a \in A} \int_{X} u(a, x) f_{X \mid y}(x \mid y) d x\right] f_{Y}(y) d y-U_{\text {prior }}
\end{aligned}
$$

As mentioned previously, the EVPI will provide the upper bound for the EVII. The expected VoI is always greater than or equal to zero. Therefore, a rational decision maker will choose to undertake an information gathering strategy, with a cost $C_{s}$ if the following is fulfilled

$$
E V I I-C_{s} \geq 0
$$

The optimal inspection strategy $\{s \in S\}$ will be the one that has the minimum cost

$$
s_{o p t}=\underset{s \in S}{\arg \max }\left[E V I I(s)-C_{s}(s)\right]
$$

Pre-posterior analysis is inherently different from prior and posterior analysis; in the latter, the decision maker decides on different maintenance strategies, whereas in the former, the decision maker decides on the opportunity to acquire additional information in order to aid decisions on maintenance strategies. Pre-posterior analysis evaluates the potential of additional information to improve decision making before the inspection or monitoring is carried out; it puts a measure on information

gathering to see if it is worthwhile, or would it be less costly to rely on prior estimates.

# 3.2 Modelling the VoI: Bayesian Networks and Influence 

## Diagrams

Vol pre-posterior decision analysis problems can be graphically modelled through a Bayesian network - influence diagrams framework. A brief overview is given below for completeness.

### 3.2.1 Bayesian Network

A Bayesian network is a compact graphical representation of a probability distribution via conditional independence and can be used for near-real-time inference, under an evolving state of information (M. Bensi et al., 2015). Bayesian networks can be broken down into a qualitative and quantitative part:

### 3.2.1.1 Qualitative

A Bayesian network is as a probabilistic graphical model characterised by a directed acyclic graph, with chance nodes representing random variables, which can be discrete or continuous, and may or may not be observable, and directed arcs (from parent to child) representing causal or influential relationships between variables (Figure 3.1). Chance nodes have a finite set of mutually exclusive states. Each variable $A$ in the model, is associated with a conditional probability distribution that specifies a distribution over the values of $A$, given each possible joint assignment of values to its parents $B_{1}, \ldots, B_{n}$ such that $P\left(A \mid B_{1}, \ldots, B_{n}\right)$. For a node with no parents, termed a root node, the conditional probability distribution turns into an unconditional (marginal) distribution $P(A)$.

# 3.2.1.1.1 Conditional Independence 

Causality is not a structural requirement of Bayesian networks. However, the model must provide a realistic representation of the conditional independence properties of the variables in the network. A Bayesian network is completely determined once the graph and the entailed dependence structure, are specified for the qualitative part. The conditional independence statements between the nodes are captured through the directed arcs using the rules of d-separation (Pearl, 1988). Two distinct variables $A$ and $B$ in a causal network are d-separated, if for all paths between $A$ and $B$, there is an intermediate variable $V$ (distinct from $A$ and $B$ ) such that either, the connection is serial or diverging, and $V$ is instantiated; or the connection is converging, and neither $V$ nor any of $V$ 's descendants have received evidence (Jensen and Nielsen). For example, consider Figure 3.1, which represents a diverging connection, encoding the conditions that 'deck condition rating' and 'support condition rating' are independent given 'bridge condition rating', but are not independent marginally.
![img-2.jpeg](img-2.jpeg)

Figure 3.1 A simple Bayesian network describing the overall bridge condition rating (CR), which is a parent to the major element condition ratings - deck CR and support CR.

### 3.2.1.2 Quantitative

From a quantitative perspective, a Bayesian network can be described as an efficient representation of a joint probability distribution. In accordance with the chain rule of

probability, the multidimensional joint distribution of the Bayesian network is given as the product of all conditional probability distributions:

$$
P(U)=P\left(A_{1}, \ldots, A_{n}\right)=\prod_{i=1}^{n} p\left(A_{i} \mid P a\left(A_{i}\right)\right)
$$

Where $P a\left(A_{i}\right)$ represents the parents of node $A_{i}$ and $n$ is the number of random variables in the Bayesian network (Jensen \& Nielsen, 2007).

# 3.2.1.2.1 Prior Probability Distribution and Variable Elimination 

The prior probability distribution of any variable (i.e. probability of a variable without evidence) can be calculated by marginalising other variables out of the joint probability function in Equation (3.18) through the process of variable elimination (Jensen and Nielsen, 2007).

# 3.2.1.2.2 Inserting Evidence 

An attractive feature of Bayesian network is the ability to insert evidence e.g. visual inspection results regarding the condition state of a bridge. The prior distribution is updated in the presence of evidence via Bayes rule and a posterior marginal distribution is calculated. Given a set of observations/evidence, $e_{j}$, where $j=1, \ldots, m$ regarding variables in the Bayesian network, the joint probability distribution of Equation (3.18) becomes:

$$
P(U, e)=\prod_{i=1}^{m} p\left(A_{i} \mid P a\left(A_{i}\right)\right) \cdot \prod_{j=1}^{m} e_{j}
$$

And the updated probability for any variable $A$, given the evidence, $e$, is:

$$
P(A \mid e)=\frac{\sum_{U(A)} P(U, e)}{P(e)}
$$

This process is called inference and provides the ability to update predictions based on information from observations. However, this operation can soon become intractable in terms of computational demand.

### 3.2.1.3 Dynamic Bayesian Networks

A Dynamic Bayesian Network can be used to model domains that evolve over time (Koller and Friedman, 2009). A dynamic Bayesian network is a sequence of identical Bayesian networks connected by temporal links and indexed by a discretized time line. Each time slice contains a set of time-indexed random variables representing the state of the dynamic Bayesian network at a particular point in time. To be classified as a dynamic Bayesian network, the structure of the time slices must be identical and the temporal links must stay the same.

# 3.2.1.4 Discrete Bayesian Networks 

For a discrete Bayesian network, the nodes represent discrete random variables. Each variable is associated with a marginal distribution for root nodes and a conditional probability table for child nodes. The conditional probability tables can be constructed by using accessible data or exploiting structured expert judgement methods (Kosgodagan et al., 2015b). For discrete Bayesian networks, discrete Bayes' rule is invoked in order to perform and propagate inference, when evidence is inserted into the model.

### 3.2.1.5 Constructing Bayesian Networks

Bayesian networks are constructed taking into consideration the following:

- Defining the graphical model which represents the probabilistic dependence structure of the problem (see d-separation above).
- Construction of the conditional probability tables that define the joint distribution over all random variables in the Bayesian network.
- Care must be taken to ensure that the model constructed is not misleading, unverifiable, unnecessarily complex or computationally intractable.


### 3.2.2 Influence Diagrams

Influence diagrams extend Bayesian networks with decision nodes and utility nodes, symbolised by rectangles and diamonds, respectively, to model decision problems under uncertainty (Figure 3.2). An influence diagram is a directed acyclic graph over chance nodes, decision nodes and utility nodes, such that the utility nodes have no children. The objective of an influence diagram is to find an optimal strategy (set of decisions) based on the principal of maximum expected utility (Von Neumann and

Morgenstern, 1953) and the updated state of information. Decision variables correspond to alternative choices available to the decision maker. In principle, there are two types of decision alternatives: action alternatives, e.g., shut down a bridge; and test alternatives, e.g., inspect a bridge. Test alternatives facilitate the gathering of information prior to making a final decision. An arc coming from a chance node into a decision node indicates that the decision maker knows the state of that random variable at the time of making the decision, whereas an incoming arc from another decision node indicates that the decision is made with knowledge of the selected alternative of that preceding decision node (Bensi et al., 2015). Utility variables represent the decision maker's utility/loss as additive components of the joint utility function. Chance nodes and decision nodes have a finite set of states; utility nodes have no states. An influence diagram is determined if, for each chance node, $X$, there is an associated conditional probability distribution, $P(X \mid p a(X))$ and each utility node, $U$, is associated with a real valued function over $p a(U)$.
![img-3.jpeg](img-3.jpeg)

Figure 3.2 A simple influence diagram outlining a BMS whereby the cost (utility node) of maintaining a bridge is dependent on the bridge state (chance node) and the maintenance action chosen (decision node).

# 3.2.2.1 Partially Observed Markov Decision Process and Limited Memory 

Influence Diagrams

Partially observable Markov decision process (POMDP) have significant uses in infrastructure maintenance decision problems due to their ability to model complex decision problems in stochastic domains, in which the states of the system are observable only indirectly, through a set of imperfect observations. Partial observability and the ability to model and reason with information-gathering actions, are the main features that distinguish the POMDP from the fully-observable Markov decision process (Hauskrecht, 2000). The POMDP framework represents the two cases of uncertainty in the problem: stochasticity of the underlying controlled process (e.g. deterioration of bridge structures in a network) and imperfect observability of condition states via a set of observations (e.g. condition ratings from visual inspection) (Hauskrecht, 2000).
![img-4.jpeg](img-4.jpeg)

Figure 3.3 POMPD Model, shaded nodes represent observed variables e.g.: condition ratings from visual inspection.

The complexity of POMDP algorithms, grows quickly over time. This is due to the 'no forgetting' assumption of the classical influence diagram framework. The Limited Memory Influence Diagram (LIMID) introduced by Lauritzen and Nilsson (2001), explicitly pinpoints which variables are remembered when taking a particular decision, thereby dropping the 'no-forgetting' assumption. Only nodes that are

explicitly represented as parents to a decision node are known when a decision is made. The advantage of LIMIDs is that they allow you to work with decision policies with smaller domains (Lauritzen \& Nilsson, 2001). A LIMID is solved via Single Policy Updating which, computes the probability distribution and expected utility function over the states of each chance and decision node in the LIMID The algorithm finds the globally optimal policies and its associated maximum expected utility. Vol analysis will be applied outside of the LIMID structure to determine the difference in value between the prior LIMID and the pre-posterior LIMID.

# 3.3 Conclusions 

In this study, the VoI that visual inspection provides in a BMS is investigated. For this specific decision problem, maintenance actions are chosen based on the bridge condition state. Associated with these maintenance actions are costs. The following characteristics make influence diagrams well-suited for the proposed application:

- They are efficient graphical tools for the representation and assessment of systems under uncertainty, such as a BMS.
- They provide an efficient framework for probabilistic updating and the assessment of bridge/network performance in view of uncertain and evolving information i.e. bridge visual inspection results (condition rating data).
- They are extended to include utility and decision nodes, thus providing a decision tool for ranking decision alternatives based on expected utility, such as maintenance actions.

- The graphical interface of influence diagrams, provides an ideal platform for interaction with and use by end users.
- Influence diagrams are a more compact representation of a decision problem in comparison to decision trees.

The limitations of using influence diagrams to solve decision problems is that the 'no forgetting' assumption, which states that values of observed variables and decisions that have been taken are remembered at all later times, can sometimes result in an intractable sum. The LIMID algorithm, as outlined above, relaxes the 'no forgetting' assumption and will be used in this study (Lauritzen \& Nilsson, 2001).

# 4 Value of Visual Inspection Information to an 

## Individual Decision Maker Managing a Single Bridge

To illustrate the methodology described in Section 3, an application is presented in this chapter, in which the VoI is computed both through the classical mathematical framework and graphically using influence diagrams solved via the LIMID algorithm. It considers a simple influence diagram as described in Figure 4.1. This example looks at decision making at bridge level, whereby the bridge can be in one of three condition states: good, degraded or poor. There are three maintenance actions which can be taken: do nothing, repair or major rehabilitation. The decision to carry out major rehabilitation, which would entail shutting down the bridge or reducing its capacity for a period of time, is made under competing objectives: on the one hand the bridge owner does not want to lose revenue by unnecessarily carrying out major works or unnecessarily shutting done the bridge, conversely the owner does not want to incur a liability by making an unsafe decision, keeping a bridge in operation that may have sustained serious damage and could be at risk of failure. To reduce the uncertainty surrounding bridge level decision making, a bridge inspection strategy is implemented for a bridge cohort. Bridge inspectors carry out visual inspections as set out in the elected BMS, incurring a certain cost that will yield information about the condition state of the bridge. The decision to carry out major rehabilitation or not is then made after gaining information from the visual inspection. To design the influence diagram for the bridge level decision making, two scenarios were considered: (a) carry out the maintenance action decision knowing the state of the bridge with certainty i.e. with perfect information and (b)

make the maintenance action decision with imperfect information gained from a visual inspection of the bridge. The costs associated with visual inspection are neglected for the purpose of this illustration.

# 4.1 VoI Calculation 

For calculation of the VoI, consider the influence diagram in Figure 4.1, considering the decision of whether or not to repair bridge $i$ in a bridge network. The chance node, Bridge_state ${ }_{i}$ indicates the true condition state of the $\left(i^{\text {th }}\right)$ bridge which can take on three possible values: good (G), degraded (D) or poor (P). The 'poor' state is assumed to lead to certain failure. The decision node, Action $_{i}$ consists of three maintenance action alternatives: do nothing (DN), repair (R) and major rehabilitation (MR). The utility node, Cost $_{i}$ is a child of Bridge_state ${ }_{i}$ and Action $_{i}$. For simplicity, the utility node Cost $_{i}$ measures the total cost in monetary terms. It assigns a cost value to every combination of the states of its parent nodes. A bridge condition rating is assigned based on the finding of a trained bridge inspector through a visual inspection but human factors remain in variations of such a rating. This imperfect observation is represented by the chance node $C R_{i}$, which can take three possible values: CR1, CR2 or CR3, corresponding to 'good', 'degraded' or 'poor' state, respectively. The 'degraded' state is assigned to have a $15 \%$ probability of failure, the 'poor' state is assumed to lead to certain failure. The notable cost values are as follows: cost of repair $\mathrm{CR}=\epsilon 25,000$, cost of major rehabilitation $\mathrm{CMR}=\epsilon 50,000$, and cost of bridge failure $\mathrm{CF}=\epsilon 250,000$. The values are chosen after considering several representative commercial cases available to the authors. The variables: Bridge_state, Action, Cost and Condition Rating (CR) are represented in figure 4.1.

![img-5.jpeg](img-5.jpeg)

Figure 4.1 Influence Diagrams modelling the repair decision for a bridge $i$, in a bridge network: (a) no information; (b) perfect information; (c) imperfect information about the condition state of bridge $i$.

In the influence diagram in Fig. 4.1(a), representing the prior case, the decision is made with no information on the bridge state (there is no incoming arc into the decision node). The direction of the arcs indicate that the value of the utility node depends on the bridge state and the selected maintenance action. Hence, if the bridge is 'good' state and the decision is made to repair the bridge, there will be a loss due to the cost of unnecessary repair. Whereas, if the bridge is 'poor' state and the decision is to do nothing, there will be a loss associated with the liability of bridge failure. The cost of each action alternative is represented via a cost matrix as shown in Table 4.1.

Table 4.1 Cost matrix for maintenance action alternatives (represented in multiples of $€ 1000$ )


The influence diagram in Fig. 4.1(b), includes an arc from the bridge state node $X_{i}$ into the decision node $A_{i}$. In this case, the decision is made with perfect information regarding the bridge state. This is an unrealistic situation; condition state data is always affected to some degree by noise. The decision maker knows the exact state of the bridge before making a decision e.g. the decision maker will only 'do nothing' if the bridge is in the 'good' state. The influence diagram in Fig. 4.1(c) represents the case, where the decision is made on the basis of imperfect information. An imperfect observation of the bridge state is made through a visual inspection of the bridge, which is represented by a chance node $Y_{i}$. The conditional probability table of node $Y_{i}$ is commonly referred to as the test likelihood matrix, as the likelihood of the observation $Y_{i}$ is conditional on the bridge state $X_{i}$. The likelihood matrix is shown in Table 4.2. This observation does not directly affect the utility node.

Table 4.2 Likelihood matrix


# 4.1.1 Prior Analysis 

In the prior analysis, the optimal decision is determined based in existing knowledge of the bridge i.e., with no information from inspection. See Figure 4.1(a), which models the case that no information is available before a decision is made. The prior probability is set as the vector $[P(G) P(D) P(P)]=[0.5 \quad 0.35 \quad 0.15]$. The minimum expected cost in the prior case is given as

$C^{\text {prior }}=\min _{a \in \mathcal{X}}\left\{\sum_{x} c(x, a) p(x)\right\}$

Where $p(x)$ is the prior probability density function (PDF) of $X$ and $c(x, a)$ is the cost associated with a given set of actions $a$ and realizations $x$.

$$
C^{\text {prior }}=\min _{a \in \mathcal{X}}\left\{\left[0.5 \times(0)+0.35 \times(37.5)+0.15 \times(250)\right],\left[0.5 \times(25)+0.35 \times(25)+0.15 \times(250)\right]\right\}
$$

$$
C^{\text {prior }}=\min _{a \in \mathcal{X}}\{50.625,58.75,50\}
$$

$C^{\text {prior }}=50$

Which is an average cost value. The optimal action is to 'major rehabilitation' in the prior case, as it is the action with the minimum expected cost.

# 4.1.2 Calculating the Value of Perfect Information 

Figure 4.1(b) represents the case where perfect information is available regarding the condition state of the bridge. Having perfect information implies the optimal decision is made for any outcome of Bridge_state ${ }_{i}$.

$$
\begin{aligned}
& C_{\text {perfect }}(x)=\sum_{a} \min _{a \in A}\{c(a, x)\} p(x) \\
& C_{\text {perfect }}(x)=[0.5 \min \{0,25,50\}]+[0.35 \min \{37.5,25,50\}]+[0.15 \min \{250,250,50\}] \\
& C_{\text {perfect }}(x)=16.25
\end{aligned}
$$

The optimal strategies are as follows: i) 'do nothing' when the bridge is in the 'good' state; ii) 'repair' when the bridge is in the 'degraded' state and iii) 'major rehabilitation' when the bridge is in the 'poor' state. It follows that the value of obtaining perfect information, VOPI, is

$$
\text { VOPI }=C_{\text {prior }}-C_{\text {perfect }}(x)=33.75
$$

This represents a $€ 33,750$ expected cost saving with perfect information. The actual value in terms of monetary units is subject to assumptions related to the original values on savings and how utility is converted to such monetary units.

### 4.1.3 Calculating the Value of Imperfect Information

To calculate the value of imperfect information, consider the prior probabilities and utility values outlined above. Also, consider the test likelihood matrix as outlined in Table 4.2.

$$
C_{\text {imperfect }}(y)=\sum_{T} \min _{a \in A}\{E(c(a, x \mid y)\} p(y)
$$

$C_{\text {imperfect }}(y)=0.485 \min \{13.15,31.975,50\}+0.31 \min \{41.74,35.89,50\}+$ $0.205 \min \{152.75,156.718,50\}$
$C_{\text {imperfect }}(y)=27.754$

The optimal strategies are as considered for perfect information in this case and the value of obtaining imperfect information, VOII, is
$V O I I=C_{\text {prior }}-C_{\text {imperfect }}(y)=22.246$

This represents a $€ 22,246$ expected cost saving with imperfect information.

# Graphical Solution of the VoI 

The graphical computation of the VOPI and the VOII is solved via the LIMID algorithm using the Bayes Net Toolbox in MATLAB (Murphy, 2001). The VOII is the maximum expected utility of the prior case subtracted from the maximum expected utility of the pre-posterior case and the results are shown in Table 4.3. For no information, the optimal strategy is to 'do nothing'. In the case of perfect and imperfect information, the optimal strategy is to 'do nothing' when the bridge is in the 'good', 'repair' when the bridge is in the 'degraded' state and to carry out 'major rehabilitation' when the bridge is in the 'poor' state. If a visual inspection strategy is implemented that yields imperfect information regarding the bridge state, the decision maker should expect to receive a cost saving of approximately $€ 22,250$. The VOPI of $€ 33,750$ represents the upper bound in the decision problem. A rational agent will decide to undertake a visual inspection strategy s, only if the cost of the strategy is less than $€ 22,250$ i.e. $V O I I-C_{s} \geq 0$.

Table 4.3 LIMID outputs for each case.


The outcome of Eqns. 3.5, 3.9, and 3.15 depend on the specific values assigned to the prior probability of the bridge state; the likelihood of inspector assigned condition ratings; and the cost values of the action alternatives. Figures 4.2 and 4.3 outline two numerical examples to examine how the accuracy of condition rating data and the prior probability of the bridge state affect the value provided by visual inspection. In Figure 4.2, the accuracy of visual inspection is varied with the other parameters in the model remaining constant. This figure outlines the importance of the accuracy of information on the value that the information provides. As the accuracy increases, the expected cost of gathering condition rating data decreases. A visual inspection with $0 \%$ accuracy and $100 \%$ accuracy is identical to a visual inspection with no information and perfect information respectively. At an accuracy level of $12 \%$, the value of imperfect information equals the visual inspection cost (Figure 4.3).

![img-6.jpeg](img-6.jpeg)

Figure 4.2 Expected cost of imperfect information conditional on the accuracy of visual inspection.
![img-7.jpeg](img-7.jpeg)

Figure 4.3 Expected value of imperfect information (VoII) conditional on the accuracy of visual inspection.

In Figure 4.4, the prior probability of the 'poor' bridge state, which is the same as the prior probability of failure PF is varied from 0 to 1.0 , with the other two bridge states, 'good' and 'degraded', fixed respectively. Three different scenarios ( $70 \%$ accuracy, $80 \%$ accuracy, and $90 \%$ accuracy) of visual inspection are suggested.
![img-8.jpeg](img-8.jpeg)

Figure 4.4 Expected cost conditional on the probability of failure, $P_{F}$.

As the prior probability of failure increases, the cost of inspection also increases. The expected cost of inspection is equivalent to the cost of major rehabilitation CMR for $\mathrm{P}_{\mathrm{F}}=0.4,0.6$, and 0.7 for accuracies of $70 \%, 80 \%$ and $90 \%$, respectively. This observation is reinforced in Figure 4.5, where the expected VoI reduces to 0 for the above probabilities and inspection accuracy scenarios. In Figure 4.5, the expected Vol peaks at $\mathrm{P}_{\mathrm{F}}=0.2$, which is due to the fact that in the case of 'no information', the optimal maintenance action is: 'do nothing' when $\mathrm{P}_{\mathrm{F}}<0.1$, 'repair' when

$0.1 \geq P_{F}<0.2$, and 'major rehabilitation' when $P_{F} \geq 0.2$. The shift of the expected cost of 'no information' between $\mathrm{P}_{\mathrm{F}}=0.1$ and $\mathrm{P}_{\mathrm{F}}=0.2$ results in a higher expected Vol at $\mathrm{P}_{\mathrm{F}}=0.2$.
![img-9.jpeg](img-9.jpeg)

Figure 4.5 Expected Vol conditional on the probability of failure, $P_{F}$.

This example indicates that a rational assessment of the Vol of visual inspection requires a full decision model, including an accurate assessment of the prior probability of the bridge states, the likelihood of inspector assigned condition ratings and the economic setting surrounding the maintenance action alternatives. If any of these elements are excluded from the decision model, an objective estimate of the Vol cannot be determined. The principal method of bridge inspection is carried out using visual means and determining the value it provides has the potential of

widespread applications to infrastructure asset managers in optimising inspection practices within different BMS.

# 4.2 Conclusions 

In this chapter, a background has been presented on the use of VoI to determine the value of data gathering strategies in a BMS, whereby the data has been obtained through visual inspection. The value of no information, perfect information and imperfect information have been calculated and the merits of each calculation outlined. Graphical tools in the form of Bayesian networks and IDs have demonstrated how condition rating data can be modelled and the VoI calculated via a concise and methodical process. Two numerical investigations were carried out to determine the effect of (1) the accuracy of visual inspection and (2) the prior probability of the bridge state, on the VoI of visual inspection. It was shown that the accuracy increases, the expected cost of gathering condition rating data decreases. It was concluded that in this demonstrative example, the value of imperfect information equals the visual inspection cost at an accuracy level of $12 \%$. It was also demonstrated that as the prior probability of failure increases, the cost of inspection also increases. The expected cost of inspection is equivalent to the cost of major rehabilitation for $\mathrm{P}_{\mathrm{F}}=0.4,0.6$, and 0.7 for accuracies of $70 \%, 80 \%$ and $90 \%$, respectively. This chapter looked at the VoI that condition rating data provides to a bridge owner operating a single bridge, the value that visual inspection provides to local authorities when operating a BMS for a network of bridges will be presented in the following chapter.

# 5 Value of Visual Inspection to Infrastructure Asset Managers Operating a BMS for a Bridge Network 

This application considers the value that visual inspection provides to local authorities when operating a BMS for a network of bridges with a specific focus on regional and local roads in Ireland. The hierarchy of roads in the Republic of Ireland comprises Motorways, National roads, Regional roads, and Local roads. Nonnational regional and local roads in Ireland account for $94 \%$ of the country's roads and carry approximately $54 \%$ of all road traffic (DTTAS, 2016). These roads provide mobility within and between local areas driving local economic activity. They also provide vital links to Ireland's strategic national roads, ports, and airports, linking Ireland with the wider European economy and have an importance social value. The maintenance of these infrastructure systems is essential from an economic, social and political perspective with $€ 7.7$ million of state grants allocated to local authorities to carry out bridge rehabilitation works on regional and local roads in 2015 (O'Brien, 2015).

Table 5.1 Condition rating descriptions (NRA, 2008).


Data for 449 bridges on regional roads and 828 bridges on local roads in County Cork, Ireland was considered for this section of study. These bridges are managed by a local authority operating the Eirspan BMS (Duffy, 2004). Additionally, data for 85 bridges for a bridge stock around Dublin is also considered. For each bridge, a visual inspection was carried out by a trained bridge inspector and a general condition rating was assigned as per Table 5.1. The cost of maintenance and repair works undertaken on each bridge in relation to the condition rating assigned is also provided. The distribution of condition ratings for three separate regions from which the bridge stocks are selected, is shown in Table 5.2. It can be seen that $7 \%, 29 \%$ and $26 \%$ of bridges were assigned a condition rating of 3 and over for the South Dublin; Cork regional; and Cork local road area respectively, suggesting that the Cork region is in significant need of investment in terms of bridge rehabilitation works.

Table 5.2 Distribution of condition ratings.


In this decision problem, the bridge condition state can take on six possible values, fixed by the BMS employed. The prior analysis will be based on a time-based maintenance strategy, whereby there is no information from inspections on the bridge state. A condition based maintenance strategy represents the pre-posterior case. The objective of a condition-based maintenance strategy is to provide information, in this case through visual inspection, regarding the condition state of a bridge. This information is combined with an existing prior belief on the degradation level of the bridge, to deliver a better estimate of the 'true' bridge state. The decision

maker can then use this information to make informed decisions as set out in the BMS guidelines. The VoI provided by visual inspection is defined as the difference in the maximum expected utility of the condition- based maintenance strategy and the time-based maintenance strategy. It is a common perception that a conditionbased maintenance strategy provides a greater value that a time-based maintenance strategy, as a better estimate of the bridge state, should lead to improved maintenance decisions. However, the benefit that visual inspection information provides is heavily dependent on an accurate description of the model parameters. A measure on the merits that visual inspection offers to infrastructure asset managers operating a BMS is provided here. How this value is influenced by the accuracy and precision of inspector assigned condition ratings, the prior probability of the bridge state and uncertainties in the condition rating scale are also illustrated. The timebased and the condition-based maintenance strategy are specified as the prior case (Fig. 5.1(a)) and the pre-posterior case (Fig. 5.1(b)), respectively.
![img-10.jpeg](img-10.jpeg)

Figure 5.1 IDs modelling maintenance strategies for a bridge $i$, in a bridge network: (a) Time-based maintenance strategy which portrays the prior case; (b) Condition-based maintenance strategy which portrays the pre-posterior case.

# 5.1 Variables Involved in the Model 

The IDs are solved using the LIMID algorithm. The conditional probability distribution of each node is given as a conditional probability table. The Cork regional road area is chosen for the 'typical case' in the analysis.

### 5.1.1 Bridge State

The change in bridge state over time is represented by $X=\left\{x_{1}, x_{2}, \ldots, x_{n}\right\}$, where n is the number of possible condition states. The degradation over time is represented by the stochastic process $\left\{X_{t}, t=0,1,2, \ldots\right\}$, where Xt describes the state of the bridge at time $t$. It is assumed that a bridge deteriorates sequentially between the condition states, with 0 being the best state. The probability that the bridge is in state i at time $t$ is represented by the following probability distribution: $\pi_{t}(i)=\operatorname{Pr}\left(X_{t}=i\right)$. The bridge state vector is defined as $\pi_{t}=\left\{\pi_{t}(0), \pi_{t}(1), \ldots, \pi_{t}(N)\right\}_{t} \pi_{t}(i) \geq 0, \forall_{t}=0,1, \ldots, N$; $\sum_{i=0}^{N} \pi_{t}(i)=1$, where $\pi_{t}$ describes the probability distribution of the bridge state at time t (Srinivasan, 2013). At time $t=0$, the decision maker's belief $\pi_{0}$ characterises the prior knowledge regarding the condition of the bridge before the beginning of the decision-making period. In this analysis, the condition rating data from the Cork regional road dataset is used to define a prior probability vector for the bridge state, given as, $\pi=[0.0630 .1920 .4580 .2190 .0580 .011]$.

### 5.1.2 Condition Rating

A trained inspector conducts a visual inspection on a bridge and assigns a condition rating as per Table 5.1 based on his assessment of the structure. This process is represented as $\left\{C R_{t}, t=0,1,2, \ldots\right\}$ with a finite observation space $C R=\{1,2, \ldots, m\}$, where

m is the number of condition states. In order to relate the information received from visual inspection to the state of the asset, an information matrix describing the error associated with visual inspection must be defined. Visual inspection is highly subjective and can lead to variable results that depend on multiple factors (Moore et al., 2001). To accurately define an information matrix, a study could be completed, in which multiple bridge inspectors inspect bridges of each condition rating, whereby the condition rating has previously been deterministically defined through an indepth expert-level inspection. This data could then be used to accurately define probability distributions of assigning the correct condition rating given the 'true' bridge state (Moore et al., 2001). As this data is not available here and for most bridge stock under practical conditions, it is assumed that the probability of an inspector assigning a correct condition rating follows a normal distribution $N(\mu, \sigma)$ with mean $\mu$ and unit standard deviation $\sigma=1$ over the finite outcome space $C R=\{0,1,2,3,4,5\}$ (Graybeal et al., 2002). This normal distribution describes the error (area underneath the curve) in the ability of an inspector to assign the correct condition rating. On the basis of this, an $n \times m$ information matrix, $Y=\left[y_{i k}\right], k \in m$, $i \in n$, is assigned, where yik represents the conditional probability of receiving condition rating k , given that the current state is i , i.e., $y_{i k}=\operatorname{Pr}\left(C R_{t}=K \mid X_{t}=i\right)$ (Srinivasan, 2013). The information matrix is given as,
$\mathrm{Y}=$



It is based on limited and existing information on the topic. From the early days of treating uncertainties around human effects on decisions on infrastructure in a systematic manner (Stewart et al., 1992) to date (Malings and Pozzi, 2016), the importance of field data and the lack of it have been highlighted, At this stage, most databases available to the authors are not mature enough to develop benchmarked information matrices, although over time this situation is expected to be improved.

# 5.1.3 Decision Alternatives 

The decision space for the decision node Di is defined first. Let $\left\{D_{i}, t=0,1,2, \ldots\right\}$ be the decision process to control the evolution of the bridge state, where $d \in D_{i}$ indicates the maintenance decision made at time $t$. For the BMS in this study, $D=\left\{d_{0}, d_{1}, d_{2}, d_{3}, d_{4}, d_{5}\right\}$ where $\mathrm{d}_{0}=$ 'do nothing', $\mathrm{d}_{1}=$ 'minor remedial works', $\mathrm{d}_{2}=$ 'minor repair works', $\mathrm{d}_{3}=$ 'minor repairs and preventative measures', $\mathrm{d}_{4}=$ 'extensive repairs', and $\mathrm{d}_{5}=$ 'replacement/extensive rehabilitation'.

### 5.1.4 Cost Matrix

The utility node is represented in terms of cost, which is a function of the bridge state and the decision alternative chosen. The cost function $C(i, d)$ represents the cost incurred when the asset is in state i and the decision d is taken. Given prior $\pi_{t}$ the expected immediate cost incurred at time $t$ is $C(d)=\sum_{i=1}^{N} \pi_{t}(i) C(i, d)$.

The cost matrix is defined based on the following assumptions:

The cost of each decision alternative is defined as the mean repair cost conditional on the condition rating assigned, i.e. if a bridge is assigned a condition rating of CR2, the mean repair cost is $€ 11,690$.

The probability of bridge failure for each bridge state is given by the following vector $\mathrm{P}_{\mathrm{F}}=[00.10 .20 .50 .751$ ]. Thus, if a bridge is defined as being in the worst state x 5 , it is assumed to lead to sure failure. This probability assignment is for demonstrative purposes only.

The cost of bridge failure is taken as a reference value of $€ 250,000$

The cost of a visual inspection strategy is $€ 500 /$ bridge

The cost matrix for the analysis is given as,


Indirect costs can vary significantly (Pakrashi et al., 2011) and thus a consideration of such variation can make the comparison for inspection uninterpretable. Under such circumstances, for this example, the relative contributions of indirect costs are assumed to be of similar level.

# 5.2 Results 

The results for the typical case using the Cork regional road data are given in Table 5.3. As anticipated, a perfect inspection has the lowest expected cost of $€ 12,339$. An inspection strategy is only worth undertaking if it costs less than its VoI and in this

case, the estimated value is $€ 6,876$, which is related to the case of imperfect information.

Table 5.3 LIMID outputs


In the case of no information the strategy with the minimum expected cost is d3.
With perfect information regarding the condition state, the optimal strategy takes the form of an identity matrix (Table 5.3). Imperfect information via visual inspection deduces a change in the above identity matrix, with the following strategy $\mathrm{D}_{\text {Imperfect_information }}=\left[(\mathrm{x} 0, \mathrm{~d} 2),(\mathrm{x} 1, \mathrm{~d} 3),(\mathrm{x} 2, \mathrm{~d} 3),(\mathrm{x} 3, \mathrm{~d} 3),(\mathrm{x} 4, \mathrm{~d} 4),(\mathrm{x} 5, \mathrm{~d} 4)\right]$ giving the lowest expected cost. As a result, visual inspection may not be suitable for certain databases and conditions, which will be investigated in the next section. These ratings can be improved in real situations by sharing more databases, which has started gaining popularity. Such information can also be related to capacities and this allows clustering of bridges (Hanley and Pakrashi, 2015) or transition of ratings over time (Reale and O'Connor, 2012), both of which are signatures of the collective performance of a bridge stock.

# 5.3 Factor Influencing the Value Provided by Visual Inspection 

### 5.3.1 Condition Rating Accuracy and Precision

Accuracy is a measure of how close an assigned condition rating value is to the actual 'true' bridge state. One of the key challenges with visual inspection is that

bridge inspectors grade the degradation differently based on their perception of the level of degradation. For example, one inspector may have an optimistic perception and grade a bridge as CR3, while another may be more pessimistic and grade the same bridge as CR4. In order to understand the impact of accuracy, the parameter CR was varied, from a pessimistic view to an optimistic view by varying the mean of the normal distribution with constant unit standard deviation over the finite outcome space $\mathrm{CR}=\{0,1,2,3,4,5\}$. The mean is shifted from the true value, in both the positive and negative direction, characterising, to varying degrees, a pessimistic and optimistic inspector, respectively. The amount of the shift represents the accuracy of the measurement. For example, in the analysis, a pessimistic inspector would assign a condition rating to a bridge in state x 1 as $\mathrm{N}(1.9,1)$ in the worst case of pessimism, where N is a normal distribution with mean and standard deviation as the two arguments respectively. Figure 5.2 estimates VoI as a function of visual inspection accuracy. As the inspector becomes more pessimistic, the expected VoI decreases linearly. In the most optimistic case the expected VoI is $€ 8,375$, which decreases to $€ 6,876$ for a neutral inspector and further decreases to $€ 5,071$ in the most pessimistic case. For the most optimistic inspector the optimal strategy $\mathrm{D}_{\text {optimistic }}=[(\mathrm{x} 0, \mathrm{~d} 2),(\mathrm{x} 1$, d2), (x2, d3), (x3, d3), (x4, d3), (x5, d4)] is risk-seeking while the optimal strategy for a pessimistic inspector is more risk-adverse, corresponding to $\mathrm{D}_{\text {pesimistic }}=[(\mathrm{x} 0$, d3), (x1, d3), (x2, d3), (x3, d4), (x4, d5), (x5, d5)]. It was observed optimistic inspection results in a higher VoI than a pessimistic inspection and more optimistic inspections lead to relatively more risk-seeking optimal maintenance strategies. The prior perception of an inspector on the degradation of an asset significantly affects the value provided.

![img-11.jpeg](img-11.jpeg)

Figure 5.2 Investigation of the VoI as a function of visual inspection accuracy

Precision refers to the closeness of two or more measurements to each other. In relation to visual inspection, precision is a measure of the repeatability of inspection. Poor precision results from random errors which results in poor repeatability. Precision is independent of accuracy and can be described by varying the standard deviation of the distribution for each condition rating. The standard deviation defines the width of the distribution, describing how much variation can occur between successive measurements. Figure 5.2 describes the estimated VoI as a function of visual inspection precision $\sigma$. The trend is monotonic but not linear, indicating that the worse the precision the lower the VoI. A high value of $€ 17,633$ is associated to the value of perfect information, whereby maintenance decisions are made with perfect information on the condition state of the asset, and diminishes towards zero as the precision of visual inspection degrades to $\sigma=9.5$. The break-even precision value occurs at $\sigma=4.7$ (Figure 5.3). Only a visual inspection strategy presenting a VoI higher than the cost of visual inspection (€500) is rationally suitable for implementation.

However, given the significantly high values related to lack of precision at which the VoI becomes less than the cost indicates that in this case an inspection is almost always beneficial. This may not be necessarily at the same level for other bridge stocks and the VoI may be lower than the visual inspection cost for particularly challenging set of bridges with access and equipment aspects, where the design of inspection programme will be of importance. For practical applications, very high standard deviation will not be expected from inspections and consequently the comparison will be relevant within the sharply decreasing part of the bar-chart of Figure 5.3. As precision decreases, the value delivered by visual inspection decreases monotonically, but nonlinearly. A visual inspection strategy presenting a VoI higher than the cost of visual inspection is rationally suitable for implementation in a Bridge Management System.

![img-12.jpeg](img-12.jpeg)

Figure 5.3 Investigation of the VoI as a function of visual inspection precision

# 5.3.2 Prior Bridge State 

Depending on the prior condition state of a bridge stock, visual inspection may give rise to different results for VoI. To examine the effect that the prior bridge state has on the VoI of visual inspection, the analysis was run whereby the prior state took on each possible distribution in Table 5.4. The likelihood of assigned condition ratings and the cost matrix were kept constant.

Table 5.3 Probability distributions for prior bridge state.


![img-13.jpeg](img-13.jpeg)

Figure 5.4 Impact of the prior bridge state on the VoI.

It is observed from Figure 5.4, that visual inspection provides the greatest VoI for CR3. The VoI is lowest for CR5 as the cost of perfect information

Cperfect_information_CR5 $=\epsilon 41,208$ converges to the cost of major rehabilitation $\mathrm{C}_{\text {Major_rehabilitation }}=\epsilon 50,760$. Bridge stocks, in reality, exhibit different prior state probability distributions depending on the type of road, bridge age, exposure conditions, state investment in bridge rehabilitation works etc. The analysis was repeated using prior probability distributions for four different road types as outlined in Table 5.5. For this purpose, a significantly larger stock with 32250 bridges in Portugal was considered with real distributions of bridge conditions.

Table 5.4 Distribution of condition ratings for different road types.


Figure 5.5 indicates the value that visual inspection provides is heavily dependent on the prior probability distribution of the bridge stock. Visual inspection provides the greatest benefit for bridge stocks with a high proportion of bridges with a CR2 rating such as the Cork regional and local roads. The VoI for the Dublin and Portuguese roads, which both had a high proportion of bridges with a CR1 rating was significantly lower, but still economically viable for a visual inspection strategy at a cost of $€ 500$. It also indicates how the proposed method can be applied to different bridge stocks of disparate sizes and how they can be compared in terms of the estimated value of their visual information.
![img-14.jpeg](img-14.jpeg)

Figure 5.5 Effect of the prior bridge state on the estimates of VoI for different bridge stocks

# 5.3.3 Uncertainty in the Condition Rating Scale 

Due to the nature of bridges in Ireland, a trend emerges in terms of the distribution of bridge condition states for local and regional roads. Ireland has an aging bridge stock and limited investment is available for bridge rehabilitation. As a result, the majority of bridges fall into the category of CR1, CR2 and CR3. It is investigated in Figure 5.6 if value is added to a visual inspection strategy where there is a finer resolution in the condition rating scale for various combinations of CR1, CR2, CR3 and CR4. For each application, the prior bridge state has equal probability of being in each state along the condition rating scale i.e. for the typical case $\pi \mathrm{t}=[0.1670 .167$ 0.1670 .1670 .167 0.167]. The cost matrix is altered based on the precision level achieved in visual inspection. The likelihood of inspector assigned condition ratings follows the same format as outlined in this study but the matrix is contracted or expanded based on the precision level of the condition rating scale.
![img-15.jpeg](img-15.jpeg)

Figure 5.6 Effect of condition rating scale on VoI

A negative impact on value was observed when CR1 was removed from the condition rating scale. A small drop in value was also observed when an additional rating was added between CR3 and CR4. The value improved from the typical case for all other cases with the greatest improvement in value observed when two additional ratings were added between CR1 and CR2. This coincides with Figure 5.6, whereby the greatest VoI was shown for bridge stocks with a high proportion of bridges in the CR2 category. In addition to assessing the actual effect on the condition rating scale on VoI, this study also provides demonstrative evidence to adapt the proposed method for practical assessment and integration of varied bridge stocks with different inspection ratings.

# 6 Conclusions 

In this study, the value of implementing a visual inspection strategy in a BMS was estimated employing the VoI methodology and several insights into visual inspection based decision making for bridge maintenance were investigated through analysis of various scenarios. Several real bridge stocks and related data were used in this regard. The estimated VoIs of no information, perfect information and imperfect information were calculated with County Cork in Republic of Ireland as a case study. The change in the optimal strategy based on perfect information and imperfect information from the prior state was also illustrated. The analysis is dependent on the characterisation of the parameters in the model, including the assumed probabilistic models of the prior bridge state, the likelihood of inspector assigned condition ratings and the economic setting surrounding the cost matrix for maintenance decision alternatives. The effect that the underlying uncertainties of the parameters have on the benefit provided by visual inspection was highlighted through numerical investigations. The following presents the main findings of the study.

It was found that an optimistic inspection results in a higher VoI than a pessimistic inspection and more optimistic inspections lead to relatively more risk-seeking optimal maintenance strategies. As an inspector becomes more pessimistic, the VoI reduces and the optimal maintenance strategy becomes more risk-adverse. The additional information must have enough accuracy to alter that belief, else the decision maker has the potential to make wrong choices or will be better off with a preventive maintenance strategy. The prior perception of an inspector on the degradation of an asset significantly affects the value provided and information from

multiple inspectors inspecting the same bridge could offer value in terms of reducing bias.

Analysing the precision of visual inspection regarding the value it provided, it was found that as precision decreases the value delivered by visual inspection decreases monotonically, but in a nonlinear fashion. A visual inspection strategy presenting a VoI higher than the cost of visual inspection is rationally suitable for implementation in a BMS.

Analyses on the prior state distribution indicate that the greatest value is provided for bridge stocks with specific priors, given the rating method is known. By analysing real bridge stocks, it was observed that the greatest benefit was provided for bridges in local and regional roads, which had a high proportion of bridges in the CR2 condition state. In contrast, a lower value was seen for the Dublin and Portuguese datasets, whose prior distribution had the majority of bridges in the CR1 state. Where a high proportion of bridges are in the CR3 or CR2 condition state, the benefit is observed to be greatest by adopting a visual inspection strategy. This was looked at further by investigating if value is added to visual inspection if the condition rating scale is presented in a different resolution. A negative impact on value was shown when the condition rating scale was narrowed by removing CR1. The highest increase in value was observed when two additional ratings were added in between CR1 and CR2, where the VoI increased significantly from the typical scenario. The applicability of VoI for visual inspections of bridges depend on the input parameters like the prior degradation model, the prior bridge state distribution, the likelihood of inspector assigned condition ratings and the economic setting surrounding the cost values of the maintenance action alternatives. Accurate

determination of these parameters obtained from several bridge stocks over an appropriately representative length of time can provide better estimates and stabilities around such values.

# 6.1 Limitations 

The use of the VoI methodology has been shown to have significant potential in the field of visual inspection and condition rating data. The limitations of determining the VoI of visual inspection lies in the ability to gain accurate information in relation to;

- Cost data
- The accuracy of inspection assigned condition ratings

In terms of cost data, the databases could potentially already exist in the field. The cost of visual inspections should be accurately calculated for the individual BMS in operation. Additionally, the cost of maintenance, repair and replacement strategies that have been implemented because of a visual inspection and condition rating assigned, should be accurately logged. In relation to the accuracy of inspector assigned condition ratings, a data collection strategy could be carried out, whereby: a group of inspectors trained in the BMS in operation, carry out inspections on many bridges with predetermined condition ratings assigned in advanced by a trained engineer. The variance in condition ratings assigned to each bridge, could give a guideline value in relation to inspector bias. Accurate data sets could dramatically increase the usefulness of the VoI in determining the role that visual inspection should pay in a BMS.

# 6.2 Opportunities for Further Work 

Based on the ideas presented in this thesis, there are several further research areas which logically follow; which include, but are not limited to:

- Analysis into benchmarking how human error affects the VoI and how this error varies for different bridge types, the condition rating, and how the consequences are defined.
- Determining a formal relationship between condition ratings and the reliability index and how this relationship could guide decision making in a BMS.
- What is the VoI of visual inspection for different BMSs in operation worldwide?
- What is the VoI of visual inspection in comparison with the other levels of bridge inspection? The current framework connecting the multilevel hierarchical inspection and testing of bridges could be investigated and the value of information received from each type of inspection determined. Analysis could then be undertaken to determine the revised hierarchy that would provide the greatest value for bridge asset managers.

This thesis is presented as a first step from which to exploit the vast landscape of large data-sets being created by BMSs in operation worldwide to further investigate the value that visual inspection provides in managing the global bridge stock. As it stands, visual inspection is the predominant method by which bridges are assessed, it is imperative that the value of the information received is defined and the value cut-

off determined, so that visual inspection can find its rightful place in the overarching bridge management context.
