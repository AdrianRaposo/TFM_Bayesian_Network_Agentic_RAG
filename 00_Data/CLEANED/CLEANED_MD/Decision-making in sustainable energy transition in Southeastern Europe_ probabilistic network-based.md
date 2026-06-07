# Decision-making in sustainable energy transition in Southeastern Europe: probabilistic network-based model 

Nena Hribar ${ }^{1}$, Goran Šimić ${ }^{2 *}$, Simonida Vukadinović ${ }^{3}$ and Polona Šprajc ${ }^{4}$


#### Abstract

Background: Sustainable energy transition of a country is complex and long-term process, which requires decisionmaking in all stages and at all levels, including a large number of different factors, with different causality. The main objective of this paper is the development of a probabilistic model for decision-making in sustainable energy transition in developing countries of SE Europe. The model will be developed according to the specificities of the countries for which it is intended—SE Europe. These are countries where energy transition is slower and more difficult due to many factors: high degree of uncertainty, low transparency, corruption, investment problems, insufficiently reliable data, lower level of economic development, high level of corruption and untrained human resources. All these factors are making decision-making more challenging and demanding.


Methods: Research was done by using content analysis, artificial intelligence methods, software development method and testing. The model was developed by using MSBNx—Microsoft Research's Bayesian Network Authoring and Evaluation Tool.
Results: Due to the large number of insufficiently clear, but interdependent factors, the model is developed on the principle of probabilistic (Bayesian) networks of factors of interest. The paper presents the first model for supporting decision-making in the field of energy sustainability for the region of Southeastern Europe, which is based on the application of Bayesian Networks.
Conclusion: Testing of the developed model showed certain characteristics, discussed in paper. The application of developed model will make it possible to predict the short-term and long-term consequences that may occur during energy transition by varying these factors. Recommendations are given for further development of the model, based on Bayesian networks.
Keywords: Sustainable energy transition, SE Europe, Decision-making, Bayesian networks

## Background

Sustainable energy transition (SET) is a complex process of multidimensional character [1], at several government levels [2] and with a large number of goals, the most important of which are: reducing energy consumption, increasing energy efficiency, reducing energy production

[^0]from fossil fuels, increasing energy production from renewable sources, reducing emissions of gases that pollute the planet and cause climate change, reducing energy poverty and reducing energy intensity of the economy [3]. The realization of the stated goals is accepted on a global level, but it is implemented with varying success and faces varying challenges [4]. The best results in terms of energy transition are achieved by the European Union, which in early nineties of the twentieth century defined the first precise directions of energy transition, and

[^1]
[^0]:    *Correspondence: gshimic@gmail.com
    ${ }^{2}$ University of Defense in Belgrade, Belgrade, Republic of Serbia Full list of author information is available at the end of the article

[^1]:    (c) The Author(s) 2021. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.

afterwards continued to adopt numerous strategies and action plans with defined way of funding and complex institutional framework [5].

The decision-making process in energy policy in the European Union is, in general, clearly defined and the realization thereof is ongoing, with evident differences in views of policies and pathways among member states [6]. The European Union is recording positive results in terms of sustainable energy transition. In addition, the newest Net zero by 2050 plan (which provides for ambitious targets and the budget) indicates that the European Union remains on track, regardless of the difficulties it faces primarily in relation to disagreements between a certain number of countries about set goals and the ways to achieve them, whereby many of the disagreements fall within the domain of foreign policy and geopolitical change [7].

The ability of sustainable energy transition in developing countries of SE Europe (hereinafter DC of SEE) depends on many different factors that are varying from one country to another [8]. Moreover, there is a causal dependence between these factors, sometimes positive, sometimes negative, from year to year, from one country to another. It implies high level of uncertainty and determines the way of transition model development [9]. There are numerous uncertainties that make the deci-sion-making in the field of sustainable energy transition in SE Europe significantly more difficult, and they can be conditionally divided into three basic groups.

Energy mix obstacles are characterized by the inherited way of a decades-long energy supply in the countries of the region: high dependence on oil and natural gas imports, with natural gas being imported from the Russian Federation as the sole supplier [10]. Furthermore, the largest amount of electricity is produced from thermal and large hydro power plants built decades ago, with outdated technology well-maintained and stable but not environmentally acceptable, and with relatively large network losses [11]. The Western Balkan countries have a particularly difficult energy transition because most electricity and heat energy is generated through coal exploitation, the elimination of which is a complex economic and political issue. Therefore, the transformation of the electricity sector can be considered the most important priority [12]. In addition, the production of energy from renewable sources is at a low level [13].

Obstacles of economic and political nature are reflected in the fact that the countries of SE Europe are at a lower level of economic development, which is not taken into account when determining the degree of energy transition, thus causing tensions, inconsistencies, and slowing the transition process down. This is also the case with other countries of the European Union [14]. Specifically,
a number of countries in the region (primarily the Western Balkan countries which are not members of the European Union) have primarily different development priorities, whereby the investment in sustainable energy transition activities is not high on the list of priorities, nor is it realistically possible in the absence of domestic or foreign investment capital. Some countries in the region are characterized by poor government efficiency, high level of corruption [15], low level (or even lack of transparency and public participation) on the occasion of decision-making in the energy sector, and low level of rule of law in general. Decision-making is particularly sensitive when it comes to countries that require an increased level of trust between all actors, clear and nontransparent decision-making and decision-making that are of interest for political purposes [16]. Resolving existing disputes and strengthening regional cooperation is one of the basic preconditions for the development of the region in every sense, especially in the field of sustainable energy future [17], which is recognized as an important prerequisite for successful implementation of the ELI Green Deal [18].

Obstacles of a methodological nature primarily refer to problems in monitoring, both the monitoring defined by the European Union and the general one. First of all, the European Union changes/innovates strategies relatively often and has a complicated system of policies it adopts; competencies are often unclear-the SET implementation system is complicated in an institutional sense as well [20]. The number of indicators monitored is too large, which results in misleading or even erroneous results that are particularly problematic for making long-term decisions, such as the ones in the field of sustainable energy transition [21, 22]. In the Western Balkan countries there is neither clear nor transparent monitoring system, and the existing one provides limited insight, with obsolete data being more than five years old. Indicator values are unreliable, the indicators are static (they measure data for one year at a time), and SET is a very dynamic process. The influence of individual indicators on SET in general is unclear, as well as is the mutual influence of indicators by type and direction, i.e., it is unclear how strong the influence is, and whether it is positive, negative, or even variable [23]. The type and number of indicators to be used for decision-making is not clearly defined, nor is there a consensus on it [24, 25]. The indicators are often contained in each other, thus causing an overlap which immediately creates a methodological problem and leads to erroneous results [21]. There is a domino effect with changes in indicators, which has been insufficiently examined-all research results in this direction indicate that there are no rules. A special (and so far, unsolvable) problem is the necessity of using GDP

and GDP-based indicators. GDP itself has been subject to numerous criticisms, but there is currently no adequate replacement for it.

Due to the above-mentioned complex specificities and a high degree of uncertainty, it would be necessary for decision-makers in all countries (including the countries of SE Europe) to use mathematical and contemporary IT tools, probability theory and other tools that could make a great contribution to the preliminary analysis of possible events, and thus help make more adequate decisions-which is generally not the case. The introduction of modern tools to support decision-making in the SET sector is at an early stage in the countries of the observed region, but does not even exist in the countries that are not members of the European Union [26].

It should certainly be borne in mind that some countries of SE Europe have not achieved the goals set in the strategic documents, the implementation of which should have already been completed. Namely, according to A European strategy for smart, sustainable and inclusive growth, EU mandated the concrete tasks (targets) related to SET: to reduce greenhouse gas emissions by at least $20 \%$ compared to 1990 levels or by $30 \%$ if the conditions are right, increase the share of renewable energy in final energy consumption to $20 \%$, and achieve a $20 \%$ increase in energy efficiency (20-20-20 target).

Given that the main goal of this paper is of a methodological nature (assessment of the acceptability of Bayesian networks in the process of decision-making about sustainable energy transition in a region characterized by a high degree of uncertainty), the above-mentioned document can be considered valid for research purposes.

## Methods

Bayesian networks (BNs) represent artificial intelligence technology based on Bayesian probability theory. BNs enable modeling of systems with numerous variables that can be interdependent and whose values can have a high degree of uncertainty [27, 28]. BNs represent a directed acyclic graph with nodes reflecting mutually interdependent variables of interest, circumscribed by arcs between these nodes. The quantitative measure of interdependence is expressed by the arrangement of conditional probabilities. It should be emphasized that there are not many studies on the use of BNs on sustainability issues, although they may be considered acceptable, especially in countries with a higher degree of uncertainty [30]. As a special advantage of the use of BNs can be mentioned: consideration of many stressors and endpoints, the possibility of conducting scenario analysis and projections [30-32].

There are various software solutions for BN-based system design. The model presented in the paper was developed using MSBNx—Microsoft Research's Bayesian Network Authoring and Evaluation Tool, in order to enable a successful transition to a sustainable energy sector.

The development of the research model was completed in four stages. First, certain variables (SET indicators) of interest were determined, and the long-term data for the observed countries were thereupon collected. In the next stage, through the analysis of the collected data the behavior of indicators was examined for each observed country in a 10-year period. In the third stage, the obtained results were used, based on which the interdependencies of variables were determined and therefrom a model based on Bayesian networks was defined. In the last stage, the values of probabilistic relations were added to the model as soon as it was made ready for evaluation and use.

The research of the model on which the decisionmaking in sustainable energy transition in SE Europe is conceived, was conducted in a sample of 12 countries, of which 7 are EU Member States (Bulgaria, Greece, Croatia, Hungary, Austria, Romania and Slovenia), and 5 are potential candidates for EU accession (Montenegro, North Macedonia, Albania, Serbia, Bosnia and Herzegovina).

It should be emphasized that Austria is a country that does not belong to the SE Europe region, but it is a neighboring country, so the data for Austria were used in order to get a more realistic picture of the situation and to make a comparison with other countries in the sample.

The data covering the period from 2009 to 2019 were used for processing, and the research included 12 indicators [33]:

1. Share of total energy production from renewable energy sources (RES) (\%)
2. Electricity price (eurocent)
3. Share of fossil fuel (\%)
4. GDP per capita (USdollars per capita)
5. Energy intensity (BTU per USdollars)
6. Energy dependency (\%)
7. Final energy consumption (million tons of oil equivalent (TOE), index $2005=100$ and TOE per capita)
8. Total energy supply (million tons of oil equivalent (Mtoe))
9. Political stability (index)
10. Government efficiency (index)
11. Rule of law (index)
12. Control of corruption (index).

Data for indicators 1 to 8 were obtained from the official Eurostat database, while governance indicators (data for indicators 9 to 12) were obtained from the results of The Worldwide Governance Indicators (WGI) project reports, funded by the World Bank with the aim of establishing a constantly updated database of aggregate and individual governance indicators for over 200 countries and territories [34].

Indicators such as total energy production and total energy import were initially included in order to maintain the principle of parsimony and were replaced by the aggregate parameter total energy supply. For a number of indicators data were only available until 2016, so they were excluded from further consideration (e.g., CO_{2} emission per capita, CO_{2} intensity—MJ or T per GDP). Thus, from the initial set of 21 indicators, 12 indicators listed above were included in the research.

In accordance with the tasks defined by the EU for SET (see Introduction), energy intensity and share of total energy production from RES (Fig. 1) were taken as target (observed) indicators. Target indicators were considered in the model as dependent variables, affected by the remaining 10 indicators (hereinafter referred to as impact indicators). The number of indicators that can be used is large, and the choice of indicators for a particular purpose is often questionable. Based on the results of several surveys conducted for the region of SE Europe and/or the Balkans, the indicators included are in line with the specificities of countries in the sample [35]. It is defined that 6 indicators have a positive impact (green) and 4 indicators have a negative impact (red) on the target indicators.

## Results

Due to the large number of insufficiently clear, but highly interdependent factors, the model will be developed on the principle of probabilistic (Bayesian) networks of factors of interest. The application of this model will make it possible to predict the short-term and long-term consequences that may occur during energy transition by varying these factors.

The initial model presented above (Fig. 1) can be translated without transformations into a probabilistic model based on Bayesian networks. In order for the hypothesis on mutual influence of the presented indicators to be proven, the initial model of Bayesian network (Fig. 2), which includes all indicators, was developed. The model allows to consider and assess the necessary changes to be implemented in different segments of social organization and energy activities, in order to enable a successful transition to a sustainable energy sector.

Indicators are represented by informative and hypothetical nodes. Informative nodes can be of neutral (gray), positive (green), or negative (red) character in relation to hypothetical ones. Hypothetical nodes (blue) are the target nodes—they contain the results of reasoning.

The complexity in terms of the implementation of such a model rests with a large number of indicators and their conditions. If there are n indicators, and if the ith indicator is described by m_{i} conditions, then the total number of combinations for evaluating each of the hypotheses is the multiple of the number of hypotheses N_{h} and the product of the number of conditions in each indicator (Eq. 1):

![img-0.jpeg](img-0.jpeg)

![img-1.jpeg](img-1.jpeg)

**Fig. 2** Bayesian network initial model for SET indicators

$$N_A = N_b \prod_{i=1}^{n} m_i. \tag{1}$$

In the simplest case, if each indicator were described with only 2 conditions, for *n* indicators it would be necessary to determine 2<sup>*n*</sup> of the resulting values for the evaluation of one hypothesis (dependent variable value). In this particular case, the required value is 2 * 2<sup>10</sup>, i.e., the conditions should be defined for 2048 combinations of values of independent variables.

In order to reduce this complexity, the common properties of the indicators were singled out in the second step. Data from the spatial–temporal analysis indicate that there are correlations between impact indicators. This phenomenon is manifested differently for different countries. The correlations with an absolute value of the correlation factor greater than 0.85, are taken as correlations of significance. Owing to a large (10-year) sample, for all correlations p—the value is less than 0.005, which confirms the statistical significance of the results. By observing the SEE countries that are members of the EU (Fig. 3), it can be concluded that there is a pronounced positive correlation between the following indicators:

1. *Final energy consumption* and *total energy supply* (5 out of 7 countries).
2. *Energy intensity* and *share of fossil fuel* (3 out of 7 countries).
3. *Total energy supply* and *share of fossil fuel* (3 out of 7 countries).

And a pronounced negative correlation between the following indicators:

1. *Share of fossil fuel* and *share of RES* (4 out of 7 countries).
2. *Energy intensity* and *GDP per capita* (5 out of 7 countries).

The SEE countries that are not members of the EU reported weaker correlations between the observed indicators (Fig. 4). As with the SEE countries that are members of the EU, there is a strong positive correlation between *final energy consumption* and *total energy supply* indicators (3 out of 5 countries). In addition to this correlation, there are also positive ones between *GDP per capita* and *electricity price* (2 out of 5 countries), and *final energy consumption* and *GDP per capita* (2 out of 5 countries). A negative correlation that may be relevant

![img-2.jpeg](img-2.jpeg)

Fig. 3 Correlation of indicators among EU SEE countries

![img-3.jpeg](img-3.jpeg)

Fig. 4 Correlation of indicators among non-EU SEE countries

exists between GDP per capita and control of corruption indicators (2 out of 5 countries).

When both groups of countries are observed together (Fig. 5), the following positive correlations become more evident:

1. Final energy consumption and total energy supply.
2. GDP per capita and electricity price.
3. Final energy consumption and GDP per capita.

### And negative correlations:

1. Total energy supply and share of RES.
2. Energy intensity and GDP per capita.

![img-4.jpeg](img-4.jpeg)

The detected correlations of indicators were subsequently used to upgrade the initial model shown in Fig. 2. They formed new probabilistic relations in the Bayesian network, which increased the reliability of the network as a platform for the support to decision-making about achievement of transition goals of the observed countries in the energy sector.

The way in which the initial model was expanded is explained on the example of a negative correlation between total energy supply and share of RES indicators. Regardless of the fact that, globally, annual changes in SRES reported the same trend as changes in TES, this is not the case for SEE (Fig. 6). The analysis of the data shows a slight decline in TES during the

![img-5.jpeg](img-5.jpeg)

period from 2010 to 2014. On the other hand, SRES reported growth in the same period, but afterwards (in the period 2014--2017) the situation completely changed: TES began to grow, while SRES stagnated and even declined. Changes in these indicators in the observed period can be explained as representing the consequences of the last economic crisis and the way out of the crisis.

To enable the presentation of the specific influence of TES indicator on SRES indicator, in addition to informative node for SRES indicator (ShareOfEPFromRES) 2 more nodes were added to the Bayesian network model (Fig. 7): a node to describe the current TES change trends (TES_trends), and a target node that is dependent on the previous two nodes and that represents the result of reasoning (SRES_Concluded). This was followed by the distribution of probabilities by target node values (Growing and Declining), for the different values defined for ShareOfEPFromRES and TES_trends nodes.

Distribution was done in three steps. First, the grouping of time series of TES indicators for individual countries was performed, and a linear regression analysis was subsequently applied to them in order to determine TES trends: the trend for each country separately, the group trend for EU member states, the group trend for non-EU countries and the common trend for all 12 countries. In the third step, based on the obtained trends and consultations with SMEs, conditional probabilities were distributed for the observed parameter (SRES_Concluded). According to the same procedure, conditional probabilities were also distributed for other indicators with statistically significant correlations.

![img-6.jpeg](img-6.jpeg)

The final model is shown in the following figure (Fig. 8). For all established correlations, instant nodes (yellow nodes with _Trends suffix) and target (hypothetical) nodes (blue nodes with _Concluded suffix) were added in a causal relationship as explained in the previous two paragraphs. Instant nodes have been used multiple times, given that the two indicators (TES and GDPPC) participate in all the isolated correlations of significance.

In addition to the presented way of developing and designing a model for SET assessment in SEE, based on Bayesian networks, an important result of this paper is usability of the designed model in relation to a specific domain of application. The presented model is scalable—new indicators can be added, existing indicators can be redesigned, new dependencies can be added. In addition, it can be used partially, and parts of the model can be experimented with. Apart from the association presented (EU member states), other associations can be defined on other grounds as well (e.g., neighboring countries, regional initiatives, etc.).

The following experiment illustrates how to use the model (Figs. 9, 10). If an individual country is analyzed, a discrete mode of operation is selected for the informative node Country, and a specific country is selected for analysis. All causally connected nodes change conditional probabilities based on that selection (presented in the assessment tables below the nodes in Fig. 9a). In the experiment, the trend of the TES indicator was varied in order to consider its influence on the behavior of the target indicator SRES. First, the TES was changed to a value decline (TES_Trends), which results in a conclusion that there is a decrease in the share of energy production from renewable sources (P_{SRES_Declining} = 0.614668 at node SRES_Concluded) for the selected country (Fig. 9b). In addition, this change also leads to a decrease in total energy consumption (P_{TEC_Declining} = 0.694117 at node TEC_Concluded).

If the TES trend of change was incline instead of decline (Fig. 10), the share of energy production from renewable sources (P_{SRES_Declining} = 0.421248 at node SRES_Concluded) would increase, and an increase in total energy consumption would be reduced (P_{TEC_Declining} = 0.56013 at node TEC_Concluded).

The second example (Fig. 11) shows the variation in trend of GDP per capita indicator (GDPPC_trends node) in order to realize its influence on the behavior of several target indicators simultaneously (electricity price, energy intensity, control of corruption, total energy consumption). Figure 11a shows the current (initial) state of these indicators. In the case of a slight increase in GDPPC (GDPPC_trends = incline), the conclusion offered by the model (Fig. 11b) indicates probable increase in electricity prices and total energy consumption, as well

![img-7.jpeg](img-7.jpeg)

as better control of corruption, but at the same time reduced increase in *Energy intensity* indicator.

### Discussion

Based on the results of the research, the implications of the findings of this study can be defined in several directions:

### Contribution to the opus of scientific papers in the field of sustainable energy future in the region of Southeast Europe

Namely, most countries in this region have historically been under the influence of the Eastern Bloc in all aspects, including energy development (legislation, infrastructure, supply, social policy, pricing policy, lack of liberal market, inefficient energy use, etc.). The transition to a sustainable energy future, which implies changes in these (and many other aspects) is a complex process that, regardless of its importance for these countries and Europe as a whole, is slow and faces many obstacles. Scientific publications on the above are rare, mostly of a theoretical nature, so this research can be used as a starting point for future research on similar topics.

*Impact on the revision of the existing decision-making process in observed countries* which are often based on non-market principles, the current political situation and with short-term impact. The decision-making process is often non-transparent. The realization of this research enables public insight into the decision-making process that is of special importance for each individual, the economy, the environment, social status and quality of life as a whole.

*Improving the decision-making process by applying advanced decision support tools* because it must be stated that, despite the existence of numerous ways to perform complexes analyzes before making a decision, with main goal to minimize the risk—their application is symbolic in observed region. There are high-quality but outdated traditional decision-making tools and techniques developed for the process of business process management (*SWOT analysis, decision matrix, Pareto analysis, cause and effect or Ishikawa diagram*).

![img-8.jpeg](img-8.jpeg)

Fig. 9 Example of usage of BN model for SET in use—TES declining
![img-9.jpeg](img-9.jpeg)

![img-10.jpeg](img-10.jpeg)

**Fig. 11** BN model for SET in use—consequences of GDP per capita change

*break-even analysis, ratio analysis* and similar). These techniques have their application primarily in business, but for decision-making in terms of strategic planning and complex processes such as the transition to a sustainable energy future, these methods must by no means be the only and/or predominant.

*Implications for policy-makers* They lie in the fact that decision-makers are often insufficiently acquainted with all the specifics they need to make a particular decision. This is understandable and expected because energy policy faces a number of challenges even in stable countries, with a stronger institutional capacity and developed and regularly updated databases. When it comes to the sample countries, in most cases, energy policy is much more complex, vulnerable and subjected to a number of internal and external factors. Big data analysis in a modern environment imposes the use of methods that can describe the cause–effect relationship and capture uncertainty: *neural network, Bayesian network, decision tree, Petri nets* and similar. This research enables the insight into the complexity of decision-making in energy policy, but it also clearly indicates the importance and possibility of reducing, simplifying and presenting the complexity in a form that is understandable for decision-makers who are often not educated in information technology.

*Methodological implications* Primarily refer to the analysis of the methodology used in this research. It can be concluded that joint observation of all countries is useful, but that a benchmark must be set, i.e., a country with which comparison is possible (in this case Austria, as a country with limited energy resources, but with an enviable level of sustainable energy development). The selection of the benchmark country is certainly based on subjective assessment, but comparisons with countries with a very small number of similar starting points in the area under observation should be avoided. In this case, as a key characteristic that determined Austria as a benchmark country, its high dependence on energy imports was chosen, which also characterizes other countries in the sample. In addition, Austria is a country on the edge of the geographical region observed.

Further, research implies importance of selection of the input data used (or to be used) for decision-making. Namely, there is no and is not expected to be a precisely defined list of indicators that should be used for decision-making in the transition toward energy

sustainability. The results obtained in this paper could have implications for further research of a similar type, with the aim of defining the optimal set of indicators for observed countries. In addition, the research implies that certain indicators should be used only for a certain country (or group of countries). This study also implies that use of only one set of indicators for decision-making can be considered useless, inefficient, misleading and with numerous consequences in many governance efficiency implications that arise as a result of this research also indicate the need to introduce and assess the behavior of governance-related indicators (political stability, government efficiency, rule of law and control of corruption), which is difficult to find in the academic literature in this context. On the other hand, these indicators greatly complicate and delay the adoption of certain decisions. In a significant number of cases, decisions made are not in line with a sustainable energy future.

Limitations are an indispensable part that comes as a result of conducting certain research. The implementation of research on the application of Bayesian networks in the decision-making process in countries facing certain political, economic, environmental, social and other uncertainties, showed the presented results, but it is important to point out the limitations observed during the research itself.

First of all, there are limitations in terms of selection and number of indicators, as well as insufficient reliability and availability of input data. Limitations can also be found in insufficiently clearly defined relations that exist between the indicators used; about which there are conflicting views in academia and among policy-makers. Further research should be based on the definition of the relationship among individual (or group) of factors in observed countries, in order to achieve the smallest possible margin of error.

Limitation of Bayesian networks itself refer to the fact that it describes the situation only on the basis of two criteria ("good" or "bad"). Certainly, the possibility of introducing more criteria for describing the condition (for example "medium" or "critical") should be considered, for which this research can serve as a starting point.

Finally, the important limitations are arising from the application of the GDP per capita indicator, as a traditional basic indicator quantifying the level of economic development of a certain country. There are numerous criticisms of this indicator, but so far, a new indicator that would serve as an adequate replacement has not been developed.

## Conclusions

The main goal of the paper is to develop a model to support decision-making in the field of sustainable energy transition under conditions of high uncertainty. The model was tested on a sample of 12 countries of SE Europe (whereby Austria is not part of the region, but the data thereof were used for comparison), for the period from 2009 to 2019.

The model was developed by applying Bayesian networks because they allow decision-making under conditions of high uncertainty, whereby using a large number of indicators that interact with each other, but also with the end result, which in this case is defined by two basic goals of sustainable energy transition of the observed region: share of total energy production from renewable energy sources and energy intensity.

The model was developed in five stages: identification of variables of significance (SET indicators); collection and processing of long-term data for the observed countries; consideration of indicator behavior for each observed country; identification of interdependence of variables; defining of a model based on Bayesian networks and determining probabilistic relations.

The model enables to apply the trends, i.e., the dynamics of indicator behavior in the reasoning process, in addition to the existing knowledge (based on the entered data). The presented way in which trends are included in the model without disturbing the predefined distributions of conditional probabilities, provides for scalability and multiple usability. The model enables monitoring of system dynamics and reveals latent dependencies between SET indicators, which are not noticeable only on the basis of statistical analyses. Experimentation has shown different trends in indicator changes for all countries, even among EU Member States.

In general, the countries of SE Europe that are members of the European Union show better results with regard to state and trend of energy transition, but since monitoring and decision-making process in all countries of SE Europe is fraught with many challenges and uncertainties, they can be observed as a whole in terms of developing models for decision-making under conditions of uncertainties.

The use of a model based on Bayesian networks can be considered an acceptable method for the support to deci-sion-making in matters of sustainable energy transition in the countries of SE Europe. Moreover, bearing in mind the latest EU energy and climate strategies, the uncertainty further increases, so the research results are not limited to the countries and indicators presented, but can also be used in a broader sense. Further research should primarily relate to adaptation of the Bayesian model to each country, in accordance with its specificities and

priorities. On the other hand, there are certain problems that may arise with the application of BNs: selection of adequate number and type of input indicators, inability to predict that the relationship between indicators is variable in individual countries and time periods, ambiguous (yes or no) mode of conclusion. All of the above should be kept in mind and BNs models should be developed in a way to be flexible and tailored in accordance with the specifics of the observed system.

## Acknowledgements

Manuscript has been translated by a professional translator Tanja Paunović, Republic of Serbia.

## Authors' contributions

NH provided the research idea, read, edited and approved the final version. NH, GŠ and PŠ developed the research concept of the paper read, edited and approved the final version. SV participated in data collection and research results, read, edited and approved the final version. GŠ worked on development of Bayesian network model. NH contributed to the explanation of human resources role and choice of related indicators. GŠ and PŠ prepared manuscript draft.

## Funding

Research presented in this manuscript is partially supported by the Ministry of Education, Science and Technological Development under the project MTR44007III. Slovenian Research Agency: Program No. P5-0018—Decision Support Systems in Digital Business.

## Availability of data and materials

All data generated or analyzed during this study are included and cited properly in this published article.

## Declarations

## Ethics approval and consent to participate

Not applicable.

## Consent for publication

Not applicable.

## Competing interests

-The authors declare that they have no competing interests.

## Author details

${ }^{1}$ Iskra Ermeco d. d., Savska loka 4, 4000 Kranj, Slovenia. ${ }^{2}$ University of Defense in Belgrade, Belgrade, Republic of Serbia. ${ }^{3}$ Faculty of Business Economics, Department of Economics and Finance, University Educons, Vojvode Putnika 87, Sremska Kamenica, Republic of Serbia. ${ }^{4}$ Faculty of Organizational Sciences, Department of organization and management, University of Maribor, Kidričeva cesta 55a, Kranj, Slovenia.

Received: 7 September 2021 Accepted: 12 October 2021
Published online: 29 October 2021

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Ready to submit your research? Choose BMC and benefit from:

- fast, convenient online submission
- thorough peer review by experienced researchers in your field
- rapid publication on acceptance
- support for research data, including large and complex data types
- gold Open Access which fosters wider collaboration and increased citations
- maximum visibility for your research: over 100M website views per year

At BMC, research is always in progress.
Learn more biomedcentral.com/submissions