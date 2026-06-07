# A probabilistic network for the diagnosis of acute cardiopulmonary diseases 

Alessandro Magrini ${ }^{\mathrm{a}}$, Davide Luciani ${ }^{\mathrm{b}}$, Federico Mattia Stefanini ${ }^{\mathrm{a}}$<br>${ }^{a}$ Department of Statistics, Computer Science, Applications - University of Florence, Florence, Italy<br>${ }^{\mathrm{b}}$ IRCCS - Mario Negri Institute for Pharmacological Research, Milan, Italy


#### Abstract

In this paper, the development of a probabilistic network for the diagnosis of acute cardiopulmonary diseases is presented. This paper is a draft version of the article published after peer review in 2018 (https://doi.org/10.1002/bimj.201600206). A panel of expert physicians collaborated to specify the qualitative part, that is a directed acyclic graph defining a factorization of the joint probability distribution of domain variables. The quantitative part, that is the set of all conditional probability distributions defined by each factor, was estimated following the Bayesian paradigm: we applied an original formal representation, characterized by a low number of parameters and a parameterization intelligible for physicians, elicited the joint prior distribution of parameters from medical experts, and updated it by conditioning on a dataset of hospital patient records using Markov Chain Monte Carlo simulation. Refinement was iteratively performed until the probabilistic network provided satisfactory Concordance Index values for a selection of acute diseases and reasonable inference on six fictitious patient cases. The probabilistic network can be employed to perform medical diagnosis on a total of 63 diseases ( 38 acute and 25 chronic) on the basis of up to 167 patient findings.


Keywords: Bayesian inference; Belief elicitation; Beta regression; Categorical logistic regression; Latent variables.

## 1. Introduction

Medical diagnosis is the process of identifying the disease a patient is affected by, based on the assessment of specific risk factors, signs, symptoms and results of exams. Probabilistic networks (Koller and Friedman, 2009) are increasingly used to support medical diagnosis, as they provide an efficient representation of complex stochastic systems by exploiting causal knowledge, and because several efficient algorithms to perform probabilistic reasoning (evidence propagation) are available (Lucas et al., 2004).

Probabilistic networks are composed of a qualitative part, that is a directed acyclic graph (DAG) defining a factorization of the joint probability distribution of domain variables, and of a quantitative part, where each factor defines a conditional probability distribution. In medical problems, the DAG is often specified in terms of causal relationships among variables according to pathophysiological knowledge contained in the specialised literature. However, the information required to estimate the quantitative part is typically scattered in many different sources and varies greatly in quality (Druzdzel and der Gaag, 2000). Medical literature represents the most reliable source of quantitative information, but it may not cover all aspects of interest. When this is the case, medical experts are a useful alternative resource, even though their quantitative assessments may not be reliable without special training (Kahneman et al., 1982). Clinical data from medical records are another valuable source of knowledge to build a probabilistic network, but they are typically limited to few variables or contain many missing values.

In existing medical applications of probabilistic networks, the quantitative part is typically estimated exploiting either expert knowledge (Nathwani et al., 1997; Suojanen et al., 1999; Andreassen

[^0]
[^0]:    Email addresses: magrini@disia.unifi.it (Alessandro Magrini), davide.luciani@marionegri.it (Davide Luciani), stefanini@disia.unifi.it (Federico Mattia Stefanini)

et al., 1991; Díez et al., 1997; der Gaag et al., 2002; Galán et al., 2002; Lacave and Díez, 2003; Charitos et al., 2009; Luciani et al., 2007; Leibovici et al., 2007), or a database of patient cases (Middleton et al., 1991; Wasyluk et al., 2001). In this paper, we describe our experience in the development of a probabilistic network for the diagnosis of acute cardiopulmonary diseases, where two sources of information, beliefs from medical experts and clinical data, were exploited to estimate the quantitative part. The probabilistic network was conceived as an extension of BayPAD (Bayesian Pulmonary embolism Assisted Diagnosis), a probabilistic network for the diagnosis of pulmonary embolism (Luciani et al., 2007). The work involved a panel of medical experts from various specialties and consisted of three stages. In the first stage, the qualitative part was specified by medical experts following the constraint DAG described in (Luciani and Stefanini, 2012). In the second stage, we applied an original formal representation to the quantitative part, characterized by a low number of parameters and a parameterization intelligible for physicians, and the joint prior distribution of parameters was elicited from medical experts. In the third stage, we updated the joint prior distribution of parameters in the Bayesian paradigm by conditioning on a dataset of hospital patient records using Markov Chain Monte Carlo (MCMC) simulation. The three stages were iterated until the probabilistic network provided reasonable inference on six fictitious patient cases. The three stages were iterated until the probabilistic network provided satisfactory Concordance Index values for several acute diseases and reasonable inference on several fictitious patient cases.

The paper is organized as follows. In Section 2, we provide details on the specification of the qualitative part. In Section 3, we explain the formal representation for the quantitative part and the method to elicit the joint prior distribution of parameters. In Section 4, we present data and provide details on Bayesian estimation of the quantitative part. In Section 5, we illustrate the elicitation task for two variables in the probabilistic network, and compare the resulting prior distribution with the posterior distribution obtained from MCMC simulation. In Section 6, we detail the refinement process. Section 7 includes the discussion of our contribution.

# 2. Specification of the qualitative part 

The qualitative part of a probabilistic network consists of a directed acyclic graph (DAG) representing a factorization of the joint probability distribution of variables. Each node of the DAG represents a variable, that may receive any number of directed edges, indicating on which variables (parent variables) its probability distribution is conditioned.

The qualitative part of our probabilistic network was specified complying the constraint DAG (c-DAG, Figure 1) described in Luciani and Stefanini (2012), where c-nodes are sets of variables and c-edges among c-nodes specify allowed directions of edges in the qualitative part of the probabilistic network. Medical experts populated c-nodes of the c-DAG with relevant medical variables, as documented in the specialised literature. Edges that join nodes belonging to different c-nodes always agree with c-edges, while eventual edges joining nodes belonging to the same c-node were specified by medical experts, without obeying any constraint besides the absence of directed cycles in the resulting DAG. The automated interview proposed by Luciani and Stefanini (2012) was not adopted because it was conceived to derive the DAG corresponding to a single patient presentation.

Due to the large number of variables, the resulting qualitative part is not displayed, but the typology and the set of parent variables (parent set) of each one is shown in Appendix . Table 1 provides the classification of variables included in the probabilistic network with respect to their statistical and medical (as defined by the maximal constraint DAG) typology.

## 3. Elicitation of the quantitative part

The quantitative part of a probabilistic network corresponds to the joint probability distribution of domain variables, and it is factored according to the DAG into the product of univariate conditional distributions, one for each variable given its parent variables in the DAG (Koller and Friedman, 2009).

The special case where each variable has finite sample space is known as Bayesian network (Korb and Nicholson, 2010). The quantitative part of a Bayesian network is composed of one Conditional

![img-0.jpeg](img-0.jpeg)

Figure 1: The maximal constraint DAG, where c-nodes are sets of medical variables: *V<sub>R</sub>*: aetiology; *V<sub>C</sub>*: epidemiology; *V<sub>Q</sub>*: pathogenesis.; *V<sub>D</sub>*: pathology; *V<sub>S</sub>*: pathophysiology; *V<sub>MC</sub>*: semiotics (patient's chief complaints); *V<sub>MO</sub>*: semiotics (future outcomes); *V<sub>MM</sub>*: semiotics (other manifestations).

Table 1: Classification of variables included in the probabilistic network. 'Binary': categorical with one non-neutral category. 'Multi-valued': categorical with more than one non-neutral category. No variables representing patient's chief complaints (*V<sub>MC</sub>*) are included, because the qualitative part was specified by considering the most relevant diseases pertaining to the medical domain under analysis, instead of focusing on specific case reports.


Probability Table (CPT) for each variable. In prominent medical applications of probabilistic networks (Nathwani et al., 1997; Suojanen et al., 1999; Andreassen et al., 1991; Díez et al., 1997; der Gaag et al., 2002; Wasyluk et al., 2001; Galán et al., 2002; Lacave and Díez, 2003; Charitos et al., 2009; Luciani et al., 2007; Leibovici et al., 2007), continuous variables underwent to discretization in order to obtain a Bayesian network. The major benefits of a Bayesian network consist of a parameterization intelligible for a domain expert (parameters are conditional probabilities) and the availability of fast algorithms for evidence propagation (Yuan and Druzdzel, 2012). However, discretization of continuous variables may dramatically increase the number of parameters required to represent the quantitative part, thus increasing uncertainty of estimates. We avoided discretization of continuous variables by applying an original formal representation to the quantitative part, characterized by a low number of parameters and a parameterization intelligible for physicians. In the proposed formal representation, continuous variables are preliminarily rescaled in order to assimilate the interpretation of quantitative and qualitative values, and a combination of the Beta regression and the categorical logistic regression, reparameterized to help physicians in performing quantitative assessments competently, is exploited to model the distribution of each variable in the network. The rescaling procedure and the two conditional models are detailed in the remainder of this section.

### 3.1. Rescaling procedure

Medical categorical variables represent a qualitative measure of a patient's condition, discriminating among a healthy status and one or more pathological conditions. We assign value 0 to the

category associated to a healthy patient condition and we refer to it as the neutral value of the variable. Instead, we assign consecutive integer numbers to the categories associated to pathological patient conditions (non-neutral categories). For example, a medical categorical variable with a single non-neutral category will have sample space $\{v: v=0,1\}$, while the sample space will be $\{v: v=0,1,2\}$ if there are two non-neutral categories.

The interpretation of measured values of medical continuous variables is similar, but it depends on the scale of the variable at hand, thus medical reasoning is more complicated. The standard medical training and medical literature provides physicians the ability to properly recognize the extreme values of a medical continuous variable in a living patient, as well as to distinguish among values involving normal and pathological patient conditions (Jacobs et al., 2001; Irwin and Rippe, 2011). On these grounds, the scale $\left(v_{\mathrm{L} 2}, v_{\mathrm{R} 2}\right)$ of a medical continuous variable $V$ is partitioned into three intervals: $n$-range $\left[v_{\mathrm{L} 1}, v_{\mathrm{R} 1}\right]$, in which values are regarded as non-pathological, $l p$-range $\left(v_{\mathrm{L} 2}, v_{\mathrm{L} 1}\right)$, including values lower than non-pathological ones, and $h p$-range $\left(v_{\mathrm{R} 1}, v_{\mathrm{R} 2}\right)$, including values higher than non-pathological ones. The mid value of $n$-range is taken as the neutral value, while the mid values of $l p$-range and $h p$-range are taken as reference for all values representing hypo- or hyper-pathological conditions, respectively. As a special case, one among $l p$-range or $h p$-range may be of null size.

In order to make reasoning on quantitative values easier for physicians, we propose a rescaling procedure making $n$-range, $l p$-range and $h p$-range of equal size and mapping their mid values to 0 , -1 and 1 , respectively:

$$
\widetilde{V}= \begin{cases}-1.5+\frac{V-v_{\mathrm{L} 2}}{v_{\mathrm{L} 1}-v_{\mathrm{L} 2}} & \text { if } V<v_{\mathrm{L} 1} \\ -0.5+\frac{V-v_{\mathrm{L} 1}}{v_{\mathrm{R} 1}-v_{\mathrm{L} 1}} & \text { if } v_{\mathrm{L} 1} \leq V<v_{\mathrm{R} 1} \\ 0.5+\frac{V-v_{\mathrm{R} 1}}{v_{\mathrm{R} 2}-v_{\mathrm{R} 1}} & \text { if } V \geq v_{\mathrm{R} 1}\end{cases}
$$

This way, a medical expert may refer to a value of a continuous variable in terms of the relative position within one among $n$-range, $l p$-range and $h p$-range, instead of as a measured value on the original scale. For instance, relative position $\varrho$ in $l p$-range corresponds to a rescaled value equal to $-1.5+\varrho$, whereas relative position $\varrho$ in $n$-range or in $h p$-range corresponds to a rescaled value equal to $-0.5+\varrho$ and $0.5+\varrho$, respectively. Furthermore, the rescaling procedure assimilates the interpretation of quantitative and qualitative medical scales, because value 0 of any variable represents a healthy patient condition, and an unit variation from value 0 is interpreted as a change of patient's state to a reference pathological condition.

In the remainder, continuous variables are implicitly considered as already rescaled.

# 3.2. Categorical logistic regression 

Consider a categorical variable included in the probabilistic network, say $Y$, with $s_{Y}$ non-neutral values and parent set $\boldsymbol{X}$. All categorical variables in $\boldsymbol{X}$ with more than one non-neutral value are replaced by a set of dummy indicators, one for each non-neutral value, obtaining the parent set $X_{1}, \ldots, X_{n}$. The categorical logistic regression (McCullagh and Nelder, 1989, Chapter 5) applied to $Y$ is:

$$
\begin{gathered}
\log \left(\frac{\operatorname{Pr}\left(Y=y \mid x_{1}, \ldots, x_{n}\right)}{\operatorname{Pr}\left(Y=0 \mid x_{1}, \ldots, x_{n}\right)}\right)=\left(1, x_{1}, \ldots, x_{n}\right)^{\prime} \boldsymbol{\beta}^{(y)} \\
\boldsymbol{\beta}^{(y)}=\left(\beta_{0, y}, \beta_{1, y}, \ldots, \beta_{n, y}\right) \quad y=1, \ldots, s_{Y}
\end{gathered}
$$

For each non-neutral value $y$ of $Y$, parameters in $\boldsymbol{\beta}^{(y)}$ are regression coefficients on the logit scale and are interpreted as log odds ratios:

$$
\begin{gathered}
\beta_{0, y}=\log \left(\frac{\pi_{0, y}}{\pi_{0,0}}\right) \quad y=1, \ldots, s_{Y} \\
\beta_{i, y}=\log \left(\frac{\pi_{i, y}}{\pi_{i, 0}}\right)-\beta_{0, y} \quad i=1, \ldots, n ; y=1, \ldots, s_{Y}
\end{gathered}
$$

where:

$$
\begin{gathered}
\pi_{0, y}=\operatorname{Pr}\left[Y=y \mid X_{1}=0, \ldots, X_{n}=0\right] \quad y=0,1, \ldots, s_{Y} \\
\pi_{i, y}=\operatorname{Pr}\left[Y=y \mid X_{i}=1, X_{j: j \neq i}=0\right] \quad i=1, \ldots, n ; y=0,1, \ldots, s_{Y}
\end{gathered}
$$

If $X_{i}$ is a continuous parent variable, it holds:

$$
\pi_{i, y}=\operatorname{Pr}\left[Y=y \mid X_{i}=1, X_{j: j \neq i}=0\right]=1-\operatorname{Pr}\left[Y=y \mid X_{i}=-1, X_{j: j \neq i}=0\right]
$$

The conditional probability of non-neutral value $y$ of $Y$ can be can be rewritten in terms of parameters $\boldsymbol{\pi}^{(y)}=\left(\pi_{0, y}, \pi_{1, y}, \ldots, \pi_{n, y}\right)$ :

$$
\begin{gathered}
\log \left(\frac{\operatorname{Pr}\left(Y=y \mid x_{1}, \ldots, x_{n}\right)}{\operatorname{Pr}\left(Y=0 \mid x_{1}, \ldots, x_{n}\right)}\right)=\left(1-\sum_{i=1}^{n} x_{i}\right) \log \left(\frac{\pi_{0, y}}{\pi_{0,0}}\right)+\sum_{i=1}^{n} x_{i} \log \left(\frac{\pi_{i, y}}{\pi_{i, 0}}\right) \\
y=1, \ldots, s_{Y}
\end{gathered}
$$

It follows that parameters are probabilities conditioned to a configuration of parent variables where all but one take value 0 , thus physicians are expected to be competent in performing quantitative assessments. The prior distribution of $\left(\pi_{i, 0}, \pi_{i, 1}, \ldots, \pi_{i, s_{Y}}\right)(i=0,1, \ldots, n)$ is elicited using the Equivalent Prior Sample (EPS) method (Winkler, 1967):

$$
\left(\pi_{i, 0}, \pi_{i, 1}, \ldots, \pi_{i, s_{Y}}\right) \sim \operatorname{Dirichlet}\left(\hat{\pi}_{i, 0} \cdot \hat{q}_{i, 0}, \hat{\pi}_{i, 1} \cdot \hat{q}_{i, 1}, \ldots, \hat{\pi}_{i, s_{Y}} \cdot \hat{q}_{i, s_{Y}}\right)
$$

where, for $y=0,1, \ldots, s_{Y}, \hat{\pi}_{i, y}$ is the assessment of $\pi_{i, y}$ and $\hat{q}_{i, y}$ is the number of patient cases on which $\hat{\pi}_{i, y}$ is based.

Value 0 is not allowed for parameters $\pi_{0,0}, \ldots, \pi_{0, s_{Y}}$. This issue can be overcome by replacing zeros with a small number, for example $10^{-7}$ to provide an exact representation up to the sixth decimal. Unfortunately, in this case or simply when $\pi_{0, y}$ is small compared to $\pi_{i, y}$ for any $y>0$ and $i>0$, the probability of the neutral value of $Y$ tends to become 0 too fast as more than one parent variable takes a non-neutral value. Thus, we further refine the model in Equation 6 as a mixture of two components: a categorical probability distribution $\pi_{0,0}, \ldots, \pi_{0, s_{Y}}$ when the sum of parent values is less or equal to zero, and, otherwise, the model in Equation 6 where parameters $\beta_{0,1}, \ldots, \beta_{0, s_{Y}}$ are replaced by new parameters $\eta_{1}, \ldots, \eta_{s_{Y}}$ unrelated to $\pi_{0,0}, \ldots, \pi_{0, s_{Y}}$ :

$$
\begin{gathered}
\left\{\begin{array}{l}
\operatorname{Pr}\left(Y=y \mid x_{1}, \ldots, x_{n}\right)=\pi_{0, y} \\
\log \left(\frac{\operatorname{Pr}\left(Y=y \mid x_{1}, \ldots, x_{n}\right)}{\operatorname{Pr}\left(Y=0 \mid x_{1}, \ldots, x_{n}\right)}\right)=\left(1-\sum_{i=1}^{n} x_{i}\right) \eta_{y}+\sum_{i=1}^{n} x_{i} \log \left(\frac{\pi_{i, y}}{\pi_{i, n}}\right) \quad \text { otherwise } \\
y=1, \ldots, s_{Y}
\end{array}\right.
\end{gathered}
$$

For $i=1, \ldots, s_{Y}$, parameter $\eta_{y}$ is set equal to 0 if $Y$ has less than two parent variables, otherwise a standard Gaussian prior is assumed.

# 3.3. Beta regression 

Consider a continuous variable included in the probabilistic network, say $Y$, with parent set $\boldsymbol{X}$. All categorical variables in $\boldsymbol{X}$ with more than one non-neutral value are replaced by a set of dummy indicators, one for each non-neutral value, obtaining the parent set $X_{1}, \ldots, X_{n}$. The variable $\frac{Y+1.5}{3}$ has sample space $(0,1)$, thus the Beta regression model (Ferrari and Cribari-Neto, 2004) can be applied:

$$
\begin{gathered}
\frac{Y+1.5}{3} \sim \operatorname{Beta}(\delta \tau,(1-\delta) \tau) \\
\log \left(\frac{\delta}{1-\delta}\right)=\log \left(\frac{\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]+1.5}{1.5-\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]}\right)=\left(1, x_{1}, \ldots, x_{n}\right)^{\prime} \boldsymbol{\beta}
\end{gathered}
$$

Parameters $\boldsymbol{\beta}=\left(\beta_{0}, \beta_{1}, \ldots, \beta_{n}\right)$ are regression coefficients on the logit scale and have the following interpretation:

$$
\begin{gathered}
\beta_{0}=\log \left(\frac{\mu_{0}+1.5}{1.5-\mu_{0}}\right) \\
\beta_{i}=\log \left(\frac{\mu_{i}+1.5}{1.5-\mu_{i}}\right)-\beta_{0} \quad i=1, \ldots, n
\end{gathered}
$$

where:

$$
\begin{gathered}
\mu_{0}=\mathrm{E}\left[Y \mid X_{1}=0, \ldots, X_{n}=0\right] \\
\mu_{i}=\mathrm{E}\left[Y \mid X_{i}=1, X_{j: j \neq i}=0\right] \quad i=1, \ldots, n
\end{gathered}
$$

If $X_{i}$ is a continuous parent variable, it holds:

$$
\mu_{i}=\mathrm{E}\left[Y \mid X_{i}=1, X_{j: j \neq i}=0\right]=-\mathrm{E}\left[Y \mid X_{i}=-1, X_{j: j \neq i}=0\right]
$$

Parameter $\tau$ is constant across the configuration of parent variables and regulates heteroscedasticity:

$$
\operatorname{Var}\left[Y \mid x_{1}, \ldots, x_{n}\right]=\frac{\left(\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]+1.5\right) \cdot\left(1.5-\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]\right)}{(1+\tau)}
$$

The logit of the expected value of $Y$ can be can be rewritten in terms of parameters $\boldsymbol{\mu}=$ $\left(\mu_{0}, \mu_{1}, \ldots, \mu_{n}\right)$ :

$$
\begin{gathered}
\log \left(\frac{\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]+1.5}{1.5-\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]}\right)=\left(1-\sum_{i=1}^{n} x_{i}\right) \log \left(\frac{\mu_{0}+1.5}{1.5-\mu_{0}}\right)+ \\
+\sum_{i=1}^{n} x_{i} \log \left(\frac{\mu_{i}+1.5}{1.5-\mu_{i}}\right)
\end{gathered}
$$

This way, parameters are expected values conditioned to a configuration of parent variables where all but one take value 0 . A medical expert is expected to be competent in performing quantitative assessments under such parameterization, because, thanks to the rescaling procedure, he/she may refer to the expected value of the response in terms of the relative position within one among n-range, $l p$-range and $h p$-range (Subsection 3.1). Typically, if no relevant parent variables are omitted, the expected value of the response is 0 when all parent variables take value 0 , that is $\mu_{0}=0$ without uncertainty, and equation 14 simplifies into:

$$
\log \left(\frac{\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]+1.5}{1.5-\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]}\right)=\sum_{i=1}^{n} x_{i} \log \left(\frac{\mu_{i}+1.5}{1.5-\mu_{i}}\right)
$$

The prior distribution of parameter $\mu_{i}(i=0,1, \ldots, n)$ is elicited using the Equivalent Prior Sample (EPS) method (Winkler, 1967):

$$
\frac{\mu_{i}+1.5}{3} \sim \operatorname{Beta}\left(\frac{\hat{\mu}_{i}+1.5}{3} \hat{q}_{i},\left(1-\frac{\hat{\mu}_{i}+1.5}{3}\right) \hat{q}_{i}\right)
$$

where $\hat{\mu}_{i}$ is the assessment of $\mu_{i}$ and $\hat{q}_{i}$ is the number of patient cases on which $\hat{\mu}_{i}$ is based. Typically, the expected value of $Y$ is equal to 0 when all parent variables take value 0 , that is parameter $\mu_{0}$ is equal to 0 without uncertainty and Equation 14 simplifies into:

$$
\log \left(\frac{\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]+1.5}{1.5-\mathrm{E}\left[Y \mid x_{1}, \ldots, x_{n}\right]}\right)=\sum_{i=1}^{n} x_{i} \log \left(\frac{\mu_{i}+1.5}{1.5-\mu_{i}}\right)
$$

A default prior distribution $\tau \sim \operatorname{Gamma}(89.4917,2.0304)$ is assigned to the precision parameter, implying a probability between 0.95 and 0.99 for the response to take value in $n$-range, given that all parent variables take value 0 .

# 4. Bayesian estimation of the quantitative part 

Data collected by Squizzato et al. (2011) were exploited to update the joint prior distribution of parameters. Let $\boldsymbol{\theta}$ be the set of parameters induced by conditional models shown in Section 3. Given a dataset of cases $\mathcal{D}$ from the problem domain, the joint prior distribution $p(\boldsymbol{\theta})$ is updated in the Bayesian paradigm by computing the joint posterior distribution $p(\boldsymbol{\theta} \mid \mathcal{D}) \propto p(\mathcal{D} \mid \boldsymbol{\theta}) p(\boldsymbol{\theta})$. Due to the large size of the probabilistic network, direct computation of the joint posterior distribution of parameters is intractable, therefore approximated calculations were performed by means of Markov Chain Monte Carlo (MCMC) simulation.

In the remainder of this section, we provide details on data and MCMC implementation.

# 4.1. Data 

The clinical study described in (Squizzato et al., 2011) gathered a total of 17497 electronic admission records of patients referred to an emergency department for cardiopulmonary disorders and then hospitalised from January to June 2007 in six italian hospitals. A block random sampling design was applied to select 800 hospitalised patients. The randomization blocks were defined by the combination of age categories (less than 30 , between 30 and 60 , over 60 ), gender and four symptoms of pulmonary embolism: acute dyspnea, chest pain, fainting and palpitations. A further block was defined by the presence of either pulmonary embolism, aortic dissection or pneumothorax.

Patients were selected within each block according to the probability of the blocking variables in the whole population. All patients hospitalised for trauma were excluded, leading to a total of 750 eligible records. In our analysis, other 28 patients were excluded because the acute disease was not of cardiopulmonary origin ( 23 patients), the visit in emergency department was planned in advance ( 3 patients), or data were of poor quality ( 2 patients). Baseline clinical characteristics of data are summarized in Table 2.

Table 2: Baseline clinical characteristics of data.


Since hospital patient records are not collected for medical purposes, variables in the categories $V_{Q}$ (pathogenesis), $V_{D}$ (pathology) and $V_{S}$ (pathophysiology) are typically unobserved, and variables in the other categories may have not been reported (missing), either because not of interest or obvious for the physician. In order to reduce the number of missing values, medical experts performed judgements on some unobserved variables on the basis of the diagnosis yielded at hospital discharge, and set explicit criteria to establish which missing data could be safely assumed as neutral values. The frequency distribution of each variable including the percentage of missing values is shown in Appendix .

Overall, 66 variables ( $25 \%$ ) included in the probabilistic network resulted completely unobserved in our dataset, observed variables contained a total of 245 missing values ( $34 \%$ ), for a total of 383 missing values ( $53 \%$ ) among all the variables included in the probabilistic network. Missing values typically arise when either a diagnosis is not available, or the physician decides that a certain ascertainment is not necessary. In the former case, a datum is missing because the observed ones are deemed insufficient by the physician in order to formulate a diagnosis. In the latter case, a datum is missing because the physician believes that a certain ascertainment is irrelevant given of the observed ones. As such, missing values comply with the Missing at Random assumption (MAR, Raghunathan (2004)).

### 4.2. Markov Chain Monte Carlo implementation

A sample from the joint posterior distribution of parameters was obtained using MCMC algorithms available in JAGS (Plummer, March 20-22, 2003). According to the MAR assumption, we ignored the mechanism generating missing values, thus they were treated as unknown variables on the same footing of parameters.

The simulation was run for 55000 iterations, of which the first 30000 were discarded and the others were thinned by an interval of 5 to reduce sample autocorrelation. We applied the Geweke

(Geweke, 1992), Heidelberger-Welch (Heidelberger and Welch, 1983) and Raftery-Lewis (Raftery and Lewis, 1995) diagnostic tests to detect lack of convergence. We obtained that less than $1 \%$ of parameters passed no tests, more than $99 \%$ of parameters passed at least one test, more than $90 \%$ of parameters passed at lest two tests and almost half of the parameters passed all the three tests.

At the end of MCMC simulation, the divergence between the prior and the posterior distribution of each parameter $\theta \in \boldsymbol{\theta}$ was quantified using the following statistic, that we call D-statistic:

$$
\mathrm{D}(\theta)=\frac{1}{S} \sum_{i=1}^{S} I^{(i)}(\theta)
$$

where $I^{(i)}(\theta)$ is a dummy indicator taking value 1 if the $i$-th value of $\theta$ from MCMC simulation is included in the equal-tail $95 \%$ prior credible interval for $\theta$, and $S$ is the length of the MCMC sample. A value of the D-statistic above 0.95 suggests a substantial agreement between the medical experts' belief and data. Values of the D-statistic near 0.95 mean that the medical experts' belief is not updated by data, provided that the posterior distribution is unimodal. Values of the D-statistic below 0.95 indicate an increasing disagreement between the medical experts' belief and data. The maximum disagreement holds for values of the D-statistic near 0 , meaning that the majority of posterior samples is outside the prior $95 \%$ credible interval.

# 5. Illustration 

In this section, we illustrate the elicitation task for two variables in the probabilistic network: 'Bradycardia/Tachycardia' and 'Heart rate', and compare the resulting marginal prior distributions with the marginal posterior distributions obtained from MCMC simulation.

### 5.1. Bradycardia/Tachycardia

'Bradycardia/Tachycardia' is a categorical variable with sample space \{'absent', 'bradycardia', 'moderate tachycardia', 'severe tachycardia'\} representing the absence or the presence of bradycardia and/or tachycardia in a patient. Its parent variables are 'Heart drive', hyper-restricted continuous variable here indicated as $X_{1}$, and 'Dehydration', hyper-restricted continuous variable here indicated as $X_{2}$.

The probability distribution of 'Bradycardia/Tachycardia' was defined by applying the Beta regression model explained in Subsection 3.2: The elicited prior distribution of parameters was:

$$
\begin{aligned}
& \left(\pi_{0,0}, \pi_{0,1}, \pi_{0,2}, \pi_{0,3}\right) \sim \operatorname{Dirichlet}(3.88,1.03,0.00,1.09) \\
& \left(\pi_{1,0}, \pi_{1,1}, \pi_{1,2}, \pi_{1,3}\right) \sim \operatorname{Dirichlet}(3.10,1.30,1.04,1.55) \\
& \left(\pi_{2,0}, \pi_{2,1}, \pi_{2,2}, \pi_{2,3}\right) \sim \operatorname{Dirichlet}(2.50,1.15,2.05,1.30)
\end{aligned}
$$

In Figure 2, marginal prior distribution and kernel density estimate of marginal posterior distribution of model parameters are shown. The summary of marginal prior and posterior distribution of parameters is provided in Table 3.

### 5.2. Heart rate

'Heart rate' is a continuous variable measuring the heart rate in a patient. Its parent variables are 'Autonomic nervous system status', a categorical variable with sample space \{'regular', 'moderate adrenergic status', 'severe adrenergic status', 'hypertensive crisis', 'moderate cholinergic status', 'severe cholinergic status'], representing the status of autonomic nervous system in a patient, and 'Bradycardia/Tachycardia', described above. Since both parents are categorical variables with more than one non-neutral category, they are replaced by dummy indicators: $X_{1}$, $X_{2}, X_{3}, X_{4}$ and $X_{5}$ represent the non-neutral categories of 'Heart rate', while $X_{6}, X_{7}$ and $X_{8}$ represent the non-neutral categories of 'Bradycardia/Tachycardia'.

The probability distribution of 'Heart rate' was defined by applying the Beta regression model explained in Subsection 3.3: The elicited prior distribution of parameters was:

Table 3: Summary of marginal prior and posterior probability density of parameters defining the conditional model of ‘Bradycardia/Tachycardia’. ‘Std. dev.’: standard deviation. ‘95% QI’: 95% quantile interval.


![img-1.jpeg](img-1.jpeg)

Figure 2: Marginal probability density of parameters defining the conditional model of ‘Bradycardia/Tachycardia’. Straight lines: posterior probability density. Dotted lines: prior probability density. The D-statistic value is shown below the title.

$$
\begin{gathered}
\frac{\mu_{0}+1.5}{3} \sim \delta(0.5) \\
\frac{\mu_{1}+1.5}{3} \sim \operatorname{Beta}(3.9187,1.0813) \\
\frac{\mu_{2}+1.5}{3} \sim \operatorname{Beta}(4.1667,0.8333) \\
\frac{\mu_{3}+1.5}{3} \sim \delta(0.5) \\
\frac{\mu_{4}+1.5}{3} \sim \operatorname{Beta}(1.0813,3.9187) \\
\frac{\mu_{5}+1.5}{3} \sim \operatorname{Beta}(0.8333,4.1667) \\
\frac{\mu_{6}+1.5}{3} \sim \operatorname{Beta}(0.8333,4.1667) \\
\frac{\mu_{7}+1.5}{3} \sim \operatorname{Beta}(3.9187,1.0813) \\
\frac{\mu_{8}+1.5}{3} \sim \operatorname{Beta}(4.1667,0.8333) \\
\tau \sim \operatorname{Gamma}(89.4917,2.0304)
\end{gathered}
$$

where $\delta$ denotes a degenerated distribution (Dirac delta function). In Figure 3, marginal prior distribution and kernel density estimate of marginal posterior distribution of model parameters are shown. The summary of marginal prior and posterior distribution of parameters is provided in Table 4.

Table 4: Summary of marginal prior and posterior probability density of parameters defining the conditional model of 'Heart rate'. 'Std. dev.': standard deviation. ' $95 \%$ QI': $95 \%$ quantile interval.


# 6. Refinement 

After MCMC simulation, we implemented the probabilistic network in GeNle (Druzdzel, 1999) by discretizing continuous variables into 5 categories and by computing CPTs at the posterior mean of parameters. Afterwards, we performed two types of evaluation. The first evaluation involved the Concordance Index for all variables included in the category $V_{D}$ (pathophysiology) with more than one quarter of observed values and a percentage of non-neutral values greater than $5 \%$ (see Table 6). The Concordance Index is defined as the proportion of patients (judged as) affected by the disease with a predicted risk greater than any patient not affected by the disease, thus value 1 indicates perfect discrimination of the judgement. It was computed by considering data on clinical presentation only, and by considering all the available patient data. The second evaluation involved the inference performed by the probabilistic network on six fictitious patient cases elaborated by the second author. These patient cases are described in Appendix . If medical experts judged Concordance Index values and diagnoses satisfactory, the refinement process ended, otherwise medical experts were invited to detect eventual inconsistencies with medical causal knowledge in

![img-2.jpeg](img-2.jpeg)

Figure 3: Marginal probability density of parameters defining the conditional model of 'Heart rate'. Straight lines: posterior probability density. Dotted lines: prior probability density. The D-statistic value is shown below the title.

the qualitative part. In this task, anchoring to parameters with a D-statistic value less than 0.01 was of great help for medical experts, because an unsatisfactory diagnostic performance of the probabilistic network often occurred together with a strong divergence between the prior and the posterior distribution of one or more parameters. After that inconsistencies in the qualitative part were detected, they were fixed and both elicitation and MCMC simulation were repeated accordingly.

After refinement, our probabilistic network consisted of 262 variables, 574 edges and 959 parameters. The frequency distribution of the D-statistic after refinement is shown in Table 5.

Table 5: Frequency distribution of the D-statistic after refinement.


Table 7 shows the estimation and 95% confidence interval (computed by bootstrapping) of the Concordance Index for the selected acute diseases after refinement. When considering data on clinical presentation only, Concordance Index values are near or above 0.8, suggesting a good diagnostic performance (Steyerberg et al., 2010). When considering all the available patient data, Concordance Index values are above 0.94, confirming a substantial consistency between prior knowledge encoded in the probabilistic network and data.

Inference performed by the probabilistic network on the six fictitious patient cases after refinement.

Table 6: Selected acute diseases. $N_{0}$ : number of patients without the disease. $N_{1}$ : number of patients with the disease. 'Total': number of patients on which the judgement was performed.


Table 7: Concordance Index values for the selected of acute diseases after refinement. $95 \%$ confidence intervals are computed by bootstrapping.


ment is shown in Appendix .

# 7. Discussion 

In this paper, we described our experience in the development of a probabilistic network for the diagnosis of acute cardiopulmonary diseases.

In existing medical applications of probabilistic networks, the qualitative part is often specified on the grounds of causal knowledge documented in the specialised literature. Several advantages result from this causal formulation. First, medical experts are able to understand and discuss the information coded in the directed acyclic graph (DAG), because it is expressed through notions provided in standard medical training. Second, it is widely recognized that the causal formulation of DAGs often simplifies their specification (e.g., *Koller and Friedman (2009)*, page 1009). Third, causal DAGs are often characterized by a relatively small number of edges while the same DAGs modified through arc reversal operations typically contain more edges (for example, see *Buntine (1994)*, Figure 16). A comprehensive account of causal modelling is provided in *Pearl (2009)*. In our work, we anchored the specification of the qualitative part of the probabilistic network to the maximal constraint DAG, a representation of equivalence classes of DAGs induced by relationships among medical variables commonly accepted by physicians (see the discussion in *Luciani and Stefanini (2012)*).

A second innovative aspect of our work is represented by the use of both expert knowledge and patient data to estimate the quantitative part of the probabilistic network. This approach is quite uncommon in the literature, where, to our best knowledge, only one of the two sources of information is typically exploited. Remarkable applications include the Bayesian network developed by Kline et al. (2005), and the expert systems DIAVAL (Díez et al., 1997) and HEPAR II (Wasyluk et al., 2001). However, in the first work,a very small set of diseases is considered and no prior information is exploited, as a consequence the DAG results highly connected and estimates of parameters are characterized by a large variance. In the other two works, hundreds of variables are considered, but expert knowledge is exploited only in the specification of the qualitative part, while the quantitative part is estimated from patient data only after continuous variables underwent to discretization. In our proposal, discretization of continuous variables is avoided by applying an original formal representation to the quantitative part, consisting in a combination of the Beta regression and the categorical logistic regression, reparameterized to help physicians in performing quantitative assessments competently. This way, the dimensionality of the quantitative part was reduced to less than one thousand parameters for more than 260 variables, and medical experts were able to interpret parameters with no additional training besides the standard medical one. Furthermore, they were satisfied for the possibility to express uncertainty in terms of the sample size of pertaining clinical studies or, when unavailable, in terms of the number of patient cases they experienced. If this was the case, medical experts paid attention to assess a number of patient cases substantially lower than the one typically handled by clinical studies, in fulfillment of principles of the Evidence-Based Medicine (EBM) paradigm (Guyatt et al., 1992).

Almost a quarter of variables included in the probabilistic network was completely unobserved in our database, while the mean percentage of missing values for those observed was $34 \%$, for a total of $53 \%$ missing values among all the variables included in the probabilistic network. Parameter estimation with unobserved variables is typically challenging, as the related probability distributions could not be consistently inferred from collected data (Settimi and Smith, 1998). However, when the joint prior distribution of parameters is informative like in our work, Bayesian estimation is possible, and it is typically performed by Markov Chain Monte Carlo (MCMC) simulation. In this case, the marginal prior distribution of some parameters remains unaltered after conditioning to collected data. (Gustafson, 2015).

The combination of two sources of information in MCMC simulation, that is quantitative beliefs from experts and data, helped medical experts in refining the probabilistic network. During refinement, we often found that unsatisfactory Concordance Index values for a selection of acute diseases and/or unreasonable inference on six fictitious patient cases occurred together with a strong divergence between the prior and the posterior distribution of one or more parameters (low value of the D-statistic).

After refinement, the probabilistic network consisted of 262 variables, 574 edges and 959 parameters. In particular, it can be employed to perform medical diagnosis on a total of 63 diseases ( 38 acute and 25 chronic) on the basis of up to 167 patient findings. The large set of diseases included in the probabilistic network highlights a further important feature of our work. On one hand, this may be of help to prompt events not considered by physicians, like rare diseases. On the other hand, it may improve the diagnosis for patients with an atypical presentation.

The refinement process ended after that the probabilistic network provided satisfactory Concordance Index values for a selection of acute diseases and after obtaining plausible inferences on six fictitious patient cases. Nevertheless, the empirical validation of its diagnostic performance remains a mandatory objective before it may be used to support decision making in a production environment. At this purpose, future work will include an evaluation of the probabilistic network based on data perspectively collected.

# Acknowledgments 

We thank Alessandro Squizzato, Andrea Rubboli, Leonardo Di Gennaro, Raffaele Landolfi, Carlo De Luca, Fernando Porro, Marco Moia, Sophie Testa, Davide Imberti and Guido Bertolini for their contribution. This work was partially supported by the University of Florence, funding framework Progetto strategico di ricerca di base per l'anno 2015, grant Disegno e analisi di studi sperimentali e osservazionali per le decisioni in ambito epidemiologico, socio-economico, ambientale

$e$ tecnologico. The authors declare that there are no conflicts of interest. Financial disclosure: Sanofi-Aventis financially supported data collection.

# Appendix 1. Fictitious patient cases 

Case 1. A 73 years old man complained of mild fever and shortness of breath. He had a history of chronic obstructive pulmonary disease and a myocardial infarction ten years before. On examination, he revealed bronchospasm and crackles in the lower third of the lung. Arterial pressure was $150 / 90 \mathrm{mmHg}$, heart rate 120 bpm . The electrocardiogram showed a supraventricular arrithmya apparently never occurred before. On blood gas-analysis, oxygen saturation was $93 \%$ after $4 \mathrm{~L} / \mathrm{min}$ of oxygen, and carbon dioxide arterial partial pressure was 50 mmHg . Chest X-rays showed signs of pulmonary condensation.

Case 2. A 45 years old woman complained of acute chest pain and shortness of breath. On examination, arterial pressure was $100 / 70 \mathrm{mmHg}$ and heart rate was 90 bpm . On blood gasanalysis, oxygen saturation was $94 \%$ and carbon dioxide arterial partial pressure was 34 mmHg . Contraceptive pill apart, she did no take any drug, but she had a smoker habit. The D-dimer test was positive and the blood count was normal. Chest X-rays revealed no anomalies.

Case 3. A 67 years old man, with chronic arterial hypertension and smoking habit, suffered of oppressive chest pain, along with sweetness and paleness. His arterial pressure was $110 / 80 \mathrm{mmHg}$ and heart rate was 90 bpm . Laboratory tests showed a mild leucocytosis and abnormal Troponin I. Chest X-rays was normal.

Case 4. A 63 years old man with a long standing diabetes referred to be recently collapsed. On examination, glycemia was $145 \mathrm{mg} / \mathrm{dl}$, heart rate was 110 bpm , arterial pressure was $100 / 60 \mathrm{mmHg}$ and chest X-rays was normal. The electrocardiogram revealed a right bundle block and sign of axis deviation. The D-dimer test was positive and blood gas-analysis showed an oxygen arterial partial pressure of 85 mmHg and a carbon dioxide arterial partial pressure of 30 mmHg .

Case 5. A 50 years old man complained of fever since 3-4 days. He had a mild cough and, more recently, he was affected by mild confusion. On examination, arterial pressure was $100 / 70 \mathrm{mmHg}$ and heart rate was 100 bpm . On blood gas-analysis, oxygen saturation was $93 \%$ and hypocapnya (carbon dioxide arterial partial pressure was 30 mmHg ). Other laboratory tests showed normal hemoglobin, mild leucocytosis and a mild increment of serum creatinine. Chest X-rays showed an increment of the interstitial pulmonary net.

Case 6. A 85 years old woman, with cardiopathy, atrial fibrillation, diabetes and chronic renal failure, complained of acute shortness of breath. On the laboratory tests, Brain Natriuretic Peptide was $200 \mathrm{pg} / \mathrm{mL}$, Troponin I was. $5 \mathrm{mg} / \mathrm{dL}$ and serum creatinine was $1.9 \mathrm{mg} / \mathrm{dL}$. Heart rate was 98 bpm , oxygen saturation was $94 \%$ after administration of $2 \mathrm{~L} / \mathrm{min}$ of oxygen. On examination, crepitations emerged at the pulmonary basis, confirmed by signs of pulmonary congestion at the chest X-rays. On blood gas analysis, carbon dioxide arterial partial pressure was 70 mmHg .

Table 8: Inference performed by the probabilistic network on the six fictitious patient cases after refinement. Values represent probabilities.


Table 8 shows the diagnosis on the the six fictitious patient cases performed by the probabilistic network after refinement.

In case 1, pneumonia appears the most likely hypothesis, supported by the occurrence of fever, pulmonary crackles on auscultation and, above all, consolidation in the chest film. Absence of cough would represent an atypical finding, although the symptom may have not been reported because deemed obvious in patients affected by chronic obstructive pulmonary disease. A cardiogenic pulmonary edema may also have occurred at this age, particularly in the light of a past episode of ischemic heart disease. Furthermore, the reported onset of supraventricular arrithmya may have easily triggered congestive heart failure. A chronic obstructive pulmonary disease exacerbation is likely to coexist with both diagnostic hypotheses.

In case 2, pulmonary embolism is the most likely diagnosis, due to the presence of a risk factor (oestrogen assumption) combined with respiratory symptoms. Nonetheless, the smoking habit and middle age of the patient also make an acute coronary event and a subsequent myocardial infarction possible.

In case 3, the presentation immediately reminds of cases with acute myocardial infarction, as attested by the chest symptoms and the laboratory findings. However, the model does not forget to remind of the existence of rarer conditions, like pulmonary embolism.

In case 4, after that electrocardiographic findings reveal a right axis deviation, the diagnosis is correctly oriented towards pulmonary embolism.

In case 5, the shortness of breath, together with the low oxygen saturation and the increment of the interstitial pulmonary net, makes pulmonary edema a likely hypothesis, possibly explained as the effect of an acute heart failure. Nonetheless, other diagnostic hypotheses cannot be dismissed, particularly pneumonia, which could justify the state of confusion, although similar consequences on patient's awareness may be referred to the low oxygen saturation.

In case 6, acute heart failure is by far the most likely explanation of worsening dyspnea due to chronic heart disease. As a secondary complicating disorder, pulmonary edema is suggested by chest X-rays and the pulmonary crepitations on auscultation. Underlying causes may encompass acute myocardial infarction, despite the absence of chest pain, particularly because the patient is diabetic and troponin levels are higher than normal. However, elevated troponin levels may be explained by other hypotheses, like a sustained tachycardia, although heart rate was not extremely higher than normal at the time of visit.

# Appendix 2. Parent set, typology and frequency distribution for each variable 

Each variable included in the probabilistic network is listed below alphabetically, together with its typology (within round brackets), relative frequency distribution (within square brackets) and parent set (after colons). The symbol '-' indicates that a variable has no parent variables.

Abnormal ventilation trigger (Pathophysiology, multi-valued) [absent: $0 \%$, present (hypo): $0 \%$, present (hyper): $0 \%$, missing: $100 \%$ ]: Pneumonia, Pulmonary edema, Pulmonary emphysema, Pulmonary venous thrombo-embolism.
Acute anemia (Pathology, binary) [absent: $96.4 \%$, present: $1.8 \%$, missing: $1.8 \%$ ]: Hemorrhage.
Acute aortic valve failure (Pathophysiology, binary) [absent: $15.51 \%$, present: $0.14 \%$, missing: $84.35 \%$ ]: Aortic dissection, Dilated cardiomyopathy, Endocarditis.
Acute atrial arrhythmia (Pathology, binary) [absent: $38.37 \%$, present: $4.29 \%$, missing: $57.34 \%$ ]: Bradycardia/Tachycardia, Chronic atrial arrhythmia.
Acute cerebro-vascular disease (Pathology, binary) [absent: $77.15 \%$, present: $2.22 \%$, missing: $20.64 \%$ ]: Arterial embolism, Arterial intra-vascular coagulation, Autonomic nervous system status, Chronic cerebro-vascular disease, Prophylaxis/anticoagulation.
Acute coronary event (Pathology, binary) [absent: $26.45 \%$, present: $10.11 \%$, missing: $63.43 \%$ ]: Arterial intra-vascular coagulation, Chronic cardiac muscle disease, Cocaine/amphetamines use, Right heart output.
Acute mitral valve failure (Pathophysiology, binary) [absent: $17.59 \%$, present: $0.69 \%$, missing: $81.72 \%$ ]: Acute mitral valve prolapse, Acute myocardial infarction, Dilated cardiomyopathy, Endocarditis.
Acute mitral valve prolapse (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Acute myocardial infarction.
Acute myocardial infarction (Pathology, multi-valued) [absent: $0 \%$, moderate: $0 \%$, severe: $0 \%$, missing: $100 \%$ ]: Acute coronary event, Myocarditis.
Acute pulmonary disease (Pathophysiology, multi-valued) [absent: $73.55 \%$, initial: $4.02 \%$, advanced: $1.39 \%$, cardiac (asthma): $5.12 \%$, missing: $15.93 \%$ ]: Ashtma, Left heart pump, Lung cancer, Pneumonia, Pulmonary emphysema, Upper airways infection.
Acute respiratory distress syndrome (Pathology, binary) [absent: $62.19 \%$, present: $0.55 \%$, missing: $37.26 \%$ ]: Lung cancer, Pancreatitis, Pneumonia, Pulmonary infarction, Sepsis.
Age (years old) (Epidemiology, continuous) [<25: $0 \%, 25-34: 0 \%, 35-44: 0 \%, 45-54: 0 \%, 55-64$ : $0 \%, 65-74: 0 \%, 75-84: 0 \%, 85-94: 0 \%, 95-104: 0 \%,>105: 0 \%$, missing: $100 \%$ ]: -
Air bronchogram (Semiotics (other), binary) [absent: $15.79 \%$, present: $0.69 \%$, missing: $83.52 \%$ ]: Pulmonary consolidation.
Air trapping (Semiotics (other), binary) [absent: $15.65 \%$, present: $0.69 \%$, missing: $83.66 \%$ ]: Pulmonary emphysema.
Alcoholism (Aetiology, binary) [absent: $95.71 \%$, present: $3.19 \%$, missing: $1.11 \%$ ]: Age (years old).
Amylase (Semiotics (other), binary) [normal: $56.37 \%$, augmented: $3.74 \%$, missing: $39.89 \%$ ]: Pancreatitis.
Anisosfigmia (Semiotics (other), binary) [absent: $45.57 \%$, present: $0.28 \%$, missing: $54.16 \%$ ]: Aortic dissection.
Anti-inflammatory drugs recent intake (Aetiology, binary) [no: $34.76 \%$, yes: $5.12 \%$, missing: $60.11 \%$ ]: Bacterial infection, Non-bacterial infection.
Antiphospholipids (Semiotics (other), binary) [absent: $2.22 \%$, present: $0.28 \%$, missing: $97.51 \%$ ]: Thrombophilia.
Antithrombin III (Semiotics (other), binary) [normal: $6.93 \%$, deficit: $0.69 \%$, missing: $92.38 \%$ ]: Thrombophilia.
Anxiety/agitation (Pathophysiology, multi-valued) [absent: $0 \%$, moderate: $0 \%$, severe: $0 \%$, missing: $100 \%$ ]: Chest pain, Hypoglycemia.
Anxiety/agitation (according to clinical judgement) (Semiotics (other), binary) [absent: $92.24 \%$, present: $6.65 \%$, missing: $1.11 \%$ ]: Anxiety/agitation.
Aortic aneurysm (Epidemiology, binary) [absent: $85.18 \%$, present: $5.68 \%$, missing: $9.14 \%$ ]: Age (years old), Chronic arterial hypertension, Gender.
Aortic dissection (Pathology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Age (years old), Aortic aneurysm, Gender.
Aortic intramural hematoma (Semiotics (other), binary) [absent: $49.17 \%$, present: $0 \%$, missing: $50.83 \%$ ]: Aortic dissection.
Aortic stenosis (Semiotics (other), binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: -
Aortic valve failure (Semiotics (other), binary) [absent: $28.95 \%$, present: $11.91 \%$, missing: $59.14 \%$ ]: Acute aortic valve failure, Chronic aortic valve failure.

Arterial embolism (Pathogenesis, binary) [absent: 0\%, present: 0\%, missing: 100\%]: Arterial intra-vascular coagulation, Patent foramen ovale, Pulmonary venous thrombo-embolism.
Arterial intra-vascular coagulation (Pathogenesis, multi-valued) [absent: $0 \%$, coronaric: $1.52 \%$, cerebral: $0.42 \%$, left (heart): $0 \%$, mixed: $0 \%$, missing: $98.06 \%$ ]: Aortic dissection, Chronic atrial arrhythmia, Chronic cardiac muscle disease, Intra-vascular coagulation, Pancreatitis.
Arterial vascular resistance (Pathophysiology, continuous) [lp-range: $0 \%$, n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Autonomic nervous system status, Chronic arterial hypertension, Left heart pump.
Ascending aorta intimal flap (Semiotics (other), binary) [absent: $49.31 \%$, present: $0 \%$, missing: $50.69 \%$ ]: Aortic dissection.
Ashtma (Pathology, binary) [absent: $78.53 \%$, present: $1.8 \%$, missing: $19.67 \%$ ]: Age (years old), Gender.
Atelactasis (Semiotics (other), binary) [absent: $88.64 \%$, present: $6.23 \%$, missing: $5.12 \%$ ]: Acute respiratory distress syndrome, Lung cancer, Pulmonary consolidation, Spontaneous pneumothorax.
Atrial arrhythmia (Semiotics (other), binary) [absent: $72.44 \%$, present: $26.45 \%$, missing: $1.11 \%$ ]: Acute atrial arrhythmia, Chronic atrial arrhythmia.
Augmented lactates (according to clinical judgment) (Semiotics (other), binary) [no: $70.5 \%$, yes: $4.43 \%$, missing: $25.07 \%$ ]: Lactates ( $\mathrm{mmol} / \mathrm{l}$ ).
Autonomic nervous system status (Pathophysiology, multi-valued) [normal: $5.26 \%$, adrenergic (1): $0 \%$, adrenergic (2): $0 \%$, hypertensive (crisis): $1.25 \%$, cholinergic (1): $0 \%$, cholinergic (2): $0 \%$, missing: $93.49 \%$ ]: Acute coronary event, Acute myocardial infarction, Acute pulmonary disease, Anxiety/agitation, Chronic cardiac muscle disease, Heart drive, Left heart pump, Right heart output, Sepsis.
Bacterial infection (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Cholecystitis, Endocarditis, Immunocompromission, Myocarditis, Non-infarctual pericarditis, Pancreatitis, Peritonitis, Pneumonia, Pulmonary infarction, Sepsis.
Bias of perfusion scintigraphy (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Atelactasis, Pleural effusion, Pulmonary consolidation, Pulmonary opacity.
Biliary colic (Semiotics (other), binary) [absent: $96.12 \%$, present: $1.8 \%$, missing: $2.08 \%$ ]: Cholelithiasis.
Blood pressure ( mmHg ) (Semiotics (other), continuous) [lp-range: $7.89 \%$, n-range: $43.49 \%$, hprange: $47.23 \%$, missing: $1.39 \%$ ]: Arterial vascular resistance, Left cardiac output.
Bradycardia/Tachycardia (Pathology, multi-valued) [absent: $64.13 \%$, bradycardia: $1.66 \%$, tachycardia (1): $3.32 \%$, tachycardia (2): $3.6 \%$, missing: $27.29 \%$ ]: Dehydration, Heart drive.
Brain natriuretic peptide (Semiotics (other), binary) [normal: $0.28 \%$, augmented: $1.52 \%$, missing: $98.2 \%$ ]: Left heart pump.
Bronchial diameter (Semiotics (other), binary) [normal: $14.68 \%$, reduced: $0.42 \%$, missing: $84.9 \%$ ]: Pulmonary emphysema.
Bronchial walls (Semiotics (other), binary) [normal: $13.99 \%$, tickened: $1.39 \%$, missing: $84.63 \%$ ]: Pulmonary emphysema.
Bronchiectasis (Semiotics (other), binary) [absent: $78.12 \%$, present: $1.8 \%$, missing: $20.08 \%$ ]: Pulmonary emphysema.
Bronchospasm/reduced vescicolar murmur (Semiotics (other), multi-valued) [normal: $76.04 \%$, rhonchi (or wheezing): $19.25 \%$, silence: $2.08 \%$, missing: $2.63 \%$ ]: Acute pulmonary disease, Pulmonary emphysema, Pulmonary venous thrombo-embolism, Spontaneous pneumothorax, Upper airways infection.
Cardiac axis right deviation (S1-Q3-T3) (Semiotics (other), binary) [absent: $90.58 \%$, present: $5.12 \%$, missing: $4.29 \%$ : ECG right heart findings.
Cardiac tamponade (Pathophysiology, multi-valued) [absent: $0 \%$, moderate: $0 \%$, severe: $0 \%$, missing: $100 \%$ ]: Hemopericardium, Pericarditis.
Cardiomegaly (Semiotics (other), binary) [absent: $55.96 \%$, present: $31.99 \%$, missing: $12.05 \%$ ]: Chronic cardiac muscle disease, Left heart pump, Pericardial effusion.
Carotid sinus massage test (Semiotics (other), binary) [negative: $0.28 \%$, positive: $0.69 \%$, missing: $99.03 \%$ : Sick sinus syndrome.

Cavitation/Colliquation (Semiotics (other), binary) [absent: $15.65 \%$, present: $0.14 \%$, missing: $84.21 \%$ ]: Pneumonia.
Central cyanosis (Semiotics (other), binary) [absent: $34.35 \%$, present: $0.55 \%$, missing: $65.1 \%$ ]: Oxygen saturation (percentage).
Central line (Aetiology, binary) [no: $97.78 \%$, yes: $2.22 \%$, missing: $0 \%$ ]: -
Central mass (thoracic) (Semiotics (other), binary) [absent: $88.09 \%$, present: $3.05 \%$, missing: $8.86 \%$ ]: Lung cancer.
Cerebral hypoxia (Pathophysiology, multi-valued) [absent: $0 \%$, recently occurred: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Acute anemia, Acute atrial arrhythmia, Acute cerebro-vascular disease, Dehydration, Left cardiac output, Obstruction of the systemic circulation, Sick sinus syndrome, Temporary suspension of heart drive, Vasovagal syncope.
Cerebral mass (Pathophysiology, binary) [absent: $70.91 \%$, present: $0.69 \%$, missing: $28.39 \%$ ]: Acute cerebro-vascular disease, Neoplastic disease (generic).
Chest pain (Semiotics (other), binary) [absent: $39.47 \%$, present: $47.09 \%$, missing: $13.43 \%$ ]: Chest pain type.
Chest pain (gastro-oesophageal origin) (Pathophysiology, binary) [absent: $93.91 \%$, present: $0.28 \%$, missing: $5.82 \%$ ]: Gastro-oesophageal reflux, Hiatal hernia, Mallory-Weiss syndrome.
Chest pain (parietal origin) (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Costochondritis, Herpes Zooster, Lower limbs fractures, Lung cancer, Pneumonia, Rib fracture, Spontaneous pneumothorax.
Chest pain (pleuritic origin) (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Costochondritis, Lower limbs fractures, Pleurisy, Pneumonia, Spontaneous pneumothorax.
Chest pain (retro-sternal origin) (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Aortic dissection, Chest pain (gastro-oesophageal origin), Chronic mitral valve prolapse, Dilatated pulmonary artery disease, Obstructive cardiomyopathy, Pericarditis, Pneumonia.
Chest pain (stabbing origin) (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Aortic dissection, Spontaneous pneumothorax.
Chest pain (upper-abdominal origin) (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Biliary colic, Chest pain (gastro-oesophageal origin), Pancreatitis, Peptic ulcer, Peritonitis.
Chest pain type (Semiotics (other), multi-valued) [absent: $39.75 \%$, stabbing: $1.8 \%$, retro (sternal): $21.61 \%$, pleuritic: $7.76 \%$, upper (abdominal): $4.85 \%$, parietal: $4.71 \%$, missing: $19.53 \%$ ]: Acute coronary event, Chest pain (parietal origin), Chest pain (pleuritic origin), Chest pain (retrosternal origin), Chest pain (stabbing origin), Chest pain (upper-abdominal origin).
Cholecystitis (Pathology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Cholelithiasis.
Cholelithiasis (Epidemiology, binary) [absent: $69.94 \%$, present: $4.85 \%$, missing: $25.21 \%$ ]: Age (years old), Gender, Obesity (Body Mass Index $>=30$ ).
Chronic anemia (Epidemiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Age (years old), Fertility.
Chronic aortic valve failure (Epidemiology, multi-valued) [absent: $0 \%$, initial: $0 \%$, advanced: $0 \%$, missing: $100 \%$ ]: Age (years old), Aortic aneurysm, Dilated cardiomyopathy.
Chronic arterial hypertension (Epidemiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Age (years old), Gender, Obesity (Body Mass Index $>=30$ ), Smoker.
Chronic atrial arrhythmia (Epidemiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Age (years old), Chronic cardiac muscle disease, Pulmonary emphysema.
Chronic cardiac muscle disease (Epidemiology, multi-valued) [absent: $0 \%$, initial: $0 \%$, advanced: $0 \%$, missing: $100 \%$ ]: Age (years old), Chronic arterial hypertension, Cor pulmonale, Dilated cardiomyopathy, Gender, Left ventricular hypertrophy.
Chronic cerebro-vascular disease (Epidemiology, binary) [absent: $35.6 \%$, present: $0.69 \%$, missing: $63.71 \%$ ]: Age (years old), Chronic arterial hypertension.
Chronic interstitial lung disease (Epidemiology, binary) [absent: $37.26 \%$, present: $0.28 \%$, missing: $62.47 \%$ ]: Age (years old).
Chronic metabolic alkalosis (Epidemiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Age (years old).
Chronic mitral valve failure (Epidemiology, multi-valued) [absent: $0 \%$, initial: $0 \%$, advanced: $0 \%$, missing: $100 \%$ ]: Age (years old), Aortic stenosis, Chronic aortic valve failure, Chronic mitral

valve prolapse, Dilated cardiomyopathy.
Chronic mitral valve prolapse (Epidemiology, binary) [absent: 0\%, present: 0\%, missing: 100\%]: -
Chronic obstructive pulmonary disease (Semiotics (other), multi-valued) [absent: $75.62 \%$, initial: $16.07 \%$, advanced: $0.97 \%$, missing: $7.34 \%$ ]: Pulmonary emphysema.
Chronic venous insufficiency (Aetiology, binary) [absent: $63.43 \%$, present: $9.56 \%$, missing: $27.01 \%$ ]: Age (years old), Gender.
$C K-M B$ (Semiotics (other), binary) [normal: $29.5 \%$, augmented: $10.25 \%$, missing: $60.25 \%$ ]: Acute myocardial infarction.
Cocaine/amphetamines use (Aetiology, binary) [no: $97.92 \%$, yes: $0.69 \%$, missing: $1.39 \%$ ]: -
Compression stockings (Epidemiology, binary) [no: $98.75 \%$, yes: $1.25 \%$, missing: $0 \%$ ]: Surgery.
Confusion (Semiotics (other), binary) [absent: $92.66 \%$, present: $7.34 \%$, missing: $0 \%$ ]: Glasgow Coma Scale, Previous transient seizure.
Cor pulmonale (Epidemiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Pulmonary hypertension.
Costochondritis (Pathology, binary) [absent: $75.62 \%$, present: $0.14 \%$, missing: $24.24 \%$ ]: -
Cough (Semiotics (other), multi-valued) [absent: $84.63 \%$, dry: $6.37 \%$, productive: $9 \%$, missing: $0 \%$ ]: Acute pulmonary disease, Pleurisy, Pneumonia, Pulmonary edema, Pulmonary emphysema, Upper airways infection.
Cystic areas /Bullae (Semiotics (other), binary) [absent: $13.99 \%$, present: $1.52 \%$, missing: $84.49 \%$ ]: Pulmonary emphysema.
D-dimer test (Semiotics (other), binary) [negative: $17.87 \%$, positive: $20.78 \%$, missing: $61.36 \%$ ]: Age (years old), Fibrinolysis, Pregnancy, Prophylaxis/anti- coagulation.
Dehydration (Pathophysiology, continuous) [n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Pancreatitis, Sepsis.
Dilatated pulmonary artery disease (Pathophysiology, multi-valued) [absent: $0 \%$, acute: $0 \%$, chronic: $0 \%$, missing: $100 \%$ ]: Pulmonary hypertension, Pulmonary venous thrombo-embolism.
Dilated ascending aorta (Semiotics (other), binary) [absent: $85.18 \%$, present: $5.68 \%$, missing: $9.14 \%$ ]: Aortic aneurysm.
Dilated cardiomyopathy (Pathology, binary) [absent: $29.22 \%$, present: $1.11 \%$, missing: $69.67 \%$ ]: Age (years old), Gender.
Dilated left ventricle (Semiotics (other), binary) [absent: $31.44 \%$, present: $8.03 \%$, missing: $60.53 \%$ ]: Dilated cardiomyopathy, Left ventricular pre-load, Myocarditis.
Dilated pulmonary artery (Semiotics (other), binary) [negative: $41.14 \%$, positive: $1.39 \%$, missing: $57.48 \%$ ]: Dilatated pulmonary artery disease.
Dilated right ventricle (Semiotics (other), binary) [absent: $37.53 \%$, present: $5.26 \%$, missing: $57.2 \%$ ]: Cardiac tamponade, Dilated cardiomyopathy, Right heart pre-load.
Dyspepsia (Pathophysiology, multi-valued) [absent: $0 \%$, moderate: $0 \%$, severe: $0 \%$, missing: $100 \%$ ]: Acute myocardial infarction, Biliary colic, Gastro-oesophageal reflux, Peptic ulcer.
Dyspnea (Semiotics (future), binary) [absent: $29.5 \%$, present: $49.58 \%$, missing: $20.91 \%$ ]: Acute anemia, Anxiety/agitation, Lactates (mmol/l), Lung perfusion, Pulmonary shunt.
ECG right heart findings (Pathophysiology, binary) [absent: $75.48 \%$, present: $12.05 \%$, missing: $12.47 \%$ ]: Acute coronary event, Right heart pre-load.
Elevated hemidiaphragm (Semiotics (other), binary) [absent: $89.2 \%$, present: $5.68 \%$, missing: $5.12 \%$ ]: Atelactasis, Pulmonary infarction.
Endocardial vegetations (Semiotics (other), binary) [absent: $43.63 \%$, present: $0.28 \%$, missing: $56.09 \%$ ]: Endocarditis.
Endocarditis (Pathology, binary) [absent: $18.42 \%$, present: $0.28 \%$, missing: $81.3 \%$ ]: -
Endoluminal thrombus (Semiotics (other), multi-valued) [normal: $8.17 \%$, subsegmental (arteries): $3.88 \%$, segmental (arteries): $4.43 \%$, missing: $83.52 \%$ ]: Pulmonary venous thrombo-embolism.
Extrasystoles (Semiotics (other), binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Chronic mitral valve prolapse, Ventricular arrhythmia.
Extrogens use (Aetiology, binary) [no: $98.48 \%$, yes: $1.52 \%$, missing: $0 \%$ ]: Fertility.
Factor II G20210A (Semiotics (other), binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Thrombophilia.
Factor VIII (Semiotics (other), binary) [normal: $0 \%$, augmented: $0 \%$, missing: $100 \%$ ]: Thrombophilia.

Fall-down (Semiotics (other), binary) [absent: $84.49 \%$, present: $15.51 \%$, missing: $0 \%$ ]: Acute cerebro-vascular disease, Syncope.
Fertility (Aetiology, binary) [no: $0 \%$, yes: $0 \%$, missing: $100 \%$ ]: Age (years old), Gender.
Fever (Semiotics (other), binary) [absent: $39.47 \%$, present: $11.22 \%$, missing: $49.31 \%$ ]: Antiinflammatory drugs recent intake, Bacterial infection, Non-bacterial infection.
Fibrinolysis (Pathogenesis, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Arterial intravascular coagulation, Venous intra-vascular coagulation.
Focal neurological signs (Semiotics (other), binary) [absent: $96.4 \%$, present: $3.6 \%$, missing: $0 \%$ ]: Acute cerebro-vascular disease, Chronic cerebro-vascular disease.
Focal neurological signs (Semiotics (other), binary) [absent: $96.4 \%$, present: $3.6 \%$, missing: $0 \%$ ]: Acute cerebro-vascular disease, Chronic cerebro-vascular disease.
FT3 (pg/ml) (Semiotics (other), continuous) [lp-range: $8.73 \%$, n-range: $10.94 \%$, hp-range: $0.55 \%$, missing: $79.78 \%$ ]: Thyroid hormones.
FT4 ( $\mathrm{ng} / \mathrm{ml}$ ) (Semiotics (other), continuous) [lp-range: $0.97 \%$, n-range: $20.78 \%$, hp-range: $1.39 \%$, missing: $76.87 \%$ ]: Thyroid hormones.
Gastro-oesophageal reflux (Pathology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Age (years old), Hiatal hernia.
Gender (Epidemiology, binary) [male: $52.22 \%$, female: $47.37 \%$, missing: $0.42 \%$ ]: -
Generalized epileptic seizure (Semiotics (other), binary) [absent: $97.78 \%$, present: $1.66 \%$, missing: $0.55 \%$ ]: Previous transient seizure.
Glasgow Coma Scale (Semiotics (other), multi-valued) [absent: $93.49 \%$, from (12 to 14): $4.16 \%$, from (9 to 11): $0.55 \%$, less (than 9): $1.52 \%$, missing: $0.28 \%$ ]: Cerebral hypoxia, Cerebral mass, Hypoglycemia, Oxygen saturation (percentage).
Ground Glass (Semiotics (other), binary) [absent: $13.3 \%$, present: $0.55 \%$, missing: $86.15 \%$ ]: Pulmonary edema, Pulmonary emphysema.
Heart drive (Pathophysiology, continuous) [n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Acute coronary event, Pheochromocytoma, Thyrotoxicosis, Ventricular pre-excitation.
Heart post-load (Pathophysiology, continuous) [n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Acute aortic valve failure, Acute mitral valve failure, Obstructive cardiomyopathy.
Heart rate (bpm) (Semiotics (other), continuous) [lp-range: $4.71 \%$, n-range: $23.96 \%$, hp-range: $71.19 \%$, missing: $0.14 \%$ ]: Autonomic nervous system status, Bradycardia/Tachycardia.
Heartburn (Semiotics (other), binary) [absent: $88.92 \%$, present: $7.06 \%$, missing: $4.02 \%$ ]: Dyspepsia.
Hemoglobin (gr/100 ml) (Semiotics (other), continuous) [lp-range: $25.9 \%$, n-range: $72.85 \%$, missing: $1.25 \%$ ]: Acute anemia, Chronic anemia.
Hemopericardium (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Acute myocardial infarction, Aortic dissection.
Hemoptysis (Semiotics (other), binary) [absent: $99.17 \%$, present: $0.83 \%$, missing: $0 \%$ ]: Lung cancer, Pneumonia, Pulmonary infarction, Upper airways infection.
Hemorrhage (Pathology, binary) [absent: $0 \%$, present: $0.69 \%$, missing: $99.31 \%$ ]: Pancreatitis.
Hepatomegaly (Semiotics (other), binary) [absent: $82.83 \%$, present: $9.97 \%$, missing: $7.2 \%$ ]: Right heart failure.
Herpes Zooster (Pathology, binary) [absent: $99.31 \%$, present: $0.28 \%$, missing: $0.42 \%$ ]: -
Hiatal hernia (Epidemiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: -
Hilar adenopathy (Semiotics (other), binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Chronic interstitial lung disease, Lung cancer, Pneumonia.
Hyperhomocysteinemia (Semiotics (other), binary) [absent: $2.08 \%$, present: $0.97 \%$, missing: $96.95 \%$ ]: Thrombophilia.
Hypertransparency (Semiotics (other), multi-valued) [absent: $74.24 \%$, parenchymal: $5.4 \%$, pleuritic: $3.19 \%$, missing: $17.17 \%$ ]: Pulmonary emphysema, Spontaneous pneumothorax.
Hypoglycemia (Semiotics (other), binary) [absent: $96.95 \%$, present: $1.94 \%$, missing: $1.11 \%$ ]: -
Iliac phlebography (Semiotics (other), binary) [negative: $0.14 \%$, positive: $0 \%$, missing: $99.86 \%$ ]: Lower limbs deep vein thrombosis.
Immobilisation (Semiotics (other), binary) [no: $85.32 \%$, yes: $14.68 \%$, missing: $0 \%$ ]: Neuromuscular disease.

Immunocompromission (Pathophysiology, binary) [absent: 51.52\%, present: 0.83\%, missing: 47.65\%]: Age (years old), Neoplastic disease (generic).
Inspired oxygen fraction (percentage) (Epidemiology, continuous) [air: 71.05\%, 0.21-0.35: 0\%, 0.350.50: $0 \%,>0.50: 0 \%$, missing: $28.95 \%$ ]: -
Intra-vascular coagulation (Pathogenesis, multi-valued) [normal: $0 \%$, ipernormal: $0 \%$, iponormal: $0 \%$, missing: $100 \%$ ]: Extrogens use, Neoplastic disease (generic), Obesity (Body Mass Index $>=30$ ), Prophylaxis/anticoagulation, Sepsis, Thrombophilia.
Jugular venous distention (Semiotics (other), binary) [absent: $81.72 \%$, present: $5.54 \%$, missing: $12.74 \%$ ]: Right heart failure.
L-dopa use (Epidemiology, binary) [no: $97.65 \%$, yes: $1.8 \%$, missing: $0.55 \%$ ]: -
Lactates (mmol/l) (Semiotics (other), continuous) [n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Left cardiac output.
LDH (Semiotics (other), binary) [normal: $52.91 \%$, augmented: $18.7 \%$, missing: $28.39 \%$ ]: Acute cerebro-vascular disease, Acute myocardial infarction, Bacterial infection, Neoplastic disease (generic), Pulmonary infarction, Thyroid disease.
Left bundle branch block (Semiotics (other), binary) [absent: $87.4 \%$, present: $8.59 \%$, missing: $4.02 \%$ ]: Acute coronary event, Chronic cardiac muscle disease.
Left cardiac output (Pathophysiology, continuous) [lp-range: $0 \%$, n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Heart drive, Left heart pump, Left ventricular pre-load.
Left heart pump (Pathophysiology, continuous) [lp-range: $0 \%$, n-range: $0 \%$, missing: 100\%]: Acute myocardial infarction, Chronic cardiac muscle disease, Heart drive, Heart post-load.
Left ventricular hypertrophy (Pathogenesis, binary) [absent: $56.09 \%$, present: $0.14 \%$, missing: $43.77 \%$ ]: Age (years old), Chronic aortic valve failure, Chronic arterial hypertension, Chronic mitral valve failure.
Left ventricular pre-load (Pathophysiology, continuous) [lp-range: $0 \%$, n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Cardiac tamponade, Heart drive, Left heart pump, Right heart output.
Left ventricular thickness $(>=5 \mathrm{~mm}$ ) (Semiotics (other), binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Cor pulmonale.
Leiden factor $V$ (Semiotics (other), binary) [absent: $1.94 \%$, present: $0.28 \%$, missing: $97.78 \%$ ]: Thrombophilia.
Leukemia (Epidemiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Neoplastic disease (generic).
Leukemic blast brisis (Pathophysiology, binary) [absent: $99.17 \%$, present: $0.83 \%$, missing: $0 \%$ ]: Leukemia.
Leukocytosis (Semiotics (other), multi-valued) [absent: $76.45 \%$, hypo: $19.94 \%$, hyper (moderate): $1.8 \%$, hyper (severe): $0.55 \%$, missing: $1.25 \%$ ]: Focal neurological signs, Lymphocytosis.
Lower limbs compression ultrasounds (Semiotics (other), binary) [negative: $2.91 \%$, positive: $1.8 \%$, missing: $95.29 \%$ ]: Lower limbs deep vein thrombosis.
Lower limbs deep vein thrombosis (Pathology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Venous intra-vascular coagulation.
Lower limbs echo-color doppler (Semiotics (other), binary) [negative: $8.31 \%$, positive: $5.12 \%$, missing: $86.57 \%$ ]: Lower limbs deep vein thrombosis.
Lower limbs fractures (Semiotics (other), binary) [absent: $97.65 \%$, present: $2.35 \%$, missing: $0 \%$ ]: -
Lower limbs magnetic resonance phlebography (Semiotics (other), binary) [negative: $0 \%$, positive: $0 \%$, missing: $100 \%$ ]: Lower limbs deep vein thrombosis.
Lower limbs pain (Semiotics (future), binary) [absent: $87.67 \%$, present: $6.23 \%$, missing: $6.09 \%$ ]: Lower limbs deep vein thrombosis.
Lung cancer (Pathology, binary) [absent: $85.46 \%$, present: $3.88 \%$, missing: $10.66 \%$ ]: Neoplastic disease (generic).
Lung perfusion (Pathophysiology, continuous) [n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Pulmonary hypertension, Pulmonary venous thrombo-embolism.
Lung perfusion scintigraphy (Semiotics (other), binary) [negative: $0.97 \%$, positive: $2.35 \%$, missing: $96.68 \%$ ]: Bias of perfusion scintigraphy, Lung perfusion.
Lymphocytosis (Semiotics (other), binary) [absent: $39.47 \%$, present: $8.86 \%$, missing: $51.66 \%$ ]: Non-bacterial infection.

Mallory-Weiss syndrome (Pathology, binary) [absent: 0\%, present: 0\%, missing: 100\%]: Alcoholism.
Miller index (Semiotics (other), multi-valued) [less (than 1): 0\%, tra (1 e 16): $0.14 \%$, more (than 16): $0 \%$, missing: $99.86 \%$ ]: Pulmonary venous thrombo-embolism.
Minute ventilation (Pathophysiology, continuous) [lp-range: $0 \%$, n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Abnormal ventilation trigger, Acute anemia, Acute pulmonary disease, Anxiety/agitation, Lactates (mmol/l), Neuromuscular disease, Sepsis.
Mitral valve failure (Semiotics (other), binary) [absent: $17.59 \%$, present: $24.52 \%$, missing: $57.89 \%$ ]: Acute mitral valve failure, Chronic mitral valve failure.
Mitral valve prolapse (generic) (Semiotics (other), binary) [absent: $38.92 \%$, present: $2.63 \%$, missing: $58.45 \%$ ]: Acute mitral valve prolapse, Chronic mitral valve prolapse.
Myocardial stretching (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: 100\%]: Acute aortic valve failure, Left ventricular pre-load, Pulmonary venous thrombo-embolism.
Myocarditis (Pathology, binary) [absent: $24.52 \%$, present: $0.97 \%$, missing: $74.52 \%$ ]: Endocarditis, Non-infarctual pericarditis, Sepsis.
Myoglobin (Semiotics (other), binary) [normal: $14.96 \%$, abnormal: $11.91 \%$, missing: $73.13 \%$ ]: Acute myocardial infarction.
Nausea (Semiotics (other), binary) [absent: $82.13 \%$, present: $12.47 \%$, missing: $5.4 \%$ ]: Dyspepsia.
Neoplastic disease (generic) (Semiotics (other), binary) [absent: $84.07 \%$, present: $14.96 \%$, missing: $0.97 \%$ ]: Age (years old), Gender, Smoker.
Neuromuscular disease (Epidemiology, binary) [absent: $85.32 \%$, present: $0.83 \%$, missing: $13.85 \%$ ]: -
Nodule (Semiotics (other), binary) [absent: $87.4 \%$, present: $7.48 \%$, missing: $5.12 \%$ ]: Lung cancer.
Non-bacterial infection (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Myocarditis, Non-infarctual pericarditis, Pancreatitis, Pulmonary infarction, Upper airways infection.
Non-infarctual pericarditis (Pathology, binary) [absent: $92.66 \%$, present: $0.69 \%$, missing: $6.65 \%$ ]: -
Non-infective pericarditis (Pathology, binary) [absent: $61.91 \%$, present: $1.52 \%$, missing: $36.57 \%$ ]: Acute myocardial infarction.
Non ST segment elevation (Semiotics (other), multi-valued) [absent: $75.21 \%$, depressed (ST): $4.99 \%$, negative ( T waves): $9.97 \%$, missing: $9.83 \%$ ]: Acute coronary event, Chronic cardiac muscle disease, Left bundle branch block, Myocarditis.
Obesity (Body Mass Index: $=-30$ ) (Aetiology, binary) [BMI (less than 30): 96.4\%, BMI (30 or more): $3.6 \%$, missing: $0 \%$ ]: -
Obstruction of the systemic circulation (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Lung perfusion, Obstructive cardiomyopathy.
Obstructive cardiomyopathy (Pathology, multi-valued) [absent: $46.26 \%$, stadium (I): $0.42 \%$, stadium (II): $0 \%$, missing: $53.32 \%$ ]: Age (years old), Aortic stenosis, Left ventricular hypertrophy.
Oliguria/anuria (Semiotics (other), binary) [absent: $88.64 \%$, present: $6.37 \%$, missing: $4.99 \%$ ]: Left cardiac output.
Opacity to chest X-rays (Semiotics (other), multi-valued) [absent: $68.01 \%$, nodular (reticulum): $18.01 \%$, widespread: $6.09 \%$, missing: $7.89 \%$ ]: Pulmonary opacity.
Orthopnea (Semiotics (other), binary) [absent: $75.76 \%$, present: $13.99 \%$, missing: $10.25 \%$ ]: Chronic cardiac muscle disease, Pulmonary edema, Pulmonary emphysema.
Orthostatic hypotension (Semiotics (other), binary) [absent: $53.46 \%$, present: $1.94 \%$, missing: $44.6 \%$ ]: Dehydration, L-dopa use, Psychiatric medication, Pulmonary venous thrombo-embolism.
Oxygen saturation (percentage) (Semiotics (other), continuous) [lp-range: $64.96 \%$, n-range: $22.3 \%$, missing: $12.74 \%$ ]: Inspired oxygen fraction (percentage), Lung perfusion, Minute ventilation, Pulmonary shunt.
$\mathrm{paCO} 2(\mathrm{mmHg})$ (Semiotics (other), continuous) [lp-range: $18.56 \%$, n-range: $21.75 \%$, hp-range: $8.73 \%$, missing: $50.97 \%$ ]: Lung perfusion, Minute ventilation, Pulmonary shunt.
Palpitations (Semiotics (future), binary) [absent: $71.19 \%$, present: $23.27 \%$, missing: $5.54 \%$ ]: Extrasystoles, Heart rate (bpm).
Pancreatitis (Pathology, binary) [absent: $90.3 \%$, present: $0.14 \%$, missing: $9.56 \%$ ]: Age (years old), Alcoholism, Cholelithiasis, Gender.

paO2 (mmHg) (Semiotics (other), continuous) [lp-range: $33.93 \%$, n-range: $14.27 \%$, missing: $51.8 \%$ ]: Oxygen saturation (percentage).
Paradoxical interventricular septum (Semiotics (other), binary) [absent: $30.06 \%$, present: $1.39 \%$, missing: $68.56 \%$ ]: Right heart pre-load.
Patent foramen ovale (Semiotics (other), binary) [normal: $41.14 \%$, pervious: $0.97 \%$, missing: $57.89 \%$ ]: -
Peptic ulcer (Pathology, binary) [absent: $88.92 \%$, present: $0.28 \%$, missing: $10.8 \%$ ]: -
Pericardial effusion (Semiotics (other), binary) [absent: $48.75 \%$, present: $3.05 \%$, missing: $48.2 \%$ ]: Hemopericardium, Pericarditis, Right heart failure.
Pericarditis (Pathology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Non-infarctual pericarditis, Non-infective pericarditis.
Peripheral edema (Semiotics (other), multi-valued) [absent: $77.98 \%$, unilateral: $4.29 \%$, bilateral: $16.62 \%$, missing: $1.11 \%$ ]: Chronic cardiac muscle disease, Lower limbs deep vein thrombosis, Lower limbs fractures, Right heart failure.
Peritonitis (Pathology, binary) [absent: $82.55 \%$, present: $0 \%$, missing: $17.45 \%$ ]: Cholecystitis, Peptic ulcer.
pH (Semiotics (other), continuous) [lp-range: $6.09 \%$, n-range: $22.71 \%$, hp-range: $20.64 \%$, missing: $50.55 \%$ ]: Chronic metabolic alkalosis, Lactates (mmol/l), paCO2 (mmHg).
Pheochromocytoma (Pathology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Age (years old).
Pleural effusion (Semiotics (other), multi-valued) [absent: $76.59 \%$, unilateral: $12.74 \%$, bilateral: $5.54 \%$, missing: $5.12 \%$ ]: Lung cancer, Pleurisy, Pulmonary infarction, Right heart failure.
Pleurisy (Pathology, binary) [absent: $18.28 \%$, present: $0.83 \%$, missing: $80.89 \%$ ]: Lung cancer, Non-infarctual pericarditis, Non-infective pericarditis, Pneumonia, Pulmonary infarction.
Pneumonia (Pathology, multi-valued) [absent: $58.73 \%$, interstiziale: $1.52 \%$, solida: $0.69 \%$, missing: $39.06 \%$ ]: Age (years old), Alcoholism, Chronic cardiac muscle disease, Chronic cerebro-vascular disease, Gender, Immunocompromission, Lung cancer, Pulmonary emphysema.
Pregnancy (Aetiology, multi-valued) [no: $99.31 \%$, prepartum: $0 \%$, postpartum: $0.69 \%$, missing: $0 \%$ ]: Extrogens use, Fertility.
Previous episode of deep venous thrombosis/pulmonary embolism (Aetiology, binary) [absent: $92.94 \%$, present: $7.06 \%$, missing: $0 \%$ ]: Thrombophilia.
Previous transient seizure (Pathophysiology, multi-valued) [absent: $0 \%$, recently occurred: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Cerebral hypoxia, Cerebral mass, Hypoglycemia.
Prophylaxis/anticoagulation (Epidemiology, multi-valued) [nessuna: $83.8 \%$, heparine: $2.49 \%$, anticoagulants: $5.12 \%$, missing: $8.59 \%$ ]: Chronic atrial arrhythmia, Previous episode of deep venous thrombosis/pulmonary embolism, Surgery.
Protein $C$ (Semiotics (other), binary) [normal: $2.35 \%$, deficit: $0 \%$, missing: $97.65 \%$ ]: Thrombophilia.
Protein $S$ (Semiotics (other), binary) [normal: $2.22 \%$, deficit: $0 \%$, missing: $97.78 \%$ ]: Thrombophilia.
Psychiatric medication (Epidemiology, binary) [no: $89.61 \%$, yes: $10.39 \%$, missing: $0 \%$ ]: Anxiety/agitation.
Pulmonary artery diameter (Semiotics (other), binary) [normal: $0 \%$, over ( 27 mm ): $0 \%$, missing: $100 \%$ ]: Dilatated pulmonary artery disease.
Pulmonary artery thrombosis (Semiotics (other), binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Dilatated pulmonary artery disease, Pulmonary venous thrombo-embolism.
Pulmonary consolidation (Semiotics (other), multi-valued) [absent: $90.3 \%$, other (consolidation): $4.02 \%$, Hampton (hump): $0.28 \%$, missing: $5.4 \%$ ]: Lung cancer, Pneumonia, Pulmonary edema, Pulmonary infarction.
Pulmonary edema (Pathology, multi-valued) [absent: $0 \%$, initial: $0 \%$, advanced: $0 \%$, missing: $100 \%$ ]: Acute respiratory distress syndrome, Left ventricular pre-load.
Pulmonary emphysema (Epidemiology, multi-valued) [absent: $0 \%$, initial: $0 \%$, advanced: $0 \%$, missing: $100 \%$ ]: Age (years old), Gender, Smoker.
Pulmonary hypertension (Pathophysiology, binary) [absent: $58.17 \%$, present: $0.69 \%$, missing: $41.14 \%$ ]: Previous episode of deep venous thrombosis/pulmonary embolism, Pulmonary emphysema.

Pulmonary infarction (Pathophysiology, binary) [absent: $38.37 \%$, present: $2.63 \%$, missing: $59 \%$ ]: Pulmonary venous thrombo-embolism.
Pulmonary interstitium (Pathophysiology, binary) [normal: $37.26 \%$, tickened: $29.5 \%$, missing: $33.24 \%$ ]: Pulmonary opacity.
Pulmonary opacity (Pathophysiology, multi-valued) [absent: $0 \%$, interstitial: $0 \%$, alveolar: $0 \%$, missing: $100 \%$ ]: Age (years old), Chronic interstitial lung disease, Lung cancer, Pneumonia, Pulmonary edema, Pulmonary emphysema.
Pulmonary shunt (Pathophysiology, continuous) [n-range: $0 \%$, hp-range: $0 \%$, missing: 100\%]: Acute pulmonary disease, Atelactasis, Pulmonary edema, Spontaneous pneumothorax.
Pulmonary venous thrombo-embolism (Pathology, multi-valued) [absent: $0 \%$, non (massive): $0 \%$, massive: $0 \%$, missing: $100 \%$ : Lower limbs deep vein thrombosis, Right heart thrombus, Upper caval circle deep vein thrombosis.
Reflux of contrast medium into the hepatic veins (Semiotics (other), binary) [absent: $11.77 \%$, present: $0.14 \%$, missing: $88.09 \%$ ]: Right heart failure.
Rib fracture (Semiotics (other), binary) [absent: $49.31 \%$, present: $2.22 \%$, missing: $48.48 \%$ ]: Neoplastic disease (generic).
Right bundle branch block (Semiotics (other), binary) [absent: $88.64 \%$, present: $10.11 \%$, missing: $1.25 \%$ ]: Cor pulmonale, Right heart pre-load.
Right circolatory obstruction trigger (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ : Pulmonary venous thrombo-embolism, Spontaneous pneumothorax.
Right heart failure (Pathophysiology, continuous) [n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Cardiac tamponade, Left heart pump, Right heart pre-load.
Right heart output (Pathophysiology, continuous) [lp-range: $0 \%$, n-range: $0 \%$, missing: 100\%]: Pulmonary venous thrombo-embolism, Right circolatory obstruction trigger, Right heart preload.
Right heart pre-load (Pathophysiology, continuous) [lp-range: $0 \%$, n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ : Cor pulmonale, Dehydration, Pulmonary venous thrombo-embolism, Right circolatory obstruction trigger.
Right heart thrombus (Semiotics (other), binary) [absent: $50.55 \%$, floating: $0 \%$, missing: $49.45 \%$ : Lower limbs deep vein thrombosis, Upper caval circle deep vein thrombosis, Venous intravascular coagulation.
Right ventricular hypokinesis (Semiotics (other), binary) [absent: $41.69 \%$, present: $1.8 \%$, missing: $56.51 \%$ : Right heart failure.
Risk of deep vein thrombosis (Pathogenesis, binary) [absent: $0 \%$, present: $0 \%$, missing: 100\%]: Chronic venous insufficiency, Lower limbs fractures, Neoplastic disease (generic), Smoker.
Ruptured chordae tendineae (Semiotics (other), binary) [absent: $42.8 \%$, present: $0.14 \%$, missing: $57.06 \%$ : Acute mitral valve prolapse, Chronic mitral valve prolapse.
Sepsis (Pathology, binary) [absent: $12.47 \%$, present: $0.69 \%$, missing: $86.84 \%$ ]: Peritonitis, Pneumonia.
Shock (Semiotics (other), binary) [absent: $95.29 \%$, present: $1.8 \%$, missing: $2.91 \%$ : Lactates $(\mathrm{mmol} / \mathrm{l})$.
Sick sinus syndrome (Pathophysiology, binary) [absent: $0 \%$, present: $0 \%$, missing: 100\%]: Age (years old).
Small pulmonary vessel diameter (Semiotics (other), binary) [normal: $13.71 \%$, reduced: $1.39 \%$, missing: $84.9 \%$ : Dilatated pulmonary artery disease.
Smoker (Aetiology, binary) [no: $90.58 \%$, yes: $9.42 \%$, missing: $0 \%$ ]: -
Sphincter incontinence (Semiotics (other), binary) [absent: $96.68 \%$, present: $1.8 \%$, missing: $1.52 \%$ : Previous transient seizure.
Spontaneous pneumothorax (Pathology, multi-valued) [absent: $90.58 \%$, limited: $1.66 \%$, extended: $1.52 \%$, missing: $6.23 \%$ : Age (years old), Lung cancer, Pulmonary emphysema.
ST segment elevation (Semiotics (other), multi-valued) [absent: $85.18 \%$, non (ubiquitous ST): $4.02 \%$, ubiquitous (ST): $0.97 \%$, missing: $9.83 \%$ : Acute myocardial infarction, Left bundle branch block, Pericarditis.
Surgery (Aetiology, multi-valued) [no: $96.68 \%$, general: $3.05 \%$, orthopedic: $0.28 \%$, missing: $0 \%$ : Lower limbs fractures.

Syncope (Semiotics (future), binary) [absent: $82.96 \%$, present: $17.04 \%$, missing: $0 \%$ ]: Cerebral hypoxia, Hypoglycemia, Previous transient seizure.
T-wave inversion in V1-V3 (Semiotics (other), binary) [absent: $82.27 \%$, present: $7.89 \%$, missing: $9.83 \%$ ]: ECG right heart findings.
Tachypnea (Semiotics (other), binary) [absent: $36.7 \%$, present: $40.86 \%$, missing: $22.44 \%$ ]: Minute ventilation.
Temporary suspension of heart drive (Pathophysiology, binary) [absent: $82.96 \%$, present: $0.55 \%$, missing: $16.48 \%$ ]: Acute coronary event, Pheochromocytoma, Thyrotoxicosis, Ventricular preexcitation.
Thrombophilia (Pathogenesis, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: -
Thyroid-stimulating hormone ( $m U I / \mathrm{ml}$ ) (Semiotics (other), continuous) [lp-range: $1.52 \%$, n-range: $25.48 \%$, hp-range: $1.66 \%$, missing: $71.33 \%$ ]: Thyroid disease.
Thyroid disease (Epidemiology, multi-valued) [absent: $1.39 \%$, hypo (primitive): $0.14 \%$, hypo (secondary): $0.14 \%$, hyper (primitive): $0.55 \%$, hyper (secondary): $0.14 \%$, missing: $97.65 \%$ ]: Age (years old), Gender.
Thyroid hormones (Pathophysiology, continuous) [lp-range: $0 \%$, n-range: $0 \%$, hp-range: $0 \%$, missing: $100 \%$ ]: Thyroid disease.
Thyrotoxicosis (Pathology, binary) [absent: $55.54 \%$, present: $0.28 \%$, missing: $44.18 \%$ ]: Thyroid hormones.
Tongue bite (Semiotics (other), binary) [absent: $80.75 \%$, present: $0.55 \%$, missing: $18.7 \%$ ]: Previous transient seizure.
Tricuspid valve insufficiency (Semiotics (other), binary) [absent: $27.7 \%$, present: $12.33 \%$, missing: $59.97 \%$ ]: Chronic mitral valve failure, Cor pulmonale, Endocarditis, Right heart pre-load.
Troponin I (Semiotics (other), binary) [normal: $50.69 \%$, augmented: $6.23 \%$, missing: $43.07 \%$ ]: Acute myocardial infarction, Myocardial stretching.
Upper airways infection (Pathology, binary) [absent: $53.6 \%$, present: $8.59 \%$, missing: $37.81 \%$ ]: -
Upper caval circle deep vein thrombosis (Pathology, binary) [absent: $0 \%$, present: $0 \%$, missing: $100 \%$ ]: Venous intra-vascular coagulation.
Urinary catecholamines (Semiotics (other), binary) [negative: $0.69 \%$, positive: $0.14 \%$, missing: $99.17 \%$ ]: Pheochromocytoma.
Vasovagal syncope (Pathology, binary) [absent: $82.96 \%$, present: $0.83 \%$, missing: $16.2 \%$ ]: -
Venous intra-vascular coagulation (Pathogenesis, multi-valued) [absent: $17.73 \%$, upper (caval circle): $0.14 \%$, lower (caval circle): $10.53 \%$, right (heart): $0 \%$, missing: $71.61 \%$ ]: Central line, Chronic cardiac muscle disease, Compression stockings, Immobilisation, Intra-vascular coagulation, Pregnancy, Previous episode of deep venous thrombosis/pulmonary embolism, Risk of deep vein thrombosis, Surgery.
Ventricular arrhythmia (Semiotics (other), binary) [absent: $88.37 \%$, present: $2.08 \%$, missing: $9.56 \%$ ]: Bradycardia/Tachycardia.
Ventricular moderator band thickness (Semiotics (other), binary) [absent: $26.04 \%$, present: $0.28 \%$, missing: $73.68 \%$ ]: Cor pulmonale.
Ventricular pre-excitation (Aetiology, binary) [absent: $36.98 \%$, present: $0.55 \%$, missing: $62.47 \%$ ]:

Ventricular segmental dyssynergia (Semiotics (other), multi-valued) [absent: $32.13 \%$, hypokinesia (or diskinesia): $7.76 \%$, akinesia: $3.46 \%$, aneurysm: $0.28 \%$, missing: $56.37 \%$ ]: Acute coronary event, Acute myocardial infarction, Dilated cardiomyopathy, Ventricular arrhythmia.
Vomit (Semiotics (other), binary) [absent: $90.44 \%$, present: $9.56 \%$, missing: $0 \%$ ]: Cerebral mass, Dyspepsia.