# NIH Public Access 

Author Manuscript
IEEE Trans Neural Syst Rehabil Eng. Author manuscript; available in PMC 2013 March 1.
Published in final edited form as:
IEEE Trans Neural Syst Rehabil Eng. 2012 March ; 20(2): 143-152. doi:10.1109/TNSRE.2011.2175309.

## Connectivity analysis as a novel approach to motor decoding for prosthesis control

Heather L. Benz,<br>Department of Biomedical Engineering, Johns Hopkins University, Baltimore, MD 21205 USA. phone: 443-424-2369<br>Huaijian Zhang,<br>Qiushi Academcy for Advanced Studies, Zhejiang University, Hangzhou, China<br>Anastasios Bezerianos[Senior Member, IEEE],<br>Department of Medical Physics, University of Patras, Patras, Greece<br>Soumyadipta Acharya,<br>Department of Biomedical Engineering, Johns Hopkins University, Baltimore, MD 21205 USA<br>Nathan E. Crone,<br>Department of Neurology, Johns Hopkins University, Baltimore, MD 21205 USA<br>Xioaxiang Zheng, and<br>Qiushi Academcy for Advanced Studies, Zhejiang University, Hangzhou, China<br>Nitish V. Thakor[Fellow, IEEE]<br>Department of Biomedical Engineering, Johns Hopkins University, Baltimore, MD 21205 USA<br>Heather L. Benz: benz@jhu.edu


#### Abstract

The use of neural signals for prosthesis control is an emerging frontier of research to restore lost function to amputees and the paralyzed. Electrocorticography (ECoG) brain-machine interfaces (BMI) are an alternative to EEG and neural spiking and local field potential BMI approaches. Conventional ECoG BMIs rely on spectral analysis at specific electrode sites to extract signals for controlling prostheses. We compare traditional features with information about the connectivity of an ECoG electrode network. We use time-varying dynamic Bayesian networks (TV-DBN) to determine connectivity between ECoG channels in humans during a motor task. We show that, on average, TV-DBN connectivity decreases from baseline preceding movement and then becomes negative, indicating an alteration in the phase relationship between electrode pairs. In some subjects, this change occurs preceding and during movement, before changes in low or high frequency power. We tested TV-DBN output in a hand kinematic decoder and obtained an average correlation coefficient $\left(r^{2}\right)$ between actual and predicted joint angle of 0.40 , and as high as 0.66 in one subject. This result compares favorably with spectral feature decoders, for which the average correlation coefficient was 0.13 . This work introduces a new feature set based on connectivity and demonstrates its potential to improve ECoG BMI accuracy.


## Index Terms

Brain computer interfaces; connectivity analysis; motor control; time-varying dynamic Bayesian networks

# I. Introduction 

The electrocorticogram (ECoG) signal is an indicator of cortical activity recorded with electrodes implanted on the surface of the brain [1]. ECoG has recently become a modality of interest for use in brain-machine interfaces (BMI) [2]-[12]. ECoG's utility as a control signal for a BMI was demonstrated in 2004 on a one- and two-directional cursor control task [2]. It has since been used in cursor control tasks [3]-[4], [7]-[8], [10]-[11], reach decoding [5], and grasp and individual finger decoding [6], [9], [12].

ECoG decoding algorithms largely mirror similar algorithms used in EEG-based BMIs. Frequency-domain features are extracted, often using an autoregressive model [13], and low-frequency and/or high-frequency band power variations are typically used in a linear model as predictors for a conditioned task or the kinematics of movement. An additional slow temporal feature, the local motor potential (LMP) has also been shown to vary with slow reaching and grasping motions and is included as a feature in recent BMI decoding models [5], [12]. While high decoding accuracy for classification of movement has been reported in the literature [3]-[4], [6], trajectory prediction accuracy and online decoding latency has not improved significantly since ECoG's introduction as a BMI control signal [2], with an average of $90 \%$ of targets hit in a 1D imagined control task. It is unlikely that the target population for ECoG-based BMI use will accept accuracy significantly below that provided by a natural or cable-controlled arm in clinical use [14]; therefore, fundamental shifts in BMI features and decoding algorithms will be necessary to create a truly clinically relevant BMI.

A clinically relevant BMI would need to operate in real-time and derive sufficient information from the neural signal to achieve nearly $100 \%$ accurate control. In order to create a BMI with an operating speed approaching natural execution time and a level of accuracy that is acceptable to a patient population, new models of cortical communication and new techniques are required with rapid calculation speed and high information rate. Current BMIs use signals from individual electrodes and features based on changes in frequency band power, indicators only of localized processing. It is very likely, however, that most processing involves extended cortical circuits, which are better observed through the signals recorded over a wider span of the ECoG array. A better understanding of the flow of information through these circuits may improve BMI accuracy. One new and promising approach is connectivity mapping, the reconstruction of functional connections between cortical areas based on the signals present in those areas. Here we implement a high-throughput, dynamic, and computationally cheap method to map connectivity. We hypothesize that the connectivity coefficients of these directed connectivity maps will be informative in decoding joint angle information during palmar grasp from the ECoG signal.

We chose to investigate rapid changes in connectivity using the recently described method of time-varying dynamic Bayesian networks (TV-DBN) [15]-[16]. The dynamic nature of the method permits the extraction of data at several time points throughout a movement trial. The method also takes advantage of graph theory to achieve efficient computation. TV-DBN is applicable to the estimation of directed, constantly time-varying networks, and avoids pitfalls such as fixed node dependencies [17], the use of a priori static networks that may fail to detect rapid connectivity changes [18], and piece-wise stationary models that do not vary constantly in time [19]. We chose this method over coherency and phase-based methods [20]-[22], [23]-[26], first because it produces directional results, potentially doubling the amount of data extracted from a single connectivity map over undirected approaches, and second because we sought to create a map of information flow at known time delays. Dynamic Bayesian networks have also been shown to outperform a Granger causality-based approach in the case of short data windows [27]. Moreover, SdDTF, a

Granger causality-based approach that is applicable to short time windows, is calculated using a multivariate autoregressive model, an algorithm that is prohibitively computationally expensive in the context of BMI [28]. We have further compared TV-DBN and alternative methods in Discussion and Conclusions, below. Here we apply TV-DBN estimation of directed connectivity to multichannel ECoG data recorded during a simple motor grasping task. We seek evidence that movement-related variation in TV-DBN coefficients occur on a different time scale compared to movement-related variation in spectral features. Then we use connectivity coefficients to create an ECoG kinematic decoder and compare it to a standard spectral feature-based decoder.

# II. Methods 

## A. Study Participants and Data Collection

Four human patients with epilepsy undergoing monitoring in preparation for surgery participated in motor experiments. During the experiments clinical ECoG data were collected. The experimental protocol was approved by the Johns Hopkins Institutional Review Board and all subjects gave informed consent. The study participants were two males and two females, aged 15-58 years and right handed. Table I summarizes additional subject details.

The ECoG signal was recorded using subdurally implanted grids with 88 to 114 platinum electrodes of diameter 4 mm imbedded in a silastic sheet and spaced 10 mm apart (Adtech Medical Instrument Corp., Racine, WI). The electrode locations were determined with Curry software (Neuroscan Inc.) by co-registration of pre-implantation MRI with post implantation CT using anatomical fiducials. In all subjects there was coverage of motor, premotor, and/or supplementary motor cortex, shown in Fig. 1. Clinical electrocortical stimulation mapping data, also depicted in Fig. 1, was used to assist in identifying sensorimotor areas. The ECoG signal was recorded using a 128-channel amplifier (Stellate Systems Inc., Montreal), digitized at 1000 Hz per channel, and referenced to an inactive intracranial electrode. The ECoG data were filtered between $0.15-300 \mathrm{~Hz}$, with a second-order Butterworth filter. A notch filter was used at 60 Hz . The signals were re-referenced with a common average reference (CAR) filter [29] to remove sources of noise common to all channels.

During the motor experiment, 18 joint angles of the hand contralateral to the hemisphere of the implanted ECoG grid were recorded and digitized at 25 Hz using a data glove (CyberGlove, CyberGlove Systems LLC, San Jose, CA). These joint angles were metacarpal phalangeal, interphalangeal, and distal phalangeal joints and abduction/adduction of all five fingers. These hand motor data were synchronized to the ECoG signal by writing simultaneous time stamps and event markers to both data streams.

## B. Experimental Protocol

Experimental sessions lasted approximately one to three hours in length, during which a battery of several hand motor tasks was performed. For this work, only palmar grasp trials were analyzed. Each subject performed 10-25 palmar grasps over the course of 128-378 s, across all trials. Subject A was tested on two successive days; all other subjects were tested in only a single session. Individual trials lasted between approximately one and five minutes. Session and trial length accommodated subject fatigue and interest. A neurologist monitored all experimental sessions and subjects were permitted to rest between trials.

The experiment was designed to collect data that could be used to build a decoding model to control a hand prosthesis: during ECoG recording, joint angles were recorded with the arm in a comfortable position, somatosensory feedback was limited, and a typical prosthesis movement was repeated a number of times. Each subject sat in a hospital bed, with the arm

of the hand wearing the data glove to record joint angles resting on a pillow to permit it to rest in a comfortable position between trials. The elbow joint was usually partially flexed in this position, and the hand partially prone. To limit unusual somatosensory feedback, the hand did not touch the pillow or any other surfaces during experimental recording. The subject performed repeated slow-paced palmar grasps, opening and closing all fingers on the hand contralateral to the implanted ECoG grid. A slow-paced palmar grasp was chosen to mimic the most typical use of a hand prosthesis. These grasps were either self-paced or verbally cued depending on patient compliance with the task.

# C. Local Motor Potential 

The LMP, a smoothed amplitude feature of the ECoG in the temporal domain, was used as an ECoG feature in conjunction with high frequency and low frequency power information for analysis and decoding. The LMP on sensorimotor electrodes has been shown to vary with slow-paced grasping motions like those used in this study, and is a commonly-used feature in ECoG BMI algorithms [5]. We have shown that the LMP alone can be used to decode these slow grasps with high accuracy, even when very few electrodes are used in the decoding model [12].

We computed the LMP with a moving average window T of 2 s duration:

$$
L M P(t)_{n}=\frac{1}{T} \int_{t-T / 2}^{t+T / 2} X(\tau)_{n}^{C A R}
$$

Here $X(\tau)_{n}^{C A R}$ is the time signal from the $n$th ECoG electrode after filtering, where $\tau$ is the time. The LMP was used in screening for electrodes whose activity was related to movement and for constructing decoding models.

## D. ECoG Electrode Activation Index

To restrict initial TV-DBN analysis to sensorimotor electrodes, we first screened electrodes for motor-related activity using the electrode activation index (AI), described below. The AI is a measure of the average extent of change in ECoG features between baseline and movement. It is calculated using both the power in low frequency bands and power in high frequency bands, ECoG features that are known to vary in sensorimotor areas preceding and during hand movement [2], [5], [30]-[31].

It has been suggested that changes in broadly-defined low and high frequency power bands are sufficient to quantify motor activity [11]. We therefore calculated log power in low (1230 Hz ) and high $(75-150 \mathrm{~Hz})$ frequency bands. To ensure compatibility of the algorithm with eventual clinical applications needing computationally efficient implementations, the fast Fourier transform (FFT) [32], which has been used in many recent online ECoG BMI implementations [7], [33], was used rather than autoregressive modeling [13]. The FFT was implemented with standard MATLAB (MathWorks, Natick, MA) toolboxes. The window size for the low frequency band (LFB) was 512 ms , and the window size for the high frequency band (HFB) was 256 ms .

We compared each of the three features (LMP, LFB, and HFB), between the baseline state (rest, $r$ ) and active state (hand movement, $m$ ). We used a statistic from the literature, the cross-correlation coefficient [34]:

Here $r$ denotes the average feature value during rest, $m$ denotes the average feature value across all hand movements, $\sigma$ denotes the feature variance across all hand states, and $N$ denotes the total number of incidences of each state.

The AI was then determined for each electrode by the feature with the largest normalized change between rest and movement states for all hand movements:

$$
A I=\max \{L M P, L F B, H F B\}
$$

The five electrodes with the highest AI values were considered to represent hand movementrelated locations for the purposes of connectivity analysis. Five electrodes were chosen because for all subjects except Subject C, previous work has shown that within five electrodes, decoding accuracy ( $r$, correlation between actual and predicted hand movements) reached approximately $95 \%$ of maximum decoding accuracy [12]. Furthermore, preliminary networks of five electrodes contained sufficient connections to probe with maps of cortical connectivity.

# E. Time-Varying Dynamic Bayesian Networks 

The TV-DBN framework was used to model connectivity and directionality between pairs of ECoG electrodes. Under this framework we considered the connectivity coefficient from electrode $i$ to electrode $j$ to be high at time $t$ if information about activity at electrode $i$ at time $t-1$ could be used to predict activity at electrode $j$ at time $t$. The $N$ ECoG channels recorded from each patient were represented as a vector at time $t$ :

$$
X^{t}=\left(x_{1}^{t}, x_{2}^{t}, \ldots, x_{N}^{t}\right) \in R^{N}
$$

The time steps $t=1, \ldots, T$ were used to express a time series of ECoG data with length $T$. A first order Markov model was used, meaning that the state of each ECoG signal, $X$, at time $t$ depended only on the previous state of all ECoG channel signals at time $t-1,200 \mathrm{~ms}$ before time $t$. In this case the conditional probability of observing a given set of ECoG amplitudes at time $t$ given amplitudes at previous time $t-1$ was $P\left(X^{t} \mid X^{t-1}\right)$.

The distribution of temporal ECoG transitions were modeled with linear regression:

$$
X^{t}=A^{t} X^{t-1}+\varepsilon
$$

The term $A^{t} \in R^{N \times N}$ was then a connectivity coefficient matrix, in which $A_{i j}^{t}$ was the connectivity weight from the $i$ th to the $j$ th channel from time $t-1$ to time $t$. The $A^{t}$ term was estimated at time $t$ by minimizing the criterion:

$$
\widehat{A}_{i}^{t}=\operatorname{argmin}_{x_{i}^{t} \in R^{1 \times N}} \frac{1}{T} \sum_{t^{\prime \prime}=1}^{T} w^{t}\left(t^{\prime \prime}\right) x_{i}^{t^{\prime \prime}}-A_{i}^{t} X^{t^{\prime \prime}-1}+A\left\|A_{i}^{t}\right\|
$$

The parameter $\lambda$ was a regularization term that shrank the sparseness of the connectivity matrix $A$. Previous work led us to use a value of 100 for this parameter [15]. The weight of an observation at time $t^{*}$ was given by $w^{t}\left(t^{*}\right)$, defined using a Gaussian RBF kernel:

$$
\begin{gathered}
w^{t}\left(t^{*}\right)=\frac{K_{h}\left(t^{*}-t\right)}{\sum_{t^{*}=1}^{T} K_{h}\left(t^{*}-t\right)} \\
K_{h}(\cdot)=e^{-t^{2} / h}
\end{gathered}
$$

The kernel bandwidth was given by the parameter $h$, which controls the scattering of the kernel. We used a value of 5 for $h$ [15]. The Gaussian RBF kernel was used in estimating $A^{t}$ to reduce noise and provide a more stable estimate. It was summed only over points up to $t$, maintaining causality. The low variance ensured that only data near time $t$ was used in estimating $A^{t}$.

The connectivity coefficient matrix $A$ was estimated by decomposing the matrix into two orthogonal axes. The first axis was defined at each time point by the weight term, which weights the signal heavily near time $t$. The second axis was defined by each channel, as in (6). Through this decomposition simplification, the network can be solved as a weighted regression problem by least squares.

# F. General Regression Neural Networks 

We hypothesized that connectivity coefficients found with TV-DBN would improve decoding of kinematic information from neural data over using traditional features alone. To test this hypothesis, we constructed two general regression neural networks (GRNN) per subject, which decoded continuous joint angle for one angle that was chosen to be representative of the trajectory of hand opening and closing [35]. The GRNN was chosen to maintain rapid computational speed. It is a fast learning algorithm and does not use an iterative procedure. The first GRNN decoded joint angle from standard BMI features (the "spectral feature GRNN"), and the second used TV-DBN connectivity coefficients (the "TV-DBN GRNN").

The spectral feature GRNN used as inputs the LMP and the log power of low ( 12 to 30 Hz ) and high ( 75 to 150 Hz ) frequency bands for all electrodes (between 264 and 342 total features). The TV-DBN GRNN used the connectivity coefficient matrix $A$. To maximize decoding accuracy, we computed TV-DBN connectivity coefficients for all electrodes, and chose as decoding features the $5 \%$ of connectivity coefficients most highly correlated with the time course of the hand joint angle (between 387 and 650 total features).

For both GRNN decoders, the states of hand movement were defined as $y_{t}(t-1, \ldots, T)$, in $T$ time steps. The spectral feature matrix $S$ and the connectivity coefficient matrix $A$ at time $t$ were reshaped as a vector. For the TV-DBN decoder, this vector was $C\left(A_{1,1}^{t}, \ldots, A_{i, N}^{t}, \ldots, A_{N, i}^{t}, \ldots, A_{N, N}^{t}\right)$. Then $y$ was a function of $C$ and $y$, and was estimated by its expected value:

$$
E[y \mid A]=\frac{\int_{-\infty}^{\infty} y f(C, y) d y}{\int_{-\infty}^{\infty} f(C, y) d y}
$$

The probability distribution function $f(C, y)$ was estimated with:

Here $n$ was the number of sample observations, $p$ was the dimension of the connectivity coefficient matrix $A, \phi$ was a smoothing parameter, and $D_{i}^{2}$ was the distance between $C$ and the $i^{\text {th }}$ observation $C_{i}$. Substituting (10) into (9), we estimated the movement state with:

$$
\bar{y}(C)=\frac{\sum_{i=1}^{n} y_{i} e^{-D_{i}^{2} / 2 \phi^{2}}}{\sum_{i=1}^{n} e^{-D_{i}^{2} / 2 \phi^{2}}}
$$

The GRNNs used were four-layer networks with input vector $C$. Each unit of the pattern layer output the distance $D_{i}^{2}$ to the summation layer, which performed the numerator and denominator operations in (11). The output layer computed the ratio between the numerator and denominator. Initial models were trained on $30 \%$ of the data and tested on $70 \%$. Fivefold cross-validation was used to construct comparison spectral feature and TV-DBN models.

# III. Results 

## A. Selection of Movement-Related Electrodes

Motor-related electrodes were selected using the metric AI representing the average change in ECoG features between baseline and movement. Maps of normalized absolute AI are shown for each subject in Fig. 2. A subset of the five electrodes from each subject with highest absolute AI values was chosen for subsequent analysis of movement-related changes in connectivity. Details on the electrodes selected for analysis, including approximate electrode location and clinical electrocortical stimulation mapping (ESM) results are given in Table II. Electrodes with high absolute AI were largely located over peri-Rolandic sensorimotor areas ( $75 \%$ ). In three of four subjects (A, B, and D) the activity on a few electrodes was well correlated with movement. Subject C had generally very low correlation between motor activity and ECoG features.

## B. Peri-Movement TV-DBN Connectivity Coefficients

TV-DBN connectivity coefficients were computed between all possible pairs from the five most movement-related electrodes for each subject. A representative plot of the evolution of TV-DBN connectivity coefficients for subject A is shown in Fig. 3. On average, movementrelated TV-DBN connectivity coefficients decreased preceding movement, entering a period during which the average influence was negative, and recovered gradually over the time course of movement. Negative values in TV-DBN connectivity coefficients may indicate a change in the phase difference between signals, or more simply that an increase in activity at one electrode precedes a decrease in the activity at another.

In three subjects the TV-DBN connectivity coefficients between at least two pairs of movement-related electrodes showed a statistically significant change from baseline during movement ( $p<0.05$, Kruskal-Wallis test). For subject B, 13 electrode pairs, the most across all subjects, exhibited statistically significant changes in TV-DBN connectivity coefficients. For subject C no electrode pairs exhibited a statistically significant change in TV-DBN connectivity coefficients. Fig. 4 depicts TV-DBN connectivity coefficients between all

movement-related electrodes for all subjects averaged over hand movement trials. Movement onset is indicated with a vertical line.

# C. TV-DBN Connectivity Coefficient Evolution in Time 

In order to better visualize the evolution of the cortical connectivity network preceding and during movement, TV-DBN connectivity coefficients between movement-related electrodes with a statistically significant change from baseline ( $p<0.05$, Kruskal-Wallis test) were overlaid on cortical reconstructions. An exemplary set of cortical connectivity networks is shown in Fig. 5 for subject A for pre-movement ( $\sim 0.6$ to $\sim 0.2 \mathrm{~s}$ ), movement onset ( 0 to 0.2 s ), and during movement ( 0.4 to 1.4 s ) conditions. In subject A the pre-movement connectivity network was widespread with strong projections between motor-related electrodes. Connectivity at movement onset was more limited. As the movement continued, the connectivity network incorporated several electrodes and may have represented sensorimotor integration.

We observed what appeared to be an early onset of TV-DBN connectivity coefficient changes, relative to the onset of movement and the onset of movement-related changes in other ECoG features. As an example, the average time courses of spectral features and TVDBN connectivity coefficients for subjects A and B are shown in Fig. 6.

We used principal component analysis to explore whether the changes in connectivity coefficients preceding and following movement onset could be grouped in a meaningful way. Principal components (PCs) of TV-DBN connectivity coefficients for all four subjects did tend to separate into those that reached extrema pre-movement, those that reached extrema near movement onset, and those that did so during movement (see Fig. 7). A representation of the connectivity coefficients that most contributed to the first four PCs for Subject A is shown in Fig. 8. The PC whose largest change occurred pre-movement is the only one to include significant connections to and from a frontal electrode, while the PC with large post-movement change includes primarily connections to and from peri-Rolandic areas.

## D. Motor Decoding with TV-DBN Connectivity Coefficients

To investigate whether TV-DBN connectivity coefficients could improve upon neural decoding based on spectral and LMP ECoG features, we constructed two GRNNs with fivefold cross-validation for each subject to decode joint angle from neural data. The first set of GRNNs used spectral features in a low frequency bin ( 12 to 30 Hz ) and a high frequency bin ( 75 to 150 Hz ) and the LMP for all electrodes, a total of 264-342 features. Average optimal decoding accuracy (correlation coefficient, $r^{2}$, between actual and predicted joint angle) with this spectral feature set of GRNNs was 0.13 . The second set of GRNNs used the top $5 \%$ of TV-DBN connectivity coefficients most correlated with joint angle, a total of 387-650 features. Average optimal decoding accuracy was 0.40 . Decoding accuracy is shown for each subject in Table III, and TV-DBN decoding results for one trial for each subject are shown in Fig. 9. Although the spectral feature GRNN s decoding accuracy is below the average reported in a recent study of decoding individual finger movement from ECoG (0.27 [9]), the TV-DBN decoding results are on average higher.

It is likely that at least some of the improved accuracy in the TV-DBN GRNN may be attributed to the increased number of features included in the decoder. For LMP, LFP, and HFP, the maximum number of features that can be used in decoding is $3 N$, where $N$ is the number of ECoG channels, whereas the maximum number of directed connectivity-based features is $N^{2}-N$. The high throughput nature of this method may lead to improved decoding capabilities.

Using MATLAB 2011b on an Intel(R) Core(TM)2 Duo 2.53 GHz processor, the approximate computation time for extracting TV-DBN features for five electrodes was 4 ms for each 200 ms time step. With five fold cross-validation, GRNN training time was 110 ms , and the computation time of each GRNN output for testing was negligible. Using only 5 electrodes, this system would be applicable to real-time BMI. However, as implemented, calculating TV-DBN coefficients for all electrodes required approximately 580 ms per time step, meaning that pre-selecting a subset of electrodes is necessary for real-time neuroprosthetic control.

# IV. Discussion and Conclusions 

We have described the application of a new method for determining directional connectivity of brain functional regions using the ECoG signal. The benefits of the TV-DBN method are the abilities to: detect early changes in connectivity, handle short data windows, and vary constantly in time. This method was applied to human ECoG data to identify cortical connectivity preceding and during hand movement. We then used TV-DBN connectivity coefficients to create a hand movement decoder that improved upon a decoder constructed with standard spectral and LMP based ECoG features.

This approach has potential applications in ECoG-based BMI, not only as a method for extracting additional information, but also for probing pre-movement and movement cortical circuits. Results suggest that further investigation into signatures of pre-movement activity may yield early movement prediction and improved decoding.

## A. Interpretation of connectivity coefficients

From literature, it is expected that immediately preceding hand movement there may be activity from supplementary motor [36]-[38] and premotor areas [39]-[40]. This activity informs the primary motor cortex, which is directly responsible for movement control [41]. It is possible that this early activity created the change in TV-DBN connectivity coefficients that we observed preceding movement. During movement, somatosensory information provides feedback to motor areas [42], updating the projected motor model. Statistically significant changes in TV-DBN connectivity coefficients from baseline support this model, with connectivity between a variety of motor areas preceding hand movement. At movement onset, a limited directed connectivity network develops involving the motor electrode most highly correlated with hand movement. As movement continues, there are once again more spatially widespread statistically significant connectivity coefficients. This connectivity network present during movement may be a reflection of the fact that the motor areas are receiving sensory feedback to update the projected motor model.

## B. Comparison to alternative techniques

A handful of approaches exist to map influences or similarities between time-varying signals, including coherency and phase-based methods [20]-[22] and Granger causalitybased methods [43]-[28]. These approaches can be applied to the problem of discovering connectedness between areas of cortex covered by ECoG electrodes.

Coherency is a baseline measure of interactivity between cortical areas [20]-[21]. The imaginary part of coherency has been used in EEG to find directionality of information flow [22]. Similar phase-based methods [23]-[26] can indicate EEG and ECoG signal flow and in some cases directionality. However, due to the nature of the phase, it is not possible to create a precise temporal map of information flow at known time delays. Moreover, there is a problem of high correlation in multichannel data, causing pair-wise interactivity algorithms to incorrectly estimate overriding common influences across multiple channels [47]-[48].

The directed transfer function (DTF), an extension of the Granger causality concept to multivariate signals [43], addresses the problem of pair-wise connectivity algorithms. The DTF has been further refined in the direct DTF (dDTF), which exhibits improved ability to differentiate direct causality from cascaded causality [46], and the short-time DTF (SDTF), which is applicable to short signal windows [44]-[45]. The dDTF and SDTF have been combined in the SdDTF [28], which is well suited to exploring rapid changes in direct connectivity. However, the SdDTF requires multiple trials and is calculated using a multivariate autoregressive model, an algorithm that is computationally expensive.

Because the TV-DBN results demonstrated here are independent of ECoG frequency band, unlike techniques such as the imaginary part of coherency [22] or SDTF [45] and SdDTF [28], we are able to investigate causality outside the constraints of frequency. The TV-DBN, like Granger causality-based methods, has a basis in causality. Connections discovered with the TV-DBN therefore reflect relationships more clearly than, for example, the imaginary part of coherency, which can only indicate that one element of an interacting pair preceded another. Compared to the SdDTF, a measure of causality that can be applied to short time windows [28], the TV-DBN has decreased computational complexity but is applicable to similarly short time windows ( 200 ms in this study compared to 360 ms in the 2008 SdDTF study).

# C. Limitations of the method 

Clinical ECoG currently offers coverage dictated by clinical need, and electrodes spaced millimeters to centimeters apart. It is likely that for a practical ECoG-based BMI, more localized and spatially dense coverage will be most practically feasible and provide the best signals for BMI control [33]. However, because $N^{2}-N$ features are extracted with directed connectivity methods, compared to the number extracted with spectral analysis (proportional to $N$ ) this may be a more information rich method of signal analysis for ECoG-based BMI.

In this experiment subjects received somatosensory, proprioceptive, and visual feedback as they moved the hand and observed their own movements. In the operation of a prosthesis, somatosensory and proprioceptive feedback would be absent, and visual feedback may be different from what the subject expects. Directed connectivity mapping provides a unique tool to model the interactions between proprioceptive, somatosensory, visual, and motor areas. The models may then be adapted to account for the absence of normal activity in these areas.

The TV-DBN model used in this analysis was based on a first order Markov model, in which the state of an ECoG signal depended only on the previous state of all ECoG channels at a time 200 ms earlier. It is unlikely that this offset effectively probes all causal relationships between cortical regions, and a more comprehensive model would consider the effects of channel states at multiple time lags. We chose to study the model at a single time lag to preserve computational efficiency of the TV-DBN and to enable implementation in a real-time BMI.

The method did not incorporate explicit models of physiological mechanisms of connectivity. For example, we did not probe phase synchronization or specific frequency bands, such as theta oscillations, that have been shown to synchronize during a variety of tasks, potentially guiding the synchronization of cortical processing [49]-[53]. However, physiological mechanisms for connectivity may be incorporated into the model in a "black box" way, without being explicitly defined, because the TV-DBN finds signal connectivity.

# Acknowledgments 

This work was supported in part by the National Institutes of Health under Grant 3R01NS040596-09S1 and the Defense Advanced Research Projects Agency under Grant 19GM-1088724.

# TABLE I

Experimental Subject Summary


TABLE II
AI-Based Electrode Selection


*Adjacent to electrodes with a motor ESM result
${ }^{X}$ Adjacent to electrodes with a sensory ESM result
${ }^{\prime}$ Adjacent to electrodes with motor and sensory ESM results

# TABLE III 

Average Maximum Decoding Accuracy by Subject (correlation coefficient, $r^{2}$ )
