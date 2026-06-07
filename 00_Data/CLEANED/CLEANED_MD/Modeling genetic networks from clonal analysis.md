# Modeling Genetic Networks from Clonal Analysis 

Radhakrishnan Nagarajan<br>Center on Aging, University of Arkansas for Medical Sciences<br>Address: Center on Aging, UAMS<br>629 Jack Stephens Drive, Room: 3105<br>Little Rock, AR 72205, USA<br>email: nagarajanradhakrish@uams.edu<br>Jane E. Aubin<br>Department of Medical Genetics and Microbiology<br>University of Toronto<br>Room 6230 Medical Sciences Building<br>1 King's College Circle<br>Toronto, Ontario M5S 1A8, Canada<br>email: jane.aubin@utoronto.ca<br>Charlotte A. Peterson<br>Center on Aging, University of Arkansas for Medical Sciences<br>Central Arkansas Veterans Health Care System<br>Address: Center on Aging, UAMS<br>629 Jack Stephens Drive, Room: 3121<br>Little Rock, AR 72205, USA<br>email: petersoncharlottea@uams.edu

Corresponding Author:
Radhakrishnan Nagarajan
Center on Aging
University of Arkansas for Medical Sciences
629 Jack Stephens Drive, Room: 3105
Little Rock, AR 72205, USA
Phone: (501) 526-7461
Fax: (501) 526-5830
email: nagarajanradhakrish@uams.edu

#### Abstract

In this report a systematic approach is used to determine the approximate genetic network and robust dependencies underlying differentiation. The data considered is in the form of a binary matrix and represent the expression of the nine genes across the ninety-nine colonies. The report is divided into two parts: the first part identifies significant pair-wise dependencies from the given binary matrix using linear correlation and mutual information. A new method is proposed to determine statistically significant dependencies estimated using the mutual information measure. In the second, a Bayesian approach is used to obtain an approximate description (equivalence class) of network structures. The robustness of linear correlation, mutual information and the equivalence class of networks is investigated with perturbation and decreasing colony number. Perturbation of the data was achieved by generating bootstrap realizations. The results are refined with biological knowledge. It was found that certain dependencies in the network are immune to perturbation and decreasing colony number and may represent robust features, inherent in the differentiation program of osteoblast progenitor cells. The methods to be discussed are generic in nature and not restricted to the experimental paradigm addressed in this study.


Keywords: Linear Correlation, Mutual Information, Bayesian Networks, Clonal Analysis, Osteoblast differentiation.

# 1. Introduction 

Biological processes such as cell differentiation are mediated by specific networks of genes, which interact with one another. Such systems evolved with time and can be aptly characterized as coupled nonlinear dynamical systems. Dynamical systems can be broadly classified into linear and nonlinear systems. While the former can exhibit interesting behavior only in the presence of noise, the latter can give rise to a wide range of behavior even in the absence of noise. Current techniques used in modeling genetic networks rely on the concepts of biochemical networks (Goldbeter, 1996; Jacob and Monod, 1961; Kauffman, 1969; Tyson et al, 2001; Yagil and Yagil, 1971). The interaction between genes is often modeled as the outcome of a deterministic sequence of events (Gardner et al, 2000; Huang and Ferrell, 1996). However, recent reports have indicated that, in spite of the deterministic phenotypic outcome, the underlying dynamics may be noisy (Hasty et al, 2000; McAdams and Arkin, 1997; McAdams and Arkin, 1999). Noise can be categorized broadly into either dynamical or measurement noise. While the former is coupled to the dynamics, the latter occurs externally (Fig. 1). Various factors that contribute to dynamical noise include: fluctuations in protein concentrations, variation in cell-to-cell switching time and micro-environment. The phenotypic outcome is deterministic in the average sense and has been attributed to population transcriptional cooperation, checkpoints, and redundancies in genes and regulatory pathways, (McAdams and Arkin, 1999). In a recent study, it was demonstrated how noise can be used to control switching and regulation of gene expression (Hasty et al., 2000). On the other hand, a purely nonlinear deterministic approach has been used to model gene interactions (Gardner et al., 2000). The gene expression values are determined with a

measurement device, which acts as a black box between the true biological activity and the output (Fig. 1). Thus, what is externally observed is the output of the measurement device and not the true biological phenomena. It might not be surprising to note that the input and output of the measurement device may be nonlinearly related, corrupted with measurement noise. Thus the choice of the mathematical technique in explaining the observed phenomenon is an open question. Given the above complexities, a pragmatic approach would be to use a combination of linear and nonlinear measures (see Sec. 2).

There have been a number of reports on modeling genetic networks as Boolean networks (Glass and Hill, 1998; Kauffman, 1993), where each gene can be either in an ON or an OFF state. The switching of a gene is commonly represented by a sigmoidal curve, whose steepness depends on the extent of transcriptional cooperativity (Goldbeter and Dupont, 1990; Huang and Ferrel, 1996). Temporal expression profile studies have also been used successfully in determining the network structure from such binary representations (Liang et al., 1998; Shmulevich et al., 2002). However, in the present report we address the problem of determining the network structure from gene expression patterns across replicate cell colonies, by observing a snap shot of the biological process represented by a binary matrix, i.e. each gene is either ON or OFF in the given time window across the replicate colonies.

# Clonal Analysis of Osteoblast Progenitor Cells 

The formation of a particular differentiated phenotype from a stem cell/progenitor is believed to follow a hierarchical sequence of events. Recent studies (Aubin and Triffit,

2001; Liu et al, 2003; Madras et al., 2002) have indicated that the osteoblast developmental program may be heterogeneous and probabilistic in nature. Madras et al., investigated the expression of nine osteoblast-associated genes in a window of observation. The genes consisted of: COLL (collagen I), ALP (alkaline phospotase), BSP (bone sialoprotein), OCN (osteocalcin), FGFR1 (fibroblast-growth factor receptor 1), PDGFR $\alpha$ ? (platelet-derived growth factor receptor $\alpha$ ), PTH1R (parathyroid hormone/parathyroid hormone related protein receptor), PTHrP (parathyroid hormone related protein) OPN (osteopontin) across ninety-nine colonies cultured under identical conditions. These genes are asynchronously expressed during the course of osteoblast differentiation, however, there are some discrepancies in the literature regarding their sequence of expression during the osteoblast development [Madras et al., 2002]. The colony forming units osteoblasts (CFU-Os) were plated from rat-calvariae cells (21 day Wistar rat fetuses). While some genes are constitutively expressed (i.e. ON), others occur with a finite probability in a given colony (i.e. ON or OFF), (Aubin, 1998; Aubin et al., 1999; Madras et al., 2002). The ON/OFF of a gene was determined by quantifying the signal over background from digitized images of Southern blots by Phosphorimager. The normalized values represent the ratio of gene A's signal over total cDNA (used as housekeeping gene control in global amplification) signal for each gene in each sample, thereby generating the binary matrix, considered in this study. While there are technical issues with quantifying densitometry signals, these were controlled rigorously. In the analysis, any normalized signal of any magnitude with a specific gene probe that was over background was considered "ON". A statistical approach was subsequently used to determine pair-wise dependence and the temporal sequence of expression of the nine

genes obtained across the ninety-nine colonies. The authors concluded that the probabilistic nature of gene expression could result in multiple pathways giving rise to the same phenotypic outcome. Determining dependencies and causal relationships between the ge nes from a snap shot of the biological process can be quite challenging. In this report, a systematic approach different from that discussed in (Madras et al, 2002) is used to infer the dependencies between the genes and the approximate network structure. The techniques are generic in nature and hence not restricted to the osteoblast differentiation data.

The report is organized as follows: in Section 2, the properties of entropy, linear correlation and mutual information are discussed. Entropy is a measure of uncertainty associated with expression of a gene, whereas correlation and mutual information measure the dependency between pairs of genes. The Fisher's exact test which is widely used in categorical data analysis is also used to capture non-random association between the genes. While the statistical significance of linear correlation and Fisher's exact test is well defined, that of mutual information is unclear. A resampling approach is proposed in Section 2, and used subsequently to determine statistically significant dependencies from mutual information estimates. In Section 3, the effect of perturbations and decreasing colony number on the entropy, linear correlation, Fisher's exact test and the mutual information estimates is investigated. Perturbations of the data were generated by bootstrap realizations. In Section 4, a Bayesian approach is used as a tool to determine the approximate network structure. Constraint-based and search algorithms are used to determine the equivalent class of networks. A brief summary of the results including

pruning the network structure with biological knowledge and possible extensions is included under Section 5.

# 2. Pair-wise Dependencies and their Statistical Significance 

### 2.1 Pair-wise dependencies - Linear Correlation, Mutual Information and Fisher's Exact

test

The two measures commonly used to determine the dependencies between any two random variables $(x$ and $y)$ are the correlation $\left(\rho_{x y}\right)$ and the mutual information $\left(I_{x y}\right)$, given by

$$
\rho_{x y}=\frac{1}{N-1} \sum_{i=1}^{N} \frac{\left(x-\mu_{x}\right)\left(y-\mu_{y}\right)}{\sigma_{x} \sigma_{y}} \text { where }\left|\rho_{x y}\right| \leq 1, \rho_{x y}=\rho_{y x}
$$

The self-information (entropy) is given by $H(x)=-\sum_{x} p_{x} \log _{2} p_{x}$ Shannon (1948).

$$
I_{x y}=\sum_{x, y} p_{x y} \log \left(\frac{p_{x y}}{p_{x} p_{y}}\right)=H(x)+H(y)-H(x, y) \text { where } I_{x y} \geq 0, I_{x y}=I_{y x}
$$

While $\rho_{x y}$ is a measure of linear dependence, $I_{x y}$ measures the generalized dependence and has been used in inferring genetic networks (Liang et al., 1998) and nonlinear studies (Fraser and Swinney, 1986). From equations (1) and (2), the measures $I_{x y}, \rho_{x y}$ are symmetric and hence fail to indicate the direction of dependence. Pair-wise dependencies of a network composed of several genes, can be represented as a symmetric matrix. The diagonal elements of the correlation matrix, represents the auto-correlation $\rho_{x x}$ and is unity, whereas those of the mutual information matrix $I_{x x}$, represents the self-information

or the entropy of the gene. The entropy of a gene across the independent cell colonies is a measure of the uncertainty in its expression. In the present experimental paradigm, the gene OPN was expressed in all the colonies and hence had an entropy zero. The mutual information $I_{x y}$ is a measure of the reduction in uncertainty of $x$ having observed $y$. For deterministic $y$ (ex: OPN) one fails to observe any reduction in uncertainty of $x$ i.e. $H(y)$ $=0$ implies $H(x, y)=H(y)$, resulting in $I_{x y}=0$ and $\rho_{x y}=0$. Hence we shall leave OPN out from subsequent discussions. An analytical relation relates $I_{x y}$ and $\rho_{x y}$ for normally distributed processes, given by $I_{x y}=-0.5 \log \left(1-\rho_{x y}^{2}\right)$. The Fisher's exact test is ideal for determining non-random associations between categorical variables and has been used successfully by (Madras et al., 2002) to capture statistically significant dependencies between the genes.

# 2.2 Significance of the pair-wise dependencies 

### 2.2.1 Resampling Techniques

Resampling methods have been used as effective tools to assess statistical significance (Efron et al., 1994). In traditional tests, the statistical measure obtained on a sample, drawn from a given population, is compared to a theoretical distribution to assess its significance. However in resampling statistics, one generates an empirical distribution by computing the statistical measure on samples generated from the same empirical sample, hence the term resampling. Unlike traditional approaches, resampling implicitly assumes the given empirical sample to be a representative of the population, which is considered a drawback of this technique. While resampling without replacement is suited for correlated data (Schreiber, 1996), resampling with replacement is ideal for uncorrelated

data. In the present study each colony is independent of the other and hence the choice of resampling with replacement (bootstrap) is justified. In a recent study, bootstrap realizations have been identified with perturbing the given data (Friedman et al., 2002).

# 2.2.2 Statistical significance of the measures 

The p-value of the linear correlation and Fisher's exact test can be estimated from parametric distributions, however this is not the case for mutual information. An ad-hoc approach would be to choose a fixed threshold $(\theta)$ and assume all pair-wise dependencies whose mutual information is greater than $(\theta)$ to be significant. In a recent report, Butte and Kohane (2000) showed that the choice of the threshold $(\theta)$ could significantly alter the network architecture. Therefore, it is important to develop a statistically rigorous approach to avoid spurious conclusions. In this report we propose a method to determine statistically significant mutual information $I_{s y}$ estimates between a pair of genes ( $x$ and $y$ ). A step-wise procedure is described below:

- Randomly choose $k$ colonies with replacement (bootstrap sample) and pair of genes $(x, y)$. The null hypothesis addressed here is that the expression of $(x, y)$ across the $k$ colonies is uncorrelated.
- Determine the mutual information between this pair $I_{s y}$.
- Randomly shuffle the ON/OFF states for these genes across the $k$ colonies. These shall be referred to as a surrogate. Compute the mutual information between the shuffled pair $I_{s, y}^{\text {shuff }}$. Generate 19 such surrogates. This corresponds to $\alpha=1 /(19+1)=0.05$ (Hope, 1968; Theiler and Prichard, 1995).

- The $p$-value is given by

$$
p=\frac{\left[\text { number of cases where } I_{x y}<I_{x, y}^{\text {shuff }}+1\right]}{20}
$$

The numerator has a minimum value of one, which corresponds to the original pair.

- If $I_{x y}>I_{x, y}^{\text {shuff }}$ for each of the 19 surrogates then the null is rejected at $\alpha=0.05$.
- Repeat the above procedure for $N_{B}$ times. The power of the test is the fraction of the number of successful rejections of the null divided by $N_{B}$.

It should be noted that the random-shuffled surrogates retain the self-information, $H(x)$ and $H(y)$ of the genes, whereas the joint-entropy $H(x, y)$ is destroyed; such surrogates have been classified under a special class called constrained randomized surrogates (Theiler and Prichard, 1995; Schreiber and Schmitz, 1996). Constrained realizations as opposed to typical realizations retain certain statistical features of the original data, imposed as constraints. The constraint here is on retaining the self-information. In the above algorithm, we determined the p-value corresponding to significance level $\alpha$. This represents the Type I error, which is the odds of falsely rejecting a given null hypothesis, i.e. concluding two genes are pair-wise dependent, when they are not. The power of the statistical test is related to the Type II error $(\beta)$ as $(1-\beta)$ and represents rejecting the null when it is false. The power is determined by generating several independent bootstrap realizations, shown in the last step.

# 2.2.3 Comment on Bonferroni correction: 

The Bonferroni correction has been used extensively in gene expression analyses (Wayne and McIntyre, 2002). However, there are some subtle details associated with the Bonferroni correction (Perneger, 1998), which brings up the question of whether it is appropriate for the analysis of gene expression data. The objective is to obtain an adjusted value $\left(\alpha^{*}=\alpha / n\right)$ of the Type I error, for each of the $n$ individual tests so as to maintain an experiment-wise error rate of $\alpha$. The null hypothesis addressed by the Bonferroni test is that the two groups of $n$ tests are not statistically different. In the present study, we have $n=8$ genes in the network (excluding OPN, see Sec. 1), resulting in 28 pairs. A $p$-value lesser than $\alpha^{*}=0.05 / 28=0.0018$, obtained on any one of the pairs, rejects the null that all the 28 pairs are independent. It is important to evaluate the usefulness of the result in the present context. The phenotypic outcome in a given experimental paradigm is mediated by specific signaling pathways with interacting components and are therefore likely to be dependent. Thus, rejecting the null that the components are independent of one another seems to be of little use. The expression for the Bonferroni correction is obtained under the assumption that the pair-wise correlations are independent of one another, which is not true in general. This can lead to spurious conclusions, more importantly an increase in the Type II error and a reduction in statistical power. The impact of the Bonferroni correction in determining the dependencies with the correlation measure shall be discussed in the following section.

Summary (Sec. 2): The choice of resampling approach as opposed to ad-hoc thresholding can be used to determine statistically significant pair-wise dependencies estimated by the mutual information measure.

# 3. Effect of number of colonies on pair-wise dependencies and entropy 

### 3.1 Self-information (entropy) of the genes

The entropy of a gene is a measure of the uncertainty or randomness associated with its expression. If there were only a single pathway to explain a given phenotypic outcome, then one would observe the same set of genes to be constitutively activated in each colony. However, the present experimental paradigm failed to exhibit such a behavior other than for OPN. The value of the entropy of binary sequence in $\log _{2}$ scale is bounded by $[0,1]$. A value of zero is indicative of determinism, whereas a value of one is indicative of maximum randomness. The former can occur when a particular gene is constitutively ON or OFF across all the colonies; the latter is observed when the odds of a gene being present or absent in a given colony is half. Entropy of the eight genes, estimated by using 100 bootstrap realizations for sample size of 99,66 , and 33 colonies, is shown in Figure 2. The ranked entropy profile of the genes [ALP, BSP, OCN, COLL, PDGFR $\alpha$, FGFR1, PTHrP, PTH1R] remained unchanged with perturbation and reduction in number of colonies.

Summary (Sec. 3.1): Non-zero entropy of genes across replicate colonies indicates possible non-determinisitic nature of gene expression across the colonies. Thus it might be possible to achieve the end phenotype through multiple gene activation programs. The

ranked entropy profile of the genes is robust to bootstrapping (perturbation of the data) and decreasing number of colonies.

While entropy is a useful measure of self-information of a gene, it does not provide insight into the dependencies between genes. Interestingly, we found the dependencies between the high-entropy genes to be robust to decreasing colony number and perturbations, discussed in the following section.

# 3.2 Estimating pair-wise dependencies using Linear Correlation 

Pair-wise dependencies were estimated by sampling 99, 66 and 33 colonies from the given 99 colonies (Madras et al., 2002). One hundred bootstrap realizations were generated from the given data ( 99 colonies) for each sample size: 99,66 and 33 . This was done to determine the robustness of certain dependencies with perturbation of the given data and decreasing colony number. The mean and the variance of the correlation ( $\rho$ ) estimated for these sample sizes ( 99,66 and 33 colonies) are shown in Figures 3b, 4b and 5 b , respectively. The correlation obtained on the random shuffled surrogates, (Sec. 2.2.2) representing the noise floor is also shown as a reference. The power $\left(N_{B}=100\right)$ estimated with Bonferroni correction $(\alpha=0.0018)$ and without Bonferroni correction $(\alpha$ $=0.05)$.

Without Bonferroni Correction: The pair-wise dependencies that came through the power analysis with (power $\sim 0.8$ ), Figure 6a, were (COLL-ALP), (COLL-OCN), (COLLFGFR1) (ALP-BSP), (ALP-OCN), (ALP-PTH1R), (BSP-OCN) and (OCN-PTH1R) by

resampling 99 and 66 colonies. However, resampling with 33 colonies retained only four of the above pairs (power $\sim 0.8$ ) namely: (COLL-ALP), (ALP-BSP), (ALP-OCN), and (BSP-OCN). The number of dependencies obtained for the various colony sizes ( $n_{c}=11$, 22, 33, 66 and 99) is enclosed under Table I. It should be noted that the number of dependencies $(\alpha=0.05$, power $\sim 0.8)$ vary considerably with varying colony size.

With Bonferroni Correction: The pair-wise dependencies that came through (power 0.8 ) by resampling 99 colonies were (COLL-ALP), (COLL-OCN), (ALP-BSP), (ALPOCN), (BSP-OCN) and (OCN-PTHIR. Those obtained by resampling 66 were (COLLALP), (ALP-BSP), (ALP-OCN), (BSP-OCN) and those obtained by resampling 33 colonies was (ALP-OCN). These results confirm our earlier remark on the effect of the Bonferroni correction in reducing statistical power, Table I. As observed by Madras et al. (2002) the genes $P D G F R \alpha$ and $P T H r P$ were independent of all the other genes and from one another. This is supported by the high p value and low power obtained for these pairs.

Summary (Sec. 3.2): The pair-wise dependencies estimated using linear correlation ( $\alpha=$ 0.05 , power $\sim 0.8$ ), that were robust to decreasing sample size ( $n_{c}=99,66$ and 33) and perturbation consisted of: (COLL-ALP), (ALP-BSP), (ALP-OCN), and (BSP-OCN)

# 3.3 Estimating pair-wise dependencies using Fisher's exact test 

The Fisher's exact test had been used recently (Madras et al., 2002) to determine statistically significant dependencies in the given experimental paradigm. As opposed to

linear correlation and mutual information, this test assumes that the given data lends itself into categories. Consider the binary expression of two genes $g_{1}$ and $g_{2}$ across n colonies. There are four possible occurrences namely $\left(g_{1}, g_{2}\right)=(00,01,10$ and 11). The number of occurrences of each of these combinations is represented by a $2 \times 2$ contingency table. The p-values are determined from hypergeometric distribution. Statistically significant genes $(\alpha=0.05)$ with (power $\sim 0.8$ ), Figure 6b, for varying colony sizes $\left(n_{c}=11,22,33\right.$, 66 and 99) is enclosed under Table I. The statistically genes with ( $\alpha=0.05$, power $\sim 0.8$ ) were similar to those obtained using linear correlation. As with linear correlation the number of statistically significant genes vary considerably with varying colony numbers. This implies that there might not be any added advantage in using linear correlation over Fisher's exact test.

Summary (Sec. 3.3): The pair-wise dependencies estimated using Fisher's exact test ( $\alpha=$ 0.05 , power $\sim 0.8$ ), that were robust to decreasing sample size ( $n_{c}=99,66$ and 33) and perturbation consisted of: (COLL-ALP), (ALP-BSP), (ALP-OCN), and (BSP-OCN)

# 3.4 Estimating pair-wise dependencies using Mutual Information 

The mean and the variance of the mutual information (Sec. 2.2.2) estimated from 100 bootstrap realizations with sample sizes: 99, 66 and 33 colonies are shown in Figures 3a, 4 a and 5 a , respectively. The noise floor is represented by value estimated on the surrogates (Sec. 2.2.2). Mutual information estimated from the correlation measure under normality assumption, as $I_{s y}=-0.5 \log \left(1-\rho_{s y}^{2}\right)$ is also shown as reference. For the data considered in this study, the mutual information estimated using the normal

approximation closely follows obtained using (2). However, this might not be true in general. The pair-wise dependencies were significant ( $\mathrm{a}=0.05$ and power $\sim 0.8$ ), Figure 6c, across samples sizes ( $\mathrm{nc}=33,66$ and 99) were (COLL-ALP), (COLL-OCN), (ALPBSP), (ALP-OCN), (BSP-OCN) and (OCN-PTH1R). Unlike linear correlation measure and Fisher's exact test, the number of statistically significant mutual information estimates ( $\alpha=0.05$, power $\sim 0.8$ ) do not change dramatically with decreasing number of colonies ( $n_{c}=33,66$ and 99). Thus mutual information is comparatively robust in capturing the pair-wise dependencies with decreasing colony number and perturbations. As with the correlation measure and Fisher's exact test, the genes $P D G F R \alpha$ and $P T H r P$ were independent of all the other genes and from one-another and reflected by the low power and high p-value. This result is in agreement with those reported by (Madras et al., 2002).

Summary (Sec. 3.4): The pair-wise dependencies estimated using mutual information ( $\alpha$ $=0.05$, power $\sim 0.8$ ), that were robust to decreasing sample size ( $n_{c}=99,66$ and 33) and perturbation consisted of: (COLL-ALP), (COLL-OCN), (ALP-BSP), (ALP-OCN), (BSP-OCN) and (OCN-PTH1R)

Although the genes ALP, BSP, OCN and COLL form the set of high entropy genes, the pair-wise dependencies COLL - ALP; ALP - OCN; ALP - BSP; BSP - OCN persist with decreasing sample sizes and perturbations. These were verified using correlation, Fisher's exact test and mutual information. Hence these might form the set of robust dependencies in the osteoblast differentiation program. While the colony numbers ( $\mathrm{nc}=$

22 and 11) are included in Table I, the number of dependencies dramatically reduce for these colony numbers, which implies that it might not be possible to statistically infer the dependencies for colony numbers lesser than $\left(n_{c}=33\right)$.

The above analysis treats pair-wise dependencies as mutually exclusive events. However, when we connect these as a part of the network, it is possible that the dependencies may cease to exist. This is attributed to the fact that the pair-wise dependency may be conditionally dependent on the other elements in the network. The symmetric nature of the pair-wise dependency measures discussed above does not provide information regarding the directionality or more precisely the causality information of the network. In the following section, we use the concepts of Bayesian networks (Pearl, 2000) to infer the network structure from the given data, under certain generic conditions.

# 4. Bayesian Networks Approach to determine network structure 

Bayesian networks (Pearl, 2000; Spirtes et al, 2001) have been used extensively to model conditional dependencies in a given data. Recent reports (Friedman et al., 2000) have discussed their application for analyzing gene expression data obtained from microarrays. In this report, Bayesian networks is used as a tool to determine the network structure from the given data. A brief introduction along with definitions and simple examples is provided for completeness. A rigorous theoretical treatment can be found elsewhere (Pearl, 2000; Spirtes et al, 2001; Heckerman, 1999).
(i) Directed Acyclic Graph: A directed acyclic graph (DAG) is a graph $\mathbf{G}(V, E)$ where $V$ represents the vertices and $E$ represents an edge, such that each edge is a directed edge

and no cycles are allowed. In this study, the vertices $(V)$ are represented by the random variables (genes) and the edges $(E)$ the dependencies between them.

A Bayesian network represents the joint distribution of a set of random variables, represented by the vertices $(V)$ in a DAG $G$ (Figure 7) as a product of conditional distributions. Consider a DAG $G: g_{i}, i=1 \ldots . . v$, where the parents of vertex $g_{i}$ is $\pi\left(g_{i}\right)$; the joint distribution of $G$ is given by:

$$
P\left(g_{1}, \ldots, g_{v}\right)=\prod_{i=1}^{v} P\left(g_{i} / \pi\left(g_{i}\right)\right)
$$

(ii) Markov Condition: A necessary and sufficient condition for a probability distribution $P$ to be Markov relative to a DAG G, is that every variable is independent of all its nondescendants conditional on its parents (Pearl, 2000).

Remark: There are two important assumptions in the definition of Bayesian networks. The first assumption is the acyclic nature of the graph, which assumes absence of cycles (feedbacks). The second assumption is that the joint distribution can be factored into a product of conditional dependencies given by (equation 3). In genetic networks, it is not uncommon to observe feedbacks (cycles) and the nonlinearly coupled nature of the networks might not lend themselves to be factored as a product of conditional dependencies. It should also be noted that the present study did not consider hidden variables, such as proteins that are an inherent part of the biological network. Thus the resulting network is an approximation of the actual biological network.

(iii) Markov Equivalence: (Pearl, 2000) defines two DAGs to be Markov equivalent if they have the same sets of $v$-structures whose tails are not connected by an arrow.

Markov equivalence addresses the important question as to whether the observed structure is unique or is it a part of an equivalent class of structures. A simple example of Markov equivalence is exhibited by the DAGs $\left(G_{1}\right)$ and $\left(G_{2}\right)$ where $G_{1}: g_{1} \rightarrow g_{2}$ and $G_{2}$ : $g_{2} \rightarrow g_{1}$. The corresponding joint probability distributions if factored into conditional dependencies are given by: $p\left(g_{1}\right) p\left(g_{2} / g_{1}\right)$ and $p\left(g_{2}\right) p\left(g_{1} / g_{2}\right)$ respectively. By Baye's theorem each of the joint probability distributions is equal to $P\left(g_{1}, g_{2}\right)$. In the first case, an upstream gene $g_{1}$ affects the value of a downstream gene $g_{2}$, whereas the roles are reversed in the second case. Thus, information of the conditional dependencies fails to provide insight into the direction of regulation or causality of the network. Therefore, the equivalent class is represented as an undirected graph $g_{1}-g_{2}$. For a DAG $g_{1} \rightarrow g_{2}$, manipulating the expression of gene $g_{2}$ has no effect on $g_{1}$, while it is not true the other way around. It is important to reiterate the fact that we do not consider feedback in these models. Gene knockout studies (interventions) may be used to infer such structures Friedman et al. (2000). However, there may be instances where even interventions may fail to provide insight into network structure. Consider the networks of the form $G_{1}: g_{1} \rightarrow g_{2} \rightarrow g_{3}$ and $G_{2}:\left\{g_{1} \rightarrow g_{2}, g_{1} \rightarrow g_{3}\right\}$, where knocking out $g_{1}$ results in no expression of $g_{2}$ and $g_{3}$. Either of the structures is a possible explanation of the result. However, a prudent choice of gene knockout can be helpful in inferring network structure, Akutsu et al. (1998).

A more classic, and an important Markov equivalence class, is shown in Figure 7. For the chains Figures 7 (a and c) and the fork Figure 7b, the marginally dependent genes $A$ and $C$ become independent, conditioned on $B$, i.e. learning about $A$ does not affect the state of $C$, given $B$. Alternatively, these DAGs are Markov equivalent and it is not possible to infer the direction of the arcs based on conditional probability distributions. The equivalence structure representing the DAGs in Figure 7 is given by $(A-B-C)$. The DAG in Figure 7d is a $v$-structure, also known as the collider (Pearl, 2000). Unlike that of the forks and the chains, the equivalent class of collider consists only the collider, thus retains the direction of the arcs. It is important to note that the tails of the collider should be free and not connected by an arrow, as per the definition of Markov equivalence (Pearl, 2000). If the tails are connected, the possible directions of the tail are $A \rightarrow C$ and $C \rightarrow A$. The former results in a DAG with joint distribution $p(B / A C) p(A) p(C / A)$, while the latter has joint distribution $p(B / A C) p(C) p(A / C)$. Since $p(C) p(A / C)=$ $p(A) p(C / A)=p(A C)$, the two structures are equivalent. Thus it is important that the tails are not connected by an arrow. Contrary to the chains and forks, in a collider, two marginally independent genes, $A$ and $C$, become dependent conditioned on gene $B$. This result is known as Berkson's paradox or explaining away effect (Pearl, 2000). There are two possible causes that explain the state of $C$. The most plausible one explains away the other. Pearl, 2000 introduced the concept of $d$-separation and pattern, which emphasizes the fact that a given distribution has a unique minimal causal structure up to d-separation. Thus, it is crucial to determine the equivalent class of a network, as conclusions based on single realizations is incomplete. This is evident from the example shown in Figure 7, where $\mathrm{a}, \mathrm{b}$ and c are equivalent structures and cannot be distinguished by probablisitic

information alone. Such an equivalent class of networks is also represented as partially directed acyclic graphs or PDAGs. They contain both directed and undirected edges, hence the term PDAG. While the directed edges of the PDAGs are common to all the DAGs in the equivalent class, it is not true the other way around. However, it is important to understand that a directional edge of the form $X \rightarrow Y$ is more of an indication rather than evidence that $X$ is the cause of $Y$ (Pearl, 2000; Spirtes et al., 2000; Glymour and Cooper, 1999; Friedman et al 2000).

Summary (Sec. 4): Given the above intricacies, supported by examples in Figure 7, it is clear that identifying pair-wise dependencies may be inadequate in determining the underlying network structure. This is attributed to the fact that some of these dependencies may break down conditioned on the other members of the network. It is also important to note that the equivalent class of networks (PDAGs) as conclusions based on (DAGs) is incomplete.

# 4.1 Learning network structure with varying sample sizes 

Several techniques have been proposed in the past for learning the structure of a Bayesian network from a given observation. These include exhaustive enumeration, constraintbased approaches, and search-based techniques (Pearl, 2000; Spirtes et al., 2000; Heckerman, 1999, Glymour and Cooper, 1999). The number of possible DAGs increases super-exponentially with the number of nodes; hence exhaustive enumeration is not feasible for networks with nodes (> 5) Glymour and Cooper, (1999). In this study, constraint-based methods (Spirtes et al., 2000) along with search techniques such as hill

climbing and Markov Chain Monte Carlo (MCMC) (Heckerman, 1999; Glymour and Cooper, 1999) were used to determine the network structure.

# 4.1.1. Learning network structure - Constraint based technique 

The PC (Peter and Clark) algorithm by Spirtes et al (2001) determines the underlying network structure from the conditional independence information. The method begins with all possible relationships between the genes and determines the network structure by systematically deleting the edges. The edge removal is based on conditional independence criteria. In this study, the Fisher's Z test was used to determine the statistical significance of the conditional dependencies. The maximum number of incoming edges to any node was fixed at three, the significance level at $(\alpha=0.05)$ and $\left(N_{B}=1000\right)$ bootstrap realizations were generated for each sample size. These bootstrap realizations represent perturbations of the given data (Friedman et al 2002). The frequency of occurrence of a (directional) dependency of the form $X \rightarrow Y$ in the resulting PDAGs $G_{\pi}$ was determined with the expression:

$$
P_{x \rightarrow y}=\frac{\text { Number of occurences of } X \rightarrow Y \text { in } G_{\pi}(i), i=1 \ldots N_{B}}{N_{B}}
$$

Similarly, one can determine $P_{x \leftarrow y}$. The frequency of occurrence of a dependency between nodes $X$ and $Y$ is given by $P_{X Y}=P_{x \rightarrow y}+P_{x \leftarrow y}+P_{x \rightarrow y}$. The dependencies generated by the constraint-based approach were ranked according to $P_{X Y}$. The values of $P_{X Y}, P_{x \rightarrow y}$ and $P_{x \leftarrow y}$ is shown in Table II. While the ranking of the dependencies is consistent with decreasing sample size, the power reduced considerably (Table II). The resulting network contained interaction between the genes $A L P, B S P, C O L L$ and $O C N$. The dependencies

COLL - ALP; ALP - OCN; ALP - BSP have power $>0.8$ in bootstraps generated with sample sizes of 66 and 99 colonies, whereas a marked decrease is observed with sample size 33. From Fig. 8, it can be observed that neither PDGFR $\alpha$ nor PTHrP is a part of the network and may act independently of other genes (Madras et al, 2002). While the frequency of occurrence can be thought of as the statistical power, it is not clear what would be an acceptable value (Friedman et al, 2002). From Table II, it should be noted that the frequency of occurrence $\operatorname{COLL} \rightarrow A L P$ is consistently greater than the frequency of occurrence of $A L P \rightarrow C O L L$, similarly for $A L P \rightarrow O C N$ and $B S P \rightarrow A L P$. Thus it is highly likely that the edges are oriented accordingly. An approximate network structure from the colony data constructed with the constraint-based approach and the probability of occurrence of the edges in the PDAGs, Table II, is shown in Figure 8.

# 4.1.2 Learning network structure - Search based technique 

While the constraint-based approach determines the network structure from conditional dependencies, search algorithms along with a scoring criteria can be used as an effective alternative. Hill climbing, is a heuristic local search technique (Heckerman, 1999), that determines the network structure by adding, deleting or reversing the edges and evaluating the score with each change. The objective is to find the structure that maximizes the scoring function, i.e. maximize $P(S / D)$, where $S$ is the structure given the data $D$, but $P(S / D)=(P(D / S) P(S)) / P(D)$. It should be noted that the term $P(D)$ is a constant and can be filtered out. Thus maximizing $\log P(S / D)$ is equivalent to maximizing $\log P(D / S)+\log P(S)$. This is known as the Bayesian score of the structure $S$. In this study, we use the Bayesian score with Bayesian Dirichlet priors [Cooper and Herskovits,

1992; Heckerman, 1999]. However, such local search techniques such as hill climbing are susceptible to local optimum. As in Sec. 4.1.1, $N_{B}=100$ bootstrap realizations were generated for this analysis. The PDAGs of the DAGs (from the hill climbing procedure) were generated using the Chickering (Chickering, 1996) and the d-separation algorithms (Pearl, 2000). The maximum number of incoming edges was fixed as three for the dseparation criteria.

The steps in determining the dependencies are as follows:

- Determine the DAG $G(i)$ from the given data $(D)$ using the hill-climbing approach
- Determine the PDAG $G_{\mathrm{x}}(i)$ of the DAG $G(i)$

Repeat the above for $i=1 \ldots N_{B}$, where $N_{B}$ represents the number of bootstrap realizations. Determine the frequency of occurrence of the edges using expression (equation 4).

The frequency of occurrence of the edges was determined with varying sample sizes (99, 66 and 33 colonies, with $N_{B}=100$ ) and subsequently ranked, Table III. The top three values corresponding to the edges $A L P-O C N, B S P-A L P$ and $A L P-C O L L$ are shown in Figure 9. The frequency of occurrence of the edges $C O L L-F G F R 1, O C N-$ PTH1R, $O C N-B S P$ were similar $(\sim 0.5)$ across the different sample sizes and hence unclear. Unlike the case of 99 and 66 colonies, the frequency of occurrence of the edges $A L P-O C N, B S P-A L P$ and $A L P-C O L L$ were below 0.8 in the case of 33 colonies. The PDAGs generated in the search and score method also did not provide information on the directionality of the edges. Finally, a Markov-chain Monte-Carlo (MCMC) implemented with Metroplis-Hasting algorithm [Metropolis et al., 1953; Hastings, 1970] was used to determine the network structure. The given data containing

all the 99 colonies were used. Determining the convergence of the MCMC is a non-trivial issue and beyond the scope of the present report. In MCMC, the acceptance or rejection of the proposed random sample is determined by the acceptance ratio [Metropolis et al., 1953; Hastings, 1970]. A large value of the acceptance ratio implies that the proposed sample is close to the current state, whereas a small value implies proposals are distant from the current state. The acceptance ratio was plotted against the MCMC steps to determine the convergence (Figure 10). The burn-in was chosen as 500, i.e. the first 500 MCMC steps were assumed to be transients, hence discarded. The number of MCMC steps was fixed at 10,000. The DAGs generated in the last 1000 steps by the MCMC was chosen for subsequent analysis. The PDAGs of the DAGs obtained from the MCMC was generated using the Chickering (Chickering, 1996) and the d-separation algorithms (Pearl, 2000). The maximum number of incoming arcs was fixed at three for the $d$ separation criteria. The frequency of occurrence of the edges was determined using expression (4) and shown in Table IV. The approximate network structure of the genetic network is shown in Figure 11.

Summary Sec.4.1: The network structure consisting of the undirected edges ALP-OCN, $B S P-A L P$ and $A L P-C O L L$ was found to be robust to perturbations and reduced sample size. This was verified using constraint-based and search-based techniques. It is highly likely that these represent the set of robust dependencies and may form the backbone of the osteoblast differentiation program.

# 5. Discussion: 

Several techniques have been proposed in the past to model the network and the dependency between a given set of genes [Kauffman, 1993; Gardner et al., 2000; Shmulevich et al., 2002; Liang et al., 1998; Akutsu et al., 1998]. Each of these techniques works under certain implicit assumptions for the gene expression data. More importantly, they require explicit information regarding temporal gene expression and/or truth tables which might require gene knockout experiments. Data mining approaches can be used to obtain representation of the truth table, however a gene can be up-regulated in apoptosis (cell death) and cancer (cell proliferation) depending in the experimental paradigm. Thus, there are practical difficulties associated with these techniques. Nonlinear dynamical approaches such as those discussed in [Kauffman, 1993; Gardner et al., 2000] are highly involved. They have been used successfully to model interactions at transcriptional level in prokaryotes and hence represent true biological network, unlike the above which use measures of association. Such detailed models can form as a follow up to confirm the results obtained in this study.

The methods discussed here, infer the dependencies and network structure from gene expression across replicate clones without explicit temporal information. The data used in this study is in the form of a binary matrix consisting of nine genes across ninety-nine colonies during osteoblast differentiation, where each gene was assigned an ON or OFF state in a given colony. However, the methods can be extended to other types of data sets too. The objective was to determine the uncertainty, dependencies and structures that are robust to perturbations and reduction in the sample size of nine genes across ninety nine

colonies in osteoblast differentiation. This was accomplished with entropy, linear correlation, mutual information and Bayesian networks. Perturbation of the data was accomplished by resampling with replacement (Sec. 2.2.1). The methods are generic and can be extended to gene expression data obtained in similar experimental paradigms. These include data sets obtained using tools such as microarrays [Friedman et al., 2000]. However, there are subtle issues associated with microarray analysis, such as: image segmentation, normalization, high dimensionality and lower number of replicates. Image segmentation and normalization form the preliminary steps and any error incurred at this stage is bound to propagate through subsequent analysis. Determining the optimal structure with a large-number of genes (dimension) and the small replicate arrays can be challenging if not impossible. This can be attributed to increasing local optimum with the number of genes. In the present study, any conclusion based on number of colonies lesser than 33 is likely to be inconclusive. However, microarrays can be used as a screening tool to subsequent clonal analysis of a small set of genes.

The ranked entropy profile of the nine genes in decreasing order was $[A L P, B S P, O C N$, $\operatorname{COLL}, \operatorname{PDGFR} \alpha, \operatorname{FGFR1}, \operatorname{PTHrP}, \operatorname{PTH1R}$ ] (Sec. 3.1) and did not change with perturbations and reduction in the sample size. The significant pair-wise dependencies obtained using linear correlation and Fisher's exact test ( $\alpha=0.05$, with power $\sim 0.8$ ), across $\left(n_{c}=33,66\right.$ and 99) were: (COLL-ALP), (ALP-BSP), (ALP-OCN), and (BSP$O C N)$. Those obtained with mutual information (power $\sim 0.8$ ) were (COLL-ALP), (COLL-OCN), (ALP-OCN), (ALP-BSP), (BSP-OCN) and (OCN - PTH1R). As reported earlier, [Madras et al., 2002], the genes PDGFRa and PTHrP were independent of each

other and the other genes. These were consistent across all the three measures of correlation. The mutual information was robust compared to the correlation measure in retaining the dependencies with perturbations and reduction in sample size, (Sec. 3). The pair-wise dependency analysis implicitly assumes each pair to be mutually exclusive and hence may be unhelpful in determining the network. It might not be surprising to note that certain dependencies may cease to exist when connected together as a part of the network. In order to capture the conditional dependencies we used the concepts of Bayesian networks (Sec. 4). The directed acyclic graphs (DAG) were determined using constraint-based and search-based techniques. The PC algorithm, which is a constraintbased technique, was used to determine the DAG and PDAG structures. Two searchbased techniques, namely, hill-climbing and Markov-Chain Monte-Carlo (MCMC), were used to determine the DAGs. The PDAGs were generated from these DAGs using d separation and Chickering's algorithm separately. Inferences based on DAG structures are incomplete, as conditional probabilistic distributions cannot distinguish equivalent structures (Sec. 4). The PDAGs represent structures (possibly causal) common to all the DAGs of a given equivalent class and hence its choice. To rule out the possibility that the given PDAG is by chance, the frequency of occurrence of the edges was determined from multiple realizations of the PDAGs. The structure (COLL-ALP), (BSP-ALP) and (ALP$O C N$ ) was preserved across the PDAGs generated by the different techniques. The genes PDGFRa and PTHrP were independent of each other and the other members of the network, hence not a part of the final structure. This structure had a (power $>0.8$ ) with decreasing sample size ( 99 and 66 colonies) and was robust to perturbation of the data. These structures were retained even when the number of boostrap realizations were

changed and with exhaustive enumeration with five nodes comprising of (COLL, ALP, $B S P, O C N$ and PTH1R), results not included. Therefore the structure (COLL-ALP), (BSP-ALP) and (ALP-OCN), might play a pivotal role in the osteoblast differentiation program. (Figures 8, 9 and 11). While the frequency of occurrence of the arcs for the edges (COLL-ALP), (BSP-ALP) and (ALP-OCN) were considerably high even in the case of 33 colonies, they failed to statistically significant (< 0.8). Thus we suspect analysis with number of colonies lesser than 33, would be inconclusive.

Biological Issues: Of the eight genes included in the analysis, the four identified above (COLL, ALP, BSP and $O C N$ ) are characteristic of osteoblasts, either encoding enzymes or matrix components integral to differentiated osteoblast function. Further, many of the aspects of the PDAGs obtained by the different approaches correlated with experimental studies (Stein and Lian, 1993; Aubin et al., 1999; Madras et al., 2002). The constraintbased technique indicated $\operatorname{COLL} \rightarrow A L P$ to be more frequent than $A L P \rightarrow C O L L$ supporting the hypothesis presented by Madras et al. (2002) that COLL is expressed before ALP. Similarly, $B S P \rightarrow A L P$ occurred more frequently than $A L P \rightarrow B S P$. ALP may not be the last of the genes to be expressed during differentiation as $A L P \rightarrow O C N$ was more frequent than $O C N \rightarrow A L P$ (Table II and Figure 8), consistent with experimental studies (Stein and Lian, 1993; Malaval et al., 1999). That $A L P$ was correlated with each of the other three genes (COLL, BSP and $O C N$ ) suggests that it is essential to osteoblast function (reviewed by Aubin et al., 1999), a conclusion supported by the observation that all bones display mineralization defects in ALP knockout mice (Fedde et al., 1999; Wennberg et al., 2000). It should be noted that the $B S P-O C N$ and $C O L L-OC N$ dependencies came through

some but not all of the measures, and may reflect the fact that all three genes contain Cbfa1 binding sites in their promoters (Ducy et al., 1997) and thus, appear to share common transcriptional regulatory mechanisms. The search-based approach by MCMC suggested that COLL-FGFR1 and OCN-PTH1R may be components of the network (Table IV and Figure 11). Both FGF and PTH drive osteoblastogenesis, but in the network described here, their receptors appear to behave marginally independent and thus may utilize parallel pathways or receptors, consistent with the idea of exchangeability (Madras et al., 2002). On the other hand, as subpopulations of osteoblasts with distinct properties have been shown to exist (Liu et al., 1997; Candeliere et al., 2001), variation in the activity of FGF and PTH signaling pathways may contribute to osteoblast heterogeneity represented in the array of colonies analyzed here.

Causality Issues: The PDAGs were generated from the DAGs to infer possible causal structures common to the equivalent class. Causality is an indicator rather than a confirmation of temporal precedence of gene expression. Traditional time course experiments on a population of cells can be used to determine a temporal sequence of events (Stein and Lian, 1993). The se in turn can be incorporated to determine the causal structure of the network obtained by the Bayesian approach. In this study, the variation in rates of differentiation between colonies incorporated a stochastic component using a single time point that may have a significant impact on the results.

Reliability Issues: From our analysis, it is clear that the genes PTHrP and PDGFR $\alpha$ are likely to behave independently of the other members of the network and from each other,

consistent with the findings of Madras et al. 2002. This is confirmed by the pair-wise dependency study and the network structure. Therefore it is possible that these may not be required for osteoblast differentiation under the in vitro conditions utilized or may participate in parallel paths leading to the end phenotype. Determining the serial and parallel paths in the network can be useful in determining the network reliability. Tractable analytical expressions can be determined if the failure of the components in the networks is assumed to be independent of one another. For a serial network with dependent components (positively correlated), expression for failure time is conservative compared to the independent assumption, whereas it is anti-conservative for parallel networks. Under the assumption of a coherent network, consisting of $k$ independent components, a bound can be achieved on the network reliability (Barlow and Proschan, 1981). The more parallel paths that may exist, the more reliable the network is to perturbations. This in turn brings up important questions as to whether some lineages are more reliable than others due to the very nature of their network. The reliability analysis also provides a way to quantify and distinguish across the various experimental conditions. Thus determining the network reliability assigns a quantitative value to the changing network structure.

Nonlinear Dynamical Perspective: While Bayesian networks is a powerful technique, it works under certain assumptions such as: acyclic nature of the network and representing the joint probability distribution as the product of conditional probability distributions. Feedback loops are ubiquitous in biological systems and their control can be explained only by nonlinear systems theory. A nonlinear dynamical perspective of the above

problem would involve a nonlinearly coupled differential equation system, representing the interactions between the genes. The evolution and temporal behavior of a $k$ gene network would be represented by a $k$ dimensional state space (phase space). The class of dissipative dynamical systems, which most real world systems are, settles down on an attractor after an initial transient behavior. Such systems can exhibit a wide range of behaviors such as limit cycle (periodic), torus (quasiperiodic) and chaotic behavior. In the present experimental paradigm, each gene in the network can be represented by a variable. Thus, the interaction of $k$ genes can be represented by a coupled nonlinear system consisting of $k$ states, given by a set of differential equations. The evolution of such a system settles down on an attractor after an initial transient behavior. This attractor represents the end phenotype. The heterogeneity observed in the expression across the colonies can be attributed to sampling at the different points in the attractor, as the state of a gene here is represented by a continuum of points and gives rise to infinite possibilities. Strange attractors are hallmarks of chaotic systems, which show sensitivity to initial conditions. Such sensitivity can be induced by minor variations in external stimuli such as serum and hormonal cocktail concentrations, whose values are on the real plane. Theoretically, an infinite choice of the concentrations can give result in the same end phenotype (attractor). Thus another possible explanation for the observed heterogeneity between the colonies may be due to sampling and quantification of the state as being ON or OFF. As with Bayesian networks, a nonlinear dynamical approach also has its limitations. Stationarity issues and high-dimensionality of the system may limit its application to the present paradigm.

# Acknowledgements: 

We would also like to thank Kevin Murphy and Philip Leray for making available their Matlab routines, and the Arkansas Cancer Research Center (ACRC) differentiation group for useful discussions. This research was supported in part by funds provided to the UAMS Microarray Facility through Act 1, The Arkansas Tobacco Settlement Proceeds Act of 2000, by NIH Grant \#P20 RR-16460 from the BRIN Program of the National Center for Research Resources and by an NIH grant to CAP (AG20941).

# Figure Legends: 

Figure 1. A block diagram showing the induction of noise at the various stages in gene expression data, where $\in_{t}$ and $\eta_{t}$ represent the dynamical and observational noise; $f$ and $g$ are nonlinear functions and $y_{t}$, the observed gene expression value.

Figure 2. The mean and the standard deviation of the entropy (self-information) of the eight genes, obtained by resampling 99 (top), 66 (middle) and 33 (bottom) colonies.

Figure 3. The mean and the standard deviation of the mutual information (I) obtained for the 28 pairs of genes, along with those obtained on the random shuffled surrogates (noise floor) is shown in Figure 3a (top). Those obtained using the correlation ( $\rho$ ) measure along with the random shuffled surrogates (noise floor) is shown in Figure 3b (bottom). The value of the mutual information derived from the normal approximation, $\mathrm{I}=-0.5 \log _{2}(1-$ $\rho^{2}$ ), is shown in Figure 3a for reference. 100 bootstrap samples with ninety-nine colonies each were used.

Figure 4. The mean and the standard deviation of the mutual information (I) obtained for the 28 pairs of genes, along with those obtained on the random shuffled surrogates (noise floor) is shown in Figure 4a (top). Those obtained using the correlation ( $\rho$ ) measure along with the random shuffled surrogates (noise floor) is shown in Figure 4b (bottom). The value of the mutual information derived from the normal approximation, $\mathrm{I}=-0.5 \log _{2}(1-$ $\rho^{2}$ ), is shown in Figure 4a for reference. 100 bootstrap samples with sixty-six colonies each were used.

Figure 5. The mean and the standard deviation of the mutual information $(I)$ obtained for the 28 pairs of genes, along with those obtained on the random shuffled surrogates (noise floor) is shown in Figure 5a (top). Those obtained using the correlation ( $\rho$ ) measure along with the random shuffled surrogates (noise floor) is shown in Figure 5b (bottom). The value of the mutual information derived from the normal approximation, $\mathrm{I}=-0.5 \log _{2}(1-$ $\rho^{2}$ ), is shown in Figure 5a for reference. 100 bootstrap samples with thirty-three colonies each were used.

Figure 6. Power estimated using the linear correlation, Fisher's exact test and mutual information for each of the 28 pairs is shown in a, b and c respectively. The (solid line and the open circle) represents resampling with 99 colonies, and those obtained using 66 colonies and 33 colonies are represented by the (dotted lines) and (bold dashed lines) respectively. 100 bootstrap samples were generated for (33, 66 and 99 colonies).

Figure 7. The DAGs shown (a, b and c) form a Markov equivalent class of the form ( $A-$ $B-C)$. The equivalence class can be generated by applying the Bayes theorem to the conditional dependencies shown in bold letters. The DAG (bottom) is an example of $v$ structure; unlike (a, b, c) it is unique.

Figure 8. Approximate structure (PDAG) constructed from the frequency of occurrence, Table II, using the constraint based approach. The arrows denote possible direction of edges. The vertices (C, A, B and O) represent the genes COLL, ALP, BSP and OCN respectively.

Figure 9. Approximate structure (PDAG) corresponding to the frequency of occurrence, Table III. The vertices (C, A, B and O) represent the genes COLL, ALP, BSP and OCN respectively.

Figure 10. Convergence of the acceptance ratio with MCMC steps.

Figure 11. Approximate structure (PDAG) constructed from the frequency of occurrence, Table IV, using Markov-Chain Monte-Carlo (MCMC). The PDAGs were determined using the Chickering algorithm and the d-separation criteria (Table IV). The vertices (C, A, B and O) represent the genes COLL, ALP, BSP and OCN respectively.

# Externally observed Gene Expression Value $\left(y_{t}\right)$ 

Measurement Noise $\Rightarrow \begin{aligned} & \text { Measurement Device } \\ & y_{t}=g\left(x_{t}\right)+\eta_{t}\end{aligned}$

Dynamical Noise $\Rightarrow$ Biological System $\quad x_{t+1}=f\left(x_{t}, \epsilon_{t}\right)$

Figure 1

![img-0.jpeg](img-0.jpeg)

Figure 2

![img-1.jpeg](img-1.jpeg)

Figure 3

![img-2.jpeg](img-2.jpeg)

Figure 4

![img-3.jpeg](img-3.jpeg)

Figure 5

![img-4.jpeg](img-4.jpeg)

Figure 6

Chain
(a)
![img-5.jpeg](img-5.jpeg)
$\mathbf{p ( A )} \mathbf{p ( B / A}) \mathrm{p}(\mathrm{C} / \mathrm{B})$
Fork
(b)
![img-6.jpeg](img-6.jpeg)
$\mathbf{p ( A )} \mathbf{p ( B )} \mathbf{p ( B )} \mathbf{p ( C / B )}$
Chain
(c)
![img-7.jpeg](img-7.jpeg)
$\mathrm{p}(\mathrm{A} / \mathrm{B}) \mathrm{p}(\mathrm{B} / \mathrm{A}) \mathrm{p}(\mathrm{A})$

# Collider 

(d)
![img-8.jpeg](img-8.jpeg)
$\mathrm{p}(\mathrm{A}) \mathrm{p}(\mathrm{B} / \mathrm{AC}) \mathrm{p}(\mathrm{C})$

Figure 7

![img-9.jpeg](img-9.jpeg)

Figure 8

![img-10.jpeg](img-10.jpeg)

Figure 9

![img-11.jpeg](img-11.jpeg)

Figure 10

![img-12.jpeg](img-12.jpeg)

Figure 11

Table I
Dependencies that had a (power $\sim 0.8, \alpha=0.05$ ) with ( $\mathrm{N}_{\mathrm{B}}=100$ ) bootstrap realization using the linear correlation, mutual information and Fisher's exact test for the various colony sizes ( $n_{c}=99,66,33,22$ and 11). The genes COLL, ALP, BSP, $O C N, F G F R 1, P T H 1 R, P D G F \alpha$ are represented by $\mathrm{C}, \mathrm{A}, \mathrm{B} \mathrm{O}, \mathrm{F}, \mathrm{P}$ and D in the table.


Table II
Frequency of occurrence of the edges from PDAGs generated using constraint based approach. The vertices (C, A, B and O) represent the genes COLL, ALP, BSP and OCN respectively.


Table III
Frequency of occurrence of the edges in PDAGs obtained by the D-separation and the Chickering algorithm, on DAGs generated by Hill Climbing. The vertices (C, A, B and O) represent the genes COLL, ALP, BSP and OCN respectively.


Table IV
Frequency of occurrence of the edges in PDAGs obtained by the D-separation and the Chickering algorithm, on DAGs generated by Monte-Carlo Markov Chain (MCMC). The vertices (C, A, B, O, F and P) represent the genes COLL, ALP, BSP, OCN, FGFR1 and PTH1R respectively.


# Reference: 

Akutsu, T., Kuhara, S., Maruyama., O. Miyano, S. 1998. Identification of Gene Regulatory Networks by Strategic Gene Disruptions and Gene Overexpressions, Proceedings of the ninth annual ACM-SIAM symposium on Discrete algorithms, 695702 .

Aubin, J.E., 1998. Bone Stem Cells. $25^{\text {th }}$ Anniversary Issue: New directions and dimensions in cellular biochemistry. Invited Chapter. J. Cell. Biochem. Suppl. 30/31, 7382 .

Aubin J.E., Candeliere, G., and Bonnelye, E., 1999. Heterogeniety of the osteoblast phenotype, Endocrinologist, 9, 25-31.

Aubin J.E., and Triffit, J.T., 2001. Principles of Bone Biology, 2nd Edition, Bilezikian, J.P. Raisz, L.G. and Rodan, G.A. (Eds.) Academic Press.

Barlow, R.E., and Proschan, F., 1981. Statistical Theory of Reliability and Life Testing Probabiltity Models. Holt, Reinhart and Winston, Inc.

Brillinger, D.R., 2002. Second-order moments and mutual information in the analysis of time series. Recent Advances in Statistical Methods. Imperial College Press, London, 6476.

Butte A.J., and Kohane, I.S., 2000. Mutual information relevance networks: functional genomic clustering using pairwise entropy measurements. Pac Symp Biocomput. 418-29.

Candeliere, G.A., Liu, F., and Aubin, J.E., 2001. Individual osteoblasts in the developing calvaria express different gene repertories. Bone 28, 351-361.

Chickering, D. M., 1996. Learning equivalence classes of Bayesian network structures. In Proceedings of the Twelfth Conference on Uncertainty in Artificial Intelligence, 150-157.

Cooper, G., and Herskovits, E., 1992. A Bayesian method for the induction of probabilistic networks from data. Machine Learning, 9: 309-347.

Ducy, P., Zhang, R., Geoffroy, V., Ridall, A.L., and Karsenty, G., 1997. Osf2/Cbfa1: A transcriptional activator of osteoblast differentiation. Cell 89, 747-754.

Efron, B., Tibshirani, R.J., and Efron, B., 1994. An Introduction to the Bootstrap. CRC press.

Fall, C.P., Marland, E.S., Wagner, J.M., and Tyson, J.J., 2002, Computational Cell Biology, Springer-Verlag, New York.

Fedde, K.N., Blair, L., Silverstein, J., Coburn, S.P., Ryan, L.M., Weinstein, R.S., Waymire, K., Narisawa, S., Millan, J.L., MacGregor, G.R., and Whyte, M.P., 1999.

Alkaline phosphatase knock-out mice recapitulate the metabolic and skeletal defects of infantile hypophosphatasia. J. Bone Miner. Res. 14, 2015-2026.

Fraser, A., and Swinney, H.L., 1986. Independent coordinates for strange attractors from mutual information. Phys. Rev. A 33, 1134.

Friedman, N., Goldszmidt, M., and Wyner, A., 1999. Proceedings of the Fifteenth Conference on Uncertainty in Artificial Intelligence, Stockholm, Sweden, July 30-August 1, Kathryn B. Laskey, Henri Prade (Eds.). Morgan Kaufmann, 196-205.

Friedman, N., Linial, M., Nachman, I., and Pe'er, D., 2000. Using Bayesian Networks to Analyze Expression Data. Journal of Computational Biology 7(3-4): 601-620.

Gardner, T.S., Cantor, C.R., and Collins, J.J., 2000. Construction of a genetic toggle switch in Escherichia coli. Nature. 20, 339-342.

Glass, L., and Hill, C., 1998.Ordered and disordered dynamics in random networks Europhysics Letters 41(6) 599-604.

Goldbeter, A., Biochemical Oscillations and Cellular Rhythms: the molecular bases of periodic and chaotic behaviour,Cambridge University Press, 1996

Goldbeter, A., and Dupont, G., 1990. Allosteric regulation, cooperativity, and biochemical oscillations. Biophys. Chem. 37, 341-53.

Glymour, C., and Cooper, G., 1999. Computation, Causation and Discovery, AAAI Press.

Hastings, W.K. 1970. Monte Carlo Sampling Methods Using Markov Chains and Their Applications, Biometrika, 57:97-109.

Hasty, J., Pradines, J., Dolnik, M., Collins J.J. 2000. Noise-based switches and amplifiers for gene expression. Proceedings of the National Academy of Sciences USA 97:20572080.

Heckerman, D., 1999. A Tutorial on Learning with Bayesian Networks. In Learning in Graphical Models, M. Jordan, ed. MIT Press, Cambridge, MA.

Hope, A.C.A., 1968. A simplified Monte Carlo significance test procedure. Journal of the Royal Statistical Society, Series B, 30, 582-598.

Huang, C. F., and Ferrell Jr, J.E., 1996. Ultrasensitivity in the mitogen-activated protein kinase cascade. 93(19), 10078-10083.

Jacob, F., and Monod, J., 1961. Genetic regulatory mechanisms in the synthesis of proteins. Journal of Molecular Biology. 3, 318-356.

Kauffman, S. A., 1969. Metabolic stability and epigenesis in randomly constructed genetic nets. J. Theor. Biol. 22, 437-467.

Kauffman, S.A., 1993. The Origins of Order: Self-Organization and Selection in Evolution, Oxford University Press, New York.

Liang, S., Fuhrman, S., and Somogyi, R., 1998. REVEAL, a general reverse engineering algorithm for inference of genetic network architectures. Proc. Pac. Symp. on Biocomputing. 3, 18-29.

Liu, F., Malaval, L., and Aubin, J.E., 1997. The mature osteoblast phenotype is characterized by extensive plasticity. Exp. Cell Res. 232, 97-105.

Liu, F., Malaval, L., and Aubin, J.E., 2003. Global amplification polymerase chain reaction reveals novel transitional stages during osteoprogenitor differentiation. J. Cell. Science. 116, 1787-1796.

Madras, N., Gibbs, A.L., Zhou, Y., Zandstra, P.W., and Aubin, J.E., 2002. Modeling stem cell development by retrospective analysis of gene expression profiles in single progenitor-derived colonies. Stem Cells, 20, 230-240.

Malaval, L., Liu, F., Roche, P., and Aubin, J.E., 1999. Kinetics of osteoprogenitor proliferation and osteoblast differentiation in vitro. J. Cell. Biochem. 74: 616-627.

McAdams, H. H., and Arkin, A., 1997. Stochastic mechanisms in gene expression. Proc. Nat'l. Acad. Sci (USA), 94, 814-819.

McAdams, H. H., and Arkin, A., 1999. Genetic Regulation at the Nanomolar Scale: It's a Noisy Business! Trends in Genetics. 15, 65-69.

Metropolis, N. Rosenbluth, A.W. Rosenbluth, M.N. Teller, A.H. and Teller. E. 1953. Equations of State Calculations by Fast Computing Machines. Journal of Chemical Physics. 21, 1087-1091.

Pearl, J., 2000. Causality: models, reasoning, and inference. Cambridge, U.K; New York: Cambridge University Press.

Perneger, T.V., 1998. What's wrong with Bonferroni adjustments British Medical Journal. 316, 1236-1238.

Pradines, H. J., Dolnik, M., and Collins, J.J., 2000. Noise-based switches and amplifiers for gene expression. Proceedings of the National Academy of Sciences USA 97: 20752080 (2000).

Schreiber, T., and Schmitz, A., 1996. Improved Surrogate Data for Nonlinearity Tests Phys. Rev. Lett. 77(4), 635-638.

Shannon, C.E., 1948. A mathematical theory of communication. Bell System Technical Journal. 27, 379-423.

Shmulevich, E.R. Dougherty, and W. Zhang, "From Boolean to probabilistic Boolean networks as models of genetic regulatory networks," Proceedings of the IEEE, Vol. 90, No. 11, pp. 1778-1792, 2002.

Spirtes, P., Glymour, C., and Scheines, R., 2001. Causation, Prediction, and Search, 2nd edition, MIT Press, Boston.

Stein, G.S., and Lian, J.B., 1993. Molecular Mechanisms Mediating Proliferation/Differentiation Interrelationships During Progressive Development of the Osteoblast Phenotype. Endocrine Reviews. 14(4), 424-442.

Theiler, J., and Prichard, D., 1995. Constrained-Realization Monte-Carlo method for Hypothesis Testing. Los Alamos, Tech. Rep. LA-UR-95-990.

Tyson, J.J., Chen, K., and Novak, B., 2001 Network dynamics and cell physiology Nat. Rev. Mol. Cell Biol. 2(12), 908-16.

Wayne, M.L., and McIntyre, L.M., 2002. Combining mapping and arraying: An approach to candidate gene identification Proc. Nat'l. Acad. Sci. USA. 99 (23) 14903-14906.

Wennberg, C., Hessle, L., Lundberg, P., Mauro, S., Marisawa, S., Lerner, U.H., and Millan, J.L., 2000. Functional characterization of osteoblasts and osteoclasts from alkaline phosphatase knock-out mice. J. Bone Miner. Res. 15, 1879-1888.

Yagil, G., and Yagil, E. 1971. On the relation between effector concentration and the rate of induced enzyme synthesis. Biophys. J. 11, 11-27.