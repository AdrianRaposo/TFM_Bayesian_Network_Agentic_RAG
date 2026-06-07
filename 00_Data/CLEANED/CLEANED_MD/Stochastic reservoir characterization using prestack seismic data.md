# NORGES TEKNISK-NATURVITENSKAPELIGE UNIVERSITET 

## Stochastic Reservoir Characterization Using Pre-stack Seismic Data

by

Jo Eidsvik, Per Avseth, Henning Omre, Tapan Mukerji and Gary Mavko

## PREPRINT <br> STATISTICS NO. 7/2001 <br> ISSN: 0804-9173

![img-0.jpeg](img-0.jpeg)

## NORWEGIAN UNIVERSITY OF SCIENCE AND TECHNOLOGY <br> TRONDHEIM, NORWAY

This report has URL http://www.math.ntnu.no/preprint/statistics/2001/S7-2001.ps
Jo Eidsvik has homepage: http://www.math.ntnu.no/ joeid
E-mail: joeid@math.ntnu.no
Address: Department of Mathematical Sciences, Norwegian University of Science and Technology, N-7491 Trondheim, Norway.

# STOCHASTIC RESERVOIR CHARACTERIZATION USING PRE-STACK SEISMIC DATA 

Jo Eidsvik ${ }^{1}$ Per Avseth ${ }^{2}$ Henning Omre ${ }^{1}$<br>Tapan Mukerji ${ }^{2}$ Gary Mavko ${ }^{2}$

${ }^{1}$ Department of Mathematical Sciences, Norwegian University of Science and Technology, 7491 Trondheim, Norway, http://www.math.ntnu.no
${ }^{2}$ Rock Physics Laboratory, Department of Geophysics, Stanford University, California 94305-2215, USA, http://pangea.stanford.edu

January 102001

#### Abstract

A spatial stochastic model for integration of well observations and seismic AVO data in reservoir characterization is presented. The model is defined in a Bayesian setting. The reservoir variables are represented as binary variables: sand or shale lithofacies; and brine or oil pore fluids. The prior spatial models are Markov random fields. Rock physics relations are used in the likelihood models in order to link the reservoir variables and the seismic AVO attributes. The posterior model is defined, and sampled from by a Markov chain Monte Carlo algorithm. The reservoir characteristics are presented as: samples from the posterior model; maximum aposteriori predictions; and probability maps. The approach is demonstrated on data from a North Sea turbidite system.

# Introduction 

Reliable reservoir characterization is of utmost importance in management of petroleum reservoirs. This characterization should be based on all available information about the reservoir. Two types of information exist: general reservoir information and reservoir specific observations. The former contains experience from studies of analogues and general physics theory. The latter constitutes the measurements actually made in the reservoir under study, i.e. well observations, seismic data and production history, if available.

In the current paper, lithofacies and pore fluids are mapped based on well observations and amplitude versus offset(AVO) seismic data. This is traditionally done in a deterministic setting, see Ostrander(1984) and Castagna et al(1998). The classification will normally be associated with large uncertainties, hence casting the problem in a statistical framework seems natural. This is done in Lörtzer and Berkhout(1992) and Avseth et al(2001). However, their models do not include spatial dependencies. In the current paper, the mapping is phrased as a spatial, Bayesian inversion problem, see Omre and Tjelmeland(1997). The work is partially inspired by the work in image analysis, see Besag(1974) and Tjelmeland and Besag(1998). Several authors have used spatial statistical approaches to integrate well observations and seismic data, see Doyen(1988), Bortoli et al(1993), Haas and Dubrule(1994) and Eide et al(1999). None of these papers use seismic AVO data, however. In a recent paper, Buland and Omre(2000), AVO inversion in a Bayesian setting is presented. The elastic properties are modeled, but it falls short of modelling reservoir characteristics like lithofacies and pore fluids.

The current paper constitutes an extension of the study reported in Avseth et al(2001). The work is generalized to account for spatial dependencies. Moreover, integration of both well observations and seismic AVO data is done. The stochastic model is formalized and communicated through a stochastic graph. A sampling algorithm with favorable properties is used. Otherwise most model assumptions and parameter values are inherited from Avseth et al(2001), in which they are thoroughly discussed.

## Problem setting

A turbidite sedimentary system located in South Viking Graben, North

Sea is evaluated. The reservoir sands represents the Heimdal Formation of Late Paleocene age, and includes an oil field of economic interest. Focus is on a heterogenous sand and shale layer representing the upper part of the Heimdal Formation. This layer is located at approximately two kilometers depth, and is capped by a shale unit, representing the Lista Formation. Hence the study is on a lateral 2D domain, termed $\mathcal{D}$, with approximate area $(6 \times 12) \mathrm{km}^{2}$, but on varying depth. The variables of interest are facies and fluid distributions over $\mathcal{D}$. See Avseth et al(2001) for more details.

The general reservoir information comes primarily from studies of other reservoirs in the same sedimentary setting and from rock physics theory. Moreover, observations in well logs in the reservoir zone is used to estimate certain model parameters. This is used to establish a prior stochastic model. In particular, the facies variable is defined to be binary: $Q_{x} \in\{$ shale,sand $\}$ and so is the fluid variable $S_{x} \in\{$ brine,oil $\}$. Both of them varying over $\mathcal{D}$, of course. This is in accordance with the model used in Avseth et al(2001).

The reservoir specific observations come from a 3 D seismic study over $\mathcal{D}$ and four wells penetrating the reservoir. The observations are:

- Seismic reflection time to top reservoir on a grid of size $245 \times 506$. This is denoted $t_{x}$ and displayed in Figure 1.
- AVO attributes extracted from pre stack seismic data represented on the same grid as above. This is denoted $d_{s, x}=\left(a_{x}^{o}, b_{x}^{o}\right) ; a_{x}^{o}$ being zero offset reflectivity, and $b_{x}^{o}$ being AVO gradient, see Figure 2.
- Observations of facies type and fluid filling in four wells, denoted $d_{w}=$ $\left(q^{o}, s^{o}\right)$, see Figure 3.
- Cap rock properties, assumed to be laterally constant, determined from the wells. This is denoted $c r=\left(\rho^{r}, v_{P}^{c}, v_{S}^{c}\right)=\left(2250 \mathrm{mg} / \mathrm{cm}^{3}, 2400 \mathrm{~m} / \mathrm{s}\right.$, $1000 \mathrm{~m} / \mathrm{s}$ ), with $\rho$ being density, and $v_{P}$ and $v_{S}$ being P-wave and $\mathrm{S}-$ wave velocity respectively.

The objective of the study is to characterize the lateral facies and fluid distributions over $\mathcal{D}$, based on the available general reservoir knowledge and conditioned to the available reservoir specific observations.

# Stochastic model 

The reservoir model is represented on a grid of size $245 \times 506$ with unit $25 \mathrm{~m} \times 25 \mathrm{~m}$ over $\mathcal{D}$, denoted $\mathcal{L}_{\mathcal{D}}$. This corresponds to the seismic grid. In order to integrate the seismic data in the study the following reservoir variables are modeled:

$$
R_{x}=\left\{\left(Q_{x}, S_{x}, \Phi_{x}, \rho_{x}, V_{P, x}, V_{S, x}\right) ; x \in \mathcal{L}_{\mathcal{D}}\right\}
$$

with $x$ being a location reference running over the grid $\mathcal{L}_{\mathcal{D}} ; Q_{x}$ being a facies indicator; $S_{x}$ being a fluid indicator; $\Phi_{x}$ being porosity; $\rho_{x}$ being density; $V_{P, x}$ being P-wave velocity and $V_{S, x}$ being S-wave velocity. Capital letters indicate random variables, hence $R_{x}$ is a $6 \times 245 \times 506$ dimensional random variable representing a six dimensional spatial random field on the grid $\mathcal{L}_{\mathcal{D}}$. The probabilistic properties will be fully specified by the associated probability density function (pdf) $f\left(r_{x}\right)$. The reservoir variables are interdependent as displayed in Figure 4. The actual model assumptions must be based on the available general reservoir knowledge and it is termed the prior model. The links between the reservoir variables and the available reservoir specific observations are termed the likelihood model. These are defined by the data acquisition procedures used.

## Prior model

The facies indicator $\left\{Q_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$ is binary; \{shale, sand\}. It is assumed to be a first order Markov random field, see Appendix A, having the Gibbs formulation,

$$
\begin{aligned}
\operatorname{Prob}(Q=q) & =\operatorname{Prob}\left(Q_{x}=q_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right) \\
& =\text { const } \cdot \exp \left(\Sigma_{c \in \mathcal{C}} \nu_{c}(q)\right) \\
& =\text { const } \cdot \exp \left(\beta_{q} \cdot \Sigma_{i \sim j} I\left(q_{x_{i}}=q_{x_{j}}\right)\right)
\end{aligned}
$$

with $I(A)$ being an indicator function taking value 1 if $A$ is true and 0 else; and $i \sim j$ denoting the sum over all neighboring pairs. The parameter of the model, $\beta_{q}$, controls the spatial continuity of the facies distribution. Increasing values of $\beta_{q}$ entails larger continuity. In the study $\beta_{q}=1.25$ hence some continuity in the facies is assumed. It is possible to estimate the spatial dependence from for example a training image, see Besag(1974). Here shale and sand is chosen to have equal probability to occur, and the continuity is defined by a fairly small neighborhood only. This defines a fairly vague prior pdf $f\left(q_{x}\right)$.

The fluid indicator $\left\{S_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$ is also binary; with possible outcomes \{brine, oil\}. It is also assumed to be a first order Markov random field, see Appendix A, having the Gibbs formulation,

$$
\begin{aligned}
\operatorname{Prob}(S=s \mid t) & =\operatorname{Prob}\left(S_{x}=s_{x} \mid t_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right) \\
& =\text { const } \cdot \exp \left(\Sigma_{c \in \mathcal{C}} \nu_{c}(s)\right) \\
& =\text { const } \cdot \exp \left(\beta_{s} \cdot \Sigma_{i \sim j} I\left(s_{x_{i}}=s_{x_{j}}\right)-\Sigma_{i} \alpha_{s}\left(t_{x_{i}}\right)\right)
\end{aligned}
$$

with $I(A)$ and $i \sim j$ being defined as above. The parameter values used are; $\alpha_{s}\left(t_{x}\right)=\eta_{h}\left[I\left(s_{x}=1\right)\left(t_{x}-h_{l}\right)-I\left(s_{x}=0\right)\left(t_{x}-h_{l}\right)\right]$, hence oil/brine contact is a function of depth through the seismic reflection times $t_{x}$. The parameter $h_{l}$ represents the expected oil/brine contact level and has been set to $2075 \mathrm{msec} ; \eta_{h}=0.01$ is a constant determining the depth uncertainty in the oil/brine contact; moreover $\beta_{s}=1.25$, hence some continuity in the fluids is assumed. In Figure 5, $\operatorname{Prob}\left(S_{x_{i}}=s_{x_{i}} \mid t_{x_{i}}, S_{x_{j}}=s_{x_{j}} ; j \sim i\right)$ is displayed as a function of $t_{x}$ and number of neighbors being identical to the center variable. This represents the influence of the seismic reflection time on the fluid model. This defines the prior pdf $f\left(s_{x} \mid t_{x}\right)$. Note the stochastic dependence on the seismic reflection time, which is represented by a single arrow in Figure 4.

Note that the facies and fluid characteristics are independent of eachother in the prior model. The fact that the combination \{shale, oil\} has no petrophysical meaning does not cause problems. Dependence will, of course, be enforced by the conditioning on the reservoir specific observations.

The porosity $\left\{\Phi_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$ is dependent on the facies type:

$$
\left\{\left[\Phi_{x} \mid q_{x}\right]=\mu_{q, x}+U_{\Phi} ; x \in \mathcal{L}_{\mathcal{D}}\right\}
$$

with $\mu_{q, x}$ being the expected value 0.3 and 0.2 for sand and shale respectively; and $U_{\Phi}$ being $N\left(0,0.025^{2}\right)$, with $N(\cdot, \cdot)$ denoting the Gaussian distribution. This defines $f\left(\phi_{x} \mid q_{x}\right)$, and the stochastic dependence on the facies indicator is represented by a single arrow in Figure 4.

The density $\left\{\rho_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$ is dependent on both facies, fluid and porosity:

$$
\left\{\left[\rho_{x} \mid q_{x}, s_{x}, \phi_{x}\right]=\rho_{q, x}\left[1-\phi_{x}\right]+\rho_{s, x} \phi_{x}+U_{\rho} ; x \in \mathcal{L}_{\mathcal{D}}\right\}
$$

with $\rho_{q, x}$ being matrix density $2700 \mathrm{mg} / \mathrm{cm}^{3}$ for shale(clay) and $2650 \mathrm{mg} / \mathrm{cm}^{3}$ for sand(quartz); $\rho_{s, x}$ being fluid density $1100 \mathrm{mg} / \mathrm{cm}^{3}$ and $800 \mathrm{mg} / \mathrm{cm}^{3}$ for

brine and oil respectively, and $U_{\rho}$ being $N\left(0,50^{2}\right)$. Hence there is a slight contrast between the cap rock and the shale in the reservoir. This defines the pdf $f\left(\rho_{x} \mid q_{x}, s_{x}, \phi_{x}\right)$ to be Gaussian, and the stochastic dependencies are represented by single arrows in Figure 4.

The seismic P-wave velocity, $\left\{V_{P, x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$, is dependent on facies, fluid and density and can be expressed as:

$$
\left\{\left[V_{P, x} \mid q_{x}, s_{x}, \rho_{x}\right]=\sqrt{\frac{\kappa_{x}+\frac{4}{3} \mu_{x}}{\rho_{x}}}+U_{V_{P}} ; x \in \mathcal{L}_{\mathcal{D}}\right\}
$$

with $\kappa_{x}=\kappa\left(q_{x}, s_{x}\right)$ and $\mu_{x}=\mu\left(q_{x}\right)$ being the bulk and shear moduli, respectively, of fluid filled facies ; and $U_{V_{P}}$ being $N\left(0,100^{2}\right)$.

The seismic S-wave velocity, $\left\{V_{S, x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$, is dependent on facies and density, and can be expressed as:

$$
\left\{\left[V_{S, x} \mid q_{x}, \rho_{x}\right]=\sqrt{\frac{\mu_{x}}{\rho_{x}}}+U_{V_{S}} ; x \in \mathcal{L}_{\mathcal{D}}\right\}
$$

with $\mu_{x}=\mu\left(q_{x}\right)$ being shear modulus as above ; and $U_{V_{S}}$ being $N\left(0,50^{2}\right)$.
The bulk and shear moduli are estimated as follows: For shale, both P-wave and S-wave velocities are assumed to be independent of the fluid filling. From measurements in wells, average values of these are estimated in Avseth et al(2001), $\bar{v}_{P}^{s}$ and $\bar{v}_{S}^{s}$. Likewise average value of density in shale is estimated, $\bar{\rho}^{s}$. By using $\mu^{s}=\bar{\rho}^{s}\left(\bar{v}_{S}^{s}\right)^{2}$ and $\kappa^{s}=\bar{\rho}^{s}\left(\bar{v}_{S}^{s}\right)^{2}-\frac{4}{3} \mu^{s}$ from Expression 6 and 7 the moduli for shale can be obtained. For sand, only brine sand observations are available in wells. From these, average velocities, $\bar{v}_{P}^{b s}$ and $\bar{v}_{S}^{b s}$, and average density $\bar{\rho}^{b s}$, for brine sand can be estimated. By using $\mu^{b s}=\bar{\rho}^{b s}\left(\bar{v}_{S}^{b s}\right)^{2}$ and $\kappa^{b s}=\bar{\rho}^{b s}\left(\bar{v}_{P}^{b s}\right)^{2}-\frac{4}{3} \mu^{b s}$ the moduli for brine sand can be obtained. For oil sand, however, no velocity measurements are available. The shear modulus is known to be independent of fluid filling, hence for oil sand one has $\mu^{o s}=\mu^{b s}$. The bulk modulus, $\kappa^{o s}$, is obtained from Gassmann's relation, see Mavko et al(1998), using bulk moduli of quartz, oil and brine equal to $36.8 \mathrm{GPa}, 1.1 \mathrm{GPa}$ and 2.8 GPa , respectively; and average sand porosity estimated from well measurements. For further details, see Avseth et al(2001). This provides:

$$
\kappa_{x}=\left\{\begin{array}{ll}
10.8 \mathrm{GPa} & q_{x}=\text { shale } \\
13.2 \mathrm{GPa} & q_{x}=\text { sand, } s_{x}=\text { brine } \\
10.5 \mathrm{GPa} & q_{x}=\text { sand, } s_{x}=\text { oil }
\end{array}\right.
$$

$$
\mu_{x}= \begin{cases}2.3 \mathrm{GPa} & q_{x}=\text { shale } \\ 4.2 \mathrm{GPa} & q_{x}=\text { sand }\end{cases}
$$

This defines the pdf's $f\left(v_{P_{x} x} \mid q_{x}, s_{x}, \rho_{x}\right)$ and $f\left(v_{S_{x} x} \mid q_{x}, \rho_{x}\right)$ to be Gaussian, and the stochastic dependencies are represented by single arrows in Figure 4 .

This defines the prior pdf of the reservoir variables given the seismic reflection times, denoted $f\left(r_{x} \mid t_{x}\right)$. Recall that the seismic reflection times to top reservoir are observed and hence can be conditioned to. In Figure 4, the model is represented as a graph with all dependencies represented by arrows. Note that the graph also indicates several conditional independencies which simplifies the model. The prior model can be expressed as:

$$
\begin{aligned}
f\left(r_{x} \mid t_{x}\right)= & f\left(q_{x}, s_{x}, \phi_{x}, \rho_{x}, v_{P_{x} x}, v_{S_{x} x} \mid t_{x}\right) \\
= & f\left(v_{S_{x} x} \mid q_{x}, \rho_{x}\right) \cdot f\left(v_{P_{x} x} \mid q_{x}, s_{x}, \rho_{x}\right) \cdot \\
& f\left(\rho_{x} \mid q_{x}, s_{x}, \phi_{x}\right) \cdot f\left(\phi_{x} \mid q_{x}\right) \cdot f\left(s_{x} \mid t_{x}\right) \cdot f\left(q_{x}\right)
\end{aligned}
$$

# Likelihood model 

The AVO attributes extracted from pre-stack seismic data, $d_{s, x}=\left(a_{x}^{o}, b_{x}^{o}\right)$, is collected on the grid $\mathcal{L}_{\mathcal{D}}$ covering $\mathcal{D}$. The likelihood model is based on Zoeppritz equations and approximations given in Shuey(1985) and Sheriff and Geldart(1995). For arbitrary $\left\{x \in \mathcal{L}_{\mathcal{D}}\right\}$ it is defined by

$$
\left[D_{s, x} \mid \rho_{x}, v_{P_{x} x}, v_{S_{x} x}, \sigma r\right]=\mu_{D_{s, x}}+U_{D_{s, x}}
$$

with

$$
\mu_{D_{s, x}}=\left[\begin{array}{c}
\mu_{A_{x}^{o}} \mid \cdot \\
\mu_{B_{x}^{o}} \mid \cdot
\end{array}\right]=\left[\begin{array}{c}
2 \frac{\Delta\left(v_{P_{x} x} \rho_{x}\right)}{\left(v_{P_{x} x} \rho_{x}\right)} \\
2 \frac{\Delta v_{P_{x} x}}{v_{P_{x} x}}+2\left(\frac{v_{S_{x} x}}{v_{P_{x} x}}+2 \frac{\Delta v_{S_{x} x}}{v_{S_{x} x}}\right)
\end{array}\right]
$$

with $\Delta \nu=\nu_{x}-\nu_{x}^{c}$ and $\overline{\nu_{x}}=\frac{1}{2}\left(\nu_{x}+\nu_{x}^{c}\right), \nu_{x}$ being either $\rho_{x}, v_{P_{x} x}, v_{S_{x} x}$ or $v_{P_{x} x} \rho_{x}$, and index $c$ indicating the corresponding cap rock characteristics. Note that this dependence is defined locationwise on $\mathcal{L}_{\mathcal{D}}$, hence without spatial dependence. Further $U_{D_{s, x}}$ is $\mathcal{N}_{2}\left(0, \Sigma_{A^{o}, B^{o}}\right)$; being a centered two dimensional Gaussian random variable with

$$
\Sigma_{A^{o}, B^{o}}=\left[\begin{array}{cc}
0.01 & -0.02 \\
-0.02 & 0.09
\end{array}\right]
$$

This covariance matrix is obtained by using calibration data from wells along the lines of the procedure used in Avseth et al(2001). This defines the likelihood model $f\left(a_{x}^{o}, b_{x}^{o} \mid \rho_{x}, v_{P_{x} x}, v_{S_{x} x}, c r\right)$. The stochastic dependencies are represented as single arrows in Figure 4. In Figure 6, samples of the AVO attributes based on the prior and likelihood models, as a function of lithofacies and fluid filling, is presented. Note how these samples covers the observed AVO attributes, although with larger uncertainty due to limited prior understanding.

The well observations $d_{w}=\left(q^{o}, s^{o}\right)$ consist of exact observations of facies and fluid in the four well locations. These are assumed to be representative of the entire grid unit which the well penetrates. The likelihood model is defined by:

$$
\begin{aligned}
& {\left[Q^{o} \mid q_{x}\right]=A_{w} q_{x}} \\
& {\left[S^{o} \mid s_{x}\right]=A_{w} s_{x}}
\end{aligned}
$$

with $Q^{o}$ and $S^{o}$ being four-dimensional vectors containing the well observations; and $A_{w}$ being a matrix identifying the well penetrations in $\mathcal{L}_{\mathcal{D}}$. One could imagine to introduce an error term in these relations to account for interpretation error and varying scales in well and seismic observations. This will cause only minor changes in the sampling algorithm. This defines the likelihood models $f\left(q^{o} \mid q_{x}\right)$ and $f\left(s^{o} \mid s_{x}\right)$ as Dirac pdf's. This deterministic dependence is represented by a double arrow in Figure 4.

# Posterior model 

Focus of the study is on the posterior model for the reservoir variables, $R_{x}$, and on $\left(Q_{x}, S_{x}\right)$ in particular, after conditioning on the reservoir specific observations $\left(d_{s, x}, d_{w}, t_{x}, c r\right)$. That is:

$$
f\left(r_{x} \mid d_{s, x}, d_{w}, t_{x}, c r\right)=\text { const } \cdot f\left(d_{s, x} \mid r_{x}, c r\right) \cdot f\left(d_{w} \mid r_{x}\right) \cdot f\left(r_{x} \mid t_{x}\right)
$$

with const being the normalizing constant $f\left(d_{s, x}, d_{w} \mid t_{x}, c r\right)^{-1}$ which is not possible to calculate. The posterior pdf for $\left(Q_{x}, S_{x}\right)$ can be obtained by integrating out the other reservoir variables of less interest.

The best predictor will usually be based on a locationwise maximum aposteriori (MAP) criterion:

$$
\left\{\left(\hat{q}_{x}, \hat{s}_{x}\right)=\operatorname{argmax}_{q_{x}, s_{x}}\left(f\left(q_{x}, s_{x} \mid d_{s, x}, d_{w}, t_{x}, c r\right)\right) ; x \in \mathcal{L}_{\mathcal{D}}\right\}
$$

and associated prediction uncertainties can also be quantified as for example misclassification rates. Moreover, probability maps of the occurence of (sand, oil) in each location are defined by:

$$
\left\{\operatorname{Prob}\left(q_{x}=\operatorname{sand} \cap s_{x}=o i l\right)=f\left(\operatorname{sand}, o i l \mid d_{s, x}, d_{w}, t_{x}, \sigma r\right) ; x \in \mathcal{L}_{\mathcal{D}}\right\}
$$

The posterior model for the reservoir variables, $R_{x}$, is not analytically tractable and can only be explored by sampling. A suitable decomposition of this posterior pdf for sampling purposes can be found from the graph in Figure 4:

$$
\begin{aligned}
& f\left(r_{x} \mid d_{s, x}, d_{w}, t_{x}, \sigma r\right)= \\
& f\left(q_{x}, s_{x}, \phi_{x}, \rho_{x}, v_{P, x}, v_{S, x} \mid a_{x}^{o}, b_{x}^{o}, q^{o}, s^{o}, t_{x}, \sigma r\right)= \\
& \text { const } \cdot f\left(a_{x}^{o}, b_{x}^{o} \mid \rho_{x}, v_{P, x}, v_{S, x}, \sigma r\right) \cdot f\left(s^{o} \mid s_{x}\right) \cdot f\left(q^{o} \mid q_{x}\right) \cdot f\left(v_{S, x} \mid q_{x}, \rho_{x}\right) \cdot \\
& f\left(v_{P, x} \mid q_{x}, s_{x}, \rho_{x}\right) \cdot f\left(\rho_{x} \mid q_{x}, s_{x}, \phi_{x}\right) \cdot f\left(\phi_{x} \mid q_{x}\right) \cdot f\left(s_{x} \mid t_{x}\right) \cdot f\left(q_{x}\right)
\end{aligned}
$$

The many conditional independencies that can be read out of the graph is used in order to define Expression 17. Note further that all terms except the two last ones are of Gaussian type. The last ones are defined as Markov random fields. Samples of $\left\{R_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$ from the posterior pdf $f\left(r_{x} \mid d_{s, x}, d_{w}, t_{x}, \sigma r\right)$ can be obtained by Markov chain Monte Carlo(McMC) sampling, see Appendix B. This sampling algorithm is iterative and convergence to a sample of the required pdf can only be proven as the number of iterations goes towards infinity. The algorithm has the following steps:

1. Initiate:

- Arbitrary $r_{x}$, such that $f\left(r_{x} \mid \cdot\right)>0$

2. Iterate:

- Propose: $r_{x}^{\prime}$ from $p\left(r_{x}^{\prime} \mid r_{x}\right)$
- Compute: $\alpha=\min \left(1, \frac{f\left(r_{x}^{\prime} \mid \cdot\right) \cdot p\left(r_{x} \mid r_{x}^{\prime}\right)}{f\left(r_{x} \mid \cdot\right) \cdot p\left(r_{x}^{\prime} \mid r_{x}\right)}\right)$
- Update: $r_{x}=r_{x}^{\prime}$ with probability $\alpha$, else: no change.
with $f\left(r_{x} \mid \cdot\right)$ being the posterior pdf of interest. In the present case $p\left(r_{x}^{\prime} \mid r_{x}\right)$ is a pdf such that one grid node in $\mathcal{L}_{\mathcal{D}}$ is sampled at random among all grid nodes. In this node, $x_{i} \in \mathcal{L}_{\mathcal{D}}, p\left(r_{x_{i}}^{\prime} \mid r_{x_{i}}\right)$ is uniform over the four possible outcomes of $\left(q_{x_{i}}^{\prime}, s_{x_{i}}^{\prime}\right)$ and the remainder of $\left(q_{x}, s_{x}\right)$ are left unchanged. This defines the proposal $r_{x_{i}}^{\prime}$ as independent of the old state. Note that according to

this updating $p\left(r_{x}^{\prime} \mid r_{x}\right)=p\left(r_{x} \mid r_{x}^{\prime}\right)$ and hence it cancels from the computation of the acceptance probability $\alpha$ and so does the non-calculatable constant in the posterior. The posterior pdf in Expression 17 must be used in the computation of $\alpha$, but due to local dependence in the prior Markov random fields of $f\left(q_{x}\right)$ and $f\left(s_{x} \mid t_{x}\right)$ and in the likelihood models, most terms cancels. Hence the algorithm is feasible from a computational point of view. The rate of convergence is hard to determine, but justification of the convergence will be presented for the actual case in the next section.

Based on the McMC algorithm a set of samples from the posterior pdf $f\left(q_{x}, s_{x} \mid a_{x}^{o}, b_{x}^{o}, q^{o}, s^{o}, t_{x}, \sigma r\right)$ can be obtained: $\left\{\left(q_{x}, s_{x}\right)^{i} ; i=1, \ldots, N\right\}$. This set of samples represents the uncertainty in the posterior model. Moreover, estimates of the best predictor, see Expression 15, is obtained by in any location to take the pair of $\left(q_{x}, s_{x}\right)$ which occur most frequently in the sample. Likewise estimates of the probability map, see Expression 16, is obtained by in any location to count the proportion of samples with $\left(q_{x}=\right.$ sand, $\left.s_{x}=o i l\right)$.

# Results with discussion 

Based on the model and parameter assumptions specified in the previous sections, the posterior pdf of real interest $f\left(q_{x}, s_{x} \mid a_{x}^{o}, b_{x}^{o}, q^{o}, s^{o}, t_{x}, \sigma r\right)$ is defined through

$$
f\left(q_{x}, s_{x}, \phi_{x}, \rho_{x}, v_{P, x}, v_{S_{x} x} \mid a_{x}^{o}, b_{x}^{o}, q^{o}, s^{o}, t_{x}, \sigma r\right)
$$

By applying the McMC algorithm described, samples from this posterior pdf can be obtained.

The convergence of the McMC algorithm is evaluated by monitoring the sand and oil fraction respectively in test runs with extreme initial states. In Figure 7 the initial states are all sand, shale, oil and brine. After 1000 sweeps of the McMC algorithm the influence of the initial state seems to have almost vanished and convergence can be assumed. Note that one sweep corresponds to $(245 \times 506)$ iterations, hence each grid node is expected to be visited once in each sweep. After this burn-in period samples can be assumed to be approximately from Expression 18. In the final runs an initial state with high probability in the posterior pdf is chosen.

In Figure 8 samples of $\left(Q_{x}, S_{x}\right)$ from $f\left(q_{x}, s_{x} \mid a_{x}^{o}, b_{x}^{o}, q^{o}, s^{o}, t_{x}, \sigma r\right)$ are presented in combined displays. These samples are generated by independent

runs of the McMC algorithm. The black areas represent shale, while white and grey represent sand with brine and oil respectively. Each sample has geometric characteristics according to the prior beliefs conditioned to the reservoir specific observations. Hence these are possible realizations of the reservoir. Moreover, the collection of samples represent the uncertainty in the posterior model. This sampling can be done since the stochastic model is fully specified. Note that there is some smoothness in the facies distribution. The model assumptions on the Markov random field have influence on this, and this model may be refined along the lines of Tjelmeland and Besag(1998) and Caers(1999). Note further how the conditioning of fluid filling on seismic reflection times forces the oil to be in relative shallow areas. Lastly, recall that the conditioning is made both on well observations and seismic AVO data.

These samples from the posterior are obtained by sampling the full vector $\left(Q_{x}, S_{x}, \Phi_{x}, \rho_{x}, V_{P, x}, V_{S, x}\right)$ from Expression 18 and only retaining the $\left(Q_{x}, S_{x}\right)$ entries. One may also inspect the posterior samples for the other reservoir variables. In Figure 9, estimated histograms from the prior and posterior model for these variables are presented. These are based on 10000 samples from both prior and posterior model. The bimodalities are caused by facies variations. Note that the maximum mode is higher, and variability less, for the posterior histograms than for the prior ones. This is primarily caused by changes in the facies proportions, while the other reservoir variables, conditioned on facies type, are relatively stable. The relative uncertainty in the prior model and the dependence through the likelihood model will determine whether a reservoir variable is stable or not.

In Figure 10 the MAP-prediction defined in Expression 15 is estimated. This can be interpreted as the most probable outcome in each location, and hence in some sense the best predictor of the facies and saturation characteristics. Note that this prediction appears as much smoother than the samples presented in Figure 8. The estimate is based on a set of samples, and in each grid unit the most frequently occuring facies and saturation state in the set is retained. Figure 10 corresponds to Figure 28(left) in Avseth et al(2001). The spatial prior model and the conditioning on seismic reflection times tend to provide a smoother prediction for both lithofacies and fluid filling. Recall that the spatial prior model for lithofacies includes no trends, hence the large shale sheet in the south-western corner is caused by the conditioning on seismic AVO data. The same holds for the sand being

dominant in what is interpreted as a feeder-channel in Avseth et al(2001). Note further how the oil tends to accumulate in the shallow areas. This is caused by conditioning on seismic reflection times in the prior.

In Figure 11 a probability map for oil-bearing-sand as defined in Expression 16 is estimated. This can be interpreted as the probability of having the favorable (sand, oil) combination at a given location. The estimate is based on a set of samples, and in each grid unit the relative occurence of the outcome (sand, oil) in the set is computed. Figure 11 corresponds to Figure 28(right) in Avseth et al(2001).

# Conclusions 

In Avseth et al(2001) a thorough analysis of interdependence between reservoir characteristics and seismic AVO attributes is presented. A procedure for predicting the former from measurements of the latter is defined. The current paper defines an extended, spatial, stochastic model for this purpose. The model is defined on a graph in a Bayesian setting. The prior model is based on general reservoir information, and includes spatial continuity for both lithofacies and fluid filling. Moreover, fluid filling is dependent on depth, represented by seismic reflection times to top reservoir. The posterior model, conditioned to observations in wells and seismic AVO data is defined. Sampling from this posterior model is done by a McMC algorithm.

It is demonstrated that a formal stochastic model, including highly nonlinear rock physics relations, can be used to integrate well observations and seismic AVO data. Based on this model uncertainty statements about the reservoir characteristics can be made.

The choice of prior model has relatively large impact on the results since the wells are few and the seismic data relatively uncertain. Hence the prior model might be refined along the lines of Tjelmeland and Besag(1998) and Caers(1999). They use a more informative spatial prior which favor certain geometric properties for the sand/shale distribution. The model should also be extended to 3D, and it should then include the procedure for Bayesian AVO inversion presented in Buland and Omre(2000).

## Acknowledgements

The study was financially supported by the URE initiative at NTNU, the Stanford Rock Physics Project and from the Stichting Foundation, Schlumberger. Jo Eidsvik is a PhD student funded by the Norwegian Research Counsil. The authors are grateful to Norsk Hydro and Statoil for providing the data.

# Appendix 

## A. Markov random fields

Consider a Markov random field $\left\{W_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$ with binary sample space $W_{x} \in\{0,1\}$; and reference $x$ being on a grid $\mathcal{L}_{\mathcal{D}}$ covering $\mathcal{D} \subset \mathbf{R}^{2}$. Let the neighborhood related to reference $y \in \mathcal{L}_{\mathcal{D}}$ be defined by $\mathcal{N}_{y}$, see Figure 12. The Markov assumption entails:
$\operatorname{Prob}\left(W_{y}=w_{y} \mid W_{x}=w_{x} ; x \in \mathcal{L}_{\mathcal{D}} ; x \neq y\right)=\operatorname{Prob}\left(W_{y}=w_{y} \mid W_{x}=w_{x} ; x \in \mathcal{N}_{y}\right)$
hence the probability of $t$ occuring in reference location $y$ given the rest of the field is only dependent on the states in the neighborhood $\mathcal{N}_{y}$ around $y$. Note that the definition of Markov random fields relies on local definitions of conditional distributions.

Consider a Gibbs random field $\left\{W_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$ with $W_{x}$ and $x$ defined as above. The Gibbs assumption entails:

$$
\operatorname{Prob}(W=w)=\operatorname{Prob}\left(W_{x}=w_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right)=\text { const } \cdot \exp \left(\Sigma_{c \in \mathcal{C}} \nu_{c}(w)\right)
$$

with $\nu_{c}(w)$ being functions of $w$-entries belonging to the clique $c$ only. A clique is a set of references in a local closed domain. The set $\mathcal{C}$ contains all cliques defined over $\mathcal{L}_{\mathcal{D}}$. Hence Gibbs random fields are defined through the joint probability of all $\left\{W_{x} ; x \in \mathcal{L}_{\mathcal{D}}\right\}$, and this probability can be expressed as a product of terms depending on $w$-entries in local cliques only.

The Hammersley-Clifford theorem, Besag(1974), states that a Markov random field exists if and only if a Gibbs random field exists. Moreover, the Gibbs cliques are defined as the largest set of references which belong to eachothers Markov neighborhoods, see Figure 13. Consequently there exists a dualism between Markov and Gibbs random fields, and one can freely choose which form to use. The former specifies the random field through local conditional distributions while the latter specifies it through the joint distribution.

# B. Markov chain Monte Carlo(McMC) sampling 

Consider a traditional stochastic Markov process, $\left\{X_{n} ; n=0,1, \ldots\right\}$ with discrete, finite state space $X_{n} \in \Omega_{X}$. The stationary Markov assumption defines the one step transition probabilities:

$$
\begin{aligned}
\operatorname{Prob}\left(X_{n}=x \mid X_{n-1}=x_{-1}, \ldots, X_{0}=x_{-n}\right) & =\operatorname{Prob}\left(X_{n}=x \mid X_{n-1}=x_{-1}\right) \\
& =P_{x_{-1}, x}^{X}
\end{aligned}
$$

for all $x_{-1}, x \in \Omega_{X}$ and all $n$. Hence the probability for occurence is only dependent on the previous step. Under relatively weak assumptions, primarily that the entire sample space $\Omega_{X}$ is spanned, does a limiting distribution $\left\{\pi_{x} ; x \in \Omega_{X}\right\}$ exist:

$$
\pi_{x}=\lim _{n \rightarrow \infty} \operatorname{Prob}\left(X_{n}=x \mid X_{0}=x_{0}\right)
$$

Note that this limiting distribution is independent on the initial state of the process. The convergence rate is hard to evaluate though. In traditional Markov process theory the transition probabilities $\left\{P_{x_{-1}, x}^{X} ; x_{-1}, x \in \Omega_{X}\right\}$ are specified, and the challenge is to determine the limiting distribution $\left\{\pi_{x} ; x \in \Omega_{X}\right\}$, and possibly its convergence rate.

The idea of the McMC sampling algorithm rests on $\left\{\pi_{x} ; x \in \Omega_{X}\right\}$ being the known probability distribution to be sampled from. The challenge is to identify a set of transition probabilities $\left\{P_{x_{-1}, x}^{X} ; x_{-1}, x \in \Omega_{X}\right\}$ having

$\left\{\pi_{x} ; x \in \Omega_{X}\right\}$ as its limiting distribution. Then the McMC algorithm can be initiated at an arbitrary state $x_{0} \in \Omega_{X}$ and by running the Markov process with these transition probabilities convergence towards the required probability distribution will be ensured. The rate of convergence will depend on the procedure for generating the initial state and on which, among many eligible, set of transition probabilities it is based.

In Hastings(1970) a procedure for selecting these transition probabilities is prescribed, the so called Metropolis-Hastings algorithm. It relies on the decomposition:

$$
P_{x_{-1}, x}^{X}= \begin{cases}\alpha_{x_{-1}, x} P_{x_{-1}, x}^{Y} & x \in \Omega_{X} ; x \neq x_{-1} \\ 1-\Sigma_{x^{\prime} \in \Omega_{X} ; x^{\prime} \neq x_{-1}} \alpha_{x_{-1}, x^{\prime}} P_{x_{-1}, x^{\prime}}^{Y} & x \in \Omega_{X} ; x=x_{-1}\end{cases}
$$

with $\left\{Y_{n} ; n=0,1, \ldots\right\}$ being a stationary Markov process on the same state space as $X_{n}$, i.e. $Y_{n} \in \Omega_{X}$, and arbitrary chosen transition probabilities $\left\{P_{y_{-1}, y}^{Y} ; y_{-1}, y \in \Omega_{X}\right\}$ such that the limiting distribution does exist. By defining

$$
\alpha_{x_{-1}, x}=\min \left(1, \frac{\pi_{x} P_{x, x_{-1}}^{Y}}{\pi_{x_{-1}} P_{x_{-1}, x}^{Y}}\right)
$$

it can be proved that the Markov process $\left\{X_{n} ; n=0,1, \ldots\right\}$ with $X_{n} \in \Omega_{X}$ will have a limiting distribution $\left\{\pi_{x} ; x \in \Omega_{X}\right\}$ as required.

# Figure Captions 

Figure 1: Seismic reflection times, $t_{x}(\mathrm{msec})$, to the horizon.

Figure 2: Zero offset reflection, $a_{x}^{o}$ (top left), AVO gradient, $b_{x}^{o}$ (top right), and plot of $a_{x}^{o}$ versus $b_{x}^{o}$ (bottom).

Figure 3: Well observations. Shale ( $\diamond$ ), oil filled sand ( $\circ$ ) and brine filled sand ( $\square$ ).

Figure 4: Model graph. Single arrows indicate a stochastic relationship, double arrows a deterministic relationship.

Figure 5: Probability of oil as a function of reflection time and the number of neighbors identical to the center variable. The parameters are $h_{l}=2075 \mathrm{msec}$ with $\eta_{h}=0.05$ (top) and $\eta_{h}=0.01$ (bottom). Four equal neighbors(-), two equal neighbors(*) and zero equal neighbors(- -).

Figure 6: Samples of AVO attributes from prior and likelihood model. Shale ( $\diamond$ ), oil filled sand ( $\circ$ ) and brine filled sand ( $\square$ ). The observed AVO attributes(*).

Figure 7: Monitoring convergence; fraction of pixels with $s_{x}=$ oil (thin line) and fraction of pixels with $q_{x}=$ sand (thick line) as function of sweeps. Two runs initiated by all (sand, oil) and all (shale, brine), respectively.

Figure 8: Posterior samples; shale(black), brine sand(white) and oil sand(grey).

Figure 9: Histograms of samples from prior model(white) and posterior model(black) for certain combinations of reservoir variables ; $\phi$ (top left),

$\rho($ top right), $v_{P}$ (bottom left) and $v_{S}$ (bottom right).

Figure 10: Estimated MAP prediction; shale(black), brine sand(white) and oil sand(grey).

Figure 11: Estimated probability map for (sand, oil).

Figure 12: Example of second order neighborhood around reference location $y$.

Figure 13: Neighborhoods(top) of first(left) and second(right) order. Corresponding maximum cliques(bottom).

![img-1.jpeg](img-1.jpeg)

Figure 1:

![img-2.jpeg](img-2.jpeg)

Figure 2:

![img-3.jpeg](img-3.jpeg)

Figure 3:

![img-4.jpeg](img-4.jpeg)

Figure 4:

![img-5.jpeg](img-5.jpeg)

Figure 5:

![img-6.jpeg](img-6.jpeg)

Figure 6:

![img-7.jpeg](img-7.jpeg)

Figure 7:

![img-8.jpeg](img-8.jpeg)

Figure 8:

![img-9.jpeg](img-9.jpeg)

Figure 9:

![img-10.jpeg](img-10.jpeg)

Figure 10:

![img-11.jpeg](img-11.jpeg)

Figure 11:

![img-12.jpeg](img-12.jpeg)

Figure 12:

![img-13.jpeg](img-13.jpeg)

Figure 13: