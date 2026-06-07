# Bayesian Network Analysis of Mobile Service and Device Usage 

Pekka Kekolahti

# Bayesian Network Analysis of Mobile Service and Device Usage 

Pekka Kekolahti

A doctoral dissertation completed for the degree of Doctor of Science (Technology) to be defended, with the permission of the Aalto University School of Electrical Engineering, at a public examination held at the lecture hall AS1 of the school on 17 January 2020 at 12:00.

Supervising professor
Professor Heikki Hämmäinen

# Thesis advisor 

Professor Heikki Hämmäinen

## Preliminary examiners

Professor Norman Fenton, Queen Mary University of London, England
Professor Pekka Neittaanmäki, University of Jyväskylä, Finland

## Opponent

Dr. Tomi Silander, Naver Labs Europe, Meylan, France

Aalto University publication series
DOCTORAL DISSERTATIONS 201/2019
(c) 2019 Pekka Kekolahti

ISBN 978-952-60-8794-8 (printed)
ISBN 978-952-60-8795-5 (pdf)
ISSN 1799-4934 (printed)
ISSN 1799-4942 (pdf)
http://urn.fi/URN:ISBN:978-952-60-8795-5

Unigrafia Oy
Helsinki 2019

Finland

Author<br>Pekka Kekolahti<br>Name of the doctoral dissertation<br>Bayesian Network Analysis of Mobile Service and Device Usage<br>Publisher School of Electrical Engineering<br>Unit Department of Communications and Networking<br>Series Aalto University publication series DOCTORAL DISSERTATIONS 201/2019<br>Field of research Network Economics<br>Manuscript submitted 27 June 2019<br>Date of the defence 17 January 2020<br>Permission for public defence granted (date) 1 October 2019 Language English<br>$\square$ Monograph $\quad \square$ Article dissertation $\quad \square$ Essay dissertation

# Abstract 

The use of mobile services has changed significantly in the last twenty years. Initially, only mobile calls and short messages were the services used, whereas today the use of mobile services has evolved into multiple parts of a human's daily life. Due to this evolution, research into mobile service usage consists of many, often complex study themes. In parallel, statistical methods and computing systems have developed rapidly, providing sophisticated methods for researchers, for example, to study mobile service usage.
The objective of this thesis is twofold. On one hand, the purpose is to describe the best practises related to a Bayesian networks-based statistical method. On the other hand, the evolution of mobile services in Finland and their usage patterns are explored empirically using the Bayesian networks approach.
The thesis documents systematically Bayesian networks-based approaches for descriptive, predictive and explanatory data analysis. The documentation covers the whole process from the pre-processing of data, construction of the models to the inferencing based on the constructed models. Moreover, differences between predictive and causal models are clarified.
The results from the empirical analysis deal with multiple aspects of mobile service usage. The following aspects were of greatest significance: structural breaks in the popularity of mobile device features in Finland were identified; these transition points over time acted as a basis for the explanation for the changes in the Finnish mobile market; mobile service users were segmented into main three groups based on service usage patterns; users' age as an important factor related to the user behaviour were indicated; and, finally, multiple risks associated with the use of mobile services were detected.
Overall, the thesis provides practical information about Bayesian networks, which will hopefully encourage more researchers to use the Bayesian networks approach in the statistical analysis. Furthermore, the research provides several individual results, which are of interest to all mobile ecosystem players. These are, for instance, the discovered role of some services as mediators of other service usage, the central role of age as a reason for service intensity and diversity, and the creation of an expert knowledge elicitation process in cases when the experts from a knowledge and location point of view are dispersed.

Keywords Bayesian networks, mobile service usage, mobile device, causal analysis, predictive analysis, clustering
ISBN (printed) 978-952-60-8794-8 ISBN (pdf) 978-952-60-8795-5
ISSN (printed) 1799-4934 ISSN (pdf) 1799-4942
Location of publisher Helsinki Location of printing Helsinki Year 2019
Pages 243
urn http://urn.fi/URN:ISBN:978-952-60-8795-5

.

# Tekijä 

Pekka Kekolahti

## Väitöskirjan nimi

Mobiilipalveluiden ja laitteiden käytön analyysi Bayes-verkoilla
Julkaisija Sähkötekniikan korkeakoulu
Yksikkö Tietoliikenne- ja Tietoverkkotekniikan laitos
Sarja Aalto University publication series DOCTORAL DISSERTATIONS 201/2019
Tutkimusala Tietoverkkotalous


## Tivistelmä

Mobiilipalvelujen käyttö on muuttunut merkittävästi viimeisten 20 vuoden aikana. Kun aluksi käyttö liittyi vain mobiilipuheluihin ja tekstiviesteihin, niin nykyään palvelujen käyttö on laajentunut kattamaan monia ihmisen jokapäiväisen elämän alueita. Tämän takia myös mobiilipalvelujen käytön tutkimus on laajentunut monille osa-alueille. Samanaikaisesti tilastolliset menetelmät ja tietojenkäsittely ovat kehittyneet nopeasti tarjoten edistyneitä menetelmiä esimerkiksi mobiilipalvelujen tutkimiseen.
Tällä väitöskirjalla on kaksi tavoitetta. Toisaalta tarkoituksena on kuvata hyvin toimivia käytäntöjä Bayes-verkoilla tapahtuvaan tilastolliseen analyysiin, toisaalta tavoitteena on analysoida mobiilipalvelujen kehitystä ja käyttöä Suomessa empiirisesti soveltaen tähän Bayes-verkkoja. Väitöskirjassa on dokumentoitu Bayes-verkkojen käyttö kuvailevaan, ennustavaan ja selittävään datan analyysiin. Dokumentaatio käsittää koko prosessin datan esiprosessoinnista ja datamallien rakentamisesta aina johtopäätöksien tekoon mallien avulla. Tämän lisäksi on tarkasteltu ennustavien ja kausaalisten mallien eroja.
Empiirisen tutkimuksen tulokset koostuivat seuraavista löydöksistä: Identifioitiin aikaan ja mobiililaitteiden kaupalliseen suosioon liittyviä rakenteellisia käännekohtia, joiden perusteella voitiin selittää tiettyjä muutoksia suomalaisessa mobiilimarkkinoissa. Mobiilipalvelujen käyttäjät segmentoitiin kolmeen pääryhmään riippuen mobiilipalvelujen käyttötavoista. Mobiililaitteiden käyttäjän iällä osoitettiin olevan merkittävä vaikutus siihen, mitä mobiilipalveluita käytetään ja kuinka tärkeänä niitä pidetään. Lisäksi todennettiin mobiilipalvelujen käyttöön liittyviä riskejä, niiden todennäköisyyksiä sekä seurannaisvaikutuksia.
Väitöskirja tarjoaa käytännönläheistä tietoa Bayes-verkoista, mikä toivottavasti kannustaa tutkijoita käyttämään Bayes-verkkoja nykyistä enemmän tilastolliseen analyysiin. Lisäksi väitöskirja sisältää useita tuloksia, jotka ovat kiinnostavia koko mobiilille ekosysteemille. Tällaisia ovat esimerkiksi eräiden palvelujen rooli mediaattorina muiden mobiilipalveluiden käytölle, ihmisen iän keskeinen merkitys palvelujen käytön intensiteetille ja monimuotoisuudelle. Kehitettiin myös menetelmä, jolla voidaan kerätä ja dokumentoida asiantuntijatietoa Bayesverkoksi erityisesti silloin, kun asiantuntijoiden osaamisalueet vaihtelevat ja heidän sijaintinsa on hajaantunut eri puolille maapalloa.

Avainsanat Bayes-verkko, mobiilipalvelu, mobiililaite


ISSN (painettu) 1799-4934
Julkaisupaikka Helsinki
Painopaikka Helsinki
Vuosi 2019
Sivumäärä 243
urn http://urn.fi/URN:ISBN:978-952-60-8795-5

.

# Preface 

Writing the dissertation has been a long learning journey, lasting almost ten years. The initial impetus for my interest in Bayesian networks took place already in my earlier work in Nokia Networks, but the actual learning and practical experience evolved out of the work done at Kekonet; work that provided a good background for this thesis. I would like to warmly thank my supervising professor Heikki Hämmäinen, who guided me through this thesis and gave me much practical advice during the period of my doctoral studies. Heikki gave me the chance to work in the research group, granting me a great deal of freedom to find my own path with the research. I am grateful for the insightful comments I received from the preliminary examiners Professors Norman Fenton and Pekka Neittaanmäki. I am also very honoured to have Dr. Tomi Silander as my opponent in the thesis defence.
I offer special thanks to docent Kalevi Kilkki, Dr. Juuso Karikoski and Dr. Antti Riikonen who gave me a lot of guidance when we wrote articles together, and to Dr. Matti Peltola and Kristian Herland for creative cooperation when adapting Bayesian networks for risk assessment. I am also grateful to many current and former members of the Network Economics research group and the department of Communications and Networking. Dr. Henna Suomi, Dr. Tapio Soikkeli, Dr. Nan Zhang, Dr. Arturo Basaure, Dr. Michail Katsigiannis, Dr. Thomas Casey, Dr. Benjamin Finley, and Dr. Alexandr Vesselkov, thank you for all the discussions and help during the years we shared at the university.
During the dissertation work, I have been lucky to receive advices from multiple Bayesian networks experts, to whom I am grateful for, including Dr. Lionel Jouffe and Dr. Petri Myllymäki. I would also like to give thanks to Dr. Larry Audet, Dr. Lassaad Essafi, Esko Räty, Vesa Jaakkola, Mikko Salminen, Edward Fonsell and the late Antti Myllykangas who pushed and encouraged me to get my dissertation finished, and William Martin who has helped with polishing the English language of the final manuscript.
Finally, I wish to thank my lovely family members Taina, Saija, Olli and Mikko for their support and encouragement to start and finalize my doctoral thesis at my mature age.

Helsinki, 20th of October 2019
Pekka Kekolahti

ii

# Contents 

Preface ..... i
Contents ..... iii
List of Abbreviations and Symbols ..... v
List of Publications ..... ix
Author's Contribution ..... x

1. Introduction ..... 1
1.1 Background and motivation ..... 1
1.2 Research problem and objectives ..... 3
1.3 Definitions ..... 4
1.4 Research approach ..... 6
1.5 Thesis structure ..... 7
2. Theoretical background ..... 8
2.1 Bayesian networks ..... 8
2.1.1 What are Bayesian networks? ..... 9
2.1.2 Properties of Bayesian networks ..... 12
2.1.3 Subjective probability ..... 14
2.1.4 Construction of a Bayesian network ..... 14
2.2 Research of mobile service usage ..... 31
2.2.1 Classification of mobile services ..... 32
2.2.2 Business models ..... 32
2.2.3 Usability of mobile services ..... 33
2.2.4 Technology acceptance ..... 33
2.2.5 Diffusion of innovation ..... 34
2.2.6 Consumer behaviour ..... 34
2.2.7 Customer experience ..... 35
2.2.8 Collection of service usage data ..... 35
2.2.9 Exploration of mobile service usage behaviour ..... 35
2.2.10 Information security ..... 36
2.2.11 Social implications ..... 36

2.3 Mobile service usage research using Bayesian network ..... 36
3. Evolution of mobile services in Finland, 1998 - 2019 ..... 39
3.1 Emergence of value-added services ..... 39
3.2 The battle between operating systems ..... 42
3.3 Always on and constantly connected ..... 44
4. Research methods and data ..... 46
4.1 Research methods ..... 46
4.1.1 Consumer behaviour and mobile service usage behaviour ..... 48
4.1.2 Elicitation and documentation of tacit knowledge ..... 51
4.2 Research data ..... 54
4.2.1 Mobile devices' feature and retail sales data ..... 54
4.2.2 Use of mobile services at Aalto University, 2009 - 2010 ..... 57
4.2.3 Use of communication services in Finland in 2011 ..... 58
5. Results ..... 61
5.1 Use of Bayesian networks for data analysis ..... 61
5.2 Trends and structural breaks in mobile device popularity ..... 62
5.3 Classification of mobile services and their users ..... 66
5.3.1 Aalto University community ..... 66
5.3.2 Population of Finland ..... 71
5.4 Risks pertaining to the usage of mobile services ..... 76
5.4.1 Information risks ..... 77
5.4.2 Availability of PSS network ..... 79
5.5 Results summary ..... 81
6. Discussion ..... 84
6.1 Research implications ..... 84
6.2 Practical implications ..... 85
6.3 Methodological implications ..... 86
6.4 Limitations ..... 87
6.5 Further research ..... 88
References ..... 91

# List of Abbreviations and Symbols 





# List of Publications 

This doctoral dissertation consists of a summary and of the following publications which are referred to in the text by their numerals

1. Kekolahti, P. (2011). Using Bayesian belief networks for modelling of communication service provider businesses. $8^{\text {th }}$ Bayesian Modelling Applications Workshop (BMAW-11) in $27^{\text {th }}$ Conference on Uncertainty in Artificial Intelligence (UAI), Barcelona, July 14, 2011, 59-67.
2. Kekolahti, P. and Karikoski, J. (2013). Analysis of Mobile Service Usage Behaviour with Bayesian Belief Networks. J. UCS, 19(3), 325-352.
3. Kekolahti, P., Karikoski, J. and Riikonen, A. (2015). The effect of an individual's age on the perceived importance and usage intensity of communications services-A Bayesian Network analysis. Information Systems Frontiers, 17(6), 1313-1333.
4. Kekolahti, P., Kilkki, K., Hämmäinen, H. and Riikonen, A. (2016). Features as predictors of phone popularity: An analysis of trends and structural breaks. Telematics and Informatics, 33(4), 973-989.
5. Peltola, M. and Kekolahti, P. (2015). Risk Assessment of Public Safety and Security Mobile Service. In 2015 1oth International Conference on Availability, Reliability and Security (ARES), (pp. 351-359). IEEE Xplore Digital Library.
6. Herland, K., Hämmäinen, H., \& Kekolahti, P. (2016). Information Security Risk Assessment of Smartphones using Bayesian Networks. Journal of Cyber Security and Mobility, 4(2-3), 65-86.

# Author's Contribution 

Publication 1: Using Bayesian belief networks for modelling of communication service provider businesses. The author is the sole contributor to this article

Publication 2: Analysis of Mobile Service Usage Behaviour with Bayesian Belief Networks. The idea for this publication was formed by the author who was also the primary author, performed the data analysis and wrote the manuscript excluding the introduction part; Karikoski collected the raw research data, wrote the introduction and reviewed and edited the article.

Publication 3: The effect of an individual's age on the perceived importance and usage intensity of communications services-A Bayesian Network analysis. The idea for this publication was formed by the author, who was also the primary author, performing the data analysis and writing the manuscript. The comments were given by Karikoski and Riikonen, who also reviewed and edited the manuscript.

Publication 4: Features as predictors of phone popularity: An analysis of trends and structural breaks. The idea for this article was formed jointly with Kekolahti, Kilkki, Hämmäinen and Riikonen. The author performed all the data analysis and wrote most of the manuscript. Kilkki wrote chapter 2 and conducted the related literature research. Riikonen pre-processed the research data for data analysis. Kilkki, Hämmäinen and Riikonen provided comments as well as reviewed and edited the manuscript.

Publication 5: Risk Assessment of Public Safety and Security Mobile Service. The idea for using a Bayesian method for the risk analysis was proposed by Kekolahti, who made the sensitivity analysis for the model variables and wrote partly the chapters 2 and 6 . He reviewed the manuscript and edited the text.

Publication 6: Information Security Risk Assessment of Smartphones using Bayesian Networks. The idea for this article was formed jointly between Herland, Hämmäinen and Kekolahti. Kekolahti proposed Bayesian networks method for risk analysis and contributed in finding the experts for the interview process. He gave comments, reviewed the manuscript and edited the text.

# 1. Introduction 

### 1.1 Background and motivation

In his book from 1999, former Microsoft CEO Bill Gates predicted how the digitalized services and information networks of the future would be able to help people and companies in their daily life (Gates, 1999). Within 20 years all the book's services, such as price comparison sites, constant staying in touch and news checking with mobile devices, health care services, on-line payments, personal assistants, home monitoring and social media, are widely used due to the tremendous development of Information and Communication Technology (ICT). However, the adoption time has not been the same for all services. As an example, GPRS adoption, measured as a time gap between the early adopters and early majority (Rogers, 1995, Christensen, 2013) has taken only a few years whereas the time for widening GPS adoption has taken nearly 15 years (Riikonen, 2016). Different technology adoption times are due to a complex relationship between technical and commercial factors, usage experience and the demographic backgrounds of users.

Technology acceptance theories seek to explain the factors for the adoption of new technology. These theories gained popularity in the late 90 and early 2000s, i.e., at the same time when the mobile communication technology made remarkable developments thus providing tools for the innovation process to explain why certain mobile technologies and services may fail and others succeed. Despite the availability of these theories and tools to test the innovations, there are multiple examples in the history of mobile communication, that certain innovations failed (such as WAP service) and some others just came too early to the markets (such as the Club Nokia service).

Multiple technology acceptance theories with slightly different constructs create difficulty to select an appropriate method for studying mobile service usage. In addition, typically these theories have been conceptualized based on opinion data. Recently, complementary and alternative methods have emerged to gain real-time service usage data, not yet possible during the early 2000s, such as to collect the service usage data from the mobile device or from the mobile network. It is also important to understand the complex multilayer structure of mobile communication ecosystem, consisting of network layer and its capabilities, mobile devices using the mobile network, mobile services used by the mobile devices and, finally, service providers providing the services.

The history of statistical theories is long (see e.g., Fienberg, 1992; Pearl, 2009) with an extensive set of available methods (see e.g., Hanushek and Jackson, 2013). Structural Equation Modelling is one example of the methods, applied for causal analysis in mobile service usage research. The recent theory building for the causality and use of graphical models for it by Judea Pearl (e.g., Pearl, 2009; Pearl, 2014; Pearl and Mackenzie, 2018), and others (e.g., Koller and Friedman, 2009; VanderWeele and Shpitser, 2011; Elwert and Winship, 2014; VanderWeele, 2015; Halpner, 2016) have provided an alternative way to analyze the interdependences of variables for causal and predictive modelling purposes.

In addition, software tools and computing platforms have developed during the last ten years enabling complicated and effective data analysis, not possible before (e.g., Bello-Orgaz et al., 2016; Davenport, 2017; Wang et al, 2018; Tiwari et al., 2018; Foote, 2018). The development in methods, computing platforms and tools has contributed also to the emergence of Bayesian networks, first coined by Judea Pearl in 1985 (Pearl, 1985). Its comprehensive mathematical base has been published two decades ago (described e.g. in Pearl, 2009), but proper algorithms, tools and computing platforms for creation and analysis of more complex Bayesian networks have not been available until this decade. Therefore, and despite the benefits provided by Bayesian networks approach (to be discussed later in this thesis), it is not a surprise, that between 1985 and 2018 3600 research papers have been published containing the words "Bayesian network analysis" (Google Scholar 2018), when over the same time period there has been 1.42 million papers containing either "Linear regression analysis", "Logistic regression analysis", "Nonlinear regression analysis" or a combination of them.

The above factors have been the reason for concentrating in this thesis mostly on Bayesian networks as a statistical method and to document proper processes and parameters when analyzing mobile service and device usage behaviour in the complex technology adoption environment. The motivation is to document a Bayesian networks-based analysis process for researchers and practitioners who do not have a deep theoretical knowledge of Bayesian networks, to use for both exploratory and confirmatory analysis. Moreover, the aim is to fill the research gap by providing insights into mobile service and device usage patterns with multiple and different types of variables. The thesis contributes also to the expert knowledge elicitation process, where experts from a knowledge and location point of view are very dispersed. The thesis and the results of the research may be especially significant for academics and practitioners who analyze very complex phenomena in the mobile communication business domain especially when no data exists, the quality of observational data is poor, there are tens or even hundreds of different kinds of variables in observational datasets and when the statistical model should be understandable also for non-statisticians.

# 1.2 Research problem and objectives 

This thesis aims to address a larger research problem (RP) to which the publications give partial solutions. The research problem is as follows:

RP: How can Bayesian networks be utilized to analyze, model and characterize mobile service and device usage?

In this dissertation, a holistic viewpoint on the Bayesian networks was taken, to conceptualize its use for descriptive, predictive and explanatory analysis in the context of different types of datasets and research questions. On a general level, the thesis aims to answer the following research questions:

RQ1: What analytical processes, modelling parameters and tools are feasible for a Bayesian networks modelling approach?
RQ2: How do the features of mobile devices predict their popularity in Finland and what trends and structural breaks are found in the predictivity?
RQ3: How can mobile services, mobile devices and their users be classified based on service usage behaviour?
RQ4: What risks pertain to the availability and usage of mobile services and devices?
The research questions are approached using a variety of data types and amounts, typical in real-world analytical tasks, i.e., surveys from both a small number of dedicated experts as well as from a sample representing the population of Finland, time series data on Finnish mobile handset retail sales and features, and a large amount of real-world service usage data from a small amount of Finnish mobile service users. The scope of the publications is to describe a Bayesian networks modelling process for different research questions, where the complexity and volume of data vary and where the target of the model is either to describe, predict or explain. The research approach is more exploratory than confirmatory analysis.

The publications aim to cover relevant analytical use cases from a mobile service provider's point of view as well as from an academic point of view. Table 1 describes these use cases. RQ1 deals with different perspectives and processes to constructing a Bayesian network for descriptive, predictive and explanatory analysis purposes. In addition, three innovative processes are introduced: (i) description of a novel method to collect domain expert knowledge for constructing a Bayesian network; (ii) an innovative process to construct a temporal Bayesian network from time series data; and (iii) construction of a causal model using temporal data and multiple iterations in Taboo learning. RQ2 deals with the popularity of mobile devices in Finland as a longitudinal analysis. Structural breaks and trends in device features have been analyzed to predict the popularity of mobile device model features over time. The discovered trends and structural breaks are used to explain the changes in the Finnish mobile markets between 2004 and 2013. RQ3 deals with mobile service and device users and usage behaviour based on survey and real-time data. The users, their mobile devices

and the used mobile services are classified based on the discovered usage patterns. In addition, causal dependences between the variables have been studied. RQ4 deals with risk assessment, by adapting a Bayesian network risk management skeleton to handle the risk assessment for both the availability of PSS services under multiple risk triggers and information security risks related to the use of mobile devices and services.

Table 1. Relations of the publications in the research process


# 1.3 Definitions 

To further position the research, key terms and concepts are defined in alphabetical order:
Bayesian networks: a probabilistic model consisting of a qualitative part based on a DAG to indicate the dependencies, and a quantitative part based on local probability distributions to specify the probabilistic relationships between variables.
Bayes' Theorem: a mathematic formula named after 18th-century British mathematician Thomas Bayes, for determining of conditional probability. It provides a way to revise an existing hypothesis given new or additional evidence.
Causal Bayesian networks: an explanatory model which can be used for interventional analysis and where the arcs in the DAG represent causal dependences.
Causality: a connection between two events or states such that one produces or brings about the other (BusinessDictionary, 2019).
Communication service: refers to interpersonal service or application that can be used for remote transmission of voice, data, texts, sound and images between persons.
Communication Service Provider (CSP): a service provider offering telecommunication services or a combination of information and media services,

content, entertainment and applications services over communication networks.
Confounder: refers to a variable that has a causal dependence on two variables, where the other is the target, causing a spurious association.
DAG: Directed Acyclic Graph.
Descriptive analytics: refers to a statistical process used to quantitatively describe or summarize features of data.
Discretization: a process, where continuous numerical values are manually or automatically transferred to discrete representation.
Diversity: in a service usage measurement context the number of different services used by a user during a certain time.
Explanatory analysis: in this thesis refers to a causal explanation and explanatory analysis to the use of statistical models for testing causal explanations.
Feature: in this thesis any characteristic of a mobile device, including its technical features as well as other characteristics, such as manufacturer brand and device sales duration.
Intensity: in a service usage measurement context the number or frequency what certain service is used by a user during a certain time.
Machine learning: a science of getting computers (using algorithms) to act without being explicitly programmed. In a Bayesian networks context using algorithms to construct a DAG.
Mobile application: a computer program designed to run on a mobile device. Also acts as a gateway to the usage of a mobile service.
Mobile device: refers to a small computing device, typically handheld, including both mobile phones and smartphones.
Mobile phone: refers to a traditional phone, capable of only voice calling and text messaging.
Mobile service: refers to service that can be used by a mobile device. In this thesis it refers also to a mobile application.
Model: a simplified representation of some aspects of the real word.
Modelling: the entire process involved for creation of the model, i.e., goal definition, study design, data collection, selection of a statistical method and model quality estimation.
Predictive analytics: refers to a branch of analytics, where historical data (observations) are used to predict unknown events.
Penetration of service or device: the degree to which a device or service is known and/or used (at least once) among a population.
Risk: the probability of some event happening multiplied by the resulting cost or benefit if it does.
Smartphone: a mobile phone with an advanced mobile operating system combining features of a personal computer with other features useful for mobile use.
User: a person who uses mobile device and mobile services.
Usage behaviour: in this thesis refers to usage pattern of mobile service, i.e., how frequently services are used, how much time spent, how many services used, what services used.

# 1.4 Research approach 

The research in this thesis is multidisciplinary as it combines theories, models and technology from mathematics, computer science and social science. The research is both method and user behaviour oriented. In the former the focus is to use Bayesian networks for statistical analysis and to document best practices for different kinds of analytical processes. In the latter the focus is to analyze userlevel patterns related to information technology products and services.
Järvinen (2004) has published a general taxonomy for research procedures (Figure 1). It includes different approaches where each approach can use alternative research methods. The taxonomy is structured as a tree with the leaves being the research approaches.
![img-0.jpeg](img-0.jpeg)

Figure 1. Research approach taxonomy (Järvinen, 2004). Colours indicate the number of publications having this approach: black $=5$, dark grey $=3$, medium grey $=2$, light grey $=1$, white $=0$.

From top down, all research in this thesis belongs to approaches studying reality rather than general mathematical approaches. Within the reality-based path, the studies in this thesis apply various approaches to differing degrees as summarized in Table 2.

Table 2. The relationships between publications and research approaches


In Publication 1, the innovation-building approach is connected to two parts: Firstly, it is related to the proposed method to collect expert opinions from location and knowledge perspectives, a dispersed but large number of experts and

to create a Bayesian network from this data; and secondly, to the usage of Bayesian networks to document the probabilistic nature of CSP business processes. In Publication 2, the conceptual-analytical approach is related to the multiple Bayesian network models constructed in the publication, where the models describe different aspects of mobile service usage behaviour. In Publication 3, the conceptual-analytical approach is related to the constructed Bayesian networks, which model the causal aspects of communication service usage behaviour. Theory testing is related to the comparison of Pearl's do-calculus theory (Pearl, 2009) and Jouffe's Likelihood matching method (Conrady and Jouffe, 2015) for estimation of the strength of causal effect. Innovation-building is related to the used machine learning process to construct a causal Bayesian network. In the process the causal model is achieved through multiple iterations using restricted Taboo learning, expert knowledge and temporal data. In Publication 4, the con-ceptual-analytical approach is related to the models describing factors predicting the popularity of a mobile devices with their features, over time. Innovationbuilding refers to the proposal of using the constructed process as a fast and lightweight method to test mobile device's potential popularity based on the planned features in the model. Finally, in Publications 5 and 6, the conceptualanalytical approach is related to the constructed risk assessment models and innovation-evaluation to the adapted probabilistic risk assessment model skeleton (taxonomy) for the study needs.

# 1.5 Thesis structure 

The structure of the thesis is as follows. After the Introduction, chapter 2 introduces the theoretical background and modelling processes relevant to this thesis and to those researchers and practitioners who does not have strong knowledge about Bayesian networks but are interested to use the method for statistical analysis. Both the theoretical concepts and different analytical processes and relevant practicalities are introduced. Moreover, different mobile service usage study areas are introduced with examples as well as mobile service usage research in those areas especially conducted with Bayesian networks. Chapter 3 is a selective narrative for the evolution of mobile services, networks and devices in Finland. Its target is to serve as background information and potential explanations and as a reference for the actual research and its results. The methods and data utilized in the thesis are introduced in chapter 4. The main results of the thesis including the summary are presented in chapter 5 . Finally, chapter 6 discusses the implications of the results from an academic, as well as from a practical perspective. Also, the limitations of the work and future research items are discussed.

# 2. Theoretical background 

The theoretical background of the thesis is divided into three subsections: Bayesian networks as data analysis method, mobile service usage research approaches and empirical mobile service usage research with Bayesian networks. In the first part, the theoretical background for Bayesian networks is reviewed and the processes for analysis described especially from the point of view of RQ1. The selection of the topics for the first part and their description scope is subjective but based on the author's many years of experience of using Bayesian networks for modelling of real-world problems. The second part provides a selective overview of mobile service usage research approaches with examples. In the third part, empirical research using Bayesian networks for mobile service usage is reviewed.

### 2.1 Bayesian networks

Especially in business analytics literature, statistical modelling is broadly divided based on the use of the results into four categories, namely descriptive, diagnostic, predictive and prescriptive analytics (see e.g., LaValle et al., 2011; Maydon, 2017; Idoine, 2018). According to these authors, descriptive analytics will answer to the question "What happened?", diagnostic to "Why did it happen?", predictive "What will happen?" and prescriptive "How to make it happen?". Conrady and Jouffe (2015) classify the modelling based on the modelling purpose to two main parts, association/correlation-based and causation-based methods. The former is further divided into descriptive and predictive and the latter to explanatory modelling, simulation and optimization. Shmueli (2010) has classified the methods into three types based on how the models are used for theory building and testing: descriptive, predictive and explanatory modelling.

Descriptive analytics creates statistical summaries from data to yield useful information, whereas predictive analytics predicts specific outcomes based on observational data. Diagnostic analytics typically refers to root cause analysis with the capability to isolate confounding variables. In fact, it is the same as explanatory analysis, discussed by Shmueli (2010) and by Conrady \& Jouffe (2015). In Pearl's grouping (Pearl and Mackenzie, 2018) the explanatory modelling belongs either to the intervention or counterfactuals class. As prescriptive modelling seeks to gain insights about what to do next, it is related mostly to

reasoning activity, such as intervention, counterfactuals, simulation and optimization with help of the constructed explanatory model.

In scientific research, methods are often classified based on the research process to exploratory and confirmatory analysis (e.g., Suhr, 2006), where the former prepares the data for further analysis and explores patterns and factors, missing values, outliers, trends and structures from data. The latter helps researcher to test whether the hypothesis about a relationship between the observed variables and their underlying latent constructs exists. The research objectives therefore dictate a proper modelling approach; descriptive, predictive or explanatory. The differences between predictive and explanatory models have not always been clear to the researchers: based on the observations of Shmueli (2010), predictive models are often wrongly used to make causal conclusions.
All three modelling approaches are introduced (descriptive, predictive and explanatory), however the work concentrates solely on using Bayesian networks as an analytical method.

# 2.1.1 What are Bayesian networks? 

A Bayesian network (BN) is also known as Bayes Net, Bayesian Network or Bayesian Belief Network (BBN). This thesis uses the term "Bayesian networks" when discussing in general about the method and models and "a Bayesian network" when discussing about a certain BN model. A Bayesian network is a probabilistic graphical model, where the nodes (vertices) represent random variables $X_{i}$. Each of these variables describes certain amount of research interest. The arcs (edges, links) between the nodes represent either a mathematical, statistical or causal dependency between the nodes. A starting node for an arc is called as a parent and an ending node as a child. The nodes without any parent are sometimes called as a root or an exogenous node and those with a parent as an endogenous node. The structure of a graph is a directed acyclic graph (DAG) where the path starting from node $X_{\mathrm{i}}$ cannot go back to the starting point $X_{i}$. A set of adjacent arcs form a path between the nodes. A node $Z$ in a path $X \rightarrow Z$ $\rightarrow Y$ is called a mediator, in $X \rightarrow Z \leftarrow Y$ a collider and in $X \leftarrow Z \rightarrow Y$ a confounder, see Figure 2. A path is closed (blocked) at a collider and open when conditioning on it.
![img-1.jpeg](img-1.jpeg)

Figure 2. $Z$ is a mediator in (a), collider in (b) and confounder in (c).
The path is open at a mediator and confounder and blocked when conditioning on them. In a DAG, local conditional probabilities for each variable $X_{i}$ are specified as $\mathrm{P}\left(X_{i} \mid \mathrm{pa}\left(X_{i}\right)\right)$, where $\mathrm{pa}\left(X_{i}\right)$ is the parent function. The global joint

probability of a DAG is $\mathrm{P}(X)=\prod_{i=1}^{m} \mathrm{P}\left(X_{i} \mid \mathrm{pa}\left(X_{i}\right)\right)$ (e.g., Pearl, 2009; Koller et al., 2009; Scutari, 2010; Barber, 2012; Elwert \& Winship, 2014; Greenland and Pearl, 2014). Thus, due to the adaptation of chain rule, a Bayesian network is a compact representation of the full joint probability distribution consisting of a product of local conditional probability distributions (CPDs) for each variable given its parents. This feature enables local computations using only a few variables at a time regardless of the number of variables.

Formally, a Bayesian network is a representation of conditional independency, where the arc direction represents probabilistic dependency, which can be applied in inferencing, whereas in causal Bayesian networks (to be discussed later) the arch indicates a causal direction, which can be applied for causal inferencing, simulation and optimization.

Bayesian networks can also be classified based on the structure type into four main groups (Figure 3): Latent variable models, used in Publication 2, Hierarchical Bayesian network models, used also in Publication 2, Dynamic Bayesian models, used in Publication 4 and influence diagrams, used in Publications 1, 3, 5 and 6 (but without utility and decision nodes). Examples of a latent variable model are a Naïve Bayesian network (Figure 3a) and data clustering model (Figure 3b) . In the latent variable model, a Naive structure is created that connects the latent variable to the manifest variables. This model, for instance, can be used for segmentation and prediction. In the Naïve Bayesian network, an over-simplified assumption has been made about conditional independency between the predictor variables given the label (the latent variable in the centre). The Naïve Bayesian network is discussed more in-depth later in this chapter. A Hierarchical Bayesian network is an extension to a standard Bayesian network and is typically created with several construction phases (e.g., Conrady and Jouffe, 2015), where the number represents the depth of the hierarchy. It is in fact a forest of latent variable models, where each hierarchy level consists of one or more latent variable models. The construction process for a Hierarchical Bayesian network is discussed more in subsection 2.1.4. A Dynamic Bayesian network (DBN) is a DAG describing a stochastic process in a discrete time space (Figures 3c and 3e). It is a discrete time model, which describes dynamic processes. A DBN consists of a series of time slices that represent the variables' dimensions at each time slice $t$ and the node transitions between the time slices. It is often assumed, that the structure of a BN does not change between the time slices and then a DBN is a generalization of a Hidden Markov Model (HMM) (see DBN e.g., in Murphy, 2002; Salem et al., 2007; Eldawlatly, 2010). In a first order Markov model only one time slice from the past is needed to predict the next slice. A DBN which needs two time slices is called a 2-TBN. A generalized version is therefore N-TBN. Figure 3e depicts HMM/Kalman Filter structure as a Bayesian network. It is a restricted DBN.

A Bayesian network, especially when it is used for causal reasoning, can be called as influence diagram. Often it refers to a Bayesian network added with

two types of extensions, utility and decision nodes (e.g., Kjaerulff and Madsen, 2008). The former is used to describe the monetary values and the latter to describe decision making alternatives in the model.
![img-2.jpeg](img-2.jpeg)

Figure 3. Example BN model structures. A latent (Naïve) variable model (a), Extension to BN: Hierarchical latent (Naïve) variable model (b), Two-slice temporal BN (2-TBN) (c), Influence diagram, where $X_{0}$ is a decision and $X_{10}$ a utility node (d), Restricted DBN: Kalman Filter/HMM (e).

A DAG represents a qualitative part of a Bayesian network model and the quantitative part comes from the probability function associated with each node. This function can be either non-parametric or parametric. Within nonparametric representation, local probability distributions are multinomial, expressed as conditional probability tables (CPTs), whereas in parametric cases the local distributions are typically Gaussian (e.g. Koller et al., 2009; Barber, 2012). A BN containing only parametric nodes is called conditional linear Gaussian Bayesian network. Also, hybrid BNs consisting of mixture of continuous and discrete variables can be used (see e.g., Neil et al. 2007), when the arch direction is from discrete to continuous variable. Non-parametric models have some advantages and disadvantages over parametric models, discussed in the discretization part of this chapter.

Pearl (Pearl, 1985; Pearl, 2009 p. 14) started to call probabilistic graphical models Bayesian networks due to three reasons. First, the probabilistic inferencing from the graphical model applies Bayes' theorem. Second, the constructed models are based on the subjective nature of input information. Third, this is done in order to distinguish the causal models from evidential models. There are also a fourth reason why graphical probabilistic models can be called Bayesian networks: scoring of machine-learned network structure can be based on MDL/BIC scores (discussed later in this chapter) which is in line with Bayesian thinking. In practise, a Bayesian network is constructed using both a Bayesian probability approach, called as subjective probability due to use of prior be-

liefs, and Frequentist probability approach, using a likelihood function. Bayesian and Frequentist approaches are compared in detail e.g., by Bayarri and Berger (2004).

Another branch of graphical models are undirected graphs and factor graphs. They are not included in Bayesian networks and are therefore not discussed in detail in the thesis. In undirected graphs the relations between two nodes are symmetric. This kind of network can be used to describe communication network topology (e.g. Knight et al., 2012), social networks (e.g. Karikoski and Nelimarkka, 2011) or travel routing (e.g., Kruskal, 1956), for instance. Factor graph is a probabilistic graphical model consisting of two types of nodes, random variables and factors (e.g., Koller et al., 2009). A random variable describes quantitatively an event, whereas a factor is a function of variables and is used to estimate the complex relationships among the variables of interest. Factor graphs are especially useful in inferencing tasks. As a Bayesian network can be converted to a factor graph, it can be used for a fast inferencing feature as part of Bayesian network tools.

# 2.1.2 Properties of Bayesian networks 

Caplin and Schotter (2008) introduced seven properties that a good (economical) model should hold: parsimony, tractability, conceptual insightfulness, generalizability, falsifiability, empirical consistency and predictive precision. Similarly, Anderson et al. (2004) and Verbeke (2012) list the central properties of a good statistical method for inferential analysis: predictive accuracy, comprehensibility, justifiability, capability to handle different kinds of data, overall computational performance, and capability to tolerate poor data. The properties of Bayesian networks as a statistical method and a capability using the above characteristics can be described as follows:

- Predictive accuracy. Based on multiple comparisons of classification methods (e.g., Williams et al., 2006; Lee and Jo, 2010; Jayasurya et al., 2010; Verbeke, 2012; Ducher et al., 2013), the differences arose not only from the algorithm but also from the used datasets and the performance metrics. Regarding the methods alone, no substantial differences were found between the methods and, according to Verbeke (2012) in real-world analysis often the other aspects, such as comprehensibility over black box determines the method of choice.
- Comprehensibility refers to the easy to understand the model construct, e.g., by domain experts who are not statisticians. Bayesian networks represents a so-called white box model, which is easy to understand and interpret due to the DAG structure, compared to some other models, such as Neural Networks or black-box models such as Support Vector Machines.
- Justifiability refers to a possibility to justify the model e.g., by experts. A BN model can be justified by merging a domain expert's views with a machine learned model structure. This is an important feature

when creating causal Bayesian networks (Pearl, 2009; Ryynänen et al., 2018). Justifiability also refers to the possibility to adjust the complexity of the learned structure of a BN model for example with a weighting factor parameter as part of an MDL/BIC scoring algorithm (e.g., Conrady and Jouffe, 2015).

- Capability to handle different kinds of data. A BN model can consist of discrete, continuous, binary, categorical and textual variables or a mixture of them.
- Computational performance. Computationally construction of a BN model can be time consuming, and sometimes practically impossible. An impossible situation arises especially in a non-parametric approach with tens or hundreds of variables, each having multiple parent nodes with multiple discrete states (see e.g., Ismail and Ciesielski, 2003). On the other hand, bi-directional inferencing with the help of the constructed model is fast enabling the inference from causes to consequences (causal reasoning) and from consequences to causes (evidential reasoning) (e.g., Uusitalo, 2007).
- Capacity to tolerate poor data refers to a natural capability of a Bayesian network for probabilistic estimation, e.g., by using the Ex-pectation-Maximization algorithm (EM) for estimating missing values, as part of learning process (Friedman, 1997; Uusitalo, 2007; Conrad and Jouffe, 2015), which increases the usability and quality of the research data.
- Capability to describe causality. According to Pearl and Mackenzie (2018) causal diagrams (causal Bayesian networks) are an intuitive way to communicate existing scientific knowledge about causalities. In addition, the graph enables the interpretation of the type of causality, whether direct or indirect, and helps to estimate potential confounding variables.
- Possibility to learn the model skeleton structure. Distinctive to Bayesian networks is its visual part of the model, the model structure. It can be constructed from observational data by using either unsupervised or supervised machine learning methods.
- Possibility to create BN models without observational data. In addition to learning the structure from observational data, it is possible to construct a Bayesian network without it, i.e., using some knowledge acquisition method from a domain expert(s). Thus, a constructed BN is a documentation of experts' common view about causal relations between the variables of interest.
- Possibility to extend and update the model refers firstly to the possibility to extend a BN with utility and decision nodes (e.g., Ryall and Bramson, 2013) for the construction of visual decision support tools. Secondly, it refers to the possibility to update the model parameters or the whole model with help of new data.
- Complex models are complex also as DAG. When the number of nodes and arcs increase, the comprehensibility of the BN model starts

to decrease. Virtual reality tools have been developed to facility the visualization of a very complex BN model in the 3-D world (e.g., BayesiaLab, 2019)

- Feedback loops. Bayesian networks (due to the acyclic nature of the model structure) used to lack an easy and intuitive way to describe loops, which are useful for example in the modelling of dynamic systems, even the theoretical base as DBN exists. Feedback loops are time-dependent phenomena and therefore they can be modelled with the help of the DBN, but only a few tools have put effort on the usability to describe the loops (e.g., Bayes Server, 2019; GeNIe, 2019).
- Discretization of continuous variables. Even though Bayesian networks can consist of nodes with continuous numerical values, it is common today to discretize them as part of the modelling process, in other words to use a non-parametric modelling approach. Local CPDs are therefore defined as local conditional probability tables (CPTs). Discretization has some benefits and drawbacks for the BN modelling process, which are discussed more in-depth later in this chapter.


# 2.1.3 Subjective probability 

Various probability interpretations exist (e.g., Hájek, 2011), among them the Bayesian probability - often referred to as Subjective probability (Degree of belief) - as well as the Frequency interpretation which has long been and still remains the dominant interpretation of the probability in academic research. As discussed in subsection 2.1.1, there are reasons why directed probabilistic graphical models can be called Bayesian networks, among them the use of Bayes' theorem in the model reasoning.

Often the Bayesian probability approach is compared with the Frequency interpretation, especially in the context of hypothesis testing (e.g., Wagenmakers et al., 2008; Moreno and Girón, 2006; Casella and Berger, 1987). A frequentist estimates the hypothesis as $\mathrm{P}($ data $\mid$ Hypothesis $)$ by using confidence intervals and assumes that the probability of an event is its relative frequency over time and that data originates from controlled experiments. A Bayesian makes the induction from the posteriori distribution $\mathrm{P}(\theta \mid$ data $)$, starting with the priori distribution $\mathrm{P}(\theta)$ before the data is observed and is careful about stipulating assumptions. The role of the prior is to reflect the results from previous studies, researcher intuition, convenience or other data sources. Therefore, it may differ from researcher to researcher and this subjective nature of the prior has been reason for some criticism towards the Bayesian probability interpretation (e.g., Gelman, 2008).

### 2.1.4 Construction of a Bayesian network

There are two main paths for construction, a manual (top-down method) process based on utilizing of domain experts' causal knowledge, when no observational data is available, and the use of machine learning (bottom-up method),

when observational data exists. The latter contains three alternatives: parameter learning for a given (often restricted) structure, a usage of score-based learning and the usage of constraint-based learning algorithms. The output from a manual process is a Bayesian network, which reflects experts' common beliefs about causal relationships and hence this kind of network is often called a Bayesian Belief network (BBN). Parameter learning for a given structure is used either in predictive modelling, when a Naïve structure is applied or in the case a hypothesis, described with a given structure, is tested with observational data. The model constructed with score-based learning is a Bayesian network, where the arch direction describes the probabilistic direction from parents to children. The constraint-based learning process produces a candidate for a causal Bayesian network, and the task of experts is to accept, reject or change the learned model. These construction alternatives are depicted in Figure 4.

The learning process can be divided into two methods, unsupervised and supervised learning processes (e.g., Kantardzic, 2011). In unsupervised learning, the target (label) has not been defined and therefore the constructed Bayesian network can be used either for exploratory analysis (i.e. for knowledge discovery and inference) or hypothesis testing (i.e., for causal analysis and inference). In the supervised learning process, where the learning target (label) has been defined, the structure is often restricted, and the constructed Bayesian network is used more for prediction than for exploratory or hypothesis testing.

# Manual construction of a Bayesian network from domain experts' causal knowledge 

A construction process consists of a set of iterative steps. First, the research target and its high-level dimensions are defined, and those domain experts invited, who have some expertise with regards to the defined dimensions. Second, based on interviews and initial brainstorming sessions, a qualitative Bayesian network is created-i.e., the DAG-part of a BN, concentrating on relevant variables for each dimension and their causal dependences. Sometimes the strength of a causal effect is identified in this phase with symbols, such as positive effects which are denoted by " + ", strongly positive effects by " ++ ", negative effects by " - ", and strongly negative effect as " - - ". Third, a quantitative causal model is constructed by defining in further brainstorming sessions the states for each variable and their conditional probabilities.
The above described process contains multiple difficulties and biases:

- It is not always possible to get the experts together to commonly find the consensus about the model details nor is the expertise evenly distributed for the dimensions as well as between the experts themselves and, hence, the weighting might be needed to evaluate the value of knowledge. Moreover, humans may have difficulty to distinguish direct and indirect relations and they tend to mix deductive and abductive relations (Nadkarni and Shenoy, 2004; Scavarda et al., 2006).
- The manual population of a CPT is time consuming and the effort grows exponentially as the number of parents and their states increase.

- Individual biases in judgement may occur, such as the framing effect, confirmation bias, control illusion bias and overconfidence (e.g., Tversky and Kahneman, 1974; Kotimäki, 2012).
- Group biases in judgement may occur, such as group thinking, polarization and social floating (e.g., Dalkey, 1969; Jones and Roelofsma, 2000).
No commonly agreed scientific process for the model construction exists, leading to multiple proposals, both for the knowledge acquisition process itself and for the completion of CPTs of complex models. Nadkarni and Shenoy (2004) have defined a systematic four-step approach to elicit a non-biased expert knowledge in large scale and to document it as a causal Bayesian network. Scavarda et al. (2006) introduces an inductive Collective Causal Mapping Methodology (CCMM), which collects knowledge asynchronously in three rounds (named as Create, Cluster, Construct) from an expert group which can be geographically dispersed holding many subdisciplines and different views. The output of this process is a document of a group's common causal knowledge as a Bayesian network. CCMM does not use brainstorming but instead adopts a Del-phi-like approach (Dalkey, 1969) and a web-based user interface for collecting and analyzing the data thus eliminating person-to-person interaction related bias. Skaanning (2013) describes an automated approach for a domain-specific knowledge acquisition and documentation as Bayesian networks to be used in troubleshooting tasks. It is based on a single fault assumption, enabling therefore use of tree structures as a BN. US Army documents expert knowledge about the maintenance of complex electronic weapon systems and uses constructed Bayesian network models for real-time fault discovery and corrections (Aebischer and Grimers, 2014). Multiple methods have been developed to help in the population of CPTs such as a weighted sum algorithm by Das (2004), the Noisy-OR and Noisy-AND algorithms (e g., Vomlel, 2006) and the ranked node algorithm by Fenton et al. (2007).

Apart from a Bayesian networks approach, qualitative causal type of information can be collected for business management needs using, for instance, fishbone diagrams (Ishikawa, 1968), strategy maps and balanced scorecard (Kaplan et al., 2004). These methods are not studied in the thesis.

![img-3.jpeg](img-3.jpeg)

Figure 4. Alternative ways to construct a Bayesian network. Score-based structure learning process (grey) produces either a probabilistic or causal Bayesian network. Constraint-based structure learning (green) produces a candidate for a causal Bayesian network. Manual construction (light blue) without statistical data produces a Bayesian (Belief) network which reflects the causal thinking of experts. Parameter learning (cyan) refers to a process, where the structure (causal or not) is given, and target is to estimate local probabilistic dependences between the variables. White colours indicate the pre-processing steps for the observational data.

Pre-processing of data for score- and constraint -based learning
Pre-processing refers to the preparation of the research data for the actual Bayesian modelling phase. Pre-processing is a fundamental step of any data analysis with a target to increase the quality and usability of the data for the actual modelling phase. Analysis based on Bayesian networks uses similar preprocessing methods as any data analysis approach, such as missing data management, data transformation, normalization, dimensionality reduction, outlier detection and resampling, discussed, for example, in (Zhang et al., 2003; Kotsiantis et al., 2006; Kantardzic, 2011). Missing data management and discretization are two of the most broadly used pre-processing tasks and are therefore studied here in more details.

# Missing data management 

There is no consensus regarding the percentage of missing data in the variable or the whole dataset that makes the analysis problematic. Multiple suggestions exist, such as $5 \%$ (Schafer, 1999), 10\% (Bennet, 2001) and 20\% (Peng et al., 2006) from the whole dataset. Tabachnick and Fidell (2007) stated that the missing data mechanisms and the missing data patterns have greater impact on the research results than the proportion of missing data. Missing data mechanisms are categorized as missing at random (MAR), missing completely at random (MCAR) and not missing at random (NMAR) (Rubin, 1976; Tabachnick and Fidell, 2007; Schlomer et al., 2010; Dong and Peng, 2013). Conrady and Jouffe (2015) proposed a fourth type called filtered value (FV), i.e. not applicable or not relevant, which resembles MAR, but which cannot be treated as MAR. Within discrete variables, FV can be treated as new information, for example as an additional state. Researchers typically assume, that the research data is either MCAR or MAR. Conrady and Jouffe (2015) modelled the above four missing data mechanisms as a Bayesian network and with this model proved, that (with an exception of MCAR), deleting of samples with missing values from the dataset is not recommended due to a potential biased mean. Traditionally missing data is handled for example by simple averaging or random draw. This may also create bias in all other cases except for MCAR. Recently principled missing data treatments are proposed especially for MAR -cases (e.g., Schlomer et al., 2010; Dong and Peng, 2013; Lang and Little, 2018). They are, for instance, Multiple Imputation (MI), Full Information Maximum Likelihood (FIML) and Ex-pectation-Maximization (EM). Dong and Peng (2013) tested the principled methods with $20 \%, 40 \%$ and $60 \%$ of missing data, and it can be safely stated that all the tested methods operate well at least with $20 \%$ of missing data. Especially FIML and EM are natural concepts for Bayesian networks, because Bayesian networks are iteratively used for computing the probabilities of the missing values, and therefore no external models and systems are needed to input the missing values.

## Discretization

A Bayesian network can be either a parametric, non-parametric or both. In the first case, the model consists of continuous variables and they can be described with a finite set of parameters, such as assumption about a Gaussian probability distribution with mean and variance and linear relationships between with

variables. In the second case, all variables need to be discrete and no assumptions about their probability distributions are done nor about their dependencies. Parametric modelling (i.e., regression) has some benefits: computationally a structure learning of a Bayesian network is less demanding as only a few parameters are needed compared to non-parametric learning. Therefore, also big and very complex networks (with hundreds of variables) can be learned. The pre-processing is also less demanding, because discretization as a special phase is not needed. On the other hand, there are restrictions, such as the arc direction needs to be from discrete to continuous variables in mixed models, learning works generally well only with variables with Gaussian distribution and not all Bayesian network tools support parametric models.

Due to the above reasons, discretization of continuous variables is very common when using Bayesian networks. The discretization process, i.e., classification, brings some benefits and drawbacks for the BN modelling process and the BN model itself (e.g., Kotsiantis, and Kanellopoulos, 2006; Uusitalo, 2007).

General benefits:

- Multiple machine learning algorithms are available due to the discretization.
- Learning result is often more understandable with a small amount of discretized values compared to parameters such as mean and variance.
- Discretization enables flexible bidirectional inferencing without restrictions between any variables.
- Non-linear dependences can be described.
- When properly discretized, it may lead to improved accuracy in predictive models according to (Elomaa and Rousu, 2004; Lustgarten et al., 2008).


# Drawbacks: 

- Discretization is an extra pre-processing step for the data.
- The proper selection of the number of intervals and their transition points requires expertise and/or dedicated software as typically simple methods do not perform the best (Flores et al., 2011; Conrady and Jouffe, 2015).
- Discretization reduces the arity and a compromise needs to be discovered among the use of the model, information quality and statistical quality (Kotsiantis and Kanellopoulos, 2006).

Discretization reduces a large spectrum of numerical values to a smaller subset of discrete values. Discretization needs two parameters: the number of intervals (bins) and the transition points (cut-off points) for each interval. These parameters are manually or algorithmically defined based on some heuristics. Multiple discretization algorithms exist, discussed for example in (Ismail and Ciesielski, 2003; Kotsiantis and Kanellopoulos, 2006; Flores et al., 2011; Garcia

et al., 2013). These algorithms either define the transition points after the number of intervals has been given or they iteratively define both parameters. A proper number of intervals is dependent on the size of the research dataset and the used minimum number of samples for each interval. Flores et al. (2011) suggests 30 as the minimum sample size for each interval, based on a rule of thumb for statistical inferences defined by Weiss and Hassett (1999). However, Flores et al. did not discuss about model complexity at all. Westland (2010) studied the validity of 10 observations per indicator, which has been a rule of thumb in many management information systems studies. He concluded, that a single heuristic like 'the rule of 10 ' are poor guides to fit to all kinds of circumstances in SEM analysis. The complexity of an SEM model defines the adequate value. As an example of the lack of consensus among the researchers, also five samples per parameter has been proposed for SEM models (Grace et al., 2012). Conrady and Jouffe (2015) highlight the dependency between Bayesian model complexity, the size of research data and the number of samples per CPT cell and propose five samples per CPT cell as an adequate heuristic for practitioners for models with at maximum three parents per child relation. The minimum size of research data should increase exponentially when the number of samples per CPT increases especially and when the complexity of the model increases (measured as number of parents per child):
Size $\geq \mathrm{K}^{\mathrm{p}^{\prime}+1} \mathrm{n}^{\prime}$, where
Size $=$ size of research data as number of samples
$\mathrm{K}=$ number of intervals in a parent and a child variable
$\mathrm{n}^{\prime}=$ number of samples per CPT cell
$\mathrm{p}^{\prime}=$ number of parent variables per child variable
The number of discretizing algorithms is large. For instance, 90 methods were reviewed by Garcia et al. (2013) and one reason for this high number is a strong evolution of classification methods and especially the use of predictive models in research of real-life problems. The discretization methods can be categorized on a high level based on the functionality in the following way (Dougherty et al., 1995; Liu et al., 2002; Kotsiantis and Kanellopoulos, 2006; Flores et al., 2011; Garcia et al., 2013):

- Manual vs algorithmic methods, where in manual methods the transition points are given manually based on some best-practice heuristics.
- Supervised vs unsupervised methods, where supervised methods find optimal transition points given the target variable (i.e., its class information) and unsupervised have no reference variable. As the name indicates, supervised discretization is used in classification-based predictive modelling. Different methods have been devised to use the class information such as Fayyad and Irani's Minimum Entropy Based method, where MDL is used to find a stop criterion (1993) and bottom-up method (see bottomup below), where a Chi-Square statistic is used to test whether two adjacent intervals are independent. Refer to (Lavangnananda and Chattanachot, 2017) for further study about supervised discretization methods.

Traditional Equal Interval Width and Equal Frequency are examples of unsupervised discretizes.

- Direct vs incremental methods, where direct methods define directly the transition points based on the given number of intervals, whereas incremental begins with simple discretization and iteratively increases the discretization until a defined stop criterion has been reached. Equal Interval Width is an example of a direct method and Bottom-up (see bottom-up below) is an example of an incremental method.
- Global vs local methods, where global methods need all the available dataset and does the discretization as a pre-processing step whereas local methods do it on the fly during the model creation phase. Equal Interval Width is an example of a global method. Local methods are often integrated to a classification method or analysis tools, such as the discretizer build in the ID3 decision tree (Quinlan, 2014) or k-means clustering-based discretizer in BayesiaLab (BayesiaLab, 2019).
- Static vs dynamic methods, where dynamic methods search for the transition points using all the variables simultaneously (to capture interdependences) and typically they are integrated to the model learning process thus being local in nature (e.g., Neil et al., 2007), whereas static methods study the transition points independently from other variables. Equal Interval Width is an example of a static method and the above-mentioned ID3 discretizer and k-means -clustering are dynamic methods.
- Top-down and bottom-up methods (splitting vs merging), where topdown starts from one interval, then partitions it to smaller and smaller intervals, until a defined stopping criterion has been researched, whereas bottom-up starts from the maximum potential number of intervals and merges the intervals until a certain stopping criterion has been researched. An example of Top-down method is the Entropy - MDL method (see above supervised methods) and of Bottom-up is the Chi-Square test-based discretizer ChiMerge method, which in merging the intervals iteratively compares the relationship between the values of the variable and the target variable (Kerber, 1992; Lavangnananda and Chattanachot, 2017).
- Univariate vs bivariate vs multivariate methods, where the univariate method does not explore the interdependences, bivariate methods analyze the interdependences between two variables, where the other is a label (i.e., it is a supervised method) and multivariable methods explore simultaneously all variables to define a best transition points altogether or one variable at a time. Therefore, in supervised multivariate methods also conjointly defined patterns can be discovered. An example of univariate methods is the Equal Interval Width, and of bivariate is Fayyad and Irani's Minimum Entropy based method (1993). An example of an unsupervised multivariate method is the Unsupervised Correlation Preserving Discretizer (Mehta et al., 2005) and of the supervised multivariate method is ConMerge (Wang and Liu, 1998).

- Classical vs recent methods, where the recent methods are according to Garcia et al. (2013) those developed during the 2010s, whereas the rest of the methods are classical methods.
The above classification helps to understand the differences in the functionality. More detailed classification in tree format are documented by Garcia et al. (2013) and Liu et al. (2002) from which it is clear, that a certain method may belong to many of the categories documented above.

Properly selected discretization parameters are a compromise between the computational time, understandability of a Bayesian network, how well a Bayesian network describes the underlaying data generating phenomena and how well the model fits the research data. In general, less intervals means better computational performance and model understandability, but decreases the model fitting the research data. In addition, when Bayesian networks are used for predictive modelling, also predictive accuracy and bias-variance need to be considered in the selection of discretization intervals. As an example, within a fixed dataset size, increasing the number of intervals will increase the predictive accuracy (Flores et al., 2011). Intuitively, increasing the number of intervals in predictive models tends to decrease the bias and to increase the variance, whereas decreasing the intervals tends to decrease predictivity, increase bias and decrease the variance.

Based on the reviewed literature and experience of the author using Bayesian networks, especially the BayesiaLab tool, the following guidelines are proposed for researchers for the discretization of continuous variables:

- If the research community is using an existing well-defined number of intervals and transition points for them, then manual discretization can be used.
- Supervised discretization methods are preferred when creating a Bayesian network for predictive modelling.
- Multivariate models are preferred over univariate and bivariate in both supervised and unsupervised modelling approaches.
- Number of intervals and transition points there need to be adapted to the dimensionality of the research data when creating predictive models. Higher dimensionality (i.e. high number of predictors) produces a lower frequency of samples per class label. Here at minimum five samples are proposed.
- Five values per CPT cell can be used as a default value to cover also complex Bayesian networks, where the complexity is at maximum three parents per child and when the size of the dataset varies from 500 to 1000 samples. For larger datasets, a greater number of intervals can be used if computationally it makes sense.
- Discretization with the Equal Interval Width Frequency method produces typically worse accuracy in classification tasks than the other methods and therefore it is not recommended to use them as a general method.

- The Equal Frequency discretizer is recommended only for situations where the distribution of the continuous values is uniform. Otherwise the method creates high bias and additionally is vulnerable to outliers.

Some of the above-mentioned discretization steps are unnecessary if the dynamic discretization is implemented in the tool (such as in AgenaRisk).

# Learning of a Bayesian network 

This chapter focuses on Bayesian networks consisting of discrete variables. However, the principles described below are valid also for Bayesian networks based on parametric models. The learning of a Bayesian network consists of two tasks, learning first the BN structure and learning the parameters. Learning the BN structure means constructing the DAG based on the observational data. The constructed DAG is called a qualitative Bayesian network. There are two main structure learning families, constraint-based learning and score-based learning. Parameter learning consists of estimating the parameters, i.e., local distributions given the constructed DAG. As the whole learning process resembles Bayesian thinking, it can be expressed as
$\mathrm{P}(M \mid D)=\mathrm{P}(G \mid D) \cdot \mathrm{P}(\Theta \mid G, D)$, where $M$ is a Bayesian network, $G$ is the constructed DAG, $D$ is observational data and $\Theta$ are the parameters (in discrete situation CPTs). The learning process is described step by step in following subsections.

## Unsupervised constraint-based learning of a Bayesian network structure

All the algorithms for constraint-based learning use the same theoretical concept defined by Pearl for the Inductive Causation algorithm (IC) (Verma and Pearl, 1991), where the constraints are conditional independence statements. The authors have formally defined with a procedure of d-separation what conditional independence relations should hold in the data if the constructed DAG were true. In addition to IC, multiple other algorithms exist, such as SGS and PC (Spirtes et al., 2000), Grow-Shrink (GS) (Margaritis, 2003), Incremental Association (IAMB) (Tsamardinos et al., 2003) and Max-Min Parents and Children (Tsamardinos et al., 2006). The structure is learned typically in three phases by analyzing first the existence of the arcs (i.e., the skeleton of the model), then the direction of those arcs which form collider structures (V-structures) and finally the direction of the remaining arcs to satisfy the DAG structure. Depending on the algorithms, different statistical methods are used to test conditional independences between the focus variable and the rest of the variables, such as Chi-Square, G-test, Mutual Information, Akaike's information criterion (AIC) and Bayes Factor (Margaritis, 2003; Campos, 2006; Koller et al., 2009; Scutari, 2010; Natori et al., 2015). The amount of conditional independence tests is often reduced to the most relevant variables in order to decrease the computational effort. As an example, a Markov Blanket (e.g., Koller et al., 2009) is used by Margaritis (2003) in GS and by Tsamardinos et al. (2003) in IAMB and Min-Max Hill Climbing.

The resulting model is in theory causal, if the following three assumptions are valid (Spirtes et al., 2000; Margaritis, 2003; Greenland and Pearl, 2014):

- Causal Sufficiency holds: no latent variables exist between the analyzed variable and its parent and the causal structure can be properly represented by a DAG.
- Markov Assumption is valid: In a Bayesian network any variable is independent of all its non-descendants given its parents.
- Faithfulness Condition holds: The observed interdependencies are indeed structural, resulting from the structure of the causal graph, and not accidental, and that graphical separation (when the path is blocked) and probabilistic independence imply each other.

As described by Margaritis (2003) and Natori et al. (2015) with multiple synthetical and real-world datasets, it is not possible in practise to infer fully the causal dependences between the variables. Koski and Noble (2012) demonstrate, that the Faithfulness assumption does not hold in many real-world situations. Therefore, the direction of a few arcs might be wrong, some of the arcs might be missing or some of them might be wrongly identified; therefore, always an expert is needed to accept, reject the model for research needs or finetune it to better meet the expectations about causalities. A general perception has been, that constraint-based learning fits better to causal discovery than score-based learning algorithms. This is also visible in the research of Margaritis (2003). However, CoWell (2001) has demonstrated, that with complete data, having properly (e.g., temporally) ordered nodes and when entropy is used to test conditional independence in a constraint-based method and the same for goodness of fit in score-based method, both approaches produce identical structures. Scutari et al. (2018) compared with simulated and real-world data the reconstruction accuracy of constraint and score-based methods and found, that only with small sample sizes and when confounding factors are eliminated, constraintbased methods outperform score-based methods.

# Unsupervised score-based learning of a Bayesian network structure 

Two components are used in a score-based learning process. The first is a scoring criterion and the second is a search algorithm to identify quickly one or more structures with a high score. The scoring part calculates a score for each Bayesian Network structure candidate found with some heuristic search method. Information theory-related scores are Minimum Description Length (MDL) (Rissanen, 1978; Lam and Bacchus, 1994; Rissanen, 1996; Friedman et al., 1997; Yun and Keong, 2004; Grünwald, 2007), Akaike's information criterion (AIC) (Akaike, 1973; Sober, 2002), Bayesian Information Criterion (BIC) (Konishi and Kitagawa, 2008) and factorized Normalized Maximum Likelihood (fNML) (Silander et al., 2008). The scores are typically in the form of penalized log-likelihood (LL) functions:
$\operatorname{Score}(M, D)=\operatorname{LL}(D \mid M)-\sum_{i=1}^{n} \operatorname{Penalty}\left(X_{i}, M, D\right)$, where $M$ is a Bayesian network including the structure and parameters, $D$ is observational data and $X_{i}$ are the variables in the $M$. MDL can be referred to as a data compression method,

where the most relevant BN is the one that leads to the best compression of the data. Therefore, the best score is the one which minimizes the MDL:
$\operatorname{MDL}(M, D)=\operatorname{DL}(D \mid M)+\operatorname{DL}(G)+\operatorname{DL}(P \mid G)$
where DL denotes description length in bits, $G$ is the DAG-part of $M$ and $P$ is the set of CPTs in an $M$. When the number of arcs in the BN increases, i.e., the Bayesian network structure becomes more complex, the penalty part, $\operatorname{DL}(G)+$ $\operatorname{DL}(P \mid G)$ will increase and $\operatorname{DL}(D \mid M)$ decrease. $\operatorname{DL}(P \mid G)$ can be written in a form of $\frac{\log N}{2} p_{i}$ bits, where $N$ is the number of observations in the dataset, $\frac{\log N}{2}$ is the expected space required to store one probability values in a CPT and $p$ is the number of cells in the CPTs (i.e., number of individual probability values for all variables) (Liu et al., 2012). There are two MDL versions, the original (Rissanen, 1978) two-stage (crude) MDL and the one-stage MDL, proposed also by Rissanen (1996) and optimized for infinite data volumes. BIC is numerically the same as MDL but the penalty part in AIC is only $p_{i}$ which means, that AIC prefers more complex models than MDL. The fNML is in fact a one-stage MDL and the penalty term is called regret, which produces a slightly more complex network than MDL (Silander et al., 2008).
The Bayesian Dirichlet family (BD-family) uses Bayesian scoring, such as the Bayesian Dirichlet equivalence uniform (BDeu) score for discrete data (Heckerman et al., 1995; Silander et al., 2012). It evaluates the structure candidates using their posterior probabilities given the dataset. Liu et al. (2012) demonstrate with real-world data, that in general MDL/BIC outperforms other scoring methods, such as AIC, BDeu and fNML and that fNML fits well for small datasets. K2 scoring together with K2 greedy search belongs to the BD family, proposed by Cooper and Herskovits (1992). It assumes, that the node ordering is known, i.e., the arrow direction is defined in advance. Therefore, if the order is temporal, defined by a domain expert, then the Bayesian network model can be causal. Recently, Scutari (2016 and 2018) and Suzuki (2017) have proposed not to use BDeu at all for structural learning, because it produces constantly too complicated DAGs with a sparse data and might incorrectly propose a variable to the available parent set even the entropy has reached zero. The model usage viewpoint for the score selection, i.e. to predict or to explain, is discussed by Shmueli (2010). He argues that AIC fits better for predictive models, whereas MDL/BIC fits better for explanatory models.

The task of the search algorithm is trying to find effectively (e.g., by reducing the search space) potential structures for good scores, because structural learning has been shown to be NP-hard (e.g., Chickering et al., 1994) both from the running time and memory usage point of view and especially for high-dimensional models. In other words, to calculate the score for all possible structure alternatives is out of the question except for only the most trivial domains. Therefore, a heuristic search is used to find reasonably well scoring structures. In a search some general-purpose methods are applied, such as greedy search or more advanced methods. Greedy search finds iteratively the best arc to add, remove or invert but stops at the first local optimum which might not be the globally the best structure. Examples of greedy search algorithms are Hill

Climbing (e.g., Tsamardinos et al., 2006), Spanning Tree (e.g., Friedman, 1997) and EQ to focus on Equivalent Classes to reduce the search space (Munteanu and Cau, 2000). Advanced search methods try to avoid the problem with local minima. As an example, the Taboo algorithm allows the possibility to eliminate some of them, depending on the size of the Taboo list (Glover, 1990). Also, TwoLevel Simulated Annealing (Wang et al., 2004) is less likely to get tracked at local minima. In addition, multiple hybrid methods have been created to increase the quality of search results and to reduce the computing time: a combination of EQ and Taboo aims to restrict the search space and avoid local minima (BayesiaLab, 2019). Similarly, Max-Min Hill Climbing is a hybrid from structure and score-based learning aimed at increasing computational performance and learning quality (Tsamardinos et al., 2006).

Some learning tools (e.g., Scutari, 2010; BayesiaLab, 2019) enable manual restriction of the search space with a possibility to define the maximum number of parents and/or children, the definition of white and blacklist for arcs and the use of temporal data in learning. These capabilities enable the use of scorebased learning also for causal analysis. The process is documented in Publication 3 and by Ryynänen et al. (2018). In addition to the above classical approximation methods, multiple exact algorithms have evolved recently for learning optimal networks, based on dynamic programming and branch and bound, for instance, discussed in (Koivisto and Sood, 2004; Malone et al., 2011; Malone and Yan, 2014).

# Supervised learning of a Bayesian network structure 

The discovery of the Naïve Bayes classifier (Langley et al., 1992) extended the use of Bayesian networks also for predictive modelling tasks. In supervised models the structure is often restricted for low model complexity and high computational power. As an example, the Naïve structure (see Figure 5a) is fixed, consisting of a common parent (the label in the model) for all the predictors and independence assumption between the predictors. Therefore, a fully Naïve structure needs only parameter learning. Based on the Bayes' theorem, this can be expressed as $\mathrm{P}\left(C_{j} \mid x_{1}, x_{2}, x_{3}, \ldots x_{d}\right) \approx \mathrm{P}\left(x_{1}, x_{2}, x_{3}, \ldots x_{d} \mid C_{j}\right) * \mathrm{P}\left(C_{j}\right)$, and due to the independence assumption, the posteriori can be written as $\mathrm{P}\left(C_{j} \mid X\right) \equiv \mathrm{P}\left(C_{j}\right) \prod_{k=1}^{d} \mathrm{P}\left(x_{k} \mid C_{j}\right)$, where $X=\left\{x_{1}, x_{2}, x_{3}, \ldots x_{d}\right\}$ are a set of predictors and $C$ is a categorical target (label) with potential values $C=\left\{\mathrm{c}_{1}, \mathrm{c}_{2}, \mathrm{c}_{3}, \ldots \mathrm{c}_{\mathrm{d}}\right)$.

![img-4.jpeg](img-4.jpeg)

Figure 5. Examples of restricted Bayesian network structures. Naïve Bayes (a), Tree Augmented Naïve Bayes (b), Augmented Naïve Bayes (c), Augmented Markov Blanket (d).

Multiple extensions exist for the Naïve Bayes classifier (Friedman et al., 1997; Keogh and Pazzani, 1999; Cheng and Greiner, 2001; Jiang et al., 2005). The Tree Augmented Naïve Bayes (TAN) algorithm (Figure 5b) relaxes the assumption of independence of predictors $x_{k}$ given the target variable $C$ but the structure is limited to a maximum of two parents for each $x_{k}$. TAN uses MWST (Pemmaraju and Skiena, 2003, p. 336) for the structure learning and CL algorithm for fitting (Chow and Liu, 1968). TAN was invented originally by Friedman et al. (1997). The CL algorithm finds a tree structure that maximizes the likelihood given the data and therefore actual scoring is not used. However, TAN can be implemented also with a scoring function such as MDL for the structure optimization (e.g., Conrady and Jouffe, 2015). Another Naïve Bayes extension is Augmented Naïve Bayes (ANB) (Figure 5c), which does not have the similar restriction of two parents per predictor as in TAN. Hence, instead of MWST some other greedy search algorithm can be used, such as Taboo. Augmented Markov Blanket (AMB) (Figure 5d) does not produce by default a Naïve structure but can be used for variable selection in supervised learning, especially from high dimensional data.

TAN and ANB outperform Naïve Bayes and C4.5 classifiers (e.g., Friedman et al., 1997; Keogh and Pazzani, 1999; Cheng and Greiner, 2001). Moreover, TAN approximation learns the structure in polynomial time. As indicated by Shmueli (2010), a Bayesian network, learned with unsupervised methods, fits better for exploratory and explanatory analysis whereas supervised structure learning methods are preferred for prediction. This is also visible in (Amancio et al., 2014), where a Bayesian network was the worst method among all studied classifiers. Friedman et al. (1997) got similar results: Models based on TAN and ANB outperformed models based on unsupervised non-Naïve Bayesian networks in classification tasks. In various non-Bayesian specific classification studies, a Naïve Bayesian classifier is typically included in the studied methods, but a non-Naïve Bayesian network model, TAN, ANB or AMB models are more seldom compared with other methods. Based on the analysis of Caruana and Niculescu-Mizil (2006) with 11 datasets, Naive Bayes, Logistic Regression and

Decision Tree are not competitive with the best methods, Random Forest, SVM, Boosted Trees and Neural Nets, whereas Amancio et al. (2014) demonstrate with multiple artificial datasets, that a Naïve Bayes classifier is showing almost equal ranking than all the other classifiers. In addition, the authors propose Naïve Bayes as a preferred method, if the researcher has no prior knowledge of the prediction parameters. Based on comparison of 21 classifier for telecom churn management (Verbeke, 2012), the differences in predictive performance arise from three sources: the used dataset, the used accuracy measurement and the classification method itself. With three measurements, AUC (Area Under ROC Curve) (e.g., Fawcett, 2006), a business-related metrics MP (maximum profit to measure effect of churn management on the revenue) and LIFT (how much better the model does than not using a model at all), a non-Naïve Bayesian network ranking varied from third to sixth best and a Naïve Bayesian network from sixth to thirteenth best among the analyzed 21 methods. Ducher at al. (2013) compared non-Naïve Bayesian network performance with Logistic Regression using clinical data and did not find remarkable differences in predictive performance. Similarly, Jayasurya et al. (2010) compared a non-Naïve Bayesian network with SVM using lung cancer patient data and found a BN slightly better performing than SVM or on par depending on the data. Nor did Williams et al. (2006) find remarkable differences in predictive accuracy between a C4.5 Decision Tree, Naïve Bayes and non-Naïve Bayesian network classification using IP traffic flow data. Narudin et al. (2016) studied the malware detection capability of TAN, Random Forest, kNN, J48 and Multi-layer Perceptron classifiers when using potentially malicious apps and found TAN as the best method measured as AUC.

# Parameter learning 

Parameter learning (parameter estimation) refers to the process where the parameter values (in discrete situation values for each cell of the CPT) are estimated in such a way, that they maximise the likelihood that the model produces the data that was observed. This phase happens for a known structure as a separate phase or is included in the structural learning process. Two approaches are used, based on the Maximum Likelihood estimation (MLE) (e.g., Koller et al., 2009, p. 720) or by using a Bayesian approach, i.e., Maximum Posteriori estimation (MAP) (e.g., Koller et al., 2009, p. 751). In case of discrete data, MLE parameters are computed as a probability of each state in the CPT corresponding to the observed frequency in the dataset. However, this approach is sensitive to small sample sizes and used discretization parameters. MAP is identical to MLE, except the prior acts as a weighting or smoothing factor.

## Some notes about causality

Causal analysis typically tries to find answers to questions such as "why things happen", "what the reasons were", "what if I do...", "how can I make things happen "and "how to control the effect". Causality is defined by Oxford Dictionaries (2019) as "the relationship between cause and effect'. A more detailed definition depends on the viewpoints, i.e., philosophical or statistical, which on the other hand are related to different causal theories. The causal theories can be classified as causal counter-factual, causal probability/potential outcomes, causal

agent-manipulation, and causal process theories (Woodward, 2013). Pearl and Mackenzie (2018) have divided "the ladder of causation" into three levels: Association -related, where the activity is seeing ("what if I see/observe"), intervention -related ("what if I do"), where the activity is intervening and counterfactual -related ("what if I had done"). In a counterfactual approach the activity is to retrospectively analyze the situations, which are counter to the facts, in other words, what did not happen but may have happened. The causal probability theory means that causal influence can be analyzed as probabilistic relations and causality is adapted on an interventional level. In a simple form, causal strength is therefore interpreted as an increase of the probability: event $A$ is a cause of event $B$, if $\mathrm{P}(B \mid A)>\mathrm{P}(B)$. This assumption does not always hold, and a typical example is a spurious correlation due to a confounding variable. Spurious correlation refers to associational relationships (statistical relationships) between two variables without a causal relationship. Additional information on causal theories can be found for example in (Dawid, 2010; Grotzer and Perkins, 2000; Pearl, 2009; Weirich, 2012; Woodward, 2013).

As discussed in the description of a constraint-based learning process, a causal Bayesian network holds, if Causal Sufficiency holds, Markov Assumption is valid, and Faithfulness Condition holds. In addition, the variables in a DAG need to be temporally ordered, meaning that an event in the future cannot cause something in the past. In the above conditions, a causal BN can be thought to consist of a set of do-operators $\operatorname{do}\left(X_{i}=x_{i}\right)$ to describe the active intervention regarding each $X_{i}$ (Pearl, 2009). According to the causal Markov assumption, this intervention cuts all the parental connections to the intervened variable $X_{i}$, thus changing the whole causal BN. The thinking behind this kind of intervention is, that the intervened variable has a certain effect on another variable if and only if the dependency between them would persist under the right sort of manipulation of $X$ (Hagmayer et al., 2007; Pearl, 2009).

Structural Equation Modelling (SEM) has been used as a causal modelling approach in academia already for 45 years (Joreskog and Van Thillo, 1973) to assess statistically the potential causal relations among studied variables. It supports both for confirmatory and exploratory analysis. The question is whether a Bayesian network or a causal Bayesian network can complement or be an alternative approach for SEM. As Bayesian networks represents probabilistic dependencies between parents and children but not causal relations, their usage cannot be an alternative approach for SEM in causal analysis. Gupta and Kim (2008) see Bayesian networks in a customer retention study a complementary method, where the role of SEM is in empirical causal validation and the use of Bayesian networks as a means of complementing the findings with prediction information. Pearl and Mackenzie claim (2018, p 7, 13, 41, 45), that causal diagrams (e.g., causal Bayesian networks) are the most transparent way to summarize and communicate the existing scientific knowledge about causality compared to other causal modelling approaches such as SEM and Propensity Scor-

ing (Propensity scoring, see e.g., Becker and Ichino, 2002). However, this statement does not take a stand on how to construct the diagram. Conrady and Jouffe (2015) claim that the process to construct a hierarchical Bayesian network is an alternative approach to SEM. They refer to it as a Probabilistic Structural Equation Model (PSEM), where the word "probabilistic" highlights the probabilistic nature of a BN. In the simplest form the PSEM is a hierarchical latent Naïve variable model (Figure 3b) but also other than Naïve structures can be used between latent variables. The PSEM construction process is the following.

1. Learn the unsupervised structure using e.g., an MWST search and some score such as MDL to compactly represent the joint probability distribution of all variables for discovering potentially those variables which can be filtered out for further analysis due to low dependence between variables.
2. Cluster the variables by using the constructed BN and some distance metrics between the variables in the network, such as Kullback-Leibler divergence $\left(\mathrm{D}_{\mathrm{KL}}\right)$. Initially all the variables are handled as a separate cluster. Iteratively add the variable with the highest $\mathrm{D}_{\mathrm{KL}}$ to distinct a cluster until a stop criterion, maximum pre-defined cluster size or minimum pre-defined $\mathrm{D}_{\mathrm{KL}}$, has been reached.
3. Find the probability distribution of the latent variable which best fits to the data by using, for example, an EM algorithm. In other words, estimate the marginal distribution of the latent variable with conditional distribution of variables which are part of the cluster, with the EM algorithm.
4. Include a label variable if relevant, use either supervised or unsupervised learning between the latent variables and potential target variable depending on the targets of the analysis. Continue to step 2 until the planned depth for the hierarchy has been reached.
The benefit of a Bayesian network over an SEM structure is the possibility to use it for inferencing. Waal and Yoo (2018) refer to theory-driven Bayesian network construction as PSEM, but refer to the process, where causality is first studied with a traditional SEM approach and then the results are constructed as a BN for inferencing purposes. Publication 3 and Ryynänen et al. (2018) describe a BN construction process, where output is a causal Bayesian network and this process can be considered as another Bayesian network-based alternative approach to SEM.

# Bayesian network software packages 

Software packages for Bayesian networks consist of both commercial and free tools. Commercial tools contain the set of functionalities in one package, from pre-processing to learning and reporting, whereas free tools often are dedicated just to certain functionalities in the form of software libraries, such as structural learning algorithms without any user interface - hence requiring software development capabilities from the researcher. Murphy (2014) has collected a list all available software packages for graphical models including one-time university packages for certain research purposes. This study updates the list (Table 3)

to reflect the 2019 situation and excludes all the packages without any new version or activity during the last ten years. For researches who prefer to create their own analytical processes and to potentially use multiple algorithms, bnlearn based on R and pgmpy based on Python are examples of such packages. Tetrad is an example of tools concentrating on constraint-based algorithms. AgenaRisk (2019), Bayes Server (2019) and Genie (2019) in turn support models based on continuous variables, mixed models and models with fully discrete variables. In addition, the latter two contain an extension to a Bayesian network for the DBN that needs to describe the loops without using discrete time slices. BayesiaLab has an extensive set of discretization methods and learning algorithms and AgenaRisk (AgenaRisk, 2019) supports well (among others) probabilistic risk assessment processes. This dissertation uses commercial tools due to their shorter learning curve compared to software development packages.

Table 3. Software packages for Bayesian networks


# 2.2 Research of mobile service usage 

Mobile service is a service that can be used with a mobile device. In this thesis, also mobile applications are considered as being mobile services. Mobile service usage research contains multiple study themes. These themes are, for example, the conditions for the use and re-use, information security aspects, social implications from the usage, the effects to the business models, technical aspects and explorative analysis of the usage data to provide answer to questions such as

who are the users of mobile services, what services do they use, how and when do they use them and what are their reasons for the usage. Below is a brief summary of the possible research areas. The terms consumer, customer, client and user are often used in these studies. According to the Oxford Dictionary (2019), a consumer is person who purchases goods and services for personal use, and a customer is a person who buys goods or services from a shop or business. Similarly, a client is an organization (sometimes a person) who is using the services. A user is the person, who interacts with the service. The telecommunication industry prefers to use the term customer over consumer, when talking about service usage experience, e.g., quality of service experience, churn and retention probability and customer experience management. Therefore, in this thesis, consumer behaviour refers to the product or service purchase phase, whereas customer experience refers to the service usage phase as a customer of a CSP.

# 2.2.1 Classification of mobile services 

When the number of mobile applications was not as high as today, a general classification of mobile services based on their characteristics was considered a relevant research topic. For instance, Smura et al. (2009) suggest a classification into ten categories based on the nature of interactivity that the applications use and the content of service. Today, both Google and Apple provide a general categorization (Google Play, 2019; Apple App Store, 2019) for their mobile services. As an example, Google categorization consist of 37 main categories and 17 sub-categories for games and 9 for family-related sub-categories. The recent research focus in classification has changed to cover new mobile service areas, such as use case classification of mobile health apps (e.g., Yasini and Marchand, 2015; Olla and Shimskey, 2015), classification of use cases, infrastructure and applications enabled by the Internet of Things (e.g., Smutný, 2016), classification of smart personal assistants (e.g., Knote et al., 2019) and classification of mobile commerce services (e.g., Groß, 2015).

### 2.2.2 Business models

According to Osterwalder and Pigneur (2002), a business model describes how an organization creates, delivers, and captures value. In this, the key role is in product (and service) innovations. The ubiquity of mobile services is perhaps the most important enabler for the innovations which can be exploited in transportation, health care, marketing, news and in the media, for instance. Chapter 3 gives examples of multiple mobile service innovations.

According to the recent Adobe survey (2017), nearly half of marketing deci-sion-makers say their mobile strategy currently contributes to cross-channel, data-driven and customer experience efforts, and roughly third of them say that mobile strategy drives those efforts. Bouwman et al. (2008) give an overview of multiple business model analysis within a mobile context. Publication 1 describes probabilistic business model structures based on Bayesian networks for CSPs. Palatella et al. (2016) describe new business models enabled by Internet

of Things within the 5G network, and Vesselkov et al. (2018) study potential business models for telehealth domain.

# 2.2.3 Usability of mobile services 

It is not a surprise, that due to the importance of the usability in technology acceptance and customer experience models, mobile service (and mobile app) usage is studied also from the usability point of view. Based on ISO 9241-11 (ISO, 2019) usability is the degree of ease with which products such as software can be used to achieve the required goals effectively and efficiently. Usability is also closely related to product functionality. Research areas can vary, being, for instance, the evolution of the user interface in mobile services, the ease of use, satisfaction, learnability, efficiency and new mobile service functionalities enabled by mobile service usage analysis. As an example, Kiljander (2004) studied the evolution of usability and interaction styles enabled by mobile devices. Harrison et al. (2013) reviewed different usability models and created a dedicated usability model for mobile applications. It should be mentioned, that due to the iPhone launch in 2007, the main user interface in mobile apps changed quickly from the old keyboard-driven method to the use of methods based on touch screens and multi-finger gestures (multi-finger gestures, see e.g., Jobs et al., 2009).

### 2.2.4 Technology acceptance

Technology acceptance models describe how individual users accept new technologies. The focus here is on information systems such as mobile networks. Typically, with the help of a selected technology acceptance theory a set of hypotheses is created to explain the phenomenon of interest and research data is collected accordingly to prove the hypothesis. The most used theory is called the Technology Acceptance Model (TAM) (Davis, F.D., 1985). TAM was seen as being too simplistic and extensions to TAM were introduced by Venkatesh and Davis (2000) as TAM2, but it's explanatory power measured as $\mathrm{R}^{2}$ remained nearly the same with TAM according to Samaradiwakara (2014). There are multiple other technology adaptation theories, such as the Theory of Reasoned Action (TRA) and a successor of TRA, the Theory of Planned Behaviour (TPB) (see e.g., Madden, T. J., 1992). The aim of the Unified Theory of Acceptance and Use of Technology (UTAUT) is to merge all the previous theories into one (Venkatesh, V. et al., 2003). UTAUT has the best $\mathrm{R}^{2}$ performance among all the technology acceptance theories according to Samaradiwakara (2014). As seen from Figure 6, UTAUT stresses the moderating role of gender, age, experience and voluntary in usage behaviour. As an example, Koivumäki et al. (2008) studied with a UTAUT construct how willing people are to try new mobile services. Verkasalo et al. (2010) used extended TAM to study drivers for intention to use the mobile services, and Mortimer et al. (2015) used an extended TAM model to investigate how mobile banking services are adapted in Asia and what are the primary determinants in the adaptation.

![img-5.jpeg](img-5.jpeg)

Figure 6. Unified Theory of Acceptance and Use of Technology (UTAUT).

# 2.2.5 Diffusion of innovation 

Diffusion of innovation (DOI), such as a mobile service, belongs also to technology acceptance theories but is used more on a market level to describe how new innovations spread as a function of time and what are the reasons for the spread (Rogers, 1995). Key components are the innovation, communication channels, time, and a social system. As an example, Kivi (2011) described the diffusion of mobile internet services over time in Finland and Riikonen et al. (2013) compared the diffusion patterns of 15 mobile handset features in Finland between 2005 and 2010.

### 2.2.6 Consumer behaviour

Marketing research uses multiple theories and scopes to describe how consumers feel, consider and select services, what are their intention to buy and how the purchase decisions are made. In a similar way to the technology acceptance theories, consumer behaviour models can be used to confirm or reject hypothesis related to service selection. Consumer utility maximization theory, for instance, describes the probability that a consumer chooses certain type of a service, maximizing the expected utility, which depends on the service characteristics, marketing activities, monetary restrictions, time and non-observational and error components (e.g., Jun and Park, 1999; Kim et al., 2005). Teng et al. (2005), for instance, demonstrated that the perceived utility of new mobile services was a key factor that resulted in mass adoption of 3 G mobile devices.

Another approach is to use loyalty-centric models (Dick and Basu, 1994; Oliver, 1999; Reichheld, 2003; Kuusik, 2007). Loyalty as a latent factor is sometimes treated as behaviour (such as repeated purchase probability) and at other times as an attitude (such as commitment). Therefore, it is measured, for example, as continuous use of services, intention to buy, retention probability and recommendation rate. The conceptual model of Dick and Basu (1994) is used for many simplified constructs. For example, Perceived Value, Trust, Satisfaction, Habit and Loyalty were used by Lin and Wang (2006) in their study of factors affecting the repeated purchase intention in a mobile commerce context. Similarly, Switching Costs, Satisfaction, Loyalty and Retention Probability

construct was used by Lee et al. (2001) in their study regarding the preferred usage of French mobile services.

Especially in mature markets, the research focus in product and service purchase behaviour analysis can be the understanding of the difference between utilitarian (perceived ease of use and usefulness) and hedonic (entertainment and aesthetics) benefits for consumers (e.g., Chitturi et al., 2008). Petruzzellis (2010) has adopted this approach for mobile device choice analysis, and Kim and Hwang (2012) have analyzed mobile service experience from both the hedonic and utilitarian value perspectives.

# 2.2.7 Customer experience 

Customer experience is a marketing term widely used by CSPs to describe the mobile service usage experience of their customers. As it is often measured as satisfaction and loyalty metrics, listed above, it belongs to the consumer behaviour model, but the focus is more on the experience, originated from the usage of the services through sensorial, emotional, cognitive, pragmatic, lifestyle and relational factors (e.g., Gentile et al, 2007). As an example of a customer experience study related to mobile network and services, Kilkki and Finley (2019) shed light to the importance of Quality of Service (QoS) and Quality of Experience (QoE) for the CSP business through user experience when interacting with the services and as customer who has bought the services.

### 2.2.8 Collection of service usage data

In this field of research, the characteristics of data collection methods are studied. The research focus may be, for instance, data sources and technology used for collection, data types and their attributes, research scopes enabled by data, data ownership, privacy and data quality (e.g., Kivi, 2007; Verkasalo and Hämmäinen, 2007; Smura et al., 2011). A growing branch of research is automated data collection through sensors for specific mobile application needs and, in general, context-aware mobile computing (Gajjar, 2017). It is also worth emphasizing that nowadays the Android operating system supports 13 different sensors (Android, 2019).

### 2.2.9 Exploration of mobile service usage behaviour

This field of research studies mobile service usage from users' perspective and consists of multiple themes, such as study about mobile service usage intensity versus diversity, service usage behaviour within some selected context, like time of day and place (home, office, abroad) (e.g., Soikkeli et al., 2011; Karikoski and Soikkeli, 2013), social relations and demographics as well as technical aspects such as physical dimensions of the mobile device and its features (e.g., Finley and Soikkeli 2017;). Another branch of study is to characterize mobile service

users based on their service usage behaviour and the used mobile devices, studied e.g., in Publications 2 and 3. Mobile service usage behaviour can be studied also using the diffusion of innovation of Rogers (1995). A typical study focus is then to find factors for usage behaviour within innovators and early adopters (e.g., Lee, 2014).

# 2.2.10 Information security 

Information security is an extensive theme. Many textbooks, including (Rhodes-Ousley 2013) provide further background to the whole theme. Typical mobile service usage related research interests are privacy management when using ad-supported mobile applications (e.g., Leontiadis, 2012), analysis of the threads and management of information risks (e.g., Publication 6; He et al., 2015). The claims about misuse of the collected information when using social media services such as Facebook (see e.g., The Guardian, 2018) have raised the research interest to the protection of privacy when using social media services (e.g., Isaak and Hanna, 2018). Information security can be part of the antecedents also in technology acceptance models.

### 2.2.11 Social implications

Studies about social implications originating from the usage of mobile technologies and mobile services cover research topics, such as assessment of the availability of the mobile services, changes in social relationships (e.g., Seo et al., 2016; Misra et al., 2016), and the effect of using of mobile services on subjective well-being and social capital (Chan, 2015).

### 2.3 Mobile service usage research using Bayesian network

Based on the recent literature review done by the author, 50 research papers were found (Table 4), that can be placed in the research areas defined in subsection 2.2 and which fulfil the subjective scoring, defined by the author based on his experience. As a scoring, at minimum (indicated with one black dot), the study needs to use one mobile service data (such as SMS or voice call), at least one Bayesian network must be applied (such as Naïve Bayes), and the DAG structure or related theory should be described in the paper. A research paper with three dots uses multiple Bayesian network methods, multiple data sources - including real-time data - and the theory is described in detail. Naïve Bayes is the most popular method in the studies according to Table 4. One reason for this is that it is included in almost all statistical tools. Even though TAN outperforms NB, it is much less used in predictive analysis. Manual construction of a Bayesian network has been used more in older papers compared to machine learned methods. Surprisingly, only two papers have been discovered, which use constraint-based model construction although there are multiple methods and strong theory behind, as discussed in chapter 2. Altogether 25 papers use Naïve Bayes, TAN or related method for prediction. The rest of the models are Bayes-

ian networks or causal Bayesian networks, which are non-restricted and according to chapter 2.1.4 fit better for explanatory than predictive analysis. However, in some of the papers a Bayesian network model is used for predictive analysis (e.g., Li et al., 2016; Erman and Yiu, 2016; Jung, 2019) and, therefore, ultimately in 22 papers the focus is on causal analysis rather than prediction.

The three most popular research categories are usability of mobile services, information security and customer experience analysis. In the 2010s, the research topic has changed from basic Naïve Bayes-based classification analysis, such as churn prediction, spam filtering and recommendation systems to more complicated models covering e.g., automatic context aware recommendation solutions, health care topics and dedicated information risk prevention (such as prevention of smishing - fraudulent messages sent over SMS). Interestingly, based on Table 4, only one mobile service usage study applying Bayesian network originates from Finland, although there are numerous methodological Bayesian network studies from Finland that are of merit (e.g., Myllymäki et al., 2002; Silander et al., 2008; Koski and Noble, 2012). This was during the time that Finland used to have a strong mobile service, device and network development activities thanks to Nokia and active CSPs. Based on the Table 4, 15 from 50 papers originated from South Korea.

# Theoretical background

## Table 4. Mobile service usage studies that apply Bayesian network method

scoring of
the paper | The study paper | Location of
the study | Sum  |
based
learning |  |  |  |  |  |  |   |
|  2.2.1
Classification of
mobile services |  |  |  |  |  |  |  | Android App classification: for warning
about risky apps |  | Oshidova et al., 2017) | France  |
influenced traffic |  | (Aseto et al., 2017) | Italy  |
in mobile device |  | (Paddan et al., 2015; Single
et al., 2018) | USA; South
Korea  |
|  2.2.2 Business
models |  |  |  |  |  |  |  |  |  |  | 0  |
recommender |  | Park et al., 2007) | South Korea  |
recommender and news recommender |  | (Hwang and Cho, 2009; | South Korea  |
activity) and sharing |  | Park et al., 2011) | South Korea  |
and spatial context data |  | Lee and Cho, 2011; Lee
and Cho, 2012) | South Korea;
South Korea  |
recognize depression |  | Chang et al., 2015) | Taiwan  |
|  2.2.3 Usability
of mobile
services |  |  |  |  |  | X | X | Mobile Health care Assistant |  | (Hammarsam et al., 2015; | Netherlands;  |
device) referencing solution from
sensors for context-aware app
development |  | (Korpiyük et al., 2003; Noh
et al., 2012) | Finland; South
Korea  |
based on context-aware device
management |  | Cho and Yu, 2019) | South Korea  |
school-life, activity): referencing
solution from sensors for context
aware life management app
development |  | (Hwang and Cho, 2009; | South Korea;  |
Technology
acceptance |  |  |  | X |  |  |  | Analysis of key access factors in mobile
games |  | Park and Kim, 2013) | South Korea  |
acceptance model |  | (Garces et al., 2016) | France  |
sharing networks |  | Nguyen et al., 2007) | France  |
|  2.2.5 Diffusion
of innovation |  |  |  | X |  |  |  | Modelling of adaptation of smart TV |  | Bae and Chang, 2012) | South Korea  |
|  2.26 Consumer
behaviour |  |  |  | X |  |  |  | Individual and cluster behaviour
analysis from mobile data |  | Zheng and Ni, 2012) | China  |
RFID data |  | Cioi and Yada, 2013) | Japan  |
experience | KANN |  |  |  |  | XXX |  | C0P customer churn prediction |  | (Verbeke et al., 2012; | Belgium;  |
al., 2013; Gallagher and | Ireland; China;  |
prediction |  | Lee and Jo, 2010) | South Korea  |
mobile environment |  | Mitra et al., 2015) | Australia  |
|  2.2.8 Collection
of service usage
data |  |  |  |  |  |  | X | Collection of sparse mobile data based
on crowdsensing |  | (Wang et al., 2016) | France  |
based on use of mobile apps and
services |  | Yu and Chen, 2006) | China  |
is going to use |  | Baeza-Yates et al., 2015) | Spain  |
|  2.2.9
Reploration of
mobile service
usage | X |  |  |  |  |  |  | Classification of Twitter data |  | Chang et al., 2012) | USA  |
Facebook's data |  | (Noulac et al., 2013) | USA  |
capacity based on mobile service
usage data |  | Shin et al., 2009) | South Korea  |
on previous usage data |  | Huang et al., 2012b; Shin
et al., 2012) | USA; USA  |
environment |  | Li et al., 2016) | U.S.  |
Information
security |  | X |  |  |  |  |  | Malware filtering |  | (Benedict et al., 2016) | Malaysia  |
services |  | Kubari et al., 2016) | Nigeria  |
human behaviour prediction |  | (Bassett, 2016) | USA  |
recognition |  | Klein, 2016) | USA  |
implications |  |  |  | X |  |  |  | Predicting mobile device dependence
and exercise use within young people |  | Jung, 2019) | South Korea  |

# 3. Evolution of mobile services in Finland, 1998 - 2019 

This chapter is a selective narrative for the evolution of mobile services, networks and devices in Finland. Its target is to serve as background information, a reference and offer potential explanations for the actual research and its results. The focus is on timelines that are important landmarks in the history of Finnish mobile services. Most of the statistics related to penetration distributions for mobile device models and their features as well as unit sales are calculated from the same GfK dataset that was used in Publication 4.

Penetration of sold 2G Mobile devices started to increase from 1991 onwards, reaching a $60 \%$-level in Finland during 1998/1999 (ITU, 2018). On the other hand, in 1998 and 1999 multiple value-added services were introduced and therefore 1998 could be considered as an entry to value-added mobile services in Finland and the starting point for this narrative. The studied time period from 1998 to 2019 has been divided into three phases:

- Emergence of value-added services, extending from 1998 to 2006
- The market share battle between operating systems, extending from 2007 to 2013
- Always on and constantly connected, extending from 2014 to 2019


### 3.1 Emergence of value-added services

Calling and SMS were the mobile services in 1999 for the masses. It is reasonable to assume, that popular phone models such as the Nokia 3210, first sold in 1999 and marketed for young people, and its successor the Nokia 3310, first sold in 2000 (The Telegraph, 2017), positively affected usage intensity of the SMS service. In addition, the Nokia 3210 motivated users to send pre-installed images (e.g., Happy Birthday images). Similarly to the way that the Nokia 3210 and 3310 educated users in Finland to use mobile calling and specially to send SMS messages, the same happened with the Nokia 1100 (first sold in 2003, the most sold mobile phone of all time) and its successor the Nokia 1110 (first sold in 2005, the second most sold phone of all time) in developing countries.

Many value-added services were introduced in the late 1990s and the beginning of the 2000s, but it took often more than ten years before their penetration as part of the devices sold exceeded $50 \%$. As an example, business phones, such

as the Nokia Communicator 9110 (first sold in 1998), Ericsson R380 (first sold in 2000) and RIM's Blackberry 5810 (first sold in 2003) contained by default a large screen and multiple value-added services: internet browsing, email, calendar and fax. However, it took 14 years until the penetration of email-service as part of yearly sold mobile devices reached $85 \%$. R380 contained a touch screenbased user interface, but it was only in 2012, i.e., 13 years later, when a touch screen was a preferred user interface in new sold mobile devices in Finland. GPS service was first announced by Benefon with its ESC! device (first sold in 2000) and 13 years later GPS capability reached $71 \%$ penetration in new devices. The Nokia 7110 (first sold in 1999) was the first Nokia device with WAP internet browsing capabilities, a key enabler at that time for interactive mobile data services.
In addition to CSPs, also ICT companies and Nokia started in 1999 to develop and test value-added services based on the Nokia 7110 and the Benefon ESC!, such as location services (local weather and traffic reports, identification of location of emergency and transport vehicles), electronic transaction services, such as banking and on-line shopping, mobile learning and multimedia services, such as music and video streaming and image exchange (e.g., Radiolinja, 2000). However, WAP-based services never became commercially successful and the initial reason was a poorly perceived ease to use according to Kiili (2002).

After SMS, the next commercially successful value-added service in Finland was a service called Jukebox, which enabled users to create ringing tones and download them to their mobile devices using OTA transfer based on the SMS service. It was developed by Yomi Media and offered first by Radiolinja in 1998 for its customers (Hakkarainen, 2010). Downloadable ringing tones became quickly very popular and in five years global sales of ringing tones exceeded $\$ 2$ billion (Mehta, 2005). Also, mobile device manufacturers started to offer valueadded services in the early 2000s, and the first of this kind of service platform was Club Nokia, later called Ovi Store and Nokia Store (Osterwalder and Pigneur, 2003). Its worldwide launch was in 2001. It was intended to act as an information and sales channel between Nokia and its customers. Initially it acted as a platform for downloadable ringing tones, images, games and user manuals.

The launch of the 2 G extensions GPRS (2.5G) and EDGE (2.75G) took place in 2001 and 2003 in Finland, enabling data transfer of max. $114 \mathrm{~kb} / \mathrm{s}$ for GPRS and $474 \mathrm{~kb} / \mathrm{s}$ for EDGE (Halonen et al., 2004). These technologies were facilitators for multiple value-added services, such as MMS, internet browsing, multimedia services and business services. A camera as part of a mobile device became popular in the 2000s. The penetration among mobile devices sold was zero in 1998 - 2000, but already 17\% in 2003 and reached 83\% in 2006/2007. A similar trend happened at the same time in the number of colours and resolution of the display (e.g., Kivi et al., 2009), which improved the usability of the mobile device as an imaging device (Kiljander, 2004). On the other hand, at the

same time the display size remained small, being on the average 1.6 inches in device models sold in 2003 and 2.0 inches in 2007. This restricted the usage of captured images mostly to MMS.

The leading Finnish CSPs of the time; Radiolinja and Sonera launched a 384 Kbit/sec 3G network late in 2004 (Radiolinja, 2004; Sonera, 2004), which initially covered $20 \%$ of the Finnish population (Liikenne- ja Viestintäministeriö, 2005). On the other hand, only Nokia's 6630 and 7600 with an unusual teardrop shape supported WCDMA technology by the end of 2004. By 2007, the penetration of WCDMA in sold device models increased to $35.4 \%$ and HSDPA to $9.5 \%$. The usage of mobile services over 3 G networks did not depend only on the coverage of the 3 G network or availability of 3 G support in the mobile devices, but also on the pricing scheme for 3 G connections, the existence of the use cases which required a 3 G connection but also positive attitude towards 3 G . As an example, opinion among some of operators was in 2004, that "Finland does not need 3 G " and a typical use case was seen a possibility for large attachments in emails (Talouselämä, 2004). In 2005, the pricing scheme for valueadded services was based on a fixed monthly price with typically a 20 or 100 Mbits usage limit plus additional fees for exceeding that limit (Liikenne- ja Viestintäministeriö2, 2005; Liikenne-ja Viestintäministeriö3, 2006), which did not motivate users to use data driven services in large scale, and therefore the attitude towards 3 G data services among consumers remained negative until 2006 according to the leading Finnish business newspaper, Talouselämä (2006). For the first time in 2006/2007 CSPs started to offer, in addition to usage-based pricing, also speed level pricing without data volume limits. As an example, Elisa announced in 2006, that all of its 3G network could reach a maximum $1 \mathrm{Mbit} / \mathrm{sec}$ speed based on HSDPA (Digitoday, 2006). Therefore, the turn of the year 2006/2007 - with new pricing schemes for value-added services and at the same time a 3 G network with increased coverage - can be considered as an important milestone in the usage intensity of value-added services in Finland.

In the early 2000s, the mobile devices were mostly bought from CSPs and therefore they saw Club Nokia as an attempt to take over the relationship with their customers with ringing tones and other value-added services (The Economist, 2008). This supposedly was one reason why Club Nokia never became a general-purpose source for value-added services during its seven years lifetime. Another reason was Nokia's hardware-driven feature strategy, where special devices with special user interface and their own account management systems for different mobile services were created. Examples of these were the Nokia 3250 and $52 \mathrm{xx}-58 \mathrm{xx}$ Xpress music phones in the mid-2000s with their own music download platform and account management system, the Nokia N-Gage devices with their own special keyboard and N-Gage gaming service platform, the free Smart2Go (Digitoday, 2007) GPS service, supported in selected models (e.g., Nseries devices) from 2007 onwards, dedicated camera phones, such as the 7650

in 2002, N90 in 2005 and N73 in 2006 as well as dedicated business phones with their own accounts for email and calendars.

# 3.2 The battle between operating systems 

The seven years period from 2007 to 2013 can be called as a battle between operating systems. It started, when Apple announced the launch of the iPhone and ended, when Nokia sold its mobile device business to Microsoft in 2013.
The capacity of mobile devices improved dramatically towards 2013, enabling the usage of services not possible before. On average in 2007 the memory size was 66 kB , storage size 0.2 GB with a 270 MHz 1 core processor, whereas in 2013 the memory size had increased on average to $0,8 \mathrm{MB}$, the storage size to 6.7 GB and the processor speed to 1150 MHz with two cores. Also, the switch in the user interface from keyboard to touch screen took place during this period (penetration of touch screen in the models sold in Finland was 5.5\% in 2007 versus $72 \%$ in 2013). The display size increased on average from 2 inches in 2007 to 3.5 inches in 2013. All these advances were enablers for usage of Inter-net-based services, such as social media services, Instant messaging and OTT media services. The capacity and coverage of the 3 G mobile network increased, reaching about $70 \%$ of the Finnish population in 2009 (Smura et al., 2011) and the use of 4 G networks started first in 2010 in Helsinki (Radiolinja) and Turku (Sonera), offering up to speeds of 100 Mbits extending to other cities later in 2012. It is reasonable to assume, that by 2013 mobile devices started to be a viable alternative to traditional PCs for use of Internet-based services, such as news reading, surfing, video watching and social media services.

However, the most profound changes took place in the mobile device markets in Finland during this period. According to Figure 7, Nokia represented about $40 \%$ of all the sold mobile device models in Finland during 2007 - 2009. They used a traditional hardware-driven way to manage the features for different user segments, in fact what they followed throughout the whole of the 2000s - and what Apple and Google started to challenge in 2007 - 2008 with their softwaredriven mobile device model approach. In it the differences between the models are mainly due to performance and the physical features of the devices. In addition, for example in 2009, four different operating systems were used in 119 Nokia models with multiple fragments of Symbian. This most probably created additional difficulties to manage the portfolio. The penetration of smartphones increased initially slowly in Finland, from 6\% in 2005 to $16.7 \%$ in 2009, but started to grow strongly thereafter reaching the $70 \%$ level in 2013 among all the models that were sold at that time. Symbian was a dominant operating system in smartphones as late as in 2009 with a $43 \%$ share, but already in 2011 there were 68 Android-based smartphones from six manufacturers compared to 31 Symbian models from two manufacturers.

![img-6.jpeg](img-6.jpeg)

Figure 7. Model and unit sales of mobile devices in Finland between 2005 and 2013.
Even more clearly Nokia's dominance in Finland was visible in the number of device units that were sold, as seen from Figure 7. Still in 2011, when Nokia announced to terminate the manufacturing of Meego and Symbian devices and to use Microsoft Windows instead, the overall unit sales of Nokia devices was far higher than its rivals. Also, the unit sales of Symbian devices were higher than the aggregated unit sales of Android, Windows and IOS sales. The turning point was in 2012: 1) For the first time in Finnish history other manufacturers sold more mobile devices than Nokia; 2) the unit sales of mobile phones was less than the sales of smartphones, and; 3) the aggregated sales of Symbian and Windows was less than the aggregated sales of Android and IOS devices.

Popular social media and OTT services entered always first to Android and IOS devices and often much later to Symbian and Windows-devices which increased the popularity of these devices among the users. As an example, mobile versions of YouTube, Gmail, WhatsApp and Google Maps were available in Android and IOS in 2009, Twitter and Netflix in 2010, Facebook Messenger in 2011, Instagram in 2012 and Facebook Home in 2013. In September 2013, Nokia announced that it had sold its entire mobile device business to Microsoft.

# 3.3 Always on and constantly connected 

Apple in 2007 and Google in 2008 entered into the global mobile device and services markets with a business model, where the value-added services are developed mostly by third parties. They use the service development platforms and processes centrally developed and maintained by Apple and Google for productizing, marketing and downloading the services. Both Apple's App Store and Google Play were established in 2008. They provide certain global services for the platform, such as search, maps, email, entertainment and payment services, what third parties can benefit from in their services.

The number of apps in the application stores started to grow rapidly from 2009 onwards, as seen from Figure 8. In 2011, Apple's App Store and Google's Google Play contained already above 300,000 apps divided into 22 (Apple) and 34 (Google) categories. As a comparison, Nokia's Ovi Store exceeded at the same time 40,000 apps, but due to multiple operating systems and device models, the actual number was much less (ComputerWorld, 2011).
![img-7.jpeg](img-7.jpeg)

Figure 8. Number of apps in Apple's App Store (IOS) and Google's Google Play (Android) (Statista 2018). The numbers vary within a single year and are therefore indicative. IOS numbers are from July and Android number from June, July or August depending on the data availability.

The usage of social media services from mobile devices contributed to the always on and constantly connected type of service usage behaviour. The number of available social media services has increased from a handful in 2013 to 60 services to cover a user's everyday life situation and location (Social Media, 2018). Internet has become a global marketing tool (e.g., Lamberton and Stephen, 2016), where a user's location and service usage behavioural data are collected, and this information is exploited with the help of analytics in personalized advertisement (e.g., Health, 2014; Wedel and Kannan, 2016). The real-time electronic-word-of mouth (e-WOM) possibility with a mobile device has shaped the travelling business, for instance (e.g., Filieri and McLeay, 2014; Huete-Alcocer, 2017). A smartphone has become the most popular camera with an $85 \%$ share of all the 1.2 trillion photos taken in 2017 (Statista, 2017). This is not a surprise due to the camera's ease of use, the reasonable high photo quality, the instant possibility to share the memories, the possibility to use the camera for

visual search and for taking notes and the possibility to extract text from a photo. The capability to combine local views from camera, GPS-location, maps and virtual scenes to create augmented reality has recently enabled new types of popular games, such as Pokémon Go, Ingress and the Walking Dead: Our World (Althoff et al., 2016; Mihale-Wilson et al., 2018). Use of mobile banking and payment services are gradually increasing. For instance, Nordea (Nordea, 2018) prefer mobile banking over browser-based connections. On the other hand, mobile payment in 2017 has been still rather marginal in Finland: Only $6 \%$ of consumers had used mobile payment during the previous month according to Deloitte (2017).

During the last few years the role of mobile devices has extended to the health care area, where the devices can proactively control its user's wellbeing with the help of internal and external sensors and may propose actions. As an example, the Apple Watch Series 4 has two electrocardiogram apps designed to catch irregular heart rhythms which may be a sign of serious heart risks. These kinds of devices can be used to predict whether the wearer has fallen and in case hasn't moved for a while, the device can call automatically for help (e.g., Charani et al., 2014; Zhang, 2015; Machado et al., 2017; Karmen et al., 2019). Today mobile devices are part of everyday human life, they are always on and connected and are used for multiple everyday activities (Deloitte, 2017; Adobe, 2017). The shape and size of a smartphone has stabilized to a rectangular form, where the target is a large screen in a small device, and which can be controlled with one hand.

When, on average, the size of new smartphones sold in Finland in 2013 was 4 inches, in 2018 the most popular category was from 5.5 to 6 inches. It is expected that this size category will stay as the most popular size also during the next four years (Statista, 2018). However, new foldable display technologies are emerging and may bring along new use cases especially with the help of 5 G networks and the Internet of Things. In the end of 2018, the market share of IOS mobile devices in Finland was $30.4 \%$ and Android 68.4\% (Statcounter, 2018). One of the new Android manufacturers is HMD Global, which exploits Nokia brand in saturated smartphone markets (Shah et al., 2018).

# 4. Research methods and data 

This chapter describes the research methods and data used in the publications of this thesis. Theoretical background for the research methods, analysis processes and the tools, relevant to this thesis are introduced previously in chapter 2. Multiple data and methods are used over multiple publications, as described in Table 5 .

Table 5. Research methods, model characteristics, research applications, data and tools in the publications


### 4.1 Research methods

According to Morse (2010), research method design can be divided into mixed and multiple designs, where mixed method design consists of single complete core and one or more complementary methods. Multiple methods design means focusing on the same research problem but with different methods. This thesis applies the mixed method design. From the eleven mobile service usage research areas described in subsection 2.2, the core research areas are consumer behaviour and exploration of mobile service usage behaviour. The complementary areas are information security and social implications. The primary statistical method is Bayesian network analysis and the complementary method is the Chow test. Explanatory and predictive modelling are the key research methods and descriptive analytics a complementary method. The main Bayesian network

construction approaches are unsupervised learning (adapted with domain knowledge) and supervised learning. The complementary approach is manual construction of a Bayesian network. Taboo search and TAN with an MDL score are the core learning approaches and EQ and MWST complementary approaches. The main sources of data are OtaSizzle project, Finnish Communications Regulatory Authority (Ficora) and market research company Gesellschaft für Konsumforschung (GfK). The complementary sources are industry experts and their knowledge and opinions. BayesiaLab is the main tool in analysis and AgenaRisk and Excel extensions serve as complementary tools. The core findings come from Publications 2, 3 and 4, and these are complemented from the findings from Publications 1, 5 and 6.

Regarding the pre-processing of research data, the studies use by default $25 \%$ of missing data as a cut-off value for variables to exclude them from the analysis due to three reasons: First, principled methods, especially EM are used for missing data management. Second, lower percentage values would have excluded some of interesting and valuable information from the analysis. Third, the missing data mechanisms are expected to be MAR and FV. Further, the guidelines proposed in subsection 2.1.4 for discretization have been followed. MDL corebased learning for structure and MLE for parameters are used in all the studies based on observational data. Moreover, a preliminary analysis of the datasets has occurred by inspecting the variable dependences visually from the Bayesian network constructed with the MWST learned network. This can be called as descriptive analysis with the BN. Based on the visual inspection of the probabilistic paths between variables, the potential role of the variables in causal or predictive models can be concluded: central contributor, mediator or marginal. This role can be further estimated by calculating each variable's Node Force -value (NF). NF estimation as well as the calculation of the causal and predictive strength of a variable is based on information gain, i.e. as Kullback-Leibler Divergence $\left(D_{K L}\right) . D_{\mathrm{KL}}$ measures the difference between two probability distributions $P$ and $Q$ (e.g. Scutari, 2009). In this thesis, $D_{\mathrm{KL}}$ is calculated by using the following equation:

$$
D_{K L}(P(X) \| Q(X))=\sum_{X} P(X) \log \frac{P(X)}{Q(X)}
$$

where $P(X)$ is the joint probability distribution of a Bayesian network where an arc exists between two variables, and $Q(X)$ a distribution of a network where this relation does not exist. NF is a heuristic metric to study the importance of an individual variable within the whole BN. The higher the Node Force per variable is, the more important the variable is in the BN from a dependency point of view. NF of variable x is calculated as

$$
\mathrm{NF}_{\mathrm{x}}=\sum_{i} D_{K L} e_{i}+\sum_{j} D_{K L} o_{j}
$$

where $D_{K L} e$ is $D_{K L}$ of the entering (towards $X$ ) and $D_{K L} o D_{K L}$ of the outgoing arc of variable $X$.

# 4.1.1 Consumer behaviour and mobile service usage behaviour 

Analysis of consumer behaviour and mobile service usage behaviour are the core methods and are based on both predictive and explanatory modelling approaches. The former focuses on predicting the mobile device purchase behaviour as a function of time, using mobile device features and applications as a predictor, whereas the latter analyzes actual mobile service usage behaviour and factors affecting the usage. Buying a mobile device is an enabler for the actual usage of the mobile service, but as Smura et al. (2011) indicate, the actual usage often lags the penetration values found in the devices sold. In both research areas the research is exploratory in nature.

## Predictive modelling

The target in predictive modelling is to find features in devices which predict in each year between 2004 - 2013 the popularity of device models, and then to discover patterns and trends in the predictivity over the selected years. TAN was chosen as a predictive method, as it outperforms the simpler Naïve Bayes method, as described in subsection 2.1.4. However, the whole predictive system used in the study can be considered as a discrete temporal Bayesian network (TBN) consisting of ten time slices, where in each year the popularity is predicted with TAN. There are two TBN extremes possible regarding the structure (e.g., Dagum et al., 1992; Mihajlovic and Petkovic, 2001; Murphy, 2002), namely

- The structure is fully repetitive, the model is a first order Markov (Carlin and Chib, 1995) and therefore can be expressed as 2TBN (two-slice TBN).
- The structure in each time slice can vary and the temporal relationships can be dynamic, resulting in a non-repetitive finite network structure 10TBN.
The latter approach was applied in the study. This is because new technical features emerge continuously as a function of time which cannot be described with a 2TBN structure. On the other hand, a first order Markov chain was applied in order to reduce the complexity of the model and because based on the analysis, the predictivity did not increase by adding features from time slices $t$ 2 and backwards in time, to predict the target, - i.e., unit sales at time $t$, discretised into different popularity levels, as seen from Figure 9.
![img-8.jpeg](img-8.jpeg)

Figure 9. Correlation between Unit sales ${ }_{t}$ and Unit sales $_{\mathrm{t}-1}$, Unit sales $_{\mathrm{t}-2}$. . .Unit sales $_{\mathrm{t}-5}$, when t is 2009, 2011 and 2013.

In addition to applying a first order Markov chain, the complexity of the predictive model was further reduced by restricting the number of temporal connections between consecutive time slices. We assumed that it is reasonable to delimit temporal relationships to commercial variables, namely unit sales, price, sales months and leave out the other variables from temporal relationships between the slices. There are two reasons for this. First, feature bundles vary quickly due to the short lifetime of device models and rapid technology evolution, and therefore the features of the previous year do not contribute to predictive power in the same way that features of the current year do. Second, commercial variables of the previous year indirectly contain the predictive effect of those years' features. This assumption was validated by constructing two types of models and by comparing their predictive accuracies. In the first model all contemporaneous and temporal dependences were allowed and in the other the temporal dependences were limited only to commercial variables.
The strength of the predictivity of each variable for unit sales' popularity intervals is calculated as information gain, i.e. $D_{\mathrm{KL}}$.

The following parameters are used in trends and structural breaks analysis:

1. A linear regression is calculated when a $D_{\mathrm{KL}}$ value exists at least in eight consecutive time slices. Eight is selected based on the typical length of a mobile device feature diffusion curve (e.g., Riikonen, 2016). A correlation coefficient $\mathrm{R}^{2}>0.8$ is used as a criterion for the existence of a linear trend by testing how well the trend line approximates the $\mathrm{D}_{\mathrm{KL}}$ data points.
2. A structural break type A is identified, if at least in four consecutive time slices the $\mathrm{D}_{\mathrm{KL}}$ value exists and in the remaining four or more it does not exist (or vice versa).
3. A structural break type B exists, if, in a Chow test, the coefficients of two linear regressions within at least eight consecutive $\mathrm{D}_{\mathrm{KL}}$ values are not equal with a $\mathrm{p}<1 \%$ confidence level. If more than one structural break fulfils this criterion, the one with the highest Chow score will be selected.
4. The strength of a feature as a predictor for the popularity in each year is calculated by accepting only results which fulfil a $\mathrm{p}<1 \%$ confidence level.

# Explanatory modelling 

Explanatory modelling applies both Latent variable Naïve modelling and causal Bayesian network modelling. This study relies on causal probability the-ories-meaning that causal influence can be analyzed as probabilistic relations and causality is adapted on an interventional level. These methods are introduced in subsection 2.1.4.

Segmentation analysis uses a latent variable (Naïve) structure creation process, described in Figure 10. Each latent variable represents as a hidden variable a common cause for observed intensity distributions of those variables

(mobile services) belonging to the same cluster. The number of intervals for a latent variable describes the number of segments in the study and can be defined as part of the EM induction process manually or automatically. After this phase, a Taboo search with MDL scoring is used to learn a new structure, consisting of the latent variables and variables describing the probability distributions of the age, gender and service usage diversity of the users.
![img-9.jpeg](img-9.jpeg)

Figure 10. A process to create latent variables and a hierarchical Bayesian network.

A causal Bayesian network is constructed with Taboo search and MDL scoring, where the learned structure is restricted with domain knowledge. Special interest has been in discovering causal relationships between usage intensity and perceived importance of traditional and mobile communication services and how they are related to user characteristics, such as age, gender and life situation. Figure 11 describes the used process for constructing a causal Bayesian network from a survey dataset, originally consisting of 112 variables.
![img-10.jpeg](img-10.jpeg)

Figure 11. High level process to construct a causal Bayesian network from Ficora survey data.
As seen from the process flow, explanatory modelling is based on an iterative use of Taboo with an MDL score and the variables' temporal ordering information and other restrictions. Temporal data has been associated with each variable as an additional parameter for the Taboo search. It is logical to assume, that newer technology may reduce (i.e., effects by reducing) the importance of older technology, and therefore the arc direction should be from the variable representing newer to the variable representing older technology. The temporal

order for variables was based on qualitatively estimated technology groups arranged into chronological order. For example, because IM was introduced later compared to SMS, it belongs to a newer technology group. Thus, if an arc between IM and SMS results from the learning process, the arc direction is from IM to SMS due to the temporal relationship between them. Arc directions in the Taboo and MDL learned structure having temporally ordered variables need to be verified, because temporality does not automatically always provide causal direction (e.g., Pearl, 2009, section 7.5). The expert-based verification of causality consists of reviewing all the arc directions and their relevance in the model and analyzing whether some latent variables is the reason for the arc and its direction. For example, arcs might exist due to spurious relationships, or a clear causal connection is missing even if it should exist based on expert hypothesis. A re-learning round might be required with additional constraints (arcs' black and white lists), such as "arc is not allowed" or "arc is mandatory" between certain variables. This phase contains also a simplification of the BN by calculating the confidence for each arc as a p-value and by eliminating those arcs from the final network, where the null hypothesis can be accepted and where the calculated p-value is greater than a pre-defined value. The output from this phase is a candidate for a causal Bayesian network. The construct is further validated by using other search methods, EQ, SoPEQ and Taboo Order (see Munteanu and Cau, 2000; Jouffe and Munteanu, 2001; Jouffe, 2002) the methods in to test whether smaller MDL values with correct causal directions are achieved with help of other search methods. In case of yes, re-learning will be implemented with Taboo and MDL with additional restrictions.

As it is possible to use a Bayesian network for omnidirectional inferencing, this capacity is exploited to infer the probability distribution of each mobile service as well as age and gender given the selected interval of the latent variable. In this way the most probable mobile services per segment and related age and gender profiles can be estimated.

# 4.1.2 Elicitation and documentation of tacit knowledge 

Complementary studies are related to information security analysis, analysis of social implications and CSP business modelling. Common to all these mobile service-related studies is the lack of observational data. The data is tacit knowledge, i.e., expert knowledge and the task is to discover and document it, in these studies using a Bayesian network approach. Subsection 2.1.4 describes the basic principles, processes and challenges in general that are related to knowledge discovery and especially when using a Bayesian network as a method of documentation.

As there is no observational data available, the research method is the whole process, from selecting experts, eliciting knowledge from them and documentation of that knowledge. Two of the studies (information security analysis and analysis of social implications) are related to probabilistic risk assessment and

in them the knowledge discovery process uses methods described in subsection 2.1.4. A specific Bayesian network skeleton (taxonomy) is applied, originally proposed by Fenton and Neil (2012) for risk assessment, see Figure 12.
![img-11.jpeg](img-11.jpeg)

Figure 12. A skeleton Bayesian network for risk assessment tasks. Figure is modified from Publication 5 .

The task in the knowledge elicitation process is to discover, treat and group the factors according to Figure 12 and to analyze their probabilistic relationships accordingly. Information risk assessment analyzes the risks originating from the usage of mobile devices and services. Analysis related to social implications concentrates to risks affecting the availability of Public Safety and Security (PSS) mobile services and the consequences of that. Figure $\mathbf{1 3}$ describes the basic process for knowledge elicitation used in both risk assessment studies. In information risk analysis each risk-consequence-pair was individually estimated with the experts and thereafter this information was combined into CPTs with the developed Excel script. Eight experts were used in the analysis, two from Aalto University, one from the National Cyber Security Centre of Finland and the rest from Finnish enterprises. In social implications analysis about the availability of PSS services, the content of CPTs assigned for each variable was estimated manually. The marginal distributions of risks, controls and mitigants were estimated based on existing occurrences in the PSS network in Finland during the research year when this information was available. Ten experts from Suomen Erillisverkot contributed to the knowledge discovery phase. The company is managing the Finnish PSS network.

![img-12.jpeg](img-12.jpeg)

Figure 13. Knowledge discovery process used in risk assessment analysis. Figure is modified from Publication 6.

The main target in the CSP business model analysis in Publication 1 was to introduce a novel method to collect knowledge from multiple experts living in different countries, each having a variety of expertise in the telecommunication domain from numerous dimensions, such as technology, marketing, business management, regulation, customer experience, HR management, strategy and product management. A Bayesian network based on the knowledge of each expert was created, referred to here as a sub-BN. Altogether 48 experts contributed to the knowledge elicitation process and 40 sub-BNs was constructed. Osterwald Business model ontology (Osterwald, 2003) was utilized to combine sub-BBNs together into a comprehensive model. The resulting Bayesian network represents typical business circumstances in the European telecommunications domain. Experts were categorized by dimensions and they were asked to list by email as many as possible causality triplets from the domain they represent, including the strength of causal connections. Each three variables with causal dependences between them are referred to as a causality triplet. Experts defined the triplets in a form of an adjacency matrix, proposed by Nadkarni and Shenoy (2004). Variables were weighted based on their popularity in different adjacency matrices and this weighting defined the variables to be selected to the final comprehensive model. The CPTs were calculated using the causal strength information in the triplets and weighted sum -algorithm, utilizing compatible parent configurations, proposed by Das (2004).

The proposed knowledge acquisition process has three benefits. First, the experts are used only once in the process which was a benefit when recruiting busy domain experts for the analysis. Second, with this method it is possible to introduce rapidly a high number of variables for the domain of interest. Third, large and complex causal Bayesian networks can be constructed using a high number of geographically dispersed knowledge sources. Experts did not use a common dictionary when creating the triplets and therefore they introduced many differ-

ent terms with the same underlying meaning. Based on this outcome, a dictionary was created, which can be used in further similar knowledge discovery tasks to decrease the number of variables.

# 4.2 Research data 

Research data consists of three datasets:

- Mobile devices' feature and retail sales data, sold in Finland 2003 2013: Annual information about mobile device model names, their sales volumes, retail prices, technical features, pre-installed apps, supported protocols, and manufacturer brands. This dataset is provided by the market research company GfK. Part of the feature information has been collected also from device description repositories and manufacturers' websites.
- Use of mobile services at Aalto University community: Handset based measurements, conducted in the OtaSizzle project at Aalto University during 2009 and 2010 from 134 Symbian users.
- Use of communication services in Finland in 2011: A telephone survey, consisting of 3008 Finns with ages between 15 - 79 years about their communication services' usage behaviour, provided by Ficora.
Below each dataset are described in detail.


### 4.2.1 Mobile devices' feature and retail sales data

The feature and retail sales data has been merged together and grouped into ten groups, as seen from Table 6. The value of a feature can be binary (e.g., camera in the device yes, no), textual (e.g., user interface qwerty, touch, 3x4) and numerical values discretized into intervals (e.g., unit sales $<=500$ "very low in popularity", $<=2500$ "low in popularity"; $<=12500$ "medium in popularity"; $<=45000$ "high in popularity"). The research data is organized, for the statistical analysis, into a matrix format with data from each device model in rows and the variables in columns (Table 7). The initial research data consists of 1482 rows representing all the phone models sold in Finland during the research period, and 90 columns representing the variables. The data was pre-processed using four methods:

1. Calculations to derive more meaningful variables, such as averaging phone models' annual price from monthly prices, calculating annual unit sales from monthly sales and converting 2-dimensional values, like x and y -axis pixel resolutions into a single value.
2. Filtering out those variables that are completely determined by other variables. As an example, variable "generation" has been kept but variable "digital stand" i.e., variable with alternatives 2G, 3G, 4G, excluded.

3. Filtering out variables without statistical data, such as e-cash, i.e. a variable which describes whether a mobile device has a preinstalled payment application.
4. Initially filtering out variables with more than $25 \%$, in the final dataset $10 \%$ of the missing values and whose type is MAR, such as size of RAM memory and the processor speed.

Table 6. Variables in mobile device feature and sales data categorized into ten groups for clarity


This pre-processing phase decreased the number of variables from 90 to 52, visible in Table 6. In addition to missing values of type MAR, a special type of missing value FV (described in subsection 2.1.4) has been added to the dataset to describe missingness, when a variable cannot logically have a value in relation to a certain other variable's value and therefore 'FV' itself is the value. This decreases the potential bias originating from misinterpreted missing values. For example, if the value of variable "camera is "no", the variable "zoom" has the state "FV."

Table 7. A subset of mobile device feature and sales data from 2013 organized into a matrix format


# 4.2.2 Use of mobile services at Aalto University, 2009 - 2010 

With the advent of smartphones, it has become possible to install third party application software on mobile devices. Handset-based measurements are a data collection method utilizing this ability. In handset-based measurements a research application is installed in the handsets of the users who have opted to participate in the measurements. This application collects data on overall usage of the device, including mobile service usage and contextual data. Data on mobile service usage is collected when the service is visible in the foreground of the device's screen. Consequently, processes or services running in the background and not directly interacting with the user are not being analyzed. More-over, data on mobile communication services, such as voice calls, SMSs, MMSs, and emails are collected whenever a voice call is made or received, or a message is sent or received.

The original dataset was collected from 200 users in the OtaSizzle project of Aalto University during 2009 and 2010 (Karikoski, 2012). The study utilized the data collected from Symbian devices from users who have produced data for a minimum of 30 days. Thus, the data consists of mobile service usage information from 134 users with males and females represented by 91 and 16 users,

respectively. These users were Aalto University students and staff. The members in the measurements have been identified by Karikoski (2012) as early adopters of mobile devices and services. Close to 600 unique services used by the participants have been analyzed and mapped to categories according to the framework of Smura et al. (2009). In this process, the non-user generated service events (mostly related to the operating system) have been excluded from the data, in order to ensure that the service usage events depict actual user behaviour. As in most computer-generated data collection efforts, the data is displayed on the user level in a time-stamped log form. In the study, the data has been aggregated from single service usage events and pre-processed by calculating the daily service usage intensities for each user by dividing the number of service usage events of a given user by the number of days that that user has produced data in the measurements. With services such as voice calls, the volume of usage as the length of voice calls has been measured. The average length of the incoming / outgoing voice calls is then aggregated on the user level. As an additional variable the diversity of mobile service usage has been calculated for each user as the number of services used. In case no usage of a given service per user exists, the value has been put to zero. Table 8 is a snapshot of the dataset in matrix format, used in the analysis.

Table 8. Otasizzle dataset organized as rows (users) and columns. Columns are gender, birth year, diversity and service usage intensity of all analyzed mobile service including call durations


3. Conditional questions consisting of both nominal and dichotomous questions (so-called skip logic), e.g., "if you have an Internet connection, what is the speed of your connection?"
The questionnaire handled six themes with multiple questions in each theme:
4. Perceived importance and usage intensity of communications services.
5. Importance of having a possibility to read daily news in general and from the Internet.
6. Fixed to mobile Internet convergence.
7. Contract types with CSP, Internet access speed and monthly payments.
8. Demographic questions.
9. Other question.

The questions were coded by using the themes and mobile service name with the " $u$ " abbreviation to denote usage intensity and " $i$ " abbreviation to denote felt importance of mobile service. Table 9 depicts the coding and actual questions used from the first theme.

Table 9. Coded questions and actual questions in theme "Perceived importance and usage intensity of communications services"


The research data has been organized in matrix format, where one row represents one person and the columns the questions. The data contains also a weight factor for adjusting the survey participants' gender and age distributions to regional level in Finland. However, it was not used and thus the results reflect the situation on a national level.

Even though the focus is in mobile service usage intensity and perceived importance, all the questions from the intensity and importance-theme (Table 9) were used in modelling, including also browsing, video and music, file transfer and age. As also other variables might contribute to the causal structure as mediators and confounders, or the dependences statistically might be weak, a Bayesian network based on a MWST search with MDL scoring was used to visually verify them. In this way, the number of columns reduced in the final dataset from 112 to 17 columns. Table 10 is a snapshot of samples consisting of the final variables. Also, the number of rows reduced because not all the samples contained an Internet connection and the person answered "cannot say" to many questions at the same time. When filtering these kinds of samples out, the number of rows in the final cleaned dataset reduced from 3008 to 1291.
Respondents' age has been categorized to five intervals (Figure 14), thus forming a nearly even distribution. This means that each range has about the same number of samples.
![img-13.jpeg](img-13.jpeg)

Figure 14. Age distribution in Ficora dataset.
Table 10. A part of the cleaned Ficora survey dataset for causal analysis. The stars indicate FV


# 5. Results 

This chapter presents the results of the thesis following the four research questions presented in the introduction chapter. The subsection 5.1 summarizes the findings and proposals from chapter 2 and subsection 4.1 related to Bayesian networks as a statistical method. Subsection 5.2 describes the results from the analysis of the predictivity of mobile device popularity based on their features during 2004 - 2013 in Finland. Subsection 5.3 analyzes the years 2009 - 2011 from a mobile service usage behaviour perspective based on two different types of populations. Finally, the last subsection 5.4 summarizes the results from two risk assessment studies.

### 5.1 Use of Bayesian networks for data analysis

The use of Bayesian networks as a statistical method has a far shorter history in comparison to the widely used and proven traditional method such as regression or SEM analysis. Bayes' theorem of Thomas Bayes is applied in Bayesian networks modelling, but also other non-Bayesian approaches are used. The big single thing is the use of DAG to document qualitatively the model, which has clear benefits but also might bring along some confusion. This may be also one reason why Bayesian networks are rarely used in academic research as a statistical method.

The thesis describes the basic principles of Bayesian networks and sheds light on practical approaches and parameters to use in the research, especially for non-parametric Bayesian networks. The topics covered are the following:

1. Characteristics of Bayesian networks as a statistical method, benefits and challenges
2. The definitions and examples for descriptive, predictive or explanatory analysis with Bayesian networks
3. Historical perspective of Bayesian networks
4. Bayes' theorem in Bayesian networks
5. Theoretical background to Bayesian networks
6. Description of Bayesian network types and concepts
7. Differences between parametric and non-parametric modelling approaches in Bayesian networks
8. Overview of extensions for Bayesian networks; latent variables and hierarchical Bayesian networks, utility and decision nodes and DBN

9. Explanations of causality, causal Bayesian networks and a Bayesian network-based approach for SEM
10. Description of the knowledge discovery and documentation processes using Bayesian networks
11. Data pre-processing: description of missing data management within a Bayesian network context and data discretization approaches
12. Recommendations for CPT size as a function of size of research data
13. A report about structural learning alternatives and preferred approaches
14. A process description for search and score-based learning to construct a causal Bayesian network
15. Tools-list supporting modelling with Bayesian networks
16. A survey of research papers in the Mobile service usage domain utilizing Bayesian networks

# 5.2 Trends and structural breaks in mobile device popularity 

A mobile device and its features are enablers for the usage of mobile services. The more that the device models with new innovative technical features have been purchased, the greater the potential exists for the usage of mobile services. The topic has been traditionally studied from technology acceptance (subsection 2.2.4), diffusion of innovation (subsection 2.2.5) and consumer purchase behaviour (subsection 2.2.6) perspectives. Based on the literature review results in Publication 4 from 16 studies covering the years 2002 - 2012, twenty important device features as choice criteria were found, but considerable variation appeared in the criteria among the studies. This variation is due to differences in questionnaire, research method, target audience, time and country of research. Because of this variation it is impossible to discover trends or structural breaks in choice criteria solely based on previous studies.

This study uses a new approach to explore trends and structural breaks in purchase behaviour by predicting the popularity of mobile devices with their features. The features can be technical features, such as support for GPRS and standbytime, physical features such as weight and thickness, commercial features, such as price, and sales volume during the last year and, additionally, operating system and manufacturer brand. The motivation was to explore patterns and trends in Finnish mobile markets with a statistically new approach, to find potential structures and patterns not discovered before. It is notable, that the study period covers most of the two intervals named in chapter 3 as "Emergence of value-added services" and "The battle between operating systems".

The accuracy of the used models as AUC in each time slice and popularity category is calculated as an average from cross validations with $\mathrm{k}=2,3$ and 5 . As can be seen from Table 11, on average the highest accuracy is obtained for the unit sales per year interval " $5-500$ " (very low popularity) and the lowest accuracy for interval " $45001-284721$ " (very high popularity). Similarly, in 2005 the

accuracy is the highest and in 2010 the lowest. The model's overall accuracy expressed as AUC is $93.6 \%$, which can be regarded as excellent in the traditional academic point system. The popularity categories from very low popularity to very high popularity for Finnish mobile markets as number of models sold was defined by the study authors.

Table 11. Model's predictive performance as AUC for each time slice. Table modified from Publication 4


The variables in each TAN are visible in Figure 15, which visualizes the predictive model for the year 2007, where unit sales ${ }_{2007}$ is predicted with the variables around it.
![img-14.jpeg](img-14.jpeg)

Figure 15. Visualization of TAN model for year 2007. The label is unit sales ${ }_{2007}$. Variables are visualized as bubbles. A bubble colour indicates the variable type. Red is commercial, light green camera related, light grey dimensions, dark grey display characteristics, light blue pre-installed apps, violet networking characteristics and lilac brand. The size of bubble diameter describes the relative importance of a variable as predictor for popularity in 2007. For clarity, arcs' heads have not drawn. Figure modified from Publication 4.

The only trend in predictivity was discovered between unit sales and the operating system fulfilling the selected linear regression criteria of $\mathrm{R}^{2}>0.8$. The operating system predicts unit sales for the first time in 2006 and $D_{\mathrm{KL}}$-values doubled between 2006 and 2013. Statistically this can be explained with the changes in unit sales probability distributions given operating system. Before 2006, both poorly and well selling models contained similar operating systems, such as Symbian, whereas towards 2013 the operating system started to be one

of the indicators for a successful device model. Figure 7 sheds light to the actual sales volumes.

Both type A and B structural breaks were found. Table 12 outlines the structural breaks and their types. Table 12 indicates, that most of the structural breaks took place during 2008, 2009 and 2010. Explanation for the structural breaks regarding availability of technical features (binary variables) seems to follow the penetration growth of that feature. As an example, camera is a predictor of certain strength until 2008, but not anymore thereafter. Camera pixels became a new predictor in 2009. Camera was in 2008 in $85.7 \%$ of devices and manufacturers started to invest in the image quality ending up in a greater variation in pixel amounts, visible as a structural break in 2008/2009. Similarly, multitouch was a predictor for the first time in 2010. Based on chapter 3, the coverage of the Finnish 3G network reached about 70\% of the Finnish population in 2009. Therefore, it is not a surprise that GPRS was not a predictor in 2007 and thereafter, EDGE started to decline in 2008 and HSDPA to increase from 2008 onwards. Sales duration and unit sales of previous year formed a type B structural break, the former in 2009/2010 and the latter in 2010/2011. They can be explained as shortened average sales duration and its smaller variation as well as a disruptive market situation in Finland from 2011 onwards.

Interestingly, price, device dimensions, screen size, design, standbytime and device type did not form any trend nor clear structural breaks. They were predictors more in random than in a structured way. It was expected based on the literature review about mobile device choice criteria in Publication 4, that for example price, standbytime and size of the device would be regularly predictors for device popularity.

Table 12. Structural breaks and their types in Finland between 2004 - 2013. B $\cap$ denotes structural break type B, where predictivity first increases and after the turn of the year starts to decrease. A $\rightarrow \mid$ means structural break $A$, which ends at the turn of the year. A $|\rightarrow$ mean structural break $A$ which starts in the turn of the year. The rest are the features without any clear trend or structural break


The obvious statistical explanation for a structural break in 2007-2008 regarding the manufacturer brand is hard to outline based unit sales distribution given manufacturers. A more logical explanation can be found in studies of the brand effect on the mobile device choice criteria. For example, according to (Petruzzellis, 2010), the manufacturer brand traditionally relates positively to consumers' intention to purchase specific mobile device over others. Therefore, this structural break might be explained as changes in the role of Nokia in purchase decisions, i.e., Nokia brand positively affected purchase decisions up to 2007 but 2008 was the first year, when Nokia's brand effect started to decrease, in less than one year after the launch of the iPhone in mid-2007. This kind of change can be further explained as a mobile device market turning from hard-ware-driven to software-driven mode from 2008 onwards, as discussed in chapter 3. Thus, the time until 2007 can be categorized more as hardware-driven market mode, and 2008 and onwards more software-driven mode. Another viewpoint can be found in chapter 3 from the discussion about changes in pricing schemes for data in 2007 in Finland. The possibility for speed-level pricing

with unlimited data volumes in 2007 potentially motivated users to use more value-added services compared to the situation in 2006 and earlier.

Another structural break without an obvious statistical explanation was the one in 2010-2011 related to the popularity of a phone model in the previous year, as a predictor for the popularity in the current year. This phenomenon can be explained as a combined effect of four factors: 1) the launch of iPad happened at the end of 2010 in Finland and might have changed the mobile device choice criteria in 2011 from the previous year; 2) the announcement of the Nokia and Microsoft cooperation in early 2011 may have changed the importance of the Nokia brand as choice criteria; 3) the number of device models increased by 40 in 2011 (see Figure 7) thus increasing thus choice alternatives, and; 4) the CSPs have increased, from 2011 onwards, the ease for consumers to switch device model.

# 5.3 Classification of mobile services and their users 

Mobile service usage behaviour is explored with two different data sets: 1) handset data representing the actual usage of mobile services of Aalto University students and staff in 2009 - 2010 with mobile devices having a Symbian operating system, and; 2) survey describing the Finnish population and their preferences regarding communication services in 2011. These datasets have been utilized in the classification of mobile services and their users based on the service usage behaviour.

### 5.3.1 Aalto University community

The 575 mobile services available for the Aalto University community were grouped manually based on the framework given in Smura et al. (2009) into ten categories. As seen from Table 13, 60\% of them belong to three categories "others", "games" and "system utility".

Table 13. Categorization of mobile services available for Aalto University community


From these services, only 14 are used on average every day, as seen from Figure 16. The intensity value in $80 \%$ of the 575 services is below 0.01 and from

them 100 services have not been used at all during the research period. The traditional services, SMS, email and calling are the top three services, followed by browsing, menu, clock and calendar. Emails are used for reading and less for writing. According to chapter 3, Nokia has put effort to music capabilities, and this may explain that music has been listened to nearly daily with the mobile device. Also, the use of camera of the mobile device is rather common and can be explained with the discovered structural break in camera feature of the mobile device during 2007/2008 and its increased average image quality in 2008/2009. The use of email can be explained with the high penetration of email apps in devices (Publication 4) and the high usage intensity of WCDMA, EDGE and GPRS (Figure 16). Also, the finding in structural breaks regarding GPRS, EDGE, WLAN and WCDMA (Table 12) explains the observed high usage intensity of WCDMA sessions over GPRS and EDGE. Even though the mobile versions of YouTube, Gmail, WhatsApp and Google Maps were available already in 2009, only Google Maps from them is visible in Figure 16 which can be interpreted as lagged support for Symbian.
![img-15.jpeg](img-15.jpeg)

Figure 16. Usage intensity of services as an average number of services used per day (black bars). Average number of network sessions per day (grey bars). Figure is modified from Publication 2.

![img-16.jpeg](img-16.jpeg)

Figure 17. A BN created with MWST search and MDL scoring from 506 variables (mobile services). Each small dot depicts a variable with some intensity distribution of one mobile service. For clarity, only a few of them have been named. The arc between two variables denotes an existing probabilistic dependency. Thick arcs denote a strong dependency. Black dots with names depict services which has a strong dependency with others and red dots services which are locally related with high number of other variables. Figure is modified from Publication 2.
![img-17.jpeg](img-17.jpeg)

Figure 18. Variables with highest Node Force with their service usage intensity values.
In addition to manual grouping of mobile services, their role as mediators and non-mediators were analyzed. A mediating service is one which relays the usage intensity of other services. As an example, App update is a mediator enabling the usage of the actual service. NF analysis from an MWST-learned network (Figure 17) was used to estimate the variable's role as mediator. Figure 18

shows the 17 variables with the highest NF with their intensity values. The clearest mediator services are Photos, Installer, App update, Settings, Secure Widget UI, Location, Poingo and Ovi Store, as their NF value is high and usage intensity value is very low. High NF, and at the same time high intensity values of incoming and outgoing SMS as well as incoming and outgoing calls, is due to their two-way usage behaviour: a person who is sending many SMSs will also most probably receive many SMSs. Especially Ovi Store's and App update's role as mediator should have been more central and their NF values therefore higher compared to the measured values.

Mobile service users of the Aalto University community are segmented using the latent variable modelling approach. The latent variable in the middle of the Bayesian network (Figure 19) has three states representing the intensity characteristics of the user classes $\mathrm{S} 1, \mathrm{~S} 2$, and $\mathrm{S}_{3}$. The means of service usage intensity values for those segments as well as their probabilities are seen in Figure 19. Using this model, the means conditionally with service usage intensity segments S1, S2 and S3 are calculated to characterize each of the segments (Figure 20). The segments are called "S1: heavy communicators", 26,9\% of users, "S2: experimentalists", $26,9 \%$ of users, and "S3: basic smartphone users", $42,2 \%$ of users.
![img-18.jpeg](img-18.jpeg)

Figure 19. A latent variable model for service usage segmentation. "Service Usage Intensity Segments" is the latent variable representing the 23 manifest variables (connected with black arcs). The black numbers are $\mathrm{D}_{\mathrm{KL}}$ values between the manifest and latent variables, and blue numbers represent the relative significance of the arc (maximum is 100\%). Blue arcs denote a new network, consisting of the originally constructed latent variable with black arcs and additional variables; Gender, Diversity, Birth Year and Call duration. The figure is modified from Publication 2.

- S1: "a heavy communicator" has a high daily SMS usage intensity ( 3.97 for in and 3.69 for out), the highest intensity for Calls in and out (2.42 and 2.79, respectively) and for Contacts (2.88). Moreover, a somewhat higher usage intensity of Clock (1.92) and Notes (0.17) exists.

- S2: "an experimentalist" has the highest daily intensity for Music player (1.65), Camera (0.77), Email (0.87), WLAN wizard (0.24), Notes (0.26), Maps (0.56), App manager (0.08), and Installer (0.18), which fit to the usage profile of a person who wants to experiment and use the device for many purposes. Furthermore, usage of SMS is moderate.
- S3: "a basic smartphone user" has tried the phone with many features but uses it moderately, mostly for Calls (in 1.68, out 1.55), but also sometimes to check Emails (0.43) and Images (0.45).
![img-19.jpeg](img-19.jpeg)

Figure 20. Service usage characteristics of user classes S1, S2, and S3 analyzed as normalized conditional intensity means. Normalized conditional intensity is zero in the middle of the chart and maximum $100 \%$ on the rim. Figure is modified from Publication 2.

In addition to the classification of users based on their service usage intensity behaviour, the model in Figure $\mathbf{1 9}$ was used to infer the users' typical age, gender, call durations and diversity behaviour in each segment as probabilities of the segment given priori data for diversity, gender, birth year, and duration of incoming and outgoing calls. Birth years were classified to 1954-1976 (10.2\% of users), 1977-1986 (33.8\% of users) and 1987-1991 (59.0\% of users). The conclusions to be drawn are as follows:

- Those persons who have low diversity (who have used all in all less than 21 services out of nearly 600) belong with $80.7 \%$ probability to segment S3 ("basic smartphone user"). Persons who have used 71 or more services belong with $66.3 \%$ probability to segment S2 ("experimentalists").
- Women belong with $53.6 \%$ probability to segment S1 ("heavy communicators") and only with $6.8 \%$ probability to segment S2 ("experimentalists"), whereas men's segment distribution is not so sharp.
- Users in the 1954-1976 category belong with $97.9 \%$ probability to segment S3, whereas users in the 1987-1991 category belong rather evenly to all three segments. Low averages in incoming and outgoing call durations are linked with $53.5 \%$ and $97.6 \%$ probabilities to segment S3, but also medium incoming call duration with $95.8 \%$ probability is linked to segment S3.

# 5.3.2 Population of Finland 

The study with a Finnish population dataset attempts to examine causal relationships between an individual's age and the perceived importance and usage intensity of communications services. An individual's age has been categorized into five ranges (see Figure 14) each having the same number of samples. Perceived importance is treated as a single survey question, having five predefined qualitative answer alternatives (Table 9). The purpose is to explore the following questions:

- What kind of causal dependencies exist between a user's age and the perceived importance and usage intensity of communications services?
- What kind of causal dependencies exist between the perceived importance and the usage intensity of communications services?
- How can these dependencies (statistical and causal) be interpreted and explained?
- What kinds of differences exist in causality results between Pearl's do calculus and a proprietary method called Jouffe's Likelihood Matching?
The study did not distinguish mobile services from services used with PC. The services were calling, SMS, IM (Instant Messaging), Facebook \& Twitter, email, Internet TV, Internet browsing, Skype, Internet usage for music and video watching, remote work, file transfer and traditional letter and newspapers for reference. Based on visual inspection of Figure 21, age is clearly dominant in this Bayesian network, as 13 variables are directly connected with it, and due to the relative size of its bubble. The numerical evaluation of NF values in Publication 3 shows, that from 100 questions, 25 have an NF value greater than 0.4 and 50 have less than 0.1. The survey questions regarding the importance and intensity of communication services (Table 9) have a high NF value and, therefore, are important to include in the causal analysis whereas half of the questions are fully independent with other questions and therefore not useful in causal analysis. In addition to age, other important questions (measured as NF), are 1.5i FB (importance of Facebook), 1.3u SMS (use of SMS), 1.4i email (importance of email), and 1.9i IM (importance of Instant Messaging), 5.5 life situation, $3.3 a$ and 3.18 g (binary questions regarding fixed network at home and whether Internet speed is important), 2.3u browsing (use of browsing), and 2.7 (binary question whether Internet is used for information searching). NF analysis of the model in Figure 21 shows also, that the Finnish communes, an individual's gender, and residence have a minor role in the BN, whereas household size and life situation have a strong dependency with each other given age.

![img-20.jpeg](img-20.jpeg)

Figure 21. Bayesian network using MWST search and MDL score based on 100 survey questions. The red coloured bubbles are ten variables with the highest NF value. The bubble size indicates qualitatively NF values. The arc thickness indicates qualitatively the size of $D_{e l}$, between variables. The numerical code follows the survey question numbering in Table 9 . For clarity, arcs' heads are not visible in the DAG. Figure is modified from Publication 3.

The causal Bayesian network was constructed by using the workflow described in Figure 11. In addition to the variables describing the age and usage intensity and perceived importance of communication services, mediating questions were identified from question themes two to six described in subsection 4.2.3, based on a visual inspection of the paths in Figure 21. As a result, 2.3u browsing, was discovered. In addition, also other structure search methods were tested for identification of mediators. Taboo produced the lowest MDL scores and based the structure with lowest MDL score, the following additional variables were re-identified as mediators: 3.2 interconnection, 2.4u video \& music, 2.6u TV, 6.2u music, and 6.4u file transfer. Interestingly, none of the questions related to demographic acted as a mediator. Also 1.2 mobilephone was excluded from the model, because $99.3 \%$ of the interviewees owned a mobile phone.

In temporality analysis, seven technology zones were defined, and the variables were arranged according to them in a chronological order from oldest (temporal index 1) to youngest (temporal index 7). One technology zone contains communication technologies with similar launch times. The technology zones were from oldest to youngest 1) letter, 2) landline, phone call, 3) Internet at home, e-mail, 4) mobile device, 5), SMS, 6) IM, Internet calls, Facebook \& Twitter, listening to music from Internet, watching videos and TV from Internet, and 7) usage of IM, Facebook \& Twitter, Internet calls from a mobile device, and watching video and Internet TV from a mobile device. The zone information (temporality information) as part of the learning process ensured, that the structure after the learning process did not contain arcs with directions from older technology to newer technology.

The structure comparison between a Bayesian network without (reference) and with temporality data (causal Bayesian network) was performed. A Bayesian network contained 20 variables and 40 arcs. Altogether $45.8 \%$ of the Bayesian network's arcs were changed in the causal Bayesian network (either directions changed, arcs discarded, or arcs added), and the overall structure became simpler and existing arcs and their directions were logical. After the final analysis of each arc strength as $\mathrm{D}_{\mathrm{KL}}$, two variables were removed from the final model based on p-value analysis ( 6.2 u music, and 6.4 u filetransfer) and 1.1 landline just because it did not have any other connections except with 5.3 age. Thus, the final number of variables in the causal Bayesian network was 17. Figure 22 represents the causal Bayesian network model structure between the 17 variables.

The structure in Figure 22 can be used to draw qualitative causal conclusions:

- An individual's age and the perceived importance of a communications service together affect the usage intensity of that specific service. This is visible in 1.3u SMS, 1.4u email, 1.5u FB, 1.6u Internet, and 1.9u IM. Internet calls (1.8u SKYPE) is an exception, which is affected by the usage of Facebook \& Twitter during free time, and IM usage intensity.
- An individual's age has only a direct effect on $1.5 i F B$, i.e., how important Facebook \& Twitter are perceived. The variable 1.5i FB acts as a central mediator between age and the perceived importance of other communications services. This means that the perceived importance of Facebook \& Twitter directly affects the perceived importance of email, SMS, and IM, while the age affects them only indirectly. Perceived importance of letter and phone call are behind a long path from age. Thus, it is expected that they are rather independent of age, and that their perceived importance is affected by how important $S M S$ is perceived.
- Internet access at home is another mediator between age and many variables.
- An individual's age affects directly the variables $2.3 u$ browsing, 2.4u video \& music, 2.6u TV, and 1.5u FB.
- Age and 1.8u SKYPE are the start and end points of the whole causal BN. Therefore, usage intensity of Internet calls is "a product of" many factors, starting from age and ending at the usage intensity of Instant Messaging and the usage intensity of Internet for staying in touch with others during free time.

![img-21.jpeg](img-21.jpeg)

Figure 22. Causal BN about perceived importance and usage intensity of communication services within Finnish population in 2011. Black arcs denote direct causal effect from 5.3 AGE, blue arcs direct causal effect from variables describing perceived importance of communications services, orange arcs direct causal effects from mediating variables not belonging to the study focus, and green arcs direct causal effects from variables describing usage intensity. Figure is modified from Publication 3.

A quantitative analysis was conducted using the causal Bayesian network of Figure 22 based on the probabilistic relations between an individual's age and 1.3i SMS, 1.4i email, 1.5i FB, 1.9i IM, 1.1oi call, and 1.11i letter and using Pearl's do-calculus. Specifically, a conditional mean analysis was conducted by calculating the most probable mean value of the effected variable given each state of the causing variable (e.g., age). This analysis answers to the following question: "what kind of causal relationships exist between an individual's age and perceived importance of communication services"? Figure 23a describes the results. Similar analysis between $1.5 i F B$ and other questions related to perceived importance were conducted. This analysis sheds light on the role of $1.5 i F B$ as a mediator for the perceived importance of other communications services (Figure 23b). Also, a causal analysis between age and the usage intensity of communications services was conducted (Figure 24a) as well as analysis about the mediator role of $1.5 i F B$ for usage intensities (Figure 24b). This analysis answers to the following question: "what kind of causal dependencies exist between the perceived importance and the usage intensity of communications services"?

Figure 23a illustrates that when age increases, perceived importance clearly decreases for Facebook \& Twitter, email, IM and SMS and slightly for phone calls. On average, Phone calls are perceived as "important", whereas IM and Facebook \& Twitter are typically perceived as "not very important". Figure 23b illustrates that dependency exists between the perceived importance of $F a$ cebook \& Twitter and the perceived importance of all studied communication services, except letter. Based on Figure 22 and Figure 23, the conclusion is

that a causal relationship exists between an individual's age and perceived importance of communications services and, in addition, that Facebook \& Twitter act as a central mediator towards other perceived important variables. The mechanism for the causal relationship between age and perceived importance and usage intensity of communication services is outside of the scope of this thesis.
![img-22.jpeg](img-22.jpeg)

Figure 23. Conditional mean of perceived importance of communication services give age (left, Fig. 23a). Conditional mean of perceived importance of communication services given perceived importance of Facebook \& Twitter (right, Fig. 23b). Figure is modified from Publication 3.

Figure 24a illustrates a decreasing trend of usage intensity of communication services (with mobile device) as an individual's age increases. Based on Figure 24b, the perceived importance of Facebook \& Twitter acts as a mediator to the usage intensities of all measured communications services. The conclusion can be drawn, that an individual's age affects, not only the perceived importance, but additionally the usage intensity. In this dependency relationship, the perceived importance of communications services in general, Internet connection at home and especially the importance of Facebook \& Twitter act as mediators for usage intensities. Also, in general when the age increases, the communication with other individuals decreases.
![img-23.jpeg](img-23.jpeg)

Figure 24. Conditional mean of active usage of communication services with mobile device given age (left, Fig 24a). Conditional mean of active usage of communication services with mobile device given perceived importance of Facebook \& Twitter (right, Fig. 24b). Figure is modified from Publication 3.

In 2011 the individuals in the age category of $155 \mathrm{age}<28$ perceived email and SMS rather important and Facebook \& Twitter somewhat important, and similarly individuals in category $645 \mathrm{age}<79$ felt them somewhat important and hardly important at all (can live without). Individuals in the youngest age category perceived calling very important (cannot live without) whereas individuals in the oldest age category felt calling rather important. When classifying the usage intensity values in Figure 24 to never (o), occasionally (o.33), weekly (o.67) and daily (1), the youngest age category uses SMS "nearly daily" and email, IM and Facebook \& Twitter "nearly weekly", whereas the oldest age category uses SMS weekly, but the rest of the services "almost never". These usage levels can be compared with the mobile service usage segments S1, S2 and S3 found in the Aalto Community. Indeed "experimentalists" (S2) have higher intensity values compared to all age categories of the Finnish population, but "basic smartphone users" (S3) seem to use the services with similar intensity to the youngest age category in Finland. Even the smartphone sales volumes and sold smartphone models in Finland in 2011 were already nearly half from all devices sold (Figure 7), and people perceived new communication methods rather important (except the oldest age category), this was not yet clearly visible in the service usage intensity. Traditional calling and SMS still dominated the usage in 2011.

Often a true causal model is not known. Based on the disjunctive confounder criterion by VanderWeele and Shpitser (2011), causal effects can be estimated by control for any covariates that are either a cause of treatment or of the outcome or both. This finding can be applied by using the constructed Bayesian network and Jouffe's proprietary Likelihood Matching method (JLM) (Conrady and Jouffe, 2015). In this network, the Direct Effect (DE) of a variable in question on the target variable is estimated utilizing Kullback's minimum cross-entropy MinxEnt (Shamilov et al., 2006) algorithm. It means, that when applying JLM to estimate causal effects from age, construction of a causal Bayesian network is not needed. Instead, the estimation can be accomplished using a Bayesian network learned with unsupervised or supervised learning methods. This can simplify the analysis process. In this study, the causal strength was compared between variables of interest using Pearl's do-operator calculated from the causal Bayesian network of Figure 22, and the same based on a Bayesian network (before addition of temporality data and iterative Taboo learning) and using the JLM method. Based on the analysis, JLM behaves logically when comparing the results with Pearl's method: if the do-operator finds some causality, JLM does too. On the other hand, JLM calculates lower causal values and therefore it fits better to a fast and indicative causal analysis rather than for a final analysis.

# 5.4 Risks pertaining to the usage of mobile services 

This study analyzes two different risk aspects within the usage of mobile services: information risks originated from the usage of mobile devices and risks

connected to the availability of PSS services. Both studies are related to mobile services and apply a similar method to assess the risks, their controls, mitigants and consequences. Both also reflect the situation in Finland in 2014 - 2015. However, the risk types, used services, service users, mobile devices and mobile networks are different. The former is based on commercial 4 G mobile network, whereas the latter uses a dedicated 2G PSS network. In the future, a PSS network may operate also in a commercial network (Peltola, 2018) and therefore the information risks that were identified will be valid also in the PSS usage.

# 5.4.1 Information risks 

Information risk assessment focuses on the risk events and their consequences and leaves out the original triggers, controls and mitigants for potential further study. Such an extended model could be used for identifying the most dangerous practices of smartphone usage and security measures that would be most useful for prevention or mitigation of risks. Figure 25 describes the risk events and their marginal probabilities in one year, defined by the experts.
![img-24.jpeg](img-24.jpeg)

Figure 25. Information risk events and their marginal probabilities for one year defined by the eight experts. Figure Modified from Publication 6.

In addition to the risk events, experts defined separately potential consequences for the device users in order of importance; the risk events which contribute to each consequence and the severity distribution of each consequence for the user in case the risks occur as none, low, medium and high. Based on this information, a common view was constructed, as described in subsection 4.1.2. The identified consequences are financial consequences, leakage of confidential data, leakage of personal data, unavailability of device or service and data loss or corruption. The final risk event - consequence model as DAG including the local conditional and marginal probabilities is illustrated in Figure 26.

Based on Figure 25, The identified risks' probabilities follow a long tail wherein the most probable risks include unintentional data disclosure, failures of device or network, shoulder surfing or eavesdropping and loss or theft of device. Experts believe that almost $50 \%$ of users share more information to other parties through their smartphones than they acknowledge or would be

willing to share. From all the consequences, leakage of personal data will happen more probably based on Figure 26, than confidential information related to the user's employer. Governmental users have significant incentives to use encryption and strong authentication, consumers often value price and ease of use more than security. Both are affected by nine risk events. Their causal effects to the leakage of personal and confidential data can be inferenced by analyzing the delta of two scenarios; the risk events will materialize, and they do not materialize. The results are shown on medium- or high-severity as personal (Figure 27a) and as confidential data leakage (Figure 27b). According to the graphs, the results resemble each other. However, two clear differences exist between these results: all risk events have a significantly higher probability of affecting personal data than confidential data and the effect of unintentional data disclosure is much higher relative to other risks' effects on leakage of personal than confidential data.
![img-25.jpeg](img-25.jpeg)

Figure 26. Information risk assessment model for mobile device usage containing risk events and consequences. Figure modified from Publication 6.

Based on similar sensitivity analysis, loss or corruption of data related to smartphone usage seems to be a relatively unlikely scenario and most often caused by loss or theft of device or technical failure of device. Also, low-severity and medium-severity unavailability is very rarely caused by anything other than technical failures of the device or network. On the other hand, high unavailability is rarely caused by anything other than loss or theft of the device.

Multiple implications are proposed for the user of mobile devices: users should ensure that their devices' built-in security features are enabled, especially a passcode and restrictions against installing applications from outside the official application store. Second, they should familiarize themselves with

the privacy settings and terms of mobile applications. Third, users should regard their smartphones as untrusted devices, wherein a minimal amount of private or confidential information should be stored on them.
![img-26.jpeg](img-26.jpeg)

Figure 27. Consequences as probability (describing medium to high severity levels) when the risk events materialize vs. does not materialize. Left (27a) personal and right (27b) confidential data. Figure is modified from Publication 6.

# 5.4.2 Availability of PSS network 

The risk assessment for availability of PSS service contains all the factors described in Figure 12. The model as a causal Bayesian network structure is illustrated in Figure 28. The used marginal probabilities for risk triggers and controls are depicted in Figure 29. They are based on the probability estimations of experts, existing statistics and discovered occurrences during a year.
![img-27.jpeg](img-27.jpeg)

Figure 28. Risk model structure for PSS services. Colour coding of badges are risk triggers (blue), controls (green), risk events (red), mitigants (yellow), different level of consequences (grey) and final target (black). Figure is modified from Publication 5.

![img-28.jpeg](img-28.jpeg)

Figure 29. Marginal probabilities for risk triggers (blue) and controls (green). Figure is modified from Publication 5.

The model was used to estimate the overall effect of triggers on the availability of a PSS network by calculating Normalized Mutual Information (NMI) between each of the triggers and the target by keeping the control distributions as they are. Natural Disaster ( $\mathrm{NMI}=11.5 \%$ ), Cyber Attack ( $\mathrm{NMI}=10.4 \%$ ) and Bad Operations by Own Personnel ( $\mathrm{NMI}=5.8 \%$ ) have the strongest dependency with the Service Availability, whereas the NMI for the remaining of triggers lies between $1.5 \%$ and $0.01 \%$. Similarly, the effect of the controls was estimated using existing probabilities for the risk triggers, by comparing the delta between the availability with full control and no control. As can be seen from Figure 30, due to the binary variables, the relationship can be drawn as linear. Controls such as Duplicated Links, Aggregates, Real-Time Traffic Monitoring and $N$ Plus 1 have the highest slope, i.e. changes in their values mostly influence the availability value. However, the default value of $N$ Plus 1 was already set at $99 \%$, so it has no additional effect on the Availability. From these findings, we can conclude that the Availability can be improved by using different control values compared to the current situation.

![img-29.jpeg](img-29.jpeg)

Figure 30. The capability of controls to reduce the effect of risk triggers on the availability of PSS Service, when controls are changed from 0 (no controls) to 100 (all possible controls), one at a time. Figure is modified from Publication 5.

By adjusting all triggers to their maximum level, Availability of 99.85\% can be achieved, but based on the study this is not economically feasible. A practical Availability target of $99.8 \%$ (i.e., the PSS service is 18 hours annually not available) is proposed, which can be achieved by selecting $92 \%$ completion within all three most effective controls: 1) Aggregates implemented in $92 \%$ of base stations (compared to the current situation of $15 \%$ in the model); 2) Duplicated Links existing in $92 \%$ of base stations (compared to the current situation of $1.5 \%$ duplicated), and; 3) Real-Time Traffic Monitoring covering $92 \%$ of traffic compared to the current value of $5 \%$. By using the commercial network as a backup, the Availability of the Service can be improved further from 99.8\% to 99.9\%.

# 5.5 Results summary 

The main contributions are twofold. On one hand, the contributions are related to the documentation and utilization of a Bayesian network for multiple differing research problems, which can then act as a guide for further research. On the other hand, the contribution is in analyzing the popularity of features in mobile devices over time to gain a better understanding of mobile market evolution in Finland, in the segmentation of mobile service users, in analysis of how users' age is related to mobile service usage behaviour, and, finally in the assessment of risks pertaining to the availability and use of mobile devices and services.

Table 14 both restates the research questions and summarizes the main thesis results in relation to each research question and publication. These results, complemented with chapter 2 ("Theoretical background") and chapter 3 ("Evolution of mobile services in Finland, 1998-2019") answer the research problem: "How can Bayesian networks be utilized to analyze, model and characterize mobile service and device usage?"

Chapter 2 provides a theoretical background about Bayesian networks for RQ1. It is required to understand descriptive, predictive and explanatory analysis processes consisting of all the steps from the data preparation and from the model creation to the model interpretation. Special emphasis has been put in this thesis on the missing data management, discretization as well as construction of predictive and causal models. Several different data types have been used in the studies: a survey, mobile device usage events (handset measurements), retail sales data and tacit knowledge. Each publication contributes partially to RQ1, covering the processes either for descriptive, predictive or explanatory modelling with Bayesian networks. The thesis provides a versatile but compact representation of the methods and processes which can be used in connection with Bayesian networks and a set of useful real-world analysis examples.

Table 14. Summary of main thesis results in relation to each research question and publication


Popularity of a mobile device model was defined as the number of sold units (discretized into popularity ranges) during a year. The learned TAN model, where the features acted as predictor variables and unit sales as the label, predicted well the popularity in each popularity range and year. This outcome provided a needed base to further study RQ2. In particular, the trend and structural break analysis about the changes as a function of time provided new information about what were features which predicted the popularity and when did they predict vs. not predict. Part of the findings are contradictory to previous studies. When adding other background information to the results, new findings about the changes in the Finnish mobile market were made. As a summary, three of the changes can be highlighted. A camera and its quality became an important purchase criterion during 2008 and at the same time the weight of the Nokia brand in the mobile device purchase phase started to decrease among the buyers. In 2011 multiple new models arrived on the Finnish mobile markets, the strategic partnership between Microsoft and Nokia started and tablets began to interest buyers. All of these factors decreased the predictive power of the previous year's sales on the sales of current year, which has been a predominant phenomenon in previous years.
The thesis provides multiple answers to RQ3. Mobile service users have been segmented into three main parts based on users' service usage behaviour and their gender and age. This segmentation, for example, indicated, that not all the mobile service users of Aalto University community are early adopters as expected based on the previous studies. Mobile services were classified in a novel way based on how they contribute to the usage intensity of other services. With help of an extensive dataset and a causal analysis, human age was proved to be a major contributor to the different mobile service usage behaviours. This finding is in line with the findings from previous studies, which used more limited samples.

RQ4 has been addressed with help of two different risk problems, but with the same approach in each. The key insight has been in using the probabilistic risk assessment structure of Fenton and Neil (2012). It enables a logical top-down approach especially for assessment, where no data exist. Both studies tackle topical themes with useful new information for practitioners.

# 6. Discussion 

This chapter discusses the research implications as well as practical implications. Moreover, methodological implications for both researchers and practitioners are discussed, before concluding the thesis with a discussion on research and methodological limitations and future research.

### 6.1 Research implications

Overall, due to the diverse nature of research questions, the methodological question (RQ1) is handled as its own subsection and here the focus is in the primary questions (RQ2 and RQ3).
A study of mobile device features as a choice criterion for the device has been a popular research topic during the 2000s. However, based on the literature review results from 16 studies covering the years 2002 - 2012, twenty important device features as choice criteria were found - however considerable variation appeared in the criteria among the studies. Because of this variation, it is impossible to discover trends or structural breaks in choice criteria just based on previous studies.

This thesis offers new viewpoints and accurate but, in some cases, also contradictory information for researchers about mobile device choice criteria. Empirical observations suggest, that one trend and multiple structural breaks can be found in Finland between 2004 - 2013, when studying how features predict the device popularity as a longitudinal analysis using predictive models. Many of the structural breaks are explained with the changes of the penetration of features in in the new device models sold. However, for instance, the explanations behind the structural break for brand and changes in predictivity of sales in previous years require additional information to infer the reasons behind. The changed role of Nokia in purchase decisions is expected to be a reason for the structural break in the brand. The Nokia brand positively affected purchase decisions up to 2007 but 2008 was the first year, when Nokia's brand effect started to decrease among Finnish buyers. Also speculated, that a change in pricing for mobile data usage at beginning of 2007 in Finland might have been the reason for the need for more "Internet savvy" devices. Multiple quick changes in mobile markets in Finland was an obvious reason why the sales volumes of the previous year were no longer able to predict the sales of the current year in 2011 and onwards as they had done prior to 2011. The price of the device was not seen as a

driver for popularity of a mobile device over multiple years, which is contrary to the findings from previous studies.

Also, a novel perspective was proposed to group and treat the mobile services as mediators and non-mediators, which deepens researchers' understanding about the role of some services "as a gateway" to the usage of other services, and which may explain some of the differences in the service usage intensity and their perceived importance.

Compared to the segmentation of the service usage behaviour, for example, to five classes based on diffusion of innovation theory of Rogers (1995), this thesis studied the usage segmentation by clustering service usage intensity of each users to an optimum three levels. This method and the results bring more dimensions than just the adoption level for mobile service usage study, e.g., how to characterize the usage in each segment, how the diversity, age and gender vary in each segment. When comparing the segments found in the thesis with user segmentation by Rogers, the segments seem to fit best in the following way: experimentalist fits best with the category consisting of innovators and early adopters, heavy communicator fits with early majority users and basic smartphone user fits with the category consisting of late majority users and laggards. Therefore, we can conclude, that not all the Aalto University community users are early adopters as indicate in previous studies.

According to the literature survey in Publication 3, less than ten research papers studied the importance of communications services with respect to the age of an individual. These studies handle the services such as SMS, IM and email and find dependences between the age and usage of the mentioned services: when age increases, the usage decreases. In addition, the studies of Thayer and Ray (2006) show a clear effect of age on online communication as well as relationship building preferences regarding friends and strangers: when age increases, the amount of online communication activities starts to decline. On the other hand, according to Rogers (2003) inconsistent evidence exists about the relationship between age and innovation adoption. Half of the diffusion studies analyzed show no relationship.

This thesis confirms that age effects clearly the usage intensity and perceived importance of communication services. Also, it confirms the findings of Thayer and Ray (2006). The results of the thesis increase the understanding of the role of an individual's age on the perceived importance and usage intensity of mobile services in Finland in the early 2010s.

# 6.2 Practical implications 

Beyond the research implications, the results have also practical implications for communication service providers, mobile device manufacturers, mobile net-

work operators, business analysts and users of mobile devices. The thesis provides novel information for business analysts in the form of trends and structural breaks in Finnish mobile markets based on mobile device features, which might help in explaining some other hypothesis. Also, the expected end time of the era of hardware-driven market model pushed by Nokia and start time of software-driven market model adopted by Apple and Google in Finland may help to understand and identify the reasons behind this observation. This thesis also shows for manufacturers and CSPs, that it is hard to predict the future popularity of a mobile device based on historical and current technical features, because typically there are no long-lasting trends (only one discovered in this study) and the growing or decreasing part of a structural break often lasts only three to four years. Also, the pricing seems not to be a regular indicator of popularity.

This thesis underlines the importance to understand a mediator role of certain mobile services. This offers a new insight for service planners and device manufacturers. They can rank the services to non-mediators, mediators, and both, and managers can pay special attention to the activities which could increase the intensity of mediator services (e.g., in terms of usability), in order to control the increase of the usage of the target services, for instance.

The thesis suggests, that the individual's age and mediating role of some services (in 2011 in Finland it was Facebook \& Twitter types of services) together should be carefully considered by device manufacturers and CSPs while planning the devices and services for target users.

For the mobile device users, the study contains multiple implications concerning the usage of a mobile device correctly in order to avoid information lossrelated risks. The risk assessment about the availability of PSS services contains implications for the PSS network operator in Finland to control the availability level in an optimum way.

# 6.3 Methodological implications 

The core method used in this thesis, i.e., Bayesian networks, contains multiple methodological implications both for researchers and practitioners:

- For researchers, the use of Bayesian networks is an alternative statistical approach especially when a white box model is preferred, and a synthesis of observational data and expert knowledge is required.
- A Bayesian network structure, constructed with MWST and MDL scoring, offers an initial and intuitive way for both researchers and practitioners to discover visually important dependences and structures from the data for further analysis. Visual and numerical analysis based on this structure can be called a descriptive analysis with Bayesian networks. The calculation of Node Force from that network highlights numerically the relevant variables for further analysis.

- The proposed processes related to the construction of a causal Bayesian network model offers researchers a fast way to implement explanatory analysis and SEM-like analysis.
- The used $\mathrm{D}_{\mathrm{KL}}$ metrics to calculate the strength of causal effect or predictive power of certain variable (compared to another variable) offers researchers an innovative way to compare dependences without any assumptions about linearity.
- The used risk assessment model skeleton and process is a recommended approach for both researchers and practitioners to quantitatively assess risks, their controls, mitigations and consequences.
- The proposed process related to the discovery and documentation of silent knowledge with Bayesian networks offers a way for organizations to collect valuable information from their experts, often dispersed geographically. This information can then be used in what-if analysis and optimization tasks in the strategy creation process, for instance.
- The process used in the thesis for analyzing the popularity of mobile device features as a function of time provides a straightforward method for marketers to analyze potential factors affecting the popularity of future device models.

Finally, the thesis aims to highlight the importance of understanding the difference between predictive and causal models when implementing statistical analysis and interpreting its results.

# 6.4 Limitations 

The thesis studies usage behaviour of mobile services and devices, which is a time-dependent phenomenon. As discussed in chapter 3, the whole mobile ecosystem, i.e., mobile networks, devices, services, service providers and revenue models have evolved considerably even during this thesis research. The analyzed datasets describe different time periods. The GfK dataset covers the circumstances in 2004 - 2013, Aalto University and Ficora datasets describe the period in 2009 - 2011, and the opinion data for risk assessment mirrors thinking in 2014 - 2015. In this light, empirically studying the usage behaviour of mobile services and devices evidently has a snapshot nature. Therefore, it is difficult to assess from all the found patterns which of them represent some more underlying and long-term aspects and which are more short-term. Besides, the thesis focuses on Finland, which due to the dominance of Nokia has historically been a special mobile market area. Therefore, the results cannot be generalized to describe the situation in any other country nor to describe the situation, for example, today. However, the study about trends and structural breaks indicate, that features indeed act only as a short-term factor to assess the popularity of a device and only the sales of previous year, brand and sales months are potential indicators which may have relevance also in the longer term. Similarly, we can speculate, that the user's age has still today an important effect on the mobile service usage behaviour as it used to have in 2009 - 2011 and before it.

On the level of details, there are some additional limitations in the used datasets. The operating system in the Aalto University dataset is biased towards Symbian. Ficora's survey lacks multiple mobile services compared to the Aalto University dataset and the GfK dataset contains only pre-installed services. Further, the GfK dataset lacks information about marketing effort spent for the models as well as background information about the buyers which both would help to interpret the results. Besides, the definition of a type-B structural break used in this thesis excludes potential structural breaks in 2004 / 2005 and 2005 / 2006 and similarly 2011/2012 and 2012 / 2013.

In respect to RQ1, the thesis presented multiple ways to construct a Bayesian network, but used only discrete data for the analysis. That is to say, the continuous variables were discretized into intervals. This approach is most popular in constructing Bayesian networks and has benefits, as discussed in the thesis. But for the sake of completeness, for example the model construction with Ficora's dataset (especially when using the pre-processed final data with less than 20 variables) could have been implemented by using a mixed modelling approach. After all, the choice was to focus on non-parametric learning and discrete variables and not to seek to address all possible methods. Similarly, all the learning algorithms in the thesis used an MDL score-based method. As discussed in the thesis, constraint-based learning has long traditions for causal learning. For example, the study about causal effect of age could have been implemented by using (e.g., in parallel) constraint-based learning for the sake of completeness and for a reference model. However, as discussed in the thesis, recent studies have shown, that score-based learning with MDL in general is a good choice for both predictive and causal modelling, especially when knowing that still today causal modelling needs expert support to finalize the model. The study used two different commercial tools to construct Bayesian network models and for inferencing with the models. There are multiple open source tools available to create similar models and inference capabilities to those that have been used with the commercial tools. They also provide better openness for researchers in the form of publishing the used algorithms compared to often proprietary algorithms provided by commercial tools.

# 6.5 Further research 

The dissertation provides several avenues for future research. First, the method used to analyze factors affecting the popularity of mobile device models as a function of time seems worth more attention. Future research should include more background information, such as marketing effort for the models, some additional information based on the survey held in connection with the sales transaction such as buyer's background information, buyer's preferences, as well as recommendations received from others. In addition, the time period should extend to the present day. The research target could be not only to explain well the past but also to predict the future.

Second, an obvious future research topic would be to extend the research about segmenting the usage behaviour from a snapshot type of study to longitudinal analysis, and to study the disparities between Android and IOS service usage behaviour and the behaviour between regions and countries, for example.

Third, causal analysis around age and mobile service usage behaviour needs still more attention. The thesis clearly indicates, that when the age of people increases, they seem to get stuck in familiar communication methods and slowly their communication using mobile devices start to decrease. This was particularly visible among the individuals over 60 years, i.e., among those who learned to use mobile calling and text messaging at 40 to 50 years of age. More information is needed about causal relationships between age and mobile service usage behaviour in order to understand how to keep the communication between individuals active also in the older age or how to enhance the telemedicine for elderly people, for instance. For this kind of effort, the Ficora type of dataset from multiple years is required.

Fourth, as already discussed before, an extended information risk model could be created for identifying initial triggers for the risks as well as risk controls and mitigants in order to identify the most dangerous practices of smartphone usage as well as to infer which security measures would be most useful for prevention or mitigation of risks.

Finally, one avenue for future research would be to study the methodological differences in constructing causal Bayesian networks. As an example, what are the differences using purely constraint-based learning compared to expert assisted score-based learning?

.

# Aalto University 

School of Electrical Engineering
Department of Communications and Networking
www.aalto.fi

BUSINESS + ECONOMY

ART +
DESIGN +
ARCHITECTURE
SCIENCE +
TECHNOLOGY
CROSSOVER
PROCTORAL
DISSENTATIONS