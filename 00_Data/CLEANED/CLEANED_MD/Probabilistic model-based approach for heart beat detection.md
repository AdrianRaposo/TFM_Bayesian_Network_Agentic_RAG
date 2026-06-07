# Probabilistic Model-Based Approach for Heart Beat Detection 

Hugh Chen<br>University of California Berkeley California, USA<br>hugh.chen\{at\}berkeley.edu

Yusuf Erol<br>University of California Berkeley California, USA<br>yusufbugraerol\{at\}berkeley.edu<br>Eric Shen<br>University of California Berkeley California, USA<br>ericshen\{at\}berkeley.edu

Stuart Russell<br>University of California Berkeley<br>California, USA<br>russell\{at\}cs.berkeley.edu

Nowadays, hospitals are ubiquitous and integral to modern society. Patients flow in and out of a veritable whirlwind of paperwork, consultations, and potential inpatient admissions, through an abstracted system that is not without flaws. One of the biggest flaws in the medical system is perhaps an unexpected one: the patient alarm system. One longitudinal study reported an $88.8 \%$ rate of false alarms, with other studies reporting numbers of similar magnitudes. These false alarm rates lead to a number of deleterious effects that manifest in a significantly lower standard of care across clinics.

This paper discusses a model-based probabilistic inference approach to identifying variables at a detection level. We design a generative model that complies with an overview of human physiology and perform approximate Bayesian inference. One primary goal of this paper is to justify a Bayesian modeling approach to increasing robustness in a physiological domain.

We use three data sets provided by Physionet, a research resource for complex physiological signals, in the form of the Physionet 2014 Challenge set-p1 and set-p2, as well as the MGH/MF Waveform Database. On the extended data set our algorithm is on par with the other top six submissions to the Physionet 2014 challenge.

Keywords: Beat Detection, PhysioNet Challenge, Particle Filter, Dynamic Bayesian Network, ECG, Blood Pressure, Model Based Probabilistic Inference.

# 1 Introduction 

Patient monitoring is a significant part of health care, not only to ensure that physicians can accurately diagnose and treat patients, but also to trigger biometric-based alarms. The intent of these alarms is to guarantee that a patient receives attention from clinicians whenever his or her condition takes a turn for the worse.

One of the important facets of such biometric data are heart beats. By monitoring heart beats, a number of cardiac issues, including a variety of life-threatening arrhythmia (asystole, bradycardia, tachycardia, etc.), can be detected (Goldberger, Amaral, Glass, Hausdorff, Ivanov, Mark, Mietus, Moody, Peng \& Stanley 2000 (June 13)). In the case where there is a high noise level and poor signal quality the heart beats themselves are unreliable. These unreliable beats can lead to false-negatives, where alarms fail to be triggered, as well as false-positives, where alarms are triggered for no substantive reason. These two cases respectively result in alarm failure and alarm fatigue (Chopra \& McMahon 2014).

False-negatives are direct alarm failures. Instances of alarm failure are dangerous because they mean that patients in life-threatening situations may be completely overlooked. Alarm fatigue, on the other hand, is an indirect consequence of an excess of false-positives (AKA false alarms). An excess of false alarms has a number of pernicious effects, including the desensitization of nurses and doctors to true alarms, disturbance of ailing patients, and the cost of time wasted for both physicians and patients. One article cites alarm fatigue as one of the top patient safety concerns in hospitals (MacDonald 2007). In a 31-day study across 461 adults in intensive care units, $88.8 \%$ of the 12,671 arrhythmia alarms were falsely detected (Drew, Harris, ZègreHemsey, Mammone, Schindler, SalasBoni, Bai, Tinoco, Ding \& Hu 2014). Other studies report similar numbers, indicating that alarm fatigue is a real phenomenon.

Typically, the methods used to identify the heart beats are straightforward signal processing algorithms that take advantage of the regular waveforms of either electrocardiogram (ECG) or arterial blood pressure (ABP) signals. In ECG signals, there exists a regular QRS complex. In signals with well-defined QRS complexes, executing signal processing algorithms that annotate heart beats at the R peaks achieves high accuracy. Likewise for the ABP signals, there exists a spike, albeit not as sharply defined as the QRS peak, that indicates the location of the heartbeat. In ABP, heart beat detection is further complicated by a delay between heartbeats and the pressure peaks. Standard methods for heart beat detection
![img-0.jpeg](img-0.jpeg)

Figure 1: Section of signal from example 1522 of Physionet 2014 Challenge's set-p2. In the left subsection you can see that the electrocardiogram has flat-lined. On the right, we conversely see an example where blood pressure has flat-lined, all within the same signal.
typically include signal processing algorithms that rely on a particular lead for a particular signal. This

naive approach is already problematic because of the potential for dropped signals. Figure 1 provides an example of dropped signals within a single piece of data. This shows that for a given patient, across a relatively short period of time, it is possible for either the ECG or the ABP signal to simply flat-line and yield no useful information. These dropped signals occur for a variety of reasons, including but not limited to technical malfunctions or the detachment of sensors due to patient movement. In these cases, any signal processing algorithm that naively depends on a single signal's lead will fail to provide useful data for extended periods of time.

The problem of dropped signals almost naturally suggests a solution in the form of a signal switching algorithm. One that evaluates whether the lead has flatlined, and if so, switches to a lead with a notable stream of data. This approach certainly works to a degree, but a naive application will fail due to events that disturb the signal and generate noise, otherwise known as artifacts. In Figure 2, the middle of the
![img-1.jpeg](img-1.jpeg)

Figure 2: Section of signal from example 1715 from Physionet 2014 Challenge's set-p2. In this subsection you can see that the electrocardiogram has an area with a significantly jittery signal.

ECG signal has a clear example of an artifact. The regular QRS complexes are disturbed, leaving a signal that bears no recognizable patterns. Artifacts can be the manifestation of a patient brushing their teeth, bumping into something, or simply rolling around in their sleep. They complicate the detection of heart beats, because the artifacts can corrupt the signals in a variety of ways, thereby rendering any naive switching algorithm insufficient. Ultimately, the goal is to robustly detect heart beats despite the occurrence of artifacts, noise, and dropped signals. In doing so, patient monitoring systems in hospitals can become much more efficient, reducing ICU false alarm rates.

Given all of this clinical data, we recognize the problem as one that can be solved through either a data-driven or a model-based approach. We could potentially treat the problem as a regression problem and allow the program to train on the Physionet data and develop its own interpretation and understanding of the problem. Alternatively, we can assume that the problem is an inherently biological problem, and take an approach that borrows from modern understanding of human physiology.

Because there exists a large corpus of research in the direction of human physiology, we choose the latter. Yet earlier, we have recognized that the data we are dealing with is inherently uncertain. In order to capture both the model and inherent uncertainty we approach the problem through a model-based probabilistic inference approach.

We develop a Dynamic Bayesian Network (DBN) to describe the interactions of the patient's physiological characteristics over time. In order to incorporate our beliefs about how artifiacts and noise

manifest themselves in data we also incorporate an observation model. Finally, we use particle filtering, which is a Sequential Monte Carlo (SMC) method, to perform combined state and parameter estimation on our non-linear, non-Gaussian model.

# 2 Physionet 

Before moving directly into the algorithm it is worth mentioning Physionet. Physionet is a research resource that offers access to a sizable supply of recorded physiological signals and their open source software. In addition, they hold challenges on a yearly basis, with last year's challenge pertaining to heart beat detection. We use several of the datasets provided by Physionet to evaluate our algorithm's performance.

### 2.1 Material

The first is the Physionet Challenge 2014 training set (set-p1), which is was a dataset released during the first phase of the challenge (Goldberger et al. 2000 (June 13)). There are 100 examples that are all relatively clean and artifact-free. The data is typically 10 minutes long or shorter and each record contains at least one ECG signal and at least one ABP signal. The sampling frequency is also consistent among these examples at 250 samples per second.

The next dataset set is the Physionet Challenge 2014 extended training set (set-p2), consisting of 100 records (Goldberger et al. 2000 (June 13)). These records contain signals that have more noise and artifacts than those of set-p1. The signals in set-p2 are mostly 10 minutes long, although there are occasionally shorter signals. The sampling frequency varies between 250 samples per second to 360 samples per second.

The final dataset we use is the Massachusetts General Hospital/Marquette Foundation (MGH/MF) Waveform Database provided by Physionet (Welch, Ford, Teplick \& Rubsamen 1991). The database consists of 250 recordings and represents a broad spectrum of physiologic and pathophysiologic states. Individual recordings vary in length from 12 to 86 minutes, and in most cases are about an hour long. The effective sampling frequency is 360 samples per second.

For these three datasets, reference beat annotations are available. These reference beat annotations represent the consensus of several expert beat annotators, and are used for determining the accuracy of the algorithms.

Beyond the datasets, we also make use of the GQRS and WABP functions, which are the basic beat detectors for ECG and ABP respectively provided by Physionet's WFDB Toolbox (Silva \& Moody 2014). In addition, we use other WFDB Toolbox functions for processing signals and annotations.

### 2.2 Related Work

Since Physionet held a challenge and collected many submissions, there are also quite a few bodies of work that make meaningful progress towards improving heart beat detection. The top six algorithms that were submitted to the Physionet 2014 Challenge, ordered by their performance in Physionet are Pangerc (Pangerc \& Jager 2014), Johnson (Johnson, Bechar, Andreotti, Clifford \& Oster 2014), Antink (Hoog Antink, Bruser \& Leonhardt 2014), De Cooman (De Cooman, Goovaerts, Varon, Widjaja \& Huffel 2014), Johannesen (Johannesen, Vicente, Scully, Galeotti \& Strauss 2014), and Vollmer (Vollmer 2014).

In general, most of the submissions involved a subset of a few typical techniques: pre-processing, a combination algorithm, and then post-processing. In addition most algorithms used some form of delay incorporation, either in their pre-processing or combination algorithm to account for the ABP delay. Finally, a few algorithms make use of signals outside of the ECG and ABP signals. It is worth noting that Pangerc, whose performance is significantly higher than the other applications involved reimplementing ECG and pulsatile-signal detection algorithms. For a recent review of the submissions, refer to the Physionet 2014 Challenge summary paper (Silva, Moody, Behar, Johnson, Oster, Clifford \& Moody 2015).

# 3 Methods - Algorithm 

### 3.1 Introduction

Dynamic Bayesian networks (DBNs) are widely used to model the processes underlying sequential data such as speech signals, financial time series, genetic sequences, and in our case, physiological signals. DBNs model a process using static parameters, hidden variables that evolve over time, and observations at each time step, as shown in Figure 3.

More specifically, for a partially observable Markov process with unobserved state variables $\left\{X_{t}\right\}_{t \geq 0}$, and observations $\left\{Y_{t}\right\}_{t \geq 0}$ that is parametrized by a static parameter space $\Theta$, the probabilistic model is defined as follows.

$$
\begin{aligned}
X_{0} & \sim p\left(x_{0} \mid \theta\right) \\
X_{t} \mid x_{t-1} & \sim p\left(x_{t} \mid x_{t-1}, \theta\right) \\
Y_{t} \mid x_{t} & \sim p\left(y_{t} \mid x_{t}, \theta\right)
\end{aligned}
$$

The first equation represents the initialization of state variables, which corresponds to the prior probability. The second equation represents the propagation model, which is based on transition probabilities from one state to another. For our propagation model, we implemented a drastically simplified model of human biometrics and then evolved variables in a physiological manner. The final equation represents the observation model, which corresponds to the probability of a particular observation given a certain state. In our case, our observations consisted of annotations and signal quality indices from signal detection algorithms.
![img-2.jpeg](img-2.jpeg)

Figure 3: A state-space model with static parameters $\theta . X_{1: T}$ are latent states and $Y_{1: T}$ are observations.

### 3.2 Sequential Monte Carlo

Given a probabilistic model and a sequence of observations, one can attempt to estimate the latent states. That is the problem of state estimation, also known as filtering: the process of computing the posterior

distribution of the hidden state variables given a sequence of observations. Exact filtering is often intractable except for specific cases, but approximate filtering using the particle filter (a sequential Monte Carlo method) is feasible in many applications (Arulampalam, Maskell, Gordon \& Clapp 2002) (Doucet \& Johansen 2011).

The specific method we use is Sequential Importance Sampling-Resampling (SIR), otherwise known as bootstrap filtering and particle filtering. This representation relies on approximating the posterior density, $p\left(x_{t} \mid y_{0: t}, \theta\right)$ function at any given time using a set of random particles that we recursively evolve. As the cardinality of the set grows, the approximation improves in accuracy.

We initialize the states of our particles based on the prior probabilities. We then propagate the state of the particles using the transition probabilities, weight based on the observation probabilities, and resample at each time step. Through this propagate-weight-resample scheme, particle filtering generates simulations that explore the likely portions of the latent probability space.

```
Algorithm 1: Sequential importance sampling-resampling (SIR)
    Input: \(N\) : number of particles;
    \(y_{0}, \ldots, y_{T}\) : observation sequence
    Output: \(\bar{x}_{1: T}^{1: N}\)
    initialize \(\left\{x_{0}^{i}\right\}\);
    for \(t=1, \ldots, T\) do
        for \(i=1, \ldots, N\) do
            sample \(x_{t}^{i} \sim p\left(x_{t} \mid x_{t-1}^{i}\right)\);
            \(w_{t}^{i} \leftarrow p\left(y_{t} \mid x_{t}^{i}\right)\);
            resample \(\left\{\frac{1}{N}, \bar{x}_{t}^{i}\right\} \leftarrow\left\{w_{t}^{i}, x_{t}^{i}\right\}\);
            \(\left\{x_{t}^{i}\right\} \leftarrow\left\{\bar{x}_{t}^{i}\right\} ;\)
```


# 4 Methods - Model 

Our approach relies on the assumption that human physiology follows a pattern that can be modeled in a Bayesian manner. Specifically, we construct a DBN that corresponds to human physiology, with static variables $\theta$ (e.g. resting heart rate), dynamic state variables $X_{i}$ (e.g. true heart rate) which define a propagation model, and observations $Y_{i}$ (e.g. ECG annotations and signal quality) which define an observation model. The propagation and observation models are described in the following sections and illustrated in Figure 5. We proceed to use the filtering techniques covered in the previous section to perform state estimation on the DBN we have constructed.

### 4.1 Propagation Model; $p\left(x_{t} \mid x_{t-1}, \theta\right)$

Our propagation model (transition model) encodes a DBN, and indicates our beliefs about the interdependent evolution of our relevant variables over time. The model makes use of nine variables to represent a simplified model of human physiology. Refer to Figure 4, to see the physical representation of a few of the propagation variables.

The first two variables are static parameters: RestHR and Latency, which represent the resting heart rate of the patient and the delay between ECG and ABP signals, respectively (Zong, Moody \& Mark 1998). These static parameters converge quickly during particle filtering.

![img-3.jpeg](img-3.jpeg)

Figure 4: This figure shows the physical representation of some of the propagation variables.

The next variables we cover are latent variables. The third variable is the TrueHR, which represents the belief of the patient's heart rate at a particular point in the signal. The fourth variable is the ECGPeak, which is a binary variable that represents whether there is a peak in the current window of the ECG signal. The ECGPeak variable evolves based on the TrueHR and the next variable, ECGLastPeak, which represents the last time we believed there was a peak in the ECG signal. The sixth and seventh variables are $A B P P e a k$ and $A B P L a s t P e a k$ which are analogous to the corresponding ECG variables, but incorporate the Latency variable. Note that in this model, the ECGPeak at time $t$ coincides with the $A B P P e a k$ at time $t+$ Latency. This means that the $A B P P e a k$ variable represents our final belief about heart beat annotations, because it incorporates both ECG and ABP information. The final two variables are ECGArtifact and ABPArtifact, which are binary variables that are used to label a signal as artifactual. For a more in-depth explanation, refer to the Propagation Model in Appendix A.

# 4.2 Observation Model; $p\left(y_{t} \mid x_{t}, \theta\right)$ 

The observation model (sensor model) encodes our beliefs about the functions we use to derive observations and the probability that the observations correspond to the current states. In the observation model there are six variables that we relate to the variables in our propagation model.

The first two variables are annotation observations, ECGAnn and $A B P A n n$. These binary variables represent whether the algorithms provided by Physionet, GQRS and WABP, found an annotation at the current time. The observation model describes a relationship between these variables and the corresponding Peak, LastPeak, and Artifact variables in the propagation model. The next two are heart rate observations, $E C G H R$ and $A B P H R$, which once again are derived using WABP and GQRS to give an estimate of the heart rate. These parameters are mainly associated with the TrueHR variable. Finally we

have two SQI observations, $E C G S Q I$ and $A B P S Q I$, which represent how trustworthy a particular signal is. The $E C G S Q I$ is calculated by comparing the results from two of Physionet's ECG signal detectors, and the $A B P S Q I$ is calculated by checking that the detections are within certain physiological boundaries (Johnson et al. 2014) (Sun, Reisner, Saeed \& Mark 2005) (Sun 2006). For a more in-depth explanation, refer to the Observation Model in the Appendix B.
![img-4.jpeg](img-4.jpeg)

Figure 5: This figure shows the propagation and observation model that encodes our Dynamic Bayesian Network. The grayed out variables correspond to observed variables.

# 4.3 Performing State Estimation 

Given our probabilistic heart beat model, we now use particle filtering to perform state estimation and to determine when heart beats occurred. Our particle filter follows SIR whereby we perform three steps recursively: propagation, weighting, and resampling.

First, we split our signals into 25 millisecond windows, and calculate the values of the observation model variables for each of these windows. Then, the particle filter assigns a prior belief to our set of particles (in our algorithm we use a set of 2000). For the propagation step we propagate the particles individually according to our transition model to acquire the state of the model one step into the future. Next, for each particle, we calculate a weight which is representative of the likelihood of that particle's realized state given the observations we have made at the corresponding time. The final recursive step is to resample the particles according to the weights we calculated in order to avoid the degeneracy problem, where the particles all have negligible weight (Doucet \& Johansen 2011).

We repeat the recursive steps above for the duration of the signal in a sequential fashion. At each step in the recursion we also save the average state of the variables across the particles, which is used to compose our actual heart beat annotations. Based on ABPPeaks, we backshift a distance of Latency and then annotate a beat only if enough particles are in the state that corresponds to a peak. This threshold is one of several hyperparameters within our algorithm that were tuned over the development of the filter.

The final annotations we use correspond to timesteps where enough particles were in a state of $A B P P e a k s$ backshifted by the Latency between ECGPeaks and ABPPeaks.

# 5 Results 

Now that we have established the algorithm, we discuss the performance of the algorithm on several datasets. In this section we compare results in terms of the sensitivity (recall) and positive predictivity (precision). The sensitivity represents the percentage of actual beats our algorithm annotated, and the positive predictivity represents the percentage of detections that corresponded to actual beats.

### 5.1 Results - Individual

The first example we discuss is record 1376 from set-p2. This record is an example where we make a large improvement over GQRS and WABP.
![img-5.jpeg](img-5.jpeg)

Figure 6: Example 1376 from set-p2. On the left we plot against the ECG signal, and on the right we plot against ABP signal. Both signals are plotted over a section of two seconds. The red dots signify annotations. On this example we achieved a sensitivity of 0.91835 and a predictivity of 0.98842 whereas GQRS had a sensitivity of 0.69051 and a predictivity of 0.99002 . The slightly misaligned beats on the left are likely due to an overestimated latency.

In Figure 6 we note that the particle filter can recover from spurious GQRS annotations on the left and spurious WABP annotations on the right, all within the same signal. Our algorithm performs well overall on record 1376, and this example illustrates its capacity for artifact recovery. Most of the improvement our algorithm achieves is in knowing when to trust a particular signal to the point that it will incorporate it within our observation model.

The next example we discuss is record 2664 from set-p2. This record demonstrates our improvement over GQRS and provides an illustrative example of signal quality and artifacts.

![img-6.jpeg](img-6.jpeg)

Figure 7: Example 2664 from the set-p2. On the left we depict the ECG signal quality observation over time. In the middle we depict the mean of the particles' $E C G A r t$ variable over time. On the right we depict the heart rate over time.
![img-7.jpeg](img-7.jpeg)

Figure 8: Example 2664 from set-p2. This visualizes an estimate of the scoring method from Physionet we used. Green indicates true positives, red is a false positive, and yellow is missed actual annotations. Note that this visualization is not the same as the method we used to collect the scoring.

In Figure 7, we see that our estimate of the ECGArtifact correlates strongly with the ECGSQI. Wherever the ECGSQI is low, our particle filter correspondingly believes there to be an artifact. The fact that the ECGArtifact variable is quite accurate serves as a proof of concept that our particle filter can track other biometric or sensor state in addition to heart beats. In addition, we see that the TrueHR matches the actual heart rate quite closely. This means we can potentially incorporate other variables, such as those that could determine the presence of arrhythmia or other information relevant to the general status of a patient, to create a more refined model.

Then, in Figure 8, we see a strong improvement over GQRS. Our algorithm has a sensitivity of 0.941 and a predictivity of 0.988 , whereas GQRS has a sensitivity of 0.343 and a predictivity of 0.975 . These numbers indicate that for example 2664, GQRS missed a lot of actual beats, but didn't make many false predictions, which is reflected in the figure as well. Overall, this example highlights the powerful recovery our algorithm elicited simply by combining GQRS and WABP annotations under a physiological model.

In our last record of interest, 1033 from set-p2, we observe a phenomenon we denoted as "double annotations" pictured in Figure 9. These double annotations are mainly due to artificial pacemakers and low dicrotic notches. This is where the signals are shaped in such a way that either the GQRS or WABP or both algorithms annotate an extra set of beats. Here we observe the case where both GQRS and WABP believe there to be a double annotation, resulting in our particle filter believing there to be a double annotations as well. These double annotation phenomena are the primary reason for our lower positive predictivity in the next results section. Recovering from double annotations is actually quite difficult within the generative capabilities of our probabilistic model, however through the introduction of new features the double annotations can potentially be ameliorated. Without other data about the signal, determining the presence of double annotations is infeasible.
![img-8.jpeg](img-8.jpeg)

Figure 9: Example 1033 from the set-p2. The red dots incidate annotations.

# 5.2 Results - Overall 

In order to generate these results, we took the top submissions on Physionet, downloaded their entries, and re-ran them against the exact same datasets we used. We then used Physionet's provided bxb function to compare the generated heart beat annotations with the reference ones and to determine the sensitivity and predictivity for a given record. Finally, we averaged the sensitivity and predictivity across all records from a given dataset. This was for the sake of consistency in our comparisons. While all the submissions ran without errors on set-p1 and set-p2, our algorithm, Pangerc's, and Johnson's did not run properly on some of the records in the MGH/MF Waveform Database. We omitted those records when calculating scores. The results for set-p1 (top left), set-p2 (top right), and the MGH/MF Waveform Database (bottom):




Overall, the performance from GQRS is nigh impossible to beat on set-p1, precisely because the data is so clean and regular. It seems highly unlikely that there is any statistical significance to be derived from set-p1. All algorithms perform extremely well, except for WABP which suffers primarily from delay.

In regards to set-p2, we start to observe some differentiation. Comparing against the other entries, we see that our particle filter ends up outperforming all algorithms in regards to sensitivity except for Pangerc on set-p2. Our predictivity does suffer due to double annotations, but we still perform well overall. This is fairly strong evidence that our algorithm is capable of accurately combining the information from multiple channels of signals. In set-p2 we see that the performance of the Pangerc submission is substantially better than the others. This is likely due to their use of custom ECG and BP pulse detectors. Their QRS detector (repdet) provided a much improved performance over GQRS on set-p2 in particular, likely due to their inclusion of a step in the detector to identify double annotations (paced beats) (Silva et al. 2015) (Pangerc \& Jager 2014). This step may account for Pangerc's improved performance over the algorithms that used GQRS.

Finally, for the MGH/MF Waveform Database, we note that the particle filter outperforms all other algorithms in predictivity, and does very well in the sensitivity aspect as well with approximately .929

sensitivity and .937 predictivity. In comparison to Pangerc and GQRS this is a great improvement, and in comparison to Johnson, we improve predictivity and only slightly lose out on sensitivity. Our algorithm was able to perform well on multiple datasets, which suggests that the improvement was fairly significant.

# 6 Discussion 

In this section, we discuss some of the interesting features of our algorithm. First, it is important to state that our algorithm is slower than other standard signal detection algorithms mainly because it is a simulation based filtering algorithm. In general, on the set-p1 (10 minutes signals), our algorithm takes 94.33 seconds on average to run on MATLAB r2015a (on a MacBook Pro with a 2.9 GHz Intel Core i5 processor and 8 GB 1867 MHz DDR3 memory), but it is worth noting that it is quite feasible for it to be implemented as an online algorithm. This is simply because particle filters process data sequentially.

We showed an example of double annotation in the previous section. In order to mitigate double annotations we would have to augment our model. One way to do this would be to incorporate information about the amplitude of the beat as an observation to determine if our algorithm should expect a double annotation, and determine peaks based off the new information. The model augmentations would likely be a few variables to probabilistically indicate the presence of double annotations and represent the amplitude of the signal.

Because there were so many other meaningful algorithms, it is worth comparing our own algorithm against the other top submissions. First of all, our algorithm inherently differed from the other approaches, and was the only one that focused on performing probabilistic inference on a Dynamic Bayesian Model. In terms of similarities, our algorithm slightly resembles the Johnson algorithm, because both algorithms use signal quality indices. However, not only do they focus on a deterministic switching, in the latter part of their algorithm they focus on the regularity of signals besides ECG and ABP as well. As a whole, our algorithm outperforms the others that relied on implementing a form of intelligent switching. Only Pangerc, who relied on their reimplemented beat detection algorithm (repdet) outperformed our own (Silva et al. 2015).

Another point of discussion is actually a point of differentiation between our algorithm and the others, which is our flexibility. With the flexibility of inputs, it becomes feasible to consider using alternate detectors to further strengthen our algorithm. One alternative would be to use the detectors used in the Pangerc submission, which should in theory greatly boost our performance.

Apart from performance concerns, we can consider the ease of implementation. Model based probabilistic inference approaches are becoming more and more appealing due to the emergence of probabilistic programming languages (PPL). A probabilistic programming language is a high-level language that makes it easy to represent probabilistic models and perform inference over them. PPLs enable domain experts who don't have enough experience in probability theory or machine learning to use state-of-the-art machine learning methodologies to perform meaningful inferences (Gordon, Henzinger, Nori \& Rajamani 2014). Because the problem we are analyzing is within the domain of physicians and clinicians, it would be best if we could empower them to create the physiological models they wished to represent on their own. As a proof of concept, we have also implemented our probabilistic model in a probabilistic modeling language called BLOG (Milch, Marthi, Russell, Sontag, Ong \& Kolobov 2007). We used BLOG's particle filtering engine to perform the state estimation, and our results agree with our MATLAB implementation. For physicians, they simply need to implement their model, and use the particle filter (or any other estimation technique) implemented in BLOG. For a glimpse at the BLOG

implementation, refer to Appendix D.1.

# 7 Conclusion 

Based on our results, we find that using particle filtering on our DBN model performs quite well. It matches or outperforms a majority of the top submissions for the Physionet 2014 Challenge. In regards to the default Physionet beat detector GQRS, we improve in set-p2 by about $4 \%$ in both sensitivity and positive predictivity. As a whole, our particle filter serves as a strong proof of concept that a probabilistic model based inference approach can robustly detect heart beats.

Our probabilistic model is not completely perfect, but some of our algorithm's advantages include: 1. Utilizes multi-channel information by incorporating the ECG-ABP peak delay (latency). 2. Flexible model - easy to incorporate new variables and relationships. 3. Flexible observations - easy to switch out GQRS and WABP for any other signal processing algorithms. 4. Consistent with a physiological perspective. 5. Can be implemented using a PPL. 6. Unlike many machine learning techniques, our model does not require a training set. Some of our disadvantages include: 1. Slower run time. One ten-minute signal takes approximately a minute and a half for the algorithm to run. 2. Depends on the signal processing methods heavily.

In terms of future work on the particle filter, we can incorporate the preprocessing mentioned in the other submissions for the sake of reducing noise. In addition, our algorithm only looks at one ECG and one ABP signal, when there are a multitude of other signals that could be utilized. Incorporating these would likely improve performance, as would initializing the delay based on one of the methods described in the other submissions. In the far future, this algorithm could be tweaked to directly detect arrhythmia. By placing emphasis on the artifacts and introducing arrhythmia variables, it would be possible to develop beliefs regarding these cardiac abnormalities. Since we have improved the detection rate for heart beats, it stands to reason we can improve the detection rate for the arrhythmia as well as for other problems that can be modelled physiologically.

## 8 Acknowledgements

We are thankful to Xiao Hu, Quan Ding, Yong Bai, Rebeca Salas-Boni and Daniel Schindler for helpful discussions.

# Supplemental Material 

## A Propagation Model

The propagation model (transition model) encodes interdependent evolution of our relevant physiological variables over time. The structure of the dependencies is observable in the figure in section 5.

## A. 1 RestHR

RestHR is a real-valued static variable that represents the resting heart of a particular patient, which is simply the patient's expected heart rate while at rest. The prior value is a Gaussian around the average heart rate as determined by patient demographics. It obeys the following static (i.e., identity) propagation function:

$$
\operatorname{Rest} H R_{t+1} \leftarrow \operatorname{Rest} H R_{t}
$$

## A.1.1 Latency

![img-9.jpeg](img-9.jpeg)

Figure 10: The blue lines represent heart beat annotations. The gray lines and circles are simply to highlight the annotated heart beat and the delay present in ART and PAP (the ABP signals).

In Figure 10, it is possible to see that the heartbeats fall on, or very near to, the R peaks in the ECG's QRS signals. Conversely, in the ABP signals the heart beat does not fall on the peaks pictured, but instead it falls a reliable distance before the peaks. In our model, Latency is an integer-valued static variable that represents this relationship between heart beats and the blood pressure. The prior value is a Gaussian

around 200 milliseconds. It obeys the following propagation function:

$$
\text { Latency }_{t+1} \leftarrow \text { Latency }_{t}
$$

# A. 2 TrueHR 

TrueHR is a real-valued variable that represents the heart rate of a patient at the current time. The prior value of the TrueHR starts off as a gaussian around the RestHR. Here norm means sampling from a gaussian distribution with a given $\mu$ and $\sigma$.

$$
\operatorname{TrueHR}_{0} \leftarrow \operatorname{RestingHR}_{0}+5 * \operatorname{norm}(\mu=0, \sigma=1)
$$

Since the true heart rate of a patient might vary over a few minutes where the resting heart rate might vary over a few months, the true heart rate is not a static variable. It obeys the following propagation function:

$$
\operatorname{TrueHR}_{t+1} \leftarrow .8 * \operatorname{TrueHR}_{t}+.2 * \operatorname{RestHR}_{t}+15 * \operatorname{norm}(\mu=0, \sigma=1)
$$

## A. 3 ECGPeak

ECGPeak is a boolean-valued variable that is 1 if there should be a beat annotated at the current timestep and 0 otherwise. ECGPeak's prior starts as 1 with a small probability (currently .01). It obeys the following propagation function:

$$
E C G P e a k_{t+1} \leftarrow \operatorname{Bernoulli}(P)
$$

We calculate $P$ dynamically. As time progresses, the $P$ parameter will change depending on the current values of the TrueHR and ECGLastPeak. First we define the difference between the current timestep and the lastpeak as diff $=t-E C G L a s t P e a k_{t}$. Then we define BeatWindow $_{t}=60 /\left(\right.$ window $\left.* \operatorname{TrueHR}_{t}\right)$, which is the number of windows per beat based on the current heart rate.

$$
\begin{aligned}
P=\text { binopdf } & \left(x=\max \left(\bmod \left(\text { diff }, \text { BeatWindow }_{t}\right), \bmod \left(\text { diff }, \text { BeatWindow }_{t}\right)+\text { BeatWindow }_{t}\right)\right. \\
& \left.n=3 / 2 * \text { BeatWindow }_{t}, p=2 / 3\right)
\end{aligned}
$$

Thus, we represent the probability according to repeated binomial distributions, as in figure 11. The reason for this calculation is to create a few important properties. The first is to create a memory that allows us to believe beats should occur based on the TrueHR and to not preclude beats even if we don't believe there to be a beat earlier on. It also has the convenient property of generally not allowing us to double annotate beats, because it's unlikely the heart will beat twice in a short span of time. The other reason is that the binomial distributed random variable $X$ with parameters $n$ and $p$ has an $E[X]=n p$ and $\operatorname{Var}[X]=n p(1-p)$. This means that we can control the expected value in our case to be BeatWindow and the variance to be $1 / 3 *$ BeatWindow, using our values of $n$ and $p$.

## A. 4 ECGLastPeak

ECGLastPeak is an integer-valued variable that represents the last time we believed there was a peak based on ECG. The prior for ECGLastPeak is a uniform distribution in the range of integers between [-BeatWindow, -1$]$. The ECGLastPeak helps to shift the expected location of all of the heartbeats,

![img-10.jpeg](img-10.jpeg)

Figure 11: This graph represents the value of $P$ as a function of $d i f f$ for a fixed TrueHR and window. This is an example with a TrueHR of 60 bpm and a window of .025 s .
because of the multimodal value of $P$ in the ECGPeak. The uniform sampling means that the prior believes the expected heartbeats may be shifted to cover all possible initializations. It obeys the following propagation function:

$$
E C G L a s t P e a k_{t+1}= \begin{cases}t+1 & \text { ifECGPeak }_{t+1}==1 \\ E C G L a s t P e a k_{t} & \text { ifECGPeak }_{t+1}==0\end{cases}
$$

In words, this equation states that the ECGLastPeak will change purely to record the last time ECGPeak was 1 .

# A. 5 ABPPeak 

$A B P P e a k$ is a boolean-valued variable that represents whether there is a peak based on the $A B P$ and the $E C G$. Since theoretically the $A B P P e a k$ should align with the ECGPeak while accounting for the Latency, it obeys the following propagation function (even for the prior):

$$
A B P P e a k_{t+1} \leftarrow\left(t==\operatorname{ECGLastPeak}_{t}+\operatorname{ParticleMean}\left(\text { Latency }_{t}\right)\right)
$$

Here, ParticleMean means that we take the mean across all the particles. This is admittedly unorthodox, but it means that we ameliorate the issue of double and triple annotations in adjacent locations for the $A B P P e a k$. If the particle filter had a while to learn the latency and let it converge, then this fix would be unnecessary, but, as is, this fix means that the particle filter's particles will not overly diverge at the $A B P P e a k$.

## A. 6 ABPLastPeak

$A B P L a s t P e a k$ is an integer-valued variable that represents the last time we believed there was a peak based on both ECG and ABP. The prior starts off as $E C G L a s t P e a k_{0}+$ Latency $_{0}$. It obeys the following propagation function:

$$
A B P L a s t P e a k_{t+1}= \begin{cases}t+1 & \text { ifABPPeak }_{t+1}==1 \\ A B P L a s t P e a k_{t} & \text { ifABPPeak }_{t+1}==0\end{cases}
$$

# A. 7 ECGArtifact and ABPArtifact 

ECGArtifact and $A B P A r t i f a c t$ are boolean-valued variables that represents whether we believe there is currently an artifact associated with either ECGPeak or ABPPeak, respectively. Their prior and propagations behavior is exactly the same. 1 represents an artifact and 0 represents no artifact. The prior belief for the artifacts starts off as 1 with a small probability (currently .01) It obeys the following propagation function:

$$
\text { Artifact }_{t+1} \leftarrow \operatorname{Bernoulli}\left(P_{A}\right)
$$

Here, $P_{A}$ represents the $\operatorname{Pr}\left(\operatorname{Artifact}_{t+1} \mid \operatorname{Artifact}_{t}\right)$, which is determined by the following conditional probability table:


This table represents a form of inertia. Given that there is currently an artifact, the probability that there continues to be an artifact is high. Likewise, it there is currently an absence of an artifact, the probability that there continues to be an absence is similarly high.

## B Observation Model

The observation model (sensor model) encodes our beliefs about the functions we use to derive observations and the probability that the observations correspond to the current states. The structure of the dependencies is observable in the figure in section 5.

## B. 1 Annotation Observations

These are the $A B P A n n$ and the $E C G A n n$ variables in the model. The observations are derived by using the WABP and GQRS algorithms that are provided by Physionet. The algorithms simply use a specified window size and see if the signal processing algorithms place any annotations within a given window. If so, then the Ann observation is set to be true (1), and otherwise it's set to be false (0). Then, we define the probability of the annotations given the states according to the following probability table:


In the case that there is a peak and there is no artifact, then the belief that there should be an annotation is quite high (.99), because there is high likelihood of signal accuracy. Correspondingly the belief that there should not be an annotation is quite low (.01).

In the case that there is a peak and there is an artifact, then the belief that there should be an annotation is lower than without an artifact (.7), because the artifact means that we are not entirely able to trust the signal. Correspondingly the belief that there should not be an annotation is higher than without an artifact (.3). In general when we fix the other states, the presence of an artifact makes our annotation beliefs less certain.

Next in the case that there is no peak and no artifact, BeatProb should represent the likelihood that the observation can be trusted. Since the probability of the annotation occuring in this case truly depends on the LastPeak and the TrueHR, we end up calculating it in the same way as the $P$ for the ECGPeak. First we define the difference between the current timestep and the lastpeak as diff $=t-$ LastPeak. Then we define BeatWindow $=60 /($ window $*$ TrueHR $)$, which is the number of windows per beat based on the current heart rate.

$$
\begin{aligned}
\text { BeatProb }=\text { binopd } f(x & =\max (\bmod (d i f f, \text { BeatWindow }), \bmod (d i f f, \text { BeatWindow })+\text { BeatWindow }) \\
& n=3 / 2 * \text { BeatWindow }, p=2 / 3)
\end{aligned}
$$

Then, we know that the probability of the annotation not occuring will simply be $1-$ BeatProb.
Finally in the case that there is no peak and an artifact, we can apply what we used earlier and say that the presence of an artifact makes our belief about the annotation less certain. So if we strongly believe there would be an annotation, in the case of an artifact, we only moderately believe there would be an annotation. Likewise if we don't believe there would be an annotation, then an artifact would make us moderately not believe in an annotation. This means that we can simply represent the NormBeatProb according to the following definition:

$$
\text { NormBeatProb }=\text { mean }(.5, \text { BeatProb })
$$

# C Heart Rate Observations 

These are the $W A B P H R$ and the $G Q R S H R$ variables in the model (collectively called HRobs variables). The observations are derived by using the WABP and GQRS algorithms that are provided by Physionet. The algorithms simply use a specified window size and have a sliding window that computes the local heart rate. The HRobs observations are set accordingly. Then, we define the probability of the observations given the states according to the following:

$$
\operatorname{Pr}(H R o b s \mid \text { States })=\operatorname{normpdf}(\text { TrueHR }, H R o b s, 1 / 4 * H R o b s)
$$

Here, normpdf corresponds to the probability density function of a Gaussian random variable with the given parameters.

## D SQI Observations

These correspond to the $E C Q S Q I$ and $A B P S Q I$ variables. ECGSQI is calculated by taking two signal processing algorithms and comparing them beat by beat. It was derived using the ecgsqi function that was

developed in another Physionet submission (Johnson et al. 2014). In particular, we use gqrs (unpublished algorithm optimized for sensitivity) and wqrs (open source algorithm optimized for adult human ECGs). The number of beats that match between the two algorithms is reported as a real number between 0 and 1. $A B P S Q I$ is calculated by checking to see if the pressure, the mean arterial pressure, the heart rate, the pulse pressure, and a variety of other physiologic details are within normal ranges or not. If everything is in a normal range, $A B P S Q I$ is 1 , otherwise it is 0 . This was also derived from the abpsqi function in the same Physionet submission, which was in turn borrowing from other publications (Sun et al. 2005) (Sun 2006).

The $S Q I$ observations are used to choose which observations to depend on. If the $E C G S Q I<.8$ and $A B P S Q I==1$, then we weight based on the ABP annotations and heart rates, otherwise we weight based on the ECG annotations and heart rates.

# D. 1 BLOG Code - Propagation Functions 

The following code is the propagation model represented in the BLOG language:

```
// Functions
random Real Rest_HR(Timestep t) ~
    if t == 00 then
        Gaussian(avg_hr, 10)
    else
        Rest_HR(prev(t));
random Real True_HR(Timestep t) ~
    if t == 00 then
        Gaussian(Rest_HR(t), 5)
    else
        Gaussian(.2*Rest_HR(prev(t)) + .8*True_HR(prev(t)), 1);
random Integer ECG_Art(Timestep t) ~
    if t == 00 then
        Bernoulli(.01)
    else case ECG_Art(prev(t)) in {
        0 -> Bernoulli(.01),
        1 -> Bernoulli(.99)
    };
random Integer ECG_Peak(Timestep t) ~
    if t == 00 then
        Bernoulli(.01)
    else
        Bernoulli(binompdf(round(60/(w_off*True_HR(prev(t)))), 2.0/3.0,
            (toInt(t)-ECG_Last_Peak(prev(t)))%round(60/(w_off*True_HR(prev(t)))));
random Integer ECG_Last_Peak(Timestep t) ~
    if t == 00 then
        UniformInt(-round(60/(w_off*True_HR(t))), -1)
```

```
    else
        if ECG_Peak(t) == 1 then
            toInt(t)
    else
        ECG_Last_Peak(prev(t));
random Integer ABP_Art(Timestep t) ~
    if t == 00 then
        Bernoulli(.01)
    else case ABP_Art(prev(t)) in {
        0 -> Bernoulli(.01),
        1 -> Bernoulli(.99)
    };
random Integer ABP_Peak(Timestep t) ~
    if (ECG_Last_Peak(t) + Latency) == toInt(t) then
        1
    else
        0;
random Integer ABP_Last_Peak(Timestep t) ~
    if t == 00 then
        ECG_Last_Peak(t) + Latency
    else
        if ABP_Peak(t) == 1 then
            toInt(t)
    else
        ABP_Last_Peak(prev(t));
```


# D. 2 BLOG Code - Observation Functions 

The following code is the observation model represented in the BLOG language:

```
// Functions
random Integer ECG_Ann(Timestep t) ~
    if ECG_Peak(t) == 1 then
        if ECG_Art(t) == 1 then
            Bernoulli(.7)
        else
            Bernoulli(.9)
    else
        if ECG_Art(t) == 1 then
            Bernoulli((binompdf(round(60/(w_off*True_HR(t))), 2.0/3.0,
                (toInt(t)-ECG_Last_Peak(t))%round(60/(w_off*True_HR(t)))) + .5)/2)
        else
            Bernoulli(binompdf(round(60/(w_off*True_HR(t))), 2.0/3.0,
                (toInt(t)-ECG_Last_Peak(t))%round(60/(w_off*True_HR(t)))));
```

```
random Real ECG_HR(Timestep t)
    Gaussian(True_HR(t), abs(True_HR(t))/4);
random Integer ABP_Ann(Timestep t)
    if ABP_Peak(t) == 1 then
        if ABP_Art(t) == 1 then
            Bernoulli(.7)
        else
            Bernoulli(.9)
    else
        if ABP_Art(t) == 1 then
            Bernoulli((binompdf(round(60/(w_off*True_HR(t))), 2.0/3.0,
                (toInt(t)-ABP_Last_Peak(t))%round(60/(w_off*True_HR(t)))) + .5)/2)
        else
            Bernoulli(binompdf(round(60/(w_off*True_HR(t))), 2.0/3.0,
                (toInt(t)-ABP_Last_Peak(t))%round(60/(w_off*True_HR(t)))));
random Real ABP_HR(Timestep t)
    Gaussian(True_HR(t), abs(True_HR(t))/4);
```


# D. 3 Running BLOG 

The following is the shell script we ran to execute the blog particle filter.
\#!/bin/sh

```
time ./../../blog/dblog \
    prop_fn.dblog \
    query.dblog \
    obs_fn.dblog \
    obs.dblog \
    -n 1000 -o out.json
```

The query.dblog and obs.dblog files contained the data we wanted to load. This command ran the particle filter with 1000 particles and put the output into the out.json file. Note: we will be making the Matlab and BLOG code we wrote available at a later date.