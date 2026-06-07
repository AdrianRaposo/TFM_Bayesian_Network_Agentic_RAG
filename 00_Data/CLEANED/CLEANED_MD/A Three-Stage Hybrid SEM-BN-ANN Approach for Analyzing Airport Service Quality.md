# Article 

## A Three-Stage Hybrid SEM-BN-ANN Approach for Analyzing Airport Service Quality

Thitinan Pholsook ${ }^{1}$, Warit Wipulanusat ${ }^{2, * *}$, Poomporn Thamsatitdej ${ }^{3}$, Sarawut Ramjan ${ }^{3}$, Jirapon Sunkpho ${ }^{3}$ and Vatanavongs Ratanavaraha ${ }^{1 *}$


#### Abstract

check for updates Citation: Pholsook, T.; Wipulanusat, W.; Thamsatitdej, P.; Ramjan, S.; Sunkpho, J.; Ratanavaraha, V. A Three-Stage Hybrid SEM-BN-ANN Approach for Analyzing Airport Service Quality. Sustainability 2023, 15, 8885. https://doi.org/10.3390/ su15118885

Academic Editor: Marinella Giunta

Received: 27 April 2023
Revised: 21 May 2023
Accepted: 25 May 2023
Published: 31 May 2023


## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Transportation Engineering, Institute of Engineering, Suranaree University of Technology, Nakhon Ratchasima 30000, Thailand; thitinan.p@g.sut.ac.th (T.P.); vatanavongs@g.sut.ac.th (V.R.)
2 Thammasat University Research Unit in Data Science and Digital Transformation, Department of Civil Engineering, Faculty of Engineering, Thammasat School of Engineering, Thammasat University, Pathumthani 12120, Thailand
3 Thammasat University Research Unit in Data Science and Digital Transformation, College of Innovation, Thammasat University, Bangkok 10200, Thailand; poomporn@citu.tu.ac.th (P.T.); sarawut@citu.tu.ac.th (S.R.); jirapon@tu.ac.th (J.S.)

* Correspondence: wwarit@engr.tu.ac.th


#### Abstract

The novel coronavirus (COVID-19) outbreak has impacted the aviation industry worldwide. Several restrictions and regulations have been implemented to prevent the virus's spread and maintain airport operations. To recover the trustworthiness of air travelers in the new normality, improving airport service quality (ASQ) is necessary, ultimately increasing passenger satisfaction in airports. This research focuses on the relationship between passenger satisfaction and the ASQ dimensions of airports in Thailand. A three-stage analysis model was conducted by integrating structural equation modeling, Bayesian networks, and artificial neural networks to identify critical ASQ dimensions that highly impact overall satisfaction. The findings reveal that airport facilities, wayfinding, and security are three dominant dimensions influencing overall passenger satisfaction. This insight could help airport managers and operators recover passenger satisfaction, increase trustworthiness, and maintain the efficiency of the airports in not only this severe crisis but also in the new normality.


Keywords: airport service quality; passenger satisfaction; structural equation modeling; Bayesian network; artificial neural network

## 1. Introduction

Airports are one of the crucial parts that drive the aviation industry, so service quality is critical to the operation and management of airports. Airports Council International (ACI) developed the Airport Service Quality (ASQ) program in 2006 to measure passengers' perceptions of airport service quality and passenger satisfaction [1]. ACI regularly surveys and evaluates airport performance based on 34 service attributes divided into eight categories: access, check-in, passport control, security, navigation, facilities, environment, and arrival [2] This becomes a standard indicator of airports' performance worldwide. With nearly 400 participating airports across 95 countries since ACI first introduced the ASQ program, it has become the world's most successful airport passenger satisfaction initiative [3]. Based on data from ASQ's Surveys, ACI World's annual ASQ Awards honor airport excellence in customer experience globally. Survey results are used to determine how well an airport performs in awards [1]. In addition to the ASQ Awards during the pandemic, the Voice of the Customer Recognition program honors airports that have made notable efforts to collect passenger feedback. Airports can gain a distinct understanding of consumer experience through ASQ's departures, arrivals, and commercial surveys [3]. Airports may improve the customer experience, service levels, and non-aeronautical revenue

by using the results of the ASQ to gauge passenger satisfaction and find solutions. High customer satisfaction with airport services is necessary to maintain high customer loyalty.

Many scholars have studied ASQ measurement with a focus on passenger perception of airport services. These studies investigate which service dimensions are the weakness of their airport that affect the overall service level, and they could improve that service to increase the service level [4-13]. Nevertheless, a few studies have measured passenger expectations of or satisfaction with ASQ dimensions. The ASQ measurement model based on passenger expectations will help airport managers and operators understand passenger needs, which plays a vital role in its application to improve passenger satisfaction directly $[6,10,13]$.

Most previous studies employed structural equation modeling (SEM), Bayesian networks (BN), or artificial neural networks (ANN) to investigate air transport customer loyalty, customer perception of airline service, airport service quality (ASQ), and passenger satisfaction [4-13]. To date, however, no study has applied an integrated SEM-BN-ANN approach to enhance the quality of the obtained models. Understanding passengers' changing needs and expectations is essential as airports resume normal operations. The reliability of the predictive-analytic model is necessary for the post-COVID-19 pandemic. It is essential to eliminate weaknesses of the separated model by using a hybrid SEM-BN-ANN model to fill in research gaps on improving airport services more effectively in the post-COVID-19 era. The research questions are as follows: what are the practical analysis tools to analyze ASQ dimensions that ultimately increase passenger satisfaction, and how well do they provide trustworthy information?

This study proposed a hybrid three-stage approach that combined structural equation modeling (SEM), Bayesian networks (BN), and artificial neural network (ANN). Figure 1 presents a model development flowchart illustrating the model's step, objective, and outcome. The SEM was constructed using an empirically validated measurement model by Chonsalasin et al. [10]. This study first employed SEM to test the research hypotheses and identified significant ASQ dimensions influencing passengers' overall satisfaction. Second, the significant dimensions obtained from the SEM were input to the BN, which was classified into three categories based on each state's opportunity of occurrence. The results from the BN determine the current level of overall passenger satisfaction. Subsequently, the ANN was conducted to identify the most critical service dimension to significantly improve overall passenger satisfaction. Findings from this research provide reliable ASQ dimensions corresponding to international benchmarks and standards. The results help to identify the most significant service dimensions that should be focused on to improve passenger satisfaction. Finally, insights into priority factors were discussed to recover passenger satisfaction, increase trustworthiness, and maintain the efficiency of the airport service not only over the COVID-19 outbreak period but also for long-term service.

The paper is organized as follows. A literature review is proposed in Section 2. Section 3 shows the problem hypothesis development, and Section 4 describes the research methodologies. The results are presented in Section 5. The discussion, implications, and limitations are addressed in Section 6. Finally, the conclusion is drawn in Section 7.

![img-0.jpeg](img-0.jpeg)

Figure 1. A model development flowchart.

# 2. Literature Review 

### 2.1. Airport Service Quality (ASQ)

Before the coronavirus pandemic, the aviation industry experienced intense competition among airports. The competition occurred in multiple dimensions in both aeronautical and non-aeronautical services. To compete with counterparts, it is better to understand the needs of passengers, airlines, and other stakeholders to improve service quality, the physical environment, and infrastructure. The Airports Council International (ACI) World's Airport Service Quality (ASQ) customer experience provides a 360-degree view of managing the passenger experience at airports and a unique suite of solutions. ACI assists nearly 400 airports worldwide in managing and offering the best customer experience possible based on its demonstrated competence in airports, marketing research, customer experience management, and delivery [14]. The ACI's ASQ program provides management data and research tools required to better understand passenger preferences and views on airport goods and services. Customer experience management is the planning and responding to customer experiences to meet or exceed the customer's expectations, hence increasing customer pleasure, loyalty, and revenue while decreasing service costs. This means that ASQ has been established as a benchmark that assesses air passenger satisfaction while traveling through an airport [15].

To meet international standards, the Airport of Thailand (AOT) has taken part in an ASQ evaluation project implemented by the Airports Council International (ACI) using the same global questionnaire [16]. However, conducting only the universal survey might not reflect the actual performance of each airport because the airport's customers have different perceptions of the airport operation [17], and the airport has different strong and weak points of the service. Therefore, identifying a measurement model of service quality for an individual airport might properly provide direct and effective improvement strategies [17-19].

The airport is a facility that involves several service stakeholders, including airlines, airport operators, immigration agents, and other service providers in the airport terminal area. The quality of airport services is being measured using a sustainable service process

approach, beginning with access to the airport (access), the check-in process at the airline counter (check-in), passport control by immigration officers (passport control) for international departures, security inspection process (security), find your way (wayfinding), airport facilities, airport environment, and arrival services. According to their individual perspectives, scholars use several dimensions to measure airport service quality. However, certain dimensions are utilized by the same scholars, and some even add extra dimensions outside the scope of the ASQ dimension provided ACI. According to systematic review of ASQ dimensions arranged by Usman et al. [20], several researchers employed eight dimensions, the three most commonly used being check-in, airport facilities, and security. The other dimensions are access, airport environment, wayfinding, arrival services, and passport control.

Regarding airport service quality, internal and external evaluations have been necessary for airport management. Yeh and Kuo [17] proposed a fuzzy multi-attribute evaluation model by obtaining information from international travel experts and investigating airport managers and other stakeholders. Fodness and Murray [6] argued that monitoring airport service performance without systematically comprehending passenger expectations may result in an unnecessary effort to improve unimportant service dimensions. This is consistent with a study by Lubbe et al. [12] that confirms the importance of air travelers' voices toward service quality evaluation. Scholars have employed different analysis methodologies to understand passenger needs in each airport service dimension. Bezerra and Gomes [4] applied exploratory factor analysis (EFA) to examine passengers' perceptions of the ASQ dimensions of the Brazilian airport. This study found seven significant service dimensions that affect the ASQ: price, convenience, ambiance, access, check-in, security, and airport facilities. In a subsequent study, the same authors used confirmatory factor analysis (CFA) to confirm that only six key dimensions, excluding price, impacted the overall ASQ [5]. Chonsalasin et al. [10] conducted CFA to develop a measurement model to study passengers' expectations toward Thai airports. The paper derived the measurement model from the research by Pandey [13]. It confirmed that seven dimensions obtained from Pandey [13] were significant: access, check-in, security, airport facilities, wayfinding, airport environment, and arrival services. Di Pietro et al. [21] used Bayesian networks to jointly analyze the perceived and provided quality of an airport check-in process, which can be utilized to create novel strategies for enhancing service quality. Farr et al. [22] used Bayesian networks to investigate human and environmental factors to facilitate effective airport wayfinding.

# 2.2. Airport Service Quality (ASQ) and Overall Satisfaction 

Due to its correlation with brand loyalty and purchase intent, customer satisfaction is essential for businesses [23]. Many studies in the aviation sector reveal the relationship between airport aeronautical and non-aeronautical performance and passengers' airport experiences [24]. Currently, it is evident that non-aviation revenue (NAR) generation is a substantial contributor to the aviation industry's overall economic growth. Graham [25] discovered that airport service quality is vital for travelers and has a significant influence on their journey.

According to ACI World's 2016 research, the greatest method for enhancing NAR is to focus on the customer experience. An increase of $1 \%$ in the number of passengers results in an increase of NAR of $0.7 \%$ to $1 \%$, as reported by the Airport Service Quality (ASQ) data study, while an increase of $1 \%$ in overall passenger satisfaction results in an increase of Nar of $1.5 \%$ on average [14]. The voices of customers have become more significant as airports have implemented business management strategies.

Numerous studies have been conducted on the relationship between airport service quality and passenger satisfaction. This research area examines the relationships between airport service quality and latent factors such as airport image, customer satisfaction, and airport loyalty [7,26]. Regarding the ASQ bibliometric analysis of Bakır et al. [27], the SEM methodology utilized by the researchers was the most frequently used method in

this research area, concentrating on the correlations between the variables. Multi-criteria decision making (MCDM) approaches, which enable optimal selection in problems with competing criteria, have been utilized in studies to prioritize and compare ASQ dimensions. Aside from the above relationship between ASQ and passenger satisfaction, Liao et al. [28] considered perceived airfare and flight offers. Then, they analyzed overall satisfaction, including alternative attractiveness and switching costs, to determine whether passengers are persuaded to reuse airports. The findings indicated a positive relationship between ASQ and passengers' likelihood of returning to airports. Table 1 summarizes ASQ dimensions of previous research.

To enhance the efficiency of the analysis, we propose a multi-stage analysis model consisting of SEM, BN, and ANN analyses to identify the significant ASQ dimensions resulting in overall satisfaction; (1) determine the current situation of passengers' satisfaction; and (2) investigate which dimension is the most important and should be improved to increase overall satisfaction.

# 3. Hypothesis Development 

Previous research has studied passenger expectations of airport service quality in Thailand using a measurement model to assess indicators for all constructs [10]. Figure 2 depicts the measurement model for assessing airport service quality, which identifies passengers' expectations via confirmatory factor analysis. This measurement model was adopted to conduct a hybrid SEM-BN-ANN. The indicators were scored on a 7-point Likert scale, with one representing strongly disagree and seven representing strongly agree. A high score indicates that each measuring item had a high level of agreement. Cronbach's alpha measures the reliability of constructs. The results demonstrated that Cronbach's alpha for all constructs is larger than 0.7 , showing that all constructs' measurement items are reliable and indicating the uni-dimensionality of the measuring scale [29]. Furthermore, the relationship of seven constructs along with the 33 observed variables shows that, at the 0.001 level of statistical significance, they have factor loadings in the positive direction. This suggests that they could all be regarded as indicators of airport service quality. Consequently, the seven significant dimensions of airport service are access, check-in, security, wayfinding, airport facilities, airport environment, and arrival services.

Access or mobility to the airport means convenience and a variety of transportation alternatives to transit to and from the airport for both arriving and departing passengers, as well as parking spaces, walkways, trolleys, and other systems that help passengers move conveniently. Check-in includes passenger waiting time regarding the check-in process, operational efficiency, and service employees' attitudes. The airport security system comprises security employees' attitudes, the security screening process, and the waiting time related to security inspections. Wayfinding is an airport signage system that includes general directions, flight information, maps, and guides to assist passengers in navigating terminals and showing walking distances. Airport facilities include features that accommodate passengers, such as Wi-Fi, lounges, banks or ATMs, currency exchange services, restaurants, shopping, and duty-free venues. The airport environment involves views and landscapes, the passenger terminal, waiting areas, the convenience and sufficiency of facilities, and the cleanliness of all areas. Airport arrival services consist of an immigration procedure, a customs inspection process, and baggage delivery speed.

Based on the results obtained from the measurement model and literature review of the seven dimensions of airport service quality, the hypotheses are formulated as follows:
H1. There is a significant positive relationship between access and overall satisfaction.
H2. There is a significant positive relationship between check-in and overall satisfaction.
H3. There is a significant positive relationship between security and overall satisfaction.
H4. There is a significant positive relationship between wayfinding and overall satisfaction.
H5. There is a significant positive relationship between the airport facilities and overall satisfaction.

H6. There is a significant positive relationship between the airport environment and overall satisfaction. H7. There is a significant positive relationship between arrival services and overall satisfaction. The above seven hypotheses were formulated to represent seven dimensions of the ASQ that impact passenger satisfaction using structural equation modeling (SEM).

Table 1. Summary of airport service quality (ASQ) dimensions in previous research.


![img-1.jpeg](img-1.jpeg)

Figure 2. Results of the measurement model.

# 4. Research Methodology 

### 4.1. Participants and Data Collection

A questionnaire survey was conducted from March to May 2019 at departure terminals of airports in northern, northeastern, central, and southern Thailand. This study's samples consisted of domestic passengers at the departure terminal of each airport in the four regions of Thailand (southern, northern, central, and northeastern), who were selected using stratified random sampling based on the area of the regions with airports in order to obtain data from distributed samples that adequately represent the population. For each region, 400 samples were collected in total. In addition, to obtain representative samples, this survey's respondents were limited to airline passengers willing to participate in interviews; the interviewer inquired whether they had utilized airline services, and if it was convenient for them to complete the questionnaire before presenting it. On average, 15 min were devoted to each interview. We gathered interviews with 1600 respondents. A total of 1,037 valid responses were obtained. Maximum likelihood (ML) was used to accomplish model fit of the measurement model so that model parameters and fit indices could be precisely calculated. The ML requires a sample size of at least 100 to obtain reliable results [37], whereas the general rule considers a sample size between 100 and 200 to be a "good sample size" [38]. Although there are no strict sample size guidelines for SEM, researchers recommend a minimum sample size of approximately 200 [39]. Therefore, the sample size of this research $(\mathrm{n}=1037)$ was sufficient for conducting SEM.

Table 2 provides a demographic profile of the respondents; $521(50 \%)$ were female, and $516(49.8 \%)$ were male. The preponderance of respondents was between 25 and 44 years old ( $55.0 \%$ were between the ages of 25 and 34 and $21.3 \%$ were between the ages of 35 and 44). In terms of the level of education, $61.2 \%$ of the population had a Bachelor's degree, while $23.0 \%$ did not. Most respondents were employed by private corporations ( $36.6 \%$ ), followed by government officials and employees of state-owned enterprises ( $34.5 \%$ ). Nearly half of the participants ( $48.5 \%$ ) said they flew at least once per year, $33.1 \%$ said twice or three times yearly, $11.7 \%$ said four to six times yearly, and $6.8 \%$ said at least seven times yearly. This reflects the Thai culture that most people fly back to their hometown every year during the New Year or Songkran Festival. Most respondents ( $47.3 \%$ ) said they were traveling for leisure, followed by $23.2 \%$ who said they were traveling for business.

Table 2. The demographic profile of the participants $(\mathrm{N}=1037)$.


# 4.2. Variable Measurement 

To reflect the quality of airport service from diverse angles, the proposed model consists of seven constructs adapted from previous studies and contains 33 indicators, as shown in Table 3 [10]. Thus, the 33 variables were administered in the questionnaire survey, which was categorized into the seven dimensions as follows: access, four variables; check-in, five variables; security, four variables; wayfinding, five variables; airport facilities, seven variables; airport environment, five variables; and arrival services, three variables. A seven-point Likert scale was applied for responding to each question, ranging from 1 (strongly disagree) to 7 (strongly agree). Therefore, a higher score represents a higher level of passenger satisfaction in each indicator.

### 4.3. Data Analysis

Many scholars have applied a hybrid model to solve solutions in different fields. A two-stage analysis of a structural equation model (SEM) and Bayesian networks (BN) was applied by Chanpariyavatevong et al. [40], which utilized a hybrid SEM-BN approach to investigate the influence of key factors on airline loyalty. Díez-Mesa et al. [41] integrated the use of BN and SEM in a two-step approach for analyzing service quality in light rail transit in Spain. Another type of hybrid model is an integration between SEM and the ANN, which was conducted by Leong et al. [42] and Sharma [43]. Leong et al. [42] applied two-stage predictive-analytic SEM-neural network models to predict customer satisfaction from service quality among low-cost and full-service airlines. Sharma [43] applied a hybrid SEM-ANN to investigate customer behavior toward mobile banking services. For a threestage approach, Raut et al. [44] propose a hybrid SEM-ANN- ISM approach for analyzing the factors that influence the adoption of cloud computing services in Indian companies. To our knowledge, no study has examined the impact of ASQ dimensions on passenger satisfaction using a hybrid SEM-BN-ANN approach.

The first stage of the proposed framework involves conducting structural equation modeling (SEM) to test the proposed hypothesis and examine the causal relationships between the constructs. The SEM in this research was conducted based on an empirically validated measurement model of airport service quality (ASQ) developed by Chonsalasin et al. [10]. The study showed that passengers' expectations of the ASQ consist of seven dimensions. Mplus version 7.2 was employed to perform and analyze confirmatory factor analysis using maximum likelihood estimation (MLE). Goodness-of-fit indices were used to measure validity and reliability.

Although SEM is an approach that proves a causal model of hypothesized relationships latent constructs, SEM cannot transfer insights obtained from a theoretical model to practical actions [45]. To strengthen the SEM analysis, Bayesian networks (BN) were employed based on the empirically validated structural model. This approach can support decision-making because the BN is a probabilistic model considering uncertainty [46]. BN can explain the overall state of service quality and the state of each dimension. However, individually applying BN is a limitation because the model's accuracy depends only on the experts' experience [47]. Therefore, integrating SEM and BN analysis can improve reliability and bring advantages to airport operations.

Identifying the ASQ's critical dimensions helps airport agencies identify the priority area for improvement. Conducting artificial neural networks (ANN) could point to the most crucial dimensions directly. Improvement in these critical dimensions helps increase overall satisfaction levels. ANN identifies non-compensatory and non-linear relationships between latent constructs and overall passenger satisfaction. Therefore, the ANN provides higher prediction accuracy than the traditional structural model [42,48]. This is because the SEM only examines the linear relationships that sometimes oversimplify the complex analysis that involves human decision-making processes [42].

This innovative research technique combines a theoretical construction based on an empirically validated structural model with the BN of a graphical interaction. Using SEM, the hypothesized relationships between the constructs were tested. Consequently, the

BN, which was constructed based on the causal relationships of the structural model, was utilized as a decision-support model. Finally, the ANN was developed to identify noncompensatory and non-linear relationships between the most important ASQ dimensions and passenger satisfaction.

Table 3. Parameter estimation of the measurement model and descriptive statistics.


Note: ${ }^{ }$ significant at $\alpha=0.001, \bar{X}=$ Mean, $\mathrm{SD}=$ Standard deviation.

# 5. Results

### 5.1. Structural Equation Modeling

The hypotheses of the seven ASQ dimensions toward overall satisfaction were tested to determine goodness of fit indices. To be an acceptable model, the ratio between the chi-square and the number of degrees of freedom $\left(\chi^{2} / d f\right)<3$ [39], root mean square error of approximation (RMSEA) $<0.07$ [49], comparative fit index (CFI) $>0.95$, Tucker-Lewis coefficient (TLI) $>0.95$, and standardized root mean square residual (SRMR) $<0.08$ [50]. The structural model of airport service quality was accurate and reliable, presenting an

acceptable model fit, as shown in Figure 3. The results were as follows: $\chi^{2}=1326.369$, $d f=467, \chi^{2} / d f=2.840$, RMSEA $=0.042, \mathrm{CFI}=0.976, \mathrm{TLI}=0.971, \mathrm{SRMR}=0.023$.
![img-2.jpeg](img-2.jpeg)

Figure 3. Results of the structural model.
The SEM results of the seven constructs toward overall satisfaction with airport service quality are shown in Table 4. With a $p$-value $<0.05$, five out of seven airport service quality


dimensions were discovered to be predictive of passengers' overall satisfaction. Security, wayfinding, airport facilities, airport environment, and arrival services were statistically significant and contributed to predicting the variance of overall satisfaction, supporting H3, H4, H5, H6, and H7. Access and check-in were found not to be significant in the structural model, rejecting H1 and H2.

Table 4. The results of structural model.

Note: ${ }^{*} p<0.05,{ }^{* *} p<0.001$.

# 5.2. Bayesian Networks 

Bayesian networks are probabilistic graphical models used for reasoning under uncertainty. Regarding the results from the SEM, we found that there were five significant ASQ dimensions that impact passenger satisfaction, including security, wayfinding, airport facilities, airport environment, and arrival services. Although the SEM results showed the regression weight, they did not explain the results numerically. At this stage, we employed the BN to refine the relationship between the significant dimensions and passenger satisfaction. The BN result can be used to determine the current level of overall passenger satisfaction.

Figure 4 depicts the BN of ASQ determinants, consisting of six nodes and five edges between nodes. Five nodes are parent nodes representing the five significant ASQ dimensions, and the child node is the passenger satisfaction. Each node has a different probability, which is a percentage of high, medium, and low states. The BN is used to explain the effect of ASQ dimensions on overall satisfaction with airport services. The results of the BN presented the current situation of overall satisfaction that $60.3 \%$ was at a high state, while $31.5 \%$ and $8.22 \%$ were satisfied at medium and low states, respectively. The mean value of overall satisfaction was 5.66, and its standard deviation was 1.4. Although most passengers reported high satisfaction levels, passenger satisfaction still has room for improvement. In the final step, ANN was utilized to evaluate which ASQ dimensions have a greater impact on overall satisfaction.
![img-3.jpeg](img-3.jpeg)

Figure 4. Results of the Bayesian network for airport service quality.

# 5.3. Artificial Neural Network 

After developing the BN, the ANN was utilized to determine which ASQ dimensions greatly influence overall satisfaction. Because SEM can only investigate linear relationships, it may occasionally oversimplify the complicated nature of human decision-making processes. To effectively address this problem, ANN is used to identify non-compensatory and non-linear relationships in the empirical framework, as it can learn complicated linear and non-linear relationships between ASQ dimensions and passenger satisfaction. The statistically significant predictors were fed into the ANN as input variables. There are five nodes in the input layers, represented by significant predictors, namely, security (SC), wayfinding (WF), airport facilities (AF), airport environment (AE), and arrival services (AS), as shown in Figure 5. The network model's output layer was presented by the dependent variable, overall satisfaction (OSQ_Level).

Synaptic Weight $>$
![img-4.jpeg](img-4.jpeg)

Figure 5. Neural network model.
To train the model, the multilayer perceptron training algorithm was used. Eighty percent of the samples were used to train the model, while twenty percent were used to validate it. After developing the ANN, the accuracy of the model was evaluated. As a classification test for this investigation, a classification matrix was utilized to evaluate the performance of the ANN. The classification matrix was constructed with columns representing the predicted values from the ANN and rows representing the observed values from the overall level of satisfaction. The confusion matrix utilizes a crossing table operation to tally the predicted and observed values to calculate a percent correct. The percent correct classifications measure the predictive abilities of the ANN during both the training and testing phases. Table 5 displays the results of the classification matrix used to test the robustness of the ANN. According to the findings of the classification matrix,

Table 5. Classification matrix for the robustness test.


Dependent Variable: OSQ_Level.
The sensitivity analysis was computed using the average predictive importance of variables. Each variable's normalized importance can be determined by dividing its importance by its highest importance value. Table 6 provides a summary of the variables' relative importance. The results obtained from the ANN model show that airport facilities are the key variable to improve the overall satisfaction of the ASQ dimensions, followed by wayfinding, security, airport environment, and arrival services. The percentage of normalized importance for the three most important dimensions was as follows: airport facilities ( $100 \%$ ), wayfinding ( $90.3 \%$ ), and security ( $88.1 \%$ ). The results obtained from each step of the three-stage analysis model are summarized in Table 7.

Table 6. Predictor importance.


Table 7. Summary of results.


# 6. Discussion 

### 6.1. Theoretical Implications

This study has advanced the literature on the impact of airport service quality (ASQ) on passenger satisfaction at airports from a theoretical standpoint. The study is one of the first to use a multi-stage model with an SEM-BN-ANN approach to evaluate passenger satisfaction. Furthermore, the model is one of the first to identify the ASQ's significant dimensions, identify quality drivers that lead to overall satisfaction, investigate which dimension is the most important and should be improved to increase overall satisfaction, and confirm the model's prediction accuracy. According to the multi-stage analysis model, airport facilities are the most critical dimension and directly affect passengers' overall satisfaction with the ASQ, followed by wayfinding and security. Consequently, the conceptual model developed in this study can be utilized as a guideline for other researchers interested in analyzing air passenger satisfaction concerning the ASQ. This research was conducted in Thailand, expanding the body of knowledge about air transportation in Southeast Asia, a popular vacation destination for people worldwide. As a result, the empirical findings can be applied as a benchmark for other studies in countries with similar airport development patterns.

### 6.2. Practical Implications

Five factors impact passenger satisfaction: security, wayfinding, airport facilities, airport environment, and arrival services. However, only three dimensions are critical factors: airport facilities, wayfinding, and security. These critical factors need special attention as significant priorities for long-term airport operation, especially during the COVID-19 pandemic and in the uncertain future. In the last three years, COVID-19 has had an immediate and dramatic impact on the financial position of airports worldwide, with a dramatic fall in passenger numbers, revenue, and profitability. Air transportation has undeniably been a part of transferring the novel coronavirus from countries to other countries. This is an enormous challenge for airport management to address a financial crisis due to the pandemic. Social distancing, hygiene, cleanliness, a touchless system, and other airport regulations have been implemented.

Moreover, passenger expectations and perceptions of airport service quality (ASQ) may change according to the pandemic. The study recommends practical strategies to guide decision-makers. Throughout the COVID-19 pandemic, airports should highlight three dimensions of service quality. The results of SEM-BN-ANN analysis revealed that airport facilities significantly directly impact passenger satisfaction, which is the most critical dimension to improve the ASQ level in Thailand. Undeniably, features that accommodate passengers are options for them whether they travel from, to, or transit to the airports. This result is consistent with previous studies showing that airport facilities significantly affect passenger expectations and perceptions in Thailand see [10,13] and in other countries (see $[2,4-9,51]$ ).

Based on the questionnaire, airport facilities consist of seven indicators, including sufficiency and quality of restaurants/shops inside the airport, value for money of restaurant/eating facilities, availability of ATMs/banks/money changers, shopping facilities, value for money of shopping facilities, availability of Internet service (Wi-Fi), and availability of business/executive lounges. This means that these seven indicators attract passengers to the airports and meet the requirements of the passengers. If airports improve these facilities beyond customer expectations, this may significantly increase overall satisfaction. During COVID-19 and the new normality, the touchless system for any payment or related activity may improve service quality and cleanliness. Additionally, service robots may reduce contact with humans, which can be used in restaurants, shops, and lounges in the airport [52]. Regarding the Sustainable Development Report of the Airport of Thailand (AOT) [53], "Touchless Airport" has been implemented. Common Use Self Service (CUSS) kiosks and Common Use Bag Drop (CUBD) technologies have been used to reduce touched points in airports. Encourage early reservations for accommodation and restaurants to avoid crowding, as well as the usage of digital payment.

Wayfinding was found to have a significant direct impact on passenger satisfaction, and it is the second most important dimension to improve ASQ level in Thai airports. It included five statistically significant indicators: ease of finding directions at the airport, flight information screen, walking distance in the passenger terminal, ease of connecting to other flights, and courtesy and helpfulness of airport staff. Undeniably, the complex direction and long walking distance in the airport makes travelers headache and tired, which may also impact passenger satisfaction. During COVID-19 and new normality, however, driverless shuttle mobility in the airport can eliminate this problem. A service robot is another option for directing passengers. This is consistent with the study by MeiduteKavaliauskiene et al. [52], which confirmed that passengers had a positive perception of using robots instead of employing staff in the airport. The study used SEM analysis to investigate perceived trust in robots in airport services. COVID-19 fear influences perceived trust in robots and the intention to use them positively, while perceived trust influences the intention to utilize robots positively. For Thai airports, AOT arranged an Innovative Creativity Contest via the virtual reality platform, and one of the reward projects was "Way Finding Signage-Suvarnabhumi Airport" proposed by Bangkok Airways. Furthermore, a feature called "Home to Gate" has been added to SAWASDEE by the AOT application. This alert and route advice system from home to the boarding gate ensures that passengers arrive at the departure gate on time [53].

Security is the third most important ASQ dimension for improving passenger satisfaction. This is consistent with Bezerra and Gomes [4], Bezerra and Gomes [5], Chonsalasin et al. [10], Correia et al. [54], Gkritza et al. [55], Isa et al. [7], Jiang and Zhang [8], Lee and Yu [2], Liou et al. [11], Pandey [13], and Pantouvakis and Renzi [9].

Four indicators were measured in the security dimension: courtesy and helpfulness of security staff, the effectiveness of security inspection, waiting time for a safety inspection, and feeling of being safe and secure. Safety and security play an important role in the airport. In particular, human security is necessary even in the COVID-19 situation and the future. Being safe and secure in the present context is not only for crime prevention but also for the opportunity to spread the novel virus. The feeling of being safe and secure can be improved by applying signage for distancing. Using temperature sensors or CCTVs with temperature detectors can help passengers feel safe from COVID-19. According to the AOT operation [53], airport safety and security are among the top factors that concern all stakeholders, particularly during the COVID-19 pandemic. AOT has reassured stakeholders that airports are safe under the strict security measures that AOT has implemented. The pandemic prevention measures announced by the Ministry of Public Health have been strictly adopted, such as body temperature monitoring before entering the airport, passenger screening at airport entrances and exits, face mask use at all times, and social distancing measurements. Apart from consistently applying the Aerodrome Safety Policy, ICAO's Safety Management System (SMS), Airport Security Program (ASP), and Airport Contingency Plan (ACP), AOT has developed information technology systems on airport safety (e-Safety) and airport security (e-Security). Aside from physical security, AOT has steadily integrated technology into its operations and passenger services. Thus, information security and privacy are becoming increasingly crucial.

# 6.3. Limitations 

This study was based at least partially on the COVID-19 pandemic. No indicator measured or involved COVID-19 prevention because the data had been collected before the pandemic. The pandemic appears to be extending into the future. Empirical studies on elements associated with COVID-19 prevention, such as self-service technology (self-checkin kiosks), touchless systems (automated gates with sensors and other airport equipment), and service robots (robots that direct paths in airports), should be considered [56]. Service robots took the roles of airport operators in some tasks during the pandemic and may also be in the future [52]. As a result, future studies should incorporate these qualities into a causal model to better understand the underlying mechanism of increasing passenger satisfaction.

Another limitation is that this study was conducted in Thailand, with only Thai passengers. The findings may not be applicable to other parts of the world. Future research could address this limitation by conducting a cross-country comparison study with a more diverse pool of respondents from various countries, revealing more about the cultural influence on passenger satisfaction.

# 7. Conclusions 

The aviation industry has been disrupted due to the COVID-19 outbreak for over two years. Airport agencies must adapt, review, and improve existing practices, formulate new policies and regulations to face the current situation, and move forward to the new normal situation.

A hybrid SEM-BN-ANN approach is proposed that integrates a structural model, Bayesian networks, and a neural network model, as presented in Table 7. The structural model indicated that airport facilities are the best ASQ dimensions for predicting the variance of overall satisfaction, and four additional ASQ dimensions that were statistically significant are security, wayfinding, airport environment, and arrival services. Two ASQ dimensions, access and check-in, were not significant factors. Subsequently, the Bayesian network (BN) was employed to determine the current passenger satisfaction. The mean value of overall satisfaction was 5.66. This value demonstrates that there is much opportunity for improvement to increase overall satisfaction.

Finally, artificial neural network (ANN) analysis was used to prioritize which airport service quality dimension should be implemented and which significantly impacts overall passenger satisfaction. The order of the three most important ASQ dimensions with the percentage of normalized importance was as follows: airport facilities, wayfinding, and security. Thus, airport managers have a guide for determining the most effective strategies for enhancing passenger satisfaction. Improving airport facilities should be a top priority. Additionally, wayfinding and security require special attention. This integrative approach can also assist airport authorities in developing and implementing more effective engagement strategies, which could be used to increase passenger satisfaction and promote the sustainable growth of Thai airports, according to the AOT sustainable development agendas [53]. Due to the COVID-19 outbreak, we also suggest airport operations strategies to address the COVID-19 pandemic and in the post-COVID-19 era. The findings confirmed that a hybrid SEM-BN-ANN provides high accuracy and reliable information for Thai airports and specifies the priority of each service dimension, which leads to effective improvement of the overall service quality.

Assessing ASQ effectively is crucial for airport management. Learning from the "voice of the customer" enables airport authorities to understand and meet passengers' needs and expectations. A data-driven crowdsourcing approach can be employed in future studies to obtain insights from passengers. Online reviews, also known as user-generated content (UGC), can be acquired from credible internet sources using sentiment analysis to represent what ASQ subjects matter to passengers in both the pre-and post-COVID periods.

Author Contributions: Conceptualization, T.P. and W.W.; Methodology, W.W.; Software, T.P., W.W., S.R. and J.S.; Validation, W.W.; Formal analysis, W.W.; Investigation, W.W. and P.T.; Resources, W.W.; Data curation, T.P.; Writing-original draft, T.P.; Writing-review \& editing, W.W.; Visualization, T.P.; Supervision, W.W., J.S. and V.R.; Funding acquisition, W.W. All authors have read and agreed to the published version of the manuscript.
Funding: The research was granted by Thammasat University Research Fund, Contract No. TUFT 18/2566.
Institutional Review Board Statement: The study was conducted in accordance with the Declaration of Helsinki, and approved by the Ethics Committee of Suranaree University of Technology (protocol code: EC-62-48 and date of approval: 7 May 2019).
Informed Consent Statement: Informed consent was obtained from all subjects involved in the study.
Data Availability Statement: The data presented in this study are available on request from the corresponding author.

Acknowledgments: This study was supported by Thammasat University Research Fund, Contract No. TUFT 18/2566.

Conflicts of Interest: The authors declare no conflict of interest.

# Abbreviations 

