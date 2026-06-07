# Green Evaluation for Building Interior Decoration Based on BIM-BN Technology 

Wenhan Fan ${ }^{1,2, \dagger}$, Baofeng Yan ${ }^{3}$, Quanxi Bao ${ }^{3}$, Yueqin Zhao ${ }^{1}$ and Jianliang Zhou ${ }^{1, * *}$ (D)<br>check for updates<br>Citation: Fan, W.; Yan, B.; Bao, Q.; Zhao, Y.; Zhou, J. Green Evaluation for Building Interior Decoration Based on BIM-BN Technology. Buildings 2023, 13, 744. https:// doi.org/10.3390/buildings13030744<br>Academic Editor: Xingwei Li<br>Received: 30 December 2022<br>Revised: 3 March 2023<br>Accepted: 10 March 2023<br>Published: 12 March 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Mechanics and Civil Engineering, China University of Mining and Technology, Xuzhou 221116, China
2 School of Engineering and Art Design, Shanxi Vocational and Technical College of Finance and Trade, Taiyuan 030031, China
3 The Third Construction Co. Ltd. of China Construction Eighth Engineering Division, Xuzhou 221100, China

* Correspondence: zhoujianliang@cumt.edu.cn; Tel.: +86-1589-521-2115
+ These authors contributed equally to this work.


#### Abstract

The popularity of green building and BIM technology has increased globally, with strong government support in China. However, the integration of green requirements into interior decoration poses practical difficulties. Despite the few studies on the combination of green evaluation and BIM in building decoration, current methods largely rely on expert scores after completion. This research proposes a green evaluation index system for building interior decoration, examining the inter-index relationships and contribute to the final green degree of the project. Additionally, a green evaluation method based on BIM technology and the Bayesian network is explored, aimed at evaluating the green degree of design schemes, providing feedback, and supporting the realization of green interior decoration. With a focus on green evaluation, the current methods that rely solely on expert scores after completion will be improved. The results will provide technical support for the realization of green decoration and offer a reference for the improvement of green evaluation methods in the future.


Keywords: building interior decoration; green evaluation; BIM; bayesian network; BIM-BN technology

## 1. Introduction and Literature Review

Green building development has become a worldwide popular topic in recent years [1]. Due to the different factors such as the level of economic development, geographical environment, resource availability, and so on, there is no single, widely accepted definition for green building [2,3]. The concept of green building in China was developed from the "energy-saving and land-saving residential buildings" launched by the central government in 2004 [4]. According to the Chinese national standard "Evaluation Standard for Green Building," formulated in 2006, green buildings can be defined as buildings that maximize resource conservation (energy, land, water, materials), protect the environment, and reduce pollution throughout the life cycle, so as to provide people with healthy, suitable and efficient use of space and live in harmony with nature [5].

Society is continuously developing, and the living qualities of people are constantly improving. The requirements of the inhabitants for a drawing room are not confined to shelter from the elements. However, what is more important, is a good place for the study and work of mankind, and a quiet and comfortable resting place, which is singularly needed [6]. In China, the total energy consumption is huge, while the resource endowment is relatively poor, with high external dependence [7]. Green building (GB) certification has been conducted as a major policy for reducing the energy consumption and greenhouse gas (GHG) emissions of buildings in developed countries [8]. Therefore, the decoration design of green buildings emerged in response to the proper time and conditions. Currently, there are several green building evaluation standards for interior decoration. However, research on green evaluation of building interior decoration with

BIM Technology is rare [9]. In addition, the existing green evaluation index system rarely considers the internal relationship between the indexes and the contribution mechanism to the green degree. Therefore, exploring green evaluation methods based on BIM technology is of great significance to the development of green evaluation in China.

It is complicated work to determine the weight of the index system, which greatly affects the accuracy of evaluation results [10]. Comparative analysis [11,12], whole life cycle theory [13,14,15,16], as well as environmental, economic, and social evaluation [17], are mainly used in the study of green building evaluation index system in China; Methods to give the weight of green building indicators mainly include the analytic hierarchy process [18,19,20,21], expert investigation method [22,23,24] and simple correlation function [25]; several commonly used evaluation models are grey clustering evaluation method [26,27,28,29,30,31], fuzzy comprehensive evaluation method [32,33], principal component analysis method [25,34,35], BP neural network $[20,36,37]$.

As the main theme of the informatization development of China's construction industry in the next decade, a series of applications based on BIM has become an irreversible trend. Many scholars around the world have also conducted relevant studies on the application depth of BIM technology in green engineering evaluation, including green evaluation application of BIM in the whole life cycle of buildings [38], using BIM models to evaluate indoor energy-saving optimization design of green buildings [39], the application of BIM in architectural lighting design [40], there are also comparisons between the BIM model in conventional design and the requirements of green building regulations [41]. In addition, by studying the defects of BIM in green evaluation [9], it is found that most of the green BIM research focuses on the design and construction stage [42]. At the design stage, the integration method of BIM and LEED system [43,44] and the Green Building Assessment Tool (GBAT) [45] can be used to extract necessary data from the BIM model and calculate green rating in order to provide feedback for further evaluation.

With the continuous acceleration of economic development, environmental pollution is becoming more and more serious. In addition,, the contradiction between economic development and environmental protection continues to escalate. Thus, it is extremely urgent to vigorously promote green decoration. Considering that the application of BIM technology in the field of decoration is of great significance to the industrialization and sustainable development of Chinese housing. The application and trend of BIM technology in the field of decoration are deeply discussed by using the huge potential of software parametric modeling and integrated database. The main research direction of the next step is to apply BIM technology to assist the green evaluation of building interior decoration and to optimize the interior design scheme in order to truly achieve green decoration and create an environmentally friendly and comfortable indoor environment.

Bayesian networks were originally proposed in 1981 by R. Howard and J. Matheson. Early Bayesian networks were primarily used in expert systems to express uncertain expert knowledge. Since the 1990s, great progress has been made in the study of Bayesian network learning methods. Domestic scholars have also conducted relevant studies on Bayesian networks. The research area mainly focuses on security risks, including the application of Bayesian networks. In terms of analyzing the mechanism of risk events caused by risk factors [46], human reliability assessment on building construction work at the height [47], and dam risk analysis, a new method for dam risk analysis is provided [48]. Since the Bayesian network is a kind of uncertain knowledge expression and reasoning technology, it can determine the relationship between different influencing factors and then provide decision support [49]. Thus, the Bayesian network can be applied for risk management, fault diagnosis, and data mining research. As a very active field, it presents great advantages in analyzing the influence mechanism between things and opens up new ideas for studying the internal relationship between the green evaluation indicators of the decoration project and the final greenness contribution mechanism.

However, the existing green evaluation methods are relatively reliant on score-giving by experts after completion. In addition, it is unclear of the internal relationship between

the evaluation indicators. There are many necessary data in BIM models for calculating the green rating and providing feedback for further evaluation. With BIM data support, designers can optimize the building's green design in the very early stages and produce a better solution. By the Bayesian networks support, it can simulate the contribution mechanism of each indicator to the green level. This paper aims to use BIM-BN technology to construct an indicator system specifically for the evaluation of green degree by the case study of building interior decoration, analyze the internal relationship between indicators and its contribution mechanism to the final green level, feed the evaluation results back into the decoration designer to provide technical support for the realization of green decoration. The research results not only help to improve the pertinence of green evaluation of decoration projects, provide a reference for improving green evaluation methods, but also promote the realization of the goals of saving resources, protecting the environment, and improving economic benefits.

# 2. Research Methodology 

### 2.1. Rebuild the Green Evaluation Index System of Building Interior Decoration Based on BIM

The Ministry of Construction of the People's Republic of China first proposed the concept of The Four Saving, One Environmental Protection in the "Green Construction Guideline", released in 2007. The Four Saving, One Environmental Protection means energy saving, land saving, water saving, material saving, and environmental protection. According to the definition and evaluation principle of "The Four Saving, One Environmental Protection" for green buildings, the Assessment standard for green interior decoration (T/CBDA 2-2016) was officially implemented in China on 1 December 2016 [50]. However, T/CBDA 2-2016 only gives the approximate weight of the first-level evaluation indicators (Mainly including: environmental protection, resource conservation, process management, etc.). The second-level indicators are only listed in the form of articles in which corresponding scores are given, and the setting of indicator levels is not clear enough. In addition, some articles are complicated and repetitive, which is not conducive to the development of green decoration evaluation and the promotion of green decoration projects.

In T/CBDA 2-2016, the evaluation components of green decoration include energy conservation and energy utilization, water conservation and water resource utilization, material conservation and material resource utilization, land conservation and space efficient utilization, indoor environmental quality, green construction management, and operation management. Each type of component involves evaluation indexes of control items and scoring items. The evaluation results of control items are either met or not, and the evaluation results of scoring items are scored as numbers. The overall evaluation process is shown in Figure 1. Firstly, experts give the corresponding score for each indicator in T/CBDA 2-2016 according to the submitted project materials and documents. Then the total score will be calculated for all evaluation components based on the experts scoring. After that, the total score of green evaluation of building interior decoration will be recalculated by adding the weights of all evaluation components. Finally, the evaluation grade is determined according to the recalculated total score.

Through an in-depth study of the green evaluation provisions of the green building interior decoration evaluation standard, valuable BIM indicators were selected through the BIM model, BIM schedule, and Ecotect secondary analysis. For example, the basic data of material saving, water saving, energy saving, and indoor air quality could be extracted from the BIM element properties and BIM schedule report. The other basic environmental data, such as indoor thermal, light, acoustic, and space use, could be output by the Ecotech secondary analysis. Figure 2 shows the green evaluation indicator system of building interior decoration based on BIM technology. The weights of each indicator are based on the corresponding weights in the China national standard Assessment standard for green interior decoration (T/CBDA 2-2016).

![img-0.jpeg](img-0.jpeg)

Figure 1. Scoring method for building interior decoration based on green evaluation standards.
![img-1.jpeg](img-1.jpeg)

Figure 2. Green evaluation index system of building interior decoration based on BIM.

# 2.2. Green Evaluation Method of Building Interior Decoration Based on BIM-BN Technology 

Bayesian network (BN) is a combination of graph theory and probability theory, which can be used to describe the dependence between variables. At present, it can be divided into three categories: discrete Bayesian network, continuous Bayesian network, and hybrid Bayesian network. In general, learning Bayesian networks follows a 'five-step' principle: defining node variables, determining node states, BN structure learning, BN parameter learning, and BN inference optimization.

The green degree can be defined as the level of "The Four Saving, One Environmental Protection" of building interior decoration. According to the evaluation grade division principle in green building interior decoration evaluation standard, the ultimate green degree of building interior decoration is divided into four grades from state0 to state3, which the four states corresponding to target nodes in the green evaluation model of

building interior decoration based on BIM-BN technology are constructed as the following Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Evaluation method for building interior decoration based on BIM-BN Technology.
In Figure 3, the BIM index of the interior building decoration green evaluation indicator is defined as the BN node variable. After the quantitative grade of the BIM index is determined as the BN node state, the qualitative relationship between BIM indexes can be determined by BN structure learning, and the quantitative relationship between BIM indexes also can be determined by using BN parameter learning. Therefore, the green evaluation model of building interior decoration based on BIM-BN is constructed. This model-based combination of BIM and BN can then be used to explore the contribution mechanism of green evaluation indicators to the green degree of the project.

# 2.3. Green Evaluation Process of Building Interior Decoration Based on BIM-BN Technology 

For the green goal to be achieved, the combination of BN and BIM can provide evaluation feedback to improve and optimize the design. The BIM can provide parameter data and information for the green evaluation of interior decoration. The BN can provide a breakthrough point for the application of results-oriented theory in the green evaluation of building interior decoration. Its principles of backward reasoning and forward verification can be used to realize not only the green design optimization of interior decoration but also help to reduce the energy consumption of interior decoration.

As the following Figure 4, the green degree evaluation process of interior decoration is divided into two stages: sub-item evaluation and overall evaluation. The former is the basis, and the latter is the purpose. First, all information of the BIM model, BIM schedule, and Ecotect secondary analysis are used to evaluate the green evaluation indicators of the interior decoration project based on BIM. Then the final green degree of the interior decoration is evaluated by the BN model. For the green goal to be achieved, the reasoning function of the BN model is used to improve the design scheme through evaluation feedback and then obtain the optimal design scheme to ensure the realization of green interior decoration and reduce decoration energy consumption.

![img-3.jpeg](img-3.jpeg)

Figure 4. The evaluation process of building interior decoration is based on BIM-BN Technology.

# 3. Implementation of the Green Decoration Assessment Based on BIM-BN Technology 

### 3.1. BIM Model Information for Green Decoration Assessment

In the BIM model, the information can be divided into geometric information and nongeometric information. Geometric information refers to the information of shape, size, and location in the interior and exterior space of the building model, including the length, width, height, coordinate, area, volume, etc., of the components of the BIM model; nongeometric information refers to the general designation of other characteristic reflecting the interior and exterior space of the building model as well as geometric information, including the physical characteristics, technical information, product information and construction of the components Information, maintenance information, etc.

In addition, in order to make better use of BIM model data and information for green evaluation of building interior decoration, it is necessary to follow the corresponding decoration BIM creation standards and clarify the input and output rules of BIM information. According to "Implementation standard for BIM of building decoration engineering" (T/CBDA 3-2016) published in China on 1 December 2016, the additional BIM information includes component name, component code, and component attribute information [51]. The rule of component name is defined as model type-model element name, such as window-aluminum alloy window; the naming rule of component code is material code-Model-Specification-number, such as C-C0910-900 * 1000-01, which corresponds to the material ID number of the local material database; The attribute information can be input as required according to the real information of component material.

Nevertheless, some information and data for green decoration evaluation need to be calculated by BIM sustainability analysis software, such as Ecotect Analysis or Green Building Studio. Consequently, the green decoration evaluation information could be divided into three categories based on the evaluation criteria for green building interior decoration:

1. The information can be stored directly in BIM modeling software, such as "selecting a more water-efficient sanitary appliance." This sort of information can be viewed directly by the BIM visualization function or schedule.
2. The information needs to be analyzed in BIM sustainable software, such as the power density of indoor lighting reaches the target value of architectural lighting design standard of the "General Code for Energy Efficiency and Renewable Energy Application in Buildings" in China [52]; and the lighting of the main operation rooms meets the architectural lighting design standards of "General Code for Building Environment" in China [53]. The acquisition of such information also involves data exchange between different types of software.
3. The information cannot be output by BIM or BIM sustainable software. This kind of green evaluation information can only be obtained through actual measurements or traditional methods, which are sampling and testing the release of harmful substances from the main indoor pollution sources, including materials and furniture. These measurements and methods only aimed to fulfill the requirements of pre-evaluation of indoor pollution in the design stage without taking the comprehensive release rate of formaldehyde and TVOC pollution into consideration.
According to the above classifications, only the first two types of information are based on BIM technology. Both of them will be considered in the green evaluation index of building interior decoration. In addition, other information related to materials, furniture, and equipment should also take attribute information into consideration in BIM modelings, such as brand, model, manufacturer, and specification.

# 3.2. Quantification of Green Evaluation Index of Building Interior Decoration 

Compared with energy conservation and energy utilization, water conservation and water resource utilization, material conservation and material resource utilization, and land conservation and efficient space utilization, residents concentrated on the indoor environment quality which is closely related to their own health. Therefore, in order to ensure that the scope of the research is limited to energy and sustainability, in this paper, only five evaluation elements are selected to evaluate the indoor environment quality, which are the indoor thermal environment, indoor light environment, indoor acoustic environment, indoor wind environment, and indoor air environment.

According to the above five evaluation elements in the China national standard (T/CBDA 2-2016), combined with the analysis characteristics of BIM Technology, the indicators that have a great impact on the green degree of buildings are selected with careful considerations. The quantitative standard corresponding to each indicator in the design stage was further refined to obtain the quantitative level. In the subsequent evaluation process, as long as the quantitative standards are compared, the corresponding index evaluation grade can be determined quickly. Here, indoor environmental quality was chosen as an example to obtain the quantitative grade table of the evaluation indicators (Table 1).

Table 1. The quantitative grade for the index of indoor environmental quality assessment elements.


### 3.3. Formatting of Mathematical Components

The process of constructing a Bayesian network structure normally requires a lot of data for network structure training. However, it is difficult to obtain relatively complete green evaluation data of building interior decoration. Moreover, it is easy to lead to deviation when using incomplete data for research. On the basis of national standards and the relevant literature, the causal relationships between nodes were identified as the preliminary version. The final causal relationships between nodes were determined after conducting expert interviews with 20 design institutes. After that, the Bayesian network model of interior environmental quality assessment of building interior decoration is established, as shown in Figure 5.

![img-4.jpeg](img-4.jpeg)

**Figure 5.** The Bayesian network structure of interior environmental quality assessment of building interior decoration.

In this BN model, the green evaluation index of building interior decoration based on BIM technology is regarded as a node variable, and the quantization level is determined according to the quantization standard of the index system to determine the status of the evidence node and intermediate node. According to the evaluation grade division principle of the evaluation standard for interior decoration of green buildings, each node and target node corresponding to the first level index are divided into four states, among which the worst state is corresponding.

In general, the indoor environmental quality of building interior decoration is affected by the indoor thermal environment, indoor light environment, indoor acoustic environment, indoor wind environment, and indoor air quality. The interaction between the secondary indicators can be clearly found from the constructed Bayesian network diagram of indoor environmental quality evaluation of building interior decoration. Among them, the ratio of window area to floor area and the ratio of ventilation opening area to room floor area affect the proportion of the area where the lighting coefficient meets the requirements; The indoor thermal comfort could be affected by many influencing factors, including the heat transfer coefficient of the external window, the independent control of the heating and air conditioning system end, the ratio of the area of the openable external window and the lighting power density value, the environmental performance of furniture, the additional environmental performance of materials, the ratio of the area of the window to the floor, as

well as indoor thermal comfort, the indoor noise level of main functional rooms, types and quantity of main pollution sources.

# 4. Case Study 

### 4.1. Item Evaluation of Green Degree of Building Interior Decoration Based on BIM

An interior decoration project in Xuzhou, China, was used as a case study. It is a sub-work of residential real estate. The case is one typical apartment on the 6th floor of this project. It is three bedrooms and two living rooms, which are shown in Figure 6. The Ecotect analysis software was selected to simulate and calculate indoor thermal comfort. As shown in Figure 7, it can be seen that the average value of PMV in the chosen building is 0.31 . In the ISO 7730-2005 thermal comfort criteria, the recommended value for the PMV indicator is -0.5 to +0.5 , while PPD is $<10 \%$ [54]. Combined with Chinese conditions and relevant studies, the generally acceptable range of thermal comfort is PMV: $-1.0<$ PMV $<1.0$; the corresponding PPD $<26 \%$. Therefore, for an ordinary room without heating and air conditioning, PMV $=0.3$ represents a comfortable environment. in Figure 8, it can be seen that the average value of PPD is 17.24 , which is also within a reasonable range [54,55]. In conclusion, the indoor thermal comfort index of the building meets the standard. Thus, the indoor thermal comfort value state1 is set to $100 \%$.
![img-5.jpeg](img-5.jpeg)

Figure 6. The BIM plan layout of the apartment as a case study in Xuzhou, China.
The results can also be verified through the window list generated by Revit software (Figure 9): all windows of the case project are made of aluminum alloy glass, and the heat transfer coefficient is more than $2.0 \mathrm{~W} /\left(\mathrm{m}^{2} \cdot \mathrm{k}\right)$. Therefore, it is determined that the external window heat transfer coefficient does not meet the standard requirements. Hence, the value is set to $100 \%$.

![img-6.jpeg](img-6.jpeg)

Figure 7. Thermal comfort PMV analysis results of indoor areas of a decoration project.
![img-7.jpeg](img-7.jpeg)

Figure 8. Analysis results of thermal comfort PPD in each area of a decoration project in Xuzhou.
![img-8.jpeg](img-8.jpeg)

Figure 9. Analysis results of heat transfer coefficient of the exterior window of a decoration project in Xuzhou.

Through the above methods, the final indoor environmental quality sub-evaluation results were obtained (Table 2).

Table 2. Evaluation of indoor environmental quality.


# 4.2. General Assessment of Indoor Environmental Quality 

On the basis of sub-item evaluation, the established Bayesian network model with node condition probability was used for the quantitative evaluation of the indoor environmental quality of the case project, and the evaluation results are shown in Figure 10.
![img-9.jpeg](img-9.jpeg)

Figure 10. Indoor environmental quality evaluation model of a decoration project in Xuzhou.
It can be seen from Figure 10 that the probability value of the indoor thermal environment index of the case project: the probability value of reaching a three-star rating standard is $64 \%$; the probability value of the indoor light environment index reaching a three-star rating standard is $69 \%$; the probability value of the indoor acoustic environment index reaching three-star rating standard is $59 \%$; the probability value of the indoor wind environment index reaching three-star rating standard is $82 \%$; the indoor air quality index reaching the three-star rating standard is $64 \%$. The probability value of the average standard is $67 \%$. Finally, the probability that the indoor environmental quality of the target node does not

meet the green evaluation standard of the decoration project is $15 \%$, the probability of reaching the one-star rating standard is $13 \%$, the probability of reaching the two-star rating standard is $17 \%$, and the probability of reaching the three-star rating standard is $55 \%$.

# 4.3. Optimization Analysis of Indoor Environment Quality 

Based on the current status, the node status of each secondary evaluation index is upgraded by one level. For example, the node value of "Heat transfer coefficient" is changed from "state0 = 100\%" to "state1 = 100\%". It means the designer requires to change the new window glass material, which has lower thermal conduction properties. According to this conception, the Bayesian network model is updated, and the evaluation results are shown in Figure 11. The indoor thermal environment state 3 value increased from $64 \%$ to $79 \%$; the indoor light environment state 3 value increased from $69 \%$ to $78 \%$; the indoor acoustic environment state 3 value increased from $59 \%$ to $68 \%$; the indoor wind environment state 3 value increased from $82 \%$ to $85 \%$; the indoor air quality environment state 3 value increased from $67 \%$ to $81 \%$; the value of state 3 of target node indoor environment quality increased from $55 \%$ to $78 \%$. The state 3 , was $41.82 \%$ higher than the previous design scheme. The data demonstrates that the above optimization scheme is feasible for the indoor environmental quality of building interior decoration.
![img-10.jpeg](img-10.jpeg)

Figure 11. Bayesian network reasoning optimization diagram of indoor environmental quality assessment of a decoration project in Xuzhou.

## 5. Discussion

As an indispensable part of construction projects, interior decoration has an inevitable impact on resource conservation and public health. Nonetheless, the current green decoration faces many practical difficulties with less guarantee. As a big energy-consuming country, it is of great significance for China to research and develop new energy-saving technologies and enhance energy efficiency. Moreover, as the main theme of the development of China's construction industry in the next decade, a series of applications based on BIM has become an irreversible trend.

In the practice of the construction industry, there is still a lot of work for the green evaluation of building interior decoration based on BIM. The existing green evaluation methods that focus on qualitative evaluation seem to relatively rely on the subjective experience of experts. The relationship between the evaluation index and the contribution mechanism of greenness was still not clear. On the other hand, only BIM does not have the evaluation function of green buildings. It needs to add much of information and do

some post-analysis work so that the designer can make simulations and optimization for the design.

Previous studies were often based on the original information type carried out by the BIM model. However, the results of this study show that, to a certain extent, the original information type cannot meet all the requirements of rule checking. For example, the parameter type attributes of BIM model components are basically physical attributes and generally do not include the function-based parameters proposed in the standard. Based on this finding, two methods, individual labeling, and centralized labeling were proposed, which can improve the information content of the model. In addition, this study not only analyzed the properties of the model components but also proposed two algorithms that be used to verify the spatial relationship between the model components. Therefore, this study expands the range of information that the model can respond to rule checking.

However, there are also some limitations to this study. This paper only focuses on the improvement of green evaluation methods for interior environmental quality evaluation indicators of decoration projects that are combined with BIM and the Bayesian network. In the future, continuous improvement of the green evaluation index system should be taken into consideration, as well as the range of research scope. On the other hand, this paper only studied the traditional decoration in green evaluation. However, China is encouraging assembly decoration to replace traditional decoration. In the future, the role of BIM-BN technology in the green evaluation of decoration projects can be discussed from the perspective of assembly and decoration so as to maximize the realization of the "green" level.

# 6. Conclusions 

Considering the urgent need for green decoration and the great potential of BIM technology, this paper tries to build an index system for the green evaluation of interior decoration projects, with emphasis on the internal relationship between the indicators and the contribution mechanism to the final green degree of the project. In addition, this paper also aims to explore a green evaluation method based on BIM and Bayesian network so as to evaluate the design scheme green and evaluate the results. Which could feedback on the design scheme and provide technical support for the realization of green decoration. Thus, the improvement of green evaluation methods could be accomplished by the given references.

First of all, the green evaluation index system of interior decoration projects is established through an in-depth study of relevant standards, specifications, documents, and other information on green evaluation of interior decoration projects. Then, the corresponding quantitative standards of each index are further refined according to the order of five evaluation elements: energy saving and energy utilization, water saving and water resource utilization, materials and materials utilization, efficient utilization of land and space, and indoor environmental quality. Therefore, the quantitative grade is obtained. At the same time, information can be directly stored in BIM modeling software, and BIM sustainable analysis software data exchange functions are also obtained. On the basis of information extraction, the index system of decoration and fitment project based on BIM technology is determined, which provides convenience for the follow-up study of the contribution mechanism and green evaluation method based on the Bayesian network.

Secondly, the evaluation model of four states of target nodes in the green evaluation of building interior decoration based on BIM-BN technology is constructed on the basis of learning the basic theorem and elements of the Bayesian network through the structure learning and parameter learning of the Bayesian network. When using this evaluation model, the forward reasoning optimization and reverse reasoning optimization of the Bayesian network are carried out, respectively, and the results are sorted out. The Qualitative/quantitative relationship between evaluation indexes of the green degree of decoration projects based on BIM technology and the contribution mechanism of each index to the green degree is discovered.

Lastly, a green evaluation method of decoration projects based on BIM- BN technology is proposed by combining BIM technology and Bayesian network effectively with the guiding principle of results-oriented principle. In the design stage, the BIM model, BIM detailed list, and BIM sustainability analysis software are used to evaluate the greenness of interior decoration projects; on this basis, the contribution mechanism and influence path obtained by Bayesian network learning is used to evaluate the overall greenness of decoration and building interior decoration; and based on the evaluation results, the design scheme is reasoned and optimized to quickly lock in the best designer. So as to avoid the blindness of the design scheme and ensure the realization of green decoration.

Author Contributions: Conceptualization, J.Z. and W.F.; methodology, J.Z.; software, W.F.; validation, B.Y. and Y.Z.; formal analysis, W.F. and B.Y.; investigation, B.Y., Q.B. and Y.Z.; resources, J.Z. and W.F.; data curation, W.F. and B.Y.; writing-original draft preparation, W.F., B.Y. and Q.B.; writing review and editing, J.Z., B.Y. and Y.Z.; visualization, W.F., Q.B. and Y.Z.; supervision, J.Z.; project administration, J.Z. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by the National Natural Science Foundation of China (Grant number 72171224) and The Humanities and Social Sciences Foundation of China's Education Ministry (Grant number 19YJAZH122).

Data Availability Statement: Not applicable.
Acknowledgments: The authors sincerely acknowledge the editors and anonymous reviewers for their valuable comments and constructive suggestions, which considerably improved the exposition of this work. The authors also gratefully acknowledge those who provided data and suggestions.
Conflicts of Interest: The authors declare no conflict of interest.
