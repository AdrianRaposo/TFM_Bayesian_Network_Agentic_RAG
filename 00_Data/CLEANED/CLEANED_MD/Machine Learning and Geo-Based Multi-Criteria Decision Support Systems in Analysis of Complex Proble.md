# Article 

## Machine Learning and Geo-Based Multi-Criteria Decision Support Systems in Analysis of Complex Problems

Behrouz Pirouz ${ }^{1, * *}$, Aldo Pedro Ferrante ${ }^{2}$, Behzad Pirouz ${ }^{3 *}$ and Patrizia Piro ${ }^{2}$

check for updates

Citation: Pirouz, B.; Ferrante, A.P.; Pirouz, B.; Piro, P. Machine Learning and Geo-Based Multi-Criteria Decision Support Systems in Analysis of Complex Problems. ISPRS Int. J. Geo-Inf. 2021, 10, 424. https:// doi.org/10.3390/ijgi10060424

Academic Editor: Wolfgang Kainz

Received: 28 April 2021
Accepted: 18 June 2021
Published: 21 June 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Department of Mechanical, Energy and Management Engineering, University of Calabria, 87036 Rende, Italy
2 Department of Civil Engineering, University of Calabria, 87036 Rende, Italy; aldopedro.ferrante@unical.it (A.P.F.); patrizia.piro@unical.it (P.P.)
3 Department of Computer Engineering, Modelling, Electronics and Systems Engineering, University of Calabria, 87036 Rende, Italy; behzad.pirouz@dimes.unical.it

* Correspondence: behrouz.pirouz@unical.it; Tel.: +39-0984-496542

Abstract: Many complex problems require a multi-criteria decision, such as the COVID-19 pandemic that affected nearly all activities in the world. In this regard, this study aims to develop a multicriteria decision support system considering the sustainability, feasibility, and success rate of possible approaches. Therefore, two models have been developed: Geo-AHP (applying geo-based data) and BN-Geo-AHP using probabilistic techniques (Bayesian network). The ranking method of Geo-APH is generalized, and the equations are provided in a way that adding new elements and variables would be possible by experts. Then, to improve the ranking, the application of the probabilistic technique of a Bayesian network and the role of machine learning for database and weight of each parameter are explained, and the model of BN-Geo-APH has been developed. In the next step, to show the application of the developed Geo-AHP and BN-Geo-AHP models, we selected the new pandemic of COVID-19 that affected nearly all activities, and we used both models for analysis. For this purpose, we first analyzed the available data about COVID-19 and previous studies about similar virus infections, and then we ranked the main approaches and alternatives in confronting the pandemic of COVID-19. The analysis of approaches with the selected alternatives shows the first ranked approach is massive vaccination and the second ranked is massive swabs or other tests. The third is the use of medical masks and gloves, and the last ranked is the lockdown, mostly due to its major negative impact on the economy and individuals.

Keywords: machine learning; AHP; geo-based data; multi-criteria; COVID-19; environment; economy; sustainability

## 1. Introduction

Analysis of complex real-world problems such as multi-criteria decision making and selecting the best choice from numerous alternatives requires different skills and data analysis in different forms [1,2]. The decisions made about the COVID-19 pandemic are among the most complex problems, and resolving the issues require not only experts' opinions but also dynamic analysis of different databanks. COVID-19 (SARS-CoV-2) was characterized as a pandemic on 11 March 2020, affecting nearly all activities, such as political, global economic, and socio-cultural [3]. Health organizations' main strategies were lockdowns, mandatory or self-quarantine, social distancing, travel bans, use of facemasks and gloves, swab tests, and vaccination [4]. There is evidence of the spread of COVID-19 by symptomatic and asymptomatic persons [5].

The use of medical facemasks is recommended to prevent the transmission of respiratory diseases [6]. Even homemade facemasks are recommended for protection since they can reduce droplets' spread [7-9]. According to the analysis, medical facemasks can be considered as a complementary means of source control and not a replacement method for core preventive measures, such as lockdown, physical distancing, smart working, etc. Additionally, wearing

facemasks may create false security for individuals [10]. Reports show that the production and ordering of facemasks by countries has increased to a million pieces per day [11].

The other method to confront the pandemic is by detecting positive cases. Thus, the use of swab tests is increasing in identifying symptomatic and asymptomatic cases [12]. The testing and detection of mild cases can affect all treatment processes [13]. Group testing is a fast method for large populations and could be efficient in the case of insufficient tests for all individuals [14]. Accurate systematic tests of COVID-19 are beneficial in controlling a pandemic [15], but the wrong tests could be worse than no tests since they would negatively affect the decision making [16,17]. Some non-pharmacological actions to control the pandemic include lockdown, border closure, and social distancing [18,19]. However, these types of actions are affecting nations economically and socially. Economic and sociological studies have shown that the pandemic has changed lifestyles and affected sustainable development [20,21,22,23]. Other study criteria include modeling of the outbreak [24,25,26], the impact of environmental factors, climate and UV [20,27,28,29], the role of mobility on the epidemic [30], characteristic and persistence resistance of SARS-CoV-2 [31,32], the dynamics of virus transmission [33,34], the veterinary perspective of the COVID-19 epidemic [35], the massive test methods [36], and the challenges around massive vaccination [37,38].

In this regard, due to the characteristics of real-life problems, this study aims to develop a geo-based multi-criteria decision support system considering probabilistic techniques for analysis sustainability, feasibility, and success rate (efficiency or probability of success) of approaches. In the case of COVID-19, many published papers have analyzed the pandemic from different viewpoints separately, such as health, vaccine, masks, and economics. However, the best decision depends on multi-variable analysis by involving all alternatives such as the hybrid analytic hierarchy process (AHP). Therefore, the research objective is to show the application of two developed models, Geo-AHP (by applying geo-based data) and BN-Geo-AHP using probabilistic techniques (using Bayesian network), and the role of machine learning in improving the results. This paper discusses an investigation of different approaches used in confronting the COVID-19 pandemic, their impact on sustainability (social, economic, environmental) beside their success rate, feasibility, acceptance rate by the society, and cost of each approach. The proposed hybrid-AHP methods can be applied in complex problems such as multi-criteria decision making, solving the issue of AHP validation, considering geo data, and machine learning in the analysis, and leading to better pairwise comparisons, rankings, and results.

# 2. Materials and Methods 

In this study, we developed a multi-criteria decision support system confronting complex problems by considering the sustainability, feasibility, and success rate of approaches. According to the literature review analysis, the data type for analysis in a decision can be different. Some data are available in geo-based databanks, such as climate factors or population density, and some have a lot of uncertainty, such as healthcare breakpoint. In the case of COVID-19, mobility from one location to another affected the data resulting in the impact on healthcare capacity and correlated decisions, so that the use of a geo-based layer seemed necessary.

Due to the structure of these types of analysis, we developed two models, including Geo-AHP (by applying geo-based data) and BN-Geo-AHP using probabilistic techniques (by using Bayesian network). Since the provided methods in this study could be applied to prioritize the alternatives in a decision, at first, we generalized Geo-APH and provided the equations so that adding new elements and variables would be possible by experts. Then, we developed the application of the probabilistic technique of the Bayesian network in BN-Geo-APH and the role of machine learning for improving the database and the weighting of each parameter.

Finally, to show the application of the developed models, the new pandemic of COVID-19 that affected nearly all activities was selected for analysis. Therefore, the main approaches and alternatives in confronting the pandemic of COVID-19 containing geo data and the uncertainties were analyzed and ranked. For this purpose, the available data about

COVID-19 and from previous studies about similar virus infections were used. In addition, the main approaches used in different countries to control the pandemic of COVID-19 and their economic and environmental impact were investigated. The analysis flowchart is shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. The analysis flowchart of Geo-AHP and BN-Geo-AHP by using machine learning.
According to the flowchart, at the heart of the system is hybrid-AHP (Geo-AHP or BN-Geo-AHP). The quantitative inputs are geo-based data such as population factors, climate conditions, etc., that might need data processing. The pre-processing of the database, the learning process based on the previous patterns, and post-processing can be carried out using machine learning methods. The qualitative inputs are criteria, alternatives, and decision makers. However, there are some uncertainties in the input data, and therefore, the Bayesian network can be applied. According to the step-by-step method in AHP, pairwise comparisons can be made, and the results would show the final rank of each parameter and the impact of alternatives on the final goal.

# 2.1. Analytic Hierarchy Process (AHP) Ranking Method 

Mathematical and ranking methods are widely used in various fields [39-42] and prioritize decisions in many phenomena [43-46]. The method of AHP, which considers

and evaluates alternatives, can be applied in decision-making problems [47,48]. In this method, different parameters that affect a decision need to be identified first and then can be categorized by their priority by comparing weights and scales. The geographical data is also an important part of some problems and could be added as a layer in the AHP method [49-52]. The weighting system can use simple numbers, fuzzy numbers, or triangular fuzzy numbers [53-56]. In the AHP method, the complex issue can be separated into several steps. Due to the complexity of COVID-19, which has various conditions alongside it, causing a more complex decision-making process, the AHP method has been selected for analysis. The main steps of the AHP method include the determination of parameters and layers, determination of the criteria of weights for comparisons, provision of an assessment matrix, calculation of the final scores, and ranking of the parameters [57]. The fundamental scale in AHP ranking is presented in Table 1.

Table 1. Fundamental scale in the AHP ranking [58].


# Advantages, Disadvantages, and Weaknesses of AHP 

The use of the AHP method changes a multi-criteria decision issue into a more organized structure of simple subjects. The main advantages of the AHP method are its usability, broad application in different fields such as engineering, medicine, and other sciences, and its reasonable system and structure [59]. Ranking by AHP does not require authentic information sets [60]. However, a weakly designed AHP could negatively affect the outcomes [61]. Human emotions may affect the judgments, and the AHP method cannot consider the available but uncertain judgements, resulting in an unrealistic rank and scale of the elements, in some cases [60]. Associated scales and pairwise comparisons in the AHP require sufficient knowledge about the subject. Otherwise, it could be confusing and might create a high level of inconsistency [62]. To improve the application of AHP, solve the issue of validation, and achieve better pairwise comparisons and ranking, one way is through group decisions or using questionnaires [63]. The other method is through a hybrid-AHP by combining the method with other analytical techniques [64], as we used in the current study.

### 2.2. The Concept of Bayesian Network

Decision making always has some degree of uncertainty due to the data, which could be quantitative, qualitative, or graphical [65-68]. To decrease and determine the uncertainty level, the scientific analysis can be combined with previous experiences in similar case studies, expert knowledge, and the Bayesian network [69,70]. A Bayesian network (BN) is a probabilistic graphical model (GM) that represents the causal relationship between variables [71].

BNs include three elements as following [72]:

- A set of "nodes" that represent key variables;
- A set of "links" representing dependency between the nodes;
- A set of "probabilities" representing the given state of the nodes.

BNs are a combination of graph theory, probability theory, statistics, and computer science. According to the Bayesian theorem, the uncertainty of event $A$ can be defined with a probability $P(A)$, which means the probability of occurrence or non-occurrence. In fact, $P(A)$ can be computed in the Bayesian theorem using information with uncertainties. The

basic Bayesian theorem can be defined with conditional probability representing an event $A$ given event $B$ is as follows [73]

$$
P(A \mid B)=\frac{P(A, B)}{P(B)}
$$

$P(A, B)$ : the probability of occurrence of both events $A$ and $B$.
$P(B)$ : the probability of occurrence event $B$.
$P(A \mid B)$ : the condition probability (The probability of occurrence $A$ once $B$ has actually occurred).

If $P(B \mid A)$ demonstrates the probability of occurrence $B$ once $A$ has occurred, then the relationship of the conditional probabilities $P(A \mid B)$ and $P(B \mid A)$ can be given

$$
P(B \mid A)=\frac{P(A \mid B) \times P(B)}{P(A)}
$$

$P(A)$ : the probability of occurrence event $A$.
The Bayesian network is an expansion of the Bayesian theorem over a set of random variables. The equation of a BN for each $x_{i}$ of $X_{i}$ conditioned on $\pi_{i}$, is as follows

$$
P_{B}\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P_{B}\left(X_{i} \mid \pi_{i}\right)
$$

$X_{1}, X_{2}, \ldots, X_{n}$ : random variables.
$P\left(x_{i} \mid \pi_{i}\right)$ : the condition probability.
A Bayesian network containing local conditional probability tables (CPTs) are shown in Figure 2. In this Figure, T means true, F means false, and X1 and X2 depend on Y1, Y2. These variables are the nodes in BNs.

# 2.3. The Role of Machine Learning in Bayesian Networks 

Machine learning techniques can be applied to maximize the performance of collected data from multiple networks. The previous patterns in recoded events can be determined by machine learning and could be applied in the future analysis [74]. The conditional probabilities could be based on experimental or field data, outputs of process-based models using machine learning/artificial intelligence, or by an expert's judgment [75]. In this way, in analysis of probabilistic techniques such as BNs, machine learning methods can be used to characterize the database and predict the behavior [76]. The main roles of machine learning include pre-processing of the database, the learning process based on the previous patterns, and post-processing to generate the rules [77]. In this way, probabilistic techniques used by machine learning methods could help to solve the given training data and prior information (e.g., expert knowledge, casual relationships), and estimate the parameters of the conditional probability tables (CPT).

### 2.4. The Impact of the COVID-19 Pandemic and the Main Methods Used to Confront It

To be able to define the layers and variables in a multi-criteria decision support system, in this section we analyzed the different effects of the COVID-19 pandemic and the main controlling approaches by different countries.

### 2.4.1. The Impact of the Pandemic on Economy

The COVID-19 crisis has changed the lives of 7.8 billion people and affected numerous economic activities. Global trade declined due to the pandemic in 2020 by about 9\% [78]. People facing food crises doubled, and income decreased by $60 \%$ for about 1.6 billion workers [79]. Global GDP declined by $3.9 \%$ in 2020, and potential income loss was significant in many countries. Airlines lost approximately USD 370 billion in 2020 worldwide [80,81]. The growth projections for many countries in 2020 were negative such as -5.9 for the U.S., -7.2 France, -9.1 Italy, -6.5 UK [82]. The analysis of different scenarios shows that this

pandemic could cost the global economy up to USD 2.7 trillion [83]. According to a World Bank analysis report, global economic growth in 2020 was the lowest since World War II [84]. The European Union (EU) announced a recovery fund of about EUR 1.5 trillion [85], and the U.S. announced a recovery program of USD 700 billion in March 2020, and a loan budget of USD 2.3 trillion to support small businesses [86].

Tourism and related activities are among the highest affected sectors. Due to the pandemic, international tourism decreased by about $60-80 \%$ in 2020, which means a loss of about USD 850 billion [87]. The impact of this huge decrease may remain for several years [88]. Finally, between 3.5 and $7 \%$ of global GDP depends on the blue economy, from coastal tourism to fisheries and sea transports, which the pandemic could heavily affect and decrease [89].
![img-1.jpeg](img-1.jpeg)

Figure 2. A Bayesian network with four variables and local conditional probability tables.

# 2.4.2. The Coronavirus Vaccine, Investments, and Vaccine Efficiency 

The problem of producing an effective vaccine with the lowest side effects is very important, and is one of the possible methods to control a pandemic. More than 150 countries joined into COVAX Facility for a COVID-19 vaccine. COVAX partners' goal is to deliver two billion doses of vaccines for high-risk groups by the end of 2021 [90]. Researchers are working on more than 165 vaccines, and, up to 24 July 2020, more than 140 vaccines were at the preclinical stage, about 27 at the stage of human trials, 19 were in phase I, 13 in phase II, 4 in Phase III, and 1 was approved for limited use [91]. After two months, huge progress had been made as, on 30 September 2020, 28 vaccines were in phase I, 14 in phase II, 11 in Phase III, and five were approved for limited use. After about 6 months, in April 2021, 4 vaccines had been abandoned, 49 vaccines were in phase I, 35 in phase II, 27 in Phase III, 5 were approved for limited use and 8 vaccines were approved for full use [91] and more than 1 billion doses of vaccine had been used worldwide [92].

The major projects and investments by different countries and international banks focused on the COVID-19 vaccine are presented in Table 2.

Table 2. Major projects and investments for a COVID-19 vaccine.

(30 September 2020) | Phase
(30 March 2021) | Reserve doses (Million) | Ref.  |

- III+ APPROVED FOR LIMITED USE.

As can be seen in Table 2, a huge investment has been made so far in different countries. However, several issues still remain for the massive vaccination in all countries including production of enough doses, the storage, transportation, and distribution of vaccines worldwide which need greater effort, organization, and trained staff.

The U.S. biomedical advanced research and development authority (BARDA) invested over USD 2.1 billion in May 2020, developing the COVID-19 vaccine both by US-based and international companies [94]. The U.S. investment in the COVID-19 vaccine has increased and reached USD 8 billion in August 2020 [100] and nearly USD 10 billion in March 2021 [119].

By May 2020, the global campaign budget increased to EUR 9.8 billion [120]. Germany, Italy, France, and the Netherlands invested about EUR 750 million (USD 843.2 million) for 300 million doses of the potential vaccine by AstraZeneca (Oxford University). The share of Italy for 75 million doses was EUR 185 million [116]. Germany-based BioNTech and Pfizer aim to provide more than 1.3 billion doses in 2021 [99,108]. The US-based company of Janssen is aiming to produce 1 billion doses of vaccine Ad26.COV2.S in 2021 [98]. Chinesebased Sinovac Biotech started the limited use of the vaccine from early 2021 [121]. Sanofi is planning to deliver up to one billion doses of vaccine in 2021 [100].

The threshold to stop spreading the virus through immunity by a new vaccine is about $60-70 \%$, which means billions of people. The prioritization for delivering the COVID-19 vaccine were different in each country. Some started the vaccination from the high-risk groups such as healthcare workers and older people and some started just based on age. It would be unrealistic to expect a COVID-19 vaccine with $100 \%$ effectiveness. However, the analysis shows a vaccine with $50 \%$ effectiveness could be a game-changer [122,123]. For the COVID-19 vaccine, there are still uncertainties about the possibility of reinfection and duration of immunity, and the efficiency of vaccines for symptomatic infection hospitalization are different; besides new mutations could affect their efficiency [124].

While the effectiveness of new vaccines is unknown [95], one can refer to studies about the vaccine for another type of Coronavirus, influenza (flu) [125-127]:

- The vaccine effectiveness (VE) can vary and depends on the variety, as the efficiency of flu vaccines for influenzas type A (H1N1) and B are better than type A (H3N2);
- If the flu vaccine is well matched with most circulating seasonal flu viruses, the total flu risk can be reduced to $40-60 \%$;
- The monitoring of vaccine effectiveness for the three different influenzas showed, in general, the success rate was between 30 and $60 \%$.
In 2018/2019, about half of adults and $68 \%$ of people aged over 65 in the U.S. used the flu vaccine. However, according to the Centers for Disease Control and Prevention (CDC), seasonal flu vaccines' effectiveness in 2018-2019 was about $29 \%$, whereas, in previous years, it was typically about $50 \%$ [128]. Moreover, for influenza, which has a clear transmission season, the vaccine needs to be updated annually, and more development is required [129]. Whereas the flu vaccine's effectiveness is about $40 \%$ to $60 \%$ [122], the measles vaccine's effectiveness is about $95 \%-98 \%$ [130]. Based on the previously infected population, the analysis determined that a vaccine with an efficacy of about $60 \%$ could stop the pandemic, but it is likely that social distancing and mask wearing would still have to continue [130]. The required vaccine efficacy for managing the pandemic of $60 \%$ is, for the moment, dependent on vaccination coverage being $100 \%$. The required efficacy rises to $70 \%$ and $80 \%$ when the vaccination coverage drops to $75 \%$ and $60 \%$, respectively. The efficacy of at least $80 \%$ might be required to stop any other measures being needed [131].

Reinfection and immunity failure are other critical factors, as a new study shows 140 days of immunity from the first infection in patients [132]. Mutations of SARS-CoV-2, which can cause the virus to elude antibodies, are another issue. Researchers have already found several mutations in the virus worldwide, which have not been recognized by neutralizing antibodies [133]. Finally, to achieve a sufficient immunity level, the majority of the population need to be vaccinated. The immunity cannot be achieved if just two-thirds of the population take a vaccine with $70 \%$ to $75 \%$ efficacy [134].

Therefore, the vaccines' success rate depends on their effectiveness and the percentage of the vaccinated population that is high enough to break the transmission chains.

# 2.4.3. Medical Face Masks, Gloves, and the Environmental Issues 

Studies show that public face masks could be an effective way to reduce virus spread [135,136]. The widespread use of medical face masks reduce the transmission rate, and even non-medical masks can block some parts of contaminated droplets [137,138]. The assessment of using medical face masks (type N95) in the context of influenza showed that if they were used by about $80 \%$ of the population, the outbreak could be eliminated [139]. The first recommendations were using N95 (or FFP2) for health workers in aerosol-generating procedures and surgical masks for non-aerosol generating procedures [140]. However, recently use of two masks has also been recommended by some analysis [141,142]. While estimations showed the required annual masks just for medical workers would be billions, the storage capability in some countries is less than $1 \%$ of the requirements [143], showing the high issues for mask producers. Masks production needs an industrial chain from basic industries, chemical, and textile to metallurgy and electronics industries. The cost of medical masks has increased severely since the start of the pandemic. Medical facemasks are produced mainly from polymers such as polyurethane, polyacrylonitrile, polypropylene, and polyester [144], and consist of three layers as follow [145]:

- The inner layer (soft fibers);
- The middle layer (the main filtering layer produced from the melt-blown filter);
- The outer layer (Nonwoven fibers, which are usually colored and water-resistant).

Microplastics, including single-use polymeric materials and plastic packaging materials, are a significant source of environmental pollution threatening aquatic lives and raising concerns on global food safety [146]. The increase in medical masks creates a new environmental challenge, and the materials of different types of medical masks have been reported in oceans [147]. One study showed that using single-use mask could create 66,000 tons of plastic waste in one year [148]. Furthermore, the same issue exists for hand sanitizers and gloves since, after the pandemic, these affect the environment in the same way as face masks.

### 2.4.4. COVID-19 Tests Characteristics and Advantages

By COVID-19 tests, it is possible to trace and isolate positive cases, thus counting as a way to control the pandemic. The recommendation of the World Health Organization (WHO) is to test every suspected cases, and to consider testing and isolation as the most effective ways to break the transmission chain [149]. The key in control of the SARS-CoV-2 pandemic is restricting the spread of the virus by rapid and massive testing [150,151]. Concerning testing methods, sensitivity and accuracy are key issues that vary significantly from one test to another test or manufacturer. Different types of tests that can be used for COVID-19 are as follow:

- Serology test: this test can be completed in 20-30 min using a few drops of blood to determine the possible presence of coronavirus antibodies (proteins produced by the immune system to neutralize bacteria/viruses) in the human body. The antibodies take around eight days to develop and to appear in the blood. Therefore, in the early stage of infection, the result can be falsely negative. However, this test is accurate after around the eighth day of infection. This test's advantages are its low cost and it does not require specially trained staff [149]. The antibodies may remain in the blood for several weeks after recovery, and this can identify previous positive cases that might have immunity in the future. However, the duration and percentage of immunity are not confirmed yet [152].
- RT-PCR and NAT tests: this direct test aims to determine whether the virus produced antibodies because of infection. In molecular tests such as nucleic acid test (NAT) and reverse transcription-polymerase chain reaction (RT-PCR), the genetic material of COVID-19 can be detected. In both RT-PCR and NAT tests, a nasal or throat swab

is used, and positive cases can be identified on the first day of infection. The cost of RT-PCR (about five to six hours to test the samples) is around ten times more than the antibodies test and two times more than NAT (about an hour). The NAT test, which can be ready in one hour, is accurate and does not need trained staff or a special lab. However, doing the RT-PCR test, which is more expensive than NAT, requires highly qualified staff to collect the samples and to do the test, and the result may take around one day [149,152]. However, the results of the test might take longer due to the high number of tests, and a late result could negatively affect the control approaches, such as the isolation of positives cases at the moment of infection.

- Antigen test: the antigen test can detect the specific proteins on the virus' surface. The antigen test method is through nasal or throat swab, and the result can be ready in about one hour. This test's positive result is highly accurate, but the negative result might need confirmation by another methods, such as a molecular test [149,152].
- Diagnostic test: another type of test is the diagnostic test, such as saliva tests, which can be done by analyzing spit instead of throat swab, and it is more comfortable for people and health workers since no close contact is required [152].
To increase the number of tests for a large population, and in the case of insufficient availability of tests for all individuals separately, the method of group testing or pooled testing (multiple individual tests together) can be applied [14]. If the result of a pooled test becomes negative, it means all individuals in the group are negative, and if the test result shows positive, all individuals in that group need to be tested separately [149]. However, the pooling test might not be a solution of RT-PCR since the effectiveness and the error level is still high and could be used for a pre-analysis.

The number of tests by country depends on several factors such as the financial condition, laboratory capacity, trained staff, and available test options. The manual test systems require special kits, devices, and chemical reagents, and the countries that produce the tests are mainly using them for domestic purposes. Automated test units can solve the need for trained staff, but the cost of the units is high. Global organizations are trying to reduce the price of test machines and the required materials [153]. Swabs for the COVID-19 test are made using a long and thin plastic with a synthetic fiber. However, the total swabs production of different countries is not clear [154,155].

More tests result in higher pandemic control successes, and any delay in doing tests can cause more spread of the virus. Accurate testing requires several processes including test kits, nasal swabs, chemical reagents, lab authorization for doing tests, PCR machines, laboratory technicians, and report system [156].

Since the production number is much less than expected, the use of 3D printers could increase production and decrease the cost [157]. The swab production chain could be established in two weeks and would make a scalable and cost-effective swab [158]. The new developed swab test can provide a molecular test result after less than 30 min , and the cost per person would be around USD 5 [159].

# 3. Results and Discussion 

### 3.1. Developing Models and Ranking of the Approaches

In this section, first we developed and generalized the ranking Geo-AHP method so it would be possible to add new criteria and alternatives by experts. Then, we showed the application of the developed model for the analysis and ranking of the main approaches and alternatives in confronting the pandemic of COVID-19. Finally, we applied the probabilistic techniques in BN-Geo-APH, demonstrated its application, and compared the results.

### 3.1.1. Generalized Geo-APH Approach for Comparison of the Decision Ranks

A. Computing the normalized weight for components of criteria:

The pairwise comparison matrix of the components in the layer of criteria is presented in Table 3.

Table 3. Pairwise comparison of Criteria concerning the main goal.


In Table 3, supposing $\mathrm{x}_{p, q}$ is the pairwise comparison of criteria $p$ and $q$, then

$$
\text { for } p, q=1, \ldots, n \text { and } p \neq q: x_{q, p}=\frac{1}{\mathrm{x}_{p, q}} \text { for } p=q: x_{p, q}=x_{q, p}=1
$$

The normalized weight can be calculated in 4 steps, Equations (5) to (8):
Step 1: calculation of $M_{q}$ (the sum of the values of the $q$ th column for $q=1, \cdots, n$ in Table 3)

$$
\text { for } q=1, \cdots, n: \quad M_{q}=\sum_{p=1}^{n} x_{p, q}
$$

Step 2: calculation of $N_{p, q}$, for $q=1, \cdots, n$

$$
\text { for } p=1, \cdots, n: \quad N_{p, q}=\frac{\mathrm{x}_{p, q}}{M_{q}}
$$

Step 3: calculation of the normalized weight for all criteria $w_{p}$

$$
\text { for } p=1, \cdots, n: \quad w_{p}=\frac{\sum_{q=1}^{n} N_{p, q}}{n}
$$

Step 4: the weight vector of the component for criteria will be

$$
w=\left(w_{1}, \cdots, w_{n}\right)^{T}
$$

The evaluation of the results can be done by computing the consistency ratio (CR) for the pairwise comparison matrix of the component of criteria. The CR of the pairwise comparison matrix can be calculated according to Equations (9) to (13) [160]:

Calculation of $v_{p}$

$$
\text { for } p=1, \cdots, n v_{p}=\sum_{q=1}^{n} x_{p, q} * w_{q}
$$

Calculation of $\lambda_{p}$

$$
\text { for } p=1, \cdots, n \lambda_{p}=\frac{v_{p}}{w_{p}}
$$

Calculation of $\lambda_{\max }$

$$
\lambda_{\max }=\frac{\lambda_{1}+\ldots+\lambda_{n}}{n}
$$

Consistency index (CI)

$$
C I=\frac{\lambda_{\max }-n}{n-1}
$$

Consistency ratio (CR)

$$
C R=\frac{C I}{R I}
$$

where RI is the Random Consistency Index and its value is presented in Table 4.
If $\mathrm{CR} \leq 0.1$, the level of inconsistency is acceptable. Otherwise, the inconsistency is high, and, to achieve better consistency, a re-estimation for the element of $\mathrm{x}_{\mathrm{p}, \mathrm{q}}$ might be required.
B. Computing the normalized weight for components of decision makers

The pairwise comparison matrix of the components of decision makers concerning different components of criteria is presented in Table 5.

Table 4. Random index for a several matrix dimensions [160].


Table 5. Pairwise comparison of decision maker components concerning components of criteria.


In Table 5, supposing $D_{p, q}^{i}$ is the pairwise comparison of decision maker $p, q=1, \ldots$, $m$, concerning the $i$ th component of criteria $(i=1, \ldots, n)$, then

$$
\text { for } p \neq q: \quad D_{q, p}^{i}=1 D_{p, q}^{i} \text { and for } p=q: \quad D_{p, q}^{i}=D_{q, p}^{i}=1
$$

With an algorithm similar to the mentioned steps 1 to 5 in the past section, the normalized weight of decision makers concerning different components of criteria can be calculated, and the weight vector is as follows

$$
w^{i}=\left(w_{1}^{i}, \cdots, w_{m}^{i}\right)^{T}
$$

where $w_{j}^{i}=$ weight of the $j$ th component of the decision makers $(j=1, \ldots, m)$, under the $i$ th component of criteria $(i=1, \ldots, n)$.
C. Computing the normalized weight for components of factors (geo-based data)

The pairwise comparison matrix for the components of factors (geo-based data) concerning different components of decision maker is presented in Table 6.

Table 6. Pairwise comparison of factors (geo-based data) concerning components of decision maker.


In Table 6, supposing $F_{p, q}^{j}$ is the pairwise comparison of factor $p, q=1, \ldots, l$, concerning the $j$ th components of decision makers $(j=1, \ldots, m)$, then

$$
\text { For } p \neq q: F_{q, p}^{j}=\frac{1}{F_{p, q}^{j}} \text { and for } p=q: F_{p, q}^{j}=F_{q, p}^{j}=1
$$

With an algorithm similar to the mentioned steps 1 to 5 in the past section, the normalized weight of factors concerning different components of decision makers can be calculated, and the weight vector is as follows:

$$
w^{j}=\left(w_{1}^{j}, \cdots, w_{l}^{j}\right)^{T}
$$

where $w_{f}^{j}=$ weight of the $f$ th component of the factors $(f=1, \ldots, l)$, under the $j$ th component of decision makers $(j=1, \ldots, m)$.
D. Computing the normalized weight of components for alternatives

The pairwise comparison matrix of the components of alternatives concerning different components of factors is presented in Table 7.

Table 7. Pairwise comparison of alternatives concerning different components of Factors.


In Table 7, supposing $A_{p, q}^{f}$ is the pairwise comparison of alternative $p, q=1, \ldots, t$, concerning the $f$ th component of factors $(f=1, \ldots, m)$, then

$$
\text { for } p \neq q: A_{q, p}^{f}=\frac{1}{A_{p, q}^{f}} \text { and for } p=q: A_{p, q}^{f}=A_{q, p}^{f}=1
$$

With an algorithm similar to the mentioned steps 1 to 5 , the normalized weight of alternatives concerning different components of factors can be calculated, and the weight vector is as follows

$$
w^{f}=\left(w_{1}^{f}, \cdots, w_{t}^{f}\right)^{T}
$$

where $w_{k}^{f}=$ weight of the $k$ th component of the alternatives $(k=1, \ldots, t)$, under the $f$ th component of factors $(f=1, \ldots, l)$.
E. Relative importance coefficient (RIC) of alternatives concerning the goal

The total aggregated score for each component of alternatives $(k=1, \ldots, l)$ concerning the goal can be calculated as follows

$$
(R I C)_{k}=\sum_{i=1}^{n} w_{i}\left(\sum_{j=1}^{m} w_{j}^{i}\left(\sum_{f=1}^{i} w_{f}^{j}\left(w_{k}^{f}\right)\right)\right)
$$

Therefore, the relative importance coefficient (RIC) can determine each alternative's final rank by considering all the upper layers' components.

3.1.2. Application of the Developed Geo-AHP in Ranking of Decisions to Control the COVID-19 Pandemic

The developed Geo-AHP for ranking of decisions is based on the literature reviews' findings to control the COVID-19 pandemic and is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. The developed Geo-AHP layers for ranking of approaches: COVID-19 pandemic.
The determined layers in our Geo-AHP are:

- Layer 1 (goal): sustainability, feasibility, and success rate of approaches (in our case means the end of pandemic and sustainable development);
- Layer 2 (criteria): including success rate, economic, environmental, and social;
- Layer 3 (decision makers): three decision makers including individuals, governments, and international organizations;
- Layer 4 (factors): four geo-based factors including healthcare capacity, population factors (density, average age, etc.), climate condition, and urban infrastructure;
- Layer 5 (alternatives): periodic lockdown, use of mask and gloves, massive vaccination, and massive swabs or other tests.
The parameters in different approaches were analyzed based on previous case studies about similar diseases and the current pandemic (literature review) and compared as pairs (two items) to be scaled under special consideration. The pairwise comparison matrices for the developed Geo-AHP are presented in Tables 8-11.

The pairwise comparison matrices were completed according to the literature review analysis. First, different criteria were scaled by considering the goal, and then decision makers were scaled by considering the criteria. In the next step, the geo-based factors were weighted according to decision makers and finally, the alternatives weights were

Table 8. Pairwise comparison matrix of criteria.


Table 9. Pairwise comparison matrix of decision makers.


Table 10. Pairwise comparison matrix of factors (geo-based data).


Table 11. Pairwise comparison matrix of alternatives.


Table 12. The RIC values for alternatives concerning the goal.


# 3.1.3. Ranking Using Bayesian Network, BN-Geo-AHP 

Bayesian networks can be used to make decisions in uncertain situations. Therefore, we used it to improve the developed Geo-AHP model as there are many uncertainties in the COVID-19 pandemic phenomenon. Three types of nodes, including the utility node (goal), probability nodes (criteria, decision makers, and geo-based factors), and decision node (alternatives) were used in the model. In Table 13. the structure of BN-Geo-AHP and the descriptions and states of the nodes are presented. The probability table of the criteria is presented in Table 14, and the conditional probability tables of decision makers and factors (geo-based data) are presented in Tables 15 and 16.

Table 13. The structure and descriptions of nodes in the developed BN-Geo-AHP.


Table 14. Probability table of the Criteria.


Table 15. Conditional probability table of the decision makers.


In Table 15. the layer of decision makers: $I=$ individuals, governments, and international organizations, and in its higher layer criteria: success rate (SR), economic (Ec), environmental (En), social (So).

Table 16. Conditional probability table for factors (geo-based data).


In Table 16, the layer of factors: $J=$ healthcare capacity, population factors, climate factors, urban infrastructure, and in its higher layer decision makers: individuals (IN), governments (GO) and international organizations (IO).

The developed BN-Geo-AHP and its calculated probabilities are shown in Figure 4. As shown in Figure 4, the highest probability among the alternatives belonged to the massive vaccination approach ( $40.1 \%$ ), and the second to massive swab or other testing ( $35.8 \%$ ). Use of mask/gloves with the probability of $16.6 \%$ was the third, and the lowest calculated probability belonged to the periodic lockdown ( $7.5 \%$ ). The results are similar to the ranks given by Geo-AHP; however, the calculations by the BN method considered the conditional probabilities and could be more relevant.
![img-3.jpeg](img-3.jpeg)

Figure 4. The developed BN-Geo-AHP.
For use with a large databank, the role of machine learning in the proposed Bayesian networks framework would be for the calculation of the pairwise weights of BN-GeoAHP according to analysis of the data, and can improve the computation of the relative importance coefficient (RIC) of alternatives concerning the main goal. To implement the application of machine learning in BN-Geo-AHP the steps are as follow:

- Pre-processing of the database;
- Classifying the attributes using machine learning algorithms;
- Obtaining the Bayesian networks model and computing the conditional probabilities tables (CPTs) based on the available database;
- Modeling of the Geo-AHP according to the result of the BN model;
- Performing the weights estimation algorithm for Geo-AHP model to convert the probabilistic values of the CPT into the weights for relevance pairwise comparisons;
- Assigning the obtained weights to calculate the relative importance coefficients (RICs) of alternatives;
- Final ranking according to the RICs.

Recommendations for future studies

In this study we developed two models and explained the role of machine learning and geo-based data in improving the weight and ranking of approaches for solving complex problems. The use of an analytic network process (ANP) for validation of the AHP is recommended for analysis in future studies. The use of databank and geo-based software like GIS for analysis of the role of machine learning is recommended for future studies.

# 4. Conclusions 

This analysis of the developed geo-based multi-criteria decision support systems considering probabilistic techniques for the sustainability, feasibility, and success rate (efficiency or probability of success) of approaches demonstrated the use of the applications in complex problems. The results showed that the proposed hybrid-AHP methods can be applied for the COVID-19 pandemic issue, considering the geo data layer, different decision makers and several alternatives, and alongside the use of machine learning for analysis of a large databank.

The analysis determined that, while ranking by the AHP method does not involve validation like linear programming, the defined structure and pairwise comparisons procedure is very important. To improve the results, group decisions, using questionnaires or developing a hybrid-AHP combining the method with other analytical techniques, and adding uncertainties such as Bayesian network, can be used.

To examine the developed models, the COVID-19 pandemic was selected. The COVID19 pandemic affected nearly all activities such as political, global economic, and sociocultural. The main strategies used so far, such as lockdowns, mandatory or self-quarantine, social distancing, travel bans, using facemasks and gloves, increasing the number of tests, and vaccination, did not fully overcome the pandemic, and it is estimated that the global cost of a new pandemic could be up to USD 2.7 trillion. The analysis of the COVID-19 outbreak in different countries shows that policies such as lockdown can be implemented only as a temporary method to help the health system, since, often after the lockdown, the number of infections kept gradually increasing. The success rate of the mandatory use of medical masks and gloves was different in separate countries and depended on people's acceptance to wear a facemask frequently and correctly. For control of the virus transmission, the use of a billion facemasks and gloves might be required before the end of the pandemic, but this has already created a new environmental challenge.

The analysis of COVID-19 tests shows that there are several types of tests and combinations of tests, and increasing the test number, besides improving the group or pooled testing, can be useful. The number of tests depends on several factors, such as the financial condition, laboratory capacity, trained staff, and available test options. Massive testing might not be feasible for the great majority of countries but could be possible in the future due to global organizations' trying to reduce the price of the test (materials and machines).

There are extensive efforts being applied for the development of a vaccine for COVID19, and massive vaccination through large investments from different countries. Moreover, the need to vaccinate $70 \%$ of the population and the vaccine's effectiveness are other important points to consider. However, previous vaccines' success rates suggest that the new vaccine would possibly be available for the whole population by the end of 2021, during which time the pandemic might have caused greater damage.

According to the analysis, before massive vaccination, the methods used previously to control the pandemic so far might need to continue in the next months, making it necessary to focus on the fastest ways to decrease the negative impacts. The ranking results with two developed models in this study show that massive vaccination is the first ranked method and the second ranked is massive swab or other testing. The third ranked is the use of medical masks and gloves, and the last ranked is lockdown. Therefore, besides the vaccination programs being developed by countries, expanding testing, the quantitative increase in tests, and the rapidity of the announcement of results for detecting and isolating positive cases and breaking the transmission chains might be the most effective approaches in the forthcoming months.

The results showed that the proposed models are suitable for analysis of the multicriteria decision making involving quantitative and qualitative inputs with degrees of uncertainty, and the new variables can be added easily in all layers. Finally, the step-bystep analysis in the models can categorize and prioritize different parameters that affect a decision by comparing weights and scales.

In conclusion, the new models of Geo-AHP and BN-Geo-AHP could be useful as multicriteria decision support system in the analysis of complex structures with uncertainties, such as the COVID-19 pandemic.

Author Contributions: Conceptualization, Behrouz Pirouz and Patrizia Piro; Methodology, Behrouz Pirouz and Behzad Pirouz; Formal analysis, Behzad Pirouz and Behrouz Pirouz; Validation, Behzad Pirouz; investigation, Behrouz Pirouz; Writing-original draft preparation, Behrouz Pirouz; Writingreview and editing, Behrouz Pirouz and Behzad Pirouz; Visualization, Behrouz Pirouz; Supervision, Aldo Pedro Ferrante and Patrizia Piro. All authors have read and agreed to the published version of the manuscript.

Funding: This research received no external funding.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data sharing not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
