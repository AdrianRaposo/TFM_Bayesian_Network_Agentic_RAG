# HHS Public Access 

Author manuscript
Physiol Meas. Author manuscript; available in PMC 2021 November 06.
Published in final edited form as:
Physiol Meas. ; 41(10): 104003. doi:10.1088/1361-6579/abbcbb.

## Patient-Adaptable Intracranial Pressure Morphology Analysis Using a Probabilistic Model-Based Approach

Paria Rashidinejad*, Xiao $\mathrm{Hu}^{\dagger}$, Stuart Russell ${ }^{\ddagger}$<br>*Department of Electrical Engineering and Computer Sciences, University of California, Berkeley<br>${ }^{\dagger}$ Physiological Nursing, School of Nursing, University of California, San Francisco; Health Systems and Analytics, School of Nursing, Duke University; Department of Electrical and Computer Engineering, Pratt School of Engineering, Duke University; Departments of Neurology, School of Medicine, Duke University; Departments of Biostatistics and Bioinformatics, School of Medicine, Duke University<br>${ }^{\ddagger}$ Electrical Engineering and Computer Science Department, University of California, Berkeley


#### Abstract

Objective.—We present a framework for analyzing the intracranial pressure (ICP) morphology. Analyzing ICP signals is challenging due to the non-linear and non-Gaussian characteristics of the signal dynamics, inevitable corruption with noise and artifacts, and variations in the ICP pulse morphology among individuals with different neurological conditions. Existing frameworks make unrealistic assumptions regarding ICP dynamics and are not tuned for individual patients.


Approach.—We propose a dynamic Bayesian network (DBN) for automated detection of three major ICP pulsatile components. The proposed model captures the non-linear and non-Gaussian dynamics of the ICP morphology and further adapts to a patient as the individual's ICP measurements are received. To make the approach more robust, we leverage evidence reversal and present an inference algorithm to obtain the posterior distribution over the locations of pulsatile components.

Results.-We evaluate our approach on a dataset with over 700 hours of recordings from 66 neurological patients, where the pulsatile components have been annotated in prior studies. The algorithm obtains an accuracy of $96.56 \%, 92.39 \%$, and $94.04 \%$ for detecting each pulsatile component on the test set, showing significant improvements over existing approaches.

Significance.—Continuous ICP monitoring is essential in guiding the treatment of neurological conditions such as traumatic brain injuries. An automated approach for ICP morphology analysis takes a step toward enhancing patient care with minimal supervision. Compared to previous methods, our framework offers several advantages. It learns the parameters that model each patient's ICP in an unsupervised manner, resulting in an accurate morphology analysis. The Bayesian model-based framework provides uncertainty estimates and reveals interesting facts about ICP dynamics. The framework can be readily applied to replace existing morphological analysis methods and support the application of ICP pulse morphological features to aid the

monitoring of pathophysiological changes of relevance to the care of patients with acute brain injuries.

## Keywords

Artificial Intelligence in Healthcare, ICP, Dynamic Bayesian Network, Particle Filter, Model-Based Probabilistic Inference, Patient Monitoring

## 1. Introduction

Intracranial pressure (ICP) is one of the most important physiological variables for guiding therapeutic decisions in the care of patients with acute brain injuries. Continuous ICP monitoring is warranted when treating patients with severe brain injuries in acute care settings and it can last several days when a patient's status is the most fragile and dynamic. ICP signal contains rich information related to a patient's pathophysiological status. The most straightforward use of such information is to detect and treat extremely high brain pressure to prevent life-threatening conditions such as brain herniation. In fact, this use of ICP monitoring is a prevailing one and well-established. However, considering that the clinically accepted practice of ICP monitoring is still highly invasive requiring surgically drilling the skull to place sensors, ideally more useful information for managing patients should be derived from ICP signals.

Physiologically speaking, ICP results from interactions among multiple physiological systems: cardiovascular, respiratory, cerebral vascular, cerebrospinal fluid, and brain tissues. ICP signal thus has a complex form and contains multiple distinct and interacting components (or sub-peaks). Due to its cardiovascular origin, ICP signal is pulsatile and in sync with heart beats. In addition, an ICP signal contains an oscillatory component that reflects influence from respiratory activities. At an even lower frequency spectrum, an ICP signal can show slow waves that exist in many other neurophysiological signals. Therefore, there is a need for biomedical engineers and data scientists to develop more advanced algorithms to extract additional information to support clinicians make the best use of ICP monitoring in their clinical decisions.

There are many potential routes to analyze an ICP signal as evidenced in published studies (Hornero et al. 2005, 2007; Hu et al. 2007; Holm and Eide, 2008; Hu et al. 2008a; Eide et al. 2012; Santamarta et al. 2012; Calisto et al. 2012; García et al. 2013; Xu et al. 2013; Lee et al. 2015; García et al. 2018; Megjhani et al. 2019; Park et al. 2019; Hüser et al. 2020). Among these approaches, one particular area worth further investigation is characterization of ICP pulse waveform. Our previous works have shown that quantification of ICP pulse waveform morphology can predict ICP elevation (Hu et al. 2010b), detect distal cerebral arterial changes (Hu et al. 2009, 2010a; Asgari et al. 2011a,b,c, 2012, 2013; Connolly et al. 2015; Liu et al. 2019, 2020), recognize false ICP alarms (Scalzo and Hu, 2013; Scalzo et al. 2012c), and determine the external ventricular drain (EVD) weaning outcome (Hu et al. 2012a; Arroyo-Palacios et al. 2016). In these studies, we developed and used an ICP pulse morphological analysis algorithm -- called morphological clustering and

analysis of intracranial pressure (MOCAIP) (Hu et al. 2008c; Scalzo et al. 2009, 2010, 2012a).

MOCAIP proceeds by first detecting individual ICP pulses, clustering them to find a representative pulse from the largest cluster, detecting a combination of landmarks of this representative ICP pulse (local optima and inflection points), and then designating the locations of up to three sub-peaks. Through this process, metrics that quantify the morphology of the pulse can be systematically computed. However, our experience has revealed weaknesses of the algorithm that result in sometime excessive needs of manually correcting the positions as returned by MOCAIP. To further translate the past discoveries enabled by MOCAIP through a more automated process to enable its practice in a real-world setting, it is imperative to address weaknesses of MOCAIP and this is the objective of this study.

In this work, we propose a framework based on dynamic Bayesian networks (DBNs) for ICP morphology analysis. Our framework adopts the first stages of MOCAIP as the data preprocessing step and offers several improvements: (1) it uses a principled way for modeling the distribution of ICP components based on data instead of simply making a Gaussian assumption, (2) it models the dynamics and temporal changes of ICP which were not considered in the MOCAIP framework, (3) it allows the ICP components not to necessarily be in the major ICP pulse landmarks, improving over possible missed detections, (4) it deploys a statistically principled optimization objective for finding the maximum a posteriori locations of ICP components, and (5) it allows the framework parameters to adapt for individual patients.

The paper is organized as follows. We begin by reviewing some preliminary concepts and notation in Section 2 on dynamic Bayesian networks and inference of state variables in DBNs using particle filtering and motivate the use of evidence reversal for the problem considered in this work. In Section 2, the modules of the proposed framework including data pre-processing steps and development of the temporal model are described. The framework is then tested on more than 700 hours of data and the performance is compared with MOCAIP as well as a clustering approach inspired by the work of (Lee et al. 2015). The experimental results are presented in Section 4, followed by careful evaluation of the advantages and shortcomings of the proposed approach. We conclude the paper by summarizing the framework and discussing several directions for future work.

## 2 Preliminaries

### 2.1 Dynamic Bayesian networks

A dynamic Bayesian network, or DBN, is a temporal probabilistic model that is used to represent a complex model of sequential data. DBNs are used in a wide range of applications such as finance (Giudici and Spelta, 2016), seismic monitoring (Riggelsen et al. 2007; Moore and Russell, 2017), and physiological monitoring (Yang et al. 2010). To construct a DBN, one must specify a set of variables, the conditional dependencies between them, and their evolution over time. In particular, a DBN models a partially observed Markov process

with hidden variables $\left\{X_{n}\right\}_{n \geq 1}$, observed variables $\left\{Y_{n}\right\}_{n \geq 1}$, and parameters $\theta$ across steps $n$ using a probabilistic model defined as follows

$$
\begin{gathered}
X_{1}-p\left(X_{1} ; \theta\right) \\
X_{n} \mid X_{n-1}-p\left(X_{n} \mid X_{n-1} ; \theta\right) \\
Y_{n} \mid X_{n}-p\left(Y_{n} \mid X_{n} ; \theta\right)
\end{gathered}
$$

where $p\left(X_{1} ; \theta\right)$ is the prior distribution over the hidden (state) variables, $p\left(X_{n} \mid X_{n-1} ; \theta\right)$ is the transition (propagation) model, and $p\left(Y_{n} \mid X_{n} ; \theta\right)$ is the sensor (observation) model. ${ }^{1}$ The transition model represents the temporal evolution of hidden variables by specifying the conditional dependencies between hidden variables across time steps. The sensor model defines the conditional probability of receiving a particular observation given a certain hidden variable.

The success of probabilistic model-based approaches has been established in several areas of healthcare (Williams et al., 2006; Heldt et al., 2006). Model-based methods have shown to be more robust in the presence of noise and artifacts, which are common in physiological applications, compared to model-free methods (Aleks et al., 2009; Chen et al., 2016). Furthermore, model-based methods are generally more data-efficient making them wellsuited for physiological applications where data are often scarce.

In this work, we use a DBN to specify a dynamical model of the ICP pulsatile components that captures the uncertainty due to temporal evolution and observation noise and adapts the model for individuals through learning the static variables in an unsupervised manner. We choose a DBN since it can represent non-linear and non-Gaussian dynamics compared to alternative dynamical models such as linear dynamical systems with Gaussian noise. After specifying the model, the three major pulsatile components are identified by solving a statistical inference problem described in the following section. The experimental results presented in Section 4 demonstrate improved performance compared to previous model-free methods.

# 2.2 Latent variable inference via particle filtering 

We are interested in computing the filtering distribution $p\left(X_{n} \mid Y_{1: n}\right)$, i.e. the posterior distribution of the current hidden variables given all the information provided by the observed variables up to the present. Exact filtering in complex systems with non-linear and non-Gaussian dynamics is generally intractable. Particle filtering methods, introduced by Gordon et al. 1993, are a popular class of algorithms used to obtain a numerical approximation of the posterior distribution using weighted samples, or particles. More

[^0]
[^0]:    ${ }^{1}$ Throughout the paper, we use capital letters to denote random variables and small letters to denote the realizations of random variables.

specifically, particle filter first samples $K$ particles $\left\{x_{1}^{k}\right\}_{k=1}^{K}$ from the prior distribution and initiates particle weights to be identical. Then the following update cycle is repeated for each time step:

1. Particle propagation: Each particle $k$ is propagated to the following time step by sampling the next particle $x_{n+1}^{k}$ conditioned on the current particle $x_{n}^{k}$ using the transition model, i.e. $x_{n+1}^{k} \sim p\left(.|x_{n}^{k} ; \theta\right) .^{2}$
2. Weight assignment: Each particle $k$ is weighted by the likelihood it assigns to the new evidence $p\left(y_{n} \mid x_{n}^{k} ; \theta\right)$.
3. Resampling: Particles are resampled proportional to their weights and new particles with identical weights are generated.

Without the resampling step, particle filter will generate a set of particles where only a few retain significant weights. As a result, the effective sample size (ESS) for representing the posterior distribution dramatically drops. Conventionally, particles are resampled proportional to their weights only at time steps where ESS falls below a certain threshold. Subsequently, samples with negligible weights are likely to be discarded and particles with large weights are likely to be duplicated, resulting in more samples in high probability regions. More advanced resampling techniques have been extensively researched, see (Li et al., 2015) for an overview.

# 2.3 Evidence reversal 

Although sequential Monte Carlo algorithms such as particle filtering often provide accurate approximations to the posterior distribution, if the DBN has certain characteristics the samples may diverge from the reality as more observations are received. For example, consider the case where the observation model $p\left(Y_{n} \mid X_{n}\right)$ is fairly accurate, i.e. any realized observation $Y_{n}=y_{n}$ has high probabilities for some values of $X_{n}$ and very low probabilities for the others. If the transition model is fairly inaccurate, the weighting process assigns extremely low weights to most particles which are incompatible with the observations. In this scenario, only a few samples approximate the posterior distribution approximation resulting in large approximation error. This happens despite the fact the sensor is accurately providing observations (Figure 1(a)).

Evidence reversal (ER), proposed by Kanazawa et al. 1995, addresses this problem by reconstructing the DBN so that the observation $Y_{n}$ becomes the ancestor of $X_{n}$. ER ensures samples to be compatible with the observations in every time step. Figure 2 illustrates an schematic diagram of the ER transformation on a DBN. We can easily see that the two networks are equivalent by writing the joint distribution of $X_{n}$ and $Y_{n}$ conditioned on $X_{n-1}$ in both networks:

$$
p\left(X_{n}, Y_{n} \mid X_{n-1}\right)=p\left(X_{n} \mid X_{n-1}\right) p\left(Y_{n} \mid X_{n}\right)=p\left(Y_{n} \mid X_{n-1}\right) p\left(X_{n} \mid X_{n-1}, Y_{n}\right)
$$

[^0]
[^0]:    ${ }^{2}$ In general, particles may be sampled from a simpler proposal distribution when direct sampling from the transition distribution is difficult.

Under ER, the particle filtering assigns weights according to p(Y_{n} | X_{n}_{-1}) and propagates samples by sampling from p(X_{n} | X_{n}_{-1}, Y_{n}). Figure 1(b) illustrates an example where evidence reversal overcomes sample impoverishment.

## 3 Intracranial pressure morphology analysis framework

Figure 3 illustrates the block diagram of the ICP monitoring framework. This framework includes three major components: (1) a pre-processing block that cleans the ICP signals and extracts a set of candidate locations for pulsatile components, (2) a training block that computes the model parameters, and (3) a dynamic Bayesian network that returns the three major pulsatile components.

### 3.1 Dataset

The dataset includes ICP and ECG signals acquired from 66 patients who were admitted to the UCLA Adult Hydrocephalus Center for assessment of normal pressure hydrocephalus (NPH) using the overnight ICP monitoring technique. ICP of these patients was continuously monitored for up to 24 hours using Codman intraparenchymal microsensors (Codman and Schurtleff, Raynaud, MA) placed in the right frontal lobe. Simultaneously, ECGs of the patients were continuously measured using GE bedside monitors. The signals were recorded either using a data acquisition system placed on a wheel (PowerLab TM SP-16) or using an enterprise-wide data acquisition software solution (BedMasterTM) at a sampling frequency of 400Hz and 240Hz, respectively. The use of this dataset to develop a set of rules to predict the outcome of cerebrospinal fluid shunt procedures for these NPH patients was reported in a prior work (Hu et al. 2012b). These rules were based on MOCAIP metrics that were obtained by first applying the MOCAIP algorithm to analyze 30-second of ICP and then by manual review and correction of any incorrectly designated ICP sub-peaks. For the purpose of the present study, the manually corrected detections of ICP sub-peaks are then used as ground truth to assess the accuracy of the proposed algorithm.

### 3.2 Data pre-processing

We adopt similar data pre-processing steps as the MOCAIP framework, which is briefly described here. We refer the reader to the original MOCAIP paper for a more detailed explanation (Hu et al. 2008c). The data pre-processing block admits a raw ICP signal, obtains a sequence of dominant pulses, and extracts a set of candidate points for each dominant ICP pulse according to the following steps.

1. ICP pulse detection: The ICP signals are first segmented into a sequence of pulses using the ICP pulse detection method presented in our previous work (Hu et al. 2008b). This algorithm leverages a robust ECG beat detection as well as interval constrains to aid ICP pulse segmentation.
2. ICP pulse clustering: ICP signals can be contaminated by various types of noise and artifacts including high-frequency noise from the measurement devices, movement artifacts, and sensor detachments. To obtain clean pulses, a hierarchical clustering algorithm is used to cluster sub-sequences of raw ICP

pulses and the average pulse of the largest cluster is taken as the representative (dominant) pulse of each sub-sequence.
3. Non-artifactual pulse recognition: Occasionally when large signal segments are corrupted with noise, dominant pulses obtained from pulse clustering become artifactual. The non-artifactual pulses are identified using a reference library of validated pulses created during training.
4. Candidate detection: Candidate locations for major pulsatile components are identified by obtaining certain landmarks on each ICP pulse. These landmarks are identified by merging the intersections of concave and convex regions and maximum curvature points.

# 3.3 Detection of major pulsatile components 

Our framework relies on constructing a DBN that corresponds to a simplified model of the ICP evolution over time. The latent and observed variables of this model are listed below.

1. Latent variables $X_{n}=\left\{X_{n}(1), X_{n}(2), X_{n}(3)\right\}$ denote the arrival time of three major components of pulse $n$ with respect to the arrival time of the most recent heartbeat. $X_{n}^{i}$ takes values in $\mathbb{R}^{+} \cup\{m\}$, with $X_{n}^{i}=m$ when component $i$ is not recognizable (missing). A sub-peak can be missing because of poor signal quality or pathological reasons. Based on our experience, the likelihood of missing a sub-peak is less than $10 \%$. The fact that any of the three target subpeaks can be missing in a given ICP pulse makes the process of sub-peak designation more challenging.
2. Observed variables $Y_{n}=\left\{Y_{n}(1), \ldots, Y_{n}\left(C_{n}\right)\right\}$ are candidate locations for major components of pulse $n$ that are extracted during the pre-processing stage. $C_{n}$ is a random variable denoting the number of candidates the algorithm has detected for pulse $n$.

Transition model.—First, we specify the transition model for the instances where all three components are present. We model the evolution of ICP pulsatile components as a Markov process according to the following:

$$
\begin{aligned}
& p\left(X_{n} \mid X_{1: n-1}=p\left(X_{n} \mid X_{n-1}\right)=p\left(X_{n}(1), X_{n}(2), X_{n}(3) \mid X_{n-1}(1), X_{n-1}(2), X_{n-1}(3)\right)\right. \\
& =p\left(X_{n}(1) \mid X_{n-1}(1)\right) p\left(X_{n}(2) \mid X_{n-1}(2), X_{n}(2)>X_{n}(1)\right) \\
& \left.\times p\left(X_{n}(3) \mid X_{n-1}(3), X_{n}(3)>X_{n}(2)\right)\right)
\end{aligned}
$$

Motivated by the histograms of the locations of major pulsatile components in the training data, we adopt the following model for evolution of $X_{n}(i)$

$$
X_{n}(i)=X_{n-1}(i)+\eta_{n}(i) \quad \text { for } i=\{1,2,3\}
$$

where $\eta_{n}(i) \sim \operatorname{Laplace}(0, b(i))$, where $b(i)$ is the Laplace distribution scale parameter. Figure 4 presents the histogram of $\eta_{n}(i)$ for three patients demonstrating that the concentration of $\eta_{n}(i)$ around zero is not well-described by a Gaussian distribution. Due the symmetry and high concentration of histograms around zero, we choose to model $\eta_{n}(i)$ according to a

Laplace distribution. Furthermore, the histograms suggest that the scale parameters b(i) vary across patients. Thus, We take b(i) to be a static hidden variable, i.e. *b*_{*i**t*}(*i*) = *b*_{*i**t* - 1}(*i*) = *b*(*i*), and infer it as the ICP observations are received for each patient. Taking b(i) as a latent variable as opposed to a constant parameter allows the model to adapt for an individual patient's physiology and neurological condition.

We allow *X*_{*i**t*}(*i*) to be missing with a constant probability *p*_{*i**t**t*}(*i*) that is learned during training. For the cases where *X*_{*i**t* - 1}(*i*) is missing, we take the temporal evolution of *X*_{*i**t*}(*i*) to be

$$X_{n}(i) = X_{n - k}(i) + \overbrace{i = n - k + 1}^{n} \eta j(i),$$

where *n* - *k* is the last pulse whose component *i* was present. Note that Equation (2) is equivalent to Equation (1) when *k* = 1.

### Prior distribution

We specify prior distributions for the latent variables b(i) and *X*_{*i**t*}(*i*). Since b(i) is a scale parameter, we use a wide uniform distribution and we take *X*_{*i**t*}(*i*) ∼ Laplace(*μ*(*i*), *b*(*i*)), where *μ*(*i*) is computed using a maximum likelihood estimate on training set.

### Observation model

In our setup, since the three major pulsatile components are often visually distinguishable landmarks, they tend to be included in or very close to the candidate points with high probability even though candidate points often include several spurious points as well. Given a set of candidate points *Y*_{*i**t*} = *y*_{*i**t*}(1), ..., *y*_{*i**t*}(*c*_{*i**t*}) the observation model *p*(*Y*_{*i**t*};*X*_{*i**t*}) assigns high weights to some values of *X*_{*i**t*} and extremely low weights to most values of *X*_{*i**t*}. Thus, the proposed DBN is an example where the standard particle filtering works poorly due to sample impoverishment as explained in Section 2.3. We address this problem by using evidence reversal.

### Model under evidence reversal

Recall from Section 2.3 that for an ER transformation, the transition distribution *p*(*X*_{*i**t*};*X*_{*i**t* - 1}, *Y*_{*i**t*}) and the likelihood distribution *p*(*Y*_{*i**t*};*X*_{*i**t* - 1}) should be specified. We design *p*(*X*_{*i**t*};*X*_{*i**t* - 1}, *Y*_{*i**t*};*b*) to be a hybrid —mixture of discrete and continuous— distribution where *X*_{*i**t*} takes values in *Y*_{*i**t*} with high probability. Denote by *p*_{*c*}(*i*) the probability that *X*_{*i**t*}(*i*) is equal to one of the candidates. Let *α*_{*j*}(*i*) be the value of the Laplace probability density function at *Y*_{*i**t*}(*j*) = *y*_{*i**t*}(*j*) with mean *x*_{*i**t* - 1}(*i*) and scale parameter *b*(*i*), i.e.

α j (k) = Laplace (y i t (j) ; x i t - 1 (i) , b (i))

Let *L*(*i*) = 0 for *i* = 1 and *L*(*i*) = *X*_{*i**t*}(*i* - 1) for *i* = 2, 3, be the minimum value that *X*_{*i**t*}(*i*) can take. The transition distribution is defined as

The above distribution states that *X_{n}(i)* is equal to candidate *Y_{n}(j)* with probability *p_{c}(i)*∑_{j∀j(i)}^{∀j(i)} if *Y_{n}(j)* > *L(i)*. The total probability that *X_{n}(i)* is one of the candidates is *p_{c}(i)* and the probability that *X_{n}(i)* is missing is *p_{m}(i)*. Finally, with probability 1 − *p_{c}(i)* − *p_{m}(i)*, *X_{n}(i)* is present but is not equal to any of the candidate points. In this case, *X_{n}(i)* has a (truncated) Laplace distribution satisfying *X_{n}(i)* > *L(i)*. Using lower bounds *L(i)* ensure that 0 < *X_{n}(1)* < *X_{n}(2)* < *X_{n}(3)*. In Figure 5, the left plot illustrates an example on the probabilities assigned to each candidate points. The right plot presents the hybrid transition distribution.

The likelihood distribution *p(Y_{n}|X_{n-1})* is computed by considering all *valid assignments* of candidates to ICP components. In particular, candidates *Y_{n}* can be assigned to either of the three components or none of them. An assignment is considered valid if it satisfies *X_{n}(1)* < *X_{n}(2)* < *X_{n}(3)*. For example, for candidates *Y_{n}* {150, 200, 230, 320, 500}, assignments {1, none, 2, 3, none} and {none, 1, none, 3, none} are valid which are equivalent to {*X_{n}(1)* = 150, *X_{n}(2)* = 230, *X_{n}(3)* = 320} and {*X_{n}(1)* = 200, *X_{n}(2)* = *m*, *X_{n}(3)* = 320}, respectively. Let *a* be the set of all valid assignments. The likelihood distribution can be written as

$$p(Y_n \mid X_{n-1}) = \sum_{a \in a} p(a) p(Y_n \mid X_{n-1}, a).$$

Probability of each assignment *p(a)* is computed using *p_{c}(i)*. For instance, if the assignment only selects components two and three from the candidates, *p(a)* = (1 − *p_{c}(1)*)*p_{c}(2)*p_{c}(3)*, which is the probability that component one is not in the candidates but components two and three are. Conditioned on an assignment, the likelihood *p(Y_{n}|X_{n-1}, a)* using the Laplace pdfs with expected values *X_{n-1}(1)*, *X_{n-1}(2)*, *X_{n-1}(3)* assuming that spurious observations can appear anywhere in the ICP pulse uniformly at random. For example, for the assignment *a* = {1, none, 2, 3, none}, we have the following likelihood

$$p(Y_n \mid X_{n-1}, a) = \text{Laplace}(Y_n(1) \mid X_{n-1}(1))\text{Uniform}(Y_n(2))\text{Laplace}(Y_n(3) \mid X_{n-1}(2)) \times \text{Laplace}(Y_n(4) \mid X_{n-1}(3))\text{Uniform}(Y_n(5)).$$

Computing this likelihood is essential for tuning parameters *b(i)*.

## 4 Results

We implement the ER transformation of the proposed DBN and use particle filtering with 1000 samples as the inference algorithm. We run the framework on more than 700 hours of data collected from 66 patients and measure the performance of the algorithm for detecting

sub-peaks against expert reviewed and corrected sub-peak annotations. A sub-peak detected by the algorithm is accepted as correct if it is within 50 ms of the annotations.

We compare the performance of our framework to the MOCAIP framework. The MOCAIP framework has a similar pre-processing method as explained earlier but uses a different method for designating the three major components given the candidates. In particular, MOCAIP models the locations of each three components as a Gaussian distribution $X_{n}(i) \sim \mathcal{N}\left(\mu(i), \sigma^{2}(i)\right)$ for $i \in\{1,2,3\}$. Note that the component location distributions in MOCAIP are the same for every pulse whereas in this work the distributions change dynamically for different pulses. The parameters of the three Gaussian distributions are computed by fitting the training data that were used in the original publication (Hu et al., 2008c). The distributions thus learned using this approach remain the same for all patients. Then, the following score function is computed for all valid assignments $\mathcal{S}\left(i_{1}, i_{2}, i_{3}\right)=$ $p\left(X_{n}(1)=Y_{n}\left(i_{1}\right)\right)+p\left(X_{n}(2)=Y_{n}\left(i_{2}\right)\right)+p\left(X_{n}(3)=Y_{n}\left(i_{3}\right)\right)$. Furthermore, component $i$ is considered missing if $p\left(X_{n}(j) \geq Y_{n}\left(i_{j}\right)\right)<\rho$, for a pre-specified value $\rho$.

# Advantages of an individualized framework. 

Figure 6 compares the performance of DBN with ER transformation (DBN-ER) with the MOCAIP framework for a patient. In Figure 6(b), the MOCAIP framework uses component location densities obtained from a group of patients in for the component designation process. As a result, MOCAIP is prone to errors for patients whose component locations are not described well by the location densities computed during training. This is despite the fact that all three major components are included in the candidates. The DBN-ER framework, however, has the advantage of adapting component location distribution to each individual patients by: (I) modeling the evolution of $X_{n}(i)-X_{n-1}(i)$ resulting in a lower variance distribution, and (II) adapting distribution parameters as more data is received for each patient.

## Advantages of a dynamical model.

Another advantage of the DBN-ER framework is that the dynamical model allows for the correction of potential errors occurred during candidate detection step. Figure 7 shows an example where the first component location is missing in the candidates. Since the MOCAIP framework only allows the components to be selected from the candidates or be declared as missing, it does not detect the first component. On the other hand, in DBN-ER, components can take values that are not necessarily equal to candidates. In addition, DBN-ER leverages the dynamic model to reliably estimate the location of $X_{n}(1)$ given $X_{n-1}(1)$.

## Failure cases.

We present two cases where the proposed method fails to identify the components correctly. Figure 8 shows a corrupted ICP pulse that was not correctly classified during the preprocessing step of non-artifactual pulse recognition. An ICP pulse is considered corrupted when an expert classifies it as too noisy that reliable sub-peak assignment is not possible. Despite the fact that this pulse is visually corrupted, the algorithm detects one component. Although the proposed method improves over MOCAIP by not heavily relying on the candidate detections, the quality of the pulse and candidates still affect the performance.

This issue can be addressed by improving the non-artifactual pulse detection and candidate point detection modules.

Figure 9 shows an example where the algorithm correctly detects the third components in the first three pulses despite the fact that they are not included in the candidate peaks. However, after receiving observations for a few pulses, the algorithm wrongly concludes that the third component is not present as it is not detected in the candidate peaks for a while. This example shows that the algorithm is somewhat vulnerable to persistent errors in the observations. This problem can be addressed by improving the quality of component detection step. In addition, including more information from the ICP pulse besides the component location such as curvature and amplitude alleviates this problem and is left for future work.

# Overall performance. 

We compare the overall performance of our framework to the MOCAIP framework as well as another method based on clustering inspired by (Lee et al., 2015). For the clustering approach, we use the same pre-processing and candidate detection steps as in MOCAIP and apply the clustering method described in (Lee et al., 2015) for the final step of designating the three major components. Table 1 compares the accuracy of algorithms in detecting the three components over the test set in addition to the standard deviation of detection accuracy among the patients. DBN-ER significantly improves the detection accuracy of each component and obtains a more robust performance across patients owing to parameter adaptation.

As an additional performance measure, we compute a displacement error: the averaged difference between the detected sub-peaks $\left\{\bar{s}_{n}(1), \bar{s}_{n}(2), \bar{s}_{n}(3)\right\}$ and the expert labels $\left\{x_{n}^{n}(1), x_{n}^{n}(2), x_{n}^{n}(3)\right\}$

$$
\Delta_{i}=\frac{1}{\bar{n}_{i}} \sum_{n=1}^{\bar{n}_{i}}\left|\bar{s}_{n}(i)-x_{n}^{n}(i)\right|
$$

where $\bar{n}_{i}$ denotes the number of true detections of component $i$. Table 2 shows that DBN-ER achieves a smaller average displacement error. As discussed before, in some ICP pulses one or more components may be missing. In Table 2, we also compare the performance of the algorithms in their ability to correctly detect a missing sub-peak by obtaining true negative rate (TNR). Overall, DBN-ER performs well in identifying missing sub-peaks. The clustering method yields the best TNR for component 1. However, this score is due to the interval constraints of the clustering method that results in assigning missing value to many first sub-peaks despite their existence. Note that since the chance of missing sub-peaks is relatively small, true positive rates are close to the accuracies reported in Table 1.

## 5 Discussion

In this paper, we presented a fully automated and patient-adaptable framework based on a probabilistic dynamic model for the identification of pulsatile components from continuous

ICP signals. The efficacy of the proposed framework was evaluated by conducting experiments over more than 700 hours of ICP recordings. We compared our results with those yielded by the MOCAIP framework (Hu et al. 2008c) as well as a clustering approach inspired by (Lee et al. 2015), demonstrating significant improvements. The temporal feature of our framework enables recalling necessary information regarding the locations of components from previous pulses. This information in addition to the observations results in making more confident and robust decisions during the component designation step. The proposed framework deploys a probabilistic generative model which can also be used to make predictions on the arrival times of upcoming pulsatile components and provide uncertainty estimates for the predictions. We included static hidden variables in the DBN that are tuned for each patient as more data are received in an unsupervised manner, which allows for improved performance by making the detection mechanism individualized. The approach presented here is theoretically guaranteed, data-efficient, and interpretable.

In addition to MOCAIP, several other approaches are proposed for ICP sub-peak detection such as (Lee et al. 2015; Calisto et al. 2012). Since the implementation and specific details of these approaches are not publicly available, we implemented an algorithm inspired by the clustering approach of Lee et al. 2015 and compared the performance to our approach in the previous section. We now highlight the algorithmic and conceptual differences between these works and our work.

The method presented by Calisto et al. 2012 is not fully automated and cannot be used for real-time patient monitoring. For each patient, this method requires an expert to annotate the three pulsatile components of ten randomly-selected pulses and the annotations are later used for component identification. Furthermore, the non-artifactual pulses are recognized by comparing the current pulse with three preceding and three succeeding pulses, which performs poorly in case of a relatively persistent artifact. Similar to MOCAIP, Lee et al. 2015 also first finds a set of candidate locations. It then applies k-means on the candidates to assign three pulsatile components, unlike the method presented in this paper which finds the most likely location of pulsatile components using a Bayesian model-based approach. A main limitation of (Lee et al. 2015) is the preliminary step of manual removal of artifactual recordings by an expert which limits the use of the framework for fully automated patient monitoring. The above frameworks do not consider the dynamics of pulsatile components, the uncertain nature of the problem, and adaptability to individual patients, which are addressed in this paper. Our framework based on DBN-ER offers additional advantages such as flexibility in admitting more complex models and providing insights on the temporal model of the ICP.

## Future work

The model-based framework for ICP morphology analysis elicits several interesting extensions and directions for future work. Possible directions for technical improvements are described below.

The transition model.

The dynamical model presented in this paper is developed by analyzing the dynamics of ICP sub-peaks from annotated data and a simple understanding of human physiology. This results in a relatively simple model that admits only a few parameters, making it less prone to overfitting in clinical applications when data are relatively scarce. However, if more data are available, using a more complex model of the dynamics would greatly improve the performance. This goal can be achieved in several ways. For example, while we only considered the arrival time of ICP components, one can increase the modeling power by considering both the arrival time and signal amplitude of each component. Introducing hierarchical structures and incorporating the temporal and static effects of different neurological conditions on the pulsatile components are other ways of improving the model. Alternatively, one can deploy expert knowledge for designing a more complex model; an example of such a method is the recent work of Wang et al. 2019 that presents a lumped parameter network for modeling the ICP signal by leveraging mechanistic understanding of physiology. Finally, the current model only considers short-term temporal dependencies. Designing a framework that handles a long-term memory, a difficult challenge in machine learning, is a direction worth pursuing.

## The pre-processing step.

We used MOCAIP's pre-processing approach to obtain a sequence of dominant ICP pulses and eliminate noise followed by a candidate detection step. Improving non-artifactual pulse recognition and candidate detection modules is expected to increase the final accuracy. Furthermore, in the current implementation, the dominant pulse represents a short segment of the ICP recording. An interesting future direction is analyzing the morphology of individual pulses by combining the proposed DBN with alternative methods of handling noise and artifacts.

## The observations.

In the current framework, we only considered candidate locations as DBN observations. Including more observations could improve the performance of the framework at the cost of making the system more complex and perhaps, adding a requirement for using more advanced inference techniques. For instance, to alleviate the problem with detecting ICP components in corrupted pulses that are not removed in the pre-processing step, additional observations such as signal quality indices can be considered. Recent works demonstrated that DBNs that include raw signals as observations without a pre-processing or feature extraction step are highly effective. An example is a signal-based DBN presented in (Moore and Russell, 2017) where raw seismic signals are used as observations to achieve state-of-the-art performance in seismic monitoring.

In addition to technical improvements, research venues that have demonstrated the potential clinical values of quantitative ICP pulse morphological analysis (Hu et al. 2010b,a; Kasprowicz et al. 2010; Asgari et al. 2012; Scalzo et al. 2012b,c; Scalzo and Hu, 2013; Hu et al. 2012a; Liu et al. 2019, 2020) can readily benefit from a more accurate delineation of ICP pulse morphological features.

The authors would like to thank the anonymous reviewers for their comments and suggestions, which helped improve the quality and clarity of the manuscript. This work is supported by the Scalable Collaborative Human-Robot Learning (SCHooL) Project, a NSF National Robotics Initiative Award 1734633, and in part by NIH awards R01NS113541A1 and R01NS106905A1.

Aleks Norm, Russell Stuart J, Madden Michael G, Morabito Diane, Staudenmayer Kristan, Cohen Mitchell, and Manley Geoffrey T. Probabilistic detection of short events, with application to critical care monitoring. In Advances in Neural Information Processing Systems, pages 49--56, 2009.

Arroyo-Palacios Jorge, Rudz Maryna, Fidler Richard, Smith Wade, Ko Nerissa, Park Soojin, Bai Yong, and Hu Xiao. Characterization of shape differences among icp pulses predicts outcome of external ventricular drainage weaning trial. Neurocritical Care, 25(3):424--433, 2016. [PubMed: 27106888]

Asgari Shadnaz, Bergsneider Marvin, Hamilton Robert, Vespa Paul, and Hu Xiao. Consistent changes in intracranial pressure waveform morphology induced by acute hypercapnic cerebral vasodilatation. Neurocritical Care, 15(1):55--62, 2011a. [PubMed: 21052864]

Asgari Shadnaz, Subudhi Andrew W, Roach Robert C, Liebeskind David S, Bergsneider Marvin, and Hu Xiao. An extended model of intracranial latency facilitates non-invasive detection of cerebrovascular changes. Journal of Neuroscience Methods, 197(1):171--179, 2011b. [PubMed: 21310179]

Asgari Shadnaz, Vespa Paul, Bergsneider Marvin, and Hu Xiao. Lack of consistent intracranial pressure pulse morphological changes during episodes of microdialysis lactate/pyruvate ratio increase. Physiological Measurement, 32(10):1639, 2011c. [PubMed: 21904021]

Asgari Shadnaz, Gonzalez Nestor, Subudhi Andrew W, Hamilton Robert, Vespa Paul, Bergsneider Marvin, Roach Robert C, and Hu Xiao. Continuous detection of cerebral vasodilatation and vasoconstriction using intracranial pulse morphological template matching. PLoS One, 7(11), 2012.

Asgari Shadnaz, Vespa Paul, and Hu Xiao. Is there any association between cerebral vasoconstriction/vasodilatation and microdialysis lactate to pyruvate ratio increase? Neurocritical Care, 19 (1):56--64, 2013. [PubMed: 23733172]

Calisto Andrea, Galeano Massimiliano, Serrano Salvatore, Calisto Amedeo, and Azzerboni Bruno. A new approach for investigating intracranial pressure signal: filtering and morphological features extraction from continuous recording. IEEE Transactions on Biomedical Engineering, 60(3):830--837, 2012. [PubMed: 22453602]

Chen Hugh, Erol Yusuf, Shen Eric, and Russell Stuart. Probabilistic model-based approach for heart beat detection. Physiological Measurement, 37(9):1404, 2016. [PubMed: 27480267]

Connolly Mark, Vespa Paul, Pouratian Nader, Gonzalez Nestor R, and Hu Xiao. Characterization of the relationship between intracranial pressure and electroencephalographic monitoring in burst-suppressed patients. Neurocritical Care, 22(2):212--220, 2015. [PubMed: 25142827]

Eide Per Kristian, Sroka Marek, Wozniak Aleksandra, and Sæhle Terje. Morphological characterization of cardiac induced intracranial pressure (ICP) waves in patients with overdrainage of cerebrospinal fluid and negative ICP. Medical Engineering & Physics, 34(8):1066--1070, 2012. [PubMed: 22153319]

García María, Poza Jesús, Santamarta David, Abásolo Daniel, Barrio Patricia, and Hornero Roberto. Spectral analysis of intracranial pressure signals recorded during infusion studies in patients with hydrocephalus. Medical Engineering & Physics, 35(10):1490--1498, 2013. [PubMed: 23664413]

García María, Poza Jesús, Santamarta David, Romero-Oraá Roberto, and Hornero Roberto. Continuous wavelet transform in the study of the time-scale properties of intracranial pressure in hydrocephalus. Philosophical Transactions of the Royal Society A: Mathematical, Physical and Engineering Sciences, 376(2126):20170251, 2018.

Giudici Paolo and Spelta Alessandro. Graphical network models for international financial flows. Journal of Business & Economic Statistics, 34(1):128--138, 2016.

Gordon Neil J, Salmond David J, and Smith Adrian FM. Novel approach to non-linear/non-Gaussian Bayesian state estimation. In IEEE Proceedings in Radar and Signal Processing, volume 140, pages 107-113. IET, 1993.
Heldt Thomas, Long Bill, George C Verghese Peter Szolovits, and Mark Roger G. Integrating data, models, and reasoning in critical care. In 2006 International Conference of the IEEE Engineering in Medicine and Biology Society, pages 350-353. IEEE, 2006.
Holm Sverre and Eide Per Kristian. The frequency domain versus time domain methods for processing of intracranial pressure (ICP) signals. Medical Engineering \& Physics, 30(2):164-170, 2008. [PubMed: 17468029]
Hornero Roberto, Aboy Mateo, Abásolo Daniel, McNames James, and Goldstein Brahm. Interpretation of approximate entropy: analysis of intracranial pressure approximate entropy during acute intracranial hypertension. IEEE Transactions on Biomedical Engineering, 52(10):1671-1680, 2005. [PubMed: 16235653]
Hornero Roberto, Aboy Mateo, and Abásolo Daniel. Analysis of intracranial pressure during acute intracranial hypertension using lempel-ziv complexity: further evidence. Medical \& Biological Engineering \& Computing, 45(6):617-620, 2007. [PubMed: 17541667]
Hu Xiao, Nenov Valeriy, Bergsneider Marvin, Thomas C Glenn Paul Vespa, and Martin Neil. Estimation of hidden state variables of the intracranial system using constrained nonlinear Kalman filters. IEEE Transactions on Biomedical Engineering, 54(4):597-610, 2007. [PubMed: 17405367]
Hu Xiao, Miller Chad, Vespa Paul, and Bergsneider Marvin. Adaptive computation of approximate entropy and its application in integrative analysis of irregularity of heart rate variability and intracranial pressure signals. Medical Engineering \& Physics, 30(5):631-639, 2008a. [PubMed: 17714974]
Hu Xiao, Xu Peng, Darrin J Lee Paul Vespa, Baldwin Kevin, and Bergsneider Marvin. An algorithm for extracting intracranial pressure latency relative to electrocardiogram R wave. Physiological Measurement, 29(4):459, 2008b. [PubMed: 18354246]
Hu Xiao, Xu Peng, Scalzo Fabien, Vespa Paul, and Bergsneider Marvin. Morphological clustering and analysis of continuous intracranial pressure. IEEE Transactions on Biomedical Engineering, 56(3):696-705, 2008c. [PubMed: 19272879]
Hu Xiao, Andrew W Subudhi Peng Xu, Asgari Shadnaz, Roach Robert C, and Bergsneider Marvin. Inferring cerebrovascular changes from latencies of systemic and intracranial pulses: a modelbased latency subtraction algorithm. Journal of Cerebral Blood Flow \& Metabolism, 29(4):688697, 2009. [PubMed: 19142194]
Hu Xiao, Glenn Thomas, Scalzo Fabien, Bergsneider Marvin, Sarkiss Chris, Martin Neil, and Vespa Paul. Intracranial pressure pulse morphological features improved detection of decreased cerebral blood flow. Physiological Measurement, 31(5):679, 2010a. [PubMed: 20348611]
Hu Xiao, Xu Peng, Asgari Shadnaz, Vespa Paul, and Bergsneider Marvin. Forecasting icp elevation based on prescient changes of intracranial pressure waveform morphology. IEEE Transactions on Biomedical Engineering, 57(5):1070-1078, 2010b. [PubMed: 20659820]
Hu Xiao, Gonzalez Nestor, and Bergsneider Marvin. Steady-state indicators of the intracranial pressure dynamic system using geodesic distance of the ICP pulse waveform. Physiological Measurement, 33(12):2017, 2012a. [PubMed: 23151442]
Hu Xiao, Hamilton Robert, Baldwin Kevin, Vespa Paul M, and Bergsneider Marvin. Automated extraction of decision rules for predicting lumbar drain outcome by analyzing overnight intracranial pressure. In Intracranial Pressure and Brain Monitoring XIV, pages 207-212. Springer, 2012b.
Hüser Matthias, Kündig Adrian, Karlen Walter, De Luca Valeria, and Jaggi Martin. Forecasting intracranial hypertension using multi-scale waveform metrics. Physiological Measurement, 41(1):014001, 2020. [PubMed: 31851948]
Kanazawa Keiji, Koller Daphne, and Russell Stuart. Stochastic simulation algorithms for dynamic probabilistic networks. In Proceedings of the Eleventh Conference on Uncertainty in Artificial Intelligence, pages 346-351. Morgan Kaufmann Publishers Inc., 1995.
Kasprowicz Magdalena, Asgari Shadnaz, Bergsneider Marvin, Czosnyka Marek, Hamilton Robert, and Hu Xiao. Pattern recognition of overnight intracranial pressure slow waves using morphological

features of intracranial pressure pulse. Journal of Neuroscience Methods, 190(2):310-318, 2010. [PubMed: 20566403]
Lee Hack-Jin, Jeong Eun-Jin, Kim Hakseung, Czosnyka Marek, and Kim Dong-Joo. Morphological feature extraction from a continuous intracranial pressure pulse via a peak clustering algorithm. IEEE Transactions on Biomedical Engineering, 63(10):2169-2176, 2015. [PubMed: 26841386]
Li Tiancheng, Bolic Miodrag, and Djuric Petar M. Resampling methods for particle filtering: classification, implementation, and strategies. IEEE Signal Processing Magazine, 32(3):70-86, 2015.

Liu Xiuyun, Zimmermann Lara L, Ho Nhi, Vespa Paul, Liao Xiaoling, and Hu Xiao. Cerebral vascular changes during acute intracranial pressure drop. Neurocritical Care, 30(3):635-644, 2019. [PubMed: 30523541]
Liu Xiuyun, Vitt Jeffrey R, Hetts Steven W, Gudelunas Koa, Ho Nhi, Ko Nerissa, and Hu Xiao. Morphological changes of intracranial pressure quantifies vasodilatory effect of verapamil to treat cerebral vasospasm. Journal of Neurointerventional Surgery, 2020.
Megjhani Murad, Alkhachroum Ayham, Terilli Kalijah, Ford Jenna, Rubinos Clio, Kromm Julie, Wallace Brendan K, Connolly E Sander, Roh David, Agarwal Sachin, et al. An active learning framework for enhancing identification of non-artifactual intracranial pressure waveforms. Physiological Measurement, 40(1):015002, 2019. [PubMed: 30562165]
Moore David and Russell Stuart. Signal-based Bayesian seismic monitoring. In Artificial Intelligence and Statistics, pages 1293-1301, 2017.
Park Chanki, Ryu Seung Jun, Jeong Bong Hyun, Lee Sang Pyung, Hong Chang-Ki, Kim Yong Bae, and Lee Boreom. Real-time noninvasive intracranial state estimation using unscented kalman filter. IEEE Transactions on Neural Systems and Rehabilitation Engineering, 27(9):1931-1938, 2019. [PubMed: 31380765]
Riggelsen Carsten, Ohmberger Matthias, and Scherbaum Frank. Dynamic Bayesian networks for realtime classification of seismic signals. In European Conference on Principles of Data Mining and Knowledge Discovery, pages 565-572. Springer, 2007.
Santamarta D, Abásolo D, Fernández J, and Hornero R. Pulse amplitude and Lempel-Ziv complexity of the cerebrospinal fluid pressure signal. In Intracranial Pressure and Brain Monitoring XIV, pages 23-27. Springer, 2012.
Scalzo Fabien and Hu Xiao. Semi-supervised detection of intracranial pressure alarms using waveform dynamics. Physiological Measurement, 34(4):465, 2013. [PubMed: 23524637]
Scalzo Fabien, Xu Peng, Asgari Shadnaz, Bergsneider Marvin, and Hu Xiao. Regression analysis for peak designation in pulsatile pressure signals. Medical \& Biological Engineering \& Computing, 47(9):967-977, 2009. [PubMed: 19578916]
Scalzo Fabien, Asgari Shadnaz, Kim Sunghan, Bergsneider Marvin, and Hu Xiao. Robust peak recognition in intracranial pressure signals. Biomedical Engineering Online, 9(1):61, 2010. [PubMed: 20959014]
Scalzo Fabien, Asgari Shadnaz, Kim Sunghan, Bergsneider Marvin, and Hu Xiao. Bayesian tracking of intracranial pressure signal morphology. Artificial Intelligence in Medicine, 54(2):115-123, 2012a. [PubMed: 21968205]
Scalzo Fabien, Hamilton Robert, Asgari Shadnaz, Kim Sunghan, and Hu Xiao. Intracranial hypertension prediction using extremely randomized decision trees. Medical Engineering \& Physics, 34 (8):1058-1065, 2012b. [PubMed: 22401795]
Scalzo Fabien, Liebeskind David, and Hu Xiao. Reducing false intracranial pressure alarms using morphological waveform features. IEEE Transactions on Biomedical Engineering, 60(1):235-239, 2012c. [PubMed: 22851230]
Wang Jian-Xun, Hu Xiao, and Shadden Shawn C. Data-augmented modeling of intracranial pressure. Annals of Biomedical Engineering, 47(3):714-730, 2019. [PubMed: 30607645]
Williams Christopher, Quinn John, and Neil McIntosh. Factorial switching Kalman filters for condition monitoring in neonatal intensive care. In Advances in Neural Information Processing Systems, pages $1513-1520,2006$.

Xu Peng, Hu Xiao, and Yao Dezhong. Improved wavelet entropy calculation with window functions and its preliminary application to study intracranial pressure. Computers in Biology and Medicine, 43(5):425-433, 2013. [PubMed: 23566389]
Yang Guosheng, Lin Yingzi, and Bhattacharya Prabir. A driver fatigue recognition model based on information fusion and dynamic Bayesian network. Information Sciences, 180(10):1942-1954, 2010 .

![img-0.jpeg](img-0.jpeg)

Figure 1:
An example demonstrating sample impoverishment when the transition model exhibits high uncertainty but the observation model is fairly accurate. The particle filtering steps of propagation, weight assignment, and resampling, applied to a standard DBN, are shown in (a). As a result of the inaccurate transition model, most particles are far from the observation and are assigned small weights. During resampling, the particles with small weights are naturally eliminated resulting in a reduction in sample diversity. Particle filtering applied to a DBN with evidence reversal is shown in (b). Here, particles are sampled after the observation is received and therefore, more diverse particles compatible with the observation are generated.

![img-1.jpeg](img-1.jpeg)

Figure 2:
The left figure shows the standard DBN and the right figure shows the ER transformation.
The shaded nodes represent the observations.

![img-2.jpeg](img-2.jpeg)

Figure 3:
Flow chart of the proposed framework for ICP morphology analysis which includes data pre-processing, training, and inference over a dynamic Bayesian model. In the model, the latent variables are the ICP major pulsatile components $X_{n}=\left\{X_{n}^{1}, X_{n}^{2}, X_{n}^{3}\right\}$ and observed variables are the candidate locations $Y_{n}=\left\{Y_{n}^{1}, \ldots, Y_{n}^{C_{n}}\right\}$, where $C_{n}$ is a random variable representing the number of candidates obtained for pulse $n$.

![img-3.jpeg](img-3.jpeg)

Figure 4:
Histogram of $\eta_{b}(i)=X_{0}(i)-X_{0-1}(i)$ for three different patients and fitted Laplace and Gaussian distributions.

![img-4.jpeg](img-4.jpeg)

Figure 5:
Left: The probability density function (pdf) of Laplace $\left(X_{n-1}(i), b(i)\right)$ at candidate locations. $X_{n}(i)$ can take values only in the candidates that are greater than $L(i)$. Right: Hybrid probability distribution of $X_{n}(i)$ over the candidates, missing value, and a truncated Laplace distribution.

![img-5.jpeg](img-5.jpeg)

Figure 6:
The top plots show two consecutive ICP pulses for a patient and the performance of DBNER (left) and MOCAIP (right). The expert annotations are denoted by 1, 2, and 3. The bottom plots show the distributions over the locations of each components which are modeled by Laplace distributions $X_{0}(i)=\operatorname{Laplace}\left(X_{0-1}(i), b(i)\right)$ in DBN-ER and Gaussian distributions $X_{0}(i)=\operatorname{Normal}\left(\rho(i), \sigma^{2}(i)\right)$ in MOCAIP.

![img-6.jpeg](img-6.jpeg)

Figure 7:
Performance of MOCAIP (top) compared to DBN-ER (bottom) where a candidate is missing. The ability of DBN-ER to use the information from previous pulses and to detect components outside candidates reduces missed detections.

![img-7.jpeg](img-7.jpeg)

Figure 8:
An example where the DBN-ER algorithm fails to detect a corrupted ICP pulse.

![img-8.jpeg](img-8.jpeg)

Figure 9:
An example where existence of a persistent error in the observations results in missing the third component.

Table 1:
Accuracy of detecting three major ICP pulsatile components and the standard deviation of the detection accuracy among patients.


Table 2:
Average displacement errors $\Delta_{i}$ and true negative rates of difference algorithms.
