![img-0.jpeg](img-0.jpeg)

# On the Generalized Belief Propagation and Its Dynamics 

Jean-Christophe Sibel, Sylvain Reynal

## To cite this version:

Jean-Christophe Sibel, Sylvain Reynal. On the Generalized Belief Propagation and Its Dynamics. International Conference on Control, Automation and Information Sciences., Nov 2012, Vietnam. pp.4. hal-00766753

## HAL Id: hal-00766753 <br> https://hal.science/hal-00766753v1

Submitted on 19 Dec 2012

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# On the Generalized Belief Propagation and its Dynamics 

Jean-Christophe Sibel and Sylvain Reynal


#### Abstract

Numerous inference problems in statistical physics, computer vision or error-correcting coding theory consist in approximating the marginal probability distributions on Markov Random Fields (MRF). The Belief Propagation (BP) is an accurate solution that is optimal if the MRF is loop free and suboptimal otherwise. In the context of error-correcting coding theory, any Low-Density Parity-Check (LDPC) code has a graphical representation, the Tanner graph, which is a particular MRF. It is used as a media for the BP algortithm to correct the bits, damaged by a noisy channel, by estimating their probability distributions. Though loops and combination thereof in the Tanner graph prevent the BP from being optimal, especially harmful topological structures called the trappingsets. The BP has been extended to the Generalized Belief Propagation (GBP). This message-passing algorithm runs on a non unique mapping of the Tanner graph, namely the regiongraph, such that its nodes are gatherings of the Tanner graph nodes. Then it appears the possibility to decrease the loops effect, making the GBP more accurate than the BP.


In this article, we expose a novel region graph construction suited to the Tanner code, an LDPC code whose Tanner graph is entirely covered by trapping-sets. Furthermore, we investigate the dynamic behavior of the GBP compared with that of the BP to understand its evolution in terms of the Signal-to-Noise Ratio (SNR). To this end we make use of classical estimators and we introduce a new one called the hyperspheres method.

## I. INTRODUCTION

A well-known problematic of the Markov Random Fields (MRF) is to extract their marginal probability distributions. Such an inference problem has numerous applications in computer vision, neural networks, image processing, statistical physics and channel coding. In [1] has been proposed the Belief Propagation (BP), known to provide accurate estimates. In the realm of error-correcting coding theory, the BP is a decoding algorithm that helps to recover a sequence of bits sent through a noisy channel. To this end it is associated to Low-Density Parity-Check (LDPC) codes that apply artifical constraints between the bits, namely the parity-check equations. The bits joined with the parity-check equations form an MRF, called the Tanner graph, used as a media for the BP [2]. It is an accurate approximate inference algorithm knwown to provide low bit-error rates. However most LDPC codes have loop-like topologies, that leads the BP to wrong estimates, making this algorithm suboptimal [3]. In particular, the combination of short loops, as the trapping-sets [4], [5], are very harmful. To circumvent this phenomenon, we bring out that the BP is equivalent to the Bethe approximation [6]. This method is used in statistical physics to estimate statistical averages of thermodynamics quantities by neglecting - to some extent - correlations

[^0]between interacting spins. This technique suffers from the loop-like topology of the spin glasses. It has been generalized to the Kikuchi approximation, a technique that consists in gathering the interacting spins to absorb loops [6]. Transposed to the case of the LDPC codes, the resulting graph, called the region-graph, is a media for a new messagepassing algorithm, the Generalized Belief Propagation (GBP) that turns out to be more accurate than the BP provided that the region-graph has absorbed damageable structures. Along the whole paper, we focus on the Tanner code [7] whose main property is that it can be entirely described by a set of trapping-sets. Then the region-graph can be built by working on them.

To investigate deeper the comparison between BP and GBP we focus on their dynamics according to the Signal-toNoise Ratio (SNR). Studied from a theoretical point of view in [8], [9], the dynamics of the BP has also been investigated by experimental results in [10]. In this paper we carry out a work on experimental study, by the use of estimators as the bifurcation diagram and the Lyapunov exponent to raise the behavior of the BP and the GBP according to the SNR.

The second II deals with preliminaries about the LDPC codes and the BP. In the section III are exposed the regiongraph construction rules and the GBP. Then we detail our novel construction of the region-graph for the Tanner code. The section IV is dedicated to the exposure of dynamics estimators to better understand the GBP and to highlight its relevant properties.

## II. PRELIMINARIES

## A. LDPC Codes - Belief Propagation

We consider $N$ binary random variables $\mathbf{X}=$ $\left\{X_{1}, \ldots, X_{N}\right\}$ whose global state is $\mathbf{x}=\left[x_{1}, \ldots, x_{N}\right]$. Each variable represent a bit to transmit through a noisy channel. We use the lightened notation $\mathbf{x}=\left[x_{1}, \ldots, x_{N}\right]$ to denote variables and states. An LDPC code is represented by $M$ parity-check equations $\mathbf{C}=\left\{c_{1}, \ldots, c_{M}\right\}$ such that for each $j \in\{1, \ldots, M\}, c_{j}=\sum_{x_{i} \in \mathcal{N}_{j}} x_{i}$ where the sum is binary. $\mathcal{N}_{j} \subset \mathbf{x}$ is the neighborhood of $c_{j}$ defined by the LDPC code. We define similarly $\mathcal{N}_{i}$ the neighborhood of $x_{i}$ as the set $\left\{c_{j}\right\}_{j}$ such that $x_{i} \in \mathcal{N}_{j} . c_{j}$ and and $x_{i} \in \mathcal{N}_{j}$ form an edge $e_{i j}$ between two nodes, a variable node $x_{i}$ and a check node $c_{j}$, in a graph $G=\left(\mathbf{X} \cup \mathbf{C},\left\{e_{i j}\right\}_{i j}\right)$, called the Tanner graph (see Fig. 1).
$G$ is an MRF whose $\left\{b_{i}\left(x_{i}\right)\right\}_{1 \leq i \leq N}$ are the beliefs, i.e. the estimate of the marginal probability distributions. $\hat{\mathbf{x}}$ is the estimate of the input bits such that $\hat{x}_{i}=\arg \max _{x_{i}} b_{i}\left(x_{i}\right)$. The Tanner graph is used as a media for the propagation of messages to get $\hat{\mathbf{x}}$ from the BP. $\left\{m_{i j}^{(k)}\right\}_{i j}$ and $\left\{n_{j i}^{(k)}\right\}_{j i}$


[^0]:    This work was supported by the French ANR Defis program under contract ANR-08-EMER-003 (COCQ project).

are respectively the messages from the variable nodes to the check nodes, and the messages from the check nodes to the variable nodes at iteration $k$ whose equations are detailed in [1], [2] such that:

$$
\begin{aligned}
\forall e_{i j}, \quad m_{i j}^{(k)} & =f_{i j}\left(\left\{n_{y x}^{(k-1)}\right\}_{(x, y)}, l_{i}\right) \\
n_{j i}^{(k)} & =g_{j i}\left(\left\{m_{r q}^{(k)}\right\}_{(x, y)}\right)
\end{aligned}
$$

with $\left\{f_{i j}\right\}_{i j},\left\{g_{j i}\right\}_{j i}$ the implicit update equations and $\left\{l_{i}=p\left(y_{i} \mid x_{i}\right)\right\}_{i}$ the likelihoods computed from the observation variables $\left\{y_{1}, \ldots, y_{n}\right\}$. The messages $\left\{n_{j i}^{(k)}\right\}$ are then computed by an iterated map $Q=g \circ f$ such that:

$$
\forall e_{i j}, \quad n_{j i}^{(k)}=Q_{j i}\left(\left\{n_{n m}^{(k-1)}\right\}_{(m, n)},\left\{l_{i}\right\}_{i}\right)
$$

## III. The Generalized Belief Propagation

## A. The region-graph construction

The region-graph $\mathcal{R}$ is a directed graph of depth $D$ built level by level. We decompose this construction in two steps.

The first step is the construction of the first level $\mathcal{R}_{0}$. The principle is to gather the nodes of the Tanner graph in order to absorb some harmful topological structures, as loops or combinations thereof. These gatherings, called regions, are nodes of $\mathcal{R}_{0}$ if and only if each check node $c_{j}$ with $\mathcal{N}_{j}$ is included in at least one of these regions. The second step is the construction of the next levels $\mathcal{R}_{1}, \ldots, \mathcal{R}_{D-1}$. A level $\mathcal{R}_{l}$ is constructed by searching for the intersections between the regions of the previous level $\mathcal{R}_{l-1}$. We respectively define $\mathbf{C}_{r}$ and $\mathbf{X}_{r}$ the sets of check nodes and variable nodes of the region $r$. A set $r=\mathbf{X}_{r} \cup \mathbf{C}_{r}$ is a region of $\mathcal{R}_{l}$ if and only if there is $n \geq 2$ regions $\left\{r_{1}, \ldots, r_{n}\right\} \in \mathcal{R}_{l-1}^{n}$ such that:

- $\forall c_{j} \in \mathbf{C}_{r}, \forall r_{k} \in\left\{r_{1}, \ldots, r_{n}\right\}, c_{j} \in \mathbf{C}_{k}$,
- $\forall x_{i} \in \mathbf{X}_{r}, \forall r_{k} \in\left\{r_{1}, \ldots, r_{n}\right\}, x_{i} \in \mathbf{X}_{k}$.

A region-graph of the Hamming code presented previously is displayed on Fig.2. The used method [6] consists in including only one check node and its neighborhood per region in $\mathcal{R}_{0}$.

The GBP performance are dependent on the region-graph, and particularly on the regions of $\mathcal{R}_{0}$. The difficulty is to
![img-1.jpeg](img-1.jpeg)

Fig. 1. Tanner graph of the Hamming code
![img-2.jpeg](img-2.jpeg)

Fig. 2. A region-graph of the Hamming code
find a construction that both implies relevant performance of the GBP and fair complexity. In the previous example, the construction is easy to implement and the complexity is low enough but there is no link with the Tanner graph toppology, preventing the GBP from obtaining relevant performance.

## B. The message-passing algorithm

The region-graph is a Bayesian network whose probability distribution is estimated by the GBP. As in the BP case, the principle is to convey messages on the edges of the regiongraph where a message $m_{r q}^{(k)}$ from a region $r$ to a region $q$ is the a posteriori probability distribution of the region $q$ given by the region $r$ at iteration $k$. We compute messages only between connected regions, i.e. $m_{r q}^{(k)}$ is considered if and only if $(r \rightarrow q)$ is a directed edge of the region-graph, we say that $q$ is one of the children $\mathcal{C}_{r}$ of $r$. An iteration of the algorithm consists in the computation of all the messages $\left\{m_{r q}^{(k)}\right\}_{r, q}$ whose equations are detailed in [6], [11]. Here we only give the implicit equation:
$\forall(r, q) \in \mathcal{R}^{2}$ s.t. $q \subset \mathcal{C}_{r}, m_{r q}^{(k)}=F_{r q}\left(\left\{m_{p s}^{(k-1)}\right\}_{p, s},\left\{l_{i}\right\}_{i}\right)$
In [6] is highlighted that the GBP suffers from a poor convergence. To circumvent this phenomenon is included a uniform weighting:

$$
m_{r q}^{(k)}=\frac{1}{2} F_{r q}+\frac{1}{2} m_{r q}^{(k-1)}
$$

## C. A novel construction

We present here a particular construction of the regiongraph for the Tanner code [7] of length $N=155$ with $M=$ 93 parity-check equations. Its Tanner graph is a sophisticated concatenation of topological structures called Trapping-Sets (TS). A TS $(a, b)$, introduced in [4] and studied in [5] among other, is a Tanner graph which contains $a$ variable nodes and $b$ unsatisfied parity-check equations. Here the TS $(5,3)$ (see Fig.3) are sufficient to cover the whole Tanner graph. Such a structure is known to damage the decoding [5] because only the total null state enables to verify all the parity-check equations. Thus to build the first level $\mathcal{R}_{0}$ of the regiongraph, it would be relevant to absorb them into regions. However, the complexity of the message-passing would soar because these regions are too large. Therefore, we had better break these structures into several smaller regions as on Fig. 4 with:

- $r=\left\{\mathbf{X}_{r}=\left\{x_{0}, x_{1}, x_{3}\right\}, \mathbf{C}_{r}=\left\{c_{0}, c_{2}, c_{6}\right\}\right\}$
![img-3.jpeg](img-3.jpeg)

Fig. 3. TS $(5,3): 5$ variables and 3 unsatisfied constraints

![img-4.jpeg](img-4.jpeg)

Fig. 4. Region-graph of the TS(5,3)

- \( p = \left\{ \mathbf{X}_p = \{x_1, x_2, x_3\}, \mathbf{C}_p = \{c_1, c_4, c_7\} \right\} \right\},
- \( q = \left\{ \mathbf{X}_q = \{x_1, x_3, x_4\}, \mathbf{C}_q = \{c_3, c_5, c_8\} \right\} \).

### *D. Results*

The region-graph of the TS(5,3) is loop free which makes the decoding optimal. When we apply this construction to all the TS(5,3) of the whole code, unfortunately we do not get a loop free region-graph because all the nodes belong to several TS(5,3). Nevertheless, the performance is still relevant to make the GBP a good candidate for the decoding.

We present on Fig.5 the BER in terms of the iteration of the GBP on the Tanner code for error events, made by the noisy channel, that are truly harmful for the Belief Propagation particularly because of the TS(5,3). On the Fig.5(b) we can see the BER of the BP which is oscillating, making the decoding divergent and wrong. On the same figure is displayed the BER of the GBP. It clearly appears that such an algorithm does not bring any improvement if we do not use the uniform weighting, noticing that it is often worse than the BP that highlights the true lack of convergence of the GBP update. When this factor is set to 0.5 then the BER is dramatically reduced.

### IV. DYNAMICS

In this section, we expose estimators to evaluate the dynamical behaviors of the GBP compared with the BP. To this end, we first define the mathematical environment in which these estimators are relevant.

#### *A. State space definition and properties*

To compare the dynamics of the BP and GBP, we need to define two state spaces that are similar. Using the fact that both are message-passing algorithms, we should consider the messages as the state variables. This choice fits perfectly with the convergence conditions written in the previous section for the GBP and written down here for the BP:

$$
\forall e_{ij}, \ n_{ji}^{(k)} = n_{ji}^{(k-1)}
$$

![img-5.jpeg](img-5.jpeg)

Fig. 5. BER of the BP and the GBP on the Tanner code with the suited region-graph construction

We consider respectively \( \{G_{ij}\}_{(i,j)} \) and \( \{F_{rq}\}_{(r,q)} \) as two sets of iterated maps on the state variables \( \{n_{ji}^{(k)}\}_{(i,j)} \) and \( \{m_{rq}^{(k)}\}_{(r,q)} \) which are called trajectories in the associated state spaces, denoted \( \mathcal{E}_{BP} \) and \( \mathcal{E}_{GBP} \), whose dimensions are the number of messages to compute at each iteration. We denote by \( U^{(k)} = \{n_{ji}^{(k)}\}_{(i,j)} \) and by \( V^{(k)} = \{m_{rq}^{(k)}\}_{(r,q)} \) the points of the trajectories of the BP and the GBP.

#### *B. Parameters and scaling*

In [10] the Signal to Noise Ratio (SNR) is used as a parameter in such a way that different values imply different dynamics of the BP. However, the most of their simulations are done for particular noise realizations scaled on the SNR, that prevents from evaluating a statistical behavior. A reason is that the noise realizations that lead the BP not to converge or to converge to a wrong estimate are rare events, essentially because the LDPC codes and the iterative algorithms are created to this end. A way to get statistical evaluations of the behavior of the BP and the GBP is the following:

1. Finding some of these noise realizations,
2. Storing the corresponding points \( \{T^{(0)} \} \) in the state space,
3. For each \( T^{(0)} \), averaging the estimators for a sufficient set of initializations whose points in the state space are close enough to \( T^{(0)} \) in the sense of the Euclidean distance.

By this way, we can target the guanine critical values of the SNR for which the algorithms blatantly change in their behaviors, i.e. for which the algorithm undergoes bifurcations. However, we have to be cautious because our simulations have shown that the state space is not uniform, i.e. the statistical evaluations are relevant for each \( T^{(0)} \) but averaging over them do not offer relevant statistics of the SNR critical values. This precision is crucial because it reveals that we do not work on the whole state space but only on subspaces of it where the systems, BP or GBP, do not behave trivially, that is to say we only deal with rare events. For all the estimators presented in the following of the paper, we use this method to get statistical results which are relevant enough to describe the behavior of the BP and the GBP.

#### *C. Bifurcation diagram*

A relevant method to extract the critical values of the SNR is the bifurcation diagram. For the explanation, we consider that we work on the BP. For a given noise realization, i.e. for a given \( T^{(0)} \) inside \( \mathcal{E}_{BP} \) it consists in evaluating the value of a description function \( E \) computed from the state variables at their steady state \( k = K \) for \( J \) different values of the SNR. Obviously, there is no reason that the dynamic system reaches any steady state at iteration \( K \) but we need to suppose it for computation time's sake. We get a sequence \( \mathbf{E} = [E_1, \ldots, E_J] \) that represents the behavior of the system in terms of the SNR. We consider the following function exposed in [10] called the mean square beliefs:

$$
\forall j \in \{1, \ldots, J\}, \quad E_j = \sqrt{\frac{1}{N} \sum_{i=0}^{N-1} b_i^2 (x_i)} \tag{7}
$$

![img-6.jpeg](img-6.jpeg)

Fig. 6. Bifurcation diagrams of the BP and the GBP

where the input sequence in the channel is [x1,...,xN] and the beliefs are computed at the last iteration K of the algorithm. The property of this function that we consider here is that E1 = 1 indicates that all the beliefs provide the input sequence equal to the input one, which is a successfull decoding. More generally, the amplitudes provides information about the decoding performance, and the variation between successive values gives us the critical values of the SNR.

We display on Fig.6 the mean bifurcation diagrams of the BP and the GBP for a given noise realization computed as we exposed in the previous subsection. We observe that for SNRs lower than 2.19 dB, the BP follows an increasing evolution. Such a behavior is analogous to that of the GBP except that the critical value is 2.07 dB. When the SNR is greater than these two critical values, the algorithms follow two distinct dynamics. The BP seems to oscillate while the SNR is lower than 2.49 dB, and for values in [2.5 dB, 2.98 dB] however it does not appear any known evolution which is an indication of chaos. Concerning the GBP, it appears globally three intervals: in [2.08 dB, 2.43 dB] the shape of E1 indicates irregular oscillations whereas for SNRs in [2.44 dB, 2.69 dB] we cannot assert anything meaning that the chaos would appear. From 2.70 dB up to 3.02 dB, the GBP tends to the right decoding state whereas the BP does not present this behavior before 2.99 dB. Moreover the shapes of the two whole signals indicate that the GBP is globally beyond the BP one, that shows that the GBP tends faster than the BP to the right state.

### *D. Reduced trajectory*

Another use of the mean square beliefs function is the representation of the trajectory in a 3-dimensional state space. To this end, we use the phase space reconstruction exposed in [12]. The method consists in computing E at each iteration to get the following sequence E1 = [Ej(k)]0≤k≤K. Afterthat we share this one dimensional sequence in a three dimensional sequence as follows:

$$
\tilde{\mathbf{E}}_j = \begin{bmatrix}
E_j(0) & E_j(1) & E_j(2) \\
\vdots & \vdots & \vdots \\
E_j(K-2) & E_j(K-1) & E_j(K)
\end{bmatrix} \tag{8}
$$

On Fig.7 and Fig.8 are displayed few reduced trajectories of the BP for SNR between the critical values computed previously. It appears for the BP four typical behaviors that match with the four intervals exposed in the previous paragraph. We obtain a very small sized attractor for SNR =

![img-7.jpeg](img-7.jpeg)

Fig. 7. Reduced trajectory for the BP on the Tanner code with SNR = 2.15 dB and 2.30 dB

2.10 dB, whereas the reduced trajectory transforms to a limit cycle when the SNR is between 2.19 dB and 2.49 dB. A crucial point is that the thickness of the trajectory along this limit cycle increases as the SNR is getting greater up to 2.50 dB. Actually the limit cycle interleaves with other limit cycles, that is as a sequence of period doubling bifurcations, as is displayed on the figure 9 with two interleft cycles. Such a phenomenon is a typical route to chaos [13], observable from 2.51 dB. A chaotic evolution means that there is not any periodic evolution or fixed point convergence anymore, as it is displayed for 2.70 dB. When the SNR reaches 2.99 dB the trajectory collapses to a single point that is a true fixed point.

Concerning the GBP, whose reduced trajectories are displayed on Fig.10 and Fig.11, we cannot split the SNR values so accurately because the reduced trajectory does not transform as blatantly as the BP one. However, it is possible to distinguish also four different behaviors that follow the same order than that of the BP: small attractor, limit cycle, chaos and fixed point. The corresponding SNR intervals match with what have been revealed previously.

We have to be cautious because E1 is not a true trajectory, it does not respect the Cauchy-Lipschitz condition [12] due to the non bijection between the messages and the beliefs. Thus, this sequence only has the role of giving clues about the true behavior of the considered algorithm as the possible shape of the actual trajectory in EBP or ELBP that are: convergence to a fixed point, convergence to a limit cycle and convergence to a chaotic attractor. To distinguish these shapes, we need a criterion that reflects the behavior by its own value. A good candidate is the Lyapunov exponent.

### *E. Lyapunov exponents*

A well-known estimator to describe the dynamics of any dynamic system is the Lyapunov exponent λ [14], [12], [15]. Its computation consists in evaluating at each iteration

![img-8.jpeg](img-8.jpeg)

Fig. 8. Reduced trajectory for the BP on the Tanner code with SNR = 2.70 dB and 3.00 dB

![img-9.jpeg](img-9.jpeg)

Fig. 9. Reduced trajectory for the BP on the Tanner code with SNR = 2.40 dB

k ≤ K the Euclidean distance d<sup>k</sup> between two initially close trajectories, and computing the log-ratio:

$$\lambda = \ln\frac{d_K}{d_0} \tag{9}$$

Numerous papers have brought out the link between the sign of λ and the behavior of the associated system.

Using the averaging method exposed previously, we compute λ for the same noise realization as in the previous subsections. We display it on Fig. 12. For SNRs lower than 2.19 dB, λ is closed to 0, that means that the trajectories neither move away one from the other nor get closer, there is no chaos but not fixed point either. The reduced trajectory indicated in that sense that this corresponded to a very small sized attractor. Then, λ crosses the x-axis, that is the sign of a bifurcation [12], and it goes higher to a constant while the SNR does not go over 2.49dB, that corresponds to the limit cycle interval: the trajectories turn around. Once the SNR exceeds this value, after a x-axis crossing indicating a new bifurcation, λ soars which is a sign of chaos, confirmed by the reduced trajectory displayed previously at 2.70dB. It means that the trajectories are close at the beginning but they quickly change behavior and they move away one from the other. From 3.1dB λ falls to negative values. It means that the trajectories get closer to the same fixed point, it is stable. Concerning the GBP, λ can provide pieces of information as the first critical values of the SNR, 2.08dB, that is to say the SNR for which the algorithm becomes unstable. From 2.08dB to 2.43dB, λ is getting greater, that corresponds to the irregular oscillations given by the bifurcation diagram. We observe a peak at 2.44dB, that matches with the beginning of the transient chaos illustrated by the reduced trajectory. The last critical values that we can read is 3.02 dB where the GBP tends to the right decoding state according to the bifurcation diagram.

## *F. Hyperspheres method*

We see that it is not trivial to extract information about the stability of the GBP due to its particular update equations. So

![img-10.jpeg](img-10.jpeg)

Fig. 10. Reduced trajectory for the GBP on the Tanner code with SNR = 2.00 dB and 2.20 dB

![img-11.jpeg](img-11.jpeg)

Fig. 11. Reduced trajectory for the GBP on the Tanner code with SNR = 2.80 dB and 3.00 dB

it seems necessary to include other tools to the investigation to raise more relevant conclusions.

We propose here a novel method to evaluate the unstability of the BP and the GBP, based on their own trajectory in E<sup>BP</sup> and E<sub>GBP</sub>. This method is complementary to the Lyapunov exponent because it reveals the size of the attractor that the trajectory falls into and other properties about the attractors.

This method consists in computing the radius R<sup>k</sup> of the hypersphere circumscribed to the trajectory inside a given temporal window centered around a point U(k) (or V(k)) of the trajectory. By dragging the window, we obtain a sequence of radii. On Fig. 13 are displayed for the BP the parallel evolutions of two radii that correspond to two initially close trajectories in the Euclidean sense. We only display for SNR that correspond to chaos i.e. for SNR greater than 2.49 dB. For SNR in [2.19dB, 2.49dB] simulations show that both radii oscillate at the same frequency of 23 iterations. For lower SNR the radii do not change a lot, their values are close to O that correspond to the small sized attractor exposed by the reduced trajectory. At 2.70 dB, on Fig. 13, the radii moved away one from the other as it was predicted by the Lyapunov exponent observations. More accurately we can see that the radii have different oscillation steps. This is due to the period doubling bifurcations explained previously.

![img-12.jpeg](img-12.jpeg)

Fig. 12. Lyapunov exponents of the BP and GBP on the Tanner scaled on the SNR

![img-13.jpeg](img-13.jpeg)

Fig. 13. Evolution of two hyperspheres radii of two initially close trajectories of the BP on the Tanner code at SNR = 2.70 dB, SNR = 3.00 dB

![img-14.jpeg](img-14.jpeg)

Fig. 14. Evolution of two hyperspheres radii of two initially close trajectories of the GBP on the Tanner code at SNR = 2.70 dB, SNR = 3.00 dB

During 92 iterations in average over numerous trajectories, for k ≤ 500, the trajectories are trapped in limit cycles of period 23 iterations, for the next 92 iterations they fall into other limit cycles of different radii but same period. For k ≥ 500 we observe a sequence of period doublings that lead to the chaos. Such an observation makes our method relevant to bring out crucial information by a one dimensional function. Another important aspect of the hyperspheres method is the raising of the behavior differences between two initially close trajectories: we easily observe that the evolution of the radii cannot be distinguished while k ≤ 200 but as k is getting greater, the evolution of the radii differentiate even though they follow the same kind of dynamics. For both of them the hypervolumes of the state space in which they are locking in, that is the hypervolumes circumscribed to the attractors, are quite of the same size. When the SNR reaches the last critical value we observe that one of the radii decreases to the null value because the BP has converged to a fixed point. The other radius has not collapsed yet because the SNR is just at the critical value, if it was increased a little we would see the two radii going to zero. Concerning the GBP, for low SNR values we did not display the evolutions of R<sup>k</sup> because it follows quiet the same dynamics as that of the BP. On Fig.14, at SNR = 2.70 dB we observe that the radii of the trajectories are quite smaller than that of the BP. Furthermore, the maximum value of the radius is still lower than the minimum value of the BP radius. The comparison between both radii on the GBP makes us deduce that even though each trajectory eventually reaches a particular attractor of the state space, their size are not very different and they collapse at the end. Because this is not the case about the BP, the GBP appears more stable than the BP for the suited construction we have proposed.

## V. CONCLUSION

In this paper, we have presented a novel method of construction of the region-graph for the GBP algorithm based on the topology of the Tanner graph. The results have shown that the error correction power was improved compared with the BP one. Furthermore it appears that the GBP was more stable than the BP. To uphold this assertion, we have used classical estimators of the dynamics. The results provided four different dynamics of that depends on the SNR values. To get more details about the dynamics of the GBP that turned out to be non-trivial compared with that of the BP, we introduce a new estimator, the radius evolution of the circumscribed hypersphere. The results highlighted that the GBP converges towards small sized attractors contrary to the BP, even for transient chaos. Finally, this work leads to conclude that a suited region-graph construction provides a good candidate to surpass the famous BP. Furthermore, the construction we propose for the Tanner code can be adapted to any other LDPC code provided that it is covered by a set of TS(o, b). In future works, we propose to find a mathematical criterion to evaluate the relevancy of any region-graph according to the associated GBP performance. Also we propose other handlings of the TS(5, 3) to build region-graphs that could present better correction power and improved stability.
