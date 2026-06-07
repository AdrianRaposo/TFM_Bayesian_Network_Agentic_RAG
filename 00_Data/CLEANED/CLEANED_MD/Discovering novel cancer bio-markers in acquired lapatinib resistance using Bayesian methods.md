# DISCOVERING NOVEL CANCER BIO-MARKERS IN ACQUIRED LAPATINIB RESISTANCE USING B AYESIAN METHODS 

A Preprint

AKM Azad<br>iThree Institute<br>Faculty of Science<br>University of Technology Sydney, Australia<br>akm.azad@uts.edu.au

Salem Alyami ${ }^{\star}$<br>Department of Mathematics \& Statistics<br>Imam Mohammad Ibn Saud Islamic University<br>Riyadh, Saudi Arabia<br>saalyami@imamu.edu.sa

December 2, 2020


#### Abstract

Genes/Proteins doesn't work alone within our body, rather as a group they perform certain activities indicated as pathways. Signalling transduction pathways (STPs) are some of the important pathways that transmits biological signals from protein-to-protein controlling several cellular activities. However, many diseases such as cancer target some of these signalling pathways for their growth and malignance, but demystifying their underlying mechanisms are very complicated tasks. In this study, we use a fully Bayesian approaches to develop methodologies in discovering novel driver bio-markers in aberrant STPs given two-conditional high-throughput gene expression data. This project, namely PathTurbEr (Pathway Perturbation Driver), is applied on a global gene expression dataset derived from the lapatinib (an EGFR/HER dual inhibitor) sensitive and resistant samples from breast cancer cell-lines (SKBR3). Differential expression analysis revealed 512 differentially expressed genes (DEGs) and their signalling pathway enrichment analysis revealed 22 singalling pathways as aberrated including PI3K-AKT, Hippo, Chemokine, and TGF- $\beta$ singalling pathway as highly dys-regulated in lapatinib resistance. Next, we model the aberrant activities in TGF- $\beta$ STP as a causal Bayesian network (BN) from given observational datasets using three Markov Chain Monte Carlo (MCMC) sampling methods, i.e. Neighbourhood sampler (NS) and Hit-and-Run (HAR) sampler, which has already proven to have more robust inference with lower chances of getting stuck at local optima and faster convergence compared to other state-of-arts methods. Next, we examined the structural features of the optimal BN as a statistical process that generate the global structure using, $p_{1}$-model, a special class of Exponential Random Graph Models (ERGMs) and MCMC methods for their hyper-parameter sampling. This step will enable us to detect key players that would supposedly drive the aberration within the chosen BN structure of STP, which yielded 31, 33, and 22 perturbation driver genes out of 79 constituent genes of three STP models of TGF- $\beta$ signalling. Functional enrichment with GO terms of these driver genes suggested their significant associations with breast cancer progression/resistance. The full code base for PathTurbEr is available in here: https://github.com/Akmazad/PathTurbEr/.


Keywords Signal Transduction Pathways $\cdot$ MCMC Methods $\cdot$ Neighbourhood Sampler $\cdot$ Hit-and-Run Sampler $\cdot$ Metropolis-Hastings Sampler $\cdot$ Exponential Random Graph Models

## 1 Introduction

Signal transduction pathways (STPs) involve collections of signalling proteins, transducing biological signal from one to another that controls cell growth and division, cell death, cell fate, and cell motility [1]. Hence, altered activities in one or more of these STPs, e.g. PI3K/AKT signalling, Ras/MAP signalling, Notch signalling and Wnt signalling

[^0]
[^0]:    *corresponding author

mediates uncontrolled cell growth/death resulting tumour initiation, progression, metastasis [2], or even resistance phenotype to targeted therapies [3]. Induction of these perturbed signalling activities often refers to oncogenic mutations of key signalling proteins that are structurally central (hub) in corresponding STP structures, resulting in their or others' hyper-activation or inactivation [1]. Therefore, elucidating mechanisms underpinning aberrant signalling activities are crucial for successful cancer therapeutics.
Hight-throughput datasets e.g. Gene/Protein expressions, copy number variation, methylation, and microRNA expression from cohorts of cancer-related sample patients (i.e. treated, untreated, and resistant) enable us genome-wide analyses of disease phenotypes (e.g. cancer malignance or cancer drug-resistance) and identification of relevant biomarkers in silico. Utilizing those high-throughput datasets for deriving data-driven models facilitates critical assessments of the systems behaviour in response to any perturbation from wild-types, i.e. due to the presence of disease markers, treatment with drugs or resistance phenotypes. Therefore, these data-driven model inference offers unique scope to deduce novel findings that may better reflect the systems dynamics under study. However, it's a very complex computational task and still an open problem in the field of systems biology since inferring optimal model from the data require smart searching algorithms within the space of all possible models. The simplest of all approaches could probably be deriving co-expression network from available datasets among all signalling proteins but those models will lack causalities that are often crucial for better understanding interactions among biological entities.
A BN is defined as a directed acyclic graph (DAG), ' $G$ ' $=(V, E)$, where ' $V$ ' are a set of random variables (here genes/Proteins) and ' $E$ ' represents relationships among those random variables. Each random variable is associated with conditional probability distributions given it's parents except the root variable, which are only associated with corresponding prior probability distributions. Causal BNs possess causal edges, for example $X \longrightarrow Y$ indicates causality from random variable ' $X$ ' to random variable ' $Y$ '. An important property of BNs is called 'Markov condition', which must be satisfied for the probability distributions of the constituent random variables. 'Markov condition' states that each variable in the BN should be conditionally independent of other random variables that are its non-descendants conditional on its parents.
To model STP as a BN, we can model the phosphorylation activities of signalling proteins as random variables and any phosphorylation activities (i.e. signalling activities) among signalling proteins as arcs among those variables. Nonetheless, BN models like such must meet the above-mentioned 'Markov condition' to represent the joint probability distribution of the random variables. Woolf et al. [4] suggested that the steady-state concentration of signalling proteins and their corresponding signalling activities supports this condition, and Sachs et al. [5] has conducted a successful proof-of-principle analysis on that.
Recently, Bayesian network (BN) has been applied to model aberrant STPs by studying case/control gene expression data [6] using MCMC methods such as Metropolis-Hastings or Gibbs sampling algorithm. Like other non-MCMC approaches (i.e. score-based methods such as Greedy, Hill-Climbing, Tabu search algorithm), these MCMC approaches also suffers local optimal problem, which means models claimed as optimal from those methods may not be globally optimal. Recently, we have shown that compared to Metropolis-Hastings algorithm, newly developed Neighbourhood sampler (NS) and Hit-and-Run sampler finds BN structures with better accuracy and faster convergence towards true distribution. For example, the main rationale behind NS sampler's efficiency lies in its reduction step, where the rejected BNs are excluded from being chosen second time, offering greater chances to others to be selected, and therefore have less chance to get stuck at local optima [7]. We hope using these two methods, we will be able to infer robust BN as a perturbed STP in given high-throughput datasets.
Biological networks reveal scale-free topology where majority of nodes possess fewer connections whereas small of amount nodes have very high connectivity, typically known as hub nodes [8]. It is shown that data-driven network models also feature the similar behaviour [9], i.e. the existence of hub nodes within the network. This behaviour is expected in biological systems as for disease perturbations to take place and/or spread within the system, it must target central players that has maximum reachability to other nodes via excessive connectedness. Hence hub nodes serve as key bio-markers which must be analysed, found and targeted in order to counteract the perturbations. It's important to acknowledge that biological processes (e.g. signalling activities) underlying data and the experimental measurements are stochastic. For example, derived interactions in the data-driven BN model may not be truly reliable whereas some critical interactions may remain undetected. Therefore, after modelling data-driven STP (optimal BN), statistical approaches relying on probabilistic models should be adopted to assess the probability of forming each interactions (i.e. aberrant activities among signalling proteins) within that BN structure. Being originally proposed in social network analyses, Exponential Random Graph Models (ERMGs), or p*-models [10] are central of statistical modelling of networks, where each possible edge in a network is considered as a random variable and modelled as combinations structural properties of the constituent nodes, e.g. global density of nodes, attractiveness/expansiveness of nodes (commonly known as sociality parameters). Note, non-statistical methods like descriptive approaches may also model hub nodes based on their degree distributions which may not address stochastic nature of the underlying data and

experimental measurements [11]. In the context of this study, hub nodes should be highly social, which would allow us to analyse the possibilities of detecting those hub nodes as a key bio-marker underlying the aberrant STP structure formation.

The primary research questions we would like address in this study are as two-folds. First, is there exists a causal structure that optimally model the aberrant signalling activities within a signal transduction pathways (STP) given two-conditional datasets e.g. cancer-vs-normal or resistant-vs-treatment? Second, how the data-driven STP structure has emerged - is there any local biological process or local structure (e.g. star-like shapes) that contributed in generating the global structure? We hypothesize that the capabilities of new MCMC sampling methods in accurate BN inference can be leveraged for finding optimally aberrant STP structures by studying two conditional studies structures that would model perturbed signalling activities in cancer-vs-normal or resistant-vs-treatment conditions. In statistical modelling, it can be hypothesized that global structure of a network emerges from the agglomeration of local structures that relies on the local inter-dependencies of edges. We also hypothesize that statistical analyses of the generic and structural properties of the inferred aberrant STP using ERGM models along with hierarchical Bayesian modelling of their hyper-parameter inter-dependencies would unravel key genes/proteins (e.g. network hubs) that drives those perturbations within that particular STP.

# 2 Methods 

PathTerbEr is a data-driven approach in detecting perturbation driver bio-markers in signaling pathways. The schematic view of the proposed research plan is depicted in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1: PathTurbEr: a schematic diagram of our proposed approach.

## Acquiring datasets and pre-processing

A global gene expression dataset for lapatinib sensitive-vs-resistant samples, for breast cancer cell-line, namely SKBR3, from Gene expression omnibus (GEO) with accession number GSE38376, published by Komurov et al. [12]. This dataset includes samples with basal conditions (i.e. lapatinib-sensitive) dosed with $0 \mu \mathrm{M}, 0.1 \mu \mathrm{M}$, and $1.0 \mu \mathrm{M}$ of lapatinib drug, and samples with resistant conditions with the same doses, respectively. Thus, two data matrices, each for

lapatinib-sensitive and lapatinib-resistant were obtained, which was further considered as control-vs-case data for the downstream analyses. 45 signalling pathways were collected from KEGG pathway database [13].

# Differential expression and functional enrichment test 

For the differential expression analysis, the raw gene expression were fitted with linear models using limma R package [14] with eBayes function to calculate the Bayes statistics. Furthermore, the significance score (i.e. p-values) were further adjusted with FDR correction techniques. Next, a set of differentially expressed genes (DEGs) based on the adjusted p-values, were used for over-representation test with 45 KEGG signalling pathways using the hyper-geometric test by phyper function available in stats R package. The enrichment significance score (p-values) were further adjusted using FDR-correction.

## Inferring optimally perturbed STP structure using MCMC sampling algorithms

In this study, we have modelled the signal transduction pathways (STPs) as Bayesian Networks (BNs), which is a graphical model for inferring causal dependencies among statistical variables, which is the genes/proteins in this case. Let, $G:=(V, E)$ be a Bayesian network as graph with V is the set of genes, and E is the set of causal edges (i.e. directed) connecting the nodes from V, which are also acyclic and connected graph.

## Parameter inference of BNs using Dirichlet-Multinomial distribution

Prior to BN structure learning, we modeled the perturbation of the lapatinib-resistant samples using the following equation:

$$
z_{i j}^{R}=\frac{r_{i j}^{R}-\mu_{i}^{S}}{\sigma_{i}^{S}}
$$

where, $r_{i j}^{R}, \mu_{i}^{S}, \sigma_{i}^{S}$, and $z_{i j}^{R}$ are raw expression value of a gene $_{i}$ in the sample $_{j}$, the average and standard deviation of all the samples in the lapatinib-sensitive condition of gene $_{i}$, and the transformed value of $R_{i j}$, respectively. Next, the transformed lapatinib-resistant data matrix were further discretized using the following formula:

$$
z_{i j}^{R t}= \begin{cases}1 & z_{i j}^{R}>1.5 \\ -1 & z_{i j}^{R}<-1.5 \\ 0 & \text { otherwise }\end{cases}
$$

In BNs, the causality is modelled as the conditional probabilities between parent and the child nodes, where the children nodes probabilities are conditioned on the probabilities of parents. With a given data $D$ and a candidate BN structure, $G$, a conditional probability is defined as $P\left(X_{i} \mid P a\left(X_{i}\right)\right)$, where $X_{i}$ is a particular gene, and $P a\left(X_{i}\right)$ is the set of parents of $X_{i}$. When the data, $D$ is given, this conditional probability can be defined as $P\left(X_{i}=k \mid P a\left(X_{i}\right)=j\right)=\theta_{i j k}$, where $\theta_{i} j k$ is is the probability of each state value $k$ within each node $X_{i}$, given that its parents are in configuration $j$. Finally, to calculate the likelihood score (i.e. probability) of a BN structure, $G$, a multinomial distribution (MD) was used to relate the data with model, with dirichlet distribution for its prior. Hence, the formula for the Dirichlet-Multinomial model is as follows:

$$
P(D \mid G)=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\Gamma\left(\alpha_{i j}\right)}{\Gamma\left(\alpha_{i j}+N_{i j}\right)} \prod_{k=1}^{r_{i}} \frac{\Gamma\left(\alpha_{i j k}+N_{i j k}\right)}{\Gamma\left(\alpha_{i j k}\right)}
$$

where $N_{i j k}$ is the number of observations in bin $k$ of node $i$ corresponding to a parent configuration $j, r_{i}$ is the number of possible state values (bins) for a particular variable $X_{i}, q_{i}$ is the total number of configurations of parent state values of $X_{i}, N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}$, and $\alpha_{i j k}$ are the hyper-parameters (hyper-conditional probabilities), $\alpha_{i j}=\sum_{k=1}^{r_{i}} \alpha_{i j k}$. Here, we have considered $\alpha_{i j k}=\frac{\alpha}{q_{i} r_{i}}$, where $\alpha$ is the total imaginary counts for the Dirichlet prior. The posterior probability distribution of the graph $G$ given data $D$ can now be constructed as:

$$
P(G \mid D)=\frac{P(D \mid G) P(G)}{P(D)}
$$

where we only consider the numerator as the $P(D)$ does not depends of $G$. Moreover, we've used a uniform prior for $P(G)$.

# Structure inference using Neighbourhood sampler, Hit-and-Run and Metropolis-Hastings sampler 

Here, we have three MCMC (Markov Chain Monte Carlo) sampling algorithms, namely Neighbourhood sampler, Hit-and-Run sampler and Metropolis-Hastings algorithms for inferring optimal STP from the whole BN search space. At each sampling iteration, each of these algorithms considers a candidate BN and looks around its neighbourhood space and evaluates the likelihood of it using equation 4, and selects the one that maximizes the likelihoods as optimal BN models for a signalling pathway of interest. The details of each of these algorithms are explained in the original articles $[7,15]$, which is beyond the scope of this article. Finally, the inferred BN STPs (from each of these MCMC sampling algorithms) was considered as the optimally perturbed STP structure model.

## Bayesian statistical modelling of the optimal STP to infer perturbation driver genes

## Network model

In this study, we have used a fully Bayesian statistical modelling approach for analysing the statistical aspect of the perturbed STP structure yielded from the MCMC sampling algorithms of BN structure learning (see previous sub-section). We have used, $p_{1}$-model, initially proposed by Holland and Leinhardt [16], is a special class of exponential families of distributions, for this study that offer robust and flexible parametric models, which is used to evaluate the probability that a gene to be hub in the perturbation network inferred in previous sub-section.
A STP BN model can be referred as a gene-gene relationship causal network with $g$ genes, which can be considered as a random variable $\mathbf{U}$ over a space of $2^{g(g-1)}$ graphs. Let $\mathbf{U}=\mathbf{u}$ is the realization of $\mathbf{U}$ and the binary outcome $u_{i j}=1$ if gene $_{i}$ interacts with gene $_{j}$, or $u_{i j}=0$ otherwise, then $\mathbf{u}$ is a binary data matrix. Let $\operatorname{Pr}(\mathbf{u})$ be the probability function given by the following formula:

$$
\operatorname{Pr}(u)=\operatorname{Pr}(\mathbf{U}=\mathbf{u})=\frac{1}{\kappa(\boldsymbol{\theta})} \exp \sum_{p} \boldsymbol{\theta}_{p} z_{p}(\mathbf{u})
$$

where $z_{p}(\mathbf{u})$ is the network statistic of type $p, \boldsymbol{\theta}_{p}$ is the parameter associated with $z_{p}(\mathbf{u})$ and $\kappa(\boldsymbol{\theta})$ is the normalizing constant that ensures $\operatorname{Pr}(\mathbf{u})$ is a proper probability distribution (sums to 1 over all $\mathbf{u}$ in $G$ ) [17]. The parameter $\boldsymbol{\theta}$ is a vector of model parameters associated with network statistics and needs to be estimated. See [?] for further details. A major challenge in computing with the $p_{1}$-model is the calculation of $\kappa(\boldsymbol{\theta})$, for which the maximum likelihood estimation is intractable due to the large graph space cardinality. A technique called maximum pseudolikelihood estimation [18] has been developed to address this issue, which employes MCMC sampling method such as Gibbs or Metropolis-Hastings sampling algorithms [19]
In this study, we have considered the undirected version of $p_{1}$-model, which can be simplified by using only two Bernoulli variables $Y_{i j 0}$ and $Y_{i j 1}$ as follows:

$$
Y_{i j k}= \begin{cases}1 & \text { if } u_{i j}=k \\ 0 & \text { otherwise }\end{cases}
$$

Now the $p_{1}$-model can be defined using the following two equations to predict the probability of an edge being present between gene $_{i}$ and gene $_{j}$ :

$$
\begin{gathered}
\log \left\{\operatorname{Pr}\left(Y_{i j 1}=1\right)\right\}=\lambda_{i j}+\theta+\alpha_{i}+\alpha_{j} \\
\log \left\{\operatorname{Pr}\left(Y_{i j 0}=1\right)\right\}=\lambda_{i j}
\end{gathered}
$$

for $i<j$, where $\theta$ is the global density parameter, and $\alpha$, which represents the sociality of a gene to be connected in an undirected network. Note, $\lambda_{i j}$ is there to ensure $\operatorname{Pr}\left(Y_{i j 0}=1\right)+\operatorname{Pr}\left(Y_{i j 1}=1\right)=1$.

## Bayesian model to infer perturbation drivers

Here, we have employed a fully Bayesian approach to infer the posteriori of parameters of the above $p_{1}$-model. For that purpose, MCMC sampling methods i.e. Gibbs sampling approach were adopted, which generate samples from the joint distribution of $P(\mathcal{M}, \theta \mid \mathcal{D})$, where $\mathcal{M}$ is model under consideration, $\theta$ is the set of model parameters to be inferred, and the $\mathcal{D}$ is the data. Gibbs sampling iteratively samples on parameter at a time with full conditional distribution of the current and old values of other parameters. Our approach relies on a hierarchical Bayesian model where the model

parameters depends on several hyper-parameters i.e., $\theta$ and $\alpha$, both assumed to be following a normal distribution, which in tern relies on 0 mean and standard deviation of $\sigma_{\theta}$ like the following:

$$
\begin{aligned}
& \theta \sim \mathcal{N}\left(0, \sigma_{\theta}^{2}\right) \\
& \alpha \sim \mathcal{N}\left(0, \sigma_{\alpha}^{2}\right)
\end{aligned}
$$

Assuming $\tau=\sigma^{-2}$, we can consider a gamma prior for both $\tau_{\theta}$ and $\tau_{\alpha}$ since, gamma is the conjugate prior of normal distribution:

$$
\begin{aligned}
\tau_{\theta} & \sim \operatorname{Gamma}\left(a_{0}, b_{0}\right) \\
\tau_{\alpha} & \sim \operatorname{Gamma}\left(a_{0}, b_{0}\right)
\end{aligned}
$$

where we set $a_{0}=0.001$ and $b_{0}=0.001$ to make the prior for $\theta$ non-informative, making its standard deviation wide enough to express large uncertainty [11]. To implement Gibbs sampling we have used JAGS (Just another Gibbs Sampler). We hypothesized that the perturbation driver genes would yield higher connectivity, i.e. reveal larger sociality score ( $\alpha$ values) in a STP.

# 3 Results 

## Differential Expression analysis and Functional enrichment test

As a pilot experiment to observe the expression dynamics between case-vs-control studies, we conducted a differential expression analysis with lapatinib-sensitive and lapatinib-resistant gene expression from Breast cancer patients collected from Gene expression omnibus (accession number: GSE38376). Using limma R package with a threshold of 0.00001 for adjusted p-value (bonferroni corrected), we have found 512 differentially expressed genes (DEGs) [Additional File 1] as shown in Figure 2A. Next, to observed which signal transduction pathways (STPs) were enriched with the selected DEGs, we conducted a statistical over-representation analysis with a hyper-geometric test with phyper function available in stat R package. Using 45 KEGG signalling pathways, we have found 20 STPs that are significantly enrihced with the selected DEGs yeilding adjusted p-value $<0.05$, which are depicted in Figure 2B. As we observed the top significantly enriched STPs include PI3K-AKT signalling (adj. p-Value $=7.2 \times 10^{-9}$ ), Hippo signalling (adj. p-Value $=6.2 \times 10^{-8}$ ), Chemokine signalling (adj. p-Value $=1.02 \times 10^{-6}$ ), TGF- $\beta$ signaling (adj. p-Value $=3.21 \times 10^{-6}$ ), and Thyroid hormone signaling (adj. p-Value $=1.65 \times 10^{-5}$ ). As a case study of all our downstream experiments and analyses, i.e optimal STP structure learning and its perturbation driver identification, we have selected the TGF- $\beta$ signaling pathway (the number of nodes $=79$ ) as it demonstrated significant enrichment with DEGs and reported to play significant role in breast cancer progression/resistance phenomenon via cross-talking with EGFR-mediated (lapatinib-targeted) signaling pathways [20].

## Novel MCMC methods for sampling Bayesian networks finds optimal STP as dys-regulated pathway in Lapatinib Resistance

## Data pre-processing

We hypothesized that the causal Bayesian network models may potentially reveal aberrant signalling activities given perturbation data from two-conditional dataset. At first, for a particular gene in a particular sample in the raw gene expression data for lapatinib-resistant cell-line (SKBR3) was standardized into z-score, based on the mean and standard deviation of expression of the all the samples in the corresponding gene in the lapatinib-sensitive conditions. This standardized score would measure how each resistant sample (case data) data is deviated from the control expression, which is in this case lapatinib-sensitive condition, thus revealing the perturbation measurements of resistant samples compared to the distribution of sensitive samples. Next, each expression values (i.e. z-score transformed) of lapatinibresistant dataset were discretized in three levels based on thresholding ( $>1.5$ or $<-1.5$ ): over-expressed, down-expressed, or neutral to model the data-driven Bayesian networks.

![img-1.jpeg](img-1.jpeg)

Figure 2: Differential expression (A) and function enrichment analyses (B) of resistant-vs-sensitive gene expression data in breast cancer cell-lines, SKBR3.

### Optimal STP sampling for TGF-β signalling using Neighbourhood Sampler, Hit-and-Run and Metropolis-Hastings algorithm

In this study, we've considered a Bayesian network (BN) approach to model the signalling transduction pathways (STPs). With the standardized and discretized expression data for lapatinib-resistant cell-lines (SKBR3), we have conducted three MCMC sampling algorithms to search through a space of Bayesian network models of a STP of interest: i.e. TGF-β signalling pathway. Those three MCMC sampling algorithms are: Neighbourhood sampler, Hit-and-Run sampler and Metropolis-Hastings sampler. For each of these samplers, we chose the threshold of the number parents and the number of children is 4. Each sampling algorithm ran for 5000 sampling iterations and the burn-in iteration was considered as 3000, which indicates the latest 2000 iterations were used for actual sampling. Figure 3A depicts the convergence of these three sampling algorithms, where Neighbourhood sampler (NS) starts to converge before Metropolis-Hastings (MH) and Hit-and-Run (HAR) samplers, but after the burn-in period (3000 iterations), all of them convergences were fairly observed.

At each sampling iteration, each sampler picks a candidate BN model that achieves the best log-likelihood score among all others in their neighbourhood BN space. When finished, each sampler returns the BN that was sampled with highest probability of sampled (highest frequency out of the remaining 2000 sampling iterations) as the optimal STP model for the TGF-β signalling pathway. Figure 3B-D, depicts three TGF-β BN models that were sampled from NS, HAR and MH samplers, respectively.

### Studying statistical properties of optimal STP reveals important genes that drive dys-regulation in lapatinib resistance

With the optimal STP model, we conducted experiment to observe the statistical aspect of the network formation with regards to their local structure formation. To that extent, we have used a fully Bayesian approach to infer the posteriori of each node's *sociality* information, which is analogous to its importance as hub-gene in its interactome, and thus reveals its potentiality of being a gene that drives the perturbation in the signalling pathway. We have used the MCMC sampling approach again to infer the posteriori of network parameters of the *p*<sup>1</sup>-model that represent the edge formation probability of an edge in the STP as a linear combination of several structure parameters, including α, the sociality parameters of involving node-pairs. This MCMC sampling algorithm was conducted for each of the three inferred TGF-β signalling pathways individually (see above) for 5000 iterations, 3000 of which were considered as the burn-in

![img-2.jpeg](img-2.jpeg)

Figure 3: MCMC sampling and inferred perturbation BN model for TGF-$\beta$ signalling pathway using Neighbourhood sampler, Hit-and-Run sampler, and Metropolis-hasting sampler.

period. When completed, MCMC sampling with these three BN models of TGF-$\beta$ signalling pathway yielded 31, 33, and 22 social genes with $\alpha$ values $>0$, respectively, that are listed along with their sensitive-vs-resistance log2 fold change in Table 1.

### Network analysis of aberrant STP

To observe the biological relevance of inferred driver genes in TGF-$\beta$ signalling pathways, we conducted GO term (Biological processes) enrichment using clueGO [21] plugin in Cytoscape. Figure 4A-C depicts the significantly enriched GO terms, where positive regulation of pathway-restricted SMAD protein phosphorylation, activin receptor signalling, regulation of androgen receptor signalling, regulation of lymphocyte differentiation, and regulation of hormone secretion are observed. Using *PathView* [22] R package, we have also shown TFG-$\beta$ signalling pathway diagram overlayed with the constituent genes/proteins with their log2 fold change values in Figure 5.

### Comparing with other methods in identifying aberrant STP

We have also experimented how our method performs in identifying pathway perturbation compared to other methods. There are several approaches for finding perturbed pathways or functional terms. SPIA (Signaling pathway impact analysis) [23] is one of such approaches, which not only considers the functional enrichment tests but also the abnormal perturbation (based on pathway topology) of that pathway given a set of DE markers. SPIA have found that, both of

Table 1: Perturbation drivers for three TGF- $\beta$ signalling pathway models identified by MCMC sampling


![img-3.jpeg](img-3.jpeg)

Figure 4: Functional enrichment of perturbation driver genes
those experiments are not necessarily dependent to each other, i.e. evidence from both of those tests signifies somewhat independent biological evidence. Hence, SPIA conducts both (perturbation test + enrichment tests) and statistically combines their significance and provides a combined significance level, namely $P G$. For mathematical details, please refer to the original article [23]. The left panel of Figure 6 shows Log2 fold-change vs perturbation accumulation scores for TGF- $\beta$ signalling pathway (KEGG pathway ID = hsa04350) with their 9 enriched DEGs. Moreover the right panel shows the density plot of total perturbation accumulation scores and a probability of perturbation. As we can see from this plot that SPIA has detected TGF- $\beta$ signalling pathway as perturbed with the probability of perturbation, $\mathrm{pPERT}=$ 0.038 ( $<0.05$ ), which is also coherent with our findings.

![img-4.jpeg](img-4.jpeg)

Figure 5: Perturbation detection of TGF- $\beta$ signalling pathway using PathView

# Discussion 

In this study, namely 'PathTurbEr', we provide a novel probabilistic approach of data-driven modeling of aberrant signal transduction pathways (STPs) via solving Bayesian Network structure learning problem, where each STP was modelled as a Bayesian Network. We adopted three MCMC sampling algorithm for this structure learning tasks, namely Neighbourhood sampler, Hit-and-Run sampler and Metropolis-Hastings sampler, where each of the sampling algorithm yielded an optimal STP BN model that best describes the aberration activities that are latent in two conditional studies, e.g. lapatinib resistant-vs-sensitive expression datasets. Note, this approach only models the aberrant activities in a signalling pathway of interest (e.g. TGF- $\beta$ signalling) by learning above two-conditional data, not just any data-driven structure of the signalling pathway. Next, we conducted MCMC sampling of the structural features of that those inferred STP to observe how the local feature can describe the overall structure formation probability by employing a fully Bayesian statistical modelling approach with $p_{1}$-model. This experiment yielded a set of important genes, namely social genes (analogous to hub genes in the interactome), in those aberrant BN models of STPs. Functional enrichment test and comparison with state-of-the-arts methods confirms the significant functional relevance of the inferred driver genes. This robustly summarizes the important contribution of our approach to this problem.

A set of bio-markers detected by differential expression analyses followed by the their functional pathway enrichment tests manifested several signalling pathways revealing perturbed expression in resistant-vs-sensitive conditions, including PI3K-AKT signalling, Hippo signalling, Chemokine signalling, TGF- $\beta$ signalling, and Thyroid hormone signalling. TGF- $\beta$ signalling has been reported to be contributing in resistance mechanism to targeted treatment in HER2-positive breast cancer [24]. Komurov et al. also reported TGF- $\beta$ signalling pathway as perturbed in resistant-vs-sensitive conditions in acquired lapatinib resistance in breast cancer cell-line, SKBR3 [12]. Tortora et al. previously reported that TGF- $\beta$ type I receptor activation is responsible for increased expression of HER ligands, and that mediates increased secretion of TGF- $\alpha$, amphiregulin, and heregulin, and that activates PI3K-AKT signalling pathway, which is also found to be perturbed in our analyses [25]. Moreover, our previous study of analysing drug-resistive cross-talks also revealed

![img-5.jpeg](img-5.jpeg)

Figure 6: SPIA analyses to detect perturbation of TGF- $\beta$ signalling pathway
that TGF- $\beta$ signalling pathway cross-talks with EGFR/HER2 signalling pathway via activation of TFG- $\beta$ receptor, and thus provide a compensating route for resistant cells to survive despite continuous drug intake, i.e. lapatinib [20].
Above evidence of TGF- $\beta$ signalling perturbation in resistant-vs-sensitive condition led us to investigate furthermore, which factors may drive this perturbation, i.e. if any bio-marker can be associated with this aberrant phenomenon. Therefore, we adopted a fully Bayesian statistical modelling approach in order to decipher important genes in a probabilistic manner. Unlike the frequentist/descriptive approach to identify hub genes as important genes in gene-gene relationship networks, probabilistic approaches adopt uncertainty in network formation, which is a intrinsic feature observed in biological networks, especially when derived from high-throughput experimental data [11]. Our hypothesis was that the statistically important genes in a given perturbation network structure in the context of connectivity, would indicate a key role underpinning the aberration. Results from this analysis revealed 31, 33, and 22 perturbation driver genes out of 79 constituent genes of three STP models of TGF- $\beta$ signalling yielded from Neighbourhood sampler, Hit-and-Run sampler, and Metropolis-Hastings sampler, respectively 1. Out of these perturbation driver genes found by MCMC sampling, 9 genes, namely THBS1, TGFB2, TGFBR2, ID4, E3F5, CREBBP, CDKN2B, BMP7, and PITX2 were also identified as differentially expressed (first 7 genes were up-regulated whereas remaining were down-reguated) in resistant-vs-sensitive conditions in lapatinib resistance, in our independent differential expression analyses.
Next, we aimed to observe the functional association of these putative genes driving the signalling perturbation by conducting an over-representation test with a set of GO terms (Biological process). We hypothesized that, the perturbation driver genes would be associated with many important biological functions triggered by TGF- $\beta$ receptor signalling that are relevant to breast cancer progression/resistance phenomenon. We have observed several biological functions including positive regulation of pathway-restricted SMAD protein phosphorylation, regulation of lymphocyte differentiation, positive regulation of transmembrane receptor protein serine/threonine kinase signaling, regulation of activin receptor signalling, cellular response to growth factor stimulus, regulation of tgf-beta receptor signalling, and cellular response to BMP stimulus. It has been reported that TGF- $\beta$-SMAD signalling plays significant role in EGFR/HER-positive breast cancer oncogenesis [26, 27]. Chen et al. recently reported that tumor infiltrating

lymphocytes serves as critical pathological factor in predicting prognosis of breast cancer patients that are treated with anti-HER2 drugs, in our case which is lapatinib [28]. The role of serine/threonine kinase signaling involving trans-membrane receptor proteins is well reported, i.e. it controls both cell proliferation and cell death in response to various stresses [29]. Jeruss et al. has also reported that regulation of both TGF- $\beta$ and activin signalling components are associated with advanced oncogenic progression in aggressive breast carcinoma [30]. BMPs are found over-expressed in breast cancer patients, but results from Owens et al. suggested that the inhibition of BMP stimulated signalling may reduce breast cancer metastasis by targeting both the tumor and its surrounding micro-environments [31].

# Conclusion 

Resistance to targeted therapies is a major obstacle in sustained and efficacious treatment plan for fighting against any cancer. Lapatinib, an EGFR/HER-2 dual inhibitor, although shown great initial promise in treating breast cancer patients, have ultimately been bypassed by the cancer-cells' alternate survival mechanism via compensatory pathways. Therefore, a root-cause analysis i.e. detection of bio-markers driving the pathway perturbation in resistant-vs-sensitive conditions with a robust framework is greatly needed to offer better therapeutic developments. Previous approaches mainly adopted descriptive methodologies with less emphasis on the stochastic phenomenon, which is very commonly exist in biological systems. Hence, 'PathTurbEr' adopts statistical models (e.g. Bayesian networks) to detect aberrant signalling networks, followed by fully Bayesian statistical approach to identify the markers driving those perturbation. Our framework has been developed in a generalized way, therefore we hope that it can be applied to any case-vs-control expression studies, and analyse similar hypothesis for any given cancer datasets.

## Competing interests

The authors declare that they have no competing interests.

## Author's contributions

AKMA and SA conceived the idea. SA contributed to the MCMC sampling method design for Bayesian network inference from data. AKMA contributed the methodologies for statistical parameter sampling methodologies using MCMC methods. AKMA conducted the experiments, analysed the data and wrote the manuscript. SA contributed to the manuscript.

## Additional Files

## Additional file $1-512$ DEGs and their function enrichment results with 45 KEGG signalling pathways
