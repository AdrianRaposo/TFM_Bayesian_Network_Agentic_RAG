# An investigation of critical factors in medical device development through Bayesian networks 

Lourdes A. Medina, Marija Jankovic, Gül E. Okudan Kremer, Bernard Yannou

## To cite this version:

Lourdes A. Medina, Marija Jankovic, Gül E. Okudan Kremer, Bernard Yannou. An investigation of critical factors in medical device development through Bayesian networks. Expert Systems with Applications, 2013, 40 (17), pp.7034-7045. 10.1016/j.eswa.2013.06.014 . hal-01216809

## HAL Id: hal-01216809 <br> https://hal.science/hal-01216809v1

Submitted on 17 Oct 2015

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# An Investigation of Critical Factors in Medical Device Development through Bayesian Networks 

Medina, L. A., Jankovic, M., Okudan Kremer, G. and Yannou, B.

## Abstract

In this paper, we investigate the impact of product, company context and regulatory environment factors for their potential impact on medical device development (MDD). The presented work investigates the impact of these factors on the Food and Drug Administration's (FDA) decision time for submissions that request clearance, or approval to launch a medical device in the market. Our overall goal is to identify critical factors using historical data and rigorous techniques so that an expert system can be built to guide product developers to improve the efficiency of the MDD process, and thereby reduce associated costs. We employ a Bayesian network (BN) approach, a well-known machine learning method, to examine what the critical factors in the MDD context are. This analysis is performed using the data from 2400 FDA approved orthopedic devices that represent products from 474 different companies. Presented inferences are to be used as the backbone of an expert system specific to MDD.

## 1 Introduction

Although advances in technology has provided many indispensable medical products to improve human health and sustain it, the development cost of medical devices burdens the healthcare systems as the industry is more technology-centric than ever before. Accordingly, the identification of critical success factors for medical device development (MDD) has become increasingly important. These critical factors should be identified so that device development can be managed to minimize the adverse effects of these factors.

Many factors are related to the likelihood of success of devices in the market; and based on a company's ability to react to them, these factors are considered to be either internal or external (Medina et al., 2012). Internal factors mostly focus on the

organizational context within which design is executed, and among others these factors include organization's composition in terms of the level of experience in design teams (Lucke et al., 2008) and effective communication of the development priorities (Brown et al., 2008). Likewise, several publications (Brown et al., 2008; Rochford and Rudelius, 1997; Millson and Wilemon, 1998) report that the execution of a complete development process that includes preliminary market analyses, financial analyses, and customer involvement is critical for the further commercial success of medical devices.

On the other hand, external factors are mostly related to costs and profits, research and development (R\&D), clinical research and insurance companies' reimbursement (Advanced Medical Technology Association 2003). Intellectual property protections and overseas market opportunities are also among these external factors. More importantly, the Food and Drug Administration (FDA), regulatory agency of medical devices marketed in the Unites States, has been suggested as the primary external factor influencing the development priorities (Advanced Medical Technology Association 2003).

Success factors in product development have been examined in various ways thus far. However, existing methods used for the identification of critical success factors have a number of shortcomings; among these are the subjectivity of survey-based studies and the complexity to comprehensively and rigorously address both internal and external factors (Medina et al., 2012). This paper discusses these shortcomings and proposes to overcome them with the application of a Bayesian network (BN) approach to examine the impact of product characteristics, company context and regulatory environment related factors on MDD.

BN is a well-known method used for machine learning. Furthermore, it has been cited in the literature as a preferred method to address the limitations of other analysis methodologies (e.g., Venter and Van Waveren, 2007; Kim and Park, 2008). The BN approach allows for a scientifically objective analysis with the ability to simultaneously consider quantitative and qualitative data (Chiang and Che 2010; Venter and Van Waveren 2007).

In the paper, we use the BN approach to investigate the critical factors of MDD. BN analysis is performed using data from 2400 FDA approved orthopedic devices. In the remaining sections of the paper, we first provide a summary of the reviewed literature to identify potential factors with implications on MDD; then, we introduce the methodology. Details about the data set and results follow before we provide conclusions.

# 2 Literature Review 

The design, development and manufacture of medical devices is challenged with the requirements from regulatory agencies, such as FDA. This fact is considered to set MDD apart from generic new product development (NPD). However, investigations of critical factors for MDD have been similar to those of generic products for which survey-based studies were conducted to separately examine internal and external factors (e.g., Ernst, 2002; Brown et al., 2008; Rochford and Rudelius, 1997; Millson and Wilemon, 1998; Advanced Medical Technology Association, 2003). An exception to the predominant choice of using surveys is Lucke et al.'s (2008) work, which followed multiple years of device developments in order to show the relevance of the development team's

experience as an internal factor with implications for development time, a performance measure.

In order to address the shortcomings of survey-based studies and the time constraints of following the complete development process, prior research efforts employed statistical methods (e.g., ANCOVA) to explain important factors in relation to FDA's decision time (Medina et al., 2012). However, this analysis did not allow for a holistic study of quantitative variables that were related given that variables with strong correlations should not be included together in the ANCOVA analysis. Accordingly, in this paper BN approach is selected for a more robust analysis, where both internal and external factors are considered.

BN was applied in the area of new product development (NPD) as a technique for decision-making support. For example, in response to the shortcomings outlined above and others, BN has been used to develop a decision framework that can (1) manage quantitative and qualitative data simultaneously, (2) provide input for the several stages of the development process, and (3) integrate multiple aspects in one visual model (Venter and Van Waveren, 2007). Accordingly, a decision support model was built to incorporate expert knowledge and perform what if analyses that would support decision makers taking actions within an NPD process.

The NPD risks and uncertainties are major concerns, for which BNs have helped to assess these risk factors (Chin et al., 2009; Chiang and Che, 2010; Cai et al., 2011). Some of the considered risk items include the time-to-market, manufacturability, maintainability and expected revenue of new products (Chiang and Che, 2010). The consideration of risks is a major issue for MDD, where the design of risk mitigation

strategies is used to reduce the medical use error. This includes the development of the Bayesian risk identification model (BRIM) to manage and mitigate the risks related to human response failures that could come from a combination of interface, environment, or contextual influences (Rieger and Rahimi, 2011). BRIM defines performanceinfluencing conditions as the root causes that relate to the probability of human response failures. The result focusing on product interface design is a user error likelihood that can be used to assess product performance in terms of human interaction. While BRIM impacts the design stage of MDD, other efforts have been focused on the assessment of risk for devices already released to the market. At this stage, issues in the manufacturing process or supply chain have been addressed proactively with a BN based approach for the Health Hazard Analysis (HHA) (Jiang et al., 2011). The results from this analysis are used by industry to perform corrective actions in the field, in addition to being considered by FDA for the classification of device recalls.

A different use of BN in medical device applications include the costeffectiveness analyses of MDD. This analysis has been improved with a BN based approach of iterative economic evaluations of new medical device technologies throughout their development process (Vallejo-Torres et al., 2008). These included the implementation of simple analyses at early stages that will become more robust by incorporating more evidence as the development process moves forward (Vallejo-Torres et al., 2008).

In general, the reviewed studies have shown successful implementations of BN, establishing BN to be a robust technique. At the same time, as summarized, there are studies that investigated the critical factors in MDD; although they are either not

comprehensive (i.e., omitted consideration of external and internal factors simultaneously), or the nature of the survey methods and analytical techniques implemented limit the ability to generalize. Accordingly, as our first step on route to developing an expert system to aid medical device developers, we have devised the following methodology to investigate the critical factors relevant to the MDD context.

# 3 Data and Variables 

Data availability was dependent on the number of approved orthopedic devices in the FDA's public database to date. As a consequence, the raw data did not have an equal number of samples per category, i.e. product codes ${ }^{1}$. From the complete data set of 9013 orthopedic devices (from 166 product codes), some product codes only had one data point while others had hundreds of data points. Only a subset (24) of these product codes was found to consistently have more than 100 data points for each code. In order to account for equal representation and hence to limit undue bias, we have randomly selected 100 devices per product code and included them along with their full FDA dataset. As a result, 2400 FDA approved orthopedic devices were randomly selected to study the critical factors of MDD.

Table 1 summarizes the variables under study with a description of their meaning. Note that the information contained in the table was a deduction of our review of the literature (presented in Medina et al., 2011; Medina et al., 2012; Medina et al., 2013) as well as an evaluation of the FDA data and how the available data could be used to represent factors cited in the literature. As can be observed in the table, for each variable we have listed if they are internal- or external-variable, and quantitative- or qualitative-

[^0]
[^0]:    ${ }^{1}$ Product codes are FDA classifications used to group medical devices with the same characteristics and requirements.

variable; we have also associated each variable either to the product, to the company or the regulatory environment (FDA). This association assignment process was done in an ad hoc manner. The variables were classified to be internal or external depending on the applicant's ability to influence such a factor. For instance, variables related to the regulatory environment (e.g., FDA's decision time and classifications) are not under the control of the applicant company. At the same time, product specific characteristics (e.g., context of use, body part, function) are under the control of the applicant company given their absolute power on the products they decide to develop and manufacture. The variables were also classified given their direct association to the product, company or regulatory environment (FDA). The variables associated to the regulatory environment include different types of classifications, such as submission type, regulation number, but also evaluate the level of experience of FDA with historical reference. There are two submission types, pre-market notification (510(k)) and pre-market approval (PMA). Both submission types differ in their requirements, having most medical devices cleared with 510(k)s given that this is a simpler and faster pathway.

The historical reference is used to measure the level of experience in multiple aspects by quantifying the number of devices previously approved with the particular characteristic. Most of the historical reference variables are related to FDA's experience with the particular product code, body part, function or material. The company experience is also considered, with the company's historical reference measuring the number of devices previously cleared/approved for the same company. Other variables associated to the company include the name of the applicant and the year of submission.

The year of submission is an important variable to consider the changes in the regulations throughout the years that might have an impact on different factors.

Finally, variables associated to the product are several, ranging from different types of classifications, e.g., product code and risk classification, to product specific characteristics. Some of the product specific characteristics include the material, intended use, context of use and body part, among others. Regulation numbers (associated to regulatory environment) and product codes (associated to the product) are used to group medical devices in generic classifications of devices with the same characteristics and therefore the same requirements. Product codes provide a more detailed classification of homogeneous devices; whereas a regulation number could have multiple product codes, the vice versa is not allowed. This allows two devices with the same regulation number but different product codes to have different requirements. For instance, all the devices with the same product code will share the same risk classification. The risk classification consists of three levels (I, II and III), where devices in the highest level represent the higher risk. Other product characteristics are related to the device specific use, which may include the intended use that defines the clinical problem to be solved and the context of use, which defines whether the device is used in the operating room or doctor's office.

The performance measure (dependent variable) in the analyses is the FDA decision time. This value results from the calculation of the elapsed time between the company's submission date and FDA's decision date. FDA's decision time is important given its impact on the time-to-market for new medical devices.

Table 1. Description of Variables (Where a number is present in parentheses, it refers to the levels of the variable, or the number of different categories considered for the variable)


# 4 Methodology 

### 4.1 Bayesian network and algorithm selection

A Bayesian network (BN) gives a graphical representation of probabilistic causal interactions between a set of variables (Kjaerulff and Madsen, 2008). The nodes in this network represent the variables that are observed, where vertices or direct links represent interactions. The existence of vertices implies conditional dependence between two given variables. In general, a BN network can be seen as a graphical visualization of a set of "fuzzy" cause-effect rules that support different types of reasoning and predictive modeling.

BNs are represented using directed acyclic graphs (DAGs) (Jensen and Nielsen, 2007), where the network is defined through a couple $B N=(S, P)$ :

- $S=(N, A)$ represents the structure (i.e., the graph);
- " $N$ " is a set of nodes. Each variable is represented as a set of mutually exclusive states;
- " $A$ " is a set of edges representing the causal interaction between variables. The link from node N1 to N2 is read (defined) as "N1 is a parent of N2", and represents the fact that if we know the information on N1 then we can deduce the knowledge on N2.
- $P$ represents a set of conditional probability distributions that define the probabilistic dependency between a node and its parents. Conditional Probability tables associated with each state of the variables are calculated, and provided for all variables using a generalization of the well-known Bayes Theorem (provided in Equation 1).

$$
P\left(\frac{A}{B}\right)=\frac{P\left(\frac{B}{A}\right) * P(A)}{P(B)}
$$

Bayesian networks can be used for building predictive models based upon learned knowledge (Heckerman, 1997) concerning a specific domain but also to discover relationships between a large set of variables. The latter case is known as a learning BN network. Two main approaches are used for Bayesian network learning: (1) Constraintbased approaches, and (2) Score-based approaches. Constraint based approaches form the network using the conditional dependence relationships found in the data (Spirtes et al., 1993). Although very reliable in network learning scenarios, constraint-based approaches have limitations in the reliability of high-dimensional conditional independence tests. Score-based approaches are based on definition of an evaluation function for candidate network quality (Heckerman et al., 1995; Friedman and Goldszmidt, 1996). These approaches are less sensitive to data quality.

In this research, we use a novel hybrid approach, Smart Greedy+ algorithm (Jouffe and Munteanu, 2000; Jouffe and Munteanu, 2001). This hybrid algorithm consists of three steps:

1. Pre-processing algorithm that collects data on the best local network configuration for each node,
2. A hybrid learning algorithm combining classical transformation operators of the score-based algorithms with a novel heuristics for arc orientation and post-processing steps based upon constraint-based approaches,
3. A post-processing algorithm to improve the final structure by conducting a restricted search in the ordered topological space.

Experimental results that compare this approach with greedy search and tabu search have shown that Smart Greedy+ outperforms these classical approaches of learning using Bayesian networks and that the precision of the network is higher in all classes (Jouffe and Munteanu, 2001). Thus, our reasons for the choice of Smart Greedy+ include the precision of the network, the avoidance of local optima in the network and the possibility of discovering causal relationships.

# 4.2 Use of Bayesian networks for relation discovering 

In this study we propose to use Bayesian network learning algorithms in order to explore data relationships. The choice of using a BN-based data mining and exploration is motivated by the advantages that BNs present when exploring different data and uncertainty modeling capabilities. First, BNs are effective in providing models for direct causal relationships, i.e., mathematical definition of probabilities and conditional independence statements can be connected to the definition of causality (Pearl and Verma, 1991; Heckerman, Meek et al., 1999; Friedman et al., 2000); thus, when relationship discovering is intended, BNs can be used to discover and represent the causal relationships. Like in our case, when the data set is relatively large and mixed data types are used (quantitative and qualitative), and in cases where data sets might be incomplete, BNs are considered to be the appropriate methodology for relationship mining (Heckerman, 1997; Chen, 2003; de Santana et al., 2007; Chang et al., 2008). It is also noteworthy that BN relationship mining affords identification of local interactions within one process, where the value of one variable directly depends upon a small number of other variables (Friedman et al., 2000). This is indeed the objective of our study, to

identify factors that directly influence FDA decision time, as well as investigating the propagation of information throughout the entire network. Finally, it is important to underline that one of the major advantages of BNs is the possibility of integrating uncertainty in the network structure modeling (Barton et al., 2008).

The research methodology followed in this study is shown in Figure 1. Utilizing actual FDA medical device development data and different factors identified in the literature, the unsupervised BN algorithm is implemented to discover relationships between different variables. Examination of various factors also required combing through the published sources in engineering and business literatures focusing on product development. In this study 19 variables are examined and integrated into 2400 data vectors (in total 45600 data points).
![img-0.jpeg](img-0.jpeg)

Figure 1. Research Methodology
After validating the network performance and precision, the capability of information propagation is used to evaluate possible changes within the network. This information

propagation can be considered as "What-if" simulations (Yannou et al., 2011; Yannou et al., 2013). We addressed scenarios related to changes in FDA decision time subject to changes in three variable categories: product, company and FDA regulation variables.

# 5 Results \& Discussion 

We have used values of 2400 FDA approved orthopedic devices across 20 variables listed in Table 1. Although hypothesized relationships can be formed by the decisionmaker for testing, we have opted for the use of unsupervised learning in order to explore the structure of the network (i.e., the relations between the given set of variables), for which the conditional joint probability computations are used. This network gives an overview of explored variables as well as their influence. The resultant network is shown in Figure 2. In the figure, red nodes indicate product associated variables, yellow nodes indicate company related variables, and green nodes show the regulatory environment related nodes.

It is important to understand the validity of the network model before drawing inferences from it; for this purpose, two different network performance parameters (Figure 3) are reviewed: (1) mean Log-likelihood function for the given network, and (2) contingency table fit defined in percentages (from $0 \%$ to $100 \%$ ) showing the predicted observation in the network in comparison to the actual data in the observed database. The higher the contingency table fit, the better the network's predictive capability is; for our case, this is $\sim 83 \%$, indicating a very high predictive capability.

![img-1.jpeg](img-1.jpeg)

Figure 2. Unsupervised Learning Using the Taboo Order Algorithm
![img-2.jpeg](img-2.jpeg)

Figure 3. Mean Log-likelihood and Contingency Table Fit

The structure of the BN network shows probabilistic inferences of the variables studied (shown in Figure 2). One of the first things that can be observed is that the FDA decision time is impacted by the type of submission that is in turn impacted by the year of decision. The different submission types, Pre-market Approval (PMA) and Pre-market Notification $(510(\mathrm{k})$ ), have different requirements making the first one the strictest (or more complex) pathway with a longer decision time. Year of decision (FDA regulatory variable) seems to be a crucial factor linking FDA decision time with product and company variables. One possible explanation to this might be that in operational policy decisions FDA takes into account contemporary market needs in the Unites States.

Another central part of this network structure (in Figure 2) is the regulation number. The FDA regulatory factor seems to be influenced by different materials used in the device, and influenced by the intended use as well as the risk classification. Device risk classification is dependent upon the type and number of materials used in the device as well as the FDA regulations represented with the regulation number. These results also underline the obvious importance of regulation number as it is connected to a large number of product variables: materials, number of descriptors, function, product ID and intended use. Supporting this, the regulation number is significant by definition as it classifies similar medical devices.

The network structure also highlights the requisite expertise of companies. The historical reference (HR) per function is a parent node of the company HR, which in turn is related to the applicant. It seems also that year of decision is a parent node of the applicant. Taken together, these confirm that companies are specialized more on product functions and that their historical records support that claim.

A further reflection of the complex medical device development environment perhaps, year of decision is a parent node of applicant; that is, companies with different expertise might be focusing on product approvals that are advertised/recommended by FDA as areas of need. While this might be seen as directing attention (as recommended by FDA to developers) to contemporary needs, it might also negatively impact the decision time for other devices in niche areas. How this fact impacts medical product innovation strategies for companies should be explored as innovation patterns might be impacted by FDA guidelines and recommendations.

Although the network shown in Figure 2 is sufficient to understand the significant relations among the variables, "What-If" simulations can enrich our understanding. Accordingly, based on the predictive capabilities of the observed BN, the distribution of the FDA decision time is varied in three cluster levels, and other product, company and regulatory environment variables are studied. We present these details in the following three sections.

# 5.1 FDA Decision Time \& Product Variables 

Studying the product variables for their potential impact on FDA decision time is important as an enhanced understanding can better prepare companies in their planning stage. Product related variables that are taken into consideration are: context of use, product function, body parts, number of descriptors, number of materials, product ID and intended use. Initial observed distributions (see Figure 4) show that in majority of the cases ( $73.88 \%$ ) the FDA decision time is less than 139.961 days. Most of the products are intended for surgery, and relate to bone ( $33.21 \%$ ), hip ( $21.13 \%$ ) and spine ( $25.71 \%$ ). Most of the approved devices are made up of three different materials, and very few

(4.1\%) combine four different materials. An interesting fact is that a large number of materials, approximately $29.17 \%$, are not specified; this means that the material was not a relevant factor for those devices.
![img-3.jpeg](img-3.jpeg)

Figure 4. Initial distributions for the Product Variables of the product sample

In order to have a deeper analysis of the potential product factors with relation to FDA decision time, we have analyzed the predictors of the decision time in three clusters, where the decision time is: (1) less than 140 (139.961 to be exact) days, (2) longer than 140 days but shorter than 355 days, and (3) longer than 355 days. We show the values for the first cluster in Figure 5. Across the clusters, the initial distributions do not vary much (only up to $1 \%$ ), indicating a modest overall impact.

![img-4.jpeg](img-4.jpeg)

Figure 5. Product Variables for the FDA Decision Time Cluster1 (Decision Time<139.961 days)

For the second cluster of the FDA decision time (139.961<Decision Time $<354.043$ days), shown in Figure 6, we observe that although the variation is still minimal, there is a noticible decrease in the function variable. The fixation is used in $55.88 \%$ of the devices whereas the similar value for the first cluster was $57.5 \%$. At the same time, an increase is detected across the first and second clusters in the prostheses from $25.34 \%$ to $27.96 \%$, respectively. The change in the body part variable is minimal where only the spinal mode decreases from $26.27 \%$ (in cluster one) to $24.19 \%$. Usage of 2 or more materials increases from $36.63 \%$ to $39.91 \%$ with the shift from cluster 1 to 2 .

![img-5.jpeg](img-5.jpeg)

Figure 6. Product Variables for FDA Decision Time Cluster 2 (139.961<Decision Time< 354.043)

When the FDA decision time is longer than $\sim 355$ days (Figure 7), there is almost no change in the distributions. Overall, it seems that product variables do not contribute much to the decrease in FDA decision time, and that there is no evidence showing that product related variables are the main reasons for the FDA decision time changes across clusters.
![img-6.jpeg](img-6.jpeg)

Figure 7. Product Variables for FDA Decision Time Cluster 3 (Decision Time>354.043 days)

These simulations might reflect the dynamics of the MDD market. For instance, the context of use is not changing; there is between $5.41 \%$ and $5.70 \%$ projects that are intended for the doctors' office. Very large percentage of the developed devices is for the surgery/operating room (from $94.30 \%$ to $94.59 \%$ ). Function is mostly impacted by fixations and prosthesis; very small percentages are related to fusion, surgical instruments and bone void fillers. Finally, in most of the cases body parts are bone, hip or spine.

# 5.2 FDA Decision Time \& Company Variables 

Company variables characterize companies partaking in the MDD market. The analysis of these variables could potentially show why some companies are more successful and their impact on global FDA decision time. At a first glance, the number of company related variables followed by the FDA is very limited. There are three variables that are taken into account in this study: (1) type of submission, (2) applicant, and (3) company HR. Initially observed distribution (Figure 8) shows that in majority of the cases, the type of submissions is either a special 510(k) or traditional 510(k). As per the FDA guidelines, the special $510(\mathrm{k})$ is an alternate method to the traditional $510(\mathrm{k})$, and is instituted in order to facilitate the review process for cases when a previously cleared device has been modified (Medina et al., 2011). Together they represent $98.45 \%$ of submissions. It seems also that companies in general have relatively significant experience levels. For example, in $67.57 \%$ of cases, companies have already submitted 72 projects, and $83.83 \%$ of the companies have previously submitted projects.

![img-7.jpeg](img-7.jpeg)

Figure 8. Association of the Company Variables with the FDA Decision Time

As was presented for the product related variables, aforementioned three cluster level observations are also reported. For the first cluster (FDA decision time <=140 days), shown in Figure 9, type of submission appears to have an impact. The special 510(k) submission type increases to $31.57 \%$ from $24.24 \%$. The traditional 510(k) submission, however, decreases from $74.21 \%$ to $67.36 \%$. Other variables do not show significant changes, which could also be observed from the BN network structure discussed earlier in the paper.
![img-8.jpeg](img-8.jpeg)

Figure 9. Company Variables for the FDA Decision Time Cluster1 (Decision Time<139.961 days)

Within cluster two, where the FDA decision time is between 139.961 and 354.043 days, (shown in Figure 10), we can observe a dramatic shift in the type of submission variable. While the special 510(k) submission represents only $4.39 \%$, the traditional 510(k) submission type constitutes $93.22 \%$ of the applications. It highlights the fact that the FDA policies afford a rapid evalution time for the special cases. In contrast with traditional 510(k) submissions, the special 510(k) does not require data about design controls, for which the compliance is achieved with a "Declaration of Conformity" as per the design control provision of FDA's Quality Systems (QS) regulation (Medina et al., 2011).
![img-9.jpeg](img-9.jpeg)

Figure 10. Company Variables for FDA Decision Time Cluster 2 (139.961<Decision Time< 354.043)

For the third cluster of the company related variables, the submission type is predominantly the original PMAs. It appears that almost all original PMAs need more than $\sim 354$ days to evaluate and arrive at a decision. There are also a large number of traditional types that is treated this way ( $95.14 \%$ ). The PMA is the strictest pathway of approval used for those devices of higher risk with the need for additional information to prove their safety and effectiveness with scientific evidence that may include non-clinical laboratory studies and clinical investigation (Medina et al., 2011). Original PMAs refer to

the first submission made for the particular device, while supplements are used to approve modifications of original submissions. Supplemental submissions were out of the scope of this work.
![img-10.jpeg](img-10.jpeg)

Figure 11. Company Variables for FDA Decision Time Cluster 3 (Decision Time $>354.043$ days)

# 5.3 FDA Decision Time \& FDA Regulation Variables 

FDA Regulation variables can potentially show accumulated know-how on FDA regulations pertinent to MDD, and how this information is incorporated into actual FDA policies; in this paper, we explore their impact on FDA decision time.

FDA Regulation variables cover the type of the submissions, year of decision, HR for materials, FDA HR for product code and other devices, regulation number and risk classification. Initial distributions (shown in Figure 12) show that majority of submissions are 510(k)s ( 99.79\%). As for the year of decision, it seems that from 1992 until 2004 the number of submissions was relatively stable ranging between $13.80 \%$ and $18.45 \%$. There is a considerable shift in 2004, however; the submissions increased to $37.14 \%$ in that year. It is also apparent that most of the submissions involved already known materials or products. HR variables show similar tendencies. However, the

majority of the devices are class II as for their risk classification predetermined by FDA (94.44\%). There are no class I devices given that most of these are exempt from having to obtain clearance/approval from FDA (Medina et al., 2011).
![img-11.jpeg](img-11.jpeg)

Figure 12. Association of the PFDA Regulation Variables with the FDA Decision Time

A closer look into the cases where the FDA decision time is $>=139.961$ days (shown in Figure 13) reveals that there are no PMA submissions, which might be the primary reason for very small changes in other variables. Overall, variations are less than $2 \%$ for different variable modalities.

We also note the means and standard deviation for the time of decision, $\mu=64.373$ and $\sigma=32.832$. The decision times within the first cluster ( $>=139.961$ days) represent a wide range of values with large variability.

![img-12.jpeg](img-12.jpeg)

Figure 13. FDA Regulation Variables for the FDA Decision Time Cluster1 (Decision Time<139.961 days)

If FDA decision time is between $\sim 140$ and $\sim 354$, there is a noticeable variation in the year of decision. We observe that more projects were in this range from 1992 until 2001, and a lesser number of projects after year 2004. This small change demonstrates an effort in FDA to reduce the decision time in recent years given the increased number of submissions.
![img-13.jpeg](img-13.jpeg)

Figure 14. FDA Regulation Variables for FDA Decision Time Cluster 2 (139.961<Decision Time< 354.043)

The differences between the distributions when FDA decision time is between 140 and 354 days and where it is larger than 354 days (see Figures 14 and 15) are very small. This lack of shift/change in distributions shows that FDA Regulation variables do not contribute considerably to the increase of FDA decision time. One point of note is that there is an increase of submissions with the Regulation No. ID that are $<=14.75$ and $<=51.083$ in comparison to the initial distributions. When we compare these distributions to the initial ones, it can be seen that for the FDA decision time $>\sim 354$ days there are less number of projects submitted in the year 2004 ( $42.83 \%$ in comparison to $51.58 \%$ ). This shift might underline the effort to reduce the FDA decision time in recent years.

The difference in number of applications concerns also the HR per function. Although the mean decision time is $(\mu) 124.292$ in the observed distribution, for the specific cluster three cases, the mean value for functional reference drops to 1706 from the overall mean of $\sim 1857$. It is possible that the projects that need more time concern new functions that FDA has less knowledge about. Companies should be aware and prepared for this situation.
![img-14.jpeg](img-14.jpeg)

Figure 15. FDA Regulation Variables for FDA Decision Time Cluster 3 (Decision Time>354.043 days)

Of course, the market potential for an innovative product can be considerable and the safety of patients is important; however, the elongated FDA evaluations of products with newer functions might discourage companies. Given the provisions of the special 510(k) submissions, companies might focus more on incremental innovations rather than drastic ones, potentially with very long FDA decision times.

# 5.4 Summary 

Unsupervised learning network structure developed using actual data underlines the importance of the FDA policies in medical device development. The dominant factor is the type of submission and the change of efforts in FDA policy that can be observed in the year of decision. The decision times for different types of submissions are consistently different as per FDA guidelines, although actual times could be longer than those specified by FDA. It also seems that recently (since 2004) there have been efforts to reduce the FDA decision time given the increase in number of submissions.

A very noteworthy fact lies in the discovery of very small relevance of product variables on the decision time. This underlines the recommendations for the companies to acquire the necessary knowledge on the FDA regulations in order to succeed in their efforts. Moreover, company variables proved to be relevant mostly based on their selection of submission types.

BN structure also demonstrates that risk classification is related to the materials used and especially the number of materials used. This link is reinforced also by the fact that regulation number is also dependent upon materials used. The network also highlights the impact of FDA policy in integrating previous knowledge, in particular the importance of different HR and the year of decision. It appears that a particular attention

by the FDA is directed to materials used, as evidenced by the fact that material used is the only product variable having causal relationship with the year of decision.

Simulations also pointed out that the FDA decision time varies with regards to the variation in HR per function. HR is an indicator of experience, which quantifies the number of devices previously approved with the same characteristic. The relevance of these variables along with the longer decision times for PMAs makes us question the likelihood of innovative products to go through the process in an efficient manner. FDA has been identified as an inhibiting factor for the discovery of medical devices (Foote, 1996); however, FDA has recently created a new regulatory pathway for innovative medical devices (FDA, 2012) to overcome this barrier.

# 6 Conclusions 

This paper presents our inference framework along with initial observations in an effort to solidify the relationships of the MDD setting in an evidence-based fashion in order to result in a useful expert system. Causal relationships identified in the network structure will be used as the significant predictors within the expert system. Although we have used only 2400 actual data points, we are able to show the legitimacy of the chosen methods in yielding useful inferences. In the subsequent expert system development, not only will the data set be enhanced but also cases from other regulatory settings will be considered.

A valid network is developed and analyzed in detail based on product, company and regulatory environment variables in relation with FDA decision time. Some of the relevant variables included the type of submission, year of decision and historical

reference. Based on these results, further research should include the application of supervised learning along with further study of other aspects of MDD.

Of importance are the potential impacts of this planned expert system with implications on innovation/technology development with a focus on MDD. The variables included, relating to product, company and regulatory setting, show the most pertinent factors with which product launch time can be reduced. Companies armed with this knowledge can preplan their knowledge and monetary capital in seeing through the projects to their completion.

This paper also extends the literature on MDD and the identification of critical factors with the implementation of a BN approach with unsupervised learning. Some of the future research directions may include investigating the importance of historical reference and innovation further, along with the interrelations between different variables.
