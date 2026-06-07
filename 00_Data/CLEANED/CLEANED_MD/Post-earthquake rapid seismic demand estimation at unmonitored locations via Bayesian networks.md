# Post-earthquake rapid seismic demand estimation at unmonitored locations via Bayesian networks 

Pooria Mesbahi ${ }^{1} \cdot$ Enrique García-Macías ${ }^{2} \cdot$ Marco Breccolotti ${ }^{1} \cdot$ Filippo Ubertini ${ }^{1}$ (D)<br>Received: 30 March 2024 / Accepted: 11 July 2024 / Published online: 24 July 2024<br>(c) The Author(s) 2024


#### Abstract

Post-earthquake safety assessment of buildings and infrastructure poses significant challenges, often relying on time-consuming visual inspections. To expedite this process, safety criteria based on a demand-capacity model are utilized. However, rapid assessment frameworks require accurate estimations of intensity measures (IMs) to estimate seismic demand and assess structural health. Unfortunately, post-earthquake IM values are typically only available at monitored locations equipped with sensors or monitoring systems, limiting broader assessments. Simple spatial interpolation methods, while possible, struggle to consider crucial physical factors such as earthquake magnitude, epicentral distance, and soil type, leading to substantial estimation errors, especially in areas with insufficient or non-uniform seismic station coverage. To address these issues, a novel framework, BN-GMPE, combining a Bayesian network (BN) and a ground motion prediction equation (GMPE), is proposed. BN-GMPE enables inference and prediction under uncertainty, incorporating physical parameters in seismic wave propagation. A further novelty introduced in this work regards separating the near and far seismic fields in the updating process to attain a clearer understanding of uncertainty and more accurate IM estimation. In the proposed approach, a GMPE is employed for the estimation, and the bias and standard deviation of the prediction error are updated after any new information is entered into the network. The proposed method is benchmarked against a classic Kriging interpolator technique, considering some recent earthquake shocks in Italy. The proposed BN framework can naturally extend for estimating the probability of failure of various structures in a targeted region, which represents the ultimate aim of this research.


Keywords Bayesian networks $\cdot$ Ground motion prediction equation $\cdot$ Kriging surrogate model $\cdot$ Machine learning $\cdot$ Markov Chain Monte Carlo $\cdot$ Seismic demand model

## 1 Introduction

Seismic demand estimation plays an instrumental role in assessing the vulnerability and resilience of critical civil engineering structures such as dams, bridges, pipelines, or power distribution systems under the action of earthquakes. The process of seismic demand estimation involves predicting the severity of ground motions in structures by considering

[^0]
[^0]:    Extended author information available on the last page of the article

various factors, including earthquake magnitude, source-to-site distance, and the site characteristics and soil conditions. Such an estimation is crucial for arranging retrofitting interventions, as well as for organizing evacuation and emergency response strategies to ensure the uninterrupted provision of vital services during and after seismic events.

A straightforward approach for estimating IMs at unobserved locations based on observed values at specific points involves the utilization of the Kriging method. Zimmaro et al. (2018) conducted an analysis on the spatial distribution of ground motions resulting from three mainshock events through the utilization of Kriging analysis on within-event IM residuals for the 2016 central Italy earthquake. Gidaris et al. (2015) developed a framework based on a Kriging surrogate model to provide an approximate relationship between the structural response and ground motion parameters that were considered uncertain. Even though it is possible to include physics-based trend models in Kriging (see eg. Worden et al. 2018), the classical Kriging model lacks the ability to extrapolate, with the subsequent risk of yielding considerable estimation errors if there is not a uniform sensor coverage in the area of interest.

In contrast, physics-based seismic demand estimation models have experienced, notable progress over the years, integrating the latest scientific research, advanced computational tools, and increasing digitalization of strong motion networks worldwide. The use of attenuation relationships or ground motion prediction equations (GMPEs) is one of the most popular methods to estimate seismic demand.

According to the definition provided by Sabetta and Pugliese (1987), "GMPEs are typically expressed as mathematical functions relating a strong motion parameter to parameters characterizing the earthquake, propagation medium, and local site geology". A plethora of GMPEs has been developed in recent decades as evidenced by the numerous review works published in the literature (Douglas 2003, 2008). Among the latest review articles, it is worth noting the one by Douglas (2021), who presented a classification of GMPEs according to the following criteria: (i) the methodology utilized to develop GMPEs; (ii) the geographical area of application; and (iii) the input variables considered in the definition of the GMPEs.

Regression analysis exploiting the correlations between the IMs of interest and different factors such as magnitude and source-to-site distance represents a classical approach to developing GMPEs. Other methods proposed in the literature include hybrid stochastic empirical methods (Atkinson 2001; Pezeshk et al. 2021), simulation-based methods (often stochastic methods) (Faccioli 1983; Sokolov et al. 2021), and non-parametric ground-motion models (often including machine learning and artificial intelligence techniques) (Schnabel and Bolton Seed 1973; Khosravikia and Clayton 2021). Interested readers can find a complete list of non-regression methods in J. Douglas's report (Douglas 2021).

With regard to geographical applicability, some of these GMPEs are applicable worldwide (Campbell 1981; Cauzzi and Faccioli 2008), while others have been developed for a specific region (Ahmad et al. 2008; Megawati et al. 2005; Bajaj and Anbazhagan 2019; Hwang and Huo 1997; Özbey et al. 2004). Lastly, in terms of the input variables taken into account within the GMPE, classical factors simply include the seismic magnitude and epicentral/fault distance (Denham and Small 1971; Ambraseys 1990), while some of the latest models incorporate other variables such as the site geology or the fault mechanism (Bindi et al. 2011; Zhao et al. 2015; Huang et al. 2021; Iervolino 2023; Chioccarelli and Iervolino 2010; Esposito and Iervolino 2012).

It is important to remark that most GMPEs exploit past ground motion data to predict future ground motions. In the process of extrapolating from historical data to make

predictions about the future, it is important to recognize the presence of two sources of uncertainty. The first source arises from the imperfect fit between the model and past data, while the second source stems from the uncertainty regarding the extent to which future events will resemble those observed in the past. Classically, such uncertainties are considered in GMPEs through an error term or a certain empirical tolerance in the predictions (typically a zero-mean Gaussian term).

As a more robust alternative, Bayesian approaches in this field can offer an effective means for addressing the uncertainty factors related to the input parameters of GMPEs. Additionally, Bayesian schemes offer a natural framework for incorporating new seismic observations and updating the prior knowledge about probabilistic variables.

Over the past years, various approaches have been proposed to develop Bayesian techniques for recalibrating GMPEs and conduct uncertainty quantification based on newly recorded seismic data. Ordaz et al. (1994) demonstrated the merits of employing Bayesian linear regression compared to standard least-squares regression. Subsequently, those authors exemplified the practical application of that approach by deriving attenuation laws for the Fourier acceleration spectrum at a specific station located in Mexico City.

Wang and Takada (2009) proposed the integration of a correction term into a GMPE within a Bayesian inference framework. This correction term is characterized as a linear function, incorporating source magnitude and distance, to account for the scarcity of available data at a specific location in Japan. Those researchers opted to employ both noninformative and informative gamma-normal prior densities to predict the posterior of IMs at the site.

Kowsari et al. (2019) recalibrated seven selected ground motion models (GMMs) to a dataset from the South Iceland Seismic Zone using Bayesian regression and Markov Chain Monte Carlo simulations to mitigate biases between the dataset and the predictions of the GMMs.

Bertin et al. (2020) presented a Bayesian model averaging (BMA) approach, using nine attenuation relationships issued from several databases. It was shown that BMA provides an improved predictive performance.

In the past decades, increasing attention has been BNs as an efficient approach for conducting inference in complex interconnected systems. In general, a BN is a probabilistic graphical model that represents the relationships between variables using a directed acyclic graph (DAG). It combines probability theory with graph theory to provide a powerful tool for modeling and reasoning under uncertainty.

Bayraktarli et al. (2005) introduced a comprehensive BN framework designed specifically for managing risks associated with earthquakes. Their study focused on the seismic demand measure, specifically spectral displacement. This measure was determined by considering various factors, including earthquake magnitude, source-to-site distance (represented by the Earthquake Distance node), soil type, and the fundamental period of the structure. To facilitate the analysis, those researchers employed a software application capable of generating synthetic accelerograms that align with a response spectrum derived from the GMPE model developed by Boore et al. (1997).

Kuehn et al. (2009) employed structural learning techniques to ascertain the optimal BN topology for effectively capturing the dependencies between ground motion intensity and the characteristics of seismic sources and sites. Yue et al. (2010) employed a seismic demand model based on an attenuation relation for peak horizontal acceleration proposed by Joyner and Boore (1981) within a framework for seismic vulnerability assessment based on BNs. Bensi (2010) presented a decision support framework based on BNs to effectively model the seismic demands imposed on an infrastructure system.

In light of the previous literature review, it is evident that relying solely on GMPEs is not an accurate approach for promptly estimating IMs and seismic demand following a seismic event. This is due to their inherent high errors and uncertainties in assessing the IM values. Furthermore, as highlighted in the article by Paolucci et al. (2022), it has been observed that several GMPEs exhibit even greater uncertainty in near-field predictions compared to those in the far-field. Conversely, the utilization of Kriging interpolation may not consistently provide a reliable solution, as it overlooks the incorporation of physical parameters governing the propagation of earthquake waves from the source to the site, such as soil type and focal mechanism. Moreover, as demonstrated in this study, when the distribution of observation points around the epicenter is non-uniform, it might lead to substantial estimation errors.

To address these limitations, this paper introduces a Bayesian approach based on the Metropolis Hasting algorithm to update the extrinsic uncertainty of chosen GMPEs using the recorded accelerograms within the area of study, utilizing a separation approach in the updating process for near field and far field allowing for a more accurate estimation of the desired IM at any geographical location. Additionally, a framework is developed to compare the IM estimation accuracy of the proposed method with the accuracy of the Kriging method, exclusively for each considered earthquake. The proposed approach can be easily extended into a BN framework capable of estimating the failure probabilities for a set of structures in specific regions. Specifically, each structure may be represented as an additional node in the network, linked with capacity models (e.g., fragility curves). In this way, data from monitoring systems further enable Bayesian updates to the estimated failure probabilities. Nonetheless, such an expansion remains on the periphery of the current study, and it will be the focus of future research.

The remainder of this paper is organized as follows. In Sect. 2, a detailed explanation of the proposed framework and its fundamental concepts is presented. Section 3 presents the numerical results and discussion of five application case studies, along with a discussion of the main findings. Finally, conclusions are presented in Sect. 4.

# 2 Proposed framework 

The rationale behind this framework can be summarized as follows: It is assumed that a seismic event has taken place, needing a post-event estimate of the seismic demand incurred at specific unmonitored geographical locations. To this aim, the data from a seismic monitoring system recording ground accelerations at scattered stations in the area of interest are retrieved.

These data, which include accelerograms and other information related to the earthquake and site condition, are used to update the attenuation model (or GMPE) and estimate the IMs at target locations. However, considering that each of the demand and capacity models has various intricacies, this work solely focuses on the development of a BN for seismic demand.

This network is intended to be utilized in the future as a part of a demand-capacity model for assessing seismic vulnerability in a network of similar structures. The conceptual framework of this proposed demand-capacity model is depicted in Fig. 1. In this figure, the seismic vulnerability of each asset (e.g. bridge) in the network is updated after a seismic event. In this framework demand models can be correlated due to the similarities in key

![img-0.jpeg](img-0.jpeg)

Fig. 1 Conceptual framework of the proposed demand-capacity model
factors in seismic wave propagation and also capacity models of different assets might be correlated due to the common features in geometry, material, scale, and structural system.

# 2.1 Attenuation models selection 

As mentioned in the introduction, particular attenuation relationships have been devised for specific regions, whereas others have been developed for application at a global scale. This division commonly depends on the dataset employed for calibrating the regression parameters. In this paper, a relatively contemporary regional GMPE proposed by Bindi et al. (2014) for Europe and the Middle East is employed. For comparison purposes, an old but well-established GMPE developed by Ambraseys et al. (1996) (for Europe and adjacent regions) has also been investigated. An overview of these selected attenuation models is presented in Table 1.

### 2.1.1 First GMPE: Bindi et al. (2014)

The ground-motion model developed by Bindi et al. (2014) reads:

$$
\log _{10} Y=e_{1}+F_{D}\left(R, M_{w}\right)+F_{M}\left(M_{w}\right)+F_{S}+F_{\text {sof }}+E_{B}
$$

where $Y$ is the IM (In this paper, we estimate as the IM $Y$ the peak ground acceleration $\left(P G A, \mathrm{~cm} / \mathrm{s}^{2}\right)$, and the spectral acceleration $\left(S A, \mathrm{~cm} / \mathrm{s}^{2}\right)$ for 0.05 damping ratio), $e_{1}$ is a constant, and the variable $M_{w}$ denotes the moment magnitude. The term $R$ stands for the Joyner-Boore distance (measured in kilometers) or the epicentral distance (in cases where the fault geometry is not ascertainable, a scenario that usually arises when the magnitude $M_{w}$ is less than 5.5). $F_{D}, F_{M}, F_{S}$, and $F_{\text {sof }}$ represent functions for distance, magnitude, site amplification, and style of faulting (fault mechanism), respectively. $E_{B}$ is the error (probabilistic) term defined according to a normal distribution (mean value is zero and within-event sigma is selected according to Table 1). The distance function $F_{D}$ is given by:

$$
F_{D}\left(R, M_{w}\right)=\left[c_{1}+c_{2}\left(M_{w}-M_{\text {ref }}\right)\right] \log _{10}\left(\sqrt{R^{2}+h^{2}} / R_{\text {ref }}\right)-c_{3}\left(\sqrt{R^{2}+h^{2}}-R_{\text {ref }}\right)
$$

while the magnitude function is as follows:

Table 1 Overview of selected GMPEs for this study


${ }^{1} V_{s}$ denotes the ground shear wave velocity

$$
F_{M}(M)= \begin{cases}b_{1}\left(M_{w}-M_{h}\right)+b_{2}\left(M_{w}-M_{h}\right)^{2} & \text { if } \quad M_{w} \leq M_{h} \\ b_{3}\left(M_{w}-M_{h}\right) & \text { otherwise }\end{cases}
$$

where $c_{1}, c_{2}, c_{3}, b_{1}, b_{2}, b_{3}$ are coefficients determined using a regression method, $h$ is a constant equal to $6.14717, M_{h}$ is the hinge magnitude at which the constrained magnitude scaling in the two-segment regression changes from the quadratic form to the linear form, and $R_{\text {ref }}$ stands for the reference distance, which marks the point where the decline in near-source predictions commences. $M_{\text {ref }}$ signifies the reference magnitude, typically positioned around the 50th percentile of the cumulative frequency distribution of recordings concerning magnitude. The following variables have been fixed following the recommendations by Boore and Atkinson (2008): $R_{\text {ref }}=1 \mathrm{~km} ; M_{\text {ref }}=5.5 ; M_{h}=6.75$.

The site amplification term $F_{S}$ in Eq. (1) is given by:

$$
F_{S}=s_{i} C_{i}, \quad i=1, . ., 4
$$

where $s_{i}$ represents the coefficient requiring determination via regression analysis, and $C_{i}$ signifies the dummy variables utilized to represent the distinct EC8 site classes (given in Table 1).

The focal mechanism term $F_{\text {sof }}$ in Eq. (1) can be written as:

$$
F_{\text {sof }}=f_{j} E_{j}, \quad j=1, \ldots, 4
$$

where $f_{j}$ are the coefficients to be determined, and $E_{j}$ are dummy variables used to denote the different fault classes of normal, reverse, strike-slip, and unknown. More details about the formal definition of the GMPE and obtained values for coefficients are available in Bindi et al. (Bindi et al. 2014) and J. Douglas (Douglas 2021).

# 2.1.2 Second GMPE: Ambraseys et al. (1996) 

The ground-motion model developed by Ambraseys et al. (1996) is as follows:

$$
\begin{gathered}
\log _{10} Y=C_{1}^{\prime}+C_{2} M_{s}+C_{4} \log _{10} r+C_{A} S_{A}+C_{S} S_{S}+E_{A} \\
r=\sqrt{d^{2}+h_{0}^{2}}
\end{gathered}
$$

where $C_{1}^{\prime}, C_{2}, C_{4}, C_{A}$, and $C_{S}$ are the coefficients determined using a two-state regression method initially developed by Joyner and Boore (1981). $S_{A}$ is equal to 1 if the site is classified as a stiff soil ( $360<V_{s} \leq 750 \mathrm{~m} / \mathrm{s}$ ), and 0 otherwise, also $S_{S}$ takes the value of 1 for soft ( $180<V_{s} \leq 360 \mathrm{~m} / \mathrm{s}$ ) and very soft ( $V_{s} \leq 180 \mathrm{~m} / \mathrm{s}$ ) soil, and 0 otherwise. $M_{s}$ denotes the surface wave magnitude, while $d$ represents the shortest distance from the station to the fault rupture's surface projection, measured in kilometers.

In Eq. (7), the term $h_{0}$ considers the variability that the source of the peak motion might not necessarily be the closest point on the surface projection of the fault or from the epicenter. Additionally, it does not explicitly account for the impact of depth on acceleration (Ambraseys et al. 1996). The constant $h_{0}$ is determined in conjunction with $C_{1}^{\prime}, C_{2}$, and $C_{4}$. Finally, $E_{A}$ is the normally distributed error with zero mean and a standard deviation according to Table 1.

### 2.2 Database selection and processing data

In the formulation of the attenuation model introduced by Bindi et al. (2014) (from now on referred to with the abbreviated name of B14), part of the RESORCE database (Akkar et al. 2014) was employed to calibrate the parameters. The RESORCE dataset, at the time of developing B14, encompassed a comprehensive collection of 5,882 seismic waveforms originating from 1814 distinct seismic events that occurred in the regions of Europe and the Middle East from the year 1967 to 2011 (Akkar et al. 2014).

The database employed in the attenuation model presented by Ambraseys et al. (Ambraseys et al. 1996). (from now on with the abbreviated name of A96) comprised 157 seismic events that occurred in Europe and its neighboring areas from 1969 to 1994 (Ambraseys et al. 1996).

In this article, for an unbiased comparison between the classic Kriging method and the proposed framework, earthquake events occurring after 2011 have been utilized (comprising 63 earthquakes with moment magnitude greater than 3.5 that occurred from the beginning of 2014 to the end of 2016).

Seismic events prior to 2011 were intentionally omitted from this comparison, as the primary objective of this study is to present a framework for estimating IMs for future earthquakes. Given that the proposed method is a combination of GMPE and BN, we

refrained from using records previously employed in GMPE calibration for the purpose of having a fair accuracy investigation.

The records employed in this study have been extracted from the Engineering StrongMotion (ESM) database (please see Data Availability section) developed by Lanzano et al. (2019) for pan-European regions, and certain details pertaining to them are presented in Fig. 2.

# 2.3 Underlying concepts 

Before delving into further details of the proposed method, it is necessary to provide a brief overview of the underlying concepts of the proposed approach. The foundation of this method is based on a statistical inference, which is defined as the process of concluding, such as estimating the value of an uncertain quantity, using data or observations (Bensi 2010). One of the schools of thought in this field is the Bayesian approach, as elaborated in Sect. 2.3.1.

### 2.3.1 Bayesian approach

Bayesian inference approaches have gained increased attention since the middle of the 20th century. The Bayesian perspective regards unknown parameters as random variables and focuses on computing their conditional probability based on observed data. In this way, the uncertainty in a predictive model can be represented as a probability distribution.

There are two main advantages of using a Bayesian approach. First, Bayesian statistical models can be updated as new observations become available. Second, they are generally more robust (compared to other approaches, such as the frequentist approach) in situations of data scarcity (Koop 2003).

In recent decades, there has been increased interest in developing various methods to solve the model parameter inference problem due to the growing use of sensors and advanced technologies for monitoring the health of structures. In Bayesian statistical inference, this inverse problem is addressed by considering model parameters as random variables and updating their probability distributions using observed data from the monitoring system. The Bayesian inference approach is based upon the well-known Bayes'
![img-1.jpeg](img-1.jpeg)

Fig. 2 Details of selected seismic events (between 2014 and 2016) from ESM database (Lanzano et al. 2019)

theorem, which is credited to Thomas Bayes, a mathematician and philosopher from the 18th century:

$$
P(\boldsymbol{\theta} \mid D)=P(D \mid \boldsymbol{\theta}) \cdot P(\boldsymbol{\theta}) / P(D)
$$

In this context, $\boldsymbol{\theta}$ represents a vector containing the model parameter(s) under consideration for estimation. $D$ refers to the measurements or observations on a model parameter(s). $P(\boldsymbol{\theta})$ is established as the prior distribution, which reflects an initial hypothesis or prior knowledge about the model parameter(s). $P(D \mid \boldsymbol{\theta})$ is denoted as the likelihood function, which reflects the degree of agreement between the measurement and the model. $P(\boldsymbol{\theta} \mid D)$ is characterized as the posterior distribution that presents the probability distribution of the parameter(s) of a model, updated with new information or evidence. $P(D)$ is defined as the evidence (or normalization constant of the posterior), which is the probability of observing the data $D$ regardless of the parameter(s) $\boldsymbol{\theta}$.

# 2.3.2 Addaptive MCMC for model updating 

While Bayesian inference offers numerous advantages, its application is often hindered by various challenges. One such obstacle involves acquiring evidence $P(D)$, which can prove computationally expensive or intractable for many complex models, necessitating the utilization of numerical Markov chain Monte Carlo (MCMC) methods to draw sample from the posterior distribution, without explicitly computing the model evidence. Consequently, Eq. (8) can be reformulated (in an un-normalized form) as follows:

$$
P(\boldsymbol{\theta} \mid D) \propto P(D \mid \boldsymbol{\theta}) \cdot P(\boldsymbol{\theta})
$$

To manage numerical stability we utilized Eq. (9) in a log-space form as follows:

$$
\log (P(\boldsymbol{\theta} \mid D)) \propto[\log (P(D \mid \boldsymbol{\theta}))+\log (P(\boldsymbol{\theta}))]
$$

considering the following form of the basic model equation, the main aim of model updating defined in this paper is improving prediction accuracy by updating the bias of the model, and reducing the uncertainty in the prediction by updating the error standard deviation (from now on with the abbreviated name of error SD), In this context, the prediction by an considered GMPE can be written as:

$$
y=f(\boldsymbol{x})+\epsilon, \quad \epsilon \sim N\left(\theta, \sigma^{2}\right)
$$

where $y$ represents observations (real values of $\log _{10}(\mathrm{IM})$ ), $f(\boldsymbol{x})$ is the model response, and vector $\boldsymbol{x}$ contains all known control variables in the model (characteristics of the earthquake e.g. soil type, epicentral distance, and fault mechanism). $\epsilon$ is a stochastic error term, indicating the variability of the GMPE prediction with respect to measured data. $\theta \in \mathbb{R}$ is the bias of the prediction (first target parameter for updating), and $\sigma$ is the error SD, presenting prediction uncertainty (second target parameter for updating). Error terms in GMPEs are usually assumed to follow independent Gaussian distributions (Schiappapietra and Douglas 2020), a property that holds true for the selected GMPEs (B14 and A96) in this paper. Therefore, independent Gaussian distributions are considered for the parameters of the error term in Eq. (11).

Assuming the discrepancy of the model estimates $f(\boldsymbol{x})$ and the observations $y$ at $N$ seismic stations are independent and identically distributed (i.i.d), Eq. (10) can be rewritten as follows:

$$
\log (P(\theta \mid D)) \propto\left\{\sum_{i=1}^{N}\left[\frac{-1}{2 \cdot \sigma^{2}}\left(y_{i}-f\left(\boldsymbol{x}_{i}\right)-\theta\right)^{2}\right]+\log (P(\theta))+\log \left(P\left(\sigma^{2}\right)\right)\right\}
$$

where $y_{i}$ is observation at $i$-th observation point, for $i=1, . ., N, f\left(\boldsymbol{x}_{i}\right)$ is the model response for $i$-th observation point and $\theta$ is the updateable model bias (for prediction of $\log _{10}(\mathrm{IM})$ ) for the considered seismic event.

In this paper, selected GMPEs are considered as the basic model equation, and the error SD and bias are chosen to be updated as the only unknown parameters. A crucial part of the modeling process is modeling the error SD (to reduce uncertainty prediction). The error variance $\sigma^{2}$ is frequently regarded as an independent parameter, occasionally even assumed to be constant. Nonetheless, it is often preferred to employ a prior distribution for it and then derive the corresponding posterior distribution (Laine et al. 2008).

Therefore, to simultaneously update the bias and error SD, the adaptive MCMC developed by Haario et al. (2006) is employed in this paper. For this purpose, on the one hand, a uniform probability distribution is considered for the prior of the model bias $(\theta)$, in which upper and lower bounds are experimentally determined to minimize prediction error (in this study from -2 to 2 ).

On the other hand, for sampling and updating the error $\mathrm{SD}(\sigma)$ at each step of the MCMC sampling in a computationally efficient manner, a conditional conjugacy property can be used. When assuming a Gaussian likelihood function and a Gamma prior for $\sigma^{-2}$, the posterior distribution of $\sigma^{-2}$ can be proved to also follow a Gamma distribution (Laine et al. 2008). The gamma distribution utilized for the inverse of error variance is defined as follows (Laine et al. 2008):

$$
p\left(\sigma^{-2}\right) \sim \Gamma\left(n_{0} / 2, n_{0} S_{0}^{2} / 2\right)
$$

where the prior parameters $n_{0}$ and $S_{0}^{2}$ represent the prior accuracy and the prior mean for $\sigma^{2}$, respectively (in this study $n_{0}=200$ and $S_{0}$ is selected from 1). Accordingly the conditional distribution $p\left(\sigma^{-2} \mid y, \theta\right)$ will also have a Gamma distribution as follows (Laine et al. 2008):

$$
p\left(\sigma^{-2} \mid y, \theta\right) \sim \Gamma\left(\left(n_{0}+n\right) / 2,\left(n_{0} S_{0}^{2}+S S(\theta)\right) / 2\right)
$$

where $S S(\theta)$ is the sum of squares function as follows:

$$
S S(\theta)=\sum_{i=1}^{N}\left(y_{i}-f\left(x_{i}\right)-\theta\right)^{2}
$$

Bayesian methods are widely used in various practical applications where efficiency and effectiveness are essential. These methods have also led to the development of a new class of acyclic graph models known as BNs, which simplify the Bayesian inference and prediction problems, especially in complex and large-scale systems.

# 2.3.3 Bayesian network 

BN is a graphical representation of a set of random variables and their dependencies. It permits probability and graph theories to be linked and is thus an intuitive means for dealing with uncertainties in complex systems (Friis-Hansen 2004).

A BN (for the first time introduced by Pearl (1985) consists of a directed acyclic graph (DAG) in which nodes represent variables: they might be latent variables, observable quantities, hypotheses, or unknown parameters. Moreover, each link (or edge) shows a direct conditional dependency (Murphy 1998) as depicted in Fig. 3.

In BN terminology, nodes can be categorized as parent (a node that directly influences one or more child nodes, affecting their conditional probabilities) or child nodes (a node that depends on one or more parent nodes, and its conditional probability is influenced by the values of its parent nodes) within the hierarchical structure of the graph. Nodes without parents are termed root nodes and are described by their probability density functions (PDFs).

BNs support two types of probabilistic inference: (i) predictive analysis, which relies on evidence (i.e., information that shows the node is in a particular state) about root nodes and involves sending information from the parent nodes to all other child nodes, and (ii) diagnostic analysis (Bayesian learning), where observations enter through child nodes to update the PDFs of the parent nodes. This feature of Bayesian learning is especially vital for postevent applications when available information from monitoring systems is uncertain and rapidly evolving (e.g., in structural health monitoring systems). These two procedures are depicted in Fig. 3.

# 2.4 Bayesian network for seismic demand estimation (BN-SDE) 

In 2010, Yue et al. developed a framework for seismic vulnerability assessment based on BNs. This framework incorporated the HAZUS model (a demand-capacity model) to calculate the probabilities of earthquake-induced damage in a network of bridges. This research idea was inspired by a research study conducted in 2009, in which Bensi et al. (2009) introduced a BN for seismic performance assessment of an infrastructure system. This BN model incorporates seismic intensities, typically identified as PGA, observed at various locations within a spatially dispersed infrastructure system post-earthquake.

These intensities are determined as a function of earthquake magnitude, site-to-source distance, and other factors related to the earthquake source and site characteristics, such as faulting mechanism type and site shear-wave velocity. The source-to-site distance is contingent upon the fault's characteristics and magnitude. Subsequently, infrastructure system component performance is simulated using fragility functions, which quantify the likelihood of surpassing specific damage thresholds based on the distribution of ground motion intensity at the site. The

Fig. 3 Two fundamental types of probabilistic inference in BN
(a) Diagnostic procedure
![img-2.jpeg](img-2.jpeg)
(b) Predictive procedure
![img-3.jpeg](img-3.jpeg)

overall system performance is then determined based on the performance of its components. Figure 3 in that paper presents the concept of the framework for seismic demand estimation.

The general BN procedure to estimate IMs at target points using an updated GMPE is shown in Fig. 4 (a simplified version of figure 3 in the paper by Bensi et al. (2009) in this figure, $M_{W}$ is moment magnitude, $F M$ represents the focal mechanism, $S$ is the soil type, $R$ refers to the epicentral distance, and $e_{T}$ is error term in GMPE. Information flow stages in this BN consist of the following two fundamental steps:

- Stage 1: Indicated by red arrows, in this stage, the IM at the observation points is directly computed from the recorded accelerograms, and this new evidence is entered into the network. Subsequently, using Eq. (12) the model error is updated. As discussed in Sect. 2.3.2, this procedure is known as Bayesian learning.
- Stage 2: In this stage, the updated GMPE is utilized to estimate the IMs at the target points, Indicated by green arrows. This step represents the predictive process in the proposed BN.

In this section, the details of the proposed BN-GMPE method, which involves a BN for the post-event updating of a GMPE, are explained. This method is used to estimate the IM at any desired point (both in the near and far seismic regions) within the applicable distance from the epicenter so that the observations of the near-field are used to update the probabilistic term in GMPE for the near-field and the observations in the far-field are used to update the probabilistic term in GMPE for the far-field.

As discussed in previous sections, the typical form of these attenuation models or GMPEs is as follows:

$$
\log \left(Y_{i}\right)=f\left(M, R_{i}, \mathbf{X}_{i}\right)+e_{T}
$$

where $Y_{i}$ is the IM at $i$-th estimation point, $M$ is the magnitude, $R_{i}$ is the epicentral distance of $i$-th estimation point, vector $X_{i}$ denotes other physical parameters (related to $i$-th estimation point) in seismic wave propagation, and $e_{T}$, is the error of GMPE.

Fig. 4 Proposed BN for seismic demand estimation
![img-4.jpeg](img-4.jpeg)

This equation consists of two parts: the function $f$ function, which is the deterministic part, and $e_{T}$, which is the probabilistic term. As mentioned in Sects. 2.1.1 and 2.1.2, this probabilistic term has a normal distribution. $e_{T}$ will be updated using the proposed BN-GMPE method when new observed accelerograms are available. A flowchart of the process of updating a GMPE within a geographical region using the proposed method is shown in Fig. 5, which can be summarized as follows:

- Step 1: All the necessary data (related to earthquake source and recording seismic stations) required for the selected GMPE are extracted from the database.
- Step 2: Initially, the desired IM (PGA or SA) is calculated for all the stations. These stations and all related information are then categorized into two groups based on their epicentral distance: near-field and far-field. Stations with epicentral distances less than 50 km are categorized in near-field and stations with epicentral distances equal or greater than 50 km are categorized in far-field.
- Step 3: In this stage, for model (GMPE) updating using MCMC, first a prior distribution of the GMPE error is considered. Next, the formation of a likelihood function is needed, in which observed IM values and model-predicted values are both considered input values. Then the prior distribution of error and formed likelihood are introduced to the MCMC function to estimate the posterior distribution of probabilistic (error) term in GMPE.
![img-5.jpeg](img-5.jpeg)

Fig. 5 Flowchart of the proposed method (BN-GMPE) for IM estimation

- Step 4: After updating the GMPE error, the updated GMPE will be available to estimate IM at any unsampled location in the applicable distance (Step three and four are repeated similarly for the far-field).
to compare the accuracy of the different methods investigated in this work, the root mean square error (RMSE) and maximum error (MAXE) have been chosen as error metrics respectively, as follows:

$$
\begin{gathered}
R M S E=\sqrt{\frac{1}{n} \sum_{i=1}^{n}\left(y_{i}-\hat{y}_{i}\right)^{2}} \\
M A X E=\max _{i=1}^{n}\left|y_{i}-\hat{y}_{i}\right|
\end{gathered}
$$

where $y_{i}$ is the real value of the $\log _{10}(\mathrm{IM})$ value observed at the $i$-th station, and $\hat{y}_{i}$ is the estimated $\log _{10}(\mathrm{IM})$ at the $i$-th station. In this work, RMSE is calculated by MC method and 20,000 iterations and MAXE is obtained based on the predicted mean value of IMs in estimation points.

From a practical perspective, the importance of accurately calculating the IM can be explained as follows: Firstly, it is assumed that in a specific geographic region, an earthquake occurs, and in this area, there are structures or infrastructures of special significance (such as a network of bridges). Before any action or decision, it is crucial to assess the structural health status of each of these entities in the region so that subsequent planning can prioritize repair, reinforcement, or emergency actions. This structural health assessment is usually based on a comparison between the seismic capacity of a structure and the seismic demand.

Hence, the precise calculation of the IM is of particular importance, especially since seismic sensors are not available at many site locations. One of the tools for comparing capacity against seismic demand is the fragility curve. If fragility curves have been pre-drawn for existing structures with only an estimation of the IM at the site location, it is possible to determine the probability of exceeding a predefined damage state; thus, identifying the most critical assets in the region will be possible.

Accurate estimation of IM can be even useful for the detection or qualification of damage if fragility curves are available for elements of a structure. In that case, it can be determined which element within that structure is more critical and requires more immediate retrofitting action.

# 2.4.1 Numerical algorithm for solving the BN 

Due to the challenges associated with estimating the evidence in the Bayes' theorem, which typically involves a complex integral across the entire parameter space, it is not usually possible to obtain the posterior distribution in Eq. (8) in closed-form, and numerical approaches are usually needed.

In the proposed framework, the classic Metropolis-Hastings MCMC algorithm is employed to estimate the posterior distribution of the probabilistic terms in selected GMPE. This algorithm involves iteratively generating a set of random samples from a target probability distribution by proposing new samples based on a predefined proposal distribution, and then accepting or rejecting them based on a specified acceptance criterion.

As the algorithm proceeds, the generated samples converge to samples from the target (posterior) distribution. PDF can be accurately estimated by acquiring many samples. By repeatedly sampling and using these samples to approximate the posterior, the MetropolisHastings algorithm sidesteps the direct computation of the denominator in Eq. (8), making Bayesian inference feasible in cases where analytical methods would be impractical.

While Metropolis-Hasting algorithm does not provide an exact solution, it offers a way to obtain valuable approximations of the posterior distribution, which can be used for inference. In this study, a function (in adaptive MCMC toolbox developed by Haario et al. (2006)) designed for MATLAB programming environment has been utilized for performing the Metropolis-Hastings algorithm.

The parameters of this algorithm have been set as follows: (burn-in: 2000, Number of samples: 20000, prior distribution of the error SD is assumed a normal distribution with zero mean and sigma corresponding to the error of employed GMPE as reported in Table 1, finally, the starting point is chosen based on a generated random value from the prior distribution. The selection of the prior and proposal distribution have been chosen based on a combination of theoretical considerations and empirical experimentation to ensure efficient and effective sampling.

Another important consideration in the proposed framework is related to the used magnitude criterion. The use of the Ambraseys attenuation relationship (Ambraseys et al. 1996) requires surface magnitudes $\left(M_{s}\right)$, while only local magnitudes $\left(M_{l}\right)$ and moment magnitudes $\left(M_{w}\right)$ are reported in the ESM database (Lanzano et al. 2019), hence, in this work the following formula suggested by Lolli et al. (2014) for a Euro-Mediterranean data set is used to convert $M_{s}$ to $M_{w}$, as follows:

$$
\begin{gathered}
M_{w}\left(M_{s}\right)=\left\{\begin{array}{l}
a M_{s}+b \\
M_{w c}-\sqrt{R^{2}-\left(M_{s}-M_{s c}\right)^{2}} \\
M_{s}
\end{array} \begin{array}{l}
M_{s}<M_{s, l o w} \\
M_{s} \\
M_{s}>M_{s, u p}
\end{array},\right. \\
R=\sqrt{\left(M_{s, l o w}-M_{s c}\right)^{2}+\left(M_{w, l o w}-M_{w c}\right)^{2}} \\
M_{w, l o w}=a\left(M_{s, l o w}\right)+b \quad \text { and } \quad M_{w, u p}=M_{s, u p}
\end{gathered}
$$

where $M_{s c}, M_{w c}$, and $R$ represent the center coordinates and radius of the connecting circular arc in the $M_{s}-M_{w}$ Cartesian space respectively, $M_{s, l o w}$ and $M_{s, u p}$ are lower and upper surface magnitude thresholds, and $a$ and $b$ are constants. All these values are presented in (Lolli et al. 2014) for three different geographical regions. In this study, the values reported for Italy are employed. The required parameters for this formula have been set based on (Lolli et al. 2014) as follows: $a=0.678, b=1.803, M_{s c}=-6.854, M_{w c}=20.664, M_{s, l o w}=4.06, M_{s, u p}=6.91$.

# 2.5 Kriging interpolation model 

Since one of the primary objectives of this article is to compare the estimation accuracy of the proposed method with classic Kriging method, it is beneficial to provide a brief reference to the definition and formulation used for this method.

Kriging refers to a group of geostatistical interpolation methods in which the value at an unobserved location is predicted by a weighted combination of the values at surrounding locations (Isaaks and Srivastava 1989). These weights are determined by a model that characterizes the spatial correlation within the dataset.

Essentially, Kriging involves a dual-phase procedure: initially, a regression (or trend) function is formulated using the data, and then, a stochastic process is formed using the residuals, Given an n-dimensional input $x \in \mathbf{D} \subseteq \mathbb{R}^{n}$, the one-dimensional deterministic response can be expressed by a model $Y$. A representation of this model defined by Lophaven et al. (2002) is as follows:

$$
Y(\mathbf{x})=f(\mathbf{x})+Z(\mathbf{x})
$$

where $f(\mathbf{x})$ represents a regression function, and $Z(\mathbf{x})$ represents a stochastic process. Various prefixes have been assigned to Kriging based on the form of the regression function utilized. However, the task of selecting the appropriate regression function is challenging. In this work, simple Kriging (i.e. $f(x)=0$ ) is assumed, given the evanescent nature of seismic excitation with the epicentral distance.

For a set of $n$ samples, $X=\left\{\mathbf{x}^{1}, \ldots, \mathbf{x}^{n}\right\}$ (including all estimation and observation points) in $d$ dimensions (here there are two dimensions one for geographical latitude and one for longitude) and its associated prediction values, $Y=\left\{Y^{1}, \ldots, Y^{n}\right\}$, the stochastic process is defined by the $\mathrm{n} \times \mathrm{n}$ correlation matrix $\boldsymbol{\Psi}$ as follow:

$$
\boldsymbol{\Psi}=\left[\begin{array}{ccc}
\psi\left(D_{1,1}\right) & \cdots & \psi\left(D_{1, n}\right) \\
\vdots & \ddots & \vdots \\
\psi\left(D_{n, 1}\right) & \cdots & \psi\left(D_{n, n}\right)
\end{array}\right]
$$

where $\psi(.,$.$) is parametrized by a set of hyperparameters \beta$. The selection of the correlation function plays a vital role in the creation of a precise Kriging model. Well-recognized category stationary correlation functions for seismic modelling are exponential functions given by (Couckuyt et al. 2014):

$$
\psi\left(D_{i, j}\right)=\exp \left(-\beta_{i}\left|D_{i, j}\right|^{p}\right), \quad i=1, \ldots, n \quad j=1, \ldots, n
$$

where $D_{i, j}$ indicates the distance between point $i$ and $j$ through Manhattan distance relationship as follows (longitude and latitude of points are shown with LONG and LAT, respectively):

$$
D_{i, j}=\left|\mathrm{LAT}_{i}-\mathrm{LAT}_{j}\right|+\left|\mathrm{LONG}_{i}-\mathrm{LONG}_{j}\right|
$$

these correlation functions only depend on the distance $D_{i, j}$ between the two points $i$ and $j$, indicating that as the distance between two points decreases, the correlation increases. The manner and rate at which this happens is dictated by several parameters.

The parameter $p$ specifies the initial drop in correlation as the distance between points increases. The second set of parameters $\beta_{1}, \ldots, \beta_{d}$ describes how fast correlation drops to zero. While parameter $p$ is usually set fixed, the parameters $\beta_{1}, \ldots, \beta_{d}$ are determined using maximum likelihood estimation (MLE). The MLE of $\beta_{1}, \ldots, \beta_{d}$ describes the amount of variation in LONG and LAT directions.

A high value of $\beta$ indicates highly non-linear behavior in that dimension (i.e. response values for close points in the input space are very different). On the other hand, a low value of $\beta$ means a more linear behavior (i.e. a point is correlated with points that are

farther away). The employed correlation function in this work is considered exponential in which parameter $p$ is set to 1 .

In this study, for performing Kriging estimation, the ooDACE software package (Couckuyt et al. 2014) (implemented in MATLAB 2017a) is used. The following considerations regarding Kriging have been taken into account: The initial guess for hyperparameter $\beta$ in the correlation function is assumed 0.5 and its lower and upper bounds are assumed equal to 0 and 100 , respectively. The optimal choice of the hyperparameter is done by the Genetic Algorithm (GA) function in the ooDACE software package Couckuyt et al. (2014) (implemented in MATLAB 2017a) with 50 population size and 200 generations, while the remaining parameters are set as default defined in ooDACE.

# 3 Numerical results and discussion 

Before entering into the discussion of the results obtained by the proposed method on a selected list of earthquakes, a few assumptions are needed:

1 Soil type classification for A96 is based on shear wave velocity, while for B14, it is based on EC8 (as a result B14 and A96 are different in the definition of rock and stiff soil classes), moreover, the shear wave velocity is not available for all stations in each seismic event so in this work it is assumed that both GMPEs follows EC8 in soil type classification.
2 While both the B14 and A96 datasets employ the Joyner-Boor distance as the source-to-site distance metric, this study, due to the limited availability of data in the ESM dataset, adopts the epicentral distance as the source-to-site distance metric.
3 The PGA and SA values reported in the following sections are calculated based on the geometric mean of two orthogonal horizontal accelerograms (North-South and East-West) . This technique is employed for all the case studies in this work, while the Newmark method has been used for derivation of the SA.
4 B14 is applicable for PGA and PSA, while A96 is just usable for PGA and SA. To compare the accuracy of B14 and A96, and BN-GMPE developed based on these GMPEs, in case study 4, SA is considered as one of the desired IMs. This means that we estimate SA with B14, while its calibration parameters are developed for PSA estimation. So this assumption is considered that SA and PSA are the same.
5 In the literature, there is a variety of definitions for near-field and far-field earthquakes based on factors such as the source-to-site distance, fault mechanism, and the characteristics of the seismic waves. However, there is no single, universally accepted definition of these terms (Davoodi and Sadjadi 2015; Li and Xie 2007). Typically, a distance range of $20-60 \mathrm{kms}$ from the epicenter is defined as the near-field region (Stewart et al. 2002), characterized primarily by its specifications such as forwarddirectivity and fling-step effect (Somerville et al. 1997). The specific distance that separates the two regions will vary depending on the earthquake and the purpose for which the terms are being used.

In this article, after plotting IM values versus epicentral distance for selected earthquakes, it was observed that the IM (i.e., PGA and SA) variations in the range of

$0-50 \mathrm{kms}$ from the epicenter exhibit more pronounced fluctuations compared to similar variations at distances greater than 50 kms .

Therefore, based on this discrepancy in behavior between these two distance ranges, a distinction was made at the 50-kilometer mark to update attenuation models separately for each of these two zones.

This nomination is solely based on distance and the disparity in IM reduction behavior, which is due to directivity effect in near-field (the related data have not been presented due to space constraints). Another reason for selecting 50 km instead of the more acceptable distance of 20 km is having enough seismic stations in the near-field.
6 The ratio between observation and estimation points is assumed 50-50. Since one of the main goals of this article is to compare the accuracy of the proposed method with the Kriging method, changing this ratio probably shows only some information about sensitivity. Investigating which method is more sensitive to the ratio between observation and estimation points requires a separate comprehensive analysis. Therefore, to maintain brevity and focus on the core aspects of this research, this sensitivity analysis is not performed in this study.
7 For generating random points' arrangements in the validation process first, stations for a specified earthquake are divided into two categories based on their epicentral distance: Near-field $(R<50 \mathrm{~km})$ and Far-field $(50 \leq R<300 \mathrm{~km})$. Therefore a vector of stations for each category will be defined (named Field vector).

To determine estimation points and observation points, a random permutation of integers (here are indices of the elements of Field vector) is generated and a new Field vector is formed that has the same elements of Field vector but with randomly changed permutation, and in the next step, half of the new Field vector constitutes a vector (observation vector) of the indices of observation points, and the other half forms a estimation vector.

If the number of stations in each observation or estimation vector is odd, then the number of estimation points is one more than the observation points. It is worth mentioning that the least number of stations for the observation vector is considered as 2 .

Hereinafter, five separate case studies have been designed, each pursuing a distinct objective. In the first case study, we will demonstrate that the adopted approach for separating the far-field and near-field regions in observation-based methods (such as the proposed method, and the Kriging method) improves the accuracy of IM estimation. The second case study aims to reveal the limitations of the Kriging method and its higher sensitivity to the arrangement of observation and estimation points compared to the proposed method.

The third case study is focused on a single seismic event, and the primary goal is to investigate the process of obtaining results for the far-field and near-field domains as well as to illustrate how to quantify uncertainty in the final results using uncertainty bounds. In the fourth case study, the accuracy of the proposed method is compared with the Kriging method, separately for the far-field and near-field domains for the IMs of PGA and SA for 63 chosen earthquakes (each earthquake has been assessed 10 times with different points' arrangement).

Obtained results from the fourth case study indicate that the best IM estimation method differs depending on the desired IM, the estimated field, the selected earthquake, and the arrangement of observation and estimation points, so a general

framework and guideline for selecting the most accurate method for IM estimation has been proposed in the fifth case study.

# 3.1 Case study 1: effect of region classification on IM estimation error 

From past observations, it has been demonstrated that near-field ground motions can exhibit characteristics significantly different from those in the far-field because of the directivity and fling step effects (Somerville et al. 1997).

The innovative approach of separating the updating process of the far-field from the near-field, developed in the proposed methodology, stems from the distinction in the behavior of IM attenuation before and after the distance of 50 km (usually, the near-field is considered at a 20 km distance from the epicenter but in this work to have enough observation points in the near-field 50 km is chosen).

To examine the impact of implementing this approach on the accuracy of IM estimation, Italian seismic events from 2014 to 2016 (53 events) have been considered in this case study (please see Table 7 in Appendix A).

To assess the accuracy of the proposed method and other methods, each seismic event is evaluated ten times separately (each time with a different random arrangement of observation points and estimation points in a ratio of 50-50). Finally, for each method, the average of RMSE and MAXE (obtained by MC with 20000 iterations) of all these 10 arrangements for each seismic event has been calculated ( 530 cases).

Five different methods of IM estimation including two GMPEs (B14 and A96), two proposed BN-GMPEs (BN-B14 and BN-A96), and a simple Kriging method ( Kr ) are used to estimate PGA at estimation points employing two different approaches: (i) Approach 1 (A1) represents the separate updating procedure for the near and far fields for the BN-GMPEs, and separate interpolation process for these fields for Kr , and (ii) Approach 2 (A2) considers no separation for updating process or interpolation.

The data corresponding to this case study is presented in Table 2. In this table estimation errors are reported for near-field, and far-field for approach 1, and also total estimation error for this approach is computed based on the weighted average (considering the number of stations in each field).

For ease of comparison, the results related to observation-dependent methods (i.e., Kr , BN-B14, and BN-A96) are highlighted in bold in the table. Comparing the bold values shows that using approach 1 (with region classification) in these methods has reduced the estimation error. It is also evident that the use or non-use of classification does not affect the accuracy of methods that are not observation-dependent. Therefore, the total error estimation in both approaches is the same for the non-bold values (i.e., B14 and A96) in the two rightmost columns of the table. This point shows the undeniable significance of the region separation in GMPE updating.

Using different approaches does not affect on estimation by GMPEs since they estimate IMs regardless of observations and just depend on the physical parameters of unsampled locations.

Data related to Table 2 is depicted in Fig. 6. It can be seen in both RMSE and MAXE that the blue column is shorter than the black one for observation-based methods, which means that the region classification approach has improved estimation accuracy. Moreover, by comparing the green and the red column it can be seen that in all cases the estimation of $\log 10(\mathrm{PGA})$ exhibits higher error in far-field.

![img-6.jpeg](img-6.jpeg)

Fig. 6 Comparison of the errors in $\log _{10}(\mathrm{PGA})$ estimation distinguishing (Approach1-A1) and not distinguishing (Approach2-A2) near and far field stations for case study 1. The terms NF, FF, and WF denote near-field, far-field, and whole-field, respectively (for Italian seismic events from 2014 to 2016)

Table 2 Comparison of $\log _{10}(\mathrm{PGA})$ estimation error with and without region classification for case study 1 (for Italian seismic events from 2014 to 2016)


${ }^{1}$ (A1): Approach 1 with consideration separate updating processes for near-field (NF) and far-field (FF)
${ }^{2}$ (A2): Approach 2 considering just one field, whole field (WF)
${ }^{3}$ Near-field
${ }^{4}$ Far-field
${ }^{5}$ Whole-field

# 3.2 Case study 2: effect of observation and estimation points' arrangement on PGA estimation error 

In this section, to investigate the impact of the spatial distribution of observation and estimation points on the accuracy of IM estimation at estimation locations, as well as to demonstrate the limitations of the Kriging method in specific scenarios, we first consider

a seismic event (epicenter: longitude: $13.1232^{\circ}$, latitude: $42.8379^{\circ}$, with a moment magnitude of 6.6, the event ID in ESM dataset: EMSC-20161030-0000029) occurred in Norcia, Italy on 30th Oct 2016. Subsequently, the PGA is separately estimated at estimation points for two different types of points' arrangement. (data related to selected points are provided in Appendix B)

It is worth mentioning that, in this case study, since the aim is only to investigate the effect of the arrangement of the observation and estimation points on the IM estimation error, there is no need to separate near-field and far-field for the updating process.

The first scenario represents a situation where points (including observation points and estimation points) are non-uniformly distributed over different epicentral distances. The positioning points in this scenario can be seen in Fig. 7a.

In the second scenario, with the same ratio of 50-50 between the number of observation and estimation points, the arrangement of their positioning is changed at previously selected coordinates for points to obtain a more uniform distribution around the epicenter, as shown in Fig. 7b.

It is noted in this figure that, when the points' arrangement is non-uniform, the area with maximum PGA predicted by Kriging does not coincide with the real epicenter location. On the contrary, the predictions for uniform points' arrangements are more accurate.

In Fig. 7c-f the $\log _{10}(\mathrm{PGA})$ estimated for the estimation points by the proposed methods (BN-A96, and BN-B14) and the Kriging method is drawn against the epicentral distance, and it can be seen that when the points' arrangement is more uniform, the estimated $\log _{10}$ (PGA) values for all three methods are closer to the actual values at the estimation points. Data related to these graphs are given in Table 3. In this table, the PGA estimation error of each method for two different types of points' arrangement is provided. Given the emphasis on the Kriging method's high sensitivity to points' arrangement in this case study, the results for this method are highlighted in bold in the table.

As can be seen in Table 3, for estimating PGA with the Kriging method, the calculated RMSE in the non-uniform arrangement (RMSE $=0.842$ ) is greater than RMSE in the situation where the point positioning is more uniform ( $\mathrm{RMSE}=0.530$ ), and the MAXE for estimating PGA using Kriging for non-uniform arrangement (MAXE $=1.100$ ) is almost three times higher compared to the case where the arrangement is uniform (MAXE $=0.3$ ).

Although the increase of the estimation error in the case of non-uniform arrangement (in both cases of the RMSE and the MAXE) can be seen for the proposed methods as well, according to the absolute difference of errors given in the rightmost column of Table 3, it can be argued that the sensitivity of the proposed methods (compared to the Kriging method) to the arrangement of points, is much lower.

Therefore, it can be concluded that the proposed method (because of taking into account the physical factors of seismic wave propagation in the final estimation) exhibits greater robustness compared to simple Kriging in IM estimation, and estimation using Kriging has significantly higher errors when observation points are non-uniformly distributed.

# 3.3 Case study 3: examination of the proposed method in PGA estimation for the 2014 Central Italy earthquake 

In this section, to provide a better understanding of the performance of the proposed method, an Italian earthquake that occurred in 2014 (epicenter located at: longitude: $11.2405^{\circ}$, latitude: $43.6058^{\circ}$, with a moment magnitude of 4.1 , the event ID in ESM

![img-7.jpeg](img-7.jpeg)

Fig. 7 Comparison of the effect of points' arrangement on $\log _{10}(\mathrm{PGA})$ estimation with different methods for case study 2 (for 2016 Norcia earthquake in Italy)
dataset: EMSC-20141219-0000039) has been chosen. For this case study, 58 stations are considered (including 6 seismic stations for estimation located in the near-field and 23 stations for estimation in the far-field shown with plus signs), and the positioning of observation points and estimation points have been randomly arranged as explained in the assumptions presented at the beginning of Sect. 3. Points' arrangement is illustrated (separately for near and far fields) in Fig. 8a and b. The contours in the mentioned figures show the PGA estimation by the Kriging method.

Table 3 Comparison of $\log _{10}$ (PGA) estimation error for uniform and non-uniform points' arrangement for case study 2 (for 2016 Norcia earthquake in Italy)


The plots in Fig. 9a-d show the trace of the bias and error SD (of $\log _{10}(\mathrm{PGA})$ ) obtained by the MCMC method for the near-field, and Fig. 10a-d for far-field. As evident, these plots indicate the convergence of sample values towards their mean and the associated uncertainty given by one standard deviation away from the mean value.

In view of the results in these figures, it can be argued that the obtained consistent mean value, low variability, and narrow standard deviation bounds demonstrate a high degree of stability. Regarding these figures it can be argued that consistent mean value, low variability, and narrow standard deviation bounds demonstrate a high degree of stability.

Figure 9e-h compare the prior and posterior distributions of bias term in GMPE for BN-A96 and BN-B14 methods in the near-field, while Fig. 10e-h depict the same comparison for the far-field. Figure 9 i and j compare the prior and posterior distributions of error SD term in GMPE in the near-field, while Fig. 10i and j depict the same comparison for the far-field.

Clearly, in all cases related to the bias, the posterior distributions have lower uncertainty compared to the prior distributions. Fig. 8c-f show that the posterior of A96 has a greater deviation from the mean value of its prior compared to B14 in both near and far fields, which indicates the higher accuracy of B14 compared to A96, and B14 estimation is closer to real values compared to A96 in most target points.

The other point that should be noted is that, by comparing Figs. 9h and 10h, both of which are related to B14, it becomes apparent that the PDF of the posterior in the far-field has a shorter tail compared to the posterior tail in the near-field, and this observation holds true for A96 by comparing 9 g and 10 g as well. The reason for this difference is that, in this case study, there are more observed points in the far-field compared to the near-field.

Figures 8c and e illustrate a comparison of $\log _{10}(\mathrm{PGA})$ estimation results obtained by different methods for the near-field. As observed, the uncertainty bounds for the proposed BN-based approach (BN-A96 and BN-B14) as well as the uncertainty bounds for simple GMPE methods and simple Kriging are shown with vertical error bars, with the mean values indicated with markers in the middle.

The results are also compared with real values at target points. Similarly, the same comparison is provided in Fig. 8d and f which show the mean and standard deviation of estimations using the mentioned methods for the far-field.

The important point in Fig. 8d and f is that as it can be seen in the far-field for this specific earthquake, estimation by both GMPEs is overestimated. Furthermore, although the results estimated by BN-GMPEs (BN-A96 and BN-B14) are also overestimated in most stations, they are much closer to real values of PGAs compared to their corresponding GMPEs.

![img-8.jpeg](img-8.jpeg)

Fig. 8 Comparison of estimation results by different methods between near-field and far-field for case study 3 (2014 earthquake in Italy)

However, the estimation by Kriging, especially after 150 kms , is underestimated in most cases. Data related to Fig. 8c-f are given in Table 4.

# 3.4 Case study 4: PGA and SA estimation for the Central Italy earthquakes between 2014 and 2016 

SA is a critical factor in structural engineering because it is valuable for assessing a structure's response to different frequency components of an earthquake. Therefore, in this case study, SA for three different natural periods $(0.2,1$, and 2 s$)$ is estimated as the

![img-9.jpeg](img-9.jpeg)
![img-10.jpeg](img-10.jpeg)
(i) PDFs of prior and posterior bias for BN-A96
![img-11.jpeg](img-11.jpeg)

Prior and posterior of error SD (BN-Amb96)
![img-12.jpeg](img-12.jpeg)

Fig. 9 Detailed estimation results achieved by proposed methods (BN-A96 and BN-B14) for the near-field for case study 3 (2014 earthquake in Italy)

![img-13.jpeg](img-13.jpeg)
![img-14.jpeg](img-14.jpeg)
(i) PDFs of prior and posterior bias for BN-A96
![img-15.jpeg](img-15.jpeg)

Fig. 10 Detailed estimation results achieved by proposed methods (BN-A96 and BN-B14) for the far-field for case study 3 (2014 earthquake in Italy)

Table 4 Updated error term in B14 and A96 based on 2014 Central Italy earthquake and $\log _{10}(\mathrm{PGA})$ estimation error with different methods for case study 3


IM alongside PGA. The accuracy of the proposed BN-based method is then compared with simple GMPEs (B14 and A96) and the Kriging method. The details of selected seismic events between 2014 and 2016 are reported in Table 8 in Appendix A.

In Fig. 11, a comparison between different methods for accuracy estimation of $\log _{10}$ (PGA) and $\log _{10}(\mathrm{SA})$ is presented. The most important point in this Figure is that the proposed methods BN-B14 and BN-A96 yield a considerably more accurate estimation compared to Kriging and simple GMPEs in the Near and far field based on both obtained RMSE and MAXE and also the RMSE after the update in both proposed methods has been reduced by more than half.
$\log _{10}(\mathrm{SA})$ estimation for three different natural periods is shown in Fig. 11. As can be observed in all cases BN-B14 and BN-A96 have better accuracy compared to kriging and their own un-updated versions, and it means that updating of attenuation model resulted in better accuracy in general. An interesting point in these results is that, although the RMSE in the original GMPEs is higher than the Kriging method, the estimation accuracy of the GMPE after model updating consistently outperforms Kriging.

All data related to Fig. 11 is provided in Table 5, where the best method in each category is visible. Based on this table, it can be concluded that not only BN-B14 and BN-A96 have better accuracy compared to the other methods but also have less uncertainty in estimation (based on the reported error SD).

Table 5 $\log _{10}(\mathrm{IM})$ estimation error for Italian earthquakes between 2014 and 2016 for case study 4(IM in $\mathrm{cm} / \mathrm{s}^{2}$ )


However, it is important to keep in mind that the arrangement of observation and estimation points is decisive for the estimation accuracy of Kriging and the proposed method. As a result, a framework is provided in case study 5 to choose the most accurate IM estimation method after an assumed earthquake in the future.

# 3.5 Case study 5: proposed IM estimation framework for 2016 earthquake in Central Italy with 1000 different points' arrangement 

Based on the results obtained from case studies 1 to 4 , it can be argued that the most accurate post-earthquake IM estimation method for various earthquakes may differ. Even for a specific earthquake, the best estimation method for the near-field and far-field may vary, and even with a change in station configuration, the error rates of the methods will change.

This issue also depends on the IM under consideration. For instance, one method may be better for PGA estimation, while another method is more suitable for SA. These variations even occur for different periods for SA estimation, as observed in the previous case study. Therefore, providing a decision-making framework for selecting the best method with the least estimation error is essential.

In this regard, PGA is considered as the desired IM, and the 2016 Norcia earthquake in Central Italy (epicenter: longitude: 13.12320, latitude: 42.83790, with a moment magnitude of 6.6, the event ID in ESM dataset: EMSC-20161030-0000029 occurred on 30th Oct 2016) is considered as a case study. For this earthquake, 122 seismic recording stations are taken into account as estimation and observation points.

To select the most accurate method, 1000 station configuration scenarios have been examined, with a $50-50$ ratio between observation and estimation points in all of these 1000 cases. Then, the average values of RMSE and MAXE for the near-field and far-field are calculated for these 1000 cases, which are visible in Table 6. As can be seen in this table, the proposed BN-GMPE methods have the best performance in terms of estimation accuracy and uncertainty reduction.

To better compare the performance of different methods, two spider plots are drawn based on the information of Table 6, separately for near and far fields which can be seen in Fig. 12, indicating the ranking of each method based on the estimation error level (lower numbers mean better rank in terms of estimation error). In this way, after an assumed seismic event, having access to such a graph allows for the determination of which method is most appropriate for estimating the considered IM in each near-field and far-field region.

## 4 Conclusions

In this paper, a method for estimating the post-earthquake IM in unsampled locations (lacking seismic sensors) within a region has been presented. Accurate IM estimation is crucial for seismic demand modeling and assessing the structural probability of failure. One of the most conventional methods for estimating the IM in a seismicity-affected geographic region involves interpolation and extrapolation using Kriging.

Since traditional simple Kriging can not consider the physical parameters of earthquake wave propagation, the accuracy of estimates using this approach is highly dependent on the

![img-16.jpeg](img-16.jpeg)
![img-17.jpeg](img-17.jpeg)
(g) RMSE $(\mathrm{T}=2 \mathrm{sec})$
![img-18.jpeg](img-18.jpeg)
(b) MAXE
![img-19.jpeg](img-19.jpeg)
(d) $\operatorname{MAXE}(\mathrm{T}=0.2 \mathrm{sec})$
![img-20.jpeg](img-20.jpeg)
(f) $\operatorname{MAXE}(\mathrm{T}=1 \mathrm{sec})$
![img-21.jpeg](img-21.jpeg)
(h) $\operatorname{MAXE}(\mathrm{T}=2 \mathrm{sec})$
![img-22.jpeg](img-22.jpeg)

Fig. $11 \log _{10}(\mathrm{IM})$ estimation with different methods for Italian earthquakes between 2014 and 2016 for case study 4 (PGA and SA in $\mathrm{cm} / \mathrm{s}^{2}$ )

Table $6 \log _{10}(\mathrm{IM})$ estimation error for 2016 Norcia Earthquake in Central Italy with 1000 different points' arrangement for case study 5 (IM in $\mathrm{cm} / \mathrm{s}^{2}$ )


![img-23.jpeg](img-23.jpeg)

Fig. $12 \log _{10}(\mathrm{PGA})$ estimation error of different methods for 2016 Norcia Earthquake in Central Italy for case study 5
spatial distribution of observation and target points and may result in significant errors as it is shown in case study 2 .

To address this issue, the proposed BN-GMPE method, which allows for the updating of selected GMPEs using BNs, has been suggested. Additionally, given that the characteristics of earthquake wave propagation differ in the near-field and far-field regions, the updating process for these two regions has been separated.

The main findings obtained in this study are as follows:

1. The approach of separating the earthquake region into two zones, near ( $0-50 \mathrm{kms}$ ) and far ( $50-300 \mathrm{kms}$ ) fields, for the GMPE updating process, in comparison to the approach without separation, significantly improves accuracy as it is demonstrated in case study 1. The reason for this accuracy improvement is that, based on the examined models, the attenuation in IM in the near-field exhibits different behavior. Therefore, using observations from the far-field for updating the GMPE in the near-field leads to significant errors. This holds true for the use of near-field observations for updating in the far-field as well.
2. According to the results of the second case study, in non uniform arrangement of observation and estimation points, Kriging estimation may result in higher errors. However, the proposed BN-GMPE method shows less sensitivity to the points' arrangement, justifying the need for developing an alternative IM estimation method besides interpolation methods such as Kriging.
3. Based on the results from the graphs in the third case study and the reported table in the fourth case study, it can be concluded that the proposed method has less uncertainty compared to its corresponding simple GMPE and Kriging.
4. According to a comprehensive comparison conducted in the fourth case study, it was concluded that the most accurate estimation method can vary depending on the desired IM, and points' arrangement but in all cases BN-based method always has the best performance in terms of accuracy and decreasing uncertainty in estimations.

To have a decision-making framework for finding the best post-earthquake IM estimation it is important to compute estimation errors (RMSE and MAXE) for various observation and estimation point arrangements using both BN-GMPE and Kriging. If one method demonstrates superior accuracy on average, it could be exclusively employed for IM estimation in that specific region and earthquake scenario. Furthermore, apart from the mentioned advantages, this framework can easily be expanded to include the following potential uses in the future:

1 The proposed BN framework is poised for an extension to estimate failure probabilities for diverse structures in a targeted region. For example, each structure in the network can be defined as a node with a seismic demand and additionally a capacity model.

Through Bayesian inference and updating shared variables among similar structures in the network, it becomes possible to update the vulnerability status of each structure (for example, via updating the fragility curve).
2 It is important to remark that the directionality of rupture can have a significant influence on IM at different locations in the area affected by an earthquake because it has a direct effect on source-to-site distance calculations. Therefore, this important factor should be considered in the GMPE updating process. Similarly, such considerations could also be incorporated into the interpolation or extrapolation processes, as more advanced kriging methods can take physical factors into account.
3 In this work, horizontal source-to-site distance is considered in selected GMPEs, However, to avoid neglecting the important factor of earthquake focal depth, it is advisable to use GMPEs in future works that incorporate focal depth into the equations.

# Appendix A 

See Tables 7 and 8.

Table 7 Selected earthquakes for case study 1 from ESM database (Lanzano et al. 2019)


Table 7 (continued)


Table 8 Selected earthquakes for case study 4 from ESM database (Lanzano et al. 2019)


Table 8 (continued)


# Appendix B 

See Tables 9 and 10.
Table 9 Selected seismic stations for uniform points' arrangement in case study 2


Table 10 Selected seismic stations for non-uniform points' arrangement in case study 2


Funding Open access funding provided by Università degli Studi di Perugia within the CRUI-CARE Agreement. This work was supported by the Italian Ministry of Education, University and Research (MIUR) through the funded project of national interest FAIL-SAFE: near-real-time perFormance Assessment of exIsting buiLdings Subjected to initiAl Failure through multi-scalE simulation and structural health monitoring (Protocol No. 2022JFXE95)

Data Availability The datasets utilized in this study are available in a machine-friendly platform to access data and metadata through this web address: https://esm-db.eu/4/data_and_services/web_services

# Declarations 

Conflict of interest The authors declare no Conflict of interest, ethics, or otherwise.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.

# Authors and Affiliations 

## Pooria Mesbahi ${ }^{1} \cdot$ Enrique García-Macías ${ }^{2} \cdot$ Marco Breccolotti ${ }^{1} \cdot$ Filippo Ubertini ${ }^{1 *}$

Filippo Ubertini
filippo.ubertini@unipg.it
Pooria Mesbahi
pooria.mesbahi@unipg.it
Enrique García-Macías
enriquegm@ugr.es
Marco Breccolotti
marco.breccolotti@unipg.it
1 Department of Civil and Environmental Engineering, University of Perugia (UNIPG), Via G. Duranti, 93, 06125 Perugia, Italy
2 Department of Structural Mechanics and Hydraulic Engineering, University of Granada, Campus Universitario de Fuentenueva s/n, 18071 Granada, Spain