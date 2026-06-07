# Unveiling the Causal Mechanisms within Multidimensional Poverty 

Hernando Grueso ( $\square$ hrg43@comell.edu )<br>The George Washington University https://orcid.org/0000-0003-0534-071X

## Research Article

Keywords: multidimensional poverty, violence, impact evaluation, complex causality, Bayesian networks, instrumental variables

Posted Date: August 2nd, 2022
DOI: https://doi.org/10.21203/rs.3.rs-1882302/v1
License: (0) This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License

# Unveiling the Causal Mechanisms within Multidimensional Poverty 

July 2022


#### Abstract

This paper combines machine learning and econometrics to explore the relationship between multidimensional poverty components and violence in Colombia. First, I create a directed acyclic graph (DAG) using Bayesian networks and census data to predict how multidimensional poverty components are interrelated. I find that minimum living standardsmeasured in terms of access to water, connection to the sewage system, and the quality of walls and floors-are strong predictors of the education and health dimensions of poverty. Second, I use the DAG output to identify potential instrumental variables (IV) that may be used to test the effect of multidimensional poverty on a household's likelihood to be a victim of violence. Illiteracy is predicted by a complex set of poverty indicators in the DAG, yet it seems to be the only connecting point between multidimensional poverty and violence showing potential to meet the validity assumptions in an IV approach. Using 2SLS, I show that having an illiterate person within a household increases by $0.4 \%$ the household's likelihood to be a victim of violence.


Key Words: multidimensional poverty, violence, impact evaluation, complex causality, Bayesian networks, instrumental variables

## 1. Introduction

A growing interest in multidimensional poverty has motivated its use in impact evaluations (e.g., Mitchell \& Macció 2021; Vaz, Malaeb \& Quinn 2019; Song \& Imai 2019; Seth \& Tutor 2018; Malaeb \& Uzor 2017). However, there is no consensus on how to conduct impact evaluations with multidimensional outcomes. Variations in the outcome can be driven by one of its dimensions, multiple dimensions, or the interaction between

them. Complexity science is an emergent field of interest within program evaluation that precisely studies nonlinear causality, where an outcome is explained by the interaction between multiple variables (e.g., Patton, 2011; Pawson; 2013; Bamberger, Vaessen, and Raimondo, 2015; Williams \& Hummelbrunner, 2010). There is still no consensus on how to conduct impact evaluations looking at such complex causal relationships. This paper responds to both gaps in the literature, by introducing a methodological framework to study complex causality in development economics that can also help to understand the drivers of multidimensional poverty. This framework is part of an emergent effort to bridge econometric designs for causal inference with machine learning techniques used for prediction (e.g., Athey 2019; Mullainathan \& Spiess 2017).

The contribution of this paper comes from a methodological and an empirical perspective. From a methodological perspective, this paper provides the first attempt to combine machine learning and econometrics for the purpose of complex causal inference. The empirical strategy shows a way to combine popular methods used for causal inference in economics with computer science methods used for prediction. From an empirical perspective, this paper provides new insights to understand how multidimensional poverty indicators interact with each other.

I focus on eleven indicators used by the Colombian government to calculate the Multidimensional Poverty Index (MPI). These variables indicate whether a household is below the minimum standards in terms of child labor, school attendance, school achievement, literacy, access to plumbing water, connection to the sewage system, overcrowding, unemployment, access to healthcare, and the quality of floors and walls. Evidence worldwide shows that multidimensional poverty indicators are often correlated

raising questions on whether they are complements or substitutes (e.g., Alkire et al., 2015; Dotter \& Klasen, 2017; Alkire \& Fang, 2018). This paper sheds light into that direction, suggesting that these correlations might be driven by causal connections between poverty indicators, and that these connections vary depending on the context. For example, I show that in the Colombian case, the relationship between MPI indicators is different when comparing urban and rural households.

The purpose of this paper is to study the drivers of multidimensional poverty in Colombia. This is, understanding to what extent the MPI indicators interact with each other. As a case study, I also analyze the relationship between violence and the set of MPI indicators. To do so, I identify which of these poverty indicators have a direct relationship with violence and then I test the causality of this relationship. I use census data from Colombia (2018) to conduct the analysis and focus on the sample of all the poor households in the country.

The empirical strategy is divided into two steps. First, I calculate a Directed Acyclic Graph (DAG) using Bayesian networks (BN) to describe predicted causal connections between MPI indicators. I use a "hill climbing" machine learning algorithm to predict these connections and then calculate the Bayesian network (BN). The BN uses conditional probabilities to define the predicted causal connections between variables. Second, I use the DAG output to identify instrumental variables (IV) that could help assessing the causal relationship between violence and specific MPI indicators. In doing so, I look at MPI differences between urban and rural households.

The first main result is that living standard indicators seem to be the main drivers of multidimensional poverty. Indicators such as access to water supply, connection to the

sewage system, and the quality of walls and floors, seem to predict other outcomes such as unemployment, school achievement, literacy, and access to healthcare. Another root indicator is child labor which is unrelated to minimum living standards and predicts school attendance, unemployment, and access to health case. The second main result is that there seems to be a lot of endogeneity among MPI indicators making it difficult to disentangle direct causal links. The third result is that having an illiterate family member within a household located in an urban area, predicts the household's likelihood to be a victim of violence. I test this causal claim using a set of six IVs and find that illiteracy increases by 0.4 percentage the likelihood of the household to be a victim of violence. Even though this is a small effect, it provides an example of how to use BNs to identify and validate IVs. The identification of instrumental variables is a challenging task and BNs can help to test the reliability of an instruments. In the Colombian case, I did not find any other good IV candidates within the MPI due to endogeneity issues. Also, once controlling for all the MPI indicators, I did not find a correlation between MPI and the likelihood to be a victim of violence in rural areas.

This paper is divided into six sections including this introduction. The second section provides background on the concept of multidimensional poverty. The third section describes the data including the definition of variables, sample restrictions, and descriptive statistics. The fourth section contains the empirical strategy and results of the machine learning approach. This includes background on Bayesian networks (BN) and the analysis of MPI indicators. The fifth section corresponds to the econometric approach, including the definition of the IV design based on the BN findings and a summary of results. Finally, the sixth section concludes with a discussion of policy recommendations.

# 2. Multidimensional Poverty 

The concept of multidimensional poverty is influenced by Amartya Sen's theoretical framework. According to Sen, poverty should be understood as a deprivation of capabilities that are related to "[...] our ability to achieve various combinations of functionings that we can compare and judge against each other in terms of what we have reason to value" (Sen 2009, p. 233). These functionings can be described as individual goals, and the capabilities as the actual possibilities to achieve those goals. This definition makes a distinction between suspected means for development, like money, and actual means such as education, health, and living standards. Therefore, education is understood as a poverty dimension itself and as a criterion for poverty measurement.

Poverty dimensions are considered as human development areas, and they can be measured according to specific poverty indicators that are proxies to capture the degree of development in those areas. For example, indicators such as school achievement or school attendance could be good proxy to capture the degree of development in the education dimension of poverty.

## Multidimensional Poverty Measurement:

The most influential poverty measurement inspired by Sen's framework is perhaps the Global Multidimensional Poverty Index (MPI) based on the Alkire-Foster (AF) Counting Methodology—also known as $M_{\alpha}$ (Alkire \& Foster, 2011). The Global MPI is calculated every year by the United Nations Development Programme (UNDP) taking three dimensions into consideration: education, health, and standard of living. A similar definition also based on the AF methodology is the Colombian MPI that considers five dimensions: education, health, housing, work, and childhood \& youth. Table 1 provides a

comparison between both definitions including the different indicators within each poverty dimension, cut-off lines, and weights assigned to each indicator. In this analysis, I use an approximation to the Colombian MPI definition based on census data from 2018. This approximation uses eleven indicators from a total of fifteenth indicators listed in Table 1.

The multidimensional approach follows the same logic of income-based poverty measures. In the same way, in which simpler measures classify people between poor and non-poor based on one indicator (e.g., income) and one cut-off line (e.g., $\$ 1.90$ per day), the multidimensional approach uses multiple indicators and multiple cut-offs to make the same classification. For example, based on the information in Table 1, the global MPI states that a household is considered deprived of education if "no household member aged 10 years or older has completed six years of schooling" (UNDP, 2019). After assessing a household's deprivations based on all the defined indicators, a weight is assigned to all the cases in which the household is below the minimum standards. ${ }^{1}$ Then all the weights are added up in an MPI score that is compared against a cross-dimensional cut-off line. Both the Global and the Colombian MPI definitions, consider a conventionally used crossdimensional cut-off line of $1 / 3$, meaning that a household is considered multidimensional deprived (or poor) if its total MPI score is greater than $1 / 3$.

Although the MPI seems to be a less straightforward method for poverty measurement - compared to conventional unidimensional approaches, it represents a more accurate approximation to picture human development. Empirical results show a mismatch between income-based and multidimensional poverty measures, indicating that

[^0]
[^0]:    ${ }^{1}$ The Global and the Colombian MPI definitions assign equal weights to all of the dimensions. This means that each of the three dimensions in the Global MPI get a $1 / 3$ weight, and that each of the five dimensions in the Colombia MPI get $1 / 5$ weight. These weights are then equally divided between the available indicators within each dimension.

multidimensional poor people are not necessarily monetarily poor. This means that people living with more than $\$ 1.90$ per day might not have access to adequate living standards, health, and education, undermining in that way the value of income as a proxy for development. The empirical evidence for this mismatch is available for countries such as Ethiopia, India, Peru, Vietnam (Kim, 2019; Roelen, 2017), Rwanda (Salecker, Ahmadov \& Karimli, 2020), Germany (Suppa, 2016), and China (Alkire \& Shen, 2017).

The policy implications of this mismatch are reflected in the type of government initiatives to reduce poverty based on different evaluation criteria. For example, in the case of Vietnam, where less than fifty percent of the monetary poor people are also multidimensionally poor, GDP growth easily translates into monetary poverty reduction but not necessarily into MPI reduction (Tran, Alkire \& Klasen, 2015). Having the MPI as an evaluation criterion, incentivizes governments to implement programs and policies intended to promote the overall levels of education, health, and living standards.

Understanding the causal mechanisms within multidimensional poverty can help to explain the mismatch between monetary and multidimensional poverty. This new insight can also help to improve the design of cost-effective policy interventions to reduce multidimensional poverty.

# Multidimensional Poverty and Violence: 

As a case study to put into practice the empirical strategy in this paper, I am interested in studying the relationship between multidimensional poverty and violence. This is an underexplored area in the literature. Alkire (2007), for example, talks about "physical safety" as one of the missing dimensions in multidimensional poverty. By this dimension, the author refers to violence as the main threat affecting a person's security.

The exclusion of this dimension is in part due to the lack of comparable data across countries; however, Alkire indicates that the missing dimensions are often implicitly measured in their causal connections with the existing ones. For instance, the author notes that "the lowest ranking countries in terms of the $\mathrm{HDI}^{2}$ are countries in or emerging from violent conflict" (p.350). Violence, therefore, might have a direct effect on multidimensional poverty by decreasing the living standards and access to social services such as health and education. This could be the case if people are afraid to leave their homes, travel to work or school, or obtain health care under threat of violence in their community. In such a scenario, it makes sense to study the extent to which changes in levels of violence affect multidimensional poverty components.

Mahadevan \& Jayasinghe (2019) conduct the first empirical attempt to understand the relationship between violence and multidimensional poverty in the case of Sri Lanka. The authors study the transition from war to peace after 30 years of ethnic war in the country and find a reduction in MPI and its components during this transition. Nevertheless, this evidence is not conclusive because the authors do not control for the problem of endogeneity in the data.

In the case of monetary poverty measures, there is evidence about the relationship between poverty and violence. This relationship has often been described as a vicious cycle in which violence produces poverty and poverty produces violence (Justino 2012). International evidence also suggests that monetary poverty increases the risk for armed

[^0]
[^0]:    ${ }^{2}$ The Human Development Index (HDI) was created as an alternative measure of a country's development that focuses on the people while also taking into account the economy. Three main components define this measure: life expectancy at birth, average years of schooling, and income per capita. The HDI corresponds to the average of these three indices (HDR, 2019).

conflict (Blattman \& Miguel, 2010) and this evidence is also available for Colombia (CottePoveda, 2011).

Even though there are no direct studies about the relationship between MPI and violence in Colombia, there are studies looking at the causal effect of violence on different MPI components. In the case of living standard indicators, some studies have reported negative outcomes in terms of human displacement and the loss of assets (Ibáñez \& Moya 2010; Ibáñez \& Moya 2006; Ibáñez 2008). In the case of education, some of these studies have reported a lower degree of educational attainment in conflict zones (Wharton \& Uwaifo Oyelere, 2011), a decrease in public expenditure on education (to compensate for higher policing expenses), physical obstacles to attending schools, and the death of family members forcing children to abandon school at an early age (Fergusson, Ibáñez, and Riaño, 2019). This paper provides new evidence on the ways in which violence can affect multidimensional poverty in Colombia.

# 3. Data 

In this study, I use data from the 2018 Colombian Census conducted by the National Department of Statistics (DANE). This is a cross-sectional dataset, at the household level, and including most of the variables required to calculate the official Colombian MPI. Furthermore, I calculate a proxy for victims of violence. This proxy indicates those households with a deceased man between 15 and 50 years old who passed during the last year. Interpersonal violence is the main cause of death among males in that age range in Colombia, which is equivalent to approximately 55\% of all the deaths (WHO, 2018). Even though not perfect, this proxy represents the best available guess to indicate which

multidimensionally poor households are likely to have been victims of violence in the country.

Besides the violence proxy, I use eleven poverty indicators $(1,0)$ in this analysis. Five of them are living standards variables indicating whether a household is overcrowded or deprived in access to water, sewage system connection, and the quality of floors and walls. Overcrowded households are those where the number of people per bedroom is greater than two. Water and sewage deprivation indicates that the household does not have a connection to the local water supply and sewage system respectively. Deprivation of floors indicates that the main material of the household's floors is dirt, and deprivation of walls indicates that the household has walls made from raw wood, vegetable material, zinc, cardboard, or no walls at all.

Three variables are classified within the education dimension of poverty: illiteracy (literacy_d), low school achievement (school_achievement_d), and low school attendance (school_attendance_d). Illiteracy indicates those households with at least one member who does not know how to read or write. Low school achievement indicates those households where there is at least one person with less than nine years of schooling and who is older than 15 years. Low school attendance indicates those households where at least there is one individual between 6 and 16 years old who is not attending school.

Two variables are classified within the work dimension: child labor and unemployment. Child labor (child_labor_d) indicates those households where at least one person is younger than 16 and worked at least one hour during the last week. This work includes paid and non-paid work at a business place. Unemployment (employment_d)

indicates those households with at least one person who searched for jobs during the last week.

Finally, one variable is classified within the health dimension. Access to health care ( sick_d) indicates those households where at least one person was sick during the last three weeks and did not receive adequate medical treatment. For example, this includes the case of people treated by a local indigenous healer.

The total sample size is approximately 8 million observations at the household level excluding missing values. I create some sample restrictions to study the relationship between MPI indicators. First, I only take into consideration poor households defined as those with a multidimensional poverty index greater than $1 / 3$. This helps me to only study variations in multidimensional poverty indicators of already poor households. Otherwise, I would be comparing poverty indicators between poor and non-poor households. Second, I divide the data into two samples, one for rural areas and another one of urban areas. The main rational for this separation is to acknowledge that the nature of urban poverty is different from rural poverty.

Table 2 shows descriptive statistics on the key variables included in the analysis. Approximately $0.2 \%$ of the households have child labor and $12 \%$ have some sort of unemployment. Within the living standards dimension, approximately 9\% households do not have access to water, $18 \%$ have no connection to the sewage system, $5 \%$ do not have adequate floors, $4 \%$ do not have adequate walls, and $6 \%$ of them are overcrowded. Within the education dimension, $10 \%$ of the households are deprived in literacy, $58 \%$ are deprived in school achievement, and $1 \%$ are deprived in school attendance. Only $3 \%$ of the households are deprived in access to health care and $2 \%$ seem to be victims of violence

according to the violence proxy. Finally, $13 \%$ of the households are in rural areas and the combination of all the above indicators suggests that $5 \%$ of them are multidimensionally poor.

# 4. Empirical Strategy: Machine Learning Approach 

The guiding research question in this paper is to what extent do multidimensional poverty indicators interact with each other? This is an exploratory question intended to approximate the complex causal pathways within MPI. Once those connections are identified, a secondary research question is which MPI indicators mediate the effect of being multidimensionally poor on the likelihood to be a victim of violence? The main hypothesis is that, conditional on all the MPI indicators, access to education is the main mechanism explaining the relationship between violence and multidimensional poverty. Furthermore, I explore MPI differences between urban and rural areas when answering these questions.

The empirical strategy to test this hypothesis integrates a machine learning approach to predict causal links with an econometrics approach to test the causality between those links. In the first step, I use Bayesian networks (BN) to predict the causal connections between MPI indicators. In the second step, I use the BN output to identify instrumental variables (IV) that can help me to test the causal effect of MPI indicators on violence.

### 4.1 Background on Bayesian Networks

BN are probabilistic graphical models that describe causal patterns between variables in complex systems via a directed acyclic graph-DAG (Rebane \& Pearl 1987). This analytical tool developed by Pearl (1982) played a central role in the emergence of

machine learning and is a useful way to predict complex causal behavior (Pearl \& Mackenzie 2018). Two main assumptions characterize BNs. First, a probabilistic theory of causality where causal effects are described as the probability of an event occurring and not in terms of counterfactuals (Hitchcock 2018). Second, the Markov condition according to which the variables (or nodes) in the network are conditionally independent of each other (Cartwright 2007). In some sense, BNs are analogous to structural equation models—SEM (Druzdzel \& Simon 1993). The main difference is that while SEMs allow estimating parameters with the size of a causal effect, BNs are non-parametric structural models that predict the direction of a causal relationship. The main advantage of BNs is that there is almost no limit to the level of complexity in the analysis. Using machine learning, it is possible to predict complex causal connections without simplifying the number of meaningful variables in the analysis. Then, these meaningful connections can be tested using SEM or other econometric approaches to causal inference.

BNs are common analytical tools in computer science but virtually unexplored in economics. In an attempt to understand this gap, the recent Nobel Prize winner in economics, Guido Imbens, compares the effectiveness of DAGs against conventional econometric approaches to causal inference (Imbens, 2020). First, the author points out that the conditional probabilities used in DAGs are analogous to OLS regressions with multiple controls. Second, he indicates that a clear advantage of DAGs is that they allow approaching complex causality and the causality of non-manipulable variables (e.g., gender or parent's education). Third, he identifies that while structural equation models in econometrics are based on theory, they are based on machine learning in DAGs. Fourth, he states that another important difference is that DAGs focus on identification rather than on

inference. Fifth, another difference is that is that DAGs are not cyclical while economics tends to be cyclical (e.g., when supply goes up, prices go down). Finally, the author concludes that the lack of value of DAGs in economics comes from the lack of clear examples on how to use them.

I believe that the study of multidimensional poverty represents a good example on how to use DAGs in economics and their complementarity with econometrics. Following Imbens, this complementarity lies precisely in understanding that DAGs are good for identification while econometrics is good for inference. I do not think DAGs are better but good complements of quasi-experimental design for causal inference such as regression discontinuity, synthetic controls, and instrumental variables. Furthermore, this paper helps to bridge the communication gap between computer science and economics for the purpose of complex causal inference.

# 4.2 Calculation of Bayesian Networks 

I follow a four-step procedure to calculate the BNs. First, I predict the causal structure within a set of meaningful variables using a hill-climbing learning algorithm. This set of variables is chosen according to a theoretical framework that corresponds to the MPI definition used in this study and a proxy to indicate which households are victims of violence. Second, I calculate conditional probabilities to describe the relationship between variables within the BN. Third, I choose a probability threshold to define which of the identified connections should be considered as meaningful links (or edges) in the network -this probability threshold is also known as the ark strength. And fourth, I plot the BN (or DAG) based on a joint probability distribution. I use the 'bnlearn' library in R to perform these four steps. The example below helps to illustrate this four-step procedure.

# 4.3 Example on How to Calculate Bayesian Networks 

Bayes theorem is the main reference point to calculate conditional probabilities in the BN. Supposing two dummy variables (or nodes) in the network, known as deprivation in access to healthcare (sick_d) and years of schooling (school_achievement_d), Bayes theorem indicates that

$$
P(\text { sick_d } \mid \text { school_achievement_d })=\frac{P(\text { school_achievement_d } \mid \text { sick_d } * P(\text { sick_d })}{P(\text { school_achievement_d })}
$$

This conditional probability does not necessarily imply a causal direction and in fact, it can be re-expressed as

$$
P(\text { school_achievement_d } \mid \text { sick_d })=\frac{P(\text { sick_d } \mid \text { school_achievement_d } * P(\text { school_achievement_d })}{P(\text { sick_d })}
$$

In the context of multiple variables and big data, it is virtually impossible to manually calculate all the possible conditional probabilities in a dataset to predict which patterns repeat the most suggesting a causal trend. This would be the case if, for example, we find that most of the households that are deprived in school achievement are also deprived of access to healthcare but not the other way around, which suggests a causal effect of school achievement on healthcare. However, this assessment becomes more difficult if we add other variables such as deprivation in a living standard indicator such as the quality of walls (walls). Machine learning becomes handy when using multiple variables in the analysis. Using a hill-climbing learning algorithm, I can predict the causal direction between multiple MPI indicators. This algorithm predicts which patterns repeat the most and then the BN is calculated based on the following joint probability distribution:

$$
P(\text { multidimensionally_d })=\prod_{i=1}^{n}\left(\text { MPI_Indicator_d }_{i} \mid \text { MPI_Indicator_d }_{j(i)}\right)
$$

Where $P$ (multidimensionally_d) is the probability of being multidimensionally deprived (or poor), which is equal to the product of being deprived in the $i$ poverty indicator (MPI_Indicator_d $\left.d_{i}\right)$ given the rest of poverty indicators affecting $i$ (MPI_Indicator_d $\left.d_{i(i)}\right)$. In the case of the previous example, the conditional probability of being multidimensionally deprived could be expressed as
$P\left(\right.$ walls, school_achievement_d, sick $\left._{d}\right)=P($ walls $) * P($ school_achievement_d $\mid$ walls $) * P($ sick_d $\mid$ walls $)$
The BN DAG could be expressed in the following way according to the above joint probability distribution:
![img-0.jpeg](img-0.jpeg)

This DAG represents the predicted causal structure in which deprivation in walls (walls) directly affects deprivation in school achievement (school_achievement_d) and deprivation in access to healthcare (sick_d). Plotting this graph also requires deciding on the arc strength, which is a minimum probability threshold indicating which "predicted causal" connections should be considered as meaningful. This probability threshold goes from 0 to 1 and it is analogous to a statistically significant relationship. There is no consensus on what represents a reliable minimum threshold when calculating BNs, but I use an arc strength of 0.99 in this study to decide which are meaningful connection between MPI indicators.

Now, to illustrate how BN can help to uncover complex causality let us suppose that violence is another meaningful variable in the network.

![img-1.jpeg](img-1.jpeg)

This network suggests that multidimensional poverty has a direct effect on violence via school_achievement_d. If this is the only connecting point between the system of MPI indicators and violence, then walls would meet the validity assumptions to be treated as an IV. These assumptions indicate that walls is not correlated with violence, and that it has an effect on violence via its effect on school_achievement_d.

# 4.4 Multidimensional Poverty Index 

To keep consistency in the analysis of multidimensional poverty, I only include multidimensionally poor households into the calculation of Bayesian Networks. This helps me to only study the relationship between MPI indicators within already poor households. Otherwise, I would be including MPI indicators of non-poor households who might have a different relationship between variables (e.g., a non-poor household can still have floors made from raw wood).

I calculate a Multidimensional Poverty Index (MPI) to identify poor households using the Alkire-Foster (AF) methodology (Alkire and Foster, 2011) and according to the official Colombian multidimensional poverty definition ${ }^{3}$. The following equation calculates

[^0]
[^0]:    ${ }^{3}$ I use a close approximation to the official Colombian MPI definition that can be calculated using census data. This close approximation uses 11 out of the 15 indicators used to calculate the official national MPI. I use census data instead of the annual household survey on living standards (used to calculate the Colombian MPI), because the national census has a larger number of observations that gives me more statistical power to calculate the Bayesian network. Furthermore, the national census includes information on mortality at the household level which allows me to calculate the proxy to identify which household are likely to be victims of violence.

a multidimensional poverty score assigning equal weights to each of the four dimensions of poverty: education, work, health, and living standards,

$$
\begin{aligned}
\text { MPI Score }_{i} & =0.1 * \text { Literacy }_{d}+0.1 * \text { School_Achievement_d } \\
& +0.1 * \text { School_Attendance_d }+0.1 * \text { Child_Labor } \\
& +0.2 * \text { Employment_d }+0.2 * \text { Sick_d }+ \\
& +0.04 * \text { Water }+0.04 * \text { Sewage }+0.04 * \text { Floors } \\
& +0.04 * \text { Walls }+0.04 * \text { Overcrowding }
\end{aligned}
$$

Poor households are classified as those with an MPI score greater than $1 / 3$. In the second part of the empirical strategy, I calculate the IV regressions using the sample without restrictions (including poor and non-poor observation), using separate samples for rural and urban households, and using separate samples for poor households located in rural and urban areas.

# 4.5 Results 

Figure 1 provides the first attempt to model the causal structure within multidimensional poverty in urban areas of Colombia using a Directed Acyclic Graph (DAG). What is novel about this DAG, is that it is calculated using machine learning instead of a theoretical approach. Using an arc strength of 0.99 (analogous to a significance level of 0.01 ), the Bayesian network results suggest that living standard indicators-such as access to water, sewage system, quality of the walls and floors-are the main drivers of multidimensional poverty predicting other MPI indicators in the education and health dimensions. Deprivation in living standards indicators seems to predict a household's deprivation in employment, school achievement, literacy, and access to healthcare (sick_d).

An example to understand the probabilistic approach to causality in Figure 1, is that households deprived in access to water, sewage system connection, quality of floors and walls, overcrowding, and literacy, also seems to be deprived in access to healthcare but not

the other way around. This means that households without access to healthcare are not necessarily likely to be deprived in living standard indicators. That is the reason why the DAG predicts a causal effect from living standards to health indicators and not in the opposite direction.

Figure 1 also shows that the presence of child labor within a household predicts school absenteeism (school_attendance_d) and that this relationship is independent of minimum living standards. The multiple arrows coming out of each node (or MPI indicator) in Figure 1, show a high degree of endogeneity among MPI indicators and therefore, it is not possible to select a good IV candidate out of this graph.

Figure 2 shows the same results but for the specific case of rural households in Colombia. The results are very similar, but it is less clear here that living standards are the main drivers of multidimensional poverty. Deprivation in access to water, the quality of floors, and walls, seem to predict other MPI indicators such as school achievement, school attendance, and literacy. However, the presence of child labor also seems to predict school attendance and the quality of floors. There seems to be more endogeneity between MPI indicators in the case of rural households.

An interesting key difference between urban and rural MPI, is that access to healthcare (sick_d) seems to only predict unemployment in rural areas of Colombia. Households without access to healthcare are classified as those where at least one person was sick during the last three weeks and did not receive adequate medical treatment. Considering that employment among poor households in rural areas involves physical labor, it makes sense to think that adequate physical health is a requirement to secure a job. Like in the case of urban areas, there are no good candidates for IVs in Figure 2.

Figure 3 displays the same information in Figure 1 but including the violence proxy. The first interesting finding is that including this variable does not alter the relationship between MPI indicators described in Figure 1. The second interesting finding is that illiteracy (literacy_d) predicts a household's likelihood to be a victim of violence (violence_proxy). This is the only connection between MPI indicators and the violence proxy, suggesting that the variables only affecting literacy_d - such as overcrowding, walls, floors, unemployment, and school achievement-are good IV candidates to test the causal effect of literacy_don violence_proxy.

Identifying instrumental variables is a challenging task and Bayesian networks are not perfect shortcuts to overcome this challenge. A key identifying assumption is that the instrument should not be correlated with the outcome of interest. Despite the lack of theoretical background to understand why the different instruments suggested in Figure 3 might be unrelated to violence_proxy, this machine learning approach uses conditional probabilities to support the identification of IVs. An important caveat is that these conditional probabilities are as good as the data included in the BN. Other relevant variables that might be excluded from this analysis are not considered in the assessment of this IV strategy. In the case of rural areas, Figure 4 shows that MPI indicators seem to be unrelated to violence_proxy. This means that none of the indicators are good predictors of violence at the 0.01 confidence level.

# 5. Study Case: Econometric Design and Results 

Using the results in Figure 3, the econometric strategy in this paper is defined by a 2SLS regression where the first stage corresponds to the following equation,

$$
\text { Illiteracy }_{i}=\lambda_{0}+\lambda_{1} \boldsymbol{Z}_{i}^{\prime}+\lambda_{2} X_{i}^{\prime}+\varphi_{i}+\mu_{i}
$$

Where the outcome is a dummy indicating which households have at least one family member who does not know how to read or write (Literacy_d ${ }_{i}$ ), $Z^{\prime}{ }_{i}$ is the vector of instrumental variables identified in Figure 3—overcrowding, school_achievement_d, employment_d, water, sewage, and floors- $\boldsymbol{X}_{i}^{\prime}$ is a vector of control variables including other relevant MPI indicators, whether the household is located in a rural area, and the households' social stratification scale ( $1=$ lowest income -6 =highest income); $\varphi_{i}$ the municipality fixed effects, and $\mu_{i t}$ is the error term.

Using the results from the first stage, the second stage is estimated based on the following equation:

$$
\text { Violence_Proxy }_{i}=\alpha_{0}+\alpha_{1} \text { Illiteracy }_{i}+\alpha_{2} X_{i}^{\prime}+\varphi_{i}+\varepsilon_{i}
$$

Where Violence_Proxy ${ }_{i}$ is a dummy indicating which households are likely to be victims of violence. According to the BN in Figure 3, the hypothesis to be tested in this IV design is that having an illiterate person within a household increases the household's likelihood to be a victim of violence.

Table 3 shows the results of the IV approach to test the causal effect of literacy on the violence proxy. Columns 2 and 3 show that once controlling for municipality fixed effects and the rest of MPI indicators, having an illiterate person within a household increases its likelihood to be a victim of violence by approximately 0.2 percentage points. This coefficient is statistically significant at the 0.001 level and calculated using clustered standard errors at the municipality level. The first stage in column 1 also shows statistically significant coefficients with an F-statistic of 611,400.7.

Robustness checks are conducted in Tables 4 and 5. Both tables conduct the same empirical strategy but using the restricted samples used to calculate the BN in Figure 3.

Table 4 uses the sample of urban households and Table 5 the sample of poor urban households. Both tables replicate the main results, with a slightly higher coefficient of $0.4 \%$ in Table 5 which describes the effect of illiteracy on the likelihood to be a victim of violence. Even though a small effect, the results in Tables 2, 4, and 5 represent good examples on how to use Bayesian networks to support the identification of instrumental variables in a complex system.

# 6. Conclusions and Policy Recommendations 

Conventional experimental and quasi-experimental methods in economics are limited in their possibility to study complex causal inference. Combining machine learning and econometrics opens a new door for complex causal inference. The empirical strategy in the paper shows an example on how to approximate complex causal inference using Bayesian networks (BN) for the identification of instrumental variables (IV). First, I calculate a Directed Acyclic Graph (DAG) using a machine leaning approach to Bayesian networks. Second, I identify IVs in the DAG to test the causal relationship between multidimensional poverty and violence. The results suggest that having an illiterate person within a household increases its likelihood to be a victim of violence by approximately $0.4 \%$. This result is statistically significant, robust to different sample restrictions, and represents a good example on how to tackle complex causal inference by integrating machine learning into quasi-experimental econometric designs.

Besides the above methodological contribution, the BN analysis in this paper provides new insights on how multidimensional poverty indicators interact with each other. An open debate in the literature is to what extent are MPI indicators complements or substitutes (e.g., Alkire et al., 2015; Dotter \& Klasen, 2017; Alkire \& Fang, 2018). Based on

the results discussed here, I state that these indicators seem to be interrelated. This means that each of them seem to be affected by changes in other MPI indicators. The does not necessarily resolve the issue on whether they are complements or substitutes, but rather, shows how improvements in one dimension can lead to positive spillover effects on other dimensions. Differences between BNs in urban and rural areas also show that the relationship between MPI indicators changes depending on the context.

Minimum living standard indicators-such as access to water, connection to the sewage system, and the quality of walls and floors-seem to be the main drivers of multidimensional poverty in urban areas of Colombia. These variables predict the outcome of other MPI indicators such as employment, school achievement, and access to healthcare. Child labor is another key predictor in the BN that seems unrelated to the lack of minimum living standards. The presence of child labor within a household predicts other MPI indicators such as school attendance and employment. I could not test the causal effect between these MPI indicators using econometrics, but I provided an approximation to it based on a probabilistic theory of causality used for the construction of Bayesian networks. A high degree of endogeneity made it difficult to disentangle what are the main drivers of multidimensional poverty in rural areas of Colombia.

Understanding which are the drivers of multidimensional poverty, helps policy makers to prioritize cost-effective interventions to reduce long-term poverty. In the Colombian case, these cost-effective interventions seem to suggest the need to increase the living standards among the poor. Further research is needed to test the causal effect of minimum living standards on other poverty dimensions using regular econometrics designs for causal inference. The empirical strategy described here can be used into that

direction, by including a greater pool of relevant variables and time periods in the calculation of Bayesian networks. This could lead to the identification of better and more robust instrumental variables to study the drivers of multidimensional poverty.
