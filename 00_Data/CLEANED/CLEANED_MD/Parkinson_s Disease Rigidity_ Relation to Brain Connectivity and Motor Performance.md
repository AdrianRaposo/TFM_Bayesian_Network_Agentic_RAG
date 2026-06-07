# Parkinson's disease rigidity: relation to brain connectivity and motor performance 

Nazanin Baradaran ${ }^{1}$, Sun Nee Tan ${ }^{1}$, Aiping Liu ${ }^{2}$, Ahmad Ashoori ${ }^{2}$, Samantha J. Palmer ${ }^{1}$, Z. Jane Wang ${ }^{2}$, Meeko M. K. Oishi ${ }^{3}$ and Martin J. McKeown ${ }^{1,2,4 *}$<br>${ }^{1}$ Pacific Parkinson's Research Centre, University of British Columbia, Vancouver, BC, Canada<br>${ }^{2}$ Department of Electrical and Computer Engineering, University of British Columbia, Vancouver, BC, Canada<br>${ }^{3}$ Department of Electrical and Computer Engineering, University of New Mexico, Albuquerque, NM, USA<br>${ }^{4}$ Department of Medicine (Neurology), University of British Columbia, Vancouver, BC, Canada

## Edited by:

Thomas Foki, Medical University of Vienna, Austria

## Reviewed by:

Josep Valls-Sole, Hospital Clínic, Spain
Oury Monchy, Université de
Montréal, Canada

* Correspondence:

Martin J. McKeown, University of British Columbia, M31, Purdy
Pavilion, University Hospital, UBC
Site, 2221 Wesbrook Mall, Vancouver, BC V6T 2B5, Canada
e-mail: martin.mckeown@ubc.ca

Objective: (1) To determine the brain connectivity pattern associated with clinical rigidity scores in Parkinson's disease (PD) and (2) to determine the relation between clinically assessed rigidity and quantitative metrics of motor performance.

Background: Rigidity, the resistance to passive movement, is exacerbated in PD by asking the subject to move the contralateral limb, implying that rigidity involves a distributed brain network. Rigidity mainly affects subjects when they attempt to move; yet the relation between clinical rigidity scores and quantitative aspects of motor performance are unknown.

Methods: Ten clinically diagnosed PD patients (off-medication) and 10 controls were recruited to perform an fMRI squeeze-bulb tracking task that included both visually guided and internally guided features. The direct functional connectivity between anatomically defined regions of interest was assessed with Dynamic Bayesian Networks (DBNs). Tracking performance was assessed by fitting Linear Dynamical System (LDS) models to the motor performance, and was compared to the clinical rigidity scores. A cross-validated Least Absolute Shrinkage and Selection Operator (LASSO) regression method was used to determine the brain connectivity network that best predicted clinical rigidity scores.

Results: The damping ratio of the LDS models significantly correlated with clinical rigidity scores $(p=0.014)$. An fMRI connectivity network in subcortical and primary and premotor cortical regions accurately predicted clinical rigidity scores $\left(p<10^{-5}\right)$.

Conclusion: A widely distributed cortical/subcortical network is associated with rigidity observed in PD patients, which reinforces the importance of altered functional connectivity in the pathophysiology of PD. PD subjects with higher rigidity scores tend to have less overshoot in their tracking performance, and damping ratio may represent a robust, quantitative marker of the motoric effects of increasing rigidity.

Keywords: Parkinson's disease, rigidity, fMRI, damping ratio, linear dynamical system, LASSO regression

## INTRODUCTION

Rigidity is defined by increased resistance during passive mobilization of an extremity, independent of direction and velocity of movement (Delwaide, 2001), and is one of the cardinal diagnostic features of Parkinson's disease (PD), along with tremor, bradykinesia, and postural instability (Tolosa et al., 2006; Shapiro et al., 2007). Since rigidity can be a manifestation of various pathologies involving the basal ganglia and can be altered during states of drowsiness or relaxation (Webster, 1960; Fung and Thompson, 2007), it is usually not considered pathognomonic of PD.

The underlying mechanism of rigidity in PD is poorly understood, and no direct relationship exists between dopamine deficiency and rigidity, making it difficult to explain through the classic model of basal ganglia pathophysiology (Rodríguez-Oroz et al., 2009). The classic description of basal ganglia activity in

PD predicts that increased neuronal activity in the subthalamic nucleus (STN) and internal globus pallidus (GPi), and its resultant inhibition of thalamocortical projections, should result in decreased muscle activation and reduced response to stretching when, in fact, the opposite is observed (Bezard and Przedborski, 2011).

Contributions from the spinal cord, brain stem including higher cortical circuits have all been proposed as being important in the pathophysiology of rigidity (Hong et al., 2007), and several mechanisms, likely not mutually exclusive, may be responsible (Delwaide, 2001). One potential mechanism may be increases in excitability in long loop reflex pathways. Rapid stretching of a contracting muscle results in responses at different latencies. The most rapid response corresponds to the well-known monosynaptic involuntary stretch reflex easily assessed by tapping a tendon

with a reflex hammer. A longer latency response corresponds to transcortical involvement. It is postulated that if this transcortical loop is hyperactive, then enhanced response to stretching may appear clinically as rigidity. A second postulate suggests that inappropriate commands from one or several descending spinal pathways caused malfunctions of the short reflex pathways at the spinal level (Delwaide, 2001). However, clinical observations may suggest an alternate explanation. It is frequently observed that Froment's maneuver (voluntary movement of the contralateral limb) can accentuate or even unmask latent rigidity. This implies that a systems-level, distributed brain network may contribute significantly to the mechanism of rigidity in PD. Therefore here we utilize fMRI imaging techniques to determine distributed brain connectivity patterns that predict clinical rigidity scores.

While PD patients may complain of stiffness, or even present with functional limitation (e.g., "frozen" shoulder), in general, rigidity is a sign detected by the clinician rather than a symptom described by patient. Yet, despite its potential functional importance, the implications of progressive rigidity in PD on quantitative motor performance are not currently known. Here we utilize Linear Dynamical System (LDS) models of tracking behavior collected concomitantly during the fMRI scanner session to assess motor performance, as we have previously shown this to be a more sensitive measure of motor performance than the normally used overall tracking error (Oishi et al., 2011). When PD subjects are asked to track a target, they tend to undershoot the actual target (Van Gemmert et al., 2003). This undershooting is rigorously defined as "damping ratio" in control systems. Specifically the damping ratio describes the behavior of a system tracking a desired target. Highly underdamped systems tend to oscillate around the desired trajectory, where highly overdamped systems tend to be sluggish and slow, and fail to sufficiently track rapidly changing targets (Ljung and Ljung, 1987). We thus hypothesize that the damping ratio parameter of LDS models fitted to each subject's motor performance would closely correlate with overall clinical rigidity scores.

## MATERIALS AND METHODS

## SUBJECTS

Written, informed consent was obtained from all subjects in accordance with the Declaration of Helsinki, and the study was approved by the University of British Columbia Research Ethics Board. Ten subjects with clinically diagnosed PD (off-medication) and 10 healthy age-matched control subjects were recruited from the Pacific Parkinson's Research Centre (PPRC)/Movement Disorders Clinic. In the PD group, all subjects (four men, six women, eight right-handed, and two left-handed) were PD patients diagnosed with mild to moderate PD (Hoehn and Yahr stage 2-3) (Hoehn and Yahr, 1967). Their mean symptom duration and mean age were $5.8 \pm 3$ years and $66 \pm 8$ years, respectively. PD subjects stopped their l-dopa medications overnight for a minimum of 12 h before the study. Those who were also taking dopamine agonists were withheld from medications for a minimum of 18 h . The mean Unified Parkinson's Disease Rating Scale (UPDRS) motor score off-medication was $26 \pm 8$ (Table 1).

Additionally, we recruited 10 healthy, age-matched individuals (three men, seven women, nine right-handed, one left-handed) without active neurological disorders as control subjects with

Table 1 | Demographic characteristics of PD patients and normal healthy controls.


mean age of $57.4 \pm 14$ years. Our exclusion criteria were: (1) subjects presenting with atypical Parkinsonism, (2) presence of other neurological or psychiatric conditions, (3) use of antidepressants, hypnotics, or dopamine blocking agents. All PD subjects were taking l-dopa medication with an average daily dose of $685 \pm 231 \mathrm{mg}$, and additionally some subjects took other anti-Parkinson's medications, including ropinirole, bromocriptine, and domperidone. For the 3/20 subjects who were left-hand dominant, we still asked subjects to perform the task with their right hand to ensure that lateralized activity in motor regions (e.g., cerebellar hemisphere, primary motor cortex) was relatively consistent. While complex hand sequence movements tend to be lateralized to the left hemisphere (Lotze et al., 2000), independent of the hand moving, lateralization was more strongly dependent upon the actual hand used since our task was simple and over-learned.

## EXPERIMENTAL DESIGN

To ensure that the results we found were relatively robust to the specific task performed, we purposely chose a task that included both externally guided (EG, e.g., in response to a visual stimulus) and internally guided (IG, e.g., recalled from memory) aspects. The basal ganglia are more active when a subject must perform an action that is selected from many potential candidates of action (Mushiake and Strick, 1995; Jueptner and Weiller, 1998; van Donkelaar et al., 1999, 2000). The cerebellum, traditionally associated with pure motor control, is now considered to be essential for the development of "forward models," such as predicting the sensory consequences of motor actions (Blakemore et al., 2001; Miall and Jenkinson, 2005). Cerebellar activity is normally associated with EG movements where sensorimotor integration is important (Jueptner et al., 1996; van Donkelaar et al., 1999, 2000). Therefore the task consisted of a squeezing a bulb in a sinusoidal pattern that was guided by visual cues corrupted with varying amounts of noise. Specifically, subjects were instructed to squeeze a rubber bulb with their right hand to control the width of a bar, which did not translate horizontally or vertically. Subjects were asked to keep the ends of the black bar within a 0.5 Hz vertically scrolling pathway by squeezing the bulb which required a force between 5 and $15 \%$ maximum voluntary contraction (MVC) (see Figure 1 for illustration of the task). They were asked to maintain a smooth

![img-0.jpeg](img-0.jpeg)

**FIGURE 1 | An illustration of the experimental task.** The sinusoidal path scrolls down vertically, with different frequencies of noise trajectories. Subjects had to control the width of the (red) bar to maintain the ends of the bar within the sinusoidal pathway.

sinusoidal force pattern at 0.5 Hz even when the scrolling pathway was partially degraded by varying amount of noise levels (0, 25, and 50%). Since we were interested in examining altered connectivity patterns, subjects performed 90 s runs where the noise level was kept constant. Each subject performed three 90 s runs at each of the three noise levels. The rubber squeeze-bulb was a custom-built, in-house designed system connected via water-filled, low-compliance tubing to a precision pressure transducer (Honeywell, Inc., Plymouth, MN, USA; model PPT0100AWN2VA) outside the scanner room. Each subject's MVC was assessed at the beginning of a 30-min training session by asking them to squeeze the bulb with their maximum force for 15 s while the pressure was measured. The median pressure over the 15 s was used as the MVC. All visual stimuli were coded with Matlab (Natick, MA, USA) and the Psychtoolbox (Brainard, 1997).

### BEHAVIORAL DATA ANALYSIS

Behavioral force data from the squeeze-bulb were sampled at ~50 Hz. We first computed the root mean square (RMS) error between the actual and desired (pure sinusoidal) squeezing profiles. For a pursuit tracking task with input trajectory *u* and output trajectory *y*, the RMS error is calculated as:

$$E_{RMS} = \sqrt{\frac{1}{N} \sum_{i=1}^{N} \left(y[i] - u[i]\right)^2},\tag{1}$$

where *u[i]* is the desired position at time index *i*, and *y[i]* is the actual tracking done by the individual at time index *i*, and *N* is the number of time points.

We used System Identification techniques to assess tracking performance in PD. A standard discrete second-order linear dynamical system model is defined as:

$$\mathbf{x}_t = \mathbf{A} \mathbf{x}_{t-1} + \mathbf{B} \mathbf{u}_{t-1}; \mathbf{y}_t = \mathbf{C} \mathbf{x}_t + \mathbf{D} \mathbf{u}_t$$

where $\mathbf{u}_t$ represents the desired sinusoidal trajectory and $\mathbf{y}_t$ represents the actual bar width at time *t*. From these two sets of values, the constant matrices $\mathbf{A}$, $\mathbf{B}$, $\mathbf{C}$, and $\mathbf{D}$ can be extracted. It is important to note that these matrices completely characterize all possible system responses, that is, once tracking performance is successfully modeled, then the output $\mathbf{y}_t$ can be predicted for any given input $\mathbf{u}_t$, not just those that were chosen experimentally. Previous work, including our own, has suggested that second-order models can successfully model normal and PD subjects during a tracking task (Oishi et al., 2011).

Since the system response, $\mathbf{y}_t$ depends on the eigenvalues of $\mathbf{A}$, the eigenvalues can capture the essential features of each model. However, in order to make the characterizations of the models more intuitive, it is customary to transform the eigenvalues into two parameters: damping ratio ( $\zeta$) and natural frequency ( $\omega_n$), such that $\lambda_{1,2} = -\zeta \omega_n \pm (\omega_n) \sqrt{\zeta^2 - 1}$. A higher damping ratio is usually associated with a better performance, i.e., less oscillation and overshoot around the desired trajectory, with lower damping ratio associated with less damping (and more overshoot) in the error response. The natural frequency does not necessarily reflect that speed at which the subject was moving, rather it reflects the responsiveness of the system: a higher natural frequency is associated with faster response; while lower natural frequency is associated with slower response. Since we were interested in determining if rigidity had a linear correlation with one or more movement parameters, we also computed other parameters derived non-linearly from the eigenvalues, including rise time, peak time, and settling time.

### CLINICAL RIGIDITY SCORES

The same trained operator evaluated all PD patients in the off-medication state, to obtain the clinical rigidity score using part three of the UPDRS. A global rigidity score was estimated by simply summing the individual limb and truncal rigidity scores.

### DATA ACQUISITION

The MRI data were collected from a Philips Achieva 3.0 T scanner (Philips, Best, Netherlands) equipped with a headcoil. A whole-brain three-dimensional T1-weighted image consisting of 170 axial slices with high resolution were also acquired to facilitate the anatomical localization for each individual. Blood oxygenation level-dependent (BOLD) contrast echo-planar (EPI) T2*-weighted images were taken with the following specifications: repetition time 1985 ms, echo time 37 ms, flip angle 90°, field of view (FOV) 240.00 mm, matrix size 128 × 128, with pixel size 1.9 mm × 1.9 mm. The duration of each functional run was 4 min during which we obtained 36 axial slices with 3 mm thickness and 1 mm gap thickness. The FOV was set to include the cerebellum ventrally and also include the dorsal surface of the brain.

### fMRI DATA PRE-PROCESSING AND ANALYSIS

Since time correction, isotropic reslicing of voxels, and initial motion correction was performed with SPM99. We then used custom-built motion-correction software that is particularly accurate for the larger head motion seen in older and PD subjects (Liao et al., 2005, 2006). Low frequency drifts were removed with a discrete cosine transformation, with cutoff period of 128 s. We did not spatially normalize each subject's data to a common space, as we have demonstrated that this will incur excessive error (Nieto-Castanon et al., 2003; Chen et al., 2009; Ng et al.,

2009). Fifty two regions of interest (ROI) were extracted using a combined FreeSurfer (Harvard, MA, USA; http://surfer.nmr. mgh.harvard.edu/) and Large Deformation Diffeomorphic Metric Mapping (LDDMM) method (Khan et al., 2008).

## CONNECTIVITY ANALYSIS: PCfdr

The connectivity network between 52 FreeSurfer-derived ROIs was computed with the PCfdr (Peter Spirtes and Clark Glymour, false discovery rate) algorithm (Li and Wang, 2009). We selected these 52 ROIs based on motor regions and the ROIs involved in the Default Mode Network (DMN), which has been shown to be altered in PD (van Eimeren et al., 2009; Palmer et al., 2010). The PCfdr method is designed to overcome the typical problem for fMRI experiments, which is a large number of ROIs but relatively few time points. After taking the average time course of all voxels within each ROI (after linear detrending) to get an ROI timecourse, the PCfdr method determines the conditional (in) dependence of each pair of ROIs dependent on all other ROIs to determine if two ROIs are connected. We set the FDR threshold at $5 \%$ in this study. In order to aid comparisons, we pooled the PD and control groups together and computed the significant connections amongst ROIs. The subject specific connection strengths were then determined using standard dynamic Bayesian network (DBN) methodology (Li et al., 2008).

## CORRESPONDENCE BETWEEN CONNECTIVITY AND CLINICAL RIGIDITY SCORES

We used multivariate linear regression to determine whether or not clinical rigidity scores could be predicted from the connectivity patterns in PD subjects ("lasso" command in Matlab). Specifically, we modeled the rigidity scores as:

$$
Y=X \cdot \beta+\varepsilon
$$

where $Y$ was a vector of rigidity scores of dimensions 10 (i.e., number of subjects) by $1, X$ was 10 by $n$ (where $n$ is the number of significant connections between ROIs determine by the PCfdr/DBN method) and $\varepsilon$ is a 10 by 1 vector of residuals. Since, in this case, the number of potential regressors $(n)$ exceeds the number of examples (Van Gemmert et al., 2003), we utilized (Least Absolute Shrinkage and Selection Operator) LASSO regression (lasso command in Matlab) (Tibshirani, 1996). Unlike other methods such as ridge regression or ordinary least squares, LASSO regression puts a sparsity constraint on $\beta$ so that most values are zero and attempts to find the most informative connections to predict clinical scores (Tibshirani, 1996). The number of regressors selected by the LASSO operator was to give the least predictive error based on a 10 -fold cross-validation. Once the regressors were selected, we used robust regression (robustfit command in Matlab) to estimate the significance of the individual regressors.

## RESULTS

## BEHAVIORAL DATA

All PD individuals and healthy age-matched controls successfully conducted the visually guided tracking task at the required frequencies. In PD patients, neither rigidity nor tremor caused any
prominent difficulty with task performance. The RMS error did not differ significantly between PD and normal groups [ANOVA $(F(2,166)=1.56, P>0.05)]$, suggesting that PD subjects were able to robustly perform the task.

## CORRELATION BETWEEN CLINICAL RIGIDITY SCORES AND SELECTED MOTOR NETWORK

The PCfdr method detected 227 significant connections between ROIs, and thus the X matrix in Eq. 2 was $10 \times 227$. The 227 significant connections represents $\sim 8.6 \%$ of all possible $52 \times 51=2,652$ directional connections.

The LASSO regression operator selected nine of 227 significant connections between brain regions that significantly predicted rigidity $\left(p<10^{-5}\right)$. These regions include primary motor area (M1), ventral premotor area, supplementary motor area, basal ganglia, areas in the temporal, parietal, and occipital lobes as well as the cerebellum. The positive and negative correlation between connectivity measures and clinical rigidity scores are demonstrated in Figure 2 and summarized in Table 2.

Two of the connections within this selected network correlated positively with clinical rigidity scores, i.e., the strength of these connections increased with clinical rigidity scores: 1 . Left cerebellar cortex (L_CB_CTX) to left ventral premotor area (L_PMv) ( $p=0.0002$ ), 2. Left temporal pole region (L_T-POLE) to left superior temporal (L_TEM_s) $(p=0.0119)$. The remaining seven connections within this network were found to correlate negatively with clinical rigidity scores: 1 . Right superior temporal (R_TEM_s) to right ventral premotor area (R_PMv) ( $p=0.03$ ), 2. Right putamen (R_PUT) to right supplementary motor area (R_SMA) ( $p=0.002$ ), 3. Right temporal pole region (R_T-POLE) to left caudal medial frontal gyrus (L_CAU_MF) $\left(p<10^{-5}\right), 4$. Left primary motor area (L_M1) to left pre-cuneus (L_PRE-CUN) ( $p=0.02$ ), 5. Left lateral occipital (L_LAT_OCC) to right inferior parietal (R_PAR_i) $(p=0.02), 6$. Right pre-supplementary motor area (R_Pre-SMA) to right middle temporal (R_TEM_m), and 7. Left inferior parietal (L_PAR_i) to right temporal pole region (R_TPOLE) $(p=0.03)$. This implies that the strengths of these seven connections decreased with increasing clinical rigidity scores.

For comparison, we examined the strength of the connections in the rigidity network in PD to the same connections in normal controls. Two of these connections, namely the Left cerebellar cortex (L_CB_CTX) to left ventral premotor area (L_PMv), and also Left primary motor area (L_M1) to left pre-cuneus (L_PRECUN) had significantly stronger connections in normal controls compared to PD subjects off-medication ( $p=0.0076$, and 0.025 respectively).

## CORRELATION OF CLINICAL RIGIDITY SCORES AND DAMPING RATIO

The damping ratios of PD subjects had a linear relationship with clinical rigidity scores $(p=0.014)$ (see Figure 3). No other model parameters significantly correlated with rigidity, including natural frequency and peak time.

## DISCUSSION

We found that clinical rigidity scores are associated with widespread, altered connectivity in subcortical and cortical regions. Several studies also demonstrate altered cortical mechanisms in

![img-1.jpeg](img-1.jpeg)

FIGURE 2 |A schematic diagram depicting the connections that were associated with rigidity in PD. Thick yellow arrows represent positive correlation between connection strength and rigidity whereas thin white arrows represent negative relationship between connection strength and rigidity (see Table 2 for details of statistical values). Connections with significant positive correlations: 1. From left cerebellar cortex (L_CB_CTX) to left ventral premotor area (L_PMV) ( $p=0.0002$ ), 2. Left temporal pole region (L_T-POLE) to left superior temporal (L_TEM_s) ( $p=0.0119$ ). Connections with significant negative correlations: 1. Right superior temporal (R_TEM_s) to right ventral premotor area (R_PMV) ( $p=0.03$ ), 2. Right putamen (R_PUT) to right supplementary motor area (R_SMA) $(p=0.002), 3$. Right temporal pole region (R_T-POLE) to left medial frontal caudate (CAU_MF) $\left(p<10^{-3}\right), 4$. Left precentral motor area (L_M1) to left pre-cuneus (L_PRE-CUN) $(p=0.02), 5$. Left lateral occipital (L_LAT_OCC) to right inferior parietal (R_PAR_i) $(p=0.02), 6$. Right pre-supplementary motor area (R_Pre-SMA) to right middle temporal (R_TEM_m), and 7. Left inferior parietal (L_PAR_i) to right temporal pole region (R_T-POLE) $(p=0.03)$.

PD. Transcranial Magnetic Stimulation (TMS) studies suggest increased primary motor cortex excitability in PD (Cantello et al., 1996; Lefaucheur, 2005) at rest. Similarly, MPTP (1-methyl-4-phenyl-1,2,3,6-tetrahydropyridine)-treated monkeys have more vigorous and less specific neuronal responses in the primary motor cortex to passive limb movements. On the other hand, stimulation of the premotor cortex using repetitive TMS increases motor cortex excitability in healthy subjects and PD patients on medication, but fails to do so in patients with PD subjects off dopaminergic medication (Mir et al., 2005). This suggests dopaminergic-dependent defective premotor-motor connectivity in PD that would normally increase motor cortical excitability (Mir et al., 2005). Also, during contraction, there is reduced facilitation of motor response, implying alterations in cortical modulation (e.g., Lefaucheur, 2005). These findings, as well as our own results, further support the notion that dysfunction in higher cortical areas, in addition to subcortical regions, are important for rigidity in PD.

We found a connection from the right putamen to the right SMA that was negatively correlated with clinical rigidity scores $(p=0.002)$. This altered connectivity in the supplementary motor area (SMA) could be considered within the context of the long loop reflex pathway (Berardelli et al., 1983; Delwaide et al., 1986; Delwaide, 2001). The long loop reflex pathway starts from primary endings of the neuromuscular spindles (Ia fibers) carrying action potentials to the spinal cord that travel up the posterior column of the spinal cord to ultimately reach the sensorimotor cortex via the thalamus (Delwaide, 2001). The sensorimotor cortex then sends information back to spinal motor neurons via the corticospinal tract (Delwaide, 2001). Normally, the SMA inhibits the motor cortex. In PD, it has been speculated that the sensorimotor cortex is either facilitated or disinhibited (i.e., in a hyperexcitable state) resulting in increased excitability of the motor cortex (Delwaide et al., 1986; Delwaide, 2001). The long reflex loop may also contain connections from the motor cortex to the basal ganglia, returning to the SMA that then inhibits the motor cortex. In PD, the

Table 2 | The individual directional connections within this selected network found to significantly correlate with clinical rigidity scores.


*These two connections had significant stronger connectivity in normal controls compared to PD subjects with significant values of $p=0.007$ (left cerebellar cortex $\rightarrow$ left ventral premotor area) and $p=0.025$ (left primary motor cortex (M1) $\rightarrow$ left pre-cuneus). loop becomes less active, resulting in a hyperexcitable sensorimotor cortex (Delwaide, 2001). Therefore with disease progression, this inhibitory loop becomes less active, resulting in a hyperexcitable motor cortex that manifests as higher rigidity scores in PD patients.

In addition to the SMA $\rightarrow$ putamen connection observed, which could be part of the long loop reflex, we found connectivity between multiple brain regions that predicted clinical rigidity scores. These included the primary motor area (M1), ventral premotor area, supplementary motor area, basal ganglia, areas in the temporal, parietal, and occipital lobes as well as the cerebellum. The directional connection from the left cerebellar cortex was positively correlated with clinical rigidity scores, consistent with previous observations indicating maladaptive interactions between cerebellar and basal ganglia circuits associated with the increase tone of dystonia (Neychev et al., 2008). Our results revealed a significant negative correlation $(p=0.02)$ between the clinical rigidity score and the connection from the left M1 to the left pre-cuneus. This finding is consistent with previous wellestablished studies indicating a dysfunctional DMN in PD patients (van Eimeren et al., 2009) and the pivotal role of pre-cuneus in DMN (Fransson and Marrelec, 2008). It has been shown that DMN has a decreased tendency to disengage in PD individuals during an active task (van Eimeren et al., 2009). The negative correlation of the primary motor area to the DMN via the pre-cuneus in our study suggests a disconnection between these cortical regions in PD. The higher the rigidity scores in our patient population, the weaker the connection between M1 and pre-cuneus, suggesting

![img-2.jpeg](img-2.jpeg)

FIGURE 3 |There is a linear relationship between clinical rigidity scores and damping ratio (robustfit, $\boldsymbol{p}=\mathbf{0 . 0 1 4 4}$ ). This relationship could be utilized to predict rigidity scores, which significantly correlate with actual recorded rigidity scores.

an abnormal communication between the motor system and the DMN in PD population.

A number of connections that were associated with rigidity in our study, while relevant to PD pathophysiology, may reflect a correlative as opposed to a causative relation with rigidity. For example, the temporal pole to superior temporal sulcus connection found in our study may be related to the extensive literature on facial emotion recognition impairments in PD patients (Sprengelmeyer et al., 2003; Suzuki et al., 2006; Lawrence et al., 2007; Clark et al., 2008). The temporal pole has also been suggested to be associated with processing of complex perceptual and emotional stimuli (Olson et al., 2007). A voxel-based morphometry study found significant white matter loss in the superior temporal pole region in PD patients with depression only (Feldmann et al., 2008; Kostic and Filippi, 2011). Thus, depression in PD may be a form of "disconnection" syndrome between neocortical-ventral limbic structures (Kostic and Filippi, 2011). This significant connection was unexpected, and since depression score was not taken into account in this particular study, our finding suggests future studies ought to consider including depression assessment tools.

When we looked at the rigidity network, we found two connections that were of significantly reduced values in PD subjects compared to controls: the left cerebellar cortex (L_CB_CTX) to left ventral premotor area (L_PMv), and also left primary motor area (L_M1) to left pre-cuneus (L_PRE-CUN). What is of particular interest is that the former connection was positively correlated with rigidity, while the latter was negatively correlated. In effect, the cerebellar $\rightarrow$ premotor connection approached normal values with worsening rigidity. We interpret this as a compensatory mechanism. This is in contrast to the premotor $\rightarrow$ pre-cuneus connection that became more abnormal with progressive rigidity, and thus was more typical of a direct disease related change.

We used functional connectivity to explore the pathophysiology of rigidity, but is important to appreciate that functional connectivity can be observed between regions where no structural connectivity exists. At the temporal resolution of the fMRI there may be polysynaptic connections between two regions that may make them appear co-activating instantaneously. For example, the functional connection between the right temporal pole region to the left caudal medial frontal gyrus in this study has no known structural connections. Previous studies have suggested that functional connections between two regions that are not anatomically connected may be indicative of mutual influence by a third region (Damoiseaux and Greicius, 2009). We note that the connectivity methods we employed are specifically designed to deal with this possibility.

## CONCLUSION

Results from our study suggest that rigidity is associated with widespread changes in the brain, as opposed to a single discrete locus. In addition, our results suggest that damping ratio may be an objective surrogate of the important clinical sign of rigidity.

Chen, J., Palmer, S. J., Khan, A. R., and McKeown, M. J. (2009). Free-Surfer-Initialized Large Deformation Diffeomorphic Metric Mapping with Application to Parkinson's Disease. Orlando, FL:The SPIE Medical Imaging.
Clark, U. S., Neargarder, S., and Cronin-Golomb, A. (2008). Specific impairments in the recognition of emotional facial expressions in Parkinson's disease. Neuropsychologia 46, 2300-2309.
doi:10.1016/j.neuropsychologia. 2008.03.014

Damoiseaux, J. S., and Greicius, M. D. (2009). Greater than the sum of its parts: a review of studies combining structural connectivity and restingstate functional connectivity. Brain Struct. Funct. 213, 525-533.
Delwaide, P. J. (2001). Parkinsonian rigidity. Funct. Neurol. 16, 147-156.
Delwaide, P. J., Sabbatino, M., and Delwaide, C. (1986).Some pathophysiological aspects of

the parkinsonian rigidity. J. Neural Transm. Suppl. 22, 129-139.
Endo, T., Okuno, R., Yokoe, M., Akazawa, K., and Sakoda, S. (2009). A novel method for systematic analysis of rigidity in Parkinson's disease. Mov. Disord. 24, 2218-2224. doi:10.1002/mds. 22752
Feldmann, A., Illes, Z., Kosztolanyi, P., Illes, E., Mike, A., Kover, F., et al. (2008). Morphometric changes of gray matter in Parkinson's disease with depression: a voxel-based morphometry study. Mov. Disord. 23, 42-46. doi:10.1002/mds. 21765
Fransson, P., and Marrelec, G. (2008). The precuneus/posterior cingulate cortex plays a pivotal role in the default mode network: evidence from a partial correlation network analysis. Neuroimage 42, 1178-1184. doi:10.1016/j.neuroimage.2008.05. 059
Fung, V. S., Burne, J. A., and Morris, J. G. (2000). Objective quantification of resting and activated parkinsonian rigidity: a comparison of angular impulse and work scores. Mov. Disord. 15, 48-55. doi:10.1002/15318257(200001)15:18th:48::AID-MDS10098gt;3.0.CO;2-E
Fung, V. S. C., and Thompson, P. D. (2007). "Rigidity and spasticity," in Parkinson's Disease \& Movement Disorder, 5th Edn, eds J. Jankovic and E. Tolosa (Philadelphia: Lippincott Williams \& Wilkins), 720.

Hoehn, M. M., and Yahr, M. D. (1967). Parkinsonism: onset, progression and mortality. Neurology 17, 427-442. doi:10.1212/WNL.17.5.427
Hong, M., Perlmutter, J. S., and Earhart, G. M. (2007). Enhancement of rigidity in Parkinson's disease with activation. Mov. Disord. 22, 1164-1168. doi:10.1002/mds. 21524
Jueptner, J., Jueptner, M., Jenkins, I. H., Brooks, D. J., Frackowiak, R. S. J., and Passingham, R. E. (1996). The sensory guidance of movement: a comparison of the cerebellum and basal ganglia. Exp. Brain Res. 112, 462-474. doi:10.1007/BF00227952
Jueptner, M., and Weiller, C. (1998). A review of differences between basal ganglia and cerebellar control of movements as revealed by functional imaging studies. Brain 121(Pt 8), 1437-1449. doi:10.1093/brain/121.8.1437
Khan, A. R., Wang, L., and Beg, M. F. (2008). FreeSurfer-initiated fully-automated subcortical brain segmentation in MRI using Large Deformation Diffeomorphic Metric Mapping. Neuroimage 41, 735-746. doi:10.1016/j.neuroimage.2008.03.024

Kostic, V. S., and Filippi, M. (2011). Neuroanatomical correlates of depression and apathy in Parkinson's disease: magnetic resonance imaging studies. J. Neurol. Sci. 310, 61-63. doi:10.1016/j.jns
Lakie, M., Walsh, E. G., and Wright, G. W. (1984). Resonance at the wrist demonstrated by the use of a torque motor: an instrumental analysis of muscle tone in man. J. Physiol. (Lond.) 353, 265-285.
Langston, J. W., Widner, H., Goetz, C. G., Brooks, D., Fahn, S., Freeman, T., et al. (1992). Core assessment program for intracerebral transplantations (CAPIT). Mov. Disord. 7, 2-13. doi:10.1002/mds. 870070103
Lawrence, A. D., Goerendt, I. K., and Brooks, D. J. (2007). Impaired recognition of facial expressions of anger in Parkinson's disease patients acutely withdrawn from dopamine replacement therapy. Neuropsychologia 45, 65-74. doi:10.1016/j.neuropsychologia. 2006.04.016

Lefaucheur, J. P. (2005). Motor cortex dysfunction revealed by cortical excitability studies in Parkinson's disease: influence of antiparkinsonian treatment and cortical stimulation. Clin. Neurophysiol. 116, 244-253. doi:10.1016/j.clinph.2004.11.017
Li, J., and Wang, Z. J. (2009). Controlling the false discovery rate of the association/causality structure learned with the PC-algorithm. J. Mach. Learn. Res. 10, 475-514.
Li, J., Wang, Z. J., Palmer, S. J., and McKeown, M. J. (2008). Dynamic Bayesian network modeling of fMRI: a comparison of group-analysis methods. Neuroimage 41, 398-407. doi:10.1016/j.neuroimage.2008.01. 068
Liao, R., Krolik, J. L., and McKeown, M. J. (2005). An informationtheoretic criterion for intrasubject alignment of FMRI time series: motion corrected independent component analysis. IEEE Trans. Med. Imaging 24, 29-44. doi:10.1109/TMI.2004.837791
Liao, R., McKeown, M. J., and Krolik, J. L. (2006). Isolation and minimization of head motion-induced signal variations in fMRI data using independent component analysis. Magn. Reson. Med. 55, 1396-1413. doi:10.1002/mrm. 20893
Ljung, L., and Ljung, E. (1987). System Identification: Theory for the User. Englewood Cliffs, NJ: Prentice-Hall.
Lotze, M., Erb, M., Flos, H., Huelzmann, E., Godde, B., and Grodd, W. (2000). fMRI evaluation
of somatotopic representation in human primary motor cortex. Neuroimage 11, 473-481. doi:10.1006/nimg.2000.0556
Martínez-Martín, P. (1993). "Rating scales in Parkinson's disease," in Parkinson's Disease and Movement Disorders, 2nd Edn, eds J. Jankovic and E. Tolosa (Baltimore, MD: Williams and Wilkins), 281-292.
Miall, R. C., and Jenkinson, E. W. (2005). Functional imaging of changes in cerebellar activity related to learning during a novel eye-hand tracking task. Exp. Brain Res. 166, 170-183. doi:10.1007/s00221-005-2351-5
Mit, P., Matsunaga, K., Gilio, F., Quinn, N. P., Siebner, H. R., and Rothwell, J. C. (2005). Dopaminergic drugs restore facilitatory premotor-motor interactions in Parkinson disease. Neurology 64, 1906-1912. doi:10.1212/01.WNL.0000163772.5 6128.A8
Mushiake, H., and Strick, P. L. (1995). Pallidal neuron activity during sequential arm movements. J. Neurophysiol. 74, 2754-2758.
Neychev, V. K., Fan, X., Mitev, V. I., Hess, E. J., and Jinnah, H. A. (2008). The basal ganglia and cerebellum interact in the expression of dystonic movement. Brain 131(Pt 9), 2499-2509. doi:10.1093/brain/awn168
Ng, B., Abu-Gharbieh, R., and McKeown, M. J. (2009). Adverse Effects of Template-Based Warping on Spatial fMRI Analysis. Orlando, FL: The SPIE Medical Imaging.
Nieto-Castanon, A., Ghosh, S. S., Tourville, J. A., and Guenther, F. H. (2003). Region of interest based analysis of functional imaging data. Neuroimage 19, 1303-1316. doi:10.1016/S1053-8119(03)00 188-5
Oishi, M. M., TalebiFard, P., and McKeown, M. J. (2011). Assessing manual pursuit tracking in Parkinson's disease via linear dynamical systems. Ann. Biomed. Eng. 39, 2263-2273. doi:10.1007/s10439-011-0306-5
Olson, I. R., Plotzker, A., and Ezzyat, Y. (2007). The Enigmatic temporal pole: a review of findings on social and emotional processing. Brain 130(Pt 7), 1718-1731. doi:10.1093/brain/awm052
Palmer, S. J., Li, J., Wang, Z. J., and McKeown, M. J. (2010). Joint amplitude and connectivity compensatory mechanisms in Parkinson's disease. Neuroscience 166, 1110-1118. doi:10.1016/j.neuroscience.2010.01. 012
Patrick, S. K., Denington, A. A., Gauthier, M. J., Gillard, D. M., and

Prochazka, A. (2001). Quantification of the UPDRS Rigidity Scale. IEEE Trans. Neural Syst. Rehabil. Eng. 9, 31-41. doi:10.1109/7333.91 8274
Prochazka, A., Bennett, D. J., Stephens, M. J., Patrick, S. K., Sears-Duru, R., Roberts, T., et al. (1997). Measurement of rigidity in Parkinson's disease. Mov. Disord. 12, 24-32. doi:10.1002/mds.870120106
Rabey, J. M., Bass, H., Bonuccelli, U., Brooks, D., Klotz, P., Korczyn, A. D., et al. (1997). Evaluation of the Short Parkinson's Evaluation Scale: a new friendly scale for the evaluation of Parkinson's disease in clinical drug trials. Clin. Neuropharmacol. 20, 322-337. doi:10.1097/00002826199708000-00004
Richards, M., Marder, K., Cote, L., and Mayeux, R. (1994). Interrater reliability of the Unified Parkinson's Disease Rating Scale motor examination. Mov. Disord. 9, 89-91. doi:10.1002/mds.870090114
Rodríguez-Oroz, M. C., Jahanshahi, M., Krack, P., Litvan, I., Macias, R., Bezard, E., et al. (2009). Initial clinical manifestations of Parkinson's disease: features and pathophysiological mechanisms. Lancet Neurol. 8, 1128-1139. doi:10.1016/S1474-4422(09)70293-5
Shapiro, M. B., Vaillancourt, D. E., Sturman, M. M., Metman, L. V., Bakay, R. A., and Corcos, D. M. (2007). Effects of STN DBS on rigidity in Parkinson's disease. IEEE Trans. Neural Syst. Rehabil. Eng. 15, 173-181. doi:10.1109/TNSRE.2007. 896997
Sprengelmeyer, R., Young, A. W., Mabic, K., Schroeder, U., Woitalla, D., Buttner, T., et al. (2003). Facial expression recognition in people with medicated and unmedicated Parkinson's disease. Neuropsychologia 41, 1047-1057. doi:10.1016/S0028-3932(02)00 295-6
Suzuki, A., Hoshino, T., Shigemasu, K., and Kawamura, M. (2006). Disgustspecific impairment of facial expression recognition in Parkinson's disease. Brain 129(Pt 3), 707-717. doi:10.1093/brain/awf011
Tibshirani, R. (1996). Regression shrinkage and selection via the lasso. J. R. Stat. Soc. Series B Methodol. 58, 267-288.
Tolosa, E., Wenning, G., and Poewe, W. (2006). The diagnosis of Parkinson's disease. Lancet Neurol. 5, 75-86. doi:10.1016/S1474-4422(05)70 285-4
van Donkelaar, P., Stein, J. F., Passingham, R. E., and Miall, R.

C. (1999). Neuronal activity in the primate motor thalamus during visually triggered and internally generated limb movements. J. Cereb. Blood Flow Metab. 16, 23-33.
van Donkelaar, P., Stein, J. F., Passingham, R. E., and Miall, R. C. (2000). Temporary inactivation in the primate motor thalamus during visually triggered and internally generated limb movements. J. Neurophysiol. 83, 2780-2790.
van Eimeren, T., Monchi, O., Ballanger, B., and Strafella, A. P. (2009). Dysfunction of
the default mode network in Parkinson disease: a functional magnetic resonance imaging study. Arch. Neurol. 66, 877-883. doi:10.1001/archneurol.2009.97
Van Gemmert, A. W. A., Adler, C. H., and Stelmach, G. E. (2003). Parkinson's disease patients undershoot target size in handwriting and similar tasks. J. Neurol. Neurosurg. Psychiatr. 74, 1502-1508. doi:10.1136/jnnp.74.11. 1502
Webster, D. D. (1960). Dynamic measurement of rigidity, strength, and tremor in Parkinson patients before and after destruction of mesial globus
pallidus. Neurology 10, 157-163. doi:10.1212/WNL.10.2.157

Conflict of Interest Statement: The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

Received: 08 March 2013; accepted: 22 May 2013; published online: 05 June 2013.

Citation: Baradaran N, Tan SN, Liu A, Ashoori A, Palmer SJ, Wang ZJ, Oishi MMK and McKeown MJ (2013)

Parkinson's disease rigidity: relation to brain connectivity and motor performance. Front. Neurol. 4:67. doi: 10.3389/fneur.2013.00067

This article was submitted to Frontiers in Movement Disorders, a specialty of Frontiers in Neurology.
Copyright © 2013 Baradaran, Tan, Liu, Ashoori, Palmer, Wang, Oishi and McKeown. This is an open-access article distributed under the terms of the Creative Commons Attribution License, which permits use, distribution and reproduction in other forums, provided the original authors and source are credited and subject to any copyright notices concerning any third-party graphics etc.