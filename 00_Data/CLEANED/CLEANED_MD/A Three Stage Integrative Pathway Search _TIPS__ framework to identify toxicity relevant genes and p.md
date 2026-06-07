# A Three Stage Integrative Pathway Search (TIPS®) framework to identify toxicity relevant genes and pathways 

Zheng Li ${ }^{1,4}$, Shireesh Srivastava ${ }^{1,6}$, Sheenu Mittal ${ }^{1,5}$, Xuerui Yang ${ }^{1}$, Lufang Sheng ${ }^{1}$ and Christina Chan*1,2,3


#### Abstract

Address: ${ }^{1}$ Department of Chemical Engineering and Materials Science, Michigan State University, East Lansing, MI 48824, USA, ${ }^{2}$ Department of Biochemistry and Molecular Biology, Michigan State University, East Lansing, MI 48824, USA, ${ }^{3}$ Department of Computer Science and Engineering, Michigan State University, East Lansing, MI 48824, USA, ${ }^{4}$ MetagenX LLC. Okemos, MI, 48864, USA, ${ }^{5}$ Department of Biochemistry and Molecular Biology, Michigan State University, East Lansing, MI 48824, USA and ${ }^{6}$ National Institute on Alcohol Abuse and Alcoholism (NIAAA/NIH), 5625 Fishers Lane, Rockville, MD 20851, USA Email: Zheng Li - lizheng1@gmail.com; Shireesh Srivastava - srivas14@egr.msu.edu; Sheenu Mittal - mittalsh@msu.edu; Xuerui Yang - yangxuer@egr.msu.edu; Lufang Sheng - shenglufang@gmail.com; Christina Chan* - krischan@egr.msu.edu * Corresponding author


Published: 14 June 2007
Received: 23 January 2007
BMC Bioinformatics 2007, 8:202 doi:10.1186/1471-2105-8-202
Accepted: 14 June 2007
This article is available from: http://www.biomedcentral.com/1471-2105/8/202
(c) 2007 Li et al; licensee BioMed Central Ltd.

This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/2.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.


#### Abstract

Background: The ability to obtain profiles of gene expressions, proteins and metabolites with the advent of high throughput technologies has advanced the study of pathway and network reconstruction. Genome-wide network reconstruction requires either interaction measurements or large amount of perturbation data, often not available for mammalian cell systems. To overcome these shortcomings, we developed a Three Stage Integrative Pathway Search (TIPS®) approach to reconstruct context-specific active pathways involved in conferring a specific phenotype, from limited amount of perturbation data. The approach was tested on human liver cells to identify pathways that confer cytotoxicity.


Results: This paper presents a systems approach that integrates gene expression and cytotoxicity profiles to identify a network of pathways involved in free fatty acid (FFA) and tumor necrosis factor- $\alpha$ (TNF- $\alpha$ ) induced cytotoxicity in human hepatoblastoma cells (HepG2/C3A). Cytotoxicity relevant genes were first identified and then used to reconstruct a network using Bayesian network (BN) analysis. BN inference was used subsequently to predict the effects of perturbing a gene on the other genes in the network and on the cytotoxicity. These predictions were subsequently confirmed through the published literature and further experiments.
Conclusion: The TIPS® approach is able to reconstruct active pathways that confer a particular phenotype by integrating gene expression and phenotypic profiles. A web-based version of TIPS® that performs the analysis described herein can be accessed at http://www.egr.msu.edu/tips.

## Background

The regulation of cellular functions is achieved through the contribution and interactions of genetic, signaling and metabolic pathways. Consequently, cellular processes
may be singularly regulated, i.e., at the gene or transcription level, or controlled by a network of interactions of genes, proteins and metabolites. Therefore, understanding the biological function of the myriad of genes and

how these genes and gene products interact and regulate each other to yield a functional cell would help to identify more appropriate pathways that should be targeted or studied for a given disease.

Novel analytical frameworks are required to unravel the regulatory and functional relationships from profiles of genes, proteins and metabolites. Approaches have been developed to infer genome wide networks from high throughput data. These approaches typically require genome-wide interaction data [1,2] or a wide range of perturbation data [3-5], which have been applied to yeast and human B cells, respectively, to reverse engineer genome wide gene regulatory networks. Unfortunately, genomewide interaction measurements as well as large amounts of perturbation data are not easily or readily obtainable for researchers working with mammalian systems. Thus, a challenge remains to reconstruct networks from a small amount of perturbation data. The small perturbation data size poses a challenge to statistical inference and makes it extremely hard to infer genome wide networks with any degree of confidence [6-8]. To address this, we developed an approach to identify a smaller network of active pathways rather than genome wide networks based upon a subset of important genes selected by integrating gene expression and phenotypic profiles. The approach first integrates genetic algorithm coupled partial least squares analysis (GA/PLS) [9] and constrained independent component analysis (CICA) [10] to identify a subset of genes relevant to a phenotype. Next, BN analysis is used to reconstruct an active sub-network from this smaller group of genes to reveal which pathways are induced by the external stimuli or environmental factors. Applying BN to a reduced subset of genes also circumvents the inefficiency of the BN analysis in inferring large size networks, such as is the case with genome wide networks. BN can detect indirect influences and unmeasured events and is not susceptible to the existence of unobserved variables [6]. It has been applied to infer gene regulatory network of yeast cell cycle from gene expression data, metabolic sub-networks from metabolic data and protein signaling network from protein activity data [6,11-13]. The reconstructed network was then used to predict the effect of perturbing a gene on the other genes in the network with BN inference, and thus provided insight into how the genes interacted within the network to produce a specific phenotype.

As proof-of-concept, the framework was applied to identify the pathways that confer cytotoxicity in HepG2/C3A cells. Liver toxicity is often used to assess the safety of drugs and is a primary reason for drug recalls [14]. Therefore, predicting liver toxicity earlier in the drug development process would be valuable. In the current study, saturated FFA, palmitate, was found to induce liver toxicity, and this effect was exacerbated by the presence of TNF-
$\alpha$. Indeed, elevated levels of FFAs and TNF- $\alpha$ have been shown to be involved in the pathogenesis of liver disorders, such as fatty liver disease and steatohepatitis [15-18]. Therefore, we applied our approach to this model system from the standpoint that if we can identify pathways that may attenuate the toxicity in the presence of FFAs and TNF- $\alpha$, perhaps this model could be applied eventually to drug candidates to identify pathways that may be modulated to enhance the efficacy and minimize the toxicity of the drug. We analyzed the genetic responses of the hepatocytes to physiologically elevated levels of FFAs and TNF$\alpha$ to identify pathways involved in conferring cytotoxicity, and which in turn may provide insight into the physiological actions of these factors.

We developed a TIPS ${ }^{\circledR}$ framework that first applied GA/ PLS [9] and independent component analysis (ICA) $[19,20]$ to identify a subset of genes relevant to cytotoxicity. We assumed, as a first approximation, a log linear relationship between gene expression and cytotoxicity. The genes selected by GA/PLS were initially corroborated with published results to identify known interactions. In order to extract an independent pathway related to a phenotype, such as cytotoxicity, from the gene expression profile, we propose a constrained ICA (CICA) approach. The relevance of the genes to the toxicity identified by GA/PLS along with the cytotoxicity profiles were used as constraints in CICA. CICA extracted a phenotype-relevantcomponent from the gene expression data. CICA assumes that the expression profile of thousands of genes can be represented by a reduced number of mutually independent processes. Biologically meaningful gene groups have been successfully identified by ICA [19,20]. A phenotyperelevant-component was identified by minimizing the mutual information between the phenotype-relevantcomponent and the other independent components while maximizing the correlation between the component and the constraints. The expression profiles of the genes with the highest weights in CICA were used in BN analysis for network reconstruction. The reconstructed network was perturbed to identify i) which genes, when perturbed, had an impact on altering the cytotoxic phenotype in the palmitate cultures, and ii) how perturbing one gene (node) affected the other genes in the network. The reconstructed network provided potential explanation(s) on how palmitate and TNF- $\alpha$ induced cytotoxicity. The model identified (i) the roles played by stearoyl-CoA desaturase (SCD), double-stranded-RNA-dependent protein kinase (PKR) and Bcl-2 in the palmitate-induced cytotoxicity, and (ii) the activation of nuclear factor kappa B (NF-кB) by TNF- $\alpha$ is mediated by protein kinase C delta (PKC- $\delta$ ). These simulated perturbations of the reconstructed network were evaluated experimentally to assess the accuracy of the predictions.

## Results

## I. Identifying genes relevant to cytotoxicity using GA/PLS

Lactate dehydrogenase (LDH) release was measured as an indicator of the cytotoxicity. We found that exposing HepG2/C3A cells to FFAs (palmitate, oleate, or linoleate) in the presence and absence of TNF- $\alpha$, only palmitate was cytotoxic to the cells and resulted in significantly higher LDH release (Figure 1). TNF- $\alpha$ alone was not toxic to the cells. The cytotoxic effect of TNF- $\alpha$ was observed only in the palmitate-treated cells. Exposure to oleate or linoleate was not cytotoxic, but caused the cells to accumulate intracellular triglycerides (Figure 2). To obtain a global view of the changes induced by FFAs and TNF- $\alpha$, we capitalized upon high-throughput cDNA microarrays to quantify the gene expression profiles of the HepG2/C3A cells.

We applied GA/PLS to the gene expression and LDH release profiles. The GA/PLS algorithm counted the frequency with which each gene was selected to predict LDH release and provided a measure of the relevance of each gene to LDH release [9]. The genes with high frequency were organized into functional groups based on the literature information on the functional role of these genes, as shown in Table 1. Evaluating the groups of genes assigned high frequency by GA/PLS suggested that the functional groups such as oxidative stress, apoptosis, TNF-signaling, mitochondria were relevant to the cytotoxicity. Several of
![img-0.jpeg](img-0.jpeg)

Figure I
Cytotoxicity (LDH release). Confluent HepG2 cells exposed to different types of fatty acids ( 0.7 mM , complexed to $4 \% \mathrm{w} / \mathrm{v}$ BSA) and TNF- $\alpha$ for 24 and 48 hours. X-axis labels indicate the TNF- $\alpha$ concentration in $\mathrm{ng} / \mathrm{ml}$ and the medium employed in each condition. Data expressed as averages of nine samples $+/-$ s.d. from three independent experiments. a, Significant medium effect, $\mathrm{P}<0.05$ relative to control (BSA medium with no TNF- $\alpha$ ); b, Significant TNF- $\alpha$ effect within a treatment, $\mathrm{P}<0.05$ compared to corresponding medium with no TNF- $\alpha$ exposure. TNF- $\alpha$ concentrations are in $\mathrm{ng} /$ ml .
![img-1.jpeg](img-1.jpeg)

Figure 2
Intracellular TG accumulation. Intracellular TG accumulation increased in FFA treated cells. * significantly higher than control, $\mathrm{p}<0.01$ by t-test. H: control, P: palmitate treatment, O: oleate treatment, L: linoleate treatment.
these potential mechanisms suggested by the GA/PLS results were experimentally validated. For example, the identification of oxidative stress related genes suggested a possible involvement of reactive oxygen species (ROS) in the palmitate-induced cytotoxicity. Indeed, we found the ROS level was elevated in the palmitate cultured cells and adding ROS scavengers prevented the cytotoxicity induced by palmitate [21]. In addition, the caspase-3 activities were significantly elevated in the palmitate cultures as shown in Figure 3, which corroborated the involvement of apoptosis in the observed cytotoxicity. Finally, identification of translocase of outer/inner mitochondria membrane (TOM/TIM) which are known to be related to mitochondrial potential [22] were corroborated by the reduced mitochondrial potential in the palmitate cultured cells [21].

## 2. Identifying genes involved in an independent pathway related to cytotoxicity using CICA

GA/PLS determined the frequency with which each gene was selected to predict LDH release. The frequencies and the profile of LDH release were applied as structure and profile constraints respectively in CICA to extract a pheno-type-relevant-component from the gene expression profile, see methods for more details. The independent component in this case identified a subset of genes whose profiles corresponded to the profile of LDH release. CICA determined the weights for each gene by minimizing the mutual information between the independent components and maximizing the correlation to the constraints. The weights determined by CICA are in the additional files [see Additional file 1]. Genes that had weights significantly different from zero with a $95 \%$ confidence using the Z-test were subjected to BN analysis for pathway reconstruction.

Table 1: Functional groups of genes related to LDH release, selected by GA/PLS


Table 1: Functional groups of genes related to LDH release, selected by GA/PLS (Continued)


![img-2.jpeg](img-2.jpeg)

Figure 3
Caspase activity. Palmitate treatment increased caspase-3 activity significantly as compared to control (BSA) and unsaturated fatty acid (oleate). * significantly higher in palmitate, $\mathrm{p}<0.01$ by t-test. BSA: control, Ole: oleate treatment, Palm: palmitate treatment.

## 3. Reconstruct pathways related to cytotoxicity using BN

BN reconstructed how the genes, identified by CICA, are connected in a network and involved in regulating cytotoxicity. The resulting network is shown in Figure 4. To evaluate potential pathways involved in palmitateinduced cytotoxicity, we performed in silico perturbation analyses with BN inference and experimentally validated the reconstructed network.

## 3.I Perturbation of the reconstructed network

The reconstructed network allowed us to perturb the network in silico to identify which nodes had an impact on modulating LDH release. BN inference was used to predict the effect of perturbing a single gene/node on i) the other gene within the network, and ii) the level of LDH release in the palmitate cultures. The predictions of the simulated perturbations were subsequently confirmed with inhibitor (or activator) experiments. We altered the activity of the nodes by inhibiting (activating) the protein activity. Perturbations of the SCD (see section 3.2) and PKR (section 3.3) were simulated with BN inference to evaluate their effects on cytotoxicity, whereas PKC- $\delta$ (section 3.4) was perturbed to predict its effect on NF- $\kappa$ B activation.

### 3.2 Role of stearoyl-CoA desaturase (SCD) in palmitate-induced cytotoxicity

SCD was found closely connected to LDH and acetyl-CoA carboxylase (ACC) in the reconstructed network. Both of these connections are supported by the literature [23]. SCD is the rate-limiting enzyme to produce monounsaturated fatty acids. Its deficiency has been found to increase fatty acid oxidation by activating AMP-activated protein
kinase (AMPK) in the liver. AMPK phosphorylates ACC at Ser-79 which leads to the inhibition of ACC activity and decreased malonyl-CoA concentration [23]. Malonyl-CoA inhibits carnitine palmitoyl-CoA transferase (CPT-1) [24]. Thus, a decrease in the levels of malonyl-CoA activates CPT-1 and increases fatty acid beta-oxidation in the mitochondrion. In the palmitate cultures, the protein expression level of SCD (Figure 5A) was reduced as compared to the control and the oleate cultures. However, co-supplementing the palmitate cultures with oleate restored the SCD protein expression level (Figure 5B) and correspondingly reduced the LDH release (Figure 5C), which indicated a protective role of SCD. This may explain, in part, the preference of the HepG2/C3A cells to oxidize palmitate as opposed to synthesizing triglycerides from it, as was done with the unsaturated fatty acids. In support of this, knockout of the SCD gene in mice has been found to increase mitochondrial fatty acid oxidation [25].

To investigate the role of SCD in modulating palmitateinduced cytotoxicity, we simulated an upregulation of SCD in the reconstructed network by setting the SCD gene expression to a higher level in silico. Up-regulating SCD reduced the probability that the LDH release would remain high from $\sim 67 \%$ to $\sim 35 \%$ (Table 2). The simulation results agreed well with the literature, e.g., overexpressing SCD protected CHO cells from palmitateinduced cytotoxicity [26].

To experimentally validate the simulation results, we supplemented the cell cultures with $50 \mu \mathrm{M}$ of clofibrate or ciprofibrate to increase the SCD activity. The SCD1 activity can be transcriptionally activated by clofibrate or ciprofibrate, which are known to increase the activity of SCD through a PPAR independent pathway [27-29]. The fibrate supplementation significantly decreased the LDH release in the palmitate cultures (Figure 6). Therefore, BN inference correctly identified SCD as a relevant factor in palmitate-induced cytotoxicity.

### 3.3 Role of Bcl-2 and PKR in palmitate-induced cytotoxicity

Bcl-2 is a group of proteins including pro-apoptotic members, such as Bax, Bid, Bad, and anti-apoptotic ones such as Bcl-2, Bcl-xl, Bcl-w. Anti-apoptotic Bcl-2 protein inhibits apoptosis by guarding the mitochondrial gate against the release of cytochrome c and the subsequent activation of caspases. Bcl-2 was found to be connected to factors such as PKR, TOM20, eIF2B and CPT-1 (Figure 4). The protein expression level of Bcl-2 in cultured HepG2 cells as a function of TNF- $\alpha$ concentrations was measured by western blotting (Figure 7A). TNF- $\alpha(20-100 \mathrm{ng} / \mathrm{ml})$ suppressed the protein expression level of Bcl-2 in a dosedependent manner. Palmitate, similarly, decreased the Bcl-2 protein expression level significantly as compared to the control and oleate cultures. The suppression of Bcl-2

![img-3.jpeg](img-3.jpeg)

Figure 4
Network reconstructed with constraints based algorithm. GA/PLS and ICA selected the relevant genes, and BN analysis reconstructed the network using the selected subset of genes. The network provides an overview of the factors and pathways involved in regulating cytotoxicity. The nodes discussed in the paper are highlighted in red. Microsoft Visio was used to generate the Figure.

![img-4.jpeg](img-4.jpeg)

**Figure 5**

**Effect of palmitate on stearoyl-CoA desaturase (SCD) measured by western blotting.** (A) SCD was downregulated in the palmitate (0.7 mM) cultures as compared to the oleate (0.7 mM) and control cultures. (B) Co-supplementation of oleate (0.3 mM) with palmitate (0.4 mM) prevented the downregulation of SCD. (C) Co-supplementing palmitate (0.4 mM) with oleate (0.3 mM) decreased LDH release significantly, P < 0.01 (t-test). P: treated with 0.7 mM palmitate for 48 hours, PO: treated with 0.4 mM palmitate plus 0.3 mM oleate for 48 hours. Data expressed as average +/- SD from three independent experiments, * significantly lower than palmitate, p < 0.01 by t-test.

may explain, in part, the cytotoxic effects of palmitate and TNF-α in the palmitate cultured cells (Figure 1). In support of this finding, over-expression of Bcl-2 in 2B4.11 T cell hybridoma cell lines have been shown to inhibit palmitate-induced cytotoxicity [30]. While TNF-α and oleate also reduced the Bcl-2 levels, they did not produce any overt toxicity by themselves. This indicates that perhaps, the reduction in Bcl-2 alone is not sufficient to cause toxicity. However, a reduction in Bcl-2 levels would prime the cells to other insults such as oxidative stress. Only palmitate, and not oleate or TNF-α, caused ROS production as well as a reduction in the Bcl-2 levels. Thus, reduced Bcl-2 levels would have only worsened the toxicity produced by the oxidative stress. Therefore, reducing

**Table 2: Simulating genetic perturbation and its effects on LDH release**


The probability of LDH release taking on a high or low level in the palmitate cultures. BN inference was used to conduct the simulations of up-regulation of SCD, down-regulation of PKR, and up-regulation of NF-KB. "↓" indicates decreased probability and "↑" indicates increased probability.

Bcl-2 may be one of the ways in which FFA and TNF-α made cells susceptible to toxicity.

In the reconstructed network, Bcl-2 was connected to the translocase of outer membrane (TOM20) and carnitine palmitoyl transferase (CPT-1). These connections are supported by published literature results. Targeting the Bcl-2 protein to the mitochondria is mediated by the interaction between the C terminus of Bcl-2 and TOM20 [31]. Similarly, a direct interaction between Bcl-2 and CPT-1 has been confirmed through a co-immunoprecipitation study [32], thus a direct connection between Bcl-2 and CPT-1 found by the model is encouraging.

The model found PKR to be indirectly connected to Bcl-2. PKR, an interferon-inducible serine/threonine kinase, has been found to mediate a number of signal transduction pathways involved in immune response, tumorigenesis and regulation of apoptosis. PKR is best known for its role in virus infection and regulating cellular apoptosis [33,34]. In our model, simulating a down-regulation in the PKR node predicted a decrease in the LDH release (Table 2) and an increase in the Bcl-2 level in the palmitate cultures (Table 3). Indeed we found that inhibiting PKR (6 μM PKR inhibitor) in the palmitate cultures upregulated the Bcl-2 protein expression (Figure 7B) and decreased the LDH release from ~50% to ~40%. Therefore, the model appropriately identified PKR to be an important factor involved in regulating Bcl-2 protein expression, and in turn the cytotoxicity.

PKR was also found to be connected to apoptosis inhibitor (API5), which is connected to PP2AB56 and apoptotic chromatin condensation inducer (ACINUS), and the latter is connected to eIF2B suggesting that these factors are likely to be involved in the apoptotic signaling pathway. These connections are supported by published results in the literature. Caspase-3 activity was enhanced in the

![img-5.jpeg](img-5.jpeg)

**Figure 6** **Effect of SCD activators clofibrate and ciprofibrate on LDH release in the palmitate cultures**. Clofibrate and ciprofibrate are known to transcriptionally increase the activity of SCD. Palm: treated with 0.7 mM palmitate for 48 hours, Palm+clofibrate: treated with 50 μM clofibrate and 0.7 mM palmitate, Palm+ciprofibrate: treated with 50 μM ciprofibrate and 0.7 mM palmitate. 6 hours pretreatment followed by 48 hours co-supplementation of 50 μM of clofibrate or ciprofibrate significantly decrease LDH release in the palmitate culture, P < 0.01 (t-test). Data expressed as average +/- SD from three independent experiments, * significantly lower than in control, p < 0.01 by t-test. H: control, P: palmitate treatment, O: oleate treatment, P+O: palmitate and oleate co-supplementation.

Palmitate cultured cells (Figure 3), which may result in enhanced phosphorylation of eIF2-α. PKR can be cleaved by caspase-3, 7, 8 to liberate the eIF2-α kinase domain, which phosphorylates eIF2-α [35]. Phosphorylation of eIF2-α by PKR will inhibit protein synthesis and lead to apoptosis [35]. PKR also can bind to PP2A at the B56 alpha regulatory subunit (PP2AB56) and increase the phosphatase activity of PP2A [36]. PP2A is a major Ser/Thr phosphatase involved in many signal transduction pathways. PP2A can dephosphorylate and inactivate the anti-apoptotic Bcl-2 at Ser-70 [37].

### 3.4 Activation of NF-κB by TNF-α is mediated by PKC-δ

We found that the phospho-p65 NF-κB levels to be significantly lower in the palmitate cultures than in the oleate and linoleate (not shown) and control cultures shown in Figure 8. BN inference predicted that an up-regulation of NF-κB in the palmitate cultures would decrease the probability of LDH release being high (see Table 2). NF-κB is an important cytoprotective transcription factor, which can be activated by oxidative stress and cytokines, including TNF-α [38]. From Figure 4 we find that the connection between TNF-α and NF-κB is linked through PKC-δ, suggesting that PKC-δ is an intermediate factor in the activation of NF-κB. Connections between TNF-α, PKC-δ and NF-κB have been identified in cells such as neutrophils [39] and pancreatic acinar cells [40]. Inhibiting PKC-δ has been shown to attenuate TNF-α-mediated activation of the anti-apoptotic transcription factor NF-κB in adherent neutrophils [39], but showed no effect on NF-κB activation in cultured myometrial cells [41], thus suggesting the pathway is cell dependent. There has been no study to date indicating that PKC-δ mediates TNF-α's activation of NF-κB in HepG2 cells. Our model suggests that down-regulating PKC-δ will decrease the probability of NF-κB taking on a high expression level in the medium (plus TNF-α).

**Table 3: Simulating down-regulation of PKR and its effects on Bcl-2**


The probability of Bcl-2 taking on a high or low level in the palmitate cultures. BN inference was used to conduct the simulations of down-regulation of PKR. "+" indicates decreased probability and "↑" indicates increased probability. This was validated experimentally as shown in Figure 7.

![img-6.jpeg](img-6.jpeg)

Figure 8 Phosphorylated p65 subunit of NF-kB was determined by western blot with a monoclonal antibody. 1) HepG2, 2) TNF- $\alpha$ at $20 \mathrm{ng} / \mathrm{m}$; 3) TNF $\alpha$ at $100 \mathrm{ng} / \mathrm{ml}$; 4) BSA 5) BSA+TNF- $\alpha$ at $20 \mathrm{ng} / \mathrm{ml}$; 6) BSA+TNF- $\alpha$ at $100 \mathrm{ng} /$ ml ; 7) palmitate; 8) palmitate + TNF- $\alpha$ at $20 \mathrm{ng} / \mathrm{ml}$; 9) palmitate + TNF- $\alpha$ at $100 \mathrm{ng} / \mathrm{ml}$.
$\alpha$ ) cultures (Table 4). To determine whether PKC- $\delta$ is involved in mediating the activation of NF- $\kappa \mathrm{B}$ by TNF- $\alpha$ in HepG2 cells, we added rottlerin, an inhibitor of PKC- $\delta$, and measured the activity levels of NF- $\kappa$ B by western blotting. Rottlerin is a PKC- $\delta$ specific inhibitor that inhibits the tyrosine phosphorylation of PKC- $\delta$, which to our knowledge does not interfere with any of the components in the NF- $\kappa$ B activation pathway. The activity of NF- $\kappa$ B was measured by detecting the levels of phosphorylated NF- $\kappa$ B p65 at Ser-536 [42]. As shown in Figure 9, the activation of NF- $\kappa$ B p65 was attenuated by rottlerin. Therefore, PKC- $\delta$ was appropriately identified by the model to be an important factor in mediating the TNF- $\alpha$ signaling to NF- $\kappa$ B.

## Discussion

With the availability of high dimensional biological data to characterize a cellular state, one of the challenges is the development of robust methods that can integrate various orthogonal datasets to identify the genes and pathways that induce a phenotype. The significance of the TIPS ${ }^{\circ}$ framework is its ability to extract relevant information, both known and unknown, from high dimensional data. The phenotypic profile was used to guide the information extraction process. Proteins relay information from the genes to execute biological functions, which define the

Table 4: Simulating down-regulation of PKC- $\delta$ and its effects on NF- $\kappa \beta$.


The probability of NF- $\kappa \beta$ taking on a high or low level. The model predicts that a down-regulation in PKC- $\delta$ will decrease the probability of NF- $\kappa \beta$ taking on a high value. This was validated experimentally and shown in Figure 9. " $\downarrow$ " indicates decreased probability and " $\uparrow$ " indicates increased probability.
![img-7.jpeg](img-7.jpeg)

Figure 9
Effect of rottlerin on NF- $\kappa$ B measured by western blotting. Expression of phospho-P65 NF- $\kappa$ B in control and palmitate mediums with $0,20,100 \mathrm{ng} / \mathrm{ml}$ TNF- $\alpha$, gith and without rottlerin $(5 \mu \mathrm{M})$. TNF- $\alpha$ activated phospho-P65 NF$\kappa B$ and this activation was attenuated with the PKC- $\delta$ inhibitor, rottlerin.
cellular phenotype. Thus, the effects of regulation occurring at the protein level manifest themselves in the phenotype. This paper illustrates that uncovering this information at the protein (i.e., intermediate) level may be achieved by integrating phenotype and gene expression data.

A handful of the connections were selected to illustrate the effectiveness of the framework. The selection was not intended to be comprehensive or exclusive of other potentially valid connections. The connections selected for further analysis and discussion were based upon i) evidence in the literature that a potential relationship may exist, although it may not be known what the exact nature of the relationship is or its relevance to toxicity, and ii) whether materials, e.g. assays or antibodies, are available to allow us to evaluate the connections.

Currently, only one phenotypic profile, e.g., LDH release, was used to identify the active network perturbed by TNF$\alpha$ and FFA exposure. Metabolic profiles, which characterize the cellular phenotype, may also be used as constraints. Incorporating more metabolic profiles would improve the characterization of the phenotype and in turn the network reconstruction and predictions. An approach to add more constraints would be to apply ICA or PLS to extract several latent variables from the metabolic profiles [43]. In addition, the current TIPS ${ }^{\circ}$ approach selects genes based upon the data without considering a priori knowledge of the system under investigation. Using a purely data driven approach may result in important genes with modest changes escaping detection by statistical analysis such as ANOVA. Incorporating domain knowledge into the TIPS ${ }^{\circ}$ approach could improve the selection of rele-

vant genes. The prior knowledge could be incorporated with approaches such as gene set enrichment analysis (GSEA) [44]. GSEA incorporates functional pathway information in the selection of significantly enriched functional gene groups.

Additionally, the current TIPS ${ }^{\circledR}$ approach reconstructs pathways from gene expression and metabolic profiles at a single time point. Dynamic regulatory interactions may be inferred if data from multiple time points are available. Indeed, the underlying biological regulatory mechanism is likely to be dynamic in response to changes in the environmental conditions. A power law model has been applied in continuous dynamic Bayesian network (DBN) analysis to model the connection between genes [45,46]. The power law model can easily be extended to allow for delayed transcription [45,46]. Both discrete [47] and continuous [45,46] DBN has been applied to model gene regulatory networks. Therefore, to detect the dynamic property of biological networks, we plan to obtain time series data and incorporate a dynamic Bayesian network reconstruction component into the TIPS ${ }^{\circledR}$ framework.

Due to computational limitation as well as limited data, it is not possible to reconstruct a network with high confidence using all the genes across the genome. GA/PLS and ICA provided an approach to identify a relevant subset of genes for further analysis. However, useful information may be missed in the selection process or not identified due to low abundance transcripts. To address the former, an approach would be to use a more targeted array with a smaller subset of genes. To address the latter, methods such as kinetically monitored reverse transcriptase-initiated PCR (kRT-PCR) could be used to measure genes with low abundance transcripts [48].

## Conclusion

In conclusion, we have demonstrated that TIPS ${ }^{\circledR}$ may be applied to reconstruct the active associations from gene expression and phenotypic profiles to help elucidate the pathways involved in regulating palmitate-induced cytotoxicity. The pathways identified and shown in Figure 4 are specific to the cytotoxicity induced by FFA and TNF- $\alpha$. If other compounds were applied to a cell culture system (HepG2 or another cell type), new microarray and phenotype data would have to be collected and the TIPS ${ }^{\circledR}$ analysis applied to identify a different set of relevant genes specific to those compounds. This is important because many connections are context-specific (i.e. cell type and treatment). For instance, the regulation of Bcl-2 by TNF $\alpha$ is cell dependent. TNF- $\alpha$ suppresses Bcl-2 in FaO rat hepatoma cells [49] while it induces Bcl-2 in rat hippocampal neuron cells [50]. Similarly, signaling pathways are stimuli specific, for example, TNF $\alpha$ activates IKK activity with a negative feedback through A20 while LPS activates

IKK activity with a positive feedback through a different pathway involving NF- $\kappa \mathrm{B}$ and IRF3 [51]. Therefore, whether a pathway is activated will depend on the type of cell and the condition under consideration. The advantage of TIPS ${ }^{\circledR}$ is that it allows for these differences and aims to reconstruct these pathways from the context-specific data.

## Methods

## Cell culture

One million Hep G2/C3A cells (ATCC, Manassa, VA) were seeded into each well of 6 -well culture plate. The cells were kept in 2 ml of medium containing Dulbecco's modified Eagles medium (Invitrogen, Carlsbad, CA) supplemented with $10 \%$ fetal bovine serum (ATCC) and 2\% Penicillin-streptomycin (Invitrogen). Cells were incubated at $37^{\circ} \mathrm{C}$ and in $10 \% \mathrm{CO} 2$ atmosphere. After cells reached confluence, the medium was replaced with 2 ml of treatment of FFA, either palmitate $(700 \mu \mathrm{M})$, oleate $(700 \mu \mathrm{M})$, or linoleate $(700 \mu \mathrm{M})$, and in the presence and absence of TNF- $\alpha(0,20,100 \mathrm{ng} / \mathrm{ml})$. Fatty-acid-free bovine serum albumin (BSA) was used as a carrier for the FFAs.

## Cytotoxicity measurement

For the LDH measurements, cells were cultured in different media for up to 48 hours and the supernatant collected. Cells were washed with phosphate buffered saline (PBS) and kept in $1 \%$ triton-X-100 in PBS for 24 h at $37^{\circ} \mathrm{C}$. Cell lysate was then collected, vortexed for 15 sec onds and centrifuged at 7000 rpm for 5 minutes. Cytotoxicity detection kit (Roche Applied Science, Indianapolis, IN) was used to measure the LDH release. LDH released was normalized to the total LDH (released + lyzed).

## Gene expression profiling

Cells were cultured in 10 cm tissue culture plates until confluence and then exposed to different treatments. RNA was isolated with Trizol reagent. The gene expression profiles were obtained with cDNA microarray. Analyses were done at the Van Andel Institute, Grand Rapids, MI. The protocols are available online at [52]. There were two biological replicates for each condition and each replicate was labeled with the Cy3 and Cy5 dyes. The microarray data has been deposited at the GEO website [53], with a query number of GSE5441.

## Inhibitors and activators

$1 \mu \mathrm{M}$ Rottlerin (inhibits PKC- $\delta$, BIOMOL Research Laboratories, Plymouth Meeting, PA), $10 \mu \mathrm{M}$ HA14-1 (inhibits Bcl-2, BIOMOL Research Laboratories, Plymouth Meeting, PA), $6 \mu \mathrm{M}$ PKR inhibitor (Calbiochem, EMD Bioscience, CA) were used in the inhibitor experiments. 50 $\mu \mathrm{M}$ of clofibrate and ciprofibrate (Sigma) were used as activators of SCD.

## Immunoblotting

Cells were lysed with $1 \times$ SDS sample buffer. Proteins in cell lysates were separated on SDS-polyacrylamide gel electrophoresis (SDS-PAGE) and blotted onto nitrocellulose membrane. Non-specific binding sites were blocked with $5 \%$ non-fat milk. The membrane were then treated with anti-SCD (1:1000, Santa-Cruz Biotechnology Inc., CA), anti-PKC- $\delta$ (1:1000, Santa-Cruz Biotechnology Inc., CA), anti-Bcl-2 (1:2000, Cell signaling Inc., MA), and anti-NF-кB-P65 (1:1000, Cell signaling Inc., MA) to detect protein level of SCD, PKC- $\delta$, Bcl-2, and NF-кB, respectively. Membranes were also immnoblotted with anti- $\beta$ actin (1:1000, Cell signaling Inc., MA) to monitor the loading level in each lane. All antibodies are against the human isoform.

## Data analysis

## ANOVA

The analysis of variance (ANOVA) was applied to compare the effect of treatment (e.g. FFA, TNF- $\alpha$ ) and to determine whether a treatment has a significant effect. We applied a two-way ANOVA test to identify the genes that are affected by FFA, TNF- $\alpha$ or the interaction between FFA and TNF- $\alpha$. The analysis was performed in MATLAB 6.3 using Stats Toolbox. A two step ANOVA analysis was performed to identify the genes that changed significantly due to FFA or TNF- $\alpha$ exposure. We identified a list of genes from the literature shown in the additional files [see Additional file 2], that are relevant to palmitate-induced cytotoxicity and applied ANOVA with $\mathrm{P} \leq 0.05$ to this list of genes (which we denote as "supervised" ANOVA). In addition, ANOVA analysis was applied to the entire list of genes with $\mathrm{P} \leq 0.01$ (which we denote as "unsupervised" ANOVA). The two lists of genes were then combined into one list, eliminating any overlaps between the lists. Using the supervised and unsupervised ANOVA tests, the expression level of 830 genes were found to be significant due to either TNF- $\alpha$ or FFA. This list of genes is in the additional files [see Additional file 3].

## TIPS ${ }^{\circledR}$ framework

We apply a mathematical framework that first integrates genetic algorithm (GA) and partial least squares (PLS) analyses to identify the genes relevant to LDH release, but these genes may be involved in many independent pathways. Therefore, the framework then applies CICA to identify an independent pathway involved in LDH release. Finally the connections between these genes selected by CICA are reconstructed using BN analysis to infer how the genes interact with each other in the independent pathways. The reconstructed network illustrates how the genes interact under the given environmental conditions to regulate LDH release. The framework is shown schematically in Figure 10.

Genetic algorithm/partial least square analysis (GA/PLS)
Based upon the notion that metabolic functions are regulated in part by the enzymes catalyzing the reactions, which in turn are determined in part by their gene expression levels, we hypothesize that the metabolic function can be predicted from the expression level of a subset of genes that are associated with the metabolic function. The log-linear model (also known as the power law function) was used to approximate the non-linear relation between metabolic function and gene expression levels. Log-liner model has its roots in biochemistry and has been applied by Savageau et. al. (also coined as S-system) to approximate the relation between reaction rates and their substrates [54-56]. The log-linear model has also been applied successfully to model the expression of a gene as a power law function of the expression of the genes that regulate it [45]. The advantage of log-linear models is that they are computationally tractable and robust [56] and restricted nonlinear relationships have been modeled as well. Although, mechanism based nonlinear models [57] can capture more accurate behavior, they require more parameters and more data to estimate these parameters and in turn higher computational cost. Therefore, we used the log-linear model to approximate the non-linear relations between phenotype and gene expression level shown in equation (1).

$$
\frac{\operatorname{Met}(\text { treatment })}{\operatorname{Met}(\text { control })}=\prod_{i=1}^{n}\left(\frac{\text { Gene }(\text { treatment })_{i}}{\text { Gene }(\text { control })_{i}}\right) C(i)
$$

where Met(treatment) and Met(control) are the metabolic function for the treated and control cultures, respectively; Gene(treatment) ${ }_{i}$ and Gene(control) ${ }_{i}$ are the expression level of gene $i$ for the treated and control cultures, respectively.

Denoting $Y$ as $\log _{2}\left(\frac{\operatorname{Met}(\text { treatment })}{\operatorname{Met}(\text { control })}\right)$ and $X_{i}$ as $\log _{2}\left(\frac{\text { Gene }(\text { treatment })_{i}}{\text { Gene }(\text { control })_{i}}\right)$, equation (1) is transformed to a log-linear model:

$$
Y=\sum_{i=1}^{n} C(i) X_{i}
$$

In this study the coefficients $C(i)$ in equation (2) are determined by PLS analysis and the genes, Gene $_{i}$, are selected by GA/PLS as described in reference [9].

## Constrained Independent Component Analysis (CICA)

ICA is a statistical method that has been applied to reveal "hidden factors" underlying sets of signal measurements [10]. The expression levels of the genes are the recorded signals which are affected by underlying regulatory pathways. We denote the signal measurements $\mathbf{Y}$ to be the gene

![img-8.jpeg](img-8.jpeg)

Figure 10
The framework to integrate gene expression and metabolic profiles. The relevancy of each gene to LDH release was first evaluated with GA/PLS. Genes with higher frequencies were considered to be more relevant. The frequencies and profile of the LDH release were then used to constrain the ICA model to extract an independent component that represents the cellular process. The genes in the independent component with high coefficients were subjected to BN analysis.
expression data, $\mathbf{S}$ to be the independent components (pathways), and $\mathbf{A}$ to be the mixing matrix. The ICA model can be expressed as

$$
\mathbf{Y}=\mathbf{A} \mathbf{S}
$$

The gene expression $\mathbf{Y}$ is supplied to the ICA model and the mixing matrix $\mathbf{A}$ can be uniquely estimated by assuming that the components in $\mathbf{S}$ are statistically independent to each other. $Y(i, t)$ represents the expression of gene $i$ in experiment $t, A(i, j)$ represents weight of gene $i$ in independent pathway $j, S(j, t)$ represents the profile of independent pathway $j$ in experiment $t$. Since the objective here is to identify a LDH release related independent pathway, $\mathbf{A}$ was further constrained with the frequency learned by GA/PLS and $\mathbf{S}$ was further constrained with the LDH release profile. Let $F(i)$ be the frequency of gene $i$ with respect to LDH release and $a(i)$ be the weight of gene $i$ in the pathway related to LDH release. Thus, $a$ is constrained to have a correlation with $F$ by equation (4), where $\rho 1$ is a threshold value.

$$
\operatorname{Corr} 1=\mathrm{a}^{\mathrm{T}} * \operatorname{diag}(\mathrm{~F})^{*} \mathrm{a} /\left(\mathrm{a}^{\mathrm{T}} * \mathrm{a}\right)>\rho 1
$$

Let $s(t)$ be the profile of LDH related pathway in experiment $t$ and $L(t)$ be the profile of LDH release in experiment $t$. Similarly, $s$ is constrained to have a correlation with $L$ by equation (5), where $\rho 2$ is a threshold value.

$$
\operatorname{Corr} 2=\mathrm{s}^{\mathrm{T}} * \mathrm{~L}^{*} \mathrm{~L}^{\mathrm{T}} * \mathrm{~s} /\left(\mathrm{s}^{*} \mathrm{~s}^{\mathrm{T}}\right)>\rho 2
$$

Implicit in the use of ICA is i) ICA separates only linear effects, ii) all the genes are assumed to be linearly independent, and iii) can handle only one Gaussian source, which is typically assumed to be the noise in the data, and the independent signal sources are non-Gaussian. The assumption that information flow from genes to proteins is linear is a reasonable first-order approximation since most genes translate to proteins which are not involved in regulation or feedback loops. We addressed the second assumption through pre-whitening the gene expression data with singular value decomposition to remove the principal components with small eigenvalues, i.e. linear dependency. For the third assumption, we evaluated the normality of the independent component and found the extracted independent component is non-Gausssian [see Additional file 4], therefore justifying the application of ICA to the gene data.

## Bayesian network analysis

Bayesian networks are directed acyclic graphs (DAG) whose nodes correspond to variables and whose arcs represent the dependencies between variables. The dependencies are determined by the conditional probabilities of each node $x_{i}$, given its parent node $p_{a^{\prime}} \operatorname{Pr}\left(x_{i} \mid p_{a}\left(x_{i}\right)\right)$. A Bayesian network i) assumes conditional independence, such that each node is independent to its non-descendants, given it parents. For example, $B$ and $C$ are conditionally independent to each other given $A$ in a network, then

$$
\operatorname{Pr}(B \mid C, A)=\operatorname{Pr}(B \mid A)
$$

and ii) consists of joint distribution defined by a set of variables $\left\{x_{i}\right\}$ as:

$$
\operatorname{Pr}\left(x_{1}, \ldots, x_{n}\right)=\prod_{i=1}^{N} \operatorname{Pr}\left(x_{i} \mid p_{a}\left(x_{i}\right)\right)
$$

In the example above:

$$
\operatorname{Pr}(A, B, C)=\operatorname{Pr}(A) \operatorname{Pr}(B \mid A) \operatorname{Pr}(C \mid A)
$$

There are two common approaches that have been applied to learn the network structure, the score and search based and the constraint based methods. This study compared the score and search based LibB [6] method with the constraint based greedy thickening and thinning algorithm [58]. The score and search based LibB method, downloaded from Nir Friedman's group at [59], used the sparse candidate algorithm to search for a network with the highest score [6]. The score $\mathrm{S}(\mathrm{G}: \mathrm{D})$ is defined to be proportional to $\mathrm{P}(\mathrm{G} \mid \mathrm{D})$ and is used to evaluate the networks, where G represents the graph and D represents the training dataset and $\mathrm{P}(\mathrm{G} \mid \mathrm{D})$ represent prob-

ability of Graph G given data D. S(G:D) can be decomposed according to equation (9).

$$
S(G: D)=\sum_{i} S_{\text {local }}\left(X_{i}, P a_{i}^{G}: D\right)
$$

$S_{\text {local }}\left(X_{i}, U: D\right)=\log P\left(P a_{i}=U\right)+\log \left\{\prod_{m} P\left[X_{i}[m] \mid U[m], \theta\right) d P(\theta)\right.$
The first term in equation (10), $\log P\left(P a_{i}=U\right)$, is the prior probability for the choice of $U$ as the parent of $X$, the second term in equation (10) calculates the probability of the data given the possible values for the parameter, $\theta ; \theta$ defines the conditional probabilities between the nodes. The score $\mathrm{S}(\mathrm{G}: \mathrm{D})$ is maximized using the sparse candidate algorithm in the structure learning process. Mutual information based algorithm was used for the constraint based network reconstruction, the details of the algorithm can be found in $[4,58]$ and consists of 3 phases. Briefly, in Phase 1 the mutual information contained in each pair of genes is calculated as a measure of closeness, indicating the correlation between the pair of genes. The algorithm creates a draft of the regulatory network based upon the calculated mutual information. The mutual information $I\left(X_{i}, X_{j}\right)$ for each pair of nodes $\left(x_{i}, x_{j}\right)$ is computed as follows:

$$
I\left(X_{i}, X_{j}\right)=\sum_{x_{i}, x_{j}} \operatorname{Pr}\left(x_{i}, x_{j}\right) \log \frac{\operatorname{Pr}\left(x_{i}, x_{j}\right)}{\operatorname{Pr}\left(x_{i}\right) P\left(x_{j}\right)}
$$

Then each pair of genes with mutual information $I\left(X_{i}, X_{j}\right)$ greater than a threshold value, $\mathbf{T}$, are sorted in a list $L$ from high to low. T is set to be the default value in BN PowerConstructor. An arc is drawn for the first two pairs of nodes in L. The pointer is then moved to the next pair of nodes. If no path exists between the pair an arc is added. In Phase 2 arcs are added when pairs of unconnected nodes are dependent as determined by the conditional independence (CI) test. The CI test is based on conditional mutual information as defined by equation (12) below. For $I(X i, X j \mid c)$ less than the specified threshold value $\mathbf{T},(X i, X j)$ is said to be independent given $\mathbf{c}$, where $\mathbf{c}$ is a set of genes.

$$
I\left(X_{i}, X_{j} \mid c\right)=\sum_{x_{i}, x_{j}, c} \operatorname{Pr}\left(x_{i}, x_{j}, c\right) \log \frac{\operatorname{Pr}\left(x_{i}, x_{j} \mid c\right)}{\operatorname{Pr}\left(x_{i} \mid c\right) P\left(x_{j} \mid c\right)}
$$

In Phase 3 each arc is examined using the CI test and arcs are removed if two genes linked by an arc are conditionally independent. The LDH node was assigned as a leaf node in the learning process, which enabled the determination of direction in the network. BN PowerConstructor downloaded from Cheng Jie's group at [60] was used in the constraint based network reconstruction. Both the
score and search based and the constraint based approaches have their advantages and disadvantages in different respects. For example, Heckerman et al. [61] showed that the scoring-based method is advantageous over the constraint-based methods when modeling a probability distribution of observations. However, Friedman et al. [62] showed theoretically that the general scor-ing-based method may result in poor prediction accuracy, which was also confirmed by Greiner et al. [63]. Score and search method often are computationally more costly [61]. Constraint based method, on the other hand, is able to discriminate between models with and without hidden variables and can indicate the presence of a hidden common cause between two variables [64]. Therefore, we applied both approaches and compared the network learned using our data. We found that fewer connections were identified using the LibB approach and the LDH node was not connected to any genes (the full network is shown in the additional files [see Additional file 5]). Based upon this comparison, we decided to use the constraint based approach to generate the network for subsequent analyses.

## Bayesian network inference

Bayesian network inference was used to predict the probabilities of a phenotype e.g. LDH or a gene will take a certain value with the other genes in the network at controlled levels. The posterior probability that the class node will take on a certain value given the values of the other nodes is determined based upon conditional probability. Suppose node A is the target node and b 1 and c 1 are the known values of evidence nodes B and C , respectively, we can predict the posterior probability $\operatorname{Pr}(\mathrm{A} \mid \mathrm{xi}, \mathrm{xj})$ according to the Bayesian rule:
$\operatorname{Pr}\left(\mathrm{A}=\mathrm{a}_{1} \mid \mathrm{B}=\mathrm{b}_{1}, \quad \mathrm{C}=\mathrm{c}_{1}\right)=\operatorname{Pr}\left(\mathrm{B}=\mathrm{b}_{1}, \mathrm{C}=\mathrm{c}_{1} \mid \mathrm{A}=\mathrm{a}_{1}\right)^{+} \operatorname{Pr}\left(\mathrm{A}=\mathrm{a}_{1}\right) /$ $\operatorname{Pr}\left(\mathrm{B}=\mathrm{b}_{1}, \mathrm{C}=\mathrm{c}_{1}\right)(9)$

However, applying this exact inference to a large network is computationally costly [65]. Therefore, we applied an approximate inference algorithm, logic sampling [66], to infer the posterior probabilities. Briefly, logic sampling generates a case by randomly assigning values to each node weighted by the probability of that value occurring. To estimate the posterior probability $\operatorname{Pr}(\mathrm{X} \mid \mathrm{E})$ where X is target node and E is the evidence node, we compute the ratio of the number of cases where both E and X are true to the number of cases where just E is true, i.e. $\operatorname{Pr}(\mathrm{X}=\mathrm{x} \mid \mathrm{E}=\mathrm{e})=\operatorname{Pr}(\mathrm{X}=\mathrm{x}, \mathrm{E}=\mathrm{e}) / \operatorname{Pr}(\mathrm{E}=\mathrm{e})$. The inference process was conducted with Genie [67].

## Availability and requirements

Project name: Three Stage Integrative Pathway Search (TIPS ${ }^{\circ}$ )

Project home page: www.egr.msu.edu/tips
Operating system(s): Platform independent
Programming language: Matlab
License: GNU GPL for academics, license needed for nonacademic users

## Abbreviations

ACC acetyl-CoA carboxylase
AMPK AMP-activated protein kinase
TIPS three-stage-integrative-pathway-search
FFA free fatty acid
GA/PLS genetic algorithm coupled partial least square analysis

ICA independent component analysis
LDH lactate dehydrogenase
NF-кB nuclear factor kappa B
PKC- $\delta$ protein kinase C delta
PKR double-stranded-RNA-dependent protein kinase
SCD stearoyl-CoA desaturase
TNF- $\alpha$ tumor necrosis factor alpha

## Authors' contributions

ZL conceived the methodology and performed part of the experiments and wrote the manuscript. SS performed the cell culture, LDH measurement, microarray measurement, caspase measurement, wrote part of the manuscript. SM performed cell culture and microarray measurement. XY performed PKR and Bcl-2 experiment and wrote part of the manuscript. LS performed western blot experiment. CC conceived the study and supervised the experiment and writing of the manuscript. All authors read and approved the final manuscript.

## Additional material

## Additional file 1

ICA gene weights. Additional file 1 is a list of the gene weights determined by ICA.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-8-202-S1.xls]

## Additional file 2

Important gene list. Additional file 2 is a list of important genes determined manually with a literature review.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-8-202-S2.xls]

## Additional file 3

Genes selected by ANOVA. Additional file 3 lists 830 genes selected by ANOVA analysis.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-8-202-S3.xls]

## Additional file 4

Normality test. Additional file 4 presents the normality test of the gene data.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-8-202-S4.doc]

## Additional file 5

Network learned by LibB. Additional file 5 presents the network learned by search and score method of LibB.
Click here for file
[http://www.biomedcentral.com/content/supplementary/1471-2105-8-202-S5.jpeg]

## Acknowledgements

The work was supported by the National Science Foundation (BES 0331297 and BES 0425821, SBIR 0610784), the National Institute of Health (IR01GM079688-01), the MSU Foundation and the Center for Systems Biology, the Environmental Protection Agency (RD83I8470I) and the Whitaker Foundation.

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