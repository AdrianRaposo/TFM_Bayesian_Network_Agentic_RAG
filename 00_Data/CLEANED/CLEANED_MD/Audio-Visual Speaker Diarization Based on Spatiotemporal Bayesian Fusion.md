# Audio-Visual Speaker Diarization Based on Spatiotemporal Bayesian Fusion 

Israel D. Gebru, Silèye Ba, Xiaofei Li and Radu Horaud


#### Abstract

Speaker diarization consists of assigning speech signals to people engaged in a dialogue. An audio-visual spatiotemporal diarization model is proposed. The model is well suited for challenging scenarios that consist of several participants engaged in multi-party interaction while they move around and turn their heads towards the other participants rather than facing the cameras and the microphones. Multiple-person visual tracking is combined with multiple speech-source localization in order to tackle the speech-to-person association problem. The latter is solved within a novel audio-visual fusion method on the following grounds: binaural spectral features are first extracted from a microphone pair, then a supervised audio-visual alignment technique maps these features onto an image, and finally a semisupervised clustering method assigns binaural spectral features to visible persons. The main advantage of this method over previous work is that it processes in a principled way speech signals uttered simultaneously by multiple persons. The diarization itself is cast into a latent-variable temporal graphical model that infers speaker identities and speech turns, based on the output of an audio-visual association process, executed at each time slice, and on the dynamics of the diarization variable itself. The proposed formulation yields an efficient exact inference procedure. A novel dataset, that contains audio-visual training data as well as a number of scenarios involving several participants engaged in formal and informal dialogue, is introduced. The proposed method is thoroughly tested and benchmarked with respect to several state-of-the art diarization algorithms.


Index Terms-speaker diarization, audio-visual tracking, dynamic Bayesian network, sound source localization,

## I. INTRODUCTION

In human-computer interaction (HCI) and human-robot interaction (HRI) it is often necessary to solve multi-party dialogue problems. For example, if two or more persons are engaged in a conversation, one important task to be solved, prior to automatic speech recognition (ASR) and natural language processing (NLP), is to correctly assign temporal segments of speech to corresponding speakers. In the speech and language processing literature this problem is referred to as speaker diarization, or "who speaks when?" A number of diarization methods were recently proposed, e.g. [1]. If only unimodal data are available, the task is extremely difficult. Acoustic data are inherently ambiguous because they contain mixed speech signals emitted by several persons, corrupted by reverberations, by other sound sources and by background

[^0]noise. Likewise, the detection of speakers from visual data is very challenging and it is limited to lip and facial motion detection from frontal close-range images of people: in more general settings, such as informal gatherings, people are not always facing the cameras, hence lip reading cannot be readily achieved.

Therefore, an interesting and promising alternative consists of combining the merits of audio and visual data. The two modalities provide complementary information and hence audio-visual approaches to speaker diarization are likely to be more robust than audio-only or vision-only approaches. Several audio-visual diarization methods have been investigated for the last decade, e.g. [2]-[7]. Diarization is based on audio-visual association, on the premise that a speech signal coincides with the visible face of a speaker. This coincidence must occur both in space and time.

In formal scenarios, e.g. meetings, diarization is facilitated by the fact that participants take speech turns, which results in (i) a clear-cut distinction between speech and non-speech and (ii) the presence of short silent intervals between speech segments. Moreover, participants are seated, or are static, and there are often dedicated close-field microphones and cameras for each participant e.g. [8]. In these cases, the task consists of associating audio signals that contain clean speech with frontal images of faces: audio-visual association methods based on temporal coincidence between the audio and visual streams seem to provide satisfactory results, e.g. canonical correlation analysis (CCA) [9]-[11] or mutual information (MI) [2], [3], [12], [13]. Nevertheless, temporal association between the two modalities is only effective on the premises that (i) speech segments are uttered by a single person at a time, that (ii) single-speaker segments are relatively long, and that (iii) speakers continuously face the cameras.

In informal scenarios, e.g. ad-hoc social events, the audio signals are provided by distant microphones, hence the signals are corrupted by environmental noise and by reverberations. Speakers interrupt each other, hence short speech signals may occasionally be uttered simultaneously by different speakers. Moreover, people often wander around, turn their head away from the cameras, may be occluded by other people, suddenly appear or disappear from the cameras' fields of view, etc. Some of these problems were addressed in the framework of audio-visual speaker tracking, e.g. [14]-[16]. Nevertheless, audio-visual tracking is mainly concerned with finding speaker locations and speaker trajectories, rather than solving the speaker diarization problem.


[^0]:    INRIA Grenoble Rhône-Alpes, Montbonnot Saint-Martin, France.
    E-mail: \{israel-dejene.gebru, sileye.ba, xiaofei.li, radu.horaud\}@inria.fr Funding from the European Union FP7 ERC Advanced Grant VHIA (\#340113) and from XEROX University Affairs Committee (UAC) grant (2015-2017) is greatly acknowledged.

In this paper it is proposed a novel spatiotemporal diarization model that is well suited for challenging scenarios that consist of several participants engaged in multi-party dialogue. The participants are allowed to move around and to turn their heads towards the other participants rather than facing the cameras. We propose to combine multiple-person visual tracking with multiple speech source localization in order to tackle the speech to person association problem. The latter is solved within a novel audio-visual fusion method on the following grounds: acoustic spectral features are extracted from a microphone pair, a novel supervised audio-visual alignment technique maps these features onto the image plane such that the audio and visual modalities are represented in the same mathematical space, a semi-supervised clustering method assigns the acoustic features to visible persons. The main advantage of this method over previous work is twofold: it processes in a principled way speech signals uttered simultaneously by multiple persons, and it enforces spatial coincidence between audio and visual features.

Moreover, we cast the diarization process into a latentvariable temporal graphical model that infers over time both speaker identities and speech turns. This inference is based on combining the output of the proposed audio-visual fusion, that occurs at each time-step, with a dynamic model of the diarization variable (from the previous time-step to the current time-step), i.e. a state transition model. We describe in detail the proposed formulation which is efficiently solved via an exact inference procedure. We introduce a novel dataset that contains audio-visual training data as well as a number of scenarios involving several participants engaged in formal and informal dialogue. We thoroughly test and benchmark the proposed method with respect to several state-of-the art diarization algorithms.

The remainder of this paper is organized as follows. Section II describes the related work. Section III describes in detail the temporal graphical model. Section IV describes visual feature detection and Section V describes the proposed audio features and their detection. Section VI describes the proposed semi-supervised audio-visual association method. The novel audio-visual dataset is presented in detail in Section VII while numerous experiments, tests, and benchmarks are presented in Section VIII. Finally, Section IX draws some conclusions. Videos, Matlab code and additional examples are available online. ${ }^{1}$

## II. Related Work

The task of speaker diarization is to detect speech segments and to group segments that correspond to the same speaker without any prior knowledge about the speakers involved nor their number. This can be done using auditory features alone, or a combination of auditory and visual features. Mel frequency cepstral coefficients (MFCC) is often the representation of choice whenever audio signal segments correspond to a single speaker. Then the diarization pipeline consists of

[^0]splitting the audio frames into speech and non-speech frames, of extracting an MFCC feature vector from each speech frame and of performing agglomerative clustering such that each cluster found at the end corresponds to a different speaker [17]. Consecutive speech frames are assigned either to the same speaker and grouped into segments, or to different speakers, by using a state transition model, e.g. HMM.

The use of visual features for diarization has been motivated by the importance of audio-visual synchrony. Indeed, it was shown that facial and lip movements are strongly correlated with speech production [18] and hence visual features, extracted from frontal views of speaker faces, can be used to increase the discriminative power of audio features in numerous tasks, e.g. speech recognition [19], source separation, [20], [21] and diarization [13], [22]-[24]. In the latter case, the most common approaches involve the analysis of temporal correlation between the two modalities such that the face/lip movements that best correlate with speech correspond to an active speaker.

Garau et al. [2] compare two audio-visual synchronization methods, based on mutual information (MI) and on canonical correlation analysis (CCA), and using MFCC auditory features combined with motion amplitude computed from facial feature tracks. They conclude that MI performs slightly better than CCA and that vertical facial displacements (lip and chin movements) are the visual features the most correlated with speech production. MI that combines gray-scale pixel-value variations extracted from a face region with acoustic energy is also used by Noulas et al. [3]. The audio-visual features thus extracted are plugged into a dynamic Bayesian network (DBN) that perform speaker diarization. The method was tested on video meetings involving up to four participants which are recorded with several cameras, such that each camera faces a participant. More recently, both El Khoury et al. [4] and Kapsouras et al. [7] propose to cluster audio features and face features independently and then to correlated these features based on temporal alignments between speech and face segments.

The methods mentioned so far yield good results whenever clean speech signals and frontal views of faces are available. A speech signal is said to be clean if it is noise free and if it corresponds to a single speaker; hence audio clustering based on MFCC (mel-frequency cepstral coefficients) features performs well. Moreover, time series of MFCC features seem to correlate well with facial-feature trajectories. If several faces are present, it is possible to select the facial feature trajectory that correlate the most with the speech signal, e.g. [9], [10]. However, in realistic settings, participants are not always facing the camera, consequently the detection of facial and lip movements is problematic. Moreover, methods based on cross-modal temporal correlation, e.g. [3], [13], [19], [22][24] require long sequences of audiovisual data, hence they can only be used offline such as the analysis of broadcast news, of audiovisual conferences, etc.

In the presence of simultaneous speakers, the task of diarization is more challenging because multiple-speaker infor-


[^0]:    ${ }^{1}$ https://team.inria.fr/perception/avdiarization/

mation must be extracted from the audio data, one one hand, and the speech-to-face association problem must be properly addressed, on the other hand. In mixed-speech microphone signals, or dirty speech, there are many audio frames that contain acoustic features uttered by several speakers and MFCC features are not reliable anymore because they are designed to characterize acoustic signals uttered by single speakers. The multi-speech-to-multi-face association problem cannot be solved neither by performing temporal correlation between a single microphone signal and an image sequence nor by clustering MFCC features.

One way to overcome the problems just mentioned is to perform multiple speech-source localization [25]-[27] and to associate speech sources with persons. These methods, however, do not address the problems of aligning speechsource locations with visible persons and of tracking them over time. Moreover, they often use circular or linear microphone arrays, e.g. planar microphone setups, hence they provide sound-source directions with one degree of freedom, e.g. azimuth, which may not be sufficient to achieve robust audiovisual association. Hence, some form of microphone-camera calibration is needed. Khalidov et al. propose to estimate the microphone locations into a camera-centered coordinate system [28] and to use a binocular-binaural setup in order to jointly cluster visual and auditory feature via a conjugate mixture model [29]. Minotto et al. [5] learn an SVM classifier using labeled audio-visual features. This training is dependent on the acoustic properties of experimental setup. They combine voice activity detection with sound-source localization using a linear microphone array which provides horizontal (azimuth) speech directions. In terms of visual features, their method relies on lip movements, hence frontal speaker views are required.

Multiple-speaker scenarios were thoroughly addressed in the framework of audio-visual tracking. Gatica-Perez et al. [14] proposed a multi-speaker tracker using approximate inference implemented with a Markov chain Monte Carlo particle filter (MCMC-PF). Navqi et al. [15] proposed a 3D visual tracker, based as well on MCMC-PF, to estimate the positions and velocities of the participants which are then passed to blind source separation based on beamforming [30]. Reported experiments of both [14], [15] require a network of distributed cameras to guarantee that frontal views of the speakers are always available. More recently, Kilic et al. [16] proposed to use audio information to assist the particle propagation process and to weight the observation model. This implies that audio data are always available and that they are reliable enough to properly relocate the particles. While audio-visual multipleperson tracking methods provide an interesting methodology, they do not address the diarization problem. Indeed, they assume that people speak continuously, which facilitates the task of the proposed audio-visual trackers. With the exception of [15], audio analysis is reduced to sound-source localization using a microphone array, and this in order to enforce spatial coincidence between faces and speech.

Recently we addressed audio-visual speaker diarization under the assumption that participants take speech turns and
that there is no overlap between their emitted speech signals. We proposed a simple model that consists of a speech-turn discrete latent variable that associates the speech signal with one of the participants [31], [32]. The main idea of this work was to track multiple persons and to extract a single soundsource direction from short time intervals, e.g. using [33] to map sound directions onto the image plane. Audio and visual observations can then be associated using a recently proposed weighted-data EM algorithm [34]. In the present paper we propose a novel dynamic audio-visual fusion model that can deal with simultaneously speaking participants. In particular, we exploit the spectral sparsity of speech signals and we propose a novel multiple speech source localization method based on a semi-supervised complex-Gaussian mixture model in the Fourier domain. We also generalize the single speakerturn diarization model of [31], [32] to multiple speaking persons.

Recently we addressed audio-visual speaker diarization under the assumption that participants take speech turns and that there is no overlap between their speech segments. We proposed a model that consists of a speech-turn discrete latent variable that associates the current speech signal, if any, with one of the visible participants [31], [32]. The main idea was to perform multiple-person tracking in the visual domain, to extract sound-source directions (one direction at a time), and to map this sound direction onto the image plane [33]. Audio and visual observations can then be associated using a recently proposed weighted-data EM algorithm [34].

In this present paper we propose a novel DBN-based crossmodal diarization model. Unlike several recently proposed audio-visual diarization works [3], [4], [7], [31], [32], the proposed model can deal with simultaneously speaking participants that may wander around and turn their faces away from the cameras. Unlike [3], [4], [7] which require long sequences of past, present, and future frames, and hence are well suited for post-processing, our method is causal and therefore it can be used online. To deal with mixed speech signals, we exploit the sparsity of speech spectra and we propose a novel multiple speech-source localization method based on audio-visual data association implemented with a cohort of frequency-wise semi-supervised complex-Gaussian mixture models.

## III. Proposed Model

We start by introducing a few notations and definitions. Unless otherwise specified, upper-case letters denote random variables while lower-case letters denote their realizations. Vectors are in slanted bold, e.g. $\boldsymbol{X}, \boldsymbol{Y}$, while matrices are in bold, e.g. $\mathbf{X}, \mathbf{Y}$. We consider an image sequence that is synchronized with two microphone signals and let $t$ denote the time-step index of the audio-visual stream of data.

Let $N$ be the maximum number of visual objects, e.g. persons, available at any time $t$. Hence at $t$ we have at most $N$ persons with locations on the image plane $\mathbf{X}_{t}=$ $\left(\boldsymbol{X}_{t, 1}, \ldots, \boldsymbol{X}_{t, n}, \ldots, \boldsymbol{X}_{t, N}\right) \in \mathbb{R}^{2 \times N}$, where the observed

random variable $\boldsymbol{X}_{t, n} \in \mathbb{R}^{2}$ is the pixel location of person $n$ at $t$. We also introduce a set of binary (or control) variables $\boldsymbol{V}_{t}=\left(V_{t, 1}, \ldots V_{t, n}, \ldots V_{t, N}\right) \in\{0,1\}^{N}$ such that $V_{t, n}=1$ if person $n$ is visible at $t$ and $V_{t, n}=0$ if the person is not visible. Let $N_{t}=\sum_{n} V_{t, n}$ denote the number of visible persons at $t$. The time series $\mathbf{X}_{1: t}=\left\{\mathbf{X}_{1}, \ldots, \mathbf{X}_{t}\right\}$ and associated visibility binary masks $\mathbf{V}_{1: t}=\left\{\boldsymbol{V}_{1}, \ldots, \boldsymbol{V}_{t}\right\}$ can be estimated using a multi-person tracker, i.e. Section IV.

We now describe the audio data. Without loss of generality, the audio signals are recorded with two microphones: let $\mathbf{Y}_{t}=\left(\boldsymbol{Y}_{t, 1}, \ldots, \boldsymbol{Y}_{t, k}, \ldots, \boldsymbol{Y}_{t, K}\right) \in \mathbb{C}^{F \times K}$ be a binaural spectrogram containing $F$ number of frequencies and $K$ number of frames. Each frame is a binaural vector $\boldsymbol{Y}_{t, k} \in$ $\mathbb{C}^{F}, 1 \leq k \leq K$. Binaural spectrograms are obtained in the following way. The short-time Fourier transform (STFT) is first applied to the left- and right-microphone signals acquired at time-step $t$ such that two spectrograms, $\mathbf{L}_{t}, \mathbf{R}_{t} \in \mathbb{C}^{F \times K}$ are associated with the left and right microphones, respectively. Each spectrogram is composed of $F \times K$ complex-valued STFT coefficients. The binaural spectrograms $\mathbf{Y}_{t}$ is composed of $F \times K$ complex-valued coefficients and each coefficients $Y_{t, k}^{f}, 1 \leq f \leq F$ and $1 \leq k \leq K$, can be estimated from the corresponding left- and right-microphone STFT coefficients $L_{t, k}^{f}$ and $R_{t, k}^{f}$, i.e. Section V. One important characteristic of speech signals is that they have sparse spectrograms. As explained below, this sparsity is explicitly exploited by the proposed speech-source localization method. Moreover, the microphone signals are obviously contaminated by background noise and by sounds emitted by other non-speech sources. Therefore, speech activity associated with each binaural spectrogram entry $Y_{t, k}^{f}$ must be properly detected and characterized with the help of a binary-mask matrix $\mathbf{A}_{t} \in\{0,1\}^{F \times K}$ : $A_{t, k}^{f}=1$ if the corresponding spectrogram coefficient contains speech, and $A_{t, k}^{f}=0$ if it does not contain speech. To summarize, the binaural spectrograms $\mathbf{Y}_{1: t}=\left\{\mathbf{Y}_{1}, \ldots, \mathbf{Y}_{t}\right\}$ and associated speech-activity masks $\mathbf{A}_{1: t}=\left\{\mathbf{A}_{1}, \ldots, \mathbf{A}_{t}\right\}$ characterize the audio observations.

## A. Speaker Diarization Model

We remind that the objective of our work is to assign speech signal to persons, which amounts to one-to-one spatiotemporal associations between several speech sources (if any) and one or several observed persons. For this purpose we introduce a time series of discrete latent variables, $\mathbf{S}_{1: t}=\left\{\boldsymbol{S}_{1}, \ldots, \boldsymbol{S}_{t}\right\} \in$ $\{0,1\}^{N \times t}$ where the vector $\boldsymbol{S}_{t}=\left(S_{t, 1}, \ldots, S_{t, n}, \ldots, S_{t, N}\right) \in$ $\{0,1\}^{N}$ has binary-valued entries such that $S_{t, n}=1$ if person $n$ speaks during the time-step $t$, and $S_{t, n}=0$ if person $n$ is silent. The temporal speaker diarization problem at hand can be formulated as finding a maximum-a-posteriori (MAP) solution, namely finding the most probable configuration of the latent state $\boldsymbol{S}_{t}$ that maximizes the following posterior probability distribution, also referred to as the filtering distribution:

$$
\hat{\boldsymbol{s}}_{t}=\underset{\boldsymbol{s}_{t}}{\operatorname{argmax}} P\left(\boldsymbol{S}_{t}=\boldsymbol{s}_{t} \mid \mathbf{x}_{1: t}, \mathbf{y}_{1: t}, \mathbf{v}_{1: t}, \mathbf{a}_{1: t}\right)
$$

We introduce the notation $\mathbf{U}_{t}=\left(\mathbf{X}_{t}, \mathbf{Y}_{t}, \mathbf{A}_{t}\right)$ for the observed variables, while the $\mathbf{V}_{t}$ are referred to as control variables. The filtering distribution (1) can be expanded as:

$$
\begin{aligned}
P\left(\mathbf{s}_{t} \mid \mathbf{u}_{1: t}, \mathbf{v}_{1: t}\right) & =\frac{P\left(\mathbf{u}_{t} \mid \mathbf{s}_{t}, \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right) P\left(\mathbf{s}_{t} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right)}{P\left(\mathbf{u}_{t} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right)} \\
& =\frac{P\left(\mathbf{u}_{t} \mid \mathbf{s}_{t}, \boldsymbol{v}_{t}\right) P\left(\mathbf{s}_{t} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right)}{P\left(\mathbf{u}_{t} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right)}
\end{aligned}
$$

We assumed that the observed variables $\mathbf{U}_{t}$ are conditionally independent of all other variables, given the speaking state $\boldsymbol{S}_{t}$ and control input $\mathbf{V}_{t} ; \boldsymbol{S}_{t}$ is conditionally independent of $\boldsymbol{S}_{1}, \ldots, \boldsymbol{S}_{t-2}$, given $\boldsymbol{S}_{t-1}$ and $\boldsymbol{V}_{t-1: t}$. Fig. 1 shows the graphical model representation of the proposed model.

The numerator of (2) is the product of two terms: the observation likelihood (left) and the predictive distribution (right). The observation likelihood can be expanded as:

$$
\begin{aligned}
P\left(\mathbf{u}_{t} \mid \mathbf{s}_{t}, \boldsymbol{v}_{t}\right)=\prod_{n=1}^{N}( & P\left(\mathbf{u}_{t} \mid S_{t, n}=1, V_{t, n}\right)^{s_{t, n}} \\
& \times P\left(\mathbf{u}_{t} \mid S_{t, n}=0, V_{t, n}\right)^{1-s_{t, n}})
\end{aligned}
$$

The predictive distribution (right hand side of the numerator of (2)) expands as:

$$
\begin{aligned}
& P\left(\mathbf{s}_{t} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right) \\
& \quad=\sum_{\mathbf{S}_{t-1}} P\left(\mathbf{s}_{t}, \mathbf{s}_{t-1} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right) \\
& \quad=\sum_{\mathbf{S}_{t-1}} P\left(\mathbf{s}_{t} \mid \mathbf{s}_{t-1}, \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right) P\left(\mathbf{s}_{t-1} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right) \\
& \quad=\sum_{\mathbf{S}_{t-1}} P\left(\mathbf{s}_{t} \mid \mathbf{s}_{t-1}, \boldsymbol{v}_{t}, \boldsymbol{v}_{t-1}\right) P\left(\mathbf{s}_{t-1} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t-1}\right) \\
& \quad=\sum_{\mathbf{S}_{t-1}}\left(\prod_{m=1}^{N} P\left(s_{t, m} \mid s_{t-1, m}, v_{t, m}, v_{t-1, m}\right)\right) \\
& \quad \times P\left(\mathbf{s}_{t-1} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t-1}\right)
\end{aligned}
$$

which is the product of the state transition probabilities (4) and of the filtering distribution at $t-1$ (5). We now expand the denominator of (2):

$$
\begin{aligned}
P\left(\mathbf{u}_{t} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right) & =\sum_{\mathbf{S}_{t}} P\left(\mathbf{u}_{t}, \mathbf{s}_{t} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right) \\
& =\sum_{\mathbf{S}_{t}} P\left(\mathbf{u}_{t} \mid \mathbf{s}_{t}, \mathbf{v}_{t}\right) P\left(\mathbf{s}_{t} \mid \mathbf{u}_{1: t-1}, \mathbf{v}_{1: t}\right)
\end{aligned}
$$

To summarize, the evaluation of the filtering distribution at an arbitrary time-step $t$ requires the evaluation of (i) the observation likelihood (3), i.e. Section VI, (ii) the state transition probabilities (4), i.e. Section III-B, (iii) the filtering distribution at $t-1$ (5), and of (iv) the normalization term (6). Notice that the number of possible state configuration is $2^{N}$ where $N$ is the maximum number of people. For small values of $N$ ( 2 to 6 persons), solving the MAP problem (1) is computationally efficient.

![img-0.jpeg](img-0.jpeg)

**Fig. 1: The Bayesian spatiotemporal fusion model used for audio-visual speaker diarization. Shaded nodes represent the observed variables, while unshaded nodes represent latent variables. Note that the visibility-mask variables V<sub>t,n</sub> although observed, they are treated as control variables. This model enables simultaneously speaking persons, which is not only a realistic assumption but also very common in natural dialogues and applications like for example HRI.**

### *B. State Transition Model*

Priors over the dynamics of the state variables in (4) exploit the simplifying assumption that the speaking dynamics of a person is independent of all the other persons. Several existing speech-turn models rely on non-verbal cues, such as filled pauses, breath, facial gestures, gaze, etc. [35], [36], and a speech-turn classifier can be built from annotated dialogues. The state transition model of [3] considers all possible transitions, e.g., speaking/non-speaking, visible/not-visible, etc., which results in a large number of parameters that need be estimated. These models cannot be easily extended when there are speech overlaps and one has to rely on features extracted from the data. To define the speaking transition priors P(s<sub>t,n</sub>|s<sub>t−1,n</sub>, v<sub>t,n</sub>, v<sub>t−1,n</sub>), we consider three cases: (i) person n visible at t−1 and visible at t, or v<sub>t,n</sub> = v<sub>t−1,n</sub> = 1 and in this case the transitions are parametrized by a self-transition prior q ∈ [0, 1] which models the probability to remain in the same state, either speaking or not speaking, (ii) person n not visible at t−1 and visible at t, or v<sub>t,n</sub> = 1, v<sub>t−1,n</sub> = 0, in this case, the prior to be either speaking or not speaking at t is uniform, and (iii) person n not visible at t, or v<sub>t,n</sub> = 0, v<sub>t−1,n</sub> = 1, in which case the prior not to be speaking is equal to 1. The following equation summarizes all these cases:

$$P(s_{t,n}|s_{t-1,n}, v_{t,n}, v_{t-1,n})$$

$$= v_{t,n}v_{t-1,n}q^{\delta_{s_{t-1,n}}(s_{t,n})}(1-q)^{1-\delta_{s_{t-1,n}}(s_{t,n})}$$

$$+ \frac{1}{2}(1-v_{t-1,n})v_{t,n} + (1-v_{t,n}) \delta_0(s_{t,n}), \tag{7}$$

where δ<sub>i</sub>(j) = 1 if i = j and δ<sub>i</sub>(j) = 0 if i ≠ j. Note that this does not consider the case of person n not visible at t−1 and at t for which the prior probability to be speaking is 0. In all our experiments we used q = 0.8.

The multiple-speaker tracking and diarization model proposed in this work only considers persons that are both seen and heard. Indeed, in informal scenarios there may be acoustic sources (speech or other sounds such as music) that are neither in the camera field of view, nor can they be visually detected and tracked. The proposed audio-visual association model addresses this problem, i.e. Section VI.

### IV. VISUAL OBSERVATIONS

We propose to use visual tracking of multiple persons in order to infer realizations of the random variables X<sub>1:t</sub> introduced above. The advantage of a multiple-person tracker is that it is able to detect a variable number of persons, possibly appearing and disappearing from the visual field of view, to estimate their velocities, and to track their locations and identities. Multiple object/person tracking is an extremely well studied topic in the computer vision literature and many methods with their associated software packages are available. Among all these methods, we chose the multiple-person tracker of [37]. In the context of our work, this method has several advantages: (i) it robustly handles fragmented tracks (due to occlusions, to the limited camera field of view, or simply to unreliable detections), (ii) it handles changes in person appearance, such as a person that faces the camera and then suddenly turns his/her head away from the camera, e.g. towards a speaker, and (iii) it performs online discriminative learning such that it can distinguish between similar appearances of different persons.

Visual tracking is implemented in the following way. Unupper-body detector [38] is used to extract bounding boxes of persons in every frame. This allows the tracker to initialize new tracks, to re-initialize lost ones, to avoid tracking drift, and to cope with a large variety of poses and resolutions. Moreover, an appearance model, based on the color histogram of a bounding box associated with a person upper body (head and torso), is associated with each detected person. The appearance model is updated whenever the upper-body detector returns a reliable bounding box (no overlap with another bounding box). We observed that upper-body detection is more robust than

face detection which yields many false positives. Nevertheless, in the context of audio-visual fusion, the face locations are important. Therefore, the locations estimated by the tracker, $\mathbf{X}_{1: t}$, correspond to the face centers of the tracked persons.

## V. AUDIO ObSERVATIONS

In this section we present a methodology for extracting binaural features in the presence of either a single audio source or several speech sources. We consider audio signals recorded with a binaural microphone pair. As already explained in Section III, the short-time Fourier transform (STFT) is applied to the two microphone signals acquired at time-slice $t$ and two spectrograms are thus obtained, namely $\mathbf{L}_{t}, \mathbf{R}_{t} \in \mathbb{C}^{F \times K}$.

## A. Single Audio Source

Let's assume that there is a single (speech or non-speech) signal emitted by an audio source during the time slice $t$. In the STFT domain, the relationships between the source-STFT spectrogram and microphone-STFT spectrograms are, for each frame $k$ and each frequency $f$ (for convenience we omit the time index $t$ ):

$$
\begin{aligned}
L_{k}^{f} & =H_{L, k}^{f} T_{k}^{f}+N_{L, k}^{f} \\
R_{k}^{f} & =H_{R, k}^{f} T_{k}^{f}+N_{R, k}^{f}
\end{aligned}
$$

where $\mathbf{T}=\left\{T_{k}^{f}\right\}_{k=1, f=1}^{k=K, f=F}$ is the unknown source spectrogram, $\mathbf{N}_{L}=\left\{N_{L, k}^{f}\right\}_{k=1, f=1}^{k=K, f=F}$ and $\mathbf{N}_{R}=\left\{N_{R, k}^{f}\right\}_{k=1, f=1}^{k=K, f=F}$ are the unknown noise spectrograms associated with the left and right channels, and $\mathbf{H}_{L}=\left\{H_{L, k}^{f}\right\}_{k=1, f=1}^{k=K, f=F}$ and $\mathbf{H}_{R}=$ $\left\{H_{R, k}^{f}\right\}_{k=1, f=1}^{k=K, f=F}$ are the unknown left and right acoustic transfer functions that are frequency-dependent. The above equations correspond to the general case of a moving sound source. However, if we assume that the audio source is static during the time slice $t$, i.e. the source emitter is in a fixed position during the time slice $t$, the acoustic transfer functions are time-invariant and only depend on the source position relative to the microphones. We further define binaural features, i.e. the ratio between the left and right acoustic transfer functions, $H_{L}^{f} / H_{R}^{f}$. Notice that we omitted the frame index because in the case of a static source, the acoustic transfer function is invariant over frames. Likewise the acoustic transfer function, the binaural features do not depend on $k$ and they only contain audio-source position information [33].

One can use the estimated cross-PSD (power spectral density) and auto-PSD to extract binaural features in the following way. The cross-PSD between the two microphones is [39], [40]:

$$
\begin{aligned}
\Phi_{L, R}^{f} & =\frac{1}{K} \sum_{k=1}^{K} L_{k}^{f} R_{k}^{f *} \\
& \approx \frac{1}{K} H_{L}^{f} H_{R}^{f *} \sum_{k=1}^{K}\left|T_{k}^{f}\right|^{2}+\frac{1}{K} \sum_{k=1}^{K} N_{L, k}^{f} N_{R, k}^{f *}
\end{aligned}
$$

where $A^{*}$ is the complex-conjugate of $A$ and it is assumed that the signal-noise cross terms can be neglected. If the noise signals are spatially uncorrelated then the noise-noise cross terms can also be neglected. The binaural feature vector at $t$ can be approximated with the ratio between the cross-PSD and autoPSD functions, i.e. the vector $\boldsymbol{Y}_{t}=\left(Y_{t}^{1}, \ldots Y_{t}^{f}, \ldots Y_{t}^{F}\right)^{\top}$ with entries

$$
Y_{t}^{f}=\frac{\Phi_{t, L, R}^{f}}{\Phi_{t, R, R}^{f}}
$$

## B. Multiple Speech Sources

We now consider the case of $P$ speakers $(P>1)$ that emit speech signals simultaneously (for convenience we omit again the time index $t$ )

$$
\begin{aligned}
L_{k}^{f} & =\sum_{p=1}^{P} H_{L, p}^{f} T_{p, k}^{f}+N_{L, k}^{f} \\
R_{k}^{f} & =\sum_{p=1}^{P} H_{R, p}^{f} T_{p, k}^{f}+N_{R, k}^{f}
\end{aligned}
$$

where $H_{L, p}^{f}$ and $H_{R, p}^{f}$ are the acoustic transfer functions from the speech-source $p$ to the left and right microphones, respectively. The STFT based estimate of the cross-PSD for each frequency-frame point $(f, k)$ is

$$
\Phi_{L, R, k}^{f}=L_{k}^{f} R_{k}^{f *}
$$

In order to further characterize simultaneously emitting speech signals, we exploit the well-known fact that speech signals have sparse spectrograms in the Fourier domain. Because of this sparsity it is realistic to assume that only one speech source $p$ is active at each frequency-frame point of the two microphone spectrograms (13) and (14). Therefore these spectrograms are composed of STFT coefficients that contain (i) either speech emitted by a single speaker, (ii) or noise. Using this assumption, the binaural spectrogram $\mathbf{Y}_{t}$ and associated binary mask matrix $\mathbf{A}_{t}$ can be estimated from the cross-PSD and auto-PSD in the following way. We start by estimating a binary mask for each frequency-frame point,

$$
A_{k}^{f}= \begin{cases}0 & \text { if } \max \left(\Phi_{L, L, k}^{f}, \Phi_{R, R, k}^{f}\right)<a \\ 1 & \text { otherwise }\end{cases}
$$

where $a$ is an adaptive threshold whose value is estimated based on noise statistics [41]. Then, we compute the binaural spectrogram coefficients for each frequency-frame point $(f, k)$ at time-slice $t$ as:

$$
Y_{t, k}^{f}= \begin{cases}\frac{\Phi_{t, L, R, k}^{f}}{\Phi_{t, R, R, k}^{f}} & \text { if } \quad A_{t, k}^{f}=1 \\ 0 & \text { if } \quad A_{t, k}^{f}=0\end{cases}
$$

It is important to stress that while these binaural coefficients are source-independent, they are location-dependent. This is to say that the binaural spectrogram only contains information

about the location of the sound source and not about the content of the source. This crucial property allows one to use different types of sound sources for training a sound source localizer and for predicting the location of a speech source, as explained in the next section.

## VI. AUDIO-VISUAL FUSION

In this section we propose an audio-visual spatial alignment model that will allow us to evaluate the observation likelihood (3). The proposed audio-visual alignment is weakly supervised and hence it requires training data. We start by briefly describing the audio-visual training data. The training data contain pairs of audio recordings and their associated directions. Let $\widetilde{\mathbf{W}}=\left\{\widetilde{\boldsymbol{W}}_{1}, \ldots, \widetilde{\boldsymbol{W}}_{m}, \ldots \widetilde{\boldsymbol{W}}_{M}\right\} \in \mathbb{C}^{F \times M}$ be a training dataset containing $M$ binaural vectors. Each binaural vector is extracted from its corresponding audio recording using the method described in Section V-A, i.e. $\widetilde{\boldsymbol{W}}_{m}=\left(\widetilde{W}_{m}^{1}, \ldots, \widetilde{W}_{m}^{f}, \ldots, \widetilde{W}_{m}^{F}\right)$ where each entry $\widetilde{W}_{m}^{f}$ is computed with (12).

Each audio sample in the training set consists of a whitenoise signal that is emitted by a loudspeaker placed at different locations, e.g. Fig. 2. The PSD of a white-noise signal is significant at each frequency thus: $\left|\widetilde{W}_{m}^{f}\right|^{2}>a>$ $0, \forall m \in[1 \ldots M], \forall f \in[1 \ldots F]$. A visual marker placed onto the loudspeaker allows to associate its pixel location with each sound direction, hence the $M$ source directions correspond to an equal number of pixel locations $\widetilde{\mathbf{X}}=$ $\left\{\widetilde{\boldsymbol{X}}_{1}, \ldots, \widetilde{\boldsymbol{X}}_{m}, \ldots \widetilde{\boldsymbol{X}}_{M}\right\} \in \mathbb{R}^{2 \times M}$. To summarize, the training data consist of $M$ pairs of binaural features and associated pixel locations: $\left\{\widetilde{\boldsymbol{W}}_{m}, \widetilde{\boldsymbol{X}}_{m}\right\}_{m=1}^{M}$.

We now consider the two sets of visual and auditory observations during the time slice $t$, namely $\mathbf{X}_{t}=\left(\boldsymbol{X}_{t, 1}, \ldots, \boldsymbol{X}_{t, n}, \ldots, \boldsymbol{X}_{t, N}\right) \in \mathbb{R}^{2 \times N}$, $\boldsymbol{V}_{t}=\left(V_{t, 1}, \ldots V_{t, n}, \ldots V_{t, N}\right) \in\{0,1\}^{N}, \mathbf{Y}_{t}=$ $\left(\boldsymbol{Y}_{t, 1}, \ldots, \boldsymbol{Y}_{t, k}, \ldots, \boldsymbol{Y}_{t, K}\right) \in \mathbb{C}^{F \times K}$ and $\mathbf{A}_{t} \in\{0,1\}^{F \times K}$. If person $n$, located at $\boldsymbol{X}_{t, n}$, is both visible and speaks at $t$ : the binaural features associated with the emitted speech signal depend on the person's location only, hence they must be similar to the binaural features of the training source emitting from the same location. This can be simply written as a nearest-neighbor search over the training-set of audio-source locations:

$$
\widetilde{\boldsymbol{X}}_{n}=\underset{m}{\operatorname{argmin}}\left\|\boldsymbol{X}_{t, n}-\widetilde{\boldsymbol{X}}_{m}\right\|^{2}
$$

and let $\widetilde{\boldsymbol{W}}_{n} \in \widetilde{\mathbf{W}}$ be the binaural feature vector associated with this location. Hence, the training pair $\left\{\widetilde{\boldsymbol{X}}_{n}, \widetilde{\boldsymbol{W}}_{n}\right\} \in \widetilde{\mathbf{X}} \times \widetilde{\mathbf{W}}$ can be associated with person $n$.

We choose to model that at any frequency $f \in[1 \ldots F]$, the likelihood of and observed binaural feature $Y_{t, k}^{f}$ follows the following complex-Gaussian mixture model (for convenience,
we omit the the time index $t$ )

$$
\begin{aligned}
& P\left(Y_{k}^{f} \mid \boldsymbol{\Theta}^{f}\right)= \\
& \quad \sum_{n=1}^{N} \pi_{n}^{f} \mathcal{N}_{c}\left(Y_{k}^{f} \mid \widetilde{W}_{n}^{f}, \sigma_{n}^{f}\right)+\pi_{N+1}^{f} \mathcal{N}_{c}\left(Y_{k}^{f} \mid 0, \sigma_{N+1}^{f}\right)
\end{aligned}
$$

where $\mathcal{N}_{c}(x \mid \mu, \sigma)=(\pi \sigma)^{-1} \exp (-|x-\mu|^{2} / \sigma), \quad x \in \mathbb{C}$ is the complex-normal distribution and $\boldsymbol{\Theta}^{f}$ is the set of realvalued model parameters, namely the priors $\left\{\pi_{n}^{f}\right\}_{n=1}^{N+1}$ with $\sum_{n=1}^{N+1} \pi_{n}^{f}=1$, and the variances $\left\{\sigma_{n}^{f}\right\}_{n=1}^{N+1}$. This model states that the binaural feature $Y_{k}^{f}$ is either generated by one of the $N$ persons, located at $\widetilde{\boldsymbol{X}}_{n}, 1 \leq n \leq N$, hence it is an inlier generated by a complex-normal mixture model with means $\widetilde{W}_{n}^{f}, 1 \leq n \leq N$, or is emitted by an unknown sound source, hence it is an outlier generated by a zero-centered complexnormal distribution with a very large variance $\sigma_{N+1}^{f} \gg \sigma_{n}$.

The parameter set $\boldsymbol{\Theta}^{f}$ of (19) can be easily estimated via a simplified variant of the EM algorithm for Gaussian mixtures: the algorithm alternates between E-step that evaluates the posterior probabilities $r_{k n}^{f}=P\left(z_{k}^{f}=n \mid Y_{k}^{f}\right), z_{k}^{f}$ is assignment varaible, $z_{k}^{f}=n$ means $Y_{k}^{f}$ is generated by component $n$ :
$r_{k n}^{f}= \begin{cases}\frac{1}{C} \pi_{n}^{f} \mathcal{N}_{c}\left(Y_{k}^{f} \mid \widetilde{W}_{n}^{f}, \sigma_{n}^{f}\right) & \text { if } 1 \leq n \leq N \\ \frac{1}{C} \pi_{N+1}^{f} \mathcal{N}_{c}\left(Y_{k}^{f} \mid 0, \sigma_{N+1}^{f}\right) & \text { if } n=N+1\end{cases}$
where $C=\sum_{i=1}^{N} \pi_{i}^{f} \mathcal{N}_{c}\left(Y_{k}^{f} \mid \widetilde{W}_{i}^{f}, \sigma_{i}^{f}\right)+\pi_{N+1}^{f} \mathcal{N}_{c}\left(Y_{k}^{f} \mid 0, \sigma_{N+1}^{f}\right)$,
and M-step that estimates the variances and the priors:

$$
\begin{aligned}
\sigma_{n}^{f} & =\frac{\sum_{k=1}^{K} A_{k}^{f} r_{k n}^{f}\left|Y_{k}^{f}-\widetilde{W}_{n}^{f}\right|^{2}}{\sum_{k=1}^{K} A_{k}^{f} r_{k n}^{f}} \quad \forall n, 1 \leq n \leq N \\
\pi_{n}^{f} & =\frac{\sum_{k=1}^{K} A_{k}^{f} r_{k n}^{f}}{\sum_{k=1}^{K} A_{k}^{f}} \quad \forall n, 1 \leq n \leq N+1
\end{aligned}
$$

The algorithm can be easily initialized by setting all the priors equal to $\frac{1}{N+1}$ and by setting all the variances equal to a positive scalar $\sigma$. Because the component means are fixed, the algorithm converges in only a few iterations.

Based on these results one can evaluate (3), namely the speaking probability of person $n$ located at $\boldsymbol{X}_{n}$ : the probability that a visible person either speaks:

$$
P\left(\mathbf{U}_{t} \mid S_{t, n}=1, V_{t, n}=1\right)=\frac{\sum_{f=1}^{F} \sum_{k=1}^{K} A_{t, k}^{f} r_{t, k n}^{f}}{\sum_{f=1}^{F} \sum_{k=1}^{K} A_{t, k}^{f}}
$$

or is silent:

$$
P\left(\mathbf{U}_{t} \mid S_{t, n}=0, V_{t, n}=1\right)=1-P\left(\mathbf{U}_{t} \mid S_{t, n}=1, V_{t, n}\right)
$$

## VII. AUDIO-VISUAL DATASETS

In this section we describe the audio-visual datasets that are used to test the proposed method and to compare it with several state-of-the-art methods. We start by describing a novel dataset that was purposively gathered and recorded

![img-1.jpeg](img-1.jpeg)

Fig. 2: The AVDIAR dataset is recorded with a camera-microphone setup. (a) To record the training data, a loud-speaker that emits white noise was used. A visual marker onto the loud-speaker (circled in green) allows to annotate the training data with image locations, each image location corresponds to a loud-speaker direction. (b) The image grid of loud-speaker locations used for the training data. (c) A typical AVDIAR scenario (the camera-microphone setup is circled in green).

to encompass a wide number of multiple-speaker scenarios, e.g. speakers facing the camera, moving speakers, speakers looking at each other, etc. This novel dataset is referred to as **AVDIAR**.<sup>2</sup>

In order to record both training and test data we used the following camera-microphone setup. A color camera is rigidly attached to an acoustic dummy head. The camera is a PointGrey Grasshopper3 unit equipped with a Sony Pregius IMX174 CMOS sensor of size 1.2" × 1". The camera is equipped with a Kowa 6 mm wide-angle lens and it delivers 1920×1200 color pixels at 25 FPS. This camera-lens setup has a horizontal × vertical field of view of 97° × 80°.

For the audio recordings we used a binaural Senheiser MKE 2002 dummy head with two microphones plugged into its left and right ears, respectively. The original microphone signals are captured at 44100 Hz, we have downsampled them to 16000 Hz. The STFT, implemented with a 32 ms Hann window and 16 ms shifts between consecutive windows, is then applied separately to the left and right microphone signals. Therefore, there are 512 samples per frame and the audio frame rate is approximatively 64 FPS. Each audio frame consists of a vector composed *F* = 256 Fourier coefficients covering frequencies in the range 0 Hz − 8 kHz.

The camera and the microphones are connected to a single PC and they are finely synchronized using time stamps delivered by the computer's internal clock. This audio-visual synchronization allows us to align the visual frames with the audio frames. The time index *t* corresponds to the visual-frame index. For each *t* we consider a spectrogram of length *K* = 25 frames, or a time slice of 0.4 s, hence there is an overlap between the spectrograms corresponding to consecutive time indexes.

The training data were recorded by manually moving a loudspeaker in front of the camera-microphone unit e.g. Fig. 2. A visual marker placed at the center of the loudspeaker enables recording of audio signals with their associated pixel positions in the image plane. The loudspeaker is roughly moved in two planes roughly parallel to the image plane, at 1.5 m and 2.5 m, respectively. For each plane we record 800 positions lying on a uniform 20×40 grid that covers the entire field of view of the camera, hence there are *M* = 1600 training samples. The training data consists of 1 s of white-noise (WN) signals. Using the STFT we therefore obtain two WN spectrograms of size 256×64, corresponding to the left and right microphones, respectively. These two spectrograms are then used to compute binaural feature vectors, i.e. Section V-A (one feature vector for each loud-speaker position) and hence to build a training dataset of audio recordings and their associated image locations {**Ŵ**, **X̂**} = {(**Ŵ**<sub>1</sub>, **X̂**<sub>1</sub>), ..., (**Ŵ**<sub>m</sub>, **X̂**<sub>m</sub>), ..., (**Ŵ**<sub>M</sub>, **X̂**<sub>M</sub>)}, i.e. Section VI.

Similarly we gathered a test dataset that contains several scenarios. Each scenario involves participants that are either static and speak or move and speak, in front of the camera-microphone unit at distance varying between 1.0 m and 3.5 m. In an attempt to record natural human-human interactions, participants were allowed to wonder around the scene and to interrupt each other while speaking. We recorded the following scenario categories, e.g. Fig. 3:

- **Static participants facing the camera.** This scenario can be used to benchmark diarization methods requiring the detection of frontal faces and of facial and lip movements.
- **Static participants facing each other.** This scenario can be used to benchmark diarization methods that require static participants not necessarily facing the camera.
- **Moving participants.** This is a general-purpose scenario that can be used to benchmark diarization as well as audio-visual person tracking.

In addition to the **AVDIAR** dataset, we used three other datasets, e.g. Fig. 4. They are briefly described as follows:

- The **MVAD** dataset described in [5]. The visual data were recorded with a Microsoft Kinect sensor at 20 FPS,<sup>3</sup> and the audio signals were recorded with a linear array of

<sup>2</sup>https://team.inria.fr/perception/avdiar/

TABLE I: Scenarios available with the AVDIAR dataset.


![img-2.jpeg](img-2.jpeg)

Fig. 3: Examples of scenarios in the AVDIAR dataset. For the sake of varying the acoustic conditions, we used three different rooms to record this dataset.

omnidirectional microphones sampled at 44100 Hz. The recorded sequences are from 40 s to 60 s long and contain one to three participants that speak in Portuguese. The speech and silence segments are 4 s to 8 s long. Since the diarization method proposed in [5] requires frontal faces, the participants are facing the camera and remain static through all the recordings.

- The AVASM dataset contains both training and test recordings used to test the single and multiple speaker localization method described in [33]. The recording setup is similar to the one described above, namely a binaural acoustic dummy head with two microphones plugged into its ears and a camera placed underneath the head. The images and the audio signals were captured at 25 FPS and 44100 Hz, respectively. The recorded sequences contain up to two participants that face the camera and speak simultaneously. In addition, the dataset has audio-visual alignment data collected in a similar fashion as the AVDIAR dataset.
- The AV16P3 dataset is designed to benchmark audiovisual tracking of several moving speakers without taking diarization into account [42]. The sensor setup used for these recordings is composed of three cameras attached to the room ceiling, and two circular eight-microphone arrays. The recordings include mainly dynamic scenarios, comprising a single, as well as multiple moving speakers. In all the recordings there is a large overlap between the speaker-turns.

These datasets contain a large variety of recorded sce-narios, aimed at a wide range of application. e.g. formal and informal interaction in meetings and gatherings, human-computer interaction, etc. Some of the datasets were not purposively recorded to benchmark diarization. Nevertheless they are challenging because they contain a large amount of overlap between speakers, hence they are well suited to test the limits and failures of diarization methods. Unlike recordings of formal meetings, which are composed on long single-speech segments with almost no overlap between the participants, the above datasets contain the following challenging situations e.g. Table I:

- The participants do not always face the cameras, moreover, they turn their heads while they speak or listen;
- The participants, rather then being static, move around and hence the tasks of tracking and diarization must be finely intertwined;
- In informal meetings participants interrupt each other and hence not only that there is no silence between speech segments, but the speech segments overlap each other, and

- Participants take speech turns quite rapidly which results in short-length speech segments, which makes audiovisual temporal alignment quite challenging.
![img-3.jpeg](img-3.jpeg)

Fig. 4: Example from different datasets. The MVAD dataset (top) contains recordings of one to three persons that always face the camera. The AVASM (middle) was design to benchmark audio-visual sound-source localization with two simultaneously speaking persons or with a moving speaker. The AV16P3 dataset (bottom) contains recordings of simultaneously moving and speaking persons.

## VIII. EXPERIMENTAL EVALUATION

## A. Diarization Performance Measure

To effectively benchmark our model with state-of-the art methods, we use the diarization error rate (DER) to quantitatively measure the performance: smaller the DER value, better the performance. DER is defined by the NIST-RT evaluation testbed, ${ }^{4}$ and corresponds to the percentage of audio frames that are not correctly assigned to one or more speakers, or to none of them in case of a silent frame. DER consists of the composition of the following measurements:

- False-alarm error, when speech has been incorrectly detected;
- Miss error, when a person is speaking but the method fails to detect the speech activity, and
- Speaker-labeling error, when a person-to-speech association does not correspond to the ground truth.

To compute DER, the MD-EVAL software package of NISTRT is used, setting the forgiveness collar to a video frame of e.g. 40 ms for 25 FPS videos.

## B. Diarization Algorithms and Setup

We compared our method with four methods: [43], [5], [21], and [32]. These methods are briefly explained below:

- Vijayasenan et al. [43] (DiarTK) use audio information only. DiarTK allows the user to incorporate a large number of audio features. In our experiments and comparisons we used the following features: mel-frequency cepstral

[^0]coefficients (MFCC), frequency-domain linear prediction (FDLP), time difference of arrival (TDOA), and modulation spectrum (MS). Notice that TDOA features can only be used with static sound-sources, hence we did not use TDOA in the case of moving speakers.

- Minotto et al. [5] learn an SVM classifier based on based on labeled audio-visual features. Sound-source localization provides horizontal sound directions which are combined with the output of a mouth tracker.
- Barzelay et al. [21] calculate audio-visual correlations based on extracting onsets from both modalities and on aligning these onsets. The method consists of detecting faces and on tracking face landmarks, such that each landmark yields a trajectory. Onset signals are then extracting from each one of these trajectory as well as from the microphone signal. These onsets are used to compare each visual trajectory with the microphone signal, and the trajectories that best match the microphone signal correspond to the active speaker. We implemented this method based on [21] since there is no publicly available code. Extensive experiments with this method revealed that frontal views of speakers are needed. Therefore, we tested this methods with all the sequences from the MVAD and AVASM datasets and on the sequences from the AVDIAR dataset featuring frontal images of faces.
- Gebru et al. [32] track the active speaker, provided that participants take speech turns with no signal overlap. Therefore, whenever two persons speak simultaneously, this method extracts the dominant speaker.

Additionally, we used the following multiple sound-source localization methods:

- GCC-PHAT which detects the local maxima of the generalized cross-correlation method: we used the implementation from the BSS Locate Toolbox [26].
- TREM which considers a regular grid of source locations and selects the most probable locations based on maximum likelihood: we used the Matlab code provided by the authors, [27].
GCC-PHAT and TREM were used in conjunction with the proposed diarization method using the AVDIAR dataset as well as the MVAD and AV3P16 datasets.


## C. Results and Discussion

The results obtained with the MVAD, AVASM, AV16P3 and AVDIAR datasets are summarized in Table II, Table III, Table IV and Table V, respectively.

Overall, it can be noticed that the method of [21] is the least performing method. As explained above this method is based on detecting signal onsets in the two modalities and on finding cross-modal correlations based on onset coincidence. Unfortunately, the visual onsets are unable to properly capture complex speech dynamics. The DiarTK method of [43] is the second least performing method. This is mainly due to the fact that this method is designed to rely on long speech segments


[^0]:    ${ }^{4}$ http://www.nist.gov/speech/tests/rt/2006-spring/

with almost no overlap between consecutive segments. Whenever several speech signals overlap, it is very difficult to extract reliable information with MFCC features, since the latter are designed to characterize clean speech. DiarTK is based on clustering MFCC features using a Gaussian mixture model. Consider, for example, MFCC feature vectors of dimension 19, extracted from 20 ms -long audio frames, and a GMM with diagonal covariance matrices. If it is assumed that a minimum of 50 samples are needed to properly estimate the GMM parameters, speech segments of at least $50 \times 19 \times 20 \mathrm{~ms}$, or 19 s , are needed. Therefore it is not surprising that DiarTK performs poorly on all these datasets.

Table II shows that the method of [5] performs much better than DiarTK. This is not surprising, since the speech turns taken by the participants in the MVAD dataset are very brief. Minotto et al. [5] use a combination of visual features extracted form frontal views of faces (lip movements) and audio features (speech-source directions) to train an SVM classifier. The method fails whenever the participants do not face the camera, e.g. sequences Two12, Two13 and Two14, where participants purposely occlude their faces several times throughout the recordings. The method proposed in this paper in combination with TREM achieves the best results on almost all the tested scenarios. This is due to the fact that the audio-visual fusion method is capable of associating very short speech segments with one or several participants. However, the performance of our method, with either TREM or GCC-PHAT, drops down as the number of people increases. This is mainly due to the limited resolution of multiple sound-source localization algorithms (of the order of $10^{\circ}$ horizontally) and thus, it makes it difficult to disambiguate two nearby speaking/silent persons. Notice that tracking the identity of the participants is performed by visual tracking, which is a trivial task for most of these recordings, since participants are mostly static.

Table III shows the results obtained with the AVASM dataset. In these recordings the participants speak simultaneously, with the exception of the Moving-Speaker-01 recording. We do not report results obtained with DiarTK since this method yields non-meaningful performance with this dataset. The proposed method performs reasonable well in the presence of simultaneously speaking persons.

Table IV shows results obtained with the AV16P3 dataset. As with the AVASM dataset we were unable to obtain meaningful results with the DiarTK method. As expected the proposed method has the same performance as [32] in the presence of a single active speaker, e.g. seq11-1p-0100 and seq15-1p-0111. Nevertheless, the performance of [32] rapidly degrades in the presence of two and three persons speaking almost simultaneously. Notice that this dataset was recorded to benchmark audio-visual tracking, not diarization.

Table V shows the results obtained with the AVDIAR dataset. The content of each scenario is briefly described in Table I. The proposed method outperforms all other methods. It is also interesting to notice that our full method performs better than with either TREM or GCC-PHAT. This is due to the robust semi-supervised audio-visual association method

TABLE II: DER scores obtained with MVAD dataset (\%).


TABLE III: DER scores obtained with AVASM dataset (\%).


TABLE IV: DER scores obtained with AV16P3 dataset (\%).


TABLE V: DER scores obtained with AVDIAR dataset (\%).


![img-4.jpeg](img-4.jpeg)

Fig. 5: Results obtained on sequence Seq32-4P-S1M1. Visual tracking results (first row). The raw audio signal delivered by the left microphone and the speech activity region is marked with red rectangles (second row). Speaker diarization result (third row) illustrated with a color diagram: each color corresponds to the speaking activity of a different person. Annotated ground-truth diarization (fourth row).
![img-5.jpeg](img-5.jpeg)

Fig. 6: Results on sequence Seq12-3P-S2M1.
![img-6.jpeg](img-6.jpeg)

Fig. 7: Results on sequence Seq01-1P-S0M1.

proposed above. Fig. 5, Fig. 6, and Fig. 7 illustrate the audiovisual diarization results obtained by our method with three scenarios. ${ }^{5}$

## IX. Conclusions

We proposed an audio-visual diarization method well suited for challenging scenarios consisting of participants that either interrupt each other, or speak simultaneously. In both cases, the speech-to-person association problem is a difficult one. We proposed to combine multiple-person visual tracking with multiple speech-source localization in a principled spatiotemporal Bayesian fusion model. Indeed, the diarization process was cast into a latent-variable dynamic graphical model. We described in detail the derivation of the proposed model and we showed that, in the presence of a limited number of speakers (of the order of ten), the diarization formulation is efficiently solved via an exact inference procedure. Then we described a novel multiple speech-source localization method and a weakly supervised audio-visual clustering method.

We also introduced a novel dataset, AVDIAR, that was carefully annotated and that enables to assess the performance of audio-visual (or audio-only) diarization methods using scenarios that were not available with existing datasets, e.g. the participants were allowed to freely move in a room and to turn their heads towards the other participants, rather than always facing the camera. We also benchmarked our method with several other recent methods using publicly available datasets. Unfortunately, we were not able to compare our method with the methods of [2], [3] for two reasons: first, these methods require long speech segments (of the order of 10 s ), and second the associated software packages are not publicly available, which would have facilitated the comparison task.

In the future we plan to incorporate richer visual features, such as head pose estimation and head-pose tracking, in order to facilitate the detection of speech turns on the basis of gaze or of people that look at each other over time. We also plan to incorporate richer audio features, such as the possibility to extract speech signals emitted by each participant (sound-source separation) followed by speech recognition, and hence to enable not only diarization but also speech-content understanding. Another extension is to consider distributed sensors, wearable devices, or a combination of both, in order to be able to deal with more complex scenarios involving tens of participants [44], [45].
