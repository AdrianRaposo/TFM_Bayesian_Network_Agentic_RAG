# Non-invasive inference of information flow using diffusion MRI, functional MRI, and MEG 

Samuel Deslauriers-Gauthier, Isa Costantini, Rachid Deriche

## To cite this version:

Samuel Deslauriers-Gauthier, Isa Costantini, Rachid Deriche. Non-invasive inference of information flow using diffusion MRI, functional MRI, and MEG. Journal of Neural Engineering, 2020, 17 (4), pp.19. 10.1088/1741-2552/ab95ec . hal-02925937

## HAL Id: hal-02925937 <br> https://inria.hal.science/hal-02925937v1

Submitted on 31 Aug 2020

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Non-invasive inference of information flow using diffusion MRI, functional MRI, and MEG 

Samuel Deslauriers-Gauthier, Isa Costantini, and Rachid Deriche<br>Inria Sophia Antipolis Mediterranée, Université Côte d'Azur, France


#### Abstract

Objective: To infer information flow in the white matter of the brain and recover cortical activity using functional MRI, diffusion MRI, and MEG without a manual selection of the white matter connections of interest.

Approach: A Bayesian network which encodes the priors knowledge of possible brain states is built from imaging data. Diffusion MRI is used to enumerate all possible connections between cortical regions. Functional MRI is used to prune connections without manual intervention and increase the likelihood of specific regions being active. MEG data is used as evidence into this network to obtain a posterior distribution on cortical regions and connections.

Main results: We show that our proposed method is able to identify connections associated with the a sensory-motor task. This allows us to build the Bayesian network with no manual selection of connections of interest. Using sensory-motor MEG evoked response as evidence into this network, our method identified areas known to be involved in a visuomotor task. In addition, information flow along white matter fiber bundles connecting those regions was also recovered.

Significance: Current methods to estimate white matter information flow are extremely invasive, therefore limiting our understanding of the interaction between cortical regions. The proposed method makes use of functional MRI, diffusion MRI, and M/EEG to infer communication between cortical regions, therefore opening the door to the non-invasive exploration of information flow in the white matter.


## 1 Introduction

A modern representation of the brain is that of a network of interconnected and specialized nodes (Sporns et al., 2005). By exchanging information along the structural substrate, the nodes of the network achieve more general goals, eventually leading to human cognitive function. How structural connectivity shapes neural dynamics, or the structure-function relationship, has received

considerable attention (Honey et al., 2010; Goñi et al., 2012) but has largely focused on resting state. For simple tasks, even as rudimentary as visual grasping and finger tapping, the cortical regions involved have been extensively studied (Beurze et al., 2007; Gallivan and Culham, 2015; Turesky et al., 2018), but their specific interaction are still poorly understood. One difficulty is that methods to quantify information flow between cortical regions along the white matter structural connections are extremely invasive (Keller et al., 2014). The development of in vivo and non-invasive methods to quantify white matter information flow is therefore essential for our understanding of the most fundamental brain functions.

Because of their high temporal resolution, electroencephalography (EEG) and magnetoencephalography (MEG) provide invaluable insight into the temporal dynamics of neuronal activity. However, the temporal resolution of these modalities is offset by their limited spatial resolution. Conversely, functional magnetic resonance imaging (MRI) provides high spatial resolution maps of the blood-oxygen-level-dependent (BOLD) signal but with limited temporal resolution. The complementary nature of M/EEG and functional MRI has not been ignored and many methods have been proposed to combine them (Ahlfors and Simpson, 2004; Babiloni et al., 2004; Daunizeau et al., 2005; Auranen et al., 2009; Cottereau et al., 2015) or fuse them (Daunizeau et al., 2007). Independently or jointly, EEG, MEG, and functional MRI identify the cortical regions involved in a task, but do not take their white matter connections into account.

Diffusion MRI allows us to map structural brain connectivity in vivo and non-invasively via tractography (Jeurissen et al., 2019). At the temporal resolution of interest in task data, typically a few hundred milliseconds, this connectivity is static meaning the transfer of information along these connection cannot be imaged with diffusion MRI. Nonetheless, the white matter connections identified introduce delays in communication due to their length which are believed to be essential to brain dynamics (Deco et al., 2009). For example, the virtual brain makes use of delays introduced by structural connectivity in the coupling between neural mass models representing brain regions (Spiegler and Jirsa, 2013; Diaz-Parra et al., 2017). While the joint use of diffusion MRI and M/EEG has been proposed (Hutchisson et al., 2013), very few methods make use of the delays introduced by the white matter to inform M/EEG temporal dynamics. To our knowledge, only the work of Fukushima et al. (2015) in addition to our own (Deslauriers-Gauthier et al., 2017, 2019) have made use of white matter delays provided by diffusion MRI in the recovery of brain activity from M/EEG measurements. In our previous work, we proposed a new method called Connectivity Informed Maximum Entropy on the Mean (CIMEM) (DeslauriersGauthier et al., 2017, 2019) on the joint use of diffusion MRI and M/EEG to map white matter information flow. However, because of the complexity of the problem solved, the CIMEM model cannot accommodate all connections of the brain. This limitation required us to manually predefine connections of interest from external knowledge of the experimental paradigm. This strategy is error prone, introduces a bias, and is time consuming for the user. In addition, this restricts the use of our algorithm to well studied paradigms where the required

prior information is available.
In this work, we propose to extend CIMEM to include functional MRI as a way to automatically select connections of interest. This addition removes the manual selection step thus reducing the bias of the introduced priors. It also enables CIMEM to be used in experimental paradigms that are not well studied and where white matter connections of interest may not be available. The result is a non-invasive imaging pipeline that makes use of functional MRI, diffusion MRI, and M/EEG in addition to the indirect use of anatomical MRI used to define the parcellated regions used by CIMEM. This pipeline allows the inference of information flow in the white matter in addition to recovering cortical activity. To validate this new pipeline, we test it on 10 subjects of the Human Connectome Project (HCP) and present the inferred white matter information flow and cortical activity.

# 2 Theory 

The recovery of brain activity from MEG measurements is called the inverse problem. In this work, we use a distributed model (Baillet et al., 2001) where dipoles, which represent the activity of a small area, are distributed along the cortical surface. Because the number of dipoles (typically around 10 k ) is larger than the number of channels ( 64 to 300 ) by an order of magnitude, recovering the cortical activity from MEG measurements is an ill-posed problem. In particular, an infinite number of dipole activity configurations will fit the observed measurements equally well. The challenge of solving the inverse problem therefore revolves around identifying which of these infinitely many solutions best describes the true underlying brain activity. To identify the best candidate, many strategies have been proposed, including minimum-norm estimates, smoothness constraints, and sparsity. In our previous work, we proposed a novel strategy that makes use of connectivity information in addition to spatial regularity to select the most likely source configuration. In addition to identifying a single cortical activation map, this approach also allowed us to infer information flow in the white matter connections. For completeness, we briefly review the theory behind CIMEM here and present in detail how it can be modified to include functional MRI.

We use a distributed model and define $\boldsymbol{X} \in \mathbb{R}^{N \times T}$ as the vector that represents the cortical activity at $N$ locations on the cortical surface at $T$ time instants. Each element $x_{n, t}$ of $\boldsymbol{X}$ represents the activation intensity of the $n^{\text {th }}$ dipole at a time $t$. These dipoles are linearly related to the MEG measurements $\boldsymbol{M} \in \mathbb{R}^{M \times T}$ via the forward operator $\overline{\boldsymbol{G}} \in \mathbb{R}^{M \times N}$, that is

$$
\boldsymbol{M}=\overline{\boldsymbol{G}} \boldsymbol{X}
$$

The forward operator $\boldsymbol{G}$ is obtained by solving the forward problem, i.e. how dipoles project on MEG sensors, and is therefore assumed to be known. Throughout the manuscript, we will use a vectorized representation of Eq. (1)

$$
\boldsymbol{m}=\boldsymbol{G} \boldsymbol{x}
$$

where $\boldsymbol{m} \in \mathbb{R}^{M T}, \boldsymbol{x} \in \mathbb{R}^{N T}$, and $\boldsymbol{G} \in \mathbb{R}^{M T \times N T}$ is block diagonal with entries $\hat{\boldsymbol{G}}$. This representation allows us to drop time indices while still considering data windows of arbitrary sizes. Let $p(\boldsymbol{x})$ be the density of $\boldsymbol{x}$ providing the probability of observing a given cortical activation. As stated previously, the inverse problem consists in estimating the source activity $\boldsymbol{x}$ from the measurements $\boldsymbol{m}$, given the forward operator $\boldsymbol{G}$. The core of CIMEM strategy, which is an extension of the work of Amblard et al. (2004), can be summarized by the following optimization problem

$$
\underset{p(\boldsymbol{x}), \lambda_{0}, \boldsymbol{\lambda}}{\operatorname{minimize}} D_{K L}(p(\boldsymbol{x}))-\boldsymbol{\lambda}\left(\boldsymbol{m}-\boldsymbol{G} \int \boldsymbol{x} p(\boldsymbol{x}) d \boldsymbol{x}\right)-\lambda_{0}\left(1-\int d p(\boldsymbol{x})\right)
$$

where

$$
D_{K L}(p(\boldsymbol{x}))=\int_{-\infty}^{\infty} p(\boldsymbol{x}) \ln \frac{p(\boldsymbol{x})}{\mu(\boldsymbol{x})} d \boldsymbol{x}
$$

is the Kullback-Leibler divergence. In Eq. (2), the last term ensures that $p(\boldsymbol{x})$ is indeed a probability density function making $\lambda_{0}$ a scaling coefficient. The second term is a data fitting term and ensure the average of $p(\boldsymbol{x})$ explains the measurements. The first term is the distance between the density $p(\boldsymbol{x})$ and a reference law $\mu(\boldsymbol{x})$. This reference law must be defined beforehand and as such represents the prior information. To summarize, solving Eq. (2) corresponds to finding the density $p(\boldsymbol{x})$ that is closest to the priors $\mu(\boldsymbol{x})$ whose average fits the measurements $\boldsymbol{m}$. Interestingly, Eq. (2) is not tackled directly and we instead solve a dual convex problem whose minimization depends only on $\boldsymbol{\lambda}$ (Deslauriers-Gauthier et al., 2019). Given the optimal $\boldsymbol{\lambda}^{*}$ of the dual, the optimal density $p^{*}(\boldsymbol{x})$ in Eq. (2) can be computed directly.

To solve Eq. (2), the prior $\mu(\boldsymbol{x})$ must be defined and it is in this term that we will inject diffusion and functional MRI information. To do so, we first define the notion of cortical region state and connection state. Cortical regions are defined by grouping dipoles (columns of the forward operator) in a spatially coherent manner. How the grouping is defined is arbitrary, but the most common strategy is to use a brain atlas such as the one defined by Desikan et al. (2006). Each cortical region is assigned a state $S_{k}$ which describes its activity. Here, each region is given three possible states: inactive (0), positively active (1), or negatively active (2). When a region is inactive (in state 0 ), the intensities of the dipoles within this region follow a Gaussian distribution with zero mean and a covariance $\boldsymbol{\Sigma}$. On the other hand, when the region is active, the intensities follow a Gaussian distribution with a mean of $\pm \boldsymbol{\rho}$ and a covariance $\boldsymbol{\Sigma}$. The mean is positive if the region is positively active (in state 1) and negative if it is negatively active (in state 2). The region state variables are collected into a vector $\boldsymbol{S}=\left(S_{1}, \ldots, S_{N_{S}}\right)$ where $N_{S}$ is the number of regions. Similarly to cortical regions, each white matter connection is given a state $C_{k}$ which describes its activity: inactive (0) or active (1). When a region is active, it increases the likelihood of the regions it connects to be active (positively or negatively). The connection states are collected into a vector $\boldsymbol{C}=\left(C_{1}, \ldots, C_{N_{C}}\right)$ with $N_{C}$ the number of connections of the model. These region and connection states allow

us to define a brain state model given by

$$
d \mu(\boldsymbol{x}, \boldsymbol{S}, \boldsymbol{C})=\prod_{i=1}^{N_{C}} \varphi\left(C_{i}\right) \prod_{k=1}^{N_{S}} \pi\left(S_{k} \mid \boldsymbol{C}_{\gamma(k)}\right) d \mu\left(\boldsymbol{x}_{k} \mid S_{k}\right)
$$

where $\boldsymbol{x}_{k}$ is the intensity of the dipoles in region $k, d \mu\left(\boldsymbol{x}_{k} \mid S_{k}\right)$ is the likelihood of observing the intensities $\boldsymbol{x}_{k}$ given the region state $S_{k}, \pi\left(S_{k} \mid \boldsymbol{C}_{\gamma(k)}\right)$ is the likelihood of observing the region state $S_{k}$ given the state of the connections that reach it $\boldsymbol{C}_{\gamma(k)}$, and $\varphi\left(C_{i}\right)$ is the likelihood of observing the connection state $C_{i}$. Because dipole intensities depend only on region states and region states depend only on connection states, Eq (3) describes a Bayesian network. We are therefore able to marginalize the regions and connection states out the network and obtain our desired density $d \mu(\boldsymbol{x})$ to be used in Eq. (2).

The Bayesian network in Eq. (3) requires the explicit definition of $d \mu, \pi$, and $\varphi$. According to our previous definition of states on clusters, we propose to define $d \mu$ by

$$
d \mu\left(\boldsymbol{x}_{k} \mid S_{k}\right)= \begin{cases}A \exp \left(-\frac{1}{2} \boldsymbol{x}^{T} \boldsymbol{\Sigma}^{-1} \boldsymbol{x}\right) & \text { if } S_{k}=0 \\ A \exp \left(-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\rho})^{T} \boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\rho})\right) & \text { if } S_{k}=1 \\ A \exp \left(-\frac{1}{2}(\boldsymbol{x}+\boldsymbol{\rho})^{T} \boldsymbol{\Sigma}^{-1}(\boldsymbol{x}+\boldsymbol{\rho})\right) & \text { if } S_{k}=2\end{cases}
$$

with $A=(2 \pi)^{-N_{k} / 2}|\boldsymbol{\Sigma}|^{-1 / 2}$ with $N_{k}$ the number of dipoles in region $k$. In our previous work, no prior knowledge on the regions involved in the task was used and all regions were assumed to be in the inactive state. Here, we instead propose to define $\pi$ using functional MRI. Let $\alpha_{k}$ be the functional MRI activation of region $k$ normalized to be between 0 and 1 . We define the priors on the regions given the connections to be given by
$\pi\left(S_{k} \mid \boldsymbol{C}_{\gamma(k)}\right)= \begin{cases}\left(1-\alpha_{k}\right) / F_{k} & \text { if } S_{k}=0 \text { and } C_{i}=0 \forall i \in \gamma(k) \\ \alpha_{k} \beta / F_{k} & \text { if } S_{k}=1 \text { or } 2 \text { and } C_{i}=0 \forall i \in \gamma(k) \\ \alpha_{k} / F_{k} & \text { if } S_{k}=1 \text { or } 2 \text { and } C_{i}=1 \text { for at least one } i \in \gamma(k) \\ 0 & \text { otherwise }\end{cases}$
where the constant $F_{k}$ ensures the probabilities sum to one and $\beta \neq 0$ allows for a region to activate even if none of the connections that reach it are active. When a region has a high $\alpha_{k}$, it increases the likelihood of observing this region as active whereas low values of $\alpha_{s}$ encourage inactivity. It is important to note that a complete agreement is not expected between functional MRI and M/EEG (Ahlfors and Simpson, 2004; Geukes et al., 2013) because of their respective limitation in temporal and spatial resolution. Using the functional MRI information in the definition of the Bayesian network encourages solutions that are supported by the functional MRI data but does not explicitly constrain the solution space. To be selected, a configuration of sources must still fully explain the MEG measurements. To clarify, even regions with a low $\alpha_{k}$ that are judged inactive by the functional MRI data can still be recruited to explain the MEG data. This may affect regions that are very briefly involved in the task and thus contribute minimally to the functional MRI signals, but significantly

to the M/EEG signals. In addition, because the value of $\alpha_{k}$ is constant over a time window, the dynamics of the regions are wholly determined by the MEG dynamics. Finally, because no external information is available on the activity of connection, we set $\varphi\left(C_{i}\right)=0.5$.

The last step to fully characterise the brain state model $\mu(\boldsymbol{x}, \boldsymbol{S}, \boldsymbol{C})$ is to choose which of the connections are included in the model. As previously stated, including all connections identified using diffusion MRI leads to an intractable optimization problem. Instead of relying on prior knowledge of the experimental paradigm to filter connections, we suggest to include connections that are supported by the functional MRI activation. Let $\alpha_{i}$ and $\alpha_{j}$ be the functional MRI activation of regions $i$ and $j$. Connections between regions $i$ and $j$ at every time instants are added if both $\alpha_{i}$ and $\alpha_{j}$ are above a threshold $\tau$. The delay of these connections is given by $\ell_{i j} f_{s} / \nu$ where $\nu$ is the conduction speed of axons, $f_{s}$ is the sampling frequency of the data, and $\ell_{i j}$ is the length of the streamlines connecting regions $i$ and $j$.

The Bayesian network of Eq. (3) encodes the following:

- anatomical MRI information in the form of cortical regions and location of dipoles in the operator $\boldsymbol{G}$;
- diffusion MRI information in the form of possible connections between cortical regions and their associated delays via streamline length;
- the functional MRI information in the form of priors on cortical regions and pruning on structural connections to yield a tractable optimization problem.

The M/EEG data is not included directly in the model because it does not constitute a prior on the state of the brain, but is instead seen as evidence. Therefore, an accurate way to describe the CIMEM optimization problem in Eq. (2) is that it finds the posterior distribution of the brain state, given the M/EEG evidence. Indeed, it is possible to find the posterior likelihood that a connection was active (in a state 1) for every connection of the model and at every time. Similarly, it is possible to find the posterior likelihood that a region was active (in a state 1 or 2 ) for every region of the model and at every time. Finally, the mean of the optimal distribution $p^{*}(\boldsymbol{x})$ describes the cortical source activity that fit the M/EEG measurements. With the addition of functional MRI, CIMEM is a non-invasive imaging pipeline that makes use of anatomical MRI, functional MRI, diffusion MRI, and M/EEG to infer information flow in the white matter in addition to recovering cortical activity.

# 3 Methods 

### 3.1 Overview

We tested our new pipeline on the data of 10 subjects provided by the HCP which includes functional MRI, diffusion MRI, and MEG. The data of the 10

![img-0.jpeg](img-0.jpeg)

Figure 1: Schematic overview of the preprocessing pipeline of CIMEM. Acquired data is illustrated in green, preprocessing steps in blue, computed outputs in yellow, and red arrows indicate direct inputs to the CIMEM algorithm. WM: white matter, GM: Gray matter, CSF: Corticospinal fluid.
subjects is used to build a group prior model which is then used on individual subjects to perform the reconstruction. The main steps of the processing pipeline are cortical surface extraction and parcellation, functional MRI preprocessing, diffusion MRI tractography, MEG preprocessing and forward problem, and CIMEM processing. Each of these steps are outlined in the following sections. An overview of the pipeline is illustrated in Figure 1.

# 3.2 Cortical mesh and parcellation 

We used the white matter cortical mesh provided by the HCP which was extracted using FreeSurfer (Fischl, 2012) and includes the parcellation of the Desikan-Killiany atlas (Desikan et al., 2006).

### 3.3 Functional MRI

The functional MRI motor task of the HCP was adapted from the one developed by Buckner et al. (2011); Yeo et al. (2011). The subjects were presented with visual cues that asked them to either tap their fingers, toes, or to move their tongue. In each block of a movement type, the subjects were asked to perform 10 movements over 12 seconds following a 3 second cue.

Our functional MRI pipeline used the minimally preprocessed (Glasser et al., 2013) functional MRI ( 2 mm isotropic, $\mathrm{TR}=720 \mathrm{~ms}, \mathrm{TE}=33 \mathrm{~ms}$ ) which was

denoised using a paradigm free iterative method (Costantini et al., 2019) and projected onto the white matter surface. The advantage of using this approach over a more conventional general linear modelling is that it does not require prior knowledge of the experimental paradigm. This would allow us, for example, to use the same processing pipeline in the case of resting state functional MRI. Samples corresponding to the right hand movement were extracted and their temporal maximum selected, yielding a single cortical activation map for each subject. For each cortical region of the atlas, the activation was computed by first averaging the activation of all vertices within the region for each subject and then averaging across subjects. The results is a single value of $\alpha_{k}$, as described in Section 2, per region for all subjects. The functional MRI activity for subject 105923 and the recovered regions of interest are illustrated on the cortical surface in Figure 2. Activations were identified in the occipital and parietal lobes in addition to the precentral and postcentral regions corresponding to the visual, primary motor, and premotor areas commonly associated with visuomotor tasks.

# 3.4 Tractography 

The tractography pipeline made use of the 7 T diffusion MR images provided by the HCP. Briefly, 286 volumes were acquired on two shells with $\mathrm{b}=$ 1000 and $2000 \mathrm{~s} / \mathrm{mm}^{2}\left(\mathrm{TE}=71 \mathrm{~ms}, \mathrm{TR}=7.0 \mathrm{~s}\right)$. For each shell, 128 diffusion weighted images, corresponding to 64 unique gradients directions with reversed phase encoding, were acquired in addition to $15 \mathrm{~b}=0 \mathrm{~s} / \mathrm{mm}^{2}$ images. A detailed description of the acquisition protocol is provided by Vu et al. (2015).

The tractography processing pipeline was implemented using the MRtrix3 software (Tournier et al., 2019). The T1 and T2 weighted images were used to segment the brain into cortical gray matter, sub-cortical gray matter, white matter, and corticospinal fluid (Smith et al., 2012; Smith, 2002; Zhang et al., 2001; Patenaude et al., 2011; Smith et al., 2004). Using this segmentation, a multi-shell response function was estimated for each tissue type (Jeurissen et al., 2014). The fibre orientation distributions for each voxel was estimated using spherical deconvolution (Tournier et al., 2004) with a maximum spherical harmonic order of 8 . Finally, 2 million streamlines were generated by seeding at the white matter gray matter interface and performing probabilistic anatomically constrained tractography with backtracking (Tournier et al., 2010; Smith et al., 2012). All diffusion MRI connections were enumerated by grouping streamlines reaching the same cortical regions. Out of all these connections, only those reaching regions with a functional MRI activation above $\tau=0.7$ were kept. This value was choosen because it was the best threshold to obtain a maximum of connections that generate a tractable optimization problem with our implementation. The streamlines for subject 105923 corresponding to connections between regions identified by the threshold are illustrated in Figure 3. The average streamline length for example connections is also noted. Overall, the connection length varies between 38 and 172 mm .

# 3.5 MEG 

The motor task MEG data provided by the HCP (Larson-Prior et al., 2013) was acquired on a whole head MAGNES 3600 (4D NeuroImaging, San Diego, CA) with 248 magnetometer channels and sampled at 2 kHz . The MEG paradigms are matched to those of the task functional MRI, therefore allowing us to use functional MRI as a prior in the MEG reconstruction. Briefly, the subjects were asked to perform a hand or foot movement following a visual cue which indicated the limb and side to use. Each task was repeated 8 times with each task block containing 10 trials for a total of 80 repetitions per task.

Our MEG processing pipeline was implemented using MNE-Python (Gramfort et al., 2013) and using MNE-HCP ${ }^{1}$ for data access. To generate cortical sources, the white matter surface was downsampled to 4098 sources per hemisphere using a recursively subdivided octahedron. The inner skull, outer skull, and outer skin surfaces were extracted using the FreeSurfer watershed algorithm (Ségonne et al., 2004). The orientation of the dipoles was fixed perpendicular to the cortical surface and the forward solution was computed using a one-layer model with a conductivity of $0.3 \mathrm{~S} / \mathrm{m}$. The MEG data was cleaned by removing bad channels and artifacts using independent component analysis. For each trial, 400 ms of data was extracted following the visual cue and averaged across conditions. The resulting evoked responses were low-pass filtered at 100 Hz and downsampled to 200 Hz . The evoked fields for the right hand movement of subject 105923 are illustrated in Figure 4.

### 3.6 CIMEM

As described in Section 2, a cluster variable $S_{k}$ was added to the CIMEM Bayesian network for each cluster of the parcellation at every time instant. For each of the selected connections and at every time instant, a variable $C_{k}$ was added to the network. The parameter $\beta$ as set to 0.1 , making it 10 times less likely for a connection to activate independently rather than following an active connection. Finally, the conduction speed of actions was set to $6 \mathrm{~m} / \mathrm{s}$ (Hursh, 1939) making the delay of connections a function of their length only.

## 4 CIMEM Results

As discussed in Section 3.3, the functional MRI priors obtained for the right hand movement task are illustrated in Figure 2 along with the cortical parcellation. After thresholding, the regions selected to filter connections include the visual areas (pericalcarine, lateral occipital, cuneus), the sensory-motor and primary motor areas (postcentral), and premotor area (precentral) as expected from a visuomotor task. The connections used to build the CIMEM network, which were identified by the functional MRI and added to the network, are those

[^0]
[^0]:    ${ }^{1}$ https://github.com/mne-tools/mne-hcp

illustrated in Figure 3. The final CIMEM Bayesian network contained a total of 5670 cluster variables and 2135 connection variables.

The recovered cortical activation obtained with CIMEM are illustrated in Figure 4 for a representative subject (105923). For comparison, the reconstruction obtained without functional and diffusion MRI priors is also illustrated. This corresponds to the assumption of independent clusters as in Amblard et al. (2004) and serves to illustrate how the new priors guide the solution. Using the priors, more focal activity is recovered in the left lateral occipital cortical region at 100 ms after the visual stimulus. At 140 ms , a stronger activation of the postcentral region, corresponding to the motor cortex, is recovered using functional and diffusion MRI priors. For both methods, cortical activity is recovered in the temporal lobe even if this region is not strongly activated by the functional MRI priors. This highlights that, although the addition of functional MRI priors guides the recovered activity, it does not force or preclude the activation of specific cortical areas. It should also be noted that both solutions fit the MEG data equally well due to the ill-posedness nature of the problem and MEG alone would be unable to differentiate between them. The solution using functional and diffusion MRI, however, is closer to the functional MRI measurements and uses activation delays that are consistent with the underlying white matter connections.

The recovered information flow for a representative subject is illustrated in Figure 5. In this diagram, each row corresponds to a cortical region with the color of the circles indicating the posterior probability of being active at a given time. Lines connecting circles indicate an active connection between two cortical regions. The distance between the start and end point of a line on the abscissa gives the temporal delay of the corresponding connection. First, we notice that the functional and diffusion MRI priors produce a sparse solution in terms of active cortical regions while still explaining the same MEG data. It should be noted that sparsity is not a constraint of the model, but a result of the priors introduced. We also observe that, using diffusion MRI connections, information flow was detected between the lateral occipital, inferior partietal, and postcentral regions. All of these regions are well known to be implicated in visual grasping, motor planning, and finger tapping (Beurze et al., 2007; Turesky et al., 2018). Interestingly, white matter activity is concentrated in the visual system 100 ms after the stimulus, in both the visual and motor regions at 140 ms , and in the motor and premotor areas 260 ms after the stimulus.

# 5 Discussion 

We showed that functional MRI, diffusion MRI, and MEG can be combined to produce a realistic forward model of brain activity and this model can be inverted to estimate cortical activity and infer information flow in the white matter at a resolution of a few milliseconds. This model leverages both the high spatial resolution of functional MRI and the high temporal resolution of MEG. In addition to providing the cortical activations produced by other M/EEG in-

verse methods it also maps information flow of the white matter. In comparison to our previous work, the addition of functional MRI allowed us to select the white matter connections of interest with no explicit knowledge of the experimental paradigm. To our knowledge, the approach we propose is the first and unique method that allows the non-invasive recovery of information flow in the white matter.

Our results on HCP data showed that the solutions found by using functional and diffusion MRI identify fewer cortical regions while still explaining the M/EEG data. It is important to recall that because there are fewer MEG measurements than cortical sources to estimate, recovering brain activity from MEG measurements is an ill-posed problem. As a direct consequence, infinitely many source configurations will explain the observed measurements. To resolve this ambiguity, our approach makes use of prior information from other modalities to select a single source configuration which is closest to the priors. In doing so, our approach also estimates white matter information flow, understood to be the posterior likelihood of a connection to be active, given the MEG measurements. With the addition of functional MRI, the information flow between cortical regions known to be involved in visuomotor tasks were identified with no manual selection of these regions of interest.

An important parameter of the proposed strategy to automatically select the white matter connections of interest is the thresholding parameter $\tau$. If a high value is used, some connections of interest may be removed thus leading to an incomplete connectivity landscape. In practice, the value is determined by the efficiency of the implementation and the available computational capabilities. In our case, using a value of 0.7 included approximately 2000 white matter connections. As we further improve our implementation, a lowering of the threshold may lead to enhancement of the results by the inclusion of previouly missed connections.

A possible improvement of the current work is modify the model to symmetrically use the functional MRI, diffusion MRI, and MEG information. Indeed, the proposed model uses the information asymmetrically in the sense of Daunizeau et al. (2007), meaning that functional and diffusion MRI are used as prior information into the MEG inverse problem; all data sets are not treated as equivalent. To improve on this situation, it may be possible to derive a single forward model encompassing all three modalities which would allow a symmetrical use of the data and a joint analysis, similarly to the work of Daunizeau et al. (2007) but extended to include connectivity information.

# Acknowledgements 

This work has received funding from the European Research Council (ERC)under the European Unions Horizon 2020 research and innovation program(ERC Advanced Grant agreement No 694665 : CoBCoM - Computational Brain Connectivity Mapping).

Data were provided by the Human Connectome Project, WU-Minn Consor-

tium (Principal Investigators: David Van Essen and Kamil Ugurbil; 1U54MH091657) funded by the 16 NIH Institutes and Centers that support the NIH Blueprint for Neuroscience Research; and by the McDonnell Center for Systems Neuroscience at Washington University.
