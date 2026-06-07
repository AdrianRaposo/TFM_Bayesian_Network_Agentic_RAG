# Article 

## Life Cycle Assessment of Bridges Using Bayesian Networks and Fuzzy Mathematics

Zhi-Wu Zhou ${ }^{1, \star}$ (D), Julián Alcalá ${ }^{1}$, Moacir Kripka ${ }^{2}$ (D) and Víctor Yepes ${ }^{1}$ (D)<br>check for updates

Citation: Zhou, Z.-W.; Alcalá, J.; Kripka, M.; Yepes, V. Life Cycle Assessment of Bridges Using Bayesian Networks and Fuzzy Mathematics. Appl. Sci. 2021, 11, 4916. https://doi.org/10.3390/app11114916

Academic Editors: Montserrat Zamorano, Javier Ordóñez and Raffaele Marotta

Received: 26 April 2021
Accepted: 20 May 2021
Published: 27 May 2021

Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## (0)

Copyright: (c) 2021 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Institute of Concrete Science and Technology (ICITECH), Universitat Politècnica de València, 46022 Valencia, Spain; jualgon@cst.upv.es (J.A.); vyepesp@cst.upv.es (V.Y.)
2 Civil and Environmental Engineering Graduate Program (PPGEng), University of Passo Fundo, Passo Fundo CEP 99052-900, Brazil; mkripka@upf.br

* Correspondence: zhizh2@doctor.upv.es; Tel.: +34-96-387-9563

Abstract: At present, reducing the impact of the construction industry on the environment is the key to achieving sustainable development. Countries all over the world are using software systems for bridge environmental impact assessment. However, due to the complexity and discreteness of environmental factors in the construction industry, they are difficult to update and determine quickly, and there is a phenomenon of data missing in the database. Most of the lost data are optimized by Monte Carlo simulation, which greatly reduces the reliability and accuracy of the research results. This paper uses Bayesian advanced fuzzy mathematics theory to solve this problem. In the research, a Bayesian fuzzy mathematics evaluation and a multi-level sensitivity priority discrimination model are established, and the weights and membership degrees of influencing factors were defined to achieve comprehensive coverage of influencing factors. With the support of theoretical modelling, software analysis and fuzzy mathematics theory are used to comprehensively evaluate all the influencing factors of the five influencing stages in the entire life cycle of the bridge structure. The results show that the material manufacturing, maintenance, and operation of the bridge still produce environmental pollution; the main source of the emissions exceeds $53 \%$ of the total emissions. The effective impact factor reaches 3.01. At the end of the article, a big data sensitivity model was established. Through big data innovation and optimization analysis, traffic pollution emissions were reduced by 330 tonnes. Modeling of the comprehensive research model; application; clearly confirms the effectiveness and practicality of the Bayesian network fuzzy number comprehensive evaluation model in dealing with uncertain factors in the evaluation of the sustainable development of the construction industry. The research results have made important contributions to the realization of the sustainable development goals of the construction industry.

Keywords: construction industry; environmental; impact factor; analysis; contribution

## 1. Introduction

The building industry, as an important basic industry of the national economy, has a pivotal role in improving human settlements, managing the ecological environment, and developing a circular economy [1]. At the same time, the construction industry, along with power generation and automobile use, is one of the three major sources of greenhouse gas emissions threatening the Earth's climate [2]. Today, buildings still account for nearly $40 \%$ of global energy consumption and carbon emissions [3,4]. Governments around the world are adopting and implementing various financial regulations and incentives to mitigate the impact of the built environment [5].

The International Organization for Standardization and the International Society for Environmental Toxicology and Chemistry have defined a life cycle impact assessment framework and a list of life cycle impact parameters with 18 categories [6]. The Product Social Impact Life Cycle Assessment database version 1.0 summarizes data from about 15,000 departments and 189 countries/regions around the world, and finally determines

88 qualitative and quantitative indicators [7]. Researchers use midpoint and endpoint modelling in the full life cycle feature modelling and weight factor analysis. The weighted parameters for influencing factors are optimized by Monte Carlo simulation set by software after empirical setting [8,9]. No scientific research methods have been established to improve the reliability and accuracy of influencing parameters.

After analyzing the above research, some ideas appear: whether the software evaluation criteria are consistent [10,11], whether the database is updated in time, whether the case analysis is perfect [12], whether the theoretical modelling is more practical [13], and whether the special research on complex structure bridges and the environmental, economic, and social impacts of the project are considered [14].

The goal of the research is to meet the maximum safety and minimum life cycle cost and environmental impact in order to solve the above-mentioned problems [15]. The first problem is to improve the reference framework and method of bridge life cycle assessment.

This work solves the following problems:
(1) A Bayesian network fuzzy mathematical model is established to solve the uncertainty problem of the environmental impact factors of bridges.
(2) The conclusion of the software analysis is checked to improve the accuracy and refinement of the research.
(3) In order to provide research ideas for reducing environmental pollution, the database optimization analysis is carried out in the stage of environmental contribution.
(4) Research has proved that basic science and applied science are closely related [16], and that strong theoretical support requires sufficient calculations for testing.

Through the establishment of the BNFC model, the environmental impact weight of five stages is deduced and calculated. The environmental impact of bridge is analyzed by OpenLCA software.

The innovation of this work lies in the application of BN and FMT in the process of the environmental impact assessment of bridges. First, the uncertain multi-factors are modelled and scientifically calculated. The calculation conclusion is applied to the analysis and evaluation process of the LCA software again, and finally the analysis conclusion is fitted with the modelling calculation, and the two are linearly consistent. We realize the accurate processing and effective evaluation and comprehensive analysis of uncertain data in the LCA evaluation process, and improve the accuracy of uncertain factors in LCA analysis.

# 2. Literature Review 

### 2.1. Current Situation of Research Results on Environmental Impact of Construction Industry

The research group searched the publishing results related to the three keywords of construction industry, environment, and research through Scopus [17], and found a total of 5391 articles and conference literature (1990-2021). This paper selects the journals published from 1990 to 2020 (accounting for $93.26 \%$ of the total articles) for cluster statistical analysis, as shown in Figure 1.

The survey results show that the environmental impact research results of the construction industry are increasing year by year, with the increasing rate reaching $11.36 \%$; the growth rate of global environmental impact research regions is $4.83 \%$, with the total number reaching 104 countries and regions, accounting for $44.64 \%$ of the global total [18]. The number of publications in the top ten countries accounted for $87.40 \%$ of the total, while other countries and regions only accounted for $12.6 \%$. Therefore, environmental governance has nothing to do with political, economic, and cultural background [19].

Cluster analysis of articles published globally over 31 years showed that the core words project performance, occupational health, sustainable construction, etc. ranked as the top ten words that are not related to mathematics. Articles about mathematical theoretical models appeared during the period of 1998-2008, and the combination of environment and mathematical modelling theory was missing. There is a phenomenon of interdisciplinarity between clusters. After 2008, the number of articles being published

decreased, but the research direction broadened systematically and comprehensively, and it tended to focus on environmental sustainability. Researchers now pay more attention to systematic research on environmental impact. The analysis conclusions show that basic science and form science are developing simultaneously, and interdisciplinary applications are necessary. Multidisciplinary research can reduce the uncertainty in the software analysis process, further improve the accuracy of Monte Carlo simulation, and make the research more complete and more scientific.
![img-0.jpeg](img-0.jpeg)

# Top 25 Keywords with the Strongest Citation Bursts 

![img-1.jpeg](img-1.jpeg)

Figure 1. Cluster analysis of published articles.

# 2.2. Uncertainty of Environmental Impact Factors in Construction Industry 

The construction industry provides the necessary infrastructure and buildings for human activities [20], while emitting $33 \%$ of the global carbon [21]. According to industry standards, it can be divided into direct and indirect emissions [22]. Direct emissions refer to carbon emissions generated in design, construction, maintenance, and demolition activities [23,24]; indirect emissions refer to the industrial upstream activities of all raw materials [25]; therefore, it is difficult to conduct a comprehensive evaluation on the micro level [26]. Macroscopically, the construction industry has close interaction with other industries [27]. How can we accurately capture the dynamic influencing factors in the whole project life cycle [28], how do we accurately study the discrete state of engineering uncertain factors is the key [29,30], and how do we judge and ignore the uncertain influencing factors for accurate modelling [31]? This is also a problem to be solved in this work. Accurately determining the uncertainty of influencing factors can improve the analytical value of research data at each stage and the optimization of database-related data, while excluding empirical assumptions and speculations.

### 2.3. Environmental Impact Assessment Method of Construction Industry

Considering the uncertainty of data in LCA analysis of bridges, Monte Carlo simulation and genetic algorithm are widely used [32,33]. Researchers proved the sustainability of LCA by weighting the analytic hierarchy process and assessment [34,35]. Sánchez-Garrido and Yepes used multi-criteria assessment to optimize villa sustainability [36].

In view of the diversification of LCA research software and research methods and the differences between them, the research team decided to expand the search scope and research scope in Scopus. The key words included: environment, engineering, bridge, and research method. In total, 2624 articles and conference papers were retrieved. From 2010 to 2021, 1447 articles were classified according to 160 keywords, and the analysis methods used included: the finite element method (251), Monte Carlo methods (71), numerical model (333), neural networks (98), genetic algorithms (77), and sensitivity analysis (134). No more specific and effective strategies were found for the uncertain factors in LCA.

Openlcal. 10 [37] was used in this research. The software uses Monte Carlo simulation to perform uncertainty distribution and geometric mean and geometric standard deviation [11]. Before the software system started the simulation, it was necessary to empirically set the influence weight coefficient of each influencing parameter. The question arises: does every researcher have rich engineering construction management experience? If researchers without similar architectural experience have determined the impact weights, are the research conclusions perfect and accurate, and how do we solve this problem scientifically?

### 2.4. Determination of Environmental Impact Assessment Method

How do we accurately reflect the change characteristics of a dynamic environment and update parameters [38], and how can we qualitatively and quantitatively describe the dependence between variables using the proposed Bayesian Networks [39]. A Bayesian network is an effective tool for probabilistic modelling and causal reasoning, which is effective for reliability modelling and evaluation of complex systems under dynamic conditions [40].

In the field of construction engineering, it is difficult to obtain accurate probability values [41]. Fuzzy set theory is usually used to deal with fuzzy and imprecise events effectively [42], and fuzzy mathematics theory is introduced. Fuzzy mathematics theory and Bayesian networks are both powerful and effective tools for knowledge reasoning in uncertain environment [43,44]. Therefore, in this work, FMT and BN are used as a decisionmaking method, referred to as BNFC. BNFC solves the problems in the above analysis and further improves the feasibility and scientific of the research. This model improves the effective evaluation and dynamic processing of uncertain factors in LCA research.

## 3. Methodology

### 3.1. Research Theory (BN and Basic Principles of FMT)

As shown in Figure 2, as the complexity of influencing factors increases, the diversity and uncertainty of parameters increase. How do we properly model and quantify to improve the reliability of data [45]? Bayesian network is a system modelling language used to deal with the relationship between random variables [46], in order to achieve the best accurate reasoning conclusion [47].

![img-2.jpeg](img-2.jpeg)

**Figure 2.** Schematic diagram of BN principle.

In 1965, Zadeh, L.A., an American cybernetic scholar, first proposed the concept of "Fuzzy Mathematics". A new fuzzy set and membership frame model is proposed to solve and deal with the inaccuracy of information representation and reasoning [48]. Fuzzy mathematics is a mathematical theory and method to study and deal with fuzzy phenomena (Figure 3). Through the analysis of fuzzy comprehensive evaluation, we can find out the common rules and attributes of set objects and establish the model [49].

![img-3.jpeg](img-3.jpeg)

**Figure 3.** The basic methods and steps of FMT comprehensive evaluation.

### 3.2. Theoretical Model Bridge Process

The introduction of some important definitions used in FMT structural hierarchy theory helps to fully understand the subsequent modelling applications (a single factor influences the weight matrix: the FMT comprehensive evaluation principle is based on the analysis and evaluation of each single impact factor (u<sub>1</sub>) in U, and after the analysis is completed, it is summarized into a set form (Figure 4). To solve the maximum eigenvalue λ<sub>max</sub> and corresponding eigenvector ν of the judgement matrix at this level, the judgement matrix needs to be normalized as the impact factor of this level on the previous level.

Consistency index:

$$CI = \left(\lambda_{max} - n\right) / (n - 1) \tag{1}$$

where CI is the consistency index; λ<sub>max</sub> is the maximum eigenvalue of the judgement matrix; and n is the number of levels.

$$CR = \frac{CI}{AI} \tag{2}$$

where CR is the consistency ratio; and AI is the average consistency index.

Equation (1) is substituted into Equation (2), giving

$$CR = \left(\lambda_{max} - n\right) / (n - 1) / AI \tag{3}$$

Judgement basis: if $\mathrm{CR} \geq 0.1$, the consistency of the impact weight matrix is not acceptable; if $\mathrm{CR}<0.1$, the consistency of the impact weight matrix is acceptable.
![img-4.jpeg](img-4.jpeg)

Figure 4. Schematic diagram illustrating the single factor influence weight matrix.
Hypothesis set $\mathrm{U}=\left\{\mathrm{u}_{1}, \mathrm{u}_{2}, \cdots \cdots, \Lambda, \mathrm{u}_{\mathrm{m}}\right\}$, weight set $\mathrm{A}=\left\{\mathrm{a}_{1}, \mathrm{a}_{2}, \cdots \cdots, \Lambda, \mathrm{a}_{\mathrm{m}}\right\}$, and comment set $\mathrm{V}=\left\{\mathrm{v}_{1}, \mathrm{v}_{2}, \cdots \cdots, \Lambda, \mathrm{v}_{\mathrm{m}}\right\}$ are established according to the fuzzy synthetical assessment theory. To perform quantitative results analysis, the comment set is divided into five levels, as shown in Figure 5:
![img-5.jpeg](img-5.jpeg)

I impact factor $=$ One item in total; II impact factor $=$ Five items in total; III impact factor $=31$ items in total; IV impact factor $=68$ items in total; V impact factor $=12$ items in total.

Figure 5. Schematic diagram of tree-shaped BN of environmental impact contribution of cable-stayed bridge.
Description: There are a total of 117 environmental impact factors for cable-stayed bridges. The amount of data information is huge-see the attached table for relevant data.

$$
\mathrm{V}=\left\{\begin{array}{cc}
\mathrm{v}_{1}=(-\infty, 0] & \text { Not effect } \\
\mathrm{v}_{2}=(0,+0.5] & \text { Slight effect } \\
\mathrm{v}_{3}=(0.5,1.0] & \text { Affect } \\
\mathrm{v}_{4}=(1.0,1.5] & \text { Moderate effect } \\
\mathrm{v}_{5}=(1.5,+\infty) & \text { Great effect }
\end{array}\right.
$$

The i-th impact factor is evaluated by the i the factor $u_{i}$ of the assessment object (factors at each phase), and the degree of membership of the $j$ th element $v_{j}$ in the comment set is $r_{i j}(\in v \notin$ cannot be used) because the fuzzy set has no strict demarcation. The degree of membership, that is, $r_{i j}$, is introduced to represent the degree of belonging of the element $j$ to the fuzzy set $v_{j}$ [50]; $r_{i j}$ is any number between 0 and 1 . The fuzzy set $u_{i}$ of factors $i$ can be expressed as:

$$
\mathrm{R}_{\mathrm{i}}=\left\{\frac{\mathrm{r}_{11}}{\mathrm{v}_{1}}+\frac{\mathrm{r}_{12}}{\mathrm{v}_{2}}+\cdots \cdots+\Lambda+\frac{\mathrm{r}_{\mathrm{im}}}{\mathrm{v}_{\mathrm{m}}}\right\}
$$

where $R_{i}$ is the assessment set of a single factor; $r_{i m}$ is the membership of $m$ kinds of elements; and $v_{m}$ is the comment set of $m$ kinds of elements. All the single-factor fuzzy assessment sets are integrated into an impact weight matrix:

$$
\mathrm{R}=\left[\begin{array}{cccc}
\mathrm{r}_{11} & \mathrm{r}_{12} \cdots \cdots & \Lambda & \mathrm{r}_{1 \mathrm{~m}} \\
\mathrm{r}_{21} & \mathrm{r}_{22} \cdots \cdots & \Lambda & \mathrm{r}_{2 \mathrm{~m}} \\
\vdots & \vdots & \vdots & \vdots \\
\vdots & \vdots & \vdots & \vdots \\
\mathrm{r}_{\mathrm{n} 1} & \mathrm{r}_{\mathrm{n} 2} & \Lambda & \mathrm{r}_{\mathrm{nm}}
\end{array}\right]
$$

where R is the single-factor fuzzy impact weight matrix.

# 3.3. LCA Research Framework and Parameters 

ISO stipulates the LCA standard research framework: the goal and scope definition, inventory analysis, impact assessment, and interpretation. These are GWP, AP, FEP, PMFP and WP. It includes five stages: survey and design, material manufacturing, construction and installation, maintenance and operation, and disassembly and recycling [11]. OpenLCA1.10 software is the analysis software used in this study [37]. The databases used in this study include Ecoinvent [51] and Bedec [52].

### 3.4. Research External Conditions

We followed the regulations and research results of the United Nations Environment Programme (UNEP); the Joint Research Center of the European Commission and Mansour Rahimi and others and have reconsidered the use of research methods [53-55].

In consideration of the above representative research results and 2.1 and 2.2, the BNFC was combined with the midpoint and the endpoint to build a model. We chose sufficient raw data and effective evaluation. The focus was on traffic pollution during the maintenance phase.

### 3.5. Impact Factor

In the study by Zhou et al., according to the characteristics of the full life cycle of the cable-stayed bridge, the value of the influence factor of each stage was accurately defined, which laid the foundation for the analysis conclusion [11]. The analysis in OpenLCA1.10 software needs to set the range of influence factors ( 1.00 to 1.50 ) at each stage. In this study, a more accurate BNFC was used to synthesize weighted impact factors.

### 3.5.1. Bridge a BN Hierarchical Analysis Model

Figure 5 shows the five levels of impact index analysis and assessment built based on research results and the BN. The first level is the total contribution of the cable-stayed

bridge to environmental emissions; the second level is the values of the five stages; the third level is the value of the contribution of each process; the fourth level is the value of the contribution of each type; and the bottom level is the values of the contributions of materials and equipment.

# 3.5.2. Establishing Impact Weight Matrix 

The comprehensive assessment of impact factors is considered in the bridge analysis. The fuzzy comprehensive assessment hypothesis is expressed as $\mathrm{K}=\mathrm{AoR}=\left\{\mathrm{k}_{1}, \mathrm{k}_{2} \cdots \cdots, \Lambda, \mathrm{k}_{\mathrm{n}}\right\}$, where o is the fuzzy composition operator; and $\mathrm{k}_{\mathrm{n}}$ is the fuzzy comprehensive assessment index. An equation can be obtained as follows based on the generalized fuzzy operations

$$
\mathrm{k}_{\mathrm{j}}=\left(\mathrm{a}_{1} \Lambda \mathrm{r}_{1 \mathrm{j}}\right) \mathrm{V}\left(\mathrm{a}_{2} \Lambda \mathrm{r}_{2 \mathrm{j}}\right) \mathrm{V} \Lambda \mathrm{~V}\left(\mathrm{a}_{\mathrm{m}} \Lambda \mathrm{r}_{\mathrm{mj}}\right)
$$

where $\mathrm{j}=(1,2, \cdots \cdots, \Lambda, \mathrm{n}) ; \mathrm{V}$ represents the operation "or"; and $\Lambda$ represents the operation "and".

The comprehensive Bayesian fuzzy impact weight model can be written as:

$$
\mathrm{E}(\Lambda, \mathrm{~V}), \mathrm{k}_{\mathrm{j}}=\mathrm{V}_{\mathrm{i}=1}^{\mathrm{m}}\left(\mathrm{a}_{\mathrm{i}} \Lambda \mathrm{r}_{\mathrm{ij}}\right), \mathrm{j}=(1,2, \cdots \cdots, \Lambda, \mathrm{n})
$$

### 3.5.3. Hypothesis

As shown in Figure 5, there is 1 first-level indicator, 5 second-level indicators, 31 third-level indicators, 68 fourth-level indicators, and 12 fifth-level indicators to derive the conclusion based on Equations (1)-(5).

$$
\begin{aligned}
& \mathrm{R}=\left[\begin{array}{cccccc}
\mathrm{r}_{11} & \mathrm{r}_{12} & \mathrm{r}_{13} & \mathrm{r}_{14} & \mathrm{r}_{15} \\
\mathrm{r}_{21} & \mathrm{r}_{22} & \mathrm{r}_{23} & \mathrm{r}_{24} & \mathrm{r}_{25} \\
\mathrm{r}_{31} & \mathrm{r}_{32} & \mathrm{r}_{33} & \mathrm{r}_{34} & \mathrm{r}_{35} \\
\mathrm{r}_{41} & \mathrm{r}_{42} & \mathrm{r}_{43} & \mathrm{r}_{44} & \mathrm{r}_{45} \\
\mathrm{r}_{51} & \mathrm{r}_{52} & \mathrm{r}_{53} & \mathrm{r}_{54} & \mathrm{r}_{55}
\end{array}\right]=\left[\begin{array}{cccccc}
1 & 1 & 1 & 1 & 1 & \mathrm{I}_{\text {level }} \\
1 & 1 & 1 & 1 & 1 & \mathrm{II}_{\text {level }} \\
3 & 7 & 8 & 6 & 7 & \mathrm{III}_{\text {level }} \\
9 & 16 & 18 & 15 & 10 & \mathrm{IV}_{\text {level }} \\
12 & 0 & 0 & 0 & 0 & \mathrm{~V}_{\text {level }}
\end{array}\right] \\
& {\left[\begin{array}{cccccc}
1-\lambda & 1 & 1 & 1 & 1 & \text { level } \\
1 & 1-\lambda & 1 & 1 & 1 & \mathrm{II}_{\text {level }} \\
3 & 7 & 8-\lambda & 6 & 7 & \mathrm{III}_{\text {level }} \\
9 & 16 & 18 & 15-\lambda & 10 & \mathrm{IV}_{\text {level }} \\
12 & 0 & 0 & 0 & 0-\lambda & \mathrm{V}_{\text {level }}
\end{array}\right]} \\
& \text { solve to get the numerical value }
\end{aligned}
$$

$\lambda_{1}=0, \lambda \lambda_{2}=1, \lambda_{3}=3, \lambda_{4}=15$. The interval range of the influence factor is calculated by taking the value of $\lambda_{2}$, combining the eigenvectors of each stage and the preliminary assumption of the interval range set by the LCA software. We can assume the impact factor weight parameters as being $\mathrm{E}=(1.00,1.02,1.10,1.45,1.01)$. The conclusions of analyses of subsequent cases will be used to check the accuracy of the assumed weight parameters.

## 4. Case and Results

### 4.1. Case Description

To better apply fuzzy mathematics to study the uncertain data of bridges, careful comparison and consideration have been made in the selection of bridge cases: bridges have similar structural types (cable-stayed bridges), similar lengths, the same construction schemes, and the same purpose (first-class highway bridge), and the designed lifetime is 100 years.

Case 1: SQ is a canal bridge. The main bridge has a total length of 212 m , a width of 26.5 m , a beam height of 2.3 m . Figure 6 shows $C$ cable-stayed bridge. The main tower is built using a creeping formwork. The side span beam and the girder \#0 are cast in place with the bracket method, and girders \#1-\#16 are constructed with a hanging basket [56].

![img-6.jpeg](img-6.jpeg)

Figure 6. Schematic diagram of two bridges.
Case 2: EH is in the Lao Dao Kou area of Shenyang, China. The main bridge is a cable-stayed bridge, with a span of 236 m , a width of 32 m , and a beam height of 3.16 m . The top plate of the beam is 26 cm thick, the bottom plate is 24 cm thick, as Figure 6 shows. The beam blocks \#1-\#13 (-\#1--\#13, with \#1-\#16 on the left and -\#1--\#16 on the right.) are built using the slide formwork method, and blocks \#0 and \#14-\#16 (-\#14--\#16) are built using the cast-in-place method [57].

The contributions of the two cable-stayed bridges to environmental emissions in five phases are analyzed first, as shown in Figure 5. Data sources include design contracts and plans, data from the survey and design phase, construction drawings, geological survey reports, construction organization design, published research results, observed local transportation data, observation data obtained from environmental protection and meteorological departments, and the Ecoinvent and Bedec databases. The criteria for the use of research resources include rich experience in bridge engineering, scientific research theories, and comprehensive research and analysis capabilities.

According to the LCA analysis process, the energy consumption of the bridge occurs in five stages, mainly in the material manufacturing stage and the maintenance and operation stage.

# 4.2. Survey and Design 

The pile foundations of SQ and EH are end bearing piles. According to China (GB) 50021-2001 regulations [58], the distance between exploratory points of end bearing piles is $12 \sim 24 \mathrm{~m}$ and the distance between exploratory points of friction piles is $20 \sim 35 \mathrm{~m}$; the depth of exploration is expected to increase by $3 \sim 5 \mathrm{~m}$. See Table 1 for specific data.

Table 1. Data summary table for the survey and design stage.


Note: Total drilling time $=$ drilling time $\times(1+20 \%)$, where $20 \%$ is the equipment loss times ratio.

### 4.3. Material Manufacturing

The main materials of SQ and EH are C (C50, C40, C30, C25, C20, C15), asphalt C, steel bars, steel strands, profiles, bellows, anchors, cables, and so on. Auxiliary materials include one creeping formwork for each tower (the weights of the creeping formworks of SQ and EH are 28.2 and 32.2 tonnes, respectively) and one hanging basket for SQ's girder, with a weight of 210 tonnes. EH's girder uses a slide formwork (the entire system consists of a formwork, fixed pier and mounting bracket, traction and slide devices, rear hanging equipment, etc.) with a weight of 360.67 tonnes.

Sections \#0 and $-\# 16 \sim-\# 7$ of SQ adopt the bracket method (the bracket pipe should have a wall thickness of 3.0 mm and a diameter of 48 mm ) for cast-in-place construction. The length is 76.5 m , the average height is 12 m , and the weight is 2770.72 tonnes. Sections \#0 and \#14-\#16(-\#14--\#16) of EH adopt the bracket method (the bracket pipe should have a wall thickness of 3.0 mm and a diameter of 48 mm ) for cast-in-place construction. The length is 66 m , the average height is 7 m , and the weight is 1552.78 tonnes.

Both bridges are municipal projects and use commercial C according to the contract. The transportation distances from SQ and EH to the commercial C plant are 16 and 15 km , respectively.

### 4.4. Construction and Installation

The main processes of SQ are the construction of main piers and foundations; the construction of side piers, auxiliary foundations, and foundations; the erection of bracket \#0 and construction of the lower tower column and block \#0 of the main tower; the construction of the upper tower of the main tower and erection of side span cast-inplace bracket; the installation of the hanging basket and repeat pouring of blocks \#1-\#16 $(-\# 1 \sim-\# 16)$; the cast-in-place construction of the side span; the locking of the closure section; and the bridge floor and auxiliary construction.

The main processes of EH are the pile foundation construction; bearing platform construction; pier body construction; the cast-in-place \#0 block after erecting the steel pipe support; the pouring construction of the main tower's creeping formwork; the hanging of cable \#1; the installation of the hanging basket; the guide cable construction before the cable-stayed basket; the pouring of blocks $-\# 1 \sim-\# 13$ and \#1-\#13; the pouring of blocks $-\# 14,-\# 15$ and $\# 14, \# 15$, and $\# 16$ on the bracket; drawing girders together; stretching the anchor bolts; and paving the bridge deck.

The construction of side piers involves the construction of the side pier pile foundation, bearing platform, and pier body, pouring of blocks $-\# 14,-\# 15, \# 14, \# 15$, and $\# 16$ by the bracket method, leaving 1.5 m at the end of block \#14 as the closure section, and casting the C at the closure section by hanging formworks on both sides. See Table 2 for specific data.

Table 2. Data summary table for construction.


# 4.5. Operation and Maintenance

According to the design codes for bridges and culverts in China (JTJ021-89, 024-85, $023-85,004-89$ ), the service life of a cable-stayed bridge is 100 years. To ensure the safety and normal use of the bridge during the design reference period, the maintenance department should carry out regular maintenance and repair. The maintenance cycle is shown in Table 3.

Table 3. Maintenance and repair data.


The existing carbonization models are basically divided into four categories: theoretical models [59], empirical models [60], semi-theoretical and semi-empirical models [61], and random models [62].

The theoretical model of carbonization depth can be simplified as:

$$
X=k \sqrt{t}
$$

where $X$ is the carbonization depth; $t$ is the carbonation reaction time; and $k$ is the carbonation coefficient (A comprehensive parameter reflecting the rate of carbonization).

The China promulgated GB/T51355-2019 in 2019 stipulates that the calculation formula of C carbonization coefficient is [63]:

$$
\mathrm{k}=3 \mathrm{~K}*{\mathrm{CO}*{2}} \mathrm{~K}*{\mathrm{k} 1} \mathrm{~K}*{\mathrm{kt}} \mathrm{~K}*{\mathrm{ks}} \mathrm{~K}*{\mathrm{F}} \mathrm{~T}^{0.25} \mathrm{RH}^{1.5}(1-\mathrm{RH})\left(\frac{58}{\mathrm{f}_{\mathrm{cu}, \mathrm{e}}}-0.76\right)
$$

where k is the carbonation coefficient of $\mathrm{C}(\mathrm{mm} / \sqrt{\mathrm{a}}) ; \mathrm{K}_{\mathrm{CO}_{2}}$ is the influence coefficient of $\mathrm{CO}_{2}$ concentration, which is set as $\sqrt{\mathrm{C}_{0} / 0.03}-\mathrm{CO}_{2}$ concentration; $\mathrm{C}_{\mathrm{CO}_{2}}$ is the $\mathrm{CO}_{2}$ concentration (\%); $\mathrm{K}_{\mathrm{k} 1}$ is the location influence coefficient (1.4 or 1.0); $\mathrm{K}_{\mathrm{kt}}$ is the C casting surface influence coefficient, and is set up $1.2 ; \mathrm{K}_{\mathrm{ks}}$ is the working stress influence coefficient, which is set as 1.0 in the compressive zone and as 1.1 in the tensile zone; T is the environmental temperature $\left({ }^{\circ} \mathrm{C}\right)$; RH is the environmental relative humidity; $\mathrm{K}_{\mathrm{F}}$ is the substitution coefficient of fly ash; and $\mathrm{f}_{\mathrm{cu}, \mathrm{e}}$ is the extrapolated value of C compression strength (MPa).

Yu et al. determined the model relationship of $\mathrm{CO}_{2}$ absorption capacity per unit volume of concrete [64].

$$
\mathrm{M}_{0}=(1-\alpha) \times 8.22 \mathrm{~B}
$$

where $\mathrm{M}_{0}$ is the $\mathrm{CO}_{2}$ absorption capacity of ordinary Portland cement $\left(\mathrm{mol} / \mathrm{m}^{3}\right) ; \mathrm{B}$ is the number of cementitious materials used per unit volume of $\mathrm{C}\left(\mathrm{kg} / \mathrm{m}^{3}\right)$; and $\alpha$ is the number of mixed materials in ordinary Portland cement (\%).

The C carbonization of SQ and EH is judged and analysed in accordance with (8), (9) and (10).

# 4.6. Disassembly and Recycling 

Each year, the global C industry generates more than 11 billion tonnes of waste, of which C waste accounts for about $50-70 \%$ [65]. According to a study by [66], the recycling rates of aggregates in Norway and China are 30 and $7 \%$, respectively. It is necessary to manage construction waste in a sustainable way [67,68]. In view of reducing the environmental pollution of construction waste and the value of China's waste recovery rate, combined with the urban location of the two bridges. The comprehensive analysis will be through mechanical and manual dismantling, and then sustainable recycling after 100 years of operation.

The demolition period of SQ and EH is 65 days and 75 days, respectively. There are 26 and 32 construction personnel, respectively. Demolition waste is transported to a steel plant $330 \mathrm{~km}(58 \mathrm{~km})$ away and a waste-to-energy plant $846 \mathrm{~km}(52 \mathrm{~km})$ away.

## 5. Discussion

The five phases of the bridge will produce environmental pollution, and improving sustainable development is the best choice to reduce pollution [69-71] (Intergovernmental Panel on Climate Change).

Table 4 shows the framework and modelling formulas of the contributions of the five phases of a cable-stayed bridge to environmental emissions. The contribution to environmental emissions of secondary use is mainly caused by the steel recycling and refining. After the bridge is dismantled by the mechanical crusher, the loaders will be used for on-site sorting and loading. This increases the steel recycling rate to $90 \%$ [72] and the C scrap recycling rate to $55 \%$ [73]. The remaining construction wastes are transported to garbage power plants and landfills for disposal. There is no garbage power plant in the surrounding area of SQ, and all the remaining construction wastes are transported to landfill for disposal.

### 5.1. Case Environmental Impact

### 5.1.1. BNFC Comprehensive Assessment

According to the results of the LCA study, the total environmental emissions contributions of SQ and EH are 147,446.95 and 135,311.42 tonnes, respectively, as shown in Table 5. Among the five contribution values, the GWPs of SQ and EH account for $95.67 \%$ and $95.47 \%$, respectively.

Table 4. Summary table of five-stage modelling formulas [11].


CI-construction and installation; DR-disassembly and recycling; E-equipment; EC-environmental impact contribution; MM-material manufacturing; MO-maintenance and operation; OF-office facilities; PGGDS-garbage generation and sewage discharge by personnel; SD-survey and design; TV-transport vehicle (this code only applies to Table 4).

Table 5. Summary table of bridge environmental impact contributions (Table 4 formula calculation).


Note (Table 5): The percentage value $(\%)=$ transportation contribution ( kg )/total value of environmental contribution at each stage $(\mathrm{kg}) \cdot \sum \mathrm{EC}_{\mathrm{SQ}}=\sum \mathrm{EC}_{\mathrm{GWP}}+\sum \mathrm{EC}_{\mathrm{AP}}+\sum \mathrm{EC}_{\mathrm{FEP}}+\sum \mathrm{EC}_{\mathrm{PMFP}}+\sum \mathrm{EC}_{\mathrm{WP}}=1474,46.95$ tonnes; $\sum \mathrm{EC}_{\mathrm{EH}}=135,311.42$ tonnes.

GWP, AP, FEP, PMFD, and WP were selected as assessment factors to build the grading system for each phase. According to the theory presented in Section 3.3.

$$
\mathrm{U}=\left\{\mathrm{GWP}, \mathrm{AP}, \mathrm{FEP}, \mathrm{PMFD}, \mathrm{WP}\right\},=\left\{\mathrm{v}_{1}, \mathrm{v}_{2}, \mathrm{v}_{3}, \mathrm{v}_{4}, \mathrm{v}_{5}\right\}
$$

where $v_{1}$ is the survey and design stage; $v_{2}$ is the material manufacturing stage; $v_{3}$ is the construction and installation stage; $v_{4}$ is the maintenance and operation stage; and $v_{5}$ is the disassembly and recycling stage.

The fuzzy matrix was established as follows according to Table 6 and Equation (5):

$$
\begin{aligned}
& \mathrm{R}_{\mathrm{SQ}}=\left[\begin{array}{cccccc}
0.23 & 25.37 & 15.31 & 56.12 & 2.97 \\
0.00 & 68.41 & 0.07 & 31.52 & 0.01 \\
0.19 & 28.86 & 2.97 & 67.95 & 0.03 \\
0.00 & 59.34 & 0.07 & 40.58 & 0.00 \\
0.17 & 51.75 & 0.08 & 48.17 & 0.00
\end{array}\right], \\
& \mathrm{R}_{\mathrm{EH}}=\left[\begin{array}{cccccc}
0.47 & 25.24 & 18.54 & 53.88 & 1.87 \\
0.00 & 55.50 & 0.06 & 44.43 & 0.00 \\
0.40 & 27.94 & 4.25 & 67.36 & 0.05 \\
0.00 & 51.75 & 0.08 & 48.17 & 0.00 \\
0.34 & 53.61 & 3.62 & 42.38 & 0.04
\end{array}\right]
\end{aligned}
$$

and $\mathrm{K}_{\mathrm{JSQ}}$ and $\mathrm{K}_{\mathrm{IEH}}$ were determined according to Equations (6) and (7), as shown in Table 7.

Table 6. Summary table of membership data of two cable-stayed bridge classification systems.


Table 7. Summary table of assessment factor weight data for two cable-stayed bridges.


Note: $\mathrm{V}_{\mathrm{i}}$ is the average value of five types of environmental influences, $\mathrm{K}*{\mathrm{j}}=\mathrm{a}*{\mathrm{i}} / \mathrm{V}*{\mathrm{i}}, \mathrm{K}*{\mathrm{j}}^{\prime}=\mathrm{K}_{\mathrm{j}} / \sum \mathrm{K}_{\mathrm{j}}$.
The assessment result can be obtained as follows by the compound operation $\mathrm{E}(\Lambda, \mathrm{V})=\mathrm{K}_{\mathrm{j}}^{\prime} \mathrm{R}_{\mathrm{SQ}}:$

$$
\begin{aligned}
& \mathrm{E}_{\mathrm{SQ}}=(0.95670 .00340 .00510 .01170 .0230) \times\left[\begin{array}{ccccc}
0.23 & 25.37 & 15.31 & 56.12 & 2.97 \\
0.00 & 68.41 & 0.07 & 31.52 & 0.01 \\
0.19 & 28.86 & 2.97 & 67.95 & 0.03 \\
0.00 & 59.34 & 0.07 & 40.58 & 0.00 \\
0.17 & 51.75 & 0.08 & 48.17 & 0.00
\end{array}\right] \\
& =(0.224926 .535815 .085155 .72642 .8416)
\end{aligned}
$$

$$
\begin{aligned}
& \left(\mathrm{E}_{\mathrm{EH}}\right)=(0.95470 .00400 .00510 .01310 .0231) \times\left[\begin{array}{ccccc}
0.47 & 25.24 & 18.54 & 53.88 & 1.87 \\
0.00 & 55.50 & 0.06 & 44.43 & 0.00 \\
0.40 & 27.94 & 4.25 & 67.36 & 0.05 \\
0.00 & 51.75 & 0.08 & 48.17 & 0.00 \\
0.34 & 53.61 & 3.62 & 42.38 & 0.04
\end{array}\right] \\
& =(0.458626 .456017 .806753 .57051 .7865)
\end{aligned}
$$

# 5.1.2. Comparative Analysis of the Results of Fuzzy Comprehensive Assessment of LCA and Bayesian 

According to the conclusion of the assessment in Section 5.1.1 and the results of software analysis shown in Figure 7, the contributions to environmental emissions of SQ according to the software analysis can be ranked from high to low as follows: operation and maintenance ( $55.57 \%$ ) > material manufacturing ( $26.64 \%$ ) > construction and installation ( $14.73 \%$ ) > disassembly and recycling ( $2.84 \%$ ) > survey and design ( $0.22 \%$ ), and SQ's contributions according to the BNFC can be ranked from high to low as follows: maintenance and operation ( $55.73 \%$ ) > material manufacturing ( $26.54 \%$ ) > construction and installation $(15.09 \%)>$ disassembly and recycling $(2.84 \%)>$ survey and design $(0.23 \%)$.

![img-7.jpeg](img-7.jpeg)

**Figure 7.** Comparison diagram of research and analysis conclusions of SQ's contribution to the environment.

As shown in Figure 8, the contribution to environmental emissions of EH according to the software analysis can be ranked from high to low as follows: maintenance and operation (53.57%) > material manufacturing (26.38%) > construction and installation (17.81%) > disassembly and recycling (1.78%) > survey and design (0.46%), and EH's contribution according to the BNFC can be ranked from high to low as follows: maintenance and operation (53.57%) > material manufacturing (26.46%) > construction and installation (17.81%) > disassembly and recycling (1.70%) > survey and design (0.46%).

![img-8.jpeg](img-8.jpeg)

**Figure 8.** Comparison diagram of research and analysis conclusions of EH environmental impact contribution.

Figure 9 shows that the conclusions obtained by the application software are basically consistent with those obtained by BNFC. For the maintenance and operation phase and the construction and installation phase of SQ, the differences between the results of the two approaches are $55.57 \%-55.73 \%=-0.16 \%$ and $14.73 \%-15.09 \%=-0.36 \%$. For the material manufacturing phase and the disassembly and recycling phase of EH, the differences between the results of the two research conclusions are $26.38 \%-26.46 \%=-0.08 \%$, and $1.78 \%-1.70 \%=-0.08 \%$. Other data are basically the same. Therefore, it is determined that the conclusions for SQ and EH obtained by the two research methods are both accurate.
![img-9.jpeg](img-9.jpeg)

Figure 9. Comparison of the conclusions of using two methods to study the environmental impact contribution of SQ and EH .

We applied the Matlab scientific computing programming method to the above conclusions to calculate the conclusion fitting (shown in Figure 10). The research image and the fitted data show that there is no discrete type of data between the software analysis results and the BNFC analysis conclusions, and the data are completely symmetric and matched. The fitted quadratic curve is $\mathrm{Y}=3 \mathrm{E}-0.6 \mathrm{x}^{2}+1.0026 \mathrm{x}+0.2577$, and the linearity tends to a straight line, indicating that the two research methods are very consistent.

# 5.1.3. Impact Factor Calibration for SQ and EH 

The impact factors of SQ and EH are obtained after the analysis by means of the BNFC analytic hierarchy process. Table 5 shows the results of the LCA analysis, and Section 5.1.1

shows the conclusion of the BNFC comprehensive assessment. The impact factor weight obtained by the above three research processes is analyzed as follows:

$$
\begin{aligned}
& \mathrm{E}_{\text {summary }}= \\
& \text { Bayesian networks analytical hierarchy process hypothesis } \quad \mathrm{E}_{\mathrm{SQ}, \mathrm{EH}} \\
& (1.00,1.02,1.10,1.45,1.01) \\
& \text { LCA software analysis conclusion } \\
& \text { (0.22, 26.64, 14.73, 55.57, 2.84) } \\
& \text { LCA software analysis conclusion } \\
& \text { (0.46, 26.38, 17.81, 53.57, 1.78) } \\
& \text { Bayesian fuzzy mathematics comprehensive evaluation } \\
& \text { (0.23, 26.54, 15.09, 55.73, 2.84) } \\
& \text { Bayesian fuzzy mathematics comprehensive evaluation } \\
& \text { (0.46, 26.46, 17.81, 53.57, 1.79) }
\end{aligned}
$$

![img-10.jpeg](img-10.jpeg)

Figure 10. The matching degree of the contribution of SQ and EH to the environmental impact is fit to the numerical curve.
To facilitate comparative analysis, Equations (2)-(4) and (5) are transformed, and the following equations are obtained:

$$
E_{\text {summary }}=\left\{\begin{array}{c}
E_{S Q, E H}=(1.00,1.02,1.10,1.45,1.01) \\
E_{S Q}=(0.01,1.81,1.00,3.77,0.19) \\
E_{E H}=(0.03,1.48,1.00,3.01,0.10) \\
E_{S Q}=(0.02,1.76,1.00,3.69,0.19) \\
E_{E H}=(0.03,1.55,1.00,3.13,0.11)
\end{array}\right.
$$

Figure 11 shows a schematic diagram of the impact factors of the three assessment methods. The factor size relationship of the five phases is in accordance with the conclusion of the LCA and BNFC analysis, and the results deduced in Section 3.5.3 are supported.
![img-11.jpeg](img-11.jpeg)

Figure 11. The influencing factors obtained by the three evaluation methods are compared and fitted with the analysis of mean difference.

Figure 12 shows the deviation analysis of the impact factors for SQ and EH. The maintenance and operation phase are still the largest contributor to environmental emissions. According to the rating system in Section 3.2, the survey and design phase and the disassembly and recycling phase are rated as "slight effect", and the material manufacturing phase and the construction and installation phase are rated as "moderate effect", requiring attention. The maintenance operation phase is rated as "great effect", which means that it leads to serious environmental pollution and requires special attention. The research data show that in the maintenance and operation phase, the environmental pollution of raw materials is ranked first, and the environmental pollution of transportation vehicles is second, accounting for $28.12 \%$ of the total emissions from the SQ bridge and $26.28 \%$ of the total emissions from the EH bridge. The environmental pollution of materials in the maintenance phase cannot be reduced, and the amount of environmental pollution caused by transportation can only be reduced through evaluation and design. Assessment and innovation research are conducted in the following sections.

Figure 13 shows that in the maintenance and operation stage, the environmental impact value is larger for the replacement of the main beam (point 2) and the garbage pollution generated by the maintenance personnel (point 12). After the MATLAB scientific algorithm is fitted, the fitting equation is reached:

Fitting algorithm program:
$>>\% S Q: z=(4.213 e+05) .{ }^{*} x^{\wedge} 2-(5.383 e+06) .{ }^{*} x+(1.744 e+07)$.
$>>\% \mathrm{EH}: \mathrm{z}=(3.727 \mathrm{e}+05) .{ }^{*} \mathrm{x} .{ }^{\wedge} 2-(4.998 \mathrm{e}+06) .{ }^{*} \mathrm{x}+(1.708 \mathrm{e}+07)$.
$>>$ clear all; \% Curve equation fitting, The first set of calculation programming language; $>>x=[12345678910111213]$

$>>y=[3175070.13326344975.58621212 .38714122 .768341378 .030917963 .4565 .164350566$ 20075.328 1057111.7762554272581782539517468.412755301.595];
$>>$ figure;
$>>\operatorname{plot}\left(x, y,{ }^{\prime} b o^{\prime}\right)$;
Interpolation analysis program:
>>Clear all/\% The second set of calculation programming language;
$>>x=1: 13$
$>>y=5: 3175070$
$>>[x, y]=$ meshgrid $(x, y)$;
$>>z=(4.213 e+05) . * x .^{\prime} 2-(5.383 e+06) .{ }^{*} x+(1.744 e+07)$;
$>>$ figure;
$>>\operatorname{surf}(x, y, z)$;
$>>$ view $([50,70])$;
$>>$ colormap('jet');
>>shading interp;
>>light('position',[0.2 0.2 0.8]);
>>axis square;
>>xlabel('x');
>>label('y');
>>zlabel('z');
![img-12.jpeg](img-12.jpeg)

Figure 12. Chart of impact factor deviation analysis for SQ and EH.
According to the fitted equation, the environmental impact change trend of SQ and EH during the 100-year maintenance period is calculated, which is divided into three stages. (1) The environmental impact value of materials, personnel, and equipment during the maintenance period is stable in a fixed area, indicated by (1)(4). (2) With the development of maintenance work, the originally installed equipment is in stable operation, without many equipment replacements (for example: main beams, main tower cables). Small materials are replaced (for example: guardrails, waterproof coating). The overall environmental impact contribution shows a downward trend, indicated by (2)(5). (3) With the replacement of large-scale equipment (such as main beams, main tower cables), the environmental

impact value continues to increase, and the increasing trend is higher than the previous downward trend until the end of the 100-year operation period, as indicated by (3)(6). (4) Comparing SQ and EH, it can be found that the environmental impact change trend of EH during the maintenance period is higher than that of SQ.
![img-13.jpeg](img-13.jpeg)

Figure 13. SQ and EH maintenance and operation stage environmental impact fitting and future change trend interpolation analysis.

# 5.2. Innovation 

### 5.2.1. Modelling Analysis

As the Internet and mobile communication technologies have advanced rapidly in the twenty-first century, reasonable use of big data to solve material procurement is of great significance. Cai et al. proposed an "Omni-Channel Management" framework and implemented omni-channel management [74]. As shown in Figure 5, the third level of the environmental emissions contribution of cable-stayed bridges can be divided into eight categories and 31 types. The impact factor is considered the variable node $x$, and the directed edges between nodes represent the interrelationships between nodes; $x$ corresponds

to the probability distribution $\mathrm{P}(\mathrm{x}) \mid \pi(\mathrm{x}))$. The joint probability distribution for n nodes $\left(x_{1}, x_{2}, \cdots \cdots, x_{n}\right)$ can be expressed as:

$$
\mathrm{P}\left(\mathrm{x}_{1}, \mathrm{x}_{2}, \cdots \cdots \mathrm{x}_{\mathrm{n}}\right)=\prod_{\mathrm{i}=1}^{\mathrm{n}} \mathrm{P}\left(\mathrm{x}_{\mathrm{i}} \mid \pi\left(\mathrm{x}_{\mathrm{i}}\right)\right)
$$

The significance of each random variable's impact on the environmental emission contribution can be expressed by the sensitivity. $\mathrm{P}\left(\mathrm{x}_{1}\right)$ and $\mathrm{P}\left(\mathrm{x}_{\mathrm{n}}\right)$ represent the probability distribution of $x_{1}$ and $x_{n} ; T\left(x_{1}, x_{n}\right)$ represents the direct influence on the relationship between $x_{1}$ and $x_{n}$ :

$$
\mathrm{T}\left(\mathrm{x}_{1}, \mathrm{x}_{\mathrm{n}}\right)=\sum_{\mathrm{x}_{1}, \mathrm{x}_{\mathrm{n}}}\left(\mathrm{x}_{1}, \mathrm{x}_{\mathrm{n}}\right)=\log \frac{\mathrm{P}\left(\mathrm{x}_{1}, \mathrm{x}_{\mathrm{n}}\right)}{\mathrm{P}\left(\mathrm{x}_{1}\right) \mathrm{P}\left(\mathrm{x}_{\mathrm{n}}\right)}
$$

Figure 14 introduces big data omni-channel assessment analysis to solve the serious traffic pollution problem of SQ and EH. The big data system analysis is used to select the best suppliers, assess the supply lines, and reduce the impact factors shown in Equation (11). Figure 15 shows that SQ's environmental impact factors are concentrated in the physicochemical energy of materials ( 43959.26 tonnes), garbage and sewage ( 43898.84 tonnes), and vehicles ( 41866.31 tonnes), accounting for $87.97 \%$ of the total. EH's environmental impact factors are concentrated in physicochemical energy of materials ( 78944.70 tonnes) and garbage and sewage ( 35901.30 tonnes), accounting for $84.87 \%$ of the total.
![img-14.jpeg](img-14.jpeg)

Figure 14. Schematic diagram of big data omnichannel assessment framework.
The symbols 1-8 in Figure 15 represent content: $1=$ Construction equipment diesel contribution; $2=$ Construction equipment electrical contribution; $3=$ Human contribution and energy consumption; $4=$ Transportation vehicle contribution; $5=$ Contribution of garbage and sewage; $6=$ Physical and chemical energy of various materials; $7=$ Concrete carbonization; $8=$ External environmental impact.

The following can be deduced from Equation (12):
$\mathrm{P}_{\mathrm{SQ}}\left(\mathrm{x}_{1}, \cdots \cdots \mathrm{x}_{\mathrm{n}}\right)=\left(1.24 \%, 1.20 \%, 4.86 \%, 28.39 \%, 29.77 \%, 29.81 \%, 2.99 \%, 1.73 \%\right)$ and $\mathrm{P}_{\mathrm{EH}}\left(\mathrm{x}_{1}, \cdots \cdots \mathrm{x}_{\mathrm{n}}\right)=\left(1.67 \%, 1.72 \%, 4.93 \%, 1.62 \%, 26.53 \%, 58.34 \%, 3.02 \%, 2.16 \%\right)$.

The following can be deduced from Equation (12):

$$
\mathrm{T}_{\mathrm{SQ}}\left(\mathrm{x}_{1}, \mathrm{x}_{8}\right)=\left\{\begin{array}{cc}
\mathrm{P}_{\mathrm{xn}} & \log \mathrm{P}_{\mathrm{xn}} \quad \log \mathrm{P}_{\mathrm{xn}}+\log \mathrm{P}_{\mathrm{xn}+1} \quad \log \mathrm{P}_{\mathrm{xn}} \times \log \mathrm{P}_{\mathrm{xn}+1} & \mathrm{~T}_{\mathrm{SQ}} \\
1.24 & 0.0934 & 0.0934 & 0 & 0 \\
1.20 & 0.0792 & 0.1726 & 0.00740 & 23.324 \\
4.86 & 0.6866 & 0.7658 & 0.05438 & 14.082 \\
28.39 & 1.4532 & 2.1398 & 0.99777 & 2.145 \\
29.77 & 1.4738 & 2.9270 & 2.14173 & 1.367 \\
29.81 & 1.4743 & 2.9481 & 2.17282 & 1.357 \\
2.99 & 0.4757 & 1.9500 & 0.70132 & 2.781 \\
1.73 & 0.2381 & 0.7138 & 0.11326 & 6.302
\end{array}\right\}
$$

$$
\mathrm{T}_{\mathrm{EH}}\left(\mathrm{x}_{1}, \mathrm{x}_{8}\right)=\left\{\begin{array}{cc}
\mathrm{P}_{\mathrm{xn}} & \log \mathrm{P}_{\mathrm{xn}} \quad \log \mathrm{P}_{\mathrm{xn}}+\log \mathrm{P}_{\mathrm{xn}+1} \quad \log \mathrm{P}_{\mathrm{xn}} \times \log \mathrm{P}_{\mathrm{xn}+1} & \mathrm{~T}_{\mathrm{SQ}} \\
1.67 & 0.2227 & 0.2227 & 0 & 0 \\
1.72 & 0.2355 & 0.4582 & 0.05245 & 8.736 \\
4.93 & 0.6929 & 0.9284 & 0.16318 & 5.689 \\
1.62 & 0.2095 & 0.9024 & 0.14516 & 6.217 \\
26.53 & 1.4237 & 2.3261 & 0.29827 & 7.799 \\
58.34 & 1.7660 & 3.1897 & 2.51425 & 1.269 \\
3.02 & 0.4800 & 2.2460 & 0.84768 & 2.650 \\
2.16 & 0.3345 & 0.8145 & 0.16056 & 5.073
\end{array}\right\}
$$

According to the calculation result, the sensitivities of the eight categories of impact factors to environmental emission contributions can be ranked as follows:

$$
\begin{aligned}
& \mathrm{T}_{\mathrm{SQ}}\left(\mathrm{x}_{1}, \mathrm{x}_{8}\right)= \\
& \left\{\begin{array}{cc}
\mathrm{P}_{\mathrm{xn}} & \log \mathrm{P}_{\mathrm{xn}} \quad \log \mathrm{P}_{\mathrm{xn}}+\log \mathrm{P}_{\mathrm{xn}+1} \quad \log \mathrm{P}_{\mathrm{xn}} \times \log \mathrm{P}_{\mathrm{xn}+1} & \mathrm{~T}_{\mathrm{SQ}} \\
1.24 & 0.0934 & 0.0934 & 0 & 0 \\
1.20 & 0.0792 & 0.1726 & 0.00740 & 23.324 \\
4.86 & 0.6866 & 0.7658 & 0.05438 & 14.082 \\
28.39 & 1.4532 & 2.1398 & 0.99777 & 2.145 \\
29.77 & 1.4738 & 2.9270 & 2.14173 & 1.367 \\
29.81 & 1.4743 & 2.9481 & 2.17282 & 1.357 \\
2.99 & 0.4757 & 1.9500 & 0.70132 & 2.781 \\
1.73 & 0.2381 & 0.7138 & 0.11326 & 6.302
\end{array}\right. \\
& \mathrm{T}_{\mathrm{EH}}\left(\mathrm{x}_{1}, \mathrm{x}_{8}\right)= \\
& \left\{\begin{array}{cc}
\mathrm{P}_{\mathrm{xn}} & \log \mathrm{P}_{\mathrm{xn}} \quad \log \mathrm{P}_{\mathrm{xn}}+\log \mathrm{P}_{\mathrm{xn}+1} \quad \log \mathrm{P}_{\mathrm{xn}} \times \log \mathrm{P}_{\mathrm{xn}+1} & \mathrm{~T}_{\mathrm{SQ}} \\
1.67 & 0.2227 & 0.2227 & 0 & 0 \\
1.72 & 0.2355 & 0.4582 & 0.05245 & 8.736 \\
4.93 & 0.6929 & 0.9284 & 0.16318 & 5.689 \\
1.62 & 0.2095 & 0.9024 & 0.14516 & 6.217 \\
26.53 & 1.4237 & 2.3261 & 0.29827 & 7.799 \\
58.34 & 1.7660 & 3.1897 & 2.51425 & 1.269 \\
3.02 & 0.4800 & 2.2460 & 0.84768 & 2.650 \\
2.16 & 0.3345 & 0.8145 & 0.16056 & 5.073
\end{array}\right\} .
\end{aligned}
$$

$\mathrm{T}_{\mathrm{SQ}}\left(\mathrm{x}_{1}, \mathrm{x}_{8}\right)=(23.324>14.082>6.302>2.781>2.145>1.367>1.357)$, and
$\mathrm{T}_{\mathrm{EH}}\left(\mathrm{x}_{1}, \mathrm{x}_{8}\right)=(8.736>7.799>6.217>5.689>5.073>2.650>1.269)$.
The conclusion of the sensitivity analysis is consistent with the research conclusion in Section 5.1. Sensitivity analysis ranking shows that the smaller the sensitivity calculation value, the greater the number of pollution emission of the impact factor. This is consistent with the $\mathrm{E}_{\mathrm{SQ}}$ and $\mathrm{E}_{\mathrm{EH}}$ ranking. The minimum value of $\mathrm{T}_{\mathrm{SQ}} 1.357$ and the minimum value of $\mathrm{T}_{\mathrm{EH}} 1.269$ are the environmental pollution emissions of raw materials consumed in the maintenance and operation phases.

![img-15.jpeg](img-15.jpeg)

Figure 15. A schematic diagram of the numerical comparison of the environmental impact contribution types of SQ and EH.

# 5.2.2. Measures 

SQ and EH require the following measures. (1) Designing and choosing energy-saving and environmentally friendly materials and reducing cement consumption. (2) Disposing of waste materials in strict accordance with construction regulations [68]. (3) Regular special garbage cleaning. (4) Strictly controlling the random discharge of garbage by construction workers.

The amounts of waste materials and wastewater generated by SQ are 527.51 tonnes and $749.27 \mathrm{~m}^{3}$; the amounts of waste materials and wastewater generated by EH are 488.38 tonnes and $693.70 \mathrm{~m}^{3}$. There is a need to install digital automatic control processing equipment for centralized recycling in the mixing plant [75-77].

### 5.3. Transportation

The transportation emission analysis of the cable-stayed bridge is calculated according to the 100-year life span of the drawing design (2011-2110). Zhou et al. determined the equivalent environmental impact indicators for fuel-powered vehicles and BEVs [78-82]. The research results show that the GWP emissions of new energy automobiles in the driving phase are between 197.17 and $284.72 \mathrm{~g} / \mathrm{km}$.

The upper limit of vehicle saturation in China is 807 vehicles/1000 people, and it will reach 390 million vehicles in 2030, which is 269 vehicles/1000 people [83]. From 2030 to 2050, the growth rate will be $2.9 \%$, reaching 455 vehicles/1000 people [84]. Joyce Dargah et al., Tian Wu et al., and Zhou et al. established a theoretical model to measure vehicles.

### 5.3.1. Modelling in Operation and Maintenance Phase

The calculation model of the membership function can be built as follows, based on Equations (11) and (12)

$$
\begin{gathered}
\mathrm{E}_{\mathrm{SQ}}= \\
\left\{\begin{array}{l}
\mathrm{M}_{\mathrm{pc}} \times\left(1 \pm \gamma_{1}\right) \times \lambda_{1}+\mathrm{M}_{\mathrm{cv}} \times\left(1 \pm \gamma_{2}\right) \times \lambda_{2}+\mathrm{M}_{\mathrm{nev}} \times\left(1 \pm \gamma_{3}\right) \times \lambda_{3} \quad 2011 \leq \mathrm{T}_{\mathrm{m}} \leq 2020 \text { year } \\
\mathrm{M}_{\mathrm{pc}} \times\left(1 \pm \gamma_{0}\right) \times \lambda_{1}+\mathrm{M}_{\mathrm{cv}} \times\left(1 \pm \gamma_{0}\right) \times \lambda_{2}+\mathrm{M}_{\mathrm{nev}} \times\left(1 \pm \gamma_{0}\right) \times \lambda_{3} \quad 2021 \leq \mathrm{T}_{\mathrm{m}} \leq 2110 \text { year }
\end{array}\right.
\end{gathered}
$$

where $\mathrm{E}_{\mathrm{SQ}}$ is the contribution of transportation on SQ to environmental emissions in the maintenance and operation phase $(\mathrm{kg}) ; \mathrm{M}_{\mathrm{pc}}, \mathrm{M}_{\mathrm{cv}}$, and $\mathrm{M}_{\mathrm{nev}}$ are the traffic volumes of different types of vehicles (per vehicle/year $/ \mathrm{km}$ ); $\lambda_{1}, \lambda_{2}$, and $\lambda_{3}$ are the environmental impact emissions indexes of different types of vehicles $(\mathrm{g} / \mathrm{km}) ; \gamma_{1}, \gamma_{2}$ and $\gamma_{3}$ are the growth

and reduction rates of different types of vehicles per year (\%); and $\gamma_{0}$ is the fixed growth and reduction rate of different types of vehicles per year (\%).

$$
\begin{gathered}
\mathrm{E}_{\mathrm{EH}}= \\
\left\{\begin{array}{c}
\mathrm{M}_{\mathrm{pc}} \times \lambda_{1}+\mathrm{M}_{\mathrm{cv}} \times \lambda_{2} \quad 2002 \leq \mathrm{T}_{\mathrm{m}} \leq 2011 \text { year } \\
\mathrm{M}_{\mathrm{pc}} \times\left(1 \pm \gamma_{1}\right) \times \lambda_{1}+\mathrm{M}_{\mathrm{cv}} \times\left(1 \pm \gamma_{2}\right) \times \lambda_{2}+\mathrm{M}_{\mathrm{nev}} \times\left(1 \pm \gamma_{3}\right) \times \lambda_{3} \quad 2012 \leq \mathrm{T}_{\mathrm{m}} \leq 2020 \text { year } \\
\mathrm{M}_{\mathrm{pc}} \times\left(1 \pm \gamma_{0}\right) \times \lambda_{1}+\mathrm{M}_{\mathrm{cv}} \times\left(1 \pm \gamma_{0}\right) \times \lambda_{2}+\mathrm{M}_{\mathrm{nev}} \times\left(1 \pm \gamma_{0}\right) \times \lambda_{3} \quad 2021 \leq \mathrm{T}_{\mathrm{m}} \leq 2102 \text { year }
\end{array}\right.
\end{gathered}
$$

where $\mathrm{E}_{\mathrm{EH}}$ is the contribution of transportation on EH to environmental emissions in the maintenance and operation phase $(\mathrm{kg})$.

Formula (13) shows the total sales volume and growth rate of the three types of automobiles in China from 2008 to 2019 [85], based on the latest development plan for the new energy automobile industry issued by the State Council of China (2021-2035) to model (13) and (14) analyse the vehicle traffic on cable-stayed bridges.

# 5.3.2. Calculations in the Operation and Maintenance Phase 

Table 8 shows the assessment vehicle data in the maintenance and operation phase, which are obtained using Equations (13) and (14) and [78-83]. The operating periods of SQ and EH are 2011-2110 and 2002-2102, respectively.

Table 8. Summary table of assessment vehicle data analysis for SQ and EH.


Figure 16 shows the assessment of transportation pollution by vehicle type. Newenergy automobiles have disadvantages such as being limited to short distances, limited installation of supporting power supply facilities, and short battery life, so they are still in the stage of promotion in China and have a low market share. HEVs have overcome some of the defects of electric vehicles, but the conclusions obtained from the assessment analysis data are not obvious. At present, research and analysis concerning improving fuel quality standards and controlling exhaust emissions after combustion is an effective solution.

As shown in Figure 17, the highest contribution to environmental emissions in the five phases of SQ is 1985.01 tonnes and is made in the disassembly and recycling stage. The reason for this is that SQ is far from the steel plant ( 330 km ) and the waste power plant ( 846 km ), resulting in high exhaust emissions. The reason for not choosing to dispose of wastes in the nearby waste treatment plant is to consider the reduction in secondary pollution, material regeneration, and secondary utilization. The highest exhaust emissions of EH total 1345.78 tonnes. After the modelling assessment and analysis of the transportation pollution of the two bridges, the pollution emissions decrease by 72.09 and 258.55 tonnes, respectively.

![img-16.jpeg](img-16.jpeg)

Figure 16. A Summary table of vehicle assessment data during operation and maintenance for SQ and EH.
(a) The five-stage sequence number of bridge environmental contribution for SQ and EH
![img-17.jpeg](img-17.jpeg)

Figure 17. Cont.

![img-18.jpeg](img-18.jpeg)

Figure 17. Five-stage contribution of transportation vehicles and operation and maintenance vehicle assessment chart for SQ and EH.

# 6. Conclusions 

In the face of the serious pollution caused by the global construction industry, researchers from all over the world are working hard to find the research framework and methods to improve the LCA of bridges, to better reduce the environmental pollution and energy consumption of bridge engineering. At the same time, many uncertain factors have appeared in the research process.

In this work, the FMT and BN theoretical model is established to solve the interference problem of uncertainty factors in LCA. Combined with the five research theories of Monte Carlo simulation, geometric mean and geometric standard deviation set by OpenLCA software, the uncertainty in LCA research is well-handled. The model is checked and analyzed with case data and evaluated comprehensively. It is found that the research conclusions are surprisingly consistent, which verifies the accuracy and practicability of the theoretical model again.

The results show that the contribution of SQ and EH to the environment in the two stages of material manufacturing and maintenance and operation accounted for $26.64 \%$ and $26.38 \%$ and $55.57 \%$ and $53.57 \%$ of the total emissions, respectively. At the same time, the two stages of software analysis data were evaluated by BNFC. The results of SQ and EH maintenance stage model evaluation was $55.73 \%$ and $53.57 \%$. The conclusion of theoretical model evaluation is almost consistent with that of software analysis.

Through the matching degree check and the comprehensive influence weight matrix verification of influence factors, it is found that the influence factors obtained by means of the three different research methods of the analytical hierarchy process based on BNFC, comprehensive evaluation of the BNFC and LCA software is very consistent with the factors assumed by fuzzy mathematics calculation, which proves the accuracy of 3.4.3 modelling.

Finally, the sensitivity analysis of the environmental severity in the maintenance and operation phase is carried out. It was found that the pollutants mainly concentrated in the physical and chemical energy of materials, garbage and sewage, and vehicles, accounting for $87.14 \%$ and $85.66 \%$ of the total emissions of SQ and EH. Through the optimization

modelling again, the SQ emission is reduced by 72.09 tonnes, and the EH emission is reduced by 258.55 tonnes.

Theoretical research in basic science is the stepping-stone of applied science, and the solid FMT paves the way for solving the complex dynamic uncertainty. The results of this study prove that in the process of achieving the sustainable development goals of the construction industry, due to the complexity and uncertainty of the research objects and other factors, it is limited and unstable to rely solely on databases and software for analysis. It is aimed at new materials, new construction machinery, and new construction techniques. The key is to apply scientific methods to prove the accuracy and robustness of research conclusions through each layer of verification and proofreading steps in the theoretical framework model. The Bayesian network fuzzy number comprehensive evaluation model breaks through the constraints of software and database and achieves the purpose of research. Contributed to a more scientific realization of the sustainable development goals. The research results of this work can be used as ideas and methods to solve LCA research in other industries, and more research results are expected to verify them, in order to make better use of interdisciplinary theory to deal with the difficulties in the research. The limitation of this study is that there is no further research, analysis, and optimization of the other four stages in order to better reduce environmental pollution. In the future, we need to increase the research on the combination of fuzzy mathematics and topology optimization, to better contribute to reducing the environmental pollution of the construction industry.

Author Contributions: Investigation, Z.-W.Z. and J.A.; methodology, Z.-W.Z., J.A., and V.Y.; supervision, J.A, M.K. and V.Y.; validation, Z.-W.Z. and M.K.; writing-original draft, Z.-W.Z.; writingreview and editing, J.A, M.K. and V.Y. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Spanish Ministry of Economy and Competitiveness, along with FEDER (Fondo Europeo de Desarrollo Regional), project grant number: BIA2017-85098-R.

Acknowledgments: The authors would like to thank the editor of the applied sciences and the anonymous reviewers for contributing to improve the earlier version of this manuscript.

Conflicts of Interest: The authors declare no potential conflict of interest with respect to the research, authorship, and/or publication of this article.

# Nomenclature 

BN Bayesian networks
LCA Life cycle assessment
FMT Fuzzy mathematics theory
BNFC Bayesian network fuzzy number comprehensive evaluation
GWP Global warming parameters
AP Acidification parameters
FEP Freshwater eutrophication parameters
PMFP Particulate matter formation parameters
WP Solid waste parameters
SQ Su Qian bridge
EH Gong He cable-stayed bridge
C Concrete
Km Kilometers
kwh Kilowatt-hour
