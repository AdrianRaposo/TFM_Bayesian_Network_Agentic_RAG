# Modelling assessment of farmers workload 

Halina Pawlak ${ }^{1}$, and Piotr Maksym ${ }^{1, *}$<br>${ }^{1}$ University of Life Sciences in Lublin, Faculty of Production Engineering, Departments of Ergonomics, 20-612 Lublin, Gęboka 28. Poland


#### Abstract

The article presents the principles of modeling the physical load assessment of farmers using Bayesian Network technology. Despite rapid development of mechanization and automation of work processes in agriculture, many farmers use their own physical strength, such as manual handling of loads. There are periods in which a farmer performs several or even a dozen of variety activities during the 24 hours. It often happens that all these activities do in a hurry, without rest, working after several hours a day, which further strengthens his physical load. The variety of activities often causes problems with the use indicators to assess the physical load gauges, so Bayesian Network technology was used to develop the evaluation model.


## 1 Introduction

The largest and oldest sector of the economy is agriculture, which employs over 2,2 million people, which accounts for about $15 \%$ of the population employed in Poland [1]. Agriculture is characterized by a large variety of work and a wide range of hazards. Farmers, regardless of season and weather conditions, perform their activities every day, and their duration often extends up to 12-14 hours per day. This situation makes the farmer, in spite of access to modern machinery, puts his work under the pressure of time, fearing the quality and yield of the crop, and the variability of the activities and work places [2].

The farmer's workplace is a house, yard, farm buildings, farmland. Often, these are activities requiring manual handling of loads, elevation work, use of multiple hand tools and machines. Animal care is also an important part of the work. With such a range of tasks and responsibilities, it is important to be aware of the type of activities performed as well as the efficiency and physical strength of the farmer [3,4].

The biggest threat to farmers is still and still the physical load. It appears mainly in manual work where human muscle strength is required. Too long time, perform one action could result in the occurrence of musculoskeletal disorders. This is primarily due to improperly adopted body position, use of tools, ambient conditions and many other significant environmental factors.

Despite the visible technical progress and mechanization of agricultural work, farmers are still exposed to physical load.

The aim of the work is to develop methods to assess the conceptualization of the workload of farmers, in the field of physical load, using Bayesian networks technology.

## 2 Material and Methods

The workload is determined by the knowledge of physical load, mental load and environmental load. Due to the nature of the farmer's work, the physical load was assessed in a particular way. Physical load is understood as a component of the workload, which consists of physical effort, static physical load, and monotype (repeatability activities). Each of these factors, describing physical load, includes some sort of measurement and evaluation uncertainty. The measure of uncertainty is probability, and the description of dependence is the total probability distribution. The calculation scheme is based on the Bayesian formula. Modeling uses Bayesian network technology that enables the expression of cause-and-effect relationships [5-7]. Probabilistic network technology allows for fast, almost automated conversion of expert knowledge, expressed verbally or in natural language, into computer models. Bayesian network is a directed acyclic graph, expressed in the visual with the nodes and directed arcs. Network nodes represent random variables, and arches link nodes to relationships between these variables. Each variable has a strictly defined type and field of values. Each node is associated with a Conditional Probability Table (CPT). Data sources for determining conditional probability distribution may be empirical data or expert judgment. Using this data, you can perform the learning process in order to determine probability distributions for all variables, means network nodes [8-11].

Starting automatic inference mechanisms, the aim of which is to obtain, with an accuracy of probability distribution, the answers to the questions: What grade receives physical load? Which variables affect physical

[^0]
[^0]:    * Corresponding author: piotr.maksym@up.lublin.pl

load? What should be the values of the physical load components to get the desired rating?

## 3 Results

According to the demands of the Bayesian Network technology, firstly there are defined area for the individual components (nodes), secondly network topology is created and then is defined code calculation formulas for determining the nodes assessing physical load.

Attribute "physical load" is evaluated on the basis of "energy expenditure", "monotype" and "static load" (Fig. 1.), whose values are given in Table 1.

The method to assess the physical load on the basis of the sum of points obtained in the evaluation of the attributes that determine the load is used to build the network $[3,12,13]$.

Table 1. Set of attributes values - „physical load".


The assessment of the physical load was based on the principle of energy expenditure assessment used in the simplified Lehmann method. It consists of summing up the energy expenditure defining the position of the body and the involved muscle groups (type of work) during the eight hour shift [14]. Set of attribute values for the "energy expenditure" attribute are shown in tables 2 and 3.

Another attribute that determines "workload" is "monotype", for which attribute values are given in table 4 , and evaluation rules in table 5 .

The severity of work is influenced by static load, which can be a limiting factor of time and correctness of performed work. If the work consists of activities performed at different body positions, the most stressed position should be taken into account when assessing the static load, provided that the duration of this activity is not less than 3 hours $[12,13]$.

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** The network structure of attributes assessment s „physical load“ (own work) where nodes C1 and C2 are constraint (logical) nodes, they allow to introduce dependency constraints on the nodes, for example: between the number of repetitions of movements and the use of force when performing the activity.

The body positions taken into account in the assessment of static load and the way the evaluation are shown in Table 6.

Attribute „physical load“ is evaluated on the basis of the following formula (Fig. 2.).

```
?Physical load?=
If(?Static load?+?Monotype?+?Energy expenditure?<=30,"Very light",
If(?Static load?+?Monotype?+?Energy expenditure?<=70,"Light",
If(?Static load?+?Monotype?+?Energy expenditure?<=120,"Average",
If(?Static load?+?Monotype?+?Energy expenditure?>120,"Heavy","Very heavy"))))
```

**Fig. 2.** Formula code of attribute evaluation of „physical load“ (own work).

The attribute "workload" is evaluated for physical and mental load. The nature of work position at the hand-shuffling operations requires force effort, which is associated with considerable physical load. Thus, in the further inference process the attributes describing this load are taken into account (Fig. 3.).

As shown by the histogram a (Fig. 3.), the probability distribution over the values of the attribute "physical load" indicates the value that determines work in this position as heavy. Therefore, we are interested in which of the attributes influencing the physical load has a significant impact on the value of this load.

With a properly organized work process, the physical load should be set at a very light, light or average level. To make the inference, the least favorable value of this range is assumed, ie "average" - histogram a '(Figure 4.). The assumption will be met when energy expenditure and the static load will be reduced (histogram b', d' Fig. 4.).

![img-1.jpeg](img-1.jpeg)

**Fig. 3.** Evaluation of attribute "physical load" (own work).

![img-2.jpeg](img-2.jpeg)

**Fig. 4.** Evaluation of attribute "physical load" with a priori set value (own work).

The obtained results will be subject to an sensitivity analysis, that can be described as a method which defines how "sensitive" mathematical model really is when the parameters and the overall structure of the model experience changes. Sensitivity analysis allows researchers to find the accuracy needed for an accurate and functional model. That kind of analysis identifies a leverage point in the model and a parameter which specific value can significantly influence the behaviour mode of the system [15, 16]. Another method of the effectiveness that will be taken account is ROC curve, which shows the classification quality of the physical load assessment using sample and test data sets [17].

# 4 Conclusions

The paper presents methods of assessing the physical load of farmers using the formal knowledge representation system.

Based on empirical data and expert opinions, Bayesian Networks could be used to develop a model for assessing the physical load of farmers. Automatic inference makes it possible to get answers to questions What grade receives physical load? Which variables affect physical load? What should be the values of the physical load components to get the desired rating?

The results are often indicative of the hard work of farmers. For example, cereal harvesting - hand-shuffling operations or animal handling activities. The determining factor of workload is the energy expenditure.

The modular Bayesian Network design allows to expand your network, for example with other criteria for assessing workload. The next step of development of the model will be measure of its effectiveness by the mentioned methods.
