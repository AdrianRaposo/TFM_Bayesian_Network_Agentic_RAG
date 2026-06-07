# Article 

## Innovation Performance Prediction of University Student Teams Based on Bayesian Networks

Xueliang Zhang ${ }^{1}$, Jiawei Liu ${ }^{2}$, Chi Zhang ${ }^{1}$, Dongyan Shao ${ }^{3}$ and Zhiqiang Cai ${ }^{1, * *}$


#### Abstract

check for updates Citation: Zhang, X.; Liu, J.; Zhang, C.; Shao, D.; Cai, Z. Innovation Performance Prediction of University Student Teams Based on Bayesian Networks. Sustainability 2023, 15, 2335. https://doi.org/10.3390/ su15032335

Academic Editors: Marta Sainz Gómez, Rosario Bermejo García and María José Ruiz-Melero

Received: 14 November 2022
Revised: 21 January 2023
Accepted: 21 January 2023
Published: 27 January 2023


#### Abstract

Copyright: (C) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /)$.


1 Department of Industrial Engineering, Northwestern Polytechnical University, Xi'an 710072, China
2 School of Public Policy and Administration, Northwestern Polytechnical University, Xi'an 710072, China
3 School of Life Sciences, Northwestern Polytechnical University, Xi'an 710072, China

* Correspondence: caizhiqiang@nwpu.edu.cn


#### Abstract

Many studies have been conducted on the impact of dualistic learning, knowledge sharing, member heterogeneity, and their influencing factors on team performance in enterprises. However, research on the substantial differences between university student teams and enterprise teams is scarce. To address this void, this empirical study explores how the mechanism of dualistic learning affects university student teams' learning performance facing rapid changes in higher education. Using the questionnaire, two modules of dualistic learning were identified through reliability and validity tests, and the research data set was formed. After preprocessing the data set, two team innovation performance prediction models were established based on the Bayesian network (BN). According to the characteristics of BN, the probability reasoning of the model was calculated and the posterior probability table was obtained under different dualistic learning levels. The results show that dualistic learning has significant impacts on innovation performance, and the improvement of dualistic learning can stimulate team innovation performance. This research can provide important theoretical guidance for teams to improve their ability, gain competitive advantages, and stimulate the creative enthusiasm of college students. Hopefully, this research will enrich the existing theoretical connotation to a certain extent and promote the development of relevant empirical research.


Keywords: Bayesian network; dualistic learning; team innovation performance; prediction model

## 1. Introduction

Innovation is the most important driving engine for development and is the strategic support for building a modern economic system. University students have the desire for interdisciplinary cooperation and the autonomy to choose courses and research fields that provide convenience for their innovative behavior. Moreover, as the inheritors of knowledge and the builders of the future society, university students play an important role in the development of innovation. In general, their innovative behavior has been paid more and more attention to by society and researchers. Team innovation performance has become a key indicator to measure the team's technological innovation ability and overall performance. Therefore, research on the prediction of team innovation performance of university students can provide an effective method for the team to improve its ability and gain competitive advantages, so as to stimulate university students' creativity and enthusiasm.

We found that in addition to the research on the factors that affect the innovation performance of enterprise employees in organizations [1], at the educational level some scholars have conducted indepth research on the relationship between creativity and intelligence in middle school students [2] and used regression analysis to verify that scientific creative capabilities can accurately predict academic performance [3]. However, the existing literature lacks research on the relationships between dualistic learning, knowledge sharing, and innovation performance of university student teams from the perspective of organizational learning and knowledge management. Meanwhile, research on predicting innovation performance using Bayesian models is relatively scarce.

Hence, we planned to use the Bayesian network (BN) model to establish two performance prediction models, which compared the impacts of different levels of dualistic learning on university student teams' learning performance. Firstly, 228 questionnaires were designed and collected. Secondly, the prediction model was established through the steps of reliability and validity tests and confirmatory factor analysis. Finally, the importance degree of each influencing factor was calculated and each research variable was ranked according to the experimental results. Generally, it was of great significance to explore the relationship between the main factors affecting university students' team learning and accurately predict the innovation performance of university student teams by the BN model. On the one hand, the research results can theoretically uncover how the mechanism of university student teams' dualistic learning affects their learning performance and reveal a predictive method of team innovation performance. On the other hand, in practical terms, the results can provide management enlightenment for improving the innovation performance of university student teams.

# 2. Literature Review 

Dualistic learning is divided into exploration learning and exploitation learning, in which exploration learning, characterized by "pursuing and acquiring knowledge in new fields, is manifested in the initiative of the organization to create new knowledge, explore new technologies and strategies, and abilities to find new opportunities and new rules." Exploitation learning is characterized by "learning and using existing knowledge" [4]; that is, in a mature or new environment, existing knowledge is fully exploited to better apply it to practice, and the original knowledge can be improved and adjusted according to actual needs, so as to improve the implementation efficiency and performance of the established scheme in the specific environment. As for the relationship between dualistic learning and team performance, Katila and Ahuja [1] found that the combination of the two learning methods can enhance the viability of the organization, improve the financial performance of the enterprise, and enhance the ability of organizational learning and innovation. Colbert [5] believes that the competitive advantage generated by the interaction of two learning methods is better than the competitive advantage obtained by carrying out one learning method alone. Some scholars have also analyzed the characteristics of complex network structures and believed that a dualistic balanced network structure can better promote organizational performance [6]. However, the impact of dualistic capability on organizational performance is flexible [7] and the change in network situation may significantly affect organizational performance. Dualistic learning plays a more important role in improving the performance of enterprise alliances with higher network centrality. It can also help enterprise alliances with fewer structural holes achieve better performance. Although the relationship between dualistic learning and team performance has been widely studied, it is mainly concentrated in the industrial and business sectors. At present, scholars have empirically studied the impacts of dualistic learning, knowledge sharing, member heterogeneity, and their influencing factors on team performance in an enterprise [8-10]. The results from these researchers have an important guiding significance for human resource management practices and innovation management practices in the enterprise field. However, there are substantial differences between university student teams and enterprise teams. There are also substantial differences in learning objects and innovation pursuits. This study focuses on the theoretical issue of "the mechanism of dualistic learning impacts on university student team learning performance" to explore the impacts of dualistic learning on innovation performance in university student teams. Hopefully, this research will enrich the existing theoretical connotation to a certain extent and promote the development of relevant theoretical research.

With the rapid development of computers and chips, the limits of computing power are constantly broken through, and a large number of artificial intelligence (AI) methods, including Bayesian methods, support vector machine (SVM), integrated learning, and deep learning, are emerging and being gradually applied to data mining and predictive

modeling [11,12,13,14,15]. Compared with the traditional generalized linear model, the Bayesian network has fewer restrictions on modeling variables and is more robust in the nonlinear relationship between variables. It can better fit the data distribution and give more accurate prediction results. At present, the Bayesian network (BN) is widely used in industrial applications, financial analysis, and military applications. Sun et al. [16] proposed an evolutionary algorithm based on BN to optimize the task allocation strategy, which to some extent solved the response delay when the industrial internet of things is used to monitor industrial plants. Bashar et al. [17] proposed three new network management solutions based on BN, which to some extent meet the requirements of automation and efficient management of telecommunications networks. Mahadevan et al. [18] put forward a structural reliability evaluation method combining BN, and also considered the multiple failure sequence characteristics of large structures and the correlation between element limit states. The effectiveness of this evaluation method was verified by comparison with the traditional series parallel reliability method. In order to control the quality risk of cold storage construction projects, Song et al. [19] constructed a BN-based cold storage construction quality risk assessment model and obtained key quality risk factors through reverse reasoning analysis and sensitivity analysis. Johnson et al. [20] created a math app to provide students in the Emirates in grade six with the opportunity to explore mathematics and then used BN to examine the educational implications and explore the impacts of different factors on their enthusiasm for learning mathematics.

To summarise, most researchers rarely use AI methods to explore the factors that affect university student teams' innovation performance and predict their innovation performance. To achieve this aim, first of all, our study conducted a questionnaire survey on university students' innovation teams to measure research variables such as dualistic learning, knowledge sharing, and task interdependence. We also verified the measurement model and data fitting of this study with confirmatory factor analysis in the next step. Then, we used the questionnaire (a five-point Likert scale) to quantify all variables and made the scale transform into the innovation performance dataset. Next, based on the dataset, we established two BN prediction models of university student team performance using a tree-enhanced Bayesian algorithm. After that, we calculated the accuracy of these models. Finally, we quantitatively analysed the importance degree of each influencing factor and ranked each research variable according to the experimental results. The theoretical solution could be viewed in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Theoretical Solution.

# 3. Methods 

### 3.1. Questionnaire

This study uses the mature scale developed by domestic and foreign scholars to ensure the validity and reliability of the questionnaire. Through literature collection and reading, we found a mature scale for dualistic learning, knowledge sharing, team innovation performance, and task interdependence of university student teams. Among them, the ambidexterity learning scale [21] includes two dimensions of exploitative learning and exploratory learning, both of which were developed by Atuahene-Gema and Murray. Each dimension includes three measurement items. The knowledge-sharing behavior scale [22] was developed by Collins and translated by Tian Lifa, including four dimensions. The team task performance scale adopted the scale [23] developed by Chen Wei and others, which has four dimensions. The task interdependence scale [24] was developed by Liden, Wayne, and Broadway, and was translated by Liu Jun, with a total of three items.

To meet the needs of this study, we made corresponding modifications and improvements and formed the first draft of this research questionnaire. Then, based on the first draft of the questionnaire, we consulted with professionals on the rationality, logical relationship, wording, and grammar of each item. In order to avoid the fact that the respondents cannot answer the questionnaire due to the academic, professional, and obscure wording, we piloted on several college students in the university's innovation team. According to their opinions, we modified and improved the relevant questions.

The five-point Likert scale was used to measure the relevant items of the research variables such as dualistic learning, knowledge sharing, and task interdependence of university student teams. Then we analyzed the reliability and validity of the predictive test data of the questionnaire and deleted the items according to the analysis results to form a formal questionnaire. The finalized questionnaire (see Appendix A) contained 11 basic personal information, 4 measurement scale dimensions, and 23 specific questions.

### 3.2. Confirmatory Factor Analysis

In this study, we used confirmatory factor analysis (CFA) to verify the convergent validity and discriminant validity of the scale for research variables, including dualistic learning, task interdependence, knowledge sharing, and learning performance. Convergent validity refers to the similarity degree of the same abstract concept or trait measured by different measurement methods. It is usually judged by the standardized factor loadings of each item and the composite reliability. If the value of the standardized factor loading of each item is greater than 0.5 and the value of composite reliability is greater than 0.6 , it indicates that the scale has good convergent validity.

Discriminant validity refers to the degree to which a construct is truly different from other constructs according to empirical criteria. In an experiment, if it can be proved statistically that the indicators which are not related to the preset construct are indeed not related to the construct, then the experiment has discriminant validity. In this study, the structural equation model was used to obtain the CFA results of variables. Kline believes that multiple fitting indicators should be used to verify the fitting degree of research samples and theoretical models, and indicators such as $x^{2} / d f$, GFI, AGFI, and RMSEA can be used to evaluate the fitting degree of structural equation models [25].

### 3.3. Bayesian Network (BN)

The BN originated from Bayesian statistical analysis theory, which is a classical machine learning method. BN uses a directed acyclic graph to succinctly represent the joint probability distribution on a group of random variables. The graph is annotated with the conditional probability table of any instantiated node probability distribution for a given parent node [26]. As an effective tool that combines probability theory and graph theory to deal with uncertainty reasoning and data analysis, BN can not only reveal the causal relationship of the problem through the graph structure but also analyze the uncertainty

of the problem according to the principles of probability theory, thus greatly reducing the complexity of reasoning calculation.

The Tree Augmented naïve Bayes network model (TAN), which considers the relationship between variables, is an extension of the NB classifier. It retains the complexity and robustness needed to facilitate the mining of associations between variables, thus improving the accuracy of the model [27]. An example of a TAN model is shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Tree Augmented Naive Bayes network model.
In this model, C represents the target variable and $A_{1}, A_{2}, \cdots, A_{n}$ represents the attribute variable. The joint probability distribution of the TAN classifier can be expressed as Equation (1)

$$
P\left(C, A_{1}, A_{2}, \cdots A_{n}\right)=P(C) \prod_{i=1}^{n} P\left(A_{i} \mid p a\left(A_{i}\right)\right)
$$

A posteriori probability refers to the probability that is more realistic after obtaining new additional information through the Bayesian formula and investigation, then modifying the prior probability. The Bayesian formula can be expressed as Equation (2)

$$
P\left(M_{i} \mid N\right)=\frac{P\left(M_{i}\right) P\left(N \mid M_{i}\right)}{\sum_{i=1}^{n} P\left(M_{i}\right) P\left(N \mid M_{i}\right)}
$$

In the formula, $P\left(M_{i}\right)$ is the prior probability obtained through data statistics. This formula is to explore the probability of each event that causes N to occur when it is observed that event N has occurred. A posteriori probability is mainly used for predictive inference to predict the probability of occurrence of a certain result node in the network through the information of the network node, and diagnostic inference-to infer the probability of occurrence of the network condition node through the information of the result node.

# 3.4. Confusion Matrix and ROC Curve 

To ensure the high accuracy of the prediction model, the accuracy of the BN model must be evaluated.

The confusion matrix is a basic method to evaluate the reliability of predictive classification models. The column represents the actual situation, while the row represents the prediction result of the classifier. The possible results produced by the classifier are true positive (TP), false positive (FP), false negative (FN), and true negative (TN).

The model accuracy is determined by the following, Equation (3).

$$
\text { Accuracy }=\frac{T P+T N}{T P+F P+T N+F N}
$$

At the same time, the Bayesian classifier classifies the samples into zero or one, according to the classification threshold. Moreover, in these classifiers, different thresholds determine different classification results and classifier evaluation indexes. Considering the above situation, we used the ROC curve and the area under the curve (AUC) to measure the model performance. The ROC curve is called the receiver operating characteristic curve,

which is commonly used to measure the overall reliability of the classification model. It takes multiple pairs of FPR rates and TPRs as the horizontal axis and vertical axis and obtains the ROC curve by connecting each intersection point. The larger the area under the curve, the higher the accuracy of the model, and the better the classification effect [28]. AUC is the calculated value of the area under the ROC curve, and the value range of AUC is between 0.5 and 1 . The greater the AUC value, the better the effect of the machine learning classifier. This method is very convenient and accurate for evaluating the performance of a prediction model.

# 3.5. Importance Measure 

Importance refers to the degree to which the state change of single or multiple components in the system affects the reliability of the system [29]. It is used to evaluate the relative importance of various factors. Birnbaum first put forward the importance analysis theory in 1969, which is also called probability importance [30].

The classic Birnbaum importance depends on the structure of the system model and has no relationship with the probability of current basic events.

At moment t , the Birnbaum importance of the i unit is defined as Equation (4)

$$
I^{B}(i \mid \mathrm{t})=\frac{\partial h(t)}{\partial p_{i}(t)}, i=1,2, \cdots, n
$$

Birnbaum importance is obtained from the partial derivative of system reliability to unit reliability $\mathrm{P}_{\mathrm{i}}(\mathrm{t})$. This is the traditional sensitivity analysis method.

For the whole system unit, the importance of Birnbaum can also be expressed as Equation (5)

$$
I^{B}(i \mid \mathrm{t})=R\left(1_{i}, p\right)-R\left(0_{i}, p\right)
$$

where $R\left(1_{i}, p\right) A A$ represents the probability of the top event when the bottom event i must occur, and $R\left(0_{i}, p\right)$ represents the probability of the top event when the bottom event i must not occur.

## 4. Results and Discussions

### 4.1. Reliability and Validity Test of the Questionnaire

The reliability of the scale is tested by Cronbach's $\alpha$ value and the CR value of the scale. The calculation shows that the Cronbach's $\alpha$ of all latent variables in this study was greater than 0.7 , and the CR value of the composite reliability was greater than 0.6 , indicating that the scale has a high level of internal consistency reliability. The scale used in this paper is formed by referring to existing literature, expert interviews, and preresearch, which can ensure its content validity. Table 1 shows that the standardized factor loading value of each item was greater than 0.5 , and the AVE value of each latent variable was greater than 0.5 , indicating that the scale had good convergent validity.

Table 1. Reliability and validity test results of the scale.


Table 1. Cont.


Finally, the null model, single-factor model, six-factor model, and seven-factor model were compared by confirmatory factor analysis to test the discriminant validity of all variables. Table 2 shows that the seven-factor model fits well $\left(x^{2}=320.868, p<0.001\right.$; $x^{2} / d f=1.535$; RMSEA $=0.049 ; \mathrm{GFI}=0.897 ; \mathrm{AGFI}=0.864 ; \mathrm{TLI}=0.936 ; \mathrm{CFI}=0.947$ ) and was significantly better than the fitness of other models, so all variables have good discriminant validity.

Table 2. Results of discriminant validity analysis.


Note: a In the null model, there was no relationship between all measured items. b Combining exploration learning and exploitation learning into a potential factor. c Combining exploitation learning and sharing willingness into a potential factor. d Combining sharing willingness and sharing behavior into a potential factor. e Combining sharing behavior and task interdependence into a potential factor. f Combining task interdependence and task performance into a potential factor. g Combining task performance and cooperation performance into a potential factor. h Integrate all items into a potential factor.

Based on the experimental results, we divided the question module in the scale into five predictive variables, namely, exploration learning, exploitation learning, sharing willingness, sharing behavior, task interdependence, and a predictive goal, learning performance.

# 4.2. Establishment of University Student Team Innovation Performance Data Set 

This study collected 280 sample data about the team learning of university students. By sample integrity verification and rationality evaluation, we finally screened 228 sample data to establish the BN prediction model. Among the respondents, 121 teams ( $53.1 \%$ ) come from world-class universities, 24 teams ( $10.5 \%$ ) come from world-class disciplines, and 83 teams ( $36.4 \%$ ) come from other universities. Some cases of the data set are shown in Figure 3.

![img-2.jpeg](img-2.jpeg)

Figure 3. University students' team innovation performance dataset.
After a single factor analysis of the basic conditions of 228 selected samples, we selected some basic information that has an impact on team learning performance into the model, including 121 ( $53.07 \%$ ) from world-class universities, 83 ( $36.40 \%$ ) world-class discipline universities, and 24 ( $10.53 \%$ ) from other universities; The team's final results were 15 research papers ( $6.58 \%$ ), 114 application software or equipment developments ( $50.00 \%$ ), and 99 business plans ( $43.42 \%$ ); 90 ( $39.47 \%$ ) of the core team members were sophomores and below, 76 ( $33.33 \%$ ) were juniors, and 62 ( $27.19 \%$ ) were juniors and above; 80 ( $35.09 \%$ ) respondents participated in the innovation team once, 75 ( $32.89 \%$ ) respondents participated twice, and 73 ( $32.05 \%$ ) respondents participated three or more times. In addition, after sorting out the questionnaire information through the equal frequency division, we received the following prior probability information of the dualistic learning part and the learning performance part. In the two-level classification model, the prior probability of learning performance was not higher than 27 points is $62.72 \%$ (143/228), and the prior probability of learning performance higher than 27 points is $37.28 \%(85 / 228)$. In another prediction model, the prior probabilities of learning performance were lower than 25 points, 25-27 points, 27-29 years, and higher than 29 points are $28.51 \%(65 / 228)$, $34.21 \%(78 / 228), 15.79 \%(36 / 228)$, and $21.49 \%(49 / 228)$, respectively. Later, based on the prior probability and the change of dualistic learning proportion distribution, the posterior probability distribution of the model is discussed.

# 4.3. TAN Model for Learning Performance Prediction 

Based on the university student team database, we established two TAN models for experiments. Primarily based on the equal frequency principle, we divided the learning performance score into two intervals $\leq 27$ and $>27$, and four intervals $\leq 25,25-27,27-29$, and $>29$. After establishing the data set of the university students' innovation team and converting all continuous prognostic factors into discrete variables, a prediction model was established using the TAN algorithm. In this model, team learning performance scores were set as target variables to be predicted, while other factors were considered to be the

attribute variables that affect the status of target variables. Since the two models are built using the same database, the Bayesian network model diagram was consistent (Figure 4).
![img-3.jpeg](img-3.jpeg)

Figure 4. Relationship of Bayesian network prediction model.

# 4.4. Accuracy of TAN Model 

The confusion matrix, reliability, and accuracy of the TAN model are shown in Tables 3 and 4. The independent variables of the data set were used to establish the TAN model to obtain the predicted team performance, compare it with the data in the original record, and then use the confusion matrix evaluation indicators to determine the reliability and accuracy of the TAN prediction model. The two-level classification model of learning performance is shown in Table 3. The reliability and accuracy of prognosis prediction were obtained by using the confusion matrix evaluation index with a default probability threshold of 0.5 .

In the two-level classification model, the number of respondents with a learning performance score of $\leq 27$ was 143 , of which 125 were classified correctly, and the reliability was $84.46 \%(125 / 143)$. The number of respondents with a learning performance score of $>27$ was 85 , of which 62 were classified correctly, and the reliability was $77.50 \%(62 / 85)$. A total of 125 respondents with a learning performance of $\leq 27$ points and 62 respondents with a learning performance of $>27$ points were correctly classified. Therefore, the overall model accuracy is $82.02 \%$ (Figure 5).

Table 3. The confusion matrix, reliability, and accuracy of the two-level classification model.


Table 4. The confusion matrix, reliability, and accuracy of the four-level classification model.


![img-4.jpeg](img-4.jpeg)

Figure 5. ROC curve of learning performance with a survival time of $>27$ months under the two-level classification model.

# 5. Research on the Effect of Dualistic Learning on Innovation Performance 

### 5.1. Research Strategy Design

First, we locked one of the initial states of exploration learning or exploitation learning, and then changed the state of the other to observe the probability distribution of learning performance. Through experiments, the posterior probabilities of both models preliminarily confirmed that the promotion of dualistic learning can improve team innovation performance. For example, the initial state of exploration learning or exploitation learning is in the middle score state. When exploration learning was improved to $>12$, the probability of the learning performance score $>27$ increased from $43.26 \%$ to $71.07 \%$ in the two-level classification model. When exploitation learning was improved to $>12$, the probability continued to increase to $78.63 \%$ (Figure 6).

![img-5.jpeg](img-5.jpeg)

Figure 6. The change of dualistic learning results in the change of learning performance probability in the two-level classification model.

# 5.2. A Posterior Probability Table Based on the Distribution of Dualistic Learning States 

After experimenting with all state combinations of exploration learning and exploitation learning, we obtained a complete posterior probability table of the TAN model that dualistic learning affects innovation performance, as shown in Table 5.

Table 5. Bayesian network posterior probability.


Table 5. Cont.


With the improvement of exploration learning and exploitation learning, the rating of learning performance was also improved. In other words, dualistic learning had a positive feedback effect on learning performance, which is consistent with the research conclusions of previous scholars.

# 5.3. Calculation of Influence Factor Importance

To quantitatively analyze the importance degree of each influencing factor, we introduced the importance calculation method. The general importance calculation method takes into account the occurrence time of the transition, so it was necessary to introduce the probability of the state occurrence into the system model. However, the design of the feature importance calculation method in this paper does not consider the failure function of the feature. It only considers the impact of a factor on the overall system from the perspective of the state change of the feature itself in order to calculate the importance of each influence factor.

We chose Formula (4) as the basic formula for the Birnbaum importance calculation. The calculation method of the Birnbaum importance of the influencing factors in the innovation performance prediction model is given: we first locked all variables in the model, and then changed the prior probability distribution of one of the variables, such as setting the sharing behavior to $\leq 15$, and then observed the difference between the probability of innovation performance $>27$ and its prior probability. Then, we set the sharing behavior to $\leq 18$ to continue recording the difference between the probability of innovation performance $>27$ and its prior probability. Finally, we added up the absolute values of the differences between all states, and calculated the importance by referring to Formula (4). Based on this method, the importance of each influencing factor is shown in Table 6.

Table 6. Feature importance ranking of two-level classification model.


Through the experiment, we found that the importance of the five scale features of sharing behavior, task interdependence, exploration learning, sharing willingness, and exploitation learning were close and at a high level, which was much higher than the three kinds of basic information we obtained through the single factor analysis. The results indicated the importance of dualistic learning for innovation performance. In addition, the study suggested that the importance of sharing behavior ranked first. It can be preliminarily judged that knowledge sharing played an important intermediary role in dualistic learning and team learning performance. The reason was that the knowledge-sharing behavior realised the knowledge circulation flow and knowledge spillover effect within the team, further improving the knowledge structure of team knowledge receivers and disseminators, enhancing the innovation ability and scientific research ability of university students, and promoting the improvement of their team task performance. In follow-up research, based on this experiment, we can further confirm this hypothesis and explore the impacts of other influencing factors on innovation performance and the interrelationship between factors.

# 6. Discussion 

In this study, we established a prediction model based on the Bayesian network and designed a method that can analyze the impact of dualistic learning on the innovation performance of university students in different situations. We explored the knowledge construction and learning performance influencing factors of university students' team learning from the perspective of knowledge construction and performance management. On this basis, we further discussed the mechanism of university student teams' dualistic learning affecting learning performance through empirical research.

The existing literature lacks research on the relationship between team dualistic learning, knowledge sharing, and learning performance from the perspective of predictive modeling. Therefore, we aimed to use statistical methods and importance measure theory to supplement the shortage of existing literature. This research focused on university student teams, constructed a theoretical model of the relationship between dualistic learning, knowledge sharing, and team learning performance, and revealed the "black box" of the mechanism of dualistic learning on team learning performance in the context of university students' innovative team learning by using quantitative and qualitative methods, indicating that the improvement of dualistic learning can significantly promote innovation performance. It is basically consistent with the results of other scholars' research, that is, dualistic learning, as well as knowledge sharing, can positively affect innovation performance or task performance in most cases. Although the research objects and methods are different, there are many similarities between our conclusions and other studies' conclusions.

The theoretical contribution of this study is mainly reflected in two aspects. First, from the perspective of university students' research-based learning, the research results of the enterprise ambidexterity learning theory are expanded to the university students' innovative team learning situation. For university students' learning, the traditional individual level is extended to the team level, the general creativity is shifted to scientific creativity, and the enterprise organizational situation is stretched to the educational organizational situation, which further promotes the integration of team level and scientific dimension and further enriches the theoretical system and research content of organizational learning. Secondly, dividing the ambidexterity learning into exploitative learning and exploratory learning not only explores the direct effects on team task performance directly, however, it also reveals the indirect effect of ambidexterity learning on team task performance through the mediating effect knowledge sharing behavior, revealing the university students' innovation team learning situation and the dual role of team task performance of the "black box".

This study has several limitations. Firstly, the data set only contains 228 samples, so more detailed data screening should be carried out for the questionnaires obtained, key information should be identified, and the dataset should be expanded for future research. Secondly, this study doesn't fully consider the impacts of knowledge sharing and task interdependence on team innovation performance. In the future, based on our calculations of the importance of each influencing factor, we will conduct supplementary research on the mediating role of knowledge sharing and the moderating role of task interdependence.

# 7. Conclusions 

This empirical study explored how the mechanism of dualistic learning affects university student teams' learning performance in the face of rapid changes in higher education. We obtained 228 samples of university student teams from three types of universities. Among them, 121 samples ( $53.1 \%$ ) were obtained from world-class universities, 24 samples $(10.5 \%)$ were obtained from world-class disciplines, and 83 samples ( $36.4 \%$ ) were obtained from other universities. We evaluated these samples and established two BN prediction models of university student team performance using a tree-enhanced Bayesian algorithm. The accuracy rates of the two-level classification model and the four-level classification model were $82.02 \%$ and $64.91 \%$, respectively. In both models, the posterior probability of high learning performance scores increased with the increase of exploitation learning and exploration learning scores. This study shows that the improvement of dualistic learning had a significant impact on innovation performance.

The practical uses of this study are as follows. From the perspective of policy making by innovation team managers, the innovation and entrepreneurship management departments of colleges and universities should actively build an academic community for university students' team knowledge sharing, formulate a scientific and reasonable system, stimulate students' knowledge-sharing motivation, improve students' knowledge sharing ability, promote university students' knowledge resource sharing, and improve the team's

innovation output. From the perspective of university students' team building, we should pay attention to establishing good interpersonal interaction and mutual learning relationships with other members, constantly optimise the team knowledge-sharing environment, promote the knowledge circulation flow within the team, further create a strong academic atmosphere to stimulate college students' learning motivation and enthusiasm. From the perspective of individual students, it is necessary to associate the expectation of success with the teams' subjective task value and pay more attention to the selection and application of learning strategies, so as to promote their teams to achieve higher task performance.

Author Contributions: Conceptualization, Z.C.; methodology, X.Z.; formal analysis, J.L. and C.Z.; investigation, J.L. and C.Z.; data curation, D.S.; writing-original draft preparation, X.Z.; writingreview and editing, Z.C.; supervision, Z.C.; project administration, X.Z.; funding acquisition, X.Z. and D.S. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by the National Social Science Foundation's Social Science Academic Association Themed Academic Activity Funding Program [Grant Nos. 22STA010]; the China Association of Higher Education Program [Grant Nos. 2022ZD03]; Development Strategy Research Fund of Northwestern Polytechnical University [Grant Nos. 2023FZZ09] and Innovation and Entrepreneurship Program of Graduate School of Northwestern Polytechnical University [Grant Nos. D5204210513].

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The experimental data used to support the findings of this study are available from the corresponding author upon request.

Conflicts of Interest: The authors declare that they have no conflict of interest regarding this work.

# Appendix A 

Table A1. Questionnaire.


Table A1. Cont.

