# Quantum gene regulatory networks 

Cristhian Roman-Vicharra (D) ${ }^{1,2}$ and James J. Cai (D) ${ }^{1,255}$


#### Abstract

In this work, we present a quantum circuit model for inferring gene regulatory networks (GRNs) from single-cell transcriptomic data. The model employs qubit entanglement to simulate interactions between genes, resulting in competitive performance and promising potential for further exploration. We applied our quantum GRN modeling approach to single-cell transcriptomic data from human lymphoblastoid cells, focusing on a small set of genes involved in innate immunity regulation. Our quantum circuit model successfully predicted the presence and absence of regulatory interactions between genes, while also estimating the strength of these interactions. We argue that the application of quantum computing in biology has the potential to provide a better understanding of single-cell GRNs by more effectively approaching the relationship between fully interconnected genes compared to conventional statistical methods such as correlation and regression. Our results encourage further investigation into the creation of quantum algorithms that utilize single-cell data, paving the way for future research into the intersection of quantum computing and biology.


npj Quantum Information (2023)9:67; https://doi.org/10.1038/s41534-023-00740-6

## INTRODUCTION

A gene regulatory network (GRN) defines the ensemble of regulatory relationships between genes in a biological system. Inferring GRNs is a powerful approach for studying transcriptional regulation and the molecular basis of the regulatory mechanism, to understand the function of genes in processes of cellular activities ${ }^{1,2}$. A GRN is often represented as a graph-which can be signed, directed, and weighted-to depict relationships between transcription factors or regulators and their targets whose expression level is regulated. However, because the regulatory activity inside a cell is difficult to observe, measurements of static, intracellular gene expression are often used as a proxy, and the statistical dependencies are used to infer real regulatory relationships between genes.

Single-cell technologies, which have recently been developed and improved, open up opportunities for studying biology at remarkable resolution and scale. Single-cell RNA sequencing (scRNA-seq), for example, allows us to measure the expression of thousands of genes in each of thousands of cells ${ }^{3}$. Computational methods for constructing GRNs can adopt scRNA-seq data and leverage the information from the sheer number of cells to improve the inference power ${ }^{4-6}$. Thus, the utilization of single-cell data can lead to the development of more detailed and precise network models, which will help us gain a better understanding of the molecular mechanisms involved in cellular activities.

Numerous computational methods have been developed for constructing GRNs. These methods use statistical approaches to detect dependencies between expression profiles of genes and establish potential regulatory relationships between genes. The typical strategies that have been employed broadly fall into several categories such as correlation, regression, information theory, Gaussian graphical model, and Bayesian and Boolean networks ${ }^{4-12}$. For a broader perspective on the topic, readers are referred to several review articles ${ }^{13-16}$. It is important to note that each method has its own set of assumptions and limitations that are not always explicitly stated ${ }^{17-19}$. More importantly, none of these conventional methods fully exploits simultaneous, interregulatory connections between all genes. There is still a need for a general and principled approach to model GRNs.

Quantum computing has become an emerging technology and an intense field of research constantly seeking applications ${ }^{20}$. Researchers have developed quantum algorithms with applications in areas such as finance, cryptography, machine learning, drug discovery, chemistry, and material science ${ }^{21-25}$. A theoretical speedup is expected in certain types of computation using quantum algorithms versus classical algorithms because a quantum computer takes advantage of superposition and entanglement phenomena during the computation ${ }^{26,27}$. Given the potential of quantum computing, conventional strategies for inferring GRNs might be expanded by taking advantage of the quantum computing framework.

In this work, we introduce a quantum single-cell GRN (qscGRN) modeling method, which is based on a parameterized quantum circuit and uses the quantum computing framework to infer biological GRNs from scRNA-seq data. In our qscGRN model, each gene is represented using a qubit, and the circuit structure is divided into two types of layers: the encoder layer that translates the scRNA-seq data into a superposition state, and the regulation layers that entangle qubits to model gene-gene interactions in the quantum framework. Our qscGRN model maps binarized gene expression values onto a large vector space, known as Hilbert space, making full use of the information in the individual cells. Thus, the signal from thousands of cells is leveraged to improve the mapping of regulatory relationships between genes. The parameterization of our qscGRN model allows gene-to-gene regulatory relationships to be inferred all at once by fitting the superposition state probabilities onto the distribution observed in the scRNA-seq data. We include a quantum-classical framework for optimizing the parameters of our qscGRN model for a given scRNA-seq data set. The classical component of our framework uses the Laplace smoothing ${ }^{28}$ and the gradient descent algorithm ${ }^{29}$ to perform optimization by minimizing a loss function based on KullbackLeibler (KL) divergence ${ }^{30}$. We apply the quantum-classical framework to real scRNA-seq data sets ${ }^{31,32}$ to show that gene regulatory relationships can be modeled using quantum computing, and the network recovered from the parameter-optimized quantum circuit is largely consistent with a previously published GRN ${ }^{33,34}$.

[^0]
[^0]:    ${ }^{1}$ Department of Veterinary Integrative Biosciences, Texas A\&M University, College Station, TX 77843, USA. ${ }^{2}$ Department of Electrical and Computer Engineering, Texas A\&M University, College Station, TX 77843, USA. ${ }^{33}$ email: jcai@tamu.edu

![img-0.jpeg](img-0.jpeg)

**Fig. 1 The qscGRN model consisting of *n* qubits that models a biological GRN for *n* genes.** The quantum circuit is composed of an encoder layer *L*enc and regulation layers *L*0, *L*1, ..., *L*n-1.

![img-1.jpeg](img-1.jpeg)

**Fig. 2 The quantum-classical framework using the qscGRN model to infer the corresponding biological GRN.** The input matrix **X** is binarized into matrix **X**<sup>**b**</sup> and *n* genes are selected to be modelled. **a** Observed distribution *p*obs and activation ratios act<sub>k</sub> are computed using the labels and binarized values, respectively. The ratios act<sub>k</sub> are used in the initial setup of the parameter **θ**0. **b** The qscGRN is trained to fit the output distribution *p*out into *p*obs by minimizing a loss function based on KL-divergence. **c** The adjacency and network representation of the biological GRN using the optimal parameter **θ**.

# **RESULTS**

## **The qscGRN model and its optimization framework**

Our qscGRN model is a quantum circuit consisting of *n* qubits and models a biological GRN for *n* genes in the framework of quantum computation giving a qubit-gene equivalence (Fig. 1). A complete quantum-classical framework, which employs the qscGRN model to infer the corresponding biological GRN, is also introduced (Fig. 2). The methods section provides a detailed explanation of the model and its optimization framework.

## **Applying qscGRN model to scRNA-seq data of lymphoblastoid cells**

This section outlines the practical application of our qscGRN model in constructing a 6-gene GRN from real scRNA-seq data sets. The process began by feeding an input expression matrix, containing the expression values of 6 genes in over 28,000 lymphoblastoid cells, into the framework. The 6 genes, IRF4, REL, PAX5, RELA, PRDM1, and AICDA, are members of the NF-κB signaling pathway. The *p*obs distribution was used to show the frequencies of the 2<sup>6</sup> = 64 possible cell states mapped into a vector space. The *p*obs is represented in blue in Fig. 3a, in which only the states with a probability greater than 0.01 are shown. The qscGRN model schema for the data set was a 6-qubit system and consisted of an encoder layer and six regulation layers. We measured the output register of the qscGRN model to recover the output distribution *p*out from the quantum framework. Then, we optimized the parameter **θ** in the qscGRN model using 1087 iterations to minimizing the loss function *L*(**θ**). The distribution *p*out was fitted into *p*obs during the optimization—smoothed distributions for *p*out and *p*obs show the similarity of the two distributions after optimization. The *p*out after optimization is also represented in pink in Fig. 3a. The similarity is quantified using the loss function and error metrics that reached values of 4.25e − 3 and 3.21e − 4, respectively (Fig. 3b). We validated the optimized parameter **θ** running a quantum simulator that uses the Aer Simulator backend (colored in yellow in Fig. 3a).

The value of the parameter **θ** after optimization retrieved an adjacency matrix (Fig. 3c), which was used to construct the biological GRN. Then, we constructed a weighted network from

![img-2.jpeg](img-2.jpeg)

Fig. 3 Application of the qscGRN modeling with real scRNA-seq data from human lymphoblastoid cells. a The observed, output, and simulated frequency distributions (p<sup>obs</sup>, p<sup>out</sup>, and p<sup>glibb</sup>) of cell activation states, colored in blue, pink, and yellow respectively. b Loss function changes during training until optimization. c The adjacency matrix of the biological GRN. The heatmap shows the strength of gene-gene interactions. The diagonal elements are colored in black due to these parameters are not trained. d A weighted representation of the biological GRN recovered from the quantum circuit, where the thickness is proportional to the corresponding adjacency matrix. e Evolution of parameters in the qscGRN model recovered from the quantum framework during the optimization.

The quantum framework using the non-diagonal elements of θ, as shown in Fig. 3d. We compared the sign of the element of each pair of genes with the corresponding regulatory effect in the previously published network, i.e., the baseline GRN<sup>33,34</sup>. Figure 3e shows the evolution of parameters for 10 regulator-target gene pairs in the qscGRN model during the optimization. These gene pairs are among the relationships recovered from the quantum framework, or present in the baseline NF-κB network<sup>33,34</sup>. Gene pairs IRF4-PRDM1, REL-AICDA, PAX5-PRDM1, REL-PRDM1, and PAX5-AICDA are correctly recovered, IRF4-AICDA incorrectly recovered, while IRF4-REL, REL-PAX5, PAX5-RELA, and PRDM1-AICDA are predicted in our workflow. These recovered relationships are supported by previous studies, for example, PAX5 plays a role in the B-lineage-specific control of AICDA transcription as suggested by a previous study<sup>35</sup>. PRDM1 is a master regulator that represses PAX5 expression in B cells<sup>36</sup>. IRF4-PRDM1's regulatory relationship might be through a third-party modulator. Indeed, IRF4 is known to inhibit BCL6 expression, and because BCL6 can repress PRDM1<sup>LefL</sup>,<sup>37,38</sup>, it has been formally speculated that the effects of IRF4 on PRDM1 expression might have been mediated through inhibition of BCL6 expression<sup>39</sup>. Although several relationships are correctly recovered, IRF4 is known to induce AICDA expression through an indirect mechanism in the NF-κB signaling cascade<sup>40</sup>, suggesting the inference power is still limited.

The qscGRN model predicted four regulatory relationships between genes that were not present in the published baseline GRN. These included the gene pair PRDM1 and AICDA, which may indeed interact as shown that PRDM1 can silence AICDA expression a dose-dependent manner<sup>41</sup>. These results indicate that our qscGRN method has the potential to uncover regulatory relationships that were previously missed in the baseline model.

### DISCUSSION

Finding ways to apply quantum computing in biological research is an active research area<sup>42–46</sup>. Many questions in biology can benefit from quantum computing by exploring many possible parallel computational paths, but identifying such questions remains challenging. Especially, understanding how to exploit quantum computers for progress in solving important biological questions is crucial. The latest development of scRNA-seq technology has made it possible to gather transcriptome information from tens of thousands of individual cells per assay in a high-throughput manner. These complex data sets with higher detail are driving the development of new computational and statistical tools that are revolutionizing our understanding of cellular processes. However, quantum computation has not yet received enough attention in the face of this single-cell big data revolution.

Here, we present our qscGRN method for modeling interactions between genes to derive the quantum computing framework for constructing GRNs. In the GRN inference, the interaction between two genes determines the level of production of the target gene based on the expression of a control gene, whether this interaction is promotion or repression. Similarly, the parameter in a c-R<sup>g</sup> gate indicates the degree of rotation of a target qubit based on the state of a control qubit. We took inspiration from the analogy between these two phenomena to design the quantum circuit in the quantum algorithm and used probability distribution to constrain the parameter of the circuit. Below we discuss three aspects of application issues.

Conventional correlation- or regression-based methods for GRN construction can handle a large number of genes because, for these methods, the gene-gene interaction is calculated as a single summary statistic from the expression profile of genes in measured cells. In contrast, our quantum approach for GRN inference can only model a small number of genes due to the

![img-3.jpeg](img-3.jpeg)

Fig. 4 The impact of rotation angle θ of a c-R<sup>y</sup> gate on the amplitude, µ, of the |1⟩ state of the target qubit in a quatum circuit. a The circuit configuration consists of a control quit (the 1st qubit) and a target qubit (the 2nd qubit), each rotated by an R<sup>y</sup> gate with angles φ<sub>1</sub> and φ<sub>2</sub>, respectively. b–f The heatmap panels display various combinations of φ<sub>1</sub> (0, 0.25π, 0.5π, 0.75π and 1.0π) and φ<sub>2</sub> (0–1.0π) settings. The heatmap colors indicate the amplitude of |1⟩ state of the target qubit with respect to θ. In general, the amplitude of |1⟩ state of the target qubit increases or decreases monotonically with respect of θ. In regions marked by red triangles in (e and f), the pattern is reversed.

Vector space size—which is equal to the number of basis states—increases exponentially with the number of genes. In other words, cells in binarized scRNA-seq matrix may only be mapped to a moderate number of basis states such that each basis state is occupied by at least one cell. For example, a 15-qubit qscGRN model offers 2<sup>15</sup> = 32,768 basis states, while a scRNA-seq data set with 20,000 cells can take at most 61% of activation states in the best case. Thus, our qscGRN model may retrieve an observed distribution with no biological information mapped to many basis states. Insufficient mapping may happen even though the latest scRNA-seq technology has the capacity to allow the transcriptome of millions of cells to be measured. To obtain enough cells, we can merge multiple scRNA-seq data sets as long as they are from the same cell types or similar biological sources and the batch effect can be corrected<sup>47</sup>. On the other hand, we can select most biologically informative genes such as highly variable genes<sup>48</sup> to be included in the analysis, reducing the burden of a large number of genes in the model while maintaining the biological relevance.

To simulate the regulatory relationship between two genes, we use a c-R<sup>y</sup> gate to create a link between each pair of qubits in the regulation layers. The rotation angle of the c-R<sup>y</sup> gate indicates the strength of interaction between the control gene and the target gene. The rotation angles of c-R<sup>y</sup> gates are parameterized and mapped to the adjacency matrix after optimization to form the GRN. Throughout the paper, we assume that the rotation angle reflects the interaction strength—this is, the greater the angle, the stronger the interaction. However, we discovered that this is not always the case. We provide a simple example in Fig. 4 to illustrate the problem. Figure 4a shows the basic unit circuit, initialized in [00⟩ state, that consists of a control qubit (1st qubit, rotated using an R<sup>y</sup> gate with an angle φ<sub>1</sub>), a target qubit (2nd qubit, rotated using an R<sup>y</sup> gate with an angle φ<sub>2</sub>) and a c-R<sup>y</sup> gate with rotation angle θ. Figure 4b–f show the effect of rotation θ in the c-R<sup>y</sup> gate on the amplitude of |1⟩ of the 2nd qubit, µ, under different settings with various combinations of φ<sub>1</sub> and φ<sub>2</sub>. When considering µ as a function of θ, we can see in most cases, µ increases with increasing θ or vice versa which is consistent with our assumption in gene regulation simulation. However, in some cases with specific combinations of φ<sub>1</sub> and φ<sub>2</sub> (as indicated with red triangles in Fig. 4e, f, the pattern is opposite—µ increases with decreasing θ or vice versa. The opposite pattern becomes evident when φ<sub>1</sub> approaches π. We regard this phenomenon “boundary effect”, which may influence the interpretation of our modeling results. However, it should not have a great impact on our analysis. This is because: First, the boundary effect happens when the absolute value of rotation angle θ of c-R<sup>y</sup> gate approaches π/2. In our real-data study, as shown in Fig. 3e, we found the values of θ for all genes are in the range between −π/4 and π/4, in which the boundary effect is neglectable. Second, the boundary effect only happens in limited areas in the regions with specific combinations of states of control and target qubits. The phenomenon becomes pronounced when the rotation angle of R<sup>y</sup> gate for the control qubit, i.e. φ<sub>1</sub>, is greater than 0.75π, which means the gene is being activated in more than 85% of cells. In the case of the rotation angle is π, the corresponding gene is always activated in all cells. In single-cell biology, a fully activated gene is most likely to happen for so called “house-keeping” genes, which are consistently expressed in a high level. These genes are essential for cell survival but are less likely to play any important regulatory role. Our previous study<sup>46</sup> provides evidence that highly variable genes such as those expressed in 50% of cells and inactivated in the other 50% of cells are most functionally important for any given cell type. Taken together, we acknowledge the potential impact of the boundary effect in our model but argue that, as the impact is likely to be limited, the interpretability of the c-R<sup>y</sup> rotation angle as a measure of interacting strength remains largely intact.

Correlation- and regression-based are the most widely used methods for GRN inference, owing to in part their computational efficiency. These methods typically compute correlation or regression coefficients for gene pairs using the total number of cells in the data. The issue with these methods is that they deal with gene pairs across cells, not fully exploiting complex expression patterns by incorporating another degree of information. The relationship between any two genes is measured using a single value of summary statistics such as correlation or regression coefficient. Once computed, the coefficient becomes independent of the total number of cells. Increasing the number of cells would have little influence on correlation or regression coefficient. The other issue is that the coefficient is computed only between the two genes, regardless of the expression values of other genes in the same

Table 1. Mapping basis states using a $c-R_{y}$ gate.


biological system. Not considering other genes in the computation may result in a biased coefficient, which does not represent the true behavior of underlying interactions. There are methods such as partial correlation ${ }^{7}$, principal component regression ${ }^{5}$, and LASSO ${ }^{49}$ that may correct this. But, the correcting effect is limited given that all-to-all interactions cannot be easily modeled.

## METHODS

The implementation of our package QuantumGRN is achieved using NumPy, Pandas, Matplotlib, iGraph and Qiskit-an opensource library for working with quantum computer simulators. Our package uses the Aer Simulator backend for a noisy circuit simulator. More details about code implementation and dataset can be found in data and code availability sections.

## Quantum computation theory

In this section, we introduce broad-audience background of quantum computation. In classical computation, a bit is the unit of information being $|0\rangle$ or $|1\rangle$ in Dirac notation, defined as (1 0) ${ }^{\mathrm{T}}$ and (0 1) ${ }^{\mathrm{T}}$ respectively ${ }^{50-53}$. In quantum computation, a qubit is the unit of information being $|\psi\rangle=c_{0}|0\rangle+c_{1}|1\rangle$ in superposition, where $|\psi\rangle$ is the quantum state, $c_{0}$ and $c_{1}$ are complex numbers, and $\left|c_{0}\right|^{2}+\left|c_{1}\right|^{2}=1$. The measurement of $|\psi\rangle$ results in 0 with a probability to be observed of $\left|c_{0}\right|^{2}$ and 1 of $\left|c_{1}\right|^{2}$.

The Hadamard gate $H$ is a single-qubit gate frequently used in quantum algorithms and is defined as $\frac{1}{\sqrt{2}}\left(\begin{array}{rr}1 & 1 \\ 1 & -1\end{array}\right)$, creating superpositions of the basis states (i.e., $\left.H|0\rangle=\frac{1}{\sqrt{2}}\left(\begin{array}{rr}1 & 1 \\ 1 & -1\end{array}\right)\binom{1}{0}=\frac{|0\rangle+|1\rangle}{\sqrt{2}}\right)$. Furthermore, the rotation gate $R_{y}$ is also a single-qubit gate that uses a rotation parameter $\theta$ and is defined as $R_{y}(\theta)=\left(\begin{array}{cc}\cos \theta / 2 & -\sin \theta / 2 \\ \sin \theta / 2 & \cos \theta / 2\end{array}\right)$. In addition, a controlled gate is a 2-qubit gate that performs an operation on a target qubit when the control qubit is in state $|1\rangle$, where the operation is typically a single-qubit gate. For example, Table 1 shows the mapping of basis states when using a controlled- $R_{y}$ gate that has the first qubit as control and the second qubit as target. The $R_{y}$ operation is performed in basis states $|10\rangle$ and $|11\rangle$ because the control qubit is 1 , no operation is performed otherwise.

In classical computation, a circuit is a model composed of a sequence of gates (NOT, AND, OR operations) having input bits that flow though such a sequence eventually computing the output bits for a given task ${ }^{53}$. Similarly, a quantum circuit is a model consisting of a sequence of quantum gates that perform operations on input qubits ${ }^{54}$. In a quantum algorithm, the input qubits are usually initialized to $|0\rangle_{\text {in }}$ meaning a string of $n$ bits of zeros. Then, the register flows through the sequence of gates, computing an output register that is measured and decoded to interpret the result.

## The qscGRN model: a parameterized quantum circuit

Here, we introduce the quantum single-cell gene regulatory network (qscGRN) model that is a quantum circuit consisting of $n$ qubits and models a biological GRN for $n$ genes in the framework of quantum computation giving a qubit-gene equivalence (Fig. 1, Algorithm 1). The sequence of gates is grouped into 2 types of layers: The encoder layer $L_{\text {enc }}$ consists of a $R_{y}$ gate in each qubit and translates biological information (i.e., the frequency of gene actively expressed among cells) onto a superposition state. The regulation layer $L_{k}$ consists of a sequence of c- $R_{y}$ gates that have the $k$ th qubit as control and a corresponding target such that the $k$ th qubit is fully connected to other qubits. In the $L_{k}$ layer, a c- $R_{y}$ gate-that has the $k$ th qubit as control and the $p$ th qubit as the target-models the regulation interaction in the corresponding gene-gene pair. In particular, the parameter of the c- $R_{y}$ gate quantifies the strength of the gene-gene interaction.

In this work, we used the notation $\theta_{k, k}$ for the parameter of the $R_{y}$ gate on the $k$ th qubit in the $L_{\text {enc }}$ layer, and $\theta_{k, p}$ for the c- $R_{y, n}$ gate with the $k$ th qubit as control and the $p$ th qubit as target, in the layer $L_{k}$ of a $n$-qubit system. Thus, two layers were defined respectively as $L_{\text {enc }}=R_{y}\left(\theta_{n-1, n-1}\right) \otimes \cdots \otimes R_{y}\left(\theta_{1,1}\right) \otimes R_{y}\left(\theta_{0,0}\right)$,
where the $\otimes$ operator is the tensor product, and
$L_{k}=\prod_{i=0, \text { i } e k}^{n-1} c-R_{y, n}\left(\theta_{k, i}\right)=\mathrm{c}-R_{y, n}\left(\theta_{k, n-1}\right) \cdots \mathrm{c}-R_{y, n}\left(\theta_{k, 1}\right) \mathrm{c}-R_{y, n}\left(\theta_{k, 0}\right)$.
The computation of $L_{\text {enc }}$ and $L_{k}$ is noncommutative due to the needed operations are matrix multiplication and tensor product.

The qscGRN model was initialized to $|0\rangle_{n}$ and put into a superposition state using the $L_{\text {enc }}$ layer. Then, the gene-gene interactions were modeled using regulation layers $L_{0}, L_{1}, \cdots, L_{n-1}$. Thus, the qscGRN model is a quantum circuit that has $n^{n}$ quantum gate parameters given by a matrix representation $\boldsymbol{\theta}$ for the set of parameters $\theta_{k, p}$ in the quantum gates:
$\boldsymbol{\theta}=\left[\begin{array}{cccc}\theta_{0,0} & \theta_{0,1} & \ldots & \theta_{0, n-1} \\ \theta_{1,0} & \theta_{1,1} & \ldots & \theta_{1, n-1} \\ \vdots & \vdots & \ddots & \vdots \\ \theta_{n-1,0} & \theta_{n-1,1} & \ldots & \theta_{n-1, n-1}\end{array}\right]$,
where the diagonal elements belong to the $R_{y}$ gates in the $L_{\text {enc }}$ layer, and the non-diagonal elements to the c- $R_{y, n}$ gates in the regulation layers $L_{0}, L_{1}, \cdots, L_{n-1}$. We recognized the matrix $\boldsymbol{\theta}$ as the adjacency matrix of the biological GRN.

Therefore, the output register $\left|\psi_{\text {out }}\right\rangle$ of the qscGRN model encodes the gene-gene interactions in superposition as a function of the matrix $\boldsymbol{\theta}$ and was defined as
$\left|\psi_{\text {out }}\right\rangle=\left(\prod_{k=0}^{n-1} L_{k}\right) L_{\text {enc }}|0\rangle_{n}=L_{n-1} \cdots L_{1} L_{0} L_{\text {enc }}|0\rangle_{n}$.

Algorithm 1. Construction of qscGRN model
Require: Number of qubits $n$, Parameter $\boldsymbol{\theta}$
1: Create $n$-qubit quantum circuit qscGRN
2: for $k=0,1, \cdots, n-1$ do
3: $\quad$ Create and append $R_{y}\left(\theta_{k, k}\right)$ gate in qubit $k$
4: end for
5: for $k=0,1, \cdots, n-1$ do
6: for $p=0,1, \cdots, n-1$ do
7: if $k \neq p$ then
8: $\quad$ Create and append c- $R_{y, n}\left(\theta_{k, p}\right)$ gate having $k$ as control and $p$ as target
9: end if
10: end for
11: end for
12: return qscGRN

## Quantum-classical framework for optimization of the qscGRN model

In this section, we introduce the complete quantum-classical framework using the qscGRN model to infer the corresponding biological GRN (Fig. 2).

Gene selection. The input data of the workflow was a scRNA-seq expression data matrix $\mathbf{X}$ that contains expression values of $N$ genes in $m$ cells. The data matrix $\mathbf{X}$ was normalized using Pearson residuals ${ }^{55}$. Then, $n$ out of $N$ genes were selected to be analyzed in the next step.

Binarization. The normalized expression matrix $\mathbf{X}$ was binarized by applying the expression threshold of 0 , which means that expression values greater than 0 are set to 1 , and 0 otherwise ${ }^{56,57}$. The outcome of the binarization was saved to $\mathbf{X}^{\mathbf{b}}$, which is a matrix of dimension $n \times m$.

Labeling. Labels were assigned for each cell in $\mathbf{X}^{\mathbf{b}}$, such that the label is a string vector composed of the binarized expression of the $n$ genes in a cell. Thus, a label is the activation state of a gene in the corresponding cells.

Activation ratios. Activation ratios were computed for each gene as the percentage of cells expressing that gene in $\mathbf{X}^{\mathbf{b}}$. Then, the $n$ rows in $\mathbf{X}^{\mathbf{b}}$ were ordered decreasingly by the activation ratio and were labeled as $g_{0}, g_{1}, \cdots, g_{n-1}$.

Observed distribution. We computed the percentage of occurrences of each label within the $m$ cells to obtain the observed distribution $p^{\text {obs }}$. The percentage of label $\left|0_{i j}\right.$ in $p^{\text {obs }}$ was set to 0 , and the rest of the distribution was rescaled to sum to 1 . The rationale for setting the $\left|0\right\rangle_{o}$ probability to 0 is that only cells with expression values for at least one of $n$ genes are informative. Sparsity is a common characteristic of scRNA-seq data because of the dropout event that occurs during the sequencing process. Figure 2a shows the steps just described in the workflow of the quantum-classical framework.

Initialization of the parameter $\boldsymbol{\theta}$. The non-diagonal elements $\theta_{k, p}$ corresponding to $\mathrm{c}-R_{y}$ gates were initialized to 0 . The diagonal elements $\theta_{k, k}$ corresponding to $R_{y}$ gates were initialized to $2 \cdot \sin ^{-1} \sqrt{\operatorname{act}_{k}}$, where $\operatorname{act}_{k}$ is the activation ratio for the $k$ th gene. The rationale for the formula is that, independently on each qubit, the probability of observing 1 is the activation ratio of the corresponding gene after the $L_{\text {enc }}$ layer. Algorithm 2 illustrates the initial setup of the workflow.

Algorithm 2. Initial setup of the workflow
Require: Normalized scRNA-seq matrix $\mathbf{X}$
Select $n$ gene from $\mathbf{X}$
$2 \mathbf{X}^{\mathbf{b}}=$ Binarized matrix $\mathbf{X}$ for the selected $n$ genes
Label each cell in $\mathbf{X}^{\mathbf{b}}$ of dimension $n \times m$
for $k=0,1, \cdots, n-1$ then
$\operatorname{act}_{k}=\# \operatorname{cells}_{k} / m$, where $\# \operatorname{cells}_{k}$ is the number of cells expressing the $k$ gene
end for
for each label $\mathbf{x} \in\{0,1\}^{n}$ then
$p_{\mathbf{x}}^{\text {obs }}=\# \operatorname{cells}_{\mathbf{x}} / m$, where $\# \operatorname{cells}_{\mathbf{x}}$ is the number of cells having $\mathbf{x}$ as label
end for
Rescale $p^{\text {obs }}$
$\theta=$ Create an $n \times n$ matrix of all elements 0
for $k=0,1, \cdots, n-1$ then
for $p=0,1, \cdots, n-1$ then
if $k=p$ then
$\theta_{k, k}=2 \cdot \sin ^{-1} \sqrt{\operatorname{act}_{k}}$
end if
end for
end for
return initial parameter $\boldsymbol{\theta}, p^{\text {obs }}$

Measuring the output register of the qscGRN model. We measured the output register $\left|q_{\text {out }}\right\rangle$ to obtain the output distribution $p^{\text {out }}$ of observing the basis states. The probability of the state $\left|0\right\rangle_{o}$ in $p^{\text {out }}$ was set to 0 , and the rest of the distribution was rescaled to sum to 1 .

Smoothing $p^{\text {obs }}$ and $p^{\text {out }}$. Laplace smoothing was used to reshape $p^{\text {obs }}$ and $p^{\text {out }}$ to distributions $\hat{p}^{\text {obs }}$ and $\hat{p}^{\text {out }}$ respectively. These smoothed distributions were computed as $\hat{p}^{\prime}=\frac{\operatorname{tr}_{\text {out }}+a}{a+\beta_{\text {out }}}$ where $i \in\{$ out, obs $\}, a$ is the smoothing parameter being typically 1 and $\#$ ocu' is the number of occurrences in the distribution $p^{\prime}$. In other words, $p^{i}=\frac{\operatorname{tr}_{\text {out }}}{m}$ is the original distribution.

Loss function. The loss function consists of KL and constrain terms, named as $L_{\text {KL }}$ and $L_{\text {cons }}$, were defined as
$L_{\text {KL }}(\boldsymbol{\theta})=\sum_{\mathbf{x} \in\{0,1\}^{n}} \hat{p}_{\mathbf{x}}^{\text {out }} \log \left(\frac{\hat{p}_{\mathbf{x}}^{\text {out }}}{\hat{p}_{\mathbf{x}}^{\text {obs }}}\right)$,
$L_{\text {cons }}(\boldsymbol{\theta})=\sum_{\theta_{i} \in \boldsymbol{\theta}} \frac{1}{\left[\theta_{i}^{\mathrm{d}}-\left(\frac{\theta}{2}\right)^{4}\right]^{2}}$,
where $\boldsymbol{\theta}$ is the parameter in the qscGRN model and $\{0,1\}^{n}$ is the $n$ Cartesian power of the set $\{0,1\}$. Thus, the loss function was defined as
$L(\boldsymbol{\theta})=L_{\text {KL }}(\boldsymbol{\theta})+\lambda \cdot L_{\text {cons }}(\boldsymbol{\theta})$,
where $\lambda$ is a dynamic coefficient that rescales $L_{\text {cons }}$ to the same order of magnitude than $L_{\text {KL }}$. In summary, the $L_{\text {KL }}$ term fits the output distribution $p^{\text {out }}$ in the observed distribution $p^{\text {obs }}$. Meanwhile, the $L_{\text {cons }}$ constraints any parameter in $\boldsymbol{\theta}$ to not get close to $n / 2$.

Optimization of the parameter $\boldsymbol{\theta}$. The optimization was achieved by minimizing iteratively the loss function to a threshold value of $2^{n} \times 1 \mathrm{e}-4$ using a modified-gradient descent algorithm with a learning rate Ir of 0.05 . Otherwise, the optimization was performed for a pre-defined iterations $t$. Then, the parameter $\boldsymbol{\theta}$ in the iteration $s+1$ was defined as
$\boldsymbol{\theta}_{s+1}=\boldsymbol{\theta}_{s}-\operatorname{Ir} \cdot \frac{\nabla L\left(\boldsymbol{\theta}_{s}\right)+\nabla^{\mathrm{T}} L\left(\boldsymbol{\theta}_{s}\right)}{2}$,
where $\nabla^{\mathrm{T}}$ is the transpose of the gradient of loss function, allowing to keep the parameter $\boldsymbol{\theta}$ as a symmetric matrix. The diagonal parameters $\theta_{k, k}$ were not trained during optimization under the assumption that these parameters encode the binarized scRNA-seq matrix given as an input to the quantum framework. Algorithm 3 illustrates the optimization of parameter $\boldsymbol{\theta}$ and Fig. 2b shows details of the optimization in the workflow. Our work is also integrated to Qiskit-an open source library for working with quantum computers-that simulates a noisy quantum circuit using Aer Simulator backend with default parameters.

Algorithm 3. Optimization of parameter $\boldsymbol{\theta}$
Require: Initial parameter $\boldsymbol{\theta}_{0}, p^{\text {obs }}$
$\hat{p}^{\text {obs }}=\operatorname{smooth}\left(p^{\text {obs }}\right)$
for $s=0,1, \cdots, t-1$ then
qscGRN $=$ Constructed quantum circuit using $\boldsymbol{\theta}_{s}$
Measure output register and obtain $p^{\text {out }}$
$\hat{p}^{\text {out }}=\operatorname{smooth}\left(p^{\text {out }}\right)$
loss $=\mathrm{L}\left(\boldsymbol{\theta}_{s}\right)$
if loss < loss_threshold then
return $\boldsymbol{\theta}_{s}$
end if
Compute gradient $\nabla L\left(\boldsymbol{\theta}_{s}\right)$
$\boldsymbol{\theta}_{s+1}=\boldsymbol{\theta}_{s}-\operatorname{Ir} \cdot \frac{\nabla L\left(\boldsymbol{\theta}_{s}\right)+\nabla^{\mathrm{T}} L\left(\boldsymbol{\theta}_{s}\right)}{2}$
end for
return $\boldsymbol{\theta}_{t}$

Recovery of gene regulatory network. We removed non-diagonal parameters in $\boldsymbol{\theta}$ that had an absolute value less than $\frac{100}{100-2}$ because no significant rotation was performed by the corresponding $\mathrm{c}-R_{g}$ gate. Next, we used the remaining parameter in $\boldsymbol{\theta}$ to construct the adjacency matrix of the biological GRN, which is a weighted symmetric network. Figure 2c shows this last step in the workflow of the quantum-classical framework.

## Single-cell transcriptomic data

The scRNA-seq data used in this study was generated from lymphoblastoid cell lines (LCLs), which are widely used cell line systems derived from human primary B cells. The single cell sequencing libraries were prepared using the 10x Genomics platform. Information about the experimental procedure and the acquisition of sequence data is provided in reference to our original study ${ }^{31}$. The data set has been deposited to the Gene Expression Omnibus (GEO) database and can be accessed with accession number GSE126321. To increase the number of cells in this study, we merged our data set with another LCL scRNA-seq data set downloaded from the GEO database with accession number GSE158275 ref. ${ }^{32}$. The data matrices were pre-processed using scGEAToolbox ${ }^{58}$ and combined to produce the final matrix, which contains expression counts of 9,905 genes of 28,208 cells. The matrix was then normalized using the Pearson residuals method ${ }^{55}$. Normalized expression values of six genes: IRF4, REL, PAX5, RELA, PRDM1, and AICDA in the NF-кB signaling pathway, were extracted. The 6-gene expression matrix with dimensions of $6 \times 28,208$ was binarized and used as the input of our qscGRN analysis. The biological regulatory relationships between these genes, called the baseline model of GRN, were obtained from the previously established B-cell differentiation circuit model ${ }^{33,34}$.

## DATA AVAILABILITY

The scRNA-seq data analyzed in the current study is available in the NCBI GEO database under accession numbers GSE126321 and GSE158275.

## CODE AVAILABILITY

The processed data and the source code implementation of the qscGRN package are provided in the GitHub repository at https://github.com/cailab-tamu/QuantumGRN/. The repository also includes tutorials written in Python language.

Received: 22 June 2022; Accepted: 29 June 2023;
Published online: 13 July 2023

## ACKNOWLEDGEMENTS

The identification of the boundary effect in the $\mathrm{c}-R_{2}$ gate impact analysis is credited to the anonymous reviewer for whom we express our gratitude. This work was supported by the DoD grant GW200026 for J.J.C.

## AUTHOR CONTRIBUTIONS

Conceptualization, J.J.C.; methodology, C.R. and J.J.C.; implementation of the software, C.R.; formal analysis, C.R. and J.J.C.; writing and editing, C.R. and J.J.C.; supervision, J.J.C. All authors reviewed and contributed to the manuscript.

## COMPETING INTERESTS

The authors declare no competing interests.

## ADDITIONAL INFORMATION

Correspondence and requests for materials should be addressed to James J. Cai.
Reprints and permission information is available at http://www.nature.com/ reprints

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http:// creativecommons.org/licenses/by/4.0/.
(c) The Author(s) 2023