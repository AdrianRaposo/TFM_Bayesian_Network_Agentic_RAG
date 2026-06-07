# Article 

## The Development of a Bayesian Network Framework with Model Validation for Maritime Accident Risk Factor Assessment

Lea Vojković ${ }^{1, *}$, Ana Kuzmanić Skelin ${ }^{2, * *}$, Djani Mohovic ${ }^{3}$ and Damir Zec ${ }^{3}$

## check for updates

Citation: Vojković, L.; Kuzmanić Skelin, A.; Mohovic, D.; Zec, D. The Development of a Bayesian Network Framework with Model Validation for Maritime Accident Risk Factor Assessment. Appl. Sci. 2021, 11, 10866. https://doi.org/10.3390/app112210866

Academic Editors: Ik-Soon Cho, Chong-Ju Chae and Margareta H. Lützhoft

Received: 21 October 2021
Accepted: 14 November 2021
Published: 17 November 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Faculty of Maritime Studies, University of Split, 21000 Split, Croatia
2 Faculty of Electrical Engineering, Mechanical Engineering and Naval Architecture, 21000 Split, Croatia
3 Faculty of Maritime Studies, University of Rijeka, 51000 Rijeka, Croatia; dmohovic@pfri.hr (D.M.); zec@pfri.hr (D.Z.)

* Correspondence: Ivojkovic@pfst.hr (L.V.); akuzmani@fesb.hr (A.K.S.); Tel.: +385-918-926-129 (L.V.)

Abstract: An integrative approach to maritime accident risk factor assessment in accordance with formal safety assessment is proposed, which exploits the multifaceted capabilities of Bayesian networks (BNs) by consolidation of modelling, verification, and validation. The methodology for probabilistic modelling with BNs is well known and its application to risk assessment is based on the model verified though sensitivity analysis only, while validation of the model is often omitted due to a lack of established evaluation measures applicable to scarce real-world data. For this reason, in this work, the modified Lyapunov divergence measure is proposed as a novel quantitative assessor that can be efficiently exploited on an individual accident scenario for contributing causal factor identification, and thus can serve as the measure for validation of the developed expert elicited BN. The proposed framework and its approach are showcased for maritime grounding of small passenger ships in the Adriatic, with the complete grounding model disclosed, quantitative validation performed, and its utilization for causal factor identification and risk factor ranking presented. The data from two real-world grounding cases demonstrate the explanatory capabilities of the developed approach.

Keywords: Bayesian belief network; Bayesian network validation; risk factor assessment; Bayesian inference; ship grounding model

## 1. Introduction

Previous experience and knowledge have defined maritime accidents as an undesirable condition of the vessel that occurs as a consequence of an initializing event and the combination of influencing factors led by a poorly understood system of causal relations. The Bayesian belief network (BBN), as a mathematical and computational framework for modelling interactions between influencing factors [1,2] has the ability to model multiple input and multiple output relations required to describe the maritime accident complex. The application of the Bayesian belief network model to the maritime domain has been on the rise in the past decade. In maritime research, BBNs have been widely utilized in navigational safety assessment [3], assessment of port collision risk influence factors [4], Arctic water transportation [5], accident severity in waterborne transportation [6], maritime piracy risk management [7], inland waterway transportation [8], and grounding and collision assessment [9-11], to name a few. It is quite challenging to make comparisons among different aspects of all the levels of details of the BBN framework, which stems from the fact that there is no generalized model for all types of maritime accidents, but a specific BBN is developed for each specific ship, area, environmental, human and technical factor, and combination thereof. Though the steps for constructing BBN models are well known, establishing the integrative BBN framework valid for future application to risk management is not a straightforward task. It comes with a spectrum of challenges, such as the definition of problem variables and dependencies among variables, tedious collection

and integration of historical data and expert knowledge and variable parametrization, verification of data flow consistency with expert expectations, and inference as the most important component of the framework. To avoid repeating good reviewing material with a detailed review of conceptual components of Bayesian belief network formalism and application for risk assessment in comparison to other approaches, the reader may refer to [12,13]. An excellent overview of maritime accident research from a broad perspective over the past 50 years, using 572 peer-reviewed papers, was published recently [14]. In [15], a recent overview of BBN modelling for shipping accidents is given.

While BBN modelling and sensitivity analysis-based verification has been previously employed and well established in maritime accident modelling, less attention has been given to investigation of the validation of maritime accident models built on the expert elicited BBN model. The goal of validation is to increase the reliability of a model when its purpose is to rank the factors that affect the accident or to exploit the model to examine the effect of action on individual observable or unobservable variables. Validation of the expert elicited Bayesian network is a difficult but required endeavor [16], upon which the validity of risk factor assessment depends. Qualitative validation approaches for this type of model are discussed in [17]; however, no clear procedure is available for quantitative validation of expert elicited BBN models. To this end, we develop a divergence-based measure for diagnostic inference that aims to quantitatively exploit each individual available real data case. While insufficient real case data for specific maritime accidents are scarce and cannot be efficiently deployed for learning-based accident model development, this work proposes to use it to test the diagnostic capabilities of an expert elicited model, giving in such a way to give quantitative insight into model behavior as the obtained data can be compared to the reported expert assessment, thus increasing the confidence in the developed model. Diagnostic inference is a promising analytic approach to identify possible causes, contributory factors, or ideally root cause of maritime accidents through forward-backward message passing in BBN; however, it has been underrepresented within maritime accident modelling and risk factor assessment due to a lack of established diagnostic inferential measures. To meet this shortcoming, we propose the Lyapunov-based divergence as a measure for identification of causal risk factors. This novel measure enables the diagnostic validation of a model and full exploitation of scarce real world data.

The complete approach is proposed and systematized in three phases. In the first phase, the BBN framework is employed for modelling influences among putative ship grounding risk factors and parametrization based on expert elicitation and historic data when available. The verification of the developed model is performed through sensitivity analysis. In the second phase, validation takes place through predictive and diagnostic inference on real scenarios. Predictive analysis of the BBN grounding model is performed to estimate the probability of grounding given evidence through forward evidence propagation, while for diagnostic inference, the newly proposed Lyapunov-based divergence measure is employed to identify risk factors. Within these settings, real world data can be efficiently exploited to validate the behavior of the model. Finally, in the third phase, the individual causal influence method [1,10] is employed to rank accident risk factors. The full pipeline of the process is given in Figure 1, which differs from previous methodology in a way that it extends the common BBN modelling and verification procedures with validation on real case accidents.

Motivation for this research on the maritime grounding risk of small passenger vessels lies in the fact that maritime traffic is continuously increasing in the Adriatic Sea due to the development of nautical tourism, with an evident increase in the number of small passenger vessels, their passenger capacity, and size. While to date the small number of accidents on the Croatian side indicate relative safety, novel developments and circumstances call for a safety review and risk factor analysis. Nowadays, the support to safety regulation and risk management depends on the existence of suitable maritime accident models and scientific risk analysis [18]. Although the Bayesian network framework has been developed for the

grounding of small passenger ships in the Adriatic, the proposed approach can be applied to similar accidents and the research of other expert elicited Bayesian belief networks.
![img-0.jpeg](img-0.jpeg)

Figure 1. The BBN framework for maritime accident risk factor assessment.
The rest of the paper is organized as follows: Section 2 presents the mathematical and computational background of Bayesian network modelling adopted for maritime accident reasoning. In this section, the predictive inference measures used in this work are systematized and adopted to the context of maritime accidents, and the novel Lyapunovbased divergence measure for diagnostic inference is defined. Section 3 explicates the modelling and verification as the first phase of the integrative approach. The second stage of the approach, i.e., the validation, both predictive and diagnostic, on real case data is given in Section 4. The final risk factors assessment based on the developed model is presented in Section 5. The paper is concluded in Section 6.

# 2. Bayesian Belief Network and Quantitative Measures for Causal Inference 

A Bayesian belief network (BBN) is an acyclic graph-based model consisting of nodes and probabilistic relationships among nodes that show the influences [2]. In a qualitative sense, nodes consist of N random variables $\mathrm{V}=\left\{\mathrm{V}_{1}, \mathrm{~V}_{2}, \ldots, \mathrm{~V}_{\mathrm{N}}\right\}$ and a set of directed edges E among nodes represent direct influence, i.e., a directed link from node $\mathrm{V}_{\mathrm{i}}$ to $\mathrm{V}_{\mathrm{j}}$ is causally interpreted as " $\mathrm{V}_{\mathrm{i}}$ causes $\mathrm{V}_{\mathrm{j}}$ " [2]. In terms of quantitative formulation, BBN is the joint probability distribution of values $\mathrm{v}=\left\{\mathrm{v}_{1}, \mathrm{v}_{2}, \ldots, \mathrm{v}_{\mathrm{N}}\right\}$ of N random variables $\mathrm{V}=\left\{\mathrm{V}_{1}, \mathrm{~V}_{2}, \ldots, \mathrm{~V}_{\mathrm{N}}\right\}$ :

$$
\mathrm{P}\left(\mathrm{v}_{1}, \mathrm{v}_{2}, \ldots, \mathrm{v}_{\mathrm{n}}\right)=\prod_{\mathrm{i}} \mathrm{P}\left(\mathrm{v}_{\mathrm{i}} \mid \mathrm{Pa}\left(\mathrm{v}_{\mathrm{i}}\right)\right)
$$

where $\mathrm{Pa}\left(\mathrm{v}_{\mathrm{i}}\right)$ are the parents of variable $\mathrm{V}_{\mathrm{i}}$, and $\mathrm{P}\left(\mathrm{v}_{\mathrm{i}} \mid \mathrm{Pa}\left(\mathrm{v}_{\mathrm{i}}\right)\right)$ is a local conditional probability associated with variable $\mathrm{V}_{\mathrm{i}}$ [19], which describes a parent-child relation.

To fully construct the BBN, the first requirement is to define the problem domain through identification of a relevant set of variables V constituting the problem being modelled. Second, relations among the variables are made to establish the graphical structure of the model, while in the next step, variable states and their relevant initial probabilities are assigned. Different information sources are used for variable identification, graph construction, and probability value assignment, such as a literature review, experts' beliefs, repository data, and empirical data. The BBN construction can be automated in domains with an abundance of data through structure learning and parameter optimization; however, the adoption of the BBN framework for modelling in maritime accidents, where data is sparse or not available, is tedious work that requires the involvement of an interdisciplinary team for maritime domain problem analysis, model structuring, and parametrizing, as will be described in Section 3.

Once developed, the BBN model represents a formal model for inference and causal reasoning [20], and can be exploited for predictive and diagnostic analysis to extract the explanations of the domain through belief update via forward and backward message passing [1]. In order to interpret BBN model outputs through both predictive analysis with cause-to-effect queries, and diagnostic analysis with combined cause-to-effect and effect-to-cause queries, the variables of a BBN are related to causal reasoning system notation. A causal set $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ of $n=1, \ldots r, r=N-1$, random variables $\mathrm{X} \subset \mathrm{V}$ of BBN is a set of risk factors that can directly or indirectly cause an accident. The remaining variable from the set $\mathrm{V} \backslash \mathrm{X}$ is a targeted event, i.e., maritime accident, denoted as Y. Each causal variable $X_{i} \in X$ can further be related in a cause-effect manner to variables from $X \backslash X_{i}$, as indicated by the link direction. In regard to the modular definition of the Bayesian network [21], causes at different levels of the network can be treated as effects, which is exploited when performing both predictive and diagnostic analysis of hypothetic scenarios and real world data. Through this modularity mechanism, a BBN accident model allows for arbitrary cause-effect and effect-cause queries of type "What's the probability of grounding given traffic distribution is high?", or "What's the probability of being off course given traffic distribution is high, there's no radar and personal condition is poor?" to be answered. Additionally, our work introduces a method to investigate the queries of the type "Which unobserved risk factor most likely contributed to the accident given evidence?" In the next section, the inference measures for quantitative interpretation of the BBN are introduced and the novel diagnostic measure is described.

# 2.1. Causal Inference Measures 

The causal inference in the Bayesian framework aims to estimate the causes of observed effects, given the current data and data manipulation [22]. In order to estimate the posterior probabilities of causes and effects, the BN model can be investigated with respect to variations of all BN variables.

The causal influence of an individual risk variable $X_{i}$ on the targeted maritime event Y is most commonly assessed by observing the difference of conditional probability $\mathrm{P}\left(\mathrm{Y} \mid \mathrm{X}_{\mathrm{i}}\right)$, [9,23,24]. The predictive individual causal influence is defined as:

$$
\operatorname{ICI}\left(X_{i}\right)=P\left(Y \mid X_{i}=x_{1}\right)-P\left(Y \mid X_{i}=x_{0}\right)
$$

where $\operatorname{ICI}\left(\mathrm{X}_{\mathrm{i}}\right)$ measures the sensitivity of the effect variable Y to changes in the causal factor $\mathrm{X}_{\mathrm{i}}$, where $\mathrm{x}_{1}$ denotes the presence of $\mathrm{X}_{\mathrm{i}}$ and $\mathrm{x}_{0}$ denotes the absence of $\mathrm{X}_{\mathrm{i}}$. This measure serves to identify importance ranking of causal variables. In a BBN, each casual factor $\mathrm{X}_{\mathrm{i}}$ is required to influence the probability of the occurrence of Y. According to the definition of (2), positive values of $\operatorname{ICI}\left(\mathrm{X}_{\mathrm{i}}\right)$ should be observed for all factors $\mathrm{X}_{\mathrm{i}}$. In this sense, the $\operatorname{ICI}\left(X_{i}\right)$ can validate a network in two ways: it helps to prune the noninfluential factor and correct the conditional probability data assigned to the network that does not obey monotonicity suggested by the expert [25]. If $\operatorname{ICI}\left(X_{i}\right)$ is lower than a predefined small sensitivity threshold $\tau$, it indicates that the cause $X_{i}$ has no influence on the change of the probability of the effect variable or its influence is insignificant, and therefore $X_{i}$ can be

removed from the network. If $\operatorname{ICI}\left(\mathrm{X}_{\mathrm{i}}\right) \leq 0$, it can serve as an indicator of local inconsistency in parametrization of the network, which should respect the predefined monotonicity of the causal parent-child relation.

The $\operatorname{ICI}\left(\mathrm{X}_{\mathrm{i}}\right)$, as a measure of the influence of an individual risk factor, is based on the forward propagation mechanism. The same message passing direction allows for quantitative presentation of the influence of multiple coexisting risk factors, $\epsilon \in X$, on an accident, by examining the state changes of the effect variable Y:

$$
\Delta \mathrm{P}_{\mathrm{e}}(\mathrm{Y})=\mathrm{P}(\mathrm{Y})-\mathrm{P}(\mathrm{Y} \mid \mathrm{e})
$$

which provides an average causal influence of the evidence set e. The effect variable Y of a maritime accident is defined as a binary variable containing the states "yes" and "no". Values $\Delta \mathrm{P}_{\mathrm{e}}\left(\mathrm{Y}={ }^{\prime \prime}\right.$ yes $\left.{ }^{\prime \prime}\right)<0$ indicate that evidence increases the probability of an accident. Conversely, value $\Delta \mathrm{P}_{\mathrm{e}}\left(\mathrm{Y}={ }^{\prime \prime}\right.$ yes $\left.{ }^{\prime \prime}\right)>0$ is interpreted as a decrease of the probability of an accident. $\Delta \mathrm{P}_{\mathrm{e}}(\mathrm{Y})$ represents a quantitative measure for scenario analysis and "what-if" analysis and is equally applicable on real observations or hypothetic data. In this work, the $\Delta \mathrm{P}_{\mathrm{e}}(\mathrm{Y})$ measure will enable validation of the developed BN model with real case grounding data.

The major drawback of these widely employed measures in the maritime domain is that they provide causal influence rankings as valid as the developed BN is a valid model of the domain. In the literature, these measures are used to provide ranking based on BN models verified only through sensitivity analysis. It is therefore of great importance to include validation on real case data. In the next subsection, we introduce a novel measure that makes use of scarce real world data and thus enables the verification of the developed model.

# 2.2. Lyapunov-Based Divergence Measure for Causal Factor Identification 

Causal candidates, $X_{i}^{\mathrm{u}} \in\left\{\mathrm{X}_{\mathrm{i}} \backslash \mathrm{e}\right\}$, are unobservable risk variables whose probabilistic state values diverge when the effect variable state transitions from state "no" to state "yes", given that the transition is mediated by the influence of the observable variables, e, i.e., transition is induced by the evidence variable. This definition follows the form of the definition of a maritime accident, which states that an accident is preceded by a certain combination of influential factors. In other words, when evidence variables are instantiated at a nominal state of a model, where the nominal state is one with no accident, then the effect, i.e., accident, variable, is instantiated to the state "yes" so as to mimic the dynamics leading to an accident, and it can be expected to observe sequential changes in the probabilities of unobservable factors $X_{i}^{\mathrm{u}}$. The sequential state values $P_{i}^{\mathrm{u}}\left(X_{i}^{\mathrm{u}} \mid \mathrm{Y}={ }^{\prime} \mathrm{no}^{\prime}\right) \rightarrow P_{i}^{\mathrm{u}}\left(X_{i}^{\mathrm{u}} \mid \mathrm{Y}={ }^{\prime} \mathrm{no}^{\prime} ; \mathrm{e}\right) \rightarrow P_{i}^{\mathrm{u}}\left(X_{i}^{\mathrm{u}} \mid \mathrm{Y}={ }^{\prime}\right.$ yes $\left.^{\prime} ; \mathrm{e}\right)$, where symbol " $\rightarrow$ " denotes transition, provide novel information. By examining the rate of change of these values, a diverging behavior of unobservable causal factor can be identified. For example, the values:

$$
\begin{gathered}
\delta \mathrm{F}_{1}=\mathrm{P}_{1}^{\mathrm{u}}\left(\mathrm{X}_{i}^{\mathrm{u}} \mid \mathrm{Y}={ }^{\prime} \mathrm{no}^{\prime} ; \mathrm{e}\right)-\mathrm{P}_{i}^{\mathrm{u}}\left(\mathrm{X}_{i}^{\mathrm{u}} \mid \mathrm{Y}={ }^{\prime} \mathrm{no}^{\prime}\right) \\
\delta \mathrm{F}_{2}=\mathrm{P}_{i}^{\mathrm{u}}\left(\mathrm{X}_{i}^{\mathrm{u}} \mid \mathrm{Y}={ }^{\prime} \text { yes }^{\prime} ; \mathrm{e}\right)-\mathrm{P}_{i}^{\mathrm{u}}\left(\mathrm{X}_{i}^{\mathrm{u}} \mid \mathrm{Y}={ }^{\prime} \mathrm{no}^{\prime} ; \mathrm{e}\right)
\end{gathered}
$$

that are both positive, $\left(\delta \mathrm{F}_{1}>0 \& \& \delta \mathrm{~F}_{2}>0\right)$, indicate the sequential growth of the probability of the causal factor $\mathrm{X}_{\mathrm{i}}$, which is interpreted as a rise of the negative influence of the causal factor $\mathrm{X}_{\mathrm{i}}$. The interpretation follows from the monotonicity property of BBN. The conceptual representation of possible parameter probability changes of $\mathrm{X}_{\mathrm{i}}$ in two sequential steps is visualized in Figure 2 and it is the interest of the approach to identify only those with sequential decay of probability.

![img-1.jpeg](img-1.jpeg)

Figure 2. Conceptual representation of possible probability parameter changes of $X_{i}$.
The described process can be formalized with a dynamical state-space model [26,27]:

$$
\begin{aligned}
& \frac{d p_{i}}{d x}=\lambda p_{i}(x) \\
& p_{i 0}=p_{i}\left(x_{0}\right)
\end{aligned}
$$

Function $p(x)$ is a path of evolution of the homogenous dynamical system with respect to change in the variable $x$, where $p_{0}$ is an initial value. The solution of the model is:

$$
p_{i}(x)=p_{i 0} e^{\lambda_{i}\left(x-x_{0}\right)}
$$

The component $e^{\lambda_{i}\left(x-x_{0}\right)}$ is a state transition matrix. Constant $\lambda_{i}$ is known as the Lyapunov exponent [28,29], which describes how small distances between nearby points in the state space change with time in continuous systems or change with the sample instance in discrete systems, and serves to identify stabile diverging of chaotic behavior of the system. There are as many Lyapunov exponents as there are sample instances. The average constant $\lambda$ has a positive value when the system is unstable, negative when the system is stable, and a zero value indicates marginal stability. Figure 3 shows the idea of the Lyapunov exponent in the time domain with transition matrix $e^{\lambda\left(t-t_{0}\right)}$ :
![img-2.jpeg](img-2.jpeg)

Figure 3. The example of diverging distances based on Lyapunov exponent theory.
The interest of the proposed approach is not to calculate the Lyapunov characteristic exponent, but to apply the model to identify the causal factor whose state value changes

obey the exponential model for unstable behavior, i.e., when $\lambda$ is positive. It can be observed that the Lyapunov exponent-based distance is an example of the exponential distance model. Relations for diverging distances are easily translated from the time domain to a discrete state space denoted as $\mathrm{x}_{0}, \mathrm{x}_{1}, \mathrm{x}_{2}, \ldots, \mathrm{x}_{\mathrm{n}}$, which is required for application to the BBN model, as follows:

$$
\begin{gathered}
\frac{\left\|\delta\left(\mathrm{x}_{\mathrm{n}}\right)\right\|}{\left\|\delta\left(\mathrm{x}_{0}\right)\right\|} \approx \mathrm{e}^{\lambda\left(\mathrm{x}_{\mathrm{n}}-\mathrm{x}_{0}\right)} \\
\frac{\left\|\delta\left(\mathrm{x}_{1}\right)\right\|}{\left\|\delta\left(\mathrm{x}_{0}\right)\right\|} \frac{\left\|\delta\left(\mathrm{x}_{2}\right)\right\|}{\left\|\delta\left(\mathrm{x}_{1}\right)\right\|} \cdots \frac{\left\|\delta\left(\mathrm{x}_{\mathrm{n}}\right)\right\|}{\left\|\delta\left(\mathrm{x}_{\mathrm{n}-1}\right)\right\|} \approx \mathrm{e}^{\lambda_{10}\left(\mathrm{x}_{1}-\mathrm{x}_{0}\right)} \cdot \mathrm{e}^{\lambda_{21}\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)} \ldots \cdot \mathrm{e}^{\lambda_{\mathrm{nn}-1}\left(\mathrm{x}_{\mathrm{n}}-\mathrm{x}_{\mathrm{n}-1}\right)}
\end{gathered}
$$

Based on the stability identifying property of the solution Equation (5), and derived discrete space relation Equation (7), we propose measurement of the diverging behavior of i causal candidates $\mathrm{X}_{i}^{\mathrm{ii}}, \operatorname{DR}\left(\mathrm{X}_{i}^{\mathrm{ii}}\right)$, as the product of transition matrices available from the imposed dynamics of an accident. In reality, the exact evidence sequence is rather unknown. In this work, two reasonable consecutive interventions are made on the model variables: firstly, on evidential causal variables and, secondly, on the effect variable, as given by a real world accident report. Thus, the dynamics is observed as $\delta \mathrm{F}_{1}$ and $\delta \mathrm{F}_{2}$, and measured by values of Equation (8):

$$
\operatorname{DR}\left(X_{i}^{\mathrm{ii}}\right)=\mathrm{e}^{\lambda\left(\mathrm{x}_{1}-\mathrm{x}_{0}\right)} \mathrm{e}^{\lambda\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right)}=\mathrm{e}^{\delta \mathrm{F}_{1}} \mathrm{e}^{\delta \mathrm{F}_{2}}
$$

The values $\operatorname{DR}\left(X_{i}^{\mathrm{ii}}\right)>1$ are selectors of causal candidates if and only if $\delta \mathrm{F}_{1}>0 \& \&$ $\delta \mathrm{F}_{2}>0$.

The value $\lambda$ for diverging behavior is set to be positive and locally constant. Since $\lambda$ has a constant multiplicative effect on differences $\left(\mathrm{x}_{1}-\mathrm{x}_{0}\right),\left(\mathrm{x}_{2}-\mathrm{x}_{1}\right), \ldots$, which does not change the evaluation value $\operatorname{DR}\left(X_{i}^{\mathrm{ii}}\right)$, it can be set to unity in the calculations of Equation (8).

The results of the application of the Lyapunov-based divergence measure are presented in Section 4.2.

# 3. BBN Model Structuring and Verification for a Grounding Accident 

The proposed framework and its approach are demonstrated for maritime grounding of small passenger ships in the Adriatic. Grounding is the position of a vessel, in which the vessel touches the seafloor to the extent that it does not permit its further navigation by its own machinery or equipment without damaging the hull, machinery, or equipment of the ship [30]. Regarding vessels under 70 m , these mostly sail in the summer season, starting from April to the end of October. The maximum passenger capacity is 250 . Observed vessels are divided into the following two groups: for one day or seven-day cruising. Day trips are characterized by a $2-3 \mathrm{~h}$ navigation. Ship leaves the home ports in the morning, takes passengers to tourist destinations, and return to home ports on the same day. The passenger capacity and the usual routes of these ships are volatile and dependent on customer needs. Multi-day cruise ships are ships with a capacity of 12 to 50 passengers. Passengers board home ports on a 7 day or 14 day basis. Their daily navigation duration is the same as for excursion boats. During the night, boats berth in ports or at tourist destinations. On average, ship speeds for daily cruises and for multi-day cruises range from 7 to 15 knots. Small passenger ships are characterized by navigation and anchoring near tourist attractions, whereby they sail and anchor in areas of increased traffic density and shallow areas due to the attractive environment of certain lagoons and similar shallow areas, thereby increasing the risk of grounding. They are often moored in ports with insufficient berths, increasing the likelihood of a maritime accident.

### 3.1. Qualitative and Quantitative Background Knowledge

Maritime transportation is a complex socio-technical system that is often influenced by economic pressures. At the coarse level of organization of the baseline BBN model structure, grounding impact factors are divided into human, organizational, external, and

technical factors. Each factor has subfactors and each of them can affect a number of other factors. Subsequently, coarse-level factors are refined into detailed variables suitable for implementation into the BBN framework (terms factor, variables, nodes are used interchangeably throughout the paper, though they represent a single concept.)

In maritime transportation, accidents caused by human error are most common. Existing data and research to date shows that $43 \%$ to $96 \%$ of all marine casualties are caused by human error. According to [31], human factors cause $67.6 \%$ of maritime grounding accidents. The nodes relating to human error and organizational segments are deliberately emphasized in the model.

Human factors are part of a scientific discipline that deals with the study of human abilities (perception, mental state, etc.) and its limitations in relation to the system [27]. The term "human factor" is often confused with the term "human error". According to [32], various authors' use of different definitions makes it extremely difficult to identify difference between human error and human factor. According to [33], human error is an intolerant activity or deviation from normal behavior whose boundaries are defined by the system and as such is a direct cause of a maritime accident. According to [34], the human factor is the root cause of a maritime casualty. According to the definition used by authors in their work, the human factor consists of organizational, group and individual factors that affect maritime safety. In this paper, the term "human error" is used as the immediate cause of a marine casualty caused by human behavior.

Organizational factors reduce the risk of maritime accidents as human experience can significantly reduce the likelihood of a maritime accident by knowledge and use of safety measures.

Technical factors refer to equipment like hardware, software, and vessel construction. Statistically, $20 \%$ of maritime accidents are caused by technical factors [35].

External factors refer to variables related to hydrometeorology, weather, traffic distribution, navigation in shallow water and special caution area navigation.

Identified factors are organized to form a causal network structure according to the subjective opinion of the expert. It is necessary to include expert knowledge at the point of structuring because most of the databases of maritime accidents do not provide causal relations, but only enumerated statistical information on different factors and consequences. The disparities in the organization of statistical data extends to the quantitative aspect of BBN modeling.

According to [36], statistical data adds to the uncertainty of the model, as this data are often incomplete or not properly investigated. For example, it is known that a certain number of accidents are not regularly reported and as such do not undergo official statistical processing nor inclusion in the databases. Additionally, real accident data collected without proper investigation often do not include the chain of events that causally led to marine accidents, thus event ordering as potentially useful information for modeling is not available.

Due to the above data limitations, including the relatively small samples in the statistical realm of rare events and inconsistent information organization, existing statistical data were supplemented with expert estimation of parameter values in the model. Statistical data were used to assign a priori values of the following factors: time and hydrometeorological factors. Human node values and parts of organizational factors are taken from other sources [9,26,36]. All other factor values in the model as well as the conditional probability tables are deduced from expert knowledge elicitation. Standard formal procedures for gathering and combining expert judgments were followed, as proposed in $[37,38]$.

Experts participated by answering simple questions, such as "What causes stress on the bridge?", "What are the causes of loss of control?", and "What are the most influential grounding factors?" When assigning values to a conditional probability table, experts were offered one or two important conditional probabilities of the node they discussed, using Van der Gaag's technique [37] of assigning values of several hundred or thousands of

conditioned probabilities of expert opinions in a quick and easy way. The method used to assign values is the probabilistic scale. The probabilistic scale is a horizontal or vertical line with numerical values. The values offered to the experts are: $(0.1,0.25,0.5,0.75,0.9)$. The median of the expert assigned values is entered in the conditional probability tables. SMILE (structural modeling, interface, and learning engine) [39] and GeNie GUI (graphical network interface) [40] were used to create and quantify the Bayesian network.

The complete grounding model is presented in Figure 4, and it refers to the grounding pertinent to the scenario when the ship is in navigation. The grounding model consists of 30 variables including the grounding variable, among which 13 variables are root variables. Variables are described in Appendix A.
![img-3.jpeg](img-3.jpeg)

Figure 4. Quantitative grounding model for passenger non-liner small vessels.
Detailed reasoning and the process of structuring and parametrization requires further elaboration and reasoning, which is given in the following section.

# 3.2. BBN Model Verification 

According to the authors [11,41], the model should be sufficiently plausible and serve as a basis for future risk analysis. Sensitivity analysis is a technique used to verify parameters of a Bayesian network [42]. Sensitivity analysis verifies the effect of small changes of the numerical values of network variables on the posterior probabilities of observed risk factor causal variables and the effect variable. Highly sensitive causal variables will have a significant impact on the effect variable. Additionally, evaluation of the sensitivity of the effect variable may provide information on the strength of the influence of causal variables. When the sensitivity values are different from those expected, then the sensitivity analysis provides identification of the parameters, which requires correction and calibration. This is often a repetitive process, which is terminated when the expected results are observed. Thus, the model verification process evaluates how well the model specifies the system it represents [23,36]. Verification tests cannot provide the accuracy of the model, but rather show whether the model is a credible representation of the modelled accident.

The algorithm for sensitivity analysis described in [42], and implemented in GeNie [5], is used for verification of the BBN model. After selecting specific nodes called "target nodes", the algorithm calculates the complete posterior probability distribution derivative sets of selected nodes over all numerical parameters of the Bayesian network [5,42]. The sensitivity testing results are given for "grounding" and "loss of control" variables, in Figures 5 and 6, respectively.
![img-4.jpeg](img-4.jpeg)

Figure 5. Sensitivity analysis for the grounding model when targeting "grounding".
![img-5.jpeg](img-5.jpeg)

Figure 6. Sensitivity analysis for the grounding model when targeting "loss of control".

By targeting "grounding", the sensitivity is most prominent to "navigation in shallow waters" and "special caution area", followed by "human error", "off course", "navigation error", and "loss of control", as shown in Figure 7.
![img-6.jpeg](img-6.jpeg)

Figure 7. Sensitivity of "grounding" to causal variables of the model (w/o "navigation in shallow waters" and "special caution area").

It can be observed that "grounding" is sensitive to variables that refer to the group of human factors: "familiarization", "stress level", "tired", "incapacitated", and "safety culture". High uncertainty is also observed for external variables related to the hydrometeorological impact, such as "sea state" and "wind force", which is in line with the reasoning that the influence of the sea state and wind can be significant for the small sailing cruisers observed in this study.

Targeting "loss of control" provided the highest sensitivity to "human error", "personal condition", "incapacitated", and "safety culture" as shown in Figure 8. It can be observed that the highest sensitivity of "loss of control" is shown to the group of human factor variables, which corresponds to the expected results. Significant sensitivity is also shown by the variable "maintenance" and the variables related to technical errors.
![img-7.jpeg](img-7.jpeg)

Figure 8. Sensitivity analysis for the grounding model when targeting "loss of control".

The obtained results ranked the influential variables in an order that is in accordance with the theoretical knowledge on the causes of grounding accidents, which verifies that the model is sufficiently plausible for further risk analysis.

# 4. BBN Model Validation 

The developed model is validated against two real world grounding cases: the grounding of the passenger ship "Zlatni Zal" and the grounding of the passenger ship "Cicero".

Case "Zlatni Zal"-Ship "Zlatni Zal" is powered by two diesel engines with a power of $492 \mathrm{~kW}, 33.5 \mathrm{~m}$ long, 5.3 m wide, 1.58 m draft, and 109 GT. The ship has radar. While sailing, he suffered a maritime accident grounding on the island Sćedro on 1 April 2017. At the time of grounding, favorable weather conditions and excellent visibility prevailed, and the captain's recklessness was determined as the cause of the accident.

Case "Cicero"-Another example of comparing the model results to a real event is the grounding of a small passenger vessel Cicero. It is a vessel used for a seven-day cruise, 32 m long, which grounded near the Splitska vrata on 18 September 2019 in the afternoon. Weather conditions were favorable at the time of the marine casualty. According to the maritime accident report, the maritime accident did not occur due to a technical failure of the ship, nor the navigation system, nor due to some external or internal influences, but due to human impact, i.e., the assessment and decision of the person operating the ship, ultimately resulting in the grounding. There were 25 passengers on board.

### 4.1. Model Validation Based on Predictive Inference

Case "Zlatni Zal"-Based on the propositions in Section 2.1 and the accident report for "Zlatni Zal", the instantiation of evidence is introduced. The root nodes were assigned the values specified in the report of the grounding "Zlatni Zal". The node values "weather", "day/night", "day" and "season", "sea state", "wind force", "situational awareness", and "visibility" form the evidence set e. According to Equation (3), average causal influence amounts to a negative value, $\Delta \mathrm{P}_{\mathrm{e}}$ ("grounding" = " yes") $=-2 \%$, where negative values indicate the increased likelihood of the occurrence of the accident (Figure 9).
![img-8.jpeg](img-8.jpeg)

Figure 9. Model of the grounding of a small passenger ship "Zlatni Zal" according to the report on the maritime accident.

Case "Cicero"-Based on the propositions in Section 2.1 and the accident report for "Cicero", the instantiation of evidence is introduced. The root nodes were assigned the values listed in the Cicero marine casualty report: weather, "day/night", "day", "season", "visibility", "special caution area", "sea state", and "wind force" (Figure 10). Ac-

cording to Equation (3), the average causal influence amounts to a negative value, $\Delta \mathrm{P}_{\mathrm{e}}$ ("grounding" = " yes") $=-22 \%$, where negative values indicate an increased likelihood of the occurrence of the "Cicero" accident.
![img-9.jpeg](img-9.jpeg)

Figure 10. Model of the grounding of a small passenger ship "Cicero" according to the report on the maritime accident.

If the developed BBN model had been used immediately before both accidents, on the available evidence, its response would issue a warning, which is in line with one of the model development objectives

# 4.2. Model Validation Based on Diagnostic Inference 

Case "Zlatni Zal"-Based on the propositions in Section 2.2 and the accident report for "Zlatni Zal", the stepwise instantiation of evidence is introduced. First, forward propagation of the observed evidence of causal variables is performed and unobserved causal variable changes are collected. Then, backward propagation from the grounding variable is added. Again, unobserved variable changes are collected. Finally, diverging change $\operatorname{DR}\left(\mathrm{X}_{i}^{\mathrm{ti}}\right)$ from the Equation (8) is used to identify the factors $\mathrm{X}_{i}^{\mathrm{ti}}$ with consistently increasing change of the accident contributing causal parameter. The Lyapunov-based diverging change $\operatorname{DR}\left(\mathrm{X}_{i}^{\mathrm{ti}}\right)$ selects seven variables, as shown in Figure 11.

The obtained results are interpreted with respect to the network structure, as shown in Figure 12. The selected causal variable that has the strongest causal contribution to grounding of "Zlatni zal" is "loss of control", supported by causal variables higher in the structure: "AIS", "human error", "personal condition", "breakdown", "other distraction", and "maintenance". All the parameters of the selected factors have negatively affecting states, e.g., "loss of control" state "yes", "AIS" state "No", "human error" state "yes", "personal condition" state "bad", etc.

As explained in Section 2, due to modularity, BBN causes at different levels of the network can be treated as effects, which is exploited in a diagnostic interpretation mechanism that led to an accident. The propagation of information is observed in the bottom-up direction, and reasoning is as follows: it is known from the accident report that "navigation in shallow water" and "special caution area" cannot be accident contributory causal factors. Therefore, "off course" is the only remaining gate through which the propagation was possible. "Off course" could have been caused through three direct causal factors: "loss of control", "navigational error", and "vessel damage". The DR measure identified the "loss of control", which is strongly supported by "AIS" and "human error". Additional

weaker support of "loss of control" comes from "breakdown", "other distractions", and "maintenance". Figure 12 visualizes the accident-contributing candidates for "Zlatni Zal" in a model structure (the BBN structure of Figure 12 is created with Netica [19]).
![img-10.jpeg](img-10.jpeg)

Figure 11. Candidate selection using the Lyapunov-based divergence measure.
![img-11.jpeg](img-11.jpeg)

Figure 12. Visualization of the accident-contributing candidates for "Zlatni Zal".
Case "Cicero"-Based on the propositions in Section 2.2 and the accident report for "Cicero", the stepwise instantiation of evidence is introduced, in a similar manner as in the "Zlatni Zal" case. The DR measure identified "navigational error" as the sole accidentcontributing causal factor. Figure 13 visualizes the accident-contributing candidate for "Cicero" in a model structure.

When the BBN causes at different levels of the network are observed as effects, and the information is observed in the bottom-up direction, the following inference is drawn: it is known from the accident report that "navigation in shallow water" and "special caution area" cannot be causal variables and therefore, "off course" is the only remaining gate through which the propagation was possible. "Off course" could have been caused through three direct causal variables: "loss of control", "navigational error", and "vessel damage". The DR measure identified the "navigational error".

![img-12.jpeg](img-12.jpeg)

Figure 13. Visualization of the accident contributing candidate for "Cicero".
Validation against two real world grounding cases has demonstrated the plausible predictive performance, and excellent explanatory performance of the developed model as the results are in accordance with the reported causes of marine casualties in the marine casualty report obtained by authorities.

# 5. Grounding Risk Factor Ranking Based on the Developed BBN Model 

The developed and verified BBN model represents a formal model for inference and causal reasoning. Using the $\operatorname{ICI}\left(X_{i}\right)$ measure, described in Section 2.1, the ranking of variables $X_{i}$ is made that has the largest causal influence on the effect variable. Ranking based on ICI for grounding is shown in Figure 14.
![img-13.jpeg](img-13.jpeg)

Figure 14. Ranking of risk factors for grounding.

The results show that the "navigation in shallow" has the greatest influence on the "grounding", which is in accordance with the expected expert belief for grounding accidents. Next, the model estimates the following factors as significant contributors to accident occurrence: "safety culture", "off course", "loss of control", and "human error". These factors comprise the joint group of human factors, which indicates that primary intervention on these factors is advisable when developing cost-effective measures to reduce the probability of an accident.

# 6. Conclusions 

In this work, a complete methodology for assessing the risk factors of a maritime accident was developed that joins and exploits two main features of the Bayesian belief network framework: (i) probabilistic semantics of a Bayesian belief network that allows for modelling with uncertainty and incomplete data, and (ii) bi-directional information flow from "cause-to-effect" and "effect-to-cause". In summary, a twofold contribution can be distilled. First, the complete framework for modeling and risk factor assessment of maritime accidents is systematized. Second, the novel measure for quantitative identification of contributing causal factors, named the Lyapunov-based divergence measure, is proposed that enables validation through diagnostic inference in BBN and identification of multiple causation factors. The advantage of the application of the Lyapunov-based divergence measure is twofold: it enables model validation through efficient use of existing real world accident data, and it allows a diagnostic of future cases and scenarios. The developed model and subsequent analysis expand the understanding of the influential factors on the maritime accident. The complete methodology ultimately supports decision-making when adopting certain measures to increase the maritime safety. Though the complete framework was showcased on a grounding of small passenger ships in the Adriatic, it can easily be generalized to risk assessment of other major maritime accident types. The limitations of the current work are related to the uncertainty of the network structure and node parametrization, due to the influence of expert knowledge, which might not be as objective as data-driven structuring and parametrization would be. This limitation, however, is not unique to our approach, yet it is inherent to the expert elicited BN. An overview of limitations of BNs in the maritime accident domain is well covered in the work of [43]. In the future work, the root cause identification analysis with the proposed Lyapunov-based divergence measure will be used to assess different accident-reducing actions through conjunctive query inferences and thus will enable the development of a system for case-action assessment. This will require the deployment of a simulation environment with a scenario-based data generation process. In order to achieve this goal, the developed static BN will be transferred into a dynamic Bayesian network framework, which will enable improved state-space analysis and consequent risk factor identification. This adaptation will give rise to interesting new challenges, and one of a few problems that will have to be investigated is how to perform a validation of the state-space varying Bayesian network as it will aggravate the real world data scarcity problem.

Author Contributions: Conceptualization, A.K.S.; methodology, L.V. and A.K.S.; software, L.V. and A.K.S.; validation, A.K.S.; formal analysis, L.V.; investigation, L.V.; writing-original draft preparation, L.V. and A.K.S.; writing-review and editing, L.V. and A.K.S.; supervision, D.M. and D.Z. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.
Conflicts of Interest: The authors declare no conflict of interest.

# Appendix A 


