# RELATIONSHIPS BETWEEN CONSECUTIVE LONG-TERM AND MIDTERM MOBILITY DECISIONS OVER THE LIFE COURSE - A BAYESIAN NETWORK APPROACH 

## Bobin Wang, Corresponding Author

MOE Key Laboratory of Urban Transportation Complex Systems Theory and Technology
School of Traffic and Transportation
Beijing Jiaotong University
No. 3 Shangyuancun, Haidian District, Beijing, 100044, P. R. China
Urban Planning Group
Department of the Built Environment
Eindhoven University of Technology
P.O. Box 513, 5600 MB Eindhoven, the Netherlands

Tel: +86-10-51682236 Fax: +86-10-51682236; Email: bobinwang@bjtu.edu.cn
Soora Rasouli
Urban Planning Group
Department of the Built Environment
Eindhoven University of Technology
P.O. Box 513, 5600 MB Eindhoven, the Netherlands

Tel: +31-40-2474527 Fax: +31-40-2438488; Email: s.rasouli@tue.nl
Harry Timmermans
Urban Planning Group
Department of the Built Environment
Eindhoven University of Technology
P.O. Box 513, 5600 MB Eindhoven, the Netherlands

Tel: +31-40-2472274 Fax: +31-40-2438488; Email: h.j.p.timmermans@tue.nl
Chunfu Shao
Key Laboratory of Transport Industry of Big Data Application Technologies for Comprehensive Transport
Beijing Jiaotong University
No. 3 Shangyuancun, Haidian District, Beijing, 100044, P. R. China
Tel: +86-10-51682236 Fax: +86-10-51682236; Email: cfshao@bjtu.edu.cn
Word count: 4821 words text +10 tables/figures x 250 words (each) $=7321$ words

Submission Date: August 1st, 2017

# ABSTRACT 

Long-term and mid-term mobility decision processes in different life trajectories generate complex dynamics, in which consecutive life events are interrelated and time dependent. This study uses the Bayesian network approach to study the dynamic relationships among residential events, household structure events, employment/education events, and car ownership events. Using retrospective data obtained from a web-based survey in Beijing, China, first structure learning is used to discover the direct and indirect relationships between these mobility decisions. Parameter learning is then applied to describe the conditional probabilities and predict the direct and indirect effects of actions and policies in the resulting network. The results confirm the interdependencies between these long-term and mid-term mobility decisions, and evidence the reactive and proactive behavior of individuals and households in the context of various life events over the course of their lives. In this regard, it is important to note that an increase in household size has a contemporaneous effect on car acquisition in the future; while residential events have a synergic relationship with employment/education events. Moreover, if people's residential location or workplace/study location will move from an urban district to a suburban or outer suburban district, it has both lagged and concurrent effects on car acquisition.

Keywords: Long-term and mid-term mobility, Life events, Life trajectory, Bayesian network approach

# 1. INTRODUCTION 

In China, increasing levels of car ownership lead to many problems, such as congestion, traffic accidents, and air pollution. By the end of 2016, Beijing ranked first in car ownership with 5.48 million vehicles (1). The government is trying a variety of policies to decrease car use and stimulate modal shift from cars to public transport and slow transport, such as the odd-and-even license plate rule, fare subsidies to public transport, and congestion charging. In the short-term, these policies may change people's travel behavior. However, the effectiveness of policies in the long run will be improved by better understanding the relationships between long-term and midterm mobility decision processes.

The life course approach provides a rich framework for better understanding these relationships. Van der Waerden et al. (2) provided a conceptual framework for understanding the dynamics of activity-travel behavior, and argued that life course events and critical incidents allow people to reconsider and possibly adapt their current activity-travel patterns. Lanzendorf (3) defended the mobility biography approach for longitudinal analysis of travel behavior, distinguishing between lifestyle domain, accessibility domain, and mobility domain. This seminal work led to a small but consistent stream of research, culminating in a recent workshop and book (4), in which the scope of the life-oriented approach was expanded to include quality of life (5). In general, these developments in transportation research pick up concepts and methods related to the life course approach as it was developed earlier and more intensively in social sciences and demography.

Theoretically, the basic idea underlying the life course approach is that human life history is a sequence of socially defined events and roles enacting over time (6). The central concepts are life trajectory, transitions and events (7). Life trajectories describe different domains in life such as residence, health, education, work, leisure and recreation, and finance. Life events are defined as changes in a person's state that trigger a process of reconsideration of various life trajectories (8).

In this study, life events are the result of major decisions in a person's life, including residential move, changes in the number of household members, workplace/study relocation, and changes in car ownership. Some events may change the spatiotemporal context in which activitytravel decisions are made. Some events constrain or expand the individual's choice sets, such as a change of car ownership. Moreover, the time horizon of different events differs. Long-term decisions are related to changes of residential and work location, while mid-term decisions involve car ownership and changes in household structure. Short-term decisions are related to daily mobility, with respect to trip frequency, mode, destination, route and time of the day (9).

Empirically, research in the life course tradition has unfolded along three different lines of analysis. First and foremost, there has been a substantial body of qualitative and quantitative research about the effects of life events on activity-travel behavior. For example, Sharmeen et al. (10) reported the effects of several life events on time allocation to different activities and associated travel. Scheiner (11) focused on gender to study the effects of key events on changes in time use over the life course. Second, other researchers investigated the duration of particular states; for example, Rashidi (12) investigated the timing and reasons for residential relocation. Beige and Axhausen (8) utilized the competing risks model to compare different durations of residence, education, employment, and ownership of mobility tools. Third, a more modest stream of research analyzed the interdependencies between life events. Zhang et al. (13) used the exhaustive CHAID approach to investigate the two-way relationships between residential location and car ownership biographies in Japan, considering the influence of household

structure mobility and employment/education mobility within the framework of life-oriented approach. Verhoeven et al. (14) developed a Bayesian network to capture the dependencies between residential relocation and changes in household size. Oakil et al. (15) found complex direct and indirect dependencies between life events and long- and short-term mobility decisions.

Although this body of research has enhanced our understanding of travel behavior dynamics, it has several limitations. Most studies only focused on a single life trajectory event or one aspect of the relevant causal and temporal relationships. Very few studies integrated these aspects into an overarching model. Moreover, most studies focused on state dependencies between the life domains, but neglected the relationships between mobility decisions (16). Regarding the temporal relationships between different life events, most research only considered the sequence of events, while the event occurrence time received less attention.

Elaborating Verhoeven et al. (14), this study utilizes a Bayesian network to investigate the dynamic interrelationships between residential events, household structure events, employment/education events, and car ownership events. A web-based survey was used to collect retrospective data of life trajectories.

This paper is organized as follows. Section 2 proposes the analytical framework and describes the modelling approach. Section 3 presents the survey and sample, and variables used for the model. Section 4 presents a detailed discussion of model results. Finally, important findings and recommendations are summarized in Section 5.

# 2. METHODOLOGY 

### 2.1 Analytical Framework

This study focuses on four life trajectories: residential trajectory, household structure trajectory, employment/education trajectory, and car ownership trajectory. Residential events concern moving house (urban district, suburban district, outer suburban district). Household structure events include birth; someone leaving their parents' house; getting married; getting divorced; and passing away. Employment/education events include a change of school, someone finding their first job, and job transfers. Car ownership events involve adding, replacing and disposing of a vehicle.

Dynamics, interdependency, and time dependency are the properties of these life events examined in this study. There are various reasons for this. First, life events focus on the transition from one state to another. Second, mobility decisions are rarely made in isolation, but are strongly interrelated. A change in one life domain may trigger other mobility decisions. Third, these interrelationships may go forward (lagged effect), backward (anticipated effect), or be synchronic (contemporaneous effect). In order to consider the timing of every life event into the model, "Time ago/future events" are defined as: "how many years ago/in the future a certain event (using some classification of events) occurred/will occur, with respect to current time, t".

An example is shown in Figure 1. There are two life trajectories, and each one has a time line. A year is the unit of time, and the bold vertical lines indicate that a certain life event took place at a particular point in time. People of different age have different life history. Each observation records the information about both for the last event and the next event in different life domains, with respect to the current observation year. For the household structure trajectory in this example, the current observation year is 2012, and the last household structure event happened in 2009, with an increase in household size. The next household structure event occurs in 2013, with a decrease in household size. Thus, the episode duration for the time ago event is three years, and for the time future event is one year. The same applies to the car ownership

events. Considering the time dependency between these two life events, it becomes clear that the increase in household size has an anticipated effect on car acquisition, while the decrease in household size has a lagged effect on car disposal. It should be noted that time dependencies do not necessarily represent causal relationships between different life events.

Moreover, the external factors influence long-term and mid-term mobility decisions. At the micro-level, individual preferences and sociodemographic characteristics determine the order of life events in the life trajectory. At the macro-level, economic, social-cultural, and market circumstances constrain the choice set of individuals. Therefore, the formal modeling framework underlying this study is presented in Figure 2.

# 2.2 Modelling Approach 

Based on the aforementioned framework, a Bayesian Belief Network (BBN) was used to discover potentially causal relationships in the raw data, and predict the direct and indirect effects of actions and policies given the network structure. The advantages that make BBN attractive are: (1) More complex causal patterns can be included in the model to represent interdependencies between different life events. (2) Model results can directly describe the dynamic relationships between mobility decisions taken at different time points. (3) Causal relationships can be derived in a flexible way $(14,15)$.

Hugin software was used for learning the BBN. Two constraints-based algorithms are available for structure learning: the PC algorithm and the NPC algorithm (17). The basic mechanism is the same for these algorithms, i.e. they are all based on generating a skeleton derived through statistical tests for a set of conditional independence and dependence statements (CID). This study uses the NPC algorithm, as it covers the deficiencies of the PC algorithm and gives a better map of reality relations. The NPC algorithm provides ambiguous regions and interacts with the user to decide the directions for undirected links. Therefore, it is recommended to use the NPC algorithm (18).

Although the NPC algorithm is closer to reality, some deterministic links may still be counterintuitive. The reason is that causality is decided on a statistical basis, which may be counterintuitive if not logically possible. Therefore, this study superimposed some constraints (domain knowledge) to fasten the learning, simplify the structure and avoid invalid relationships (19). The constraints regarding the causal relationships provide a priori assumptions and conditions about the structure and direct effects for the network. In particular, on theoretical grounds, the following constraints are applied:

1. Age, as a personal attribute, is only allowed to have direct effects on employment/education events and household structure events.
2. Intra-domain relationships between time ago events and time future events, and the intra-relationships between different life events in the same life domain, are not considered in the BBN structure.
3. Household structure mobility cannot be decided by workplace/study location, residence location, and car ownership.
4. Car ownership events don't have direct effects on employment/education events and residential events. Moreover, residence location changes in the future cannot influence work location changes in the past.

During the parameter learning phase, the CPTs for all nodes in the BBN were specified. As there were some unobserved data, the Expectation-Maximization (EM) algorithm was used to deal with this problem. The EM algorithm tries to estimate the CPTs that maximize the log likelihood of the current joint probability distribution on the case data. The learning process terminates when the difference in log likelihood between two successive iterations reaches a value smaller than the convergence threshold (20). The convergence threshold was set to 1.0e-4.

# 2.3 Variables 

The selected variables are shown in Table 1. The state " 0 " means the event happens in the observation year, and this state only belongs to the time ago event. The state "never" means this kind of event has never happened. For example, there is no car in the family at the observation year, so this family cannot add or replace a car in the past, nor dispose of or replace a vehicle in the future.

## 3. SURVEY

### 3.1 Data Collection

In order to gather information about people's long-term and mid-term mobility decisions over the life course, longitudinal data was necessary. A retrospective approach was used in this study, asking respondents to recall their life events in chronological order. The survey was conducted at the household level, and the questionnaire recorded respondents' life course from when they were 18 years old. If a respondent arrived in Beijing when he/she was older, the respondent was requested to recall the life trajectory events from the time of arrival. The questionnaire content included both the state and life events in every calendar year during the respondent's observation period. Questions related to the four life events, shown in Table 1, include the total number of life events, the time (year) when the events happened, and what exactly was changed by these events. The sample size for present analysis is based on 294 questionnaires with 5251 observation years.

The design and visual presentation of web-based survey can increase the response efficiency and improve the quality of each answer (21). The data were collected in Beijing, China, covering 16 districts of 2 central urban districts (Xicheng and Dongcheng), 4 suburban districts (Chaoyang, Fengtai, Shijingshan and Haidian) and 10 outer suburb districts (Fangshan, Tongzhou, Shunyi, Changping, Daxing, Mentougou, Huairou, Pinggu, Miyun and Yanqing). Respondents have to be at least 19 years old, and have settled in Beijing more than one year by the time of the survey.

Age, gender and residential distributions of the sample in that year have been summarized in Table 2. It shows that Compared with the Beijing statistics of 2014 (22), the sample data are reasonably representative of the population of Beijing, except for the typical bias introduced by web-based samples.

### 3.2 Sample Description

The frequency statistics of the various life events are shown in Table 3. Out of 5251 observation years, a total of 365 workplace/study location changes occurred. Changes within suburban districts occurred more often ( $2.9 \%$ ) than the other places. That means the suburban districts, areas full of job-hopping, provide a lot of job and learning opportunities. Similarly, most residential events happened within the suburban or outer suburban districts. Moreover, car

acquisition took place more frequently than car disposal and replacement, and more families increased in size.

In terms of event occurrence in different life trajectories, the frequencies for residential relocation ( $8.9 \%$ ), work/education relocation ( $6.9 \%$ ), and household member changes ( $6.6 \%$ ) were much higher than changes in car ownership (3.9\%). Residential relocation happened more frequently than the other mobility aspects, which is in line with the actual situation of the metropolis in China.

In order to consider the time dependencies between different life events, the time intervals between two consecutive events in these four life trajectories are shown in Figure 3. It is worth noting that some events may occur in the same year, so the time interval is 0 . The results show that most life events in these four life trajectories occurred within two years, and the frequency distributions for these four life trajectories showed similar trends, except car ownership. That is because the changes in car ownership are not as frequent as other mobility aspects, and the respondents rarely had two or more consecutive car ownership changes during the observation period. More importantly, the discrete states of different life events, as shown in Table 1, are decided by the frequency distribution of time intervals.

# 4. RESULTS AND ANALYSIS 

### 4.1 Structure Learning

Hugin software was used to build and estimate the Bayesian Belief Network for life trajectories, using the input data and constraints described earlier. The level of significance was set to the standard value of 0.01 for the learning process. The causal relationships found in the learned network are shown in Figure 4 and Figure 5.

The direct and indirect relationships between life events can be found through these links. Based on the time property of the node, the temporal relationships are distinguished by lagged effects, contemporaneous effects, and anticipated effects. The link directed from the time ago node to the time future node refers to a lagged effect, while the reverse direction signifies an anticipated effect. Interrelationships within the same time domain are called the contemporaneous effect. These relationships are discussed below:

Relationships between external factor and life events: "Age" directly links to employment/education events and household structure events, which indicates that the specific mobility occurs at a specific age.

Relationships between car ownership events and other life events: car acquisition in the past was mainly affected by workplace/study location changes and residential location changes in the past. The employment/education event "Ep_outsuburban_suburban" and residential event "Rp_outsuburban_outsuburban" both have a contemporaneous effect on car acquisition in the past. It is understandable as a change in work location or residential location, that increases the daily commuting distance, leads to the necessity for a car. For car acquisition in the future, work location changes were seen to increase the number of family cars in the future, which can be explained as follows: the increase in salary with job-hopping allows people to earn enough money to buy a car. Residence relocation from urban district to suburban or outer suburban district also has direct effects on car acquisition in the future, because the greater travel distance induces people to consider buying a car in the mid-term. Moreover, an increase in household size, such as planning to have a baby, leads to car acquisition in the future.

Relationships between residential events and other life events: residential events seems to be mainly affected by household structure events and employment/education events. Compared

with other residential events, "Rp_suburban_suburban", "Rp_suburban_outsuburban", "Rp_outsuburban_suburban", "Rf_suburban_suburban", "Rf_suburban_outsuburban", "Rf_outsuburban_outsuburban" had more links. Work location events had contemporaneous and lagged effects on residence location events, and their locations after change fell into the same area. For example, "Ep_urban_outsuburban" was linked with "Rp_suburban_outsuburban", and "Ep_outsuburban_suburban" was linked with "Rf_suburban_suburban". Meanwhile, household structure events had lagged, contemporaneous, and anticipated effects on residential events.

Relationships between employment/education events and other life events: employment/education events were mainly decided by age, residential, and household structure events. Residential events had lagged and contemporaneous effects on employment/education events. More specifically, there was usually a synergic relationship between them, meaning the variation range for their changed locations is consistent, such as "Rp_urban_suburban" linked to "Ep_urban_suburban", "Rf_urban_outsuburban" linked to "Ef_urban_outsuburban. Moreover, an increase in household size had contemporaneous and anticipated effects on employment/education events. This is plausible in that people usually want to have sufficient economic security before having a baby or getting married.

Relationships between household structure events and other life events: the household structure cannot be influenced by other life events, so it was only affected by age. Based on the above analysis, household structure events had lagged, contemporaneous, and anticipated effects on residential, employment/education, and car ownership events. Compared to other life events, there are frequent links between household structure events and residential events. This means these two life trajectories have an intimate relationship between each other.

# 4.2 Parameter Learning 

Based on the network structure, the EM algorithm was used to estimate the CPTs for each node with the observed data. The estimated marginal probability distribution for every node is shown in Figure 6. In the structure learning analysis, the temporal effects can be divided into lagged effects, contemporaneous effects, and anticipated effects. Actually, contemporaneous effects also contain these three kinds of time attributes, if the states of the nodes are taken into account. To differentiate, they are expressed as lag effects, concurrent effects, and lead effects. These specific temporal relationships were not observed in the structure learning, but can only be found in the parameter learning.

One application of this network is to observe the direct and indirect dynamic relationships between the nodes of interest based on the process of simulation. Simulation refers to entering hard evidence into the network and compare the probabilities of certain nodes of interest with and without evidence. The hard evidence means a certain condition is known and the probability for this state is $100 \%$. When the hard evidence for one or more nodes is entered into the BBN, the probabilities for their related nodes, directly or indirectly, are updated.

In this study, we focused our interest on car acquisition in the future. In order to solve housing problems of low-income families, the Beijing government annually provides a batch of economically affordable housing to the public, usually located in the outer suburban districts. Structure learning showed that changing residence from urban district to suburban or outer suburban district will lead to car acquisition in the future. So the relationship between remote relocation and car acquisition in the future are analyzed in this study. The relative probability difference (the difference between the updated probability and initial probability divided by the

initial value) is used to describe the sign of the evidence effects, and the greater the relative difference, the greater the tendency is. The results are shown in Table 4.

The relevant residential events include three kinds of changes: moving from urban district to suburban district (Rf_urban_suburban), moving from urban district to outer suburban district (Rf_urban_outsuburban), and moving from suburban district to outer suburban district (Rf_suburban_outsuburban). The relative probability differences of car acquisition given evidence of residential events in the future are shown in Table 4. The analysis found that the life event "Rf_urban_suburban" has lag effects on car acquisition in the future. For example, the probability of car acquisition in three years later increases by $90.52 \%$ if the person decides to relocate from urban district to suburban district in one or two years. Likewise, the residential event "Rf_suburban_outsuburban" had similar effects on car acquisition in the future. For the residential event "Rf_urban_outsuburban", "three years" was a cut-off point. When this residential event happens one or two years later, the probability of car acquisition in four years increases by $78.45 \%$. However, if this residential event occurs three or more years later, car purchase is expected to happen simultaneously.

# 5. CONCLUSIONS 

Long-term and mid-term mobility decision processes constitute a complex system of interdependencies, in which life events of different life trajectories are interrelated and time dependent. Changes in one state may trigger various direct and indirect effects through the network. Very few studies have attempted to address the complexity of these decision dynamics. In this study, the Bayesian network approach was used to study the dynamic relationships between consecutive long-term and mid-term mobility decisions over the life course, covering four life trajectories: changes in residence, changes in household structure, changes in employment/education, and changes in car ownership.

The model results provide evidence to confirm the interdependencies between different life events. Considering their causal relationships, the main reasons for car acquisition are the increase of household size, workplace/study location changes, and residential relocation. These are related to the changing of family needs and travel demand. Residential events were closely related to and interacted with employment/education events. Moreover, a synergic relationship was established between these two life trajectories. Household structure events have direct effects on the residential, employment/education, and car ownership events. Compared to other life events, household structure trajectory and residential trajectory have a more intimate relationship with each other.

In terms of temporal relationships, lagged, contemporaneous, and anticipated relationships exist between various life events. Most importantly, changes in household structure have contemporaneous and anticipated effects on residence location events, while an increase in household size has contemporaneous effects on car acquisition in the future. Moreover, more detailed temporal relationships are found from the contemporaneous effects, after considering the timing of the last and the next life events. Residential relocation has a lag effect on car acquisition in the future, if the person expects to move from urban district to suburban district or from suburban district to outer suburban district. This phenomenon is logical: car acquisition and changing house are both big expenditures for a family, which cannot be achieved at the same time. Moreover, when people anticipate a change in workplace/study location from urban district to suburban or outer suburban district in three or more years, it has concurrent effects on car acquisition in the future.

Although this study has established multiple causal and temporal relationships, it still have several limitations and extensions. First, the learned network structure is built on individual life trajectories, without considering interaction between household members. Therefore, it is not guaranteed that the current model consistent for members of the same family. Second, the interrelationships between various life events will change with the means of transportation, spatial and economic context. It would be an interesting extension to study behavioral adaption to new policies or context changes.

# ACKNOWLEDGMENTS 

This work was supported by the National Natural Science Foundation of China (Grant No. 51678044) and Science Fund for Creative Research Groups of the National Natural Science Foundation of China (Grant Number 71621001).

## AUTHOR CONTRIBUTION

The authors confirm contribution to the paper as follows: study conception and design: Bobin Wang, Soora Rasouli, Harry Timmermans; data collection: Bobin Wang, Chunfu Shao; analysis and interpretation of results: Bobin Wang, Soora Rasouli, Harry Timmermans; draft manuscript preparation: Bobin Wang, Harry Timmermans, Chunfu Shao. All authors reviewed the results and approved the final version of the manuscript.

# LIST OF FIGURES 

FIGURE 1 Relationships between household structure events and car ownership events.
FIGURE 2 Modeling framework for data analysis.
FIGURE 3 Frequency distribution of the time interval between two consecutive life events.
FIGURE 4 Learned life trajectory network.
FIGURE 5 Learned life trajectory network.
FIGURE 6 Estimated marginal probability distributions for Bayesian Belief Network.

## LIST OF TABLES

TABLE 1 Explanation of Variables
TABLE 2 Sample Distribution
TABLE 3 Frequency Statistics of the Long-Term and Mid-Term Mobility Decisions
TABLE 4 Relative Probability Difference of Car Acquisition Given Evidences of Residential Events in the Future

![img-0.jpeg](img-0.jpeg)

FIGURE 1 Relationships between household structure events and car ownership events.

![img-1.jpeg](img-1.jpeg)

FIGURE 2 Modeling framework for data analysis.

TABLE 1 Explanation of Variables


TABLE 2 Sample Distribution


TABLE 3 Frequency Statistics of the Long-Term and Mid-Term Mobility Decisions


![img-2.jpeg](img-2.jpeg)

FIGURE 3 Frequency distribution of the time interval between two consecutive life events.

![img-3.jpeg](img-3.jpeg)

TRB 2018 Annual Meeting

![img-4.jpeg](img-4.jpeg)

# FIGURE 5 Learned life trajectory network.

![img-5.jpeg](img-5.jpeg)

FIGURE 6 Estimated marginal probability distributions for Bayesian Belief Network.

TABLE 4 Relative Probability Difference of Car Acquisition Given Evidences of Residential Events in the Future
