# Modelling the Demand for AM Technologies in Polish Manufacturing Enterprises Using Bayesian Networks 

Justyna Patalas-Maliszewska (D), Małgorzata Śliwa * (D) and Marcin Topczak (D)<br>check for updates

Citation: Patalas-Maliszewska, J.; Śliwa, M.; Topczak, M. Modelling the Demand for AM Technologies in Polish Manufacturing Enterprises Using Bayesian Networks. Appl. Sci. 2021, 11, 601. https://doi.org/ 10.3390/app11020601

Received: 21 December 2020
Accepted: 7 January 2021
Published: 10 January 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (C) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Institute of Mechanical Engineering, University of Zielona Góra, 65-417 Zielona Góra, Poland; J.Patalas-Maliszewska@iim.uz.zgora.pl (J.P.-M.); m.topczak@wp.pl (M.T.)

* Correspondence: m.sliwa@iim.uz.zgora.pl


#### Abstract

Combining the knowledge about additive manufacturing technologies available in the literature with the results of empirical research in Polish manufacturing enterprises, regarding the implementation of AM, using the Bayesian network, will allow the recent demand for AM technologies to be defined in the context of an industry's needs. The main purpose of the study is to build a new model that integrates: (1) knowledge about the implementation of AM in manufacturing companies, gained from the literature, (2) knowledge about the demands and state of the use of AM from 250 Polish metal and automotive manufacturing enterprises, and (3) Bayesian networks. The results reveal that the model developed is able to accurately detect the key determinants of the implementation process of AM technologies within a manufacturing company and identify the specific requirements for the further implementation of additive technologies. The freshness of our work is defining the demand for AM technology based on the knowledge gained from literature and knowledge received through empirical study. The possibilities of using the results of research in economic practice were demonstrated. This new approach can be treated as a solution, which will both direct and help mangers to take the decision to implement AM technologies.


Keywords: additive manufacturing technology; Bayesian network; knowledge modelling; empirical research; Polish manufacturing enterprises

## 1. Introduction

Competitive market and the changing needs of customers mean that, ever more frequently, companies are forced to react quickly and modernise their production lines. In order to avoid technological backwardness, manufacturing companies are looking for new technological solutions in the area of product, process and material improvement. Additive manufacturing (AM) technologies are becoming increasingly popular, and this is particularly the case with laser technologies in the automotive, aviation, military and metal industries [1,2]. The uses of AM technologies allow the production of products of complicated shape, with a relatively low input of energy and material resources and the emission only small amounts of waste. Additive technologies can be classified by the material used (1) the type of substrate structure (2) and the form of energy supply (3). In the case of the third division criterion, one can distinguish between forms of energy supply such as a laser and an electron beam. Additive manufacturing technologies allow the costly replacement of machine and equipment components to be avoided, offering the possibility of repair using, inter alia, laser material deposition (LMD), also referred to as direct energy deposition (DED). Continuous research and progress in the field of process control, have facilitated a significant improvement of AM techniques and a significant improvement in surface roughness and the properties of materials, as well as a reduced variability between layers and the occurrence of discontinuities of embedded materials, thanks to which, manufacturing companies are increasingly deciding to implement AM technology in production. Often laser technologies allow the production parts with complex shape in

a number of materials at various scales are of great interest in the areas of prototyping [3,4]. There are reports, that manufacturing companies use additive methods to regenerate and repair machinery and equipment [5], ex. in the literature were describing reproduction of turbines and blades [6]. For this purpose, powder bed technologies are useful. These can be distinguished, i.e., selective laser melting (SLM) uses fusion in a powder bed for processing metal or selective laser sintering, SLS, consisting of merging polymer powder layers using a laser light beam [7].

The manufacturing industry is currently using AM technology in order to achieve goals related to lightness, increased functionality, a reduction in the number of parts, and a reduction in the assembly stage and also to provide maximum cost reduction and design time [8]. Many laser cladding solutions, in industry, have changed over to serial production in recent years [9]. It is carried out on technologies as well as materials with a specific composition, based, inter alia, on titanium, aluminum, iron, nickel or chromium. The subjects of the technological research are process parameters and the impact of the main elements of the laser coating process on the structure of individual paths, the results of coaxial laser plating, analysis of the impact of the main process parameters, and individual factors on the single track. In the case of research into materials, the modelling approach was examined statistically, in order to forecast selected elements on the processing path, test steel and alloys features, there mechanical properties, the micro-structure, the microhardness and the tribological properties of individual cladding paths, analyse the using individual lasers. The influence of the laser on the process and material was also examined, as the relations of the laser power on the shapes of individual paths, the influence of the laser coating process parameters on the geometry and dilution of the alloy, the change in the hardness and the microstructure, etc. [10].

In order to define the niche in the research on determining and modelling demand for AM technologies in manufacturing companies in the context of the needs of industry, based on an analysis of the literature [11-21], the main results of knowledge about AM technologies modelling were identified. The data collected are shown in Table 1.

Based on the literature analysed, the emerging AM areas where the focus of manufacturing enterprises. It is predominantly product design and quality, the consumption and selection of materials, planning and process management as well as data management. Modelling knowledge in the areas indicated allows manufacturing companies to acquire and use reliable knowledge and influence effective resource management and process management, and to reduce wastage, energy and thus. It can be observed that receiving specialist knowledge about the requirements of AM technology, is needed for different processes within a manufacturing company, such as, manufacturing planning (item 3 in Table 1), quality analysis (item 4 in Table 1) and data management in AM processes (item 6 in Table 1). Empirical research, conducted in 2019 among 250 Polish manufacturing companies from the metal and automotive industries and representing $1 \%$ of manufacturing companies in Western Poland, shows that almost half of the respondents use AM technologies, and more than half are interested in implementing AM technology. According to empirical research results, companies in the automotive industry use AM technologies mainly for production of technical devices ( $21.6 \%$ ) and prototyping ( $23.2 \%$ ), while in the metal industry they are used in the production of injection molds and precision components, which often would not be possible to produce with conventional manufacturing methods ( $43.2 \%$ ), prototyping ( $3.2 \%$ ), and regeneration and repair processes ( $2.4 \%$ ).

Table 1. Defining areas of knowledge about AM technologies in manufacturing companies.


There is a noticeable gap in any research into the modelling of the demand for applications of new, AM technologies, as well as into any research into assessing the technology implementation opportunities prior to deciding. This study attempts to establish the

demand for AM area in manufacturing enterprises as a result of combining the results of the literature research about the state of the use AM technologies in manufacturing companies and knowledge obtained through empirical research. So, a model for selecting the demand for AM in an area is sought which, based on the theoretical and empirical knowledge obtained, will enable manufacturing companies to make decisions in the field of the implementation of AM technology. The research question that we address is, therefore, 'How can the process for selecting AM technologies, be assessed within a manufacturing company, based on recent advances in AM technologies?"

This article proposes a new approach to model the demand for AM in manufacturing enterprises, using Bayesian networks (BN) in the context of Industry 4.0. Our model includes: (1) knowledge about the implementation of AM in manufacturing companies, gained from the literature, (2) knowledge about the state of the use of-and the demand for-AM within Polish manufacturing companies (3) Bayesian networks, and (4) the level of knowledge that identifies the specific requirements for the implementation of new additive technologies. Thanks to the research results, it is possible to indicate current trends in the development of AM in the context of industry's needs.

# 2. Materials and Methods 

The research conducted was based on (1) a review of the literature; (2) empirical study; (3) the use of the Bayesian networks. The combination of the research methods mentioned allows new knowledge, regarding specifically recent requirements for the implementation of new additive technologies, within a manufacturing company, to be achieved (Figure 1).
![img-0.jpeg](img-0.jpeg)

Figure 1. A model for estimating the recent demand for AM technologies.

### 2.1. Step 1: A Review of the Literature

This involved building a knowledge base in a selected area of additive technologies based on a review of the literature. Originally, articles from selected publications were reviewed within the 2016 to 2019 time-frame, corresponding to AM technologies (Step 1.1). The articles were verified in the Wiley, Springer, MDPI and Science Direct databases. Next, scientific research articles belonging to the database Science Direct, containing the keywords "single path" AND "laser" were selected to assign research areas to SLM / LPBF additive manufacturing. In order to carry out further research steps, only 52 articles were analysed [22-73].

It was noticed that the most common types of laser technologies are SLM printers, and lasers: Nd/Yd, CO2, high power diode (HPDL), YAG, hybrid, fiber, and also selfdevelopment printers. Based on the 52 articles collected, the type of laser, type of material, material, properties tested, and the 'impact factor' of the journal in which the article was

published were adopted for the knowledge base. In line with the assumptions in step 1.1, the literature review data was collected and compiled in a table (see Supplementary Table S1). Each one represents a researched article which describes a certain level of knowledge and refers to the impact factor assigned to the journal, hereinafter referred to as the IF node. This also symbolised the availability of knowledge, its complexity and the detailed nature of the research presented in it. The 1st. step in the methodology, allowed knowledge about additive manufacturing, using lasers, to be gathered, along with knowledge about the materials used and discussions on the physical and strength parameters tested.

# 2.2. Step 2: Empirical Research 

Step 2 allowed the needs of regional industry to be explored vis-à-vis the use and future implementation of incremental technologies. Originally, the study aimed to research the state of AM technologies application and needs of its implementation in Polish manufacturing companies [2]. The empirical study required the design of a closed questionnaire containing multiple-choice questions (Step 2.1). On this basis, a knowledge base was built on the interest in additive technologies shown by enterprises (Step 2.2). Next, an empirical study was conducted using a survey containing multiple-choice questions. Questionnaire concerned the needs of the polish regional industry in the field of AM technology. Attention focussed on questions contained in the areas of the AM technology used by the company (1), materials used in processes (2), the purpose of AM technology (3), the motives behind the desire to implement the new AM technology (4) and the factors affecting decisions in the field of the implementation of AM (5). The study covered 250 Polish manufacturing companies from the metal and automotive industry from the Lubuskie Voivodeship, Lower Silesia, Opole, Greater Poland, and West Pomeranian Voivodeship in December 2019. Only 99 questionnaires were selected for further work, where enterprises declared their interest in implementing additive technologies based on the sintering of metal or ceramic powders. The positive (true) answers selected by the respondents received a 'State 1', while the negative (false) was a 'State 0' (see Supplementary Table S2).

### 2.3. Step 3: The Use of Bayesian Networks

The database, based on data received in Steps 1 and 2, was installed in order to learn the Bayesian networks (Step 3). The network modelled also used rules designed to illustrate the relationship between the knowledge about AM technology in literature and the state of knowledge in enterprises. The Bayesian network has been a popular method for quantitative and qualitative risk assessment. It is especially useful for modelling rare accidents and forecasting, thanks to the possibility of using expert data, in the case of insufficient historical data.

Bayesian network is presented by acyclic graph, which shows dependencies between variables, which is described by the conditional probability collected in tables (CPTs) [74]. It allows knowledge to be gathered and classified by inference, based on premises. Premises can be modified with logical functions, thus creating a network structure described by a set of rules what allow to assess a probability of events, as example-level of knowledge [75-77]. Bayes' theorem-Equation (1)—is based on the formula which describe relations between the information or hypothesis and its evidence:

$$
\mathrm{P}(\mathrm{Y} \backslash \mathrm{Z})=[\mathrm{P}(\mathrm{Z} \backslash \mathrm{Y}) \mathrm{P}(\mathrm{Y})] / \mathrm{P}(\mathrm{Z})
$$

where:
$\mathrm{P}(\mathrm{Y} \backslash \mathrm{Z})$ —the 'a posteriori' probability of Y , due to evidence of Z ,
$\mathrm{P}(\mathrm{Y})$ —the 'a priori' probability of Y , before the evidence Z ,
$\mathrm{P}(\mathrm{Z} \backslash \mathrm{Y})$ —the probability of the Z evidence, if Y was true,
$\mathrm{P}(\mathrm{Z})$ —the probability of the Z evidence.

In our previous research work [78] the comparative analysis of classification algorithms was carried out in order to decide to use the Bayesian network to build a research model aimed at clustering knowledge. So, the proposed approach, using BN, aims to present the possibilities of the effective analysis of knowledge based on probability prediction, through the synergistic use of knowledge from the literature and the results of empirical research. Based on elements obtained from Step 1 and Step 2, BN is connected the two independent models with a common node and referred to as " P ". The value probability for this node, can answer questions in the research problem, what is the probability of identifying recent demand for AM in the context of meeting the needs of companies? Due to this, a network of dependencies was created, based on training sets. It consisted of nodes representing knowledge obtained from the literature named as the "IF" network, and empirical research named the "AM" network.

Relations for knowledge of the BN algorithm can be marked as Bayesian network $<\mathrm{B}$, $\Theta>$, with set of B nodes and set of $\Theta$ arches, which represents conditional relation. Set $\mathrm{B}\left\{\mathrm{X}_{\mathrm{i}}\right\}$, $\mathrm{i} \in \mathrm{N}$ was defined [11]. Each element of set $\mathrm{B}\{\mathrm{Xi}\}$ has an alternatives $\mathrm{x}\left\{\mathrm{x}_{\mathrm{i}, \mathrm{j}}\right\}, \mathrm{j} \in \mathrm{N}$ [10]. The training set for Bayesian networks can be described as $\mathrm{C}_{\mathrm{IF} \text { network }}=\left\{\mathrm{C}_{1}, \mathrm{C}_{2}, \ldots, \mathrm{C}_{99}\right\}$, and $\mathrm{C}_{\mathrm{AM} \text { network }}=\left\{\mathrm{C}_{1}, \mathrm{C}_{2}, \ldots, \mathrm{C}_{99}\right\}$, and their alternatives $\mathrm{x}_{\mathrm{i}, \mathrm{j}}$. Where, always the "IF" network contains elements [10]:

- X1 "Type of material", $x \in\{$ powder; filament $\}$,
- X2 "Lasers", $x \in\{\mathrm{SLM} ; \mathrm{Nd} / \mathrm{Yd}: \mathrm{YAG} ; \mathrm{CO} 2 ;$ High-power diode; Self-development; Hybrid; Fiber\},
- X3 "Materials": Fe alloy, Ti alloy, Cu alloy, Cr Ni alloy, Ceramic, Al Alloy, Hi speed steel, Stainless steel, Special alloy, Tool steel, Super alloy, YCF101, where x $\in\{$ State0;State1\},
- X4-X17 "Tested properties": Mechanical properties, Structural properties, Microstructure, Micro-hardness, Hardness, Geometry, Interlayer, Wettability, Morphology, Porosity, Morphology of melt pool, Nano-hardness, Cracking, Modelling, where $x \in$ \{State0;State1\},
- X18 "IF", impact factor for the analysed articles, $x \in\{A ; B ; C ; D ; E\}$.

The second part "AM" network, was built with elements acquired from the questionnaire, where each of item had alternatives $x \in\{$ State0; State1\}: $\square$

- Xi-Xn "P9.1 AM technologies used": FDM, EBM, Metalization, Laser, Machining, Electroerosion, Welding,
- Xi-Xn "P9.3 Material used": Steel (alloys mainly based on Fe), Other alloy, Composite, Ceramic, Polymer,
- Xi-Xn "P9.2 Goal for implement": Prototyping, Production, Revitalisation,
- Xi-Xn "P10.1 Interest of using AM technology": EBM, DMLS, Welding,
- Xi-Xn "P10.2 Determinant" of using AM technologies: Determinant A (reduction of production costs), B (effective use of material), C (freedom in product design), D (no assembly), E (product personalisation), F (quick response to market needs), G (optimization of product functions), H (other),
- Xi-Xn "P10.3 Factor of implement AM technology": Factor A (competition), B (material innovations on the market), C (the tendency of competing companies to adopt new manufacturing technologies), D (high production costs), E (demand for personalised products), F (high risk related to the lack of suitable suppliers), G (reduce the waiting time).


# 3. Research Results 

The program used to build the network, learn it and run tests was the GeNIe Academic Version 2.3.3828.0 [79]. The first step was the automatic separate learning of each network "AM" and "IF" by implementing the corresponding the knowledge base-data set (training set). The GeNie program teaches the network by using EM (Expectation-Maximisation). The advantage of EM is teaching with missing values in the training set [80]. In every experiment, the parameter initialization group was: Uniformize. This triggers the algorithm with

all network parameters taken from the uniform distribution with the existing parameters describing the network ignored. Taught networks were then connected with the result node "P", which was taught manually by inputting the appropriate Equations (2)-(5), to filled in CPT.

Therefore, three research experiments were carried out, which differed in nodes building the network. Representation of BN is presented at Figure 2, where "IF" nodes are blue color, P9.2 nodes-green, P10.1 nodes-violet, or P10.3 nodes-red. The following relationship was defined, viz. the number of elements to choose from in questionnaires in order to maximise the number of possible choices, according to the assumption: the more times choice appears, the more popular, available, and known it is.
![img-1.jpeg](img-1.jpeg)

Figure 2. The scheme of Bayesian network with "IF" nodes and all "AM" nodes.
Network constructions and rules for each experiments are presented below. Always, probability for "P" node for State0 was defined as Equation (2):

$$
\mathrm{P}_{(\mathrm{P}=\text { State } 0)}=1-\mathrm{P}_{(\mathrm{P}=\text { State } 1)}
$$

where:
$\mathrm{P}\left(\mathrm{P}=\right.$ State0)-the probability of the occurrence of State 0 of "P" node, $\mathrm{P}(\mathrm{P}=$ State1)-the probability of the occurrence of State 1 of "P" node.

The proposed "two-parts" model, firstly, using resources from literature ( 52 records) and then using data from empirical research ( 99 records), yields $85.00 \%$ and $92.00 \%$ accuracy, respectively.

# 3.1. Experiment 1 

To examine the specific requirements for the implementation of new additive technologies in companies in experiment 1, AM technologies currently used in the enterprise (P9.1i) were taken into account. These are chiefly related to the materials used by the company for production in these technologies (P9.3i). Having assumed this, the company which has shown interest in the adoption of AM technology (node group: P9), also influences the decision on the adoption of AM technology (P10.2i) orientate the goal that the company sees in the use of AM technology (P9.2i). IF node with alternative: A, B, C, D, E, always represent literature knowledge. The most frequently occurring IF helps to achieve a higher chance to implement the AM technology represented by $\mathrm{P}(\mathrm{P}=$ State1), because the largest pool of knowledge gives a chance for successful implementation. Parents influencing the P node result are the nodes: IF, P9.2 with predecessors.

Due to the Pareto principle known as 20:80, where [81] is known that only around $20 \%$ of factors have a significant impact on final effect, it was decided that knowledge in the literature about AM technologies influences the practical effect, vis-à-vis use and implementation in production enterprises. This assumption was used to build the rules to fill in CPT in the P output node in each of the experiments. However, it was decided to reduce the disproportion in the weight of the components of the rule, i.e., the "IF" node resulting from literature research and the nodes from empirical research. It is therefore claimed that $30 \%$ of literature-based knowledge ("IF" network) causes $70 \%$ of practical results in enterprises ("AM" network). In all experiments is always assumed that the more times each element of the network is selected, the more popular and accessible and therefore the more important it becomes, as symbolised by weight. Thus, the CPT for P node was described by Equation (3) which includes only the state of the parents for P node):

$$
\mathrm{P}_{(\mathrm{P}=\text { State } 1)}=\left(0.7 * \frac{\sum_{1}^{3} S_{9.2 \mathrm{i}} * w_{9.2 \mathrm{i}}}{\sum_{1}^{3} w_{9.2 \mathrm{i}}}\right)+\left(0.3 * \sum_{1}^{5} w_{\mathrm{IF}_{\mathrm{i}}}\right)
$$

where:
$\mathrm{P}_{\left(\mathrm{P}=\right.$ State1) - the probability of the occurrence of State 1 of "P" node, $S_{9.2 \mathrm{i}}$-the alternative state in 9.2 i nodes (State $1 / 0$ ), where i $\{1,2,3: \mathrm{n} \in \mathrm{N}\}$, $w_{9.2 \mathrm{i}}$-the weight assigned to the P9.2 nodes i $\{1,2,3: \mathrm{n} \in \mathrm{N}\}$, $W_{\text {IFi }}$-the weight assigned to the alternative i $\{1, \ldots, 5: \mathrm{n} \in \mathrm{N}\}$, of "IF" node.

Learning, which was conducted for BN is described by measure $\log (p) \in(-\infty ;+\infty)$ which represent fitting between the model and the data [79]. Due to the fact, that the "IF" network did not change its structure in subsequent experiments, this indicator always remained the same $=-460 . \log (p)$ for the "AM" network in experiment 1, was -1188 . The networks were connected, after the learning process, by close association and the CPT table for the node " P " was determined according to the equation 3. In each test, a Tornado analysis was performed in the GeNie programme for the resting-state network. This means a state in the network where no nodes were selected for observation. The analysis shows the sensitivity at the target node P:State1 with its positive change on the left side of the vertical axis, and negative change on the right. Figure 3 shows the combinations of nodes affecting the change in the designated probability for P. Assumed parameter spread is $100 \%$ of the current value: 0.0767 .

Through this experiment, areas of demand for AM technologies were sought, in relation to trends in the research literature, due to meet the needs of companies in the context of the implementation of AM technology. The modelled network, after learning, indicates the possibility of implementing AM technology at a level of $7.67 \%$ (Table 2). Tornado analysis was performed for goal node where $\mathrm{P}=$ State1 for each experiment. The result for experiment 1 is shown in Figure 3. Selected observations in each test were based on the nodes and their alternatives that most affect the output node. Based on the Tornado analysis and the tests conducted, it is believed that the greatest impact on positive change $\mathrm{P}(\mathrm{P}=$ State1), is the goal of implementation: "Production" (P9.2) with the highest

availability to popular journals (with low $\mathrm{IF}=\mathrm{A}$, where $\mathrm{A} \leq 2$ ). The results for the P node were poor, with the most detailed, hardly accessible knowledge, corresponding to the highest IF, i.e., $\mathrm{E}>5$.
![img-2.jpeg](img-2.jpeg)

Figure 3. The Tornado analysis for node $\mathrm{P}=$ State1 in the experiment 1.
Table 2. Results of the tests for experiment 1, estimated by the Bayesian Network.


# 3.2. Experiment 2 

Experiment 2 aimed to examine the impact of AM technologies planned to be introduced in the company (10.1i) relative to "IF" node. The parents influencing the P result are the nodes of the "IF" and P10.1. The important relations between the "IF" parts of the network and "AM" is justified just like in experiment 1, and is $30 \%$ ("IF" network) to $70 \%$ ("AM" network). There, the CPT for P node is described by Equation (4).

$$
P_{(P=\text { State1 })}=\left(0.7 * \frac{\sum_{1}^{3} S_{10.1 i} * w_{10.1 i}}{\sum_{1}^{3} w_{10.1 i}}\right)+\left(0.3 * \sum_{1}^{5} w_{\mathrm{IF}_{i}}\right)
$$

where:

$\mathrm{P}_{(\mathrm{P}=\text { State1) }}$-the probability of the occurrence of State 1 of " P " node, $S_{10.1 i}$-the alternative state in 10.1 i nodes (State $1 / 0$ ), where $\mathrm{i}\{1,2,3: \mathrm{n} \in \mathrm{N}\}$, $W_{10.1 i}$-the weight assigned to the 10.1 nodes $\mathrm{i}\{1,2,3: \mathrm{n} \in \mathrm{N}\}$, $W_{\mathrm{IFi}}$-the weight assigned to the alternative $\mathrm{i}\{1, \ldots, 5: \mathrm{n} \in \mathrm{N}\}$, of "IF" node.

The learning was conducted for the "AM" network, where $\log (p)$, in experiment 2, was -117 . The networks after the learning process were connected by relations and the CPT table for the node P was determined according to the equation 4. The effect of the P : State1, when the resting-state network is 0.0739 .

Through experiment 2, AM technologies planned to be introduced in the company were sought in relation to trends in the research literature, in order to meet the needs of companies to implement AM technology. The modelled network, after learning, indicates the possibility of implementing AM technology at the level of $7.74 \%$ (Table 3). Based on the Tornado analysis, it is believed that the greatest impact on positive change $\mathrm{P}(\mathrm{P}=$ State1) is the implementation of DMLS technology in the enterprise (P10.1). AM technologies, with the accessible studies, i.e., with the almost lowest IF (in the range $2<\mathrm{B} \leq 3$ ), give the most promising possibilities for implementing AM technologies.

Table 3. Results of the tests for experiment 2, estimated by the Bayesian network.


# 3.3. Experiment $3 a$ 

Experiment 3a is an extension of experiment 1. In this research, the possibility of implementing AM ( P node) technology is examined in addition to the impact of key industry determinants that could influence the decision to adopt AM technology in the company (10.3i), relative to "IF" nodes. The parents influencing the P node result are the nodes of the "IF", P9.2 with 9.1, 9.3, and P10.3.

The validity relationships between the "IF" part of the network and the "AM" part, again refer to the division according to the Pareto principle. This time, due to 3 components in sum, it was decided to share $40 \%$ of the weight for P9.2 and P10.3 nodes belonging to the "AM" network and $20 \%$ of the weight for the IF node. The CPT for P node is described by Equation (5):

$$
\mathrm{P}_{(\mathrm{P}=\text { State1 })}=\left(0.4 * \frac{\sum_{1}^{3} S_{9.2 \mathrm{i}} * w_{9.2 \mathrm{i}}}{\sum_{1}^{3} w_{9.2 \mathrm{i}}}\right)+\left(0.4 * \frac{\sum_{1}^{7} S_{10.3 \mathrm{i}} * w_{10.3 \mathrm{i}}}{\sum_{1}^{7} w_{10.3 \mathrm{i}}}\right)+\left(0.2 * \sum_{\mathrm{i}}^{\mathrm{s}} w_{\mathrm{IF}_{\mathrm{i}}}\right)
$$

where:
$\mathrm{P}_{(\mathrm{P}=\text { State1) }}$-the probability of the occurrence of State 1 of " P " node, $S_{9.2 i}$-the alternative state in 9.2 i nodes (State $1 / 0$ ), where $\mathrm{i}\{1,2,3: \mathrm{n} \in \mathrm{N}\}$, $S_{10.3 i}$-the alternative state in 10.3 i nodes (State $1 / 0$ ), where $\mathrm{i}\{1, \ldots, 7: \mathrm{n} \in \mathrm{N}\}$, $W_{9.2 i}$-the weight assigned to the 10.1 nodes $\mathrm{i}\{1,2,3: \mathrm{n} \in \mathrm{N}\}$, $W_{10.3 i}$-the weight assigned to the 10.3 nodes $\mathrm{i}\{1, \ldots, 7: \mathrm{n} \in \mathrm{N}\}$, $W_{\mathrm{IFi}}$-the weight assigned to the alternative $\mathrm{i}\{1, \ldots, 5: \mathrm{n} \in \mathrm{N}\}$, of "IF" node.

In experiment 3a, there was no need to learn the "AM" and "IF" fragments of the network because they consisted of previously developed parts, which were connected by relations. Occurrence P:State1, when network the resting-state network is the value 0.0425 .

Through experiment 3a, AM technologies planned to be introduced into the company were sought in addition the impact of key industry determinants that could influence the decision to adopt AM technology in the company, with relation to trends in literature research, due to needs of companies in the context of the implementation of AM technology. The modelled network, after learning, indicates the possibility of implementing AM technology at the level of $3.91 \%$ (Table 4). Based on the Tornado analysis, it is believed that the greatest impact on a positive change $\mathrm{P}(\mathrm{P}=$ State1 $)$ is to choose the goal: production (P9.2).

Table 4. Results of the tests for experiment 3a, estimated by the Bayesian Network 1.


In experiment 3a, which was based on experiment 1, tests were also conducted. Maximum result was at Test $21=15 \%$ (Table 4), where the enterprises declared as their goal, using AM: production and revitalisation at the knowledge level $\mathrm{IF}=\mathrm{A}$, where adding implication motives to analysis (P10.3i) increases the success of the implementation of AM technology.

# 3.4. Experiment $3 b$

Experiment $3 b$ is an extension of experiment 2. It is aimed at examining the impact of $A M$ technologies planned to be introduced in the company (10.1i) and the impact of key industry determinants that could influence the decision to adopt AM technology in the company (10.3i), relative to "IF" node. Thus, the parents for P node are "IF" with other nodes, P10.1 and P10.3.

The validity relationships between the "IF" part of the network and the "AM" part, again refer to division according to the Pareto principle. Due to 3 components in sum, it was decided to share $40 \%$ of the weight for P10.1 and P10.3 nodes belonging to the "AM" network and $20 \%$ of the weight for the "IF" nodes. The CPT for P node is described by Equation (6).

$$
P_{(\mathrm{P}=\text { State } 1)}=\left(0.4 * \frac{\sum_{1}^{3} S_{10.1 \mathrm{i}} * w_{10.1 \mathrm{i}}}{\sum_{1}^{3} w_{10.1 \mathrm{i}}}\right)+\left(0.4 * \frac{\sum_{1}^{7} S_{10.3 \mathrm{i}} * w_{10.3 \mathrm{i}}}{\sum_{1}^{7} w_{10.3 \mathrm{i}}}\right)+\left(0.2 * \sum_{1}^{5} w_{\mathrm{IF}_{\mathrm{i}}}\right)
$$

where:
$\mathrm{P}_{\{\mathrm{P}=\text { State }\}}$ —the probability of the occurrence of State 1 of " P " node,
$S_{10.1 i}$ —the alternative state in 10.1 i nodes (State $1 / 0$ ), where i $\{1,2,3: \mathrm{n} \in \mathrm{N}\}$,
$S_{10.3 i}$ —the alternative state in 10.3 i nodes (State $1 / 0$ ), where i $\{1, \ldots, 7: \mathrm{n} \in \mathrm{N}\}$,
$W_{10.1 i}$ —the weight assigned to the 10.1 nodes i $\{1,2,3: \mathrm{n} \in \mathrm{N}\}$,
$W_{10.3 i}$ —the weight assigned to the 10.3 nodes i $\{1, \ldots, 7: \mathrm{n} \in \mathrm{N}\}$,
$W_{\mathrm{IF} \mathrm{i}}$ —the weight assigned to the alternative $\mathrm{i}\{1, \ldots, 5: \mathrm{n} \in \mathrm{N}\}$, of "IF" node.
In experiment 3b, there was no need to learn the "AM" and "IF" fragments of network because it consisted of previously developed parts, which were connected by relations. Occurrence $\mathrm{P}=$ State1, when network the resting-state network is the value 0.0424 .

Through experiment 3b, AM technologies planned to be introduced in the company were sought in addition the impact of key industry determinants that could influence the decision to adapt adopt AM technology in the company, with relation to trends in literature research, in order to meet the needs of companies in the context of the implementation of AM technology. The modelled network, after learning, indicates the possibility of implementing AM technology at the level of $3.91 \%$ (Table 5). Based on the Tornado analysis, it is believed that the greatest impact on positive change $\mathrm{P}(\mathrm{P}=$ State1), is implementation of DMLS technology in the enterprise (P10.1). Smoothing the distribution of results, in the tests conducted, with results spread $=0.07$ (min. Test 5, max. Test 3, Table 5), may indicate that the motive for the implementation of AM (P10.3) should not be directly related to success ("P" node) or that key industry determinants do should not coincide with the implementation objectives of individual enterprises. The best results give the possibility to implement knowledge about AM technologies with middle $\mathrm{IF}=\mathrm{C}$ level $(3<\mathrm{C} \leq 4)$ and with the lowest IF (in the range $\mathrm{A} \leq 2$ ).

Table 5. Results of the tests for experiment 3b, estimated by the Bayesian Network.


# 4. Discussion 

The changes that can be observed on the market influence the decisions of managers in manufacturing companies, in particular in the area of applied AM technologies. Production companies analysing the market and available technologies need a tool to facilitate decision making in the area of implementing new technology. The presented model, based on the BN, can be treated as a solution, which will direct and help to assess the decision vis-à-vis implementing AM technologies.

The main goal of our research experiments was to identify the demand for AM in Polish manufacturing companies. Based on the conducted research it is believed that:

- Management sees the rationale for implementation of AM technologies in the production area and by using the proposed model (results of experiment 1 and 2) it is possible to determine the type of AM technology needing to be implemented (in our case study it is DMLS technology).
- The key determinants that influence the decision to adopt AM technology in the company is the need of customers to reduce the waiting time for the product and their demand for personalised products.

- There is a need to build a customer-oriented, knowledge-driven framework in order to implement AM technology
Moreover, the results of the tests of the research experiments in estimating the recent demand for AM technologies, as assessed by the Bayesian network illustrate that:
- The most hardly accessible knowledge of articles from Journals corresponding to the highest Impact Factor, i.e., IF $>5$, does not affect the successful implementation of AM technology within a manufacturing company, in contrast to the positive impact on the implementation of AM technology with readily available knowledge.
- Smoothing the distribution and the small variability in the results, in the case of research conducted with "AM implementation motive", means that it should not be directly related to the success of the implementation of AM technologies or that key industry determinants should not coincide with the real objectives of individual enterprises.
- The practical needs of enterprises, symbolised by the achievement of goals, contributes to success in implementing AM technology.
The results of the experiment 1 illustrate that although empirical studies have obtained results showing that companies in the automotive industry use AM technologies mainly for prototyping ( $23.2 \%$ ), as a result of combining these results with analysis of the literature on results, the purpose of implementing AM technology is production. Experiment 2 enabled to indicate AM technology that should be implemented in the company-in our case study, it is DMLS technology.

We know that mangers can determinate the knowledge transfer in a manufacturing company [82] and therefore the obtained models, that is, the results of experiments 1 and 2, can be useful for managers in terms of assessing the decision vis-à-vis the implementation of AM technologies in the following way.

- The research questions indicated in the research methodology should be put to managers in the company.
- The answers obtained should then be added to the database on which the model is currently built.
- The Bayesian network will be again subjected to training.
- Finally, the manager receives a recommendation to choose an area of AM technology to apply (results of experiment 1) along with a specific type of technology (results of experiment 2).
Advantages of the use of obtained models based on results of experiment 1 and experiment 2:
- Possibility for managers to assess the decision vis-à-vis the implementation of AM technologies, based on the knowledge gained from literature and the knowledge received through empirical study.
- Ease with which the model can be adapted to the needs of a given company by adding a response from the given experts to the database.
- Posssibility of defining the recommended AM technology to be implemented within a company.
The secondment (results of experiment 3a and 3b) presents the need to analyse customer expectations for our products in the decision-making process regarding the purchase of AM technology. Research results indicate that recent research into AM technologies should cover the needs of customers of manufacturing companies. Therefore, the proposed model (results of experiments 3a and 3b) makes it possible to indicate an area that is the main motivation for making a decision vis-à-vis implementing AM technology. These models (results of experiments 3a and 3b) are also useful for enterprise managers in the context of the implementation of AM technology, because the manager receives a recommendation about the main motivation for implementing AM technology. The procedure for using these models is identical to models resulting from experiment 1 and experiment 2.

The limitation of our approach is that this study focuses on the limited number of articles that were reviewed and Polish manufacturing industries. It would be unwise to generalize the findings too broadly to other enterprises. However, the advantage of the proposed approach is that it is possible to automatically define the demand for AM technology based on the knowledge gained from literature and knowledge received through empirical study to help mangers to take the decision to implement AM technologies.

The presented results require further work to improve the operation of the algorithm and the reliability of the effects. The proposed BNs models are dedicated to the metal and automotive industries-especially production companies struggling with the implementation of new technologies. The dedicated algorithm could also be used in other branches of industries, but this requires additional empirical research, particularly proposals of newly dedicated rules describing the node relations of the Bayesian network. Additionally, it is planned to implement the developed models as part of IT decision support system.

# 5. Conclusions 

In this paper, attention was paid to modelling the demand for AM technologies in Polish manufacturing enterprises, because a research gap in this area was identified through analysis of the literature. Modelling knowledge in the said area is an extremely important aspect, because making decisions about the implementation of a new technology is often associated with involving large financial and investment resources. Incorrect assessment, at the decision-making stage, of the opportunities for implementation, as well as regarding the areas of demand and application of the planned technology, without proper verification, can cause huge material losses, as well as contribute to the failure of the project.

This paper presents the results of research in the field of improving the decisionmaking processes vis-à-vis the implementation of additive manufacturing in Polish production companies. The main advantage of the proposed approach is the two-stage demand for modelling AM technology, based on knowledge gained from the literature and knowledge received via empirical study, confirming the validity of the innovative model proposed. Our idea was to create a model to support managers in making decisions about the implementation of AM technology. We believe that supervising the decision-making processes vis-à-vis the implementation of AM, can be done by using our models automatically and having a data base containing expert knowledge, received from the literature and from managers.

Supplementary Materials: The following are available online at https://www.mdpi.com/2076-3 417/11/2/601/s1, Table S1: Literature review data for learning "IF" Bayesian networks, Table S2: Empirical data for learning "AM" Bayesian networks.

Author Contributions: Conceptualization, J.P.-M.; data curation, M.Ś.; formal analysis, J.P.-M., M.Ś., and M.T.; funding acquisition, J.P.-M.; methodology, J.P.-M., M.Ś., and M.T.; resources, J.P.-M., M.Ś., and M.T.; software, M.Ś.; validation, J.P.-M., M.Ś., and M.T.; visualization, J.P.-M. and M.Ś.; writingoriginal draft, J.P.-M., M.Ś., and M.T.; writing-review and editing, J.P.-M., M.Ś., and M.T. All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by the programme of the MINISTEROFSCIENCEANDHIGHEREDUCATION under the name: "Regional Initiative of Excellence" in 2019-2022 project number 003/RID/2018/19; funding amount 11.936.596.10 PLN.

Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
