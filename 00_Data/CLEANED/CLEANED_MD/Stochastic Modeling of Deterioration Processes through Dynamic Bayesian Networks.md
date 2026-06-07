This article appeared in:
Journal of Engineering Mechanics, Trans. ASCE, 2009, 135(10): 1089-1099.
http://dx.doi.org/10.1061/(ASCE)EM.1943-7889.0000024

# Stochastic modeling of deterioration processes through dynamic Bayesian networks 

Daniel Straub ${ }^{1}$


#### Abstract

A generic framework for stochastic modeling of deterioration processes is proposed, based on dynamic Bayesian networks (DBN). The framework facilitates computationally efficient and robust reliability analysis and, in particular, Bayesian updating of the model with measurements, monitoring and inspection results. These properties make it ideally suited for near-real time applications in asset integrity management and deterioration control. The framework is demonstrated and investigated through two applications to probabilistic modeling of fatigue crack growth.


## Keywords

Bayesian analysis; cracking; deterioration; inspection; Markov chain; monitoring; stochastic processes.

[^0]
[^0]:    ${ }^{1}$ Associate Professor, Engineering Risk Analysis Group, Technische Universität München, Arcisstr. 21, 80290 Munich, Germany, straub@tum.de

# Introduction 

The modeling of deterioration is subject to significant uncertainty, which arises from a simplistic representation of the actual physical processes (typically through empirical or semi-empirical models) and from limited information on material, environmental and loading characteristics. This uncertainty has been addressed in stochastic models of deterioration processes in the past (Committee on Fatigue and Fracture Reliability 1982; Yang 1994; Melchers 1999). Additionally, observations of the deterioration processes or influencing factors (e.g., from inspection and monitoring) have been included in the models through Bayesian updating (Tang 1973; Madsen et al. 1986), in particular in the context of life-cycle optimization and inspection planning (Thoft-Christensen and Sørensen 1987; Pedersen et al. 1992; Straub and Faber 2006). In principle, the methods of structural reliability enable efficient Bayesian updating of any stochastic model with any kind of information (Madsen et al. 1986). In reality, however, algorithmic difficulties occur (Sindel and Rackwitz 1998), which can make the computations cumbersome and hinder the implementation in software that is run by engineers who are not experts in structural reliability methods.

This paper proposes a novel computational framework for evaluating stochastic deterioration models. The strength of the framework is its computational efficiency and robustness when performing Bayesian updating. It is based on Bayesian networks (BN), a modeling tool that originated in computer science (Pearl 1988; Jensen 2001; Russell and Norvig 2003), but has recently had a number of applications in engineering risk and reliability analysis (Faber et al. 2002; Friis-Hansen 2004; Grêt-Regamey and Straub 2006; Langseth and Portinale 2007). Few researchers have applied BN in the context of deterioration modeling. Friis-Hansen (2001) studies the application of BN for deterioration modeling and inspection planning by means of an example considering fatigue crack growth; Montes-Iturrizaga et al. (2009) use BN for optimizing inspection efforts for offshore structures subject to multiple deterioration mechanisms; Attoh-Okine and Bowers (2006) present an empirical model of bridge deterioration using Bayesian networks. In contrast to these previous publications, which make use of the BN

capabilities mainly for modeling the system aspects or for optimizing inspection and maintenance decision, the present paper focuses on the deterioration modeling. The resulting computational framework enables efficient and robust reliability updating for realistic deterioration models. By robust it is understood that the reliability updating can be performed in an automated manner, not requiring the input from an expert in reliability analysis. This is in contrast to existing efficient computational methods, such as first/second-order reliability methods (FORM/SORM), importance sampling or subset simulation, and facilitates the implementation in software that can be used by the lay engineer for the planning of inspection, repair and maintenance activities, as well as in automated alarm systems based on monitoring data.

The proposed framework is demonstrated and investigated through two applications considering fatigue crack growth, which are representative for a large number of deterioration mechanisms subject to uncertainty.

# Relation to Markov process models 

Dynamic Bayesian networks (DBN) can be interpreted as a generalization of Markov process models, which have frequently been applied for the modeling of deterioration (Bogdanoff and Kozin 1985; Spencer and Tang 1988; Cesare et al. 1992; Ishikawa et al. 1993; Rocha and Schuëller 1996; Mishalani and Madanat 2002). Markov deterioration processes are characterized by the fact that for a given condition at time $t_{1}$, the condition at any future time $t_{2}>t_{1}$ is statistically independent of the condition at any past time $t_{0}<t_{1}$. It is noted that the Markovian assumption does not hold in engineering practice, where epistemic uncertainties are prevalent (Yang 1994; Melchers 1999; Mishalani and Madanat 2002). Epistemic uncertainties are often time-invariant (e.g., uncertainties due to simplistic parametrical models, due to limited statistical data for empirical models, or due to incomplete knowledge of influencing parameters), thus invalidating the Markovian assumption. To overcome this shortcoming, here a deterioration model is formulated that corresponds to a Markov process model conditional on time-invariant random variables. The DBN technique enables the efficient computation of such models.

Among Markov process models, it can be distinguished between two fundamentally different approaches: models that are based on an underlying parametric model (Ishikawa

et al. 1993) and models that are purely empirical (Cesare et al. 1992; Mishalani and Madanat 2002). The latter are typically finite space Markov chain models. Although the DBN approach can be applied to both models, this paper focuses on parametric models, which are preferable in that they facilitate learning and transferability.

# Dynamic Bayesian networks 

The textbooks by Pearl (1988), Jensen (2001) and Russell and Norvig (2003) provide an introduction to BN. In the following, a concise introduction to BN is given, limited to the case of discrete random variables, i.e., random variables that are defined in a finite space.

BN are probabilistic models based on directed acyclic graphs that represent $p(\mathbf{x})$, the joint probability mass function (PMF) of a set of random variables $\mathbf{X}$. The space of $\mathbf{X}$, i.e., the number of outcome states of $\mathbf{X}$ for which $p(\mathbf{x})$ must be computed, increases exponentially with the number of variables in $\mathbf{X}$, but BN enable an efficient modeling by factoring the joint probability distribution into conditional (local) distributions for each variable.
![img-0.jpeg](img-0.jpeg)

Figure 1. A simple Bayesian network.

A simple BN is illustrated in Figure 1. It consists of three discrete random variables $X_{1}, X_{2}, X_{3} . X_{1}$ is a parent of $X_{2}$ and $X_{3}$, which are children of the former. The PMF of each variable is defined conditional on its parents and the joint PMF of this network is given as a product of these conditional probabilities:

$$
p\left(x_{1}, x_{2}, x_{3}\right)=p\left(x_{1}\right) p\left(x_{2} \mid x_{1}\right) p\left(x_{3} \mid x_{1}\right)
$$

Wherein $p\left(x_{i} \mid x_{j}\right)$ is the conditional PMF of $X_{i}$ given $X_{j}=x_{j}$. More generally, the joint probability mass function for any BN having discrete variables is given as

$$
p(\mathbf{x})=p\left(x_{1}, \ldots, x_{N}\right)=\prod_{i=1}^{N} p\left(x_{i} \mid \mathbf{p a}_{i}\right)
$$

where $\mathbf{p a}_{i}$ is the set of realizations of the parents of $X_{i}$. The basic supposition of BNs is that each variable $X_{i}$ is independent of all other variables for given values of the variables in its Markov blanket, which includes the parents of $X_{i}$, the children of $X_{i}$ and the parents of the children of $X_{i}$.

The BN allows entering evidence: probabilities in the network are updated when new information becomes available. For example, when the state of $X_{2}$ in the network in Figure 1 is observed to be $e$, this information propagates through the network and the joint PMF of $X_{1}$ and $X_{3}$ change according to Bayes' rule to

$$
p\left(x_{1}, x_{3} \mid e\right)=\frac{p\left(x_{1}, e, x_{3}\right)}{p(e)}=\frac{p\left(x_{1}\right) p\left(e \mid x_{1}\right) p\left(x_{3} \mid x_{1}\right)}{\sum_{X_{1}} p\left(x_{1}\right) p\left(e \mid x_{1}\right)}
$$

Consequently the marginal posterior probabilities of $X_{1}$ and $X_{3}$ are also updated. Note that the common influencing variable $X_{1}$ introduces dependence between $X_{2}$ and $X_{3}$, but evidence can change the dependence among variables in the network; in the above example, if $X_{1}$ is known, $X_{2}$ and $X_{3}$ become independent. For given sets of evidence, it is possible to infer the independence assumptions encoded in the graphical structure using the rules of $d$-separation (Pearl 1988).

Dynamic Bayesian networks (DBN) are a special class of Bayesian networks, which represent stochastic processes. They consist of a sequence of slices, each of which consists of one or more BN nodes. The slices are connected by directed links from nodes in slice $i$ to nodes in slice $i+1$. Figure 2 shows an example of a DBN. If the model structure and the conditional probability tables are identical for all slices except the first, then the DBN is homogenous. As for any BN, the joint PMF of the variables in the DBN is defined through Equation (2), but a number of inference algorithms are available that are developed especially for the DBN structure (Murphy 2002).
![img-1.jpeg](img-1.jpeg)

# Modeling deterioration processes using dynamic Bayesian networks 

## Probabilistic modeling of deterioration processes

Consider a parametric deterioration model $h$ that describes the state of deterioration as a function of time $t$, a set of time-invariant model parameters $\boldsymbol{\theta}$, a set of time-variant model parameters $\boldsymbol{\omega}_{t}=\boldsymbol{\omega}(t)$ and the initial condition $d_{0}$. Deterioration is expressed by defect dimensions $d_{t}$ or an empirical damage index $d_{t}$ at time $t$, e.g., for fatigue, $d_{t}$ is either (a) the depth and/or length of a crack when using a fracture mechanics (FM) based model or (b) the Palmgren-Miner damage when using the empirical model based on SNcurves. The model is written in generic form as

$$
d_{t}=d(t)=h\left(t, d_{0}, \boldsymbol{\theta}, \boldsymbol{\omega}_{1}, \ldots, \boldsymbol{\omega}_{t}\right), \quad t>0
$$

The proposed DBN model does not replace the parametric deterioration model $h$. Instead, the DBN model provides a computational framework that allows accurate and efficient evaluation of $d_{t}$ based on the prior stochastic model of the parameters and including all observations of the deterioration process and any of the parameters. The DBN also facilitates learning about the model parameters $\boldsymbol{\theta}$ and $\boldsymbol{\omega}_{1}, \ldots, \boldsymbol{\omega}_{t}$ based on the observations.

Hereafter, we limit ourselves to modeling deterioration as a discrete time process. Furthermore, in accordance with common deterioration models, we require that the dependence among the $d_{t}$ is conditionally Markovian, i.e.,

$$
f\left(d_{t} \mid d_{0}, \ldots, d_{t-1}, \boldsymbol{\theta}, \boldsymbol{\omega}_{1}, \ldots, \boldsymbol{\omega}_{t}\right)=f\left(d_{t} \mid d_{t-1}, \boldsymbol{\theta}, \boldsymbol{\omega}_{t}\right), \quad t=1,2, \ldots, T
$$

where $f$ denotes the probability density function (PDF). Note that $f\left(d_{t} \mid d_{t-1}, \boldsymbol{\theta}, \boldsymbol{\omega}_{t}\right)$ can vary with $t$, i.e., the conditional Markov process is not homogenous in the general case. Additionally, we require that the time-variant model parameters $\boldsymbol{\omega}_{t}$ are a Markov process conditional on $\boldsymbol{\theta}$ and $d_{t-1}$, i.e.,

$$
f\left(\boldsymbol{\omega}_{t} \mid \boldsymbol{\omega}_{1}, \ldots, \boldsymbol{\omega}_{t-1}, d_{0}, \ldots, d_{t-1}, \boldsymbol{\theta}\right)=f\left(\boldsymbol{\omega}_{t} \mid \boldsymbol{\omega}_{t-1}, d_{t-1}, \boldsymbol{\theta}\right), \quad t=1,2, \ldots, T
$$

Since $d_{t}$ is dependent on the time-invariant uncertain model parameters $\boldsymbol{\theta}$ for given $d_{t-1}$, the deterioration process is not Markovian in the unconditional case, i.e., in general it is $f\left(d_{t} \mid d_{0}, \ldots, d_{t-1}\right) \neq f\left(d_{t} \mid d_{t-1}\right)$.

# Limitations of the model framework 

In the generic model, the model parameters $\boldsymbol{\omega}_{t}$ and $d_{t}$ are assumed to be Markov processes, conditional on $\boldsymbol{\theta}$. This represents a limitation, which, however, is not critical in practice, because most stochastic models of deterioration fit at least approximately in this scheme. In particular, models with exclusively time-invariant random variables are a special instance of the framework. Examples of time-variant models that fit into the above framework are deterioration models based on a Gaussian process $X(t)$ with exponential autocovariance function, Equation (7), since this process is Markovian (Ishikawa et al. 1993).

$$
R_{X X}\left(t_{1}, t_{2}\right)=\operatorname{cov}\left[X\left(t_{1}\right), X\left(t_{2}\right)\right]=\sigma_{X}^{2} \exp \left(-\left|t_{2}-t_{1}\right| / \alpha_{X}\right)
$$

Fortunately, deterioration process models in the literature almost exclusively utilize an exponential autocovariance function. Even if the process is not Gaussian, the Markovian assumption might still be a reasonable approximation. As an example, consider the lognormal process $Y(t)$ with median 1, which can be obtained from a zero-mean Gaussian process $X(t)$ through the transformation $Y(t)=\exp X(t)$. Since $\exp X(t)=1+X(t)+X^{2}(t) / 2!+X^{3}(t) / 3!+\ldots$, the first-order approximation of $Y(t)$ is $Y(t) \approx 1+X(t)$ and the first-order approximation of the autocovariance function is $R_{Y Y}\left(t_{1}, t_{2}\right) \approx R_{X X}\left(t_{1}, t_{2}\right)$, see also (Ortiz and Kiremidjian 1988). If the process $Y(t)$ has an exponential autocovariance function, then $X(t)$ and $Y(t)$ are approximately Markovian. This is utilized in an application later in this paper.

## Representation of the deterioration model as a dynamic Bayesian network

We represent the generic deterioration model as a DBN in Figure 3. Here, the vectors $\boldsymbol{\theta}_{1}, \ldots, \boldsymbol{\theta}_{T}$ are introduced to ensure that the time slices are identical. These vectors are related by the deterministic function $\boldsymbol{\theta}_{t}=\boldsymbol{\theta}_{t-1}, t=2, \ldots, T$ and $\boldsymbol{\theta}_{1}=\boldsymbol{\theta}$. Introducing these additional parameter vectors has no effect on the computational efficiency of the model, yet it can facilitate the model building process and graphical representation of the model.

![img-2.jpeg](img-2.jpeg)

Figure 3. Generic DBN deterioration model.

The links in the DBN shown in Figure 3 correspond to the assumptions of statistical independence among the variables of the generic deterioration model described above. Removing links in a DBN is equivalent to making additional independence assumptions in the model. Therefore, any DBN that is created by removing links from the generic DBN in Figure 3 is a special case of the generic DBN model. As a consequence, the inference algorithm for the generic DBN as presented later can be applied to such DBNs.

The nodes in the generic model represent vectors of variables (e.g., most models have more than one time-invariant model parameter $\boldsymbol{\theta}$ ). Often, it will be computationally beneficial to consider the variables in these vectors as individual nodes in the network. To separate variables allows exploiting conditional independence of variables in the BN, which can increase the computational efficiency of the models.

# Including observations in the model 

A main motivation for the DBN modeling approach is its computational efficiency and robustness for Bayesian updating when new evidence is available. Observations can be available of the initial conditions, the extent of the deterioration $d_{t}$ and the model parameters $\boldsymbol{\theta}$ and $\boldsymbol{\omega}_{1}, \ldots, \boldsymbol{\omega}_{t}$. Examples of such observations are results from inspection and monitoring, observations of the environmental parameters (e.g., measurements of the chemical and physical properties of liquid and gas in a pipeline), observations of failure/survival events. Often these are indirect observations, i.e., observation that only provide an indication of the true parameter values.

Most observations will be independent of the past given the states of the DBN at the time of the observation. Under that condition, each time-slice of the generic DBN can be treated individually by adding the observations as variables in that time-slice. Figure 4 shows the inclusion of an inspection result $Z_{t}$ in the model. Such an inspection result can be a discrete random variable (with two states "indication" and "no-indication" of a defect) or a continuous random variable (a measured defect size). In the former case, the inspection is characterized by a Probability of Detection (PoD) model, in the latter case through a measurement accuracy. In either case it is assumed that the inspection result at time $t$ is independent of all other random variables for given deterioration condition $d_{t}$. The corresponding quantitative model is known as the likelihood function in the context of Bayesian updating, $L\left(d_{t} \mid z_{t}\right) \propto \operatorname{Pr}\left(Z_{t}=z_{t} \mid d_{t}\right)$. This function fully defines the variable $Z_{t}$ in the DBN. Any inspection result is included in the model by instantiating the variable $Z_{t}$ with the observed outcome (evidence). When evaluating the DBN with the evidence, the model is automatically updated.
![img-3.jpeg](img-3.jpeg)

Figure 4. Including an inspection event (observation) in the DBN.

# Computational aspects 

## Continuous versus finite state space models

Most variables in deterioration models are defined in a continuous space. Approximate inference algorithms such as Markov Chain Monte Carlo (MCMC) (Gilks et al 1996; Beck and Au 2002) allow working with BN that involve continuous random variables, yet this flexibility comes at a price. While it is possible to prove convergence of the algorithms in the limit, the rate of convergence is unknown and can be extremely slow, therefore, the algorithms might not converge in practical applications. This problem is intensified by the fact that the resulting DBN models can be very large, and that the Gibbs sampler, which is an efficient MCMC inference algorithm for large BN, cannot handle deterministic relations among variables (Hrycej 1990). Approximate inference algorithms might therefore not be suitable for many of the envisaged applications, which involve the updating of the probabilistic model in a near-real-time manner, and they will not be studied further here. However, as long as the amount of evidence is low, approximate inference algorithms such as stochastic simulation or evidence weighting perform well and are easily implemented. This will be used for validation purposes of the discrete model.

In the remainder of the paper, we focus on DBN models wherein all random variables are defined in a finite space. The nodes in the generic DBN model shown in Figure 3 and Figure 4 are defined through probability tables representing the conditional PMFs $p\left(\boldsymbol{\theta}_{t} \mid \boldsymbol{\theta}_{t-1}\right), p\left(\boldsymbol{\omega}_{t} \mid \boldsymbol{\omega}_{t-1}, d_{t-1}, \boldsymbol{\theta}_{t}\right), p\left(d_{t} \mid d_{t-1}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t}\right)$ and $p\left(\mathbf{z}_{t} \mid \boldsymbol{\omega}_{t}, d_{t}, \boldsymbol{\theta}_{t}\right)$. If random variables are defined in a continuous space, they must be replaced by corresponding discrete random variables, as described later.

# Exact inference in the dynamic Bayesian network model 

We can distinguish between a number of inference problems in temporal models (Russell and Norvig 2003). Those most relevant in the context of deterioration modeling are filtering, prediction and smoothing ${ }^{2}$. We can summarize these inference problems as:

- Filtering (or monitoring): The task of computing the posterior distribution over the state at time $t$ given evidence up to time $t$, i.e., $p\left(\mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$.
- Prediction: The task of computing the posterior distribution over the state at a future time $T$ given evidence up to time $t$, i.e., $p\left(\mathbf{0}_{T}, \boldsymbol{\omega}_{T}, d_{T} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$, with $t<T$.
- Smoothing: The task of computing the posterior distribution over the state at a past time $t$ given evidence up to time $T$, i.e., $p\left(\mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{T}\right)$, with $t<T$.

For DBN with discrete random variables, a number of exact inference algorithms exist for these tasks (Murphy 2002; Russell and Norvig 2003), some of which are implemented in commercial and free BN software (Murphy 2001). In the Appendix, an adopted version of the "forward-backward" algorithm is introduced. The main constituents of this algorithm are

- the forward operation (for time $t$ ), which computes $p\left(\mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$ by means of a recursive algorithm as presented in the Appendix;
- the backward operation (for time $t$ ), which computes $p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)$ by means of a recursive algorithm as presented in the Appendix.

Filtering is performed by simply applying the forward operation for time $t$. Predicting is performed by applying the forward operation for time $T$, whereby the likelihood

[^0]
[^0]:    ${ }^{2}$ Another inference task is learning of the conditional probability tables defining the nodes. However, since the DBN model is based on a parametric deterioration model, data is not used to learn the conditional probability tables, e.g., $p\left(d_{t} \mid d_{t-1}, \boldsymbol{0}, \boldsymbol{\omega}_{t}\right)$. Instead, the probability distributions of the time-invariant model parameters $\boldsymbol{0}$ are updated with the observations.

functions for $\mathbf{z}_{i+1}, \ldots, \mathbf{z}_{T}$ are set equal to one: $p\left(\mathbf{z}_{i} \mid d_{i}\right)=1, i=t+1, \ldots, T$ (i.e., no evidence is entered for these variables). Finally, smoothing is carried out by performing both the forward operation and the backward operation for time $t$. We then obtain

$$
p\left(\mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{0}, \ldots, \mathbf{z}_{T}\right) \propto p\left(\mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{0}, \ldots, \mathbf{z}_{t}\right) p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)
$$

Equation (8) is an application of Bayes' rule, whereby the forward operation result $p\left(\mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$ is the prior probability. The likelihood function is $p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)$, the result of the backward operation, because of independence of $\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T}$ from $\mathbf{z}_{1}, \ldots, \mathbf{z}_{t}$ for given $\mathbf{0}_{t}, \boldsymbol{\omega}_{t}, d_{t}$, as prescribed by the DBN structure.

Let the number of states of $d_{t}, \boldsymbol{\omega}_{t}, \boldsymbol{0}_{t}$ be $m_{d}, m_{\mathbf{a}}, m_{\mathbf{0}}$, respectively. As demonstrated in the Appendix, the computation time for filtering is $O\left[\left(m_{d}^{2} m_{\mathbf{a}}+m_{d} m_{\mathbf{a}}^{2}\right) m_{\mathbf{0}} t\right]$, whereas it is $O\left[\left(m_{d}^{2} m_{\mathbf{a}}+m_{d} m_{\mathbf{a}}^{2}\right) m_{\mathbf{0}} T\right]$ for predicting and smoothing. Therefore, the computational performance is determined by the number of states utilized for representing the variables, in particular $d_{t}$ and $\boldsymbol{\omega}_{t}$. The discretization of the random variables defined in a continuous space is thus a critical part of the framework.

# Discretization of continuous random variables 

All random variables that are defined in continuous space are replaced by equivalent variables defined in a finite space. It is suggested to perform this discretization sequentially, i.e., one variable at the time, and to proceed according to the hierarchy in the BN, i.e., parents are discretized before their children.

Consider discretization of a single random variable $X$. This variable has a set of parent variables $\mathbf{X}_{P}=p a(X)$ and a set of children variables $\mathbf{X}_{C}=c h(X)$. Its corresponding discrete variable is $\hat{X}$ and has $m_{X}$ states, which are denoted by $\hat{x}^{(k)}, k=1 \ldots m_{X}$. The $m_{X}$ states of $\hat{X}$ correspond to mutually exclusive, collectively exhaustive intervals in the space of the original variable $X$. Because of the hierarchal discretization order, all variables in $\mathbf{X}_{P}$ are discrete.

The continuous random variable $X$ is replaced in the BN with the discrete random variable $\hat{X}$. Therefore, the conditional PMF of $\hat{X}$ given $\mathbf{X}_{P}=\mathbf{x}_{P}^{(l)}$ must be defined, as well as the conditional distribution of $\mathbf{X}_{C}$ given $\hat{X}=\hat{x}^{(k)}$. The conditional PMF of $\hat{X}$ is

$$
p\left(\hat{x}^{(k)} \mid \mathbf{x}_{P}^{(l)}\right)=F_{X}\left(x_{k}^{+} \mid \mathbf{x}_{P}^{(l)}\right)-F_{X}\left(x_{k}^{-} \mid \mathbf{x}_{P}^{(l)}\right)
$$

wherein $F_{X}$ is the cumulative distribution function (CDF) of $X$, which is conditional on $\mathbf{X}_{P}=\mathbf{x}_{P}^{(l)}$, and $x_{k}^{-}$and $x_{k}^{+}$are the lower and upper boundaries of the interval corresponding to state $k$.

The distribution of $\mathbf{X}_{C}$ conditional on $\hat{X}=\hat{x}^{(k)}$ is approximated by

$$
F_{\mathbf{x}_{C}}\left(\mathbf{x}_{C} \mid \hat{x}^{(k)}, \mathbf{y}_{P}\right)=\int_{x_{k}^{+}}^{x_{k}^{+}} F_{\mathbf{x}_{C}}\left(\mathbf{x}_{C} \mid x, \mathbf{y}_{P}\right) f_{X}\left(x \mid \hat{x}^{(k)}\right) d x
$$

in which $\mathbf{y}_{P}$ are realizations of all random variables that are parents to $\mathbf{X}_{C}$ excluding $X$. The approximation in Equation (10) is twofold. First, it is assumed that the distribution of $X$ is independent of $\mathbf{Y}_{P}$ for given $\hat{X}$, which does not hold in the general case, although it does in many special instances. Second, an assumption about $f_{X}\left(x \mid \hat{x}^{(k)}\right)$ must be made, because $f_{X}(x)$ is unknown. (Remember that the variable $X$ in the BN is only defined conditional on $\mathbf{X}_{P}$.) A straightforward choice is the uniform distribution for $f_{X}\left(x \mid \hat{x}^{(k)}\right)$ :

$$
f_{X}\left(x \mid \hat{x}^{(k)}\right)=\frac{1}{x_{k}^{+}-x_{k}^{-}}, \quad x_{k}^{-}<x \leq x_{k}^{+}
$$

The uniform assumption is not suitable if the interval is only bounded on one side. In such a case, it is suggested to apply an exponential PDF, e.g., for the case of an interval with only a lower bound:

$$
f_{X}\left(x \mid \hat{x}^{(k)}\right)=\lambda \exp \left[-\lambda\left(x-x_{k}^{-}\right)\right], \quad x_{k}^{-}<x
$$

$\lambda$ can be freely selected to best represent the original distribution.
When $X$ has no parents, $f_{X}(x)$ is known and no approximation is required. Then $f_{X}\left(x \mid \hat{x}^{(k)}\right)$ is simply the original PDF of $X$, truncated in the range $x_{k}^{-}<x \leq x_{k}^{+}$.

# Choice of the discrete intervals 

The approximation in Equation (10) introduces an unknown error, which becomes zero in the limit as the size of the discretization intervals approaches zero. The choice of these intervals, therefore, is crucial for the accuracy of the results as well as the computational

performance of the algorithms. This choice is application-specific, but some general considerations are made and a heuristic for the selection is presented in the following

Obviously, the goal is to select the discretization scheme that provides sufficient accuracy at maximum computational speed. Additionally, the scheme must ensure flexibility with respect to potential evidence that may become available in applying the model. Evidence will update the marginal distributions of the random variables in the model, thus increasing the difficulty in selecting an optimal discretization scheme a-priori. It is crucial that the discretization scheme leads to accurate results for all possible combinations of evidence. There is potential for an adaptive procedure, whereby the discretization scheme is adjusted as evidence becomes available (Neil et al 2007), but this is not further considered here since it is our aim to keep the procedure as simple as possible. For the same reason, only homogenous DBN models are considered, i.e., we require that the discretization scheme is the same for all time slices.

Consider discretization of a single random variable $X$. First, we identify the probable range of values of $X$. The probable range of values is defined so that the a-priori probability of a variable being outside that range is smaller than $p$ for all time slices $t$. The value of $p$ will determine the minimum probability value that can be computed accurately with the model. For most practical applications, in particular when the probability of the failure event is of interest, $p=10^{-6}$ will be sufficient.

Next, we determine the discretization intervals in the space of $X$ within the probable range of values. These intervals are assigned without consideration of the a-priori distribution of $X$, to ensure flexibility with respect to potential evidence. The simplest choice would be intervals with equal lengths. However, it is recommended to account for the influence of $X$ on the deterioration damage $d_{t}$. To this end, intervals of equal length are assigned in the space of $T_{x}(x)$, with $T_{x}(x)$ being a suitable transformation such that the relation between $T_{x}(x)$ and $d_{t}$ is approximately linear. In most cases, it will be sufficient to select a simple functional form for $T_{x}(x)$, such as $T_{x}(x)=\ln (x)$ or $T_{x}(x)=\exp (x)$. Finally, the interval borders $\mathbf{x}_{B}$ are established as a function of the upper bound $x_{u b}$ and the lower bound $x_{l b}$ of the probable range of $X$ as
$\mathbf{x}_{B}\left(2: m_{X}\right)=T_{x}^{-1}\left[T_{x}\left(x_{l b}\right):\frac{T_{x}\left(x_{u b}\right)-T_{x}\left(x_{l b}\right)}{m_{X}-2}: T_{x}\left(x_{u b}\right)\right]$

$\mathbf{x}_{B}(1)$ and $\mathbf{x}_{B}\left(m_{X}+1\right)$ are set equal to the borders of the physically admissible domain of $X$. The number of discrete states, $m_{X}$, is adjusted to achieve the optimal balance between accuracy and speed. A higher value is chosen for variables with a higher importance (e.g., as appraised by a sensitivity measure on the reliability index a-priori). Finally, the resulting discretization scheme must be validated by comparing results for a few selected evidence cases with results obtained by alternative computation methods (typically crude simulation, which has the advantage of being unbiased and robust).

# Application I: Fatigue crack growth modeling involving time-invariant random variables only 

This example presents the application of the DBN model to a representative fracture mechanics (FM) based fatigue model that involves only time-invariant random variables. The aim of this example is to study the effect of discretization and to compare the performance of the DBN model with other numerical solutions, such as the second-order reliability method (SORM) and crude Monte Carlo simulation (MCS). For the sake of the example, a simple model is chosen from Ditlevsen and Madsen (1996). Crack growth is described by Paris' law, Equation (14).
$\frac{\mathrm{d} a(n)}{\mathrm{d} n}=C[\Delta S \sqrt{\pi a(n)}]^{m}$
$a$ is the crack length, $n$ is the number of stress cycles, $\Delta S$ is the stress range per cycle (constant stress amplitudes are assumed) and $C$ and $m$ are empirically determined model parameters. In this formulation of Paris' law, the geometry correction factor is one, which in theory corresponds to the case of a crack in a plate with infinite size. With the boundary condition $a(n=0)=a_{0}$, this differential equation can be solved for the crack size as a function of the number of cycles $n$, (Ditlevsen and Madsen 1996):
$a(n)=\left[\left(1-\frac{m}{2}\right) C \Delta S^{m} \pi^{m / 2} n+a_{0}^{(1-m / 2)}\right]^{\left(1-m / 2\right)^{-1}}$
The event of failure is described by the limit state function $g$ as a function of $a(n)$ and the critical crack length $a_{c}$ :

$$
g=a_{c}-a(n)
$$

The performance of the structural element is represented through the binary variable $E$. Failure of the element $\{E=0\}$ occurs if $g \leq 0$, and its complement $\{E=1\}$, the survival event, occurs if $g>0$. The probabilistic model is summarized in Table 1.

Table 1. Parameters of the fatigue crack growth application with time-invariant parameters.


*1) dimension corresponding to N and mm

Since this model contains only time-invariant parameters, we have, in terms of the generic model, $\boldsymbol{\theta}=[\Delta S, C, m]$ and $d_{t}=a_{t}$. In analogy to Equation (15), we obtain the deterministic function for $a_{t}$ :
$a_{t}=\left[\left(1-\frac{m}{2}\right) C \Delta S^{m} \pi^{m / 2} \Delta n+a_{t-1}^{(1-m / 2)}\right]^{[1-m / 2]^{-1}}, \quad t=1, \ldots, T$
$\Delta n$ is the number of stress cycles during one time step. If the model were implemented with each variable as a separate node, the space of $\boldsymbol{\theta}$ would consist of $m_{\theta}=m_{\Delta S} m_{C} m_{m}$ states. To reduce $m_{\theta}$, and consequently computation time, we make use of the fact that the two variables $\Delta S, C$ can be replaced by a single variable $q=(1-m / 2) C^{m / 2} \Delta S^{m} \Delta n$ in Equation (17). The dimension of the space of $\boldsymbol{\theta}$ is reduced, and it is $m_{\theta}=m_{\theta} m_{m}$. The

![img-4.jpeg](img-4.jpeg)

Figure 5.
![img-5.jpeg](img-5.jpeg)

Figure 5. Fatigue crack growth as a DBN, case with time-invariant parameters.

In the numerical implementation, we choose $\Delta n=10^{5}$. The discretization scheme for the random variables is summarized in Table 2. It is noted that this discretization scheme is likely suboptimal, because of the strong statistical dependence between $q$ and $m$. To optimize the discretization scheme, the joint space of $q$ and $m$ should be considered, but the present discretization scheme is considered sufficiently accurate and efficient. The numbers of discrete states of $S$ and $\ln C$ have little effect on the computational speed,

because for given values of $q$ and $m$ the remaining variables of the model are statistically independent of $S$ and $\ln C$. It is, therefore, sufficient to evaluate the prior distribution of $q$ and $m$, then update all variables in the model according to the proposed algorithm, and then compute the posterior PMF of $S$ and $\ln C$ based on the posterior joint PMF of $q$ and $m$. The computation time for this last step is orders of magnitude lower than for performing a forward or backward operation.

The PMF of $\Delta S$ and $m$ are obtained analytically using Equation (9); $p(C \mid m)$ is computed from the cumulative bi-Normal distribution; $p(q \mid \Delta s, m, C)$ and $p\left(a_{t} \mid a_{t-1}, m_{t}, q_{t}\right)$ are evaluated using MC simulation with $10^{4}$ samples. Finally, $p\left(m_{t} \mid m_{t-1}\right)$ and $p\left(q_{t} \mid q_{t-1}\right)$ are unit diagonal matrixes.

Table 2. Discretization scheme.


${ }^{* 1}$ ) dimension corresponding to N and mm

# Including evidence 

Inspections of the structural element are carried out in intervals of $10^{6}$ cycles and it is assumed that all inspections result in no-indication (i.e., no defect is found). In the numerical example, we consider the following PoD model (with $D$ being the event of detection):
$\operatorname{Pr}\left(Z_{t}=D \mid a\right)=\operatorname{PoD}(a)=1-\exp (-a / 10 \mathrm{~mm})$

Obviously, the probability of no-detection at time $t$ conditional on $a$ is $\operatorname{Pr}\left(Z_{t}=\bar{D} \mid a\right)=1-P o D(a)$. As described earlier, evidence is included by instantiating the inspection variables $Z_{t}$ in the DBN with the observed events (here: no-indication) at the times of inspection.

# Results 

The results obtained with the DBN are compared to results obtained with MCS and SORM, in terms of the reliability index $\beta=\Phi^{-1}[\operatorname{Pr}(E=1)]$ with $\Phi^{-1}$ being the inverse normal CDF. For the unconditional case (no observations), the results are shown in Figure 6.
![img-6.jpeg](img-6.jpeg)

Figure 6. Results for the unconditional case.

For the case including inspection results, we apply the filtering inference algorithm, i.e., the reliability index $\beta$ after $n$ cycles is computed by consideration of all inspection results up to $n$ cycles, but neglecting later inspection results. The results are shown in Figure 7.

![img-7.jpeg](img-7.jpeg)

Figure 7. Results for the conditional case (no indication of a defect at all inspections).

The results in Figure 6 and Figure 7 demonstrate the accuracy of the DBN approach. Besides facilitating efficient computation of the reliability as a function of time, the DBN model enables updating of the distribution of all random variables in the model with given inspection results. As an example, Figure 8 presents the updated complementary CDF of the stress ranges $\Delta S$ for different evidence cases.

![img-8.jpeg](img-8.jpeg)

Figure 8. Updating of the distribution of stress ranges $\Delta S$ with inspection results.

# Computational performance 

With the DBN established, the computation of the results presented here takes in the order of 10 CPU seconds on a standard PC with a 2.0 GHz processor with a Matlab-based program. The computation time increases linearly with the number of time steps considered (the 10 CPU seconds correspond to 100 time steps), but is independent of the number of observations.

## Application II: Fatigue crack growth as a stochastic process

Fatigue crack growth has frequently been modeled by a random process model (Ortiz and Kiremidjian 1988; Lin and Yang 1985; Yang and Manning 1996; Zheng and Ellingwood 1998; Beck and Melchers 2004). To demonstrate the applicability of the DBN framework for such models, the model suggested by Yang and Manning (1996) is utilized in a numerical example. Equation (19) shows the model in its generic format.

$\frac{\mathrm{d} a(n)}{\mathrm{d} n}=Y(n) g_{c g}[a(n), \mathbf{0}]$
$a(n)$ is the crack size after $n$ cycles and $g_{c g}[\cdot]$ can be any deterministic crack growth law as a function of $a(n)$ and of time-invariant parameters $\mathbf{0}$. The simplistic crack growth law considered in this example is the same as in the previous example, i.e.,

$$
g[a(n), \mathbf{0}]=C[\Delta S \sqrt{\pi a(n)}]^{m}
$$

$Y(n)$ in Equation (19) is a stationary lognormal process with a median value equal to 1 and standard deviation $\sigma_{Y}$. The autocovariance function of $Y(n)$ is of an exponential form:

$$
R_{Y Y}\left(n_{1}, n_{2}\right)=\operatorname{cov}\left[Y\left(n_{1}\right), Y\left(n_{2}\right)\right]=\sigma_{Y}^{2} \exp \left(-\left|n_{2}-n_{1}\right| / \alpha_{Y}\right)
$$

The parameter $\alpha_{Y}$ is a measure of the correlation time for $Y(n)$.
For given values of $\mathbf{0}$ and $a_{0}$, Yang and Manning (1996) present an analytical solution for the probability of the crack exceeding a given value $a_{c}$ :

$$
\operatorname{Pr}\left[a_{c}<a(n) \mid \mathbf{0}, a_{0}\right]=\Phi\left\{\frac{\ln n-\ln \left[n_{0.5}\left(a_{c} \mid \mathbf{0}, a_{0}\right) / \lambda(n)\right]}{\psi(n)}\right\}
$$

This solution is a second-order approximation, based on the assumption that $W(\tau)=\int_{0}^{\tau} Y(n) d n$ is a lognormal process. $n_{0.5}\left(a_{c} \mid \mathbf{0}, a_{0}\right)$ is the median number of cycles to reach $a_{c}$, computed as

$$
n_{0.5}\left(a_{c} \mid \mathbf{0}, a_{0}\right)=\int_{a_{0}}^{a_{c}} \frac{d a}{g[a, \mathbf{0}]}
$$

For the crack growth law in Equation (20), it is

$$
n_{0.5}\left(a_{c} \mid \mathbf{0}, a_{0}\right)=\frac{1}{C \Delta S^{m} \pi^{m / 2}}\left[\frac{a_{c}^{(1-m / 2)}-a_{0}^{(1-m / 2)}}{1-m / 2}\right]
$$

The remaining parameters in Equation (22) are obtained as follows (for details refer to (Yang and Manning 1996)).

$$
\lambda(n)=\exp \left(\sigma_{\ln Y}^{2} / 2\right)\left[1+\phi^{2}(n) \exp \left(\sigma_{\ln Y}^{2}\right)-\phi^{2}(n)\right]^{-1 / 2}
$$

$$
\begin{aligned}
& \psi(n)=\left\{\ln \left[1+\phi^{2}(n) \exp \left(\sigma_{\ln Y}^{2}\right)-\phi^{2}(n)\right]\right\}^{1 / 2} \\
& \phi^{2}(n)=\frac{2 \alpha_{Y}^{2}}{n^{2}}\left[\exp \left(-\frac{n}{\alpha_{Y}}\right)+\frac{n}{\alpha_{Y}}-1\right]
\end{aligned}
$$

where $\sigma_{\ln Y}^{2}$ is the variance of $\ln Y(n)$.
The solution in Equation (22) is applied to verify the results obtained with the DBN model. The unconditional $\operatorname{Pr}\left[a_{c}<a(n)\right]$ is computed from $\operatorname{Pr}\left[a_{c}<a(n) \mid \boldsymbol{0}, a_{0}\right]$ by means of numerical integration.

In the numerical investigations, the parameter values provided in Table 3 are applied. $\alpha_{Y}$, the correlation length of $Y(n)$, is modeled as a random variable.

Table 3. Parameters of the stochastic process crack growth model example.


*1) dimension corresponding to N and mm

# DBN modeling 

The DBN model for this example is shown in Figure 9. The binary variable $E$ represents the performance of the structural element (failure $\{E=0\}$ or survival $\{E=1\}$ ). The potential evidence that is included in the DBN model are measurements $M_{t}$ of the crack depth. $M_{t}$ is assumed to be Normal distributed with mean equal to the true crack depth

$a_{t}$ and standard deviation $\sigma_{M}=1 \mathrm{~mm}$. This DBN model assumes that the Lognormal process $Y(n)$, represented by the variables $Y_{t}$, is Markovian, which represents a firstorder approximation as discussed earlier.
![img-9.jpeg](img-9.jpeg)

Figure 9. Fatigue crack growth as a DBN, random process model.

The discretization scheme is summarized in Table 4. The PMFs $p\left(\alpha_{Y}\right), p\left(Y_{1}\right)$ and $p\left(a_{0}\right)$ are calculated analytically from Equation (9); $p\left(Y_{t} \mid Y_{t-1}, \alpha_{Y t}\right), p\left(a_{t} \mid a_{t-1}, Y_{t}\right)$ and $p\left(M_{t} \mid a_{1}\right)$ are calculated using the approximations in Equations (11) and (12), assuming that $Y_{t}$ is constant during one time slice. The correlation coefficient between $Y_{t}$ and $Y_{t-1}$ is given by Equation (21). The number of cycles between the slices is $\Delta n=10^{5}$. For 100 time slices, this discretization scheme leads to CPU times in the order of 1-10 seconds on a standard PC with a 2.0 GHz processor for the presented results.

Table 4. Discretization scheme for the random process example.


# Numerical results 

Figure 10 presents a comparison of the DBN results with the solution based on secondorder approximation, in terms of the reliability index for the case of no measurements. It is observed that the first-order Markovian approximation for $Y_{t}$ has little influence on the reliability index. The deviation of the DBN result from the second-order results for small numbers of cycles is mainly due to the approximation in the discretization of $Y_{t}$, as found from additional numerical investigations, which are not reported here for brevity. When doubling the number of discrete states for $Y_{t}$, the difference between the two solutions becomes negligible.
![img-10.jpeg](img-10.jpeg)

Figure 10. Result for the random process crack growth example - unconditional case.

To demonstrate the model updating with measurements of the deterioration size, the model is updated with the measurement results summarized in Table 5. Figure 11 presents the resulting posterior mean of the crack depth for filtering (including evidence up to $t$ ) and for smoothing (including all evidence).

Table 5. Measurement results.


![img-11.jpeg](img-11.jpeg)

Figure 11. Posterior mean of the crack depth $a(n)$.

For the same measurements, Figure 12 presents the posterior mean of the stress range process $\Delta S \cdot Y(n)^{1 / m}$ for two values of the correlation length $\alpha_{\mathrm{T}}$. For higher values of $\alpha_{\mathrm{T}}$, larger differences are observed between the posterior and the prior mean of $\Delta S \cdot Y(n)^{1 / m}$. (The latter is $63.7 \mathrm{~N} / \mathrm{mm}^{2}$ in both cases.) This effect is expected, because higher correlation implies that a measurement at time $t$ provides more information about the process at other times (Straub and Faber 2007).

![img-12.jpeg](img-12.jpeg)

Figure 12. Posterior mean of the stress range process $\Delta S \cdot Y(n)^{1 / m}$ for two different values of the correlation length.

The updating of the probability distribution of model parameters based on inspection results is straightforward with the DBN. Exemplarily, the measurement results in Table 5 are utilized to update the distribution of the correlation length $\alpha_{Y}$. This results in a posterior distribution of $\alpha_{Y}$ that has mean value $1.1 \cdot 10^{6}$ and standard deviation $0.95 \cdot 10^{6}$. These values are close to the prior values, which indicates that the measurement results contain little information on $\alpha_{Y}$. This is in agreement with other results, which are not reported here, showing that the value of $\alpha_{Y}$ has little effect on the reliability and the probability distribution of the crack depth, despite its significant impact on the posterior probability distribution of the stress range process. However, it is conceivable that learning about the correlation length is possible by collecting measurement data from a larger number of specimens, in particular in combination with other information, e.g., on the initial crack depth.

# Concluding remarks 

The aim of the DBN framework is to provide a computationally robust and efficient approach to probabilistically assess the condition and the reliability of structural elements subject to deterioration when observations are available. Figure 6, Figure 7 and Figure 10

demonstrate the accuracy of the framework for computing the reliability of deteriorating structural elements. Figure 8 illustrates the capability of the DBN approach for Bayesian updating of the uncertain model parameters. Finally, Figure 11 and Figure 12 demonstrate the capabilities of the DBN framework in monitoring the performance of structures subject to deterioration in a near-real time manner. Based on these results, it is concluded that the proposed framework has a huge potential for applications in monitoring, inspection, maintenance and repair planning.

The DBN framework is limited with respect to the number of random variables that can be included, due to the exponential increase in computation time with the number of random variables in the general case. However, as illustrated by the introduction of the auxiliary random variable $q$ in the first application, it is often possible to reduce the number of time-invariant random variables by reformulating the problem. Furthermore, at present most practically relevant deterioration models contain only a small number of random variables.

Future work should aim at extending the presented framework to consider multiple structural elements. This is relevant for the asset integrity management of structural systems, but also for parameter estimation from experiments. Such an extension could be based on formulating the PMF of the time-invariant parameters $\boldsymbol{\theta}$ and the initial damage condition $d_{0}$ conditional on so-called hyper-parameters $\mathbf{A}$ that are common to all structural elements (i.e., the hyper-parameters are introduced as common parents to the variables $\boldsymbol{\theta}$ and $d_{0}$ of all elements). The DBNs representing the individual elements are then connected through the $\mathbf{A}$ node, which allows passing information between the elements, such that the information collected for one element is used to update the probabilistic model of all elements. Depending on the type of dependence among the system elements, different models can be envisaged and should be investigated. The flexibility of the BN methodology will facilitate such developments.

# Acknowledgment 

This work was supported by the Swiss National Science Foundation (SNF) through grant PA002-111428.

# Appendix - Inference algorithm 

This Appendix presents algorithms for the forward and the backward operation, which form the basis for all inference, as summarized earlier. The algorithms are based on algorithms originally developed for Hidden Markov Models (HMM) (Russell and Norvig 2003) and are here adopted to the proposed deterioration modeling framework. They approximately correspond to the frontier algorithm presented by Murphy (2002).

## Forward computation

We compute $p\left(\boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$ through a recursive algorithm. By considering the independence assumptions encoded in the BN structure, as shown in Figure 3 and Figure 4 , we obtain the following relationships:

$$
\begin{aligned}
& p\left(d_{t}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t} \mid \mathbf{z}_{0}, \ldots, \mathbf{z}_{t}\right) \propto p\left(d_{t}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t} \mid \mathbf{z}_{0}, \ldots, \mathbf{z}_{t-1}\right) p\left(\mathbf{z}_{t} \mid d_{t}\right) \\
& p\left(d_{t}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t} \mid \mathbf{z}_{0}, \ldots, \mathbf{z}_{t-1}\right) \\
& =\sum_{d_{t-1}} \sum_{\boldsymbol{\omega}_{t-1}} \sum_{\theta_{t-1}} p\left(d_{t}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t} \mid d_{t-1}, \boldsymbol{\omega}_{t-1}, \boldsymbol{\theta}_{t-1}\right) p\left(d_{t-1}, \boldsymbol{\omega}_{t-1}, \boldsymbol{\theta}_{t-1} \mid \mathbf{z}_{0}, \ldots, \mathbf{z}_{t-1}\right) \\
& =\sum_{d_{t-1}} \sum_{\boldsymbol{\omega}_{t-1}} \sum_{\theta_{t-1}} p\left(d_{t} \mid d_{t-1}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t}\right) p\left(\boldsymbol{\omega}_{t} \mid d_{t-1}, \boldsymbol{\omega}_{t-1}, \boldsymbol{\theta}_{t}\right) p\left(\boldsymbol{\theta}_{t} \mid \boldsymbol{\theta}_{t-1}\right) p\left(d_{t-1}, \boldsymbol{\omega}_{t-1}, \boldsymbol{\theta}_{t-1} \mid \mathbf{z}_{0}, \ldots, \mathbf{z}_{t-1}\right) \\
& =\sum_{d_{t-1}} p\left(d_{t} \mid d_{t-1}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t}\right) \sum_{\boldsymbol{\theta}_{t-1}} p\left(\boldsymbol{\omega}_{t} \mid d_{t-1}, \boldsymbol{\omega}_{t-1}, \boldsymbol{\theta}_{t}\right) \sum_{\boldsymbol{\theta}_{t-1}} p\left(\boldsymbol{\theta}_{t} \mid \boldsymbol{\theta}_{t-1}\right) p\left(d_{t-1}, \boldsymbol{\omega}_{t-1}, \boldsymbol{\theta}_{t-1} \mid \mathbf{z}_{0}, \ldots, \mathbf{z}_{t-1}\right)
\end{aligned}
$$

Equations (28) and (29) establish the relationship between $p\left(d_{t-1}, \boldsymbol{\omega}_{t-1}, \boldsymbol{\theta}_{t-1} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t-1}\right)$ and $p\left(\boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$. Starting from $p\left(d_{1}, \boldsymbol{\omega}_{1}, \boldsymbol{\theta}_{1} \mid \mathbf{z}_{0}, \mathbf{z}_{1}\right)$, it is thus possible to compute all $p\left(\boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$ for any $t$ recursively.

In principle it is not necessary to determine the proportionality constant in Equation (28), but to prevent underflow it is recommended to normalize $p\left(\boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$ at each time step of the recursive algorithm.

If there is no evidence at a time $t$, the corresponding likelihood function can be set equal to one, i.e., $p\left(\mathbf{z}_{t} \mid d_{t}\right)=1$. This is equivalent to omitting Equation (28) in the forward operation.

# Backward computation 

The backward-part of the algorithm computes the likelihood $p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)$. By considering the independence assumptions encoded in the BN structure, we obtain the following relationships:

$$
\begin{aligned}
& p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right) \\
& =\sum_{d_{t+1}} \sum_{\boldsymbol{\omega}_{t+1}} \sum_{\theta_{t+1}} p\left(\mathbf{z}_{t+2}, \ldots, \mathbf{z}_{T}, \boldsymbol{\theta}_{t+1}, \boldsymbol{\omega}_{t+1}, d_{t+1}, \mathbf{z}_{t+1} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right) \\
& =\sum_{d_{t+1}} \sum_{\boldsymbol{\omega}_{t+1}} \sum_{\theta_{t+1}} p\left(\mathbf{z}_{t+2}, \ldots, \mathbf{z}_{T} \mid \mathbf{z}_{t+1}, \boldsymbol{\theta}_{t+1}, \boldsymbol{\omega}_{t+1}, d_{t+1}, \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right) p\left(\boldsymbol{\theta}_{t+1}, \boldsymbol{\omega}_{t+1}, d_{t+1}, \mathbf{z}_{t+1} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right) \\
& =\sum_{d_{t+1}} \sum_{\boldsymbol{\omega}_{t+1}} \sum_{\theta_{t+1}} p\left(\mathbf{z}_{t+2}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t+1}, \boldsymbol{\omega}_{t+1}, d_{t+1}\right) p\left(\boldsymbol{\theta}_{t+1}, \boldsymbol{\omega}_{t+1}, d_{t+1} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right) p\left(\mathbf{z}_{t+1} \mid d_{t+1}\right) \\
& =\sum_{d_{t+1}} \sum_{\boldsymbol{\omega}_{t+1}} \sum_{\theta_{t+1}} p\left(\mathbf{z}_{t+2}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t+1}, \boldsymbol{\omega}_{t+1}, d_{t+1}\right) p\left(d_{t+1} \mid d_{t}, \boldsymbol{\omega}_{t+1}, \boldsymbol{\theta}_{t+1}\right) p\left(\boldsymbol{\omega}_{t+1} \mid d_{t}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t+1}\right) p\left(\boldsymbol{\theta}_{t+1} \mid \boldsymbol{\theta}_{t}\right) p\left(\mathbf{z}_{t+1} \mid d_{t+1}\right) \\
& =\sum_{d_{t+1}} p\left(\mathbf{z}_{t+1} \mid d_{t+1}\right) p\left(d_{t+1} \mid d_{t}, \boldsymbol{\omega}_{t+1}, \boldsymbol{\theta}_{t+1}\right) \sum_{\boldsymbol{\theta}_{t+1}} p\left(\boldsymbol{\omega}_{t+1} \mid d_{t}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t+1}\right) \sum_{\boldsymbol{\theta}_{t+1}} p\left(\boldsymbol{\theta}_{t+1} \mid \boldsymbol{\theta}_{t}\right) p\left(\mathbf{z}_{t+2}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t+1}, \boldsymbol{\omega}_{t+1}, d_{t+1}\right)
\end{aligned}
$$

$p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)$ is computed recursively, starting from $p\left(\mathbf{z}_{T+1} \mid \boldsymbol{\theta}_{T}, \boldsymbol{\omega}_{T}, d_{T}\right)=1$. Typically, values of $p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)$ can become very small. To prevent underflow, it is recommended to normalize $p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)$ at every step, i.e., we multiply $p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)$ with a normalization factor $\alpha_{t}$ in Equation (30) above. $\alpha_{t}$ can be chosen freely, the results computed in this paper were obtained with
$\alpha_{t}=\left[\sum_{\theta_{t}} \sum_{\omega_{t}} \sum_{d_{t}} p\left(\mathbf{z}_{t+1}, \ldots, \mathbf{z}_{T} \mid \boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t}\right)\right]^{-1}$

## Computational performance of the algorithms

Let the number of states of $d_{t}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t}$ be $m_{d}, m_{\omega}, m_{\theta}$, respectively. The computation time for calculating $p\left(\boldsymbol{\theta}_{t}, \boldsymbol{\omega}_{t}, d_{t} \mid \mathbf{z}_{1}, \ldots, \mathbf{z}_{t}\right)$ is then $O\left[\left(m_{d}^{2} m_{\omega}+m_{d} m_{\omega}^{2}\right) m_{\theta} t\right]$. To verify this result, consider the last line of Equation (29) and note that the computation is performed from right to left. $O\left[m_{d} m_{\omega}^{2} m_{\theta} t\right]$ time is spent in multiplying the elements of $p\left(\boldsymbol{\omega}_{t} \mid d_{t-1}, \boldsymbol{\omega}_{t-1}, \boldsymbol{\theta}_{t}\right)$ with the terms on its right, and $O\left[m_{d}^{2} m_{\omega} m_{\theta} t\right]$ time is spent in multiplying the elements of $p\left(d_{t} \mid d_{t-1}, \boldsymbol{\omega}_{t}, \boldsymbol{\theta}_{t}\right)$ with the terms on its right. The summation over $\boldsymbol{\theta}_{t-1}$ does not have to be performed; since $p\left(\boldsymbol{\theta}_{t} \mid \boldsymbol{\theta}_{t-1}\right)$ takes value one if $\boldsymbol{\theta}_{t}=\boldsymbol{\theta}_{t-1}$ and zero otherwise, it is sufficient to exchange $\boldsymbol{\theta}_{t-1}$ with $\boldsymbol{\theta}_{t}$. It is noted that a simple Markov chain model would require a computation time of $O\left(m_{d}^{2} m_{\omega}^{2} m_{\theta}^{2} t\right)$, which is orders of magnitude higher. Based

on similar consideration, the computation time required for the backward operation is determined as $O\left[\left(m_{d}^{3} m_{\omega}+m_{d} m_{\omega}^{3}\right) m_{\theta}(T-t)\right]$. It follows that the computation time for filtering is $O\left[\left(m_{d}^{3} m_{\omega}+m_{d} m_{\omega}^{3}\right) m_{\theta} t\right]$, whereas it is $O\left[\left(m_{d}^{3} m_{\omega}+m_{d} m_{\omega}^{3}\right) m_{\theta} T\right]$ for predicting and smoothing.
