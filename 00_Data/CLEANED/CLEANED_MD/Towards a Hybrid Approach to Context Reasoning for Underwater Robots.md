# Towards a Hybrid Approach to Context Reasoning for Underwater Robots 

Xin Li *, José-Fernán Martínez and Gregorio Rubio<br>Research Center on Software Technologies and Multimedia Systems for Sustainability (CITSEM), Campus Sur, Technical University of Madrid, 28031 Madrid, Spain; jf.martinez@upm.es (J.-F.M.); gregorio.rubio@upm.es (G.R.)<br>* Correspondence: xin.li@upm.es; Tel.: +34-914-524-900 (ext. 20794)<br>Academic Editor: Antonio Fernández-Caballero<br>Received: 23 December 2016; Accepted: 8 February 2017; Published: 15 February 2017


#### Abstract

Ontologies have been widely used to facilitate semantic interoperability and serve as a common information model in many applications or domains. The Smart and Networking Underwater Robots in Cooperation Meshes (SWARMs) project, aiming to facilitate coordination and cooperation between heterogeneous underwater vehicles, also adopts ontologies to formalize information that is necessarily exchanged between vehicles. However, how to derive more useful contexts based on ontologies still remains a challenge. In particular, the extreme nature of the underwater environment introduces uncertainties in context data, thus imposing more difficulties in context reasoning. None of the existing context reasoning methods could individually deal with all intricacies in the underwater robot field. To this end, this paper presents the first proposal applying a hybrid context reasoning mechanism that includes ontological, rule-based, and Multi-Entity Bayesian Network (MEBN) reasoning methods to reason about contexts and their uncertainties in the underwater robot field. The theoretical foundation of applying this reasoning mechanism in underwater robots is given by a case study on the oil spill monitoring. The simulated reasoning results are useful for further decision-making by operators or robots and they show that the consolidation of different reasoning methods is a promising approach for context reasoning in underwater robots.


Keywords: context reasoning; uncertainty; Multi-Entity Bayesian Network (MEBN); underwater robots; ontology; context awareness

## 1. Introduction

Context awareness [1] is important in many research domains, such as Smart Cities [2], Smart Homes [3], Ambient Assisted Living [4], and Smart Grids [5]. As a key enabler for entities to understand their environment and make adaptations accordingly, context awareness implies an effective exploitation of contexts. With advances in sensing, pervasive computing, and communication technologies, more and more contexts can be obtained and promisingly used. To make the most of the available contexts is key to achieving context awareness. In general, three conventional approaches have been used to achieve context awareness [6]: (1) each application or domain acquires, processes, and employs contexts of its interest in its own manner; (2) some libraries that provide methods to process contexts are used in context-aware applications or domains; and (3) a context-aware framework/middleware/intermediation architecture is adopted to provide common functionalities to manage contexts and deliver context awareness. According to Li et al. [7], the third approach is regarded as the best solution due to its ability to decrease the complexity of building context-aware applications.

The European Smart and Networking Underwater Robots in Cooperation Meshes (SWARMs) [8] project includes introducing context awareness into the field of underwater robotics as one of its objectives. This project aims to expand the use of unmanned underwater vehicles (e.g., AUVs or

ROVs) in maritime and offshore operations in a collaborative, cooperative, and context-aware manner. The SWARMs approach is underpinned by designing a semantic and distributed middleware. The middleware layer has been designed to facilitate communication between heterogeneous vehicles and a Command \& Control Station (C \& CS) and provide a set of common services. A context-aware framework, dedicated to delivering context awareness in underwater robots, is designed as part of the middleware. The context-aware framework aims to provide different context treatments that comply with the general lifecycle of context awareness. As depicted in Figure 1, the context awareness lifecycle is summarized into four essential phases [9], namely context acquisition (obtaining necessary context data), context modeling (representing contexts in a machine-readable and processable form), context reasoning (deriving high-level contexts from available contexts), and context dissemination (distributing useful contexts). Ontologies, which are considered the most promising modeling technique in terms of expressiveness and interoperability [10], have been adopted in the context-aware framework to formally represent heterogeneous contexts that are exchanged between vehicles, such as the battery level of vehicles, capabilities of vehicles, turbidity, position, speed, salinity, and wind direction [11]. It is worth noting that operators or vehicles are more willing to use high-level context information instead of raw context to conceive and offer context-aware services [12]. For instance, a piece of high-level context, vehicle A might collide with vehicle B soon, is more meaningful for operators to make decisions than the basic context information vehicle $A$ is out of trajectory and heading in the direction of vehicle $B$. Therefore, context reasoning based on information formatted in ontologies is important for realizing context awareness in underwater robots. In particular, the harsh nature of the underwater environment and the limitations of sensors attached to vehicles impose more challenges in making effective context reasoning in underwater robots. In the underwater environment, the majority of contexts, namely sensory data, are prone to be uncertain [12]. Uncertainties, as an inherent characteristic of context, should be handled in the reasoning phase. Therefore, there is a need for context-aware framework to provide suitable accommodation for the inclusion of uncertainties.
![img-0.jpeg](img-0.jpeg)

Figure 1. The lifecycle of context awareness.

A lot of context reasoning methods have been off-the-shelf and reviewed in [13,14]; however, none of them is versatile and could individually solve all the reasoning requirements in underwater robots. There is a necessity for a shift towards a combination of different context reasoning methods [7]. Ontological reasoning [15] is the widely used context reasoning method as it could can ontology consistency and concept subsumption. SWRL (Semantic Web Rule Language) [16] rules are proposed to be incorporated into ontologies and could mitigate the lack of ontologies in determining useful information based on rules [17]. However, both of them lack the ability to reason under uncertainties as they assume a deterministic world. Probability is considered the most well-known formalism for computational scientific reasoning under uncertainties [18]. The emerging probabilistic reasoning method, namely the Multi-Entity Bayesian Network (MEBN) [18], as an extension of the standard Bayesian Network (BN), could represent and reason about problems that involve a varying number of uncertain entities. Such complex reasoning problems are common in the underwater robot field. For example, the investigated robot may have more than one robot around. The collision risk is

affected by all possible nearby robots, thus resulting in a problem that involves a varying number of entities. The MEBN shows a lot of potential in reasoning about such complex problems in underwater robots. Therefore, in this paper, the first proposal of using a hybrid context reasoning mechanism, including ontological, rule-based, and MEBN reasoning, in underwater robots is presented. The incorporation of ontological, rule-based, and MEBN reasoning methods can provide better performance by compensating for individual weaknesses using others' strengths. The proposed reasoning mechanism is more flexible and effective to provide different reasoning capabilities to satisfy different reasoning needs. It could provide a logic reasoning strategy to deal with certain context information while enabling a probabilistic inference on uncertain contexts. A scenario of oil spill detection is simulated and it is used to theoretically verify the proposed hybrid reasoning mechanism in terms of applicability and usefulness.

The remainder of this paper is structured as follows. Section 2 reviews existing context-aware frameworks for underwater robots and different context reasoning methods used in the realization of context awareness. An overview of the context-aware framework and the SWARMs ontology proposed in the SWARMs project is provided in Section 3. In Section 4, the proposed hybrid context reasoning is presented and the specific workflow of the hybrid context reasoning engine is shown. A case study of an oil spill monitoring problem is provided in Section 5 to show the usefulness of the proposed reasoning mechanism. Finally, conclusions are given in Section 6 and future work is pointed out as well.

# 2. Related Work 

The concept of context-aware framework emerged in the 1990s when the first attempt to build context-aware frameworks focused on exploiting location data [19]. Thorough analyses of existing context-aware frameworks have been provided by a number of surveys [7,9,10,20,21]. Existing context-aware frameworks have been proposed mainly for Smart Homes, Smart Cities, Ambient Assisted Living, Smart Grids, etc. Introducing the technique of context-aware framework into the field of underwater robots is under-researched [12]. Only a few attempts, including Pandora [22], Trident [23], and CoCoRo [24], have been presented for delivering context awareness in underwater robots. However, they differ from each other in terms of context awareness level and they present unsatisfactory performance due to their lack of important data treatments [9]. Specifically, Pandora and Trident employ ontologies to represent contexts but fail to provide effective context reasoning to generate high-level contexts. CoCoRo does not include proper capabilities for modeling context data in a formalized manner so it considerably limits the potential of transparent context sharing and lacks support for context reasoning. Efficient context distribution methods are not considered in the Pandora and Trident context-aware frameworks. In addition, neither of them takes into account context uncertainty, either in the context modeling or context reasoning phase. Different from them, the context-aware framework proposed in the SWARMs project aims to provide a complete management covering the whole lifecycle of context awareness for underwater robots.

Efforts at the managing uncertainty in context information have been made in the recent literature. For instance, Lukasiewicz and Straccia [25] summarized approaches to manage uncertainty and vagueness in description logics for the semantic web. Ding et al. [26] used Bayesian theories to manage context uncertainties; a similar approach was adopted by Yang et al. [27]. An approach to assess the ambiguity of context data was proposed by [28] using probabilities and fuzzy logic. Probabilistic Datalog was employed to add probabilities and rules to Web Ontology Language (OWL) [29] Lite subsets in order to represent and infer context uncertainties [30]. In particular, focusing on the context reasoning phase, it is noted that all individual reasoning techniques have different weaknesses, explicitly described in [8,13]. For instance, ontological and rule-based reasoning could not handle uncertainty in their reasoning process. The importance of employing multiple reasoning techniques to mitigate individual drawbacks by using others' advantages is highlighted [8,31]. For example, Pilato et al. [32] applied ontological and BN reasoning to derive

high-level contexts toward marine awareness. A combination of ontological and rule-based reasoning was adopted to intuit user activities [33]. Bobillo et al. [34] also introduced fuzzy logic into ontologies to provide a combined reasoning. The emerging probabilistic reasoning method, MEBN, which is based on BN reasoning, shows good performance in reasoning over uncertainties in some domains, including procurement fraud detection [35], maritime awareness [36], knowledge-driven analysis for cultural heritage [37], and Robocup Soccer [38]. In the SWARMs project, a hybrid context reasoning mechanism is needed to deal with reasoning under uncertainties. Thus, this paper presents a proposal for applying ontological, rule-based, and MEBN reasoning to the SWARMs project. The combination of three different context reasoning methods could meet the different reasoning requirements in the underwater robot field. Notably, the applicability of the MEBN reasoning to reason about uncertain contexts for underwater robots is explored in this paper.

# 3. Overview of the SWARMs Context-Aware Framework for Underwater Robots 

### 3.1. The Context-Aware Framework

The SWARMs middleware is capable of being context-aware when offering various information and services for vehicles or the mission management tool (MMT), which is located onshore or on a vessel and is in charge of the generation of missions, assignment of tasks to robots, and supervising the missions. Vehicles and MMT can make use of information and services provided by the middleware, such as adapting behaviors according to the ever-changing environment and making mission planning/re-planning better. A significant feature, context awareness, is enabled by the context-aware framework tailored to the domain of underwater robots.

As part of the SWARMs middleware, the context-aware framework aims to provide a complete and well-defined management for context data that are exchanged between vehicles, such as information about the underwater environment, mission and planning, communications, and context from external data sources (e.g., marine experts and third-party information providers). Specifically, the objective of the context-aware framework is to abstract heterogeneous context in a unified format, enable data and capabilities sharing between vehicles, encase data with semantics, reason about contexts for high-level information, disseminate relevant data to entities, and provide a homogeneous application development interface. Thus, the SWARMs general architecture can be augmented by the context-aware framework in terms of context awareness. With the context-aware framework, vehicles and operators can have a better understanding of the complete picture of the SWARMs environment. The proposed architecture for the context-aware framework can be seen in Figure 2.

The context-aware framework is conceived to be modular and distributed, which could imply a better potential to be employed in robot coordination and cooperation versus a centralized framework one. Specifically, the context-aware framework consists of six logic components, namely, Ontology Model, Data Processor, Semantic Mapper, Rules Creator, Context Reasoner, and Semantic Query. The functional capabilities of each component are described as follows:

- Data Processor. The extreme underwater conditions impose more challenges in the data acquisition phase. Thus, context data obtained from the environment could be uncertain. A preliminary treatment for uncertain data is needed and this treatment is provided by the data processor component. This component can pre-process the data obtained by sensors or other sensing instruments. Statistics, such as probability distribution, can be learned using machine learning algorithms in this component. Operations, such as validating values, checking inconsistencies, calculating uncertainty degrees, removing outliers, and filling in missing values, can be executed in this component.
- Ontology Model. This component, acting as a semantic repository, keeps the SWARMs' ontology and stores all data obtained as instances in the ontology model. Ontology is adopted to serve as a common information model to represent information and enable sharing, reuse, and integration of data between vehicles. The information model is structured in a hierarchical manner. The networked

information model consists of three levels of ontologies: core ontology (acting as an upper-level ontology to glue all domain specific ontologies), domain-specific ontology (providing information models for different domains, e.g., mission planning, vehicles, environment, and communications), and application-specific ontology (describing information with a focus on particular applications, e.g., oil spill detection, plume tracking, berm construction). Therefore, data, including but not limited to contextual measurements, vehicle-related data, data from external sources (Global Positioning System, oceanic weather forecast, etc.), and marine experts' knowledge, can be abstracted and formalized in an ontological format. All data can be displayed with a homogeneous view associated with the semantic content. The ontology model could annotate context uncertainties based on MEBN theories. Specifically, probability information about uncertain context can be modeled using ontology constructs defined in the PR-OWL [39] ontology. With PR-OWL classes and properties, ontology engineers could fully specify an MEBN model while maintaining compatibility with the OWL ontology language. The SWARMs ontology will be briefly introduced in Section 3.2.

- Semantic Mapper. This component plays a vital role in facilitating the transparent sharing of information. As data might be formatted in different manners pertaining to different data sources, this component aims to parse and formalize them in an ontology-compliant format. Translations from different standards, such as XML, JSON, or binary files, to ontological formations, such as Resource Description Framework (RDF) [40] or OWL, can be enabled in this component. For differently formatted data that do not comply with the SWARMs ontology, corresponding mapping files should be predefined in order to parse and map them into the common information model.
- Rules Creator. Operators or marine experts are able to define rules based on their knowledge before or during missions through this component. A set of user-defined rules can be translated into the SWRL format and inserted into the ontology model. Rules can be diverse, including restrictions or definitions for entities, regulations for evaluating data values, or specifications for relationships between entities. The rule set is very important for the context reasoner to consider when making inferences.
- Context Reasoner. The essential capability of this component is to derive new knowledge from available contexts stored in the ontology model. Basically, it will consult information stored in the ontology model and also take experiences and knowledge from marine experts into account. A hybrid reasoning mechanism, including the ontological, rule-based, and MEBN reasoning, is intended to be employed in this context reasoner. Specifically, the ontological reasoning enables several kinds of operations, including concept satisfiability, consistency check, class subsumption, and logic inference. The rule-based reasoning could augment the ontological reasoning in terms of logicality and human readability. The MEBN reasoning is dedicated to reasoning under uncertainties.
- Semantic Query. This component deals with any semantic query made by operators. It receives queries, calls corresponding reasoning services, and finally outputs answers. This is one of the context dissemination strategies defined in the SWARMs project. Apart from this, the SWARMs project also follows a subscribe/publish paradigm to distribute context information.

The context-aware framework provides architectural support for different context treatments. Within the framework, the context reasoner is significant as it is able to provide the necessary services to meet all the reasoning requirements in the SWARMs project. In particular, it can handle the intricacies inherent to the reasoning over uncertainties. The hybrid context reasoning, proposed for the context reasoner component, will be presented in Section 4.

![img-1.jpeg](img-1.jpeg)

Figure 2. Overview of the proposed context-aware framework.

# 3.2. The SWARMs Ontology 

The SWARMs ontology can address context heterogeneity by providing a formal representation of information that is necessarily exchanged between vehicles and middleware/MMT components. By complying with the SWARMs ontology, a common understanding for the exchanged information can be achieved by heterogeneous vehicles. The SWARMs ontology is a networked ontology. Figure 3 shows a simplified version of the SWARMs ontology structure and the full version is accessible online [41]. As shown in Figure 3, the SWARMs ontology is composed of different domain-specific ontologies

that are linked by a core ontology. Different domain-specific ontologies model common classes, relationships, and axioms of certain domains, including mission \& planning, environment recognition \& sensing, robotic vehicle, and communication \& networking. Specifically, the robotic vehicle ontology models the robots and vehicles used in the different SWARMs missions. The mission \& planning ontology represents the whole mission composition and planning procedure of the low-level planning at a vehicle level. The environment where missions are carried out is characterized in the environment recognition \& sensing ontology. The communication \& networking ontology models the communication links that are available in the SWARMs missions. The core ontology defines a set of relationships to interconnect different domain-specific ontologies. For instance, as shown in Figure 3, the concept Service in the mission \& planning ontology can be related to the concept Asset in the Robotic Vehicle ontology through a pair of inverse relationships, namely, providedBy and contributes. The concept VehicleLevelTask can be interrelated to the concept RoboticVehicle by relationships assignedTo and allocatedTo. The mission \& planning ontology can also be linked to the robotic vehicle ontology through the relationship (canPerform and performedBy) between the concept Action and the concept RoboticVehicle. The concept Sensor from the environment recognition \& sensing ontology and the concept CommunicationLink from the communication \& networking ontology are subsumed into the concept System in the robotic vehicle ontology. The concept Vehicle from the robotic vehicle ontology is modeled as a subclass of the concept ManmadeObject from the environment recognition \& sensing ontology. With the four domain-specific ontologies interconnected by the core ontology, the SWARMs ontology could provide a general description of information exchanged in the scope of the SWARMs project. When dealing with different missions (e.g., oil spill detection, corrosion repair, seabed mapping, berm construction, and plume tracking), the SWARMs ontology can be extended with application semantics. In addition, context uncertainties in specific missions can be annotated by using the PR-OWL ontology constructs and modeled in MEBN theories.
![img-2.jpeg](img-2.jpeg)

Figure 3. The structure of the Smart and Networking Underwater Robots in Cooperation Meshes (SWARMs) ontology.

# 4. The Hybrid Context Reasoning Mechanism 

The proposed hybrid context reasoning mechanism is described in this section. Specifically, Section 4.1 presents the principles behind the three context reasoning methods used to build the hybrid mechanism

for the SWARMs context-aware framework. The specific interactions between the context reasoner and other context-aware framework components are given in Section 4.2.

# 4.1. Principles of the Different Reasoning Methods 

This reasoning engine, depicted in Figure 4, is flexible to provide different advanced reasoning capabilities so that the most suitable method can be used to accommodate to different reasoning needs. This hybrid approach is built based on the ontological, rule-based, and MEBN reasoning techniques. Ontological and rule-based reasoning are well understood and widely used in many context-aware frameworks. MEBN, as an emerging probabilistic reasoning method, is given more emphasis in the following.
![img-3.jpeg](img-3.jpeg)

Figure 4. The hybrid context reasoning method for the context reasoner component.

To correctly select reasoning techniques, two key factors are necessarily considered. The performance of a specific reasoning technique is regarded as the primary criterion. In addition, given that different modeling methods are available, the reasoning techniques selected should be compatible and suit the specific modeling technique used for knowledge representation. The reasons for integrating the ontological, rule-based, and MEBN reasoning methods in the proposed approach will be given in the following sections. In addition, the basic principles of each method will be introduced.

### 4.1.1. Ontological Reasoning

Ontological reasoning, also referred to as description logic reasoning, uses a set of constructs, such as TransitiveProperty, SymmetricProperty, AsymmetricProperty, ReflexiveProperty, IrreflexiveProperty, subClassOf, subPropertyOf, disjointWith, equivalentTo, and inverseOf, to specify a terminological hierarchy and assert inner restrictions. It is mainly supported by two semantic web representation languages, $\operatorname{RDF}(\mathrm{S})$ and OWL. Tableau algorithm is the de facto standard reasoning algorithm that is employed in ontological reasoning. Ontological reasoning enables several kinds of operations, including concept satisfiability, consistency check, class subsumption, and logic inference. Therefore, by means of ontology-based reasoning, some facts that are implicit in the ontology given explicitly stated facts can be deduced. Table 1 presents a list of ontology-based reasoning rules [42].

As all context data are formalized in the SWARMs ontology, it is natural to apply ontology-based reasoning over ontology classes and instances. Several reasoners, including Pellet [43], HermiT [44], and FaCT++ [45], have been developed to support the ontological reasoning in ontologies. However, ontology-based reasoning lacks the ability to express complex relations or rules for reasoning tasks. In addition, it is unable to deal with missing values and reason over uncertainties.

Table 1. Partial ontological reasoning constructs.


# 4.1.2. Rule-Based Reasoning 

To compensate for ontological reasoning's inability to represent complex rules and relations, SWRL is adopted to define rules in the proposed hybrid context reasoning mechanism. SWRL represents a combination of OWL and RuleML [46]. The expressivity of OWL is extended by including Horn-like rules enabled by SWRL. SWRL rules contain unary predicates for the description of classes and data types, binary predicates for expressing object properties, and several built-in n-ary predicates, such as math built-ins, comparisons built-ins, and string built-ins. In essence, SWRL rules are defined in an antecedent-and-consequent, also referred to as if-then, implication. If the set of conditions specified in the antecedent part is met, then the SWRL rule is executed and the assumptions specified in the consequent part can be inferred as high-level information. Hence, marine experts can encode their knowledge and experience into SWRL rules and insert them into the knowledge base. A simple SWRL rule example can be seen as follows:

SWRL rule-based reasoning: Robot(?x), hasBatteryLevel (?x,?y), swrlb:greaterThan(?y, 40\%) $\rightarrow$ RobotCandidates(?x).

The rule above is very straightforward and expresses an assumption that a robot can be regarded as a potential candidate to carry out a task if its battery level is higher than $40 \%$. Once the ontology model is populated with instances, the rule-based reasoning can infer over those instances based on the pre-defined rule. Afterward, more useful information (e.g., robot_Alister is a candidate to execute the task) can be derived given low-level context (e.g., robot_Alister is an underwater robot and its current battery level is higher than $40 \%$ ).

With the allowance of encasing user-defined rules in the ontology model enabled by SWRL, the reasoning task can be augmented in terms of logicality and human readability. Pre-insertion and formalism of SWRL rules are supported by the Protégé [47]. The rules creator component also provides interfaces for operators to define and insert rules during missions. Reasoners Pellet and HermiT can enable automatic reasoning based on SWRL rules. Despite the fact that rule-based reasoning has several useful features (e.g., ease of use, ease of implementation, extendibility, and human readability), it also has several limitations remaining to be solved. Manually encasing a large volume of user-defined rules in the ontology model might lead to error-proneness and undecidability in the reasoning phase. Besides, in terms of the ability to define changing events, they lack interoperability and reusability. Similar to ontological reasoning, rule-based reasoning is unable to reason over uncertainties.

# 4.1.3. Multi-Entity Bayesian Network (MEBN) Reasoning 

MEBN, first proposed by Laskey et al. [18], combines the expressivity of First-Order Logic (FOL) with the inferential power of BN. With this incorporation, the MEBN is able to provide a consistent treatment of uncertainty, such as representing uncertainty about the type of an entity, refining type-specific probability distributions through Bayesian Learning, and reasoning under uncertainty. Beyond the capability of traditional BN in reasoning about a fixed number of attributes, MEBN could deal with a varying number of entities with their number, type, and relationships undetermined. MEBN provides a means of defining probability distributions over an unbounded and varying number of interrelated hypotheses with the aid of syntax, a set of model construction and inference processes, and semantics.

MEBN interprets the world as a set of entities that have attributes and have causal relationships with other entities. Knowledge about the attributes of the entities and their relationships to each other is represented as a MEBN model. MEBN logic consists of a collection of MEBN fragments (MFrag) organized into an MEBN Theory (MTheory). An MTheory could represent a particular domain of discourse. Each MFrag, as a modular component, represents knowledge about specific subjects within the domain of discourse and models probability information about a group of related random variables. Similar to BN, each MFrag is a Directed Acyclic Graph (DAG) with parameterized nodes that represent attributes of entity and edges that represent dependencies among them. Three types of nodes, resident nodes, context nodes, and input nodes, are defined in the MTheory.

- Resident nodes. In an MFrag graph, resident nodes represent variables that have local probability distributions dependent on the values of their parents. Exactly one home MFrag is assigned to contain the complete expression of a resident node.
- Context nodes. Context nodes are Boolean nodes, including value True, False, and Absurd. The MFrag must satisfy the conditions expressed by context nodes in order to be valid.
- Input nodes. Input nodes have their distributions defined in other MFrags and they are important inputs for the definition of resident nodes.

The MTheory could be instantiated with specific information about the individual entity instances to reason about specific situations. The instantiated MEBN, named Situation-Specific Bayesian Network (SSBN) [18], could make inferences under uncertainties based on standard BN reasoning. In order to enable MEBN reasoning compatible with ontologies, an upper ontology PR-OWL [39] is used to provide a set of ontology constructs to express the probability distribution information associated with ontology elements. PR-OWL is based on MEBN theories. By incorporating with PR-OWL, traditional ontologies could annotate uncertainties of ontology elements based on MEBN theories. The PR-OWL ontology could provide support to reasoning over uncertainty using FOL and probability and the reasoning process in PR-OWL ontology is an automatic generation of SSBN to determine the probabilities of a query.

The UnBBayes [48] tool provides both Graphical User Interface (GUI) and Java Application Programming Interfaces (APIs) to build MEBN models, generate probability-annotated ontology to represent the MEBN models, and make uncertainty reasoning.

By integrating the ontological, rule-based, and MEBN reasoning methods, it is able to provide multiple reasoning capabilities that can cover all needs from the SWARMs project. When dealing with different inference needs, specific reasoning mechanisms can be invoked. The specific reasoning workflow is presented in the next section.

### 4.2. Specifications for the Reasoning Workflow

In this section, interactions between the context reasoner and other context-aware framework components are introduced. The specific process to invoke different reasoning capabilities embedded in the context reasoner is described in the following.

# 4.2.1. Use of the Ontological Reasoning 

In order to get information stored in the ontology model, operators or vehicles can make semantic queries, such as a SPARQL [49] query, through the semantic query component. For instance, after receiving a query to insert/remove data in the ontology, the semantic query would turn the context reasoner on. Once the ontology is manipulated, an ontology-based reasoner, such as a Pellet reasoner, is fired and applies the ontological reasoning on the ontology model. Reasoning results could be locally stored in the ontology model so that operators or vehicles can obtain answers over the data inferred.

### 4.2.2. Use of the Rule-Based Reasoning

The context-aware framework enables operators or marine experts to insert rules through the rules creator. The rules creator could allow people with ontological knowledge to specify rules in the SWRL format. Non-ontological users, such as operators or marine experts, could insert rules using an if-then implication and the rules creator could translate them into corresponding SWRL rules. Rules formatted in the SWRL manner are sent to the ontology model and stored in the ontological repository. When operators or vehicles create a new rule, the rules creator invokes the Pellet reasoner employed in the context reasoner and the rule-based reasoning is applied on the ontology model. New facts can be inferred based on rules, stored in the ontology model, and finally consulted by MMT or vehicles.

### 4.2.3. Use of MEBN Reasoning

When dealing with different scenarios, operators or marine experts can pre-define MEBN models to represent reasoning problems that involve uncertainties and store the MEBN models in the ontology model. Operators or vehicles could make queries through the semantic query component for information involved in a reasoning problem, such as the probability of specific ontology elements and possible states of ontology concepts. Once receiving the query, the semantic query component will invoke the MEBN reasoner embedded in the context reasoner component. The MEBN reasoning will be applied to the ontology model and infer new data. The ontology model component is updated with inferred data so that it can provide corresponding answers to queries made by MMT or vehicles.

## 5. The Proof of Concept: A Case Study on Oil Spill Detection

In this section, a case study on oil spill detection is described. The proposed hybrid reasoning mechanism will be demonstrated to tackle the reasoning task within the case study.

### 5.1. Description of the Scenario

The proactive detection of oil spills is an important means to minimize the damage of spills to the marine environment. Thus, oil spill detection is considered one of the use cases in the SWARMs project. A set of SWARMs vehicles could collaboratively detect the occurrence of oil spills based on contextual data they could obtain. After detecting oil spills in a specific marine region, it is important to predict the severity of the spilled region so that remedial measures (e.g., clean-up, containment) can be taken accordingly. The estimation of the severity level of the specific area depends on several available raw contexts, including the thickness of spills, the estimated size of spills, the weather condition, and the currents. In addition, the severity level of the specific area could be influenced by different spills that occurred in the same area at the same time. For instance, two oil spills (spill_1 and spill_2) are detected in a specific region of the ocean (region_1). Spill_1 is observed as being thick and large and spill_2 is detected as being thin and small. In addition, the weather conditions above the spilled marine region are known to be inclement. Currents in the region_1 fluctuate very strongly.

5.2. Application Ontology Extensions for Modeling the Scenario

Application ontology extensions, shown in Figure 5, are defined to enrich the SWARMs ontology model in order to represent the oil spill detection scenario and encode marine experts' understanding.
![img-4.jpeg](img-4.jpeg)

Figure 5. Application ontology extensions for representing the scenario.

The determination of the severity of an oil spill is subject to several factors, including SpreadSpeed, EstimatedSize, Thickness, Currents, and Weather. The concept of the SeverityLevel is linked to its reference factors via the relationship dependsOn, whose attribute is set as transitive. All these criteria are described in the following.

- SpreadSpeed. This concept includes two types of velocity, namely, Fast and Slow, to describe the possible spreading speed of the detected oil spill. It is asserted that the spreading speed depends on two features: Weather and Currents.
- Weather. It conceptualizes two kinds of weather conditions: Clement and Inclement. Spills often occur in inclement weather and spread more widely in such weather.
- Currents. It describes whether currents in the spilled region fluctuate strongly or weakly.
- EstimatedSize. It is a characteristic of spills and represents the estimated coverage range of spills. Specifically, it is divided into two kinds, Large and Small.
- Thickness. It defines a measuring unit to estimate the quantity of spilled oil, such as Thick and Thin.

All raw context information, gathered by vehicles, can be diagnosed by the data processor component, transformed by the semantic mapper component, and populated into the ontology described above. Therefore, based on the ontology model, a set of high-level information with more meaningful semantics, which is more useful for operators and vehicles, can be obtained based on the different reasoning capabilities provided by the context reasoner.

# 5.3. Context Reasoning in the Case Study 

Three different reasoning capabilities, ontological, rule-based, and MEBN reasoning, are demonstrated in the following sections.

# 5.3.1. Ontological Reasoning 

The ontology model is found to be consistent and accurate after applying ontological reasoning. The specific ontological reasoner employed is the Pellet reasoner. In addition, more high-level context information can be inferred. For instance, an implicit context, SeverityLevel, depends on Currents and Weather and can be obtained through the following ontological reasoning capability.
(?dependsOn rdf:type owl:TransitiveProperty) $\wedge$ (?SeverityLevel ?dependsOn ?SpreadSpeed) $\wedge$ (?SpreadSpeed ?dependsOn ?Currents) $\Rightarrow$ (?SeverityLevel ?dependsOn ?Currents)
(?dependsOn rdf:type owl:TransitiveProperty) $\wedge$ (?SeverityLevel ?dependsOn ?SpreadSpeed) $\wedge$ (?SpreadSpeed ?dependsOn ?Weather) $\Rightarrow$ (?SeverityLevel ?dependsOn ?Weather)

Similarly, other high-level information that is more meaningful for usage can also be deduced based on ontological reasoning.

### 5.3.2. Rule-Based Reasoning

Rules can be defined to provide a more accurate specification for some ontology elements. For instance, to provide a clear boundary and explanation for different Thickness degrees, rules can be set as follows:

Thickness(?x), hasDegree(?x,?y), swrlb:greaterThan(?y,?1200) $\rightarrow$ Thick(?x)
Thickness(?x), hasDegree(?x,?y), swrlb:lessThan(?y,?1200), swrlb:greaterThan(?y,?20) $\rightarrow$ Thin(?x)
Based on the ontological representation enriched with the rules listed above, a specific spill with a thickness measurement (e.g., 2500 micron) can be classified as Thick after invoking rule-based reasoning. Likewise, SWRL rules can be defined to encode experts' understanding of other concepts, such as Currents and EstimatedSize. In this way, the raw data stored in the ontology model can be inferred to get higher-level contexts with more meanings.

### 5.3.3. MEBN Reasoning

An MEBN model, shown in Figure 6, is built using the UnBBayes tool to reason about the severity level of spills under uncertainties. The MEBN model is formatted in an OWL format and stored in the context reasoner.
![img-5.jpeg](img-5.jpeg)

Figure 6. The Multi-Entity Bayesian Network (MEBN) model to reason about the severity level of spills.

The MTheory consists of seven MFrags, Thickness, EstimatedSize, Weather, Currents, Location, SpreadSpeed, and SeverityLevel. Each MFrag represents knowledge for a specific entity and its local probability distribution. Specifically, the Thickness, EstimatedSize, Weather, Currents, and Location MFrags provide modeling of variable Thickness, EstimatedSize, Weather, Currents, and Location and their prior probability distribution. The SpreadSpeed and SeverityLevel MFrags represent local probability distribution of variable SpreadSpeed and SeverityLevel under the influence of their causal variables, such as Weather, Currents, and Thickness. For instance, the SpreadSpeed MFrag models that the spread speed of detected spills is affected by two inputs, namely, Weather and Currents. These two input nodes, weather and currents, are specified in the Weather and Currents MFrags, respectively. The local probability distribution of SpreadSpeed is shown in Figure 7. Annotation of this probability information using PR-OWL constructs can be seen in Figure 8. In this case study, all the probability information in this model is directly provided by marine experts based on their experiences. It is worth noting that the probability information can also be derived from historical data.
![img-6.jpeg](img-6.jpeg)

Figure 7. The local probability distribution of SpreadSpeed.

```
<hasProbDist>
<DeclarativeDist rdf:ID="SpreadSpeed_Table">
<hasDeclarationrdf:datatype="http://www.w3.org/2001/XMLSchema
a#string">
if any rgn have ( Weather = Clement & Currents = Strong ) [ Fast =
0.5, Slow = 0.5 ] else if any rgn have ( Weather = Clement & Currents
= Weak ) [ Fast = 0.1, Slow = 0.9 ] else if any rgn have ( Weather =
Inclement & Currents = Strong ) [ Fast = 0.9, Slow = 0.1 ] else [ Fast =
0.5, Slow = 0.5 ]
</hasDeclaration>
<isProbDistOf rdf:resource="#Domain_Res.SpreadSpeed"/>
</DeclarativeDist>
</hasProbDist>
```

Figure 8. Ontology annotation of SpreadSpeed local probability distribution.

With the aforementioned seven MFrags, the MTheory could collectively model the unique joint probability distribution for the SeverityLevel entity. The MTheory represents an infinite number of possibilities, thus it can be instantiated to specific scenarios and inferences made based on the observed evidence. In this scenario, the obtained findings are listed in Figure 9. As shown in Figure 9, all necessary context information for estimating the severity level of the spilled region is obtained.

Findings:
isA(spill_1, Spill)=True
isA(spill_2, Spill)=True
isA(region_1, Region)=True
Location(spill_1) =region_1
Location(spill_2) =region_1
Weather(region_1) =Inclement
Currents(region_1) =Strong
EstimatedSize(spill_1) =Large
EstimatedSize(spill_2) =Small
Thickness(spill_1) =Thick
Thickness(spill_2) =Thin

Query:
SeverityLevel(region_1)?
SpreadSpeed(spill_1)?
SpreadSpeed(spill_1)?

Figure 9. Findings in the scenario.

With the complete findings specified in Figure 9, the MEBN can be specified to the scenario and instantiated as a SSBN, as shown in Figure 10.
![img-7.jpeg](img-7.jpeg)

Figure 10. Situation-Specific Bayesian Network (SSBN) generated for the scenario with complete findings.

Based on standard BN inferences, the SSBN can be queried to find updated beliefs of different random variables. For example, the region_1 with the existence of two spills could be estimated as very serious with a probability of $88 \%$ and there is a $90 \%$ chance that the spread speed of spill_1 and spill_2 will be fast. This high-level context could be sent to the MMT for further exploitation. For instance, it could be used by operators as a parameter to conceive a plan for underwater robots so that they can take remedial measures accordingly. It is also worth noting that the MEBN reasoning can reason under

incomplete and uncertain contexts. For instance, in the same scenario, assuming that the thickness of two spills is unknown, the nodes in the MEBN model can be collectively instantiated as an SSBN to represent the specific scenario. The newly generated SSBN with incomplete findings can be seen in Figure 11. As shown in Figure 11, the instantiated nodes of Thickness, namely, Thickness_spill_1 and Thickness_spill_2, are not populated with evidence. However, even with unknown contexts, SSBN can also make inferences under uncertainties. The severity level of the spilled region can be inferred with as high a probability as $78.24 \%$. It is a fact that this estimation is less reliable than the previous inference with complete findings known. However, it showcases that the MEBN reasoning can cater to real-world situations that are partially observable and can deal with uncertainty reasoning given unknown data.
![img-8.jpeg](img-8.jpeg)

Figure 11. SSBN generated for the scenario with incomplete findings.

In this scenario, only two spill instances are exemplified as influence factors for the severity level. It is worth noting that the built MEBN can be flexible to accommodate reasoning that involves more spill instances due to its modularity. Therefore, the same MEBN could be instantiated to deal with a varying number of entities.

# 5.3.4. Discussion 

Oil spill detection is one of the use cases that are defined in the SWARMs project. It implies different reasoning problems (e.g., inference under uncertainties) and thus is a good benchmark scenario to testify the proposed hybrid reasoning mechanism, including ontological, rule-based, and MEBN reasoning. The three different reasoning methods are shown to address different reasoning problems. The use of the MEBN reasoning to reason under uncertainties in underwater robots is explored first. Simulation results using the Protégé (along with the Pellet reasoner) and UnBBayes GUI tools show that the three context reasoning methods employed can deal with partial reasoning problems in the scenario and can compensate for each other's weakness. Therefore, the effectiveness of using these three context reasoning methods in underwater robots is verified theoretically. The simulated proof of concept shows that it is a promising approach to encase these three context reasoning methods in the context reasoner component. In further implementation, the Pellet reasoner API can be employed to provide ontological and rule-based reasoning, while the UnBBayes Java API can provide functionalities for the MEBN reasoning. As the MEBN makes reasoning based on probabilistic ontologies and ensures compatibility with OWL, it can be foreseen that the integration of ontological, rule-based, and MEBN reasoning in the context reasoner could be realistic without inconsistencies. However, the combination of these three context reasoning methods should be rigorously proven by a full implementation of the context reasoner, which will be done in the near future. In a nutshell, in this case study, the focus was to provide a theoretical foundation for applying ontological, rule-based, and MEBN reasoning in the context reasoner component to tackle underwater

robot reasoning. However, the efficiency of the proposed hybrid context reasoning should also be studied in the future. In particular, the reasoning time of each context reasoning method should be recorded under different conditions. For instance, how the number of rules inserted into the ontology model would affect the reasoning time in rule-based reasoning is worth investigating.

# 6. Conclusions and Future Work 

This paper has presented a conceptual proposal of a context-aware framework for underwater robots. The proposed context-aware framework aims to provide complete context management and is devoted to facilitating context awareness in the SWARMs project. The framework offers different data treatments for underwater robots, such as pre-processing context data, modeling heterogeneous contexts in ontologies, reasoning about contexts for more useful information, and disseminating contexts. Different logic components within the framework, including ontology model, data processor, semantic mapper, rules creator, semantic query, and context reasoner, have been described along with their main functionalities and interactions.

In the underwater robot field, context reasoning, as a significant phase in realizing context awareness, is more challenging because the context data obtained by robots are prone to be uncertain. To tackle the challenge of reasoning under uncertainties, a hybrid context reasoning mechanism has been proposed to be used in the context reasoner component. Three reasoning methods, ontological, rule-based, and MEBN reasoning, have been proposed to use in the context reasoner so that it can provide different reasoning strategies to meet the different reasoning requirements. Ontological reasoning is able to provide deductive capabilities, such as context consistency and accuracy checking. Rule-based reasoning is more flexible and simpler than ontological reasoning, and enables the insertion of user-defined rules and inferring more useful information. However, neither ontological nor rule-based reasoning can deal with the uncertainties that are inherent to context data in the underwater robot field. Therefore, an emerging probabilistic reasoning method, MEBN, has been incorporated into the context reasoner in order to provide inferential functionalities dedicated to uncertain contexts. The hybrid context reasoning method has been described in detail and the specific process for using different context reasoning methods has been specified. A case study on oil spill detection has been presented to verify the usefulness and applicability of the hybrid context reasoning mechanism. The simulated results have shown that in theory the hybrid context reasoning method can make logical inferences in certain contexts and also probabilistically reason under uncertainties in the underwater robot field. Through this case study, a theoretical foundation of applying the proposed hybrid context reasoning method in the context reasoner component has been provided and has indicated that the hybrid method can be a promising approach to implement in the context reasoner component.

Future work could focus on the following aspects:

- The presented context-aware framework is still at the prototype level. Completing its implementation and testing it in real scenarios will be the next step.
- Though the proposed context-aware framework is designed specifically for underwater robotics, it does present a generic solution for managing context and providing context awareness. Therefore, applying it to other robotic domains (e.g., on land and air) and application fields (e.g., smart homes and smart agriculture) could be a potential extension of its usage.
- Other uncertainty reasoning algorithms, such as fuzzy logic and the Markov logic network, will be thoroughly studied. The possibilities of integrating them into the proposed reasoning mechanism for enhancement will be explored.
- Context processing and reasoning are normally time-consuming and resource-intensive. How to achieve a trade-off between the load on managing context data and the actual benefit obtained from high-level context needs to be determined.

Acknowledgments: The research leading to the presented results has been undertaken within the SWARMs European project (Smart and Networking Underwater Robots in Cooperation Meshes), under Grant Agreement

No. 662107-SWARMs-ECSEL-2014-1, partially supported by the Electronic Components and Systems for European Leadership Joint Undertaking (ECSEL JU) and the Spanish Ministry of Economy and Competitiveness (Ref: PCIN-2014-022-C02-02).
Author Contributions: Xin Li, José-Fernán Martínez, and Gregorio Rubio conceived the context-aware framework. Xin Li and José-Fernán Martínez proposed the hybrid context reasoning mechanism and also tested it. Xin Li, José-Fernán Martínez, and Gregorio Rubio all wrote this manuscript.
Conflicts of Interest: The authors declare no conflict of interest.
