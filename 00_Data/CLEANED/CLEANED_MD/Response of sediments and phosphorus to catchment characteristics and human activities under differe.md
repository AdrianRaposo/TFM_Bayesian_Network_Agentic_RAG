# QUT 

## Queensland University of Technology

Brisbane Australia

This may be the author's version of a work that was submitted/accepted for publication in the following source:

Jin, Guangqiu, Xu, Jing, Mo, Yuming, Tang, Hongwu, Wei, Tong, Wang, You-Gan, \& Li, Ling
(2020)

Response of sediments and phosphorus to catchment characteristics and human activities under different rainfall patterns with Bayesian Networks. Journal of Hydrology, 584, Article number: 124695 1-13.

This file was downloaded from: https://eprints.qut.edu.au/198217/

## © 2020 Elsevier B.V

This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other specified license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au

License: Creative Commons: Attribution-Noncommercial-No Derivative Works 4.0

Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identified by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.
https://doi.org/10.1016/j.jhydrol.2020.124695

# Response of sediments and phosphorus to catchment characteristics and human activities under different rainfall patterns with Bayesian Networks 

Guangqiu Jin ${ }^{1,2}$, Jing Xu ${ }^{1,2,3 *}$, Yuming $\mathrm{Mo}^{1,2}$, Hongwu Tang ${ }^{1,2}$,
Tong Wei ${ }^{4}$, You-Gan Wang ${ }^{3}$, Ling $\mathrm{Li}^{5}$

${ }^{1}$ State Key Laboratory of Hydrology-Water Resource and Hydraulic Engineering, Hohai University, Nanjing, China

Emails: jingq@hhu.edu.cn
xujinghhu@hhu.edu.cn
yuming_m@hhu.edu.cn
hwtang@hhu.edu.cn
${ }^{2}$ College of Water Conservancy and Hydropower Engineering, Hohai University, Nanjing, China
${ }^{3}$ School of Mathematical Sciences, Queensland University of Technology, Queensland, Australia
Emails: j60.xu@qut.edu.au
you-gan.wang@qut.edu.au
${ }^{4}$ State Key Laboratory of Water Environment Simulation, School of Environment, Beijing Normal University, Beijing, China

Emails: tongwei@bnu.edu.cn
${ }^{5}$ School of Engineering, Westlake University, Hangzhou, China
Email: liling@westlake.edu.cn

Resubmitted to Journal of Hydrology on 12 Feburay 2020

* Corresponding author.

The rainfall patterns play an important role in determining the response of Suspended Sediment (SS) and Total Phosphorus (TP) to influence factors, which is complex and needs to be better understood. The Bayesian Network (BN), with each variable depending on only its immediate parent variables, can help to describe the complex processes involved. In this study, BNs were developed to assess the impacts of catchment characteristics and human activities on SS and TP loads under different rainfall patterns in the Huaihe River Basin (HRB). The results showed that SS made significant contributions to TP in rivers which increased with the rainfall intensity. Catchment characteristics (sub-catchment area, slope and soil erosion area) affected the SS and TP loads; however the influence of human activities (sewage outfalls and land use) was more significant. With the rainfall intensity rising, farmland switched from a "sink" to a "source" of nutrients. When the antecedent three-day-average rainfall intensity was high but the current one was low, the farmland became the most significant source of SS and TP. The urbanization had significant positive effects on SS (ranging from $10.9 \%$ to $15.1 \%$ ) and TP (ranging from $8.3 \%$ to $10.5 \%$ ), which was insensitive to rainfall patterns as a result of the high proportions of impervious surface coverage in the urban area. These results improve our understanding of influence factors on river water quality and will contribute to effective water environment management for rivers.

55 Rainfall pattern, Suspended sediment, Total phosphorus, Human activity, Bayesian
56 Network

Rainfall intensity is a key driver in runoff generation and soil erosion. It significantly affects sediment levels in catchments (López-Tarazón and Estrany, 2017; Nord and Esteves, 2010; Ran et al., 2012; Vaezi et al., 2017). Storm events play important roles in sediment transport and are responsible for a large proportion of the annual sediment loads (Bussi et al., 2016; Gao et al., 2017; Sherriff et al., 2015). Because runoff events and sediment transport are usually associated with nutrients loss, rainfall would also affect phosphorus loads.

Phosphorus is an essential nutrient for the primary productivity of a river and can be a limiting nutrient in the freshwater ecosystem (Cao et al., 2016; Wang et al., 2018; Yu et al., 2017). However, excessive phosphorus degrades the water environment and causes serious problems, such as hypoxic/anoxic episodes in the bottom water and increasing toxicity to aquatic organisms (Haygarth et al., 2005; Huang et al., 2018; Santos et al., 2015). Phosphorus is discharged into rivers from both point and non-point sources (external sources). The point sources of phosphorus typically come from domestic and industrial wastewater, which are discharged to rivers through sewage outfalls (Liu et al., 2017; Rattan et al., 2017; Tammeorg et al., 2017). The transport of phosphorus from non-point sources is mainly in the "sediment-bound" form; therefore, phosphorus levels in rivers is directly affected by suspended sediment concentrations (Huisman and Karthikeyan, 2012; Zhou et al., 2013). Sediments can work as a "sink" of phosphorus during transportation from land to water. Fine sediments accumulate in the riverbed during low flow periods, and start to resuspend and release phosphorus with increasing flow rates (Harvey et al., 2012; Park and Hunt, 2018; Yan et al., 2017; Yao et al., 2016; Zhang et al., 2015). Previous research has

reported that internal phosphorus released from sediments in the riverbed is an important source for total phosphorus loads in the overlying water and thus can hinder the improvement of the river water quality. The internal sources have become a major challenge in tackling poor water quality, in spite of success in controlling external phosphorus sources (Cavalcante et al., 2018; Doan et al., 2018; Huser et al., 2016). Therefore, internal phosphorus released from riverbed sediments should be taken into account when assessing factors influencing the river water quality; however, it was neglected by previous studies.

Many studies reported that the sediment and phosphorus loads rose with increasing rainfall amount or during storm events (Chen et al., 2012; Guo et al., 2010; Hancock, 2012; Noble et al., 2003; Rodríguez-Blanco et al., 2013). Zi et al. (2016) reported that when the topsoil was near the full saturation, the sediment loads per unit rainfall amount would largely increase. It means that the soil saturation condition could directly affect the amount of sediment loads under the same rainfall intensity. The soil saturation condition can be affected by the rainfall on the days prior to sampling. Thus, only considering the current rainfall is not enough for describing the effects of rainfall on sediment loads. In addition, the significant effects of antecedent discharge and rainfall on water quality have been demonstrated by several previous research (Guo et al., 2019; Leight and Hood, 2018; Mcmillan et al., 2018; Wang and Tian, 2013; Zhang and Ball, 2017). Therefore, an in-depth analysis of how the different antecedent and current rainfall patterns affect the sediment and phosphorus loads in rivers is essential for efficient river management.

Natural catchment characteristics and human activities are important factors in determining sediment and phosphorus levels in river basins. Dynamics of sediments and nutrients in rivers are highly dependent on catchment characteristics such as the

area and slope. Different land uses are shown to be a decisive factor in determining sediment and phosphorus levels in catchments due to different hydrological processes and transport capacities with different land uses (Buendia et al., 2016; Dunne, 1979; Zhu et al., 2013). Accordingly, even relatively minor changes in the land use can have a significant influence on sediment and nutrients loads in river basins (Wang et al., 2012).

In order to better understand the factors that influence the water environment, we analyzed the response of Suspended Sediment (SS) and Total Phosphorus (TP) to catchment characteristics and human activities (land use and sewage outfalls) under different rainfall patterns in the Huaihe River Basin (HRB). The HRB is a highly polluted river basin in China due to economic developments and urbanization (Xu et al., 2018; Zhai et al., 2017). Because large numbers of physical and biogeochemical processes are involved in determining SS and TP levels in rivers (Hollaway et al., 2018), conventional statistical models are not sufficient for describing the complex interdependencies. The Bayesian Network (BN) can describe complicated processes in a simple way (Aguilera et al., 2011; Korb and Nicholson, 2004; Li et al., 2018), and provide an approach to incorporate both quantitative and qualitative variables into one model.

The main objectives of this paper are to (1) develop the BN model to describe the complex interdependencies between influence factors (catchment characteristics and human activities) and water quality (SS and TP) in the HRB; (2) explain the distribution of SS and TP loads and the relative importance of internal sources to TP (released from resuspended SS) under different rainfall patterns; (3) assess the role of rainfall patterns in affecting the response of SS and TP to catchment characteristics and human activities. This study will improve the understanding of the effects of

antecedent/current rainfall patterns, catchment characteristics and human activities on water quality, which is crucial for efficient water environment management.

# 2 Material and methods 

### 2.1 Study area and monitoring stations

The HRB is one of the most important river basins in eastern China, with a drainage area of $270,000 \mathrm{~km}^{2}$ (Fig. 1 (a)). It is located between latitudes $30^{\circ} \sim 36^{\circ} \mathrm{N}$ and longitudes $111^{\circ} \sim 121^{\circ}$ E. The Main Reaches of Huaihe River (MRHR) originates from the Tongbai Mountain in Henan province, and runs through Anhui and Jiangsu provinces from west to east before flowing into the Hongze Lake (Xu et al., 2018; Zhai et al., 2017) (Fig. 1 (b)).

There are sixteen monitoring stations in the study area (Table 1) with six of them (S1-S6) in the MRHR while the others are in tributaries: three stations (S13-S15) on the Guo River (GR), two stations (S9, S10) on the Jialu River (JLR) and two stations (S11, S12) on the Huiji River (HJR). Another three stations (S7, S8, S16) lie on Hong River (HGR), Shaying River (SYR) and Hui River (HR), respectively.

### 2.2 Data sources and processing

The water quality datasets (including TP concentration, SS concentration and water temperature) and amount of TP contaminants from sewage outfalls (from 2003 to 2014) were provided by the Monitoring Center of Huaihe River Water Resource Protection Bureau. The TP concentration and water temperature were measured on the same day and their sampling frequencies were from weekly to monthly, and the SS samples were collected at the daily frequency. All water quality variables were

measured by the national standard methods of water quality testing. The samples of the TP contaminant from the sewage outfalls, which contained domestic wastewater and untreated or partly treated (from wastewater treatment plant) industrial effluents, were collected weekly by the Monitoring Center. The daily flow datasets were collected from the hydrographic office of Huaihe River Commission of the Ministry of Water Resources, P. R. C.

The digital elevation model (DEM) with a resolution of $90 \mathrm{~m} \times 90 \mathrm{~m}$, soil erosion map and land use map in 2005, 2010 and 2015 were collected from the Data Centre for Resources and Environmental Science, Chinese Academy of Sciences (RESDC, http://www.resdc.cn). The locations of monitoring stations, stream networks and DEM data were transformed to GIS layers by ArcGIS 10.5 (ESRI Company, Redlands, California, USA) for the HRB under the Gauss-Kruger projected coordinate system. Based on stream networks and topographical features extracted from the DEM, the HRB was delineated into sixteen sub-catchments using the ArcHydro toolset in ArcGIS (Fig. 1(c)).

The area and mean slope of each sub-catchment were extracted from the DEM map (Fig. 3). The percentage of soil erosion area and each land use type in 2005, 2010 and 2015 were extracted for all sub-catchments. Six categories of land use were considered in our study: woodland, grassland, water, urban, rural resident land and farmland (Fig. 1(c)). The detailed inclusions in each land use category were shown in Table 2. As few changes in percentage of land use had happened over the research periods (Table 3) and the land use data were available in these three years, we used the land use data in 2005 (Fig. 2 (a)) to match the dataset from 2003 to 2007, the land use data in 2010 (Fig. 2 (b)) to match the dataset from 2008 to 2012 and the land use data in 2015 (Fig. 1(c)) to match the dataset from 2013 to 2014.

The daily rainfall data at all monitoring stations over the study period were collected from the National Meteorological Information Center (http://data.cma.cn). The rainfall amount at each sub-catchment was estimated by Thiessen Polygons (Thiessen, 1911), which is a widely used method for estimating areal rainfall (Dessie et al., 2015; Ghanem, 2011; Goovaerts, 2000; Han and Bray, 2006; Ly et al., 2011; Shen et al., 2012). The rainfall measured at one station could represent the region, namely, the Thiessen Polygon, which is enclosed by the lines drawn midway between the station and its neighbor stations (Jarvis et al., 2013). Thirty rain gauges were chosen from the national rain gauges networks in the study (Fig. 4). Compared with the research area vs. the amount of rain gauges in the relative references, the number of rain gauges in the study can meet the research need (Table 4). The rainfall amount on the sampling days and antecedent TDA rainfall amount were calculated for all sub-catchments. Based on the standard of rainfall intensity recommended by the China Meteorological Administration (Table 5), the current rainfall and TDA rainfall were separated into three categories, namely, "low", "medium" and "high" rainfall intensity. In order to denote rainfall patterns conveniently, we used the first letter of rainfall patterns to denote the current rainfall intensity and the second letter to denote the TDA rainfall intensity, for example, the "LH" means current rainfall and TDA rainfall are low and high, respectively.

# 2.3 Methods 

The BN is a graphical approach, which includes nodes and arrows to represent random variables (continuous and/or discrete) and probabilistically conditional dependencies between variables, respectively. The DAG is used to demonstrate the structure of the BN model, in which the global probability distribution was factorized

into a set of local probability distributions for each variable following the Markov Property (Korb and Nicholson, 2004). Therefore, the complex interdependencies can be described in a simple way, in which each variable only depends on its immediate parent variables. The BN model works in a two-step approach. First, it learns the model structure using Structure Learning Algorithms. Second, it estimates the conditional regression coefficients for continuous variables and conditional probabilities for discrete variables based on local conditional dependencies. Thus, each local conditional function could be considered without knowing the explicit information in global probability distribution (Korb and Nicholson, 2004; Li et al., 2018; Scutari, 2010; Wijesiri et al., 2018).

In this study, the BN was developed to describe the complex response of water quality indicators (SS and TP) to influence factors (catchment characteristics, human activities) under different rainfall patterns in the HRB (Fig. 5). Accordingly, six land use categories, different rainfall patterns (rainfall intensity on the sampling day and TDA) and catchment characteristics (area, slope and soil erosion area) were identified as factors (inputs) that influenced SS loads (outputs). Similarly, the land use, rainfall patterns, catchment characteristics (area, slope and water temperature), sewage outfalls and SS loads were set as factors (input) that influenced TP loads (output), among which SS could significantly affect TP due to its capacity of TP absorption/desorption.

In order to conform to the conditional Gaussian distribution, the two water quality indicators (TP and SS) underwent log-transformation. The log-transformed TP and SS loads, water temperature, proportions of six land use types, soil erosion area, catchment area, slope and TP amount from sewage outfalls were fed into the BN as quantitative (continuous) data, while rainfall intensity and TDA rainfall intensity were

inputted as qualitative (discrete) data, namely, "low", "medium" and "high" scenarios respectively. The BN model was developed by the "bnlearn" package (Scutari, 2010) in the R statistical computing platform (R Core Team, 2016), which is a common program in statistical analysis. The validation of the developed BN model and the uncertainty analysis can be found in the supplementary material.

In order to find out whether SS loads had significant effects on TP loads, the BN models with and without SS influence were developed with the whole dataset for comparison. The goodness-of-fit of models was evaluated by Pearson's correlation coefficients (Cor) and Nash-Sutcliffe efficiency coefficients (NSE) (Nash and Sutcliffe, 1970). According to the recommendation from Moriasi et al. (2007), when the NSE of a model is higher than 0.5 , the model can be viewed to be acceptable.

To properly evaluate the effects of influence factors, the relative importance (RI) of each factor was calculated based on the predicted parameters from the developed BN model (Eq. 1).

$$
R I_{i}=\frac{\operatorname{Parm}_{i}}{\sum_{i=1}^{n}\left|\operatorname{Parm}_{i}\right|} \times 100 \%
$$

where $R I_{i}$ is the relative importance of $i$ th influence factor, $\operatorname{Parm}_{i}$ is the predicted parameter of the ith influence factor from the BN model. The numeric value of RI presents the magnitude of relative importance and the plus-minus sign indicates the positive or negative correlation between the influence factors and the SS or TP loads.

# 3 Results and discussion 

### 3.1 Evaluation of the BN model

The variables of the developed BN models were chosen by the arrow strength test. The results were shown in Table S2 in the supplementary materials. The performance of the BN models for paired SS and TP predictions can be evaluated by the Cor and NSE. The Cor and NSE between observed and predicted SS loads were 0.780 and 0.609 , respectively (Table 6). According to the comparisons between observed and predicted SS (Fig. 6 (a)), as most of the points were along the 1:1 line, it means the predictions of SS loads were almost the same as the observed ones. Therefore, the performance of the BN model for SS loads was satisfactory.

The BN model failed to make good fitness to observed TP loads, if predicting TP loads without SS (Fig. 6 (b)). However, when considering the influence of SS to TP, the Cor and NSE between observed and predicted TP loads increased from 0.652 to 0.853 and from 0.496 to 0.727 (Table 6), respectively. The BN model (with SS) gave satisfied prediction performance for observed TP loads (Fig. 6 (c)). The results implied that SS had significant effects on TP loads in the HRB. It was also supported by plots of SS and TP loads in Fig. 7, in which TP loads had similar trends to SS loads in these typical stations. Accordingly, when the SS loads got the highest values in the year, the TP loads tended to be in a high value range, and vice versa. Our result was consistent with the results from previous studies that a highly positive correlation existed between SS and TP (Wang et al., 2015b; Zhou et al., 2013).

### 3.2 Patterns and relationship of SS and TP loads under different rainfall patterns

According to the current (at the sampling day) and the TDA rainfall intensity in

the HRB from the real rainfall dataset, rainfall patterns were divided into five cases, namely, "LL", "LM", "LH", "ML" and "HL" patterns, then the possibilities of all patterns were calculated (Table 7). The "LL" pattern had the highest possibility in the HRB. The "LM" and "ML" patterns had relatively lower possibilities in the HRB, while the "LH" and "HL" patterns had the lowest possibilities.

The SS and TP loads reached the maximum under the "LH" pattern, followed by the "HL" pattern (Table 7). The SS and TP loads were higher under the "LM" pattern than those under the "ML" pattern. The lowest SS and TP loads happened under the "LL" pattern. According to rainfall intensity at the typical stations in Fig. 7, it was clear that the relatively high values of SS and TP loads always were observed together with the medium or high rainfall intensity. The results showed that SS and TP loads increased with rainfall intensity as the main driver in soil loss which resulted in the transport of sediment and nutrients (Hancock, 2012; Rodríguez-Blanco et al., 2019; Wang et al., 2014; Wu et al., 2018). Previous research reported the similar results that SS and TP loads were mainly transported and washed into rivers during storm events or flood events (Adams et al., 2014; Chen et al., 2018b; Nerantzaki et al., 2015; Ockenden et al., 2016).

Our results revealed that the TDA rainfall intensity had more important effects on the SS and TP loads than the rainfall intensity on the sampling day. Accordingly, the SS and TP loads were higher under "LH" patterns rather than "HL" patterns; and similarly they were higher under "LM" patterns rather than "ML" patterns. Generally, the highest SS and TP loads were observed with the high antecedent rainfall intensity. This due to the travel time of SS and TP moving from land to rivers; thus, a time lag exists in the response of SS and TP loads to rainfall. The current rainfall intensity mainly affected the resuspension of sediments from the riverbeds, which could release

TP to the overlying water (internal sources). Differently, the TDA rainfall intensity was mainly associated with the SS and TP loads caused by soil loss from lands (external sources) although it may also contribute partly to sediment resuspension. In general, SS and TP loads under different rainfall intensities implied that the external TP sources contributed more to TP loads than internal TP sources. When comparing the loads under the same TDA rainfall intensity, namely, "LL", "ML" and "HL", an obvious increase in loads could be observed. It means that although the contribution of internal SS and TP loads is less than external loads, it still has important effects on loads and cannot be ignored in managing the water environment. In order to control the internal TP loads, dredging sediment is a potential solution that can decrease TP releasing from riverbeds reported by several researchers (Chen et al., 2018a; Yu et al., 2017).

SS had a significant positive influence on the TP loads, and the contribution increased from $8.3 \%$ to $21.3 \%$ with increased rainfall intensity (Fig. 8). According to results from the Random forest, SS was the most important influence factor for TP (Fig. S2 in the supplementary material). More intensive rainfall caused more sediment exporting from lands and more sediment re-suspending from streambeds, therefore, SS could make more contribution to TP by transporting and releasing it (Huisman and Karthikeyan, 2012).

# 3.3 Rainfall patterns can affect the response of SS and TP to catchment characteristics 

The influence factors associated with catchment characteristics to SS and TP are sub-catchment area, slope, soil erosion area and water temperature. The relative importance of catchment characteristics was analyzed based on the results from BN

The sub-catchment area had a positive influence on SS and TP loads. To SS, the contribution reached the maximum ( $11.9 \%$ ) under the "LH" pattern; however, the contributions were minor under other rainfall patterns. It was supported by previous research that a larger catchment area can supply more sediment. However, travel time, which is another factor affecting sediment loads, is needed for sediment moving from land to rivers. Larger catchments are expected to have longer flow paths, thus longer travel time (Alatorre et al., 2010; Huang et al., 2018). When the TDA rainfall intensity was "high", enough time was provided for SS transport until the sampling day. Therefore, the positive contribution of the area to SS can be observed. If the rainfall intensity on the sampling day was "high", although a large amount of soil loss could be triggered, it could not be transported into rivers immediately, especially the sediment loads from the longer distance. Therefore, the sub-catchment area would not have significant effects on SS loads when the current rainfall intensity is "high" and the TDA rainfall intensity is "low" or "medium". The impacts of different rainfall patterns provided possible explanations for why different relationship (positive, negative or combined positive and negative) had been found between sub-catchment area and SS loads by previous studies (Hancock et al., 2017; Huisman and Karthikeyan, 2012; López-Tarazón and Estrany, 2017). The contributions of the sub-catchment area to TP were similar to that to SS, which can be easily explained by that TP was absorbed and transported by soil particles from land to rivers.

The slope had positive effects on SS and TP loads (Fig. 8). It made the highest contribution ( $14.3 \%$ ) to SS under the "LH" pattern. With highly intensive rainfall on the previous days, the saturated topsoil was easy to be eroded and the erosion rate increased with the increased slope (Defersha and Melesse, 2012; Vanmaercke et al.,

2011; Wang et al., 2014; Wongsa and Shimizu, 2004). Similarly, the slope had a positive contribution (8\%) to TP loads under "LM", "LH" and "ML" patterns, however, the contributions were quite low under other rainfall patterns.

The soil erosion area had significant positive effects on SS loads when the current rainfall intensity was "low", and its contribution decreased sharply with increased rainfall intensity (Fig. 8). Highly intensive rainfall could cause soil loss in all types of soil particles. Thus, the relative effects of soil erosion area were lower under these rainfall patterns. Besides, TP loads had a positive response to water temperature, however, the contribution is less than $3 \%$ (Fig. 8). It implied that the amount of TP releasing from SS tended to increase at warm conditions, which is consistent with the results from previous studies (Ding et al., 2018; Santos et al., 2015; Zhou et al., 2016).

# 3.4 Rainfall patterns can affect the response of SS and TP to human activities 

The influence factors associated with human activities to SS and TP are land use and sewage outfalls. The influence of six types of land use has been considered, including farmland, grassland, woodland, urban, water and rural resident land. The relative importance of human activities was analyzed based on the results of the BN models.

The farmland is the main influence factor to SS and TP loads under all rainfall patterns (Fig. 8). Previous researches reported that intensive agriculture was an important cause of accelerated soil erosion (Heathwaite, 1994; Huisman and Karthikeyan, 2012; Sherriff et al., 2015; Zhang et al., 2018). Farmland had a significant negative relationship to SS and TP loads under the "LL" and "LM" patterns, while it made a positive contribution under other rainfall patterns. Several reasons are responsible for the "sink" and "source" processes transforming in

farmland. When the current rainfall intensity is "low", without enough surface runoff, sediment and phosphate fertilizers tend to store in the farmland. With rainfall intensity increasing, the sediment and nutrients are transported with the generated runoff, and thus farmland acts from "sink" (under low rainfall intensity) to "source" (under high rainfall intensity). It is consistent with the result from previous research that the majority of SS and TP loads from agricultural diffusion pollution were supplied during storm events (Bowes et al., 2015; Weigelhofer et al., 2018; Wu et al., 2017). Besides, Uwimana et al. (2018) reported that farming practices, such as hoeing, weeding and transplanting (Labrière et al., 2015), had the highest impacts on sediment and phosphorus runoff during high flow periods, especially following the low flow periods with high nutrients accumulated. However, the "LH" rainfall pattern was a special case in that farmland acted as "source" to SS and TP which was different from "LL" and "LM" patterns. Under the "LH" pattern, farmland had the most significant influence on SS and TP loads, which was caused by the following two reasons. First, topsoil tended to be near saturated when the TDA rainfall intensity was "high", therefore, the soil was easy to erode under the subsequent rainfall events (Rodríguez-Blanco et al., 2019; Zi et al., 2016), despite that the rainfall intensity was "low". The second potential reason was related to the farming activities in the HRB. The irrigated farmland was filled with water after storm events, and farmers tended to discharge the generated runoff caused by the following rainfall events, no matter whether the rainfall intensity was "high" or "low". Thus, agricultural runoff transported a large quantity of sediments and nutrients. Moreover, based on the results from the Random Forest application, the farmland was one of the most important influence factors to SS level in rivers (Fig. S3 in the supplementary material). Due to the large proportion of soil and nutrients lost from farmland, measures should be

taken to control it, such as constructing runoff detention and settling ponds (Ockenden et al., 2017; Ouyang et al., 2016; Tan et al., 2017), to improve water environment in the HRB.

The grassland and woodland had significant negative effects on SS and TP loads when the current rainfall intensity was “low”, and had positive contribution under the other rainfall patterns (Fig. 8). Previous researches showed that the denser vegetation can reduce runoff volumes and trap soil, and thus retain the sediment particles and intercept pollutant sources (Gonzales-Inca et al., 2018; Kang et al., 2001; Le Bouteiller and Venditti, 2015; Rodriguez-Lloveras et al., 2015). Therefore, woodland and grassland could have better water and soil conservation functions to reduce water pollution from non-point sources (Ha et al., 2018; Jiao et al., 2000; Uwimana et al., 2018; Wang et al., 2015a; Zorzal-Almeida et al., 2018). However, the woodland was the source of SS and TP loads under the “HL” pattern, which is similar to the finding from previous studies (Smith and Owens, 2014; Uwimana et al., 2018). The surface runoff generated by rainfall events with high rainfall intensity was responsible for the transport of SS and TP (Burt and Pinay, 2005).

The urban factors played a positive role in SS and TP loads, which had relatively stable contribution under different rainfall patterns (Fig. 8). The reason is the high proportion of impervious surface coverage in the urban area. With the infiltration process occurring on the soil surface, the overland runoff is in the form of saturation excess runoff which cannot be generated by low rainfall intensity. However, the overland runoff on the impervious ground generated by rainfall is without the infiltration process. Therefore, the loads in the urban area are less sensitive to the change in rainfall intensity when comparing to the soil surface in farmland, as farmland witnessed the transition between the “sink” and “source” states under

different rainfall patterns. Previous research has also observed that most of particles or sediment were transported by urban runoff which was still increasing by intensive human activities in urban development (Dillon and Kirchner, 1975; Le Gall et al., 2018; Nelson and Booth, 2002). Water, which includes reservoirs, marshes, wetlands and lakes, had a negative influence on SS loads when the current rainfall intensity was "low", and had a positive influence under the other rainfall patterns (Fig. 8). The result can be explained by the reason that sediment was deposited at riverbeds under "low" rainfall intensity, which would re-suspend during storm events. Differently, water had positive effects on TP loads under all rainfall patterns, especially under "ML" and "HL" patterns. The majority of the remobilization of TP from bed sediment at high flow periods could be a potential reason for this result (Bowes et al., 2015). Rural resident land had a slightly negative influence (less than 5\%) to SS loads when the current rainfall intensity was "low", while it had about $20 \%$ contribution under the other conditions, and had significant positive effects on TP loads under all rainfall patterns (Fig. 8). It was related to domestic and livestock wastewater discharged in this area which contained considerable nutrients (Rattan et al., 2017).

Sewage outfalls had positive effects on TP loads, with contributions ranging from $12.9 \%$ to $17.7 \%$ when the current rainfall intensity was "low" (Fig. 8). Similar results had been reported that wastewater discharged from rapid industrialization and urbanization had greatly increased the nutrients levels in rivers (Zhang et al., 2018). However, with the increased rainfall intensity, the contribution of sewage outfall had a sharp decrease, and non-point sources started to play an important role in SS and TP loads.

To assess the response of SS and TP to catchment characteristics and human activities under different rainfall patterns in the HRB, the BN model was developed to describe these complex interdependencies. The prediction performances of the BN model were satisfactory. Key findings are summarized as follows:
(1) The SS and TP loads reached the maximum under the "LH" rainfall pattern, which means that external sources made more contribution to the degradation of water quality in the HRB than the internal sources. SS had great impacts on TP in river basins, and the contribution of SS became more significant under high rainfall intensity.
(2) Catchment characteristics (area, slope and soil erosion area) had positive contribution to SS and TP loads, and the maximum contribution rate were $11.94 \%$, $14.33 \%$ and $11.48 \%$ to SS and $12.37 \%, 17.63 \%$ to TP, respectively. However, the contributions were relatively minor with comparison of human activities.
(3) Human activities (land use and sewage outfalls) had a significant influence on the SS and TP loads. The influence of the farmland transformed between "sink" and "source" of SS and TP under different rainfall patterns. It had the most significant positive influence under the "LH" condition because of the soil saturation and farming activities which were related to high TDA rainfall intensity. The positive impacts of urbanization were insensitive to rainfall patterns because of its impervious surface coverage. Woodland and grassland had significant negative effects on SS and TP under low rainfall patterns, which could be used as river buffers. Sewage outfalls had positive effects on TP loads, whose contribution decreased sharply with increased rainfall intensity.

These findings highlight that both current rainfall intensity and the TDA rainfall intensity played important roles in determining the river water quality (SS and TP). The processes that drive nutrients transport and release from fine sediment particles need to be considered. In this paper, we considered these processes using statistical models; however, the mechanisms and underlying the nutrient transport and release should be analyzed in the future. In order to better manage the river water environment, measures such as constructing runoff detention and settling ponds should be implemented to control SS and TP loss from farmland and urban, especially under high rainfall intensity. Moreover, for better water and soil conservation, denser vegetation cover such as woodland and grassland could be used as riparian buffers to trap sediment particles and nutrients. Although the study presented here is based on the HRB, the BN model and the approach can also be applied in other polluted river basins around the world.

This research was supported by the Natural Science Foundation of China (51421006, 51679065), Fundamental Research Funds for the Central Universities (2019B71414), Postgraduate Research \& Practice Innovation Program of Jiangsu Province (SJKY19_0479), Basic Research Programs (Natural Science Foundation) of Jiangsu Province (BK20171436), Priority Academic Program Development of Jiangsu Higher Education Institutions (YS11001) and the China Scholarship Council. This research was partially supported by ARC DP (DP160104292) for Jing Xu and ARC Centre of Excellence for Mathematical and Statistical Frontiers for You-Gan Wang. Data used in the analysis presented in the paper can be obtained by sending a request to the corresponding author (xujinghhu@hhu.edu.cn).

Adams, R. et al., 2014. A catchment study of sources and sinks of nutrients and sediments in south-east Australia. Journal of Hydrology, 515: 166-179. DOI:https://doi.org/10.1016/j.jhydrol.2014.04.034
Aguilera, P.A., Fernández, A., Fernández, R., Rumí, R., Salmerón, A., 2011. Bayesian networks in environmental modelling. Environmental Modelling \& Software, 26(12): 1376-1388. DOI:https://doi.org/10.1016/j.envsoft.2011.06.004
Alatorre, L.C., Beguería, S., García-Ruiz, J.M., 2010. Regional scale modeling of hillslope sediment delivery: A case study in the Barasona Reservoir watershed (Spain) using WATEM/SEDEM. Journal of Hydrology, 391(1): 109-123. DOI:https://doi.org/10.1016/j.jhydrol.2010.07.010
Bowes, M.J. et al., 2015. Characterising phosphorus and nitrate inputs to a rural river using high-frequency concentration-flow relationships. Science of The Total Environment, 511: 608-620. DOI:https://doi.org/10.1016/j.scitotenv.2014.12.086
Buendía, C., Herrero, A., Sabater, S., Batalla, R.J., 2016. An appraisal of the sediment yield in western Mediterranean river basins. Science of The Total Environment, 572: 538-553. DOI:https://doi.org/10.1016/j.scitotenv.2016.08.065
Burt, T.P., Pinay, G., 2005. Linking hydrology and biogeochemistry in complex landscapes. Progress in Physical Geography: Earth and Environment, 29(3): 297-316. DOI:10.1191/0309133305pp450ra
Bussi, G., Dadson, S.J., Prudhomme, C., Whitehead, P.G., 2016. Modelling the future impacts of climate and land-use change on suspended sediment transport in the River Thames (UK). Journal of Hydrology, 542: 357-372. DOI:https://doi.org/10.1016/j.jhydrol.2016.09.010
Cao, X., Wang, Y., He, J., Luo, X., Zheng, Z., 2016. Phosphorus mobility among sediments, water and cyanobacteria enhanced by cyanobacteria blooms in eutrophic Lake Dianchi. Environmental Pollution, 219: 580-587. DOI:https://doi.org/10.1016/j.envpol.2016.06.017
Cavalcante, H., Araújo, F., Noyma, N.P., Becker, V., 2018. Phosphorus fractionation in sediments of tropical semiarid reservoirs. Science of The Total Environment, 619-620: 1022-1029. DOI:https://doi.org/10.1016/j.scitotenv.2017.11.204
Chen, M. et al., 2018a. Successful control of internal phosphorus loading after sediment dredging for 6years: A field assessment using high-resolution sampling techniques. Science of The Total Environment, 616-617: 927-936. DOI:https://doi.org/10.1016/j.scitotenv.2017.10.227
Chen, N., Krom, M.D., Wu, Y., Yu, D., Hong, H., 2018b. Storm induced estuarine turbidity maxima and controls on nutrient fluxes across river-estuary-coast continuum. Science of The Total Environment, 628-629: 1108-1120. DOI:https://doi.org/10.1016/j.scitotenv.2018.02.060
Chen, N., Wu, J., Hong, H., 2012. Effect of storm events on riverine nitrogen dynamics in a subtropical watershed, southeastern China. Science of The Total Environment, 431: 357-365. DOI:https://doi.org/10.1016/j.scitotenv.2012.05.072
Defersha, M.B., Melesse, A.M., 2012. Field-scale investigation of the effect of land use on sediment yield and runoff using runoff plot data and models in the Mara River basin, Kenya. CATENA, 89(1): 54-64. DOI:https://doi.org/10.1016/j.catena.2011.07.010
Dessie, M. et al., 2015. Water balance of a lake with floodplain buffering: Lake Tana, Blue Nile Basin, Ethiopia. Journal of Hydrology, 522: 174-186. DOI:https://doi.org/10.1016/j.jhydrol.2014.12.049
Dillon, P.J., Kirchner, W.B., 1975. The effects of geology and land use on the export of phosphorus from watersheds. Water Research, 9(2): 135-148. DOI:https://doi.org/10.1016/0043-1354(75)90002-0
Ding, S. et al., 2018. Internal phosphorus loading from sediments causes seasonal nitrogen limitation for harmful algal blooms. Science of The Total Environment, 625: 872-884. DOI:https://doi.org/10.1016/j.scitotenv.2017.12.348
Doan, P.T.K. et al., 2018. Phosphorus retention and internal loading in the Bay of Quinte, Lake Ontario, using diagenetic modelling. Science of The Total Environment, 636: 39-51. DOI:https://doi.org/10.1016/j.scitotenv.2018.04.252
Dunne, T., 1979. Sediment yield and land use in tropical catchments. Journal of Hydrology, 42(3): 281-300. DOI:https://doi.org/10.1016/0022-1694(79)90052-0
Gao, G. et al., 2017. Spatio-temporal patterns of the effects of precipitation variability and land use/cover changes on long-term changes in sediment yield in the Loess Plateau, China. Hydrol. Earth Syst. Sci., 21(9): 4363-4378. DOI:10.5194/hess-21-4363-2017

Ghanem, A.A., 2011. Climatology of the areal precipitation in Amman/Jordan. International Journal of Climatology, 31(9): 1328-1333. DOI:doi:10.1002/joc. 2160
Gonzales-Inca, C. et al., 2018. Spatial modeling of sediment transfer and identification of sediment sources during snowmelt in an agricultural watershed in boreal climate. Science of The Total Environment, 612: 303-312. DOI:https://doi.org/10.1016/j.scitotenv.2017.08.142
Goovaerts, P., 2000. Geostatistical approaches for incorporating elevation into the spatial interpolation of rainfall. Journal of Hydrology, 228(1): 113-129. DOI:https://doi.org/10.1016/S0022-1694(00)00144-X
Guo, D. et al., 2019. Key Factors Affecting Temporal Variability in Stream Water Quality. Water Resources Research, 55(1): 112-129. DOI:10.1029/2018wr023370
Guo, T., Wang, Q., Li, D., Wu, L., 2010. Sediment and solute transport on soil slope under simultaneous influence of rainfall impact and scouring flow. Hydrological Processes, 24(11): 1446-1454. DOI:doi:10.1002/hyp. 7605
Ha, M., Zhang, Z., Wu, M., 2018. Biomass production in the Lower Mississippi River Basin: Mitigating associated nutrient and sediment discharge to the Gulf of Mexico. Science of The Total Environment, 635: 1585-1599. DOI:https://doi.org/10.1016/j.scitotenv.2018.03.184
Han, D., Bray, M., 2006. Automated Thiessen polygon generation. Water Resources Research, 42(11). DOI:doi:10.1029/2005WR004365
Hancock, G., 2012. Modelling stream sediment concentration: An assessment of enhanced rainfall and storm frequency. Journal of Hydrology, 430-431: 1-12. DOI:https://doi.org/10.1016/j.jhydrol.2012.01.022
Hancock, G.R., Hugo, J., Webb, A.A., Turner, L., 2017. Sediment transport in steep forested catchments - An assessment of scale and disturbance. Journal of Hydrology, 547: 613-622. DOI:https://doi.org/10.1016/j.jhydrol.2017.02.022
Harvey, J.W. et al., 2012. Hydrogeomorphology of the hyporheic zone: Stream solute and fine particle interactions with a dynamic streambed. Journal of Geophysical Research: Biogeosciences, 117(G4). DOI:doi:10.1029/2012JG002043
Haygarth, P.M., Wood, F.L., Heathwaite, A.L., Butler, P.J., 2005. Phosphorus dynamics observed through increasing scales in a nested headwater-to-river channel study. Science of The Total Environment, 344(1): 83-106. DOI:https://doi.org/10.1016/j.scitotenv.2005.02.007
Heathwaite, A.L., 1994. Chemical fractionation of lake sediments to determine the effects of land-use change on nutrient loading. Journal of Hydrology, 159(1): 395-421. DOI:https://doi.org/10.1016/0022-1694(94)90269-0
Hollaway, M.J. et al., 2018. The challenges of modelling phosphorus in a headwater catchment: Applying a 'limits of acceptability' uncertainty framework to a water quality model. Journal of Hydrology, 558: 607-624. DOI:https://doi.org/10.1016/j.jhydrol.2018.01.063
Huang, H. et al., 2018. Influence of land use on the persistence effect of riverine phosphorus. Hydrological Processes, 32(1): 118-125. DOI:doi:10.1002/hyp. 11408
Huisman, N.L.H., Karthikeyan, K.G., 2012. Using radiometric tools to track sediment and phosphorus movement in an agricultural watershed. Journal of Hydrology, 450-451: 219-229. DOI:https://doi.org/10.1016/j.jhydrol.2012.05.007
Huser, B.J., Futter, M., Lee, J.T., Perniel, M., 2016. In-lake measures for phosphorus control: The most feasible and cost-effective solution for long-term management of water quality in urban lakes. Water Research, 97: 142-152. DOI:https://doi.org/10.1016/j.watres.2015.07.036
Jarvis, D., Stoeckl, N., Chaiechi, T., 2013. Applying econometric techniques to hydrological problems in a large basin: Quantifying the rainfall-discharge relationship in the Burdekin, Queensland, Australia. Journal of Hydrology, 496: 107-121. DOI:https://doi.org/10.1016/j.jhydrol.2013.04.043
Jiao, J.Y., Wang, W.Z., Jing, L.I., 2000. EFFECTIVE COVER RATE OF WOODLAND AND GRASSLAND FOR SOIL AND WATER CONSERVATION. Acta Phytoecologica Sinica, 24(5).
Kang, S. et al., 2001. Runoff and sediment loss responses to rainfall and land use in two agricultural catchments on the Loess Plateau of China. Hydrological Processes, 15(6): 977-988. DOI:doi:10.1002/hyp. 191
Korb, K.B., Nicholson, A.E., 2004. Bayesian Artificial Intelligence,. Chapman and Hall,.
Labrière, N., Locatelli, B., Laumonier, Y., Freycon, V., Bernoux, M., 2015. Soil erosion in the humid tropics: A systematic quantitative review. Agriculture, Ecosystems \& Environment, 203: 127-139. DOI:https://doi.org/10.1016/j.agee.2015.01.027
Le Bouteiller, C., Venditti, J.G., 2015. Sediment transport and shear stress partitioning in a vegetated

flow. Water Resources Research, 51(4): 2901-2922. DOI:doi:10.1002/2014WR015825
Le Gall, M. et al., 2018. Investigating the metal contamination of sediment transported by the 2016 Seine River flood (Paris, France). Environmental Pollution, 240: 125-139. DOI:https://doi.org/10.1016/j.envpol.2018.04.082
Leight, A.K., Hood, R.R., 2018. Precipitation thresholds for fecal bacterial indicators in the Chesapeake Bay. Water Research, 139: 252-262. DOI:https://doi.org/10.1016/j.watres.2018.04.004
Li, Y., Jia, Z., Wijesiri, B., Song, N., Goonetilleke, A., 2018. Influence of traffic on build-up of polycyclic aromatic hydrocarbons on urban road surfaces: A Bayesian network modelling approach. Environmental Pollution, 237: 767-774. DOI:https://doi.org/10.1016/j.envpol.2017.10.125
Liu, X. et al., 2017. Effect of water quality improvement on the remediation of river sediment due to the addition of calcium nitrate. Science of The Total Environment, 575: 887-894. DOI:https://doi.org/10.1016/j.scitotenv.2016.09.149
López-Tarazón, J.A., Estrany, J., 2017. Exploring suspended sediment delivery dynamics of two Mediterranean nested catchments. Hydrological Processes, 31(3): 698-715. DOI:doi:10.1002/hyp. 11069
Ly, S., Charles, C., Degré, A., 2011. Geostatistical interpolation of daily rainfall at catchment scale: the use of several variogram models in the Ourthe and Ambleve catchments, Belgium. Hydrol. Earth Syst. Sci., 15(7): 2259-2274. DOI:10.5194/hess-15-2259-2011
Mcmillan, S.K. et al., 2018. Before the storm: antecedent conditions as regulators of hydrologic and biogeochemical response to extreme climate events. Biogeochemistry(1): 1-15.
Moriasi, D.N. et al., 2007. Model evaluation guidelines for systematic quantification of accuracy in watershed simulations. Transactions Of the Asabe, 50(3): 885-900.
Nash, J.E., Sutcliffe, J.V., 1970. River flow forecasting through conceptual models part I - A discussion of principles. Journal of Hydrology, 10(3): 282-290. DOI:http://dx.doi.org/10.1016/0022-1694(70)90255-6
Nelson, E.J., Booth, D.B., 2002. Sediment sources in an urbanizing, mixed land-use watershed. Journal of Hydrology, 264(1): 51-68. DOI:https://doi.org/10.1016/S0022-1694(02)00059-8
Nerantzaki, S.D. et al., 2015. Modeling suspended sediment transport and assessing the impacts of climate change in a karstic Mediterranean watershed. Science of The Total Environment, 538: 288-297. DOI:https://doi.org/10.1016/j.scitotenv.2015.07.092
Noble, R.T. et al., 2003. Storm effects on regional beach water quality along the southern California shoreline. Journal of Water \& Health, 1(1): 23-31.
Nord, G., Esteves, M., 2010. The effect of soil type, meteorological forcing and slope gradient on the simulation of internal erosion processes at the local scale. Hydrological Processes, 24(13): 1766-1780. DOI:doi:10.1002/hyp. 7613
Ockenden, M.C. et al., 2016. Changing climate and nutrient transfers: Evidence from high temporal resolution concentration-flow dynamics in headwater catchments. Science of The Total Environment, 548-549: 325-339. DOI:https://doi.org/10.1016/j.scitotenv.2015.12.086
Ockenden, M.C. et al., 2017. Major agricultural changes required to mitigate phosphorus losses under climate change. Nature Communications, 8(1).
Ouyang, W., Jiao, W., Li, X., Giubilato, E., Critto, A., 2016. Long-term agricultural non-point source pollution loading dynamics and correlation with outlet sediment geochemistry. Journal of Hydrology, 540: 379-385. DOI:https://doi.org/10.1016/j.jhydrol.2016.06.043
Park, J., Hunt, J.R., 2018. Modeling fine particle dynamics in gravel-bedded streams: Storage and re-suspension of fine particles. Science of The Total Environment, 634: 1042-1053. DOI:https://doi.org/10.1016/j.scitotenv.2018.04.034
R Core Team, 2016. R: A Language and Environment for Statistical Computing, R Foundation for Statistical Computing, Vienna, Austria.
Ran, Q., Su, D., Li, P., He, Z., 2012. Experimental study of the impact of rainfall characteristics on runoff generation and soil erosion. Journal of Hydrology, 424-425: 99-111. DOI:https://doi.org/10.1016/j.jhydrol.2011.12.035
Rattan, K.J. et al., 2017. Quantifying seasonal variation in total phosphorus and nitrogen from prairie streams in the Red River Basin, Manitoba Canada. Science of The Total Environment, 575: 649-659. DOI:https://doi.org/10.1016/j.scitotenv.2016.09.073
Rodríguez-Blanco, M.L., Taboada-Castro, M.M., Taboada-Castro, M.T., 2013. Phosphorus transport into a stream draining from a mixed land use catchment in Galicia (NW Spain): Significance of runoff events. Journal of Hydrology, 481: 12-21. DOI:https://doi.org/10.1016/j.jhydrol.2012.11.046

Rodríguez-Blanco, M.L., Taboada-Castro, M.M., Taboada-Castro, M.T., 2019. An overview of patterns and dynamics of suspended sediment transport in an agroforest headwater system in humid climate: Results from a long-term monitoring. Science of The Total Environment, 648: 33-43. DOI:https://doi.org/10.1016/j.scitotenv.2018.08.118
Rodriguez-Lloveras, X. et al., 2015. Patterns of runoff and sediment production in response to land-use changes in an ungauged Mediterranean catchment. Journal of Hydrology, 531: 1054-1066. DOI:https://doi.org/10.1016/j.jhydrol.2015.11.014
Santos, R.M.B., Sanches Fernandes, L.F., Pereira, M.G., Cortes, R.M.V., Pacheco, F.A.L., 2015. A framework model for investigating the export of phosphorus to surface waters in forested watersheds: Implications to management. Science of The Total Environment, 536: 295-305. DOI:https://doi.org/10.1016/j.scitotenv.2015.07.058
Scutari, M., 2010. Learning Bayesian Networks with the bnlearn R Package. Journal of Statistical Software, 35(03): 2010.
Shen, Z., Chen, L., Liao, Q., Liu, R., Hong, Q., 2012. Impact of spatial rainfall variability on hydrology and nonpoint source pollution modeling. Journal of Hydrology, 472-473: 205-215. DOI:https://doi.org/10.1016/j.jhydrol.2012.09.019
Sherriff, S.C. et al., 2015. Investigating suspended sediment dynamics in contrasting agricultural catchments using ex situ turbidity-based suspended sediment monitoring. Hydrol. Earth Syst. Sci., 19(8): 3349-3363. DOI:10.5194/hess-19-3349-2015
Smith, T.B., Owens, P.N., 2014. Individual and cumulative effects of agriculture, forestry and metal mining activities on the metal and phosphorus content of fluvial fine-grained sediment; Quesnel River Basin, British Columbia, Canada. Science of The Total Environment, 496: 435-442. DOI:https://doi.org/10.1016/j.scitotenv.2014.07.014
Tammeorg, O., Möls, T., Niemistö, J., Holmroos, H., Horppila, J., 2017. The actual role of oxygen deficit in the linkage of the water quality and benthic phosphorus release: Potential implications for lake restoration. Science of The Total Environment, 599-600: 732-738. DOI:https://doi.org/10.1016/j.scitotenv.2017.04.244
Tan, Z. et al., 2017. A Global Data Analysis for Representing Sediment and Particulate Organic Carbon Yield in Earth System Models. Water Resources Research, 53(12): 10674-10700. DOI:doi:10.1002/2017WR020806
Thiessen, A.H., 1911. Precipitation Averages for Large Areas. Monthly Weather Review, 39(7): 1082-1084.
Uwimana, A., van Dam, A.A., Gettel, G.M., Irvine, K., 2018. Effects of agricultural land use on sediment and nutrient retention in valley-bottom wetlands of Migina catchment, southern Rwanda. Journal of Environmental Management, 219: 103-114. DOI:https://doi.org/10.1016/j.jenvman.2018.04.094
Vaezi, A.R., Ahmadi, M., Cerdà, A., 2017. Contribution of raindrop impact to the change of soil physical properties and water erosion under semi-arid rainfalls. Science of The Total Environment, 583: 382-392. DOI:https://doi.org/10.1016/j.scitotenv.2017.01.078
Vanmaercke, M., Poesen, J., Verstraeten, G., de Vente, J., Ocakoglu, F., 2011. Sediment yield in Europe: Spatial patterns and scale dependency. Geomorphology, 130(3): 142-161. DOI:https://doi.org/10.1016/j.geomorph.2011.03.010
Wang, C. et al., 2018. Synergistic removal effect of P in sediment of all fractions by combining the modified bentonite granules and submerged macrophyte. Science of The Total Environment, 626: 458-467. DOI:https://doi.org/10.1016/j.scitotenv.2018.01.093
Wang, F. et al., 2015a. Distinguishing the impacts of human activities and climate variability on runoff and sediment load change based on paired periods with similar weather conditions: A case in the Yan River, China. Journal of Hydrology, 527: 884-893. DOI:https://doi.org/10.1016/j.jhydrol.2015.05.037
Wang, G., Jiang, H., Xu, Z., Wang, L., Yue, W., 2012. Evaluating the effect of land use changes on soil erosion and sediment yield using a grid-based distributed modelling approach. Hydrological Processes, 26(23): 3579-3592. DOI:doi:10.1002/hyp. 9193
Wang, G., Wu, B., Zhang, L., Jiang, H., Xu, Z., 2014. Role of soil erodibility in affecting available nitrogen and phosphorus losses under simulated rainfall. Journal of Hydrology, 514: 180-191. DOI:https://doi.org/10.1016/j.jhydrol.2014.04.028
Wang, X.-q., Liu, Z.-c., Miao, J.-l., Zuo, N., 2015b. Relationship between nutrient pollutants and suspended sediments in upper reaches of Yangtze River. Water Science and Engineering, 8(2): 121-126. DOI:https://doi.org/10.1016/j.wse.2015.04.003
Wang, Y.-G., Tian, T., 2013. Sediment concentration prediction and statistical evaluation for annual

|  791 | load estimation. Journal of | Hydrology, 482: 69-78.  |
| --- | --- | --- |
|  792 | DOI:https://doi.org/10.1016/j.jhydrol.2012.12.043 |   |
|  793 | Weigelhofer, G., Ramião, J.P., Pitzl, B., Bondar-Kunze, E., O'Keeffe, J., 2018. Decoupled |   |
|  794 | water-sediment interactions restrict the phosphorus buffer mechanism in agricultural streams. |   |
|  795 | Science of The Total Environment, 628-629: 44-52. |   |
|  796 | DOI:https://doi.org/10.1016/j.scitotenv.2018.02.030 |   |
|  797 | Wijesiri, B., Deilami, K., Goonetilleke, A., 2018. Evaluating the relationship between temporal changes |   |
|  798 | in land use and resulting water quality. Environmental Pollution, 234: 480-486. |   |
|  799 | DOI:https://doi.org/10.1016/j.envpol.2017.11.096 |   |
|  800 | Wongsa, S., Shimizu, Y., 2004. Modelling artificial channel and land-use changes and their impact on |   |
|  801 | floods and sediment yield to the Ishikari basin. Hydrological Processes, 18(10): 1837-1852. |   |
|  802 | DOI:doi:10.1002/hyp. 1450 |   |
|  803 | Wu, Q., Qi, J., Xia, X., 2017. Long-term variations in sediment heavy metals of a reservoir with |   |
|  804 | changing trophic states: Implications for the impact of climate change. Science of The Total |   |
|  805 | Environment, 609: 242-250. DOI:https://doi.org/10.1016/j.scitotenv.2017.04.041 |   |
|  806 | Wu, X. et al., 2018. Effects of soil type and rainfall intensity on sheet erosion processes and sediment |   |
|  807 | characteristics along the climatic gradient in central-south China. Science of The Total |   |
|  808 | Environment, 621: 54-66. DOI:https://doi.org/10.1016/j.scitotenv.2017.11.202 |   |
|  809 | Xu, J. et al., 2018. Assessing temporal variations of Ammonia Nitrogen concentrations and loads in the |   |
|  810 | Huaihe River Basin in relation to policies on pollution source control. Science of The Total |   |
|  811 | Environment, 642: 1386-1395. DOI:https://doi.org/10.1016/j.scitotenv.2018.05.395 |   |
|  812 | Yan, R., Huang, J., Li, L., Gao, J., 2017. Hydrology and phosphorus transport simulation in a lowland |   |
|  813 | polder by a coupled modeling system. Environmental Pollution, 227: 613-625. |   |
|  814 | DOI:https://doi.org/10.1016/j.envpol.2016.09.093 |   |
|  815 | Yao, Y. et al., 2016. Assessment of mobilization of labile phosphorus and iron across sediment-water |   |
|  816 | interface in a shallow lake (Hongze) based on in situ high-resolution measurement. |   |
|  817 | Environmental Pollution, 219: 873-882. DOI:https://doi.org/10.1016/j.envpol.2016.08.054 |   |
|  818 | Yu, J. et al., 2017. Evaluation of simulated dredging to control internal phosphorus release from |   |
|  819 | sediments: Focused on phosphorus transfer and resupply across the sediment-water interface. |   |
|  820 | Science of The Total Environment, 592: 662-673. |   |
|  821 | DOI:https://doi.org/10.1016/j.scitotenv.2017.02.219 |   |
|  822 | Zhai, X., Xia, J., Zhang, Y., 2017. Integrated approach of hydrological and water quality dynamic |   |
|  823 | simulation for anthropogenic disturbance assessment in the Huai River Basin, China. Science |   |
|  824 | of The Total Environment, 598: 749-764. DOI:https://doi.org/10.1016/j.scitotenv.2017.04.092 |   |
|  825 | Zhang, Q., Ball, W.P., 2017. Improving riverine constituent concentration and flux estimation by |   |
|  826 | accounting for antecedent discharge conditions. Journal of Hydrology, 547: 387-402. |   |
|  827 | DOI:https://doi.org/10.1016/j.jhydrol.2016.12.052 |   |
|  828 | Zhang, Y., He, F., Xia, S., Zhou, Q., Wu, Z., 2015. Studies on the treatment efficiency of sediment |   |
|  829 | phosphorus with a combined technology of PCFM and submerged macrophytes. |   |
|  830 | Environmental Pollution, 206: 705-711. DOI:https://doi.org/10.1016/j.envpol.2015.08.018 |   |
|  831 | Zhang, Y. et al., 2018. Sedimentary lipid biomarker record of human-induced environmental change |   |
|  832 | during the past century in Lake Changdang, Lake Taihu basin, Eastern China. Science of The |   |
|  833 | Total Environment, 613-614: 907-918. DOI:https://doi.org/10.1016/j.scitotenv.2017.09.185 |   |
|  834 | Zhou, J., Zhang, M., Lu, P., 2013. The effect of dams on phosphorus in the middle and lower Yangtze |   |
|  835 | river. Water Resources Research, 49(6): 3659-3669. DOI:doi:10.1002/wrcr. 20283 |   |
|  836 | Zhou, X., Chen, N., Yan, Z., Duan, S., 2016. Warming increases nutrient mobilization and gaseous |   |
|  837 | nitrogen removal from sediments across cascade reservoirs. Environmental Pollution, 219: |   |
|  838 | 490-500. DOI:https://doi.org/10.1016/j.envpol.2016.05.060 |   |
|  839 | Zhu, A.X. et al., 2013. Modeling runoff and soil erosion in the Three-Gorge Reservoir drainage area of |   |
|  840 | China using limited plot data. Journal of Hydrology, 492: 163-175. |   |
|  841 | DOI:https://doi.org/10.1016/j.jhydrol.2013.03.038 |   |
|  842 | Zi, T., Kumar, M., Kiely, G., Lewis, C., Albertson, J., 2016. Simulating the spatio-temporal dynamics |   |
|  843 | of soil erosion, deposition, and yield using a coupled sediment dynamics and 3D distributed |   |
|  844 | hydrologic model. Environmental Modelling \& Software, 83: 310-325. |   |
|  845 | DOI:https://doi.org/10.1016/j.envsoft.2016.06.004 |   |
|  846 | Zorzal-Almeida, S. et al., 2018. Effects of land use and spatial processes in water and surface sediment |   |
|  847 | of tropical reservoirs at local and regional scales. Science of The Total Environment, 644: |   |
|  848 | 237-246. DOI:https://doi.org/10.1016/j.scitotenv.2018.06.361 |   |