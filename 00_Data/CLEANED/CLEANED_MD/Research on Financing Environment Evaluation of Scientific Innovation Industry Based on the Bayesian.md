# Research on Financing Environment Evaluation of Scientific Innovation Industry Based on the Bayesian Network Model under the Background of Green Economy 

Chengxuan Geng, Bihan Wen*, Rui Liu**<br>College of Economics and Management, Nanjing University of Aeronautics and Astronautics, Nanjing Jiangsu 211106 China

Received: 7 April 2023
Accepted: 14 July 2023


#### Abstract

As the global environmental crisis evolves, China's traditional industries have serious problems of high energy consumption, high emission and low energy efficiency. Developing green industries has become an important direction of China's industrial transformation and upgrading. This paper selects scientific innovation industry as a typical representative of green industry and studies its financing environment assessment. In order to solve the financing dilemma faced by the science and technology innovation industry, this paper puts forward the evaluation method of the financing environment of science and technology innovation industry based on Bayesian network from the Angle of industry particularity. In this paper, Netica software is used to construct a Bayesian network model of the financing environment of the science and technology innovation industry, and the financing environment of the science and technology innovation industry in 2016-2020 is inferred according to the annual probability distribution. Then, the sensitivity analysis is carried out, and the hierarchical policy simulation is used to simulate the conditional probability of the initial node and the intermediate node respectively, so as to determine the impact of each node on the financing environment, and finally obtain the optimization path. The research results can be of great value for improving the financing environment of scientific innovation industry and promoting the development of green industry.


Keywords: environmental crisis, green economy, scientific innovation industry, financing environment, Bayesian networks

[^0]
[^0]:    *email: Wenbihan98@163.com
    **email: Ruiliu_68@163.com

## Introduction

Since the industrialization of the world, the global climate environment has continued to deteriorate. If no effective measures are taken, the global temperature will rise by $3.7 \sim 4.8^{\circ} \mathrm{C}$ in 2100 , and the global climate change is developing in a disastrous direction. In October 2020, 127 countries signed the Paris Agreement, making carbon neutrality a common action for all countries in the world. Due to the rapid economic development, China has become the world's largest energy consuming country since 2009. In order to do a good job in energy conservation and emission reduction, the Chinese government has put forward the goal of "2030 carbon peak and 2060 carbon neutral" in 2020.

In the traditional industrial structure, China's energy endowment is "more coal, less oil, less gas", and coal accounts for about 60 percent of energy supply. Traditional industries have serious problems of high energy consumption, high emissions and low energy efficiency, posing a major threat to the environment. In order to achieve the goal of "double carbon", developing green industries has become an important direction of China's economic structural transformation and upgrading. Scientific innovation industry is a new and green industry characterized by high and new technology, and it is the key field of green economy development. Scientific innovation industries adhere to the concept of green development, which plays an important role in promoting high-quality economic growth and protecting the environment.

The ability of scientific and technological innovation is an essential guarantee for China to win the advantage in today's international competition [1], and the realization of independent scientific and technological innovation cannot be achieved without the support of the scientific innovation industry [2]. The scientific innovation industry and science and technology innovation board arose in Europe and America. Since its establishment in 1971, NASDAQ has completed multiple stages of innovation and development and now covers software, computer, biotechnology, and other high-tech industries, becoming a capital market of science and technology innovation for economic development [34]. The $14^{\text {th }}$ Five-Year Plan released in 2020 calls for improving the quality interaction between science and technology, finance and industry. With the support of the policy, our scientific innovation capability has been strengthened in recent years. However, compared with developed countries, the Chinese scientific innovation industry has problems such as a lack of core technology, a low conversion rate of science and technology achievements, and a lack of self-owned brands. Capital plays a vital role in the development of scientific and technological innovation [5], and the support of financial capital plays an essential role in promoting the development of the scientific innovation industry [6]. Therefore, a high-quality financing environment is a basis for the development of the scientific innovation industry. It is of great significance to clarify the mechanism of the scientific innovation industry's financing environment for the industry's survival and development.

Compared with traditional industries, although the scientific innovation industry has the advantages of high yield, high return, talent and innovation [7], on the other hand, it also has high uncertainty risks, including environmental risks, technological risks, market risks and management risks, due to the confidentiality and information asymmetry of its R\&D and innovation activities [8]. As a result, the financing environment of the scientific innovation industry is complicated and severe and urgently needs to be solved [10]. Presently, domestic and foreign scholars' research on the evaluation and analysis of the financing environment can be divided into two parts: the classification of the financing environment and the evaluation method. In terms of the division of financing environment, Zhao et al. put forward the optimization direction of the financing environment based on the different analyses of the policy environment, tax environment, bank credit environment and capital market environment of technological SMEs in the United States, South Korea and China [11]. Kang Jianping et al. evaluated the financing environment of local small and micro enterprises from the perspective of financing development, availability and efficiency [12]. For specific industries or regions, some scholars have divided the financing environment into the entrepreneurial environment, legal environment [13-14], ecological environment [15] and humanistic and social environment [16]. In terms of financing environment evaluation methods, the traditional evaluation methods include the entropy weight method, factor analysis method [17], analytic hierarchy process [16], principal component analysis method [18] and correlation analysis method [19]. Then some scholars have integrated the triangular fuzzy number [20] and system dynamics method [21] with the traditional evaluation methods. However, as an emerging industry, there are few types of research on the financing environment evaluation of the scientific innovation industry. The above evaluation systems and methods for the financing environment have their own advantages in research and application. However, due to the regional, industrial and static nature of the research perspective, they cannot be fully applied to the scientific innovation industry.

Bayesian networks were proposed by Pearl [22] after combining the prior probability thought obtained by Bayes [23] and the Jeffreys criterion discovered by Jeffreys [24]. As an organic combination of probability theory and graph theory, Bayesian networks can process much random information well. By applying the Bayesian network method, domestic and foreign scholars have made certain research achievements. Fu et al. applied it to fault diagnosis and elimination of integrated circuit test probes [25], Wang et al. applied it to scenario analysis under the cognitive uncertainty of scientific and technological accidents [26], and Cao

applied it to personal credit evaluation. To predict the default risk of future borrowers [27], Wang et al. applied it to predict the probability of technological progress to get the path of technological optimization [28], Li et al. combined it with the explanatory structure model to build the risk identification and early warning model of social media network public opinion under emergencies [29], Bai et al. combined it with the rough set theory. The probabilistic decision reasoning of watershed water quality is realized [30]. The above studies are analyzed from the perspectives of risk assessment, fault diagnosis, scenario simulation and path optimization, indicating that in Bayesian networks, probability theory can be used to reason uncertainty, and graph theory can be used to make the relationship between variables more intuitive and clear. Through the dynamic changes of each factor policy simulation [31].

Given the deficiencies of the classification and evaluation methods of the financing environment of the scientific innovation industry in the existing studies, in order to more scientifically clarify the composition of its financing environment and evaluate and analyze the characteristics of the high-risk and high-uncertainty of the scientific innovation industry, this paper innovatively proposes to use the Bayesian network method to evaluate the financing environment. Through Netica software, the financing environment evaluation model designed for the scientific innovation industry was constructed, and the hierarchical policy simulation was carried out to obtain the optimization path and put forward countermeasures and suggestions. Therefore, the main innovation of this study lies in (1) the establishment of a financing environment evaluation system only for scientific innovation industry, and (2) the introduction of Bayesian network method in the financing environment evaluation research field. And the contribution of this study is that it can not only improve the relevant research on the construction of financing environment evaluation system for special industries in order to make the evaluation results more targeted and accurate, but also the introduction of Bayesian networks is helpful to expand the methods and ideas of related research.

## Materials and Methods

## Bayesian Network

The Bayesian network, first proposed by Pearl, mainly solves the problem of uncertain knowledge representation through probability and graph theory [32]. By referring to the research of Qu et al., the modeling ideas of the Bayesian network model can be obtained as follows [33]:

Assuming that the model has independently distributed condition variables, then:

$$
\begin{aligned}
& p(b \mid a)=p(b), p(s \mid a, b)=p(s) \\
& p(g \mid a, b, s)=p(g \mid a), p(j \mid a, b, s, g)=p(j a, b, s)
\end{aligned}
$$

Meanwhile, the variable control expression of the parameter is as follows:

$$
\phi_{i j k}=p\left(x_{i}^{k} \mid p d_{i}, Z^{k}, \sigma\right)
$$

The above formula $\sigma$ describes the cumulative knowledge level of the corresponding $Z^{k} p d_{i}$ sample. Represents the parent node set of the discrete sample $x_{i j}{ }^{k}$ under a prior probability.

Then, the parameter estimation and hierarchical progression of Bayesian network learning mainly include three aspects:

Step 1: Parameter learning
$x_{i j}{ }^{k}$ can be used as a set of continuous node variables when the Bayesian network learns the evaluation sample. The specific description is as follows:

$$
\begin{aligned}
p\left(\phi_{i} \mid Z^{k}, \sigma\right) & =\prod_{i=1}^{n} \prod_{j=1}^{N} p\left(\phi_{i} \mid Z^{k}, \sigma\right)=\prod_{i=1}^{n} \prod_{j=1}^{N} \operatorname{dir}\left(N_{i j 1}^{t}, \ldots, N_{i j 1_{i}}^{r}\right) \\
& =\prod_{i=1}^{n} \prod_{j=1}^{N} \frac{\Gamma \prod_{k=1}^{r} N_{i j k}^{t}}{\prod_{i=1}^{r} \Gamma\left(N_{i j k}^{t}\right)} \prod_{k=1}^{r} \phi_{i j k}^{N^{t}}
\end{aligned}
$$

Where $N_{i j k}^{r}=N^{N} p\left(X_{i}=k, p a_{i}=j \mid Z_{C}^{k}, \sigma\right)$.
Meanwhile, Bayesian network learning with posterior probability conditions is as follows:

$$
\begin{aligned}
p\left(\phi_{i} \mid D, Z^{k}, \sigma\right) & =\prod_{i=1}^{n} \prod_{j=1}^{N} p\left(\phi_{i} D_{i} \mid Z^{k}, \sigma\right)=\prod_{i=1}^{n} \prod_{j} \operatorname{dir}\left(N_{i j 1}^{t}+N_{i j 1}, \ldots, N_{i j 1}^{t}+N_{i j j}\right) \\
& =\prod_{i=1}^{n} \frac{\Gamma \prod_{k=1}^{r} N_{i j k}^{t}\left(N_{i j k}^{t}+N_{i j k}\right)}{\prod_{i=1}^{r} \Gamma\left(N_{i j k}^{t}+N_{i j k}\right)} \prod_{k} \phi_{i j k}^{N^{t}}
\end{aligned}
$$

The above formula $N_{i j k}$ represents the probability of samples of sample element set $C_{i}$ under the conditions of $X_{i}=x_{i}^{k}, p a_{i}=j$.

Step 2: Structural learning
Network structure learning is mainly to further optimize the sample, and the main strategies are as follows:

$$
p Z^{k} \mid D=\frac{p\left(Z^{k}\right) p\left(D \mid Z^{k}\right)}{p(D)}
$$

Where $Z^{k}$ stands for hypothesis set, $Z$ structure set, $p\left(Z^{k}\right)$ and hierarchical learning probability.

Step 3: Probabilistic learning
Dynamic Bayesian network learning is mainly obtained through a prior and a posterior joint distribution

calculation, $N_{i j}^{\prime}=\sum_{k=1}^{n} N_{i j k}^{\prime}, N_{i j}=\sum_{k=1}^{n} N_{i j k}$ respectively. The specific calculation formula is as follows:

$$
\begin{aligned}
& p\left(x_{n} \mid x_{1}, \ldots, x_{n-1}, \phi_{S}, D, Z^{h}\right) p\left(\phi_{S} \mid D, Z^{h}\right) d \phi_{S} \\
& =\int \sum_{i=1}^{n} \phi_{i j k} p\left(\phi_{S} \mid D, Z^{h}\right) d \phi_{S}=\sum_{i=1}^{n} \int \phi_{i j k} p\left(\phi_{S} \mid D, Z^{h}\right) d \phi_{S} \\
& =E_{F}\left(\phi_{S} \mid D, Z^{h}\right)\left(\sum_{i=1}^{n} \phi_{i j k}\right)=\sum_{i=1}^{n} \sum_{j=1}^{n} \frac{N_{i j k}^{\prime}+N_{i j k}}{N_{i j}^{\prime}+N_{i j}}
\end{aligned}
$$

## Entropy Weight Method

Entropy is an index to measure the disorder degree of information in a specific system, which can make full use of the original data information [34]. In Bayesian network learning, the entropy weight method is used to determine the weight of the evaluation index. According to the research of Wang et al. [35], the entropy weight method needs to go through three steps: data standardization processing, data variation degree calculation and weight integration. The details are as follows:

Step 1: Standardized processing of index data
Because each indicator's units are inconsistent, the data must be standardized in calculating indicator weight and comprehensive evaluation. According to the different positive and negative properties of the impact of indicators on the financing environment, the corresponding formulas are adopted, as shown in formula (7) and formula (8). Among them, the positive index indicates that the index positively impacts the financing environment of the scientific innovation industry. In contrast, the negative index indicates that the index harms the financing environment of the scientific innovation industry.

Positive indicators:

$$
x_{i j}^{\prime}=\frac{x_{i j}-x_{\min }}{x_{\max }-x_{\min }}
$$

Negative indicators:

$$
x_{i j}^{\prime}=1-\frac{x_{i j}-x_{\min }}{x_{\max }-x_{\min }}
$$

Step 2: Entropy calculation
Entropy is an indicator to measure the degree of information disorder in a specific system. The entropy $e_{j}$ of the JTH indicator is calculated by the following formula:

$$
e_{j}=\frac{-\sum_{i=1}^{m} p_{i j} \ln p_{i j}}{\ln m}
$$

Where $p_{i j}=\sum_{i=1}^{m} x_{i j}^{\prime}$.
Step 3: Variation degree of index data calculation
The varying degree of indicator data during the sample period $D_{j}$ represents the proportion of each indicator data in the index in each year. The greater the degree of variation, the greater the influence of this index. The specific calculation formula is as follows:

$$
D_{j}=1-e_{j}
$$

Step 4: Index weight calculation
Entropy weight $\omega_{j}$ is the index weight calculated by the information size of the data entropy value. The specific calculation formula is as follows:

$$
\omega_{j}=\frac{D_{j}}{\sum_{j=1}^{n} D_{j}}
$$

Fig. 1 shows how to evaluate the financing environment of the scientific innovation industry with the Bayesian network learning method.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Environmental assessment thinking of the scientific innovation industry based on the Bayesian network.

## Data Sources and Descriptive Statistics

By combing and reviewing relevant literature, this paper finds that establishing a scientific and reasonable evaluation index system for the financing environment of the scientific innovation industry should not only consider the needs of the financing environment of the scientific innovation industry but also consider the systematization, completeness and comparability of the evaluation system. When analyzing the criterion level of the financing environment of the scientific innovation industry, this paper draws on the research of Yan et al. [36] and divides the financing environment of the scientific innovation industry into five criterion-level sub-environments as shown in Fig. 2: economic environment, financial market environment, scientific innovation industry environment, financial credit environment and fiscal policy environment, among which the main components are the industrial environment, financial credit environment and fiscal policy environment.

These independent evaluation indicators completely explain the financing environment of the scientific innovation industry from five different perspectives:

Economic environment is the most basic external environment in the financing environment of science and innovation industry. When the total national economy is at different levels of development, the demand for funds of enterprises will also change. And as one of the important factors affecting macroeconomic environment, GDP is often used by scholars as an indicator to reflect the level of regional economic development [37].

Financial market environment is the most direct financing environment for the scientific and creative industry to carry out financing activities, which reflects the degree of play of the intermediary role of financial institutions, the diversity of financial instruments and the perfection of financial markets. Scholars believe that the balance of deposits and loans of financial institutions reflects the performance of its intermediary function [38-39].

Industrial environment can most directly reflect the particularity of the financing environment of the science and innovation industry itself, and the development of the science and innovation industry is an important
basis for investors to judge the profitability of science and innovation enterprises and the internal driving factor to promote the successful financing of enterprises. Scholars usually divide the scientific innovation industry environment into three aspects: input, output and effectiveness [37], which respectively reflect the industrial infrastructure, the production capacity of scientific innovation results, and the efficiency relationship between input and output [40].

Financial credit environment is an indispensable factor for the smooth operation of the financial market in which the scientific and creative industry is located. For example, for the science and innovation industry, information asymmetry will exacerbate the deterioration of the financial credit sub-environment. And scholars believe that based on the special national conditions of China, it is more practical to describe the financial credit environment with the situation of private lending based on geographical relations [36].

Fiscal policies related to the scientific innovation industry are mainly reflected in the state's allocation and financial incentives in tax [40], and financial incentives are the main measures for the government to encourage the industry to strengthen the training of scientific and technological innovation ability.

Based on the above analysis of the five subenvironmental factors affecting the financing environment of scientific innovation industry, this paper selects 17 specific indicators of the index layer, and the evaluation indexes of the criterion layer and index layer of the scientific innovation industry financing environment are shown in Table 1.

The research scope of this paper is five subenvironments of the financing environment of China's scientific innovation industry from 2016 to 2020, among which the relevant data of the economic subenvironment and financial market sub-environment are from the China Statistical Yearbook and the relevant data of the industrial sub-environment are from China Innovation Index Research. The relevant data from the credit sub-environment are from China's judicial documents network (https:// wenshu.court.gov.cn/), and the relevant data from the fiscal policy sub-environment are from the China statistical yearbook of science and technology.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Sub-environment composition of the scientific innovation industry financing environment.


#### Table 1. Evaluation index of the financing environment of the scientific innovation industry.

*Geng C., et al.*

Table 2. The index weight of scientific innovation industry financing environment evaluation.


## Results and Discussion

## Data Processing of Scientific Innovation Industry <br> Financing Environment Evaluation Model

(1) Index weight determination based on the entropy weight method

Based on the entropy weight method, the weight of influencing factors of each index layer can be calculated, and then the weight of index data of the corresponding criterion layer can be obtained by the comprehensive evaluation index method. The weights obtained through consolidation are shown in Table 2.
(2) Index grading

After confirming the weights of each evaluation index, in order to better study the financing environment of the Chinese scientific innovation industry in different years, this paper uses the distance method to grade the evaluation index of the financing environment by referring to relevant studies [41]. The specific calculation formula is shown in Formula (12):

$$
P\left(x_{j} \mid y_{i j}\right)=\frac{\frac{1}{L_{i j}}}{\sum_{i=1}^{2} \frac{1}{L_{i j}}}
$$

where $x_{j}$ represents the actual value of the JTH index; $y_{i j}$ represents the standard value of the JTH index when the level of financing environment condition is $i ; L_{i j}\left|x_{j}-y_{i j}\right|$, the greater the absolute value of the difference between the actual value of the index and the standard value of the corresponding level, the smaller the probability of the index is divided into the evaluation level in the actual situation. Based on the data of the financing environment evaluation index of China's scientific innovation industry from 2016 to 2020, Formula 12 is used to calculate the index classification results for each year, as shown in Table 3.

The grading result of the index layer in the table is the initial node probability of Bayesian network learning.

Bayesian Network Learning of Scientific Innovation Industry Financing Environment Evaluation
(1) Structural learning of Bayesian network

Based on the above classification of assessment indicators for the financing environment of the scientific innovation industry and the independent relationship among all indicators, the initial Bayesian network topology, as shown in Fig. 3, can be obtained: The financing environment for scientific innovation industry in our country consists of the macro-economic environment, financial market environment, financial credit environment and fiscal policy environment, and each sub-environment influences each other independently.

Combined with the parameter and Probabilistic learning results of the Bayesian network evaluation model for the financing environment of the Chinese scientific innovation industry from 2016 to 2020, the final network structure and the corresponding node probabilities of indicators at each level are input into Netica software to obtain the action path of the impact indicators of the financing environment in each year and the final evaluation results.
(2) Parameter learning of Bayesian network

After determining the initial structure of the Bayesian network, the parameter learning of the Bayesian network is to deduce each parameter in the Bayesian network model, namely the probability distribution of each node. In this paper, the Bayesian estimation method is used to study parameters. Take the credit sub-environment in 2016 as an example. The learning results of parameters are shown in Table 4:

The Result of the Financing Environment Evaluation of the Scientific Innovation Industry
(1) Overall financing environment evaluation result

After completing the construction of the evaluation model for the financing environment of the scientific innovation industry, according to the learning results of the structure and parameters of the Bayesian network evaluation model for the financing environment of

Table 3. The index grading result of scientific innovation industry financing environment evaluation.


the scientific innovation industry during 2016-2020, input the node probability corresponding to the network structure and indicators at each level into Netica software. Then we get the conduction path of the financing environment index and the final evaluation result. By summarizing the reasoning results, we can get the changing trend of the financing environment of China's scientific innovation industry from 2016 to 2020, as shown in Fig. 4.

As can be seen from Fig. 4, the probability of a poor financing environment is always more significant than the probability of a good condition. According to the principle of maximum probability, the financing environment of the Chinese scientific innovation industry in the past five years is not optimistic. Further, it can be found that the probability of a favorable environment fluctuates in the five years, showing a trend of decreasing first and then increasing. The probability

![img-2.jpeg](img-2.jpeg)

Fig. 3. Bayesian network structure for Financing Environment evaluation of Scientific innovation industry.

Table 4. Parameter learning result of credit sub-environmental in 2016.


![img-3.jpeg](img-3.jpeg)

Fig. 4. The changing trend of the evaluation result of the financing environment of the scientific innovation industry from 2016 to 2020.
of a favorable environment increased rapidly after reaching the lowest point of $33.3 \%$ in 2018, and the increase rate in the following two years was significantly higher than the decrease rate in the previous two years and increased to $45.9 \%$ in 2020. This must be separated from the announcement of the establishment of the Science and Technology Innovation Board in 2018 and the official opening of the board in 2019. Establishing a science and technology innovation board is an important reform measure for China to implement an innovationdriven strategy, strengthening science and technology and promoting economic and social development.

Regarding market function, the science and technology innovation board makes our scientific and technological innovation and capital market a further in-depth combination. Scientific and technological innovation activities are characterized by high investment, long cycles and high risk. Short-term and indirect financing is often powerless in this field, while the survival and development of the scientific innovation industry need the guidance and catalysis of long-term funds. Therefore, with the help of the SciTech innovation board, the financing environment of the Chinese scientific innovation industry shows an accelerated optimization state after 2018, and the development prospect is good.
(2) Sub-environment evaluation result

According to the reasoning results, the year-by-year trend of the sub-environmental evaluation results of the financing environment of China's scientific innovation industry from 2016 to 2020 is shown in Fig. 5.

Fig. 5 shows the year-by-year trend of each subenvironment of the criterion layer. Fig. 5(a) shows the changing trend of the economic sub-environment. It can be seen from the figure that the probability of the economic sub-environment being good increased steadily from 2016 to 2019 but dropped somewhat in 2020. The steady rise is mainly because the country gradually adapted to the transition of economic development, and the capital market is increasingly perfect and constantly optimized, making our country's economic environment present a stable and sound development trend. The economic sub-environment fell back to the same level as 2018 in 2020, mainly due to the impact of the novel coronavirus epidemic. All walks of life were hit by sudden shocks, negatively affecting the overall macroeconomic environment.

Figs 5(b) and 5 (c) show the financial market and industrial sub-environment. Their year-to-year trend is consistent with the overall financing environment. However, in terms of concrete data, the favorable probability of the financial market sub-environment is far lower than other sub-environments, which means that the financial market conditions of our scientific innovation industry still have significant room for improvement. To study the reason, our country is still taking bank loans as the primary way of gradual financing, with four banks as the dominant bank system occupying the main financing channel, leading to the uneven development of the financial market environment. Therefore, the financing structure of the scientific innovation industry needs to be further optimized to improve financing efficiency.

Fig. 5d) shows the changing trend of the financial credit sub-environment. As can be seen from the figure, the credit sub-environment presents an overall development trend of rising-falling - flat, and the overall change is not significant. In addition, the credit subenvironment has a significantly higher probability of being in good condition than other sub-environments and is the only sub-environment stably maintained in good condition. This shows that although the scientific innovation industry has the problem of a credit crisis caused by information asymmetry, the overall credit environment has always been in good condition.

Fig. 5e) shows the changing trend of the fiscal policy sub-environment. Compared with the first four subenvironments, the fiscal policy environment fluctuates the most, showing an upward-downward-upward change in five years. In 2019, the probability of a favorable fiscal policy environment was higher than that of a poor environment, reaching $66.1 \%$. This shows that policy support plays a non-negligible role in the process of promoting the financing environment of the science and technology innovation board. On the whole, although the

![img-4.jpeg](img-4.jpeg)

Fig. 5. The changing trend of the evaluation result of the sub-environment of the scientific innovation industry from 2016 to 2020. a) Economic sub-environment, b) Financial market sub-environment, c) Industrial sub-environment, d) Credit sub-environment, e) Fiscal policy sub-environment
financing environment of China's scientific innovation industry fluctuated during 2016-2020, it showed a state of continuous optimization in the later period.

## Evaluation Result Test

In order to further prove the feasibility of using the Bayesian network method to evaluate the financing environment, this paper will use the comprehensive evaluation index method to test the above evaluation results.

The comprehensive evaluation index method has been widely used in the evaluation field, and its index normalization method is simple and intuitive. Therefore, by referring to the research of Zhang et al. [42], this paper uses the comprehensive evaluation index method to conduct an annual comprehensive evaluation of the investment environment of the scientific innovation industry and then tests the results compared with the results of the Bayesian network model. The relevant results are shown in Fig. 6.

According to the comparison results shown in the figure above, although the evaluation results of the two methods differ in specific probability values due to different calculation mechanisms, the overall change trend of the evaluation results of the two methods is the same, showing a downward-upward trend, which verifies the feasibility of applying Bayesian networks to this field.

## The Optimization Path of Financing Environment of the Scientific Innovation Industry

The industrial sub-environment, credit subenvironment and fiscal policy sub-environment are highly correlated with the scientific innovation industry itself, and optimizing the index with the highest secondlevel weight can most effectively promote improving the financing environment. Therefore, the optimal path of each sub-environment can be obtained through simulation. In order to better compare the impact of the changes of various influencing factors on the

![img-5.jpeg](img-5.jpeg)

Fig. 6. Comparison of evaluation results between the synthetic index method and Bayesian network method.
optimization of the financing environment, this paper sets the change rate of all indicators as $10 \%$, while other indicators remain unchanged. Netica software is used to simulate and analyze the optimization path of these three sub-environments, and the results are as follows.

Fig. 7 shows the impact degree of improving different industrial variables on improving the financing environment and the comparison result of the optimization ratio of the three paths. It can be seen from the figure that the optimization effect of strengthening the output and effect of science and innovation on the financing environment is significantly higher than that of increasing investment in science and innovation, and the effect of developing science and innovation over time is higher than that of science and innovation output. Therefore, the government and enterprises should not blindly believe that increasing investment in science and innovation can be a permanent solution but should pay more attention to the production, creation and utilization of science and innovation products and services.

Fig. 8 shows the influence degree of improving different credit environment variables on the
improvement of the financing environment. Reducing loan litigation cases has a certain positive effect on the optimization of the financing environment. However, the effect is not very significant, and improving loan disputes has a slightly higher optimization effect on the financing environment than improving loan disputes. The reason, according to the above model evaluation results, it can be seen that the credit environment is the only sub-environment that can be stably maintained in a good state, so the improvement of the indicators under this sub-environment will not have a significant effect on the improvement of the financing environment of the scientific innovation industry.

Fig. 9 shows the improvement of the influence degree of different fiscal policy environment variables on improving the financing environment. It can be seen that no matter what kind of policy preferences have a promoting effect on the optimization of the financing environment of the scientific innovation industry, increasing the proportion of scientific and technological appropriations in financial appropriations has a more substantial effect on the optimization of
![img-6.jpeg](img-6.jpeg)

Fig. 7. The influence of the improvement of different industrial environment variables on the optimization of the financing environment.

![img-7.jpeg](img-7.jpeg)

Fig. 8. The influence of the improvement of different credit environment variables on the optimization of the financing environment.

![img-8.jpeg](img-8.jpeg)

Fig. 9. The influence of the improvement of different fiscal policy environment variables on the optimization of the financing environment.

financing environment than increasing the proportion of enterprises with additional deduction and tax exemption. Therefore, for the country and the government to optimize the financing environment of the scientific innovation industry more effectively, it is necessary to focus on adjusting the proportion of science and technology appropriations and other financial appropriations. Compared with traditional industry, the scientific innovation industry is still in the beginning of development, so the government's allocation of science and technology is particularly needed. Therefore, increasing the proportion of scientific research funds in the scientific innovation industry can reduce the risk of research in the field of science and innovation, promote the enthusiasm of science and innovation talents, thus improving the output level of scientific innovation, and optimize the financing environment and promote industrial development, forming a virtuous circle.

To sum up, the improvement of the three approaches of the scientific innovation industry environment, financial credit environment and fiscal policy environment has a positive promoting effect on the financing environment of the scientific innovation industry. Among them, the criterion sub-environment with the most significant optimization effect on the financing environment is the industrial sub-environment, followed by the fiscal policy and credit sub-environment. Moreover, the scientific innovation effect index is the most effective in the scientific innovation industry environment. Therefore, strengthening the scientific innovation ability of the industry is more effective for optimizing the financing environment of the scientific innovation industry than improving the external influencing factors.

# Conclusion

According to the particularity of the financing environment of the scientific innovation industry, this paper innovatively constructs a Bayesian network-based financing environment evaluation model for China's scientific innovation industry which is deduced by the year-by-year grade probability distribution of each sub-environmental index, and the main conclusions are as follows:

(1) Construct the financing environment evaluation model of the scientific innovation industry using a Bayesian network. Through network learning, it is found that the financing environment of the Chinese scientific innovation industry still needs to be improved in recent years, but the overall development trend is gradually improving.

(2) Using a Bayesian network to conduct policy simulation to obtain the path to optimize the financing environment of the scientific innovation industry. The optimization effect of the criterion layer environment on the financing environment from the largest to the smallest is as follows: industrial

environment $>$ fiscal policy environment $>$ credit environment. In the industrial sub-environment, the most effective is the scientific innovation effect index.
(3) According to the optimization effectiveness of different financing environment paths, strengthening the industry's own scientific innovation output capacity, increasing the proportion of national science and technology appropriation, and improving the industrial environment and fiscal policy environment can optimize the financing environment and promote industrial development at the same time, forming a virtuous cycle.
(4) The test results of the comprehensive index method are satisfactory, which proves that the innovative use of the Bayesian network method to evaluate the financing environment of the scientific innovation industry is scientific and reasonable and provides a new idea for the financing environment evaluation.

## Acknowledgments

This paper is supported by the project "Research on the Driving Mechanism and Promotion Path of the market-oriented Allocation of Scientific Innovation Industry Elements under the Background of Digital Economy". The project approval number is 22BJL140.

## Conflict of Interest

The authors declare no conflict of interest.
