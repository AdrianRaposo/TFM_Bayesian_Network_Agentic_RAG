# Mathematical Modelling Plant Signalling Networks 

D. Muraro ${ }^{1,2 *}$, H.M. Byrne ${ }^{1,3,4}$, J.R. King ${ }^{1,4}$, M.J. Bennett ${ }^{1}$<br>${ }^{1}$ Centre for Plant Integrative Biology, School of Biosciences, University of Nottingham<br>Sutton Bonington Campus, Loughborough LE12 5RD, UK<br>${ }^{2}$ Weatherall Institute of Molecular Medicine, University of Oxford, Oxford, OX3 9DS, UK<br>${ }^{3}$ Oxford Centre for Collaborative Applied Mathematics, Mathematical Institute, Oxford, OX1 3LB, UK<br>${ }^{4}$ School of Mathematical Sciences, University of Nottingham, University Park<br>Nottingham NG7 2RD, UK


#### Abstract

During the last two decades, molecular genetic studies and the completion of the sequencing of the Arabidopsis thaliana genome have increased knowledge of hormonal regulation in plants. These signal transduction pathways act in concert through gene regulatory and signalling networks whose main components have begun to be elucidated. Our understanding of the resulting cellular processes is hindered by the complex, and sometimes counter-intuitive, dynamics of the networks, which may be interconnected through feedback controls and crossregulation. Mathematical modelling provides a valuable tool to investigate such dynamics and to perform in silico experiments that may not be easily carried out in a laboratory. In this article, we firstly review general methods for modelling gene and signalling networks and their application in plants. We then describe specific models of hormonal perception and cross-talk in plants. This mathematical analysis of sub-cellular molecular mechanisms paves the way for more comprehensive modelling studies of hormonal transport and signalling in a multi-scale setting.


Keywords and phrases: Arabidopsis thaliana, signalling networks, mathematical modelling
Mathematics Subject Classification: 35Q53, 34B20, 35G31

## 1. Introduction

The development of animals and plants is coordinated by the activity of multiple extracellular signalling molecules. In animals this role is played mostly by small proteins or peptides, whereas in plants hormones exert a more prominent role [96], [18], [35], [76]. The main plant hormones are auxin, cytokinin, gibberellin and ethylene.

Auxin plays an influential role in plant development by promoting cell proliferation and defining the boundaries of meristematic tissues. Auxin is heterogeneously distributed throughout the plant tissues and forms concentration gradients as a result of a combination of diffusive and active, directed transport [13], [43]. This flux also determines the direction of growth [58].

[^0]
[^0]:    *Corresponding author. E-mail: daniele.muraro@ndm.ox.ac.uk

Cytokinin acts antagonistically to auxin by negatively modulating auxin transport [88] and meristem size [22]. Auxin and cytokinin are mutually antagonistic at the cell and plant level. For example, organ differentiation in tobacco pith tissue cultures is known to depend on the ratio between cytokinin and auxin [92]: a high cytokinin-to-auxin ratio promotes shoot formation, whereas a low ratio stimulates rooting. Some of the molecular mechanisms through which these hormones interact have been uncovered $[76]$.

Gibberellin influences several developmental processes such as stem and leaf growth, seed germination and flowering time [94]. In roots, it sustains auxin activity at early stages of development by enhancing the size of the meristem [77]. In shoots, mutants of Arabidopsis thaliana which have reduced levels of endogenous bioactive gibberellins (GAs) regenerate shoot buds more readily than the wild-type controls [30].

Ethylene inhibits cell elongation in roots [95] and plays a significant role in leaf expansion [63]. Auxin, cytokinin and ethylene affect each other's biosynthesis: auxin and cytokinin synergistically activate ethylene biosynthesis [109], [93], while ethylene upregulates auxin biosynthesis [95].

Cellular responses to hormones appear to be the result of multiple signalling pathways which communicate through a network of reactions involving genes, mRNA molecules and proteins. Such cellular mechanisms may be difficult to understand intuitively and mathematical modelling provides a useful tool for their analysis. Different mathematical tools can be used to analyse genetic networks, depending on their size and the knowledge of the roles of their components. This knowledge is particularly poor when considering genome-scale networks so that, in such cases, gene interactions are typically inferred by applying reverse engineering techniques. Moreover, networks of such a dimension are too complex to allow accurate modelling which accounts for all possible transcriptional regulatory mechanisms; therefore, methods that rely upon pair-wise comparisons of gene expression are generally applied by using, for instance, correlation-based [86] or information-theoretic measurements [110], a notable example being the ARACNE algorithm, which applies an information theoretic approach to eliminate the majority of indirect interactions inferred by co-expression methods [86], [71]. In contrast to these methods, Gaussian Graphical Models enable the inference of an interaction between two nodes to be done in the context of the whole system; however, being correlation-based, the metric evaluating statistical dependence among genes is less general than information theoretic estimates such as mutual information [112]. The resulting networks can then be analysed statistically, by evaluating their topological properties [1], [7], [111], but they are not suitable for dynamic simulations.

Because of these drawbacks, in this review we will focus on mathematical approaches for modelling signalling networks composed of a relatively small number of genes (from tens to a few hundred genes). These methods enable a more detailed analysis of the network structure and its dynamics, although raising the further issue of selecting biologically relevant genes. Formal approaches have been proposed which combine dimensionality reduction (to identify latent variables) and graphical modelling (to capture the remaining statistical structure not attributable to the latent variables) [15] but, in most cases, genes selection is performed by either differential expression or prior knowledge. These models can be classified into three main groups: logical, deterministic and stochastic. Logical models allow a qualitative understanding of the overall network dynamics and their simplicity makes possible the analysis of networks with a relatively large number of components [21], [52]. When a more detailed investigation is needed, continuous deterministic models, typically in the form of ordinary differential or differential-delay equations, may be developed to investigate the evolution in time of network response. Additional realism can be included by accounting for the effects of noise on gene expression. This stochasticity can be modelled at a single-molecule level [37], [38] or by applying Bayesian techniques [65], [32], [79], [64], [11].

A further benefit of modelling a small number of components is the possibility of investigating the influence of signalling networks among different cells by embedding sub-cellular models into a multiscale setting. In this regard, plants are ideal as model organisms because, unlike animals, plants do not require centralised centres to coordinate their development; their response to the environment is local and permits higher independence of their distant parts. In addition, cell walls play a simplifying role

from the modelling perspective: their presence reduces the complexity of cell-to-cell communication by allowing only small molecules, which stimulate cell growth and proliferation, to be transported between neighbouring cells; cell migration cannot occur. Techniques for staining such molecules also enable the geometry of the plant tissue to be readily visualised.

The remainder of this review is divided into two parts. In the first section, we describe general methods for modelling gene and signalling networks and illustrate how they may be applied to plants. In the second section, we summarise the main features of plant signalling, highlighting the differences with animal signalling; we then review cellular models of signalling perception and cross-talk in plants. We continue by reviewing how hormone perception has been studied in multi-cellular and multi-scale settings. The paper concludes with a summary of the insight gained from the different models and indicates possible directions for future research.

# 2. Mathematical models of gene networks 

In this section, we review the most common methods for modelling small gene networks. In section 2.1, we describe logical approaches as tools for preliminary, approximate analyses. We then review, in section 2.2 , more detailed techniques based on differential equations and, in section 2.3 , mathematical models that account for stochasticity. We present examples to illustrate how each modelling approach can be applied to the study of plant gene networks.

### 2.1. Logical models

Describing gene regulation with rules that do not represent biological details, logical models are suitable approaches to analyse global network dynamics [21], [52]. Their coarse-grained structure makes parameters search easier and may orient the development of more detailed quantitative ODE models [10]. Their introduction in molecular biology is due to Kauffman and Thomas [53], [40], [97] who employed them to determine how regulatory networks organise the development of sea urchin embryos.

Logical models represent the expression levels of each network component at discrete levels. As a first approximation, each gene can be considered to be either in an active or an inactive state. Such models are called Boolean models and their dynamics can be defined as follows.

Let us define the state of an $N$-dimensional network by a vector $\boldsymbol{x}=\left(x_{i}\right) \in \mathbf{B}^{N}$, with $i=1, \ldots, N$ and $\mathbf{B}=\{0,1\}$. The state transition from time $t$ to time $t+1$ is defined for each $x_{i}$ by the Boolean functions $f_{i}: \mathbf{B}^{k_{i}} \rightarrow \mathbf{B}$, with $1 \leq k_{i} \leq N$, as

$$
x_{i}(t+1)=f_{i}(\boldsymbol{x}(t)), \quad i=1, \ldots, N
$$

In this framework, the network usually evolves synchronously, over discrete time steps, according to the regulatory functions $f_{i}$ which are described using logical rules. The sequence of such transitions is called a trajectory which, passing through transient states, may stabilise at a point (steady state), a dynamic attractor (state cycle), or display chaotic behaviours [14]. Model generalisations include the incorporation of a larger number of discrete states and asynchronous transitions.

Logical models can be used to determine how local properties of gene regulation may affect the global dynamics of a network and to infer network interactions. One of the first logical tools was the REVEAL algorithm which, by optimising the mutual information within a dataset, determines for each gene a set of candidate parent nodes [65]. Extensions of the REVEAL algorithm have also been proposed in [119], $[80]$.

Despite their coarsed-grained structure, logical models cannot reach the genome scale because the set of all Boolean vectors and the number of interactions grows exponentially with the number of components, leading to excessive computational times as the size of the state space increases. Other drawbacks of Boolean models are that they provide limited detail and cannot always correctly model self-regulations. In fact, whereas in a continuous model the system is stabilised when a transcription factor down-regulates

itself, when using a Boolean network nodes repeatedly flip in a nonbiological manner between no activity and full activity [52], [54].

An application of logical gene networks in plants was developed by Espinosa-Soto et al. to analyse ABC floral genes during flower development in Arabidopsis [29]. Logical rules integrate published gene interaction data into a dynamic network model. By extensively analysing all possible initial conditions, the authors showed that the model always converges to a finite number of steady states that match the experimentally observed gene expression profiles. The authors interpreted their model to show that precise signalling pathways are not required to restrain cell types to those found in Arabidopsis, but these are rather determined by the overall gene network dynamics.

Boolean networks can be also used to translate information from microarray data into Boolean language in order to compare gene expression under different treatment conditions. This approach has been proposed by Genoud et al. to describe the signalling network associated with disease resistance in Arabidopsis [36]. In this way, the authors investigated multiple cross-talks between salicilic acid, ethylene and jasmonate in defence-related responses.

Incomplete knowledge may require consideration of several alternative regulatory mechanisms. A Boolean function, which synchronously and deterministically assigns the next state of a variable, does not permit investigation of different transition rules. This problem can be addressed by considering either asynchronous rules [98], or sets of Boolean functions assigning a probability to function selection. Networks which are modelled accounting for stochastic behaviour are called probabilistic Boolean networks [91], [90]. This method may be better suited to the design of a Boolean function from microarray gene expression data, the latter in general being sparse relative to the number of system variables. In fact the design process is likely to be imprecise because the number of possible input states is too large for accurate estimation. Associating a vector of Boolean functions for each node and selecting one of its components according to its corresponding probability may provide a more comprehensive exploration of transcriptional rules [91].

# 2.2. Differential equations based models 

Using logical rules to model gene expression can provide qualitative insight into the global dynamics of a network; conversely, continuous differential equation models permit quantitative and more direct comparisons with biological experiments. Different ODEs models can be developed depending on the level of detail needed to describe the underlying regulatory mechanisms.

As a first approximation, and in order to limit the number of equations and parameters involved, mRNA and protein levels can be viewed as a single variable, whose concentration is governed by a regulatory function. Let us consider a group of $N$ genes. If we denote by $x_{i}$ the concentration of the $i$ th component and by $f_{i}$ the function defining its net production rate, then the network is modelled by the system of ODEs

$$
\frac{d x_{i}}{d t}=f_{i}(\boldsymbol{x}(t), \boldsymbol{p}), \quad i=1, \ldots, N
$$

where the parameters $\boldsymbol{p}$ describe gene interactions (activations and repressions).
The choice of function $f_{i}$ depends on the level of detail needed. Several transcription functions have been proposed in the literature.

Linear models can be used to obtain approximate network dynamics. Their simplicity and the possibility of automating their construction makes them suitable for inference as, for example, in the TSNI algorithm [6], in which the possibility of including an external perturbation is also taken into account. In this case each regulatory function takes the form

$$
f_{i}:=\sum_{j=1}^{N} a_{i j} x_{j}(t)+\sum_{l=1}^{P} b_{i l} u_{l}(t), \quad i=1, \ldots, N
$$

where $a_{i j}$ represents the influence of gene $j$ on gene $i ; b_{i l}$ represents the effect of the $l$ th perturbation on $x_{i}$ and $u_{l}(t)$ represents the $l$ th external perturbation at time $t$. Other applications of linear models are described in [117], [68].

Alternatively, one approach which abstracts the details of the molecular mechanisms involved in gene regulation is based on piecewise-linear differential equations [40]. Transcription is modelled using discontinuous step functions, which resemble the switch-like behaviour of logical transcription rules. As a result, gene expression is modelled by systems of differential equations of the form

$$
\frac{d x_{i}}{d t}=g_{i}(\boldsymbol{x})-\gamma_{i} x_{i}, \quad i=1, \ldots, N
$$

where $x_{i}$ is the cellular concentration of the product of gene $i$ and $\gamma_{i}>0$ its degradation rate. The function $g_{i}: \mathbb{R}_{\geq 0}^{N} \rightarrow \mathbb{R}_{\geq 0}$ is defined as $g_{i}(\boldsymbol{x})=\sum_{l \in L} k_{i l} b_{i l}(\boldsymbol{x}) \geq 0$, where $k_{i l}>0$ is a parameter regulating the strength of transcription, $L$ is a set of indices and $b_{i l}: \mathbb{R}_{\geq 0}^{N} \rightarrow\{0,1\}$ is a function defined by sums and products of step functions that plays a role that is equivalent to a Boolean function.

To account for the affinity of transcription factors when binding a promoter, a more explicit regulatory function is needed. Hill functions allow gene regulation to be viewed as a sigmoidal function. For the case of an activator $A$ we have

$$
H_{A}\left(A, \theta_{A}, m_{A}\right)=\frac{\left(A / \theta_{A}\right)^{m_{A}}}{\left(A / \theta_{A}\right)^{m_{A}}+1}
$$

whereas for a repressor $R$ we have

$$
H_{R}\left(R, \theta_{R}, m_{R}\right)=\frac{1}{\left(R / \theta_{R}\right)^{m_{R}}+1}
$$

where $\theta_{A}, \theta_{R}>0$ are binding thresholds indicating the transcription factor concentration at which activation or repression is half-maximal and the parameters $m_{A}, m_{R}>0$ model the steepness of the switch [48]. By accounting also for degradation, the net gene transcription levels follow the differential equations

$$
\frac{d x_{i}}{d t}=f_{i}:=p_{i} \cdot H_{A}-d_{i} \cdot x \quad i=1, \ldots, N
$$

when the gene associated to the gene product $x_{i}$ is activated and where $p_{i}, d_{i}$ are respectively the net rates of production and degradation of $x_{i}, H_{A}$ being replaced by $H_{R}$ when $x_{i}$ is repressed. Other transcription functions of sigmoidal type have been proposed to infer transcriptional networks [117], [118], giving, for example, that

$$
f_{i}:=\frac{p_{i}}{1+\exp \left(-a_{i 0}-\sum_{j \in S} a_{i j} x_{j}\right)}-d_{i} x_{i}
$$

where $p_{i}$ is the maximum expression rate of the $i$ th gene and $d_{i}$ is its decay rate. This model was shown to reproduce well specific expression profiles of microarray data [118].

Grouping transcription and translation together depends on the underlying hypothesis that proteinprotein interactions have no substantial effect on the set of genes considered. When this assumption is not valid, translational effects should be treated separately. Notable examples of such reactions in plant signalling are the ubiquitination pathways that are involved in the perception of some hormones, see Section 3. These pathways can be modelled by using the law of mass action to determine the functional forms of the reaction rates and integrating the resulting differential equations with those that model transcriptional regulation, depending on the network topology [73], [78].

Although for piece-wise linear differential equations a number of analytical results have been obtained, particularly regarding the existence and stability of periodic orbits or aperiodic behaviours in specific networks [27], when equations (2.2) are nonlinear analytical investigations are in general more limited than in linear cases. However, it is possible to analyse numerically how the system behaviour depends on the network topology. The sensitivity of steady states to parameter values can also be investigated using

bifurcation analysis, to analyse qualitative changes in the overall systems dynamics [59], or sensitivity analysis to investigate how parameters uncertainty in the parameters of the model can quantitatively affect its variables [84]. Biological networks are known to include patterns that recur more frequently than random, these structures being called motifs. Well-studied motifs include auto-regulation, feedforward and feedback loops [2], [3], see Figure 1. Different motifs can generate different qualitative dynamics and influence other network components.
![img-0.jpeg](img-0.jpeg)

Figure 1. Schematic of common network motifs: (a) auto-regulation; (b) feedforward loop motif; (c) feedback loop motif; (d) de-repression motif. In Figures (a) and (b) all arrows represent a general regulation (which may be either an activation or a repression); in Figures (c) and (d) green arrows with pointed caps represent activations, red arrows with round caps repressions. Solid arrows represent transcriptional regulation, whereas dashed arrows represent protein-protein interactions (for example promoting ubiquitination).

Auto-regulation occurs when a transcription factor either represses or activates its own transcription, see Figure 1(a). In the former case, negative auto-regulation can play a dual role [2]. Firstly, in comparison with simple regulation, it accelerates the response time of the gene considered, its expression level quickly reaching its steady state. In addition, since a protein at high concentration reduces its production rate and the same protein at low concentration decreases it, negative auto-regulation can diminish the stochastic cell-cell variation in protein levels by narrowing the range of protein levels realised [3]. In contrast to negative auto-regulation, positive auto-regulation slows down response times and enhances variation. When the effect is strong, this regulatory motif may generate bi-stability and partition cell differentiation. Direct positive autoregulation has been shown to be essential for shoot apical meristem maintenance in rice [101]: the gene Oryza sativa homeobox1 (OSH1), a member of a family of genes (KNOX) known to regulate cell differentiation in shoots, is positively regulated by direct autoregulation. An analysis of mutants has revealed that positive autoregulation of OSH1 is vital for its expression and shoot apical meristem maintenance.

Feedforward loops consist of a gene A that regulates a second gene B both directly and indirectly through its regulation of a third gene C, which also regulates gene B, see Figure 1(b). Since each regulation can be either an activation or a repression, eight types of feedforward loops can be defined depending on the choices of the interaction signs. For each of these types, sub-cases can be considered depending on how co-regulation of gene B by genes A and C is modelled. Different qualitative dynamics can emerge from these motifs such as delay after stimulus addition, pulses in expression levels of gene

B and response acceleration [3]. Such a feedforward loop has been shown to control the timing of the switch from vegetative to reproductive development in Arabidopsis [89]. This switch is controlled by the transcription factor and meristem identity regulator LEAFY (LFY) in part via the direct activation of the gene CAULIFLOWER (CAL), which acts together with the transcription factor LMI1 to activate CAL expression.

Cells have developed control mechanisms to maintain gene expression within certain ranges. Such control can be achieved by including feedback loops, defined by a signal, a sensor, detecting the signal, and an effector, controlling cellular response, with the sensor having an output that loops back to control the effector [20]. In particular, when a gene influences, directly or indirectly, its own regulation the set of components involved is called a feedback-loop motif. Several types of feedback loop have been defined, depending on the sign of its regulation, its type (transcriptional or translational) and the number of elements of which it is composed. A common feedback loop comprises transcriptional activation of a gene coupled with degradation of the protein which is translated from that gene, see Figure 1(c). Coupling positive and negative regulation defines a negative feedback loop. Such feedback loops can generate oscillatory dynamics when additional interactions are included [60], [33]. Mathematical models of such systems confirm these observations for certain parameters ranges and when transcriptional regulation is delayed, for example by intermediate interactions prior transcription factor binding [73], [78], [41], [44], [103]. A notable example of a negative feedback loop comprising more than two components is the repressilator, this being made of three repressors hooked up in a cycle [2], [28]. When the production rates of the proteins are fluctuating, the repressilator usually generates noisy oscillatory dynamics. In Arabidopsis negative feedback loops have been identified within the set of genes that regulate the circadian clock [67]. There are two types of positive feedback loop whose interactions are transcriptional: doublepositive and double-negative loops. In the former case two transcription factors activate each other, while in the latter they both repress. Both motifs have a bi-stable nature; whereas double-positive loops can express both or neither transcription factors, double-negative loops can express either one or the other. Such switches in steady states enable cells to make irreversible decisions during developmental processes. An example of a positive feedback loop which may reinforce cell fate decisions and cell type patterning has been identified in the epidermis of the root of Arabidopsis [51]. The transcription factor gene MYB23 is part of a positive feedback loop: MYB23 gene transcription is promoted by a complex that includes the MYB23 protein. This complex determines cell pattern by specifying the non-hair fate (in cells accumulating this complex) and the hair fate (in adjacent cells).

A motif which occurs frequently in plants is the inactivation of repressor proteins, see Figure 1(d). This motif is present in most plant signalling pathways [96]. Mathematical modelling of signalling cascades comprising negative regulators suggests that this motif generates a faster response in downstream genes than direct activation [87]. Being able to respond rapidly may have conferred a selective advantage during plant evolution.

The models described above are based on the assumption that gene regulation occurs in a homogenous system in which all the network components maintain a uniform concentration. This is, in general, an over-simplification when considering different compartments or tissues. In this context, gene regulation can be more realistically modelled by using partial differential equations. Systems of reaction-diffusion equations are commonly used to analyse the formation of patterns in animal embryonic tissues, in which gradients of proteins specify tissue differentiation [102], [116], [19], [72]. In plants, a reaction-diffusion model has been shown successfully to explain the development of shoot apical meristems [34]. Molecular genetic studies revealed that the formation of shoot apical meristems is regulated by feedback between WUSHCEL (WUS) and CLAVATA (CLV). A reaction-diffusion based mathematical model has been developed to study interactions between WUS and CLV. The model reproduces patterns similar to those observed in wild type and mutant plants, suggesting that reaction-diffusion dynamics may play a crucial role in regulating this developmental process.

A mechanistic model has been also proposed to investigate the formation of dynamic patterns in root meristems of barley seedlings [26]. The authors developed a PDEs model that describes how the

density distribution of root apices evolves as a function of the root expansion rate, gravitropism and branching rate. They showed that development of a root system can be viewed as a propagating wave of meristematic activity, a 'meristematic wave', and that root system architecture is the footprint of this process.

# 2.3. Stochastic models 

Gene expression is a highly stochastic process due to the randomness of associations and dissociations between proteins and genes, RNA polymerase binding, open complex formation, translation and degradation of mRNA and proteins [50]. Such randomness can, in some cases, play an important role in gene expression and therefore stochastic models are valuable in providing a deeper understanding of stochastic variation in gene regulation. In this section, we review two types of model. In section 2.3.1, we explore how stochastic fluctuations can qualitatively modify the dynamics of a gene network. In section 2.3.2, we address how probabilistic or Bayesian techniques can be used to infer gene networks from incomplete and often noisy gene expression data.

### 2.3.1. Stochastic models of chemical kinetics

Deterministic models usually rely upon the law of mass action by assuming that stochastic fluctuations can be ignored due to the large number of identical and independent events occurring in each cell [82]. This approximation is not valid when the number of protein molecules falls to low values, in some cases as large as 100, and discreteness and stochasticity may play an important role. This role can be taken into account by applying stochastic state transitions as follows [38].

Given a set of $N$ chemical species $S_{i}$, with $i \in 1, \ldots, N$, interacting through $M$ chemical reactions $R_{j}$, with $j=1, \ldots, M$, in a medium of constant volume, we denote by $\boldsymbol{X}=\left(X_{i}(t)\right)$, with $i \in 1, \ldots, N$, the state vector at time $t$ of the number of molecules $X_{i}$ of the species $S_{i}$. Changes in the number of molecules over a time period $d t$ are due to the reactions $R_{j}$, which are characterised by two mathematical quantities: a state change vector $\boldsymbol{d} \boldsymbol{x}_{j}=\left(d x_{i, j}\right)$ describing the change of the system state, as a consequence of reaction $R_{j}$, from its state at time $t$, denoted by $\boldsymbol{x}$, to its state at time $t+d t$, given by $\boldsymbol{x}+\boldsymbol{d} \boldsymbol{x}_{j}$; a propensity function $a_{j}(\boldsymbol{x})$ describing the probability, given $\boldsymbol{X}(t)=\boldsymbol{x}$, that the reaction $R_{j}$ will occur in the time interval $[t, t+d t)$. In order to estimate the evolution of $\boldsymbol{X}(t)$ over time, we define $P\left(\boldsymbol{x}, t \mid \boldsymbol{x}_{0}, t_{0}\right)$ as the probability that the system is in state $\boldsymbol{x}$ at time $t, \boldsymbol{X}(t)=\boldsymbol{x}$, given $\boldsymbol{X}\left(t_{0}\right)=\boldsymbol{x}_{0}$ and we derive a time evolution equation for $P\left(\boldsymbol{x}, t \mid \boldsymbol{x}_{0}, t_{0}\right)$. The change of the probability of the system being in a particular state $\boldsymbol{x}$ over a time period $d t$ depends on the probability balance between the contribution from all other states to $\boldsymbol{x}$ during $d t$

$$
\sum_{j=1}^{M} a_{j}\left(\boldsymbol{x}-\boldsymbol{d} \boldsymbol{x}_{j}\right) P\left(\boldsymbol{x}-\boldsymbol{d} \boldsymbol{x}_{j}, t \mid \boldsymbol{x}_{0}, t_{0}\right)
$$

and the contribution of state $\boldsymbol{x}$ to the other states

$$
\sum_{j=1}^{M} a_{j}(\boldsymbol{x}) P\left(\boldsymbol{x}, t \mid \boldsymbol{x}_{0}, t_{0}\right)
$$

The result is the chemical master equation

$$
\frac{\partial P\left(\boldsymbol{x}, t \mid \boldsymbol{x}_{0}, t_{0}\right)}{\partial t}=\sum_{j=1}^{M}\left[a_{j}\left(\boldsymbol{x}-\boldsymbol{d} \boldsymbol{x}_{j}\right) P\left(\boldsymbol{x}-\boldsymbol{d} \boldsymbol{x}_{j}, t \mid \boldsymbol{x}_{0}, t_{0}\right)-a_{j}(\boldsymbol{x}) P\left(\boldsymbol{x}, t \mid \boldsymbol{x}_{0}, t_{0}\right)\right]
$$

Multiplying Equation (2.4) by $\boldsymbol{x}$ and summing over all $\boldsymbol{x}$ it follows

$$
\frac{d\langle\boldsymbol{X}(t)\rangle}{d t}=\sum_{j=1}^{M} \boldsymbol{d} \boldsymbol{x}_{j}\left\langle a_{j}(\boldsymbol{X}(t))\right\rangle
$$

that, in the particular case in which there are no fluctuations, so that $\left\langle a_{j}(\boldsymbol{X}(t))\right\rangle \equiv a_{j}(\boldsymbol{X}(t))$ and $\langle\boldsymbol{X}(t)\rangle \equiv \boldsymbol{X}(t)$, reduces to the system of coupled ODEs (2.2) with $f_{i}:=\sum_{j=1}^{M} d x_{i, j} a_{j}(\boldsymbol{X})$.

The influence of stochastic effects on network dynamics was shown in the pioneering work by Arkin et al. [4] on a bacteriophage infecting Escherichia coli cells. The relevance of inherent random fluctuations on concentration dynamics were anticipated by a mathematical model of a unimolecular chemical reaction in [8], [9] providing an extension to the current deterministic theories. The authors analysed the effects of random patterns on gene expression and, in particular, on the developmental choice between two different paths, the lysogenic and the lytic. Stochasticity was modelled by Gillespie's stochastic simulation algorithm to simulate individual reactions [37], [38]. This algorithm is based on a Monte Carlo procedure to simulate numerically the time evolution of the given chemical system. After initialising the system parameters, such as the number of molecules and the reaction constants, each reaction and its time interval are randomly selected, with a probability depending on the number of molecules of the reactants, and the time step is updated till a termination criterion is reached (for example when all the reactants have been selected). The underlying assumptions are that the system is confined to a constant volume, that it is in thermal equilibrium at some constant temperature and that the effects of non-reactive molecular collisions are negligible. Reactions involving synchronous collisions of three or more molecules are considered to occur with a negligible probability and are modelled as a chain of bi-molecular interactions. Using this approach Arkin et al. showed that the developmental choice between the lysogenic and lytic paths is the result of the stochastic fluctuations in the temporal pattern of the growth in protein concentration, which are in turn due to random fluctuations in the reactions rates of the chemical reactions comprising the regulatory circuit.

The main drawback of this approach is its computational cost, so that it can be used to analyse small scale networks only, composed of few tens of genes. For this reason, several variants of this algorithm have been proposed which sacrifice some levels of detail in order to improve its efficiency. These include hybrid approaches, in which the most abundant molecules are modelled using differential equations 39], and tau-leaping, which considers larger time steps and randomly selects reactions occurring within these time periods [57].

A stochastic model of the circadian clock of Arabidopsis proposed by Guerriero et al. 46] was able to explain the experimentally observed dampening of the oscillations in plants gene expression under constant light conditions and to predict that the desynchronisation between noisy oscillations in single cells contributes to the observed damped oscillations at the level of the cell population.

# 2.3.2. Bayesian models 

Bayesian networks were proposed as a new framework for discovering interactions between genes based on multiple expression measurements [31] and, since then, they have been extensively used to analyse gene expression data in relatively small datasets. A Bayesian network is a probabilistic graphical model in which conditional dependencies between random variables are incorporated in a directed acyclic graph that is constructed in the following way. Let us consider a set of random variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$ and associate with each variable a node of a directed acyclic graph. We denote by $\mathbf{P a}_{i}$ the set of parents of node $X_{i}$ as well as the variables corresponding to those parents. Given any set of random variables $\mathbf{X}$, the joint probability distribution of any member $\mathbf{x}=\left\{x_{1}, \ldots, x_{n}\right\}$ can be always written according to the chain rule as follows

$$
P(\mathbf{X}=\mathbf{x})=P\left(X_{1}=x_{1}\right) \prod_{i=2}^{n} P\left(X_{i}=x_{i} \mid X_{i-1}=x_{i-1}, \ldots, X_{1}=x_{1}\right)
$$

In particular, associating $\mathbf{X}$ with the graph and denoting by $\mathbf{p a}_{i}$ the set of values of $\mathbf{P a}_{i}$, the chain rule becomes

$$
P(\mathbf{X}=\mathbf{x})=\prod_{i=1}^{n} P\left(X_{i}=x_{i} \mid \mathbf{P a}_{i}=\mathbf{p a}_{i}\right)
$$

The absence of a directed edge in a particular graph is encoded as a conditional independency. Under the above assumptions, gene expression does not vary with time and a Bayesian network cannot account for network dynamics.

In order to analyse time series data it is necessary to consider dynamic Bayesian networks (DBNs). Let us suppose that the microarray data measure the time series expression of $N$ genes at $T$ data points. We denote the microarray dataset by $\mathbf{X}=\left(\mathbf{x}_{1}, \ldots, \mathbf{x}_{t}, \ldots, \mathbf{x}_{T}\right)$ where $\mathbf{x}_{t}$ corresponds to the expression level of the $N$ genes at the time point $t$. We assume that the data can be described using a first-order Markov model, in which the state vector at time $t$ depends only on that at time $t-1$. Under this assumption, together with the one of stability of the network structure at all the time points, it is possible to model any graph as a directed acyclic graph. Assuming that gene $j$ has $p_{j}$ parents, gene regulation can thus be modelled by the conditional probability

$$
P\left(\mathbf{X}_{t} \mid \mathbf{X}_{t-1}\right)=P\left(X_{t, 1} \mid \mathbf{P a}_{t-1,1}\right) \times \ldots \times P\left(X_{t, N} \mid \mathbf{P a}_{t-1, N}\right)
$$

for $t=1, \ldots, T$, where the vector $\mathbf{P a}_{t-1, j}=\left(P_{t-1,1}^{(j)}, \ldots, P_{t-1, p_{j}}^{(j)}\right)$ contains the random variables $P_{t-1, p_{k}}^{(j)}$, with $k=1, \ldots, p_{j}$, which are associated with the genes that are parents of the $j$ th gene at time $t-1$. By applying the chain rule the joint probability can be rewritten as

$$
P(\mathbf{X})=P\left(\mathbf{X}_{1}\right) P\left(\mathbf{X}_{2} \mid \mathbf{X}_{1}\right) \times \ldots \times P\left(\mathbf{X}_{T} \mid \mathbf{X}_{T-1}\right)
$$

The goal is now to select the graph that best fits the data. This is achieved either by optimising a suitable objective function, which is generally an approximation of the maximum likelihood, or by performing independence tests [114], [16]. Besides enabling the analysis of time courses, this framework provides the further advantage of extending the search to graphs that are not necessarily acyclic. Examples of Dynamic Bayesian networks applications can be found in [45], [62], [85].

Bayesian network algorithms vary according to the degree of knowledge about the observability of the data (full, partial) and the values of the random variables (continuous, discrete). The network can be inferred either by applying un-supervised, global approaches, or using semi-supervised methods that predict novel interactions starting from a known network [12], [113]. The performance of a continuous, linear-Gaussian state-space model proposed in [11] has been tested on a well-characterised Arabidopsis clock network using data from replicated time course microarrays [83]. The method was able to recover known links accurately, including the feedback loop between morning and evening elements of the clock, as well as to capture partially loops between some clock-related genes.

In [80], a discrete Bayesian network was used to analyse a set of genes known to regulate the circadian clock in Arabidopsis. The authors developed an algorithm to infer a network of transcription factors by iteratively adding genes to an initial set. The inferred interactions were in agreement with independent experiments on the circadian clock network.

Other graphical models include tree-based ensemble methods, e.g. random forests [49]; Gaussian graphical models for estimating multiple related graphs from several not independent and identically distributed assays, in which the experimental conditions may affect the interactions [17], and modular methods which estimate global network responses by perturbing functional units comprising groups of particular gene interactions [56]. Meta-analyses which combine different inference algorithms into a consensus method were also shown to limit systematic prediction errors [69], [70], [108].

# 3. Plant signalling networks 

In what follows, we review the main features of plant signalling and some of the mathematical models used to investigate the response of plant cells to hormone levels through a genetic network. In section 3.1 we describe the main features of the perception of the main plant hormones and highlight differences with animals. In section 3.2 we review how some of the signalling pathways of these hormones and their interactions with other hormones have been analysed using mathematical models.

# 3.1. Signal transduction in animal and plant cells 

Plants and animals have developed different sensitivities to external and internal signals so that they can efficiently adapt their response to their sessile or mobile life styles [96]. Environmental signals, such as light and temperature, play key roles in controlling plant growth; on the contrary, physiological responses are more influential in animals. In what follows, we describe the main differences between the signalling pathways of plants and animals and present examples of the perception of well-known plant hormones.

In contrast to animals, the limited mobility of plants required them to develop a faster adaptation to the environment and, to this end, a faster cellular response. The structure of a signalling pathway can have a strong effect on how quickly the cell can mount a response to a stimulus. For example, derepression of active genes can result in a fast response to hormonal stimulus (to about one fifth of the not regulated response) [87]. Thus, whereas the response of animal cells to hormone levels is mostly triggered by the activation of cascades of positive regulators, plant signalling tends to involve multiple repressions. Inactivation of negative regulators may be achieved by protein degradation or ubiquitination. Notable examples of signals with a ubiquitin-dependent pathway are the hormones auxin and gibberellin. The auxin response is controlled by activation of the $A u x / I A A$ genes, a family of genes that is rapidly induced in response to auxin (indole-3-acetic acid, IAA). Auxin binds to its receptor (TIR1), which interacts with the cullin AtCUL1 and a SKP1-like protein to form the auxin-SCF-TIR1 complex. This complex targets the Aux/IAA proteins for proteolysis and degradation and, as a result, promotes transcription of auxin response genes [55], [24]. Similarly, gibberellin binds to its receptor (GID1) which undergoes a conformational change enabling the GA-GID1 complex to bind DELLA proteins and tagging them for ubiquitin-dependent degradation [105], [106]. Degradation of DELLAs releases transcription factors PIF3,4 that promote gene expression.

Once the expression of genes responding to hormones is promoted through derepression, control loops are needed to avoid excess production of the associated proteins. This balance is achieved by downregulating gene expression through multiple negative feedback loops. In auxin signalling this occurs in the following way. Most $A u x / I A A$ genes have binding sites in their promoter region which are compatible with Auxin Response Factors (ARFs) and their binding can activate or inhibit Aux/IAA transcription [107], [47]. In vitro studies suggest that, when repressing, the associated negative feedback is caused by Aux/IAA-ARF heterodimers [100]. The resulting complex acts as a transcription factor repressing $A u x / I A A$ genes [99]. These sets of reactions constitute negative feedbacks of auxin response. Similarly, the levels of the hormone gibberellin are limited through multiple negative feedback loops, these being caused partly by the direct repression by DELLA proteins of their own transcription [115] and partly by their promotion of GID1 transcription, which is responsible for DELLA degradation. Schematic representations of auxin and gibberellin perception are shown respectively in Figure 2 and Figure 3. In both cases, the hormone binds to a receptor and degrades its response protein by ubiquitination: Aux/IAA in auxin pathway and DELLA in gibberellin signalling. The response protein dimerises and acts as a repressor on its gene forming a negative feedback loop.

Plants have evolved from both prokaryotic and eukaryotic ancestors. As a result, some of their signalling pathways are derived from bacteria. Examples are regulatory systems comprising two components, a sensor protein and a response regulator protein, see Figure 4(a). The sensor protein detects the signal in different locations of the plant cell and sends it, via phosphorylation, to the response regulator that controls gene expression. The receptor sequences of the plant hormones cytokinin and ethylene follow this regulatory system. Cytokinin is perceived at the plasma membrane by the receptors AHK2,3,4, which autophosphorylate in response to cytokinin binding. The AHK phosphoryl group is then transferred to the Arabidopsis His Phosphotransfer Proteins (AHPs) within the cytoplasm. They, in turn, transfer it to the type A and B Arabidopsis Response Regulators (ARR-A and ARR-B). A schematic representation of cytokinin perception is shown in Figure 4(b). The ethylene receptor is located in the endoplasmic reticulum. Ethylene inactivates the activated form of its receptors ETR1, ETR2, ERS1, ERS2, EIN4 and represses interactions between the receptor complexes and another negative regulator of ethylene response, CTR1, a protein that interacts directly with the receptors. As a result, the proteins EIN2,3

![img-1.jpeg](img-1.jpeg)

Figure 2. A schematic representation of auxin perception. Auxin binds to its receptor SCF-TIR1 and degrades Aux/IAA protein by ubiquitination. Aux/IAA transcription is repressed by the Aux/IAA-ARF dimer via a negative feedback loop.
![img-2.jpeg](img-2.jpeg)

Figure 3. A schematic representation of gibberellin perception. Gibberellin forms a complex with SCF-SLY2-GID1 and degrades DELLA protein by ubiquitination. DELLA transcription is repressed by DELLA-PIF dimers via a negative feedback loop.

are derepressed and act as transcription factors of ethylene response genes. A schematic representation of ethylene perception is shown in Figure 5.
![img-3.jpeg](img-3.jpeg)

Figure 4. Two-component signalling perception in prokaryotes (a) and a multi-step derivative of cytokinin perception in eukaryotes (b). Figure re-drawn and modified from L. Taiz, E. Zeiger [96].

# 3.2. Sub-cellular models of plant signalling 

Several mathematical models of plant hormone signalling have been proposed. In what follows, we review mathematical approaches that have been developed to study the perception of a single signal (see section 3.2.1) and then present further examples to show how integrated models of interacting signalling pathways can be developed (see section 3.2.2).

### 3.2.1. Models of signalling perception

In the previous section we have illustrated how plant hormones commonly act by derepressing transcription factors and how the expression of hormone response genes is controlled by negative feedback loops. This mechanism is not trivial and its dynamics can be better understood using mathematical models. A mathematical model of auxin signalling has been developed and studied by Middleton et al. [73], where the attention focuses on the role of auxin in regulating the expression of Auxin Response Factors (ARFs) and auxin response genes (Aux/IAAs). The model is formulated as a system of time-dependent, autonomous ordinary differential equations and the relevant concentrations and functional forms for the interaction terms are derived by appealing to the law of mass action and using Michaelis-Menten kinetics. For a particular range of parameters the system evolved to a stable limit cycle characterised by oscillations in $A u x / I A A s$ expression levels. Otherwise, a steady state results (either a stable node or a stable spiral). The predicted oscillatory behaviour was interpreted as a possible cause of the oscillations of an auxin reporter (DR5::GUS) in a proto-xylem cell located in the basal meristem as suggested in [23]. Such oscillatory behaviour is tissue specific, correlates with the branching of new lateral organs and was

![img-4.jpeg](img-4.jpeg)

Figure 5. A schematic representation of ethylene perception.
experimentally confirmed in [75] where the presence of these dynamics was detected in a large number of genes.

A recent deterministic model of gibberellin perception was developed in [74]. The model is based on ordinary differential equations derived from the mass action law with Hill kinetics. As mentioned in Section 3.1, gibberellin is perceived via multiple feedback loops. GA is synthesised via the action of enzymes of the GA 20-oxidase (GA20ox) and the GA 3-oxidase (GA3ox) families, which feedback on GA signalling. By combining mathematical modelling with in vitro and in vivo data on the expression levels of GA-responsive genes, the authors concluded that the GA20ox feedback dominates the GA3ox loop, the former being highly synergistic with GID and DELLA regulation.

A model of the transcriptional network involved in cytokinin perception was proposed in [42]. This model comprises cytokinin signalling and a regulator (WUS) that influences gene expression and patterning within the Arabidopsis shoot apical meristem. By applying this model, based on differential equations, the authors showed that feedback between the cytokinin response and key genetic regulators determines the probability that a cell will express WUS. Since WUS promotes cell proliferation and stem cells are a source of active cytokinin, the authors' results may support the hypothesis that a positive feedback loop between stem cells and rib meristem cells maintains the organisation of the shoot apical meristem when stem cells are displaced during growth.

A quantitative framework for simulating ethylene signalling was proposed in [25]. The authors developed a continuous, deterministic model of the activation dynamics of the gene ERF1 in response to ethylene signalling. This model predicts an ERF1 dose-response curve that has the same qualitative form as the phenotypic dose-response curves obtained experimentally. The authors concluded that the phenotypic dose-response curves obtained experimentally could be due, at least in part, to changes in ERF1 caused by different ethylene concentrations. In addition, the ethylene pathway may filter stochastic and rapid chaotic fluctuations in ethylene availability.

# 3.2.2. Models of signalling cross-talk 

Since the dynamics of hormone perception are influenced by cross-talk with other hormonal pathways, it is natural to aim to develop new models that couple different pathways.

A mathematical model which integrates auxin and cytokinin signalling pathways, by extending the model developed in [73], was proposed in [78]. The model is based on ordinary differential equations derived from the mass action law with Hill kinetics. Cytokinin plays a negative role during lateral root development by disrupting the regular pattern of division that characterises the organisation of the lateral root primordium [61]. This effect is correlated with a reduced expression of PIN genes in the founder cells, which prevents an auxin gradient from forming. In particular, the expression of PIN1,2,3,4 and 7 was reduced in cytokinin treated plants. By developing a model of cross-talk, the authors showed in [78] that the cytokinin pathway may play an antagonistic role to the auxin pathway by causing the cessation of periodicity. Tissues with high levels of auxin and low levels of cytokinin, such as the division zone, may maintain periodic dynamics, whereas tissues with higher relative levels of cytokinin signalling, such as the elongation zone, may find their oscillatory dynamics being eliminated.

A modelling and experimental analysis of the cross-regulation of auxin, cytokinin and ethylene was undertaken by Liu et al. [66]. A key role is played by the gene POLARIS (PLS), whose action influences the biosynthesis of and the interactions between, the hormones auxin, cytokinin and ethylene. A combination of modelling and experiments implies that PLS is at the centre of a regulatory loop involving auxin and ethylene. In more detail, PLS is responsible for the accumulation of auxin in the root tip; auxin, together with cytokinin, synergistically activates the biosynthesis of ethylene; ethylene, in turn, exerts a feedback control on PLS, down-regulating its transcription. The authors conclude that integrating biological knowledge into a mathematical model opens many channels to study the dynamics of systems with multiple hormones and stress the relevance of embedding a single-cell model in a spatio-temporal environment to account for how the interplay among hormones depends on the spatial expression of genes.

### 3.3. Multi-scale analysis of plant signalling

The availability of tissue specific promoters has recently made it possible to analyse the influence of hormones when targeted in specific root tissues by investigating their effects in mutant plants [104]. Experimental observations of the hormone-mediated promotion of cell-wall-remodelling enzymes led to the general idea that cell expansion is due to the balance between the yielding of the cell wall and turgor pressure when new cell wall is synthesised [81]. From this viewpoint it would follow that the global effect of multiple hormonal pathways involves transcriptionally regulating genes that control cell expansion. Identifying where these signals are synthesised, how they flow among different tissues and how they communicate both sub-cellularly and between adjacent cells would provide a deeper insight about how their local activities promote an overall, coordinated cell growth. Multi-scale models can help analysing subtle effects of this spatial, dynamical cross-talk. A multi-cellular model of the role of auxin in regulating root growth has been developed by Grieneisen et al. [43]. The model is developed in a cellular potts framework and diffusion and permeability are dealt with independently, using realistic parameter values. The simulations reproduce the spatial distribution of auxin in the root of Arabidopsis; nevertheless, although the model is multi-cellular, it is not multi-scale in the sense that the signalling network responsible for auxin perception at a sub-cellular level and its possible feedbacks on auxin transport were not included.

A recent analysis in this vein was performed on gibberellin perception in [5]. The authors embedded the model developed in [74] in a multi-scale spatial framework to analyse the interplay between GA signalling and root growth. The model represents the elongation zone of the Arabidopsis root as a single cell file and simulates with differential equations gibberellin movement on the subcellular scale, treating each cell as comprising four compartments: the vacuole, nucleus, cytoplasm, and adjacent cell wall. From one side the authors investigated the effects of growth on the spatial distribution of the hormone gibberellin in the root elongation zone. Dilution was found to play a key role in creating a significant gradient in gibberellin levels, which decrease as cells pass through the elongation zone. From the other side, by incorporating

the pathway of gibberellin perception, it was possible to predict a gradient in DELLA proteins, which act as growth repressors, providing an explanation for the reduction in growth towards mature root regions. Such model provides valuable steps towards more sophisticated root models incorporating realistic root geometries and cross-talk among different hormone pathways.

# 4. Conclusion 

Plant cells differentiate as a result of their unequal response to heterogeneous distributions of hormones across different tissues. In each cell the perception of hormones stimulates a network of partially known interactions that eventually leads to a cell decision. Identifying and understanding the dynamics of such interactions is not intuitive and requires mathematical modelling to obtain more detailed insight.

Several types of mathematical models have been proposed to analyse genetic networks. In this review, we first described these classes of models and how they have been applied to study genetic networks in plants. Subsequently, after describing how signals are perceived by plants and the main differences with animal signalling, we focused on reviewing mathematical models of signal perception and cross-talk in plants, and in particular on the model system of Arabidopsis. Sub-cellular models may provide useful information by exploring how the network topology affects the qualitative dynamics of gene response, by quantifying parameters of production and degradation through calibrations against experimental data and by reverse engineering unknown interactions.

Plant growth is controlled by hormones that lead this developmental process in a tissue specific way [104]. The capability of hormones to be transported and their permeability across tissues, makes a multi-scale analysis a natural extension of sub-cellular mathematical models of signalling networks. This approach has been recently applied to analyse gibberellin perception in Arabidopsis.

Further extensions of this analysis may lead in future to a detailed understanding of tissues specification in realistic geometries that accounts for hormone transport. Since each tissue has different bio-mechanical properties, influencing for example the effects of cell growth, proliferation and death, a higher level of cross-talk will need to be considered between the influence that different hormones have on plant growth and the environmental and bio-mechanical effects on hormone levels.

Acknowledgements. We gratefully acknowledge the Biotechnology and Biological Research Council and the Engineering and Sciences Research Council for financial support as part of the CISB programme award to CPIB. The work of the second author was supported in part by Award No. KUK-013-04, made by King Abdullah University of Science and Technology (KAUST).
