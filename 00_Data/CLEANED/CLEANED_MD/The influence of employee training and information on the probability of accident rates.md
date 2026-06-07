# The influence of employee training and information on the probability of accident rates. 

E.M. López-Perea, M.A. Mariscal, S. García-Herrero \& J.R. López-García<br>University of Burgos, Spain

S. Herrera

University of Cantabria, Spain
ABSTRACT: The construction industry is one of the most important socio-economic sectors of the Spanish economy and one of the most affected by workplace accidents. An analysis of the data on accident rates is needed, in order to identify variables related with workplace accidents and to define the measures that need to be taken for their reduction. In this study, an analysis is conducted using Bayesian Networks and data from the 7th National Survey on Working Conditions (VII NSWC), to study the relations between workplace accidents, visiting a doctor for occupational reasons, time in the company/sector, information that workers have on workplace risks in the workplace, and information and training on workplace risks that workers have received over the past two years. The NSWC survey, which is conducted every four years, was administered to 8892 workers, in Spain, in 2011. The values derived from the analysis yield certain implications involving the aforementioned variables and how to reduce the probability of workplace accidents. From among the variables under study, information on workplace risks is the most important, with the probability of suffering an accident in the construction industry doubling when such information is insufficient. In accordance with the results, these implications could also help with decision-making focused on improvements to training and on-the-job information, intended both to prevent and to reduce workplace accidents

## 1 INTRODUCTION

Workplace accidents are among the worst problems in modern-day society. Despite every effort to prevent these accidents, they not only persist, but, in some cases, are even on the rise. For example, in 2014 there were 491,099 (580) lost-time (fatal) accidents in Spain, an increase of 23,069 (22) with respect to 2013 (MEYSS, 2015a, 2015b). In addition, preliminary reports for 2015 again reflected increases in both lost-time accidents, up to 518,988 , and fatal accidents, up to 608 (MEYSS, 2016). A broader view that considers the trend over recent years shows a significant reduction in workplace accidents, which reached a minimum in 2012. Since then, however, accident rates have been climbing significantly (MEYSS, 2015a). Regarding the different socio-economic sectors, the construction industry in Spain is of the utmost concern with an incident rate (no. of accidents / workers exposed) of 6314 accidents per 100,000 workers in 2014, approximately doubling the average for each sector, 3111, in that year (MEYSS, 2015a). These data, gathered both by the National Healthcare System and by the Social Security Administration, highlight the need to improve our understanding of the factors affecting both the occurrence and the severity of workplace accidents.

The Ministry of Labor and Social Security (MEYSS), through the National Institute for Workplace Safety and Hygiene (INSHT), conducts National Workplace Condition Surveys (NWCS) for various purposes, including identifying the frequency of exposure to occupational risks and characterizing the most frequent occupational exposures, in order to determine the preventive measures that companies are taking and to ascertain which workplace factors exercise most influence on employee health. The NWCS has been conducted in Spain since 1987, with seven having taken place to date, in 1987, 1993, 1997, 1999, 2003, 2007 and, most recently, the 7th NWCS in 2011. The data from the 8th NWCS is soon to be released. The survey is conducted every four years and has become an essential information tool in the area of workplace health and safety (Artazcoz, 2003). Moreover, surveys on working conditions are also conducted in the European Union, in this case by the European Foundation for the Improvement of Living and Working Conditions (EUROFOUND), an independent European Union agency located in Dublin. The first was in 1990, and since then they have been carried out every five years. The most recent survey published was the Sixth European Survey on Working Conditions (2015), with almost forty-four thousand European workers of 35 nationalities. These workers were sampled from every country in the Union, including Spain.

In addition to the data collection, in the past decade different data-mining techniques have been applied in this framework to improve our knowledge of workplace accidents. For example, Squillante et al. proposed a probabilistic approach based on Bayesian Networks to design safety systems for industry using databases with missing data (Squillante et al., 2018), Liao et al. applied Bayesian Networks to analyze the role of human errors in the occurrence of workplace accidents (Liao, Shi, Su, \& Luo, 2018), Sanmiquel et al. applied

different data-mining techniques to analyze accidents in mining (Sanmiquel, Rossell, \& Vintro, 2015); Mohajeri and Amiri applied fuzzy logic techniques to rank the causes of fall accidents in construction projects (Mohajeri \& Amiri, 2014). -Rivas et al. compared different data-mining techniques, modelling accidents in mining and construction sectors (Rivas et al., 2011). This study suggests that the Bayesian Networks technique (Castillo, Gutiérrez, \& Hadi, 1997), extensively used in risk analysis (Gerassis, Martin, Garcia, Saavedra, \& Taboada, 2017; Ghasemi, Kalatpour, Moghimbeigi, \& Mohammadfam, 2017; Papazoglou, Aneziris, Bellamy, Ale, \& Oh, 2017) over the past few years, is one of the most appropriate data-mining techniques for such an analysis.

In this work, our primary aim is to determine the relation or influence that training and information have on occupational risks and accident rates in the workplace. Bayesian Networks are applied to analyze the data from the 7th National Survey on Working Conditions (VII NSWC), to study the relationship between workplace accidents, visits to a doctor for work-related reasons, time in the company/sector, the information that workers have on occupational risks in the workplace, and the information or training that they have received over the past two years on occupational risks. The paper will be organized as follows: Section 2 will describe the variables considered as key factors in the occurrence of workplace accidents, Section 3 will describe the data and methodology used, Sections 4 and 5 will summarize the main results and conclusions, whilst Section 6 will mention the main limitations to this study and the future challenges.

# 2 VARIABLES INFLUENCING WORKPLACE ACCIDENTS 

Some definitions of a workplace accident may be considered, for a better understanding of the figures given in the previous section, before going on to describe the variables that affect workplace accidents. Spain's Ministry of Labor and Social Security (MEYSS) defines a workplace accident as any bodily injury sustained by a worker as a result of performing work for someone else. A lost-time accident is one that causes the worker to be absent from work for one day, not including the day of the accident (MEYSS, 2015c).

Several research papers have attempted to analyze the causes of and the main risks involved in workplace accidents. An initial separation may be made by dividing the causes of accidents into triggers (which lead immediately to an accident) and basics (underlying causes) (Baselga, 1984).

An example of triggers is provided in the 2014 report on accidents in Spain, which lists the most frequent type of accident as "physical over-exertion of the musculoskeletal system", accounting for $38.9 \%$ of all accidents, followed by "hitting immovable objects", at $24.5 \%$ of all accidents, and "hitting moving objects and collisions", amounting to $13.4 \%$ of all accidents. These three groups account for $76.8 \%$ of all lost-time accidents.

There are additional studies that set out to discover the basic causes and their effects by analyzing broader factors, such as work site, individual factors and working conditions (Bolivar Munoz, Daponte Codina, Lopez Cruz, \& Mateo Rodriguez, 2009), risk assessment and a climate of occupational safety (Pinto, Nunes, \& Ribeiro, 2011), the definition of safety from the initial planning of a project and increasing the role of employees to ensure overall safety (Haslam et al., 2005), investments in prevention (López-Alonso, IbarrondoDávila, Rubio-Gámez, \& Munoz, 2013), and labor market characteristics (Giraudo, Bena, Leombruni, \& Costa, 2016).

An increasing number of studies have pointed to prevention, information (Mattson, Hellgren, \& Goransson, 2015) and training (Misiurek \& Misiurek, 2017; Rivas et al., 2011; Suárez-Cebador, Rubio-Romero, Car-rillo-Castrillo, \& López-Arquillos, 2015) as basic tools for reducing accident rates. Along these lines, Cheng et al. found safety management, supervisor training in this area and the degree of compliance with workplace health and safety regulations as the typical factors behind workplace accidents (Cheng, Leu, Lin, \& Fan, 2010). Hasle et al. concluded that there is a need to educate owners and employees on those factors that contribute to the occurrence of accidents, so as to determine the proper prevention measures (Hasle, Kines, \& Andersen, 2009).

The development of strong leadership, of transformational characteristics that assign responsibilities to all involved, demonstrates that the resulting climate is one of improved safety, with fewer accidents and injuries. These measures are applicable to every sector, from construction (García-Herrero, Mariscal, López-García, \& Cofiño, 2015) to specific industries, such as nuclear power plants (García-Herrero, Mariscal, Gutiérrez, \& Toca-Otero, 2013; Hoffmeister et al., 2014; Mariscal Saldaña, García-Herrero, López Perea, Toca Otero, \& Obeso Torices, 2015).

As a result, in this study we wish to analyze how such factors as the information available to workers on job-related risks and the training received over the previous two years influence accident rates.

# 3 METHODOLOGY 

### 3.1 Data acquisition

The National Institute for Workplace Safety and Hygiene (INSHT) conducts periodic nationwide surveys intended to provide statistical information on the working conditions and health of various groups of workers and on how companies organize and carry out preventive actions. The survey was first conducted in 1987. Starting with the third edition in 1997, the surveys are available on the INSHT website (http://www.insht.es). The last three surveys were the $5^{\text {th }}$ ENCT (Almodovar, 2003), administered to 5236 workers in 2003; the $6^{\text {th }}$ ENCT (Almodovar \& Pinilla, 2007), administered to 11054 workers in 2007; and the $7^{\text {th }}$ ENCT (Almodovar \& Pinilla, 2011), administered to 8892 workers in 2011. The number of workers per sector surveyed in each ENCT is shown in Table 1. Note that these data do not include civil servants and freelancers who opted out of specific coverage for professional contingencies.

The model was developed with data from the 7th Spanish National Workplace Conditions Survey database (Almodovar \& Pinilla, 2011). The field work was carried out between October 2011 and February 2012.

Table 1: Number of workers surveyed by sector.


Source: Compiled by authors from 5th, 6th and 7th NWCS data.
The survey involved a total sample of 8892 workers, who were interviewed in their homes using a 62 -point questionnaire. A confidence interval of $95.5 \%$ was defined for the survey, which yielded a sampling error of $\pm 1.1 \%$. The population group involved in the survey employed individuals aged 16 and older. All the data in this study were compiled from the survey data. None of the variables, such as area of activity or size of staff, for example, was weighted. The survey can be found at:
http://encuestasnacionales.oect.es/enge/EngeCuestionarios.jsp
Table 2: Results of the variables used in the 8892 surveys.


Source: Compiled by authors from 7th NWCS data.
The study attempts to ascertain how certain variables affect workers' decisions to visit a doctor, due to workplace-related health problems, and how they affect workplace accident rates. The original results from

the variables used in the study are shown in Table 2. Twelve respondents gave no answer when asked if they had had a workplace accident over the past two years. Those questionnaires were therefore eliminated from the study, leaving 8880 .

Table 3 shows that the total number of workers reporting an accident, based on survey data, was 686, of whom $32(4.7 \%)$ worked in the agricultural sector, $170(24.8 \%)$ in the industrial sector, $50(7.3 \%)$ in construction and $434(63.3 \%)$ in the services sector.

Table 3: Number of workers reporting an accident.


Source: Compiled by authors from 7th NWCS data
We should note that these data yield the initial probabilities of the occurrence of an accident. As the data originated from a survey to which the worker responds, and not from an official record, they may differ slightly from official statistics. Moreover, the specific question in the survey asks whether the worker has had an accident over the past two years, not over the past year, which is what the firm has to notify to the authorities. The period changes but the figures remain the same.

Table 4: Visited doctor due to work-related problems.


Source: Compiled by authors from 7th NWCS data.
The percentage of workers who visited a doctor due to a health problem resulting from or aggravated by workplace activities is shown in Table 4.

# 3.2 Factors studied 

The model is proposed to examine how employee training and information affect the probability of workplace accident rates. It includes aspects relating to worker training and information, as well as aspects that directly affect the worker such as contract type, length of time in the job, and industry in which the worker is employed.

Finally, the model included workplace accidents in which workers were involved over the past 2 years, which is the outcome variable of the model, along with the worker's visits to the doctor as a result of worsening health.

The following variables were studied:

- Type of employee contract. This variable is associated with question 3 on the NWCS "What contract type do you have?", shown in Table 5.
- Length of time on the job. This variable is associated with question 13 in the questionnaire "How long have you been working at your place of employment?", shown in Table 6.
- Information on the health and safety risks associated with the worker's activities that the worker has received. This variable is associated with question 48 of the questionnaire "How informed would you say you are concerning the risks at your workplace to your health and safety?". The responses to the question are shown in Table 7.

- Training or information received in the previous two years on the health and safety risks is associated with question 49 on the questionnaire "In the last two years, have you received any training or information on the risks to your health and safety associated with your job?" The responses to the question are shown in Table 8.
- Accidents reported by workers. This variable corresponds to question 52 on the NWCS "In the last two years, have you experienced a workplace accident that required medical assistance or treatment, or the application of first aid?" (see Table 3).
- Visits to the doctor due to a health problem resulting from or aggravated by workplace activities is associated with question 54 on the questionnaire "Could you tell me if you have any of the following health problems? Have you seen a doctor for this health problem?". The relevant data is shown in Table 4 .

Table 5: Question 3 on the NWCS


Source: Compiled by authors from 7th NWCS data. The contract types, as presented in the questionnaire, are shown in Table 5. The question is preceded in the questionnaire by another one that differentiates between salaried and all other employees. This distinction results in Table 5 containing a section on non-salaried workers, which includes freelancers, business owners, etc. Both questions were combined for easier processing of the data.

In the questionnaire, the worker's length of time in the job lists the numbers of months and years separately. These data are presented in Table 6 below, which will now be considered, converted to show the intervals and the number of answers received.

Table 6: Question 13 on the NWCS converted into intervals with the number of answers


The exact text of question 48 is: How informed would you say you are concerning the risks at your workplace to your health and safety? The responses to this question are shown in Table 7.

Table 7: Question 48 on the NWCS


Source: Compiled by authors from 7th NWCS data. The exact text of question 49 is: In the last two years, have you received any training or information on the risks to your health and safety associated with your job? The answers to this question are shown in Table 8.

Table 8: Question 49 on the NWCS

In the last two years, have you received any training or in-
formation on the risks to your health and safety associated
with your job?

Source: Compiled by authors from 7th NWCS data.

The exact text of question 52 is: In the last two years, have you experienced a workplace accident that required medical assistance or treatment, or the application of first aid? The answers to this question are shown in Table 3.

Question 54 in the questionnaire is quite long, as the same question encompasses three concepts. It first asks what health problems the worker has. If any, the question then asks whether the worker feels the problem was aggravated or caused by work. It finally asks if the worker has seen a doctor as a result of this health problem. In our study, we only used the third question, and the results revealed that 3618 workers, or $40.7 \%$, had visited a doctor at least once due to these kinds of problems. These figures are shown in Table 4.

# 3.3 Bayesian Networks and Model Performance.

Bayesian Networks (Castillo et al., 1997) is a widely applied machine learning technique to infer relations between different aspects/factors of a particular problem, for example workplace accidents. From a formal point of view, Bayesian Networks are a probabilistic graphical model (PGM), (Koller, 2009) based on a directed acyclic graph (DAG), which are commonly used to represent and to infer knowledge under conditions of uncertainty, and to spread new evidence of knowledge regarding the state of some of the variables included in the model. Therefore, Bayesian Networks method is perfectly aligned with the objective of the present study. In particular, Discrete Bayesian Networks, due to the discrete nature of the variables considered in this study which limits the application of other techniques (e.g. regression-based methods). Moreover, the DAG

gives us a graphical and easily interpretable representation of the dependencies between the variables under consideration.

From a practical point of view, the application of BNs to real-world problems depends on the graphical structure, which defines the dependence (conditional or otherwise) between the different variables of the model, and on the parameters of the probability tables. Note that these probabilities are obtained according to the factorization of the joint probability distribution defined by the DAG; both the DAG and the probabilities were directly obtained from data (Neapolitan, 2004) using appropriated learning algorithms (e.g. K2algorithm for the DAG). As a result, the probability of an accident can be inferred through evidences in the different factors under consideration, which is the objective of this work.
A K-fold cross validation approach, with $\mathrm{K}=10$, was considered to define a partition of the sample into 10 folds containing $10 \%$ of the total sample, in order to evaluate both the effectiveness and the generalization capabilities of the model. A BN network was obtained for each fold, considering the other $90 \%$ of the sample, which was used to obtain a prediction from each fold. The prediction was evaluated in terms of the Area Under the ROC (Receiver Operating Characteristic, Fawcett 2006) Curve (AUC), which is a standard measure of overall accuracy (Hanley \& McNeil, 1982) for probabilistic and binary classifiers. Note that this parameter varies from 0.5 (random guess) to 1 (perfect performance). Finally, a prediction for the whole sample was obtained by joining the predictions of each of the 10 -folds and then evaluating it. There were therefore eleven AUC values, ten from each of the folds plus the one corresponding to the whole sample.

All the calculations in this study have been developed using the Bayes Net (Murphy, 2001) and MeteoLab (Gutiérrez, 2004) Toolboxes for Matlab (MATLAB)

# 3.4 Bayesian Networks applied to accident prevention 

Bayesian networks have been used in many areas of knowledge such as medicine (Antal, Fannes, Timmerman, Moreau, \& De Moor, 2004), ecology, and the management of natural resources (Borsuk, Stow, \& Reckhow, 2004; McCann, Marcot, \& Ellis, 2006; Miras, 2010), and geology (Rivas, Matias, Taboada, \& Arguelles, 2007).

This tool is also routinely used in such as life-cycle engineering (Zhu \& Deshmukh, 2003), software engineering (Fenton et al., 2007) and reliability (Langseth \& Portinale, 2007).

Bayesian Networks are commonly used in work intended to reduce accidents in specific sectors, such as the maritime industry, offshore drilling operations and aviation (Akhtar \& Utne, 2014; Brooker, 2011; Khakzad, Khan, \& Amyotte, 2013; Ren, Jenkinson, Wang, Xu, \& Yang, 2008; D. Zhang, Yan, Yang, Wall, \& Wang, 2013; G. Z. Zhang \& Thai, 2016), and to reduce specific risks, such as falling hazards (Martin, Rivas, Matias, Taboada, \& Argueelles, 2009), and accidents caused by movement (Abdat, Leclercq, Cuny, \& Tissot, 2014). In the latter study BNs were used to identify those circumstances that have a greater effect on workplace accidents while on the job, such as the use of unsafe work postures, task duration and worker unfamiliarity with safety regulations.

At a different level, there are the studies that use BNs to determine the influence of psychosocial factors as generators of risk. Within this field there are studies that identified heavy workloads, dangerous exposures and job dissatisfaction (Laaksonen, Pitkaniemi, Rahkonen, \& Lahelma, 2010), personal experience factors (Zhou, Fang, \& Wang, 2008), stress (Cardenas-Gonzalo, Garcia-Herrero, Mariscal-Saldana, \& GutierrezLlorente, 2015; García-Herrero, Mariscal-Saldaña, López-Perea, \& Quiroz-Flores, 2016) or organizational aspects and the safety culture and safe work behavior (Jitwasinkul, Hadikusumo, \& Memon, 2016; Mariscal Saldaña, García Herrero, Toca Otero, \& Gutierrez Llorente, 2012; Mohammadfam, Ghasemi, Kalatpour, \& Moghimbeigi, 2017).

There are some studies closer to the topic of our research that rely on similar surveys, whether national or European. In a study with data from 2011, (García-Herrero, Mariscal, García-Rodríguez, \& Ritzel, 2012) related accidents and their causes. This study was also focused on analyzing the relations between conditions involving hygiene, ergonomics and occupational demands and physical and psychological symptoms. There are also numerous studies that use BNs in an effort to relate stress to workplace conditions so as to reduce this stress (García-Herrero et al., 2016; García-Herrero, Mariscal, Gutiérrez, \& Ritzel, 2013).

## 4 RESULTS

The Bayesian Network that is generated is shown in Figure 1. The BN model considers doctor visits (ASISTENC...), information on risks (P48INFO...), training received (P49FORM...), contract type (P3CONTR...), time on the job (P13TIEMP...), the workplace accident variable (P52ACCID) and the sector

or activity variable (SECTOR_...). This network shows all the significant dependencies existing between the variables and the accident report.

On the one hand, three variables, accident, training, and length of time in the job, are identified as independent (without "parents", i.e., at the end of an arrow and linked to other variables), while the state of the other variables will be conditioned by explicit knowledge in each case, which is reflected by the factorization of the joint probability distribution:

$$
\mathrm{P}(\mathrm{~A}, \mathrm{DV}, \mathrm{CT}, \mathrm{ToJ}, \mathrm{~S}, \mathrm{~T}, \mathrm{IoR})=\mathrm{P}(\mathrm{~A}) \mathrm{P}(\mathrm{ToJ}) \mathrm{P}(\mathrm{~T}) \mathrm{P}(\mathrm{DV} \mid \mathrm{A}, \mathrm{ToJ}) \mathrm{P}(\mathrm{IoR} \mid \mathrm{DV}, \mathrm{~T}) \mathrm{P}(\mathrm{~S} \mid \mathrm{CT}, \mathrm{ToJ}, \mathrm{~T})
$$

On the other hand, as might be expected, there is a direct connection between accidents and visits to a doctor, and this variable connects the accident with the rest of the graph, defining a conditional dependence between accidents and length of time in the job or training, once the status of the visits to the doctor is known.

Figure 1: Bayesian Network Model
![img-0.jpeg](img-0.jpeg)

Source: Compiled by authors.
Table 9 shows the variation in the probability of an accident when the result of question 48 on the training and information given to the worker on workplace risks is varied (see table 9). This is done by starting with the initial probabilities and then showing the probability of an accident, on the assumption that very good $(\mathrm{R}=1)$, good $(\mathrm{R}=2)$, not very good $(\mathrm{R}=3)$ and poor $(\mathrm{R}=4)$ information was given to the worker. The study also considers various sectors.

Table 9: Variation in accident probability by sector as a function of information received on the risks (Q 48)


Source: Compiled by authors from BN model.
The results in this table are very important, since they indicate that receiving very good information on risks does not yield the lowest probability of an accident; rather, receiving good information does. This is the case in the agriculture ( $3.86 \%$ ), industry ( $9.67 \%$ ) and construction ( $7.53 \%$ ) sectors. In the services sector, however, receiving very good information does yield the lowest probability of an accident (5.77\%). One might conclude, then, that information is needed to reduce the probability of accident, regardless of whether it was good or very good information.

Table 10 below shows the variation in the probability of an accident for the same case as in Table 9, but for a worker who has seen a doctor for work-related health problems. Every value increases considerably in the

table, confirming that for workers who visited a doctor previously, the probability of an accident increases significantly, even doubling in some cases.

The initial data show how the most problematic sector in terms of workplace accidents is industry, with the probability of an accident occurring of $12.03 \%$. The figure under the same heading is $8.1 \%$ for the construction sector.

Table 10: Variation in accident probability by sector for workers who have visited a doctor based on their knowledge of the risks at their workplace


Source: Compiled by authors from BN
For the construction industry, acting on information on workplace risks reveals how very good information on those risks can actually raise the probability of an accident somewhat. This observation indicates that there is not much difference between providing good information on risks and very good information, since the probability of having an accident is very similar. However, the lack of information increases this probability, even doubling it.

When analyzing the data on workers who have visited a doctor, these probabilities also increase significantly, especially when the information is not very good.

Lastly, there is very little variation as a function of the information and training received on workplace risks in the previous two years. This variation is even lower when no such information was received. For workers who visited a doctor, the probability of an accident occurring decreases from $12.39 \%$ to $10.24 \%$ when no information was received. For workers who did not visit a doctor, this probability decreases from $5.84 \%$ to $3.43 \%$ when no information was received.

A very interesting aspect is to see the change in the probability of an accident occurring based on the information on risks given to the worker, the training received in the last two years and the type of contract. These results are shown in Table 11. Note that there are several situations in which the probability of an accident cannot be calculated, due to the low number of workers in a given situation, such as workers hired through a placement agency, which accounted for 40 out of 8880 .

Table 11: Accident probability by contract type, information and training.


Source: Compiled by authors from BN model.

In those cases for which a calculation was possible, we see that the initial $7.48 \%$ probability of an accident occurring rises significantly as the information known by the worker concerning the workplace risks decreases. With the same information, however, the probability drops, when less prevention information is available, which might indicate that information is provided primarily for jobs subject to higher risks.

By contract type, training contracts exhibit the highest increase in accident rates for every case, sometimes doubling the probability $(14.20 \%)$. In the case of indefinite or permanent contracts, the information and training received in some cases increased the rates and in others they decreased it, based on the reference probability. Note that the highest increase in the accident rate for contracts that are not indefinite or permanent reaches $26 \%$ and $27 \%$.

In the BN network, the influence of the variable time on the position of employment may be seen. For example, Table 12 shows the relationship between this variable and the visits to the doctor, due to work-related health problems and the quality of the information received on occupational risks. The main results of this table are shown in Graph 1. Note the general rise in the number of visits to the doctor with the length of time in the job. This tendency is natural, as time in the job is directly related to age.

Another conclusion that can be drawn is that as the information on workplace risks worsens, the higher the number of visits to the doctor, up to the maximum value, which is for workers with more than ten years in the job with average information on the risks, who visit the doctor in $63.24 \%$ of the cases. Furthermore, we see more visits to the doctor as the information worsens in every range of length of time in the job. There is an average difference in visits to the doctor of over ten percentage points for each time-on-the-job range and as a function of the information received, which gives an idea of the importance of the aforesaid information in preventing risks and doctor visits for work-related reasons.

Table 12: Probability of visiting the doctor due to work-related health problems based on time in the job and information received.


Source: Compiled by authors from BN model.
Graph 1: Variation in the probability of visiting the doctor due to work-related health problems based on time in the job and information received.
![img-1.jpeg](img-1.jpeg)

The process of analyzing the area under the ROC curve yields the values shown in Table 13. The eleven values given are for the AUCs associated with the ten 10 -fold subsamples, the AUC for the union of the ten predictions made in the 10 -folds and the AUC obtained under optimal conditions. Value 11 can be considered as approaching the average of the ten previous values.

Table 13: AUC values for the network analyzed


Source: Compiled by authors.

As we can see, the "average" value of 0.756 may be considered acceptable, based on the analysis criteria for the methodology used to measure the AUC.

# 5 CONCLUSIONS 

The first conclusion from the study is the similarity between the results of the NWCS conducted in Spain and the 6th European Survey on Working Conditions. For example, there is one question common to both on how the worker is informed about on-the-job risks. In the 6th European Survey, $89 \%$ of workers stated that they were well or very well informed (Eurofound, 2016), in the 5th European Survey it was 90\% (Eurofound, 2012), and in the 7th NWCS in Spain in 2011, it was $86 \%$ (Almodóvar et al., 2011). These data reveal two findings: the first is that the performance in Spain is similar to that of European countries, and the second is that a majority of workers affirm that they are well informed about on-the-job risks.

The second finding of notable interest is the difference in behaviors shown by the four economic sectors in terms of the probability of an accident, ranging from a minimum of $5.54 \%$ in agriculture to a maximum of $12.03 \%$ in industry.

Acting on information pertaining to the risks has a significant influence on the probability of an accident occurring. In general, the better the information the lower the probability, though this probability does not always drop with respect to the initial situation when maximum information is provided. It is however always true that as the information worsens, the accident probability rises, even doubling.

When workers' visits to the doctors are considered, we see that those who visited a doctor as the result of pain produced or aggravated by work are more likely to have an accident; what is more, this probability increases the less informed they are.

Training received in the two previous years also affects accident rates, though to a lesser extent than the long-term information received. Long-term information on workplace risks, provided as part of a culture of prevention, has a greater effect and lowers accident rates more than specific training activities in the two pre-

vious years. In addition, we have noticed that more on-the-job training is received in jobs that are more dangerous or more likely to result in an accident.

Two other variables considered, length of time in the job and contract type, which were assumed to have a greater influence, were not very significant in the results. In the study, neither length of time in the job correlated strongly with the accident rate, nor experience, which had a very insignificant effect on the accident rate. The same point was noted by (Zhou et al., 2008) in their study, which showed that on-the-job experience by itself was not related to safety behavior, as a result of which Zhou proposed joint strategies. However, length of time in the job would have to be taken into account, as suggested by Vidal (Vidal-Gomel, 2017), when proposing worker training that is not based solely on regulations and procedures, but that takes into account the accumulated experience of the worker over the years.

Specifically, in construction, the difference between having bad or good information means that the probability of having an accident can fall from $15.38 \%$ to $8.1 \%$, thus emphasizing the importance of this variable.

# 6 LIMITATIONS AND FUTURE CHALLENGES 

One limitation of the study is the little information available on the training received by workers. Given the importance of this training, particularly in the construction sector, more detailed information is needed on training types, whether general or specific, the provider, and so on. In future studies we plan to ascertain which specific training and information activities have the greatest influence on accident rates. We will also consider other variables, such as the role of new technologies in training and information.

## 7 ACKNOWLEDGMENTS

We would like to thank the staff at the National Institute for Workplace Safety and Hygiene (Ministry of Labor and Social Security) for their cooperation in this study, and in particular for allowing us to use the data compiled as part of the 7th NWCS, which made it possible for us to complete this work, and to the research project awarded under reference $53 / 09 \mathrm{PH} / \mathrm{cm}$ (UBU/FACTOR), and entitled "Influence of organization in the workplace on health and safety outcomes. Case studies".
