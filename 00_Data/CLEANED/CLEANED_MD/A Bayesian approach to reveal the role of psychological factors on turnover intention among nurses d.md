# A Bayesian approach to reveal the role of psychological factors on turnover intention among nurses during the COVID-19 pandemic 

Saeid yazdanirad ${ }^{1}$, Mojtaba haghighat ${ }^{2}$, Mahsa Jahadinaeini ${ }^{3}$, Amirhossein khoshakhlagh ${ }^{4}$ and Seyedmahdi mousavi ${ }^{2,5 *}$


#### Abstract

Background Turnover intention is considered a significant challenge for healthcare and treatment organizations. The challenging conditions of treating COVID-19 patients and the physical and mental stress imposed on nurses during the pandemic may lead them to leave their jobs. The present study aimed to determine the role of psychological factors (general health, mental workload, work-family conflicts, and resilience) on turnover intention using a Bayesian approach during the COVID-19 pandemic.


Methods The present cross-sectional study was carried out during the winter of 2021 at three hospitals in Khuzestan Province, Iran. To collect data for this investigation, 300 nurses were chosen based on Cochran's formula and random sampling technique. Seven questionnaires, including General Health, Mental Workload, Work-Family Conflict, Resilience, Job Stress, Fear of COVID-19, and Turnover Intention Questionnaires. Bayesian Networks (BNs) were used to draw probabilistic and graphical models. A sensitivity analysis also was performed to study the effects of the variables. The GeNle academic software, version 2.3, facilitated the examination of the Bayesian network.
Results The statistically significant associations occurred between the variables of fear of COVID-19 and job stress (0.313), job stress and turnover intention (0.302), and resilience and job stress (0.298), respectively. Job stress had the highest association with the fear of COVID-19 (0.313), and resilience had the greatest association with the workfamily conflict (0.296). Also, the association between turnover intention and job stress (0.302) was higher than the association between this variable and resilience (0.219). At the low resilience and high job stress with the probability of $100 \%$, the turnover intention variable increased by $20 \%$, while at high resilience and low job stress with the probability of $100 \%$, turnover intention was found to decrease by $32 \%$.
Conclusion In general, the results showed that four psychological factors affect job turnover intention. However, the greatest impact was related to job stress and resilience. These results can be used to manage job turnover intention in medical environments, especially in critical situations such as COVID-19.
Keywords Turnover intention, Job stress, Resilience, Psychological factors, COVID-19 pandemic, Bayesian approach

[^0]
[^0]:    *Correspondence:

    Seyedmahdi mousavi
    mahdi.mousavi90@yahoo.com
    Full list of author information is available at the end of the article

## Background

Turnover intention is a widespread organizational problem that persists across different types and sizes of organizations. It is a particularly pressing issue during manmade or natural crises, leading to lost time and productivity [1]. Therefore, organizations that clearly understand the factors affecting turnover intention can implement effective policies and methods to design and execute comprehensive retention programs [2]. This is important, especially during health crises like pandemics, in which human resources play a crucial role [3]. Throughout the recent COVID-19 pandemic, there has been significant emphasis on the crucial role of healthcare providers in addressing the various aspects of the situation, including prevention and treatment [4]. Accordingly, nurses, comprising nearly 80% of hospital human resources, play a crucial role in responding to medical demands and are considered essential to the health service system [5, 6]. High nurse turnover rates can significantly weaken the ability of health services to respond during times of crisis. A cross-sectional study spanning 10 European countries revealed that 33% of nurses are considering leaving their current jobs or even the profession as a whole [7]. Based on statistics, the financial cost of turnover for each registered nurse in Australia, the United States, and Canada amounted to 48,790, 20,561, and 65,226, respectively [8].

There are various factors that can influence job turnover among nurses. Some of these factors have been mentioned in previous studies, including fatigue, emotional trauma, ethical dilemma, fear of transmitting the disease to family members, general health, mental workload, work-family conflicts, and resilience [9--11]. In previous studies, some of these factors have been less discussed, which are mentioned below. In previous studies, the effect of some of these factors on job turnover has not been paid attention to, which are mentioned as follows.

Paying attention to the general health of nurses is of double importance, as it not only remarkably uplifts their health and well-being but also improves the quality of services they provide. According to the latest research, the COVID-19 outbreak is the biggest threat to nurses' public health in the last 2 years [12--14]. Ki et al. also observed that health problems can significantly affect job turnover among nurses [15].

The second effective factor is mental workload which is defined as the amount of thinking, level of cognitive demand, or thought-processing effort required by a worker to meet the physical, temporal, and environmental demands of the task. High mental workload has been reported as the main source of stress in nurses and can lead to turnover intention [16, 17]. Xiaoming et al. found that workload has a significant effect on burnout and turnover intention among medical staff [18].

The third factor is Work-family conflicts (WFCs). WFCs are the result of an imbalance in the fulfillment of job and family tasks, which, in turn, lays a significant burden on individuals, families, and organizations [19, 20]. Nohe et al. concluded that there are meaningful relationships between work-family conflict and turnover intention [21].

Also, previous studies show that the COVID-19-related fear and stress among nurses who had a direct encounter with COVID patients and provided patient care appeared to be significantly higher compared with nurses in other areas of assignment. Consequently, this debilitating fear can eventually factor into low job satisfaction, burnout, and turnover intention of nurses [22, 23].

Moreover, Job stress occurs when there is no harmony between the job requirements and the individual's abilities, capabilities, and desires [24, 25]. Accordingly, based on the study by Chegini et al. in 2019, stress was recognized as one of the principal factors resulting in an increased rate of turnover intention among intensive care unit nurses [26].

Finally, as an important predictor of nurses' turnover intention, resilience is defined as an individual's belief in their capacity to cope with stress and control their emotional stability, and it is a factor that can contribute to reducing the negative effects of a variety of physical and mental illnesses [27, 28]. According to the literature, factors such as self-esteem, positive communication, hope, adaptability, skill recognition, reducing focus on deficiencies, and flexibility increase resilience levels. In this regard, Wood et al. recommended strengthening resilience in order to deal with professional problems and ensure mental health [29]. Therefore, compromised resilience is considered to increase nurses' intention to leave their jobs.

Understanding which factors contribute to employee turnover is important, as it can be costly for organizations. There may be internal relationships between the mentioned factors, which cause the factors to affect job turnover through different paths. The results of a study performed by Gao et al. showed that there are significant relationships between well-being and mental health with resilience [30]. Yorulmaz et al. found the role of work-family conflict on psychological resilience during the Covid-19 pandemic [31]. Belen et al. observed the relationship between fear of COVID-19 and mental health with resilience during the COVID-19 outbreak [32]. Danielsson et al. reported a significant relationship between health problems and psychosocial stress [33]. Cooper et al. found the associations between mental health and job stress [34]. An et al. observed that work-family conflict can significantly affect job stress and job satisfaction [35]. De los Santos et al. concluded that fear of COVID-19 influences job stress and turnover intentions among

nurses [36]. Also, Cha et al. revealed that there is a relationship between job stress and resilience among nurses [37]. Moreover, the effect amount of these factors on job turnover has not been determined in previous studies. The present study investigates these relationships along with their effect amount.

Different ways can be used to study the factors that lead to employees wanting to leave their jobs. One method is Bayesian network analysis, which is based on probability theory [38]. A Bayesian network consists of nodes and links representing cause-and-effect relationships, which can be analyzed graphically as a system. Causal links depict connections between nodes, often used in conditional probability tables. These networks are helpful for predicting the likelihood of known causes contributing to a particular event [39]. This analysis method has been used in various studies. For example, Herrero et al. used Bayesian network models to study the impact of working conditions on psychological/physical symptoms and occupational accidents [40]. Khoshakhlagh et al. conducted a study to investigate the connection between job stress and safety climate factors in the context of accidents using Bayesian network models [41]. Tokac et al. conducted a study utilizing Bayesian network analysis to delve into the effects of years of nursing experience and mental health on work impairment among nurses during the COVID-19 crisis [42].

As previously mentioned, some of the factors have internal relationships together and influence job turnover intention in relation to each other, which have been less discussed in previous studies. Also, it is not clear which factors have the greatest effect on job turnover intention, which needs to be investigated. Therefore, the present study aims to investigate the impact of psychological factors on turnover intentions among nurses during the COVID-19 pandemic. This research is crucial due to the unprecedented challenges faced by healthcare workers during this global crisis.

## Methods

## Hospital selection

The study, as a cross-sectional analysis, was conducted at three medical hospitals within Khuzestan Province, Iran, during the winter season of 2021. Hospitals were in an area that has experienced a high number of deaths due to the COVID-19 crisis. The sample size was calculated as 300 participants using Cochran's formula. To select the sample, a list of 823 nurses working in COVID-19 wards across various hospitals was provided. From this list, 600 nurses, 200 persons from each hospital, were chosen randomly. Subsequently, their medical records were examined. A total of 523 nurses met the inclusion criteria and were subsequently contacted to enter the study. Out of these, 350 agreed to participate. Ultimately, from the 350 who initially agreed, 300 completed the questionnaires.

## Sampling procedure

Based on the correlation coefficient formula with a significance level of 0.95 and a test power of 0.90 , the sample size was determined to be 350 [43]. Criteria for participation included having at least one year of professional experience, a lack of chronic diseases such as cancer, cardiovascular diseases, and multiple sclerosis, along with mental health stability and not-consumption of psychiatric drugs. These criteria were considered because chronic diseases and mental disorders may affect the assessment of general health and mental workload as two main variables in the present study [44, 45]. Criteria for exclusion encompassed a lack of willingness to participate, failure to cooperate in completing the surveys, and filling out the surveys haphazardly or without proper attention.

## Data collection

A questionnaire was created on an online platform to gather information and sent to the participants via email. Upon entering the site, participants first reviewed and confirmed the study's purpose and a consent form was sent by email. A video guide for completing the questionnaires was available for assistance in the profile's help section. Additionally, contact numbers for the research team were provided for any inquiries. The study period was 15 days. Out of 350 registered nurses, 300 completed all the questionnaires accurately within the specified time frame.

## Tools

This study collected data using seven different surveys. These included questionnaires on general health, mental workload, work-family conflict, resilience, job stress, corona fear, and turnover intention. Information on the reliability and validity of the questionnaires, the number of questions, and how to score them has already been published. The Persian versions of these questionnaires have also been described in detail [46]. The names of the questionnaires are listed below.

## Fear of COVID-19 scale (FCV-19 S)

The Corona Fear Questionnaire, developed by Ahorsu et al. in 2020, is used to assess people's fear of the coronavirus. This questionnaire comprises seven items and uses a five-point Likert scale, with 1 representing the lowest level of fear and 5 the highest. Scores on this questionnaire range from 7 to 35, with higher scores indicating greater fear of the coronavirus. The correlation between the items ranges from 0.66 to 0.74 , and the Cronbach's alpha coefficient is 0.82 . The Persian version of the FCV-19 S questionnaire has shown acceptable reliability

values, with internal consistency (α=0.82) and retest reliability (ICC=0.72). Concurrent validity has been demonstrated with the hospital anxiety and depression scale (depression, r=0.425 and anxiety, r=0.511) [47].

## Job stress questionnaire

The Occupational Stress Inventory consists of 60 items, evenly distributed across six domains: workload, role insufficiency, role ambiguity, role boundary, responsibility, and the physical work environment. Responses on the Osipow Occupational Stress Inventory are evaluated using a 5-point Likert scale. Respondents rate each item with one of five responses: ‘never' scores 1 point, ‘sometimes' scores 2 points, ‘often' scores 3 points, ‘usually' scores 4 points, and ‘most of the time' scores 5 points. The overall score can range from 60 to 300, with higher totals indicative of elevated stress levels [48]. Moreover, Sharifian et al. assessed the validity and reliability of the Persian version of the questionnaire and reported its Cronbach's alpha coefficient as 0.83 [49].

## Turnover intention questionnaire

The questionnaire designed to assess turnover intention, crafted by Kim and colleagues in 2007, consists of 15 items. Responses are gauged using a five-tiered Likert scale that ranges from Strongly Disagree (1) to Agree (5) Strongly. The possible scores one can obtain from this instrument span from a minimum of 15 to a maximum of 75 [50]. Ghaffari et al. conducted a validation study of the Persian version of this questionnaire in Iran. The study reported a reliability of 0.88 and confirmed the questionnaire's validity [51].

## General health questionnaire (GHQ)

Originally developed by Goldberg in 1972, the General Health Questionnaire (GHQ) is a diagnostic tool comprising four distinct subsets, each containing seven items. These items are organized in a sequential manner, with the first seven addressing somatic symptoms, the next set (items 8--14) focusing on anxiety and sleep disturbances, followed by items 15--21 which assess social dysfunction, and finally, items 22--28 pertain to severe depressive conditions. Each item within the GHQ presents four response options, scored on a scale from 1 to 4. Consequently, an individual's overall score can range between zero and 84 [52]. The Persian version of this questionnaire was assessed for reliability and validity in a study by Ebrahimi et al. in 2007, with Cronbach's alpha reported as 0.97 [53].

## NASA-TLX mental workload questionnaire

The NASA Task Load Index (NASA-TLX), crafted by Hart and Staveland in 1988, is a prevalent instrument for gauging workload from an individual's standpoint. This multidimensional approach derives a workload index based on the weighted sum of six distinct dimensions: mental and temporal demands, physical demands, overall performance, exertion, and frustration levels [54]. The validity and reliability of the Persian version of the Mental Worker Questionnaire were assessed by Mohammadi et al. in 2013 and they confirmed the validity and reliability of this questionnaire [55].

## Work-family conflict questionnaire

Carlson et al.'s (2000) study used an 18-item multidimensional questionnaire to measure work-family conflict. According to the literature, work-family conflict can take three forms: time-based, strain-based, and behaviorbased. Gutek et al. (1991) identified two directions for each of these forms: conflict due to work interfering with family (WIF) and conflict due to family interfering with work (FIW). Combining the three forms and two directions results in six dimensions of work-family conflict: (1) time-based WIF, (2) time-based FIW, (3) strain-based WIF, (4) strain-based FIW, (5) behavior-based WIF, and (6) behavior-based FIW. The responses are measured on a Likert scale ranging from 1 (strongly agree) to 5 (strongly disagree) [56].

## CD-RSC resilience questionnaire

The evaluation method for this 25-item instrument, created by Davidson & Connor in 2003, utilizes the Likert scale for scoring, with the following designations: 0 for ‘not at all correct', 1 for ‘seldom accurate', 2 for ‘occasionally accurate', 3 for ‘frequently accurate', and 4 for ‘consistently accurate'. As a result, scores can range from a low of 0 to a high of 100. [57]. In 2007, an assessment was carried out to determine the reliability of the Persian version of the resilience questionnaire developed by Samani et al. [58].

## Data analysis

Statistical analysis was conducted using SPSS software, version 24. Initial steps included conducting descriptive statistical evaluations. Subsequently, probabilistic and graphical representations were constructed utilizing Bayesian Networks (BNs). The GeNIe academic software, version 2.3, facilitated the examination of the Bayesian network. In the subsequent phase, the model generated a Conditional Probability Table (CPT) employing the Expectation-Maximization algorithm. Parameters were prioritized based on the outcomes of delta p sensitivity analysis. To assess the robustness of the model, a 10-fold cross-validation procedure was implemented. Additionally, a sensitivity analysis was carried out to ascertain the impact of different variables on the model.

Table 1 Demographic characteristics of the participants


Table 2 Frequency distribution of the studied variables


Table 3 CPT for turnover intention


## Results

The mean $\pm$ standard deviation (SD) of the age was $42.15 \pm 9.42$. In Table 1, the demographic characteristics of participants are presented. Table 2 also represents the frequency distribution of the studied variables. $49.7 \%$ of subjects had low job stress and $50.3 \%$ of them showed high job stress. $41.0 \%$ of individuals exhibited low resilience and $59.0 \%$ of them had high resilience. $42.3 \%$ of participants were in the group of low turnover intention and $57.7 \%$ of them were in the group of high turnover intention. Table 3 also represents the Conditional Probability Table (CPT) for turnover intention, which describes the relationship coefficient among the variables.

Figure 1 indicates the dependencies among the variables and the marginal probabilities of the studied variables based on the Bayesian network model. Table 4 reports the sensitivity analysis for the studied parameters. At the low general health with the probability of $100 \%$, the probability of the variables of low resilience, high job stress, and high turnover intention increased by 4,14 , and $4 \%$, respectively, and at the high general health status with the probability of $100 \%$, the probability of the variables of high resilience, low job stress, and low turnover intention increased by 3,10 , and $3 \%$, respectively. For the high mental workload with a probability of $100 \%$, the probability of the variables of low resilience, high job stress, and high turnover intention enhanced by 2,4 , and $2 \%$, respectively, and for low mental health with the probability of $100 \%$, the probability of the variables of high resilience, low job stress, and low turnover intention increased by 3,5 , and $2 \%$, respectively. For the high WFCs

![img-0.jpeg](img-0.jpeg)

Fig. 1 The marginal probabilities of the studied variables based on the Bayesian network model

Table 4 Sensitivity analysis for the studied parameters


with a probability of $100 \%$, the probability of the variables of low resilience, high job stress, and high turnover intention increased by 8,6 , and $4 \%$, respectively, and for the WFCs with a probability of $100 \%$, the probability of the variables of high resilience, low job stress, and low turnover intention increased by 11,7 , and $5 \%$, respectively. At the high fear of COVID-19 with the probability of $100 \%$, the probability of the variables of low resilience, high job stress, and high turnover intention increased by 1,8 , and $2 \%$, respectively, and at the low fear of COVID-19 with the probability of $100 \%$, the probability of the variables of high resilience, low job stress, and low turnover intention increased by 3,16 , and $5 \%$, respectively. For the low resilience with the probability of $100 \%$, the probability of the variable of high turnover intention enhanced by $8 \%$, and for the high resilience with the probability of $100 \%$, the probability of the variable of high turnover intention decreased by $18 \%$. For the high job stress with the probability of $100 \%$, the probability of the variable of high turnover intention increased by $16 \%$, and for the low job stress with the probability of $100 \%$, the probability of the variable of high turnover intention decreased by $17 \%$. At

the low resilience and high job stress with the probability of $100 \%$, the probability of the variable of high turnover intention increased by $20 \%$ and the high resilience and job stress with the probability of $100 \%$, the probability of the variable of high turnover intention decreased by $32 \%$.

Table 5 represents the computed influence value from the association of the factors in the model. The most significant mean values belonged to the association between variables of fear of COVID-19 (0.313) and job stress, job stress, and turnover intention ( 0.302 resilience and job stress ( 0.298 ), respectively. Job stress had the highest association with the fear of COVID-19 (0.313) and resilience showed the greatest association with the workfamily conflict ( 0.296 ). Also, the association between turnover intention and job stress ( 0.302 ) was higher than the association between this variable and resilience ( 0.219 ).

A ROC curve was drawn to evaluate the validity of the fitted Bayesian model, shown in Fig. 2. The area under the curve was equal to 0.681 . The confusion matrix related to the classification of the quality patient care status was also calculated and reported in Table 6. Also, the values of the sensitivity, specificity, and accuracy of the model were $0.647,0.693$, and 0.700 , respectively.

## Discussion

The results of the present study showed that job stress and resilience had the highest effect on turnover intention among the studied variables. The four psychological factors also could affect job stress, resilience, and turnover intention. Fear of COVID-19 and work-family conflicts were found to be the most influential factors contributing to turnover intention.

In fact, there is a correlation between high workload, as a dimension of occupational stress, and poor general health. If stress is not dealt with timely, it can lead to nurses' burnout and in turn a decrease in the quality of patient care as one of the worst consequences [59]. Also, results of the study of Chen et al. showed that job stress was positively related to turnover intention ( 0.57 ,

CI $[0.45,0.68])$, which was further positively associated with their turnover intention ( 0.82 , CI $[0.73,0.92])$ [60]. In the study of Moghaddam et al., the results of the multiple linear regression analysis showed that job stressors could significantly affect turnover intention. Job stress compared to other factors had the greatest impact on turnover intention ( $\beta=0.624, p=0.013$ ) [61]. According to previous research, there is a significant link between psychological well-being and resilience, and resilience, along with higher levels of job and family satisfaction, enables workers to strike a balance between work and family. Therefore, steps can be taken to reduce WFCs by fostering favorable settings for nurses and boosting their resilience $[62,63]$.

Yawei et al. conducted a study on 446 nurses to investigate their mental workload during the coronavirus epidemic. The study found that new and young nurses experienced the highest mental load. It is assumed that in the conditions of covid-19 pandemic, the mental workload of nurses, especially novice nurses, increases due to psychological pressures and results in increased job stress. Hence, reducing the mental workload and, ultimately, the occupational stress of nurses seems necessary because the duties of healthcare workers are particularly sensitive in the conditions of the COVID pandemic and can result in irreparable complications in the event of medication and medical errors [64]. The results of the study of Yang Xiaoming et al. demonstrated that workload had remarkable effects on turnover intention. Time load ( $\beta=2.153, p<0.001$ ), spirit investment ( $\beta=2.342$, $p<0.001$ ), and mental stress ( $\beta=2.573, p<0.001$ ) dimensions of the workload showed significant positive effects on turnover intention [65]. Based on the results of a study performed by Herrero et al. revealed that excessive workload increased workers' stress by $42.9 \%$. It is possible to argue that Covid-19 has increased the workload on nurses, causing them to put themselves in danger to save the lives of others and devote more time and focus to their work [66].

Table 5 The computed influence value from the association of the factors in the model


![img-1.jpeg](img-1.jpeg)

**Fig. 2** the ROC curve



The findings of an empirical study conducted by Alsam et al. on employees of the Pakistani banking sector revealed a positive and significant impact of work-family conflict on turnover intentions [67]. Moreover, Azhar et al. explored the association between work-family conflict and turnover intention. The findings of this study indicated that work-family conflict has a positive and significant interrelationship with turnover intention (*r*=0.262).

$p<0.01$ ) [68]. Additionally, social support significantly reduced stress levels [69]. Moreover, considering the highest value of WFCs ( $100 \%$ unfavorable) along with the lowest value of WFCs ( $100 \%$ favorable), the most significant change is in items related to increasing low resilience and increasing high resilience, respectively.

As reported in a 2021 study by Leodoro et al., the fear of COVID-19 is significantly linked to stress among Filipino nurses. Given that nurses are more exposed to infected patients, it's crucial to provide them with proper training in COVID-19 prevention and treatment to reduce their stress levels [2]. Popa et al. found that resilience can protect nurses' mental health from the negative effects of COVID-19 fear [70]. The fear of the COVID-19 outbreak has placed a heavy psychological strain on the medical staff, particularly nurses. Lack of knowledge and awareness and spread of new COVID variants contribute to the rising fear of COVID-19. Nurses are more prone to the fear of catching the virus and transmitting the infection due to the nature of their job and exposure to infected patients. Increased fear and stress, decreased resilience, rising work-family conflicts, and declining general health can lead to higher turnover intention among nurses, which can strain the health system and lead to understaffing [71]. To reduce nurses' fear of COVID-19 and decrease task-related stress, measures should include stress management interventions such as raising awareness, teaching problem-solving skills, and enhancing resilience. These efforts can help reduce turnover intention and improve nurses' mental and physical health [72]. Among the other findings of the present study, a noteworthy $20 \%$ increase in turnover intention is observed, particularly in scenarios characterized by the lowest resilience and highest stress levels (the least favorable cases). The results of a study performed by Erhan Ekingen et al. showed that a one-unit increase in the nurses' fear of COVID-19 level caused a 0.68 -unit increase in their stress levels and a 0.13 -unit increase in turnover intentions. In addition, a one-unit increase in the nurses' work stress level caused a 0.35 increase in turnover intention [73]. Murat et al. also observed that controlling COVID19 was linked to public health promotion and reduced job stress [31]. These results are consistent with those of the present study.

## The limitations of the study

It seems that there are various psychological factors to predict and influence turnover intention. Therefore, the lack of examination of various factors on turnover intention can be considered one of the limitations of this study.

## Implication of the results

In general, the results showed that four psychological factors affect job turnover intention. However, the greatest
impact was related to job stress and resilience. These results can be used to manage job turnover intention in medical environments, especially in critical situations such as COVID-19.

## Conclusion

In the research findings, it was observed that all four psychological factors, namely fear of COVID-19, general health, mental workload, and work-family conflicts (WFCs), had significant associations with job stress, resilience, and turnover intention. Specifically, fear of COVID-19 and general health had the most impact on job stress, whereas high work-family conflicts had the greatest influence on resilience. Additionally, fear of COVID-19 and work-family conflicts were found to be the most influential factors contributing to turnover intention. The combined impact of these psychological factors shows that high job stress and low resilience, attributed to fear of COVID-19, general health, workfamily conflicts, and overall resilience, could lead to a substantial $20 \%$ increase in turnover intention. It is suggested that necessary measures be taken to reduce mental workload, maintain public health, reduce workfamily conflict, and decrease fear of COVID-19 so that work-related stress and thereby job turnover intention is diminished. Also, the results determined that a useful measure to increase people's tolerance against job stress and reduce job turnover intention can be resilience, which requires planning to increase it. Also, It is proposed that the impact of other psychological factors that were not investigated in this study be measured in future studies. It is also apparent that other unpredicted psychological factors can be included in future studies.

## Acknowledgements

Researchers need to thank all staff who have participated in this study.

## Author contributions

Saeid yazdanirad: Conceived and designed the experiments; Analyzed and interpreted the data; Wrote the paper. Mojtaba haghighat and Amirhossien khoshakhagh : Conceived and designed the experiments; Analyzed and interpreted the data.Mahsa jahadinaeini: Performed the experiments; Wrote the paper. Seyedmahdi mousavi: Contributed reagents, materials, analysis tools or data; Wrote the paper.

## Funding

This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.

## Data availability

The data that support the findings of this study will be available from the corresponding author, upon reasonable request.

## Declarations

## Ethics approval and consent to participate

The study was approved by the ethics committee of Behbahan Faculty of Medical Sciences under code IR.BHN.REC.1401.024. All methods were performed in accordance with relevant guidelines and regulations. Informed

consent was obtained from all subjects. All subjects were allowed to withdraw from the research at any time during the research period.

## Consent for publication

Not applicable.

## Competing interests

The authors declare no competing interests.

## Author details

${ }^{1}$ School of Public Health, Shahrekord University of Medical Sciences, Shahrekord, Iran
${ }^{2}$ Behbahan university of medical sciences, Behbahan, Iran
${ }^{3}$ Department of Occupational Health Engineering, School of Public Health, Isfahan University of Medical Sciences, Isfahan, Iran
${ }^{4}$ Department of Occupational Health Engineering, Faculty of Health, Kashan University of Medical Sciences, Kashan, Iran
${ }^{5}$ Student Research Committee, Department of Occupational Health and Safety Engineering, School of Health, Isfahan University of Medical Sciences, Isfahan, Iran

Received: 23 March 2024 / Accepted: 11 July 2024
Published online: 01 August 2024

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.