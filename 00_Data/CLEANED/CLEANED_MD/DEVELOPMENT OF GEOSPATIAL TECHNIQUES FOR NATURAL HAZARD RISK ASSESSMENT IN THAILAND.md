# DEVELOPMENT OF GEOSPATIAL TECHNIQUES FOR NATURAL HAZARD RISK ASSESSMENT IN THAILAND 

Phoompanich S. ${ }^{1 *}$, S. Barr ${ }^{1}$, R. Gaulton ${ }^{1}$<br>${ }^{1}$ School of Engineering, Cassie Building, Newcastle University, NE1 7RU, United Kingdom (s.phoompanich2, stuart.barr, rachel.gaulton)@ncl.ac.uk

## Commission VI, WG VI/4

KEY WORDS: Multiple natural hazards, Machine learning, Geographic Information System, Naïve Bayes, Bayesian Network, National risk assessment


#### Abstract

: In order to mitigate environmental risk in Thailand it is essential to understand where and when specific geographic areas will be exposed to individual and multiple natural hazards. However, existing national scale approaches to natural hazard risk assessment are poorly adapted to deal with multiple hazards where significant uncertainties are associated with input variables and prior knowledge of the spatiotemporal nature of hazards is limited. To overcome these limitations, a geospatial approach has been developed that integrates machine learning within a GIS environment. Four hazards were investigated by Naïve Bayes while multiple hazards and their causalities were analysed via a Bayesian Network. Geospatial and Earth observation data representing past hazard events and their trigger variables were analysed to derive the probability of a hazard. Results revealed that lowland areas covering 22,868 and $139,193 \mathrm{~km}^{2}$, or $5 \%$ and $29 \%$ of total lowland areas were at-risk at a $90 \%$ probability-level of floods in rainy-seasons and droughts in the summer. High mountains and the plateaus were exposed to landslides over $90 \%$ probability in rainy, and forest fires in summer with over $60 \%$ probability, covering 37,727 and $40,069 \mathrm{~km}^{2}$, respectively. Within the Bayesian Network four relations of multiple hazards were investigated. At a $90 \%$ significance level approximately $190,250 \mathrm{~km}^{2}$ was at risk from a combination of forest fires and droughts. At a $80 \%$ or greater probability, $161,450,120,027$, and $102,628 \mathrm{~km}^{2}$ of land were at risk from a combination of 1) floods and landslides, 2) forest fires, floods, and landslides, and 3) all four hazards, respectively. The results were then used to produce the first fine-spatial scale multi-hazard assessment to support national policies on risk mitigation.


## 1. INTRODUCTION

Thailand routinely experiences intense natural hazards and also many coincident multi-hazard disruptions that cause enormous human impact and economic losses (DDPM, 2013b; DDPM, 2014). The spatiotemporal pattern of natural hazards are associated with topographical characteristics and climate conditions (TMD, 2015a; TMD, 2015b). In the rainy season, people living in areas of significant topographic relief are threatened from landslides after heavy rain, while flat plains are often overwhelmed by flooding. In the summer season many areas are subject to prolonged droughts that cause water shortages and forest fires. There is often the risk of coincident multi-hazard events, particularly debris flow and debris flood in several provinces such as Phrae (May 2001), Phetchabun (August 2001), and Uttaradit (May 2006); events have caused hundreds of deaths and over hundred million Thai baht of losses, or $£ 2.60$ million (DMR, 2011c; DMR, 2015; DMR, 2016b).

An investigation of areas that will be exposed to individual and multiple natural hazards is required for risk mitigation in the Twelfth national socio-economic development plan (2017-2021) of Thailand (NESDB, 2017). Natural hazards were found not to be independent of each other, both in space, time and causality; therefore, the understanding of their relations and interactions in a holistic manner to be able to fully quantify associated risk is essential risk reduction. However, existing national scale approaches for natural hazard assessment used in Thailand are mostly based on a knowledge-driven approach e.g. multi-criteria decision analysis and potential surface analysis (DDPM, 2007;

DDPM, 2011; GISTNorth, 2015; KU, 2013; ONEP, 1998; Waichareon, 2006; Wipulanusat et al., 2011). The approaches are not frequently updated and are difficult to implement. Also, the uncertainties from input variables and subjective evaluation that relies on knowledge and experience of experts can adversely affect results.

Machine learning (ML), a subset of artificial intelligence, has been shown to have the potential to robustly address natural hazard problems (Tehrany et al., 2014; Vogel et al., 2014). ML algorithms, namely Naïve Bayes (NB) and Bayesian Network (BN) based on Bayes' theorem rely on prior knowledge and learning from known input data for predicting hazard risks. These algorithms integrated with geospatial techniques have been used for assessing natural hazard risks such as landslides (Pham et al., 2016; Tsangaratos and Ilia, 2016), floods (Liu et al., 2017), and forest fires (Dlamini, 2010; Zwirglmaier et al., 2013). However, their use for assessing the spatiotemporal risk associated with multiple hazards is less well developed.

To address these issues, a geospatial approach employing ML for natural hazard assessment was developed in order to produce a fine-spatial scale national individual and multiple natural hazard risk assessment for Thailand. Geospatial and Earth observation (EO) data representing hazards and their trigger variables were used as input variables. An integrated machine learning algorithm and GIS-based approach were combined with expert prior knowledge on natural hazards, the analysis of past hazard events, and existing literature.

[^0]
[^0]:    * Corresponding author

## **2. STUDY AREA AND DATA SETS**

### **2.1 Natural Hazard Profile of Thailand**

Thailand is geographically situated in the Southeast Asia region, bordered by Myanmar, Laos, Cambodia, Malaysia, the Gulf of Thailand, and the Andaman Sea (Figure 1). The country is under the influence of the seasonal monsoons, the Inter Tropical Convergence Zone (ITCZ), and several cyclones (TMD, 2015a; TMD, 2015b; TMD, 2017). The southwest monsoon (SW) contributed abundant rainfall between May-October, or rainy season, and causes individual and multi-hazard disruptions in the upper part of the country (DDPM, 2013a; DDPM, 2013b; DDPM, 2014; NESDB, 2011). Between November and February, the northeast monsoon (NE) brings cold and dry air from China during the winter season. This combined with ITCZ and cyclones causes heavy rainfall and rainfall-induced landslides in southern regions (DMR, 2016a; TMD, 2015a; TMD, 2015b). The summer is a transitional period between the SW and the NE monsoons. During this period the weather becomes warmer and drier with a maximum temperature of 40°C (TMD, 2015a; TMD, 2015b; TMD, 2017). The climate conditions combined with topographical characteristics cause hydro-meteorological hazards in Thailand, accounting for enormous impacts to people, farmlands, infrastructure, and economic (TMD, 2015b).

![img-0.jpeg](img-0.jpeg)

Figure 1. Thailand and its neighbours with the monsoons and cyclones

### **2.2 Data Sets**

Existing geospatial and EO data were mainly used in this study. These data were categorized into 2 main groups: past hazard events and their triggering variables. Flood inundation (GISTDA, 2016), landslide scars and flash flood-prone area (DMR, 2011a; DMR, 2011b; DMR, 2011c; DMR, 2011d; DMR, 2015; DMR, 2016b), drought events derived from a combined satellite index from MODIS-MYD09A1 and MOD13A2, and monthly burnt areas from MODIS-MCD64A1 (LPDAAC, 2017) were used to characterize past hazards. Geospatial data on rock types, soil groups, streams and rivers, groundwater, temperature, relative humidity, roads, villages, irrigation zone, existing land use, and EO data, including daily precipitation from GSMaP (EORC/JAXA, 2017), SRTM DEM 90 m (CGIAR-CSI, 2017), land surface temperature (LST) from MODIS-MOD11A2, and vegetation health product derived from AVHRR (AVHRR-VHP) were compiled and used as potential factors to cause or trigger a hazard. For data pre-processing, ArcPy, a Python package in ArcGIS, was used to define projection, convert data, and spatial clipping of geospatial and EO data. The MODIS Reprojection Tool (MRT) was specifically used for processing MODIS data (Dwyer and Schmidt, 2006). All data were manipulated into a geodatabase and then converted to a raster file format with a 90-m spatial resolution, and a WGS84/UTM zone 47N coordinate system.

## **3. METHODOLOGY**

An integrated Python-based GIS approach where Naïve Bayes (NB) and Bayesian Network (BN) were employed for an assessment of the spatial probability of individual and multiple hazards was developed. Figure 2 shows the conceptual framework of an integrated spatiotemporal hazard assessment of individual and multiple hazards. The framework was divided into 5 stages as described below.

![img-1.jpeg](img-1.jpeg)

Figure 2. The conceptual framework of the individual and multiple hazard assessment

### **3.1 Selecting Potential and Contributing Factors of Hazards**

The potential and contributing factors i.e. floods, landslides, droughts, forest fires, and multiple hazards were investigated by learning from past hazard events, the literature, and prior knowledge from intensive and extensive one-to-one interviews of 24 experts in Thailand. This included an investigation of threshold values of the factors that cause or trigger a hazard. For example, daily rainfall over 100 mm on a slope over 30 degree has been shown to act as a trigger of landslides (DMR, 2011d). These threshold values were then used to classify precipitation of GSMaP data and SRTM DEM before input into the model. This stage was also performed for all hazard triggers.

### **3.2 Data Pre-processing and Transformation**

The NB and the BN models employ discrete variables; therefore, data pre-processing and transformations were required. Continuous data were converted to categorical data, while re-

quantisation was used for certain discrete data types to generate categorical groups. For ease of data processing in Python, the original values of geospatial data and multi-raster files were transformed to a numeric scale. For example, slopes below 30 degrees and slopes equal to or above 30 degrees as a trigger variable of landslides were transformed to 1 and 2. For an assessment of multiple hazards based on Boolean variables, threshold values of slopes were transformed to 0 and 1, representing non-contributing and contributing trigger values for a hazard.

### **3.3 Individual Hazard Assessment by Naïve Bayes (NB)**

The NB is a simple probabilistic ML classifier with the naïve assumption of independence between the factors. It assumes that all attributes are fully independent given the output class. Its advantage is its fast performance with less training data for supervised classification. Therefore, the NB algorithm was implemented for individual hazards. The NB classifier based on Bayes' theorem is computed as equation 1.

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

where, *P(A)* is the prior probability of the event A, *P(B)* is prior probability of the event B, *P(B|A)* is the likelihood probability of B given A, and *P(A|B)* is the posterior probability of A given B.

In this study, this theorem is applied for floods, landslides, droughts, and forest fires by determining how often a hazard occurs when potential factors cause or trigger a hazard. For example, the event of flooding was investigated when rainfall happens. Firstly, the prior probability was derived from the proportion of the events of flooding (F) and non-flooding (~F) in a training dataset. The likelihood probability was then calculated from each class of rainfall conditions (R) for F and ~F. Lastly, the posterior probability of both F and ~F was calculated from the probability of F and ~F given R by multiplying the prior and the likelihood probability (Mitchell, 1997). The results of both P(F|R) and P(~F|R) were equal to 1; therefore, they were normalized to maximize the posterior probability as equation 2. This probability ranging between 0-1 was used to generate a map of individual hazard assessment.

$$P(F|R) = \frac{P(F|R)}{P(F|R) + P(~F|R) \tag{2}$$

where, *P(F|R)* is the posterior probability of F given R, *P(~F|R)* is the posterior probability of ~F given R.

### **3.4 Multiple Hazard Assessment by Bayesian Network (BN)**

#### **3.4.1 Learning and Constructing the BN Structure and Its Nodes**

A directed acyclic graph (DAG) demonstrating the qualitative relationships between hazards and vulnerabilities was developed through expert knowledge and from an analysis of past events. In this study, the relationships between floods, landslides, droughts, and forest fires from dry to wet periods were investigated.

In dry period, the causalities between human-caused fires and droughts were presented by forest fires, humidity, temperature, vegetation losses, soil moisture, annual rainfall, and droughts. Fires caused low humidity, high temperature, and losses of vegetation cover that resulted in low soil moisture in burnt areas and their surroundings. These conditions together with low rainfall resulted in droughts. The network of floods and landslides considered as multiple hazards during wet periods was investigated by soil moisture, cyclones, daily rainfall, 3-day rainfall accumulation, floods, slope, and landslides. Cyclones caused heavy daily rain, high rainfall accumulation, and floods in combination with high soil moisture and steep slopes triggering landslides.

In the seasonal transitional period between April and May, the network of forest fires, floods, and landslides was developed where forest fires, vegetation losses, soil moisture, cyclones, daily rainfall, 3-day rainfall accumulation, floods, slope, and landslides were employed. Loss of vegetation cover in burnt areas results in a dramatic decline in soil moisture (Chankaew and Kurat, 1976). Dry soil is easily eroded by heavy rainfall or rainfall accumulation induced by cyclones and floods. These conditions combined with steep slopes trigger landslides in susceptible areas. Overall, all relationships of four hazards and their relative vulnerabilities were constructed in the overall DAG structure as shown in Figure 3.

![img-2.jpeg](img-2.jpeg)

**Figure 3.** The DAG presenting the causal relationships of forest fires, droughts, floods, and landslides.

#### **3.4.2 Determining the variables of nodes in the BN structure**

The variables representing in the DAG nodes were determined by geospatial and EO data. Past hazard events were used to characterize forest fires, droughts, floods, and landslides. Climatic conditions of relative humidity, maximum temperature, and the frequent cyclone-prone areas were used to characterize humidity, temperature, and cyclones, respectively. Annual rainfall, daily rainfall, and 3-day rainfall accumulation derived from GSMaP was processed and used in nodes of annual rainfall, daily rainfall, and 3-day rainfall accumulation, respectively. Existing land use, soil moisture from LST-MODIS data, and slope degree extracted from SRTM-DEM data were used in nodes of vegetation losses, soil moisture, and slope, respectively.

#### **3.4.3 Computing the Conditional Probabilities and the Joint Probability Distribution (JPD)**

After constructing the DAG, the quantitative relationships between nodes were derived through a conditional probability table (CPT). The conditional probabilities are the probability of the event A given the event B and can be calculated as the joint probability of 2 events occurring divided by the probability of the event B. The CPT of the nodes denoted the relations of the parent nodes to their child nodes. Illustrated by Figure 3, the conditional probabilities of all variables in the DAG were demonstrated by the JPD and calculated using equation 3.

$$
P(X)=\prod_{i=1}^{n} P\left(X_{i} \mid C_{i}\right)
$$

where, $P(X)$ represents the JPD of the nodes in the DAG, $P\left(X_{i} \mid C_{i}\right)$ presents the joint probability distribution of the parent $C_{i}$ given $X_{i}$, and $n$ represents hazards and their potential factors in the BN

### 3.5 Generating Maps of Individual and Multiple Hazards

Table 1 shows an example of the results derived from the NB model saved to a CSV format for flooding. For example, the probability of 0.9786 , or $98 \%$ was with the condition of daily rainfall over 90 mm , elevation below 100 m , agricultural land, well drained soils, drainage density over $1.00 \mathrm{~km} / \mathrm{sq} . \mathrm{km}$., water obstacle over $6.0 \mathrm{~km} / \mathrm{sq} . \mathrm{km}$, and the proximity to rivers below $2,364 \mathrm{~m}$. These classes from each variable represented by geospatial and EO data were used for generating a map of individual and multiple hazard assessment.

## 4. RESULTS AND DISCUSSION

### 4.1 Mapping Individual Hazard Assessment

Figure 4 shows maps of individual spatiotemporal hazard assessment and Table 2 presents the areas categorised by the probability. A description of each hazard is described as follows.
![img-3.jpeg](img-3.jpeg)

Figure 4. Maps of a spatiotemporal individual hazard assessment presenting the probability between 0-1


Table 1. An example of flood probability derived from the developed model in a CSV format
4.1.1 Flood Assessment: The highest probability of floods was 0.98 . A $90 \%$ probability covered approximately 22,868 , 22,249 , and $22,265 \mathrm{~km}^{2}$ of rainy, winter, and summer seasons, respectively. The spatial pattern of floods was mainly in low elevation areas close to rivers, particularly in the lower north region continuing to the central plain, and some coastal areas in the east of Thailand. The former area was subject to floods in rainy while the latter was highly exposed to floods in winter and summer seasons. This resulted from the NE monsoon in combination with ITCZ and cyclones contributing heavy rainfall in the east coast of Thailand.
4.1.2 Landslide Assessment: The highest probability was 0.99 , with over $90 \%$ probability covering $37,727,31,690$, and $38,271 \mathrm{~km}^{2}$ of rainy, winter, and summer seasons, respectively. These areas mainly found in northern and western regions and the mountain ridges in the south of Thailand. The temporal pattern of landslides and floods had the similar correlation but the spatial pattern of exposed areas were in high steep slope being to mountains and hills.
4.1.3 Drought Assessment: The highest probability was 0.99 , with a $90 \%$ probability covering $71,883 \mathrm{~km}^{2}$ of dry spell in rainy
and $139,193 \mathrm{~km}^{2}$ of droughts in summer seasons. These areas were mainly in plateaus in northeastern and plains in central regions, and part of river basin in northern and coastal plains of southern Thailand.
4.1.4 Forest fire Assessment: The highest probability was 0.85 , mainly in upland catchments and headwaters. Approximately $40,069 \mathrm{~km}^{2}$ in mountains and hills covered by deciduous forest in northern and central highland, northeast plateau, and upper western highland had a probability over 0.60 . The temporal pattern is associated with droughts in summer; a transitional period between the SW and the NE monsoons, leading to prolonged droughts.

Overall, the spatiotemporal pattern of individual hazards is dependent on terrain characteristics and a seasonality. Low lying areas were highly exposed to floods during the rainy season and droughts in summer, while high mountains and hills exposed to floods might trigger landslides in rainy season, and forest fires usually occurred in summer.


Table 2. Areas of a spatiotemporal individual hazard assessment categorized by the probability

### 4.2 Mapping Multiple Hazard Assessment

Four observed relations of forest fires, droughts, floods, and landslides were investigated following seasonality. They were 1) forest fires and droughts (MH1), 2) floods and landslides (MH2), 3) forest fires, floods, and landslides (MH3), and 4) forest fires, droughts, floods, and landslides (MH4). Due to a difference of minimum and maximum values, the probability of these four relations was normalized between $0-1$ in order to compare the spatial pattern of each relation. Figure 5 shows maps of the multihazard assessment categorized by their relationships and Table 3 shows the areas of a multi-hazard assessment.

![img-4.jpeg](img-4.jpeg)

Figure 5. Maps of a spatiotemporal multi-hazard assessment presenting the probability between $0-1$


Table 3. Areas of a multiple hazard assessment categorized by the probability

In dry period between November and April, most of MH1 with over $90 \%$ probability is found in the central plain, northeast plateau, and part of northern and western highland, covering an area of $190,250 \mathrm{~km}^{2}$, or $37 \%$ of total land. Between May and October the areas in northeast plateaus and west continental highlands, central highland, and part of mountains in the south of Thailand were exposed to MH2 in wet period with over $80 \%$ probability, covering $161,450 \mathrm{~km}^{2}$, or $32 \%$ of total land. The areas exposed to MH1 and MH2 were greater than MH3 and MH4, with approximately $10 \%$ difference of total land. Noticeably, the spatial pattern of MH1 was similar to exposed areas of forest fires and droughts, particularly in the upper part of the country. Areas in the west part of Thailand in the MH2 showed the same spatiotemporal pattern of floods and landslides.

In transitional period (MH3) between April and May, over 80\% probability found in the northeastern plateau, and eastern highland, and part of northern and western highlands, covering $120,027 \mathrm{~km}^{2}$, or $23 \%$ of total land. The overall multi-hazard assessment (MH4) demonstrated that approximately 102,628 $\mathrm{km}^{2}$, or $20 \%$ of total land, mainly in northeastern and eastern regions, and part of lower northern and western highlands had over $80 \%$ probability. These areas showed the same hazard pattern as the wet period, except the south of Thailand.

From above, most of the country was exposed to MH1 and MH2 while the southern region showed low spatiotemporal correlation

among four hazards because of the difference of the climatic conditions and topographical characteristics. During the rainy season the country is influenced by the monsoons and tropical cyclones between May and October while the southern region between October and May. This resulted in high humidity and high soil moisture that might cause floods and landslides, so human-caused fires were rare due to the difficulty of setting a fire in tropical evergreen forest or rain forest. Relation between forest fires and droughts in southern region was therefore low.

Overall, areas can be vulnerable to different hazards with or without temporal correlation. The pattern of individual hazards mainly depends on terrain characteristics and seasonal conditions such as low elevation areas exposed to floods in rainy and droughts in summer seasons. Conversely, an assessment of multiple hazards requires temporal correlation to be considered. Therefore, an investigation of multiple hazards and their relationships is an importance for determining exposed areas that will be harmed by more individual hazards. The different combinations denoting multiple hazards in different time periods provide the possible situations of the spatiotemporal hazard pattern. These results are an effective demonstration of investigating more individual hazards and their trigger variables. These can be used as a guidance of a national scale hazard assessment for risk mitigation in Thailand.

### 4.3 Model Evaluation

Sensitivity analysis is a practical method to quantify the uncertainties in the result from a model related to the uncertainties in its inputs (Aguilera et al., 2011; Salciccioli et al., 2016). It was often used for evaluating natural hazard studies (Liu et al., 2016; Liu et al., 2017; Stelzenmüller et al., 2010a; Stelzenmüller et al., 2010b). Therefore, three empirical techniques were designed to validate the relationships between the inputs and the outputs of the given model. The results were then used to assess the overall sensitivity of the model compared with the primary analysis.

Two techniques were used for evaluating individual hazards. The proportion of samples presenting a hazard and the creation of 10 new sets of samples were designed for computing the probability of a hazard. These samples were randomly created and overlaid with past hazard events. For the first technique, the samples presenting a presence of a hazard were proportioned by $60 \%$, $70 \%, 80 \%$, and $90 \%$ of the total hazard points. The set of these points were used to individually compute the probability of a hazard and the results of the probability were used to generate sensitivity analysis maps.

For evaluating multiple hazards, the whole boundary of the country was manually divided into 3 parts: upper (part I), middle (part II), and lower (part III). Each part was used to clip all multiple rasters representing input variables. All rasters of each part were then input into the model and recomputed the conditional probabilities of four relations. The results were then used to generate a sensitivity analysis map of a multi-hazard assessment.

To investigate the difference of the probability at each location, 100 points were randomly created and then used to extract multiple values of the probability from individual and multiple hazards. The statistics of mean and median were used for observation. The findings revealed that the average difference of individual hazards was $-0.00166,-0.00280,-0.00036$, and 0.02235 for floods, landslides, droughts, and forest fires, or less than $2 \%$ probability. Compared to the probability of multiple
hazards extracted from the full national study, there was a slight difference of the probability in upper and central parts, with below $5 \%$ probability. The probability of lower part showed a difference of over $10 \%$ probability for MH2, MH3, and MH4, with the probability of MH1 was below $5 \%$ probability. This is because the climate conditions of the southern region was different from other regions.

## 5. CONCLUSION

Based on the past hazard events and their potential factors, the spatiotemporal pattern of individual hazards is dependent on terrain characteristics and seasonality. Low land areas in central plains and plains in northeastern region were at-risk to floods during the rainy season and droughts in summer. High mountainous and hill areas of the plateaus in northern and western regions were exposed to rainfall-induced landslides in rainy season, particularly susceptible areas with high steep slopes while these areas were also subject to forest fires in summer. For multiple hazards, the causal relationships between MH1 (forest fires and droughts) and MH2 (floods and landslides) showed the high probability with large coverage areas more than MH3 (forest fires, floods, and landslides) and MH4 (forest fires, droughts, floods, and landslides).

An integrated Python-based GIS approach along with NB and BN algorithms is able to determine the probability of individual hazards and the conditional probabilities of multiple hazards. The maps produced provide effective information of spatiotemporal hazard assessment and helps the understanding of causal relationships between hazards for prioritizing the most critical areas for risk mitigation. The methods developed in this study provide a data-driven approach for hazard assessment that can be applied to other areas at different scales. The approach allows frequent update, ease of implementation, and fast computation. However, there were still requirements to further enhance the approach to better consider contributing factors and their threshold values, to undertake a more detailed investigation of the causal relationships between hazards, and complete information of past hazard events.

## ACKNOWLEDGEMENTS

The author would like to thank 24 experts who provided their prior knowledge of natural hazard risk and supporting data sets used for hazard assessment. Special thanks to Jedsada Phengsawan, Ph.D. student in School of Computing, Newcastle University, for the contribution in the development of Python integrated with GIS for NB and BN algorithms.
