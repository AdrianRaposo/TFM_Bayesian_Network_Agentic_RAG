# Towards a knowledge-based approach for effective decision making in railway safety 

Garcia-Perez, A. , Shaikh, S.A. , Kalutarage, H. and Jahantab, M. Author post-print (accepted) deposited in CURVE April 2015*

Original citation \& hyperlink:
Garcia-Perez, A. , Shaikh, S.A. , Kalutarage, H. and Jahantab, M. (2015) Towards a knowledgebased approach for effective decision making in railway safety. Journal of Knowledge Management, volume 19 (3): 641-659.
http://dx.doi.org/10.1108/JKM-02-2015-0078
Publisher statement: This article is (c) Emerald Group Publishing and permission has been granted for this version to appear here http://curve.coventry.ac.uk/open/items/40354d81-65c4-435a-856f-9bbfdaeedeb0/1/. Emerald does not grant permission for this article to be further copied/distributed or hosted elsewhere without the express permission from Emerald Group Publishing Limited.

Copyright © and Moral Rights are retained by the author(s) and/ or other copyright owners. A copy can be downloaded for personal non-commercial research or study, without prior permission or charge. This item cannot be reproduced or quoted extensively from without first obtaining permission in writing from the copyright holder(s). The content must not be changed in any way or sold commercially in any format or medium without the formal permission of the copyright holders.

This document is the author's post-print version, incorporating any revisions agreed during the peer-review process. Some differences between the published version and this version may remain and you are advised to consult the published version if you wish to cite from it.
*Re-uploaded with updated cover sheet August 2015.

CURVE is the Institutional Repository for Coventry University
http://curve.coventry.ac.uk/open

# Title Page 

Title: Towards a knowledge-based approach for effective decision making in railway safety
Authors: Alexeis Garcia-Perez, Siraj A. Shaikh, Harsha K. Kalutarage, Mahsa Jahantab Coventry University, UK
ab1258@coventry.ac.uk

## Structured Abstract:

## Purpose

This paper contributes towards understanding how safety knowledge can be elicited from railway experts for the purposes of supporting effective decision making.

## Design/methodology/approach

A consortium of safety experts from across the British railway industry is formed. Collaborative modelling of the knowledge domain is used as an approach to the elicitation of safety knowledge from experts. From this a series of knowledge models is derived to inform decision making. This is achieved by using Bayesian networks as a knowledge modelling scheme underpinning a safety prognosis tool to serve meaningful prognostics information and visualise such information to predict safety violations.

## Findings

Collaborative modelling of safety-critical knowledge is a valid approach to knowledge elicitation and its sharing across the railway industry. This approach overcomes some of the key limitations of existing approaches to knowledge elicitation. Such models become an effective tool for prediction of safety cases by using railway data. This is demonstrated using Passenger-Train Interaction safety data.

## Practical implications

This study contributes to practice in two main directions: by documenting an effective approach to knowledge elicitation and knowledge sharing, while also helping the transport industry to understand safety.

## Social implications

By supporting the railway industry in their efforts to understand safety this research has the potential to benefit railway passengers, staff and communities in general, which is a priority for the transport sector.

## Originality/value

This research applies a knowledge elicitation approach to understanding safety based on collaborative modelling, which is a novel approach in the context of transport.

## Keywords:

Knowledge elicitation, Knowledge transfer, Knowledge modelling, Rail transport, Railway Safety.
Article Classification: Research Paper

## Acknowledgments:

This research has been funded by the UK Railway Safety and Standards Board (RSSB) through the Rail Research UK Association (RRUKA). This work has benefited from contributions from several organisations including Network Rail, London Underground, Transport for London, First Class Partnerships, SMT (Staff Management Tools) Ltd, TRE Ltd, TIBCO Software Ltd. We are grateful for their valuable time and input.

# Towards a knowledge-based approach for effective decision making in railway safety 

Alexeis Garcia-Perez, Siraj A. Shaikh, Harsha K. Kalutarage, Mahsa Jahantab

## 1. Introduction

Railways increasingly underpin the public transport in most modern economies. Safety therefore remains a priority for train and infrastructure operators; recent incidents only serve to highlight this further (Evans, 2011). With increasing digitisation of the railways the opportunities to collect data increase. Such digitisation manifests itself in terms of signalling and control, communications, sensing, comfort and passenger interaction. Continuous data collection provides the sector the ability to more effectively monitor for safety-related incidents, and ultimately provide better condition monitoring, low-cost maintenance and increased uptime.

With availability of data, collected at such scale, diversely across the infrastructure comes the need for effective knowledge management to ensure that an operationally consistent view of such a data (in terms of models and the inferences derived from them) is available to the industry.

An additional motivation exists in terms of the need for cross-border rail services, which is increasing and particularly relevant in the European context. The need for tighter integration of safety systems for railways therefore has led to standards such as the European Train Control System (ETCS) (Europa, 1996) designed for control, signalling and protection. Such standards rely on data, communication and electronic control at various levels. The need for better modelling of data for effective safety, while an increase in capacity and efficiency, is ever so more critical. However the focus of our effort is beyond the safety of the ETCS software; we are concerned with data at the systems level and do not concern ourselves with specific such standards or the safety-critical nature of the software that underlies it (Feuser et al., 2014; Yoshinao, 2012). Any knowledge derived for safety purposes however may encapsulate data from additional sources.

The diverse nature of data collected, across various parts of the sector and under different ownership raises difficult questions on how such data could be used for effective decision making. Of particular interest to us are data models that allow us to predict likelihoods of safety incidents (Marsh and Bearfield, 2004; Kyriakidis et al., 2012; Tretten and Karim, 2014). Implicit in safety-related decision making is domain-specific knowledge that is difficult to derive, build and model for decision making. One source of such knowledge are professionals (from safety engineers to signalling operators) in the domain who bring with them sources of implicit knowledge and point to explicit repositories. This is one important source of knowledge we make use of in the pursuit of this work.

Elicitation of safety-critical knowledge from railway experts therefore becomes an imperative if such knowledge is to be effectively shared, managed and used for related decision making. In this paper we exercise a novel approach to knowledge elicitation and transfer from domain experts (reference).

The aim of this paper is to understand how such safety knowledge can be elicited from railway experts for the purposes of supporting effective decision making. It demonstrates a critical principle of using a knowledge management approach to add value to raw data collection for the sector providing timely and valuable knowledge. The three main questions this paper addresses are:

- How do we capture safety-critical knowledge from domain experts?
- Could a facilitated knowledge elicitation approach be used to model knowledge directly from experts?
- How do we use such knowledge for effective decision making?


### 1.1. Objectives and Methodology

To address the stated aim of this paper we set out to achieve two main objectives. The first objective is to elicit safety-related knowledge from railway experts. This has been achieved through a structured

process that concluded by bringing a group of railway safety experts together in a workshop to provide an agreed view on the growing relationship between data and safety.

Building up on the above, the second objective of this research was to validate the elicited knowledge by using it for effective safety decision making. This validation is achieved by developing a software tool that can use a safety model of railways, defined as a Bayesian network, to analyse data available for the purpose of predicting safety-related incidents. The effectiveness of the software tool will be used to assess the validity of the elicited knowledge which in turn would point to the value of the knowledge elicitation method previously implemented.

This approach to knowledge transfer and its validation involves four key stages as shown in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Key stages of the knowledge elicitation and transfer mechanism.
Our choice of methodology for the elicitation of knowledge from experts is deliberate. Originally developed in a collaboration with a major engineering organisation, collaborative development of

knowledge representations was found to be a novel approach to knowledge elicitation, which has been successfully applied in a number of domains.

# 1.2 The rationale behind our methodology: 

The notion of knowledge elicitation essentially represents methods and tools that make the arduous task of capturing and validating an expert's knowledge as efficient and effective as possible. Experts can describe systems in a variety of ways and with different levels of abstraction. One way is by building up sets of metadata which can be arranged to form models which describe a system from a particular perspective, that is, safety in this case (Chen et al. 2003).

The group elicitation (collaborative modelling) exercise is supplemented by additional input in terms of critical factors and data models that the domain experts pointed to during early stages of the knowledge elicitation method used.

The authors acknowledge that the depth of the knowledge elicited is limited to a high-level understanding of the domain. The limitation is due to two main factors, namely (1) the complexity of railway safety domain and (2) the limited availability of experts. However, the value of such knowledge resides in the number of key safety concepts and relationships identified by experts and the fact that knowledge models emerged as a result of a collaborative exercise where achieving experts' agreement was paramount.

A Decision Support System was developed by the authors which enabled the research team to use data already available and its analysis to consolidate, improve and reorganise where necessary the qualitative models of rail operation and safety into more elaborated and accurate knowledge representation structures. In doing so, the new system serves the purpose of validating the knowledge elicited from experts.

Section 2 presents a brief literature review to situate this research in the context of railway safety and the probabilistic nature of such safety, alongside the current approaches to knowledge elicitation. Sections 3.1 to 3.3 present the main contribution of this paper, that is, our approach on knowledge elicitation from railway safety experts. Section 4 describes the evaluation of the knowledge elicitation approach, which consisted of using the elicited knowledge to support the railway industry in their efforts to predict safety incidents. In particular, section 4 describes the tool that was developed along with a safety case enumerated for analysis. Section 5 concludes the paper.

## 2. Literature Review

The first half of this section outlines the key theories informing our approach to eliciting safety-related knowledge from railway experts and then using this knowledge for safety decision making in the railway industry. The second half of the literature review provides a focus on the methodological aspects of this work.

We structure our review in three sections, where Section 2.1 addresses the domain of railway safety. We narrow the literature down to decision-making in the context of railway safety that is based on systems providing data. This reflects the priorities of the railway industry, where research on effective use of knowledge is limited.

The second half of this section is divided into two further areas. Section 2.2 reviews the state of the art in the knowledge elicitation literature, highlighting limitations of traditional approaches. Section 2.3 finally serves to clarify the methodology adopted in this paper by emphasising on the role of facilitation in the adopted methodology. We evaluate the choice of our approach by providing pointers to other similar domains where this approach has been successfully applied.

### 2.1. Railway safety and challenges associated with its management

Rail transport is part of the essential infrastructure that ensures economic success for any country or region. The railway industry is a complex system and all of the companies that are part of it share a common purpose: they seek to deliver a safe, reliable and environmentally friendly railway while offering value for money (RSSB, 2009). The main challenge associated to rail transport is its economic and safety management (Cox et al., 2003).

Although safety has improved significantly in the UK railway industry in recent years, as the pace of technological change increases more emphasis is put on the need for predicting the potential impact of changed systems and procedures, and on managing the safety associated with their implementation and operation (Holloway et al., 2013). However, it cannot always be assumed that safety is related to systems and procedures. Where human factors are involved complexity appears both at the operational and at management levels. Here "complexity" is used much in the sense of unpredictability (Elms, 2001). For example, the pressure on job completion targets and the lack of essential experience and awareness means a conflict between following rules to preserve safety and completing work on time. In addition to emphasis on productivity and not safety, a safety incident might be the result of human error.

The need for a clear and effective decision making for safety-related issues in railways has been motivated by Bohnenblust (1998) who makes a case for formal and agreed means to reach safety decisions, in an environment which is typically found to be complex, operational ownership of resources (such as assets and data) is shared, and where more than a single entity is often involved.

One such approached proposed has been Reliability Centered Maintenance (RCM), with a view to safety issues that may arise due to maintenance of assets part of a rail infrastructure (Carretero et al., 2003). Explored in the European context, the approach is promising and has been adopted by some Spanish and German operators to handle maintenance in such large scale deployments; dependencies are defined in terms of different components with a view that making (predictive) maintenance effective would lead to fewer safety issues. The scope of this approach however is narrow, down to only maintenance aspects.

Another proactive approach is demonstrated in an Australian case study (Graham et al., 1996) where an interventionist approach, essentially a system's approach by Reason (1995), to proactively manage and decide on safety issues, is demonstrated. Investigated using train drivers from an Australian rail operator, the advantages of a proactive safety management approach are shown, with a particular finding that an overall systems view is very important. The finding suggests that if safety-related data is to be used effectively then an organisation needs to be engaged both horizontally and vertically. This underpins our effort to strive for holistic data sets for effective safety decision making.

In common with all areas of safety management, decisions have to be made about the level of resources that can be committed to supporting the achievement of safety. Such decisions take place in a context of competing demands, regulatory requirements, and a wider politics concerning the issues in question (Horlick-Jones, 2008). Therefore, attempts to facilitate safety decision making are seen as a positive step by the railway industry. Continuous data collection processes from several sources provide the railway industry with regular snapshots of the situation and usage of their infrastructure and capabilities.

# 2.2. Knowledge elicitation and transfer 

Informed by the views reported by Mowery et al. (1996), Cooke (1999) and Hickey and Davis (2004), knowledge elicitation and transfer can be understood as the process of enabling people to acquire new capabilities while others who already have such capabilities explicate the domain specific knowledge underlying their performance (Garcia-Perez, 2010). The aim of knowledge elicitation is the development of methods and tools that make the arduous task of capturing and validating an expert's knowledge as efficient and effective as possible (Gavrilova and Andreeva, 2012).

From the origins of knowledge engineering in the 1980s knowledge elicitation from experts and its transfer to others have been the focus of a growing number of areas concerned with the integration of Knowledge Management into enterprise environments for the improvement of organisational business processes . which have used mainly two general techniques (Davis and Steinglass, 1997; Pun and Nathai-Balkissoon, 2011).

However, significant problems have continued to arise when organisations undertake knowledge elicitation strategies fully based on the use of software or approaches that are purely based on peoplebased mechanisms. Paradoxically, organisations continue to try to elicit knowledge from experts and transfer such knowledge to its potential stakeholders using approaches that rely on extreme positions. These range from interviewing an expert who is leaving in an attempt to record everything they know, to the use of software to gather raw data and generate a knowledge repository (Hoffman et al., 2008, p. 86). Thus, defining and implementing the right approach to knowledge elicitation and transfer continues to be one of the main challenges of integrating KM in organisations today (McInerney, 2002).

# 2.3. Collaborative modelling as an approach to knowledge elicitation and transfer 

A new mechanism which is based on the identification of key concepts and the creation of models of the domain based on stakeholders' experience has been found to overcome the main challenges of existing approaches (Garcia-Perez and Ayres, 2009). In this approach experts and key individuals for whom experts' knowledge might be relevant (referred to as stakeholders of that knowledge) are identified and then brought together to discuss and agree on key concepts in the domain and develop some representation or model which links these concepts in a meaningful way.

The Concepts-Modelling-Experience (CoMEx) approach to knowledge elicitation and transfer used in this research, has been successful in other contexts (Garcia-Perez, 2010). Its first application was in an engineering setting and focused on capturing knowledge about gas turbine operation (Garcia-Perez and Ayres, 2009). Subsequently, CoMEx has been applied in the fields of infrastructure management within the defence industry, and research within the higher education sector (Garcia-Perez and Ayres, 2012).

The modelling associated with the method is essential, both as a knowledge sharing mechanism and as a process of capturing the knowledge into a representation scheme as a tangible output. There are few constraints on what is used as a knowledge representation scheme - it might be a concept map, spreadsheet or complex dependency diagram showing relationships - provided it is useful in helping experts and stakeholders develop and refine a common understanding. The role of the knowledge management specialist becomes one of facilitating this process. The specialist will give structure to the meetings and suggest representation schemes for participants to consider. This view is in line with Gavrilova and Andreeva's (2012) view whereby the specialist can act as an intermediary between an expert and his knowledge, on the one side, and an organisation (a knowledge base and/or individual members of the organisation) on the other side, thus facilitating knowledge transfer between the two.

## 3. Knowledge elicitation in practice for railway safety

This section describes our central effort where we put in practice the knowledge elicitation method to the case study at hand. Section 3.1 provides for a brief background to the project objectives. Section 3.2 describes the research team preparation underlying the knowledge elicitation exercise. Section 3.3 delves into the detail of engaging with the experts and presents the significant outcomes in terms of data and safety models.

### 3.1. Project initiation

The researchers sought to involve in this project expertise from different sections of the British railway industry (i.e. infrastructure manufacturers, owners and operators) to first identify and later understand their key data stocks and data flows and, more importantly, the perceived relevance of such resources for the purpose of understanding safety. A consortium was formed including safety and

data experts from the railway industry and their regulating body (the UK Railway Safety and Standards Board), as well as academic partners with knowledge of safety and related human factors. Twelve individuals holding senior managerial positions at 8 rail-related organisations agreed to provide their knowledge for the benefit of the industry. Their roles varied from data and information managers to railway safety consultants.

# 3.2. Knowledge elicitation project preparation 

An initial desktop research was conducted to identify and understand the nature and structure of key data streams within the different sections of the rail industry. Members of the consortium provided what they understood as the key data structures for their specific areas, which were also analysed during this phase of the research. Figure 2 shows an example of the type of models produced by the authors during the preparation stage.
![img-1.jpeg](img-1.jpeg)

Figure 2. A section of one of the models produced by the project team using railway data.
Having created initial models for railway data and safety, the authors focused on the elicitation of knowledge of railway operation and performance from railway experts in the form of metadata-driven knowledge models, with focus on factors of safety concern.

### 3.3. Knowledge elicitation exercise

The key to this phase of the research consisted of bringing a group of railway safety experts together to provide their views on the growing relationship between data and safety, as a mechanism of capturing their knowledge in an explicit, transferable form. The models previously developed by the project team were used as a catalyst to the process of eliciting knowledge from experts. A knowledge elicitation workshop was then planned as a two-day exercise to take place at an academic institution, where experts could avoid having to deal with the pressures of their working environments.

An additional aim of the knowledge elicitation workshop consisted of verifying the value of the sources of safety-critical data discovered by the project team in phase one, as well as identifying new sources, to then integrate these into a probabilistic data analysis tool to understand safety.

A series of four meetings lasting approximately 2 hours each were carried out over the two days. A room was prepared to hold the meetings by following the recommendations in Garcia-Perez (2010) and the experience from similar projects such as those reported by Garcia-Perez and Ayres (2009) and Garcia-Perez and Ayres (2012). This included, for example:

- A U layout for the room which enabled visibility and collaboration.
- Availability of drawing facilities such as flip chart sheets and whiteboards.

Each meeting started with a short introduction to the subject, followed by the presentations of the models previously developed by the project team. Key developments during the series of meetings included:

- Discussions of different views of safety, its probabilistic nature, its reliance on a number of human factors and the approaches to understanding and addressing these by different organisations within the railway industry.
- Identification of several safety-related data sources and provision of relevant data samples by participants.
- Collaborative development of a series of models of railway operation and railway safety. A section of two of such models (figures 3 and 4) are included in this paper for illustration purposes.

The workshop highlighted the need to have a common approach to questions such as the safety of new IT-based products and services for the railway and the need for new strategies to use experts' views to understand safety. A number of models of railway data and safety were produced by experts. Sections of two of these are included in Figures 3 and 4.
![img-2.jpeg](img-2.jpeg)

Figure 3. A section of one of the models developed by participants during the knowledge elicitation workshop: understanding asset risks.

Figure 3 captures experts' attempt to reach a common understanding of safety by identifying key concepts (e.g. risk, assets, operation) and creating a series of models which helped them understand high-level relationships between such concepts.

![img-3.jpeg](img-3.jpeg)

Figure 4. A section of the Platform-Train Interface safety incident model as outlined by experts during the knowledge elicitation exercise.

Figure 4 presents a section of a model which captures experts' views on the factors that influence a particular type of safety incident which may result in injuries to individuals in or close to the Platform-Train interface. The key factors identified were related to the injured person, the train, the station or the timing of the incident. The relationships between those factors resulted from the collaboration at the modelling phase of the project.

At a later stage, qualitative values representing the likelihood of occurrence of each of these factors (i.e. probabilities) was added to the qualitative model in figure 4 to produce a statistical model in the form of a Bayesian network, a type of probabilistic graphical model which can then be used for data analysis.

The quality and richness of the data gathered throughout the two days of the workshop promoted an understanding of the potential benefits of knowledge sharing for the stakeholders involved. This shows that developing a meaningful knowledge elicitation and transfer strategy is key where knowledge (that is, experience, skills) and information would be used as a means of improving safety in the industry.

# 4. Data-driven safety analysis and prediction in railway 

A central question we address in this section is how do we use captured knowledge for effective decision making in the context of this domain? The essential aim here is to validate our approach and demonstrate the models derived for the kind of decision making such models are used for. Section 4.1 describes the dedicated support tool developed by the team to estimate safety parameters based on the models derived from the experts.

The particular safety case we addressed was the Platform-Train Interface (PTI). PTI incidents are those that occur at the boundary where the platform and train meet. Though there is a very low probability of PTI incidents occurring to an individual, the consequences of failures at the interface can be severe. The Railway Safety and Standards Board (RSSB) estimates that, on the British mainline, the largest proportion of serious injuries and fatalities to individual passengers occur at the platform train interface, representing around $40 \%$ of passenger fatality risk. On London Underground this is also an important topic as PTI accounts for over 20\% of passenger fatality risk (ORR, 2014).

Sections 4.2 to 4.4 each addresses an individual incident category that has a role to play in decision making for such a safety case. These include platform foot-falls, weather, and the day and time of the week. Each section demonstrates the knowledge elicited from experts and how it could be used to decide on individual cases. Each of these serves to validate our approach in this paper.

As a mechanism of validating the knowledge elicited, a software tool was developed to explore the value of such knowledge for the railway expert to:

- Use data already available and its quantitative analysis to understand the relationship between the different parameters that influence a PTI incident,
- Use the resulting probabilistic model to generate meaningful prognostics information from data available and visualise such information in a way that supports prediction of safety violations.

The tool combines functionality for creating new models of railway data and its relation with safety, running simulations to analyse trends or factors affecting or leading to safety incidents, and running exploratory, probabilistic inferences based on the likelihood of safety incidents, given specific, hypothetical assumptions. Addressing the needs that were raised in the workshop, the tool was designed to integrate with other existing or future tools for the railway industry to handle safety.

The core of the implementation of the Safety Prognosis tool is determined by the use of two free and open source software tools: GeNIe and SMILE (DSL, 2014), developed by the Decision Systems Laboratory of the University of Pittsburgh. GeNIe is a development environment for creating and manipulating belief networks, which is a type of probabilistic model. SMILE is a library of classes to use the models to implement graphical decision-theoretic methods.

# Section 4.1 Providing for tool support in decision making 

On completion of the workshop, the project team was able to formalise the PTI model developed by experts. Using the Bayesian approach to the analysis of causal inference, two models were integrated: a qualitative and a quantitative model of PTI. The knowledge elicited formed the qualitative dimension of the Bayesian Network, as a directed acyclic graphical model, while its quantitative dimension (i.e. probabilities associated to the different variables) was estimated using the data sets provided by workshop participants and/or expert's judgments. It must be stressed at this point that given the variety of factors potentially affecting a PTI incident the model and Bayesian Network used in this research for validation of the knowledge elicitation approach are not necessarily exhaustive.

Experts' perception was that station footfall, weather, day of the week and time of the day are key factors that influence the probabilities of a PTI incident taking place at any station. Thus, understanding and predicting the occurrence of a PTI safety incident by looking at variations in those parameters could be the key for decision makers within the railway industry to put in place the right measures to minimise such risk. We use the PTI case to demonstrate the Safety Prognosis tool and explore the relationship between such a safety incident and other parameters.

### 4.2. Case 1: Predicting relationships between PTI incidents and station footfall

Station footfall, that is, the number of passengers that entry/exit the station plus those that use the station for an interchange, is one of the factors to be considered when studying the likelihood of the occurrence of a PTI safety incident. This section of the research was therefore set to address the following question:

Question: To which extent is the possibility of occurrence of a PTI incident at a particular train station related to the number of customers entering, leaving and using the station for interchange?

As Figure 3 shows, there is an effect between station footfall and a PTI, determined by the following chain of direct influences: Footfall $\rightarrow$ Station operation $\rightarrow$ Station $\rightarrow$ PTI Incident.

The footfall variable can take three different values, determined by two different situations.

- Footfall may have not been observed/recorded (value: none). This describes a situation where data for the footfall parameter is not available for a particular station. In this case, footfall

observations from historical data, e.g. from previous months/years, could be used to run inferences and understand relationships which may exist.

- The number of customers entering and/or leaving the station has been observed and recorded. In this case the value of the footfall parameter could be either high or low. Using the Safety Prognosis tool, such information can be considered by updating the initial Bayesian network which was developed from the experts' knowledge models. Then a number of inferences may be drawn by the railway expert as appropriate for decision making.

Probabilities for each of the values of the footfall variable (above), which were extracted from safetycritical data sets provided by consortium members, are presented in table 1.

Using the safety models elicited from experts, the authors ran a number of simulations using the Safety Prognosis tool. These resulted in a number of estimated probabilities for the occurrence of a PTI incident in relation to the footfall variable. The results are presented in table 1 and in figure 5.

Table 1: The footfall variable: possible states and their impact on safety.


In Figure 5, the $X$ axis represents possible situations of the footfall variable, that is not recorded (unknown), recorded as high and recorded as low. The $Y$ axis represents probability values (maximum value is 1). The probabilities of each of the two states high and low of the footfall parameter and those of the two states true and false of the PTI-Incidents parameter are represented by coloured bars in the figure. Note that given the scale of the diagram, the variation in the probability of a PTI incident is better seen in table 1 above.
![img-4.jpeg](img-4.jpeg)

Figure 5: Variations in the likelihood of a PTI safety incident in relation to the station footfall

According to the analysis described in this section there is a direct relationship between footfall and safety of railway passengers and staff. This result serves to inform the industry management of the need to understand why, where and when there will be a significant change in footfall so that the right measures are put in place to minimise the risk of slips and trips leading to accidents in or around the passenger-train interface.

The results of this and similar PTI-Footfall simulations have been presented to safety experts from the railway industry. Their feedback shows that the Safety Prognosis tool supports the industry in their efforts to understanding the potential effects of footfall in PTI safety incidents so that right decisions are made to minimise risks in predictive footfall situations. Ultimately, this is an evidence of the validity and value of the knowledge elicited from railway experts using the approach to knowledge elicitation proposed by this research.

# 4.3. Case 2: Predicting the effects that weather may have on PTI incidents 

Weather conditions appear to have an effect on the rate of PTI incidents. The Railway Safety and Standards Board has found that there are more incidents occurring when the weather is wet and icy than when it is dry (Carpenter, 2011). The key question that this research addressed in this area was:

Question: In the view of safety experts, is there a direct link between weather conditions and the occurrence of a PTI safety incident? If so, how relevant is such a relationship for the purpose of decision making?

In order to study the influence of weather in the overall nature of the PTI safety incidents -as understood by railway experts involved in this research, the authors conducted a similar analysis to that for footfall described on section 4.1.1.

Weather has been defined as a variable which can be described as: normal/dry, wet/rainy, and snow/icy conditions. There is also a probability that data about the weather variable has not been collected for a particular period of time or location. This case would be represented in the analysis as none, and the value of the weather variable would need to be estimated by using other parameters. Where weather conditions are known, the influence network developed by the project team also allows a combination of these to form, for example, wet and icy weather conditions.

According to the Bayesian network developed on the basis of knowledge elicited from railway experts, there is a dependency between weather conditions and PTI incidents, determined by the following chain of influences: Weather $\rightarrow$ External factors $\rightarrow$ Station operation $\rightarrow$ Station $\rightarrow$ PTI incident. Assuming that all probability definitions and likelihoods are correct, then the influence of weather on a PTI Incident can be estimated by using the Safety Prognosis tool developed by the authors.

Under the above assumption, the authors extracted probabilities for each of the values of the weather variable from safety-critical data sets provided by members of the consortium. The results of this data analysis are presented in table 2 .

Using the safety models elicited from experts, the authors ran a number of simulations using the Safety Prognosis tool. By leaving all other parameters unchanged, these simulations provided a number of estimated probabilities for the occurrence of a PTI incident in relation to the weather variable. The results are presented in table 2 and in figure 6.

Table 2: The weather variable: possible states and their impact on safety.



In figure 6, the $X$ axis represents possible situations of the weather variable, that is not recorded (none), recorded as normal, wet or snow. The $Y$ axis represents probability values (maximum value is 1). The probabilities of each state of the weather parameter and those of the two states true and false of the PTI-Incidents parameter are represented by coloured bars in the figure. Note that given the scale of the diagram, the variation in the probability of a PTI incident is better seen in table 2 above.
![img-5.jpeg](img-5.jpeg)

Figure 6: Variations in the likelihood of a PTI safety incident in relation to the weather

In line with experts' understanding of safety, the use of the knowledge models and data available has corroborated that there is a link between weather and safety incidents in the passenger-train interface. This helps raise awareness in the industry management of the need to put measures in place at stations -particularly those with platforms exposed to the weather, where significant variations in weather conditions are expected, in order to minimise the risk of PTI safety incidents.

As with the PTI-Footfall simulations, safety experts from the railway industry have confirmed the value of the weather simulations facilitated by the Safety Prognosis tool for the purpose of decision making. This, again, suggests that the approach to knowledge elicitation proposed by this research was successful in capturing and recording safety knowledge which is both valid and valuable for the railway industry.

# 4.4. Case 3: Analysis of relationships between date/time and PTI incidents 

There is enough evidence to suggest that the value of many safety-critical variables depend on the timing of the data collection, that is the month of the year, day of the week and time of the day. Such variables include the passenger profile, station footfall and others which experts at the knowledge elicitation exercise identified as essential for the understanding of PTI safety incidents. In this sense, the Railway Safety and Standards Board found that the number of PTI accidents increases during the week and on weekends, possibly due to increase in leisure travellers at these times, who may be less frequent passengers and therefore less familiar with the railway network (Carpenter, 2011).

On these basis, this research looked to understanding experts' perception of the timing of a PTI incident by combining it with historical data to run a simulation using the Safety Prognosis tool. Giving the availability of data to run the simulations, the analysis focused on one variable at a time, starting with day of the week and later focusing on time of the day.

The focus of the analysis was therefore defined by the following question:
Question: According to railway experts, is there a direct link between timing of a PTI safety incident (i.e. day of week, time of day) and the probabilities of occurrence of such an incident? Should time be considered by the industry management for the purpose of decision making?

# 4.4.1. Day of the week and its effects on PTI safety incidents 

The analysis of the day of the week was made by looking at two possible cases: weekdays and weekends. There is also a need to consider those cases in which the day of the week has not been recorded in the data collected. This is done by including a third state (defined as none) for the day of the week, which is then estimated by looking at other parameters within the data set.

The authors acknowledge that the study of the day of the week could be taken further to analyse special cases such as bank holidays weekdays where the profile of the transport network and its passengers is significantly different. However, a high level analysis of the day of the week was considered sufficient for the purpose of assessment of the proposed approach to knowledge elicitation.

According to the knowledge elicited from railway experts, there is a direct dependency between day of the week and PTI incidents, represented in the Bayesian network as follows: Day of the week $\rightarrow$ PTI incident. It is therefore possible to estimate the influence of day of the week on a PTI Incident by using the Safety Prognosis tool developed by this research.

The authors extracted probabilities for each possible value of the day of the week variable from safetycritical data sets provided by members of the consortium. The results of this data analysis are presented in table 3. Then, using the safety models elicited from experts, a number of simulations were ran using the Safety Prognosis tool while leaving all other parameters unchanged. These simulations provided a number of estimated probabilities for the occurrence of a PTI incident in relation to the day of the week variable. The results are presented in table 3 and in figure 7.

Table 3: The day of the week variable: possible states and their impact on safety.


In figure 7, the $X$ axis represents possible situations of the day of the week variable, that is not recorded (none), recorded as a weekday or recorded as a weekend. The $Y$ axis represents probability values (maximum value is 1 ). The probabilities of each state of the day of the week parameter and those of the two states true and false of the PTI-Incidents parameter are represented by coloured bars in the figure.

![img-6.jpeg](img-6.jpeg)

Figure 7: Variations in the likelihood of a PTI safety incident in relation to the day of the week (weekday/weekend)

The findings of this analysis conform to the expectation that the day of the week is directly related to the probabilities of occurrence of a PTI safety incident. This could be due to a number of reasons, some of which may still need to be explored/understood by the industry. However, the industry has now had confirmation -based on experts' views, that specific measures need to be put in place to address the difference between the number of PTI incidents occurring during the week and at weekends, and thus minimise the risk of safety incidents at certain times of the week.

The day of the week analysis has been another opportunity to confirm that the approach to knowledge elicitation proposed by this research has been successful in capturing and recording knowledge which is accurate and valuable for the purpose of decision making in the railway industry.

# 4.4.2. Time of the day and its effects on PTI safety incidents 

Having understood the value of the time of the day as a variable for analysis of safety incidents, the authors sought to define the possible states for it. There is awareness of the different ways of looking at the time of the day, depending on the purpose of the analysis. However, for the purpose of validating the approach to knowledge elicitation and transfer proposed by this research, the authors took a view of time of the day which was easy to draw from data available and to understand by readers from different backgrounds. Thus, time of the day was considered as a variable which may take three possible values: morning, afternoon and evening. An additional value, represented as none was introduced for those situations where the time of the day has not been recorded.

As with day of the week, railway experts expressed their view of time of the day as a variable which directly determines the probabilities of occurrence of PTI incidents. This was represented in the Bayesian network as: Time of the day $\rightarrow$ PTI incident, with the purpose of estimating the influence of time of the day on a PTI Incident by using the Safety Prognosis tool.

The authors extracted probabilities for each possible value of the time of the day variable from safetycritical data sets made available by experts, as shown in table 4. Later, the safety models elicited from experts were used to run simulations using the Safety Prognosis tool while leaving all other parameters unchanged. A number of estimated probabilities for the occurrence of a PTI incident in relation to the time of the day variable are presented in table 4 and in figure 8.

Table 4: The time of the day variable: possible states and their impact on safety.



In figure 8, the $X$ axis represents possible situations of the time of the day variable, that is not recorded (none), recorded as a morning, afternoon or evening. The $Y$ axis represents probability values (maximum value is 1 ). The probabilities of each state of the time of the day parameter and those of the two states true and false of the PTI-Incidents parameter are represented by coloured bars in the figure.
![img-7.jpeg](img-7.jpeg)

Figure 8: Variations in the likelihood of a PTI safety incident in relation to the time of the day (morning/afternoon/evening)

Once again the findings of the analysis of data meet the expectations of railway experts in terms of the relationship between the time of the day and the probabilities of occurrence of a PTI safety incident. This cannot be seen in isolation but related to other variables such as footfall or passengers profile, which vary for a particular train station across the day. However, this research provides yet another view of the relationship between those variables based on knowledge elicited from experts, which adds to the value of the approach to knowledge elicitation proposed by this study.

# 5. Conclusion 

This paper set out to address a number of important questions including the capture of safety-critical knowledge and its use for effective decision making. Another important element central to our work has been the use of a knowledge elicitation approach for this purpose.

We have reported on the application of an approach to knowledge elicitation which overcomes some of the key limitations of existing approaches at an industry level. Section 3 shows how our effort serves to assess the feasibility of capturing knowledge from railway experts in the form of models of the safety domain and then using railway data effectively for predicting safety cases.

This paper provides a proof of concept to the transport community for making safety decisions based on a wide variety of expertise areas within safety and disparate safety-critical data sources. Section 4 provides examples of real-world safety cases in the railway domain. We have used a high-level architecture of the safety data in the railway domain in the UK, and build over it a tool to help analysts incorporate data sources for handling safety decisions for data holders to be able to understand the potential safety implications of their data sets.

In an industrial context, this work potentially sets a precedent for a systematic yet simple approach to account for expert knowledge to reach important decisions. While our demonstration has been limited in scale, the use of actual data attributes and datasets, along with knowledge captured from real experts is an important milestone that this paper has achieved.

# Acknowledgments 

This research has been funded by the UK Railway Safety and Standards Board (RSSB) through the Rail Research UK Association (RRUKA). This work has benefited from contributions from several organisations including Network Rail, London Underground, Transport for London, First Class Partnerships, SMT (Staff Management Tools) Ltd, TRE Ltd, TIBCO Software Ltd. We are grateful for their valuable time and input.
