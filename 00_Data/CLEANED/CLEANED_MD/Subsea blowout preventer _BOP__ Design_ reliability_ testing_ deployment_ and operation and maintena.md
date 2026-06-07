# Journal Pre-proof 

Subsea blowout preventer (BOP): Design, reliability, testing, deployment, and operation and maintenance challenges

Mahmood Shafiee, Tobi Elusakin, Evenye Enjema

PII: S0950-4230(19)30542-X
DOI: https://doi.org/10.1016/j.jlp.2020.104170
Reference: JLPP 104170

To appear in: Journal of Loss Prevention in the Process Industries

Received Date: 2 July 2019
Revised Date: 12 April 2020
Accepted Date: 13 May 2020

Please cite this article as: Shafiee, M., Elusakin, T., Enjema, E., Subsea blowout preventer (BOP): Design, reliability, testing, deployment, and operation and maintenance challenges, Journal of Loss Prevention in the Process Industries (2020), doi: https://doi.org/10.1016/j.jlp.2020.104170.

This is a PDF file of an article that has undergone enhancements after acceptance, such as the addition of a cover page and metadata, and formatting for readability, but it is not yet the definitive version of record. This version will undergo additional copyediting, typesetting and review before it is published in its final form, but we are providing this version to give early visibility of the article. Please note that, during the production process, errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.
(c) 2020 Published by Elsevier Ltd.

# Subsea Blowout Preventer (BOP): Design, Reliability, Testing, Deployment, and Operation and Maintenance Challenges 

Mahmood Shafiee ${ }^{1 *}$, Tobi Elusakin ${ }^{2}$, Evenye Enjema ${ }^{2}$<br>${ }^{1}$ School of Engineering and Digital Arts, University of Kent, Canterbury CT2 7NT, UK<br>${ }^{2}$ Department of Energy and Power, Cranfield University, Bedfordshire, MK43 0AL, UK<br>*Corresponding author. Email: m.shafiee@kent.ac.uk


#### Abstract

Subsea blowout preventer (BOP) is a safety-related instrumented system that is used in underwater oil drilling to prevent the well to blowout. As oil and gas exploration moves into deeper waters and harsher environments, the setbacks related to reliable functioning of the BOP system and its subsystems remain a major concern for researchers and practitioners. This study aims to systematically review the current state-of-the-art and present a detailed description about some of the recently developed methodologies for through-life management of the BOP system. Challenges associated with the system design, reliability analysis, testing, deployment as well as operability and maintainability are explored, and then the areas requiring further research and development will be identified. A total of 82 documents published since 1980's are critically reviewed and classified according to two proposed frameworks. The first framework categorises the literature based on the depth of water in which the BOP systems operate, with a subcategorization based on the Macondo disaster. The second framework categorises the literature based on the techniques applied for the reliability analysis of BOP systems, including Failure Mode and Effects Analysis (FMEA), Fault Tree Analysis (FTA), Reliability Block Diagram (RBD), Petri Net (PN), Markov modelling, Bayesian Network (BN), Monte Carlo Simulation (MCS), etc. Our review analysis reveals that the reliability analysis and testing of BOP has received the most attention in the literature, whereas the design, deployment, and operation and maintenance (O\&M) of BOPs received the least.


Keywords: Oil and gas; Blowout Preventer (BOP); Deepwater; Design; Reliability; Testing; Deployment; Operation and Maintenance (O\&M).

# 1. Introduction 

In the process of drilling a well for oil and gas, the wellbore is usually lined with a casing through which a drill string runs. The annular (ring-shaped) region between the casing and the drill stem is filled with drilling mud which provides hydrostatic pressure to restrict formation fluids (oil/gas) from coming up the wellbore. When a drill bit punctures a hydrocarbon reservoir, underground pressure forces formation fluids into the wellbore. Throughout the drilling process, these fluids try to force their way through the annulus. Primary well control during drilling is achieved through a counterbalance of reservoir pressure by hydrostatic mud pressure. The appropriate safety margin is achieved by varying the fluid density. When this pressure is lost during a kick, the Blowout Preventer (BOP) is employed as an alternative.

As a large specialized, mechanical array of valves, assembled to seal wells against kicks or blowouts during drilling or work-over operations, a typical BOP consists of Lower Marine Riser Package (LMRP) and a combination of several types of preventers, differing in number and capacity principally for operational reasons. Figure 1 shows the conventional and modern BOP systems with their main components including: connectors (wellhead and LMRP), BOP control system, flex joint, annular preventer (upper and lower), ram preventers, choke and kill system.

## ** Figure 1 **

Figure 1. (a) A conventional BOP and (b) a modern BOP.
Based on operators' choice, BOP subsystems may differ in number, size and capacity, particularly so as exploration in deeper water is seemingly the most prospective way forward [1]. Aside the failsafe function of monitoring and maintaining well integrity, BOP system's primary functions are: (i) to confine or seal off well fluids in the well bore; (ii) to provide means of adding or withdrawing controlled volumes of fluid to and from the well bore; and (iii) to shut or 'kill' the well and seal the wellhead.

The annular or ram preventers with their associated components seal and/or shear the wellbore and its contents through hydraulic power stored and launched from accumulators. Hence, importance of the seals cannot be overemphasised. Connectors link the entire assembly to the wellhead and to the riser which is directly hooked to the drilling platform, whereas the choke and kill system are laden with valves, lines and hoses in order to safely transfer fluids to and from the system. A pilot control system consisting of modular pods is also embedded within the LMRP for essential control functions.

The BOP has maintained the all-important function of a drilling safety barrier since its discovery in the early 1900s. Due to its robust nature and complex assembly, little modification has been made since its entry into the oil and gas market and its acceptance as last line of defense for any drilling or workover operation. However, as oil and gas exploration moves into deeper waters and harsher environments, the setbacks related to reliable functioning of the BOP system and its subsystems remain a major concern for researchers, operators and other stakeholders in

the industry. The BOP system failures usually result in injury/loss of life, economic losses, environmental damage and possible damage to oil reservoir [2, 3]. According to [4], 65\% of blowouts occur through the BOP, either through the drill string or the annulus. An efficient way to avoid blowouts is to improve design, reliability, testing and certification, and operation and maintenance (O\&M) of BOP systems.

This study aims to systematically review the current state-of-the-art and present a detailed description about some of the recently developed methodologies for through-life management of the BOP system. The challenges associated with the BOP system design, reliability analysis, testing, deployment, as well as its operability and maintainability in the oil and gas industry are identified, analyzed and discussed. For this purpose, a total of eighty-two (82) documents published since 1980's are critically reviewed and classified according to two proposed frameworks. The first framework categorises the literature based on the depth of water in which the BOP systems operate, with a sub-categorization based on the Macondo disaster. The second framework categorises the literature based on the techniques applied for the reliability analysis of BOP systems, including Failure Mode and Effects Analysis (FMEA), Fault Tree Analysis (FTA), Reliability Block Diagram (RBD), Petri Net (PN), Markov modelling, Bayesian Network (BN), Monte Carlo Simulation (MCS), etc. The areas requiring further research and development will also be identified and discussed.

The rest of the paper is organized as follows. A brief description of the reviewed literature on the challenges associated with safe and reliable operation of BOPs is given in Section 2. The reliability analysis techniques applied for the reliability analysis of BOPs are presented in Section 3. Section 4 contains the analysis and discussions of the findings, and Section 5 concludes the study and provides future research directions

# 2. The reviewed literature 

This section attempts to review systematically the papers published about the challenges associated with safe and reliable operation of subsea BOPs. The review focuses on identifying drawbacks and areas of amelioration with regards to system safety and reliability as well as the techniques applied to analyze and improve the device maintainability. This implies that documents relating to other aspects such as overall functioning, historical development, general design, etc. are not inclusive. All relevant sources of literature were identified through keyword searching of databases. These sources included journal articles, conference proceedings, technical reports and governmental documents published since 1980's. Publications in languages other than English and text books and dissertations were excluded from the review.

Due to the varied nature and extensive scope of documentation, we propose two frameworks to classify the reviewed sources. The first framework is based on safety and reliability challenges identified in shallow water ( $<500$ ), deep water ( $>500$ ), or general related issues. The second framework categorises the literature based on the techniques applied for the reliability analysis of BOP systems. The classification based on water depth indicates that the research methods and findings in the document are specifically within the said boundaries. The classification 'general'

will indicate any other research with no such specific boundaries but related and within the scope of analysis. Within each category, sub-divisions are identified relating literature prior to or after the Macondo disaster in the Gulf of Mexico (GoM). Investigations and research into this event has sparked a rapid evolution in safety, risk and reliability awareness of BOPs and the oil and gas industry in general.

# 2.1 Deep and shallow waters 

Despite the outlined importance of the BOP, technological advancement in the petroleum industry in general has actually been a forced issue, mainly in response to business needs [5]. Drilling success rates in conventional deep water ( $>500 \mathrm{~m}$ ) seemed to have peaked recently [6] and advances in ultra-deep (UD) zones ( $>1500 \mathrm{~m}$ ) are increasingly economically feasible. Worth noting is the fact that approximately 58 billion barrel of oil equivalent (BBOE) have been discovered in deep waters, with more than half the amount found after 1995 [5]. Drilling and exploration have taken a massive leap into deep and UD waters. This affects general operation and handling of BOPs as manufacturers now face the inherent challenge of modifying the device to fit new environments, without compromising reliability.

BOPs in the 1950s were simple 11", 3000psi rated devices, working for a few days in depths of about 1500ft. Nowadays, newly discovered deep and UD oil fields require up to 20,000psi rated 18 3/4" BOPs [7], capable of lasting for the life of the well. Size notwithstanding, unexplored terrain in new water depths present unique challenges and peculiar difficulties [8]. UD waters are characterized by high pressure, high temperature (HPHT) zones, gas pockets, and increasing amount of hydrogen sulphide $\left(\mathrm{H}_{2} \mathrm{~S}\right)$, with associated reliability problems such as infant mortality, depth/pressure sensitivity, environmental corrosion/erosion, salt water ingress and design performance failures [9]. According to [10], problems associated with the increase in water depth include: weather problems, mechanical failures of subsea equipment, wellbore instability, formation and cementing issues and specifically, BOP challenges. Blowout control in these new environments has not been mastered and is often handled reactively. These issues have shaped recent BOP research as greater reliability and availability are more than ever, highly desirable. Operators and other industry partners seek to cut down the inevitable costs associated with deeper water operations without compromising the reliability of the device.

### 2.2 Pre and post Macondo disaster

The Macondo disaster that left the GOM coast flooded with more than four (4) million barrels of oil and the loss of 11 lives [11] resulted in a re-examination of the 'safe' perception of the oil/gas industry and the one of its principal safety equipment, the BOP, in particular [12]. Investigations after the disaster revealed several pitfalls within the device, which could have simply been overlooked or minimised prior to the April 2010 event. This has since led to rapid evolution of both prescriptive and performance-based regulations and safety management system requirements governing the BOP and the industry at large. A brief summary of the BOP challenges in deep waters, shallow waters and general is provided in Table 1, Table 2 and Table 3 , respectively.

# ** Table 2 ** 

Table 1. Classification of BOP Challenges (deep-water related)

## ** Table 2 **

Table 2. Classification of BOP Challenges (Shallow water related)

## ** Table 3 **

Table 3. Classification of BOP challenges (General)
With regard to the oil and gas industry, regulatory changes started with the dissolution of the Mineral Management Service (MMS) - which had been in charge of the safety and security of operations on the outer continental shelf (OCS) - and its replacement with the Bureau of Ocean Energy Management (BOEM) and Bureau of Safety and environment enforcement (BSEE) [86]. Changes were also made to the drilling safety rules, worst-case blowout response and wellcontainment measures [87]. The Macondo incident also had a profound impact on theoretical research. In the wake of the accident, the amount of research performed focusing on the reliability of offshore drilling assets and more specifically, BOP reliability, increased markedly as the BOP increased in relative significance. Going by the sheer volume, the amount of research performed on BOP reliability in the ten years following the Macondo incident greatly exceeds the amount of research performed in the three decades prior.

## 3. BOP reliability analysis techniques

This section reviews the results of the classification framework based on the techniques adopted for reliability analysis of BOP systems. Only literature with subject matter relating to BOP reliability analysis have been included in this classification. The purpose of this framework is to better categorize existing research and ease further studies in BOP reliability analysis.

In response to recent events in the industry, a lot of attention has been shown to the reliability of BOP systems. However, the research on the topic is still lacking in some regard [70]. The reliability assessment of subsea BOP systems has come a long way since Holand and Rausand [33] used a combination of drilling, BOP test, well and equipment failure reports and applied Fault Tree Analysis (FTA) as a means of reliability assessment. Some years later, Fowler and Roche [42] applied FTA and Failure Mode and Effects Analysis (FMEA) to assess the reliability of a subsea BOP and a hydraulic control system. Reliability Block Diagrams (RBDs) were also used by Zou et al. [74] to model the reliability performance of subsea BOPs and then the results were compared against design requirements. Some advanced reliability analysis techniques which provide more robust solutions have also been applied in recent years, however, gaps still exist with regards to incorporation of maintenance strategies and dynamic operating condition of the BOPs.

The reliability analysis techniques discussed within this review focus on the application to subsea BOPs and their components. The following subsections give brief summaries on each technique.

# 3.1. Failure mode and effects analysis (FMEA) 

The application of FMEA as a technique to assess system reliability dates back for at least five decades and its use and effectiveness in a myriad of industries is well documented. The FMEA process begins with a qualitative analysis of the system in question and its functions followed by a quantitative analysis which explores each component, identifies their failure modes and determines the effects of those failure modes on the overall system. A risk priority number (RPN) which serves as a means to prioritise and rank the identified risks is developed. It considers three factors: severity of impact (S), likelihood of occurrence (O) and likelihood of detection (D) [88]. Though it has been criticized on multiple occasions over time on account of the RPN, as a reliability assessment technique, it has quite a number of advantages which help justify its use. The FMEA technique can be used to identify failure modes and evaluate risks early in the design process, it ensures that risks are comprehensively identified and categorised, and it helps the analyst determine the system's functional vulnerabilities [89]. The FMEA technique has been applied a number of times towards analysis of BOP reliability in literature. The technique was applied in [53] towards three BOP reliability analyses performed on specific BOP components. Shafiee et al. [79] also discussed its application in conjunction with FTA in order to perform risk analysis on a subsea BOP. When a criticality is involved, the analysis is referred to as Failure Mode, Effects and Criticality Analysis (FMECA).

### 3.2. Fault tree analysis (FTA)

The fundamental theory of FTA is the conversion of a system into an organized logic structure (Lee et al., 1985). Over time, its definition has evolved to being a diagram which depicts the relationships between a possible critical event in the system and its causes [90]. In terms of system maintenance, FTA allows operators identify and then qualify the initiating failure causes that will help set the stage for developing a maintenance program fit to maintain system reliability at the required level [91]. There are two types of nodes which make up a fault tree, namely: the event nodes and gate node. Events can be either basic (meaning they cannot be deconstructed into smaller events) or intermediate (meaning they are represented as a combination of basic events and other intermediate events) [92]. The types of gates include the AND gate (which represents the combination of all inputs to produce the output event) and the OR gate (which represents the existence of the output provided at least one of the input events exists) [93]. Performing FTA consists of the following steps [94]:

- System and boundary definition;
- Fault tree construction;
- Minimal cut set definition;
- Qualitative analysis;
- Quantitative analysis.

The FTA technique has been applied for the analysis of BOP reliability in a number of studies. Holand and Rausand [33] used it in conjunction with failure reports as a means of assessing the reliability of subsea BOPs. Mutlu et al. [84] performed a qualitative FTA to assess the reliability of a BOP control system. In another study, Zhang et al. [77] discussed its application in combination with fuzzy analysis theory to determine the reasons for failure of an annular BOP.

# 3.3. Markov modelling (MM) 

The Markov method is a modelling technique applied to analyse the reliability of fault tolerant systems [95]. It depicts the system to be analysed using state circles and transition arcs which form a Markov transition diagram. The Markov method is known for being flexible and has been noted in several literature as being uniquely suitable for reliability assessment of redundant systems such as BOP [96]. It also is a very suitable technique to solve dynamic problems which conventional reliability analysis techniques such as FTA and FMEA cannot deal with. The Markov chain, which is a stochastic process that possesses a Markov property, is used to model multi-state systems as well as the transitions between the states. It can be described as discretetime or continuous-time depending on the time variable for a particular process [90]. The Markov method does have its shortcomings. For instance, it can be quite tedious to determine transition rates due to lack of data. Also in some complex systems, it is very possible that some states and transitions are omitted when defining both elements [97]. In literature, Kim et al. [63] applied the Markov modelling to reliability analysis of subsea BOPs by considering demand rate for its components.

### 3.4. Monte-Carlo simulation (MCS)

Monte Carlo simulation is one of the most commonly used tools for reliability analysis of engineering systems. This is due to its independence from the complexities of the problem it is trying to solve [98]. The main drawback associated with MCS is its inaccuracy and inefficiency in dealing with very small failure probabilities. To overcome this shortcoming, subset simulation (SS) was developed. SS is a simulation tool used for handling small failure probabilities. This technique was developed as a result of the apparent inefficiencies associated with using direct MCS to compute reliability problems which contain small failure probabilities [99]. Using SS requires expressing the failure probability of the event in question as an amalgamation of chosen smaller probabilities [100]. SS has been applied to different engineering systems such as reliability of subsea pipelines [98], dynamic stiffness of large offshore wind turbines [101], and so on.

### 3.5. Petri Net (PN)

The PN concept, which was developed by Dr Carl Petri as part of his PhD dissertation, is a reliability method applied to modelling and assessment of non-deterministic, parallel systems [64]. As an extremely versatile technique, it can be used to evaluate redundant systems, manufacturing systems, and safety-critical elements, among others [57, 102, 103]. The technique

can be used as a graphical tool - for aiding visual communication, and as a mathematical tool for developing mathematical models which govern the behaviour of systems [104]. There are four main modelling elements which make up the PN. These include: places, arcs, transitions and tokens. Places are denoted by circles, transitions by rectangles, tokens by solid circles which are located inside places and arcs connect places with transitions. There are multiple variations to the PN technique such as the coloured petri net (CPN), the stochastic petri net (SPN) and the deterministic and stochastic petri net (DSPN). The SPN is very suitable for complex dynamic systems such as the BOP due to the fact that it explicitly introduces the time parameter [105]. In a recent study, Elusakin and Shafiee [106] applied the SPN technique to analyse the reliability of subsea BOPs with different failure modes subject to condition-based maintenance (CBM).

# 3.6. Bayesian Network (BN) 

According to Langseth and Portinale [107], BN is a compact representation of a multi-variate statistical distribution function. The BN technique has recently come into prominence as being a more robust and viable alternative to the conventional reliability assessment techniques such as FTA and FMEA [70]. This is mainly due to the fact that BN can perform predictive as well as diagnostic analyses [51]. For reliability assessment, BN models are developed by converting and building on the conventional reliability models. A BN model is made up of qualitative and quantitative sections. The qualitative section is a directed acyclic graph (DAG) containing nodes and arcs which denote the system variables and their dependencies respectively. The quantitative section highlights the connections between each node and its parents through a conditional probabilistic table [55]. Variations to the BN technique can be applied to evaluate system reliability evaluation depending on the type of system and operating circumstances. For example, dynamic Bayesian networks (DBNs) is applied when temporal features are involved in reliability analysis. Object-oriented Bayesian networks (OOBNs) are appropriate for analysing the reliability of sizeable, complex structures. Dynamic object-oriented Bayesian networks (DOOBNs) are used to analyse degrading components as well as repetitive systems [108]. The BN technique has been applied to BOP system reliability analysis in a number of studies. Readers can refer to $[56,58,67,68,83]$ for further reading.

### 3.6. Reliability Block Diagram (RBD)

RBD is a graphical framework in the form of block diagrams which represents how functioning components of a system form logical connections to complete a specific system function. It is suited mainly to non-repairable components and scenarios where the order in which failure occur is not important [90]. RBDs have three main structural configurations: series, parallel and a mixture of the two. A series configuration represents all the blocks (or components) being required to work for the system to function. A parallel configuration represents only one component being required for the system to successfully function. A prime example of this is component redundancy. A mixture configuration is used to represent more complex models. An example of this being if a series system gets duplicated or made redundant. RBDs depicting system reliability are more often represented as a mixture of series and parallel structure

configurations [109]. In literature, the RBD technique has been used as part of reliability analysis to ascertain the impact of testing, inspection and maintenance actions on the BOP availability [110].

Table 4 shows the distribution of published literature among the different reliability analysis techniques discussed.

# ** Table 4 ** 

Table 4. Distribution of the literature by BOP reliability analysis techniques.

## 4. Observations and findings

### 4.1.Observations

From the documents reviewed, prominent challenges associated with the BOP can be grouped into three principal categories: design, deployment, and operation. Design challenges are mainly related to sealing, shearing, and accumulator issues; deployment challenges are associated with recent developments in BOP technology; and operational challenges are related with the testing, inspection and maintenance, and extreme operating or environmental conditions. These three categories are addressed in more detail in the following sections:

### 4.1.1. Design challenges

## - Sealing elements

Due to their soft, nearly incompressible elastic properties, complex elastomeric polymers which are the main components of seals are used to support deformation and compression in different preventer types. According to API SPEC 16A [115], these polymers must be capable of sealing and preventing leaks. However, leaks are common and generally associated with inappropriate elastomer selection [116, 117]. High temperature nitrile elements in packer seals have a limited useable temperature range [118] and are subject to extrusion and abrasion. Though largely elastic, they undergo stress relaxation, creep, damping and increased stiffness with frequency of loading, likely to worsen in unpredictable environments.

Surrounding drilling conditions usually affect seals in two major ways: chemical degradation under high temperatures or stiffness/brittleness, and swelling due to fluid absorption after prolonged exposure. Since abrasion and extrusion cannot be totally avoided in specific parts like elastomeric ram packers, degradation rates are simply reduced to achieve the desired sealing property [40]. Material selection for specific applications, fluid compatibility and operating conditions on a holistic platform is necessary for increased reliability in deep and UD waters.

## - Shearing capabilities

Blind and casing shear ram preventers are fitted with blades, to cut through different tubing types, and seal off a well. Failure to shear is not very common [10]. However, as drilling advances into UD waters, drill pipe properties such as material strength, toughness and ductility are continuously improved to reduce drill pipe failure and increase life span, which result in

increased shearing force requirements. Studies attribute failure-to-shear to material composition [119] and other increasing exogenous parameters include drilling fluid density and shut-in pressure. Inability to cut through drill collars, drill bits, tool joints, connectors and other drill pipe attachments are not uncommon. According to [120], the Bureau of Safety and Environmental Enforcement (BSEE), after several months of investigation, recognized the importance of the BOP being 'shear certain', a requirement which may well become part of developing industry regulations. Though current BOP designs are ambiguous, industry is predisposed to achieve this goal. Laser application, stronger bladders, use of explosives, greater hydraulic cutting pressure, are all technologies under study. New shear ram designs are already available in the BOP markets [121]. Some companies like Shell and BP have started the implementation of two blind shear rams in one stack arrangement [120] as a means to ensure shearing/sealing, hence improving reliability though it is a more costly option due to mobility and weight challenges. The manufacturing of strong yet shear-able drill collars (thinner skins and lead centers) is another feasible solution [3].

# - Accumulator design and capacity 

One way to tackle the vagaries of UD environments is to modify the distance and number of accumulator bottles. The further accumulator bottles are located, the lower the usable fluid volume per accumulator bottle [23], as actuation pressure reduces with distance travelled. When accumulator bottles are used, communication must be established with control pods via control lines. Reaction time for different line diameters varies and operates by a power law relationship. A small diameter control line at 400 feet may react anywhere within 1 and 10 seconds in depths of 3000 feet [122], increasing command-to-completion time. Many techniques have been developed to solve this problem when the BOP is connected to the riser.

In emergency situations, the act of shearing or dropping the drill string may become mandatory if rig control is lost and a functional BOP with sufficient accumulator volume should be able to complete this task. In deep and UD water depths, the accumulator bottles could become prohibitory due to increased expense and floater capability to handle such large LMRPs. At these depths however, charging and replenishing accumulator canisters can only be done by remotely operated vehicles (ROV) intervention, an area of continual questionable reliability [123]. As the Emergency Disconnect System (EDS), Deadman switch and blind shear rams depend solely on the proper functioning of hydraulics, independence from main controls in the event of blackouts and loss of power are vital.

### 4.1.2. Deployment challenges

Commissioning and decommissioning of BOPs are fairly simple with on-board cranes and hoisting systems in shallow waters. In deep-water locations, the project's cost and schedule contribute immensely to overall installation activity. A winch with $20 \mathrm{~m} /$ minute speed for deployment at 2500 m water depth is likely to span an entire day for installation and recovery process [124] and even more so in adverse met-ocean conditions. All the more, recent inevitable redundancy and increased safety measures have created a weight and size footprint in subsea

hardware. Modern BOPs are much larger and heavier than conventional ones. They weigh about 450 tons and have 60 feet of height [61]. Typical deep water fields also comprise of several blocks and reservoirs in extensive areas, making installation and maintenance costly and timeconsuming. Three factors are of primary concern with regards to subsea deployment: handling technology, load control and positioning, and met-ocean and weather effects.

In recent years, the third and fourth generations of BOP systems have become popular. The new systems employ casing risers in place of flexible tube risers and a Subsea Isolation Device (SID), placed on the seabed [123]. A Subsea Deployment System (SDS) has also recently emerged, making use of a fully floodable solid buoyancy hull with chains attached to float equipment being deployed in water [125]. Though it is said to save cost and time with low risks for transporting heavy equipment in deep water and harsh environments, weight limitations make it difficult to operate beyond a limited water depth. Positioning issues such as dynamic responses, positioning reference issues, soil conditions etc. are also worth considering.

# 4.1.3. Operational challenges 

In spite of having high availability levels [34, 96], BOP failures are continually reported and the device does not seem to work properly when required [126]. In the Macondo disaster, though the device had been tested some days earlier and deemed fit for purpose, it failed in a similar sequence to most oil and gas disasters [127]. Subsea operating conditions have now gone beyond those specified in 30 CFR 250.517 [128], API 17N [129], API RP 53 [130] and API SPEC 16A [115]. Standard development and compliance activities lag behind the increasing pace of technology development [131]. The rewrite of API RP 53 [130], which is coded as API STD 53 [132] remains a major regulatory milestone and places additional strength to the articulated requirements [54]. Industry has now realised that a high level of reliability and integrity is a key requirement for the operation of subsea systems [133].

## - Environmental conditions

New operating environment remains a fundamental challenge, flooded with high gas-oil ratios, HPHT regions, elevated tides and wave currents, difficult formations and even lack of experienced personnel [97]. Since 1992, more than 1,500 wells have been drilled in water depths exceeding $500 \mathrm{~m}(1,500$ feet) and approximately 320 wells were drilled in water depths greater than $1500 \mathrm{~m}(5,000$ feet). Safety and environmental concerns are not limited to deep water but stakes are relatively higher in deep waters compared to shallow waters since costs of mishap are proportionately higher.

BOPs were used on conventional land mines till hydrocarbon deposits were discovered on the ocean floors. These devices translated their safety and control function to land rigs which were mounted on barges several decades ago. This became common practice for jack-up rigs as drilling moved to shallow waters and extended depth capabilities to about 650 feet. Then, semisubmersible rigs and drillship evolved, moving water depths to 1,500 feet and the BOP to the seabed. This move enabled the use of low pressure and less expensive risers to connect and transport the drill fluid back to the rig. This flexibility helped industries develop capabilities of

drilling rigs in locations with depth of 10,000 feet [134]. However, the initial advantage of cost savings has phased out over the years as greater depths have different requirements.

# - Testing, inspection and maintenance 

Minimal exogenous risk analysis is carried out during the operational life of a BOP. The cognizance of changing environmental conditions will certainly alter the outlook on testing, inspection and maintenance specified by API RP 53 [130] and BSEE 30 CFR 250.517 [128]. The claim that continuous usage and testing of the BOP will cause wear, therefore sometimes accounting for failure [34], is not uncommon and is possibly the reason for its usage only as a 'last' resort during incidents. Subjecting BOPs to high pressure testing may cause wear, vibration, leaks and fracture which, if not properly maintained and monitored, can result in a disaster. However, tests are essential to ascertain proper functioning and maintenance procedures. Financial implications of about 5\% of drilling time [17] notwithstanding, tests cannot be overlooked. There remains a possibility that due to above mentioned factors and other human limitations, test procedures are generally neglected by the drilling crew and/or regulatory bodies.

Ram locks are a vital part of ram block in a BOP system and a classic example of a component which is not usually tested. API SPEC 16A [115] does not require testing of these locks when manufactured. API qualification pressure and sealing tests are carried out on new BOPs like other pressure containment equipment and rated solely on bore size and design. No reference to external loads or water depths are provided [25]. According to these specifications, a good BOP test means no visible leaks. Local bearing stress and fatigue calculations are also not considered. Many such leaks are not detected due to high pressures employed in today's large BOPs. Visual inspections are necessary to detect leaks and should be carried out by personnel who know where to look within the system. Progressing from a repair-on-failure philosophy, maintenance is an obvious tool for improving reliability. Eliminating data acquisitioning difficulties in the oil and gas industry will make Reliability Centred Maintenance (RCM) more applicable. Maintenance logbooks may become necessary for the BOP system as well as its components in the oil and gas industry. The amount of time between BOP repairs may need to be regularly recorded. Incorrect, insufficient, inefficient and untimely maintenance may be the trigger to barrier failure [135].

Though commonalities such as risk-based inspection (RBI) and robotic inspection technologies exist, the use of non-destructive testing (NDT) techniques will enhance the performance of BOPs in deeper waters [9, 136]. Techniques such as vibration analysis, infrared thermography, acoustic emission and ultrasound analysis can be adapted for BOP inspection [137]. Though vibrational analysis is costly and invasive, infrared thermography, acoustic emissions and ultrasound analysis are non-intrusive and can provide data on a more real-time basis. However, the infrared and acoustic based techniques are more susceptible to error and the ultrasound analysis requires more thorough understanding. These techniques, among others already play a role in the maintenance of offshore drilling assets and are poised to be applied to subsea BOP maintenance in the future [85].

In order to test basic functionality of the BOP control system, its software is subjected to extensive regression testing which leads to unwanted errors. To overcome this, the hardware-in-the-loop (HIL) testing methodology, which is a staple in the aerospace industry can be applied [138]. HIL testing involves the integration of actual working equipment into a simulated environment and this can be used to test the BOP control system software without adding unnecessary new functions or modifications [139].

# - Reliability 

With reliability being a foundational attribute for the safe operation of BOPs, ensuring and maintaining high system reliability constitutes a fundamental challenge. Reliability analysis is therefore performed to address the protective barriers of the BOP components. The BOP, being a modern drilling system, is mainly constituted of hardware, software, human and organisational elements. The combination of these factors coupled with the focus on failures relating to hardware and software raises the relative significance of errors which occur in human and organisational elements. In addition, complex operational tasks such as maintenance must not just be performed for its own sake, but to ensure consistency between BOP reliability characteristics and production as well as regulatory directives [140].

### 4.2. Review findings

Critical analysis of the literature reveals the current state-of-the-art in subsea BOP operational safety, any progress achieved, and exposes areas requiring further regulatory, design and research ameliorations. More so, it is clear that there has been increasing attention, particularly after 2010, on the safety of subsea BOPs, emphasising the wake-up call by the Macondo disaster.

Pre-Macondo concerns related to the BOP are limited to overall reliability. External leakage, failure to seal, and lower reliability of surface preventers [40] account for approximately $53 \%$ of the reviewed documents. Post-Macondo however has witnessed a slight shift in focus. The years following the disaster has witnessed major regulatory changes, several joint industry projects and even a complete re-write of the API RP 53 [130], now API STD 53 [132]. Researchers have intensified concerns with regards to real-time monitoring [141, 142], risk monitoring [143] and modelling [114].

Continual refining of design elements such as shearing blades and sealing elements are paramount in UD drilling. Active component redundancy and even entire system replacement spares are gaining increasing interest in the industry. The hydraulic control system, ram preventers, and hydraulic connectors fail more frequently and require unabated design amelioration as understanding of the new oceanographic conditions is gained. More so, aspects discussed herein are largely analogous and intermittently affect each other. Design improvements such as active redundancy may create a weight/size footprint, which in turn affects deployment. This implies BOP challenges, though diverse and far reaching, should be treated in a consolidated fashion.

About twenty-five percent of the reviewed literature focused on deep-water related issues, whilst little attention has been paid to shallow water issues specifically post-Macondo. It is

however important to note that the documents classified as 'general' specific reference were not made to either deep or shallow water but they may still be applicable in either case. Several factors may be responsible for this but principally, by 2010, focus had greatly shifted to deep and UD waters. Aside individual research, significant efforts were made by bodies such as the Foundation for Scientific and Industrial Research at the Norwegian Institute of Technology (SINTEF) (https://www.sintef.no/en/), the U.S. Mineral Management Services (MMS) which is now Bureau of Ocean Energy Management (BOEM) (https://www.boem.gov/) and Bureau of Safety and Environmental Enforcement (BSEE) (https://www.bsee.gov/).

Other findings in terms of failure prone subsystems, common-cause failure and component redundancy and conventional and advanced reliability analysis techniques for subsea BOP systems are also discussed in followings.

# - Failure prone subsystems 

Studies reveal that some BOP subsystems fail more frequently and impair the overall reliability of the device. According to Holand [34], a study of 188 inch, 10000-15000psi rated subsea BOPs between the years 1978 and 1989 revealed that annular preventers, choke/kill lines and the hydraulic control system contributed approximately $79 \%$ of rig downtime. Choke/kill lines and the hydraulic control system experienced majority of failures within the study period. Other contemporary studies [62, 110] employing the Offshore and Onshore Reliability Data (OREDA) (https://www.oreda.com/) as data source agree in many ways with the latter. Slight variations are presented again by Holand [44], where deep-water wells ( $>1312 \mathrm{ft}$ ) in the Gulf of Mexico were studied and main data sources included daily drilling and BOP test reports. Ram preventers seem to fail on a similar scale to control systems and choke/kill valves. Cai et al. [96] validated these results, proving that ram preventers, annular preventers, LMRP connector and wellhead connectors were the main components responsible for stack failure whilst the upper annular preventer, control pods and LMRP connector require greater maintenance effort. Pareto analysis of the results showed the subsystems that require urgent design improvement. Over time, research and innovation programs have employed system and component redundancy to improve BOP reliability. Control pods, annular preventers, ram preventers, control stations and several valves are all redundantly configured for this purpose [64].

## - Common-cause failure and component redundancy

Common-cause failures have proven over time to have a dominant impact on accidents [51]. Redundancy in BOPs was an issue in the past when unique valves and other controls operated major mechanisms within the system. To enhance the reliability characteristics of a coherent system, redundant components may be provided, using active redundancy for component redundancy or system redundancy. Nowadays, rigs equipped with spare BOPs are common [94]. Industry introduced backups into the BOP system but over the years, due to weight, space and other considerations, modern systems, especially control systems incorporate less redundancy. Generally, the control stations, control pods, annular preventers and ram preventers are redundantly configured. However, the entire system can be considered as a series system, since

the failure of any major component category results in the failure of the entire system. A single failure in the hydraulics may cause total loss of control and such problems have been observed in the past [144]. Common cause failures of various existing redundant devices in the control system of the subsea BOP are known to reduce the reliability greatly [51]. Attempts to activate the Deepwater Horizon shear ram as well as the EDS failed as a result of the failure of other systems, resulting in a complete failure of the BOP.

# - Conventional and advanced reliability analysis 

Conventional reliability assessment methods have their own drawbacks. According to Bai and Bai [145], complex systems are difficult to model using the RBD technique and computing the system's reliability numerically can be a time-consuming task. Both the FTA and FMEA techniques only work well for non-repairable systems and do not possess a time element, a characteristic which is extremely important when analysing subsea systems such as the BOP. In addition, the FMEA cannot differentiate a situation of common-cause failures or severe failures caused by compound failures and the FTA technique itself is not suitable for analysis of sequential events [64]. Advanced reliability techniques such as Petri Net (PN), Markov Method, Bayesian Network (BN), Monte-Carlo Simulation (MCS) and their different variations have been developed and applied to assess the reliability of subsea BOPs. These advanced techniques help overcome some of the drawbacks of the conventional reliability assessment techniques [146]. The BN technique for example has come into prominence recently as being a more robust and viable alternative to the conventional reliability assessment techniques [70]. The Markov Method technique as well as the semi-Markov method are regularly used to evaluate complex systems such as the subsea BOP due to their flexibility in representing the dynamic behaviour of the system [94]. The PN technique is a numerical and graphical tool used to model asynchronous, simultaneous, distributed and parallel systems [103]. One of its variations, Stochastic Petri Net (SPN) is very suitable for complex dynamic systems because it explicitly introduces a time parameter [55].

## 5. Conclusions and further works

Despite the economic challenges in the current oil and gas market, the prospects of this resource remaining the world's main energy supplier are huge. Economically viable fields are still being discovered in waters of greater depths and unexplored terrain. This, however, raises questions regarding reliability, particularly that of the all-important drilling safety device, the blowout preventer (BOP). This paper aimed at identifying, in a consolidated fashion, pertinent issues affecting the BOP device reliability, particularly so in a post-Macondo era. Eighty-two (82) documents expounding these challenges between the years 1980 and 2019 were systemically reviewed. Major challenges and issues associated with the device design, reliability analysis, testing, deployment as well as operability and maintainability were identified. These issues are further discussed in the paper as they are deemed critical, not only affecting the safe and proper

functioning of the BOP but also incurring significant capital expenditure (CAPEX) and operating expenditure (OPEX). The findings from critical review of literature include the following:

- Reduced design, installation and operational costs as well as increased safety and better reliability are all benefits that can be accrued from critical assessments of the identified challenges.
- There has been increased attention, particularly after and as a result of the Macondo disaster on the safety of subsea BOPs.
- Some BOP subsystems were found to be more failure prone than others with annular preventer, control pods and LMRP connector requiring greater maintenance effort.
- Active redundancy has been applied to the BOP system and its components to enhance the reliability characteristics of the system.
- Advanced reliability analysis techniques such as Petri Net (PN), Bayesian network (BN), Markov modelling and their different variations have been recognized to overcome the drawbacks of conventional reliability assessment techniques such as FTA and FMEA.

The review of scientific literature revealed that the number of publications about reliability analysis of BOP systems is gradually increasing. In spite of remarkable progress in the application of various reliability analysis techniques, there are still opportunities for further research in this area of study. Some of the potential future research directions are provided below:

1. Comprehensive reliability and availability improvements as a result of redundancy. This will continuously enhance current drilling trend research;
2. Accruing updated failure information (failure modes, causes and rates) of subsea BOPs with respect to new water depths being explored and the operational and environmental challenges that accompany those explorations;
3. Reliability analyses that account for multiple degradation processes within various BOP subsystems as opposed to the current binary outlook.

# RESEARCH HIGHLIGHTS 

- To review current state-of-the-art of subsea blowout preventer (BOP) technology;
- To identify challenges in BOP design, reliability, testing, deployment, and maintenance;
- To classify the literature based on depth of water and the Macondo disaster;
- To evaluate the techniques applied to reliability analysis of BOP;
- To identify and evaluate the areas requiring further research and development.

# AUTHORS STATEMENT 

Mahmood Shafiee: Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Data curation, Writing - Original Draft, Writing - Review \& Editing, Visualization, Supervision.

Tobi Elusakin: Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Data curation, Writing - Original Draft, Writing - Review \& Editing, Visualization, Project administration.

Evenye Enjema: Conceptualization, Methodology, Software, Validation, Formal Analysis, Investigation, Data curation, Writing - Original Draft, Visualization, Project administration.

# AUTHOR DECLARATION 

We wish to confirm that there are no known conflicts of interest associated with this publication and there has been no significant financial support for this work that could have influenced its outcome.

We confirm that the manuscript has been read and approved by all named authors and that there are no other persons who satisfied the criteria for authorship but are not listed. We further confirm that the order of authors listed in the manuscript has been approved by all of us.

We confirm that we have given due consideration to the protection of intellectual property associated with this work and that there are no impediments to publication, including the timing of publication, with respect to intellectual property. In so doing we confirm that we have followed the regulations of our institutions concerning intellectual property.

We understand that the Corresponding Author is the sole contact for the Editorial process (including Editorial Manager and direct communications with the office). He is responsible for communicating with the other authors about progress, submissions of revisions and final approval of proofs. We confirm that we have provided a current, correct email address which is accessible by the Corresponding Author and which has been configured to accept email from m.shafiee@kent.ac.uk

Signed by all authors as follows: Mahmood Shafiee, Tobi Elusakin, Evenye Enjema

# Subsea blowout preventer (BOP): Design, reliability, testing, deployment, and operation and maintenance challenges 

Shafiee, Mahmood

2020-05-14
Attribution-NonCommercial-NoDerivatives 4.0 International

Shafiee M, Elusakin T, Enjema E. (2020) Subsea blowout preventer (BOP): Design, reliability, testing, deployment, and operation and maintenance challenges. Journal of Loss Prevention in the Process Industries, Volume 66, July 2020, Article number 104170
https://doi.org/10.1016/j.jlp.2020.104170
Downloaded from CERES Research Repository, Cranfield University