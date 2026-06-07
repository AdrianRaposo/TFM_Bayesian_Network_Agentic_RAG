# Environmental Bioindication Studies by Bayesian Network with Use of Grey Heron as Model Species 

Agnieszka Sujak ${ }^{1} \cdot$ Andrzej Kusz ${ }^{2} \cdot$ Marcin Rymarz ${ }^{1} \cdot$ Ignacy Kitowski ${ }^{3}$


#### Abstract

The article presents a procedure for assessing the quality of the environment, using eggshells of birds as a biomarker implemented into a Bayesian network. An environmental quality index (EQI) was proposed and calculated on the basis of local quality indicators. Experimental data on concentrations of toxic elements in grey heron (Ardea cinerea) eggshells (biomarker of river valleys) were used to determine the empirical variables (nodes) and the probability distributions on the set of these variables. A probabilistic graphical model represents a multitude of relationships between variables in a system that enables the prediction of EQI. The model presented is a useful tool for environmental quality management.


Keywords Environment $\cdot$ Toxic elements $\cdot$ Environmental quality index $\cdot$ Bayesian networks

## 1 Introduction

Biological indices which are frequently created by scientists in order to communicate with non-biologists in many cases provide apparently good objectivity and quantification of environmental issues, especially in small scale applications.

[^0]Unfortunately, in a larger scale and when the chosen parameters are 'location-specific', the output of data after analysis makes the interpretation of indices less effective. Environmental management is a complex process that comprises phases of monitoring, data analysis and undertaking appropriate preventative or remedial actions. Before taking any action, it is necessary to combine the data with expert knowledge and to take into account the relevant elements of uncertainty. Environmental conditions and states (values) of the markers used in their assessment are known to an accuracy of probability distribution. The advantage of Bayesian networks in practical applications is the ability to create models relatively easily, based on different sources of knowledge such as databases or expert knowledge, together with efficient reasoning algorithms based on a combination of graph algorithms and probability. Therefore, we decided to study environmental quality with the use of a probabilistic method such as Bayesian networks.

More and more frequently, one can encounter the use of Bayesian networks in the field of life sciences such as medicine, agriculture, psychology [4, 18, 22, 23, 43] and in environmental science [9, 31]. The individual aspects of ecosystems, both locally and worldwide, have been studied more extensively. Researchers have begun the process of modelling of the environment [41], as well as its response to the processes associated with human activity [40]. In the field of environmental protection, various networks are used to support the information and assessment of decision-making processes related to the management of water resources $[6,10]$, modelling of the development of aquifers [35] and responses to groundwater contamination [10, 17]. Research has been undertaken on the bioaccumulation of nanoparticles of silver in aquatic sediments as a potential threat to the environment [27], as well as the validation of models representing the


[^0]:    Agnieszka Sujak
    agnieszka.sujak@up.lublin.pl

    1 Department of Biophysics, University of Life Sciences in Lublin, Akademicka 13, 20-933 Lublin, Poland
    2 Department of Modelling and Information Systems, University of Life Sciences in Lublin, Doświadczalna 50A, 20-280 Lublin, Poland
    3 State School of Higher Education in Chełm, Pocztowa 54, 22-100 Chełm, Poland

presence of nanoparticles in the environment [26]. Attention has been drawn to water systems, expressing an increase in salinity and to the ecological risk that this phenomenon entails [15]. The introduction of biological markers and their incorporation into Bayesian networks for the construction of environmental reports were important factors in improving the accuracy of environmental risk assessment [32]. New ways of thinking and decisionmaking have also been introduced regarding the protection of species [24], the improvement of the environmental management of rivers [37] and the creation of the Red List of Threatened Species [28].

An important element in creating tools to support the process of environmental management is to find a marker characteristic for the area of environmental research that is unique and easy to access and ensures the right amount of material for analysis. It is important that the object examined is closely linked to the area of observation and that its presence is documented by many years of observations. It should also be connected with the dominant indigenous sources responsible for any environmental degradation. For this paper, we considered the possibility of accumulation of heavy metals and/or trace elements by birds. Typically, environmental studies are based on samples of air, water and soil. In many cases, particularly for the collection of heavy metals, there is a tendency to use animals as biomarkers of the environment [7, $12,25,33,38]$. Various groups of animals, including birds, are used in the monitoring of wetlands due to their specific role as a link in the elements of an ecosystem [36]. Currently, there is an increase of interest in the issue of environmental pollution and in the possibility of using wild birds as a source of information on the content of heavy metals in nature [5, 29]. The use of eggshells as markers of environmental pollution is becoming more frequent $[1,11,16,39]$.

The grey heron (Ardea cinerea) is a species of bird inhabiting Eurasia. This colonially nesting top predator is characterised by longevity and a large population. An important feature of the heron is high mobility and exploitation of a very wide range of vertebrate and invertebrate prey [19], beyond fish, which allows this species to live in a very broad spectrum of different kinds of wetlands [13, 42]. Like other birds, this species has the property of removing toxic elements in the form of deposits in eggshells $[3,16,39]$ or feathers [1, 2]. Colonial living allows massive and non-invasive collection of eggshells and feathers, after completing of reproduction, from under the trees of the breeding colony. This is a big advantage to the bioindication as indicated by many authors [3, 11]. These are the arguments for the choice of eggs of this species as a tool for bioindication of the state of the environment of the Lublin Province of Poland.

The aim of the study was to provide a method of conceptualisation of the problem of environmental quality in the environment of Bayesian networks by defining and creating an environmental quality index (EQI) model based on the measurement of concentrations of heavy metals and trace elements in the eggshells of grey heron from the Lublin Province. This problem has not been studied previously, and there is no data in literature relating to this issue.

## 2 Methodology

### 2.1 Data for the Calculation of EQI

The experimental work consisted of the collection of eggshells of the grey heron from colonies in the Lublin Province, which were analysed for concentrations of 18 trace elements. The details of the experiments as well as the results of those analyses were published previously [20, 21, 34]. For the calculations and construction of the EQI model, 10 elements were chosen (As, $\mathrm{Ba}, \mathrm{Cd}, \mathrm{Cr}, \mathrm{Hg}$, $\mathrm{Ni}, \mathrm{Pb}, \mathrm{Sc}, \mathrm{Sr}$ and V ). Studies comprised of five locations (colonies): Kosmów ( $50^{\circ} 42^{\prime} 32^{\prime \prime} \mathrm{N}, 24^{\circ} 0^{\prime} 29^{\prime \prime}$ E), Stulno ( $51^{\circ} 22^{\prime} 27^{\prime \prime} \mathrm{N}, 23^{\circ} 37^{\prime} 9^{\prime \prime} \mathrm{E}$ ), Wólka Michowska ( $51^{\circ} 33^{\prime}$ $20^{\prime \prime} \mathrm{N}, 22^{\circ} 21^{\prime} 27^{\prime \prime}$ E), Chodlik ( $51^{\circ} 12^{\prime} 40^{\prime \prime} \mathrm{N}, 21^{\circ} 55^{\prime} 5^{\prime \prime}$ E) and Lipsko ( $51^{\circ} 09^{\prime} 30^{\prime \prime} \mathrm{N}, 21^{\circ} 38^{\prime} 57^{\prime \prime} \mathrm{E}$ ), in the Lublin region (East Poland). The grey heron colonies were then grouped into three areas of data collection, based on the similarity of the studied foraging areas: Kosmów-Stulno (Kos_Stu), where the birds foraged in a relatively narrow river valley rich in backwaters; Wólka Michowska-Chodlik (Wm_Chod), where the birds foraged in vast river valleys rich in backwaters and Lipsko (Lip), where the birds en masse preyed on areas of small fish ponds around the colony and small watercourses. In Wólka Michowska-Chodlik, birds did not forage in the fish ponds due to intense hunting pressure.

The value of the EQI assigned to a specific location was determined as the weighted sum of the local quality indices (BIOINDICATOR_i) based on the concentrations of selected elements for $i$ th location.
$\mathrm{EQI}=\sum_{i=1}^{3} w_{\mathrm{i}} \cdot$ BIOINDICATOR_ $i$
where $w_{\mathrm{i}}$ represents the weight of the $i$ th local quality indicator, $w_{\mathrm{i}}>=0, i=1,3$ is the number of locations of data collection and BIOINDICATOR_i represents the value of the $i$ th local quality indicator. On the basis of the area of feeding surface and the number of individual herons in the colonies, the appropriate standardised weights $\left(w_{\mathrm{i}}\right)$ for the locations marked as Kos_Stu,

Wm_Chod and Lip were appointed as $0.4,0.4$ and 0.2 , respectively.
$\sum_{i=1}^{3} w_{\mathrm{i}}=1$
The local quality index assigned to the $i^{\text {th }}$ location was determined as follows:
BIOINDICATOR_ $i=\sum_{j=1}^{10} w_{\mathrm{ij}} \cdot M_{-} i j$,
where $w_{\mathrm{ij}}$ represents the weight of the $j$ th element, $j=1, n$ represents the number of elements taken into account and $M_{-} i j$ represents the value of the concentration of the $j^{\text {th }}$ element. The weights assigned to each of the elements (Table 1) were identical, regardless of the location of colony. The weights $w_{\mathrm{ij}}$ were subjected to normalisation [34]:
$\sum_{j=1}^{10} w_{\mathrm{ij}}=1$

Under these assumptions, the EQI index and the local indices of environmental quality (BIOINDICATOR_ $i$ ) are dimensionless quantities from the interval $[0,1]$. The lower the EQI or BIOINDICATOR_ $i$, the better the quality of the environment. The values of the concentrations of chosen elements $M_{-} i j(\mathrm{j}-1,2 \ldots 10)$ were obtained based on experimental data. For each element, 36 averages from three independent measurements were available, for a total of 108 measurements. In Kos_Stu and Wm_Chod, together, 216 measurements were available for each element, and for the colony Lip, the number of independent measurements amounted to 108. On the basis of these data, the probability distributions over the set of values of individual variables were determined. The measured concentrations of elements (excluding Hg ) were subjected to normalisation by performing linear transformation of data into the interval $[0,1]$ according to the formula:
$M_{-} i j=\left(V A L_{\text {exp }}-V A L_{\min }\right) /\left(V A L_{\max }-V A L_{\min }\right)$
where $M_{-} i j$ represents the value obtained after normalisation, $V A L_{\text {exp }}$ represents the value obtained from experiment, $V A L_{\min }$ represents the minimum value obtained from experiment and $V A L_{\max }$ represents the maximum value obtained from experiment. The normalised data were used for automatic edition of
variables (nodes) representing the concentrations of toxic elements. It was assumed that the variables can take one of the following five values, each represented by an interval $0-0.2$, $0.2-0.4,0.4-0.6,0.6-0.8$ and $0.8-1$.

Table 2 shows an example of the assignment of the elements' concentration values after the process of normalisation and discretisation into five equal intervals for the area representing the Wm_Chod colonies. A similar dependence was determined for Kos_Stu and Lip. The probability distributions over the set of variables representing the normalised environmental markers were empirical distributions designated on the basis of the experimental data. In some intervals, there were no values. In intervals where there were no recorded values, a probability value of 0.0001 was assumed, which was necessary due to the calculation of implemented cumulative data distribution.

It was assumed that the variable representing the concentration of mercury $(\mathrm{Hg})$ had a normal distribution with a low standard deviation $(0.001)$ and the expected values of $0.0,0.5$, 0.7 and 0.9 . The average value of this variable was assigned as a result of logical formula, depending on the observed instances of occurrence of this element and represented in the model by a discrete random variable number_occurrences_Hg. This variable can take five values $(0,1,2,3,4)$ corresponding to the observed number of occurrences of mercury in a specific location.

### 2.2 Bayesian Network Modelling

BaysiaLab v. 5 software (www.bayesia.com), which provides a comprehensive environment for machine learning, knowledge modelling, analytics, simulation and optimisation, was used for the construction of the EQI model. The proposed model is based on the Bayesian network paradigm which involves the possibility of using machine learning methods to build an active network that allows one to study the possible scenarios through the application of the inference methods typical of Bayesian networks $[14,30]$.

All concentrations of elements were expressed in $\mathrm{mg} \times \mathrm{kg}^{-1}$, but the process of normalisation eliminated the impact of scale. The normalisation of variables was integrated with the automatic assignment of a priori probability distributions under the BaysiaLab environment. Figure 1 shows the structure (in the graphical form) of the network used to calculate the value of the EQI in a Bayesian network technology [8].

Table 1 The weights assigned to the elements in the normalisation process


Table 2 The example of normalised variable values and the corresponding ranges of the real concentrations of elements (Wólka Michowska and Chodlik) based on the previously published data $[20,21,34]$


${ }^{a}$ Single value within the interval

Network topology results from the structure of the calculation process. The structure of the network is divided into three subnets representing the three locations of data collection. The final node represents the EQI; the value of which is calculated in accordance with formula (1). Similarly, the values of the variables represented by the nodes with the names BIOINDICATOR_1_Kos_Stu, BIOINDICATOR_ 2_Wm_Chod and BIOINDICATOR_3_Lip are calculated using formula (3). The values assigned to nodes representing the operations of random variables are also random variables, and their values are determined with the accuracy of the
probability distribution. Another network layer represents the raw data input. The values of the variables of this layer represent dimensionless normalised concentrations of individual elements. These variables are marked with the symbol of the element and the location of the colony. Probability distributions of the values of the nodes (except Hg ) were determined automatically. In order to reduce computational complexity, two additional nodes were introduced - Sub_1 and Sub_2. The values in these nodes were calculated on the basis of weights and concentrations of toxic elements. Elements were chosen in such a way that the sum of the weights of these
![img-0.jpeg](img-0.jpeg)

Fig. 1 Structure of the network for the determination of environmental quality index (EQI)

elements was similar, and in total not more than 0.3, Sub_1 integrated data represent the concentration of $\mathrm{Ba}, \mathrm{Cd}, \mathrm{Sc}$ and V , while Sub_2 represents $\mathrm{As}, \mathrm{Cr}, \mathrm{Ni}$ and Sr .

## 3 Bayesian Network Analysis and Validation

Figures 2, 3 and 4 show the distributions of probabilities of occurrence of elements within the intervals representing their concentrations after normalisation and discretisation, as well as distributions of probabilities of values in data collecting nodes (type 'Sub') and distributions of probabilities in nodes marked as BIOINDICATOR_i. A similar distribution of probabilities of the occurrence of Hg was observed for all examined locations, while the distributions of probabilities of Cd were different. In Wm_Chod, the distribution of Cd had the highest probability of obtaining values from the interval $0-0.2$. In Kos_Stu, a high probability of occurrence of Cd from the extreme intervals (that is, $0-0.2(50 \%)$ and $>0.8$ ) was observed. For location Lip, the distribution of Cd attained the highest probability for the interval $0.2-0.4(35.14 \%)$ and the interval $0.4-0.6$ ( $24.32 \%$ ). For that location, the probability of the intervals $<0.2,0.6-0.8$ and $>0.8$ amounted to $13.5,18.92$ and $8.11 \%$, respectively. Mean values for this element amounted to $0.301,0.447$ and 0.441 , respectively, for the locations Wm_Chod, Kos_Stu and Lip. The probability of
distribution of analysed elements contributed to the observed differences in BIOINDICATOR_i. The average values obtained for BIOINDICATOR_i amounted to 0.311 , 0.317 and 0.335 , respectively. The value of the EQI was 0.315 . Considering the range of values that this parameter can take, it is a relatively low value which shows little risk of environmental impact on the surveyed areas, even though the registered Cd values with a fairly large probability ( $46.58 \%$ ) belonged to the highest interval at the location Kos_Stu.

Using the inference mechanisms typical for Bayesian networks, a sensitivity analysis of the model was conducted. Responses of the model to the input data were examined, in particular the sensitivity of the model to extreme changes in the distribution of variables representing the concentrations of metals with the highest and lowest weights. At this stage, both prognostic and backward reasoning were used. In all analysed cases ( 11 different variants), the response of the model to a change in the values of individual variables was considered as correct and consistent with logic and quantitative assessment of these changes, which positively demonstrates the sensitivity of the model.

The response of the model to extreme changes in the distribution of values corresponding to the elements with the highest weights, such as $\mathrm{Hg}, \mathrm{Pb}$ and Cd , was examined at the beginning of validation analysis. First, it was assumed that the concentration of these elements belonged to the interval 0 -
![img-1.jpeg](img-1.jpeg)

Fig. 2 Distribution of probabilities of variables representing normalised concentrations of elements for the location Wm_Chod. All values are dimensionless and belong to the interval $[0,1]$. Calculations based on previously published data $[20,21,34]$

![img-2.jpeg](img-2.jpeg)

Fig. 3 Distribution of probabilities of variables representing normalised concentrations of elements for the location Lip. All values are dimensionless and belong to the interval $[0,1]$. Calculations based on previously published data $[20,21,34]$
0.2 (minimal values). Additionally, the absence of mercury in all locations was assumed (Fig. 5). In response, the model
gave the average EQI value of $0.262 \pm 0.08$. The values in the nodes BIOINDICATOR_i for individual colonies were
![img-3.jpeg](img-3.jpeg)

Fig. 4 Distribution of probabilities of variables representing normalised concentrations of elements for the location Kos_Stu. All values are dimensionless and belong to the interval $[0,1]$. Calculations based on previously published data $[20,21,34]$

![img-4.jpeg](img-4.jpeg)

Fig. 5 Prognostic reasoning for the variant assuming Cd in the interval $0-0.2$ and no occurrences of Hg. All values are dimensionless
located mainly in the intervals between 0.0 and 0.6 but most likely ( $66-83 \%$ ) in the interval range of $0.2-0.4$. The
likelihood of obtaining EQI from the interval of $0.2-0.4$ was $80.74 \%$.
![img-5.jpeg](img-5.jpeg)

Fig. 6 Prognostic reasoning for the variant assuming Pb and Cd in the interval $>0.8$ and the maximal number of occurrences of Hg. All values are dimensionless

![img-6.jpeg](img-6.jpeg)

Fig. 7 Prognostic reasoning for the variant assuming Pb and Cd in the interval $0-0.2$ and no occurrences of Hg for two locations and the concentrations of the above elements in the interval $>0.8$ for the remaining colony accompanied with maximal number of occurrences of Hg

In the next step, it was assumed that the values corresponding to the concentrations of $\mathrm{Hg}, \mathrm{Pb}$ and Cd belong to the interval $>0.8$. In addition, the maximum number of occurrences of mercury in all locations was assumed (Fig. 6). As a result, an increase of the values in the nodes designated as BIOINDICATOR _i was observed. Values for all locations were close to 0.7 , with a maximum probability of values from
the interval $0.6-0.8$ at $86.06,90.42$ and $91.54 \%$, respectively, for the locations Kos_Stu, Wm_Chod and Lip. The EQI value obtained in this case, belonging to the interval $0.6-0.8$ with a probability of $92.72 \%$, was $0.695 \pm 0.054$. From the above validation procedures, it follows that the difference in response of the EQI model to extreme changes in concentration of the most toxic elements amounted to about 0.4 .
![img-7.jpeg](img-7.jpeg)

Fig. 8 Simulation of event-backward reasoning under assumption of EQI value of 0.3 . All values are dimensionless and belong to the interval $[0,1]$

![img-8.jpeg](img-8.jpeg)

Fig. 9 Changes in the value of node Bioindicator_1 depending on the concentration of Pb at different number of occurrences of Hg. Simulation for the location Kos_Stu. All values are dimensionless and belong to the interval $[0,1]$

The response of the EQI model was investigated under the condition that in two locations (Wm_Chod and Lip), the values reflecting $\mathrm{Hg}, \mathrm{Pb}$ and Cd concentrations belonged to the interval $0-0.2$ (minimal values), while in the remaining location (Kos_Stu), the values belonged to the interval $>0.8$ (maximal values) (Fig. 7). Additionally, in Kos_Stu, the maximal number of occurrences of Hg (four instances) was assumed. In Wm_Chod and Lip, the number of occurrences belonged to the interval $0-0.2$. As a response, the increase in the value in the node assigned as BIOINDICATOR_1 $(0.683 \pm 0.073)$ was observed in the location where the increased values of $\mathrm{Hg}, \mathrm{Pb}$ and Cd were set. The values in the nodes BIOINDICATOR_2 and 3 belonged to the interval $0.2-0.4$. The EQI obtained using these values was $0.451 \pm 0.087$, in the interval $0.4-$ 0.6 with a probability of $75.14 \%$.

The operation of the model was additionally checked by the application of backward reasoning (Fig. 8). Initially, an EQI value of 0.3 was assumed. This resulted in a change of the probability distribution in the layer
![img-9.jpeg](img-9.jpeg)

Fig. 10 Relationship between the concentrations of Ba and V for constant, assumed a priori values of the variable Sub_1. Simulation for the location Kos_Stu. All values are dimensionless and belong to the interval $[0,1]$
![img-10.jpeg](img-10.jpeg)

Fig. 11 Relationship between the value of the variable Bioindicator_1 and the values of variables representing the concentration of Hg and Pb at the location Kos_Stu. All values are dimensionless and belong to the interval $[0,1]$
containing nodes assigned as BIOINDICATOR_i. In each node, an increase in the probability of obtaining values from the interval of $0.2-0.4$ was observed. Mean values were $0.302,0.310$ and 0.331 , respectively, for the nodes BIOINDICATOR_1, 2 and 3. Changes in the probability distributions in the nodes representing $\mathrm{Pb}, \mathrm{Cd}$ and Hg (with number of occurrences) were also observed. All locations showed probability distributions in the Pb nodes in the interval $0-0.2$, with a probability higher than $85 \%$. The probability of appearance of Hg in the interval $0-0.2$ was the highest and amounted to over $85 \%$ for all locations. A single instance of occurrence of Hg had a probability of about $9 \%$. The probability of Hg from interval $0.4-0.6$ (imposed EQI value of 0.5 ) was higher than $9 \%$. This indicates the possibility of registering at least one instance of elevated level of Hg at each location examined. Under these assumptions, the probability distribution for Cd was also different for each location. In Wm_Chod and Kos_Stu, the highest probability of Cd was in the interval $0-0.2$, while in Lip, the highest probability of Cd was in the interval of $0.2-0.4$. In response to the predetermined interval for the location Kos_Stu, the probability of occurrence of Cd from the interval $>0.8$ was nearly $45 \%$.

Imposition of the EQI value of 0.7 resulted in an increased probability of higher concentrations of $\mathrm{Hg}, \mathrm{Pb}$ and Cd . The probability of registration of one or more instances of Hg in all locations increased. There was an increase in the probability

of Cd from the highest range of values at the location Kos_Stu, to $89.4 \%$. The above analysis shows that an increase in the value of EQI entails an increase in the probability of $\mathrm{Hg}, \mathrm{Pb}$ and Cd from the highest ranges of concentrations.

Figure 9 shows the relationship between the values in the nodes BIOINDICATOR_1 and values representing the concentration of Pb in the location Kos_Stu for different numbers of occurrences of Hg , assuming that all other variables have values in the interval $0.4-0.6$. Figure 10 shows an example of the relationship between the node representing the concentration of Ba and V , under a permanent value of Sub_1 for Kos_Stu. It was assumed that the other two elements, Sc and Cd, adopt the most probable values. The relationship between the value of the variable BIOINDICATOR_1 and the values adopted by the nodes representing the lower layer with respect to BIOINDICATOR_1 is shown in Fig. 11. For further analysis, the elements with the highest weights, including Hg and Pb , were selected. The highest values of the node BIOINDICATOR_1, 0.611 and 0.606, respectively, were observed at different values of Pb and Hg . Notable are the repetitions of the 0.5 value of the node BIOINDICATOR_1 for Hg and Pb from different intervals. There were dynamic changes in the values of the node BIOINDICATOR_1 at constant values of Hg and Pb belonging to certain intervals.

## 4 Conclusions

The proposed procedure of the assessment of the EQI and the scenarios for the functioning of the model shown within this work provide an example of the calculation process implemented in a Bayesian network. Uncomplicated input of data and sensitivity of the model to possible changes in the distribution of values mean that the proposed method may be of great importance as a tool to support decision-making processes related to management of the environment. The advantages of using Bayesian networks are the following: the determination of the EQI parameter with the accuracy of probability distribution; the possibility of merging data of any type, as the automatic system of determination of distribution of probabilities abolishes the effect of scale and unit; and the possibility of integrating expert knowledge with statistical data. Predictive inference allows the user to analyse all possible solutions depending on the input values. Backward temporal projection allows the user to define the requirements for variables representing the concentration of particular elements by setting the terminal variable (e.g. variables represented by the nodes EQI, BIOINDICATOR or 'Sub'). The proposed model is a
modern and versatile alternative to existing systems used to describe the environment.

Open Access This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http:// creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.
