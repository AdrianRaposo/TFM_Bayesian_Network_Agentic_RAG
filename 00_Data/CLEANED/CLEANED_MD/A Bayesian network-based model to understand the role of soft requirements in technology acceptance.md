# A Bayesian Network-Based Model to Understand the Role of Soft Requirements in Technology Acceptance: the Case of the NHS COVID-19 Test and Trace App in England and Wales 

Luis H. Garcia Paucar<br>SEA Group, Aston University, UK<br>garcial2@aston.ac.uk<br>Alistair Sutcliffe<br>Durham University, UK<br>alistair.g.sutcliffe@durham.ac.uk

## ABSTRACT

Soft requirements (such as human values, motivations, and personal attitudes) can strongly influence technology acceptance. As such, we need to understand, model and predict decisions made by end users regarding the adoption and utilization of software products, where soft requirements need to be taken into account. Therefore, we address this need by using a novel Bayesian network approach that allows the prediction of end users' decisions and ranks soft requirements' importance when making these decisions. The approach offers insights that help requirements engineers better understand which soft requirements are essential for particular software to be accepted by its target users. We have implemented a Bayesian network to model hidden states and their relationships to the dynamics of technology acceptance. The model has been applied to the healthcare domain using the NHS COVID-19 Test and Trace app (COVID-19 app). Our findings show that soft requirements such as Responsibility and Trust (e.g. Trust in the supplier/brand) are relevant for the COVID-19 app acceptance. However, the importance of soft requirements is also contextual and time-dependent. For example, Fear of infection was an essential soft requirement, but its relevance decreased over time. The results are reported as part of a two stage-validation of the model.

## KEYWORDS

Technology acceptance, soft requirements in SE, Bayesian inference, Reasoning tools, probabilistic models, human values

## ACM Reference Format:

Luis H. Garcia Paucar, Nelly Bencomo, Alistair Sutcliffe, and Pete Sawyer. 2022. A Bayesian Network-Based Model to Understand the Role of Soft Requirements in Technology Acceptance: the Case of the NHS COVID19 Test and Trace App in England and Wales. In The 37th ACM/SIGAPP Symposium on Applied Computing (SAC '22), April 25-29, 2022, Virtual Event,

[^0]
## Nelly Bencomo

AIHS Group, Durham University, UK
nelly.bencomo@durham.ac.uk

## Pete Sawyer <br> SEA Group, Aston University, UK <br> p.sawyer@aston.ac.uk

. ACM, New York, NY, USA, Article 4, 10 pages. https://doi.org/10.1145/ 3477314.3507147

## 1 INTRODUCTION

The success of software-based systems largely depends on understanding their requirements but also, being able to persuade potential users that the benefits of using an application outweigh the related costs or disadvantages, hence ensuring adoption and continued use [9, 12, 43]. Requirements Engineering (RE) techniques have been mainly focused on detailed functional and non-functional characteristics of a potential software product [4, 20, 29, 46, 47]. Traditionally, soft requirements have not been considered in such techniques. Soft requirements include users' perceptions of values, and their influence on requirements is noteworthy. Soft requirements also cover other aspects such as emotions (e.g. fear, pleasure, anger), which have an impact on acceptance and use of software products [43]. Existing research in Technology Acceptance TA $[13,33,49]$ has supported the analysis of soft requirements that may contribute to software products success. However, these studies still lack prediction support to help requirements engineers to deal with uncovered soft requirements and their combined effects on software products adoption. Hence, there is a gap between RE, which has focused on detailed functional and non-functional characteristics of potential software products, and TA analysis to identify soft requirements and quantify their influence on software products success. We argue that to address these issues and better understand the acceptance of software products, we need to enrich RE techniques by including soft requirements and their effects. More precisely, we aim to support requirements engineers to help them understand the motivations for and barriers to the adoption of a new product. Our research makes the following contributions:

- A probabilistic approach to quantify how important soft requirements are in the adoption of software products.
- Evaluation of the approach by its implementation on a case study.

In this paper, a novel Bayesian network (BN) model has been used. One important reason for its selection as a model implementation technique was its capacity to simulate the occurrence of events (which are settled as evidence in the Bayesian network), and predicts the likelihood of any of several possible causes [23]. For example, one event could be the users' disposition is equal to "Yes"


[^0]:    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
    SAC '22, April 25-29, 2022, Virtual Event,
    (C) 2022 Association for Computing Machinery.

    ACM ISBN 978-1-4503-8713-2/22/04... $\$ 15.00$
    https://doi.org/10.1145/3477314.3507147

to download an app. Given that event, the model can infer the most critical soft requirements for influencing that event.

The BN model provides a ranking technique for soft requirements and predicts end users' decisions regarding their disposition to download and install a software product. Specifically, a ranking of soft requirements that influences decisions to adopt the COVID-19 app was established. To do so, we conducted a sensitivity analysis of the probabilistic model to determine how different values of influential combinations of soft requirements affect the end users' decisions on whether to download and install the app. We then identified a set of acceptance scenarios uncovered from the sensitivity analysis. Finally, actual end users' responses, collected from an online survey, have been tested against these scenarios to validate the model.

The remainder of this paper is organized as follows. In section 2 we review related research in RE technology acceptance. Section 3 presents the technical background that is applied in the following parts of this paper. Section 4 presents details on the process for capturing the dynamics of early acceptance to support their modelling. Next, a BN model to infer end users' decisions regarding downloading the COVID-19 app is presented and evaluated in section 5. Threats to the validity of the results are presented in Section 6. Section 7 concludes the paper with a discussion of the current contributions and an outline of directions for future research.

## 2 RELATED WORK

Studies related to the Technology Acceptance Model (TAM) framework highlight the influence of soft requirements on end users' attitudes and behaviour towards system acceptance and continued use [26, 27, 48]. These factors may include motivations, individual user attributes and facilitating conditions belonging to the user context, and social influences (e.g. group conformance, identification, social contagion) [27, 48]. For example, a study [7] revealed that the use of fitness apps among Germans relied mainly on two reasons, (i) achieving fitness goals and (ii) improving enjoyment for physical activities, for instance, by sharing fitness results with social contacts [22]. Another relevant study [39] shows that the belief that "relevant referents expect users to use a system" causes the users to assume the referents' expectation, generating a sense of belonging in the users.

The role of soft requirements has also been recognised in RE. For example [44] presented a taxonomy of soft issues (user-oriented values, motivations and emotions) with implications in the requirements process for high-level goals. Social and political RE issues for recognising affective reactions among stakeholders were proposed by [34, 35], and requirements modelling using $i^{*}$ strategic dependency models was supported by Schwartz values [40] in combination with Holbrook's [19] consumer values to elaborate the implications of human values as soft goals for requirements in education applications [54].

In conclusion, while the importance of soft requirements has long been recognised in RE, advice and support to deal with such requirements are still fragmented and incomplete.

## 3 RESEARCH BASELINE

This section explains the main concepts that serve as the starting point for this work. Next, soft requirements are defined; then, we present our approach for modelling technology acceptance.

### 3.1 Soft requirements

We define soft requirements as follows:
Constructs that influence and contribute to the RE process of delivering system acceptance by users, which are neither user goals nor functional requirements.

Under this definition fall human values, social influences, emotions and traits of people, which have impact on the behaviour of users using software products.

Human values and their motivations can have an indirect influence on design and hence functional requirements [44]. In a broader sense, values are defined as guiding principles in people's lives that form an ordered system of priorities that characterize people as individuals [40, 41]. These priorities shape our responses to events, which in turn can result in actions, that may also give rise to feelings and emotions [41]. RE related studies [35, 44] have shown that emotions can influence users' behaviour, and reactions to systems.

Social influences are also relevant regarding the adoption and continuous use of software products. Several studies [7, 21, 25, 49] have shown that social influences significantly impact users' appraisal of a technology's usefulness. Users' cognition of significant others' expectation, also contributes to the users's decision to continue using an app [7]. The impact of social influences can also obey specific cultural-value characteristics of society. For example, descriptive social norms (referring to what most people usually do [11]) appears to have more substantial effects of continuing using an app among users from more collectivistic societies (e.g. Asians) [7], than in highly individualistic users (Self-direction value [41]). In more collectivistic societies, which predominant conformity and tradition values [41], the need to conform is high [18, 53].

In this paper, we model relationships among soft requirements based on the probabilistic approach presented as follows.

### 3.2 Modelling technology acceptance: a BN-based approach

Most tasks in daily life require a person or an automated system to take the available information and reason about both what might be true in the world and how to act. Bayesian networks (BNs) allow reasoning under uncertainty. Uncertainty is due to lack of information or innate stochastic behaviour in the phenomena observed[23]. BNs offer:

- Specific support for modelling and reasoning under uncertainty.
- Flexibility to build models from data and/or experts' opinions.
- A tool to visualize the stochastic model of a domain problem.

- Capacity to evaluate probabilistic events that occurred (i.e. they are settled as evidence in one or more nodes) to predict the likelihood of several possible causes.

Specifically, we model relationships among soft requirements while representing and supporting the analysis of trade-offs between end users’ Motivations and Barriers [9] (See Fig. 1), which would influence their disposition to download / not download the COVID-19 app.

Details in the BN model implementation. A BN represents a joint probability distribution over a set of observed variables [17]. It contains a qualitative part denoting the interdependence of the variables and a quantitative part specifying the conditional probabilities of the variables.

A BN uses a directed acyclic graph (G). The nodes of G are variables $X_{1}, \ldots, X_{n}$ belonging to a particular dataset of interest. The edges of G represent a linear interdependence among the variables. In this work, the dataset of interest and the edges of G are represented by soft requirements and their relationships identified by following the methodology presented in section 4.1. Therefore, graph $G$ can be said to encode the interdependence relationships of the variables in the domain under investigation [5].

We can also say that a distribution P over a Graph G can be expressed as the following joint probability distribution:

$$
P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid P a_{X_{i}}^{G}\right)
$$

$P a_{X_{i}}^{G}$ denotes the parents of $X_{i}$ in G. The individual elements $P\left(X_{i} \mid P a_{X_{i}}^{G}\right)$ are called conditional probability distributions (CPDs). As a general approach, first, we determine the structure G of the network representing the inter-dependencies between soft requirements (i.e the variables $X_{1}, \ldots, X_{n}$ ), which are organised in two main branches: Motivations and Barriers as depicted in Fig. 1. Then the CPDs are estimated using the dependencies identified in G.
![img-0.jpeg](img-0.jpeg)

Figure 1: BN model for decisions to select the NHS COVID-19 Test and Trace app

## 4 SOFTWARE PRODUCT ACCEPTANCE

We guided our study with the following research question:

RQ: Can a predictive model help requirements engineers predict what soft requirements are needed to support when making a software system?

### 4.1 Methodology

To achieve our aim and answer our research question, we present the following process, which was applied in section 5.2:
4.1.1 Step 1: Initial set of soft requirements. First, we surveyed the literature to discover an initial set of soft requirements for the adoption of the COVID-19 app. The selection was based on (i) previous studies about general soft issues in RE and technology acceptance [35, 43, 44] and (ii) experience reports about the COVID19 app and other similar track and trace apps [2, 6, 45].
4.1.2 Step 2: Interviews. The purpose of the interviews was twofold: to validate the identified soft requirements in the previous step and act as a pilot of the initial survey. Specifically, the interviews explored respondents' rationale for their value choices related to their attitudes towards their choices and experience with the COVID-19 app. Qualitative insights which supported/rejected the initial set of soft requirements were collected in this step. Thirteen participants were involved ( 8 male, 5 female). The participants rated values [40] on a scale from not important to extremely important in order to evaluate qualitative and quantitative results. Interviews lasted approximately 40 minutes, and were organized into sections: (i) importance and interpretation of value categories and importance in lifestyle decisions; (ii) importance of values and other factors that affect the choice of software products in general; and (iii) specific context of COVID-19 app choice and experience. Participants were also encouraged to volunteer their own perceptions on other non-value influences on choice of software products, as well as their rationale for downloading decisions for the COVID-19 app.
4.1.3 Step 3: Initial survey. This step quantified the qualitative insights collected from the previous step about the importance of soft requirements through a questionnaire, where people were asked to rank them. The survey involved questions related to (a) values with the prompts "How important is each value in guiding decisions in your life?," (b) the same values with a prompt eliciting importance ratings in relation to acceptance of IT-Products in general, and (c) the same values in relation to downloading the COVID-19 app. Additional questions elicited other potential influences on end users' decisions like price and brand (trust), compatibility, external influences on choice (social media, reviews, etc.) or COVID fear for the case of the COVID-19 app. The initial survey was completed by 20 respondents. The respondents were postgraduate and research staff at Aston University and the University of Manchester, 9 males, 11 females, age range 21 to over 65 with $80 \%$ of respondents $<50$ years old. The survey is illustrated as an Appendix in the electronic supplementary materials [1].

4.1.4 Step 4: Implementation of the model. The qualitative and quantitative insights collected were used to configure the COVID-19 BN model. We built a probabilistic predictive model based on Bayesian networks (BNs).
4.1.5 Step 5: Model validation. A larger-scale survey was conducted to validate the COVID-19 model against the survey results. 208 respondents completed this survey. The respondents were members of the organization U3A (University of the Third Age), also participated Aston University and the University of Manchester. The total of participants were 68 males, 139 females, 1 non-binary, age range 18 to over 80 with $80 \%$ of respondents $<70$ years old.

## 5 ACCEPTANCE FOR NHS COVID-19 TEST \& TRACE APP: DOWNLOAD DECISION

This section presents details on the identification, modelling and validation of soft requirements for early acceptance of the COVID19 app.

### 5.1 NHS COVID-19 Test and Trace app

The COVID-19 app [31] (See Fig. 2) tracks the proximity of registered users and alerts each user if they have been in contact with another infected person. If a positive alert is received the user has to self isolate for 10 days as well as reporting their infection status. Other features include information about symptoms, test results and checking COVID-19 risk by postcode area and venue. After an initial pilot trial in May 2020, its second version was made available in September 2020 [51], [10]. The app was selected because experience was likely to have been vivid for most users, and the download decision implicated emotions and value issues such as trust in government and security concerns [2, 6, 45].
![img-1.jpeg](img-1.jpeg)

Figure 2: NHS COVID-19 Test and Trace app

### 5.2 COVID-19 app - soft requirements elicitation and model implementation

Next, we apply the methodology presented in section 4.1.
5.2.1 Step 1 - Initial set of soft requirements. Trust and brand reputation, Privacy and Security were selected as our initial set of soft requirements as they represent well known RE issues associated to technology acceptance [43, 44, 50]. The selection was reinforced by insights collected from studies related to the COVID-19 app and other Track and Trace apps [2, 6, 45], where privacy, security and anonymity of the collected data were highlighted as relevant.

Other issues such as concerns about reliability and effectiveness, excessive battery consumption, compatibility of OS versions and consent withdrawal (the ability of a user to stop participating in data sharing) were also reported [2, 6, 45]. As we further investigate on these issues, we formulated concrete questions in the interviews and surveys about functions usefulness, apps compatibility, and other matters.

We also decided to pay attention to emotions such as fears, and conflicts experienced by individuals, which have been identified in previous studies as relevant for RE and software acceptance [34, 35]. Specific questions regarding COVID fear and Trust in the NHS (National Health Service) and HMG (Her Majesty's Government) were reflected in our surveys.
5.2.2 Step 2 - Interviews. We conducted several interviews to validate the initial set of soft requirements. All interviewees were aware of the app and its intended role in tracking and tracing infection. Examples of qualitative insights collected from this step are presented as follows.

Five interviewees (I1, I2, I6, I8 \& I12), had downloaded the COVID19 app. They were motivated by social responsibility, the utility of the app for gaining access to venues and its potential to reduce the risk of infection. For example, I1 explained "I think I don't have anything to lose if I use it, and it is important that most of us use the app to have a real positive effect at controlling COVID-19". I8 valued the access to venues supported by the app: "at the beginning if you didn't have the App, you were not allowed to enter places, to get into places, right? So, like that's why I did it from the beginning".

Non downloaders (I3, I4, I5, I7, I9, I10, I11 \& I13) were motivated by privacy/security concerns (7) which were linked to mistrust in the Government (6), no perceived need for the app (8), and poor accuracy (4) that may lead to false alerts. For example, I3 stated "despite the government saying that data is treated as anonymous, I don't believe the government! I think how you can trust in a completely incompetent government?". Non downloaders also had little perceived need for the app because of their limited potential for exposure to the virus. In this regard I5 highlighted "I .... stay indoors so I don't see the point to use the app".

From quantitative information collected at this step, we produced the following updated list of soft requirements: Social Responsibility, app Utility, COVID fear, Privacy and Security concerns and Trust and Brand reputation. Quantification of their importance is studied the next step.
5.2.3 Step 3 - Initial survey. Several findings were collected regarding the COVID-19 app. They are presented as follows.

General findings. Five values and seven other soft requirements were more important with means $>3$ (See Table 1) although the three more detailed security questions can be grouped as one question. COVID fear was the key motivation (mean 3.95, 1st), followed by helpfulness ${ }^{1}$ and responsibility values ( $2 \gg$ ) which reflected users' desire to benefit society (altruistic motivation) as well as the app being helpful in their own lives. Security questions were all important (means $3.75,3.70$ ), and rated slightly higher than the security value (mean 3.45). Trust in the NHS (mean 3.40) was more important than Functions useful (mean 2.50) and social order (mean 3.30), the latter reflecting end-users motivation for society-wide benefits, as did knowledge (mean 3.05) which was interpreted as generating knowledge for infection control measures and research.

Table 1: Initial survey ratings - COVID-19 app ranked means. Soft requirements related to Values are highlighted in Bold


Downloaders / non-downloaders findings. The same soft requirements were important for both downloader users and non-downloaders although their priorities in the rank order differed. For downloaders COVID fear dominated (mean 4.08, 1st), with the desire to help with research and managing the spread of COVID through helpfulness and social responsibility values ( $2 \gg$ ), while concerns over specific security issues were less important (6th, 7th), although security as a value was more important (mean 3.54, 4th). Rating of specific security concerns may reflect the downloaders' favourable evaluation of privacy data management in the COVID-19 app, although security overall was still an important concern. Non-downloaders were more concerned with specific data security issues, and had lower trust in the NHS.

As a result of this step, a final list of soft requirements was selected: External Influences, Fear of Infection, Usefulness, Altruism,

[^0]Table 2: Soft requirements selected for the updated hypothesis (Selection justification based on the interviews and the initial survey)


NHS Trust, UKGov Trust and Security. Their selection was based on the combination of quantitative and qualitative evidence as is depicted in Table 2. This set of soft requirements will constitute the inputs of the BN model.
5.2.4 Step 4 - Implementation of the model. The structure of the BN shown in Fig. 1 models the initial choice to download / nondownload the COVID-19 app.

The Download node (top-parent), represents the probability of downloading the COVID-19 app. Motivations, represent the positive influences on the download decision, whilst Barriers represent negative influences. The download decision is a trade-off between motivations and barriers [43], a specialization of the more general Cost-Benefit model. Next, we present details on its implementation.

Model Inputs. The leaf nodes of the model represent the BN inputs. They form the "what if" scenarios for the model testing. On the Motivations branch the model inputs are External Influences, Fear of Infection, Usefulness and Altruism. On the Barriers branch these are NHS Trust, UKGov Trust and Security. A scenario represents a set of observed values for the inputs of the model. In Fig. 1, with the exception of the root node, each other node can represent three possible observed values: High, Medium, and Low. A specific set of observed values, i.e. a scenario, will be the input for the BN model to predict, using Bayesian inference, the current probabilities of the Download disposition (Yes/No) and the current levels of Motivations and Barriers (High, Medium or Low). Examples of scenarios and their impact on the users' Download disposition can be observed in Table 3.

Prior probabilities of the model. For the COVID-19 model we had contrasting means, rankings and qualitative evidence for both downloader and non-downloader respondents collected from the previous steps. This enabled more informed decisions in setting the Conditional Probability Distributions CPDs according to the overall value/other soft requirement rank order and the Download Yes/No differences. For example, variables with higher Yes/No differences (e.g. Altruism, Security) were assigned more skewed priors in the


[^0]:    ${ }^{1}$ Helpfulness value definition: " It is important to help people and care for their wellbeing". The complete set of values definitions used in our surveys can be consulted in [1].

outcome distribution (High/Medium/Low terciles); while lower Yes/No differences (e.g. Usefulness) were assigned less skewed priors.
5.2.5 Step 5 - Model validation. The BN model (see Fig. 1) predicts the probability of users' download disposition of the COVID-19 app, based on trade-offs among the 7 input variables. Predictions of the model will be compared against data collected from the larger-scale survey presented in section 4.1 (Step 5). Two different analysis are presented as follows.

Sensitivity analysis. Based on Bayes' theory, input evidence values are propagated through the network, updating the values of other nodes [42]. The model performs sensitivity analysis testing of all possible settings of its input variables. The outputs which agree with a pre set threshold are counted as "survivor" scenarios [42]. The BN model is used to exhaustively test all the possible variations of input variables and provides output showing which scenarios meet the predefined thresholds. In the current implementation, the input variables have three states (High, Medium and Low), that is, $3^{7}$ or 2187 scenarios have been tested. Two thresholds were defined for the model analysis: P(Download==Yes) $>=70 \%$ and $\mathrm{P}($ Download $==\mathbf{N o})>=70 \%$. The survivor scenarios for these thresholds are summarized in Table 3 and Table 4.

Table 3: COVID-19 model: Scenarios with highest impact on the probability P(Download==Yes) $>=70 \%$


Table 4: COVID-19 model: Scenarios with highest impact on the probability P(Download==No) $>=70 \%$


It is apparent that High observed values of Motivations and Low observed values of Barriers achieve output values equal or higher to the probability P(Download==Yes) $>=70 \%$ (See Table 3). Conversely,

Low observed values of Motivations and High observed values of Barriers achieve output values equal or higher to the probability $\mathrm{P}($ Download $==$ No $)>=70 \%$ (See Table 4).

Table 5: COVID-19 model: Frequency of observed values on scenarios with highest impact on P(Download==Yes) $>=70 \%$


47 scenarios produced an output which agreed to the probability $\mathrm{P}($ Download $==$ Yes $)>=70 \%$. Table 5 shows the frequencies of the observed values in these scenarios. In the Motivations branch, the most relevant input values were Altruism $==$ High (26 observed values) and Usefulness $==$ High (22 observed values). No differences were reported among the soft factors in the Barriers branch, only Low values were observed (47). These initial findings suggested that when concerns about Security and Trust (UKGov trust and NHS trust) are Low, Altruism is the most important factor (over Fear of Infection and Usefulness) to influence end users' attitude towards downloading the COVID-19 app.

Similar analysis was supported by data in Table 6 for the scenarios (365) that produced an output which agreed to the probability $\mathrm{P}($ Download $==$ No $)>=70 \%$. For this case, in the Motivations branch, the most relevant input values were Altruism $==$ Low (259 observed values) and Usefulness $==$ Low (246 observed values). In the Barriers branch, Security $==$ High (214 observed values) was the most relevant input value.

Table 6: COVID-19 model: Frequency of observed values on scenarios with highest impact on P(Download==No) $>=70 \%$


The sensitivity analysis presented above have shown which soft requirements are more important based on the predefined thresholds for the model analysis. Equivalent results were obtained for

the thresholds $\mathrm{P}($ Download $==$ Yes $)>=60 \%$ and $\mathrm{P}($ Download $==$ No) $>=60 \%$ (See Tables 7 and 8). In the following analysis, we evaluate the model behaviour under a more extreme implication: $100 \%$ either Download==Yes or Download==No.

Table 7: COVID-19 model: Frequency of observed values on scenarios with highest impact on $\mathbf{P ( D o w n l o a d}==\mathrm{Yes})>=\mathbf{6 0 \%}$


Table 8: COVID-19 model: Frequency of observed values on scenarios with highest impact on $\mathbf{P ( D o w n l o a d}==\mathrm{No})>=\mathbf{6 0 \%}$


Table 9: Model predictions: Motivations/Barriers trade-offs


Table 10: Final survey ratings - COVID-19 app ranked means.


(mean 6.04, 1st) and Helpfulness (mean 5.98, 2nd) were the key motivations, followed by Trust NHS (mean 5.92, 3rd). The Helpfulness and Responsibility values reflected users' desire to benefit society (altruistic motivation, social responsibility) which corresponds to the results in our sensitivity analysis: Altruism was the most important motivation to download the app (See Table 5). Altruism was also import in the back propagation analysis, a High probability value ( 0.65 ) was predicted among downloaders. The importance of Trust NHS highlighted by the survey corresponds to the Low probability value ( 0.18 ) predicted by the model about NHS concerns (See Table 9).

Compared to the initial survey, an important finding in the largerscale survey was that COVID fear stopped being important among non-downloaders or downloaders. Our results in the sensitive analysis agreed with this finding (See Table 5) but our results in the

back propagation analysis did not (See Table 9). We argue that the social-health contexts when our surveys were taken influenced this result. High levels of COVID infections and low levels of vaccinations [14, 16] characterized the context of our initial survey (February 2021). On the other hand, our larger-scale survey, which support the finding, was conducted under a context where the levels of COVID infections started decreasing due to the progress on the vaccination program, in special among senior and middle-aged people [15, 16] (April - June 2021). Youth were still in the queue at the progress of the vaccination program's priority groups [16, 30]. Because in our initial survey, $40 \%$ of the participants were youth between 23 and 30 years old, we further explored whether this demographic characteristic also influenced the initial prevalence of COVID fear as an important factor. We created subsamples from the larger-scale survey with the same size and age distributions as the initial survey. We observed that COVID fear started to appear again although surprisingly among non-downloaders. One example is show in Table 11 (mean 5.75, 2nd).

Table 11: Sample from final survey ratings - COVID-19 app ranked means.


From data collected among non-downloaders (See Table 10), Responsibility (mean 5.38, 1st) and Knowledge (mean 5.06, 2nd) were the most important soft requirements, followed by Helpfulness (mean 5.02, 3rd). They also had lower trust in the UKGov (mean 4.56, 16th) and the NHS (mean 4.88, 6th). Lower trust corresponds to results for UKGov Trust and NHS Trust shown as barriers to download the app in the sensitivity analysis (See Table 6). In the back propagation analysis we also obtained equivalent results. Higher concerns about UKGov Trust were predicted (Prob. 0.62) in comparison to NHS Trust concerns (Prob 0.21) as is shown in Table 9. The high ranks obtained in the survey for Responsibility and Helpfulness (1st and 3rd), corresponds to the probability ( 0.57 ) for Altruism predicted by the model, one of the highest among non-downloaders (See Table 9).

As an important finding among non-downloaders, and different from our model predictions, the survey results shown that Security (6th) was less important than other soft requirements such as Knowledge (2nd) (See Table 10). We argue that a more diverse sample in our larger-scale survey allowed the uncovering of this soft requirement which resulted more important than Security, as was highlighted in our initial survey. The insights collected in our validation process will contribute to the improvement of future versions of the model.

## 6 THREATS TO VALIDITY

In the following, the main threats that might impact on the validity of the results of this work are presented.

Internal validity. Internal validity refers to the degree of confidence that relationships being tested are not influenced by other factors and whether the evidence supports our claims [3, 52]. The initial convenience sample bias mainly towards a University population (interviews and initial survey) limited the scope of our study. We have mitigated this threat by supporting the modelling of the BNs with both, insights collected from our study (interviews and an initial survey) but also (i) studies on soft issues in RE [24, 26, 34, 35, 43, 44, 50], and (ii) specific studies for COVID-19 related apps [2, 6, 45]. We also performed a larger-scale survey with a more representative sample size ( 208 participants) and a more diverse demographic background. In future work, we will conduct a survey with a larger population using a purposeful sampling strategy to sample opinions from respondents with a wide range of socio-economic backgrounds and sample older and younger users from diverse ethnicities.

External validity. This aspect of validity is concerned with the extent that it is possible to generalize the findings [36]. Even though our results correspond to a specific case study, they provide initial insights into the importance of soft requirements for the acceptance of a software product and how they can potentially inform requirements engineers of designing features in a software system or higher level implications. For example, some soft requirements such as Security, may suggest more direct design concerns in a software application, while Altruism can represent socially oriented implications for systems [43].

The steps described in section 4.1 can be adapted and applied to other domain problems. As such, we have also contributed towards the generalization of our proposal by offering a methodology to implement the approach. Furthermore, the implementation technique (Bayesian Networks) used in this work can also be applied to other application domains where causal relationships among different soft requirements and their influence in software products acceptance need further study. It is part of our future work to carry out further implementations in actual settings of other domains.

## 7 DISCUSSION AND CONCLUSIONS

In this section, we highlight our contributions by answering the research question of this paper. The section presents concluding remarks and explores potential paths to develop the research further.

### 7.1 Discussion

In response to our research question about the feasibility of building a predictive model that help requirements engineers predict what soft requirements they need to support when making a software system, we found that our model, for the COVID-19 case study, was able to identify its most important soft requirements. The COVID-19 case is especially relevant as it represents an important global issue that has affected the whole humanity in different dimensions, and therefore offers a feasible "laboratory" to study soft requirements.

In the study, altruism was predicted as a key motivation to download and install the app. In our model, Altruism represented the Responsibility and Helpfulness values which reflected under the COVID-19 context, users' desire to benefit society. Altruism has socially-oriented implications for systems, for example, through sharing data issues.

Also, trust in the UK Government was identified by the COVID19 BN model as a concern among non-downloaders. This prediction agrees with our findings in the surveys and interviews. Nondownloaders cited the initial lack of transparency in the COVID-19 app, and poor trust in the app's provenance controlled by the UK Government. More specifically, poor trust in implementation not only of the app but also of the Track and Trace socio-technical system in which it was a key component. Trust in software systems can be manifested as non-functional requirements (NFRs) for predictability, transparency and visibility of system actions.

Although with less relevance, security was also predicted as a concern among non-downloaders. Security and Safety values have a clear design implication for privacy/security and applications involving sensitive data, as well as in the many computerized control systems with safety and reliability engineering requirements for hazard detection and error prevention.

### 7.2 Concluding remarks and future work

In this paper, we have presented a BN model for reasoning support and quantitative analysis of soft requirements that helps requirements engineers to identify what soft requirements they need to be focused when making a software system.

Using the model, we have been able to rank soft requirements that influence the adoption of the COVID-19 app. We have demonstrated how functional and non-functional characteristics can be complemented by the consideration of factors such as values and other soft requirements (e.g. brand trust, altruism) during productwise judgements. Furthermore, insights collected from the BN model can be potentially applied to design of product features. Our generic process for the implementation of the approach (See section 4.1) can be adapted to a variety of domains or product types for assessing how soft requirements and their trade-offs influence product acceptance.

So far, we have undertaken a two-stage validation study by testing the BN model with a range of scenarios. We simulated the possible combinations of the input variables of the models. This produced an extensive set of test data that allowed the evaluation of the validity of the model against a larger-scale survey. Specifically, the model's CPDs and the influences of soft requirements were analysed using (i) relevance analysis, a technique that ranks input parameters of the model based on their relevance to one of
the model's output parameters, e.g. Download disposition (Yes/No) in our BN, and (ii) back propagation analysis, to infer the relevance of soft requirements among specific end users groups (e.g. downloaders and non-downloaders).

Most of the initial assumptions about influences onto the end users' Download disposition were validated. However, specific findings collected from the survey data, will be used to further calibrate the current CPDs and the structure of the BN model. Uncovered soft requirements such as Knowledge and updated importance such as Security.

As part of our future work, we will use ML techniques to specify or update CPDs by automatically inferring influences from training data [42]. Influences by soft requirements do not stay constant over time. As such, we will use other probabilistic reasoning tools, such as Hidden Markov Models, Markov Decision Processes (MDPs)[37] and Partially Observable MDPs[32] to work further on modelling functional and non-functional characteristics together with soft requirements not just as a snapshot but overtime. Essentially, we would be looking into soft requirements as part of the evolution of requirements at runtime $[8,38]$ and support for the operationalization of human values in software[28].

## ACKNOWLEDGMENT

This work has been partially funded by the Leverhulme Trust Research Fellowship (Grant No. RF-2019-548/9) and the EPSRC Research Project Twenty20Insight (Grant No. EP/T017627/1).
