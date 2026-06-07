To cite this article: Requejo-Castro, D., Giné-Garriga, R., Pérez-Foguet, A., 2020. Datadriven Bayesian Network modelling to explore the relationships between SDG 6 and the 2030 Agenda. Sci. Total Environ. 710, 136014.

To link to this article: https://doi.org/10.1016/j.scitotenv.2019.136014

# DATA-DRIVEN BAYESIAN NETWORK MODELLING TO EXPLORE 

## THE RELATIONSHIPS BETWEEN SDG 6 AND THE 2030 AGENDA

David Requejo-Castro, Ricard Giné-Garriga, Agustí Pérez-Foguet


#### Abstract

The Sustainable Development Goals (SDGs) are presented as integrated and indivisible. Therefore, for monitoring purposes, conventional indicator-based frameworks need to be combined with approaches that capture and describe the links and interdependencies between the Goals and their targets. In this study, we propose a data-driven Bayesian Network (BN) approach to identify and interpret SDGs interlinkages. We focus our analysis on the interlinkages of SDG 6, related to water and sanitation, across the whole 2030 Agenda. To do this, we use SDGs global available data corresponding to 179 countries, 16 goals, 28 targets and 44 indicators. BN results are analysed and validated by different means. First, we demonstrate the robustness of the BN approach in identifying indicator relationships (i.e. consistent results throughout different country sample sizes). Second, we show the coherency of the results obtained by comparing them with an exhaustive study developed by UN-Water. As an added value, our data-driven approach provides further interlinkages, which are contrasted against the existing literature. We conclude that the approach adopted is useful to accommodate a thorough analysis and interpretation of the complexities and interdependencies of the SDGs.


Keywords: Sustainable Development Goals, SDG 6, Bayesian Networks, interlinkages, data-driven

# 1. Introduction 

On $25^{\text {th }}$ September 2015, the 2030 Agenda resolution announced 17 Sustainable Development Goals (SDGs), remarking their integrated and indivisible nature (United Nations General Assembly, 2015). The SDGs seek to address in a holistic way the three dimensions of sustainable development (SD) environmental, social and economic - and their institutional/governance aspects (Costanza et al., 2016). Lack of integration across these dimensions in development strategies, policies and implementation has long been perceived as a major weakness in previous attempts towards SD, such as in the Millennium Development Goals (MDGs) (Le Blanc, 2015; Liu et al., 2018; Obersteiner et al., 2016). In the SDGs era, more holistic and integrated approaches are needed to elucidate the interdependencies among the different targets and goals, as well as to facilitate their effective implementation.

To date, indicator frameworks have been increasingly recognized as a useful tool for policy making, benchmarking and public communication (Nardo et al., 2005; Singh et al., 2009). They will represent the backbone of monitoring progress towards the SDGs at all levels (i.e. local, national, regional and global). Their assessment will require quality, accessible, timely and reliable disaggregated data from all countries (United Nations General Assmebly, 2015). This, in turn, will require much greater efforts and investments in building national statistical capacities and strengthening statistical quality and standards. However, this challenge comes together with a huge opportunity within the so-called "data revolution" (UN-IEAG, 2014). To date, data collection and harmonization has been assigned to at least one lead technical or specialist agency (SDSN, 2015). Some of these custodian agencies are already elaborating data baselines and reports, and therefore, presenting a starting point for SDGs achievement. This step forward has promoted an emerging catalogue of publications already reviewed elsewhere (Allen et al., 2018), which include indicator-based assessments. An illustrative example is the development of an unofficial SDG Index (Sachs et al., 2018), as a tool to provide indicative country-level estimates and trends, covering 111 and 88 indicators for the OEDC and the 193 UN member countries, respectively. Countries are ranked according to the index values, and those

indicators which require priority attention are identified for each country. Nevertheless, and despite of the likely utility of this approach, indicator-based assessments may fall short on explaining how multiple and interacting forces have led to specific outcomes (Schmalzbauer and Visbeck, 2016). Such assessments, therefore, need to be complemented with analyses that enable interlinkages among targets and indicators to be assessed (Le Blanc, 2015; Allen et al., 2018).

In this sense, the literature shows several contributions that address, to a certain extent, SDGs interlinkages. From a more conceptual and qualitative perspective, SDGs have been read as a network of targets connecting the different goal areas (Le Blanc, 2015), or analysed and presented as a list of relationships (ICSU-ISSC, 2015). They have been also organized through a grading system of interactions (Nilsson et al., 2016), with specific focus on one SDG (Bangert et al., 2017; Coopman et al., 2016; Hall et al., 2018; Herrera, 2019; Singh et al., 2018; UN-ESCAP, 2016), or on a "nexus approach" (e.g. water-energy-food nexus) (Fader et al., 2018; Rasul, 2016; Pahl-Wostl, 2017) with the aim to understand connections, synergies and trade-offs (Liu et al., 2018). On the other hand, from a quantitative point of view, SDGs relationships have been assessed to assist planning and decisionmaking for their implementation by applying sophisticated modelling approaches to evaluate reduced and different sets of Goals (Mainali et al., 2018; Collste et al., 2017; Gao and Bryan, 2017), to assess the (in)consistency of the SDG framework (Spaiser et al., 2017), to simulate and evaluate the interactions among multiple SDG policy options over one specific Goal (Obersteiner et al., 2016), and to introduce stakeholder's knowledge (Khalili et al., 2017; Kanter et al. 2016).

In parallel, Bayesian Networks (BNs) have gained popularity among practitioners (Aguilera et al., 2011; Marcot, 2017; Marcot and Penman, 2019) to explore the interdependencies and cause-effect relationships, simulating complex problems that involve a large number of variables that are highly interlinked. Briefly, BNs are probabilistic graphical models compounded with nodes (variables), links (representing informational or cause-effect relationships) and conditional probability tables (quantification of the dependencies among nodes). BNs flexibility is commonly exploited in scenario simulation and analysis (e.g. Bromley et al., 2005; Dang et al., 2019; Eldridge et al., 2019; GonzalezRedin et al., 2019; Molina et al., 2009), but has also been used to identify the key factors that

influence aspects of interest (Li et al., 2019; Song et al., 2018), to replicate hierarchical composite indicators (Requejo-Castro et al., 2019), or to elucidate the network structure underlying the data-athand, through associated structure learning algorithms (SLA) (Alameddine et al., 2011; Garcia-Prats et al, 2018).

In this study, we propose a data-driven Bayesian Network (BN) approach to identify and interpret SDGs interlinkages. Specifically, we apply SLA to automatically capture those interlinkages spurred on by data. We select SDG 6 on water and sanitation as a case study. We develop a BN model, and we then carry out a comprehensive analysis of achieved results, checking their robustness and validating them through an extensive literature review.

# 2. Case study 

The dedicated goal on water and sanitation has been selected in this study to explore its interlinkages across the 2030 Agenda. SDG 6 reads "to guarantee the availability of water and its sustainable management and sanitation for all" (United Nations General Assembly, 2015), and includes eight targets: six of them are based on outcomes, and two are based on the means of implementation. In more detail, targets 6.1 and 6.2 relate to drinking-water, sanitation and hygiene. Target 6.3 expands the framework beyond the use of sanitation facilities to focus on wastewater and water quality. Targets 6.4 and 6.5 refer to water-use efficiency and water scarcity, and the implementation of Integrated Water Resources Management (IWRM), respectively. Target 6.6 focuses on healthy waterrelated ecosystems. Finally, targets 6.a and 6.b suggest the importance of international cooperation and local stakeholder participation to achieve previous targets.

Main reason for this selection is that an extensive literature puts water and sanitation at the very core of sustainable development (Mugagga and Nabaasa, 2016; Nhamo et al., 2018; United Nations, 2018a; UN-Water, 2016; WWAP, 2019). Available water and adequate sanitation for all and for different purposes are pillars of human health and well-being, thus contributing to the achievement of other development goals such as health, adequate nutrition, gender equality, education and the eradication of poverty (Bartram et al., 2005; Cairncross et al., 2010; Cohen and Sullivan, 2010; Joint Monitoring Programme, 2015; UN-Women, 2018). We seek to capture the bi-directionality of the

interlinkages: incorporating water and sanitation in other Goals is necessary for the achievement of Goal 6, and implementing targets under Goal 6 enables the achievement of a number of other targets across the 2030 Agenda. In doing so, we contribute to the existing applications of BN modelling to the SDG 6. To date, BNs flexibility has been exploited to address the inherent complexity of individual SDG 6 targets, and the literature shows several studies on target 6.1 (Fisher et al., 2015; Cronk and Bartram, 2017; 2018), 6.1 and 6.2 (Dondeynaz et al., 2013; Giné-Garriga et al., 2018; Requejo-Castro et al., 2019) or 6.4 and 6.5 (Mohajerani et al., 2017; Molina et al., 2009; 2013). To the best of our knowledge, however, BNs have not been applied to explore the relationships between targets of different goals.

We take as a reference point the UN-Water Analytical Brief entitled "Water and sanitation interlinkages across the 2030 Agenda for Sustainable Development" (UN-Water, 2016). This report captures the complex nature of the SDGs and gives a qualitative snapshot as far as the relationships between the SDG 6 and the 2030 Agenda, providing an overview of the target-level linkages and their interdependencies (UN-Water, 2016). This report allows comparing the results obtained in our study and validating the proposed data-driven approach.

# 3. Methods 

In this section, we first introduce in detail the criteria and steps followed for data selection and preprocess. Specifically, we focus on the process to select the final set of indicators for the BN analysis - as well as a complete definition of these indicators -, the assumptions made to deal with missing data, and the normalization process for the correct data management. Second, we briefly describe the background underlying this data-driven approach, including the initial settings considered. Third, we describe the steps followed to carry out the BNs analysis.

# 3.1. Data selection and data pre-process 

## Indicator selection

SDGs global available data are provided by the different specialist agencies and published online by the United Nations Statistic Division (UNSD) ${ }^{1}$. In their website, latest official available data for all indicators is published and regularly updated at both the regional and country level. In this study, a first screening of eligible indicators was conducted based on the study developed by UN-Water (2016). This report analyses the relationships between targets of Goal 6 and rest of Goals' targets included in the 2030 Agenda. It comprises 107 outcome-based targets (excluding those related to the means of implementation) and 169 indicators. It provides a summary table of all these linkages, identifying as well whether the link represents a synergy (positive impact) or a conflict (negative impact). The report shows, for instance, the water and sanitation links with those targets related to the reduction of poverty (i.e. SDG targets 1.1, 1.2 and 1.4). In contrast, none of the SDG 6 targets are linked to SDG target 11.5 , which deals with the reduction of deaths and people affected by natural disasters. In order to work with a manageable number of variables, we select those SDG targets showing a high number of synergies and/or conflicts (i.e. 3 or more linkages with SDG 6 targets). However, we have also considered Target 4.2 - related to the access to quality early childhood development, with only two identified linkages with SDG6 -, to represent Goal 4. In doing so, all SDGs reflected in the report are represented in this study with, at least, one target.

In total, 52 SDG targets and 80 associated indicators were analysed. However, global data were only available for 28 out of these $51(55 \%)$ targets and $44(55 \%)$ different indicators (UNSD, 2018). Although no indicators related to the means of implementation were considered, SDG Target 6.a was exceptionally included due to its relevance for the study. Table 1 presents the final list of indicators, their definition, the custodian agency in charge of data reporting, and the number of countries with available information. For each indicator, we also specify how we have dealt with missing data and data normalization (see next section).

[^0]
[^0]:    ${ }^{1}$ Data available at https://unstats.un.org/sdgs/indicators/database.

Table 1. SDG indicators employed in the data-driven Bayesian Network analysis. Source: UNSD, 2018.



* By the time of this study, and for each indicator-country pair, the more recent data were used. When data were obtained from different years, the time period is specified.
Missing data and data gaps have been addressed by applying: a) Regional data, b) HDI groups related information, c) literature review. In some cases, missing data treatment was required for those indicators with more than 179 countries as to reach the final list of countries with information associated with all indicators considered.
${ }^{1}$ : Indicators transformed from the scale "less is better" to "more is better".

The final set of 44 indicators was assessed, to a different extent, in 189 countries. The full dataset of 189 countries and available data for all 44 indicators was extracted from the UNSD database. These countries were classified according to their Human Development Index (HDI) (UNDP, 2018). The purpose of this classification was two-fold. First, it shows the unbiased nature of the sample in terms of countries development context. Second, it assists us in how to deal with missing data. From Table 2, it is observed that a representative number of countries from each HDI group was included. However, only 7 countries have available data for the 44 indicators considered, and more than $50 \%$ of selected countries do not have data for five or more indicators. To increase the final sample of countries, a set of assumptions were made for missing data treatment in the first three groups (referred to the number of indicators with no data available). A total number of 179 countries were finally included in the analysis.

Table 2. Number of countries considered in the study according to their HDI. Sources: UNDP, 2018; UNSD, 2018.


# Imputation of missing data

BNs are only fully functional in absence of missing data. The following assumptions have been considered when dealing with missing data:

- When SDG regional data were available, they were used to fill information gaps at the country level. This assumption applied to $55 \%$ (24 out of 44 ) of the indicators considered (the number of countries using regional data for each indicator varied between indicators).

- When regional data were not available, information gaps were replaced considering country HDI groups (UNDP, 2018) in two different manners. For some indicators, VH HDI countries obtained the highest score (e.g., $0 \%$ of population below the international poverty line of US $\$ 1.90$ per day (SDG 1.1.1); or 0 billion of USD were received as official flows for water supply and sanitation (SDG 6.a.1)). In other indicators, average values were assigned to replace missing data according to HDI group (i.e. very high, high, medium or low). In total, this was applied to $35 \%$ of the indicators within this study (the information gaps varied from one indicator to another).
- Values from the literature were also considered, when available. For example, a value of $1.2 \%$ prevalence of undernourishment rate (SDG indicator 2.1.1) was assumed for VH and H HDI countries with missing data (SDSN, 2016); or 6\% of European urban dwellers living in extremely precarious conditions (UN-Habitat, 2015), which we computed it as proportion of urban population living in slums (SDG indicator 11.1.1). Considerations from existing literature were applied to $10 \%$ of the indicators considered.


# Normalization 

Prior to the BN analysis, indicators were normalized between 0 and 100, with 0 denoting the worst performance and 100 describing the optimum. To do this, those indicators expressed in percentage were kept invariable. On the other hand, the rest of indicators were normalized using "min-max" technique. This method normalizes indicators to have an identical range by subtracting the minimum value and dividing by the range of the indicator values (Nardo et al., 2005). No max-min thresholds were fixed and maximum and minimum values were defined according to the best and worst performance of the indicators, applying logarithms when values were either considerably lower or greater than the rest. Finally, a last transformation was required for several indicators according to "more is better" scale (see Table 1). For instance, SDG indicator 9.4.1 ( $\mathrm{CO}_{2}$ emissions), which represents a "less is better" goal, was assessed by calculating the complementary value. In contrast, similar examples to SDG indicator 7.1.1 (proportion of population with access to electricity),

representing a "more is better" indicator and presented in percentage, were kept constant according to the scale fixed.

# 3.2. Data-driven Bayesian network background and initial settings 

In terms of network construction, BNs can be developed manually or automatically (Aguilera et al., 2013) and, within the latter, a range of SLA (Liu et al., 2017; Madsen et al., 2016) provide the optimum structure of the network (i.e. identification of interlinkages spurred on by data). There are three types of SLA: constraint-based, score-based or a hybrid approach. Briefly, the constraint-based method learns the network structure by analysing the probabilistic relations with conditional independence (C-Ind) tests; while the score-based method assigns a score to each candidate BN and then tries to maximize it with a heuristic search algorithm (Scutari, 2010). In this study, we have opted for the constraint-based SLA since it reduces the subjectivity of the links among the nodes of the network (Requejo-Castro et al., 2019). In addition, despite the large amount of data needed to guarantee the reliability of the C-Ind tests, a recent study points out that constraint-based algorithms are more accurate than score-based algorithms for small sample sizes (Scutari et al., 2018).

In this study, we use the free R software and its package bnlearn (version 4.4), developed by Scutari (2010). This package implements the following constraint-based learning algorithms (Scutari, 2010): grow-shrink (gs), incremental association (iamb), fast incremental association (fast.iamb), interleaved incremental association (inter.iamb) and max-min parent and children (mmpc). We consider that all indicators follow a normal distribution (see Supplementary Material Fig. S1). The C-Ind tests are chosen with respect to this data typology. Avoiding intensive computing time, C-Ind test selection is reduced to linear correlation (cor), Fisher's Z (zf) and mutual information (mi-g) tests (Scutari, 2010). By applying the combination of both SLA and C-Ind tests to the database, 16 candidate networks are obtained.

Scutari et al. (2017) suggest the selection of a single BN model from the data and draw the conclusions from this model, treating it as a "fixed" quantity. However, this model is not "fixed" and it carries its own uncertainty from the selection procedure used to learn it from the data. To reduce this source of uncertainty, we apply the bootstrap technique (re-sampling), which has been largely

used in the determination of confidence intervals (Henderson, 2005). Moreover, this technique has been used to test the stabilities and strength of the links among variables and to obtain the direction of these links (Chao et al., 2018; Scutari et al., 2017).

# 3.3. Data-driven Bayesian Network model generation and analysis settings 

In order to facilitate the implementation of other similar studies (i.e., with a focus on a different SDG), a step-by-step methodology is provided to carry out this data-driven BN analysis. For validation purposes, it is recommended to identify in the literature relevant reference studies. We take as a reference the UN-Water Analytical Brief (UN-Water, 2016), which allows us to compare achieved results and to validate the proposed approach.

The process to develop the analysis is divided in two complementary stages (see Fig.1). The first stage aims to develop a BN model that allows the identification and assessment of the interlinkages between selected targets and indicators. The second stage aims to assess the robustness of the achieved results (i.e. consistency of the interlinkages obtained through the data-driven approach). The step-by-step procedure to construct the BN model (i.e. first stage) from the dataset is as follows:

Stage 1: BN modelling
![img-0.jpeg](img-0.jpeg)

Fig. 1. Process followed to carry out the BN analysis.
A1. SLA + C-Ind test tandem selection. In this initial stage, we apply three selection criteria to identify the most suitable BN network. It should: i) identify a higher number of links associated with the objective nodes (i.e. SDG-6 associated indicators) ii) present a higher number of directed links; and iii) leave a lower number of nodes isolated.

A2. Isolated nodes removal. As these nodes do not contribute to the analysis, they are removed.

A.3. SLA + C-Ind test tandem application. The overall interlinkages $\left(\mathrm{O}_{\mathrm{n}}\right)$ identified by the model are obtained. They are differentiated between directed links $\left(\mathrm{D}_{\mathrm{n}}\right)$, which imply one-way directions, and undirected links $\left(\mathrm{U}_{\mathrm{n}}\right)$, which imply two-ways directions.
A.4. Bootstrap technique application. When applying bootstrap, the so-called strong links $\left(\mathrm{S}_{\mathrm{n}}\right)$ are identified. To do this, data are re-sampled 500 times and the selected tandem SLA + C-Ind test is performed separately on each of the resulting samples, thus collecting 500 networks. Then, the frequency of the links with which each appears in those networks is computed (known as arc strength) and those resulted links that have a frequency above a certain threshold are selected (in this case, a value of 0.80 over 1). Specifically, three are the steps followed: i) computing 100 bootstrapped networks to get a reference list of relationships, ii) selecting those links which are repeated more than $60 \%$ from 100 new bootstrapped networks in comparison to the previous list, and iii) obtaining the directions of the strong links (i.e. cause-effect direction).
A.5. Node of interest extraction. As our focus is on those indicators related to SDG 6, we extract from $\mathrm{O}_{\mathrm{n}}$ those "first order" or "direct" links (Dir-link ${ }_{n}$ ) which associate these indicators with the neighbouring ones. Moreover, we analyze the "second order" links (Indir-link ${ }_{n}$ ), which represent indirect relationships through the above mentioned neighbour indicators.
A.6. Coherency assessment. The interlinkages obtained in the previous step are then contrasted against those ones selected from the literature or based on expert opinion. In our case, we focus our comparative analysis on the UN-Water Analytical Brief (2016), complemented by an extensive literature review.

Regarding the second stage of this analysis, we carry out the following steps:
B.1. Random samples generation $\left(n_{i}\right)$ from the initial number of 179 countries. We opt for the following sample sizes: $175,160,145,130,115,100$ and 85 countries. For each sample size, we generate 100 different networks.
B.2. SLA + C-Ind test and Bootstrap application. For each network associated to each sample size, we apply the selected SLA + C-Ind test tandem (Step A.1) and the bootstrap technique. We then distil the overall relationships $\left(\mathrm{O}_{\mathrm{n}_{\mathrm{i}}}\right)$, the strong links $\left(\mathrm{S}_{\mathrm{n}_{\mathrm{i}}}\right)$ and the "first order" (Dir-link ${ }_{\mathrm{n}_{\mathrm{i}}}$ ) linkages.

B.3. Comparative assessment. Obtained relationships are then compared to the ones identified from the overall sample size. This comparison is complemented with further quality analysis in terms of results coherence.

# 4. Results and Discussion 

In this section, we present and discuss achieved results, relating them to the step-by-step methodology presented above. The objective is three-fold: i) identify the different interlinkages of interest from the overall dataset; ii) test the robustness of the above results by comparing these results against the ones obtained from the different sample sizes; and iii) carry out an in-depth assessment of results regarding the interlinkages between the SDG 6 and the 2030 Agenda.

### 4.1. Identifying interlinkages of interest

The tandem SLA + C-Ind test produced 16 candidate networks. The tandem incremental association (iamb) algorithm and mutual information (mi-g) test showed the best performance - according to the 3 criteria described - and was thus selected for the analysis (Step A.1). Specifically, it identified 23 links associated to SDG 6 indicators and 61 directed links (out of 65). Two nodes with no relationship within the network (6.6.1 and 15.2.1 indicators) were removed (Step A.2). Figure 2 depicts the key elements of this analysis: the overall interlinkages $\left(\mathrm{O}_{\mathrm{n}}\right)$ among SDG indicators are represented by grey dot arrows; and the strong links $\left(\mathrm{S}_{\mathrm{n}}\right)$ and their direction are represented by black solid arrows, as an outcome of bootstrap application (Steps A. 3 and A.4).

![img-1.jpeg](img-1.jpeg)

Fig. 2. Reference network showing the interlinkages between the SDG indicators considered. Corresponding definitions to these indicators can be found in Table 1. This network was obtained through the tandem SLA (iamb) and C-Ind test (mi-g). Three different elements are shown; strong links, $\mathrm{S}_{\mathrm{n}}$ (black solid arrows), directed links, $\mathrm{D}_{\mathrm{n}}$ (grey dot arrows) and undirected links, $\mathrm{U}_{\mathrm{n}}$ (bi-directional red dot arrows).

# 4.2. Testing the data-driven approach robustness 

To demonstrate the robustness of results shown in Fig 2, different random samples were generated (Step B.1). For each sample size and for each of the 100 networks generated, SDG indicators links $\left(\mathrm{O}_{\mathrm{n}}\right)$ were identified together with the strong links $\left(\mathrm{S}_{\mathrm{n}}\right)$ and their direction (Step B.2). Fig. 3 shows how the overall link repetitiveness decreases while reducing the sample size of countries (Step B.3). This decrease appears slightly more pronounced for the samples of $\mathrm{n}=175$ and $\mathrm{n}=160$ countries. When reducing the sample size to 115 countries ( $65 \%$ of the total), the repetitiveness mean value still reaches $71.8 \%$. Maximum and minimum values present unequal fluctuations, but those related to $90^{\text {th }}$ and $10^{\text {th }}$ percentiles show a trend similar to the repetitiveness mean value.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Overall link repetitiveness for the different random samples of countries in comparison to the reference network ( 179 countries and 42 SDG indicators).

As regard those interlinkages identified as strong ones, the same decreasing tendency is observed (Step B.3). For instance, when country sample is reduced at $72 \%(\mathrm{n}=130)$, approximately half of the strong links ( $55 \%, 10$ out of 18 ) are identified in at least $70 \%$ of the bootstrapped networks. This ratio increases to 62,74 and $100 \%$ for the samples of $\mathrm{n}=145,160$ and 175 , respectively (see Supplementary Material Table S1). Two trends are observed. On the one hand, there are strong links presenting a high repetitiveness even if the sample size of countries is reduced drastically. On the other, there are strong links with low repetitiveness when reducing the sample size (see Supplementary Material Table S1). The performance of the model is positively evaluated up to the sample size of 130 countries.

Complementary to this, an in-depth analysis of the direction (i.e. cause-effect direction) of these strong links is carried out. To do this, the strong links are firstly disaggregated considering all of them as undirected, although they are not (see Fig. 2). For instance, the obtained link from 3.9.2 to 3.1.1 is considered from 3.1.1 to 3.9.2 as well. The direction of a link is obtained through the bootstrap technique which assigns a value between 0.5 and 1 , where 0.5 is related to an undirected link and 1.0 assures the direction of the link. Positively, $72 \%$ (13 out of 18 ) of the strong links are identified in one specific direction throughout the different sample sizes (see Supplementary Material Table S2).

However, most of the links present values close to 0.5 , which should be taken carefully before stating a clear cause-effect of the links (see Supplementary Material Table S3).

A further complementary assessment is carried out considering the "first-order" or direct (Dir-link ${ }_{n}$ ) relationships associated with SDG 6 indicators (Step B.3) (see Table 3). In this case, only their frequency is taking into account and not their strength and direction. From the results shown in Table 3, it is observed that, for $\mathrm{n}=130,12$ out of $27(44 \%)$ links are identified in more than $70 \%$ of the bootstrap networks. This value increases up to 60 and $67 \%$ for sample sizes $\mathrm{n}=145$ and 160 , respectively (see full details in Supplementary Material Table S4). Again, two trends are observed. First, there are links which present a high repetitiveness while reducing the sample size (most of them coincide with the links identified as strong). Second, there are relationships whose repetitiveness is reduced rapidly when decreasing the number of countries within the sample. These linkages require special attention for final consideration.

Extending this assessment in terms of quality measures, we analyse the impact of the approach for missing data treatment in model results (Step B.3). We carry out the process described in Section 3 but considering only those countries with 10 or less SDG indicators presenting missing data (see Table 2). Thus, 155 countries are employed for a second BN model construction. Table 6 shows that $78 \%$ (21 out of 27 ) of the links related to SDG-6 indicators are identified in the new model. In addition, $86 \%$ ( 6 out of 7 ) of the strong links are shown. This confirms that the approach employed for fulfilling information gaps has a slight impact on the results achieved.

Table 3. Links identified in relation to SDG-6 indicators, for different country samples.



In bold, strong links.

* Links identified in the second BN model ( 155 countries).
** Links identified in the second BN model but not as strong links.

We analyze in more depth the coherency of the results obtained by constructing the contingency tables associated with the links presented in Table 3 (see also Supplementary Material Table S5). To do this, we discretize the continuous values of the indicators in 5 different intervals. As an example, the relationship between the proportion of population using at least basic drinking water services (6.1.1) and the proportion of population with access to electricity (7.1.1) is considered. This link, identified as strong one, shows a positive correlation according to the values of the diagonal of the table. In other words, an improvement in one of these indicators might generate a similar impact in the other one. This is consistent with the fact that access to drinking water services requires energy for the extraction, treatment and distribution of water. Reciprocally, water is required

to produce all forms of energy to some degree (United Nations 2018a; UN-Water 2016; WWAP 2014).

Summarizing the results presented in this sub-section, it has been demonstrated that the applied datadriven approach provides robust results up to certain sample size (i.e. $\mathrm{n}=130$, which represents approximately $70 \%$ of the overall countries considered). Moreover, the strategy employed for missing data treatment does not impact significantly on the final results and it might be considered as an appropriate approach for other studies. The applied data-driven techniques (SLA + C-Ind test and bootstrapping) allow identifying different kind of links (i.e. strong or not). However, these fall short on identifying specifically the direction (i.e. cause-effect) of the links.

# 4.3. Assessing the SDG-6 interlinkages across the 2030 Agenda 

This sub-section assesses the results achieved with the aim to validate the proposed data-driven approach. To do this, we first compare the results obtained from the data with those presented in the UN-Water Analytical Brief (2016). We do not consider the direction of the links identified within this assessment and we focus on dependencies between the indicators employed. In addition to this, and for each SDG 6 target, we explore both "first order" (Dir-link ${ }_{6}$ ) and "second order" (Indir-link ${ }_{6}$ ) interlinkages identified (Step A.5) to evaluate their coherency with the main findings from an extensive literature review. This sub-section ends with a short recapitulation of results and we give an insight of further applications derived from this data-driven BN approach.

The UN-Water Analytical Brief argues how Goal 6 impregnates the social, environmental and economic dimensions of sustainable development, identifying relationships with all SDGs. From the results depicted in Fig. 4, it is observed that "first order" (direct) interlinkages are identified in relation to Goals on health (SDG 3), gender (5), energy (7), economic growth (8), inequality (10), sustainable cities and communities (11), sustainable consumption and production (12) and terrestrial ecosystems (15). When considering "second order" (indirect) links, identified interdependencies also includes the goals on poverty (1), food (2), infrastructure and industry (9), oceans (14) and peace and security (16). Specifically, 37 out of 42 indicators ( $88 \%$ ) are connected as a result of the BN model generated. Indicators related to the participation rate in organized learning (4.2.2), economic growth

per employee (8.2.1), unemployment rate (8.5.2), passenger volume by air transport (9.1.2) and people affected by a disaster (13.1.1) fall out of the direct and indirect relationships considered (not shown in Fig. 4). These results are summarized in Table 4, including those targets i) identified in both the UN-Water Analytical Brief (2016) and the BN model (considering direct and indirect links), ii) identified within the Analytical Brief but not by the BN model, iii) identified by BN the model but not within the Analytical Brief, and iv) with no information available.
![img-3.jpeg](img-3.jpeg)

Fig. 4. SDG-6 related interlinkages identified. "First order" (Dir-link ${ }_{n}$ ) linkages are represented by solid blue arrows. "Second order" (Indir-link ${ }_{n}$ ) relationships by dot orange arrows.

Table 4. Summary of interlinkages (direct and indirect) associated with SDG-6 in comparison to those ones identified in the UN-Water Analytical Brief (2016).

Links in network but not in Analytical Brief: Universal electricity (T7.1) | Malnutrition (T2.2); Smallscale agricultural productivity (T2.3); Sustainable food production (T2.4); Education for sustainable development (4.7); Gender equality (T5.1, T5.2); Labour rights (T8.8); Sustainable tourism (T8.9); Inequalities (T10.2 \& 10.3); Sustainable urbanization (T11.3); Marine pollution (T14.1); Desertification and loss of biodiversity (T15.3 \& T15.5); Accountability (T16.6)  |


These indicators refer specifically to the access to "at least basic" drinking water and sanitation services. The former relates to improved drinking water sources where collection time is not more than 30 minutes for a round trip (including queuing). The latter refers to improved facilities which are not shared with other households (Joint Monitoring Programme, 2017a).

Considering both "first order" (direct) and "second order" (indirect) interlinkages, the BN model identified, for the case of water, $30 \%$ ( 7 out of 23 ) of the target-level relationships pointed out within the UN-Water Analytical Brief. In contrast, this result rises up to $48 \%$ (11 out of 23 ) for the sanitation-related indicator (see Table 4).

In Table 5, the coherency of the results is expanded and contrasted against the existing literature. Specifically, this comparison is carried out on 3 levels: whether the link identified by the BN model is related to i) a direct relationship, ii) an indirect relationship, and iii) a missed relationship. As regard direct relationships, it is observed the link between both SDG 6 indicators and the links with Goal 3 (health) and Goal 7 (energy). The latter is of particular relevance, as the UN-Water Analytical Brief does not refer to it specifically. However, water is required to produce energy, and vice versa (United Nations, 2018a; UN-Water, 2016; WWAP, 2014). In addition to this, energy is required to treat faecal sludge and wastewater. In turn, it is possible to produce energy from wastewater in the form of heat, biogas and biofuels (United Nations, 2018a; UN-Water, 2016). When considering indirect links, the spectrum of health and energy is expanded to the relationships between access to water and sanitation and Goal 1 (poverty), Goal 5 (gender) and Goal 11 (sustainable cities and communities). For instance, the results show a relationship with the population living below the international poverty line (1.1.1). As pointed by Cohen and Sullivan (2010), there exists a mass of literature which examines the interlinkages between water and poverty from different points of view (e.g. economic assessment, physical accessibility or basic needs perspective). As an illustrative example, access to water (and sanitation) is a component of the Multidimensional Poverty Index formulated by the United Nations Development Programme (Alkire and Jahan, 2018). Additionally, and per definition, SDG 1 includes a target for universal access to basic services (Target

1.4). Another result points at the link with the proportion of seats held by women in national parliaments (5.5.1). The lack of adequate sanitation facilities might expose women and young girls to illness and safety risks, compromising their learning experience (UN-Women, 2018). Thus, it hinders the opportunities to reach professional positions of national responsibility.

From those relationships not identified by the BN model (see Table 4), we acknowledge the absence of the links related to the participation rate in pre-primary school (4.2.2) and the proportion of women in managerial positions (5.5.2), which might be treated together. Women and girls are responsible for water collection in 8 out of 10 households with water off-premises (UN-Women, 2018). In different world regions, if women and young girls reduced the time to collect water, then they would have more time and opportunity to improve their lives through education, paid work and better health (ILO, 2019; Fisher, 2008; UNDP, 2006a; Willetts et al., 2010). Moreover, it would give the opportunity to combat further problems that threaten poor women's well-being (Kevany and Huisingh, 2013). However, it cannot be assumed that increased water access reduces women's workload or strengthens women's empowerment (Ivens, 2008). This implies an unequal sharing of family and household responsibilities, which means that when public services such as education, childcare, water and sanitation are cut back or become less affordable, it is usually women and young girls who fill gap and the overall families who do not enjoy these services (Desai and Alva, 1998; UN-Women, 2018). In addition to this, the BN model does not identify any relationship with Goal 8 (economic growth). Economic growth (8.1.1) and jobs rely on limited environmental resources such as water (ILO, 2018). Specifically, $78 \%$ of the jobs constituting the global workforce are water dependent (WWAP, 2016). Furthermore, the provision of WaSH services at home and in the workplace enables a robust economy by contributing to a healthy and productive population workforce (8.2.1) (WWAP, 2016). Investments in WaSH have paved a path to economic growth and unemployment rates (8.5.2) reduction and new business opportunities appear as a result of policies which address, for example, water (and sanitation) infrastructures (UN-EMG, 2011; WWAP, 2016).

Table 5. Literature review in relation to the relationships identified (i.e. direct and indirect) and missed for the case of SDG Targets 6.1 and 6.2.




# 4.3.2 SDG target 6.4 on water-use efficiency and water stress 

This target includes two indicators which are strongly linked and offer complementary information. On the one hand, indicator 6.4.1 assesses to what extent a country's economic growth is dependent on the use of water resources, representing an economic indicator. On the other hand, indicator 6.4.2 is an environmental indicator, tracking the physical availability of freshwater resources (FAO, 2018). In this case, the BN model identified 15 out of $20(75 \%)$ of the target-level relationships extracted from the UN-Water Analytical Brief, taking into account both direct and indirect links. Similarly to the case of access to water and sanitation, the links identified refer as well to Goals on poverty (1), health (3), gender (5), energy (7) and cities (11). However, in this case, the spectrum of the relationships obtained expands to Goal 12 (sustainable consumption and production), Goal 14 (oceans), Goal 15(terrestrial ecosystems) and Goal 16 (peace and security) (see Table 4).

As in the case of Targets 6.1 and 6.2, Table 6 provides a summary of the academic contributions behind the direct, indirect and missed interlinkages associated with the BN analysis. In this sense, and focusing on the direct links identified, it is observed, for instance, a relationship of water-use efficiency (6.4.1) with the degree of IWRM implementation (6.5.1) and the ODA for water supply and sanitation (6.a.1). Regarding the former, IWRM has been presented during the last decades as the framework to support, among others, the achievement of an efficient use of water (GWP, 2000; UNEP, 2018). According to the latter, Target 6.a advocates expanding international cooperation and capacity-building in water-related activities and programmes, such as water efficiency. In fact, a recent survey to 24 external support agencies show that more than $40 \%$ promote water use efficiency and sustainable withdrawals and $50 \%$ support the implementation of IWRM as "very high" priority areas (GLAAS, 2017). On the other hand, the results show a relationship between water-stress (6.4.2) and the renewable energy share in the total final energy consumption (7.2.1). Water is used for nonrenewable energy generation (e.g. in the extractive industries for producing fuels or for cooling purposes in power plants), but for renewable energy generation as well (e.g. as an input for energy crops or as driving force for hydroelectric turbines) (WWAP, 2014). However, the latter is also identified as a potential conflict, as hydropower and bio-energy might have significant impacts on

land and water resources and ecosystems (UN-Water, 2016). In this study, the tendency of the data employed shows that when the share of renewable energy increases, less countries show water stress (see Supplementary Material Table S5). Another direct link identified is that one associated with the forest area as a proportion of total land area (15.1.1). Natural resources, such as land, have been acquired to satisfied immediate human needs, often at the expense of degrading the environment. Forests have been cleared for intensive agriculture and livestock, and for expanding urban settlements. Water demands associated with these practices, especially irrigation for agriculture, directly affect freshwater supplies and increase water scarcity levels (Foley et al., 2005; Mekonnen and Hoekstra, 2016; United Nations, 2018a). Similar to the previous relationship identified, the tendency of the data used in this study suggests that there is a positive correlation between high rates of forest coverage and low levels of water stress (see Supplementary Material Table S5). In addition to these direct links associated to water-use efficiency (6.4.1) and water stress (6.4.2), we highlight those relationships identified by the BN model and not reflected within the Analytical Brief. For instance, it is observed a link between water-use efficiency (6.4.1) and the essential health service coverage (3.8.1) and, indirectly, to other health-related targets (see Table 6). It is acknowledged that an increase in water-use efficiency makes more water available for drinking and other uses (UNEP, 2018). Access to improved water (and sanitation) represents a tracer indicator for universal health coverage achievement (WHO, 2015b) and is especially useful for monitoring the progressive realization of the right to health (Backman et al., 2008). In the case of water stress (6.4.2), it is observed a direct link with the proportion of women in managerial positions (5.5.2). Although this link has not been addressed within this specific focus, its interdependency has been largely analyzed. Several publications affirm that women's involvement in water management is a key aspect to improving programme and project effectiveness due to women's roles, concerns and priorities in water-related issues (Ivens, 2008) and, thus, balancing the access to the control over resources such as water (Panda, 2007; UNDP, 2006b) and hastening the achievement of sustainability in the management of scarce water resources (GWA, 2003). The data employed in this study suggest that the higher the participation of women is, the lower the water stress is (see Supplementary Material Table S5).

When paying attention to the indirect links, several relationships are provided by the BN model which are not reflected in the Analytical Brief. In particular, it is observed an indirect relationship between water-use efficiency (6.4.1) and maternal mortality (3.1.1), child mortality (3.2.1) and the number of people requiring interventions against neglected tropical diseases (3.3.5). As mentioned previously, an increase in water-use efficiency makes more water available which, in turn, impacts positively in health issues. In the case of water stress (6.4.2), it is observed a relationship with the marine Key Biodiversity Areas (14.5.1). In this sense, it is acknowledged that much of the pollution affecting oceans and coastal zones comes from human activities, such agriculture or industry (United Nations, 2018a). In addition to this, population and economic growth are some of the major drivers that affect and will affect water resources (Ercin and Hoekstra, 2014; Vörösmarty et al., 2000). It is suggested, as well, that in this stress context the protection of marine areas would raise.

Table 6. Literature review in relation to the relationships identified (i.e. direct and indirect) and missed for the case of SGD Target 6.4.

Access to improved water (and sanitation) represents a tracer indicator for universal health coverage achievement (WHO, 2015b)
Useful for monitoring the progressive realization of the human right to health (Backman et al., 2008).  |
It balances the access to the control over resources such as water (Panda, 2007; UNDP, 2006b) and accelerates the achievement of sustainability in scarce water resources management (GWA, 2003)
Higher participation of women is correlated to lower levels of water stress (see Supplementary Material Table S5)  |
More than $40 \%$ and $50 \%$ of surveyed agencies consider, respectively, water use efficiency and sustainable withdrawals and IWRM implementation as "very high" priority areas (GLAAS, 2017)  |
Potential conflict, as hydropower and bio-energy might have significant impacts on land and water resources and ecosystems (UN-Water, 2016)
Tendency of lower levels of water stress when increasing 7.2.1 (see Supplementary Material Table S5)  |




# 4.3.3. SDG target 6.5 on integrated water resources management 

IWRM represents a process-oriented and aspirational target instead of an outcome as the previous ones. Its implementation supports balancing the environmental, social and economic dimensions of sustainable development and achieving all Goals across the 2030 Agenda (UNEP, 2018). Specifically, indicator 6.5.1 refers to the degree of IWRM implementation, which it is assessed through a selfassessed country questionnaire, organized into four main dimensions; enabling environment, institutions and participation, management instruments and financing (UNEP, 2018).

Overall relationships related to the degree of IWRM implementation encompass 33\% (7 out of 21) of the target-level links pointed within the UN-Water Analytical Brief (see Table 4). Even though, IWRM is per definition wide in scope, it should be taken into consideration that, due to the aggregated nature of this indicator, it might mask further potential links. In this case, from Table 7 it is observed that those linkages identified are related to Goal 3 (health), Goal 8 (economic growth), Goal 10 (inequality), Goal 14 (oceans) Goal 15 (terrestrial ecosystems) and Goal 16 (peace and security) (see Table 7).

Unlike the UN-Water Analytical Brief, the BN model show a direct relationship between IWRM (6.5.1) and growth rates inequalities (10.1.1). It is acknowledged that water (and sanitation) is essential to reduce inequalities. IWRM concept calls to "leave no one behind". This highlights overlapping aspects between IWRM and the human rights based-approach to water and sanitation (i.e. equality, equity, participation and governance) (WWAP, 2019).

Indirectly, it is observed a link between IWRM and the coverage of essential health services (3.8.1) and economic growth (8.1.1). These links are not reflected in the Analytical Brief. However, a recent report states the existence of a positive correlation with the Human Development Index (UNEP, 2018), where life expectancy (health) is one of its parameters (UNDP, 2018). Furthermore, it states that wealthier countries present higher degrees of IWRM implementation (UNEP, 2018). The BN analysis shows, as well, a relationship between IWRM and marine KBAs (14.5.1). In general, Key Biodiversity Areas provide a range of ecosystem services (e.g. drinking water) both upstream and

downstream. A key principle of IWRM is that water resources also need to be managed according to hydrological boundaries (UNEP, 2018).

# 4.3.4. SDG target 6.a on international cooperation and capacity-building support 

Unlike previous targets, this one focuses on the means of implementation to achieve SDG 6. Specifically, it assesses the amount of water- and sanitation-related official development assistance (ODA) that is part of a government-coordinated spending plan (6.a.1). Due to fact that there is no room for comparison to the UN-Water Analytical Brief, only the direct links obtained from the BN model are considered to evaluate their coherency.

Interestingly, this indicator shows the highest number of direct links identified (see Table 8). Specifically, these refer to Goal 3 (health), Goal 10 (inequality), Goal 11(sustainable cities and communities) and Goal 12 (sustainable consumption and production). For instance, the BN model shows a link between the ODA (6.a.1) and the maternal mortality (3.1.1) and the number of people requiring interventions against neglected tropical diseases (3.3.5). Relatively, ODA for health has been much greater in countries with highest levels of maternal (and child) mortality (GLAAS, 2017; Pitt et al., 2010). In addition to this, from the data used in this study, the ODA for water and sanitation is greater in countries with higher rates of maternal mortality and more interventions against neglected tropical diseases (see Supplementary Material Table S5). However, some authors considered necessary to increase the share of ODA for NTD control (Liese and Schubert, 2009). Another example points at the relationship with the growth rates inequalities (10.1.1). A recent study states that ODA plays an important role in reducing gender inequalities and rural-urban disparities in social and human development (Ndikumana and Pickbourn, 2017).

Table 7. Literature review in relation to the relationships identified (i.e. direct and indirect) and missed for the case of SGD Target 6.5.



# 4.4. Potential applications in decision-making processes 

Up to this point, we have demonstrated the potentiality of this BN data-driven approach to identify the relationships among global development indicators. In particular, we have presented the coherency of the results obtained comparing them with an exhaustive study developed by UN-Water. As an added value, our data-driven approach provided further linkages, which have been contrasted against the existing literature. As stated previously, understanding these linkages enables the full exploitation of synergies, conflict resolution and trade-offs balances. On the basis of these linkages, integrated planning and management can support decision-making, reduce investment costs and facilitate implementation of a number of strategies that are geared towards sustainable development. Having said this, current data gaps for a number of indicators and countries clearly limit the scope of the study and the lessons learnt. We have tested the robustness of our approach, showing that its performance is positive until a specific side of the sample. Credible data are the lifeblood of decisionmaking (IEAG, 2014), as are needed to underpin sector advocacy, stimulate political commitment and trigger well-placed investment towards optimum health, environment and economic gains (UN-Water, 2016). Moreover, data are the raw material for BN models, since the validity of their outcomes are directly dependant on both data quality and quantity. At present, there are several global initiatives that are monitoring different aspects of the development Agenda, but a coherent framework is missing. To the extent that existing efforts expands to ensure harmonised and integrated monitoring of SDGs, increasing high-quality data availability, it is expected that a wide range of potential uses may emerge in relation to BNs applications.

For instance, the study might focus on the sub-national level where decisions are taken by decentralized administrations. In this sense, the presented approach appears as a flexible tool to be adapted to a specific context. In fact, the 2030 Agenda resolution encourages each Government to set "its own national targets guided by the global level of ambition but taking into account national circumstances" (United Nations General Assembly, 2015). Specifically, it exits the possibility to simulate different scenarios and to infer the impact of potential interventions. To illustrate this idea, and taking as an example Figure 2, different levels of improvement (investments) regarding node

6.2.1 (access to "at least basic" sanitation services) might be simulated (through CPTs modification). Thus, the impacts on immediate nodes 6.1.1 (access to drinking water services), 3.9.2 (mortality rate due to unsafe WaSH ), 3.8.1 (coverage of essential health services) and 7.1.1 (access to electricity) could be evaluated. Similarly, further connected nodes to the latest could be analyzed as well. This requires a shift on the way that potential interventions are assessed, encouraging decision-makers to integrate interdisciplinary perspectives which, in turn, it is essential for sustainable development. In this scenario-based analysis, and considering the difficulty of countries to collect all the information related to the 17 SDGs, BNs might be also especially helpful when there is scarcity or some degree of uncertainty in the data. For example, and following with the same example, if there is no information related to the access to sanitation services, it is possible to set up different hypothesis and assess the potential impacts on associated nodes.

A last potential application of BNs falls on its inverse use (Li et al., 2019; Song et al., 2018; RequejoCastro et al., 2019). Contrary to the methodology in scenario simulation, where one or more nodes can be modified to assess the impact in subsequent nodes, this use allows establishing a desirable value in an objective node and obtaining the new values of connected nodes in order to reach that value. Thus, specific interventions can be design, assess and implement. This possibility might be useful for planning purposes, allowing decision-makers to optimize these interventions in order to achieve the expected results.

# 5. Conclusions 

As per definition, the SDGs are presented as integrated and indivisible. Therefore, conventional indicator-based frameworks need to be combined with innovative approaches for an accurate assessment of interlinkages and interdependencies between targets and indicators. With this in mind, we have tested the validity of a data-driven BN approach to elucidate SDGs interlinkages. In particular, we have applied our approach to explore the relationships of SDG 6 across the 2030 Agenda.

The relevance of the proposed approach and achieved results has been discussed and validated in different means. First, we have demonstrated the robustness of the approach in identifying indicator interlinkages. Specifically, results were consistently obtained up to a sample size of 130 countries. This aspect is particularly important when considering that the results are spurred on by the data used. Furthermore, this sample size represents the potentiality this approach to deal with a relative low amount of data. However, this approach fell short on identifying the cause-effect relationships, which might be of interest and represents a limitation of this approach. In any case, these results might be considered as a potential starting point for further discussion. Second, we have demonstrated the coherency of the results obtained. Taking as a starting point the UN-Water Analytical Brief, we have compared the results provided by the BN model with the main water and sanitation interlinkages on the SDGs identified by this study. On the one hand, our results have reached different levels of coincidence when considering both "first order" (direct) and "second order" (indirect) relationships. Positively, relationships regarding SDG target 6.4 have reached $75 \%$ of coincidence. In contrast, lower levels of concurrence have been obtained for targets $6.1(30 \%), 6.2(48 \%)$ and $6.5(33 \%)$. On the other hand, our analysis has identified other linkages which were not reflected in the UN Water Analytical Brief, which have been positively contrasted against the existing literature. Thus, this result represents an added value of our approach.

We conclude that a data-driven BN approach complements existing approximations, which is neededto increase the understanding and the interpretation of the complexities and interdependencies of the SDGs.

# Continuation of Fig S1. 

![img-6.jpeg](img-6.jpeg)

Table S1. Evolution in the identification of strong links within the different country samples generated. Corresponding definitions to these indicators can be found in Table 1 of the manuscript.


In bold, those interlinkages associated with SDG-6 indicators.

Table S2. Disaggregated identification of all strong links identified for the different country samples. Corresponding definitions to these indicators can be found in Table 1 of the manuscript.


$72 \%$ (13 out of 18) of the strong links are identified in one specific direction throughout the different sample

sizes. The remaining $28 \%$ ( 5 out of 18 ) of the strong links are identified in both directions. Specifically, these links refer to the pairs 3.9.2 - 3.1.1, 3.2.1 - 3.9.2, 6.1.1 - 7.1.1, 9.4.1 - 7.2.1 and 14.4.1 - 15.1.2.2.

Table S3. Strength of the links (arc strength) and their direction. Results are presented as the mean value of 100 bootstrap networks. Corresponding definitions to these indicators can be found in Table 1 of the manuscript.


The direction of the links (i.e. cause-effect direction) is associated to a value, where 0.5 is related to an undirected link and 1.0 to the maximum value, which assures the direction of the link. To this respect, only $31 \%$ (4 out of 13) linkages present values higher than 0.6 . Considering the results presented in Table S2, 28\% (5 out of 18) of the strong links are identified in both directions. This is coherent with the values obtained for their directions, which are close to 0.5 and, thus, fluctuate in the identification of one of the two possible directions.

Table S4. Overall interlinkages identified in relation to SDG-6 indicators for the different country samples generated.

(mortality rate due to unsafe WaSH) | 3.1.1 | Maternal mortality ratio | 100 | 100 | 100 | 86 | 91 | 90  |
(basic drinking water) | 6.2.1 | Population using AT LEAST BASIC sanitation services | 99 | 87 | 70 | 68 | 63 | 60  |
(basic sanitation) | 3.8.1 | Universal health coverage (UHC) | 84 | 80 | 74 | 63 | 60 | 57  |
(water-use efficiency) | 3.8.1 | Universal health coverage (UHC) | 63 | 49 | 27 | 30 | 24 | 29  |
(freshwater withdrawal) | 5.5.2 | Proportion of women in managerial positions | 100 | 100 | 99 | 97 | 94 | 84  |
(IWRM) | 6.4.1 | Water-Use Efficiency | 62 | 52 | 38 | 38 | 32 | 30  |
(cooperation and capacity building) | 3.1.1 | Maternal mortality ratio | 83 | 67 | 63 | 52 | 51 | 38  |

In bold, those interlinkages identified as strong ones.

Table S5. Contingency tables associated with SDG-6 interlinkages identified (3.9.2 indicator is included as well). Results are obtained from the 179 countries considered within this study. Corresponding definitions to these indicators can be found in Table 1 of the manuscript.

SDG 3.9.2: Mortality rate attributed to unsafe water, unsafe sanitation and lack of hygiene



SDG 6.1.1: Proportion of population using AT LEAST BASIC drinking water services



# Continuation of Table S5. 

SDG 6.2.1: Proportion of population using AT LEAST BASIC sanitation services




SDG 6.4.1: Water-Use Efficiency




# Continuation of Table S5. 

SDG 6.4.2: Level of water stress




SDG 6.5.1: Degree of integrated water resources management implementation




# Continuation of Table S5. 

SDG 6.a.1: Total official development assistance for water supply and sanitation


Table S6. Further contingency tables associated with SDG-6 indirect interlinkages identified. Results are obtained from the 179 countries considered within this study.


