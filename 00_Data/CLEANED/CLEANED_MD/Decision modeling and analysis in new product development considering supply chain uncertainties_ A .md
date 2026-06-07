# Decision Modeling and Analysis in New Product Development Considering Supply Chain Uncertainties: A Multi-Functional Expert Based Approach 

Mohit Goswami ${ }^{\mathrm{a}}$, Yash Daultani ${ }^{\mathrm{b}}$, Arijit De ${ }^{\mathrm{c}}$<br>${ }^{a}$ Operations Management Group, Indian Institute of Management Raipur, Raipur, India<br>${ }^{\text {b }}$ Operations Management Group, Indian Institute of Management Lucknow, Lucknow, India<br>${ }^{c}$ Newcastle University Business School, Newcastle Upon Tyne, United Kingdom<br>${ }^{a}$ E-mail: mgg123456@gmail.com<br>${ }^{b}$ E-mail: Yash.daultani@gmail.com<br>${ }^{c}$ E-mail: arijit.de22@gmail.com

# Decision Modeling and Analysis in New Product Development Considering Supply Chain Uncertainties: A Multi-Functional Expert Based Approach 


#### Abstract

Successful new product development projects and extant research literature advocate for inclusion of inputs pertaining to the supply chain at early stages of product development to proactively identify risk averse product design concepts. To this end, we devise an analytical framework to converge upon product design concept(s) that would be associated with lesser supply chain risks, usually function of both technical and commercialization considerations. The high-level and constituent lower-level supply chain risks are represented by parent and root nodes respectively within the devised Bayesian network driven research framework. Thereafter, a quantitative measure denoted as SCRI (supply chain risk index) is evolved that yields overall composite risk numbers corresponding to respective design concepts at different risk states. Validation and comparison of the devised method with an extant study illustrates the consistency and reliability of the study. It is found that the risk propensity of a particular design concept is inversely related to the probabilistic utility of that particular concept. The case of a construction power tool of a global firm is used to demonstrate the methodology. Our research addresses an important future research pathway as argued by Hosseini et al., (2020) that extant research literature is devoid of decision-making frameworks focused on measurement and analysis the propagation of risks on complex networks.


Keywords: Decision support systems, New Product Development, Supply chain risk management, Design concept selection.

# Parameters 

$X_{i j}=$ If module instance " $j$ " is chosen for module " $i$ ".
$C_{r}=$ Parent node " $r$ ".
$d_{q}=$ Root node " $q$ ".
$g_{t}=$ combination of root nodes " $t$ ".
$p\left(C_{r}^{H} / d_{q}^{H}\right)_{v}=$ Probability of node "r" in state "H" provided node "q" is in state "H" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{H} / d_{q}^{M}\right)_{v}=$ Probability of node "r" in state "H" provided node "q" is in state "M" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{H} / d_{q}^{L}\right)_{v}=$ Probability of node "r" in state "H" provided node "q" is in state "L" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{M} / d_{q}^{H}\right)_{v}=$ Probability of node "r" in state "M" provided node "q" is in state "H" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{M} / d_{q}^{M}\right)_{v}=$ Probability of node "r" in state "M" provided node "q" is in state "M" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{M} / d_{q}^{L}\right)_{v}=$ Probability of node "r" in state "M" provided node "q" is in state "L" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{L} / d_{q}^{H}\right)_{v}=$ Probability of node "r" in state "L" provided node "q" is in state "H" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{L} / d_{q}^{M}\right)_{v}=$ Probability of node "r" in state "L" provided node "q" is in state "M" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{L} / d_{q}^{L}\right)_{v}=$ Probability of node "r" in state "L" provided node "q" is in risk state "L" as determines by stakeholder " $v$ ".
$p\left(C_{r}^{H} / g_{t}^{H}\right)_{v}=$ Probability of node "r" in state "H" provided paired nodes"t" is in state "H" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{H} / g_{t}^{M}\right)_{v}=$ Probability of node "r" in state "H" provided paired nodes"t" is in state "M" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{H} / g_{t}^{L}\right)_{v}=$ Probability of node "r" in state "H" provided paired nodes"t" is in risk state "L" as determined by stakeholder " $v$ ".

$p\left(C_{r}^{M} / g_{t}^{H}\right)_{v}=$ Probability of node "r" in state "M" provided paired nodes"t" is in state "H" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{M} / g_{t}^{M}\right)_{v}=$ Probability of node "r" in state "M" provided paired nodes"t" is in state "M" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{M} / g_{t}^{L}\right)_{v}=$ Probability of node "r" in state "M" provided paired nodes"t" is in state "L" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{L} / g_{t}^{H}\right)_{v}=$ Probability of node "r" in state "L" provided paired nodes"t" is in state "H" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{L} / g_{t}^{M}\right)_{v}=$ Probability of node "r" in state "L" provided paired nodes"t" is in state "M" as determined by stakeholder " $v$ ".
$p\left(C_{r}^{L} / g_{t}^{L}\right)_{v}=$ Probability of node "r" in state "L" provided paired nodes"t" is in risk state "L" as determined by stakeholder " $v$ ".
$p\left(d_{q / j_{i}}^{H}\right)_{v}=$ Prior probability of root node " $d_{q}$ " in risk state "H" for module instance " $j_{i}$ " as evaluated by stakeholder " $v$ ".
$p\left(d_{q / j_{i}}^{M}\right)_{v}=$ Prior probability of root node " $d_{q}$ " being in risk state "M" for module instance " $j_{i}$ " as evaluated by stakeholder " $v$ ".
$p\left(d_{q / j_{i}}^{L}\right)_{v}=$ Prior probability of root node " $d_{q}$ " being in risk state "M" for module instance " $j_{i}$ " as evaluated by stakeholder " $v$ ".
$\operatorname{SCRI}\left(r / j_{i}\right)_{v}=$ Supply chain risk index for parent node " $r$ " for module instance " $j_{i}$ " as evaluated by stakeholder " $v$ ".
$p\left(Z_{t, j_{i}}^{H}\right)_{v}=$ Prior probability of module instance $j_{i}$ in high risk state provided $t^{t h}$ combination of nodes is in state "H" as evaluated by stakeholder " $v$ ".
$p\left(Z_{t, j_{i}}^{M}\right)_{v}=$ Prior probability of module instance $j_{i}$ in high risk state provided $t^{t h}$ combination of nodes is in state "M" as evaluated by stakeholder " $v$ ".
$p\left(Z_{t, j_{i}}^{L}\right)_{v}=$ Prior probability of module instance $j_{i}$ in high risk state provided $t^{t h}$ combination of root nodes is in risk state "L" as evaluated by stakeholder " $v$ ".

# 1. Introduction 

Conventionally, NPD (new product development) is often thought of as a stage-gate based process wherein product design concepts are selected based on broad business and technical needs, followed by realization of physical prototypes, testing and, validation, mass production, and finally product launch (Ulrich and Eppinger, 2017). However, in order to improve TTM (time to market), reduce life cycle costs, and facilitate smooth launch of new products, OEMs (original equipment manufacturers) have been increasingly taking a concurrent view of product development to include supply chain partners that are internal to the organization and external vendors, for advance and proactive validation of technical and commercial concerns (Petersen, et al., 2005 and Long, 2016). For instance, sometimes an OEM includes suppliers to evaluate computer aided designs (even before release of engineering drawings) of components that suppliers would be tasked to manufacture in order to gauge integrational aspects related to the product and manufacturability related concerns of components. Furthermore, with increased intricacies of contemporary manufacturing supply chains wherein several vendors supply different (with varying lead times) parts to the manufacturer for an end product, it is quite obvious that manufacturers need to consider supply chain related concerns during the design concept selection stage within NPD projects. The need to include supply chain related concerns at early stages of new product development has been also adequately emphasized by the extant research literature as well (Marsillac et al., 2014, and Pashaei et al., 2015).

Within a NPD project, design concept selection is often considered to be perhaps one of the critical decisions that OEMs need to undertake for subsequent development and commercialization of associated product lines (Yang et al., 2015 and Aarikka-Stenroos et al., 2012). Selecting a sub-optimal design concept may have an adverse influence on the targeted performance of enterprises in terms of escalated costs, reduced quality levels and inferior delivery performance indicators (Zhao \& Cao, 2015, and Zhao et al., 2014). Further, to validate design concepts, manufacturers often carryout physical testing and validation activities. These activities may include technical validations such as performance testing and market validation such as prelaunch for consumer assessment. The problem associated with such a conventional approach however is that significant resources both in monetary terms and in terms of the number of manhours spanned across different functional agencies of the enterprise are invested. Design concept selection is driven by multifunctional inputs in terms of involvement of various supply chain

stakeholders handling the product either in physical or abstract form at various stages of the valuechain (for instance, the production department for manufacturing and assembly; marketing department for gauging the mapping of product to customer needs). Thus, it would be fairly prudent to assert that design concept selection is characterized by uncertainties that, if not recognized and mitigated early in NPD properly, can derail the targeted supply chain performance of the manufacturer (Kaki et al., 2015, Zacharia et al., 2011, and Karna et al., 2017). A key motivation for our research rationale is IBM's design for supply chain (DfSC) program that emphasizes end-to-end collaboration to optimize a product before it takes shape in physical form (Brody et al., 2013, and Das et al, 2015). The aim here is to apply the life cycle management mentality at the design concept selection stage such that products can be developed and commercialized for optimal supply chain efficiency.

In view of the foregoing arguments, it is imperative that manufacturers evaluate feasible design alternatives in a structured manner by taking into account major supply chain concerns aimed at identification of design concept(s) associated with least overall supply chain risk. Evaluating the design concepts would however require answering the following research questions.
a) Considering that supply chain risks are often layered, how can accompanying supply chain risks be represented in various strata (s)?.
b) How can we ascertain on a composite level, overall supply chain risk index (SCRI) for a design concept that is characterized by modular architecture?

To respond to these two primary research questions, we consider a typical OEM that needs to select amongst feasible design alternatives, design concept(s) associated with least value of SCRI. Planning, sourcing, operational, logistics, market and aftersales related uncertainties are the broad components of supply chain risk considered in this research. Employing the Bayesian theory, each of the six risk components are segregated in terms of parent and root nodes. Each of these parent and root nodes are also assumed to exist in three risk states, specifically, high, medium, and low. The research problem is formulated in terms of an optimization model wherein the objective is to select the optimal combination of modules' instance associated with the least SCRI considering constraints pertaining to operationalization of design concept, module selection, and compatibilities amongst modules' instances. We demonstrate our research framework employing an example of construction power tool product line of a global firm. In particular, our research

addresses an important future research pathway as advocated by Hosseini et al., (2020) that argued that extant research literature is devoid of decision-making frameworks focused on measurement and analysis the propagation of risks on complex networks. As far as the scope of supply chain risks in the study are concerned, they are primarily regional in nature in that, the OEM primarily relies upon regional design and sourcing capabilities to ensure presence of its product line in the market space. Dimensions related to international supply chains such as risks related to sourcing from multiple international locations/off-shoring etc. are beyond the scope of our work.

The remainder of the paper is organized as follows. Section 2 presents the literature review followed by the methodology and details of the model in Section 3. Sections 4 and 5 enumerate the model formulation and illustrative example, respectively. The results and validation are discussed in detail in Section 6. Finally concluding remarks, limitations and pathways for future research are presented in Section 7.

# 2. Literature review 

In this section, we discuss some of the relevant and recent research literature. In particular, our research framework evolves from primarily two domains viz. a) product design and supply chain; b) Bayesian network and probabilistic interference. We particularly consider the viewpoint from production research and operations management.

### 2.1 Product design and supply chain

There has been a number of extant literature that bridges the aspects of product design with that of supply chains. These studies fall into both empirical as well as mathematical modelingbased approaches. Chui and Okunduan (2014) investigated the effect of extent of modularity on supply chain performance. An important contribution of the research was in terms of the introduction of an analytical framework demonstrating that increased level of modularity facilitates enhanced time to market performance, while reduced level of modularity aids in achieving cost efficiency. Oehmen et al. (2009) introduced a systems-oriented perspective in supply chain risk management. Further, this research also devised a supply chain risk oriented dynamic model to predict the possible dynamics of supply chain risks. Shahzad et al. (2013) proposed the concept of sustainable mass customization to address specific challenges faced by manufacturers when a non-performing product within the market space(s) needs to be replaced

with a superior product thus hindering the existing mass customization effort(s) of a given enterprise. A key contribution of the work was in terms of a Go/No-Go decision set for specific market segments for mass customization. The developed simulation model was tested with varying market segment demands, sales prices, and product costs. Marsillac et al. (2014) connected product design, process capabilities, and supply chain decisions by employing a case study-based approach, thus aiding global supply chain capabilities to be strengthened. Droge et al. (2012) employing the empirical study populated a number of key insights. The study inferred that the lack of direct correlation between process modularity and service performance imply that modular processes: a) lack intrinsic interfaces such as those found in corresponding product architectures; and b) are reliant upon integrational aspects to fulfil the role of interface. Sokolov et al. (2016) formalized the ripple effect in supply chains by including key performance indicators such as resilience, robustness and stability. Lavigne et al. (2016) proposed a methodology for joint optimization of product family and supply chain design. The model was based upon populating several scenarios representing uncertain parameters within the model. Rodger et al. (2014) employing the data on acquisition history used regression method to forecast backorder aging using National Item Identification Numbers (NIINs) as unique identifiers in the context of defense logistics. The complexities and uncertainties in their study were captured using Bayesian theory. A key benefit of the study was that the devised probabilistic estimation decision support tool could be deployed for other Department of Defense systems. Caniato et al. (2015) investigated the impact of product design complexity on organizational performance. An important contribution of their paper was that product design complexity alone does not have moderating effect on NPD supply chain integration. Shidpour et al., (2016) proposed a new decision-making method to evaluate product design concepts based on the distance between interval vectors. Gokhan et al. (2010) investigated and quantified potential benefits of design for supply chain by simultaneously tackling product design decisions and supply chain related considerations. Gan et al. (2016) employing an exploratory literature review proposed a concurrent design attribute trade-off pyramid as an operational level deliverable for integrated concurrent product design-supply chain decisions. Broeke et al. (2015) bridged product family decisions with costs within the supply chain network. The key decisions that the research sought to converge upon pertained to; a) number of platforms to develop; b) which platform(s) to develop; and c) which products to be derived from which platform. An important indicator of the extent of commonality/differentiation within a

product family is often the commonality/differentiation index. To this end, Alizon et al. (2009) evolved a commonality and differentiation index (CDI) to cater to two purposes: a) ascertain the degree of commonality to gauge the extent of economy of scale, and, b) ascertain degree of differentiation to gauge the extent to which diverse customer needs are met. Jiao et al. (2007) in their state of art review article identified primarily two research challenges from a product family perspective. The first challenge pertained to redressal of manufacturing and production related challenges such as management of process variety, determination of optimal production pertaining to supply chain management including sourcing/outsourcing tactics, decoupling, supply chain configuration design and resource allocation.

# 2.2 Bayesian network and probabilistic interference 

Cao et al., (2019)'s work revolved around quantitative assessment of impact of dynamic risk propagation within and between integrated firms in global fresh produce supply chains. In particular, ontology based Bayesian network (BN) was evolved in the study for considering the traceability related to root nodes representing the supply chain risks. Chen et al., (2020) evolved a novel learning cloud BN for risk analysis for selection of civil engineering projects. It was ascertained in the study that cloud based BN is more adaptive and effective in capturing the forward and backward propagation as compared to traditional BNs. Hossieni et al., (2019) in context of resilient supplier selection problem devised a methodology for determining the likelihood of disruptive events using a probabilistic graphical model. In particular, the research contributions primarily revolved around identifying optimal level of restorative and surplus capacities. Hossieni and Ivanov (2019) theorized a novel measure to quantify the resilience of the OEM using a multi-stage assessment of suppliers' proneness to disruptions and the SC's (supply chain's) exposure to the ripple effect. The study also tested the developed notion of SC resilience as a function of supplier vulnerability and recoverability using a Bayesian network while considering disruption propagation. Kammouh et al., (2020) introduced a new approach to assess the time-dependent resilience of engineering systems using resilience indicators based on causal BN. The study's contribution primarily pertained to application of dynamic BNs to engineering systems (as opposed to static BNs). Wan (2019) devised a novel model for evaluating the risk factors of maritime supply chains by incorporating a fuzzy belief rule approach with BNs. The new model, compared to traditional risk analysis methods was demonstrated to have the capability

of improved result accuracy under a high uncertainty in risk data. The work carried by Chin et al., (2009) was first review of BN considering supply chain risks. Using the BN structure characterized by root and parent nodes (representative of supply chain risks), the study discriminated one product type from the other in terms of utilities associated at different risk states (i.e. high, medium and low). These utilities were essentially function of experts' probabilistic assessment of two types of products considered in the research based on the relationship amongst root and parent nodes.

However, the research carried out by Chin et al., (2009) had a number of noteworthy limitations. First, the study took a rather simplistic view of product structure in that the product considered (penlight) essentially is an integral product wherein a single probabilistic assessment differentiates one design concept from the other. However, in reality vast majority of products (however simplistic the associated design and functions may be) are often characterized by modularity such that different modules and their associated probabilistic evaluation drives the overall supply chain risk associated with that product. Second, considering multiple probabilistic evaluations of associated modules by multiple experts would automatically lead to significant computational enumeration; an important dimension that Chin et al., (2009) did not consider as the study considered only one set of probabilistic evaluation corresponding to only a single module. Third, the probabilistic evaluation from multiple experts with respect to parent and root nodes (leading to overall risk score) would have to be considered for final concept selection decisions; an important consideration that remained rather abstract in Chin et al. (2009) as it considered only one expert's evaluation. Finally, the overall risk associated with a product would be contingent on the aggregate conditional probability of the BN (characteristics of supply chain risk network) and prior probabilities (individual supply chain risks of individual modules). Chin et al., (2009) essentially considered only the aggregate conditional probability associated with the product development project's BN (without taking into account prior probabilities associated with the product).

Table 1 captures the relevant research dimensions and contrasts our scope of work with respect to some recent studies.
<<Insert Table 1 here>>
The above presented studies highlight the need for inclusion of supply chain related considerations in the planning and execution stages of design concept selection. We will for the

sake of illustration of our analytical framework, adhere to the product design concept selection problem of a construction power tool product line.

The motivation for our approach is driven by the fact that supply chain related decisions at planning and operational levels can only be taken once the detailed design activities (final concept freeze, release of drawings/technical specifications and so forth) have been carried out. However due to market related challenges such as ever shrinking product life cycles and the need to compress time to market owing to competitive pressures, it is imperative that enterprises predictively (and proactively) identify the risk prone design concepts at early stages of NPD itself. The idea here is to consider concurrency of the product development process and gauge design alternatives from a supply chain perspective, so that subsequent risks arising out of handling by supply chain stakeholders involved within the value-chain of company can be mitigated to a higher degree proactively. Goswami (2018) in his work had evolved a measure for assessing the risks associated with a product line. Chin et al., (2009) had also evolved the framework for aggregate risk measurement for limited set of design concepts. However, our study makes significantly deeper contributions with regard to extant studies in terms of the following.
a) First, Goswami et al., (2018) did not carry out any validation of its proposed $\operatorname{PS}\left(P L_{X}\right)$ - measure of overall risk associated with a product line. We in our study, however, contrast the devised SCRI measure with regard to the probabilistic design utility measure as proposed by Chin et al., (2009), thus uncovering that probabilistic design utility measure holds a negative relationship with respect to the devised SCRI measure.
b) Second, the network model conceptualized in Goswami et al., (2018) and Hosseini et al., (2019) was rather intractable in that interdependencies amongst root and parent nodes were considered thus resulting in significant computational effort. These interdependencies though play a minor part in overall risk score of a particular product line at initial screening stages pertaining to analysis of design concept. To this end, in context of design concept assessment at early stages of product development, evaluation with respect to independent supply chain risk network is more desirable as it would be of much more interest as to how individual supply chain dimensions impact concept selection decisions. This implies that design concepts are purely evaluated from the perspectives of the six supply chain high level risks considered in this study.

c) Third, the methodology proposed by Goswami et al. (2018) did not recognize the fact that optimal design concept may be different for the customer and for the enterprise. To this end, we treat the optimal design concept selection from both the customer's and the enterprise's perspective. In particular, divergent perspective of addressing the design concept selection problem is motivated by the work of Cao et al., (2019) that viewed minimization of aggregate risk for an agricultural supply chain from the perspectives of both customer value and supplier risk.
d) Finally, Goswami et al., (2018) addressed the product line design collectively from three perspectives viz. planning, sourcing, and logistics. In our study, we address the design concept selection problem from a broader supply chain perspective in that risks related to planning, sourcing, operational, logistics, market and aftersales are considered. Further, as opposed to the work of Shen et al., (2019) wherein risk assessment was based on a single focus group (thus essentially imposing consensus within the expert's focus group), our approach considers inputs from all concerned experts. The objective essentially here is to ensure inclusion of inputs from all concerned experts such that overall risk measurement does not have to necessarily follow an artificially imposed consensus based assessment.

# 3. Research Methodology and Model Setting 

### 3.1 Research Methodology

In our research environment, a manufacturer needs to select a particular design concept from a number of design alternatives for subsequent development and commercialization by seeking to converge at a design solution that is associated with least SCRI. Given the MCDM (multi-criteria decision-making) nature of the problem and accompanying considerations in terms of layers of risks pertaining to the supply chain, we employ a Bayesian network methodology to map risk propensities. There are two broad rationales for application of the Bayesian network in this research. First, owing to the ability of the Bayesian network (as opposed to other methodologies such as analytical network process) to represent given risk related dimensions in terms of parent and associated root nodes, we specifically utilize a Bayesian modeling approach for our underlying problem. Second, modularity aspect as considered in this work, results in a number of module instances corresponding to respective modules. Since these module instances

(of respective modules) have their own intrinsic risk propensities in terms of pertinent risks from both an independent and interdependent perspective, the Bayesian approach has been adopted to model such characteristics. Further, there are a number of product related considerations as well that need to be captured in terms of suitable mathematical relationships. For instance, constraints related to functionality of product, selection of a particular module instance corresponding to the product, and module compatibilities/incompatibilities have been represented in terms of mathematical expressions that are functions of module instances. In view of the problem characteristics discussed above, in this research, we have devised an optimization model wherein decision variables pertain to selection of a particular module instance of a given module within the product such that cumulative risks at high, medium, and low risk states are minimum while satisfying the product related considerations.

# 3.2 Model setting 

### 3.2.1 Design concept representation

Suppose a manufacturer needs to select a design concept, $Z$ for subsequent development and commercialization. The selected design concept $Z$ such that $Z \in\left(Z_{1}, Z_{2}, \ldots ., Z_{i}\right)$, thus, would have a number of associated modules $Z_{i}$ such that $i \in I$; and $I$ is number of required modules for a product to be operational. Further, each of the modules $Z_{i}$ would have a number of possible module instances $Z_{i j} \mathrm{~s}$ such that $j \in J_{i}$.

The integration of module instances of respective modules would also be driven by compatibility/incompatibility constraints. An instance of such a consideration would be incompatibility of digital signal processing module with an analog signal processing system. If $C$ is the number of total module-instances available, then $C$ can be formulated employing the following mathematical relationship.
$C=\sum_{i=1}^{J} J_{i}$
In the above equation $J$ is total number of module instances available for module " $i$ ".
Matrix $M$ containing $C$ number of rows and columns can be formulated as below.
$M\left(Z_{i j}, Z_{p q}\right)>0 \quad \forall i \neq p ; j \neq q$

# 3.2.2 Modeling the supply chain risks from a Bayesian perspective 

A product designed within the organizational framework of an enterprise needs to receive inputs from multiple supply chain related functionalities before it assumes physical shape that satisfies all form and fitness requirements. Figure 1(a) illustrates the involvement of different supply chain related functionalities in the context of the design concept selection problem.

## <<Insert Figure 1 here>>

Referring to Figure 1(a), it can be inferred that we have considered two types of supply chain functional risks in our model. Marketing and service risks are considered as consumer related risks as these are the risks that directly impact customer's perception about the product. For example, a product having integrated architecture (as opposed to a modular product) would be more difficult to service; hence the service risks associated with such architecture would be higher. We specifically consider six different types of supply chain related risks (represented by parent risk nodes) as considered by the work of Daultani et al. (2017). For definition of these risks, Daultani et al., (2017) can be referred. Further, each of these parent risk nodes are subdivided into root node risks. Parent and root nodes have three different risk states: high (H), medium (M), and low (L). All the parent nodes and their associated root nodes together form the SCRI. This risk index would form the basis for evaluation of a product design concept. The concept associated with least SCRI would be closest to the enterprise's supply chain related targeted metric. Table 2 illustrates the parent nodes and the associated root nodes.

## <<Insert Table 2 here>>

### 3.2.2.1 Prior probabilities

If there exists $n$ disparate states i.e. $S_{1}, S_{2}, S_{3} \ldots \ldots . S_{n}$ of a node without having a parent node and probability of a particular state $S_{k}$ i.e. $P\left(S_{k}\right)$ need to be specified.
$P\left(S_{k}\right)$ can be determined by comparing just two states at a time (rather than comparing $n$ different states) employing the pair-wise comparison matrix method as deployed by Chin et al., (2009) such that following mathematical express is satisfied.
$P\left(S_{k}\right)=\mu_{k}$
$\mu_{k}$ denotes relative importance of state $S_{k}$ among all the states.

# 3.2.2.2 Conditional probabilities 

A single root node network containing a parent node M and a root node N together constitutes a causal relationship. All states of node M and N can be represented by $S_{M 1}, S_{M 2}, S_{M 3}$, ..... $S_{M p}$. and $S_{N 1}, S_{N 2}, S_{N 3}, \ldots . . S_{N q}$ respectively. In this case, our objective would be to determine the probabilities of individual state of node N conditional on each state of node M i.e. $P\left(S_{M j} / S_{N i}\right)$. In the case of single root node system, we can populate the pairwise comparison matrix and using the method deployed by Chin et al. (2009), the conditional probabilities can be ascertained using following mathematical expression.
$\mathrm{P}\left(N=S_{N j} / M=S_{M i}\right)=w_{i n}$
In the above equation $w_{i j}$ is the likelihood of node N being in state $S_{N j}$ given that node M is in state $S_{M i}$.

### 3.2.2.3 Conditional probabilities for multi-root node system

A multi-root node system in illustrated in Figure 2.
<<Insert Figure 2 here>>
Due to multiple combinations of root nodes and associated risk states, obtaining probabilities of each state of N contingent on a combination of states of its root node formulated as $\quad P\left(N=S_{R j} / M 1=S_{A 1 r 1}, M 2={ }_{S A 2 r 2}, M 3={ }_{S A 3 r 3}, \ldots . . M k=S_{A k, i k}\right)$ would be computationally unrealistic. Hence, it would be intractable to gauge the relationship between combinations of individual states of nodes M and N. Therefore, using the method as deployed by Goswami et al., (2018) and Chin et al. (2009) in context of a multi-root node system, the conditional probability can be ascertained using following mathematical equation.
$P\left(B=S_{R j} / A 1=S_{A 1 r 1}, A 2={ }_{S A 2 r 2}, A 3={ }_{S A 3 r 3}, \ldots . . A k=S_{A k, i k}\right)=\alpha \times \prod_{j=1}^{n} P\left(B=S_{A i} / B_{j}=S_{R j i j}\right)$

Where $\alpha$ is normalization factor to ensure that its value is equal to 1 .

## 4. Model Setting

In our problem environment, there are $V(v=1,2,3 \ldots . . V)$ number of supply chain stakeholders representing the six supply chain functionalities as enumerated earlier.

The value of a supply chain risk node being judged by stakeholder $v$ for module instance $j_{i}$ for module $i$ corresponding to $r^{t h}$ parent node being in high risk state given that $t^{t h}$ combination of root nodes are in high risk state, can be mathematically expressed by the following term.
$\left\{p\left(C_{r}^{H} / g_{t}^{H}\right)_{v} \times p\left(Z_{t, j_{i}}^{H}\right)_{v}\right\}$

Where $p\left(C_{r}^{H} / g_{t}^{H}\right)$ is the aggregate conditional probability for $r^{t h}$ parent node being in high risk state given that $t^{t h}$ combination of root nodes is in high risk state.
$p\left(Z_{t, j_{i}}^{H}\right)$ denotes the prior probability of module instance $j_{i}$ being in high risk state given that $t^{t h}$ combination of root nodes is in high risk state.

The objective function (for stakeholder $v$ ) at high risk state for the least risk averse function such that SCRI is minimized can be formulated by the following equation.
$F_{v}^{H}=\operatorname{Min}\left[\prod_{i \in I}\left[\prod_{r \in R} p\left(C_{r}^{H} / g_{t}^{H}\right)_{v} \times p\left(Z_{t, j_{i}}^{H}\right)_{v}\right]\right]$
Similarly, corresponding to the medium and low risk states, the SCRI can be formulated by the following mathematical relationships.
$F_{v}^{M}=\operatorname{Min}\left[\prod_{i \in I}\left[\prod_{r \in R} p\left(C_{r}^{M} / g_{t}^{M}\right)_{v} \times p\left(Z_{t, j_{i}}^{M}\right)_{v}\right]\right]$
$F_{v}^{L}=\operatorname{Min}\left[\prod_{i \in I}\left[\prod_{r \in R} p\left(C_{r}^{L} / g_{t}^{L}\right)_{v} \times p\left(Z_{t, j_{i}}^{L}\right)_{v}\right]\right]$
Further, we also intend to determine the distribution of objective functions in each risk state i.e., high, medium, and low considering inputs of $V$ stakeholders. Assuming a normal distribution, the distribution functions in high, medium, and low risk states are represented by functions $N\left(\mu_{H}, \sigma_{H}\right), N\left(\mu_{M}, \sigma_{M}\right)$, and $N\left(\mu_{L}, \sigma_{L}\right)$ respectively, such that the following equations are satisfied.
$\mu_{H}=\left(\sum_{v \in V} F_{v}^{H}\right) / V$

$\mu_{M}=\left(\sum_{v \in V} F_{v}^{M}\right) / V$
$\mu_{L}=\left(\sum_{v \in V} F_{v}^{L}\right) / V$
$\sigma_{H}=\operatorname{stddev}\left(F_{1}^{H}, F_{2}^{H}, \ldots \ldots . . F_{v}^{H}\right) \forall v$.
$\sigma_{M}=\operatorname{stddev}\left(F_{1}^{M}, F_{2}^{M}, \ldots \ldots . . F_{v}^{M}\right) \forall v$.
$\sigma_{L}=\operatorname{stddev}\left(F_{1}^{L}, F_{2}^{L}, \ldots \ldots . . F_{v}^{L}\right) \forall v$.
The objective function proposed in equation 6,7 and 8 will be subject to the below constraints.
a) Product operational constraint: This constraint would ensure that the desired product design concept contains all required modules for the product to be operational. Following mathematical relationship ensures this constraint.

$$
\sum_{i \in I} \sum_{j \in J_{i}} X_{i j}=I \forall i, j
$$

b) Module selection constraint: Only one module instance for a given module will be selected for the desired design concept.

$$
\sum_{j \in J_{i}} X_{i j}=1 \forall i, j
$$

c) Module instance compatibility constraint: This constraint posits that only certain module instance(s) of a particular module would be compatible with certain other module instance(s) of other modules. Zugasti et al. (2000) mapped the module instance compatibilities in terms of an inequality equation, such that the following mathematical relationship is established to model module instance compatibility constraint.

$$
M\left(Z_{i j}, Z_{i j}\right)>0 \quad \forall i \neq i^{\prime} ; j \neq j^{\prime}
$$

Key assumptions made in our devised model are as follows.

1. For a given module, all the module instances can be used interchangeably in a product concept implying that all instances of a particular module instance meet desired functional and consumer related requirements.

2. Supply chain stakeholders belonging to both the internal organization and consumer have complete knowledge in their respective domains for taking rational decisions. To this end, we have considered inputs from experts belonging to a construction equipment manufacturing firm having at least 10 years of experience in pertinent functional areas within the value chain of the firm. Final counts of approximately 15 experts (stakeholders) from individual functional areas are considered.
3. Each module contained within the product has the same functional importance implying that each module has the same weight as far as functionality of the overall product is considered.
4. Final SCRI values for different design concepts follow normal probability distribution and are expressed in terms of derived mean and standard deviation.

A high level abstraction of the problem is depicted through Table 3(a).
<<Insert Table 3 here>>

# 5. An illustrative case example with solution methodology 

To illustrate our devised model, we present the case example of construction power tool. The respective instances for individual modules are enlisted in Table 3(b).

Referring to Table 3(b), there are a number of module instances available for selection for the design concept. These module instances are differentiated amongst themselves in terms of the manufacturing processes and material specifications. For example, the module "drill bit" contains three different module instances. These module instances are differentiated in terms of manufacturing processes. Module instance "M11" is produced through the casting process, while module instances "M12" and "M13" are manufactured through forging and powder metallurgy respectively. Without considering module compatibility constraints, the total number of module instances for our case example would be equal to ( $3 \mathrm{x} 2 \mathrm{x} 3 \mathrm{x} 3 \mathrm{x} 2 \mathrm{x} 1 \mathrm{x} 2 \mathrm{x} 3$ ), i.e., 648 . However, factoring in module compatibility constraints, total feasible combinations would be reduced such that design concept would have to be selected from a lesser number of pools (108 design concepts) The solution methodology for solving the devised problem is illustrated through Figure 3.

The detailed calculations and illustration of entire methodology is shown in subsequent sub sections.

# 5.1 Populate all possible design concepts 

The purpose of this step is to populate all feasible design concepts considering compatibility/incompatibility among module instances of different module instances. The modules compatibility matrix is presented in Table 3(c).

Referring to Table 3(c), (where 0 indicates incompatibility; 1 indicates compatibility; and X indicates non-applicability), it can be inferred that a number of incompatibilities exist amongst the module instances of different modules. For example, module instance "M13" is incompatible with module instances "M51" and "M52". The reason for this kind incompatibility is related to the material properties since a drill bit manufactured using a powder metallurgy process would not be able to match the corresponding material properties of a forged or cast gear. Along similar lines, all the compatibilities/incompatibilities are identified and captured. Employing combinatorics, we obtain a total of 108 different possible combinations of module instances that would form a feasible product. For the sake of brevity, not all 108 feasible design concepts are presented.

### 5.2 Generate the conditional probabilities for enterprise risk network

For determining conditional probabilities, pair wise comparisons are made. 15 experts (also stakeholders) qualified within the enterprise having significant experience in strategic, functional, operational, and technical domains are selected to perform pairwise comparisons thus enabling us to determine conditional probabilities. As illustrated in Table 3, parent node "PLR" has three different root nodes i.e. "RDC", "INC" and "ENR". Definitions of root and parents nodes have been adopted from Daultani et al., (2019). These definitions were developed based on the work of Daultani et al. (2015); Tang (2006); Tang and Tomlin (2008), Tang and Musa (2011), and Wieland and Wallenburg (2012). For instance, Daultani et al., (2019) defined "PLR" as likelihood that the product specifications and forecasts do not withstand various environmental turbulences within the expected resources. The corresponding root nodes i.e "RDC", "INC" and "ENR" associated with parent node "PLR" has been defined by Daultani et al., (2019) in the following manner.

RDC (research and development capability): measure of the extent that evaluates the firm's potential to efficiently design and develop existing/new products in a turbulent technological environment.

INC (information competency): measure of the extent that evaluates the sharing, accuracy, visibility and security of the information shared among various functional divisions and with other supply chain partners

ENR (environmental risk): measure of the extent that evaluates the effect of various external events such as legal, economic, environmental, social, political, natural and cultural factors on the firm's performance.

For the sake of brevity, we don't include other definitions of root and parent nodes. The related definitions can be referred in the work of Daultani et al., (2019).

Adopting the convention presented in Table 2, the following equations (for stakeholder 1) can be populated that would enable us to determine $p(P L R / R D C), p(P L R / I N C)$ and $p(P L R / E N R)$ in different risk state combinations.

$$
\begin{aligned}
& p(P L R=H / R D C=H)_{1}=p\left(C_{1}^{H} / d_{1}^{H}\right)_{1} \\
& p(P L R=H / I N C=H)_{1}=p\left(C_{1}^{H} / d_{2}^{H}\right)_{1} \\
& p(P L R=H / E N R=H)_{1}=p\left(C_{1}^{H} / d_{3}^{H}\right)_{1}
\end{aligned}
$$

Stakeholder 1 fill out the matrix by answering the question "ignoring the influence of other roots nodes on 'PLR', when 'RDC' is in the H state, which state of 'PLR" is more likely to occur and how much more likely?".

The resulting matrix is shown in Table 4(a).
<<Insert Table 4 here>>

Referring to Table 4(a), if 'RDC' is in risk state H , the probability of 'PLR' being at risk state M is half the probability of 'PLR' at risk state H and the probability of 'PLR' being at risk state L is one third of the probability of 'PLR' at risk state H . This comparison is quite reasonable since higher risks in research and developmental capabilities would imply higher planning risks.

The resulting probabilities of "PLR" conditional on different states of "RDC" are listed in Table 4(b).

Employing the above approach, probabilities of different risk states of "PLR" conditional on different risk state of "INC" and "ENR"; the probabilities of different risk states of "SCR" conditional on different risk state of "SMR", "PMR", and "SFR"; the probabilities of different risk states of "OPR" conditional on different risk state of "PRC", "PPC", and "OOD"; the probabilities of different risk states of "LGR" conditional on different risk state of "DSR", "PMR", and "LSR" and "TRC"; the probabilities of different risk states of "MKR" conditional on different risk state of "SMR", "MKT", and "CMD"; the probabilities of different risk states of "SER" conditional on different risk state of "ASR", "CPR", and "PAM" are estimated and listed in Table 5(a).
<<Insert Table 5 here>>

Thereafter, the probabilities of all states of the node 'PLR' conditional on various states of its root nodes i.e. "RDC", "INC" and "ENR" are estimated using the following equations.

At risk state "H", the following equation can be written employing the Bayesian principle.

$$
\begin{aligned}
& p(P L R=H / R D C=H ; I N C=H ; E N R=H)_{1}=p\left(C_{1}^{H} / g_{1}^{H}\right)_{1} \\
& \left\{p\left(C_{1}^{H} / d_{1}^{H}\right)_{1} \times p\left(C_{1}^{H} / d_{2}^{H}\right)_{1} \times p\left(C_{1}^{H} / d_{3}^{H}\right)_{1}\right\} / \\
& \left\{p\left(C_{1}^{H} / d_{1}^{H}\right)_{1} \times p\left(C_{1}^{H} / d_{2}^{H}\right)_{1} \times p\left(C_{1}^{H} / d_{3}^{H}\right)_{1}\right. \\
& +p\left(C_{1}^{H} / d_{1}^{M}\right)_{1} \times p\left(C_{1}^{H} / d_{2}^{M}\right)_{1} \times p\left(C_{1}^{H} / d_{3}^{M}\right)_{1} \\
& \left.+p\left(C_{1}^{H} / d_{1}^{L}\right)_{1} \times p\left(C_{1}^{H} / d_{2}^{L}\right)_{1} \times p\left(C_{1}^{H} / d_{3}^{L}\right)_{1}\right\}=.903
\end{aligned}
$$

Similarly, at risk state "M", the conditional probability can be determined employing the following equation.

$$
\begin{aligned}
& p(P L R=M / R D C=M ; I N C=M ; E N R=M)_{1}=p\left(C_{1}^{M} / g_{1}^{M}\right)_{1} \\
& \left\{p\left(C_{1}^{M} / d_{1}^{M}\right)_{1} \times p\left(C_{1}^{M} / d_{2}^{M}\right)_{1} \times p\left(C_{1}^{M} / d_{3}^{M}\right)_{1}\right\} / \\
& \left\{p\left(C_{1}^{M} / d_{1}^{H}\right)_{1} \times p\left(C_{1}^{M} / d_{2}^{H}\right)_{1} \times p\left(C_{1}^{M} / d_{3}^{H}\right)_{1}\right. \\
& +p\left(C_{1}^{M} / d_{1}^{M}\right)_{1} \times p\left(C_{1}^{M} / d_{2}^{M}\right)_{1} \times p\left(C_{1}^{M} / d_{3}^{M}\right)_{1} \\
& \left.+p\left(C_{1}^{M} / d_{1}^{L}\right)_{1} \times p\left(C_{1}^{M} / d_{2}^{L}\right)_{1} \times p\left(C_{1}^{M} / d_{3}^{L}\right)_{1}\right\}=.297
\end{aligned}
$$

Finally, at risk state "L", the conditional probability can be determined employing the following equation.

$$
\begin{aligned}
& p(P L R=L / R D C=L ; I N C=L ; E N R=L)=p\left(C_{1}^{L} / g_{1}^{L}\right)_{1} \\
& \left\{p\left(C_{1}^{L} / d_{1}^{L}\right) \times P\left(C_{1}^{L} / d_{2}^{L}\right) \times p\left(C_{1}^{L} / d_{3}^{L}\right)\right\} / \\
& \left\{p\left(C_{1}^{L} / d_{1}^{H}\right) \times P\left(C_{1}^{L} / d_{2}^{H}\right) \times p\left(C_{1}^{L} / d_{3}^{H}\right)\right. \\
& +p\left(C_{1}^{L} / d_{1}^{M}\right) \times p\left(C_{1}^{L} / d_{2}^{M}\right) \times p\left(C_{1}^{L} / d_{3}^{M}\right) \\
& \left.+p\left(C_{1}^{L} / d_{1}^{L}\right) \times p\left(C_{1}^{L} / d_{2}^{L}\right) \times p\left(C_{1}^{L} / d_{3}^{L}\right)\right\}=.926
\end{aligned}
$$

Similar to the above approach represented by equations 21,22 , and 23 , the probabilities of other parent nodes conditional on other root nodes at the risk states $\mathrm{H}, \mathrm{M}$, and L can be estimated. These conditional probabilities are $p\left(C_{2}^{H} / g_{2}^{H}\right)_{1}, p\left(C_{2}^{M} / g_{2}^{M}\right)_{1}, p\left(C_{2}^{L} / g_{2}^{L}\right)_{1}, p\left(C_{3}^{H} / g_{3}^{H}\right)_{1}, p\left(C_{3}^{M} / g_{3}^{M}\right)_{1}$, $p\left(C_{3}^{L} / g_{3}^{L}\right)_{1}, p\left(C_{4}^{H} / g_{4}^{H}\right)_{1}, p\left(C_{4}^{M} / g_{4}^{M}\right)_{1}, p\left(C_{4}^{L} / g_{4}^{L}\right)_{1}, p\left(C_{5}^{H} / g_{5}^{H}\right)_{1}, p\left(C_{5}^{M} / g_{5}^{M}\right)_{1}, p\left(C_{5}^{L} / g_{5}^{L}\right)_{1}$, $p\left(C_{6}^{H} / g_{6}^{H}\right)_{1}, p\left(C_{6}^{M} / g_{6}^{M}\right)_{1}$, and $p\left(C_{6}^{L} / g_{6}^{L}\right)_{1}$

# 5.3 Estimate the prior probabilities for respective module instances 

For a given module and its respective root nodes, all the module instances are compared amongst themselves by answering the question "Considering the similarity of existing modules at the enterprise which state is more likely to occur and how much more likely". This procedure is repeated for all the 18 root nodes (by stakeholder 1) using the method suggested in Section 2.2. These prior probability values are listed in Table 5(b). It is to be noted that for the sake of brevity, these probability values for only select module instances are populated.

For a particular module instance, evaluations at different risk states are not independent, hence the following formulae is utilized for determining the net prior probability at the three risk states of H, M, and L. For module instances, i.e., M11, the value of $p\left(Z_{t, l_{i}}^{H}\right)_{v}$ (by stakeholder 1) for the $1^{\text {st }}$ paired combinations of root nodes i.e. root nodes "RDC", "INC" and "ENR" can be estimated employing the following formula.

$$
p\left(Z_{1,1}^{H}\right)_{1}=\left[1-\left\{1-p\left(d_{1 / 1}^{H}\right)_{1}\right\} \times\left\{1-p\left(d_{2 / 1}^{H}\right)_{1}\right\} \times\left\{1-p\left(d_{3 / 1}^{H}\right)_{1}\right\}\right]=0.722
$$

Similarly, at the risk states M and L , for module instance 1 and for root nodes "RDC", "INC", and "ENR" the values of $p\left(Z_{t, j_{i}}^{M}\right)_{v}$ and $p\left(Z_{t, j_{i}}^{L}\right)_{v}$ (by stakeholder 1) can be determined employing the following equations.

$$
\begin{aligned}
& p\left(Z_{1,1}^{M}\right)_{1}=\left[1-\left\{1-p\left(d_{1}^{M}{ }_{/ 1}\right)_{1}\right\} \times\left\{1-p\left(d_{2}^{M}{ }_{/ 1}\right)_{1}\right\} \times\left\{1-p\left(d_{3}^{M}{ }_{/ 1}\right)_{1}\right\}\right]=0.128 \\
& p\left(Z_{1,1}^{M}\right)_{1}=\left[1-\left\{1-p\left(d_{1}^{M}{ }_{/ 1}\right)_{1}\right\} \times\left\{1-p\left(d_{2}^{M}{ }_{/ 1}\right)_{1}\right\} \times\left\{1-p\left(d_{3}^{M}{ }_{/ 1}\right)_{1}\right\}\right]=0.15
\end{aligned}
$$

Similar to the above approach, the values of $p\left(Z_{t, j_{i}}^{H}\right)_{v}, p\left(Z_{t, j_{i}}^{M}\right)_{v}$ and $p\left(Z_{t, j_{i}}^{L}\right)_{v}$ for all the root node combinations for the entire module instance can be determined.

The $\operatorname{SCRI}\left(r / j_{i}\right)$ for a parent node " $r$ " and module instance " $j_{i}$ " can thus be estimated employing the following equation at the three risk states. We illustrate this for module instance "M11", parent node "PLR" corresponding to inputs from stakeholder " 1 ". As the evaluations of $p\left(C_{1}^{H} / g_{1}^{H}\right)_{1}$ and $p\left(Z_{1,1}^{H}\right)$ are independent of each other, hence the following equations at the three risk states can be written.

$$
\begin{aligned}
& \operatorname{SCRI}(1 / 1)_{1} \text { at } \mathrm{H}=p\left(C_{1}^{H} / g_{1}^{H}\right)_{1} \times p\left(Z_{1,1}^{H}\right)=0.652 \\
& \operatorname{SCRI}(1 / 1)_{1} \text { at } \mathrm{M}=p\left(C_{1}^{M} / g_{1}^{M}\right)_{1} \times p\left(Z_{1,1}^{M}\right)=0.038 \\
& \operatorname{SCRI}(1 / 1)_{1} \text { at } \mathrm{L}=p\left(C_{1}^{L} / g_{1}^{L}\right)_{1} \times p\left(Z_{1,1}^{L}\right)=0.138
\end{aligned}
$$

# 5.4 Determine the configurations of product concept at each the risk states $H, M$, and $L$ with minimum SCRI 

Employing the approach illustrated in section 3.2.2 and utilizing equations 10, 11, and 12, the SCRI at high, medium, and low risk index is determined for stakeholder 1 and thereafter for the remaining stakeholders. Figure 4 exhibits values of SCRI for the top five design concepts at each risk state i.e. $H, M$, and $L$ (least five obtained values of SCRI). It is to be noted that the SCRI value obtained here is the grand average (mean) of final SCRI values considering the assessments of all 15 experts implying that all the experts' assessment carries the same level of importance.
<<Insert Figure 4 here>>

# 6. Results, validation and implications 

### 6.1 Results and discussions

We have considered all parent risks (that are representative of supply chain risks associated with the enterprise) to have equal weightage without one factor dominating the other. Further inputs to our developed framework are provided by stakeholders having functional expertise who have significant cross functional exposure within the organization as well as are expert in their own domain. The objective, thus, is to exploit both depth and breadth of functional knowledge (Long, 2018). The distribution function (taking into consideration all 15 stakeholders) of the minimal SCRI value that yields a particular design concept in terms of combination of module instances of respective modules are derived for the three risk states i.e. H, M, and L. These functions at H, M, and L are normally distributed to be $N\left(.387, .023^{2}\right), N\left(.257, .019^{2}\right)$, and $N(.201$, . $022^{2}$ ) respectively. Further, the configuration of design concept with lowest mean value of $S C R I$ at the three risk states i.e. H, M, and L are listed in Table 5(c).

Referring to Table 5(b), it can be observed that at risk state H for module 1, the module instance M12 is preferred over module instance M11. However, at the risk states M and L, the module instance M11 scores over M12, i.e., the SCRI value of M11 is less than that of M12.

At high risk state H, a crucial reason for the lower SCRI value of M12 compared to that of M11 is explained by the disparate manufacturing processes of the two module instances. As the associated production process of M12, i.e., forging yields relatively precise fit and form tolerances, the functional performance of the design concept containing the module instance M12 would be significantly higher than that of the module instance M11. Since, at higher risk state H, marketing requirements would much be more demanding than at lower risk states M and L , the chances of M12 ensuring higher consumer satisfaction would be quite plausible. Further, since at the highrisk state H , time to market consideration and aftersales turnaround time would be significantly compressed compared to those at lower risk states M and L , it would be quite reasonable to infer that M12 is associated with lower risk compared to M11 (the cycle time of the forging process is significantly lower compared with that of the casting process). However, at lower risk states M and L, M11 yields lesser SCRI value compared to M12 due to the fact that crucial attributes market and aftersales related attributes such as requirements related to functional performance, time to market consideration and aftersales turnaround are significantly less stringent than at higher risk state H .

We further propose two different scenarios wherein the design concepts will be solely evaluated from: a) only the consumer standpoint and, b) the enterprise standpoint.

Evaluation from the consumers' standpoint pertains to assessment of design concepts from the viewpoint of two consumer related parent nodes, i.e., SER and MKR; while evaluation from the enterprise standpoint is related to assessment of design concepts from viewpoints of four enterprise related parent nodes i.e. PLR, OPR, LSR and SCR. Employing the methodology for determining the SCRI value in previous sections, distribution of SCRI values (for least risk averse design concept) at three risk state, i.e., H, M, and L corresponding to the two scenarios i.e. from a consumer standpoint and from an enterprise standpoint is calculated and illustrated in Figure 5(a).
$<<$ Insert Figure 5 here $>>$

# 6.2 Validation with respect to an existing methodology 

We compare our evolved methodology with that of Chin et al. (2009) that measured the cumulative risk posed by a particular design concept in terms of associated probabilistic utility. Employing a case example of a multinational flashlight manufacturer, this research demonstrated that, in the context of an appropriate Bayesian project structure (involving aspects related to product development), utility score (between 0 to 1 ; with 0 corresponding to lowest utility and 1 corresponding to highest utility) associated with a particular design concept is representative of the degree of overall risk. The higher the overall risk value, the lower would be the utility and viceversa. Employing the detailed methodology of Chin et al. (2009), we determine the utility values of: a) each of the top five design concepts; and b) the remaining 103 design concepts. These utility values $\{$ considering utility $(\mathrm{H})=0$; utility $(\mathrm{M})=0.5$; utility $(\mathrm{L})=1\}$ are then compared with the SCRI values using our evolved method corresponding to each of the three risk states and are illustrated in Figure 5(b), 5(c) and 5(d).

Referring to Figure 5(b), 5(c), and 5(d), it can be inferred that SCRI values and utility values (for the top five design concepts under the three risk states) are related to each other in terms of a negative correlation substantiating that the higher the SCRI value, the lower the utility values and vice-versa. Further, we also contrast the mean SCRI values with mean utility values for the other 103 design concepts and plot in Figure 5(e). The comparison of the mean values of both SCRI and utility also suggest similar negative correlation between SCRI and utility. This indicates the consistency and reliability of our evolved methodology in that our evolved measure i.e. SCRI

holds a direct negative correlation with regard to the utility measure evolved by Chin et al. (2009). Based on a linear regression model, wherein SCRI and utility are modelled as dependent and independent variable respectively, the following resulting equation is obtained.
$\operatorname{SCRI}=0.3632-0.307 \times($ Utility $)$
The $\mathrm{R}^{2}$ and adjusted $\mathrm{R}^{2}$ values were obtained as 0.9342 and 0.9335 respectively implying strong goodness of fit. Further, at confidence levels of $99 \%, 95 \%$ and $90 \%$, the $p$ value was found to be less than the corresponding $\alpha$ values implying statistically significant relationship between SCRI and utility

A major contrasting aspects of our work as opposed to that of Nepal et al. (2012) is the consideration of module instance compatibility constraint that is reflective of the congruence/incongruence of the module instances of respective product modules. In context of the fact that that most of the product systems often have modular architecture as opposed to having an integrated architecture, our method is better positioned to deal with the supply chain intricacies than that of Xu et al. (2015) and Chin et al. (2009); as these studies considered purely an integrated product architecture.

# 6.3 Managerial implications 

The analytical model evolved in this research and illustrated considering an example of construction power tool can be deployed to deal with many typical issues often encountered in industries such as automotive and construction industry. The framework devised for illustration of our methodology is analogous to many elements within automobile and construction industry such as project planning and selection, project risk assessment, site selection, vendor selection, tendering and so forth.

Our devised method can be of value to OEMs in that it would allow vetting of high risk design concepts at the early stages of product development itself. The advantage therefore would be that OEMs would not have to painstakingly develop multiple design concepts in physical forms and then validate them with respect to individual supply chain risk elements. This in turn would lead to improved time to market for the concerned organization's product line. Further, by proactively discriminating between risk prone design concepts and risk neutral/risk averse design concepts, organizational resources (manpower, money, technical capabilities) can be deployed effectively as several cost elements can be avoided. Our devised method also explicitly allows to

uncover high risk design concepts from the perspective of individual dimensions of supply chain risks. By doing so, the product development teams can then converge on to the specific source(s) of accompanying design/processes/technical knowhow that contributes towards high risk associated with a particular risk type. The environment of the NPD is often dynamic and uncertain in that new evidences will come out from time to time that in turn would impact risks associated with design concepts. Our devised method then can be deployed to update the pair-wise comparisons that in turn would influence the design concept selection decisions.

Within construction industry, project planning and selection is often one of the problematic areas in that owing to multitude of factors (such as those related to budgetary uncertainties, varying skill levels of contactors, varying level of expectations from stakeholders, differing technological levels of vendors), it becomes paramount that the project schedule considers these factors in terms of respective level of uncertainties. The uncertainties thus considered would enable construction managers to chalk out proactively a realistic, grounded, and implementable project schedule before even the project commences. Another benefit of such approach would be that deviations from such project schedule can be minimized.
Adoption of evolved analytical framework based on qualitative inputs from stakeholders belonging to construction value-chain would also lead to better assessment and prioritization of strategy, project, systems and vendor related factors. This is of particular importance due to subjective nature of influencing dimensions within construction industry viz. uniqueness of construction projects, project size, organizational topography, public-private partnerships etc. The evolved analytical framework if deployed effectively would also add value to stakeholders involved viz. contractors, vendors, architects, and so forth in proactive identification of sources of risks during key decision making stages viz. tendering, procurement, and project execution. From a lifecycle of building construction point of view, wherein design, construction, maintenance, renovation, recycle, reuse, and deconstruction assume primacy, our evolved framework can aid stakeholders to analyze risk factors related to labor, capital, technology and so forth for better mitigation of uncertainties involved.

SCRI proposed in our research is primarily intended to be used at early stages of NPD to weed out risky design concepts in such a way that risk averse design concepts can be considered further for subsequent NPD stages such as detailed design and prototyping. The supply chain risk network considered at early stages of NPD can also include certain other risk factors that may hold

certain interrelation with other nodes. For instance, there might be certain interdependent relationship between risk nodes related to sourcing and logistics. However, in this case we would have to consider the aggregate conditional probability wherein such interactions are also present. In such case however, the overall aggregate conditional probability would be fairly less sensitive to the interaction of risk factors as opposed to the single conditional probability representing a particular risk node. The reason for this would be that when we ascertain the aggregate conditional probability considering interdependencies, the corresponding probability element would be a multiplication of prior probabilities of the such interdependent risk nodes and also the probabilistic strength (based on low, medium, high level of interdependency) of such interdependency. This in turn will results in fairly low probability value compared to either of the prior probabilities or their probabilistic strength.

# 7. Concluding remarks, limitations and pathways for future research 

### 7.1 Conclusions and limitations

The focus of our research is to integrate the decision-making pertaining to design concept selection at early stages of new product development from the standpoint of key supply chain risks such that the selected design concept represents the least supply chain risk. The supply chain risk network established is expressed in terms of risk parameters characterized by both parent and root nodes. Thereafter, employing the real-life example of construction power tool product line, we demonstrate the devised methodology. Employing the module compatibility matrix, different design concepts composed of disparate module instances are generated. Thereafter, employing a Bayesian approach, conditional probabilities of parent nodes conditional on respective root nodes for three considered risk states i.e. high (H), medium(M), and low (L) are determined. Further, prior probabilities for respective module instances are generated. The conditional probabilities associated with supply chain risk network and prior probabilities associated with module instances then serve as a key input for determination of supply chain risk index at states H, M, and L. We further analyze the design concept selection problem from a consumer and functional risk standpoint. Some key novelties associated with our research is as follows.

a) Development of an analytical supply chain risk evaluation methodology for a complex product consisting of different modules in contrast to products having integrated architecture.
b) Our research aims to aid manufacturers having a product life cycle-based mindset to include the supply chain considerations during the early stages of new product development thus enabling them to eliminate many of the physical and time-consuming supply chain related validation activities.
c) The devised framework incorporates various technical and commercial risks emanating from involvement of multiple supply chain related considerations; thus, seeking to address design concept selection problems from a supply chain centric standpoint using expert inputs from multiple stakeholders.

There are certain limitations in our research. First, we consider only three risk states, namely high, medium and low, for each of the parent and root nodes. However, in a real industry setting there can be varying numbers of risk states associated with respective parent nodes and root nodes. Future work can capture these variations in risk states and refine the devised methodology to make it more realistic. Second, our research at this point is suitable only for modular products as opposed to scalar products. Third, all the stakeholders supplying their expert opinions in relation to the design concepts belonged to only one organization. This automatically implies that all the stakeholders had a rather homogenous mindset considering both technical and other softer organizational factors. From a technical standpoint, all stakeholders had exposure to a relatively homogenous mix of design, manufacturing and assembly related technologies, SOP (standard operating procedures), supply chain philosophies etc. On the organizational side, all stakeholders had a similar understanding about the organization's vision, the organization's stand in the industry, growth pathways and so forth. If the stakeholder would have belonged to diverse organizations (within the construction equipment manufacturing industry), it is quite possible that the concept selection decisions might have been different in that varying exposures to technological and organizational aspects would have altered some concept selection decisions.

# 7.2 Pathway for future research

The model devised in the current study can also be made more robust by taking into account externalities such as uncertainties associated with currency and regulations. In particular, it would be in the interest of OEMs that rely heavily on sourcing of critical parts/sub-assemblies/systems from international vendors to consider risks emanating from currency fluctuations including transaction, economic and translation exposures. For OEMs particularly operating in fast-changing industries such as those in telecommunications would be well served to include evolving technological and environmental regulations in their decision-making process during the design, development and sourcing stages. This is of particular importance in that designing effective regulatory policies around changing technologies is difficult, as it requires understanding as to how regulatory changes may alter market conditions that often renders prevailing regulatory policies obsolete or even counterproductive.

The SCRI framework evolved in our research aids decision-makers to zero down to the risk averse design concept(s). The key assumption involved however here is that experts(stakeholders) involved are able to carry out a reasonably accurate analysis with respect to various supply chain related risks considered in our research. However, when such approach is utilized considering the philosophy of MVP (minimum viable product), the process of ascertaining overall supply chain risks would have to be much more adaptive and perhaps iterative involving feedbacks. This implies that early risk analysis would be from more of an early adopter's perspective. Based on the feedbacks about MVP, the products would have to be fine-tuned to address inadequacies such that improved version of MVP can be evolved. In particular, Bayesian learning framework here would be of immense important in that based on the additional information and evidences wrt. pertinent risks, the associated probabilities (both conditional and prior) can be fine-tuned iteratively.
