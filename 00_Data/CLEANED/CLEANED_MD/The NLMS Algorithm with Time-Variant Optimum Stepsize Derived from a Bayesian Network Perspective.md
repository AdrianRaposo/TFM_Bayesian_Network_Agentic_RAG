# The NLMS algorithm with time-variant optimum stepsize derived from a Bayesian network perspective 

Christian Huemmer, Student Member, IEEE, Roland Maas, Walter Kellermann, Fellow, IEEE


#### Abstract

In this article, we derive a new stepsize adaptation for the normalized least mean square algorithm (NLMS) by describing the task of linear acoustic echo cancellation from a Bayesian network perspective. Similar to the well-known Kalman filter equations, we model the acoustic wave propagation from the loudspeaker to the microphone by a latent state vector and define a linear observation equation (to model the relation between the state vector and the observation) as well as a linear process equation (to model the temporal progress of the state vector). Based on additional assumptions on the statistics of the random variables in observation and process equation, we apply the expectation-maximization (EM) algorithm to derive an NLMS-like filter adaptation. By exploiting the conditional independence rules for Bayesian networks, we reveal that the resulting EM-NLMS algorithm has a stepsize update equivalent to the optimal-stepsize calculation proposed by Yamamoto and Kitayama in 1982, which has been adopted in many textbooks. As main difference, the instantaneous stepsize value is estimated in the M step of the EM algorithm (instead of being approximated by artificially extending the acoustic echo path). The EM-NLMS algorithm is experimentally verified for synthesized scenarios with both, white noise and male speech as input signal.


Index Terms-Adaptive stepsize, NLMS, Bayesian network, machine learning, EM algorithm

## I. INTRODUCTION

MACHINE learning techniques have been widely applied to signal processing tasks since decades [1], [2]. For example, directed graphical models, termed Bayesian networks, have shown to provide a powerful framework for modeling causal probabilistic relationships between random variables [3]-[7]. In previous work, the update equations of the Kalman filter and the normalized least mean square (NLMS) algorithm have already been derived from a Bayesian network perspective based on a linear relation between the latent room impulse response (RIR) vector and the observation [8], [9]. The NLMS algorithm is one of the most-widely used adaptive algorithms in speech signal processing and a variety of stepsize adaptation schemes has been proposed to improve its system identification performance [10]-[21]. In this article, we derive a novel NLMS-like filter adaptation (termed EMNLMS algorithm) by applying the expectation-maximization (EM) algorithm to a probabilistic model for linear system identification. Based on the conditional independence rules for Bayesian networks, it is shown that the normalized stepsize of the EM-NLMS algorithm is equivalent to the one proposed in [10], which is now commonly accepted as optimum NLMS stepsize rule, see e.g. [22]. As the main difference relative to [10], the normalized stepsize is here estimated as part of the EM algorithm instead of being approximated by artificially extending the acoustic echo path. For a valid comparison, we review the algorithm of [10] for the linear acoustic echo
cancellation (AEC) scenario shown in Fig. 1. The acoustic path between loudspeaker and microphone at time $n$ is modeled by the linear finite impulse response (FIR) filter

$$
\mathbf{h}_{n}=\left[h_{0, n}, h_{1, n}, \ldots, h_{M-1, n}\right]^{T}
$$

with time-variant coefficients $h_{\kappa, n}$, where $\kappa=0, \ldots, M-1$. The observation equation models the microphone sample $d_{n}$ :

$$
d_{n}=\mathbf{x}_{n}^{T} \mathbf{h}_{n}+v_{n}
$$

with the additive variable $v_{n}$ modeling near-end interferences and the observed input signal vector $\mathbf{x}_{n}=\left[x_{n}, x_{n-1}, \ldots, x_{n-M+1}\right]^{T}$ capturing the time-domain samples $x_{n}$. The iterative estimation of the RIR vector by the adaptive FIR filter $\hat{\mathbf{h}}_{n}$ is realized by the update rule

$$
\hat{\mathbf{h}}_{n}=\hat{\mathbf{h}}_{n-1}+\lambda_{n} \mathbf{x}_{n} e_{n}
$$

with the stepsize $\lambda_{n}$ and the error signal

$$
e_{n}=d_{n}-\mathbf{x}_{n}^{T} \hat{\mathbf{h}}_{n-1}
$$

relating the observation $d_{n}$ and its estimate $\hat{d}_{n}=\mathbf{x}_{n}^{T} \hat{\mathbf{h}}_{n-1}$. In [10], the optimal choice of $\lambda_{n}$ has been approximated as:

$$
\lambda_{n} \approx \frac{1}{M} \frac{\mathcal{E}\left\{\left\|\mathbf{h}_{n}-\hat{\mathbf{h}}_{n-1}\right\|_{2}^{2}\right\}}{\mathcal{E}\left\{e_{n}^{2}\right\}}
$$

where $\|\cdot\|_{2}$ denotes the Euclidean norm and $\mathcal{E}\{\cdot\}$ the expectation operator. As the true echo path $\mathbf{h}_{n}$ is unobservable, so that the numerator in (5) cannot be computed, $\lambda_{n}$ is further approximated by introducing a delay of $N_{T}$ coefficients to the echo path $\mathbf{h}_{n}$. Moreover, a recursive approximation of the denominator in (5) is applied using the forgetting factor $\eta$ [22], [23]. The resulting stepsize approximation

$$
\lambda_{n} \approx \frac{1}{N_{T}} \frac{\sum_{n=0}^{N_{T}-1} \hat{h}_{k, n-1}^{2}}{\left(1-\eta\right) e_{n}^{2}+\eta \mathcal{E}\left\{e_{n-1}^{2}\right\}}
$$

leads to oscillations which have to be addressed by limiting the absolute value of $\lambda_{n}$ [24]. In this article, we derive the EM-NLMS algorithm which applies the filter update of (3) using the stepsize in (5), where $\lambda_{n}$ is estimated in the M Step of the EM algorithm instead of being approximated by using (6).
![img-0.jpeg](img-0.jpeg)

Fig. 1. System model for linear AEC with RIR vector $\mathbf{h}_{n}$

TABLE I: RELATION BETWEEN THE NLMS ALGORITHM FOLLOWING [10] AND THE PROPOSED EM-NLMS ALGORITHM


This article is structured as follows: In Section II, we propose a probabilistic model for the linear AEC scenario of Fig. 1 and derive the EM-NLMS algorithm, which is revealed in Section III to be similar to the NLMS algorithm proposed in [10]. As main difference (cf. Table I), the stepsize is estimated in the M Step of the EM algorithm instead of being approximated by artificially extending the acoustic echo path. In Section IV, the EM-NLMS algorithm is experimentally verified for synthesized scenarios with both, white noise and male speech as input signal. Finally, conclusions are drawn in Section V.

## II. THE EM-NLMS ALGORITHM FOR LINEAR AEC

Throughout this article, the Gaussian probability density function (PDF) of a real-valued length- $M$ vector $\mathbf{z}_{n}$ with mean vector $\boldsymbol{\mu}_{\mathbf{z}, n}$ and covariance matrix $\mathbf{C}_{\mathbf{z}, n}$ is denoted as

$$
\begin{aligned}
& \mathbf{z}_{n} \sim \mathcal{N}\left\{\mathbf{z}_{n} \mid \boldsymbol{\mu}_{\mathbf{z}, n}, \mathbf{C}_{\mathbf{z}, n}\right\} \\
= & \frac{\left|\mathbf{C}_{\mathbf{z}, n}\right|^{-1 / 2}}{(2 \pi)^{M / 2}} \exp \left\{-\frac{\left(\mathbf{z}_{n}-\boldsymbol{\mu}_{\mathbf{z}, n}\right)^{T} \mathbf{C}_{\mathbf{z}, n}^{-1}\left(\mathbf{z}_{n}-\boldsymbol{\mu}_{\mathbf{z}, n}\right)}{2}\right\}
\end{aligned}
$$

where $|\cdot|$ represents the determinant of a matrix. Furthermore, $\mathbf{C}_{\mathbf{z}, n}=C_{\mathbf{z}, n} \mathbf{I}$ (with identity matrix $\mathbf{I}$ ) implies the elements of $\mathbf{z}_{n}$ to be mutually statistically independent and of equal variance $C_{\mathbf{z}, n}$.

## A. Probabilistic AEC model

To describe the linear AEC scenario of Fig. 1 from a Bayesian network perspective, we model the acoustic echo path as a latent state vector $\mathbf{h}_{n}$ identically defined as in (1) and capture uncertainties (e.g. due to the limitation to a linear system with a finite set of coefficients) by the additive uncertainty $\mathbf{w}_{n}$. Consequently, the linear process equation and the linear observation equation,

$$
\mathbf{h}_{n}=\mathbf{h}_{n-1}+\mathbf{w}_{n} \quad \text { and } \quad d_{n}=\mathbf{x}_{n}^{T} \mathbf{h}_{n}+v_{n}
$$

can be jointly represented by the graphical model shown in Fig. 2. The directed links express statistical dependencies between the nodes and random variables, such as $v_{n}$, are marked as circles. We make the following assumptions on the PDFs of the random variables in Fig. 2:

- The uncertainty $\mathbf{w}_{n}$ is normally distributed with mean vector $\mathbf{0}$ (of zero-valued entries) and variance $C_{\mathbf{w}, n}$ :

$$
\mathbf{w}_{n} \sim \mathcal{N}\left\{\mathbf{w}_{n} \mid \mathbf{0}, \mathbf{C}_{\mathbf{w}, n}\right\}, \quad \mathbf{C}_{\mathbf{w}, n}=C_{\mathbf{w}, n} \mathbf{I}
$$

- The microphone signal uncertainty $v_{n}$ is assumed to be normally distributed with variance $C_{v, n}$ and zero mean:

$$
v_{n} \sim \mathcal{N}\left\{v_{n} \mid 0, C_{v, n}\right\}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. Bayesian network for linear AEC with latent state vector $\mathbf{h}_{n}$

- The posterior distribution $p\left(\mathbf{h}_{n} \mid d_{1: n}\right)$ is defined with mean vector $\boldsymbol{\mu}_{\mathbf{h}, n}$, variance $C_{\mathbf{h}, n}$ and $d_{1: n}=d_{1}, \ldots, d_{n}$ :

$$
p\left(\mathbf{h}_{n} \mid d_{1: n}\right)=\mathcal{N}\left\{\mathbf{h}_{n} \mid \boldsymbol{\mu}_{\mathbf{h}, n}, \mathbf{C}_{\mathbf{h}, n}\right\}, \quad \mathbf{C}_{\mathbf{h}, n}=C_{\mathbf{h}, n} \mathbf{I}
$$

Based on this probabilistic AEC model, we apply the EM algorithm consisting of two parts: In the E Step, the filter update is derived based on minimum mean square error (MMSE) estimation (Subsection II-B). In the M step, we predict the model parameters $C_{v, n+1}$ and $C_{\mathbf{w}, n+1}$ to estimate the adaptive stepsize value $\lambda_{n+1}$ (Subsection II-C).

## B. E step: Inference of the state vector

The MMSE estimation of the state vector identifies the mean vector of the posterior distribution as estimate $\tilde{\mathbf{h}}_{n}$ :

$$
\tilde{\mathbf{h}}_{n}=\underset{\tilde{\mathbf{h}}_{n}}{\operatorname{argmin}} \mathcal{E}\left\{\left\|\tilde{\mathbf{h}}_{n}-\mathbf{h}_{n}\right\|_{2}^{2}\right\}=\mathcal{E}\left\{\mathbf{h}_{n} \mid d_{1: n}\right\}=\boldsymbol{\mu}_{\mathbf{h}, n}
$$

Due to the linear relations between the variables in (2) and (8), and under the restrictions to a linear estimator of $\tilde{\mathbf{h}}_{n}$ and normally distributed random variables, the MMSE estimation is analytically tractable [9] . Exploiting the product rules for linear Gaussian models and conditional independence of the Bayesian network in Fig 2, the filter update can be derived as a special case of the Kalman filter equations [9, p. 639]:

$$
\tilde{\mathbf{h}}_{n}=\tilde{\mathbf{h}}_{n-1}+\boldsymbol{\Lambda}_{n} \mathbf{x}_{n} e_{n}
$$

with the stepsize matrix

$$
\boldsymbol{\Lambda}_{n}=\frac{\mathbf{C}_{\mathbf{h}, n-1}+\mathbf{C}_{\mathbf{w}, n}}{\mathbf{x}_{n}^{T}\left(\mathbf{C}_{\mathbf{h}, n-1}+\mathbf{C}_{\mathbf{w}, n}\right) \mathbf{x}_{n}+C_{v, n}}
$$

and the update of the covariance matrix given as

$$
\mathbf{C}_{\mathbf{h}, n}=\left(\mathbf{I}-\boldsymbol{\Lambda}_{n} \mathbf{x}_{n} \mathbf{x}_{n}^{T}\right)\left(\mathbf{C}_{\mathbf{h}, n-1}+\mathbf{C}_{\mathbf{w}, n}\right)
$$

By inserting (9) and (11), we can rewrite the filter update of (13) to the filter update defined in (3) with the scalar stepsize

$$
\lambda_{n}=\frac{C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}}{\mathbf{x}_{n}^{T} \mathbf{x}_{n}\left(C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}\right)+C_{v, n}}
$$

Finally, the update of $C_{\mathbf{h}, n}$ is approximated following (11) as $C_{\mathbf{h}, n} \stackrel{(11)}{=} \frac{\operatorname{diag}\left\{\mathbf{C}_{\mathbf{h}, n}\right\}}{M} \stackrel{(15)}{=}\left(1-\lambda_{n} \frac{\mathbf{x}_{n}^{T} \mathbf{x}_{n}}{M}\right)\left(C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}\right)$,
where diag $\{\cdot\}$ adds up the diagonal elements of a matrix.
Before showing the equality of the stepsize updates in (16) and (5) in Section III, we propose a new alternative to estimate $\lambda_{n}$ in (16) by deriving the updates of the model parameters $C_{\mathbf{w}, n}$ and $C_{v, n}$ in the following section.

## C. $M$ step: Online learning of the model parameters

In the M step, we predict the model parameters for the following time instant. Although the maximum likelihood estimation is analytically tractable, we apply the EM algorithm to derive an online estimator: In order to update $\theta_{n}=\left\{C_{v, n}, C_{\mathbf{w}, n}\right\}$ to the new parameters $\theta_{n}^{\text {new }}=\left\{C_{v, n}^{\text {new }}, C_{\mathbf{w}, n}^{\text {new }}\right\}$, the lower bound

$$
\mathcal{E}_{\mathbf{h}_{1: n} \mid \theta_{1: n}}\left\{\ln \left(p\left(d_{1: n}, \mathbf{h}_{1: n} \mid \theta_{1: n}\right)\right)\right\} \leq \ln p\left(d_{1: n} \mid \theta_{1: n}\right)
$$

is maximized, where $\theta_{1: n}=\left\{C_{v, 1: n}, C_{\mathbf{w}, 1: n}\right\}$. For this, the PDF $p\left(d_{1: n}, \mathbf{h}_{1: n} \mid \theta_{1: n}\right)$ is determined by applying the decomposition rules for Bayesian networks [9]:

$$
\begin{aligned}
& p\left(d_{1: n}, \mathbf{h}_{1: n} \mid \theta_{1: n}\right)=p\left(\mathbf{h}_{n} \mid \mathbf{h}_{n-1}, C_{\mathbf{w}, n} \mathbf{I}\right) p\left(d_{n} \mid \mathbf{h}_{n}, C_{v, n}\right) \\
& \cdot \prod_{m=1}^{n-1} p\left(\mathbf{h}_{m} \mid \mathbf{h}_{m-1}, C_{\mathbf{w}, m} \mathbf{I}\right) p\left(d_{m} \mid \mathbf{h}_{m}, C_{v, m}\right)
\end{aligned}
$$

Next, we take the natural logarithm $\ln (\cdot)$ of $p\left(d_{1: n}, \mathbf{h}_{1: n} \mid \theta_{1: n}\right)$, replace $\theta_{n}$ by $\theta_{n}^{\text {new }}$ and maximize the right-hand side of (18) with respect to $\theta_{n}^{\text {new }}$ :

$$
\begin{aligned}
\theta_{n}^{\text {new }} & =\underset{C_{\mathbf{w}, n}^{\text {new }}}{\operatorname{argmax}} \mathcal{E}_{\mathbf{h}_{1: n} \mid \theta_{n}}\left\{\ln \left(p\left(\mathbf{h}_{n} \mid \mathbf{h}_{n-1}, C_{\mathbf{w}, n}^{\text {new }} \mathbf{I}\right)\right)\right\} \\
& +\underset{C_{v, n}^{\text {new }}}{\operatorname{argmax}} \mathcal{E}_{\mathbf{h}_{1: n} \mid \theta_{n}}\left\{\ln \left(p\left(d_{n} \mid \mathbf{h}_{n}, C_{v, n}^{\text {new }}\right)\right)\right\}
\end{aligned}
$$

where we apply two separate maximizations starting with the estimation of $C_{v, n}^{\text {new }}$ by inserting

$$
\ln \left(p\left(d_{n} \mid \mathbf{h}_{n}, C_{v, n}^{\text {new }}\right)\right) \stackrel{(8)}{=}-\frac{\ln \left(2 \pi C_{v, n}^{\text {new }}\right)}{2}-\frac{\left(d_{n}-\mathbf{x}_{n}^{T} \mathbf{h}_{n}\right)^{2}}{2 C_{v, n}^{\text {new }}}
$$

into (20). This leads to the instantaneous estimate:

$$
\begin{aligned}
C_{v, n}^{\text {new }} & =\mathcal{E}_{\mathbf{h}_{1: n} \mid \theta_{n}}\left\{\left(d_{n}-\mathbf{x}_{n}^{T} \mathbf{h}_{n}\right)^{2}\right\} \\
& =d_{n}+\mathbf{x}_{n}^{T}\left(C_{\mathbf{h}, n} \mathbf{I}+\tilde{\mathbf{h}}_{n} \tilde{\mathbf{h}}_{n}^{T}\right) \mathbf{x}_{n}-2 \mathbf{x}_{n}^{T} \tilde{\mathbf{h}}_{n} \\
& =\left(d_{n}-\mathbf{x}_{n}^{T} \tilde{\mathbf{h}}_{n}\right)^{2}+\mathbf{x}_{n}^{T} \mathbf{x}_{n} C_{\mathbf{h}, n}
\end{aligned}
$$

The variance (of the microphone signal uncertainty) $C_{v, n}^{\text {new }}$ in (24) consists of two components, which can be interpreted as follows [25]: The first term in (24) is given as the squared error signal after filter adaptation and is influenced by near-end interferences like background noise. The second term in (24) depends on the signal energy $\mathbf{x}_{n}^{T} \mathbf{x}_{n}$ and the variance $C_{\mathbf{h}, n}$ which implies that it considers uncertainties in the linear echo path model. Similar to the derivation for $C_{v, n}^{\text {new }}$, we insert

$$
\begin{aligned}
& \ln \left(p\left(\mathbf{h}_{n} \mid \mathbf{h}_{n-1}, C_{\mathbf{w}, n} \mathbf{I}\right)\right) \\
& \stackrel{(8)}{=}-\frac{M \ln \left(2 \pi C_{\mathbf{w}, n}^{\text {new }}\right)}{2}-\frac{\left(\mathbf{h}_{n}-\mathbf{h}_{n-1}\right)^{T}\left(\mathbf{h}_{n}-\mathbf{h}_{n-1}\right)}{2 C_{\mathbf{w}, n}^{\text {new }}}
\end{aligned}
$$

into (20), to derive the instantaneous estimate of $C_{\mathbf{w}, n}^{\text {new }}$ :

$$
\begin{aligned}
C_{\mathbf{w}, n}^{\text {new }} & =\frac{1}{M} \mathcal{E}_{\mathbf{h}_{1: n} \mid \theta_{n}}\left\{\left(\mathbf{h}_{n}-\mathbf{h}_{n-1}\right)^{T}\left(\mathbf{h}_{n}-\mathbf{h}_{n-1}\right)\right\} \\
& \stackrel{(11)}{=} C_{\mathbf{h}, n}-C_{\mathbf{h}, n-1}+\frac{1}{M}\left(\tilde{\mathbf{h}}_{n}^{T} \tilde{\mathbf{h}}_{n}-\tilde{\mathbf{h}}_{n-1}^{T} \tilde{\mathbf{h}}_{n-1}\right)
\end{aligned}
$$

where we employed the statistical independence between $\mathbf{w}_{n}$ and $\mathbf{h}_{n-1}$. Equation (27) implies the estimation of $C_{\mathbf{w}, n}^{\text {new }}$ as difference of the filter tap autocorrelations between the time instants $n$ and $n-1$. Finally, the updated values in $\theta_{n}^{\text {new }}$ are used as initialization for the following time step, so that

$$
\theta_{n+1}:=\theta_{n}^{\text {new }} \rightarrow C_{\mathbf{w}, n+1}:=C_{\mathbf{w}, n}^{\text {new }}, C_{v, n+1}:=C_{v, n}^{\text {new }}
$$

## III. COMPARISON BETWEEN THE EM-NLMS ALGORITHM AND THE NLMS ALGORITHM PROPOSED IN [10]

In this part, we compare the proposed EM-NLMS algorithm to the NLMS algorithm reviewed in Section I and show the equality between the adaptive stepsizes in (5) and (16). We reformulate the stepsize update in (16) by applying the conditional independence rules for Bayesian networks [9]: First, we exploit the equalities

$$
\begin{aligned}
& \mathbf{C}_{\mathbf{h}, n} \stackrel{(11)}{=} C_{\mathbf{h}, n} \mathbf{I} \stackrel{(12)}{=} \mathcal{E}\left\{\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n}\right)\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n}\right)^{T}\right\} \\
& \mathbf{C}_{\mathbf{w}, n} \stackrel{(9)}{=} C_{\mathbf{w}, n} \mathbf{I}=\mathcal{E}\left\{\mathbf{w}_{n} \mathbf{w}_{n}^{T}\right\}
\end{aligned}
$$

which lead to the following relations:

$$
\begin{aligned}
& C_{\mathbf{h}, n}=\frac{\mathcal{E}\left\{\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n}\right)^{T}\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n}\right)\right\}}{M}=\frac{\mathcal{E}\left\{\left\|\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n}\right\|_{2}^{2}\right\}}{M} \\
& C_{\mathbf{w}, n}=\frac{\mathcal{E}\left\{\mathbf{w}_{n}^{T} \mathbf{w}_{n}\right\}}{M}=\frac{\mathcal{E}\left\{\left\|\mathbf{w}_{n}\right\|_{2}^{2}\right\}}{M}
\end{aligned}
$$

Second, it can be seen in Fig. 2 that the state vector $\mathbf{h}_{n-1}$ and the uncertainty $\mathbf{w}_{n}$ are statistically independent as they share a head-to-head relationship with respect to the latent vector $\mathbf{h}_{n}$. As a consequence, the numerator in (16) can be rewritten as

$$
\begin{aligned}
C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n} \stackrel{(30)}{=} & \frac{\mathcal{E}\left\{\left\|\mathbf{h}_{n-1}-\tilde{\mathbf{h}}_{n-1}\right\|_{2}^{2}\right\}}{M}+\frac{\mathcal{E}\left\{\left\|\mathbf{w}_{n}\right\|_{2}^{2}\right\}}{M} \\
& \stackrel{(8)}{=} \frac{\mathcal{E}\left\{\left\|\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right\|_{2}^{2}\right\}}{M}
\end{aligned}
$$

Finally, we consider the mean of the squared error signal

$$
\mathcal{E}\left\{e_{n}^{2}\right\} \stackrel{(2),(4)}{=} \mathcal{E}\left\{\left(\mathbf{x}_{n}^{T}\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right)+v_{n}\right)^{2}\right\}
$$

which is not conditioned on the microphone signal $d_{n}$. By applying the conditional independence rules to the Bayesian network in Fig. 2, the head-to-head relationship with respect to $d_{n}$ implies $v_{n}$ to be statistically independent from $\mathbf{h}_{n-1}$ and $\mathbf{w}_{n}$, respectively. Consequently, we can rewrite (32) as:

$$
\begin{aligned}
\mathcal{E}\left\{e_{n}^{2}\right\} \stackrel{(10)}{=} & \mathbf{x}_{n}^{T} \mathcal{E}\left\{\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right)\left(\mathbf{h}_{n}-\tilde{\mathbf{h}}_{n-1}\right)^{T}\right\} \mathbf{x}_{n}+C_{v, n} \\
\stackrel{(8)}{=} & \mathbf{x}_{n}^{T} \mathbf{x}_{n}\left(C_{\mathbf{h}, n-1}+C_{\mathbf{w}, n}\right)+C_{v, n}
\end{aligned}
$$

The insertion of (31) and (33) into the stepsize defined in (16) yields the identical expression for $\lambda_{n}$ as in (5). The main difference of the proposed EM-NLMS algorithm is that the model parameters $C_{\mathbf{h}, n}$ and $C_{\mathbf{w}, n}$ (and consequently the normalized stepsize $\lambda_{n}$ ) are estimated in the M step of the EM algorithm instead of being approximated using (6).

## IV. EXPERIMENTAL RESULTS

This section focuses on the experimental verification of the EM-NLMS algorithm ("EM-NLMS") in comparison to the adaptive stepsize-NLMS algorithm described in Section I ("Adapt. NLMS") and the conventional NLMS algorithm ("Conv. NLMS") with a fixed stepsize. An overview of the algorithms including the individually tuned model parameters is shown in Table II. Note the regularization of all three stepsize updates by the additive constant $\epsilon=0.01$ to avoid a division by zero. For the evaluation, we synthesize the microphone signal by convolution of the loudspeaker signal

with an RIR vector measured in a room with $T_{60}=100 \mathrm{~ms}$ (filter length $M=512$ at a sampling rate of 16 kHz ). This is realized for both white noise and a male speech signal as loudspeaker signals. Furthermore, background noise is simulated by adding Gaussian white noise at a global signal-to-noise ratio of 20 dB . The comparison is realized in terms of the stepsize $\alpha_{n}$ and the system distance $\Delta h_{n}$ as a measure for the system identification performance:

$$
\Delta h_{n}=10 \log _{10} \frac{\left\|\hat{\mathbf{h}}_{n}-\mathbf{h}_{n}\right\|_{2}^{2}}{\left\|\mathbf{h}_{n}\right\|_{2}^{2}} \mathrm{~dB}, \quad \alpha_{n}=\lambda_{n}\left(\mathbf{x}_{n}^{T} \mathbf{x}_{n}\right)
$$

The results for white noise as input signal are illustrated in Fig 3. Note that in Fig. 3a) the EM-NLMS shows the best system identification compared to the Adapt. NLMS and the Conv. NLMS. As depicted in Fig. 3b), the stepsize $\alpha_{n}$ of the EM-NLMS and the Adapt. NLMS decreases from a value of 0.5 with the stepsize of the EM-NLMS decaying more slowly. For male speech as input signal, we improve the convergence of the Conv. NLMS by setting a fixed threshold to stop adaptation $\left(\alpha_{n}=0\right)$ in speech pauses. Furthermore, the absolute value of $\lambda_{n}$ for the Adapt. NLMS is limited to 0.5 (for a heuristic justification see [24]). As illustrated in Fig. 4a), the EM-NLMS shows again the best system identification compared to the Adapt. NLMS and the Conv. NLMS. By focusing on a small time frame, we can see in Fig. 4b) that the stepsize $\alpha_{n}$ of the EM-NLMS algorithm is not restricted to the values of 0 and 0.5 (as Conv. NLMS) and not affected by oscillations (as Adapt. NLMS).
Note that the only relevant increase in computational complexity of the EM-NLMS relative to the Conv. NLMS is caused by the scalar product $\hat{\mathbf{h}}_{n}^{T} \hat{\mathbf{h}}_{n}$ for the calculation of $C_{\mathbf{w}, n}$ (cf. Table II), which seems relatively small compared to other sophisticated stepsize adaptation algorithms.

TABLE II
REALIZATIONS OF THE EM-NLMS ALGORITHM ("EM-NLMS"), THE NLMS ALGORITHM DUE TO [10] ("ADAPT. NLMS") AND THE CONVENTIONAL NLMS ALGORITHM ("CONV. NLMS")


## V. CONCLUSION

In this article, we derive the EM-NLMS algorithm from a Bayesian network perspective and show the equality with respect to the NLMS algorithm initially proposed in [10]. As main difference, the stepsize is estimated in the M Step of the EM algorithm instead of being approximated by artificially extending the acoustic echo path. For the derivation of the EM-NLMS algorithm, which is experimentally shown to be promising for the task of linear AEC, we define a probabilistic model for linear system identification and exploit the product and conditional independence rules of Bayesian networks. All together this article exemplifies the benefit of applying machine learning techniques to classical signal processing tasks.
a)
![img-2.jpeg](img-2.jpeg)
b)
![img-3.jpeg](img-3.jpeg)

Fig. 4. Comparison of the EM-NLMS algorithm ("EM-NLMS"), the NLMS algorithm due to [10] ("Adapt. NLMS") and the conventional NLMS algorithm ("Conv. NLMS") in terms of the system distance $\Delta h_{n}$ and the stepsize $\alpha_{n}$ (short time frame for visualization purposes) for male speech as input signal (see the microphone signal $d_{n}$ in Fig. 4c)).
