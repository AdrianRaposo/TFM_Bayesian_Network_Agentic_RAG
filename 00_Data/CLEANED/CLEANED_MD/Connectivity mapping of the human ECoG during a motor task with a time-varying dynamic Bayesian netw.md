# NIH Public Access 

## Author Manuscript

Conf Proc IEEE Eng Med Biol Soc. Author manuscript; available in PMC 2014 May 15.
Published in final edited form as:
Conf Proc IEEE Eng Med Biol Soc. 2010 ; 2010: 130-133. doi:10.1109/IEMBS.2010.5627179.

## Connectivity Mapping of the Human ECoG During a Motor Task with a Time-Varying Dynamic Bayesian Network

Huaijian Zhang*,<br>the Qiushi Academy for Advanced Studies, Zhejiang University, Hangzhou, China

## Heather L. Benz ${ }^{*}$,

the Department of Biomedical Engineering, Johns Hopkins University, Baltimore, MD 21205 USA; phone: 443-424-2369

## Anastasios Bezerianos [Senior Member IEEE],

the Department of Medical Physics, University of Patras, Patras, Greece

## Soumyadipta Acharya,

the Department of Biomedical Engineering, Johns Hopkins University, Baltimore, MD 21205 USA

## Nathan E. Crone,

the Department of Neurology, Johns Hopkins University, Baltimore, MD 21205 USA

## Anil Maybhate,

the Department of Biomedical Engineering, Johns Hopkins University, Baltimore, MD 21205 USA

## Xiaoxiang Zheng, and

the Qiushi Academy for Advanced Studies, Zhejiang University, Hangzhou, China

## Nitish V. Thakor [Fellow, IEEE]

the Department of Biomedical Engineering, Johns Hopkins University, Baltimore, MD 21205 USA
Huaijian Zhang: alexwillzhj@hotmail.com; Heather L. Benz: benz@jhu.edu; Anastasios Bezerianos: bezer@upatras.gr; Soumyadipta Acharya: acharya@jhu.edu; Nathan E. Crone: ncrone@jhmi.edu; Anil Maybhate: anil@jhmi.edu; Xiaoxiang Zheng: zxx@mail.bme.zju.edu.cn; Nitish V. Thakor: nthakor@jhu.edu


#### Abstract

As a partially invasive and clinically obtained neural signal, the electrocorticogram (ECoG) provides a unique opportunity to study cortical processing in humans in vivo. Functional connectivity mapping based on the ECoG signal can provide insight into epileptogenic zones and putative cortical circuits. We describe the first application of time-varying dynamic Bayesian networks (TVDBN) to the ECoG signal for the identification and study of cortical circuits. Connectivity between motor areas as well as between sensory and motor areas preceding and during movement is described. We further apply the connectivity results of the TVDBN to a movement decoder, which achieves a correlation between actual and predicted hand movements of 0.68. This paper presents evidence that the connectivity information discovered with TVDBN is applicable to the design of an ECoG-based brainmachine interface.


[^0]
[^0]:    *These authors contributed equally to the work.

# I. Introduction 

Directional neural connectivity mapping with the electrocorticogram (ECoG) is a field of intense interest in functional brain mapping [1], [2] and the characterization of seizure dynamics [3]. Furthermore, ECoG-based brain computer interfaces have proven in recent years to benefit from ECoG's high bandwidth and high signal to noise ratio in comparison to EEG [4]-[6]. Measures of brain connectivity may provide information about the ECoG signal that can improve both the reliability of an ECoG-based brain machine interface (BMI) and the ability to achieve multiple degrees of freedom of control.

Connectivity mapping has traditionally employed the cross-correlation function or Fourier coherence, methods that are ideal when the signal to noise ratio is high [7], [8]. However, in the presence of noise and nonlinearity, as in the ECoG signal, these methods are less robust [9]. Furthermore, they may be used to identify coupling but contain little information about directionality.

Granger causality-based methods, including the directed transfer function (DTF) [1] and partial directed coherence [10]-[11], have become popular in directional connectivity. DTF has a number of variants. The direct DTF (dDTF) and the conditional Granger causality test distinguish between direct and cascade flows, and the short-time DTF (SDTF) is applicable to short time windows and rapidly changing signals [2], [12], [13], [14]. The dDTF and SDTF have been used in conjunction as the SdDTF [15].

Time-varying dynamic Bayesian networks (TVDBN) have recently been proposed as a novel way to model connectivity in non-stationary time series [16]. This approach is particularly applicable to the ECoG signal due to its ability to compensate for non-stationary data. It is also computationally efficient, making it an attractive solution for an ECoG-based BMI.

## II. Methods

## A. Data collection

A single epilepsy patient undergoing subdural ECoG monitoring in preparation for brain resection surgery gave informed consent to participate in a motor task. Experiments were performed under a protocol approved by the Institutional Review Board at Johns Hopkins University. During trials that lasted between approximately 1 and 5 minutes, the subject performed repeated palmar grasps, opening and closing all fingers on the hand contralateral to the implanted ECoG grid.

The ECoG signal was recorded with the clinical system sampled at 1000 Hz from 74 subdural electrodes on the right hemisphere, shown in Fig.1. The electrodes covered sensorimotor areas as identified by an expert neurologist and electrical stimulation mapping (ESM).

Joint angle data were simultaneously recorded at 25 Hz from a data glove (CyberGlove Systems) worn on the left hand. The data glove reported angles of metacarpal phalangeal,

interphalangeal, and distal phalangeal joints of all five fingers, as well as finger abduction and adduction.

The ECoG data was filtered by a second-order Butterworth filter with a passband of $0.15-300 \mathrm{~Hz}$, with a notch filter at multiples of 60 Hz . It was then re-referenced using a common average reference (CAR) filter [17]:

$$
X(t)_{n}^{C A R}=X(t)_{n}-\langle X(t)\rangle
$$

where $X(t)$ is the time-domain ECoG signal of the $n$th channel of a total of $N$ channels.

# B. ECoG Electrode Activation Index 

To find the electrodes detecting signals most related to hand movement, we computed the activation index (AI). The AI is based on the local motor potential (LMP), the smoothed amplitude of the ECoG, which is known to be correlated in some motor areas with the time course of arm and finger movements [18]. To compute the LMP we used a moving average window with a length of two seconds, $T$ :

$$
L M P(t)_{n}=\frac{1}{T} \int_{t-T / 2}^{t+T / 2} X(\tau)_{n}^{C A R}
$$

Hand-related activation was computed from the LMP:

$$
A I_{m r}=\frac{(m-r)^{3}}{|\bar{m}-\bar{r}| \sigma_{m, \mid r}^{2}} \frac{N_{m} N_{r}}{N_{m, \mid r}^{2}}
$$

where $m$ denotes the LMP during hand movement state, $r$ denotes the LMP during hand rest state, $\sigma_{m \mid, \mid r}^{2}$ denotes the variance across all hand states, and $N$ denotes the total number of each type of movement state.

The AI was computed across all hand movements for each electrode, and the five electrodes with the largest absolute AI values were considered movement-related for the purpose of subsequent analyses.

## C. Time- Varying Dynamic Bayesian Network

Connectivity between ECoG electrodes was modeled using a TVDBN. In this model, $N$ channels recording the ECoG signal at time $t$ are represented as a vector,

$$
X^{t}=\left(x_{1}^{t}, x_{2}^{t}, \ldots, x_{N}^{t}\right) \in R^{N}
$$

where $t=I, \ldots, T$ defines steps in an ECoG time series with length $T$. The conditional probability of observing a given value at time $t$ given a value at previous time $t-1$ is $P\left(X^{t} \mid\right.$ $X^{t-1}$ ), a first order Markov model in which the state of $X$ at time $t$ depends only on its previous state.

The distribution of temporal ECoG transitions can be described as a linear model:

$$
X^{t}=A^{t} X^{t-1}+\varepsilon
$$

The term $A^{t} \in R^{N \times N}$ is a connectivity coefficient matrix, in which $A^{t}{ }_{i j}$ is the connectivity weight from the $i$ th to the $j$ th channel from time $t-1$ to time $t$.

The $A^{t}$ term can be estimated at time $t$ with:

$$
\hat{A}_{i,}^{t}=\underset{A_{i}^{t} \in R^{1 \times N}}{ } \frac{1}{T} \sum_{t *=1}^{T} w^{t}(t \#)\left(x_{i}^{t *}-A_{i}^{t} X^{t *-1}\right)+\lambda\left\|A_{i}^{t}\right\|
$$

where the weight of an observation at time $t^{*}$ is given by $w^{t}\left(t^{*}\right)$. The parameter $\lambda$ defines a regularization term that shrinks the sparseness of the connection matrix $A$. We set this parameter to 100 [16]. We define the weighting term:

$$
w^{t}(t \#)=\frac{K_{h}(t *-t)}{\sum_{t *=1}^{T} K_{h}(t *-t)}
$$

Where $K_{h}(\cdot)=e^{(-t^{2} / h)}$ is a Gaussian RBF kernel. The parameter $h$ gives the kernel bandwidth that controls the scattering of the kernel. We used a value of 5 for $h[16]$.

The estimation of connectivity coefficient matrix $A$ is decomposed into two orthogonal axes. First, the estimation of the network is separated for each time point by the weight term, which weights the signal heavily near time $t$. Second, the estimation is separated for each channel, as in (6). By this decomposition, the solution to the network is simplified and can be solved as a weighted regression problem by least squares.

# D. General Regression Neural Network 

The time-varying connectivity coefficients in matrix $A$ found with TVDBN were employed as temporal features in a general regression neural network (GRNN). We used the results of our connectivity estimation to create a decoder for hand movement trajectory.

The states of hand movement were defined as $y_{t}(t-1, \ldots, T)$, in $T$ time steps. The connectivity coefficient matrix $A$ at time $t$ was reshaped as a vector: $C\left(A^{t}{ }_{I, I}, \ldots, A^{t}{ }_{I}, N, \ldots\right.$, $\left.A^{t}{ }_{N, I}, \ldots A^{t}{ }_{N, N}\right)$. Then $y$ is a function of $C$ and $y$, and can be estimated by its expected value:

$$
E[y \mid A]=\frac{\int_{-\infty}^{\infty} y f(C, y) d y}{\int_{-\infty}^{\infty} f(C, y) d y}
$$

The probability distribution function $f(C, y)$ is estimated from a set of sample observations by:

$$
\hat{f}(C, y)=\frac{1}{(2 \pi)^{(p+1) / 2} \sigma^{p+1}} \frac{1}{n} \sum_{i=1}^{n} e^{\left(-D_{i}^{2} / 2 \sigma^{2}\right)} e^{\left(-\left(y-y_{i}\right) / 2 \sigma^{2}\right)}
$$

where $n$ is the number of sample observations, $p$ is the dimension of the connectivity coefficient matrix $A, \sigma$ is a smoothing parameter, and $D_{i}{ }^{2}$ is the distance between $C$ and the $i$ th observation $C_{i}$. Substituting (9) into (8), we estimate the hand movement state with:

$$
\hat{y}(C)=\frac{\sum_{i=1}^{n} y_{i} e^{\left(-D_{i}^{2} / 2 \sigma^{2}\right)}}{\sum_{i=1}^{n} e^{\left(-D_{i}^{2} / 2 \sigma^{2}\right)}}
$$

The GRNN used was a four-layer network. The input layer received an input vector, $C$, and transmitted it to the pattern layer. Each unit of the pattern layer output the distance $D_{i}{ }^{2}$ to the summation layer, which performed the numerator and denominator operations in (10). The output layer computed the ratio between the numerator and denominator. The model was trained on $30 \%$ of the data and tested on $70 \%$.

# III. Results 

Eighteen trials of hand opening and closing movements were measured with the data glove. The simultaneously recorded ECoG signals were pre-processed, and LMP and AI of each channel were calculated. Using the AI, five ECoG channels were identified as displaying movement-related changes in LMP activity. The distribution of the AI measure is shown below in Fig. 2 .

Channels 39, 68, 2, 55, and 4 were considered movement-related for the purpose of subsequent analyses. Channels 39 and 55 had positive AI values, which indicates that the evolution of the LMP in these channels was positively correlated with the hand movement. Channels 68, 2, and 4 had negative values, indicating negative correlations with hand movement.

TVDBN connectivity coefficients for the five movement-related ECoG channels are shown in Fig.3. Fig.3a shows the averaged hand movements across trials. The onset of hand movement occurred at 0.8 s . In Fig.3b the connectivity coefficients between channels 39, 68, 2,55 , and 4 are averaged across all 18 hand open/close trials. Most connectivity coefficients decrease before and during hand movement onset; the exceptions are connections $4 \rightarrow 2$, $68 \rightarrow 2,68 \rightarrow 4,2 \rightarrow 68$, and $4 \rightarrow 68$. From the average of all connections, there is a reversal in average connectivity coefficient values preceding movement onset. Over the course of the movement duration, the average of the connectivity coefficients returns to baseline.

The mean and standard error of movement-related ECoG channels' TVDBN connectivity coefficients during movement trials are shown in Fig.4. In many cases there is a measurable and statistically significant change in the strength of connectivity before and during hand movement.

To further validate the TVDBN's tracking of movement-related cortical network changes and test the feasibility of using TVDBN connectivity coefficients to inform a motor BMI,

we built a GRNN decoder. The results of this decoding algorithm using TVDBN connectivity coefficients as input are shown in Fig.5.

The correlation between actual and predicted hand movement in the testing data was 0.68 , which is comparable to reported spike-based movement decoding [19]. The TVDBN results can therefore be used as a valid input and informational tool for an ECoG-based BMI.

# IV. Discussion and Conclusions 

We have demonstrated the TVDBN's ability to represent changes in connectivity measured in the ECoG signal during hand movement.

The electrodes selected for this analysis are located, based on ESM results, in cortical areas that are primary motor, premotor and/or supplementary motor, and sensory. We have therefore described cortical circuits active preceding and during movement that process motor and sensory information. As expected, the largest changes in TVDBN connectivity coefficients occurred in connections between electrode 39, which was near hand primary motor area, and other movement-related electrodes. However, a large, early onset connectivity shift was also observed in, e.g., electrodes 2 and 68. ESM predicts that electrode 2 is in a sensory area, and electrode 68 is adjacent to electrodes that elicited a primary motor ESM response. TVDBN reveals a potential premovement sensory-to-motor circuit. TVDBN as applied to ECoG during a motor task elucidates the mechanisms of cortical processing during movement.

The authors thank Matthew Fifer for his contributions to the project, including support of the data analysis.

This work was supported in part by a grants from the National Science Foundation, ECCS-0835554, and from the National Institutes of Health, 1R01EB010100-01.
