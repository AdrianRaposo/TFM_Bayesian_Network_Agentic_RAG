# Detecting social-ecological resilience thresholds of cultural landscapes along an urban-rural gradient: a methodological approach based on Bayesian Networks 

C. Arnaiz-Schmitz (1) $\cdot$ P. A. Aguilera (1) $\cdot$<br>R. F. Ropero (1) $\cdot$ M. F. Schmitz (1)<br>Received: 28 December 2022 / Accepted: 12 July 2023 / Published online: 29 July 2023<br>(c) The Author(s) 2023


#### Abstract

Context The difficulty of analysing resilience and threshold responses to changing environmental drivers becomes evident in the social-ecological systems framework due to their inherent complexity. Research is needed to develop new tools able to deal with such challenges and determine potential thresholds for SES variables that primarily influence tipping point behaviour. Objectives In this paper, a methodology based on the application of Bayesian Networks (BNs) has been developed to quantify the social-ecological resilience along an urban-rural gradient in Madrid Region, detecting the tipping point values of the main socioeconomic indicators implying critical transitions at landscape stability thresholds.


[^0]Method To do this, the spatial-temporal trends of the landscape in an urban-rural gradient from Region de Madrid (Spain) were identified, to then quantify the intensity of the changes and explain them using BNs based on regression models. Finally, through inference propagation the thresholds of landscape change were detected.
Results The results obtained for the study area indicate that the most resilient landscapes analysed are those where the traditional silvo-pastoral activity was maintained by elderly people and where there is cohesion between neighbouring rural municipalities.
Conclusion The method developed has allowed us to detect the tipping points from which small changes in socioeconomic indicators generate large changes at the landscape level. We demonstrate that the use of BNs is a useful tool to achieve an integrated socialecological spatial planning.

Keywords Social-ecological planning $\cdot$ Tipping points $\cdot$ Traditional ecological knowledge $\cdot$ Landscape-socioeconomic interactions $\cdot$ Landscape vulnerability $\cdot$ Innovative methodological approach

## Introduction

In the last decades, the studies of social-ecological systems (SES), integrating socioeconomic and ecological dimensions, have increased exponentially. The result of this co-evolutionary adaptation between


[^0]:    C. Arnaiz-Schmitz $\cdot$ M. F. Schmitz

    Department of Biodiversity, Ecology and Evolution, Complutense University of Madrid, Madrid, Spain
    C. Arnaiz-Schmitz ( $\boxtimes$ )

    Complutense University of Madrid, Cuidad Univerisitaria, 28040 Madrid, Spain
    e-mail: caschmitz@ucm.es
    P. A. Aguilera

    Department of Biology and Geology, University of Almería, Almería, Spain
    R. F. Ropero

    Department of Mathematics, University of Almería, Almería, Spain

structures provides a powerful framework for understanding the highly dynamic interactions of social and ecological changes (Liu et al. 2007; Ostrom 2009; Gatzweiler 2014). In these systems, the role of human beings is usually the main driver of changes in the ecological regime, generating alterations of ecosystems such as biological invasions, loss and degradation of habitat, appearance of new diseases and climate change (Allen et al. 2016). In this context, the resilience concept is the central framework that links SES. Resilience is understood as an emerging property of socio-ecosystems that determines ecosystem stability and its ability to increase its capacity to learn and adapt in response to natural or human-induced perturbations (Holling 1973; Lenton et al. 2008). The concept of 'social-ecological resilience' integrates the study of landscape change intensity as a consequence of socioeconomic alterations (Perz et al. 2012; Salvati et al. 2013), since landscape is the result of interactions among society, economy and ecosystems (Lepart and Debussche 1992; Sirami et al. 2010). Quantifying and understanding SES resilience allows to predict and adapt to landscape changes (Hu et al. 2018) and, together with vulnerability to land degradation, is an important tool for sustainable land use planning and decision-making (Salvati et al. 2013).

Resilience and vulnerability represent two related, yet different, approaches to understanding the response of SES to change (Miller et al. 2010). In this sense, vulnerability is defined as the degree to which a system or system component is susceptible to sustaining damage from a hazard (Turner et al. 2003). Vulnerability assessments need to be robust and consider the hazards (perturbations or stressors) that can affect the resilience of the system in question. To identify resilience and vulnerabilities it is also important to detect the complex systems of threshold responses to drivers of change, as well as breakpoints or tipping points that may result in critical effects on a system (Nitschke and Innes 2008; Scheffer et al. 2012; Capon et al. 2015; Reyer et al. 2015). Nevertheless, thresholds are difficult to determine and few empirical studies quantify the amount of disturbance a system can absorb before changing to another state (Walker and Meyers 2004; Renaud et al. 2010; Angeler and Allen 2016). The concept of tipping point was defined by van Nes et al. (2016) as "thresholds of localized effects, including ecological, socio-cultural or economic system properties, which occur when small changes in pressures induce large, abrupt changes in system properties" (SES, in our case). Acceleration is caused by positive feedback driving the system to a new state.

The difficulty of analysing resilience and threshold responses to changing environmental drivers becomes evident in the SES framework due to their inherent complexity. Frequently, the different theoretical interpretations of the concept of socioecological resilience and the existing gap between the theoretical and methodological development to measure it create confusion in its empirical application, which suggests that this area of study still faces some challenges. Including both socioeconomic and natural variables often lead to complicated modelling tasks (different sources of information, metrics, units, among others). Furthermore, the interaction of fast and slow variables between social and ecological systems generates complex dynamics and makes it difficult to identify system thresholds. It is also noteworthy that the development of new technologies allows for a spread in data availability and complexity, which, at the same time, increases the uncertainty inherent to the data and the system. A review of the literature on this topic illustrates the state of the art of social-ecological resilience evaluation and reveals that, in general, the choice of a certain method depends on the context, the availability of the necessary information or the research questions (González-Quintero and Avila-Foucat 2019; Schwind et al. 2016). Most studies use indicators and indices to assess resilience attributes. These approximations have the inherent advantage of being easy to measure, compared to targets that are more difficult to quantify, since they reduce the complexity of a system to a compact and manageable amount of information (Quinlan et al. 2016; Suárez et al. 2016). In cases where resilience is used to understand and predict system changes, dynamic models prove to be a useful tool for simulating complex and dynamic systems that can effectively support programmes and policy design, decision-making processes, outline natural resource management strategies and social learning or help resolve socio-environmental conflicts, among others (Sellberg et al. 2015; Sharifi and Yamagata 2017; Assumma et al. 2020; Datola et al. 2022). The relationship between the quantified resilience of SES and the political aspects related to human well-being

could be of great importance to policymakers (Bene et al. 2011; Franco-Gaviria et al. 2022).

It seems necessary to develop a consistent method to measure the resilience of SES and determine potential thresholds for SES variables that primarily influence tipping point behaviour (González-Quintero and Avila-Foucat 2019; Reyer et al. 2015). Thus, research is needed to develop new tools able to deal with such challenges. In this sense, Bayesian approaches, based on rigorous probabilistic models, have been efficiently applied to SES modelling showing robust results and potential applications in this field (Aguilera et al. 2011; Ropero et al. 2014, 2015). Bayesian Networks (BNs) provide a mathematically consistent framework for SES analysis, in which the graphical representation of model structures and probability distributions are very useful in solving many management questions (McCann et al. 2006). The graphical structure, integrating qualitative and quantitative information, represents a causal model and increases the transparency of the modelling process (Jensen 1996). BNs have proven to be suitable for dealing with problems dominated by uncertainty, an inherent aspect of SES (Franco-Gaviria et al. 2022). Quantifying uncertainty can add substantial perspective to many real-life problems (Uusitalo 2007).

In this paper, a methodology based on the application of Bayesian Networks (BNs) has been developed to quantify the social-ecological resilience along an urban-rural gradient, detecting the tipping point values of the main socioeconomic indicators that imply critical transitions at landscape stability thresholds. The urban-rural gradient paradigm constitutes an appropriate scenario for the study of SES resilience, since as systems subjected to different exploitation pressure, they often exhibit a different status in ecological structure and function (McDonnell et al. 1997; Vizzari and Sigura 2015; Cao et al. 2020). To achieve this objective, the authors used high-resolution, long-term data on land use-land cover and socioeconomic variables, considering the following premises: (i) at a regional scale, SES generate a particular landscape composition and spatial structure, especially noticeable along urban-rural gradients; (ii) the socioeconomic context is one of the main drivers in landscape structure and SES change. In this way, given that resilience is the amount of disturbance that a system can withstand before becoming an alternative stable state, it may be considered that a resilience
landscape is that which maintains its spatial configuration despite socioeconomic changes. The proposed methodology, easily replicable, can be considered as a useful tool for sustainable land planning and management, from a social-ecological perspective.

## Material and methods

Study area

The present study focused on a marked urban-rural gradient of the Madrid Region (Central Spain), identified in previous studies (Arnaiz-Schmitz et al. 2018a). This area covers $2,535 \mathrm{~km}^{2}$ ranging from 400 m asl in the valleys to altitudes of $2,000 \mathrm{~m}$ on the mountain summits and includes 36 municipalities (Fig. 1). The topography divides the landscape into two main sectors associated with different geomorphological dynamics (Schmitz et al. 2007). One-third of the area, to the north and west, is occupied by granitic and gneissic rocks with lithic and dystrict leptosols, and a mountain range exhibiting well-differentiated altitudinal belts with oak and pine forests, upland grasslands and silvo-pastoral uses (Hewitt and Escobar 2011). The remainder area to the centre and east is the sedimentary basin of the Tagus River that originates an agricultural landscape. Traditionally, SES of the area were represented by a rural network of human settlements in which the main activities were related to agriculture and livestock. Nowadays, the region is considered as one of the hotspots in urban development (European Commission 2006; Kuemmerle et al. 2016).

Along the urban-rural gradient studied, there is a clear variation of land use-land cover (LULC), which gives rise to different types of landscape. This gradient assigns its land uses to different activities depending on their environmental characteristics and their degree of connection with the city of Madrid. The traditional use of the municipalities to the north of the gradient, characterized by the mountainous area and high grasses, is linked to livestock activities and contrasts with the south-eastern municipalities that have a highly developed and intensive agricultural sector. In this landscape context, the selected gradient is very useful to visualize the most pronounced changes that have occurred in the study area.

Fig. 1 Location of the urban-rural gradient in Madrid Region (Central Spain). Municipal boundaries, human settlements and main motorways and highways are shown

![img-0.jpeg](img-0.jpeg)

## Database collection

Quantitative information was recorded referring to socioeconomic and LULC data of the 36 municipalities included in the urban-rural gradient: (a) eight LULC types, obtained from pre-existing land use maps (reclassified from CORINE Land Cover Maps for the years 1991 and 2018; Table 1a (b) six landscape metrics (LM) calculated from the same CORINE maps in that temporal scale (Table 1b) (c) fifteen socioeconomic descriptors obtained from the most current public census (IECM, 2009-2018) (Table 2). The socioeconomic period was selected considering that the present values of the socioeconomic variables, able to explain landscape changes (Schmitz et al. 2003; Antrop 2006; De Aranzabal et al. 2008), are the most evident result of past economic activities. As spatial analysis units, the 36 municipalities in the study area have been considered, since they are the smallest governance unit in the Madrid region and also the administrative scale of greater detail in which there are data available from the socioeconomic census and agriculture (Schmitz et al. 2012; Salvati and Serra 2016, among others). Figure 2 summarizes the main steps of the methodological approach followed.

## Landscape metrics calculations

According with McGarigal et al. (2012), six spatially explicit and non-redundant LM were selected (Table 1b). The selection criterion of these spatial metrics was based on their high capacity to describe landscape patterns, ease of interpretation, non-redundancy and comparability (Su et al. 2012; Zhang and Gao 2016; Arnaiz-Schmitz et al. 2018a, b). We used Largest patch index (LPI) as a patch area metric that deal with the size of patches and the amount of edge created by these patches and represents an indirect measure of landscape homogeneity (Herrero-Jáuregui et al. 2019). Edge contrast index (ECON) allowed us to calculate the structural contrast between neighbouring patches types (Kie et al. 2002). Euclidean nearest neighbour distance (ENN), describes the

Table 1 Landscape descriptors (LULC) and metrics (LM) used in the analyses


The values correspond to the total study area, composed of 36 municipalities along the urban-rural gradient. t1 and t2 indicate the values of the variables at the periods of time studied

Table 2 Socioeconomic descriptors used in the analyses


The values correspond to the total study area, composed of 36 municipalities along the urban-rural gradient
degree of spatial isolation of patches and, therefore, the degree of landscape connectivity (Geri et al. 2010). To measure the degree of landscape fragmentation we calculate both Edge density (ED), which inform about the occurrence of ecotones or amount of edge created by the patches present in the landscape, and Splitting index (SPLIT), that is a simple index of
landscape division (Jaeger 2000; Lausch and Herzog 2002; Lasanta et al. 2006). We calculated landscape composition and structure by means of Patch richness density (PRD) that refers to the number or variety of patch types present in a landscape and it is a good indicator of landscape heterogeneity (Nagendra 2002; Arnaiz-Schmitz et al. 2018a).

![img-1.jpeg](img-1.jpeg)

Fig. 2 Outline of the methodological development followed

For the calculation, we used rasterized CORINE Land Cover Maps (years 1991 and 2018), reclassifying land cover classes into the eight LULC types previously selected (Table 1b). Raster maps of the study area were produced and, using a round moving window with a radius of 100 m , a mean value for each spatial metric was calculated at municipal scale. We used ArcGis software V.10.1 (ESRI, 2012) and Fragstats V.4.2 (McGarigal et al. 2012) for the landscape metrics calculation.

## Calculating landscape change intensity

In order to characterize the municipalities of the urban-rural gradient according to their landscape context, a Principal Component Analysis (PCA) was performed using 72 observations ( 36 municipalities at two times, $t_{i}$ ) and 14 variables related to landscape structure (LULC and LM indicated in Table 1). The PCA allowed us to project the municipalities on a plane, whose dimensions represent the main trends in landscape variation over time.

Subsequently, on the PCA plane we calculated the intensity of the landscape change by means of a vector analysis, measuring the modules of change trajectories of municipalities (1).
$\left\|\Delta \overline{D_{j}}\right\|=\sqrt{\left(x_{t_{j}}-x_{t_{j}}\right)^{2}+\left(y_{t_{j}}-y_{t_{j}}\right)^{2}}$,
where, $\Delta \overline{D_{j}}$ refers to the displacement vectors of the coordinates of each municipality $(j)$ on PCA axes from initial time, $t_{i}$, to final time, $t_{f}$. The direction of the vectors in relation to the reference PCA axes allowed us to determine the tendency of change in each municipality.

## Bayesian Networks regression models

Bayesian Networks (BNs) are a statistical multivariate model for a set of variables $X=X_{1} \ldots X_{n}$ explained in terms of two components:

- A qualitative one, defined by means of a directed acyclic graph in which arcs linking nodes determine the (in)dependence relationships among them (Fig. 3a).
- A quantitative one, specified using a conditional distribution $p(x i / p a(x i))$ for each variable $\mathrm{X}_{\mathrm{i}}, \mathrm{i}=1$, $2, \ldots, \mathrm{n}$ given its parents in the graph denoted by $p a(X i)$ (Fig. 3b)

They were originally proposed for handling discrete variables but it is known that environmental

Fig. 3 An example of a discrete Bayesian Network with three binary variables

$$
\begin{aligned}
& P\left(X_{1}=0\right)=0.4 \\
& P\left(X_{2}=0 \mid X_{1}=0\right)=0.4 \\
& P\left(X_{2}=0 \mid X_{1}=1\right)=0.3 \\
& P\left(X_{3}=0 \mid X_{1}=0, X_{2}=0\right)=0.2 \\
& P\left(X_{3}=0 \mid X_{1}=0, X_{2}=1\right)=0.1 \\
& P\left(X_{3}=0 \mid X_{1}=1, X_{2}=0\right)=0.7 \\
& P\left(X_{3}=0 \mid X_{1}=1, X_{2}=1\right)=0.3
\end{aligned}
$$

![img-2.jpeg](img-2.jpeg)
(a) Qualitative component.
(b) Quantitative component.
data often present continuous domains. Even when discretizing them does not always imply a bad solution (Ropero et al. 2018a, b), it often leads to a loss in precision. To avoid discretization, several approaches have been developed. In this paper, the so-called Mixture of Truncated Exponential (MTEs) model was used (for more information see Rumí and Salmerón 2006; Rumí et al. 2006) which consists in splitting the domain of the continuous variable into several intervals, where the corresponding density function is approximated by an exponential function. In that way, standard BNs inference processes can be applied since they are closed under restriction, marginalization and combination. BNs based on MTEs have been successfully used in social-ecological and landscape modelling (Maldonado et al. 2016; Flores et al. 2019).

BNs can have four different aims depending on the number and nature of the target variable(s) (Aguilera et al. 2011). When the focus is set on one target variable, regression (if it is continuous) or classification (when it is discrete) is dealt with. According to the objective of this paper, we selected a set of socioeconomic indicators in order to relate it to landscape change. In this sense, a regression problem emerges
![img-3.jpeg](img-3.jpeg)
(a)
where the features are the socioeconomic indicators selected, and the target variable is landscape change. The methodology applied for a regression model based on BNs is deeply explained in (Ropero et al. 2014).

Since the purpose is to predict the goal variable as precisely as possible, rather than trying to accurately model the joint probability of all the variables, the socalled fixed structures have been developed. The simplest is the Naive Bayes (NB) (Minsky 1961) structure. It consists of a BN with a single root node and a set of feature variables having only the root node as a parent. Its name comes from the fact that the feature variables are independent given the root (Fig. 4a). It is a naive assumption that rarely holds in real problems, as the feature variables may have direct dependencies. Thus, a step beyond is the Tree Augmented Naive Bayes (TAN) structure (Friedman et al. 1997). In this case, each feature is allowed to have one more parent in addition to the target variable. This structure is firstly learnt as a directed tree structure with the feature variables, using the mutual information with respect to the target variable. In the second step, the relationships between the target variable and each
![img-4.jpeg](img-4.jpeg)
(b)

Fig. 4 Structures of Naive Bayes (NB) (a) and Tree Augmented Naive Bayes (TAN) (b)

feature are included (Fig. 4b). These relationships do not have any environmental meaning, and they are there merely to provide a better estimation of the target variable. Both NB and TAN structures allow to include the previous step of variable selection through the learning process following the methodology explained in Ropero et al. (2014). In this way, it is possible to avoid those variables that could introduce noise into the model.

Once models were learnt, root mean square error, rmse (2), was calculated in order to compare them.
$r m s e=\sqrt{\sum_{i=1}^{n} \frac{\left(y_{i}-\overline{y}_{i}\right)^{2}}{n}}$

## Inference propagation

Once the BN regression models are learnt, new information, or evidence, may be included in the model, through the so-called inference process or
probabilistic propagation. If the set of evidenced variables is established as $E$, and their values as $e$, then the inference process consists in calculating the posterior distribution $p\left(x_{i} \mid e\right)$ for each variable of interest (for more information see Ropero et al. (2014). In the present model, the new information or evidence is a total of 10 equidistant points of each feature variable (socioeconomic variables). They were included in the model one by one, and probabilistic propagation was carried out, in such a way that the posterior distribution of the target variable (land use change) was obtained. In order to properly interpret the results, the mean value of this distribution was calculated for each evidence.

## Results

Figure 5 represents the temporal variation of the landscape in the study gradient, analysed by means of PCA. The coordinates of the municipalities are projected on the ordination plane in relation to the two
![img-5.jpeg](img-5.jpeg)

Fig. 5 Coordinates of the municipalities of the urban-rural gradient studied on the PCA plane and trajectories of change in landscape composition and structure. The main landscape indicators (highest factor loadings) are at the ends of the axes. The arrows show the direction of the displacement vectors over
time. The length of the lines indicates the magnitude of the change. Two types of municipalities with different landscape changes are observed: silvo-pastoral systems (light greenshaded area) and agricultural systems (light yellow-shaded area)

main trends of landscape change, expressed by the first two axes of the PCA. These axes jointly explain a large part of the total variability of the data (variance absorption of $62.72 \%$ ). The arrows show the direction of the displacement vectors of each municipality over time. The length and direction of the vectors indicate the intensity of the change that occurred in each case.

The global interpretation of the PCA ordination plane, according to the factor loadings of the landscapes descriptors (Table 3), allows us to detect two types of municipalities in relation to both their composition of land uses and spatial structure, as well as their change trends. Thus, PCA-axis 1 (variance $33.24 \%$ ) differentiates along the urban-rural gradient the municipalities with a rural landscape eminently agricultural, with a spatial structure characterized by large and homogeneous patches related to the intensification of agricultural practices (positive end of the axis) from those that present a heterogeneous landscape, with a more naturalness appearance, mainly characterized by forest systems (negative end of the axis). PCA-axis 2 (variance $29.48 \%$ ) expresses, from bottom to top of the ordination plane, a variation from silvo-pastoral landscapes (traditional pasture systems and dehesas) to areas characterised by fragmentation processes and urban expansion, linked to the abandonment of the rural land use system. The

Table 3 Factor loadings of the landscape descriptors (LULC and LM) on PCA-Axes


agricultural group of municipalities is geographically located in the S-SE zone of the urban-rural gradient, while the silvo-pastoral one is in the W-NW zone (Fig. 1).

The vector calculation on the ordination plane allowed us to determine that the silvo-pastoral landscapes (left end of the plane) tend to change unidirectional and intensely (direction and magnitude of the arrows, respectively) towards the abandonment of traditional land use systems and urban expansion. On the contrary, the magnitude of the change in landscapes with an agricultural vocation (extreme right of the plane) is less, evolving towards two types of situations: agricultural intensification or urban transformation.

Based on these results, and with the aim of testing the usefulness of Bayesian Networks as a methodological tool to detect thresholds or tipping points in landscape change trends, we focus on the group of municipalities in which a greatest spatial-temporal change has been identified (i.e., the silvo-pastoral systems of the studied gradient). To build the networks, we created a data matrix in which the intensity of landscape change, calculated using vector Eq. (1) on coordinates of PCA plane, acts as the target variable, while the characteristic variables are those different socioeconomic ones which were previously obtained. For this model, four structures were learnt, NB and TAN and their alternatives with variable selection (SNB, STAN). A comparison among them was carried out, in order to ascertain the best model in terms of error rate. Results are shown in Table 4. In all cases, TAN structure with a variable selection (STAN) is the best option.

We used BNs model using the fixed structure TAN with variable selection (STAN) to calculate the threshold of landscape transformation. Table 5 shows the variables selected by the STAN model. To detect inflection points, the values of the variables were resized by ten equidistant points based on their maximum and minimum values. These values were

Table 4 Comparison in terms of root mean square error (rmse) of both NB and TAN structure with and without variable selection (SNB and STAN respectively)


Table 5 Variables selected by the STAN and its 10 reference values included in the model


included in the model one by one to calculate their probabilistic propagation, obtaining the distribution function of the objective variable (landscape change intensity).

Figure 6 shows the results in which thresholds can be identified. These are points from which the variations in the socioeconomic indicator (feature variable) generate large changes in the landscape, determining the degree of landscape vulnerability to variations in this indicator. Taking into account the type of relationship between socioeconomic and landscape change and, consequently, their potential resilience, the thresholds detected can indicate tipping points from which vulnerability increases or decreases. a) b)

![img-6.jpeg](img-6.jpeg)

Fig. 6 Distribution functions of the socioeconomic indicators selected through the methodology proposed. The points of the distributions highlighted in red are the thresholds detected. To the right of each distribution, the whisker box plots show the outliers, interpreted as tipping points. The interquartile range is represented by the green boxes. The median of each distribution is represented by red crosses and the mean by the black line. In each case, the selection of the tipping points has been based on the maximum distance to the interquartile range

The results show the threshold values of the socioeconomic indicators from which the landscapes studied are transformed with a greater or lesser intensity over time. For the period of time analysed, four very well differentiated socioeconomic thresholds were observed (Fig. 6), indicating that: (i) the rejuvenation of the population, as well as the connectivity with the city of Madrid, increase changes in the landscape; (ii) the connectivity with neighbouring municipalities and the abundance of livestock in the studied areas contribute to the resilience of the landscape (Fig. 6a). The rest of the socioeconomic indicators do not present a differentiated change threshold, but they provide valuable information on the resilience of the landscape in the face of their magnitude. Thus, the landscapes studied are more resilient when municipalities generate high values of industrial GDP, high per capita income per inhabitant, and the cadastral value of rural assets remains low, without urban interest (Fig. 6b).

## Discussion

Analyses of changes in landscape structure and composition along a remarkable urban-rural gradient in which the city of Madrid occupies a central geographical and socioeconomic position, indicate that the study area is subject to a multifaceted trend of landscape variation. This variation affects in a different way the silvo-pastoral landscapes of the N-NW of the gradient of those with agricultural vocation, located to the S-SE (Fig. 1). Nonetheless, land transformation towards urban sprawl is a common trend throughout the study region (Fig. 5).

The two main types of landscapes identified, with dissimilar degrees of naturalness and agricultural intensification, have unalike social-ecological conditions (Arnaiz-Schmitz et al. 2018a,b) and, therefore, their response to changes is also of different magnitude. Over time, silvo-pastoral landscapes show the most intense dynamics of change that implies the abandonment of traditional land uses, spatial fragmentation and urban transformation. These degraded rural systems have low resilience and, therefore, high vulnerability to the adverse effects of land use changes related to the new prevailing socioeconomic conditions (Adger 2006; Malek and Verburg 2020). Our results agree with the processes of change observed by other authors in Mediterranean landscapes, that underline the trend of abandonment of the rural landscape related to the socioeconomic transition from the traditional rural context to the urban one (Antrop 2000, 2006; Plieninger et al. 2014; Schmitz et al. 2021; Thapa et al. 2021).

Diachronic analyses of environmental and socioeconomic data series are powerful tools capable of dealing with the inherent complexity of social-ecological systems and their ability to adapt to change. However, few operational methods exist to quantify and predict the resilience of a landscape (Keane et al. 2018). Different authors have developed theoretical models, although often complicated, in which they detect thresholds of change in the SES through complex systems (Walker and Meyers 2004; Carpenter and Brock 2006, are some of them). Unfortunately, the empirical evidence of thresholds and their quantification is scarce. A review in this regard shows that the literature does not refer to any method that applies this probabilistic tool to the study of landscape change thresholds. The study of SES as complex adaptive systems is likely to make their analysis more difficult, limiting the amount of broad-scale research (Renaud et al. 2010; Lauerburg et al. 2020). Therefore, the development of integrative methods that model landscape-socioeconomic interactions is necessary and useful to understand the social-ecological feedback that regulates changes in land use and landscape resilience (De Aranzabal et al. 2008; Lambin and Meyfroidt 2010; Rescia et al. 2010).

In this study we demonstrate that BNs allow for the development of a useful methodological approach to analyse this information and detect the thresholds of landscape resilience. Despite the fact that BNs are a widely cited tool in the bibliography, most of the studies that analyse them focus on theoretical-methodological developments, disregarding their broad application capacity in Environmental Sciences (Aguilera et al. 2011). The main advantage of using BN networks over traditional multivariate models is that the BN ones used provide information about the structure of the relationships between the components of the system and how these components are related (that is, if a variable change, all others are affected) (Ropero et al. 2018b). Although, to date, BNs models have been rarely used in SES resilience assessments, research on them has shown that they can provide

valuable information on resilience structure and function (Franco-Gaviria et al. 2022).

The socioeconomic conditions of local populations have shaped and maintained rural cultural landscapes over the last few centuries, and today's rapid and drastic socioeconomic changes may affect landscape resilience beyond the thresholds of its adaptive capacity (Arnaiz-Schmitz et al. 2018b; Rescia et al. 2010). The loss of rurality observed in the traditional silvo-pastoral systems and the consequent rupture of the historical landscape-local socioeconomic links are related to the process of urban expansion and metropolisation of the region, which modifies existing social-ecological patterns creating new relationships between rural settlements, towns and cities. Spatial mobility is one the main features of urban transformation and metropolisation process of rural landscape (Serra et al. 2014; Cuadrado-Ciuraneta et al. 2017; Arnaiz-Schmitz et al. 2018b).

The results obtained indicate that silvo-pastoral landscapes are more resilient and less vulnerable to possible socioeconomic shocks that may arise when the traditional ecological knowledge (TEK) of local older people, accumulated during many generations of close interaction between people and nature, favours the maintenance of traditional livestock activities. Likewise, the cohesion between neighbouring rural settlements, interconnected through transportation networks, supports the stability of these landscapes. Landscape resilience and its associated thresholds of change are established within a coupled socioeconomic-ecological system, with feedback responses between human activities and landscape processes (Horan et al. 2011). Population rejuvenation without social mechanisms that allow the transmission TEK can result in a decoupling between the rural landscape and the local socioeconomic interactions and cause a gradual loss of resilience, driving the system towards thresholds of change (Berkes et al. 2000; Drew 2005; Gómez-Baggethun et al. 2013; Arnaiz-Schmitz et al. 2018c). The lack of adequate and effective land planning and management aimed at the conservation of cultural landscapes, together with institutional deficiencies in supporting local populations and their own TEK, favour the abandonment of rural landscapes and place them in a position of vulnerability (Schmitz et al 2021).

The resilience of these rural landscapes facing possible disturbances is fundamental to guarantee the
ecosystem's conditions. Although, in many cases, preventing the arrival of a threshold is impossible, especially if they are generated by external exogenous factors that are difficult to control and regulate (Horan et al. 2011), knowing the socioeconomic limits to which landscapes are submitted can be a very useful tool for the maintenance and conservation of the territory. The critical analysis of changes in the landscape before and after crossing one of these tipping points allows the development of adaptive and participatory management strategies in which the costs and benefits of the past and present situation of the territories are evaluated in order to achieve a and optimal benefit (Riekhof et al. 2022).

The method developed in this paper has allowed us to detect the tipping points from which small changes in socioeconomic indicators generate large changes at the landscape level. This information is of great value due to its usefulness for the conservation and maintenance of cultural rural landscapes, as tipping point dynamics are fundamental drivers for the development of more sustainable SES (Mathias et al. 2020).

## Conclusions

The preservation of cultural rural landscapes depends closely on the socioeconomics of their population settlements and the TEK of their local inhabitants, which plays a key role in increasing the landscape resilience. The social-ecological resilience of rural landscapes studied, located along an urban-rural gradient in Madrid region, is threatened by the drastic and rapid socioeconomic changes that have occurred in recent times, mainly due to the strong influence of the processes of metropolisation and urban expansion. Especially the silvo-pastoral landscapes of the region have experienced the abandonment, reduction and/or disappearance of rural land uses and traditional knowledge. These degraded rural systems have low resilience and high vulnerability to environmental changes.

The analysis of the landscape resilience, identifying the tipping points from which small changes in the main socioeconomic indicators give rise to important landscape changes, can facilitate decisionmaking in preventive policies and land management in the face of possible changes. However, the inherent complexity of SES makes it difficult to develop

empirical methods to quantify thresholds of change. By applying the integrative method developed here, which allowed us modelling landscape-socioeconomic interactions and feed-backs, we have detected the threshold values of socioeconomic indicators from which the silvo-pastoral landscapes studied have transformed with a greater or lesser intensity over time. The socioeconomic indicators identified that significantly contribute to the resilience of this type of landscape are both the maintenance of traditional livestock activities, supported by the TEK of local older people, and rural cohesion, favoured by improved mobility and interconnection between neighbouring municipalities through transport networks.

The results obtained demonstrate that the use of BNs networks is helpful to detect thresholds of change in the landscapes analysed and that, therefore, they are a useful tool to achieve an integrated socialecological land planning and can help to achieve more resilient territories.

Author contributions CAS performed the data collection; CAS and RFP performed the data analyses and wrote the methodology; MFS, PA and CAS developed the study conception and design; MFS and CAS wrote the paper. All of the authors read and corrected the paper, and gave their final approval for publication.

Funding Open Access funding provided thanks to the CRUE-CSIC agreement with Springer Nature. This research was funded by the projects: Contemporary Criteria, Methods and Techniques for Landscape Knowledge and Conservation (LABPA-CM) (H2019/HUM-5692), funded by the European Social Fund and the Madrid Regional Government; Project PID2019-106758 GB-C32 funded by MCIN/ AEI/10.13039/501100011033, FEDER \Una manera de hacer Europa" funds.

Data availability The datasets analysed during the current study are available from the corresponding author on reasonable request.

## Declarations

Conflict of interest The authors declare no conflict of interest or competing interests.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included
in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
