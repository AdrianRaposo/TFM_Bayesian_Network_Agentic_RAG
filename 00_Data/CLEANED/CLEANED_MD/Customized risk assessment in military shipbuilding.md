# Customized risk assessment in military shipbuilding 

José Crispim* ${ }^{\text {a,b }}$, Jorge Fernandes ${ }^{\text {a,c }}$, and Nazaré Rego ${ }^{\text {a,b }}$<br>* correspondence author: crispim@eeg.uminho.pt<br>${ }^{a}$ Escola de Economia e Gestão, Universidade do Minho, Campus de Gualtar, 4710-057 Braga, Portugal<br>${ }^{b}$ INESC TEC, Campus da FEUP, Rua Dr. Roberto Frias, 4200-465 Porto, Portugal<br>${ }^{c}$ Brazilian Navy, COrM, Esplanada dos Ministérios, Brasília. 70.055-900, Brazil

The final version of this paper is available at:
https://doi.org/10.1016/j.ress.2020.106809
© 2020. This manuscript version is made available under the CC-BY-NC-ND 4.0 license https://creativecommons.org/licenses/by-nc-nd/4.0/

# Customized risk assessment in military shipbuilding 


#### Abstract

This paper describes a customized risk assessment framework to be applied in military shipbuilding projects. The framework incorporates the Delphi method with visual diagrams, Bayesian Networks (BN) and the expression of expert opinions through linguistic variables. Noisy-OR and Leak Canonical models are used to determine the conditional probabilities of the BN model. The approach can easily be adapted for other shipbuilding construction projects. The visual diagrams that support the Delphi questionnaire favor the comprehensive visualization of the interdependencies between risks, causes, risks and causes, and risks and effects. The applicability of the framework is illustrated through the assessment of risk of two real military shipbuilding projects. This assessment includes a sensitivity analysis that is useful to prioritize mitigation actions. In the two cases studies, the risks with higher probability of occurrence were failures or errors in production, of the contracted, in the requirements, and in planning. The results of the sensitivity analysis showed that a set of mitigation actions directed at relatively easily controllable causes would have achieved important reductions in risk probabilities.


## Highlights:

- The proposed framework for risk assessment is customizable.
- The visual diagrams that support Delphi ease the design of the risk network.
- The use of Bayesian Network provides quantitative measures of risk.
- Leaky Noisy-OR is used to decrease the effort of expert opinion elicitation.
- The application to two real projects shows the suitability of the framework.

Keywords: Project management; Shipbuilding projects; Risk network model; Delphi; Bayesian network

## 1. Introduction

Military shipbuilding projects in private shipyards in Brazil have repeatedly been affected by problems related to delivery delays and increased costs. The literature has shown that insufficient risk management has contributed to project delays and cost overruns [1], therefore, the lack of a formal risk management plan for military shipbuilding projects may have contributed to such occurrences.

It is expected that several ships for the Brazilian Navy are constructed in domestic shipyards in the coming years, which increases the need for the design and improvement of processes to manage the risks of related projects. Kwak and Smith [1] identified a lack of studies about risk management practices for defense projects. This research confirms that the situation persists since only two articles addressing risk issues in military shipbuilding projects were found [2, 3]. This study contributes to narrow this gap by proposing a customized risk assessment framework that comprises the main risks, their cause and effect relations, and a network that shows the interactions between these variables in a military shipbuilding context.

Risk assessment measures risks and identifies the effects of hazardous events on a project or organization and integrates three main processes: risk identification, risk analysis, and risk evaluation [4]. Risk identification is the most important element of the whole risk management process [5].

However, it is normally difficult to identify risks because of the limited knowledge about factors that can cause failures and the high interaction between those factors. In military contexts, the difficulty increases because risk information is usually scarce and restricted. Databases can function as bodies of knowledge in organizations where information about risks and subsequent actions from previous projects can be continuously recorded to be reused when new projects are developed. However, in this work, their use is limited for the reasons pointed out in the literature: 1) generally, the knowledge captured about past projects is organized around single facts, without information about the causes, conditions (risk factors), and possible interactions related to the failure events [6]; and 2) military shipbuilding projects are very dependent on technology and, consequently, their environment and associated risks are continuously evolving [7]. Moreover, in the case of the Navy of Brazil, databases that comprehensively integrate risk related knowledge did not exist at the time of the study and other instruments had to be used to collect information about risks. Expert opinion interviews are commonly used to collect this type of information [see e.g., 4, 8].

In the military arena, knowing the hierarchy of a participant may inhibit the opinion of others, especially those from lower ranks. Therefore, in this study, it was essential to preserve the anonymity of the experts since the early stages of the research. The Delphi method is a formal communication technique that guarantees the required anonymity and confidentiality.

Risk as a numerical quantity is useful for risk prevention and for prioritizing mitigation measures, therefore risk assessment should be considered as a tool for rational decision making [9]. In line with this idea, our approach to risk assessment is quantitative although limited by the data availability conditions of the organization.

The complexity of defense projects results in a network of interdependent risks: a risk in an "upstream" activity can trigger several risks "downstream", and a risk in a "downstream" activity may emerge from the combined occurrence of several risks located "upstream" [10]. The questionnaire developed is supported by visual diagrams because it was impossible to show the interdependencies between risks only through word questions. This approach eases the understanding of interrelationships by the experts and the customization of the risk network structure for specific projects. Bayesian Networks (BN) are used as a method of representation that is closer to the complex reality and the dynamics of risks in different types of projects [11]. They are suitable for knowledge representation and reasoning [12] and to deal with uncertain information in complex environments [13].

To show the functionality of the framework, a risk evaluation based on BN for two shipbuilding projects of the Navy of Brazil was performed. The HUGIN Expert software was used to build and run the BN. This software facilitates visual BN model formulation, reasoning, and decision making. The determination of the probabilities of occurrence of the identified risk events can help the decision maker develop mitigation actions to decrease those probabilities and hence the correspondent risks (e.g., delivery delays or budget slippage).

# 2. Literature review 

There is limited research about risk assessment in shipbuilding and even less in military shipbuilding projects. Most of the studies assess risks only qualitatively.

Queiroz [14] reviewed the literature and used the risks identified as a starting point for brainstorming sessions in order to obtain list of risks suitable for Brazilian shipbuilding. Pires Jr. et al. [15] and Ferreira et al. [16] used brainstorming and Delphi to develop risk matrixes to assess risk in Brazilian shipyards. Kochetkov and Aliev [17] also created a risk matrix (through the analysis of statistical data) to compare the probability of undesirable results and the extent of possible damages in the shipbuilding and ship repair industry in Latvia. Jacinto and Silva [18] use the bow-tie model for risk identification and a classical risk-matrix approach to assess risk of a Portuguese shipyard qualitatively. Christiansen and Thrane [2] used interviews and risk report analysis to study how managers translate emerging risks into reported risks in the acquisition of military ships. Only Lee et al. [19], Basuki et al. [20], Fragiadakis et al. [21], Iwańkowicz and Rosochacki [22], and Sokri and Ghanmi [3] applied quantitative approaches in risk assessment of military shipbuilding. Lee et al. [19] developed a Bayesian Belief Network based on information collected through a survey to 250 experts of the eleven major Korean shipbuilding companies. Basuki et al. [20] developed a risk assessment method using probabilistic value at risk in each production subprocess (design, material procurement, production) to control the production of fast patrol vessels in Indonesia. Fragiadakis et al. [21] applied an adaptive neuro-fuzzy inference system to predict the effect of working conditions on occupational injury in Greek ship repair yards. Iwańkowicz and Rosochacki [22] used clustering and simulation and the accidents database of a Polish shipyard to predict shipbuilding risks related to the health and life of workers. Sokri and Ghanmi [3] developed a hybrid method that combines a learning curve model with stochastic simulation to estimate the probability distribution of the project labor cost.

A systematic literature review to identify possible risks and their causes, and risk assessment methods in related contexts (shipbuilding, defense, construction, and development and integration of technological systems) was carried out by searching referential databases, namely, EBESCO, Scopus, and Google Scholar, using combinations of appropriate search words: [(shipbuilding OR construction) AND risk], [(systems development OR systems integration) AND risk management], [(defense OR defence OR military) AND project AND risk management], and (risk assessment AND project management). The area of integration of technological systems was included because military shipbuilding projects have a strong technological component. Except for shipbuilding, an area where a small number of articles was identified, the search was limited to the last eight years (2010 and afterwards). Additionally, we considered risk related documents collected from the websites of the Departments of Defense of Australia and the United Kingdom.

As a result of skimming through the documents pre-identified, 78 were selected due to their relevance for the study (Table 1), resulting in the identification of 89 risks, causes and effects, and 18 different assessment techniques and methods (normally combined in hybrid approaches). For risk identification, the most used source of information has been the opinion of experts, collected by interviews, questionnaires, brainstorming or Delphi. Historical data was used in six works, in conjunction with expert opinion in two of them. This evidence shows that databases with information about previous projects are scarce. Project managers are usually the keepers of information about past experiences. This is the case in a military context since information may be classified as confidential.

In terms of analysis and evaluation methods, traditional techniques (i.e., matrix of probability and impact or probability index, impact index for time, impact index for cost, and weighted risk factor) are still being used because of their simplicity, although they have often been criticized. Thomas et al. [23] argue that, despite being intuitive and simple, there is no empirical evidence showing that the risk matrix actually improves risk management or the outcomes of decision making. Failure Mode and Effect Analysis has also been criticized. For example, Zhang and Chu [24] claim that different combinations of occurrence, severity and detection may result in the same risk priority value, while the hidden risk implications of these sets may be totally different. Fuzzy logic, combined with other techniques (for example, AHP or TOPSIS) has been the most used evaluation method, since it is tolerant to imprecision when modelling uncertainty. AHP has been the second most used technique, but it can be time consuming and tedious if the decision hierarchy has many levels. BN, alone or combined with other methods, are a very flexible method that can be used to [25]: 1) model uncertainties and provide probabilistic estimates; 2) combine historical data with specialized experience or prior knowledge; 3) show visual cause-effect relationships (which provide explicit knowledge for risk analysis and planning); 4) perform "what-if" analysis in order to explore the effect of changes made in specific nodes of the network on other nodes; and 5) develop sensitivity analysis, diagnosis, prediction, classification and causal reasoning.

BN depend on databases or experts' elicitation for model construction and parameterization. When databases exist, large number of data points are available; if not, the large number of conditional probability entries put a great workload on the experts and pose challenges to the quality or consistency of the elicited result [26]. Therefore, as Pourreza et al. [27] recognize, new methods for experts' knowledge elicitation should be developed and applied to improve the model validity. Canonical models (like OR, AND, Noisy-OR and Leaky Noisy-OR) can be used to overcome this situation. Although a canonical model reduces significantly the work of the experts and contributes to improve consistency during the BN model parameterization process [26], in a military context, only Louvieris et al. [28] used this kind of approach (Noisy-OR). In other areas, the use of BN with Noisy-OR has been more common, e.g., in the energy sector [e.g., 27], railway infrastructures [e.g., 29], new product development [e.g., 30], and Human Reliability Analysis [e.g., 31].

Table 1 - Risk assessment methods



# 3. Proposed framework 

The risk assessment framework proposed incorporates several methods (explained in detail in the next subsections). Figure 1 displays its main steps: 1) a literature review to identify (and contextually adapt) an initial list of risks, causes and related effects; 2) the selection of the two panels of experts: the first to adapt the framework to the context of problem under analysis, and the second to operationalize and control the application of the framework; 3) the application of the Delphi method (with the participation of the first panel) to create a network of risk events; 4) the assessment of the risks, i.e., assigning and confirming risk events probabilities (by the second panel); and 5) simulation and ranking of mitigation actions (also with the participation of the second panel).

### 3.1. Delphi method

The Delphi method is a formal communication technique designed to obtain the maximum number of unbiased opinions from a panel of experts [51]. The iterative nature of the procedure generates new information in each round, allowing the appraisers to modify their assessments and to project them beyond their own subjective opinions [95]. Typically, the interaction between the Delphi administrator and the members of the panel occurs through questionnaires. Our questionnaire is based on interrelationship diagrams representing causes, risks and effects identified in the literature. These diagrams facilitate: a) the construction of the network (the experts can easily add/delete nodes and edges), and b) the expression of the level of importance of each risk event and/or of the relationships between risks.

The application of the Delphi method involves three critical steps: i) selection of the number and profile of the participants; ii) method to obtain consensus; iii) number of rounds.

![img-0.jpeg](img-0.jpeg)

Fig. 1 - Risk assessment framework

# Number and profile of the participants 

The ideal size of a Delphi panel does not depend on statistical power but rather on the group dynamics for achieving consensus; thus, 10 to 20 experts have been recommended [96]. This study had the participation of 17 experts from the Navy of Brazil.

The profile of the experts is directly related to the validity of the study [79]. In project risk contexts, a minimum experience time or the participation in a minimum number of projects have frequently been considered as selection criteria [see e.g., 43, 48, 53, 65, 68, 75, 79, 90, 97]. At the time of their participation in this study, the experts had a minimum of five years of experience in, at least, one of the following functions in a military shipbuilding context: shipbuilding supervision, member of management team, naval systems expert, project manager or advisor. Furthermore, they had participated in, at least, three military shipbuilding projects. The profile of the participants selected (first panel) is detailed in Table 2.

Table 2 - Profile of the respondents (first panel)


# Measurement of consensus and number of rounds 

There is still no unanimous way to measure consensus in Delphi studies [98]. The following have been used for this purpose: the percentage of agreement [e.g., 40, 51], the stability of the responses in two successive rounds [e.g., 65, 99], and associations of central tendency and dispersion measures [e.g., 69, 100]. Consensus criteria, such as the median and interquartile range (IQR), have been widely used in other fields (e.g., corporate governance and information technology) [101, 102]. Another widely recognized metric is Kendall's coefficient of concordance (W) [96], an inferential statistical measure that can be used to estimate agreement between raters [98]. This metric determines if any consensus has been achieved, if it is increasing and its relative force [103]. A $W$ between 0.5 and 0.7 indicates moderate agreement, and a $W$ higher or equal 0.7 is a signal of strong agreement. Since this metric is only suitable for ordinal variables, the extension of the kappa method, Fleiss' kappa ( $k$ ) [104], should be used for nominal variables. Values of $k$ less than 0.4 mean weak agreement, between 0.41 and 0.6 are considered moderate, between 0.6 and 0.8 mean substantial agreement, and higher than 0.8 mean almost perfect agreement [105]. In this work, we used a combination of metrics with the objective of obtaining more robust results. For the set of ordinal variables: 1) at least a moderate $W$ should be found; 2) a low dispersion, represented by an IQR $\leqslant 1$, should be obtained for each item assessed. Regarding the set of nominal variables, at least a moderate $k$ index should be found. Without the fulfillment of these conditions, the process would end if there was no change of stances between two successive rounds. Frequently, three iterations are enough to collect the necessary information and reach a satisfactory level of consensus [40].

In this work, the first round had a total duration of 25 days and a response rate of $100 \%$. The results obtained by the end of this round suggested a weak consensus ( $W=0.178$ and $k=0.167, \mathrm{p}<0.005$ ). In order to check the consensus between respondents with similar experience, the participants were divided according to their professional function (project managers, members of project management teams, naval systems experts, and consultancy/ supervision). The $W$ obtained showed weak consensus for all groups ( $W<0.5$ ). In terms of measures of location and dispersion of each assessed item, we obtained an IQR $<1$, and an answer convergence of over $50 \%$ for all nominal variables.

Possible reasons for the low level of consensus are: 1) lack of access to available information (8 of the 17 respondents did not visit the site created to explain the meaning of each risk, cause and effect); 2) the process of grouping and summarizing the risks and their causes (obtained from the literature) may have reduced the detail of the information, making it too broad and difficult to assess, and thus allowing for different interpretations; 3) the experts may have different perceptions about what is the success of a project. After the first round, some adjustments were made: clarification of the questions, graphical representation of the responses, inclusion of comments.

The response rate of the second round was $94 \%$. The global agreement of the experts' assessment was above 0.7 (Table 3). The results indicate that the adjustments made may have contributed to a significant change in the opinions from the first to the second round.

Table 3 - Levels of agreement on the assessed sets


$W=$ Kendall's Coefficient of Concordance.
Two additional tests were performed: the Kruskal-Wallis nonparametric test, to test possible differences between the opinions of each group, and the Spearman nonparametric test, to assess the stability between rounds. Differences were observed in the distribution of responses for only two variables, "Planning failures may occur due to acts in bad faith (sabotage) by one of the stakeholders" and "Requirement errors may occur due to lack of financial capacity". Divergent opinions presented by some participants, possibly related to differences in professional experience, were not enough to compromise the global consensus. The Spearman test showed no statistically significant correlations between the variables assessed.

Due to the strong consensus at the end of the second round, it was decided not to hold a third one, given the low benefit (over cost) that it could provide.

One of the main limitations of the Delphi method, discussed by Rowe and Wright [106], is the possibility that "consensus" is only apparent, since respondents may change their estimates in order to be in accordance with the group, without actually changing their opinions about the topic under analysis.

In order to understand how the group worked to reach consensus, at the end of the questionnaire, the experts were asked to indicate the two factors that influenced their assessment the most. The options presented to them were:
a) The description and examples of the risks and causes enabled a better understanding about the questions;
b) The comments from experts helped to think about some questions;
c) The general trend (percentage) of the responses to the first questionnaire favored a better reasoning about each problem;
d) I gave an opinion on a particular item only because most of the experts did, and it does not represent my personal judgment on the questions; and
e) Other.

The responses to this question suggest that the convergence of opinions found in the second round did not result from compliance with other panel members, but rather from a genuine change of opinions. Respectively, $81.3 \%$ and $93.8 \%$ of the respondents chose options a) and c). None of the respondents chose option d).

# Data collection 

Data was collected through an online questionnaire based on interrelationships diagrams (Figure 2 shows the example of question 4) and structured around the following questions ${ }^{1}$ :

1. Can the success (viewed through schedule delays and cost overruns) of a military ship construction project be affected by the risks represented in the figure? Would you like to suggest other risk(s)?
2. For each risk, how often do the causes of risk represented in the figure occur in the construction of a military ship? Would you like to suggest other cause(s)?
3. Do you agree that the interactions between risks represented in the figure could occur in the construction of a military ship? Would you like to add/delete any interaction?
4. Do you agree that the interactions between causes, and between causes and risks represented in the figure could occur in the construction of a military ship? Would you like to add/delete any interaction?

The assessment of the questions was carried out using a 5-point Likert scale. For questions 1 and 2, 1 corresponded to "Never", 2 to "Seldom", 3 to "Sometimes", 4 to "Often", and 5 to "Always". For

[^0]
[^0]:    ${ }^{1}$ The whole questionnaire (in Portuguese) is available at http://goo.gl/forms/0Ykuq11mZZe54WnK2

questions 3 and 4,1 corresponded to "I strongly disagree", 2 to "I disagree", 3 to "Undecided", 4 to "I agree", and 5 to "I strongly agree".

At the end of each section/question, fields for comments or additional contributions by the respondents were included. The sequential construction interactively helps the decision maker creating a network of interconnected causes and risks.
![img-1.jpeg](img-1.jpeg)

Fig. 2 - Interrelationship diagram showing the causes of a given risk

# 3.2. Bayesian networks $(B N)$ 

BN are directed acyclic graphs with nodes that represent random variables and edges that represent their conditional dependencies. Each node has a finite set of mutually exclusive states and is associated with a conditional probability distribution that gives the probability of each state for each combination of values of its parents. The parent node directly affects the child node. The joint probability distribution of a BN over its set of variables $X_{i} \in X=\left\{X_{1}, \ldots X n\right\}$ is given by the product of all the conditional probability distributions [107]:

$$
P(X)=\prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

where $p a\left(X_{i}\right)$ are the parent nodes of $X_{i}$ in the network. In this work, we considered that each node of the network has two states: "true" and "false". The "true" state indicates a state of positive affirmation of cause due to that particular variable. A Conditional Probability Table is associated with each node to denote the causal influence between variables represented by the edges. BN can be used to support visible and repeatable decision-making, which is an important advantage. They have, however, been criticized for subjectivity in the construction of the influence diagrams and in the determination of the conditional probabilities. In general, a BN models the belief of its constructor [10]. Another limitation emerges when a child node has more than two parents, since, for every event, the number of possible

combinations grows exponentially [7]. For example, the risk "failures of production" is a child node with 16 parents (causes) which leads to a total of $2^{16}=65.536$ possible combinations. This makes elicitation from experts an impossible task. One way to reduce the complexity of the elicitation of numerical probabilities is to rely on canonical models that build probability distributions from a small number of parameters. Among the existing canonical models, the best known are Noisy-AND and Noisy$O R[108]$, the model used in this study:

$$
\text { Noisy } O R: \mathrm{P}\left(Y / X_{i}, X_{j}\right)=1-\left(1-P\left(Y / X_{i}\right)\right) *\left(1-P\left(\left(Y / X_{j}\right)\right)\right.
$$

We also used the "leak probability" [109] to incorporate an additional edge corresponding to the probability that an effect occurs even when all the causes listed in the model are not active. Lemmer and Gossink [110] incorporated the idea of "leak probability" assuming the "leak" to be independent of the other causes of the model. This allows the modeler to focus on significant causes and to group insignificant, incidental or unimportant causes in a single factor, thus simplifying large networks. In practice, we considered an additional casual interaction for each child node. The probability of occurrence of a $Y$ effect, given a cause $X$, is calculated according to the following expression:

$$
\text { Noisy } O R / \text { leak: } \mathrm{P}(Y / X)=1-(1-P(\text { leak })) *\left(1-P^{R}(X)\right)
$$

where $P($ leak $)$ represents the probability of occurrence of $Y$ in the absence of other causes listed in the model and $P^{R}(X)$ is the probability estimated by the Noisy $O R$.

We used the HUGIN Expert software ${ }^{2}$ to build a BN for conducting risk assessments of shipbuilding projects because it eases BN model formulation, reasoning, and decision making under uncertain conditions. The software has been used for risk analysis in different areas [e.g., 13, 111, 112].

A BN model will be valid if it is representative of reality. The following steps were taken to assure the internal validity of the model: 1) posterior probability distributions were confirmed through redundant computation for several nodes; 2) the final model structure, the number of variables, their states, and casual relationships were confirmed by the first panel of experts in the successive Delphi rounds; 3) the second panel of experts confirmed that the results from the application of the model to two real projects were consistent with the reality of those projects; and 4) a sensitivity (what-if) analysis was then performed and validated by the same panel of experts. In terms of external validation, the experts (second panel) confirmed that the proposed model meets the users' requirements.

# 3.3. Linguistic variables 

When historical data is unavailable, it is more realistic and intuitive to use linguistic terms than numerical values to assess risk events. Fuzzy set theory, initially proposed by Zadeh [113], has been

[^0]
[^0]:    ${ }^{2}$ Expert A/S, Hugin Litle ${ }^{2} 8.3$. Academic version [Computer Software]. Retrieved from: http://www.hugin.com/ in March 2016

extensively applied to reflect ambiguities in human judgment. The fuzzy set concept is a convenient way of keeping track of imprecise, vague, and uncertain informative statements [114].

A fuzzy number (FN) is a way of representing uncertain or fuzzy information. The most widely used format of fuzzy numbers is the Triangular Fuzzy Number. The linguistic term set and their membership functions are defined in Table 4.

Table 4 - Linguist terms and experts weight importance


To aggregate the information, we weighted each opinion expert differently depending on two factors: 1) his/hers experience (in years) in functions related to shipbuilding projects, and 2) the number of projects in which he/she participated. This indicator was inspired by the work of Zhang et al. [13].

For determining the fuzzy probability of occurrence of risk events the following formula was used:

Weighted $F N=E_{1}$ opinion $* \frac{E_{1} \text { score }}{E_{1} \text { score }+\cdots+E_{n} \text { score }}+\cdots+E_{n}$ opinion $* \frac{E_{n} \text { score }}{E_{1} \text { score }+\cdots+E_{n} \text { score }}$

In the defuzzification procedure, we used the $\alpha$-weighted method developed by Detyniecki and Yager [115]. To obtain the final probabilities of occurrence of project risks, we run the model with the Noisy-OR and Leak input probabilities in HUGIN.

# 4. Application of the proposed framework 

### 4.1. Risk event identification

The risks identified through the literature review performed were grouped, synthetized and sketched, resulting in the scheme presented in Figure 3.

![img-2.jpeg](img-2.jpeg)

Legend: (1) Basuki et al. [20]; (2) Queiroz [14]; (3) Basuki et al. [116]; (4) Iwańkowicz and Rosochacki [22]; (5) McManus and Haddad [117]; (6) Fragiadakis et al. [21] (7) Pérez-Garrido et al. [118]; (8) Pires Jr. et al. [15]; (9) Lee et al. [19]; (10) Lee et al. [119]; (11) Venkatesh et al. [75]; (12) Yao et al. [82]; (13) Carbonara et al. [40]; (14) Sokri and Ghanmi [3]; (15) Yue and Zhang [120]; (16) Lu and Tang [121]; (17) Barlas [35]; (18) Cheng and Lu [43]; (19) Jacinto and Silva [18]; (20) Barney [36]; (21) Yun and Park [122]; (22) Bennet [37]; (23) Meier [62]; (24) Nowinski and Kohler [123]; (25) Kwak and Smith [1]; (26) National Audit Office [124]; (27) Department of Defence [125]; (28) Rodger et al. [71]; (29) Nicoll and Delaney [126]; (30) Nicoll and Delaney [127]; (31) Tuunanen et al. [128]; (32) Neves et al. [66]; (33) Wan et al. [76]; (34) Keith et al. [129]; (35) Yu et al. [84]; (36) Karvetski and Lambert [130]; (37) Iden et al. [50]; (38) McLeod and MacDonell [131]; (39) Stanley and Wilhite [132]; (40) Siemieniuch and Sinclair [133]; (41) Moreland et al. [134]; (42) Radjenovic and Paige [135]; (43) Boehm and Bhuta [136]; (44) Schaefer [137]; (45) Wang et al. [138]; (46) Hung et al. [49]; (47) Philip et al. [139]; (48) Christiansen and Thrane [2]; (49) Mane and DeLaurentis [140]; (50) Marmier et al. [141]; (51) Felderer and Ramler [46]; (52) Kochetkov and Aliev [17]; (53) Marmier et al. [141].

Fig. 3 - Causes, risks and effects

# 4.2. Risk analysis 

The final model (obtained using the Delphi method with the collaboration of the first panel) comprises eight risk groups and twenty causes (Figure 4). Based on their experience, the experts on the first panel also stated the frequency of occurrence of a given risk qualitatively (using the linguistic term set $=\{$ almost never, infrequently, sometimes, often, always $\}$ ). These frequency perceptions were used to control the probabilities of occurrence referred by the second panel. Given the complexity of the network, the three less frequent causes (Transport inefficiency, Fast growth of orders, and Growth of the sector) were not included in subsequent analysis (also because the strength of related interconnections was relatively low).
![img-3.jpeg](img-3.jpeg)

Fig. 4 - Risk Network Model for military shipbuilding projects

### 4.3. Risk evaluation

Two projects for the construction of Brazilian warships in national shipyards, carried out in the last decade, were selected for this study. For reasons of confidentiality, such projects are denominated as "project X" and "project Y". In the context of these projects, seven project managers were

interviewed (in two sequential moments: first, to obtain the input data; afterwards, to validate the obtained results). Table 5 shows some characteristics of the projects and of the interviewed experts (second panel). The guide for the interviews and the research objective of the questions is available in Appendix 1. All the interviewees agreed that implementing the framework steps is easy: 1) the use of diagrams helps understanding the cause-effect relationships; 2) the use of linguistic variables simplifies the expression of the probabilities of occurrence, moreover in situations where lack of experience exists (which is the case of the Brazilian Navy), although, according to the interviewees, expressing opinions about conditional probabilities remains a difficult task. The interviewees also agreed that the results obtained through the use of the framework are in accordance with what really happened in the two projects analyzed and that, given the simplicity of the process and the flexibility of the structure network, it will be easy to adapt the network to other projects/contexts. Moreover, two of the interviewees highlighted the importance of the framework to the organization as a mean to start structuring the assessment of risks and to induce gathering of risk related information for future use.

Table 5 - Project and expert (second panel) characteristics


Note: For example, $0.265=E 1$ score / sum of scores of all project $X$ experts The weight (importance) given to the experts was (subjectively) attributed depending on their experience (see Table 4). For a more rigorous approach, other elicitation or scoring methods should be used, for example, Cooke's classical performance-based weight model [142].

In order to illustrate the process of obtaining the probabilities of occurrence, we use the opinions of 3 experts (E5, E6, E7) for risk "failures of the supplier" that has four causes: A - inexperience of the stakeholders, B - financial inability, C - delay in customs clearance, and D - another cause not present in the diagram (like, for example, fast growth of orders) (Table 6). The aggregation of the expert opinions is obtained through a simple weighted arithmetic average.

Table 6 - Probabilities of occurrence (calculation process)


The structure of the Bayesian Network and the inference results based on the Bayesian Network are shown in Figure 5 for project X and Figure 6 for project Y. To control the results, the obtained probabilities are compared with the results of question 2 of the Delphi method (For each risk, how often do the causes of risk represented in the figure occur in the construction of a military ship? Would you like to suggest other cause(s)? - see figure 4). For projects X and Y , none significant difference was detected (it should be noticed that the framework uses two independent samples of experts). In case there are differences, we recommend that the results of question 2 are shown to the second panel in order to verify if they want to reconsider their inputs.

![img-4.jpeg](img-4.jpeg)

Figure 5 - Risk Network Model for Project X

![img-5.jpeg](img-5.jpeg)

Figure 6 - Risk Network Model for Project Y

Table 7 shows the probabilities of occurrence obtained for the eight risk groups considered for projects X and Y . It should be noted that the probabilities presented may be higher than those that would have been obtained if the application of the framework to projects X and Y was made in anticipation of project development, because the experts may have overvalued the probabilities of primary causes they knew had occurred. The risks with higher probability of occurrence were, for both projects, failures or errors of production, of the contracted, of requirements, and of planning.

Table 7 - Probability of risk occurrence for projects X and Y .


# 4.4. Sensitivity analysis (risk mitigation actions) 

Project managers need to identify preventive actions to reduce risk probability before the risk occurs or protective actions to lower the risk impact after its occurrence. Mitigation actions should be directed at the primary causes associated with the risks with the greatest sensitivity (e.g., in project X, acting on the cause "Replacement of duties or lack of career incentives" would impact the probability of risk "Lack of qualified labor force" significantly, see Table 9).

The causes can be seen individually or can be grouped in categories according to their level of control (high, average or low control). High control corresponds to less complex mitigation measures, usually for internal causes with less costly mitigation actions; average control is usually related to

external causes linked to suppliers or other partners with close relationships, to technology changes, to financing, etc., with a medium mitigation cost; and low control is related to external causes that the organization does not control or has very little control over, for example, the issuing of new laws. Table 8 shows a possible classification.

For illustrative purposes, we performed two simulations: experience A, a reduction of $30 \%$ on the primary causes (one at a time, keeping the others constant); and experience B, a $30 \%$ reduction on the three groups of causes - high control, partial control, little or no control (one at a time, keeping the others constant). The results of these experiences (presented in Table 9) show that, while the use of mitigation actions directed at individual primary causes may have had significative impact on the probability of occurrence of some individual risks, more generalized reductions may have been obtained through a set of actions. Thus, important effects could have been attained through less complex and less costly internal mitigation actions (directed at the first set of causes) or through actions involving an improvement in the management of the relations with suppliers and other partners (directed at the second set of causes).

Table 8 - Classification of mitigation actions


Table 9 - Risk probability variations as a result of the reductions of the probability of occurrence of primary causes (experiences A and B)



Notes: Blank cells mean that the variation was 0.000; shadowed lines correspond to experience $B$.

# 5. Conclusions 

This research has provided some insights about what risks and causes may affect the success of complex projects related to the shipbuilding of the Navy of Brazil according to the (consensual) perception of the experts. Its main contribution has been providing a simple and understandable framework for risk management applicable to complex and unique projects with scarce/limited data, based on visual diagrams and using the Noisy OR canonical model. The effort required by the process used to obtain the experts' opinion was reasonable. Fuzzy theory was helpful to deal with the linguistic inputs of experts. The examples of application show that the proposed framework has acceptance between military experts mostly because it is suitable to customize the structure of the risk network according to the uniqueness and complexity of the ship under construction, it allows a global visualization of the interdependencies of the risk events, it obtains likelihoods of the risks and it allows simulations of risk mitigation strategies along the project duration (in the beginning, with a preventive perspective and, during the execution of the project, with a protective perspective). The proposed approach can be useful even when the project is still in an embryonic stage and it is not possible to design the global network and assess the likelihood of the risk events and measure their impact. The simple perception of the relationships and of the likelihood that each identified risk event may have on the success of the projects will enable decision makers to direct some decisions to the mitigation of the causes of risks.

Additionally, this work contributes to the research in defense contexts by proposing a framework that combines the Delphi method (to collect expert opinion), fuzzy theory, and BN with Noisy OR. The framework starts by identifying risk events (from military shipbuilding and other areas) that are then confirmed (refuted) as suitable for the case under analysis. The customize risk network structure thus obtained is contained in terms of dimension so that it can be used by the decision makers. Two real examples were used to confirm the practical applicability of the framework in real situations. A simple

sensitivity analysis was performed to illustrate how to obtain the necessary information for the discussion of the best mitigation actions to apply in a specific case.

The developed study has several limitations. The need to collect inherently subjective data from groups of experts may have introduced some bias in the analysis. Some effort should be placed to develop and maintain databases to collect and store formal, quantitative and accurate information about shipbuilding projects. It was not possible to validate the BN model by applying it to a project in anticipation of its development and comparing the results of the model with the occurrences of the project. Also, the used approach did not consider the possibility of dependency between causes. This possibility should be addressed in future research. Finally, the results of this research may have been shaped by the context of the study. For different shipbuilding contexts, adaptations will probably be needed.

Interesting developments of this study may arise from the consideration of the whole shipbuilding supply chain since several of the identified causes and risks arise from the interaction with suppliers or contracted partners.
