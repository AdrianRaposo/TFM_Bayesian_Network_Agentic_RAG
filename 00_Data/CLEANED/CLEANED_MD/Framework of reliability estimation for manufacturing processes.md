# Framework of reliability estimation for manufacturing processes 

T. Karaulova*, M. Kostina**, J. Sahno***<br>*Tallinn University of Technology, Ehitajate tee 5, 19086 Tallinn, Estonia, E-mail: tatjana.karaulova@ttu.ee<br>**Tallinn University of Technology, Ehitajate tee 5, 19086 Tallinn, Estonia, E-mail: marina.kostina@Autoliv.com<br>***Tallinn University of Technology, Ehitajate tee 5, 19086 Tallinn, Estonia, E-mail: jevgeni.sahno@gmail.com

crossref http://dx.doi.org/10.5755/j01.mech.18.6.3168

## 1. Introduction

In today's competitive environment companies are increasingly forced to respond to diverse market demands with the alignment of their organizational structure and competitive strategies. The companies improve their capability, long term flexibility and responsiveness of processes. Up to the present, a production system and its internal structures have been in the centre of the entrepreneurial activities and plans, which foster adaptation to actual market needs.

The objective of any factory is to increase the overall production reliability. It means maximization of the current resources output by waste reduction equipment and process reliability. The equipment and process reliability jointly create reliable production.

The system reliability assessment and prediction has become an increasingly important aspect of the process operating different stages. It is important to develop efficient reliability assessment techniques for complicated systems with several methods and different failure mechanisms, in order to ensure adequate performance under extreme and uncertain demand [1]. The reliability requirement for a production process ensures the sustainability of the whole enterprise.

The goal of the current research is to develop the reliability assessment methods with an extension of the existing ones and pooling them to a common framework. The system must identify the most unreliable parts of a production process and suggest the most efficient ways for the reliability improvement. Significant cost-saving opportunities for industrial enterprises can be achieved through the reliability improvement of the facilities for their practical realisation. When the process failure criteria are established, the reliability of manufacturing processes can be obtained from daily production data.

## 2. Reliability of a production system

What is the production system? The production system reflects the whole enterprise including all required functions, activities, processes, and resources to produce marketable performances [2].

The term "process" generally describes a delibe-rately-defined sequence of coherent actions in time and space. Objects are processed materials and information. Processes serve three managerial tasks of the production system [3]:

1. Problem solving task: taking running from a concept through a detailed design, engineering of products and dedicated manufacturing systems up to production launch.
2. Information management task: a detailed scheduling running up from an incoming customer order to a delivery.
3. Physical transformation task: the processing started from raw materials up to a finished product delivery to the customer.

Process management contains a body of knowledge for the process improvement. By enhancing efficiency and effectiveness, the process management offers the potential to improve customer satisfaction, followed by increased profits, fast growth, and a sustainable business. Most organizations are motivated to manage their process through several dimensions. In order to increase the profitability, organisations reduce the process cost, increase throughput and improve the quality of products at the same time.

A process management involves five phases (Fig. 1):

- process mapping;
- process diagnosis;
- process design;
- process implementation;
- process maintenance.
![img-0.jpeg](img-0.jpeg)

Fig. 1 Main parameters of a production system
Process reliability is the capacity of equipment or processes to operate without failure. The business issues of reliability are prevention and control of failures to reduce costs for improving customer satisfaction. The process reliability is a method for identifying the problems, which have significant cost reduction opportunities for improvements.

When the complexity of systems increases, their reliability suffers from deterioration. At the same time, more severe requirements are set to the system reliability. A non-sufficient reliability of a system results in:

- increased operating costs of machines;
- increased breakdown time of machines;
- unacceptable rate of malfunctions to occur.


## 3. Reliability analysis

Realistically, it is impossible to avoid all feasible

failures of a system or a product on the design stage, so one of the goals of reliability engineering is to recognize the most expected failures and then to identify appropriate actions to mitigate the effects of those failures [4].

Qualitative and quantitative methods were used for the system safety analysis. They are all interrelated and help to understand the logical structure of the failure modes of a system. The proposed reliability estimation framework includes three main parts (Fig. 2):

- reliability analysis module - the main part;
- design-level part for process analysis;
- analytical part.

All those parts will be considered in sections 4-6.
Every part is considered on the following levels:

- standard methods for reliability assessment;
- additional activities for reliability assessment;
- extended reliability analysis.

The standard methods used in this framework are based on an international standard proposed in Electronic Reliability Design Handbook (MIL-HDBK-338B) [5]:

- fault mode and effects analysis (FMEA);
- fault tree analysis (FTA);
- mathematical reliability prediction (RP).
![img-1.jpeg](img-1.jpeg)

Fig. 2 The framework of a manufacturing processes reliability assessment

The reliability analysis module enables: to calculate the max/min boundaries of an error probability for a selected production route; to define the most critical faults that influence the production route reliability; to select the most efficient corrective actions for the production route reliability improvement.

## 4. Reliability analysis module

This part is the core of all this research. In the centre of the framework is - FMEA, other methods are based on the data from this analysis. Therefore the analysis must be implemented as precisely as possible. An assessment of expert opinions is used for the evaluation of the more significant parameters of FMEA. Especially it's important for such a parameter as fault severity.

The FMEA is a reliability procedure which documents all possible failures in a system design within specified ground rules. It determines, by the failure mode analysis, the effect of each failure on the system operation and identifies single failure points, which are critical to the mission success or crew safety [6].

In general the FMEA is a systemized group of activities designed to:

- recognize and evaluate the potential failure of a product/process and its effects;
- identify actions, which could eliminate or reduce the chance of a potential failure occurring;
- document process.

The purpose of the FMEA [7] is to take actions to eliminate or reduce failures, starting with the highestpriority ones. It may be used to evaluate risk management priorities for mitigating known threat-vulnerabilities. In the FMEA failures are prioritized according to three dimensions:

- how serious their consequences are;
- how frequently they occur;
- how easily they can be detected.

Used properly - the FMEA methodology allows to identify and document the potential system failures and to predict the consequences resulted. It would enable to determine the actions that would reduce severity and occurrence, but increase the detection of the potential failures. The composite risk score for each unit operational step is the product that combines three individual component ratings: Severity ( $S$ ), Occurrence ( $O$ ) and Detection ( $D$ ). All three parameters are estimated on scale of " 1 " to " 10 ". This composite risk is called a risk priority number ( $R P N$ ). This number is then used to rank the order of various concerns and failure modes associated with a given design, as previously identified in the FMEA.

$$
R P N=(S) x(O) x(D)
$$

The $R P N$ is a measure of a design risk. The $R P N$ is also used to rank the order of the processes' concerns (e.g., in Pareto fashion). The $R P N$ will be between " 1 " and " 1000 ". For higher $R P N$ a team must undertake efforts to reduce this calculated risk through the corrective actions.

Advantages:

- identifies connections between reasons and effects;
- takes into account the failure severity;
- demonstrates previous unknown event outcomes;
- it is a systematized analysis;
- provides focus for an improved testing and development;
- minimizes late changes and the associated cost. Disadvantages:
- the number of data can be quite big;
- the analysis can become rather complicated;
- the environment and maintenance conditions cannot be examined.

In our research the outcome of the FMEA is a list of recommendations to reduce the overall risk to an acceptable level that can be used as a source for designing of a control strategy. The FMEA data may also be used in other types of a reliability analysis (Fig. 2).

Assessments of expert opinions are used for more precise estimation of the FMEA parameters. This approach is needed when the expert opinions do not match.

The FMEA method implementation may be characterised as activities of an organised group. The initiation of the FMEA requires assembling of a team, usually comprised of a facilitator, a team leader, and functional experts from development, manufacturing, quality, and others specialists as appropriate. The assembled team should first describe the process of unit operations in general, then section each unit operation into its component parts and

estimate every part by its main parameters. During the estimation of the parameters, especially the faults severity, experts' opinions often diverge. In the current work we suggest to use the consistency assessment of the expert opinions for increasing the quality of the estimation of the FMEA parameters.

Proposed by Maurice G. Kendall and Bernard Babington Smith, Kendall's coefficient of concordance $W$ is a measure of the agreement among several $m$ quantitative or semi-quantitative variables that are assessing a set of $n$ objects of interest [8]. The Kendall coefficient of concordance can be used to assess the degree to which a group of variables provide a common ranking for a set of objects. It should only be used to obtain a statement about variables that are all meant to measure the same general property of the objects [9].

The consistency of the opinions of experts can assess the magnitude of the coefficient of concordance. The coefficient of concordance varies in the range of $0<W<1$ :

0 - the total incoherence, 1 - complete unanimity.
If $W \geq 0.7-0.8$ opinions are consistent,
If $W<0.2-0.3$ opinions are not consistent,
If $W=0.3-0.7$ average consistency.

$$
W=\frac{12 S}{n^{2}\left(m^{3}-m\right)}
$$

where $n$ is a number of experts; $m$ is a number of objects of expertise; $S$ is a sum of squared deviations of all the examination objects' rank.
$S$ may be defined as

$$
S=\sum_{i=1}^{n}\left(\sum_{j=1}^{m} x_{i j}-\frac{1}{2} m(n+1)\right)^{2}
$$

where $x_{i j}$ is the rank assigned to the $i$-th object $j$-th expert.
The classifier of faults is needed for a fault ordering in machinery enterprises. It must help engineers, by the codes of faults, to define quickly the causes of faults. These codes must be included in the FMEA. On the base of this classifier it is possible, quite easily, to build the Bayesian belief network (BBN) for a process, because the structure of BBN must be the same as the one of a classifier with the faults revealed by the FMEA of the process.

Reliability engineering is dealing with analysis of the causes of the faults in the factories. For this reason was used as a base DOE-NE-STD-1004-92 standard [10]. The assessment phase includes analyzing the data to identify the causal factors, summarizing the findings, and categorizing the findings by the cause categories. The major cause categories are:

- equipment/material problem;
- procedure problem;
- personnel error;
- design problem;
- training deficiency;
- management problem;
- external phenomena.

We have adapted the classifier from this document for machinery enterprises (Fig. 3).

Faults classification
![img-2.jpeg](img-2.jpeg)
2. Procedure problem (technology)
![img-3.jpeg](img-3.jpeg)
3. Personnel error
![img-4.jpeg](img-4.jpeg)
4. Design problem
![img-5.jpeg](img-5.jpeg)
5. Training deficiency
![img-6.jpeg](img-6.jpeg)
6. Management problem
![img-7.jpeg](img-7.jpeg)
7. Supplier/subcontractor problem
![img-8.jpeg](img-8.jpeg)

Fig. 4 The header of FMEA table

Pareto Analysis is a formal technique for finding the changes that will give the biggest benefits. This principle can be applied to a quality improvement to the extent, that a great majority of problems ( $80 \%$ ) are produced by a few key causes ( $20 \%$ ). In order to focus on significant problems, it is necessary to rank the importance in a descending order of occurrence. This is typically done using the Pareto Chart. Pareto analysis is simple to use [7]:

- listing all relevant problems and available options;
- grouping options that are solving the same larger problem;
- applying an appropriate score to each group;
- working on the group with the highest score.
![img-9.jpeg](img-9.jpeg)

Fig. 5 Pareto chart
Priorities on the failure modes can be set according to the FMEA risk priority number ( $R P N$ ). A concentrated effort can be placed on the higher $R P N$ items. The Pareto analysis will be taken as the base for elaboration of more effective corrective actions and the manufacturing process improvement. For this aim in our research we use the BBN.

BBN is a graphic probabilistic model through which one can acquire, capitalize on and exploit knowledge. It consists of a set of interconnected nodes, where each node represents a variable in the dependency model and the connecting arcs represent the causal relationships between these variables [11, 12].

Why did we decide to use the BBN in our research? It is the most suitable way, because the structure of BBN is the same as that of a faults' classifier. Reliability engineers must, only, by using the existing FMEA, cause codes, create the same structure of BBN and include in an every node the probability of particular cause errors. The Bayesian networks are natural successors of statistical approaches to Artificial Intelligence and Data Mining. Particularly suited to taking uncertainty into consideration, they can be easily described manually by experts in the field.
![img-10.jpeg](img-10.jpeg)

Fig. 6 Synthesis of information by Bayes' theorem [13]
A key feature of Bayesian statistics [13] is the synthesis of two separate sources of information - see

Fig. 1 for a schematic representation of this process. The result of combining the prior information and data in this way is the posterior.

A Bayesian network is a graphical model that encodes probabilistic relationships among variables of interest. When used in conjunction with statistical techniques, the graphical model has several advantages for data analysis, because [14]:

- the model encodes dependencies among all variables, it readily handles situations where some data entries are missing;
- the Bayesian network can be used to learn causal relationships, and hence to gain understanding about a problem domain and to predict the consequences of intervention;
- the model has both, causal and probabilistic semantics, it is an ideal representation for combining prior knowledge (which often comes in a causal form) and data;
- the Bayesian statistical methods, in conjunction with the Bayesian networks, offer an efficient and principled approach for avoiding the over-fitting of data.

In this research the BBN is used to analyze the effect that the improvement of different fault groups will cause.

In BBN, the decision-maker is concerned with determining the probability that a hypothesis $(H)$ is true, from evidence $(E)$ linking the hypothesis to other observed states of the world [15]. The approach makes use of the Bayes' rule to combine various sources of evidence. The Bayes' rule states that the posterior probability of the hypothesis $H$, given that evidence $E$ is present or $P(H \mid E)$

$$
P(H \mid E)=\frac{|P(E \mid H) P(H)}{P(E)}
$$

where $P(H)$ is the probability of the hypothesis being true prior to obtaining the evidence $E$ and $P(H \mid E)$ is the likelihood of obtaining the evidence $E$, given that the hypothesis $H$ is true.

When the evidence consists of multiple sources denoted as $1,2, n, E, E, \ldots, E$, each of which is conditionally independent, the Bayes' rule can be expanded into the expression

$$
P\left(H \mid \bigcap_{j} E_{j}\right)=\frac{\prod_{j=1}^{n} P\left(E_{j} \mid H\right) P(H)}{\prod_{j=1}^{n} P\left(E_{j}\right)}
$$

## 5. Design-level part for process analysis

Process modelling and simulation are used for a process visualisation and execution of a dynamic analysis of a system. The purpose of any model is to increase an understanding and a reasoned decision making from a model. It helps to support and improve the process.

Enterprises are competing in the environment, which requires the ability to rapidly reconfigure an enterprise and its processes. This ability requires modelling

methods to support an analysis and design in multiple aspects of a process performance and structure.

The purpose of modelling and simulations:

- analysis and understanding of the observed phenomena;
- testing of hypotheses and theories;
- prediction of the system's behaviour under various conditions and scenarios.

For the analysis of manufacturing processes more suitable are structural modelling methods based on the IDEF standard. The IDEF0 modelling method could test and evaluate each product and process alternative [16].

There are several common measures of performance, obtained from a simulation study of a manufacturing system, including [17]:

- throughput;
- time in system for parts (cycle time);
- times parts spend in queues;
- times parts spend in transport;
- sizes of in-process inventories (work-in-process or queue sizes);
- utilization of equipment and personnel (i.e., proportion of time busy).
![img-11.jpeg](img-11.jpeg)

Fig. 7 Common view of design level analysis
For a more complete analysis of a process a structural and dynamic analysis are used for revealing the bottlenecks of the process, as well as FTA and RBD, which give the reliability of the system on the whole. The FTA, as well RBD, may be built on the base of a structural model of the process.

When establishing a reliability model of technical system, FTA and RBD are two well proven and frequently used techniques. Both are Boolean models, represent exactly the same things, and may be converted from one to another [5]. Actually RBD is often mainly seen as method of representation than as an analysis method.

Roughly speaking RBD approach is often chosen when the system structure is fairly simple and the number of components is limited. However FTA constitutes a top down method, helping the analyst to develop the reliability model step by step from the unwanted "top" event. So if the system structure is very complex one might find it advantageous to use FTA to model it.

If an enterprise is interested in building of FTA so information about probabilities of failures can be taken from FMEA [18, 19]. The main advantage of FTA above FMEA is combination of failures. By taking into account this plus, FTA avoids the obvious shortcomings of FMEA and additional information about failures can be obtained therefore the decision about improvements can be corrected.

## 6. Analytical part

Mathematical Reliability Prediction (RP) calculates the reliability of the system from component data.

The failure rate of the system $\lambda_{s}$ is calculated by summing up the failure rates of each component $\lambda_{i}$ (based on probability theory) [5]

$$
R_{s}(t)=\prod_{i=1}^{N} R_{i}
$$

where $R_{s}(t)$ is probability that the system will not fail before time $t . R_{i}(t)$ is probability that the $i$ th element of the system will not fail before time $t$.

The failure rate for every system element under reference conditions is calculated as follows

$$
R_{i}(t)=e^{-\lambda t}=\exp (-\lambda t)
$$

The failure rate $\lambda$ is a measure of how frequently they arise.

$$
R_{s}(t)=\prod_{i=1}^{N} \exp \left(-\lambda_{i} t\right)
$$

Mean time between failures (MTBF) can be calculated [5]

$$
M T B F=\frac{1}{\lambda_{s}}=\frac{1}{\sum_{i=1}^{N} \lambda_{i}}
$$

This calculation helps to planning of the system maintenance. The data sources used should be the latest available that are applicable to the product and its specific use conditions. Ideally, as was shown in Fig. 2, the failure rate data should be obtained from the FMEA.

Advantages:

- time and cost claim of an analysis is small;
- evaluation of dates can be effective with computer. Disadvantages:
- do not analyse fault cause and effects;
- do not examine repair and maintenance strategies.


## 7. Using the reliability analysis module for a more reliable and effective route selection

In the research we are going to evaluate the reliability of a production process and the pinpoint potential areas for its improvement. The reliability analysis module, which was described in the previous part, may be used separately for a production process reliability assessment. In this research it is shown (Fig. 8), how it is possible to use mutually with Enterprise Resource Planning (ERP) system for new production route creation.

The operational data of an enterprise is managed by an integrated cross-functional ERP system. The integration is made through a data base shared by all functions and data processing applications in the company. The operational data required for analysis and reporting is replicated to Data Warehouse (DW) [20].

By using the special capacities of the DW it is possible to select a more suitable route (routes) for elabora-

tion of a new production process for the needed part or product. When the appropriate production route is discovered, the process of the route modification for a particular order is started in the Reliability analysis module. This level enables to perform it by combining the FMEA method with the BBN approach. FMEA provides data about all possible failures at work station (WS) and BBN allows to prioritize work with these failures and to estimate improvement of reliability of the production route. At this level analysis starts from receiving the percentage of WS faults from DW where this data is collected. For this purpose the number of products with defects produced by every WS divided by total number of product produced. If suggested percentage of faults is within the level required by customer, work with reliability analysis module is finished. If percentage of faults is too high the causes must be analysed [21]. For this purpose the posterior probability boundary is calculated, based on the assumption that the error took place. The calculation of the max/min boundaries of the error probability for the selected operation of a production route shows the most critical fault types, that influence the production route reliability, and enables a decision maker to select the most efficient corrective actions for the causes with the maximum influence of the production route operation reliability improvement.
![img-12.jpeg](img-12.jpeg)

Fig. 8 Maturity work of a reliability analysis module and the ERP system for a production route selection

After the required level of reliability is achieved the decision maker chooses the most suitable production route, that further is imported to the ERP system and then into production.

The reliability improvement process consists from the following steps:

Step 1 - Definition of failure types. The preparation process is started by definition of possible failure types and adaptation of a classifier under the requirements of a selected enterprise.

Step 2 - FMEA elaboration. This process was started from the analysis of production system operations and particular enterprise requirements.

Step 3 - Analysis of FMEA data and faults probability calculation. It will be used in BBN. The probability of an error for every fault group is calculated on the base of the FMEA by the following equation

$$
P_{P R}=\frac{\sum R P N_{P C}}{\sum R P N_{\text {Total }}} 100 \%
$$

where $P_{R P}$ is probability of production route errors; $\sum R P N_{P C}$ is $R P N$ value for a particular cause of errors; $\sum R P N_{\text {Total }}$ is Total $R P N$ value of a production route.

Step 4 - Building BBN. The Bayesian network is build on the base of an elaborated classifier. To every node of the network it is necessary to include the value of a particular cause error probability. The probabilities on some nodes are affected by the state of the other nodes depending on causalities.

Step 5 - Finding a more effective way to increase the operation reliability by using the BBN analysis.

Step 6 - Including more reliable operations to the production process.

An example of BBN is introduced in Fig. 9. According to Fig. 9 the personnel error is the most probable failure type. The BBN can answer questions like: if a personnel error exists, was it more likely to be caused by an inadequate work environment, inattention to detail, or violation of requirements. Particularly, inattention to details, which is one of the personnel errors, has the highest probability. Therefore, corrective actions are focused on this failure cause, aiming to decrease it as much as possible. Four corrective actions are planned as:

1 - Poka-Yoke, 2 - visual instruction, 3 - improvement route card and 4 - additional training.

In order to make this analysis, the RPN of a corrective action was taken from the FMEA and imported to the Bayesian model. The influence of failure severity was also taken into account. Fig. 9 (the lower part) shows the impact of each of the corrective actions on the personnel error. In Fig. 9 there are presented available corrective actions and their influence on the corresponding failure cause. As shows the analysis, a more effective corrective action for the Personnel errors elimination is Poka-Yoke implementation - probability of success $98 \%$.

The information with probabilities of failures is calculated starting from the bottom levels to the top level. In the current example probability of an error on the top level is $14 \%$. On the basis of this number a decision maker decides whether to implement some corrective actions or not. As usually $14 \%$ probability of error is not satisfied thus it is decided to implement some corrective actions and consequently to improve reliability of the whole process.

When probability of failures in case of using of different corrective actions is calculated, decision maker needs to make a decision about corrective action in a production process. His decision can depend on different aspects: efficiency of corrective action, price, time and complexity of implementation and so on.

This scheme may be implemented plenty of times until the desired result is achieved. Decision makers may benefit from its output to make the most relevant decision in their manufacturing processes. The improvement of production process reliability enables to move towards to more sustainable production process [22].

BBN enables to combine FMEA data (failures probability) with quantitative data and subjective judgments about the process. Hence BBN provides a method of modelling process losses and measuring the effectiveness of recommendations using for process reliability improvement.

![img-13.jpeg](img-13.jpeg)

Fig. 9 BBN for the production route probability of error

## 8. Conclusions

An integrated modelling method based on a system modelling and complemented with a reliability evaluation mechanism has the capability to analyse and design manufacturing systems. The tool developed to analyse a production process enables companies to analyse the process as a whole and its parts and get an efficient prognosis for the production process reorganization.

The methodology offered in current paper allows making the most effective decisions for implementation of corrective actions of manufacturing process. In the frame of this work was done:

- FMEA was expanded by the classifier of production process faults for machinery industry;
- was offered the mechanism of more precise definition of parameters of FMEA such as severity and detection of faults. The parameters can be specified by using of assessment of expert;
- BBN was used for calculating the probabilities for each fault group and their influence on error probability of the whole manufacturing process. It enables to do decision making concerning selection of corrective actions quickly and precise.
- for a more complete analysis of a manufacturing system processes was offered a structural and dynamic analysis in concert with FTA and RBD analysis for revealing the bottlenecks of the process.

The reliability analysis module for machinery manufacturing enterprises was developed in order to increase the reliability of a selected production route.

## Acknowledgements

The research was supported by Estonian Ministry of Education and Research for targeted financing scheme SF0140035s12, grant ETF9460.

## R e z i u m é

Gamybinio proceso patikimumas yra svarbiausias veiksnys lemiantis sistemos darbo stabilumą, produkcijos kokybę ir padedantis mažinti darbo nuostolius. Straipsnyje pasiūlytas metodas, leidžiantis išanalizuoti gamybinị procesą ir numatyti būdus atsiradusiems defektams šalinti.

Siūlomos struktūros pagrindinis elementas (grandis) yra FMEA - plačiausiai gamyklose papiltęs patikimumo analizės būdas. Straipsnyje siūloma išplėsti FMEA analizės būdą taikant defektų klasifikaciją ir ekspertinị kriterijų vertinimą. Taikant Pareto analizę iš FMEA išskiriamos kritinės gamybos proceso defektų grupės ir, naudojantis Bajeso tinklais, surandamas efektyviausias jų šalinimo būdas. Bajeso tinklai turi defektų struktūros klasifikatorių dèl to atliekama ribota proceso patikimumo analizė. Siekiant detaliau išanalizuoti gamybinị procesą, naudojama jo struktūrinė ir dinaminė analizė, atskleidžianti proceso silpnąsias vietas, defektų medį (FTA). Tai leidžia susidaryti nuomonę apie visos sistemos patikimumą. Naudojantis FMEA bazės duomenimis, galima apskaičiuoti defektų periodiškumą ir sudaryti įrenginių palaikymo planą.

## T. Karaulova, M. Kostina, J. Sahno

## FRAMEWORK OF RELIABILITY ESTIMATION FOR MANUFACTURING PROCESSES

## S u m m a r y

Reliability of production processes is a key issue to ensuring a stable system operation, increasing a product quality, and reducing production losses. In this paper we proposed a tool for the analysis of faults in a process and the definition of the most effective way for their elimination.

In the centre of the offered framework is FMEA a reliability analysis type, the most widely used in enterprises. In the paper it is proposed to extend the FMEA by introducing a classification of faults and an estimation of expert opinions for the FMEA parameters. By using the Pareto analysis, it is possible to extract from the FMEA the most critical process failures.

To analyse these faults through the Bayesian Belief Network is the most effective way to address them. The Bayesian network structure duplicates the faults classifier structure, therefore this method fits well for this analysis. BBN enables to calculate the probabilities for each fault group based on the error of the manufacturing processes probability.

For a more complete analysis of a process we used a structural and dynamic analysis for revealing the bottlenecks of the process, as well as the Fault Tree Analysis and Reliability Block Diagram, which may be built on the base of a structural model of a process and gives the reliability of the system on the whole. On the base of the FMEA data it is possible to calculate an optimal plan of the equipment maintenance for a current process.

The framework for the analysis of the production process enables companies of machinery manufacturing enterprises to analyse processes as a whole as well as its parts for efficient forecast of the production process improvement.

Keywords: manufacturing processes, framework of reliability estimation.

Received December 02, 2011
Accepted December 11, 2012