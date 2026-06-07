# Blood Risk Analysis of Different Climatic Phenomena during Flood Season Based on Copula-Based Bayesian Network Method: A Case Study of Taihu Basin, China 

Yun Luo *, Zengchuan Dong *, Xike Guan and Yuhuan Liu<br>College of Hydrology and Water Resource, Hohai University, Nanjing 210098, China<br>* Correspondence: luoyun_hhu@hhu.edu.cn (Y.L.); zcdong@hhu.edu.cn (Z.D.)

Received: 19 June 2019; Accepted: 23 July 2019; Published: 24 July 2019


#### Abstract

We propose a flood risk management model for the Taihu Basin, China, that considers the spatial and temporal differences of flood risk caused by the different climatic phenomena. In terms of time, the probability distribution of climatic phenomenon occurrence time was used to divide the flood season into plum rain and the typhoon periods. In terms of space, the Taihu Basin was divided into different sub-regions by the Copula functions. Finally, we constructed a flood risk management model using the Copula-based Bayesian network to analyze the flood risk. The results showed the plum rain period occurs from June 24 to July 21 and the typhoon period from July 22 to September 22. Considering the joint distribution of sub-region precipitation and the water level of Taihu Lake, we divided the Taihu Basin into three sub-regions (P-I, P-II, and P-III) for risk analysis in the plum rain period. However, the Taihu Basin was used as a whole for flood risk analysis in the typhoon period. Risk analysis indicated a probability of $2.4 \%$, and $0.8 \%$, respectively, for future adverse drainage during the plum rain period and the typhoon period, the flood risk increases rapidly with the rising water level in the Taihu Lake.


Keywords: flood risk analysis; plum rain period; typhoon period; copula; bayesian network; Taihu Basin

## 1. Introduction

Flood risk management includes flood risk analysis [1-3], vulnerability analysis [4-6], flood disaster assessment [7-10], and response [11-13]. Several factors can influence the risk of flood disasters, such as astronomy, meteorology, hydrology, topography, landforms, and human activities. Obviously, the interaction between such heterogeneous factors cannot be described clearly by using only one variable and, therefore, the study of multivariable joint distribution models is a significant facet of research on flood risk analysis $[14,15]$.

Multivariable joint distribution models can be divided into two types [16] based on the characteristics of marginal distribution functions. There are models with the same marginal distributions (such as the multivariate normal model) [17-19] and models with different marginal distributions (such as the meta-Gaussian model) [20-22]. Considering the actual situation of a flood disaster, the second type of model is more appropriate, as choosing marginal distributions is more flexible. However, the requirement of correlation between variables in some models (such as the Farlie-Gumbel-Morgenstern model [20]) limit the application range of such models. Consequently, the copula function, that has a more flexible structure, has been introduced in flood risk analysis. Then, researchers study the various aspects of the copula function, such as function type selection, parameter estimation, and the goodness-of-fit [23-26]. In hydrology, the application of copula function, generally, includes several parts, which are as follows: (1) frequency analysis of hydro-meteorological variables

that have multi-feature attributes, such as flood duration, flood volume, and flood peaks [27,28]; (2) the encountering combination problem of different hydrological extreme events, such as an interval rainstorm combined with river flooding [23,24,29]; and (3) bias correction techniques, that are used generally in climate and hydrological modeling [30-32]. The study of flood risk analysis involves all these aspects.

Under the influence of different climatic phenomena, the types of precipitation in the Taihu Basin are divided into plum rain and typhoon rain. Statistical data indicate that the duration of the plum rain differs each year, with the average being approximately 20 days. Generally, the plum rain period starts in the middle of June, and ends in early July. Mid-May is the earliest month when the typhoon rains starts to affect the Taihu Basin, with the latest being middle November. However, most typhoons occur between July and September and, particularly, between late August and early September.

The different types of precipitation bring about spatial and temporal differences in flood risk, which leads to significant challenges in flood management in the basin. Hu et al. [33] constructed the joint distribution functions of typhoon and plum rain with the Gumbel copula function and pointed out that the encounter probability of typhoon and plum rain is $9.23 \%$ in the Taihu Basin. Taking into account a particular typhoon's birthplace, movement path, and rainfall characteristics, Cui et al. [34] put forward a concept of typhoon impacting the Taihu Basin. This concept points out that there are three kinds of typhoon which could affect the Taihu basin. It is useful information for typhoon emergency management. Liu et al. [28] used the Frank copula function to study the correlation between the start time of the plum rain period and the rainfall amounts of this period in the Taihu Basin. The results showed that when the plum rain period started early, more attention would need to be paid to flooding.

The above-mentioned studies mainly estimate the hydrological variables encountering combination problems, and they focus on the entire flood season [25,35,36]. However, compared with other situations, the encountering probability of hydrologically extreme events is small, as shown in previous study results. For example, in the Taihu Basin, the probability of only plum rain arising or only a typhoon occurring is $90.77 \%$, compared with the occurance of plum rain and typhoons [33]. Accordingly, the primary objectives of this research are; (1) to analyze the temporal characteristics of plum rain and typhoons in the research areas and to divide the flood season into the plum rain period and the typhoon period; (2) to study the precipitation heterogeneous in different climatic phenomena and identify the flood risk during the different periods; and (3) to build a proper copula-based Bayesian network model for flood control in the Taihu Basin.

# 2. Study Area and Data 

### 2.1. Study Area

As shown in Figure 1, the Taihu Basin is located in the delta region of the Yangtze River of China. The total area of the Taihu Basin is approximately $36,895 \mathrm{~km}^{2}$. The Taihu Lake, with a water surface area of $2336.8 \mathrm{~km}^{2}$, is located in the center of the basin. The basin lies in a subtropical zone, with the climate being controlled by the summer monsoon. The average annual precipitation is 1177 mm , concentrated mainly in the flood season. The upper reaches of the Taihu Basin are mountainous areas, whereas the lower reaches are mostly plains. In the flood season, this unusual terrain (high on all sides and low in the middle) leads to upstream floods and basin precipitation confluence in the plains (urbanized areas). Consequently, flood disasters can occur easily. According to geographic and hydrological conditions, the Taihu Basin is usually divided into eight hydrological regions [36]. Detailed information on the eight hydrological sub-regions is listed in Table 1.

![img-0.jpeg](img-0.jpeg)

Figure 1. Location of the study areas.
Table 1. Information on eight hydrological sub-regions.


# 2.2. Data 

Plum rain data and daily Taihu Lake water level data, from 1962 to 2011, were obtained from the Taihu Basin Authority of Ministry of Water Resources (TBA). The daily precipitation data of 67 hydrological stations, from 1962 to 2011, were also provided by the TBA. Typhoon data from 1962 to 2011 were derived from the basic data sets of Northern Pacific typhoons in Shanghai Typhoon Institute, China Meteorological Administration.

## 3. Methodology

### 3.1. Flood Season Staging Based on the Different Climatic Phenomena

Under the influence of continental polar air masses, maritime tropical air masses, and tropical cyclones, the precipitation in the Taihu Basin include, plum rain and typhoon rain. The flood season can be divided into the plum rain period and the typhoon period according to the climatic phenomenon

occurrence times. The intensity of rainfall is small in the plum rain period but the duration is long, whereas, during the typhoon period, the rainfall intensity is larger and the duration is short. Precipitation with such varying characteristics obviously leads to differing flood risks, as well as significant challenges to flood management in the basin.

# 3.1.1. Distribution Function of Plum Rain and Typhoon Occurrence Times 

The start time of the plum rain period (STP) and end time of the plum rain period (ETP) and the initial time when typhoon begins to affect the Taihu Basin (ITT) were chosen as indices to describe the occurrence time rule of plum rain, and typhoon, respectively. Norm distribution, Log-norm distribution, Gamma distribution, Beta distribution, Logistics distribution, and Weibull distribution, the six distribution functions commonly used in hydrology and meteorology, were chosen as candidate functions, and the maximum likelihood method was used for parameter estimation. The Kolmogorov-Smirnov (K-S) goodness-of-fit hypothesis test was applied to test the six distribution functions. In addition, the Probability Point Correlation Coefficient (PPCC), Root Mean Square Error (RMSE), Mean Absolute Error (MAE), and the Deterministic Coefficient (DC) were used to determine the most suitable probability density function (PDF) and cumulative distribution function (CDF) for relevant random variables (STP, ETP, and ITT). The definition of each test method is as follows:

$$
\begin{gathered}
\operatorname{PPCC}=\frac{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)\left(y_{i}-\bar{y}\right)}{\sqrt{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2} \sum_{i=1}^{n}\left(y_{i}-\bar{y}\right)^{2}}} \\
\operatorname{RMSE}=\frac{1}{n} \sqrt{\sum_{i=1}^{n}\left(x_{i}-y_{i}\right)^{2}} \\
\operatorname{MAE}=\frac{1}{n} \sum_{i=1}^{n}\left|x_{i}-y_{i}\right| \\
\mathrm{DC}=1-\frac{\sum_{i=1}^{n}\left(x_{i}-y_{i}\right)^{2}}{\sum_{i=1}^{n}\left(x_{i}-\bar{x}\right)^{2}}
\end{gathered}
$$

where $x_{i}$ and $y_{i}$ represent the empirical frequency, and theoretical frequency, respectively; $\bar{x}$ and $\bar{y}$ are the mean of empirical frequency and theoretical frequency, respectively; and $n$ is the number of samples.

### 3.1.2. Flood Season Staging and Results Verification

We chose the point-in-time when the STP cumulative is $90 \%$ as the starting point of the plum rain period, and the point-in-time when the ITT cumulative distribution is $90 \%$, as the end time of the typhoon period (the $90 \%$ percentile is the closest to the actual situation). The coefficient $\omega$ was proposed to calculate the time when the plum rain period ended and the typhoon period started. We determined the time node of the demarcation point between the plum rain period and the typhoon period using this coefficient. The time node with the maximum $\omega$ value was chosen. The coefficient $\omega$ can be calculated as follows:

$$
\omega=F_{(x)}^{\text {plum }} \times\left(1-F_{(x)}^{\text {typhoon }}\right)
$$

where $\omega$ represents the contribution rate of plum rain and typhoon to precipitation, $F_{(x)}^{\text {plum }}$ is the CDF of the ETP, and $F_{(x)}^{\text {typhoon }}$ is the CDF of the ITT.

The flood season staging results were tested against the Taihu Lake water level, which is the response factor of precipitation. Considering the actual situation, we chose the mixture normal distribution to fit the time when the water level of the Taihu Lake exceeds the warning water level (TWL). The warning water level of Taihu Lake is 3.8 m (according to the flood control project of the Taihu Basin [37]). The mixture normal distribution definition is as follows:

$$
X \sim \alpha_{1} N\left(\mu_{1}, \sigma_{1}^{2}\right)+\alpha_{2} N\left(\mu_{2}, \sigma_{2}^{2}\right)
$$

where $\alpha_{1}$ and $\alpha_{2}$ are the weight coefficients $\left(\alpha_{1}+\alpha_{2}=1\right), \mu_{1}$ and $\mu_{2}$ are the means of the samples, and $\sigma_{1}$ and $\sigma_{2}$ are the mean square deviations of the samples.

# 3.2. Division of Precipitation Sub-Region Based on Hydrological Regionalization 

Optimal division of the precipitation sub-regions was carried out in two steps, namely; (1) clustering of the hydrological sub-region, and (2) selection of the optimal precipitation sub-region division. The first step is based on the division of eight sub-regions (I, II, III, IV, V, VI, VII, VIII), which is the result of hydrological regionalization. In any hydrological sub-region, the geographical and hydrological conditions are the same, and the construction and planning of the water conservancy projects are mutually compatible. However, the different hydrological sub-regions can have similar precipitation characteristics. To respectively divide the precipitation sub-regions in the plum rain period and the typhoon period, correlation analysis methods were used. The second step is based on the relationship of regional precipitation and the Taihu Lake water level, which plays a significant role in flood control. The Copula functions were applied in the selection of optimal precipitation sub-regions division. This method not only maintains the hydraulic connection between the sub-regions, but also considers the spatial distribution of precipitation.

### 3.2.1. Clustering of Hydrological Sub-Regions Based on the Correlation Analysis of Precipitation

First, the Thiessen polygon method was used to calculate precipitations of the eight sub-regions during the plum rain and typhoon periods. Next, Person correlation, Spearman correlation, Kendall correlation, which are the three correlation analysis methods generally used in hydrology and meteorology assessments, were chosen to analyze the precipitation correlation between each sub-region. Finally, the sub-regions with strong precipitation correlations were merged successively.

### 3.2.2. Select Optimal Precipitation Sub-Regions Division by Copula Functions

The optimal precipitation sub-region division, which best reflects the relationship between precipitation and water level, was selected using Copulas. Copulas are defined as multivariate distribution functions with uniform margins on the interval 0 to 1 . Based on Sklar's theorem [38], copulas are capable of linking the joint CDF to its marginal distribution functions [39].

The joint distribution of sub-region precipitations and the Taihu Lake water level can be expressed by a copula as follows:

$$
H\left(x_{1}, x_{2}, \cdots, x_{n}, y\right)=C_{\theta}\left(F_{1}\left(x_{1}\right), F_{2}\left(x_{2}\right), \cdots, F_{n}\left(x_{n}\right), F(y)\right)
$$

where $H$ is a joint distribution, $n$ is the number of precipitation sub-region, $F_{i}\left(x_{i}\right)$ represents the marginal distribution of the $i$-th sub-region precipitation, $F(y)$ represents the marginal distribution of the Taihu Lake water level, and $C_{\theta}$ is the copula CDF with parameter $\theta$.

We selected four widely used Archimedean copulas (Clayton, Gumbel, Frank, and Joe copulas) as the candidate functions to model the joint distribution of regional precipitation and the Taihu Lake water level. The four Archimedean copula functions are defined in Table 2 [39].

Table 2. Function expressions of Archimedean copulas.


NOTES: $u_{1}, u_{2}, \cdots, u_{d}$ are independent uniform distributions.

Estimating parameter $\theta$ of the Archimedean copulas can be done by using different parametric and semi-parametric methods, such as Kendall's $\tau$ method, Spearman's $\rho$ method and maximum likelihood-based methods (MLs). MLs include the full maximum likelihood method (FML), the inference for margins method (IFM), and the canonical maximum likelihood method (CML). We used the IFM for parameter estimation [40,41].

Several commonly evaluation criteria were used to select the optimal copula functions [42], such as the Akaike Information Criterion (AIC) and the Bayesian Information Criterion (BIC). The definition of the evaluation criteria are as follows:

$$
\begin{gathered}
\mathrm{AIC}=-2 \ln (L)+2 k \\
\mathrm{BIC}=-2 \ln (L)+k \ln (n)
\end{gathered}
$$

where $L$ is the likelihood function, $k$ is the number of joint distribution function parameters, and $n$ is the number of samples.

The optimal precipitation sub-region division of the plum rain period and the typhoon period were determined by comparative analysis of the relationship between sub-region precipitations and the Taihu Lake water level under different hydrological sub-region clustering situations.

# 3.3. Flood Risk Management Based on Copula-Based Bayesian Network 

Based on a posterior knowledge input, the backward reasoning function of the Bayesian network was utilized to conduct simulation calculations of the water level states in some certain precipitation situations that could occur in future during the plum rain and the typhoon periods [43,44].

### 3.3.1. Setting of Flood Disaster Situations

The flood control planning of the Taihu Basin indicates that, the flood control standards of the basin and sub-regions are 100, and 50 years, respectively after 2025. The warning water level of Taihu Lake is 3.8 m and the water level with safety guarantee of the Taihu Lake is 4.65 meters [37]. The results of the precipitation sub-region division indicated two categories, namely: (1) the spatial distribution of precipitation of the entire basin is assumed homogeneous; therefore, we chose the basin flood control standard, the warning water level, and the water level with safety guarantee of Taihu Lake to design the flood disaster situation; (2) dividing the precipitation of the basin into different regions indicates that the spatial distribution of precipitation is heterogeneous; therefore, the flood control standards of those sub-regions and the warning water level of Taihu Lake should be used to design the flood disaster situation.

3.3.2. Establishment of Bayesian Network

Bayesian networks are probabilistic models that describe the conditional dependencies of a set of random variables by means of directed acyclic graphs (DAG) [45]. The joint density for Bayesian networks can be expressed as follows: [46,47,48]

$$
f_{X_{1}, \cdots, X_{n}}\left(x_{1}, \cdots, x_{n}\right)=\prod_{i=1}^{n} f_{X_{i} \operatorname{Pa}\left(X_{i}\right)}\left(x_{i} X_{\operatorname{Pa}\left(X_{i}\right)}=x\right)
$$

where $X_{P a\left(X_{i}\right)}=x$ is a shorthand notation for $X_{P a 1\left(X_{i}\right)}=x_{P a 1\left(X_{i}\right)}, \ldots, X_{P a m\left(X_{i}\right)}=x_{P a m\left(X_{i}\right)}$ and $P a\left(X_{i}\right)$ indicate the set containing $m$ parents of node $X_{i}$. For nodes without parents, $P a\left(X_{i}\right)$ is an empty set so that $f_{X_{i} \mid P a\left(X_{i}\right)}=f_{X_{i}}$.

Identifying network nodes, developing the Bayesian network, and assigning occurrence probabilities to network nodes are three crucial steps to build a Bayesian network model. They can all be determined from expertise or calculated by machine learning methods. We conducted the three steps as follows:

Step 1: Identifying network nodes. The flood disasters in the Taihu Basin are caused mainly by heavy precipitation and high water levels. Therefore, we selected the water level of Taihu Lake and the precipitation of the Taihu Basin as the network nodes.

Step 2: Developing a network structure. As the terrain of Taihu Basin is unusual (high sides and low middle area) and a number of the flood disasters have occurred (1954, 1983, 1991, 1999), expertise, and not machine learning, was considered more suitable to construct the network.

Step 3: Assigning occurrence probabilities to network nodes. The future flood control standard of the basin is more than 100 years, implying limited observed data. Therefore, instead of expert experience, the copula functions (machine learning method) were used to calculate the occurrence probabilities of network nodes [46].

This modeling work not only takes advantage of expertise but also avoids the limited knowledge of experts. It improves the efficiency of Bayesian network establishment and can reflect the actual situation with a limited amount of data.

The framework of this study is shown in Figure 2. The programs of this paper such as copula functions were implemented in R programming language.
![img-1.jpeg](img-1.jpeg)

Figure 2. Framework of flood risk analysis of the different climatic phenomena.

# 4. Results 

### 4.1. Results of Flood Season Staging

Table 3 lists the parameters of six reference distributions. The results of the K-S test and other goodness-of-fit tests are shown in Table 4, and Table 5, respectively. Figure 3 shows the probability density functions of STP, ETP, ITT, and TWL.

Table 3. Parameters of six reference distributions.


NOTES: Param\#1 and Param\#2 are the location and scale parameters of each distribution.
Table 4. K-S test results of random variables with six reference distribution.


Table 5. Goodness-of-fit tests for start time of the plum rain period (STP), plum rain period (ETP), and initial time when typhoon begins to affect the Taihu Basin (ITT).


![img-2.jpeg](img-2.jpeg)

Figure 3. Probability density functions of random variables. (a) start time of the plum rain period (STP); (b) plum rain period (ETP); (c) initial time when typhoon begins to affect the Taihu Basin (ITT); (d) Taihu Lake exceeds the warning water level (TWL).

Tables 4 and 5 show that the Weibull distribution, Log-normal distribution, and Normal distribution are the most suitable distribution functions for STP, ETP, and ITT, respectively (these results are similar to the previous study [33]). From Figure 2a-c, shows that the plum rain period is from June 24 (175th day, when the STP cumulative is $90 \%$ ) to July 21 (202nd day, with the maximum $\omega$ value) and the typhoon period is from July 22 (203rd day) to September 22 (265th day, when the ITT cumulative is $90 \%$ ).

Three conclusions can be drawn from Figure 3d, as follows: (1) during 170th to 180th days, the probability of the water level of Taihu Lake exceeding the warning water level increases rapidly, indicating that precipitation increases during this period. The June 24 (175th day) serving as the start time of the plum rain period is therefore rational; (2) on July 10 (191st day), the probability of the water level of the Taihu Lake exceeding the warning water level ( 3.8 m ) is highest during the plum rain period. On August 4 (216th day), the probability of the actual water level of Taihu Lake exceeding the warning water level is lowest. This means that the demarcation point of the plum rain period and the typhoon period is after July 10 and before August 4. Therefore, July 21 (202nd day) is considered reasonably as the end of the plum rain period and start of typhoon period; (3) The shape of the PDF of TWL during the plum rain period (175th to 202nd day) is high and thin, whereas during the typhoon

period (203rd to 265th day) it is low and fat. This phenomenon is consistent with the precipitation characteristics of the plum rain period and the typhoon period.

# 4.2. Results of Hydrological Sub-Region Clustering 

As shown in Figure 4a-c, as regards the geographic topological relation, for the plum rain period, the eight hydrological sub-regions were merged into four precipitation sub-regions (I and II, III and VIII, IV and V, VI and VII). As shown in Figure 4d-e, during the typhoon period, the eight hydrological sub-regions were merged into four precipitation sub-regions (I and II, III and VIII, IV and V, VI and VII).

![img-3.jpeg](img-3.jpeg)

Figure 4. Correlation results of precipitation between eight hydrological regions. (a-c) are the results for the plum rain period. (d-f) are the results for the typhoon period; (a,d) are Pearson correlation results; (b,e) are Spearman correlation results; (c,f) are Kendall correlation results.

Subsequently, the second division was implemented. As shown in Figure 5a-c, the figures show that the precipitation correlation between the III and VIII sub-region and IV and V sub-region is still high. Therefore, the III and VIII sub-region and IV and V sub-region were merged in the plum rain period. Figure 5d-f shows that the precipitation correlation between every pair of the four sub-regions is strong, indicating that the spatial heterogeneity of precipitation is not apparent in the typhoon period. However, to compare with the plum rain period, the second division of the typhoon period was kept consistent with that of the plum rain period.

After two precipitation sub-region divisions, the four schemes were calculated for the plum rain period, and typhoon periods, respectively. The joint distribution of regional precipitation and the Taihu Lake water level were calculated by Archimedean copulas in each scheme. The results are shown in Figure 6.

![img-4.jpeg](img-4.jpeg)

Figure 5. Correlation results of precipitation between four precipitation sub-regions. (a-c) are the results for the plum rain period; (d-f) are the results for the typhoon period; (a,d) are Pearson correlation results; (b,e) are Spearman correlation results; (c,f) are Kendall correlation results.

As shown in Table 6, in the plum rain period, the Clayton copula was selected to be the best-fitting copulas for Scheme 1, Scheme 2, and Scheme 3, whereas the Joe copula best fits the data in Scheme 4. In the typhoon period, the Gumbel copula was selected for Scheme 1, the Clayton copula for Scheme 2 and Scheme 3, And the Joe copula for Scheme 1.

Table 6. Goodness-of-fit tests for the copula functions in the plum rain and typhoon periods.


Subsequently, the optimal divisions for plum rain period and typhoon period were selected according to the optimal copula of each scheme. Based on the minimum value criterion of AIC and BIC, it is clear that the Scheme 3 and Scheme 4 best describe the relation of the precipitation and the Taihu Lake water level during the plum rain period, and the typhoon period, respectively. Accordingly, the final results of precipitation sub-region division as follows: (1) in the plum rain period, the Taihu Basin is divided into P-I sub-region, P-II sub-region, and P-III sub-region; (2) in the typhoon period, the Taihu Basin as a whole for flood risk analysis (Figure 7).

![img-5.jpeg](img-5.jpeg)

Figure 6. Precipitation sub-region divisions and the probability-probability plots of regional precipitation and the Taihu Lake water level in the typhoon period (a) and plum rain period (b). C is short for Clayton copula; G is short for Gumbel copula; F is short for Frank copula; J is short for Joe copula.

# 4.3. Risk Management Model for Flood Control and Drainage in the Taihu Basin 

### 4.3.1. The Result of Flood Disaster Situation Setting

The conducive and adverse drainage situations were designed according to the flood control planning of the Taihu Basin drawn up by the TBA.

In the plum rain period, when the water level of Taihu Lake exceeds the warning water level, it is unfavorable for flood drainage as long as a rainstorm with a return period over 50 years occurs in one of the four sub-regions. The 16 situations are shown in Table 7.

In the typhoon period, it is unfavorable for flood drainage if a rainstorm occurs in the Taihu Basin with a return period of more than 100 years, and the water level of Taihu Lake exceeds the warning water level. Alternatively, it is unfavorable if a rainstorm occurs in the Taihu Basin with a return period between 50 and 100 years and simultaneously, the Taihu Lake water level exceeds the safety guarantee level. The nine situations are shown in Table 8.

![img-6.jpeg](img-6.jpeg)

Figure 7. Results of precipitation sub-region division in the plum rain period (a) and typhoon period (b).
Table 7. Calculation of encounter probability during the plum rain period.


NOTES: Low means precipitation with a return period of less than 50 years; High means precipitation with a return period of more than 50 years. The upwards, arrow and down arrow symbols mean the Taihu Lake water level is lower, or higher than the warning water level, respectively. The encounter probability is expressed as percentage.

Table 8. Calculation of encounter probability during the typhoon period.


NOTES: Low means precipitation with a return period of less than 50 years; middle means precipitation with a return period between 50 and 100 years. High means precipitation with a return period of more than 100 years. The downwards arrow symbol means the Taihu Lake water level is lower than the warning water level. The upwards arrow symbol means the Taihu Lake water level is higher than the water level with safety guarantee. The double arrow symbol means the Taihu Lake water level is between the warning water level and the water level with safety guarantee.

4.3.2. The Result of Copula-Based Bayesian Network Model

As shown in the Tables 7 and 8, future total probabilities for adverse drainage situations in the Taihu Basin during the plum rain period and the typhoon period are $2.4 \%$, and $0.8 \%$, respectively. The Bayesian network structures of the flood risk management model during the plum rain period and the typhoon period are shown in Figures 8 and 9. In the plum rain period, the Bayesian network structures of the flood risk management model has five network nodes (the circles in Figure 8). The P-I sub-region precipitation is a parent node and the Taihu Basin drainage situation is a child node, whereas the others are norm nodes. The directed edges between the network nodes represent correlations between variables, and the tables beside the network nodes are occurrence probabilities in different situations. In the typhoon period, the Bayesian network structures of the flood risk management model has three network nodes (the circles in Figure 9). The precipitation of the Taihu Basin is a parent node, the Taihu Basin drainage situation is a child node, and the Taihu Lake water level is a norm node. The means of the symbols in Figure 9 are the same as those of Figure 8.
![img-7.jpeg](img-7.jpeg)

Figure 8. Bayesian network structure parameter map of the plum rain period.


![img-8.jpeg](img-8.jpeg)

Figure 9. Bayesian network structure parameter map of the typhoon period.

# 5. Discussion 

### 5.1. Rationality Analysis of the Precipitation Sub-Region Division Results

To determine whether the precipitation sub-region division results are reasonable, we analyzed the amount and structure of precipitation in the Taihu Basin during the different periods.

The precipitation concentration degree (PCD) and the precipitation concentration period (PCP) are new parameters characterizing the precipitation structure [49], calculated as follows:

$$
P C D_{i}=\sqrt{R_{x i}^{2}+R_{y i}^{2}} / R_{i} P C P_{i}=\arctan \left(R_{x i} / R_{y i}\right) R_{x i}=\sum_{j=1}^{N} r_{i j} \sin \theta_{j} ; R_{y i}=\sum_{j=1}^{N} r_{i j} \cos \theta_{j}
$$

where $P C D_{i}$, and $P C P_{i}$, respectively, are the precipitation concentration degree and concentration period in the research time; $R_{i}$ is the total precipitation in the research time, and $r_{i j}$ is the precipitation in five days. $\theta_{j}$ is the corresponding azimuth angle in the research time (the entire research time is $360^{\circ}$ ); $i$ is the year $(i=1954, \ldots, 2011) ; j$ is a five day series in the research time.

We drafted isograms (precipitation amount, PCD, PCP), which are useful in demonstrating the spatial and temporal heterogeneity of precipitation.

According to Figure 10a, in the flood season, more precipitation occurs over the west and the south of the basin, and the rainfall over the south is higher than over the north. There are three precipitation grades from the southwest to the northeast. However, it is vastly different in the plum rain period. As shown in Figure 10b, there are two maximum precipitation regions in the northwest and southwest of the Taihu Basin. Figure 10c shows that the spatial distribution of precipitation is homogeneous, except for the VII sub-region in the typhoon period. Figure 10d-f shows that the PCD values and spatial distribution differ during the different periods. In the flood season, the PCD value shows a decreasing trend from northwest to southeast. However, the distribution of the PCD maximum regions is dispersive in the plum rain period and typhoon period. Figure 10h-j shows that the average PCP of the plum rain period, the typhoon period, and the flood season appear in the 3rd pentad (early July), the 6th pentad (late August) and the 15th pentad (middle July), respectively. In conclusion, if the whole flood season was selected to study the heterogeneity of precipitation, the precipitation characteristics of the different climatic phenomena would not be revealed.

![img-9.jpeg](img-9.jpeg)

Figure 10. Isogram of precipitation amount (a-c), precipitation concentration degree (PCD) (d-f), and precipitation concentration period (PCP) (g-i) in the Taihu Basin.

The water level of the Taihu Lake plays a significant role in flood control. The amount of precipitation is the reason for the Taihu Lake water level. According to the Figures 7a and 10b, the result of precipitation sub-region division in the plum rain period corresponds to the spatial distribution of precipitation amount. Similarly, the result of precipitation sub-region division in the typhoon period corresponds to the spatial distribution of precipitation amount, as shown in Figures 10c and 7b.

# 5.2. Risk Analysis of Flood Disaster in the Taihu Basin During Different Periods 

### 5.2.1. Flood Analysis in the Plum Rain Period

Based on a posterior knowledge input, the backward reasoning function of the Bayesian network was used to conduct simulation calculations of the Taihu Lake water level states in some certain precipitation situations that could occur in the plum rain period [50,51]. These precipitation situations are shown in Table 9.

Table 9. Situation-setting of precipitation in the plum rain period.


NOTES: The definitions of "Low", "High" " $\uparrow$ " and " $\downarrow$ " are the same as for Table 7.
According to Figure 11a,b, the probability of the Taihu Lake water level rising beyond 3.8 m increases dramatically when the P-I precipitation sub-region encounters a rainstorm with a return period of more than 50 years, which in turn, increases the risk of flood disaster up to $40.5 \%$. According to Figure 11b,c, the probability of the Taihu Lake water level exceeding 3.8 m increases again when the P-I precipitation sub-region and P-II precipitation sub-region encounter a rainstorm with a return period of more than 50 years at the same time. In such instances, the risk of flood disaster in the Taihu Basin increases to $91.9 \%$. According to Figure 11c,d, when all precipitation sub-regions encounter the rainstorm with a return period over 50 years simultaneously, the probability of flood disaster increases from $91.9 \%$ to $95.5 \%$.
![img-10.jpeg](img-10.jpeg)

Figure 11. The priori reasoning of Bayesian network (a), and the posterior probability of various precipitation situations (b-d) in the plum rain period.

In the plum rain period, the P-I precipitation sub-region and P-II precipitation sub-region are considered maximum precipitation regions. These precipitation sub-regions in the upper reaches of the Taihu Basin are hilly areas, with fast water flow and a short flow concentration time. Furthermore, the runoff of P-I precipitation sub-region and P-II precipitation sub-region mostly flows into the Taihu Lake. However, the P-III precipitation sub-region is located in the lower reaches of the Taihu Basin, which are plain areas with slow water flow. Accordingly, more attention should be paid to the precipitation of P-I precipitation sub-region and P-II precipitation sub-region during the plum rain period. However, the precipitation of P-III precipitation sub-region should be monitored continuously, as it could cause poor drainage in the lower reaches.

# 5.2.2. Flood Analysis in the Typhoon Period 

The precipitation situations of the typhoon period are as Table 10 shown. According to Figure 12a,b, when the Taihu Basin encounters a rainstorm with a return period of less than 50 years, there is little likelihood of a flood disaster. However, as shown in Figure 12b,c, when the Taihu Basin encounters a rainstorm with a return period between 50 years and 100 years, the probability of the Taihu Lake water level being 3.8 m to 4.65 m is up to $85 \%$. This increases the risk of flood disaster slightly. According to Figure 12c,d, when the Taihu Basin encounters a rainstorm with a return period of more than 100 years, the probability of the Taihu Lake water level rising above 4.65 m increases dramatically and the probability of flood disaster in the Taihu Basin increases from $7.5 \%$ to $60 \%$.

Table 10. Situation-setting of precipitation in the typhoon period.


NOTES: The definitions of "Low", "Middle", "High", " $\uparrow$ ", " $\leftrightarrow$ " and " $\downarrow$ " are the same as Table 8.
![img-11.jpeg](img-11.jpeg)

Figure 12. Priori reasoning of the Bayesian network (a), and the posterior probability of various precipitation situations (b), (c), (d) in the typhoon period.

In the typhoon period, the spatial heterogeneity of precipitation is not obvious. Therefore, we focused on precipitation over the entire basin. In particular, rainstorms with a return period of more than 100 years should generally be monitored.

## 6. Conclusions

To analyze the flood disaster risk in the Taihu Basin, we divided the flood season into the plum rain period and the typhoon period, due to different precipitation heterogeneous in different climatic phenomena. Subsequently, we divided the Taihu Basin into precipitation sub-regions by using Copula functions. Finally, based on Bayesian network theory, we proposed a risk management model for flood control in the Taihu Basin to analyze the flood disaster during the different periods. The main conclusions of this study are as follows:

1. Due to meteorological reasons, the occurrence time of plum rain and typhoon present regularity, resulting in uneven distribution of precipitation during the flood season. Our flood season staging indicated that the plum rain period is from June 24 to July 21 and the typhoon period is from July 22 to September 22.
2. The spatial heterogeneity of precipitation is different under the influence of the different climatic phenomena. In the plum rain period, the Taihu Basin is divided into three precipitation sub-regions (P-I, P-II, and P-III). In the typhoon period, the Taihu Basin serves as a whole for flood risk analysis.
3. In future, the occurrence probability of adverse drainage situations in the Taihu Basin during the plum rain period and the typhoon period is $2.4 \%$, and $0.8 \%$, respectively. Furthermore, the risk increases rapidly as the Taihu Lake water level rises.
4. Although the annual precipitation of the Taihu Basin is concentrated in the flood season, the precipitation heterogeneous varies with the differing climatic phenomena. This implies that the risks of flood disaster also differs. Consequently, appropriate emergency plans should be developed to prevent and manage flood disasters occurring in the different periods during the flood season.

In this study, the Taihu Basin was used as a case study to analyze the flood risk of different climatic phenomena. Further research, employing the proposed methodology of our study, could be conducted in the coastal areas of East Asia, such as Taiwan, the Liaodong Peninsula, and Japan that are also affected by typhoons and plum rains. Given the considerable risk of flooding in the coastal areas of East Asia, it is crucial that flood season staging scheduling for flood control be implemented.

Author Contributions: Conceptualization, Y.L. (Yun Luo); Data curation, Y.L. (Yun Luo); formal analysis, Y.L. (Yun Luo); Funding acquisition, Z.D.; investigation, X.G.; methodology, Y.L. (Yun Luo); project administration, Z.D.; resources, Z.D.; software, X.G.; supervision, Z.D.; validation, X.G.; visualization, Y.L. (Yuhuan Liu); writing-original draft, Y.L. (Yun Luo); writing-review and editing, Y.L. (Yuhuan Liu).
Funding: This research was funded by the National Key Research and Development Program of China, grant number 2018YFC1508200. And the Research Innovation Program for College Graduates of Jiangsu Province, grant number KYZZ15_0136.
Acknowledgments: We sincerely thank the anonymous reviewers and the editors for their helpful and constructive comments.
Conflicts of Interest: The authors declare no conflict of interest.
