# Variational Gaussian Mixture Models with robust Dirichlet concentration priors for virtual population generation in hypertrophic cardiomyopathy: a comparison study 

Vasileios C. Pezoulas, Student Member, IEEE, Grigorios I. Grigoriadis, Nikolaos S. Tachos, Member<br>IEEE, Fausto Barlocco, Iacopo Olivotto, and Dimitrios I. Fotiadis, Fellow, IEEE


#### Abstract

Nowadays, there is an emerging need for the development of computationally efficient virtual population generators for large-scale clinical trials. In this work, we utilize Gaussian Mixture Models (GMM) with variational Bayesian inference (BGMM) using robust estimations of Dirichlet concentration priors for the generation of virtual populations. The estimations were based on an exponential transformation of the number of Gaussian components. The proposed method was compared against state-of-the-art virtual data generators, such as, the Bayesian networks, the supervised tree ensembles (STE), the unsupervised tree ensembles (UTE), and the artificial neural networks (ANN) towards the generation of 20000 virtual patients in hypertrophic cardiomyopathy (HCM) clinical trials. Our results suggest that the proposed BGMM can yield virtual distributions with small inter- and intra-correlation difference ( 0.013 and 0.012 ), in less execution time ( 0.432 sec ) than the STE which achieved the second-best performance.


Keywords: Gaussian Mixture Models, variational inference, Dirichlet concentration priors, Hypertrophic cardiomyopathy

## I. INTRODUCTION

In the recent years, there is an emerging need for virtual population generation in the domain of in-silico clinical trials (ISCTs), where the financial burden of expensive drug testing and development is large [1-4]. Virtual population generation is a computational approach which can provide insight into the pathogenic mechanisms of different diseases, such as, the cardiovascular diseases (CVDs) through the augmentation of real patient data with high-quality virtual patient data that "mimic" the real one. So far, virtual population generation has multiple applications in ISCTs specifically in drug testing and development [1, 3], as well as, in pharmacokinetics [2, 4].

Probabilistic approaches are the most common methods for virtual population generation [5, 6], where the synthetic samples are randomly drawn from the real distributions. A widely used probabilistic method is the multivariate normal distribution (MVND) which has been widely adopted for the generation of virtual patients in in-silico clinical trials, such as, in hypertrophic cardiomyopathy (HCM) [6]. MVND utilizes multi-dimensional normal distributions given the

[^0]mean vector and the covariance matrix of the real data to generate synthetic data. However, a fundamental assumption in MVND is that the real data follow a normal distribution. Bayesian networks [7] have been also used for the generation of virtual data based on conditional probabilities across different network topologies, where the nodes represent the features. Another family of virtual population generation involves the application of machine learning algorithms, such as, the supervised tree ensembles (STE), the unsupervised tree ensembles (UTE) [8-10], and the artificial neural networks (ANNs) with radial basis functions [8-10] which are trained on the real data and then transformed into data generators.

The emerging need for the development of computationally efficient virtual data generators yielding virtual data with reduced inter- and intra- correlation with the real data remains a technical challenge. The state-of-the-art virtual generators yield high-quality virtual data with reduced goodness of fit (gof) values, such as, the UTE [8]. The gof, however, assumes that the distributions belong to a particular set of distributions [11] and thus introduced biases in the outcomes. In addition, the STE, and the ANN $[9,10]$ require a target feature which influences the associations of the virtual features. Moreover, in the case of Bayesian networks, the number of all possible permutations of edges is infinite [7]. Furthermore, these methods are computationally demanding due to the training execution time which is crucial in large-scale clinical trials.

Towards this direction, Gaussian Mixture Models (GMMs) with variational Bayesian inference (BGMM) were developed to generate large-scale virtual populations. The proposed method utilizes Dirichlet process mixtures as the BGMM's prior structure, where the concentration of each component on the weight distribution is an exponential function of the number of components. Our approach was compared against state-of-the-art virtual data generators, including the Bayesian networks, the STE, the UTE, and the ANN for the generation of 20000 virtual patients for in-silico clinical trials in HCM yielding the lowest inter- and intra-correlation differences ( 0.013 and 0.012 ), in less execution time ( 0.432 sec ) than the STE ( 46.537 sec ) which had the second-best performance.

[^1]
[^0]:    *This project has received funding from the European Union's Horizon 2020 research and innovation programme under grant agreement No 777204. This paper reflects only the author's view and the Commission is not responsible for any use that may be made of the information it contains.
    V.C. Pezoulas, G.I. Grigoriadis and N.S. Tachos are with the Unit of Medical Technology and Intelligent Information Systems, Dept. of Materials Science and Engineering, University of Ioannina, GR 45110 Ioannina, Greece (e-mails: bpezoulas@gmail.com, greg8grigoriadis@gmail.com, ntachos@gmail.com).

[^1]:    D.I. Fotiadis is with the Department of Biomedical Research, Institute of Molecular Biology and Biotechnology, FORTH, Ioannina, Greece and the Dept. of Materials Science and Engineering, Unit of Medical Technology and Intelligent Information Systems, University of Ioannina, GR 45110, Ioannina, Greece (e-mail: fotiadis@uoi.gr).
    F. Barlocco and I. Olivotto are with the Department of Experimental and Clinical Medicine, University of Florence and Cardiomyopathies Unit, Azienda Ospedaliera Careggi, Florence, Italy (e-mails: fausto.barlocco@unifi.it, iacopo.olivotto@gmail.com).

## II. Materials And Methods

## A. Data sharing and data quality control

Anonymized data were obtained from 776 patients under the SILICOFCM project [12]. The dataset included 20 features related to demographic and echocardiographic measurements. A data curation pipeline presented in a previous study [13] was applied on the clinical data to remove outliers, duplicated fields, and inconsistent data types using both univariate and multivariate methods [13].

## B. Methods for virtual population generation

1) Bayesian networks

Bayesian networks [14] are based on the definition of a directed acyclic graph (DAG) as a set $\boldsymbol{D}=(\boldsymbol{V}, \boldsymbol{E})$, where $\boldsymbol{V}$ is a set of nodes and $\boldsymbol{E}$ is a set of directed edges between the nodes in $\boldsymbol{V}$. Each node $v \in \boldsymbol{V}$ is assigned to a random variable, say $x_{v}$, with parents, say $x_{p a(v)}$, yielding a set $\boldsymbol{X}=x_{v}, v \in \boldsymbol{V}$. Then, a set of probabilities, say $\boldsymbol{P}=p_{v}, v \in \boldsymbol{V}$, is defined:

$$
p_{v}=p\left(x_{v} \mid x_{p a(v)}\right)
$$

The probability in (1) is the local probability distribution for the random variable $x_{v}$ around $v$. Assuming conditional independencies among these variables, (1) is re-written as:

$$
p_{v}=\prod_{c \in C} p\left(x_{c} \mid x_{p a(c)}\right) \prod_{d \in D} p\left(x_{d} \mid x_{p a(c)}, x_{p a(d)}\right)
$$

where, $p\left(x_{d} \mid x_{p a(c)}, x_{p a(d)}\right)$ is the conditional probability of $x_{c}$ given the parents of both the discrete and the continuous variables, $x_{p a(c)}, x_{p a(d)}$, and $p\left(x_{c} \mid x_{p a(c)}\right)$ is the conditional probability of variable $x_{c}$ given $x_{p a(c)}$.

## 2) Tree ensembles

Both supervised tree ensembles (STE) and unsupervised tree ensembles (UTE) were used for virtual population generation [8-10]. In the supervised schema, an ensemble of decision trees is built, where in each tree node, the univariate empirical cumulative distribution function (ECDF) of the splitting feature is captured. In the unsupervised schema, a density forest ensemble is built, where the ensembles are density trees instead of decision trees [8-10]. In this case, the variance is used for the selection of the splitting feature.

## 3) Artificial neural networks

Artificial neural networks (ANNs) were also used for virtual population generation, where Gaussian radial basis functions (RBFs) are used as activation functions [9, 10]. In this case, the Gaussian RBFs are defined as in:

$$
y(\boldsymbol{x})=\sum_{i=1}^{N} w_{i} \exp \left(-\beta\left|\mid \boldsymbol{x}-x_{i}\right|^{2}\right)
$$

where $\boldsymbol{x}$ is an input vector with $N$-features, $x_{i}$ is the center vector, $y(\boldsymbol{x})$ is the output, $w_{i}$ is the weight of the $i$-th neuron, and $\beta$ is a standard Gaussian parameter.
4) Gaussian Mixture Models with variational inference

A Gaussian mixture model (GMM) is a probabilistic model which assumes that the samples are generated from a mixture of a finite number of Gaussian distributions with unknown parameters [15]. A GMM approximation is defined as:

$$
q(\boldsymbol{x} ; \boldsymbol{\theta})=\sum_{i=1}^{N} q(i ; \boldsymbol{\theta}) q(\boldsymbol{x} \mid i ; \boldsymbol{\theta})
$$

where $i$ is the mixture component, $\boldsymbol{\theta}$ is the set of hyperparameters, $q(i ; \boldsymbol{\theta})$ are the mixture weights, and $q(\boldsymbol{x} \mid i ; \boldsymbol{\theta})$ is a multivariate normal distribution (MVND) with mean $\boldsymbol{\mu}_{\boldsymbol{o}}$ and covariance matrix $\boldsymbol{\Sigma}_{\boldsymbol{o}}, N\left(\boldsymbol{x} \mid \boldsymbol{\mu}_{\boldsymbol{o}}, \boldsymbol{\Sigma}_{\boldsymbol{o}}\right)$. A common approach for estimating $\boldsymbol{\theta}$ is based on the expectation-maximization algorithm which maximizes the data likelihood [15]. The EM, however, might yield GMMs with topologies that might not fit well to the underlying data structures. A solution to this is provided by variational inference (VI), which seeks for a lower bound on the model evidence instead of the likelihood. The goal of the GMM with variational Bayesian inference (BGMM) is to estimate the hyper-parameter(s) $\boldsymbol{\theta}$ in $q(\boldsymbol{x} ; \boldsymbol{\theta})$, so that the Kullback-Leibler (KL) divergence with the posterior distribution $p(\boldsymbol{x})$ is minimized.

The KL-divergence is defined as in [16]:

$$
K L(q(\boldsymbol{x} ; \boldsymbol{\theta}) \| p(\boldsymbol{x}))=\int_{\boldsymbol{x}} q(\boldsymbol{x} ; \boldsymbol{\theta}) \log \left(\frac{q(\boldsymbol{x} ; \boldsymbol{\theta})}{p(\boldsymbol{x})}\right) d \boldsymbol{x}
$$

where the quotient of the search model over the posterior is the logarithm of the evidence, $L(\boldsymbol{\theta})$. Minimizing (5) is the same as maximizing a lower bound on $L(\boldsymbol{\theta})$ :

$$
\left.\arg \max_{\theta} \int_{x} q(\boldsymbol{x} ; \boldsymbol{\theta})(\log (p(\boldsymbol{x}))-\log (q(\boldsymbol{x} ; \boldsymbol{\theta}))) d \boldsymbol{x}\right]
$$

which is referred to as the Evidence Lower Bound Objective (ELBO) [17]. In the case of GMM, where the search model is a multivariate normal distribution, (6) becomes:

$$
\arg \max_{\theta} \int_{x} q(\boldsymbol{x} ; \boldsymbol{\theta})(R(\boldsymbol{x})+\log (\bar{q}(i \mid \boldsymbol{x}))) d \boldsymbol{x}+H(q)
$$

where $R(\boldsymbol{x})$ is equal to $\log (p(x))$ and $H(q)=H(q(x \mid i))=$ $-\int_{\boldsymbol{x}} q(\boldsymbol{x} ; \boldsymbol{\theta}) \log (q(\boldsymbol{x} ; \boldsymbol{\theta})) d \boldsymbol{x}$ is the entropy of $q(\boldsymbol{x} ; \boldsymbol{\theta})$.

## 5) Proposed BGMM approach

Due to its Bayesian rationale, VI needs more hyperparameters than EM, the most important of these being the concentration prior of the BGMM [17-19]. A common practice is to define the BGMM's prior structure according to a Dirichlet process mixture with concentration (or gamma) values equal to the inverse of the number of the Gaussian components [17-19]. However, in that case, a small weight concentration value with many components would make the model put most of the weights close to zero [17-19]. In this work, we utilize Dirichlet process mixtures as the BGMM's prior structure, where the concentration of each component on the weight distribution is defined as an exponential function of different Gaussian components to yield a stable number of components across multiple runs.

## C. Virtual data quality evaluation

1) Variability and explainability

A key issue in virtual population generation lies in the underlying variability of the associations among the features in the virtual data which directly affects the explainability of the virtual data generators. In this work, we compute the intracorrelation as the average of the correlation differences between the real and the virtual data, on a feature basis, to examine whether the associations between the features in the virtual data are preserved across multiple runs. The intercorrelation was also calculated as the overall mean correlation difference to examine the explainability of the generators.

## 2) Goodness of fit (gof)

The goodness of fit (gof) test statistic [8] is used to quantify the similarity among the real and the virtual distributions as described in [8]. Large gof value denotes distributions with increased similarity wit the absence of statistical significance.

## 3) Kullback-Leibler (KL) divergence

The Kullback-Leibler ( $K L$ ) divergence [20] is defined as in (5), where $q(\boldsymbol{x} ; \boldsymbol{\theta})$ and $p(\boldsymbol{x})$ are replaced by the probability densities of the real data and the virtual data, respectively. KL values close to 0 denote distributions with small divergence.

## III. RESULTS

## A. Data quality evaluation

All detected outliers and duplicated fields, as well as, features with high number of missing records were removed from further analysis. The final curated dataset included 11 features, namely the: (i) "Ech_Echo_LA" (Left Atrium), (ii) "Ech_Echo_LVIDs" (Left ventricular internal dimension), "ABNORMAL_HOLTER" (Abnormal Holter indicator), "Ech_Echo_Aortic_Root", "NYHA" (New York Heart Association class), "ARRHYTHMIA_NSVT" (Non sustained ventricular tachycardia), "Ech_Echo_PW" (Pulse Wave Doppler), "BMI" (Body Mass Index), "BSA" (Body Surface Area), "Height", "High_Risk". These features were used to evaluate the generators across multiple virtual patients in the range [1000, 20000] with a step 1000.

## B. BGMM hyperparameter tuning

The average goodness of fit and inter-correlation values are depicted in Fig. 1 for components in the interval [1, 30]. For illustration purposes, the number of virtual patients has been restricted in the interval [1000, 10000].
![img-0.jpeg](img-0.jpeg)

Figure 1: Performance evaluation of the proposed BGMM across multiple virtual patients in range [1000,10000].
According to Fig. 1, the average gof value was less than 0.1 for more than 5 Gaussian components. The average intercorrelation difference was less than 0.04 across the multiple virtual populations' executions and in some executions even
less than 0.03 . The average goodness of fit and correlation values from the four most prominent Gaussian components of Fig. 1 (i.e., for 19, 20, 24, and 25 components) are depicted in Fig. 2, along with the corresponding KL divergence and log-likelihood scores (which are referred to as BGMM scores). According to Fig. 2, the number of components that yielded virtual data with the smallest goodness of fit, KL divergence scores, correlation values, and the highest BGMM scores, across all executions, was 24 . This number was combined with the Dirichlet concentration (gamma) value to generate multiple virtual patients.
![img-1.jpeg](img-1.jpeg)

Figure 2: Performance evaluation of the proposed BGMM for the four best components across multiple virtual patients.

## C. Performance comparison

For comparison purposes, the number of virtual patients was set to 20000. According to Table 1, the proposed BGMM approach achieved the lowest gof (less than 0.1) along with the UTE and the STE compared to the RBF-based ANN and the Bayesian networks. In addition, the proposed BGMM method yielded the lowest inter- and intra-correlation differences between the features in the virtual data ( 0.0133 inter-correlation and 0.0121 intra-correlation). In all cases, the average KL divergence was less than 0.001 .

Table I: Performance Evaluation Results.


According to Fig. 4, the average execution time of the proposed BGMM approach was faster than the UTE and the STE methods, yielding multiple virtual populations in 0.432 sec against the UTE and the STE which required 46.537 sec , and 34.096 sec , respectively. The average execution times of

the ANNs and the Bayesian methods were comparable with the proposed BGMM approach (1.5919 sec for the ANN and 0.4863 for the Bayesian) but with poor performance.
![img-2.jpeg](img-2.jpeg)

Figure 3: Execution time (sec) per virtual data generator.

## IV. CONCLUSIONS

In this work, we utilized probabilistic Gaussian Mixture Models with variational Bayesian inference (BGMM) towards the generation of large-scale virtual populations for in-silico clinical trials in HCM. The proposed approach uses weight concentration values for variational inference which are based on an exponentially decaying transformation of the number of Gaussian components. The proposed approach was compared against state-of-the-art virtual data generators, including, the Bayesian networks, the supervised tree ensembles (STE), the unsupervised tree ensembles (UTE), and the ANN yielding better inter- and intra- correlation differences in less execution time than the unsupervised tree ensembles which achieved the second-best performance.

The proposed method for the estimation of the Dirichlet concentration of each component on the weight distribution yielded a stable number of components ( 24 components) across multiple virtual populations executions, where the prior structure of the GMM was defined according to the Dirichlet process mixture. The proposed BGMM with the optimal number of Gaussian components achieved the lowest goodness of fit values (less than 0.1) along with the UTE and the STE compared to the RBF-based ANN and the Bayesian networks (with average gof larger than 0.15). In addition, the proposed BGMM method yielded the lowest inter- and intracorrelation differences between the features in the virtual data (almost 0.01 ), in less execution time ( 0.4319 sec ) than the STE ( 46.5373 sec ), which had the second-best performance. This confirms the computational efficiency of the proposed BGMM approach towards the generation of large-scale virtual populations for in-silico clinical trials in HCM.

As a future work, we plan to extend the proposed approach for data augmentation in other clinical domains, apart from in-silico clinical trials, as well as, investigate the effect of the Dirichlet processes on the prior structure of the Gaussian Mixture Models to yield more robust finite mixture models.
