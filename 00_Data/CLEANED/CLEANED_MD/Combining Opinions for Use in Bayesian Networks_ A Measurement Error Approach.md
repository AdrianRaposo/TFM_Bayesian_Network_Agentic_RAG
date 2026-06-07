# QUT 

## Queensland University of Technology

Brisbane Australia

This may be the author's version of a work that was submitted/accepted for publication in the following source:

Charisse Farr, A., Mengersen, Kerrie, Ruggeri, Fabrizio, Simpson, Daniel, Wu, Paul, \& Yarlagadda, Prasad
(2020)

Combining Opinions for Use in Bayesian Networks: A Measurement Error Approach.
International Statistical Review, 88(2), pp. 335-353.
This file was downloaded from: https://eprints.qut.edu.au/199173/

## © 2019 The Authors. International Statistical Review

This work is covered by copyright. Unless the document is being made available under a Creative Commons Licence, you must assume that re-use is limited to personal use and that permission from the copyright owner must be obtained for all other uses. If the document is available under a Creative Commons License (or other specified license) then refer to the Licence for details of permitted re-use. It is a condition of access that users recognise and abide by the legal requirements associated with these rights. If you believe that this work infringes copyright please provide details by email to qut.copyright@qut.edu.au

License: Creative Commons: Attribution-Noncommercial 4.0

Notice: Please note that this document may not be the Version of Record (i.e. published version) of the work. Author manuscript versions (as Submitted for peer review or as Accepted for publication after peer review) can be identified by an absence of publisher branding and/or typeset appearance. If there is any doubt, please refer to the published source.
https://doi.org/10.1111/insr. 12350

# Combining opinions for use in Bayesian Networks: 

## a Measurement Error Approach

A.C. Farr ${ }^{1}$, K.L. Mengersen ${ }^{1}$, F. Ruggeri ${ }^{1,2}$, D.P. Simpson ${ }^{3}$, P. Wu ${ }^{1}$, P. Yarlagadda ${ }^{1}$

May 17, 2019

${ }^{1}$ Science and Engineering Faculty, Mathematical Sciences, Queensland University
of Technology, Brisbane, Australia
${ }^{2}$ Consiglio Nazionale delle Ricerche, Istituto di Matematica Applicata e
Tecnologie Informatiche, Milano, Italy
${ }^{3}$ University of Toronto, Canada


#### Abstract

Bayesian networks (BNs) are graphical probabilistic models used for reasoning under uncertainty. These models are becoming increasingly popular in a range of fields including engineering, ecology, computational biology, medical diagnosis, and forensics. In most of these cases, the BNs are quantified using information from experts, or from users' opinions. While this quantification is straightforward for one expert, there is still debate about how to represent opinions from mul- This is the author manuscript accepted for publication and has undergone full peer review but tiple experts in a BN. This paper proposes the use of a measurement has not been through the copyediting, typesetting, pagination and proofreading process, which may lead to differences between this version and the Version of Record. Please cite this article as doi: $10.1111 /$ insr. 12350

error model to achieve this. The proposed model addresses the issues associated with current methods of combining opinions such as the absence of a coherent probability model, the loss of the conditional independence structure of the BN, and the provision of only a point estimate for the consensus. The proposed model is applied to a subnetwork (the three final nodes) of a larger BN about wayfinding in airports. It is shown that the approach performs well when compared to existing methods of combining opinions.

Keywords: Bayesian networks; measurement error model; wayfinding; expert opinions.

# 1 Introduction 

Bayesian networks (BNs) have become a ubiquitous statistical tool for describing complex systems. A typical BN is based on a directed acyclic graphical (DAG) model in which variables are represented as nodes and probabilistically linked by a set of directed arcs. BNs are growing in popularity in engineering (Trucco et al., 2008), ecology (Johnson, 2009), natural resource management (Pollino et al., 2007), computational biology (Friedman et al., 2000), medical diagnosis (Heckerman, 1990) and forensics (Taroni et al., 2004). The application of BNs has also had an impact on their methodological aspects, raising various issues that still need to be addressed adequately. One of them is the way in which information from multiple experts, possibly

with different opinions and levels of expertise, can be represented in a BN.

Common ways of addressing this issue include consensus building approaches such as the Delphi method (Dalkey \& Helmer, 1963), averaging using the arithmetic mean (Beliakov et al., 2007; Burgman et al., 2011) or linear pooling (Cooke, 2008; French, 2011; Genest \& Zidek, 1986), and Bayesian approaches (French, 1985; Lindley, 1983; West, 1988; Winkler, 1968). These are briefly discussed in Section 4.

In this paper, a BN is represented as a directed acyclic graph (DAG) and the probabilities attributed to each node in the BN by each expert are assumed to be observations of the underlying true probabilities, subject to measurement error. The paper provides a review of measurement error models in the context of generalized linear random effects models and proposes their use in representing the systemic variation in the probabilities assigned by the experts. The novel use of measurement error models to combine expert opinions in BNs is the major contribution of the paper. Compared with linear pooling, the proposed model has the advantage of following from a coherent probability model and allowing for uncertainty, since the resulting distribution is more informative than a point estimate.

The conditional dependencies imposed by the BN are reflected in the associated precision matrices. The approach is then applied to a key subnetwork of a wayfinding Bayesian Network model (WBNM) (Farr et al., 2014) that was developed to investigate the factors that influence effective

wayfinding in airports. Previous wayfinding research has been split into two distinct streams: research that investigated human factors such as cognition to define issues such as cognitive mapping, information processing, memory and spatial recognition (Gärling et al., 1984; Kuipers, 1978; Passini, 1981, 1984; Peponis et al., 1990; Timpf et al., 1992), and research that used environmental factors to present mathematical measures such as the Visibility Index (VI) (Braaksma et al., 1980; Dada \& Wirasinghe, 1999; Tosic \& Babic, 1984) and the inter-connection density (ICD) (O'Neill, 1991). The WBNM combines these previously separate sets of factors into a single model via a BN. Given their relevance, we have decided to concentrate on the final nodes of those two streams and their influence on wayfinding. Therefore, we apply the measurement error model to the subnetwork that relates the final three nodes of the WBNM, i.e., Human Factors, Environmental Factors and Wayfinding. The WBNM has been chosen since it is a real case study, with a significant number of experts providing their opinions, whereas the decision of concentrating on the three final nodes is justified not only by computational constraints which would hinder how the proposed method works if a larger number of nodes were used but also by the possibility of getting extra insights about the influence of human and environmental factors on wayfinding. The structure of the WBNM was fixed in earlier studies and not questioned by the experts: the combination of experts' opinion on structuring a BN is a very complex problem, well beyond the scope of the

current paper.

The paper is structured as follows. In order to motivate the problem, the wayfinding case study and the WBNM model are described in Section 2. In Section 3 the basic properties of DAGs and BNs are presented, and existing methods for combining information in BN are described in Section 4. Measurement error and generalized linear models are presented in Sections 5 and 6 , respectively. The proposed model is described in Section 7, illustrated for a three node BN in Section 8 and applied to the WBNM subnetwork for the wayfinding case study in Section 9. Finally, additional comments and pointers for future research are discussed in Section 10.

# 2 Case Study - The Wayfinding Bayesian Network 

## Model

Wayfinding is the 'process of finding your way to a destination in a familiar or unfamiliar setting using cues given by the environment' (Farr et al., 2012). It requires the successful interplay between human and environmental factors. Previous research on wayfinding has investigated this process from one of two perspectives, namely either human or environmental factors. Studies of human factors have investigated issues such as memory, cognitive mapping, spatial recognition, and information processing (Gärling et al., 1984; Kuipers, 1978; Passini, 1981). Studies of environment factors

have focused on measures related to the wayfinding process. For example, the Visibility Index gives a measure of the ease of wayfinding to the value of available sight lines in an environment (Braaksma et al., 1980; Dada \& Wirasinghe, 1999; Tosic \& Babic, 1984) and the Inter-Connection Density measures the complexity of a floor plan (O'Neill, 1991). The Wayfinding Bayesian Network model (WBNM) (Farr et al., 2014) combined both the human and environmental aspects into one BN model and investigated the joint influence of these factors on effective wayfinding in airports.

The model was developed via focus groups composed of a multi-disciplinary team with differing levels of air travel and airport experience, a review of the wayfinding research (Farr et al., 2012), and from feedback from an audience of airport operators and BN modelers (Farr et al., 2014). It was quantified using a combination of data obtained from a focus group using the Delphi method (Landeta, 2006), literature on wayfinding, and an online survey. This survey was re-released to obtain more participants for this study and the results from the 99 respondents were used (their values are provided in the Appendix). The WBNM, shown in Figure 1, is comprised of five interconnected subnetworks, but we will concentrate just on three of them: one (pink) that includes the human factors, one (light blue) the environmental factors and one (orange) that connects these two subnetworks to the target node representing the probability of effective wayfinding. The full network comprises 49 nodes and 58 connections. The analysis described in this pa-

per focuses on the subnetwork comprising the three primary nodes, namely Human Factors, Environmental Factors and Wayfinding.

# 3 Bayesian Networks 

A Bayesian Network (BN) is a graphical representation of the joint probability distributions of a set of variables (Pearl, 1985, 1986), and is used for reasoning under uncertainty. A BN represents variables of interest as nodes and the dependencies between the variables as arcs. The variables underlying the nodes of the BN can be continuous, ordered or categorical, or alternatively continuous variables can be discretised to allow for ease of elicitation and computation (Korb \& Nicholson, 2010). Examples of common discrete nodes are Boolean, ordered values, integer values and ranges of values. The number of categories is usually chosen in light of the context, desired inferences, available information and computational complexity. For example, all of the nodes in the WBNM are binary, as described in (Farr et al., 2014).

A BN with binary nodes is depicted in Figure 2. It is immediately obvious that this representation is equivalent to a directed acyclic graph (DAG), comprised of nodes representing the variables of interest, arcs which show the direct influences between these variables, prior probability tables for the nodes that have no parents, and conditional probability tables (CPTs) for the other nodes (Valtorta \& Huang, 2008), like in Figure 2 (c).

![img-0.jpeg](img-0.jpeg)

Figure 1: The Wayfinding Bayesian Network model (WBNM), comprising three interconnected subnetworks (top) which expand to a full model (bottom) (Farr et al., 2014).

More precisely, for a directed acyclic graph given by $\mathcal{G}=(\mathrm{V}, \mathrm{E})$, where V is the set of nodes and E is the set of directed links between nodes, a joint probability distribution $\mathrm{P}\left(\mathbf{X}_{\mathrm{V}}\right)$ over the set of variables $\mathbf{X}_{\mathrm{V}}$ can be factorised as

$$
\mathrm{P}\left(\mathbf{X}_{\mathrm{V}}\right)=\prod_{v \in \mathrm{~V}} \mathrm{P}\left(\mathbf{X}_{\mathrm{V}} \mid \mathbf{X}_{\mathrm{pa}(v)}\right)
$$

where $\mathbf{X}_{\mathrm{pa}(v)}$ is the set of parent variables of variable $\mathbf{X}_{\mathrm{V}}$ for each node $v \in \mathrm{~V}$. This provides the defining property of a BN, i.e. the joint distribution of a node is conditioned only on the parents of that node.

For the network shown in Figure 2(a) with the states listed in Figure 2(b), the joint probability table given by $\mathrm{P}(A, B, C, D)$ would have $2^{4}=16$ entries. However, the constraints implied by the conditional independence structure in Figure 2(a) lead to $\mathrm{P}(A, B, C, D)=\mathrm{P}(A) \mathrm{P}(B) \mathrm{P}(C \mid A, B) \mathrm{P}(D \mid B, C)$, which only contains $1+1+4+4=10$ parameters.

Some terminology used in the BN literature and illustrated in Figure 2(a) is as follows (Korb \& Nicholson, 2010). First, a node is a parent of a child if an arc goes from the former to the latter; for example, nodes A and B are the parents of C and nodes C and D are the children of B. Second, if a directed chain of nodes exists, one node is an ancestor of another if it appears earlier in the chain, and it is a descendant of another if it comes later in the chain; for example, node D is a descendant of A. Third, a node without parents is a root node, for example node A. Finally, a node without children is a leaf node, for example node D.

![img-1.jpeg](img-1.jpeg)


(c)

Figure 2: (a) A sample Bayesian Network, with 4 nodes of interest, (b) the states of each of the variables, and (c) the underlying conditional probability table for node $C$, given nodes $A$ and $B$.

The BN representation also allows for a reduction in the time needed to compute the marginal probabilities, which is the most common operation undertaken on a BN (Pearl, 1986; Valtorta \& Huang, 2008). When new knowledge is obtained, beliefs are updated in a straightforward manner (Lauritzen \& Richardson, 2002). Software such as Hugin (www.hugin.com), GeNIe \& SMILE (www.bayesfusion.com), and Netica (www.norsys.com/netica.html) are able to perform these updates in an efficient manner.

# 4 Current Approaches for Combining Information in Bayesian Networks 

Using opinions from multiple sources or experts to parameterise a BN is standard practice, particularly in situations where data are not available. This however raises the problem of how these opinions should be combined and used in a BN. Linear pooling (McConway, 1981) is a common way of combining the probabilities obtained from multiple experts or sources. The probability of an event $X$, say, is approximated by averaging $n$ conditional probabilities $P\left(X \mid \mathbf{E}_{i}\right)=P_{i}(X)$, provided by different sources of information or experts $\mathbf{E}_{i}, 1=1, \ldots, n$, without knowing the joint model given by $P\left(P\left(X \mid \mathbf{E}_{1}\right), \ldots, P\left(X \mid \mathbf{E}_{n}\right)\right)$. The probabilities in question are calculated by:

$$
P(X)=\sum_{i=1}^{n} \lambda_{i} P_{i}(X)
$$

where $\lambda_{i}$ are positive weights given to each of the $n$ experts and $\sum_{i=1}^{n} \lambda_{i}=1$.
Although the weights $\lambda_{i}$ can sometimes be determined empirically given suitable data, they are often prescribed a priori based on the problemspecific context. In the case study considered in this paper, each expert is given equal weighting, based on the premise that the wayfinding process is quite a person-specific experience so all experiences were considered equally

valuable. Thus $\lambda_{i}=1 / n$ and

$$
P(X)=\sum_{i=1}^{n} P_{i}(X) / n
$$

Two kinds of linear pooling can be used to combine expert opinions for use in Bayesian Network models (Farr et al., 2018). Prior Linear Pooling describes the process by which elicited probabilities are pooled within each node and the resultant conditional probability tables are then propagated through the network to find the marginal probabilities for the nodes of interest. In contrast, Posterior Linear Pooling describes the process of quantifying and computing the BN for each expert separately, and the marginal probability distributions for the final nodes in the $n$ BNs are then pooled. Thus in prior linear pooling, Equation (2) is applied to each node separately in order to combine the opinions provided by the $n$ experts into a pooled probability table for that node, whereas, in posterior linear pooling, Equation (2) is applied to combine the $n$ marginal probability tables for the final nodes of the BN.

Despite the conceptual simplicity of linear pooling, there are some serious drawbacks to this approach (Genest \& Zidek, 1986). Firstly, pooling only gives a point estimate for the consensus, losing the variety of opinions across the experts. Secondly, pooling, particularly when used with BNs, does not follow from a coherent probability model (de Finetti, 1964). That is, linear

pooling can be considered an estimator if each observation is normally distributed and independent. The posterior mean is the sample average, and this implies that the errors are normally distributed. However, in the cases considered here the data are discrete and often binary, so they cannot be generated by a normal distribution (without substantive assumptions) and no coherence can exist. Hence it follows that linear pooling cannot follow from a coherent probability model. Thirdly, as illustrated in the case study below, the different linear pooling methods can result in different outcomes for the nodes of interest. Finally, the conditional independence structure of the BN is not reflected in the way in which the expert opinions are combined, particularly in the case of prior linear pooling.

As an example of the last point, say node $X$ influences node $Y$ and each node has the states ' $T$ ' and ' $F$ '. If $n$ experts provide their opinions, there would be $n$ probabilities for $P(X=\mathrm{T}), P(X=\mathrm{F}), P(Y=\mathrm{T} \mid X=$ $\mathrm{T}), P(Y=\mathrm{T} \mid X=\mathrm{F}), P(Y=\mathrm{F} \mid X=\mathrm{T})$, and $P(Y=\mathrm{F} \mid X=\mathrm{F})$. By applying prior linear pooling, the average for each of these probabilities is found, however these are not a reflection of what was originally given by the experts. That is, when the initial expert opinions were obtained, the 4 probabilities, $P(Y=\mathrm{T} \mid X=\mathrm{T}), P(Y=\mathrm{T} \mid X=\mathrm{F}), P(Y=\mathrm{F} \mid X=\mathrm{T})$, and $P(Y=\mathrm{F} \mid X=\mathrm{F})$, were given as conditional probabilities. By pooling these probabilities, the conditional independence structure is lost. This is illustrated in Table 1 where a toy example is shown. Here, the pooled

probabilities from five experts are combined via prior linear pooling in a BN. These values can be markedly different from the original probabilities given by the experts questioned, particularly if experts have very different opinions. Considering $P(Y=\mathrm{T})$, for example, prior pooling gives a value of 0.5944 , whereas 0.62 is obtained when using posterior pooling.

Table 1: Example: comparison among elicited and pooled probabilities in a BN, based on five experts $\mathbf{E}_{i}, i=1, . .5$.


An alternative approach, proposed in this paper, is to consider a measurement error model for combining expert opinions for use in BNs. The approach uses the posterior probabilities ascribed to each node in the BN, which are computed from the prior information given by each expert. These observed probabilities are assumed to be noisy 'measurements' of the true probabilities, and allow the representation of the systematic variation due to experts. This is described in more detail in Section 7.

# 5 Measurement error models 

In almost all fields of statistical modelling, there is measurement error in the data generating process, such that the observations of a variable $X$, say, vary from the underlying true value. The reasons for this variation can include inaccuracies in the recording device, potential bias or misclassification due to the study design, data collection practicalities in observational or experimental studies, and errors in data input. These errors can induce random or systemic variation and, if ignored, the parameter estimates and confidence intervals in statistical models can suffer from serious biases (Muff et al., 2015). If information about the errors induced in the measurement process is available, it may be useful to include them directly into the model. Information derived from experts can also be seen as a form of measurement error, in that the quantitative information elicited from each expert can be considered as a noisy realisation of an underlying common value.

There is a large literature on frequentist methods for addressing measurement error in regression (Carroll et al., 1999, 2006; Gustafson, 2003) and a growing literature on Bayesian methods for this issue (Muff et al., 2015; Richardson \& Gilks, 1993; Stephens \& Dellaportas, 1992). Bayesian approaches provide a natural framework for the inclusion of measurement errors, since discrepancies between observed and true values of a variable can be considered as, and described through, prior distributions and the linear predictors can then be written in terms of the true values. In addition,

a Bayesian model has been argued to be more straightforward to implement via Markov chain Monte Carlo (MCMC) than analogous frequentist models via Expectation-Maximisation (EM) (Carroll et al., 2006).

# 6 Generalised linear models: a baseline case 

A generalised linear model (GLM) extends linear regression by relating the linear model to the response variable via a link function and allowing the magnitude of the variance of each measurement to be a function of its predicted value (Nelder \& Wedderburn, 1972). Assuming that there are $n$ observations in a GLM, the data would be $(\mathbf{y}, \mathbf{z}, \mathbf{x})$, where the response variable is given by $\mathbf{y}=\left(y_{1}, \ldots, y_{n}\right)^{\mathrm{T}}$, the covariate matrix of dimension $n \times p$ for $p$ error-free covariates is given by $\mathbf{z}=\left(z_{1}, \ldots, z_{p}\right)$, and $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)^{\mathrm{T}}$ is the single error prone covariate whose true values are unobservable. In the case study, this can be applied to the $n$ expert opinions used to quantify the BN. Generalisation to multiple error prone covariates can be achieved by assuming that $\mathbf{y}$ comes from the exponential family with mean given by $\mu_{i}=E\left(y_{i} \mid x_{i}\right)$, and is linked to the linear predictor $\eta_{i}$ via

$$
\begin{aligned}
& \mu_{i}=h\left(\eta_{i}\right) \\
& \eta_{i}=\beta_{0}+\beta_{x} x_{i}+\mathbf{z}_{[i]} \beta_{z}
\end{aligned}
$$

where $h(\cdot)$ is a known response function, $\beta_{0}$ is the intercept, $\beta_{x}$ is the fixed effect for the error prone covariate $\mathbf{x}$, and $\mathbf{z}_{[i]}$ is a $1 \times p$ vector with corresponding vector of fixed effects given by $\beta_{z}$. By letting $\mathbf{w}=\left(w_{1}, \ldots, w_{n}\right)^{\mathrm{T}}$ be the observed version of the true, but unobservable, covariate $\mathbf{x}$, it is possible to formulate the classical measurement error model.

# 6.1 Classical measurement error model 

The classical measurement error model assumes that the covariate $\mathbf{x}$ can only be observed by a proxy $\mathbf{w}$ such that $\mathbf{w}=\mathbf{x}+\mathbf{u}$. The error vector is given by $\mathbf{u}=\left(u_{1}, \ldots, u_{n}\right)^{\mathrm{T}}$, the components of which are assumed to be independent and normally distributed with mean $=0$ and common variance $\tau_{u}^{-1}$, say (Muff et al., 2015). In a regression setup, if the error term $\mathbf{u}$ is assumed to be independent of the true covariate $\mathbf{x}$, any of the other covariates $\mathbf{z}$ and the response $\mathbf{y}$, then $\mathbf{y}$ and $\mathbf{w}$ are conditionally independent given $\mathbf{z}$ and $\mathbf{x}$. This means that, given the true covariate $\mathbf{x}$ and covariates $\mathbf{z}$, then having w provides no further information about the response variable, y (Carroll et al., 2006; Muff et al., 2015).

### 6.2 Measurement error models and Bayesian Networks

To our knowledge, there is no published literature on using measurement error models to combine expert opinions in Bayesian Networks. The closest work has been by Marella \& Vicard (2013), in which a mixed measure-

ment error model was proposed and an Object Oriented Bayesian Network (OOBN) (Koller \& Pfeffer, 1997) framework was used to implement the model. OOBNs are an extension of BNs where, instead of a node representing only a variable of interest, it can also contain nodes that are instances of other networks. The OOBN paradigm allows for hierarchical definition and construction of a BN by using network classes. The measurement model proposed in Marella \& Vicard (2013) describes the relationship between an observed and a true category in a questionnaire survey. The results from the measurement model are then used in an OOBN which is then used to represent, in a single model, the entire survey process.

# 7 Proposed Model 

For exposition and without loss of generality, consider a BN in which each node is binary, so that the information provided by the expert is in the form of the probability associated with one of the outcomes of the node. A measurement error model is proposed to treat the experts' probabilities for a node as observations of the underlying true probabilities, subject to systemic variation. While the focus of this work is primarily on the situation where consensus or agreement is formed simultaneously for multiple nodes in a BN, it is noted that a random effects model can be applied when considering only a single node.

In order to pool the probabilities on the correct 0 to 1 scale, a Beta

distribution for the response variable is used since it is more suitable as a data generating mechanism than the Gaussian error distribution implied by the linear pooling estimator. This is similar to the work of Ferrari \& Cribari-Neto (2004) and Figueroa-Zúniga et al. (2013), where the response variable is assumed to be beta distributed with the mean and the precision parameter modeled using fixed and random effects.

For the univariate model, where the consensus is formed for a single node of interest, consider

$$
p_{i} \sim \operatorname{Beta}\left(a_{i}, b_{i}\right)
$$

where $p_{i}$ is the marginal probability for expert $i=1, \ldots, n$. To allow for variation between experts, we take

$$
\begin{aligned}
\operatorname{logit}\left(\frac{a_{i}}{a_{i}+b_{i}}\right) & =\operatorname{logit}\left(\frac{a_{i}}{b_{i}}\right)=\mu+\epsilon_{i} \\
\text { where } \quad \mu & \sim \mathrm{N}\left(0, \tau_{\mu}^{-1}\right) \\
\epsilon_{i} & \sim \mathrm{~N}\left(0, \tau_{\epsilon}^{-1}\right)
\end{aligned}
$$

where the hyperparameters $\tau_{\mu}$ and $\tau_{\epsilon}$ are specified according to the problem.
Since the expected value of the logit term equals 0 , this implies that $a_{i}=b_{i}$, so an alternative construction is to consider a distribution symmetric

around $p_{i}=1 / 2$ and impose a prior on $a_{i}+b_{i}$,

$$
a_{i}+b_{i} \sim \operatorname{Gamma}\left(\alpha_{0}, \beta_{0}\right)
$$

where, as above, the hyperparameters $\alpha_{0}$ and $\beta_{0}$ are problem-specific.
An analogous multivariate measurement error (MME) model can be developed when forming consensus for multiple nodes in a BN. Consider

$$
p_{i j} \sim \operatorname{Beta}\left(a_{i j}, b_{i j}\right)
$$

where $p_{i j}$ is the marginal probability for expert $i=1, \ldots, n$ at node $j=$ $1, \ldots, m$. A multivariate Gaussian random effect for each expert can be used since the probabilities ascribed by experts to each node are treated as observations of the underlying true probabilities, which are closer around a mean value. To allow for extra variation due to the heterogeneity between experts, an independent random effect $\epsilon_{i}=\left(\epsilon_{i 1} \ldots \epsilon_{i m}\right)$ for each expert $i$ was added and a vague normal prior given to the mean, so

$$
\begin{aligned}
\operatorname{logit}\left(\frac{a_{i j}}{a_{i j}+b_{i j}}\right) & =\mu_{j}+\boldsymbol{\epsilon}_{i j} \\
\text { where } \quad \mu_{j} & \sim \mathrm{~N}\left(0, \tau_{\mu}^{-1}\right) \\
\boldsymbol{\epsilon}_{i} & \sim \mathrm{~N}\left(\mathbf{0}_{m}, \mathbf{Q}^{-1}\right), i=1, \ldots, n \\
a_{i j}+b_{i j} & \sim \operatorname{Gamma}\left(\alpha_{\tau}, \beta_{\tau}\right)
\end{aligned}
$$

The structure of the random effect term, $\boldsymbol{\epsilon}$, is such that $\boldsymbol{\epsilon}=\mathbf{R s}$, where $\mathbf{R}$ is the Cholesky decomposition of the precision matrix $\mathbf{Q}$ and $\mathbf{s}$ is a vector of iid standard normals, that is $\mathbf{s}=\mathrm{N}(0, I)$. By definition, if $\epsilon=\mathbf{R s}$ for $\mathbf{s}$ iid normals, then $\epsilon$ has the precision matrix such that $\mathbf{Q}=\left(\mathbf{R R}^{T}\right)^{-1}$ (Eaton, 2007). This implies that, if $\mathbf{R}$ has the correct sparsity required, then $\mathbf{Q}$ will also have the correct sparsity structure (Rue \& Held, 2005). This is an indirect way in which to put a prior on precision matrices with a fixed sparsity structure, or equivalently, on Gaussian distributions with the right conditional independence structure. Applying this to the multivariate model, it follows that $\boldsymbol{\epsilon} \sim \mathrm{N}\left(\mathbf{0}_{m}, \mathbf{R R}^{T}\right)$. Hence, similarly, by finding $\mathbf{R}$, we are able to give $\mathbf{Q}$ the right structure that reflects the conditional independence of a BN.

# 8 The three node MME Model 

In this section, we illustrate the use of a measurement error model for combining experts' opinions in a three node BN corresponding to the subnetwork of the WBNM described in Section 2. This provides sufficient opportunity to demonstrate the feasibility and utility of the approach in a simple, but significant, case. Recall that the subnetwork is structured as two root parent nodes, Environmental Factors (E) and Human Factors (H), connected by directed arcs to the child leaf node of Wayfinding (W), as depicted in Figure 3.

Following from the model described in the previous section, we observe that the precision matrix $\mathbf{Q}$ of the random effect, $\boldsymbol{\epsilon}_{i}$, gives information about the conditional probabilities and ensures that the expert opinions flow through the BN (here from Human and Environmental Factors to Wayfinding), as shown in (8). The proposed model allows also for the combination of all the opinions, so that all of them will count. If reordering of the independent expert opinions occurs, coherence is maintained and there will not be an impact on the result of the model. Additionally, $\mathbf{Q}$ allows the model to 'borrow strength' from other parts of the model (Tukey, 1974). That is, information from one node can be used to inform other nodes as information is able to travel up and down the levels of the hierarchy (Efron, 2010). The issue of ensuring that the conditional independence structure of the BN is reflected when combining expert opinions is addressed by the

![img-2.jpeg](img-2.jpeg)

Figure 3: The sparsity structure of the precision matrix, $\mathbf{Q}$. The structure of this matrix reflects the conditional independence structure of the final 3 nodes of the WBNM.
precision matrix $\mathbf{Q}$. In order for the consensus model to be consistent with the BN structure, the conditional independence structure of the Gaussian random effect was forced to mirror that of the BN. This forces a sparsity structure on the precision matrix $\mathbf{Q}$, such that $\mathbf{Q}_{i j} \neq 0$ iff node $i$ depends on node $j$ in the BN.

The structure of the precision matrix, $\mathbf{Q}$, is constructed to reflect the conditional independence structure of these nodes, as shown in Figure 3.

This requires the construction of $\mathbf{R}$, the Cholesky decomposition of Q. This is where the expert priors on $\mathbf{Q}$ are used. Recall that in (6), $\operatorname{logit}\left(\frac{a_{i j}}{a_{i j}+b_{i j}}\right)=\mu_{j}+\boldsymbol{\epsilon}_{i j}$. It is possible to write $\boldsymbol{\epsilon}_{i}=\mathbf{R s}$, which leads to

$$
\left.\begin{array}{l}
\operatorname{logit} \mu_{H}=\mu_{H}+\beta_{1} \epsilon_{W}+\epsilon_{H} \\
\operatorname{logit} \mu_{E}=\mu_{E}+\beta_{2} \epsilon_{W}+\epsilon_{E} \\
\operatorname{logit} \mu_{W}=\mu_{Q}+\beta_{3} \epsilon_{H}+\beta_{4} \epsilon_{E}+\epsilon_{W}
\end{array}\right\}
$$

where $\mu_{H}, \mu_{E}$, and $\mu_{W}$ are the mean opinions for nodes H, E, and W respec-

tively and $\epsilon_{H}, \epsilon_{E}$, and $\epsilon_{W}$ are the random effect associated with the expert opinions for nodes H, E, and W respectively. The $\beta$ terms give a measure of how much of the random effect comes from the other nodes. That is, $\beta_{1}$ says how much noise from W influences $\mathrm{H}, \beta_{2}$ is a measure of how much W influences E , and $\beta_{3}$ and $\beta_{4}$ gives the size of the influence of H and E respectively on W .

In vector form, this gives

$$
\operatorname{logit} \boldsymbol{\mu}_{X}=\boldsymbol{\mu}_{X}+\mathbf{R s}
$$

where $\mathbf{R}$ is given by

$$
\mathbf{R}=\left(\begin{array}{ccc}
\tau_{H}^{-1 / 2} & 0 & \beta_{1} \tau_{W}^{-1 / 2} \\
0 & \tau_{E}^{-1 / 2} & \beta_{2} \tau_{W}^{-1 / 2} \\
0 & 0 & \tau_{W}^{-1 / 2}
\end{array}\right)
$$

with $\tau_{X} \sim \operatorname{Gamma}\left(1,5 \times 10^{-5}\right)$ and $\beta_{X} \sim \mathrm{~N}\left(0,5 \times 10^{-5}\right)$. Since $\mathbf{Q}=$ $\left(\mathbf{R R}^{T}\right)^{-1}$ (Eaton, 2007), this gives the precision matrix as

$$
\mathbf{Q}=\left(\begin{array}{ccc}
\tau_{H} & 0 & -\beta_{1} \tau_{H} \\
0 & \tau_{E} & -\beta_{2} \tau_{E} \\
-\beta_{1} \tau_{H} & -\beta_{2} \tau_{E} & \beta_{1}^{2} \tau_{H} \tau_{W}^{2}+\beta_{2}^{2} \tau_{E} \tau_{W}^{2}+\tau_{W}
\end{array}\right)
$$

It should be noted that if all of the $\beta$ 's are zeros, then the random effects

$\epsilon_{H}, \epsilon_{E}$, and $\epsilon_{H}$ are independent and $\mathbf{Q}$ is a diagonal precision matrix.

# 9 Results 

The MME model given by Equation (6) was applied to the final three nodes of the WBNM. As discussed in Section 2, the dataset used for the analysis (available in the Appendix) comprised the set of opinions elicited from the $n=99$ experts about the states 'Good', 'Good' and 'Effective' for the Human Factors, Environmental Factors and Wayfinding nodes respectively. A $\operatorname{Gamma}(1,0.1)$ distribution was specified for the prior on the terms $a+b$, in line with the ambition to have proper but relatively uninformative priors. This was justified by calculating an approximate $95 \%$ interval for the anticipated values for $p_{i}$ implied by this prior, obtained by taking the $2.5 \%$ and $97.5 \%$ quantiles for the prior, letting $a_{i}=b_{i}$, and undoing the logit transformation. The obtained interval was 0.53 to 1 , which was considered to be reasonable. Proper but relatively uninformative priors were also specified for $\mu$ and $\epsilon$, with $\tau_{\mu}^{-1}=10^{4}$ producing a diffuse distribution on $\mu$ and hence an almost uniform distribution on $p_{i}$, and $\left(a_{\tau}, b_{\tau}\right)=\left(1,5 \times 10^{5}\right)$ producing a distribution for $\epsilon$ that reflected a relatively small contribution of the measurement error to the overall value of $p_{i}$.

The analysis was undertaken using the R package Integrated Nested Laplace Approximation (R-INLA) (Rue et al., 2009). R-INLA allows full Bayesian inference to be performed on a class of latent Gaussian models

(LGMs) including spatial models, geostatistical models, generalised linear mixed models, and generalised additive models (Martins et al., 2013). It utilises deterministic Laplace approximations by fitting Gaussian conditional posteriors via an optimisation step for LGMs. The approximation can also be used in a nested framework and provides a faster and more accurate alternative to simulation-based Markov chain Monte Carlo (MCMC) schemes (Martins et al., 2013). The multivariate model given by (6) and its application to the final three nodes of the WBNM is a good candidate for using R-INLA due to the sparsity of $\mathbf{Q}$ and the ability to perform fast, easy and accurate computation for this class of problem. The R-INLA code used for the analysis is provided in the Appendix.

The resulting distributions from the MME model are shown by the solid black line in Figure 4. For comparison, prior and posterior linear pooling were also performed using the same BN and dataset. The results are also shown in Figure 4, with the distributions depicted in blue and red, respectively.

The results for both pooling methods are almost identical for the Human and Environmental Factor nodes at 0.708 and 0.768 respectively, with the MME model mean differing in both cases at 0.715 and 0.7587 for the respective nodes. The posterior pooling result and the MME model mean for the Wayfinding node are almost the same at 0.755 , and are different to the prior pooling result which is 0.752 . This may be due to the fact that both

![img-3.jpeg](img-3.jpeg)

Figure 4: The results of the implementation of the MME model (solid black line), prior linear pooling (dashed blue line), and posterior linear pooling (solid red line) on the final 3 nodes of the Wayfinding Bayesian Network Model.

the MME model and the posterior pooling follow the conditional independence structure of the BN, whereas the prior pooling method does not. By using the MME model it is possible to obtain a distribution for the nodes of interest. This is more informative than a point estimate like that obtained using the pooling methods as it describes the uncertainty associated with the estimates.

To investigate if a small sample size has an impact on the results, the MME model and the posterior pooling were implemented for $n=15$ randomly selected data points for the final three nodes of the WBNM. The distribution for the MME model is shown in Figure 5 as the solid black line, with the pooled results shown as the solid red line. For all three nodes, the MME model and the posterior pooling results were comparable. Given the choice of which method to use, the MME model would still be preferable to posterior pooling for the reasons noted earlier. That is, it follows from a coherent probability model, the resulting distribution is more informative than a point estimate, and it allows for uncertainty.

Using the same subset of 15 data points, the univariate model given by (4) was also implemented for each of the 3 final nodes of the WBNM. This method is easier to implement than the MME model since the conditional independence structure of $\mathbf{Q}$ does not have to be calculated. That is, the $\beta$ 's in Equation (8) are zero and $\mathbf{Q}$ is a diagonal matrix. The results of the implementation of this model are shown by the dashed lines in Figure

![img-4.jpeg](img-4.jpeg)

Figure 5: The results from an implementation of the MME model (solid black line), posterior pooling (red line), and the univariate model applied to each node (dashed black line) on $n=15$ randomly selected data points.

5. For each of the three nodes, the probability mass for the MME model resulted in both better location and a more conservative spread than that of the univariate model. This is because the MME model is able to borrow strength from other nodes in order to better inform the model.

# 10 Discussion 

The MME model proposed in this paper addresses the issues associated with the current pooling methods used for combining expert opinions in Bayesian networks. Namely the issues are that pooling, when used with BNs, does not follow from a coherent probability model, the conditional independence structure of the BN is not followed, particularly in the case of prior pooling, and pooling only gives a point estimate for the consensus. The MME model overcomes these issues by using a measurement error model to treat each of the probabilities ascribed by experts to each node as observations of the underlying true probabilities that are subject to systemic variation due to experts.

The systemic variation is modelled through the random effect term, $\boldsymbol{\epsilon}_{i}$, which contains the precision matrix $\mathbf{Q}$. By ensuring the correct structure and sparsity of $\mathbf{Q}$, the conditional independence of the BN is reflected in the model. Additionally, $\mathbf{Q}$ also contains information regarding the conditional probabilities in the BN and as such addresses the issue of coherence. Finally, by using a measurement error approach, it is possible to obtain a distribution

for each state and node of interest. This makes it possible to obtain a measurement with uncertainty for any marginal probability of interest rather than just a point estimate.

It must be noted that since expert opinions may not necessarily follow the measurement error model (for example, the experts questioned may all be biased), this uncertainty cannot be taken on face value. Keith (1996), for example, argues against the aggregation of opinions or, at least, the overaggregation of opinions. This is particularly relevant to situations where opinions may be biased or extreme, since the combined distributions of the opinions may bear no similarity to the true distribution of the probabilities.

The MME model can be modified to cater for issues such as expert weighting and outlier detection. Expert information can be differentially weighted in the BN through the weights $\lambda_{i}$ in Equation (2) or by imposing a differential inflation factor on the variances of the expert-specific priors in Equations (4) and (6). In this case study, all experts were weighted equally. Outlier detection can be incorporated by considering the conditional predictive ordinate (CPO) values (Geisser, 1980), which is a tool for detecting observations that are fitted poorly by a given model. In this case, it would measure how well an expert is predicted from the other experts. The CPO expresses the posterior probability of observing the value $i$ when the model is fitted to all data except $i$. Very low CPO values imply that $i$ is an outlier and an influential observation (Gelfand, 1996).

The MME model could also be extended to include bias and additional covariates. In the case study, if there was an interest in investigating the effect of experienced (E) and inexperienced (I) travellers, the overall mean for node $j, \mu_{j}$, in the model given by (6) could be modified as follows,

$$
\begin{aligned}
\mu_{I} & \sim \mathrm{~N}\left(\mu_{j}-\delta_{I}, \sigma_{I}^{2}\right) \\
\mu_{E} & \sim \mathrm{~N}\left(\mu_{j}+\eta_{E}, \sigma_{E}^{2}\right)
\end{aligned}
$$

where $\mu_{I}$ and $\mu_{E}$ are the means for inexperienced and experienced travellers respectively, $\sigma_{I}^{2}$ and $\sigma_{E}^{2}$ are the variances for inexperienced and experienced travellers respectively, and $\delta_{I}$ and $\eta_{E}$ represent the impact of inexperienced and experienced travellers respectively on the overall mean, $\mu_{j}$.

As discussed earlier, there is a strong connection between generalised linear models and measurement error ones and it could be worth fitting a generalised multivariate regression model and comparing the results with the ones in the current paper. We believe that the sparsity structure of the BNs makes our approach more suitable but we leave the practical comparison to future work.

Finally, it has to be noted that the method proposed here to obtain the correct conditional independence structure in the Gaussian random effect is hard to extend to more complicated networks. If more than three nodes were to be investigated, the use of G-Wishart priors for $\mathbf{Q}$, which are restrictions

of Wishart random variables to the subspace of matrices with the correct sparsity structure, has to be undertaken (Lenkoski, 2013). Recent results have derived direct samplers for G-Wishart random variables, which makes them practical in this application (Lenkoski, 2013; Wang \& Li, 2012). An extension to more than three nodes means that an MCMC scheme rather than INLA would be used to perform the inference.

In this paper, we have focussed on a three node sub-graph of the full wayfinding Bayesian network. The methods described in this paper would, theoretically, scale up to a problem of that size. As with many multivariate models, we are defeated by an explosion in the number of parameters. For a Bayesian network with $n$ nodes and $n_{c}$ connections, then fitting the multivariate measurement error model proposed in Section 3 requires the estimation of $n+n_{c}$ precision parameters and $n$ intercepts. This is significantly smaller than the number of precision parameters needed for the MME model without the conditional independence assumptions; for the full wayfinding network, the number of precision parameters is reduced from 1125 to 107. Unfortunately, with only 99 data points, it is not feasible to fit a model of this complexity to the current data set.

# Acknowledgments 

This research forms part of the work undertaken by the Airports of the Future (LP0990135) project, which is funded by the Australian Research

Council Linkage Project scheme. The authors also acknowledge the contributions made by the many aviation industry stakeholders also involved in this project. More details on Airports of the Future and its participants can be found at https://research.qut.edu.au/aotf/.

# Appendix 

## Dataset for the three nodes of the Wayfinding BN Model

The following dataset was used for the case study analysis. The values represent the probabilities assigned by each of the 99 experts to the three nodes, Environmental Factors (ef), Human Factors (hf) and Wayfinding (wf).


# R-INLA code 

The following code indicates the workflow and includes the model calls to R-INLA.
```
#Install packages "INLA" from "http://www.r-inla.org/download"
#Get and process data and adjacency matrix
formula = Y -1 + Node.Name + f(Expert.No,model="iid") + f(Node.No, model="bym2", graph=adj)
result = inla(formula,data=data,family=c("beta","binomial"), Ntrials = data\$n, control.fixed=list(prec.intercept=0.1,prec=0.1), verbose= FALSE, control.predictor = list(compute=T, link=1))
#Plot the required marginal posterior probabilities
#Fit the model without random effects and compare the IQRs
formula2 = Y -1 + Node.Name
result2 = inla(formula2,data=data,family=c("beta","binomial"), Ntrials
= dat$n,control.fixed=list(prec.intercept=0.1,prec=0.1), verbose=FALSE,
control.predictor = list(compute=T, link=1))
print((result$summary.fitted.values"0.975quant"[5000:5050] -
result$summary.fitted.values"0.025quant"[5000:5050])/
(result2summary.fitted.values"0.975quant"[5000:5050]-
result2summary.fitted.values"0.025quant"[5000:5050]))
#Plot the different posterior consensus probabilities for the individual
nodes
```

![img-5.jpeg](img-5.jpeg)

This article is protected by copyright. All rights reserved.

![img-6.jpeg](img-6.jpeg)
bn_q.png

# Good Environmental Factors 

![img-7.jpeg](img-7.jpeg)

This article is protected by copyright. All rights reserved.

![img-8.jpeg](img-8.jpeg)

This article is protected by copyright. All rights reserved.

# Good Human Factors 

![img-9.jpeg](img-9.jpeg)

This article is protected by copyright. All rights reserved.

# Good Human Factors 

![img-10.jpeg](img-10.jpeg)
hf_sub_15_b.png

![img-11.jpeg](img-11.jpeg)
(a)


(b)


(c)
sample.png

![img-12.jpeg](img-12.jpeg)

# Wayfinding

# Effective Wayfinding 

![img-13.jpeg](img-13.jpeg)
wf_full_all.png

# Effective Wayfinding 

![img-14.jpeg](img-14.jpeg)
wf_sub_15_b.png