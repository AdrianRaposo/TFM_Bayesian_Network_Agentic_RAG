# Article 

## Risk Prediction Method for Renewable Energy Investments Abroad Based on Cloud-DBN

Wenjiao Zai ${ }^{1}$, Yuying He ${ }^{1, *}$ and Huazhang Wang ${ }^{2}$

## check for updates

Citation: Zai, W.; He, Y.; Wang, H. Risk Prediction Method for Renewable Energy Investments Abroad Based on Cloud-DBN. Sustainability 2023, 15, 11297. https://doi.org/10.3390/su151411297

Academic Editors: Oleksandr Kubatko, Hynek Roubik and Rui Li

Received: 6 June 2023
Revised: 4 July 2023
Accepted: 18 July 2023
Published: 20 July 2023

## 0

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Engineering, Sichuan Normal University, Chengdu 610101, China; zaiwenjiao@sicnu.edu.cn
2 College of Electrical Engineering, Southwest Minzu University, Chengdu 610041, China; wanghuazhang@126.com

* Correspondence: heyuying@stu.sicnu.edu.cn


#### Abstract

There are many specific risks in renewable energy (RE) investment projects, and the incidences of these risk factors are fuzzy and uncertain. In different stages of a project's life cycle, the main risk factors frequently change. Therefore, this paper constructed a cloud dynamic Bayesian network model (Cloud-DBN) for RE operation processes; it uses the DBN graph theory to show the generation mechanism and evolution process of RE outbound investment risks, to make the risk prediction structure clear. Based on the statistical data of observation nodes, the probability of risk occurrence is deduced to ensure the scientific nature of the reasoning process. The probability of risk being low, medium, or high is given, which is highly consistent with the uncertainty and randomness of risk. An improved formula for quantitative data normalization is proposed, and an improved calculation method for joint conditional probability based on weight and contribution probability is proposed, which reduces the workload of determining numerous joint conditional probabilities and improves the practicability of the BN network with multiple parent nodes. According to the 20-year historical statistical data of observation nodes, the $\mathrm{GM}(1,1)$ algorithm was used to extract the transfer characteristics of observation nodes, construct the DBN network, and deduce the annual risk probability of each risk node during the operation period of the RE project. The method was applied to the wind power project invested by China in Pakistan, and the effectiveness of the method was tested. The method in this paper provides a basis for investment decisions in the RE project planning period and provides targeted risk reduction measures for the project's operation period.


Keywords: RE; foreign investment; risk forecast; Cloud-DBN; risk probability

## 1. Introduction

The demand for energy and its related services to support human social and economic development, welfare, and health is increasing [1]. The use of fossil fuels in various sectors, especially those with fewer added values, has caused serious environmental problems [2]. At the same time, crises, such as COVID-19 and the Russia-Ukraine conflict, have raised questions about the reliability of non-renewables and what actions could be taken by policymakers to immediately mitigate the reliance on fossil fuels for vulnerable importers [3]. The use of RE and related industries is also of concern. In the future, RE will be the main source of energy in the energy market, and the construction and development of RE projects will gain widespread attention.

Following market-oriented reforms in the electric power industry, the RE industry has expanded more quickly in developing countries facing rapid economic growth and severe energy shortages [4]. The numbers given by almost all energy bodies worldwide show that RE is growing faster than all other traditional forms of energy. This trend is a response to instability in the fossil fuels market and the numerous benefits of renewable resources [5]. Renewable energy dynamics have introduced many new terms; for example, trade openness, economic growth, and technological progress [6]. Investment in sustainable

and renewable technologies must be doubled if globally agreed-upon climate targets are to be met [7]. Foreign investment decisions in RE are faced with many uncertain factors, such as the volatility of electricity prices, the randomness of renewable energy, the instability of policy, the rapidity of technological development, the diversity of investment subjects, etc. These uncertainties bring corresponding investment risks to the planning and construction of the power systems. In this paper, a more comprehensive and reasonable decision model for RE investment risk is proposed based on the decision model for RE investment risks at home and abroad. The method in this paper provides the basis for investment decisions in a RE project planning period and provides targeted risk reduction and control measures for the project's operation period.

Classical methods commonly used include net present value (NPV) [8,9], decouple net present value (DNPV) [10,11], real option theory method [12-14], argumentative discourse analysis [15], analytic hierarchy process (AHP) [16-18], analysis network process (ANP) [19-21], a group decision-making approach [22], a game theory-based method [23], and soft decision-making [24]. de Freitas et al. [8] proposed a model to assist investment decision-making in renewable energy power generation. Under a given level of risk aversion, the conditional value at risk (CVaR) was introduced to maximize the expected financial return of the entire company's portfolio. But venture capital still needs to consider the behaviors of generation, future prices, future costs, and all factors that will make up its cash flow over the next few years. Bekaert et al. [9] quantified political risk, evaluated its impact on expected cash flows, and discounted expected cash flows at a rate that reflected systemic risk. To eliminate the losses caused by political risks to international investment projects, the NPV method is used to evaluate the economic performance of the project. Espinoza et al. [10,11] used the concept of insurance or claim valuation to conduct discrete quantification of risks related to project cash flows, and separated investment project risks from their actual sources (cash flows). Because identified project risks are quantified in financial terms and treated as the actual costs of the project, DNPV allows business executives to assess the impact of different risks on the project's value and select management techniques that are considered more effective. Liu et al. [12], addressing the risk management needs of power generation capacity investments in a market environment, established a differential equation describing the change in option value to make optimal power generation investment decisions, based on an unvested option analysis method. Xun et al. [13], in the electricity market environment, comprehensively considered a variety of uncertain factors, applied the theory of real options to evaluate the investment strategy, and studied the impacts of income fluctuations at various investment stages on the decision-making behaviors of power generation investors under a variety of uncertain factors. Cao et al. [14], considering the uncertainty of wind power feed-in tariffs, wind farm investments, running costs, investment policies, and investment opportunities on the influence of investment risks, utilized the portfolio investment concept to establish a quantitative assessment model for wind power project investment decisions. This model allows for a quantitative evaluation of the impact of different factors on different power investment decision-making stages. Tani et al. [15] used the Boston area's transition to clean energy technologies as the backbone of their case study. They used argumentative discourse analysis (ADA) to assess the role of policy in promoting or hindering the development of a clean energy niche and the deployment of clean energy technologies.

The above literature focuses on quantifying the risks of one or several factors in RE investment to project investment while ignoring other risk factors. In recent years, scholars at home and abroad have analyzed and demonstrated the main risk factors in RE power generation projects from a number of risk factors. Ilbahar et al. [16] constructed four main risk categories and seventeen risks through a comprehensive literature review and expert interviews. Based on prospect theory and the intuitionistic fuzzy analytic hierarchy process, the effect analysis of the risk decision model was carried out, which effectively overcame the uncertainty and cognitive bias of experts and prioritized the risks of renewable energy investment. Kul et al. [17] used Turkey's renewable energy investment (REI)

as an example and proposed the three-step decision method of the multi-criteria decision method (MCDM). The Delphi method was used to identify the REI risk factors, the AHP was used to evaluate the identified REI risk factors, and the fuzzy weighted aggregated sum product assessment (FWASPAS) was used to evaluate and prioritize strategies to overcome the risk factors in the REI project, and eventually find the best fit for the given decision situation. Zhou et al. [18] proposed a three-stage decision model. Firstly, the dimensions and standards of renewable energy investment risks were defined. Secondly, the IT2F-DANP with alpha cut was used to calculate the significance level of these factors. Finally, the IT2F-QUALIFLEX method with alpha cut was used to divide investors into high, medium, and low levels according to risk awareness. A hybrid approach was used in the analysis, with two different MCDM models (DANP and QUALIFLEX) considered at different stages, so the standard weights and alternative ranks obtained were calculated objectively. This approach considers all possible energy investment risks and develops appropriate strategies for investors by assessing these risks. Hashemizadeh et al. [19] used the MCDM method to determine the risk factors of renewable energy investments in Belt and Road countries and divided them into five categories: economic, technological, environmental, social, and political. The fuzzy analysis network process (F-ANP) was used to weigh the identified factors, and the COPRAS, MABAC, and GRA methods were used to rank different renewable energy sources under uncertain conditions. This paper focuses on the tradability of renewable energy projects and analyzes the sensitivity of investment decisions. Aimed at the operation stage of the renewable energy technology project, Egli [20] determined the risks behind new energy investments via 40 interviews with investors from Germany, Italy, and the UK. The long-term ranking of risk types based on interviews shows their relative importance over time, and a network analysis of interview records was used to identify the main drivers behind the observed changes in the importance of each risk type over the course of risk evolution. Yunna et al. [21] considered 32 risk factors, including technology, politics, economy, social environment, and resource risks. Using ANP, 54 countries were divided into six groups for analysis and the cloud model was used to calculate the risk weight. The main risks of China's investments in RE power generation projects in 54 countries were analyzed. Li et al. [22] proposed a group decision-making method for supplier selection that considered the interaction between multi-period fuzzy information and the opinions of decision makers. In this method, decision-makers use generalized fuzzy numbers to provide their preferences in multiple periods and determine the weights in different periods by mathematical programming. Claudia et al. [23] proposed a modeling method based on game theory to analyze the influences of resource complementarity and strategic behavior on the power generation technology selection. They highlighted the research methods of the intersection of game theory and diversification theory, aiming to analyze how resource complementarity affects generator selection and the ultimate energy mix. MEMIŞ et al. [24] applied a bibliometric analysis to evaluate research trends in desalination systems and renewable energy sources from an engineering perspective using optimization or simulation techniques. Jing et al. [25] summarized various risk factors existing in RE investment activities from a macro perspective; on this basis, they provided three evaluation steps regarding whether to invest in a certain RE project. Ximei et al. [26] focused on the analysis of the main risk factors in various historical stages in the development process of RE industry (based on the modeling method of system dynamics). Xie et al. [27] aimed to identify innovative strategies for renewable energy investments via a novel multi-criteria decision-making (MCDM) model based on incomplete preferences, CGDM, and Pythagorean fuzzy sets. Understanding the potential and capabilities needed to produce renewable energy resources is crucial for countries to utilize them and to scale up clean and stable sources of electricity generation [28]. Considering multiple uncertain factors, the literature review is shown in Table 1. Few studies have thoroughly addressed the "Belt and Road Initiative" and its social, economic, and environmental risks [29]. As nations strive for economic growth, they must rely on their pool of


resources, including both natural and intellectual assets [30]. The abbreviations mentioned in the text are in Appendix A.

The investment in clean energy investment projects is typically large, with 70-80% of the investment amount being invested in the early project construction stage. However, the project earnings need to be obtained year-by-year throughout approximately 20 years of the project's life cycle [31]. There is an interdependent relationship between the incidence of risk factors and the factors affecting RE power generation. The key factors influencing RE power generation differ across countries and project operational stages. As a result, RE projects in different countries have different primary risk factors in different periods. Predicting the total risk of the operational period of an RE project can form the foundation for informed project investment decisions; predicting the main risk factors at each stage of the project's operation period can provide technical support for the project's design and management.

Table 1. Review of the methods in the literature.

Based on the characteristics of RE power generation in different countries, this paper focuses on the key factors affecting the RE power generation, establishes the factor-risk dependency relationship, constructs the factor-risk dynamic Bayesian network (DBN) structure, and divides the risk into three levels: high, medium, and low, with the help of the Delphi expert consultation method and cloud model. Using Bayesian inference, we calculate the probability that the annual total risk of the project belongs to the three levels (high, medium, and low), and judge whether the project has investment value. The three risk items with the highest annual risks are selected, the risk factor sensitivity test is carried out, and the corresponding risk reduction measures are given. Finally, the method proposed in this paper is used to evaluate the wind power projects invested by China in Pakistan, and the effectiveness of the method is tested.

The method proposed in this paper is based on a literature review to predict and analyze the factors affecting the RE project from many aspects. The innovation of this paper is to build a Cloud-DBN based on the GM $(1,1)$ algorithm to predict the probability of risk nodes, propose an improved quantitative data normalization processing formula, and propose an improved calculation method for joint conditional probability based on weight and contribution probabilities, reducing the workload of determining numerous joint conditional probabilities and improving the practicality of BN networks with multiple parent nodes.

The structure of the risk prediction method in this paper is shown in Figure 1, and its main contributions are reflected in the following aspects:

- In the DBN graph theory, the risk generation mechanism and evolution process in foreign RE investment are presented, and the probability of risk occurrence is deduced based on the statistical data of observation nodes. The DBN diagram makes the risk prediction structure clear; using statistical data as the starting point of reasoning ensures that the reasoning process is scientific. The probability of risk being high, medium, or low is given, which is highly consistent with the uncertainty and randomness of risk.
- An improved normalization formula for quantitative data processing is proposed. By means of the Delphi expert consultation method and maximum expected parameter learning algorithm based on the cloud model [32], continuous and discrete risk items are uniformly divided into three risk levels: high, medium, and low, which are used as the evaluation criteria for whether a project has investment value. An improved calculation method for joint conditional probability based on weight and contribution probability is proposed, which greatly reduces the workload of determining many joint conditional probabilities. These three steps improve the practicability of BN networks with multiple parent nodes.
- According to the ( 20 years' worth of) historical statistical data on observation nodes, the $\mathrm{GM}(1,1)$ algorithm is used to extract the transfer characteristics of the observation nodes, construct the DBN network, deduce the annual risk probability of each risk node during the RE project operation period, provide the basis for the investment decision in the project planning period, and provide targeted risk reduction measures for the project operation period.
![img-0.jpeg](img-0.jpeg)

Figure 1. RE external investment risk assessment structure.

# 2. Static Bayesian Structure (BN) 

Bayesian reasoning gives the probability of random events in the form of probability, which is especially suitable for the risk assessment of various projects. The basis of Bayesian inference involves the directed acyclic structure graph and joint conditional probability table.

### 2.1. Factor-Risk Dependency Directed Acyclic Structure Diagram

Various reasons or conditions that determine RE'a foreign investments are denoted as factors affecting RE's foreign investments, which can be summarized into three categories. First, reflect the user's demand for RE power-related factors. Second, reflect the international investment environment-related factors. Third, factors related to the level of technological development are represented, as shown in Figure 2. Investment risk refers to the factors that may bring losses to investment returns. There is an interdependent relationship between factors and risks affecting RE projects. Direct factors that may lead to income loss in RE investments include the unit kilowatt-hour cost, feed-in tariff, absorption rate, and financial cost. The uncertainty factors related to the unit electricity costs are the power generation technology risk, RE resource risk, policy risk (loan interest rate; tariff rate), economic risks of power generation, and social and environmental risks. The uncertain factors of the feed-in tariff include the policy risk (subsidy) and the economic risk of the electricity price. The uncertainty factors in the consumption rate include the economic risk of electricity consumption (the economic payment ability of electricity consumption), the technical risk of electricity consumption, the proportion of RE electric energy in the total electric energy, the risk of fossil energy (whether fossil energy can meet the energy demand of the country), the natural environmental risk (whether it is necessary to reduce the consumption of fossil energy by increasing the use of RE, so as to reduce the emission of $\mathrm{CO}_{2}$, improve environmental quality, etc.), and population. These risk factors can be derived from 25 factors, such as RE power generation technology maturity, power grid networking degree, research and development ability, effective utilization time of resources, GDP, CPI, population, etc. The data of these 25 factors are obtained by the World Bank and the U.S. Energy Information Administration (U.S. EIA) and are denoted as observation nodes. According to the above analysis, the Bayesian structure diagram (table of factor-risk dependencies) shown in Table 2 is obtained. "*" in the table represents discrete variables, and the rest are continuous variables. The data of risk nodes and economic nodes in the table are obtained by Bayesian network reasoning.
![img-1.jpeg](img-1.jpeg)

Figure 2. RE external investment risk assessment structure.

Table 2. RE project factor-risk dependency.


Marked with * as a discrete variable.

# 2.2. Normalization Processing of Node Variables 

In the observation node variables, discrete variables are described by language, such as RE generation technology maturity (higher, average, low); continuous variables are represented by specific data, such as tariff rate, GDP, etc. The size and unit of each node's variable are inconsistent, and each variable has randomness and uncertainty. Different evaluation indicators often have different dimensions and dimensional units, which will affect the results of data analysis. In order to eliminate the dimensional impacts among indicators, data normalization processing is needed to solve the comparability of data indicators. After the original data are normalized, each index is in the same order of magnitude, which is suitable for the comprehensive comparative evaluation. In this paper, the risks brought about by each variable to RE investment activities are divided into three levels: S1 (low), S2 (medium), and S3 (high). The practical application can be divided into five, seven, and nine risk levels, according to the needs.

The processing steps for the normalization of observation node variables are as follows:

1. Score the verbal descriptive variables: Based on a large number of historical data and the Delphi expert consultation method, the maximum expected parameter learning algorithm is used to score each linguistic descriptive variable on a scale of 0 to 100.
2. Assign value ranges to variable risk states, S1, S2, and S3: The value ranges of variable risk state partition parameters $m_{i}, a_{i}, n_{i}, b_{i}, \mathrm{~S} 1, \mathrm{~S} 2$, and S 3 are obtained by means of Step (1), as shown in Table 3. Tables 4 and 5 show the risk state division of the 25 observation nodes in Table 2. Table 4 shows the risk classification of discrete variables, and Table 5 shows the risk status classification of continuous variables.

Table 3. Variable risk state division.


Table 4. Risk state division of discrete variables.


Table 5. Risk status division of continuous variables.


3. Determine the value range of state variables S1, S2, and S3 on [0,1]: The expectations for S1, S2, and S3 are Ex1 $=0, \operatorname{Ex} 2=0.5$, and Ex3 $=1$, respectively. According to the cloud generation method of the golden section rate, as the entropy and superentropy move closer to the center of the domain, both entropy and superentropy values decrease. The relationship between the entropy and superentropy of the two adjacent evaluation levels is 0.618 times; that is, $E n 3=E n 1=E n 2 / 0.618, \mathrm{He} 1=\mathrm{He} 3$ $=\mathrm{He} 2 / 0.618$. The rating range on the x -axis is $[\mathrm{Exi}-3 E n i$, Exi +3 Eni]. Therefore, the range of the three evaluation status levels S1, S2, and S3 on the x-axis is [0.3En2/0.618], [0.5-3En2,0.5+3En2], [1-3En2/0.618,1]. In order to ensure that the three evaluation levels cover all the data between $[0,1]$ and stay within the range, it is required that:

$$
\left\{\begin{aligned}
\frac{3 E n 2}{0.618} & \geq 0.5-3 E n 2 \\
0.5+3 E n 2 & \geq 1-\frac{3 E n 2}{0.618} \\
0.5+3 E n 2 & <1
\end{aligned}\right.
$$

Then, for $0.1667>E n 2 \geq 0.064$, if $E n 2=0.07, \mathrm{He} 2=0.005$, the cloud features of the three equivalent evaluations, S1, S2, and S3 are, respectively, [0,0.113,0.0081], $[0.5,0.07,0.005],[1,0.113,0.0081]$. S1, S2, and S3 on the x -axis scope is $[0,0.339],[0.29,0.71]$, and $[0.661,1][32]$.
4. Variable normalization processing: The value of each variable is normalized to its own risk level according to the value range of S1, S2, and S3 in Table 3. The value ranges ofthe S1, S2, and S3 cloud models determined in Step (2) are crossed. The midpoints of the crossing points of S1 and S2 and S2 and S3 are as follows: $\mathrm{A} 1=\frac{3 E n 2 / 0.618+0.5-3 E n 2}{2}$, $\mathrm{A} 2=\frac{0.5+3 E n 2-3 E n 2 / 0.618}{2}$. In this paper, $\mathrm{A} 1=0.3145, \mathrm{~A} 2=0.6855$. The variable $y_{i}$ is normalized according to Formula (2).

$$
\tilde{y}_{i}= \begin{cases}A 1 \cdot \frac{y_{i}-m_{i}}{a_{i}} & m_{i} \leq y_{i}<m_{i}+a_{i} \\ (1-2 A 1) \cdot \frac{y_{i}-\left(n_{i}-b_{i}+m_{i}+a_{i}\right) / 2}{\left(n_{i}-b_{i}\right)-\left(m_{i}+a_{i}\right)}+\frac{1}{2} & m_{i}+a_{i} \leq y_{i}<n_{i}-b_{i} \\ A 1 \cdot \frac{y_{i}-n_{i}}{b_{i}}+1 & n_{i}-b_{i} \leq y_{i}<n_{i}\end{cases}
$$

# 2.3. Probability Calculation of Variable Risk Level 

The level a variable belongs to is reflected in the form of probability, and its probability sum is required to be 1 , as shown in Formula (3).

$$
\sum_{j=1}^{j=3} P\left(\tilde{y}_{i}=S_{j}\right)=1
$$

The variable value after normalization is transferred to the risk level cloud model as the input (features are shown in Section 2.1), and the certainty that the variable belongs to each risk level is obtained. Because the probability value is transmitted in the BN network, the certainty is converted into the probability value by Formula (4) [33].

$$
P\left(\tilde{y}_{i}=S_{j}\right)=\frac{\mu\left(\tilde{y}_{i}=S_{j}\right)^{\frac{1}{n}}}{\sum_{j=1}^{j=3} \mu\left(\tilde{y}_{i}=S_{j}\right)^{\frac{1}{n}}}
$$

The certainty obtained after cloud model processing has a certain randomness, and it needs to calculate the average value after multiple cloud processing to ensure the stability of the membership value.

### 2.4. Joint Conditional Probability

The risk probability of each child node in Table 2 is strongly dependent on the observation node and can be obtained through BN network classification. In the BN network, when the child node has N parent nodes and each parent node has M states, there will be $M^{N}$ joint conditional probabilities. When there are more parent nodes, it takes a lot of work to obtain the joint conditional probabilities. In order to reduce the workload of obtaining joint conditional probability, this paper proposes an improved calculation method for joint conditional probability based on the risk contribution probability and influence weight. The number of improved joint conditional probabilities is shown in Table 6.

Table 6. Number of joint probability conditions.


$N_{q}$ is the sum of the number of variables of the parent and child nodes in the network.

$y_{1}, y_{2}, \cdots, y_{n}$ are the parent nodes of $R$, and their influences on child node $R$ are independent. $\mathrm{P}\left(\mathrm{R}=s_{i} \mid y_{i}=S_{k}\right)$ is denoted as the contribution probability of parent node $y_{i}=S_{k}$ to child node $\mathrm{R}=S_{j}$. Let the influence weights of $y_{1}, y_{2}, \cdots, y_{n}$ on R be $\omega_{1}, \omega_{2}, \cdots, \omega_{n}\left(\sum_{i=1}^{i=n} \omega_{i}=1\right)$, respectively. The joint influence relation of $y_{1}, y_{2}, \cdots, y_{n}$ on R is synthesized according to the "or" operator relation, namely:

$$
P\left(R=S_{j} \mid y_{1}, y_{2}, \cdots, y_{n}\right)=\sum_{i=1}^{i=n} \omega_{i} \cdot \sum_{k=1}^{k=3} P\left(R=S_{j} \mid y_{i}=S_{k}\right) \cdot P\left(y_{i}=S_{k}\right)
$$

The risk contribution probability distribution table is obtained through the EM algorithm experiment, as shown in Table 7. The calculation process of the influence weight is shown in Figure 3, and the joint conditional probability structure is shown in Figure 4.

Table 7. Probability distribution of the risk contribution.


![img-2.jpeg](img-2.jpeg)

Figure 3. Flow chart of the influence weight calculation.
![img-3.jpeg](img-3.jpeg)

Figure 4. Joint conditional probability structure diagram.

The weight of the influence of the parent node on the child node is shown by the red number on the arrow in Figure 5. There are 42 in total. If the traditional method is adopted, the number of joint conditional probabilities to be obtained is:

$$
3^{3}+3^{1}+3^{3}+3^{2}+3^{1}+3^{1}+3^{1}+3^{1}+3^{3}+3^{1}+3^{3}+3^{1}+3^{2}+3^{5}+3^{2}+3^{7}+3^{1}+3^{4}=2670
$$

The comparison shows that the improved joint conditional probability calculation method based on the risk contribution probability and influence weight will greatly reduce the workload of determining the joint conditional probability.

By inputting the obtained joint conditional probability and observation data into the BN network program, the probability that the static risk node, economic node, and RE investment risk belong to S1, S2, and S3 can be obtained. After $\mathrm{P}\left(\mathrm{R}=S_{j} \mid y_{1}, y_{2}, \cdots, y_{n}\right)$ is processed by the integrated cloud generation algorithm, the probability that each variable belongs to a certain risk level can be obtained [34].
![img-4.jpeg](img-4.jpeg)

Figure 5. DBN structure of RE projects invested abroad.

# 3. Dynamic Bayesian Network Structure 

The operation period of the RE project is generally 20-30 years, so it is necessary to investigate the annual investment risk during the operation period of the project. By referring to the idea of the net present value, the annual risk probability should be discounted to the year of the project investment to consider whether the project has investment value. During the operation of the project, the data of the observation node are constantly changing, as well as the risk grade probability. The DBN can effectively predict the variable risk level trend during the project's operation period. DBN is the extension of static BN. The dynamic Bayesian structure of foreign RE investment projects is shown in Figure 5.

$$
\begin{gathered}
R(t)=\sum \omega_{i} \sum \omega_{i j} \sum y_{j k} \omega_{j k} \\
\text { s.t. }\left\{\begin{array}{l}
\sum_{i=1}^{o} \omega R i=1 \\
\sum_{j=1}^{p} \omega R i j=1 \\
\sum_{k=1}^{q} \omega y_{j k}=1
\end{array}\right.
\end{gathered}
$$

where $o$ is the number of parent nodes of $R(t), p$ is the number of parent nodes of $R i(t)$, and $q$ is the number of parent nodes of $\operatorname{Rij}(t)$. The number of parent nodes of each child node varies according to the number of corresponding influencing factors.

It is assumed that the stochastic process satisfies the Markov hypothesis, the BN structure is stable, and the BN reasoning process is stable. The transfer characteristics of the observed node variables are given by the $\mathrm{GM}(1,1)$ algorithm [35]:

$$
\hat{y}(t+1)=\left(e^{-a}-1\right)\left[y(T)-\frac{b}{a}\right] e^{-a(t-1)}
$$

where $\hat{y}(t+1)$ is the $t$ year predicted value of the random variable; $y(T)$ is the initial value of the random variable; $a$ is denoted as the developmental grayscale, indicating the main trend of random variables changing with time; $b$ is denoted as the endogenous control gray level, reflecting the volatility of random variables.

# 4. Risk Analysis of China's Investment in Pakistan's Wind Power Project 

Pakistan is deficient in fossil energy but abundant in wind, hydro, and photovoltaic RE. A coastal corridor extending from Gharo to Geti Bandel to Hyderabad, approximately 180 km in length and 80 km wide, is very suitable for the installation of wind power generation equipment [34]. In 2019, Pakistan's wind and solar power generation only accounted for $3.9 \%$ of the country's total power generation. The main reasons are that Pakistan's economy is relatively backward, its own ability to invest in RE power generation projects is insufficient, and foreign investment risks are high [21], which makes it difficult to attract foreign funds. In order to attract more foreign RE investments into RE projects, the Pakistani government offers preferential policies, such as exemptions on RE equipment tariffs and guarantees of government purchases of electricity generated from the projects.

### 4.1. Experimental Preparation

The data collected from wind power projects in Pakistan in 2017 are shown in Table 8. Based on the characteristics of the RE project, the $\mathrm{GM}(1,1)$ algorithm was used to analyze the statistical data of observational nodes from 1998 to 2017. Over the 20-year project operation period, the data of observation nodes y5, y6, and y25 remained unchanged, and the transfer characteristics of the other observation nodes are shown in Tables 9 and 10.

Table 8. Pakistan wind power observation node data (2017).


Table 9. Pakistan wind power observation node transfer characteristics-1.


Table 10. Data transfer characteristics of Pakistan's wind power observation node-2.


# 4.2. Experimental Simulation 1—Risk Probability Analysis 

Based on historical data, the variable risk state partitioning parameters $\left(m_{i}, a_{i}, n_{i}, b_{i}\right)$, risk probability contribution probability parameters, and joint conditional probability data were trained by the program (the state variables were determined according to the cloud generation method of the golden ratio, the risk probability contribution probability parameters were determined according to the cloud model, and the joint conditional probability data were determined according to DBN), and the observation node data and their transfer characteristic parameters were input into the program for DBN inference. The total investment risk of RE during the project's operation is shown in Figure 6, and the three nodes with the highest annual risks in the past 20 years are shown in Figure 7. The values of the green, yellow, and red columns in Figure 6 represent the probabilities of S1, S2, and S3, respectively. The probability value of S1 slowly decreases, the probability value of S3 slowly increases, and the probability value of S2 slowly increases for 1-9 years, remains stable for 10-15 years, and slowly decreases for 16-20 years. It shows that the total investment risk of RE increases with the operation time of the project, the project risk is low in the first 8 years, the project risk is relatively stable for 9-16 years, and the project risk is relatively high for 17-20 years. In Figure 7, the three dotted columns of green, yellow, and red represent the probabilities of the three nodes with the highest risks in each of the 20 years. In Figure 7, the nodes with the greatest risks over the years are as follows: power generation technical risk (26), policy risk (power generation cost) (28), policy risk (feed-in tariff) (31), economic risk of electricity use (33), technical risk of electricity use (34), financial risk (38), and feed-in tariff (40). In the context of renewable energy project investments-advanced power generation technology, government policies conducive to project development, and electricity settlement prices provided by power generation enterprises have the greatest impacts on project investments. During the operation of the RE project, the distribution of high-risk factors in each stage is shown in Table 11. It can be seen that during the initial stages of China's investment in Pakistan's wind power projects, the primary risk factors were technical (power generation and electricity consumption) and economic risks. In the middle stage, technical risks still existed, and policy risks began to become prominent.

Table 11. Distribution of high-risk factors at each stage of the project's life cycle.


Technical risk of power generation (26) Technical risk of power generation (26) Technical risk of power generation (26) Financial Risks (38)

![img-5.jpeg](img-5.jpeg)

Figure 6. RE total investment risk grade probability during the operation.
![img-6.jpeg](img-6.jpeg)

Figure 7. Distribution of the three nodes with the highest annual risks during the 20 years. The values of the green, yellow, and red dashed columns represent the probabilities of the three riskiest nodes in each of the 20 years.

# 4.3. Experimental Simulation 2—Node Parameter Sensitivity Test 

Four observation nodes, which are closely related to the main risks in Table 11, i.e., RE subsidy, loan interest rate, exchange rate fluctuation level, and corporate income tax, are selected for the risk sensitivity test. The four nodes are increased by $30 \%$, respectively, to observe the fluctuation of the total risk of RE investment.

In Figure 8, the red curve shows the trend of the RE investment risk in the past 20 years without changing the input data. The black, pink, blue, and green curves, respectively, represent the exchange rate fluctuation level, $+30 \%$, corporate income tax, $+30 \%$, loan interest rate, $+30 \%$, and RE subsidy, $+30 \%$. The vertical axis of Figure 8 shows the total risk probability of the RE investment. As can be seen from the figure, the total investment risk of RE is sensitive to the fluctuation level of the exchange rate and corporate income tax. When the two observation nodes (exchange rate and corporate income tax) are $+30 \%$, the total investment risk of RE increases significantly but is less sensitive to subsidy and loan

interest rates. When the two observation nodes (subsidy and loan interest rate) are $+30 \%$, the total investment risk of RE does not fluctuate much.
![img-7.jpeg](img-7.jpeg)

Figure 8. Risk sensitivity test.

# 5. Conclusions 

Following the market-oriented reform of the electric power industry, many risks in foreign investment for RE have surfaced, leading to a reduction in project income, the forced abandonment of RE power, and even the grounding of sizeable investment projects in RE, resulting in significant capital and environmental damage. Therefore, in the planning stage of an RE project, how to effectively conduct risk assessment is an urgent problem that needs to be solved in the field of foreign RE investment.

DBN diagrams clearly express the generation mechanism and evolution process of risks in foreign RE investment. Cloud models can better express the uncertainty and randomness of risks. Observation node information is obtained from statistical data processing, which ensures the scientific reasoning of DBNs. The improved normalization formula for quantitative data and the improved joint conditional probability calculation method based on weight and contribution probability greatly improve the performance of DBN networks with multiple parent nodes.

The method in this paper was applied to risk analysis for China's investment in wind power projects in Pakistan. The simulation results show that the overall risk of the project is low, and is a viable investment, which is consistent with the actual situation, and proves the effectiveness of the method in this paper. The simulation results also show that project risks are sensitive to exchange rate fluctuations and corporate income tax. In project planning, the Chinese side can consider using RMB as the settlement currency to avoid project risks brought about by exchange rate fluctuations and consider in-depth communication with the Pakistani government to negotiate long-term corporate income tax preferential policies and ensure the healthy operation of the RE project. The simulation results also show that in the China-Pakistan wind power project, early-stage technical risks (i.e., electricity and power generation) and economic risks are dominant, medium-term policy risks and technical risks

(i.e., electricity and power generation) are the most prominent, and later-stage feed-in tariff and financial risks are more obvious. China can consider introducing more advanced power generation technologies in Pakistan to reduce technical risks, and negotiate an agreement with the Pakistani government on RE-related policies to ensure the stability of RE feed-in tariffs and the high uptake rate of RE electric energy.

The method proposed in this paper aligns with traditional algorithms. In recent years, the research on neural networks has become a hot topic and has been widely used in risk assessment and prediction. In further research, we will consider the use of appropriate neural networks for risk prediction to improve prediction efficiency and accuracy.

Author Contributions: Conceptualization, methodology, and writing-original draft, W.Z.; writing-review and editing, software, and validation, Y.H.; supervision, H.W. All authors have read and agreed to the published version of the manuscript.
Funding: This work is supported by "the Fundamental Research Funds for the Central Universities", Southwest Minzu Universities (grant no. 2021101). This work is also supported by the National Natural Science Foundation of China (grant nos. 72174172, 71774134).

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data that support the findings of this study are openly available at https://data.worldbank.org.cn and https://www.eia.gov/, accessed in December 2022.
Conflicts of Interest: The authors declare no conflicts of interest.

# Appendix A 

Table A1. Abbreviated list.

