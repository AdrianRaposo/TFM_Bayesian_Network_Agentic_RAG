# Classification of Epileptic and Non-Epileptic EEG Events 

Evangelia Pippa, Evangelia I. Zacharaki, Iosif Mporas, Vasileios Megalooikonomou<br>Dept. of Computer Engineering and Informatics University of Patras<br>Rion-Patras, Greece<br>pippa@ceid.upatras.gr, ezachar@upatras.gr, imporas@upatras.gr, vasilis@ceid.upatras.gr

Vasiliki Tsirka, Mark Richardson, Michael Koutroumanidis
Dept. of Clin. Neurophysiol. and Epilepsies, Guy's \& St. Thomas' \& Evelina Hospital for Children London, UK
vasiliki.tsirka@gstt.nhs.uk, mark.richardson@kcl.ac.uk, michael.koutroumanidis@gstt.nhs.uk


#### Abstract

In this paper, the classification of epileptic and nonepileptic events from multi-channel EEG data is investigated using a large number of time and frequency domain features. In contrast to most of the evaluations found in the literature, in this paper the non-epileptic class consists of two types of paroxysmal episodes of loss of consciousness namely the psychogenic non epileptic seizure (PNES) and the vasovagal syncope (VVS). For the classification, several classification algorithms were explored. The classification models were evaluated on EEG epochs from 11 subjects in an inter-subject cross-validation setting and the best among them achieved classification accuracies of $\mathbf{8 6 \%}$ (Bayesian Network), $\mathbf{8 3 \%}$ (Random Committee) and $\mathbf{7 4 \%}$ (Random Forest).


Keywords: epileptic seizures; PNES; vasovagal syncope; classification; machine learning

## I. INTRODUCTION

One of the most common and challenging medical cases in everyday clinical practice is that of patients reporting one or more episodes of paroxysmal loss of consciousness or altered awareness. The management of these medical cases may be proven to be demanding, time consuming and expensive and finally, in spite of the extensive and exhaustive investigation, the underlying diagnosis may remain elusive [12]. The differential diagnosis that a clinician usually faces is mainly that of an epileptic seizure, a possible psychogenic non epileptic seizure (PNES) and a probable vasovagal syncope (VVS).

Epileptic seizures are brief episodes of abnormal excessive or synchronous neuronal activity in the brain of patients suffering from epilepsy [17]. During an epileptic seizure there are several specific changes recorded in the electroencephalogram (EEG) which is a sensitive and important test used to evaluate patients with suspected epilepsy. There are certain characteristic ictal neurophysiological patterns that support the identification and detection of epileptic events and postictal and/or interictal abnormalities that can provide supplementary information. Pshychogenic non-epileptic seizures (PNES) are sudden paroxysmal changes in behavior or consciousness, that resemble epilepsy but are not accompanied by the
electrophysiological changes that characterize an epileptic seizure [24]. Although the clinical history can help differentiate these episodes, it is not unlikely to have inconclusive and insufficient event description by the patient and witnesses, not being able to confidently exclude and underlying epileptic disorder. In these cases the diagnosis of PNES can be supported by video-EEG monitoring, especially if a psychogenic event is captured, since in the case of PNES there are no specific EEG changes. Vasovagal or vasodepressor syncope is a common type of syncope and various mechanisms have been postulated for explaining the characteristic association of hypotension and bradycardia. The term "vasovagal" was introduced by Lewis [11] to indicate that both blood vessels and heart were implicated and since atropine reversed the bradycardia but not the hypotension he considered vasodilatation as the primary responsible factor. During a vasovagal syncopal attack there may be some characteristic EEG changes starting with progressive generalized theta slowing of background rhythms, followed by sometimes hypersynchronous delta activity of high voltage (beta / alpha $\rightarrow$ theta $\rightarrow$ delta) and appearance of progressively lower voltage rhythms until isoelectric suppression [2, 13]. This pattern is progressively reversed after the patient's fall, during his/her recovery. These changes do not include any ictal activity.

Several methods have been proposed for the classification of EEG captured events into epileptic or normal [8, 14, 22, 23, 25]. However, only a few studies deal with the differentiation between epileptic and other paroxysmal episodes of loss of consciousness such as PNES and vasovagal syncope. It is worth to note that the discrimination between different types of non-epileptic events is considerably more useful in diagnostic procedure given the semiological resemblance between the aforementioned paroxysmal attacks. Furthermore, according to [24] the one third of PNES patients may have clinical convincing GrandMal like seizures. This makes discrimination between PNES and epileptic seizures a challenging task, especially in an online monitoring system for automatic detection of epileptic events, such as [3], where false alarms caused by events similar to epilepsy are undesired.

![img-0.jpeg](img-0.jpeg)

Figure 1. Architecture for classification of epileptic and non-epileptic events from EEG
To the best of our knowledge, only a few studies have been proposed in the literature for automated classification between epileptic and non-epileptic pathological events from EEG. Poulos et al. [21] proposed an algorithm which estimates a number of auto-correlated coefficients extracted from an appropriately selected epileptic EEG segment and examines whether these coefficients are correlated with the coefficients of the unknown EEG segments in order to classify the latest into epileptic or non-epileptic. Their algorithm obtained a sensitivity of $83 \%$ for $90 \%$ specificity. Papavlasopoulos et al. [19] trained a LVQ1 neural network on an appropriately extracted set of auto-correlation coefficients (codebook) and used the resulting model to classify the corresponding feature vectors of the unknown EEG segments. The LVQ1 network achieved $86 \%$ accuracy. The feature extraction methods of the aforementioned classification frameworks, as well as the achieved results, can be found in [18]. Statistical analysis of the results based on chi-square test showed that the LVQ neural network method is superior than the cross-correlation one [18].

In this paper, we evaluate a large set of time and frequency domain features which have been widely used for the analysis of EEG signals in the literature. In addition to the reported evaluations found in the literature, we extend the non-epileptic class to both PNES and VVS events. The diagnosis of epilepsy is more challenging compared to the detection of seizure onset due to the semiological resemblance between epileptic and non-epileptic events, especially when video-EEG monitoring is not incorporated [4]. Also the classification of abnormal episodes into different types requires a broad knowledge of EEG patterns across patients, while seizure detection can rely on patient-specific models which are easier to learn, especially for generalized seizures [16].

The rest of this paper is organized as follows. In Section II the classification methodology is presented. Section III provides details about the evaluation data and the experimental protocol followed and Section IV presents the achieved results. Finally in Section V we conclude this work.

## II. METHODOLOGY FOR CLASSIFICATION OF EPILEPTIC AND NON-EPILEPTIC EVENTS

The presented architecture for classification between epileptic and non-epileptic EEG events is part of an end-to-end system for monitoring and analysis of brain disorders, which is part of the EC FP7 research and development ARMOR project [3]. Within the ARMOR framework patients suffering from seizures are monitored through sensors and the multiparametric data are processed automatically (real-time by
software tools) or semi-manually (offline with the support of software tools and visualizations) by neurology experts [15, 16].

The block diagram of the classification methodology is illustrated in Figure 1. Short time analysis is performed in the multidimensional EEG data (one dimension per electrode) and models for binary classification between epileptic or nonepileptic (PNES or VVS) events are built.

During the training phase a bootstrap set of training data including EEG recordings with manual time annotations for the onsets and offsets of the events of interest, i.e. the epileptic and the non-epileptic intervals, are used to build the binary classification models. Specifically, the multidimensional EEG data are initially preprocessed and subsequently parameterized as shown in Figure 1. Preprocessing consists of notch filtering, baseline correction, re-sampling (in order to obtain a common resolution level for all data) and frame blocking of the incoming EEG streams to epochs of constant length $w$ with constant time-shift and without time-overlap between successive epochs. The epoch length was selected equal to 1 second to match other relevant studies [14, 15, 16]. Thus each data sample is represented by a $N \times w$ matrix, where $N$ is the number of selected EEG electrodes. After preprocessing, time and frequency domain features are extracted from each epoch for each one of the $N$ electrodes. The extracted time domain and frequency domain features are afterwards concatenated to a single feature vector as a representative signature for each epoch. More details on the extracted features are provided in section III. The feature vectors of the training data (with assigned class labels known from the manual annotations) are used to train binary models for epileptic and non-epileptic events (the epileptic class includes generalized spike wave discharges whereas the non-epileptic class includes PNES or VVS).

During the test phase the unknown multidimensional EEG signal is preprocessed and parameterized with the same setup as in the training phase. Each produced feature vector is compared against the epileptic and non-epileptic models, as shown in Figure 1, and a class label is assigned to each feature vector, i.e. each corresponding epoch. Further post-processing of per epoch decisions can be applied by using rules for minimum duration of the events.

## III. EXPERIMENTAL SETUP

The previously described classification methodology was evaluated on multi-parametric recordings performed within the

ARMOR project, aiming to differentiate between epileptic and non epileptic events. Specifically, the recordings were performed in the Department of Clinical Neurophysiology and Epilepsies in St Thomas' Hospital in London and data from 11 patients in total were investigated. All participants had at least one of their typical epileptic or non epileptic events captured during the recording procedure. The epileptic group, consisted of patients with known diagnosis of Idiopathic Generalized Epilepsy (IGE), manifested clinically with absence seizures and they had at least one clinical episode captured during the recording, associated with Generalized Spike Wave Discharges (GSWD) on the EEG. The non epileptic group included patients that had sustained a vasovagal syncope (2 participants) or a psychogenic non epileptic attack (PNES) (5 participants) during their monitoring. The selected EEG channels were Fp2, F8, F4, T4, C4, A2, P4, T6, O2, Fp1, F7, F3, A1, C3, T3, P3, T5, O1, Fz, Cz, Pz. The recordings were manually annotated by neurological experts of the King College London (the coauthors V.T and M.K). Only epochs during the seizure duration were considered for training and for testing. All data were stored in EDF formatted files.

Each of the EEG channels was parameterized using the following features: (i) time-domain features: minimum value, maximum value, mean, variance, standard deviation, percentiles ( $25 \%, 50 \%$-median and $75 \%$ ), interquartile range, mean absolute deviation, range, skewness, kyrtosis, energy, Shannon's entropy, logarithmic energy entropy, number of positive and negative peaks, zero-crossing rate, and (ii) frequency-domain features: 6-th order autoregressive-filter (AR) coefficients, power spectral density, frequency with maximum and minimum amplitude, spectral entropy, delta-theta-alpha-beta-gamma band energy, discrete wavelet transform coefficients with mother wavelet function Daubechies 16 and decomposition level equal to 8 , thus resulting to a feature vector of dimensionality equal to 55 for each of the $N=21$ EEG channels, i.e. 1155 in total.

The computed feature vectors, V, were used to train binary classification models. In order to evaluate the ability of the above features to discriminate between epileptic and nonepileptic epochs we examined several classification algorithms implemented by WEKA machine learning toolkit software [8], including BayesNet [6,7], RandomCommittee, RandomForest [5], IBk [1] and SMO [10,20] with RBF kernel.

During the test phase, the EEG recordings are preprocessed and parameterized as in training. Each classification model is used to label each of the incoming EEG epochs as epileptic or non-epileptic (either PNES or vasovagal syncope). In the present evaluation no post-processing algorithm was applied on the estimated epoch-based results.

Evaluation was performed in a leave-one-out crossvalidation setting. Specifically, each time one subject was leftout for testing, while the rest of the subjects were used for training. For the left-out subject, all epochs between seizure onset and offset were used as testing samples. Table I shows the number of epochs $(M)$ that were extracted for each subject during the seizure.

TABLE I. NUMBER OF EPOCHS PER SUBJECT


TABLE II. CLASSIFICATION PERFORMANCE


## IV. RESULTS

The classification method presented in Section II was evaluated following the experimental setup described in Section III. Table II shows the classification performance in terms of accuracy, sensitivity and specificity, defined as:

$$
\begin{gathered}
\text { Accuracy }=(\mathrm{TP}+\mathrm{TN}) /(\mathrm{TP}+\mathrm{FP}+\mathrm{TN}+\mathrm{FN}) \\
\text { Sensitivity }=\mathrm{TP} /(\mathrm{TP}+\mathrm{FN}) \\
\text { Specificity }=\mathrm{TN} /(\mathrm{FP}+\mathrm{TN})
\end{gathered}
$$

where true positives are denoted as TP, true negatives as TN, false positives as FP and false negatives as FN. Here we consider the epileptic class as the positive and the non-epileptic class (PNES or VVS) as the negative.

As can be seen in Table II, the overall highest accuracy of the proposed methodology for classification between epileptic and non-epileptic EEG events is $86 \%$ for BayesNet classification model. RandomCommittee and Random Forest classification models follow with $83 \%$ and $74 \%$ accuracy, respectively. For the classifier with the highest accuracy (BayesNet), the sensitivity (or recall), i.e. the fraction of actual epileptic events which are correctly identified as such, is $92 \%$ and the specificity, i.e. the proportion of non-epileptic events (either PNES or VVS) which are correctly classified as such, is $78 \%$. Although direct comparison with other studies is not possible due to the different characteristics of each dataset (e.g. different seizure types, lack of PNES or VVS examples or single channel data), the achieved epileptic recognition accuracy is

comparable to the performance reported in the literature. In particular, the achieved accuracy in [19] is $86 \%$, equal to the accuracy of BayesNet in our methodology. Furthermore, in [21] the reported sensitivity ( $83 \%$ ) is lower than the sensitivity of the majority of the classification methods evaluated in our work, while the specificity is $90 \%$, higher than the specificity achieved by our framework.

## V. CONCLUSION

In this paper, we investigated the problem of classification between epileptic and non-epileptic events from multi-channel EEG data using a large scale feature vector of time-domain and frequency domain features. Examination of several classification algorithms showed that the best classification accuracy was achieved by BayesNet. The proposed methodology was evaluated in EEG data from 11 subjects and the achieved accuracy was up to $86 \%$, comparable to the results reported in the literature. The method has been tested across subjects and showed that it can generalize satisfactorily providing the means for diagnosis support. Preliminary analysis showed that feature selection before classification further improves the overall performance of our methodology. Under this scope we aim to highlight in the future the most important features or electrodes for seizure classification and evaluate our framework on different datasets.

## ACKNOWLEDGMENT

This study is partially funded by the EC under the FP7/2007-2013 with grant ARMOR, Agreement Number 287720. This research has been co-financed by the European Union (European Social Fund - ESF) and Greek national funds through the Operational Program "Education and Lifelong Learning" of the NSRF - Research Funding Program: Thales. Investing in knowledge society through the European Social Fund.
