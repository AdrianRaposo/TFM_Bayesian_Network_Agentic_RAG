# A novel dynamic Bayesian network approach for data mining and survival data analysis 

Ali Sheidaei ${ }^{1}$, Abbas Rahimi Foroushani ${ }^{1}$, Kimiya Gohari ${ }^{2}$ and Hojjat Zeraati ${ }^{1 *}$


#### Abstract

Background: Censorship is the primary challenge in survival modeling, especially in human health studies. The classical methods have been limited by applications like Kaplan-Meier or restricted assumptions like the Cox regression model. On the other hand, Machine learning algorithms commonly rely on the high dimensionality of data and ignore the censorship attribute. In addition, these algorithms are more sophisticated to understand and utilize. We propose a novel approach based on the Bayesian network to address these issues.


Methods: We proposed a two-slice temporal Bayesian network model for the survival data, introducing the survival and censorship status in each observed time as the dynamic states. A score-based algorithm learned the structure of the directed acyclic graph. The likelihood approach conducted parameter learning. We conducted a simulation study to assess the performance of our model in comparison with the Kaplan-Meier and Cox proportional hazard regression. We defined various scenarios according to the sample size, censoring rate, and shapes of survival and censoring distributions across time. Finally, we fit the model on a real-world dataset that includes 760 post gastrectomy surgery due to gastric cancer. The validation of the model was explored using the hold-out technique based on the posterior classification error. Our survival model performance results were compared using the Kaplan-Meier and Cox proportional hazard models.
Results: The simulation study shows the superiority of DBN in bias reduction for many scenarios compared with Cox regression and Kaplan-Meier, especially in the late survival times. In the real-world data, the structure of the dynamic Bayesian network model satisfied the finding from Kaplan-Meier and Cox regression classical approaches. The posterior classification error found from the validation technique did not exceed 0.04 , representing that our network predicted the state variables with more than $96 \%$ accuracy.
Conclusions: Our proposed dynamic Bayesian network model could be used as a data mining technique in the context of survival data analysis. The advantages of this approach are feature selection ability, straightforward interpretation, handling of high-dimensional data, and few assumptions.
Keywords: Dynamic Bayesian network, Directed acyclic graph, Survival analysis, Gastric cancer

[^0]
## Background

Survival analysis is the formal name for an essential branch of statistics. It aims to study the time of the specific event and explore the particular circumstances or characteristics that influence it [1]. We know these techniques as reliability analysis in engineering and industries. The usual interest is the lifetime of devices, products, and machines in these contexts [2-4]. The intrinsic features of subjects in these domains enable the

## E BMC

[^1]
[^0]:    *Correspondence: zeraatih@tums.ac.ir
    ${ }^{1}$ Department of Epidemiology and Biostatistics, School of Public Health, Tehran University of Medical Sciences, Pour Sina St., Keshavarz Blvd., Tehran 14176-13151, Iran
    Full list of author information is available at the end of the article

[^1]:    (c) The Author(s) 2022. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/. The Creative Commons Public Domain Dedication waiver (http://creativecommons.org/publicdomain/zero/1.0/) applies to the data made available in this article, unless otherwise stated in a credit line to the data.

investigators to control all the processes and fully observe the data $[3,5]$.

Further, when the subjects are humans, the survival models confront the crucial challenge of incomplete data and the high dimension of confounders more than the other context. The incomplete data known as censoring is expected because sample withdrawal or loss of follow-up exceeds the event time of the study period [6, 7]. Despite all efforts to evolve the survival models, some challenges in classical methods show the necessity of developing new approaches in practice [8-10].

The Kaplan-Meier method, also known as productlimit, is one of the primary and still popular methods in analyzing survival data. This method estimated the survival probability function of data in a straightforward and easy-to-understand manner. In addition, the KaplanMeier is a nonparametric approach, and a few assumptions are required to apply it to data [1, 11]. However, the simplicity of Kaplan-Meier restricts its applications. For instance, it cannot account for multiple factors or control for confounding factors. Therefore, in the case of feature selection and group comparisons, we need to apply additional analyses such as the low power log-rank test. In this procedure, insufficient sample size and increasing the number of features lead to inaccurate inferences [12]. Another alternative is regression approaches like the Cox proportional hazard model. Using these models is limited by restrictive assumptions like the proportionality of hazards, independence of censoring and survival distribution, and exponential relation between hazard and covariates [13].

On the other hand, developing the application of machine learning algorithms in recent decades has reformed many classical approaches to data analysis. The survival analysis is one of the domains that changed significantly $[2,9,10]$. In this manner, the applications of random forests [14, 15], Bayesian methods [5, 16, 17], neural networks [18-21], support vector machines [22, 23], ensemble learning [24, 25], and active learning [26, 27] algorithms were introduced in survival analysis. These changes enable us to resolve issues with a new practice even though the general idea is similar to classical approaches.

As mentioned, incompletely observed data or censorship is the primary challenge in survival modeling, especially in health. Considerable studies that introduced the application of machine learning algorithms in survival analysis did not engage the censorship because of the study subject's type [5]. Some other studies relied on high sample size and ignored the censored observations or imputed them by modeling approaches [28, 29]. Finally, a few studies directly address censorship using the methods like weighting the censored observation [30]. However, there is a gap between classical approaches and novel machine learning techniques that use intelligent algorithms to extract data patterns. The classic methods were developed to handle small to medium-dimension data and find a general overview. In contrast, the machine learning algorithm and data mining techniques aim to handle high-dimensional data. These methods focus on the prediction with maximum accuracy.

This study proposes a novel Dynamic Bayesian Network (DBN) model for data mining in the context of survival data analysis. The Bayesian Network (BN) has a series of powerful tools that could facilitate survival analysis. Actually, the BN combines probability theory and graphical models [31]. Consequently, it enabled us to capture the uncertainty of stochastic survival events and represent a graphical structure of probability distribution. In addition, our model uses the KaplanMeier idea to consider the censoring phenomena and the various capability of BN models to add extra tools for more precise inferences simultaneously. The structure learning algorithm of the BN ables us to compare the groups and find the significant features. In addition, parameter learning algorithms lead to more precise inferences, estimations, and predictions. In this study, we present our DBN model for survival analysis, evaluate its performance using a simulation study, and finally use a real-world data set to show the way analysis could be performed using that.

## Methods

## Product limit estimators

The primary objective of survival analysis is to explore the time until a particular event. Hence, we describe the stochastic behavior of an outcome variable in time type. We usually use survival, density, hazard, and the mean or median residual life functions in this regard. As these functions are attainable from each other, there is no priority except for better interpretability in choosing one. The product limit estimators are the estimates of survival function, which is defined as the probability of an individual surviving after a given time point $t$ :

$$
S(t)=\mathrm{P}(T>t)
$$

T is a random variable that denotes when the event of interest occurs. Kaplan and Meier partitioned observed times into intervals according to unique event times and proposed the following estimator for all $t$ values in the range of observed data when $t_{1}$ represent the first event time [1]:

where *d_{i}* and *Y_{i}* represent the number of failures and at-risk persons in each interval, respectively. Therefore, the product-limit estimator is a discrete approach that leads to a step function that only changes at event times. The Greenwood formula is the well-known approach to estimating the variance of the estimators [1]:

$$
\hat{V}[\hat{S}(t)] = \hat{S}(t)^2 \sum_{t_i \leq t} \frac{d_i}{Y_i(Y_i - d_i)} \tag{2}
$$

### Bayesian network

Every Bayesian Networks (BNs) correspond to a Directed Acyclic Graph (DAG) and a joint distribution, which are the graphical and probabilistic aspects of the model. DAG consists of nodes corresponding to random variables and edges that present conditional probabilities. According to the domain of the random variables, the BN could be discrete, Gaussian, or hybrid. Our BN in this study is a discrete one. Therefore, for a set of discrete random variables *X* = (*X*₁, *X*₂, ..., *X*ₚ) Taking their values in the discrete and finite D-dimensional domain. The BN is defined as pair *M* = {}, (*P*(*X*ₚ|*P*ₜ(*X*ₚ))*)₁≤ₚ₋₇) where *} = (*X*, *ε*) is a DAG presentation of random variables *X* with edges set *ε*, *Pₜ*(*X*ₚ) is the set of parents *X*ₚ in *X*, and (*P*(*X*ₚ|*P*ₜ(*X*ₚ))*)₁≤ₚ₋₇) is the conditional probability of node *X*ₚ given their parents in the set *X*.

The appealing feature of BN is to summarize the complex joint probability distribution *X* in the following parsimonious way using the conditional independence and Markov chain properties:

$$
P(X_1, X_2, \dots, X_D) = \prod_{d=1}^{D} P(X_d | P_X(X_d)) \tag{3}
$$

### Dynamic Bayesian network

The classical BN is not adopted to address time-dependent processes like survival analysis [32]. Therefore, Dynamic Bayesian Network (DBN) [33] was introduced to extend this process. In this context, time-dependent random variables (*X*t)t≥1 = (*X*₁,t, ..., *X*ₚ,t)t≥1 are defined where *t* is a discrete index time formally called slice. DBN uses Markov property which indicates the future of a stochastic process is independent of its past, given current status or several lags before it. The number of lags determines the order of the Markov process. This study only needs to use the Markov process of order 1, which leads to a 2-slice Temporal Bayesian Network (2-TBN). In this regard, we assume *X_{t-1}⊥X_{t+1} |X_{t}* for all *t* ≥ 2. A 2-TBN could be defined as a pair of 2 BNs (*M*₁, *M*→) where *M*₁ is the joint distribution of the initial process *X*₁ = (*X*₁,₁, ..., *X*ₚ,₁) and *M*→ represent the transition model. The joint probability distribution *M*₁ easily derived from BN approach in Eq. 3:

$$
P(X_1) = \prod_{d=1}^{D} P(X_{d,1} | P_X(X_{d,1})) \tag{4}
$$

In the transition model, the joint distribution of *X_{t}* only depends on random variables belonging to the set of parents *X_{t}* at slice *t* - 1 in the form:

$$
\begin{aligned}
P(X_t | X_{t-1}) &= P(X_{1,t}, \dots, X_{D,t} | X_{1,t-1}, \dots, X_{D,t-1}) \\
&= \prod_{d=1}^{D} P(X_{d,t} | P_{X_t}(X_{d,t}))
\end{aligned} \tag{5}
$$

Hence the probability distribution of 2-TBN is calculated by the combination of Eqs. 4,5:

$$
\mathbf{R}_{ij}^{(k)} = r_{ij}^{(k)} \mathbf{a}_{i}^{(k)} (\mathbf{a}_{i}^{(k)})^{\mathbf{H}} + r_{ij}^{(k)} \mathbf{R}_{i}^{(k)} \tag{6}
$$

In order to consider the time stationary covariates *Z* = (*Z*₁, ..., *Z*q) in the model, we could extend the parent sets in both initial processes *M₁* and transition model *M*→. In this manner, the initial conditional probability could be presented as:

$$
P(X_1) = \prod_{d=1}^{D} P(X_{d,1} | P_{X_t}(X_{d,t}), P_{Z}(X_{d,1}))
$$

where the *P_{X}* (*X*ₚ,₁) and *P_{Z}* (*X*ₚ,₁) represent the sets of parents *X_{d,1}* in *X* and *Z*, respectively. On the other hand, the modified transition probability distribution is reformed to:

$$
\begin{aligned}
P(X_t | X_{t-1}, Z_1, \dots, Z_q) &= P(X_{1,t}, \dots, X_{D,t} | X_{1,t-1}, \dots, X_{D,t-1}, Z_1, \dots, Z_q) \\
&= \prod_{d=1}^{D} P(X_{d,t} | P_{X_t}(X_{d,t}), P_{Z}(X_{d,t}))
\end{aligned} \tag{7}
$$

### Dynamic Bayesian network interpretation of product limit estimators

A DBN of type 2-TBN could efficiently conduct the calculation process of product-limit estimators. The product-limit approach considers the time as discrete

intervals between consecutive observed failure times and counts the individuals at risk and failures. Equivalently, we define discrete intervals of Kaplan–Meier as slices and two time-dependent binary status variables. The survival state variables *N_{i,t}* is equal to 1 if individual *i* survives at least to slice *t* and state variables *Q_{i,t}* is equal to 1 if the individual *i* censored before or at slice *t*. Defining these variables enables us to form the DBN in Fig. 1 to analyze survival data. In addition, we can enter other fixed effect covariates in *Z* to the model and examine their importance by the structure learning algorithms.

The DBN estimators of survival probability at each time *t* according to Eq. 6 are equal to:

$$
\hat{S}(t) = P(N_1 = 1 | P_{Z}(N_t)) \prod_{t=2}^{T} P(N_t = 1 | N_{t-1} = 1, Q_{t-1} = 0, P_{Z}(N_t))
$$

Moreover, the discrete covariates set *P_{Z}(N_t)* were found by structure learning algorithms.

For simplicity, we consider there are no covariates in the model, so Eq. (7) could be modified by counter function *N*:

$$
\hat{S}(t) = P(N_1 = 1) \prod_{t=2}^{T} P(N_t = 1 | N_{t-1} = 1, Q_{t-1} = 0)
$$

$$
= \frac{N(N_{i1} = 1)}{N} \prod_{t=2}^{T} \frac{N(N_{it} = 1)}{N(N_{i,t-1} = 1, Q_{i,t-1} = 0)}
$$

$$
= \hat{S}(1) \prod_{t=2}^{T} \left[ 1 - \frac{d_t}{Y_t} \right]
$$

That is the same as product-limit estimators in Eq. (1). Therefore, we are able to use the Greenwood formula in Eq. (2) to calculate the variance of survival estimations. In addition, the common bootstrapping approaches in the BN context, like likelihood weighting and logic sampling, are the alternative approach in this way[34].

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Prior and transition Bayesian networks correspond to the extended dynamic Bayesian network representation of the Kaplan–Meier approach

### Simulation study

We conducted a simulation study to assess the performance of our model in comparison with the Kaplan–Meier and Cox proportional hazard regression. We defined various scenarios according to the sample size (*N* = 800, 5000, 10,000), censoring rate (*R* = 25%, 40%, 60%), and shape parameters of survival (*αS*) and censoring (*αC*) distributions. We considered five covariates distributed as mutually independent binomial distributions with different probability parameters [*X_{i}* ∼ *B(N, P_{i}), i* = 1, . . . , 5*P_{i}* = 0.1, 0.2, 0.5, 0.7, 0.9].

The survival and censoring times were generated using Weibull distributions. The scale parameter of survival

time distribution was reparametrized according to the summation of the covariates $$ \left[ \theta_S = \sum_{i=1}^5 X_i \right] $$. Using the numerical methods and assuming the fixed value for censorship, we found the scale parameter of censoring time distribution. We set the shape parameter of survival and censoring distributions as the values 0.5 (decreasing event/censor rate), 1 (constant event/censor rate), and 2 (increasing event/censor rate). In this manner, we achieved nine different scenarios for the shape of survival/censoring times.

In brief, if the survival time *S* ≥ 0 follows the below Weibull distribution:

$$
f(s; \alpha_S, \theta_S) = \frac{\alpha_S}{\theta_S} \left( \frac{s}{\theta_S} \right)^{\alpha_S - 1} \exp \left( -\left( \frac{s}{\theta_S} \right)^{\alpha_S} \right)
$$

where scale parameter *θ_S* and shape parameter *α_S* were defined before, the cumulative distribution function of *S* is:

$$
F(s; \alpha_S, \theta_S) = 1 - \exp \left( -\left( \frac{s}{\theta_S} \right)^{\alpha_S} \right)
$$

As the Weibull is a continuous random distribution *F(s; αS, θS)* ∼ *U*(0, 1). Therefore we generated *N* samples *u_{i}* ∼ *U*(0, 1) for *i* = 1, . . . , *N* and then compute the *s_{i}* = *θ_S^1 / αS / ln(u_{i})*. A similar approach was used to generate the censored times *c_{i} s*.

We fitted all three models to the simulated data and estimated survival probability at 20%, 50% (median), and 80% percentiles of actual survival times. The bias and its Root Mean Squared Errors (RMSE) were calculated in 1000 randomly generated samples in each scenario.

## Real data analysis

We applied our proposed method to real-world survival data. The 760 patients diagnosed with gastric cancer at the Iran cancer Institute and who had undergone gastrectomy from 1995 to 2012 entered the study. This historical and artificial cohort of patients was followed until observing death events. The censorship was considered in case of loss to follow-up or being alive at the end of observation time. All the variables except follow-up duration were time stationery and were collected at the surgery time.

We conducted the ordinary Kaplan--Meier survival analysis, DBN, and Cox proportional hazard (PH) model. The Cox PH model was added to compare our findings with a regression model that could handle the covariate effect in survival analysis. In addition, the censor probability plots were generated using the Kaplan--Meier approach. For this purpose, we defined censorship as the primary event and death as the alternative status.

## Structure learning

We used Hill-Climbing (HC) and Tabu search, two of the most popular score-based learning algorithms, to find the structure of DAG [35]. The last event occurred 15 years after surgery, and there was no event in year 13 post-surgery. Therefore 14 eligible slices $t$ correspond to the unique event year were defined in the DBN structure. The prior and transition networks in Fig. 1 related to $N_{l, t}$ and $Q_{l, t}$ were considered as the white list, and the algorithms learned the structure of stationary variables Z. The validation of structure learning was conducted by the ten repeated hold-out technique using ten subsamples in size $30 \%$ of the original data [36]. The posterior classification error based on likelihood weighting was set as the loss function [37]. The validation process was repeated according to different score functions, including logarithm of likelihood, AIC, BIC, BDE, BDS, and $K^{2}$ [38].

## Results

## Simulation study

Table 1 represents the bias and related RMSE of estimated survival probability by models in different scenarios. For instance, the first value of $-0.0033(0.0046)$ is observed for bias (RMSE) for a sample size of 800 and censorship of $25 \%$. It shows that the Kaplan--Meier approach estimated the survival probability by 0.0033 less than the actual value when the random samples come from the survival and censoring distributions with increasing rates over time. Cox and DBN estimations in this scenario are 0.004 and -0.0008 differ from the actual probability, respectively. Therefore, the minimum absolute bias value is related to the DBN model.

The Cox regression model shows superiority according to the minimum bias for most scenarios in Table 1. On the other hand, the DBN estimates actual survival probability better than the Cox approach in $52 \%$ of simulation scenarios which assumes an increasing censor rate across time. Increasing the censoring rate causes higher observed bias (RMSE) for all the models. The constant censor rate across time (alpha $\mathrm{c}=1$ ), which corresponds to non-informative censoring, shows lower levels of bias (RMSE) in all the scenarios.

Similar results for exploring median survival time are presented in Table 2. The number of scenarios in which the DBN is superior to other models due to bias (RMSE) reduction is relatively higher than in Table 1. In addition, Cox is not significantly better than DBN in all situations, and in many cases, its absolute bias is less than 0.001 of DBN.

The results of exploring the percentile of $80 \%$ of survival time in Table 3 reveal that the DBN model is superior in bias (RMSE) reduction in all the scenarios except one. When the data comes from survival distribution with shape parameter 0.5 and the censoring rate increases across time (alpha $\mathrm{c}=2$ ), for the sample sizes of 5000 with $60 \%$ censoring, the bias (RMSE) of Cox regression is $-0.1373(0.1345)$. DBN's bias (RMSE) for this scenario is $-0.1375(0.138)$. We should consider the increasing RMSE according to heavy censoring in this scenario. It causes more variation for Cox results, leading to the unstable mean of bias values.

## Real data analysis

The baseline characteristics of patients by their status in the last observation are summarized in Table 4. The pathology exam for the 672 (88\%) patients resulted in adenocarcinoma; however, the prevalence did not differ significantly across groups. The total gastrectomy was the most prevalent procedure, with 403 (53\%). However, the death event was distributed almost equally in all the surgery types ( $P$-value $=0.3$ ). As a predictable pattern, the metastasis cases were less frequent in survivors ( $17 \%$ of them survived compared to $83 \%$ of death cases). In addition, the survivors were almost categorized into the lower Stages.

We used the Tabu search algorithm based on the BDE score function, considering the clinical justifications and validation results. The final DAG is presented in Fig. 2. For a better exploration, the survival and censor probability curves are depicted in Figs. 3 and 4. According to the DAG in Fig. 2, the baseline age is related to survival in the first- and second years post-operative. The corresponding Kaplan--Meier curve in Fig. 3 confirmed this finding, and the survival lines diverge in the initial years and continue to be parallel. On the other hand, there is an edge between metastatic status and

Table 1 The models'bias and RMSE in survival probability estimation in percentile 20% of real survival time


Table 2 The models'bias and RMSE in survival probability estimation in the median of real survival time


Table 3 The models'bias and RMSE in survival probability estimation in percentile 80% of real survival time


Table 4 Descriptive statistics of patients by the last observation status


${ }^{a}$ Pearson's Chi-squared test
$N_{4}$ in DAG. The survival lines in Fig. 3 for metastasis and non-metastasis cases started to get away from each other at this time point.

On the other hand, the directed edges from age to $Q_{6}$ and $Q_{7}$ in DAG correspond to flattening the censor probability after year 6 for more than 70 years old patients and a sharp decrease in censor probability less than 61 in year seven that leads to crossing another line (Fig. 4). The censor probability lines of adenocarcinoma and the other group separate from each other at years 3 and 5 in Fig. 4. It is coordinated to edges from the pathology node to $Q_{3}$ and $Q_{5}$. All the other edges from the covariates to $Q_{t}$ nodes in DAG correspond to a specific pattern in Fig. 4 and are justifiable.

According to Table 5, the higher baseline age is the most critical factor for experiencing the death event early. The hazards for $61-70$ and more than 70 years old patients are 1.77 ( $95 \%$ CI $1.40-2.24$ ) and 3.99 ( $95 \%$ CI $3.09-5.14$ ) times for those less than 61 years old. The edges from the age node to $N_{1}$ and $N_{2}$ in Fig. 2 assert that the effect of age is more notable in the initial times.

The stage and metastasis reflect two relatively same aspects of disease progression in surgery time. Therefore, there is some degree of correlation between these variables. That is why the stage was no longer significant in the multivariable model when we added metastasis. The metastasis cases had a 3.89 ( $95 \%$ CI $1.57-9.62$ ) times higher hazard than the others. In

![img-1.jpeg](img-1.jpeg)

**Fig. 2** Representation of DAG corresponds to survival analysis of real-world data (survival of patients after gastrectomy) surgery

![img-2.jpeg](img-2.jpeg)

**Fig. 3** Kaplan–Meier survival probability curves of patients according to their baseline characteristics and the results of the log-rank test to compare the curves

![img-3.jpeg](img-3.jpeg)

**Fig. 4** The censorship probability curve of patients according to their baseline characteristics and the results of the log-rank test to compare the curves

contrast to the DBN, the Cox model does not ensure us about the relations between these variables. We present the conditional probability tables of the model covariates in the Additional file 1 for more clarification.

As the results of model validation, the mean posterior classification errors and their standard deviation for the whole learned network and *N*<sub>*t*</sub>, and *Q*<sub>*t*</sub> nodes are represented in the Additional file 1. The expected loss for all the scenarios did not exceed the acceptable value of 0.04, which means all the networks predicted the state variables with more than 96% accuracy.

## Discussion

We extended the classical idea of the Kaplan–Meier estimator and used the BN facilities to make a novel model for analyzing the survival data. The Bayesian network tools enable us to explore the different aspects of data in a previously impossible way. For instance, nonparametric survival methods like Kaplan–Meier were not adjusted to take covariates into account. On the other hand, the regression approaches only focus on the outcome variable and ignore the relations between covariates. The majority of the survival models were developed according to strict assumptions. In most applied cases, checking these assumptions is ignored or even hard to satisfy. Our model addressed the issues of the previous approaches and required the least possible assumptions.

Censorship which leads to incomplete observations is an intrinsic property of survival data. Methods developed in this domain tried to manage this issue and incorporate the information of the censored observation as much as possible. Many researchers in the setting of machine learning ignore the censor observation and change the problem to explore the continuous-time outcome variable [5, 17, 28, 29]. In contrast, we consider a state for censorship that enables the model to examine how covariates affect this state. This property significantly increases the prediction power of the model. In real-world applications, administrators of data registries could manage situations to avoid preventable censorship.

The graphical aspect and conditional probability distributions of BN reflect much information in the simplest form. In comparison, other survival base algorithms in machine learning, like neural networks [18–21], support vector machines [22, 23], and ensemble models [24, 25], are as much sophisticated in outlining the patterns of data. On the other hand, alternative classical approaches like the Cox PH, frailty concept, and the other parametric regression models [1] involves the users in the intricate interpretations of their effect sizes.

Table 5 The results of the univariable and multivariable Cox PH model


${ }^{a}$ Pearson's Chi-squared test

The DAG of the BN model is the only mechanism for demonstrating the intra-relationship of covariates which is not available in the alternative approaches. For instance, interventions could be designed basis on the roots of the network or the parents of unchangeable nodes. In addition, this model feedback the correlation between variables, as we have seen in our example. The causal inference is one of the extensions of BNs, which we do not explore here [39]. Finally, the DBN forced the covariates to be discretized.

Using the semiparametric and parametric survival models should be cautionary. The Cox model's proportional hazard assumption violation leads to incorrect inferences or underestimating the hazard ratio [13, 40]. On the other hand, the parametric approach relies on the outcome distribution. These models assume a parametric distribution for the survival time, which is hard to satisfy, significantly when we have heavily censored data [41]. Finally, even the nonparametric approaches assume noninformative censorship [42]. Our BN has two primary assumptions. At first, the variables follow the Markov property, and then conditional multinomial or conditional binomial distribution is appropriate for discrete nodes. Both of these assumptions are logical in practice [43].

We conducted a wide range of scenarios in the simulation study. The DBN was superior to Kaplan-Meier in bias (RMSE) reduction in almost all of them. In addition, our results showed the comparability of Cox regression and DBN in this context. Our model was significantly superior to the Cox regression when the interest was exploring late survival times.

The Kaplan Meier biases were negative in all the scenarios. Hence, this method always estimates the survival probability as less than the actual value. Other simulation studies explain this issue [44, 45], and several suggest correction approaches. Stute and Wang proposed a Jackknife method to reduce the Kaplan Meier bias [46]. In another attempt, Jiang used the geometric mean of survival and censoring curves for bias correction [47].

In most scenarios that explore the lowest percentile with the lower sensor rate, the bias of Cox regression was estimated to be positive. In addition, the Cox biases were positive in the decreasing event rate and increasing censor rate for all the scenarios. Langner et al. showed that the maximum likelihood estimations of Cox are biased.

They conducted a simulation study and concluded that there is a direct relationship between higher levels of event risk and seeing positive bias [48]. In concordance with their findings, we find that everywhere we expected to see the event, more than censoring the biases tend to the positive values.

The relation of covariates in our model is reasonably justifiable in the clinical aspect. Gender is the most known indicator of smoking across the population. According to the national representative survey, the age-standardized prevalence of current tobacco smoking among Iranian adults was 24.4% (95% CI 23.6--25.1) in males and 3.8% (95% CI 3.5--4.1) in females [49]. Therefore, it seems evident that the sex node is the parent of smoking.

We used the 7th version of the TNM Classification of Malignant Tumors (TNM) staging system for gastric cancer. The M parameter in TNM, representing distance metastases, is a critical prognostic for survival probability [50]. On the other hand, some studies described that the 7th TNM did not appropriately classify the biological behavior of cancer and the prognosis of patients [51]. In this manner, the 8th edition of the TNM staging with reforms to show relevant differences in stage III disease survival rates was released [52]. These arguments support our finding that TNM and stage nodes are affected by metastasis but are not the parents of any survival mechanism nodes.

Several studies on the Iranian population confirmed that a higher baseline age increases the hazard of death events in gastric patients who have undergone surgery. Interestingly, these studies did not mention a significant difference between males and females [53, 54].

## Conclusion

Our proposed DBN could be used as a data mining technique in the context of survival data analysis. The feature selection ability of this model is comparable with the Cox PH model in both statistical and clinical aspects. In contrast to the Kaplan--Meier, our model can handle high-dimensional data and does not require the restrictive assumptions of regression approaches. The available machine learning algorithms are relatively sophisticated and rarely consider the censorship property of survival data. Whereas BN is a straightforward method, the DBN incorporates the information of censoring observations in inferences.

In this study, we introduced the simplest DBN model for survival analysis and compared its performance to the most used methods in the clinical field. This model could be adjusted for a specific situation like competing risk, time-variant covariates, and high dimensional data. In this manner, more specific simulation studies would be required.

TNM
TNM Classification of Malignant Tumors
DAG
Directed Acyclic Graph
BN
Bayesian Network
DBN
Dynamic Bayesian Network
2-TBN
2-Slice Temporal Bayesian Network
PH
Proportional Hazard
HC
Hill-Climbing

## Supplementary Information

The online version contains supplementary material available at 10.1186/s12911-022-02000-7.

Additional file 1: Supplementary file 1. The validation of structure learning. The posterior classification error of HC and Tabu algorithms for all nodes according to different score functions. Supplementary file 2. Conditional probability distribution of time stationary variables in the model. Supplementary figure 1. Conditional probability distribution of node stage given the different levels of its parents (Metastasis and TNM). Supplementary figure 2. Conditional probability distribution of node TNM given the different levels of its parent (Metastasis). Supplementary figure 3. Conditional probability distribution of node metastasis given the different levels of its parent (Smoking). Supplementary figure 4. Conditional probability distribution of node pathology given the different levels of its parent (Sex). Supplementary figure 5. Conditional probability distribution of node smoking given the different levels of its parent (Sex). Supplementary figure 6. Conditional probability distribution of node surgery given the different levels of its parent (Site).

## Acknowledgements

This study is a part of the research process supported by the Tehran University of Medical Science to achieve a Ph.D. degree.

## Author contributions

All authors contributed to the study's conception and design. HZ and AS performed analysis. AS wrote the first draft of the manuscript, and all authors commented on previous versions. All authors read and approved the final manuscript.

## Funding

Not applicable.

## Availability of data and materials

The datasets used and/or analysed during the current study available from the corresponding author on reasonable request.

## Declarations

## Ethics approval and consent to participate

All methods were carried out following relevant guidelines and regulations. This study was found to be under the ethical principles and the national norms and standards for conducting medical research in Iran by the research ethics committee of the school of public health \& allied medical sciences - Tehran university of medical sciences. The approval ID is IRTUMS.SPH. REC.13993061. All participants provided written informed consent that their data collected as part of the study can be used in research. All the patients were followed until the event or when they preferred to stop participation.

## Consent for publication

Not applicable.

## Competing interests

The authors declare that they have no competing interests.

## Author details

^{1}Department of Epidemiology and Biostatistics, School of Public Health, Tehran University of Medical Sciences, Pour Sina St., Keshavarz Blvd., Tehran 14176-13151, Iran. ^{2}Department of Biostatistics, Faculty of Medical Sciences, Tarbiat Modares University, Tehran, Iran.

Received: 23 May 2022 Accepted: 19 September 2022Published online: 22 September 2022

## Publisher's Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## Ready to submit your research? Choose BMC and benefit from:

- fast, convenient online submission
- thorough peer review by experienced researchers in your field
- rapid publication on acceptance
- support for research data, including large and complex data types
- gold Open Access which fosters wider collaboration and increased citations
- maximum visibility for your research: over 100M website views per year

At BMC, research is always in progress.
Learn more biomedcentral.com/submissions