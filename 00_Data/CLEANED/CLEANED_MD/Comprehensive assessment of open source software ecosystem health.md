# Comprehensive Assessment of Open Source Software Ecosystem Health 

Marc Oriol ${ }^{\mathrm{a}, *}$, Carlos Müller ${ }^{\mathrm{b}}$, Jordi Marco ${ }^{\mathrm{a}}$, Pablo Fernandez ${ }^{\mathrm{b}}$, Xavier Franch $^{\mathrm{a}}$, Antonio Ruiz-Cortés ${ }^{\mathrm{b}}$<br>${ }^{a}$ Universitat Politècnica de Catalunya, Barcelona, Spain<br>${ }^{\mathrm{b}}$ Universidad de Sevilla, Sevilla, Spain


#### Abstract

Recent surveys expose that the use of Open Source Software (OSS) is increasingly becoming a need for organisations in their development projects. However, deciding a proper OSS to be adopted or to contribute to its development is a complex and error-prone task. Analysing the OSS ecosystem (OSSECO) health may help providing information about: (1) the OSS itself (number of commits, days after the last release, etc); and (2) their main actors (number of contributors, partners, etc). There exist proposals that go further and provide aggregated high-level indicators (e.g. visibility as an aggregation of number of community events, number of partners, and other metrics). Nevertheless, there is a lack of useful OSSECO analysis tools to ease the decision making on which OSSECO has the health required by a potential OSS adopter or contributor. In this work, we provide OSS-CARE (OSSeCo heAlthy monitoR and analysEr), an OSS-independent, fully automatic, and real-time framework to assess OSSECO's health. OSS-CARE supports defining the ecosystem health objectives of potential OSS adopters, OSS contributors, and even OSS managers to inspect their provided health. These objectives are defined based on a well-established model characterizing health metrics that can be potentially aggregated by using a Bayesian network technique. Moreover, the integrated monitoring and analysis components perform an automated assessment of OSSECO's health by checking the fulfillment of the required health objectives. Furthermore, the result is shown in an appealing dashboard that may ease the complex decision making of which OSS to choose.


keywords Open Source Software Ecosystem (OSSECO), Open Source Software (OSS), Monitoring, Ecosystem Health

[^0]
[^0]:    *Corresponding author. Campus Nord, Omega building, 004, C/ Jordi Girona Salgado 1-3, E-08034, Barcelona, Spain

    Email addresses: marc.oriol@upc.edu (Marc Oriol), cmuller@us.es (Carlos Müller), jordi.marco@upc.edu (Jordi Marco), pablofz@us.es (Pablo Fernandez), xavier.franch@upc.edu (Xavier Franch), aruiz@us.es (Antonio Ruiz-Cortés)

# 1. Introduction 

Open Source Software (OSS) is increasingly becoming a core asset for information technology (IT) related organizations. As of 2022, it is estimated that $97 \%$ of software applications are using OSS [1], and $80 \%$ of IT leaders expect to increase the usage of OSS for emerging technologies (e.g., Artificial Intelligence, Internet of Things, Serverless Computing) [2]. Given this importance, choosing to adopt a particular OSS component and then managing it and even contributing to its evolution is a crucial task for most organizations. However, over $60 \%$ of such organizations do not have in place a formal process for managing OSS [3]. The absence of robust and trustworthy OSS-related processes can significantly impact the quality of the software integrated or produced within an organization.

One of the main factors to consider in these processes is that OSS does not exist in isolation. Instead, the adoption, contribution and management of a particular OSS component heavily depends on its context or ecosystem. Generally speaking, a software ecosystem is a set of actors functioning as a unit and interacting with a shared market for software and services, together with the relationships among them [4]. In the particular case of OSS ecosystems, abbreviated as OSSECO, the focus lays on the OSS community that manages a set of projects in an open-common platform [5]. OSSECOs differ from proprietary software ecosystems in terms of production processes, open community perspective, distribution methods, license types, social organization, support and quality evaluation (e.g. Eclipse, Apache, Linux) [6]. In this context, the traditional problem of OSS adoption, contribution and management evolves into a more general (and complex) problem at the level of OSSECOs. In particular, selecting an OSS component is leveraged into selecting the OSSECO that surrounds it.

In order to address OSS-related issues from the perspective of OSSECOs, we coincide with Lucassen et al. [7] in arguing that a proper indicator that can help to select an OSSECO is its health. Health is an elusive concept that can be approached from several perspectives, and various software ecosystem health definitions have been proposed in the literature (see Section 2 for a discussion). This work adopts a simple definition from Wang et al.: the OSSECO health is "the ability of the ecosystem to continuously develop and maintain structure and function over time" [8].

The indicators that can be used to measure the OSSECOs' health are highly dependent on the context in which they are used and the purposes a stakeholder pursues (e.g., an OSSECO with a mature OSS may not require a large number of development activities from its contributors to be considered healthy, compared to an OSSECO with a less mature OSS) [9]. In this study, we distinguish three main types of stakeholders: OSS adopters, OSS contributors, and the OSS manager:

- OSS adopters: organizations and individuals aiming to integrate and use existing OSS in their projects.

- OSS contributors: organizations and individuals contributing to OSS components (e.g., implementing improvements or extending their functionalities)
- OSS manager: the responsible to manage the development and maintenance of the OSS.

In this work, we claim that an automated domain-independent technique to ease the decision making processes related to OSS adoption, contribution and management shall provide tangible benefits to OSSECO stakeholders. These stakeholders could establish some conditions on some health-related attributes denoting either their expected health (for OSS adopters and OSS contributors), or their provided health (for OSS managers). For instance, a potential OSS adopter that is looking for a mature OSS from an OSSECO may appreciate a low number of open bugs in the OSS against other OSSECOs with better contributors expertise or a higher number of contributors. These later features might be essential features for a developer that is looking for an OSSECO to contribute, but not for a potential OSS adopter. Finally, the OSS manager may be interested to monitor several attributes of the OSSECO health related to its usage and popularity.

This vision motivates our research question:

RQ: How to define, monitor and analyze conditions over the health attributes of an OSSECO considering the different perspectives of (1) OSS adopters, (2) OSS contributors, and (3) OSS managers?

To address this research question, we propose a domain-independent framework, named OSS-CARE (OSSeCo heAlthy monitoR and analysEr), able to assess the health of different types of OSSECOs, and able to perform the monitoring and analysis of OSSECO health in a fully automatic and real-time manner.

The contributions of this work are the following:

- A reference model to define, monitor and analyze conditions over health indicators of an OSSECO.
- An instantiation of the reference model with a specific architecture and implemented components.
- An extension of the quality model QuESo 10, 11] to facilitate the monitoring of health indicators within the OSS-CARE architecture.
- A language to specify conditions over health indicators, enabling its analysis within the OSS-CARE architecture.

The rest of the paper is structured as follows: Section 2 presents the background on what constitutes a healthy OSSECO. Section 3 discusses the related

work. Section 4 presents the OSS-CARE framework: the conceptual model, the specific architecture, and its main artifacts. Section 5 describes the process of deploying the OSS-CARE framework. Section 6 presents the conducted evaluation. Finally, section 7 provides the conclusions and discusses future work.

# 2. Background: What is a healthy OSSECO? 

This section summarizes the key definitions and characteristics on OSSECOs' health, mainly based on the results of Franco-Bedoya et al.' systematic mapping $[5]$.

One of the early definitions of OSSECO's health was provided by Wynn et al. [12], who described it as a proxy for the sustainability of the social system that surrounds the OSS. More specifically, they defined the OSSECO's health as the ability of an ecosystem to remain viable and capable of sustaining the participation of their members.

In order to evaluate the OSSECO's health, Wahyudin et al. [13] proposed the concept of health indicators as a means to measure and quantify key characteristics that may be used to predict the survivability of the underlying projects. Similarly, Jansen et al. [4] proposed several indicators to conduct such measurements. In particular, Jansen et al. adopted indicators from the Business ecosystem domain previuosly introduced by Iansiti et al. (e.g. survival rates, network stability, network connectedness, centrality, etc.) [14]. To structure these health indicators, various quality models have been proposed [15, 8, 16]. Quality models are engineering artifacts that structure the health indicators in a hierarchical manner: on top of the hierarchy there are high-level characteristics (e.g., size, visibility), which may be decomposed in other health indicadors, until reaching low-level measurable metrics (e.g., Number of contributors, Number of partners). Several approaches exist to compute the values of these high-level characteristics from the measurable metrics they are composed of using a bottom up approach (e.g., by applying aggregation functions that combine the different metrics) $[8,17]$.

Subsequently, Jansen [9] argued that an OSSECO is healthy if it expresses qualities that are typically associated with health (e.g., liveliness, activity, longevity) and adopted the definition proposed by Lucassen et al. [7] who define the OSSECO's health as longevity and propensity for growth.

Other relevant definitions include the one proposed by Manikas et al. [18] who defined the health of an OSSECO as the ability of the ecosystem to endure and remain variable and productive over time. In this work, a similar but more recent definition for OSSECO's health is used: "the ability of the ecosystem to continuously develop and maintain structure and function over time" [8], which is a definition adopted from the environmental management field [19].

## 3. Related work

This section discusses and evaluates the related work according to four dimensions we identified as relevant for the definition, monitoring and analysis of

an OSSECO's health:

- Dimension 1 - Characterization of the health of an OSSECO: To what extent the different indicators that constitute the health of an OSSECO are defined and structured.
- Dimension 2 - Computation of the values of health indicators: How the values of the different health indicators are computed and propagated.
- Dimension 3 - Definition of conditions over the health indicators: Whether conditions over the health indicators can be specified, and the level of expressiveness of those conditions.
- Dimension 4 - Monitoring and analysis of conditions over the health indicators: Whether the values of the health indicators can be automatically monitored, and if the assessment of the conditions is automatically analyzed.

Table 1 provides a summary of the results of such analysis, showing that none of the existing proposals completely fulfill dimensions 3 and 4, as detailed below.

Table 1: Assessment of related work (proposals appear in inverse chronological order of publication)


Dimension 1 - Characterization of the health of an OSSECO: Several works propose a quality model to characterize health indicators in a hierarchical man-

ner. Most of them are generic and cover different aspects of an OSSECO [20, $8,16,23,10,11,9,27,30]$. A few, although they also present a quality model, focus only on indicators that can be obtained from a single specific source, such as a software repository $[17,22,31]$ or a mailing list [29]. Some quality models are limited to a specific domain, like Content Management Systems [25], antivirus tools [24] or a specific Linux distribution [28]. Others present a quality model with several characteristics, but they are not decomposed into further attributes or metrics [18], or those metrics are presented as examples, without properly defining the quality model [26]. Finally, one proposal presents several metrics but without defining a quality model [21],

Dimension 2 - Computation of the values of health indicators: Some approaches provide means to compute the values of the characteristics and metrics from an OSSECO's health quality model following a bottom up approach [8, 17, $10,11,27,29,30]$. We found one proposal that, although having a component to compute characteristics from metrics, the details of how this computation is performed are not described [26]. A few proposals provide other mechanisms to compute characteristics from metrics but with some limitations: characteristics are limited to boolean values only [16, 23], the aggregation technique can only be applied to a specific characteristic [22], or the aggregation is limited to just computing the average, maximum or minimum values of the metric without combining other metrics [31]. Finally, the rest of analysed proposals, do not aggregate the values of metrics $[21,20,24,9,18,25,28]$.

Dimension 3 - Definition of conditions over the health indicators: Only one proposal partially supports the definition of conditions over the values of health indicators (characteristics and/or metrics), which is accomplished through ontological rules [23]. However, the syntax of those rules cannot combine conditions over multiple indicators. The rest of the proposals do not provide mechanisms to define conditions over health indicators.

Dimension 4 - Monitoring and analysis of conditions over the health indicators: Some approaches propose a monitoring framework to gather automatically the values of the metrics [21, 17, 24, 26, 28]. However, they do not conduct an analysis to detect possible violations over specified conditions, as they lack this feature. One proposal partially provides the ability to specify and analyse conditions [23], however, most of the collected metrics are not automatically monitored, but rather collected manually through a user-input form.

As a result of the analysis, we can conclude that although some of the proposals fulfill dimensions 1 and 2 , none of the existing proposals successfully fulfill completely the dimensions 3 and 4 . Even more, the four proposals completely fulfilling dimensions 1 and 2 , do not cover any of the other two dimensions even partially. The only proposal addressing the four dimensions is Carvalho et al [23], but still with significant limitations in three of them. To fill this gap, in this paper we propose a domain-independent framework, able to assess the health of an OSSECOs, by specifying conditions over health indicators and performing the monitoring and analysis in an automatic manner.

# 4. OSS-CARE framework 

To attain the defined Research Question, and considering the gaps identified in the Related Work (specifically, the dimensions 3 and 4 discussed in the previous section), we propose a versatile framework, named OSS-CARE, to define, monitor and analyze conditions over health indicators of an OSSECO. This framework has been designed following two levels of abstraction:

- OSS-CARE conceptual model: defines a reference model with the key entities, resources and relationships to assess the OSSECO's health. It provides a generic framework that can be ultimately instantiated through different architectures, components, languages and technologies.
- OSS-CARE architecture: presents an actual instantiation of the OSSCARE conceptual model, with a specific architecture and implemented components. The OSS-CARE architecture includes as well the definition of the artifacts required to support the monitoring and assessment of OSSECOs.


### 4.1. OSS-CARE conceptual model

We have designed the OSS-CARE conceptual model by applying principles and methods that are well stablished in related fields of monitoring and analysis. In particular, the OSS-CARE conceptual model adopts the principles from the field of monitoring and analysis of Quality of Service (QoS) in Service Oriented Computing (SOC). Although these two fields, namely SOC and OSSECOs, differ from a technical point of view, we argue that the inherent core principles and methods in SOC are analogous and can be applied to the field of OSSECO from a conceptual point of view (see Figure 1).
![img-0.jpeg](img-0.jpeg)

Figure 1: Approaching OSSECO healthy analysis as performed in SOC
In the field of SOC, illustrated in the left-hand side of the figure, Services are provided by Service Providers, who must guarantee a certain $Q o S$ as to fulfill the

Service Client's needs about performance, availability, etc. The different quality characteristics, attributes and metrics that conforms the $Q o S$ are structured in a Quality Model; and the conditions that must be satisfied upon them are operationalized into a Service Level Agreement (SLA), which is composed of a set of Service Level Objectives (SLOs) agreed between the Service Provider and Service Client.

The $Q o S$ is computed in a regular basis using a Monitor, which measures the behaviour of the services during their execution. The monitoring results are checked against the $S L A$ by an Analyser, and possible violations are detected and reported. On top of this basic schema, several tasks as Service Selection, and techniques as Proactive Adaptation, may benefit of the monitoring infrastructure.

In the field of OSSECOs, illustrated in the right-hand side of the figure, it can be observed that the OSS manager is the counterpart of a Service Provider, since they manage the OSSECO and want to guarantee an adequate level of healthiness, which is operationalized in Key Health Indicators (KHI) (the counterpart of QoS). As in the QoS, KHIs are structured through a Quality Model that we may call OSSECO Health Model; and the conditions that must be satisfied upon them are operationalized into what we call an Ecosystem Health Objective Set (EHOS), composed of a set of Ecosystem Health Objectives (EHO) (the counterparts of $S L A$ and $S L O$, respectively). In contrast with SOC, where the $S L A$ is agreed between Service Clients and Service Providers, in OSSECO, each stakeholder may define the conditions that they demand independently. In this regard, the OSS adopters and OSS contributors (the counterpart of Service Clients) may as well operationalize the quality that they require in their respectives EHOS.

Analogously to SOC, the KHIs are computed in a regular basis by a Monitor, which measures the different health indicators of the OSSECO. The monitoring results are checked against the EHOS by an Analyser, and possible violations are detected and reported. On top of this basic schema, several tasks as OSSECO selection may benefit of the monitoring infrastructure.

It is worth to mention that the OSS-CARE conceptual model is technologically agnostic and can potentially be applied to other domains, such as proprietary software ecosystems, hybrid software ecosystems (where OSS and proprietary software components coexist), or even non-software ecosystems (such as complex ecosystems of IoT devices and Cyber-Physical systems). For each of these different types of ecosystems, a specific architecture dependent on the underlying technology should be defined to instantiate the conceptual model. This architecture comprises the technological components to monitor and analyze the KHIs of the ecosystem, as well as the OSSECO Health Model and EHOS used to define those KHIs.

In the following subsections, a particular instantiation of the conceptual model for the OSSECO domain is provided.

# 4.2. OSS-CARE architecture 

In this section, the previously described OSS-CARE conceptual model is instantiated into a concrete architecture. Exploiting the conceptual analogy among SOC and OSSECOs presented above, the architecture of OSS-CARE has followed some of the techniques and design principles from an existing SOC framework, named SALMonADA [32], which is a versatile monitoring and analysis platform to monitor and analyze the fulfillment of SLAs of services. OSS-CARE has been implemented using the SOA principles of low coupling, high reusability, and composability. The different components have been implemented as RESTful services enabling the deployment of the whole solution in a distributed manner, facilitating its scalability (e.g., horizontal scalability through load-balancing techniques) and robustness (e.g., if a service fails, it may be replaced by another one providing the same functionality).

The architecture of OSS-CARE is depicted in Figure 2 and its main components are described below.
![img-1.jpeg](img-1.jpeg)

Figure 2: Detailed architecture of OSS-CARE

Wrapping API: To monitor an OSSECO using OSS-CARE, the OSS manager must first implement a simple web service interface (Wrapping API) that

connects with the different management tools that the OSSECO participants use to develop the OSS (e.g. GIT, JIRA, ...), as these management tools provide the raw data required to compute the KHIs. The Wrapping API provides a common interface to access the required data, hiding specific technologicaldependent characteristics of these tools, enabling its integration with the rest of the components of the architecture.

Composer: This component is the central part of the OSS-CARE architecture to assess the OSSECO's health. It receives as input: (1) the OSSECO Health model for an OSSECO and (2) the list of EHOS that the stakeholders of the OSSECO (OSS managers, adopters and/or contributors) want to monitor and analyze.

- The OSSECO Health Model may be any of the Health Models from the literature (as presented in the discussion of Dimension 1 in the Related Work), but for this architecture we have chosen the QuESo model $[10,11]$ (details on the selection of the QuESo model and its structure are discussed in section 4.3.1). To support the monitoring process of OSS-CARE, the QuESo Model has been extended to include not only the set of structured KHIs, but also the endpoints where the values of those KHIs will be made accessible during the monitoring process.
- The EHOS includes a list of objectives (EHO) over the KHIs of the OSSECO. We propose a simple but yet powerful syntax based on SLAs to define those EHOS (detailed examples of EHOS are presented in Section 4.3.2). To support the analysis process, the included KHIs must be part of the QuESo Model of the OSSECO.

The Composer extracts, from the QuESo Model, the KHIs with their respective endpoints, and configure the Measure Instruments of the Monitor to gather and expose their values. The Composer also checks that the KHIs included in the EHOS conforms to the received QuESo model, and forwards both the QuESo model and EHOS to the Analyzer for its analysis.

Monitor: The monitor includes several Measure Instruments to gather raw data from the Wrapping API and compute low-level metrics (e.g. number of partners, commits, open bugs). Each Measure Instrument is responsible to compute a specific metric. In this regard, the monitor can be easily extended with further metrics by implementing its corresponding Measure Instrument. These Measure Instruments feed a Bayesian learner, which computes the values of KHIs as a probabilistic result from the collected data. In particular, the Bayesian learner computes the probability that a given KHI of the OSSECO is high or low from the different measured metrics (e.g. it may determine that the OSSECO is highly active with a probability of $70 \%$ given the number of commits and frequency of releases). To compute these KHIs, OSS-CARE adopts existing Bayesian approaches applied in Sofware Quality Assurance, in particular it implements the Bayesian techniques presented in [33].

All computed KHIs are stored in a Repository, exposed in the defined endpoints of the QuESo Model, and notified to the Analyzer through the Monitor

API.
Analyser: With the EHOS and the values of KHIs from the Monitor, the Analyser component determines whether the EHOS are fulfilled or not; providing an explanation in the latter case denoting which KHIs are violating which EHO. The technique developed in [32] to analyse if a service is provided to the consumer as described in an SLA has been used to analyse if the EHOS is fulfilled. The results are shown to users by means of an appealing grafana-based dashboard. Note that, as occurs with the monitor that notifies new monitored data, the availability of a new analysis result is implemented using an observer pattern which would support to notify any other external component or service such as an automated OSS selector, a higher-level OSSECO Healthy governance platform, etc.

# 4.3. OSS-CARE artifacts 

This section describes in more detail the artifacts that are used to configure and run OSS-CARE to monitor and analyze an OSSECO, namely the QuESo Model and the EHOS.

### 4.3.1. QuESo model

As discussed in the related work, there are several quality models to structure the indicators related to the OSSECO's health [8, 17, 10, 11, 27, 29, 30]. From these existing proposals, this work adopts the QuESo Model [10, 11], because from the four proposals that fulfill dimensions 1 and 2 as reported in the related work section, it is the one conceptually closest to OSS-CARE ${ }^{1}$.

The KHIs in QuESo are organized into three categories: Platform-related, Community-related and Ecosystem network-related. Figure 3 presents an excerpt of the QuESo model presenting some KHIs for the Community-related category.

Regardless of the category, we distinguish among two types of KHIs:

- Low-level KHIs: KHIs that are directly linked to measurable metrics. For instance: number of contributors, open bugs, number of downloads.
- High-level KHIs: KHIs that are the aggregation of other KHIs. For instance: Activeness, Size or Visibility.

In OSS-CARE, the QuESo model has been extended with an endpoint for each of these KHIs, where each endpoint exposes the computed value of the KHI for the OSSECO. To compute these values, OSS-CARE uses the Bayesian Learner, which implements a Bayesian Network following the same methodology used for Software Quality Assurance proposed in [33].

Each KHI has associated two possible states: Low and High, and the probability of the KHI being in one of these two states is computed from the nodes it depends on, following a bottom-up approach:

[^0]
[^0]:    ${ }^{1}$ In fact, this quality model was proposed by one of the research teams authoring this paper.

![img-2.jpeg](img-2.jpeg)

Figure 3: Excerpt of the QuESo Quality Model
![img-3.jpeg](img-3.jpeg)

Figure 4: Excerpt of the Bayesian Network to compute KHIs

- Low-level KHIs are computed directly from measured metrics. The technique to compute the probabilities of low-level KHIs depends on whether historical data is available or not.
- If historical data is available, the values of historical metrics are discretized and probabilities are assigned as described in [34]. It is worth mentioning that Bayesian Networks are known to be robust in the presence of minor gaps in the data [35]. However, when these gaps are substantial, the accuracy and reliability of KHIs may be compromised. To address this issue, existing techniques for handling missing data in Bayesian Networks could be used [36].

- If there is no historical data, the probabilities of low level KHIs can be assigned by domain experts following the method presented in [37].

As a result of this process, measured metrics (e.g., 5 contributors) are converted into KHIs (e.g., the Number of contributors is High with a probability of 0.1 )

- High-level KHIs are computed from other KHIs through the Node Probability Tables (NPTs) of the Bayesian Network. To build these NPTs, a probability wheel or regression methods from empirically collected data can be used [38]. Figure 4 provides an excerpt of the Bayesian Network as an illustrative example. As shown, from a probability of Number of contributors being High at 0.1 , and a probability of the Number of partners being High at 0.4 , the resulting probability of Size being High is computed by calculating the corresponding Conditional Probability Distribution (CPD) of the node, which results in 0.39 .


# 4.3.2. Ecosystem Health Objectives Set (EHOS) 

The EHOS are based on the concept of Service Level Agreement (SLA) in the services domain. In this regard, the proposed EHOS defines a set of conditions over KHIs that should be met to satisfy the requirements of the OSSECO stakeholders.

Unlike SLAs, where conditions are established directly against quality metrics, EHOS support not only the definition of conditions over metrics (e.g. number of contributors), but also logical conditions over KHIs (which are based on probabilistic Bayesian Networks). For example, an OSSECO stakeholder may state that the OSSECO shall be highly active with at least an $80 \%$ of probability (Activeness_high $>80 \%$ ).

The other significant difference is that an EHOS is not a single and agreed document between the OSSECO stakeholders (OSS adopter, contributor, and manager), but rather each OSSECO stakeholder can define their own EHOS based on their specific needs.

EHOs are made concrete as part of a requirements analysis and refinement process with the stakeholders. Following Goal-Oriented Requirements Engineering methods and processes [39], a set of initial generic goals can be elicited and formalized from the high-level KHIs of the QuESO model (e.g., the OSSECO must be highly active). These generic goals can be subsequently decomposed into more concrete goals involving low-level KHIs (e.g., the frequency of releases should be high). This refinement process is supported by the QuESO model, as it identifies which low-level KHIs impact on the elicited generic goals involving high-level KHIs. Finally, well-defined conditions with clear-cut criteria must be specified. This last step can be supported by the knowledge of domain experts and/or historical data (e.g., by looking into the values of the KHIs in periods when the OSSECO was considered highly active). In this work, the specification of conditions have been supported by domain experts through informal conversations with members of the Eclipse community.

In the rest of the section this elicitation process is omitted, providing directly the EHOS for the OSS manager, adopter and contributor given the following generic goals as example:

- OSS manager: An OSS manager may be interested to guarantee that an OSSECO is active, with a high visibility and with a good size.
- OSS adopter: An OSS adopter may be interested in adopting an OSS only if it can be ensured that is is well maintained by an active community and with a good visibility.
- OSS contributor: An OSS contributor may be interested to contribute into an OSS only if is highly visible and with a good size.

Following the aforementioned goals, the different stakeholders may operationalize the corresponding EHOS using an SLA-based language as in the examples below:

OSS manager: Figure 5 shows conditions to guarantee that an OSSECO is active, visible and with a good size:

- The OSSECO shall have and demonstrate a good activity in terms of releases. Such a condition can be implemented by defining that the number of days before the last release should be e.g. below 30 days.
- The OSSECO shall have either a high number of partners (e.g., with a probability higher than $70 \%$ according to the corresponding Bayesian Network), or should be organizing a high number of events (e.g., with a probability higher than $50 \%$ ).
- The OSSECO shall maintain, with a probability of $70 \%$, a good visibility.

```
Objectives:
- Obj1: daysafterlastrelease < 30
- Obj2: numberofpartners_high > 0.7 OR numberofevents_high > 0.5
- Obj3: Visibility_high > 0.7
```

Figure 5: EHOS for the OSS manager
OSS adopter: Figure 6 shows conditions to guarantee that an OSSECO is well maintained with an active community and with a high visibility:

- The OSSECO shall score high in terms of the days after the last commit and days after the last release, e.g. with a probability higher than $90 \%$ and $70 \%$ respectively.
- The OSSECO shall have a high activeness with a probability higher than $70 \%$

```
Objectives:
- Obj1: daysafterlastcommit_high > 0.9 AND
    daysafterlastrelease_high > 0.7
- Obj2: Activeness_high > 0.7
- Obj3: Visibility_high > 0.6
```

Figure 6: EHOS for the OSS adopter

- The OSSECO shall have a high visibility with a probability higher than $60 \%$

OSS contributor: Figure 7 shows conditions to guarantee that an OSSECO is highly visible and with a good size:

- The OSSECO should have a high number of project types (e.g. with a probability higher than $60 \%$ ) and a high visibility (e.g. with a probability higher than $70 \%$ )
- The OSSECO should have a high size (e.g. with a probability higher than $70 \%)$.

```
Objectives:
- Obj1: numberofprojecttypes_high > 0.6 AND Visibility_high > 0.7
- Obj2: Size_high > 0.7
```

Figure 7: EHOS for the OSS contributor

# 5. OSS-CARE in action 

This section describes the process of deploying OSS-CARE to evaluate the health of a particular OSSECO. The reader is referred to Figure 2 for the details of the different architectural elements mentioned in the description below.

1. Deployment of the required Measure Instruments and Wrapping API. In the current implementation, OSS-CARE is able to gather 6 different metrics, namely: DateLastCommit, DateLastRelease, NumberOfDownloads, NumberOfPartners, NumberOfProjectTypes, and NumberOfEvents. The computation of these metrics are supported by the Wrapping API, which currently provides the functionality to retrieve data from GIT, JIRA and HTML data.
Depending on the OSSECO domain, it might be required to implement and deploy new Measure Instruments or extending the Wrapping API with additional sources of information. Both the Measure Instruments and the Wrapping API have been designed in an extensible manner to enable the addition of new metrics and sources of information. The newly

implemented Measure Instruments should provide a RESTful endpoint to expose the monitored data.
2. Instantiation of the QuESo Model. The QuESo Model can be instantiated and tailored to satisfy the needs of the target OSSECO domain. An instantation of the QuESo Model includes the KHIs and the endpoints of the Measure Instruments to collect the monitored data of raw metrics. Finally, the QuESo model is registered in the analyzer of OSS-CARE, which parses the QuESo model and registers the different KHIs as variables that might be included in the conditions of the EHOS.
3. Introducing EHOS within the analyzer of OSS-CARE. OSS-CARE provides an input form to ease the OSSECO participant the process of including the EHOS to analyze (see Figure 8). Thus, at the moment of having enough values for metrics provided by the monitors, the system will show the state of objectives and its comprised metrics in the dashboard.

![img-4.jpeg](img-4.jpeg)

Figure 8: Screenshot of the definition of EHOS

# 6. Evaluation 

### 6.1. Experimental setup

Our proposal is evaluated using Eclipse OSSECO as a use case. We have chosen Eclipse because it is a well-known and well-established OSSECO with a high degree of complexity in terms of teams, projects, and tools used for its management.

OSS-CARE has been deployed following a distributed approach, where the different components can run in parallel and the overall performance is improved. The Monitor of OSS-CARE has been deployed in a server with Intel i7 2.6 Ghz (x4) CPU and 4Gb RAM, whereas the Analyzer has been deployed in another server with a E3-SSD-1-32 - Xeon E3-1245v2 (4c/8th) CPU and 32GB of RAM.

Table 2: KHIs and data sources used


To set up the components, we have applied the different steps described in Section 5, as follows:

1. Deployment of the required Measure Instruments and Wrapping API: For the experiment, we have used the Measure Instruments and Wrapping API already implemented in OSS-CARE.
2. Instantiation of the QuESo Model. The QuESo Model has been defined using the implemented metrics and the following high-level KHIs: Activeness, Visibility and Size. The QuESo Model has been instanciated by including the endpoints of the deployed Measure Instruments to gather the data.
3. Introducing EHOS within the analyzer of OSS-CARE. In this use case, we have defined three EHOS for the three type of participants, namely OSS adopters, contributors and manager. The conditions of these EHOS are the ones presented as illustrative examples in Section 4.3.2, and have been defined based on informal conversations with several Eclipse community members. Although the provided EHOS are not from a real OSS adopter, contributor or manager, we argue that they are illustrative of realistic scenarios.

# 6.2. Experiment results 

The Eclipse OSSECO has been monitored and analysed from 04/04/2021 until 08/06/2021.

During the evaluation, OSS-CARE has monitored the six defined KHIs, four of them on a daily basis (NumberOfPartners, DateLastRelease, NumberOfEvents and NumberOfProjectTypes) and the other two on an hourly basis (DateLastCommit and NumberOfDownloads) yielding to a grand total of over 3300 measures gathered by the Monitor. Table 2 shows the list of sources used to compute these KHIs. For each update on the monitored KHIs, OSS-CARE has analyzed the fulfilment or violation of the different objectives stated in the three EHOS. Although during the whole experimental process we kept the same EHOS, it is worth to remark that those EHOS can be updated at any time.

The complete online results of the fulfillment or violation of the EHOS in the Eclipse OSSECO are available through the Dashboard ${ }^{2}$ of the Analyzer.

Here, a representative excerpt of the analysis for some of the monitored KHIs is presented, highlighting how OSS-CARE is able to monitor and analyze the fulfilment or violation of the specified objectives.

EHOS of the OSS manager: Figure 9 presents a screenshot of the Analyzer for one of the objectives of the EHOS of the OSS manager, namely Obj2, which states that the OSSECO shall have either a high number of partners (with a probability higher than $70 \%$ ), or should have a high number of events (with a probability higher than $50 \%$ ):

Obj2: NumberOfPartners_high $>0.7$ OR NumberOfEvents_high $>0.5$
The chart presented on top of the figure shows the results of Obj2. Three monitoring periods can be distinguished, separated by vertical dashed lines. This is because, there were very brief interruptions of the monitors in which no monitoring data was collected (see section 6.4 for a detailed discussion).

The value " 1.0 " of Obj2 indicates the fulfillment of the objective. Below, the results for its constituent KHIs are depicted. As shown, the NumberOfPartners KHI was roughly stable around 0.9 during all the period (slightly increasing from 0.89 at the beginning of the period to 0.93 at its end). In contrast, the NumberOfEvents, which are events by the Eclipse community where stakeholders sharing an interest in the OSSECO are brought together, presents much more variability, ranging from 0.09 to 0.65 . This is because this latter KHI measures the specific number of organized events (which is highly variable from day to day). As a result of these KHIs, and in particular because the NumberOfPartners KHI was higher than the defined threshold for the whole period, the objective Obj2 was always fulfilled.

EHOS of the OSS adopter: For the analysis of the EHOs of the OSS adopter, the results for all the different objectives are presented.

```
- Obj1: DaysAfterLastCommit_high > 0.9 AND
    DaysAfterLastRelease_high > 0.7
- Obj2: Activeness_high > 0.7
- Obj3: Visibility_high > 0.6
```

A screenshot of the Analyzer for the objective Obj1 of the OSS adopter is depicted in Figure 10. As it can be observed, the objective is never fulfilled during the period under study. Looking at the KHIs of this objective (namely, DaysAfterLastRelease and DaysAfterLastCommit), it can be observed that both KHIs are always below their defined thresholds. It can also be observed that the DaysAfterLastrelease KHI has a short abrupt increase followed by a steady decrease of its value. This is because every time there is a new release in a project, this KHI increases accordingly, and as time goes by without a new

[^0]
[^0]:    ${ }^{2}$ https://ui.osseco.governify.io/render?model=/index/model.json\&view= /index/view.html\&ctrl=/index/controller.js (required credentials: username $=$ viewer password $=$ osseco)

![img-5.jpeg](img-5.jpeg)

Figure 9: Screenshot of the Analizer for the Obj2 of the OSS manager (NumberOfPartners_high $>0.7$ OR NumberOfEvents_high $>0.5$ )
release, the value of the KHI gradually decreases. In contrast, the DaysAfterLastCommit KHI is much more variable, as the frequency of commits varies continuously.

Figure 11 shows the results for the objective Obj2 of the EHOS of the OSS

![img-6.jpeg](img-6.jpeg)

Figure 10: Screenshot of the Analyzer for the Obj1 of the OSS adopter's EHOS (DaysAfterLastCommit_high > 0.9 AND DaysAfterLastRelease_high > 0.7)
adopter. As can be seen, Obj2 was fulfilled only once (by 19/04/2021). This objective is composed of only one KHI: Activeness. It can be observed in the results that the Activeness KHI is highly variable. However, its values are almost always lower than its threshold, defined at 0.7 . This KHI surpassed this threshold only once on 19/04/2021 (which corresponds to the day where the

DaysAfterLastCommit KHI was at its highest point, see Figure 10).
![img-7.jpeg](img-7.jpeg)

Figure 11: Screenshot of the Analyzer for Obj2 of the OSS adopter's EHOS (Activeness_high $>0.7)$

Figure 12 provides a screenshot of the Analyzer for the objective $O b j 3$ of the EHOS of the OSS adopter, which states that the Visibility of the OSSECO should be high with a probability of at least 0.6 . As shown, there are multiple violations of Obj3. This is caused by the high variability of the Visibility KHI (which measures the number of references or mentions of the community on the web on daily basis).

EHOS of the OSS contributor: A screenshot of the Analyzer for one of the objectives of the EHOS of the OSS contributor is depicted in Figure 13. The objective being assessed is Obj1, which states that the number of project types should be high with a probability of at least 0.6 and the visibility of the OSSECO should be high with a probability of at least 0.7 .

```
Obj1: NumberOfProjectTypes_high > 0.6 AND Visibility_high > 0.7
```

This objective is always violated, primarily due to the KHI NumberOfProjectTypes of the OSSECO being evaluated always as close to 0 . This KHI measures the types of projects the OSSECO works on (e.g. IoT, OSGi, mod-

![img-8.jpeg](img-8.jpeg)

Figure 12: Screenshot of the Analyzer for Obj3 of the OSS adopter's EHOS (Visibility_high $>0.6)$
eling), and it is considered very low given the big size of the ecosystem (there are over 400 projects in Eclipse, but only 10 project types). The Visibility KHI presented a higher degree of variability, but was almost always violated.

From the experimental results, we can conclude that OSS-CARE is able to monitor and analyze multiple EHOS. The values of KHIs are computed at runtime, and EHOS violations are detected and reported.

# 6.3. Discussion 

In this section, a brief discussion of some lessons learned from the conducted experiment is presented.

EHOS and highly variable KHIs: Some KHIs present much more variability than others. This needs to be considered when defining the EHOS. For instance, we have seen that KHIs with a high variability may trigger EHO violations that are corrected shortly after (and become violated and corrected again in a repetitive manner). In these cases, it might be appropriate not to consider individual data points, but rather some aggregate values that capture the tendency of the

![img-9.jpeg](img-9.jpeg)

Figure 13: Screenshot of the Analyzer for the Obj1 of the OSS contributor's EHOS (NumberOfProjectTypes_high $>0.6$ AND Visibility_high $>0.7$ )

KHI (e.g. Figure 14 shows the moving average of 50 datapoints of the Visibility KHI).

KHIs variability and monitoring frequency: In the results of the experiments we have observed that, in some instances, some KHIs have remained stable with

![img-10.jpeg](img-10.jpeg)

Figure 14: Moving average of the Visibility KHI
little variation. For these KHIs, it may be appropriate to reduce the frequency of monitoring to save resources (e.g. from a daily basis to a weekly basis). It may also be convenient to actively adapt the frequency of monitoring when the values of these KHIs get closer to the defined threshold.

Definition of the thresholds in the EHOS: In the experiment, we have defined in the EHOS some thresholds for the different KHIs to assess that OSS-CARE is capable of capturing and notifying violations. Even though we argue that the EHOS are illustrative of realistic scenarios, the particular thresholds have been defined based on our expertise and to demonstrate the capabilities of OSSCARE. One of the challenges that an OSSECO stakeholder (i.e. OSS adopter, contributor or manager) may face is how to adequately define thresholds for the KHIs they deem important. In this regard, the stakeholders could use OSS-CARE to obtain historical values of the KHIs in the period in which they considered that the OSSECO was healthy as a reference to define the EHOS. Alternatively, they could also look at the values of the same KHIs applied to other similar OSSECOs for comparison.

# 6.4. Threats to validity 

This section describes the threats to validity in the evaluation.

- Internal validity. The internal validity concerns the design of the experiment and the outcomes observed. In our study, we designed an experiment to test the functional correctness of OSS-CARE. In particular, the capability to monitor the KHIs and detect EHOS violations whenever they occur. The experiment has been run during roughly two months (from 04/04/2021 to 08/06/2021) with multiple EHOS to cover different scenarios. During the execution of the experiment, the monitoring process was interrupted on three occasions (20/04/21, 24/04/21, and 26/05/21) due to server maintenance or updates. While this caused a few data points to be missed, it did not impact the values of KHIs when the monitors were

restarted. However, when the issue was on the monitored side (e.g. inaccessible web page, typos, etc.), it could introduce incorrect measurements. Despite this, Bayesian Networks are known to be robust to occasional measurement errors [35] and only resulted in minor inaccuracies in the computation of KHIs.

- Construct validity. We have chosen a real OSSECO (Eclipse) in order to mitigate any possible threat related to construct validity (e.g., nonrepresentative subjects). The EHOS have been defined based on informal conversations with members of the Eclipse community. While the EHOS provided are not from a real OSS adopter, contributor or manager, we argue that they are illustrative of realistic scenarios.
- Conclusion validity. Conclusion validity concerns our ability to draw conclusions from the experimental results. In this regard, statistical conclusions based on the experimental results have been left out of the scope of the presented work, and the experimental results has been used only to prove the feasibility of the proposal.
- External validity. External validity refers to the generalizability of the results. A potential threat to validity is that OSS-CARE has been validated using a single OSSECO and a more complex scenario requiring more resources might be needed to validate the approach in other, potentially larger, scale settings. However, we argue that the data being monitored and analyzed does not change often (e.g. a few times a day) and hence, we do not expect performance issues in other larger or more complex scenarios.


# 7. Conclusions and future work 

This paper presents OSS-CARE, a fully automatic and real-time framework to assess the health of an OSSECO.

OSS-CARE characterizes the health of an OSSECO through a set of KHIs structured in the form of a Health model. These attributes are then evaluated as KHIs using BN to compute their values. On top of those, KHIs, conditions can be specified in the form of a EHOS, which can be defined by each of the OSSECO participants: OSS adopters, contributors, or managers.

On top of the defined artifacts, an architecture to monitor and analyse the health of an OSSECO has been proposed, adopting some principles derived from SOC. The feasibility of the proposal has been demonstrated by using the Eclipse OSSECO as a use case, providing furthermore, the tool online.

As future work, we plan to extend the list of services to monitor in order to include more data repositories, validate our proposal in other use cases, and apply some of the techniques described that would benefit from the monitoring and analysis of OSSECOs (e.g. OSSECO selection).

# Declaration of Competing Interest 

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work has been supported by the Spanish project PID2020-117191RBI00 funded by MCIN/AEI/10.13039/501100011033; grants RTI2018-101204-BC21, RTI2018-101204-B-C22, PID2021-126227NB-C21, PID2021-126227NB-C22 funded by MCIN/AEI/10.13039/501100011033 and "ERDF a way of making Europe"; grants PYC20 RE 084 US, P18-FR-2895, US-1264651, US-1381595 funded by Junta de Andalucia/ERDF, UE; and FPU19/00666 funded by MCIN/ AEI/10.13039/501100011033 and by "ESF Investing in your future".
