## OPEN ACCESS

EDITED BY
Wei Zhao,
Institute of Mountain Hazards and Environment (CAS), China

REVIEWED BY
Shuai Chen,
Central South University, China
Paraskevas Tsangaratos,
National Technical University of Athens,
Greece
Himan Shahabi,
University of Kurdistan, Iran
*COREESPONDENCE
Shengwu Qin,
(c) qinsw@jlu.edu.cn

SPECIALTY SECTION
This article was submitted to Geohazards and Geonsks, a section of the journal Frontiers in Earth Science

RECEIVED 07 December 2022
ACCEPTED 21 March 2023
PUBLISHED 30 March 2023

## CITATION

Lv J, Qin S, Chen J, Qiao S, Yao J, Zhao X, Cao R and Yin J (2023), Application of different watershed units to debris flow susceptibility mapping: A case study of Northeast China.
Front. Earth Sci. 11:1118160.
doi: 10.3389/feart.2023.1118160
COPYRIGHT
(c) 2023 Lv, Qin, Chen, Qiao, Yao, Zhao, Cao and Yin. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## Application of different watershed units to debris flow susceptibility mapping: A case study of Northeast China

Jiangfeng $\mathrm{Lv}^{1,2}$, Shengwu Qin ${ }^{1 *}$, Junjun Chen ${ }^{1}$, Shuangshuang Qiao ${ }^{1}$, Jingyu Yao ${ }^{1}$, Xiaolan Zhao ${ }^{2}$, Rongguo Cao ${ }^{2}$ and Jinhang Yin ${ }^{2}$<br>${ }^{1}$ College of Construction Engineering, Jilin University, Changchun, China, ${ }^{2}$ China Water Resources Bei Fang Investigation, Design \& Research Co. LTD., Tianjin, China

The main purpose of this study was to compare two types of watershed units divided by the hydrological analysis method (HWUs) and mean curvature method (CWUs) for debris flow susceptibility mapping (DFSM) in Northeast China. Firstly, a debris flow inventory map consisting of 129 debris flows and 129 non-debris flows was randomly divided into a ratio of $70 \%$ and $30 \%$ for training and testing. Secondly, 13 influencing factors were selected and the correlations between these factors and the debris flows were determined by frequency ration analysis. Then, two types of watershed units (HWUs and CWUs) were divided and logistic regression (LR), multilayer perceptron (MLP), classification and regression tree (CART) and Bayesian network (BN) were selected as the evaluation models. Finally, the predictive capabilities of the models were verified using the predictive accuracy (ACC), the Kappa coefficient and the area under the receiver operating characteristic curve (AUC). The mean AUC, ACC and Kappa of four models (LR, MLP, CART and BN) in the training stage were 0.977 , 0.931 , and 0.861 , respectively, for the HWUs, while $0.961,0.905$, and 0.810 , respectively, for the CWUs; in the testing stage, were $0.904,0.818$, and 0.635 , respectively, for the HWUs, while $0.883,0.800$, and 0.601 , respectively, for the CWUs, which showed that HWU model has a higher debris flow prediction performance compared with the CWU model. The CWU-based model can reflect the spatial distribution probability of debris flows in the study area overall and can be used as an alternative model.

## KEYWORDS

debris flow susceptibility mapping, watershed units, hydrological analysis method, mean curvature method, machine learning model

## 1 Introduction

According to the China Statistical Yearbook (http://www.stats.gov.cn/tjsj/ndsj/), a total of 7,840 geological disasters occurred in China in 2020, resulting in 197 casualties and direct economic losses of 740 million dollars, of which debris flows accounted for $11.46 \%$. Debris flows are among the most frequent and destructive disasters in mountainous areas (Dash et al., 2022; Jiang et al., 2022; Qiu et al., 2022). Debris flow susceptibility mapping (DFSM), representing where debris flows are likely to occur, plays an important role in debris flow management strategies and has been a hot

topic in disaster research worldwide (Ilia and Tsangaratos, 2015; Qin et al., 2019; Sun et al., 2021; Yao et al., 2022).

There are many uncertainties in the process of disaster susceptibility mapping, such as selecting appropriate mapping units, determining evaluation models, screening influencing factors, determining the proportion of training and testing data and others (Tien Bui et al., 2015; Cama et al., 2016; Zezere et al., 2017; Chen et al., 2018; Du et al., 2018; Dou et al., 2019; Qiao et al., 2021). Among the above uncertainty factors, selecting appropriate mapping units is the first step to address disasters and environmental factors. The mapping unit is the basic functional spatial element for dividing the study area (Cama et al., 2016). The term refers to a portion of the land surface which contains a set of ground conditions that differ from the adjacent units across definable boundaries (Van Den Eeckhaut et al., 2009). The selection of mapping units affects the methods used to address the uncertainty in the input data, the model fitting, the reliability of disaster susceptibility mapping and the application of disaster susceptibility mapping in disaster prevention and mitigation (Fausto Guzzetti et al., 1999; Cama et al., 2016; Qiao et al., 2021). At present, mapping units mainly include the following classes: grid cell units, slope units, watershed units, topographic units, geohydrological units, political or administrative units, and unique condition units (Van Den Eeckhaut et al., 2009; Chen et al., 2019; Sun et al., 2020).

For DFSM, grid cell units and watershed units are used frequently. Grid cell units are the most popular mapping units

![img-0.jpeg](img-0.jpeg)

FIGURE 1 The geographic location of the study area.

![img-1.jpeg](img-1.jpeg)

FIGURE 2 Geological map and debris flow field photos of the study area: (A) geological map; (B–E) debris flow field photos.

with the same cell size, fast processing speed and simple algorithm (Reichenbach et al., 2018). However, the division of grid cells destroys the integrity of debris flows and is almost completely unrelated to geological and topographic information (Dragut and Eisank, 2011; Wang et al., 2017). Moreover, since debris flows are a dynamic process, the DFSM based on grid cell units cannot comprehensively reflect spatial information (Qin et al., 2019). Watershed refers to the river catchment area that is surrounded by the water-parting line; it is the basic unit for the development and activity of debris flows, and it is the object of exploration, research, and prevention of debris flows. Furthermore, the watershed unit includes the formation area, circulation area, and accumulation area of a debris flow (Qin et al., 2019). Compared with grid cell units, watershed units can completely consider the spatial information of a debris flow. Some scholars have carried out DFSM based on watershed units and obtained reliable results. Qin et al. (2019) explored the accuracy and practicability of mapping units for the evaluation of debris flow susceptibility based on grid cell units and watershed units, and the results showed that watershed units were more feasible than grid cell units when considering the effects of geology and geomorphology on the occurrence of debris flows. Qiao et al. (2021) proposed a region-partitioning method for DFSM based on the topographic characteristics of watershed units, and the results demonstrated that this method can enable more reasonable regional-scale DFSM. Li et al. (2017) presented an application of the rock engineering system and fuzzy C-means algorithm for debris flow susceptibility assessment using watershed units as mapping units in the Wudongde Dam area, the evaluation results agreed well with field investigations. Zou et al. (2019) developed a quantitative method for regional risk assessment of debris flows by analyzing in-depth the relationships among hazard-forming environments, disaster factors and elements at risk based on hydrological response units. The presented method may serve as pertinent guidance for regional risk assessment of debris flows. In addition, some scholars have used watershed units to evaluate and compare the performance of different evaluation models for DFSM (Liang et al., 2020; Xiong et al., 2020), and the conclusions provide helpful data for assessing and mitigating debris flow hazards. Therefore, it is important to carry out research based on watershed units, which provide more evidence and views for DFSM research. The commonly used watershed units are based on the hydrological analysis model, also known as hydrological response units (Li et al., 2021). In addition, watershed units can be generated based on the mean curvature model (Romstad and Etzelmüller, 2012). To compare the results of applying different watershed units in DFSM, we extracted the watershed units based on the hydrological analysis method and mean curvature method in the study.

There are plenty of evaluation models for disaster susceptibility mapping, from qualitative approaches to quantitative approaches (Aditian et al., 2018; Huang et al., 2020; Asadi et al., 2022). Qualitative methods are based on air photo and field interpretation and the opinions of an individual or a group of experts (Aditian et al., 2018; Ghasemian et al., 2022b). Some qualitative methods include ranking and weighting, such as analytic hierarchy process and weighted linear combination (Ayalew and Yamagishi, 2005; Rozos et al., 2010). These qualitative or semi-quantitative methods are subjective and highly dependent on experts' knowledge, and are not suitable for large-scale research fields (Bälteanu et al.,

![img-2.jpeg](img-2.jpeg)

FIGURE 3 Classification process of the watershed units: (A) hydrological analysis method and (B) mean curvature method.

2010). Quantitative statistical models are built based on appropriate mathematical models to analyze the statistical relations between disasters and influencing factors (Hadinoko et al., 2017; Ghasemian et al., 2022b), including the information value (Xu et al., 2012), certainty factor concepts (Devkota et al., 2012), frequency ratio method (Balamurugan et al., 2016), bivariate statistical analysis (Ayalew and Yamagishi, 2005), index of entropy (Shirani et al., 2018), weight of evidence (Constantin et al., 2010), evidential belief functions (Carranza, 2014), logistic regression (Cao et al., 2019), etc. Machine learning models are now widely used because these models can analyze the non-linear corrections between past events and the influencing factors and they predict where disasters will occur (He et al., 2012; Xiong et al., 2020). These models include artificial neural networks (Pham et al., 2017; Chen et al., 2021; Chen et al., 2022), support vector machines (Colkesen et al., 2016), random forest (Hong et al., 2016), decision trees (Althuwaynee et al., 2014), classification and regression tree (Youssef et al., 2015), boosted regression trees (Xiong et al., 2020), Bayesian network (Song et al., 2012), adaptive neuro-fuzzy inference (Jaafari et al., 2019), logistic model tree (Tien Bui et al., 2015) and random gradient descent (Hong et al., 2020). Reichenbach et al. (2018) reviewed the statistically-based landslide susceptibility assessment literature from 1983 to 2016, and found that the most common statistical methods for landslide susceptibility modeling include logistic regression, neural network analysis, data-overlay and index-based and weight of evidence analyses. In this study, to avoid the model uncertainty caused by different evaluation models, we use logistic regression (LR), multilayer perceptron (MLP), classification and regression tree (CART) and Bayesian network (BN) to carry out DFSM based on two types of watershed units.

This study compared and analyzed the applicability of two different watershed units in regional DFSM based on four models (LR, MLP, CART, and BN). The main purpose is to support the selection of watershed units for DFSM. Yongji county in the Jilin Province, China was taken as the study region because it is under serious threat of frequent debris flows. The division process and results of two types of watershed units were compared. Eight DFSMs are discussed and AUC, ACC, and Kappa analyses were used to evaluate the accuracy of the debris flow susceptibility models.

![img-3.jpeg](img-3.jpeg)

FIGURE 4
Division of watershed units: (A) hydrological analysis method and (B) mean curvature method.

## 2 Study area

### 2.1 General settings

Yongji county is located in central eastern Jilin Province, China (Figure 1), which covers a total area of 2,620 km². The number of debris flows in Yongji county has increased from 71 in 2007 to 129 in 2021, causing several deaths, destroying hundreds of houses and thousands of acres of farmland. The debris flows scoured the roadbed and piled up on the road, resulting in traffic paralysis. It is necessary and urgent to map the susceptibility of debris flows in Yongji county.

The study area lies between 125°48′09″E to 126°40′01″E longitude and 43°18′07″N to 43°35′00″N latitude. There are four landforms in the entire area: middle mountains, low mountains, platform, and river valley. From southeast to northwest, the landforms of the study area are middle mountains, low mountains and platform with the altitudes ranging from 1,386 to 182 m. In addition to several andesites and metamorphic rocks, the main rock type is Yanshan Early Granite. The study area lies in the Tianshan–Xingan geosyncline fold area of the Jilin and Heilongjiang fold system (Qin et al., 2019). Folds and faults are relatively developed in Yongji county, which provides conditions for the occurrence of geological disasters (Figure 2A). Yongji county is in the mid-latitude subtemperate continental climate zone with an annual average precipitation of 722.75 mm. There are 39 rivers covering an area of more than 20 km². The main rivers include the Yinma River, Wende River, Chalu River and Aolong River.

### 2.2 Debris flow data inventory

A debris flow inventory map is a prerequisite for DFSM(Xu et al., 2012; Arabameri et al., 2020; Dash et al., 2022). A total of 129 debris flows were collected based on field surveys and historical materials. Figure 2A shows that debris flows are mainly distributed across the southeast mountain area. Statistics show that among 129 debris flows, only 7 are medium in size and 122 are small. In recent years, the increase in debris flow frequency in Yongji county has been closely related to deforestation and reclamation. With the destruction of forest vegetation, rainfall is more likely to cause soil erosion, which gradually forms a series of gullies. These gullies provide circulation conditions for debris flows. Figures 2B–E shows some images of occurred debris flows in the study area.

## 3 Watershed units

### 3.1 Division methods for different watershed units

In this study, the extraction of watershed units was completed in ArcGIS 10.2 software (Tien Bui et al., 2015; Cao et al., 2019). The most commonly used watershed units (HWUs) are classified by the hydrological principles (Fausto Guzzetti et al., 1999). HWUs are derived based on an 8-direction flow algorithm (Horton et al., 2013). Establishing the HWUs consists of the following six steps: 1) filling the original DEM, 2) extracting the flow direction, 3) calculating the flow accumulation, 4) extracting river networks based on a threshold, 5) stream linking, 6) dividing HWUs based on flow direction and stream linking. The detailed classification process is shown in Figure 3A.

In addition, watershed units can be generated based on the mean curvature method (CWUs). The mean curvature is a simple combination of profile curvature and plan curvature. Its maximum and minimum values can indicate the changes in aspect and slope positions at the same time. Therefore, the mean curvature can reflect the ridge line, valley line, platform edge and wide valley edge (Romstad and Etzelmüller, 2012). Establishing the CWUs consists of the following five steps: 1) smoothing the original

![img-4.jpeg](img-4.jpeg)

FIGURE 5
Flowchart of the research methodology.

DEM, 2) calculating the mean curvature, 3) extracting the flow direction, 4) filling depressions based on flow direction data, and 5) dividing CWUs based on flow direction and depressions. The detailed classification process is shown in Figure 3B.

### 3.2 Watershed unit classification results

For HWUs, the number and size are closely related to DEM resolution and flow threshold, but for CWUs, the control factor is

![img-5.jpeg](img-5.jpeg)

FIGURE 6
(Continued)

only DEM resolution. For HWUs, flow threshold values of 500, 1,000, 2,000, 5,000, and 10,000 were chosen based on a DEM with a resolution of 30 m. For CWUs, we resampled the DEM with resolutions of 50, 100, 200, 300, 500, and 1,000. To ensure that the number and size of the two types of watershed units were not much different and consistent with the actual watersheds, a flow

![img-6.jpeg](img-6.jpeg)

threshold of 1,000 and a DEM resolution of 300 were selected to divide the watershed units. For the HWUs, the study area was divided into 1,092 watershed units. The smallest unit was 0.10 km², the largest unit was 13.63 km², and the mean size was 2.40 km² (Figure 4A). For CWUs, the study area was divided into 1,211 watershed units. The smallest unit was 0.11 km², the largest unit was 8.87 km², and the mean size was 2.17 km² (Figure 4B).

![img-7.jpeg](img-7.jpeg)

FIGURE 6 (Continued). Maps of influencing factors based on HWUs with a flow threshold of 1,000: (A) watershed area; (B) relative height difference; (C) watershed slope; (D) mean curvature; (E) fault density; (F) river density; (G) SPI; (H) TWI; (I) NDVI; (J) landforms; (K) precipitation; (L) land use; (M) lithology.

## 4 Materials and methods

The flowchart of the research methodology is shown in Figure 5. DFSM of Yongji county using four models (LR, MLP, CART, and BN) and watershed units (HWUs and CWUs) have been carried out in five main steps: 1) data collection and screening influencing factors, 2) division of two types of watershed units, 3) calculation of frequency ratio values (FRs) for all influencing factors, 4) building debris flow models and constructing DFSM, and 5) debris flow model validation and comparison using AUC, ACC and Kappa.

### 4.1 Screening influencing factors

The occurrence of debris flows is affected by many factors including topographic, geomorphologic, geological, ecological and meteorological factors (Zhang et al., 2012; Bregoli et al., 2014; Hu et al., 2014). Based on field observations, available literature and expert experience, fourteen influencing factors were considered, such as watershed area, relative height difference, watershed average elevation, watershed slope, mean curvature, fault density, river density, stream power index (SPI), topographic wetness index (TWI), plan normalized difference vegetation index (NDVI), landforms, precipitation, land use and lithology.

Because substantial collinearity will lead to model instability, collinearity analysis is essential before influencing factors are applied for DFSM (Qiu et al., 2022). Person's correlation coefficient was calculated to test the collinear relationship among these factors, and the results are shown in Table 1. There is no correlation coefficient when the absolute value is less than 0.7 (Dormann et al., 2013; Yao et al., 2022). There was high collinearity between relative height difference and watershed average elevation, and the Person's correlation coefficient was 0.86. In addition, the value of collinearity between watershed average elevation and precipitation was 0.69. Therefore, the watershed average elevation was eliminated.

The watershed area, relative height difference, watershed slope, mean curvature, SPI and TWI were extracted from the DEM with a resolution of 30 m. Fault, river, and lithology data were acquired from the geological map of Yongji county and field investigations. The Landsat 8 image taken on 11 August 2021, was used to produce the NDVI. Landforms, precipitation, and land use were provided by government reports. Thirteen influencing factors were converted to a grid cell with a resolution of 30 m in ArcGIS 10.2 (Chen et al., 2017). Table 2 shows date source and scale of influencing factors. When watershed units are applied to DFSM, grid patterns for each factor need to be transferred to the corresponding watershed units. For watershed area, geometric calculation in the attribute table was used to calculate the area of each watershed. The difference between the highest and the lowest points in each watershed was calculated as a relative height difference (Qin et al., 2019). For watershed slope, mean curvature, SPI, TWI, and NDVI, the zonal statistics tool in the spatial analysis was used and the statistical type was "mean." The length of faults and rivers in each watershed was extracted by using the intersection tool, and then, the fault density and river density in each watershed were calculated using the field calculator. Precipitation for each watershed was determined based on the principle of majority, and this principle was also applied to factors of landforms, land use and lithology. The data types of precipitation, landforms, land use and lithology are discrete, while the data types of other factors are continuous. The influencing factor layers based on HWUs with a flow threshold of 1,000 are shown in Figure 6.

The FRs of the influencing factor subclass were used as the input variable of the DFSM models (Huang et al., 2020). Based on a series of previous studies (Xu et al., 2012; Aditian et al., 2018; Vakhshoori et al., 2019; Chang et al., 2020), we divided the continuous factor into eight levels using the natural fracture method. Taking HWUs with a flow threshold of 1,000 as an example, the FRs for each level of thirteen factors are shown in Table 3.

### 4.2 Logistic regression (LR)

Logistic regression (LR) may be the most widely used statistical technique in susceptibility assessment (Colkesen et al., 2016). As a multivariate regression method, LR can find a model to describe the relationship between multiple independent variables and a dependent variable (Lee and Pradhan 2006; Lee 2007; Pourghasemi et al., 2013). For DFSM, the influencing factors are considered the independent variables and the occurrence and non-occurrence of debris flows are considered the dependent variables. For LR, variables may be continuous, discrete or arbitrary combinations of two types (Lee, 2007). LR can be expressed as follows (Ayalew and Yamagishi 2005; Yalcin et al., 2011; Schlögel et al., 2018):

$$P = \frac{1}{1 + e^{-z}} \tag{1}$$

$$Z = \alpha + \beta_1 x_1 + \beta_2 x_2 + \ldots \beta_n x_n \tag{2}$$

where *P* denotes the probability of a debris flow occurrence in each watershed, varying between 0 and 1; *Z* represents the dependent variable including non-debris flows (0) and debris flows (1); *α* represents the

TABLE 1 The results of the Person's Correlation Coefficient.


('WA' represents 'Watershed area', 'E' represents 'Watershed average elevation', 'RHD' represents 'Relative height difference', 'WS' represents 'Watershed slope', 'F' represents 'Fault density', 'R' represents 'River density', 'NDVI' represents 'Plan normalized difference vegetation index', 'SPI' represents 'Stream power index', 'TWI' represents 'topographic wetness index', 'Pre' represents 'precipitation', 'MC' represents 'mean curvature', 'LU' represents 'Land use', 'LF' represents 'Landforms' and 'Li' represents 'Lithology').

TABLE 2 Date source and scale of influencing factors.


intercept of the regression function, $\beta_{1}, \beta_{2}, \ldots \beta_{n}$ are the regression coefficients; and $x_{1}, x_{2}, \ldots x_{n}$ are the debris flow influencing factors.

### 4.3 Multilayer perceptron (MLP)

Multilayer perceptron (MLP) is a kind of artificial neural network and has been widely used in classification (Tien Bui et al., 2015; Pham et al., 2017). The MLP generally consists of three main components, namely, input layers, hidden layers, and output layers (Kavroglu and Mather 2003). For DFSM, the input layers are considered the influencing factors of debris flow, the output layers are considered the classification result of inferring debris flow or non-debris flow, and the hidden layers are considered the classification layers that convert input into output. The MLP model with only one hidden layer is the most basic three-tier structure model, which can fit and predict many

TABLE 3 Description and FRs of all the influencing factors (HWUs with a flow threshold of 1,000).


TABLE 3 (Continued) Description and FRs of all the influencing factors (HWUs with a flow threshold of 1,000).


TABLE 3 (Continued) Description and FRs of all the influencing factors (HWUs with a flow threshold of 1,000).



**TABLE 4** Confusion matrix.


non-linear problems (Li et al., 2019). In this study, a single-hidden-layer MLP model is used in DFSM. For example, *n_{0}*, *n_{1}* and *n_{2}* represent the number of input, hidden and output layers, respectively, and the input variables are X = {*x*_{1}, *x*_{2}, ..., *x_{nh*}}. Then, the input and output of the hidden layer are: (Li et al., 2019; Huang et al., 2020):

$$ z_{j} = \sum_{i=1}^{n_{0}} w_{ij} x_i + b_{j} $$

$$ y_j = f\left(z_{j} \right) = \left(1 + e^{-z_j} \right)^{-1} $$

where *z_{j}*, *b_{j}* and *y_{j}* represent the *y* th input variable, threshold value and output variable of the neuron in the hidden layer, respectively, *w_{ij}* represents the weight value between the *i* th input neuron and the *j* th neuron in the hidden layer, and *f* (*z_{j}*) represents the activation function. Then the input and output of neurons in the output layer are:

$$ z_k = \sum_{j=1}^{n_k} w_{jk} y_i + b_k $$

$$ y_k = z_k $$

where *z_{k}*, *b_{k}* and *y_{k}* represent the *j* th input variable, threshold value and output variable of the neuron in the output layer, respectively, *w_{ik}* represents the weight value between the *j* th neuron in the hidden layer and the *k* th output neuron.

### 4.4 Classification and regression tree (CART)

The decision tree model is a technique that uses a tree structure to discover and describe structural patterns in data. It does not require a preestablished relationship between all input variables and a target variable (Hitoshi Saito and Matsuyama, 2009). As an algorithm of the decision tree model, classification and regression tree (CART) was first proposed by Breiman et al. (1984). The CART consists of a root node, a set of internal nodes and a set of leaf nodes. The leaf nodes correspond to the classification result, and the other nodes correspond to the classification rules. CART was selected as the decision tree model in this study in view of its performance efficiency (Wang et al., 2015).

### 4.5 Bayesian network (BN)

The Bayesian network (BN) is a graphical model for probabilistic relationships among a set of variables (Song et al., 2012). BN can be represented by directed acyclic graphs and conditional probabilities, reflecting the independent and interdependent relationship among various variables. The calculation formula is given as follows (Han et al., 2019):

$$ P(L, M, N) = P(L) \times P(M|L) \times P(N|L, M) $$

where *P(L)* is the prior probability, indicating the conditional probability without the parent node, *P(M|L)* is the conditional probability, indicating the occurrence probability of *M* under *L* conditions and *P(N|L, M)* is the conditional probability, indicating the occurrence probability of *N* under *L* and *M* conditions.

### 4.6 Model performance evaluation

In this study, three commonly used criteria, including the predictive accuracy (ACC), the Kappa coefficient and the area under the receiver operating characteristic curve (AUC) were used to evaluate the prediction ability of DFSMs. The calculation of the three criteria is based on the confusion matrix (Ghasemian et al., 2022a). The confusion matrix, also known as the error matrix, is a standard format for accuracy evaluation. The confusion matrix can represent the difference between the model prediction results and the actual observation results (Xiong et al., 2020). In this study, the confusion matrix of the debris flow susceptibility predictive models is shown in Table 4. For example, a true positive (TP) suggests that the prediction result is 'Debris-Flow', and the actual observation result is 'Debris-Flow'.

The predictive accuracy (ACC) represents the ratio of correctly predicted observations to total observations. This index shows how well the debris flow model works:

$$ ACC = \frac{TP + TN}{TP + FN + FP + TN} $$

The Kappa index is used to assess the acceptability of debris flow models which can be calculated by:

![img-8.jpeg](img-8.jpeg)

FIGURE 8
(Continued)

$$K = \frac{p_0 - p_r}{1 - p_r}$$

$$p_r = \frac{A \times a + B \times b}{n^2}$$

where *K* is the Kappa coefficient; *p*<sub>0</sub> is overall classification accuracy, namely, ACC; *A* is the actual number of debris flows, and it is also the sum of TP and FN (Table 4); *B* is the actual number of non-debris flows, and it is also the sum of FP.

![img-9.jpeg](img-9.jpeg)

FIGURE 8 (Continued). Eight DFSMs: (A) DFSM of HWUs and LR; (B) DFSM of HWUs and MLP; (C) DFSM of HWUs and CART; (D) DFSM of HWUs and BN; (E) DFSM of CWUs and LR; (F) DFSM of CWUs and MLP; (G) DFSM of CWUs and CART and (H) DFSM of CWUs and BN.

and TN; *a* is the predicted number of debris flows, and it is also the sum of TP and FP; *b* is the predicted number of non-debris flows, and it is also the sum of FN and TN; *n* is the total number of samples, and it is also the sum of *A* and *B* or *a* and *b*. The *K* varies from 0.0 to 1.0, the higher the *K* value is, the better the classification accuracy of the model.

The receiver operating characteristic (ROC) curve and area under the curve (AUC) can compare the prediction performance of different classifiers (Akgun et al., 2012). The abscissa and ordinate of the ROC are the false-positive rate (FPR) and true-positive rate (TPR) respectively. They can be obtained from the following equations (Pourghasemi et al., 2013):

$$
FPR = \frac{FP}{FP + TN} \tag{11}
$$

$$
TPR = \frac{TP}{TP + FN} \tag{12}
$$

AUC represents the quality of models that reliably predict the occurrence or non-occurrence of debris flows. The AUC varies from 0.5 to 1.0, and the higher the AUC value is, the better the prediction performance of the model.

# 5 Results and validation

## 5.1 Model parameters

The whole analysis process was implemented in IBM SPSS software (Sun et al., 2019; Sun et al., 2021). For LR, the forward step mode was adopted to screened variables. For BN model, the mechanism type was Tree Augmented naive Bayes (TAN), and Bayesian adjustment of small cell count was selected as a parameter learning method. For MLP, one hidden layer was selected, and the maximum training time was used as the termination rule. For CART, the maximum tree depth was set to 10, and percentage was used as the termination rule. Other parameters are default.

## 5.2 Contribution of debris flow influencing factors

The Chi-Squared statistic was employed to identify the most important factors affecting the occurrence of debris flows in the study area (Ghasemian et al., 2022a). Figure 7 shows that landforms have the highest impact (128.5) on debris flows in the study area, followed by relative height difference and SPI (114.5), watershed slope (110.5), TWI (82.5), precipitation (74.5), lithology (60), land use (43.5), watershed area (27.5), river density (26.5), mean curvature (24), NDVI (23), and fault density (21.5).

## 5.3 Spatial datasets for model building

According to field surveys and historical materials, a total of 129 debris flows were collected. Meanwhile, 129 non-debris flows were selected, which were at least 500 m away from the nearest debris flow (Figure 4) (Dou et al., 2019; Sun et al., 2020). Assigned 1 and 0 for debris flows and non-debris flows, respectively. The FRs of the thirteen influencing factors shown in Table 2 were taken as the input variables, and the debris flows and non-debris flows were taken as the output variables. For all 258 samples, 70% (n = 180) were selected randomly for training data, which were used to create the DFSM models. The remaining 30% (n = 78) were used as testing data, which were applied to validate the DFSM models. Based on two types of watershed units (HWUs and CWUs) and four models (LR, MLP, CART and BN), eight DFSMs of Yongji county were completed.

![img-10.jpeg](img-10.jpeg)

**B** Debris flows ratio of susceptibility grades

![img-11.jpeg](img-11.jpeg)

**C** Debris flow density of susceptibility grades

![img-12.jpeg](img-12.jpeg)

**FIGURE 9** The classification of DFSMs and debris flow density: (**A**) area ratio; (**B**) debris flows ratio; (**C**) debris flow density.

### 5.4 Eight DFSMs

In this paper, IBM SPSS software was chosen to build the debris flow susceptibility predictive models. The model outputs are the debris flow susceptibility indices of all watershed units in the study area. Debris flow susceptibility indices are the probability of debris flow occurrence which varies from 0 to 1 (Xiong et al., 2020). Based on the ArcGIS software, the debris flow susceptibility indices were

![img-13.jpeg](img-13.jpeg)

FIGURE 10 The AUC, ACC, and Kappa coefficient values of the eight models for the training and testing data.

converted into raster format to produce the debris flow susceptibility map. Quantile classification was applied to divide the final maps into five classes, namely, very low susceptibility (VL), low susceptibility (L), moderate susceptibility (M), high susceptibility (H), and very high susceptibility (VH). (Martha et al., 2013; Hussin et al., 2016; Steger et al., 2017).

As shown in Figure 8, the susceptibility distributions of the eight models have common characteristics. Very high and high susceptibility areas are mainly distributed in the southeast, moderate susceptibility areas are mainly distributed in the middle, and very low and low susceptibility areas are mainly distributed in northwestern of Yongji county, which is consistent with previous research results (Qin et al., 2019). The landform in the southeast of the study area is mainly middle mountains, and the land use is mainly forest and farmland. The watershed units distributed in the southeast have large relative height differences and slopes, which leads to frequent debris flow disasters. The precipitation decreases from southeast to northwest, which is consistent with the susceptibility distribution. The lithology in southeastern Yongji county is hard massive rock, mainly granite. Weathered granite is a component of debris flows, which increases the density and destructive power of debris flows (Figures 2B–E).

For the eight DFSMs, the area ratios of the five susceptibility classes (very high, high, moderate, low, and very low) were 12.85–19.96, 13.82–21.51, 14.87–23.79, 17.70–28.33, and 16.56%–36.70%, respectively (Figure 9A); The debris flow ratios of the five susceptibility classes were 62.79–76.74, 12.40–24.81, 6.98–14.73, 0.78%–3.10% and 0%–0.78%, respectively (Figure 9B). As shown in Figure 9C, the debris flow density was calculated to evaluate the performance of the DFSMs, that is, the ratio of debris flow percentage to area percentage on each susceptible class (Pham et al., 2016). The maximum values of the debris flow density of the eight models appear in the very high susceptibility class, varying from 3.15 to 5.61. The minimum values all appear in the very low susceptibility class, varying from 0.00 to 0.04. The debris flow density increases gradually from a very low class to a very high class, which provides a good visualization of the spatial predictions of debris flows (Pham et al., 2017; Asadi et al., 2022).

### 5.5 Validation and comparison of the models

Model validation is a vital step in disaster susceptibility mapping (Wang et al., 2022). By considering the three commonly used performance metrics of ACC, AUC and Kappa, eight models were verified. The AUC, ACC and Kappa coefficient values of the eight models on the training and testing data are shown in Figure 10.

In the training phase, when HWUs were used as the mapping unit, the ACC stated that HWUs_CART model had the highest value (0.990), followed by HWUs_MLP (0.932), HWUs_BN (0.919) and HWUs_LR (0.881). It showed that the HWUs_CART model can correctly classify the debris flow and non-debris flow locations as debris flow and non-debris flow situations respectively. The highest and lowest Kappa values were 0.980 and 0.762, respectively for the HWUs_CART and HWUs_LR. Meanwhile, HWUs_MLP (0.864) and HWUs_BN (0.838) was ranked in other positions. In terms of AUC, results indicated that the HWUs_CART model with a value of 0.991 had higher performance than the HWUs_MLP (0.982), HWUs_BN (0.970) and HWUs_LR (0.966). When CWUs was used as the mapping unit, the ACC, Kappa and AUC values of the CWUs_CART model were 0.980, 0.960 and 0.985, which showed that the performance of the CWUs_CART model was the highest,

![img-14.jpeg](img-14.jpeg)

FIGURE 11 Watershed unit classification results comparison: (A) The boundaries of HWUs are relatively consistent with reality in mountainous areas; (B) The boundaries of CWUs do not match well with the actual situation in mountainous areas; (C) Small and narrow units in flat areas of HWUs; and (D) The division of CWUs in flat areas is relatively satisfactory.

TABLE 5 AUC values of testing data in different studies.


followed by the CWUs_MLP (0.893, 0.787, 0.967), CWUs_BN (0.899, 0.778, and 0.946) and CWUs_LR (0.858, 0.716, and 0.946) (Figure 10). Although the results showed the excellent performance for all the four algorithms, the CART had the highest ability in debris flow classification and susceptibility mapping in the study area. In terms of watershed unit, ACC, Kappa and AUC values decreased when HWUs was replaced by CWUs, indicating that HWUs were more suitable for DFSM in the study area than CWUs.

Right side of Figure 10 showed the prediction capabilities of the eight models based on testing dataset. These results are very important for evaluating the applicability and robustness of the models. When HWUs were used as the mapping unit, the highest value of ACC was 0.834 for the HWUs_CART model, next for the HWUs_MLP (0.826), HWUs_BN (0.808) and HWUs_LR (0.802) models. The Kappa for the HWUs_CART model was 0.668 as the highest value, whereas this value was 0.652, 0.617, and 0.604 for HWUs_MLP, HWUs_BN, and HWUs_LR, respectively. The highest and lowest AUC values were 0.942 and 0.882, respectively for the HWUs_CART and HWUs_LR. Meanwhile, HWUs_MLP (0.902) and HWUs_BN (0.892) was ranked in other positions. Correspondingly, ACC, Kappa and AUC from CWUs were shown in Figure 9, which indicated a similar result with HWUs. CART model resulted in the highest ACC, Kappa and AUC values of 0.832, 0.663, and 0.909, which manifested it is the best model for the study area. At the same time, the HWU-based models had better performance than the CWU models for DFSM in the study area.

## One-way ANOVA test

The results of the models are tested by one-way ANOVA in SPSS. For HWUs, there are significant differences between CART and each of the three methods (LR, MLP, and BN). There are no significant differences among LR, MLP, and BN. For CWUs, there are no significant differences between MLP and each of the two methods (LR and BN). There are significant differences between the other methods.

## Discussion

### Watershed unit classification processes and results comparison

As shown in Figure 3, the extraction processes of HWUs are more complex than those of CWUs, because HWUs require six steps while CWUs require five steps. Model builder in ArcGIS is a workflow that connects a series of geoprocessing tools (Qin et al. 2019). It takes the output of one tool as the input of the other tool. Model builder can greatly reduce operation time and improve work efficiency. We had built two workflows for the processes of extracting HWUs and CWUs in the model builder. Experiments on two types of watershed units showed that HWUs extraction required 17 s, while CWUs extraction required only 3 s. In addition, for the division of HWUs, the influence of DEM resolution and flow threshold needs to be considered, while for CWUs, only DEM resolution needs to be considered. In summary, it takes more time and effort to extract HWUs than CWUs.

There are also significant differences between the two types of watershed units in the classification results. As shown in Figure 4, HWUs are mostly strip-shaped and widely different in size, while CWUs are nearly square and relatively uniform in size. The watershed unit boundaries extracted by the hydrological analysis method in areas with obvious topographic changes are relatively consistent with reality (Figure 11A). However, there are many small and narrow units in flat areas, because there is no clear flow direction in flat areas for hydrological analysis (Massimiliano et al. 2016) (Figure 11C). For the curvature method, the division of watershed units in flat areas is relatively satisfactory, and there is no parallel line problem similar to the hydrological analysis method (Figure 11D). However, in areas with obvious topographic changes, the boundaries of watershed units do not match well with the actual situation (Figure 11B).

### Comparison of DFSMs based on different evaluation models

Four models, LR, MLP, CART and BN, were used to complete the DFSMs of Yongji county in this study. Figure 10 shows the predictive ability of the eight models. When HWUs were used as mapping units, CART had the highest evaluation criteria with AUC, ACC and Kappa values of 0.991, 0.990, and 0.980 respectively, followed by MLP (0.982, 0.932, 0.864), BN (0.970, 0.919, 0.838) and LR (0.966, 0.881, 0.762) in the training stage. For the testing stage, the CART had the highest prediction accuracy with AUC, ACC and Kappa values of 0.942, 0.834 and 0.668 respectively, followed by MLP (0.902, 0.826, 0.652), BN (0.892, 0.808, 0.617) and LR (0.882, 0.802, 0.604). When CWUs were used as mapping units, the evaluation results showed the same trend as HWUs. The comparisons of the four evaluation models show that the CART had the best predictive ability over the other three models. The current research was in agreement with previous research results. Wang et al. (2015) analyzed landslide susceptibility based on five mathematical models (artificial neural network, frequency ratio, CART, LR and weights of evidence methods) and three sampling strategies. They indicated the results obtained from CART show steady prediction power with an AUC value larger than 0.7. Felicísimo et al. (2012) indicated that the CART is one of the most predictive models with the AUC value of 0.77. Using random forest (RF), boosted regression tree (BRT), classification and regression tree (CART), and general linear (GLM), Youssef et al. (2015) found the success rate for CART was 0.816 and for the prediction rate the CART was the highest with a value of 0.862. CART represents information in an intuitive and easy visual way, and is widely used in many fields (Bevilacqua et al. 2003; Malinowska 2014; Kim et al. 2015; Youssef et al. 2015; Yang et al. 2016).

Several studies have been conducted in similar areas. Selecting the frequency ratio (FR) model as the statistical method, Qin et al. (2019) explored the accuracy and practicability of HWUs and grid cell units (GCUs) in evaluating debris flow susceptibility in Yongji county. Qiao et al. (2021) built debris flow susceptibility models via the analytical hierarchy process (AHP) method and generated maps of Yongji county. The AUC values of the testing data in different studies are shown in Table 5. When the HWUs were chosen as mapping units, the AUC values of the DFSMs based on AHP, FR, LR, BN, MLP and CART were 0.812, 0.879, 0.882, 0.892, 0.902, and 0.942 respectively. The main difference among these DFSMs is the selection of different evaluation models, which indicates that machine learning models can improve the prediction accuracy of DFSMs. These results are consistent with previous studies, indicating that machine learning models are more suitable for DFSM than heuristic and general statistical models (Huang et al. 2020; Sun et al. 2021).

### Comparison of DFSMs based on different watershed units

The selection of mapping units is one of the key issues for the rationality and correctness of disaster susceptibility mapping (Van Den Eeckhaut et al. 2009; Chen et al. 2019; Sun et al. 2020). The impact of different mapping units on disaster susceptibility mapping is greater than that of statistical methods (Zezere et al. 2017). Although many studies have tried to compare different evaluation models for disaster susceptibility mapping (Achour et al. 2018; Liang et al. 2020; Xiong et al. 2020; Dash et al. 2022; Qiu et al. 2022), very few studies have considered different mapping units. Qin et al. (Qin et al. 2019) explored the effect of grid cell unit and HWUs on the susceptibility mapping of debris flow, they found HWUs can reflect the geological and geomorphic environmental conditions of a debris flow accurately and perfectly. Li et al. (Li et al. 2021) discussed the influence of four different HWUs on debris flow susceptibility assessment results.

The results show that the appropriate watershed division scheme can obtain more reasonable results. In this study, HWUs and CWUs were selected to map debris flow susceptibility. When the CART was selected as the machine learning model, the HWUs generated high AUC, ACC, and Kappa for training data (0.991, 0.990 and 0.980) compared to the CWUs (0.985, 0.980, and 0.960). For testing data, the AUC, ACC, and Kappa of HWUs were 0.942, 0.834, and 0.668, respectively. The AUC, ACC, and Kappa of CWUs were 0.909, 0.832, and 0.663, respectively. The results suggest that the HWU model has a higher debris flow prediction performance than the CWU model. The same trend can be observed in the LR, MLP, and BN models. Therefore, the HWU-based model is superior to the CWU-based model in debris flow susceptibility assessment due to higher training and testing accuracy.

As described in “6.1 Watershed unit classification processes and results comparison,” compared with CWUs, HWUs agree well with the actual watershed units in mountainous areas, but small and narrow units appear in plain areas. Since the frequency of debris flows in mountainous areas is much higher than that in plain areas, the division of watershed units in mountainous areas is more important than that in plain areas. Therefore, the HWU model is more practical than the CWU model. CWUs can also represent the distribution of watersheds and can be used as an alternative scheme.

Although this paper discussed the application of two types of watershed units in DFSM and obtained positive results, there are some limitations: 1) the number of debris flows is small, and 2) only HWUs with a threshold of 1,000 and CWUs with a resolution of 300 are selected for comparison. In future research, we will constantly update the debris flow database to improve the data quality. Moreover, it is necessary to explore the similarities and differences of multiscale watershed units in DFSM.

## 7 Conclusion

This paper mainly explored the influence of using different watershed units (HWUs and CWUs) in debris flow susceptibility assessment models. LR, MLP, CART, and BN were chosen as evaluation models to avoid the model uncertainty caused by different models. Yongji county, with 129 recorded debris flows and 13 related influencing factors, was used as the study area and eight DFSMs were produced.

The DFSM results showed that CART has the best predictive ability over the other three models through the analysis of AUC, ACC and Kappa. By using Model Builder in ArcGIS, 1,092 HWUs and 1,211 CWUs were extracted. Compared with HWUs, the extraction process of CWUs is simpler. For the results of watershed unit division, HWUs have more advantages in areas with undulating terrain, but they are not satisfactory in areas with flat terrain. CWUs perform well in flat areas but do not match the actual watershed boundaries in areas with undulating terrain. Since debris flows mostly occur in mountainous areas, the DFSM based on HWUs is more accurate and practical than that based on CWUs. In addition, the AUC, ACC and Kappa showed that the HWU-based model has remarkably higher debris flow prediction performance than CWUs. This result means that the HWUs are more effective in debris flow susceptibility assessment of the study area. The CWU-based model can also reflect the spatial distribution probability of debris flows in the study area overall and can be used as an alternative model. Further studies should propose a more appropriate watershed unit for DFSM.

## Data availability statement

The original contributions presented in the study are included in the article/supplementary material, further inquiries can be directed to the corresponding author.

## Author contributions

JL: Conceptualization, methodology, formal analysis, investigation, writing, original draft, writing-review and editing. SUQ: Methodology, validation, resources, data curation, writing -original draft, visualization, project administration, funding acquisition. JC: Validation, investigation, supervision, project administration. SGQ: Investigation, supervision. JGY: Software, data curation. XZ: Conceptualization, supervision. RC: Software, supervision. JHY: Investigation, data curation.

## Funding

This work was funded by the National Natural Science Foundation of China under Grants 41977221 and 41972267, and in part by the Jilin Provincial Science and Technology Department (Grant No. 20190303103SF).

## Acknowledgments

The authors are also thankful to the reviewers for their valuable feedback on the manuscript.

## Conflict of interest

JL, XZ, RC, and JHY were employed by China Water Resources Bei Fang Investigation, Design & Research Co. LTD.

The remaining authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.
