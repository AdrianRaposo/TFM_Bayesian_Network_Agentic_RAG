# Online Appendix to: Trustworthy Service Selection and Composition 

CHUNG-WEI HANG and MUNINDAR P. SINGH, North Carolina State University

## A. BAYESIAN NETWORKS

We provide some additional technical background in this section.

## A. 1 Parameter Estimation

Given an acyclic Bayesian network graph $G$ over $d$ variables, $x_{1}, x_{2}, \ldots, x_{d}$, the associated joint distribution is written as

$$
P\left(x_{1}, \ldots, x_{d}\right)=\prod_{i=1}^{d} P\left(x_{i} \mid x_{p o_{i}}\right)=\prod_{i=1}^{d} \theta_{i}
$$

where $\theta_{i}$ is the conditional probability $P\left(x_{i} \mid x_{p o_{i}}\right)$, and $x_{p o_{i}}$ is the set of parent variables of $x_{i}$. Suppose the consumer obtains $n$ complete observations, $D=\left\{\left(x_{1}^{t}, \ldots, x_{d}^{t}\right), t=\right.$ $1, \ldots, n\}$. In a fully observable environment, $\theta_{i}$ can be learned from the observed data by Maximum Likelihood Estimation (MLE) [Buntine 1994].

In our model, each parameter $\theta_{i}$ represents trust: the conditional probability of obtaining a good outcome from $x_{i}$ given obtaining a good outcome from each of the services in $x_{p o_{i}}$. We assume that all variables $x_{i}$ are pairwise independent and identically distributed (i.i.d.). $\theta$ is the set of all parameters $\theta_{i}$. The likelihood function is defined as the probability of the observations given the parameters. Following Bishop [2006], we write this as

$$
\begin{aligned}
P(D \mid \theta) & =\prod_{t=1}^{n} P\left(x_{1}^{t}, \ldots, x_{d}^{t} \mid \theta\right) \\
& =\prod_{t=1}^{n} \prod_{i=1}^{d} \theta_{i} \\
& =\prod_{i=1}^{d} \prod_{x_{i}, x_{p o_{i}}} \theta_{i}^{n\left(x_{i}, x_{p o_{i}}\right)} \\
& =\prod_{i=1}^{d} \theta_{i}^{m_{i}}\left(1-\theta_{i}\right)^{l_{i}}
\end{aligned}
$$

where $n\left(x_{i}, x_{p o_{i}}\right)$ is the number of observations that satisfy the variable assignment, $m_{i}=n\left(x_{i}, x_{p o_{i}}\right)$, and $l_{i}=n\left(x_{p o_{i}}\right)-m_{i}$. Then, given the observations, the parameters that maximize the likelihood are

$$
\hat{\theta}_{i}=\frac{m_{i}}{m_{i}+l_{i}}
$$

For example, suppose a consumer obtains 10 good outcomes out of 15 interactions with service $x_{i}$, given that $x_{p o_{i}}$ provides good services. Then we have, $m_{i}=n\left(x_{i}=\right.$ $\left.1, x_{p o_{i}}=1\right)=10$ and $l_{i}=n\left(x_{p o_{i}}=1\right)-m_{i}=15-10=5$. From these observations, the consumer can calculate that the estimated trustworthiness $\hat{\theta}_{i}$ is $\frac{10}{15}$. By using MLE, a

[^0]
[^0]:    (c) 2011 ACM 1556-4665/2011/02-ART5 $\$ 10.00$

    DOI 10.1145/1921641.1921646 http://doi.acm.org/10.1145/1921641.1921646

consumer can estimate the trustworthiness of a service from the consumer's observations of it.

# A. 2 Bayesian Inference 

Note that when the number of observations is small, MLE may yield overfitted results. Consider an extreme case where $x_{i}^{t}=1$ for $t=1, \ldots, n$. That is, all the observations are the best possible. The parameter $\hat{\theta}_{i}$ maximizing the likelihood is $\frac{a}{a}=1$, which is not reasonable. Thus, we use Bayesian inference to treat this problem by introducing a beta distribution $P\left(\theta_{i}\right)$ over the parameter $\theta_{i}$ as a conjugacy prior [Bishop 2006, Chapter 2].

$$
P\left(\theta_{i}\right)=\frac{\Gamma\left(\alpha_{i}+\beta_{i}\right)}{\Gamma\left(\alpha_{i}\right) \Gamma\left(\beta_{i}\right)} \theta_{i}^{\alpha_{i}-1}\left(1-\theta_{i}\right)^{\beta_{i}-1}
$$

Here $\alpha_{i}$ and $\beta_{i}$ are hyperparameters controlling the distribution of the parameter $\theta_{i}$, and $\Gamma(x)=\int_{0}^{\infty} u^{x-1} e^{-u} d u$. The coefficient $\frac{\Gamma\left(\alpha_{i}+\beta_{i}\right)}{\Gamma\left(\alpha_{i}\right) \Gamma\left(\beta_{i}\right)}$ in Eq. (10) ensures $\int_{0}^{1} P\left(\theta_{i}\right) d \theta_{i}=1$. We simplify the coefficient to a function $B$ of the hyperparameters $\alpha_{i}$ and $\beta_{i}$, yielding

$$
P\left(\theta_{i}\right)=B\left(\alpha_{i}, \beta_{i}\right) \theta_{i}^{\alpha_{i}-1}\left(1-\theta_{i}\right)^{\beta_{i}-1}
$$

The expected value or mean of $\theta_{i}$ is given by $E\left(\theta_{i}\right)=\frac{\alpha_{i}}{\alpha_{i}+\beta_{i}}$. Bayesian inference uses observations to update the prior. The parameters $\theta_{i}$ can be learned using Bayes' rule.

$$
P\left(\theta_{i} \mid D\right)=\frac{P\left(D \mid \theta_{i}\right) P\left(\theta_{i}\right)}{P(D)}
$$

That is, the posterior distribution $P\left(\theta_{i} \mid D\right)$ is proportional to the multiplication of the prior $P\left(\theta_{i}\right)$ and the likelihood function $P\left(D \mid \theta_{i}\right)$. Now we combine Eqs. (9), (11), and (12) to obtain

$$
P\left(\theta_{i} \mid D\right)=B\left(m_{i}+\alpha_{i}, l_{i}+\beta_{i}\right) \theta_{i}^{m+\alpha_{i}-1}\left(1-\theta_{i}\right)^{l_{i}+\beta_{i}-1}
$$

Note that the posterior distribution is also a beta distribution with hyperparameters $m_{i}+\alpha_{i}$ and $l_{i}+\beta_{i}$. Here we assume the values of $x_{i}$ are independent of $\theta_{i}$, that is, $P\left(D \mid \theta_{i}\right)=$ $\theta_{i}$. Then the predictive distribution of $x_{i}$ given the observations $D$ is defined by the mean of $\theta_{i}$ given the observations $D$. This enables consumers to learn the parameters from the observations without the problems caused by MLE in some extreme cases.

$$
\begin{aligned}
P\left(x_{i} \mid D\right) & =\int_{0}^{1} P\left(x_{i} \mid \theta_{i}\right) P\left(\theta_{i} \mid D\right) d \theta_{i} \\
& =\int_{0}^{1} \theta_{i} P\left(\theta_{i} \mid D\right) d \theta_{i} \\
& =E\left(\theta_{i} \mid D\right) \\
& =\frac{m_{i}+\alpha_{i}}{m_{i}+\alpha_{i}+l_{i}+\beta_{i}}
\end{aligned}
$$

Bayesian inference provides an intuitive way to update the trust (a beta distribution) placed in a service. For example, let a consumer's current trust value of service $x_{i}$ be $\theta_{i}=\left(\alpha_{i}, \beta_{i}\right)=(5,5)$. Suppose the consumer observes two new good outcomes and one bad outcome. The consumer can update the trust value by simply adding the new observations to the previous value. That is, $\hat{\theta}_{i}=\left(\hat{a}_{i}, \hat{\beta}_{i}\right)=(7,6)$. Then the consumer can predict that the probability of obtaining a satisfactory quality value from the next interaction is $\frac{7}{13}$.

![img-0.jpeg](img-0.jpeg)

Fig. 11. Service composition example.
Table III. An Example Observation Derived from a Consumer's Experience


Additionally, to incorporate the dynamism of service behavior, a discount factor $\gamma$ reduces the impact of the old information when we calculate the posterior distribution. In other words, instead of Eq. (17) we have

$$
P\left(x_{i} \mid D\right)=\frac{m_{i}+\gamma a_{i}}{m_{i}+\gamma a_{i}+l_{i}+\gamma \beta_{i}}
$$

The notion of a discount factor is common in trust and reputation systems. The estimate reflects the overall behavior if it is high; otherwise, the estimate depends more on the recent behavior. Hang et al. [2008] study the effect of the discount factor on updating trust estimates. Section 4.2 shows how our approach keeps track of dynamic service behavior in a service composition.

# B. EXTENDED EXAMPLE FOR BAYESIAN APPROACH 

We can implement a sequential approach to construct and learn the service composition model from observations. Taking the scenario of Figure 11 as an example, Table III shows the incomplete observations from a consumer in terms of its response time. In the first observation, the consumer interacts with the hotel service $H$ and obtains a satisfactory response time. The consumer is also aware of the constituent Four Seasons Hotel service $f$ and its good response time. In the second observation, the consumer interacts with the car rental service $C$ but with a bad response time. Here the consumer is not aware of any constituent services. In the third observation, the consumer directly interacts with the travel service $T$ with a positive experience. Here the consumer also realizes the presence of the two constituent services $H$ and C. $T$ reports service $H$ as offering good outcomes and service $C$ as offering bad outcomes. Service $C$ further reports its bad response time as having been caused by its constituent Enterprise service $e$.

Table IV shows the parameters estimated using Bayesian inference. The parameters are represented as pairs of hyperparameters $\alpha_{i}, \beta_{i}$ of the corresponding beta distribution. The numbers in the parentheses in Table III are the inferred counts to

5:App-4
C.-W. Hang and M. P. Singh

Table IV. Parameter Estimation Over Time Based on the Observations of Table III


complete the missing data in the E step. For example, $n\left(x_{f}^{2}=1\right)=E\left(\theta_{f}^{1}\right)=\frac{\sigma_{f}^{1}}{\sigma_{f}^{1}+\beta_{f}^{1}}=0.67$. Then we can infer $n\left(x_{H}^{2}=1\right)$ as follows.

$$
\begin{aligned}
n\left(x_{H}^{2}=1\right) & =n\left(x_{H}^{2}=1 \mid x_{f}^{2}=1\right)+n\left(x_{H}^{2}=1 \mid x_{f}^{2}=0\right) \\
& =P\left(x_{H}^{2}=1 \mid x_{f}^{2}=1\right) P\left(x_{f}^{2}=1\right)+P\left(x_{H}^{2}=1 \mid x_{f}^{2}=0\right) P\left(x_{f}^{2}=0\right) \\
& =0.5 \times 0.33+0.67 \times 0.67=0.61
\end{aligned}
$$

Subsequently, we use the completed data to update the parameter estimation. For example, the new estimation $\theta_{H}^{2}$ (including $\theta_{H \mid f=0}^{2}$ and $\theta_{H \mid f=1}^{2}$ ) is given by

$$
\begin{aligned}
& \left(\alpha_{H \mid f=1}^{2}, \beta_{H \mid f=1}^{2}\right) \\
& \quad=\left(\alpha_{H \mid f=1}^{1}+n\left(x_{H}^{2}=1, x_{f}^{2}=1\right), \beta_{H \mid f=1}^{1}+n\left(x_{H}^{2}=0, x_{f}^{2}=1\right)\right) \\
& \quad=\left(2+P\left(x_{H}^{2}=1 \mid x_{f}^{2}=1\right) \times x_{f}^{2}, 1+P\left(x_{H}^{2}=0 \mid x_{f}^{2}=1\right) \times x_{f}^{2}\right) \\
& \quad=(2.44,1.22) \\
& \left(\alpha_{H \mid f=0}^{2}, \beta_{H \mid f=0}^{2}\right) \\
& \quad=\left(\alpha_{H \mid f=0}^{1}+n\left(x_{H}^{2}=1, x_{f}^{2}=0\right), \beta_{H \mid f=0}^{1}+n\left(x_{H}^{2}=0, x_{f}^{2}=0\right)\right) \\
& \quad=\left(1+P\left(x_{H}^{2}=1 \mid x_{f}^{2}=0\right) \times\left(1-x_{f}^{2}\right), 1+P\left(x_{H}^{2}=0 \mid x_{f}^{2}=0\right) \times\left(1-x_{f}^{2}\right)\right) \\
& \quad=(1.17,1.17)
\end{aligned}
$$

Note that some parameters may not exist until a particular observation because the consumer may not be aware of the corresponding random variables. For example, service $C$ is not reported until the second observation. Further the conditional dependencies may change because some constituent services may be observed later. For example, $\theta_{C \mid e=0}^{1}$ actually means $\theta_{C}^{1}$ in the first observation because service $e$ is not reported. However, $\theta_{C}^{2}$ changes to $\theta_{C \mid e=0}^{2}$ and $\theta_{C \mid e=1}^{2}$ is initialized because service $e$ and the dependency on service $C$ are discovered in the third observation. In these cases, the Bayesian network is updated at the same time to reflect the new discovery.

# C. ADDITIONAL EXPERIMENTAL RESULTS 

Here we present some additional experimental results. The explanations for these graphs (Figures 12, 13, 14, 15) follow those given in the main article.

![img-1.jpeg](img-1.jpeg)

Fig. 12. Beta-mixture approach: estimated beta-mixture and actual distribution of trust in quality for a SUM composition. The composite distribution is learned accurately. However, the beta-mixture approach fails to learn the constituent components well, because the composite histogram tends to follow a unimodal distribution (i.e., only one peak).
![img-2.jpeg](img-2.jpeg)

Fig. 13. Beta-mixture approach: estimated beta-mixture and actual distribution of trust in quality for a PRODUCT composition. Similar to Figure 12, the histogram is accurately fit by the composite distribution, but the accuracy of the constituent distributions is hard to learn because of the unimodal observations.

![img-3.jpeg](img-3.jpeg)

Fig. 14. Beta-mixture approach: estimated beta-mixture and actual distribution of trust in quality for a MIN composition. The histogram is dominated by one constituent component (i.e., one provides good service), which is accurately learned by the beta-mixture approach. Also, beta-mixture accurately estimates the responsibility (dominance) of each component. However, the component other than the dominating one is not accurately learned because of the lack of evidence.
![img-4.jpeg](img-4.jpeg)

Fig. 15. Beta-mixture approach: estimated beta-mixture and actual distribution of trust in quality for a MAX composition. Similar to Figure 14, the composite distribution, and the dominating constituent component is predicted well, but the lack of evidence affects the accuracy of the minor component. However, beta-mixture learns the responsibility (dominance) well.