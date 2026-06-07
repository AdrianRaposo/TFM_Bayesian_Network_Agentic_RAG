# Time-Dependent Gene Network Modelling by Sequential Monte Carlo 

Sergiy Ancherbak, Ercan E. Kuruoğlu, and Martin Vingron


#### Abstract

Most existing methods used for gene regulatory network modeling are dedicated to inference of steady state networks, which are prevalent over all time instants. However, gene interactions evolve over time. Information about the gene interactions in different stages of the life cycle of a cell or an organism is of high importance for biology. In the statistical graphical models literature, one can find a number of methods for studying steady-state network structures while the study of time varying networks is rather recent. A sequential Monte Carlo method, namely particle filtering (PF), provides a powerful tool for dynamic time series analysis. In this work, the PF technique is proposed for dynamic network inference and its potentials in time varying gene expression data tracking are demonstrated. The data used for validation are synthetic time series data available from the DREAM4 challenge, generated from known network topologies and obtained from transcriptional regulatory networks of S. cerevisiae. We model the gene interactions over the course of time with multivariate linear regressions where the parameters of the regressive process are changing over time.


Index Terms—Bayesian network, gene expression data, gene network, particle filter, sequential Monte Carlo, time series

## 1 INTRODUCTION

CHANGES in the gene expression in time and under different external/internal stimulus play an important role in protein production. It is well known that expression level of one gene can influence that of another gene. Usually, genes with similar expression profiles are more likely to encode interacting proteins [1], [2]. It was also shown that the genes of experimentally derived protein complexes are often co-expressed [3]. Such variations in expression levels can have significant effect on the functions of the genes in a single cell or in a complex organism.

Thus, genes should be studied in a group, as a number of objects, which form a network, interacting with each other, and not as isolated entities. Interactions between genes have long been studied in model organisms in order to identify functional relationships among genes or their corresponding gene products [4], [5], [6]. Examples of model organisms studied in the literature include yeast [6], [7] and Drosophila Melanogaster [8].

The interactions among genes in a network are not stationary during the life cycle of an organism. These relations evolve over time as shown experimentally in [7], [9]. Such relations/interactions can change over time depending on life period and/or various external factors [7], [8], [9], [10], [11]. Information about dynamically changing gene network in different stages of a life cycle is of high importance for biology. It plays an important role in the understanding of

- S. Ancherbak and E.E. Kuruoğlu are with the Istituto di Scienza e Tecnologie dell'Informazione, "A. Faedo", CNR (Institute of the National Research Council of Italy), via G. Moruzzi 156124, Pisa, Italy. E-mail: ancherbaks@gmail.com, ercan.kuruoglu@isti.cnr.it.
- M. Vingron is with the Max Planck Institute for Molecular Genetics, Ihnestraße 63-73, 14195, Berlin, Germany.
E-mail: vingron@molgen.mpg.de.
Manuscript received 12 Mar. 2015; revised 17 Aug. 2015; accepted 28 Sept. 2015. Date of publication 30 Oct. 2015; date of current version 5 Dec. 2016. For information on obtaining reprints of this article, please send e-mail to: reprints@ieee.org, and reference the Digital Object Identifier below. Digital Object Identifier no. 10.1109/TCBB.2015.2496301
human disease [12], [13], [14] and in designing personalized treatment plans.

Usually to model relations between genes in a network gene expression data are used. A large amount of gene expression data measured at a single time instant can be found in the literature [15], [16], [17], [18], [19], [20]. These data are obtained via microarray experiments which can measure thousands of genes of an organism, providing a "genomic" viewpoint on gene expression. To understand the temporal variations in relations among genes, we are interested in time series data, i.e., gene expression levels measured with time during the life cycle of an organism. Some sources present experimental data on the evolution of temporal sequence datasets for gene expression during the yeast cell cycle and the life cycle of Drosophila Melanogaster [7], [8], [21], [22], [23] and also studies on circadian rhythms in mammals [10], [11]. However, for most of them only one temporal sequence dataset is available for each gene. Moreover, all experimental data are measured for a quite short time length. This lack of experimental information significantly limits the success of inference on network topology.

To simplify the analysis, many authors discretize measured gene expression values into two (expressed (1), not expressed $(-1)$ ) or three levels (under-expressed ( -1 ), normal (0), and over-expressed (1), depending on whether the gene expression value is significantly lower than, similar to, or greater than certain threshold value, respectively) [24]. It is obvious that by discretizing the measured expression data important information can be lost. On the other hand, it allows us to specify a probability with which a discrete expression level is assumed by a gene. Then the relations between genes in a network can be represented by a conditional probability table. This is one of the most commonly used representations which can describe any discrete conditional distribution.

Another popular representation is to use continuous variables of gene expression data. Unlike the case of discrete

variables there is no way to represent all possible values. An obvious choice for multivariate continuous variables is to use certain distributions, e.g., Gaussian one [25].

Due to lack of experimental data, most existing methods used for gene regulatory network reconstruction are concentrated on the inference of steady state networks [24], [26], [27], [28]. Others divide whole time-series sequences into a number of homogeneous subsequences where one averaged network is estimated for each of subintervals [29], [30]. In such cases, the dynamics in the gene network during the life cycle is represented by a number of frames averaged over the subintervals. This procedure again does not take into account information between adjacent time intervals.

In the statistical graphical models literature, one can find a number of methods for studying the network structure [31], [32], [33], [34], [35] while the study of time-varying networks is rather recent. In this work, we propose a linear vector regression model for time changes in a gene interaction network which we learn via a state of the art sequential Monte Carlo method, namely Particle Filtering. Such networks describe the conditional dependence structure between multiple interacting quantities, in our case expression values of different genes, which are changing in time. Moreover, our approach is capable of handling noise which is always present in experimental data. Therefore, the interactions, the signal of which in the data is strong, can be detected and represented in the network with certain probability. The Particle Filtering method was proposed recently for time-varying network modelling in [36] and its success was demonstrated on computer vision data. Differing from [36], which tracks the topology of the network directly as a discrete sequence of graphs, we track the changes in the dependence of gene expression values of various genes over time, from which we infer also the network topology.

Thus, the motivation of this work is to model varying gene interactions over the life time of an organism or a biological process such as circadian cycles.

## 2 MEthoDs

### 2.1 Time Series Data Modelling

A great interest in various areas involving multivariate data such as signal processing, computational biology, finance, automation, etc. is to model and analyze the evolution of temporal sequences. Bayesian Networks are established tools for efficiently modelling multivariate data. A DBN (Dynamic Bayesian Network) is an extension of Bayesian network to temporal domain. In time domain conditional dependencies can be modelled between random variables within as well as across time epochs. The conditional distributions in DBN are assumed to be homogeneous, i.e., the structure and parameters of a network are maintained constant throughout the time. Taking this into account, a DBN is simply constructed by unwrapping a Bayesian network in time domain that causes significant simplification to the model learning procedure. At the same time, this assumption constrains the strength of DBN in modelling non-stationary sequences, where intrinsic relationships between different variables change in time [37]. These non-stationary sequences are present everywhere in common life, for example the gene interactions in different stages of a life
cycle. Obviously, usage of a stationary statistical model is insufficient for modeling gene expression data sequences at all time instances.

Learning a time varying network is not a trivial problem. One may try naively to learn a dynamically changing network independently for each time epoch. However, this is a complex task as there are very little available observations at one time epoch for most applications in real life. One way to overcome the problem of data scarcity is to divide temporal sequences into segments-stationary epochs, with an assumption that in each epoch data are generated from the same probability distribution. However, the lack of knowledge about models in each segment makes the problem more complex. Moreover, the solution space grows exponentially with the length of time sequence [36]. From another point of view, since observations are most often distorted by noise, statistics can be recovered from these modifications of signal.

To overcome all the difficulties mentioned above, one of the propositions is to expand DBN to nonstationary scenarios by introducing various additional conditions on the type of a network and how the network can change in time. The works done before have been mainly concentrated on nonstationary models with static structure. One of the most popular is the time-varying autoregression model (TVAR) [38]. TVAR is able to describe nonstationary linear dynamic systems, coefficients and noise variances which continuously change with time. In order to estimate recursively the regression parameters, normalized least squares algorithm can be used. And an error of estimation is shown to be bounded when the model parameters change smoothly [39]. TVAR modelling is widely used in the works related to gene expression data [40]. Extended TVAR models have also been developed for other time-varying processes, e.g., Poisson counting process [41] and non-Gaussian autoregression [42].

One of the tutorials on Bayesian network application to inference the interactions between genes is Friedman et al. paper [24]. The authors proposed a framework built on the use of Bayesian networks for describing statistical dependences between variables. The method was applied to the time series gene expression data of the S. cerevisiae cell-cycle measurements of Spellman et al. [7]. The proposed approach is quite different from the clustering approach used by [7], [43], [44], [45], in that it attempted to learn a richer structure from the data, even without use of any prior biological knowledge. However, in learning from time series data [7], the authors treated each measurement as an independent sample from a distribution, and did not assume the temporal aspect of the measurement. Thus, the complex network structure inferred from the experimental data and causal relationships, interactions between genes were "frozen", not varying in time.

### 2.2 Observation of Time Varying Networks

J. Khan et al. [30] derived the LASSO-Kalman smoother for the inference of time-varying genetic networks from a limited number of noisy observations. Their approach recursively computes the minimum mean-square sparse estimate of the network connectivity at each time point. To overcome the limited number of observations with respect to the size

of domain (small $n$ large $p$ problem) authors performed target tracking in a compressed domain. Chopping the timeseries sequence with gene expression values (experimental data were taken from [8]) into homogeneous subsequences they estimated 21 dynamic gene networks, one per three time points, during the life cycle of Drosophila Melanogaster.

Another application of LASSO-based least squares regression operation for description of the regulatory network together with a particle filter-based state estimation algorithm, which was used to capture the nonlinearity of the system, was proposed in an article of Noor et al. [26]. The parameters which characterize the regulatory relations between different genes were estimated online using Kalman filter. The parameter vector was expected to be sparse "since a particular gene interacts with a few other genes only, and as such, many of the system parameters modelling "weak" relationships are irrelevant" [26]. The authors used both synthetic and real biological data of Drosophila Melanogaster for learning steady state gene regulatory networks.

Young et al. [27] introduced a Bayesian Model Averaging method (ScanBMA) which is able to infer gene regulatory networks using time series data. Time series data generated from the DREAM competition [46] as well as experimental time series S. cerevisiae data were used for estimation of static network structures. Authors state that their method allows inference for networks of thousands of genes to be completed much faster respect to other competing methods.

Despite the fact that the methods for inference of steady state gene regulatory networks still prevail, there is a positive trend towards the study of dynamically changing relationships between genes in a network. And the method proposed in this paper is a step forward for solving this problem.

## 3 MODEL

A network is assumed to be consisting of $I$ genes. Genes are represented by nodes in the studied network, whereas the relationships among interacting genes are modelled by edges which connect the related nodes. Our aim is to model how the gene network structure evolves over time. We propose a multivariate linear regression model relating the expression value of each gene at a given time to the gene expression values of the previous time instant. Hence, the observation equation describes the gene expression values at a particular time epoch $t$ :

$$
\begin{aligned}
& x_{i, t}=a_{i 1, t} \cdot x_{1, t-1}+a_{i 2, t} \cdot x_{2, t-1}+\cdots+a_{i I, t} \cdot x_{I, t-1}+\eta_{t} \\
& i=1, \ldots, I ; \quad I-\text { total number of genes, }
\end{aligned}
$$

where $x_{i, t}$ denote set of observations for all genes in a network for each time epoch $t ; a_{i j, t}$ - coefficients of regression equation which model regulatory relations between gene $i$ and gene $j$ in consequent time epochs.

Unlike classical regression, this multivariate regression is a time-varying regression. The regression coefficients $a_{i j, t}$ are not constant and can be changing at each instant.

We also propose a parametric model to model the changes in the process coefficients. For simplicity, we assume a linear model for the time being, but it can be extended to nonlinear models:

$$
a_{i j, t}=a_{i j, t-1}+v_{t}
$$

More explicitly, equation (1) can be written in a vector form as:

$$
\left[\begin{array}{c}
x_{1, t} \\
x_{2, t} \\
\cdots \\
x_{I, t}
\end{array}\right]=\left[\begin{array}{cccc}
a_{11, t} & a_{12, t} & \cdots & a_{1 I, t} \\
a_{21, t} & a_{22, t} & \cdots & a_{2 I, t} \\
\vdots & \vdots & \ddots & \vdots \\
a_{I 1, t} & a_{I 2, t} & \cdots & a_{I I, t}
\end{array}\right]\left[\begin{array}{c}
x_{1, t-1} \\
x_{2, t-1} \\
\cdots \\
x_{I, t-1}
\end{array}\right]+\left[\begin{array}{c}
\eta_{1, t} \\
\eta_{2, t} \\
\cdots \\
\eta_{I, t}
\end{array}\right]
$$

In both equations (1) and (2) noise terms $\eta_{t}$ and $v_{t}$ can be of any distribution which can be decided depending on the nature of the data. In the simplest case, they can be assumed to be i.i.d. Gaussian such that $\eta_{t}^{(n)} \sim \mathcal{N}\left(0, \sigma_{\eta}^{2}\right)$ and $v_{t}^{(n)} \sim$ $\mathcal{N}\left(0, \sigma_{v}^{2}\right)$. However, data with outliers or impulsive noise might require a model with heavy-tailed distributions. In such cases, models such as Cauchy or alpha-stable [47] distribution are preferable as alternatives to Gaussian distribution over other heavy-tailed distributions due to satisfying a generalized version of the central limit theorem.

This is clearly a linear regression model and in the context of Bayesian networks reminds one of how partial correlations are calculated to estimate dependencies between nodes [48]. Although, similar to partial correlations, one tries to recover dependencies on all variables, there is a fundamental difference in this case, where the regression is made over gene expressions of the previous time instant. That is, we are trying to estimate a network which is not describing a given instant but how the gene expressions evolve overtime.

Hence, such a model (1) describes an inter-slice network structure and shows what relations exist between all genes in the network at the previous time epoch, $\left\{x_{1, t-1}, x_{2, t-1}\right.$, $\left.\ldots, x_{I, t-1}\right\}$, and the gene under consideration at the current time, $\left\{x_{i, t}\right\}$. That is, the network describes how a certain gene expression at the current time epoch is influenced by the expression level of other genes at the previous time epoch. The coefficients $a_{i j, t}$ approximate linearly the conditional dependence of the expression of the $i$ th gene at time $t$ on the expression of the $j$ th gene at time $t-1$. That is, $a_{i j, t} \approx f\left(x_{i, t} \mid x_{j, t-1}\right)$. An exact expression would involve also nonlinear dependence terms as well as dependencies on further past which are ignored in the current work.

## 4 Particle Filter or Sequential Monte Carlo

To construct the gene interaction network, we need to devise an iterative algorithm to solve for $a_{i j, t}$ 's. This is a classical problem in signal processing: to recover hidden (possibly time varying) model parameters from observations. Classical approaches to solve the problem include Kalman filtering which is a generalization of Wiener filtering, which finds the optimal linear estimate to recover original signal from noisy observations, to non-stationary data. We would like to address the problem in a Bayesian setup which would allow us also to utilize any prior information we might have and also let us reason in terms of probability distributions rather than single point estimates. This also

allows one to make error analysis and see the success of the modelling for a population of networks rather than a single case. To solve Eqs. (1) and (2) and estimate unknown time varying network parameters $a_{i j, t}$, we propose to utilize an influential Sequential Monte Carlo method namely Particle Filtering [51] which achieved important success in tracking problems in radar signal processing and computer vision.

The Particle Filtering method was applied recently to gene regulatory network inference by Noor et al. [26], who used this method for estimation of the states recursively using nonlinear state equations for the model; however, in their formulation the hidden states to be estimated are the gene expression values. The parameters $a_{i j, t}$ characterizing the regulatory relationships between genes were estimated applying Kalman filter on gene expression values. Then, they go on to reduce the solution space with LASSO-regularized least squares estimation to obtain the steady state network structure. Whereas in current work state equation describes the evolution of the parameters which characterize the regulatory relations among genes in a network and we use Particle Filtering method for direct inference of these parameters at each time epoch.

For many applications, it is very important to know the observation order of the data [49], [50]. In the case of nonstationary data, the probability density function (pdf) of the related parameter is changing with time. Thus, in nonstationary cases, the expectations and the pdf should be sequentially updated as the new data become available. With this aim, the dynamic systems usually can be described in terms of state-space equations:

$$
\begin{gathered}
\boldsymbol{a}_{t}=f_{t}\left(\boldsymbol{a}_{t-1}, v_{t}\right) \\
\boldsymbol{x}_{t}=h_{t}\left(\boldsymbol{a}_{t}, \eta_{t}\right)
\end{gathered}
$$

where $\boldsymbol{a}_{t}$ and $\boldsymbol{x}_{t}$ are related to the hidden variables and the observation vectors at actual time $t$, respectively. In this paper, we assume a linear regression model; however, we would like to note that Particle Filtering method can also accurately model any kinds of nonlinearities present in the state and observation equations. $v_{t}$ and $\eta_{t}$ are the process and observation noise terms, respectively, which are modelled as Gaussian or Laplace processes in this paper and their statistics are assumed to be known. The aim is to estimate sequentially the posterior distribution of unknown variables, the hidden state parameters $\boldsymbol{a}_{t}$, as a set of observations become available online, i.e., $p\left(\boldsymbol{a}_{0: t} \mid \boldsymbol{x}_{1: t}\right)$, where $\boldsymbol{a}_{0: t}=\left\{\boldsymbol{a}_{0}, \boldsymbol{a}_{1}, \ldots, \boldsymbol{a}_{t}\right\}$ and $\boldsymbol{x}_{1: t}=\left\{\boldsymbol{x}_{1}, \boldsymbol{x}_{2}, \ldots, \boldsymbol{x}_{t}\right\}$.

It is worth noting that proposed method is able to work online, i.e., in real-time. For a real time system, data processing should not be longer than data acquisition. In applications such as following, the gene interaction changes in a circadian cycle, where the data are sampled at 1-2 hour intervals, proposed method is definitely real-time. Even if the data were sampled in minute intervals the method is able to deal with it and process the data as they become available.

The posterior distribution of parameters $\boldsymbol{a}_{\boldsymbol{t}}$ is estimated at each time instant in two steps: first is prediction and sec-ond-update. In the first step, the value of the hidden parameter, $\boldsymbol{a}_{\boldsymbol{t}}$, at time $t$ is predicted from the previous time
instant $t-1$ according to the first order Markov process (4) $p\left(\boldsymbol{a}_{t} \mid \boldsymbol{a}_{t-1}\right)$ [51]. At time instant $t$, the predicted parameter is updated via Bayes rule as an observation $\boldsymbol{x}_{t}$ becomes available as follows:

$$
p\left(\boldsymbol{a}_{t} \mid \boldsymbol{x}_{1: t}\right)=\frac{p\left(\boldsymbol{x}_{t} \mid \boldsymbol{a}_{t}\right) p\left(\boldsymbol{a}_{t} \mid \boldsymbol{x}_{1: t-1}\right)}{p\left(\boldsymbol{x}_{t} \mid \boldsymbol{x}_{1: t-1}\right)}
$$

where, assuming a Gaussian observation noise, $p\left(\boldsymbol{x}_{t} \mid \boldsymbol{a}_{t}\right)$ is given by

$$
p\left(x_{t} \mid a_{t}\right)=\frac{1}{\left(2 \pi \sigma_{\eta}^{2}\right)^{1 / 2}} \exp \left(-\frac{\left(x_{t}^{o b s}-x_{t}\right)^{2}}{2 \sigma_{\eta}^{2}}\right)
$$

The relation (6) gives the optimal Bayesian solution. In general, this recursive solution cannot be determined analytically [49]. Particle filtering provides a stochastic recursive algorithm for the solution of Eqs. (4) and (5).

It employs a sampling scheme rather than analytically or numerically evaluating associated probability densities. In particular, it represents pdfs with a summation over Dirac functions located at samples as in a histogram.

Thus, the idea of sequential Monte Carlo method is to form a finite set of $N$ weighted state samples, called particles, which approximates the posterior distribution [49]:

$$
p\left(\boldsymbol{a}_{t} \mid \boldsymbol{x}_{1: t}\right) \approx \sum_{n=1}^{N} w_{t}^{(n)} \delta\left(\boldsymbol{a}_{t}-\boldsymbol{a}_{t}^{(n)}\right)
$$

where $\delta$ denotes the delta-Dirac function, $w_{t}^{(n)}$ are the weights or the counts of the samples appearing at value $\boldsymbol{a}_{t}^{(n)}$.

When number of particles, $N$, goes to infinity, the approximation approaches the exact solution, true distribution. Briefly, at each time epoch $t$ the filtering starts with the sample set $\left\{\boldsymbol{a}_{t-1}^{(n)}, w_{t-1}^{(n)}\right\}_{n=1 \ldots N}$ related to the previous time epoch. Due to the lack of an exact of knowledge of the underlying distribution, it is in general difficult to sample from the actual distribution $p\left(\boldsymbol{a}_{t} \mid \boldsymbol{x}_{1: t}\right)$, therefore the samples are generated from a proposal or importance function $q$ which approximates the real pdf in some sense:

$$
\boldsymbol{a}_{t}^{(n)} \sim q\left(\boldsymbol{a}_{t} \mid \boldsymbol{a}_{t-1}^{(n)}, \boldsymbol{x}_{t}\right)
$$

In this case, one should take care of the samples coming from $q$ but not belonging to $p$. The care is taken by the correction factor $p / q$, that is $w_{t}^{(n)} \propto p\left(\boldsymbol{a}_{t} \mid \boldsymbol{x}_{1: t}\right) / q\left(\boldsymbol{a}_{t} \mid \boldsymbol{a}_{t-1}^{(n)}, \boldsymbol{x}_{t}\right)$ [51].

Sampling from $q\left(\boldsymbol{a}_{t} \mid \boldsymbol{a}_{t-1}^{(n)}, \boldsymbol{x}_{t}\right)$ to approximate posterior $p\left(\boldsymbol{a}_{0: t} \mid \boldsymbol{x}_{1: t}\right)$ and updating with the correction factor $p / q$ as shown above, is known as the "sequential importance sampling" method [49]. It can be shown that importance sampling is a variance reduction approximation method and hence is preferable to other sampling methods such as rejection sampling since it needs less amount of samples to approximate the target distribution.

When new samples $\boldsymbol{a}_{t}^{(n)}$ are obtained, we estimate the likelihood of each of the particle using the observation model. It can be shown (see [51] for details) that the weight updates can be turned into a sequential update avoiding recalculation from scratch for every new data sample. Hence, the weights are updated sequentially by

$$
w_{t}^{(n)} \propto w_{t-1}^{(n)} \frac{p\left(\boldsymbol{x}_{t} \mid \boldsymbol{a}_{t}^{(n)}\right) p\left(\boldsymbol{a}_{t}^{(n)} \mid \boldsymbol{a}_{t-1}^{(n)}\right)}{q\left(\boldsymbol{a}_{t}^{(n)} \mid \boldsymbol{a}_{t-1}^{(n)}, \boldsymbol{x}_{t}\right)}
$$

Choosing a good proposal density $q\left(\boldsymbol{a}_{t} \mid \boldsymbol{a}_{t-1}, \boldsymbol{x}_{t}\right)$ is crucial for the efficiency of the particle filter. State transition distribution $p\left(\boldsymbol{a}_{t} \mid \boldsymbol{a}_{t-1}\right)$ is a convenient choice for proposal distribution and reduces weight update in Eq. (10) into trivial accumulation of likelihoods as shown below:

$$
w_{t}^{(n)} \propto w_{t-1}^{(n)} \cdot p\left(\boldsymbol{x}_{t} \mid \boldsymbol{a}_{t}^{(n)}\right)
$$

Due to its simplicity, this is the most popular proposal distribution in the literature. After this step, the importance weights are normalized to form a proper probability distribution [49]:

$$
\tilde{w}_{t}^{(n)}=\frac{w_{t}^{(n)}}{\sum_{n=1}^{N} w_{t}^{(n)}}
$$

The resultant sample set $\left\{\boldsymbol{a}_{t}^{(n)}, w_{t}^{(n)}\right\}_{n=1 \ldots N}$ can give estimations for the posterior distribution of current data and information about network structure.

## Algorithm. Time-Varying Network Learning

1. Input gene expression time series data $x_{i, 1: t}^{\text {obs }}$.
2. Initialization of all parameters.
3. for $\mathrm{n}=1, \ldots, \mathrm{~N}$ do
4. Generating particles for $a_{i j, t=0}^{(n)}$ from $p\left(a_{i j, t=0} \mid x_{t=0}\right)$.
5. Assigning equal weights to the particles.
6. end for
7. for $\mathrm{t}=1, \ldots, \mathrm{~T}$
8. for $\mathrm{n}=1, \ldots, \mathrm{~N}$
9. Prediction of $a_{i j, t}^{(n)}$ from $q\left(\boldsymbol{a}_{t} \mid \boldsymbol{a}_{t-1}^{(n)}, \boldsymbol{x}_{t}\right)$.
10. Prediction of $x_{i, t}$ using (1), $a_{i j, t}^{(n)}$ and observations of $x_{i, t-1}^{\text {obs }}$.
11. Update the weights of each particle using (11).
12. end for
13. Normalization of the weights, (12).
14. Resampling, if necessary, (13).
15. Set of $\left\{\boldsymbol{a}_{i j, t}^{(n)}, w_{t}^{(n)}\right\}_{n=1 \ldots N}$ is used for the next time epoch, step 7 .
16. end for.

However, a problem known as "degeneracy" rises when one uses the sequential Monte-Carlo algorithm. It occurs when the dimension of the state space is high: after few iterations, most of the samples drawn from the state transition distribution may have very small weights. In such situations sampling efficiency should be increased by performing resampling [49], [50]. The number of effective particles $N_{\text {eff }}$ is a measure of the degeneracy and can be calculated by

$$
N_{e f f}=\frac{1}{\sum_{n=1}^{N}\left(w_{t}^{(n)}\right)^{2}}
$$

When $N_{\text {eff }}$ is below a certain threshold value, the resampling should be performed: samples with low importance weights are eliminated, and those with high importance
![img-0.jpeg](img-0.jpeg)

Fig. 1. A regulatory network of S. cerevisiae used for synthetic data generation in this work (reproduced from [27]).
weights are allocated to obtain $n$ equally weighted samples of $a_{t}^{(n)}$.

The algorithm used for inferring the network parameters from Eqs. (1) and (2) is displayed below.

## 5 ReSults and DisCussion

### 5.1 Synthetic Data

The proposed algorithm was tested on time-series simulated data from the DREAM competition [46]. Data were generated from known transcriptional regulatory networks of S. cerevisiae using GeneNetWeaver 3.1.1 Beta (GNW) software [52]. Gene networks were modeled by a system of ordinary differential equations describing the dynamics of the mRNA concentration and the protein concentration of every gene. Time-series experiments were simulated by integrating the networks using different initial conditions. Both transcription and translation are modelled. To model internal noise in the dynamics of the networks the simulations are based on stochastic differential equations (Langevin equations). In addition, measurement noise was added to the generated gene expression datasets. Existing model of noise observed in microarrays, which is very similar to a mix of normal and lognormal noise, was also used [46], [53].

Each time series has 201 time points. The network structure used for synthetic simulation is shown in Fig. 1. Fig. 2 shows generated time series for each gene (201 time points) and how expression levels respond to a perturbation. Perturbation was simulated by slightly increasing or decreasing the basal activation of all genes of the network simultaneously by different random amounts [46]. It was applied to the data at $t=0$ and removed at $t=100$. The first half of the time series (until $t=100$ ) shows the response of the network to the perturbation. The second half of the time series (until $t=201$ ) shows how the gene expression levels go back from the perturbed to the steady-state levels.

As discussed before, the idea is to dynamically estimate unknown regulatory coefficients $\boldsymbol{a}_{i j, t}$ using particle filtering method. Careful estimation of $a_{i j, t}$ allows us to highlight the main gene interactions in the network. The number of particles used is $N=300$. The variance of the noise in the state update equation (1), $v_{t}$, is taken to be $10^{-2}$ and the variance of measurement noise is assumed to be known and constant, $\sigma_{q}^{2}=10^{-3}$.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Time evolution of gene expression data for 10 genes undergone a perturbation at $t<100$.

It is important to specify a certain threshold in order to estimate the strongest relations between genes. Threshold is estimated using the level of dispersion around the average of $a_{i j, t}$ (mean) at particular time epoch: For each time epoch both mean and standard deviation (std) of estimated $a_{i j, t}$ are calculated. Thus, values of $a_{i j, t}$ above a threshold (mean + std) indicate that gene $i$ activates gene $j$, and values below the threshold (mean - std) are considered as repression activity of gene $j$ in relation to gene $i$. The parameters $a_{i j, t}$ whose values are between two limit thresholds indicate an absence of relations or weak relations among the genes, and they are not considered in further analysis. The choice of threshold is rather arbitrary and should be chosen according to the biological problem at hand.

### 5.2 Modeling Results

Results for gene expression estimation by Particle filter are shown in Fig. 3 for a two genes network. It is clearly observed that the proposed model, Eqs. (1) and (2), makes a good enough estimation of the gene expression data. Moreover, the use of particle filter allows us to follow with high accuracy all changes in gene expression data undergone due to different external perturbations. Residuals of the estimated gene expression values with respect to the synthetic ones are shown in Fig. 4.
![img-2.jpeg](img-2.jpeg)

Fig. 3. Comparison of Particle Filter estimation (red dashed lines) with true synthetic gene expression data (blue solid lines) for two genes.

As it was discussed above the idea is not only to predict and follow expression level changes in a gene network, but also to estimate the posterior distributions of $a_{i j, t}$ coefficients which model the relations between genes in time. The relations in a network consisting of two genes are described by four coefficients - $\left\{a_{11}, a_{12}, a_{21}, a_{22}\right\}$. Coefficients $a_{11}$ and $a_{22}$, autocorrelation terms, are related to auto-regulation of a gene in adjacent time epochs; $a_{12}$ and $a_{21}$ - cross-correlation terms, which show how expression level of one gene at the time epoch $(t-1)$ effects on expression level of other gene at time $t$.

Since the results obtained are stochastic and can fluctuate slightly from realization to realization we launched the algorithm for a number of runs and calculated average values of regulatory coefficients over all runs for each time epoch.

Histograms for the distributions of the estimated network coefficients $a_{i j, T}$ at the final time epoch $(t=201)$ are shown in Fig. 5. After running the algorithm 100 times the average values of $a_{i j, T}$ over all runs at the final time epoch were calculated. Running the algorithm even 1,000 times does not change significantly the final estimates: histograms become more refined, meanwhile the average values and variance remain almost the same (see Fig. 6 and Table 1).
![img-3.jpeg](img-3.jpeg)

Fig. 4. Residuals between synthetic gene expression data, $x_{\text {sdo }}$, and estimated by Particle Filter, $x_{\text {est }}$, for two genes.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Histograms for distributions of the inferred $a_{i j, T}$ coefficients for two genes network at the final time epoch averaged using 100 runs. Vertical axis is the number of particles with certain value, and horizontal axis is the values of $a_{i j, T}$.
![img-5.jpeg](img-5.jpeg)

Fig. 6. Histograms for distributions of the inferred $a_{i j, T}$ coefficients for two genes network at the final time epoch averaged using 1,000 runs. Vertical axis is the number of particles with certain value, and horizontal axis is the values of $a_{i j, T}$.

TABLE 1
Average Values of $a_{i j, T}$ Coefficients and Their Variance Estimated for $N$ Runs


Time dependence of the estimated coefficients $a_{i j, t}$ is shown in Fig. 7. It can be seen that at the beginning, inferred values are scattered and after some time $(\mathrm{t} \approx 10)$ they become more stable smoothly changing with time with some insignificant fluctuations. Also in Fig. 7 we can observe an effect of removal of the perturbation, at times exceeding 100 some regulatory coefficients $\left(a_{12}, a_{21}\right.$, and $\left.a_{22}\right)$ simultaneously slightly change their values.

After successful gene expression data tracking and estimation of coefficients $a_{i j, t}$, we would like to understand how they reflect the relations between genes. Unfortunately, there is still no certain interpretation for the coefficients which model the relationships in gene regulatory networks.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Time dependence of coefficients $a_{i j, t}$ averaged using 100 runs for two genes.
![img-7.jpeg](img-7.jpeg)
(a)
![img-8.jpeg](img-8.jpeg)
(b)

Fig. 8. Possible time-varying network structure consisting of two genes. Figures $a$ and $b$ show different representations of the same time-varying network: $a$ - all genes are shown for each time epoch and arrows indicate activities from one time epoch to another; $b$ - genes are shown only once and all arrows directed from gene at time $t-1$ to the gene at current time epoch. In both figures, red and blue arrows indicate expression and repression activity at adjacent time epochs, respectively; red, blue and black colors of nodes indicate self-expression, self-repression, and no expression of a gene in adjacent time epochs ( $t=200$ and $t=201$ ), respectively. The representation $b$ will be used further in this work.

Some authors [26] suggest that positive value of $a_{i j, t}$ above certain threshold indicates that gene $i$ activates gene $j$, whereas negative values show repression activity. However, these authors use different models and methods from ours for inferring gene networks. The statistical interpretation we give is that the coefficients approximate the conditional probabilities: $a_{i j, t} \approx f\left(x_{i, t} \mid x_{j, t-1}\right)$.

In our case for two-gene network, coefficients averaged over all runs at the last time epoch $(t=201)$ are $\left\{a_{11}=0.620 ; a_{12}=1.629 ; a_{21}=0.152 ; a_{22}=-0.334\right\}$. If we assume, as was discussed above, that the threshold would be the mean value of all four coefficients ( $\approx 0.52$ ) plus/ minus standard deviation ( $\approx 0.84$ ) we get upper threshold value $\approx 1.36$ and lower $\approx-0.32$, and take into account the values above and below that threshold, only $a_{12}$ and $a_{22}$ remains. This can suggest that in our two gene network gene G2 at time epoch $t=200$ expresses gene G1 at $t=201$, and gene G2 at time epoch $t=200$ represses itself at $t=201$. Graphically the network can be shown as in Fig. 8.

In order not to cause confusion we would like to make distinction between two modes of averaging. Since multiple runs are performed, the mean values of regulatory coefficients are estimated first over all runs for each time epoch, that is, we do ensemble averaging over realizations. Then, we calculate mean and standard deviation for each time

![img-9.jpeg](img-9.jpeg)

Fig. 9. Comparison of Particle Filter estimation (red dashed lines) with synthetic gene expression data (blue solid lines) for 10 genes that have undergone a perturbation at *t* < 100.

instant over such calculated ensemble averages of **a**_{ij,t}. Next, from these means and standard deviation values we calculate a threshold at each time epoch, which is used for the estimation of network structure, as described above.

Extending our analysis to a gene network consisting of 10 genes, we again observe very good results of data tracking by particle filter: excellent agreement between synthetic gene expression data and PF estimates (see Fig. 9).

The time dependence of learned coefficients **a**_{ij,t} for 10 genes network is not shown here due to overlapping of 100 coefficients on each other that does not give clear picture of what is happening with time. However, histograms for the distributions of the estimated network coefficients **a**_{ij,t} at the final time epoch and their averaged values for 100 runs of the algorithm are shown in Fig. 10 and Table 2, respectively, together with the standard deviation. The standard deviation in Table 2 shows an amount of dispersion of a set of regulatory coefficients values **a**_{ij,T} in the network estimated for the last time epoch.

Possible gene network results for the final time epoch are shown in Fig. 11. An animated time-varying network structure across all time epochs is available as supplemental material (Fig. S1), which can be found on the Computer Society Digital Library at http://doi.ieeecomputersociety.

org/10.1109/TCBB.2015.2496301. Red arrows in Fig. 11 indicate the expression activities of a gene where an arrow starts at time epoch *t* = 200 in relation to another gene where an arrow points at time epoch *t* = 201. On the other hand blue arrows show the repression activities of a gene where an arrow starts at time epoch *t* = 200 in relation to another gene where an arrow points at time epoch *t* = 201. Red, blue and black colors of the nodes indicate self-expression, self-repression and no expression of a gene in adjacent time epochs (*t* = 200 and *t* = 201), respectively.

Next, in order to get smoother network changes with time we adopted a Laplace prior instead of Gaussian. Moreover, to investigate the sparsity of the network we introduced a new proposal function *q*(*a*<sub>*t*</sub>|*a*<sub>*t*<sub>*i*−1*</sub></sub>, *x*<sub>*t*</sub>) = *p*(*a*<sub>*t*</sub><sup>(*n*)</sup>|*a*<sub>*t*<sub>*i*−1*</sub></sup>*)/p*(*a*<sub>*t*</sub><sup>(*n*)</sup>), which includes a Laplace prior in addition to the state transition prior.

After introduction of the new proposal function the weight update equation (Eq. 11) becomes:

$$w_i^{(n)} \propto w_{t-1}^{(n)} \cdot p\left(\mathbf{x}_t \mid \mathbf{a}_t^{(n)}\right) \cdot p\left(\mathbf{a}_t^{(n)}\right). \tag{14}$$

The Laplace prior introduces regularization with an *l*<sub>1</sub>-norm metric as in the case of LASSO. In other words, LASSO is the limit case of the Laplace prior in the Bayes framework, which gives us much more flexibility in model testing and error analysis when compared to LASSO. Moreover, another difference and advantage to the way LASSO was applied in [26] is that the regularization is applied within the time series at each time instant rather than being applied separately after particle filtering is performed. That is, in the current algorithm the effect of LASSO is integrated in the learning process by sequential Monte Carlo.

The resulting network structure using Laplace prior for the final time epoch is shown in Fig. 12. An animated time-varying network structure across all time epochs is available as supplemental material (Fig. S2), available online.

Comparing the networks, the original (Fig. 1) and the reconstructed ones (Figs. 11 and 12), care must be taken since

![img-10.jpeg](img-10.jpeg)

Fig. 10. Histograms for distributions of the inferred **a**_{ij,T} coefficients for 10 genes network at the final time epoch averaged using 100 runs. Vertical axis is the number of particles with certain value, and horizontal axis is the values of **a**_{ij,T}.

TABLE 2 Mean Values of $\boldsymbol{a}_{i j, T}$ Coefficients for 10 Genes Network at the Final Time Epoch Averaged Using 100 Runs Together with Standard Deviation


the original network shows static structure for the whole time period while the inferred network indicates a dynamic case: relations between genes at two adjacent time epochs (between time instants, not at a particular time). From Figs. S1 and S2 it can be observed that for the case with the new proposal function the network structure changes smoothly, less fluctuations of regulatory coefficients are observed with time. The smoothness can be increased even more by fixing the scale parameter of the Laplace prior. Sparsity can be improved with clever choice of the thresholds which need to be chosen according to the biological constraints.

Moreover, fluctuations present in the time varying network are influenced by the magnitude of noise added after the simulation to the generated gene expression data in [52]. Analysis has shown that for high noise magnitude (one order higher than by default) the network inference drops since the signal (gene expression) amplitude is less than the amplitude of added noise which brings to a network structure which has nothing to do with that original shown in Fig. 1. Whereas very small noise magnitude (one order less than by default) causes numerical problems in particle filtering algorithm since this method does not work with

![img-11.jpeg](img-11.jpeg)

Fig. 11. A snapshot of time-varying network structure with 10 genes obtained using Gaussian prior. The network is reconstructed for $t=201$ after 100 runs. Red and blue arrows indicate expression and repression activities at adjacent time epochs, respectively; red, blue, and black colors of nodes indicate self-expression, self-repression, and no expression of a gene in adjacent time epochs ( $t=200$ and $t=201$ ), respectively. nearly noise-free models. For the given level of noise and carefully chosen thresholds, the obtained recall and precision values are similar to the results given in [27].

In comparison to the network estimation methods discussed in [27], our method has the important difference of being able to follow changes in the network structure. It is also important to note that the threshold value selection effects the level of sparsity very significantly that in its turn effects on the final precision of the reconstructed network.

Summarizing, the proposed PF method successfully tracks time series of gene expression data, infers online time varying hidden parameters which are regulatory coefficients in a gene network. Introduction of the new proposal function with Laplace prior leads to stable and smoother network changes.

Further important problems that will be investigated in future are adaptation of the code to large-scale time varying gene networks, analysis of the gene network sparsity, and application of our method to real gene expression data which are changing with time.

## 6 CONCLUSION

We demonstrated the potentials of a sequential Monte Carlo method, namely particle filtering method, to synthetic gene

![img-12.jpeg](img-12.jpeg)

Fig. 12. A snapshot of time-varying network structure with 10 genes obtained using Laplace prior. Specification of the figure is the same as in Fig. 11.

expression time series dataset for a network of genes in tracking with high accuracy the changes in gene expression data undergone due to different external perturbations. Gene expression temporal sequence data were utilized for online learning of time varying gene network structure. The proposed model is capable of discovering causal relationships, interactions between genes that vary in time. The method can be extended also to modelling other time-varying biological networks.

## ACKNOWLEDGMENTS

This work was funded by the CNR Flagship project InterOmics. Ercan E. Kuruoğlu gratefully acknowledges partial support from Alexander von Humboldt Foundation in the form of an Experienced Research Fellowship which made his stay in the Max Planck Institute possible. The authors acknowledge the Dream Project organizing team and GNW software developers, in particular Dr. Thomas Schaffter.

## $\triangleright$ For more information on this or any other computing topic, please visit our Digital Library at www.computer.org/publications/dlib.