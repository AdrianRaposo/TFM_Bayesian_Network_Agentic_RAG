# Maintenance decision model for steel bridges 

## Citation for published version (APA):

Attema, T., Kosgodagan, A., Morales-Napoles, O., \& Maljaars, J. (2017). Maintenance decision model for steel bridges: a case in the Netherlands. Structure and Infrastructure Engineering, 13(2), 242-253.
https://doi.org/10.1080/15732479.2016.1158194

## Document license:

TAVERNE

DOI:
10.1080/15732479.2016.1158194

Document status and date:
Published: 01/02/2017

## Document Version:

Publisher's PDF, also known as Version of Record (includes final page, issue and volume numbers)

## Please check the document version of this publication:

- A submitted manuscript is the version of the article upon submission and before peer-review. There can be important differences between the submitted version and the official published version of record. People interested in the research are advised to contact the author for the final version of the publication, or visit the DOI to the publisher's website.
- The final author version and the galley proof are versions of the publication after peer review.
- The final published version features the final layout of the paper including the volume, issue and page numbers.
Link to publication


## General rights

Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.

- Users may download and print one copy of any publication from the public portal for the purpose of private study or research.
- You may not further distribute the material or use it for any profil-making activity or commercial gain
- You may freely distribute the URL identifying the publication in the public portal.

If the publication is distributed under the terms of Article 25fa of the Dutch Copyright Act, indicated by the "Taverne" license above, please follow below link for the End User Agreement:
www.tue.nl/taverne

## Take down policy

If you believe that this document breaches copyright please contact us at:
openaccess@tue.nl
providing details and we will investigate your claim.

# Structure and Infrastructure Engineering 

Maintenance, Management, Life-Cycle Design and Performance

## Maintenance decision model for steel bridges: a case in the Netherlands

Thomas Attema, Alex Kosgodagan Acharige, Oswaldo Morales-Nápoles \& Johan Maljaars

To cite this article: Thomas Attema, Alex Kosgodagan Acharige, Oswaldo Morales-Nápoles \& Johan Maljaars (2017) Maintenance decision model for steel bridges: a case in the Netherlands, Structure and Infrastructure Engineering, 13:2, 242-253, DOI: 10.1080/15732479.2016.1158194

To link to this article: http://dx.doi.org/10.1080/15732479.2016.1158194

Published online: 26 Apr 2016.

Submit your article to this journal

Article views: 81

View related articles

View Crossmark data

Full Terms \& Conditions of access and use can be found at http://www.tandfonline.com/action/journalInformation?journalCode=nsie20

# Maintenance decision model for steel bridges: a case in the Netherlands 

Thomas Attema ${ }^{a}$, Alex Kosgodagan Acharige ${ }^{a, b}$, Oswaldo Morales-Nápoles ${ }^{a, c}$ and Johan Maljaars ${ }^{a, d}$<br>${ }^{a}$ Netherlands Organization for Applied Scientific Research (TNO), The Hague, The Netherlands; ${ }^{\text {b }}$ Institut de Recherche en Communications et Cyberntique de Nantes (IRCCyN), École des Mines de Nantes, Nantes, France; ${ }^{c}$ Faculty of Civil Engineering and Geosciences, TU Delft, Delft, The Netherlands; ${ }^{d}$ Department of the Built Environment, Eindhoven University of Technology, TU Eindhoven, Eindhoven, The Netherlands


#### Abstract

A probabilistic model is developed to investigate the crack growth development in welded details of orthotropic bridge decks. Bridge decks may contain many of these vulnerable details and bridge reliability cannot always be guaranteed upon the attainment of a critical crack. Therefore, insight into the crack growth development is crucial in guaranteeing bridge reliability and scheduling efficient maintenance schemes. The probabilistic nature of the crack growth development model and the dependence of this model on many interdependent random variables result in significant uncertainties regarding model outcome. To reduce some of these uncertainties, the probabilistic model is combined with a monitoring system installed on a part of the bridge. In addition, a Bayesian network is used to determine the dependence structure between the different details (monitored and non-monitored) of the bridge. This dependence structure enables us to make more accurate crack growth predictions for all details of the bridge while monitoring only a limited number of those details and updating the remaining uncertainties.


## ARTICLE HISTORY

Received 6 August 2015
Revised 11 January 2016
Accepted 12 January 2016
Published online
26 April 2016

## KEYWORDS

Fatigue; bridge deck; monitoring; non-parametric Bayesian networks; linear elastic fracture mechanics

## 1. Introduction

Fatigue cracking is one of the main degradation mechanisms of steel bridges. It is the result of fluctuating stresses caused by the crossing of heavy vehicles. Especially, welded details in the deck structure are vulnerable to fatigue cracking (Maljaars, Kolstein, \& Van Dooren, 2012) because these details are directly loaded by passing wheels and because of the stress concentrations, initial notches and high residual stresses that are specific to welded deck structures (Pfeil, Battista, \& Mergulhão, 2005). Some critical welded details occur multiple times in a bridge deck, so that cracks can basically occur everywhere in the deck. On the other hand, distribution of loads to adjacent parts of the structure is often possible if a detail is weakened as a result of a fatigue crack. The latter implies that critical crack lengths - i.e. crack lengths at which failure can be assumed - are typically long (in the order of 400 mm or longer) and that crack growth rates of large cracks are typically low as compared to fatigue tests on single details. For these reasons, monitoring systems aimed at identifying fatigue cracks can be used to guarantee the safety of the bridge deck structure.

In recent years, monitoring systems based on acoustic emission have successfully been used to detect (fatigue) cracking, Grosse, McLaskey, Bachmaier, Glaser, and Krüger (2008), Holford, Davies, Pullin, and Carter (2001), Nair and Cai (2010). This type of system records the acousto-ultrasonic emissions generated by a growing crack, i.e. it listens to crack activity. Using
several sensors spread over a structure, it is possible to localise a fatigue crack by evaluating the duration of the wave propagation. Piezoelectric sensors can subsequently be used to determine the size of a localised crack. Finally, strain gauges can be used to accurately determine stress ranges in a certain detail. Such a system is successfully developed and installed by research organisation TNO in the orthotropic bridge deck of a motorway bridge in The Netherlands. The monitoring system is described in detail elsewhere, Pijpers, Pahlavan, Paulissen, Hakkesteegt, and Jansen (2013).

Although the costs of monitoring vary from bridge to bridge, it can be said that monitoring systems are in general expensive, especially if a large surface such as a bridge deck needs to be covered. Installation costs form a large portion of the total costs. According to Issa, Shabila, and Alhassan (2005), the installation time of a complete measurement system for bridges can potentially consume over $75 \%$ of the total testing time. Installation labour costs can approach well over $25 \%$ of the total system cost. But also maintenance costs and costs of data processing can be significant. For this reason, this research considers a system that monitors a small part of the bridge deck and uses the output of the system in order to provide an assessment of the general condition of the non-monitored part of the bridge deck.

The output provided by the monitoring system is used to probabilistically predict the remaining life of the structure. Apart from the output of the monitoring system (observations), this

![img-0.jpeg](img-0.jpeg)

Figure 1. Crack of concern.
prediction requires models. This paper describes the underlying models required for the assessment of the remaining lifetime of the bridge. The two models used in the assessment are:
(1) a physical fracture mechanics model to evaluate the crack growth rate,
(2) a non-parametric Bayesian network to update the crack growth and end-of-life prediction of the nonmonitored part of the bridge deck based on the observations of the monitored part.

Previous research has been devoted to incorporating monitoring data in the fatigue life prediction. For example, Deng, Li, and Ding (2014), Liu, Frangopol, and Kwon (2010) have considered monitoring of stress ranges and number of cycles. In other cases, the results of fatigue crack inspections have been used in order to assess the remaining life, e.g. Boutet, Hild, and Lefebvre (2013), Toft, Sørensen, Yalamas, and Baussaron (2013). Research in which the observations regarding crack size monitoring are considered and used for prediction of the remaining resistance or life span is less common in the literature. One of the main differences between inspections and monitoring from the point of view of the models required is that monitoring systems usually only cover a part of the structure. Hence, models that use the information obtained from the monitored part of a structure in the assessment of the non-monitored part are required. In this paper, a Bayesian network is used for this step.

Previous research (Maljaars \& Vrouwenvelder, 2014) shows that an inspection of one detail is of little use for the assessment of the remaining life of a non-monitored equal detail separated physically from the inspected detail. This holds even in case of inspections with high probability of detection. In the current case, however, the most heavily loaded detail of the bridge is monitored, being the detail near the expansion joint that experiences the largest dynamic load. Because the first fatigue cracks are expected in this region, information from this region may be
valuable for the assessment of non-monitored locations. This is explored in the current paper.

## 2. Description of the detail

The main focus in this research is a type of crack that is observed in orthotropic steel bridge decks. The crack starts from the root of the weld between a trapezoidal stringer and the deck plate usually at the junction with a crossbeam - and subsequently grows along the weld line (Figure 1). This type of detail occurs multiple times in a bridge deck. Per crossbeam the number of heavily loaded details - i.e. details directly below the wheel tracks is approximately equal to 6 . Depending on the span of the bridge, the total number of heavily loaded details varies between 10 and 100 .

Figure 1 displays the type of crack considered in this paper. The crack shapes considered are a semi-elliptical surface crack and a through-thickness crack, indicated in Figures 1(c) and (d), respectively. If not repaired, a surface crack will grow and form a through-thickness crack after a certain number of cycles. The dimensions of the surface crack are indicated with depth $a$ and semi-length $c$. Those of the through-thickness crack are the semi-length on the bottom side $c$, the semi-width on the top side $d$ and the effective height $a$, see Figure 1.

The type of crack in Figure 1 is considered as being a serious threat to the traffic safety, because a wheel load rolling on one side of the crack may cause a level difference between the two parts of the deck plate separated by the crack, implying that the vehicle is uncontrollable. In addition, it is difficult to detect the type of crack because it is covered by the surface finish on the top side and by the stringer on the bottom side. Moreover, the type of crack is observed in many existing bridges in various countries.

Variables 1-4 in Table 1 provide the relevant geometric dimensions of the detail, here $a_{0}$ and $c_{0}$ are the initial defect dimension at the weld root prior to fatigue loading. Because $a_{0}$ and $c_{0}$ are

Table 1. Model variables.


${ }^{a}$ Equal to $2: 5$ for a deck plate without surface finish.
correlated, a distribution is provided for the ratio between $a_{0}$ and $c_{0}$. For each variable, the distribution function is provided together with the average, $\mu$, and the coefficient of variation, $V$. Moreover, a dependency structure between the various locations of this type of detail in one bridge is imposed. This dependency structure exists since these different details are exposed to similar conditions and it is quantified by the rank correlation, $r$, between variables in different sections of the bridge. As will be seen in Section 4.1, the class of Bayesian networks (BNs) used in this research are parameterised by rank correlation coefficients. For our application, in particular, these are the correlations between variables in the monitored and non-monitored sections of the bridge. All the variables in Table 1 are based on those presented in Maljaars and Vrouwenvelder (2014), where a fracture mechanics model of a different detail in the same type of orthotropic deck structure is provided. However, some modifications accounting for the specific detail and models are considered in this paper. For details regarding the original quantification of the model, the reader is referred to Maljaars and Vrouwenvelder (2014).

## 3. Linear elastic fracture mechanics model for crack growth development in orthotropic steel bridge decks

Linear elastic fracture mechanics (LEFM) theory is used to determine the crack growth and crack size as a function of stress ranges and the number of cycles, i.e. the number of stress fluctuations. The LEFM theory and its application to fatigue are explained elsewhere (Anderson, 2005), and in this paper, only the basic equation and principles are explained. The basic parameter used in LEFM is the stress intensity factor, $K$, which is a measure for the stress state in the direct vicinity of a crack tip. It has a theoretical basis and can be determined based on the crack depth, $a$, the geometry of the joint and the far-field stress of the unflawed joint, $\sigma$. In fact,

$$
K=Y \sigma \sqrt{\pi a}
$$

where $Y$ is the geometric correction factor accounting for the crack shape, the geometry of the joint and the type of loading (bending or membrane stress). In Section 3.1, the stress intensity factor is provided for semi-elliptical surface cracks up to the attainment of a through-thickness crack (Figure 1(d)). The stress intensity factor for through-thickness cracks that grow in width direction is provided in Section 3.2.

The stress intensity factors at the maximum and minimum stresses of a far-field stress cycle are $K_{\max }$ and $K_{\min }$, respectively, the stress intensity factor range is $\Delta K=K_{\max }-K_{\min }$ and the stress intensity ratio is $R=K_{\min } / K_{\max }$. In a fatigue analysis, the crack extension, $a$, per cycle, $N$, can be determined as a function of the stress intensity factor range and the stress ratio via a material-dependent crack growth curve:

$$
\frac{\mathrm{d} a}{\mathrm{~d} N}=f(\Delta K, R, \text { material properties })
$$

Similar expressions exist for the crack extension in length direction, $\mathrm{d} c / \mathrm{d} N$ or $\mathrm{d} d / \mathrm{d} N$, where dimensions $a, c$ and $d$ are indicated in Figure 1. The crack growth curve used here follows the framework proposed in Forman and Mettu (1992). The governing material properties determining the crack growth in Equation (2) are given by variables 5-10 in Table 1. These variables are uncorrelated except for $A$ and $m$, which are correlated as a result of the mathematical description of the crack growth curve. In agreement with the most probabilistic fracture mechanics studies, this is considered by applying a deterministic value for $m$ and a distribution for $A$ that reflects the variability of the crack growth curve.

### 3.1. Model for a semi-elliptical surface crack

Parametric expressions, for the geometric correction factor $Y$ in Equation (1), are provided in the literature and standards for a number of simple geometries such as a crack starting from a weld toe of a straight weld. For the type of detail indicated in Figure 1, however, such a parametric expression does not exist. An approximate expression for $K$ has been derived, which consists of an

![img-1.jpeg](img-1.jpeg)

Figure 2. Stress gradient correction factor $M_{s c}$.
extension of a preliminary expression developed in Maljaars et al. (2012). The model uses the parametric expression for a semielliptical crack, $M_{s c}$, according to Newman and Raju (1984) and a correction for weld toe cracks, $M_{k}$, according to Maddox and Andrews (1990) as a basis. A further correction, $M_{g}$, has been applied to account for the difference between the weld toe flank angle of $45^{\circ}$ adopted in Maddox and Andrews (1990) and the angle of $65^{\circ}$ that has been observed in macros of the weld root geometry of the detail indicated in Figure 1.

The factors $M_{s c}, M_{k}$ and $M_{g}$ are different for the deepest point ( $a$-direction) and the surface point ( $c$-direction) of the crack, indicated here by $M_{s c, x}, M_{k, x}$ and $M_{g, x}$ where $x$ is either $a$ or $c$. Each of the factors is a function of the crack dept $a$, the aspect ratio $a / c$ and the geometric dimensions in Table 1. In addition, the model accounts for the stress gradient towards the crossbeam by considering the findings in Bueckner (1958) that the energy needed for crack extension in a body can be evaluated by projecting the stress field from the uncracked body onto the crack plane.

The hot-spot stress of the uncracked geometry was determined using the finite element method for both a rolling wheel and a wheel applied vertically above the crossbeam. The ratio between this hot-spot stress and the far-field stress of the wheel, $M_{s c}$, is then a function of the semi-crack length, $c$, the stress concentration factor, $S C F$, and the length of the stress concentration,
$l_{s c}$, see Figure 2. The distributions of these variables, SCF and $l_{s c}$, are given by variables 11 and 12 of Table 1. Altogether for semi-elliptical surface cracks, the geometric correction factor $Y$ of Equation (2) is equal to:

$$
Y_{x}=M_{s c, x} M_{k, x} M_{g, x} M_{s c}
$$

The results of this crack growth model are compared with constant amplitude tests carried out on configurations with the detail of Figure 1 in Jong (2007). The tests were carried out with a vertically loaded wheel on an orthotropic deck without surface finish. Based on these test, Kolstein (2007) reports an average hot-spot fatigue reference strength at $2 \times 10^{6}$ cycles of $\sigma_{c}=211 \mathrm{MPa}$ corresponding to the criterion of the first visual observation of a crack on the top side. This first observed crack had a semi-length of $d=12 \mathrm{~mm}$. The crack growth model described above with the average dimensions and the average crack growth variables 1-12 of Table 1 was used to simulate the number of cycles from an initial defect up to a surface breaking crack (i.e. $a=T$ ). The stress range required to cause failure at $2 \times 10^{6}$ cycles with this model was equal to $\sigma_{c}=210 \mathrm{MPa}$. Hence, the constant amplitude fatigue tests agree with the model for a semi-elliptical surface crack in the detail of Figure 1.

### 3.2. Model for through-thickness crack

Some of the tests in Jong (2007) were continued after the first observation of a through-thickness crack up to the attainment of a relatively large crack. The crack length on the tip side, $2 d$, was measured at certain intervals and is plotted as a function of the number of cycles in Figure 3(a) for six tests with a force range of $\Delta F=64 \mathrm{kN}$ and 10 tests with a force range of $\Delta F$ between 72 and 75 kN . The figure shows that the crack growth rate remains fairly constant. This would imply that the crack growth rate $\mathrm{d} d / \mathrm{d} N$ is independent of the actual semi-crack length, $d$. This allows for an evaluation of the crack growth rate based on the stress range only. The latter is plotted in Figure 3(b) based on the hot-spot stress $(\Delta \sigma \cdot S C F)$ measured using strain gauges. The regression line is:

$$
\frac{\mathrm{d} d}{\mathrm{~d} N}=2.85 \times 10^{-12} \cdot(\Delta \sigma \cdot S C F)^{2}
$$

The above observation is not in line with the theory that the stress intensity increases with increasing crack size. The authors
![img-2.jpeg](img-2.jpeg)

Figure 3. Results of the fatigue tests for through-thickness cracks (data taken from Jong (2007)).

![img-3.jpeg](img-3.jpeg)

Figure 4. Annual hot-spot stress histogram.
believe that the observed independence of the crack growth rate with dimension $d$ is a coincidence and has the following two causes:

- Consider the aspect ratio $a / c$ as being approximately constant for a crack that has just grown through the plate thickness. For such a crack - i.e. for small values of $d-$ an increment in the crack size will provide a much larger increase in the crack length on the top side, $d$, as compared to the crack length on the bottom side, $c$.
- The tests were carried out with a fixed wheel position. Figure 2 indicates that this implies a lower stress range as the crack grows for larger crack dimensions. This means that the crack growth rate would have increased had the stress been constant such as in the case of a rolling wheel on a deck plate containing a large crack.

Using the crack growth function of Equation (2) and the above two aspects, the stress intensity factor for the surface point on the bottom side can be calculated so that the crack growth rate according to the model using average values for the variables corresponds with the average crack growth rate observed in the tests. The stress intensity factor obtained in this way reads:

$$
K=.375 M_{w} \sigma \sqrt{\pi c}
$$

The end-of-life criterion for the detail is the attainment of a crack with a size at which instable crack growth occurred due to fracture and/or plastic failure of the remaining ligament. Tests in Jong (2007) were carried out with very high loads on the detail with long cracks in order to determine the semi-crack length of this critical crack; these are indicated by $c_{f}$ (variable 13 of Table 1). Instable crack growth did not occur even for a semi-crack length of 400 mm and a wheel load of 440 kN , i.e. seven times larger than the legislative maximum wheel load. However, these tests were carried out with machined cracks, i.e. not a sharp fatigue crack in which case the critical crack size can be substantially smaller. In addition, the fracture toughness of the material used is not reported. Experience in practice is available in bridges of the crack type of Figure 1 with a semi-length up to 500 or 600 mm . Instable crack growth is not reported for any of these cracks. As a conservative estimate, the average value of $c_{f}$ used in this study is 250 mm .

### 3.3. Loading

Stress ranges in the actual bridge as a result of the crossings of heavy vehicles are obtained by strain gauge measurements on the bottom side of the bridge deck. However, there is no access to the locations at which the hot-spot stresses need to be determined because these locations are inside the stringers. Therefore, strains are measured on other locations and the measurements are compared with the results of a finite element model of the bridge deck. The axle loads applied onto the model are obtained from weigh in motion (WIM) measurements approximately 50 km away from the bridge (see Morales-Nápoles \& Steenbergen, 2014). The stress ranges obtained from the measurements at the bridge were approximately $20 \%$ lower than the stress ranges obtained by the finite element model. This difference is attributed to aspects such as small differences between the traffic loads at the bridge and at the WIM station and more importantly to conservative approximations in the finite element model. An example of the latter is the non-composite working of the asphalt layer and the steel deck plate assumed in the model, whereas some composite working might be present in reality. It is assumed that the same reduction of $20 \%$ on the stress ranges applies to the hot-spot stress of the detail in Figure 1. The annual stress range histogram estimated in this way is provided in Figure 4.

The annual stress histogram of Figure 4 is obtained for the year 2013. However, the loads and therefore the stress ranges are subjected to traffic trends. The distribution of the annual trend factors on the axle loads, $s_{f y}$, and on the number of vehicles, $n_{f y}$, is provided in Table 1 (variables 14 and 15). The number of trucks to be considered is subjected to a maximum, $n_{\max }$ (variable 16 of Table 1), because of the capacity of a lane. This maximum is obtained from WIM measurements on various highways within a distance of 300 km from the bridge which show that $n_{f y}$ reduces to 0 at a certain number of trucks. The distribution of $n_{\text {tmax }}$ (variable 16) is also shown in Table 1. In a Monte-Carlo simulation, the maximum number of axles on the lane is obtained by multiplying $n_{\text {tmax }}$ with the average number of axles per vehicle $n_{\text {axle }}$ (variable 17 in Table 1), which is also obtained from the WIM measurements.

Finally, the response of the bridge is a dynamic response, and for this reason, the stress ranges need to be multiplied by a dynamic amplification factor. The dynamics are more important for the part of the bridge deck at the direct vicinity of the expansion joint as compared to the part of the bridge deck more remote from the expansion joint. The first mentioned area is much smaller - typically a few square metres - than the other area. The stress measurements that were used to construct Figure 4 are located a few metres away from the expansion joint and they include the dynamics of the response. The dynamic amplification factor for the area remote from the expansion joint $\delta_{a f}$, therefore has an average value of 1 . Further down the bridge, a small scatter can be expected. The dynamic amplification factor for the area near the expansion joint $\delta_{a x}$ is estimated to be larger and so is its variation. These dynamic amplification factors are also considered stochastic and the distributions are provided in Table 1 (variables 18 and 19).

![img-4.jpeg](img-4.jpeg)

Figure 5. Flowchart of the crack growth model.

### 3.4. Model uncertainty

A number of aspects of the model are subject to uncertainty. For this reason, an uncertainty factor, $C_{\text {unc }}$, is introduced with which the stress intensity factors are multiplied. The distribution of this uncertainty factor is given in Table 1 (variable 20). The uncertainty factor is an expert estimate which accounts for the uncertainty in traffic load trends, the uncertainty in the calculation of stresses by the finite element method, the uncertainty in the geometric correction factors of the stress intensity factors and the uncertainty in the thickness of the asphalt layer. In a full uncertainty analysis, expert assessments may be obtained by formal methods. For example, those described in Cooke (1991). In the case of this research, estimates are obtained from a single expert from TNO. See also Maljaars and Vrouwenvelder (2014), Maljaars, Steenbergen, and Vrouwenvelder (2012) and Faber and Vrouwenvelder (2001) where different aspects of the uncertainty factor are treated.

### 3.5. Model formulation

The sequence of stress ranges (Figure 4) is fully mixed. This allows for a crack growth rate calculation based on the weighted average of the stress intensity factor. A numerical iteration is applied for solving the governing equations constituting the model:

$$
\begin{gathered}
x_{t}=x_{t-1}+\Delta x_{t} \\
\Delta x_{t}=\Delta t \cdot \min \left(n_{t \max } n_{\text {axle }},\left(1+n_{f y}\right)^{\Delta t_{m}} \sum_{i} n_{i}\right)\left(\frac{\mathrm{dx}}{\mathrm{dN}}\right)_{a v}
\end{gathered}
$$

$$
\begin{gathered}
\left(\frac{\mathrm{dx}}{\mathrm{dN}}\right)_{a v}=f\left(\Delta K_{a v, x}, R, \text { material properties }\right) \\
\Delta K_{a v, x}=\frac{\sum\left(n_{i} \Delta K_{i, x}\right)}{\sum_{i} n_{i}} \\
\Delta K_{i, x}=\left\{\begin{array}{ll}
C_{\text {unc }} Y_{x} \Delta \sigma_{i} \delta\left(1+s_{f y}\right)^{\Delta t_{m}} \sqrt{\pi a} & \text { if } a \leq T \\
C_{\text {unc }} G \Delta \sigma_{i} \delta\left(1+s_{f y}\right)^{\Delta t_{m}} \sqrt{\pi c} & \text { if } a>T
\end{array}\right. \\
Y_{x}=f(\text { geometry, } a, c) \\
G=.375 M_{s c}
\end{gathered}
$$

where:
$x_{t}=$ Crack size, equal to either $a$ or $c$, at time $t(\mathrm{~mm})$, $\Delta x_{t}=$ Crack increment at time $t(\mathrm{~mm}), \Delta t=$ Time increment (year), $\Delta t_{m}=$ Difference between assessment year and year of monitoring (year), $\Delta \sigma_{i}=$ Stress range $i$ of the histogram in Figure $4, \Delta K_{i, x}=$ Stress intensity factor range corresponding with stress range $\Delta \sigma_{i}$ and crack size $x, n_{i}=$ Annual number of repetitions of a cycle with range $\Delta \sigma_{i}, \Delta K_{a v, x}=$ Average stress intensity factor

![img-5.jpeg](img-5.jpeg)

Figure 6. Typical dependence structure for one monitored location together with $k$ other non-monitored locations (a) and one empirical probability density function (PDF) of NE location complying with monitoring (b).
range weighted for the number of cycles, $(\mathrm{dx} / \mathrm{dN})_{a v}=$ Average crack growth rate, $\delta=$ Dynamic amplification factor, equal to $\delta_{e x}$ at the expansion joint or $\delta_{g t}$ away from the expansion joint.

Here, the material properties are represented by the variables $K_{1 C}, \Delta K_{0}, A, m$ and $p$, and the geometry is represented by the variables $T$ and $t_{a}$.

In the evaluation of the semi-crack length at the top of the plate, $d$, it is assumed that the aspect ratio of the throughthickness crack, $a / c$, is equal to that of a surface breaking crack (Figure 1). Because the geometric correction factors $Y_{a}$ are functions of the crack dimensions, $a$ and $c$, the equations need to be solved simultaneously for these crack dimensions. Figure 5 gives a schematic overview of the crack growth model.

## 4. Dependence model - preliminaries and context

The crack growth model outlined in Section 3 outputs the crack growth development for one detail of the bridge. As explained earlier, a bridge may contain hundreds of these heavily loaded details. Correlation between variables in different sections of the bridge has to be taken into account which can stem from various reasons, e.g. same welding procedure, similar loading condition, etc. The goal is to make use of this characteristic in order to propagate information coming from monitored sections into non-monitored parts. The rank correlations, $r$, of the random variables between different locations of the detail of Section 2 are given in Table 1. These correlations were quantified by field data, using previous literature and expert opinion (as provided in Maljaars \& Vrouwenvelder, 2014). The aim is at quantifying the complete dependence structure of the random variables. In order to achieve this, a Bayesian network is used. From this Bayesian network, the variables in Table 1, used in the crack growth model underlying every detail in a bridge, are sampled. Next, the class of BNs that will be used in the remainder of this paper is briefly described.

### 4.1. Bayesian networks

BNs are objects developed around probability and graph theory. A BN consists of vertices (also called nodes) and directed arrows (also referred to as edges or arcs). Nodes represent univariate
random variables that can be either continuous or discrete. Arcs join the different nodes of a BN and entail probabilistic dependencies between them. The graph corresponding to a BN must be a directed acyclic graph (DAG). In the DAG, the direct predecessors of a node are referred to as parents and conversely children are direct successors of a particular node. The BN together with the probabilistic dependencies implied by the DAG ensures the construction of a joint distribution. One of the main advantages of BNs that makes them appealing for applications is precisely their ability to represent a joint distribution in a relatively simple and intuitive way.

A complete review of BNs is out of the scope of this paper. However, for the formalisation of discrete BNs, we refer to Pearl (1988). The class of BNs that will be used in this paper corresponds to Non-Parametric BNs (NPBNs) which are developed for continuous random variables such as the ones treated in this paper. For a detailed overview of the theory and applications of NPBNs, we refer to Hanea, Kurowicka, and Cooke (2006), Hanea, Morales-Napoles, and Ababei (2015) and the references therein. Here, only the main concepts of NPBNs will be repeated for the purpose of completeness. For an example of an NPBN, see Figure 6(a), which will be discussed in detail in the next subsection. Observe that Figure 6(a) represents nodes (marginal distributions) as histograms. In this case, variable 11 in Table 1, stress concentration factor at the crossbeam web, is represented. This log normal variable has mean 2.1 and a standard deviation of .21 , (displayed at the bottom of the histogram are the sample mean and standard deviation).

The parent variable exhibits a certain dependence pattern with $k$ children. In the NPBNs, the dependence is induced through copulas. For a recent and complete overview of copulas, the reader is referred to Joe (2015). Copulas are roughly a joint distribution of uniform variables in $[0,1]^{D}$, where $D$ denotes the dimension of the copula. This property makes them appealing for simulation as well as for more clearly investigating dependence patterns since one may separate the dependence structure from the marginal distribution.

For one parameter copulas, the dependence structure may be summarised through Spearmans rank correlation coefficient. Spearmans rank correlation coefficient for random variables $X$

and $Y$ is the usual Pearsons product moment correlation coefficient applied to the ranks of $X$ and $Y$ :

$$
r(X, Y)=\frac{\mathbb{E}\left(F_{X}(X) F_{Y}(Y)\right)-\mathbb{E}\left(F_{X}(X)\right) \mathbb{E}\left(F_{Y}(Y)\right)}{\sigma_{F_{X}(X)} \sigma_{F_{Y}(Y)}}
$$

where $F_{X}(x)$ is the rank of $x \in X$. The main result of NPBNs states that by specifying the one-dimensional margins, the DAG and the (conditional) bivariate copulas (summarised by conditional rank correlations), the joint distribution of the variables is completely determined and satisfies the properties (dependence structure) represented by the BN. The rank correlations $r$ in Table 1 were obtained from expert knowledge with techniques similar to the ones in Morales-Nápoles, Delgado-Hernández, and De-León-Escobedo (2015). The next section elaborates about the dependence structure of interest for this application.

### 4.2. Dependence structure

The set of random variables determining the crack growth development in the monitored location is displayed in Table 1. It is assumed that these variables are independent of each other. Moreover, one set of these variables for the crack growth development is present in every other detail on the bridge in the non-monitored section. These variables are correlated with each other. The dependence structure of each variable in different parts of the bridge is described with a BN. As discussed before, the monitored section is the most vulnerable section of the bridge due to the fact that the dynamic amplification factor for this location differs from the one in the other locations.

Figure 6 displays both the typical dependence structure (Figure 6(a)) of these variables and one sampled non-monitored location (Figure 6(b)). As an example, variable 11 from Table 1 is shown, i.e. the stress concentration factor at the crossbeam web. The histograms represent the unconditional distributions both for the monitored (parent) and for the $k$ non-monitored (children) locations elsewhere in the bridge. The mean and standard deviation are displayed below the corresponding histogram. The arcs connecting the nodes are also displayed in Figure 6(a) and the numbers .8 represent the rank correlation between the monitored and non-monitored locations. The probability density function (PDF) illustrated in Figure 6(b) represents one of the $k$ sampled non-monitored locations and is obtained by MonteCarlo simulations where only those samples that agree with monitoring data are selected.

Both the dependence structure and sampled non-monitored locations for all other variables listed in Table 1 are built in the same way as Figure 6. In this way, a $k$-dimensional distribution for each variable has been obtained, and consequently, a multidimensional distribution represented by sets of BNs similar to the one is shown in Figure 6(a). It is important to mention that other dependence configurations have been explored and discarded. The alternative configurations include, for example, a complete graph (all variables connected to each other, so that correlations are also considered between all non-monitored locations for each variable), however, no significant difference in the output of the model was observed with respect to the simpler configuration displayed in Figure 6(a).

The BNs for the different variables are used to perform inference on the crack growth development given observations.

## 5. Simulation results

### 5.1. Simulations without conditioning

Let us consider a (fictitious) bridge with construction year 1991 and with a total number of 492 heavily loaded details of type described in Section 2 (Figure 1). The model in Section 3 describes the crack growth development of a crack in one such a detail. Monte-Carlo simulations are used to sample the variables of Table 1 for both the monitored and non-monitored details. The difference between these locations is the location of the detail; the monitored detail is located close to the expansion joint, experiencing a higher dynamic load (variable 18) than the non-monitored details away from the expansion joint (variable 19).

Apart from the higher dynamic load in the monitored detail of the bridge, the same model is used to predict the crack growth development in the non-monitored details. The Monte-Carlo sampling also takes into account the dependence structure imposed by the Bayesian network. In other words, each sample is drawn from a multivariate distribution giving values for all the variables of Table 1 and for all the modelled details of the bridge, taking into account the correlations between the different locations.

Hence, for every Monte-Carlo sample, both the monitored and the non-monitored locations are considered in order to preserve the dependence structure. The sampled variables then determine the crack growth development in the different details. As an example, the crack growth developments of 1000 of these Monte-Carlo simulations are displayed in Figure 7. The ends of the curves represent the attainment of the critical crack length regulated by variable 13 of Table 1. The year of attainment of the critical crack length is selected for each Monte-Carlo simulation and the PDF of this failure year resulting from $10^{5}$ Monte-Carlo simulations is displayed in Figure 8. Again, the difference of the two curves in Figure 8 is the location of the detail.

The average life obtained with the simulation is consistent with our previous models, which in turn agreed well with observed cracks in bridge decks in The Netherlands (Maljaars et al., 2012). The scatter in the figure is in line with the considered uncertainty in the fatigue load on the one hand, and with the data scatter of the fatigue response on the other hand. With respect to the latter: the scatter in fatigue life, $N$, is roughly between $\log (N)=.2$ for one test series (DNVGL-RP-0005, 2014) and $\log (N)=.35$ for several test series on one material (Den Besten, 2015).

In Figure 7, a high variation in the simulation results is observed. This variation is caused by the fact that the crack growth development is determined by various variables all taking random values. Without any extra knowledge, it is hard to give an accurate prediction of the crack growth development. The PDFs of Figure 8 reveal the effect of a higher dynamic load on the monitored detail. It is observed that the end-of-life is expected earlier for the monitored details. The expected value of the failure year is 2068 for the monitored detail and 2095 for the non-monitored detail.

![img-6.jpeg](img-6.jpeg)

Figure 7. Crack growth development for monitored detail.
![img-7.jpeg](img-7.jpeg)

Figure 8. PDF of the failure year.

### 5.2. Sample-based conditioning for the monitored section

To reduce the uncertainty of the model, a crack monitoring system is installed near the detail close to the expansion joint with the objective of updating believes regarding crack growth of this detail. Let us assume that a crack is first detected in 2013, i.e. 22 years after construction of the bridge. The depth, $a$, of this first detected crack is estimated between 3 and 6 mm .

This monitoring result is now used to interfere in the BNs. Inference refers to computing the conditional distribution of a subset of variables given observations of a different subset in the same BN. Inference in NPBNs may be exact under the normal copula assumption. In the case of the present application, however, the crack size resulting from the monitoring system is output instead of input for the model, and hence, exact inference is not possible. Instead, sample-based conditioning
is performed by selecting only those Monte-Carlo simulations that agree with the monitoring results. Out of a total of $10^{5}$ Monte-Carlo simulations, 2716 Monte-Carlo samples had a crack depth, $a$, between 3 and 6 mm in 2013. A selection of these conditioned samples is indicated in black in Figure 9 for the monitored section.

Figure 9 reveals that the extra information coming from the monitoring system significantly decreases the variability of the outcomes and thereby increases the accuracy of the crack growth predictions.

The Monte-Carlo samples of the monitored section (i.e. near expansion joint) complying with the monitoring results were selected together with the corresponding samples of the non-monitored sections (i.e. away from the expansion joint). This provides us not only with the conditional probability densities of the end-of-life of the monitored section, but also of that of the non-monitored section. Since the variables of the other non-monitored details are equally distributed, only one of the non-monitored details is simulated. Moreover, the dependence structure that is chosen, after trying different configurations (see Section 4.2), indicates that the variables of the non-monitored details are conditionally independent given the results of the monitored detail. Apart from the resulting end-of-life, also the variables of Table 1 can be conditioned on the monitoring results by selecting the values for the variables of the MonteCarlo simulations complying with the monitoring results. This enables us to obtain a first root cause analysis and find out which variables have a significant influence in the current use-case. An example of the sample-based conditioning for variable 11 is presented in Figure 6(b). Other variables in the monitored and non-monitored sections of the bridge are conditioned similarly.

![img-8.jpeg](img-8.jpeg)

Figure 9. Crack growth development for monitored detail conditioned on the monitoring results.
![img-9.jpeg](img-9.jpeg)

Figure 10. Prior and posterior distribution of variable 7 (crack growth threshold at $R=0$ ).

For these specific variables, sample-based conditioning shows different amplitude in terms of sensitivity. While it was explored that for the majority of them the posterior distribution remains practically unchanged (e.g. variable 11 of Figure 6), a few, namely variables 5 (stress intensity ratio) and 7 (crack growth threshold at $R=0$ ) prove to be relatively sensible with respect to conditioning. For variable 7, the conditional and unconditional distributions are displayed in Figure 10. Here, it is observed that the probability distribution for the difference between the unconditional distribution and the distribution obtained after conditioning on the monitoring results. Quantitatively for variable 7, this is translated by the following: for the unconditional case, its average equals $243 \mathrm{~N} / \mathrm{mm}^{3 / 2}$ and its standard deviation equals $97.2 \mathrm{~N} / \mathrm{mm}^{3 / 2}$, whereas for the conditional case, the average equals $189.34 \mathrm{~N} / \mathrm{mm}^{3 / 2}$ and standard deviation $61.55 \mathrm{~N} / \mathrm{mm}^{3 / 2}$.
![img-10.jpeg](img-10.jpeg)

Figure 11. PDF of the failure year conditioned on the monitoring results.

![img-11.jpeg](img-11.jpeg)

Figure 12. Expected number of critical cracks.

The conditioned (posterior) end-of-life distributions resulting from the analysis are provided in Figure 11 together with their unconditioned (prior) counterparts. The figure indicates that the posterior end-of-life prediction of the monitored part is more certain than its prior. The reduced variation allows us to make more accurate predictions about the degradation of this detail. The update of the non-monitored part is, however, much smaller due to the rather weak correlation structure. This weak correlation is the reason that in Maljaars and Vrouwenvelder (2014), it is concluded that the effect of inspecting only a part of the structure instead of all vulnerable details is not effective. However, here, the monitoring system is applied on the detail for which the shortest life was expected. In this case, the posterior distribution of the non-monitored details still provides valuable information because critical cracks in non-monitored details typically arrive later than the crack first observed in the monitored location. This is displayed in Figure 12. Since the number of details is known, the expected number of critical cracks over time both unconditioned and conditioned on the monitoring results can be computed. In this case, the measured size of the monitored crack is larger than the prior expectation; therefore, the bulk of the cracks arrive earlier than originally anticipated as becomes apparent from Figure 12. This allows the owner of the bridge to plan actions such as a renovation of the bridge.

It is observed that combining the model with a monitoring system has a significant impact on the uncertainty of the results, also for the details of the bridge that are not monitored. Moreover, it is possible to do a root cause analysis, via the Bayesian network, and find the governing variables determining the outcome of the model.

## 6. Conclusions

A crack growth model for cracks in welded details of the orthotropic deck structure of steel bridges has been developed. The type of crack considered can be a serious threat to bridge reliability and timely maintenance is crucial. Crack growth predictions can therefore be very useful in determining maintenance intervals for which traffic safety can be guaranteed without performing unnecessary maintenance. Monte-Carlo simulation has been used to predict the 5,50 and $95 \%$ quantiles of the crack growth developments of cracks in a specific bridge.

The failure year distribution resulting from the simulations spans approximately 200 years, demonstrating a significant scatter caused by wide distributions of some variables.

In order to reduce some of the associated uncertainties, a monitoring system for detecting fatigue crack activity has been installed. Sample-based conditioning on the MonteCarlo simulation was then used in order to obtain a new conditioned failure year distribution. This conditioned failure year distribution shows less variation (with a span of approximately 20 years) and enables us to give a more accurate crack growth prediction.

Monitoring a complete bridge is expensive and might be unnecessary because crack growth developments in different sections of the bridge are correlated. A Bayesian network was used to describe the dependence structure between the different details of the bridge and the monitored section which is, because of the presence of the expansion joint, the heaviest loaded section of the bridge. Through the same approach, a new conditioned failure year distribution is obtained not only for the monitored detail, but also for other details of the bridge. The updated, more accurate prediction of the failure year of the details considered causes a reduction of unnecessary maintenance and helps preventing unplanned closure of the bridge due to ad hoc repairs.

In summary, the following conclusions can be derived:

- Because of the high amount of scatter and uncertainty in the input parameters, the crack growth model provides very scattered results.
- Installing a monitoring system significantly decreases the uncertainty of the crack growth prediction.
- The BN makes it possible to apply the monitoring results in order to make more accurate predictions about the non-monitored details.
- The BN also enables a root cause analysis, and indeed, it was discovered that the crack growth threshold and the stress intensity ratio are the variables with most influence in the crack growth model.
- The combination of the crack growth model and monitoring system provides therefore valuable information about the degradation of the bridge.

Future research would profit from monitoring other sections of the bridge while taking advantage of the dependence model proposed for the non-monitored section of the bridge. The Bayesian network can be used to incorporate knowledge on every detail of the bridge, each time updating the crack growth predictions. The current model constitutes a first step towards this goal.

The next steps constitute further calibration of distributions and correlations between parameters using field measurements and information from fatigue tests. In addition, further validation of the outcomes of the model by comparing it to reported cracks in actual bridges is suggested.

## Disclosure statement

No potential conflict of interest was reported by the authors.
