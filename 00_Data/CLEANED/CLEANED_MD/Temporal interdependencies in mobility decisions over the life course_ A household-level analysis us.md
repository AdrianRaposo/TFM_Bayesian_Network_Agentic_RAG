# Temporal interdependencies in mobility decisions over the life course 

Citation for published version (APA):
Guo, J., Feng, T., Zhang, J., \& Timmermans, H. J. P. (2020). Temporal interdependencies in mobility decisions over the life course: a household-level analysis using dynamic Bayesian networks. Journal of Transport Geography, 82, Article 102589. https://doi.org/10.1016/j.jtrangeo.2019.102589

Document license:
TAVERNE

DOI:
10.1016/j.jtrangeo.2019.102589

Document status and date:
Published: 01/01/2020

Document Version:
Publisher's PDF, also known as Version of Record (includes final page, issue and volume numbers)

Please check the document version of this publication:

- A submitted manuscript is the version of the article upon submission and before peer-review. There can be important differences between the submitted version and the official published version of record. People interested in the research are advised to contact the author for the final version of the publication, or visit the DOI to the publisher's website.
- The final author version and the galley proof are versions of the publication after peer review.
- The final published version features the final layout of the paper including the volume, issue and page numbers.
Link to publication


## General rights

Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.

- Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
- You may not further distribute the material or use it for any profit-making activity or commercial gain
- You may freely distribute the URL identifying the publication in the public portal.

If the publication is distributed under the terms of Article 25fa of the Dutch Copyright Act, indicated by the "Taverne" license above, please follow below link for the End User Agreement:
www.tue.nl/taverne

## Take down policy

If you believe that this document breaches copyright please contact us at:
openaccess@tue.nl
providing details and we will investigate your claim.

# Temporal interdependencies in mobility decisions over the life course: A household-level analysis using dynamic Bayesian networks 

Jia Guo ${ }^{\text {a }}$, Tao Feng ${ }^{\mathrm{a}, *}$, Junyi Zhang ${ }^{\text {b }}$, Harry J.P. Timmermans ${ }^{\mathrm{a}}$<br>${ }^{a}$ Urban Planning Group, Department of the Built Environment, Eindhoven University of Technology, PO Box 513, 5600MB Eindhoven, the Netherlands<br>${ }^{b}$ Mobilities and Urban Policy Lab, Graduate School for International Development and Cooperation, Hiroshima University, Japan, 1-5-1 Kagamiyama, Higashi Hiroshima 739-8529, Japan

## A R T I C L E I N F O

Keywords:
Life course decisions
Residential change
Job change
Car ownership change
Temporal dependencies
Household decision making mechanisms

## A B S T R A C T

Life trajectory analysis has been shown a powerful approach to understand the interdependencies between key life events, critical incidents and long-term mobility decisions such as residential move, job change and change in vehicle possession, which in turn constitute the context of daily activity-travel decisions. Because people in multi-earner households share resources, some of these long-term decisions affect them equally, while job change affects them differently because their job location likely differs. Current life course models in transportation research, however, have typically considered individuals' trajectories. To contribute to the further development of the relatively thin line of research in transportation studies, a dynamic Bayesian network approach is proposed to investigate the temporal interdependencies between life course events from a household perspective. Results show that the effects of child birth are much larger on residential and car ownership change than on job change for both household heads in dual-earner households. Moreover, the probability of residential and car ownership change increases when both spouses have relatively long commuting times. In case only the husband faces an excessive commuting time, households have a larger probability of moving house or purchasing an additional car. By contrast, in case only the wife faces an excessive commuting time, she is more likely to change job rather than the household taking particular actions to adjust to the problematic situation.

## 1. Introduction

Models that predict the effects of transportation policies tend to be confined to this specific domain. They fail to acknowledge that daily travel is just one factor influencing people's quality of life. Consequently, the application of such models may be misleading if the considered transportation policy does not only affect the daily travel patterns of households, but also other life domains. For example, if the travel time between an O-D pair reduces for a particular transportation mode, travel demand models will typically predict an increasing market share for that mode. However, if concepts such as action space (Horton and Reynolds, 1969), reasonable travel times (Timmermans, 1979) and (probabilistic) space-time prisms (Lenntorp, 1976; Liao et al., 2014) are valid, households may not change transportation mode but rather use the gain in travel time to move to a larger house further away from the city at lower cost/squared meter. In other words, transportation policies may affect individual and household decisions in other life domains, in this case residential location, which should be taken into consideration to avoid biased assessments of the effects of transportation policies.

Similar to the concept of mobility biography, the life course approach, with a long history in sociology, demography and geography but introduced in travel behavior research only in the early 2000s and growing slowly but steadily in popularity ever since (e.g., van der Waerden et al., 2003; Lanzendorf, 2003; Verhoeven et al., 2005, 2007; Oakil et al., 2011; Scheiner and Holz-Rau, 2013; Xiong and Zhang, 2014; Müggenburg et al., 2015; Beige and Axhausen, 2012, 2017; Delbosca and Nakanishi, 2017; Zhang and van Acker, 2017; de Haas et al., 2018; Scheiner, 2018; Wang et al., 2018), is one of the few comprehensive approaches that considers this wider perspective. Life trajectory analysis assumes that individuals wish to achieve particular goals in life. In order to reach these goals, they need to go through a series of co-dependent stages in different life domains. For example, to possess a dream house, individuals need to acquire a job that provides them with sufficient income. A precondition for that job is to have the education, training and job experience. Dependent on the accumulated income, it may be impossible to buy the dream house in one step. Rather, households may need to move up on the housing ladder in multiple, small steps.

[^0]
[^0]:    * Corresponding author.

    E-mail addresses: j.guo@tue.nl (J. Guo), t.feng@tue.nl (T. Feng), zjy@hiroshima-u.ac.jp (J. Zhang), h.j.p.timmermans@tue.nl (H.J.P. Timmermans).
    https://doi.org/10.1016/j.jtrangeo.2019.102589
    Received 21 September 2018; Received in revised form 28 March 2019; Accepted 29 October 2019
    0966-6923/ © 2019 Elsevier Ltd. All rights reserved.

Since the introduction of the life course approach in travel behavior research, several studies have emphasized the interdependencies between different life domains, including residence, job, household structure, car ownership, etc. (e.g., van der Waerden et al., 2003; Verhoeven et al., 2005, 2007; Goulias, 2009; Oakil et al., 2011, 2014; Rashidi et al., 2011; Dubernet et al., 2018; Scheiner, 2018; Wang et al., 2018). The approach acknowledges that life events may lead to a reconsideration of a household's current status in different life domains and possibly to decisions changing the current status. For instance, several studies found that child birth plays an important role in various life course mobility decisions due to the fact that an increase in the number of household members may create the need for a bigger house or an additional or larger car (e.g., Dieleman and Mulder, 2002; Warner and Sharp, 2015). Similarly, Clark et al. (2016) found that commuting mode changes are primarily driven by job change and residential relocation. These interdependencies between key life events and longterm decisions may involve both lagged and lead effects, reflecting reactive respectively pro-active behavior (e.g., Yamamoto, 2008; Oakil et al., 2014; Zhang et al., 2014; Chatterjee and Scheiner, 2015; Fatmi and Habib, 2016). Long-term mobility decisions are not only made concurrently, but also in adjustment to past events and/or in anticipation of future expected events.

Because household members physically share household resources, long-term decisions affect all household members. Some of the effects such as residential move will affect them equally, while other effects such as changing commuting distance may differ between spouses (e.g. Timmermans et al., 1992; Borgers and Timmermans, 1993). Scheiner (2014) studied changes in travel mode specific trip rates after life course events from a gender perspective. He found that the effects of child birth, labor market entrance, and changes in spatial context, accessibility and mobility differed distinctly between men and women. Similarly, Oakil (2016) provided empirical evidence that life events such as birth of the first child, residential relocation and job change only significantly affect women's decision to get full-access to a car.

This study contributes to the literature on life course analysis in transportation research by modeling long-term mobility of dual-earner households, looking into the dependencies between various life domains: child birth, residential change, job change, and car ownership change. The central question here is to what extent child birth affects life trajectories in other domains of wives and husbands, and how status of wives and husbands affects household decisions. Concurrent and lagged/lead effects are considered. In addition to this substantive contribution, the modeling will be based on dynamic Bayesian networks and in that sense the current study also elaborates prior research in life course analysis that has relied on static Bayesian networks (Verhoeven et al., 2005; Wang et al., 2018).

The remainder of this paper is organized as follows. Section 2 presents the structure of the integrated model that explicitly incorporates time-dependent dependencies within and between different life domains, using households as the observed decision-making unit. Section 3 discusses the retrospective survey that was used to collect the life trajectory data of households. The model results are presented and interpreted in Section 4. Finally, concluding remarks are made regarding results, policy implications and future research.

## 2. Methodology

### 2.1. Background

Long-term decisions such as residential and job choice are high involvement decisions that have long-term repercussions on people's daily life. These decisions tend to co-depend on past and future decisions across different life domains. The aim of this study is to uncover these dynamic interdependencies between household long-term mobility decisions in various life domains. The term mobility decision refers to the notion that individuals move through different stages of different
life domain-specific careers. In particular, we focus on residential mobility (moving house), job mobility (changing job) and car ownership mobility (change in car possession). This study is particularly concerned with dual-worker households.

First, we analyze the interdependencies between life domains (child birth, residential move, job change, and car ownership change). Residential moves relate to moving from one house to another. Job change includes the first time entering the labor market and switching to a new job. Change in car ownership means that a new car is added to the owned vehicle pool (which may be zero) with or without replacing another. Second, we analyze the long-term decisions of different members of the same dual-earner household (wife and husband). Residential change and change in car ownership are treated at the household level in the sense that both spouses experience the same change, while job change is examined at the individual level. Third, apart from concurrent effects, both one and two years lagged and lead effects are considered in this study.

We use one year as the time unit. If any event occurs more than once in a single year, we take the last event into account. For example, if individuals reported they changed jobs three times within one year, we take the state of the last event as input to the Bayesian decision network.

### 2.2. Model specification

Bayesian networks are attractive to flexibly examine the interdependency relationships between various life course domains. BNs belong to the family of probabilistic graphical models. They consist of a set of nodes and a set of arcs that form a directed acyclic graph (DAG). Each node represents a domain variable whereas directed arrows between variables indicate dependence between them given that the values of their parents are known. Let $\mathbf{X}=\left(X_{1}, X_{2}, \ldots X_{n}\right)$ denote a set of random variables, while $\mathbf{P a}\left(X_{i}\right)$ denote the parents node of $X_{i}$ in the DAG. The conditional probability distribution of $X_{i}$ is denoted by $P$ $\left(X_{i} \mid \operatorname{Pa}\left(X_{i}\right)\right)$. Then the joint probability distribution can be represented as follows.
$P\left(X_{i}, X_{j}, \ldots X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \mathbf{P a}\left(X_{i}\right)\right)$
Any probability of interest can be computed from this joint probability distribution.

While Bayesian networks are powerful models for examining the interdependencies between various household long-term decisions, the Bayesian Networks were originally not designed to explicitly model temporal relationships; they are static models. As a temporal extension of a Bayesian network, Dynamic Bayesian network have been developed to introduce a temporal dimension to BNs. Therefore, this study represents an extension of previous work on life trajectory decisions using static Bayesian networks (e.g. Verhoeven et al., 2005; Wang et al., 2018). It offers an appropriate approach to explore the dynamic dependencies between various life course domains into an integrated model, in which a state of a variable in one time instance is dependent on one or more states in other time instances.

DBNs can be defined as a pair of BNs $\left(B, B_{\rightarrow}\right)$, where $B$ represents the initial distribution $P\left(X_{i}\right)$, and $B_{\rightarrow}$ is a two-slice temporal Bayes net which contains an instance of each variable at time $m+m^{\prime}$ and $m$. The probability of node $i$ over two time slices is defined as,
$P\left(X_{m+m^{\prime}}^{i} \mid X_{m}^{i}\right)=\prod_{t=m}^{m+m^{\prime}} P\left(X_{t}^{i} \mid \mathbf{P a}\left(X_{t}^{i}\right)\right)$
where $X_{t}^{i}$ is the $i^{\prime}$ th node at time instance $t$, and $\mathbf{P a}\left(X_{t}^{i}\right)$ is the set of parent of nodes $X_{t}^{i}, t_{t}\left(m^{\prime}, m\right)$.

In the present study, this modeling approach was adopted to study interdependencies between life events and long-term mobility decisions of double-earner households. Child birth was chosen as an example of a

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** Network structure.

life event. It may trigger reconsidering job choice, residential choice and/or vehicle possession, which were the long-term mobility decisions examined in this study. Because the location of the job relative to the home defines commuting distance/time and changes in one of these thus leads to change in commuting distance, commuting distance is another node of the Bayesian network. Moreover, household income was included in the model as it is linked to the job.

The network structure is shown in Fig. 1. As discussed, the framework includes dynamics, time dependence, and interrelationship among long-term decisions. With respect to temporal interdependencies between different long-term mobility decisions, it is assumed that child birth may have both 1 and 2 years lagged and lead effects on the long-term mobility decisions. Thus, for example, mobility events such as residential and job relocation may have lagged, concurrent and lead effects on car ownership change. Lastly, mobility states such as income and commuting time are assumed to have direct impacts on various long-term mobility decisions. For example, people may take different actions such as changing job, moving house, and purchasing/changing cars to avoid excessive commuting time.

### 2.3. Learning

Given a dataset, developing a DBN requires two steps: learning the network structure and estimating the parameters of the learned network structure. Structure learning is about finding the significant relationships between network nodes. Potential causal dependencies between household life events can be interpreted through pairs of temporal network nodes. Structure learning of a DBN involves both intra-time slice and inter-time slice connectivity. Dealing with the temporal data, MCMC (Markov chain Monte Carlo) and Structure EM algorithms (Expectation Maximization), can only be applied to networks of moderate complexity due to many time instances and state variables (e.g., Murphy, 2003). Therefore, a semi-structure learning process was adopted in this study.

First, to simplify the network structure and avoid unrealistic relationships, plausible constraints were set. In particular, child birth may affect residential change, job change for both wives and husbands, and car ownership change. However, the reversed effects are not allowed. Thus, unidirectional effects were set between child birth and various long-term decisions. Secondly, the inter time-slices structure network is constructed a priori using the dynamic properties of the dynamic Bayesian network. Third, given these constraints, the Bayesian search algorithm is applied to learn the dependencies between life course mobility decisions within one time slice. Given this semi-learned network, the EM (Expectation Maximization) algorithm (Dempster et al., 1977) was used to learn the parameters.

### 3. Data collection and sample description

#### 3.1. Data collection

The analysis of life course decision-making processes requires longitudinal data. However, obtaining sufficient information about long-term behavioral change through a panel survey is both time and resource consuming. Thus, as an alternative to a panel survey, a retrospective survey was used in the present study. In a retrospective survey, respondents are invited to recall past life events in certain domains, typically in chronological order. For example, they are asked to recall the sequence of houses in which they lived and prompted to elicit a set of attribute levels of each house. Because the data collection is based on recalling events that may have occurred considerable time ago, retrospective surveys are sensitive to recall bias. Fortunately, experience learns that the amount of recall bias is relatively small for life events that have shaped the life trajectory of the respondent (Lanzendorf, 2003; Verhoeven et al., 2005; Behrens and Del Mistro, 2010). Moreover, one should not forget that panel surveys have their own problems.

The retrospective survey was administered between September and November 2016, in Shenyang, China. Considering the aim of the study, we restricted our sample to respondents belonging to dual earner households. Except for socio-demographic information of each household member, data about life course events were collected. In particular, the following events were included in the data collection: child birth, residential moves, car ownership change and job change of each spouse. In addition, because these were assumed to be important influential variables, annual income/and commuting time of both spouses were collected. A single respondent provided the data of both spouses. This may be less ideal, but arranging interviews with two spouses would have been much more demanding and not worthwhile. In order to reduce respondent burden, respondents were asked to provide information about the life events for only the last five times it occurred. In many cases, this maximum of five still covers the full trajectory of life events in a particular domain, particularly for younger respondents.

The retrospective survey was implemented through face-to-face interviews conducted by master students, who were specially trained for this task. To improve data quality, interviewers used a Web-based survey system developed by our research group. This system checks for data input ranges and logically impossible or unlikely answers, giving the interviewer the opportunity to double-check the answer with the respondent. The face-to-face interviews were conducted in five main urban districts and four surrounding areas of Shenyang using a spatially stratified sample. Recruitment was based on the method of random walks. Respondents were given small gifts of appreciation as the survey

Table 1
Sample description.


was 24 pages long and its completion took over 50 min . The response rate is $16 \%$, which is satisfactory, considering the unannounced contacting of possible respondents, the high percentage of non-eligible respondents (recall: dual earner households) and the length of the survey. After limited data cleaning, the ultimate sample used for analysis consisted of 266 dual-worker households.

### 3.2. Sample description

The sample consists of 138 (51.9\%) females and 128 (48.1\%) males. The average age is 38.2 , while on average are younger than their husbands. Average household size is 3.2 persons. $12.8 \%$ of the couples have no children; $5.6 \%$ have two children, while the remaining $81.6 \%$ has one child. These statistics indicate that some households involved three generations.

Table 2 presents the descriptive statistics for the main life course events. $22.9 \%$ of the respondents never changed residence; $41.4 \%$ changed only once, $25.2 \%$ changed twice and only about $10.5 \%$ moved house $>2$ times. In case of car ownership change, $33.5 \%$ of the respondents never had a car in their household; $43.2 \%$ had one car but never changed; $14.4 \%$ reported to have changed cars once, while the remaining $5.7 \%$ changed cars more than once in the past. Moreover, data of job change were collected for both spouses. As shown in Table 1, wives changed job less often than husbands.

Table 2
Descriptive statistics of the life course events.


Table 3-1
Lagged, concurrent and lead effects of child birth on residential change.


Table 3-2
Lagged, concurrent and lead effects of child birth on car ownership change.


Table 3-3
Lagged, concurrent and lead effects of child birth on job change.


Table 4-1
Lagged, concurrent and lead effects of residential change on car ownership change.


## 4. Results and analysis

### 4.1. Results of structure learning

The Bayesian search algorithm was used in the structure learning process within one time slice. The prior link probability was set as the default value 0.001 for the structure learning process. The learned structure network for the one time slice is shown in Fig. 2a. Concurrent effects between various household mobility decisions are shown as two aspects. First, as we expected, child birth has direct effects on various household mobility decisions such as residential change, car ownership change, and job change for both husband and wife. Second, the learned structure network indicates that moving house and changing job for both wife and husband have direct effects on household car ownership change. Lagged and lead causal relationship between various household mobility decisions discussed in Section 2.3 are represented in Fig. 2b and c respectively. 1-year temporal effects are shown by the blue lines, while 2 -year temporal effects are shown by red lines.

Table 4-2
Lagged, concurrent and lead effects of job change on car ownership change.


Table 5-1
Lagged, concurrent and lead effects of residential change on commuting time change of the spouses.


Table 5-2
Lagged, concurrent and lead effects of car ownership change on commuting time change of the spouses.


### 4.2. Results of parameter learning

Based on the network structure shown in Fig. 1, the EM algorithm was applied to estimate the time-dependent conditional probability tables (CPTs) for all nodes and time slices. In this paper, both the updated conditional probability and relative probability differences are calculated. Updated conditional probability indicates the updated probabilities for the related nodes once a particular change in the network is activated. Relative probability difference is defined as the

Table 6
Predicted probability of car ownership change given different levels of wife and husband's commuting time.


difference between the updated conditional probability and the prior probability divided by the prior probability. Assume the prior probability of a certain event is denoted as $p_{0}$, and the updated conditional probability as $p^{\prime}$. Then, the relative probability difference $p_{\text {diff }}$ is calculated as follows,
$p_{\text {diff }}=\frac{p^{\prime}-p_{0}}{p_{0}}$
The relative probability difference can be both negative and positive. Positive values represent the case when the effect of an event of mobility decision is positive, while negative values indicate a negative impact. A probability difference close to zero indicates that the event/ mobility decision do not influence the variable of interest.

### 4.2.1. Household mobility decisions given child birth

The effects of child birth on different household mobility decisions are presented in Tables 3-1, 3-2, 3-3. Here, ' $t$ ' indicates the year where a certain event occurred; ' $t-1, t-2$ ' indicates one-year and two-year ahead of the event, while ' $t+1, t+2$ ' indicates one-year and two-year later than the event. Tables 3-1, 3-2, 3-3 shows that child birth positively influences different mobility decisions in households. However, the effects differ in size for different decisions. Looking at the conditional probability table, the effects on residential change and car ownership change are much stronger than the effect on job change for both wife and husband in dual-worker households. The birth of a child implies new responsibilities. Consequently, household are more likely to find a larger house/change cars in response to the increase in household size.

In addition, the temporal effects of child birth are shown to differ in size between the long-term mobility decisions in different life domains. Specifically, results show that both the 1-year lagged and lead effect are much bigger than the 2 -years temporal effects. In addition, the lead effects $(t+1 / t+2)$ are in general larger than the lagged effects $(t-1 / t-$ 2), suggesting that residential change/car ownership change is more likely to occur in anticipation of a household structure change in the current study.

However, a reverse result is found on car ownership. A child birth increases the probability of a change in car ownership most in the same year. The two year lag effect is much smaller than the 2 -year lead effect,

Table 7-1
Probability difference of residential change given different levels of wife and husband's annual income.


while the one year lead and lag effects are the same. It suggests that child birth tends to immediately increase people's mobility needs and hence their tendency of purchasing an (additional) car.

In case of changing job, results show that both the lagged and lead effect as well as the concurrent effects of child birth on changing job for both wife and husband are much smaller than the effects on other life course mobility decisions. It means that childbirth tend to primarily increase the need for a larger dwelling and/or a more convenient transportation option. Although the set of responsibilities of both wife and husband may increase due to a new-born baby, there is no strong evidence that household members will change their jobs. Moreover, a noticeable finding is that both the 2 -year lagged and lead effects for the wife are bigger than the 1 -year and concurrent effects, indicating that wives need more time to change jobs before/after giving birth to a child as a similar result is not found for husbands.

### 4.2.2. Car ownership change given residential and job change

Tables 4-1, 4-2 shows the results of the relative probability differences given evidence of various household mobility decisions. The lagged, lead and concurrent effects of residential and job change for both wife and husband are found to positively influence car ownership change. In general, concurrent effects are stronger than lagged and lead effects on car ownership change.

Taking a closer look at the different temporal effects on various mobility decisions, results show that the conditional probability for car ownership decisions is nearly double the prior probability. Moreover,

Table 8
Probability difference of changing job given different levels of wife and husband's annual income.


the updated CPTs show that concurrent and lagged effects are slightly larger than the lead effects. Only minor differences are found between wife and husband. However, when both wife and husband change their jobs, the probability for households buying or changing cars increases dramatically.

### 4.2.3. Household mobility decisions given wife and husband's commuting time

Our conceptual model assumed that commuting times of the household members may influence long-term residential change, job change and car ownership change. Several interesting findings are found in this study (shown in Tables 5-1, 5-2). First, as expected, wife and husband's commuting times differently influence household residential change and car ownership change. In the case that husbands have excessive commuting times ( $>1 \mathrm{~h}$ ) while wives have a relative

Table 7-2
Probability difference of car ownership change given different levels of wife and husband's annual income.


![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

**Fig. 2.** a Learned structure of concurrent effects. b Structure of lagged effects. c Structure of lead effects.

long commuting time (40–60 min), the residential change and car ownership change increase to 14% and 18%, respectively. However, when wives have > 1 h travel time while the husband has 40–60 min commuting time, the probability of change is small (only 5% and 12%, respectively). This means that the probability of residential change and car ownership change increase when both wife and husband face relative long commuting time. However, the magnitude of this effect varies between household members.

Second, in dual-earner households, the probability of moving house dramatically increases if the residential location is very close to one worker but quite far away from the other worker's job location. For example, as shown in Tables 5-1, 5-2, in case the commuting time is < 20 min and more than one hour for the wife and husband respectively, the probability of moving house is increased to 14%. Similar results can be found on car ownership mobility change. Lastly, if at least one household member has a relative short commuting time (20–40 min), the desire to move house and change cars are relatively low.

Given different levels of commuting time for wife and husband, results show that excessive commuting times do increase the probability of job change. However, this effect differs between wives and husbands. As shown in Table 6, wives are more sensitive to long commuting times (> 40 min) than husbands, and consequently more likely to change job. In this regard, wives and husbands may take different actions when faced with excessive commuting times. In case only husbands face excessive commuting time, dual-worker households have a larger probability to move to a new house or switch to a more convenient transportation mode (53% and 35% increase of probability, respectively). However, if only the wife is facing excessive commuting times, they are more likely to change jobs instead of moving house or changing car ownership.

### 4.2.4. Household mobility decisions given wife and husband's annual income

The difference in probabilities of various life course mobility decisions given different levels of annual income for both wife and husband are shown in Tables 7-1, 7-2 and 8. Results show that households with a high income in general have a larger probability to move house and change cars. The probabilities of moving house and changing cars for both wife and husband with the highest annual income (> 150,000 yuan/year) are 8.7 times and 3.4 times higher than for households with the lowest annual income (< 40,000 yuan/year for both wife and husband). Another notable finding is that wife's income plays an important role in various household mobility decisions. Households with

the wife having the lowest annual income ( $<40,000$ yuan/year) and the husband having the highest annual income ( $>150,000$ yuan/year) have a $14 \%$ probability of moving house. On the other hand, the probability of moving house for the households with the same total annual income but different contribution between members (i.e. wife has the highest and husband has the lowest annual income) is $17 \%$. Similar results are also found for car ownership change.

Likewise, wife and husband's income have a direct influence on the decision of changing job. In general, the probability of changing job is relatively high for people with a relatively low income. In addition, income has a different effect on the decision to change jobs for wives and husbands. When both household members have the lowest annual income ( $<40,000$ yuan/year), wives have a larger probability of changing job ( $67 \%$ vs. $8 \%$ respectively). When having a high-paid job ( 150,000 yuan/year), the probability for husbands to change job is lower than for wives.

## 5. Conclusions and discussion

Life course analysis is a rich approach to analyze and model the interdependencies among a set of lifetime events. In contributing to this emerging field of study in transportation research, this paper reports the main findings of a Dynamic Bayesian Network derived from life trajectories of dual-earner households, considering lagged, concurrent and lead effects, in part separately for husbands and wives. Four life course domains (child birth, residential change, job change for both wife and husband, and car ownership change) are incorporated. In addition, commuting time and income of husband and wife are taken into consideration, in order to examine their potential influence on various household mobility decisions.

Whereas similar prior studies have relied on static Bayesian network, in this study a Dynamic Bayesian network based on retrospective life trajectory data was applied to examine the temporal dependencies between various life-course mobilities. Taking household as the decision unit, the model results point at some interesting findings. First, child birth is found to have positive effects on different mobility decisions. The effects on residential change and car ownership change are much stronger than the effects of childbirth on job change for both wife and husband. Moreover, in terms of residential change and car ownership change, results suggest that lead effects are in general larger than lagged effects, indicating that residential change and car ownership change are more likely to occur in anticipation of household structure change. In terms of changing jobs for both wife and husband, results show that both the 2 -year lagged and lead effects are larger than the 1 year and concurrent effects. It suggests that wives need more time to change jobs before/after giving birth to a child. Second, the lagged, lead and concurrent effects of residential and job change for both wife and husband are found to positively influence car ownership change. Moreover, in case of the influences of changing jobs on car ownership change, only minor differences are found between wife and husband. However, when both wife and husband change their jobs, the probability of buying or changing cars increase dramatically.

Apart from the long-term mobility decisions, commuting time and income are important factors influencing various mobility decisions. The probability of residential change and car ownership change will largely increase when both wife and husband face relatively long commuting times. Moreover, results show that, in dual-worker households, the probability of moving house will dramatically increase if residential location is very close to one worker but quite far from another worker's work location. Given the evidence of commuting time for both wife and husband, it shows that excessive commuting time does increase the probability of job change. An interesting finding is that wives and husbands may take different actions when faced with excessive commuting times. For dual-worker households, in case that only the husband has an excessive commuting time, the household has a larger probability to move house or switch to a more convenient
transportation mode. However, in case only the wife faces an excessive commuting time, dual-earner households are more likely to change job instead of taking other mobility decisions. Moreover, the annual income of both wife and husband were shown to have a direct influence on various mobility decisions. Findings indicate that households with a higher income tend to have a larger probability to move house and change cars and a smaller probability to change job. In addition, income has a different effect on work mobility decisions for both wife and husband. Wives are more likely to change job than husbands when they have a low-paid job. When having a high-paid job, the probability for husbands to change is very low. However, such an effect was not found for wives.

These findings illustrate the richness of the suggested approach. Findings of this study in part confirm findings of earlier studies, mostly conducted in a European context. In addition, the differential effects complement earlier findings in life trajectory analysis, where the vast majorities of studies did not involve households. Despite the convincing results, a caveat should be mentioned. Although time has been treated explicitly and some causal relationships have been constrained in the model, still Bayesian networks rely on observed co-occurrences in the data. The network structure learnt from data differs from the sense of a theoretical validation.

Future research may extend this analysis into different directions. If a larger sample can be obtained, the network can be realistically expanded with additional lifetime events, such as marriage, divorce, retirement, etc. Similarly, node reflecting aspects of daily activity-travel behaviour can be added. Data allowing, further refinement can be obtained by allowing for number of working hours or household work schedules. Finally, rather than examining the mobility histories of dualearner households, other types of households can be studied.

## Acknowledgement

This research was supported by the China Scholarship Council.
