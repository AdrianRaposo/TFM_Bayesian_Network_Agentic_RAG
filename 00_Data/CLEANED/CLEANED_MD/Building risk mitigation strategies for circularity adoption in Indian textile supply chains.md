# Building risk mitigation strategies for circularity adoption in Indian textile supply chains 

Ashutosh Mishra ${ }^{1} \cdot$ Gunjan Soni ${ }^{1}$ (D) $\cdot$ Bharti Ramtiyal ${ }^{2} \cdot$ Mayank Dhaundiyal ${ }^{3} \cdot$ Aalok Kumar ${ }^{4} \cdot$ P. R. S. Sarma ${ }^{4}$<br>Accepted: 10 May 2023<br>(c) The Author(s), under exclusive licence to Springer Science+Business Media, LLC, part of Springer Nature 2023


#### Abstract

Textile industries are among the most polluting and demand urgent management measures to mitigate their negative environmental impact. Thus, it is imperative to incorporate the textile industry into the circular economy and to foster sustainable practices. This study aims to establish a comprehensive, compliant decision framework to analyse risk mitigation strategies for circular supply chain (CSC) adoption in India's textile industries. The Situations Actors Processes and Learnings Actions Performances (SAP-LAP) technique analyses the problem. However, interpreting the interacting associations between the SAP-LAP modelbased variables is somewhat lacking in this procedure, which might skew the decisionmaking process. As a result, in this study, the SAP-LAP method is accompanied by a novel ranking technique, namely, the Interpretive Ranking Process (IRP), which reduces decisionmaking issues in the SAP-LAP method and aids in evaluating the model by determining the ranks of variables; furthermore, the study also offers causal relationships among the various risks and risk factors and various identified risk-mitigation actions by constructing Bayesian Networks (BN) based on conditional probabilities. The study's originality represents the


[^0]
[^0]:    G Gunjan Soni
    gsoni.mech@mnit.ac.in
    Ashutosh Mishra
    ashutosh_m@me.iitr.ac.in
    Bharti Ramtiyal
    bhartiramtiyal.mgt@geu.ac.in
    Mayank Dhaundiyal
    mdhaundiyal@jgu.edu.in
    Aalok Kumar
    aalok.kumar@iimv.ac.in
    P. R. S. Sarma
    prs.sarma@iimv.ac.in
    1 Department of Mechanical Engineering, Malaviya National Institute of Technology, Jaipur, Rajasthan, India
    2 Department of Management Studies, Graphic Era (Deemed to Be University), Dehradun, India
    3 Jindal Global Business School, O P Jindal Global University, Sonipat, Haryana, India
    4 Indian Institute of Management, Visakhapatnam, India

findings using an instinctive and interpretative choice approach to address significant concerns in risk perception and mitigation techniques for CSC adoption in the Indian textile industries. The suggested SAP-LAP and the IRP-based model would assist firms in addressing risk mitigation techniques for CSC adoption concerns by providing a hierarchy of the various risks and mitigation strategies to cope with. The simultaneously proposed BN model will help visualise the conditional dependency of risks and factors with proposed mitigating actions.

Keywords Circular supply chain $\cdot$ Bayesian networks $\cdot$ Risk mitigation strategies $\cdot$ Indian textile sector $\cdot$ Interpretive ranking process

# Abbreviations 

CE Circular economy
SC Supply Chain
CSC Circular supply chain
TSC Textile supply chain
SAP-LAP Situations actors processes and learnings actions performances
IRP Interpretive ranking process
BN Bayesian networks
DAG Directed acyclic graphs

## 1 Introduction

With the rising prominence of sustainability and environment-friendly operations in the clothing industry, the Circular Economy (CE) has become crucial for industrial organisations (Breja et al., 2010; Mishra et al., 2023). The transformation from the linear take-make and dispose process to a Circular Supply Chain (CSC) is unavoidable for textile manufacturing sectors to have a sustainable and equitable global economy (Balanay \& Halog, 2018; Coste-Maniere et al., 2018). Apprehensions about sustainably developing goods, such as macroclimate change and rising carbon emission levels, have compelled businesses to shift from a linear operation to a circular creation model (Lahane \& Kant, 2022).

The CSC and its implementations are primarily necessary for the textile sector; The textile manufacturing sector is one of the most polluting sectors in the world, contributing $20 \%$ of global water pollution, $10 \%$ of global carbon emissions, and approximately 90 million tonnes of solid waste to landfills each year. The textile supply chain (TSC) processes use many compounds that pollute water, air, and land (Kazancoglu et al., 2020a, 2020b). The amount of textile waste is rising worldwide; nevertheless, recycling or reusing textile goods will minimise new waste from raw materials (Koszewska, 2018; Leon et al., 2016). Like all industrial operations, the textile sector requires a lot of water to finish the production process (Bukhari et al., 2018; Voncina et al., 2018). CSC principles can help in reducing pollution by increasing substantial energy concentration, reducing materials, using re-usable materials, using fewer toxic materials, increasing recycling ability, focusing on source efficiency, using goods for a long time, creating value-added products, and eradicating waste, so the use of raw materials and virgin fibres can be considerably decreased (Forman \& Carvalho, 2017; Kazancoglu et al., 2020a, 2020b; Levanen et al., 2021).

In the last few decades, textile companies have made products with a relatively shorter product life cycle, which makes them less durable and more expensive. The usage of textiles and the waste of textile goods have increased considerably (Kazancoglu et al., 2020a, 2020b; Levanen et al., 2021). The trash generated during the production method would be an essential input for other manufacturing methods, including gathering raw resources, designing, yarn manufacturing, spinning process, weaving process, dyeing process, sewing process, and cutting process. Today's linear economy cannot achieve a more sustainable and green production process, so CSC implementation is required, particularly in the textile sector (Chauhan, 2016; Franco, 2017). Yet, it was proposed to textile firms that they transition their capacities from linear to circular processes; however, enterprises have encountered various vulnerabilities throughout this process. As a result, the managers and decision-makers in the textile supply chains (TSCs) are less prone to accept this transition from linear to circular processes considering the risk associated with it (Ambika \& Srilekha, 2021). Various dangers and risk factors make CSC networks increasingly complicated. It may steer the organisational supply chain towards a culture of disruptions, with the implications being a decline in any organisation's complete performance and many more spartan effects if administrators do not account for extenuation actions promptly. Understanding risks and their management for CSC implementation in textile sectors is critical for this consideration. As a result, to address the difficulties of risks and ambiguity in adopting circular processes in the textile industry, this research proposes a few significant research objectives, which are as follows.
i. To understand and identify the risks of adopting CSC practices in Indian Textile industries.
ii. To develop a decision-making framework for risk mitigation strategies for circularity adoption in the TSCs.
iii. To analyse the inter-relationships between various risk and mitigation strategies of CSC initiatives in the TSCs.
iv. To quantify causality between various factors of adoption risk of CSC initiatives in the TSCs.

The current study proposes a management framework for risk-curtailing strategies to help managers successfully manage CSC operations. For this, we employed the SAP-LAP methodology, commonly regarded as a compliant approach developed by Sushil (2001). It is an intuitive decision-making process with certain limits regarding rationality, transparency, perceptive overload, etc. As a result, in this study, the variables have been ranked concerning process performance determined using the IRP procedure (Mangla et al., 2014). Constructing Bayesian Networks (BN) for conditional dependencies between different risks and mitigation strategies is necessary to understand the causal relationship between risk factors. The suggested general model for all textile industries is maintained to enable its application in real-world instances. The rest of the current research is organised as follows:

Section 2 contains an examination of pertinent literature. The research technique is explained in Sect. 3. Further, Sect. 4 provides the application of the SAP-LAP paradigm by considering an example of a textile firm that shows how the suggested approaches can be used. IRP and BN analysis are presented in Sect. 5 and 6, respectively. Additionally, the results and discussions followed by the study's implications are presented in Sect. 7. And in the last section of the study, the conclusions, limitations, and future scope for further exploration are offered in Sect. 8.

# 2 Literature review 

The subsequent literature review discussion is divided into three sub-categories, i.e., the role of CSC in the textile sectors, the risk of CSC adoption in the textile supply chain, and the previous studies that have implemented SAP-LAP, IRP and IRP and BN methodologies. This section broadly discusses aspects related to the role of CSC in textile industries prescribed in recent literature studies, identified risk factors associated with the implementation of the CSC principle in textile industries and a comparison of past literature studies based on the scope methodology adopted and key outcomes.

### 2.1 Role of CSC in the textile sectors

The textile and apparel supply chain, which includes housing, transportation, and sustenance, significantly impacts the environment. These concerns of the industry involve lowering the cost of materials as well as energy consumption, increasing usage of renewable resources, reducing substantial harmful dispersion, extending product durability, improving recycling, and improving service from a sustainability standpoint (Fischer \& Pascucci, 2017; Forman \& Carvalho, 2017). The existing phase of the CE involves the shared and linear circulation of resources. The literature has focused on textile and fabric recycling and reuse difficulties. Changes may be made so that resource usage is controlled in a closed-loop manner as if continuously elegant and nutritive (Valentine et al., 2017; Voncina et al., 2018).

Consequently, compared to burning and landfilling, the recycling and re-utilisation of textile goods are widely acknowledged as the desired technique for reducing environmental consequences (Prakash et al., 2020; Shukla et al., 2022). According to Yu et al. (2015), CSC adoption is critical to boosting a firm's overall efficiency from a systematic standpoint. Furthermore, recent research on the barriers to CSC adoption in diverse situations has provided insight and practical recommendations for CSC adoption (Balanay \& Halog, 2018; Koszewska, 2018). Recent studies have intensive on specific settings, such as the industrial sector, the car business in developing nations, and the rehabilitation and devastation of the trash disposal sector (Kabadurmus et al., 2022). There has, however, been little research on the challenges the textile industry experiences in switching to CSC and how to solve them (Crespo et al., 2018; Franco, 2017; Quartinello et al., 2017).

Regarding inventory retrieval and adverse effect reduction, parts of CSC practices are reintroduced into the supply chain through closed-loop systems. Implementing CSC adoption strategies may considerably reduce manufacturing waste (Benltoufa et al., 2018; Bukhari et al., 2018; Immacolata, 2018). Moving the textile industry towards CSC requires unique system-level innovations and unprecedented dedication, invention, and cooperation. Numerous entrepreneurial concerns are possible barriers to a paradigm shift. The purpose of this study was to fill a research vacuum by proposing risk mitigation strategies for using CSC intervention approaches. (Gardetti, 2018; Lahane \& Kant, 2022).

According to the review of past studies, CSC adoption has various practical characteristics, including multiple vertical stages in the supply chain: the micro, macro, and meso levels (Franco, 2017). For pivotal businesses, the hurdles of transitioning to a circular operation model include determining the logic of how a firm generates, value supply and capture for, and inner loops of closed material. Wang et al. (2022), Identify many risks that prevent small and medium-sized enterprises (SMEs) from adopting CSC business types, such as an absence of cash, technical knowledge, administrative costs, supply and demand network assistance, government backing, and information. According to one more study by Serra

et al. (2021), the most significant barriers to CSC adoption include initial financial expenses, misconceptions, and a sense of urgency. According to another survey, the most significant risks to CSC adoption include high initial funding costs, ambiguity, and a lack of speed. Kim and $\mathrm{Wu}(2021)$ classified constraints as internal and external to the focus enterprises and recommended closed-loop business models that would demand tailored CSC resolutions. Establishing a CSC at the macro level is crucial for numerous closed-loop remanufacturing or recycling corporate models (Gardetti, 2018; Y. Kim \& Wu, 2021). Kazancoglu et al. (2020a, 2020b) investigated the scuffles and challenges of CSC implementation inside the textile and fabric supply chain. They revealed that the most significant common roadblocks are a lack of the customers' consideration of remanufactured products or goods, commercial expertise restrictions in producing goods that can be rapidly redeveloped, and a lack of public awareness for a CSC (Serra et al., 2021; Yu et al., 2015).

Furthermore, Grundmann et al. (2013) researched the causal links between different barriers in a CSC; redesigning and repurposing was the most challenging obstacle in remanufacturing the goods. According to a study by Chen and Lin (2021) on the risks of CSC adoption, cultural difficulties, including a lack of consumer interaction, understanding, and uncertain business culture, are the most critical barriers for representatives and textile business specialists implementing CSC.

# 2.2 Identification of risks in the adoption of CSC practices in textile industries 

Table 1 depicts the obstacles to implementing CSC in textile enterprises' supply chains, as found by completing comprehensive literature research and gathering comments from textile sector experts in India.

### 2.3 Past studies using SAP-LAP, IRP, and bayesian networks

A few past studies are presented in Table 2, in which the SAP-LAP, IRP or BN methods have been used for developing the risk mitigating strategies in the different sectors. It can be observed from Table 2 that the various studies used these tools to construct the risk mitigation measures at different supply chains, as Gangotra and Shankar (2016) developed risk mitigation strategies for the implementation of business analytics in the telecom sector. Mangla et al. (2014) proposed a decision-making framework for green supply chain management.

In the most recent studies, Kumar et al. (2022) and Pal and Shankar (2022) used SAPLAP and IRP methodologies for proposing decision-making frameworks. Zhou et al. (2023) used BN modelling integrated with Fuzzy AHP to investigate risks from an SC perspective. Similarly, Hosseini and Ivanov (2022), Yusriza et al. (2022) and Chhimwal et al. (2021) used BN modelling in their respective research works.

Following the completion of the literature review on adopting CSC in the textile production process, a few gaps were identified that the current study attempted to address.

From the literature exploration, it is found that transitioning towards circularity in textile production from the Linear-production process in the Indian context has not been explored yet.

The Risks of adopting circular and regenerative behaviour in textile production and consumption in India are not yet discussed.

How SC managers can analyse the risk mitigation strategies that can be developed in the context of Circularity adoption has not been discussed yet.

Table 1: List of CSC adoption risks in Textile sectors


Table 1 (continued)


Table 1 (continued)


Table 1 (continued)


In what ways factors can be analysed to facilitate the textile SC in improving their ecological and economic performance has not been explored yet.

To address these gaps, the study aims to perform an integrated methodology, including SAP-LAP, IRP, and BN methodologies, to assist the managers and policymakers in the risk mitigation measures in the textile industries. In the further sections of the study, the conceptual SAP-LAP method is used to develop risk mitigation strategies (Sushil, 2001). However, increasing the openness standpoint. The IRP approach has been documented in the literature to accomplish this. The causal relationship between various risks and risk factors is crucial for the implementation of risk mitigation strategies; therefore, the Bayesian Network method is used to analyse the typical causal relationship amongst different risks and recognised actions to mitigate the risks; the BN model is based on conditional probability addressed the conditional dependency which may use to perform actions for mitigation of

Table 2 Existing studies Using SAP-LAP, IRP, or BN Methodologies


circularity adoption risks in TSCs of India. The research methodology used for the study is discussed in the next section.

# 3 Research methodology 

This study employs a qualitative research approach to achieve the objectives of this research. Because the expert's opinion is critical, a decision panel of specialists must be formed to

debate the topic. As a result, a few industrial visits and surveys have been done to investigate the impact of risks, troublemaking events, and objective risk aspects in adopting CSC efforts in India's textile sectors from a comprehensive viewpoint. A group of professionals, comprising senior managers and employees from various textile production establishments, advisors, academicians, and consultants, participated in the process and shared their experience, thoughts, and knowledge about CSC adoption and the circular or closed-loop business concept in Supply Chain Management, CSC adoption risks complications, and the importance of extenuating internal as well as external turbulences in the SC. Every expert participating has a strong decision-making ability and has managed administrative tasks for at least 5-6 years. Following a fundamental grasp of risk management and CSC, it is essential to establish a decision-making attempt to minimise risk concerns expressly. In this regard, an SAP-LAPbased method presents a management practice for developing risk extenuation approaches framework for CSC adoption within India's textile and fabric industries. In addition, the IRP approach is used to understand interfaces between the different variables of flexible SAP-LAP-centred decision-making approach.

The same group of experts was interviewed to determine the causal relationship among various factors and sub-factors of risks identified by the literature review discussed in the prior section. To analyse the mutual causal relationship among factors BN model is built based on conditional likelihoods of the factors and sub-factors identified in the perspective of circularity adoption in India's textile and clothing supply chain. The flow of the study performed to develop risk mitigation strategies and the causal and conditional relationship between various factors of risks of circularity adoption in the textile supply chain is shown in Fig. 1.

To evaluate the management effectiveness of this research effort, we considered a textile company focused on implementing CSC initiatives and finding strategies to reduce the risks associated with implementing CSC practices in each organisation. SAP-LAP and IRP methods were used to evaluate the management efficacy of a study effort; in the next section, the specifics of the SAP-LAP framework are presented.

# 4 SAP-LAP application 

The Risks in the close looping of TSCs are a critical factor for enterprises, as the failure to control risks would jeopardise efficiency and economic advantages. There is a need to provide a framework for understanding risk reduction measures. Creating the framework would enable management to reduce risks associated with implementing CSC activities. Sushil (2001) proposed the SAP-LAP process, a comprehensive and adaptable management strategy that logically supports the development of such managerial structures. This section has developed the conceptual SAP-LAP model for developing the mitigation strategies for the risks in adopting CSC initiatives in textile industries. Figure 2 shows a theoretical "SAP-LAP model" for developing risk mitigation strategies. The SAP-LAP paradigm is a versatile management approach with three critical components from any good management standpoint: situations, actors, and processes. The component 'process' or 'processes' refers to the restoration method used to replicate the problem. LAP is the result of the interface and synthesis of the SAP. Managers can act and take steps based on their concerns to improve the system's overall operation.

![img-0.jpeg](img-0.jpeg)

Fig. 1 Flow of the study

![img-1.jpeg](img-1.jpeg)

Fig. 2 A Theoretical "SAP-LAP model" for developing risk mitigation strategies (Sushil, 2001)

# 4.1 The situations 

Attainment of the situation for developing risk mitigation approaches for csc adoption in the textile industries-Because of many risks/uncertain elements, CSCs networks in the textile sector are getting increasingly complicated. This article focuses on establishing a broad, adaptable "SAP-LAP-based flexible model" to construct risk extenuation measures for CSC adoption in India's textile businesses. Furthermore, numerous variables impact the circulation or looping of the SC, such as political influence, increasing environmental deterioration, heavy waste generation, the unsustainable nature of the supply chain, consumer demand, globalisation, and so on. These variables are decided and confirmed by the experts and treated in situations such as S1, S2, S3, S4, S5, and S6 (Table 3).

What is trendy now, and what is anticipated to happen?-In the twenty-first century, there is still a shortage of debate on the risks and disruptions in SC for transitioning through CSC activities in the context of the textile sector. Risk concerns and mitigation techniques for implementing CSCs in the textile industries must be established and understood to minimise, prevent, and manage risks.

### 4.2 The actors

A viewpoint on building risk Mitigation tactics for CSC adoption in the textile industries-Developing risk mitigation techniques necessitates a collaborative and integrative effort by all players intricated in the CSC implementation. According to experts, the key actors involved in and contributing to developing risk extenuation strategies for CSC adoption in the textile industries are top management, manufacturers, suppliers, customers, employees, system integrators and consultancy firms.

The parts and capabilities unveiled by the actors in the supply chain-The planners and managers must be competent in considering the necessary circumstances in Closed Looping the SCs for a firm to succeed. Customers should also be heavily involved in developing and managing risk mitigation approaches. Managers must convey risks to senior management. Their obligation and permission are essential for developing and instigating risk mitigation measures.

In Which Areas is the "Freedom of Choice" Obtainable-Businesses can decide whether to adopt CSC. The responsibilities and degree of engagement of the players and the beliefs of management may indicate the assortment of "freedom of choice". The ability and methods of the dealers to risk problems in CSC adoption support organisers in making judgments on their selection. The choice to include clients and contractors is solely at the discretion of the management. The selected competence in the sector determines senior management's freedom of choice. In the event of a fault, departures from CSC adoption in textile industries' risk mitigation techniques can occur. These variables are decided and confirmed by the experts and treated as the Actors as A1, A2, A3, A4, A5, A6, A7, A8, and A9 (Table 3).

### 4.3 The processes

Risk Managing Approach and Need of it in CSC Adoption-The mitigation of risks is a strategy that focuses on potential occurrences and how to manage them if they occur. It is serious about implementing a specific approach to minimise these risks in the scene of CSC adoption, and techniques highlighting hazards are shown in Fig. 3. As a result, it is desirable

Table 3 The 'SAP-LAP' Framework variables for edifice risks mitigation tactics in CSC Adoption in Textile industries


to concentrate on the likelihood of risk occurrence at any specified time. It can be exercised in a route that decreases the possibility of every risk occurrence.

The fortification plan addresses steps to safeguard a CSC network. This technique cannot eliminate dangers, but it can assist in reducing user interval. Response techniques can shorten the time required to fix the MTTR. It indicates that the sooner a company begins to solve an

![img-2.jpeg](img-2.jpeg)

Fig. 3 A conceptual schematisation of risk mitigation tactics for CSC in Textile Industries
issue, the sooner it will be able to recover. This strategy is classified into numerous methods for risk reduction in CSC adoption.

Regarding risk mitigation recovery measures, most operational management research has concentrated on pronouncements before a risk incident. Though stressing readiness for risk events is equally critical, firms should not neglect chances for minimising the impact of Supply Chain disruptions.

Technique for Mitigating Risks in CSC-

- Risk mitigation has become increasingly crucial in CSC adoption to understand the influence of risks on enterprises. Administrators should define well-recognised mitigation methods or stage series while dealing with risk concerns. Following consultation with specialists, the following recommendations have been made in this study.
- It is anticipated to identify the risks associated with adopting a CSC by a textile production organisation, which would make available a general understanding of unanticipated events in its surroundings.
- Risks assessment in the following approach entails assigning possibility standards to several risk-bearing occurrences in the CSC adoption system and restructuring the implications of the detected risk events.
- Following the risk assessment, steps must be suggested to reduce a specific CSC adoption risk. An organisation's strategy for risk mitigation efforts is determined by its capacity and the surrounding environment. Risk mitigation activities take direct action on predetermined risks (i.e., proactive measures) or the gridlock scenario following risk incidents (i.e., reactive measures).
- The next phase is to monitor risk concerns, which entails continual system supervision to detect and recognise risks and disruptions in the SC network as it moves through CSC activities.

# 4.4 The learning 

Problems in developing Risk Extenuation Strategies for CSC Adoption in Textile Industries-The study plots the internal and external environment and technological and operational fluctuations in forward and converses operations in the CSC network. Firms must implement management mitigation methods to remain competitive in a fluctuating business environment. Risk mitigation practices must be developed to guarantee that CSC networks acclimatise and retort in real-time in today's volatile business climate.

Problems Associated with the Actors-Practical cooperative activities among suppliers, Supply Chain managers, customers, and the top management are essential concerns related to the players in CSC adoption. Managers must maintain a rising advantage in recognising unpredictable business situations, technologies, process changes, and environmental effects. Identification of freedom of choice areas for future cooperation is another significant concern. Managers must maintain a rising advantage in recognising unpredictable business situations, scientific process changes, and environmental impacts. The skill of managers and planners in understanding uncertain and unpredictable occurrences and the likelihood of an event is a significant concern. Attention is meant to the current risk extenuation measures to examine suppliers' competencies in the environmental dimension.

Problems Associated with Processes of Developing Risk Mitigation Tactics in CSC Adoption. -Organisational, social, technological, and operational issues must be discussed to develop risk mitigation approaches for CSC adoption in the textile industry. Two significant issues in developing risk mitigation tactics for CSC are investigating existing conditions on risk mitigation or management approaches, the methodology for execution, and defining the clusters of the risk mitigation strategies for a business. Critical issues associated with the risk management process include collaborating business strategies with countermeasures.

### 4.5 Actions

Actions can/should/ought to be completed to Alter the Situation-A company's total expenses may be minimal in a stable environment. Still, the situation may differ in an unpredictable climate. This segment suggests features for changing and improving the state of building risk mitigation measures in CSC adoption. The creation of tactics differs amongst firms and is critical in determining an appropriate risk-mitigation approach.

The Actions that can be taken to Transform the Actors-Special seminars and training programs should be organised by top-level management to keep managers up to speed on technical, environmental, and operational developments. Any enterprise must recognise the significance of the players in developing their enterprise goals and risk-managing ecosystem for CSC adoption. To close the CSC loop, managers must thoroughly understand the hazards and risks associated with sourcing, manufacturing, dispersal, reverse logistics, and end-user activities. Furthermore, they should be aware of the effects of risks and the significance of risk reduction in CSC adoption. Consumers, suppliers, and customers should be included in choices on risk reduction techniques developed to meet the various standards of CSC. Coherence between consumer and supplier provisions and management planning is required for creating risk-associated decisions in CSC adoption in textile businesses.

Actions ought to be taken to Alter the Process-Administrators of Circularity adoption must address weaknesses in CSC adoption. For example, a strong relationship between businesses and their contractors may help to increase the risk reduction strategy. The risk

extenuation plans process may also be aided by considering the impact of technological revolutions and consumer preferences and expectations.

# 4.6 The performance 

Impacts on the situations-CSC's adoption of risk mitigation methods in CSC adoption will improve its complete performance. The start of risk consideration would equip administrators with a foundation for dealing with present and necessary risk mitigation measures. This will create an optimal conversation between environmental changes and risk reduction techniques.

The impacts on the actor (s) performance-Developing risk mitigation approaches framework in CSC adoption, as per the actor, may increase customer and supplier loyalty. SC planners and policymakers may develop effective mitigation methods to control risks by involving users appropriately. As a result, top-level management will achieve CSC implementation in the textile sector's commercial success.

The impacts on process performances-Administrative CSC adoption may be achieved when a risk extenuation strategy framework is developed and instigated. Organisations may readily manage the implications of a risk incident by using risk mitigation methods. Information and resources will stream freely and smoothly in all purposeful areas of the CSC adoption.

However, the SAP-LAP-based flexible decision-making model falls short when comprehending the relationships between the listed variables. This research employs the IRP decision-making approach to address this; specifics are provided in the following section of the study.

## 5 Application of interpretive ranking process

The IRP is a revolutionary ranking approach that draws on the strengths of intuitive and logical decision-making processes. The IRP as a flexible judgment strategy was introduced and applied by Sushil (2009). This method expands on the merits of a pair-wise comparison method (Badhotiya et al., 2022a, 2022b) and reduces perceptive fatigue. It leverages an interpretative matrix and associated interpretation comparisons within the matrix (Haleem et al., 2012). This section has developed an interpretation of the interactions amongst the 'SAP-LAP' Model Variables. The technique overcomes the problem of the spontaneous decision-making process, like SAP-LAP. The following are the specifics of the IRP procedure that was used in this study:

Step 1: Establishment of a dual set of variables, one to be ranked regarding the other:
Created on the "SAP-LAP" paradigm, this work investigates the task of the actors in the processes and the impact of the actions happening on the performances. Table 3 shows the many factors discovered in the 'SAP-LAP' model. To explain the remaining phases of the IRP, the ranking of 'Actors' concerning 'Processes' is explored.

## Step 2: Deriving the cross-interaction matrix among the dual sets of variables:

The relationship among the variables discovered in the study, namely, actor vs. process and actions vs. performance, is represented by a cross-collaboration matrix. In that matrix, the character ' 1 ' signifies the existence of a link between the two variables, while character ' 0 ' represents its nonappearance. Expert advice was used in this case. Furthermore, a binary matrix of cross-interaction of variables (i.e., actors w.r.t processes as well as actions w.r.t

performances) is established and given in Tables 4(a) and 5(a) to achieve a building risk mitigation method in the CSC adoption.

Step 3: The Conversion of the cross-interface-matrix to the interpretive matrix:
The binary matrix is now turned into an interpretative matrix by interpreting all possible relations, including an entry of ' 1 ' in indirect connection (Sushil, 2009). For example, (actor A1 and Process P2) are translated as 'Knowledge of Suppliers and dedication will be critical from the standpoint of the protection strategy.' Tables 4 b and 5 b offer a comprehensive crossinterpretive matrix (i.e., actor versus process and action versus performance) for developing a risk extenuation approach in the CSC.

Step 4: Changing the interpretative matrix to informational reasoning (that is, Learning Base) of the pair-wise assessments and dominance interfaces-matrix:

This was accomplished by judging the dominance of one encounter over another. This was accomplished with the assistance of professionals. It presents the interpretative lucidity of Knowledge Base variables (like actor vs. process and action vs. performance) to achieve a risk extenuation policy and principles in the CSC-adopted business. Furthermore, the variables in the informational matrix were compared in pairs concerning the mentioned variables. For example, actor 'A1' is analogised to actor 'A2' in terms of multiple processes such as P1 (prevention strategy), 'P2' (protection strategy), 'P3' (responsive approach), and 'P4' (recovery strategy), and the interpretative sagacity of 'A1' (suppliers) and 'A2' (Textile waste collectors)'s prevailing interaction concerning their reference variables is recorded. Adoption is established and displayed in Tables 6 and 7 based on the dominant interface for variables (actor versus process and action versus performance) towards constructing risk extenuation strategy and ethos in the CSC.

Step 5: Obtaining the ranking and interpretation of rank positions in the form of dominations of the summation of interactions:

A domination matrix represents dominant interactions. It tracks how often one rankings variable dominates or some other variable dominates. The net of the dominance for a ranked team variable, such as action, is calculated as dominated subtracted by dominating ( $\mathrm{D}-\mathrm{B}$ ), here ' D ' signifies the overall number of instances in which these factor(s) influence another dependent factor(s), and B illustrates an over-all number of the circumstances that all further ranking variables underestimate a specific ranking variable. The rank of the variable with the most evident net positive dominance has been assigned as the number ' 1 ', followed by the next lowest, and so on. Because other factors dominate them, the variables with the uppermost substantial net dominance negative will be ranked the lower. For example, actor A4, i.e., Top management, has the most prominent positive net dominance and ranks first. As a result, Table 8 and Table 9 establish and offer a ranking position of the factors (like actor versus process and action versus performance) toward building a risk extenuation plan and ethos in the CSC implementation. If more than one variable has an equal negative dominance score, the ranking position is determined by the numeral of circumstances it dominates (Sushil, 2009). In such a situation, the variables with the highest number of points will be ranked higher. For example, if action (task) T2 (Building technological management) and T3 (Provision and engagement of Supply Chain managers) have identical negative net dominance, but task T2 has a more significant number of cases actuality dominated than task T3; hence task T2 is ranked as II (Table 9).

# Step 6: Confirmation of ranks accordingly decided: 

In this study, positions produced by the domination matrix were verified. This is accomplished by using cross-validation in the study of the domination matrix.

Table 4 Cross interface matrix for actors vs. processes


Table 5 The Cross-interaction-matrix for actions versus performances


Table 6 The Dominating relations matrix (actor w.r.t. process)


Table 7 The Dominating relations matrix (Tasks w.r.t. performances Results)


Step 7: Representation of the attained ranking graphically in the system of an interpretive ranking approach:

An interpretative ranking model shows the concluding positions of the ranking variables. The arrows in the figure denote the reference variable, which is an actual ranking of the variable that dominates the other ranked position variable. Additionally, the statistics dominating and actuality dominated for each variable are indicated in the brackets. It will help interpret how Actors and Actions influence respective Processes and Performances. The IRP model in Fig. 5 shows that actor A4 (i.e., Top management) has the peak rank. This shows that senior management involvement is critical for any industry seeking to enhance CSC processes and performance in the textile sectors of India. The remaining actors are listed in the following order: A5 (Manufacturers) [A2 (Textile waste collectors)] [A3 (Supply chain managers) [A9 (System Integrators)] and so on. The rank from A4 to A6 here displays that A4 dominates other actors, as in the dominance matrix for all the processes (i.e., P1, P2, P3, and P4). The figures dominating all actors and tasks are summarised within brackets. For instance, for A4, the dominant and dominant numbers are displayed as $(20,7)$.

Figures 4 and 5 depict the collaborative ranking positions of the variables (like actor versus process and action versus performance) used to develop a risk extenuation strategy and culture of a CSC.

Step 8: Interpretation of the rankings and use of it as the base for proposing actions:
The actors versus processes position ranking model analyses various players' roles in premeditated processes. That also elucidates the dominant functions performed by distinct players that will be necessary for businesses implementing the actors-cantered tactic to improve the efficacy of these processes. Correspondingly, the Actions versus Performances ranking model assesses the impact of significant tactical activities on performance. That will help create strategic priorities for improving performance to the considerable extent of risk extenuation practices in the context of CSC adoption in the textile and apparel sectors.

In the next section of the study Bayesian Networks (BN) model was used to establish the mutual causal relationship among the variables by utilising the concept of conditional probability. The risk mitigation actions derived from the IRP model are further used in the BN model to analyse the causal relationship among the risks and risk factors and proposed risk-minimising measures.

Table 8: Domination matrix (Ranking of the actor for the process)


${ }^{a}$ Number of cases to be dominated

Table 9 Dominance matrix (Ranking of action for performance)


${ }^{\mathrm{a}}$ Number of cases to be dominated

# 6 Bayesian networks 

The Bayes theorem underpins Bayes networks, allowing for generating outcomes using historical data and expert views. BN has been applied in various domains, particularly risk and statistical modelling (Çikmak \& Ungan, 2022). There are numerous benefits to using BN; first, it stipulates a framework for exhibiting uncertainties; it aids in visualising the interaction of variables by offering a graphical illustration of the model; it is simple to develop probabilistic inferences due to efficient software; sensitivity analyses can be accomplished; it can be investigated in different scenarios; and together forward and backward dissemination scrutiny (cause and effect plus effect and cause) can be executed (Sharma \& Routroy, 2016).

BN or BBN are focussed acyclic networks in that variables signify by the nodes. The arrows in the network reflect immediate causal impacts between the connected nodes, and the assets of these consequences are stated in terms of conditional probabilities. These networks are acyclic, as the arrows don't create a circle or loop that starts and ends at the same node. (Qazi et al., 2016).

Figure 6 shows an example of a BN with five nodes. The nodes at which the arrows point is called 'child' nodes. Child nodes are X3, X4, and X5. The arrows originating from the nodes are termed 'parent' nodes. X1 and X2 are the parents of X3 and X4, respectively, while X4 is the parent of X5. Nodes with no parents are referred to as 'root' nodes, whereas nodes with no children are called 'leaf' nodes. As a result, nodes X1 and X2 are both parent and root nodes. Likewise, the X5 node in Fig. 6 is a child as well as a leaf node.

A BN has both qualitative and quantitative components. Variables (nodes) that exhibit conditional dependence connections with targeted arrows are shown as nodes in the qualitative section. The quantitative section expresses dependency connections as the values of conditional probabilities for each variable in the network (Sharma \& Routroy, 2016). The probability distribution of child nodes is conditional, whereas the probability distribution of root nodes is marginal. The marginal probability values $\mathrm{P}(\mathrm{X} 1)$ and $\mathrm{P}(\mathrm{X} 2)$, as well as the conditional probabilities $\mathrm{P}(\mathrm{X} 3 \mid \mathrm{X} 1), \mathrm{P}(\mathrm{X} 4 \mid \mathrm{X} 1, \mathrm{X} 2)$, and $\mathrm{P}(\mathrm{X} 5 \mid \mathrm{X} 4)$, should be determined in the figure.

Variables in a BN model might be either discrete or continuous. The shared probability values for all nodes are determined by the multiplication of the values of conditional probabilities for each node. The combined probability for the case in Fig. 6 is calculated as Eq. 1:

![img-3.jpeg](img-3.jpeg)

Fig. 4 Ranking model Constructed by using IRP (Actor vs. Process)

![img-4.jpeg](img-4.jpeg)

Fig. 5 Ranking model Constructed by using IRP (Tasks vs. Results)

Fig. 6 Bayesian Network Example with five Nodes (variables)
![img-5.jpeg](img-5.jpeg)

$$
P(X 1, X 2, X 3, X 4, X 5)=P(X 1) P(X 2) P(X 3 \mid X 1) P(X 4 \mid X 1, X 2) P(X 5 \mid X 4)
$$

Assume a Bayesian network has n variables X1, X2...., Xn. The network's jointprobability distribution is given by the product of the conditional probability distributions of the network variables, as shown in Eq. 2.

$$
P(\mathrm{X} 1, \mathrm{X} 2, \ldots, \mathrm{Xn})=\prod_{i=1}^{n} P(X \mid \text { parent }(X))
$$

When a new signal about variables or a variable set's probable scenarios is gained from external causes, the conditional probability values of the variables may be determined by ostracising the outcome. If the fresh indication is presented, the chance of occurrences happening can be computed as Eq. 3:

$$
P(Q \mid R)=\frac{P(Q, R)}{P(R)}
$$

Here Q is a universal set of variables A1, A2......, An.
The probabilities generated from the model are computed after establishing a Bayesian network from prior knowledge. Calculating the relevant likelihood in each model is called 'probabilistic inference.'

After identifying fresh evidence for additional variables, the calculation process for the subsequently combined probability values of the associated variables is called probabilistic inference. The combined probability distribution of variable deviations changes with each additional information learned about the variables (Badhotiya et al., 2022a). The inability to do manual calculations in full actual models with numerous states precluded employing the BN's approach to decision-making and risk concerns. As a result, several software solutions with efficient algorithms were created. These applications help to construct network models as well as make probabilistic judgments. The GeNIe 4.0 (academic version) was employed in this study to build the network and execution of analysis.

# 6.1 The data collection 

A thorough exploration of the literature was done to classify CSC adoption risks and subfactors in the context of the Textile and Clothing Industry (Table 1) discussed in the literature review section of the study. As a result of this study, many CSC risks were revealed. Because subjecting all these risks to expert evaluation is challenging, the semi-structured interview is conducted to collect data from experts in the textile supply chain. A group of professionals, including senior managers and employees from various textile production establishments, advisors, academicians, and consultants, participated in the process. About six experts from different textile businesses were interviewed in the process. Afterwards, participants were requested to give the possible values of the risks and mitigation strategies. In the BN model, these probabilities are used as conditional probabilities further constructed in networks using a graphical technique. The textile business professionals were initially questioned about the risks and risks found by the literature survey and relevant risk mitigation techniques.

### 6.2 Construction of network structure

Some risk variables and mitigation measures were deleted from the research based on the advice of experts from the industry, while a few others were included. The Construction of the network was done by the opinions of industry professionals (Fig. 7).

![img-6.jpeg](img-6.jpeg)

Fig. 7 Proposed Bayesian Network Model

# 6.2.1 Defining the state terminologies of the variables 

In BN models, variables should be stated as a set of probabilities. The model determined state expressions to explain the causality among factors with conditional probabilities. The different states of variables can be termed as "low/medium/high," "low/high," "yes/no," or "true/false" using the Boolean approach. Creating conditional probability tables becomes increasingly difficult as the quantity of parent variables and states in a BN model grows. To avoid the complexity of the model, the number of states in binary expressions was maintained as minimal as possible. After the assessments by experts, it was decided that it is required to present a few variables with more than two states.

### 6.2.2 Conditional probability determination for the model

It is necessary to elicit probability between variables because BN is based on the concept of conditional probabilities generated using expert opinions in this study. The experts enquired about the marginal and conditional probability values. This was accomplished using a questionnaire. The arithmetic averages of the 20 surveys were used to compute the conditional probabilities of the variables. Experts may struggle to determine multi-combination conditional probability values since they are time-consuming and complicated. Kim and Pearl (1983) proposed a technique to solve this difficulty. In any Bayesian network, if any child node X contains two parent nodes, Y and Z , then the conditional probability of node X is linked to Y and Z can be estimated using Eq. 4:

$$
P(X \mid Y, Z)=\alpha P(X \mid Y) P(X \mid Z)
$$

![img-7.jpeg](img-7.jpeg)

Fig. 8 Bayesian Model Results

Here, $\alpha$ is a normalisation factor used to stabilise and approximate the cumulative probability at each node. This formula is generalised for use after getting the probability of each parent node fitting in with its child nodes, especially for many parent nodes. The values are multiplied and normalised using Eq. 4 to compute all the appropriate combinations of all the parent nodes.

$$
P(A \mid X 2, X 3 \ldots, X n)=\alpha P(A \mid X 1) P(A \mid X 2) \ldots \ldots, P(A \mid X n)
$$

Using Eq. 5, the variables influencing the risks and various risk mitigation measures' conditional probabilities were determined, and the tables were generated for each node.

The probability is calculated using conditional probabilities from $\mathrm{X} 1 \ldots \mathrm{Xn}$. The constructed Bayesian networks with their results are shown in Fig. 8. The result from the constructed model shows that the financial and quality risks have the maximum probability at maximum and medium states. This shows the importance of risk mitigation measures for circularity adoption. The subsequent section discusses the results and implications for this study's managers, policymakers, and researchers.

# 7 Discussions and implications 

### 7.1 Discussions

The proposed conceptual and flexible decision-making model aids in developing a risk mitigation approach for the CSC in the textile business setting, with considerations for 'situation-actors-process' and 'learning-actions-performance'. The framework for risk relief

approaches includes methods for handling turbulent or transient situations while maintaining the closed-loop supply chain network. The SAP-LAP paradigm is better investigated to evaluate Actors and Tasks concerning Process and Performance. The results from IRP methods show that the involvement of top managers is crucial for developing risk mitigation measures (Mangla et al., 2014). The developed BN model in the study revealed causal relationships among various risk factors. The study demonstrated that quality and financial risks indicate the maximum probability values maximum $=72 \%$ and $53 \%$ (Çikmak \& Ungan, 2022). The environmental risk's likelihood value is $32 \%$ at maximum and $68 \%$ at minimum. The operational risk's maximum probability is $46 \%$, medium at $33 \%$, while the low probability is only 20\% (Sharma \& Routroy, 2016). 'Environmental' and 'Tactical' risks have the lowermost probabilities at a maximum of $32 \%$ and $48 \%$, respectively (Qazi et al., 2016). According to the results, elements related to environmental risk are less expected to appear, and response activities will minimise its effects. Except for the 'Building Top Management' action, the high probability of execution for all risk-reducing activities is greater than $50 \%$. With a $58 \%$ chance, the most likely action is a 'Strong waste collecting system.' 'Involvement of supply chain management and flexible procurement' comes second with a $57 \%$ chance. 'Employee Training and Education are ranked third, with a likelihood of 56\% (Yusriza et al., 2022). Other activities, such as 'organisational plans and contingencies,' rated fourth with a likelihood of $53 \%$, 'assurance from top management,' ranked fifth with a probability of $52 \%$, and 'building technological management,' ranked sixth with a probability of $45 \%$. Managers and policymakers are essential in managing circularity in the supply chain; organisations will benefit from expanding their knowledge. This study assures several repercussions for managers because of the unique, intuitive, adaptable, and interpretive decision-making tactics, which are as follows:

The conceptually flexible proposed decision-making approach aids in developing risk mitigation stratagems for the CSC in the textile business setting, with considerations for "situation-actors-process" and "learning-actions-performance." The framework for risk extenuation tactics includes methods for handling tempestuous or transient situations while maintaining the Supply Chain network closed-looped. The "SAP-LAP" paradigm is further investigated to assess "actors and actions" in connection to "processes and performances," correspondingly. Planners and managers are essential in managing circularity in the supply chain; organisations will benefit from expanding their knowledge. This study provides the following managerial implications due to the flexible, unique, intuitive, and informative nature of this decision-making method:

# 7.2 Implications 

To assist managers and executives, a conceptual "SAP-LAP" based framework is presented for risk extenuation methods in this study in developing an awareness of the risks related to conflict of raw resources and accompanying CSC employment in textile firms. Two proactive and reactive techniques have been offered on the "SAP-LAP-based" model created to manage risks in the CSC in the textile sectors to overcome the risks. Any organisation, association, or company cannot afford to use all tactics. The administrators must comprehend in cooperation with the values and limitations of these approaches and their suitability for the company. It is necessary for managers to constantly evaluate the importance and engagement of the suppliers, contractors, different stakeholders, customers, and top-level management while developing mitigating risk actions for circularity adoption. The IRP approach was used to identify the ranks of actors and actions. It would define the dominant roles performed by

various players, which would be necessary for companies implementing an actor-centred method to improve the efficacy of the discussed process. It will be conducive to establishing premeditated priorities for improving important recital indicators. Using IRP, managers may better grasp the relationships among the factors based on the "SAP-LAP-based" flexible managerial framework. The constructed BN model analyses all involved risks and factors and assists the SC managers and top management with a quantified causal relationship. The BN approach used in the study provides valuable insights for managers into CSC adoption risk management. The BNs can perform various what-if analyses in complex network structure modelling while building mitigation strategies for circularity adoption risks. The BN model assists policymakers and top management in transitioning towards circular practices in textile production processes.

# 8 Conclusions 

This study attempts to build a flexible and holistic decision-making framework for evaluating risk mitigation approaches in the context of CSC adoption in textile businesses. This framework would help organisations implement CSC practises and improve ecologicaleconomic performance, customer satisfaction, etc. The study proposes an all-inclusive adaptable "SAP-LAP" and then an IRP-based methodology to decrease the consequences of risks in CSC adoption in textile sectors. The IRP is an innovative ranking approach that takes advantage of the assets of both intuitive and logical decision-making processes. It starts with an interpretive matrix and compares interpretations in the matrix in pairs. An attempt was made to build an SAP-LAP-based comprehensive adaptable framework for examining CSC adoption risk mitigation options. The causal relationship between various risks and risks factor is crucial for the implementation of Risk mitigation strategies. The BN method analyses the mutual causal relationship among different risks and identifies actions to lessen the risks. The IRP approach, which examines the interactions within the SAP-LAP modelbased variables, is also used to develop the DAGs. According to the suggested SAP-LAP model, while developing a flexible CSC adoption risk mitigation plan for mitigating various circularity adoption risks, the players' perspectives, including those of the final manipulators, SC managers, top management, and suppliers, should be addressed.

Furthermore, an interactive decision-making process is employed to apprehend the interactions between the different factors of the "SAP-LAP" based model: The "Actor versus Process" and "Action versus Performance." Using the IRP technique allows administrators to confine the other limits of the SAP-LAP; it is an instinctive managerial strategy. Conferring to the IRP method and its findings, the top roles of the top level of management as an actor and the obligation of the top level of control as actions are the most significant in developing and executing CSC adoption risk mitigation measures. The decision to pick and apply the stated risk mitigation techniques is heavily influenced by the supply chain managers' and top-level management's situation and preferences. Furthermore, the proposed adaptable framework may assist supply chain experts and managers analyse current risk mitigation measures in CSC adoption in the textile setting and various risks to plot further changes to make them more abundant and vigorous. Based on conditional probabilities, a BN model was anticipated, which provides risk and risk relief strategies probabilities and can be revised as more information appears. This study puts the groundwork for forthcoming studies. The methodology suggested in this study may be used in numerous sectors of India's textile and

apparel industries to enhance the overall performance of circularity adoption. The different sectors might also be considered in future studies.

One of the limitations of this model is that the causality between risk and mitigation strategies' effect could not be reflected. Sensitivity analysis of the BN-Model can be performed in further studies by observing data from various textile sectors. Sensitivity analysis in the BN model can be performed in further studies by observing data from various textile sectors. Models considering the same can be developed in future studies. The knowledge and the experience are solely used to create the model. A case study technique might be employed in future investigations to narrow down the findings of the research work. Identifying and deciding on the risks of CSC adoption might be difficult. Because this study depends on human views, future studies might use various methods to eliminate humanoid subjectivity.

# Declarations 

Conflict of interest Authors declare that we have no conflict of interest.
Ethical approval All procedures performed in studies involving human participants were in accordance with the ethical standards of the institutional and/or national research committee and with the 1964 Helsinki Declaration and its later amendments or comparable ethical standards.

Informed consent Informed consent was obtained from all individual participants included in the study.
