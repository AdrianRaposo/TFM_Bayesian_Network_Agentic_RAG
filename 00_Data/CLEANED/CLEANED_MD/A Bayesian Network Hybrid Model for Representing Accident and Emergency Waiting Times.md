![img-0.jpeg](img-0.jpeg)

# A Bayesian network hybrid model for representing accident and emergency waiting times

Marshall, A. H., & Burns, L. (2007). A Bayesian network hybrid model for representing accident and emergency waiting times. In *Proceedings of the Twentieth IEEE International Symposium on Computer-Based Medical Systems, CBMS'07* (Annual IEEE Symposium on Computer-Based Medical Systems: Proceedings). Institute of Electrical and Electronics Engineers Inc.. https://doi.org/10.1109/CBMS.2007.1

## Published in:

Proceedings of the Twentieth IEEE International Symposium on Computer-Based Medical Systems, CBMS'07

## Document Version:

Peer reviewed version

## Queen's University Belfast - Research Portal:

Link to publication record in Queen's University Belfast Research Portal

## Publisher rights

Copyright 2007 IEEE.

This work is made available online in accordance with the publisher's policies. Please refer to any applicable terms of use of the publisher.

## General rights

Copyright for the publications made accessible via the Queen's University Belfast Research Portal is retained by the author(s) and/or other copyright owners and it is a condition of accessing these publications that users recognise and abide by the legal requirements associated with these rights.

## Take down policy

The Research Portal is Queen's institutional repository that provides access to Queen's research output. Every effort has been made to ensure that content in the Research Portal does not infringe any person's rights, or applicable UK laws. If you discover content in the Research Portal that you believe breaches copyright or violates any law, please contact openaccess@qub.ac.uk.

## Open Access

This research has been made openly available by Queen's academics and its Open Research team. We would love to hear how access to this research benefits you. Share your feedback with us: http://go.qub.ac.uk/oa-feedback

# A Bayesian Network Hybrid Model for Representing Accident and Emergency Waiting Times 

Adele H. Marshall, Member, IEEE


#### Abstract

The paper introduces a new modeling approach that represents the waiting times in an Accident and Emergency (A\&E) Department in a UK based National Health Service (NHS) hospital. The technique uses Bayesian networks to capture the heterogeneity of arriving patients by representing how patient covariates interact to influence their waiting times in the department. Such waiting times have been reviewed by the NHS as a means of investigating the efficiency of A\&E departments (Emergency Rooms) and how they operate. As a result, activity targets are now established based on the patient total waiting times with much emphasis on trolley waits.


Index Terms-Bayes Procedures, Medical Services, Modeling, Statistics.

## I. INTRODUCTION

The UK National Health Service (NHS) has received a large amount of media attention concerning their provision of care to the general public. One aspect, under particular scrutiny is the queues of waiting patients at Accident \& Emergency (A\&E) departments, the equivalent of Emergency Rooms (ERs) in USA. Upon receipt of their treatment, A\&E patients either leave hospital and return home or they become an emergency admission requiring further medical care or attention during a stay in hospital. The numbers of emergency admissions have been reported to rise rapidly each year prompting the NHS to review how A\&E departments operate [1]. The review clearly focuses on targets for A\&E activity. Monitoring activity has become a necessity by health care providers heralded by the introduction of efficiency measures, set in place to assist the assessment of these targets. For example issues such as the patient total waiting time in A\&E have become measures of efficiency for hospital managers with much emphasis currently concentrated on emergency admissions trolley waiting times. These are quite often referred to by both the media and health care managers as the 'trolley

[^0]waits' as they are the times that the emergency admission patients spend waiting in a hospital trolley (gurney) from the clinician's decision to admit (DTA) until they are allocated a hospital bed in a hospital ward [2]. In particular, Northern Ireland has two current targets concerning trolley waits.

1) $75 \%$ of patients should be admitted to a ward within 2 hours of DTA.
2) No patient should have a trolley wait greater than 12 hours.
It is this kind of emphasis on targets that is motivating health care providers to turn to health care modeling as a means of representing hospital activity and efficiency in the wards, not just for A\&E but all aspects of patient care.

Previous research has been carried out on the statistical modeling of length of stay, the total length of time patients spend in hospital [3]. This is usually measured as the number of days in hospital starting from the moment the patient arrives at the hospital ward and is allocated a bed. Quite often it does not include the time taken to get from A\&E until the allocation of a bed or any component of the waiting times experienced along the way. An alternative representation of length of stay is to consider the time measured from arrival to A\&E until departure from hospital. In doing so, the time is measured as one total amount unlike the research discussed in this paper which will investigate one important component of that length of stay time; the trolley waiting time. It is hoped that the consideration of waiting times as a separate component will lead to further accuracy in the models.

Reviews of health care modeling (e.g. [3]) have highlighted a trend towards the employment of a portfolio of methods and techniques to include recent developments in scientific fields such as artificial intelligence, data mining and information technology. Consider the framework described by Harper [4] where there are various components or stages of analyses combining a preliminary statistical analysis with a further data investigation using methods such as classification and regression tree analysis (CART) and modeling techniques on patient length of stay. This is complemented by a final stage of modeling using simulation techniques. In this case, various data mining, statistical and operational research (OR) methods come together to provide operational modeling for hospital resources. Another example is Walczak et al.'s [5] use of neural networks to facilitate the modeling and prediction of


[^0]:    Manuscript received November 30, 2007. This work was supported in part by the Engineering and Physical Science Research Council, EPSRC Grant GR/S26910/01.
    A. H. Marshall is with the Centre for Statistical Sciences and Operational Research, CenSSOR, Queen's University, Belfast, BT7 1NN, UK. (e-mail: a.h.marshall@qub.ac.uk).

resource utilization associated with patient length of stay in hospital. Such research implies that the future of modeling patient activity in health care systems, is based on the successes of current models and the evolution of hybrid approaches formed from techniques within the data mining, statistics, OR and artificial intelligence domains.

This paper presents a hybrid modeling technique that uses an approach comprising of a Bayesian network and survival distribution. The motivation behind the research was the desire to create a model that could adequately represent the skewed nature of the survival distribution, the waiting time of patients in A\&E, while also capturing the interconnected factors that influence this skewed survival. As is the nature of many health service research studies, it is difficult to find one specific method that can easily deal with the application in mind [3]. Bayesian Network theory [6] is a well advanced field of research whose models can clearly capture inter-relationships between variables, having been applied to many areas of research not only within the medical domain. However, there has been little development associated with the inclusion of continuous variables that are skewed in nature. Alternatively, a key feature of the advanced statistical methods of Survival Analysis is their suitability and ease in which they represent this skewed continuous data though the representation of interrelated variables influencing the skewed survival times can be limited. It is with this in mind that a hybrid methodology was considered and developed using these two modeling mechanisms.

The resulting Bayesian network hybrid model is capable of capturing the heterogeneity of arriving patients by representing how patient covariates interact to influence their skewed survival distribution of hospital trolley waiting times.

## II. BAYESIAN NETWORK HYBRID MODEL

The Bayesian network hybrid model consists of two components as illustrated in Fig. 1. The first component utilizes a Bayesian network [6], a graphical structures defining various events, the dependencies between these events and the conditional probabilities involved in those dependencies. This can be used to represent the inter-relationships between categorical variables. The graphical structure of the resulting Bayesian network provides a basis on which to condition the second component of the model, the survival distribution. Survival analysis is a statistical methodology used to represent the length of time it takes a certain event to occur such as the observed time it takes an individual (the experimental unit) to experience the event [7]. The resulting times for a group of observations may be represented by a probability density function and generalized to form a survival distribution. This allows the probabilities of surviving up until certain time points to be calculated. In the case of the A\&E patients, the survival distribution represents the continuous time variable in the model, the time period in which the patient waits. There are many forms of statistical distribution that can model survival such as the exponential, gamma, Weibull and lognormal distributions.

Previous research has led to the development of the C-Ph model [8] which specifically models the survival distribution component using a specialist type of distribution known as the Coxian phase-type distribution [9]. Rather than restrict further modeling to that of the Coxian phase-type distribution, current research has expanded the C-Ph model to form the Bayesian network hybrid model incorporating any kind of probability distribution as its second component.
![img-1.jpeg](img-1.jpeg)

The general form of the Bayesian network hybrid model is illustrated in Fig. 1 where the first component is a Bayesian network (BN) whose structure ends with a variable referred to

as the outcome node. The existence of such an outcome node in the BN, eases the learning of the model separating it into two components. The first BN component can then be learnt independently from the statistical survival model.

## III. LEARNING THE BAYESIAN NETWORK HYBRID MODEL

The PowerConstructor [12], software package is designed to learn Bayesian networks from a data set. Using a three phase construction algorithm the software calculates the mutual information that a potential edge would contribute and determines whether it should be added to the network.

PowerConstructor takes advantage of Chow and Lui's algorithm [13] which uses mutual information for learning causal relationships and enhances the method with the addition of further procedures to form a three stage process of structure learning from the data. The first phase (drafting) takes advantage of Chow and Liu's algorithm for identifying strong dependencies between variables by calculating the value of mutual information gained. The second stage (thickening) performs conditional independence (CI) tests on pairs of nodes that were not included in the first stage. Stage 3 (thinning) then performs further CI tests to ensure that all edges that have been added are necessary. This three-stage approach manages to keep to one CI test per decision on an edge throughout each stage and as such has a favourable time complexity of $\mathrm{O}\left(\mathrm{N}^{2}\right)$ unlike many of its competitors which have exponential complexity.

The resulting Bayesian network will contain a set of discrete nodes that comprise the variables from the data set and a set of directed edges between these nodes. The edges represent the interrelationship or direct influence that the variables have on each other. This is quantified by conditional probability tables for each interaction between nodes.

The continuous survival time in the BN hybrid model can be modeled using a statistical software package such as SAS ([14], [15]) or mathematical software such as MATLAB [16].

## IV. APPLICATION OF THE BAYESIAN NETWORK HYBRID MODEL TO A\&E DATA

The Bayesian network hybrid model is applied using data taken from the NIRAES (Northern Ireland Regional Accident and Emergency System) database. It is based on all new arrivals at a busy A\&E department (Emergency Room), over a 12 month period between 2005/06. In total, the data set contains records for 52,928 new patients presenting at the A\&E department.

Patient information, recorded on entry to the A\&E department, includes patient age, sex, arrival method, departure method, incident type, assigned priority code and an indicator variable on whether a patient should be admitted to hospital, that is, whether a decision to admit (DTA) was made or not (No DTA).

On arrival to the A\&E department, a patient may wait for a period of time before seeing a triage nurse for initial assessment. After this they may 'queue' for a further time period before they are given a further examination by a doctor.

The next stage is the DTA, the decision from the doctor on whether the patient should be admitted to a hospital bed for additional treatment and care. If a patient is admitted to hospital, they may experience a 'trolley wait' in the A\&E department where they wait for a further period of time before proceeding to a bed in one of the hospital's wards.

Also recorded were dates/times of various A\&E activities such as arrival to A\&E, assessment by nurse, examination by doctor, time of departure and, if applicable, time of DTA and time to ward. This facilitated the calculation of an associated trolley waiting time for all DTA patients.

Twenty-four percent of those patients arriving to the A\&E department received the clinician's decision to be admitted to a hospital ward and are thus classified as a DTA patient, the remainder are referred to as No DTA as these are the patients who are not admitted but instead return home after consultation with the doctor. The total time patients spend in A\&E differs substantially depending on whether the patient has a DTA or not. From inspection of Fig. 2, it is apparent that the majority of NO DTA patients leave the A\&E department reasonably quickly as the graph for NO DTA peaks sharply with a higher proportion of patients having a shorter waiting time. The DTA patients have a longer wait in A\&E with fewer leaving early in the skewed distribution which tails off extensively to the right.
![img-2.jpeg](img-2.jpeg)

Fig. 2. Distributions of total time in A\&E for DTA and No DTA patients.

This is also evident when examining the descriptive statistics of the two distributions. The mean time in A\&E for the DTA patients is 372 (median of 237) minutes compared to

No DTA patients who, as expected, have a much shorter mean time in A\&E of 129 (median of 100) minutes.

The difference in the two distributions may be due to trolley waits experienced by the DTA patients. At the time of DTA, there may not have been any hospital beds available so instead patients may wait in a trolley. Their time waiting in the trolley would be included as part of the patient's total time in A\&E possibly explaining why the DTA patients in general have a longer total time distribution. This distinction between the groups of patient provide support for having an outcome node in the model where it is obvious that these two types of patient follow distinctly different waiting time distributions in A\&E.

The BN component of the model will therefore comprise the patient variables, how they inter-relate and influence the final node of the network. The last node in the network can be viewed as a kind of outcome variable such as the DTA outcome variable in this example. As such this will act as a connecting node between the rest of the BN component and the survival distribution component (Fig. 1).

As previously stated the NHS targets are focused on trolley waiting times being less than 2 hours with the aim of having no wait to exceed 12 hours. In the case of the current study, $64 \%$ of patients had trolley waiting times of less than 2 hours (target $75 \%$ ), while approximately $9 \%$ of patients were waiting over 12 hours (target $0 \%$ ). Based on this data, the hospital does not meet the required NHS targets. It is therefore necessary to accurately represent the patient trolley waiting time so that further assessment of the hospital activity can be made and actions taken to improve the situation. The trolley waiting times were therefore investigated and used as the second component of this particular model. By representing the data in the Bayesian network hybrid model, it is hoped that the BN will potentially be able to predict those patients who obtain DTA, that is, those who require medical attention and admission to a hospital ward. Once identified, the duration of trolley waits may then be forecasted for the new DTA patients arriving into the A\&E departments.

## A. Survival Distributions

The survival distribution represents the final patient trolley waiting time as the second component of the model. The trolley waits have a maximum recorded value of 3255 minutes (approximately 2.25 days) with a median of 60 minutes. With such differences in the mean and median values, it is evident that the data will not be normally distributed and therefore cannot lend itself to certain types of BN models such as the Conditional Gaussian distribution [10]. Fig. 3 illustrates the skewed nature of the data, typical of all survival data, therefore deeming it suitable for modeling using survival analysis.

Survival analysis was carried out on the trolley waiting times. Several distributions including the exponential, gamma, Weibull and lognormal were fitted to the data using the maximum likelihood technique implemented by the Matlab software package [11]. Comparison of the resulting log likelihood values indicated which distribution best fitted the
data. In this particular example the trolley waiting times were found to be most suitably modeled using a lognormal distribution, with parameters; mean $=4.18$ and standard deviation $=1.67$ and probability density function as follows:

$$
f(t)=\frac{1}{1.67 t \sqrt{2 \pi}} \exp \left(\frac{-(\log t-4.18)^{2}}{5.57}\right)
$$

![img-3.jpeg](img-3.jpeg)

Fig. 3. Distribution of trolley waiting times.
Fig. 3 illustrates the fit of the distribution compared with the real data. The curve of the fitted distribution, as in (1), captures the shape of the data to a reasonable accuracy. Although it doesn't manage to depict the large peak at the beginning of the distribution, the log likelihood values indicate that it provides the best representation out of all of the alternative statistical distributions. The peak at the beginning is owing to the large frequency of patients for which zero waiting was recorded. Such a situation would occur if patients were immediately moved to the hospital ward as soon as DTA was declared by the doctor. It is possible that these patients may have been the more urgent cases, those with more severe incidents or those patients with the highest priority code.
An alternative reason may be if patients were referred by their GP who had arranged a bed to be available for them on arrival to the A\&E department. Such reasoning will follow when considering the final model.

## B. Bayesian Network Hybrid Model

The Bayesian network hybrid model brings together the survival distributions with other characteristics that could potentially improve the predictive power of the model. In this particular A\&E example, the outcome node is the one characteristic that has been chosen to be influential on patient trolley wait.

![img-4.jpeg](img-4.jpeg)

Fig. 4. Bayesian network hybrid model for A\&E patients.
The structure of the BN component for the A\&E patient variables was learned using PowerConstructor with the DTA variable as the final outcome node. The resulting network of inter-related variables is illustrated as the first component in Fig. 4. A node in the network represents a variable and a directed arc between nodes represents a relationship or direct influence of one variable on another.

Fig. 4 illustrates the fitted Bayesian network hybrid model for patient trolley waiting times including the first component in the model as the network of patient characteristics and how they inter-relate to determine the patient outcome of admission to hospital. The second component then captures this waiting time for patients placed in trolleys awaiting admission to a specific hospital ward.

The diagrammatic representation highlights some interesting relationships in the data for example the age group of a patient has an influence on the type of incident, arrival mode and outcome of the patient. This was also evident from preliminary data analysis which highlighted teenagers as the age group category with the smallest ( $6 \%$ ) proportion of patients being admitted to hospital, while 60 year olds and over make up $54 \%$ of all DTA patients, in particular, the patients aged 80 to 89 years consisted of the single largest group of DTA patients (19\%). This is to be expected as the older patients would be considered more dependent on others, potentially having other medical complaints which could lead to more complications and an overall more likely decision to be admitted to hospital.

In addition to age group, the variables incident type, arrival mode and priority level are considered to have a direct influence on outcome. Incident type refers to the kind of incident in which the patient was involved such as 'road traffic accident', 'non-trauma case' or 'home accident' case.

A high proportion of DTA patients were admitted as a nontrauma case whereas those patients with No DTA tended to be
in A\&E due to non-trauma, home accident or due to an incident that happened in a public place.

Arrival mode refers to the form of transport taken to get to the Accident and Emergency department for instance 'ambulance arrival', 'private transport' or 'public transport' are possible. The DTA patients, as is expected were generally arriving at the A\&E department via ambulance or private transport. This seems reasonable as you would expect that those patients that are admitted to hospital for further care to be the more severe cases and thus the more urgent so more likely to be the ambulance cases or private transport. This may also explain the earlier observation that there was a peak in the trolley wait distribution at time 0 minutes of patients who were DTA. Certainly those patients who were DTA appear to have an arrival mode that implies that they were the more urgent cases. This may be explained further by the BN edge between priority code and outcome.

Priority level is a variable assigned to the patient, by hospital staff, on arrival to the Accident and Emergency department. There are five different levels starting with code red or level 1 which is the most severe where the patient requires immediate resuscitation, level 2 refers to patients considered to be very urgent right through to the least severe level 5 classed as non-urgent. The patients who receive a decision to be admitted (DTA) mainly comprised of the urgent cases (coded as level 3) while those patients that have No DTA tend to be less severe cases, coded as level 4 referred to as standard. Again this explains the earlier observation in the peaked trolley waiting time distribution due to the urgent DTA patients getting a hospital bed immediately.

Table 1 provides an example of one of the conditional probability tables used in the BN. It represents the probability of DTA and No DTA according to the patient's arrival mode and priority code. The first line of each row is the DTA probabilities, and the second line of each row the No DTA probabilities. For example the probability that a patient is

admitted to hospital (DTA) given they have priority code 1 (immediate resuscitation) and arrival mode ambulance is high at 0.84 . On the other hand the probability of a patient being admitted to hospital given they have priority code 5 (nonurgent) and arrival mode ambulance is 0.17 , much lower.

TABLE 1: Conditional Probability of DTA and No DTA Given Patient Priority Code (PC) and Arrival Mode


The Bayesian network hybrid model represents the characteristics of the patients on arrival to the A\&E department and predicts the patient outcome through conditional probability tables, in this case whether or not the clinician or medical doctor admits the patient to hospital for further care and medical attention. Those patients who are 'decision to admit', are modeled using the second component of the Bayesian network hybrid model which uses the statistical distribution, the lognormal detailed in equation (1) to predict the patient trolley waiting time.

The BN model was evaluated using a separate test set of $30 \%$ of the original data and found that the use of arrival mode and priority code successfully matches $81.82 \%$ of decisions. Once this prediction has been made the lognormal distribution, previously found to be a good representation of the survival data, is used to estimate the expected trolley waiting time.

In addition to the general predictive power of the model, it is worth noting that its transparent graphical nature can be of benefit too. This allows the user, for instance the health care manager to see how the patient characteristics are inter-related and possibly suggest actions that may be taken to reduce patient waiting times. Previous discussion listed hospital performance targets for trolley waits which ideally should be less than the specified 2 hours and certainly no more than 12 hours. A preliminary investigation of the data in this study reveals that $27 \%$ of patients waited between 2 and 12 hours with no obvious indication or reason why and a further $9 \%$ waited beyond 12 hours. By utilizing the BN hybrid model, it is possible to identify four factors; priority code, admission mode, age group and incident type, that were all shown to be influencing factors on DTA. Although priority code and admission mode proved good indicators of DTA, the age group and incident type of the patient, appear to provide more explanation of long trolley waits. In particular, the shorter
trolley wait patients tend to comprise more of the elderly patients. It is possible that elderly patients are treated with more caution as they generally have more complications and additional health problems that could hinder their recovery. However it would be worth investigating this further to see whether elderly patients have more complications so are prioritized or whether they have a different care program that could potentially be applied to other younger patients to reduce their trolley wait.

Other modeling approaches that may be considered alternatives to that presented in this paper include Cox proportional hazards models [17], neural networks [18] and alternative hybrid BNs such as Conditional Gaussian models and Conditional Gaussian regression models [19]. However, all of these approaches have at least one drawback which hinders the representation of the data. The Cox proportional hazard's model assumes proportional hazard functions for which the data does not. Neural networks do produce a successful network of variables however its use is limited due to the black-box nature of the method providing little understanding of how the model works. This has been a criticism of neural networks since their development. As such there has been further research to develop hybrid models involving neural networks and symbolic approaches. One of the main purposes of developing the BN hybrid model is to provide understanding of how the variables inter-relate and are associated with the continuous time variable. The BN structure provides a graphical illustration that is useful for explaining these relationships and conditional probabilities to health care specialists. The use of a neural network for this purpose would therefore be pointless.

Compared to traditional BNs, the alternative hybrid BNs provide a better representation of the model since they do not require the discretization of the continuous variables where information may be lost. Conditional Gaussian (CG) networks are one such form of BN that can model both discrete and continuous variable, however there is a restriction on the continuous variables that they must be normally distributed, conditional on their parents [10]. This is therefore unsuitable for the A\&E data set which comprises mainly discrete variables and one highly skewed non Gaussian continuous variable. The Conditional Gaussian regression model allows the use of discrete variables but is still deemed unsuitable for the A\&E data as it again restricts the continuous variable to be Gaussian distributed.

## V. CONCLUSION AND FURTHER WORK

This paper considers the Bayesian network hybrid model to represent a set of covariates that influence a survival distribution where the inter-related variables impact upon an outcome variable which has an associated skewed survival. The skewed survival distributions are represented using any number of possible probability distribution. The example in the paper serves as a means of demonstrating the methodology where patient information, known on arrival to an Accident

and Emergency (A\&E) department, the equivalent of Emergency Rooms (ERs) in USA, is used to predict the future outcome of the patients and their associated trolley waiting time.

The model may be used to identify those patients at risk of experiencing a long trolley wait so that something can be arranged to alleviate this problem and prevent the situation occurring. Alternatively, the model has the potential of acting as a management support tool where 'what if?' scenarios can be considered and the consequences of them impacting upon the system modeled in advance to highlight benefits, potential problems and further requirements that will improve and monitor the efficiency of the hospital system. Ideally, the model could be extended to examine bed allocations in the hospital wards with the introduction of additional variables at the BN level. The resulting model could be represented in a simulation modeling environment where the flow of patients though the system could be assessed at a glance.

Another aspect is to consider the entire process from arrival at the A\&E department right though to the point of when the patient leaves the hospital either with or without undergoing a hospital stay. In fact, targets are currently being developed for the UK NHS with this is mind. The Bayesian network hybrid model, introduced in this paper, would be an ideal representation for such data. As previously discussed in the preliminary investigation of the patient data, the total waiting time in the Accident and Emergency department, for the 'decision to admit' appears to be significantly longer than that of the 'no decision to admit' patients. As with the survival distribution for trolley waits, the nature of the total time in the A\&E department for both DTA and No DTA patients is positively skewed making its analysis amenable for the methods of survival analysis and its incorporation into the Bayesian network hybrid model.

Furthermore, there is potential to obtain costing data for such a service that could in turn be incorporated in the new model. Such a development would fit with previous research [20] and allow for the assessment of predicted associated costs thus facilitating future budget planning.

## ACKNOWLEDGMENT

The author would like to thank the staff of the Northern Ireland Accident and Emergency department who collected and provided the data; Louise Burns and Adele Graham for the cleaning and validation of the data and Doctors Ann Wilson and William Moore for their contribution and feedback.
