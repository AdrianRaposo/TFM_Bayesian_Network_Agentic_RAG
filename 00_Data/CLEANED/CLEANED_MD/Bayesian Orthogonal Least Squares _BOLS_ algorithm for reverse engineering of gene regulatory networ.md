# Bayesian Orthogonal Least Squares (BOLS) algorithm for reverse engineering of gene regulatory networks 

## Chang Sik Kim*

Address: Bioinformatics Group, Turku Centre for Computer Science, Turku, Finland
Email: Chang Sik Kim* - cskim@kangwon.ac.kr

* Corresponding author

Published: 13 July 2007
Received: 21 October 2006
BMC Bioinformatics 2007, 8:251 doi:10.1186/1471-2105-8-251
Accepted: 13 July 2007
This article is available from: http://www.biomedcentral.com/1471-2105/8/251
(c) 2007 Kim; licensee BioMed Central Ltd.

This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


#### Abstract

Background: A reverse engineering of gene regulatory network with large number of genes and limited number of experimental data points is a computationally challenging task. In particular, reverse engineering using linear systems is an underdetermined and ill conditioned problem, i.e. the amount of microarray data is limited and the solution is very sensitive to noise in the data. Therefore, the reverse engineering of gene regulatory networks with large number of genes and limited number of data points requires rigorous optimization algorithm.


Results: This study presents a novel algorithm for reverse engineering with linear systems. The proposed algorithm is a combination of the orthogonal least squares, second order derivative for network pruning, and Bayesian model comparison. In this study, the entire network is decomposed into a set of small networks that are defined as unit networks. The algorithm provides each unit network with $\mathrm{P}\left(\mathrm{D}_{1} \mid \mathrm{H}_{1}\right)$, which is used as confidence level. The unit network with higher $\mathrm{P}\left(\mathrm{D}_{1} \mid \mathrm{H}_{1}\right)$ has a higher confidence such that the unit network is correctly elucidated. Thus, the proposed algorithm is able to locate true positive interactions using $\mathrm{P}\left(\mathrm{D}_{1} \mid \mathrm{H}_{1}\right)$, which is a unique property of the proposed algorithm.
The algorithm is evaluated with synthetic and Saccharomyces cerevisiae expression data using the dynamic Bayesian network. With synthetic data, it is shown that the performance of the algorithm depends on the number of genes, noise level, and the number of data points. With Yeast expression data, it is shown that there is remarkable number of known physical or genetic events among all interactions elucidated by the proposed algorithm.
The performance of the algorithm is compared with Sparse Bayesian Learning algorithm using both synthetic and Saccharomyces cerevisiae expression data sets. The comparison experiments show that the algorithm produces sparser solutions with less false positives than Sparse Bayesian Learning algorithm.
Conclusion: From our evaluation experiments, we draw the conclusion as follows: 1) Simulation results show that the algorithm can be used to elucidate gene regulatory networks using limited number of experimental data points. 2) Simulation results also show that the algorithm is able to handle the problem with noisy data. 3) The experiment with Yeast expression data shows that the proposed algorithm reliably elucidates known physical or genetic events. 4) The comparison experiments show that the algorithm more efficiently performs than Sparse Bayesian Learning algorithm with noisy and limited number of data.

## Background

High-throughput technologies such as DNA microarrays provide the opportunity to elucidate the underlying complex cellular networks. There are now many genome-wide expression data sets available. As an initial step, several computational clustering analyses have been applied to expression data sets to find sets of co-expressed and potentially co-regulated genes [1-5]. As a next step, there have been efforts to elucidate gene regulatory networks (GRN) embedded in complex biological systems. A growing number of methods for reverse engineering of GRN have been reported as follows: Boolean networks [6,7], Bayesian networks [8-10], Algorithm for the Reconstruction of Accurate Cellular Networks (ARACNe) [11], linear models [12], neural networks [13], methods using ordinary differential equations [14,15], a sparse graphical Gaussian model [16], a method using a genetic algorithm [17], a method using Sparse Bayesian Learning (SBL) algorithm [18,19], and etc.

In the reverse engineering of GRN, essential tasks are developing and comparing alternative GRN models to account for the data that are collected (Figure 1). There are two levels of inference involved in the task of data modeling process [20]. The first level of inference is fitting one of models to the data with an assumption that our chosen model is true. The second level of inference is the task of model comparison. It is desired to compare the alternative models with the help given by the data, and give some level of preference to the alternative models. Thus, the reverse engineering method should be used as a framework for fitting several different GRN models to the data to compare the models. For instance, there are several GRN modeling studies in which the reverse engineering algorithm could be applied: 1) system of ordinary differential equation (ODE) [15], 2) Dynamic Bayesian networks based methods (DBN) [10,18], 3) a linear stochastic differential equation for a transcriptional regulatory network [14], and etc. It is noted that these three models can be represented by linear systems. By a "linear system", we mean a system represented as a linear equation in matrix form such as Eq. 2 in methods section.

Microarrays have been used to measure genome-wide expression patterns during the cell cycle of different eukaryotic and prokaryotic cells. The review paper of Cooper and Shedden [21] presents various published microarray data sets, which have been interpreted as showing that a large number of genes are expressed in a cell-cycle-dependent manner. From this point of view, it is assumed that the underlying GRN is dependent upon cellcyclic time. Therefore, this study uses the DBN because it can represent how the expression levels evolve over time.
![img-0.jpeg](img-0.jpeg)

Figure I
The Bayesian Orthogonal Least Squares algorithm could be used as a framework for gene regulatory study including the collecting and modeling of data.

In this paper, we address two main challenges in reverse engineering with linear systems and present a novel algorithm to overcome these difficulties. Firstly, reverse engineering of GRN will be computationally less challenging task if significantly large amount of experimental data is available. However, this is limited due to the expensive cost of microarray experiments. This problem makes the reverse engineering of GRN to be underdetermined, which means that there is substantially greater number of genes than the number of measurements. Secondly, reverse engineering of GRN with linear systems is ill conditioned because small relative changes in design matrix E in Eq. 2 due to the noise make substantially large changes in the solution. Therefore, the reverse engineering algorithm named as Bayesian orthogonal least squares (BOLS) is developed to overcome these difficulties. The BOLS method is created by combining three techniques: 1) Orthogonal Least Squares method (OLS) [22], 2) second order derivative for network pruning [23], and 3) Bayesian model comparison [20].

We evaluate the BOLS method by inferring GRN from both synthetic and Yeast expression data. We provide the performance comparison between BOLS and one of state-of-the-art reverse engineering methods, SBL algorithm [24]. The SBL algorithm has been recently used in GRN studies with linear systems [18,19]. For evaluation with Yeast expression data, we validate the inferred GRN using

the information from the database that contains large data sets of known biological interactions.

## Results and discussion

## Case study I: In silico experiment

Our in silico experiment follows the methodology for the generation of synthetic expression dataset for systems of DBN as used in Rogers and Girolami [19]. We generate synthetic networks using power-law distribution. To create a network structure, we decompose the entire network into a set of small networks that are defined as unit network and proceed a unit network by a unit network. Figure 2 presents a unit network consisting of a target gene and a list of genes as regulators. It should be noted that there is no requirement for the network to be acyclic. All created unit networks will be combined to create a whole GRN. The combination of all (or selected) unit networks is straightforward process based on the definition of a graph (see Methods section). This unit network approach is similar to the approach adopted in Bayesian network based methods [9,25] and SBL based method [19]. For each target gene, we sample the number of genes (m_{i}) regulating this target gene from the approximate power distribution

$$
P\left(m_{i}\right)= \begin{cases}M^{-1} m_{i}^{-\eta} & m_{\min } \leq m_{i} \leq m_{\max } \\ 0 & \text { otherwise }\end{cases}
$$

where the normalization constant is given by

$$
M=\sum_{i=m_{\min }}^{m_{\max }} m_{i}^{-\eta}
$$

Following Rogers and Girolami [19], Wagner [26], and Rice et al. [27], the constant $\eta$ is set to $2.5 . \mathrm{m}_{\text {max }}$ (or $\mathrm{m}_{\text {min }}$ ) is the maximum (or minimum) number of allowed regulator genes in a unit network respectively. The condition $\mathrm{m}_{\max }<<\mathrm{K}$ (the number of genes) ensures the sparseness of the synthetic network. Note that $\mathrm{m}_{\text {max }}$ is set to 4 for all experiments. The more details of creating synthetic network can be found from the supplementary information of Rogers and Girolami's study [19]. In this study, the Matlab code from Rogers and Girolami's study for creating synthetic network is used, which is available from [28]. We first randomly generate the synthetic networks unit network by unit network to combine them for a whole GRN, and then we generate the synthetic expression data with randomly generated synthetic GRN. Using these synthetic expression data, we infer the network with BOLS and the simulated data set. It should be noted that BOLS and the generation method of synthetic networks are not cooperative to work because the generation and inference of networks are completely separate processes.
![img-1.jpeg](img-1.jpeg)

Figure 2
The schematic of unit network. (a) Input unit network consisting of target gene $\mathbf{Y}_{\mathbf{i}}$ and all other genes as regulator candidates. (b) Output unit network consisting of target gene $\mathbf{Y}_{\mathbf{i}}$ and its most probable regulators.

In this experiment, the synthetic expression data is generated based on DBN using Eq. 1, in which the expression data are evolved over the time. However, as the simulation process is continued over the time, the expression data diverge by constantly either increasing or decreasing. Thus, we collect a single time point only after the expression data are simulated for a certain period of time (from $\mathrm{t}=0$ to $\mathrm{t}=\mathrm{T}$ ) to avoid expression levels being too high. We proceed in a single time point by a single time point manner. For a single time point, the generation of expression data is started with initial synthetic data. For each gene, the initial condition is assigned with random number between 0 and 1 . With given initial condition, we simulate the expression data for each gene i from $\mathrm{t}=0$ to $\mathrm{t}=\mathrm{T}$ using Eq. 1. We take the measure with $\mathrm{t}=\mathrm{T}$-1 for design matrix E and with $\mathrm{t}=\mathrm{T}$ for $\mathrm{Y}_{\mathrm{i}}$ in Eq. 2. We repeat these process N times to collect N data points and apply the reverse engineering algorithms to reconstruct the synthetic network.

We make the performance comparison between BOLS and SBL methods to show the efficiency of BOLS method. The SBL method is one of the state-of-the-art algorithms, which has been recently applied to GRN studies with linear systems [18,19]. We use the Matlab code of SBL algorithm that is available from [29]. At first, we investigate the effect of the number of data points ( $N=20,40,60,80$, 100) and noise ( $\varepsilon=0.01,0.05,0.1$ ) on the performance using synthetic GRN and expression data with fixed number of genes ( $\mathrm{K}=100$ ). Sensitivity and complementary specificity are used as measures for the performance of the algorithm [9,19,27]. We compute the sensitivity = $\mathrm{TP} /(\mathrm{TP}+\mathrm{FN})$ and the complementary specificity $=\mathrm{FP} /(\mathrm{TN}$ $+\mathrm{FP})$, where TP is the number of true positive, FN is the number of false negative, FP is the number of false positive, and TN is the number of true negative. In other words, the sensitivity is the proportion of recovered true positive interactions and the complementary specificity is the proportion of false positive interactions. To investigate the variability of test results, we have run both algorithms 20 times with same control parameters, i.e. the number of data points, noise, and etc. For each run, new random synthetic network has been created. We find that the sensitivity and the complementary specificity are constant over 20 experiments with small variability (see Table 1). The systematic effect of noise and the number of data points on the performance can be analyzed from Table 1. As the number of data points increases with the fixed number of genes and noise level $\varepsilon$, the performance of both algorithms increase. As noise level $\varepsilon$ increases, the performance of both algorithms decreases. For the number of data points $\geq 80$, the sensitivity of SBL is slightly greater than BOLS and the complementary specificity of SBL is significantly greater than the ones of BOLS. It means that BOLS algorithm produces significantly smaller proportions of false positive interactions than SBL algorithm. It should be noted that results from SBL algorithm with $\mathrm{N}=20,40$, and 60 are not available because the Matlab code of SBL algorithm dose not run when the number of data points N is relatively low. SBL algorithm includes the Cholesky factorization of their Hessian matrix that is required to be positive definite. Note that the Hessian matrix is consisted of design matrix and hyperparameters [24]. When the number of data points is relatively smaller than the number of genes in the data set, this Hessian matrix becomes non positive definite. Our experiments show that SBL algorithm is not suitable for the reverse engineering with limited number of data points and it doesn't even run with significantly limited number of data points. On the other hand, BOLS algorithm produces relatively small proportion of FP interactions with limited number of data points. It should be noted that Rogers and Girolami [19] generate 2R expression levels for each gene in each knock-out experiment-R in the normal (wild type) system and R in the knock-out
(mutant) system. In a network of K genes, in which each is knocked out individually, they have 2 RK data points. Since the evaluation of BOLS with Rogers and Girolami's knockout approach [19] is beyond the scope of the objectives of our study, i.e. the underdetermined problem using DBN model, we provide the comparisons between BOLS and SBL based on their approach as Additional file 1.

We use the receiver operating characteristic (ROC) analysis [19] to characterize the trade-off between the proportions of true and false positive interactions with limited number of data points ( $\mathrm{N}<20$ and $\mathrm{K}=100$ ) in Figure 3. This ROC analysis shows that BOLS algorithm produces the solution with extremely small proportion of false positive interactions when the number of data points is extremely small. We also analyze the effect of the number of gene K with limited number of data points $\mathrm{N}=10$. In Figure 4, it is shown that the performance of BOLS algorithm decreases as K increases from 100 to 300 . Therefore, it can be concluded that performance of the proposed algorithm is dependent on $\mathrm{K}, \mathrm{N}$, and $\varepsilon$.

From the experiments, it is shown that BOLS produce solutions with significantly low complementary specificity regardless of $\mathrm{K}, \mathrm{N}$, and $\varepsilon$, because Bayesian model selection scheme is efficiently enough to discover the optimal solution. Since we do not have any information on noise in the data, we completely over-fit the data to DBN model using OLS as a first step. Then, we remove the unnecessary inferred parameters (the inferred parameters that are related with "noise") to obtain the optimal solution by a trade-off between minimizing the natural complexity of inferred GRN and minimizing the data misfit. As the complexity of inferred GRN decreases with network pruning process, we use the Bayesian model selection to select the most optimal solution. It should be noted that the Bayesian model selection includes Occam's factor, which automatically suppresses the tendency to discover spurious structure in data. Thus, we can say that BOLS is efficient to infer GRN with significant small portion of FP interactions with the noisy and limited number of data set for DBN. In Figure 5, we present an example showing that the performance of BOLS increases as the network pruning step proceeds. We first generate the synthetic networks of 50 genes ( N ) and then simulate 20 data points ( K ) with this networks and noise level $\varepsilon=0.1$. We concentrate on an output unit-network with highest evidence value $\log \mathrm{P}(\mathrm{D} / \mathrm{H})$, for evaluation. It should be reminded that as the network pruning continues the number of inferred interactions in the unit network decreases. Figure 5b shows that the number of errors ( $\mathrm{FP}+\mathrm{FN}$ ) decreases, as the network pruning proceeds. The complementary specificity also decreases along the network pruning (Figure 5c). On the other hand, the sensitivity remains constant, which is equal to 1 (Figure 5d). It means that the over-fitted solu-

Table I: Sensitivity and complementary specificity for BOLS and SBL algorithms


$\mathrm{N}=$ is the number of data points, and $\varepsilon$ the noise level. $m_{\max }$ is set to 4 and the number of genes $K 100$. tions after OLS step contain only TP and FP interactions (no FN interactions). It is observed that the number of errors and the complementary specificity converge at 0 as the network pruning process proceeds, in which the unit network has the highest evidence $\log \mathrm{P}\left(\mathrm{D} \mid \mathrm{H}*{1}\right)$ (Figure 5a). Therefore, it can be concluded that the OLS method can cope with underdetermined problems using noisy data, provided that the method is combined with network pruning process and Bayesian model selection techniques.

The BOLS algorithm should be run K times producing K unit networks, which are combined to build the whole network. Each unit network is assigned with $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}*{1}\right)$. For each unit network, we compute the number of errors $=\mathrm{FN}$ $+\mathrm{FP}$. The relationship between $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}*{1}\right)$ and the number of errors for each unit-networks is shown in Figure 6. The number of errors decreases as the number of data points increases on the synthetic data. Unit networks with higher $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}*{1}\right)$ s are more accurate than those with lower $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}*{1}\right)$ s. This signifies that unit networks with higher $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}*{1}\right)$ s have a higher confidence that unit networks are correctly reconstructed. Thus, when low numbers of data points and extremely high numbers of genes are given, the algorithm should be able to recover a partially correct network with unit networks only having relatively high $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}*{1}\right)$ s. It should be noted that BOLS algorithm does not provide the confidence levels among interactions inside unit network. However, it can be noticed from Figure 6 that many unit networks with relatively high evidence values have zeroed number of incorrectly inferred interactions. Therefore, the evidence values for unit networks are efficient enough to cope with problems for locating unit networks without FP or FN interactions.

## Case study 2: Application of BOLS to Saccharomyces cerevisiae data

To evaluate our algorithm for reverse engineering of GRN, we use the microarray data from Spellman et al. [30], in which they created three different data sets using three different synchronization techniques. We focus our analysis using the data set produced by $\alpha$ factor arrest method. Here we concentrate on our study with the expression data set of 20 genes known to be involved in cell cycle regulation [31]. Thus, we have a data set with 20 genes and 17 data points in this experiment. Based on the previous

![img-2.jpeg](img-2.jpeg)

**Figure 3**

ROC analysis of BOLS output with K = 100. (a) N = 5 and ε = 0.01, (b) N = 5 and ε = 0.05, (c) N = 5 and ε = 0.1, (d) N = 10 and ε = 0.01, (e) N = 10 and ε = 0.05, (f) N = 10 and ε = 0.1, (g) N = 15 and ε = 0.01, (h) N = 15 and ε = 0.05, (i) N = 15 and ε = 0.1. For all Figures, the x-axis corresponds to the complementary specificity, the y-axis sensitivity.

Simulation experiment, it is expected to have sensitivity as 0.967 (ε = 0.01), 0.937 (ε = 0.05), 0.919 (ε = 0.1) and complementary specificity as 0.022 (ε = 0.01), 0.019 (ε = 0.05), 0.029 (ε = 0.1), respectively. It means that the output is expected to have approximately less than 3% of complementary specificity if we assume that ε ≤ 0.1, the sparseness mmax of GRN = 4, and etc.

The output unit networks using this data set are presented in Table 2 including the P(D|H) of unit networks, in which there are 107 inferred interactions from BOLS. Among those interactions, 45 of them are identified as physical or genetic interactions from the BioGRID database [32]. Later in this section, we provide the logical basis such that some of unidentified interactions might be possible physical or genetic events. BioGRID is a freely accessible database including physical or genetic interactions from the *Saccharomyces cerevisiae* available at [33]. The output in Table 2 shows that the interactions with higher P(D|H) have higher likelihood of having known physical or genetic interactions identified from the BioGRID than the interactions with lower P(D|H)5: 1) Among the elucidated interactions with P(D|H) > 66th percentile of all P(D|H)5, 23 of them are identified as physical or genetic interactions from BioGRID database. 2) Among the elucidated interactions with 66th percentile > P(D|H)5 > 33rd percentile, 14 of them are identified as physical or genetic interactions, 3) Among the elucidated interactions with P(D|H)5 < 33rd percentile, 8 of them are identified as physical or genetic interactions. This could be explained from the previous simulation experiment showing that BOLS has less false positive interactions with relatively high P(D|H) than with low P(D|H). It is noted that the overall values of P(D|H) in Table 2 are relative small compared to the ones in Figure 6. It should be noted that number of genes is set to 20 in Table 2 and the number of genes is set to 100 in Figure 6. From Figure 6, it is also noted that the overall values of P(D|H) decreases as the number of data points decreases. It is also found that the overall values of P(D|H) decreases as the noise level increases. Therefore, the overall values of P(D|H) can be relatively different depending on the number of genes, noise level, and the number of data points.

We pool both physical and genetic interactions from BioGRID to validate the output interactions in this experiment. The rationale for this pooling can be described as follows. Several proteins join together to form multi-protein complex having certain functions or regulating other proteins. For example, SCF complex consists of Skp, Cullin, and F-box proteins, which promotes G1-S transition by targeting G1 cyclins and Cln-Cdk inhibitor Sic1 for degradation. From Breeden's [34] review study, it is known that cell cycle regulated complexes with at least one sub-unit are regulated at the transcript level. This means that certain protein complexes might regulate other complexes with time delay. With only expression data sets, we only have information that which proteins are present for certain time. In terms of efficiency and log-

![img-3.jpeg](img-3.jpeg)

**Figure 5**

The changes of performance of BOLS as the network pruning step proceeds. The simulation experiment is done with N = 50, K = 20, and ε = 0.1. In these Figures, we concentrate on an output unit-network that has the highest logP(D|H<sub>i</sub>) among all output unit networks. For all Figures, the x-axis corresponds to the number of inferred interactions: as the network pruning proceeds, the number of inferred interactions in unit network decreases. Each y-axis corresponds to (a) logP(D|H<sub>i</sub>), (b) the number of errors (FP+FN), (c) the complementary specificity, (d) the sensitivity.

![img-4.jpeg](img-4.jpeg)

**Figure 6**

The relationship between the evidence value P(D|H<sub>i</sub>) and the number of errors for unit networks, where K = 100, ε = 1.0e-2, and m<sub>max</sub> = 4. (a) N = 10, (b) N = 15, (c) N = 20. For all Figures, the x-axis corresponds to log(P(D|H<sub>i</sub>)), the y-axis the number of errors.

ical order, it is assumed that the cell only makes the proteins when it is needed. If the proteins are made all the time, the cell could be inefficient in an environment without the substrates of the protein [21]. From these points of view, there can be two possible cases to be considered when certain two proteins are present: 1) two proteins form a multi-protein complex by interacting each other, 2) One protein might form a complex with some other proteins. This complex might regulate the other protein that could also form a protein complex. Therefore, those two types of interactions can be pooled together to validate the output interactions.

Unit-networks having relatively many identified physical or genetic interactions are the ones with Cln3, Cln2, Clb5, Cln1, Cdc28, Swi6, Cdc53 and Cdc34 as target genes. For example, we present a unit network with Cdc28 as a target gene. Cdc28 is identified as having physical or genetic interactions with Cln1 [35-40], Cln2 [36-49], Cln3 [47,50-55], Clb1 [35,56,57], Clb2 [35,38,41,58-64], Clb4 [56,57,61], Hct1 [38,53,63,65-67], Sic1 [37,53,61,68-71], Cdc20 [53,67], Swi5 [53], and Swi6 [53,72]. Cdc28 is a catalytic subunit of the main cell cycle cyclin-dependent kinase (CDK), which alternatively associates with G1 cyclins (Cln1, Cln2, and Cln3) and G2/M cyclins (Clb1, Clb2, and Clb4) that direct the CDK to specific substrates. Hct1 (Cdh1) and Cdc20 are cell cycle regulated activators of the anaphase-promoting complex/cyclosome (APC/C), which direct ubiquitination of mitotic cyclins. One of Cdc28's Gene Ontology definitions gives another evidence that Cdc28 might have associations with Hct1 and Cdc20, because Cdc28 is involved in the progression from G1 phase to S phase of the mitotic cell cycle. Sic1 is an inhibitor of Cdc28-Clb kinase complexes that controls G1/S phase transition, which prevents premature S phase and ensuring genomic integrity.

Among the list of genes inside Cdc28 unit network, there are several genes not identified as having physical or genetic interactions with Cdc28 from the BioGRID: Clb6, Mbp1, Mcm1, Cdc34, Cdc53 and Skp1. However, the definitions of these genes from the BioGRID give enough evidences such that some of them indirectly interact with Cdc28. For example, Clb6 is a B-type cyclin involved in DNA replication during S phase, which activates Cdc28 to promote initiation of DNA synthesis. Clb6 also has a role for the formation of mitotic spindles along with Clb3 and Clb4. Thus, Clb6 indirectly regulates Cdc28 along with Clb4. Cdc53, Cdc34 and Skp1 also indirectly regulate Cdc28 through Sic1. They form a structural protein of SCF complexes, called cullin, with an F-box protein. The SCF promotes the G1-S transition by targeting G1 cyclins and the Cln-Cdk inhibitor Sic1 for degradation. Mbp1 is a transcription factor involved in regulation of cell cycle progression from G1 to S phase, which forms a complex

Table 2: The output unit networks of BOLS with $\log \left(P\left(D \mid H_{i}\right)\right)$


(X)s indicate that the regulator gene is identified as having known interactions with its target gene from the BioGRID database, which is a freely accessible database of physical and genetic interactions available at [33]. with Swi6 that binds to Mull cell cycle box regulatory element in promoters of DNA synthesis genes. Thus, Mbp1 is associated with Cdc28 by forming a complex with Swi6.

For another example, we present a unit network having Clb5 as target gene. Clb5 is identified as having physical or genetic interactions with Clb6 [73-79], Sic1 [41,61,71,80-82], Clb2 [83], Cdc20 [84], Cln3 [75], Hct1 [63,85], Swi4 [75,86], and Swi6 [86].

Among the list of genes inside Clb5 unit network, there are several genes not identified as having physical or genetic interactions with Clb5: Cln2, Clb1, Mcm1, Mbp1, Swi5 and Clb4. However, there are evidences that some of genes in the list might have indirect interactions with Clb5. For example, Clb4 has an association with Clb5, because Clb5 is a B-type cyclin involved in DNA replication during S phase and has a role for the formation of mitotic spindles along with Clb3 and Clb4. For another

![img-5.jpeg](img-5.jpeg)

**Figure 7**

The inferred GRN by both BOLS and SBL are compared with the same expression data used in Table 2. (a) A GRN by BOLS, (b) A GRN by SBL, (c) The inferred interactions both by BOLS and SBL, (d) The inferred interactions only by BOLS, (e) The inferred interactions only by SBL. For all figures, the solid line correspond to the inferred interactions which are identified as known physical or genetic interactions from the BioGRID database, and the dashed line the unknown interactions.

example, Mbp1 and Clb5 have an indirect interaction. Mbp1 is a transcription factor involved in regulation of cell cycle progression from G1 to S phase, which forms a complex with Swi6 that binds to MluI cell cycle box regulatory element in promoters of DNA synthesis genes. It is already identified that Swi6 regulates Clb5. Thus, Mbp1 indirectly regulate Clb5 through Swi6.

We also evaluate both BOLS and SBL using the same data set in Table 2 to compare the efficiency of BOLS with SBL. For direct comparison purposes, we make the graphs of inferred GRN by BOLS and SBL (Figure 7). There are 107 inferred interactions (45 of them are identified as known interactions from the database) by BOLS (Figure 7a) and 116 interactions (38 of them are known interactions) by SBL (Figure 7b). Figure 7c shows that 62 interactions are inferred by both BOLS and SBL, in which 32 of them are known interactions. Figure 7d shows 45 interactions only by BOLS in which 13 of them are identified as known interactions from the database. On the other hand, Figure 7e shows 54 interactions only by SBL in which only 6 of them are known interactions from the database. It is reasonable to assume that the complete information of biological interactions of Yeast is not available from the database yet. It is believed that the more depositions of the information concerning Yeast interactions are still on the way to reach the more complete understanding of the underlying complex cellular networks of Yeast. Based on the currently available information from the database, we can say that SBL algorithm infers GRN with relatively more complexity and less identified known interactions than BOLS. Therefore, based on our evaluation experiments with synthetic and Yeast expression data, it is sufficient to conclude that SBL produces more over-fitting solutions (i.e., more FP solutions) than BOLS.

# **Conclusion**

In the evaluation of BOLS using synthetic data, it is shown the proposed BOLS algorithm is able to reconstruct networks using a very limited number of experimental samples. In this study, we assume that there is significantly limited number of data points and the noise level in the data is not known. This is a common situation in expression data analysis. To handle these difficulties, we adopt a decomposition strategy to break down the entire network into a set of unit networks. This decomposition makes the inferring of a whole GRN into several separate regressions. Thus, if we have extremely small number of data points,

our method can not provide $100 \%$ correct solutions, but provides each unit network with $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}_{\mathrm{i}}\right)$, which can be used as confidence level. The unit network with a higher $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}_{\mathrm{i}}\right)$ has a higher confidence such that the unit network is correctly inferred (Figure 5). Previously, Basso et al. [11] validated their ARACNe algorithm using 19 nodes synthetic network. With 350 sample size, the sensitivity and complementary specificity are approximately $80 \%$ and $20 \%$, respectively. The inferred interactions from their method contain approximately $20 \%$ false positive and false negative interactions, respectively. With our method, it is possible to locate false positive or false negative interactions with $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}_{\mathrm{i}}\right) \mathrm{s}$, which is the unique property of BOLS algorithm. Our in silico experiment shows that the performance depends on the number of data points, genes, and noise level. Further study will be required to investigate the relationship between these parameters and the performance so that the BOLS algorithm can be generally applied to the microarray data with any number of genes, data points, and noise level.

Another evaluation is conducted with the Yeast Saccharomyces cerevisiae data of 20 genes, which are involved in cell-cycle regulation. In the output network, there is noticeable number of interactions that are identified as physical or genetic interactions from the literature. There are also several interactions that are not identified from the literature. However, it is shown that the definition of these genes from the BioGRID database gives enough evidences that some of them have indirect interactions. Thus, this experiment shows that BOLS algorithm is able to elucidate remarkable number of known physical or genetic events.

For both evaluation experiments with synthetic and Yeast expression data, we compare the performance between BOLS and SBL algorithms. The SBL algorithm [18,19,24] is a general Bayesian framework to obtain sparse solutions utilizing linear models. This method is known as type-II maximum likelihood method [24], in which the solutions are obtained by maximizing the marginal likelihood. On the other hand, BOLS utilizes the Bayesian model selection that is an extension of maximum likelihood model selection, in which the posterior is obtained by multiplying the best fit likelihood by the Occam's factor. From our both evaluation experiments, it is concluded that BOLS produces sparser solutions with less FP than SBL does.

## Methods

## I. Gene regulatory network model and Unit networks

To study GRN, we choose a system of DBN as our GRN model. This model is described by

$$
e_{i}(t+1)=\sum_{j=1}^{K} w_{i j} e_{j}(t)+\xi_{i}(t) \text { for } t=1,2, \ldots, N-1
$$

Here N is the number of data points, K is the number of gene in the data, and $\xi_{\mathrm{i}}(\mathrm{t})$ is a noise at any time. The $\mathrm{e}_{\mathrm{i}}(\mathrm{t}) \mathrm{s}$ are the level of mRNAs at any given time $t$, which influences the expression levels of the gene. The value $\mathrm{w}_{\mathrm{ij}}$ describes the interaction strength between the $\mathrm{j}^{\text {th }}$ gene and the $\mathrm{i}^{\text {th }}$ gene. This model has the first order Markov property, which means that the future expression $e_{i}(t+1)$ is independent of the past expression level $e_{i}(t-1)$ given the present expression level $e_{i}(t)$. As briefly mentioned in the previous section, it is required that the data set is reorganized into a linear system to reverse engineer GRN using BOLS algorithm. This GRN model can be easily rewritten into a linear system as

$$
Y_{i}=E w_{i}+n_{i}
$$

where $\mathrm{i}=1,2, \ldots, \mathrm{~K}$. $w_{i}$ is a column matrix of regulation strength values, which is defined as $w_{i}=\left[\mathrm{w}_{i 1}, \mathrm{w}_{i 2}, \ldots \ldots\right.$, $\left.\mathrm{w}_{\mathrm{ik}}\right]^{\mathrm{T}} . Y_{i}$ is a column matrix of expression levels for target genes, which is defined as $Y_{i}=\left[e_{i}(2), e_{i}(3), \ldots, e_{i}(N)\right]^{\mathrm{T}} . E$ is a $\mathrm{N}-1 \times \mathrm{K}$ design matrix, which is defined as $E=\left[\mathrm{e}_{1}, \mathrm{e}_{2}, \ldots \ldots\right.$, $\mathrm{e}_{\mathrm{K}}$ ] and $\mathrm{e}_{\mathrm{i}}=\left[\mathrm{e}_{\mathrm{i}}(1), \mathrm{e}_{\mathrm{i}}(2), \ldots \ldots, \mathrm{e}_{\mathrm{i}}(\mathrm{N}-1)\right]^{\mathrm{T}} . n_{i}$ is an Gaussian noises, which is defined as $n_{i}=\left[n_{i}(1), n_{i}(2), \ldots, n_{i}(N-1)\right]^{\mathrm{T}}$.

It should be noted that the expression levels $e_{i}(t)$ s in both Eq. 1 and 2 are same and noisy ones. Eq. 1 describes that the current expression levels $e_{i}(t)$ s are determined depending on the previous ones $e_{i}(t-1)$ and noises $\xi_{i}(t-1)$ and the expression levels are evolved over the time based on the GRN. Hence, $\xi_{i}(t)$ is a noise added into $e_{i}(t)$ s during the generation of synthetic or real expression levels based on DBN model. Once the "noisy" expression levels are available, we consider Eq. 2 for reverse engineering of GRN. Because the given expression levels $e_{i}(t)$ s in Eq. 2 are noisy, we should have a condition such that $\left|Y_{i}-E w_{i}\right|=\left|n_{i}\right|$ $>0$. If $n_{i}=0$, we will have over-fitting solutions, in which model fitting oscillates widely so as to fit the noise. Thus, we can say that $n_{i}$ is a noise related with "data misfit" or "confidence interval" on the best fit parameters. On the other hand, $\xi_{i}(t)$ is a noise related with the "generation" of expression levels. If $n_{i}$ is modeled as zero-mean Gaussian noise with standard deviation $\sigma_{n}$, the probability of the data given the parameter $w_{i}$ is

$$
P\left(D \mid w_{i}, \beta\right)=\frac{\exp \left(-\beta E_{D}\left(D \mid w_{i}\right)\right)}{Z_{D}(\beta)}
$$

where $\beta=1 / \sigma_{n}{ }^{2}, \mathrm{E}_{\mathrm{D}}=\left(\mathrm{Y}_{\mathrm{i}}-\mathrm{Ew}_{\mathrm{i}}\right)^{\mathrm{T}}\left(\mathrm{Y}_{\mathrm{i}}-\mathrm{Ew}_{\mathrm{i}}\right)$, and $\mathrm{Z}_{\mathrm{D}}=(2 \pi / \beta)^{\mathrm{N} /}$ ${ }^{2} . \mathrm{P}\left(\mathrm{D} \mid \mathrm{w}_{\mathrm{i}}, \beta\right)$ is called the maximum likelihood. It is well known that maximum likelihood is underdetermined and

ill conditioned problems. Thus, we are motivated to develop a novel strategy to overcome these problems.

We decompose the entire network into a set of small networks that are defined as unit networks. Each unit network consists of one particular target gene and its regulator genes. The unit network is used as input and output of BOLS algorithm. Figure 2a presents an input unit network that includes all genes in the data set as regulator candidates. Figure 2b presents an output unit network that contains most probable regulator genes to the target gene. Thus, we can decompose the GRN into several separate regressions and apply the BOLS algorithm to each unit network. Therefore, for GRN with K number of genes, we will run the algorithm K times-producing a unit network for each time. It should be noted that we can use all unit networks to create whole GRN that consists of two finite sets, a set of nodes (genes) and a set of edges (interactions) such that each edge connects two nodes. With all (or selected) unit networks, the generation of GRN can easily be generalized by constructing a $K \times K$ graph matrix $\mathrm{G}=\left[\mathrm{g}_{\mathrm{i}, j}\right]$, with binary element
$g_{i, j}= \begin{cases}1 & \text { if gene } i \text { and gene } j \text { have regulatory relationship } \\ 0 & \text { otherwise. }\end{cases}$
Furthermore, this matrix induces a GRN, in which nodes corresponds to genes and an edge joins nodes $i$ and node $j$ if and only if $\mathrm{g}_{\mathrm{i}, j}=1$. For each edge, we store the information of unit network where it belongs. The information of these sets can be easily obtainable from all unit networks. Thus, the combination of all unit networks for creating whole GRN is easy and straightforward procedure.

## 2. Bayesian orthogonal least square algorithm

As briefly described in background section, reverse engineering with a linear system with limited data has to overcome two difficulties. In this section, we describe our efforts to overcome these challenges by developing BOLS algorithm.

The system is referred as underdetermined when the number of parameters is larger than the number of available data points, so that standard least squares techniques break down. This issue can be solved with the OLS [22] method involves decomposition of the design matrix into two using Gram-Schmidt Orthogonalization theory as,

$$
\mathrm{E}=\mathrm{XU}
$$

where $\mathrm{E}_{\mathrm{N}-1+\mathrm{K}}=\left[\mathrm{e}_{1}, \mathrm{e}_{2}, \ldots \ldots, \mathrm{e}_{\mathrm{k}}\right], \mathrm{X}_{\mathrm{N}-1+\mathrm{K}}=\left[\mathrm{x}_{1}, \mathrm{x}_{2}, \ldots \ldots, \mathrm{x}_{\mathrm{k}}\right]$ and $\mathrm{U}_{\mathrm{K}+\mathrm{K}}$ is a triangular matrix with 1's on the diagonal and 0 's below the diagonal, that is,

$$
U=\left[\begin{array}{cccccc}
1 & u_{12} & u_{13} & \cdots & u_{1 k} \\
0 & 1 & u_{23} & & u_{2 k} \\
0 & 0 & \ddots & \ddots & \vdots \\
\vdots & & \ddots & 1 & u_{k-1 k} \\
0 & \cdots & 0 & 0 & 1
\end{array}\right]
$$

Let's say that w is the regression parameter inferred by E and $g$ is the regression parameter inferred by $X$. It is noted that g and w satisfy the triangular system

$$
\mathrm{g}=\mathrm{Uw}
$$

The computational procedure of Gram-Schmidt method is described as

$$
\begin{aligned}
& x_{1}=e_{1} \\
& u_{i j}=x_{i}^{T} e_{j} /\left(x_{i}^{T} x_{i}\right), 1 \leq i \leq j \\
& x_{j}=e_{j}-\sum_{i=1}^{K-1} u_{i j} x_{i}, 2 \leq j \leq K
\end{aligned}
$$

Because $\mathrm{x}_{\mathrm{i}}$ and $\mathrm{x}_{\mathrm{j}}(\mathrm{i} \neq \mathrm{j})$ are orthogonal to each other, the sum of square of $Y$ is defined as

$$
Y^{T} Y=\left(x_{i}^{T} x_{i}\right) g_{i}^{2}+n_{i}^{T} n_{i}
$$

The variance of $Y_{i}$ is defined as

$$
Y^{T} Y / N-1=\left(x_{i}^{T} x_{i}\right) g_{i}^{2} / N-1+n_{i}^{T} n_{i} / N-1
$$

It is noticed that $\left(\mathrm{x}_{\mathrm{i}}^{\mathrm{T}} \mathrm{x}_{\mathrm{i}}\right) \mathrm{g}_{\mathrm{i}}^{2} / \mathrm{N}-1$ is the variance of $\mathrm{Y}_{\mathrm{i}}$ which is contributed by the regressors and $n_{i}{ }^{T} n_{i} / N-1$ is the noise (or unexplained) variance of $\mathrm{Y}_{\mathrm{i}}$. Hence, $\left(\mathrm{x}_{\mathrm{i}}{ }^{\mathrm{T}} \mathrm{x}_{\mathrm{i}}\right) \mathrm{g}_{\mathrm{i}}^{2} / \mathrm{N}-1$ is the increment to the variance of $\mathrm{Y}_{\mathrm{i}}$ contributed by $\mathrm{w}_{\mathrm{i}}$, and the error reduction ratio only due to $\mathrm{x}_{\mathrm{i}}$ can be defined as

$$
[\text { NError }]_{i}=\left(x_{i}^{\mathrm{T}} \mathrm{x}_{\mathrm{i}}\right) \mathrm{g}_{\mathrm{i}}^{2} /\left(\mathrm{Y}^{\mathrm{T}} \mathrm{Y}\right), 1 \leq \mathrm{i} \leq \mathrm{K}
$$

This error term provides a simple and efficient measure for seeking a subset of significant regression parameters in a forward-regression way. The repressor selection procedure from Chen et al. [22] is summarized as follows:

1) At the first step, for $1 \leq \mathrm{i}<\mathrm{K}$, compute

$$
\begin{gathered}
\mathrm{x}_{1}{ }^{(i)}=\mathrm{e}_{\mathrm{i}} \\
\mathrm{~g}_{1}{ }^{(i)}=\left(\mathrm{x}_{1}{ }^{(i)}\right)^{\mathrm{T}} \mathrm{Y} /\left(\left(\mathrm{x}_{1}{ }^{(i)}\right)^{\mathrm{Tx}}{ }_{1}{ }^{(i)}\right) \\
{[\text { NError }]_{1}^{(i)}=\left(\mathrm{g}_{1}{ }^{(i)}\right)^{2}\left(\mathrm{x}_{1}{ }^{(i) \mathrm{T}} \mathrm{x}_{1}{ }^{(i)}\right) /\left(\mathrm{Y}^{\mathrm{T}} \mathrm{Y}\right)}
\end{gathered}
$$

Find

$$
[\text { NError }]_{i}{ }^{(i)}=\max \left\{[\text { NError }]_{i}{ }^{(i)}, 1 \leq \mathrm{i} \leq \mathrm{K}\right\}
$$

and select

$$
\mathrm{x}_{\mathrm{i}}=\mathrm{x}_{\mathrm{i}}{ }^{(i)}=\mathrm{e}_{\mathrm{i} 1}
$$

(2) At the $j^{\text {th }}$ step where $j \geq 2$, for $1 \leq i \leq K, i \neq i_{1}, \ldots, i \neq=i_{j}$. , compute

$$
\begin{gathered}
u_{m j}{ }^{(i)}=x_{m}^{\prime} e_{i} /\left(x_{m}{ }^{T} x_{i}\right), 1 \leq m<j \\
x_{j}^{(i)}=e_{i}-\sum_{m=1}^{j-1} u_{m j}^{(i)} x_{m} \\
g_{j}^{(i)}=\left(x_{j}^{(i)}\right)^{T} Y /\left(\left(x_{j}^{(i)}\right)^{T} x_{j}^{(i)}\right) \\
{[\text { NError }]_{i}{ }^{(i)}=\left(g_{i}^{(i)}\right)^{2}\left(x_{j}^{(i)}\right)^{T} x_{j}^{(i)} /\left(Y^{T} Y\right)}
\end{gathered}
$$

Find
$[\text { NError }]_{i}{ }^{(i)}=\max \left\{[\text { NError }]_{i}{ }^{(i)}, 1 \leq i \leq K, i \neq i_{1}, \ldots, i \neq=i_{j-1}\right\}$
and select

$$
\mathrm{x}_{\mathrm{j}}=\mathrm{x}_{\mathrm{j}}^{(\mathrm{ii})}=\mathrm{e}_{\mathrm{ij}}-\sum_{m=1}^{j-1} u_{m j}^{(i)} \mathrm{x}_{m}
$$

where $u_{m j}=u_{m j}{ }^{(i j)}, 1 \leq m<j$.
(3) The OLS is terminated at the $\mathrm{K}_{\mathrm{s}}{ }^{\text {th }}$ step when

$$
1-\sum_{m=1}^{K_{S}}[\text { NError }]_{m}<\rho
$$

where $0<\rho<1$ is a chosen tolerance.
We assume that we do not have any information about noise level in the data, so that we completely over-fit the data to the model using OLS method with $\rho<<1$ ( $\rho=$ $1.0 \mathrm{e}-3$ in this study). Then we reduce unnecessary parameters to deal with the ill-conditioned problem by using second order derivative for network pruning techniques and Bayesian model comparison framework. We can obtain the optimal solution by trading off between the complexity of the model and the data misfit [20]. We start this procedure using an extremely small value for data misfit by completely over-fitting the data to the model. As the complexity of the model is reduced; i.e. the number of effective parameters is reduced, the value for data misfit is increased. The optimal complexity of the model for "true solution" is decided using a Bayesian model comparison frame that assigns a preference to the model $\mathrm{H}_{\mathrm{i}}$ with cer-
tain complexity, a Bayesian evaluation so called as the evidence $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}_{\mathrm{i}}\right)$. The evidence is obtained by multiplying the best-fit likelihood by the Occam's factor,

$$
\begin{aligned}
P\left(D \mid H_{i}\right) & =\int P\left(D \mid g_{i}, H_{i}\right) P\left(g_{i} \mid H_{i}\right) d g \\
& \cong P\left(D \mid g_{M P}, H_{i}\right) P\left(g_{M P} \mid H_{i}\right)(2 \pi)^{k / 2} \operatorname{det}^{-1 / 2} \Lambda
\end{aligned}
$$

where $\mathrm{P}\left(\mathrm{D} \mid \mathrm{g}_{\mathrm{MP}}, \mathrm{H}_{\mathrm{i}}\right)$ corresponds to the best fit likelihood, $\mathrm{P}\left(\mathrm{g}_{\mathrm{MP}} \mid \mathrm{H}_{\mathrm{i}}\right)(2 \pi)^{k / 2} \operatorname{det}^{-1 / 2} \Lambda$ corresponds to the Occam's factor, $\mathrm{A}=\partial^{2} \log \mathrm{P}(\mathrm{g} \mid \mathrm{D}, \mathrm{Hi}) / \partial \mathrm{g}^{2}$, and $\mathrm{g}_{\mathrm{MP}}$ represents the most probable parameters of g . The Occam's factor is equal to the ratio of the posterior accessible volume of $\mathrm{H}_{\mathrm{i}}$ 's parameter space to the prior accessible volume, or the factor by which $\mathrm{H}_{\mathrm{i}}$ 's hypothesis space collapses when the data is collected [20]. The model $\mathrm{H}_{\mathrm{i}} \mathrm{s}$ can be viewed as consisting of a certain number of exclusive sub-models, of which only one is chosen when the data is collected. The Occam's factor is a measure of complexity of the model that depends not only on the number of parameters in the model but also on the prior probability of the model. Therefore, the over-fitting solution can be avoided by using Bayesian model comparison frame because the Bayesian Occam's factor assures getting the optimal complexity of the model. See Mackay [20] for more details of Occam's factor.

With a second order derivative for network pruning [23], we can select the parameters to be eliminated first. Our goal here is to find a set of parameters whose deletion causes the least increase of cost function C

$$
\mathrm{C}=\beta / 2(\mathrm{Y} \cdot \mathrm{Xg})^{T}(\mathrm{Y} \cdot \mathrm{Xg})+\alpha / 2\left(\mathrm{~g}^{\mathrm{T}} \mathrm{~g}\right)
$$

where $\alpha$ and $\beta$ are hyper-parameters that measure the complexity of the model and data misfit, respectively. It will be shown later in this section the iterative formulae to estimate $\alpha$ and $\beta$ with a given data set and model structure in Eq. 6 and 7. Using the second order derivative for network pruning method, we can derive the saliency equation as follows,

$$
L_{j}=\frac{1}{2}\left(\frac{g_{j}^{2}}{A_{i j}^{-1}}\right)-\alpha\left(\frac{g_{j}}{A_{i j}^{-1}}\right)\left(g^{T} A^{-1} v_{j}\right)-\frac{\alpha^{2}}{2}\left[g^{T} A^{-1} g-\frac{\left(g^{T} A^{-1} v_{j}\right)^{2}}{A_{i j}^{-1}}\right]
$$

where $A_{i j}{ }^{-1}$ is a $j^{\text {th }}$ diagonal component of the inverse matrix of $\mathrm{A}, \mathrm{A}=\partial^{2} \mathrm{C} / \partial \mathrm{g}^{2}$, and $\mathrm{v}_{\mathrm{j}}$ is the unit vector in parameter space, the $j^{\text {th }}$ dimension at which it is equal to one and the rest of the dimensions are equal to zero. It should be noted that A and $\mathrm{A}^{-1}$ are diagonal matrices because of the decomposition of design matrix E by Gram-Schmidt Orthogonalization theory. With Eq. 3 we can select parameters, whose elimination produces the least increase of cost function C.

With a Bayesian frame [20] we can compare alternative models when our model structures keep changing with the network pruning method. Let's say we have a data set $\mathrm{D}=[\mathrm{Y}, \mathrm{X}]$, where $\mathrm{Y}=[\mathrm{y}(1), \mathrm{y}(2), \ldots, \mathrm{y}(\mathrm{N})]^{\mathrm{T}}$ is the target data set, $\mathrm{X}=\left[\mathrm{x}_{1}, \mathrm{x}_{2}, \ldots, \mathrm{x}_{\mathrm{R}}\right]$ the $N \times K$ design matrix, and $\mathrm{x}_{\mathrm{i}}=\left[\mathrm{x}_{\mathrm{i}}(1)\right.$, $\left.\mathrm{x}_{\mathrm{i}}(2), \ldots, \mathrm{x}_{\mathrm{i}}(\mathrm{N})\right]^{\mathrm{T}}$ each column matrix in X . The regression parameters we want to infer are $\mathrm{g}=\left[\mathrm{g}_{1}, \mathrm{~g}_{2}, \ldots, \mathrm{~g}_{\mathrm{R}}\right]^{\mathrm{T}}$. The log posterior probability of data D , given $\alpha$ and $\beta$, can be derived [20] as,

$$
\begin{aligned}
\log \left(P\left(D \mid \alpha, \beta, H_{i}\right)\right)= & -\frac{1}{2} \beta\left(Y-X g_{M P}\right)^{T}\left(Y-X g_{M P}\right)-\frac{1}{2} \alpha g_{M P}^{T} g_{M P} \\
& -\frac{1}{2} \log |A|+\frac{k}{2} \log (\alpha)+\frac{N}{2} \log (\beta)-\frac{N}{2} \log (2 \pi)
\end{aligned}
$$

where the subscript MP denotes Most Probable. The evidence $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}_{\mathrm{i}}\right)$ can be obtained if we marginalize the probability defined in Eq. 5 over the hyper-parameters $\alpha$ and $\beta$. Before the estimation of the evidence $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}_{\mathrm{i}}\right)$, we have to find the most probable value of the hyper-parameters $\alpha$ and $\beta$. The differentiation of Eq. 5 over $\alpha$ and $\beta$ and the rearrangement gives formulae for the iterative re-estimation of $\alpha$ and $\beta[20]$,

$$
\begin{gathered}
\hat{\alpha}:=\frac{\gamma}{g^{T} g} \\
\hat{\beta}:=\frac{K-\gamma}{(Y-X g)^{T}(Y-X g)}
\end{gathered}
$$

where $\gamma=N-\alpha \operatorname{Trace}\left(A^{-1}\right), g=A^{-1} X^{\mathrm{T}} Y, \mathrm{~N}$ is number of data points, and K is number of variables (genes). To rank alternative structures (or complexities) of the model in the light of data set D , we evaluate the evidence by marginalizing the posterior probability $\mathrm{P}(\mathrm{D} \mid \alpha, \beta, \mathrm{H}_{\mathrm{i}})$ over $\alpha$ and $\beta$,

$$
P\left(D \mid H_{\mathrm{i}}\right)=\iint P\left(D \mid \alpha, \beta, H_{\mathrm{i}}\right) P(\alpha, \beta) d \alpha d \beta
$$

We have very little prior information about $\alpha$ and $\beta$. When the available prior information is minimal, the learning process is often started with an objective prior probability. This uninformative prior probability is referred to as "vague prior" for a parameter with a range from 0 to $\infty$, which is a flat prior [87]. This prior probability can be left out when we compare alternative models. With the prior available, we can marginalize the posterior $\mathrm{P}\left(\mathrm{D} \mid \alpha, \beta, \mathrm{H}_{\mathrm{i}}\right)$. The marginalization of $\mathrm{P}\left(\mathrm{D} \mid \alpha, \beta, \mathrm{H}_{\mathrm{i}}\right)$ over $\alpha$ and $\beta$ can be estimated using a flat prior and Gaussian integration [20],

$$
\begin{aligned}
P\left(D \mid H_{i}\right) & \equiv P\left(D \mid \alpha, \beta, H_{i}\right) \cdot P(\log \alpha, \log \beta) \cdot \sqrt{2 \pi} \cdot \sigma_{\log \alpha \mid D} \cdot \sqrt{2 \pi} \cdot \sigma_{\log \beta \mid D} \\
& =P\left(D \mid \alpha, \beta, H_{i}\right) \cdot \sqrt{2 \pi} \cdot \sigma_{\log \alpha \mid D} \cdot \sqrt{2 \pi} \cdot \sigma_{\log \beta \mid D}
\end{aligned}
$$

where $\sigma_{\log \alpha \mid D}$ and $\sigma_{\log \beta \mid D}$ are the error bars on $\log \alpha$ and $\log \beta$, found by differentiating Eq. 5 twice:

$$
\begin{gathered}
\sigma_{\log \alpha \mid D}^{2} \equiv \frac{2}{\gamma} \\
\sigma_{\log \beta \mid D}^{2} \equiv \frac{2}{(N-\gamma)}
\end{gathered}
$$

In this study, we create a novel reverse engineering algorithm for linear systems with K number of genes using three techniques described above. The algorithm is run K times so that all genes in the data set are considered as a target gene at least once. The algorithm of BOLS for a unitnetwork construction is summarized as

1. Set certain gene as the target gene and set remaining genes as regulator candidates as input.
2. Over-fit the data to Eq. 2 using OLS.
3. While the number of parameters is greater than 1 .
3.1 Estimate $\alpha$ and $\beta$ with iterative re-estimation Eq. 6 and 7.
3.2 Compute the $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}_{\mathrm{i}}\right)$ for the current state network $\mathrm{H}_{\mathrm{i}}$ with Eq. 8.
3.3. Find the parameter $g_{i}$ that gives the smallest $L_{i}$ by Eq. 4 and delete $g_{i}$
4. Select the network with the maximum $\mathrm{P}\left(\mathrm{D} \mid \mathrm{H}_{\mathrm{i}}\right)$ as an output unit network.

## Authors' contributions

CSK developed BOLS algorithm, performed experiments for evaluation of BOLS algorithm, and drafted and finalized manuscript.

## Additional material

## Additional file 1

Comparing the performance between BOLS and SBL using the data set generated based on Rogers and Girolami's study - Supplementary Information. This description provides the comparison of performance between BOLS and SBL using the synthetic data generated by Rogers and Girolami [19].
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-8-251-51.doc]

## Acknowledgements

The author was supported by the postdoctoral fellowship of Turku Centre for Computer Science during the development of BOLS algorithm. The author thanks Tapio Salakoski and Mauno Vihinen for helpful discussion.
