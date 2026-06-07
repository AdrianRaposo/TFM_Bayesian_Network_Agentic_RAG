# NIH Public Access 

## Author Manuscript

C Comput Biol Med. Author manuscript; available in PMC 2011 December 1.
Published in final edited form as:
Comput Biol Med. 2011 December ; 41(12): 1156-1165. doi:10.1016/j.compbiomed.2011.04.011.

## Effective connectivity analysis of fMRI and MEG data collected under identical paradigms

Sergey M. Plis ${ }^{\mathrm{a}, \mathrm{b}}$, Michael P. Weisend ${ }^{\mathrm{a}}$, Eswar Damaraju ${ }^{\mathrm{a}}$, Tom Eichele ${ }^{\mathrm{d}}$, Andy Mayer ${ }^{\mathrm{a}}$, Vincent P. Clark ${ }^{\mathrm{a}}$, Terran Lane ${ }^{\mathrm{b}}$, and Vince D. Calhoun ${ }^{\mathrm{a}, \mathrm{c}}$<br>${ }^{a}$ The Mind Research Network, USA<br>${ }^{\text {b }}$ Computer Science, The University of New Mexico, USA<br>${ }^{\text {c }}$ Electrical and Computer Engineering, The University of New Mexico, USA<br>${ }^{\text {d }}$ Biological and Medical Psychology, University of Bergen, Norway


#### Abstract

Estimation of "effective connectivity" can potentially reveal valuable information about organization of brain networks. It is usually applied to the functional data of a single modality. In this paper we show why that may be dangerous and lead to incorrect conclusions about "effective connectivity". As a tool to estimate the connectivity we use Bayesian networks. We analyze structures of estimated "effective connectivity" networks using aggregate statistics from the field of complex networks. Our study is conducted on functional MRI and magnetoencephalography data collected from the same subjects under identical paradigms.


## 1. Introduction

The morphology and connectivity of neurons define the functional properties of the brain. A combination of short-, mid- and long-range interactions among neurons forms multiscale networks that give rise to high level cognitive functions [1, 2].

Anatomical neuronal connections are extensively studied at all scales of brain's interaction network. Initially, in vitro studies provided the most of information. Subsequent advent of noninvasive imaging methods, such as DTI [3], lead to an explosion of the number of in vivo connectivity studies $[4,5]$ and equipped large mapping efforts, such as the human connectome project [6], with essential tools.

Noninvasive studies of mid- and long-range connections as well as invasive studies of dendritic connections provide information about structural networks in the brain. These connections form a "supporting fabric" for dynamically changing processing networks. Interaction within and among these changing function induced networks also supports high level cognitive processing. Some of these network-circuits are surprisingly stable under equivalent conditions in single-subject as well as in group studies [7, 8].

Functional neuroimaging provides a way to look at these networks by tracking different aspects of dynamical brain behavior [9-11]. Among many currently used functional modalities we have focused this study on magnetoencephalography (MEG) and functional magnetic resonance imaging (fMRI). The main advantages of functional neuroimaging in general and of the two selected modalities is in providing spatiotemporal data. These data inform us of brain dynamics at different regions and with different spatiotemporal resolution.

Among available approaches to extracting neuronal function-induced networks, we are interested in those that result in a graphical model representing regions of interest (ROI) as graph vertices and their connections as edges [12]. A widely accepted approach to extracting such models from functional data involves obtaining a correlation (mutual information, spectral coherence or others) matrix, thresholding its values and using the result as the adjacency matrix of the graph representing the data. This approach only extracts the second order pairwise interactions or "functional connectivity", whereas causal relationships involving groups of ROIs acting together ("effective connectivity") require more involved approaches [13].

The definition of "effective connectivity" usually involves extraction of causal relationships among ROIs as well as going beyond second order measures to multiple potentially nonlinear interactions. Causality in its strong sense is a difficult concept to handle and it often requires intervention analysis for estimation [14]. However, it is possible to estimate graphical models having causal interpretations from data and prior knowledge [15] or to resort to a specific definition of causality (cite Granger causality initial paper and Roenbroek's neuroimaging application paper). Multiway interactions with a possible causal interpretation are also modeled by Bayesian networks (BN) developed specifically for reasoning about "effective connectivity" in the field of artificial intelligence [16, 17].

The more traditional approaches to "effective connectivity" estimation in neuroimaging such as dynamic causal modeling [15] have their limitations restricting interactions among variables to bilinear, and posing difficulties for full brain graphical model structure estimation. In this paper we use Bayesian networks with multinomial random variables as our model of "effective connectivity" and a structure learning algorithm to recover the graphical model from the data. Recent developments in structure learning algorithms [18] allow us to estimate structures of networks covering all cortical ROIs.

Estimated "effective connectivity" can be used to compare the groups of subjects (such as patients and controls) or/and to make conclusions about interactions among ROIs [19, 20]. In the latter case we feel that a special care should be taken to attribute the result to the modality that was used to obtain "effective connectivity". Although in essence all neuroimaging modalities with timeseries information measure neuronal activity and connectivity at their core, the degradation of such signals through e.g. the neurovascular transformation in fMRI and volume conduction/mixing in EEG/MEG before detection at the sensors does heavily influence the result. The combination of imaging modalities provides a way to minimize the loss of neuronal information although it remains unclear in which way connectivity from multimodal signals should be estimated in an optimal fashion. In order to test this problem, in this work we have estimated "effective connectivity" from two modalities (MEG and fMRI) of the same subjects performing the same task in MEG and in fMRI collected on separate occasions in a Bayesian network approach. Thus, we attempt to eliminate all differences but functional modality in these datasets. Then we compare the results for MEG and fMRI.

The rest of the paper is structured as follows. Section 2 describes details of Bayesian network modeling and the structure search algorithm as an approach to "effective connectivity" estimation as well as the data collection. Section 3 gives details of our data processing and application to each modality, and then covers the results of the structure search obtained in this study. We discuss consequences of our findings together with their interpretation in relation to the current literature in Section 4.

# 2. Methodology 

The goal of our work is studying how the choice of a functional modality may affect the conclusions of an "effective connectivity" study. In the following, we describe the method of Bayesian network structure search used here to estimate the connectivity, the metrics originating in the graph community structure research for characterizing graph structure properties, and the MEG and fMRI modalities we apply our comparison to.

### 2.1. Bayesian networks

Bayesian networks [14, 17, 21] can be viewed as a way to compactly represent a joint probability distribution by encoding the conditional independence structure of its random variables. This is done through two parts: a directed graph $G$, and parameters $\theta$ of conditional densities. Since all information about a set of random variables and their interactions is encoded in the joint probability density, being able to estimate and reason about it provides a way to understand complex structured data. The joint probability density of a given set of $n$ random variables $\boldsymbol{X}=\left\{X_{1}, X_{2}, \ldots X_{n}\right\}$ in the Bayesian network representation is expressed as

$$
P_{\theta}(\boldsymbol{X})=\prod_{i=1}^{n} P\left(X_{i} \mid P_{a}\left(X_{i}\right) ; \theta\right)
$$

where $P_{a}(\cdot)$ denotes the parent set of the argument in the corresponding graph structure $G$ of the BN. Compactness is achieved due to the significant decrease in the number of parameters, $\theta$, required to describe random variable values in conditional densities compared to every possible combination of values for all random variables of the joint density. This, however, is a consequence of the graphical representation, $G$.

The BN graphical representation $G$ is a directed acyclic graph (DAG) with random variables at nodes and directed edges connecting them according to the independence structure (Figure 1a). A random variable is called a parent if it has outgoing graph edges pointing to other nodes of the graph. A random variable with incident edges is called a child. The key property of a BN that gives it an advantage over the "functional connectivity" approaches is that, every variable is conditionally independent of its non descendants given its parents. This property and the factored form of the joint distribution (1) leads to special importance of a graphical unit called a family: a child node plus its parents (Figure 1b).

While in "functional connectivity" studies, the fundamental unit is a pair of ROIs connected by an edge, in "effective connectivity" analysis the fundamental unit is an entire family. Since it may simultaneously involve several parents and a child, the interactions it is modeling are of higher order than in the pairwise model. Figure 1c shows an example of modeling higher order nonlinear interactions in the family of 3 ROIs.

The data arriving from functional measurements is, by nature, continuous. Unfortunately, the approaches to treat it in the context of Bayesian networks are either not well developed or limited. In this paper we employ the quantized representation. In terms of generality of relationships a Bayesian network can represent, discrete versions are arguably the best due to the high expressiveness of multinomial probability densities encoding conditional distributions of each family.

Because fMRI and MEG provide only indirect measures of the underlying true neural activity, we could potentially employ a "hidden state" (or latent variable) Bayesian network

model. However, in functional neuroimaging application of this paper, we do not need this property because measurements of fMRI and MEG are available at all points to fully cover the ROI map of the cortex.

What is of essential interest in this paper is the graph structure $G$ that leads to the factorization in equation (1). Estimating the graph of a Bayesian network from available data is called structure search. Structure search algorithms can be roughly split in two categories: constraint-based and score based[22]. We use the score-based approach in this paper. All parameters of multinomial conditional densities are estimated as an integral part of the structure search procedure. This paper is solely focused on the resulting graphical structures and their properties. Most of all we are interested in the aggregate descriptions that originate from community network literature and provide metrics suitable for graph comparison and quantify holistic graph characteristics [23].

The superexponential complexity of the score based structure search [24] and inevitable presence of noise in the imaging data, if not completely rule out the use of approaches that return a single "best" graph $G$ then clearly make it difficult in our application. We want to characterize distributions of graph structures that are consistent with the available data and the Markov chain Monte Carlo (MCMC) is a natural choice that fits this goal [25, 26]. Among several MCMC approaches and implementations of structure search we have found the approach of Grzegorczyk and Husmeier [18] to work best for our data. This approach has returned consistent results for MEG and fMRI, whereas we have gotten similar and stable results for MEG using other MCMC [27] and greedy [28] approaches, fMRI results were unstable and tended to get trapped in local minima with these approaches.

# 2.2. Graph structure characterization 

An "effective connectivity" graph can provide answers to a number of interesting questions, such as causal interactions among ROIs, density of interactions, cliques in the brain network, stable families across the distribution of likely graphs and many others. Our goal is to be able to look at the graph as a whole and trace changes that occur due to changes in experimental conditions and modalities.

Characterizing the whole graph by a single interpretable summary statistic is a common technique in the field of random graphs [29] and the complex network analysis and community structures research [30-32]. In neuroimaging the approach is gaining popularity for obtaining neurobiologically meaningful measures and even revealing neurological and psychological disorders by comparing across populations [23]. Although currently applied mostly to characterization of structural networks and the networks of "functional connectivity", we adopt it for "effective connectivity" graphs. To the best of our knowledge, this is a novel area of application, and we believe it to be very useful.

In this study we use some of the standard measures [23], which are explained below:

- in-degree - number of parents of node $X$

$$
\operatorname{deg}_{\text {in }}(X)=\sum Y_{i}, \quad Y_{i} \in P_{a}(X)
$$

- out-degree - number of children of node $X$

$$
\operatorname{deg}_{\text {out }}(X)=\sum Y_{i}, \quad X \in P_{a}\left(Y_{i}\right)
$$

- degree centrality - The degree centrality of a single node, $X$, is given by (4). The degree centrality of the entire graph, given in (5), is defined with respect to the maximal degree node, $X^{*}$.

$$
c(X)=\frac{\operatorname{deg}(X)}{n-1}
$$

$$
c(G)=\frac{\sum\left(c\left(X^{*}\right)-c\left(X_{i}\right)\right)}{n-2}
$$

- maximum degree - the maximum degree of a node in a graph
- diameter - the greatest distance between any pair of vertices in $G$
- density - the ratio of the number of edges and the number of possible edges
- average path length - the average geodesic length in a graph, or the average of all shortest paths for all pairs of vertices in a graph
- average local transitivity - the probability that the adjacent nodes of a node are connected, which is also called the clustering coefficient


# 2.3. Functional modalities 

MEG and fMRI both provide indirect views of the underlying neural activity. Focusing our attention on cortical regions of the brain, we can assume that the common source of the signal for both modalities is local and incoming synaptic activity as is currently understood [33]. Nevertheless, the physical mechanisms of signal generation are quite different and lead to substantial differences in signal properties $[9,10]$.

Due to a high effective temporal sampling rate, on the order of milliseconds, MEG can provide instantaneous measurements of large-scale synchronous electromagnetic phenomena introduced by neural activity. On the other hand, the neurovascular transformation of neural activity into the fMRI signal can be measured with full brain coverage with high spatial resolution without a spatial inverse problem. The two modalities have complementary strengths and weaknesses. For example, the ill-posed inverse problem accompanying MEG analysis becomes an issue when the goal is localization of the neural activity [11, 34, 35]. The localized spatial resolution of fMRI allows one to concentrate on the relationship among brain regions. In this case, the dynamical properties of a modality gain high importance. However, fMRI is unable to reflect neural activity dynamics with the temporal resolution and quality found in MEG.

A number of publications on estimating brain's "functional connectivity" from fMRI data is available [36, 37]. Multiple studies of "effective connectivity", albeit with limited number of ROIs due to the high complexity of the task, are also mostly done on fMRI data [38, 39, 15, 40], although MEG data has also been used [41]. Since these functional modalities are both representing neural activity, which is more true since we are talking only about cortical regions, the conclusions that are desired from connectivity studies should be general and relate to the brain function, or particularly acknowledge the role of the modality in the obtained result. In our work we look at the cortical representation of MEG (source space) and fMRI (after appropriate segmentation) data side by side and compare the structures that we receive using the exact same approach for both of the modalities. Graph community characterization metrics [23] of Section 2.2 are instrumental here.

# 3. Application 

### 3.1. Data collection and processing

All participants completed the multimodal oddball task while undergoing FMRI on a 3.0 Tesla Siemens Trio scanner. Participants rested supine in the scanner with their head secured by a forehead strap, with additional foam padding to limit head motion within the head coil. Presentation software (Neurobehavioral Systems) was used for stimulus presentation, synchronization of stimulus events with the MRI scanner and recording of RTs. Visual stimuli included a white fixation cross on a black background that was rear-projected onto an opaque white Plexiglas projection screen using a Sharp XG-C50X LCD projector. Auditory stimuli were presented via an Avotec Silent Scan 3100 Series system.

Stimulus timing was identical to that used in Clark et al. [42]. Stimuli were a frequent standard image of a desert scene ( $82 \%$ of stimuli), novel, non-repeated non-threatening images of middle-eastern scenes including people, houses and other objects ( $9 \%$ ), and a threatening target stimulus of a middle-eastern combatant shooting a rifle at the observer ( $9 \%$ of stimuli). Along with the images, computer generated sounds were also presented to the subjects, coincident with the visual images. This included a repeated birdsong for the repeated standard stimulus, a repeated gunshot sound for the repeated threat target stimulus, and various non-repeated sounds (whistles and chords) with the non-repeated novel stimuli. Stimuli were presented sequentially in pseudorandom order for 200 ms each with the interstimulus interval (ISI) varied randomly from 550 to 2050 ms across trials. Subjects were instructed to make a speeded button-press response upon each presentation of the repeated threat stimulus. Subjects were further requested to maintain gaze. Direction of gaze was not monitored. The non-repeated novel stimuli had the same presentation frequency as the repeated target threat stimulus, but no response was required. Each run was comprised of 90 stimuli.. Stimulus sequences were selected with a low correlation of predicted blood oxygen level dependent (BOLD) responses among the three stimulus types $(|r|<0.2)$, which allowed the BOLD response evoked by each stimulus type to be tested separately.

High resolution T1-weighted anatomic images were acquired with a 5 -echo multi-echo MPRAGE sequence [TE (echo time) $=1.64,3.5,5.36,7.22$ and 9.08 qms, TR (repetition time) $\mathrm{TR}=2.53 \mathrm{~s}, \mathrm{TI}=1.2 \mathrm{~s}, 7^{\circ}$ flip angle, number of excitations (NEX) $=1$, slice thickness $=1 \mathrm{~mm}$, FOV (field of view) $=256 \mathrm{~mm}$, resolution $=256 \times 256]$ on a 3 Tesla Siemens Trio scanner. For the FMRI series, 88 echo-planar images were collected using a single-shot, gradient-echo echoplanar pulse sequence [TR $=2000 \mathrm{~ms} ; \mathrm{TE}=29 \mathrm{~ms}$; flip angle $=75^{\circ}$; $\mathrm{FOV}=240 \mathrm{~mm}$; matrix size $=64 \times 64]$ per run across 12 runs. A total of 1056 images were used for the final analyses. Thirty-three contiguous sagittal 3.5 mm thick slices with a gap factor of 1.05 mm were selected to provide whole-brain coverage (voxel size: $3.75 \times 3.75$ $\times 4.55 \mathrm{~mm})$.

Functional images were generated using Analysis of Functional NeuroImages (AFNI) software package [43] and SPM. Time series images were spatially registered in threedimensional space to minimize effects of head motion, temporally interpolated to correct for slice-time acquisition differences, and blurred using a 10 mm full-width-half-maximum Gaussian kernel. Functional images were then interpolated to volumes with 3 mm 3 voxels and converted to Montreal Neurological Institute (MNI) standard stereotaxic coordinate space.

MEG data were recorder on a separate day from the same subjects under the same conditions as for fMRI.

The data were recorded with a VSMMedtech Omega 275 whole-head biomagnetometer system (VSM MedTech, Vancouver, BC, Canada) located at the Mind Research Network Imaging Center (Albuquerque, NM, USA). The MEG data was recorded at 1200 samples/ second, with only antialiasing filters applied.

Informed consent was acquired prior to data collection (UNM HRRC Protocol 07-121).
MNE analyses were conducted as follows. The continuous recording was filtered from 1 to 100 Hz . Epochs were extracted from the continuous recording for calculation of the evoked response. The MEG data set was coregistered to the MRI images that result from FreeSurfer analysis. A boundary element model for use in the forward model was constructed from the FreeSurfer tessellations of the cortical surface. The patterns of cortical activation were reconstructed using the minimum norm estimate.

A deconvolution analysis of fMRI data was then performed on a voxel-wise basis to generate one hemodynamic response function (HRF) for each of the three conditions (novel, target and standard). Each HRF was derived relative to the baseline state (visual fixation plus baseline gradient noise) and based on the first 18 seconds post-stimulus onset. Deconvolution ends with 18 samples per IRF.

Cortical parcellation of each subjects structural image was obtained using Freesurfer [44]. An affine transformation was obtained between subjects T1 weighted image and MNI template. The cortical parcellations were then transformed to MNI space using the transformation obtained above. These values were mapped using nearest neighbour interpolation. A total of 68 cortical ROIs were obtained. For each ROI, deconvolved response averages were obtained from voxels corresponding to top $25 \% T$-statistic for target and novel conditions separately, which are later interpolated to 2400 samples to obtain an exact match to MEG data. This is done to equalize statistical power of both datasets and avoid introducing a balancing parameter. The ROI average responses were then quantized on a per subject basis by dividing the maximum and minimum response values across both target and novel conditions and ROIs into 5 equally spaced bins ("very low", "low", "baseline", "high","very high"). Subject data were pooled (stacked in time) together to obtain the resulting dataset shown above. A sample deconvolved fMRI and evoked MEG data are shown in Figure 2a for a single subject with all 68 ROI timecourses per plot for both modalities and two conditions. Note the difference in temporal scale of fMRI and MEG, where we gave each modality a window where the stimuli effect is detectable, similar to the approach used by Daunizeau et. al [45]. Quantized version of this signal stacked together for all subjects is shown in Figure 2b, which is the complete dataset used in our study.

# 3.2. Networks 

The MCMC algorithm was run for 1500 iterations of the burn-in periodwhich were discarded. In subsequent sampling every tenth DAG was saved for further analysis. The results are based on 1000 stored DAGs that are consistent with the data. Using these graphs we have computed marginal distributions of the edges, which are shown in Figure 3.

The complete marginal distributions for both modalities and two conditions per modality are hard to analyze and provide meaningful comparison. Exactly for that reason we will be using aggregate measures below. However, some of the details are already visible in Figure 3:

- distributions of fMRI induced edges are denser than these of MEG;
- stronger interactions between contralateral homologs in fMRI than in MEG;

- for novel stimuli in fMRI more of the right hemisphere ROIs are inuencing its left hemisphere homologs, and for target stimuli the relationship reverses (diagonals of the darker blocks in Figure 3);
- in MEG there are much fewer connections between homologs, but a reversed pattern can nevertheless be observed: novel stimuli - left inuences right, target stimuli - right inuences left, but to a much smaller extent.

To put the distribution in context, Figure 4 shows the highest scoring graphs that were sampled during MCMC runs for each modality and each condition: a total of 4 graphs. Each graph is overlaid on top of a brain projection, to show corresponding locations of graph nodes within the brain. The same graph is also displayed in a force-based layout to avoid node overlap. Node sizes are proportional to the total node degree. Blue color indicates anode from the left hemisphere and red - from the right.

The networks produced by the structure search algorithm are consistent with our current understanding of brain processing the oddball task. The right hemisphere on average is more active during non-verbal oddballs, the right temporal lobe is the major source of the N1 enhancement/MMN, and also more active during later components [46-51].

Figures 3 and 4 provide detailed information about resulting "effective connectivity" networks obtained in our study. However, they show all information almost unprocessed. In order to see the differences between the modalities and stimuli types we take advantage of an aggregate statistics from Section 2.2 and show degree distribution in Figure 5 for all nodes in all 1000 sampled networks for MEG and fMRI (novel and target stimuli)for indegree and out-degree separately. Histogram bars that identify nodes with number of children more than 15 are of separate color to emphasize the difference in MEG and fMRI.

Out-degree distributions of Figure 5 exhibit behavior which is reversed between MEG and fMRI. In the MEG case the distribution gains the tail in the case of target stimuli compared to the novel stimuli distribution, but in fMRI case the fat tail of the distribution in the novel stimuli case is not present when the target stimuli is presented. In-degree distributions (the indegree was limited above by 3 for computational reasons, which is a common practice for improving tracktability of the structure search algorithm [19])are not changing in the fMRI case, and shift to a denser case (more families of 2 and 3 parents) for the target stimuli.

# 4. Discussion 

Structure search in Bayesian and dynamic Bayesian networks has been previously applied to "effective connectivity" estimation in fMRI data [52-54, 19, 20]. We are not aware of an application similar to ours that would compare structures across modalities.

In Bayesian and, in general, probabilistic approaches the system is modeled with the joint probability distribution over random variables, which represent different aspects of the system. Quantities of interest and their distributions are discovered from the available information through systematic application of probability calculus [55]. Probabilistic Bayesian approaches are attractive in their inherent ability of providing confidence estimates automatically, since the result is usually not a single solution but rather a distribution of likely solutions [55]. An additional and important benefit of these methods is their relatively easy extensibility to different numbers of data sources and flexible incorporation of prior information. This can be used in future work to combine MEG and fMRI modalities to discover underlying Bayesian networks.

Interesting to note that marginal edge distributions are denser in case of fMRI and there are more connections across hemispheres especially between contralateral homologs. This can

be explained be temporal blurring of hemodynamic response function. Brain "effective connectivity" networks are processing units and must be constantly involved in information flow. The oddball task is not complicated and requires brain resources only for a short time. While MEG is able to capture that "context switch" when the brain network is processing the stimuli not being involved in other tasks, fMRI even after deconvolution still contains large amounts of information about what brain was doing in these 18 seconds after response. This is, certainly, more demanding than just processing the oddball stimuli and leads to denser networks. Also the background brain processing is not specific to the right hemisphere, as is the task in our study, and results in denser inter-hemisphere connections.

The difference in distribution changes between MEG and fMRI shown in Figure 5, suggest that conclusions in "effective connectivity" studies depend on the modality chosen for the study. Interestingly, behavior of the out-degree distribution can lead not only to different but contradicting conclusions depending on weather MEG or fMRI were chosen for the study. Since an exponential distribution with a fatter tail is closer to the small world network [30], from MEG estimated "effective connectivity" we may conclude that target stimuli increase the small-worldness of the brain network. However, for an fMRI only study that conclusion would have been a decrease in the small-worldness. In order to see if this behavior reversal only holds for the out-degree distribution, we have computed distributions of several other metrics described in Section 2.2. Figure 6 summarizes distributions of these metrics for MEG and fMRI in novel and target conditions. fMRI result either exhibits a change reversed compared to the MEG trend, or shows no change at all, when MEG based distribution does. This is an undesired behavior especially for making neurologically meaningful conclusions [23].

A possible resolution would be information fusion, when several data sources are used to estimate "effective connectivity". That could be done either by working with the types of models used in this paper directly and applying a hierarchical Bayesian model to model interactions between structures. Another possibility is to first deconvolve the BOLD response to neural activity and perform structure search on this data, as already done by dynamic causal modeling [15]. This still may have problems for biasing the structure towards fMRI, and a better approach would be to use all available functional modalities to estimate neural activity on which a structure search algorithm can later operate [56].

# 5. Conclusions 

In this study we have shown that "effective connectivity", estimated from the fully observed data, depends on the functional modality. Possible solutions would involve fusion of functional modalities for "effective connectivity" estimation, deconvolution of available modalities to the neural signal, or both in the latent variable modeling.

By recovering network patterns expected in an oddball study, we have confirmed that Bayesian network is a suitable tool for "effective connectivity" studies. To the best of our knowledge, we have used for the first time the aggregate measure of complex network structures to study behavior of "effective connectivity" networks, as opposed to their previous applications to the structural and "functional connectivity". The use of MCMC approach as the structure learning algorithm proved to be fruitful by allowing analysis of distributions of measures on all likely graphs.
