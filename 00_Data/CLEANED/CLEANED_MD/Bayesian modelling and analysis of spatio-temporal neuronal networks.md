# Bayesian Modelling and Analysis of Spatio-Temporal Neuronal Networks 

Fabio Rigat*, Mathisca de Gunst ${ }^{\dagger}$, and Jaap van Pelt ${ }^{\ddagger}$


#### Abstract

This paper illustrates a novel hierarchical dynamic Bayesian network modelling the spiking patterns of neuronal ensembles over time. We introduce, at separate model stages, the parameters characterizing the discrete-time spiking process, the unknown structure of the functional connections among the analysed neurons and its dependence on their spatial arrangement. Estimates for all model parameters and predictions for future spiking states are computed under the Bayesian paradigm via the standard Gibbs sampler using a shrinkage prior. The adequacy of the model is investigated by plotting the residuals and by applying the time-rescaling theorem. We analyse a simulated dataset and a set of experimental multiple spike trains obtained from a culture of neurons in vitro. For the latter data, we find that one neuron plays a pivotal role for the initiation of each cycle of network activity and that the estimated network structure significantly depends on the spatial arrangement of the neurons.


Keywords: hierarchical models, shrinkage priors, Bayesian model selection, multiple spike trains analysis, multi-electrode arrays.

## 1 Introduction

Stochastic modelling of multiple spike trains provides a formal framework to evaluate the scientific hypotheses explaining the observed neuronal firing patterns. This paper presents a novel hierarchical dynamic Bayesian network (DBN) model for the analysis of such patterns. The rationale to adopt such a modelling framework is that the functional relationships within any group of neurons can be uniquely represented as a directed cyclic graph (DCG), where the directed edges identify pair-wise connections and the cycles represent each neuron's self dependence over time. Furthermore, it is well known that DCGs are in one-to-one correspondence with the class of DBN models. Seminal papers in the area of Bayesian networks and of DBNs are Spirtes (1995), Heckerman (1996), Ghahramani (1998), Friedman et al. (1998), Murphy and Mian (1999), Murphy (2001) and Friedman (2004). Here we adopt a Bayesian hierarchical perspective to jointly estimate from the spike data all the model parameters, namely each neuron's baseline firing probability, the functional connectivities and their prior standard deviation, the unknown network structure and the covariate effects. By letting the network relationships be unknown parameters, we face a problem of model uncertainty (Gelfand and Dey (1994), Draper (2002), Spiegelhalter et al. (2002), Clyde and George (2004)). Dellaportas et al. (2000), George and McCulloch (1997) and Godsill (2001)

[^0]
[^0]:    *EURANDOM, The Netherlands, mailto:rigat@eurandom.tue.nl
    ${ }^{\dagger}$ Free University, The Netherlands, degunst@cs.vu.nl
    ${ }^{\ddagger}$ Netherlands Institute for Neurosciences, j.van.pelt@nih.knaw.nl

provide extensive reviews of several simulation-based Bayesian model selection methods using the Gibbs sampler and the reversible jump Markov chain Monte Carlo algorithm (Green (1995)). In order to infer the unknown network structure, we employ a shrinkage prior along the lines of George and McCulloch (1993). In this framework, joint inference for the network parameters can be carried out using the standard Gibbs sampler within a parameter space of fixed dimension. We also show that the shrinkage prior yields robust inferences for the network structure with respect to the occurrence of moderate random spike detection errors. Finally, in order to take into account some of the main features of the neuronal spiking process, the network model described in this work incorporates a Markovian dependence of varying order over time and a spatial regression term, both of which are not standard features of DBNs.

The remainder of this paper is organized as follows. Section 2 reviews the statistical literature relevant for this work. Section 3 presents our model for the joint distribution of the network spiking activity and its hierarchical prior. Section 4 illustrates the derivation of the posterior estimates of the model parameters and the predictive probabilities of future spiking states. Section 5 describes the assessment of the model's goodness of fit and of its predictive power. Sections 6 and 7 report the analyses of simulated spike trains and of a set of in vitro spike data. Section 8 discusses the strengths and weaknesses of our modelling approach and it describes some directions for future developments. The Appendix gives the expressions for the full conditional posterior distributions used within the Gibbs sampler.

# 2 A review of the statistical modeling of spike trains 

Neurons are complex input-output systems whose dynamics have been investigated by experimental neurophysiologists during the last sixty years. Nowadays, high-throughput technologies generate measurements of the activity of the nervous system from the level of single neurons (Van Pelt et al. (2004), Morin et al. (2005)) up to the whole brain (Woolrich et al. (2004)). For a comprehensive review of the literature in this area, we refer to Dayan and Abbott (2001), Gerstner and Kistler (2002), Feng (2003) and to the fundamental papers by Hodgkin and Huxley (1952), FitzHugh (1961), Nagumo et al. (1962) and Izhikevitch (2001). Fienberg (1974) described the essential physiology of the neuronal spike process and the early literature on the statistical analysis of single neuron spike trains. Brillinger and coauthors (Brillinger et al. (1976), Brillinger and Segundo (1979), Brillinger (1988b), Brillinger (1988a), Brillinger (1992)) and Doss (1989) developed several point process models characterizing the spiking activity of single neurons and the interactions among small numbers of neurons over time. West and Turner (1992), Turner and West (1993) and West (1997) employed a Dirichlet process mixture of Gaussian densities (Ferguson (1983), Escobar and West (1995)) to model the distribution of the response to excitatory post synaptic potentials of individual neurons. Kass and Ventura (2001) introduced the inhomogeneous Markov interval point process, which memory structure is determined by the inter-arrival times of successive spikes. Kass et al. (2003) proposed the BARS method (Di Matteo et al. (2001)) as a modelbased smoother of the instantaneous firing rate function. As emphasized by Iyengar

(2001), the focus of this literature is the behaviour of either single neurons or of small sets of neurons. Brown et al. (2004) and Kass et al. (2005) offer two perspectives on the state-of-the-art in the area of multiple spike trains analysis, which is concerned with the development of statistical models for the joint firing activity of many neurons over time. These papers indicate two key challenges, namely estimating the mutual dependence of the firing activity of several neurons over time and modelling the noise induced by spike detection problems. In order to address the former issue, Brillinger and Villa (1997) proposed a discrete time random threshold model where the interactions among neurons are captured via their membrane potential and threshold functions. Recently, Okatan et al. (2005) introduced a maximum likelihood method to estimate the functional connectivity of stochastic neuronal networks based on a discretisation of the approach of Chornoboy et al. (1988). Truccolo et al. (2005) proposed a point process framework to relate the spiking probability of neuronal ensembles to the neurons' own spiking history, to the concurrent ensemble activity and to extrinsic covariates, such as external stimuli and behaviour. Martignon et al. (2000) modelled the high order interactions among the measured spike trains using log-linear models. Finally, Rao (2005) proposed a Bayesian hierarchical model for integrate-and-fire networks in continuous time based on measurements of the cells' membrane potentials.

The Bayesian model proposed in this work differs from the current literature in three essential aspects. First, we separate the notions of connectivity between neurons and strength of their functional interaction. Second, we explain the structure of network connections through a regression term at the top of the model hierarchy. Third, we assess the model adequacy from two perspectives, namely by evaluating the goodness of the model fit for a training sample and its predictive power for a distinct validation sample.

# 3 A binary stochastic neuronal network 

At any point in time a neuron is spiking if its membrane potential exhibits a characteristic large fluctuation called an action potential. Because action potentials arise within very short time intervals, the spiking state can be thought of as having only two values, spiking and not-spiking. We assume that experimental measurements of such spiking states for a fixed set of $K$ neurons are available for a time grid $t \in\{1, \ldots, T\}$. In what follows, the intervals between the time points are small enough so that spikes occurring within the interval $(t-1, t]$ are observed at time $t$.

Let $Y$, with dimensions $K \times T$, columns $Y_{t}$ and elements $Y_{i t}$, be the binary matrix of random spiking states, so that $Y_{i t}=1$ if neuron $i$ is firing at time $t$ and $Y_{i t}=0$ otherwise. Let $P$ denote the joint distribution of the data $Y$, given a parameter vector $\theta$ of length $K$ and a parameter matrix $\beta$ with dimensions $K \times K$. Conditionally on

$(\theta, \beta), P$ can always be factored as

$$
\begin{aligned}
P(Y \mid \theta, \beta) & =P\left(Y_{1}, \ldots, Y_{T} \mid \theta, \beta\right) \\
& =\prod_{t=1}^{T} P_{t}\left(Y_{t} \mid \theta, \beta,\left\{Y_{w}\right\}_{w=1}^{t-1}\right)
\end{aligned}
$$

where $P_{t}$ is the conditional distribution of the $K$-dimensional column vector $Y_{t}$ and $\left\{Y_{w}\right\}_{w=1}^{0}$ is defined to be the empty set. In this framework, each $\theta_{i}$ represents a neuronspecific baseline coefficient whereas each element $\beta_{i j}$ represents the strength of the pairwise functional connection having $j$ as the transmitting neuron and $i$ as the receiving neuron. Furthermore, let the distribution of the firing state $Y_{i t}$ depend only on $(\theta, \beta)$ and on the past network history between neuron $i$ 's last firing time, $\tau_{i t}$, and time $(t-1)$. Formally $\tau_{i t}$ is defined as

$$
\tau_{i t}= \begin{cases}1 \text { if } \sum_{\tau=1}^{t} Y_{i \tau}=0 \text { or } t=1 \\ \max \left\{1 \leq \tau<t: Y_{i \tau}=1\right\} \text { otherwise }\end{cases}
$$

Under the latter assumption, the joint distribution $P$ can be further factored as

$$
P(Y \mid \theta, \beta)=\prod_{t=1}^{T} \prod_{i=1}^{K} P_{i t}\left(Y_{i t} \mid \theta_{i}, \beta_{i 1}, \ldots, \beta_{i K},\left\{Y_{w}\right\}_{w=\tau_{i t}}^{t-1}\right)
$$

with $P_{i t}$ being the conditional distribution of $Y_{i t}$. In equation (2), the spiking process for each neuron is modelled as a discrete time renewal process which renewals take place after each firing (Dayan and Abbott (2001), Brillinger (1988b), Kass and Ventura (2001)). This assumption reflects an essential feature of the underlying biological process, namely that at each point in time the firing probability of a neuron can be thought of as a function of the network activity taking place between its successive firings. Moreover, equation (2) states that at each time $t$, conditionally on their parameters $\left(\theta_{i}, \beta_{i 1}, \ldots \beta_{i K}\right)$ and on the relevant history of the network, the spiking states $Y_{1 t}, \ldots, Y_{K t}$ are independent random variables. Finally, we note that the factorization (2) would not hold if the random spiking states would be allowed to simultaneously depend on each other. In such a case, to define consistently the joint distribution $P$ we would face the issues illustrated, for instance, in Lauritzen and Spiegelhalter (1988) and in Lauritzen (1996).

In order to give an explicit form to the likelihood function (2), at any time $t$ we let $\left\{Y_{i t}\right\}_{i=1}^{K}$ be conditionally independent Bernoulli random variables given their success probabilities $\pi_{i t}\left(\theta_{i}, \beta_{i 1}, \ldots, \beta_{i K},\left\{Y_{w}\right\}_{w=\tau_{i t}}^{t-1}\right)$. We also assume a linear integration of the input signal and we adopt a logistic link, defining the firing probabilities $\pi_{i t}$ as

$$
\pi_{i t}\left(\theta_{i}, \beta_{i 1}, \ldots, \beta_{i K},\left\{Y_{w}\right\}_{w=\tau_{i t}}^{t-1}\right)= \begin{cases}\left(1+e^{-\theta_{i}}\right)^{-1} \text { if } t=1 \\ \left(1+e^{-\theta_{i}-\sum_{j=1}^{K} \beta_{i j} \frac{\sum_{k=1}^{t-1} Y_{j w}}{t-\tau_{i t}}}\right)^{-1} \text { otherwise }\end{cases}
$$

For notational convenience, in what follows we will drop the dependence of $\pi_{i t}$ on the array of parameters and the network history. Under equation (3), the likelihood (2) can be rewritten as

$$
P(Y \mid \theta, \beta)=\prod_{i=1}^{K} \frac{e^{Y_{i t} \theta_{i}}}{1+e^{\theta_{i}}} \prod_{t=2}^{T} \prod_{i=1}^{K} \frac{e^{Y_{i t}\left(\theta_{i}+\sum_{j} \beta_{i j} \frac{\sum t-1_{r_{i t}} V_{i t}^{t}}{t-\tau_{i t}}\right)}}{1+e^{\theta_{i}+\sum_{j} \beta_{i j} \frac{\sum t-1_{r_{i t}} V_{i t}^{t}}{t-\tau_{i t}}}}
$$

We note that Brillinger (1988a) and Brillinger and Villa (1997) proposed a specification of the conditional spike probabilities similar to equation (3) for their random threshold spike train models. However, in our formulation we do not assume that a spike occurs at time $t$ when the membrane potential of a neuron exceeds an unknown threshold but we let its firing probability, $\pi_{i t}$, depend on its own as well as on other neurons' spiking history. Truccolo et al. (2005) illustrate the relationship between discrete time Bernoulli generalised linear models such as (4) and continuous time Poisson generalised linear point process models.

In equation (4), each parameter $\beta_{i i}$ measures the slope of the linear relationship between the time lag $\left(t-\tau_{i t}\right)$ and the firing $\log$ odds $\log \left(\frac{\pi_{i t}}{1-\pi_{i t}}\right)$. When $\beta_{i i}<0$ this coefficient represents the overall refractoriness of neuron $i$, i.e. the propensity of its firing probability to decrease after a spike as a consequence of the underlying ion channel dynamics. If $\beta_{i i}>0$, neuron $i$ is self-excitatory and it can display a bursting behaviour. Each off-diagonal term $\beta_{i j}$ represents the constant contribution of neuron $j$ 's firing proportion $\frac{\sum t-1_{r_{i t}} Y_{j w}}{t-\tau_{i t}}$ to the spiking probability $\pi_{i t}$. Positive values of $\beta_{i j}$ correspond to excitatory functional relationships whereas negative values characterise inhibitory functional relationships. These parameters in fact do not correspond to individual synapses between pairs of interconnected neurons but they represent the average effect of the activity of neuron $j$ on the firing rate of neuron $i$ under the linear input integration process modelled in equation (3). Finally, in absence of network inputs and when neuron's $i$ own refractoriness becomes negligible, (3) implies that neuron $i$ 's firing probability is $\left(1+e^{-\theta_{i}}\right)^{-1}$, constant over time.

Let $X$ with elements $x_{i j}$ be a $K \times K$ matrix of predictors fixed over time, representing the available neuron-specific characteristics which may influence the functional development of the network. Potential covariates of interest are the cell type (e.g. pyramidal, interneuron, sensory, motor), the spatial coordinates of their somas, the location of a neuron within a particular brain section, past exposure of the neurons to chemical treatments and genetic covariates such as indicator variables for knock-out genes and so forth. In the following analyses, the elements $x_{i j}$ represent the Euclidean distance between the somas of neurons $(i, j)$. The effect of this predictor on the network connectivity is introduced in the next Section via a regression term at the top of the model hierarchy.

# 738Bayesian Modelling and Analysis of Spatio-Temporal Neuronal Networks 

### 3.1 Prior distributions

The neuron-specific coefficients $\theta$ are assigned a $K$ dimensional Gaussian prior density with zero mean and with covariance matrix $s_{\theta}^{2} I_{K}$, where $s_{\theta}^{2}$ is their common prior variance and $I_{K}$ is the $K \times K$ identity matrix.

To introduce the prior uncertainty about the network structure, for any couple $(i, j)$ we let the connectivities $\beta_{i j}$ be a priori Gaussian with zero mean, zero prior correlation with the other connectivity parameters and standard deviations

$$
\sigma_{i j}=\sigma\left(v_{i j}+\epsilon\left(1-v_{i j}\right)\right)
$$

In equation (5), the coefficient $\sigma$ represents the unknown common baseline prior standard deviation for the network connectivities, the scalar $\epsilon \in(0,1)$ is a fixed shrinkage factor common to all neurons and $v_{i j}=1$ indicates the existence of a statistically significant functional relationship with direction $j \rightarrow i$. Box and Tiao (1968) used a mixture with form (5) to extend the Bayesian linear regression model in presence of outliers. Furthermore, the prior mixture (5) has been proposed in the context of covariate selection for the linear regression model by George and McCulloch (1993) and by George and Foster (1997), who labeled their method stochastic search variable selection (SSVS). In our work the prior standard deviation $\sigma$ is estimated jointly with the other parameters given a fixed value of $\epsilon$ to fit the shrinkage mechanism to the spike data. Estimation of $\sigma$ is carried out by placing a conjugate inverse gamma prior $I G(a, b)$ on $\sigma^{2}$. We note that when both $a$ and $b$ tend to zero, this inverse gamma prior approaches $1 / \sigma^{2}$, which is the Jeffreys' prior for the variance of the Gaussian distribution.

In order to let the structure of functional connections depend on the spatial arrangement of the neurons, we let $v$ be the $K \times K$ binary matrix which $(i, j)$ th element, $v_{i j}$, is one with probability $\left(1+e^{-\alpha_{0}-\alpha x_{i j}}\right)^{-1}$ and zero otherwise. In this formulation, $\alpha$ represents the spatial dependence of the network connectivity. In particular, $\alpha<0$ implies that the further apart are the somas of neurons $(i, j)$, the lower is the prior expectation of a direct functional connection being established between them and vice versa. Moreover, $\alpha_{0}$ represents an unknown intercept capturing the baseline propensity of the network to form pair-wise functional connections independently of the spatial covariates. Conditionally on $\alpha_{0}, \alpha$ and $X$, the parameters $v_{i j}$ are assumed to be a priori independent Bernoulli random variables, so that the prior distribution for the network structure is

$$
P\left(v \mid \alpha_{0}, \alpha, X\right)=\prod_{i j} e^{\left(\alpha_{0}+\alpha x_{i j}\right) v_{i j}}\left(1+e^{\alpha_{0}+\alpha x_{i j}}\right)^{-1}
$$

By equation (6), with prior probability $\left(1+e^{\alpha_{0}+\alpha x_{i j}}\right)^{-1}$ we have that $v_{i j}=0$. Having fixed $\epsilon$ close to zero, from equation (5) it can be seen that in this case the spiking activity of neuron $j$ does not significantly affect the firing probability of neuron $i$ and at any point in time. Indeed, if $v_{i j}=0$ the $99 \%$ probability interval for the conditional prior of the parameter $\beta_{i j}$ is approximately $(-3 \sigma \epsilon, 3 \sigma \epsilon)$. In the case $v_{i j}=1$, this shrinkage prior allocates $99 \%$ probability on the interval $(-3 \sigma, 3 \sigma)$. Thus, in this framework the

value of $\epsilon$ defines the size of a negligible network effect relative to the prior standard deviation $\sigma$.

Finally, the spatial dependence parameter $\alpha$ and the intercept $\alpha_{0}$ are assigned independent Gaussian priors with mean zero and with common standard deviation $s_{\alpha}$. Under this prior structure, the full model can be written as

$$
\begin{aligned}
\alpha_{0}, \alpha \stackrel{\text { ind. }}{\sim} & N\left(0, s_{\alpha}^{2}\right) \\
v_{i j} \mid \alpha_{0}, \alpha, x_{i j} & \stackrel{\text { ind. }}{\sim} & \text { Bernoulli }\left(\left(1+e^{-\alpha_{0}-\alpha x_{i j}}\right)^{-1}\right) \\
\sigma^{2} & \sim I G(a, b) \\
\sigma_{i j} & =\sigma\left(v_{i j}+\epsilon\left(1-v_{i j}\right)\right) \\
\beta_{i j} \mid v_{i j}, \sigma, \epsilon & \stackrel{\text { ind. }}{\sim} N\left(0, \sigma_{i j}^{2}\right) \\
\theta & \sim N\left(0, s_{\theta}^{2} I_{K}\right) \\
Y \mid \theta, \beta & \sim \quad \text { equation (4). }
\end{aligned}
$$

# 4 Parameter estimation and prediction of future spiking states 

In what follows, the data $Y$ is divided in a training sample including all the spike states recorded during the period $t \in\left\{1, \ldots, t^{*}<T\right\}$ and a validation sample including the remaining spikes. The former is used to estimate the model parameters which, in turn, are used to assess the model's predictive power for the validation sample.

Under model (7), the posterior estimates of all parameters $\left(\alpha_{0}, \alpha, v, \sigma, \theta, \beta\right)$ can be computed by simulation via the Gibbs sampler
(Gelfand and Smith (1990), Smith and Roberts (1993), Tierney (1994)). The latter proceeds by iteratively sampling realisations of the parameters from their respective full conditional posterior densities (FCPDs) which can be obtained, up to a multiplicative constant, by dropping from the joint posterior the terms which do not depend on the parameter of interest. The FCPDs of all model parameters are reported in the Appendix. The FCPDs for $\sigma$ and $\nu$ are conjugate to their priors, so that these parameters can be updated in closed form. For the update of $\left(\alpha_{0}, \alpha\right)$ we employ a vector-wise random walk Metropolis step, whereas for the update of $(\theta, \beta)$ we use a neuron-wise random walk random scan Metropolis sampler. The proposal distributions used for these Metropolis steps are Gaussian.

In this work we adopt the sample means and the sample $95 \%$ equal tails frequency intervals computed from the Gibbs sampler output as estimates of the marginal posterior means and of the marginal posterior probability intervals of the model parameters. Averaging over the Gibbs sampler draws for $(\theta, \beta)$ we obtain estimates of the marginal posterior means for the likelihood parameters, $(\widehat{\theta}, \widehat{\beta})$. The latter are plugged in equation (3) to compute the fitted spiking probabilities $\widehat{\pi}_{i t}=\pi_{i t}\left(\widehat{\theta}_{i}, \widehat{\beta}_{i 1}, \ldots, \widehat{\beta}_{i K},\left\{y_{w}\right\}_{w=v_{i t}}^{t-1}\right)$ over the training period. The posterior mean network $\widehat{v}=\left\{\widehat{v}_{i j}\right\}_{i, j=1}^{K}$ can be obtained by

letting $\widehat{v}_{i j}=1$ if $\frac{\sum_{m=B+1}^{M} v_{i j}^{m}}{M-B} \geq 0.5$ and $\widehat{v}_{i j}=0$ otherwise, where $\left\{v_{i j}^{m}\right\}$ represents the sequence of Gibbs sampler draws for the parameter $v_{i j}, B$ is a fixed burn-in period and $M$ is the total number of draws. An alternative point estimate of the network structure $\widehat{v}$ is the posterior modal network, which is the configuration of $v$ most visited during the posterior sampling. From a decision theoretical perspective, the mean is the posterior summary which minimizes the posterior risk under a quadratic loss function, whereas the mode minimizes the posterior risk under an absolute value loss function (Berger (1985)). In the following examples the mean estimate will be preferred to the mode because the latter might not be unique. In order to graphically represent the network point estimate, an arrow will be drawn from neuron $j$ to neuron $i$ when $\widehat{v}_{i j}=1$. The DCG of the posterior mean network will be constructed by matching the set of arrows between all pairs of neurons together with the spatial coordinates of their somas.

Within the Bayesian framework, predicting the random spiking state $Y_{i, t+1}$ conditionally on the observed data $\left\{y_{w}\right\}_{w=1}^{t}$ can be carried out via the neuron's one step ahead marginal posterior predictive spiking probability, which for model (7) is

$$
\begin{aligned}
p_{i, t+1} & =P\left(Y_{i, t+1}=1 \mid\left\{y_{w}\right\}_{w=1}^{t}\right) \\
& =\int P\left(Y_{i, t+1}=1, \theta_{i}, \beta_{i 1}, \ldots, \beta_{i K} \mid\left\{y_{w}\right\}_{w=1}^{t}\right) d\left(\theta_{i}, \beta_{i 1}, \ldots, \beta_{i K}\right) \\
& =\int \pi_{i, t+1}\left(\theta_{i}, \beta_{i 1}, \ldots, \beta_{i K},\left\{y_{w}\right\}_{w=\tau_{i, t+1}}^{t}\right) \times \\
& \times f\left(\theta_{i}, \beta_{i 1}, \ldots, \beta_{i K} \mid\left\{y_{w}\right\}_{w=1}^{t}\right) d\left(\theta_{i}, \beta_{i 1}, \ldots, \beta_{i K}\right)
\end{aligned}
$$

The right-hand side of equation (8) is the expectation of the spiking probability for neuron $i$ at time $t+1$ with respect to the joint posterior density of its parameters $\left(\theta_{i}, \beta_{i 1}, \ldots, \beta_{i K}\right)$. Under model (7), these predictive probabilities cannot be computed analytically. However, the left-hand side of (8) can be estimated by Monte Carlo integration:

$$
\widehat{p}_{i, t+1}=\frac{\sum_{m=B+1}^{M} \pi_{i, t+1}\left(\theta_{i}^{m}, \beta_{i 1}^{m}, \ldots, \beta_{i K}^{m},\left\{y_{w}\right\}_{w=\tau_{i, t+1}}^{t}\right)}{M-B}
$$

where the summands on the right-hand side of (9) are defined in equation (3) and the sequence $\left\{\theta_{i}^{m}, \beta_{i 1}^{m}, \ldots, \beta_{i K}^{m}\right\}_{m=1}^{M}$ includes the Gibbs sampler draws of the parameters $\left(\theta_{i}, \beta_{i 1}, \ldots, \beta_{i K}\right)$. Given $\widehat{p}_{i, t+1}$, the one step ahead predicted spiking state is $\widehat{Y}_{i, t+1}=$ $1_{\left\{\widehat{p}_{i, t+1} \geq 0.5\right\}}$.

# 5 Model assessment 

Conditionally on the spike data observed along the training period, $\left(y_{1}, \ldots, y_{t^{*}}\right)$, the goodness of fit of model (7) can be evaluated through the fitting residuals

$$
r_{i t}^{f}=y_{i t}-\pi_{i t}, \quad i=1, \ldots, K ; t=1, \ldots, t^{*}
$$

If $y_{i t}=1$, then $r_{i t}^{f} \in[0,1]$ and the closer the residuals are to 1 , the more the fit is at odds with the observed data. If $y_{i t}=0$, then $r_{i t}^{f} \in[-1,0]$ and lack of fit is reflected by residuals close to -1 . Unfortunately, for model (7) the sampling distribution of these residuals is not known. As illustrated by Pregibon (1981), Landwehr et al. (1984) and Albert and Chib (1996), similar difficulties are encountered in the evaluation of the goodness of fit for the class of generalized linear regression models with binary outcomes. However, following Albert and Chib we note that, given the spike data over the training period, the Gibbs sampler draws of $(\theta, \beta)$ provide an estimate of the distribution of each residual $r_{i t}^{f}$ through equation (3). The latter estimate reflects the degree of agreement between the model fit and the training data. After observing the spike data up to time $T>t^{*}$, we can also compare the model predictions with the validation data using the prediction residuals

$$
r_{i t}^{p}=y_{i t}-p_{i t}
$$

where $t$ belongs to the validation period $\left\{t^{*}+1, \ldots, T\right\}$. Unlike the fitting residuals $r_{i t}^{f}$, conditionally on the spike data, the prediction residuals $r_{i t}^{p}$ do not depend on the model parameters.

Here we employ the estimated distributions of the fitting residuals and the estimated values of the prediction residuals as graphical displays of the consistency between the model results and the observed spiking patterns. For instance, if the assumption of an underlying constant functional connectivity structure does not hold for some neurons, we may expect their residuals to deteriorate over time. Furthermore, if the spiking activity of a group of measured neurons functionally depends on that of some unobserved neurons, we expect all residuals of the former group to depart from zero when the activity of the latter varies.

To provide a quantitative measure of the model fit and of its predictions, we use the well-known time-rescaling theorem (Papangelou (1972), Daley and Vere-Jones (2003) or, in the context of neuronal spiking models, Brown et al. (2001), Truccolo et al. (2005) and Feng (2003)). Let the sequence $\left\{s_{i j}\right\}_{j=1}^{J_{i}}$, with $J_{i}=\sum_{w=1}^{t^{*}} y_{i w}$ and $s_{i j}=\min \{s$ : $\left.\sum_{w=1}^{s} y_{i w}=j\right\}$, represent the spike times for neuron $i$ over the training period. For $j=$ $2, \ldots, J_{i}$, we define the rescaled spike times as $\widetilde{u}_{i j}=1-\exp \left(\sum_{t \leq s_{i j}} \widetilde{\pi}_{i t}-\sum_{t \leq s_{i, j-1}} \widetilde{\pi}_{i t}\right)$. Then we compare the empirical distribution function of the rescaled spike times with the cumulative distribution function of the uniform distribution on $(0,1)$. When the grid of time points adopted in (1) is fine with respect to the spike times and if the model fit is adequate, these functions should be approximately the same and the empirical distribution function should lie approximately on the $45^{\circ}$ line. An approximate $95 \%$ confidence band for this comparison, obtained from the Kolmogorov-Smirnov test, has width $2.72 \sqrt{J_{i}}$. To evaluate the adequacy of the model's predictions over the validation period we repeat for each neuron the same comparison as for the training period while using in the transformation of the spike times the estimated predictive spiking probabilities, $\widehat{p}_{i t}$, instead of the fitted spiking probabilities $\widehat{\pi}_{i t}$.

# 6 Analysis of a simulated dataset 

In this Section, we first illustrate the analysis of a set of simulated data by employing our implementation of model (7). Second, we evaluate the robustness of the model estimates when the same set of data is contaminated by a moderate proportion of false negative and false positive spiking states.

The simulated network includes ten neurons, so that the number of possible configurations of $v$ is $2^{10^{2}}=1.267651 e+30$. The true value of the connectivity matrix $v$ and of the network parameters $\beta$ were sampled from the hierarchical prior introduced in Section 3, having fixed $\alpha_{0}=0.50, \alpha=-2.00, \sigma=4.00$ and the shrinkage factor $\epsilon=0.05$. Moreover, the spatial coordinates of all neurons were sampled uniformly at random over the unit square. Four thousand data points were generated for each neuron by implementing equations (3) and (4). The sample was then divided in a training batch including the first half of the data points and a validation batch composed of the remaining data. On the left-hand side, Figure 1 shows the spike intensity functions (SIFs) for the simulated neurons. Each point of a SIF represents the proportion of spikes recorded for its corresponding neuron over windows of four hundred time points. In order to give a smoother representation, in Figure 1 the SIFs were computed using windows overlapping by one hundred time points. The firing rates of the ten neurons lie approximately within the interval $8-21$ percent. These low firing rates were obtained by setting $\theta_{i}=-s_{\theta}=-1.00$ and $\beta_{i i}=-1.5 \sigma$ for all neurons. In this example, we set these parameters to such low values in order to ensure that the simulated firing rates are comparable to those observed for in vitro multi-electrode recordings. Although these values are not generated from the prior, they are nevertheless included in their $95 \%$ prior probability intervals. On the right-hand side, Figure 1 shows the histograms of the inter-spike times for all neurons. The histograms display their largest mode between 5 and 10 time units, whereas most of inter-spike times are included in the interval $(1,25)$.

In order to analyse the simulated data through model (7), the prior standard deviations of the spatial dependence parameter and of the intercept $\alpha_{0}$ were set at $s_{\alpha_{0}}=s_{\alpha}=1 / 3$ whereas that of the coefficients $\theta$ was set at $s_{\theta}=1.00$. We used the Jeffreys' prior for the variance $\sigma^{2}$, letting its inverse gamma parameters be $a=0$ and $b=0$. The starting configuration for the posterior sampling of the network structure was the null network, whereas the starting value for $\sigma$ was 1.00 and those of the parameters $\left(\alpha_{0}, \alpha\right)$ were set at zero. The starting values for $(\theta, \beta)$ were set by numerically maximising the likelihood (4) with respect to these parameters. The posterior estimates were computed using a Gibbs sampler run of one hundred thousand iterations using a burn-in period of fifty thousand iterations. The posterior sampling for $(\theta, \beta)$ was carried out via a neuron-wise random scan random walk Metropolis within Gibbs step with independent Gaussian proposals having standard deviation 0.20 , which yielded acceptance ratios between 18 and 55 percent. In the current model implementation, these computations took half an hour to complete on a single 2 GHz laptop CPU with 1 Gb of RAM. Figure 2 illustrates

![img-0.jpeg](img-0.jpeg)

Figure 1: on the left-hand side, the plot shows the spike intensity functions (SIFs) for the ten simulated neurons, representing their proportions of spikes over overlapping windows 400 time points wide. On the right-hand side, the plot shows the histograms of the inter spike times for the ten simulated neurons.
the inference results for the parameters at the top of the hierarchy, namely $\left(\alpha_{0}, \alpha\right)$, and for the prior standard deviation $\sigma$. The posterior means for $\left(\alpha_{0}, \alpha\right)$ are respectively 0.69 and -1.67 with $95 \%$ equal tails posterior intervals $(-0.19,1.63)$ and $(-2.61,-0.78)$. The posterior mean for $\sigma$ is 4.53 and its $95 \%$ interval is $(3.44,6.10)$. The estimated $95 \%$ posterior intervals for these three parameters include their underlying true values.

The posterior mean for the network structure $v$ is shown in Figure 3. The plot on the left-hand side represents the estimated marginal posterior probabilities of all pair-wise network connections. In this plot, each row represents the estimated marginal posterior probabilities for the occurrence of functional connections incoming into a particular neuron, whereas each column represents the estimate probabilities for the outgoing connections originating from each neuron. The plot on the right-hand side shows the estimated network connections with estimated probability larger than 0.5 within their 2-dimensional spatial layout. In this plot, directed edges are represented as arrows and a vertical bar within a neuron represents the existence of a significant self-dependence over time. Furthermore, the red edges in this plot are associated to positive estimates for their corresponding parameter $\beta_{i j}$ whereas the green edges correspond to negative estimates. The estimated network coincides with the underlying true value of $v$.

As illustrated in Figure 4, the true values of all parameters $\theta$ are included in their

![img-1.jpeg](img-1.jpeg)

Figure 2: on the left-hand side, the two curves represent the Gibbs sampler frequencies for the intercept $\alpha_{0}$ (black) and for the spatial dependence coefficient $\alpha$ (red). On the right-hand side, the plot shows the posterior frequencies for the standard deviation $\sigma$. All the three $95 \%$ posterior intervals include their respective true values $\left(\alpha_{0}=0.50, \alpha=\right.$ $-2.00, \sigma=4.00)$.
![img-2.jpeg](img-2.jpeg)

Figure 3: the plot on the left-hand side represents the estimated marginal posterior probabilities of all pair-wise network connections. The plot on the right-hand side represents the estimated network structure within its 2-dimensional spatial layout. The estimated network structure coincides with the underlying true value of $v$.

estimated $95 \%$ posterior intervals. Furthermore, as opposed to the network parameters $\beta$, the precision of these estimates is comparable across neurons.
![img-3.jpeg](img-3.jpeg)

Figure 4: posterior inferences for the neurons' intercept parameters $\theta$. Plus symbols mark the positions of the true values of the parameters, whereas circles mark their estimated posterior means. Their common true value, -1.00 , lies within the estimated $95 \%$ posterior intervals for all neurons. Furthermore, the precision of these posterior estimates is comparable across neurons.

The posterior point estimates for the parameters $\beta$ are presented in Figure 5. On the upper left side, the plot represents the true values of these parameters. On the upper right side, the plot shows their estimated marginal posterior means. The two lower plots illustrate in detail the posterior estimates of the coefficients $\beta$ for the incoming connections of two representative neurons, namely number 2 and number 7 . In the latter two plots, circles mark the position of the estimated posterior means, triangles mark the endpoints of their $95 \%$ posterior intervals and plus signs indicate the true values of the corresponding coefficient. Due to the shrinkage prior (5), the width of the posterior intervals for the statistically insignificant coefficients, which estimated posterior mean lies around zero, is smaller than that of the significant network parameters.

Figures 6 illustrates the goodness of fit for neurons 2 and 7 over the training period, reflecting the typical model performance for these simulated data. On the left-hand side, the Figure reports the estimated posterior mean of the fitting residuals, marked by plus symbols, along with their $95 \%$ posterior intervals, which endpoints are marked

![img-4.jpeg](img-4.jpeg)

Figure 5: the upper left plot represents the true values of the network parameters $\beta$. The upper right plot represents their estimated marginal posterior means. The two plots at the bottom show in detail the estimates of the network parameters $\beta$ for the connections directed into the representative neurons 2 and 7 . The effect of the shrinkage prior can be appreciated in these two plots, where the $95 \%$ posterior intervals for the parameters close to zero are generally narrower than for the other parameters.

by triangles. At the times when the two neurons actually fired (marked in red) their fitted spiking probabilites are rather low, so that the fitting residuals are concentrated towards one. This feature should not be taken as an indication of lack of fit. In fact, given the low value of the neuronal intercepts $\theta$ and of the diagonal parameters $\beta$, their true spiking probabilities at the observed firing times lie approximately in the range $(0.05,0.35)$. In other terms, when the fitted parameter values coincide with their true values, the residuals marked in red in Figure 6 lie approximately in the range $(0.65,0.95)$. Therefore, as pointed out in the previous Section, we cannot base our conclusions about the lack of fit only on the magnitude of these fitting residuals. On the other hand, we note that the variability of these residuals for the two neurons is approximately constant over time, which is consistent with the assumption of a fixed network structure. On the right-hand side, the Figure compares the uniform CDF, represented by red lines, with the empirical CDF of the neurons' rescaled spike times, which have been computed using their estimated spiking probabilities as illustrated in the previous Section. These two plots show that the fit for both neurons is consistent with their uniform reference distribution.

# 6.1 Spike detection and robustness 

In this Section we use the simulated data analysed above to assess whether, under the shrinkage prior adopted in model (7), the posterior estimates are robust with respect to the occurrence of spike detection errors. We define this extrinsic noise component as the errors caused by the hardware used to record the neuronal spike trains, as in Gerstner and Kistler (2002). These errors should thus be distinguished from the intrinsic variability of the neuronal firing patterns, which is modelled in equation (4). Extrinsic noise can also be included in model (7) via a separate measurement error equation. However, currently very little is known about the statistical properties of the extrinsic noise affecting multiple spike trains recordings. Here we induce a moderate random error in the simulated data by changing the spiking status of each neuron at each time point independently with constant probability 0.01 . After contaminating the data with this extrinsic error, we repeat the analysis using the same priors and simulation strategy as above. The posterior means for the top-level parameters $\alpha_{0}, \alpha$ are respectively 0.66 and -1.77 with $95 \%$ posterior intervals $(-0.20,1.56)$ and $(-2.78,-0.81)$. With respect to its true value, the estimated network structure is missing the four pair-wise connections $10 \rightarrow 3,1 \rightarrow 5,2 \rightarrow 6$ and $4 \rightarrow 8$ whereas the remaining ninety-six entries of the matrix $v$ are correctly estimated. The posterior mean for $\sigma$ is 3.07 and its $95 \%$ posterior interval is $(2.24,4.40)$. The posterior intervals for 22 of the one hundred coefficients $\beta$ do not include their respective true values, with the largest bias occurring for the self-dependence parameters $\beta_{i i}$. The posterior intervals for all parameters $\theta$ include their common true value -1.00 .

From these results we conclude that, in presence of this moderate spike detection error, the posterior estimates for the network structure and for the coefficients at the

![img-5.jpeg](img-5.jpeg)

Figure 6: evaluation of the goodness of fit for neurons 2 and 7 over the training period. The plots on the left-hand side represent the estimated posterior means of the fitting residuals for the two neurons (plus signs) along with their $95 \%$ posterior intervals (delimited by triangles). The red points correspond to the neurons' spike times whereas the blue points correspond to time intervals during which the corresponding neuron did not fire. The plots on the right-hand side represent the evaluation of the goodness of fit using the time-rescaling theorem. For both neurons, the fitting residuals corresponding to their spiking times are rather high, reflecting their low spiking probabilities. Furthermore, the plots on the right-hand side show that the transformed spike times obtained using the estimates values of $(\theta, \beta)$ are consistent with their uniform reference distribution.

top of our model's hierarchy are not affected, whereas a considerable proportion of the connectivity parameters $\beta$ may be significantly biased.

# 7 In vitro multiple spike train analysis 

In this Section we analyse via model (7) a set of multiple spike trains recorded from an ensemble of neurons cultured in-vitro. A detailed description of the materials and methods employed to generate the data can be found in Van Pelt et al. (2004). The neurons recorded during the experiment are part of a large pool of dissociated rat cortical cells. After extraction from the rat embryo, the cells were plated as a monolayer in a culture chamber, the bottom of which consisted of a multi-electrode array (MEA), i.e. a glass plate in which 61 conductive lanes where etched, ending in a hexagonal pattern of electrode tips with diameter $12 \mu \mathrm{~m}$. In this experiment, the size of the electrodes roughly matches that of the somas, ensuring that the detected spikes mostly originate from single cells. Since the Euclidean distance between neighboring electrodes is $70 \mu \mathrm{~m}$, the space between electrodes is filled with many cells from which no activity is recorded. Therefore, in this example the structure of functional connections among the recorded cells cannot be interpreted as corresponding to their physical network of synapses. The data consist of the spiking times recorded at the 61 electrodes for more than 40 days in-vitro (DIV). No external stimulation was given during the whole experiment, so that the resulting firing patterns and the corresponding network dynamics are entirely spontaneous. In this Section we will analyze the spikes recorded during the first four minutes of the twelfth hour of day 14 of the experiment for electrodes ( $7,11,22,29,37,46,52,53$ ). The first two minutes of recordings will be used to estimate the model parameters and the successive two minutes will be used to compute the prediction residuals. We focus on this subset of neurons because the remaining 53 electrodes do not exhibit enough activity to estimate their network parameters with acceptable precision within such a short time frame. Although the cultured network at 14 DIV is still in a developing state, the period over which the data is being analyzed is much smaller than the time scale of neurite outgrowth and synapse formation. Therefore we can reasonably assume that the functional connectivity within these four minutes is stable.

In this Section we discretised the spike data into time bins with constant width of one millisecond. Figure 7 shows the spike intensities of the eight neurons along with the histograms of their inter-spike times. The latter plot emphasizes that the spiking activity of these neurons is markedly different, with numbers 22 and 29 exhibiting many more spikes than the other six cells. Furthermore, as noted in Van Pelt et al. (2005), the spike intensities display a cyclical pattern characterised by very low levels of activity. In particular, Figure 7 shows that for each cycle of network activity the firing rate of number 29, depicted in cyan, increases over time until firing of all the other neurons is triggered. The latter in turn appear to inhibit firing of number 29 until all neurons fall silent. The successive cycle of network activity seems to be initiated spontaneously by neuron 29. Our main interest in analysing this data is to investigate whether the posterior inferences of model (7) can adequately explain and predict such spiking pattern.

![img-6.jpeg](img-6.jpeg)

Figure 7: spike intensity functions and histograms of the inter-spike times for the eight analysed neurons. Neurons 22 and 29 exhibit many more spikes than the remaining six neurons. The activity of all neurons is markedly cyclical, with neuron 29 (depicted in cyan) starting a new cycle soon after all neurons fall silent.

Simulation based inferences for all model parameters were obtained by summarizing a Gibbs sampler run of fifty thousand iterations after discarding a burn-in period of twenty thousand iterations. As in the previous Section, the parameters $(\sigma, v)$ were updated in closed form, whereas updating for $\left(\alpha_{0}, \alpha\right)$ was carried out via a vector-wise random walk Metropolis step and that of $(\theta, \beta)$ was performed by a neuron-wise random walk Metropolis step with independent Gaussian proposals. The prior setting for all model parameters is the same as in the previous example. Completion of the posterior sampling took approximately twelve hours on a single 2 GHz laptop CPU using 1 Gb of RAM. Figure 8 shows the Gibbs sampler draws and the corresponding posterior frequencies for the intercept $\alpha_{0}$, for the spatial dependence coefficient $\alpha$ and for the prior standard deviation $\sigma$. The former has estimated posterior mean 0.48 and $95 \%$ posterior interval $(-0.08,1.03)$. The estimated posterior mean for $\alpha$ is -0.22 and its $95 \%$ posterior interval is $(-0.69,0.28)$. The posterior mean for $\sigma$ is 13.94 and its $95 \%$ posterior interval is $(10.42,18.73)$. From these inferences we conclude that the analysed neurons tend to develop functional connections with other cells in their vicinity more likely than with far cells. Furthermore, since the shrinkage factor was set at $\epsilon=0.05$, the latter results imply that a priori the network parameters $\beta$ within the interval $(-4.20 .4 .20)$ are not associated with significant pair-wise functional connections.

The posterior inference for the network structure $v$ are shown in Figure 9. The plot on the left-hand side reports the estimated marginal posterior probabilities for each

![img-7.jpeg](img-7.jpeg)

Figure 8: on top, the plots show the Gibbs sampler draws of $\left(\alpha_{0}, \alpha\right)$ (left) and for $\sigma$ (right). At the bottom, posterior inferences for $\left(\alpha_{0}, \alpha\right)$ (left) and for $\sigma$ (right). Most of the posterior mass for the spatial dependence parameter is allocated to negative values, suggesting that couples of neurons which are close in space develop direct functional connections more likely than neurons which are far from each other. Given $\epsilon=0.05$, the posterior inference for $\sigma$ indicate that a priori the network parameters $\beta$ within the interval $(-4.20,4.20)$ do not correspond to significant network connections.

# 752Bayesian Modelling and Analysis of Spatio-Temporal Neuronal Networks 

network pair-wise connection. The plot on the right-hand side represents the functional connections with estimated probability larger than 0.5 , projected on the MEA's layout. The posterior inferences uncover a complex network of 42 pair-wise functional relationships, of which 20 are inhibitory and 22 are excitatory. In particular, with high probability neuron 29 receives input from all other neurons in the network and it provides excitatory inputs to its nearest neighbours, numbers 22 and 37 . Moreover, despite of its relatively isolated position, neuron number 11 provides input to all other neurons but to number 7 .
![img-8.jpeg](img-8.jpeg)

Figure 9: on the left-hand side, estimated marginal posterior probabilities for each pairwise functional connection. On the right-hand side, estimated posterior mean network. The pivotal role of neuron 29 is reflected by these estimates. This neuron in fact receives significant input from all other neurons in the network and it provides excitatory inputs to its two nearest neighbours, numbers 22 and 37 .

As can be seen in Figure 10, the estimated values for the neuronal intercepts $\theta$ are negative, reflecting the low firing rates of all neurons. However, the posterior mean of the neurons exhibiting more spikes, number 22 and 29 , have a larger value than those of the other neurons. In particular, the estimate for $\theta_{29}$ may partially account for the fact that, as noted in Figure 7, following each interruption of the spiking activity of all neurons, number 29 starts spontaneously a new cycle of network firing.

Figure 11 shows the posterior inferences for the network parameters $\beta$. The upper left plot represents their estimated posterior means. The plot shows that neuron 29 is

![img-9.jpeg](img-9.jpeg)

Figure 10: posterior inferences for the intercept parameters $\theta$. The high estimates for $\theta_{22}$ and $\theta_{29}$ explain the higher firing rates of these two neurons with respect to the remaining six cells.
strongly excited by number $11,22,46$ and 52 whereas it is inhibited by its own activity and by that of neuron 53 . The activity of the latter is promoted and promotes that of neurons 11 and 22. The remaining three plots in the figure represent the estimated posterior means and the $95 \%$ posterior intervals of the network parameters for the incoming connections of three representative neurons, namely number 11, 22 and 29. The width of the posterior intervals reflects the information content of the data for different pair-wise interactions. For instance, the self-dependence parameters for the relatively high-firing neurons $\beta_{22,22}$ and $\beta_{29,29}$ are estimated with good precision, whereas the interactions with the lowest-firing neuron, $\beta_{37,11}, \beta_{37,22}$ and $\beta_{37,29}$, exhibit large posterior intervals.

In Figure 12 are displayed the fitting and prediction residuals for neurons 22 and 29, which are the most active in the analysed ensemble. The estimated firing probabilities for both neurons lie in the range $(0.20,0.58)$, so that the residuals corresponding to their firing times are rather high. As pointed out in the previous example, in absence of a reference distribution for the residuals, we cannot interpret these relatively high values as indicating a significant lack of fit and of predictive power. However, also some of the residuals at times when the two neurons did not spike appear to be large. In particular, these negative residuals are concentrated over the same short time periods for both cells, suggesting that the model might fail to capture a common inhibitory input. Given that along the analysed period the remaining 53 recorded neurons hardly displayed any activity, we conclude that such an inhibitory input may be originated by one or more of the cells in the culture which was not recorded by the MEA. Finally,

![img-10.jpeg](img-10.jpeg)

Figure 11: the upper left plot represents the estimated posterior means for all the network parameters $\beta$. The remaining three plots show in detail the posterior inferences for the parameters $\beta$ corresponding to the connections incoming into neurons 11, 22 and 29. Neuron 29 is strongly excited by number $11,22,46$ and 52 , whereas it is inhibited by its own activity and by that of neuron 53 . The activity of the latter is promoted and promotes that of neurons 11 and 22 .

the pattern of both these residuals as well as that of the remaining six neurons appears to be constant over time, suggesting that the structure of the functional connections among the neurons does not change over the analysed recordings.
![img-11.jpeg](img-11.jpeg)

Figure 12: estimated fitting residuals (left-hand side) and estimated prediction residuals (right-hand side) for neurons 22 and 29. The estimated firing probabilities for both neurons lie in the range $(0.20,0.58)$, so that the residuals corresponding to their firing times are rather high. The negative residuals for both neurons are concentrated approximately over the same short time periods, suggesting that the model might fail to capture a common inhibitory input for these two neurons.

Our model's fit and predictions were again evaluated for the eight analysed neurons via the time-rescaling theorem. The model results are generally consistent with the uniform reference distribution of the rescaled spike times for all neurons. The results for the two

# 756Bayesian Modelling and Analysis of Spatio-Temporal Neuronal Networks 

most active cells, which are neurons 22 and 29, are presented in Figure 13. From these results we conclude that the parameter values inferred during the training period predict adequately the spiking pattern observed during the validation period. Consistently with the residuals illustrated in Figure 12, this suggests that the network structure and the connectivity parameters did not significantly change over the analysed recordings.
![img-12.jpeg](img-12.jpeg)

Figure 13: evaluation of the model fit (on left-hand side) and of the predictions (on the right-hand side) via the time-rescaling theorem for neurons 22 and 29. The model results are generally consistent with the uniform reference distribution of the rescaled spike times for both neurons.

# 8 Discussion 

In this paper we introduced a novel Bayesian hierarchical network model for the analysis of multiple spike trains recordings. As in Brillinger (1988a) and in Brillinger and Villa (1997), we defined the spiking probabilities over a finite grid of time intervals. Along the lines of Kass and Ventura (2001), we adopted a Markovian dependence structure of varying order over time to mimic some of the main features of the spiking process. A distinctive feature of our approach is that the network structure $v$ is modelled explicitly as one of the unknown parameters via a shrinkage prior for the network effects $\beta$. Within this hierarchical model structure, the network connectivity is explained by a regression term including the available fixed-time covariates. We note that these are two differences of our approach with respect to the model proposed by Truccolo et al. (2005), where the effects of their time-varying covariates and those of the network inputs independently influence a neuron's firing probability. Of course, when both fixed covariates and time-varying covariates are available, integrating these two approaches would be recommendable. For instance, equation (3) can be generalised by introducing a neuron-specific and time-dependent regression term.

In this work we model via equation (3) the relationships between the network coefficients $\beta$, the past history of the spiking process $Y$ and the firing probabilities of the neurons being analysed. This aspect of model (7) is very specific and it arises from several simplifying assumptions. For instance, in equation (3) the firings recorded within each inter-spike time of a given neuron $i$ are not weighted using their arrival times, but they contribute by the same amount via the proportion $\frac{\sum_{i_{0}=t_{i j}} Y_{j w}}{1-\beta_{j i}}$. Moreover, although the exponent of equation (3) is linear in the model parameters $(\theta, \beta)$, the logit link implies a symmetric saturation of the spiking probability with respect to the input process. In fact, since the logistic density is a symmetric bell-shaped curve, the fluctuations of the network activity produce small changes of a neuron's firing probability when the exponent of (3) is far from zero and larger changes when it is close to zero. For these reasons, we regard further investigation of this model stage as a key focus for our forthcoming research.

Since the number of possible network configurations for any set of $K$ neurons is $2^{K^{2}}$, an exhaustive search throughout its domain is computationally infeasible even for small networks. The Markov chain Monte Carlo (MCMC) estimation for $v$ proposed in Section 4 is an appealing alternative to exhaustive model search because, rather than systematically scanning the state space, the Gibbs sampler tends to visit more frequently the network configurations with high posterior probability and it rejects those which could not have generated the observed spiking patterns. In particular, when the posterior distribution of $v$ is characterized by several peaks, the Gibbs sampler can effectively locate the most likely configurations. In such a case, instead of adopting the posterior mean as the point estimate of the network structure, it may be more informative to report all the configurations associated with the highest estimated marginal posterior probabilities. For the analyses presented above, the standard Gibbs sampler generated reliable posterior inferences for all the model parameters. It was also noted that when the firing rates of the neurons to be analysed are very low, a neuron-wise update of

$(\theta, \beta)$ yields more reliable estimates than a component-wise sampling. However, since the number of parameters of model (7) grows more than quadratically with the number of recorded neurons, computing reliable MCMC estimates for large neuronal ensembles is a critical issue. In particular, while the estimation of the parameters $\left(\alpha_{0}, \alpha\right)$, representing global network properties, benefits from the inclusion of additional neurons, estimating a large number of network parameters $\beta$, which represent local network properties, may pose serious computational problems. In the authors' experience, the current implementation of model (7) is effective for the analysis of networks including up to about one hundred neurons recorded over a few minutes. For larger networks, faster mixing of the Markov chains may be obtained by employing more sophisticated posterior samplers. For instance, Nott and Green (2004) proposed a method for the Bayesian assessment of the model uncertainty based on the Swendsen-Wang algorithm (Swendsen and Wang (1987)). In the context of model (7), Nott and Green's sampler prescribes the introduction of a further layer of auxiliary variables conditionally on which the parameters $\beta$ can be efficiently block-updated. Alternatively to variable augmentation methods, a multiple-chains sampler such as the parallel tempering algorithm (Geyer (1991)) may be employed. Since these alternatives are computationally more expensive than the standard Gibbs updating, in general the choice of the posterior sampler will reflect a compromise between mixing of the Markov chains and computational speed. Finally, from the computational perspective it is important to note that, conditionally on $\sigma$, the joint posterior distribution of the parameters $(\theta, \beta)$ factors into a product of neuron-specific posterior distributions. Therefore, when the network to be analysed is large, fast posterior sampling can be implemented by updating in parallel the likelihood parameters belonging to different neurons.

Section 6 demonstrates that the current implementation of model (7) can effectively recover the true parameter values for a set of simulated data which firing rates are comparable to those observed for in vitro recordings. Furthermore, we showed that the shrinkage prior (5) yields robust estimates for the network structure with respect to a moderate random spike detection error. This is a relevant model feature because, as emphasised in Section 7, experimental multiple spike trains typically report the activity of a small fraction of the neurons in culture and can be affected by several sources of error. Moreover, specific sources of extrinsic noise can be added to the hierarchical framework (7) in the form of a measurement error equation in order to further enhance the robustness of the posterior estimates. For instance, spike sorting errors may be modelled by introducing a spatially correlated extrinsic noise structure. From this perspective, additional topics for further research are the study of explicit formulations for such measurement errors and assessing the robustness of model (7) with respect to missing neurons.

Finally, the results of our analysis in Section 7 suggest that functional connections among pairs of neurons are more likely established between cells which somas are close in space. Furthermore, we concluded that neuron 29 plays a key role in the initiation of the network activity, which reveals over time a complex pattern of functional network relationships among the eight analysed cells. We note that the latter findings are consistent with the exploratory analysis over longer time periods reported in Van Pelt et al.

(2004). From this perspective, we look forward to using model (7) to fit multiple spike trains including richer sets of covariates.

# Appendix 

The expressions for the FCPDs of all the model parameters are reported in this Section. In the following equations, the symbol $\propto$ indicates that the left-hand side is proportional to the right-hand side up to a multiplicative constant.

Conditionally on the array $\left(s_{\alpha}, X, v, \alpha_{0}\right)$, the spatial dependence coefficient $\alpha$ is a posteriori independent of $(\theta, \beta, \sigma, Y)$. Its FCPD satisfies

$$
f\left(\alpha \mid s_{\alpha}, X, v, \alpha_{0}\right) \propto \phi\left(\alpha \mid s_{\alpha}\right) \prod_{i j} e^{\alpha x_{i j} v_{i j}}\left(1+e^{\alpha_{0}+\alpha x_{i j}}\right)^{-1}
$$

where $\phi\left(. \mid s_{\alpha}\right)$ is the Gaussian density with zero mean and with standard deviation $s_{\alpha}$. This conditional posterior density does not have a closed form so that updating of $\alpha$ within the Gibbs sampler can be carried out via the Metropolis-Hastings algorithm (Metropolis et al. (1953), Hastings (1970)).

Conditionally on $\left(s_{\alpha}, X, v, \alpha\right)$, the intercept coefficient $\alpha_{0}$ is a posteriori independent of the spike data and of the remaining model parameters. For its FCPD we have

$$
f\left(\alpha_{0} \mid s_{\alpha}, X, v, \alpha\right) \propto \phi\left(\alpha_{0} \mid s_{\alpha}\right) \prod_{i j} e^{\alpha_{0} v_{i j}}\left(1+e^{\alpha_{0}+\alpha x_{i j}}\right)^{-1}
$$

As for the spatial dependence parameter, updating of $\alpha_{0}$ can be carried out via a Metropolis within Gibbs step.

Conditionally on $\left(\beta_{i j}, \alpha_{0}, \alpha, x_{i j}, \sigma, \epsilon\right)$ each $v_{i j}$ is a Bernoulli random variable independent of the remaining parameters and of the spike data. Its conditional posterior success probability is given by

$$
P\left(v_{i j}=1 \mid \beta_{i j}, \alpha_{0}, \alpha, x_{i j}, \sigma, \epsilon\right)=\frac{\phi\left(\beta_{i j} \mid \sigma\right) e^{\alpha_{0}+\alpha x_{i j}}}{\phi\left(\beta_{i j} \mid \sigma\right) e^{\alpha_{0}+\alpha x_{i j}}+\phi\left(\beta_{i j} \mid \sigma \epsilon\right)}
$$

Given $(\epsilon, \beta, v)$ and under the inverse gamma prior adopted in model (7), the FCPD of $\sigma^{2}$ is inverse gamma with parameters $\left(a^{*}, b^{*}\right)$ defined as

$$
\begin{aligned}
a^{*} & =a+\frac{K^{2}}{2} \\
b^{*} & =b+0.5 \sum_{i j} \frac{\beta_{i j}^{2}}{v_{i j}+\epsilon^{2}\left(1-v_{i j}\right)}
\end{aligned}
$$

so that updating for $\sigma$ can be carried out in closed form.

# 760Bayesian Modelling and Analysis of Spatio-Temporal Neuronal Networks 

For the FCPD of each parameter $\beta_{i j}$ we have

$$
\begin{aligned}
f\left(\beta_{i j} \mid Y, v_{i j}, \beta_{i,-j}, \sigma, \epsilon, \theta_{i}\right) & \propto \phi\left(\beta_{i j} \mid \sigma_{i j}\right) \prod_{t} e^{Y_{i t} \beta_{i j} \frac{\sum_{i-l_{\sigma_{i t}}^{i}} v_{i j}}{t-l_{i t}}} \times \\
& \times\left(1+e^{\theta_{i}+\sum_{k} \beta_{i k} \frac{\sum_{i-l_{\sigma_{i t}}^{i}} v_{i k}^{k}}{t-l_{i t}}}\right)^{-1}
\end{aligned}
$$

where $\sigma_{i j}$ is given in equation (5) and $\beta_{i,-j}$ represents the $i$ th row of the matrix $\beta$ except $\beta_{i j}$. Updating of each $\beta_{i j}$ can be carried out via a Metropolis within Gibbs step as for the parameters $\alpha$.

The FCPD of each neuron-specific parameter $\theta_{i}$ is given by

$$
f\left(\theta_{i} \mid Y, \beta, \theta_{-i}, s_{\theta}\right) \propto \phi\left(\theta_{i} \mid s_{\theta}\right) \prod_{t} e^{Y_{i t} \theta_{i}}\left(1+e^{\theta_{i}+\sum_{j} \beta_{i j} \frac{\sum_{i-l_{\sigma_{i t}}^{i}} v_{i j}}{t-l_{i t}}}\right)^{-1}
$$

where $\theta_{-i}$ stands for the vector $\theta$ but its $i$ th term. These conditional posterior densities are not available for exact sampling, so that the Metropolis-Hastings algorithm can be employed to produce approximate posterior inferences also for the neuronal intercepts $\theta$.

# 762Bayesian Modelling and Analysis of Spatio-Temporal Neuronal Networks 

A.E. Gelfand and A. F. M. Smith. Sampling-based approaches to calculating marginal densities. Journal of the American Statistical Association, 85:398-409, 1990. 739
E. George and D. Foster. Calibration and empirical Bayes variable selection. Technical Report, University of Texas at Austin and University of Pennsylvania, USA, 1997. 738
E.I. George and R.E. McCulloch. Variable selection via Gibbs sampling. Journal of the American Statistical Association, 88:882-889, 1993. 734, 738
E.I. George and R.E. McCulloch. Approaches for Bayesian variable selection. Statistica Sinica, $7: 339-373,1997.733$
W. Gerstner and W.M. Kistler. Spiking Neuron Models. Cambridge University Press, 2002. 734,747
C.J. Geyer. Markov chain Monte Carlo maximum likelihood. In Proceedings on the 23rd Symposium on the Interface between Computing Science and Statistics, pages 156-163, Seattle, WA, 1991. Interface Foundation of North America. 758
Z. Ghahramani. Learning dynamic Bayesian networks. Adaptive processing of sequences and data structures. Lecture notes in artificial intelligence. C.L.Giles and M.Gori editors. Springer-Verlag, 1998. 733
S. Godsill. On the relationship between MCMC model uncertainty methods. Journal of Computational and Graphical Statistics, 10:230-248, 2001. 733
P.J. Green. Reversible jump MCMC computation and Bayesian model determination. Biometrika, 82:711-732, 1995. 734
W.K. Hastings. Monte Carlo sampling methods using Markov chains and their applications. Biometrika, 57-1:97-109, 1970. 759
D. Heckerman. A tutorial on learning with Bayesian networks. Technical Report MSR-TR-9506, Microsoft Research, Redmond, Washington, 1996. 733
A.L. Hodgkin and A.F. Huxley. A quantitative description of membrane current and its application to conduction and excitation in nerve. Journal of Physiology, 117:500-544, 1952. 734
S. Iyengar. The analysis of multiple neural spike trains. In: Advances in Methodological and Applied Aspects of probability and Statistics; N. Bolakrishnan editor; Gordon and Breack, pages $507-524,2001.734$
E.M. Izhikevitch. Resonate and fire neurons. Neural networks, 10:1171-1266, 2001. 734
R.E. Kass and V. Ventura. A spike train probability model. Neural computation, 13:1713-1720, 2001. 734, 736, 757
R.E. Kass, V. Ventura, and E. Brown. Statistical issues in the analysis of neuronal data. Journal of Neurophysiology, 94:8-25, 2005. 735
R.E. Kass, V. Ventura, and C. Cai. Statistical smoothing of neuronal data. NETWORK: Computation in Neural Systems, 14:5-15, 2003. 734

J.M. Landwehr, D. Pregibon, and A.C. Shoemaker. Graphical methods for assessing logistic regression models. Journal of the American Statistical Association, 385:61-71, 1984. 741
S.L. Lauritzen. Graphical models. Oxford University press, 1996. 736
S.L. Lauritzen and D.J. Spiegelhalter. Local computations with probabilities on graphical structures and their applications to expert systems. Journal of the Royal Statistical Society B, 50:157-224, 1988. 736
L. Martignon, G. Deco, K. Laskey, M. Diamond, W. Freiwald, and E. Vaadia. Neural coding: higher-order temporal patterns in the neurostatistics of cell assemblies. Neural Computation, $12: 2621-2653,2000 . \quad 735$
N. Metropolis, A. Rosenbluth, M. Rosenbluth, M. Teller, and E. Teller. Equations of state calculations by fast computing machines. J. Chem. Phys., 21:1087-2092, 1953. 759
F.O. Morin, Y. Takamura, and E. Tamiya. Investigating neuronal activity with planar microelectrode arrays: achievements and new perspectives. Journal of Bioscience and Bioengineering, 100:131-143, 2005. 734
K. Murphy. An introduction to graphical models. Intel Research Technical Report, 2001. 733
K. Murphy and S. Mian. Modelling gene expression data using dynamic bayesian networks. Technical report, Computer Science Division, University of California, Berkeley, CA., 1999. 733
J.S. Nagumo, S. Arimoto, and S. Yoshizawa. An active pulse transmission line simulating nerve axon. Proceedings of the IRE, 50:2061-2072, 1962. 734
D.J. Nott and P.J. Green. Bayesian veriable selection and the Swendsen-Wang algorithm. Journal of computational and Graphical Statistics, 13:141-157, 2004. 758
M. Okatan, M.A. Wilson, and E.N. Brown. Analyzing functional connectivity using a network likelihood model of ensemble neural spiking activity. Neural computation, 17:1927-1961, 2005. 735
F. Papangelou. Integrability of expected increments of point processes and related random change of scale. Transactions of the American Mathematical Society, 165:483-506, 1972. 741
D. Pregibon. Logistic regression diagnostics. The Annals of Statistics, 9:705-724, 1981. 741
R.P.N. Rao. Hierarchical Bayesian inference in networks of spiking neurons. To appear in: Advances in NIPS; MIT press, 17, 2005. 735
A. F.M. Smith and G.O. Roberts. Bayesian computations via the Gibbs sampler and related Markov chain monte Carlo methods. Journal of the Royal Statistical Society B, 55:3-23, 1993. 739
D.J. Spiegelhalter, N.G. Best, P.B. Carlin, and A. van der Linde. Bayesian measures of model complexity and fit. Journal of the Royal Statistical Society B, 64:583-639, 2002. 733

# 764Bayesian Modelling and Analysis of Spatio-Temporal Neuronal Networks 

P. Spirtes. Directed cyclic graphical representations of feedback models. Proceedings of the eleventh conference on uncertainty in artificial intelligence. Philippe Besnard and Steve Hanks editors. Morgan Kauffmann Publishing Incorporation. San Mateo, pages 491-498, 1995. 733
R.H. Swendsen and J.S. Wang. Nonuniversal critical dynamics in Monte Carlo simulations. Physics review letters, 58:86-88, 1987. 758
L. Tierney. Markov chains for exploring posterior distributions. The Annals of Statistics, 22: $1701-1762,1994 . \quad 739$
W. Truccolo, U.T. Eden, M.R. Fellows, J.P. Donoghue, and E.N. Brown. A point process framework for relating neural spiking activity to spiking history, neural ensemble and extrinsic covariate effects. Journal of Neurophysiology, 93:1074-1089, 2005. 735, 737, 741, 757
D.A. Turner and M. West. Statistical analysis of mixtures applied to postsynaptic potential fluctuations. Journal of neuroscience methods, 47:1-23, 1993. 734
J. Van Pelt, I. Vajda, P.S. Wolters, M.A. Corner, and G.J.A. Ramakers. Dynamics and plasticity in developing neuronal networks in vitro. Progress in brain research, 147:173-187, 2005. 749
J. Van Pelt, P.S. Wolters, M.A. Corner, W.L.C. Rutten, and G.J.A. Ramakers. Long-term characterization of firing dynamics of spontaneous bursts in cultured neural networks. IEEE Trans. BioMed. Eng., 51:2051-2062, 2004. 734, 749, 758
M. West. Hierarchical mixture models in neurological transmission analysis. Journal of the American Statistical Association, 92:587-606, 1997. 734
M. West and D.A. Turner. Deconvolution of mixtures in analysis of neural synaptic transmission. The Statistician, 43:31-43, 1992. 734
M.W. Woolrich, M. Jenkinson, M.J. Brady, and S.M. Smith. Fully Bayesian spatio-temporal modelling of FMRI data. IEEE transcripts on medical imaging, 23:213-231, 2004. 734

## Acknowledgments

The authors wish to thank two anonymous referees and the editor, whose comments contributed to a substantial improvement of this paper. The development of this paper has also benefited from numerous conversations with the members of the CASPAN group Arjen B. Brussaard, Ronald van Elburg, Arjen van Ooyen and Randal Koene. The implementation of model (7) can be obtained upon request to the first author in the form of an independent MATLAB toolbox for non-commercial use only.