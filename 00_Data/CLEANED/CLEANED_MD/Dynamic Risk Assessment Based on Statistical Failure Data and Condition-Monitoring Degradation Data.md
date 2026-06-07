# HIAL open science 

## Dynamic Risk Assessment Based on Statistical Failure Data and Condition-Monitoring Degradation Data

Zhiguo Zeng, Enrico Zio

## To cite this version:

Zhiguo Zeng, Enrico Zio. Dynamic Risk Assessment Based on Statistical Failure Data and Condition-Monitoring Degradation Data. IEEE Transactions on Reliability, inPress, pp. 1 - 14. 10.1109/TR.2017.2778804 . hal-01786588

## HAL Id: hal-01786588 <br> https://centralesupelec.hal.science/hal-01786588v1

Submitted on 11 Jan 2022

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Dynamic risk assessment based on statistical failure data and condition-monitoring degradation data 

Zhiguo Zeng and Enrico Zio, Senior Member, IEEE


#### Abstract

Traditional Quantitative Risk Assessment (QRA) methods (e.g., event tree analysis) are static in nature, i.e., the risk indexes are assessed before operation, which prevents capturing time-dependent variations as the components and systems operate, age, fail, are repaired and changed. To address this issue, we develop a Dynamic Risk Assessment (DRA) method that allows online estimation of risk indexes using data collected during operation. Two types of data are considered: statistical failure data, which refer to the counts of accidents or near misses from similar systems and condition-monitoring data, which come from online monitoring the degradation of the target system of interest. For this, a hierarchical Bayesian model is developed to compute the reliability of the safety barriers and a Bayesian updating algorithm, which integrates Particle Filtering (PF) with Markov Chain Monte Carlo (MCMC), is developed to update the reliability evaluations based on both the statistical and conditionmonitoring data. The updated safety barriers reliabilities, are, then, used in an Event Tree (ET) for consequence analysis and the risk indexes are updated accordingly. A case study on a High-Flow Safety System (HFSS) is conducted to demonstrate the developed methods. A comparison to the DRA method which only uses statistical failure data shows that by introducing conditionmonitoring data on the system degradation process, it is possible to capture the system-specific characteristics, and, therefore, provide a more complete and accurate description of the risk of the target system.


Index Terms—Dynamic risk assessment, event tree analysis, hierarchical Bayesian model, condition-monitoring, Particle Filtering (PF), Markov Chain Monte Carlo (MCMC)

## I. INTRODUCTION

QUANTITATIVE Risk Assessment (QRA) has been widely applied in various areas [1-3]. Despite of the wide application, traditional QRA methods (e.g., event tree analysis [4]) have been frequently criticized for being "intrinsically static", i.e., the risk indexes are assessed before systems come into operation, and, so, they do not capture the timedependent variations as components and systems operate, age, fail, are repaired and changed [5]. Dynamic Risk Assessment (DRA) is defined in [6] as a risk assessment method that updates the estimated risk of a deteriorating process according to the performance of the control system, safety barriers, inspection and maintenance activities, the human factors, and the implementation of procedures. Compared to the traditional

[^0]${ }^{\text {a }}$ Static" QRA, DRA is capable of capturing the time-dependent behaviors of the risk indexes and provides a more realistic description of the system risk $[3,5,6]$.

Traditionally, DRA methods use only statistical failure data for risk updating, which refer to count data of accidents or near misses from similar systems [7, 8]. A drawback of using only statistical failure data is that, one has to wait for accidents or near misses (precursors) to occur before updating the estimation of the risk indexes. Besides, statistical failure data are collected from similar systems, reflecting population characteristics but not fully accounting for the individual features of the target system. A beneficial complement of statistical failure data is condition-monitoring data, which come from the online monitoring of the system's operational state and degradation process [9]. Condition-monitoring data contain information on the individual degradation process of the target system and, therefore, provide the opportunity to update the reliability values before actual failures occur. Hence, integrating condition-monitoring data with statistical failure data can significantly enhance the effectiveness of DRA.

Statistical failure data and condition-monitoring data have been used separately for DRA but the integration of the two data sources for DRA remains an open issue. To fill this gap, we develop a novel method for DRA that integrates both statistical and condition-monitoring data. The main contribution of the paper can be summarized as follows:

- A hierarchical Bayesian reliability model is developed for incorporating both statistical failure data and conditionmonitoring data;
- A hybrid MH/Gibbs algorithm is developed for dynamic reliability assessment;
- A sequential Bayesian method is developed by integrating the two data sources in DRA.
The rest of this paper is organized as follows. The developed DRA method is presented in Section III and applied in Section IV to a high-flow safety alarm system. Finally, the paper is concluded in Section V with a discussion of potential future work.


## II. Related works

In this section, we review existing works related to DRA. Based on the data used for DRA, we divide the existing works into two categories: in Sub-Section II-A, we discuss DRA methods using statistical failure data, while in SubSection II-B, we focus on DRA methods using conditionmonitoring data.


[^0]:    Zhiguo Zeng is a postdoc researcher at Chair on System Science and the Energy Challenge, Fondation Electricite de France (EDF), CentraleSupélec, Université Paris-Saclay, Grande Voie des Vignes, 92290 Chatenay-Malabry, France. Email: zhiguo.zeng@centralesupelec.fr.

    Enrico Zio is a professor at Chair on System Science and the Energy Challenge, Fondation Electricite de France (EDF), CentraleSupélec, Université Paris-Saclay, Grande Voie des Vignes, 92290 Chatenay-Malabry, France and Energy Department, Politecnico di Milano, Milano, Italy. Emails: en-rico.zio@centralesupelec.fr, enrico.zio@polimi.it.

It should be noted that as [6], the DRA methods discussed in this paper only consider the time-dependent behavior of the failure probability of the safety barriers. The system failure logic, on the contrary, remains static, i.e., does not change over time. For DRA with time-dependent failure logic, readers might refer to dynamic fault tree/event tree analysis (e.g., see [10] and [11]).

## A. DRA with statistical failure data

Statistical failure data, also known as Accident Sequence Precursor (ASP) data, refer to count data of accidents or near misses from similar systems [7, 8, 12]. Most existing DRA methods use statistical failure data to update the reliability and risk indexes. For example, an early attempt of DRA was conducted in [7, 8], where Bayes theorem was used to dynamically update the estimates of accident probabilities, using near misses and incident data collected from similar systems. Kalantarnia et al. developed a similar DRA method, where Bayes theorem is used for probability updating and Event Tree (ET) analysis is used for consequence modeling [12]. Roy et al. used ET to model the accident sequences of an ammonia storage unit and Bayes theorem for DRA [13]. Pariyani et al. used ET and Bayes theorem to update the risk in chemical process industries based on data from a large nearmiss data base [14]. Khakzad et al. developed a hierarchical Bayesian model for DRA and applied it to analyze the nearaccident data of offshore blowouts [15]. Yang et al. applied a similar hierarchical Bayesian model to dynamically assess the risk of an offshore drilling platform [16].

In [17], Bayes theorem was combined with a Bow-Tie (BT) model for DRA: failure probabilities of the primary events and safety barriers in the BT were constantly revised over time and the updated BT model was used to estimate the updated risk profile. Paltrinieri et al. used BT to support the DRA from metal dust accidents [18]. Abimbola et al. applied a similar method to update in real time the risk estimation of offshore drilling operations [19]. Khakzad et al. developed a DRA method using a Bayesian Network (BN) model, where the probabilities of the basic events in the BN are updated when new accident data are collected [20]. A comparison of the BT-based and BN-based methods were made in [21], and a procedure was given to map a BT into a BN. Li et al. considered the DRA for assessing the risk of leakage failure in submarine oil and gas pipelines using BT and BN [22]. In [23], Zarei et al. applied the BN in the DRA of a natural gas station.

The DRA methods reviewed above use only statistical failure data for risk updating. As mentioned in Section I, one significant drawback of statistical failure data is that they cannot give alerts prior to the occurrence of accidents, since they are collected at failure. Another issue is that statistical failure data are collected from a population of similar systems, and, therefore, do not fully account for the system-specific features of the target system.

## B. DRA with condition-monitoring data

Condition-monitoring data refer to the online-monitoring data related to the system's operational state and degradation
processes [9]. In practice, accident initiating events and safety barriers failures usually occur as a result of degradation mechanisms, e.g., wear [24], corrosion [25], fatigue [26], crack growth [27], oxidation [28], etc. These degradation processes can be monitored and failures can be predicted and anticipated with reference to specific thresholds of the monitored variables. Condition-monitoring data contain information on the individual degradation process of the target system and provide the opportunity to update the reliability values before actual failures occur.

There are a few initial attempts of using conditionmonitoring data in DRA. For example, Zadakbar et al. applied Kalman filtering to estimate the true degradation states from condition-monitoring data and conducted DRA based on a loss function associated with the degradation states [29]. Similar works were also conducted by the same authors using different condition-monitoring techniques, i.e., Particle Filtering (PF) [30] and Principal Component Analysis (PCA) [31]. To deal with nonlinear and non-Gaussian features, Yu et al. developed a self-organizing map-based approach for DRA using condition-monitoring data [32]. Wang et al. proposed the concept of remaining time and used it to develop a DRA method for multiple condition-monitoring variables [33]. Liu and Zio [34] presented a Bayesian reliability updating method using condition-monitoring data considering the dependencies between two components. Kim et al. conducted a DRA by monitoring sensitive variables of a passive residual heat removal system, but without considering the possible noise in the monitored data [9].

Condition-based Fault Tree Analysis (CBFTA) is developed by Shalev and Tiran [35] for DRA, where the failure rates of the basic events are updated using condition-monitoring data, such as vibration, electrical current, etc. Hu et al. developed a DRA method based on Dynamic Bayesian Network (DBN), where condition-monitoring data from a process monitoring system are used to update the parameters of the DBN model [36]. Gomes et al. applied Kalman filter to predict the Remaining Useful Life (RUL) of the components, and then conduct DRA using a fault tree model [37]. Aizpurua et al. developed a dynamic dependability assessment framework where prognostic capability has been introduced to update the reliabilities of some minimal cut-sequence sets [38]. In [39], a dynamic Bayesian network is constructed for reliability centered maintenance planning, where the conditional probabilities of the nodes are updated based on condition-monitoring data using a Kalman filter.

The works reviewed above use only condition-monitoring data for risk updating, and do not consider statistical failure data. How to integrate condition-monitoring data with statistical failure data, then, remains a challenge for a more informed DRA. To address this issue, we develop a new DRA method. Compared to the existing methods, the developed method integrates statistical failure data and condition-monitoring data for risk model updating, and, therefore, provides a more condition-informed result from the risk assessment. It should be noted that by "integrate", we mean using both statistical failure data and condition-monitoring data to update the initial distribution of the risk index, which is derived based on

historical data. In this context, both condition-monitoring data and statistical failure data serve as evidence, i.e., they should appear in the likelihood function part of the Bayesian updating framework.

## III. A NOVEL METHOD FOR DRA

In this section, we develop a new DRA method that considers both statistical and condition-monitoring data. The problem we intend to address in this paper is formally defined in Subsection III-A. A first step in the DRA is to online update the reliability of the safety barriers using the two types of data. For this, a hierarchical Bayesian reliability model is developed in Subsection III-B. Based on the model, an online assessment algorithm is developed for the reliability values of the safety barriers in Subsection III-C and III-D. Finally, a sequential Bayesian algorithm is developed in Subsection III-E to update the risk indexes using the revised reliability values of the safety barriers.

## A. Problem definition

Without loss of generality, we consider an ET with $n$ possible consequences $C_{1}, C_{2}, \cdots, C_{n}, m$ safety barriers $B_{1}, B_{2}, \cdots, B_{m}$ and an initial event IE. Conceptually, the ET can be expressed as

$$
\mathbf{r}_{C}=g_{\mathrm{ETA}}\left(R_{B_{1}}, R_{B_{2}}, \cdots, R_{B_{m}} \mid \mathrm{IE}\right)
$$

where $R_{B_{i}}$ is the reliability of the $i$ th safety barrier and $\mathbf{r}_{C}=$ $\left[r_{C_{1}}, r_{C_{2}}, \cdots, r_{C_{n}}\right]$ is the consequence risk index considered in this paper, which is measured by the conditional occurrence probability of the consequence given that IE has occurred:

$$
r_{C_{i}}=\operatorname{Pr}\left\{C_{i} \mid \text { IE has occurred }\right\}, i=1,2, \cdots, n
$$

In this paper, we consider the dynamic assessment of the risk indexes as defined in (1), using both statistical failure data and condition-monitoring data. Statistical data refer to the count data of the consequences of accidents that occur during the operation of similar systems, thus providing "population" information, while condition-monitoring data come from online monitoring the degradation of the specific target system of interest and describe system-specific features. More specifically, it is assumed that:

1) statistical failure data and condition-monitoring data are collected at predefined observation instants $t=t_{j}, j=$ $1,2, \cdots, q$
2) the collected statistical failure data are denoted by $N_{k, j}, k=1,2, \cdots, n$, where $N_{k, j}$ denotes the number of the $k$ th consequences that occur in the interval $\left(t_{j-1}, t_{j}\right]$ and $t_{0}=0$
3) the collected condition-monitoring data on the $i$ th safety barrier at $t=t_{j}$ are denoted by $y_{i, j}, i=1,2, \cdots, m$ and $j=1,2, \cdots, q$
4) the degradation threshold for the $i$ th safety barrier is $y_{i h, i}$ and failure of the $i$ th safety barrier occurs when $y_{i, j} \leq y_{i h, i}$.
The problem of DRA can, then, be defined as: at each $t=$ $t_{j}, j=1,2, \cdots, q$, update the estimation of $\mathbf{r}_{C}$ in (1), based on statistical failure data $N_{k, j}$ and condition-monitoring data $y_{i, j}$.

## B. Hierarchical Bayesian model for safety barrier reliability updating

In this section, a hierarchical Bayesian model is developed for evaluating the reliability of the safety barriers considering both statistical and condition-monitoring data. The model is based on the following assumptions:

1) in each interval $\left(t_{j-1}, t_{j}\right], j=1,2, \cdots, q$, the $i$ th safety barrier in the population of similar systems has reliability $\pi_{i, j}$, where $\pi_{i, j}$ is a random variable with prior distribution $p_{0, \pi_{i, j}}$ and posterior distribution $p_{1, \pi_{i, j}}$ and $t_{0}=0$
2) the prior distribution of $\pi_{i, 1}$ is a Beta distribution with parameter $\alpha_{i}$ and $\beta_{i}$ :

$$
\pi_{i, 1} \sim \operatorname{Beta}\left(\alpha_{i}, \beta_{i}\right)
$$

while for $j \geq 2, p_{0, \pi_{i, j}}=p_{1, \pi_{i, j-1}}$
3) in each interval $\left(t_{j-1}, t_{j}\right], j=1,2, \cdots, q$, the reliability of the $i$ th safety barrier in the target system of interest, denoted by $R_{B, i, j}$, is a random variable whose prior distribution is a Beta distribution:

$$
R_{B, i, j} \sim \operatorname{Beta}\left(K \pi_{i, j}, K\left(1-\pi_{i, j}\right)\right)
$$

where $\pi_{i, j}$ follows its posterior distribution $p_{1, \pi_{i, j}}$.
4) $K$ is a random variable with uniform prior distribution:

$$
K \sim \operatorname{Uniform}\left(K_{L}, K_{U}\right)
$$

From Assumption 1, the statistical count data of occurrence of accidents with given consequences in each interval can be modeled by a binomial probability model:

$$
\operatorname{Pr}\left\{N_{S, i, j}, N_{F, i, j} \mid \pi_{i, j}\right\} \propto \pi_{i, j}^{N_{S, i, j}}\left(1-\pi_{i, j}\right)^{N_{F, i, j}}
$$

where $N_{S, i, j}$ and $N_{F, i, j}$ represent the number of successes and failures of the $i$ th safety barrier in $\left(t_{j-1}, t_{j}\right]$, respectively. The detailed procedures for calculating $N_{S, i, j}$ and $N_{F, i, j}$ from the statistical failure data are given in Subsection III-C. The reason for us to choose the binomial model is that the statistical failure data on the safety barriers are of failure-on-demand type [40, 41]. Equation (6) serves as the likelihood function for the statistical failure data. It should be noted that, for simplicity, we drop the constants in the likelihood function, since they do not affect the derivation of posterior distributions in Bayes theorem [42].

According to Assumption 2, at each $t_{j}, j=1,2, \cdots, q$, the prior distribution in (3) can be updated recursively based on Bayesian theorem [41]. Since the likelihood function in (6) is conjugate to the Beta prior in (3), the posterior $p_{1, \pi_{i, j}}$ is also a Beta distribution [41]:

$$
\pi_{i, j} \sim \operatorname{Beta}\left(\alpha_{i}+\sum_{\tau=1}^{j} N_{S, i, \tau}, \beta_{i}+\sum_{\tau=1}^{j} N_{F, i, \tau}\right)
$$

Assumption 3 relates the condition-monitoring data to the statistical failure data. To explain it, note that the mean value of the Beta distribution in (4) is calculated by [41]:

$$
E\left[R_{B, i, j}\right]=\frac{K \pi_{i, j}}{K \pi_{i, j}+K\left(1-\pi_{i, j}\right)}=\pi_{i, j}
$$

Therefore, it is assumed that statistical failure data from similar systems determine the mean value of the reliability of the target system under condition-monitoring. Let $M_{S, i, j}$ and $M_{F, i, j}$ denote the number of successes and failures of the $i$ th safety barrier in $\left(t_{j-1}, t_{j}\right]$, respectively. Assumption 3 also indicates that $M_{S, i, j}$ and $M_{F, i, j}$ can be modeled by a binomial model:

$$
\operatorname{Pr}\left\{M_{S, i, j}, M_{F, i, j} \mid R_{B, i, j}\right\} \propto R_{B, i, j}^{M_{S, i, j}}\left(1-R_{B, i, j}\right)^{M_{F, i, j}}
$$

Note that $M_{S, i, j}$ and $M_{F, i, j}$ have to be generated from condition-monitoring data by conducting "pseudo-tests", since in practice, we have only one sample, i.e., that of the target system under condition-monitoring. Detailed procedures of generating $M_{S, i, j}$ and $M_{F, i, j}$ are discussed in details in Subsection III-C. Equation (8) is the likelihood function for the condition-monitoring data. As in (6), the constants in the likelihood function are dropped since they do not affect the derivation of the posterior distributions [41].

As discussed in [41], $K$ can be regarded as the "prior sample size". Let $M=M_{S, i, j}+M_{F, i, j}$ denote the sample size of the pseudo-tests based on the condition-monitoring data. Roughly speaking, the ratio between $K$ and $M$ measures the trust on the statistical failure data compared to the condition-monitoring data: a high value of $K / M$ indicates that one has more trust on the statistical failure data than the condition-monitoring data, and vice versa. In practice, the value of $K$ should be determined based on the value of $M$ to reflect the weight of trust on the two types of data. A detailed discussion on the effect of $K$ is given in Section IV-C. Assumption 4 accounts for the uncertainty in determining the precise value of $K$.

Some existing works can be found in literature for DRA, e.g., [7], [20], [12], etc. These models, however, do not assume a hierarchical structure for the reliability and, therefore, can only be used for modeling statistical failure data. Compared to the existing models, the uniqueness of the developed model is that it proposes a hierarchical Bayesian model, which allows integrating both statistical failure data and conditionmonitoring data.

## C. Generating pseudo-test data

Pseudo-test data are an important concept in the developed DRA method. They are generated, based on the collected data, (either statistical failure data or condition-monitoring data), to represent the "equivalent" binomial tests and failure data on each safety barrier. In this paper, we distinguish two types of pseudo-tests:

1) Statistical data-based pseudo-tests: Statistical data $\left(N_{k, j}, k=1,2, \cdots, n, j=1,2, \cdots, q\right)$ count the number of occurrences of the consequences in each observation interval. Note that in an ET, observing a certain consequence indicates that the events associated to it have occurred. Since the events correspond to success or failure of the safety barriers, the statistical failure data can be viewed as pseudo-tests on the safety barriers. Take a simple ET in Figure 1 as an example. From Figure 1, we can see that if consequence $C_{2}$ occurs, safety barrier $B_{1}$ must be working and $B_{2}$ must be failed.

Therefore, the occurrence of $C_{2}$ is equivalent to a pseudotest on $B_{1}$ whose result is success and a pseudo-test on $B_{2}$ whose result is failure. The same reasoning applies to the other consequences and safety barriers. Let us define an indicator function $\mathbb{1}\left(B_{i}, C_{k}\right)$ :

$$
\mathbb{1}\left(B_{i}, C_{k}\right)=\left\{\begin{array}{l}
1, \text { if the occurrence of } C_{k} \text { indicates the } \\
\text { success of the } i \text { th safety barrier, } \\
0, \text { if the occurrence of } C_{k} \text { indicates the } \\
\text { failure of the } i \text { th safety barrier. }
\end{array}\right.
$$

The pseudo-test data $N_{S, i, j}$ and $N_{F, i, j}$ can, then, be calculated from $N_{k, j}$ :

$$
\begin{aligned}
& N_{S, i, j}=\sum_{k=1}^{n} \mathbb{1}\left(B_{i}, C_{k}\right) \cdot N_{k, j} \\
& N_{F, i, j}=\sum_{k=1}^{n}\left(1-\mathbb{1}\left(B_{i}, C_{k}\right)\right) \cdot N_{k, j}
\end{aligned}
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. An illustrative ET
2) Condition-monitoring data-based pseudo-tests: Condition-monitoring data $\left(y_{i, j}, j=1,2, \cdots, q\right)$ are collected by online-monitoring the degradation process of the $i$ th safety barrier at $t=t_{j}, j=1,2, \cdots, q$. Since condition-monitoring data are often subject to process and observation noises, PF is used in this paper to estimate the true degradation states. PF is chosen for its flexibility and ability to handle complex nonlinear system dynamics and non-Gaussian noises. Although other methods, such as extended Kalman filter and unscented Kalman filter, might also be applied on nonlinear and non-Gaussian problems, they are based on Taylor approximation of a non-linear function. PF, on the other hand, does not require such approximation and fully represent the nonlinear system dynamics.

It is assumed that the degradation process of the $i$ th safety barrier follows a state space model [43]:

$$
\left\{\begin{array}{l}
\mathbf{x}_{i, j}=g_{i}\left(\mathbf{x}_{i, j-1}, \epsilon_{i}\right) \text { (state equation) } \\
y_{i, j}=h_{i}\left(\mathbf{x}_{i, j}, \delta_{i}\right) \text { (observation equation) }
\end{array}\right.
$$

where $\mathbf{x}_{i, j}$ is the state variable, $y_{i, j}$ is the observation, $\epsilon_{i}$ is the process noise and $\delta_{i}$ is the observation noise. In PF, the forms of $g_{i}(\cdot)$ and $h_{i}(\cdot)$ are assumed to be known and the true system state $\mathbf{x}_{i, j}, j=1,2, \cdots, q$ are estimated recursively based on Bayesian theorem [43, 44] (Eq. (13)), where in (13), $p\left(\mathbf{x}_{i, j} \mid y_{i, 1}, y_{i, 2}, \cdots, y_{i, j}\right)$ is the posterior density for $\mathbf{x}_{i, j}$, updated at $t=t_{j} ; p\left(y_{i, j} \mid \mathbf{x}_{i, j}\right)$ is determined by the

observation equation in (11) and $p\left(\mathbf{x}_{i, j} \mid y_{i, 1}, y_{i, 2}, \cdots, y_{i, j-1}\right)$ is determined based on the output of the PF at $t=t_{j-1}$.

In practice, (13) is evaluated using sequential Monte Carlo simulations: at each $t_{j}, p\left(\mathbf{x}_{i, j} \mid y_{i, 1}, y_{i, 2}, \cdots, y_{i, j}\right)$ is approximated by

$$
p\left(\mathbf{x}_{i, j} \mid y_{i, 1}, y_{i, 2}, \cdots, y_{i, j}\right) \approx \sum_{k=1}^{N_{P}} w_{i, j}^{(k)} \delta\left(\mathbf{x}_{i, j}-\mathbf{x}_{i, j}^{(k)}\right)
$$

where $\left\{\mathbf{x}_{i, j}^{(k)}, w_{i, j}^{(k)}\right\}, k=1,2, \cdots, N_{P}$ are the samples (referred to as "particles") and the associated weights generated by sequential importance sampling, and $\delta(\cdot)$ is the Dirac delta function.

It is shown in [43] that if at each $t=t_{j}$, the particles are generated by

$$
\mathbf{x}_{i, j}^{(k)} \sim p\left(\mathbf{x}_{i, j} \mid \mathbf{x}_{i, j-1}\right)
$$

where $p\left(\mathbf{x}_{i, j} \mid \mathbf{x}_{i, j-1}\right)$ is the proposal density of the importance sampling and is determined by the state equation in (11), then, the weights can be updated by

$$
w_{i, j}^{(k)}=\frac{w_{i, j-1}^{(k)} p\left(y_{i, j} \mid \mathbf{x}_{i, j}^{(k)}\right)}{\sum_{k=1}^{N_{P}} w_{i, j-1}^{(k)} p\left(y_{i, j} \mid \mathbf{x}_{i, j}^{(k)}\right)}
$$

Algorithm 1 [43] summarizes the major steps of the PF here employed. The purpose of resampling in Algorithm 1 is to avoid the well known problem of particle degeneracy and resampling is often conducted by sampling with replacement from $\left\{\mathbf{x}_{i, j-1}^{(k)}, w_{i, j-1}^{(k)}\right\}_{k=1}^{N_{P}}$ [45].

Algorithm 1 PF-based estimation of the states of the safety barriers [43]
Inputs: $\left\{\mathbf{x}_{i, j-1}^{(k)}, w_{i, j-1}^{(k)}\right\}_{k=1}^{N_{P}}, y_{i, j}$
Outputs: $\left\{\mathbf{x}_{i, j}^{(k)}, w_{i, j}^{(k)}\right\}_{k=1}^{N_{P}}$
1: for $k=1: N_{P}$ do
2: Sample $\mathbf{x}_{i, j}^{(k)}$ using (14);
3: end for
4: Update $w_{i, j}^{(k)}, k=1,2, \cdots, N_{P}$, using (15);
5: $N_{e f f}^{-} \leftarrow\left(\sum_{k=1}^{N_{P}}\left(w_{i, j}^{(k)}\right)^{2}\right)^{-1}$;
6: if $N_{e f f}^{-}<N_{P} / 2$ then
7: Update $\mathbf{x}_{i, j}^{(k)}$ and $w_{i, j}^{(k)}$ by resampling;
8: end if
9: return $\left\{\mathbf{x}_{i, j}^{(k)}, w_{i, j}^{(k)}\right\}_{k=1}^{N_{P}}$.

At each $t=t_{j}$, the posterior density of $\mathbf{x}_{i, j}$ is approximated by the updated particles and weights from sequential importance sampling. Therefore, the particles can be viewed as pseudo-tests on the reliability of the safety barriers, based on which $M_{S, i, j}$ and $M_{F, i, j}$ can be generated (Algorithm 2).

## D. Updating the reliability of the safety barriers

In this section, we discuss how to update the reliability of the safety barriers based on the pseudo-test data generated

Algorithm 2 Generating pseudo-test data based on PF
Inputs: $\left\{\mathbf{x}_{i, j}^{(k)}, w_{i, j}^{(k)}\right\}_{k=1}^{N_{P}}, y_{i, t h}$
Outputs: $M_{S, i, j}, M_{F, i, j}$
1: $M_{S, i, j}=0, M_{F, i, j}=0$
2: for $k=1: N_{P}$ do
3: $\quad \mathbf{x}_{\text {pseudo }}^{(k)} \leftarrow$ Randomly select one element from $\left\{\mathbf{x}_{i, j}^{(k)}\right\}_{k=1}^{N_{P}}$, where $\mathbf{x}_{i, j}^{(k)}$ is selected with probability $w_{i, j}^{(k)}$;
4: $\quad$ Calculate $y_{\text {pseudo }}^{(k)}$ using the observation equation in (11);
5: if $y_{\text {pseudo }}^{(k)}>y_{i, t h}$ then
6: $\quad M_{S, i, j}=M_{S, i, j}+1$;
7: else
8: $\quad M_{F, i, j}=M_{F, i, j}+1$;
9: end if
10: end for
11: return $M_{S, i, j}, M_{F, i, j}$.
in Subsection III-C. The updating is done in two stages. In the first stage, statistical failure data are used to update the reliability of similar systems $\left(\pi_{i, j}\right)$. As shown in Assumption 2, the prior distribution of $\pi_{i, j}$ and the statistical failure data follow a beta-binomial model [41]. Therefore, the posterior density of $\pi_{i, j}$ can be recursively updated using (7). The updated posterior density is, then, combined with conditionmonitoring data in the second stage to update the reliability of the safety barriers $\left(R_{B, i, j}\right)$.

To do this, first note that $R_{B, i, j}$ is modeled by a hierarchical Bayesian model with a hyper-parameter $K$ (see Assumptions (3) and (4) in Subsection III-B). It should be mentioned that the $\pi_{i, j}$ in (4) is not regarded as a hyper-parameter, but as a random variable with a fixed probability distribution (i.e., $p_{1, \pi_{i, j}}$ yielded by the first stage updating). Based on Bayes theorem [41], the joint posterior density of $R_{B, i, j}$ and $K$, denoted by $p_{1}\left(R_{B, i, j}, K\right)$, can be expressed as

$$
\begin{aligned}
p_{1}\left(R_{B, i, j}, K\right) \triangleq & p\left(R_{B, i, j}, K \mid M_{S, i, j}, M_{F, i, j}\right) \\
& \propto p\left(M_{S, i, j}, M_{F, i, j} \mid R_{B, i, j}\right) \\
& p\left(R_{B, i, j} \mid K\right) \cdot p(K)
\end{aligned}
$$

where $p\left(M_{S, i, j}, M_{F, i, j} \mid R_{B, i, j}\right)$ is the likelihood function in (8), $p\left(R_{B, i, j} \mid K\right)$ is the prior distribution of $R_{B, i, j}$ in (4), and $p(K)$ is the prior distribution of $K$ in (5). Equation (16) can be further expressed as (20) where $B(\cdot)$ is the Beta function and $\Delta$ is a proportional constant.

Due to the complexity of (20), it is hard to derive the analytical form of $p_{1}\left(R_{B, i, j}, K\right)$. Therefore, we use Markov Chain Monte Carlo (MCMC) to generate samples from $p_{1}\left(R_{B, i, j}, K\right)$. For a detailed discussion of MCMC, readers might refer to Chapter 3 in [41]. Note that in this case, if we fix the value of $K$ in (20), we have (21), which indicates that conditioned on $K$ and the data, $R_{B, i, j}$ follows a Beta distribution:

$$
\begin{array}{rl}
R_{B, i, j} & K, M_{S, i, j}, M_{F, i, j} \\
& \sim \operatorname{Beta}\left(M_{S, i, j}+K \pi, M_{F, i, j}+K(1-\pi)\right)
\end{array}
$$

$$
p\left(\mathbf{x}_{i, j} \mid y_{i, 1}, y_{i, 2}, \cdots, y_{i, j}\right)=\frac{p\left(y_{i, j} \mid \mathbf{x}_{i, j}\right) p\left(\mathbf{x}_{i, j} \mid y_{i, 1}, y_{i, 2}, \cdots, y_{i, j-1}\right)}{\int p\left(y_{i, j} \mid \mathbf{x}_{i, j}\right) p\left(\mathbf{x}_{i, j} \mid y_{i, 1}, y_{i, 2}, \cdots, y_{i, j-1}\right) d \mathbf{x}_{i, j}}
$$

Therefore, in the MCMC, $R_{B, i, j}$ can be updated using Gibbs sampler based on (17) [41]. On the other hand, if we condition on $R_{B, i, j}$ and the data, we have:

$$
\begin{aligned}
p\left(K \mid R_{B, i, j}, M_{S, i, j}, M_{F, i, j}\right) & \propto \\
R_{B, i, j}^{K \pi} \cdot\left(1-R_{B, i, j}\right)^{K(1-\pi)} \cdot & \frac{1}{B(K \pi, K(1-\pi))}
\end{aligned}
$$

which cannot be expressed as any known probability distribution. Therefore, the Metropolis-Hastings (MH) algorithm is used to update $K$. In this case, we choose the proposal distribution to be a Uniform distribution over $\left[K_{L}, K_{U}\right]$, i.e., the same as the prior distribution of $K$. Therefore, the acceptance probability $p_{\text {acc }}$ becomes [41]:

$$
\begin{aligned}
p_{\text {acc }} & =\min \left(1, \frac{p\left(\theta^{*} \mid \text { data }\right)}{p\left(\theta^{(l-1)} \mid \text { data }\right)} \frac{f\left(\theta^{(l-1)} \mid \theta^{*}\right)}{f\left(\theta^{*} \mid \theta^{(l-1)}\right)}\right) \\
& =\min \left(1, \frac{p\left(K^{(*)} \mid R_{B, i, j}, M_{S, i, j}, M_{F, i, j}\right)}{p\left(K^{(l-1)} \mid R_{B, i, j}, M_{S, i, j}, M_{F, i, j}\right)}\right)
\end{aligned}
$$

where $f(\cdot \mid \cdot)$ is the proposal density and the ratio in (19) is calculated based on (18).

A hybrid Gibbs/MH algorithm is developed to dynamically update the reliability of the safety barriers, as shown in Algorithm 3, where $N_{l}$ is the number of the iterations. As $l$ becomes large, $\left\{R^{(l)}, K^{(l)}\right\}$ converge to a random sample from the joint posterior distribution [41]. In practice, the first $N_{\text {burn-in }}$ samples are dropped to reduce the correlation between the samples [42]. Therefore, at each $t=t_{j}$, Algorithm 3 is used to update the reliability of the $i$ th safety barrier and the posterior density of $R_{B, i, j}$ is approximated by $R^{(l)}, l=N_{\text {burn-in }}+1, N_{\text {burn-in }}+2, \cdots, N_{l}$.

One thing that needs special attention when applying Algorithm 3 is to check the convergence of the MCMC samples. Normally, the MCMC algorithms start from initial values that might be far away from the center of the posterior distribution. As the algorithm iterates, the MCMC samples tend to converge to samples from the posterior distribution. In this paper, we use trace plots for the convergence checks: a stable trace plot indicates good convergence, while a trace plot with significant increasing or decreasing trends means that more iterations are needed for convergence [41]. Some numerical indicators, e.g., autocorrelation coefficient, sample standard deviation of the batch means, potential scale reduction, etc., can also be used to monitor the convergence of the MCMC. For more details, readers might refer to Chapter 3 of [41].

## E. A sequential Bayesian updating algorithm for DRA

Once the reliability of the safety barriers are updated, DRA can be done using Algorithm 4. The resulting $\left\{\mathbf{r}_{C}^{(l)}\right\}_{l=1}^{N_{l}-N_{\text {burn-in }}}$ approximate the posterior distribution of $\mathbf{r}_{C}$ updated at $t=t_{j}$. At each $t=t_{j}, j=1,2, \cdots, q$, Algorithm 4 is recursively applied for the DRA.

Algorithm 3 A hybrid Gibbs/MH algorithm to update the reliability of the safety barriers
Inputs: $M_{S, i, j}, M_{F, i, j}, N_{S, i, j}, N_{F, i, j}$
Outputs: $\left\{R^{(l)}, K^{(l)}\right\}_{l=1}^{N_{l}}$
1: Set initial values for $R^{(0)}, K^{(0)}, \pi^{(0)}$;
2: for $l=1: N_{l}$ do
3: $\quad R^{(l)} \leftarrow$ Generate a random sample from (17), where $K=K^{(l-1)}, \pi=\pi^{(l-1)} ;$
4: $\quad K^{*} \leftarrow$ Generate a random sample from the proposal density, i.e., Uniform $\left(K_{L}, K_{U}\right)$;
5: $\quad p_{\text {acc }} \leftarrow$ Calculate $p_{\text {acc }}$ using (19), where $R_{B, i, j}=$ $R^{(l)}, \pi=\pi^{(l-1)} ;$
6: $\quad r \leftarrow$ Generate a sample from Uniform $(0,1)$;
7: if $r \leq p_{\text {acc }}$ then
8: $\quad K^{(l)} \leftarrow K^{*}$;
9: else
10: $\quad K^{(l)} \leftarrow K^{(l-1)}$;
11: end if
12: $\pi^{(l)} \leftarrow$ Generate a random sample from (7);
13: end for
14: return $\left\{R^{(l)}, K^{(l)}\right\}_{l=1}^{N_{l}}$.

Algorithm 4 Sequential Bayesian updating for DRA (for $t=$ $t_{j}$ )
1: for $i=1: m$ do
2: $\quad\left\{N_{S, i, j}, N_{F, i, j}\right\} \leftarrow$ Generate pseudo-test data based on statistical failure data, using (10);
3: $\quad\left\{\mathbf{x}_{i, j}^{(k)}, w_{i, j}^{(k)}\right\}_{k=1}^{N_{P}} \leftarrow$ Particle filtering based on condition-monitoring data, using Algorithm 1;
4: $\quad\left\{M_{S, i, j}, M_{F, i, j}\right\} \leftarrow$ Generate pseudo-test data based on $\left\{\mathbf{x}_{i, j}^{(k)}, w_{i, j}^{(k)}\right\}_{k=1}^{N_{P}}$, using Algorithm 2;
5: $\quad\left\{R_{B, i, j}^{(l)}\right\}_{l=1}^{N_{l}-N_{\text {burn-in }}} \leftarrow$ Update $R_{B, i, j}$ using Algorithm 3;
6: end for
7: for $l=N_{\text {burn-in }}+1: N_{l}$ do
8: $\quad R_{B_{i}} \leftarrow R_{B, i, j}^{(l)}, i=1,2, \cdots, n$;
9: $\quad \mathbf{r}_{C}^{\left(l-N_{\text {burn-in }}\right)} \leftarrow$ Calculate the risk indexes using (1);
10: end for
11: return $\left\{\mathbf{r}_{C}^{(l)}\right\}_{l=1}^{N_{l}-N_{\text {burn-in }}}$.

## IV. APPLICATIONS

In this section, we consider the High-Flow Safety System (HFSS) analyzed in [12] as a case study to demonstrate the application of the developed methods. The configuration of the HFSS is introduced first in Subsection IV-A. Then, in Subsection IV-B, pseudo-test data are generated based on statistical failure data and condition-monitoring data, respectively. The reliability of the safety barriers are updated in Subsection IV-C

and the results of the DRA for the HFSS are presented in Subsection IV-D.

## A. Description of the HFSS

The HFSS is a system installed on a hazardous material storage tank to defend against potential accidents that might be caused by a High-Flow (HF) event, i.e., the flow rate of the input pipeline becomes abnormally high for some reasons [12]. A defense-in-depth strategy is implemented by five safety barriers in the HFSS (Table I): when the HF event occurs, it is detected by the Basic Process Control (BPC) and the Bypass Line (BL) is activated by the BPC to prevent the excess flows from entering the tank. If the BPC does not work properly, the High Level Alarm (HLA) is triggered and an alarm is sent to the operator. The operator can close the Manual Valve (MV) to stop the excess flows. If, by any chance, all the above measures fail, excess flows generate high-pressure vapors in the tank. These vapors can be detected and the Pressure Safety Valve (PSV) will open automatically to reduce the pressure inside the tank.

An ET is constructed in [12] for the HFSS. Depending on the states of the safety barriers, 11 consequences, i.e., $C_{1}, C_{2}, \cdots, C_{11}$ can result from an initial HF. These consequences are grouped into three categories based on their severity: normal operation $\left(C_{A}\right)$, overflow of hazardous materials $\left(C_{B}\right)$ and excessively high pressure inside the tank $\left(C_{C}\right)$, where $C_{A}=C_{1} \cup C_{2} \cup C_{7}, C_{B}=C_{3} \cup C_{5} \cup C_{8} \cup C_{10}, C_{C}=$ $C_{4} \cup C_{6} \cup C_{9} \cup C_{11}$. The risk of incursions in the three different consequence categories, can, then, be evaluated as

$$
\left\{\begin{array}{l}
r_{C_{B}}=R_{1} R_{2}+R_{1}\left(1-R_{2}\right) R_{3} R_{4}+\left(1-R_{1}\right) R_{3} R_{4} \\
r_{C_{B}}=R_{1}\left(1-R_{2}\right) R_{3}\left(1-R_{4}\right) R_{5}+ \\
\left(1-R_{1}\right)\left(1-R_{3}\right) R_{5}+ \\
R_{1}\left(1-R_{2}\right)\left(1-R_{3}\right) R_{5}+ \\
\left(1-R_{1}\right) R_{3}\left(1-R_{4}\right) R_{5} \\
r_{C_{C}}=R_{1}\left(1-R_{2}\right) R_{3}\left(1-R_{4}\right)\left(1-R_{5}\right)+ \\
R_{1}\left(1-R_{2}\right)\left(1-R_{3}\right)\left(1-R_{5}\right)+ \\
\left(1-R_{1}\right)\left(1-R_{3}\right)\left(1-R_{5}\right)+ \\
\left(1-R_{1}\right) R_{3}\left(1-R_{4}\right)\left(1-R_{5}\right)
\end{array}\right.
$$

where $R_{1}, R_{2}, \cdots, R_{5}$ represent the reliability of the BPC, BL, HLA, MV and PSV, respectively, and $r_{C_{i}}$ is defined by (2).

## B. Statistical and condition-monitoring data

Statistical data of occurrence of consequences $C_{A}, C_{B}$ and $C_{C}, N_{k, j}, k=A, B, C$, are available from similar HFSS, as tabulated in Table II [12]. The data are collected annually for 10 years, i.e., $t=1,2, \cdots, 10$ (years). Pseudo-test data
$N_{S, i, j}, N_{F, i, j}, i=1,2, \cdots, 5, j=1,2, \cdots, 10$ are, then, generated using (10) and listed in Table III.

TABLE II
STATISTICAL DATA FROM SIMILAR SYSTEMS [12]


In this paper, we assume that the failure of the BPC and the HLA are primarily caused by the degradation of the Lithiumion battery, which provides the needed electrical power for their operation. Typically, degradation of Lithium-ion batteries is measured by its capacity $q(t)$, which is subject to conditionmonitoring. For illustrative purposes, we use the real data from CALCE (see [46] and [47] for details) as the conditionmonitoring data for the BPC and the HLA. The conditionmonitoring data, shown in Fig. 2, are collected in real time by measuring the current of the battery during each chargingdischarging cycle. The capacities, are, then, estimated using coulomb counting method [46, 47]. The failure threshold is defined as $y_{t h}=0.8[46,47]$. Note that to better illustrate the idea of dynamic risk assessment, we transformed the time scales of the condition-monitoring data.

As in [45], the state-space model in (23) is used to characterize the degradation behaviors of the two Lithium-ion batteries. The true degradation states (in terms of mean value and $95 \%$ credibility interval) are, then, estimated from the conditionmonitoring data using PF (Algorithm 1) and presented in Fig. 2. The number of particles simulated is $N_{P}=5000$. It should be noted that for both safety barriers, the state variable vector $\mathbf{x}$ in Algorithm 1 contains nine elements, i.e., $p_{1}, p_{2}, p_{3}, p_{4}, \sigma_{1}, \sigma_{2}, \sigma_{3}, \sigma_{4}, \sigma_{y}$, where the first four elements are updated recursively using (23) and the other elements are assumed to be constants (but unknown to us). The initial values for the state variables are drawn uniformly in the intervals of values given in Table IV.

$$
\left\{\begin{array}{l}
p_{1, t}=p_{1, t-1}+\mathcal{N}\left(0, \sigma_{1}^{2}\right) \\
p_{2, t}=p_{2, t-1}+\mathcal{N}\left(0, \sigma_{2}^{2}\right) \\
p_{3, t}=p_{3, t-1}+\mathcal{N}\left(0, \sigma_{3}^{2}\right) \\
p_{4, t}=p_{4, t-1}+\mathcal{N}\left(0, \sigma_{4}^{2}\right)
\end{array}\right.
$$

$y_{t}=p_{1, t} \exp \left(p_{2, t} \cdot t\right)+p_{3, t} \exp \left(p_{4, t} \cdot t\right)+\mathcal{N}\left(0, \sigma_{y}^{2}\right)$

TABLE I: SAFETY BARRIERS IN THE HFSS


TABLE III: PSEUDO-TEST DATA


![img-1.jpeg](img-1.jpeg)

(a) Condition-monitoring data for the BPC

![img-2.jpeg](img-2.jpeg)

(b) Condition-monitoring data for the HLA

Fig. 2. Condition-monitoring data from [46, 47]

The pseudo-test data $M_{S,i,j}$ and $M_{F,j,j}, i = 1, 2, j = 1, 2, \ldots, 10$, are, then, generated using Algorithm 2, and the results are also given in Table III.

### *C. Dynamic reliability analysis*

In this section, we demonstrate how to proceed with the dynamic reliability analysis method (Algorithm 3) of the BPC. The same procedure is applied to update the reliability of the HLA.

*1) Parameter setting and convergence analysis:* At each $t = t_j, j = 1, 2, \ldots, 10$ (years), the initial values $R^{(0)}, K^{(0)}, \pi^{(0)}$ are set as the expected values of the corresponding prior distributions:

$$ \begin{aligned} R^{(0)} &\leftarrow \frac{\alpha_1 + \sum_{\tau=1}^{j} N_{S,1,\tau}}{\alpha_1 + \sum_{\tau=1}^{j} N_{S,1,\tau} + \beta_1 + \sum_{\tau=1}^{j} N_{F,1,\tau}}, \ K^{(0)} &\leftarrow \frac{K_U + K_L}{2}, \ \pi^{(0)} &\leftarrow \frac{\alpha_1 + \sum_{\tau=1}^{j} N_{S,1,\tau}}{\alpha_1 + \sum_{\tau=1}^{j} N_{S,1,\tau} + \beta_1 + \sum_{\tau=1}^{j} N_{F,1,\tau}}.\end{aligned} $$

As in [12], we assume that $\alpha_1 = 2.1, \beta_1 = 0.25$. Also, we choose $K_L = 800$ and $K_U = 1000$. Posterior distributions of $R_{B,1,j}$ are generated by $N_l = 10^4$ MCMC samples, where the first $N_{burn-in} = 500$ samples are dropped for burn-in. The convergence of the MCMC is monitored using the trace plots. Normally, the MCMC algorithms are initialized with parameter values that happen to fall far from the center of the posterior distribution, updates obtained early in the chain exhibit a systematic drift toward the region of the parameter space where the posterior distribution is concentrated. Therefore, an increasing or decreasing trend in the parameter values in the trace plot indicates that the burn-in period is not over. When the trace plot stabilizes, the samples converge to the posterior distribution. Due to page limits, we only show the trace plots for $t = 6$ (years) in Fig. 3. It is seen that both $R_{B,1,j}$ and $K$ converge well to their posterior distributions after the "burn-in" period, since both the two trace plots are stable and do not exhibit significant increasing or decreasing tendency.

TABLE IV INITIAL INTERVALS FOR THE STATE VARIABLES


![img-3.jpeg](img-3.jpeg)

Fig. 3. Trace plots at $t=6$ (years) 2) Results and discussions: The posterior distribution for the reliability of the BPC at each $t=1,2, \cdots, 10$ (years) is given in Fig. 4. It can be seen from Fig. 4 that, in general, the reliability degrades as time evolves. In particular, the reliability degrades slowly for $t<7$ (years) and a dramatic decrease occurs for $7 \leq t \leq 8$ (years). The trend can be more clearly seen by computing the posterior mean of the reliability for each $t_{j}$, as shown in Fig. 5. To explain such phenomenon, first note that the posterior distribution is obtained by considering both condition-monitoring data from the target system and statistical failure data from a population of similar systems. For comparison, we compute also the posterior mean of the reliability using only statistical failure data (see [12] for details) and only the condition-monitoring data (see [45] for details), respectively. The results are also shown in Fig. 5. When $t<7$ (years), it can be seen that the posterior estimates from both statistical failure data and condition-monitoring data are quite stable. Therefore, the estimated posterior reliability is also stable in this region. On the other hand, the estimated posterior reliability remains at relatively high values when compared to that calculated using only statistical failure data. This is because, from Fig. 2, we can see that the conditionmonitoring data suggest that the BPC is highly reliable, since the safety margin (distance of the monitored variable from the failure threshold) is relatively large compared with the uncertainties in the estimation, which are represented by the $95 \%$ credibility interval in Fig. 2. When $7 \leq t \leq 8$ (years), the condition-monitoring data suggest that the degradation is approaching its threshold and the estimated posterior reliability drops coherently (see Fig. 2).

A further comparison is made in Fig. 6 by showing the posterior densities for $t=5,6 \cdots, 10$ (years). It can be seen from the comparison that the posterior reliability estimated by the developed method always lies between the estimates using statistical failure data and condition-monitoring data, only. This shows that the proposed method integrates information from the population of similar systems with the systemspecific information contained in the condition-monitoring data. Also, it can be seen from Fig. 6 that at different times, the two data sources have different importance to the estimated reliability. Before $t=7$ (year), the reliability estimated from condition-monitoring data is close to 1 , indicating that it is highly unlikely for the safety barrier to fail due to the degradation process. The reliability estimated by integrating the two data sources, however, is much lower and determined primarily by the statistical failure data. This is because, other than the degradation process, the safety barrier can also fail due to other failure causes, e.g., random shocks. Statistical failure data contain information from a population of similar systems, and, therefore, can capture well such "extra" failure causes. When $t>7$ (year), the contribution of conditionmonitoring data is higher than that of the statistical failure data. This is because, in this range, the safety barrier has already failed due to the degradation process, as suggested by the condition-monitoring data. $\square$

Fig. 4. Updated posterior distributions for the BPC reliability Figure 7 shows how the initial value of $K$ influences the

![img-4.jpeg](img-4.jpeg)

Fig. 5. Updated posterior mean of the BPC reliability
![img-5.jpeg](img-5.jpeg)

Fig. 6. Comparison of the posterior densities estimated using different data
trust on statistical failure data and condition-monitoring data. In Fig. 7, posterior distributions of the reliability are calculated at $t=7$ (years) using different initial distributions of $K$. The pseudo-test sample size from statistical failure data is $N_{P}=$ 5000. It can be seen from Fig. 7 that a larger value of $K$ tends to shift the posterior distribution towards the one yielded by statistical failure data. Therefore, $K$ can be viewed as the "prior sample size" of (4). In practice, the initial interval of $K$ is set based on the assumed trust on the condition-monitoring data when compared to the statistical failure data: if we trust more the condition-monitoring data than the statistical failure data, the values of $K_{L}$ and $K_{U}$ should be set to be less than the pseudo-test sample size of the condition-monitoring data $\left(N_{P}\right)$, and vice versa.

## D. Dynamic risk assessment (DRA)

DRA of the HFSS is made using Algorithm 4. Note that for safety barriers $2,4,5$, we do not have condition-monitoring data. By assuming the beta-binomial model as [12], their reliability can, then, be updated using (7), based on the pseudotest data $N_{S, i, j}$ and $N_{F, i, j}$ in Table III, $i=2,4,5$. Therefore,
![img-6.jpeg](img-6.jpeg)

Fig. 7. Posterior distributions under different initial distributions of $K$
the posterior samples for $R_{B, 2, j}, R_{B, 4, j}$ and $R_{B, 5, j}$ can be generated directly from the corresponding posterior distributions from (7). The posterior samples for $R_{B, 1, j}$ and $R_{B, 3, j}$, on the other hand, are generated following the dynamic reliability analysis procedures discussed in the previous subsection. The prior distributions for $R_{B, 1, j}, R_{B, 2, j}, \cdots, R_{B, 5, j}$ are assumed to take the same values as Table 2 of [12].

The posterior means of the risk indexes, $r_{C_{A}}, r_{C_{B}}$ and $r_{C_{C}}$ are, then, calculated based on (22) and the results are given in Fig. 8. It can be seen from Fig. 8 that, as expected, the conditional probability of $C_{A}$, which indicates the normal operation after the occurrence of the high flow event, decreases as time evolves. This is because, in general, the reliability of the five safety barriers are decreasing over time, as suggested by their posterior means in Fig. 9. The risk of accidents, therefore, becomes more severe as the safety barriers age. A closer look at Fig. 8 shows that the variation of the risk indexes can be divided into four ranges:

- A dramatic change of the risk indexes (decrease of $r_{C_{A}}$ and increase of $r_{C_{B}}$ and $r_{C_{C}}$ ) occurs in the first range, where $t \leq 5$ (years). As shown in Fig. 9, the dramatic change is caused primarily by the degradation of safety barriers 2 and 4 , which affect the risk indexes according to (22).
- When $5 \leq t \leq 7$ (years), the reliability of the safety barriers are relatively stable (see Fig. 9). Therefore, the risk indexes are also stable in this range.
- The risk indexes start changing again from $t=7$ (years) to $t=9$ (years). This is primarily caused by, as shown in Fig. 9, the dramatic decrease of the reliability of safety barriers 1 and 3 , which, as indicated in Fig. 2, is the result of the degradations reflected in the condition-monitoring data.
- Finally, in the last range when $9 \leq t \leq 10$ (years), both the reliability in Fig. 9 and the risk indexes in Fig. 8 become stable again.
Figure 8 provides a condition-informed online assessment of the risk indexes and can be used to support condition-

informed maintenance planning to reduce the risk of undesirable accident consequences along the life of the system. For example, maintenance interventions might be needed at $t=5$ (years), since the risk of accident becomes comparable to the conditional probability of normal operation. As our previous discussions show, maintenance on safety barriers 2 and 4 can help to reduce the risk, since the change in this range is primarily caused by these two safety barriers. Also, it can be seen from the DRA that maintenance actions are needed on safety barriers 1 and 3 , after $t=7$ (years), since based on the condition-monitoring data in Fig. 2, the degradation of safety barriers 1 and 3 approaches the threshold and become critical when $t \geq 7$ (years).
![img-7.jpeg](img-7.jpeg)

Fig. 8. Posterior means for the risk indexes

A comparison is made between the results obtained by the developed method and those of the DRA method that only considers statistical failure data [12]. By using the method in [12], the reliability of safety barriers 1 and 3 are updated using only the statistical failure data in Table II. It can be seen from Fig. 10 that before $t=7$ (years), the risk indexes estimated by both methods show the same trend (decrease of $r_{C_{A}}$ and increase of $r_{C_{B}}$ and $r_{C_{C}}$ ) but in this region, the risks estimated by the developed method is less severe than that estimated by the method in [12]. This is because, as shown in Fig. 2, the corresponding condition-monitoring data suggest that both the BPC and the HLA have high reliability in this region, since their safety margins are large compared to the uncertainties in their estimates. Having this information, we are more confident that the HFSS can reliably work to reduce the potential risk from an accident.
![img-8.jpeg](img-8.jpeg)

Fig. 9. The mean posterior reliability for the 5 safety barriers

Significant differences between the two methods are observed when $t \geq 7$ (years) in Fig. 10: the developed method suggests that $r_{C_{A}}$, the conditional probability of normal operation, begins to decrease from $t>7$ (years), while the method in [12] suggests that it remains relatively stable. Also, the credibility interval becomes significantly narrower than the one obtained from [12]. The same phenomenon is also observed in $r_{C_{B}}$ and $r_{C_{C}}$. This can be explained by the differences in the posterior reliability values of safety barriers 1 and 3 given by the two methods: as shown in Fig. 5, if we only use the statistical failure data, $R_{B, 1, t}$ is relatively stable over the entire range $[0,10]$ (years); if we introduce the condition-monitoring data in Fig. 2, $R_{B, 1, t}$ is stable from $t=1$ to $t=7$ (years), while it decreases dramatically when $t>7$ (years). The same phenomenon can be observed on safety barrier 3 , which results in the deviation of the two methods in Fig. 10.
![img-9.jpeg](img-9.jpeg)
a) Dynamic risk assessment of $r_{C_{A}}$
![img-10.jpeg](img-10.jpeg)
b) Dynamic risk assessment of $r_{C_{B}}$
c) Dynamic risk assessment of $r_{C_{C}}$

Fig. 10. Comparison to the method in [12]

## V. CONCLUSIONS

In this paper, we present a newly developed sequential Bayesian algorithm to support DRA using both statistical and condition-monitoring data. The former refer to the count data of accidents or near misses from similar systems and reflect statistical population characteristic while the latter come from realtime monitoring of the degradation process of the target system of interest and reflects the system-specific conditions. In the first stage of the algorithm, condition-monitoring data are treated by a PF and integrated with statistical failure data in a MCMC-based framework to update the reliability of the safety barriers in an ETs. The updated ET is, then, used to revise the estimated risk indexes in the second stage of the algorithm. A case study on a HFSS is conducted to demonstrate the developed methods and a comparison is made to an existing DRA method based only on statistical failure data. The results show that by introducing conditionmonitoring data, the developed method is able to capture the system-specific characteristics related to the degradation of the target system, and, therefore, provides a more informed description of the risk of the target system.

Note that in this paper, we have used the PF only to estimate the degradation state of the target system. On the other hand, PF can also be applied to predict the system degradation evolution in the future. Future work is, therefore, to extend the developed method from "risk updating" to "risk prognostics" by predicting the future evolution of the risk indexes using statistical and condition-monitoring data. Also, PF is a modelbased method and it requires the availability of physical models to describe the degradation process. Such premise is not always held in practice. In the future, data-driven methods, e.g., support vector machine, artificial neural network, etc., will also be considered for DRA. Besides, importance measures can be defined to quantify the relative importance of different data sources and to determine the required number of data in each source to support risk-informed support decision making.

## ACKNOWLEDGMENT

The authors would like to thank Dr. Jie Liu and Miss Jinduo Xing from CentraleSupélec, Université Paris-Saclay for their help in this work. Also, the authors would like to express their deepest gratitude to the three anonymous reviewers, as well as the Associate Editor, Prof. Franz Wotawa, for their insightful comments and suggestions that greatly help us to improve the quality of this paper.

## ACRONYMS

ASP Accident Sequence Precursor
BL Bypass Line
BN Bayesian Network
BPC Basic Process Control
BT Bow-Tie
CBFTA Condition-based Fault Tree Analysis
DBN Dynamic Bayesian Network
DRA Dynamic Risk Assessment
ET Event Tree
HFSS High-Flow Safety System
HLA High Level Alarm
MCMC Markov Chain Monte Carlo
MH Metropolis-Hasting
MV Manual Valve
PCA Principal Component Analysis
PF Particle Filtering
PSV Pressure Safety Valve
QRA Quantitative Risk Assessment
RUL Remaining Useful Life

## NOTATIONS

$r_{C_{i}} \quad$ Conditional occurrence probability of the consequence given that IE has occurred
$N_{k, j} \quad$ Number of the $k$ th consequences that occur in the interval $\left(t_{j-1}, t_{j}\right]$
$y_{i, j} \quad$ Condition-monitoring data on the $i$ th safety barrier at $t=t_{j}$
$R_{B, i, j} \quad$ Reliability of the $i$ th safety barrier at $t=t_{j}$
$\pi_{i, j} \quad$ Prior mean of $R_{B, i, j}$
$K \quad$ Prior sample size of $R_{B, i, j}$
$\alpha_{i}, \beta_{i} \quad$ Parameters of the prior distribution of $\pi_{i, 1}$
$N_{S, i, j} \quad$ Number of successes in the pseudo test data generated from statistical failure data
$N_{F, i, j} \quad$ Number of failures in the pseudo test data generated from statistical failure data
$M_{S, i, j} \quad$ Number of successes in the pseudo test data generated from condition-monitoring data
$M_{F, i, j} \quad$ Number of failures in the pseudo test data generated from condition-monitoring data
$B_{i} \quad$ The $i$ th safety barrier
$N_{P} \quad$ Sample size of PF