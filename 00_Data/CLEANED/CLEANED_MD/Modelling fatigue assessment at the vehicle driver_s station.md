# Modelling fatigue assessment at the vehicle driver's station 

Piotr Maksym ${ }^{1, *}$, and Halina Pawlak ${ }^{1}$<br>${ }^{1}$ University of Life Sciences in Lublin, Faculty of Production Engineering, Department of Ergonomics, 20-612 Lublin, Gęboka 28. Poland


#### Abstract

The article presents the principles of fatigue assessment modeling in a driver's station using Bayesian networks. One of the causes of road collisions and accidents is fatigue. The factors determining fatigue are age of driver, psychophysical and health condition, time and length of the route being taken. At present, there is no clear criteria for assessing fatigue among professional drivers, so the objective of assessment is to attempt to design and construct a fatigue assessment model using Bayesian network technology.


## 1 Introduction

On Polish roads there are many collisions and road accidents every day. The main culprits are drivers of both passenger vehicles and trucks. They carry dangerous consequences. They can cause severe injury, irreversible changes in the human body, and lead to death. Trucks are the most common means of transporting different types of loads, and due to their size in the crash, they can cause more damage than passenger cars.

The profession of a driver, like any other profession, involves a number of dangerous situations that can take place every day. The biggest threat is traffic accidents. Their cause may be a bad technical condition of the vehicle, bad weather conditions or driver fatigue.

The phenomenon that naturally accompanies every job is fatigue. It is a warning signal to the human body from excessive, unfavorable, and in special cases - even health-threatening effort. The natural reaction to feeling fatigued is rest, which allows for regeneration and restore of the body [1].

It is the fatigue of the driver that is influenced by perception, decision-making and motor skills. Driving a car requires careful attention from the driver and a focus on external stimuli. In addition, the organization of the work day, including the length of the route taken, sleep deprivation, breaks, and inappropriate and uncomfortable position while driving and monotony [24]. As a result, driver fatigue is a serious safety problem. Such diverse causes are often difficult to identify immediately.

The aim of this paper is to develop a fatigue assessment model at the driver's station using Bayesian technology, with the ability to indicate the accuracy of the probability distribution, which factor has the greatest influence on fatigue.

## 2 Material and Methods

The process of modelling the fatigue assessment of drivers is related to obtaining a set of empirical data that is used to build and test the Bayesian network. Therefore, a survey was conducted. The author's questionnaire, was based on the Japanese questionnaire of subjective fatigue symptoms, developed by the Research Committee on Industrial Fatigue of Japan Society for Occupational Health [5]. The answers have been derived from subjective feelings of driver fatigue regarding factors affecting fatigue.

The questionnaire included twenty questions, such as participation in traffic collisions and accidents, fatigue symptoms, the length and complexity of the route being taken, time pressure, shift work, exposure to external factors (noise, temperature). The survey was supplemented by expert opinion.

The first step in designing a formal knowledge representation system is to build a conceptual model of the subject area. This is related to the ordering and structuring of acquired knowledge. Non-formal conceptualization is the representation of knowledge in a natural language, containing many ambiguities, best interpreted by the expert. Methodology of designing a formal knowledge representation system assumes ease of transition from the description of the problem in natural language to representation in formal and executable language [6]. The second step is to identify ways to move from the informal conceptualization of the problem of driver's fatigue assessment to the computer model. This approach involves choosing an appropriate system that will be sufficiently expressive to precisely describe the subject matter as fatigue. An additional fact to be considered is the uncertainty with regard to the ratings received. The sources of this uncertainty are both incomplete knowledge about the object being evaluated and the lack of evaluation criteria.

As a measure of uncertainty adopted probability. Attributes of the assessed object and the evaluation of driver fatigue are treated as variables for which values are known to an accuracy of the probability distribution. One of the systems of knowledge representation that fulfills the assumption is a Bayesian-based system.

Bayesian network technology allows expression of cause - effect relationships that exist permanently or temporally, described as cumulative probability distribution. The computational scheme is based on the Bayesian formula and the conditional independence statement, which allows for the cumulative probability distribution as a factorization of conditional probability distributions [7].

The conditional probability of event A provided that B has occurred, denoted $P(A \mid B)$, we call the quotient of the probability of the product $A \cap B$ and probability of event B:

$$
P(A \mid B)=\frac{P(A \cap B)}{P(B)}, P(B) \neq 0
$$

The Bayesian formula is a conditional probability calculation scheme:

$$
P(B \mid A)=\frac{P(A \mid B) P(B)}{P(A)}
$$

The Bayesian network is an acyclic directed graph, visualized using an alphabet containing two symbols:

- node
- directed arc

The nodes represent random variables (discrete or pseudo continuous) and arcs connecting the nodes - the relationship between these variables (Fig. 1.).
![img-0.jpeg](img-0.jpeg)

Fig. 1. Example of bayesian network build in BayesiaLab (own work).

Each node is associated with a conditional probability table. Each variable has a strictly defined type, and value domain. Based on such data, a learning process can be performed to determine probability distributions for all network nodes [8-10].

The use of the Bayesian network consists in launching an automatic inference mechanism to determine the probability distribution of variables [11], that applies to:

- prediction - knownig the reason we ask about the consequences,
- explanation - knownig the consequences we ask about the reason.


## 3 Results

The survey was conducted among fifty professional drivers. Among the respondents were drivers aged between 20 and 46 , with a secondary education of $70 \%$. $92 \%$ of the respondents answered "Yes" to the question of whether they followed the correct work day and designated breaks. The most common answer to the question about symptoms of fatigue was: back pain, drowsiness, desire to lie down, and other. As part of the "other" answer, respondents were able to list their subjective feelings, for example: variability and a high amount of information, constant attention (Fig. 2.).
![img-1.jpeg](img-1.jpeg)

Fig. 2. Symptoms of fatigue according to respondents answers (own work).

According to experts, these statements from drivers, have suggested an increase in mental load, which has been one of the attributes of the Bayesian networks topology. The attribute "fatigue" of drivers is evaluated on the basis of "workload", "stress", "organization of work", "work experience" as a professional driver and "sex" of the driver (Table 1, Fig. 3.).

The obtained results will be subject to an sensitivity analysis, that can be described as a method which define how "sensitive" mathematic model really is when the parameters and the overall structure of the model experience changes.

![img-2.jpeg](img-2.jpeg)

Fig. 3. The network structure of attributes assessments „fatigue" (own work).
Sensitivity analysis allows researcher to find the accuracy needed for an accurate and functional model. If the analysis shows signs of insensitivity of parameter change, then it is probable rough estimation might serve a better information than an actual value. The analysis could points which parameter values are appropriate to use in the model $[12,13]$.

Table 1. Set of attributes values - "fatigue".


## 4 Conclusions

Taking care of the traffic safety is associated with the awareness of drivers on the phenomenon of fatigue and its effects. At present there is no uniform criteria for fatigue assessment of professional drivers, so an attempt was made to build a fatigue assessment model using Bayesian technology.

The next step of development of the model will be measure of its effectiveness by the sensitive analysis method.

Bayesian networks allow for rapid conversion of expert knowledge and empirical data, expressed verbally (written in natural language), into computer models. The quality of models depends on the conceptualization of the modeled domain. According to the assumptions Bayesian networks should help to quickly assess the degree of fatigue of drivers and explain the reasons for the fatigue.
