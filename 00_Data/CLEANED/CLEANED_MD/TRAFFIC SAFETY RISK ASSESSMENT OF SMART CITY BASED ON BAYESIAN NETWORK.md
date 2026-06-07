Professor Erming CHU PhD<br>E-mail cem2159@163.com<br>Business School, Xiangtan University<br>Lecturer Hongguo SUN PhD (Corresponding author)<br>201931000044@smail.xtu.edu.cn<br>Business School, Xiangtan University

# TRAFFIC SAFETY RISK ASSESSMENT OF SMART CITY BASED ON BAYESIAN NETWORK 


#### Abstract

With the development of smart city construction in China, technology governance has become a popular method to solve traffic safety problems. However, the effectiveness of technology governance needs to be evaluated scientifically. Based on Bayesian network model, this paper takes the top 50 smart cities in 2019 as the object to evaluate the safety risk of traffic. The results show that: the risk of traffic safety is highly negatively correlated with the construction of smart city, and smart traffic helps to reduce the risk of traffic safety; different levels of smart traffic construction among different cities not only make the level of traffic safety risk different, but also make the source of risk different. Travel environment safety risk is the main risk source of cities with low traffic safety risk, public traffic safety awareness risk is the main risk source of cities with medium traffic safety risk, while infrastructure safety risk is the main risk source of cities with high traffic safety risk .

Keywords: Road traffic ; traffic safety ; smart city ; risk assessment ; Bayesian network.


JEL Classification: C11, R41

## 1. Introduction

With the rapid development of China's urbanization, the urban scale is expanding, the urban population and the number of motor vehicles are increasing, it is difficult to drive and park, which has aroused widespread concern in China. How to prevent and control traffic safety risks is an important issue in the modernization of urban governance system and governance capacity in China.

With the development of a series of information technologies such as big data and cloud computing and the promotion of smart city construction, in addition to governance of urban traffic safety risks from two dimensions of infrastructure construction and traffic system construction, it also provides people with the third dimension of governance of urban traffic safety risks, namely technology

governance. From the practical process of intelligent transportation, many countries in the world have put intelligent transportation system into transportation planning, which make intelligent transportation play an increasingly important role in urban traffic safety management. The construction of intelligent transportation in various cities of China is in full swing in recent years. The investment scale of China's intelligent transportation industry increased by $127.5 \%$ from 72.09 billion in 2013 to 164.015 billion. Cities in China have invested a lot in the construction of intelligent transportation. Does intelligent transportation effectively reduce the risk of urban traffic safety in practice? To answer this question, this paper selects the top 50 smart cities in 2019 as the research object, and evaluates the safety risk of traffic based on the Bayesian network structure model.

From the perspective of risk source analysis, most scholars believe that people, vehicles, roads, environment and management are the main causes of traffic safety risks, so they choose appropriate indexes from these aspects to build the evaluation index system of traffic safety risks. For example, De Oña et al (2011), when studying the traffic safety risk of rural roads in Granada, Spain, selected indicators include driver data (driver's age and gender), accident cause (accident type, accident time, vehicles involved in the accident), road information (road width, lane width, road markings, sight distance, etc.), weather information (sunny day, rain, fog, snow, wind), and serious injury degree variables (number and severity of injuries). Anthony et al.(2016), when studying the highway traffic safety risk in developing countries, selected indicators as follows: driver status (reckless driving, fatigue driving), number of registered vehicles, policy environment (road condition, road obstacles), traffic monitoring equipment, number of annual accidents, and the number of ten thousand vehicle deaths. When Todd (2018) studied the trend of traffic accidents and the demand for the new traffic safety paradigm, he considered that the main factors affecting the traffic safety risk are public transport improvement, parking system, road condition, fuel and insurance pricing, smart road policy, transportation demand management, economic foundation, social and environmental factors. To sum up, although different scholars choose different specific indicators, the basic indicators are consistent, including the large-scale choices of people, vehicles, roads, environment and management.

From the perspective of the impact of intelligent transportation on safety risk, the existing research results show that intelligent transportation can effectively reduce traffic safety risk. For example, in view of the interference of haze weather on the driver, the traffic signs can be cleared quickly through the defogging algorithm, and the image information after defogging processing can be transmitted to the driver immediately(Xue, 2016). For reckless driving, urban intelligent driving assistance system can help drivers avoid accidents and reduce the severity of traffic accidents (Irina et al., 2020; Marusin \& Danilov, 2018). In view of the blind spot and processing lag of human management of road traffic safety, big data and cloud computing provide high-definition images, which

effectively improve the management level and management efficiency, and significantly reduce the traffic safety risk (Zhao et al.,2019). It can be seen that the impact of intelligent transportation on traffic safety risk is mainly realized through intelligent technology and intelligent management.

From the perspective of traffic safety risk assessment methods, it mainly includes data envelopment analysis (DEA), micro simulation method, neural network method, Bayesian network analysis method and so on. Data envelopment analysis (DEA) can measure the relative efficiency of decision-making units. In road traffic safety risk assessment, the relative efficiency of road traffic safety can be evaluated according to the input (such as municipal road input) and output (such as the number of deaths per 10000 vehicles, etc.) (Odeck, 2006; Doron et al., 2015). However, the implicit assumption of DEA is that there is no difference among all decision-making units, which is difficult to exist in reality. With the rapid development of computer science and technology, micro simulation method has been applied to traffic safety risk assessment. In a simulation cycle, real-time and accurate simulation data are collected to carry out micro traffic simulation (Chen et al., 2018; Shahdh et al., 2015). Its advantages are visibility, dynamics and prediction of accident degree. However, as a traffic safety method, simulation is controversial. Some scholars have questioned its reliability, believing that it can not well reflect the real world traffic safety situation (Tarko, 2012). Neural network method uses multiple input and single output method to detect traffic accidents, which is usually used together with microscopic simulation(Wang et al., 2019). Although neural network method has the advantage of objectively weighting multiple input indicators in the risk assessment and prediction of traffic accidents, it can not trace the source of the risk. Compared with these evaluation methods, the biggest advantage of Bayesian network analysis method is probability reasoning under uncertain conditions, which can not only use Bayesian network for reasoning, but also carry out risk traceability. Because of these advantages, Bayesian network analysis method has been widely used in road traffic safety risk assessment in recent years. Wan and Huang(2016) proposed a Bayesian hierarchical model for road network safety assessment to assist planners to take traffic safety as an important reference factor in road network planning. Liu et al.(2020)used Bayesian network analysis method to evaluate the safe operation of Beijing rail transit system.

With the help of Bayesian network structure model, this paper uses the data of China's top 50 smart cities in 2019 to evaluate the traffic safety risk level, and makes an in-depth analysis of the differences between different cities on the basis of risk traceability.

# 2. Design of traffic safety risk assessment method for smart city 

To evaluate the traffic safety risk of smart city, we need to construct a safety risk assessment index system which integrates intelligent transportation, then

determine the weight of each index, and finally choose the appropriate risk assessment method.

# 2.1. Risk assessment index system 

As mentioned above, the risk sources affecting urban traffic safety mainly include people, vehicles, roads, environment and management. Based on the existing classification methods, this paper will build the evaluation index system of traffic safety risk in smart cities from the following aspects: (1) Infrastructure safety risk. How the traffic infrastructure of a city will directly affect the traffic safety risk; (2) Manage system security risk. The intelligent and modernized traffic management system of a city is an effective way to reduce the traffic safety risk; (3) Public safety awareness risk. The road safety awareness of drivers and the public is an important factor affecting urban road traffic safety accidents; (4) Travel environmental safety risk. Travel environment includes weather and other climate environment, natural environment such as roads, population and other social environment; (5) Traffic accidents loss risk. Generally speaking, the greater the loss of traffic accidents, the higher the traffic safety risk. The calculation method of main indicators is shown in Table 2.

### 2.2 CRITIC weighting method

This paper uses the CRITIC weighting method to determine the weight of each index in the evaluation system. This method is proposed by Diakoulaki et al.(1995), which is an objective weighting method, as shown in Table 1. The contrast strength between indicators is measured by the size of sample standard deviation. The larger the standard deviation, the greater the difference between indicators, which means that the greater the information reflected by the indicator, the greater the weight of the indicator. The conflict between indicators is measured by correlation coefficient, that is, the greater the correlation coefficient between indicators, the lower the conflict, which means that there is a lot of information repetition between indicators, and the smaller the weight of indicators.

Table1. Calculation formula of CRITIC method


### 2.3 Bayesian network structure

This paper chooses Bayesian network analysis method to calculate and evaluate the traffic risk level of smart cities. Bayesian network is a probability

graph model, which is composed of directed acyclic graph and network parameters. It contains nodes and directed line segments. Nodes include evidence nodes, intermediate nodes and target nodes. Basic nodes represent various causes of events, which are also called parent nodes. Usually, the parent node is the secondary indicator. Intermediate nodes ,which are also called child nodes, are the nodes between basic nodes and target nodes to connect parent nodes and target nodes. Intermediate nodes are usually the primary indicators. The nodes are connected by directed line segments, representing causality. The network parameters include the prior probability attached to the parent node and the conditional probability attached to the intermediate node, representing the degree of dependence between variables(Mao, 2020). Bayesian formula describes the mathematical logic relationship among prior probability, conditional probability and posterior probability, the formula is as follows:

$$
P\left(A_{i} \mid B\right)=\frac{P\left(B \mid A_{i}\right) P\left(A_{i}\right)}{\sum_{j=1}^{n} P\left(B \mid A_{j}\right) P\left(A_{j}\right)}
$$

Where $P\left(A_{i}\right)$ is the prior probability of node $A_{i}, P\left(B \mid A_{i}\right)$ is the conditional probability of parent node $B, P\left(A_{i} \mid B\right)$ is the posterior probability of node $A_{i}$.

# 3. Related work 

### 3.1 Data source

This paper selects the top 50 cities in the 9th (2019) smart city development level assessment report of China jointly released by the Chinese Academy of Social Sciences (CASS) and the Guomai think tank. There are several reasons: first, the basic characteristics of cities with high level of smart are highly developed information base. Therefore, the cities with the highest smart ranking generally have the fastest implementation of smart transportation construction, the sample data can provide experience for the smart transportation construction of other cities; secondly, the top 50 cities cover municipalities directly under the central government, cities with separate planning, provincial capital cities and general prefecture level cities, therefore the sample distribution is wide, which meets the needs of evaluation and analysis.

The original data mainly come from the official websites of the people's republic of China statistics bureau, city statistics bureau, national development and reform commission, public resources trading network, government procurement network, traffic management bureau, traffic safety integrated service management platform, bank of China insurance regulatory commission and China urban construction statistical yearbook, The year of sample data is 2018.

# 3.2 Calculation of index weight 

This paper uses the CRITIC method to determine the weights of the primary and sub-indexes. The calculation results and the calculation formula of subindexes are shown in Table 2 and Table 3, respectively. From the weight of each level index in Table 2, the impact on traffic safety risk of smart cities from high to low is traffic accident loss risk, infrastructure safety risk, public safety awareness risk, management system safety risk and travel environment safety risk.

Table 2. Index system and weight of traffic safety risk assessment


Table 3. The calculation formula of sub-indexes


# 3.3 Bayesian network structure 

According to the traffic safety risk assessment index system, the relationship between all the assessment indexes is taken as the network node, and the Bayesian network structure diagram of 5 primary indexes and 17 sub-indexes is constructed. The Bayesian network structure model is used to assess the risk of traffic safety, as shown in Figure 1.

![img-0.jpeg](img-0.jpeg)

Figure 1. Bayesian network structure

# 4. Traffic safety risk assessment results 

In this study, with the help of the Bayesian network implementation platform Netica software, the information security risk of smart city is systematically evaluated. The specific operation steps are as follows: first, based on the traffic safety risk assessment index system, all the evaluation indexes and the relationship between them are taken as the network; Secondly, it inputs the sample data of 50 smart cities into the network structure model, and uses EM algorithm for parameter learning to calculate the risk probability value of each evaluation index of traffic safety risk in smart cities; Thirdly, it inputs the prior probability value of 50 smart cities into the Bayesian structure model to calculate the risk probability value of single smart city, then combining with the index weight, it determines the traffic safety risk value and risk level of each smart city. The final evaluation results are shown in table 4.

Table 4. Risk assessment results and ranking of traffic safety risk probability in 50 cities



Note: Column o is the score of smart city development level (percentage system), and the data source is the ninth (2019) China smart city development level evaluation report.

# 4.1 Risk probability analysis of smart cities 

According to the risk assessment results in Table 4, the 50 cities are divided into three levels according to the probability of traffic safety risk: the top 15 cities are low risk $(\mathrm{L})$, the middle 20 cities are medium risk $(\mathrm{M})$, and the bottom 15 cities are high risk $(\mathrm{H})$. On the whole, the correlation coefficient between the smart traffic safety risk probability and the smart city development level score of 50 cities is 0.7 , showing a highly negative correlation. The broken line chart between the development level score of 50 smart cities and the risk probability of smart traffic safety is shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Relationship between smart city development level and traffic safety risk level

It can be seen from Figure 2 that with the improvement of the score of smart city development level, the probability of traffic safety risk decreases, which indicates that the construction of smart city, especially the construction of smart traffic system, helps to reduce the traffic safety risk, while the smart traffic safety risk between different cities shows different characteristics.
(1) The top 15 cities have advanced intelligent transportation construction and low safety risk probability. The average safety risk level of these urban management systems is only 0.161 , and the average risk probability of traffic safety is 0.286 . The main reasons are as follows: on the one hand, these cities have developed economy, perfect road infrastructure and high public awareness of

traffic safety; on the other hand, these cities have large investment in smart city construction and advanced construction of smart transportation system, which can effectively reduce the probability of traffic accidents through technical governance, and reduce accidents through intelligent rapid processing in the event of safety accidents. Specifically: Shenzhen has invested 604 million yuan in the construction of traffic violation and accident detection projects in 2017; it has invested 338 million yuan in the construction of Futian central area traffic comprehensive improvement and smart parking cloud platform system in 2018. Beijing has invested 180 million yuan and 610 million yuan respectively in the construction of smart traffic system in 2017 and 2018, including comprehensive traffic management and smart parking. Shanghai has also made a lot of explorations in the construction of intelligent transportation. There are motor vehicle travel service app and "thirteen in one" electronic police, sonar electronic eye, etc. to capture all kinds of traffic violations in 2018. Hangzhou has invested 120 million yuan and 217 million yuan respectively in 2017 and 2018 to build traffic city data brain and intelligent transportation projects, involving signal controlled intersection, traffic monitoring system, electronic police system, intelligent bayonet system and remediation facilities for potential accident points.
(2) The construction of smart transportation in the middle 20 cities is relatively slow, and the safety risk probability is medium. The average risk probability of management system safety in these cities is 0.3 , and the average risk probability of traffic safety is 0.392 . The main reason is that the construction of intelligent transportation in these cities is relatively slow, which leads to medium urban safety risk. For example, the probability of infrastructure safety risk, public safety awareness risk and travel environment safety risk in Wuxi are not high, which are $0.198,0.176$ and 0.246 respectively, but the probability of management system safety risk is 0.457 . Due to the imperfect management system, the probability of traffic accident loss is high, which is 0.568 , as a result, the probability of traffic safety risk in Wuxi is 0.334 . Compared with Chongqing, the traffic safety risk of Guiyang is lower than that of Chongqing. The safety risks of infrastructure and public travel environment in Guiyang are 0.342 and 0.356 respectively, which are higher than those in Chongqing ( 0.164 and 0.34 ), but the safety risk of management system in Guiyang is 0.083 , which is far lower than that in Chongqing ( 0.558 ), which leads to the higher traffic safety risk in Chongqing.
(3) The construction of smart transportation in the last 15 cities lags behind, and the probability of traffic safety risk is high. The average risk probability of management system safety in these cities is 0.423 , and the average risk probability of traffic safety is 0.544 . From the specific index value, these cities not only have high risk probability in infrastructure safety risk, public safety awareness risk and traffic accident loss risk, with average levels of $0.672,0.757$ and 0.582 respectively, but also have high risk probability in traffic management system due to the lag of intelligent transportation construction. These cities are small in scale, and they are unable to keep up with technical governance to control all kinds of road traffic

safety hazards, resulting in high road traffic accident losses and ultimately higher risk probability level of urban traffic safety than other cities.

# 4.2 Analysis of risk sources in different cities 

Although the above risk probability analysis has confirmed that urban intelligent traffic construction is an important factor affecting the risk probability of urban traffic safety, the specific sources of traffic safety risk are different in different cities even if the level of intelligent traffic construction is generally the same or the overall traffic safety risk probability is generally the same. In order to find out the sources of these risks, this paper analyzes the risk sources of different cities by using the condition probability estimation of Bayesian network. The analysis results are shown in Table 5.

Table 5. Traffic safety risk condition probability of 50 smart cities



According to the data in Table 5, the main risk sources of different cities are as follows:
(1) The safety risk of travel environment is the main risk source of cities with low traffic safety risk. Among the top 15 cities, the risk probability of travel environmental safety conditions in 10 cities is higher than 0.5 , with an average of 0.5 . The characteristics of environmental safety in these cities are mainly rainy weather. In 2018, one third of the year in Shenzhen, Ningbo, Xiamen, Suzhou, Wuhan and Changsha was rainy, while nearly half of the year in Shanghai, Foshan, Guangzhou, Hangzhou and Chengdu was rainy. Rainy weather affects the normal driving of drivers, so the service of weather forecast in traffic safety should be strengthened in the construction of intelligent transportation. In terms of social environment, these cities are more prone to traffic accidents due to their prosperous economy, high population density and large number of motor vehicles. Therefore, in the construction of intelligent transportation, it is necessary to strengthen the diversion of intelligent people and vehicles to reduce road traffic pressure.
(2) Public traffic safety awareness risk is the main risk source of mediumsized cities with traffic safety risk. In the middle 20 cities in Table 5, the risk of public traffic safety awareness in 15 cities is higher than 0.5 , with an average level of 0.6 . In these cities, the public traffic safety awareness is not high, mainly in the process of urbanization in China, the expansion of medium-sized cities are much faster than that of big cities. Part of the new city residents, who come from smaller cities or rural areas, are not familiar with the road network system around the city, and they do not form the habit of checking traffic signs and markings.

(3) Infrastructure safety risk is the main risk source of cities with high traffic safety risk. In Table 5, the main risk of smart traffic safety in the last 15 cities comes from infrastructure safety risk. The conditional probability of infrastructure safety risk in these cities exceeds 0.6 , and the average conditional risk level is 0.75 , which is in a high state. The main characteristic of these cities in terms of infrastructure security is the weak information infrastructure. Therefore, in the construction of smart city, we should also strengthen the municipal road intelligent facilities, digital transportation service platform and other infrastructure construction.

# 5. Conclusions 

In this paper, Bayesian network structure model is used to evaluate the traffic safety risk of 50 smart cities, we give some conclusions as follows:
(1) The construction of intelligent transportation system helps to reduce the risk of urban traffic safety. In the state of high public safety awareness risk, environmental safety risk and road traffic accident loss risk, intelligent traffic management can reduce the probability of each potential risk, and ultimately reduce the probability level of urban traffic safety risk.
(2) Different urban traffic safety risk sources have different characteristics. From the perspective of risk source analysis, travel environment safety risk is the main risk source of smart cities with low risk of traffic safety; public traffic safety awareness risk is the main risk source of cities with medium risk of traffic safety; infrastructure safety risk is the main risk source of cities with high risk of traffic safety.

## ACKNOWLEDGMENTS

This paper is supported by Funds for Major Consulting Project of Chinese Academy of Engineering "Strategic Research on Modernization of Urban Governance System and Governance Capacity for New Smart City" (2019-ZD-38, 2020. 01. 01 -2020. 12. 31).
