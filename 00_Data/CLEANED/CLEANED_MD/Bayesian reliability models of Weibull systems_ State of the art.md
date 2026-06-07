# BAYESIAN RELIABILITY MODELS OF WEIBULL SYSTEMS: STATE OF THE ART 

Abdelaziz ZAIDI **, Belkacem OULD BOUAMAMA *, Moncef TAGINA **<br>* LAGIS, Polytech'Lille<br>University of Lille Nord de France, 59650 Villeneuve d'Ascq, France<br>e-mail: Belkacem.Ouldbouamama@polytech-lille.fr<br>${ }^{* *}$ LACS<br>National School of Engineering of Tunis, BP 37, 1002 Belvedere, Tunisia<br>e-mail: Abdelaziz.Zaidi@isetso.rnu.tn, Moncef.Tagina@ensi.rnu.tn


#### Abstract

In the reliability modeling field, we sometimes encounter systems with uncertain structures, and the use of fault trees and reliability diagrams is not possible. To overcome this problem, Bayesian approaches offer a considerable efficiency in this context. This paper introduces recent contributions in the field of reliability modeling with the Bayesian network approach. Bayesian reliability models are applied to systems with Weibull distribution of failure. To achieve the formulation of the reliability model, Bayesian estimation of Weibull parameters and the model's goodness-of-fit are evoked. The advantages of this modelling approach are presented in the case of systems with an unknown reliability structure, those with a common cause of failures and redundant ones. Finally, we raise the issue of the use of BNs in the fault diagnosis area.


Keywords: hierarchical modeling, reliability, Weibull, Bayesian networks, fault diagnosis.

## 1. Introduction

Reliability analysis of industrial systems is one of the most dynamic branches of research. However, safety critical systems analysis such as in electrical production energy power stations and aeronautic systems requires suitable knowledge on the reliability of a system's components. The evolution of statistical methods of modeling gave a considerable contribution in this context.

Empirical statistical methods are replaced in several applications by hierarchical Bayesian ones. The Bayesian modeling framework is based on incorporation of different sources of quantitative and qualitative data in the model. These data are considered prior information on the system. The analyses presented in this paper are simple illustrations of the power of the Bayesian Networks (BNs) approach in the domains of reliability analysis and fault diagnosis.

Furthermore, this paper shows how to assess the parameters of the reliability model by the hierarchical Bayesian approach. It is emphasized here that he Weibull probability density function (pdf) is a more general failure density than the classical exponential one (i.e., it permits the modeling of different regions of the bathtub curve in
the lifecycle of a great number of components).
Bayesian networks (Pearl, 1988), also known as probabilistic networks or belief networks, have been known in the artificial intelligence community and exploited in different expert systems to model complex and uncertain interactions among causes and consequences. In probabilistic reasoning, random variables are used to represent events and/or objects in the world. Bayesian reasoning and inference procedures have only recently gained popularity in the fusion of information obtained from different sources. A BN, as a graphical approach, has become the best suited way of representing our beliefs about the elements of several systems and the relationships that exist between these various elements. Consider the simple directed acyclic graph of Fig. 1. Suppose $A$ and $B$ are two objects, each one associated to an event which can be observed or not. This causal representation is the most intuitive representation of the influence of an event/situation on another event/situation. This can be interpreted as follows: The knowledge that we have on $A$ determines what we can have on $B$ and, conversely, any information on $B$ will modify our knowledge on $A$.

Indeed, a Bayesian network is a directed acyclic

![img-0.jpeg](img-0.jpeg)

Fig. 1. Simple directed acyclic graph.
graph (DAG) $\mathcal{G}=\mathcal{G}(N, \mathcal{A})$, where $N$ is the set of nodes of $\mathcal{G}$ and $\mathcal{A}$ the set of arcs connecting the nodes. The set of stochastic variables $X=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ are associated with the nodes of the graph $\mathcal{G}$ which is governed by a set of Conditional Probability Distribution (CPDs) for every node,

$$
P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=0}^{n} P\left(X_{i} \mid \operatorname{Par}\left(X_{i}\right)\right)
$$

where $\operatorname{Par}\left(X_{i}\right)$ is the set of the causes (parents) of $X_{i}$ in the graph $\mathcal{G}$. We could say that BNs operate by propagating beliefs throughout the network, once some evidence about the existence of certain entities can be asserted. We are able to learn probabilities of all parts in the system, given our knowledge of the existence of a few of them and the conditional probability distributions. These conditional probabilities do not have to be known a priori and can be learned using statistical sampling techniques or supervised learning approaches.

We refer to the work of Langseth and Portinale (2007) for details on building BN models as well as different conditional independence statements and inference. Here we must note that our work can be considered a non-exhaustive application to Bayesian reliability modeling with the Weibull pdf, and also an introduction to the use of BNs in the fault diagnosis area.

As stated by Langseth and Portinale (2007), the history of BNs in reliability started in the beginning of the 1990s. The first true test is the work of Almond (1992), who proposed the use of the Graphic Belief tool for calculating reliability from measurements of a pressure of an injection coolant system in a nuclear reactor (a problem originally addressed by Martz and Waller (1990)).

In this field, several papers have been published. Portinale et al. (2005) showed a comparison between the Fault Tree Analysis (FTA) approach and the BN in the field of reliability and dependability analysis of industrial systems. According to Bobbio et al. (2001), it is possible to convert the static gates of a Fault Tree (FT) into a BN. Torres-Toledano and Sucar (1998) demonstrated that the
same conversion is possible between the Reliability Diagram $(\mathrm{RD})$ and the BN.

With the BN formalism, one can perform not only all dependence analyses led by FT and RD approaches, but also the modeling of several non-classic operation modes. Portinale et al. (2005) used the same approach to model the reliability of systems with an unknown structure, a Common Cause of Failure (CCF) and redundant systems with imperfection of the recovery mechanism. The authors also studied the modeling of degraded states and sequentially dependent failures. This reference treated the problem of parameter uncertainty and sensitivity analysis by insertion of nodes associated to a stochastic variable uniformly distributed between minimal and maximal values of the reliability parameter.

Boudali and Dugan (2006) introduced Continuous Time Bayesian Networks (CTBNs) for reliability modeling of dynamic systems. The suggested approach targets complex systems where it is not only necessary to take into account the combination of the failure events but also their order of succession. The CTBN formalism also allows the analysis of the sensitivity and uncertainties of parameters. The authors showed the limits of Markov chains, which are considered a low level approach and must be derived from a high level one such as Dynamic Fault Trees (DFTs). The most significant limitation of Markovian processes is having exponentially distributed states, and the increase in the size of the system causes an explosion of the state space, and, consequently, an exponential increase in the differential equations to be solved. A comparison between the DFT and the BN was presented, showing that the latter is more general, i.e., it is possible to convert a DFT to a BN, and the reverse is not always possible.

The problem of inference in BNs for reliability analysis is an active subject in the literature. However, several algorithms are proposed. In the BN literature, the approach of a Temporal BN (TBN) is widespread. In the reliability context, these networks introduce the possibility of order analysing of the failures. Generally, there are two categories: the approach based on events (event-based or interval-based) and the one based on time-slices (instantbased).

Within the TBN framework with the event-based approach Boudali and Dugan (2005) showed how to translate a DFT into a Discrete Temporal BN (DTBN). According to them, the study of dependence in Probabilistic Risk Assessment (PRA) must evoke three types of analyses: (i) the time of occurrence of the event, (ii) the order of the events (iii), and the dependence of the occurrence time of the event with the temporal evolution of the system's variables. The proposed discretization algorithm consists in dividing time into $(n+1)$ intervals so that a random variable has a finite number of $(n+1)$ possible states. The $n$ first states divide the interval time $[0, T]$ (T

is the mission time) in $n$ equal intervals. The state $(n+1)$ represents the interval $] T,+\infty[$. The authors showed on an example that discretization over a well defined order $n$ does not improve the precision of the result, whereas the computing time becomes more considerable. In the same reference, there is shown the possibility of carrying out, with the same approach, several other analyses such as the importance factor of Birnbaum (Andrews and Moss, 1993). This type of static discretization is implemented in the software Hugin (Hugin, 2011) and Netica (Netica, 2011).

In the event-based approach the period of time is subpartitioned into a finite number of disjoint time intervals. A random variable can appear in a certain time interval. The event-based approach assumes that each event happens at most once. In fact, this assumption concerns non-repairable systems where the failure of a component (i.e., the event) happens only once during the mission time. Temporal Nodes Bayesian Networks (TNBNs) (Arroyo-Figueroa and Sucar, 1999), the Net of Irreversible Events in Discrete Time (NIEDT) (Galan and Diez, 2000) and Networks of Probabilistic Events in Discrete Time (NPEDTs) (Galan and Diez, 2002) are classified as eventbased approaches. Nodelman et al. (2002) propose Conditional Markovian Processes (CMPs) for the modeling of Markovian processes by the BN formalism; it represents the equivalent of CPD in a BN.

Marquez et al. (2007) elicited Hybrid BNs (HBNs) for reliability modeling of complex dynamic systems. The model contains random continuous nodes representing the times to a failure of the system's components. The discrete random variables represent the state of the system or the subsystem at one well defined moment (faulty or healthy). This approach has the advantage of using not only exponential distributions but also data failure information or prior information provided from experts. The inference procedure is carried out by a dynamic discretization, an approach introduced by Kozlov and Koller (1997), as well as Koller et al. (1999). The criterion of discretization uses the error of entropy. This approach does not require a numerical integration or a stochastic simulation and can treat censured data. As an application, this discretization algorithm was implemented in the AgenaRisk software (Agena, 2011). It is described in detail by Neil et al. (2007). Moral et al. (2001) proposed the Mixture of Truncated Exponentials (MTE) algorithm for HBN inference. This approach defines for each discrete variable of the network, a potential function through continuous variables in the form of a weighted sum of the exponential of these variables.

According to Neil et al. (2008), the discretization approach presented by Boudali and Dugan (2005) has some disadvantages. The user must define in advance discretization the intervals independently of any information arriving thereafter. In the presence of observations, the
inference may lead to errors. The refinement of the discretization can be expensive from the computational time point of view, whereas in the method suggested by the authors this precision can be required only for well defined areas of the marginal posterior distribution. Moreover, the discretization is adjusted each time there are new observations to obtain better precision.

In the time-slice approach, a BN is associated with one specific moment. The same network is generally used to describe the model for the next sampling slices, and consequently one finds arcs connecting the various networks to form a Dynamic Bayesian Network (DBN). The concept of 2-TBN is most often used in this approach (Ben Salem et al., 2006; Weber and Jouffe, 2003). Weber and Jouffe (2003) show how to use a 2-time-slice DBN to model temporal dependencies between components for reliability calculations. The authors also demonstrate the equivalence between their DBN model and a Markov chain, i.e., they both possess the Markov property. Thus, the model is applicable exclusively to Markovian processes.

Ben Salem et al. (2006) highlight the importance of the DBN for the modeling of various types of degradation in a dynamic system. Stochastic models such as Markov Chains (MCs), Hidden Markov Models (HMMs), InputOutput Hidden Markov Models (IOHMMs) and Markov Switching Models (MSMs) (same as CMPs) can be represented in the form of interconnections of a DBN, which shows the richness of this representation to model most complicated types of failures by taking into account the influence of time as well as the exogenous variables (abrupt changes in the functioning modes) and environmental conditions (e.g., humidity, temperature). A new application is illustrated by Weber et al. (2006) regarding the use of a DBN to increase the performance of the decisionmaking in the field of model based diagnosis. This approach will be highlighted in Section 4.

Portinale et al. (2007) presented the RADYBAN software implementation of the DBN as a solution for reliability analysis of dynamic systems. The software allows reliability modeling of complex systems by two approaches, DBNs and DFTs. The DBN model is a 2TBN one. This tool lets the user choose among two possible tasks: filtering/prediction or outputs smoothing. The inference used is either the Junction Tree (JT) (Jensen, 2001; Murphy, 2002), or the Boyen-Koller algorithm (Boyen and Koller, 1998), and it is emphasized that the discretization step must be chosen suitably compared to the time of mission. A comparison was made between the use of the RADYBAN and Galileo sofware by Sullivan et al. (1999).

An interesting approach regarding Bayesian reliability modeling of complex systems is the inference by the Markov Chain Monte Carlo (MCMC) method which is proposed by Wilson et al. (2006), Reese et al. (2005), and

Johnson et al. (2003). Wilson and Huzurbazar (2007) use BNs to model systems with an unknown reliability structure, which cannot be modelled by the FT approach. The authors studied various cases of available data for the reliability analysis of global systems and their components. As a modular fashion approach, Dynamic Object Oriented Bayesian Networks (DOOBNs) are proposed by Weber and Jouffe (2006) for repetitive structures in the process.

Although TBN approaches are attractive, their application and contribution in the field of reliability analysis is a difficult task; this difficulty lies in (i) the definition of the structure, which represents correctly the interactions of components within the system and (ii) specification of the prior distributions of the random variables and the conditional probability tables.

In Section 2, hierarchical Bayesian approach for estimating the reliability parameters is presented. As an illustration example, the Weibull model is treated. Section 3 describes reliability modeling with BNs and the study of different cases of structures. Section 4 is dedicated to the application of BN reliability modeling to the Fault Detection and Isolation (FDI) field, and Section 5 concludes the paper.

## 2. Reliability estimation with the Bayesian approach

2.1. Introduction. The Bayesian approach is based on the concept of a prior distribution of parameters. With Bayesian inference, one can obtain a posterior distribution in the presence of observations (this one is proportional to the likelihood function multiplied by the prior distribution of the parameters). The calculation of the marginal density requires integration over all possible ranges of the parameter variation. A Bayesian estimator can integrate several types of prior knowledge: opinions of experts, tests, failure data, etc.

Bayesian techniques of data analysis are grouped into two main families: hierarchical methods and empirical ones. The foundation of the empirical methods dates back to the 1940s. In the literature, there is a significant number of papers explaining this theory and the logic of its use as well as the relationships to the other statistical techniques (Casella, 1985; Deely and Lindley, 1981; Morris, 1983). Essentially, empirical Bayesian methods are an approximation of Bayesian true analysis. They do not represent true analyzes of data because they use a traditional statistical approach to estimate the prior distribution of the parameters such as frequential analysis. The hierarchical Bayes idea has become very important in recent years. It allows dealing with a much richer class of models that can better capture our statistical understanding of the problem. With the advent of MCMC, it has become possible to perform calculations on these much more complex models, thus rendering this approach more practical.

The basic idea in a hierarchical model is that when you look at the likelihood function and decide on the right priors, it may be appropriate to use priors that themselves depend on other parameters not mentioned in the likelihood. These parameters themselves will require priors and can depend on the new ones. This can continue in a hierarchical framework until there are no more parameters to incorporate in the model. Several papers focused on the effectiveness of this approach compared with the traditional empirical methods (Robinson, 2001).
2.2. Weibull probability density function. The Weibull distribution of failure, with its two parameters (shape and scale), permits the modeling of different regions of the bathtub curve in the lifecycle of a great number of components. For more details on this distribution and its applications, see the work of Rinne (2008).

The Weibull pdf is defined by

$$
f(t \mid a, b, \tau)=\left(\frac{a}{b}\right)\left(\frac{t-\tau}{b}\right)^{a-1} \exp \left[-\left(\frac{t-\tau}{b}\right)^{a}\right]
$$

where $a$ is the parameter of shape, $b$ is the parameter of scale, and $\tau$ is the parameter of location (delay). One can notice that, if $a=1$, the distribution becomes exponential.

The hazard rate (instantaneous failure rate) is

$$
h(t)=\left(\frac{a}{b}\right)\left(\frac{t-\tau}{b}\right)^{a-1}
$$

where $b$ is homogeneous with $t$ and $a$ do not have dimension. This last parameter reflects the behavior of the hazard function:

- $a>1$ : the hazard function is increasing, which makes it possible to model aging failures;
- $a<1$ : the hazard function is decreasing, which makes it possible to model youth failures (infant mortality defects);
- $a=1$ : the hazard function is constant; it is equivalent to the exponential distribution, which can model accidental failures.

In practice and for physical reasons, the shape parameter $a$ is bounded (Bousquet, 2006). The reliability is determined by the relation

$$
R(t)=\int_{t}^{\infty} f(u) \mathrm{d} u=\exp \left[-\left(\frac{t-\tau}{b}\right)^{a}\right]
$$

2.3. Bayesian estimation of parameters. Let us suppose that one has $n$ i.i.d. samples $\mathcal{D}=\left(x_{1}, \ldots, x_{n}\right)$ from a density $f_{\theta}$, with an unknown vector of parameters

$\theta=\left(\theta_{1}, \theta_{2}, \ldots, \theta_{k}\right)$, and the associated likelihood function

$$
L(\theta \mid \mathcal{D})=\prod_{i=1}^{n} f_{\theta}\left(x_{i}\right)
$$

This quantity represents the fundamental entity for the analysis of observation data about $\theta$ through $\mathcal{D}$, and the Bayesian inference will be based on this function. The posterior distribution of the parameter $\theta$ is given by

$$
p(\theta \mid \mathcal{D})=\frac{L(\theta \mid \mathcal{D}) \pi(\theta)}{\int L(\theta \mid \mathcal{D}) \pi(\theta) \mathrm{d} \theta} \propto L(\theta \mid \mathcal{D}) \pi(\theta)
$$

where $\pi(\theta)$ is the prior distribution of the parameter $\theta$.
For the Weibull $(a, b)$ distribution, the likelihood is

$$
L(a, b \mid \mathcal{D})=\prod_{i=1}^{l} \frac{a}{b}\left(\frac{x_{i}}{b}\right)^{a-1} \exp \left[-\left(\frac{x_{i}}{b}\right)^{a}\right]
$$

and the posterior density of parameters is defined by

$$
p(a, b \mid \mathcal{D}) \propto L(a, b \mid \mathcal{D}) \pi(a, b)
$$

Thereafter, this model is applied to the Weibull $(a, b)$ distribution with informative and non-informative prior distributions of the parameters.

### 2.3.1. Estimate with improper non-informative prior

distributions. Consider the Weibull model with two parameters ((2), $\tau=0$ ). We suppose to have uncensured data $t=\left\{t_{1}, t_{2}, \ldots, t_{n}\right\}$ characterizing the failure times of $n$ identical components whose distribution of failure follows the Weibull pdf. With the reparametrisation $\lambda=$ $b^{a}$, one can deduce the new expression of the Weibull pdf,

$$
f(t \mid \lambda, a)=\lambda a t^{a-1} \exp \left[-\lambda t^{a}\right]
$$

The likelihood function is written as

$$
\begin{aligned}
L(\lambda, a \mid \mathbf{t}) & =\prod_{i=1}^{n} \lambda a t_{i}^{a-1} \exp \left[-\lambda t_{i}^{a}\right] \\
& =(\lambda a)^{n} \prod_{i=1}^{n} t_{i}^{a-1} \exp \left[-\lambda \sum_{i=1}^{n} t_{i}^{a}\right]
\end{aligned}
$$

The log- likelihood is

$$
\begin{aligned}
& \mathcal{L}(\lambda, a \mid \mathbf{t}) \\
& \quad=n \ln (\lambda a)+(a-1) \sum_{i=1}^{n} \ln \left(t_{i}\right)-\lambda \sum_{i=1}^{n} t_{i}^{a}
\end{aligned}
$$

The choice of the prior non-informative distribution will be, according to Jeffery's relation,

$$
\pi(\lambda, a) \propto \sqrt{|I(\lambda, a)|}
$$

For the determination of this prior distribution, one will need to calculate the Fisher information matrix (Jeffreys, 1961),

$$
\begin{aligned}
& |I(\lambda, a)|= \\
& -E\left|\begin{array}{cc}
\partial^{2} \ln f(t \mid \lambda, a) / \partial \lambda^{2} & \partial^{2} \ln f(t \mid \lambda, a) / \partial \lambda \partial a \\
\partial^{2} \ln f(t \mid \lambda, a) / \partial \lambda \partial a & \partial^{2} \ln f(t \mid \lambda, a) / \partial a^{2}
\end{array}\right|
\end{aligned}
$$

which is proportional to $(1 / \lambda a)^{2}$. This yields

$$
\pi(\lambda, a) \propto \frac{1}{\lambda a}
$$

Using (8), one can deduce the join posterior distribution of parameters $\lambda$ and $a$ from (10) and (14),

$$
p(\lambda, a \mid \mathbf{t}) \propto(\lambda a)^{n-1} \prod_{i=1}^{n} t_{i}^{n-1} \exp \left[-\lambda \sum_{i=1}^{n} t_{i}^{a}\right]
$$

The posterior distributions of parameters are

$$
\begin{aligned}
p(\lambda \mid \mathbf{t}, a) & \propto \lambda^{n-1} \exp \left[-\lambda \sum_{i=1}^{n} t_{i}^{a}\right] \\
& \propto \operatorname{Gamma}\left(n, \sum_{i=1}^{n} t_{i}^{a}\right) \\
p(a \mid \mathbf{t}, \lambda) & \propto a^{n-1} \prod_{i=1}^{n} t_{i}^{a-1} \exp \left[-\lambda \sum_{i=1}^{n} t_{i}^{a}\right]
\end{aligned}
$$

The Gamma distribution is defined by

$$
\begin{aligned}
f(t \mid \alpha, \lambda)=\frac{\lambda^{\alpha}}{\Gamma(\alpha)} t^{\alpha-1} & \exp (-\lambda t) \\
& t>0, \quad \alpha>0, \quad \lambda>0
\end{aligned}
$$

It is clear that the second density (17) is not trivial to calculate. This can take expensive computational time; it would be interesting to take into account the recommendation present in several references regarding the equivalence of the Bayesian estimator and the Maximum Likelihood (ML) one in the case of non-informative prior (Rinne, 2008; Lynch, 2007). The use of the Bayesian inference method requires an effective method of sampling for $p(a \mid t, \lambda)$, which is a log-concave function. Most often, if the inverse method is not possible for generation of random samples, the rejection sampling method can be applied (Gilks and Wild, 1992).
2.3.2. Estimate with informative conjugated prior distributions. When prior conjugated distributions are used, the Gamma density is a suitable choice. Let us suppose that the parameters $\lambda$ and $a$ are distributed as follows:

$$
\begin{aligned}
& \lambda \quad \sim \quad \operatorname{Gamma}(\alpha, \beta) \\
& a \quad \sim \quad \operatorname{Gamma}(\gamma, \eta)
\end{aligned}
$$

The most current hierarchical model used in this case is the one with two stages. Hyperparameters $\alpha, \beta, \gamma$ and $\eta$ are assumed to be known; thus, the posterior distribution of $\lambda$ follows also the Gamma density,

$$
\begin{aligned}
p(\lambda \mid \mathbf{t}, a) & \propto \lambda^{\alpha+n-1} \exp \left[-\lambda\left(\beta+\sum_{i=1}^{n} t_{i}^{a}\right)\right] \\
& \propto \operatorname{Gamma}\left(\alpha+n, \beta+\sum_{i=1}^{n} t_{i}^{a}\right)
\end{aligned}
$$

The posterior distribution of $a$ is written as

$$
p(a \mid \mathbf{t}, \lambda) \propto a^{\gamma+n-1} \prod_{i=1}^{n} t_{i}^{a-1} \exp \left[-\eta a-\lambda \sum_{i=1}^{n} t_{i}^{a}\right]
$$

2.4. Model's goodness-of-fit. Two families of tests are evoked in this context. The first one consists in checking if there is a discrepancy between the data and the model. In this case, the $p$-value is used; it is determined from the Prior Predictive Distribution (PPD). The distribution of $y^{r e p}$ (replicated data) conditionally to the current state of knowledge is described by the PPD,

$$
p\left(y^{r e p} \mid y\right)=\int p\left(y^{r e p} \mid \theta\right) p(\theta \mid y) \mathrm{d} \theta
$$

The checking procedure consists in generating replicated data from $p\left(y^{r e p} \mid y\right)$ called $y_{i}^{r e p}$ for $(i=1, \ldots, N)$ with $N$ being the total number of the replications, and comparing them with the observation data. Generally, it is necessary to use thereafter a test function $T(\cdot) . T(y)$ is a statistical test using the observation data and $T\left(y^{r e p}\right)$ is the same test for the replicated data. Then, the $p$-value is deduced as

$$
p \text {-value }=P\left(T\left(y^{r e p}\right)>T(y) \mid \theta\right)
$$

The $p$-value measures the statistical significance of the model and not the practical significance. Consequently, an interval of $[0.05,0.95]$ is reasonable for the $p$-value. When the $p$-value is close to 0.5 , this indicates a good agreement between the data and the model (Kelly and Smith, 2009).

The second family uses the concept of the Bayes factor (Lynch, 2007), which allows choosing from among several models. For hierarchical models, one can use the Deviance Information Criterion (DIC) score. This uses, to compare models, a criterion based on a trade-off between the fit of the data to the model and the corresponding complexity of the model. The DIC score is defined by

$$
D I C=\bar{D}+p_{D}
$$

where

$$
\bar{D}=E_{\theta}[D(\theta)]
$$

is the posterior mean deviance calculated from the posterior distribution of deviance:

$$
D(\theta)=-2 \log [p(y \mid \theta)]
$$

and $p_{D}$ measures the complexity of the model (related to the effective number of parameters) knowing the deviance evaluated at the posterior mean of the parameters $D(\hat{\theta})$ :

$$
p_{D}=\bar{D}-D(\hat{\theta})
$$

The model is preferable for low values of the DIC. To compare two models, a difference more than 10 in the DIC score is supposed to be significant.
2.5. Reliability estimation. The Bayesian estimator permits to determine the posterior densities of the parameters. Consequently, the mean, the median and the percentile values will have to be calculated. The expected value of reliability for an operating time $T$ is determined by the formula

$$
E[R(T \mid \text { Data })]=\int R(T) p(\theta \mid \text { Data }) \mathrm{d} \theta
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. MCMC simulation of the two Weibull parameters: with non-informative priors (a), with informative priors (b).

The two sided Credibility Interval (CI) for reliability is defined by

$$
C I=\int_{R_{l}(T)}^{R_{u}(T)} f(R \mid \text { Data }, T) \mathrm{d} R
$$

$\left[R_{l}, R_{u}\right]$ is the variation interval of reliability.
Example 1. Consider the example regarding LCD lamp projector failure times discussed by Hamada et al. (2008).

Data failures (in hours of projection) are (387, 182, $244,600,627,332,418,300,798,584,660,39,274,174$, $50,34,1895,158,974,345,1755,1752,473,81,954$, $1407,230,464,380,131,1205), \mathrm{N}=31$.

The corresponding Winbugs (David et al., 2000) script of the Weibull model is as follows:

```
model
{
for (i in 1:N) {
duration[i] 'dweib(alpha, lambda)
}
# non-informative priors
alpha 'dgamma (0.5, 0.0001) # alpha is parameter a
lambda 'dgamma (0.5, 0.0001) # lamda is b'a
# informative priors
# alpha 'dgamma (1, 1)
# lambda 'dgamma (2.5, 2350)
}
```

The simulation was carried out with three chains whose initial values are dispersed (Fig. 2).

The $p$-value for the Weibull models with two priors: informative and non-informative, using the statistical Watson test, is presented in Table 1. The script of the program is (Kelly and Smith, 2009)

```
model
{
for (i in 1:N)
{
time[i] 'dweib (alpha, lambda) # alpha is parameter a
time.rep[i] 'dweib(alpha, lambda) # lamda is b'a
time-ranked[i] <- ranked(time[], i)
time.rep-ranked[i] <- ranked(time.rep[], i)
F.obs[i] <- 1-exp(-lambda*pow(time-ranked[i], alpha))
F.rep[i] <- 1-exp(-lambda*pow(time.rep-ranked[i], alpha))
diff.obs[i] <- pow(F.obs[i]-(2*i-1)/(2*N), 2)
diff.rep[i] <- pow(F.rep[i]-(2*i-1)/(2*N), 2)
}
CVM.obs <- sum(diff.obs[])
CVM.rep <- sum(diff.rep[])
p.value <- step(CVM.rep-CVM.obs)
alpha 'dgamma (0.5, 0.0001)#priori non-informative
lambda'dgamma (0.5, 0.0001)
# alpha'dgamma (1, 1)#priori informative
# lambda'dgamma (2.5, 2350)
}
```

The DIC score is calculated by the Winbugs software. Results of analysis for a Weibull model and an exponential model built around the same data are presented in Table 1.

As can be observed, the Weibull model with noninformative prior gave the $p$-value closest to 0.5 . Although the differences between the various computed values of
the DIC are not too significant, one can notice that the same model gave the lowest value of the DIC. Clearly, according to these results, the Weibull model with noninformative prior is most representative for this set of data.

For the drawing of reliability (Fig. 3.), the simulated chains of alpha and lambda are exported to the R language environment (CoreTeam, 2008) using the Brugs package. The script allowing calculating the reliability with a credibility interval of $90 \%$ is

```
t=seq(1,18000)
p5=0*t; p50=0*t; p95=0*t
for(j in 1:18000)
{
R=exp(-lambda*(t[j])'alpha) # Reliability
q=quantile(R,c(.05,.5,.95))
p5[j]=q[1]; p50[j]=q[2]; p95[j]=q[3]
}
```

Table 1. p-value and DIC for Weibull and exponential models.


## 3. Bayesian network approach for reliability modeling

3.1. Introduction. Contrary to the fault tree and reliability diagram models, the graphic BN reliability model can have an identical form for two different structures such as parallel or series. But the distinction consists in the expression of the conditional probabilities. To distinguish between the two structures, it is possible to mention ' $A N D$ ' or ' $O R$ ' close to the global reliability node.
3.2. Serial reliability model. The representation of this serial reliability form between two components $A$ and $B$ is portrayed by the BN of Fig. 4. We assume that value 1 indicates success and 0 stands for failure. The joint probability of the network is expressed as follows:

$$
P(S, A, B)=P(A) P(B) P(S \mid A, B)
$$

The marginalisation of the probability of success or failure for the total system $S$ is

$$
P(S)=\sum_{A, B} P(A) P(B) P(S \mid A, B)
$$

The probability of success of the whole system $P(S=1)$ can be calculated knowing the properties of

![img-2.jpeg](img-2.jpeg)

Fig. 3. Reliability curves median and $90 \%$ quantiles.
a serial system resumed by the conditional probabilities

$$
\begin{aligned}
& P(S=1 \mid A=0, B=0)=0 \\
& P(S=1 \mid A=0, B=1)=0 \\
& P(S=1 \mid A=1, B=0)=0 \\
& P(S=1 \mid A=1, B=1)=1
\end{aligned}
$$

This yields

$$
P(S=1)=P(A=1) P(B=1)
$$

Example 2. Consider the global serial system made up of three components, $A, B$ and $C$, and the following failure data:

- Component $A:(35,38,42,56,58,61,63,76,81,83$, $86,90,99,104,113,114,117,119,141,183), N=$ 20.
- Component $B:(450,460,1150,1150,1560,1600$, $1660,1850,1850,1850,1850,1850,2030,2030$, 2030, 2070, 2070,2080, 2200, 3000, 3000, 3000, $3000,3100,3200,3450,3750,3750,4150,4150$, $4150,4150,4300,4300,4300,4600,4850$, $4850,4850,4850,5000,5000,5000,6100,6100$, $6100,6100,6300,6450,6450,6700,7450,7800$, $7800,8100,8100,8200,8500,8500,8500,8750$, $8750,8750,9400,9900,10100,10100,10100$, $11500), \mathrm{N}=70$.
- Component $C:(657,384,142,54,42,102,110,37$, $16,87,100,17), N=12$.

All the components are supposed to have a Weibull pdf. The corresponding BN reliability model involving uncertain parameters is shown in Fig. 5. To determine the different reliabilities, simulated chains for the three components are created independently, and the following script provides the reliability of the global system:

```
t=seq(1,9000)
p5=0*t; p50=0*t ; p95=0*t
```

![img-3.jpeg](img-3.jpeg)

Fig. 4. Serial form of reliability: FT (a), BN (b).
for(j in 1:9000)
\{
$\mathrm{Rs}=\exp \left(-\operatorname{lambda}_{*} \mathrm{~A}^{*}(\mathrm{t}[j])^{*} \text { alpha } \_\mathrm{A}\right)$
*exp(-lambda_B*(t[j])'alpha_B)
*exp(-lambda_C*(t[j])'alpha_C)
q=quantile(Rs,c(.05,.5,.95))
p5[j]=q[1]; p50[j]=q[2]; p95[j]=q[3]
\}

The reliability curves are displayed in Fig. 6.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Serial form of reliability of a three components system: FT (a), BN (b).
3.3. Parallel reliability model. The representation of the parallel structure between two components $A$ and $B$ is portrayed by the BN of Fig. 7.

However, according to the definition of a parallel system, the only true conditional probability is

$$
P(S=0 \mid A=0, B=0)=1
$$

The probability of failure of the whole system $P(S=0)$ is calculated by

$$
P(S=0)=P(A=0) P(B=0)
$$

3.4. Modeling with the covering factor. For the modeling of redundant systems, it is interesting to take into account the covering factor (Portinale et al., 2005). It is

![img-5.jpeg](img-5.jpeg)

Fig. 6. Reliability curves with $90 \%$ quantiles.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Parallel form of reliability: FT (a), BN (b).
defined as the probability that a failure in the recovery mechanism of a redundant system can cause the failure of the global structure. However, this mechanism can be imperfect, which makes the redundancy inactive. The BN equivalent model is just like the serial one, but the conditional probabilities are defined as follows:

$$
\begin{aligned}
& P(S=1 \mid A=1, B=1)=1 \\
& P(S=1 \mid A=1, B=0)=1-c \\
& P(S=1 \mid A=0, B=1)=1-c \\
& P(S=1 \mid A=0, B=0)=0
\end{aligned}
$$

where $c$ is the covering factor.
Example 3. Let us take the example of a redundant system composed of two identical units with the Weibull pdf. The parameters $a$ and $b$ are supposed to be respectively 1.1 and 100000 . Figure 8 illustrates a comparison of reliability curves corresponding to a system without redundancy, redundancy with $c=0.2$ and redundancy without the covering factor $(c=0)$. Clearly, taking into account this factor affects the reliability of the global system.
3.5. Systems with a common cause of failure. Generally, systems with a common cause of failure are represented by the FT of Fig. 9. According to Bobbio et al.
![img-7.jpeg](img-7.jpeg)

Fig. 8. Reliability curves.
(2001), the BN reliability representation of this structure does not change from the last presented model, but conditional probabilities will depend on a factor $\alpha_{C C F}$ representing the probability of the common cause of failure. Therefore, the conditional probabilities will be defined as follows:

$$
\begin{aligned}
& P(S=1 \mid A=1, B=1)=1 \\
& P(S=1 \mid A=1, B=0)=\alpha_{C C F} \\
& P(S=1 \mid A=0, B=1)=\alpha_{C C F} \\
& P(S=1 \mid A=0, B=0)=\alpha_{C C F}
\end{aligned}
$$

The probability of success of the system $S$ will be

$$
P(S=1)=\alpha_{C C F}\left(1-\pi_{A} \pi_{B}\right)+\pi_{A} \pi_{B}
$$

where $\pi_{A}$ and $\pi_{B}$ are the reliabilities of components $A$ and $B$.
![img-8.jpeg](img-8.jpeg)

Fig. 9. FT model for a two components system with a CCF.
3.6. Systems with an unknown structure. When the global system has a complex structure which can be represented neither by a reliability diagram nor by an FT,

the BN approach will be an efficient framework for reliability modelling (Wilson and Huzurbazar, 2007; Hamada et al., 2008). This recent approach is used not only in this context, but also for design of reliable systems. Let us study the independence of the operation of two components $A$ and $B$ in a global system $S$ via an example. The BN approach allows capturing the interaction of the two components to produce a totally faulty, healthy or degraded system. The conditional probabilities for such a structure are given by the following expressions:

$$
P(S=1 \mid A=i, B=j) \sim \alpha_{k}
$$

The variables $i$ and $j$ correspond to the two cases of success or failure ( 1 or 0 ), $\alpha_{k}$ are probability parameters which can be estimated. It is possible to associate prior distributions for these parameters. If $\alpha_{k}$ varies in bounded intervals, one can use the uniform density for the conditional probabilities with additional parameters $\beta_{k}$,

$$
P(S=1 \mid A=i, B=j) \sim \operatorname{Uniform}\left(\alpha_{k}, \beta_{k}\right)
$$

It is important here to note that the studied uncertitude concerns only the structure of the system. When we deal with uncertain parameters of reliability, this will appear in reliabilities $\pi_{A}$ and $\pi_{B}$ (Eqn. (27)).
![img-9.jpeg](img-9.jpeg)

Fig. 10. Reliability of a global system with an unknown structure with $90 \%$ quantiles.

Example 4. Let us take the same data as in Example 2. Writing the conditional probabilities for this structure can be performed using (34) applied to three components, which yields

$$
\begin{aligned}
& P(S=1 \mid A=1, B=1, C=1)=\alpha_{1} \\
& P(S=1 \mid A=0, B=1, C=1)=\alpha_{2} \\
& P(S=1 \mid A=1, B=0, C=1)=\alpha_{3} \\
& P(S=1 \mid A=1, B=1, C=0)=\alpha_{4}
\end{aligned}
$$

$$
\begin{aligned}
& P(S=1 \mid A=0, B=0, C=1)=\alpha_{5} \\
& P(S=1 \mid A=1, B=0, C=0)=\alpha_{6} \\
& P(S=1 \mid A=0, B=1, C=0)=\alpha_{7} \\
& P(S=1 \mid A=0, B=0, C=0)=\alpha_{8}
\end{aligned}
$$

The probability of success of the global system $S$ is calculated by the relation

$$
\begin{aligned}
p(S= & 1) \\
= & \alpha_{1} \pi_{A}(t) \pi_{B}(t) \pi_{C}(t) \\
& +\alpha_{2}\left(1-\pi_{A}(t)\right) \pi_{B}(t) \pi_{C}(t) \\
& +\alpha_{3} \pi_{A}(t)\left(1-\pi_{B}(t)\right) \pi_{C}(t) \\
& +\alpha_{4} \pi_{A}(t) \pi_{B}(t)\left(1-\pi_{C}(t)\right) \\
& +\alpha_{5}\left(1-\pi_{A}(t)\right)\left(1-\pi_{B}(t)\right) \pi_{C}(t) \\
& +\alpha_{6} \pi_{A}(t)\left(1-\pi_{B}(t)\right)\left(1-\pi_{C}(t)\right) \\
& +\alpha_{7}\left(1-\pi_{A}(t)\right) \pi_{B}(t)\left(1-\pi_{C}(t)\right) \\
& +\alpha_{8}\left(1-\pi_{A}(t)\right)\left(1-\pi_{B}(t)\right)\left(1-\pi_{C}(t)\right)
\end{aligned}
$$

where $\pi_{A}, \pi_{B}$ and $\pi_{C}$ are the reliabilities of components $A, B$ and $C$. As an application, the parameters $\alpha_{\{i=1, \ldots, n\}}$ are supposed to be respectively $\{0.98,0.8,0.7,0.75,0.55,0.5,0.45,0.03\}$. The reliability curves of the global system (with $90 \%$ quantiles) are displayed in Fig. 10. As can be observed, the reliability of this structure is 0.2 at the beginning of the operation time. Consequently, given the parameters above, a system with this structure is not reliable.

## 4. Bayesian networks and fault diagnosis

4.1. Introduction. In the last decade, there has been growing a common area between BNs and FDI. Mehranbod et al. (2005) a method for sensor fault detection and identification. It consists in using a multi-stage BN to detect different sensor fault types (bias, drift and noise). This paper also aims to reduce the size of required conditional probability data. Improving decision making in Analytical Redundancy Relations (ARRs) based approaches using BNs and reliability data is treated by Weber et al. (2006). In ARR based approaches, a binary Fault Signature Matrix (FSM) is systematically generated, but making the final binary decision is not always feasible because of the problems revealed by such a method (unknown and identical failure signatures). The authors proposed a DBN (a 2-TBN model with two time slices: $(t-1)$ and $(t)$ ) incorporating nodes with exponential failure distributions for the components. The approach supposes that ARRs are already generated, and it is not proposed for a specific generation method. The given approach is applied only for components whose distribution of failure is exponential.

The structure of the network becomes more complex if the number of components increases since we need two

time slices for every component. Zaidi et al. (2010) proposed the same method with application of an ARR Bond Graph (BG) based approach. The BG is a unified multidisciplinary graphical tool widely used not only for dynamic modelling but also for FDI because of its structural and causal proprieties. This diagnostic approach consists in associating the evaluated residuals and the components reliability data to build a hybrid Bayesian network. This network is used in two distinct inference procedures: one for the continuous part and the other for the discrete part. The continuous nodes of the network are the prior probabilities of the components failures, which are used by the inference procedure on the discrete part to compute the posterior probabilities of the failures. This approach can be employed for large-scale systems with components having all types of failure distributions (the one applied is Weibull's).

Koller and Lerner (2000) elicited dynamic Bayesian networks for monitoring dynamic systems. It is pointed out that hidden Markov model processes and Kalman filters are particular cases of DBNs. The structure of the BN is deduced from the temporal causal graph, which is a representation deduced from the BG model. Anderson et al. (2004) studied the comparison between different filtering algorithms with the DBN and noted the interest of the particle filtering approach with a proposal distribution generated by an Unscented Kalman Filter (UKF) for networks of large size. Roychoudhury et al. (2006) proposed a Bayesian approach for the monitoring of model parameter deviations. The elicited FDI architecture is an observer based on a DBN modeling the nominal operation of the system. The structure of the network is also deduced from the BG model. The inference algorithm is the Extended Kalman Filter (EKF) to treat the system non-linearities. The authors used a qualitative reasoning from the TCG to generate the possible hypotheses of the failure. To achieve the isolation, a DBN incorporating discrete nodes is used to indicate the possible failures of the continuous parameters.

Cholewa et al. (2010) proposed a belief-networkbased diagnostic model. This model incorporates modelbased and symptom-based diagnostics. It consists of a parallel multi-stage Belief-Network Based Model (BNBM). The first stage incorporates transformation blocks carrying out data preprocessing tasks. The second stage comprises mapping blocks and the third one includes belief networks, post processing and result visualisation. This strategy of diagnosis may use approaches such as One-Class Classifiers (OCCs) and memetic algorithms for model tuning and optimization of output data. Zhang and Hoo (2011) address FDI in complex plants by using a hierarchical strategy involving different modeling approaches. The BG tool is used as a first physical domain layer. Thereafter, Principle Component Analysis (PCA) to reduce the data dimension and a Discrete Wavelet Trans-
form (DWT) is applied to abstract the dynamics of the plant at different scales. Finally, in the last layer, BNs are used to describe the conditional dependence between faulty domains and fault signatures.
4.2. Application to reliability modeling and fault diagnosis. In the concept of Bayesian fault diagnosis, providing continuous decision variables in the form of posterior probabilities of failures is of great interest for monitoring the degradation of components. These variables can be used for further intelligent supervision tasks; programming preventive maintenance, analysis of the failure cost by using utility nodes, risk based reconfiguration of the faulty system by controlling its global or partial reliability (prognosis tasks). To ensure high availability and system safety for today's industry, it is convenient to introduce the notion of fault tolerant control. A number of recent studies have attempted to link, for autonomous systems, the control performance requirements and overall system reliability. This is perhaps the great challenge of modern automation. In this field we can mention the works of Hongbin et al. (2007) and Khelassi et al. (2011).
4.2.1. Bayesian fault diagnosis model. Here we shall introduce an approach providing these posterior probabilities in model based diagnosis. It consists in linking residuals deduced from the physical model constraints and the reliabilities of different components in the process to be monitored (Weber et al., 2006; Zaidi et al., 2010).

Suppose our system is composed of $n$ components $C=\left\{C_{i} ; 1 \leq i \leq n\right\}$ with Weibull distributions of failures. The Bayesian model of decision contains random variables associated to the residuals $r=\left\{r_{j} ; 1 \leq j \leq\right.$ $p\}$, to the components as well as the Bayesian reliability model of these components. The proposed Bayesian decision-making model is displayed in Fig. 11. An arc that joins node $C_{i}$ to node $r_{j}$ (we really join associated random variables) indicates that $r_{j}$ is sensitive to the failure of the component $C_{i}$. For a residual $r_{j}$ there are two states $\{D($ Detected $), N D($ NotDetected $)\}$, and we have also two states $\{F($ Faulty $), S($ Safe $)\}$ for a component $C_{i}$. Every component $C_{i}$ is associated with its reliability $R_{i}$.

As can be observed, this structure is hybrid: there are discrete and continuous nodes. A hybrid BN represents a probability distribution over a set of random variables where some are discrete and others are continuous. In the literature, the most widely used subclass of hybrid BNs is the Conditional Linear Gaussian (CLG) model (Lauritzen and Jensen, 1999). This model involves discrete parents and continuous leaves. Many kinds of inference algorithms can be stated: exact inference (Lerner et al., 2001), approximate inference (Koller et al., 1999), dynamic discretisation (Kozlov and Koller, 1997), truncated exponen-

tial mixtures (Moral et al., 2001).
![img-10.jpeg](img-10.jpeg)

Fig. 11. BN diagnostic model: continuous part (a), discrete part (b).

The network displayed in Fig. 11 can be treated as an association of a discrete BN and a Continuous BN (CBN). The CBN permits to prepare the prior information on the failure of the component. Thus when a residual is detected at instant $t$, the component $C_{i}$ has the prior probabilities: $P\left(C_{i}=\right.$ Faulty $)=F_{i}(t)=1-R_{i}(t)$. (The function $F_{i}$ signifies the Cumulative Distribution Function (CDF).)

The discrete part possesses a structure that depends on the failure signatures (i.e., the FSM); when a residual $r_{j}$ is not sensitive to the failure of a component $C_{i}$, no arc is pulled from node $C_{i}$ toward node $r_{j}$. The inference of the two parts can be performed separately. After the detection of residuals, the posterior probabilities of the failures $p\left(C_{i} \mid r_{1}, \ldots, r_{p}\right)$ can be determined by inference on the discrete part of the network.
4.2.2. Application example. The approach is simulated on a system (Fig. 12) made of two tanks $T_{1}$ and $T_{2}$, two valves $V_{1}$ and $V_{2}$, two level sensors $L_{1}$ (De1) and $L_{2}$ (De2), a pump $P$, a proportional-integral controller (PI) and a bang bang controller $K$ (On-Off). Figure 13 summarizes the FSM of the monitored system. As can be observed, faults on $V_{2}$ and $T_{2}$ are not isolable.

The reliability parameters are supposed to be certain and follow a Weibull pdf. The failure rates are displayed in Fig. 14. For the inference of the discrete part of the diagnostic model, we used the free software Genie 2.0 (http://genie.sis.pitt.edu) after introducing the prior probabilities of false alarms and non-detection ( $P f a_{i j}$ and $P n d_{i j}$ ) which are supposed to be identical for all components ( $P f a=0.05, P n d=0.02$ ).

We suppose, as a simulation scenario, to have the residual $\left[r_{1}, r_{2}, r_{3}, r_{4}, r_{5}\right]=[0,0,0,0,1]$ after 20000 operating hours. Normally, this corresponds to the failure of both $V_{2}$ and $T_{2}$. Figure 15. shows the results of analysis for isolation. The classic method gives the same probability of failure for both components. We can notice the posterior probabilities of failures ( 0.74 and 0.51 ) for valve
![img-11.jpeg](img-11.jpeg)

Fig. 12. Example of a two tank system.
$V_{2}$ and tank $T_{2}$. The global reliability of the system is $R s=0.006255$. One can deduce that $V_{2}$ is the most probable defective component for this simulation scenario.
4.2.3. Diagnosis with dynamic Bayesian networks. As stated in the first section of this paper, DBNs are used with two main approaches: event based and time-sliced. The latter is known with the concept of TBNs which is widespread in the field of fault diagnosis. In this part we will introduce this concept applied to fault diagnosis and decision in supervision tasks. First, we can simply say that a DBN is a graphical description of systems evolving over time, and this is more general than static Bayesian networks used in previous sections. This model will enable users to monitor and update the system as time proceeds, and even predict, for some applications, further behaviour of the system. A DBN can be described by a probability distribution function on the sequence of $T$ hidden-state variables $X=\left\{X_{0}, \ldots, X_{T-1}\right\}$ and the sequence of $T$ observable variables $Y=\left\{Y_{0}, \ldots, Y_{T-1}\right\}$, where $T$ is the time boundary for the given event we are investigating. This can be expressed by the following term:

$$
P(X, Y)=\prod_{t=1}^{T-1} P\left(X_{t} \mid X_{t-1}\right) \prod_{t=0}^{T-1} P\left(Y_{t} \mid X_{t}\right) P\left(X_{0}\right)
$$

In order to completely specify a DBN, we need to define three sets of parameters:

- State transition pdfs $P\left(X_{t} \mid X_{t-1}\right)$, specifying time dependencies between the states.


Fig. 13. Fault signature matrix of the two-tank system.


Fig. 14. Failure parameters of the two-tank system.

![img-12.jpeg](img-12.jpeg)

Fig. 15. Probabilities of failures for the simulated scenario.

- Observation pdfs $P\left(Y_{t} \mid X_{t}\right)$, specifying dependencies of observation nodes regarding the other nodes at time slice $t$.
- Initial state distribution $P\left(X_{0}\right)$, bringing initial probability distribution in the beginning of the process.

Knowing that we deal with a 2-TBN model, the transition probabilities for any variable are determined completely by the value of the variables in the current and the previous time step-this is what we call the Markov property. First order stationarity is ensured for systems with an exponential pdf of failure. On the other hand, for the Weibull pdf, this stationarity is not ensured for the whole life cycle of the component. To overcome this problem, we will suppose to have stationarity for a certain sequence of time. This assumption is possible especially for real time diagnostics, where the sampling period is extremely small to depict the dynamics of residuals. Here, as an application for diagnosis of the two tank system, we use the concept of IOHMM modeled by a DBN (for more details, Ben Salem et al., 2006; Murphy, 2002). The diagnostic model is illustrated in Fig. 16.

The DBN diagnosis model whose static form is presented in the previous subsection works as follows:

- The inputs $U_{t-1}^{(i)}$ are the results of the inference by the continuous part of the diagnosis model (Fig. 11(a)), which represents the reliabilities of components supposed to be constant during the sequence $T$ of time slices where we invertigate. The variable $i$ is used to differ sequences.
- The states $X_{t-1}^{(i)}$ are the component states; they are determined with the CPD $p\left(X_{t-1}^{(i)} \mid U_{t-1}^{(i)}\right)$.
- The states $Y_{t-1}^{(i)}$ are the results of the evaluations of residuals $r_{j}$; the associated CPD is $p\left(Y_{t-1}^{(i)} \mid X_{t-1}^{(i)}\right)$.
- The current states $X_{t}^{(i)}$ are calculated by the following conditional probabilities:

$$ \begin{aligned} & p\left(X_{t}^{(i)}=\text { Faulty } \mid X_{t-1}^{(i)}=\text { Faulty }\right)=1, \ & p\left(X_{t}^{(i)}=\text { Faulty } \mid X_{t-1}^{(i)}=\text { Safe }\right)=0, \ & p\left(X_{t}^{(i)}=\text { Safe } \mid X_{t-1}^{(i)}=\text { Faulty }\right)=1-R_{C}^{(i)}(T), \ & p\left(X_{t}^{(i)}=\text { Safe } \mid X_{t-1}^{(i)}=\text { Safe }\right)=R_{C}^{(i)}(T), \end{aligned} $$

where $R_{C}^{(i)}(T)$ are the reliabilities of components estimated during the sequence $T$. The DBN model in the compact form using the same sofware is displayed in Fig. 17.

Here we must note that inputs are not shown because, as we mentioned before, the model is hybrid and the inference of the continuous part can be made independently knowing that we deal here with certain Weibull parameters, so there is no problem of reliability estimation. We suppose, as a simulated scenario, to have an active residual $r_{5}$ for one slice time, and it persists after that until the end of the sequence. As can be observed in Fig. 18, there is no action of diagnosis for that slice, and this can be explained as a robustness advantage of the DBN against false alarms. When the residual persists, the simulation shows a posterior probability of the component $V_{2}$ failure slightly greater than the one corresponding to $T_{2}$.

![img-13.jpeg](img-13.jpeg)

Fig. 16. IOHMM represented by a DBN.

## 5. Conclusions

A Bayesian approach to reliability modeling has been introduced. First, we presented Bayesian estimation of pdf parameters with the hierarchical Bayesian approach. Thereafter, the estimation of the reliability was evoked and the incorporation of this model in a BN framework for the modeling of different types of reliability structures (serial, parallel, active redundancy, systems with a

![img-14.jpeg](img-14.jpeg)

Fig. 17. DBN model (in compact form) of the diagnosis module.
![img-15.jpeg](img-15.jpeg)

Fig. 18. Simulation results for the DBN structure.
common cause of failures, an unknown structure). It was shown how this approach permits the modelling of nontraditional operating modes and the most complex systems which cannot be modelled with the FT and the RD. Thereafter, the use of BN in the fault detection and isolation area was pointed out by the monitoring of a two-tank system.

We notice the interest of the DBN framework in several stated diagnosis approaches, and especially when we aim to reduce false alarms. The approaches presented here were illustrated with systems having the Weibull pdf as a general case of the exponential one. Clearly, as a final conclusion, one can deduce the great richness of the BN contribution in the reliability and diagnosis fields.

## Acknowledgment

This research work is supported by the LAGIS (Laboratoire d’Automatique, Génie Informatique et Signal, Lille, France) and LACS (Laboratoire d’Analyse et Commande des Systèmes, Tunis, Tunisia) laboratories.
