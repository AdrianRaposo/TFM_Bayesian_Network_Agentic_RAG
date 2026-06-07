Published in final edited form as:
Int J Prod Res. 2020 ; 58: . doi:10.1080/00207543.2019.1680895.

# Enriching Analytics Models with Domain Knowledge for Smart Manufacturing Data Analysis 

Heng Zhang ${ }^{\mathrm{a}, *}$, Utpal Roy ${ }^{\mathrm{a}}$, Yung-Tsun Tina Lee ${ }^{\mathrm{b}}$<br>${ }^{a}$ Department of Mechanical and Aerospace Engineering, Syracuse University, Syracuse, NY, USA<br>${ }^{\text {b }}$ Systems Integration Division, National Institute of Standards and Technology, Gaithersburg, MD, USA


#### Abstract

Today, data analytics plays an important role in Smart Manufacturing decision making. Domain knowledge is very important to support the development of analytics models. However, in today's data analytics projects, domain knowledge is only documented, but not properly captured and integrated with analytics models. This raises problems in interoperability and traceability of the relevant domain knowledge that is used to develop analytics models. To address these problems, this paper proposes a methodology to enrich analytics models with domain knowledge. To illustrate the proposed methodology, a case study is introduced to demonstrate the utilization of the enriched analytics model to support the development of a Bayesian Network model. The case study shows that the utilization of an enriched analytics model improves the efficiency in developing the Bayesian Network model.


## Keywords

Smart Manufacturing; Data Analytics; Domain Knowledge; Interoperability; Traceability; Bayesian Network

## 1. Introduction

Due to advances in information technologies and artificial intelligence, the Smart Manufacturing (SM) concept has emerged to lead a new paradigm of manufacturing systems. In such systems, data analytics can play an important role to turn data into valuable insights to assist SM decision making. To successfully perform data analytics, domain knowledge is required to support the development of analytics models. Kopanas et al. (2002) investigated the role of domain knowledge in industrial data analytics projects. They concluded that the use of domain knowledge is crucial in all phases of a data analytics project - problem definition, data understanding, data pre-processing, data mining, evaluation of the analytics model and deploying the developed analytics model. However, in today's data analytics projects, the relevant domain knowledge, which is used in developing

[^0]
[^0]:    *Corresponding author. hzhang33@syr.edu.

an analytics model, is only documented, but not properly captured and integrated with the analytics models.

The lack of properly captured and integrated domain knowledge raises an issue in the interoperability of the domain knowledge for developing an analytics model. Currently, there are two standards that support analytics models' interoperability - PMML (Predictive Model Markup Language) (Data Mining Group, 2016) and PFA (Portable Format for Analytics) (Data Mining Group, 2015). The PMML formally represents analytics models to allow the exchange of analytics models between data analytics applications. The PFA covers the main functionalities of the PMML and focuses on the deployment of analytics models by streamlining the entire scoring flow. However, these standards only capture information that is related to the final stages of data analytics projects. They do not possess the capability to capture the domain knowledge that is used in the early phases of data analytics projects. The information exchange between domain experts and data analysts about the application domain relies solely on vocal discussions and written document exchange. To improve the efficiency of the information exchange in SM environment, this interoperability problem must be addressed.

Another issue that is caused by the lack of properly captured and integrated domain knowledge lies in the traceability of analytics models. Without domain knowledge being properly captured and integrated, no software tools can process and understand the documented natural language-based knowledge. This brings difficulties in carrying out data analytics projects for SM systems. As more data is collected from an SM system (as more sensors to be plugged), an analytics model that has already been developed for the SM system needs to be updated accordingly. This calls for the traceability of the domain knowledge that is used to develop the analytics model because the modification or the redevelopment of the analytics model needs the previous knowledge. To bring understanding of analytics models to downstream activities, the knowledge traceability problem must be solved.

The contribution of this paper is twofold. First, we propose to formalize domain knowledge to support the development of analytics models. Second, to allow the exchange of the domain knowledge with analytics models, we propose to integrate the formalized domain knowledge with analytics models by semantically connecting them. This paper is organized as follows: Section 2 reviews the related studies about integrating domain knowledge into data analytics. Section 3 describes the general framework to enrich analytics model with domain knowledge. To illustrate the proposed idea in detail, the development of a Bayesian Network (BN) model to predict energy consumption of injection moulding processes is investigated. So, section 4 first briefly describes this data analytics project without using the proposed enriched analytics model. Then, it elaborates the details of the development and utilization of the enriched analytics model for developing the BN model. Finally, section 5 summarizes the paper.

## Related Work

Researchers have previously tried to integrate domain knowledge and engineering models. For example, Kim et al. (2017) proposed a local model calibration approach and a local model averaging approach to incorporating domain expert knowledge into engineering process models. However, these approaches lack model interoperability which is required by SM. Kusiak (2018) mentioned that data-driven modelling and enterprise interoperability are expected to become the pillars of the future of SM. But the interoperability of analytics models was not discussed in his work. Dotoli et al. (2018) pointed out that big data analysis and semantic models are crucial for factory automation. Similarly, they did not consider the integration between analytics models and semantic models. Palmer et al. (2018) presented a comprehensive manufacturing reference ontology to support manufacturing knowledge's interoperability. However, computational models for manufacturing decision-making, especially data-driven models, were not included.

Some research was carried out in bridging the semantic gap between data and analytics models. For example, Johnson et al. (2010) proposed using an ontology to capture the domain concepts which were used to represent important variables for learning a decision tree. Although this was a good attempt in using ontologies to capture domain concepts for learning a decision tree, this study did not formalize the rules for data processing in the ontology. It also did not explicitly represent the decision tree and semantically connect the decision tree to the ontology. Trappey et al. (2013) developed a knowledge management approach using ontology-based artificial neural networks to automatically classify and search documents. In their research, the domain ontology was used as a bridge to map the concepts related to the documents to the input nodes of the neural network. However, there was no formal representations of the neural network so that there was no semantic links between the domain ontology and the neural network. Similar research on formalizing domain knowledge to bridge semantic gaps had been performed by Perez-Rey et al. (2006), Sinha and Zhao (2008), Munger et al. (2015), and Arena et al. (2018), etc. They also have problems in semantically integrating formal domain knowledge with analytics models.

There are also studies on using domain knowledge to construct analytics models. Campos and Castellano (2007) proposed learning a BN structure by specifying the structural restrictions from expert knowledge. However, no specific domain knowledge formalization and integration were shown in this research. Lechevalier et al. (2016) introduced a domainspecific modelling approach to integrate a manufacturing system model with data analytics to facilitate effective and efficient data analytics in manufacturing systems. In this research, although the manufacturing domain knowledge was captured, and the knowledge was used in creating a Neural Network structure, the domain knowledge and the Neural Network model's structure were loosely coupled. There were no mappings between the pieces of knowledge used for creating the structure and the specific structures (e.g. input neurons, hidden neurons, the structure of the Neural Network) that were captured explicitly and formally by the manufacturing meta-model. Again, the semantic links between the manufacturing meta-model and the Neural Network meta-model were missing. Kalet et al. (2017) proposed using a dependency-layered ontology, which was implemented in OWL (Web Ontology Language), to solve the inconsistency and incompatibility between different

BN models in the medical domain. However, the BN model was not formally represented. Also, there were no semantic links between the developed BN model and the ontology.

Hartmann et al. (2017) presented a model-driven analytics idea to emphasize the importance of using formalized domain knowledge in data analytics. They proposed using a domain model to explicitly define the semantics of raw data in the form of metadata, domain formula, mathematical models, and learning rules. However, the paper did not specify in what format to capture the metadata, mathematical formulas, and learning rules as well as how to integrate them. Also, the metadata model was not semantically connected to the analytics model.

To sum up, there are research gaps in (1) formalizing domain knowledge for data analytics, especially in explicitly and formally modelling the rules to process the data and constructing the analytics model; and (2) integrating formalized domain knowledge with analytics model. To address these problems, this paper proposes an enriched analytics model to enrich the formally captured analytics models with domain knowledge.

## 3. Proposed Enriched Analytics model

To support the development of an analytics model, knowledge that is needed from the SM domain can be: (1) the domain meanings of the analytics model's entities (e.g. nodes, arcs, variables, etc.), (2) the physical or behavioural information that provides insights of a certain manufacturing system on which the data analytics project focuses, and (3) reasons or descriptions about why or how a certain structure or a parameter of the analytics model is defined. To incorporate all these types of knowledge into an analytic model, in this paper, they are captured into information model(s), physics-based model(s), and rationales, respectively. Figure 1 depicts the relationships between these models and the analytics model. From the perspective of facilitating the interoperability of the enriched analytics model, all three models along with the analytics model can be modelled using a uniform text-based format like XML (Extensible Markup Language), JSON (JavaScript Object Notation) or OWL, etc. To support the traceability of the enriched analytics model, the entities which are related across models should be semantically connected. The detailed descriptions of the four models are described in the following sections.

### 3.1 Information Model

In software engineering, an information model is a representation of concepts, relationships, constraints, rules, and operations to specify data semantics for a chosen domain of discourse (Lee, 1999). Here, the information model(s) provides a common terminology for the application domain of a data analytics project. Compared to data models which have implementation-specific details, information models define concepts and relationships in a higher abstract level, and they are protocol neutral (Pras and Schoenwaelder, 2003). In manufacturing domain, for example, the ANSI/ISA-95 (ANSI/ISA, 2010) standard is an information model that defines concepts and relationships to support the interfacing between an enterprise's business system and its manufacturing control system. The B2MML (Business To Manufacturing Markup Language) (Mesa International, 2013) is an XML-based data model which implements ANSI/ISA-95.

To explicitly express the domain meanings of other models (i.e. physics-based model, analytics model, and rationales), entities from other models need to be semantically linked to the corresponding entities in information model(s). Additionally, the information model(s) also needs to be semantically connected to the corresponding data model(s) for understanding the data.

### Physics-based Model

Physics-based models are mathematical, empirical, simulation-based, and AI-based models, etc. that are developed to capture physical mechanics of a phenomenon or behaviours of an SM system. For example, forecasting models are developed to predict customer demand; production scheduling models are used for shop floor management; and cutting force models are developed for modelling material removal processes. Though these models are developed for a certain manufacturing application, the physics/behaviours captured in these models can provide valuable insights of the manufacturing system for data analytics.

Normally, the physics-based models can only be processed by specific software tools. This is because these physics-based models are normally represented as application-specific languages. For example, the mathematical optimization problems can be modelled by the AMPL (A Mathematical Programming Language) (Fourer et al. 1990) and the OPL (Optimization Programming Language) (Hentenryck, 1999), which are processable in optimization solvers like CPLEX (IBM, 2018). But it is very difficult to process optimization models in these languages outside these application-specific tools.

To enable a universal method to extract information from the physics-based models, physics-based models need to be transformed into text-based formats. The text-based formats are friendly for software tools to parse. Currently, a lot of models have the text-based representation formats. For example, The MathML (Mathematical Markup Language) is an XML-based markup language which can represent both the meaning (i.e. Content ML) and format (i.e. Presentation ML) of mathematical expressions. The PMML, as discussed previously, is developed to represent predictive models in XML. The Ontology for Optimization (Witherell et al. 2007) represents optimization models in the engineering design domain in OWL. It should be noted that, no matter by which text-based format (i.e. XML, JSON, or OWL, etc.) a physics-based model is represented, to incorporate the physics-based model(s) into an analytics model, the physics-based model(s) should be transformed into the same format as the other models (i.e. information model(s), analytics model, and rationales).

### Analytics Model

The analytics model captured here is the model for developing a data analytics project for an SM application. To facilitate the enrichment of the SM domain knowledge, models like decision trees, cluster models, regression models, Neural Network models, or BN models, etc. also need to be formally represented. To express the domain meanings, the entities in an analytics model (e.g. nodes in a BN) should be semantically connected to the corresponding domain concepts defined in the information model(s).

Current standards like PMML and PFA that provide formal representations to support interoperability of analytics models can be used to represent the enriched analytics model to formally represent analytics models. Again, the analytics model needs to be converted to the same representation format as other models.

### Rationales

In a data analytics project, the knowledge, which is a set of rules for guiding the development of an analytics model, is represented in rationales. For the knowledge from the application domain, rationales need to have connections to the related information models for obtaining the semantic meaning of the domain concepts. The rationales may also need to be linked to the physics-based models to indicate the part of system behavioural knowledge used in developing the analytics models. Also, the rationales need to connect to the analytics models to specify the links between the analytics model and the knowledge used in model development.

Like other individual models in the enriched analytics model, the rationales are also needed to be formally represented to make them processable and understandable by software tools. Because of the nature of the rationales, the rationales can be represented as rule-like styles. There are some technologies available to formally express rules. For example, the XEXPR scripting language (W3C, 2000) enables the expression of rules in XML. JsonLogic (Wadhams, 2015) allows the construction of complex rules and serialization of the rules in JSON. In OWL, the SWRL (Semantic Web Rule Language) (W3C, 2004) language can be used to build rules. The selection of the languages should conform to the overall representation technique.

## Validation of the Proposed Method Using a Case Study

To illustrate the proposed enriched analytics model in detail, this section introduces an example of data analytics project in a previous work. The overall data analytics process in the previous work without using the enriched analytics model is first introduced. Then, the reproduction of the process using the proposed enriched analytics model is elaborated. Finally, the utilization of the enriched analytics model and the benefits of using it are discussed.

### Development of A Bayesian Network for Predicting Energy Consumption of Injection moulding Processes

In a previous study (Li et al. 2017), a BN model was developed to predict the energy consumption of the injection moulding process. The advantages of using a BN to predict energy consumption of injection moulding are: (1) BN is suitable for small data sets. To train a BN model for energy estimation, data from part design, mould design, material, and machine needs to be available. Although injection moulding is one of the mass-production processes, the collected data for different products/parts may be limited. (2) A BN allows efficient use of different sources of knowledge: knowledge provided by domain experts and the knowledge learned from data. The ability to learn a BN structure from data can help the user to identify new relationships between parameters, which in turn can be used for process

improvement. (3) A BN can answer queries based on incomplete information. A designer may not possess all the information like the properties of the injection moulding machine that will be used for producing the part. A BN can provide an estimate for a query considering nearly all possible values for that missing information based on the knowledge learned from data.

To study the role of SM domain knowledge in developing the BN, a BN model was first created by learning its structure and parameters from data using the ‘bnlearn' package (Scutari and Denis, 2014) in R without the intervention of the domain knowledge. The BN nodes were selected from the parameters related to product, material, machine, process, and environment, etc. (Table I). The parameters were extracted from Nannapaneni et al. (2016). After the learning process, prediction correctness was tested. It was achieved at 76.8%, which is relatively low for effective prediction. For more information about the definition of prediction correctness, please refer to Li et al. (2017). By carefully studying the structure of the learned BN (Figure 2), we found that the learned structure missed finding important relationships and captured wrong/weak relationships instead. To improve the learned model, expert knowledge was applied to identify the problems in the model. The BN development process is shown in Figure 3.

Due to the lack of LCA (Life-cycle assessment) data from real injection moulding processes, a simulation-based data generator had been developed to generate the data. This data generator had been validated against experimental data from the literature (Ribeiro, 2012). Before learning the structure from data, a whitelist which captures important relationships between nodes was created. A whitelist, which contains arcs that need to be included in the BN, was created based on the knowledge found from mathematical equations (shown in Table II) for calculating the energy consumption of injection moulding processes. The equations are extracted from Madan et al. (2013). An equation can be considered as defining the parent/child relationships for the equation variables. The independent variables (i.e. variables on the right-hand side) of an equation are treated as the parent nodes of the dependent variable (i.e. the variable on the left-hand side).

Additionally, a blacklist, which prevents the BN from creating arcs between nodes, was created from the problems identified in the learned BN structure. Through carefully examining the learned BN structure (Figure 2), four problems were identified: (1) a parameter node (i.e. nodes which represent material, product, or process parameters) from one of the five categories (i.e. product, process, material, machine, and environment) should not have causal relationships with parameter nodes from the other four categories. For example, in Figure 2, material-related parameters like density ρ and heat capacity C_{p} are found to not dependent on material but are related to a product-related property - maximum wall thickness h_{m}, which is wrong. Though there are recommendations for the minimum wall thickness according to the injection moulded materials, h_{m} are normally designed as thin as possible. This is because thinner walls require less material and less cooling time. However, there are no recommendations for h_{m} according to different materials. (2) The concept nodes like Material and Machine should not be related to the parameters from categories other than Material and Machine, respectively. Figure 2 shows that machine property nodes of maximum clamp stroke s and injection power P_{inj} are found to be

dependent on node Material. However, the injection moulding machine is selected based on the shot size and the maximum clamp stroke, which are dependent on the product not material. (3) Parameter nodes within a category should not have parent-child relationships. It is true that within some categories, like Machine and Material, parameter nodes are related. But mainly material type or machine type determines the properties. (4) The parameter nodes from the five categories should not have any parent nodes other than the concept nodes. It can be observed in Figure 2 that parameter nodes from the five categories like injection temperature $T_{\text {inj }}$ and ejection temperature $T_{e j}$ are found to have parent nodes in the Others category like injection $t_{\text {inj }}$. However, there should not have causal relationships between $T_{\text {inj }}$ and $t_{\text {inj }}$.

By utilizing the whitelist and the blacklist, an iterative approach to learn the BN structure from data was applied (Figure 3). By using the iterative approach, the wrong arcs can be easily identified and handled during each iteration. With the whitelist and the iteratively updated blacklist, the learning procedure is repeated until no wrong arcs can be found in the BN structure. After learning the BN parameters (i.e., conditional probability tables for discrete nodes and Gaussian distributions for continuous nodes) and verifying the BN model, the development of the BN was finalized. The prediction correctness of the BN model developed with the domain knowledge was achieved at $85 \%$, which is sufficient and is higher than the learned BN model (Figure 2).

# 4.2 Development of the Enriched Analytics model 

In this section, the enriched analytics model for the BN is developed. The development of each individual model and the integration between the models are introduced. In this paper, OWL 2 (W3C, 2012) is used as the format for implementing all the models.
4.2.1 Information Model-Since the application domain of this case study is targeting at estimating energy consumption of injection moulding processes, the information model used in this paper is selected from a previous work (Zhang et al., 2015). This information model was developed to facilitate the sustainability evaluation in the manufacturing domain. This model was also extended with respect to the injection moulding process. A compact version of the information model, or the Sustainable Manufacturing Ontology (SMO), is shown in Figure 4. A brief explanation of some important concepts in the information model is narrated below:

- Product: A Product describes an object which is synthesized by a set of parts or subassemblies (each subassembly itself is also a product). The spatial relationships and contact constraints between parts are also defined within the Product class.
- Part: A Part is a single component that is used to construct a Product. A Part is a minimal functional unit of a product; thereby a part must be formed with a type of material and it has a certain geometrical shape.
- Material: A Material describes a kind of material associated with a Part. A Material has a list of properties like mechanical properties, chemical properties, thermal properties, etc. which are captured in the Parameter class.

- Process Plan: A ProcessPlan defines a sequence of manufacturing operations to produce a Part. The types of processes, types of equipment and operation parameters are specified in a ProcessPlan.
- Process: A Process describes a series of operations that need to be carried out to produce the final product. A Process can be a ManufacturingProcess or an AssemblyProcess. A ManufacturingProcess is a process that transforms a raw material into a finished or a semifinished Part. It can be a machining process, a casting process, a forging process, or a heat treatment process, etc. All the ManufacturingProcesses required to be carried out to produce a Part construct a ProcessPlan.
- Activity: An Activity is a minimal operational unit of a Process. For example, an Activity of a typical machining process can be setting up the machine, fastening the workpiece, positioning the cutting tool, injecting the cutting fluid, etc.
- Environment: The Environment class describes the environment related concepts of an Activity or a Process. All types of the environmental impacts are defined here, and each type of impacts is represented as a sustainability indicator. The sustainability of a Part or a Product can be further evaluated by considering the Processes that are carried out to produce the Part or Product.
- Parameter: A Parameter represents an entity that describes a property of a manufacturing concept. The properties of a Product, a Part, a Material, a Process, and an Activity are modelled as Parameters.
- Equipment: An Equipment can be a tool or a machine on the shop floor.
4.2.2 Physics-based Model-The physics-based models used in developing the BN are the mathematical equations which estimate the energy consumption of injection moulding (Table II). To represent mathematical equations in OWL, the OntoModel proposed by Suresh et al. (2010) has been used. In OntoModel (Figure 5), other than capturing the assumption, universal constant and dependent variable, etc., an equation can be represented using the Content ML in MathML. In Figure 5, the black boxes represent owl:classes; the green boxes are datatypes; the red arrows indicate the has-a object properties; the green arrows indicate the data properties. The OntoModel is modified so that it can be connected to the domain information model (i.e., SMO). The Variable class in OntoModel is connected to the Parameter class in the SMO, which connects the variables in an equation to their domain meanings.
4.2.3 Analytics model—To represent a BN (i.e., the analytics model) in OWL, an OWL-based BN model is developed. Figure 6 demonstrates this OWL-based BN model in a tree structure. The class names in this model are borrowed from PMML 4.3 - Bayesian Network Models (Data Mining Group, 2016). The structure of the PMML BN model is slightly modified (e.g., adding BayesianNetworkNode class, replacing the 'has-a' relationship between ContinuousDistribution and NormalDistribution with the 'hasSubClass' relationship) to better fit the OWL structure. This OWL-based BN model has

been verified with the BN example provided on the webpage of the PMML BN model. The verification proves the OWL-based BN model to be capable of fully representing BNs.

All the parameters in Table I are modelled as the BayesianNetworkNode instances in the OWL-based BN model. The semantic connection between a BayesianNetworkNode and a manufacturing concept in the SMO is achieved by an isAssociateTo(BayesianNetworkNode, domainConcept) object property.
4.2.4 Rationales-To improve the BN structure with domain knowledge, the rationales to facilitate the creation of the whitelist and the blacklist have been developed. The whitelist rules/rationales are created to capture the BN node relationships provided from the physicsbased models (i.e., equations) and domain rules. Based on the identified four problems of the learned BN structure (section 4.1), blacklist rules/rationales are developed. The blacklist rules can be used to avoid incorrect structures in the BN. All the whitelist and blacklist rules are modelled using SWRL in OWL. Object property hasParentNode represent a whitelist relationship. Object property hasWrongArc represents a blacklist relationship. To enhance the traceability of the rationales, each rule has its own corresponding numbered object property. For example, object property hasParentNode in whitelist rule 1 is hasParentNode1. The whitelist rules and blacklist rules are described as follows.

Whitelist Rule 1: This rule is created based on the physics-based models (i.e., equations in Table II). As discussed before, an equation can be considered as defining the parent/child relationships for the equation variables. The independent variables (i.e., variables on the right-hand side of an equation) of an equation are treated as the parents of the dependent variable (i.e., the variable on the left-hand side of an equation). Object property hasParentNode1 represents a parent/child relationship between two BayesienNetworkNodes.

```
DependentVariable(?dv), IndependentVariable(?iv), MathematicModel(?m),
Variable(?v_dv), Variable(?v_iv), Parameter(?p1), Parameter(?p2),
BayesianNetworkNode(?n1), BayesianNetworkNode(?n2),
hasDependentVariable(?m, ?dv), hasIndependentVariable(?m, ?iv), hasVariable(?
dv, ?v_dv), hasVariable(?iv, ?v_iv), isAssociatedWith(?n1, ?p1),
isAssociatedWith(?n2, ?p2), isAssociatedWith(?v_dv, ?p1), isAssociatedWith(?
v_iv, ?p2) -> hasParentNode1(?n1, ?n2)
```

Whitelist Rule 2: According to the classification of parameters in Table I, the manufacturing concept nodes (i.e., Machine and Machine) should have parent-child relationships with their related parameter nodes.

```
ManufacturingConcept(?mc), Parameter(?p), BayesianNetworkNode(?n1),
BayesianNetworkNode(?n2), isAssociatedWith(?n1, ?mc), isAssociatedWith(?n2, ?
p), hasParameter(?mc, ?p) -> hasParentNode2(?n2, ?n1)
```

Whitelist Rule 3: Some process parameters in the injection moulding process are selected according to the material. For example, the selection of $T_{i n p} . T_{e p} . T_{m}$, and $p_{i}$ are based on the material type (Boothroyd et al., 2011). So, causal relationships between the Material node and these process parameters should be captured.

```
Material(?m), Parameter(?pp), Process(?p), BayesianNetworkNode(?n_m),
BayesianNetworkNode(?n_pp), isAssociatedWith(?n_m, ?m), isAssociatedWith(?
n_pp, ?pp), hasParameter(?p, ?pp) -> hasParentNode3(?n_pp, ?n_m)
```

Blacklist Rule 1: To address the first problem of the learned BN structure, a set of rules to prevent connecting parameter nodes from different categories are created. Here, the rule to prevent parameter nodes from the Material and Product categories to be connected is demonstrated.

```
Material(?material), Parameter(?p_material), Parameter(?p_product),
Product(?product), BayesianNetworkNode(?n_p_material),
BayesianNetworkNode(?n_p_product), isAssociatedWith(?n_p_material,
?p_material), isAssociatedWith(?n_p_product, ?p_product),
hasParameter(?material, ?p_material), hasParameter(?product, ?p_product) ->
hasWrongArc1(?n_p_material, ?n_p_product), hasWrongArc1(?n_p_product, ?
n_p_material)
```

Blacklist Rule 2: This rule addresses problem \# 2. It avoids the Material and the Machine nodes to be connected to the parameter nodes from other categories. An example rule is shown below to prevent the Material node to be connected to the machine-related parameter nodes.

```
Machine(?machine), Material(?material), Parameter(?p_machine),
BayesianNetworkNode(?n_material), BayesianNetworkNode(?n_p_machine),
isAssociatedWith(?n_material, ?material), isAssociatedWith(?n_p_machine, ?
p_machine), hasParameter(?machine, ?p_machine) -> hasWrongArc2(?n_material, ?
n_p_machine), hasWrongArc2(?n_p_machine, ?n_material)
```

Blacklist Rule 3: Targeting at problem \# 3, this blacklist rule avoids the parameter nodes within one category to be connected to each other. The example for the material category is shown below.

```
Material(?m), Parameter(?p1), Parameter(?p2), BayesianNetworkNode(?n1),
BayesianNetworkNode(?n2), isAssociatedWith(?n1, ?p1), isAssociatedWith(?n2, ?
p2), hasParameter(?m, ?p1), hasParameter(?m, ?p2), DifferentFrom (?n1, ?n2) -
> hasWrongArc3(?n1, ?n2)
```

Blacklist Rule 4: To prevent the parameter nodes from the 5 categories to have any parent nodes other than the ones defined by the whitelist rules (problem 4), an example rule is demonstrated below for the process category. In this rule, the "hasTempParentNode" object property represents an arc learned from data.

Process(?process), Parameter(?pm), hasParameter(?process, ?pm), BayesianNetworkNode(?n_p_m), BayesianNetworkNode(?n_mc), isAssociatedWith(?n_p_m, ?pm), hasTempParentNode(?n_p_m, ?n_mc) -> hasWrongArc4(?n_p_m, ?n_mc)

### Representation of the Enriched BN Model in OWL

During the development of the enriched BN model, the individual models for the information model, analytics model, and physics-based model are separately created first. These models are general and could be applied to any applications and do not have any populated instances. After verifying that all the individual OWL-based models can sufficiently represent the models, the enriched analytics model is then created by importing the three OWL-based models into the OWL-based enriched analytics model. Instances of the domain concepts in the SMO, the BayesianNetworkNodes in the BN model, and the equations represented by the OntoModel are populated. The whitelist and blacklist rules are then created using the SWRL rules. All these models and rules are implemented in protégé 5.2, which is an opensource ontology editor. The screenshot of the enriched BN model in protégé is demonstrated in Figure 7.

Figure 8 shows a screenshot of reasoning the rationales (i.e. whitelist and blacklist rules). The object property assertions highlighted in light yellow are inferred relationships from reasoning the rationales. It can be observed that the rationale used to create or eliminate an arc can be easily tracked by using the numbered object properties.

### Utilization of the Enriched Analytics model

Following the development process (Figure 3), a BN is developed (Figure 9) by utilizing the enriched analytics model. In the development process, the enriched analytics model has been used to exchange information between a domain expert and a data analyst. The domain expert first models the domain knowledge (integrating the information model, adding the physics-based model, creating rationales) for the development of the BN. Then, the data analyst iteratively learns the BN structure from data with the whitelist and the blacklist, which are extracted from the enriched BN model through a parser (that has been developed for this purpose). Here, the enriched BN model is used to pass the BN along with its relevant domain knowledge between the domain expert and the data analyst. After sending the enriched BN model with the learned structures, the domain expert can analyse the BN structure and add the corresponding rationales to improve the BN structure. The domain expert can directly add or modify domain knowledge on the enriched analytics model in GUI (Graphical User Interface) -based software tools like protégé. Figure 10 is a sequence diagram that shows the information exchange.

# 4.4 Discussion 

Two benefits have been identified during the development of the BN using the enriched analytics model: (1) Shortened cycle time for the analytics model development. In this case study, with the assistance of automatic processing and reasoning from the software tools, the development cycle time has been reduced from 2 hours to 15 minutes. With the formally defined rationales, the arcs captured by the whitelist and the blacklist can be generated automatically instead of working manually. (2) Eliminating human error. Through reasoning the formally defined rationales, more arcs in the blacklist have been identified. Some of these arcs can be easily missed by manual work.

These two direct benefits are brought by the enhanced interoperability and traceability of the enriched analytics model. From the perspective of enhancing interoperability, the enriched analytics model can explicitly represent the analytics models with their relevant domain knowledge through capturing their concepts, relationships, and rules, etc. without semantic ambiguity; the analytics models and their relevant domain knowledge are formally represented, which enables the automatic processing through software tools. From the perspective of enhancing traceability, the entities of an analytics model can be directly traced to its corresponding domain concepts; the analytics models' structures can also be easily traced to the rationales which are used to create these structures. It can be expected that with the enhanced interoperability and traceability, more effective and efficient information exchange can be achieved by using the enriched analytics model in a distributed environment, where the domain experts and the data analysts are not necessarily in the same geographical area.

Further efforts need to be done to implement a platform to support the formal communications with the proposed enriched analytics model in real production applications. Technically, the parser of the OWL-based enriched analytics model is developed on top of OWL API (Horridge and Bechhofer, 2010). OWL API is a Java-based open-source OWL editor which also supports the same reasoning capability as protégé. So, the authors suggest to integrate OWL API-based parsers/reasoners into the industrial tools to support the parsing and reasoning of the OWL-based enriched analytics model. Additionally, domain experts can use protégé to directly edit an enriched analytics model since protégé has a friendly user interface for knowledge modelling.

## 5. Conclusion

This paper proposed a methodology to enrich analytics models with domain knowledge to facilitate data analytics in a Smart Manufacturing environment. The motivation for encapsulating an analytics model and its domain knowledge in a single model came from the need for interoperability and traceability. To model the SM domain knowledge, this paper proposed to explicitly and formally represent domain information models, physics-based models, and rationales. Information models are used to bridge the semantic gaps between the SM domain and the data analytics applications. By formally representing the physics-based models, the knowledge captured in the physics-based models can be reused. The rationales, which are used to develop the analytics model, are digitally documented to enhance traceability. The formal representation of the targeting analytics model can be modelled

based on the existing standards like PMML or PFA. To enrich an analytics model, the formally represented domain information models, physics-based models, and rationales should be semantically integrated with the analytics model.

A case study from a previous study, where a Bayesian Network model was developed to predict the energy consumption of the injection moulding process, was used to illustrate the development and utilization of the enriched analytics model. The components of the enriched analytics model are: a manufacturing domain information model, a set of mathematical equations as the physics-based models, the whitelist/blacklist rationales for constructing the BN, and the formally represented BN model. All these models are implemented using OWL. The case study demonstrates the benefits from utilizing the enriched analytics model: shortened cycle time for model development and eliminating human error. These two benefits come from the enhanced interoperability and traceability of the analytics model and its relevant domain knowledge.

# Acknowledgement and Disclaimer 

This work has been sponsored under the cooperative agreement between the U.S. National Institute of Standards and Technology (NIST) and Syracuse University.

Certain commercial systems are identified in this article. Such identification does not imply recommendation or endorsement by NIST; nor does it imply that the products identified are necessarily the best available for the purpose. Further, any opinions, findings, conclusions, or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of NIST or any other supporting U.S. government or corporate organizations.
