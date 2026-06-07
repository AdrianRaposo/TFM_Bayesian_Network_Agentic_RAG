# How artificial intelligence will transform project management in the age of digitization: a systematic literature review 

Maria Elena Nenni ${ }^{1} \cdot$ Fabio De Felice ${ }^{2} \cdot$ Cristina De Luca ${ }^{2} \cdot$ Antonio Forcina ${ }^{2}$

Received: 3 October 2023 / Accepted: 9 March 2024
(c) The Author(s) 2024


#### Abstract

Among the causes of the low success rate of the projects (around $35 \%$ of the total) is the low level of maturity of the technologies available for the management of the projects themselves. However, today many researchers, startups and innovative companies are starting to apply artificial intelligence (AI), machine learning and other advanced technologies to the field of project management. By 2030 the industry will undergo significant changes. By using the Preferred Reporting Items for Systematic Review and Meta-Analyses (PRISMA) protocol this paper explores the intersection of project risk management and AI. The study highlights how AI-driven methodologies and tools can revolutionize the way project risks are managed throughout the project lifecycle. Specifically, 215 papers have been analysed to explore how the scientific community has been moving so far on the topic. Besides, a cross-sectional investigation of the PM processes and AI categories/tools was carried out to identify any path that is prevalent, where the prevalence comes from, and for which PM process or sector it is most successful. Finally, from this study several gaps emerged that scientific research would have to fill to effectively implement AI in PM and that have been turned into opportunities for future research in the form of a research agenda.


Keywords Artificial intelligence $\cdot$ Project risk management $\cdot$ PMBOK $\cdot$ Decision making $\cdot$ Expert system

JEL Classification D2 $\cdot$ D24

## Abbreviations

AI Artificial intelligence
AHP Analytic hierarchy process
AIHP Interval analytic hierarchy process
APIs Application programming interfaces
BNCC Bayesian networks with causality constraints

[^0]
[^0]:    Extended author information available on the last page of the article


# 1 Introduction 

Project management has deep roots in history and has evolved over the centuries. The earliest forms of project management can be traced back to antiquity, with the construction of great works such as the pyramids of Egypt and the Great Wall of China. One of the key early developments in modern project management was the "Gantt Chart" method, developed by Henry L. Gantt in 1917 (Pacagnella and da Silva 2023). In the 1950s and 1960s, scholars such as Peter Drucker and Frederick Taylor helped develop theories on the organization and management of production processes (Winkler-Schwartz et al. 2019). During the Cold War, the aerospace and defense industry in the United States invested heavily in complex project management. With the advent of computers and project management software in the 1980s and 1990s, project management has become increasingly automated and sophisticated (Friedrich 2023). Today, project management has become a key discipline in a wide range of industries, from construction to information technology, healthcare to manufacturing (De Felice et al. 2022; Makarov et al. 2021; Vollmer et al. 2020). It is supported by a wide range of tools, methodologies and standards that continue to evolve to meet the ever-changing needs of modern organizations (Listikova et al. 2020; Wang and Chen 2023). In this context it is worth mentioning that pproximately $\$ 48$ trillion is invested in projects every year. However, according to the Standish Group, only $35 \%$ of projects are considered successful. The waste of resources and unrealized benefits of the remaining $65 \%$ are staggering. One of the reasons why success rates are so low is the low level of maturity of the available technologies. For project management, most organizations and project managers still use spreadsheets, slides and other applications that have not evolved much in recent decades. These tools are adequate when it comes to measuring the success of a simple project based on deliveries and deadlines met, but they are not up to par in a complex environment where projects and initiatives are constantly adapting and evolving (Weber et al. 2012). In recent years, Artificial Intelligence (AI) has begun to radically transform the way projects are planned, managed and executed (Shukla Shubhendu and Vijay 2013). Due to its numerous applications and even more so due

to its enormous benefits (Castro and New 2016), AI has been able to spread rapidly in many areas (Health, Finance, Business, etc.) and generate considerable social and economic value, as testified by the large amount of research in the scientific library (Nguyen et al. 2022; Nishimwe et al. 2022; Sangeetha et al. 2022; Xue et al. 2020; Zhao and Saeed 2022). Even the main international standardization body for project management, the Project Management Institute (PMI), supports the application of AI (PMI 2021). Observing that conventional project management tools often fall short in accurately predicting project success, Martínez and Fernández-Rodríguez (2015) conducted a study to explore alternative tools. Their research particularly emphasizes the value of artificial intelligence in managing the uncertainties and complexities inherent in project environments. The literature was also analyzed by Afzal et al. (2021) to investigate the connection between complexity and risk and to identify the main AI technologies for risk management in construction projects. Still in Fridgeirsson et al. (2021) have worked on identifying the potential areas of greater success of AI (project cost, planning and risk). Finally, many studies and research have already been conducted to explore the benefits and risks of applying AI to risk management processes (Jiang et al. 2013; Naim 2022; Žigienė et al. 2019; Nimmy et al. 2023). Despite all this abundance of literature, the research is mostly focused on the technology solutions and still sparse and confusing when considering managing project risks with digitized systems such as AI (Gejke 2018; Pande and Khamparia 2023). In this scenario, it seemed appropriate to provide a comprehensive Systematic Literature Review (SLR) to (i) investigate the state of the art of project management; (ii) how AI can support the project management; (iii) which specific aspects of project management will be innovated, and (iv) to understand which AI tools are best suited for any processes of project management and why. SLR emphasizes the most important authors, research institutes and countries where important contributions to the field have been made. It is a fundamental method used in academic and scientific research to summarize and analyze the current state of knowledge in a particular field (Kitchenham 2004). Thus, the present research aims to clarify the subject from a scientific point of view to offer a starting point for future studies that intend to concretely pursue this idea of using AI for risk management. With this purpose, this document also provides a proposal for the future research agenda with a specific focus of producing in a very near future a framework to outline the critical decision of a successful process for introducing AI in PM and to promote a rapid maturation of AI in this field.

The rest of the paper is organized as follows: Sect. 2 explains the research methodology used to conduct the literature review; Sect. 3 discusses the main findings of the research. While, in Sect. 4 an overview of future development and research agenda is given. Finally, Sect. 5 provides the main implications of research.

# 2 Research methodology 

A Systematic Literature Review (SLR) is applied to identifying, evaluating, and synthesizing existing research studies relevant to the specific research questions (Moher et al. 2009). Figure 1 shows the main phases followed to carried out the SLR.

![img-0.jpeg](img-0.jpeg)

Fig. 1 Methodology applied to the development of the Systematic Literature Review (author's elaboration)

In detail, SLR starts by identifying the research questions (Phase\#1). Then, Phase\#2 continues defining the analysis sample. The search results are selected and evaluated considering well-defined exclusion, inclusion and quality criteria. The process of screening articles up to the definition of the final analysis sample is summarized graphically by using the PRISMA Protocol (Rethlefsen et al. 2021). Next, the Phase\#3 develops a bibliometric analysis of the papers forming the sample by classifying the papers by year, country and journal of publication. Furthmeore, the Phase\#4 shows an analysis of bibliometric networks obtained using the VOSviewer software (Li et al. 2022). In this phase, firstly, objective data, as such as the PM processes addressed-as reported in the PMBOK (Faraji et al. 2022)—and the Project Management (PM) processes connected with them, AI categories and tools were extracted from papers. Besides, in order to deepen the study, a cross-analysis is performed to assess the coexistence and relationship of the PM processes, AI categories and tools. Afterward, the main results of the process are classified and analyzed. Then, the discussion follows the results, and the definition of challenges and limits.

# 2.1 Phase\#1: research question definition 

In a SLR, research questions guide the entire review process. These questions help define the scope of the review and provide a clear focus for selecting, analyzing, and synthesizing relevant studies. Well-formulated research questions ensure that the review is systematic, structured, and goal-oriented. Typically, SLRs have one or more research questions that address specific aspects of the topic under investigation. Research questions should be relevant to the research area or field being studied. Thus, it is important to it is important to remember the assumptions underlying our SRL:
(a) By their nature, projects are characterized by unpredictability, which makes them highly susceptible to risk (Trier and Treffers 2021). Risk management is therefore fundamental to the effective development and implementation of the project itself.
(b) The purpose of PM is to continuously identify, analyze and control all projectrelated uncertainty factors to minimize the probability of occurrence and the impact of risks (Cervone 2006).
(c) PM is also viewed as a systematic and proactive approach that aim to increase the probability of project success (Willumsen et al. 2019). Today, this activity is carried out by the Project Manager (PM), or Project Risk Manager (PM), sustained often by a team of experts.

This research stems from the idea of providing managers with a specific support in risk management coming from the AI and aims at promoting and backing an effective application of AI.

For this purpose and based on what pointed out, we identified a few Research Questions (RQ) that are summarized in Table 1.


# 2.2 Phase\#2: identification of the analysis sample 

### 2.2.1 Database search identification

A systematic review involves a comprehensive search of various academic databases, journals, conference proceedings, and other sources to identify all relevant studies. The databases taken into consideration for the search are the Web of Science and Scopus, currently the largest bibliographic database of scientific literature. To perform the subject-specific search, thirteen keywords, listed in the Table 2, were selected, and appropriately combined using the Boolean operators of union and intersection. Only articles in which the string was found in (1) article title, or in (2) abstract or in (3) keywords were analyzed.

The bibliometric analysis considered articles completely in English published from 1996 to 2023.

### 2.2.2 Eligibility criteria definition: exclusion ad inclusion criteria

A systematic review follows a well-defined and systematic process, including clear criteria for study selection, data extraction, and analysis. This process is designed to minimize bias and ensure transparency. Therefore, it is necessary to define inclusion and exclusion criteria to select the studies that will be included in the analysis sample. In detail, the exclusion criteria considered are:

- E1. Incomplete documents;
- E2. Documents such as books, proceedings and thesis;
- E3. Documents such as literature reviews, surveys and repots;
- E5. Duplicate documents;
- E6. Documents outside the reference time;
- E7. Documents out of scope.

Table 2 Search protocol and selection of literature (initial setting)


While the inclusion criteria are:

- I1. Papers published in English only;
- I2. Papers only;
- I3. Documents referring to AI according to a precise definition.


# 2.2.3 Quality criteria definition 

The quality and validity of each included study are assessed using predetermined criteria. This assessment helps in evaluating the reliability of the evidence. This study established three criteria:

- Q1: Papers that include risk management processes and artificial intelligence;
- Q2: Papers exploring the fields of application of artificial intelligence categories and tools;
- Q3: Papers with a significant impact factor, SCImago Journal Rank or CiteScore.


### 2.2.4 Identification of the analysis sample (PRISMA)

According to the above sections, the documents were identified and checked for eligibility and relevance to form an inclusion set using the PRISMA Protocol. The initial investigation returned a sample of $\mathbf{1 8 2 0}$ bibliographic records. However, considering the assumed selection criteria the analysis identified 666 out-of-scope documents, returning a sample of $\mathbf{5 2 4}$ eligible documents. It is worth pointing out that the selected studies were analyzed checking in each of them the effective use of AI was analyzed. This check is due to the fact that there is no single definition of AI. A few papers include basic algorithms that are, however, far from the true essence of AI. To perform this kind of check, the definition of Kaplan and Haenlein (2019) was used: Artificial intelligence is the ability of a system to correctly interpret external data, to learn from that data, and to use that learning to achieve specific goals and tasks through flexible adaptation. The final list of the analyzed documents is shown in Online Appendix A. Figure 2 summarizes the represents flow diagram for the selection of documents based on PRISMA.

### 2.3 Phase\#3: bibliometric sample analysis

### 2.3.1 Publication by years

The analysis of the trend of the number of publications per year highlights that from 2020 to 2023 there is an increase in the number of documents of documents developing researche on integration of PM with AI. The trend does not surprise us considering the evolution of digitalization in project management (as shown in Fig. 3). The trend does not surprise us considering the evolution of digitalization in project management. In addition, it is reasonably conceivable that this trend is also due to the spread of the Covid-19 pandemic that caused certainly a moment

![img-1.jpeg](img-1.jpeg)

Fig. 2 Flow diagram for the selection of documents based on PRISMA
![img-2.jpeg](img-2.jpeg)

Fig. 3 Publications per year from 1996 to 2023 (source: Scopus)

of discontinuity. Presumably, the research on this topic was experiencing a stalemate when the economic and social crisis triggered from pandemic worked as a "catalyst" factor that accelerated digital and technological change. This undoubtedly encouraged the adoption, and consequently research, of innovative technologies such as AI. The tred suggests that the next few years will be characterized by the ever-increasing publication of scientific publications on this research frontier.

# 2.3.2 Country analysis 

Figure 4 shows that research is concentrated outside Europe. The first country in terms of number of publications on the integration of AI in PM is China, which is credited with $17 \%$ ( 33 documents) of the publications. This is followed by the United Kingdom (19;10\%), Iran and the United States (15;8\%) and Taiwan $(10 ; 5 \%)$. However, these results are due to government policies implemented to foster AI research and application; especially in countries such as China and the US which are the main competitors in the global landscape for the development of AI technology. Over the past 5 years, the two countries have recorded the highest rate of adoption of this technology in government and business. They contributed $94 \%$ of global funding of new companies employing $70 \%$ of the best global researchers in this field (Kratochwill et al. 2020). In the United States, in 2019, the "American AI Initiative" presidential degree was signed, inviting federal agencies to increase funding for AI research by allowing scientists and researchers to access government data as well. More recently, the Department of Defense formulated a $\$ 2$ billion strategic plan with the aim of overcoming the limitations of current AI technologies (Wiltz 2019). In China, in 2017, 2 billion dollars was allocated for research and development and 2.1 billion for the creation of a research park dedicated to AI topics in 2018 (Kumar 2021).
![img-3.jpeg](img-3.jpeg)

Fig. 4 Publications by country (source: Scopus)

# 2.3.3 Documents by types 

The analysis of the documents by type revealed the following breakdown: articles (149; 88\%), conference papers ( $14 ; 8 \%$ ), and brief surveys ( $7 ; 4 \%$ ). The 215 articles published between 1996 and 2023 that make up the analysis sample were published in 71 journals. A total of $62 \%$ of the papers were published in 12 journals, with the remainder recording no more than two publications on the topic of interest for this study. The main journals and publication details are shown in Table 3.

Thus, it can be deduced that the research interest in this topic is diversified from the field of innovation, through management to sustainability.

### 2.3.4 Analysis of research trends

This section aims to highlight the bibliometric network to understand the magnitude of the phenomenon. Specifically, VOSviewer software was used to analyse bibliographic records from a collection of scientific literature, including keywords and citations, and to generate co-occurrence networks of significant terms. Through the same software, a keyword co-occurrence clustering view was generated. The total number of identified keywords is approximately 1315, which include both keywords provided by the authors of the articles and those assigned by Scopus. However, regarding how many times a keyword is repeated, the maximum value calculated by VOSviewer is 87 . A total of 55 keywords with a frequency of at least 5 were selected and a co-occurrence analysis was performed on them, as shown in Fig. 5.

Furthermore, the larger is the node, the higher is the frequency of that specific keyword. Accordingly, the most frequent word is "risk assessment", located in the yellow cluster, with an occurrence value of 78 . This is followed by the words "risk management" in the red cluster with occurrence 57 and "project management" with occurrence 56 belonging to the purple cluster. The thickness and proximity of the lines connecting the keywords in the visualization denotes the frequency of cooccurrence between two keywords across publications. Therefore, smaller distances between elements and thicker lines signify a strong relationship between them. It means that words that are close or connected by thick lines are more frequent, while a high distance or thin connection between two keywords indicates that they do not occur. The colour of each cluster is not random but determined by the complex score considering occurences, links and link strength. Colours range from purple (indicating a very low score) to yellow (indicating a low score), blue (indicating a medium-low score), green (indicating a medium score) and red (indicating a high score). To carry out the analysis of research trends followed below, it is importat to consider that our research focuses on the integration of AI into PM, particularly in risk management. The research also highlights an integrated approach in which AI is used for data collection and analysis in risk management, showcasing AI-powered decision support tools. Additionally, the role of AI extends to other PM processes such as Portfolio Analysis, General Framework, and Decision Support Systems (DSS), where it aids in risk identification and decision-making. The study positions techniques like AHP, Fuzzy Logic, Machine Learning, and Optimization within an AI framework, suggesting that their use in AI-driven decision support systems.



![img-4.jpeg](img-4.jpeg)

Fig. 5 Mapping of index keywords used in articles
2.3.4.1 Red cluster Table 4 lists the keywords that belong to the cluster, including the number of occurrences of these keywords and the number and strength of links they have.

The red cluster is the largest and most significant, presenting 12 keywords referring mainly to the decision-making aspect of risk management in projects. A

Table 4 Occurrence and total link strength of keywords in red cluster


new method for decision support in project risk response is introduced by Zhang et al. (2020). The method is comprised of two key steps: the creation of alternative risk response actions (RRAs) using case-based analysis, and the identification of the optimal set of RRAs through a fuzzy optimization model. In addition to these, fuzzy set theory is applied to assess risk probability, risk impact and risk similarity in the RRA selection process. For the prediction of project control, Wauters and Vanhoucke (2017) introduce the Nearest Neighbors (NN) technique. This technique is used as a predictor and compared with existing EVM/ES and AI methods. It is therefore referred to as hybridization as the prediction process requires the use of NN and an AI method. Liu et al. (2020) present a new intelligent model for project risk management during the construction of large, prefabricated building projects. The model is a hybrid of two algorithms: the Backpropagation (BP) neural networkbased feedforward multilayer deep learning algorithm and the Modified Teaching-Learning-Based-Optimization (MTLBO) algorithm. To enhance the traditional Teaching-Learning-Based Optimization (TLBO) algorithm, information entropy was incorporated to create the MTLBO algorithm, resulting in the MTLBO-BP neural network prediction model. This risk management model provides faster convergence and a more precise solution to the problem of reliability and cost allocation in engineering projects. Recently, Bilgin et al. (2023) propose a process model and a tool, COPPMAN (COnstruction Project Portfolio MANagement), were developed to support project portfolio decisions in construction companies.
2.3.4.2 Green cluster The green cluster is the second most significant cluster and relates mainly to the identification of risk and its classification. Table 5 summarizes all characteristics.

In real development, the success of a project can be jeopardized by a multitude of risk factors, which are not necessarily uniform and can vary widely. In most projects, risk impacts are often difficult to identify, relying largely on subjective assessments rather than hard data. Dikmen et al. (2007) proposes a methodology

Table 5 Occurrence and total link strength of keywords in green cluster


for quantifying risk assessments of construction projects. Specifically, the influence diagram method is used to construct a risk model. This is integrated with a fuzzy risk assessment approach to estimate a cost overrun risk assessment. While, it was the absence of empirical models for project risk planning and analysis that motivated Hu et al. (2013a) research in the context of software projects. To mitigate risk impacts and improve predictability of project outcomes, an integrative framework for intelligent software project risk planning (IF-ISPRP) was proposed. The research team employed the random forest algorithm to develop a risk analysis model and introduced a many-to-many actionable knowledge discovery method (MMAKD) for risk planning purposes.

To minimize the overall risks associated with a project, however, Albogami et al. (2021) proposed a new approach using a hybrid method of Analytic Hierarchy Process (AHP) and Dempster-Shafer theory of evidence. The study involved several phases: firstly, quantitative research was conducted to identify potential risk factors that could impact a project. Then, a hybrid unsupervised machine learning algorithm based on Principal Component Analysis (PCA) and agglomerative clustering was used to classify projects according to ownership, operational and technological, financial, and strategic risk factors. Finally, a hybrid AHP and Dempster-Shafer evidence theory was developed to select the best alternative with the lowest overall risk. The results of their study highlighted four primary risk categories: Property Risk Factors, Technology and Operational Risk Factors, Financial Risk Factors, and Strategic Risk Factors. More recently, Ansari et al. (2022) aim to take a significant step to improve the efficiency of projects by identifying and ranking the causes of claims and analyzing their effects on key efficiency indicators using AHP-TOPSIS technique.
2.3.4.3 Blue cluster The blue cluster, the characteristics of which are shown in Table 6, concerns the modelling and programming of project risk.

Table 6 Occurrence and total link strength of keywords in blue cluster


Mokhtari and Aghagoli (2020) propose a technique for selecting risk-responsive actions in the project portfolio. A Bayesian belief network is used to model the portfolio risks, their impacts and responses. Whereas, to select the response, an optimization model is used to minimize the sum of the residual risk impacts on the objectives of the portfolio components and the costs of implementing the responses. Solving the model is a genetic algorithm whose results support project managers in providing an appropriate combination of actions consistent with available resources. While, Lee et al. (2012) introduce a framework for assessing and simulating outsourcing risks in the supply chain. The framework aims to incorporate not only established but also emerging risks and is guided by sound risk management practices, including risk identification, analysis and mitigation actions. The proposed methodology involves both qualitative and quantitative risk assessment. For the former, the use of Failure Mode and Effects Analysis (FMEA) is suggested to construct a risk map. For the second, Monte Carlo simulation (MCS) is used. In a complex and dynamic environment with high uncertainties amidst limited resources, project risk assessment is crucial for project success. Isah and Kim (2021) propose a stochastic multiskilled resource planning model (SMSRS) for resource-constrained project scheduling problems (RCSPSP) that considers the impact of risk and uncertainty on task duration. The SMSRS model is developed by integrating a planning risk analysis (SRA) model with an existing algorithm (MSRS) to create feasible and realistic planning. In particular, triangular probability distribution and Monte Carlo simulation using MS Excel are applied to assess the risks and uncertainties associated with the duration of construction activities. Recently, Prieto and Alarcón (2023) develop new approaches regarding AI systems, using fuzzy sets and multiple linear regression for managing waste in construction project delivery in the metropolitan area of Santiago, Chile.
2.3.4.4 Yellow cluster The yellow cluster is mainly related to project-related economic risk, as can be seen from the cluster characteristics shown in Table 7.

Table 7 Occurrence and total link strength of keywords in yellow cluster


An industrial case concerning large projects in the energy industry is used to illustrate the application of the method proposed by Sanchez et al. (2020) to reduce the risk of project cost (or budget) overruns. The case study outlines the development of a rigorous and repeatable method for estimating the impact of Project Management Maturity (PMM) on project performance. Bayesian networks are employed to formalize the knowledge of project management experts and extract information from a database of previous projects, allowing for a better understanding of performance failures (such as the risk of cost overruns) caused by insufficient PMM maturity. Project portfolios are strategic tools for the implementation of corporate strategy. Therefore, Dixit and Tiwari (2020) proposed a way to reduce the likelihood of experiencing significant losses by implementing a risk-averse strategy. The approach involves using the conditional value-at-risk (CVaR) measure as an objective function to construct a portfolio of projects that has the least risky profile. There are three models that researchers have developed for selecting and planning project portfolios, namely the risk-neutral (max_E), risk-averse (max_CVaR), and combined compromise (max_E_CVaR) models. These models enable organizations to choose and plan project portfolios based on their appetite for risk and the importance they assign to risk-averse and risk-neutral objectives. A flexible and rational approach is proposed by Idrus et al. (2011) who proposed a method for estimating cost contingency based on risk analysis and a fuzzy expert system. The method involved the development of a cost contingency model in construction projects. The fuzzy expert system is incorporated in the use of the risk analysis technique as a general technique applied as a method for estimating project cost contingency. Recently, de Oliveira et al. (2023) propose an interesting case study on self-organizing maps and Bayesian networks in organizational modelling.
2.3.4.5 Purple cluster Finally, the smallest is the purple cluster with 8 keywords. This groups those articles from the literature that deal with risk assessment, response and management; as shown in Table 8.

Project risks are commonly treated as separate entities in the field of risk management. However, not considering the potential interrelationships among them can

Table 8 Occurrence and total link strength of keywords in purple cluster


lead to an inadequate assessment of potential risks and decrease the overall effectiveness of the management process. To address this problem, Guan et al. (2021) developed a new risk interdependence network model with the aim of helping deci-sion-makers accurately assess project risks and develop more effective risk mitigation strategies. The novel model incorporates both Interpretive Structural Modeling (ISM) and Monte Carlo simulation (MCS) techniques to effectively model the stochastic nature of project risk occurrence, considering interdependencies and analyzing the potential consequences of risk propagation. This integration allows for a more comprehensive and accurate assessment of project risks, providing decisionmakers with valuable insights to inform their risk management strategies.

Risk management (RM) is a process that heavily relies on knowledge, necessitating the effective management of risk-related information. However, it is common to overlook the importance of integrating various stages of the process, such as risk identification, analysis, response, and monitoring. This can result in suboptimal risk management outcomes and missed opportunities to identify and address potential risks. Fan and Yu (2004) show that Bayesian belief networks (BBNs) provide visible and repeatable decision support under conditions of uncertainty in software design risk management. A BBN-based procedure has been developed using a feedback loop to predict potential risks, identify sources of risk and advise on the dynamic adjustment of resources. Okudan et al. (2021) proposed a knowledge-based RM tool called CBRisk, which utilizes case-based reasoning (CBR) techniques. CBRisk is web-based, enables the cyclic RM process and incorporates an efficient case finding method using a comprehensive set of design similarity features in the form of fuzzy linguistic variables. The tool utilizes a database of past projects to provide a risk register model, which identifies them, calculates their probability and impact, and generates response plans for each risk. By understanding all RM processes and supporting the project team throughout the project lifecycle, CBRisk proves to be a valuable resource for managing risks effectively. While, recently, Waqar et al. (2023) explore the integration of AI into construction safety management, highlighting its potential to improve risk management. It identifies key factors for successful AI implementation, based on industry expert analysis.

# 2.4 Data analysis 

In this section we provide an analysis of data from the 170 primary studies with the aim of giving a clear overview of how the scientific community has moved to date and highlight any gaps to fill. The analysis is organized accordingly to the research questions listed above.

### 2.4.1 RQ \#1 "Are there industries where the spread of AI for PM processes has been wider and faster so far?"

Analysis of the selected sample from 1996 to 2023 shows that a large majority of studies are focused on a specific sector. Specifically, out of 215 articles, as many as 70 focus on construction ( $50.3 \%$ ). This sector is followed by the field of IT, software

development (13.4\%). The remaining articles are spread over different sectors as shown in Fig. 6.

The reasons that probably make these two sectors so relevant are essentially related to the fact that both sectors contribute to economic growth worldwide (Ma et al. 2019). However, it should be noted that although both the construction sector and the IT sector heavily utilize project management techniques, but for different reasons and in different ways as explained below:

1. Construction Sector: Project management is extensively used in the construction sector due to the inherently complex nature of construction projects. Here is why: a) Large-Scale Projects (Project management is crucial to manage the various aspects of these large-scale projects effectively); b) Multidisciplinary Teams (Project management ensures that these multidisciplinary teams work cohesively toward a common goal); c) Resource Management (Project management techniques help optimize resource usage, minimize waste, and keep projects on track); d) Budget and Cost Control (Project management methodologies assist in controlling budgets, tracking expenses, and preventing financial setbacks); and e) Risk Management (Project management provides strategies to identify, assess, and mitigate these risks).
2. IT Sector: The IT sector heavily relies on project management to navigate the complexities of technology-driven initiatives. Here is why project management is crucial in the IT sector: a) Rapid Technological Advancements (Project management provides a structured approach to adopting new technologies and managing complex software development projects); b) Software Development Lifecycles (Project management helps in organizing and streamlining these phases); c) Budget Constraints (Project management methodologies ensure efficient allocation of resources and cost control); d) Risk and Change Management (Project management techniques aid in managing changes, addressing risks, and maintain-
![img-5.jpeg](img-5.jpeg)

Fig. 6 Application fields of AI for PM processes

ing project stability); e) Agile Methodologies (Project management helps implement these methodologies effectively).

Thus, Project management is indispensable in ensuring the successful execution of complex, resource-intensive, and time-sensitive projects in both sectors.

# 2.4.2 RQ \#2 "What is the support for effectively applying the topic of AI in PM, in terms of frameworks, models, tools, etc., already provided in literature?" 

The second research question is asked to understand in a quantitative way the real extent of AI research for PM in terms of gained knowledge for an effective application. To obtain in-depth and detailed results, the research question is divided into sub-questions such as:

- RQ2.a: Which PM processes are most likely to be managed through AI?
- RQ2.b: Which AI categories are most involved in the research?
- RQ2.c: What are the most used AI tools for PM??
$\boldsymbol{R Q 2 . a :}$ According to PMBOK sixth Edition, there are seven main PM processes: Plan risk management, Identify Risk, Perform Qualitative rick Analysis Perform, Quantitative rick Analysis, Plan Risk Responses, Implement Risk Responses and Monitor Risks. The 215 in the analysis sample were investigated to understand the integration of AI into PM. The results show that only one process occurs frequently (43 items) while the rest occur insignificantly. Table 9 shows these results in detail.

Most of the articles dealt with PQRA processes. This is probably due to the quantitative and data-driven characteristics of these processes for which AI offers better advantages. The selected documents, however, revealed that several articles dealt with not just one process, but an integrated approach involving several processes in sequence. In particular, three main combinations of PM processes were intercepted (Table 10). However, it should be clarified that the "Perform risk analysis" process combines Quantitative Analysis and Qualitative Analysis.

The integrated approach in project management (PM) leverages AI for data collection, particularly in the quantitative phase of risk analysis. AI is utilized to analyze large datasets, identifying potential risk triggers and providing decision

Table 9 Number of papers for each PM process


Table 10 Number of papers for integrated $P M$ processes ((integration of AI into $P M$ )


support. This includes recommendations for risk response based on historical data and project context, as demonstrated in Ebrahimnejad et al.'s (2010) research, which outlines a new risk structure using methods like FTOPSIS and FLINMAP. Similarly, Isaac and Navon (2014) highlight the use of AI-powered dashboards for semi-automated project monitoring and risk management, including an Automated Project Performance Control (APPC) system. The research sample includes studies where AI is applied in PM processes, especially in areas closely related to risk management, such as Portfolio Analysis, General Framework, Prediction/Estimation/Forecasting, Optimization, and Decision Support Systems (DSS). These studies often use AI for risk identification and decision-making. The analysis is specific to papers where AI directly influences risk management decisions. Papers not directly utilizing AI for risk management, comprising $28 \%$ ( 49 papers) of the sample, are categorized under "other PM processes". This approach ensures a focused examination of AI's role in project risk management. Table 11 show the details.

For example, Han et al. (2008) introduced a web-based decision support system for managing risks in international construction projects, offering global accessibility and addressing the high risk of failure due to uncertainties. The paper emphasizes the significance of risk identification and analysis in project management. Ghasemzadeh and Archer (2000) discussed the challenges in selecting a project portfolio, proposing the PASS for structured decision-making. Idrus et al. (2011) developed a method for objectively estimating project costs using a fuzzy expert system, enhancing traditional subjective judgments in risk analysis. Furthermore, research on optimization in project management, though less prevalent, has been noted. Honari Choobar et al. (2012) applied optimization to classify risks in power plant projects using fuzzy analytical network and the fuzzy Technique for Order Preference by Similarity to Ideal Solution (TOPSIS) for a comprehensive risk assessment. Lastly, Fang and Marle (2012) created an integrated Decision Support System

Table 11 Number of articles for each other AI process


(DSS) framework for managing complex risk networks in projects. This framework combines the design structure matrix (DSM) for dependency modeling with the analytical hierarchy process (AHP) to evaluate risk interactions, supplemented by simulation techniques for dynamic risk assessment. This approach provides an indepth understanding of risk behavior and supports effective risk management deci-sion-making in project management. Additionally, simulation techniques are used to analyze the propagation of risks and reassess them as needed. By integrating these various approaches, the proposed framework provides comprehensive understanding of risk behavior and enables more effective risk management decision-making. To see if some PM processes have been systematically supported by AI in a specific industry, the relationship between sector and processes is analysed, as illustrated in Fig. 7. Radar charts show two series representing the sectors that, from the analysis conducted so far, they seem to have applied AI more to PM processes: construction and IT. For each sector, the number of documents reporting the PM processes of the PMBOK is reported, including the integrated ones, (Fig. 7a) and the PM processes
![img-6.jpeg](img-6.jpeg)

Fig. 7 Relationship between industry and processes: A: PM processes of PMBOK; B: "other" processes

that in this research have been indicated as "others PM processes connected to PM ones" (Fig. 7b).

As shown in Fig. 6, there is not a specific pattern, as both considered industries, construction and IT, present a higher number of papers dealing with performing quantitative risk analysis both as singular as well as integrated approach. Numbers are also consistent with the general trend not depending thus on any industry.
$\boldsymbol{R} \mathbf{Q 2 . b}$ : Continuing the investigation, the next step is to link PM processes with specific AI applications. There are a great number of AI applications and many ways to group them. In this research, eight possible AI applications are distinguished, the characteristics of which are shown in Table 12.

Also in this analysis, a distinction is made between works in which only one AI category is applied and others that mix several categories. A total of 132 papers $(77.1 \%)$ were found to apply only one category of AI. There are three categories with the highest number of applications in the surveyed sample, such as: 1) Advising; 2) Prediction and 3) Classification. The other categories have fewer than 10 associated documents. The importance of these 3 categories is also demonstrated by the Pareto Analysis shown in Fig. 8.

From the sample study, the category "Advising" is the most frequently used application of AI. For example, in Nie et al. (2009) research, advising is utilized to develop a mechanism for evaluating a company's eligibility for launching a data mining project. Similarly, Hu et al. (2013a, b) proposes an integrative framework called IF-ISPRP for intelligent software project risk planning, which leverages advising techniques. The second most applied AI category is "Predictive". A modelling framework using AI methods is applied by Wu et al. (2015) to develop an integrated interpretative structure modelling (ISM) and Bayesian network system in a risk assessment context. In the research of Ghasemi et al. (2018) forecasting is used to define a framework for analysing the risk of a portfolio to achieve sustainability. The last most applied category of AI is Classification. This category is applied in Ebrahimnejad et al. (2010) research to create risk classification methods that can identify critical factors and evaluate associated risks. In a similar vein, Fan and Yu (2004) employs AI classification to forecast potential risks, detect risk sources, and recommend real-time resource adjustments.

As far as the mix of categories is concerned, the results obtained from the sample study are shown in Table 13.

As shown, the "Classification/Prediction" pair is by far the most used. This is shown in the research of Zhang et al. (2013) that introduce a novel assessment framework that combines the analytical interval hierarchy process (AIHP) and the extension of the technique for order preference by similarity to ideal solution (TOPSIS). This approach aims to enhance the accuracy and dependability of risk identification in hydropower projects. Classification/Prediction is also applied in the context of cost, benefit and return on investment (ROI) risks of projects by Yet et al. (2016). A Bayesian network modelling framework capable of modelling various risk events is proposed, allowing users to assess project costs and benefits under different risk scenarios.
$\boldsymbol{R} \mathbf{Q 2 . c}$ : This research question aims to find out what are the most used AI for PM and why? Specific artificial intelligence tools are defined for each category of


![img-7.jpeg](img-7.jpeg)

Fig. 8 Pareto analysis for AI categories

Table 13 Number of papers for AI categories


AI. Specifically, 104 tools are identified, which in turn are grouped into clusters, as shown in Fig. 9. This classification took place in two steps in an empirical way. First, clusters were identified through a study aimed at identifying the main categories of AI mentioned in articles focusing on the topic available in the scientific literature. Then, for each article in the analysis sample, the AI tool applied was identified and placed in one of the categories identified in the previous stage.

Three of them account for $52 \%$ of the total tools, as shown in Table 14.

# 2.4.3 RQ \#3 "Is there a pathway that matches AI categories/tools and PM processes?" 

The investigation conducted so far has shown the importance of searching for pathways linking AI categories and PM processes. Therefore, several "cross-over"

![img-8.jpeg](img-8.jpeg)

Fig. 9 Clusters of AI tool
analyses are given below. The first analysis is shown in Table 15, where AI categories are cross-referenced with PM processes to evaluate if a relationship exists.

The analysis, as depicted in Table 15, indicates that out of various combinations of PM and AI, two are particularly significant. First, the Perform Quantitative/ Qualitative Risk Analysis combined with Prediction, utilized in 18 research papers. Notably, Hu et al. (2013b) employed Bayesian networks with causality constraints (BNCC) in this category, developing a framework for risk causality analysis in software projects. This framework focuses on identifying causal links between risk factors, using historical data to discover new connections and validate existing ones impacting project outcomes.

The second significant combination involves Advising in the context of Perform Quantitative/Qualitative Risk Analysis and Risk Response processes, featured in 14 studies. This indicates that risk analysis is instrumental in supporting decisions related to risk responses. Lachhab et al. (2018) showcased this through a multi-criteria decision support tool integrating Project Management and System Engineering (SE) sub-processes. They introduced a novel multi-objective ant colony (ACO) algorithm, MONACO, which uses a unique learning mechanism allowing ants to learn from past decisions, thereby optimizing future choices efficiently. Furthermore, Plan Risk Response combined with Advising was highlighted in the research of Yavari et al. (2013), which developed an effective method for measuring software risk using fuzzy logic. These results illustrate the evolving role of AI in enhancing various aspects of PM, particularly in risk analysis and response planning. A second analysis, shown in the Table 16 below, cross-references the AI categories with other PM processes to clarify the existing relationship.

The analysis reveals that only a few combinations of AI categories and PM processes yield significant results. The most prominent combination, featuring in 7 articles, is Consulting with Portfolio Analysis. In this context, Khalili-Damghani et al. (2013) introduced a multi-objective approach for selecting sustainable project portfolios, proposing a hybrid framework that merges data mining, Data Envelopment Analysis (DEA), and an evolutionary algorithm (EA) to construct a Fuzzy

Table 14 Key AI tools



Table 15 A cross-analysis between AI categories and PM processes


Table 16 A cross-analysis between AI categories and other PM processes
PM process


Rule-Based (FRB) system. Another notable combination, found in 6 articles, is Decision Support Systems (DSS) with Consulting. This involves modeling, identifying, and interacting with risks, particularly in complex and uncertain project environments. Fang and Marle (2012) proposed an integrated DSS framework that includes risk network identification, evaluation, and analysis, combining the design structure matrix for dependency modeling with the analytical hierarchy process for risk interaction evaluation. This simulation-based model aids project managers in planning risk response actions systematically. However, the impact of Advising in developing a General framework is less apparent, with only three articles addressing this aspect. Notably, Dey (2012) integrated all risk management processes, including risk identification and assessment, using a combined multi-criteria decisionmaking technique and decision tree analysis. This approach employs the cause-andeffect diagram for risk identification, the analytical hierarchy process for analysis, and a risk map for developing responses. Decision tree analysis is then applied to model various risk response options and optimize risk mitigation strategies. Another analysis was conducted by cross-referencing the AI categories with the integrated approaches of the PMBOK stages intercepted in a previous analysis. The results are shown in Table 17.

Considering the integrated PM processes, the most significant results are noted for Identify Risks + Perform Quantitative Risk Analysis associated with Prediction and Advising; and Risk + Perform Quantitative Risk Analysis + Planning Risk Responses associated with Advising.

The latter solution is given by Khodakarami and Abdi (2014) with their research aiming to fill a gap in the literature. According to his studies despite a causal relationship between sources of uncertainty and cost items; this causality is not modelled in current state-of-the-art project cost risk analysis techniques (such as simulation techniques). Therefore, it proposes a quantitative evaluation framework by modelling the uncertainty of common characteristics and performance indicators affecting cost items. The model integrates the Bayesian network inference process

Table 17 Cross-category analysis of AI and integrated PM processes
PM process


to probabilistic risk analysis. The data analysis indicates that AI research in project management (PM) primarily focuses on technological aspects and specific applications. The literature suggests the field is not yet mature from a managerial perspective, lacking sufficient knowledge for widespread AI integration in PM. Future research directions are discussed next.

# 3 Discussions 

This discussion is structured, as the data analysis in the previous section, according to the posed research questions and findings are used to advance, in the last paragraph, future research directions that need to be explored further by scholars.

### 3.1 Main application fields

The analysis shows that AI is applied for the risk management of projects mainly in two sectors: construction and IT sector. Concerning the construction industry, reasons behind the interests for AI seem to be twofold: first of all the economic and social role played from this industry (Moradi et al. 2022). The Global Construction 2030 estimates in fact that global spending on construction and engineering projects may reach over $\$ 212$ trillion by 2030 (Robinson 2015). Not surprisingly, the construction industry is the mainstay of the economy in many countries, accounting for a significant percentage of the nation's Gross Domestic Product (GDP). For example, in China, in 2016, the total value of construction output was $6.5 \%$ of GDP (Ayoub and Mukherjee 2019). In Italy, in 2021, the construction sector had a percentage value of $4.9 \%$ of GDP (Norkus and Markevičiūtė, 2021), while in Malaysia, in the same period, the percentage was $4.5 \%$ (Mustafa et al. 2021). Besides, this industry faces also organizational and management difficulties due to the complexity and dynamism of these projects that always show a strong propensity to risk even when characterized by pre-calculated and calibrated project details (Pinto et al. 2011). Consequently, the dominant feature of this environment is the risk due to processes that are very difficult to manage as they are characterized by many decisions, often spread over a long period of time with many interdependencies in a highly uncertain environment (Chen et al. 2022). The challenge is to create a risk management system that adopts tools and methodologies suitable for the construction industry, which motivates research interest in the application of AI in this sector. One more reason why the world of research has directed its interest towards this field is the spread in recent times of Building Information Modeling (BIM). The term BIM finds a synonym in "digital twin", which indicates the integral digital transposition of the model of a material work (López et al. 2018). During its life cycle, each building constantly generates a set of data that represent the genetic code of an asset's digital twin (Azhar et al. 2012). If the data transmitted from one stage of the life cycle to another is accurate and truthful, all stakeholders can be reliably informed through appropriately verified digital transactions entrusted to a

distributed accounting system (Sacks et al. 2010). Considering that AI feeds on data, these systems can be the promoters and accelerators of the use of AI in project risk management.

Concerning the IT sector, in particular the software development industry it is important to say that in just a few years, software has "eaten" both traditional markets (bookstores, advertising, music distribution, recruiting, communications) and individual processes or portions of value chains (logistics and distribution, price optimization, satellite image management, transport) (Pontikes 2022). This spread is evidenced by the Compound Annual Growth Rate (CAGR) growing by $14.3 \%$ in 2022, resulting from the market value increasing from USD 1141.43 billion in 2021 to USD 1304.74 billion in 2022. In the short term, the market is estimated to grow to $\$ 2040.37$ bn in 2026 at a CAGR of $11.8 \%$ (Tang et al. 2022). However, to date, software design and development are high-risk activities. The success rate of global software projects is only about $32 \%$ (Sharma and Kumar 2022). The cause of this failure is the risks associated with the software development project (Butler et al. 2020; Mahmud et al. 2022; Fazli et al. 2020). Research shows that AI and machine learning may be the solution to the problem as they can revolutionize each stage of the software development life cycle (SDLC) (Wallace et al. 2004). Given the more advanced state of development in the two industries, they are candidates to become the subjects of a more searching study and testing with the aim to code the knowledge and best practices for a more effective application of AI in PM.

# 3.2 Integration between AI categories and PM processes 

The analysis of project management (PM) processes, as per the PMBOK guidelines, shows that "Identify Risks", "Perform Quantitative Risk Analysis", and "Plan Risk Responses" are the most frequently used processes. A significant trend observed in the sample is the integration of multiple PM processes. For instance, "Performing Risk Analysis" is often combined with "Monitoring Risks" or "Identifying Risks", with the latter also being integrated with "Perform Risk Analysis" and "Plan Risk Responses". This integration forms a complex "black box" of interconnected processes.

In this scenario, AI plays a pivotal role by providing "augmented intelligence". AI assists project managers in handling the complexities of these integrated systems. Interestingly, the application of AI extends beyond typical PM processes to include "other processes" such as Portfolio Analysis, General Framework, Prediction/Estimation/Forecasting, Optimization, and Decision Support Systems (DSS). These other processes are covered in $28 \%$ of the sampled articles, indicating a broadening scope of AI application in PM that goes beyond conventional risk categories.

The study also categorizes various AI applications, including Advising, Classification, Clustering, Guiding, Knowledge Extraction, Modelling, Optimization, Prediction, and Regression. Among these, Advising, Prediction, and Classification emerge as the most utilized in the sample. This trend persists even in integrated approaches, with Classification/Prediction being the dominant combination, followed by Classification/Advising and Classification/Clustering/Prediction. These

findings underscore AI's role in enhancing, not replacing, the project manager's functions. AI facilitates cognitive capabilities with high accuracy and performance, transforming the PM's role to collaborate with AI systems, monitor their performance, analyze outcomes, and complete tasks beyond the scope of autonomous systems (Hribernik et al. 2021). The analysis also reveals that significant AI categories like Advising, Classification, and Prediction are consistently integrated into common PM processes. However, when it comes to "Other Processes", Advising is predominantly applied, particularly in Portfolio Analysis and General Framework. The study suggests that no single AI category is exclusively suited for specific PM processes. Thus, it highlights the potential benefit of developing a matching system between PM processes and AI categories to better support their application in project management activities.

# 3.3 Artificial intelligence tools and recommendations for practitioners 

The most significant impact of AI in PM processes is observed in the construction and IT sectors, accounting for a substantial portion of the research focus. In the construction sector, AI plays a pivotal role in managing large-scale, complex projects, facilitating cohesive work among multidisciplinary teams, optimizing resource usage, controlling budgets, and mitigating risks. In the IT sector, AI aids in handling rapid technological advancements, streamlining software development lifecycles, managing budgets, and implementing agile methodologies (Al-Mhdawi et al. 2023). These sectors are crucial due to their substantial contributions to global economic growth and the complexity of projects they encompass. Recent research demonstrates how new AI models (e.g. deep neural networks and reinforcement learning) are increasingly used in project management to improve risk prediction and resource optimization (Altan and Işık 2023). Innovations in AI are revolutionizing project management through tools such as predictive analytics platforms, which predict future outcomes by improving decisions and optimizing resources. AI-powered risk management software identifies risks early, while advanced decision support systems provide data-driven recommendations. AI-enhanced collaboration platforms improve communication and workflows, and robotic process automation (RPA) tools free up human resources for high-value tasks. Additionally, generative AI facilitates content creation, increasing efficiency and reducing manual efforts (Fridgeirsson et al. 2023; Zabala-Vargas et al. 2023). With these premises, the study of the analysis sample identified more than a $\mathbf{1 0 0}$ AI tools. Given the large number, these were grouped into clusters, such as: Case Based Reasoning (CBR), Network Analysis, DSS, Algorithm, Fuzzy Logic, Simulation, Machine learning, Support vector machine, FMEA and Others. Each paper in the sample, based on the AI tool reported in the research, was placed in one of the identified clusters which resulted in a clear prevalence of three clusters, such as: Fuzzy Logic, Network Analysis and Decision Support System. However, this result is not surprising but in line with previous findings. These tools, like the most applied AI categories and PM processes, are characterized by their supporting capability. The

term "fuzzy" refers to the ability to handle imprecise or vague input. Fuzzy logic in fact comes very close to human reasoning by applying linguistic descriptions to define the relationship between input information and output actions (Ahmed et al. 2022). Network Analysis tools use a network as a decision support technique to handle probabilistic events. Whereas Decision Support Systems improve the quality of decisions by providing powerful analysis capabilities that enable the exploration and comparison of a set of mutually incompatible alternatives (Hak et al. 2022). In addition, to the clear trend owards the application of solutions capable of supporting and improving project risk management activities, from the analysis of the 215 papers it was impossible to individuate a clear-cut divide among PM processes, AI categories and AI tools. It means that research is still in a primordial state comparing to application of AI in other topics (i.e. medicine, etc.), as well as that there is an important gap to fill. In fact the lack of a trajectory to take makes the application of AI in PM very chaotic and probably uneffective. Table 18 summarizess the challenges for the construction sector and for the IT sector with AI integration in project management.

Definitely, the study allows us to affirm that AI's role in project management is multifaceted and expanding. Its ability to handle large datasets, provide insightful analysis, and support complex decision-making processes significantly enhances the effectiveness of PM, especially in sectors characterized by high complexity and rapid technological change. The insights from AI applications in PM not only aid current practices but also pave the way for future innovations and research directions in this field. As AI continues to evolve, its integration within PM processes is expected to become more profound, offering new opportunities and challenges for project managers and organizations. For the previous considerations, practitioners should select AI tools that align with their specific project needs, team size, industry, and the complexity of the tasks at hand. The key is to leverage these tools to enhance efficiency, decisionmaking, risk management, and overall project success. Table 19 offers a concise overview of various AI tools and platforms, highlighting their primary functions and key features. It serves as a guide for project management practitioners to select appropriate tools based on their specific needs and project requirements.

It is equally important to keep some considerations in mind for choosing AI Tools, as follows:

- Compatibility with Existing Systems: Ensure the tool integrates well with current project management software and systems.
- Scalability: Choose tools that can scale with the growth of projects and organization.
- User-Friendly Interface: Prioritize tools with intuitive interfaces to facilitate quicker adoption by the team.
- Cost-Effectiveness: Consider the cost-benefit ratio, especially for small and medium-sized projects.
- Data Security and Privacy: Ensure the tool adheres to data security and privacy standards.

![img-9.jpeg](img-9.jpeg)

## 18 Challenges for the construction sector and for the IT sector with AI integration in PM




# 4 Future development and research agenda 

This present research provided a global picture of AI in project risk management and a few concerns arose to constitute the base for future developments and to structure a research agenda:

1. Construction and IT sectors made the most progress in applying AI to project risk management processes: most of research in the literature addressed the issue specifically or, if presenting an application, it was in either of the two industries. Such concentration of papers asks for a deep investigation to identify a scientific rationale that could boost AI in project risk management even in other industries.
2. There exists no pathway in applicating AI to project risk management: despite the large amount of research developed in the last years, scientifically substantiated choices in selecting an AI category/tool under specific circumstances don't seem to occur, as well as best practices to guide the effective application. This leads to the conclusion that the topic remains relatively disintegrated theoretically.
3. Project risk management processes are mostly involved by AI in an integrated way: the majority of papers address AI not only in a specific project risk management process, but by developing a tool or a procedure to cover more processes. This trend sends a clear message that researchers and practitioners intend to recognize a pervasive role played by AI or even it might mean the pursuing of a fully automated approach to project risk management.

Throughout this review, we critically evaluated the literature related to our research questions and highlight potential gaps for further study. We outlined a fourpronged agenda for future AI in PM research that build from the identified gaps:

1. Providing general frameworks for introduction of AI in PM: in the previous section we highlighted as the theoretical knowledge on the topic is large yet unorganized and it leads to chaotic implementation trajectories. In other fields, as such as medical application (He et al. 2019), researchers and practitioners have been able to develop guidelines, good practices, check lists, and even regulatory documents to support and make more effective AI implementation. Clearly, the project risk management would also benefit of frameworks to guide choices towards the most suitable methods/tools adjusted to the characteristics of the context or the project. Throughout this review we also glimpsed possible drivers to structure knowledge as such as number and type of processes involved, aim to be pursued, proposed role for AI. In the next future we hope for researchers focussed on exploring those drivers or even finding new ones.
2. Developing criteria for evaluating AI performance: this area of research is connected and serving the previous point as well. In fact, despite a large amount of KPIs aimed at evaluating technical performance of AI, criteria to assess instead the effectiveness of AI implementation methods are missing. Addressing this issue might be very helpful also to provide effective frameworks for introduction of AI in PM.

3. Selecting enabling factors for implementing AI in PM: factors as such as a better organizational culture and a higher level of maturity in project risk management, as well as availability of data and processes of knowledge management might easily represent enabling factors and for this be explored together with new ones coming from analysing current implementation. A good starting point for this line of research is the analysis of construction and IT, as industries with the greatest number of applications AI to PM.
4. Hard Skills Development: Training and skill development are crucial for project managers in the digital age, allowing them to understand and effectively apply AI technologies. This not only improves efficiency and innovation in projects, but also ensures competitiveness and adaptability in a rapidly changing business environment.

Table 20 provides a structured overview of the key recommendations for both practitioners in the field of project management and researchers focusing on the future of AI in this domain. It highlights actionable steps for current practice and areas of interest for academic and practical research.

# 5 Conclusion 

Project risk management is a crucial phase for project success, especially in dynamic environments where traditional tools are proving inadequate due to their lack of planning, collaboration, automation, and smart functionalities. To address these gaps, recent research has increasingly focused on the application of AI in project risk management. A literature review was conducted on 215 articles published between 1996 and 2023 to understand the scientific community's progress in this area. The review aimed to answer research questions about AI's application areas in project risk management and to explore any patterns between AI categories or tools and PM processes. The research indicated that AI in PM is predominantly applied in the construction and IT sectors. The AI categories most employed in these sectors are those with capabilities for analysis, processing, and learning, which are necessary to support project managers in handling large amounts of data. The most popular AI tools are those that can manage ill-defined and seemingly disconnected information, predict events, compare alternatives, and deliver accurate results quickly. AI algorithms, complemented by human skills and experience, are essential for rapidly evaluating data and providing effective responses to achieve project objectives. The role of AI is seen as strategic, not to replace humans but to enhance human capabilities with data analysis power. An interesting trend identified in the study is the integrated approach to addressing PM processes, aiming to provide a unified and automated solution for a substantial portion of PM. Despite analyzing a large number of studies, the research could not identify clear trajectories, patterns, or best practices for AI application in PM. This gap, along with the trend of integrating PM processes and the advancements in IT and construction sectors, forms the basis of the proposed research agenda. This research is among the first to quantitatively evaluate AI's application in PM through a literature review. However, it reveals that this

Table 20 Recommendations for practitioners and future research


solution is still in its early stages, lacking a well-defined path for successfully integrating PM processes and AI categories. Future studies are encouraged to develop ad hoc tools and methods for applying AI in specific industries, with potential for replication in other fields. The findings suggest an urgent need for future research to focus on identifying clear trajectories and best practices for the integration of AI in PM processes (such as Identify Risks + Perform Quantitative Risk Analysis associated with Prediction and Advising, and Risk + Perform Quantitative Risk Analysis + Planning Risk Responses associated with Advising). This future research should aim to develop tailored AI tools and methodologies for specific industries, potentially establishing a well-defined framework that can be replicated across various sectors. Such studies could significantly contribute to bridging the current gap and advancing the field of AI in project management. Based on the latest scientific research, it is clear that adopting AI in project management presents significant challenges, such as data privacy and security issues, which require robust protocols to protect sensitive information. Ethical considerations, such as algorithmic bias and impact on work, need special attention to ensure fairness and transparency. Barriers to adoption include resistance to change, lack of technical expertise and the cost of initial investments. Overcoming these challenges requires ongoing training, stakeholder engagement to develop trust in AI technologies, and strategic investments in security and skill development, ensuring that AI is used responsibly and effectively.

Supplementary Information The online version contains supplementary material available at https://doi. org/10.1007/s11301-024-00418-z.

Author contribution Conceptualization, M.E.N., and F.D.F.; methodology, M.E.N. and F.D.F.; software, C.D.L.; writing-original draft preparation, M.E.N., A.F., C.D.L.; writing-review and editing, M.E.N. F.D.F. and A.F.; supervision, M.E.N. and F.D.F. All authors have read and agreed to the published version of the manuscript.

Funding Open access funding provided by Università Parthenope di Napoli within the CRUI-CARE Agreement. We have not received any funding for this study.

Data availability All data and resources discussed in this document are freely available and accessible to the public.

# Declarations 

Conflict of interest We all authors declare that we have no conflict of interest.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/ licenses/by/4.0/.

# Authors and Affiliations 

## Maria Elena Nenni ${ }^{1} \cdot$ Fabio De Felice ${ }^{2} \cdot$ Cristina De Luca ${ }^{2} \cdot$ Antonio Forcina ${ }^{2}$

Fabio De Felice
fabio.defelice@uniparthenope.it
Maria Elena Nenni
menenni@unina.it
Cristina De Luca
cristina.deluca001@studenti.uniparthenope.it
Antonio Forcina
antonio.forcina@uniparthenope.it
1 Department of Industrial Engineering, University of Napoli Federico II, Piazzale Tecchio. 80, 80125 Naples, Italy
2 Department of Engineering, University of Naples "Parthenope", Isola C4, Centro Direzionale Napoli, 80143 Naples, NA, Italy