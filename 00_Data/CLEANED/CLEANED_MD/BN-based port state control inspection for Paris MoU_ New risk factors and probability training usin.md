# LJMU Research Online 

Liu, K, Yu, Q, Yang, Z, Wan, C and Yang, Z
BN-based port state control inspection for Paris MoU: New risk factors and probability training using big data
http://researchonline.ljmu.ac.uk/id/eprint/16959/

## Article

Citation (please note it is advisable to refer to the publisher's version if you intend to cite from this work)

Liu, K, Yu, Q, Yang, Z, Wan, C and Yang, Z (2022) BN-based port state control inspection for Paris MoU: New risk factors and probability training using big data. Reliability Engineering and System Safety, 224. p. 108530. ISSN 0951-8320

LJMU has developed LJMU Research Online for users to access the research output of the University more effectively. Copyright © and Moral Rights for the papers on this site are retained by the individual authors and/or other copyright owners. Users may download and/or print one copy of any article(s) in LJMU Research Online to facilitate their private study or for non-commercial research. You may not engage in further distribution of the material or use it for any profit-making activities or any commercial gain.

The version presented here may differ from the published version or from the version of the record. Please see the repository URL above for details on accessing the published version and note that access may require a subscription.

For more information please contact researchonline@ljmu.ac.uk

# BN-based Port State Control Inspection for Paris <br> MoU: New Risk Factors and Probability Training <br> using Big Data 

Kezhong Liu ${ }^{1,4}$, Qing Yu ${ }^{1,3,5}$, Zhisen Yang ${ }^{2 *}$, Chengpeng Wan ${ }^{4}$, Zaili Yang ${ }^{5}$<br>${ }^{1}$ School of Navigation, Wuhan University of Technology, Wuhan, China<br>${ }^{2}$ College of Urban Transportation and Logistics, Shenzhen Technology University, Shenzhen, China<br>${ }^{3}$ School of Navigation, Jimei University, Xiamen, China<br>${ }^{4}$ National Engineering Research Centre for Water Transport Safety (WTSC), Wuhan, China<br>${ }^{5}$ Liverpool Logistics, Offshore and Marine (LOOM) Research Institute, Liverpool John Moores<br>University, Liverpool, UK

*Corresponding author: Zhisen Yang
Email address: yangzhisen@sztu.edu.cn

# Abstract 

Given to the increasing traffic volume in ports in recent years, ship selection and inspection procedure in the port state control (PSC) should be improved to reduce any unnecessary delay caused by the inefficient inspections. This study aims to newly use a data training technique and the newest PSC data to improve the usage of Bayesian Network (BN) to assess detention risk to a point where risk factors are identified, interrelationships among the factors are analysed and prior probability training based on big data is obtained more easily. To construct the BN model, a Bayesian theorembased machine learning approach is adopted to ensure the obtained model is objective and reliable. The model is developed based on 1880 inspection records in the Paris Memorandum of Understanding (MoU) regime between 1st January 2017 and 31st March 2020. The obtained model not only present the probability distribution of each factor but also explore interrelationships among them. Compared to the Ship Risk Profiles (SRP) model, the used data-driven structure learning algorithm is more convenient and useful. The analysis results provide insights for ship owners to manage ship detention risk while support port authorities to prioritize the ship checklist and utilise more efficient ship inspection.

Keywords: Port state control, Bayesian networks, Machine learning, Ship Risk Profiles, Maritime safety

# 1. Introduction 

Over the past several decades, seaborne trade has seen a remarkable development as waterway transport carries the vast majority of international trade contributing to around 80 and 90 per cent of the global trade by volume and about 60 to 70 per cent by value (Review of Maritime Transport, 2018). This predominance is particularly pronounced in developing countries. With the increase of world fleet and seafarer registering in over 150 nations, the safety of maritime transportation becomes more critical and important. However, the safety management of maritime transportation is still facing challenges (Wan et al., 2018; 2019). According to the Safety and Shipping Review 2020, the numbers of world shipping accidents significantly increased in last four years, from 1129 in 2017 to 2815 in 2019 (AGCS, 2020), some serious cases are the fire disaster of Norman Atlantic, the sank of Bulgaria, and the sank of Express Samina. Therefore, it is of vital importance to ensure maritime safety around the world.

The port state control (PSC) is a complementation measure to flag state control, through which port authorities are rendered the ability to inspect foreign vessels in their own ports. Thus, they are able to detain the estimated sub-standard vessels in their waters for accident preventions (Yang et al., 2018). Further in 2011, in order to improve the efficiency of the PSC inspection, New Inspection Regime (NIR) was launched and implemented by Paris Memorandum of Understanding (MoU). Once accepted by authorised counties, the MoU NIR significantly improves the performance of vessel management by prompting the vessels to obey maritime safety regulations and rules so that it was viewed as the most significant change that transforms and modernizes the PSC inspection system in recent years (Paris MoU, 2011). One of the remarkable features of the NIR is the establishment of a ship risk profile (SRP) system, which is used to determine the risk priority of ships before inspections, the intervals between the inspections of a ship, and the scope of the inspections based on a risk associated information system. The SRP evaluates the risks of ships by using a set of generic factors such as vessel type, vessel age, and company performance. The criterion within each factor is weighted to reflect their relative influence to ship detentions. If the weighting points of an arriving vessel exceed the set threshold value (which is 5 points), it will be estimated as high-risk level, indicating that it has a high probability to be inspected in ports. Additionally, if the detected deficiencies of the vessel are so serious that it should be rectified before its departure, then the vessel will be detained, because a substandard vessel is more likely to cause maritime accidents and thus brings potential

hazards to maritime safety. Therefore, it is necessary and significant to study the factors influencing ship detention risk and investigate the relationships among them. This could help to improve the performance of the SRP system by providing more accurate results, and make it more suitable for dynamic situations, so as to improve the overall safety of maritime shipping.

Reviewing of literature reveals that previous studies in the risk-based PSC field have made significant contributions including the employment of advanced uncertainty models (i.e., BN) to improve the inspection efficiency, among which Yang et al., (2018, 2019, 2020), and Wang et al., (2019) are illustrative examples. Despite the effort on risk-based PSC in recent years, previous use of data driven BN in PSC still reveals several research challenges which have theoretical implications not being well dealt with in current literature and cannot be easily solved without developing new approaches, based on the incorporation of our analysis on these studies and other resources. 1) Current data training method in BN-based PSC risk studies used in Yang et al. (2018) and Fan et al. (2020) is inefficient; 2) the factors influencing ship detention are not fully explored as listed on Paris MoU website (Paris MoU official website); 3) data used to model the interdependency among the influencing factors are old, not being able to reflect today's PSC risk demand and safety practice (Paris MoU Detention List); 4) previous studies were more focusing on theoretical model development, leaving very limited insightful policy implications explored.

In view of this, this study aims to newly use a data training method to improve BN performance in assessing ship detention risk in PSC through the identification of new risk factors and configuration of their interrelationships using the newest big data. To construct the BN model, a Bayesian theorem-based machine learning approach is introduced and applied to capture the characteristics from historical inspection data from Paris MoU. It relieves the complexity of developing a BN while ensure the obtained model is objective as the model structures are purely data-driven. In terms of the network training, the BN is established not only to present the probability distribution of each factor but also to explore interrelationships among them.

The main contributions of this study include: 1) A new data-driven structure learning algorithm is applied to develop the BN model, which is more convenient compared to traditional ones (i.e. TAN learning used in Yang et al., 2018; Fan et al., 2020) as it does not need to set a target node manually; 2) the interrelationships among major factors in SRP systems influencing ship detention are revealed comprehensively; 3) it provides

insightful policy implications for ship owners to manage ship detention risk while support Port State Control Officers (PSCOs) to priories the ship checklist and utilise more efficient ship inspection; 4) the regulations and rules (i.e. SRP selection system, inspection procedure) in PSC inspection system could be improved based on the obtained findings via detailed discussion.

The rest of the paper is organized as follows. Section 2 overviews the existing studies related to PSC inspection and the application of BN methods in the maritime field. Section 3 describes the main methodologies and the framework used to develop the proposed detention risk assessment model, which is followed by the model construction process in Section 4. Section 5 discusses the research results including results analysis, comparative analysis, and research implications. This study is concluded in Section 6.

# 2. Literature review 

Since the implementation of NIR in 2011, PSC inspections have received increasing attention from the academic field due to its importance and significance to alleviate maritime risks and to ensure maritime safety. Different types of approaches have been used to analyse the PSC inspection performance from both qualitative and quantitative perspectives. It is noted that in this section, only the research considering the implementation of the NIR are included in order to provide more relevant reference.

### 2.1 Studies on PSC inspection

### 2.1.1 Research on PSC inspection systems

1) Ship deficiencies

Based on the Tokyo MoU inspection database, Tsou (2018) used association rule mining techniques to examine the relationships between detention deficiencies and external factors, as well as the relationships between detention deficiencies themselves. The research results provided countermeasures to reduce the detention rate of vessels, improve working efficiency of staff members, and reduce the adverse influences brought by substandard vessels. Chung et al. (2019) conducted similar research, indicating that less attention was paid to discovering the correlations among ship deficiencies. Fu et al. (2020) proposed an improved Apriori algorithm-based inspection model to explore the intrinsic relationships among ship deficiencies. The experimental results can be used as a guideline for PSC inspections.
2) Improvement on the PSC inspection system

Although the implementation of NIR is a significant promotion of PSC inspection practice, scholars suggested that there are still rooms for further improvement. Focusing on the Concentrated Inspection Campaigns (CIC), Cariou et al. (2015) applied quantile regressions to the number of deficiencies to improve the selection process for some specific types of deficiencies of CIC. Yang et al. (2018a) pioneered a data-driven BN development to aid port authorities in substandard vessel detection to deal with the problem that there is a lack of tacking dynamic PSC risks in different environments in practical application. Later in the same year, based on the BN model, Yang et al. (2018b) proposed a risk-based game model between ship owners and port authorities to help port authorities select the optimal PSC inspection policy.

Efficiency improvement is another research direction. Fan et al. (2019) employed a BN model with greedy thick thinning to identify key deficiency items, thus helping port authorities to simplify inspection procedure and improve inspection efficiency. Similarly, Wang et al. (2019) developed a BN non-parametric classifier to replace the current SRP selection scheme. The results showed that the proposed classifier can discover $130 \%$ more deficiencies than current practice.

# 3) Effectiveness and influence of NIR 

Recently, more and more ports and regional MoUs joined the NIR, which enlarges the sphere of influence of the NIR. Due to this, some researchers turned their attention to the effectiveness and influence of NIR. Based on the previous studies, Yang et al. (2020) conducted a comprehensive comparative analysis from both qualitative (i.e., KPI analysis) and quantitative perspectives (i.e., BN model analysis) to clarify the impact of the NIR. The results revealed that most of the influences brought by NIR are positive, no matter on vessel quality and inspection system. Taking advantage of binary logistic regression and decision tree, Xiao et al. (2020) demonstrated some important characteristics of NIR, for example, vessel age, vessel type, flag states and number of deficiencies are considered significantly in NIR.

### 2.1.2 Research on risk factors influencing PSC inspection

Another dimension in PSC risk study is the analysis of factors influencing PSC inspection. Some studies focused on vessel-related factors (such as vessel age, and vessel type) and inspection-related factors (such as inspection type, and deficiency type), while the others placed emphasis on aspects like inspection background. Hanninen \& Kujala (2014) developed a BN model to explore the dependencies of PSC inspections and ship's involvement in maritime accidents and incidents based on PSC

inspection records collected from Finnish ports. The results revealed that vessel type, inspection type, and the number of structural conditions is among the most influencing factors on PSC inspection. Focusing on the factors influencing vessel detention, Chen et al. (2019) proposed a grey rational analysis (GRA) model with improved entropy weight to investigate how much the varied factors influence the ship detention under PSC inspection, and to identify key factors leading to ship detention. The research results could be used by port authorities to guarantee shipping safety and environmental protection. Graziano et al. (2018) pointed out that the inspection commitment, inspection quality and the professional competence of PSCOs could influence the inspection results as well.

In view of the above-mentioned, it can be seen that PSC inspection is an important research area that has been widely discussed in the maritime transportation field. However, most of the existing studies are relevant to general inspection performance or variable selection. Few studies have been conducted on the analysis of SRP, let along the assessment on the interrelationships among ship detention risks. The SRP system, as one of the most important changes introduced in NIR, was overlooked. If we go through the relevant regulations and rules formulated by International Maritime Organisation (IMO) and regional MoUs (i.e., Paris MoU, Tokyo MoU), it is not difficult to find that SRP is an important item in PSC inspections. The implementation of NIR can aid port authorities to select high-risk vessels at a cost-effective manner, as well as aid ship owners to do self-assessment before its voyage. Meanwhile, the results provided by the current SRP are not accurate to some extent. For example, even if a vessel meets all of the requirements of PSC inspection, it still has the possibility to be classified into high-risk level, only because it is an old vessel. In addition, the lack of accuracy of SRP results blur the difference between vessels in terms of detention risk. This reveals a research gap to be fulfilled in this area.

# 2.2 The development and challenges of BN-based PSC inspections 

Since PSC inspections play an increasingly important role in maritime safety area, more and more researchers stepped into this field in the past two decades. It is evident by the increasing number of relevant papers since 2011 when NIR was initiated. The following table illustrates the development of the risk assessment methods applied in this field in the past decades.

Table 1. Overview of risk assessment methods applied in maritime safety

(2018, 2020) | BN | to create a detention rate prediction tool for port authorities and reveal the importance of NIR | provides important insights to seek the optimal inspection policies under different environments in NIR; revealed that it is beneficial to implement NIR for PSC inspection system, vessel quality and maritime safety  |
|  Yan et al.
(2021) | Balanced random forest | to predict ship detention at the Hong Kong port | the BRF model is much more efficient and can achieve an average improvement of $73.72 \%$ in detained ship identification  |

|  Wang et al.
(2021) | Bayesian
Information
Criteria | to analyse the dependency and interdependency among the factors influencing detention | safety condition and technical features are the most influential factors concerning ship detention  |
(2019) | grey rational analysis | to identify key factors of detainment to guarantee shipping safety and environmental protection | results could be used by port authorities to develop the suggestions and countermeasures of reducing ship detention  |

Taking advance of causal inference, BN can be used to analyse the importance degree of risk factors and simulate the interactions between them. When applied in maritime studies, BN shows its superiority over traditional risk assessment approaches. The capabilities of bi-directional analysis and relationship revelation among factors make it a widely applied method in the maritime field. Table 2 illustrates some representative and valuable studies in risk assessment of maritime related systems in the past decade, which demonstrates the popularity and feasibility of BN applications.

Table 2 BN applications in risk analysis of maritime sector


In terms of using BN in PSC risk analysis, Yang et al., $(2018,2019)$ carried out ship detection risk studies from analysis (only BN ) and management (the hybrid of BN and game theory) perspectives. These original studies stimulate follow-up investigations such as Wang et al., (2019) which used the BN as a base for rational inspection resource allocation, and Wang et al., (2021) which extended ship detection to detention risk analysis.

Specifically, Table 3 lists the relevant research of BN application in the PSC inspection area which provides for good reference for its further usage in SRP improvement studies.

From Table 3, it is obvious that BN has been widely applied in PSC inspection area on many topics, and if we go through these literatures carefully, one remarkable characteristics of research in this area could be found: The network construction approaches are mostly data driven.

Table 3 BN applications in PSC inspections


2 Normally, there are two ways to obtain the network structure, one is using human
3 knowledge or historical experience, the other is data-driven approach. Normally, to
4 construct a data-driven BN model, hundreds of thousands of data is required to improve
5 the accuracy and reliability. No matter wat type of data-driven approaches is, the
6 essence of these approaches is actually an optimization problem, aiming to find out the
7 best match option for the relationships among different nodes in the network through
8 the obtained data. However, although the latter one is more objective and accurate, most
9 researchers in maritime field prefer the former way because of the difficulty in
10 collecting data. In recent years, there is an increasing trend in choosing the latter one in
11 PSC inspection related research, which is evidenced by relevant studies (i.e., Yang et
12 al. 2018a; Wang et al., 2019). Specifically, there are many types of approaches applied
13 in PSC inspection research, i.e., repeated high-climbing algorithms (Hannien \& Kujala,
14 2014), Tree augmented naïve learning approach (Yang et al., 2018a; Wang et al., 2019),
15 Bayesian search algorithms (Yu et al., 2020), and other advanced methods. Among
16 them, TAN learning and its derivative are the most popular algorithm adopted by many
17 researchers, not only in PSC inspection, but also in the whole maritime safety field.
18 However, although showing great popularity, TAN learning still has some limitations
19 demanding prompt solutions: 1) the directions of relationships between nodes in the
20 model are undefined; 2) the conditional probability table grows too huge when there
21 are many factors in the model, leading to the requirement of large amount of data.

22 In this research, a novel structure learning approach is proposed to define the
23 correlations between the factors in the constructed networks, which is capable of
24 solving the abovementioned issues effectively. The application of this algorithm, as
25 well as the in-depth analysis on policy implications, highlight the novelty of this
26 research.

# 3. Methodology 

2 To model the SRP risk from inspection databases, a framework is developed in this section, which consists of four steps: data acquisition, variable identification, BN construction and validation.

### 3.1 Data acquisition

6 The member countries share their inspection records to the regional MoU that including Paris MoU (European countries, Canada) Tokyo MoU (Pacific Ocean), Acuerdo Latino (South and Central America), Caribbean MoU, Indian MoU, etc. These MoUs provide sufficient inspection records that can be easily acquired from their websites. In this work, we manually collect and analyse the inspection records from Paris MoU covering the period of 2017-2020.

### 3.2 Variable identification

The variable used in the model should be selected to describe the ship situations in the rational manner. In previous studies, the variables used in the BN model refer to designers' experience or PSC inspection lists, which show dissimilarity and inconsistency across the selected factors in this process and then lead to different conclusions. In the meantime, the variables require rational state assignments to better describe attendance attributes. Thus, this framework applies the variable selection criteria in the SRP system due to two reasons: 1) The used variables in the model are consistent with the MoU recommendations, so that a new model is transparent and understandable for all the users; 2) the uses of same variables and criteria not only simplify the data processing procedures but also provide a benchmark to validate the new model.

### 3.3 Model construction

### 3.3.1 BN modelling approach

In this study, the SRP risk will be assessed with data-driven BNs. A BN is a directed acyclic graph consisting of two main components, which are nodes and directed arcs. The nodes donate the relative variables or factors in a system, while the directed arcs are used to describe the relationships among nodes. Each node has a set of finite numbers to represent its variable states (Yu et al., 2021). Normally, nodes are categorised as parent nodes (root nodes) and child nodes (contain intermedium nodes and final nodes). The direction of an arc shows the causation between two nodes, in which the nodes at the tail of an arc are root nodes, while the nodes at the arrow side are child nodes (Yang et al., 2018a).

A BN can be used to analyse a system from both qualitative and quantitative perspectives. In the qualitative term, the graph of a BN structure gives a clear network structure to observe nodes and their dependences. While on the other hand, in terms of the quantitative perspective, the BN follows the Bayes theory, which uses prior probabilities and conditional probabilities to calculate the posterior probabilities (Zhang et al., 2018). Therefore, the development of a BN should cover the following steps: 1) variable selection, 2) state definition, 3) structure determination, 4) conditional mutual information computation between all pairs of attributes, 5) prior probabilities and conditional probabilities calculation, 6) BNs establishment and 7) BNs validation.

In recent years, BNs were becoming increasingly popular in the maritime risk analysis field as they are recognised as an effective tool to model the complicate systems such as ship traffic. However, because of the complexity of marine systems, which contains many impact variables, some difficulties were highlighted in relevant risk assessment research by using BNs. For instance, relationships are difficult to define, the structures of BNs are hard to establish, and mutual information is significantly large to obtain the conditional probabilities (Maria et al., 2012).

1) Relationships are difficult to define and model structures are hard to establish. Because of the complexity of maritime system (the bigger the system is, the more risk factors and casual relationships exist), traditional way (i.e., expert judgment) to construct the structure of BN model is no longer able to support current studies, as it fails to model the casual relationships between different factors objectively and rationally. Hence, more data-driven structure learning approaches based on machine learning are applied in this field to overcome such issue because of the superiority of machine learning methods in casual relationship identification work under complicated situations, which is very helpful when constructing theoretical model structure. For example, the TAN learning (Yang et al., 2018).
2) A common criticism of BN is that the size of conditional probability table quickly grows as more parent nodes are added, leading to complexity and difficulty in obtaining the values. There are two ways to solve this issue according to the literatures, one is defining the risk factors into different layers based on the principal of divorcing approach (Jensen, 2001; Yang et al., 2018), as the hierarchical BN structure can significantly reduce the difficulty of CPT calculation (Huang et al, 2006); the other solution is on the basis of huge amount of data. Once enough data is obtained, the CPT could be obtained based on some optimization algorithms, such

as Expectation-maximization algorithm and gradient descent approach.

# 3.3.2 Developing BN structure from SRP data 

The reliability of BNs strongly rely on the used inputs and the BN structures. As the relationships are defined based on background knowledge or expert judgements, it is difficult to establish a BN structure when too many variables involved (Zhang and Thai, 2016). To overcome this difficulty, this study applies a Bayes-based approach (i.e., Bayesian searching classifier approach) to develop a data-driven BN based on SRP inspection data. The approach identifies observations belongs by using statistical classifications, in which the classifier is built from the SRP data and the potential relationships associated with variables are trained by using Bayesian Search algorithm (BSA) and numerically defined by using a 'Bayesian estimator' (Cooper and Herskovits, 1992).

The BSA assumes a system $X$ contains a set of $m$ impact variables $x_{i}(i \in m)$. Let a variable $x_{i}$ has $n$ possible states as $\left(v_{i}^{1}, v_{i}^{2}, \cdots, v_{i}^{n}\right)$, the SRP inspection database $D$ contains $N$ records, each of which contains a value assignment for each variable in $X$. There are $h$ possible BN structures $\left(B_{1}, B_{2}, \ldots, B_{h}\right)$ that describe interrelationships between the $x_{i}$ and each structure represents a unique interrelation between $x_{i}$ that are identified from the inspection database $D$. In a specific $B_{c}(c \in h), x_{i}$ has a set of parent nodes, which can be presented with a list of variables as $l$. There is a total of $r$ instantiations in the 1 and the $j$ th $(j \in r)$ unique instantiation relative to $D$ is $l_{j}$. Then we define $N_{i j k}(k \in n)$ to be the number of records in $D$ in which variables $x_{i}$ has the value $v_{i}^{k}$ and 1 is instantiated as $l_{j}$. Meanwhile, the sum of $N_{i j k}(k \in n)$ is defined as $N_{i j}=\sum_{k=1}^{n} N_{i j k}$. After defining the above parameters, the likelihood $P\left(B_{c} \mid D\right)$ for $B_{c}$ in the $D$ by using Eq. (1) and (2):

$$
P\left(B_{c} \mid D\right)=\frac{P\left(B_{c}, D\right)}{\sum_{c=1}^{h} P\left(B_{c}, D\right)}
$$

where

$$
P\left(B_{c}, D\right)=P\left(B_{c}\right) \prod_{i=1}^{m} \prod_{j=1}^{r} \frac{(n-1)!}{\left(N_{i j}+n-1\right)!} \prod_{k=1}^{n} N_{i j k}!
$$

and $P\left(B_{c}\right)$ is a constant prior probability for each $B_{c}$. In this way, the structure that obtains the highest score is selected to be the most likely BN structure.

After the relationships among $x_{i}$ being defined, a 'Bayesian estimator' $E$ is selected to calculate conditional probabilities. This study assumes that the conditional probabilities $O_{i j k}$ for $v_{i}^{k}$ in $x_{i}$ are consistent with the Dirichlet distribution (Cooper and Herskovits, 1992), a 'Bayes estimator' $E$ can be used to calculate $O_{i j k}$ for $v_{i}^{k}$ under $B_{c}$ and $l_{j}$ in $D$. This gives the following equation:

$$
E\left(O_{i j k} \mid D, B_{c}\right)=\frac{N_{i j k}+1}{N_{i j}+n}
$$

where $E\left(O_{i j k} \mid D, B_{c}\right)$ is the estimator value for $O_{i j k}$. By using a table to combine all $E\left(O_{i j k} \mid D, B_{c}\right)(k=1,2, \ldots, n)$ under $B_{c}$ in $D$, a CPT for $x_{i}$ is obtained.

# 3.4 Model validation 

A newly constructed model is required to be validated through validation measure to ensure its reliability. Mainly two types of validation measures are suggested in the framework. One is the face validity that checks the rationality of the developed BN in a qualitative manner (Goerlandt and Kujala, 2014), and another is the content validity to ensure the model is practical in its applications (Yu et al., 2020). In the content validity, the priority of the nodes will be identified through a mutual information approach. Nevertheless, the evaluation results can be compared with the SRP system as mentioned in the early Section 3.2.

## 4. Model construction

### 4.1 Data collection

The database is constructed based on the ship inspection records from the Paris MoU website (available at: https://www.parismou.org/inspections-risk/library-faq/ship-riskprofile). The database consists of 1880 ship detention records in countries subject to Paris MoU regime, between $1^{\text {st }}$ January 2017 and $31^{\text {st }}$ March 2020. For the extreme events and data, as their occurrence are too few to be representatives for the relationships in the network, they will not be selected when constructing the model. Meanwhile, in this research, the obtained data has first been refined to better fit the inspection model, hence the construction of BN will not be influenced by this issue.

The inspection data contains the following variables: The International Shipping Management (ISM) company, ship IMO number, certificate issuing authority, ship name, ship charterer name, ship type, flag, gross tonnage, keel data, place of inspection,

1 data of release, duration of detention, defective item code.

# 24.2 Risk variables 

3 This section introduces the risk variables used in the BN model, which are referred to
4 SRP system. As the variables require rational state assignments to better describe
5 attendance attributes, the states are described with a set of linguistic terms (see Table
64 ).

Table 4: Attendance attributes for variables


8 Type of ship. According to the SRP system, the chemical tankers, gas carriers, oil
9 tankers, bulk carriers and passenger ships obtain relatively higher risk weighting points
10 than that of other ship types. The inspections for these types of ship are more frequent.
11 Therefore, few ship types are considered in this study and the proposed division of ship
12 types contains seven categories, which are "general cargo ship", "bulk carrier",
13 "container", "oil chemical gas tanker", "Ro-Ro ships", "tug special activities" and

Age of ship. As suggested in previous studies that 'with an increase of ship age, a vessel's safety level is decreased' (Li et al., 2014), four states from low risk to high risk are assigned to this variable: "age less than 10 years", "age between 10 and 20 years", "age between 21 and 30 years" and "age more than 30 years".

Ship flag. Ship flag refers to the nationality that a ship belongs. According to the annual report published by Paris MoU (i.e., White, Grey and Black flag (WGB) list), the performance of countries is assessed and ranked with different states using 'white', 'grey' and 'black'. The WGB list divides most of the countries into one of these three states from high performance to low performance, in which, a quality flag is stated as 'white' and a poor flag is considered as 'black' flag. For those countries that have not been listed in the WGB list, they are grouped as 'not on list (i.e., unassigned)'. In this study, the most recent WGB list published in 2018 is applied, in which the 'White List' contains 41 countries (e.g. UK, China, Portugal), the 'Grey List' contains 18 countries, and the 'Black List' shows 14 counties are under the risk states (from medium risk to very high risk). In order to investigate the risk differences, more specifically, the ships with 'black' flag are further divided into four states from medium risk to high risk. They include the 'medium risk', 'medium to high risk', 'high risk', 'very high risk'. Thereby, total of seven states are assigned to the ship flag, include 'white', 'grey', 'medium risk', 'medium to high risk', 'high risk', 'very high risk' and 'unassigned'.

Recognised organisation (RO). The performance of recognized organizations (more than 60 inspections in three years) will be evaluated by Paris MoU every year and the evaluation results will be summarized into a performance list and opened to public. In the Recognised Organisation Performance Tables, a four-states-classification is given to describe the RO performance, saying as 'high', 'medium', 'low' and 'very low'.

ISM company performance. ISM company performance is explained as the performance of a shipping management company that implements the International Safety Management (ISM) code. The SRP system evaluates this factor with four states: 'high', 'medium', 'low' and 'very low'. Specifically, a company that has a low ship deficiency rate and a no/short ship detention time in the past 36 months is defined as 'high performance'; while on the contrary, a shipping company is assigned as 'low' performance or 'very low' performance if the deficiency rate is high and detention time is long. The states used in the SRP systems are adopted to this study.

Duration of detention. This factor shows the period of time that a ship is detained by PSCOs. It to some extent describes the severity of ship risk, but it also depends on the type of defectives. In this study, five states are used to describe the factor from a time period perspective. There are 'less than 3 days', 'between 3 and 6 days', 'between 6 and 9 days', 'between 10 and 20 days' and 'more than 20 days'.

Total detentions in past 36 months. This factor refers to the total detentions of a vessel in the past 36 months. According to the Paris MoU, one scenario leading to the refusal of access (banning) is that a ship with black flag has been detained 3 times within a period of 36 months. However, this is a temporarily ban, not a permanent one. The company could make a request asking for a ban lifting, and if it passes a re-inspection at an agreed port of Paris MoU, it will be allowed to access to ports in the Paris MoU region again. For each vessel sailing within Paris MoU region, it will be permanently banned under one condition: 1) after its third ban; 2) it fails to follow the requirements of Paris MoU within 24 months after the third ban happens (Port State Control Committee Instruction 53/2020/06). Therefore, it is not surprised to see some vessels are detained more than three times.

Therefore, this factor is classified into four categories: 'once', 'twice', 'three times', and 'more than 3 times'.

Defective item code. During an inspection, the PSC inspectors may identify one or more deficiencies and include these in the PSC inspection report. They are closely connected with the inspection results and should be treated with care in PSC inspections. Each deficiency has a unique code. Following the list of Paris MoU deficiency codes, all the deficiencies are coded with item numbers, which are grouped into 6 categories in this study, which are crew and environment, document and facilities, operations, pollution, safety issues and others.

Place of inspection. All the ports are grouped based on their country of registry. Most of the inspection records are from 12 countries, which take $85 \%$ of the total number of records, including Belgium, Canada, France, Germany, Greece, Italy, Netherlands, Poland, Romania, Russia, Spain and UK. Records from other counties belong to the state of 'other countries'.

Gross Tonnage (GT). The ship gross tonnage is considered in this study to reflect the ship risk under different ship sizes. States used to describe the ship's gross tonnage are defined as: less than 600 GT, between 600 and 3000 GT, between 3000 and 20000 GT,

2 SRP values. Under the SRP system, the detained ships are evaluated and stated with three risk level which are "low risk ships (LRS)", "standard risk ships (SRS)" and "high risk ships (HRS)" based on their points. HRS are ships which meet criteria to a total value of 5 or more weighting points; LRS are ships which meet all the criteria of the low risk factors and have had at least one inspection in the previous 36 months; The others belong to SRS.

# 4.3 Construction of the BN model 

9 The application utilizes the developed inspection database to characterise the detained ships in the Paris MoU regions by applying Bayesian searching approaches. The probability distributions of the risk variables and their relationships with each other are integrated to construct a BN. By using the Bayesian software "GeNle", the collected inspection database is trained, and the obtained results are presented as a BN and shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1 data training results
17 As shown in Figure 1, approximately $68 \%$ detained ships are recognised in the ship classification organisations with high performance, but ship recognised in medium or low performance organisations take a total proportion of $33 \%$, which is $24 \%$ in medium, $2 \%$ in low and $7 \%$ in very low. This factor closely relates to ship flag and place of inspection. The detention records contain 1241 ships ( $66 \%$ of overall ship numbers)

that registered in white flag countries, $7 \%$ in grey flag countries, $27 \%$ ships that
registered in countries with a certain risk. While, among all detained ships in the database, 301 ships are detained in Russia ports, ranking first, followed the number in Italy (226 ships being detained) and Greece (188 ships being detained). The ship company performance and ships age show relationships with the ship flags. Only $33 \%$ of ships managed with companies in high performance levels. Most of the ships have served for more than 8 years, in which, $32 \%$ of them are between 11 and 20 years, $23 \%$ between 21 and 30 years, and $37 \%$ more than 30 years. $52 \%$ of the detained ships are general cargo ships. Most of the detained ships are between 3000 GT and 100000 GT, $35 \%$ of them are detained due to the deficiencies in the document and facilities. There are $9 \%$ (i.e., 169 ships) of the ships are detained more than 20 days, and $73 \%$ of the ships are detained in the past 36 months for the first time. According to the SRP system, 526 ships are HRS, 940 ships are SRS and 414 ships are LRS.

# 4.4 Validation of the model 

### 4.4.1 Face validity

The rationality of the BN is validated through face validity by comparing the relationships in the model with the expert's background knowledge and previous studies. The obtained BN structure is compared with related research works (Dinis et al., 2020; Yang et al., 2020, 2018) to check if the interrelationships and probability distributions are consistent. It is worth noting that this study aims to develop a BN model to improve the reliability and the rationality of the SRP system and related research works but not to question them, hence the comparison is necessary and valuable.

As results, the developed BN shows great consistency with previous studies, not only on the factors used in the model covering all the possible ship inspection situation but also the relationships among the factors showing great consistency with the understanding of PSC inspections.

In addition, for the purpose of implementing the face validity in an objective way, the data source (i.e., Paris MoU data in the period of 2017-2020) is used to develop another BN by using a fine-turned inspection modelling method (i.e., TAN) that proposed by Yang et al. (2018). During the learning process, the node of SRP is selected as the target node, a total of 19 links among the nodes are determined. It can be noted that the consistency between two BNs (i.e., the BNs developed by BAS and TAN) is proved. Most of the interactions among the nodes are clarified by using two learning

approaches. Meanwhile, BSA model shows its superiority over other techniques (i.e., TAN Training) in some aspects:

1) Based on the algorithms used in TAN, all nodes need to be considered as the consequence of the target node, which reverses the causal direction among nodes. Although this is reasonable from mathematical perspective, it will still bring some confusion and misleading for the model users. In contrast, the BSA resolves the problems by scoring all the possible structures, so that the structure presented by BSA conforms to the common knowledge, that the interactions defined in the BN are purely driven by data.
2) Comparing to TAN, the superior of target free learning process is observed for BAS. The TAN assumes that all the nodes in the BN have direct interactions on the target node, links them to the target node compulsorily and ignores if they have interactions in reality. For instance, 10 nodes are linked to the target node of SRP in the learning BN but some of the links are irrational. On the other side, huge task would be placed on conditional probability calculation and data acquisition, as the size of the relevant CPT table would have been enormous if all root variables are defined as the parent nodes of the target node. To solve this issue, previous studies (i.e., Yang et al., 2018) introduced the uses of intermediate level risk variables, which are based on the principle of divorcing approach to divide the network into several layers to reduce the CPT calculation work. In contrast, the BSA based BN could automatically define the network structure and determines the links among nodes by removing the restriction of setting target nodes in the learning process, which will alleviate the workload of CPT calculation to a certain extent and explores the real interactions that purely data driven.

In conclusion, the BN developed in this study is accepted in the face validity and is able to provide reliable simulation on the ship inspections.

# 4.4.2 Content validity 

The content validity aims to discuss the findings of the BN is consistent with reality. For instance, the importance of the selected factor should meet the human sense or common agreements and the most important factor should be identified to guide further risk mitigations. Thereby, an entropy-based sensitivity analysis approach (i.e., mutual information analysis) is applied to prioritise the factors. Here we define that a high entropy factor is more informative than other low entropy factors. The mutual information entropies for each node are calculated with aids of the GeNIe program and

are shown in Table . The node of SRP is selected as the target to compare the relative importance between the target node and others.

Table 5: Mutual information analysis


The target node of SRP obtains a value of 0.115 . Using its entropy value as the benchmark, top three important variables are ranked according to their relative importance values from high and low as company performance ( $437.83 \%$ ), ship flag ( $396.52 \%$ ) and recognised organisation ( $396.52 \%$ ). The company performance is defined as the most important variable that affects the SRP as it obtains an entropy value of 0.492 with the relative importance of $427.83 \%$. However, three variables of the duration of detention, the place of inspection and the total detention in the past 36 months show no interactions to the SRP, which evident that the inspection criteria and punishments are basically the same and fair in all the Paris MoU member countries. On such a basis, the content validity validates the BN is rational and logical.

# 4.4.3 Model verification \& the uncertainty analysis 

The purpose of model verification process is to test the uncertainty of our model. For BN model, uncertainty normally consists of two parts: one is epistemic uncertainty, representing the uncertainty in the model structure construction and parameter determination, the other is aleatoric uncertainty, which comes from the obtained data. The first type of uncertainty could be eliminated by inputting a large quantity of data, stimulating us to enlarging our database in this research; while the second type of uncertainty could not be eliminated because it is accompanied with the data (Bhattacharyya et al., 2017). Therefore, to test the uncertainty of our model, verification process focuses on two aspects: one is the performance test, the other is the consistency

test (Yang et al., 2021). The results of performance and the consistency tests indicate the uncertainty of our model is controlled in a rational level as our model is reliable for real practice.

# 1) Performance test 

To verify the proposed model, 185 new detention cases in the Paris MoU region from April 2020 to June 2021 are collected on the official website. Relevant information of the 185 new entries is used individually to test the proposed model, the state of SRP with the highest probability is used as the result delivered by the proposed model. The following table reveals the accuracy rate of our model in determining the SRP of different detained vessels by comparing the model results with the ones in real reports.

Table 6. Model Performance


To explain Table 6, an example of 'LRS' is used. Among 185 new entries, 40 vessels are LRS. When incorporating the information of each detention into the proposed model, 39 suggests LRS, while 1 receive an SRS evaluation. Therefore, the accuracy rate for 'LRS' is calculated as $97.5 \%(39 / 40)$. The same goes to 'SRS' and 'HRS'. From Table 6 , the accuracy rates of 'LRS', 'SRS' and 'HRS' is $97.5 \%, 96.7 \%$ and $98.2 \%$ respectively, indicating the model is reliable in terms of providing accurate and consistent forecasting results. Additionally, its overall accuracy rate is $97.3 \%$ $(39+87+54 / 185)$.
2) Consistency test

In this research, the consequence severity levels are unbalanced with the majority being slight injuries. In this case, using the percent calculation along for the model accuracy prediction and validation are arguably insufficient. Kappa statistic, as an alternative statistical approach, is used to test the model consistency. Since there are two raters in this research (model results and real results), Cohen's kappa coefficient is selected for the model validation.

The calculation process is shown as follows:

$$
\begin{gathered}
p_{e}=\frac{55 \times 55+89 \times 90+41 \times 40}{185 \times 185}=0.3703, \quad p_{0}=0.9531 \\
\boldsymbol{k}=\frac{0.9531-0.3703}{1-0.3703}=0.9255
\end{gathered}
$$

The Cohen's kappa ( $\boldsymbol{k}$ ) is 0.9255 . Based on the guidelines from Altman (1999), a kappa $(\boldsymbol{k})$ of 0.9255 represents a strong strength of agreement, which means the model is strongly consistent with the real accident consequences.

# 4.4.4 Comparison analysis 

The constructed model is validated through a comparison of risk evaluations. The comparison contains implemental test and a consistency validation.

In the test, the ship risk results are calculated by using the proposed model and the SRP system respectively. As the SRP system gives a score to describe the risk, the outputs from the trained BN need to be converted to a numerical value for better comparison. Thus, a utility function is applied to prioritise the detention risk, in which the utility values are assigned to risk variables and the crisp values are then calculated. The utility function is given below:

$$
C R=\sum_{i=1}^{n} P_{i} U_{i}
$$

Where the $C R$ is the crisp value of the ship detention risk, $n$ is the number of the states that a node contains. $P_{i}$ stands the marginal probability for the $i$ th state and $U_{i}$ is the synthesised utility value assigned to the $i$ th state. The score used in the SRP system are assigned to each node in the BN, the details are shown in Table .

Table 7 Utility value assignments



1 When the utility value is assigned to each state of all the nodes, the model is ready to evaluate ship risk. Assuming that an oil tanker planning to call at the Liverpool Port (UK) is waiting for an inspection. Before the ship approaching the port waters, the ship could take a self-check via the SRP system. The ship is a tanker flagged by a country with black (medium risk), keeled in 2001 and managed by a ship company with low performance. It has 4 detention record in the past 36 months.

The above information is converted to a set of states to describe the ship condition according to the variable state assigned in this study, it is \{ship type=tanker, age=between 10 and 20, recognised organisation=low performance, ship flag=medium risk, company performance=low, total detention in past 36 months=more than three times $\}$.

The ship's details are first assessed by using the SRP calculator provided by Paris MoU on Port State Control web site, (available at: https://portal.emsa.europa.eu/widget/web/thetis/ship-risk-profile-calc/-/ShipRiskProfile_WAR_portletpublic). The result is shown in Figure 2:


Figure 2 the evaluation results from the SRP calculator

As a result, the SRP calculator suggests that the ship is an HRS, which has a total weighting point of 7 . Meanwhile, the ship information is inputted to the developed BN model, and the results are given and shown in Figure 3.
![img-1.jpeg](img-1.jpeg)

Figure 3 the evaluation results from the BN
Figure 3 shows that the BN gives an SRP value of 7.39 to the investigated ship, which shows a great consistency with the results from SRP inspection system. Moreover, the proposed BN model is able to provide more rich information. For example, based on the previous ship detention records, the BN predicts that the ship's gross tonnage is more likely to locate in the interval between 3000 GT and 20000 GT with a probability of $55 \%$. There is a $36 \%$ probability of the ship being detained under PSC inspection due to the document and facility issues, and the probabilities for safety issues and pollution issues are $21 \%$ and $14 \%$, respectively. Moreover, the BN predicts that the ship has a $32 \%$ probability being detained by PSCOs between 3 and 6 days. It shows the BN is more informative than the traditional SRP system.

# 5. Results and discussion 

### 5.1 Analysis on defective item code

Normally, the ship owners are required to rectify the deficiencies within a certain period, i.e., rectified at the inspection, rectified within 14 days, rectified before departure. However, sometimes the results of the inspection assessments are negative, and the deficiencies found in a ship are sufficiently serious, the ship will be strongly considered for detention. For example, the detainable deficiencies list produced by Paris

MoU grouped under relevant Conventions and/or Codes. Therefore, to better understand the inspection detention and SRP, the analysis on deficiencies is indispensable.

# 5.1.1 Overall description 

Based on the model results presented in Figure 1, several conclusions are made and research implications are derived.

1) Document and facilities deficiencies have the highest probability (35\%) leading to detention than other defective items, requiring ship owners and port authorities to pay additional attention on them. Specifically, this type of deficiency code mainly consists of the certificates and documentations of ship certificates, crew certificates and documents.
2) Safety issues are another big deficiency threatening the vessel quality and inspection passing rate, which occupies $22 \%$ of the total number within Paris MoU region. Some notable defective items are safety of navigation and life-saving appliances.
3) The probabilities of environmental items and pollution items causing vessel detention are both $14 \%$, lower than environmental and safety items, but higher than operation defective items ( $6 \%$ ) and other deficiencies ( $8 \%$ ).

### 5.1.2 Detailed analysis of defective item code-Relationship between defective item code and duration of detention

If a ship is considered to be unsafe to continue the voyage and detained by a PSCO, it will be forced to stay in the port for a certain period until meeting all the requirements. According to their severities, different defective items may lead to different duration of detention. Understanding the relationship between the defective items and duration of detention could provide useful insights for port authorities to guide them on improving the inspection system through putting emphasis on those defective items contributing to long duration of detention.

1) Crew and environment-related defective items

The following figure illustrates the scenario when all the inspected deficiencies are crew and environmental items.

![img-2.jpeg](img-2.jpeg)

Figure 4 analysis of crew and environmental defective items
Under most of the cases ( $52 \%$ ), the vessels with crew and environmental deficiencies are detained less than 3 days, and $27 \%$ of the vessels are detained between 3 to 6 days. In other words, around $80 \%$ of the vessels with crew and environmental deficiencies are detained less than 6 days, indicating the punishment on this type of deficiencies is relatively low. This is mainly because the sub items under this category (such as the certificates of crew, training on crew, and some working condition on board), are usually easy to be rectified and hence do not need too much time.
2) Document and facilities

When it comes to the document and facilities, the result is presented as follows.

In Figure 5, the probability distribution of detention duration is similar with the general situation. $25 \%$ cases are detained less than 3 days, $35 \%$ cases are detained between 3 to 6 days, $19 \%$ cases are detained between 6 to 9 days, $14 \%$ cases are detained between 10 to 12 days, and $7 \%$ cases are detained for more than 20 days. The similarity of document and facilities category shows its representativeness in PSC inspection, which is also proved by the fact that it has the most detention cases in the detention database. Normal punishment intensity is posed on this type of deficiencies.

![img-3.jpeg](img-3.jpeg)

Figure 5 analysis of document and facility defective items
3) Operation

Operational deficiency refers to those defective items related to vessel operations, i.e., machinery operations, emergency operations, radio communication operations, cargo operations including equipment, and navigational operations. Operational actions are closely connected with shipping safety, as an ignorance or substandard operation system/equipment could lead to catastrophic consequences. The following figure displays the result when defective items are all from operational issues.
![img-4.jpeg](img-4.jpeg)

Figure 6 analysis of operation defective items

It could be concluded from Figure 6 that a quite harsh punishment intensity is implemented on vessels with operational deficiencies. $12 \%$ vessels are required to stay at the port for more than 20 days, and $23 \%$ vessels are detained between 10 to 20 days; $30 \%$ vessels are asked to rectify their vessel in 6 to 9 days, and the same number goes to the vessels of 3 to 6 days detention duration, while only $4 \%$ vessels can be released within 3 days. All these signs indicate that although operational issue is not the deficiency with a high frequency, its potential consequence is serious, hence strict control measures are taken on it, reflected by the duration of detention.
4) Pollution

In recent years, pollution is gradually becoming one of the major topics that Paris MoU focused when regulating policies and rules. In 2018, the Paris MoU Committee recognized the importance of the IMO requirements for stricter limits on air pollution from ships and this has led to the decision to have a Concentrated Inspection Campaign on MARPOL Annex VI. This decision demonstrated the importance to the Paris MoU of environmental awareness and compliance, especially regarding prevention of air pollution from ships (Paris MoU).
![img-5.jpeg](img-5.jpeg)

Figure 7 analysis on pollution issues
From Figure 7, the severity of pollution deficiencies is further clarified. $10 \%$ vessels in this scenario are detained for more than 20 days, $13 \%$ vessels are detained for 10 to 20 days, while $28 \%$ vessels are asked to stay for 6 to 9 days, $37 \%$ vessels stay at the port between 3 to 6 days, and $12 \%$ vessels are permitted to leave the port less than 3 days.

The results reveal that more vessels are required to detain for a longer period than normal situation, indicating that a relatively higher level of punishment has been placed on this type of deficiency.
5) Safety issues

Vessel safety is always of primary importance of the Paris MoU. It consists of many different aspects, for example, fire safety, structural safety, navigation safety, and occupational safety. In recent years, Paris MoU has implemented many actions with regard of this area, i.e., 2017 CIC - safety of navigation, 2012 CIC - fire safety systems and 2011 CIC - structural safety and load lines. The following figure presents the results of model result of this deficiency type.
![img-6.jpeg](img-6.jpeg)

Figure 8 analysis on safety issues
In general, the situation under this situation is quite promising, with most of the vessels being detained less than 6 days ( $40 \%$ less than 3 days, and $34 \%$ between 3 to 6 days). Only $5 \%$ of the vessels are forced to stay at the port for more than 20 days. Compared with the normal situation, a slighter punishment intensity is posed on the detained vessel, probably because the propaganda on vessel safety in recent years is effective and thus the overall safety condition of vessels is improved to a relatively high level. In other words, most defective items are slight and easy to rectify.
6) Others

There are other deficiency types that also could lead to detention. Some typical

examples include emergency system issues, radio communication issues, alarms issues, dangerous goods issues, employment issues, and ISM issues. Although these deficiencies are not major ones causing detention, their occurrence should not be ignored and may lead to more severe consequences affecting maritime safety.
![img-7.jpeg](img-7.jpeg)

Figure 9 other issues
From Figure 9, it is found that the strictest control measure is applied on this category. The vessels with a detention period for more than 20 days occupies $28 \%$ of the total database, while only $5 \%$ vessels are detained for less than 3 days. Additionally, $28 \%$ vessels are detained between 6 to 9 days, $23 \%$ vessels are required to stay at the port between 3 to 6 days, and $16 \%$ vessels have a detention duration of 3 to 6 days.

To further clarify the influence of different deficiencies on duration of detention, a comprehensive analysis is conducted. In accordance with the BN model, we assign different utility values on different states of duration of detention. Specifically, 'less than 3 days $=1$ ', 'between 3 to 6 days $=2$ ', 'between 6 to 9 days $=3$ ', 'between 10 to 20 days $=4$ ', 'more than 20 days $=5$ '. For different deficiency types, the expected utilities are calculated based on the assigned values and the resulted probability distribution. The following table shows the utility value of detention duration under different scenarios.

Table 8 Utility value of different deficiency types


It is easy to rank the deficiencies according to the obtained expected utility value, which represents the punishment intensity of port authorities.

Others $>$ Operation $>$ Pollution $>$ Document $\&$ facilities $>$ Safety issues $>$ Crew $\&$ environment

In addition, the above value could be viewed as the consequence of each deficiency type. To obtain a comprehensive comparison on their risk level, a further calculation is needed. Since risk = probability * consequence, the risk level of deficiency type could be obtained based on the expected utility value (consequence) and the probability distribution (probability).

Table 9 Expected utility value of different deficiency types


It could be concluded from Table 6 that the risk level of different deficiency types is ranked as follows:

# Document \& facilities $>$ Safety issues $>$ Pollution $>$ Others $>$ Crew $\&$ environment $>$ Operation 

### 5.2 Analysis on company performance

As a newly added factor in the PSC inspection system, company performance plays an important role when calculating the SRP of vessels (Yang et al., 2020). Things have changed since the implementation of the company performance. Ship owners need to choose their shipping management companies more carefully, while shipping management companies are no longer insignificant stakeholders and begin to select vessels with care. Actually, company performance is viewed as one of the most significant improvements and changes of the inspection system stated by many PSCOs and members of the Paris MoU (Paris MoU annual report). It not only represents the

performance of ISM companies, but also reveals the impact of human factor on inspection results to a certain degree. The performance level of shipping management company is dynamic, which is determined by the choice of the administrator of the company. If the administrator tends to stimulate the ship owners to reinforce the maintenance level of the vessel, it will implement strict regulations on vessel selection; otherwise, it will not put too much effort on it, leading to the vessel a higher chance of being caught in the inspection. In other words, the company performance is acting as one of the most important human factors in the PSC inspections. Therefore, in this section, the relationship between company performance and other factors is further clarified to better understand the influence of company performance. The state of company performance will be adjusted to see the possible changes it brings to other variables.

The following figures presents the variations in the probability distribution of some important variables when company performance is presented at different states, including ship flag, vessel age, recognized organization and total detention.
![img-8.jpeg](img-8.jpeg)

Figure 10 Probability distribution of ship flag under different cases

![img-9.jpeg](img-9.jpeg)

Figure 11 Probability distribution of vessel age under different cases
![img-10.jpeg](img-10.jpeg)

Figure 12 Probability distribution of recognised organisation under different cases

![img-11.jpeg](img-11.jpeg)

Figure 13 Probability distribution of total detention under different cases
From Figure 10 to 13, several findings related to the company performance are highlighted.

1) The trends of these variables are similar. Specifically, when the company performance is becoming worse, the probability distribution will be inclined to variable states with low/poor performance. For example, when the company performance is changed from high to very low, the probability of 'vessel age $>30$ years' increases from $37 \%$ to $52 \%$; for ship flag in high risk, the number grows from $7 \%$ to $22 \%$. The same also goes to other variables. On the other hand, when the company performance is becoming better, the probability distribution squints towards variable states with better performance.
2) The change rates of the worse state of variables are huge along with the change of company performance, which means company performance should be paid more attention by port authorities. For example, when company performance is changing from high to very low, the probability of 'ship flag with very high risk' increases by $1600 \%$, while the probability of 'recognized organization with very low performance' increases by $175 \%$. Moreover, 'total detention with three or more than three times' grows rapidly with a $200 \%$ speed, and 'vessel age with more than 30 years old' rises by $73.3 \%$. All these numbers indicate the severe consequence if the management companies do not meet the requirements of the Paris MoU, thus demonstrating the necessity of adding company performance in the PSC inspection

3) The involvement of shipping management company is an effective way to stimulate ship owners to ensure vessel quality. Before the implementation of NIR, shipping companies are just third-party managers who, for a negotiated fee and with no shareholding ties with their clients, undertake the responsibility of managing vessels in which they have no financial stake (Mitroussi, 2003). However, the random selection of ship owners, the poor operation and management of shipping companies led to vessel quality concerns, which can be reflected by the comparison between good company performance and bad company performance from Figure 10 to 13. The introduction of shipping companies in PSC inspection system on one hand forces ship owners to choose the shipping companies of high-performance level to avoid potential punishment, while it on the other hand stimulates ship owners to improve their vessel quality with the help of shipping companies as shipping companies do not want to accept sub-standard vessels now.
4) It is found that our model suggests that there is lack of sensitivity between company performance and deficiency codes. Actually, it is because company performance is determined by not only deficiency codes, but also detention history, as stated by the $43^{\text {rd }}$ Amendment of Paris MoU on Port state control. Meanwhile, the deficiency code is classified into ISM codes and other codes when calculating company performance, although ISM codes have higher points than other deficiency codes when calculating deficiency index, it is not the decisive item because of their relatively low occurrence, thus the relationship between company performance and deficiency codes is not obvious.

# 5.3 Analysis on ship risk profiles 

The previous inspection records demonstrate that most of the high-risk ships have some commonalities on variables. Here, the proposed model is used to investigate these commonalities of variables for high-risk ships. When setting the node of 'SRP' as $100 \%$ of HRS, the results are simulated and presented in Figure 14.

![img-12.jpeg](img-12.jpeg)

Figure 14 the model simulation for the high-risk ships
Figure 14 reveals that if a vessel is identified as an HRS, there is a $48 \%$ probability that it belongs to a general cargo ship, and the probability that the HRS is more than 30 years old is $54 \%$. Approximate $57 \%$ of ships are recognised in an organisation of medium or low performance. One out of three ships are flagged in the countries that categorised as the white flag and those from black flag countries account for more than $60 \%$ of the HRSs. Moreover, $92 \%$ of the HRSs are charted or owned by shipping companies that have been evaluated as low or very low performance, and $43 \%$ of them have been detained more than twice in the past 36 months. Common detention reasons for HRSs include documents and facilities, safety issues, pollution and crew and environment. If an HRS was detained under PSC inspections, the detention period for these ships is much longer than other ships, as $73 \%$ of them will be detained for more than 3 days. These HRSs are relatively more common in ports of Russia, Greece and Italy, where more attention needs to be paid by local PSCOs.

# 6. Conclusion 

This study uses a new data training approach and new PSC records from 2017-2020 to analyse the changed pattern of the risk factors influencing PSC inspections and the relationships among them. The database consists of 1880 ship detention records collected from the Paris MoU regime between 2017 and 2020, thus ensuring the quality of the constructed BN model and the study outcomes. An unsupervised Bayesian-based machine learning method is applied to develop a purely data-driven BN from the collected data, and the developed BN is tested by comparing the evaluation results

obtained from both the original method (i.e., the SRP calculator) and the proposed model. The results are consistent to a large extent. However, the new model in this paper provides much more detailed information: 1) the risk level of different deficiency types is revealed as follows: Document \& facilities $>$ Safety issues $>$ Pollution $>$ Others $>$ Crew \& environment > Operation; 2) the relationships between company performance and other factors is clarified, such as the probability distribution will be inclined to variable states with low/poor performance when the company performance is becoming worse; company performance should be paid more attention by port authorities; The involvement of shipping management company is an effective way to stimulate ship owners to ensure vessel quality. Other findings such as the most possible deficiencies that cause detention, and the duration of the ships being detained, showing its superiorities of the proposed model with respect to the performance of PSC inspections.

The findings also reveal the interrelationships among major factors influencing ship detention, which on one hand, could improve the regulations and rules in PSC inspection system and support PSCOs to optimize the ship checklist and conduct more efficient ship inspection, and on the other hand, could provide useful aids to ship owners to reduce the ship detention risk through targeted self-check of ships.

Due to the inherent advantages of BNs, the network can be updated automatically when more ship dentition records are incorporated into the database in the future to further improve the accuracy of the evaluation results. Besides, we believe that if some original PSC inspection records (in addition to the detained ship records) can be collected and combined, more useful insights may be generated for PSCOs in terms of the performance improvement of PSC inspection.

# Acknowledgement 

This research is supported by the National Science Foundation of China (52031009; 51909202), the National Key R\&D Program of China (2020YFE0201200), and partially supported by the European Union's Horizon 2020 Research and Innovation Programme RISE under grant agreement no. 823759 (REMESH).
