University of Groningen

# Bayesian network based procedure for regional drought monitoring 

Ali, Zulfiqar; Hussain, Ijaz; Grzegorczyk, Marco Andreas; Ni, Guangheng; Faisal, Muhammad; Qamar, Sadia; Shoukry, Alaa Mohamd; Wahab Sharkawy, Mohammed Abdel; Gani, Showkat; Al-Deek, Fares Fawzi<br>Published in:<br>Journal of Environmental Management

DOI:
10.1016/j.jenvman.2020.111296

IMPORTANT NOTE: You are advised to consult the publisher's version (publisher's PDF) if you wish to cite from it. Please check the document version below.

Document Version
Publisher's PDF, also known as Version of record

Publication date:
2020

Link to publication in University of Groningen/UMCG research database

Citation for published version (APA):
Ali, Z., Hussain, I., Grzegorczyk, M. A., Ni, G., Faisal, M., Qamar, S., Shoukry, A. M., Wahab Sharkawy, M. A., Gani, S., \& Al-Deek, F. F. (2020). Bayesian network based procedure for regional drought monitoring: The Seasonally Combinative Regional Drought Indicator. Journal of Environmental Management, 276, Article 111296. https://doi.org/10.1016/j.jenvman.2020.111296

## Copyright

Other than for strictly personal use, it is not permitted to download or to forward/distribute the text or part of it without the consent of the author(s) and/or copyright holder(s), unless the work is under an open content license (like Creative Commons).

The publication may also be distributed here under the terms of Article 25fa of the Dutch Copyright Act, indicated by the "Taverne" license. More information can be found on the University of Groningen website: https://www.rug.nl/library/open-access/self-archiving-pure/taverneamendment.

## Take-down policy

If you believe that this document breaches copyright please contact us providing details, and we will remove access to the work immediately and investigate your claim.

Downloaded from the University of Groningen/UMCG research database (Pure): http://www.rug.nl/research/portal. For technical reasons the number of authors shown on this cover page is limited to 10 maximum.

# Bayesian network based procedure for regional drought monitoring: The Seasonally Combinative Regional Drought Indicator 

Zulfiqar Ali ${ }^{\mathrm{a}, \mathrm{b}, *}$, Ijaz Hussain ${ }^{\mathrm{b}}$, Marco Andreas Grzegorczyk ${ }^{\mathrm{c}}$, Guangheng $\mathrm{Ni}^{1}$, Muhammad Faisal ${ }^{\mathrm{d}, \mathrm{e}}$, Sadia Qamar ${ }^{\mathrm{f}}$, Alaa Mohamd Shoukry ${ }^{\mathrm{g}, \mathrm{h}}$, Mohammed Abdel Wahab Sharkawy ${ }^{\mathrm{g}}$, Showkat Gani ${ }^{1}$, Fares Fawzi Al-Deek ${ }^{\mathrm{g}}$<br>* School of Statistics, Minhaj University, Lahore, 54000, Pakistan<br>${ }^{\text {b }}$ Department of Statistics, Quaid-i-Azam University, Islamabad, Pakistan<br>${ }^{a}$ Johann Bernoulli Institute, Groningen University, 9747AG, Groningen, Netherlands<br>${ }^{b}$ Faculty of Health Studies, University of Bradford, BD7 1DP, Bradford, UK<br>${ }^{c}$ Bradford Institute for Health Research, Bradford Teaching Hospitals NHS Foundation Trust, Bradford, UK<br>${ }^{f}$ University of Sargodha, Sargodha, Pakistan<br>${ }^{g}$ Arriyadh Community College, King Saud University Riyadh, Saudi Arabia<br>${ }^{\text {h }}$ KSA Workers University, Nsar, Egypt<br>${ }^{1}$ State Key Laboratory of Hydro-Science and Engineering and Dept. of Hydraulic Engineering, Tsinghua University, Beijing, 100084, China<br>${ }^{2}$ College of Business Administration, King Saud University Muzahimiyah, Saudi Arabia

## A R T I C L E I N F O

Keywords:
Drought
Standardized precipitation temperature index (SPTI)
Bayesian networks
Geospatial variation

## A B S T R A C T

Drought is a complex natural hazard. It occurs due to a prolonged period of deficient in rainfall amount in a certain region. Unlike other natural hazards, drought hazard has a recurrent occurrence. Therefore, comprehensive drought monitoring is essential for regional climate control and water management authorities. In this paper, we have proposed a new drought indicator: the Seasonally Combinative Regional Drought Indicator (SCRDI). The SCRDI integrates Bayesian networking theory with Standardized Precipitation Temperature Index (SPTI) at varying gauge stations in various month/seasons. Application of SCRDI is based on five gauging stations of Northern Area of Pakistan. We have found that the proposed indicator accounts the effect of climate variation within a specified territory, accurately characterizes drought by capturing seasonal dependencies in geospatial variation scenario, and reduces the large/complex data for future drought monitoring. In summary, the proposed indicator can be used for comprehensive characterization and assessment of drought at a certain region.

## 1. Introduction

In many regions across the world, the risk of drought hazard has been increasing due to climate change and global warming (Turral et al., 2011; Marquina, 2010). Unlike other natural hazards, is a complex and recurrently occurring hazard (Tsakiris, 2017). Therefore, more comprehensive and rigorous procedures are required for drought monitoring, forecasting, and spatial analysis (Ali et al., 2019b, 2018). In the past three decades, numerous methods and tools have been developed for drought monitoring for various climatological regions. Some of them are Palmer Drought Severity Index (PDSI) (Wayne, 1965),

Keetch-Byram drought index (KBDI) (Keetch and Byram, 1968), Surface Water Supply Index (SWSI) (Dezman et al., 1983), Crop-specific Drought Index (CSDI) (Meyer et al., 1993), and Reconnaissance Drought Index (RDI) (Tsakiris et al., 2007). Svoboda and Fuchs (2016) discussed each of these indices and their data requirement. However, among all drought indices, Standardized Drought Indices (SDI) is one of the most commonly used procedures (Erhardt and Czado, 2018). Example of SDI indices includes Standardized Precipitation Index (SPI) (McKee et al., 1993), Standardized Precipitation Evapotranspiration Index (SPEI) (Vicente-Serrano et al., 2010) and Standardized Precipitation Temperature Index (SPTI) (Ali et al., 2017). These standardized methods

[^0]
[^0]:    * Corresponding author. Department of Statistics, Quaid-i-Azam University, Islamabad, Pakistan.

    E-mail addresses: zulfiqarali@stat.qau.edu.pk (Z. Ali), ijaz@qau.edu.pk (I. Hussain), m.a.grzegorczyk@rug.nl (M.A. Grzegorczyk), ghni@tsinghua.edu.cn (G. Ni), m.faisal1@bradford.ac.uk (M. Faisal), diyaqau@gmail.com (S. Qamar), aabdulhamid@ksu.edu.sa (A.M. Shoukry), mosharkawy@ksu.edu.sa (M.A. Wahab Sharkawy), sgani@ksu.edu.sa (S. Gani), faldeek@ksu.edu.sa (F.F. Al-Deek).
    https://doi.org/10.1016/j.jenvman.2020.111296
    Received 31 October 2019; Received in revised form 18 August 2020; Accepted 20 August 2020
    Available online 6 September 2020
    0301-4797/© 2020 Elsevier Ltd. All rights reserved.

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** Locations of selected meteorological stations in north region of Pakistan.

provide sufficient evidence for the establishment of effective drought mitigation policies and early warning strategies.

Among other climatic and meteorological variables, the distribution of rainfall and temperature are the main factors of drought hazard (Vicente-Serrano et al., 2010; Easterling et al., 2007; Hu and Willson, 2000). These two climatic variables have great influence and substantial importance in continuous drought monitoring. Most SDI procedures use long time series data of precipitation and temperature (Guttman, 1999; Cancelliere and Salas, 2004; Hiscock, 2009). In this regard, regional drought monitoring involves accurate estimation of SDI indices based on regionally representative time series. However, climate cycle and spatio-temporal features of meteorological stations within a particular region are the main barriers in acquiring regionally representative time series data.

From geostatistical and data mining point of view, accurate estimation and continuous monitoring of drought at the regional level requires a dense meteorological network. In past few decades, several algorithms and methods for the optimal selection of meteorological stations have been the subject of great interest (Arsenault and Brissette, 2014; Lark, 2016; Hong et al., 2016). These algorithms and methods reduce the size of the network and provide more accurate and regionally representative estimates of meteorological variables. However, the implications in numerous meteorological stations (regardless of an optimal number of meteorological stations) at specified region need high cost, time and resources. Especially in developing countries, the high cost of equipment installations and complex sampling design may force to adopt the compromised solution. Further, the adoption of these techniques raises several questions on the accuracy in measurements. For example, the rainfall is a spatial climatic variable that varies in both spatial and temporal dimensions. Its short distance variability characteristics and being a spatial variable suggest the complex structure of the meteorological network (Scarsoglio et al., 2013; Einfalt et al., 1990).

On the other hand, several studies have suggested advanced statistical and geostatistical methods for monitoring drought and other meteorological variables in various climatological regions (Bayat et al., 2015; Chen et al., 2017; Drogue et al., 2002; Miniscloux et al., 2001). However, these methods are based on temporal data records at a single station, that is, it only covers a single realization at a continuous spatial domain. This deprived the study and findings of the spatial prevalence effect of climate nature and climate change. Further, the increases in uncertainty in the estimation may lead to bad impact on climate change policies and reliability of forecasting environmental characteristics. In addition, regional patterns of long-term rainfall and temperature at various seasons play an important role in the continuous drought monitoring. Therefore, drought management must define and monitor drought conditions using more representatively regional data and procedures. Consequently, a regionally representative meteorological observatory or location is required for accurate and precise quantification of drought.

In summary, various factors are involved to diminish the efficiency and accuracy of drought monitoring methods such as seasonal and geospatial climate variation, an inappropriate network of gauging locations, errors in the estimation phase of drought indices, lack of resource, and the creation of complex data at a particular geographical region. In these perspectives, advanced statistical procedures are helpful to find important and regionally representative gauge stations under complex meteorological network setting. This research aims to employ Bayesian network-based probabilistic model for regional drought monitoring. Bayesian network method has been widely used to establish a probabilistic relationship between variables. It is a powerful technique, which produces multivariate Joint Probability Distribution (JPD). These probabilities describe the dependency structure between variables (Pearl, 2014). Some recent applications of Bayesian network theory in various fields are available in Lee et al. (2019), Bertone et al. (2018), Moglia et al. (2018) and Liu et al. (2015).

In this paper, we proposed a new drought indicator - the Seasonally Combinative Regional Drought Indicator (SCRDI). SCRDI integrates Bayesian networking theory and SDI tools coupled with different seasons at varying gauged stations in a specified region. The organization of this article is as follows. Section 2 provides descriptions of material and methods. The proposed regional drought indicator: The Seasonally Combinative Regional Drought index (SCRDI) is presented in section 3. Section 4 and 5 elaborate results and discussion, respectively. Finally, we concluded our findings in section 6.

Table 1 Summary statistics of precipitation and temperature (Time Range, 1971-2017).


## 2. Material and methods

### 2.1. Data and study area

The application of this research is based on five meteorological stations named as Astor ( $35.3570^{\circ} \mathrm{N}, 74.8624^{\circ} \mathrm{E}$ ), Skardu ( $35.3247^{\circ} \mathrm{N}$, $75.5510^{\circ} \mathrm{E}$ ), Gupis ( $36.2274^{\circ} \mathrm{N}, 73.4421^{\circ} \mathrm{E}$ ), Gilgit ( $35.8819^{\circ} \mathrm{N}$, $74.4643^{\circ} \mathrm{E}$ ), and Chilas ( $35.4222^{\circ} \mathrm{N}, 74.0946^{\circ} \mathrm{E}$ ). These stations are located in the Northern part of Pakistan (see Fig. 1). Due to a significant change in climate and global warming scenario, the agricultural and industrial sectors of the whole geographical parts of the country are badly suffering from severe drought hazards. In addition, the prevalence of death is reported in many parts of the country. Especially in Tharparker (district of Sindh Province), numerous peoples including children died due to severe condition of drinking water shortage (Siddiqui and Safi, 2019). So, the continuity of drought for several future years will lead in lowering of per capita income that will result in poor health and nutrition especially for pregnant women and newly born children. In this scenario, prediction, continuous monitoring and accurate reporting of drought will strengthen drought mitigation policies. In this context, the selected regions consisting of five meteorological stations have a significant contribution to the whole part of the country and its climatology (Salma et al., 2012).

Table 1 shows the climatology of these stations in different sessions. One can observe that most of the stations have cold climate nearly all month.

### 2.2. The standardized drought indices (SDI)

During the past three decades, numerous methods developed for drought monitoring (Svoboda and Fuchs, 2016). The SDI method is one of the most commonly used drought monitoring method (Erhardt and Czado, 2018). From a data mining point of view, SDI mainly relies on univariate or multivariate data modeling. For univariate data modeling, several drought indices developed by various authors. For example, McKee et al. (1993) introduced the SPI drought index for the characterization of drought at various time scales. In SPI, monthly time series data of precipitation is standardized by an appropriate probability function. Vicente-Serrano et al. (2010) developed a standardized index-the SPEI. On the same line of SPI, SPEI is obtained by standardizing of water balance equation (see Eq. (1)).

$$ D E F_{i}=P_{i}-P E T_{i} $$

In the above equation, $\mathrm{P}_{\mathrm{i}}$ is the monthly total amount of precipitation, $\mathrm{PET}_{\mathrm{i}}$ is the estimated amount of Potential Evapotranspiration (PET). On the same line of McKee et al. (1993) and Vicente-Serrano et al. (2010), Ali et al. (2017) proposed another multi-scaler drought index called SPTI index.

For multivariate data modeling, there are several procedures and frameworks of drought indices. For example, Hao and AghaKouchak (2013) proposed Multivariate Standardized Drought Index (MSDI) by using copula function. Posteriorly, they modified MSDI by including the concept of non-parametric modeling (Hao and AghaKouchak, 2014). To resolve multiscaling issues in univariate SDI method, Bazrafshan et al. (2014) introduced a framework based on the principal component analysis. Consequently, they suggested a new multivariate drought index-the Multivariate Standardized Precipitation Index (MSPI).

In recent years, several drought monitoring studies and applications are based on SDI procedure. Some of them are Vicente-Serrano et al. (2018), Tigkas et al. (2018), Faiz et al. (2018) and Mathbout et al. (2018), Shen et al. (2017), Zarch et al. (2015), Golian et al. (2015).

This research is mainly based on the SPTI drought index. Contrary to SPI, SPTI is based one more than one meteorological variable. In addition, SPTI is an alternate of SPEI drought index particularly design for low-temperature regions (Ali et al., 2017). The indicator used in SPTI (see equation (9)) accounts the direct role of temperature in the selection of appropriate probability distribution. In our case, the selected study area has a cold climate and low temperature in most of the month (see Table 1). Therefore, the selection SPTI index is rationally valid. A brief estimation procedure of SPTI index is as follows:

The first step is to compute De Martonne Aridity Index (DAI) (De Martonne, 1926). ( using monthly total precipitation and average

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** An example of Bayesian network with five nodes (Grzegorczyk, 2010).

monthly temperature for each selected station separately.

$$DAI_i = \frac{P_i}{10 + T_i} \tag{2}$$

In the above equation, *P*<sup>*i*</sup> is the monthly total precipitation and, *T*<sup>*i*</sup> is the mean monthly temperature. In further steps, *DAI*<sub>*i*</sub> series are used to obtain standardized values. In the computational procedure of SPTI, we have followed the standard guidelines of standardized drought index provided by Stagge et al. (2015). As our main focus is to give procedure of regional drought monitoring, therefore we include the only type of drought which is a meteorological index. To do this, we restrict our research on SPTI-1-time scale drought index. To estimate SPTI values, thirty-two distributions were used to assess their appropriation on the time series data of De Martonne index defined in equation (2) using *propagate* (Spiess, 2014) R package, separately for each station.

In this article, the specific computational results of SPTI index includes the selection of probability distribution for all the five stations. However, we have skipped the stepwise procedure of standardization of SPTI. One is referred to as the Ali et al. (2019a) and Ali et al. (2018) for a detailed overview and computational step of SPTI index.

After the selection of appropriate probability distributions, their numerical CDFs for all the station is standardized by the transformation function. See standardization procedure in Ali et al. (2017).

### 2.3. Bayesian networks and posterior probabilities

Bayesian networks are a class of probabilistic graphical models for leaning network topologies (Koller and Friedman, 2009; Pearl, 2014). Bayesian networks have applications in numerous multidisciplinary fields of research. For example, Bayesian networks are used for decision making (Watthayu and Peng, 2004; Kochenderfer, 2015), for prediction (Zhu et al., 2016; Borsuk et al., 2004; Mendes and Mosley, 2008), for anomaly detection (Wong et al., 2003; Sebyala et al., 2002), and reasoning (Neapolitan, 2012; Darwiche, 2009). In a nutshell, Bayesian networks can be used to learn the (un-)conditional dependencies among large numbers of interacting variables. In addition, these models quantify the dependencies between interacting variables in terms of so-called marginal edge posterior probabilities. The underlying concept is the Bayesian model averaging. Consequently, Bayesian network models are a flexible and promising statistical tool for reverse-engineering unknown network structures from data (Uusitalo, 2007). In this paper, we will apply static Bayesian network models to continuous data. We assume that the measurements are continuous and are independent (non-temporal) of domain variables. Here we only provide a brief overview of the Bayesian network methodology, but the readers are referred to a book chapter for a more detailed explanation on Bayesian networks models (Grzegorczyk, 2010).

Bayesian networks use directed acyclic graphs (DAGs) to describe the (un-)conditional independencies among a set of variables (*X*<sub>1</sub>, *X*<sub>2</sub>, ..., *X*<sub>*n*</sub>). More formally, let *X* denote a set of *n* random variables. The variables are then the nodes of the DAG and the directed edges encode the dependency structure among them. From the structure of the DAG (i.e. from its directed edges), it can be seen how the joint probability distribution over the *n* variables can be factorized into a product of so-called local conditional probability distributions. For instance, Fig. 2 shows a DAG for *n* = 5 variables (*A*, ..., *E*). In Fig. 2 nodes *B* and *C* are child nodes of node *A*, and vice-versa node *A* is called a parent node of *B* and *C*. Similarly, *D* is a child node of *B* and *C*, whereas, node *E* has parent node *D*.

In the factorization of the joint probability distribution of the *n* variables, each variable just depends on its parent nodes:

$$P_{G}(x_1, x_2, \dots, x_n) = \prod_{i} P(x_i | Pa(X_i, G)) \tag{3}$$

where *Pa*(*X*<sub>*i*</sub>, *G*) denotes the set of parent nodes of node *X*<sub>*i*</sub> in the directed acyclic graph *G*.

#### 2.3.1. Learning the network structure

Conceptually, the edges of the graph *G* imply that the (un-)conditional dependencies among the domain variables are such that the factorization in Equation (2) is valid. The goal of Bayesian network analysis is to infer the underlying dependency structure (e.g. to infer the graph that best describes the dependencies among the observed variables).

Let *D* denote the observed data, i.e. a set of *m* independent *n*-dimensional vectors, whose entries are in one-to-one correspondence with the *n* variables. Within a Bayesian modeling framework, the posterior probabilities of a directed acyclic graph *G* is defined as:

$$P(G|D) = \frac{P(D|G)}{P(D)} P(G) \tag{4}$$

where *P(D|G)* is the marginal likelihood, *P(G)* is the graph prior distribution, and *P(D)* is a normalization constant. The marginal likelihood is the probability of the data *D* given the graph *G*, i.e. it is the likelihood marginalized over all possible parameter instantiations that the graph *G* could have. Under certain modeling assumptions, the marginal likelihood can be computed analytically so that a closed-form solution is available. The graph prior distribution can be used to bring in preknowledge about the dependencies. If there is no genuine preknowledge available a uniform distribution over all graphs can be used.

When the data *D* is sparse, it is often not useful to search for the one single 'best' graph having the highest posterior probability. For sparse data, there might be various graphs that explain the data (approximately) equally well, so that they have (approximately) the same posterior probability in Equation (4). A more robust approach is then to average across all possible graphs, to identify whether there are some 'features' (e.g. particular edges) that all the 'good' graphs share. The marginal posterior probability of a feature is the sum of the posterior probabilities of all those graphs *G* that possess this feature. Mathematically this can be expressed as follows:

Table 2 BIC values of candidate distributions for all stations.


$P(f / D)=\sum_{G} P(G \mid D) f(G)$ where the sum is over all possible directed acyclic graphs $G$, the posterior probability $P(G \mid D)$ has been defined in Equation (4), and $f$ is an indicator function for a specific feature (e.g. a particular edge). That is $f(G)$ takes the value 1 if $G$ possesses the feature, and $f(G)=0$ otherwise. The higher the marginal feature posterior probability, the more certain we are about the presence of this feature. E.g. if a feature has probability 0.9 , then this means that the posterior probabilities of the graphs that support the feature sum up to 0.9 , whereas only 0.1 of the probability mass goes to graphs that do not support the feature.

### 2.3.2. Model averaging and structure MCMC

As the number of valid directed acyclic graphs (DAGs) grows superexponentially in the number of variables $n$, the edge feature probabilities in Equation (5) cannot be computed analytically. The sum is over too many graphs, and thus computationally not feasible. Henceforth, in practice, the marginal feature posterior distributions are approximated. To this end, a graph sample from the posterior distribution in Equation (4) is generated. This can be done by Markov Chain Monte Carlo (MCMC) simulations. Loosely speaking, the key idea is to design a Markov chain in the space of all valid DAGs, whose stationary distribution is the desired posterior distribution from Equation (5). Simulating this Markov chain yields a trajectory of DAGs. After an initial burn-in period, the stationary distribution ( $=$ posterior distribution) is reached, so that the frequency, with which each DAG appears in the trajectory, converges to the posterior probability of this DAG.

Various MCMC sampling algorithms have been developed for Bayesian networks (Madigan et al., 1995; Friedman and Koller, 2000; Grzegorczyk and Husmeier, 2008). By running one of those MCMC sampling algorithms, a sample of DAGs $\left(G_{1}, G_{2}, G_{3}, \ldots, G_{T}\right)$ from the posterior distribution in Equation (4) is generated. For our study, we employ improved Metropolis-Hastings sampler (Grzegorczyk and Husmeier, 2008). For the technical details, the reader is referred to (Grzegorczyk and Husmeier, 2008).

### 2.3.3. Marginal posterior probabilities of edges

After having generated a sample of DAGs $\left(G_{1}, G_{2}, G_{3}, \ldots, G_{T}\right)$ from the posterior distribution, the next step is to approximate the marginal posterior probability of all features of interest. The most interesting features are the individual edges. For each possible edge, we would like to approximate the marginal edge posterior probability (often referred to as edge score). Compare Equation (5) with the indicator function $f$ indicating the presence (or absence) of a particular edge. Given the DAG sample $\left(G_{1}, G_{2}, G_{3}, \ldots, G_{T}\right)$ from Equation (4) a consistent estimator for the expression in Equation (4) is: $\tilde{P}(f \mid D)=\sum_{i=1}^{T} f\left(G_{i}\right)$ where $f(G)=1$ if $G$ possesses the edge, and $f(G)=0$ otherwise. Computing the marginal edge posterior probabilities for all possible edges defines a ranking of all edges. To obtain a concrete network prediction, one can impose a threshold and extract all edges whose marginal posterior probability is higher than this threshold, whereas edges with probabilities lower or equal to the threshold are assumed to be absent.

To test for convergence (i.e. to test whether the stationary distribution has been reached), we always run three independent MCMC simulations on each data set. A widely applied convergence diagnostic is to plot the edge scores from two independent runs against each other. If all points in those scatter plots are located near the diagonal, it can be concluded that the chains have produced (approximately) the same results, and thus sufficiently converged. In our study, we always observed sufficient convergence, so that we eventually averaged the edge scores of the three independent simulations. This procedure is briefly described in subsection 3.3.

## 3. The proposed regional drought indicator: The Seasonally Combinative Regional Drought index (SCRDI)

The main objective of this research is to develop a new drought indicator by incorporating most representative information at the regional level. To achieve this, this section is mainly based on the selection of SDI index and Bayesian network procedures. Details of these two methodologies have already been described in section 2. Before the execution of the proposed procedure, we have defined the following three main point which has substantial importance for accurate inferences related to regional settings.

1. Defining Region: This step determines the selection of region for drought monitoring. In this step, a particular region is identified for regional drought monitoring. However, this research suggests those regions which are the most influential on the larger part of the country/province and have rich climate characteristics. Accordingly, appropriate selection of region will strengthen accurate and efficient drought mitigation policies at the province or country level.
2. Defining Meteorological station: After the selection of regions, appropriate selection of meteorological stations/monitoring stations is suggested. As we know that long climatic data has a significant role in model building and statistical inferences. Thus, the meteorological stations which have rich drought monitoring history are suggested.
3. Seasonality Indication: Within a particular region, climatology among meteorological stations varied in most parts of the world. For example, a real and temporal variability in precipitation and temperature at various locations in a specified region is a renowned topic (Ma et al., 2018; Asfaw et al., 2018; Ongoma and Chen, 2017; Mondal et al., 2015; Gehne et al., 2016). From previous studies, we

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** At Chilas station subfigure (a) represents frequency and fitted Probability distributions on DAI; time series data, (b) represents Q-Q plot of the selected 3P Weibull distribution, and (c) represents the time series data of SPTI index.

observed that some regions have a long duration of the cold season (Yang et al., 2013), while some have hot climate throughout the year (Wu et al., 2018; Uvo et al., 1998). In this scenario, it is difficult to define a generalized seasonality index. However, to ease in quantification, this study recommends each month as a season. Although various regions have various levels of variability within a specific month, it is a simple, comprehensive, and most practiced way. Several climatological and environmental studies are based on a monthly-defined seasonal index (Ayugi et al., 2016; Yang et al., 2013; Zhang et al., 2012, 2006).

After defining the above three points, the stepwise execution of the proposed framework consists of four phases. A detailed description of each phase is described in the subsequent subsections.

### 3.1. Phase 1: the choice of drought indices and their estimation

This phase consists of the selection of drought indicators. In literature, many authors have provided various drought indicators for the standardized procedure of drought index. Some of them are available in Svoboda and Fuchs (2016). In section 2, we have described a summary of various SDI indicators and their applications in various regions. Parallel to SDI procedures, recent developments also concentrate on the estimation procedure these drought indices such as parametric and non-parametric based estimation Soláková et al. (2014). Therefore, this phase is very important for accurate regional drought monitoring and its analysis.

The major concern of this phase is to select the climatic parameters and the time scale for the estimation of multi-scalar drought indices. Depending on the nature of climatic, soil type, and tropical status, various drought indices required various climatic parameters such as temperature, precipitation, solar radiation, and humidity, etc. Therefore, optimized selection of drought indices and their estimation procedure can significantly contribute to inaccurate and reliable drought monitoring. In particular, this step requires a deep knowledge of the following issues:

Table 3 Marginal posterior probability matrices of three simulation runs in January.


Table 4 Marginal posterior probability matrices of three simulation runs in February.

Runs | Matrix of Stations |  |  |  |  |

- The identification of the nature of gauging station and the accessibility of the time series data on the climatic parameters.
- The appropriate selection of multi-scalar drought indicator (i.e. SPI, SPEI, SPTI) that can be accomplished with the available data.
- Type of drought with their corresponding time scale. In this step, the time scale of multi-scalar drought indices is selected. For example, short time scales are recommended for meteorological Guttman (1998), whereas longer time scales are specified for the monitoring of agricultural and hydrological drought Ma'rufah et al. (2017).



### 3.2. Phase 2. segregation of time series data by seasonality indexing

This phase describes the temporal formation of SDI data. In the previous section, we have described the seasonal index. Accordingly, this phase suggests separate analysis on the time series data set of SDI of a specific region according to the seasonality index. For the sake of generality, this research assumes and defines seasonal index at a monthly level. Let $R_{1}, R_{2}, \ldots, R_{12}$ be the time series data indexed by month, where each month is considered as a season. In the consequent step, each indexed time series for all the stations would be considered as an independent time series data for further practice.

### 3.3. Phase 3. configuring BN model

This phase describes and configures Bayesian network models on the seasonally separated time series data of SDI data of multiple meteorological stations.

Consider, the network of meteorological stations $\left(Y_{1}, Y_{2}, Y_{3}, \ldots\right.$, $\left.Y_{n}: Y\right)$ at the specified region. Here, the purpose to obtain a probabilistic model representing the whole uncertainty about the drought in the network at a specific season/month/time. In section 3, we have described how Bayesian networks is a useful and most powerful probabilistic technique for extracting probabilistic information about interacting variables. The main source of probabilistic information is the marginal posterior probabilities of edge nodes/variable. The marginal posterior probabilities describe dependency/independency structure among variable in a quantitative way. In this context, the marginal posterior probabilities of individual seasonal time series data of SDI index at various meteorological stations are suggested to specify regional dependency features of the most dominant meteorological station. Mathematically, let $Y_{1}, Y_{2}, Y_{3}, \ldots, Y_{n}$, be the seasonal (monthly separated) time series vector data of SDI index at meteorological stations, where a sub-index refers to the station number. And each meteorological station $\left(Y_{1}, Y_{2}, Y_{3}, \ldots, Y_{n}\right)$ is considered as a node/variable. Here, $Y_{i}$ can take a value or state $y_{i}$, where the value or state is the realization of a variable/node/meteorological stations. Mathematically, $P\left(y_{1}, y_{2}, \ldots, y_{n}\right)=P\left(Y_{1}=y_{1}, \ldots, Y_{n}=y_{n}\right)$

The structure of the above equation describes the probability of meteorological stations $Y_{1}$ in $y_{1}$, meteorological stations $Y_{2}$ in $y_{2}$ and so on. Accordingly, Equation (6) is suggested to obtain marginal posterior probabilities of edges.

The consequent subsection consists of the uses of these marginal posterior probabilities in our proposed drought method.

### 3.4. Phase 4. the choice of meteorological stations

In this phase, a meteorological station at a particular season or month is suggested to identify from probability structure of Bayesian networks results.

Suppose that, a particular region/domain $\Theta$ has a well-known set of meteorological stations $\underline{Y}$. In a single run of Bayesian networks, consider that the marginal posterior distribution of $\Theta$ at a particular month $R_{i} \in \underline{R}$ have the following mathematical form.

### 3.5. $Y_{1} Y_{2} \ldots Y_{n}$

$\left.\begin{array}{llll}Y_{1} & p_{11} & p_{12} & \cdots & p_{1 n} \ Y_{2} & p_{21} & p_{22} & \cdots & p_{2 n} \ \vdots & \vdots & \vdots & \ddots & \vdots \ Y_{n} & p_{n 1} & p_{n 2} & \cdots & p_{n n}\end{array}\right]$ where the element in the above matrix is mapped from the results of equation (6). In the above matrix, the lower side of the off-diagonal element describes dependence probability between meteorological stations in $\Theta$ at a particular month $R_{i} \in \underline{R}$. Whereas upper diagonal describes independency features accordingly.

By careful implementation of Bayesian networks, we suggest choosing one meteorological station on which most of the station have maximum Average Marginal Posterior Probability Matrix (AMPP). From the above matrix, the mathematical form of AMPP is represented as follows: $A M P P=\max \left(\hat{p}_{1}+\hat{p}_{2}, \ldots, \hat{p}_{n}\right)$

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** Scatter plots of the marginal posterior probability estimates observed in January and February data.

where, $$P_1 = \frac{\sum_{i=1}^{n} p_i}{n}$$ is the average of individual column entities of the marginal posterior distribution matrix. Then, the choice of MS from Y in all the defined seasonal indicators R is made for those that have maximum associated probability AMPP as defined in 8. To maintain accuracy in result, we suggest taking an average of three independent runs of the BN model. That is, there should be at least three MCMC simulations.

For more comprehension, the step-wise summary of the proposed procedure is as follows.

1. The first step is to find JPD by configuring Bayesian network model on the time series data of SDI. In each month, the BN model will produce joint probability matrix (see matrix presented in section 3.4).

2. The second step consists of the two more replication of step 1 and 2.

3. The third step computes Average Dependence Probability (ADP) for all the stations. This step is due to three runs of the Bayesian network model. The formula of average dependence probability is defined in equation (9). Consequently, we will concentrate on the grand average. Mathematically,

$$P_i = \frac{\sum_{t=1}^{3} \left( p_{i1} + p_{i2} + p_{i3} \right)}{3} \tag{9}$$

4. In the fourth step, monthly time series data of that station which have the highest ADP probabilities are selected for further data mining.

After the estimation of the standardized drought indices for each station, the data is divided into 12 sets. In each set, we have time series variables associating from five selected stations. As the time series range

![img-4.jpeg](img-4.jpeg)

![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

(c) Graphical representation of marginal posterior probability estimates of third simulation run

(d) Scatter plots of the marginal posterior probability estimates

**Fig. 5.** Observed quality of three structure MCMC simulation runs in March, (a) Graphical representation of marginal posterior probability estimates of first simulation run, (b) Graphical representation of marginal posterior probability estimates of second simulation run, (c) Graphical representation of marginal posterior probability estimates of third simulation run, (d) Scatter plots of the marginal posterior probability estimates.

From 1971 to 2017, therefore each variable contains 47 observations. For all the 12 data sets, three independent structure MCMC simulations runs are made. In structure MCMC simulation setting, a total of 200,000 iterations with 100 step save and burn-in are configured subjectively (Grzegorczyk, 2010).

The evaluation and accuracy of these probabilities are assessed by performing more than three structure MCMC simulations. These simulations are either have different seeded runs or independent and identical. This practice is followed by Grzegorczyk and Husmeier (2008). To do this, scatter plots of the marginal posterior probability of edges consisting of three pairwise simulations runs are presented in result and discussion section.

### 4. Results

#### 4.1. Estimation of SPTI index

This section describes and presents some numerical and graphical results related to the estimation of SPTI-1 index for all stations. Table 2 shows the list of probability distributions corresponding with the

Table 5


Bayesian Information Criterion (BIC) values. We observed that three parameters (3P) Weibull distribution have the lowest BIC values (-480.82, -379.153, 197.265) for Astor, Chilas and Gilgit respectively. In addition, Fig. 3a shows how 3P probability distribution is well fitted for computing SPTI indicator. Further, Fig. 3b demonstrates the scatter plot of theoretical and empirical density. Accordingly, 4P Weibull with BIC values -427.46 and Johnson Sb distribution with BIC values -871.55 are found to be well-fitted probability distributions for Gupis and Skardu respectively (see Table 2).

After the standardization step, temporal behaviors of SPTI index are observed (see Fig. 3c). From the temporal data, significant discrepancies have been observed. From a very short distanced meteorological stations, such discrepancy has serious data mining problems. That is, it reflects many challenges for future drought forecasting, drought monitoring and data dissemination at a regional scale.

### 4.2. Implications of Bayesian networks

Tables 3 and 4 comprises on the marginal posterior probabilities of three simulation runs for January and February data sets, respectively. In term of identical convergence of MCMC results, the quality of simulation runs is presented in Fig. 4. These plots are used to evaluate the convergence of marginal posterior probabilities in each simulation. The pairwise comparison shows that the MCMC simulation runs have achieved a sufficient degree of convergence in both of these months. In addition, there are no significant deviations within the marginal posterior probability matrices. Hence, the results of MCMC runs are consistent with each other.

To check the most representative station, the marginal posterior probabilities of each station is averaged according to the proposed setup. We observe that Chilas have maximum values of Average Marginal Posterior Probability Matrix (AMPP). This means that irrespective to other stations, Chilas is the most representative station in January and February. By the rationale of our proposed design, we have concluded that the temporal data of Chilas station is the most representative in January and February under regional settings.

Similar to January and February data sets, structure MCMC practice is made of all other months separately. Fig. 5 exhibits the results of structure MCMC simulation runs. We have presented the estimate marginal posterior probabilities from three independent simulation runs for Jan and Feb (See table). However, to save the volume of pages and ease in understanding, we skipped the presentation of numerical values of marginal posterior probabilities for all the month. The graphical results are archived in the author's gallery.

In the next step, maximum AMPP is identified using equation (8). Table 5 presents the average marginal posterior probability for all the month. We have found that the Chilas is the most representative meteorological station in January, February, June, and July. While Skardu is the most representative in all other months.

## 5. Discussion

In this article, we first computed the SPTI index under the parametric approach of standardization. In the computation procedure, we have followed Stagge et al. (2015) procedure of varying probability distributions. After the estimation of SPTI index for all the stations, time series data at each station is segregated according to monthly defined season. We have described the segregation process of time series data in methodology. For each data set, Bayesian network models are employed separately under structure MCMC. Our experimental results consist of three independent simulation runs. Where, each simulation run is made on monthly based segregated time series data of SPTI index for all the station combatively. For validation of Bayesian networks, the scatter plots of the posterior probabilities for all the simulation runs are investigated. In addition, marginal posterior probability distributions for all the month are shown in the form of tables and graphs.

After discovering dependency structure using maximum AMPP, the monthly time series values of respective representative stations are desegregated and merged into a single series. We have named this single series of SPTI index as the SCRDI. Fig. 6 shows the temporal plot of SCRDI index. This single time series data of SCRDI have characteristics to describe and characterize drought situation at the regional level. Hence to report regional statistics such as forecasting, model fitting, and dissemination of meteorological event (i.e drought or wet), the proposed index has a strong rationale of its candidacy.

![img-7.jpeg](img-7.jpeg)

Fig. 6. Temporal representation of regional drought indices: the SCRDI.

The main advantages of the proposed methods are 1) the proposed method provides a sound procedure for composite assessment of regional drought (Chen et al., 2020), 2) it provides a solid way to combined information of drought coming from various stations.

The limitations of the proposed approach is the choice of MCMC simulation setting and BNs. In literature, there are several BNs and simulation setting. However, the optimal selection of the MCMC simulation setting and BNs is required for accurate and comparable results.

## 6. Conclusions

This paper provides a systematic way to combine SDI time series data of various meteorological stations located in a certain region under Bayesian network theory. Here, a new combinative procedure of defining a regional drought indicator: the SCRDI have been proposed. Practical implementation for establishing SCRDI time series is made for five meteorological stations located in the Northern Area of Pakistan. In this research, we have used seasonally segregated time series data of SPTI-1 index in Bayesian network model under structure MCMC setup. To preserve more accuracy, our results and inferences are based on three independent structure MCMC based simulation runs. Under the rationale of exploring dependency/independency structure among variables by Bayesian network theory, the most representative and influential stations are identified using maximum AMPP of three simulations. Among five meteorological stations, two stations, namely Chilas and Skardu are found to be the most dominant stations. However, the behavior of dominance of these stations varies with months. After these results, the original time series data of SPTI index is desegregated accordingly to the proposed rationale of SCRDI. Here, we conclude that the SCRDI is a regionally representative indicator for characterizing meteorological drought at a regional scale. In addition, being a single regional representative, SCRDI is a good choice for efficient model searching and fitness. That is, SCRDI leads lessen in the calculation, save time and resources in the forecasting of future drought at a regional scale.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgement

The authors extend their appreciation to the Deanship of Scientific Research at King Saud University for funding this work through research group no RG-1437-027.

## Appendix A. Supplementary data

Supplementary data related to this article can be found at https:// doi.org/10.1016/j.jenvman.2020.111296.
Astor $\left(35.3570^{\circ} \mathrm{N}, 74.8624^{\circ} \mathrm{E}\right)$, Skardu $\left(35.3247^{\circ} \mathrm{N}, 75.5510^{\circ} \mathrm{E}\right)$, Gupis $\left(36.2274^{\circ} \mathrm{N}, 73.4421^{\circ} \mathrm{E}\right)$, Gilgit $\left(35.8819^{\circ} \mathrm{N}, 74.4643^{\circ} \mathrm{E}\right)$, and Chilas $\left(35.4222^{\circ} \mathrm{N}, 74.0946^{\circ} \mathrm{E}\right)$.
