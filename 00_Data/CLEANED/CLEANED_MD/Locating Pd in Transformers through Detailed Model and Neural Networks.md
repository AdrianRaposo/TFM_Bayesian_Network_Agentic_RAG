# LOCATING PD IN TRANSFORMERS THROUGH DETAILED MODEL AND NEURAL NETWORKS 

Hamed Nafisi - Mehrdad Abedi - Gevorg B. Gharehpetian *


#### Abstract

In a power transformer as one of the major component in electric power networks, partial discharge (PD) is a major source of insulation failure. Therefore the accurate and high speed techniques for locating of PD sources are required regarding to repair and maintenance. In this paper an attempt has been made to introduce the novel methods based on two different artificial neural networks (ANN) for identifying PD location in the power transformers. In present report Fuzzy ARTmap and Bayesian neural networks are employed for PD locating while using detailed model (DM) for a power transformer for simulation purposes. In present paper PD phenomenon is implemented in different points of transformer winding using threecapacitor model. Then impulse test is applied to transformer terminals in order to use produced current in neutral point for training and test of employed ANNs. In practice obtained current signals include noise components. Thus the performance of Fuzzy ARTmap and Bayesian networks for correct identification of PD location in a noisy condition for detected currents is also investigated. In this paper RBF learning procedure is used for Bayesian network, while Markov chain Monte Carlo (MCMC) method is employed for training of Fuzzy ARTmap network for locating PD in a power transformer winding and results are compared.


Keywords: Bayesian network, detailed model (DM), fuzzy ARTmap (FAM) neural network, partial discharge (PD), transformer

## 1 INTRODUCTION

Partial discharges (PD) are well known as a source of insulation degradation and the major sources for insulation failure in power transformers, which play important role in electric power system $[1,2]$. The capital cost of a power transformer is relatively high and economic penalty due to transformer failure and consequent outage is remarkable. Thus deterioration of insulated material caused by PD activity can be detected in early stage, then incipient insulation failure can be identified and preventive maintenance measures can be done [3]. PD detection technique is classified into acoustic and electrical methods. Electrical method is based on detecting of created impulses in the cavity of transformer insulation. Assessment of PD in electrical method is possible by using current transducers, which are connected to measuring terminals. In this method different procedures such as tip-up, dielectric loss analysing, inductive probes, pulse detecting and analysing, or other methods can be employed [4].

The advantage of acoustic relative to electrical technique for PD detection is its simplicity. However acoustic method has low sensitivity. On the other hand complicated structure of power transformer causes difficulty due to propagation velocity of acoustic waves associated with PD [5]. Therefore in recent years most reports are available concentrated on electrical methods [3-7]. Most of these reports deal with discharge between transformer winding and ground, and discharge between coil to coil has received little and incomplete attentions.

In this paper, partial discharge in the insulation between coil to coil is considered With EMTP simulation tools and DM of transformer. Then the current of neutral point of winding was measured when PD model was located at different positions in the winding and is used to finding location of PD using Fuzzy ARTmap neural network and Bayesian network. Simulated results must contain measurement noise for approximate to the truth. For mentioned reason in the last section simulated currents is changed to new one with considering measurement noise. Then the corrected currents are used for determination of the location of PD in transformer with aforesaid neural networks.

## 2 PARTIAL DISCHARGE MODEL

PD is localized ionization within insulator caused by high strength electric field. PD occurs in the part of insulation and is limited to some extends. Therefore PD does not cause full insulation breakdown immediately [4]. In this paper three-capacitor model shown in Fig. 1 is employed for PD modeling, which its accuracy is verified by EMTP software [5]. In this model we have

- $C_{g}$ is the capacitance of the region in which discharge occurs,
- $C_{b}$ is the capacitance of region located in series with $C_{g}$,
- $C_{a}$ is the capacitance of the other region in dielectric.

If discharge happens in $C_{g}$ a current $\left(I_{d}\right)$ flows from external terminals through $C_{a}$ and $C_{b}$.

[^0]
[^0]:    * Electrical Engineering Department, Amirkabir University of Technology, Tehran, No. 424, Hafez Ave, 15914, Tehran, Iran, nafisi@aut.ac.ir, abedi@aut.ac.ir, grptian@aut.ac.ir

![img-0.jpeg](img-0.jpeg)

Fig. 1. Three-capacitor model for PD
![img-1.jpeg](img-1.jpeg)

Fig. 2. DM of a two winding transformer

## 3 DETAILED MODEL

The equivalent circuit diagram of the test objects beyond 10 kHz is shown in Fig. 2. A winding unit can contain one disk, two disks or several numbers of turns. The number of units is a modeling parameter and the chosen value is a compromise between the accuracy and the complexity. For the sake of simplicity only three winding units of the double disk high voltage winding are shown in Fig. 2. Only one layer with three winding units have been shown for the low voltage winding in Fig. 2, too. This model is called detailed model [8].

The elements of the circuit diagram are defined in [8]. Using this model, it is possible to calculate node voltages
and branch currents in the time as well as in the frequency domain. Due to the frequency dependence behaviour of the resistive elements ( $R_{p i}, R_{e i}$ and $R_{s i}$ ) the calculation in the frequency domain is preferable.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Typical fuzzy ARTmap
Model parameters are calculated analytically after some simplifications of the geometrical structure of the winding. Determination of self inductance, mutual inductance, capacitances, and resistances is described in [8].

## 4 FUZZY ARTMAP NEURAL NETWORK

For the purpose of training and testing, in this paper Adaptive Resonance Theory (ART) neural networks have been used. In general, this family of neural networks include ART1, ART2 [9], ART3 [10], ARTmap [11], Fuzzy ART [12] and Fuzzy ARTmap [13]. ART1 and ARTmap categorize the binary input patterns while, Fuzzy ARTmap are also capable to categorize analogue patterns.

Fuzzy ARTmap is an incremental supervised learning algorithm which combines fuzzy logic and Adaptive Resonance Theory (ART) neural network for recognition of pattern categories and multidimensional maps in response to input vectors presented in an arbitrary order. It realizes a new minmax learning rule which conjointly minimizes predictive error and maximizes code compression, and therefore gives generalization. This is achieved by a match tracking process that increase the ART vigilance parameter (fuzzy degree of membership of the input with respect to the category templates) by the minimum amount needed to correct a predictive error (PE). The Fuzzy ARTmap neural network is composed of two Fuzzy ART modules [13], ie fuzzy $A R T_{a}$ and fuzzy $A R T_{b}$, which are depicted in Fig. 3 and are essentially the same as those described by Carpenter et al.

The interactions mediated by the map field $F^{a b}$ operationally characterized as follows.

### 4.1 ART $_{a}$ and ART $_{b}$

Inputs to $A R T_{a}$ and $A R T_{b}$ are in the complement code form: for $A R T_{a} I=A=\left(a, a^{c}\right)$ and for $A R T_{b}$ $I=B=\left(b, b^{c}\right)$ (See Fig. 3). Variables in $A R T_{a}$ or $A R T_{b}$ are designated by subscript " $a$ " and " $b$ " respectively. For $A R T_{a}$, let $x^{a}=\left\{x_{1}^{a}, \ldots, x_{2 M_{a}}\right\}$ denote the $F_{1}^{a}$ output vector, let $y^{a}=\left\{y_{1}^{a}, \ldots, y_{N_{a}}\right\}$ denote $F_{2}^{a}$, and let $w_{j}^{a}=$ $\left\{w_{j 1}^{a}, \ldots, w_{j 2 M_{a}}^{a}\right\}$ denote the $j^{\text {th }} A R T_{a}$ weight vector. For $A R T_{b}$, let $x^{b}=\left\{x_{1}^{b}, \ldots, x_{2 M_{b}}^{b}\right\}$ denote the $F_{1}^{b}$ output vector and let $y^{b}=\left\{y_{1}^{b}, \ldots, y_{N_{b}}^{b}\right\}$ denote $F_{2}^{b}$. And let $w_{k}^{b}=\left\{w_{k 1}^{b}, \ldots, w_{k 2 M_{b}}^{b}\right\}$ denote the $k^{\text {th }} A R T_{b}$ weight vector. For the map field, let $x^{a b}=\left\{x_{1}^{a b}, \ldots, x_{N_{a}}^{a b}\right\}$ denote the $F^{a b}$ output vector, and let $w_{j}^{a b}=\left\{w_{j 1}^{a b}, \ldots, w_{j N_{b}}^{a b}\right\}$ denote the weight vector from the $j^{\text {th }} F_{2}^{a}$ node to $F^{a b}$. Vectors $x^{a}, y^{a}, x^{b}, y^{b}$, and $x^{a b}$ are set to 0 between input presentations.

### 4.2 Map Field Activation

The map field $F^{a b}$ is activated whenever one of the $A R T_{a}$ or $A R T_{b}$ categories is active. If node $J$ of $F_{2}^{a}$ is chosen, then its weights $w_{j}^{a b}$ activate $F^{a b}$. If K in $F_{2}^{b}$ is active, then node $K$ in $F^{a b}$ is activated by one-toone pathways between $F_{2}^{b}$ and $F^{a b}$. If both $A R T_{a}$ and $A R T_{b}$ are active, then $F^{a b}$ becomes active only if $A R T_{a}$ predicts the same category as $A R T_{b}$ via the weights $w_{j}^{a b}$. The $F^{a b}$ output vector $x^{a b}$ obeys the following

$$
\left\{\begin{array}{cl}
y^{b} \wedge w_{j}^{a b} & \text { If the } j^{\text {th }} F_{2}^{a} \text { is active } \\
& \text { and } F_{2}^{b} \text { is active. } \\
w_{j}^{a b} & \text { If the } j^{\text {th }} F_{2}^{a} \text { is active } \\
& \text { and } F_{2}^{b} \text { is inactive. } \\
y^{b} & \text { If the } j^{\text {th }} F_{2}^{a} \text { is inactive } \\
& \text { and } F_{2}^{b} \text { is active. } \\
0 & \text { If the } j^{\text {th }} F_{2}^{a} \text { is inactive } \\
& \text { and } F_{2}^{b} \text { is inactive. }
\end{array}\right.
$$

From (1), $x^{a b}=0$ if the prediction $w_{j}^{a b}$ is disconfirmed by $y^{b}$. Even such a mismatch triggers and $A R T_{a}$ search for a better category, as follows.

### 4.3 Match Tracking

At the start of each input presentation, the $A R T_{a}$ vigilance parameter $\rho_{a}$ equals to baseline vigilance $\rho_{a}$. The map field vigilance parameter is $\rho_{a b}$

$$
\text { If } x^{a b}<\rho_{a b}|y^{b}|
$$

The $\rho_{a}$ is increased until it is slightly larger than $\left|A \wedge w_{j}^{a}\right||A|^{-1}$, where $A$ is the input to $F_{1}^{a}$, in complement coding form, and

$$
\left|x^{a}\right|=\left|A \wedge w_{j}^{a}\right|<\rho_{a}|A|
$$

where $J$ is the index of active $F_{2}^{a}$ node.
When this occurs, $A R T_{a}$ search leads either to activation of another $F_{2}^{a}$ node $J$ with

$$
\left|x^{a}\right|=\left|A \wedge w_{j}^{a}\right| \geq \rho_{a}|A|
$$

and

$$
\left|x^{a}\right|=\left|y^{b} \wedge w_{j}^{a b}\right| \geq \rho_{a}\left|y^{b}\right|
$$

Or, if no such nodes exist, ie the input pattern to $F_{2}^{a}$ layer does not match any pattern: the input pattern is classified as a new pattern.

### 4.4 Testing of Network

In this testing method, neural network have no surveillance on foreseen output. This means for each patterns of inputs one pattern is offered in output and this proffer downright after passing from condition (minimum error with existing output patterns) is accomplished which is caused faster response but reduction in precision because errors may so classified that clusters are sorely close to each other. In these cases resemblance of estimated pattern to each output pattern may cause accuracy descend in estimation, thereupon existence probability of error is considered.

Block diagram of accustomed testing method is shown in Fig. 4.

Also test algorithm for FAM network is depicted is Fig. 5.

## 5 FUNDAMENTAL OF BAYESIAN NETWORK

Bayesian networks are usually used to model the situations (eg, medical diagnosis) in which causality plays a role but where the understanding of what is actually going on is incomplete. That is, a Bayesian network for the domain represents a joint probability distribution over a set of variables (ie, chance nodes) [14].

Bayesian network is a directed acyclic graph that consists of single-evidence, multiple-evidence, and multiplelayer probabilistic relationships among the variables. For detailed description about DAGs see [15]. Thus, Bayesian network expresses the global joint distribution with a set of local distributions and relates only the neighboring nodes. Figure 6 illustrates the basic structure of a Bayesian network.

The Bayesian network has been successfully applied in many fields such as medical diagnosis [16], equipment diagnosis [17], and mineral exploration [18]. Extensive review of Bayesian networks can be found, for example, in [19].

The Bayesian network is a directed acyclic graph in which the following holds.

- A set of random variables makes up the nodes of the network.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Typical fuzzy ARTmap test method
![img-4.jpeg](img-4.jpeg)

Fig. 5. Algorithm of FAM network test method
![img-5.jpeg](img-5.jpeg)

Fig. 6. Basic structures of Bayesian network (DAG) [15]

- A set of directed links or arrows connects pairs of nodes.
- Each node has a conditional probability table that quantifies the effects that the parents have on the node. The parents of a node are all those nodes that have arrows pointing to it.
- The graph has no directed cycles (hence is a directed, acyclic graph or DAG).
A Bayesian network provides a complete description of the domain. Every entry in the joint probability distribution can be calculated from the information in the network. A generic entry in the joint is the probability of a conjunction of particular assignments to each variable. The value of this entry is given by [20]

$$
P\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{n} P\left(x_{i} \mid \operatorname{parents}\left(X_{i}\right)\right)
$$

We use the notation $P\left(x_{1}, \ldots, x_{n}\right)$ as an abbreviation for this. Thus, each entry in the joint is represented by the product of the appropriate elements of the conditional probability tables (CPTs) in the belief network. The CPTs therefore provide a decomposed representation of the joint.

$$
\begin{aligned}
& P\left(x_{1}, \ldots, x_{n}\right)= \\
& P\left(x_{n} \mid x_{n-1}, \ldots, x_{1}\right) P\left(x_{n-1} \mid x_{n-2}, \ldots, x_{1}\right) \ldots P\left(x_{1}\right)= \\
& \prod_{i=1}^{n} P\left(x_{i} \mid x_{i-1}, \ldots, x_{1}\right)
\end{aligned}
$$

Then we repeat this process, reducing each conjunctive probability to a conditional probability and a smaller conjunction. We end up with one big product. Comparing this with Equation (6) and (7), we see that the specification of the joint is equivalent to the general assertion that.

### 5.1 Markov Chain Monte Carlo Blanket

A node is conditionally independent of its non-descendants, given its parents. A node is conditionally independent of all other nodes in the network, given its parents, children, and children's parents that is, given its Markov blanket.

From these conditional independence assertions and the CPTs, the full joint distribution can be reconstructed; thus, the "numerical" semantics and the "topological" semantics are equivalent.

According to the theory of Markov blanket, the nodes for inference, such as the fault node or protection node, are chosen first.

### 5.2 The MCMC Algorithm

The MCMC generates each event by making a random change to the preceding event. It is therefore helpful to think of the network as being in a particular current

state specifying a value for every variable. The next state is generated by randomly sampling a value for one of the non-evidence variables Xi , conditioned on the current values of the variables in the Markov blanket of $X_{i}$. MCMC therefore wanders randomly around the state space-the space of the possible complete assignments-flipping one variable at a time, but keeping the evidence variables fixed. The algorithm is that:

Let $q\left(x \rightarrow x^{\prime}\right)$ be the probability that the process makes a transition from states $x$ to state $x^{\prime}$. This transition probability defines what is called a Markov chain on the state space. Now suppose that we run the Markov chain for $t$ steps, and let $P_{t}(x)$ be the probability of being in state $x$ at time $t$. Similarly, let $P_{t+1}\left(x^{\prime}\right)$ be the probability of being in state $x^{\prime}$ at time $t+1$. Given $P_{t}(x)$, we can calculate $P_{t+1}\left(x^{\prime}\right)$ by summing, for all states the system could be in at time $t$, the probability of being in that state times the probability of making the transition to $x^{\prime}$

$$
P_{t+1}\left(x^{\prime}\right)=\sum_{x} P_{t}(x) q\left(x^{\prime} \rightarrow x\right)
$$

We will say that the chain has reached its stationary distribution if $P_{t}(x)=P_{t+1}\left(x^{\prime}\right)$. Let us call this stationary distribution $P$; its defining equation is therefore

$$
P\left(x^{\prime}\right)=\sum_{x} P(x) q\left(x^{\prime} \rightarrow x\right) \quad \text { for all } x^{\prime}
$$

Under certain standard assumptions about the transition probability distribution $q$, there is exactly one distribution $P$ satisfying this equation for any given $q$.

Equation (8) can be read as saying that the expected "outflow" from each state (ie, its current "population") is equal to the expected "inflow" from all the states. One obvious way to satisfy this relationship is if the expected flow between any pair of states is the same in both directions. This is the property of detailed balance

$$
P\left(x^{\prime}\right) q\left(x \rightarrow x^{\prime}\right)=\sum_{x} P(x) q\left(x^{\prime} \rightarrow x\right) \text { for all } x, x^{\prime}
$$

### 5.3 Radial Basis Function (RBF)

In order to assess the input data Radial Basis Function (RBF) method is used. A radial basis function (RBF) is a real-valued function whose value depends only on the distance from the origin, so that [21]

$$
\varphi(x)=\varphi(\|x\|)
$$

Or alternatively on the distance from some other point $c$, called a center, so that

$$
\varphi(x, c)=\varphi(\|x-c\|)
$$

Any function $\varphi$ that satisfies the property $\varphi(x)=$ $\varphi(\|x\|)$ is a radial function. The norm is usually Euclidean distance.

Radial basis functions are typically used to build up function approximations of the form

$$
y(x)=\sum_{i=1}^{N} \omega_{i} \varphi\left(\left\|x-c_{i}\right\|\right)
$$

where the approximating function $y(x)$ is represented as a sum of $N$ radial basis functions, each associated with a different center $c_{i}$, and weighted by an appropriate coefficient $\omega_{i}$. Approximation schemes of this kind have been particularly used in time series prediction and control of nonlinear systems exhibiting sufficiently simple chaotic behaviour.

The sum can also be interpreted as a rather simple single-layer type of artificial neural network called a radial basis function network, with the radial basis functions taking on the role of the activation functions of the network. It can be shown that any continuous function on a compact interval can in principle be interpolated with arbitrary accuracy by a sum of this form, if a sufficiently large number N of radial basis functions is used.

There are some commonly used types of radial basis functions include $r=\left\|x-c_{i}\right\|$.

- Gaussian

$$
\varphi(r)=\exp \left(-\beta r^{2}\right) \text { for some } \beta>0
$$

- Multi-quadric

$$
\varphi(r)=\sqrt{r^{2}+\beta^{2}} \quad \text { for some } \beta>0
$$

- Polyharmonic spline

$$
\varphi(r)=\left\{\begin{array}{ll}
r^{k}, & k=1,3,5, \ldots \\
r^{k} \ln r, & k=2,4,6 \ldots
\end{array}\right.
$$

- Thin plate spline (a special polyharmonic spline)

$$
\varphi(r)=r^{2} \ln r
$$

These polyharmonic splines (which include the thinplate spline) minimise certain energy semi-norms and are therefore the "smoothest" interpolators. Note that the associated basic functions are not compactly supported - they grow as $r$ increases from the origin.

RBFs are popular for interpolating scattered data as the associated system of linear equations is guaranteed to be invertible under very mild conditions on the locations of the data points. For example, the thin-plate spline only requires that the points are not co-linear while the Gaussian and multi-quadric place no restrictions on the locations of the points. In particular, RBFs do not require that the data lie on any sort of regular grid.

In this paper Radial Basis Function method with Gaussian type is considered for assessment of data which is depicted in Fig. 7.

![img-6.jpeg](img-6.jpeg)

Fig. 7. Un-normalized radial basis functions with $c_{1}=0.75$ and $c_{2}=3.25$

### 5.4 Estimating the Weights

The approximant $y(x)$ is differentiable with respect to the weights $\omega_{i}$. The weights could thus be learned using any of the standard iterative methods for neural networks. But such iterative schemes are not in fact necessary because the approximating function is linear in the weights $\omega_{i}$, the $\omega_{i}$ can simply be estimated directly, using the matrix methods of linear least squares.

The input assessment has been shown in this section. In the next section required input-output data and modeling of power system will be presented.

## 6 CASE STUDY

DM of transformer is used for simulation PD mechanism in EMTP and this PD model is considered between coil to coil, as mentioned in previous sections.

### 6.1 Transformer Specification

The used transformer is $35 \mathrm{kV} / 220 \mathrm{kV}$ and 50 MVA . Windings dimensions and model of the transformer tank are detailed in [4].

HV winding of the simulating transformer consist of 56 discs. The first 6 two-discs is interleaved type and the 22 other two-disc is inverted type. Dimensions of all twodiscs are presented in Tab. 1.

Table 1. Technical Specification of HV Winding


![img-7.jpeg](img-7.jpeg)

Fig. 8. Current waveform in neutral point resulting from PD model in 1st node of DM

Table 2. Results of neural network testing


### 6.2 simulation Results

PD model is placed in different points of the winding and steep impulse current applied to the winding as input signal. The current at the other terminal is measured as output. Produced current in neutral point of the winding is recorded. For instance Figs. 8, 9 and 10 show the current in neutral point of the winding when PD in two-disk 1,18 and 28 was modelled, respectively.

### 6.3 Test result of Fuzzy ARTmap Neural Network

In order to train the neural networks there is a need for measured training patterns. The current neutral point is used for learning of Fuzzy ARTmap neural network. This neural network is implemented in MATLAB software. Used DM consists of 28 nodes. Thus all simulated states are 28 . For training of neural network 22 of them is used. This low number of data sets is because of the EMTP limitation for number of the mutual inductances.

As mentioned, necessary simulations of transformer are done in EMTP and the results used for input data for the Fuzzy ARTmap neural network in MATLAB. Result of the Fuzzy ARTmap neural network testing is shown in Tab. 2.

As it is shown in Tab. 2, the best PD location accuracy is reached to 100 for 0.93 of training rate, 0.95 for mapfield vigilance parameters. The obtained number of

![img-8.jpeg](img-8.jpeg)

Fig. 9. Current waveform in neutral point resulting from PD model in 18th node of DM

Table 3. Results of neural network testing with noise

|  Training
rate | Vigilance
parameter | Num. of
clusters | Accuracy
$(\%)$  |

Table 4. Results of Bayesian Network

|  PD located
in | Output of
Bayesian network | Rounded
value  |

clusters is 89 . The reason of this matter is lack of the parameters which are used for training and test of Fuzzy ARTmap neural network because of EMTP limitation. But because of sufficient difference among current waveform Fuzzy ARTmap neural network can determine the correct position of PD in power transformer.

With regard to this point that in truth and actual measured current waveforms contain measurement noise and different from simulated values, white noise is added to simulated currents. Amplitude of the white noise considered form 1 to 10 percent of peak value of simulated current amplitude in 1 percent steps. Therefore, neural network response to noisy inputs with best training rate and mapfield vigilance parameters, obtained from Tab. 2, is shown in Tab. 3.

According to Tab. 3, accuracy of Fuzzy ARTmap neural network with considering noise is about $86.2 \%$. The best output of FAM network is a network with vigilance parameter equal to 0.95 and training rate of 0.93 .

### 6.4 Test result of Bayesian Network

In Bayesian network such as FAM neural network, EMTP software is used for simulations of the transformer. The obtained current waveforms used for input data for the Bayesian network in MATLAB. Some result of the Bayesian network test result is shown in Tab. 4. ![img-9.jpeg](img-9.jpeg)

Fig. 10. Current waveform in neutral point resulting from PD model in 28th node of DM

As it is shown in Tab. 2, a wide range of outputs are similar to the targets and if the output of the Bayesian network round, the best PD location accuracy is reached. As the result of the simulation, Bayesian network has $100 \%$ accuracy for determination of partial discharge location as FAM neural network.

Actually measured currents have measurement noise component and is not identical as the simulated values, hence white noise is added to simulated current waveforms. Amplitude of the white noise considered form 1 to 10 percent of peak value of simulated current amplitude in 1 percent steps. Accuracy of this network is 91 percent which is better than FAM network. The excellence of Bayesian network respect to FAM neural network is the better accuracy to finding the PD location in power transformer with presence of measurement noise.

## 7 CONCLUSION

In this paper Fuzzy ARTmap neural network and Bayesian network are proposed for locating of PD in power transformers winding. DM of transformer is used for PD simulation in EMTP and three-capacitor PD model is considered between coil to coil of power transformer winding. A study on DM parameters selection is presented in this paper and the results show highly dependency of results and prediction of PD location to these parameters. It has been shown that Fuzzy ARTmap neural network response to the signals with considering noise is acceptable and the results have good accuracy. But Bayesian network have better accuracy in noisy environment. These methods can be used as a general solution for locating of partial discharge in power transformers, provided the parameters value of detailed model of transformers to be selected truely.
