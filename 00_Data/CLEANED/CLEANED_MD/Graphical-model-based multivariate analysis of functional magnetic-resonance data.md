# NIH Public Access 

Author Manuscript
Neuroimage. Author manuscript; available in PMC 2008 June 13.
Published in final edited form as:
Neuroimage. 2007 April 1; 35(2): 635-647.

## Graphical-model-based Multivariate Analysis of Functional Magnetic Resonance Data

Rong Chen ${ }^{*}$ and Edward H Herskovits ${ }^{\dagger}$<br>*Rong Chen is with the Department of Radiology, University of Pennsylvania, 3400 Spruce Street, Philadelphia, PA. Phone: 215-662-7797. E-mail: rong.chen@uphs.upenn.edu<br>$\dagger$ Edward H Herskovits is with the Department of Radiology, University of Pennsylvania, 3400 Spruce Street, Philadelphia, PA. Phone: 215-615-3705. E-mail: ehh@ieee.org


#### Abstract

We propose a method for the analysis of functional magnetic resonance (fMR) data, based on a Bayesian-network representation. Our method identifies multivariate linear/nonlinear voxelactivation pattern differences across groups, which may provide information complementary to that resulting from a general linear model (GLM)-based analysis. In addition, we describe a modelstabilization method based on data resampling, which may be helpful in the presence of small numbers of subjects, or when data are noisy.


## 1 Introduction

Many functional magnetic-resonance (fMR) studies center on finding activation differences among different groups, such as normal elderly vs. demented elderly (Buckner et al. (2000)), normal females vs. females with fragile-X syndrome (Tamm et al. (2002)), or reading Chinese characters versus Pinyin (Chen et al. (2002)). Most of these fMR studies examine functional segregation (Lazar et al. (2002); Worsley et al. (2002); Penny et al. (2003)), i.e., they examine a hypothesis in which a particular cortical area is specialized for some aspect of cognition. Evaluation of these hypotheses typically proceeds in two steps: within-subject analysis, to detect activated voxels for a single subject, followed by between-subject analysis, to determine activation-pattern differences among experimental groups. In this context, we denote by $F$ the categorical group-membership variable; for the sake of simplicity, we refer to $F$ as the clinical variable.

Methods for between-subject analysis are often mass univariate, and adopt the general linear model (GLM) framework. Most commonly, random-effects analysis (Penny et al. (2003)) is performed; in this approach, differences of observed effects are assumed to be due to a combination of data noise and between-subject variability. For example, using the SPM analysis application, (The Wellcome Department of Imaging, Institute of Neurology, University College London), a contrast image is computed for each subject, and GLM-based methods, such as the $t$-test or analysis of variance, are used to detect differences among these contrast images.

Although widely applied, mass-univariate statistical analysis of fMR data to characterize group differences has important limitations. First, as typically implemented, GLM-based methods

[^0]
[^0]:    Publisher's Disclaimer: This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

incorporate the assumption that voxel activations are consistent for subjects in the same group, and that intersubject variability within an experimental group is due to noise. Second, GLMbased methods can detect linear associations among voxel activation and $F$, but are not designed to detect nonlinear associations.

To highlight these limitations, assume that we are studying two groups of subjects performing the same task; group 1 is the experimental group, and group 2 consists of normal control subjects. Consider three scenarios, as depicted in Figure 1. In scenario 1 (Figure 1, top), for the experimental group, region A and only A is consistently activated in the task, and subjects in the normal control group manifest consistent activation in a brain region other than A. In this case, a GLM-based mass-univariate method will identify region A as characterizing group differences.

In scenario 2 (Figure 1, middle), control subjects manifest consistent activation in a brain region other than A or B. However, subjects in the experimental group engage two different subprocesses. Some of them engage a sub-process dependent only on region A; others engage a sub-process dependent only on region B. This scenario is an example of functional degeneracy (Edelman and Gally (2001); Price and Friston (2002);Noppeney et al. (2006)), defined as "the ability of elements that are structurally different to perform the same function or yield the same output" (Edelman and Gally (2001)). An example of functional degeneracy is seen when examining action retrieval. Phillips et al. suggested that an action for an object is retrieved either from visual structural features or from accessing semantic knowledge (Phillips et al. (2002)). GLM-based approaches cannot distinguish regions related to different sub-processes in the presence of functional degeneracy.

In the third scenario (Figure 1, bottom), subjects in both the experimental and control groups engage a process dependent on both A and B-an example of functional integration (Friston (1994)). Assume further that the association among $F$ and regions A and B is nonlinear, for example, an exclusive-OR (XOR) function. GLM-based methods cannot handle this type of nonlinear structure-function association, because, considered individually, neither A nor B manifests an activation difference between experimental and control groups.

To facilitate the detection of regions characterizing group differences in case of functional degeneracy or nonlinear associations among regions and the clinical variable, we propose a novel approach, called functional graphical-model-based multivariate analysis (fGAMMA). The major strength of fGAMMA is that it models multivariate associations among voxelactivation patterns and $F$, based on a Bayesian-network (BN) representation (Pearl (1988)).

As we described in Section 2.2, there are two major advantages to using Bayesian networks, rather than GLM-based approaches, to model associations among brain regions and $F$ : (1) a BN can represent linear or nonlinear associations among variables of interest; in fact, a BN can represent any joint distribution of categorical variables; and (2) a BN is a probabilistic model that encodes uncertainty, which could include data noise, experimental error, and uncertainty regarding cognitive processes.

Although the primary goal of our approach is to identify associations among voxel-activation patterns and $F$, it is important to identify a model that is stable under data perturbation, because a fMR study may involve small number of subjects, rendering the resulting model unstable to data noise. Therefore, we employ an ensemble-learning approach to stabilize the model. The rationale behind ensemble methods is to reduce model variability via averaging (Breiman (1996); Freund and Schapire (1996); Breiman (2001)).

The remainder of this paper is organized as follows: Section 2 describes fMR data preprocessing, within-subject analysis, Bayesian networks, and an overview of fGAMMA. We present experimental results in Section 3. Section 4 consists of discussion and conclusions.

# 2 Methods 

Figure 2 provides an overview of data flow within the fGAMMA framework. First, fMR images undergo preprocessing, to generate binary-voxel activation maps. Next, fGAMMA generates Bayesian-network model of associations among voxel variables and $F$, and a corresponding label field, in which each voxel is labeled as belonging to a cluster, or region of interest; this process may be embedded within a model-aggregation resampling framework, to evaluate how stable the Bayesian-network model is to data noise.

### 2.1 fMR data preprocessing and within-subject analysis

We used SPM2 for data preprocessing (Figure 2, Stage 1). First, we aligned the images within an acquisition, normalized them to the MNI space, and then smoothed the normalized images using a 9 mm -FWHM isotropic Gaussian kernel.

We also used SPM2 to perform within-subject analysis, that is, to detect the activation foci for a single subject (Friston et al. (1995)). We used a high-pass filter with a cut-off period of 128 seconds to remove low-frequency noise, and we used an $\operatorname{AR}(1)$ model to correct for serial correlation in the temporal domain. Statistics comparing the estimated effects with appropriate error measures were generated; these results constitute statistical parametric maps for each contrast of interest. Finally, we chose a $p$-value with family-wise error correction to threshold the statistical parametric maps; for each analysis, we chose this parameter from the typical range of $p$-value $[0.001,0.05]^{1}$. Thresholding yielded a binary effect map, whose voxels assume states in $\{0,1\}$, representing off (no effect) and on (effect) at each voxel, respectively. If the contrast of interest represents voxel activation, we herein refer to the generated effect map as a binary activation map.

### 2.2 Bayesian network

We use Bayesian networks to model multivariate associations among voxel-activation patterns and $F$. A Bayesian network $\mathcal{B}$ is a probabilistic graphical model defined as $\mathcal{B}=\{\mathcal{S}, \Theta\} ; \mathcal{S}$ and $\Theta$ are defined presently. The structure of the Bayesian network, $\mathcal{S}=\{\mathcal{V}, \mathcal{E}\}$, is a directed acyclic graph (DAG), where $\mathcal{V}=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ represents the variables in to be analyzed, and $\mathcal{E}$ is a set of edges representing associations among these variables. If $X_{i} \rightarrow X_{j}$ is an edge in $\mathcal{E}$, then $X_{i}$ is called a parent node of $X_{j}$. We use $p a\left(X_{j}\right)$ to denote the set of parents of $X_{j}$.

To quantify probabilistic associations among variables in a BN, we specify the conditionalprobability distribution $P\left(X_{i} \mid p a\left(X_{i}\right)\right)$. If the variables are continuous, the commonly used model assumes $P\left(X_{i} \mid p a\left(X_{i}\right)\right)$ is Gaussian, implying that the joint distribution of $\left\{X_{i}\right\}$ be multivariate Gaussian, which may be too restrictive for our application. To enable fGAMMA to detect nonlinear multivariate associations among voxel variables and $F$, we employ the discrete Bayesian network, in which all variables are categorical, to model this domain. In this case, when we assume that $P\left(X_{i} \mid p a\left(X_{i}\right)\right)$ is an unrestricted multinomial distribution, the corresponding BN can represent any joint distribution among these variables.

Each variable $X_{i}$ in a BN is associated with a conditional-probability table, which represents $p$ $\left(X_{i} \mid p a\left(X_{i}\right)\right)$. Let $\theta_{i j k}=p\left(X_{i}=k \mid p a\left(X_{i}\right)=\mathbf{j}\right)$ be the conditional probability of $X_{i}$ assuming state

[^0]
[^0]:    ${ }^{1}$ Ardekani, B., SPM Tutorial (Block Design Data), http://claymore.rfmh.org/public/computer_resources/swdocs/spmdoc.pdf. Statistical Parametric Mapping Courses, http://www.fil.ion.ucl.ac.uk/spm/course/

$k$, given that its parents, $p a\left(X_{i}\right)$, assume joint state $\mathbf{j}$; if $X_{i}$ does not have parents, then $\theta_{i \cdot k}=p$ $\left(X_{i}=k\right)$ is a marginal distribution. $\Theta=\left\{\theta_{i j k}\right\}$ constitutes the parameters of the BN.

An example of a simple BN is depicted in Figure 3. In this BN, $p a(F)=\{A, B\}$, and $p(F=1 \mid$ $A=1, B=0)=0.9$ means that the probability of a subject's being in group 1 , given that region A is activated and region B is not, is 0.9 .

Since the number of potential BN models increases exponentially in the number of variables, in our implementation we restricted the type of BN model in fGAMMA to have inverse-tree structure, as shown in Figure 4. In a Bayesian network with inverse-tree structure, $F$ is a leaf node and all other variables (for fGAMMA, all fMR voxel variables) are parents of $F$.

A common approach to BN generation from a data set $\mathbf{D}$ is to define a metric that captures the fidelity of a BN model to associations among variables in $\mathbf{D}$, as well as the parsimony of that model; this metric guides the search for $\mathcal{S} *$, the model that optimizes this metric. The most widely used metric is the BDe score (Herskovits (1991); Cooper and Herskovits (1992); Heckerman et al. (1995)); derivation of the $B D e$ score is based on the assumptions that each variable $X_{i}(1 \leq i \leq n)$ in $\mathcal{V}$ is discrete, that $X_{i}$ assumes a state in $\left\{1,2, \ldots, r_{i}\right\}$, where $r_{i}$ is the number of states that $X_{i}$ can assume (e.g., 2 for a binary variable), and that, for fixed structure $\mathcal{S}$, the prior distribution of $\Theta$ is Dirichlet: $P\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}} \mid \mathcal{S}\right) \sim D i\left(\alpha_{i j 1}, \ldots, \alpha_{i j r_{i}}\right)$. Given these assumptions, the $B D e$ score, $P(\mathbf{D} \mid \mathcal{S})$, can be expressed as

$$
P(\mathbf{D} \mid \mathcal{S})=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\Gamma\left(\alpha_{i j}\right)}{\Gamma\left(\alpha_{i j}+N_{i j}\right)} \int_{k=1}^{r_{i}} \frac{\Gamma\left(\alpha_{i j k}+N_{i j k}\right)}{\Gamma\left(\alpha_{i j k}\right)}
$$

where $N_{i j k}$ is the the number of samples in $\mathbf{D}$ for which $X_{i}=k$ and $p a\left(X_{i}\right)=\mathbf{j} ; q_{i}$ is the number of states $p a\left(X_{i}\right)$ can assume; $N_{i j}=\sum_{k} N_{i j k}$; and $\alpha_{i j}=\sum_{k} \alpha_{i j k}$. Note that $B D e$ metric, which does not distinguish among categorical variable states; that is, this score is invariant to inversion of all variables, or, in general, remapping of states of multinomial variables.

Given a fixed structure, the posterior distribution of $P\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}} \mid \mathcal{S}\right)$ is Dirichlet $D i$ $\left(\alpha_{i j 1}+N_{i j 1}, \ldots, \theta_{i j r_{i}}+N_{i j r_{i}}\right)$. The maximum a posterior estimation of parameters $\Theta$ are as follows:

$$
\widehat{\theta}_{i j k}=\frac{N_{i j k}+\alpha_{i j k}}{N_{i j}+\alpha_{i j}}
$$

$\hat{\theta}_{i j k}$ is the mean of posterior distribution. The variance of posterior which is

$$
\frac{\left(N_{i j k}+\alpha_{i j k}\right)\left(N_{i j}+\alpha_{i j}-N_{i j k}-\alpha_{i j k}\right)}{\left(N_{i j}+\alpha_{i j}\right)^{2}\left(N_{i j}+\alpha_{i j}+1\right)}
$$

can be used to describe the uncertainty in estimate $\theta_{i j k}$ (Gelman et al. (1995)).

# 2.3 Functional Graphical-model-based Multivariate Analysis 

As stated in the previous section, fGAMMA generates a Bayesian network with inverse-tree structure; in this network, which $F$ is the leaf node, and each parent of $F$ represents a ROI, or collection of voxels manifesting a common activation pattern. A key property of fGAMMA is that each ROI is among those most strongly associated with $F$.

Figure 5 explains how the generated Bayesian network distinguishes among subjects in different experimental groups. Assume that several regions are involved in performing a task (e.g., regions 1-6 in Figure 5(a)); we can model the associations among these regions and $F$

using a Bayesian network (Figure 5(b)). However, exhaustive search for the optimal Bayesian network is intractable, due to the sheer number of possible models. To solve this problem, we exploit a key property of Bayesian networks: conditional independence. Let $I(X ; Y \mid Z)$ represent the statement that $X$ and $Y$ are conditionally independent, given $Z$. Given a set of variables $\mathcal{V}$, which includes $X$ and $Y$, the Markov blanket of $X$ is defined as the smallest set in $\mathcal{V}$ that renders $X$ conditionally independent of $Y$, that is, $I(X ; Y \mid m b(X))$ for all $Y \in \mathcal{V} \backslash\{X, m b(X)\}$ (Pearl (1988); Koller and Sahami (1996)). In other words, given knowledge of the variables in $m b(F)$, knowledge of any other variables in $\mathcal{V}$ tells us nothing more about $F$, and thus will not increase predictive accuracy. Note that $m b(F)$ for a Bayesian network with inverse-tree structure is simply the parent set of $F$. We previously proved that the set of the parents of $F$ in a Bayesian network with inverse-tree structure (Figure 5 (c)) is guaranteed to be a subset of $m b(F)$ in the ground-truth Bayesian network (Figure 5(b)) (Chen and Herskovits (2005a)). Therefore, the ROIs generated by fGAMMA are among those that are most informative about $F$.

Let $\mathcal{V}$ be the set of all voxels defined in the standard MNI space. In the BN-generation process, fGAMMA identifies a subset of voxels $\mathbf{R V}=\left\{R V_{1}, \ldots, R V_{l}\right\}$ in $\mathcal{V}$ that are jointly informative about $F$. Belief-map generation constructs, for each $R V_{i}$, a ROI consisting of voxels that are probabilistically equivalent to $R V_{i}$. By probabilistically equivalent, we mean that two voxels tend to be in the same state across subjects and experimental conditions. Finally, in the modelaggregation step, fGAMMA checks for statistical artifacts, and modifies the BN model to obtain a stable model.

As previously described in Section 2.1, within-subject analysis for each subject $i$ yields a binary effect map $D_{i}$. Let $\mathbf{D}=\left\{D_{1}, D_{2}, \ldots, D_{M}\right\}$ and $F=\left\{F_{1}, F_{2}, \ldots, F_{M}\right\}$, where $M$ is the total number of subjects in the study. We provide the image data $\mathbf{D}$ and clinical variable $F$ as input to fGAMMA.
2.3.1 Bayesian-network generation-fGAMMA iteratively performs BN generation and belief-map generation: BN generation yields a small set of representative voxels, whose activation states are strongly associated with $F$, and belief-map generation yields a set of probabilistically equivalent voxels for each representative voxel; groups of probabilistically equivalent voxels constitute clusters of voxels that have similar probabilistic associations with $F$. Note that a particular cluster may not be spatially contiguous.

The overall goal of Bayesian-network generation is to select representative voxels that are strongly associated with $F$. In particular, fGAMMA searches for the representative-voxel set, $\mathbf{R V}^{*}=\left\{R V_{1}, R V_{2}, \ldots, R V_{l}\right\}$, that maximizes the $B D e$ score for the BN in which $p a(F)=\mathbf{R V}^{*}$. That is,

$$
\mathbf{R V}^{*}=\underset{\mathbf{R V}}{\operatorname{argmax}} B D e(\mathcal{S}, \mathbf{D})
$$

where $\mathcal{S}$ is an inverse-tree structure, and $p a(F)=\mathbf{R V}$ in $\mathcal{S}$.
Let $\mathcal{V}$ denote the entire voxel set. As the computational cost of exhaustive search over all possible $\mathbf{R V}$ sets grows exponentially with the number of voxels in $\mathcal{V}$, exhaustive search is infeasible for a nontrivial data set. Instead, fGAMMA employs heuristic search to find $\mathbf{R V *}$. Let $\mathbf{R} \mathbf{V}_{k}$ and $\mathbf{V}_{k}$ be the representative voxel set and the set of all candidate voxels in iteration $k$, respectively. fGAMMA starts with an empty representative voxel set $\mathbf{R} \mathbf{V}_{0}, \mathbf{V}_{0}=\mathcal{V}$, and iteration index $k=0$. On iteration $k+1$, fGAMMA first computes the $B D e$ score for the BN structure with $p a(F)=\mathbf{R} \mathbf{V}_{k}$, denoted by $B D e\left(\mathbf{R} \mathbf{V}_{k}\right)$; then we calculate $B D e\left(\mathbf{R} \mathbf{V}_{k} \cup\left\{V_{i}\right\}\right)$ for

$V_{i}$ in $\mathbf{V}_{k}$, and add it to a candidate set $\mathbf{A}$ if $\Delta\left(V_{i}\right)=B D e\left(\mathbf{R V}_{k} \cup\left\{V_{i}\right\}\right)-B D e\left(\mathbf{R V}_{k}\right)>0$. Within A, we search for the voxel that maximizes $\Delta\left(V_{i}\right)$, and we assign that voxel to $R V_{k+1}$. That is,

$$
R V_{k+1}=\underset{V_{i} \mid V_{i} \in \mathbf{A}}{\operatorname{argmax}} \Delta\left(V_{i}\right)
$$

The next step is to identify a set of voxels, $\mathbf{E} \subset \mathbf{V}_{k}$, that are probabilistically equivalent to $R V_{k+1}$. We describe the details of this step, including our definition of probabilistic equivalence, in the next paragraph. Finally, we add the new representative voxel to the representative voxel set $\left(\mathbf{R} \mathbf{V}_{k+1} \leftarrow \mathbf{R} \mathbf{V}_{k} \cup\left\{R V_{k+1}\right\}\right)$, we remove the new representative voxel and all voxels that are equivalent to it from the candidate voxel set $\left(\mathbf{V}_{k+1} \leftarrow \mathbf{V}_{k} \backslash\left\{\left\{R V_{k+1}\right\} \cup \mathbf{E}\right\}\right)$, we increment $k$, and proceed to the next iteration. The model-generation process ends when $\mathbf{A}=\varnothing$ or $\mathbf{V}_{k+1}=\varnothing$.
2.3.2 Belief-map generation-Belief-map generation identifies a set of ROIs; each ROI consists of a representative voxel and all voxels that are probabilistically equivalent to it. We define a voxel $X$ as probabilistically equivalent to voxel $Y$ if their probabilistic associations with $F$, that is, their conditional-probability distributions, are similar. For binary $X$ and $Y$, one measure of probabilistic equivalence is $P(X=0, Y=1) \approx 0$ and $P(X=1, Y=0) \approx 0$. In iteration $k$, fGAMMA's belief-map generation algorithm searches voxels in $\mathbf{A}$ rather than in $\mathbf{V}_{k-1}$ to generate the equivalence set $\mathbf{E}$, because $\Delta\left(R V_{k}\right)>0$, and $\mathbf{A}$ consists of all voxels $V_{i}$ in $\mathbf{V}_{k-1}$ for which $\Delta\left(V_{i}\right)>0$. Restricting the search space to $\mathbf{A}$ instead of $\mathbf{V}_{k-1}$ can greatly reduce search time and the false-positive rate, since $\mathbf{A}$ is typically a small subset of $\mathbf{V}_{k-1}$.

For each voxel $V_{i}$ in the candidate set $\mathbf{A}$, fGAMMA calculates the equivalence metric $s\left(V_{i}\right.$, $\left.R V_{k}\right)=P\left(V_{i}=1, R V_{k}=1\right)+P\left(V_{i}=0, R V_{k}=0\right)$ to define probabilistic equivalence. The similarity map, $\mathbf{S}=\left\{s\left(V_{1}, R V_{k}\right), \ldots, s\left(V_{l}, R V_{k}\right)\right\}\left(V_{i} \in \mathbf{A}\right)$, constitutes the input to belief-map generation. We treat as a clustering problem the task of inferring the equivalence set $\mathbf{E}$ for $R V_{k}$, based on the similarity map $\mathbf{S}$. We previously implemented a contextual-clustering algorithm to solve this problem (Chen and Herskovits (2005b)).

We refer to the mean similarity measure of voxels within each cluster as the centroid of that cluster. fGAMMA identifies the cluster with the largest centroid, and thus the greatest similarity measure, as the equivalence set for $R V_{k}$. This process labels each voxel with its equivalence-set membership. Let $L_{i}$ be the label variable associated with the voxel at location i. $\mathbf{L}=\left\{L_{1}, L_{2}, \ldots, L_{a}\right\}$ represents the label set, where $a$ is the number of voxels in $\mathbf{A}$.

To incorporate spatial information, we model the prior for $\mathbf{L}$ as a pairwise Markov random field (MRF). In particular, we employ a MRF with a second-order neighborhood system defined on a 3D lattice, as shown in Figure 6. For any voxel location $i$, the Markov blanket of $i$, denoted by $m b(i)$, consists of voxel locations associated with nonzero potential functions. Because in-plane resolution usually exceeds $z$-axis resolution for fMR experiments, we assume that interactions among voxels in the $x-y$ plane are stronger than those in the $z$ direction, and therefore that $m b(i)$ consists of the eight surrounding locations in the $x-y$ plane, and the two locations directly above and below $i$ in the $z$ direction, as shown in Figure 6. However, an fGAMMA user can specify any neighborhood type for the MRF.

Let $c$ be the number of clusters in the label map $\mathbf{L}(1 \leq c \leq a) . \mathrm{T}=\left\{\mu_{1}, \mu_{2}, \ldots, \mu_{c}\right\}$ is the set of centroids. Given $c$, the goal is to find $\overrightarrow{\mathbf{L}}$ and $\overrightarrow{\mathrm{T}}$, such that

$$
\{\overrightarrow{\mathrm{L}}, \overrightarrow{\mathrm{~T}}\}=\underset{\mathrm{L}, \mathrm{~T}}{\operatorname{argmax}} P(\mathbf{L}, \mathrm{~T} \mid \mathbf{S})
$$

$\mathbf{L}$ and $\hat{\mathrm{T}}$ are the MAP estimation of $\mathbf{L}$ and T , given $\mathbf{S}$. We use a generalized expectationmaximization (EM) method to solve this problem; this algorithm iteratively searches for $\mathbf{L}$ and T. In iteration $k$, our approach first finds $\mathbf{L}(k)$ that maximizes $P(\mathbf{L} \mid \mathbf{S}, \hat{\mathrm{T}}(k-1))$; then searches for $\hat{\mathrm{T}}(k)$ that maximizes $P(\mathrm{~T} \mid \mathbf{S}, \mathbf{L}(k))$. Finding $\hat{\mathrm{T}}(k)$ is straightforward: when $\mathbf{L}(k)$ is known, for all voxels in the same cluster based on $\mathbf{L}(k)$, the empirical mean of intensities in the similarity map is the best linear unbiased estimator of $\mu$.

Given $\hat{\mathrm{T}}$, the maximum a posteriori (MAP) estimate of $\mathbf{L}$ is

$$
\widehat{\mathbf{L}}=\underset{\mathbf{L}}{\operatorname{argmax}} \prod_{i, j} \varphi\left(L_{i}, L_{j}\right) \prod_{i} \phi\left(L_{i}, S_{i}\right)
$$

where $S_{i}=s\left(V_{i}, R V_{k}\right) ; \psi\left(L_{i}, L_{j}\right)=e^{-\beta\left(\mu(i)-\mu(j)\right)^{2}}$ and $\varphi\left(L_{i}, S_{i}\right)=e^{-\left(S^{i}-\mu(i)\right)^{2}} ; i \in \Lambda$ and $j \in m b$ (i). $\mu(i)$ is the centroid of the cluster to which voxel $i$ belongs. $\beta$ is a parameter controlling smoothness.

We use loopy belief propagation (Weiss (1997); Yedidia et al. (2003)) to find the MAP estimate of $\mathbf{L}$. The output of loopy belief propagation for each voxel is a vector with length $c$, whose values constitute the probability distribution for this voxel's membership in each cluster. We choose the mode of this distribution, which we call $\hat{L}_{i}$, to be the label for voxel location $i$. We present further details regarding Equation 7, the estimation of $c$, and loopy belief propagation in the Appendix.

In this manner, the label field $\Lambda$ stores probabilistic-equivalence. Let $N_{r}$ be the cardinality of $\mathbf{R V}$; then $\Lambda$ contains $N_{r}$ ROIs $\left\{C_{1}, C_{2}, \ldots, C_{N_{r}}\right\}$, each ROI consisting of a representative voxel and its equivalent voxels. For voxel $V_{i}$, if, based on $\hat{L}_{i}$, this voxel is probabilistically equivalent to representative voxel $R V_{k}$, we set the value of this voxel in $\Lambda$ to $k$; if a voxel is not equivalent to any representative voxel, we set its value in the label field to 0 . Each cluster in $\Lambda$ thus constitutes a ROI in which voxels are considered homogeneous with respect to their probabilistic association with $F$, as represented by the conditional probability distribution $P$ $\left(R V_{k} \mid F\right)$.
2.3.3 Model aggregation-Bayesian-network generation and belief-map generation yield a model $\mathcal{M}=(\mathcal{B}, \Lambda)$, where $\mathcal{B}$ and $\Lambda$ represent a Bayesian network and a label field, respectively. However, the model generated from $\mathbf{D}$, which consists of the activation maps for all subjects, may not be stable under data perturbation, for two reasons. First, a fMR study comparing groups or trial conditions may include a small number (e.g., dozens) of subjects, whereas the cardinality of the hypothesis space $\mathcal{H}$, from which we select the model, is an exponential function of the number of voxels. In this model-generation problem, if we have $N$ voxels in the stereotaxic space, and if we set the maximum length of $\mathbf{R V}$ to be $r$, then the size of the hypothesis space, $|\mathcal{H}|$, is $\sum_{k=1}^{r}\binom{N}{k}$. For $N=10000$ and $r=3,|\mathcal{H}|>10^{11}$. Due to the sheer size of H , there could exist many models with the same $B D e$ score. Second, Bayesian-network generation is based on greedy search, which may cause fGAMMA to be sensitive to small perturbations of $\mathbf{D}$.

We therefore implemented a model-aggregation algorithm to increase the stability of our results in the face of noise, undersampling, and heuristic search. This algorithm selects different subsets of $\mathbf{D}$, generates a model for each subset, and aggregates the resulting models. Let the training samples be $\mathbf{D}=\left\{D_{1}, \ldots, D_{M}\right\}$, where $M$ is the total number of subjects and $D_{i}$ is the activation map for subject $i$. We use the jackknife method to generate a subset of samples $\mathbf{D}^{i}$ $=\left\{D_{1}, \ldots, \mathrm{D}_{\mathrm{i}-1}, D_{i+1}, \ldots, D_{M}\right\}$, in which we exclude the activation map for subject $i$. For each

$\mathbf{D}^{i}$, we generate a model $\mathcal{M}^{i}=\left(\mathcal{B}^{i}, \Lambda^{i}\right)$. We thus obtain a model ensemble: $\Xi=$ $\left\{\mathcal{M}^{1}, \mathcal{M}^{2}, \ldots \mathcal{M}^{M}\right\}$. We induce a stabilized model by aggregating models in the ensemble $\Xi$.

Algorithm 1 delineates this model-aggregation process; $\mathbf{D}$ constitutes the input. Steps 1 and 2 generate a model ensemble $\Xi$. In step 3, we calculate the frequency of model pattern $j$, defined as

$$
f_{B}(j)=\sum_{i=1}^{M} 1_{\left\{\mathcal{B}^{i}=\mathcal{B}^{j}\right\}}
$$

where $\mathbf{1}_{\text {[cond] }}$ is an identity function, equal to 1 if cond is true, 0 otherwise; and $f_{\mathcal{B}}$ is the histogram of model occurrence for $\left\{\mathcal{B}^{i}\right\}$. In the next step we select the mode of $f_{\mathcal{B}}, \mathcal{B}^{\text {mode }}$, because $\mathcal{B}^{\text {mode }}$ is the most stable BN among $\left\{\mathcal{B}^{i}\right\}$. $\mathcal{B}^{\text {mode }}$ is associated with a set of models, $\left\{\mathcal{M}^{k}\right\}$, whose $\mathcal{B}^{k}=\mathcal{B}^{\text {mode }}$.

Since all $\left\{\Lambda^{k}\right\}$ are associated with $\mathcal{B}^{\text {mode }}$, their representative voxel sets must also be identical. However, the values of voxels in $\Lambda^{k}$ may differ among these models, because fGAMMA uses different data sets $\mathbf{D}^{i}$ to compute $\Lambda^{k}$ for each model. Therefore, we must aggregate these $\left\{\Lambda^{k}\right\}$; this process is shown in steps 5-8. To reconcile these differences, we create a class map $\mathcal{C}_{a}$ for each representative voxel $R V_{a}$ associated with $\mathcal{B}^{\text {mode }}$. Each voxel in the class map $\mathcal{C}_{a}$ is the probability of that voxel's belonging to class $a$, defined as:

$$
V_{c}(i)=\frac{\sum_{j=1}^{N_{r}} 1_{\left\{\Lambda_{i}^{j}=a\right\}}}{N_{r}}
$$

where $N_{r}$ is the cardinality of set $\left\{\Lambda^{k}\right\}$, and $\Lambda_{i}^{j}$ denote voxel $i$ in label field $\Lambda^{j}$. Finally, we assign a class to each voxel by voting. If a voxel is in class $a$ for the majority of subjects in $\left\{\mathcal{M}^{k}\right\}$, we set that voxel in $\Lambda^{\text {mode }}$ to $a$. The output of Algorithm 1 is an aggregated model $\mathcal{M}$ * $=\left(\mathcal{B}^{\text {mode }}, \Lambda^{\text {mode }}\right)$.

# 3 Experimental results 

In this section, we apply fGAMMA to synthetic data, and to data from a previously published study including young, and nondemented and demented older adults.

### 3.1 Simulated Data

In this experiment, we synthesized fMR data for 24 subjects, based on data from a visual-motor experiment available with Voxbo software (http://www.voxbo.org/). Each subject was presented with flashing lights, and either performed sequential finger tapping or rested, in eight 42 -second alternating blocks. The 14 volumes in each block were acquired 3 seconds apart; there were thus a total of 112 volumes. Image size was $64 \times 64 \times 45$, and spatial resolution was $3 \times 3 \times 3 \mathrm{~mm}^{3}$. For each subject, we generated a binary activation map, corresponding to each voxel's activation state. The activation regions included bilateral motor and visual areas.

We synthesized a study with two groups of 24 subjects each. Subjects in group 2 were exposed to a stimulus, whereas those in group 1 were not. In generating the data for group 2, we stipulated that exactly one of two regions, A and B , with equal probability, would be activated when a subject was exposed to the stimulus; that is, either region A or region B would be activated, but not both. This is a typical functional degeneracy scenario. In this manner, we generated 12 subjects with $[A=1, B=0, F=2]$ and 12 subjects with $[A=0, B=1, F=2]$,

where $[A=1, B=0, F=2]$ represents a subject with activation of region A , no activation of region B , and membership in group 2 .

In the MNI space, we created two bounding-boxes: bounding-box 1 incorporated right and left visual areas, and bounding-box 2 contained right and left motor areas. We used the binary activation map of the visual areas in the Voxbo data set as the activation map for region A, and that of the motor areas in the Voxbo data set as the activation map for region B. Let $D^{\text {simu }}(i)$ and $D^{\text {voxbo }}(i)$ represent the activation map of subject $i$ in simulated data and in Voxbo data, respectively. We initialized $D^{\text {simu }}(i)$ to zero at each voxel. For group 1, we created 24 activation-difference maps with all zero values, representing $[A=0, B=0, F=1]$. For each of the 12 samples of type $[A=1, B=0, F=2]$, region A was activated and B was not; since $A=$ 1 , for voxels in the bounding-box 1 , we set their values in $D^{\text {simu }}(i)$ to be same as those in $D^{\text {voxbo }}(i)$. Since $B=0$, for voxels in bounding-box 2 , their values in $D^{\text {simu }}(i)$ remained zero. We performed a similar procedure to generate 12 samples of type $[A=0, B=1, F=2]$.

We presented these 48 activation maps, and corresponding values for $F$, as input to fGAMMA. fGAMMA detected three clusters, shown in Figure 7. Cluster 1 (Figure 7(b)) corresponds to the strongly activated voxels in the visual region (A). Clusters 2 and 3 (Figure 7(d)) are within the motor region (B); fGAMMA detected two clusters in region B because there does not exist a single activation pattern in region B, as there does in region A. As shown in Figure 8, $R_{2}$ and $R_{3}$ jointly covers all activation patterns in region B for all subjects. Setting $p a(F)$ to $R V_{1}$, $R V_{2}$, and $R V_{3}$ clearly differentiates the two groups.

Model-aggregation results are shown in Figures 9 and 10. The empirical model distribution arising from jackknife sampling, $f_{\beta}$, is shown in Figure 9. Let $\mathcal{B}^{\text {oill }}$ denote the BN generated using all subjects without resampling (i.e., D). In Figure 9, we also show how many BNs in model ensemble are identical to $\mathcal{B}^{\text {oill }}$, and annotate that portion of the histogram with $\mathcal{B}^{\text {oill }}$. fGAMMA generated 11 different BN patterns in the model ensemble; the mode has frequency 0.79 ; $\mathcal{B}^{\text {mode }}$ is identical to $\mathcal{B}^{\text {oill }}$ in this simulated data set. Therefore, we conclude that $\mathcal{B}^{\text {mode }}$ is stable under data perturbation. Class maps are shown in Figure 10; there are differences among $\left\{\Lambda^{k} \mid \mathcal{B}^{k}=\mathcal{B}^{\text {mode }}\right\}$. The label field $\Lambda^{\text {mode }}$ is consistent with the majority of $\Lambda^{k}$

To demonstrate that fGAMMA can detect multivariate associations among brain regions and $F$ that cannot be identified by GLM-based mass-univariate methods, we performed a twosample $t$-test on the same simulated data. In particular, we used the contrast map of the visual area in the Voxbo data set as the contrast map for region A, and that of the motor areas in the Voxbo data set as the contrast map for region B. We then computed $t$ statistics for these contrast maps to compare between group voxel-activation differences. The resulting $t$-map is depicted in Figure 11; both regions A and B demonstrate more activation foci in group 2 than in group 1. The $t$-test does detect a region within which activation levels are significantly different across groups; however, these results cannot be used to delineate interactions among regions and $F$. Although the activation patterns of these two regions are quite different during the task, we cannot distinguish them based on only this $t$-map.

# 3.2 A study of young, nondemented, and demented older adults 

In addition to testing fGAMMA on simulated data, we applied fGAMMA to data from a previously published fMR study of nondemented young adults, nondemented older adults, and demented older adults (Buckner et al. (2000)). A subject with dementia of the Alzheimer type manifests cognitive deficits such as memory impairment, language disturbance, or impaired ability to carry out motor activities despite intact motor function. We obtained data for 41 subjects from the registry of the Washington University Alzheimer Disease Research Center (Buckner et al. (2000)). Participants were English-speaking and right-handed. People with

neurological, psychiatric, or medical illness that could cause dementia were excluded from this study. Older subjects were assessed with the Clinical Dementia Rating (CDR) (Morris (1993)), where CDR=0 indicates no dementia, CDR=0.5 indicates very mild dementia, and CDR=1 indicates mild dementia of the Alzheimer type. There were 14 participants ( 5 male) with mean age 21.1 years in the young-adult group. The nondemented older-adult group consisted 14 subjects ( 5 male) with $\mathrm{CDR}=0$, with mean age of 74.9 years. The demented olderadult group consisted of 13 participants ( 6 male), with a mean age of 77.2 years; 8 of them had $\mathrm{CDR}=0.5$ and 5 had $\mathrm{CDR}=1$. Functional-MR images were acquired with an asymmetric spinecho sequence sensitive to BOLD contrast ( $\mathrm{TR}=2.68 \mathrm{sec}, \mathrm{T} 2^{*}$ evolution time $=50 \mathrm{msec}$ ). Image resolution was $3.75 \times 3.75 \times 8 \mathrm{~mm}^{3}$. These data are publicly available from the National fMR Data Center (http://www.fmridc.org), with access number 2-2000-1118w.

There were two trial conditions in this experiment. In condition 1, a 1.5 -second duration visual stimulus was presented. The visual stimulus was an $8-\mathrm{Hz}$ counter-phase flickering checkerboard. Each subject was instructed to press a key with his/her right index finger at stimulus onset. In condition 2, a pair of visual stimuli with interval 5.36 seconds were presented. Each subject underwent 4 runs of 15 trials; 8 image volumes were collected during each trial. Conditions 1 and 2 were pseudo-randomly intermixed; in each run, eight of the trials were of one condition, and the other seven were of the other condition.

We used SPM2 to detect activated voxels for condition 1 (the isolated visual stimulus). We applied a $p$-value threshold of 0.005 to the $t$-map, with a multiple-comparison correction based on Gaussian random-field theory (Worsley et al. (1992)). We chose this $p$-value to control the false-positive rate; although it resulted in low statistical power, we can be confident in activation foci that survive this threshold.

As expected, all three groups showed activation in motor cortex on the left, and in visual cortex. We applied fGAMMA to detect activation-map differences among (I) young vs. nondemented older, (II) young vs. demented older, and (III) nondemented older vs. demented older subjects. In these three analyses, $F=2$ indicated young, young, and nondemented-older groups, respectively. The aggregated label fields, and model frequencies are shown in Figure 12, and Figure 13.

The CPTs for $F$ are shown in Table 1. Each row in a CPT, denoted by $\theta_{i j}$, represents a conditional distribution of $F$ given a parent state. We introduce a measure $f_{\mathrm{RV}}$ to describe the relative frequency of the occurrence of a parent state. Combining the CPT for $F$ and $f_{\mathrm{RV}}$, we can determine the strongest co-occurrence patterns of $\mathbf{R V}$ and $F$, and use them to understand the underlying cognitive processes. In this manner, in Table 1, for study I, we can infer that $F$ has a probabilistic AND type association with $R V_{1}$ and $R V_{2}$. A dominant co-occurrence pattern was $\left[R V_{1}=0, R V_{2}=0, F=1\right]$, which means if there is no activation in $R V_{1}$ or $R V_{2}$, that subject will have a high probability ( 0.94 ) of being a nondemented-older subject. We observed this pattern with frequency $P\left(R V_{1}=0, R V_{2}=0, F=1\right)=P\left(F=1 \mid R V_{1}=0, R V_{2}=\right.$ $0) P\left(R V_{1}=0, R V_{2}=0\right)=0.94 \times 0.50=0.47$. In study II, the association among $R V_{1}$ and $F$ was linear. If $R V_{1}$ was activated, we could predict this subject was a young adult with high probability ( 0.88 ). For study III, the association among $\mathrm{RV}_{1}, \mathrm{RV}_{2}, \mathrm{RV}_{3}$, and F was complicated. The strongest co-occurrence pattern was $\left[R V_{1}=0, R V_{2}=0, R V_{3}=0, F=1\right]$, suggesting that the demented older group had less activation. Other strong co-occurrence patterns were [ $R V_{1}$ $=1, R V_{2}=0, R V_{3}=0, F=2]$ and $\left[R V_{1}=0, R V_{2}=1, R V_{3}=1, F=2\right]$; these two co-occurrence patterns characterized the non-demented older group; that is, the non-demented older group tended to have activation in $R V_{1}$ only, or in $R V_{2}$ and $R V_{3}$.

The label fields for analyses I and II clearly show reduced spatial extents of activation for nondemented and demented older subjects, compared to young subjects; these results are

consistent with those reported in the original analysis of these data (Buckner et al. (2000)). The regions manifesting group differences are primarily in the visual areas. The results of study II are more stable than those of study I: $I_{B}$ for study II contained 5 BN patterns, whereas $I_{B}$ for study I contained 14 patterns, and the frequency of the mode was lower in study I than in study II. In addition, the label field from study II was more spatially compact than that from study II, suggesting that the demented older/young difference was greater than the nondemented older/young difference. The label field from study III was noisy; the noise in the label field results from noise in the activations of both the nondemented older and demented older subjects. As expected, fGAMMA's ability to detect a valid pattern characterizing group differences decreased with increasing noise.

We could not detect a difference among groups for motor-area activation in studies I and II. Similarly, D'Esposito et al. reported that the hemodynamic-response amplitudes of voxels in activated motor areas were similar for young and old adults (D'Esposito et al. (1999)). Buckner et al. reported similar response amplitudes of voxels in activated motor areas across young, nondemented older, and demented older subjects (Buckner et al. (2000)). Our findings are consistent with those previously reported in the literature, and suggest that there is no difference in the spatial extents of motor-area activation between young and old adults.

Figure 13 demonstrates that model aggregation leads to greater stability of models generated by fGAMMA. In studies II and III, $\mathcal{B}^{\text {all }}$ is different from $\mathcal{B}^{\text {mode }}$.

# 4 Discussion and Conclusions 

We have described a method for group analysis of fMR data; our approach uses a Bayesiannetwork representation to identify linear or nonlinear multivariate probabilistic associations among groups of activated voxels and a clinical variable $F$. In addition, fGAMMA incorporates data resampling to select a model that is robust under data perturbation.
fGAMMA and GLM-based approaches, such as random-effects analysis, attempt to detect activation-pattern differences among experimental groups. Both approaches share the same general two-stage analytic framework: within-subject analysis to detect individual activation, followed by between-subject analysis to detect group differences. The major differences between fGAMMA and GLM-based approaches are threefold. First, fGAMMA treats group membership as a categorical variable and generates a model to represent associations among regions and that variable; regions critical to detecting group differences constitute the Markov blanket of the group variable in the Bayesian network generated by fGAMMA. In contrast, GLM-based approaches directly compare the voxel-wise activation differences across groups. Second, fGAMMA is a multivariate nonparametric method, whereas GLM-based approaches, as typically applied to fMR analysis, are mass-univariate and assume normality. Third, fGAMMA adopts a model-selection approach to find an optimal model of the fMR data, as measured by maximization of a fitness function. In contrast, GLM-based approaches compute voxelwise parametric statistics, with multiple-comparison correction.

Empirically, GLM-based approaches cannot handle the case of functional degeneracy, or complex nonlinear associations among regions and the group-membership variable, whereas fGAMMA was designed to handle these scenarios. The simulated functional-degeneracy study in Section 3.1 clearly demonstrates this difference. Our method focuses on the detection of associations among voxels (or voxel groups) and $F$, whereas most mass-univariate methods, such as random-effects analysis, are formulated to detect region-specific effects.

Various types of structure-function associations can also be detected by other group-analysis methods. For example, linear structure-function associations among regions and $F$ can be

revealed by a $t$-test, and the AND relationship can be obtained using a conjunction analysis with conjunction null (Nichols et al. (2005)).

There exist many multivariate methods for group analysis, such as (Coulon et al. (2000); Calhoun et al. (2001); Svensen et al. (2002); Esposito et al. (2005)). These methods have different strengths and assumptions. For example, independent component analysis for group inference, proposed in Calhoun et al. (2001), reveals spatiotemporal modes of signal variability. This method imposes a common space of observations for all sources, although the activation time courses of different subjects may differ. We plan to apply these multivariate methods to a test data set that contains interesting structure-function associations, such as functional degeneracy, and compare them with fGAMMA.

We assume that the activation pattern associated with the underlying neural process is consistent across subjects, and dominates the data. Although lack of statistical power or noise could affect CPT values, the number of representative voxels, and the spatial shape and extent of ROIs, the types of structure-function associations detected tend not to change because of BN's ability to encode uncertainty. Equation (3) may help distinguish results due to high noise or small sample size from inherently high variability. We plan to extend our work towards comprehensive evaluation of fGAMMA, including noise level, the choice of threshold, and the number of subjects, among other parameters.

In constructing a Bayesian network to model associations among regions and $F$, fGAMMA detects regions that, when considered together, are strongly associated with group differences. In this respect, our Bayesian-network approach is fundamentally different from classification methods, such as support vector machines (Cox and Savoy (2003); Mitchell et al. (2004); Zhang et al. (2005)). fGAMMA does not maximize a metric of classification accuracy; rather, fGAMMA maximizes modeling of the joint probability distribution that characterize structurefunction associations in the fMR data. To extend fGAMMA to support classification, we are developing a classification algorithm that uses voxels in a label field as features.

Our simulations demonstrated that fGAMMA can identify nonlinear multivariate associations among voxels and $F$. The results of our analysis of studies involving young, nondemented older, and demented older subjects are consistent with those reported in the literature, demonstrating the validity of our approach. However, we plan additional validation experiments with simulated and with previously analyzed data.

Our current implementation requires binary voxel and clinical variables, which may lead to loss of information. In the fMR study of young, nonde-mented, and demented older adults, we found our results were consistent with those found by applying standard statistical methods to the same data without discretization. These results suggest that discretization, as applied in fGAMMA, does not cause severe loss of information.
fGAMMA currently can analyze only one clinical or group-membership variable. We plan to extend fGAMMA to handle more than one clinical variable. We expect that after this extension of our work, fGAMMA will be able to show how several clinical variables, such as age and sex, as well as group membership, jointly modulate interactions among region activations.

One problem with fGAMMA is the computational cost of model aggregation, which requires running the model-generation algorithm many times. In a fMR study involving dozens of subjects with approximately $10^{6}$ voxels, with spatial resolution $3 \times 3 \times 3 \mathrm{~mm}^{3}$, we can obtain results in several hours using a readily available desktop workstation. In a study involving more subjects and voxels, a parallel version of fGAMMA may be required to produce results in a timely manner.

# Acknowledgements 

This work was supported by The Human Brain Project, National Institutes of Health grant R01 AG13743, which is funded by the National Institute of Aging, the National Institute of Mental Health, and the National Cancer Institute.

# Appendix 

We describe the procedure of belief-map generation in this section. The goal of belief-map generation is to infer the equivalence set $\mathbf{E}$ based on the similarity map $\mathbf{S}$.

Provided that the number of clusters $c$ is known, the prior for $\mathbf{L}$ is a MRF such that

$$
P(\mathbf{L})=\frac{1}{Z} e^{-\sum_{i} \sum_{j ; j \text { (odds })} \beta\left(\mu(i)-\mu(j i)^{2}\right.}
$$

where $\mu(i)$ denotes the centroid of the cluster to which voxel $i$ belongs, and $\beta$ is a parameter controlling global smoothness. Let $\mathrm{T}=\left\{\mu_{1} ; \mu_{2}, \ldots, \mu_{c}\right\}$ where $\mu_{i}$ is the centroid of cluster $i$. T and $\beta$ are the hyperparameters of $\mathbf{L}$. In this MRF model, if $L_{i}$ and $L_{j}$ are in clusters $a$ and $b$, respectively, and the centroids of clusters $a$ and $b$ are close to each other, the probability of observing this pattern is greater than that in the case in which the centroids of clusters $a$ and $b$ are far from each other.

The goal is to find $\hat{\mathbf{L}}$ and $\hat{\mathrm{T}}$ such that

$$
[\overline{\mathbf{L}}, \overline{\mathrm{Y}}]=\underset{\mathbf{L}, \mathrm{Y}}{\operatorname{argmax}} P(\mathbf{L}, \mathrm{Y} \mid \mathbf{S})
$$

$\mathbf{L}$ and $\overline{\mathrm{Y}}$ are the MAP estimation of $\mathbf{L}$ and T , given $\mathbf{S}$. We use a generalized expectationmaximization (EM) method to solve this problem. The generalized EM algorithm iteratively searches for $\mathbf{L}$ and T. In iteration $k$, the algorithm first searches for $\mathbf{L}(k)$ such that $\mathbf{L}(k)=$ $\operatorname{argmax}_{\mathbf{L}} P(\mathbf{L} \mid \mathbf{S}, \overline{\mathrm{Y}}(k-1))$, and then finds $\overline{\mathrm{Y}}(k)$ that maximizes $P(\mathrm{~T} \mid \mathbf{S}, \mathbf{L}(k))$. Finding $\overline{\mathrm{Y}}$ $(k)$ is straightforward: given $\mathbf{L}(k)$, for all voxels in cluster $i$, the empirical mean of their intensities in the similarity map is the estimator of $\mu_{i}$. The key issue is how to compute $\mathbf{L}(k)$.

From Bayes' theorem, $P(\mathbf{L} \mid \mathbf{S}, \mathrm{T}) \propto P(\mathbf{S} \mid \mathbf{L}, \mathrm{T}) P(\mathbf{L} \mid \mathrm{T})$. Assume that

$$
P(\mathbf{S} \mid \mathbf{L}, \mathrm{Y}) \propto e^{-\sum_{i} U\left(L_{i}, S_{i}\right)}
$$

where $U\left(L_{i}, S_{i}\right)$ is a function that describes the relationship between the similarity map and the label field. For this purpose, we use $U\left(L_{i}, S_{i}\right)=\left(S_{i}-\mu(i)\right)^{2}$; thus, we assume that $S_{i}=\mu(i)+$ $N_{i}$, where $N_{i}$ represents independently and identically distributed Gaussian white noise. Let $\psi\left(L_{i}, L_{j}\right)=e^{-\beta(\mu(i)-\mu(j))^{2}}$ and $\varphi\left(L_{i}, S_{i}\right)=e^{-\left(S_{i}-\mu(i)\right)^{2}}$. From Bayes' theorem and Equations (10) and (12), we have

$$
P(\mathbf{L} \mid \mathbf{S}, \mathrm{Y})=\frac{1}{Z} \prod_{i, j} \psi\left(L_{i}, L_{j}\right) \prod_{i} \phi\left(L_{i}, S_{i}\right)
$$

where $Z$ is a normalization constant. Therefore, the goal is to find the MAP estimate of $\mathbf{L}$ based on equation (13). That is,

$$
\overline{\mathbf{L}}=\underset{\mathbf{L}}{\operatorname{argmax}} \prod_{i, j} \psi\left(L_{i}, L_{j}\right) \prod_{i} \phi\left(L_{i}, S_{i}\right)
$$

To solve this optimization problem, we use loopy belief propagation (LBP). The LBP algorithm works in an iterative fashion. On each iteration, the message $m_{i j}\left(L_{j}\right)$ contains the information that is propagated from node $i$ to node $j$ regarding relative likelihoods for particular states that $j$ might assume. If $L_{i}$ has $r$ states, then $m_{i j}\left(L_{j}\right)$ is a vector of length $r$. On each iteration, each node $L_{i}$ sends a message $m_{i j}\left(L_{j}\right)$ to nodes in its Markov blanket $m b\left(L_{i}\right)$. The updating rule for $m_{i j}\left(L_{j}\right)$ is as follows:

$$
m_{i j}\left(L_{j}\right) \leftarrow \sum_{L_{i}} \phi\left(L_{i}, S_{i}\right) \psi\left(L_{i}, L_{j}\right) \prod_{k \in m b(i) \mid j} m_{k i}\left(L_{i}\right)
$$

The belief for node $i$ is a vector of length $r$; it represents the marginal probability distribution for this node, and is determined by the product of the evidence term $\varphi\left(L_{i}, S_{i}\right)$ and the messages coming into node $i$ :

$$
b\left(L_{i}\right)=\frac{1}{Z_{i}} \phi\left(L_{i}, S_{i}\right) \prod_{j \in m b(i)} m_{j i}\left(L_{i}\right)
$$

where $Z_{i}$ is a normalization constant. LBP updates $m_{i j}$ and $b\left(L_{i}\right)$, based on equations (15) and (16). On each iteration, each node computes the messages for all nodes in its Markov blanket. Once all messages are calculated, the messages are delivered to their recipient nodes; these messages are then used to update the messages and beliefs on the next iteration. If $\left|b_{k}\left(L_{i}\right)-\right.$ $\left.b_{k-1}\left(L_{i}\right)\right| \approx 0$ for any $i$, then LBP converges, and the hidden label of $L_{i}$ is set to be the mode of belief vector $b\left(L_{i}\right)$.

The number of clusters is estimated based on GVRC metric (Chen and Herskovits (2005a)). Based on the experimental results in (Chen and Herskovits (2005a)), belief-map generation is not very sensitive to the global smoothness parameter $\beta$.

![img-0.jpeg](img-0.jpeg)

Figure 1.
An illustration of functional segregation, degeneracy, and integration. Each gray rectangle represents a task, the rectangle contains brain regions (white ellipses) required to complete that task.

![img-1.jpeg](img-1.jpeg)

Figure 2.
An overview of the analysis procedure

![img-2.jpeg](img-2.jpeg)

Figure 3.
An example of a fMR study. Left: brain regions involved. Right: a Bayesian network that represents probabilistic associations among regions $A$ and $B$, and the clinical variable $F$.

![img-3.jpeg](img-3.jpeg)

Figure 4.
A Bayesian network with inverse-tree structure

![img-4.jpeg](img-4.jpeg)

Figure 5.
A hypothetical demonstration of how fGAMMA is designed to generate a Bayesian network characterizing group differences; note that Markov blankets in inverse-tree models are subsets of those in unrestricted Bayesian networks.

![img-5.jpeg](img-5.jpeg)

Figure 6.
A second-order neighborhood system in a 3D lattice. The yellow and red voxels are the neighbors of the black voxel. The red voxels constitute the Markov blanket of the black voxel.

![img-6.jpeg](img-6.jpeg)

Figure 7.
The summation of activation maps for all subjects and the label field $\Lambda^{\text {mode }}$ for the simulated data. The summation map shows the probability of voxel activation in the activation maps. (a) summation map in region A; slice numbers from left to right are $14,16,18,20$, respectively. (b) cluster 1 (purple) in $\Lambda^{\text {mode }}$. (c) summation map in region B; slice numbers from left to right are $35,37,39,41$, respectively. (d) cluster 2 (yellow) and 3 (white) in $\Lambda^{\text {mode }}$.

![img-7.jpeg](img-7.jpeg)

Figure 8.
Representative voxels and $F$ for the simulated-data experiment. For representative voxels, black is 0 (not activated) and white is 1 (activated). For $F$, black is 1 (control) and white is 2 (exposed to stimulus).

![img-8.jpeg](img-8.jpeg)

Figure 9.
Model-frequency histogram for the simulated-data experiment.

![img-9.jpeg](img-9.jpeg)

Figure 10.
Class maps for the simulated-data experiment. (a) $C_{1}$, slice 16; (b) $C_{1}$, slice 20; (c) $C_{2}$, slice 37; (c) $C_{2}$, slice 39; (e) $C_{3}$, slice 39; (f) $C_{3}$, slice 41.

![img-10.jpeg](img-10.jpeg)

Figure 11.
The $t$-map for comparing voxel-activations across groups for the simulated data. Brighter color represents higher t-statistic value.(a) $t$-map in region A; slice numbers from left to right are 14, $16,18,20$, respectively. (b) $t$-map in region B; slice numbers from left to right are $35,37,39$, 41 , respectively.

![img-11.jpeg](img-11.jpeg)

Figure 12.
Aggregated label fields are overlaid on transverse sections for each study. The aggregated label fields are superimposed on the average anatomic image in the MNI coordinate system. For (a) and (b), the anatomic image is from a young subject. For (c), it is from a nondemented older subject. (a) Study I: young vs. nondemented older; cluster $1\left(R V_{1}\right)$ is red; cluster $2\left(R V_{2}\right)$ is white. (b) Study II: young vs. demented older; cluster $1\left(R V_{1}\right)$ is white. (c) Study III: nondemented older vs. demented older; cluster $1\left(R V_{1}\right)$ is purple; cluster $2\left(R V_{2}\right)$ is yellow; cluster $3\left(R V_{3}\right)$ is white.

![img-12.jpeg](img-12.jpeg)

Figure 13.
Model-frequency histograms for experiment 2. From left to right: young vs. nondemented older; young vs. demented older; nondemented older vs. demented older.

Table 1 Conditional probability tables for $F$, and parent-state frequencies $\left(f_{\mathrm{RV}}\right)$. Top: young vs. nondemented older; middle: young vs. demented older; bottom: nondemented older vs. demented older. Values in brackets are posterior variance to characterize uncertainty in estimation.


# Algorithm 1 <br> Model aggregation in fGAMMA 

```
1: Remove the \(l^{\text {th }}\) samole from D to generate \(\mathbf{D}^{l}(1 \leq i \leq M)\);
2: Generate a model \(\mathcal{M}^{1}=i \mathcal{B}^{1}, \Lambda^{1}\) ) for each \(\mathbf{D}^{1}\);
3: Calculate the frequency \(f_{\mathcal{B}}\) of model \(\mathcal{M}^{1}\) based on \(\left\{\mathcal{B}^{1}\right\}\);
4: Select the mode \(\mathcal{B}^{\text {mode }}\) of \(\mathcal{B}\);
5: for each class \(j\) in \(\mathcal{B}^{\text {mode }}\) do
6: Calculate the class map \(C_{j}\) based on \(\left\{\Lambda^{k} \mid \mathcal{B}^{k}=\mathcal{B}^{\text {mode }}\right\}\);
7: Threshold \(C_{j}\) to get a binary class map;
8: end for
```