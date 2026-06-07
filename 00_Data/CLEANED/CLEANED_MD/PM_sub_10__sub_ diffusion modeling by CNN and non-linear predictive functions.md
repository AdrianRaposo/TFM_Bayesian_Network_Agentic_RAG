# $\mathbf{P M}_{10}$ diffusion modeling by CNN and non-linear predictive functions 

F. M. Raimondi, A. Lo Bue, M. C. Vitale \& G. S. Amico<br>Dipartimento di Ingegneria dell'Automazione e dei Sistemi, Palermo University, Italy


#### Abstract

In this paper a model for the forecast and control of atmospheric pollution caused by particulate matter $\left(\mathrm{PM}_{10}\right)$ is proposed. It is based on the use of cellular neural networks (CNNs).

More precisely, the model is the result of the integration of the mass balance equation and, at the same time, by the use of cellular neural networks (CNNs) and Bayesian networks in the context of a planar grid which describes a whole urban area; we considered the "areal" sources conditioned by meteorological and pollutant parameters.

The CNNs allow one to define a cellular system which gives the redefinition of the mass balance equation trough a dynamic discrete rule (update) that considers the contributions of the near cells.

Bayesian nets provide the forecast in a fixed time interval which will be used for the determination of the pollutant amount in the interested area. Dynamics of the single cell feel the effect of meteorological and environmental parameters; contributions of these parameters are considered by means of some weights that will be determined through the minimization of an error index that is a function of the estimated data and the provisional data coming from the learning process by Bayesian networks tested with values from monitoring stations. The results obtained with this approach are quite interesting and the proposed model produces innovative results because it takes advantage of the combination of two models: CNN (for mesoscale topology) and Bayesian network (for the daily forecast of the $\mathrm{PM}_{10}$ concentration).


## 1 Introduction

Controlling possible sources of atmospheric pollution and prevention critical events has become a relevant problem in our increasingly degraded environment.

Air pollution produced by motor vehicles is one of the most serious and rapidly growing problems in the urban centers of Italy (but the situation is not different in many other parts of the world) [18].

Moreover, concentrations of atmospheric pollutants change rapidly with meteorological variables such as wind speed and direction, temperature, humidity and quantity of rain precipitations, solar radiation.

The $\mathrm{PM}_{10}$ (Particulate Matter with less than $10 \mu \mathrm{~g} / \mathrm{m} 3$ of diameter) is one of the most harmful air pollutants. Its levels are particularly high in the town of Palermo (Italy) and therefore they have captured researcher attention in the last few years [15].

The air pollution models can help to analyze the impact of pollutants in a specific study area and to identify and quantify cause-effect relationships between polluting sources and air quality, allowing us to evaluate different scenarios [3][6].

Many different mathematical models have been used in the study of this problem [16] and in the last few years soft computing techniques have been used in similar problems, providing good results. Their success depends on their possibility of dealing with systems affected by uncertainty. In fact, theories such as fuzzy logic, neural networks, and Bayesian networks have been applied to this topic [1, 2]. Neural networks, in particular, have often been used in predicting atmospheric pollutant concentrations [11].

The aim of our work is to develop a probabilistic model for an input part and a deterministic model for the prediction of atmospheric pollution critical events. We used data measured in the urban area of Palermo by several monitoring stations deployed in the town. They were the $\mathrm{PM}_{10}$ concentration and meteorological parameters that include rain, humidity, wind speed and direction at the different hours of the day. We illustrate a method based upon the application of Cellular Neural Networks (CNN) for modeling the $\mathrm{PM}_{10}$ concentrations in the whole city of Palermo (the ours mesoscale) considering values obtained by Bayesian networks trained with data measured from monitoring stations.

In the next section we will discuss the significant characteristics of Cellular Neural Networks. In the third paragraph we analyze the CNN models of $\mathrm{PM}_{10}$ and we discuss typical network topology and parameters. In the fourth section we report the several optimization method used and the best one, in the fifth section we report the experimental results. Finally, some conclusions are drawn about the proposed approach and future works.

# 2 Cellular Neural Networks: basics and applications 

Cellular Neural Networks (CNNs) have been applied in very different fields, and they proved successful in several applications allowing one to solve problems $[4,5]$.

Some real applications include image processing, PDE resolution, intelligent pattern and motion detection, bioinformatics and memory association. CNN, also called Cellular Nonlinear Network, constitute an elaboration model proposed by

Chua and Yang in 1988 [7], defined like a set of non-linear circuits in an ndimensional space with a parallel and asynchronous elaboration structure.

CNNs can work with continuous or discrete values. Generally, CNN data and parameters have continuous values.

The fundamental building block of the CNN is the cell. The CNN is an array of cells. Every cell is a performing element with several inputs and one individual output.

The cells are arranged in one or more layers on a regular grid. Each cell influence evolution of a finite number of cells called "neighborhood" [4].

The definition of a cell neighborhood is univocally identified by a metric and a radium; more precisely an r-neighborhood of $\mathrm{C}(\mathrm{i}, \mathrm{j})$ is

$$
N(i, j)=\{C(k, l) \mid d(k, l, i, j) \leq r, l \leq k \leq M ; l \leq l \leq N\}
$$

where $r \in N-\{0\}$ is the radium.
The influence relation among cells is said "Sinaptic law" that defines the coupling between the considered cell $\mathrm{Ci}, \mathrm{j}$ and all cells $\mathrm{Ck}, \mathrm{l}$ within their neighborhood [4]. This law is expressed as:

$$
\boldsymbol{I}_{i, j}^{s}=\AA_{i, j}^{k, l} \quad x_{k, l}+\AA_{i, j}^{k, l} * f_{k, l} \quad\left(x_{i, j}, x_{k, l}\right)+\boldsymbol{B}_{i, j}^{k, l} \times u_{k, l}
$$

More precisely interactions between cells are local and usually translation invariant, but these interactions indirectly cause a propagation of local effects over all the cells. The cell core can be any dynamical system. In the case of continuous-time CNN the dynamic is defined by:

$$
\left\{\begin{array}{c}
\boldsymbol{x}_{i, j}=-\mathrm{g}\left(\mathrm{x}_{\mathrm{i}, \mathrm{j}}, \mathrm{z}_{\mathrm{i}, \mathrm{j}}, \mathrm{u}_{\mathrm{i}, \mathrm{j}}(\mathrm{t}), \mathrm{I}_{\mathrm{i}, \mathrm{j}}^{\mathrm{s}}\right) \\
\mathrm{y}=\mathrm{f}\left(\mathrm{x}_{\mathrm{i}, \mathrm{j}}\right)
\end{array}\right\}
$$

where:
$\mathrm{g}\left(\mathrm{x}_{\alpha}, \mathrm{z}_{\alpha}, \mathrm{u}_{\alpha}\right)$ is the cell state derivative;
$\mathrm{I}_{\alpha}^{\mathrm{s}}$ is the "synaptic law";
$\mathrm{f}\left(\mathrm{x}_{\mathrm{i}, \mathrm{j}}\right)$ is the output function.
In most cases a linear CNN is utilized, where cell dynamics are governed by the following differential equation

$$
\frac{d x_{i, j}(t)}{d t}=-x_{i, j}(t)+\sum_{(k, l) \in N(i, j)} a_{(i, j, k, l)} f\left(x_{k, l}(t)\right)+\sum_{(k, l) \in N(i, j)} b_{(i, j, k, l)} u_{k, l}+I_{i, j}
$$

where:
$\{a(i, j, k, l)\}$ is the feedback coefficient set about the output;
$\{b(i, j, k, l)\}$ is the control coefficient set about the input;
$f\left(x_{i, j}(t)\right)$ is the output function.

Besides, CNN defines boundary conditions that determine the bias of the outer cells on boundary cell dynamics [5].

From the computational point of view a two-dimensional CNN is a model of calculation that summarizes some typical characteristics of the neural nets and the Cellular Automata. In contrast to other types of artificial neural networks the interaction between CNN cells can be given by nonlinear functions.

Different to well known neural nets, in CNN the concepts of hidden layers and Feed-Forward are missing, but there is a Feed-Back concept.

# 3 CNN models of $\mathrm{PM}_{10}$ pollution 

In this work we aim to provide an estimation (prevision every two hours, from 8 a.m. to 22 p.m) of the $\mathrm{PM}_{10}$ concentrations on the mesoscale (the area of interest is defined as the area where monitoring stations, providing pollutant values and meteorological parameters, are located) and the areas influenced by the diffusion and production of the $\mathrm{PM}_{10}$ in the cells of the whole grid. The mesoscale is constituted by cells covering an area of $1 \mathrm{~km}^{2}$.

The pollutant concentration in a cell at time $\mathrm{k}+1$ depends on pollutant concentration released at time k and pollutant components that came from the near cells.

All of that is conditioned by meteorological data course that is present through a functions template with parameters that will be defined from a pollutant concentrations identification process in order to obtain the best value that summarizes all phenomena that exist in the considered urban area.

The pollutant concentrations and meteorological parameters determination has happened through an optimization process of an error function (the broadcast average error) having as inputs the forecast data given by Bayesian nets [10] and the values obtained by the CNN evolution (mean square error). The implemented model is reported in figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1: The implemented forecasting model.
To realize the model we considered a CNN obtained by discretizing the mass balance equation in space and time. Such a model turns out from the disposition on planar $\mathrm{n} \times \mathrm{m}$ dimension grid.

# 3.1 CNN Model of the cell $\mathbf{C}(\mathbf{i}, \mathbf{j})$. 

We considered a CNN model that is related to a model referred to as the mass balance principle, [8][9] redefined according to exogenous variables and to the state $\overline{\mathrm{x}}$ coinciding with urban, environmental and meteorological parameters. The $\overline{\mathrm{x}}$ vector is represented as:
[C Rug Pop Roads RedTl GreenTl YellowTl Wx Wy Hum Rain] $]_{(i, j, h)}$ with:
C is the pollutant concentration;
Rug is the rugosity coefficient;
Pop is the number of resident people;
Roads are total length (in Km ).
RedTl, GreenTl, YellowTl constitute different traffic controller (traffic light);
Wx and Wy are the wind components;
Hum is the humidity;
Rain is the quantity of precipitations.
Therefore, from a second order PDE [3]:

$$
\frac{\partial \mathrm{C}}{\partial \mathrm{t}}=-\mathrm{v}_{\mathrm{x}} \frac{\partial \mathrm{C}}{\partial \mathrm{x}}-\mathrm{v}_{\mathrm{y}} \frac{\partial \mathrm{C}}{\partial \mathrm{y}}+\mathrm{K}_{\mathrm{xx}} \frac{\partial^{2} \mathrm{C}}{\partial^{2} \mathrm{y}}+\mathrm{K}_{\mathrm{xx}} \frac{\partial^{2} \mathrm{C}}{\partial^{2} \mathrm{y}}+\left(\frac{\partial}{\partial \mathrm{y}}\left(\mathrm{~K}_{\mathrm{zz}} \frac{\partial \mathrm{C}}{\partial \mathrm{z}}\right)\right)+\mathrm{S}(\mathrm{x}, \mathrm{y}, \mathrm{z}, \mathrm{t})+\mathrm{R}(\mathrm{x}, \mathrm{y}, \mathrm{z}, \mathrm{t})
$$

we will have a discretized equation in space and in time for the update of $\mathrm{PM}_{10}$ component at time $k+1$ :

$$
\mathrm{C}_{\mathrm{ij}}(\mathrm{k}+1)=\left[\mathrm{C}_{\mathrm{ij}}(\mathrm{k})+\mathrm{S}_{\mathrm{ij}}(\mathrm{k})+\sum_{\mathrm{c}(\mathrm{k}, \mathrm{l}) \in \mathrm{N}(\mathrm{i}, \mathrm{j})}(\mathrm{fWind} \circ \mathrm{fHum})\left(\overline{\mathrm{x}}_{\mathrm{k}, \mathrm{l}}\right)\right)-\mathrm{Cdis}_{\mathrm{ij}}] * \operatorname{fRain}\left(\overline{\mathrm{x}}_{\mathrm{i}, \mathrm{j}}\right)
$$

where:
$S_{i j}(k)$ is the pollutant amount released in cell $\mathrm{i}, \mathrm{j}$;
$\mathrm{fWind}\left(\overline{\mathrm{P}}_{\mathrm{w}}, \overline{\mathrm{x}}_{\mathrm{i}, \mathrm{j}}\right)$ is the contribute that derives from the transport phenomenon parameterized in vector $\mathrm{P}_{\mathrm{w}}$;
$\mathrm{fHum}\left(\overline{\mathrm{P}}_{\mathrm{H}} \overline{\mathrm{x}}_{\mathrm{i}, \mathrm{j}}\right)$ is the value that conditions the pollutant dispersion parameterized in vector $\mathrm{P}_{\mathrm{H}}$;
$\operatorname{fRain}\left(\overline{\mathrm{P}}_{\mathrm{R}}, \overline{\mathrm{x}}_{\mathrm{i}, \mathrm{j}}\right)$ is the value that conditions the pollutant dejection parameterized in vector $\mathrm{P}_{\mathrm{R}}$

Moving from the PDE mass balance equation [6] to the previous update equation we redefined the molecular diffusion phenomenon, the vertical component of wind, the coefficients Kxx and Kyy that are independent from x and y and the removal phenomena with the replacement of relations which consider the meteorological parameters and rugosity.

For the pollutant production in the cell, the following socio-ambient parameters are considered:

- number of citizens resident in cell $\mathrm{Ci}, \mathrm{j}$;
- number of traffic lights installed in the cells of the network;
- total length (in Km ) of principal roads that could be run by motor vehicles in considered time range.
The source at time k will result be sum of three components

$$
\mathrm{S}_{\mathrm{ij}}(\mathrm{k})=\Gamma(\mathrm{k}, \mathrm{i}, \mathrm{j}) \times \sum_{\mathrm{l}=1}^{\mathrm{n}} \mathrm{~S}_{\mathrm{ij}}
$$

$\Gamma(k, i, j)$ is the value better fitting $\mathrm{PM}_{10}$ evolution in similar cell, concerning urban parameters, where is installed the monitoring station;

The contribution of every member is outside the following polynomial weight function:

$$
S_{i j l}(k)=\sum_{m=1}^{n} w_{l m} \times P_{i j l}^{m}
$$

$P_{i j l}$ is the l-th urban parameter.
The cell $(\mathrm{i}, \mathrm{j})$ is characterized by a neighbors set which depend on an r order and on d metrics.

For own model we have choose the Von Neumann [4] neighborhood namely

$$
\begin{gathered}
\boldsymbol{d}=\max (|\mathrm{i}-\mathrm{m}|+|\mathrm{j}-\mathrm{n}|) \\
\boldsymbol{r}=1
\end{gathered}
$$

the resultant neighborhood for a generic inner cell is reported in figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2: Neighborhood for a generic inner cell $\mathrm{C}_{\mathrm{i}, \mathrm{j}}$.
Such a choice has been motivated by the fact we considered the wind field turning in the two directions (North and East).

For our model, we choose the fixed (Dirichlet) [4] boundary conditions, namely
$\overline{\mathrm{x}}_{\mathrm{k}, 1}=\overline{0}$ if the cell $\mathrm{C}(\mathrm{k}, \mathrm{l})$ do not belong to the CNN lattice.

# 4 The used optimization method 

In order to obtain the pollutant concentrations and the functions template parameters that give the best forecast of the pollution value in studied area, an optimization procedure [10] that requires the use of a standard technique, Adaptive simulated annealing (ASA) [14], has been executed.

This optimization problem belongs to the class of multivariate, continuous, quadratic nonlinear and constrained problems.

We used three simulation methods that provide the initial stadiums and the parameters that minimize the error function: Particle Swarm Optimization (PSO)[12], Downhill-simplex [13, 17] with constraints, and ASA [14].

These optimization methods have been chosen because of the high number of model variables and because it would have been difficult to calculate the gradient on the control variables representing the initial states.

Our optimization problem requires the function to minimize (the mean square error):

$$
\mathrm{E}=\frac{1}{\mathrm{~N}_{\mathrm{c}} \mathrm{~N}_{\mathrm{k}}} \sum_{(\mathrm{i}, \mathrm{j}) \in \mathrm{T}} \sum_{\mathrm{k}}\left[\mathrm{C}_{\mathrm{ij}}(\mathrm{k})-\tilde{\mathrm{C}}_{\mathrm{ij}}(\mathrm{k})\right]
$$

where T is the cells set containing monitoring stations of the obtained CNNsolution for the cell containing the monitoring stations.

Control variables, placed in a vector, turn out form

$$
\left[\begin{array}{c}
\mathrm{Ci}, \mathrm{j}(0) \\
\tilde{\mathrm{w}} \\
\mathrm{P}
\end{array}\right]
$$

where:
$\mathrm{Ci}, \mathrm{j}(0)$ is the initial time $\mathrm{PM}_{10}$ value for the generic cell without monitoring stations;
$\tilde{w}$ is the array of weights that is related to polynomial weight function (8) ;
$P$ is the vector that identifies meteorological parameters and functions (6).
PSO has been used because well right at the functions study with several parameters.

The downhill-simplex-method requires no explicit gradient information, while ASA [14] allows us to better explore the research space avoiding the local minimums in a way that can obtain a best error minimum and the global minimum.

With several simulations we observed that the best results have been produced using the ASA method.

## 5 Experimental results

We conducted several experiments, applied to the city of Palermo, with a single network topology but with different dynamic laws of cells and consequently considering different values of the parameters.

We used historical data from the beginning of 1998 to end of 2002 to update the probabilistic tables of the Bayesian networks and then we used the prediction provided by Bayesian network to obtain previsions of $\mathrm{PM}_{10}$ pollution in cells of CNN, missing of monitoring stations in first months of 2003.

After we have applied the minimization process previously described, the broadcast average error has been approximately $22 \%$.

Some optimization process results ( $\mathrm{Pm}_{10}$ distribution and model template functions) are shown in the tables 1 and 2 for January 12, 2003.

The model template functions and the source weights vector are:

$$
f \text { Wind }\left(w \text { Rug, } w \text { RugExp, }(v, c, \text { rug })_{i, j}\right)=w \text { Rug } \times a b s(v) \times c \times \exp (-w \text { RugExp } \times \text { rug })
$$

where: wRug is 0,0104 , wRugExp is 2,07 .

$$
f \text { Hum }(\text { lower, upper }, u)=\text { upper }+\frac{\text { lower }- \text { upper }}{100} \times u \text { with } 0 \leq u \leq 100
$$

where: lower is 0,263 , upper is 0,862 .

$$
\begin{aligned}
& f \text { Rain }(a l p h a, \text { lower }, w \text { Rain }, r)=w \text { Rain } \times \max \{l o w e r, \exp (-a l p h a \times r)\} \\
& \text { with } r \in \mathfrak{R} \cup\{0\}
\end{aligned}
$$

where: alpha is 0.0856 , lower is 0.727 , wRain is 0.894 .

$$
w^{T}=\left[\begin{array}{lll}
w R o a d s= & 1.08 & w \text { Green }=1.03 \\
& & w B l u=1.48
\end{array} \quad w \operatorname{Re} d=1.37 \quad w \text { Pop }=0.489\right]
$$

The results obtained with experimental simulations are quite interesting and we observed that similar cells have a congruous trend with the reference cell.

# 6 Conclusions 

In this paper a model for the forecast of $\mathrm{PM}_{10}$ pollution is proposed. This model is based on the use of Cellular Neural Networks (CNNs) for the mesoscale topology and Bayesian networks for the daily forecast of pollutant concentration. It has been applied to the city of Palermo using $\mathrm{PM}_{10}$ concentrations and meteorological data measured by several monitoring stations. We have obtained interesting results but in the future we expect to improve the model behaviour by addressing the following limits of the model:

- the small volume of data for the vehicular traffic volumes in the city roads;
- the low granularity of the model - the greater number of cells that the net is composed of the better the performance of the model;
- results could improve if tridimensional CNN is adopted.

The model studied could be used to support the following operating scenario: the municipal authorities acquiring the measurements of the relevant parameters can soon have an estimation of the levels of $\mathrm{PM}_{10}$ with respect to the law limits that is sufficiently affordable to quickly establish specific restrictions on traffic in order to deal with the presence of critical events.

Table 1 shows the sea cells zone, and some similar cells.

Table 1: $\quad \mathrm{Pm}_{10}$ Distribution at 20.00 .


![img-2.jpeg](img-2.jpeg)

Figure 3: PM10 Isometric graphic at 20.00 .

# Acknowledgements 

We would to thank: Azienda Municipalizzata Igiene Ambientale (AMIA) Palermo, Club Albaria: Associazione sportiva Albaria - Mondello (Pa), Osservatorio Astronomico "G. S. Vaiana" (INAF) - Palermo, SIAS Servizio informatico agrometeorologico siciliano (Assessorato regionale agricoltura e foreste) - Palermo, Ufficio Statistica - Palermo, Comando Polizia Municipale di Palermo for providing the atmospheric pollutant and meteorological data we used.
