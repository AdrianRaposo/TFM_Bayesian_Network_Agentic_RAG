# Article 

## A Bayesian Network-Based Integrated for Flood Risk Assessment (InFRA)

Hongjun Joo ${ }^{1}$, Changhyun Choi ${ }^{1}$, Jungwook Kim ${ }^{1}$, Deokhwan Kim ${ }^{2}$, Soojun Kim ${ }^{1, *}$ and Hung Soo Kim ${ }^{1}$ (D)<br>1 Department of Civil Engineering, Inha University, Incheon 22212, Korea<br>2 Department of Land, Water and Environment Research, Korea Institute of Civil Engineering and Building Technology, Ilsan 10223, Korea<br>* Correspondence: sk325@inha.ac.kr; Tel.: +82-32-860-7563

Received: 28 May 2019; Accepted: 2 July 2019; Published: 9 July 2019


#### Abstract

Floods are natural disasters that should be considered a top priority in disaster management, and various methods have been developed to evaluate the risks. However, each method has different results and may confuse decision-makers in disaster management. In this study, a flood risk assessment method is proposed to integrate various methods to overcome these problems. Using factor analysis and principal component analysis (PCA), the leading indicators that affect flood damage were selected and weighted using three methods: the analytic hierarchy process (AHP), constant sum scale (CSS), and entropy. However, each method has flaws due to inconsistent weights. Therefore, a Bayesian network was used to present the integrated weights that reflect the characteristics of each method. Moreover, a relationship is proposed between the elements and the indicators based on the weights called the Integrated Index for Flood Risk Assessment (InFRA). InFRA and other assessment methods were compared by receiver operating characteristics (ROC)-area under curve (AUC) analysis. As a result, InFRA showed better applicability since InFRA was 0.67 and other methods were less than 0.5 .


Keywords: flood risk; Bayesian networks; integrated index for flood risk assessment

## 1. Introduction

Recent major disasters highlight the importance of disaster preparedness around the world and emphasize the concept of disaster risk across communities. Floods are major natural disasters and have been studied with great interest worldwide [1,2]. Federal Emergency Management Agency (FEMA) [3] and National Oceanic and Atmospheric Administration (NOAA) [4] developed a risk assessment program to estimate the extent of damage related to disasters. Munich Re Group [5] classified disasters into four categories after evaluating disaster scenarios using four factors (natural, technological, socio-political, and economic factors) and direct/indirect damages. The Tyndall Centre [6] classified flood vulnerability into social and biological categories and proposed a basic framework to improve vulnerability-specific adaptability.

Rygel et al. [7] suggested that the most important issue in a vulnerability assessment is selecting appropriate indicators. They proposed a method to evaluate flood risk using the Pareto ranking process after selecting and collecting vulnerabilities into two categories (exposure and sociological). Chang and Huang [8] selected potential impact indicators (PIs) for urban areas in Taiwan and estimated the flood risk index by combining PIs with adaptive capacity indicators (AIs). Kablan et al. [9] estimated a flood vulnerability index based on the concept of climate change vulnerability assessment through proxy variables that are relevant to disaster risk management and adaptation to climate changes using three flooding indices: (1) an exposure index (EI), (2) sensitivity index (SI), and (3) adaptive capacity

index (AI). In addition, some studies have examined the impact of forest areas on flood risk [10] and the relationship between intensity-duration-frequency (IDF) curves and flood risk [11].

Many research institutes around the world have also assessed flood risk, including the Environment Agency (EA), Jeollabuk-do Total Human Institute National of Korea (JTHINK), Korea Institute of Civil Engineering and Building Technology(KICT), Korea Research Institute for Human Settlements (KRIHS), Korea Environment Institute(KEI), Ministry of Land, Transport and Maritime Affairs (MOLTMA), National Disaster Management Research Institute (NDMI), National Institute for Land and Infrastructure Management (NILIM), and Seoul Institute (SI) [12,13,14,15,16,17,18,19,20,21]. The above studies commonly selected indicators that are expected to have an effect on flood risk. Then, the conclusive flood risk is derived from the weight between each indicator (mainly expert questionnaire or subjective judgment). Their goal is to address flood management through flood risk assessment.

To assess flood risks, it is essential to select indicators that affect floods and assign them reasonable weights. However, as mentioned earlier, most studies lack a basis for the selection of indicators, and they have typically selected indicators based on the frequency of their use in other studies or a subjective view on the importance of such indicators. In addition, most flood risk assessment methods are not differentiated because they use similar estimation methods. These problems have not been validated for the methods to be actually applied.

The purpose of this study is to develop a flood risk assessment method that can address the problems of undifferentiated and accurate estimates of previous methods. To this end, a methodology is proposed to derive the integrated weights of components and indicators using Bayesian networks (BNs) as an integrated decision model after selecting representative indicators among the existing flood risk indicators through factor analysis and principal component analysis (PCA). Section 2 explains the basic theories behind the methodologies that are material in this study, and Section 3 discusses the result of the methodology used on the target areas. Finally, Section 4 presents the conclusions.

# 2. Materials and Theories 

### 2.1. Existing Flood Risk Assessment Indices

In general, flood risk is computed by multiplying three factors of vulnerability related to flood occurrence: (1) hazard; (2) asset or human exposure; and (3) lack of flood protection [22]. Based on these definitions, many flood risk assessment indicators have been developed for flood risk management. The indicators mainly used in Korea are the potential flood damage (PFD) [17], excess flood vulnerability index (EFVI) [18], flood disaster risk reduction index (FDRRI) [19], flood vulnerability assessment (FVA) [13], flood damage index (FDI) [15], and regional safety assessment (RSA) [21]. These six methods have been used mainly in Korea because they are well known to be applicable with general indicators for assessing flood risk. Each assessment method is estimated by the general procedure with almost similar methods presented in introduction.

In this study, the factors of these indicators were reviewed and classified into four components: (1) hydro-geology; (2) socio-economics; (3) protection; and (4) climate. Furthermore, 28 indicators were also used for the components, as shown in Table 1. The flood risk index (FRI) increases as the H (hydro-geology), S (socio-economics), and C (climate) components increase. The index decreases as the P (protection) component increases. With these indicators, the FRI can be expressed as follows:

$$
\mathrm{FRI}=(\mathrm{H} \times \mathrm{S} \times \mathrm{C}) / \mathrm{P}
$$

Table 1. Classification of components and indicators using six assessment methods.

Hydro-geology | (1) Flood hazard area
(2) Flood damage cost for public facilities
(3) Imperviousness
(4) Urban rate
(5) Curve number (CN)
(6) Basin slope
(7) Lowland area rate
(8) Stream density | 0
0
0
0 | 0
0
0 | 0
0
0 | 0
0
0 | 0
0
0 | 0
0
0  |
|  B.
Socio-economy | (9) Population density
(10) Asset (reference land price)
(11) Financial independence rate
(12) Infrastructure
(13) Dependence population
(14) Manufacturing output in value
(15) Total number of houses | 0
0
0
0 | 0
0
0
0 | 0
0
0
0 | 0
0
0
0 | 0
0
0
0 | 0
0
0  |
(17) Frequency of intensive rainfall per day ( $\mathrm{P} \geq 150 \mathrm{~mm}$ )
(18) Maximum hourly rainfall
(19) Annual precipitation
(20) Probability rainfall | 0
0 |  | 0
0 |  |  |   |
(22) Levee length
(23) Pump station (number)
(24) Pump station (capacity)
(25) Dam and reservoir
(26) Drainage capacity
(27) Number of public servants per resident
(28) Index of damage reduction ability | 0
0
0 |  | 0
0
0
0 |  |  |   |

# 2.2. Methodology for Selecting Representative Indicators

Factor analysis is used to reduce the complexity of data by grouping measurement variables into common factors and determining whether the measured variables measure the desired data in the same construct [23]. Factor analysis is advantageous because it is relatively free of constraints of multicollinearity, it can classify variables by factors in the development process of a measurement scale, and it can analyze them based on the correlation of variables. principal component analysis (PCA) in factor analysis is a technique for creating a small number of new variables by combining many highly correlated variables. It is a method of forming a group of components that represent many variables by reducing the dimensionality of data [24]. In addition, it can easily identify the component that has the highest explaining power in the group because the component of each variable can be quantified.

Figure 1 illustrates the method of selecting representative indicators using factor analysis and PCA. Assuming that there are six indicators A-F, they can be grouped by factor analysis, and the ones that have high explanatory power can be selected using PCA. In this way, the complexity of the FRI can be effectively reduced. ![img-0.jpeg](img-0.jpeg)

Figure 1. Overview of factor analysis and principal component analysis (PCA).

# 2.3. Methodology for Assigning Weights 

Weights should be assigned according to the importance of each indicator that affects the flood in assessing flood risk. There are many theories for weight assignment methods, and it is difficult to say that these weighting techniques differ in explanatory power or merit. Only the classification methods differ according to the purpose of a study or a subjective view about importance. The weighting techniques originate from differences in assumptions that lead to values or preferences [25], and they are categorized into direct and indirect methods, including surveys [26]. In this study, the analytic hierarchy process (AHP), constant sum scale (CSS), and entropy weight were selected for weighting the flood risk indicators identified to derive the FRI.

AHP is a typical method of multicriteria decision-making (MCDM). It forms a hierarchical structure by assessment items and evaluates alternatives through pairwise comparison. Quantitative and qualitative data can be processed on a ratio scale, which makes the method useful for verifying objectivity through the process of secondary processing of data [27,28]. CSS provides a consistent fixed total score to respondents and divides the score according to the relative importance of the attributes within the total score [29]. The score used for the total fixed scale is usually 10 or 100 based on the number of factors and indicators.

The entropy weight technique is based on the theory that information about the signal can be measured indirectly with a degree of reduction of uncertainty. In this sense, information and uncertainty are dual terms and sometimes used interchangeably [30], and weights between the indicators can be determined using the characteristics of these entropies. The estimation procedure consists of (1) constructing a matrix for each item; (2) normalizing the attribute information for each constructed indicator; (3) calculating the entropy for each attribute; (4) considering the degree of diversity between the indicators; and (5) determining the final weights (see Equations (2)-(6)).
(1) Matrix construction

$$
\begin{array}{ccc}
x_{11} \cdots & x_{1 j} \cdots & x_{1 n} \\
\vdots & \vdots & \vdots \\
x_{i 1} & x_{i j} & x_{1 n} \\
\vdots & \vdots & \vdots \\
x_{m 1} & x_{m j} & x_{m n}
\end{array}
$$

(2) Normalization of assessment items

$$
p_{i j}=\frac{x_{i j}}{\sum_{i=1}^{m} x_{i j}}(i=1,2, \cdots m ; j=1,2, \cdots n)
$$

(3) Calculation of entropy of each attribute

$$
E_{j}=-k \sum_{i=1}^{m} p_{i j} \log p_{i j}\left(\text { Here, } k=\frac{1}{\log m} ; i=1,2, \cdots m ; j=1,2, \cdots n\right)
$$

(4) Weight assignment between assessments

$$
\begin{gathered}
d_{j}=1-E_{j} \\
w_{j}=\frac{d_{j}}{\sum_{j=1}^{n} d_{j}}(j=1,2, \cdots n)
\end{gathered}
$$

2.4. Bayesian Networks (BNs)

A BN is a stochastic graphical model that can represent the relationship between variables even when there is uncertainty between them. It consists of a directed acyclic graph (DAG) model of nodes and links and has the advantage of integrating variables of sources and types into a single structure. The relationship between nodes is described by conditional probability distribution (CPD), which considers dependencies between variables [31-33].

For example, the child nodes $\left(x_{1}, x_{2}\right)$ in Figure 2 are determined by the conditional probability of the parent nodes $\left(x_{2}, x_{3}\right)$ if there is a graph that has the nodes $\left(x_{1}, x_{2}, x_{3}\right)$ that follow the CPD. Any unconnected node is ignored. The joint distribution with n number of variables $\mathrm{p}\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ is expressed in Equation (7):

$$
p\left(x_{1}, x_{2}, \cdots, x_{n}\right)=\prod_{i=1}^{n} p\left(x_{i} \mid a_{i}\right)
$$

where $a_{i}$ denotes the set of parent nodes of $x_{i}$, and $\mathrm{p}\left(x_{1}, x_{2}, \cdots, x_{n}\right)$ is normalized constantly as the predistribution has been normalized.
![img-1.jpeg](img-1.jpeg)

Figure 2. Example of a Bayesian network.

# 2.5. Integrated Index for Flood Risk Assessment (InFRA) 

Equation (8) is proposed as a formula to construct the Integrated Index for Flood Risk Assessment (InFRA) based on the weight of each factor:

$$
\operatorname{InFRA}=H^{a_{1}} \times S^{a_{2}} \times C^{a_{3}} \times(1-P)^{a_{4}}
$$

where:
$H=$ hydro-geology
$S=$ socio-economics
$C=$ climate
$P=$ flood protection and
$\alpha_{i}=$ weight of each indicator
As flood protection is inversely proportional to InFRA, it is necessary to consider it in descending order when estimating flood protection. If flood protection is 0 and the other indicators are 1, the value of InFRA will be 1, and the closer the value is to 1 , the higher the flood risk will be. The key components that make up an indicator can be determined by multiplying them by the weights and summing them (Equations (9)-(12)):

$$
\begin{aligned}
H & =\beta_{1} h_{1}+\beta_{2} h_{2}+\cdots+\beta_{\mathrm{n}} h_{n} \\
S & =\gamma_{1} s_{1}+\gamma_{2} s_{2}+\cdots+\gamma_{\mathrm{n}} s_{n} \\
C & =\delta_{1} c_{1}+\delta_{2} c_{2}+\cdots+\delta_{\mathrm{n}} c_{n} \\
P & =\varepsilon_{1} p_{1}+\varepsilon_{2} p_{2}+\cdots+\varepsilon_{\mathrm{n}} p_{n}
\end{aligned}
$$

where:

$h_{i}, s_{i}, c_{i}, p_{i}=$ each indicator
$\beta_{i}, \gamma_{i}, \delta_{i}, \varepsilon_{i}=$ the weights of each indicator

# 3. Application and Results 

### 3.1. Selection of Target Areas and Data Collection

This study targeted the Midwest region of the Republic of Korea, including Daejeon Metropolitan City, Sejong Special Self-Governing City, Chungnam Province, and Chungbuk Province. The area consists of 28 cities and gun (districts or counties in Korea), including two municipalities, 11 cities, and 15 gun (see Figure 3). The advantage of the area is that it provides various geographical environments to select flood risks because it encompasses large cities, small and medium cities, coastal cities, mountainous regions, and rural areas.
![img-2.jpeg](img-2.jpeg)

Figure 3. Target area (Chungnam and Chungbuk Provinces).
The elements needed to construct an indicator database are summarized as statistical data and geographic information system (GIS)-based data. Demographic, social, and economic data were collected from the Korean Statistical Information Service (KOSIS), the statistical yearbooks of local governments, and the Statistical Yearbook of Natural Disasters. Meteorological data were collected from the Korea Meteorological Administration. All data were collected based on GIS for spatial analysis. The base year of the data is 2016, and statistical data for the ten years prior (2007-2016) were used. As shown in Table 1, data were collected for all 28 indicators of four components. All indicators were normalized to values between 0 and 1 using the average values estimated for each region and the standard deviations. Thus, the larger the value of an indicator for a region is, the closer it is to 1 . The indicators of the H, S, and C components are positively correlated with FRI, whereas the indicators of P are negatively correlated.

### 3.2. Selection of Indicators Using Factor Analysis and Principal Component Analysis

Factor analysis and PCA were performed on each of the four components (hydro-geology, socio-economics, flood protection, and climate), which each consisted of several indicators. First, the indicators were grouped by factor using factor analysis, and the indicators with the highest component point for each group were selected using PCA. The procedure can prevent the duplication of meaning of the indicators and reduce dimension of the indicators in each group.

Table 2 shows the results of the factor analysis. The hydro-geology, socio-economic, and protection components were classified into three groups, whereas climate was classified into two groups. Kaiser-Meyer-Olkin (KMO) [34] and Barlett's test of sphericity [35] were used to determine the appropriateness of the analysis. The Kaiser-Harris measurement [34] was used to select principal components that have an eigenvalue of 1 or higher (see Table 2). The result of each component was determined to be significant because KMO remained at 0.5 or higher, and the probability value (p) remained below 0.05 .

Table 2. Grouping and selection of representative indicators by PCA and factor analysis.


PCA was used to select indicators that have the most significant contribution for each group. Among 28 indicators, 17 were eliminated and 11 were chosen: (1) three indicators for hydro-geology (damage cost, urban rate, and lowland area rate); (2) three for socio-economics (total number of houses, financial independence rate, and dependence population); (3) three for flood protection (number of pump stations, drainage capacity, and number of public servants per resident); and (4) two for climate (frequency of intensive rainfall and probability rainfall), as shown in Table 2.

# 3.3. Weight Assignment by Method and Calculation of Integrated Weights 

### 3.3.1. Weight Assignment by Method

The factors selected are expressed as normalized values between 0 and 1, and each indicator is estimated using the assigned weights. The flood risk index can be quantified using the weight of each indicator. To this end, weights can be assigned by various methods, and three weight assignment methods were applied, as described in Section 2.3. For the AHP, a survey was conducted with 30 respondents from academia and research. The survey was constructed in such a way that the importance of each indicator was compared in pairs. The terms of each indicator were defined and presented in the questionnaire to improve the accessibility for the respondents. The first-level hierarchy consists of four upper-level assessment components (hydro-geology, socio-economics, flood protection, and climate), and the second-level hierarchy consists of 11 lower-level assessment indicators.

For the CSS, a survey was conducted with 21 experts who have experience in work related to flood or wind damage and did not participate in the AHP survey. The questionnaire was structured in such a way that the sum of the four components presented and the sum of indicators for each component was 10. A sufficient explanation of the survey method was provided to supplement the questionnaire so that the respondents would not be confused.

For entropy weighting, Equations (1)-(6) from Section 2.3 were used based on the data collected for each component. The weights are shown in Table 3 and Figure 4. In summary, the weights

for the socio-economic component were low in the survey methods, while they were high in the entropy weight method. In particular, the weights were evenly distributed among the rest of the components other than the socio-economic component and thus gave a relatively identical position concerning importance.

Table 3. Weight assignment for the representative indicators.


![img-3.jpeg](img-3.jpeg)

Figure 4. Weight distribution.

The indicators within a component showed a different aspect in the survey and entropy methods: the entropy method showed higher weight values for specific indicators, while the surveys showed relatively similar weight values for the indicators. This was due to the unique characteristics of entropy, which increases when deviations between alternatives are low. Moreover, the deviations between the normalized values of the indicators were small. However, the number of public servants per resident indicator of the flood protection component and the annual precipitation indicator of the climate component were low, and divisions in indicators between regions were high, which resulted in low entropy weights.

# 3.3.2. Integrated Weight Assignment Using Bayesian Networks (BNs) 

The estimated weights affect the outcome of the estimated flood risk. It is not easy to determine the weights for each component and indicator, particularly when the entropy weight is higher than the other weights, such as for the total number of houses in Table 4. Thus, the BN method was used to estimate the combined weights while considering causal relationships between weights obtained from the AHP, CSS, and entropy techniques. First, a BN with 20 nodes and 19 links was constructed with AgenaRisk 10, as shown in Figure 5. The BN was constructed in consideration of the relationships between the components and indicators. The pre-probability assigned to each higher node can be inferred directly from the conditional probability, and the deviation of the probability determines the post-probability of the lower nodes. That is, the post-probability (the integrated weights) can be derived from pre-weights (the current weights), the conditional probability of each component (hydro-geology, socio-econometrics, flooding protection, and climate), and its indicators. As each component was weighted separately, it will not affect its indicators and can be expressed as dotted-line links that have indirect influences. Table 4 shows all of the probabilities (weights) of each component and indicator obtained from the configuration in Figure 5 and the post-probabilities (integrated weights).

Table 4. Resulting integrated weights.


The estimated weight of each component was relatively uniform in the range of $0.20-0.28$. The weight of the socio-economic component was low in the survey method but increased significantly in the entropy method. This indicates that the entropy weight contributed to conditional probabilities as a prior probability. Similarly, the other indicators within each component were adjusted adequately by prior and conditional probabilities. For example, the drainage capacity indicator of the flood protection component was weighted as 0.50 and 0.45 in two surveys, respectively, while it was weighted as 0.35 in the entropy method, and its integrated weight became 0.36 .

Moreover, the annual precipitation of the climate component was weighted with a small value of 0.01 in the entropy method, but the integrated weight was 0.06 because it was weighted with 0.23 and 0.28 in the two surveys. The BN model has an effective and optimal decision-making capability

to integrate different knowledge and data [36,37]. Thus, BNs are expected to be a new alternative in assigning weights between indicators.
![img-4.jpeg](img-4.jpeg)

Figure 5. BN configuration for integrated weight assignment.

# 3.4. Results of Calculation with InFRA 

The final InFRA was estimated for hydro-geology, socio-economics, flood protection, and climate components in 28 cities in the Chungcheong Province using several formulas (see Figure 4). As a result, InFRA did not show a significant gap between regions except for some areas and showed a flood risk of $0.3-0.5$ in most places. The resulting values for Seosan (17), Dangjin (20), and Taean (27) were close to 0.7 , despite their low risk from the socio-economic component. This occurred because the risk from the other components was high. Some village areas including Jeungpyeong (8) and Jincheon (9) showed a low InFRA level because they had a low level of flood protection and other components. The risk related to the hydro-geology component was high in the countryside because these areas are more influenced by flood damage, and there are more lowland areas than urban areas. In the socio-economic component, the indicators of the total number of houses and financial independence rate showed a high risk in large cities, followed by some villages that have a high dependent population.

In the flood protection component, large and medium cities showed a high level of protection, whereas villages showed a low level of protection because they lack flood protection systems. The flood protection component shown in Figure 6 is expressed in the concept of "1-flood protection," so it is interpreted accordingly. In the climate component, the basins were clustered in a continuous pattern and showed a constant flood risk, particularly in coastal areas according to the consistent measurement of the measurement stations in the Thiessen network along the coastal cities. This is attributed to the high frequency of intense rainfall in coastal areas, and thus, the frequency of intensive rainfall indicator is weighted higher than the annual precipitation indicator.

![img-5.jpeg](img-5.jpeg)

Figure 6. Integrated Index for Flood Risk Assessment (InFRA) estimation.

### 3.5. Comparison with Other Methods and Discussion

The proposed method was compared with other three methods used to assess flood risk: PFD, FDI, and RSA [15,17,21]. The three methods are the most popular in a practical field because they are easy to collect data and simple to apply. These methods are briefly explained in Table 5. However, the same assessment criteria must be used to compare the two sets of methods. The other assessment methods use various criteria with grades (1–5) or groups (A–D), and thus, comparing the methods using the same set of criteria is not appropriate. Therefore, they were compared in an alternative way using risk values between 0 and 1 instead of using grades or groups for a consistent comparison. In all the assessment methods, the risk of flood increased when the risk value was closer to 1, indicating that appropriate measures need to be taken for flood mitigation.

Table 5. Basic information on other flood risk assessment methods.


The other assessment methods generally showed high flood risk in cities and low risk in villages. In particular, flood risks were high in Daejeon, Cheongju, Chungju, and Cheonan but low in Yeongdong, Jincheon, Goesan, and Geumsan. The other assessment methods were polarized in urban and rural areas and showed large regional variations compared to InFRA (see Figure 7). It seems that the duplicated meaning in the construction of indicators and the insufficient level of flood protection in cities are major reasons for such results. Nevertheless, indicators such as population, financial independence rate, and infrastructure are typically high in urban areas. Thus, the other risk assessment methods are considered to have produced somewhat overestimated values because they use a system that would inevitably estimate large flood risk in large cities.

![img-6.jpeg](img-6.jpeg)

**Figure 7.** Results of previous flood risk assessment methods.

This comparison was qualitative, and a quantitative comparison is necessary. Therefore, the methods were validated by analyzing the area under the curve (AUC) of the receiver operating characteristic (ROC) curve. The ROC curve is a graph where the x-axis shows the specificity, which indicates the probability of the estimated value being false. The y-axis shows the sensitivity, which indicates the probability of the estimated value being true. That is, the evaluation method is better if the risk assessment is more likely to be correct and has a lower false probability rate. A higher

AUC indicates higher accuracy of the prediction, and the accuracy of the results increases as AUC approaches 1.

The limit of this validation is that the factors to be compared must be considered to evaluate the accuracy of each method, but the assessment factors are already included as indicators, and there is no suitable criterion to apply. As the best alternative, data from [38] were used, and total flood damage costs were derived, including injuries and flooding of farmland and cities, for the flood damage cost for public facilities (see Table 6). Then, the integrated sums were normalized. If the value is 0.5 or higher, the corresponding region is considered to have high damage cost. The ROC analysis was then conducted.

Table 6. Estimated total flood damage cost by district.


According to the AUC of the ROC, the accuracy of InFRA was 0.67 , while that of PFD, FDI, and RSA was less than $0.5(0.296,0.417$ and 0.174 , respectively). Thus, they were withdrawn from the assessment of flood damage cost (see Figure 8). In other words, the other risk assessment methods were revealed to be inappropriate for assessing flood damage costs. The evaluation showed that InFRA is better than the classic methods for assessing flood risk and could thus be applicable in the field.
![img-7.jpeg](img-7.jpeg)

Figure 8. Validation of flood risk assessment methods using receiver operating characteristic (ROC)-area under curve (AUC) analysis.

# 4. Conclusions 

Numerous methods have been developed to assess flood risk. In this study, a methodology was proposed for use in decision-making by integrating existing methods rather than developing another flood risk assessment method. First, previous flood risk assessment methods were evaluated (PFD, EFVI, FDRRI, FVA, FDI, and RSA), and four components and 28 indicators were extracted. Factor analysis and PCA were carried out, and 11 of the 28 indicators were selected as a result. Then, the weights of each component and indicator were estimated by the AHP, CSS, and entropy methods, and the results of each method differed from one another. Therefore, BNs that integrate the conventional weight assignment methods were structured to estimate integrated weights.

The BN-based InFRA was applied to target regions to estimate the flood risk of each region. The result of both qualitative and quantitative comparisons between InFRA and the conventional methods demonstrated the excellent applicability of InFRA. The InFRA methodology can integrate various other flood risk assessment methods and it could be used as a useful tool in decision-making for flood risk management.

Author Contributions: Conceptualization and methodology, H.J. and S.K.; statistical analysis, C.C., J.K. and D.K.; writing-original draft preparation, H.J.; Final review, H.S.K.; supervision, S.K. and H.S.K.
Funding: This research was supported by a grant [MOIS-DP-2015-05] through the Disaster and Safety Management Institute funded by Ministry of the Interior and Safety of Korean government.
Conflicts of Interest: The authors declare no conflicts of interest.
