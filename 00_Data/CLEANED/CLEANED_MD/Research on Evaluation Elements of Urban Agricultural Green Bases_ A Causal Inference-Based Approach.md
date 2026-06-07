# Article 

## Research on Evaluation Elements of Urban Agricultural Green Bases: A Causal Inference-Based Approach

Yuchong Long ${ }^{1, \dagger} \odot$, Zhengwei Cao ${ }^{1, *}, \bullet \odot$, Yan Mao ${ }^{2, \dagger} \odot$, Xinran Liu ${ }^{1}$, Yan Gao ${ }^{1}$, Chuanzhi Zhou ${ }^{1}$ and Xin Zheng ${ }^{1}$


#### Abstract

check for updates Citation: Long, Y.; Cao, Z.; Mao, Y.; Liu, X.; Gao, Y.; Zhou, C.; Zheng, X. Research on Evaluation Elements of Urban Agricultural Green Bases: A Causal Inference-Based Approach. Land 2023, 12, 1636. https://doi.org/ 10.3390/land12081636


Academic Editor: Eusebio Cano
Carmona
Received: 6 July 2023
Revised: 12 August 2023
Accepted: 18 August 2023
Published: 20 August 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Agriculture and Biology, Shanghai Jiao Tong University, Dongchuan Street, Minhang District, Shanghai 200240, China; ayinmostima@sjtu.edu.cn (Y.L.); roxas5@sjtu.edu.cn (X.L.); gao.yan@sjtu.edu.cn (Y.G.); zhouchuanzhi@sjtu.edu.cn (C.Z.); zhwngxin@sjtu.edu.cn (X.Z.)
2 Institute for Public Policy, Zhejiang University, Hangzhou 310058, China; myy0716@outlook.com

* Correspondence: zhengweiskylark@sjtu.edu.cn
+ These authors contributed equally to this work.


#### Abstract

The construction of agricultural green bases is an important part of sustainable agricultural development. This paper takes urban agriculture green bases in Shanghai as an example, choosing base construction elements, production, and ecological construction elements, as well as status assessment elements as evaluation indicators, in order to construct an evaluation system for urban agriculture green bases. Using a Bayesian network, typical urban agricultural green bases in six agricultural districts of Shanghai were evaluated. The construction of the evaluation system was analyzed by using intervention, counterfactual inference, and other methods to analyze the correlation and importance of the indicators. The results show that there are differences among the bases in various indicators, but they all reach a high level overall; base construction elements as well as production and ecological construction elements are the main factors affecting the level of urban agricultural green bases; improving the base management system (BMS), innovativeness (IN), and economic benefits (EBs) are key ways to improve the production capacity of agriculture green bases. Green base construction should pay attention to top-level design, coordinate the planning of industrial layout, technical mode, scientific and technological support, and supporting policies. Based on the conclusion, this paper provides some useful recommendations for creating urban agriculture green bases, which help promote urban agriculture transformation, upgrading, and coordinating development between urban and rural areas.


Keywords: urban agriculture; green base evaluation; Bayesian network; causal inference

## 1. Introduction

In 2015, the United Nations General Assembly, at its 70th session, adopted Transforming Our World [1]: the 2030 Agenda for Sustainable Development, which includes 17 Sustainable Development Goals, including one to "end hunger, achieve food security, improve nutrition, and promote sustainable agriculture." One of the essential strategies to solve food insecurity and achieve sustainable agricultural development is to develop urban agriculture (UA) [2-4]. The most widely cited definition of UA is any form of agricultural or horticultural activity that takes place in and/or around a city [5]. UA is an essential foundation for food security while simultaneously becoming a new cultural-political expression and land-use fashion as a source for social cohesion and environmental education worldwide [6-8]. Compared to traditional agriculture, the critical characteristic of UA is that it is more deeply integrated into the urban system, including social and cultural life, economics, and the city's metabolism [9]. UA introduces a new form of agricultural development and can mitigate the effects of urban heat islands [10], optimize resource efficiency [11], foster integration and cohesion in multicultural settings [12], improve biodiversity and species richness [13], alleviate water scarcity [14], and reduce considerable greenhouse gas emissions $[15-17]$.

High-tech agricultural facilities and factory production are among the hallmarks of China's current urban agriculture development [18]. The high-quality construction of urban agricultural green bases (UAGBs) can improve the total production capacity of China's UA [19] because UAGBs often utilize advanced agricultural science and technology. The definition of UAGBs is not yet uniform, and even the terminology used to express its concept is different, such as "peri-urban farms", "urban agricultural production zones", etc. In this paper, we adopt the term "UAGBs" based on Shanghai's DB31/T 1389-2022 (Construction and Management Specification For Agricultural Green Bases) [20]. Meanwhile, for the definition of the base, we adopt the standard definition of DB31/T 1389-2022, which defines UAGBs as the use of advanced agricultural science and technology, supporting equipment, management concepts, and green development modes to carry out agricultural production located in the green food reserve bases of large-scale planting or breeding areas. The types of UAGBs in Shanghai include orchards, rice fields, vegetable farms, etc. In recent years, the distinction between organic products and green products has seen a significant trend toward high-quality agricultural products [21,22]. For ease of understanding, the classification criteria for AGBs and their organic and green products can be seen in Table 1.

Table 1. Comparison among certification types of green agricultural products, organic agricultural products, and green agricultural bases.


How to build sustainable agricultural green bases (AGBs) around the city is a new topic for the development of UA. Many countries and regions have undertaken some exploration based on their differences in agricultural development. In 2015, Japan passed legislation aimed at utilizing the versatility of UA to explore ways to develop peri-urban farms in a diversified manner [23]. There are various AGBs in Singapore, such as the well-known Kranji Countryside, a plant planting and animal breeding base northwest of the island [24]. The new policy of the Singaporean authorities dictates the establishment of AGBs oriented toward modern, intensive, and high-tech agriculture. In accordance with the spirit of the Central Government on improving the quality of agricultural products, Chinese provinces are also actively promoting the construction of UAGBs for high-quality agricultural products. For example, the Shanghai Municipal Agriculture and Rural Committee has formulated the Implementation Plan for the Construction of Agricultural Green Bases in Shanghai (2021-2025). The document calls for improving the comprehensive production capacity of green agriculture by optimizing the city's layout, creating UAGBs, and comprehensively promoting green production methods.

Building UAGBs is a very important task, so it is important to have a comprehensive understanding of the current building situation and to further develop sustainable UA by summarizing the experience. However, few studies have conducted field surveys and analyses of the overall construction of UAGBs. Therefore, this study has two main objectives. Firstly, we aim to fill the research gap in the evaluation of the current status of UAGB construction in China. To this end, we conducted in-depth field research and presented our findings in detail in this paper. Secondly, considering that UAGBs, as new types of agricultural production entities, do not yet have a fully mature standard and evaluation method, we constructed a comprehensive evaluation system based on the construction goals of DB31/T 1389-2022. We applied this evaluation system and conducted detailed calculations on various indicators to comprehensively evaluate the operation and management level of UAGBs and summarize their potential for improvement. Our evaluation system has significant value in promoting sustainable agricultural development.

The first section of this paper provides an introduction, and the second section summarizes the related literature. The third and fourth sections introduce the main methods of empirical analysis: causal inference and Bayesian network. The fifth section introduces the construction results of the evaluation system, and the conclusions are given in the final section of the paper.

# 2. Literature Review 

The overall development of UA relies on the unified improvement of the level of UAGBs. With the continuous development of UA, more and more studies are analyzing the construction situation of UAGBs from multiple dimensions, including land, environment, planting type, layout, etc.

Land suitability analysis is one of the important tools for the rational planning of AGBs, ensuring sustainable agricultural development, and achieving global food security goals. At present, there is no unified standard, method, or solution for the land suitability evaluation of UAGBs. Taking the Yusufeli District of Altwen City, Turkey, as an example, the construction of UAGBs was reasonably evaluated by using many criteria: large soil group, land use capacity class, land use capability sub-class, soil depth, slope, elevation, erosion level, and other soil properties [25]. Agricultural land suitability evaluation for crop production is a process that requires specialized geo-environmental information and the expertise of a computer scientist to analyze and interpret the information, such as ALSE, an intelligent system for assessing land suitability [26]. At the same time, environmental change and climate change will also affect the land suitability of AGBs. For example, Ethiopia is one of the countries that are most vulnerable to climate change due to its reliance on rain-fed agriculture [27].

In the construction process of UAGBs, it is also necessary to achieve green quality standards in the production environment. Pollution-free fruit and vegetable bases are required to restrict or prohibit the use of high-toxicity and high-residue pesticides [28]. Taking the construction of green and high-quality agricultural product bases in Jiangsu Province as an example, the optimization and supervision of the UAGBs must be controlled by a double reduction in pesticides and fertilizers [29]. The star fruit UAGB in Fujian Province pays special attention to the hazards in the biological, chemical, and physical fields of the base and takes site management, fresh fruit testing, fruit collection, and market sales of fresh-keeping products as the four key control objects to promote the reasonable development of the UAGB [30].

Due to the different geographical locations, uneven distribution of agricultural resources, different levels of productivity, and other factors, the planning policies and agricultural layouts of UAGBs vary greatly worldwide. The United States is divided into ten AGBs according to climate, soil type, distance to market, terrain height, and other factors: Appalachian Region, Northeast Region, Southeast Asia, Lake Region, Corn Belt, Delta Region, Southern Plain, Northern Plain, and Western Mountain [31]. The Law Concerning the Facilitation of Leasing of Urban Farmland was enacted in 2018 for the development of

the fulfillment of multiple functions of UAGBs in Japan. UAGBs include different forms of business in Japan, such as experience farms/allotment gardens, disaster prevention cooperation farmland, green areas/waterside spaces in urban areas, etc. [32]. UA in Australia has unique socio-cultural and environmental benefits. It can also have different scales depending on urban planning projects and operations. For example, there are three UAGBs in Queensland, Tasmania, and New South Wales, namely Verge Gardening, Market Farm, and Community Greening Program [33].

In summary, the factors selected for examining the construction situation of UAGBs are relatively scattered at present, and few studies have systematically summarized the key variables that need to be considered in the construction process of UAGBs and given improvement suggestions through specific analysis by empirical mode. Therefore, this paper adopts an empirical method combining Bayesian networks and geographic information, guided by the concept of green production, and selects various variables of base construction, production ecology, and current situation evaluation according to the systematic principle of green base research to construct an evaluation system for base evaluation. In addition, the UAGBs selected by previous studies are not typical and are few, with a single type, while the UAGBs considered in this paper are located in Shanghai, one of China's most advanced cities. They are all demonstration UAGBs with indicators evaluated by experts.

# 3. Indicators Selection 

To gain a multidimensional understanding of the agricultural base, it is crucial to comprehend the indicators used for evaluating sustainable agricultural production. As depicted in Figure 1 and Table 2, we propose that the establishment of agricultural green bases should prioritize top-level design, harmonize industrial layout, technology mode, scientific and technological support as well as supporting policies. The selection of these indicators is rooted in a comprehensive set of considerations. Firstly, green bases should primarily focus on production, to enhance the greening process and improve the quality of local agricultural products. This involves concentrating on bases with a high degree of organization and specialization and applying integrated pest management, green prevention, and control, healthy breeding, and other technologies. Secondly, the creation of an agricultural green base should be guided by green development principles, which involve formulating a scientific evaluation system and an institutional system. Lastly, the consideration of agricultural location is crucial. This involves improving the base level of production-deficient areas in a coordinated way, playing a radiating, driving role and gradually forming a green production pattern of urban agriculture that covers the whole industry, region, and subject. These considerations ensure a well-rounded and effective selection of indicators for the evaluation of sustainable agricultural production.
![img-0.jpeg](img-0.jpeg)

Figure 1. Detailed indicators for evaluating bases. In the framework of this study, the evaluation elements of agricultural bases were divided into three major elements.

Table 2. Evaluation indicators include the content.


Table 2. Cont.


Low: 0-6
Medium: 6-8
Relatively High: 8-9
High: 9-

Low: 0-3
Medium: 3-4
High: 4-

Low: 0-3
Medium: 3-4
Relatively High: 4-5
High: 5-

Low: 0-3
Medium: 3-4
Relatively High: 65-74
High: 74-

Our evaluation elements include several variables listed in the table below, each evaluated using a scoring method (Table S1). According to our research purpose, we divide the related elements of the base into three categories: Base Construction Elements, Production Ecology Construction Elements, and Status Assessment Elements. Figure 1 elucidates the specific meaning of these elements. This approach ensures a comprehensive and well-founded selection of indicators, providing a robust framework for the evaluation of sustainable agricultural production.

# 3.1. Base Construction Elements 

The Status of Base Construction (SBC) is the most important element of base construction [34]. This part should take the requirements of "Green Food Production Environment Quality" (NY/T 391) as the standard [35], evaluate the degree of satisfaction of the base in a good ecological environment, flat field, orderly layout, avoiding various pollution sources, and other requirements, the degree of excellence of basic environmental indicators such as air, soil, water, and so on in the base, and the degree of perfection of various basic facilities that should be matched with production in the base. The Base Management System (BMS) is an important indicator to evaluate the modernization construction of the base. Under the conditions of limited space resources and large production demand in urban agriculture, more attention should be paid to the important role of the management system for agricultural sustainability [34]. This study takes standardized production, postmanagement, environmental management, and input management systems as the main evaluation criteria to promote standardized production in the base.

Management Level (ML) is a concrete manifestation of the base management effect. According to the base management effect, a comprehensive evaluation is carried out on management orderliness, degree of execution intensity, and execution effect.

Certification of Agricultural Products (CEP) is a key element in evaluating agricultural product quality. Different base construction situations will affect agricultural product certification. The basic CEP refers to pollution-free agricultural products, green food, and organic agricultural products [36]. This paper discusses three types of agricultural products: pollution-free, green, and organic. Pollution-free products use safe inputs and meet national standards. Green products are grown in excellent environments and are of high quality. Organic products do not use any chemicals, genetically engineered organisms, or their products. Each type of product has a specific sign.

### 3.2. Production and Ecological Construction Elements

Status of Production Management (SPM) measures how standardized the production process of agricultural bases is [37]. It evaluates how well bases follow quality control and standardized production in areas such as inputs, pest control, animal health, harvesting, storage, transportation, and traceability. Traceability information and other aspects of the implementation of the whole process of quality control management promote a degree of standardized production.

Testing and Evaluation System (TES) is mainly the extent to which the base carries out the monitoring of products and the environment [38,39] to achieve effective quality control and production environment improvement. Among them, plantation bases should carry out monitoring of soil quality and ground strength maintenance; livestock and poultry farming bases should carry out monitoring according to the relevant requirements; and aquaculture bases should carry out monitoring of farming tailwater and pond substrate.

Pollution is a key issue that cannot be ignored in the process of agricultural production activities [40,41], and to meet the ecological and environmental protection requirements of agricultural green bases, the Status of Pollution Prevention (SPP) is used to evaluate whether the bases have done a good job in the disposal of various wastes and pollutants generated during agricultural production, strengthening the comprehensive utilization of straw, recycling of agricultural films and waste packaging, resource utilization of manure,

treatment of breeding tailwater and substrate, and odor control to effectively protect and improve the environmental quality of agricultural production.

# 3.3. Status Assessment Elements 

With the renewal and development of modern agricultural technologies and farming concepts, agricultural sites have to innovate their production methods and keep up with the times [42,43]. To assess the innovativeness (IN) of a site, it is important to assess whether the measures taken have led to an increase or improvement in the yield, efficiency, or potential of the cultivation methods. In addition, the sustainability of an agricultural site necessarily requires a balance of financial flows, and we evaluate the economic benefits (EBs) of agriculture in terms of business conditions, business models, and sustainability.

Healthy soil, as a dynamic living system that provides multiple ecosystem functions, is necessary for sustainable agriculture. The health of the soil affects plant composition, productivity, and sustainability [44], and ensuring the quality of agricultural soils is a common challenge for modern agriculture [45]. To assess the soil health of agricultural sites, we used a comprehensive soil quality score based on index scores and assignments. Several indicators were included, such as soil respiration rate, FDA hydrolase activity, neutral phosphatase activity, earthworm abundance, Shannon index, organic matter, total salinity, bulk weight, and geometric mean weight diameter.

## 4. Evaluation Methodology

In order to systematically and structurally evaluate the development status of green agricultural bases, it is necessary to combine geographic information systems and Bayesian networks for analysis. Compared with traditional statistical methods, causal inference not only focuses on the correlation between variables but also attempts to determine whether a change in one variable will lead to a change in another. This is crucial for understanding the relationships between the evaluation indicators of green bases. In assessing the current situation of green bases, causal inference can effectively handle confounding variables that may affect both dependent and independent variables, helping us identify the direct and indirect variables that influence the construction of green bases. Causal inference emphasizes randomized experimental design, making it an ideal analytical method for green base status surveys where comparative experiments cannot be conducted. Causal inference not only focuses on the predictive effect within the sample but also on the predictive effect in different environments, which helps us better understand and predict the effects of policy changes and other interventions and is of great importance for evaluating future improvement measures for green bases. The correlation between various evaluation elements of the base is established from an overall perspective by using a Bayesian network, and then the current situation of agricultural development is evaluated by using a Geographic Information System (GIS) according to the agricultural regions.

### 4.1. Bayesian Networks and Structural Causal Models

Bayesian networks consist of two parts: structure $G$ and parameters $\theta$ [46]. The structure $G=(V, E)$ is a directed acyclic graph, wherein the set of $n$ nodes $V=\left(X_{1}, X_{2}, \cdots, X_{n}\right)$ is variable and the set of directed edges represents the causal dependence between variables. $\theta$ is the network parameter, i.e., the probability distribution of nodes, which indicates the degree of interaction between nodes. $\theta_{i} \in \theta$ denotes the conditional probability at the parent of a given node $X_{i}$, and the joint probability distribution of the set of nodes can be expressed as follows:

$$
P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left[X_{i} \mid \pi\left(X_{i}\right)\right]
$$

where $X_{i}$ is the set of node variables in the network, $i=1,2, \cdots, n, \pi\left(X_{i}\right)$ is the set of parent node variables of the node $X_{i}$. In causal inference, Bayesian networks are called Structural Causal Models (SCMs), which are Causal Graphical Models.

# 4.2. Structural Causal Model Construction 

Bayesian network structure learning consists of three parts: Bayesian network structure learning, Bayesian network parameter modeling, and Bayesian network inference, where Bayesian network structure learning uses the PC algorithm [47] and knots the GPDC conditional independence test [48].

Bayesian network parameter learning is used to learn and calculate the posterior conditional probability distribution (CPD) of a Bayesian network using a dataset after establishing the network topology according to certain mathematical criteria. Bayesian network inference is performed using the belief propagation (BP) algorithm [49]. Bayesian network structure learning is performed using the tigramite package [50], and parameter learning and inference are performed using the pgmpy package [51].

The PC algorithm is a constraint-based causal discovery algorithm. It must obey the following two assumptions: the Causal Markov Assumption-for the set of variables with causal sufficiency if all variables and their non-descent nodes are mutually conditionally independent of each other under the condition that the father nodes of the variables are known; and the Causal Faithfulness Assumption-if variables $v_{i}$ and $v_{j}$ are mutually or conditionally independent given the set of variables, then in a causal network graph $G$ consisting of variables and their causal dependencies, all paths between $v_{i}$ and $v_{j}$ are d-separated by the appropriate variables in the set of variables V. The PC algorithm first determines the dependencies by d-separation, and then passes through the GPDC conditional independence algorithm. The PC algorithm first determines the dependencies via d-separation, then determines the correlations by using the GPDC conditional independent test, and finally determines the dependencies to construct the DAG.

In order to extend the results, we classify the variables into different classes in addition to causal inference, as well as construct a Bayesian probability model using the BP algorithm to infer the conditional probabilities.

### 4.3. Intervention of Variables

The ultimate goal of many statistical studies is to predict the outcome of an intervention. Randomized controlled experiments are considered the gold standard in statistics. In a properly conducted randomized controlled experiment, all factors affecting the output variable are either constant or vary randomly except for the input variable, so any change in the output variable is necessarily caused by this input variable. Unfortunately, many problems do not lend themselves to resolution with randomized controlled experiments. Intervening from causal graphs that have been constructed [52,53] is a way to study the interrelationship of variables when experiments cannot be conducted.

The SCM language makes it straightforward to formalize interventions as operations that modify a subset of assignments:

$$
X_{i}:=f_{i}\left(P A_{i}, U_{i}\right),(i=1, \ldots, n)
$$

e.g., changing $U_{i}$, setting $f_{i}$ (and thus $X_{i}$ ) to a constant or changing the functional form of fi (and thus the dependency of $X_{i}$ on its parents).

For a causal graph $G$ such that $P(\cdot)$ is the probability distribution function for all variables, for any four mutually disjoint subsets of variables $X, Y, Z$, and $W$, with the following:

Adding or deleting:

$$
P(y \mid \hat{x}, z, w)=P(y \mid \hat{x}, w) \text { if }(Y \perp Z \mid X, W)_{G_{X}}
$$

Intervention and observation exchange:

$$
P(y \mid \hat{x}, \hat{z}, w)=P(y \mid \hat{x}, z, w) i f(Y \perp Z \mid X, W)_{G_{X Z}}
$$

Add or remove interventions:

$$
P(y \mid \check{x}, \check{z}, w)=P(y \mid \check{x}, w) \text { if }(Y \perp Z \mid X, W)_{G_{\bar{X}, Z(W)}}
$$

In the above formulation of the axiom, $G_{\bar{X}}$ denotes a subgraph $G_{\bar{X} Z}$ obtained by removing all edges in $G$ that point to $X$ nodes denoting a subgraph obtained by removing all edges in $G$ that point to $X$ nodes and edges that point to $Z$ nodes.

# 4.4. Definition of Base Quality Improvement Potential 

To design ecological farms in a targeted manner, the geospatially enhanceable components are studied. We measure the potential capacity of base enhancement in terms of counterfactual extrapolation. Let $X$ and $Y$ be two subsets of variables in $V$. The counterfactual sentence " $Y$ would be $y$ (in situation $u$ ), had $X$ been $x$ " is interpreted as the equality with $Y_{x}(u)$ being the potential response of $Y$ to $X=x$ [54]. Given the observed feature $E=e$, the counterfactual expectation is denoted as $E\left[Y_{X=x} \mid E=e\right]$, where we allow for $E=e$ to conflict with the antecedent $X=x$. To compute the expectation, the three-step process reads as follows:

Step 1: Abduction: Use evidence $E=e$ to determine the value of $U$.
Step 2: Action: Modify the model, $M$, by removing the structural equations for the variables in $X$ and replacing them with the appropriate functions $X=x$, to obtain the modified model $M_{X}$.

Step 3: Prediction: Use the modified model $M_{X}$ and the value of $U$ to compute the value of $Y$, the consequence of the counterfactual.

Defining base quality improvement potential:

$$
\begin{gathered}
\text { if } i \text { is not root node : } \\
\text { Improve }=\max \left(0, \text { Value }_{i \max (\text { mean }(x), x)}\right)(U)-\text { origin }) \\
\text { if } i \text { is root node }: \\
\text { Improve }=\max \left(0, \text { mean }\left(\text { Value }_{i}\right)-\text { origin }\right)
\end{gathered}
$$

where $i$ is the evaluation index. Improve means that, if the variable is the root variable, the difference between the mean value of the variable mean $\left(\right.$ Value $\left._{i}\right)$ and the current value origin is taken and compared with 0 , to measure the degree of enhancements; if it has parent nodes, the value of all parent nodes is made to be the mean value, and then the counterfactual inference Value $_{i, \max (\operatorname{mean}(x), x)}(U)$ and the difference between the obtained value and the current value is compared with 0 to measure the degree of elevation.

## 5. Results and Analysis

The data were obtained through field research in agricultural areas of Shanghai. To comply with management standards and facilitate standardized management, these planting bases have uniformity in terms of farm types (economic units). We categorize them into three major types: orchards, vegetable farms, and rice fields. Our samples show that, with orchards, vegetable farms, and rice fields as the three main crops, there are more important agricultural bases in Pudong and Chongming, with the orchards being mainly distributed in Pudong and the vegetable farms being mainly distributed in Chongming and Pudong. The distribution of agricultural bases in Shanghai is consistent with the map of Shanghai and has a clustering effect. In Figure 2, within the Shanghai area, there are a variety of crops cultivated that belong to the species structure of integrated agriculture. However, for localization, it is mainly a combination of cultivation and livestock farming, wherein orchards and vegetable farms are usually clustered in cultivation, and rice fields are relatively scattered.

![img-1.jpeg](img-1.jpeg)

Figure 2. Distribution of samples and basic information.
$76 \%$ of the surveyed bases are Green bases, $66 \%$ of them have a medium management level, and the high-level bases are basically distributed in Fengxian, Jinshan, and Chongming. The management capacity of the rice fields is lower in Chongming, but the number is higher, and it is basically a green-certified base. Pudong's management level rating is in the low-to-medium range.

# 5.1. Descriptive Statistics of Indicators and Geographical Distribution 

The mean values of all indicators were higher in rice fields, followed by orchards and vegetable farms. The distribution of indicators in orchards and vegetable farms was not as uniform as that in rice fields. Table 3 shows the numerical characteristics of the different variables. The basic situation of the bases of different cultivation types is shown in Figure 3 and the basic situation of the bases of different regions is shown in Figure 4.

The construction of base facilities (SBC), agricultural production management (SPM), comprehensive treatment of pollutants (SPP), and base rules and regulations (BMS) of rice fields are higher than those of orchards and vegetable farms, but they are lower in terms of base innovation (IN), economic benefits (EB), and land sustainable cultivation ability (SHD). In terms of production process monitoring and evaluation (TES), rice fields and vegetable farms are higher than orchards, among which Jinshan, Chongming, and Songjiang districts have the best monitoring work, while Fengxian, Qingpu, and Chongming districts have the worst monitoring work. Among rice fields, SBC is the highest in the Fengxian district, SPM is concentrated around 43 points, SPP is concentrated around 8-10 points, TES is concentrated around 5 points, and BMS is concentrated around 12-14 points. The SBC, SPP, and TES of orchard bases are low, among which SBC is mainly concentrated between 12 and 18 points, with uneven highs and lows. Jiading and Baoshan have higher SBC, while Qingpu and Songjiang have lower SBC; SPP is mainly concentrated around 6 points; TES is the lowest in the Fengxian district. The SPM, IN, EB, and SHD of orchard bases are high, among which SPM is the highest in Jinshan district and Chongming district, IN is concentrated between 3-5 segments, EB is concentrated between 4.5-5 segments, and SHD is concentrated between 60-80 segments. The scores of vegetable farms are evenly distributed, without much difference. Among them, SPM, EB, and SHD are high, while SPP and TES are low. SPM is concentrated around 43 points, EB is concentrated around 4.5 segments, SHD is concentrated between 60-80 segments; SPP is concentrated around 6 points, and TES is the highest in Jinshan district and Songjiang district.

The differences in scores between different regions are also very obvious. Among them, Jinshan district has the highest scores in agricultural production management, comprehensive treatment of pollutants, and production process monitoring and evaluation. Jiading district has the highest scores in base rules and regulations, base innovation, and

economic benefits. Songjiang district has the lowest score in land sustainable cultivation ability. Fengxian district and Qingpu district perform poorly in multiple aspects, while Pudong district has mixed results.

Table 3. Descriptive statistics of each indicator.


![img-2.jpeg](img-2.jpeg)

Figure 3. Distribution of variables for different cultivation types of bases. Significance level: ** for 1% and * for 5%.

![img-3.jpeg](img-3.jpeg)

Figure 4. Distribution of variables in different regions. Significance level: * for 5%.

# 5.2. Basic Structure of Bayesian Network 

The survey data were obtained from the field survey, covering the basic conditions of the major agricultural bases in each region of Shanghai, and were reviewed by experts for reliability and authenticity. Based on the survey data, we applied the causal inference method to analyze the factors affecting the bases.

We consider most of the variables in the model to be continuous variables, but they are artificially graded for ease of generalization when used in practice. Using the PC algorithm based on the conditional independence test GPDC combined with a priori knowledge to infer the network structure and the graphical method of causal inference to calculate the contribution degree and link strength, the distribution of the probability of no evidence case and the conditional probability distribution were calculated by using BP for the divided ranks, and the following figure was obtained. The order of cause-to-effect in the figure is shown from top to bottom. The inferred results are consistent with reality and a priori knowledge. On the basis of our study, the probability that the indicators are in the upper-middle range is high.

The reasonableness and sensitivity of the network were assessed using causal inference methods. The results of the Markov independence test, the addition of confounding variables, randomization of variables, and evaluation using subset validation all indicate that the network is rational. Table 4 exhibits that all sub-nodes passed the Markovness test, and Table 5 shows that none of the results obtained after refuting the network using the three approaches were significantly different.

Table 4. Local Markov test.


Table 5. Causal Inference Node Refutation.


Figure 5 shows the structure of the Bayesian network obtained by inference using the PC algorithm, and Figure 6 shows the centrality of each node. The EBs are essentially in the

relatively high (0.344) and high (0.307) ranges, which is the result of the combined effect of several variables directly influenced by SPM and ML. SBC, SPM, and BMS have higher centrality, between 0.3 and 0.5, and are more important nodes with a higher likelihood of higher evaluation, reaching 0.428 and 0.519, while SBC, TES, and the certification system are the more important nodes. IN affects BMS and SPM, which indicates that base innovation mainly changes management systems and production methods. TES affects the SHD, and long-term monitoring and improvement of the site environment will improve the suitability of the growing environment.

![img-4.jpeg](img-4.jpeg)

Figure 5. Bayesian network structure.

![img-5.jpeg](img-5.jpeg)

Figure 6. Node centrality radar map.

The Kullback-Leibler divergence was used to measure the intensity of arrows for categorical targets and the variance in continuous real-valued targets. Any change in the marginal distribution of the target (obtained by marginalizing the joint distribution) is due to a change in the causal mechanism of the target variable. This means that we can also quantify arrow intensity based on changes in the properties of the marginal distribution (e.g., mean, variance) of the target when edges are removed. The units of measurement for the arrow strength scalar values are the variance of the continuous real-valued targets as well as the number of bits of the categorical targets. Contribution refers to the contribution of each variable to the target variance, i.e., for the target variable, how much of the variance comes from the other variables. This can be seen from the contribution degree table and the link strength in the Bayesian network diagram. Table 6 shows the contribution of each node.

Table 6. Contribution of nodes.


TES has a high link strength of 40.542 for SHD but only 0.623 for SPP, so positive control of the quality of the environment (TES) at the base will enhance the sustainable use of the soil (SHD). The connection strength of BMS to SPM is 36.438 , while the connection strength of SHD to SPM is only 2.155. Explain that the management of agricultural production processes (SPM) and base administrative management (BMS) should complement each other. The linkage strength of SPM, CEP, and ML on EB are $0.144,0.004$, and 0.045 ,

respectively. Among the three, the management of the agricultural production process (SPM) is the most important factor affecting economic benefits (EB). SPM (0.635) and TES (0.623) have similar strengths of association with SPP, showing that TES has a similar strength of association with SPM. This shows that actively constructing a monitoring and evaluation production system (TES) and having an environmentally friendly production process (SPM) can effectively improve the pollution prevention and control effect of the base (SPP). The innovative type contributed 15.707 to SPM, and IN has the highest nodal contribution to BMS (2.497), even higher than the intensity of BMS itself (1.978). The highest contributor to EBs is IN (0.209), which far exceeds the contribution of other items to EBs. This shows that having an innovative production system (IN) can improve the overall level of the base and achieve high economic benefits. TES has the highest contribution to SHD, with a significant contribution of 37.420. Establishing a sound production monitoring system (TES) and conducting reasonable monitoring is an important means to improve the sustainable utilization capacity of the land (SHD).

In summary, these indicate that the rules and regulations of the base are closely linked to the production system and the production monitoring process. Innovation within agricultural green bases is a crucial factor in enhancing base earnings and transforming production management methods. Moreover, the effective management of various agricultural pollutants in the base can improve the health of farmland soil, enabling sustainable utilization.

# 5.3. Intervention Effects at Important Nodes 

Through intervention, we further studied the causal effects between variables. Overall, the improvement of economic benefits (EB) is greatly influenced by the innovation of production methods (IN), and it also requires the organic integration of production systems (SPM) and management systems (BMS). The sustainable development of soil (SHD) requires the monitoring and evaluation of production processes (TES) and the adoption of active measures for pollution prevention and control (SPP). The specific empirical analysis is as follows:

Figure 7 shows the results of the intervention experiment on vegetable farms. The effect of the intervention on most of the important variables in vegetable farms is positive. As TES increased from 2 to 4, SPP increased from 5 to over 8; as SPM increased from 15 to 50, SPP increased from 5 to over 8. This indicates that tracking and managing the production process (TES), along with actively implementing pollution prevention and control measures (SPP), can greatly enhance the effectiveness of pollution prevention and control (SPM). As BMS increases from less than 4 to more than 14, SPM increases from 6 to more than 8 ; as SHD increases from less than 30 to more than 70 , SPM increases from 6 scores to more than; SPM increased only slightly as SHD increased from less than 30 to more than 70 . This indicates that the quality of management practices during cultivation at the base (SPM) significantly impacts the sustainable development of the land (SHD). As SBC increases from 8 to 20, BMS increases only slightly; as IN increases from 2 to 5, BMS increases from 6 to over 12. As IN increases from 2 to 5, EB also increases from 2 to 5; as SPM increases from less than 15 to 50, EB increases from 2 to 5; and BMS increases only slightly. EB increases from 2 to 5 as SPM increases from less than 15 to 50; an increase in ML and seriousness type does not significantly increase EB and may even decrease it. This suggests that the economic returns of the base (EB) are closely related to the management system (ML) in place, and improving innovative base management systems and planting models can enhance economic benefits. The ML for a CEP of 1 or $2(2.00)$ is much higher than the ML for a CEP of 0 (1.00). SHD increased from 40 to 60 , but when the TES is 5 , there is a slight decrease in SHD. This demonstrates that agricultural product certification (CEP) can effectively distinguish the comprehensive management capabilities of different bases (SHD).

Figure 8 shows the results of the intervention experiment on rice fields. Only a few of the intervention effects among the important variables in the rice fields were significantly positive, while the rest of the intervention effects were insignificant (close to 0). SPP increased from 8 to 10 as TES increased from 3 to 5, and SPM increased from 32 to over

46. EB increased from 3.0 to 4.5, and SPP remained at about 9.5 despite the significant increase in SPM (from 32 to over 46). Similar to orchards, the pollution prevention and control effects (SPP) in rice fields are influenced by monitoring systems and production management (TES). However, the linkage effect between production management (SPM), base construction (SBC), and base management (BMS) in rice fields is not strong, which may be related to the construction characteristics of such bases. BMS to SPM, SBC to BMS, and SHD to SPM were not significant. The improvement of SPM (from 30 to 45) can significantly increase EB (from 3 to 5), indicating that production management capability (SPM) is a crucial factor in obtaining economic benefits (EB).

Figure 9 shows the results of the intervention experiment on orchards. The intervention effects between the orchards' significant variables were almost always significantly positive. There was a small increase in SPP between 6 and 8 as TES increased from 2 to 5 and a small increase in SHD (apart from a TES of 3). This suggests that orchards have a strong capacity for sustainable soil utilization (SHD), unlike the first two types of bases, which generally require stronger monitoring capabilities (TES) to maintain health. As SPM increases from less than 10 to 50, SPP increases from 2 to more than 8, and EB increases from 1 to 4. As BMS increases from 2 to over 14, SPM increases from 10 to over 40. As IN increases from 1 to 5, both BMS and EB increase slightly, and as ML increases from 0 to 2, EB and ML are comparable when CEP is 1 or 2 and are significantly greater than when CEP is 0 . This indicates that a series of management capabilities (ML) in orchards, including pollution control (SPP), production management (SPM), and base management, have a linkage effect. The improvement of innovation (IN) and management capabilities (ML) will bring economic benefits (EB). Moreover, bases with organic certification and green certification will have higher economic benefits than ordinary bases. Finally, a large increase in SHD did not significantly increase the SPM. The intervention effects among important variables for vegetable farms and orchards were mostly positive, while the intervention effects for rice plantations were generally insignificant.
![img-6.jpeg](img-6.jpeg)

Figure 7. Effectiveness of interventions on vegetable farms.

![img-7.jpeg](img-7.jpeg)

Figure 8. Effectiveness of interventions on rice fields.

![img-8.jpeg](img-8.jpeg)

Figure 9. Effectiveness of interventions on orchards.

In summary, the agricultural structure in Shanghai is characterized by integrated agriculture. In the process of localization, it primarily involves a combination of cultivation and breeding, where orchards and vegetable farms are typically concentrated in cultivation while rice fields are relatively dispersed. Vegetable farms usually require regular weeding,

fertilization, and watering. The planting and harvesting times of vegetables need to be adjusted according to the type and growth cycle of the vegetables, which means that the health status and pollution condition of the soil are greatly affected by real-time monitoring. The management of orchards includes the regular pruning of trees, fertilization, and disease control. This makes the management of orchards relatively easy and the environment relatively stable after the trees are planted, preventing sudden environmental changes due to changes in subsequent pollution monitoring conditions. The management of rice fields includes planting, irrigation, fertilization, weeding, and harvesting. Rice fields need to be kept moist during planting to support the growth of rice. Therefore, like vegetable gardens, maintaining soil health and avoiding excessive pollution are crucial for sustainable development.

# 5.4. Base Quality Improvement Potential Based on Counterfactual Inference 

The potential for improvement is calculated according to the definition formula and normalized to a percentage; the larger the percentage, the more room for improvement there is. Figures 10-12 and Tables 7-9 show the results of counterfactual extrapolation for different planting methods.
![img-9.jpeg](img-9.jpeg)

Figure 10. Base quality improvement potential of orchards.
Table 7. Base quality improvement potential of orchards (\%).


According to the overall results, the soil sustainability capacity (SHD) of Chongming, Pudong, and Fengxian has more room for improvement, and the potential improvement potential of SHD for the three bases is $100 \%$. Although Chongming is an eco-island under construction, the attention to soil health seems to be insufficient, while the SHD of the orchards and vegetable farms in Minhang is better, the rice fields still have some

room for improvement. The overall level of base construction (SBC), production process management capability (SPM), and monitoring completeness of production process (TES) in Chongming, Pudong, Fengxian, and Qingpu have more room for improvement, and these areas need to further improve the base facilities and systems.
![img-10.jpeg](img-10.jpeg)

Figure 11. Base quality improvement potential of vegetable farms.
Table 8. Base quality improvement potential of vegetable farms (\%).


The construction level (SBC) of the orchard bases in various districts of Shanghai is quite perfect, with a potential for improvement of $0.00 \%$. The production management level (SPM) of the orchard base in Jinshan District is perfect, with an improvement potential of $0.00 \%$. In terms of the pollution monitoring results (SPP) of the orchard base, the improvement potential of Fengxian District is as high as $100 \%$, indicating that there is a large room for improvement of SPP in the orchard base of Fengxian District, and it is necessary to improve the pollution monitoring and evaluation and production management in multiple aspects to improve the pollution prevention and control effect. In contrast, the improvement potential of SPP in Jinshan District and Qingpu District is $0.00 \%$. In terms of the completeness of pollution monitoring means (TES), except for Jinshan District, other districts have a lot of room for improvement, among which the improvement potential of TES in Qingpu District orchard is the largest, reaching 100\%, followed by Pudong New Area ( $96.05 \%$ ) and Songjiang District ( $91.44 \%$ ). In terms of the perfection of the base management system (BMS) of the orchard, Qingpu District has the largest room for improvement (100\%), followed by Pudong ( $75.64 \%$ ) and Songjiang ( $74.69 \%$ ). The BMS in Jinshan District is relatively perfect, and the rest of the districts have medium room for improvement, with an improvement potential of about $50 \%$. In terms of the sustainable development of soil (SHD), the SHD of the Fengxian District orchard needs to be improved, while Jinshan District and Qingpu District are relatively perfect, with an improvement potential of $0 \%$. From the

comprehensive situation of orchards in various districts, the Jinshan District orchard base is well constructed, with an improvement potential of $0 \%$ for all indicators.
![img-11.jpeg](img-11.jpeg)

Figure 12. Base quality improvement potential of rice fields.
Table 9. Base quality improvement potential of rice fields.


The vegetable farms in various districts of Shanghai have the largest room for improvement in the management of production process (SPM), among which the improvement space of SPM in Fengxian District vegetable farms is the smallest ( $0.00 \%$ ), and Qingpu ( $100 \%$ ) and Jinshan ( $91.12 \%$ ) have the largest improvement space. In terms of the pollution prevention and control effect (SPP) of vegetable farms, Jinshan District has a better overall level of pollution prevention and control ( $0.00 \%$ ), while Qingpu District has the largest room for improvement ( $100.00 \%$ ). In terms of the perfection degree of the vegetable farm monitoring and evaluation system (TES), Qingpu District has the largest room for improvement ( $100.00 \%$ ), followed by Jinshan District ( $68.32 \%$ ), and the improvement space of the TES in Fengxian District and Chongming vegetable farms is between 20.00-30.00\%. In terms of base facility construction (BMS), Qingpu District (100.00\%) and Jinshan District ( $69.64 \%$ ) have larger room for improvement, and the improvement space of BMS in other districts' vegetable farms does not exceed $10.00 \%$. In terms of the sustainable utilization capacity of soil (SHD) in vegetable farms, except for Jinshan District ( $0.00 \%$ ) and Pudong District ( $25.64 \%$ ), the rest of the districts have more than $75.00 \%$ room for improvement.

The rice fields in various districts of Shanghai have little room for improvement in the current situation of facility construction (SBC) and production process management system (SPM), but the pollution prevention and control effect (SPP) of the rice fields in Minhang District ( $0.00 \%$ ) and Jiading District ( $33.33 \%$ ) has some deficiencies. The improvement space of the perfection degree of the rice fields monitoring and evaluation system (TES) in Songjiang District is the largest ( $100.00 \%$ ), and the improvement space of TES in other

districts does not exceed 50\%. Songjiang District (100.00\%) and Fengxian District (79.6\%) need to focus on improving the base management system (BMS). In terms of the sustainable utilization of soil (SHD), Jiading District, Fengxian District, and Songjiang District have little room for improvement, all being $0.00 \%$. In contrast, Chongming District (100.00\%) and Minhang District ( $94.12 \%$ ) have more room for improvement.

By using counterfactual inference, we can better understand the current situation and improvement priorities of Shanghai's agricultural green base development, and also incorporate the new bases to be built in the future into the model for analysis. The model constructed in this study has created a new method for evaluating agricultural green bases. In conclusion, Shanghai's agricultural base has room for improvement in all aspects but also has strengths and specific characteristics. For example, Chongming, Pudong, and Fengxian's SHD is low, while Jinshan and Songjiang's SHD is high. Chongming, Pudong, and Fengxian need to improve their pollution monitoring and soil management levels to promote the sustainable use of land. The SBC, SPM, and TES in Chongming, Pudong, Fengxian, and Qingpu are low and these districts need to design higher-standard ecological agricultural bases and strengthen their environmental monitoring and management. In terms of these values, rice fields in Minhang, orchards and vegetable farms in Fengxian, and orchards and vegetable farms in Qingpu are low. On different types of planting bases, vegetable farms, and orchards should pay particular attention to monitoring agricultural pollution sources. The indicators of agricultural bases in Qingpu are excellent and can serve as a reference for the planting model of agricultural green bases. The significance of this analysis is that, through the analysis results, some agricultural production areas with lower indicator evaluation can improve the deficiencies of related production links in a targeted manner.

# 6. Conclusions 

Urban agriculture is one of the essential strategies to solve food insecurity, improve nutrition, and promote sustainable development. With the acceleration of urbanization, urban agriculture faces challenges such as limited land resources, severe environmental pollution, low production efficiency, and so on. In order to improve the quality and efficiency of urban agriculture, it is necessary to build urban agriculture green bases that conform to the concept of green development and achieve coordinated development between urban and rural areas. The construction of agricultural green bases should pay attention to the toplevel design and coordinate the planning of industrial layout, technical mode, scientific and technological support, and supporting policies. In this study, Base Construction Elements, Production Eco-logical Construction Elements, and Status Assessment Elements were selected as evaluation indices to investigate and assess different types of urban agricultural bases in Shanghai, taking urban agricultural green bases as the target. These indicators provide a reference for assessing the sustainability and future prospects of agricultural production. The main conclusions are as follows:

There are some differences in the scores of various indicators among the bases in the six agricultural districts, which indicates that different types, scales, and modes of bases have their own characteristics, advantages, and disadvantages. Vegetable farms are typically established in areas with fertile soil and good drainage. They often require intensive management and high inputs, including frequent irrigation and fertilization. The advantage is that they yield a high output and can be harvested multiple times. The downside is that they may lead to soil nutrient loss and environmental pollution. Orchards are usually set up in areas with deep soil and good drainage. They require long-term investment and management, but once established, they can continue to produce for many years. The advantage is that they can produce high-quality fruits, and their impact on the environment is relatively small. The downside is that they require long-term investment and management, and they have high requirements for climatic conditions. Rice fields are usually established in areas with rich clay soil and poor drainage. They require a large amount of water resources, but they can produce a large amount of grain. The advantage

is that they yield a high output and can provide a stable source of food. The downside is that they have a high demand for water resources, which may lead to overexploitation of water resources. The research results show that, for different types of agricultural bases, the health of the soil, the protection of the base environment, and the sustainable development of land resources are all of paramount importance.

In general, according to our research, the development of urban agriculture green bases is influenced by the top-level design of the administrative management and continuous monitoring of the production process of the bases, while the overall industrial layout of the green bases, such as the monitoring and control of soil and land pollution and other ecological environment measures and advanced agricultural production technology modes, will affect the sustainable utilization capacity of the land, and ultimately affect the overall construction and economic and social benefits of the bases. Top-level design is an important prerequisite and guarantee for the construction of agricultural green bases, which involves policy orientation, goal setting, planning formulation, institutional arrangement, and other aspects. The top-level design should fully consider national strategies, regional characteristics, market demand, and other factors and form a general framework that is in line with reality and conducive to long-term development. Industrial layout is a key factor that determines the functional positioning and benefit level of agricultural green bases, which involves industrial structure, product varieties, market positioning, and other aspects. Industrial layout should optimize the allocation of resources, environmental capacity, consumer demand, and other factors, and form an industrial system that has competitiveness, adaptability, and innovation. Technology mode is the main means to achieve the production goals and quality standards of agricultural green bases, which involves planting technology, breeding technology, processing technology, and other aspects. The technology mode should select and innovate according to ecological conditions, product characteristics, market norms, and other factors and form a technical system that is efficient, energy-saving, safe, environmentally friendly, and high-quality. Scientific and technological support is an important source of development motivation and core competitiveness for agricultural green bases, which involves scientific research input, technology transformation, talent cultivation, and other aspects. Scientific and technological support should strengthen basic research, applied research, and demonstration promotion, improve scientific and technological innovation ability and level, and cultivate a group of scientific and technological talents and teams at the international level. The construction of green bases is the result of a series of supporting policies. Supporting policies are an important guarantee for the smooth operation and sustainable development of agricultural green bases, which involve financial support, tax preferences, financial services, and other aspects. Supporting policies should formulate a series of policies and measures that are conducive to stimulating vitality and promoting the coordinated development of the bases according to the development stage, characteristics, and needs of the bases. Although these views have been considered in the initial stage of agricultural green base construction planning, through our constructed evaluation model, we have empirically verified the internal correlation of these factors, which can quantify the impact of these factors more finely, which plays an important role in the evaluation of old bases and the guidance of new base construction.

This paper also has some limitations and shortcomings, such as an imperfect evaluation indicator system, limited data sources, simple evaluation methods, and so on. In the future, it is possible to further improve the evaluation indicator system, expand the data source range, use more diversified evaluation methods, and increase the depth and breadth of the research.

Supplementary Materials: The following supporting information can be downloaded at: https: //www.mdpi.com/article/10.3390/land12081636/s1, Table S1: Scoring rules for base indicators.

Author Contributions: Conceptualization, Y.L., Z.C. and Y.M.; Methodology, Y.L., X.L. and X.Z.; Software, Y.L.; Validation, Y.L.; Formal analysis, Y.L.; Data curation, Y.L. and X.L.; Writing original draft, Y.L., Y.M. and X.Z.; Writing—review \& editing, Y.L., Z.C. and Y.M.; Visualization, Y.L.; Supervision,

Z.C.; Project administration, Z.C., Y.G. and C.Z.; Funding acquisition, Z.C. All authors have read and agreed to the published version of the manuscript.
Funding: This work was co-supported by the Shanghai Philosophy and Social Science Program (17Z2017030008), Shanghai Agriculture Applied Technology Development Program, China (T20200201) and Shanghai Pujiang Talent Program (16Z2022010010).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: The data that support the findings of this study are available from the corresponding author upon reasonable request.
Conflicts of Interest: The authors declare no conflict of interest.
