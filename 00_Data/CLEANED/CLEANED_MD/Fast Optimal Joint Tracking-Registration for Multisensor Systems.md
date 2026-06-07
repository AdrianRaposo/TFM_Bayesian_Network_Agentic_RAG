# Fast Optimal Joint Tracking-Registration for Multi-Sensor Systems 

Shuqing Zeng, Member


#### Abstract

Sensor fusion of multiple sources plays an important role in vehicular systems to achieve refined target position and velocity estimates. In this article, we address the general registration problem, which is a key module for a fusion system to accurately correct systematic errors of sensors. A fast maximum a posteriori (FMAP) algorithm for joint registrationtracking (JRT) is presented. The algorithm uses a recursive two-step optimization that involves orthogonal factorization to ensure numerically stability. Statistical efficiency analysis based on Cramèr-Rao lower bound theory is presented to show asymptotical optimality of FMAP. Also, Givens rotation is used to derive a fast implementation with complexity $O(n)$ with $n$ the number of tracked targets. Simulations and experiments are presented to demonstrate the promise and effectiveness of FMAP.


## I. INTRODUCTION

Recently, active safety driver assistance (ASDA) systems such as adaptive cruise control (ACC) and pre-crash sensing (PCS) systems [5] have drawn considerable attention in intelligent transportation systems (ITS) community. To obtain the necessary information of surround vehicles for ASDA systems, multiple sensors including active radars, lidars, and passive cameras are mounted on vehicles. Those sensor systems in a vehicular system are typically calibrated manually. However, sensor orientation and signal output may drift during the life of the sensor, such that the orientation of the sensor relative to the vehicular frame is changed. When the sensor orientation drifts, measurements become skewed relative to the vehicle [18]. When there are multiple sensors, this concern is further complicated. It is thus desirable to have sensor systems that automatically align sensor output to the vehicular frame [1], [2].

Two categories of approaches have been attempted to address the registration problem. The first category decouples tracking and registration into separate problems. In [7], [12], [15], [24], [27], filters are designed to estimate the sensor biases by minimizing the discrepancy between measurements and associated fused target estimates, from a separated tracking module. However, these methods are not optimal in term of Cramer-Rao bounds [25]. In the second category, the approaches jointly solve for target tracking and sensor registration. For example, [19]-[22], [26] have applied extended Kalman filtering (EKF) to an

Manuscript was drafted in May 28, 2010, and published in May 5, 2011.
augmented state vector combining the target variables and sensor system errors in aerospace applications. In [6] a fixed-lag smoothing framework is employed to estimate the augmented state vector to deal with communication jitters in networked sensors. Unscented Kalman filter (UKF) in [14] and expectation-maximization based interacting multiple model (IMM) in [11] have been applied to the augmented state vector in vehicle-to-vehicle cooperative driving systems. In [23] the particle filter outperforms EKF at the cost of more demanding computations in state estimation for industrial systems. However, there are a few difficulties with these approaches. Since the registration parameters are constant, the error model of state-space is degenerated. This not only makes the estimation problem larger-leading to higher computational cost (complexity $O\left(n^{3}\right)$ with $n$ denoting number of targets), but also results degenerated covariance matrices for the process noise vectors due to numerical instability inherent to EKF, UKF, and the variants.

In this article, we propose a fast maximum a posteriori (FMAP) registration algorithm to tackle the problems. We combine all the measurement equations and process equations to form a linearized state-space model. The registration and target track estimates are obtained by maximizing a posterior function in the state space. The performance of FMAP estimates is examined using Cramèr-Rao lower bound theory. By exploiting the sparsity of the Cholesky factor of information matrix, a fast implementation whose complexity scales linearly with the numbers of targets and measurements is derived.

The rest of this article is organized as follows. Section II is devoted to the algorithm derivation. An illustrative example is given in Section III. The results of simulation and experiment are presented in Sections IV and V, respectively. Finally we give concluding remarks in Section VI.

## II. Algorithm Derivation

In this section, we address the computational issues in using an EKF or UKF to solve joint tracking-registration (JTR). Fig. 1 shows the results of a joint problem with ten tracks and six registration parameters. The normalized covariance of the joint state from EKF is visualized in Fig. 1(a). Dark entries indicate strong correlations. It is clear that not only the tracks $x$ and the registration $a$ are correlated but also each

pair of tracks in $x$ is mutually correlated. The checkerboard appearance of the joint covariance matrix reveals this fact. Therefore, the approximation that ignores the off-diagonal correlated entries [24], [27] is not asymptotical optimal.

A key insight that motivates the proposed approach is shown in Fig. 1(b). Shown there is the Cholesky factor of the inverse covariance matrix (also known as information matrix) normalized like the correlation matrix. Entries in this matrix can be regarded as constraints, or connections, between the locations of targets and registration parameters. The darker an entry is in the display, the stronger the connection is. As this illustration suggests, the Cholesky factor $R$ not only appears sparse but also is nicely structured. The matrix is only dominated by the entries within a track, or the entries between a track and the registration parameters. The proposed FMAP algorithm exploits and maintains this structure throughout the calculation. In addition, storing a sparse factor matrix requires linear space. More importantly, updates can be performed in linear time with regard to the number of tracks in the system.

The sparsity of information matrix has been widely used to derive fast implementations of robotic Simultaneous Localization and Mapping (SLAM) [3], [9], [13], [16], [17]. In those approaches the authors insightfully observed that the resulting information matrix is sparse if the measurements involve only “local” variables. However the sparsity is destroyed in time-propagation steps where old robotic poses are removed from the state representation by marginalization. Approximations (e.g., [8], [16]) are needed to enforce sparsity during the marginalization.

Although inspired by SLAM information filters, FMAP is different in the following aspects:

- JTR and SLAM are different problems despite the similarity between their system dynamics equations. The number of stationary landmarks dominates the time

[^0]complexity in the SLAM case. On the other hand, the number of tracked targets that are in stochastic motion determines the time complexity in the JTR case.

- Unlike SLAM, FMAP needs no approximation to enforce the sparsity in the measurement update and time propagation, as illustrated in Fig. 1 (b).
- FMAP recursively computes Cholesky factor of infor-
mation matrix $R=\left[\begin{array}{cc}R_{s} & R_{s a} \\ 0 & R_{a}\end{array}\right]$ as shown in Fig. 1
(b), contrasting the fact that information matrix is com-
puted in the SLAM case. In addition, marginalization of
old tracked targets $x^{\prime}$ does not destroy the sparsity of
$R$.

Throughout this article italic upper and lower case letters are used to denote matrices and vectors, respectively. A Gaussian distribution is denoted by information array [4]. For example, a multivariate $x$ with density function $N(\bar{x},Q)$ is denoted as $p(x)\propto e^{\left(-\frac{2R x-x_{0}^{2}}{2}\right)}$ or the information array $[R,z]$ in short, where $z=R\bar{x}$ and $Q=R^{-1}R^{-T}$.

## A. Joint State Space

The setting for the JTR problem is that a vehicle, equipped with multiple sensors with unknown or partially unknown registration, moves through an environment containing a population of objects. The sensors can take measurements of the relative position and velocity between any individual object and the vehicle.

The objective here is to derive a joint dynamics model where $n$ tracks and registration parameters from $k$ sensors are stacked into one large state vector as below:

$$
s=\left[\begin{array}{llll}
x_{1}^{T} & x_{2}^{T} & \ldots & x_{n}^{T} & a_{1}^{T} & \ldots & a_{k}^{T}
\end{array}\right]^{T}
$$

where the $i$-th target track $x_{i},(i=1, \ldots n)$ comprises a set of parameters, e.g., position, velocity, and acceleration, and the registration parameters for $j$-th sensor $a_{j},(j=1, \ldots, k)$ comprises of location error, an azimuth alignment error, and range offset.

The system dynamics equation for the state is expressed as:

$$
s(t+1)=f(s(t), w(t))
$$

where the function relates the state at time $t$ to the state at time $t+1$; and where terms $w$ are vectors of zero-mean noise random variables that are assumed to have nonsingular covariance matrices.

The measurement process can be modeled symbolically as a function of target track $(x)$, and registration parameter (a), such as

$$
o(t)=h(x(t), a(t))+v(t)
$$

where $o(t)$ and $v(t)$ denote the measurements and the additive noise vectors at time instant $t$, respectively.


[^0]:    ${ }^{1}$ The Cholesky factor $R$ of a matrix $P$ is defined as $P=R^{t} R$. A semipositive definite matrix can be decomposed into its Cholesky factor.

## B. Measurement update

The FMAP algorithm works with the posterior density function $p\left(s(t) \mid o_{(0: t)}\right)$, where $o_{(0: t)}$ denotes a series of measurements $\{o(0), \ldots, o(t)\}$ from the sensors.

Using the Bayes rule, we obtain the posterior function as

$$
\begin{aligned}
& p\left(s(t) \mid o_{(0: t)}\right)=p\left(s(t) \mid o_{(0: t-1)}, o(t)\right) \\
& =c_{1}(t) p\left(o(t) \mid o_{(0: t-1)}, s(t)\right) p\left(s(t) \mid o_{(0: t-1)}\right)
\end{aligned}
$$

with $c_{1}(t)$ denotes the normalization factor. Typically, we will assume that measurements at time $t$ depend only on the current state $s(t)^{2}$, and (3) can be written as

$$
p\left(s(t) \mid o_{(0: t)}\right)=c_{1}(t) p(o(t) \mid s(t)) p\left(s(t) \mid o_{(0: t-1)}\right)
$$

Assuming the density functions are normally distributed, the prior density function ${ }^{3} p\left(s \mid o_{(0: t-1)}\right)$ can be expressed by information array $[\tilde{R}, \tilde{z}]$, i.e.,

$$
\begin{aligned}
& p\left(s \mid o_{(0: t-1)}\right)=\frac{|\tilde{R}|}{(2 \pi)^{N_{s} / 2}} \exp \left(-\frac{\|\tilde{R} s-\tilde{z}\|^{2}}{2}\right) \\
& =\frac{|\tilde{R}|}{(2 \pi)^{N_{s} / 2}} \exp \left(-\frac{\left\|\left[\begin{array}{cc}
\tilde{R}_{x} & \tilde{R}_{x a} \\
0 & \tilde{R}_{a}
\end{array}\right]\left[\begin{array}{l}
x \\
a
\end{array}\right]-\left[\begin{array}{c}
\tilde{z}_{x} \\
\tilde{z}_{a}
\end{array}\right]\right\|^{2}}{2}\right)
\end{aligned}
$$

where $|\tilde{R}|$ is the determinant of $\tilde{R}$, and $N_{s}$ is the dimension of $s$.

Linearizing (2) using Taylor expansion in the neighborhood $\left[x^{*}, a^{*}\right]$, produces:

$$
o=C_{x} x+C_{a} a+u_{1}+v
$$

with $u_{1}=h^{*}-C_{x} x^{*}-C_{a} a^{*}, h^{*}=h\left(x^{*}, a^{*}\right)$, and Jacobian matrices $C_{x}$ and $C_{a}$. Without loss of generality, the covariance matrix of $v$ is assumed to be an identity matrix ${ }^{4}$. Thus, the measurement density function can be written as

$$
\begin{aligned}
& p(o \mid s)=\frac{1}{(2 \pi)^{N_{o} / 2}} \\
& \cdot \exp \left(-\frac{\left\|\left[\begin{array}{cc}
C_{x} & C_{a}
\end{array}\right]\left[\begin{array}{l}
x \\
a
\end{array}\right]-\left(o-u_{1}\right)\right\|^{2}}{2}\right)
\end{aligned}
$$

with $N_{o}$ being the dimension of $o$.
The negative logarithm of (4) is given by

$$
\begin{aligned}
J_{t} & =-\log p\left(s \mid o_{(0: t)}\right) \\
& =-\log p(o \mid s)-\log p\left(s \mid o_{(0: t-1)}\right)-\log \left(c_{1}\right)
\end{aligned}
$$

[^0]Plugging in Eqs. (5) and (7), (8) becomes

$$
J_{t}=\frac{\left\|\left[\begin{array}{cc}
\tilde{R}_{x} & \tilde{R}_{x a} \\
0 & \tilde{R}_{a}
\end{array}\right]\left[\begin{array}{l}
x \\
a
\end{array}\right]-\left[\begin{array}{c}
\tilde{z}_{x} \\
\tilde{z}_{a}
\end{array}\right]\right\|^{2}}{2+c_{2}}
$$

with $c_{2}$ denoting terms not depending on $(x, a)$.
The principle of the maximum a posteriori (MAP) estimation is to maximize the posterior function with respect to the unknown variables $(x, a)$. Clearly, the maximization process is equivalent to minimization of the squared norm in (9). Ignoring the constant term, the right hand side (RHS) of (9) can be written as a matrix $X$ expressed as:

$$
X=\left[\begin{array}{ccc}
\tilde{R}_{x} & \tilde{R}_{x a} & \tilde{z}_{x} \\
0 & \tilde{R}_{a} & \tilde{z}_{a} \\
C_{x} & C_{a} & o-u_{1}
\end{array}\right]
$$

$X$ can be turned into an upper triangular matrix by applying an orthogonal transformation $\hat{T}$ :

$$
\hat{T} X=\left[\begin{array}{ccc}
\tilde{R}_{x} & \tilde{R}_{x a} & \tilde{z}_{x} \\
0 & \tilde{R}_{a} & \tilde{z}_{a} \\
0 & 0 & e
\end{array}\right]
$$

where $e$ is the residual that reflects the discrepancy between the model and measurement. Applying orthogonal $\hat{T}$ to the quadratic term in (9), produces ${ }^{5}$ :

$$
J_{t}=\frac{\left\|\left[\begin{array}{cc}
\tilde{R}_{x} & \tilde{R}_{x a} \\
0 & \tilde{R}_{a}
\end{array}\right]\left[\begin{array}{l}
x \\
a
\end{array}\right]-\left[\begin{array}{l}
\tilde{z}_{x} \\
\tilde{z}_{a}
\end{array}\right]\right\|^{2}}{2}+c_{3}
$$

with $c_{3}=c_{2}+\frac{1}{2}\|e\|^{2}$ denoting the constant term with respect to variables $(x, a)$.

Because $J_{t}$ is the negative logarithm of $p\left(s \mid o_{(0: t)}\right)$, the posterior density can be written as

$$
p\left(s \mid o_{(0: t)}\right) \propto e^{-\frac{\left\|\left[\begin{array}{cc}
\tilde{R}_{x} & \tilde{R}_{x a} \\
0 & \tilde{R}_{a}
\end{array}\right]\left[\begin{array}{l}
x \\
a
\end{array}\right]-\left[\begin{array}{l}
\tilde{z}_{x} \\
\tilde{z}_{a}
\end{array}\right]\right\|^{2}}
$$

or in the information-array form

$$
[\tilde{R}, \tilde{z}]=\left[\begin{array}{cc}
\tilde{R}_{x} & \tilde{R}_{x a} & \tilde{z}_{x} \\
0 & \tilde{R}_{a} & \tilde{z}_{a}
\end{array}\right]
$$

Since the estimate of the state variable $s$ can be written as $\hat{s}=\hat{R}^{-1} \hat{z}$, (14) allows us to solve the estimates of the track variables $\hat{x}$ and registration parameters $\hat{a}$ by back-substitution using $\hat{R}$ and right hand side $\hat{z}$, i.e.,

$$
\left[\begin{array}{cc}
\tilde{R}_{x} & \tilde{R}_{x a} \\
0 & \tilde{R}_{a}
\end{array}\right]\left[\begin{array}{l}
x \\
a
\end{array}\right]=\left[\begin{array}{l}
\tilde{z}_{x} \\
\tilde{z}_{a}
\end{array}\right]
$$

[^1]
[^0]:    ${ }^{3}$ In Bayesian filtering, the state variables are designed such that they contain all information gathered from the past measurements. Thus $s(t)$ is a sufficient statistics of the past measurements $o_{(0: t-1)}$.
    ${ }^{4}$ Unless it is necessary, we will not include time such as (t) in all the following equations.
    ${ }^{4}$ If not, the noise term $v$ in (6) can be transformed to a random vector with identity covariance matrix. Let $\operatorname{cov}\{v\}=R_{v}$ denote the covariance matrix of the measurement model. Multiplying both sides of (6) by $L_{v}$, the square root information matrix of $R_{v}$, results in a measurement equation with an identity covariance matrix.

[^1]:    ${ }^{5}$ The least-squares $\|R s-z\|^{2}$ is invariant under an orthogonal transformation $T$, i.e., $\|T(R s-z)\|^{2}=(R s-z)^{t} T^{t} T(R s-z)=(R s-z)^{t}(R s-$ $z)=\|R s-z\|^{2}$.

## C. Time propagation

The prior density $p\left(s(t+1) \mid o_{(0: t)}\right)$ at time $t+1$ can be inferred from the system dynamics and posterior function $p\left(s \mid o_{(0: t)}\right)$ at time $t$. Assuming registration is time-invariant the linear approximation of the system dynamics in (1) in the neighborhood $\left[s^{*}, w^{*}\right]$ can be expressed as,

$$
\left[\begin{array}{c}
x(t+1) \\
a(t+1)
\end{array}\right]=\left[\begin{array}{cc}
\Phi_{x} & 0 \\
0 & I
\end{array}\right]\left[\begin{array}{l}
x \\
a
\end{array}\right]+\left[\begin{array}{c}
G_{x} \\
0
\end{array}\right] w+\left[\begin{array}{c}
u_{2} \\
0
\end{array}\right]
$$

where $\Phi_{x}$ and $G_{x}$ are Jacobian matrices; and the nonlinear term $u_{2}=f\left(s^{*}, w^{*}\right)-\Phi_{x} x^{*}-G_{x} w^{*}$.

If variables $s$ and $w$ are denoted by the information arrays in (14) and $\left[R_{w}, z_{w}\right]$, respectively, the joint density function given the measurements $o_{(0: t)}$ can be expressed in terms of $x(t+1)$ and $a(t+1)$ as $^{6}$

$$
p\left(s(t+1), w \mid o_{(0: t)}\right) \propto e^{-\frac{\left\|A z_{w}-b\right\|^{2}}{2}}
$$

with $\quad A \quad=\left[\begin{array}{ccc}R_{w} & 0 & 0 \\ -\bar{R}_{x} \Phi_{x}^{-1} G_{x} & \bar{R}_{x} \Phi_{x}^{-1} & \bar{R}_{x a} \\ 0 & 0 & \bar{R}_{a}\end{array}\right]$, $s_{w}=\left[\begin{array}{c}w \\ x(t+1) \\ a(t+1)\end{array}\right]$, and $b=\left[\begin{array}{c}z_{w} \\ \tilde{z}_{x}+\tilde{R}_{x} \Phi_{x}^{-1} u_{2} \\ \tilde{z}_{a}\end{array}\right]$.

The quadratic exponential term in (17) can be denoted as matrix $Y$, expressed as

$$
Y=\left[\begin{array}{ll}
A & b
\end{array}\right]
$$

The matrix $Y$ can be turned into a triangular matrix through an orthogonal transformation $\hat{T}$, i.e.,

$$
\hat{T} Y=\left[\begin{array}{ll}
\tilde{A} & \tilde{b}
\end{array}\right]
$$

with $\tilde{A}=\left[\begin{array}{ccc}\tilde{R}_{w}(t+1) & \tilde{R}_{w x}(t+1) & \tilde{R}_{w a}(t+1) \\ 0 & \tilde{R}_{x}(t+1) & \tilde{R}_{x a}(t+1) \\ 0 & 0 & \tilde{R}_{a}(t+1)\end{array}\right]$ and $\tilde{b}=$ $\left[\begin{array}{c}\tilde{z}_{w}(t+1) \\ \tilde{z}_{x}(t+1) \\ \tilde{z}_{a}(t+1)\end{array}\right]$.

Given the measurements $o_{(0: t)}$, the prior function $p(s(t+$ 1) $\left|o_{(0: t)}\right\rangle$ can be produced by marginalization on variable $w$. Applying Lemma 6.3 in Appendix A, we obtain

$$
\begin{aligned}
& p\left(s(t+1) \mid o_{(0: t)}\right)=c_{4} \exp -\frac{\|\tilde{R}(t+1) s(t+1)-\tilde{z}(t+1)\|^{2}}{2} \\
& =c_{4} e^{-\frac{\left\|\left[\begin{array}{cc}
\bar{R}_{x}(t+1) & \bar{R}_{x a}(t+1) \\
0 & \bar{R}_{a}(t+1)
\end{array}\right]\left[\begin{array}{c}
x(t+1) \\
a(t+1)
\end{array}\right]-\left[\begin{array}{c}
\tilde{z}_{x}(t+1) \\
\tilde{z}_{a}(t+1)
\end{array}\right]\right\|^{2}}{2}
\end{aligned}
$$

with $c_{4}$ being the normalization factor.
Therefore, we obtain the updated prior information array $[\tilde{R}(t+1), \tilde{z}(t+1)]$ at time $t+1$ as:

$$
\left[\begin{array}{ccc}
\tilde{R}_{x}(t+1) & \tilde{R}_{x a}(t+1) & \tilde{z}_{x}(t+1) \\
0 & \tilde{R}_{a}(t+1) & \tilde{z}_{a}(t+1)
\end{array}\right]
$$

${ }^{6}$ Detailed derivation is shown in Lemma 6.2 in Appendix A.

The derivation leading to (20) illustrates the purposes of using the information array $[\tilde{R}, \tilde{z}]$, which is recursively updated to $[\tilde{R}(t+1), \tilde{z}(t+1)]$ at time instant $t+1$.

One can verify (c.f., [4, VI.3]) that the covariance matrix $\tilde{P}(t+1)=\Phi \tilde{P} \Phi^{T}+G Q G^{T}$ where $\tilde{P}(t+1)=$ $\tilde{R}^{-1}(t+1) \tilde{R}^{-T}(t+1), \tilde{P}=\tilde{R}^{-1} \tilde{R}^{-T}, Q=R_{w}^{-1} R_{w}^{-T}$, $G=\left[\begin{array}{ll}G_{x}^{T} & 0\end{array}\right]^{T}$ and $\Phi=\left[\begin{array}{cc}\Phi_{x} & 0 \\ 0 & I\end{array}\right]$. In addition, $\tilde{s}(t+1)=\Phi \tilde{s}+G \bar{w}+u$ where $\tilde{s}(t+1)=\tilde{R}^{-1}(t+1) \tilde{z}(t+1)$, $\bar{w}$ denotes the mean of $w$, and $u=\left[\begin{array}{ll}u_{2}^{T} & 0\end{array}\right]^{T}$.

## D. Algorithm

Fig. 2 illustrates the flow chart of FMAP. The algorithm is started upon reception of sensor data, and the state variables of every track and registration parameters are initialized using zero-mean noninformative distributions, respectively. A data association module matches the sensor data with the predicted location of targets. The measurement update module combines the previous estimation (i.e., prior) and new data (i.e., matched measurement-track pairs), and updates target estimation and registration. FMAP checks whether the discrepancy between measurements and predictions (innovation error) is larger than a threshold $T$. A change of registration parameters is detected when the threshold is surpassed, and the prior of the sensor registration is reset to the noninformative distribution. This is typically occurred when the sensor's pose is significantly moved. The time propagation module predicts the target and registration in the next time instant based on the dynamics model (16).

The complete specification of the proposed algorithm is given in Algorithm 1. Note that the prior $\left[\tilde{R}_{0}, \tilde{z}_{0}\right]$ at time 0 is initialized as $\bar{R}_{0}=\varepsilon I$ and $\tilde{z}_{0}=\mathbf{0}$ where $\varepsilon$ is a small positive number, and $I$ is an identity matrix of appropriate dimension.

Although static registration $a$ is assumed in the derivation (i.e., Eq. (16)), the case in which $a$ in stochastic motion can be easily accommodated. As shown in Fig. 9, the step change of $a$ can be easily detected by applying threshold checking to innovation error curve. Once a change is detected, we set the registration prior to the noninformative distribution, i.e., $\tilde{z}_{a}=\mathbf{0}$ and $\tilde{R}_{a}=\varepsilon I$. This forces FMAP to forget all past information regarding registration and to trigger a new estimation for $a$. Since $a$ rarely occurs and sufficient duration exists between two changes, as shown in Fig. 9, we can approximate the dynamics of sensor by a piecewise static time propagation model.

## E. Statistical Efficiency Analysis

The Cramèr-Rao lower bound (CRLB) is a measure of statistical efficiency of an estimator. Let $p\left(o_{(0: t)}, s\right)$ be the joint probability density of the state (parameters) $s$ at time instant $t$ and the measured data $o_{(0: t)}$, and let $g\left(o_{(0: t)}\right)$ be a

![img-0.jpeg](img-0.jpeg)

Fig. 2. Flow chart of the fast maximum a posteriori (FMAP) algorithm.

## Algorithm 1: FMAP update

**Require:** Given prior at instant $t$ (i.e., previous results and its uncertainty measure) expressed as information array $[\hat{R}, \hat{z}]$ and measurements $o$; the system dynamical equation (1) and measurement equation (2).

**Ensure:** The updated estimate of $s$ expressed by $\hat{s}$

1. Compute $C_{s}$, $C_{a}$, and $u_{1}$.
2. Plug prior $[\hat{R}, \hat{z}]$; sensor measurement matrices $C_{x}$ and $C_{a}$; and vectors $u_{1}$ and $o$ into matrix $X$ (c.f., (10)).
3. Factorize $X$ (c.f., Algorithm 2).
4. Derive the posterior density information array $[\hat{R}, \hat{z}]$ as shown in (14) (Measurement update).
5. Compute the update of tracking and registration as $\hat{s} = R^{-1} \hat{z} \text{ (c.f., (15))}$.
6. Compute $\Phi_{s}$, $G_{s}$, and $u_{2}$.
7. Plug the posterior information array $[\hat{R}, \hat{z}]$, $R_{w}$, $\Phi_{x}$, and $G_{x}$ into $Y$.
8. Factorize $Y$ (c.f., Algorithm 3).
9. Derive prior information array $[\hat{R}(t+1), \hat{z}(t+1)]$ for time $t+1$ (c.f., (20)), which can be utilized when the new sensor measurements are available (Time propagation).

Function of an estimate of $s$. The CRLB for the estimation error has the form

$$P \equiv \mathrm{E}\{[g(o_{(0:t)})-s][g(o_{(0:t)})-s]^{t}\} \ge J_t \tag{21}$$

where $J_t$ is the Fisher information matrix with the elements

$$J_{t}^{(ij)} = \mathrm{E}\left\{\frac{\partial^2 \log p(o_{(0:t)}, s)}{\partial s_i \partial s_j}\right\}$$

**Proposition 2.1:** Considering the system defined by (1) and (2), the Fisher information matrix of the system $J_t$ at time $t$ is identical to $[\hat{R}(t)]^t[\hat{R}]$, with $\hat{R}(t)$ defined in (14).

**Proof:** The joint probability density can be derived from the equality $p(o_{(0:t)}, s) = p(s|o_{(0:t)})p(o_{(0:t)})$. Since $p(o_{(0:t)})$ is a function of measured data, not depending on the state $s$; therefore, we have $J_t = \mathrm{E}\{\Delta \log p(s|o_{(0:t)}\}$ where $\Delta$ denotes the second-order partial derivative, i.e., $\Delta L(s) = \frac{\partial L(s)}{\partial s} \frac{\partial L(s)}{\partial s}^t$. Plugging (13) in, the logarithm of the posterior function $\log p(s|o_{(0:t)})$ reads

$$-\log p(s|o_{(0:t)}) = c_0 + \frac{\|\hat{R}s - \hat{z}\|^2}{2}$$

where $c_0$ denotes a constant independent of $s$. Then the Fisher information matrix $J_t$ reads $J_t = [\hat{R}(t)]^t[\hat{R}]$.

If $s$ is estimated by $g(s) = \mathrm{E}(s|o_{(0:t)}) = \hat{R}^{-1} \hat{z}$, then (21) is satisfied with equality. Therefore the FMAP algorithm is optimal in the sense of CRLB.

### F. Fast Implementation

We have observed the FMAP algorithm comprises two factorization operations outlined in Eqs. (11) and (19), and back substitution operation (15). However, directly applying matrix factorization techniques (e.g., QR decomposition) can be as computationally ineffective as the UKF since the complexity of QR is $O(n^3)$ ($n$ denotes number of targets).

![img-1.jpeg](img-1.jpeg)

Fig. 3. Triangular factorization (a) Example $X$ matrix (b) Example $Y$ matrix

As shown in Fig. 1, we have noted that the matrices in (10) are nicely structured. Fig. 3(a) illustrates an example schematically with two tracks, two registration parameters, and six measurements. The non-zero elements of the matrix in (10) are denoted by crosses; and a blank position represents a zero element.

Givens rotation [10] is used to eliminate the non-zero elements of the matrix $C_x$ in (10), shown in Fig. 3(a) as crosses surrounded by circles. Givens rotation is applied from

the left to the right and for each column from the top to the bottom. Each non-zero low-triangular element in the $i$-th row of $C_{x}$, is combined with the diagonal element in the same column in the matrix block $\tilde{R}_{x}$ to construct the rotation. If the element in $C_{x}$ is zero, then no rotation is needed.

Consequently, the algorithm to factorize $X$ can be written as Algorithm 2. Note that Algorithm 2 is an in-place algorithm, which uses a small, constant amount of extra storage space.

```
Algorithm 2: Factorization of \(X\)
Require: Given \(X\) defined in (10).
Ensure: Output an upper triangular matrix \(X^{\prime}=\hat{T} X\) such
    that \(X^{\prime \prime} X^{\prime}=X^{\prime} X\), with \(\hat{T}\) an orthogonal matrix.
    Let \(L\) be the dimension of \(s\).
    for all Column \(j\) in \(C_{x}\) do
        for all Row \(i\) in \(C_{x}\) do
            if \(C_{x}(i, j) \neq 0\) then
                Let \(\alpha=\tilde{R}_{x}(i, i)\) and \(\beta=C_{x}(i, j)\).
                    Construct the rotation \(\operatorname{Rot}(\alpha, \beta)=\)
                \(\alpha / r \quad \beta / r\)
                \(-\beta / r \quad \alpha / r\)
            for all \(k\) such that \(j \leq k \leq N\), with \(N\) denoting
            the last column of \(X\) do
                if \(X(i, k) \neq 0\) or \(X(i+L, k) \neq 0\) then
                    Let \(d=\left[\begin{array}{c}X(i, k) \\ X(i+L, k)\end{array}\right] \).
                    Apply the rotation \(\operatorname{Rot}(\alpha, \beta)\) to \(d\), i.e., \(d^{\prime}=\)
                    \(\operatorname{Rot}(\alpha, \beta) d\).
                    Save \(d^{\prime}\) back to \(X\) in the same location as \(d\).
                    end if
                    end for
            end if
            end for
    end for
17: Apply QR decomposition to the sub-matrix \(\Lambda=\)
    \(\left[\begin{array}{ll}\tilde{R}_{a} & \tilde{z}_{a} \\ C_{a} & o-u_{1}\end{array}\right]\), i.e., \(\Lambda=T_{q r} U\) with \(T_{q r}\) and \(U\) being
    the orthogonal and upper triangular matrices, respectively.
18: Write the result \(U\) back to \(X\) in the same location as \(\Lambda\).
```

Lemma 2.1: If $\tilde{R}_{x}$ in (10) is a block-diagonal matrix, then 1) the result $\tilde{R}_{x}$ in (11) has the same form as $\tilde{R}_{x}$; and 2) the complexity of Algorithm 2 is $O\left(m k^{2}\right)$, where $m$ and $k$ denote the numbers of measurements and sensors, respectively.

Proof: The triangulation described in Algorithm 2 comprises of two steps: first turn $C_{x}$ into a zero matrix using Givens rotation; and second apply QR decomposition to the sub-matrix $\Lambda$. Note that $C_{x}$ in $X$ is sparse. This is seen by expanding the measurement equation (2) as $o_{a, i}^{(j)}=h\left(x_{i}, a_{j}\right)+v_{j}$ where $o_{a, i}^{(j)}$ denotes the measurements associated with the target track $x_{i}$ from the $j$-th sensor; and $\kappa_{i}$ is the measurement association variable for the $i$-th target track. Therefore, there is at most $O\left(N_{x}+k N_{a}\right)$ nonzero entries in each paired set of rows of $\tilde{R}_{x}$ and $C_{x}$, where $N_{x}$ denotes the number of parameters for each tracked target; and
$N_{a}$ denotes the number of registration parameters for each sensor. Since an off-diagonal zero entry $\varsigma$ in $\tilde{R}_{x}$ pairs up with a zero entry in $C_{x}$ in the rotation operations, the condition specified in Step 8 of Algorithm 2 is not satisfied, and then the off-diagonal entry $\varsigma$ remains zero after the rotation. Thus 1) is established.

We note that in each paired set of rows of $\tilde{R}_{x}$ and $C_{x}$, there are at most $O\left(N_{x}+k N_{a}\right)$ non-zero pairs. Therefore, in order to turn an element of $C_{x}$ to zero, at most $O\left(N_{x}+k N_{a}\right)$ rotations in Step 10 are needed. Providing that $m$ measurements are presented, $O\left(m N_{x}\right)$ elements need to be eliminated to zero. Givens rotation is applied a maximum $O\left(m N_{x}^{2}+m k N_{x} N_{a}\right)$ times to transform $C_{x}$ into a zero matrix, which is equivalent to $O(m k)$ additive and multiplicative operations. In the second step, additional $O\left(m k^{2}\right)$ operations are needed. Therefore, the total complexity is $O\left(m k^{2}\right)$.

Triangulation of (19) can be treated similarly as that of (11). Fig. 3(b) illustrates an example schematically with two tracks and two registration parameters. The non-zero elements of the matrix $Y$ are denoted by crosses; and blank position represents a zero element. Givens rotation is used to eliminate the non-zero entries in the matrix $R_{x G}^{d}=$ $-\tilde{R}_{x} \Phi_{x}^{-1} G_{x}$, shown in Fig. 3(b) as crosses annotated by circles. Givens rotation is applied from the left to the right and for each column from the top to the bottom. Each nonzero entry in the $i$-th row of the matrix $R_{x G}^{d}$ is paired with the element in the same column in $R_{w}$ to construct the rotation.

Similarly, the algorithm to factorize $Y$ is given as Algorithm 3.

Lemma 2.2: If $\tilde{R}_{x}$ in (18) is a block-diagonal matrix, then 1) the result $\tilde{R}_{x}(t+1)$ in (19) has the same form as $\tilde{R}_{x}$; and 2) the complexity of Algorithm 3 is $O(n k)$, with $n$ denoting the number of targets.

Proof: Each individual target has its own system dynamics equation. For the $i$-th target, (16) can be expressed as:

$$
x_{i}(t+1)=\Phi_{i} x(t)+G_{i} w_{i}(t)+u_{2 i}
$$

where $\Phi_{i}$ and $G_{i}$ are Jacobian matrices; the nonlinear term $u_{2 i}=f\left(x_{i}^{*}, w_{i}^{*}\right)-\Phi_{i} x_{i}^{*}-G_{i} w_{i}^{*}$; and $w_{i}(t)$ is represented by the information array $\left[R_{w i}, z_{w i}\right]$. Therefore, the corresponding collective quantities $\Phi_{x}, G_{x}$, and $R_{w}$ are in the same block-diagonal form. In addition, $\tilde{R}_{x} \Phi_{x}^{-1}$ and $R_{x G}^{d}$ are in the same block-diagram form. Since each off-diagonal zero entry $\varsigma$ in $\tilde{R}_{x} \Phi_{x}^{-1}$ pairs up with a zero entry in the rotation operations, the condition in Steps 8 and 24 is not satisfied for the pairs and, then, the off-diagonal entry $\varsigma$ remains zero. Thus 1) is established.

As Fig. 3(b) shows, in the paired rows of $R_{w}$ and $R_{x G}^{d}$, there are at most $O\left(2 N_{x}+k N_{a}\right)$ non-zero pairs. Thus, to eliminate an element to zero, a maximum $O\left(2 N_{x}+k N_{a}\right)$ rotations in Steps 10 and 26 are needed. If $n$ tracked targets are considered, $O\left(n N_{x}^{2}\right)$ elements need to be eliminated to zero. Givens rotation is applied a maximum $O\left(2 n N_{x}^{3}+k n N_{a} N_{x}^{2}\right)$

Algorithm 3: Factorization of $Y$
Require: Given $Y$ defined in (18).
Ensure: Output an upper triangular matrix $Y^{\prime}=\hat{T} Y$ such that $Y^{\prime t} Y^{\prime}=Y^{t} Y$, with $\hat{T}$ an orthogonal transformation.
1: Let $R_{x G}^{d}=-\hat{R}_{x} \Phi_{x}^{-1} G_{x}$. Let $L$ be the number of rows in $R_{w}$.
2: for all Column $j$ in $R_{x G}^{d}$ do
3: for all Row $i$ in $R_{x G}^{d}$ do
4: if $R_{x G}^{d}(i, j) \neq 0$ then
5: $\quad$ Let $\alpha=Y(i, i)$ and $\beta=R_{x G}^{d}(i, j)$.
6: $\quad$ Construct the rotation $\operatorname{Rot}(\alpha, \beta)$.
7: for all $k$ such that $j \leq k \leq N$, with $N$ denoting the last column of $Y$ do
8: $\quad$ if $B(i, k) \neq 0$ or $B(i+L, k) \neq 0$ then
9: $\quad$ Let $d=\left[\begin{array}{c}B(i, k) \\ B(i+L, k)\end{array}\right]$
10: $\quad$ Apply the rotation $\operatorname{Rot}(\alpha, \beta)$ to $d$, i.e., $d^{\prime}=$ $\operatorname{Rot}(\alpha, \beta) d$
11: $\quad$ Save $d^{\prime}$ back to $Y$ in the same location as $d$. 12: end if
13: end for
14: end if
15: end for
16: end for
17: Let $R_{x}^{d^{\prime}}=\hat{R}_{x} \Phi_{x}^{-1}$. Let $M$ be the number of columns of $R_{w}$.
18: for all Column $j$ in $R_{x}^{d}$ do
19: for all Row $i$ in $R_{x}^{d}$ do
20: if $R_{x}^{d}(i, j) \neq 0$ then
21: $\quad$ Let $\alpha=Y(i, i+M)$ and $\beta=R_{x}^{d}(i, j)$.
22: $\quad$ Construct the rotation $\operatorname{Rot}(\alpha, \beta)$.
23: for all $k$ such that $j+M \leq k \leq N$, with $N$ denoting the last column of $Y$ do
24: $\quad$ if $B(i, k) \neq 0$ or $B(i+L, k) \neq 0$ then
25: $\quad$ Let $d=\left[\begin{array}{c}B(i, k) \\ B(i+L, k)\end{array}\right]$
26: $\quad$ Apply the rotation $\operatorname{Rot}(\alpha, \beta)$ to $d$, i.e., $d^{\prime}=$ $\operatorname{Rot}(\alpha, \beta) d$
27: $\quad$ Save $d^{\prime}$ back to $Y$ in the same location as $d$. 28: end if
29: end for
30: end if
31: end for
32: end for
32: end for
times to transform the matrix $Y$ into a triangular matrix, which is equivalent to $O(n k)$ additive and multiplicative operations. 2) is established.

Lemma 2.3: The complexity of the back substitution operation expressed in (15) is $O\left(n+k^{3}\right)$.

Proof: Since $\hat{R}_{x}$ is a block-diagonal matrix, (15) can be written as

$$
\left[\begin{array}{cccc}
\hat{R}_{x_{1}} & \ldots & 0 & \hat{R}_{x_{1} a} \\
\vdots & \ddots & \vdots & \vdots \\
0 & \ldots & \hat{R}_{x_{n}} & \hat{R}_{x_{n} a} \\
0 & \ldots & 0 & \hat{R}_{a}
\end{array}\right]\left[\begin{array}{c}
x_{1} \\
\vdots \\
x_{n} \\
a
\end{array}\right]=\left[\begin{array}{c}
z_{x_{1}} \\
\vdots \\
z_{x_{n}} \\
z_{a}
\end{array}\right]
$$

where $x_{i}$ denotes the $i$-th target. One can verify that

$$
\begin{aligned}
a & =\hat{R}_{a}^{-1} \\
x_{i} & =\hat{R}_{x_{i}}^{-1}\left(\hat{z}_{x_{i}}-\hat{R}_{x_{i} a} a\right)
\end{aligned}
$$

$O\left(\left(k N_{a}\right)^{3}\right)$ and $O\left(n N_{a}^{3}\right)$ operations are needed to solve $\hat{a}$ and $\hat{x_{i}}$ for $i=1, \ldots, n$ in (22), respectively. Let $\hat{P}_{x_{i}}$ and $\hat{P}_{a}$ be covariance matrices of $x_{i}$ and $a$. We can write

$$
\begin{aligned}
\hat{P}_{a} & =\hat{R}_{a}^{-1} \hat{R}_{a}^{-T} \\
\hat{P}_{x_{i}} & =\hat{R}_{x_{i}}^{-1} \hat{R}_{x_{i}}^{-T}+\hat{R}_{a}^{-1} \hat{R}_{x_{i} a} \hat{P}_{a} \hat{R}_{x_{i} a}^{T} \hat{R}_{a}^{-T}
\end{aligned}
$$

Additional $O\left(\left(k N_{a}\right)^{3}\right)$ and $O\left(n N_{a}^{3}\right)$ operations are needed to solve $\hat{P}_{a}$ and $\hat{P}_{x_{i}}$ for $i=1, \ldots, n$ in (23), respectively.

Therefore, the total complexity is $O\left(n+k^{3}\right)$.
To summarize, we establish the following proposition:
Proposition 2.2: The complexity of the FMAP algorithm is $O\left((m+n) k^{2}+k^{3}\right)$, where $m, n$ and $k$ denote the numbers of measurement equations, targets and sensors.

Proof: The FMAP algorithm comprises of three matrix operations whose complexity are specified by Lemmas 2.1, 2.2 and 2.3, respectively. Thus the total complexity is $O\left(m k^{2}+n k+n+k^{3}\right)=O\left((m+n) k^{2}+k^{3}\right)$.

Note that the number of sensors $k$ is a constant. The complexity in the above proposition is thus simplified as $O(n+m)$. This shows FMAP scales linearly with the number of measurements and with the number of target tracks.

## G. Handling Changes of the State Vector

So far, we have assumed the state vector $s=[x, a]$ has a fixed dimension. This means that we have the same number of targets in the whole observation span. However this is rarely true in practice. The dimension of $s$ changes due to new targets coming into or existing targets leaving the field-of-view of the sensors.

Once $s$ has been estimated at time instant $t$ (c.f., Section II-B), the prior distribution of $s(t+1)$ (inferred from $s$ ) can be easily obtained using the method described in Section II-C. Therefore, the main problem is to compute the distribution of the updated state vector $s^{\prime}(t+1)$ after changes of the state vector $s$.

In the following we define different vectors:

- $x^{r}$ : all targets that are visible at instant $t$ and remain at instant $t+1$;
- $x^{c}$ : all new targets that are visible at instant $t+1$ but not visible at instant $t$;
- $x^{d}$ : all deleted targets that are visible at instant $t$ but not visible at instant $t+1$;
- $s^{r}$ : the concatenated vector of the remaining targets and registration parameters, i.e., $s^{r}=\left[x^{r}, a\right]$.
Note that the following relationships hold:

$$
s(t+1)=\left[\begin{array}{c}
x^{d} \\
s^{r}
\end{array}\right], s^{\prime}(t+1)=\left[\begin{array}{c}
x^{c} \\
s^{r}
\end{array}\right]
$$

Let $\Pi=\left\{\pi_{1}, \ldots, \pi_{d}, \pi_{d+1}, \ldots, \pi_{n}\right\}$ be a permutation of $s(t+1)$ such that

$$
s(t+1)=\left[\begin{array}{ll}
x^{d} & \\
x_{\pi_{1}}, \ldots, x_{\pi_{d}} & x^{r} \\
x_{\pi_{d+1}}, \ldots, x_{\pi_{n}}, a
\end{array}\right]
$$

So we can find a permutation matrix [10] $P_{\Pi}=\left[P_{\Pi}^{(1)}, P_{\Pi}^{(2)}\right]$ such that

$$
P_{\Pi} s(t+1)=\left[\begin{array}{c}
P_{\Pi}^{(1)} s(t+1) \\
P_{\Pi}^{(2)} s(t+1) \\
a(t+1)
\end{array}\right]=\left[\begin{array}{c}
x^{d} \\
x^{r} \\
a(t+1)
\end{array}\right]
$$

We can verify that the marginal distribution of $s^{r}$ as (c.f., Lemma 6.3 in Appendix A)

$$
s^{r}=\left[\begin{array}{c}
x^{r} \\
a(t+1)
\end{array}\right] \sim\left[\begin{array}{ccc}
\tilde{R}_{x}^{r} & \tilde{R}_{x a}^{r} & \tilde{z}_{x}^{r} \\
0 & \tilde{R}_{a}(t+1) & \tilde{z}_{a}(t+1)
\end{array}\right]
$$

with

$$
\begin{aligned}
\tilde{R}_{x}^{r} & =P_{\Pi}^{(2)} \tilde{R}_{x}(t+1)\left(P_{\Pi}^{(2)}\right)^{T} \\
\tilde{R}_{x a}^{r} & =P_{\Pi}^{(2)} \tilde{R}_{x a}(t+1) \\
\tilde{z}_{x}^{r} & =P_{\Pi}^{(2)} \tilde{z}_{x}(t+1)
\end{aligned}
$$

where $\tilde{R}_{x}(t+1), \tilde{R}_{x a}(t+1), \tilde{R}_{a}(t+1), \tilde{z}_{x}(t+1)$, and $\tilde{z}_{a}(t+1)$ are defined in (20). We note that $\tilde{R}_{x}^{r}$ is a blockdiagonal matrix, i.e., $\tilde{R}_{x}^{r}=\operatorname{diag}\left(\left[\tilde{R}_{\Pi_{d+1}}, \ldots, \tilde{R}_{\Pi_{n}}\right]\right)$ where $\tilde{R}_{\Pi_{i}}$ denotes the $\Pi_{i}$-th diagonal block in $\tilde{R}_{x}(t+1)$.

Giving the new targets $x^{c}=\left[x_{1}^{c}, \ldots, x_{k}^{c}\right]$ at instant $t+1$, we can write the updated state vector $s^{\prime}(t+1)=$ $\left[\overbrace{x_{1}^{c}, \ldots, x_{k}^{c}}^{x^{c}} \overbrace{x_{\pi_{d+1}}, \ldots, x_{\pi_{n}}, a}^{x^{r}}\right]$. Assume the new targets are distributed as $x^{c} \sim\left[R^{c}, z^{c}\right]$ where $R^{c}$ denotes a blockdiagonal noninformative information matrix ${ }^{7}$. In addition we assume $x^{c}$ be statistically independent of $s^{r}$. Therefore, the updated state vector $s^{\prime}(t+1)$ is distributed as

$$
s^{\prime}(t+1) \sim\left[\begin{array}{ccc}
R^{c} & 0 & 0 & z^{c} \\
0 & \tilde{R}_{x}^{r} & \tilde{R}_{x a}^{r} & \tilde{z}^{r} \\
0 & 0 & \tilde{R}_{a}(t+1) & \tilde{z}_{a}(t+1)
\end{array}\right]
$$

## III. AN ILLUSTRATIVE EXAMPLE

The schematic illustration in Fig. 4 includes the sensors mounted at the front of a vehicle at positions A and B. A single target T , in front and in the same lane as the vehicle, moves away from the vehicle.

In the scenario illustrated in Fig. 4, the positions of the sensors A and B are denoted by $\left(\xi_{A 0}, \eta_{A 0}\right)$ and $\left(\xi_{B 0}, \eta_{B 0}\right)$, respectively. The orientations of the sensors A and Sensor B are denoted by $\Psi_{A 0}$ and $\Psi_{B 0}$, respectively. The target is located at position $x=\left(\xi, v_{\xi}, \eta, v_{\eta}\right)$ in the $\xi \eta$-coordinate system. Let the registration parameters of Sensor A and

[^0]![img-2.jpeg](img-2.jpeg)

Fig. 4. An example
B be $a_{A}=\left(\xi_{A 0}, \eta_{A 0}, \Psi_{A 0}\right)$ and $a_{B}=\left(\xi_{B 0}, \eta_{B 0}, \Psi_{B 0}\right)$, respectively. Then the joint state vector $s=\left[\begin{array}{lll}x & a_{A} & a_{B}\end{array}\right]$.

Providing each sensor measures range $(r)$, range rate $(\hat{r})$, and azimuth angle $(\theta)$, the measurement functions $h_{A}=\left(\begin{array}{ll}r_{A}, \hat{r}_{A}, \theta_{A}\end{array}\right)$ for Sensor A can be expressed as, $r_{A}=\sqrt{\left(\xi-\xi_{A 0}\right)^{2}+\left(\eta-\eta_{A 0}\right)^{2}}, \hat{r}_{A}=v_{r}^{T} n_{A}$ and $\theta_{A}=$ $\arctan \left(\frac{\eta-\eta_{A 0}}{\xi-\xi_{A 0}}\right)-\Psi_{A 0}$, respectively, where $v_{r}$ and $n_{A}$ denote the relative velocity vector $\left(v_{\xi}, v_{\eta}\right)$ and unit vector along the direction from the target to Sensor A. Approximating the measurement functions $h_{A}$ in linear form at the neighborhood of the point $\left(x^{*}, a_{A}^{*}\right)$, produces:

$$
\begin{gathered}
C_{A x}=\left.\frac{\partial h_{A}}{\partial x}\right|^{\ast}=\left[\begin{array}{ccc}
\frac{\xi^{*}-\xi_{A 0}^{*}}{r_{A}^{*}} & 0 & \frac{\eta^{*}-\eta_{A 0}^{*}}{r_{A}^{*}} & 0 \\
0 & \frac{\xi^{*}-\xi_{A 0}^{*}}{r_{A}^{*}} & 0 & \frac{\eta^{*}-\eta_{A 0}^{*}}{r_{A}^{*}} \\
-\frac{\eta^{*}-\eta_{A 0}^{*}}{\left(r_{A}^{*}\right)^{2}} & 0 & \frac{\xi^{*}-\xi_{A 0}^{*}}{\left(r_{A}^{*}\right)^{2}} & 0
\end{array}\right] \\
c_{A a}=\left.\frac{\partial h}{\partial a_{A}}\right|^{\ast}=\left[\begin{array}{cc}
-\frac{\xi^{*}-\xi_{A 0}^{*}}{r_{A}^{*}} & -\frac{\eta^{*}-\eta_{A 0}^{*}}{r_{A}^{*}} & 0 \\
0 & 0 & 0 \\
0 & 0 & -1
\end{array}\right]
\end{gathered}
$$

where $x^{*}=\left(\xi^{*}, v_{\xi}^{*}, \eta^{*}, v_{\eta}^{*}\right), a_{A}^{*}=\left(\xi_{A 0}^{*}, \eta_{A 0}^{*}, \Psi_{A 0}^{*}\right)$, and $r_{A}^{*}=\sqrt{\left(\xi^{*}-\xi_{A 0}^{*}\right)^{2}+\left(\eta^{*}-\eta_{A 0}^{*}\right)^{2}}$.

Similarly, $h_{B}, C_{B x}$, and $c_{B a}$ of the sensor B can be derived.

Let the measurement vector $o$ be denoted as

$$
o=\overbrace{\left(r_{A}, \hat{r}_{A}, \theta_{A}\right.}^{\hat{r}_{A}, \hat{r}_{B}, \hat{r}_{B}, \theta_{B}})^{n_{B}}
$$

The matrix coefficients $C_{x}$ and $C_{a}$ of the measurement equation in (6) for the scenario illustrated in Fig. 4 can then be expressed as:

$$
\begin{gathered}
C_{x}=\left[\begin{array}{l}
C_{A x} \\
C_{B x}
\end{array}\right] \\
C_{a}=\left[\begin{array}{cc}
c_{A a} & 0 \\
0 & c_{B a}
\end{array}\right]
\end{gathered}
$$

Assuming the system dynamics can be modeled with a constant velocity (CV) model, $\Phi_{x}, G_{x}, u_{2}$ in (16) can be written as

$$
\begin{gathered}
\Phi_{x}=\left[\begin{array}{ccc}
1 & \Delta T & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & \Delta T \\
0 & 0 & 0 & 1
\end{array}\right] \\
G_{x}=I_{4} \quad u_{2}=0
\end{gathered}
$$


[^0]:    ${ }^{7} R^{c}=\operatorname{diag}(\epsilon I, \ldots, \epsilon I)$ and $z^{c}=[0, \ldots, 0]^{T}$ where $\epsilon$ denotes a small positive number.

Process noise $w$ in (16) is denoted by the information array $\left[R_{w}, z_{w}\right]$, expressed as $z_{w}=0$ and

$$
R_{w}=\left[\begin{array}{cc}
q_{\xi} W & 0 \\
0 & q_{\eta} W
\end{array}\right]
$$

where $W=\left[\begin{array}{ccc}
\sqrt{\frac{\Delta T^{2}}{3}} & \sqrt{\frac{\eta \frac{\Delta T}{4}}{3}} & \\
0 & \sqrt{\frac{\Delta T}{4}} & &
\end{array}\right] ; q_{\xi}$ and $q_{\eta}$ are random walking parameters for $\xi$-coordinate and $\eta$-coordinate, respectively.

## IV. SIMULATION

As shown in Fig. 4, the simulation results presented here are based on two sensors simulated near the front bumper. Sensor A is located at $\left(\xi_{A 0}=2, \eta_{A 0}=0.6\right)$, oriented $10^{\circ}$ $\left(\Psi_{A 0}=10^{\circ}\right)$ outwards from the vehicle's bore-sight ( $\xi$ coordinate). Sensor B is located at $\left(\xi_{B 0}=2, \eta_{B 0}=-0.6\right)$, oriented $10^{\circ}\left(\Psi_{B 0}=-10^{\circ}\right)$ outwards from the vehicle's bore-sight. The random walking parameters in (30) are expressed as $q_{\xi}=0.1$ and $q_{\eta}=0.1$. The measurement noise variance $\left(\sigma_{r}, \sigma_{r r}, \sigma_{\theta}\right)$ is set to $\left(0.1,0.2,1^{\circ}\right)$. Three algorithms are implemented: SEP, UKF, and FMAP. SEP [24] treats the tracking and registration problems separately; but the UKF and FMAP algorithms address the problems jointly. Each algorithm has been implemented in Matlab on a 2 GHz Intel Core 2 Duo processor running Window XP. No special care has been taken to produce efficient code.

In the first simulation, ten targets are randomly generated in the field-of-view of the sensors over a period of about 50 seconds. We initially set the registration parameters of the sensors randomly with small numbers. Tracks are initialized using the zero-mean noninformative distributions. Fig. 5 shows the trajectories of unregistered measurements and an tracked target vs. ground truth. The red solid line represents the true trajectory of the target while the other blue solid, green dash-dotted, and dashed lines represent the fused results of the SEP, UKF, and FMAP algorithms, respectively. Fig. 6 show the mean errors ${ }^{8}$ of position and velocity estimates of the target for the three algorithms, respectively. The bar plot in Fig. 7 shows the mean errors of the registration estimates for the three algorithms. The performance difference between UKF and FMAP are too small to seen on the scale used in the Figures. Note that in all the cases the performance of FMAP and UKF is clearly superior to that of SEP. This confirms the asymptotical optimality of JTR algorithm versus the decoupled approaches (e.g., SEP algorithm).

In the next simulation, we investigate the time complexity of the SEP, UKF, and FMAP algorithms by varying the

[^0]number of simulated targets from 10 to 300. Fig. 8 plots the execution time curves for the three algorithms at the different input sizes. The figure clearly illustrates the factor that the time complexities of FMAP and SEP are similar and are both an order of magnitude lower than that of UKF. This confirms the superior time-efficiency of FMAP vis-a-vis that of UKF.
![img-3.jpeg](img-3.jpeg)

Fig. 5. Top-down view of the trajectories of registered (left) and unregistered (right) sensor measurements of an tracked target vs. ground truth, respectively
![img-4.jpeg](img-4.jpeg)

Fig. 6. Mean errors of estimated longitudinal and lateral positions $\left(e_{\xi}\right.$ and $\left.e_{\eta}\right)$ and the corresponding velocities $\left(e_{\xi}, e_{\hat{\eta}}\right)$ for a tracked target.

The last simulation investigates how FMAP responses in the step change of registration. For example, in Fig. 9 the orientation of Sensor B $\left(\Psi_{B 0}\right)$ steps from $-10^{\circ}$ to $-5^{\circ}$ at Second 25 (see the third plots from the top), namely, the sensor rotates counterclockwise $5^{\circ}$ that may be caused by an external collision impact. As in the first simulation, ten targets


[^0]:    ${ }^{8}$ The mean error is defined as $e_{x}=E\left\{\left|x-x_{T}\right|\right\}$ with $x$ and $x_{T}$ the measurement and ground truth, respectively. Giving a series of measurement and truth pairs $\left(x_{i}, x_{T i}\right), 1 \leq i \leq N$, the sample mean error is computed as $e_{x}=\frac{\sum_{i}^{N}\left|e_{i}-x_{T i}\right|}{N}$.

![img-5.jpeg](img-5.jpeg)

Fig. 7. Mean errors of sensor registration estimates for Sensor B.
![img-6.jpeg](img-6.jpeg)

Fig. 8. Execution time
are randomly generated for the 50 -second simulation. The innovation error curve has two peaks caused by two different cases: unknown registration at Second 0 and step change of registration at Second 25, respectively. As shown in Fig. 9, the registration estimates converge to their corresponding ground truth within 5 seconds for both cases.

## V. VEHICULAR EXPERIMENT

A test vehicle (Fig. 10 (a)) equipped with two SICK LMS291 rangefinders is used as the test-bed to verify the effectiveness of the proposed FMAP. The two rangefinders are mounted at two corners of the front bumper. The positions and orientations of the rangefinders are precisely surveyed. The left rangefinder (Sensor A) is located at $\left(\xi_{A 0}=3.724, \eta_{A 0}=0.883\right)$, oriented $45^{\circ}\left(\Psi_{A 0}=45^{\circ}\right)$ outwards from the vehicle's bore-sight ( $\xi$-coordinate). The right rangefinder (Sensor B) is located at $\left(\xi_{B 0}=3.720, \eta_{B 0}=\right.$ $-0.874)$, oriented $45^{\circ}\left(\Psi_{B 0}=-45^{\circ}\right)$ outwards from the
![img-7.jpeg](img-7.jpeg)

Fig. 9. The response under step change of sensor registration. The top three plots are for the estimates of the registration parameters $\xi_{B 0}, \eta_{B 0}$, and $\Psi_{B 0}$ vs. ground truth. The bottom plot is the innovation error.
vehicle's bore-sight. The vehicle is also equipped with wheel encoders and an IMU sensor for determining the motion control inputs.

The rangefinder scans from right to left in its $180^{\circ}$ field-of-view at a resolution of $0.5^{\circ}$ and generates 361 distance measurements to the closest line-of-sight obstacles. Each rangefinder is equipped with a point-object detector (e.g., tree trunks, light poles, and etc.) that selects scan clusters such that 1) the size of the cluster is less than 0.5 meter, and 2) the distance to the nearest point of other clusters is larger than 5 meters. The speed (i.e., range rate) of a point object is inferred from the host vehicle motion because of the stationary assumption of the point objects.

The experiment ${ }^{9}$ was conducted in a parking lot with plenty road-side point objects shown in Fig. 10 (b). The vehicle was manually driven, and an observation sequence of about 50 seconds was collected. The plot (c) shows a snapshot of unregistered range data for the scene in Fig. 10 (b). The black dots and magenta circles in the plot denote the scan data generated by the left and right rangefinders, respectively. The blue circles and red stars denote the detected point objects from the left and right rangefinders, respectively.

The measurement inconsistence caused by the registration bias is clearly seen. For example, the contours of the vehicle and the point objects in (b) from the sensors is not aligned. The inconsistence raises an issue for data association. Without a consistent registration, data from one sensor cannot be correctly associated with that from a different sensor. For comparison, the snapshot of the registered range data of the same scene using FMAP algorithm is shown in Fig. 10 (d).

[^0]
[^0]:    ${ }^{9}$ The demo source code can be downloaded from http://code.google.com/p/joint-calibration-tracking/ along with the data set.

The additional black diamonds in (d) denote the fused targets. This plot clearly reveals the fact that FMAP significantly improves the sensor registration and thus the data association among multiple sensors.

In each discrete time instant, the detected objects from both sensors are matched with the tracked targets (drawn as black diamonds in Fig. 10 (d)) at previous instant using a nearest-neighbor and a maximum distance gating data association strategy. We then apply the FMAP filter to jointly track the associated track-object pairs and registration parameters. Note that no target is visible in the whole observation sequence. As shown in the last plot in Fig. 11, the dimension of the state vector $s$ changes due to new targets coming into or existing targets leaving the field-of-view of the sensors. The method described in Section II-G is used to handle the change.

In the experiment, the right rangefinder’s registration is unknown and initially set to $\left(\xi_{B 0}=2.720,\eta_{B 0}=\right.$ $\left.-0.126, \Psi_{B 0}=-40^{\circ}\right)$. The SEP and FMAP algorithms are applied to the data set. The resulted registration error curves for both algorithms versus the surveyed values are shown in Fig. 11(a). The blue solid lines and the magenta dashed lines denote the error curves of SEP and FMAP, respectively. FMAP clearly exhibits superior performance comparing with that of SEP. A shown in Fig. 11(a), the estimates of the sensor’s position $\left(\xi_{B 0}, \eta_{B 0}\right)$ and orientation $\Psi_{B 0}$ converge to their true values in about 5 seconds, respectively. The slight transitory oscillation near the start of the run is partially due to the vehicle’s steering maneuver and lack of shared detected objects from both sensors. Selecting a suitable model for the target motion requires giving consideration to the tradeoff between the filter accuracy and the model complexity. Better results can be obtained by incorporating vehicular motion model and global target map building. This may increase the computational complexity of the algorithm. The fourth plot in 11(a) shows the number targets tracked by FMAP.

On the other hand, the significant mean registration error by the SEP algorithm can be observed in Fig. 11(b). We should note that the divergence of SEP curves increases over time in Fig. 11(a), and this is partially contributed by the erroneous data association caused by registration biases of previous cycles. Therefore, the estimates of registration by FMAP is more consistent and robust than that by SEP.

## VI. SUMMARY AND CONCLUSION

In this article, we have addressed the recursive JTR. The FMAP algorithm is derived in which the time complexity scales linearly with the numbers of measurements and targets. It is proved that FMAP is asymptotically optimal and has an $O(n)$ implementation based on matrix orthogonal factorization. The results from experiments on synthetic and vehicular data demonstrate that, as expected, FMAP consistently
![img-8.jpeg](img-8.jpeg)

Fig. 10. (a) The test-bed vehicle equipped with two rangefinders. (b) The snapshot of a scene in the parking lot. (c) The top-down view of unregistered range data of the scene in (b). (d) The top-down view of registered range data of the scene in (b).
performs better than the methods where tracking and registration are separately treated. It has been also demonstrated experimentally using the synthetic data that the complexity of FMAP is indeed $O(n)$. Although FMAP and UKF are quite equivalent in performance but the time complexity of

![img-9.jpeg](img-9.jpeg)

Fig. 11. (a) The error curves of sensor registration estimates ( $\xi_{B 0}$, $\eta_{B 0}$ and $\Psi_{B 0}$ ) for the right rangefinder when the true value is initially unknown. The last plot shows the number of detected objects varies with time. (b) The corresponding mean errors for the registration estimates.

FMAP is a magnitude lower than that of UKF. Additionally, results of simulation and vehicle experiment demonstrate that FMAP can handle the dynamics of sensor registration and a variable number of targets.

## APPENDIX A

Lemma 6.1: Let $\rho \sim \mathcal{N}\left(\mu_{\rho}, \Sigma_{\rho}\right)$ or in information array terms, $\left[R_{\rho}, z_{\rho}\right]$. If $\omega=\alpha \rho+\beta, \omega \sim \mathcal{N}\left(\alpha \mu_{\rho}+\beta, \alpha \Sigma_{\rho} \alpha^{t}\right)$, or in information array terms, $\omega$ can be represented through $\left[R_{\omega}, z_{\omega}\right]$, where $R_{\omega}=R_{\rho} \alpha^{-1}$ and $z_{\omega}=z_{\rho}+R_{\omega} \beta$.

Proof: Since $\mu_{\rho}=R_{\rho}^{-1} z_{\rho}$ and $\Sigma_{\rho}=R_{\rho}^{-1} R_{\rho}^{-t}$, we get

$$
\mu_{\omega}=R_{\omega}^{-1} z_{\omega}=\alpha \mu_{\rho}+\beta
$$

and

$$
\Sigma_{\omega}=R_{\omega}^{-1} R_{\omega}^{-t}=\alpha \Sigma_{\rho} \alpha^{t}=\alpha R_{\rho}^{-1} R_{\rho}^{-t} \alpha^{t}
$$

One can verify that $R_{\omega}=R_{\rho} \alpha^{-1}$ and

$$
\begin{aligned}
z_{\omega} & =R_{\omega} \mu_{\omega}=R_{\omega}\left(\alpha \mu_{\rho}+\beta\right)=R_{\omega}\left(\alpha R_{\rho}^{-1} z_{\rho}+\beta\right) \\
& =R_{\rho} \alpha^{-1}\left(\alpha R_{\rho}^{-1} z_{\rho}+\beta\right) \\
& =\left(R_{\rho} \alpha^{-1}\right)\left(\alpha R_{\rho}^{-1}\right) z_{\rho}+\left(R_{\rho} \alpha^{-1}\right) \beta \\
& =z_{\rho}+\left(R_{\rho} \alpha^{-1}\right) \beta \\
& =z_{\rho}+R_{\omega} \beta
\end{aligned}
$$

Lemma 6.2: Let the system dynamics be defined in (16); the density function of the state variable $s(t)=[x, a]$ be expressed as information array in (14); and random noise term $w$ be in information array form $\left[R_{w}, z_{w}\right]$. Let $\rho \equiv[w, s(t)]^{t}$. If $w$ and $s(t)$ are statistically independent, the joint density of $\omega \equiv[w, x(t+1), a(t+1)]^{t}$ can be represented through the information array $\left[R_{\omega}, z_{\omega}\right]$, where

$$
R_{\omega}=\left[\begin{array}{ccc}
R_{w} & 0 & 0 \\
-\hat{R}_{x} \Phi_{x}^{-1} G_{x} & \hat{R}_{x} \Phi_{x}^{-1} & \hat{R}_{x a} \\
0 & 0 & \hat{R}_{a}
\end{array}\right]
$$

and

$$
z_{\omega}=\left[\begin{array}{c}
z_{w} \\
\hat{z}_{x}+\hat{R}_{x} \Phi_{x}^{-1} u_{2} \\
\hat{z}_{a}
\end{array}\right]
$$

Proof: Since $w$ and $s(t)$ are statistically independent, the information array of the joint vector $\rho=$ $[w, s(t)]^{t}=[w, x, a]^{t}$ is represented as $\left[R_{\rho}, z_{\rho}\right]$ where $R_{\rho}=\left[\begin{array}{ccc}R_{w} & 0 & 0 \\ 0 & \hat{R}_{x} & \hat{R}_{x a} \\ 0 & 0 & \hat{R}_{a}\end{array}\right]$ and $z_{\rho}=\left[\begin{array}{lll}z_{w} & \hat{z}_{x} & \hat{z}_{a}\end{array}\right]^{t}$
One verifies that the system dynamics equation (16) can be reorganized as

$$
\omega=\alpha \rho+\beta
$$

with $\alpha=\left[\begin{array}{ccc}I & 0 & 0 \\ G_{x} & \Phi_{x} & 0 \\ 0 & 0 & I\end{array}\right]$ and $\beta=\left[\begin{array}{c}0 \\ u_{2} \\ 0\end{array}\right]$, and $\alpha^{-1}=$ $\left[\begin{array}{ccc}I & 0 & 0 \\ -\Phi_{x}^{-1} G_{x} & \Phi_{x}^{-1} & 0 \\ 0 & 0 & I\end{array}\right]$.

Using Lemma 6.1, we obtain the

$$
R_{\omega}=R_{\rho} \alpha^{-1}=\left[\begin{array}{ccc}
R_{w} & 0 & 0 \\
-\hat{R}_{x} \Phi_{x}^{-1} G_{x} & \hat{R}_{x} \Phi_{x}^{-1} & \hat{R}_{x a} \\
0 & 0 & \hat{R}_{a}
\end{array}\right]
$$

and

$$
z_{\omega}=z_{\rho}+\left(R_{\rho} \alpha^{-1}\right) \beta=\left[\begin{array}{c}
z_{w} \\
\hat{z}_{x}+\hat{R}_{x} \Phi_{x}^{-1} u_{2} \\
\hat{z}_{a}
\end{array}\right]
$$

Lemma 6.3: Let $\rho=\left[\begin{array}{c}\rho_{1} \\ \rho_{2}\end{array}\right]$ be distributed as $\rho \sim$ $\mathcal{N}\left(\mu_{\rho}, \Sigma_{\rho}\right)$ or information array $\left[R_{\rho}, z_{\rho}\right]$ with $R_{\rho}=$ $\left[\begin{array}{cc}R_{\rho_{11}} & R_{\rho_{12}} \\ 0 & R_{\rho_{22}}\end{array}\right]$ and $z=\left[\begin{array}{c}z_{\rho_{1}} \\ z_{\rho_{2}}\end{array}\right]$. Then the marginal distribution of $\rho_{2}$ is normal and has $\rho_{2} \sim\left[R_{\rho_{22}}, z_{\rho_{2}}\right]$.

Proof: $R_{\rho}^{-1}=\left[\begin{array}{cc}R_{\rho_{11}}^{-1} & -R_{\rho_{12}}^{-1} R_{\rho_{12}}^{-1} R_{\rho_{22}}^{-1} \\ 0 & R_{\rho_{22}}^{-1}\end{array}\right]$. Thus the mean

$$
\begin{aligned}
\mu_{\rho} & =R_{\rho}^{-1} z_{\rho} \\
& =\left[\begin{array}{cc}
R_{\rho_{11}}^{-1} & -R_{\rho_{12}}^{-1} R_{\rho_{12}} R_{\rho_{22}}^{-1} \\
0 & R_{\rho_{22}}^{-1}
\end{array}\right]\left[\begin{array}{c}
z_{1} \\
z_{2}
\end{array}\right] \\
& =\left[\begin{array}{cc}
R_{\rho_{11}}^{-1} z_{\rho_{1}} & -R_{\rho_{12}}^{-1} R_{\rho_{12}} R_{\rho_{22}}^{-1} z_{2} \\
R_{\rho_{22}}^{-1} z_{\rho_{2}}
\end{array}\right]
\end{aligned}
$$

The marginal distribution of $\rho_{2} \sim \mathcal{N}\left(\mu_{\rho_{2}}, \Sigma_{\rho_{2}}\right)$ with $\mu_{\rho_{2}}=$ $R_{\rho_{22}}^{-1} z_{\rho_{2}}$ and $\Sigma_{\rho_{2}}=R_{\rho_{22}}^{-1} R_{\rho_{22}}^{-1}$. Therefore $\rho_{2} \sim\left[R_{\rho_{22}}, z_{\rho_{2}}\right]$.