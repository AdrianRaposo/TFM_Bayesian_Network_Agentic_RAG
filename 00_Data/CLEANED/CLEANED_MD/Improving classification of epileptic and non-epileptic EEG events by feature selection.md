# Citation for published version: 

E. Pippa, et al, "Improving classification of epileptic and nonepileptic EEG events by feature selection", Neurocomputing, Vol. 171: 576-585, July 2015.

DOI:
https://doi.org/10.1016/j.neucom.2015.06.071

## Document Version:

This is the Accepted Manuscript version.
The version in the University of Hertfordshire Research Archive may differ from the final published version. Users should always cite the published version of record.

## Copyright and Reuse:

Copyright © 2015 Elsevier B.V. All rights reserved.
This Manuscript version is distributed under the terms of the Creative Commons Attribution licence (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted re-use, distribution, and reproduction in any medium, provided the original work is properly cited.

## Enquiries

If you believe this document infringes copyright, please contact the Research \& Scholarly Communications Team at rsc@herts.ac.uk

# Improving Classification of Epileptic and Non-Epileptic EEG Events 

## by Feature Selection

* Evangelia Pippa ${ }^{1}$, Evangelia I. Zacharaki ${ }^{1}$, Iosif Mporas ${ }^{1}$<br>Vasiliki Tsirka ${ }^{2}$, Mark P. Richardson ${ }^{2}$, Michael Koutroumanidis ${ }^{2}$ and Vasileios<br>Megalooikonomou ${ }^{1}$<br>${ }^{1}$ Multidimensional Data Analysis and Knowledge Management Laboratory<br>Dept. of Computer Engineering and Informatics, University of Patras<br>26500 Rion-Patras, Greece<br>${ }^{2}$ Dept. of Clinical Neurophysiology and Epilepsies<br>Guy's \& St. Thomas' and Evelina Hospital for Children, NHS Foundation Trust/ King's College,<br>London, United Kingdom<br>*Corresponding Author's email: pippa@ceid.upatras.gr


#### Abstract

Correctly diagnosing generalized epileptic from non-epileptic episodes, such as psychogenic non epileptic seizures (PNES) and vasovagal or vasodepressor syncope (VVS), despite its importance for the administration of appropriate treatment, life improvement of the patient, and cost reduction for patient and healthcare system, is rarely tackled in the literature. Usually clinicians differentiate between generalized epileptic seizures and PNES based on clinical features and videoEEG. In this work, we investigate the use of machine learning techniques for automatic classification of generalized epileptic and non-epileptic events based only on multi-channel EEG data. For this purpose, we extract the signal patterns in the time domain and in the frequency domain and then combine all features across channels to characterize the spatio-temporal manifestation of seizures. Several classification algorithms are explored and evaluated on EEG epochs from 11 subjects in an inter-subject cross-validation setting. Due to large number of features feature ranking and selection is performed prior to classification using the ReliefF ranking algorithm within two different voting strategies. The classification models using feature subsets, achieved higher accuracy compared to the models using all features reaching 95\% (Bayesian Network), 89\% (Random Committee) and 87\% (Random Forest) for binary classification (epileptic versus non-epileptic). The results demonstrate the competitiveness of this approach as opposed to previous methods.

# 1. Introduction 

One of the most common and challenging medical cases in everyday clinical practice is that of patients reporting one or more episodes of paroxysmal loss of consciousness or altered awareness. The management of these medical cases may be proven to be demanding, time consuming and expensive and finally, in spite of the extensive and exhaustive investigation, the underlying diagnosis may remain elusive $[1,2,3]$. The differential diagnosis that a clinician usually faces is mainly that of an epileptic seizure, a possible psychogenic non epileptic seizure (PNES) and a probable vasovagal syncope (VVS).

The diagnosis of epilepsy and its differentiation from other causes of TLoC is typically based on historical information and is assisted by specific tests [2]. However clinical information is commonly fragmented or even missing because patients may have limited or no recall of the event and a witness account might not be available to describe diagnostically decisive clinical phenomena [1,2]. Even when a witness is available, diagnosis may be difficult and often remains uncertain because convulsive syncope, a seizure-like reaction resulting from global cerebral hypoperfusion, can mimic epileptic seizures [3,4]. Agreement between physicians as to the nature of a single event may also be limited [5]. Such diagnostic uncertainty has cost both in terms of mortality and ongoing morbidity and in terms of the financial burden associated with hospitalization and repeated investigations.

Epileptic seizures are brief episodes of abnormal excessive or synchronous neuronal activity in the brain of patients suffering from epilepsy [6]. During an epileptic seizure there are several specific changes recorded in the electroencephalogram (EEG) which is a sensitive and important test used to evaluate patients with suspected epilepsy. There are certain characteristic ictal neurophysiological patterns that support the identification and detection of epileptic events and postictal and/or interictal abnormalities that can provide supplementary information. Fig. 1 shows generalized spike wave abnormalities from an epileptic patient. Specifically, there is a burst of generalized $3-5 \mathrm{~Hz}$ spike and slow wave complex lasting approximately 5 secs.

## FIGURE 1

Pshychogenic non-epileptic seizures (PNES) are sudden paroxysmal changes in behavior or consciousness, that resemble epilepsy but are not accompanied by the electrophysiological changes that characterize an epileptic seizure [7]. Although the clinical history can help differentiate these episodes,

it is not unlikely to have inconclusive and insufficient event description by the patient and witnesses, not being able to confidently exclude an underlying epileptic disorder. In these cases the diagnosis of PNES can be supported by video-EEG monitoring, especially if a psychogenic event is captured, since in the case of PNES there are no specific EEG changes. Fig 2 shows an EEG fragment during a PNES. No EEG correlates can be seen and the recording is frequently marred by muscular artifacts.

# FIGURE 2 

Vasovagal or vasodepressor syncope is a common type of syncope and various mechanisms have been postulated for explaining the characteristic association of hypotension and bradycardia. The term "vasovagal" was introduced by Lewis [8] to indicate that both blood vessels and heart were implicated and since atropine reversed the bradycardia but not the hypotension he considered vasodilatation as the primary responsible factor. During a vasovagal syncopal attack there may be some characteristic EEG changes starting with progressive generalized theta slowing of background rhythms followed by sometimes hypersynchronous delta activity of high voltage, (beta / alpha $\rightarrow$ theta $\rightarrow$ delta) and appearance of progressively lower voltage rhythms until isoelectric suppression [9,10] (see Fig. 3). This pattern is progressively reversed after the patient's fall, during his/her recovery. These changes do not include any ictal activity.

## FIGURE 3

Several methods have been proposed for the classification of EEG captured events into epileptic or normal [11,12,13,14,15]. The problem of the discrimination between ictal and interictal EEG signals has been studied [16], too. However, only a few studies deal with the differentiation between epileptic and other paroxysmal episodes of loss of consciousness such as PNES and vasovagal syncope. It is worth to note that the discrimination between different types of non-epileptic events is considerably more useful in diagnostic procedure given the semiological resemblance between the aforementioned paroxysmal attacks. Furthermore, according to [7] the one third of PNES patients may have clinical convincing GrandMal like seizures. This makes discrimination between PNES and epileptic seizures a challenging task, especially in an online monitoring system for automatic detection of epileptic events, such as [17], where false alarms caused by events similar to epilepsy are undesired.

To the best of our knowledge, only a few studies have been proposed in the literature for automated classification between epileptic and non-epileptic pathological events from EEG. Poulos et al. [18] proposed an algorithm which estimates a number of auto-correlated coefficients extracted from

an appropriately selected epileptic EEG segment and examines whether these coefficients are correlated with the coefficients of the unknown EEG segments in order to classify the latest into epileptic or non-epileptic. Their algorithm obtained a sensitivity of $83 \%$ for $90 \%$ specificity. Papavlasopoulos et al. [19] trained a LVQ1 neural network on an appropriately extracted set of autocorrelation coefficients (codebook) and used the resulting model to classify the corresponding feature vectors of the unknown EEG segments. The LVQ1 network achieved $86 \%$ accuracy. The feature extraction methods of the aforementioned classification frameworks, as well as the achieved results, can be found in [20]. Statistical analysis of the results based on chi-square test showed that the LVQ neural network method is superior than the cross-correlation one [20].

Regarding the features used for the classification of EEG segments the relevant works in the literature are considerably more. In the majority of them, the analysis is based on the estimation of the EEG channels' spectral magnitude [11, 15, 21, 22]. Other EEG features that have been reported are the autoregressive filter coefficients, the continuous and discrete wavelet transform, as well as energy per brain wave (delta, theta, alpha, beta, gamma) bands [15,21, 23]. Finally, time domain features have been proposed, such as zero-crossing rate [24] and statistics of the EEG samples per channel [15,21].

In this study, we evaluate a large set of time and frequency domain features which have been widely used for the analysis of EEG signals in the literature. In addition to the reported evaluations found in the literature, we extend the non-epileptic class to both PNES and VVS events. The diagnosis of epilepsy is more challenging compared to the detection of seizure onset due to the semiological resemblance between epileptic and non-epileptic events, especially when video-EEG monitoring is not incorporated [25]. Also, the classification of abnormal episodes into different types requires a broad knowledge of EEG patterns across patients, while seizure detection can rely on patient-specific models which are easier to learn, especially for generalized seizures [26]. For the evaluation, we examined a number of different classification algorithms. Our classification methodology can be used as part of our previous seizure detection architecture [26,27] in order to discriminate the detected events into epileptic or non-epileptic.

In a further step, feature ranking investigation using two different strategies (one based on frequency of feature appearing in a specific rank and the other based on sum of the weights assigned by the ReliefF ranking algorithm) was performed. The classification models using subsets of N best features were evaluated and revealed the most significant features for the classification task.

The rest of this paper is organized as follows. In Section 2 the classification methodology is presented and details about the evaluation data are provided. Section 3 describes the experimental protocol followed and presents the achieved results. Finally, in Section 4 we conclude this work.

# 2. Material and methods 

### 2.1 Methodology for classification of generalized epileptic and non-epileptic events

The presented architecture for classification between generalized epileptic and non-epileptic EEG events is part of an end-to-end system for monitoring and analysis of brain disorders, the ARMOR framework [17]. Within the ARMOR framework patients suffering from seizures are monitored through sensors and the multi-parametric data are processed automatically (real-time by software tools) or semi-manually (offline with the support of software tools and visualizations) by neurology experts $[26,27]$.

The proposed classification methodology can be used as additional module after the seizure detection and focal-vs-generalized events classification components [26,27] in order to discriminate the detected events into generalized epileptic, manifested by Generalized Spike Wave discharges (GSW) or non-epileptic, such as PNES and VVS. The block diagram of the overall architecture is illustrated in Figure 4.

## FIGURE 4

Initially, the multidimensional EEG data are preprocessed by applying notch filtering (at 50 Hz ), baseline correction and re-sampling at 250 Hz (in order to obtain a common resolution level for all data coming from different patients and acquisition systems). Frame blocking of the incoming EEG streams to epochs of constant length $w$ ( $=2$ seconds ) is performed with constant time-shift and without timeoverlap between successive epochs. Each epoch is a $N \times w$ matrix, where $N$ is the number of selected EEG electrodes. A large number of features is extracted for each one of the $N$ electrodes to characterize the temporal patterns and frequency content of each epoch. The extracted time domain and frequency domain features from all electrodes are concatenated to a single feature vector as a representative signature for each epoch. Details on the type of extracted features are provided in section 2.3 .

All epochs are used as input to ARMOR's seizure detection module which detects paroxysmal events. The epochs classified as normal are ignored whereas epochs classified as seizure are further

entered to the seizure type classifier. In this final step, models for binary classification between generalized epileptic or non-epileptic events (PNES or VVS), which have been previously built in a training phase, are used in order to label the epochs. Each epoch is classified independently and no temporal constraints (across epochs) are applied, such as taking into consideration the class label of the precedent or subsequent epoch or the total event duration.

During the training phase of the classification architecture, epochs with known class labels (labeled manually by medical experts) are used to train binary classification models, i.e. generalized epileptic (GSW) vs non-epileptic (PNES and VVS).

During the test phase the unknown multidimensional EEG signal is preprocessed and parameterized with similar setup as in the training phase. Each extracted feature vector is provided as input to the seizure detector and according to the decision to the seizure classifier.

# 2.2 Data 

The previously described classification methodology was evaluated on multi-parametric recordings performed within the ARMOR project [17]. The recordings were performed in the Department of Clinical Neurophysiology and Epilepsies in St Thomas' Hospital in London and acquired from 11 patients in total. All participants had at least one of their typical epileptic or non epileptic events captured during the recording procedure. The epileptic group, consisted of patients with known diagnosis of idiopathic generalized epilepsy, manifested clinically with absence seizures and they had at least one clinical episode captured during the recording associated with generalized spike wave discharges on the EEG. The non epileptic group included patients who had sustained a vasovagal syncope (2 participants) or a psychogenic non epileptic attack (5 participants) during their monitoring. The epilepsy group contains 105 generalized seizures while the non-epilepsy groups include 21 events (19 PNES and 2 VVS). Patients with focal seizures were excluded from this analysis.

The recordings were performed using conventional AgCl EEG electrodes positioned according to the extended international 10-20 system. A subset of the main EEG channels was selected for analysis which included the following channels: Fp2, F8, F4, T4, C4, A2, P4, T6, O2, Fp1, F7, F3, A1, C3, T3, P3, T5, O1, Fz, Cz, Pz. The recordings were manually annotated by expert Neurologists of the King College London. Only epochs during paroxysmal events were considered for training and for testing. All data were stored in EDF+ formatted files [28].

# 2.3 Feature Extraction and Classification Algorithms 

After preprocessing, time domain and frequency domain features were extracted for each epoch. In particular, each of the EEG channels was parameterized using the following features: (i) timedomain features: minimum value, maximum value, mean, variance, standard deviation, percentiles ( $25 \%, 50 \%$-median and $75 \%$ ), interquartile range, mean absolute deviation, range, skewness, kyrtosis, energy, Shannon's entropy, logarithmic energy entropy, number of local maxima and local minima, zero-crossing rate, and (ii) frequency-domain features: 6-th order autoregressive-filter (AR) coefficients, power spectral density, frequency with maximum and minimum amplitude, the power of continuous wavelet transform using symlet 5 mother wavelet of scale 25 and 32, the power of discrete wavelet transform with mother wavelet function Daubechies 16 and decomposition level equal to 8. This resulted to 55 variables for each of the $N=21$ EEG channels producing a feature vector of dimensionality equal to 1155 in total.

The computed feature vectors, V, were used to train classification models. In order to evaluate the ability of the above features to discriminate between epileptic and non-epileptic epochs we examined several classification algorithms, including BayesNet [29,30], RandomCommittee, Random Forest [31], IBk [32] and SMO [33,34] with RBF kernel, which were implemented by the WEKA machine learning toolkit [35]. The classifiers in our study were selected in an attempt to evaluate representative algorithms for each one of the main categories of machine learning classification methods including probabilistic networks (BayesNet), decision trees (RandomForest), support vector machines (SMO), ensemble classifiers (RandomCommittee and RandomForest) but also simple methods such as k nearest neighbors (IBk).

During the test phase, the EEG recordings were pre-processed and parameterized as during training. Each classification model was used to label each of the detected seizure epochs. In the present evaluation no additional rules (e.g. knowledge based rules regarding events duration) were applied on the classification decision .

Evaluation was performed in a leave-one-out cross-validation setting. Specifically, each time one subject was left-out for testing, while the rest of the subjects were used for training. For the left-out subject, all epochs between seizure onset and offset were used as testing samples. Table 1 shows the number of epochs that were extracted from each subject during the seizure(s).

The purpose of this study was to evaluate the seizure classification module, thus only paroxysmal events were used for training and testing of the classifiers. Evaluation of the total ARMOR framework may include the combined use of seizure detection and seizure classification in future work.

# 2.4 Feature Ranking and Feature Subsets Evaluation 

In a further step we examined the discriminative power of the extracted features for the classification of epileptic and non-epileptic EEG events. The ReliefF algorithm [36] (which is an extension of an earlier algorithm called Relief [37]) was used for estimating the importance of each feature in binary classification (generalizing to polynomial classification by decomposition into a number of binary problems). In the ReliefF algorithm the weight of any given feature decreases if the squared Euclidean distance of that feature to nearby instances of the same class is more than the distance to nearby instances of the other class. ReliefF is considered one of the most successful feature ranking algorithms due to its simplicity and effectiveness [38, 39,40] (only linear time in the number of given features and training samples is required), noise tolerance and robustness in detecting relevant features effectively, even when these features are highly dependent on other features [38,41]. Furthermore, ReliefF avoids any exhaustive or heuristic combinatorial search compared with conventional wrapper methods and usually performs better compared to filter methods due to the performance feedback of a nonlinear classifier when searching for useful features [40].

In this study, ranking is performed by following a leave-one-out strategy on the available subjects. Specifically, for each leave-one-out experiment, feature ranking is performed using the ReliefF algorithm in each training subset. We combine the rankings of all leave-one-out experiments and calculate the total rank of features using two different strategies. The first strategy calculates the total rank of features according to the frequency of a feature appearing in a specific rank. For example the top-ranked feature is assumed to be the one that more frequently has the highest ranking score, regardless of the distribution of the scores it receives across experiments. The second strategy calculates the total rank of features according to the sum of the weights assigned by ReliefF in each training set. We examined the performance of the method, in terms of accuracy, sensitivity and specificity, for different number of N-best features ( $\mathrm{N}=10,20,30, \ldots 100,200,300, \ldots, 1100$ ), with respect to the above strategies of feature ranking.

# 3. Results and Discussion 

The classification methodology presented in Section 2.1 was evaluated using the classification algorithms and the cross-validation scheme described in Section 2.3. The accuracy, sensitivity and specificity are defined as:

$$
\begin{aligned}
& \text { accuracy }=\frac{T P+T N}{T P+F P+T N+F N} \\
& \text { sensitivity }=\frac{T P}{T P+F N} \\
& \text { specificity }=\frac{T N}{F P+T N}
\end{aligned}
$$

where TP denotes the true positives, TN the true negatives, FP the false positives and FN the false negatives. The results of the method using all features are shown on the left of Table 2. Here we consider the epileptic class as the positive and the non-epileptic class (PNES or VVS) as the negative.

## TABLE 2

As can be seen in Table 2, the overall highest accuracy of the proposed methodology for classification between epileptic and non-epileptic EEG events is $86 \%$ for BayesNet classification. RandomCommittee and Random Forest classification models follow with $83 \%$ and $74 \%$ accuracy, respectively. For the classifier with the highest accuracy (BayesNet), the sensitivity (or recall), i.e. the fraction of actual epileptic events which are correctly identified as such, is $92 \%$ and the specificity, i.e. the proportion of non-epileptic events (either PNES or VVS) which are correctly classified as such, is $78 \%$.

In a further step, we applied feature ranking using the ReliefF algorithm and the two strategies described in Section 2.4. The performance of the classification, in terms of accuracy, for different number of N-best features ( $\mathrm{N}=10,20,30 \ldots, 100,200,300, \ldots, 1100$ ) and for each algorithm separately are shown in Fig. 5 for the 1st ranking strategy and in Fig. 6 for the 2nd ranking strategy.

## FIGURE 5

## FIGURE 6

As can be seen in the above figures the highest classification accuracy is achieved when a small subset of discriminative features are used. Specifically, when the 1st ranking strategy is used the highest accuracy is achieved for a subset of 10 best features with a percentage of $95 \%$ for the Bayesian

Network, which is sufficiently high in comparison to the accuracy achieved when all features are used. Similarly, Random Committee and Random Forest achieve their highest accuracies for a subset of 300 and 200 best features respectively. The reported accuracies for these subsets of features are $92 \%$ and $87 \%$ for each algorithm respectively. IBk and SMO follow with an accuracy of $86 \%$ when a subset of 40 best features is used and $87 \%$ for a subset of 200 best features, respectively.

The 2nd ranking strategy shows similar behavior. For the Bayesian Network the highest accuracy (94\%) is achieved for a subset of 50 best features. Random Committee, Random Forest, IBk and SMO follow with $85 \%$ for a subset of 70 best features, $89 \%$ for a subset of 50 best features, $84 \%$ for a subset of 70 best features and $90 \%$ for a subset of 60 best features, respectively.

In general, Random Forest and Random Committee seem to be the less stable algorithms, SMO on the other hand, although not the most accurate classifier, shows a more stable behavior as function of number of retained features, with the accuracy decreasing significantly for more than 200 features.

Tables 3 and 4 show the 50 best features according to the ranking strategy 1 and 2 respectively.

# TABLE 3 

## TABLE 4

As can be seen, in general the two ranking strategies overall agree. Both of them rank features $n \min$ (number of local minima), nmax (number of local maxima), aryule3 (the 3rd coefficient of 6th order autoregressive filter), minfreq (frequency with minimum power ), cwt25 and cwt32 (the coefficients of continuous wavelet transform using symlet 5 mother wavelet of scale 25 and 32) in the top 50 features.

The number of local minima ( $n \min$ ) and the number of local maxima ( $n \max$ ) seem to be the features with the highest discriminative ability. Since these features measures the smoothness of the signal it seems that the smoothness of the epileptic epochs is different from the one of non-epileptic epochs and aids the discrimination among them. Such a claim can be verified from the distributions of the values of the $n \min$ (see Fig. 7) and $n \max$ (see Fig. 8) features for the epileptic and non-epileptic class.

## FIGURE 7

## FIGURE 8

In both figures 7 and 8 , the blue boxes indicate the distribution of the feature values on the epileptic class and the black boxes the distribution of the feature values on the non-epileptic class. As can be seen, there is a perfect discrimination between the epileptic and non-epileptic main boxes with the non-

epileptic epochs having a significantly larger number of local minima and maxima indicating less smooth signal compared to the generalized spike waves. The only overlap is observed between the extreme values of two classes (whiskers of the boxplots). The evaluation of our framework using only these two features ( $n \min$ and $n \max$ ) extracted from all the available channels resulted in $91 \%$ accuracy for $92 \%$ sensitivity and $89 \%$ specificity. The performance in terms of accuracy increases slightly when nmin and nmax are extracted from the 5 best channels (Fp1, T4, T5, F7, Fp2), reaching $92 \%$. This increase indicates that the frontotemporal regions in the brain covered by the aforementioned channels might be more important in discriminating generalized spike waves from PNES or VVS. The next most important features for discriminating epileptic from non-epileptic events are aryule3, minfreq and cwt25 and cwt32. The autoregressive model specifies whether the EEG epoch depends linearly on its own previous values by expressing the signal with lagged terms of itself. In particular, the AR model residual (i.e. the prediction error ) shows how possible is to model each sample as a linear combination of its previous ones. The lower absolute values of the AR coefficients of the non epileptic class (see Fig. 9 for the aryule3 feature values) indicates that the signal of the non-epileptic class is much more noisy and stochastic-like compared to the epileptic signals which seem to be more structured and deterministic-like. Such an experimental result is consistent with our intuition about the two types of signals and the clinicians description of the events.

# FIGURE 9 

Differentiation is also observed on the frequency with the minimum power (minfreq) in the spectrogram of epileptic and non-epileptic epochs (see Fig. 10), with the minfreq of the epileptic class having a much greater range of values compared to the non-epileptic class in which the minfreq values are clustered around 50 Hz . Note that this finding is not due to notch filtering since the same preprocessing was applied to all data (both epileptic and non-epileptic).

## FIGURE 10

Finally, the expression of each epoch as a linear combination of the chosen wavelet basis functions captures the frequency content of the epoch in a localized area of the signal which seem to highlight the differences between the two classes (see Fig. 11 and 12).

Finally, in order to examine the ability of the BayesNet classifier to discriminate each type of pathological events (GSW, PNES or VVS) from the others, we performed binary classification of all possible pairs of pathological events (GSW-PNES, GSW-VVS and PNES-VVS). The results in terms of classification accuracy for different number of N-best features (10, 20, ..50) are shown in Fig. 13.

FIGURE 13

As can be seen, the PNES-VVS classification problem is the most difficult case for the classifier. The best classification accuracy ( $76 \%$ ) for PNES-VVS pair is achieved when all features (1155) are used. On the other hand, GSW-PNES and GSW-VVS pairs are much easier cases for the classifier obtaining their maximum accuracy for the 10 best features. Specifically, GSW-PNES classification achieves $96 \%$ accuracy for $96 \%$ sensitivity and $100 \%$ specificity while GSW-VVS classification results in slightly lower percentages, i.e. $93 \%$ accuracy for $96 \%$ sensitivity and $87 \%$ specificity. Since generalized spike waves are very specific ictal neurophysiological patterns, they present much more consistent features (compared to the other types) which makes their detection an easier task. On the other hand, PNES has no specific EEG patterns but is frequently accompanied by muscular artifacts which present a variability across subjects. Similar variability appears even between consecutive epochs of VVS examples since there are several changes that happen successively in time during such an episode (beta / alpha $\rightarrow$ theta $\rightarrow$ delta $\rightarrow$ lower voltage rhythms $\rightarrow$ isoelectric suppression). It seems that the variability in the feature values of the PNES and VVS epochs is high (in respect to the available training data) impeding the learning of a discrimination model.

While 19 PNES appear to make a rather limited dataset, we believe that are sufficient given the lack of ictal EEG changes and the fact that their variability reflects only muscle and movement activities. The main problem is the really small sample of the 2 VVS-patients. However, VVS typically occur very rarely, in most patients annually, and only in very few patients more frequently, say monthly. It is therefore extremely unlikely to record them on standard EEG that is a 20 min to one hour "snapshot" of brain activity. Still, because of the rather predictable sequence of EEG changes (alphatheta delta etc) we believe that reasonable learning of a discrimination model is achievable / possible.

The proposed methodology takes into account features extracted from all the available channels by concatenating them in a single feature vector. The spatial localization of the features is encoded in their location within the feature vector presented to the classifier. Since the seizure onset patterns in focal seizures appear over a small subset of channels close to or at the epileptic focus, a strategy to

overcome the problem that different focal seizures appear on different channels is required. Such a strategy that successfully tackles the aforementioned problem has already been proposed in the literature [42]. In order to remove the information about the spatial location of the seizure from the training set, the authors in [42] proposed a sorting operation on the extracted features that reorders the features from the different channels in the feature vector before feeding it to the classifier.

However, since a seizure with focal onset (as manifested electroencephalographically) is always epileptic, here we have implemented a simplified version of a focal-vs-generalized seizure classification rule (as part of the ARMOR project) that automatically detects and labels the focal seizures. The focal-vs-generalized seizure classification rule is part of the online seizure detector [26][27] which performs a per channel analysis followed by the imposition of spatiotemporal constraints before taking the final decision (clear, focal, generalized) for each tested epoch. The classification rule is based on a mimetic approach requiring the seizure to be detected in at least $65 \%$ of the channels in order to be characterized as generalized; otherwise it is characterized as focal. Due to the different type of analysis (fusion of channel-based decisions versus fusion of features per channel to reach a decision), we are not presenting results of focal seizure classification in this paper, but rather focus on the classification of generalized events, which is the last component in our seizure analysis framework.

For a clinician the differentiation between focal and generalized events is important because it will play a crucial role in the medication/ treatment and general management choices. Such a rule (appearance in at least $65 \%$ of channels) is mainly useful when the events are focal, since focal EEG onset always indicates focal epileptic seizure activity. This rule has no clinical utility to the other event types, since the EEG expression of both psychogenic non-epileptic seizures and vasovagal syncope which leads to impairment of consciousness are "generalized". However, this step was introduced to facilitate the solution methodologically. Upon the characterization of focal events, the method presented here can be used to discriminate the remaining events into epileptic or non-epileptic.

On the clinical usefulness front, it is true that a competent seizure detection algorithm or set of algorithms should be able to detect both focal and generalized seizures, and either of these from nonepileptic events. The reason is that impairment of consciousness can be seen in temporal lobe seizures or seizures with secondary generalization. However, initial prodromal clinical symptoms and some typical EEG characteristics can be used for the differential diagnosis. Due to the big variability of

seizure presentation there needs to be a detailed analysis of adequate number of representative cases of different evolving patterns and this will be the part of our next work.

Until however we will be able to evaluate the method more extensively on a large dataset with an adequate number of representative cases for focal seizures we applied the proposed methodology on a dataset of 9 patients ( 2 subjects with focal seizures, 5 subjects with PNES and 2 subjects with VVS). We developed also a different algorithm to remove the spatial content from the features. The algorithm sorts the features for each channel according to feature type and then extracts the standard deviation of each feature type across channels, and the difference between maximum and minimum values of each feature (max-min). We introduced the standard deviation and the max-min values to the BayesNet classifier and achieved $74 \%$ accuracy, $70 \%$ sensitivity and $76 \%$ specificity when the 20 best features are used. The above results were obtained with a leave-one-patient-out strategy for validation. Since the dataset size is small we assessed the method also in a leave-one-epoch-out strategy, as performed in some other studies and achieved $90.2 \%$ accuracy, $86.7 \%$ sensitivity and $91.5 \%$ specificity. The achieved accuracy in this case is much higher, as expected. However, we do not emphasize the importance of these results since they might not generalize to other data.

Although direct comparison with other studies is not possible due to the different characteristics of each dataset (e.g. different seizure types, lack of PNES or VVS examples in most studies or use of single channel data), the achieved classification accuracy is higher than the one reported in the literature. In particular, the achieved accuracy in [22] is $86 \%$, lower than the accuracy of BayesNet in our methodology ( $95 \%$ ). Furthermore, in [21] the reported sensitivity ( $83 \%$ ) and specificity ( $98 \%$ ) are lower than the sensitivity of the majority of the classification methods evaluated in our work and the specificity achieved by our framework ( $98 \%$ ) when a subset of 10 discriminative features are used with respect to BayesNet classification.

Finally, although an initial work was held to reliably solve the problem of discrimination between different types of paroxysmal event and reveal the most discriminative features from a large set of time and frequency domain features given a dataset of 11 patients, there are some limitations that should be taken into account. The number of non-epileptic examples especially those of VVS) is limited and might not capture well the variability of the corresponding EEG events while the available generalized spike waves seem to be enough to describe such a consistent group of patterns. Under this scope we plan to start EEG recordings during tilt table test, which provokes VVS and therefore we

shall have a substantial number for further analysis. Furthermore, we aim to perform a more in depth analysis of focal seizures.

# 4. Conclusions 

In this paper, we investigated the problem of classification between epileptic and non-epileptic events from multi-channel EEG data using a large number of time-domain and frequency domain features. The proposed methodology was evaluated in EEG data from 11 subjects. Examination of several classification algorithms showed that the best accuracy is achieved by BayesNet. Feature ranking investigation and evaluation of the classification models using subsets of features were performed and revealed the most significant features for the classification task. The use of the most discriminative features $(N=10)$ increased significantly the performance of BayesNet classification at $95 \%$ accuracy ( $94 \%$ sensitivity for $98 \%$ specificity). The method has been evaluated using crossvalidation across subjects and showed that it can generalize satisfactorily providing the means for diagnosis support.

## 5. Acknowledgement

This study is partially funded by the EC under the FP7/2007-2013 with grant ARMOR, Agreement Number 287720. This research has been co-financed by the European Union (European Social Fund - ESF) and Greek national funds through the Operational Program "Education and Lifelong Learning" of the NSRF - Research Funding Program: Thales. Investing in knowledge society through the European Social Fund.
