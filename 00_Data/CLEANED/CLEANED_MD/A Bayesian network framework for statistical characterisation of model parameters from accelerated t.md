# HIAL open science 

## Bayesian Network Framework for Statistical Characterisation of Model Parameters from Accelerated Tests: Application to Chloride Ingress Into Concrete <br> Thanh-Binh Tran, Emilio Bastidas-Arteaga, Franck Schoefs, Stéphanie Bonnet

## To cite this version:

Thanh-Binh Tran, Emilio Bastidas-Arteaga, Franck Schoefs, Stéphanie Bonnet. Bayesian Network Framework for Statistical Characterisation of Model Parameters from Accelerated Tests: Application to Chloride Ingress Into Concrete. Structure and Infrastructure Engineering, 2017, $10.1080 / 15732479.2017 .1377737$. hal-01583276

## HAL Id: hal-01583276 <br> https://hal.science/hal-01583276v1

Submitted on 7 Sep 2017

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Bayesian Network Framework for Statistical Characterisation of Model Parameters from Accelerated Tests: Application to Chloride Ingress Into Concrete 

Thanh-Binh Tran, Emilio Bastidas-Arteaga, Franck Schoefs, Stéphanie Bonnet

UBL, University of Nantes, Institute for Research in Civil and Mechanical Engineering/Sea and Littoral Research Institute, CNRS UMR 6183/FR 3473, Nantes, France

Corresponding author (E. Bastidas-Arteaga): 2 rue de la Houssinière BP 99208, 44322 Nantes Cedex 3 France. +33 2511255 24. emilio.bastidas@univ-nantes.fr


#### Abstract

This paper addresses the topic of long-term characterisation and probabilistic modelling of chloride ingress into reinforced concrete (RC) structures. Since the corrosion initiation stage may cover various decades, normal tests which simulate chloride penetration into concrete in laboratory conditions as the same as natural conditions, will require significant experimental times. Hence, long-term lifetime assessment of RC structures under chloride attack remains still a challenge. In practice this problem is solved through the use of accelerated tests which speed up the chloride ingress rate and provide valuable mid- and long-term information on the chloride penetration process. Nevertheless, this information cannot be directly used for parameter statistical characterisation if the equivalent times required in natural conditions to reach the same chloride concentrations in the accelerated tests are unknown. Consequently, this study proposes a novel iterative approach based on Bayesian network updating to estimate chloride ingress model parameters from the data obtained under accelerated laboratory conditions. The Bayesian Network structure and iterative approach are first tested with numerical evidences. Thereafter, the complete proposed methodology is verified with results from real experimental measurements. The results indicate that combining data from normal and accelerated tests significantly reduces the statistical characterisation error of model parameters.


Keywords: Accelerated Test; Reinforced Concrete; Corrosion; Bayesian Network; Statistical Characterisation; Random Variable

## 1. Introduction

Chloride ions have been frequently considered as the main cause of deterioration of various types of reinforced concrete (RC) structures located in marine environments or in contact with de-icing salts (Salta, Melo, Ricardo, \& Póvoa, 2012; Shekarchi, MoradiMarani, \& Pargar, 2011). Reinforcement corrosion induced by penetrating chlorides will result in loss of bond between steel and concrete, concrete cracking and concrete delamination and eventually in a reduction of the loading capacity of structures through the loss of reinforcement cross-section. Consequently, planning maintenance strategies

that minimise the impacts of corrosion becomes an essential task for minimising costs, failure risks and environmental impact (Bastidas-Arteaga \& Schoefs, 2015; Faustino, Chastre, Nunes, \& Brás, 2016; Lounis \& Daigle, 2013).

In the management of deteriorating RC structures generally a distinction can be made between inspection and decision making (do nothing, repair or replacement). Inspection data provide valuable information on the damage condition of RC structures under chloride attack. Based on these data, appropriate repair actions may be undertaken at allowed deterioration conditions. In addition, model parameters characterising material durability or environmental exposure could be identified from inspection measurements. These parameters, combined with chloride ingress models, are useful to: (i) update service life prediction models and costs (Samarakoon \& Sælensminde, 2015), and (ii) optimise inspection campaigns (Bastidas-Arteaga \& Schoefs, 2012; Sánchez-Silva \& Klutke, 2016); however, long-term results of the above mentioned applications are often influenced by:
(1) Uncertainties in the chloride ingress process: these uncertainties are mainly related to material properties and exposure conditions (Chiu, Tu, \& Zhuang, 2016; Deby, Carcasses, \& Sellier, 2008; Marano, Quaranta, Sgobba, Greco, \& Mezzina, 2010). They are also influenced by temporal and spatial variability of associated deterioration processes (Peng \& Stewart, 2016; Schoefs, BastidasArteaga, Tran, Villain, \& Derobert, 2016).
(2) Lack of inspection data: time-consuming and expensive destructive tests are necessary to determine the evolution of chloride concentration in time by limiting the quantity of data available in each inspection campaign. Despite a large number of non-destructive inspection techniques have been developed to facilitate the assessment of risks related to reinforcement corrosion, these techniques are still expensive, time-consuming and require specific posttreatment methods (Lecieux, Schoefs, Bonnet, Lecieux, \& Lopes, 2015; Ploix, Garnier, Breysse, \& Moysan, 2011; Torres-Luque, Bastidas-Arteaga, Schoefs, Sánchez-Silva, \& Osma, 2014). If additional inspection and testing works are carried out to provide sufficient data for probabilistic condition assessment, the extra costs need to be considered (Gehlen et al., 2011).
(3) Time-dependencies and chloride ingress kinetics: since concrete transport properties vary with time and the chloride ingress is slow, comprehensive midand long-term assessment should be based on late inspection times. However, deterioration rates will be higher at late inspection times increasing corrective maintenance costs.

To deal with uncertainty related issues, Bayesian approach is a suitable tool that can integrate new information for updating the estimations. This kind of technique is proposed by Fib bulletin 59 (Gehlen et al., 2011) for updating statistical distribution parameters in chloride ingress and planning future inspection campaigns. For multievents problems, it turns in the form of Bayesian Network (BN) to model relationships between random variables. BN has been previously applied for probabilistic modelling of chloride and carbonation-induced corrosion. Deby, Carcasses, \& Sellier $(2008,2012)$ have used BN for the assessment of the probabilistic distribution of random variables in the chloride diffusion problem. Tesfamariam \& Martín-Pérez (2008) have proposed a Bayesian Belief Network that is able to consider qualitative and quantitative information for carbonation-induced corrosion assessment. These approaches seem to be robust when allowing the possibility to update the statistical distributions with new qualitative or experimental information. Hackl (2013) proposed a framework that

combines structural analysis and BN for reliability assessment. This combination allows Bayesian updating of the model with measurements, monitoring and inspection results. Ma, Wang, Zhang, Xiang \& Liu (2014) developed a BN combining in situ load testing to predict the strength degradation of bridge structures subjected to chloride attack. Nevertheless, the abovementioned studies have not optimised the utilisation of inspection data, especially when the information is scarce. Tran, Bastidas-Arteaga \& Schoefs (2016a, 2016b) proposed an approach to identify random parameters in chloride ingress models from limited inspection data. The robustness of this approach lies on taking into consideration uncertainties in a probabilistic framework from inspection data. However, these studies did not consider time-dependencies of material properties and they require inspection data measured at various exposure times to reduce statistical characterisation errors.

Time-dependencies and chloride ingress kinetics issues could be answered by: (i) employing more advanced chloride ingress models that consider time-dependent model parameters, and (ii) using inspection data obtained from accelerated tests for parameter statistical characterisation. In general, accelerated data are obtained by performing experiments at higher stress levels. These data could be useful for further applications (reliability analysis or parameter statistical characterisation) if they can be translated to normal conditions. Several studies have been devoted to calibrate the accelerated tests and their data (Volf \& Timková, 2014; Wang, Pan, Li, \& Jiang, 2013) and to use this information for lifetime or reliability assessment (Haghighi, 2014; Liao \& Elsayed, 2006). In specific applications on RC degradation processes, Neves, Branco, \& De Brito (2013) established the relationship between accelerated and natural carbonation coefficients using a regression method. However, the limitation of this approach is that it did not account for the uncertainty in the carbonation process. Duprat, Vu \& Sellier (2014) developed a probabilistic framework based on a BN approach to integrate the accelerated data for designing the cover of concrete structures under carbonation exposure. This study was based on a comprehensive carbonation model able to incorporate directly the accelerated data to improve lifetime assessment. However, it is difficult to extend this approach to other deterioration processes because it is not always possible to adequately model the accelerated conditions.

Within this context, this study proposes a novel approach to derive chloride ingress model parameters from the data obtained in accelerated laboratory conditions. This approach combines BN with an iterative approach for uncertainty propagation and statistical characterisation purposes. Section 2 presents the BN used for modelling chloride ingress that accounts for concrete ageing through an age factor. Section 3 performs a sensitivity analysis on the effect of the age factor on parameter statistical characterisation. Section 4 presents the construction of a BN configuration combining data from normal and accelerated tests for parameter statistical characterisation. Normal tests simulate chloride penetration into concrete as in natural conditions; accelerated tests speed up the chloride ingress rate and provide valuable mid- and long-term information on the chloride penetration process. Finally, Section 5 details the experimental setup and the proposed approach for statistical characterisation of model parameters from real data coming from normal and accelerated tests.

# 2. BN for identifying chloride ingress model parameters 

### 2.1 Introduction to BN

BN is Direct Acyclic Graph (DAG) consisting of a set of nodes that are connected by

edges to illustrate their dependencies. Nodes in BN are a graphical representation of objects and events that exist in the real world and can be modelled as continuous or discrete random variables. To each child node with its parents is assigned a conditional Probability Density Function (PDF), $f(X \mid \mathbf{p a}(X))$ or Probability Mass Function (PMF), $p(x \mid \mathbf{p a}(X))$, where $\mathbf{p a}(X)$ are the parents of $X$ in the DAG (Stewart, 2011). An edge may represent causal relationships between the variables (nodes) but this is not a requirement. The graphical structure of a BN encodes conditional independence assumption among the random variables. Hence, a BN is a compact model representing the joint PDF or PMF among random variables. In this study, only BNs with discrete random variables are considered. Figure 1 illustrates a simple BN that consists of three nodes representing three discrete random variables $X_{1}, X_{2}$ and $X_{3}$ in which $X_{2}$ and $X_{3}$ are children of the parent node X1. For each node in the BN, its PMF defines conditional dependences on its parents and the joint PMF of the BN presented in Figure 1 is formed as a product of these conditional probabilities:

$$
P\left(X_{1}, X_{2}, X_{3}\right)=P\left(X_{1}\right) P\left(X_{2} \mid X_{1}\right) P\left(X_{3} \mid X_{1}\right)
$$

where $\mathrm{P}\left(X_{i} \mid X_{j}\right)$ denotes the conditional probability of $X_{i}$ given $X_{j}$.
BN allows introducing new information (evidences) from the observed nodes to update the probabilities in the network. For example, if we have some evidences $o$ to introduce to node $X_{2}\left(X_{2}=o\right)$, this information propagates through the network and the joint PMF of the two other nodes can be recalculated as:

$$
P\left(X_{1}, X_{2} \mid o\right)=\frac{P\left(X_{2}, o, X_{3}\right)}{P(o)}=\frac{P\left(X_{1}\right) P\left(o \mid X_{1}\right) P\left(X_{3} \mid X_{1}\right)}{\sum_{i} P\left(X_{i}\right) P\left(o \mid X_{1}\right)}
$$

Therefore, the a posteriori probabilities of $X_{1}$ and $X_{3}$ are updated and Eq. (2) becomes the key of parameter statistical characterisation from inspection data. It is assumed that the marginal probability $P\left(X_{1}\right)$ is the parameter of interest, then both exact and approximate inference algorithms are available for such computation. However, to illustrate the principle of exact inference which is used later in this paper, this probability can be derived from the joint PMF of the BN as follows:

$$
\begin{aligned}
P\left(X_{1}\right) & =\sum_{X_{2}, X_{3}} P\left(X_{1}, X_{2}, X_{3}\right) \\
& =\sum_{X_{2}, X_{3}} P\left(X_{1}\right) P\left(X_{2} \mid X_{1}\right) P\left(X_{3} \mid X_{1}\right) \\
& =P\left(X_{1}\right) \sum_{X_{2}} P\left(X_{2} \mid X_{1}\right) \sum_{X_{3}} P\left(X_{3} \mid X_{1}\right)
\end{aligned}
$$

The summation operations in the third line of Eq. (3) are performed in smaller domains and imply node eliminations. The calculation order starts from the last term in the right to the left, hence $X_{3}$ is the first node to eliminate followed by node $X_{2}$. Elimination order is arbitrary and the size of the domains to handle due to elimination order defines the complexity of inference. Therefore, the objective of exact inference algorithms is to determine the elimination order that yield the smallest domains to handle (Jensen \& Nielsen, 2007). Among exact inference algorithms, junction tree inference which can be seen as an extension of node elimination, can compute the a posteriori probabilities for all nodes in a BN simultaneously and consider multiple evidences cases. The junction tree algorithm is selected for inference of all BN in this paper.

# 2.2 Chloride ingress model 

Chloride penetration from the environment produces a chloride concentration profile in the concrete characterised by a high chloride concentration near the external surface that decreases at greater depths. In saturated concrete, Fick's diffusion equation is generally used to predict the unidirectional diffusion at a distance $x$ from the concrete surface:

$$
\frac{\partial C_{f_{c}}}{\partial t}=D \frac{\partial^{2} C_{f_{c}}}{\partial x^{2}}
$$

where $C_{f c}$ is the concentration of chloride dissolved in pore solution, $t$ is the time and $D$ is the chloride diffusion coefficient. Let us assume that concrete is a homogeneous and isotropic material with the following initial conditions: (1) the chloride concentration is zero at time $t=0$ and (2) the chloride surface concentration is constant for $t \geq 0$. The free chloride ion concentration $C(x, t)$ at depth $x$ after time $t$ for a semi-infinite medium could therefore be expressed by an analytical solution to Fick's equation using the error function (Collepardi, Marciallis, \& Turriziani, 1972):

$$
C(x, t)=C_{s}\left[1-\operatorname{erf}\left(\frac{x}{2 \sqrt{D_{a} t}}\right)\right]
$$

where $C_{s}$ is the chloride surface concentration, and $D_{a}$ is the apparent chloride diffusion coefficient and $\operatorname{erf}($.$) is the error function. Eq. (5) is used to calculate the chloride$ concentration at depth $x$ and given time $t$. This relation describes theoretically the kinetics of a non-stationary diffusion process. However, Eq. (5) is just valid when RC structures are completely saturated and subjected to a constant concentration of chlorides on the exposed surface. However, in practice these conditions are rarely present because concrete is a heterogeneous material that is frequently exposed to timevariant surface chloride concentrations. Under natural conditions, chloride ingress is a more complex process influenced by other aspects such as: chloride binding capacity, concrete cracking, concrete ageing, environmental factors (temperature and humidity), etc. (Bastidas-Arteaga, Sánchez-Silva, Chateauneuf, \& Ribas Silva, 2008; BastidasArteaga \& Stewart, 2016; Nguyen, Bastidas-Arteaga, Amiri, \& El Soueidy, 2017).

Although some assumptions are oversimplified, error function models are widely used by practical applications due to their relatively simple mathematical expressions. The simplest error function model represented by Eq. (5), which treats the chloride diffusion coefficient as constant in time and space, has been proven to be conservative due to the lack of consideration of the retarding effect on the diffusion process resulting from chloride binding and the refinement of the pore structure over time (Nilsson \& Carcasses, 2004). In a more advanced model, the chloride diffusion coefficient is modelled as time-variant following an exponential function (Tang \& Gulikers, 2007) :

$$
D(t)=D_{0}\left(\frac{t}{t_{0}}\right)^{-n_{D}}
$$

where $D_{0}$ is the chloride diffusion coefficient determined at time $t_{0}$, and $n_{D}$ is the age factor that takes into consideration the time-dependency of $D$. Some models considering a time-variant chloride diffusion coefficient may lead to overestimated predictions of service life when the age factor is high (Tang \& Gulikers, 2007). The model proposed by Nilsson \& Carcasses, (2004) accounts for this time-dependent effect in a more realistic way and gives a relatively better prediction:

$$
C(x, t)=C_{s}\left[1-\operatorname{erf}\left(\frac{x}{2 \sqrt{\frac{D_{0}}{1-n_{D}}\left[\left(1+\frac{t_{e x}}{t}\right)^{1-n_{D}}-\left(\frac{t_{e x}}{t}\right)^{1-n_{D}}\left\|\frac{t_{0}}{t}\right\|^{n_{D}} t\right.}}\right]\right]
$$

where $t_{e x}$ is the age of concrete at the start of exposure. This equation is valid only under these assumptions: (1) concrete is a homogeneous material, (2) chloride binding is time-independent and linearly proportional to the free chloride concentration, (3) the effect of co-existing ions is constant, and (4) the chloride diffusion is one-dimensional into a semi-infinite space. Despite some physical phenomena have been neglected, this model is selected for illustrative purposes. In comparison with Eq. (5), the timedependency of $D$ considered by Eq. (7) is essential to introduce information from accelerated tests for characterising the mid- and long-term performance of the material. The methodology proposed in this paper could be extended for other chloride ingress models.

# 2.3 BN for modelling chloride ingress 

In chloride ingress models, the chloride concentration $C\left(x_{i}, t_{j}\right)$ at depth $x_{i}$ and time $t_{j}$ can be described as a general function of model parameters (Eq. (8)). The number of parameters involved in the right-hand side of Eq. (8) depends on the model selected to describe the chloride ingress. This study uses the model proposed in Nilsson \& Carcasses, (2004) (Eq. (7)) that depends on three parameters ( $C_{s}, D_{0}$ and $n_{D}$ ).

$$
C\left(x_{i}, t_{i}\right)=f\left(C_{s}, D_{0}, n_{D}, \ldots\right)
$$

The BN representing the chloride ingress model given by Eq. (7) is described in Figure 2. Three model parameters ( $C_{s}, D_{0}$ and $n_{D}$ ) are defined as three parent nodes (random variables to identify) whereas chloride concentrations $C\left(x_{i}, t_{j}\right)$ at depth $x_{i}$ and at inspection time $t_{j}$, which depend on the model parameters, are acting as child nodes. There are $n$ child nodes $C\left(x_{i}, t_{j}\right), 1 \leq i \leq n_{x}, 1 \leq j \leq n_{t}$ representing the discrete chloride concentration measurements in time and space. For a homogeneous inspection, i.e. when using the same protocol of inspection at each time, the number of child nodes is computed as:

$$
n=n_{x} n_{t}
$$

where $n_{x}$ is the total number of points in depth and $n_{t}$ is the total number of inspection times.

Both exact and approximate inference algorithms can be used to update probabilities of the BN described in Figure 2. Exact inference is useful to analytically compute the conditional probability distribution over the variables of interest. However, they can only be applied to a very limited set of cases: when all nodes are discrete or when all nodes have a linear Gaussian distribution. In the case of complex and densely connected BNs, exact inference may require an extremely long computational time and approximate inference can then be seen as an attractive alternative. Most approximate algorithms are based on stochastic sampling. However, these techniques still have some algorithmic difficulties that provide some limitations in the rate of convergence (Bensi, Der Kiureghian, \& Straub, 2011; Straub, 2009). In this study, chloride ingress model is described in an analytical form and the number of parent nodes (parameters to identify) is limited. Exact inference algorithms therefore could be applied here regarding their shortcomings. Continuous parameters are then replaced by discrete random variables.

The discretisation of continuous random variables generates approximation errors depending on the discretisation of the problem (Straub, 2009). However the effect of the discretisation errors is beyond the scope of this study. The probability of chloride concentration $p\left(C\left(x_{i}, t_{j}\right)\right)$ can be calculated as follows:

$$
p\left(C\left(x_{i}, t_{j}\right)\right)=\sum_{C_{s}, D_{0}, n_{D}} p\left(C\left(x_{i}, t_{j}\right) \mid C_{s}, D_{0}, n_{D}\right) p\left(C_{s}, D_{0}, n_{D}\right)
$$

Assuming that $C_{s}, D_{0}$ and $n_{D}$ are three independent variables, the joint probability of $C_{s}, D_{0}$ and $n_{D}$ can be written as: $p\left(C_{s}, D_{0}, n_{D}\right)=p\left(C_{s}\right) p\left(D_{0}\right) p\left(n_{D}\right)$.

The BN allows updating the probabilities in the network when new information is available (evidences). In the BN given in Figure 2, the evidences could be computed from measurements of chloride concentration at given depths and times (chloride profiles). Let us denote $C x t_{1}, C x t_{2}, \ldots, C x t_{n}$ as $n$ measurements obtained at depth $x_{i}$ and inspection time $t_{j}: C\left(x_{i}, t_{j}\right)$. The joint probability mass function of the BN presented in

Figure 2 can be written in the form:

$$
p\left(C_{s}, D_{0}, n_{D}, C x t_{1}, \ldots, C x t_{n}\right)=p\left(C x t_{1} \mid C_{s}, D_{0}, n_{D}\right) \ldots p\left(C x t_{n} \mid C_{s}, D_{0}, n_{D}\right) p\left(C_{s}\right) p\left(D_{0}\right) p\left(n_{D}\right)
$$

where the conditional probabilities $p\left(C x t_{l} \mid C_{s}, D_{0}, n_{D}\right), \ldots, p\left(C x t_{n} \mid C_{s}, D_{0}, n_{D}\right)$ can be derived from the Conditional Probability Tables (CPT). Monte Carlo simulations are used to compute the CPT based on Eq. (7). Supposing that $k$ observations: $C x t_{l}$, $C x t_{2}, \ldots, C x t_{k}$ are used to update the BN , we aim at computing the a posteriori distributions: $p\left(C_{s} \mid o\right), p\left(D_{0} \mid o\right)$ and $p\left(n_{D} \mid o\right)$ as:

$$
\begin{aligned}
& p\left(C_{s} \mid o\right)=\sum_{D_{0}, n_{D}} p\left(C_{s}, D_{0}, n_{D} \mid o\right) ; p\left(D_{0} \mid o\right)=\sum_{C_{s}, n_{D}} p\left(C_{s}, D_{0}, n_{D} \mid o\right) \\
& \text { and } p\left(n_{D} \mid o\right)=\sum_{C_{s}, D_{0}} p\left(C_{s}, D_{0}, n_{D} \mid o\right)
\end{aligned}
$$

where

$$
p\left(C_{s}, D_{0}, n_{D} \mid o\right)=p\left(C_{s}, D_{0}, n_{D} \mid C x t_{1}, \ldots, C x t_{k}\right)=\frac{p\left(C_{s}, D_{0}, n_{D}, C x t_{1}, \ldots, C x t_{k}\right)}{p\left(C x t_{1}, \ldots, C x t_{k}\right)}
$$

These a posteriori distributions can be estimated by marginalising the joint distribution in Eq. (11) to obtain the joint distribution over the subsets of the variables:

$$
p\left(C_{s}, D_{0}, n_{D}, C x t_{1}, \ldots, C x t_{k}\right)=\sum_{C x t_{D=(m)}}\left(p\left(C_{s}, D_{0}, n_{D}, C x t_{1}, \ldots, C x t_{n}\right)\right.
$$

and:

$$
p\left(C x t_{1}, \ldots, C x t_{k}\right)=\sum_{C_{s}, D_{0}, n_{D}, C x t_{D=(m)}} p\left(C_{s}, D_{0}, n_{D}, C x t_{1}, \ldots, C x t_{n}\right)
$$

To perform probabilistic inference, the computation of above probabilities is possible but it requires an exhaustive computational effort. A more efficient way is to use inference algorithms. As previously mentioned in this section, only exact inference algorithms (junction tree algorithm (Bensi et al., 2011)) are considered to perform inference. The inference is carried out by the BN Tool Box (Murphy, 2001) which is built on the Matlab ${ }^{\circledR}$ software.

# 3. Sensitivity analysis for age factor statistical characterisation 

The age factor is a crucial parameter for characterising the time-dependency of the

chloride diffusion coefficient. However, according to Gulikers (2003) there are three main difficulties concerning its statistical characterisation: (1) the numerical approach to determine it is not clearly established, (2) the experimental data are limited and (3) the considered exposure time is short. Attari, McNally, \& Richardson (2016) also pointed out the significant impact of age factor on lifetime assessment. Consequently, before focusing on the statistical characterisation of other model parameters (section 5), this section performs a sensitivity analysis to study the influence of the age factor on the statistical characterisation of the chloride diffusion coefficient. The sensitivity analysis considers the effects of: (1) different values of mean and standard deviation of the age factor $\left(n_{D}\right)$ on the statistical characterisation of model parameters (section 3.2), and (2) the selection of inspection times (section 3.3).

# 3.1 BN description 

The BN considered in this sensitivity analysis is based on the model proposed by Nilsson \& Carcasses (2004a) (Eq. (7)). The child nodes representing the chloride concentrations at 3 inspection times ( $\mathrm{T} 1=300$ days, $\mathrm{T} 2=600$ days and $\mathrm{T} 3=900$ days) are introduced to combine evidences from different exposure times. The discretisation and the prior information for model parameters are defined in Table 1. Each node in the BN is discretised into a finite number of states. For parent nodes, we assume uniform distributions defined over upper and lower bounds.

Depending on different test protocols for a given total inspection length, the BN configurations are defined based on the number of inspection points in depth $\left(n_{s}\right)$, the number of inspection times $\left(n_{i}\right)$, and the number of parameters to identify. The evaluation of the effectiveness of the statistical characterisation for a given BN configuration should be based on a given criterion. Preferably, it should include a larger amount of experimental data (chloride profiles) that can be used to estimate "real" probabilistic models of model parameters and consequently to test and compare various BN configurations. However, such a database is in practice very hard to obtain because chloride profiles are computed from semi-destructive tests that are expensive and timeconsuming. Therefore, in order to assess the error associated with each BN configuration without considering statistical bias and to provide general recommendations that minimise the statistical characterisation errors, this section only considers a large number of numerical evidences (chloride profiles) generated through Monte Carlo simulations. The theoretical probabilistic models given in Table 2 are used to generate 3,000 simulated chloride profiles for all numerical study cases. These theoretical values correspond to an ordinary Portland cement (OPC). We assume $\mathrm{t}_{0}^{\prime}=\mathrm{t}_{\mathrm{ex}}^{\prime}=30$ days as deterministic values. The number of child nodes in Figure 2 depends on the discretisation of chloride profiles as described in Figure 3 for determining $n_{s}$ as well as on the number of inspection times for computing $n_{i}$. We assess the performance of the BN configuration in terms of a 'statistical characterisation error' $(\operatorname{Error}(Z))$ as the relative error of the identified parameter $\left(Z_{\text {identified }}\right)$ with respect to the theoretical value $\left(Z_{\text {theory }}\right)$ :

$$
\operatorname{Error}(Z)=\frac{\left|Z_{\text {identified }}-Z_{\text {theory }}\right|}{Z_{\text {theory }}} \times 100 \%
$$

where $Z$ represents the mean or the standard deviation of the parameter to identify e.g., the mean or standard deviation of $D_{0}, Z_{\text {identified }}$ is determined from the a posteriori histograms of parent nodes, and $Z_{\text {theory }}$ is the value of the mean or standard deviation

used to generate numerical evidences provided in Table 2. In practice it is unrealistic (almost impossible) to collect 3,000 chloride profiles. However, this larger database is necessary for obtaining a convergence on the error assessment. The results of this section focus only on the assessment of statistical characterisation errors of the chloride diffusion coefficient which is considered time-dependent as characterised by the age factor.

The sensitivity analysis considers 5 inspection schemes that combine evidences from one and/or several inspection times (Table 3). Each scheme considers the same number of numerical profiles ( 3,000 simulations). The total inspection depth for each chloride profile is chosen equal to 21 mm because beyond this depth, the chloride concentration is almost zero for a maximum exposure time of 900 days. This inspection depth is divided into various intervals with a discretisation depth $\Delta x$. This example considers the minimum inspection depth corresponding to the minimum grinding depth $d_{i j}$ to account for the maximum available information for each chloride profile - i.e. $\Delta x$ $=d_{i j}=3 \mathrm{~mm}$ (Figure 3).

# 3.2 Influence of different values of the mean and standard deviation on the statistical characterisation of $\boldsymbol{n}_{\boldsymbol{D}}$ 

This section considers two cases (Table 4) with different values for the mean and standard deviation of $n_{D}$ representative for OPC concretes in atmospheric and submerged environments, respectively (DuraCrete, 2000). In both cases $n_{D}$ follows a beta distribution.

The statistical characterisation errors of $D_{0}$ (Figure 4) are significantly different for each case. Indeed, in case $2\left(\mu_{n D}=0.30\right)$, the errors for all inspection schemes are higher than $40 \%$ and $250 \%$ for the mean and the standard deviation, respectively. Large errors for the statistical characterisation of the standard deviation are attributed to the fact that $n_{D}$ is an exponent. In contrast, statistical characterisation errors for case 1 are significantly less than $10 \%$ and $160 \%$ for the mean and standard deviation, respectively. These differences are related to the time-variant nature of the chloride diffusion coefficient illustrated in Figure 5. A higher value of $n_{D}$ implies that there is a strong reduction of $D(t)$ at the beginning of the exposure and after $D(t)$ decreases slowly. The sensitivity of different inspection times hinges on the value of $n_{D}$. In case 1, after $\mathrm{T} 1=300$ days, the evolution with time of $D(t)$ is almost constant leading to a small statistical characterisation errors of $D_{0}$ with a single inspection time T1, T2 or T3. Therefore, it is important to have long-term inspection data for statistical characterisation. However, taking information of various inspection times after T1 does not provide more useful information about the evolution of $D(t)$ with time. Hence, schemes that combine inspection times ( $\mathrm{T} 1+\mathrm{T} 2$ or $\mathrm{T} 1+\mathrm{T} 2+\mathrm{T} 3$ ) could not improve significantly the statistical characterisation errors. In contrast, in case $2, D(t)$ presents a decreasing trend at inspection times T1, T2 and T3 (Figure 5). In this case, the combination of inspection data provides more information about the decreasing trend of $D(t)$ diminishing statistical characterisation errors.

The histograms plotted in Figure 6 show that the a posteriori distribution of $D_{0}$ obtained from case 1 is close to the theoretical one in comparison with case 2 . This means that the selected times are not capturing adequately the time-dependency of the chloride diffusion coefficient in case 2 and introduce statistical characterisation errors. In the next section, other values of inspection times (T1, T2 and T3) will be selected to illustrate this aspect for case 2 .

# 3.3 Influence of the selection of inspection times 

As previously discussed in section 3.2, for a given material characterised by an age factor $n_{D}$ the statistical characterisation errors depend on the chosen inspection times. This section compares two cases considering two sets of inspection times presented in Table 5. Case 2a has an early inspection time ( 100 days) in comparison with case Case 2b. The first set of inspection times ( $\mathrm{T1}^{\prime}, \mathrm{T} 2^{\prime}$ and $\mathrm{T3}^{\prime}$ ) is denoted by a higher black line and the second set (T1, T2 and T3) is represented by a lower grey line. According to Figure 5, the variation of the chloride diffusion coefficient with inspection times in case 2 a is higher than in case 2 b . In case 2 a a first inspection at a relatively early exposure time is considered ( $\mathrm{T1}^{\prime}=100$ days) in which the chloride diffusion coefficient is high. By introducing this early time, the time-dependency of the chloride diffusion coefficient can be described adequately. Consequently, the statistical characterisation of $D_{0}$ in case 2a reveals smaller errors as compared to case 2b (Figure 7). The combination of evidences in case 2 a also diminishes significantly the statistical characterisation errors. For example, the statistical characterisation error for the mean of $D_{0}$ is reduced from $30 \%$ (scheme 1) to $8 \%$ (scheme 5) (Figure 7a). Similar trends are also observed for case 2 b , but at a lower reduction rate. The influence of the selection of inspection times is also illustrated for the inspection scheme 5 by comparing the a posteriori histograms of both cases (Figure 8). It should be noted that the shape of the a posteriori histogram of case 2 a is close to the theoretical one. These findings highlight the importance of selecting appropriate inspection times for minimising statistical characterisation errors. In case 2a, early inspection times are very useful for describing the time-dependency of the chloride diffusion coefficient. Hence, in real practice, it is recommended to have also early inspection data for better characterisation the time-dependency of the chloride diffusion coefficient.

Figure 7 also includes a case in which the age factor is fixed at a deterministic value $\left(n_{D}=0.3\right)$. In such a case, smaller errors are estimated for the mean and standard deviation of $D_{0}$. This indicates that the statistical characterisation errors increase significantly when the age factor is introduced as a random variable in the BN. This is a well-known shortcoming when an equation is raised to the power of a random variable (Eq. (7)). To take advantage of this finding, sections 4 and 5 propose an approach to estimate a deterministic age factor in the BN.

## 4. Statistical characterisation of equivalent times from accelerated test data

Section 3.3 indicated that the statistical characterisation error increases significantly when the age factor is considered as a random variable and introduced in the BN as a parent node. Consequently, the level of uncertainty and statistical characterisation error can be reduced if the age factor is determined and introduced as a deterministic value in the BN. In parameter statistical characterisation, data from inspection campaigns (chloride profiles) are used for BN updating. However, the exposure times in normal ageing tests are often short (less than 700 days) and they cannot provide information about mid- and long-term performance of concrete. On the other hand, data from accelerated tests could provide such information. This section presents the construction of a BN configuration that combines data from both normal and accelerated tests to improve the characterisation of the chloride ingress process and analyse the influence of assumptions on deterministic values for the age factor on the statistical characterisation of equivalent times.

# 4.1 BN configuration and basic considerations 

This section considers a BN configuration that combines evidences coming from normal and accelerated data (Figure 9). It consists of 3 parent nodes representing for model parameters $C_{s}, D_{0}$ and the equivalent time $\left(t_{e q}\right)$ for the accelerated test. The equivalent time in accelerated tests could be defined as the required time in normal conditions (normal tests) to reach the same chloride content in accelerated tests. The child nodes denote inspection points in chloride profiles obtained from normal and accelerated tests. Chloride profiles obtained from normal tests provide information about chloride concentration at depth $x_{i}$ and real exposure time $t_{e x p}$. In this numerical example it is assumed that higher chloride concentrations were measured and correspond to "a virtual accelerated test". These higher concentrations (evidences) were generated by fixing various a priori deterministic equivalent times that are in theory unknown. Therefore, those virtual accelerated tests just provide information about chloride content at depth $x_{i}$ and this BN configuration aims at determining the equivalent time $\left(t_{e q}\right)$ for accelerated tests.

Theoretical values given in Table 6 are used to generate evidences for both normal and accelerated data with 9,000 simulations for each inspection time. Evidences from data obtained for normal tests are combined for 3 inspection times: $\mathrm{T} 1=100$ days, $\mathrm{T} 2=300$ days, and $\mathrm{T} 3=600$ days. Evidences from data based on accelerated tests are created from different equivalent times varying from 300 days to 3,000 days. The total inspection depth is assumed to be 30 mm with a discretisation length of $\Delta x=d_{g}=3 \mathrm{~mm}$. We also assume $t_{e s}^{\prime}=t_{0}=30$ days in Eq. (7).

A priori information and the discretisation of model parameters are detailed in Table 7 in which the three parent nodes are assumed to follow uniform distributions. The information provided in Table 7 is used to create the CPTs from simulations. In real practice, the 'theoretical' age factor for creating the evidences ( $n_{D, \text { theory }}$ ) is unknown and it is an additional model parameter to identify. In this case, the BN configuration (Figure 9) considers that the age factor is deterministic with an assumed value $n_{D, \text { assum }}$. We study then different cases corresponding to various assumptions about the age factor ( $n_{D, \text { assum }}=0.30,0.50,0.65$ and 0.70 ). Note that one of these cases considers that $n_{D, \text { assum }}$ is equal to $n_{D, \text { theory }}$ provided in Table 6 (reference case).

### 4.2 Results

Figure 10 presents the statistical characterisation errors for the mean of the equivalent time of accelerated tests $\left(t_{e q}\right)$. It is obvious that the errors are smaller when $n_{D, \text { assum }}$ is equal to $n_{D, \text { theory }}$. In both cases when this factor is under- $\left(n_{D, \text { assum }}=0.3\right)$ or overestimated $\left(n_{D, \text { assum }}=0.65 ; 0.7\right)$ with respect to $n_{D, \text { theory }}$, the statistical characterisation errors increase. Therefore, these results highlight that it is important to propose an approach for improving the characterisation of the age factor from experimental data. Section 5 will propose an iterative procedure towards this aim.

## 5. Methodology for statistical characterisation of model parameters from normal and accelerated tests

This section proposes an approach to determine the age factor and equivalent times from limited inspection data. Normal and accelerated tests are carried out under welldefined laboratory conditions to obtain the experimental data, which are used afterwards for BN statistical characterisation. As previously mentioned, the combination of data from both normal and accelerated tests can improve the mid- and long-term assessment

of chloride ingress; thus the BN configuration presented in Figure 9 is used towards this aim. Section 5.1 describes the experimental setup used to obtain data from normal and accelerated tests. The proposed methodology is illustrated in section 5.2 and the results are presented and discussed in section 5.3.

# 5.1 Experimental setup and problem definition 

### 5.1.1 Context and description

The chloride penetration tests were carried out within the framework of the MAREO project (MAintenance and REpair of concrete coastal structure: risk based Optimisation) in the period 2008-2012 (Bastidas-Arteaga \& Schoefs, 2015). This project aimed at characterising the durability performance of new commercial materials that could be used to repair RC components located in tidal zones by performing both normal and accelerated tests. The results provided mainly qualitative information (a comparison between three repair materials) about the durability performance after a few months of exposure to accelerated tests. This study would like to use the information from accelerated tests to characterise (quantify) the structural performance. We will focus on a commercial repair cement-based material whose composition was not provided by the factory. The name of the material is not provided to avoid any conflict of interest.

In these tests, concrete slabs $(50 \mathrm{~cm} \times 50 \mathrm{~cm} \times 15 \mathrm{~cm})$ are placed in a tank with salty water (Figure 11): University of Nantes Synthetic Seawater Tidal Test Device (UN-SEA-NDT) (Bastidas-Arteaga, Schoefs, Chateauneuf, Sánchez-Silva, \& Capra, 2010). To minimise the effect of hydration processes that can lead to fast decrease of the chloride diffusion coefficient, chloride exposure of the slabs started 300 days after casting. The exposure seawater salinity is within the range $[30 \mathrm{~g} / \mathrm{l}, 37 \mathrm{~g} / \mathrm{l}]$. This range corresponds to the average salinity of the North Atlantic seawater to guarantee a chloride ingress exposure similar to natural conditions. A protective coating applied on 5 sides of the slab and the exposure conditions ensure chloride ingress in one direction from the bottom side (Figure 12) allowing to use the one dimensional penetration model (Eq. (7)). Tidal cycles (high and low) are simulated by varying the level of water (Figure 12). A daily exposure ( 24 hours) is divided into 12 h of immersion (high tide) and 12 h of drying (low tide). For the accelerated tests, fans are used to dry the samples during the low tide cycle. The drying step accelerates chloride ingress due to an increase of the capillarity sorption of concrete (Hong, 1998). Normal tests are subjected to the same tidal cycles without drying by fans. The tests are automatically controlled via a Labview ${ }^{\circledR}$ program. The tanks are placed inside a building and its environmental conditions (room temperature, water salinity and relative humidity) are recorded during the tests.

### 5.1.2 Determination of chloride profiles from normal and accelerated tests

At certain exposure times, slabs are cored to measure chloride profiles. The inspection time is defined as the exposure time of samples until they are cored from slabs. There are 3 concrete cores taken from each slab at 3 different inspection times. Each concrete core is a cylinder concrete with 10.5 cm of diameter and 12 cm in height. Table 8 provides the times at which concrete cores are drilled from slabs for normal ( 9 cores) and accelerated ( 18 cores) tests. We used more cores for accelerated tests to obtain a better assessment of the variability of chloride ingress under this new exposure

condition.
Each core is divided into grinding depth $\left(d_{g}\right)$ for being crushed into concrete powder. The grinding depth is 3 mm and should not be smaller than this value due to the accuracy of equipment. These powders are afterwards used for filtration and titration tests to determine the chloride concentration at each depth point corresponding to the average depth of each interval. The filtration and titration tests follow the procedures described in (Ben Fraj, 2009; Ben Fraj, Bonnet, \& Khelidj, 2012; RILEM TC 178TMC, 2002). Due to the short exposure time, the maximum length for each chloride profile is 42 mm . For chloride profiles with lower chloride concentrations, the total length of chloride profiles might be shorter. With the same exposure times in laboratory conditions, chloride profiles from accelerated tests present higher chloride concentrations as compared with those obtained from normal tests.

# 5.2 Methodology description 

This section details the proposed approach to determine the age factor and equivalent times of accelerated tests when the experimental data is limited. In this section, the real normal data comes from 3 exposure times obtained for laboratory conditions: 65 days, 207 days, and 320 days. The accelerated data introduced in the BN represents the chloride concentration at a certain depth with unknown equivalent time of exposure. A priori information and the discretisation of model parameters are presented in Table 7. The age factor is considered as a deterministic value that is estimated from the experimental data. The total inspection length of chloride profiles is 42 mm with a discretisation length of $\Delta x=3 \mathrm{~mm}$.

The methodology to characterise the age factor is described by the flowchart presented in Figure 14. Stage I implements least square fitting to determine a set of values of $C_{s}$ and $D$ for each chloride profile from normal tests. The mean values of $D$ from normal data at different times (Table 9) are used to estimate a preliminary age factor by applying least square fitting from Eq. (6). Results from curve fitting are presented in Figure 13 with $n_{D}=0.5705$. This result is within the range of values presented in (DuraCrete, 2000a). This age factor is introduced in the BN to determine the mean value of the equivalent times for accelerated tests in the next stage.

Stage II aims at determining the equivalent times from the BN with evidences from both normal and accelerated data. The accelerated data corresponds to 3 different exposure times in the laboratory conditions denoted $t_{\text {eq, } 1}, t_{\text {eq, } 2}$ and $t_{\text {eq, } 3}$ (equivalent times to identify). This stage ends when the equivalents times $t_{\text {eq }, 1}, t_{\text {eq, } 2}$ and $t_{\text {eq, } 3}$ are determined after updating the Bayesian network (Figure 9) with the data coming from accelerated tests.

The equivalent times identified in Stage II allow to estimate chloride diffusion coefficients $(D)$ from accelerated data at these times by using curve fitting (Stage III). For example, Table 9 also presents the equivalent times determined from the BN and the mean values of $D$ estimated by curve fitting at each time for the first iteration. This new information allows re-estimating the age factor by combining new values of $D$ at times $t_{\text {eq, } 1}, t_{\text {eq, } 2}$ and $t_{\text {eq, } 3}$ with those obtained from normal data at $t_{\text {exp, } 1}, t_{\text {exp, } 2}$ and $t_{\text {exp, } 3}$. Results from applying the curve fitting method in Eq. (6) are also shown in Figure 13. It can be seen that introducing data from accelerated tests gives a better assessment about long-term evolution with time of chloride diffusion coefficient that may be overestimated if only data from normal tests is used. A new value of the age factor is also obtained after fitting and it will be introduced to the BN for a new iteration until

convergence by repeating Stages I and II. Here the convergence criterion is defined by a difference smaller than $10^{-3}$ of values obtained between iterations. The final results are not influenced by the fitting method employed in Stage I because all parameters are updated after Bayesian inference.

# 5.3 Results after the iterative procedure 

With real data obtained from experimental tests, the procedure to identify the age factor in this study is stopped after 4 iterations when values of age factor $\left(n_{D}\right)$ and the equivalent times $\left(t_{\text {eq }, 1}, t_{\text {eq }, 2}\right.$ and $\left.t_{\text {eq }, 3}\right)$ reach convergent values (Table 10).

Model parameters identified after each iteration (Table 10) could be used to compute $5 \%$ and $95 \%$ percentiles of chloride concentration at depth $x=10.5 \mathrm{~mm}$ at different times. By plotting these percentiles with real data from normal and accelerated tests, it can be seen in Figure 15 that the predicted $95 \%$ percentile at iterations 2 and 3 are closer to the accelerated data than those from BN updating with only normal data or iteration 1. There are several data points that do not fall in the range $5 \%$ and $95 \%$ percentiles. This is, on the one hand, due to the limited number of experimental data that leads to the poor quality of information used for BN statistical characterisation. On the other hand, the inspection points at depth $x=10.5 \mathrm{~mm}$ are quite close to the surface of structures (convection zone) where the selected model is not able to account for convection effects. However, in practice, it is of interest to evaluate chloride concentration at deeper points near the rebar.

The exposure times considered in this study were not sufficient to allow significant chloride concentrations to reach the cover depth. Therefore, we select a second depth $(x=31.5 \mathrm{~mm})$ to compare the $5 \%$ and $95 \%$ percentiles of chloride concentration and real data (Figure 16). A similar trend as $x=10.5 \mathrm{~mm}$ is observed for $x=31.5 \mathrm{~mm}$ after iterations where predictions of $95 \%$ percentiles are closer to real data.It is also worth noticing that all accelerated data fall in the range of $5 \%$ and $95 \%$ percentage. This finding can be explained by the fact that at a depth $x=31.5 \mathrm{~mm}$, there is hardly any effect of a convection zone and the chloride ingress model is more appropriate to estimate chloride concentrations. Note that in both cases ( $x=10.5 \mathrm{~mm}$ and $x=31.5 \mathrm{~mm}$ ), the predicted $5 \%$ percentile remains almost the same after update. This is due to the effect of short distribution tails at $5 \%$ percentile where the updating process has no significant change (Figure 17). On the contrary, the updating of the right distribution tail is significant which is of first importance for reliability assessment. Moreover, it is seen that at $x=31.5 \mathrm{~mm}$ we are able to capture the dissymmetrical distribution shape that has been observed (Bonnet, Schoefs, Ricardo, \& Salta, 2009). Therefore, it can be concluded that this approach is useful for identifying the age factor from real data. The statistical characterisation would be improved if more experimental data is provided.

## 6. Conclusions and perspectives

Chloride ions are aggressive species leading to reinforcement corrosion of RC structures. Related parameters for modelling this process are necessary for studying reliability of structures and planning inspection schedules. Frequently, these parameters are estimated from inspection data obtained from on-site measurements after decades. Thus, inspection campaigns require significant time to obtain a sufficient amount of data for condition assessment and reliability analysis. Therefore, this study accounts for data from normal and accelerated tests for characterising and modelling the penetration

of chloride ions into concrete. This data could provide useful information for parameter statistical characterisation from BN updating.

Chloride ingress models should consider the time-dependency of the chloride diffusion coefficient by introducing an age factor. Results from sensitivity analysis indicated that this factor has a significant influence on the estimation of model parameters. For specific concrete characteristics and exposure conditions (a given age factor), the inspection schemes should consider both early and long-term inspection times describing adequately the evolution of the chloride diffusion coefficient with time. Combining information coming from these inspection times improves the statistical characterisation of parameters. It is also worth noticing that considering the age factor as a random variable in BN increases uncertainty and adds errors for the statistical characterisation.

This study proposed a BN framework to improve the statistical characterisation of parameters in chloride ingress models. The procedure estimates a priori information about age factor from data obtained from normal exposure tests and based on that determines the equivalent times for data from accelerated tests. By integrating information from normal and accelerated data the age factor is then re-estimated. Afterwards, the equivalent times are also updated from BN. A convergence trend was obtained when both mean equivalent times and age factor lead to constant values. In this procedure, the combination of data from normal and accelerated tests provides a better assessment of the time-dependent process of chloride diffusion coefficient that can be under- or overestimated if only normal data is used. This result also highlights the importance of data from long-term inspection for identification of $n_{D}$. By comparing the confidence intervals estimated from probabilistic modelling of chloride ingress and real data, it can be concluded that this approach is useful for characterising the age factor and that BN is a powerful tool for analysing such a time-dependent problem.

There are some aspects that could be considered in future works:

- Consideration of modelling errors as new parameters to identify and to be determined from real data.
- Extension of the statistical characterisation of random variables to the statistical characterisation of random fields.
- Consideration of costs for recommending inspection procedures (inspection times, number of cores, number and positions of measures in each core, etc.) that provide a balance between error and cost.
- Validation and improvement of the proposed procedure with long-term data.


# Acknowledgments 

The authors are grateful for the insightful and constructive comments from the reviewers.

# List of Tables 

Table 1 BN discretisation and a priori information of model parameters
Table 2 Theoretical values for generating simulated chloride profiles
Table 3 Description of the inspection schemes
Table 4 Considered theoretical values of $n_{D}$ (DuraCrete, 2000b)
Table 5 Studied cases with different inspection times
Table 6 Theoretical values for generating simulated evidences (Bastidas-Arteaga, Bressolette, Chateauneuf, \& Sánchez-Silva, 2009; Duprat, 2007)
Table 7 A priori information and discretisation of model parameters
Table 8 Times (in days) to take cores from slabs since the beginning of the exposure
Table 9 Fitted mean values of $D$ at each exposure time in normal and accelerated tests
Table 10 Evolution of model parameters after the iterative procedure

# List of Figures 

Figure 1 A Simple Bayesian Network
Figure 2 BN for modelling chloride ingress
Figure 3 Discretisation for estimating chloride profiles
Figure 4 Statistical characterisation errors of $D_{0}$ for: (a) mean - (b) standard deviation
Figure 5 Time-variant chloride diffusion coefficient for different values of age factor
Figure 6 A posteriori distribution of $D_{0}$ for the inspection scheme $5(\mathrm{~T} 1+\mathrm{T} 2+\mathrm{T} 3)$
Figure 7 Statistical characterisation errors of $D_{0}$ for: (a) mean - (b) standard deviation
Figure 8 A posteriori distributions of $D_{0}$ for different inspection times in the inspection scheme 5
Figure 9 BN configuration combining data from both normal and accelerated tests
Figure 10 Statistical characterisation errors for the mean of equivalent time of accelerated test $\left(t_{e q}\right)$ with different assumed values of $n_{D}\left(n_{D, \text { assum }}\right)$
Figure 11 Distribution of concrete slabs in the tank
Figure 12 Laboratory tidal conditions
Figure 13 Estimation of age factor using curve fitting with normal data and combining data at iteration 1
Figure 14 Flowchart to identify the age factor and the equivalent times
Figure $155 \%$ and 95 percentiles of chloride concentration at depth $x=10.5 \mathrm{~mm}$
Figure $165 \%$ and 95 percentiles of chloride concentration at depth $x=31.5 \mathrm{~mm}$
Figure 17 Probability density and distribution tails with $5 \%$ and $95 \%$ percentiles at: (a) $x=10.5 \mathrm{~mm}$ and (b) $x=31.5 \mathrm{~mm}$

Table 1 BN discretisation and a priori information of model parameters


${ }^{\text {a }}$ Using different boundaries for child nodes (Tran et al., 2016a)

Table 2 Theoretical values for generating simulated chloride profiles


${ }^{\text {a }}$ Value estimated from a concrete density $\rho_{c}=2300 \mathrm{~kg} / \mathrm{m}^{3}$

Table 3 Description of the inspection schemes


Table 4 Considered theoretical values of $n_{D}$ (Duracrete, 2000)


Table 5 Studied cases with different inspection times


Table 6 Theoretical values for generating simulated evidences (Bastidas-Arteaga et al., 2009; Duprat, 2007)


${ }^{a}$ Value estimated from a concrete density $\rho_{c}=2300 \mathrm{~kg} / \mathrm{m}^{3}$

Table 7 A priori information and discretisation of model parameters


[^0]
[^0]:    ${ }^{a}$ Using different boundaries for child nodes according to (Tran et al., 2016a)

Table 8 Times (in days) to take cores from slabs since the beginning of the exposure


Table 9 Fitted mean values of $D$ at each exposure time in normal and accelerated tests


Table 10 Evolution of model parameters after the iterative procedure




![img-0.jpeg](img-0.jpeg)

Figure 1 A Simple Bayesian Network
![img-1.jpeg](img-1.jpeg)

Figure 2 BN for modelling chloride ingress

![img-2.jpeg](img-2.jpeg)

Figure 3 Discretisation for estimating chloride profiles
![img-3.jpeg](img-3.jpeg)

Figure 4 Statistical characterisation errors of $D_{0}$ for: (a) mean - (b) standard deviation

![img-4.jpeg](img-4.jpeg)

Figure 5 Time-variant chloride diffusion coefficient for different values of age factor
![img-5.jpeg](img-5.jpeg)

Figure 6 A posteriori distribution of $D_{0}$ for the inspection scheme $5(\mathrm{~T} 1+\mathrm{T} 2+\mathrm{T} 3)$

![img-6.jpeg](img-6.jpeg)

Figure 7 Statistical characterisation errors of $D_{0}$ for: (a) mean - (b) standard deviation
![img-7.jpeg](img-7.jpeg)

Figure 8 A posteriori distributions of $D_{0}$ for different inspection times in the inspection scheme 5

![img-8.jpeg](img-8.jpeg)

Figure 9 BN configuration combining data from both normal and accelerated tests
![img-9.jpeg](img-9.jpeg)

Figure 10 Statistical characterisation errors for the mean of equivalent time of accelerated test $\left(t_{e q}\right)$ with different assumed values of $n_{D}\left(n_{D, \text { assum }}\right)$

![img-10.jpeg](img-10.jpeg)

Figure 11 Distribution of concrete slabs in the tank
![img-11.jpeg](img-11.jpeg)

Figure 12 Laboratory tidal conditions

![img-12.jpeg](img-12.jpeg)

Figure 13 Estimation of age factor using curve fitting with normal data and combining data at iteration 1
![img-13.jpeg](img-13.jpeg)

Figure 14 Flowchart to identify the age factor and the equivalent times

![img-14.jpeg](img-14.jpeg)

Figure $155 \%$ and 95 percentiles of chloride concentration at depth $x=10.5 \mathrm{~mm}$
![img-15.jpeg](img-15.jpeg)

Figure $165 \%$ and 95 percentiles of chloride concentration at depth $x=31.5 \mathrm{~mm}$

![img-16.jpeg](img-16.jpeg)

Figure 17 Probability density and distribution tails with $5 \%$ and $95 \%$ percentiles at: (a) $x=10.5 \mathrm{~mm}$ and (b) $x=31.5 \mathrm{~mm}$