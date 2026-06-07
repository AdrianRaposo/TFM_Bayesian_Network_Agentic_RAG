# ARTICLE 

DOI: 10.1038/s41467-018-06867-x OPEN

## Mutational interactions define novel cancer subgroups

Jack Kuipers ${ }^{1,2}$, Thomas Thurnherr ${ }^{1}$, Giusi Moffa(1) ${ }^{3,4}$, Polina Suter ${ }^{1,2}$, Jonas Behr ${ }^{1}$, Ryan Goosen ${ }^{5}$, Gerhard Christofori ${ }^{5}$ \& Niko Beerenwinkel(1,2

Large-scale genomic data highlight the complexity and diversity of the molecular changes that drive cancer progression. Statistical analysis of cancer data from different tissues can guide drug repositioning as well as the design of targeted treatments. Here, we develop an improved Bayesian network model for tumour mutational profiles and apply it to 8198 patient samples across 22 cancer types from TCGA. For each cancer type, we identify the interactions between mutated genes, capturing signatures beyond mere mutational frequencies. When comparing mutation networks, we find genes which interact both within and across cancer types. To detach cancer classification from the tissue type we perform de novo clustering of the pancancer mutational profiles based on the Bayesian network models. We find 22 novel clusters which significantly improve survival prediction beyond clinical information. The models highlight key gene interactions for each cluster potentially allowing genomic stratification for clinical trials and identifying drug targets.

[^0]
[^0]:    ${ }^{1}$ Department of Biosystems Science and Engineering, ETH Zurich, 4058 Basel, Switzerland. ${ }^{2}$ SIB Swiss Institute of Bioinformatics, 1015 Lausanne, Switzerland. ${ }^{3}$ Division of Psychiatry, University College London, London WC1E 6BT, UK. ${ }^{4}$ Institute for Clinical Epidemiology and Biostatistics, University Hospital Basel, 4031 Basel, Switzerland. ${ }^{5}$ Department of Biomedicine, University of Basel, 4058 Basel, Switzerland. Correspondence and requests for materials should be addressed to J.K. (email: jack.kuipers@bsse.ethz.ch) or to N.B. (email: niko.beerenwinkel@bsse.ethz.ch)

The past years have seen great progress towards a deeper understanding of the molecular changes underpinning cancer progression. Identification and characterisation of molecular subtypes within and across different cancer types has emerged as a promising approach for the development of targeted therapies^{1--3}. Nevertheless, cancer treatment is far from optimal. The approval of the limited number of available cancer drugs is often limited to a specific cancer type or subtype, preventing widespread use of targeted therapies. Moreover, cancers may develop resistance against these therapies, rendering them ineffective^{4}.

Pancancer analyses enabled by large datasets such as The Cancer Genome Atlas (TCGA)^{5} or the International Cancer Genome Consortium (ICGC)^{6} may aid a better understanding of the disease biology across different tissues, and can, for example, identify mutational hotspots in tumours^{7}. Genes strongly associated with a cancer type or pancancer subgroups provide insights into the molecular mechanisms, which are key for pinpointing novel therapeutic opportunities and improving current treatment strategies. For example, analysis of endometrial carcinoma showed genetic similarities to certain types of breast and ovarian cancer^{8} while olaparib, approved for BRCA-mutated ovarian cancer, provided a good response in metastatic prostate cancer patients with DNA repair mutations^{9}. Pancancer, or basket, clinical trials^{10} could extend targeted treatments beyond their current indication, like testing the BRAF inhibitor vemurafenib outside of metastatic melanoma^{11}, or test novel agents, like Loxo Oncology's trial of larotrectinib for patients with a TRK gene fusion mutation. Recently, the FDA granted its first approval for a drug (pembrolizumab) based on genetic markers, regardless of the tissue type.

Cancer is known to be a disease characterised by a progression of molecular changes leading to malignant features and activities^{12,13}. Alongside stratifying tumours based on static molecular profiles^{14,15}, investigating their development^{16--22} may offer a new perspective on pancancer analyses with the potential to identify key drivers and provide benefits on multiple levels, including (1) prioritisation of mutation-based biomarkers; (2) uncovering previously unknown mutational dependencies; (3) identification of biomarkers of progression; and (4) biological insight into the genetic progression of cancer.

The facets of clustering patient samples, inferring their genetic tumour progression and mutational interactions are highly interrelated (Supplementary Section A). Here, we introduce a unified statistical framework to combine them by modelling the mutations as a Bayesian network. The probability of observing each mutation depends on the state of its parents in the network, thereby accounting for mutational interactions such as co-occurrence or mutual exclusivity, as well as more complex relationships. The directions of the connections may be suggestive of causal relationships^{23--25}, though they may not be fully resolved from the data.

We develop efficient methods to infer the dependency structure of the mutations and performed fully Bayesian inference (Methods) to capture the uncertainty in the network structure learned from mutational profile data. Characterising mutational data through Bayesian networks provides useful insights through the analysis of the mutational interactions encoded by the network, beyond just analysing mutational frequencies. We employ our Bayesian network modelling to cluster patient samples into groups, with different interactions among mutated genes. The key interactions within and across novel subgroups may uncover common mechanistic insights, potential therapeutic targets, and prognostic and predictive biomarkers.

## Results

### Analysis overview

We performed two distinct analyses of non-silent mutation data, summarised at the gene level for 201 genes, from 8198 patient samples across 22 cancer types (Supplementary Table 1) from TCGA. Initially, in a supervised analysis, we built cancer-specific probabilistic models to explore type-specific mutational interactions and pancancer heterogeneity. Then, in an unsupervised analysis, we proceeded to cluster the samples into novel mutational subgroups (Fig. 1).

### Cancer-specific Bayesian networks

Stratifying the TCGA mutation data by tissue of origin, we built Bayesian networks (Methods) separately for each cancer type. We obtained an alternative representation of the mutational landscape that goes beyond mutation frequencies by highlighting the interdependencies between genes. Edges show co-occurrence or mutual exclusivity, or higher order correlations between sets of genes, offering a systematic visualisation of the most important mutational interactions in 22 different cancer types (Fig. 2).

The network parameters estimated from the data capture information both about the mutational frequencies and about their interactions, allowing us to evaluate how well each model explains the mutational status of each patient sample (Methods), including those from other cancer type. Simulations show that our approach performs notably better than alternatives in learning the network structure (Supplementary Section B). It also improves on the potential to effectively characterise different cancer types with respect to simple distance-based measures (Supplementary Section C). The network structure inference is informed (Methods) by using the STRING protein-protein interaction network^{26} as a prior, but even without this information a comparison (Methods) reveals a significant overlap of the edges (permutation test; p = 4.1×10^{5}), suggesting the inferred network of mutational interactions is biologically relevant as known functional interactions coincide.

We rediscovered many key genes that have previously been associated with their respective cancer types. For example, genes ATM, PIK3CA and PTEN with a lot of connections in colorectal cancer (Fig. 2) have previously been reported as highly mutated^{27}. In lung adenocarcinomas, we recapitulate the mutual exclusivity between KRAS and EGFR as well as the importance of TP53^{28}, for which our model suggests that it is frequently co-mutated with both KRAS and others like MLL3, as well as KRAS and STK11 are frequently co-mutated.

TP53 is a major hub with the most interactions across multiple cancer types (67 in total) and with multiple dependencies in brain cancer and especially lower-grade glioma. TP53 mutations in lower-grade glioma have previously been associated with the disease, along with IDH1, FUBP1, ATRX, CIC, NOTCH1, EGFR, and PIK3CA^{29} among which we see some interactions. Similarly in glioblastoma, where in addition to TP53, we observe interactions involving PTEN, IDH1 and ATRX which were previously reported to be mutated^{30}.

Other hubs with high connectivity like TP53 include MLL2 (65 interactions), MLL3 (58), XYLT2 (56) and FAT1 (55). Mutations in these genes have previously been associated with cancer^{31--33}. MLL3 and FAT1 share connections across several cancer types, with both having several interaction in uterine cancer, while MLL2 exhibits many connections for stomach, and XYLT2 for oesophageal cancer.

Strong edges can hint at common mechanistic causes or fitness effects. For the example of FAT1, our study finds relevant interacting mutations in breast, colorectal, endometrial, kidney, lung, liver, stomach and head and neck cancer, with mutation rates between 2 and 24%. Although FAT1 was reported to be

![img-0.jpeg](img-0.jpeg)

Fig. 1 Overview of the analyses. Starting from the mutation data, we perform two types of analysis. Supervised learning of the Bayesian network structure for each known cancer type, allowing us to uncover mutational interactions and visualise pancancer heterogeneity. Unsupervised clustering of the mutation data into components with common interactions to uncover a novel stratification of the patient samples

recurrently mutated in several cancer types32,34,35, our results suggest that the gene correlates with a large number of mutations in different cancer types, including *FAT1* in breast cancer, *ATM* in colorectal cancer, and *APC*, *MTOR* and *MLL3* in endometrial cancer. On the pathway level, we found highly connected genes across cancer types to be significantly involved in many signal transduction pathways, as well as cellular processes and DNA damage repair (Supplementary Table 8).

Several genes with mutational interactions are putatively actionable, with drugs either approved or currently tested in a clinical study (labelled with black diamonds in Fig. 2). In general, approval of targeted therapies is limited to one or several cancer types or cancer subtypes. Strong dependencies in the Bayesian network potentially indicate effectiveness of targeted therapies against dependent gene mutations, particularly if it is in the same pathway. Moreover, the network potentially expands the group of tumours responsive to a specific targeted therapy, within the same tumour types and between different tumour types. Although the drugs are only targeting the mutation itself, we see for example several interactions of *KRAS* in lung adenocarcinoma (with *TP53*, *EGRF* and *STK11*) and there are currently several clinical trials investigating the effectiveness and safety of targeted therapies against *KRAS* for this cancer type (NCT02642042, NCT01912625 or NCT02079740).

A two-dimensional visualisation based on multiscale projections (Methods) highlights the differences and similarities of patient samples as measured over the Bayesian networks, within and across cancer types (Fig. 3). Some, like colorectal, thyroid and lower grade glioma, are well separated and hence well defined by the mutation profiles of their patient samples; others are much more similar, for example those within overlapping groups. Even for the better separated cancer types, we observe substantial heterogeneity with some patient samples closer to those from other cancers.

As well as being applicable to pancancer cohorts, these methods naturally apply when focussing on individual cancer types and their subtypes (as we discuss for breast cancer in Supplementary Section D).

De novo clustering based on Bayesian networks. Given the considerable heterogeneity across cancer types, we asked ourselves whether the mutation profiles themselves can be reclustered on the basis of Bayesian network models without knowing the cancer types. This model-based de novo clustering of the binary mutation data (Methods and Supplementary Section F) identified 22 groups, coincidentally the same number as the original cancer types (which was not imposed), but distinct in their composition. Each cluster is defined by a Bayesian network which constitutes a generative model of its patient data. These models fit the data much better than the partitioning by cancer type—the average cluster assignment is 91.5% compared to 71.9% for the cancer-specific models.

The composition of the clusters (Fig. 4) shows that the more differentiated cancer types, like colorectal, thyroid and lower grade glioma from the 2D projection (Fig. 3) initiate new clusters. Clusters G and I are mostly composed of glioma and colorectal samples respectively. Almost all thyroid cancer samples belong to cluster V, along with samples from other cancer types, and this cluster exhibits a strong enrichment in *BRAF* mutations (17% compared to an overall rate of 7%, Supplementary Table 9). Cluster K, where *TP53* plays a strong role, mostly consists of colorectal samples, and cluster L of leukaemia with *IDH* mutations being prominent. The ovarian cancer samples belong almost entirely to cluster U (where all samples exhibit a *TP53* mutation). Samples with no mutations among the 201 genes are assigned to cluster V.

The de novo clustering also split patient samples from the same cancer type, like the glioma samples into clusters G and N: cluster N has elevated mutation rates in *TP53* and *ATRX* which are largely absent from cluster G which instead has elevated rates of *CIC* as well as even higher rates of *IDH1* than N (98% compared to 86%). Patient samples from certain cancer types may actually be more similar to tumours in other cancers. Cluster S, for example, groups samples of several different cancer types, including bladder, breast, liver and lung cancers and possesses elevated mutation rates in several genes, like *TP53*, *MLL*, *ARID* and *CTNNB1*.

![img-1.jpeg](img-1.jpeg)

**Fig. 2** The cancer-specific connections between the genes. For clarity, we limit the display to only include connections between the 20 most frequent and connected mutations per cancer type. The Bayesian networks for each cancer type are overlaid on the same union of gene nodes. Edges highlight interactions between the selected mutations and are coloured by the cancer type for which they occur (leukaemia: yellow; glioblastoma: green, etc.). Directed edges point in the inferred direction of dependency, whereas undirected edges indicate cases where the direction cannot be inferred. Solid edges indicate positive correlation (a degree of co-occurrence) while dashed edges indicate negative correlation (a degree of exclusivity) between the genes connected. Genes are coloured according to the colours of their edges. Those with edges in only one specific cancer type are grouped and labelled with the same colour. Genes with edges in different cancer types are arranged in the two circles in the centre. The size of each gene correlates with the total number of edges across all cancer types, including edges that are not shown. Black diamonds mark putatively actionable targets.

For cancers with known subtypes, the clustering recovered some of these differences. For example, the microsatellite stable subtype of uterine cancer has a rather different cluster composition than the other uterine patient samples (Supplementary Fig. 14), with enrichment moving from clusters M and U to A and F. Similarly, the colorectal subtypes are quite distinct in their cluster composition. For the breast cancer patient samples, the luminal subtypes, especially luminal A, have a strong presence in clusters T and V while the basal and Her2 enriched subtypes are mostly absent from these clusters and appear preferentially in cluster U instead.

The clusters are highly significant in predicting survival (likelihood ratio = 37.0; p = 7.6×10<sup>−8</sup>), also accounting for clinical and histopathological information (age, stage, and cancer type; Methods), showing that considering the mutation data and their interactions provides a more complete and informative picture of tumours and their progression. The Bayesian network clustering also performs favorably in survival prediction compared to a range of standard clustering approaches (Supplementary Table 6).

The clustering is based solely on the mutation data, so we also compared individual clusters without adjusting for clinical and histopathological information. We observed significant differences (Fig. 4 and Supplementary Table 3) showing that the clustering uncovers strong biological signals. In particular, clusters G, M, T, and V show good survival (5-year overall survival of 70–80%), whereas clusters B, P, and R show poor survival; cluster B has the poorest outcome with a 5-year overall survival of just over 30%.

Some of the differences between individual clusters can be explained by the mutational profiles correlating with and recapitulating clinical and histopathological variables. When we remove the confounding by age, stage, and cancer type, clusters G, J, N, and U are still significantly different compared to reference (cluster V, Supplementary Table 4). Clusters G and N both contain a large fraction of lower grade glioma patient samples and have good survival. The cancer type is adjusted for in the survival analysis, meaning that the improvement in survival predictions is due to the diverse patient samples that are clustered with them (Fig. 4) along with the separation of lower grade glioma into two

![img-2.jpeg](img-2.jpeg)

**Fig. 3** Visualisation of pancancer heterogeneity. 2D visualisation of the similarity between patient samples based on their fit to each cancer-specific Bayesian network, highlighting the heterogeneity within and across cancer types. For example, stomach, breast and liver cancer show high inter-tumour heterogeneity with a high spread across the plot, whereas pancreatic cancer shows low inter-tumour heterogeneity and is much more localised. Ovarian and breast cancers as well as bladder cancer and lung adenocarcinomas show similar mutational profiles, while lower grade glioma is rather distinct from other cancer types, as is thyroid cancer. The solid shapes are based on contours that together contain a total of 50% of the respective cancer types. The group of samples on the lower right possess no mutations among the 201 genes while those exhibiting a mutation only in *TP53* are also indicated. Versions highlighting certain cancer types are displayed in Supplementary Fig. 5.

Main groups. Clusters J, with a large group of lung adenocarcinomas, and U have significantly poorer prognosis.

Some cancer types are split by the clustering, with one portion forming the bulk of a cluster, and show differences in survival between the patients assigned to different clusters. For example, leukaemia samples in cluster L show a significantly lower lethal risk compared to samples in cluster V (hazard ratio = 0.51; *p* = 0.012). Lower grade glioma samples in cluster N have a non-significantly higher risk than those in cluster G (hazard ratio = 1.64; *p* = 0.056). Similarly colorectal samples in cluster K show non-significantly higher lethal risk than colorectal samples in cluster I (hazard ratio = 1.67; *p* = 0.063), in line with the fact that cluster K contains a large number of samples from the MSS subtype which has the worst outcome[36].

The probabilistic model describing each cluster can be utilised to visualise the important mutational interactions characterising the mutation profiles of its samples (Fig. 5). The cluster composition is distinct from the grouping by cancer (Fig. 2), even for clusters dominated by one cancer type such as cluster B, G, I or J, so that the key interactions mostly differ, especially when focussing on 20 genes per cluster for clarity.

*TP53*, as the most frequently mutated gene across all cancer types, remains fairly prominent when clustering samples by their mutation profile. Looking at its connections among all genes, these differ substantially across the clusters even when the marginal frequency is similar (Fig. 6), suggesting that it plays different roles in different clusters. Our approach emphasises mutational interaction patterns which are specific to a cluster. Along with its interactions, the prevalence of *TP53* in each cluster is also used in assigning patient samples. For example all members of cluster U possess a *TP53* mutations while none of cluster V do.

Among the clusters, genes such as *ERBB2* (37 interactions), *MSH3* (36) or *CDKN1B* (33) have more interactions than *TP53* (32) in total. Of the selected interactions (Fig. 5), *ERBB2* has connections particularly for clusters T and M, and for cluster M interacts with *CTNNB1*. *PIK3CA* has several interactions, including three for cluster C (with *TP53*, *CTNNB1* and *VHL*), a cluster dominated by colorectal cancer samples.

We found several cancer-associated signalling pathways significantly enriched in highly connected genes across clusters, including HIF-1, Jak-STAT, p53, Toll-like receptor, and TNF signalling (Supplementary Table 10). These results suggest that genes involved in signalling pathways are not only highly connected, with a large number of mutational interactions with other genes, but that they also play an important role in characterising the clusters.

Clustering samples by their mutational profile, independent of their cancer type, provides an alternative patient stratification which may inform targeted treatment (putatively actionable genes are marked by black diamonds in Fig. 5). For example, *BRAF* inhibitors are being currently tested or have already been approved for multiple cancer types, including lung cancer, ovarian cancer, and thyroid cancer[37]. Substantial fractions of these cancer types are grouped in the single cluster V (for which *BRAF* exhibits three interactions in Fig. 5). The similarity of mutational profiles to other cancer types in cluster V suggests that they may be responsive to the same targeted treatment, such as

![img-3.jpeg](img-3.jpeg)

Fig. 4 De novo clustering. a Assignment of the 8198 patient samples to the 22 clusters, labelled A–V, based on Bayesian network clustering of their mutation profiles. The left-hand side of the bar for each cluster indicates the number of patient samples with a given cancer type, while the right-hand side indicates the breakdown into the known subtypes. b Survival probabilities of the 22 clusters

BRAF inhibitors, provided the targeted gene or pathway is mutated.

## Discussion

We modelled mutational profiles with Bayesian networks, which capture the interactions between mutations, in a pancancer setting across 22 cancer types. Clustering of pancancer data can be highly insightful into the molecular similarities across cancer types[14,15]. In order to concurrently model cancer heterogeneity and mutational interactions we combined the Bayesian network approach with clustering in an integrated framework. The challenge for network clustering of large datasets resides in achieving reliable inference of networks with many nodes. Therefore we also developed methods for fast network learning for large data (Methods), so to extend the analysis to a couple of hundred important genes. Larger networks than those analysed may not lead to any further benefit, since many cancer mutations are quite rare and therefore unlikely to show strong interactions detectable in network modelling.

Mutations can be modelled at different levels, from the finer scale of individual mutation sites or hotspots[7] up to the pathway level. Higher resolution comes at the cost of lower frequencies, but this could be balanced out by combining aberrations by their molecular or pathway functions. A powerful alternative could be to use diffusion algorithms to condense aberrations to their affected subnetworks[38] or mediator genes[39]. Here we focussed on mutation data summarised at the gene level, which contain a large amount of information. Mutational profiles are one genomic lens through which to identify molecular subtypes which can then complement other views based on, for example, copy number, expression and methylation profiles[15] and there may also be interactions across data modalities. Cancers can be highly heterogeneous, potentially harbouring distinct clones with different mutational profiles and prognostic signatures. Finer modelling of clonal structure and its impact on patient stratification present substantial challenges, as well as opportunities for more precise treatment options.

Furthermore, we account for uncertainty in the network structure through a fully Bayesian approach (Methods). The networks learnt provide the key gene interactions characterising each cancer type (Fig. 2) and a significantly extended view over just mutational frequencies. Along with the edges, the networks also utilise the frequency of each mutation to quantify how similar or disparate the mutation patterns of patient samples are within and across cancer types (Fig. 3).

Because the networks we infer are related to a class of clustering methods, we directly employed our models to re-cluster the TCGA data. We discovered and characterised 22 clusters in the data, distinct from the original cancer types but happening to match in number. New patient samples, including mutation profiles from different tumour types, can also be classified into the clusters, for which we provide a web application (Software). The new clusters significantly improve survival prediction, over and above that from the clinical and histopathological status of each patient sample. Integrating this information along with the mutational profiles during the clustering could further improve the survival prediction. Different types of mutations can occur and mutations also have different functional impact, which may affect their potential interactions, and may have different effects in different tissues. Accounting for such interactions could offer further refinements.

The Bayesian network modelling and clustering developed here provides us with insights into the mutation events and specifically their dependencies in cancer types and in novel cancer subgroups. These can be used as biomarkers which may be explored experimentally for therapeutic intervention.

## Methods

Cancer mutation data. Mutation annotation files were obtained through GDAC Firehose[40] for the 22 cancer types with sequenced primary tumour samples from more than 100 patients (see Supplementary Table 1), giving a total of 8198 patient samples. The 16 most significantly mutated genes for each cancer type were collated to give a total of 201 genes considered. The different sample sizes and potentially different effect sizes makes comparing the significance of gene mutations challenging across cancer types. We found such comparisons led to gene lists dominated by a small number of cancer types, with correspondingly fewer discriminatory pancancer markers. Instead, a fixed number per cancer type was employed to ensure markers were retained for each cancer type to better characterise inter-tumour heterogeneity. A binary matrix of the non-silent mutations in these genes across all patient samples was generated.

Putatively actionable targets are identified based on approved drugs or drugs currently undergoing clinical studies as collected by MyCancerGenome[37], a manually curated precision cancer medicine knowledge resource. MyCancerGenome was queried through rDGIdb[41,42]. Functional annotation of genes was performed using the KEGGREST package[43].

![img-4.jpeg](img-4.jpeg)

**Fig. 5** The cluster-specific connections between the genes. The connections between the 20 most frequent and connected genes per cluster (rather than per cancer type, as in Fig. 2). Black diamonds near nodes indicate putatively actionable genes. Edges highlight interdependencies between the selected mutations: solid for positive and dashed for negative correlation. Directed edges point in the inferred direction of dependency, whereas undirected edges are where the direction cannot be inferred. Node size reflects the total number of edges, including edges not shown. Nodes are coloured by combining the colours of their edges from the different clusters.

**Graph inference.** To quantify the extent to which a Bayesian network can explain a set of binary data, we use the BDe score[44] where the state of a node *X* is determined by a different parameter θ<sub>*Y*</sub> for each configuration of its *m* parents **Y**: *P*(*X* = 1 | **Y**) = θ<sub>*Y*</sub> with a beta prior on each θ<sub>*Y*</sub> with hyperparameters α = β = 1/2, defined in terms of a single parameter χ which represents the number of pseudocounts added.

To make inference of the Bayesian network structure, which is a directed acyclic graph (DAG), we adopt a modified version of order MCMC[45,46]. For large networks we search over a reduced skeleton, initially found via the PC algorithm[47] and then expanded by MCMC search using the software package **BiDAG**[48]. From the final skeleton, a sample from the posterior is obtained using partition MCMC[46] optimised for such a skeleton[48].

**Prior edge knowledge.** We obtained all human functional interactions from STRING[26], selecting those between the 201 genes included in this study (≈7000 interactions). Edges that were not in this STRING network were penalised by a factor 2 for the graph inference.

**Additional edge penalisation.** When examining the networks learned from binary data, as in Figs. 2 and 5 we additionally penalise all edges. Edge penalisation (by a factor of 2) has previously been examined with the marginal uniform prior[49] and shown to improve network reconstruction. Based on simulation studies (Supplementary Section B) we find stronger regularisation further improves the accuracy for data mimicking the TCGA and employ a factor of 16 to regularise the network. We sample 100 DAGs from the posterior. Edges are only displayed if they appear in at least half of the posterior sample.

To select genes to display per cancer type or per cluster in Figs. 2 and 5, for each gene we multiply its number of connections by its frequency, and choose the 20 genes with the largest product.

**Scoring samples against DAGs.** For a given DAG the posterior distribution of each node *X* given its parent state **Y** is again a beta distribution with updated parameters α + a<sub>*Y*</sub> and β + β<sub>*Y*</sub>, where a<sub>*Y*</sub> is the number of times *X* takes the value 1 when the parents are **Y** and β<sub>*Y*</sub> is the number of times it takes the value 0 in the data. Hence the likelihood

$$P(X = 1|G, Y) = \hat{\theta}_Y = \frac{\alpha + \hat{\alpha}_Y}{\alpha + \hat{\alpha}_Y + \beta + \hat{\beta}_Y} \tag{1}$$

can be evaluated for each node of an arbitrary observed binary vector **X**, providing a measure of fit of the observed vector to the DAG.

Given a sample of *M* DAGs from the posterior distribution *P*(*G* | *k*) of different cancer types (indexed by *k*), we can score each patient sample *D*<sub>*i*</sub> against each DAG *G*<sub>*j*</sub> (dropping the index for the cluster *k*). From the sample we can build the Monte Carlo approximation to the likelihood of the data for a given cluster *k*

$$P(D_i|k) \approx \frac{1}{M} \sum_{j=1}^{M} P\left(D_i|G_j\right) \tag{2}$$

using the likelihoods in Eq. (1). Under a uniform prior over cancer types, the likelihoods in Eq. (2) are normalised to probability vectors over the collection of cancer types according to *P*(*k*|*D*<sub>*i*</sub>) ∝ *P*(*D*<sub>*i*</sub>|*k*)*P*(*k*). Similarities between the probability vectors of different patient samples are computed as their Jensen-Shannon divergence. Calculating this divergence between all pairs of patient samples provides a distance matrix between patient samples which we project into 2D with multidimensional scaling using the **cmdscale** command in **R**, as in Fig. 3.

**Clustering with frequency information.** We cluster the data with a mixture model. Given *K* graphs and parameter sets (*G*<sub>*k*</sub>, θ<sub>*K*</sub>), we assume that each patient sample *D*<sub>*i*</sub> is generated from one of *K* models depending on the value of a latent

![img-5.jpeg](img-5.jpeg)

**Fig. 6** Focus on *TPS3*. **a** Cancer types or **b** clusters are characterised by interactions of *TPS3* with different genes. For cancer types or clusters where *TPS3* shows a similarly high mutation frequency (around 0.5), we display all its interactions (positive correlation is represented by solid arrows, negative correlation by dashed). Groups are annotated by the cancer type or cluster name and the respective mutation frequency of *TPS3* across samples (in brackets). Several of these interactions have been studied in cancer. For example, an inverse relationship between *ARID1A* and *TPS3* was previously observed in gastro-intestinal cancers52 while *TPS3* mutations co-occur with *RB1* in bladder cancer53

variable *Z<sub>i</sub>*

$$D_i \left| (Z_i = k) \sim (G_k, \theta_k) \right| \tag{3}$$

with

$$P(Z_i = k) = r_k \tag{4}$$

To start we allow no edges between the nodes. The different parameters *θ<sub>k</sub>* we learn for each empty graph *G<sub>k</sub>* only depend on the mutation frequencies in each group and do not account for any correlations between them. A Dirichlet prior is assumed on the cluster probabilities *τ* with all the parameters set to the value *χ*.

We find the maximum a posteriori (MAP) estimates of the mixture model parameters and the cluster membership probabilities of patient samples using the EM approach. This model-based clustering can also be seen as a latent class analysis50 where we include prior information. Without the prior (or taking the limit *χ*→0), and without edges in the graph and hence independence between mutations, this clustering reduces to a Bernoulli mixture model.

**EM MAP algorithm**. To find the MAP estimates for the mixture model we repeat the following steps: (1) given the membership probabilities, update the posterior parameters, and (2) given the updated parameters, update the probabilities. This is repeated until the probabilities and parameters no longer change.

At each step *t* of the algorithm we start with the current membership probabilities *T<sub>jk</sub><sup>(t)</sup>* of each patient sample *i* being in cluster *k*. From the membership probabilities we can derive the cluster probabilities (as relative cluster sizes)

$$\tau_k^{(t)} = \frac{\bar{\chi} + \sum_{i=1}^{N} \overline{T_{jk}^{(t)}}}{\bar{\chi} K + N},\tag{5}$$

where *N* is the number of patient samples. A weighted version of Eq. (1) gives the posterior means for each node *j* in the empty graph of each cluster:

$$\theta_j^{(t)} = \frac{\bar{\chi} + \sum_{i=1}^{N} D_{ij} \overline{T_{jk}^{(t)}}}{\bar{\chi} + \sum_{i=1}^{N} \overline{T_{jk}^{(t)}}},\tag{6}$$

where *D<sub>ij</sub>* is 1 if patient *i* exhibits mutation *j* and 0 otherwise so that it acts as an indicator function in the sum. From this we can directly evaluate *P*(*D<sub>i</sub> | G<sub>k</sub>, θ<sub>k</sub>)*

$$\ln \left[P(D_i | G_k, \theta_k)^{(t)}\right] = \sum_{i=1}^n D_{ij} \ln \left[\theta_j^{(t)} \right] + (1 - D_{ij}) \ln \left[1 - \theta_j^{(t)} \right] \tag{7}$$

again using *D<sub>ij</sub>* as an indicator function.

Then we update the membership probabilities to start the next iteration

$$\overline{T_{jk}^{(t+1)}} = \frac{\tau_k^{(t)} P(D_i | G_k, \theta_k)^{(t)}}{\sum_{k=1}^K \overline{T_{jk}^{(t)}} P(D_i | G_k, \theta_k)^{(t)}} \tag{8}$$

and repeat the iterations until they no longer change.

The case where each patient sample has their membership probability equally spread across the clusters constitutes an unstable equilibrium for the mixture. To initialise the algorithm we therefore add a small random perturbation to this equilibrium to start with almost uniform probabilities *T<sub>jk</sub><sup>(0)</sup>* ≈ $\frac{1}{K}$.

**Cluster discovery**. The global parameter *χ* quantifies the tradeoff between the within cluster variability and the number of clusters. Larger values of *χ* place less importance on each data point and lead to fewer larger clusters. Decreasing *χ*, the clusters break up leading to progressively more clusters. Since each clustering is stochastic, we run the clustering 240 times with different initial perturbations and retain the best. To find the optimal value of *χ* and number of clusters *K* we vary both and calculate a modified version of the AIC (Supplementary Section E). For each value of *χ* we choose the number of clusters with the lowest AIC and scan through a range of *χ* values. To select *χ* we chose the value whose clustering has the highest overlap (measured with the normalised mutual information) with clustering results for the range of *χ*.

**Clustering with structure learning**. Allowing edges between the mutations in the DAG models refines the clustering. For each cluster we repeatedly learn the MAP DAG and reassign samples accordingly until convergence. In particular, we repeat the following steps: (1) given the current membership probabilities, learn the MAP graph structure, and (2) given the graph structure, repeat till convergence: (2i) given the membership probabilities, update the graph parameters, and (2ii) given the updated graph parameters, update the probabilities. We separate out learning the graph structure from updating its parameters since the latter is much less computationally demanding than the former. For given graph structures, the parameters and membership probabilities are continuous so the inner loop will converge. However since the graph space is discrete, periodic solutions for the outer loop are possible which can be alleviated by replacing the single graph in each cluster by a collection.

Once the clustering has converged and the final membership probabilities have been learnt, we sample 100 DAGs from the posterior of each cluster and visualise their connectivity and clustering features.

**Survival analysis**. For each of the patient samples, we obtained the most recent clinical information51. Patients with missing clinical data were removed, leaving 8085 subjects. To evaluate the prognostic power of the clusters derived from the mutational data for survival prediction, we employed the Cox proportional hazards model, with and without adjustment for age, stage and tissue type which are all significant predictors. The model fit with and without the cluster indicator

was evaluated by the likelihood ratio test, based on the asymptotic $\chi^{2}$ distribution.

The possible values for stage were I, II, III, IV, along with unclassified values of '[Not Applicable]', '[Not Available]', '[Discrepancy]', '[Unknown]', and 'Stage X'. The '[Not Applicable]' category is entirely determined by the tissue type and hence does not affect the regression when adjusting for tissue type. The remaining categories other than '[Not Available]' consisted of only 56 patient samples. Performing a Cox regression with adjustment for age and tissue type indicated that keeping those categories separate did not lead to significantly better predictions (likelihood ratio $=1.2 ; p=0.13$ ) due to their small sizes. All the unclassified values were hence combined into a single stage X. Keeping stage I and stage II separate led to significantly better survival prediction compared to their combination into a single category, and similarly for stage III and IV, and hence all stages were kept separate. Therefore five levels (whose size is summarised in Supplementary Table 5) were retained for the stage covariate in the Cox regression.

Modelling survival on the basis of the clinical data available from TCGA is challenging, due to intrinsic limitations in the data ${ }^{21}$, including, for example, relatively short follow-up times as well as heterogeneity in data collection and cohort selection across the different cancer types. Therefore, although we adjust for cancer type in our Cox regressions and use the same survival model to compare different clustering methods, there may be other effects like cancer-type-specific confounding not accounted for.

Overlap with functional network. To compare the STRING ${ }^{26}$ network to the Bayesian networks inferred in this study we re-ran the analysis without using the functional STRING network as a prior. We then created the union of all edges in the Bayesian networks over all cancer types. We performed a permutation test on the overlap between these two networks by generating one million random permutations of the gene labels in the functional network. For each permuted network, we computed the mean overlap to derive the empirical $p$ value.

A web interface to classify new patient samples is at https://cbg.bsse.ethz.ch/ pancancer/.The package BiDAG for Bayesian network inference is at https://CRAN. R-project.org/package=BiDAG. R code for the Bayesian network clustering and survival analysis is available at https://github.com/cbgethz/pancancer-clustering.

Code availability. The network inference code is available at https://CRAN.Rproject.org/package=BiDAG. The clustering and survival analysis code is available at https://github.com/cbg-ethz/pancancer-clustering.

## Data availability

The mutational profiles and clinical information of the patient samples used in the study are available at https://github.com/cbg-ethz/pancancer-clustering, along with their cluster assignments.

## Received: 20 September 2017 Accepted: 1 October 2018 Published online: 19 October 2018

## Acknowledgements

J.K. was supported by ERC Synergy Grant 609883 (http://erc.europa.eu/). T.T. was supported by EU Horizon 2020 PHC Grant 633974 (SOUND).

## Author contributions

J.K., G.M., J.B., and N.B. designed the study. J.K., G.M., and P.S. developed the methodology. T.T. collated the data. J.K., T.T., and R.G. performed the analyses. J.K., T.T., G.
M., and R.G. drafted the article. G.C. and N.B. critically reviewed the manuscript. All authors approved the final version.

## Additional information

Supplementary Information accompanies this paper at https://doi.org/10.1038/s41467-018-06867-x.

Competing interests: The authors declare no competing interests.
Reprints and permission information is available online at http://npg.nature.com/ reprintsandpermissions/

Publisher's note: Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/ licenses/by/4.0/.
(c) The Author(s) 2018