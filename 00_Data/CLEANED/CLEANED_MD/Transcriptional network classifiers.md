# Proceedings 

## Transcriptional network classifiers

## Hsun-Hsien Chang* and Marco F Ramoni


#### Abstract

Address: 'Childrens' Hospital Informatics Program, Harvard-MIT Division of Health Sciences and Technology, Harvard Medical School, Boston, Massachusetts, USA


E-mail: Hsun-Hsien Chang* - hsun-hsien.chang@childrens.harvard.edu; Marco F Ramoni - marco_ramoni@harvard.edu
*Corresponding author
from 2009 AMIA Summit on Translational Bioinformatics
San Francisco, CA, USA 15-17 March 2009
Published: 17 September 2009
BMC Bioinformatics 2009, IO(Suppl 9):SI doi: 10.1186/1471-2105-10-59-SI

This article is available from: http://www.biomedcentral.com/1471-2105/10/59/SI
(c) 2009 Chang and Ramoni; licensee BioMed Central Ltd.

This is an open access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


#### Abstract

Background: Gene interactions play a central role in transcriptional networks. Many studies have performed genome-wide expression analysis to reconstruct regulatory networks to investigate disease processes. Since biological processes are outcomes of regulatory gene interactions, this paper develops a system biology approach to infer function-dependent transcriptional networks modulating phenotypic traits, which serve as a classifier to identify tissue states. Due to gene interactions taken into account in the analysis, we can achieve higher classification accuracy than existing methods.


Results: Our system biology approach is carried out by the Bayesian networks framework. The algorithm consists of two steps: gene filtering by Bayes factor followed by collinearity elimination via network learning. We validate our approach with two clinical data. In the study of lung cancer subtypes discrimination, we obtain a 25 -gene classifier from III training samples, and the test on 422 independent samples achieves $95 \%$ classification accuracy. In the study of thoracic aortic aneurysm (TAA) diagnosis, 61 samples determine a 34 -gene classifier, whose diagnosis accuracy on 33 independent samples achieves $82 \%$. The performance comparisons with three other popular methods, PCA/LDA, PAM, and Weighted Voting, confirm that our approach yields superior classification accuracy and a more compact signature.

Conclusions: The system biology approach presented in this paper is able to infer functiondependent transcriptional networks, which in turn can classify biological samples with high accuracy. The validation of our classifier using clinical data demonstrates the promising value of our proposed approach for disease diagnosis.

## Background

Genome-wide expression analysis has revolutionized disease diagnostic models through the identification of
molecular signatures [1], which are selected from high ranked genes determined by statistical measures, such as fold change [2], $t$ statistic [3], signal-to-noise ratio [4], or

subnetwork scores [5]. Over the last decade, system biology researchers also exploited the comprehensive transcriptional landscape offered by microarrays to identify the transcriptional networks that unravel regulatory gene interactions and explain how diseases progress [6-8]. Although these two analysis approaches seem antithetic, they can be unified to create transcriptional network classifiers to enhance disease diagnosis accuracy. We can regard the transcriptional networks underpinning disease development as perturbed by the presence of diseases. The phenotype is treated as a binary perturbation of the overall transcriptional network. To reconstruct the classifier, our task is just to infer from expression profiles the function-dependent transcriptional network that modulates phenotypic traits.

Gene interactions play a central role in transcriptional networks. Abnormal interactions between gene transcripts will give rise to disease incursion [8,9]. To develop transcriptional network classifiers, we consider a system biology approach to capture gene interactions through the measurements of expression collinearity between genes. Our approach is carried out by the Bayesian networks framework, which is a powerful instrument to delineate dependence networks among variables. Bayesian networks have been extensively applied to analyze several types of genomic data, including gene regulation [10], protein-protein interactions [11], single-nucleotide polymorphisms [12] and pedigrees [13]. A Bayesian network is a directed acyclic graph in which nodes represent random variables and arcs define directed dependencies quantified by probability distributions. This study considers a mixed Bayesian network, where the tissue type is represented by a discrete variable and gene expression levels are modelled by continuous, log normal, distributions. Figure 1 illustrates a Bayesian network, where a node represents a gene or a phenotype, and a directed arc linking a pair of nodes records the conditional probability of the child (target) node on the parent (source) node.

Both the graphical structure of a Bayesian network and the parameters of the conditional probabilities can be learned from the available database. Nevertheless, learning a network is computationally intensive because ideally the dependent relations of all pairs of variables must be evaluated. We circumvent the demanding computations by a two-stage learning process. Our algorithm begins with the use of Bayes factor to select the genes that are functionally dependent on the phenotype, since only function-dependent genes have potential to play a role in tissue discrimination. Then, we explore the detailed dependencies between the selected genes to reconstruct a transcriptional network. After the
![img-0.jpeg](img-0.jpeg)

Figure I
An example Bayesian network. A node represents a variable, and a directed arc linking a pair of nodes records the conditional probability of the child (target) node on the parent (source) node. In this network, genes $1,2,3$ are under the phenotype's Markov blanket, so they form a signature for phenotype classification.
transcriptional network is learned, it can be exploited for tissue classification, again formulated in the Bayesian networks framework. In the learned network, the phenotype's Markov blanket is the set of nodes composed of the phenotype's parents, its children, and its children's parents. Given the genes under the Markov blanket, the phenotype is independent of the genes not covered by the Markov blanket. Hence, only the genes under the Markov blanket contribute to phenotype classification, and they assemble a signature. With reference to Figure 1, genes 1, 2, 3 are those under the phenotype's Markov blanket, consisting of a signature for tissue classification.

## Results

We validate our approach by two clinical studies: discrimination of lung cancer subtypes and diagnosis of thoracic aortic aneurysm.

## Discrimination of lung cancer subtypes

Lung adenocarcinoma (AC) and squamous cell carcinoma (SCC) are the most common subtypes of lung cancer. They are heterogeneous in many clinical aspects, such as responses to chemotherapy [14], tendency to metastases [15,16], and mortality rates [17,18]. Unfortunately, the current gold standard is histology which is subjective [19] and may fail when tumors are small [20] or when patients suffer from multiple types of primary lung carcinomas [21]. Gene expression profiling will avoid these problems and perform automatic discrimination of lung cancer subtypes. The classifier is trained by a Duke University data [22], which is available on

Gene Expression Omnibus with accession number GSE3141, in a total of 58 ACs and 53 SCCs. The lung specimens are assayed by Affymetrix HG-U133A. Figure 2 shows the function-dependent transcriptional network inferred from the data. Of the 22,283 gene probes in the microarray, seventy seven probes are dependent, directly or indirectly, on the carcinoma subtypes. Of these 77 genes, 25 are under the phenotype Markov blanket, so they per se assemble a signature. Enrichment study shows that there are 23 unique genes in this signature, summarized in Table 1.

The performance of 10 -fold cross validation achieves $98.5 \%$ accuracy. We further test the classification accuracy of the network on seven independent study populations with Gene Expression Omnibus accession numbers GSE10072, GSE7670, GSE12667, GSE4824, GSE2109, GSE4573, and GSE6253, for a total of 422 samples, 232 AC and 190 SCC, from subjects of Caucasian, Asian and African descent representing $84.6 \%, 6.9 \%$, and $2.8 \%$ of the data, respectively. On these independent samples, our transcriptional network classifier achieves an accuracy of $95.2 \%$.

The 25 -gene signature identified by the classifier is unique to discriminate AC and SCC with high accuracy. Furthermore, most of these genes have been reported their specificity to lung cancer. ABCC3, CLDN3, DPP4, MUC3B, MUC5B, NTRK2, SPINK1, TJP3 are specific markers of lung AC [23-29]. KRT6A, KRT6B, KRT6C, KRT17, RHCG, SPRR1A, and VSNL1 are unique to lung SCC [30-33]. BICD2, CDA, NMNAT2, SERPINB13, and
![img-1.jpeg](img-1.jpeg)

Figure 2
The functional dependence network for lung cancer subtypes characterization. There are 77 genes dependent on the lung cancer subtypes and they are selected to build up this network, where 25 genes (in green) are under the phenotype's Markov blanket to assemble a signature.

TOX3 have no specificity to either AC or SCC but to lung cancer [34-38].

## Diagnosis of thoracic aortic aneurysm

Thoracic aortic aneurysm (TAA) is usually asymptomatic and associated with high mortality. Identification of atrisk individuals is a challenging task. Gene expression patterns in peripheral blood cells are expected to assist the diagnosis of TAA. The data used to derive the classifier is publicly available on Gene Expression Omnibus with accession number GSE9106 [39], which involves 36 cases and 25 controls for training purpose. Peripheral blood samples were collected at Yale-New Haven Hospital. Gene expression experiments were carried out by Applied Biosystems Human Genome Survey Microarray v2.0, which is equipped with 32,878 probes. The utilization of Bayes factor in our algorithm first filters out 346 genes that are dependent on the phenotype. Bayesian network learning results in the functional dependence network shown in Figure 3. There are 34 genes under the phenotype's Markov blanket, and they form a signature for TAA diagnosis. Table 2 summarizes the annotations of the signature, where the nameless genes are provided with their probe identifies only. The genes ABCG4, ARNT2, BCOR, CABP2, CSTF2, DNTTIP1, FGG, IGF2BP1, MAL2, MMP11, RBM16, TM4SF1, ZBTB4, ZNF394 are involved in connective tissue disorders and inflammatory disease, which are prerequisite to TAA. The 10 -fold cross validation of the classifier yields $97 \%$ accuracy. We further examine the classifier on the independent samples, 24 cases and 9 controls, also included in the Yale data GSE9106. The accuracy on these independent samples achieves $82 \%$, demonstrating good performance of our approach.

## Comparisons with other methods

We contrast our proposed system biology approach with other popular algorithms that do not take into account regulatory gene interactions:

1) Principal Component Analysis with Linear Discriminant Analysis (PCA/LDA): The PCA/LDA method begins with reducing the number of genes to a small number of principal genes and then searches for a discriminative linear function on expression values to separate tissues.
2) Prediction Analysis for Microarray (PAM) [40]: PAM utilizes signal to noise ratios to pick up a signature and uses the ratios to determine the tissue types of testing samples.
3) Weighted Voting [1]: This method ranks genes by the fold change of the means of the expression values. The classification is determined by how close to the high rank genes the testing data is.

Table I: The signature of 25 genes for characterizing lung cancer subtypes. Enrichment shows that there are 23 unique genes in the signature


Unlike our approach, the above methods neglect dependencies among genes, so they yield worse performance than our TNC. Table 3 and Table 4 summarize the comparisons of our approach with these methods on the lung cancer and TAA studies, respectively. The results show that our approach is superior to other algorithms. On the other hand, our approach leads to more compact signatures because collinearity elimination is addressed after gene selection. The differences between our approach and other schemes are statistically significant ( $\mathrm{p}<0.005$ ), except that weighted voting performs close to ours in the lung cancer study. Although weighted voting reaches high classification accuracy on the lung cancer data, it requires a large number of genes in the signature, giving rise to overfitting problem.

## Discussion

The clinical application confirms improved accuracy of our proposed system biology approach. Literature survey on the functions of the signature genes also validates the capability of our approach to extract biologically reasonable signatures. Furthermore, the large-scale independent test on seven cohorts in the lung cancer study shows robustness of our classifier across platforms and populations. The two studies also demonstrate the capability of our method to analyze data assayed by microarrays manufactured by different makers.
![img-2.jpeg](img-2.jpeg)

Figure 3
The functional dependence network for TAA
diagnosis. There are 346 genes selected to reconstruct this network, because of their distinct expression patterns between TAA and normal samples. The signature consists of the 34 genes (in green) under the phenotype $\delta \in^{\mathrm{TM}}$ s Markov blanket.

Table 2: The signature of 34 genes for diagnosing TAA


Unlike existing methods that require the operator to specify a cutoff of statistical measures to select high ranked genes, our method is threshold free for signature selection, because the signature genes are determined once the transcriptional network is modelled. For phenotype classification, we need to keep the network merely composing of the signature genes, and the remaining network can be discarded; this way can save storage resources in clinical usage. Another feature of our transcriptional network classifier is its visualization of molecular dependence network, which will provide biologists a clue for gene causality investigation.

A recent work proposes to use prior knowledge of known pathway information to select gene subnetworks as features for tissue classification [5]. However, this method will discard a major portion of the data, because a large number of genes have not been discovered their functional pathways. Dissimilar to this method, our approach fully utilizes the entire data to screen the function-dependent genes and to reconstruct the network.

## Conclusions

This paper uses a system biology approach to develop transcriptional network classifiers. The classifier can be thought of as a gene network perturbed by the presence

Table 3: Performance comparisons with other methods on the lung cancer data


Table 4: Performance comparisons with other methods on the TAA data


of the phenotypic traits. We adopt Bayesian network framework to model the classifier. The algorithm uses Bayes factor for gene filtering, followed by collinearity elimination via network learning. The clinical applications of our approach to lung cancer subtypes classification and TAA diagnosis demonstrate high classification accuracy of the network based classifiers. The biological validation of the signatures further confirms the ability of the transcriptional network classifier to extract meaningful signatures.

## Methods

Let $Y_{1}, Y_{2}, \ldots, Y_{N}$ be Gaussian random variables representing the expression levels of genes $1, \ldots, N$, and $C$ be a multinomial random variable indicating tissue conditions. We use uppercase to denote random variables and lowercase to denote their values. Our algorithm first uses Bayes factor to filter function-dependent genes and then exploit Bayesian network learning to eliminate collinearity among these selected genes.

## Gene filtering by Bayes factor

The genes functionally dependent on the phenotype are filtered in the beginning. The filtering can be realized by Bayes factor, which evaluates for each gene the ratio of its likelihood of being dependent on the phenotype to its likelihood of being independent of the phenotype. When the Bayes factor is greater than one, the gene is selected because it is more likely to be dependent on than to be independent of the phenotype.

## Collinearity elimination via network learning

Without loss of generality, we assume that the first $G$ out of $N$ genes were selected by the preceding step. The gene expression data under consideration now is $D=\left\{y_{1}, y_{2}, \ldots\right.$, $\left.Y_{G}, c\right\}$. When a gene $Y_{i}$ is collinearly expressed with another gene $Y_{j}$, the dependence of gene $Y_{i}$ on the phenotype is mediated by gene $Y_{j}$. In other words, our goal is to search which gene modulates gene $Y_{i}$ with the highest likelihood. When we find out for every gene its best upstream variable, the network is achieved. In the framework of Bayesian network, our objective is to learn from a set of candidate network models $\Omega=\left\{M_{1}, M_{2}, \ldots, M_{K}\right\}$ the optimal network $\hat{M}$ fit best to the data $D$. Equivalently, we look for the highest posterior probability $p\left(M_{k} \mid D\right)$. Applying Bayes' theorem
to $p\left(M_{k} \mid D\right)$ results in $p\left(M_{k} \mid D\right) \propto p\left(M_{k}\right) p\left(D \mid M_{k}\right)$, where $p\left(M_{k}\right)$ is the prior probability of model $M_{k}$ and $p\left(D \mid M_{k}\right)$ is the marginal likelihood. The computation of $p\left(D \mid M_{k}\right)$ is to average out $\theta_{k}$ from the likelihood function $p\left(D \mid M_{k}, \theta_{k}\right)$, where $\theta_{k}$ is the values of the random vector $\Theta_{k}$ parameterizing the distribution of $y_{1}$, $y_{2}, \ldots, Y_{G}, C$ conditional on $M_{k}$. We can exploit the local Markov properties encoded by the network $M_{k}$ to rewrite the joint probability $p\left(D \mid M_{k}, \theta_{k}\right)$ as

$$
p\left(D \mid M_{k}, \quad{ }_{k}\right)=p\left(c \mid p a(c), \quad{ }_{k}\right) \prod_{g=1}^{C} p\left(y_{g} \mid p a\left(y_{g}\right), \quad{ }_{k g}\right)
$$

where $p a(x)$ denotes the values of the parents $\operatorname{Pa}(X)$ of random variables $X$, and ${ }_{k x}$ is the subset of parameters used to describe the dependence of variable $X$ on its parents.

In this paper, we model a gene $Y_{g}$ to be dependent on either the phenotype $C$ or another single gene $Y_{a}$, and the phenotype $C$ is the root in the network without parents. We further can assume the $J$ samples in the database are independent. The likelihood function becomes

$$
p\left(D \mid M_{k}, \theta_{k}\right)=\left[\prod_{j=1}^{J} p\left(c_{j} \mid \theta_{k c}\right)\right] \times\left[\prod_{j=1}^{J} \prod_{g=1}^{C} p\left(y_{g j} \mid p a\left(y_{g j}\right), \theta_{k g}\right)\right]
$$

where the subscripts $j$ indicate the $j$ th sample. The first term can be estimated by sample frequencies, and the second term can be derived using linear Gaussian model [41]. The marginal likelihood function is the solution of the integral

$$
p\left(D \mid M_{k}\right)=\int p\left(D \mid M_{k}, \theta_{k}\right) p\left(\theta_{k}\right) d \theta_{k}
$$

Due to limited space, we in this paper do not present the detailed computation, which can be derived from [41]. Finally, the determination of the best Bayesian network model is $\hat{M}=\arg \max _{k} p\left(M_{k}\right) p\left(D \mid M_{k}\right)$.

## Sample classification

The phenotype classification $\hat{c}$ of a sample is to find the maximum probability of the tissue class that the sample belongs to, conditional on the expression values of the

sample. The formulation for the classification is as follows:

$$
\hat{c}=\arg \max _{c} p\left(c \mid \gamma_{1}, \gamma_{2}, \ldots, \gamma_{C}\right)
$$

The application of Bayes' theorem leads to

$$
\begin{aligned}
\hat{c} & =\arg \max _{c} \frac{p\left(\gamma_{1}, \gamma_{2}, \ldots, \gamma_{C} \mid c\right) p(c)}{p\left(\gamma_{1}, \gamma_{2}, \ldots, \gamma_{C}\right)} \\
& =\arg \max _{c} p\left(\gamma_{1}, \gamma_{2}, \ldots, \gamma_{C} \mid c\right) p(c)
\end{aligned}
$$

where the second equality holds because the denominator $p\left(\gamma_{1}, \gamma_{2}, \ldots, \gamma_{C}\right)$ in the first line is not a function of $c$. Since only genes directly dependent on the phenotype variable $C$ matter in the maximization, the tissue classification becomes

$$
\hat{c}=\arg \max _{c} p(c) \prod_{g \in H} p\left(\gamma_{g} \mid c\right)
$$

where $H$ denotes the set of genes that are the children of the phenotype $C$ in the network and assemble a signature. Equivalently, the set $H$ of genes corresponds to the genes under the phenotype's Markov blanket.

## Competing interests

The authors declare that they have no competing interest.

## Authors' contributions

HHC designed the method and conducted the analysis; MFR directed the study; both authors prepared the manuscript.

## Acknowledgements

This research is supported in part by NIH/NHGRI (R01HG003354).

This article has been published as part of BMC Bioinformatics Volume 10 Supplement 9, 2009: Proceedings of the 2009 AMIA Summit on Translational Bioinformatics. The full contents of the supplement are available online at http://www.biomedcentral.com/1471-2105/10?issue=S9.

## Publish with Bio Med Central and every

scientist can read your work free of charge
"BioMed Central will be the most significant development for disseminating the results of biomedical research in our lifetime."

Sir Paul Nurse, Cancer Research UK
Your research papers will be:

- available free of charge to the entire biomedical community
- peer reviewed and published immediately upon acceptance
- cited in PubMed and archived on PubMed Central
- yours - you keep the copyright

Submit your manuscript here:
http://www.biomedcentral.com/info/publishing_adv.asp
BioMedcentral