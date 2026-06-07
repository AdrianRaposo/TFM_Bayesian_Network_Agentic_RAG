# IEEE/ACM TRANSACTIONS ON 

## COMPUTATIONAL BIOLOGY AND BIOINFORMATICS

![img-0.jpeg](img-0.jpeg)

OCTOBER-DECEMBER 2007

# TABLE OF CONTENTS 

## SPECIAL SECTION on Bioinformatics Research and Applications

513 Guest Editors' Introduction to the Special Section on Bioinformatics Research and Applications
I.I. Mándoiu, Y. Pan, and A. Zelikovsky

515 Removing Noise and Ambiguities from Comparative Maps in Rearrangement Analysis
C. Zheng, Q. Zhu, and D. Sankoff

523 Comparing Genomes with Duplications: A Computational Complexity Point of View
G. Blin, C. Chauve, G. Fertin, R. Rizzi, and S. Vialette

535 Exemplar Longest Common Subsequence
P. Bonizzoni, G. Della Vedova, R. Dondi, G. Fertin, R. Rizzi, and S. Vialette

544 Fast and Practical Algorithms for Planted (I, d) Motif Search
J. Davila, S. Balla, and S. Rajasekaran

553 SynPAM—A Distance Measure Based on Synonymous Codon Substitutions
A. Schneider, G.H. Gonnet, and G.M. Cannarozzi

561 Algorithms for Efficient Near-Perfect Phylogenetic Tree Reconstruction in Theory and Practice
S. Sridhar, K. Dhamdhere, G.E. Blelloch, E. Halperin, R. Ravi, and R. Schwartz

## REGULAR PAPERS

572 Cascaded Bidirectional Recurrent Neural Networks for Protein Secondary Structure Prediction J. Chen and N.S. Chaudhari

583 Data-Dependent Kernel Machines for Microarray Data Classification
H. Xiong, Y. Zhang, and X.-W. Chen

596 Finding a Common Motif of RNA Sequences Using Genetic Programming: The GeRNAMo System
S. Michal, T. Ivry, O. Schalit-Cohen, M. Sipper, and D. Barash

611 High-Confidence Rule Mining for Microarray Analysis
T. McIntosh and S. Chawla

624 Inferring Adaptive Regulation Thresholds and Association Rules from Gene Expression Data through Combinatorial Optimization Learning
I. Ponzoni, F.J. Azuaje, J.C. Augusto, and D.H. Glass

634 Inferring Gene Regulatory Networks Using Differential Evolution with Local Search Heuristics N. Noman and H. Iba

648 An Intelligent Two-Stage Evolutionary Algorithm for Dynamic Pathway Identification from Gene Expression Profiles
S.-Y. Ho, C.-H. Hsieh, F.-C. Yu, and H.-L. Huang
(Contents continued on inside back cover)

## FINANCIAL COSPONSORS

![img-1.jpeg](img-1.jpeg)

## TECHNICAL COSPONSORS

![img-2.jpeg](img-2.jpeg)

## IEEE CONTROL SYSTEMS SOCIETY

John Baillleul
President

# Inferring Adaptive Regulation Thresholds and Association Rules from Gene Expression Data through Combinatorial Optimization Learning 

Ignacio Ponzoni, Francisco J. Azuaje, Juan Carlos Augusto, and David H. Glass


#### Abstract

There is a need to design computational methods to support the prediction of gene regulatory networks (GRNs). Such models should offer both biologically meaningful and computationally accurate predictions which, in combination with other techniques, may improve large-scale integrative studies. This paper presents a new machine-learning method for the prediction of putative regulatory associations from expression data which exhibit properties never or only partially addressed by other techniques recently published. The method was tested on a Saccharomyces cerevisiae gene expression data set. The results were statistically validated and compared with the relationships inferred by two machine-learning approaches to GRN prediction. Furthermore, the resulting predictions were assessed using domain knowledge. The proposed algorithm may be able to accurately predict relevant biological associations between genes. One of the most relevant features of this new method is the prediction of adaptive regulation thresholds for the discretization of gene expression values, which is required prior to the rule association learning process. Moreover, an important advantage consists of its low computational cost to infer association rules. The proposed system may significantly support exploratory large-scale studies of automated identification of potentially relevant gene expression associations.


Index Terms-Combinatorial optimization, genetic regulatory networks, machine learning, gene expression data, decision trees.

## 1 BACKGROUND

A gene regulatory network (GRN) aims to represent high-level relationships that govern the rates at which genes in the network are transcribed into mRNA. In this way, genes can be viewed as nodes in this network whose expression levels (outputs) are controlled by other nodes (transcription factors). Nowadays, the inference, modeling, and simulation of GRNs is a fundamental topic in functional genomics [1], [2]. Over the past few years, several statistical and artificial intelligence techniques have been proposed to carry out the reverse engineering of GRNs from monitoring and analyzing large-scale gene expression data [3], [4]. Clustering algorithms represented one of the first approaches to support the large-scale identification of regulatory modules [5], [6]. Such an approach approximated regulatory networks by 1) identifying groups of coexpressed genes and 2) analyzing relationships between their regulatory regions and DNA binding motifs targeted by known transcription factors. A key limitation of this approach is that it assumes that coexpression is always equivalent to regulation. Moreover, this method implies

- 1. Ponzoni is with the Department of Computer Science and Engineering, Universidad Nacional del Sur, Av. Alem 1253, Bahía Blanca, CP 8000, Argentina. E-mail: ip@cs.uns.edu.ar.
- F.J. Azuaje is with the Computer Science Research Institute and the School of Computing and Mathematics, University of Ulster at Jordanstown, BT37 0QB, Newtonnabbey, Co. Antrim, UK. E-mail: fj.azuaje@ieee.org.
- I.C. Augusto and D.H. Glass are with the School of Computing and Mathematics, University of Ulster at Jordanstown, BT37 0QB, Newtonnabbey, Co. Antrim, UK. E-mail: (jc.augusto, dh.glass)@ulster.ac.uk.
Manuscript received 14 Mar. 2006; revised 23 Aug. 2006; accepted 6 Nov. 2006; published online 22 Jan. 2007.
For information on obtaining reprints of this article, please send e-mail to: tcb9@computer.org, and reference IEEECS Log Number TCBB-0057-0306. Digital Object Identifier no. 10.1109/TCBB.2007.1049.
symmetric relationships between the genes, which may not always correspond to biological phenomena.

Within the area of machine learning, Boolean Networks were one of the first models to be employed in GRNs inference [7], [8] and variations of this approach have been published recently [9]. These models basically aim at inferring logical rules from a discretization of gene expression time series. Even though these models can be easily applied, they depend on arbitrary discretizations of the gene expression values [10], which impose strong assumptions and restrictions about the biological system under study.

Bayesian Networks have also provided the basis for several approaches to inferring GRNs [11], [12], [13]. These methods employ conditional probabilistic distributions for gene interactions modeling. Despite the strong theoretical rationale behind these approaches, the exponential explosion of the parameter space required for these models, together with the large quantity of data needed to make reliable inferences, reduces their capacity to infer complex GRNs by using gene expression data only. Since they are acyclic directed graphs, they cannot represent autoregulation or time-course regulation in a straightforward way [2].

From the area of evolutionary computing approaches [14], several methods were proposed. Ando et al. [15] presented an algorithm that combines genetic programming with the minimum least squares method. This technique infers a differential equation system that represents regulation interactions between genes. Although this method may be robust in statistical terms, the algorithm was only tested on small GRNs ( 10 genes) and the authors detected important scalability limitations when applied to more complex data. Iba and Mimura [16] proposed an iterative

inference approach based on a genetic algorithm (GA) whose learning process was guided by a molecular biologist. The main goal was to allow the expert to perform interactive analysis and validation of the results based on the introduction of new constraints until a GRN with a high level of predictive confidence was achieved. One of the most important drawbacks of this methodology is that it requires the biologist to have a good understanding of the dynamics of the GA in order to select optimum learning parameters. Recently, Hallinan and Wiles proposed an evolutionary algorithm [17], which predicts GRNs based on the Artificial Genome model presented by Reil [18]. Although this model is more biologically plausible than traditional machine-learning methods and presents potentially useful properties, the network dynamics rely on synchronous updating, which is biologically implausible. On the other hand, when a more realistic asynchronous updating scheme was used, the dynamic behavior collapsed at a single point attractor under almost all conditions [17].

Soinov et al. [10] approached the task of reconstructing GRNs as a classification problem. In summary, the authors proposed the application of decision trees to infer classifiers that may represent regulatory rules (relationships) between genes. They applied the C4.5 algorithm to infer the decision trees [19]. This method's computational efficiency limitations are well known for classification problems with continuous-valued attributes [20], which is the case in the GRNs inference problem since the gene expression values are real numbers. Although this is a sound and conceptually interesting approach, it may exhibit significant predictive limitations when dealing with more complex GRNs (that is, networks that may consist of hundreds or thousands of genes).

Another important category of predictive approaches includes several methods that are based on the detection of modules of genes significantly coexpressed under specific conditions [21], [22], [23]. Such modules allow both the approximation of higher level network representations and module-specific relationships. This divide-and-conquer approach is a useful option for achieving reliable predictions in the absence of larger amounts of expression samples. However, recent evidence suggests conflicting views about the meaning and nature of functional modules represented in GRNs [24]. For a more comprehensive review of GRN inference methods, the reader is referred to [2], [25], and [26].

### 1.1 Proposed Approach

The method proposed in this paper addresses key limitations shown by data-driven whole-set GRNs prediction methods. The main objective is to provide a user-friendly, biologically meaningful, and computationally efficient algorithm to support the inference of complex putative GRNs. We do not claim that data-driven machine-learning approaches are sufficient to infer biologically meaningful networks. However, such tools may provide significant evidence necessary to aid scientists in detecting and validating biologically relevant associations. Moreover, the method proposed here neither makes strong statistical assumptions nor applies arbitrary expression discretization schemes (including adaptive thresholds for inferring
regulation rules). Thus, a new machine-learning algorithm based on combinatorial optimization, from now on referred to as GRNCOP (abbreviated from Gene Regulatory Network inference by Combinatorial OPtimization), is assessed. This method infers association rules that represent interactions between genes, which are obtained from gene expression data sets. The discovered rules may be used to predict the gene expression states of a gene in terms of the gene expression values of other genes and, in this way, a putative GRN may then be reconstructed by applying and combining these rules.

Our approach offers several advantages in relation to existing methods. First of all, it does not assume arbitrary and uniform gene expression value discretizations. Second, GRNCOP is not constrained by regulatory symmetry relationships that are shown by clustering-based network inference techniques. Third, the results can be easily interpreted since the association rules are derived from models that classify the different regulation states. Finally, the algorithm computes the potential interactions between genes with a low computational effort of $\mathrm{O}\left(n^{2}\right)$, where $n$ is the number of genes in the GRN. Moreover, the new methodology may in principle be adapted to other modeling approaches, such as modular methods [21], [22], [23] and multisource-based prediction techniques [27].

GRNCOP aims at inferring different types of rules that capture relevant associations (that is, potential regulatory relationships) reflected in the expression values of the genes. In order to test this approach, GRNCOP was applied to the microarray data sets presented by Spellman et al. [28] to infer a GRN relevant to the yeast cell cycle. The results were statistically validated. Moreover, the rules generated by GRNCOP were compared to relationships inferred by two other published methods [10], [12]. Furthermore, biologically relevant predictions were verified and potentially novel predictions were assessed through literature searches and an analysis of curated functional annotations derived from the Saccharomyces cerevisiae Genome Database (SGD).

The rest of this paper is organized as follows: Key definitions to interpret the regulatory rules and the combinatorial optimization problem are introduced in Section 2, the new algorithm is explained in Section 3, and experimental results obtained by GRNCOP are discussed in Section 4. A summary of contributions, future research, and conclusions are presented in Section 5.

## 2 Systems and Methods

### 2.1 Gene Expression Association Rules and GRNS Inference

The time series encoded in a gene expression data set may be represented by means of a gene expression data matrix, $X$, where the rows and columns represent genes and samples (experimental perturbations or conditions), respectively. In this way, each element $\boldsymbol{x}_{i j}$ of $X$ contains the expression value of gene $i$ in the sample $j$.

Although the gene expression values belong to a continuous range of the real numbers, it is possible to define a finite expression state set for each gene by means of a discretization procedure. Such a procedure is required in order to encode the inputs to any combinatorial optimization

process or other machine-learning methods. The results reported in this paper, as in previous representative studies, concentrate on two states for each gene: upregulated (when the gene is expressed with a value greater than its mean gene expression value) and downregulated (when the gene is expressed with a value less than or equal to its mean expression value). Nevertheless, the model can be generalized to any number of states in a straightforward way. In GRNCOP, the state of a gene $i$ in a sample $j$ is denoted as $s_{i j}$ and $\mu_{i}$ represents the mean expression value for this gene. Thus, $s_{i j}=1$ if $\boldsymbol{x}_{i j}>\mu_{i}$; otherwise, $s_{i j}=-1$.

On the other hand, the inference process also requires the definition of discretization thresholds in order to infer putative regulatory relationships between genes. These "regulation thresholds" have traditionally been estimated as unique static values for all of the genes under study. For example, ad hoc methods based on mean expression values have been applied. However, a more biologically meaningful scheme should model the fact that a gene may actually have distinct regulation thresholds in relation to different genes in the regulatory network. For example, regarding the regulatory network under study (see Section 4), the genes CLB2 and SWI5 are shown to be inhibited by gene CLB1, but their respective downregulation thresholds are different. CLB2 is downregulated (or inhibited) when the gene expression value of CLB1 is above 0.07 , whereas SWI5 is downregulated when the gene expression of CLB1 is above -0.28 . Therefore, a fundamental problem consists of estimating the regulation thresholds for each gene in relation to each potential target gene, which can more accurately reflect significant interactions between genes.

At this point, our hypothesis is stated as follows: Association rules (that is, potential regulatory relationships) may be accurately inferred from expression data to reveal how the present and future state of a gene may be affected by the gene expression values of the other genes, taking into account their relative regulation thresholds. In this paper, we consider three types of association rules: simultaneous, time-delay, and change-based rules. The rule types are the same as those studied by Soinov et al. [10] and Bulashevska and Eils [12], but the rule syntax adopted here is slightly different. In particular, Soinov et al. [10] referred to the third group of associations as changes rules. In this paper, we refer to such relationships as change-based rules.

Simultaneous rules represent the situation in which the state of a gene $i$ in a sample $j$ depends on the gene expression values of other genes in the same sample $j$. The syntax for these rules is $<$ symbol $><$ gene $>\Leftrightarrow<$ symbol $><$ gene $>$. The symbols + and - on the left side of the rule indicate above and below some specific regulation threshold, respectively, whereas the symbols + and - on the right side of the rule indicate upregulated and downregulated states, respectively. For example, the rule $+\mathrm{CLB} 1 \Leftrightarrow+\mathrm{CLB} 2$ denotes that, when CLB1 is above its regulation threshold in relation to CLB2 $t_{\text {CLB1,CLB2 }}$ in a sample, then CLB2 will be upregulated in the same sample.

Time-delay rules represent the situation in which the state of a gene $i$ in a sample $j$ depends on the gene expression values of other genes in the previous sample (that is, previous experimental condition) $j-1$. The syntax for these rules is

TABLE 1
Summary of the Different Types of Association Rules Inferred by GRNCOP


The first column encodes the cases.
$<$ symbol $><$ gene $>\rightarrow<$ symbol $><$ gene $>$. The symbols + and - on the left side of the rule indicate above and below some specific regulation threshold, respectively, whereas the symbols + and - on the right side of the rule indicate upregulated and downregulated states, respectively. For example, the rule $+/-$ CLB1 $\rightarrow-/+$ MCM1 denotes that, if CLB1 is above its regulation threshold in relation to MCM1, $t_{\text {CLB1,MCM1 }}$, in a sample, then MCM1 will be downregulated in the next sample and, if CLB1 is below or equal to $t_{\text {CLB1,MCM1 }}$ in a sample $j$, then MCM1 will be upregulated in the next sample $j+1$.

Finally, change-based rules represent events of the transi-tion-state machine corresponding to the GRN. The syntax for these rules is $<$ symbol $><$ gene $>\Rightarrow<$ symbol $><$ gene $>$. In both sides of the rule, the symbols + and - indicate upregulated and downregulated states, respectively. For example, the rule $+\mathrm{CLB} 1 \Rightarrow+\mathrm{CLB} 2$ denotes that, when the gene CLB1 changes its state from downregulated to upregulated, then the gene CLB2 will also change its state from downregulated to upregulated at the same experimental condition $j$. The six resulting regulation cases for the three types of rules are shown in Table 1.

Note that two different types of discretization are defined in this paper. The first one is to set the state of each gene, which is computed using its mean expression value, and the second one is to evaluate the potential interaction between each pair of genes and it is calculated in an adaptive gene-pair-specific way. In this paper, we focus on the impact of adaptive regulation thresholds in the rule inference process. However, the study of adaptive thresholds for the definition of the gene's states is another potential improvement of existing GRN inference methods. This task will be part of future research.

### 2.2 Combinatorial Optimization for Putative GRNs Inference

GRNCOP infers the association rules described above by exploring the possible combinations of interactions between each pair of genes. In this sense, we assume six particular cases, which are represented by the nonnull integer numbers between -3 and 3 and a special case that indicates the absence of association, which is represented by the number 0 . All of these cases are described in Table 1.

![img-3.jpeg](img-3.jpeg)

Fig. 1. General schema of the GRNCOP algorithm. Dotted arcs indicate the connection between the main program and the subroutine used for phases 1 and 2 (gray box).

In mathematical terms, the inference of the rules to reconstruct a GRN can be expressed as the following combinatorial optimization problem:

$$
\bigcup_{i=1}^{n} \max _{\bar{x}_{i} \in \mathbf{P}} \boldsymbol{\sigma}\left(\bar{\pi}_{i}, \boldsymbol{\delta}(\boldsymbol{X}, \boldsymbol{i})\right)
$$

subject to:

- $n=$ number of genes in the microarray data set,
- $m=$ number of samples in the microarray data set,
- $X \in \Re^{\text {exon }}$, matrix with the gene expression data,
- $\mathbf{P}$ is the space of all vectors $v$ of dimension $n$ such that $v_{i} \in\{-3,-2,-1,0,1,2,3\} \forall i, i=1 . . n$,
- $\delta(X, i)$ is the discretization function such that $\delta(X, i)=D_{i}$ and $D_{i} \in\{-1,1\}^{\text {exon }}$,
- $\bar{\pi}_{i} \in \mathbf{P}$ is a classifier for $D_{i}$, and
- $\sigma\left(\bar{\pi}_{i}, D_{i}\right)$ is a performance function of $\bar{\pi}_{i}$ as classifier of $D_{i}$.
From now on, the symbol $\Pi$ indicates the set of optimal classifiers, $\Pi=\left\{\bar{\pi}_{1}, \bar{\pi}_{2}, \ldots, \bar{\pi}_{n}\right\}$. It is important to note that the general optimization problem is the same for the three types of rules. The only difference lies in the definition of the discretization function $\delta$ because each type of rule is based on different expression discretizations of $\boldsymbol{X}$.


## 3 AlGORITHMS

### 3.1 GRNCOP: Combinatorial Optimization Algorithm

The machine-learning process to obtain the rules consists of three phases, one for each type of rule (see the left side of Fig. 1). Phases 1 and 2 follow a similar processing principle (see the right side of Fig. 1). The core of the algorithm is a loop, where the vector of potential regulators $\left(\bar{\pi}_{i}\right)$ for a gene $i$ is calculated at each iteration. After $n$ iterations, the set of potential regulators corresponding to all the genes is held in set $\Pi$.

Phases 1 and 2 differ in terms of the procedure applied to calculate the discretization thresholds, which are required for the discretization of the matrix $\boldsymbol{X}$ and for obtaining the
![img-4.jpeg](img-4.jpeg)

Fig. 2. Schema of the phase 3 subroutine corresponding to the GRNCOP algorithm. The discretization step is shown outside of the loop.
discretization function $\delta(X, i)$. Both procedures will be explained in Section 3.2.

Note that, although computing the threshold is conceptually a subroutine of the discretization procedure, these two procedures are actually independent components in the algorithm due to efficiency reasons. All of the regulation thresholds corresponding to each gene are calculated simultaneously, whereas the discretization of $\boldsymbol{X}$ is calculated in relation to each gene.

With respect to phase 3 (Fig. 2), the main difference with the previous phases is the discretization procedure, which is calculated only once. This is because the same discrete matrix is common to all genes. The rationale behind this difference is further explained later. Therefore, the discretization function has matrix $X$ as its unique argument. Consequently, only the procedure to obtain the optimum $\bar{\pi}_{i}$ for a gene $i$ is calculated in each iteration. In this way, as we have mentioned before, the procedure to calculate the optimal solution $\Pi$ is the same for each type of rule.

### 3.2 Discretization Step: Function $\delta$ Calculation

During discretization, the real numbers corresponding to the gene expression values, which are held in matrix $\boldsymbol{X}$, are mapped to values -1 and 1 using the function $\delta(\boldsymbol{X}, i)$. The main question at this point is how to define the discretization regulation thresholds for each gene in relation to the others. A traditional approach consists of using the mean expression value from a gene $i$ in the sample set $X$. This solution is easy to implement, but it represents a strong simplification of reality because it assumes a unique putative regulation threshold for each gene with respect to the others. It is well known that the gene expression value required by gene $_{\mathrm{R}}$ to activate (or inhibit) a gene $_{\mathrm{T} 1}$ is not necessarily the same value required by the same gene $_{\mathrm{R}}$ to activate (inhibit) a gene ${ }_{\mathrm{T} 2}$. For this reason, we propose applying a more flexible and dynamic threshold-selection policy which calculates a specific regulation threshold for each pair of genes.

In particular, GRNCOP calculates the thresholds by applying the same continuous-valued attribute discretization techniques as those used for classification algorithms based on decision trees. Basically, it considers each expression value shown by gene ${ }_{\mathrm{R}}$ in $X$ as a potential threshold for the discretization of gene $_{\mathrm{R}}$. A partition of the sample set $\boldsymbol{X}$ into two subsets, namely, Do and $\boldsymbol{U} \boldsymbol{p}$, is generated for each gene and each candidate threshold, $\boldsymbol{t}$. Do

contains all samples where the gene ${ }_{R}$ has an expression value less than or equal to $t$, whereas $U p$ contains all of the samples where the gene ${ }_{R}$ has an expression value greater than $t$. In other words, $D o$ and $U p$ represent sample sets in which the gene ${ }_{R}$ has values equal to -1 and 1 , respectively, on the basis of $t$, which is the candidate discretization regulation threshold for the gene ${ }_{R}$.

The next step consists of the calculation of the partition entropy, which is a statistical indicator of the quality of a threshold $t$ as a discretization value for gene ${ }_{R}$ with respect to another gene ${ }_{T}$. To further illustrate this concept, suppose that we are trying to infer the potential regulators for a given gene ${ }_{\mathrm{T}}$, then, for each gene ${ }_{\mathrm{R}}$ (potential regulator of gene ${ }_{\mathrm{T}}$ ), we obtain a discretization of this gene's expression values, which can help us to infer whether or not the gene ${ }_{\mathrm{R}}$ is actually a regulator of gene ${ }_{\mathrm{T}}$. In numerical terms, the partition entropy is 0 when all samples satisfy the same association rule case (ideal situation from a predictive viewpoint) and the partition entropy is 1 when the samples belong to both regulation scenarios in equal proportion ( 50 percent and 50 percent). Then, when the partition entropy value associated with a discretization approximates to 0 , the threshold that generates this discretization represents a better solution. Thus, such a threshold value allows one to optimally detect potential significant relationships between gene ${ }_{\mathrm{T}}$ and gene ${ }_{\mathrm{R}}$ in terms of the association rule cases. The entropy calculation is based on definitions given in [29] and the partition entropy equation was previously applied by Kohani [30] as follows:
$P \operatorname{Entropy}(\mathrm{R}, t, X)=\frac{|D o|}{|X|} \operatorname{Entropy}(D o)+\frac{|U p|}{|X|} \operatorname{Entropy}(U p)$
where

- R identifies the gene under consideration (potential regulator),
- $t$ is the partition threshold,
- $X$ is the set of samples corresponding to the time series,
- Do is the subset of $X$ with the samples, where the gene expression value of the gene ${ }_{R}$ is less than or equal to $t$, and
- $U p$ is the subset of $X$ with the samples where the gene expression value of the gene ${ }_{R}$ is greater than $t$.
Then, for each pair of genes, GRNCOP calculates the threshold that minimizes the partition entropy using (2). After that, for each gene ${ }_{i}$, the function $\delta(X, i)$ maps the corresponding gene expression values in $X$ to the discrete matrix $D_{i}$ using the thresholds previously calculated. Thus, each gene $i$ in the original matrix $X$ is associated with a discrete matrix $D_{i}$.

This discretization policy for $\boldsymbol{X}$ is used for both simultaneous and time-delay rules. However, a temporal shift for the vector encoding the expression values of gene ${ }_{i}$ is required for the latter type. The time-delay rules predict the situation when the state of a gene ${ }_{i}$ in a sample $j$ depends on the gene expression values of its regulators in the previous sample $j-1$. In other words, these rules determine the correlations between the expression value of a
gene ${ }_{i}$ in a sample $j, X_{i, j}$, and the values of the others genes in the previous sample, $X_{k, j-1}$, for $k=1 \ldots n$. For this reason, if $X \in \Re^{n \times m}$, then $D_{i} \in\{-1,1\}^{n \times(m-1)}$, where the $i$ th row of $D_{i}$ corresponds to the discretization of gene ${ }_{i}$ in the last $m-1$ samples of $X$, whereas the values of the remaining rows of $D_{i}$ correspond to the discretization of other genes in the first $m-1$ samples of $X$.

Finally, the discretization procedure for the change rules is significantly different. The discretization goal in this case is to obtain a matrix $D$ that represents the transition of each gene between the upregulated and downregulated states in time. As explained in Section 2, because the state of a gene is discretizated using its mean expression value, the discretization function $\delta(X)$ does not require a threshold for each pair of genes. In this situation, we are only interested in identifying the state changes of each gene. For this reason, only one matrix, $D$, is generated which is common to all genes. This discretization coincides with the change rules modeling presented by Soinov et al. [10].

### 3.3 Optimization Step: Function $\sigma$ and $\bar{\pi}_{i}$ Calculation

As defined in (1), the optimization problem consists of finding a set of optimal $\bar{\pi}_{i}$ which define potential association rules between $i$ and the other genes (potential regulators). Basically, $\bar{\pi}_{i}$ is a vector that represents the set of potential regulators of the gene ${ }_{i}$. Each component of the vector holds an integer value between -3 and 3 , which represents one of the seven regulatory cases shown in Table 1. Thus, $\bar{\pi}_{i}(\mathrm{k})$ indicates the regulation case detected between gene ${ }_{k}$ and gene ${ }_{i}$, that is, $\bar{\pi}_{i}$ is a gene expression classifier that represents the potential regulators for the gene $_{i}$ along with the characteristics of these potential relationships.

The next step is the definition of an objective function $\sigma$ for the selection of the optimal set of association rules. Taking into account that $\bar{\pi}_{i}$ represents a classifier obtained from the set of samples $D_{i}$, the optimum $\bar{\pi}_{i}$ could be calculated by maximizing a typical classifier performance function. In particular, we use the following function proposed by Carvalho and Freitas [31]:

$$
\sigma\left(\bar{\pi}_{i}, D_{i}\right)=\left(\frac{T P}{(T P+F N)}\right) \times\left(\frac{T N}{(F P+T N)}\right)
$$

where

- $T P$ (True Positives) is the number of positive association cases (see Table 1) of $D_{i}$ correctly classified by $\bar{\pi}_{i}$,
- $F N$ (False Negatives) is the number of positive cases of $D_{i}$ incorrectly classified by $\bar{\pi}_{i}$,
- $T N$ (True Negatives) is the number of negative cases of $D_{i}$ classified correctly by $\bar{\pi}_{i}$, and
- $F P$ (False Positives) is the number of negative cases of $D_{i}$ incorrectly classified by $\bar{\pi}_{i}$.
In this formula, the first factor is usually known as the sensitivity of a classifier, whereas the second one is typically recognized as specificity of a classifier. Both factors generate values between 0 and 1 and, so, $\sigma\left(\bar{\pi}_{i}, D_{i}\right)$ is always in this range too. The best classifier is obtained when $\sigma\left(\bar{\pi}_{i}, D_{i}\right)=1$

because this represents the situation where all expression association states were correctly classified, whereas $\sigma\left(\bar{\pi}_{i}, D_{i}\right)=0$ refers to the opposite case.

GRNCOP calculates $\bar{\pi}_{i}$ using a constructive approach, which explores all possible combinations of values for its components $\bar{\pi}_{i}(k)$. In short, GRNCOP computes the sensitivity and specificity for each possible interaction case value (encoded by values ranging from -3 and 3 ) for each $\bar{\pi}_{i}(k)$ and assigns the value that maximizes the product of both rates to $\bar{\pi}_{i}(k)$. After repeating this for each $\bar{\pi}_{i}(k)$, with $k=1 \ldots n$, the resulting $\bar{\pi}_{i}$ maximizes (3).

It is important to stress the low computational effort required for GRNCOP to infer a putative GRN. For example, for a problem with $n$ genes, the algorithm only needs to calculate the metrics TP, FP, TN, and FN $n$ times to find the association rules relative to each gene. These four metrics can be calculated simultaneously for a gene. Taking into account the fact that the sensitivity and the specificity are calculated with a computational complexity of $\mathrm{O}(n)$, where $n$ is the number of genes, the total runtime required to find the exact combinatorial solution to this problem is very low, $\mathrm{O}\left(n^{2}\right)$. That is, the calculation of the sensitivity and specificity values is repeated $n$ times, one iteration per gene. This represents an improvement in relation to previous research. For example, the $\mathrm{C}_{4.5}$ algorithm applied by Soinov et al. [10] has a complexity of $\mathrm{O}\left(n^{2} \log (n)\right)$ for problems with continuous-valued attributes [32].

## 4 ReSults and Discussion

The predictive performance of GRNCOP was tested using the microarray data in [22], which also includes data from S. cerevisiae cell cultures [27]. These data were synchronized by three different methods: cdc15, cdc28, and alpha-factors. Therefore, these three gene expression data sets may be defined as statistically independent [10].

For the performance analysis of the proposed method, the same training and validation experiments used by Soinov et al. [10] and Bulashevska and Eils [12] were analyzed in order to achieve a fair comparison between the three inference methods. The results reported here focus on genes CLN1-3, CLB1-6, CDC28, MBP1, CDC53, CDC34, SKP1, SWI4-6, HCT1, CDC20, SIC1, and MCM1 in order to establish comparisons with previous studies ([10], [12]); hence, $n=21$. The largest database, cdc15, was used as a training set, that is, as the matrix $X$ of the optimization problem. For the prediction of simultaneous rules, we used all of the samples in cdc15, whereas, for the time-delay and changes rules inference, we used adjacent equidistant samples only.

All the data available was considered in the prediction of simultaneous rules, whereas only adjacent equidistant samples were considered for inference of time-delay and change-based rules. The accuracy of the rules obtained from the cdc15 training set was assessed by three different validation procedures: a 10 -fold stratified cross-validation [30] and independent tests using the cdc28 and alpha-factor data sets. Our choices of training and validation data sets, as well as validation procedures, were the same as those implemented by Soinov et al. [10] and Bulashevska and Eils [12]. However, these studies differ in the sense that

TABLE 2
Candidate Association Rules Inferred by GRNCOP, Soinov et al. (2003), and Bulashevska and Eils (2005) for S. cerevisiae Using the cdc15 Data Set from Spellman et al. (1998)


Bulashevska and Eils did not carry out a 10 -fold crossvalidation test.

The association rules inferred by GRNCOP are summarized in Table 2. Only the rules that achieved the highest levels of accuracy after the validation process are reported. All of the rules included in Table 2 reached an accuracy over 70 percent in each validation procedure and an overall mean accuracy higher than 80 percent, that is, taking into account the average of the three validation tests. As a consequence of this stringent evaluation, none of the change-based rules detected from cdc15 passed the validation test.

The last two columns of Table 2 indicate interaction relationships that were also inferred by the methods proposed by Soinov et al. [10] and Bulashevska and Eils [12], respectively, using the same data sets. The GRN corresponding to the simultaneous rules inferred by GRNCOP is shown in Fig. 3. The nodes represent genes, and the arcs indicate the potential regulatory relationships. The direction of the arcs determines the direction of the putative regulatory interactions. In particular, the dotted arcs denote new potential relationships discovered exclusively by GRNCOP.

The accuracy values obtained for the classifiers proposed in the three studies are presented in Tables 3 and 4. Each row holds the mean accuracy value obtained by the rules that represent the set of potential interactions for a particular gene. It is important to clarify that Bulashevska and Eils [12] did not report results by applying 10 -fold stratified cross-validation. They only carried out independent tests using the cdc28 and alpha-factor data sets.

In summary, all simultaneous rules inferred by the decision-tree method [10] were also detected by GRNCOP, with the exception of the rules associated with genes MBP1, CDC34, and SKP1. Nevertheless, the simultaneous rules

![img-5.jpeg](img-5.jpeg)

Fig. 3. GRN based on the simultaneous rules inferred by GRNCOP for S. cerevisiae. Dotted arcs show potentially novel association rules for CLN1, CLN2, CLB1, CLB5, and SWI4.
involving these genes are reported as "Questionable rules" by Soinov et al. [10] because these rules have a high 10 -fold cross-validation accuracy on cdc15 data, but their accuracy decreases significantly with the cdc28 and alpha-factor data sets. For example, Soinov et al. reported that the accuracy estimated by 10 -fold cross validation for the rule $+\mathrm{MBP} 1 \Leftrightarrow$ -SKP1 under "simultaneous" events is almost 92 percent, but the performance of the rule was not confirmed by estimations with cdc28 and alpha-factor test sets. In other words, the number of "FP" for this rule is high when cdc28 and alpha-factor are used as test sets. Therefore, GRNCOP inferred all the highly accurate simultaneous rules obtained by the decision-tree method [10].

Furthermore, the unquestionable simultaneous rules discovered by Soinov et al. [10] also belong to the most accurate rule subset inferred by GRNCOP. Each unquestionable simultaneous rule obtained by Soinov et al.'s algorithm was inferred by the GRNCOP with an accuracy of approximately 90 percent. It is important to note that the number of rules inferred by Soinov et al.'s algorithm is increased by GRNCOP by 40.5 percent, with the same overall accuracy (the mean accuracy of the three validation tests was exactly equal to 84.93 percent for both methods). In other words, GRNCOP detects more association rules than Soinov et al.'s method with the same accuracy levels.

Although the Bulashevska and Eils's method based on Bayesian Networks infers several interaction relationships that were not detected by GRNCOP, the emergence of many of their rules may be explained by the relaxation of the

TABLE 3
Comparison between the Validation Test Results Obtained by GRNCOP and Soinov et al. (2003) for S. cerevisiae Using the cdc15 Data Set from Spellman et al. (1998)


TABLE 4
Comparison between the Validation Test Results Obtained by GRNCOP and Bulashevska and Eils (2005) for S. cerevisiae Using the cdc15 Data Set from Spellman et al. (1998)


accuracy percentages required during the validation test, as shown in Table 4, and not as a result of a better predicting ability. From this table, it is clear that, both in [10] and in our work, a more conservative validation test was carried out to decide the final set of association rules. Moreover, if the accuracy percentage is decreased to 60 percent, GRNCOP obtained more rules, but an accuracy of at least 70 percent was used in order to achieve a fair but stringent comparison in relation to Soinov et al.'s experiments.

In addition, from Table 2, it is evident that several of the rules inferred by GRNCOP and Soinov et al. [10] were not detected by Bulashevska and Eils. Finally, it is important to stress that, despite these differences, no major inconsistencies were found between the methods.

### 4.1 Biological Relevance of Results

The biological relevance of the inferred rules was estimated by analyzing whether such interrelationships reflect key functional properties relating to the different cell cycle phases $\mathrm{G}_{1}, \mathrm{~S}, \mathrm{G}_{2}, \mathrm{M}$, and $\mathrm{M} / \mathrm{G}_{1}$. Genes CLN1 and CLN2 transcribe $\mathrm{G}_{1}$ cyclins, whereas CLB5 and CLB6 transcribe B-cyclins. They share a similar expression pattern and attain their highest expression level during the $\mathrm{G}_{1}$ phase, which can be verified in the experimental data analyzed [34], [35], [36]. This knowledge is consistent with the rules:

$$
\begin{aligned}
& +/-\mathrm{CLB} 6 \Leftrightarrow+/- \mathrm{CLB} 5,+/- \mathrm{CLN} 1 \Leftrightarrow+/- \mathrm{CLB} 5 \\
& +/-\mathrm{CLN} 2 \Leftrightarrow+/- \mathrm{CLB} 5,+/- \mathrm{CLB} 5 \Leftrightarrow+/- \mathrm{CLB} 6 \\
& +/-\mathrm{CLN} 1 \Leftrightarrow+/- \mathrm{CLB} 6,+/- \mathrm{CLN} 2 \Leftrightarrow+/- \mathrm{CLB} 6 \\
& +/-\mathrm{CLB} 5 \Leftrightarrow+/- \mathrm{CLN} 1,+/- \mathrm{CLN} 2 \Leftrightarrow+/- \mathrm{CLN} 1 \\
& +/-\mathrm{CLN} 1 \Leftrightarrow+/- \mathrm{CLN} 2
\end{aligned}
$$

In particular, the new rules inferred by GRNCOP,

$$
\begin{aligned}
& +/-\mathrm{CLN} 2 \Leftrightarrow+/- \mathrm{CLB} 5,+/- \mathrm{CLB} 5 \Leftrightarrow+/- \mathrm{CLN} 1 \\
& +/-\mathrm{CLN} 1 \Leftrightarrow+/- \mathrm{CLN} 2
\end{aligned}
$$

are consistent with observations on the partial functional redundancy existing among CLB5, CLN1, and CLN2, which have been reported by Epstein and Cross [37] and Levine et al. [38].

CLB1 and CLB2 are specific cyclins of the $\mathrm{G}_{2}$ phase and there is a biological evidence that they are coexpressed in this process [39]. Gene SWI5 is a transcription factor whose

activation occurs during the G2 phase. These facts justify the following rules:

$$
\begin{aligned}
& +/-\mathrm{CLB} 2 \Leftrightarrow+/- \mathrm{CLB} 1,+/- \mathrm{SWI} 5 \Leftrightarrow+/- \mathrm{CLB} 1 \\
& +/-\mathrm{CLB} 1 \Leftrightarrow+/- \mathrm{CLB} 2,+/- \mathrm{SWI} 5 \Leftrightarrow+/- \mathrm{CLB} 2 \\
& +/-\mathrm{CLB} 1 \Leftrightarrow+/- \mathrm{SWI} 5,+/- \mathrm{CLB} 2 \Leftrightarrow+/- \mathrm{SWI} 5
\end{aligned}
$$

which are further supported by biological evidence presented by Koranda et al. [40]. Furthermore, the transcription of SWI5 is activated late in phase $S$ and its peak of mRNA concentration occurs during the $\mathrm{G}_{2}$ phase [41]. This information is consistent with the rule: $+/-$ CLB1 $\rightarrow+/-$ SWI5.

It is also well known that, in budding yeast, the $\mathrm{G}_{1}$ cyclins such as CLN1 and CLN2 are expressed in $\mathrm{G}_{1}$ and $S$ phases, whereas mitotic cyclins such as CLB1 and CLB2 are expressed in G2 and M phases. Amon et al. [42] found that the CLBs play a central role in the transition from S to $\mathrm{G}_{2}$ phases, showing evidence that CLBs repress CLNs. This negative regulation of CLNs may occur via the transcription factor SWI4 because CLBs are necessary for $\mathrm{G}_{2}$ repression of SCB-regulated genes like CLN1 and CLN2. On the other hand, Andrews and Measday [43] present evidence that the Cyclin/CDK complexes (CDC28/CLN1 and CDC28/ CLN2) regulates CLB proteolysis. This data is consistent with the inhibitory relationships inferred between $\mathrm{G}_{1}$ and $\mathrm{G}_{2}$-specific genes:

$$
\begin{aligned}
& +/-\mathrm{CLN} 1 \Leftrightarrow-/+ \mathrm{CLB} 1,+/- \mathrm{CLN} 2 \Leftrightarrow-/+ \mathrm{CLB} 1 \\
& +/-\mathrm{CLB} 6 \Leftrightarrow-/+ \mathrm{CLB} 1,+/- \mathrm{CLN} 1 \Leftrightarrow-/+ \mathrm{CLB} 2 \\
& +/-\mathrm{CLN} 2 \Leftrightarrow-/+ \mathrm{CLB} 2,+/- \mathrm{CLB} 2 \Leftrightarrow-/+ \mathrm{CLN} 2 \\
& +/-\mathrm{SWI} 5 \Leftrightarrow-/+ \mathrm{CLN} 2
\end{aligned}
$$

and the time-delay rule: $+/-$ CLB6 $\rightarrow-/$ CLB1. In particular, the rules

$$
\begin{aligned}
& +/-\mathrm{CLN} 1 \Leftrightarrow-/+ \mathrm{CLB} 1,+/- \mathrm{CLN} 1 \Leftrightarrow-/+ \mathrm{CLB} 2 \\
& +/-\mathrm{CLN} 2 \Leftrightarrow-/+ \mathrm{CLB} 1
\end{aligned}
$$

and $+/-$ CLN2 $\Leftrightarrow-/+$ CLB2 were only inferred by GRNCOP. The reader is referred to [39], [41], and [44] for additional detailed information on the biological relevance of these associations.

With regard to SIC1, it is well known that this gene is an inhibitor of CLB complexes and that it is active during the $\mathrm{G}_{1}$ phase inhibiting CLB1 and CLB2 [45]. This validates the simultaneous rule: $+/-$ SIC1 $\Leftrightarrow-/+$ CLB2. CDC20 is transcribed late in the $\mathrm{S} / \mathrm{G}_{2}$ phase [36], whereas CLN1 is expressed during the $\mathrm{G}_{1}$ phase. This explains its interaction with CLN1, which may be represented by the rule $+/-$ CDC20 $\Leftrightarrow-/+$ CLN1. Printz et al. [46] presented evidence that CLB2 stimulates the synthesis of CDC20 and Chen et al. [47] described time delays between the expression of CLB2 and the activation of CDC20. This feature is captured by a new rule inferred by GRNCOP: $+/-$ CLB2 $\rightarrow+/-$ CDC20. This rule was not detected by the methods compared with GRNCOP.

The protein SWI4 is a component of the SBF complex, which controls the expression of genes during phase $\mathrm{G}_{1}$ [48]. This is in concordance with the inhibitory action of SWI4 on the genes expressed in the $\mathrm{G}_{2}$ phase, as represented by the
rule $+/-$ SWI4 $\Leftrightarrow-/+$ CLB1, and its activator role of the genes expressed during the $\mathrm{G}_{1}$ phase, as revealed by the rule $+/-$ SWI4 $\Leftrightarrow+/-$ CLN2. Moreover, Igualetal. [48] showed experimental evidence that the SWI4 regulates the transcription of gene CLN2, which is represented in one of the simultaneous rules inferred by GRNCOP only. These observations offer evidence of the biological relevance of the association rules inferred by GRNCOP.

Additionally, a functional annotation-driven analysis of the interacting pairs only predicted by GRNCOP (Table 2) further suggests its potential for making biologically meaningful predictions. Their curated Gene Ontology (GO) [49] annotations derived from the SGD (http:// www.yeastgenome.org/) were processed to assess functional similarity between such pairs under the three GO hierarchies: Molecular Function (MF), Biological Process (BP), and Cellular Component (CC), as investigated elsewhere [50]. Only higher quality annotations were processed, that is, electronically inferred annotations were not considered.

All of the pairs exhibited relatively high functional similarity values over all the GO hierarchies using the March 2005 release of the SGD. This stresses that these pairs are linked to common biological functions, pathways, and cellular localizations. With regard to the BP hierarchy, for example, all of the similarity values were higher than 0.4 , which is above the SGD mean similarity value. Only the pair SWI4-CLN2 showed null similarity under the MF hierarchy. All of the pairs showed CC similarity values above 0.6 , except for the pair CLB2-CDC20 (0.20). A closer look at the GO annotations for these novel predictions confirms the relevance of these findings. For example, the pair CLN1-CLB1 is involved in regulation of cyclin dependent proteins. Similarly, CLB2 is a known regulator of cyclin dependent protein kinase activity, which was predicted by GRNCOP as a regulator of CDC20. CDC20 is known to be involved in cyclin catabolism.

## 5 CONCLUSIONS

In this paper, GRNCOP, a combinatorial optimization algorithm designed for the inference of putative GRNs, was presented. GRNCOP obtains an optimal classifier that represents potential interaction relationships between genes. This classifier is attained in two sequentially executed main steps. First, a gene-specific discretization of the gene expression values is carried out, which can more accurately reflect the complexity of the regulatory relationships between pairs of genes. In a second stage, the association rules are inferred by means of a combinatorial exploration of the predictive relationships existing between the discretized values.

This study does not claim that our or other data-driven machine learning approaches are sufficient to infer biologically meaningful regulatory networks. However, such tools may offer significant evidence necessary to aid scientists in exploring and identifying biologically relevant associations. The method proposed here is also computationally efficient (that is, runtimes), it does not require arbitrary assumptions about the discretization of gene expression values, and it also proved to have a good predictive performance in the

inference of a GRN for S. cerevisiae. The results obtained by GRNCOP were compared with the relationships inferred by two recently published methods [10], [12]. This comparison reveals the efficacy of GRNCOP as a prediction tool. This is not only because it detects a high percentage of the rules inferred by the other methods, but also because it finds new relevant relationships, which satisfied a stringent statistical validation. Moreover, all interactions between genes inferred by GRNCOP are consistent with previous biological knowledge. It is also important to remark that the low computational effort required by our method makes it suitable for the inference of complex GRN, involving thousands of genes.

As future work, we plan to extend our algorithm in order to implement other types of inferable interaction relationships. The algorithm currently has the ability to infer potential regulatory rules with one-to-one cardinality, that is, rules where the precedent (left side of the rule) contains only one gene. Biological phenomena may, of course, comprise relationships described by a "many-to-one" cardinality. Moreover, a variety of motifs may also be found, such as "one-to-many" relationships. Therefore, we will incorporate the prediction of rules with higher cardinality.

A related future direction concerns the manner in which inferences of potential interactions are made. At present, our algorithm assesses each gene independently as a potential regulator for the target gene under consideration, that is, in determining whether gene ${ }_{\mathrm{R}}$ is a potential regulator of gene ${ }_{\mathrm{T}}$, we do not take into account gene $_{\mathrm{R}}$ 's relationship with other regulators of gene ${ }_{\mathrm{T}}$. This means that it is possible that some direct interactions identified by our approach are, in fact, due to indirect relationships between genes. A first step to addressing this issue would be to investigate thresholds for both direct and indirect processes identified by our approach in order to determine whether there is any redundancy in the GRN that has been inferred.

We also intend to integrate additional data sources such as factor binding motifs and location analysis data, as well as prior functional knowledge (for example, ontologybased) and network constraints such as topological constraints. With respect to possible applications, we also plan to test our method on data from other organisms such as mice. Finally, further comparisons with others methods and the hybridization with modular techniques constitute another long-term goal.

## ACKNOWLEDGMENTS

Dr. Ponzoni did this work as a visiting researcher at the School of Computing and Mathematics, University of Ulster. The authors would like to express their acknowledgment to the ANPCyT from Argentina for their economic support given through Grant No. 11-12778 (Res. 117/2003) as part of the "Contrato de Préstamo BID 1728/OC-AR" and to the Universidad Nacional del Sur for their economic support given through Grants Res. CSU-598 and PGI 24/N019.
