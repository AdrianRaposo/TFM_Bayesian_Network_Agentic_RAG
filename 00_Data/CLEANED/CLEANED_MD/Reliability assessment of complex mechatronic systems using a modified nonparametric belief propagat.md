# Reliability assessment of complex mechatronic systems using a modified nonparametric belief propagation algorithm 

Xiaopin Zhong, Mohamed Ichchou, Alexandre Saidi

## To cite this version:

Xiaopin Zhong, Mohamed Ichchou, Alexandre Saidi. Reliability assessment of complex mechatronic systems using a modified nonparametric belief propagation algorithm. Reliability Engineering and System Safety, 2010, 95 (11), pp.1174-1185. 10.1016/j.ress.2010.05.004 . hal-02075618

## HAL Id: hal-02075618 <br> https://hal.science/hal-02075618v1

Submitted on 23 Oct 2020

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Reliability assessment of complex mechatronic systems using a modified nonparametric belief propagation algorithm 

X. Zhong ${ }^{\text {a }}$, M. Ichchou ${ }^{\text {a,* }}$, A. Saidi ${ }^{\text {b }}$<br>${ }^{a}$ Laboratoire de Tribologie et Dynamique des Systèmes, École Centrale de Lyon-36, Avenue Guy de Collongues, 69130 Ecully, France<br>${ }^{\mathrm{b}}$ Laboratoire d'Informatique en Image et Systèmes d'Information, École Centrale de Lyon-36, Avenue Guy de Collongues, 69130 Ecully, France

Various parametric skewed distributions are widely used to model the time-to-failure (TTF) in the reliability analysis of mechatronic systems, where many items are unobservable due to the high cost of testing. Estimating the parameters of those distributions becomes a challenge. Previous research has failed to consider this problem due to the difficulty of dependency modeling. Recently the methodology of Bayesian networks (BNs) has greatly contributed to the reliability analysis of complex systems. In this paper, the problem of system reliability assessment (SRA) is formulated as a BN considering the parameter uncertainty. As the quantitative specification of BN, a normal distribution representing the stochastic nature of TTF distribution is learned to capture the interactions between the basic items and their output items. The approximation inference of our continuous BN model is performed by a modified version of nonparametric belief propagation (NBP) which can avoid using a junction tree that is inefficient for the mechatronic case because of the large treewidth. After reasoning, we obtain the marginal posterior density of each TTF model parameter. Other information from diverse sources and expert priors can be easily incorporated in this SRA model to achieve more accurate results. Simulation in simple and complex cases of mechatronic systems demonstrates that the posterior of the parameter network fits the data well and the uncertainty passes effectively through our BN based SRA model by using the modified NBP.

## 1. Introduction

Reliability analysis is an essential element during the development of mechatronic systems. The attempt to improve system reliability makes the system reliability assessment (SRA) an ongoing research topic. A number of methods for SRA have been developed, most of which estimate the system reliability using only the data of components since it is much easier and less expensive to test the components/subsystems than the entire system. In general, the authors believe that SRA remains a difficult problem for the following reasons.

- Complexity: Products are built increasingly complex due to added functionalities. It becomes more difficult to propagate component information to the system level in those systems with high complexity.
- Expensiveness: of testing. Testing a whole complex system tends to be impossible. Reliability assessment at the system

[^0]level requires a good tool to efficiently combine the information collected from various levels and diverse sources.

- Functional and temporal dependency: A failure might be caused by more than one mutually-dependent event, such as shared causes, exclusive events and standby redundancies. The exploitation of explicit dependence is itself a challenge.
- Uncertainty due to variability of model, also known as epistemic uncertainty. This arises from a lack of knowledge about the probability distribution of time-to-failure data.

SRA is clearly a problem of system decision with inherent ambiguities. The statistical inference provides a promising methodology for such decision problems by finding the "best guess" for the interesting items given the existing observation. As one of the most popular approaches over the last decade, Bayesian networks (BNs) have many advantages over the classical reliability formalisms when applied to SRA [1,2]. BNs can deal with the problem of dependency under not only temporal but also functional relations. The BN formalism can accept and integrate the diverse data from all kind of sources, such as the prior specifications given by manufacturers, the historical TTF data and the current testing data. In a BN, we can easily propagate the uncertainties, which would be difficult and even impossible with conventional logic models, e.g. fault trees and


[^0]:    * Corresponding author. Tel.: +33 04721862 30; fax: +33 0472189144.

    E-mail addresses: xiaopin.zhong@ec-lyon.fr (X. Zhong).
    mohamed.ichchou@ec-lyon.fr (M. Ichchou), alexandre.saidi@ec-lyon.fr (A. Saidi).

event trees. Moreover, the methodology of BNs has been so wellstudied that we have many options for modeling and reasoning in various situations.

However, the previous research on BNs has not paid enough attention to the parameter uncertainty of failure models that are usually parametric skewed distributions. There are obviously some unobservable items (e.g. no test data) in a complex mechatronic system, thus it is a challenge to estimate the model parameters of those items. The main contribution of this research is that we propose a continuous BN model to estimate the optimal configuration of time-to-failure (TTF) model parameters for a complex mechatronic system using data from diverse sources, and we develop a modified nonparametric belief propagation algorithm to obtain the marginal density in non-singly-connected BNs without the use of a junction tree.

The remainder of this paper is organized as follows. After reviewing the related works in Section 2, we formulate in Section 3 our basic model of system reliability assessment. In Section 4, the nonparametric belief propagation is modified and applied to the inference of the basic model. The simulation results and discussion shown in Section 5 demonstrate that our model is effective and efficient. Finally, some conclusions and perspectives are offered in Section 6.

## 2. Related works

In this section, the related methods of system reliability assessment (SRA) are reviewed and classified, especially those using the BN based approaches. Since there exist various methodologies for modeling and analyzing system reliability, the authors also refer the readers to a more detailed classification by Mihalache [3] and an alternative review by Zio [4].

In the past decades, many methods have been applied to SRA with the help of specific mathematical tools, such as fault trees (FTs) [5], reliability block diagrams [6], petri nets [7], method of moments [8] and so on. Among these approaches, the FT formalism is undoubtedly the most widely used one due to its efficiency and the capability of system abstraction. However, it cannot cope with the temporal or functional dependency among components. To deal with the temporal interrelation, people proposed Markov chain (MC) method [9,10] and dynamic fault trees (DFTs) [11,12]. The problem of combinatorial explosion is nevertheless intractable when applying those two well-known methods to highly-complex mechatronic systems. Moreover, they work only under the assumption that the TTF of components obey the exponential distribution law. In recent years, Bayesian reliability analysis has proved to be a powerful tool providing important methodological advantages over the conventional techniques [13]. The BN methodology is strongly recommended [1] as an effective and versatile SRA tool that is capable of modeling both temporal and functional dependency. Another important advantage over traditional approaches is the ability to combine the information from diverse sources [14]. BNs become attractive due to the ease of building a BN from FT [15] and directly from existing data [16].

In the authors' view, the published approaches based on BNs can be classified into three categories according to the variable type in the network. (1) Working state based BNs, also known as event based BNs. The working state usually indicates fail/work which is inherited from binary decision diagrams (BDD) and FTs. The node variables are thus defined in discrete space. Most published research work [17,18,2] falls into this category. For more flexibility in modeling the working condition, Weber [19] introduced the multi-state variable to describe the degradative states of items in dynamic Bayesian networks (DBNs). These
methods calculate the distribution of system state deterministically by using conditional probability tables (CPTs) established by experts in advance. However, the temporal dependency might be time-varying due to the existence of component deterioration and environment change. An unchangeable CPT may mismatch the time-varying temporal dependency. Furthermore, the working state based BNs are not flexible enough to analyze the risk in continuous time space because the estimation must be reexecuted at each timestamp concerned. (2) TTF model based BNs. These BNs assign a probabilistic description to the TTF data of an item, see the simple example of binary distribution discussed by Langseth [1]. Boudali [20] presented a non-parametric discretetime TTF model, and Boudali [21] succeeded in modeling a continuous-time TTF in close-form without considering the model uncertainty. However it is still non-trivial to directly model the TTF because of the complexity of modeling an arbitrary probability density in continuous space. Johnson [22] and Anderson-Cook [23] modeled the distribution parameters of TTF as a continuous unknown variable, such as the scale and the shape of a 2D Weibull density. This facilitates passing information through the network and the reliability analysis at system level based on the characteristics of the skewed distributions, e.g. Weibull analysis. Therefore, the uncertainty of the model parameters must unavoidably be considered. The problem of SRA is hence regarded as an inference of the continuous model parameters in a BN. We notice three advantages compared with the first category: any parametric distribution can be used to model the TTF model parameters uniformly or differently; no CPT needs to be completed, the dependency is specified according to the problems or learned from examples; after statistical inference, the posterior finds the "best guess" solution and fully describes the uncertainty relative to the TTF model parameters. (3) Hybrid state based BNs. Neil [24] and Marquez [25] have successfully modeled TTF distribution by continuous random variables as well as by discrete random variables (e.g. working states of items). In fact, the discrete variables can be directly appended into the BNs of the second category when the TTF models of items are ready. In all the research works above, little study was made of parameter uncertainty in the TTF model for system reliability, though it has long been investigated in relation to component reliability $[26,27]$.

On the other hand, a number of statistical inference algorithms have been proposed to perform reasoning in a graph. Exact inference in discrete state BNs is possible with some exact marginalization algorithms for trees, such as variable elimination, belief propagation [28] and junction trees [29]. However, the integral in continuous state space still raises some difficulties. Until recently a number of discretization methods have been suggested to perform the inference in the continuous graph [30], such as mixture of truncated exponentials [31] and dynamic discretization [24,32]. Most of these methods rely on the junction tree algorithm in the case of non-singly-connected BN. However, performing an inference in the junction tree with treewidth $k_{t}$, will have at least one computation which requires time exponential in $k_{t}$, due to the marginalization process over supernodes. Therefore the junction tree based methods become less attractive for mechatronic systems because the subsystems in a mechatronic system, especially the electronic devices, commonly have a large number of components (input items), which leads to a large treewidth in the generated junction tree. We found that the sampling based nonparametric belief propagation (NBP) [33] is efficient and applicable to our BN model because of the flexible uncertainty representation by means of kernel density estimation (KDE, an open-source toolbox of KDE has been provided by Ihler [34]). Unlike the other inference methods for loopy graphs, the NBP does not propagate information in a

junction tree, but instead it iterates the message updates in a loopy graph until convergence.

From the review above, we see that the previous research has not paid enough attention to the stochastic nature of parametric TTF models in system reliability. In this paper, we formulate a new BN model to cope with the parameter uncertainty of the SRA problem. Our proposed BN model falling into the second category is an extension of the formalism of Bayesian component reliability [13], see Section 3 for the basic model. In contrast with conventional methods, we do not predefine the quantitative part of BNs, but learn the dependency, which is derived from probabilistic noisy gates, from some sample testing data. This model is efficiently solved by a modified version of the NBP algorithm.

### 3. A new model for SRA

Unlike the continuous time-to-failure (TTF) models in [21,35], our method for SRA uses the general BN framework to model the failure parameters of items in the complex system and their dependency. This model allows us to estimate the parametric TTF distributions of all items given the observed failure data as evidence.

As the qualitative part of a BN model, the directed acyclic graph (DAG) can be constructed from the fault tree model by Bobbio's method [15]. However, in our model the network variables denote neither the working state of items nor the items' TTF, but the items' failure parameters which are function outputs of the noisy gates rather than the deterministic gates. By "noisy" we do not mean the uncertainty of the output event (success/failure) as do the methods in other published work [15,35], rather we mean the uncertainty of the model parameters of the output failure distribution. For example, a simple OR-gate system C is shown in Fig. 1a with two basic independent components A and B. A, B and C have exponential failure distributions with the failure rates $$λ_a$$, $$λ_b$$, and $$λ_c$$ respectively. Their failure times are denoted by $$t_a$$, $$t_b$$, and $$t_c$$ respectively. If the OR-gate is deterministic, C fails when either A or B fails. Then C fails in the time interval (0,t] with the probability $$Pr(t_c \leq t) = Pr(t_a \leq t \cup t_b \leq t) = Pr(t_a \leq t) + Pr(t_b \leq t) - Pr(t_a \leq t)Pr(t_b \leq t)$$. Notice that for an exponential failure distribution $$Pr(t) = 1 - e^{-λt}$$. Therefore the failure rate of C can be obtained from the equation above, i.e. $$λ_c^d = λ_a + λ_b$$, where the superscript d represents the deterministic case. Analogously in the case of the deterministic AND-gate, $$Pr(t_c \leq t) = Pr(t_a \leq t \cap t_b \leq t)$$, then $$λ_c^d = -\frac{1}{2}ln(e^{-λaT} + e^{-λaT} - e^{-tλa} + λaT)$$. We say that the gate is noisy or uncertain, then the failure rate is contaminated by a noise, such as $$λ_c = λ_a^d + w_c$$ where $$w_c$$ is an additive noise. This parameter uncertainty can be perceived by the stochastic nature of failure density in reliability analysis, see Fig. 2. Indeed, this uncertainty is common in a mechatronic system for at least the following reasons.

First, not all failure modes can be found because of the large number of components in the electronic and mechanical subsystems. The modes not found can have more or less influence on the gates. Second, the multi-parameter skewed distributions are widely used for a mechatronic system due to its various failure modes. For some multi-parameter distributions, the deterministic output parameters may not have any solution because we have only one equation (the output failure distribution). Third, the effect of environment is usually unmeasurable, especially for the electronic and mechanical subsystems.

None of the previous research has addressed this noise which is difficult to measure. Fortunately, this uncertainty can generally be described by a statistical model on the test data acquired from the basic components as well as from the system. The SRA problem can then be formulated as a probabilistic reasoning process for the failure parameter of each item given the test data.

As analyzed above, it is difficult to model the parameter uncertainty directly. For this reason we turn to the TTF density that is a function of the parameters. We denote the density by $$f_i(x_i, t)$$, $$i \in 2n$$, where 2n is the label set of the nodes in the BN and $$X_i = x_i$$ is a unified notation for all types of multidimensional parameters. For brevity the time is hereafter omitted in density expressions. For instance, the exponential TTF density of $$X_i$$ in Fig. 1c is $$f_c(X_c = λ_c) = f_c(λ_c) = λ_c e^{-λcT}$$, $$t \geq 0$$.

Fig. 2 shows the stochastic nature of failure density in reliability analysis. Thus a probability distribution is expected to represent the stochastic nature of $$f_i(X_i)$$, $$i \in 2n$$. Notice that a higher probability should be assigned to an uncertain density that is closer to the deterministic density. Then some symmetrical distributions, such as the normal and the triangular distributions, can be selected when no other prior information is known [26]. In this paper, the normal distribution is used because of its flexibility. Further the "closer" is measured based on a distance

![img-0.jpeg](img-0.jpeg)

**Fig. 2.** The stochastic nature of failure density in reliability analysis.

![img-1.jpeg](img-1.jpeg)

**Fig. 1.** The simplest OR-gate and AND-gate models described by Fault tree (FT) and Bayesian network (BN). The BN model is converted from the FTs by the method in [15]. (a) FT OR-gate model, (b) FT AND-gate model and (c) BN model.

function *d*(*·*,·) between probability densities. Thus the parameter uncertainty can be reduced to the distance uncertainty,

$$d(f_i(X_i), f_i^d) \sim \mathcal{N}(0, \sigma_i), \quad i \in \mathcal{I} \text{n},\tag{1}$$

where *f*<sup>*i*</sup><sub>*i*</sub> denotes the deterministic output density function of the gate going to node *i*. *N*(0, σ<sub>*i*</sub>) is a normal distribution with zero mean and standard deviation σ<sub>*i*</sub> which will be discussed at the end of this section. Note that a distance cannot be negative. A one-sided normal distribution is then considered. Then given σ<sub>*i*</sub>, we have

$$\Pr\left\{d(f_i(X_i), f_i^d) \mid \sigma_i\right\} = \frac{2}{\sqrt{2\pi}\sigma_i} \exp\left\{-\frac{d^2(f_i(X_i), f_i^d)}{2\sigma_i^2}\right\}, \quad i \in \mathcal{I} \text{n}.\tag{2}$$

In fact this "one-sided" transformation does not affect the simulation results of those parameters because of the normalization stage in a probabilistic inference algorithm. The formulation above plays the role of output parameter prediction based on the parameters of the basic items.

For the gates with more than two basic items, the deterministic output density functions *f*<sup>*d*</sup><sub>*i*</sub> can still be derived without difficulty [13]. For a series structure, the system functions only if all components function, i.e. for *i* ∈ ℤ*n*,

$$f_i^d = \sum_{j \in \mathcal{B}(i)} f_j(x_j) \cdot \prod_{k \in \mathcal{B}(i)} (1 - F_k(x_k)),\tag{3}$$

where *B*(i) denotes the label set of node *i*'s basic component nodes and *F*<sub>*k*</sub>(*X*<sub>*k*</sub>) is the cumulative probability function of *f*<sub>*k*</sub>(*X*<sub>*k*</sub>). *B*(i) *j* means the set *B*(i) except *j*. For a parallel structure, the system functions if any component functions, i.e. for *i* ∈ ℤ*n*,

$$f_i^d = \sum_{j \in \mathcal{B}(i)} f_j(x_j) \cdot \prod_{k \in \mathcal{B}(i)} F_k(x_k).\tag{4}$$

Series and parallel structures are special cases of *k*-of-*n* systems, which can be re-structured as *C*<sub>*k*</sub><sup>*i*</sup> parallel subsystems of *k* series components. Hence any *k*-of-*n* system can also be analyzed by a repeated calculation of Eqs. (3) and (4).

So far we can obtain the dependency between the output parameter and the parameters of basic items in Eqs. (2)–(4). Finally the quantitative part of our BN model, i.e. the conditional probability distribution (CPD), is defined by

$$\Pr(X_i = x_i \mid X_i = x_i)_{\hat{i} \in \mathcal{B}(i)} = \Pr\left\{d(f_i(\hat{i}, i), f_i^d) \mid \sigma_i\right\}, \quad i \in \mathcal{I} \text{n}.\tag{5}$$

There are many choices for the distance function between probability densities [36], such as Kullback–Leibler (KL) divergence and Euclidean distance. The following example demonstrates the effect of the dependency described above.

**Example.** A simple exponential-distributed series system consists of two components, whose FT model has the same structure as that of Fig. 1a. The TTF of node A is modeled as exponential density with failure rate λ<sub>*a*</sub> = 0.68 and that of node B is modeled as Weibull distribution with shape *k*<sub>*b*</sub> = 1.5 and scale λ<sub>*b*</sub> = 1. We discretize the densities (time interval = 10<sup>−3</sup>s) and take the KL divergence as distance metric. The distribution of the system parameter ⟨*X*<sub>*c*</sub>⟩ given the parameters of the basic items, i.e. Pr(*X*<sub>*c*</sub> = λ<sub>*c*</sub>) *X*<sub>*a*</sub> = (λ<sub>*a*</sub>), *X*<sub>*b*</sub> = (*k*<sub>*b*</sub>, λ<sub>*b*</sub>)), is then calculated from Eq. (5) and shown in Fig. 3 for different deviation value σ<sub>*c*</sub>. From Fig. 3 we observe that the smaller σ<sub>*c*</sub> is, the sharper the distribution is. In other words, the gate tends to be deterministic with the decrease of σ<sub>*c*</sub>. While σ<sub>*c*</sub> increases, the information from the basic items to the system tends to be cut off by the gate because Pr(*X*<sub>*c*</sub>) *X*<sub>*a*</sub> = (λ<sub>*a*</sub>), *X*<sub>*b*</sub> = (*k*<sub>*b*</sub>, λ<sub>*b*</sub>) tends to be uniform and no uncertainty can pass through a uniform CPD.

The remainder of this dependency model is the standard deviation σ<sub>*i*</sub> in Eq. (2) that encodes the dependency between the parameters of the basic items and those of the higher level

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** The distribution of output parameter given the parameters of the basic items.

item. In order to achieve the best distinguishing capacity of Eq. (2), this standard deviation can be estimated by a parameter estimation technique. The maximum likelihood estimation (MLE) approach is selected in our implementation because of its ease of use. If there exists adequate sample data, MLE yields

$$\sigma_i^s = \arg\max_{\sigma} \prod_{j} \Pr(y_j \mid \sigma_i), \quad i \in \mathcal{I} \text{n},\tag{6}$$

where *y*<sub>*j*</sub> = *d*(*f*<sub>*j*</sub><sup>*i*</sup>⟩, *f*<sub>*i*</sub><sup>*i*</sup>) is called pseudo-observation that represents the distance between a sample candidate density *f*<sub>*i*</sub><sup>*i*</sup> and the deterministic density *f*<sub>*i*</sub><sup>*d*</sup>. The above formulation can be converted to logarithmic interpretation to avoid the trouble of exponential overflow. In practice, we reuse this parameter σ for the same type of components or subsystems. The readers are referred to Section 5 for a simulation example of this standard deviation estimation.

### 4. Approximate inference

After modeling, the Bayesian network needs a process of probabilistic reasoning, i.e. an approximate inference in the continuous networks. The inference task of a BN is to calculate the posterior marginal probability of each hidden variable given the observed variables. We have various methods to perform the approximate inference in a continuous network [30]. As described in Section 2 the conventional inference methods for non-singly-connected continuous graphs depends on a junction tree, such as dynamic discretization in [35,32]. However, the computation of exponential in treewidth makes the junction tree based methods less attractive for mechatronic applications. Recently a nonparametric belief propagation (NBP) in Markov random fields (MRFs) has attracted our attention because of its reasoning capacity and efficiency in the general loopy graphs. In particular, it is a linear time algorithm proportional to the number of hidden variables. To facilitate the inference process of NBP, we need to convert the BN to a corresponding MRF. Then following a brief introduction of NBP, a modification on the NBP is made to adapt the NBP to the newly-generated MRF.

#### 4.1. NBP algorithm in pairwise MRF

According to Weiss' method [37], arbitrary BN can be converted to an undirected graphical model, i.e. pairwise MRF. An

![img-3.jpeg](img-3.jpeg)

Fig. 4. An example of the conversion from (a) a BN to (b) the corresponding pairwise MRF and (c) the local message passing in the MRF. The shaded circles represent the hidden nodes and the white circles denote the observed ones. (a) BN model, (b) pairwise MRF model, and (c) local message passing in MRF.

example of this conversion is demonstrated in Fig. 4. The method is to add a cluster node for the parent nodes that share a common child in the BN, add the connection between the cluster node and the parents/child, then replace the directed arcs with undirected ones. In the example, the variable for the newly-created node is denoted by \( X_5 \) which is a compound variable of the parents, i.e. \( X_5 = \{X_{5,2}, X_{5,3}, X_{5,4}\} \). We say \( X_5 \) and \( X_4 \) are consistent with each other if \( x_{5,4} = x_4 \) and inconsistent if \( x_{5,4} \neq x_4 \). For convenience in the pairwise MRF, we still call node 1 the child of node 5 and node 2 (or 3, 4) a parent of node 5. The child set and the parent set of a cluster node, say \( i \), are denoted by \( i \langle b_i \rangle \) and \( \forall a(i) \) respectively. Furthermore \( \mathcal{I}_c \) refers to the label set of the cluster nodes and \( d_i \) denotes the corresponding test data (e.g. TTF) of node \( i \), \( i \in \mathcal{I}_n \).

Besides the qualitative specification, the corresponding MRF and the original BN should have the same joint probability distribution, which is a quantitative part of the graphical model. Suppose that all probabilities are positive, the Hammersley–Clifford theorem [28] guarantees that the joint probability distribution can be factorized into a product of the compatibility functions of the cliques over the graph. Thus the joint density of a pairwise MRF is factorized as follows

$$
\operatorname{Pr}(X, D) \propto \prod_{i \in \mathcal{I}} \phi_i(X_i) \prod_{i \in \mathcal{I}_f} \prod_{j \in \Gamma(i)} \psi_{ji}(X_i, X_i),
\tag{7}
$$

where \( \mathcal{I} = \{\mathcal{I}_n, \mathcal{I}_c\} \). \( X \) and \( D \) denote the joint variable and joint observation respectively. \( \Gamma(i) \) denotes the label set of neighbors of node \( i \). The quantitative specification of a pairwise MRF is then composed of \( \phi_i(\cdot) \) and \( \psi_{ji}(\cdot, \cdot) \), named as first-order potential and second-order clique potential respectively. They encode the dependency between nodes and are set in the following way so that the joint probability distribution of the MRF is identical to that of the BN: \( \phi_i(X_i) = \operatorname{Pr}(d_i|X_i) \) represents the likelihood of observed data \( d_i \) with respect to variable \( X_i \), implying the local evidence; \( \psi_{ji}(X_i, X_i) \) is the child's conditional probability given the corresponding cluster variable if it is a potential between a cluster node and the corresponding child (e.g. node 5 and node 1 in Fig. 4b); otherwise, \( \psi_{ji}(X_i, X_i) \) is set to one if the compound node is consistent with the parent node and zero otherwise. For the example in Fig. 4b, \( \psi_{51}(X_5, X_1) = \operatorname{Pr}(X_1|X_5) \), \( \psi_{25}(X_2, X_5) = 1 \) if \( X_{5,2} = X_2 \) (\( X_2 \) and \( X_4 \) are consistent with each other) and 0 when \( X_{5,2} \neq X_2 \) (inconsistent). Finally \( \operatorname{Pr}(X, D) = \prod_{i} \operatorname{Pr}(d_i|X_i) \cdot \operatorname{Pr}(X_1|X_2, X_3, X_4) \), which is identical to that of the BN model.

In the belief propagation (BP) algorithm, we use a so-called "message" from a hidden node (say \( j \)) to another one (say \( i \)) to describe how likely node \( i \) will be in one state given the knowledge of node \( j \), i.e. \( m_j(X_i) \), see Fig. 4c for message passing paths. The belief at node \( i \) denotes how likely node \( i \) should be in one state given the information from neighbors and from its local evidence. It is then proportional to the product of local evidence and all the messages coming to node \( i \), i.e.

$$
b_i(X_i) \propto \phi_i(X_i) \cdot \prod_{j \in \Gamma(i)} m_j(X_i).
\tag{8}
$$

Accordingly, the estimates of minimum mean square error (MMSE) and maximum a posterior (MAP) are obtained based on this belief. Furthermore, the messages are updated iteratively by the rule

$$
m^t_j(X_i) = \alpha \sum_{X_j} \psi_{ji}(X_i, X_i) \cdot \phi_j(X_i) \cdot \prod_{k \in \Gamma(j)} m_{k_j}^t \cdot (X_j),
\tag{9}
$$

where \( t \) indicates the iteration index and \( \alpha \) is a normalization constant. The summation is replaced by an integral with respect to \( X_j \) for a continuous network. The BP is also known as a sum–product algorithm. It has been proven [38] that in the case of a singly-connected graph, the BP in fact converges and gives the exact marginal probabilities for all the hidden nodes. Although the BP cannot guarantee the convergence in the loopy case, the BP has been applied with experimental success [39].

Until recently, the techniques of Monte Carlo sampling and kernel density estimation has provided an efficient way to perform BP inference in loopy continuous graphs, named nonparametric belief propagation (NBP, [33]). It is called nonparametric because the message is represented by a mixture of Gaussian which is a sample-based or kernel density estimate

$$
m_j(X_i) = \sum_{n=1}^{N} w_j^{(n)} \cdot \mathcal{N}(X_i; \mu_j^{(n)}, \Delta_j),
\tag{10}
$$

where \( w_j^{(n)} \) is a weight associated with \( n \)th kernel mean \( \mu_j^{(n)} \), and \( \sum_{i} w_j^{(n)} = 1 \). \( N \) is the number of kernel means used for density estimation. \( \Delta_j \) is the common bandwidth. The belief (Eq. (8)) and message updating (Eq. (9)) are implemented by using sampling-based approximations in two stages: message product and message propagation.

In the first stage, the product of \( m \) \( N \)-component messages yields a new mixture of Gaussian with \( N^m \) components. Each component and its weight can be obtained by the following equations

$$
\mathcal{N}(\overline{\mathcal{X}}; \overline{\mu}, \overline{\mathcal{A}}) \propto \prod_{i=1}^{m} \mathcal{N}(\overline{\mathcal{X}}; \mu_i, \Delta_i),
\tag{11a}
$$

$$
\overline{\mathcal{A}}^{-1} = \sum_{i=1}^{m} \Delta_i^{-1}, \quad \overline{\mathcal{A}}^{-1} \overline{\mu} = \sum_{i=1}^{m} \Delta_i^{-1} \mu_i,
\tag{11b}
$$

$$
\overline{\overline{\mathcal{W}}} = \prod_{i=1}^{m} w_i \mathcal{N}(\overline{\mathcal{X}}; \mu_i, \Delta_i) / \mathcal{N}(\overline{\mathcal{X}}; \overline{\mu}, \overline{\mathcal{A}}).
\tag{11c}
$$

To avoid the exponentially-large number of mixture components, a Gibbs sampler [40] is employed to draw \( N \) independent samples as

kernel means of the message product. In our experience, about one hundred kernels make it possible to achieve satisfying approximations of the 2D and 3D densities even for a rare event. It is not surprising that this approximation is much faster than the other stochastic simulation methods, such as Markov chain Monte Carlo (MCMC) which requires many more samples to stochastically update the density representation.

In the second stage, the NBP propagates each component of a message by approximating the integral in Eq. (9). Before the propagation, the product of $$ \int \psi_{ji}(X_i, X_i) \, dX_i $$ and $$ \phi_j(X_i) $$ are regarded as a marginal influence and calculated as $$ \xi(X_i) $$,

$$ \xi(X_i) = \phi_j(X_i) \int_{X_i} \psi_{ji}(X_i, X_i) \, dX_i. $$

For message $$ m_{ji}(X_i) $$, each sample $$ x_i^{(n)} $$ drawn from the product $$ \xi(X_i) \phi_j(X_i) \prod_{k \in \Gamma(j) \times I} m_{ki}(X_i) $$ in the first stage is propagated to node $$ i $$ by sampling $$ X_i $$ from $$ \psi_{ji}(X_i^{(n)}, X_i) $$ using importance sampling or MCMC techniques. After obtaining those output samples as kernel means of the updated message, we can choose a kernel bandwidth $$ A_i $$ by leave-one-out likelihood cross-validation [41]. We refer the readers to [33] for the detailed generic NBP algorithm.

### 4.2. Modified NBP

We notice that the generic NBP may encounter two problems in the newly-generated MRF when propagating the message between a cluster node and its parents, because of the specification of second-order clique potentials generated by the conversion from BN to MRF. Without loss of generality, we suppose node $$ s \in \mathcal{I} \text{c} $$ is a cluster node and node $$ p \in \mathcal{P} a(s) $$ is one of its parents. Like the example in Fig. 4b $$ X_5 = (X_{5,2}, X_{5,3}, X_{5,4}) $$, we denote by $$ X_{i,p} $$ the corresponding component of node $$ p $$ in compound variable $$ X_i $$. Then we discuss the message propagation stage for the constructions of $$ m_{ip}(X_p) $$ and $$ m_{pi}(X_s) $$ as follows respectively.

First, since the second-order clique potential between $$ X_s $$ and $$ X_p $$ is a delta function, any common sampling technique for $$ X_i \sim \psi_{pi}(X_p, X_s) $$ or $$ X_p \sim \psi_{sp}(X_s, X_p) $$ is unfeasible. We suggest making them consistent with each other instead of sampling. For example, given a message product sample $$ x_i^{(n)} $$ of $$ X_i $$ we set $$ x_i^{(n)} = x_i^{(n)} $$ as a new sample of $$ X_p $$. Vice versa, when given a sample $$ x_i^{(n)} $$ of $$ X_p $$ we set $$ x_i^{(n)} = x_i^{(n)} $$. For the other components in $$ X_i $$, sampling techniques can still be used. However, $$ \psi_{pi}(X_p, X_s) $$ does not provide any information about the other components except that of node $$ p $$. Any sampling method will sample from a uniform distribution for the other components.

The second concern is that sampling the other components from uniform distributions will degenerate the message product $$ \prod_{p \in \mathcal{P} a(s)} m_{pi}(X_s) $$. We use a two-component example for further explication. When a system, say $$ X_3 $$, consists of two basic components, say $$ X_1 $$ and $$ X_2 $$, we can refer $$ X_4 = (X_{4,1}, X_{4,2}) $$ to the compound node. Then the kernel means of message $$ m_{14}(X_4) $$ are sampled as described in the first issue, i.e. $$ x_{4,1}^{(n)} = x_i^{(n)} $$ and $$ X_{4,2} $$ sampled from uniform distribution. The kernels of message $$ m_{24}(X_4) $$ are obtained in the same manner. Before propagating those messages to node 3, a message product is required. Fig. 5 shows a possible kernel of $$ m_{14}(X_4) $$ and two possible kernels of $$ m_{24}(X_4) $$. According to the rule of message product in Eqs. (11a)–(11c), their product is also a normal function whose mean is a linear interpolation of two kernels. Obviously, the important region for the following message propagation is a small area where the samples get high probability in both components, such as the ellipse region in Fig. 5. This is because concentrating the samples in this area can reduce the estimation variance and failing to do so leads to a biased estimation of the density [42]. However in this two-component example, most of these product

![img-4.jpeg](img-4.jpeg)

**Fig. 5.** The degeneration problem of message product in a two-component case.

**Table 1**

Algorithm of modified NBP for pairwise MRFs converted from BN by Weiss' method [37].

1. Initialization:

   (1) sample randomly N kernel means for all messages,

   (2) initialize the messages $$ m_{ji}^i, i \in \mathcal{I}, j \in \Gamma(i) $$ as uniform distributions, i.e. $$ w_i^{(n)} = 1/N $$,

   (3) initialize the iteration step $$ t = 0 $$ and the maximum iteration number $$ T $$.

2. Updating the messages and the beliefs for $$ i \in \mathcal{I}, j \in \Gamma(i) $$: given input messages $$ m_{ki}^i(X_i) = (x_{ki}^{(n)}, A_i)^{T}, w_{ki}^{(n)}, \sum_{i} = 1 $$, where $$ k \in \Gamma(j) \times I $$, construct $$ m_{ki}^{(n)} \sum_{i} $$ as follows

   (1) determine the marginal influence of Eq. (12) to get $$ \xi(X_i) $$,

   (2) draw N samples $$ (x_i^{(n)})^N_{i-1} $$ from the product $$ \xi(X_i) \prod_{k} m_{ki}^i(X_i) $$ by using Eqs. (11a)–(11c) and the Gibbs sampler depicted in [33],

   (3) for $$ n = 1, \ldots, N $$, update kernel means:

   — if $$ j \in \mathcal{I} \text{c} $$ (or $$ i \in \mathcal{I} \text{c} $$) and $$ i \in \text{Ch(j)} $$ (or $$ j \in \text{Ch(i))} $$, draw a sample from $$ x_i^{(n)} $$ — $$ \psi_j(X_i) = x_i^{(n)}, X_i $$) by importance sampling or MCMC technique,

   — if $$ j \in \mathcal{I} \text{c} $$ and $$ i \in \mathcal{P} a(j) $$, $$ x_i^{(n)} = x_i^{(n)} $$,

   — if $$ i \in \mathcal{I} \text{c} $$ and $$ j \in \mathcal{P} a(i) $$, $$ x_{ji}^{(n)} = x_i^{(n)} $$, the remaining components are sampled from previous beliefs by Gibbs sampler, i.e.

$$ x_{ji}^{(n)} \sim \phi_j(X_i) \prod_{k \in \Gamma(i)} m_{ki}^i(X_i), r \in \mathcal{P} a(i) \cdot j $$

   (4) Construct $$ m_{ji}^{(n)} \sum_{i} (X_i) = (x_{ji}^{(n)}, A_i)^{T}, w_{ji}^{(n)} \sum_{i} = 1 $$,

   — set $$ w_i^{(n)} $$ as the importance weights (if they exit) generated by sampling techniques,

   — select a bandwidth $$ A_i $$ by using the method in [41].

3. If $$ t + 1 \in T $$, set $$ t = t + 1 $$ and go to step 2.

4. Compute the MMSE and MAP estimations, for $$ i \in \mathcal{I} n $$:

   (1) compute the beliefs and normalize them, $$ b_i(X_i) \times \phi_j(X_i) \prod_{k \in \Gamma(i)} m_{ki}^i(X_i) $$,

   (2) find the optimum, $$ \hat{x}_i^{\text{MAP}} $$ — argmax$$_{x_i^{(n)} } b_i(X_i^{(n)}), \hat{x}_i^{\text{MMSE}} = \sum_{i} b_i(X_i^{(n)}) x_i^{(n)} $$,

kernel means (N in total) are spread out instead of being concentrated into the important region. Therefore there will be a degeneration of the sample set for the message product. It occurs in the multi-component case in the same way.

Our strategy to overcome this degeneration is to obtain the samples of the other components from their corresponding beliefs instead of from uniform distributions. For the above two-component example, given all the messages of previous time step i.e. $$ m_{ji}^{(n)} (X_i) $$, $$ i \in \mathcal{I} $$, $$ j \in \Gamma(i) $$, and the kernel mean set of current message product for node 1 i.e. $$ \{x_i^{(n)} \}_{ n = 1 } $$, the kernel means of current message $$ m_{14}(X_4) $$, denoted by $$ x_{ji}^{(n)} = (x_{14}^{(n)}, x_{14}^{(n)}) $$ where $$ n = 1, \ldots, N $$, are sampled as follows: $$ x_{14}^{(n)} = x_i^{(n)} $$; draw a sample $$ x_{14}^{(n)} $$ from $$ \phi_j(X_{2}) \prod_{k \in \Gamma(2) \times I} m_{ki}^{(n)} (X_{2}) $$. In fact $$ \Gamma(2) \times I = 0 $$ for this two-component example. The multi-component case can be deduced by analogy. Now the samples of message product are certainly concentrated into the important region by this means.

In summary, a modified version of NBP is then proposed for our pairwise MRF and Table 1 shows the steps of the algorithm. In

practice, our simulation demonstrates that one hundred kernels is enough to achieve good convergence results.

### 5. Simulation analysis: application to mechatronic systems

In this section, we demonstrate simulations on a hypothetical mechatronic system: an active vehicle suspension (AVS). We start by giving a brief description of the complex system. Our model is then applied to its passive subsystem with/without observation and the entire system itself. These simulations are all implemented based on the Kernel Density Estimation (KDE) Matlab toolbox [34].

The AVS system is intended to support the vehicle body and reduce body vibration from the road surface. Fig. 6 shows the fault tree of some important components/subsystems. Apart from the linkage which is considered to be unfailing, the parallel system is composed of two subsystems: a passive subsystem and an actuator subsystem. When the two subsystems both function, the suspension works in semi-active mode. It fails if none of the subsystem functions. But then it works in passive mode if only the actuator subsystem fails and in active mode if only the actuator subsystem functions. Moreover, the passive subsystem works in a series structure with the spring and damper components. So does the actuator subsystem whose failure can be provoked by a series mechanical part or by a series electronic part.

This FT description (Fig. 6) is then converted to BN representation (Fig. 7a), by the transition algorithm of Bobbio [15]. For simplicity, only constant failure rates of the root components are taken from the reliability data base [43] and given in Table 2, where the unit of failure rate has been converted to failure-per-kilometer by assuming a constant velocity. Moreover, their observations are sampled from the corresponding exponential distribution of km-to-failure (KTF).

#### 5.1. Passive subsystem

##### 5.1.1. Learning the dependency

The passive subsystem is a simple series case with only three nodes. The failure rate (FR) of the subsystem is thus 0.785 × 10<sup>−7</sup> F/km when decided deterministically. Given its true FR we can obtain the optimal deviation parameter σ<sub>2</sub><sup>2</sup> of node 2 by

![img-5.jpeg](img-5.jpeg)

**Fig. 6.** A fault tree example of an active vehicle suspension.

![img-6.jpeg](img-6.jpeg)

**Fig. 7.** The corresponding BN model and pairwise MRF model of an active vehicle suspension. The gray circles represent hidden nodes and the white ones denote cluster nodes. (a) BN model and (b) pairwise MRF converted from BN model.


**Table 2**

![img-7.jpeg](img-7.jpeg)

**Fig. 8.** Monte Carlo simulation of learning σ in Eq. (6), where X4=0.105×10−7 F/km, X5=0.68×10−7 F/km.

Monte Carlo simulation of Eq. (6). Thanks to the easy manipulation of discretized probability density function (PDF), the density distance measure in Eq. (2) is defined as a city block difference between two densities,

$$d(r, q) = s_t \cdot \sum_{i} |r_i - q_i|, \tag{13}$$

where r<sub>i</sub> and q<sub>i</sub> are discretized values of the two probability densities r and q. s<sub>t</sub> is the constant interval of the discretization. A curve of σ<sub>2</sub><sup>2</sup> with respect to actual FR λ<sub>2</sub><sup>true</sup> is illustrated in Fig. 8 after maximum likelihood estimation (MLE). For a series structure, the FRs greater than the deterministic one (sum of the components' FR) are not feasible, thus plotted by a dashed line. It is also found that the optimal σ is monotonically decreasing with respect to the distance from observed FR to the deterministic one that is indicated in the figure by dash-dot straight line. This is sound because the increasing FR implies decreasing dependency (see in Eq. (2)) when it is less than the deterministic one.

### 5.1.2. SRA of unobserved subsystem

Without loss of generality, the KTF data is modeled by a one-parameter exponential distribution. Using the i.i.d. KTF data observed in Table 2, the likelihoods of the observation with respect to FR are calculated as follows:

$$L_i(d_i|x_i) \propto \prod_{n=1}^{\text{10}} \text{Pr}(d_i^{(n)}|x_i), \quad i = 4, 5, \tag{14}$$

where d<sub>i</sub><sup>(n)</sup> denotes the nth sample KTF in the data set of d<sub>i</sub>. We show the normalized likelihoods with solid line in Fig. 9a and b respectively. When the passive subsystem is unobserved and has no priors, the likelihood curve with respect to FR is assumed to be uniform in the range of [0.485×10−7 F/Km, 1.085×10−7 F/Km], shown as a solid straight line in Fig. 9c. After 10 iterations of inference by our modified NBP, the maximum marginal criteria yields the marginal posterior (MP) distributions. They are plotted in Fig. 9a, b and c with dash-dot lines for the spring (node 4), the damper (node 5) and the passive subsystem (node 2) respectively. Notice that the posteriors are all sharper than the normalized likelihoods even when the priors do not exist. This implies that the network has been correctly driven by the dependency defined in Eq. (2). To compare more easily, the actual FRs of the components and the deterministic FR of the subsystem are all indicated in those figures by dashed straight lines.

The comparison of those estimates is also reported in Table 3. The results are identical to the densities in Fig. 9. In this table MLE comes from normalized likelihood density, while the minimum mean square estimation (MMSE), maximum a posterior (MAP) and the quantiles are evaluated by using the posterior distribution. Notice that the MMSE results are much closer to the actual values than the MLE results. We also obtain the MMSE and the MAP of subsystem, which is not feasible for MLE. These confirm the effectiveness of our model. Furthermore, Fig. 9d presents the reliability of the subsystem given by R2(t)=exp[-x2(t)] with the mean of the marginal posterior (solid line) and 90% confidence intervals (dashed lines) respectively.

### 5.1.3. SRA of observed subsystem

In the following example, we kept the configuration of Section 5.1.2 unchanged except that the subsystem acquired 30 KTF data given as Passive device in Table 2. We use a Weibull distribution with two parameters for the subsystem node. The likelihood of the observed data with respect to FR can be estimated in the same way as done in Section 5.1.2. It is plotted in Fig. 10c by a surface in the 2D Weibull parameter space: shape and 1/scale (for comparing the FR because scale=FR−1 when the shape is set at one). After 10 iterations of our modified NBP, we likewise obtain the FR's marginal posteriors (MP) of the components and the Weibull's marginal posterior surface of the subsystem in Fig. 10. Notice that the marginal posteriors in Fig. 10a and b are sharper than those of Section 5.1.2 because we have received more evidence for the network. In the same way, the posterior in Fig. 10d has less covariance than the normalized likelihood does in Fig. 10c. Moreover, MAP of the posterior is much closer to the actual value than the MLE, see Fig. 10d and c where the straight solid line indicates the actual FR (0.785×10−7 F/Km). These results demonstrate that our model is validated by the inference.

![img-8.jpeg](img-8.jpeg)

**Fig. 9.** Normalized likelihood and marginal posterior (MP) of FR in the passive subsystem. In (a), (b) and (c) solid lines stand for the likelihoods, dash-dot lines for the posteriors and dashed lines for the actual values. In (d) the solid line represents the reliability of the subsystem by FR's posterior mean and the dashed lines for those of 5% and 95% quantiles of the posterior, indicating the 90% confidence intervals.

**Table 3**

**Comparison of FR estimations in passive unobserved subsystem (F/10<sup>7</sup> km).**


The goodness-of-fit is discussed based on the statistic of Bayesian χ² presented in [13] where K = 4 ≈ 30<sup>0.4</sup> equal probability bins are suggested for our case. We draw repeatedly from the marginal posterior of Weibull parameter space, say (a,b), and compute the corresponding cumulative probability of observations' likelihood, F_{lik}(d_{i}|(a,b)). We decide which bin the draw should be assigned to, and calculate the Bayesian χ² statistic, then compare it against the 0.95 quantile of χ² (χ²_{0.95} ≈ 7.82). We observed that 13% of these values exceed the quantile, which indicates that the marginal posterior fits the subsystem's data observed reasonably well.

Notice that in this example the newly-observed data is successfully combined into the network and this can yield an up-to-date posterior estimation. In the same way, other types of new data, such as expert prior and historical data, can also be integrated to the network without difficulty. More information is fused, more-accurate estimation can be achieved. This can further help to identify the system deterioration by sequential updating after replacing the past observation with the new one.

### 5.2. The entire mechatronic system

In this example, the new SRA model is tested on the entire system by the NBP and the modified NBP respectively. In this system only the root nodes are observed and given in Table 2 (all data except the passive subsystem). As a deterministic function, a series structure of exponential family still has an output of exponential distribution, but a parallel structure does not. Therefore we use a Weibull distribution for the system node and the exponential family for the subsystems. The actual FR of the nodes are given in Table 4, where the optimal deviation is leaned by Eq. (6) with some simulated observation by the density distance measure in Eq. (13). Note that a loop (formed by node 3, 6, 7, and 10) exists in the actuator subsystem. Hence the inference algorithm needs more iterations to converge. After 60 iterations in the modified NBP, we obtain the MMSE and MAP results of the system as well as those of the subsystems, shown in Table 4. Notice that the errors of MMSE results are all less than 10% even without any observation of those nodes. The further reliability assessment can be accomplished by using the corresponding TTF distribution model, as done in Fig. 9d.

We also show every-five-iterations the convergence process of the system's Weibull parameters in Fig. 11, where the points indicate the MMSE values by NBP and modified NBP respectively.

![img-9.jpeg](img-9.jpeg)

Fig. 10. Likelihood and marginal posterior (MP) of passive subsystem (X2) with respect to Weibull parameters (shape and 1/scale) after 10 iterations of inference.

Table 4 Comparison of FR estimation in the suspension system.


It is clear that our modification makes NBP converge much faster. All these results demonstrate again that our dependency model is effective by using the normal distribution in Eq. (2).

### 6. Conclusion

In this research, the system reliability assessment (SRA) has been formulated as a statistical inference problem of Bayesian networks (BNs). In contrast to conventional methods, we model the time-to-failure of the system/components by the parametric distributions whose parameters are considered as random variables in the BN, such as failure rate of exponential family, shape and scale of 2D Weibull family and so on. Further, the parameter uncertainty of output function is modeled by a normal distribution whose standard deviation can be learned from samples. All of these uncertainties constitute the quantitative specification of the BN. To avoid the use of junction trees which are inefficient for the large-treewidth mechatronic systems, a modified nonparametric belief propagation (NBP) is developed to perform the inference in the BNs. For reasoning in a continuous BN, this provides an alternative solution to the other methods, such as mixture of truncated exponentials (MTE), dynamic discretization (DD) and Markov chain Monte Carlo (MCMC).

![img-10.jpeg](img-10.jpeg)

Fig. 11. Scale and shape means of system Weibull model in 60 iterations by the NBP and the modified NBP algorithm. The dashed lines denote the actual values.

Experimental results demonstrate the efficiency of our NBP modification and the effectiveness of our SRA method: the posterior fits the observed data well, and the uncertainty is effectively propagated through our BN based SRA model. Based on the parametric time-to-failure (TTF) representation, our BN model can perform further analysis, such as sensitivity analysis, diagnosis analysis. One future work is to consider model selection for unobservable items. It is another future work to apply our SRA method to the reliable active control issue in complex structural problems [44–46].

## Acknowledgment

The authors would like to thank China Scholarship Council (CSC) 2007153069 for the financial support of this research and gratefully acknowledge the anonymous referees for all their insightful comments and very helpful suggestions.

## Appendix A. Notation


- **C<sub>n</sub><sup>k</sup>** : combination: the number of k-combinations from the set with n elements
- **m<sub>ij</sub>(X<sub>j</sub>)**: message from node i to node j
- **x<sub>ij</sub><sup>(i)</sup>** : the nth kernel mean in message m<sub>ij</sub>(X<sub>j</sub>)
- **x<sub>ij</sub><sup>(i)</sup>** : corresponding component of variable X<sub>i</sub> in the nth kernel mean of message m<sub>ij</sub>(X<sub>ij</sub>)
- **w<sub>ij</sub><sup>(i)</sup>** : weight associated with nth kernel mean in message m<sub>ij</sub>(X<sub>j</sub>)
- **A<sub>ij</sub>** : common bandwith of message m<sub>ij</sub>(X<sub>j</sub>)
