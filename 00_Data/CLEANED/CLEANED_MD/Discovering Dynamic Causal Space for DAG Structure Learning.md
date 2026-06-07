# Discovering Dynamic Causal Space for DAG Structure Learning 

Fangfu Liu<br>Tsinghua University<br>liuff19@mails.tsinghua.edu.cn<br>Xiang Wang ${ }^{\dagger}$<br>University of Science and Technology of China<br>xiangwang1223@gmail.com

Wenchang Ma<br>National University of Singapore<br>e0724290@u.nus.edu<br>Yueqi Duan<br>Tsinghua University<br>duanyueqi@tsinghua.edu.cn

An Zhang ${ }^{\text {a }}$<br>National University of Singapore<br>anzhang@u.nus.edu<br>Tat-Seng Chua<br>National University of Singapore<br>dcscts@nus.edu.sg

## ABSTRACT

Discovering causal structure from purely observational data (i.e., causal discovery), aiming to identify causal relationships among variables, is a fundamental task in machine learning. The recent invention of differentiable score-based DAG learners is a crucial enabler, which reframes the combinatorial optimization problem into a differentiable optimization with a DAG constraint over directed graph space. Despite their great success, these cutting-edge DAG learners incorporate DAG-ness independent score functions to evaluate the directed graph candidates, lacking in considering graph structure. As a result, measuring the data fitness alone regardless of DAG-ness inevitably leads to discovering suboptimal DAGs and model vulnerabilities.

Towards this end, we propose a dynamic causal space for DAG structure learning, coined CASPER, that integrates the graph structure into the score function as a new measure in the causal space to faithfully reflect the causal distance between estimated and groundtruth DAG. CASPER revises the learning process as well as enhances the DAG structure learning via adaptive attention to DAG-ness. Grounded by empirical visualization, CASPER, as a space, satisfies a series of desired properties, such as structure awareness and noiserobustness. Extensive experiments on both synthetic and real-world datasets clearly validate the superiority of our CASPER over the state-of-the-art causal discovery methods in terms of accuracy and robustness.

## CCS CONCEPTS

- Mathematics of computing $\rightarrow$ Causal networks; $\cdot$ Computing methodologies $\rightarrow$ Causal reasoning and diagnostics.


## KEYWORDS

Differentiable Causal Discovery, Score-based Structure Learning, Score Function, DAG-ness Aware Scoring

[^0]
## ACM Reference Format:

Fangfu Liu, Wenchang Ma, An Zhang, Xiang Wang, Yueqi Duan, and TatSeng Chua. 2023. Discovering Dynamic Causal Space for DAG Structure Learning . In Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD '23), August 6-10, 2023, Long Beach, CA, USA. ACM, New York, NY, USA, 12 pages. https://doi.org/10.1145/3580305. 3599309

## 1 INTRODUCTION

Learning directed acyclic graph (DAG) structure from observational data (i.e., causal discovery) is a fundamental problem [52] in machine learning for a broad range of applications, including genetics [22], biology [33], economics [35, 36] and social science [41]. The purpose of DAG structure learning is to discover causal relationships among a set of variables that are encoded in a DAG [48]. Conventional score-based methods assess the directed graph candidates by utilizing a pre-defined score function over the DAG space [47]. However, the intractable combinatorial nature of acyclic space frames DAG learning as a combinatorial optimization problem w.r.t. discrete edges, which has been proven to be NP-hard [7]. A recent breakthrough, NOTEARS [58], successfully transforms the discrete DAG constraint into a continuous equality constraint, resulting in a differentiable optimization framework with an acyclic regularization term. Following differentiable causal discovery methods $[3,25,54,55,59,60]$, inspired by NOTEARS [58], optimize the score function by leveraging various highly parameterized deep networks via gradient descent. Though effective, these cutting-edge methods inevitably simplify the searching space from DAG space to directed graph space, further increasing the risk of discovering suboptimal DAGs.

This motivates us to rethink the framework of score-based differentiable causal discovery, aiming to infer the causal structure model that encodes both graph structure (i.e., DAG) and data mapping (i.e., structural equations). Three essential components comprise the most recent differentiable score-based DAG learner: score function, DAG constraint, and deep networks for gradient-based optimization. DAG constraint, a hard penalty, quantifies the DAG-ness of graph and its coefficient has to go to infinity to impose acyclicity, whereas, in most training processes, the DAG learner searches in directed graph space. While prevalent score functions, such as least square loss $[58,59]$ and maximum log-likelihood estimator [25], only evalute the goodness-of-fit, which describes how well the data fit the estimated structure equations. In other words, the majority of existing score functions neglect the graph structure and merely evaluate the data fitness using static metrics [45] for all the directed


[^0]:    ${ }^{a}$ An Zhang is the corresponding author.
    ${ }^{\dagger}$ Xiang Wang is also affiliated with the Institute of Artificial Intelligence, Institute of Dataspace, and Hefei Comprehensive National Science Center.

![img-0.jpeg](img-0.jpeg)

Figure 1: An illustrative example of the DAG learning progress is that NOTEARS may yield the same scores for different DAG-ness graphs across different optimization phases, each parameterized by $h(\mathbf{W})$. The values of $h(\mathbf{W})$ defined in Equation (3) quantify the extent of violations of acyclicity as the weighted matrix W deviates further from DAGs. Consequently, NOTEARSbased methods fail to quantify the intrinsic causal distance by conventional score function. In contrast, our method CASPER can dynamically perceive the DAG structure and score the models based on the underlying causal relationships, further guiding the DAG structure learning.
graphs, regardless of the DAG-ness degree. To ensure today's score functions appropriately evaluate the candidate directed graphs, these static metrics are implicitly defined in a fixed scoring space holding an inherent assumption, i.e., that the estimated directed graph is an acyclic graph throughout the training process. However, the differentiable optimization framework makes it simple to violate this underlying assumption. We conclude that measuring the static fitness of the structural equations regardless of DAG-ness fails to quantify the intrinsic distance between the estimated directed graph and the optimal DAG [21, 58]. This contributes to learning a suboptimal DAG, also leading to the lack of noise-robustness in DAG learning [21, 54].

In this paper, we conjecture that an ideal score function should not only successfully measure the data fitness but also take the graph structure into consideration. We further substantiate our claim with an illustrative example as shown in Figure 1. In this example, the estimated directed graph is forced to be more acyclic (i.e., the value of $h(\mathbf{W})$ drops) as the intensity of the DAG constraint grows in the training process. The scores of NOTEARS in phases 2 and 3, focusing solely on data fitness, are comparatively indiscriminate. Unfortunately, facing an exponentially increasing of DAG constraint coefficient, NOTEARS is likely to encounter ill-conditioning issues and slip into the local minimum in phase 2. In contrast, benefiting from taking graph structure into account, it is considerably easier for CASPER to pass phase 2, avoiding falling into a local optimal graph. Hence, such DAG-ness independent score fucntions hardly reveal the distance between the estimated and ground-truth DAG, being at odds with the true learning process under causal structure space.

Motivated by the limitation of DAG-ness independent score functions, we attempt to discover a simple form of score function encoding the graph structural information. We consider DAG structure learning in a dynamic space from a distributional view as opposed to using the static metrics of existing score functions. Specifically, the desirable score function, as the measure in this new
space, has causal semantics, indicating that by incorporating information from structural equation models, it can accurately reflect DAG-ness of candidate graphs. The DAG-ness-aware property of the new score function enables us to alleviate the local minimum issue and helps reconstruct a more precise DAG. As a result, the dynamical space can measure intrinsic causal relationships and data fitness from the perspective of distribution, which can further enhance the robustness of the DAG learner.

Guided by this idea, we propose a dynamic causal space for DAG structure learning, coined CASPER, which satisfies a series of good properties, including complete probability metric and noise-robustness. In this paper, firstly, we develop a descriptor that encapsulates the graph structural equation. By inserting the descriptor of the causal space, CASPER may dynamically adjust the complexity of the measure in accordance with DAG-ness in the optimization process. Secondly, we use the measure (also known as causal distance in our paper) defined in causal space as the primary component of the score function. As a result, we may adaptively perceive the DAG-ness of candidate graphs in the training process. Thirdly, we define the Boral probability measure in our causal space, which may accurately reflect the sampling distribution while remaining faithful to the DAG. Our causal space is therefore robust to the distortion caused by noise in observational data.

In summary, our contributions are highlighted as:

- To the best of our knowledge, we are among the first class to impose the DAG-ness-aware information into the framework of differentiable DAG structure learning.
- We propose a novel optimization scheme for DAG structure learning called CASPER. CASPER encodes the graph structure of the structural equation model using a dynamic causal space, allowing us to enhance the score function with adaptive attention to the causal structure.

- Extensive experiments both on synthetic and real-world datasets demonstrate our proposed method can significantly improve the performance of existing causal discovery models.


## 2 ALGORITHM

Prevailing algorithms for DAG structure learning can be broadly categorized into two research lines: constraint-based methods [19] and score-based methods [11, 52]. Constraint-based approaches always test for conditional independencies according to the empirical joint distribution under certain assumptions [20, 48], in order to construct a graph that reflects these conditional independencies. On the other hand, the score-based approaches evaluate the validity of a candidate graph $\mathcal{G}$ under some predefined score function [53]. In this paper, our focus is primarily on differentiable score-based algorithms. Before introducing our CASPER, we provide a brief overview of the fundamental concepts in DAG structure learning.

### 2.1 Problem Definition

DAG structure learning (i.e., causal discovery) aims to infer the Structural Equation Model (SEM) [12, 36] from the observational data, which models the data generating procedure. Formally, the basic DAG structure learning problem is formulated as follows: Let $\mathbf{X}=\left[\mathbf{x}_{\mathbf{1}} \mid \ldots \mid \mathbf{x}_{\mathbf{d}}\right] \in \mathbb{R}^{n \times d}$ be a data matrix consisting of $n$ i.i.d. observational data of $d$ variables. And $\mathcal{H}$ denotes the space of DAGs $\mathcal{G}=(\mathcal{V}, \mathcal{E})$ on $d$ nodes, where $\mathcal{V}$ represents the set of node variables, denoted as $X=\left(X_{1}, \ldots, X_{d}\right)$ and $\mathcal{E}$ is the set of causeeffect edges between variables. Given $\mathbf{X}$, we try to learn a directed acyclic graph (DAG) $\mathcal{G} \in \mathcal{H}$ for the joint distribution $P(X)$ [22, 48]. To model $X$, we consider a generalized structural equation model (SEM) as follows:

$$
X_{j}:=f_{j}\left(X_{p a\left(X_{j}\right)}\right)+N_{j}, \quad j \in\{1, \ldots d\}
$$

where $X_{j}$ is the $j$-th node variable, $p a\left(X_{j}\right)$ denote the parents of $X_{j}, f_{j}$ is the causal structure funntion, and $N_{j}$ refers to the additive noise with variance $\sigma_{j}^{2}$. Without loss of generality, the observed data $\mathbf{X}$ can be regarded as the samples from the joint distribution $P(X)$, our goal is to use the samples to reconstruct the underlying causal structure represented by DAG $\mathcal{G}$.

### 2.2 Preliminary

Structure Identifiability. Unraveling the identifiability of causal direction is a crucial issue in the process of DAG structure learning. In general, it is impossible to reconstruct $\mathcal{G}$ given only observational samples from $P(X)$ if we do not impose any assumptions on SEMs (i.e., Equation (1)). Considering a set of assumptions $\mathcal{A}$ over a causal graphical model $\mathcal{M}_{\mathcal{A}}=\left(P_{X}, \mathcal{G}\right)$, the graph $\mathcal{G}$ is identifiable from $P(X)$ if and only if there is no other $\overline{\mathcal{A}}_{\mathcal{A}}=\left(\hat{P}_{X}, \hat{\mathcal{G}}\right)$ satisfying the same $\mathcal{A}$ such that $\hat{\mathcal{G}} \neq \mathcal{G}$ and $\hat{P}(X)=P(X)$. To satisfy the identifiability of the graph, researchers [27, 37, 40] always assume that the conditional densities belong to a specific parametric family (e.g., additive noise models).

Score-based Structure Learning. The goal of conventional scorebased structure learning is stated as the following combinatorial optimization problem [39]:

$$
\begin{gathered}
\min _{\mathcal{G}} F(\mathbf{X} ; \mathcal{G})=\mathcal{L}_{\text {rec }}(\mathbf{X} ; \mathcal{G})+\lambda \mathcal{R}_{\text {sparse }}(\mathcal{G}) \\
\text { s.t. } \mathcal{G} \in \text { DAGs }
\end{gathered}
$$

where $F$ is a score function, $\mathbf{X}$ symbolizes the observational data and $\mathcal{G}$ refers to a directed graph. We notice that the score function $F(\mathbf{X} ; \mathcal{G})$ consists of two terms: (1) the measure of graph reconstruction, referred to as the proximity of the optimized graph to the true DAG; (2) the sparsity regularization term, represented as $\mathcal{R}_{\text {sparse }}(\mathcal{G})$, mandates that the count of edges in the graph be subject to a penalty, typically achieved through $l_{1}$ regularization in practice. The hyperparameter $\lambda$ plays a pivotal role in modulating the significance of the regularization process. Common score functions include the MDL [4], BIC [28] and BGe [23]. However, the Equation (2) is NP-hard to solve due to the nonconvex and combinatorial nature of the optimization problem [5, 8]. To address the combinatorial problem, Zheng et al. [58] convert it into a continuous program as:

$$
\min _{\mathcal{G}} F(\mathbf{X} ; \mathcal{G}) \quad \text { s.t. } \quad h(\mathcal{G})=0
$$

where $h(\mathcal{G})=0$ is a differentiable function over real matrices, whose level set at zero exactly means the acyclicity of a graph. Note that, there are various alternatives of $h(\mathcal{G})[24,53,54,58]$ in literature. Therefore, we went from the combinatorial optimization problem to a continuous constrained optimization problem. Fortunately, numerous solutions (e.g., augmented Lagrangian method [2, 30]) can be applied to solve the Equation (3). As a result, the optimization problem in Equation (3) can be further reformulated as:

$$
\min _{\mathcal{G}} F(\mathbf{X} ; \mathcal{G})+\mathcal{L}_{\mathrm{DAG}}\left(\mathcal{G}, \alpha_{t}, \mu_{t}\right)
$$

where $\mathcal{L}_{\mathrm{DAG}}=\alpha_{t} h(\mathcal{G})+\frac{\mu_{t}}{2}|h(\mathcal{G})|^{2}$ is the penalty term in Lagrangian method. $\alpha_{t}$ and $\mu_{t}>0$ are the penalty coefficients of the $t_{t h}$ subproblem respectively. Existing differentiable approaches always predefine a static $F(\mathbf{X} ; \mathcal{G})$ to measure SEMs in a fixed space (e.g., penalized least-square loss in a fixed Euclidean Space [32, 58, 59] and Evidence Lower Bound (ELBO) in a fixed asymmetry probability space [54]) without considering graph itself. Considering that the score function aims to measure the goodness of a causal structure, a sufficient score function should include three parts: in addition to the first two terms in Equation (2) that have been well studied $[13,60]$ but DAG-ness independent, a descriptor which encodes the structure's own information in $F$ is required.

### 2.3 Proposed Model

In this section, we will introduce the details of our model CASPER, which defines a DAG-ness aware score function in a dynamic causal metric space and reshape the optimization scheme for differentiable DAG structure learning. This allows the gradients of the loss function to be optimized towards the direction of more accurate causal graph reconstruction. For clarity, we first present the definition of our causal space and its desirable properties. Afterward, we describe the approach of applying it to DAG structure learning.

Dynamic Causal Space. Most of the standard score-based differentiable algorithms tend to apply the same score on different causal structures (see the example in Figure 1), leading to suboptimal

graph construction when using observational data. As a result, the DAG learners are error-prone to constructing spurious edges due to DAG-ness independent forms and model vulnerability [17, 21]. To address these problems, our goal is to discover a novel form of score function, predefined in a specific metric space (i.e., causal space), which encodes the DAG-ness information into the score function for DAG-ness-aware causal structure learning. We introduce the CASPER framework, as shown in Figure 2, which aims to adaptively perceive the causal structure and facilitate more accurate gradient optimization. Before formally introducing the causal space, we first present the following lemma and definition of the Lipshitz norm for convenience in later notations. Let $\mathbf{W} \in\{0,1\}^{d \times d}$ denote the $\mathcal{G}$ 's adjacency matrix. Specifically, $\mathbf{W}_{i j}=1$ if the directed edge $X_{j} \rightarrow X_{i}$ exists in $\mathcal{G}$, otherwise $\mathbf{W}_{i j}=0$. The DAG lemma is formulated as:

Lemma 2.1. A matrix $\mathbf{W} \in \mathbb{R}^{d \times d}$ is a DAG if and only if

$$
h(\mathcal{G})=\operatorname{tr}\left(e^{\mathbf{W} \circ \mathbf{W}}\right)-d=0
$$

where $\circ$ is the Hadamard product.
Lemma 2.1 [58] uses the trace of matrix exponential with Hadamard product of $\mathbf{W}$ to quantify the DAG-ness. To ease the numerical difficulty of computing $\operatorname{tr}\left(e^{\mathbf{W} \circ \mathbf{W}}\right)$, Yu et al. [54] adopt a more convenient form of $h$ function:

$$
h(\mathcal{G})=\operatorname{tr}\left[\left(I+\alpha(\mathbf{W} \circ \mathbf{W})^{d}\right)\right]-d, \quad \alpha>0
$$

Definition 2.2 (Lipshitz norm). Let $\mathcal{M}_{A}$ and $\mathcal{M}_{B}$ be metric spaces. Let $\mathcal{T}: \mathcal{M}_{A} \rightarrow \mathcal{M}_{B}$ be a mapping function. The Lipshitz norm or Lipshitz modulus $\|\mathcal{T}\|_{\text {Lip }}$ of $\mathcal{T}$ is the supremum of the absolute difference quotients, i.e.,

$$
\|\mathcal{T}\|_{\text {Lip }}:=\sup _{a \neq b, a, b \in \mathcal{M}_{A}} \frac{|\mathcal{T}(a)-\mathcal{T}(b)|}{\|a-b\|}
$$

And we call the map $\mathcal{T}: \mathcal{M}_{A} \rightarrow \mathcal{M}_{B}$ Lipshitz continuous or imply Lipshitz if its Lipshitz norm is finite.

Guided by the aforementioned idea, we now formally give the definition of our dynamic causal space.

Definition 2.3 (Causal Space). Let $(\mathcal{S}, \mathcal{D})$ be a Polish space (complete metric space) for which Borel probability measure on $\mathcal{S}$ is a Radon measure. Let $\mathcal{P}(\mathcal{S})$ denote the collection of all probability measures $v$ on $\mathcal{S}$ with finite moment, that is, for any $z \in \mathcal{S}$, there exists some $z_{0}$ in $\mathcal{S}$ such that:

$$
\int_{\mathcal{S}} \mathcal{D}\left(z, z_{0}\right) d v(z)<\infty
$$

For any $z_{X}, z_{Y} \in \mathcal{S}$ and let $P$ and $Q$ be the distribution of $z_{X}$ and $z_{Y}$. The distance in the space $\mathcal{S}$ between two probability measures $P$ and $Q$ in $\mathcal{P}(\mathcal{S})$ is defined as:
$\mathcal{D}_{\mathcal{S}}^{\mathcal{T}}(P, Q)=\sup _{\|\mathcal{T}\|_{L i p} \leq g(h(\mathcal{G}))}\left\{\mathbb{E}_{z_{X} \sim P}\left[\mathcal{T}\left(z_{X}\right)\right]-\mathbb{E}_{z_{Y} \sim Q}\left[\mathcal{T}\left(z_{Y}\right)\right]\right\}$,
where $g$ is an increasing function, $h(\mathcal{G})$ is the DAG-ness function as explained in the part of Lemma 2.1. $\mathcal{T}$ is a continuous mapping function $\mathcal{T}: \mathcal{S} \rightarrow \mathbb{R}$ and $\|\cdot\|_{\text {Lip }}$ is the Lipshitz norm. We call $\mathcal{S}$ causal space and $g(h(\mathcal{G}))$ structure-aware descriptor, which encodes the DAG-ness of the causal graph in causal space. And the
distance $\mathcal{D}_{\mathcal{S}}^{\mathcal{T}}$ is called causal structure distance which defined in $\mathcal{S}$ with mapping function $\mathcal{T}$.

Furthermore, our dynamic causal space has the following desirable properties:
(a) The causal space $\mathcal{S}$ is a complete probability metric space that allows us to learn a DAG structure from a distributional view.
(b) DAG-ness information of a causal graph can be dynamically quantified by the smoothness of causal space through the process of structure learning.
(c) This space is noise-robust enough to observational data under "perturbation" (i.e., additive noise).
Due to space limitations, we provide a detailed analysis and performance evaluation of these properties in the experiments presented in Section 3. Here, we offer some illustrative discussions regarding properties (a) to (c). Property (a) implies that the causal structure distance defined in our causal space satisfies the axioms of a distance on Borel probability. This property allows us to capture the observational sampling distribution more faithfully to the DAG, particularly in real data, as demonstrated in our experiments. Property (b) enables us to incorporate DAG-ness information into the score function during the optimization process, leading to more precise DAG solutions. This property enhances the optimization process and improves the accuracy of the resulting DAG. Property (c) enhances the robustness of our model in handling heterogeneous data. Although there exists methods [25, 54] that achieve property (a) by measuring the SEMs from a static probabilistic view, they hardly satisfy (b) and (c). These methods overlook the importance of dynamical structure information in the optimization and robustness of their models. Fortunately, our proposed dynamic causal space provides a comprehensive solution that satisfies all of the above properties.

Learning DAG Structure in Causal Space. Given the definition of causal space, we consider it a crucial criterion for differentiable score-based structure learning. Before delving into the learning process of DAG structures in the causal space, we provide the following characterization to guarantee the convergence of the structure learning process.

Proposition 2.4 (Convergence of Causal Space). Let $P$ be a distribution on our causal space $\mathcal{S}$ and $\left\{P_{n}\right\}_{n \in \mathbb{P}}$ be a sequence of distributions on $\mathcal{S}$. Then, considering limits as $n \rightarrow \infty, P_{n} \xrightarrow{\text { distribution }} P$ if and only if $\mathcal{D}\left(P_{n}, P\right) \rightarrow 0$ in $\mathcal{S}$, where $\xrightarrow{\text { distribution }}$ represents convergence in distribution for random variables.

Proof. Let us start from a sequence $\left\{P_{n}\right\}$ such that $\mathcal{D}\left(P_{n}, P\right) \rightarrow$ 0 . Based on the definition 2.3 of Causal Space, for every $\mathcal{T} \in$ $\operatorname{Lip}_{g(h(\mathcal{G}))}$, we have $\int \mathcal{T}\left(P_{n}-P\right) \rightarrow 0$. And the same is true for any Lipshitz function. Then, we fix a subsequence $\left\{P_{n_{k}}\right\}$ that satisfies $\lim _{k} \mathcal{D}\left(P_{n_{k}}\right)=\lim \sup _{n} \mathcal{D}\left(P_{n}, P\right)$. For each $k$, we pick a function $\mathcal{T}_{n_{k}} \in \operatorname{Lip}_{g(h(\mathcal{G}))}$ such that $\int \mathcal{T}_{n_{k}}\left(P_{n_{k}}-P\right)=\mathcal{D}\left(P_{n_{k}}, P\right)$. Up to adding a constant, which does not affect the integral, we can assume that the $\mathcal{T}_{n_{k}}$ all vanish at the same point, and they are hence bounded and equicontinuous. By Arzela-Ascoli theorem [14], we can extract a sub-sequence uniformly converging to a certain

![img-1.jpeg](img-1.jpeg)

Figure 2: Pipeline of Dynamic Causal Space for DAG Structure Learning (CASPER). Given observational data $X$, we apply the causal space mapper $\mathcal{T}_{\phi}$ to encode data into causal space. Then we use the DAG-fitting model $f_{\theta}$ to optimize the causal graph with sparsity and DAG constraint. Finally, the DAG-ness information can be transmitted to the causal space through the structure-aware descriptor $g$. Thus the causal space is able to dynamically capture structural information and provide more accurate solutions.

```
Algorithm 1 CASPER Algorithm for DAG Structure Learning
    Input: observational data \(\mathbf{X}=\left\{\mathbf{x}^{(k)}\right\}_{k=1}^{n}\) sampled from \(P_{r}\) and
    threshold \(\omega>0\), maximum epoch in the inner loop \(K_{\text {inner }}\), maxi-
    mum epoch in the outer loop \(K_{\text {outer }}\)
    Initialize: initialize the parameters of causal fitting model \(\theta\) and
    parameters of causal space model \(\phi\)
    for \(t=0\) to \(\tau_{0}\) do
        Update \(\theta\) and \(\mathcal{G}\) to minimize \(F_{\phi}\) and get \(\mathcal{G}^{\text {pre }}\)
    end for
    for \(k_{1}=0\) to \(K_{\text {outer }}\) do
        Fix causal space model parameters \(\phi\)
        Calculate \(F_{\phi}(\mathbf{X} ; \mathcal{G}, \theta)+\mathcal{L}_{\text {DAG }}(\mathcal{G})\) in Equation 12
        Update \(\theta\) and \(\mathcal{G}\) to minimize \(F_{\phi}+\mathcal{L}_{\text {DAG }}\)
        for \(k_{2}=0\) to \(K_{\text {inner }}\) do
            Fix graph \(\mathcal{G}\) and the causal fitting model's parameters \(\theta\)
            Update \(\phi\) to maximize \(F_{\phi}(\mathbf{X} ; \mathcal{G}, \theta)\) in Equation 11
            \(c \leftarrow \log (1+h(\mathcal{G}))\)
            \(\phi \leftarrow \operatorname{clip}(\phi,-c, c)\)
            end for
    end for
    Prune the edges less than \(\omega\) of \(\mathcal{G}\)
    return predicted \(\mathcal{G}\)
```

$\mathcal{T} \in \operatorname{Lip}_{g(h(\mathcal{G}))}$. By replacing the original subsequence with this new one, we now have:

$$
\mathcal{D}\left(P_{n_{k}}, P\right)=\int \mathcal{T}_{n_{k}} d\left(P_{n_{k}}-P\right) \rightarrow \int \mathcal{T} d(P-P)=0
$$

where the convergence of the integral is justified by the distributional convergence $P_{n_{k}} \rightarrow P$ together with the strong convergence in continuous function $\mathcal{T}_{n_{k}} \rightarrow \mathcal{T}$. It shows that $\lim \sup _{n} \mathcal{D}\left(P_{n}, P\right) \rightarrow$ 0 and concludes the proof.

Proposition 2.4 provides a good demonstration of the convergence in the causal space we proposed, which leads to theoretical guarantees for our optimization process.

Formally, we cast the overall framework of CASPER to learn DAG structure in the causal space and boost causal discovery. Given observational data $\mathbf{X}$ sampled from $P_{r}$, the DAG-ness-aware score function defined in causal space $\mathcal{S}$ is:
$F_{\phi}(\mathbf{X} ; \mathcal{G}, \theta)=\left\{\mathbb{E}_{\mathbf{X} \sim P_{r}}\left[\left(\mathcal{T}_{\phi}(\mathbf{X})\right)\right]-\mathbb{E}_{\hat{\mathbf{X}} \sim P_{\theta}}\left[\left(\mathcal{T}_{\phi}(\hat{\mathbf{X}})\right)\right]+\lambda \mathcal{R}_{\text {sparse }}(\mathcal{G})\right.$,
where $\mathcal{T}_{\phi}$ is the causal space mapping function parameterized by $\phi$ and $\mathcal{R}_{\text {sparse }}(\mathcal{G})$ is the graph sparsity regularization term by $l_{1}$ norm in practice. $\hat{\mathbf{X}}$ is recovered through the data generative process of $\mathbf{X}$ by learnable DAG-fitting model $f$ with parameter set $\theta$, i.e., $\hat{\mathbf{X}}=f(\mathbf{X} ; \theta)$. Then we cast the overall framework of CASPER to learn DAG structure as the following bilevel optimization problem:

$$
\begin{aligned}
& \min _{\mathcal{G}, \theta} F_{\phi^{*}}(\mathbf{X} ; \mathcal{G}, \theta)+\mathcal{L}_{\mathrm{DAG}}\left(\mathcal{G}, \alpha_{I}, \mu_{I}\right) \\
& \text { s.t. } \quad \phi^{*} \in \underset{\phi \in C(\mathcal{G})}{\arg \max } F_{\phi}(\mathbf{X} ; \mathcal{G}, \theta)
\end{aligned}
$$

where $C(\mathcal{G}):=\left\{\phi: \mathcal{T}_{\phi}\right.$ is continuous, $\left\|\mathcal{T}_{\phi}\right\|_{\text {Lip }} \leq g(h(\mathcal{G}))\}$ and $g(\cdot)$ is an increasing function which is $g(x)=\log (1+x)$ for implementation. More specifically, Equation (12) consists of two terms, where the inner-level objective (i.e., optimize $\phi$ by maximizing $F_{\phi}$ to compute the causal structure distance in causal space) is nested within the outer-level objective (i.e., optimize $\mathcal{G}$ and $\theta$ by minimizing the score function). We notice that solving the outer-level problem should be subject to the optimal value of the inner-level problem. For better convergence, we can pretrain the $\mathcal{G}$ and $\theta$ according to $F_{\phi}$ for a few epochs at first.

Now we introduce how to solve the bilevel optimization in Equation (12) in detail. In the inner loop, we fix the DAG-fitting model which predicts the data generative process of $\mathbf{X}$ and then update $\phi$ to maximize the score function $F_{\phi}$ to compute the causal structure distance in causal space $\mathcal{S}$. In the outer loop, upon the parameters

Table 1: Linear Setting, for ER graphs of 10, 20, 50 nodes.


of causal space mapping function $\phi$ is determined in the inner loop, we minimize the score function to optimize the DAG-fitting model. By alternately training the inner and outer loops, the score function can adaptively aware the causal structure in causal space, thus leading to more accurate gradient optimization and faster convergence to the optimal solution. Our CASPER algorithm is summarized in the Algorithm 1.

## 3 EXPERIMENTS

In this section, we conduct extensive experiments to answer the research questions:

- RQ1: How does CASPER perform compared to the previous methods in both linear and nonlinear settings?
- RQ2: How do CASPER and other baselines perform with various factors (i.e., noise scales, graph density)?
- RQ2: How does CASPER perform on real heterogeneous data compared with other applicable baselines?


### 3.1 Experimental Settings

Baselines. To answer the first and second question (RQ1 \& RQ2), we select six state-of-the-art causal discovery methods as baselines for comparison:

- NOTEARS [58] is specifically designed for linear settings and estimates the true causal graph by minimizing the fixed reconstruction loss with the continuous acyclicity constraint.
- NOTEARS-MLP [59] is an extension of NOTEARS [58] for nonlinear settings, which aims to approximate the generative structural equation model (i.e., Equation (1)) by MLP while only utilizing the continuous acyclicity constraint to the first layer of the MLP.
- DAG-GNN [54] reformulates DAG structure learning with variational autoencoder, where both encoder and decoder are graph neural networks. By selecting the evidence lower bound as the score function, DAG-GNN is capable of effectively recovering the causal structure.
- NoCurl [55] utilizes a two-step procedure: initialize a cyclic solution first and then employ Hodge decomposition of graphs
and learn a DAG structure by projecting the cyclic graph to the gradient of a potential function.
- GraN-DAG [25] adapts the constrained optimization formulation to allow for nonlinear relationships also by neural networks and makes use of the final pruning step to remove spurious edges.
- DARING [17] introduces an adversarial learning strategy to impose an explicit residual independence constraint, aiming to improve the learning of acyclic graphs.
To comprehensively demonstrate the effectiveness of our proposed CASPER, extensive experiments are conducted with more baselines on the real heterogeneous data (RQ3). In addition to the baselines mentioned above, we further implement CD-NOD [19], FGS [42], ICA-LINGAM [46] GOLEM [31], and GES [6] in the real-world benchmark dataset, i.e., Sachs [43].

Hyperparameter Settings. For linear settings, there are two main hyper-parameters, the sparsity coefficient $\lambda_{1}$ for the $l_{1}$-norm regularization term; $K_{\text {inner }}$ in Algorithm 1 for inner loops as we choose the same stop condition as NOTEARS [58] to replace $K_{\text {outer }}$ for the parameter-free. We tune $\lambda_{1}$ in $\{0.002,0.005,0.01,0.015,0.02$, $0.03,0.09,0.1,0.25\}$ and tune $K_{\text {inner }}$ in $\{1,2,3,4,5,6,7,8,9,10\}$. For nonlinear settings, there are three main hyper-parameters in total: $\lambda_{1}, \lambda_{2}, K_{\text {inner }}$, among which $\lambda_{1}$ and $\lambda_{2}$ are for the $l_{1}$-norm and $l_{2}$-norm regularization terms respectively. And we follow the same tuning strategy in linear settings to tune the three hyper-parameters. We find that often $\lambda=0.01, K_{\text {inner }}=3$ wor well. In practice, we adopt multilayer perception (MLP) with parameters $\theta$ and $\phi$ to approximate $f_{\theta}$ and $\mathcal{T}_{\phi}$. More details of the network design will be open-sourced upon acceptance. As the training process is the augmented Lagrangian problem, we follow the same optimization of Lagrangian coefficients as NOTEARS for a fair comparison. Besides, following the convention in NOTEARS-based methods [17, 58, 59], we adopt the same post-processing strategy for all the methods, cutting off the edges with values less than 0.3 .

Evaluation Metrics. To evaluate the DAG structure learning, four metrics are reported: True Positive Rate (TPR), False Discovery Rate (FDR), Structural Hamming Distance (SHD), and Structural

Table 2: Nonlinear Setting, for ER graphs of 10, 20, 50 nodes.


Intervention Distance (SID) [38], averaged over ten random trails. The SHD simply counts the number of missing, falsely detected, or reversed edges. And the SID is especially well suited for causal inference since it counts the number of couples $(i, j)$ such that the interventional distribution $p\left(x_{j} \mid d o\left(X_{t}=\bar{x}\right)\right)$ would be miscalculated if we use the estimated graph to form the parent adjustment set. Higher TPR stands for better performance, while FDR, SHD, and SID should be lower to represent a better estimate of the target causal graph.

### 3.2 Overall Performance Comparison (RQ1)

Simulations. Following the convention of causal discovery, the generating data differs along three dimensions: the number of nodes, the degree of edge sparsity, and the graph type. We consider two well-known graph sampling models, namely Erdos-Renyi (ER) and scale-free (SF) [1] with $k d$ expected edges (denoted as ER $k$ or $S F k$ ) and $d=\{10,20,50\}$ nodes. Specifically, in linear settings, similar to Zheng et al. [58] and Gao et al. [10], the coefficients are assigned following Uniform distribution $U(-2,-0.5) \cup U(0.5,2)$ with additive standard Gaussian noise. In nonlinear settings, same as Zheng et al. [59], we generate the ground truth structural equation model (SEM) in Equation (1) under the Gaussian process with radial basis function (RBF) kernel of bandwidth one, where $f_{f}(\cdot)$ is the additive noise model with $N_{f}$ as an i.i.d. random variable following the standard normal distribution. Notice that both of these settings are known to be fully identifiable [37, 40]. In this experiment, we explore the improvements when introducing both linear and nonlinear settings by comparing the DAG estimations against the ground truth structure. We simulate \{ER2, ER4, SF2, SF4\} graphs following ER or SF scheme with $d=\{10,20,50\}$ nodes. For each graph, 10 datasets of 2,000 samples are generated and the mean and standard deviations (std) of the above metrics are reported for a fair comparison.

Results. Table 1, Table 2, and Tables in the Appendix demonstrate the comparison of overall performance on both linear and nonlinear synthetic data. Notice that the best-performing methods are bold
and the error bars report the standard deviation across datasets over ten trials. We observe that:

- Our method CASPER significantly outperforms the state-of-the-art baselines across all datasets. Specifically, our proposed model, i.e., dynamic causal space can achieve consistent improvements in terms of SHD and SID, revealing a lower number of missing, falsely detected, reversed edges and a better estimation of the ground truth graph. We attribute the improvements to the dynamic and DAG-ness-aware causal space, which enhances the score function with adaptive attention to the causal graph and boosts the quality of score-based DAG structure learning. With a closer look at the TPR and FDR, CASPER typically lowers FDR by eliminating spurious edges and increases TPR by actively identifying more correct edges. This clearly demonstrates that CASPER effectively helps reach a more accurate gradient optimization through the structure distance in causal space, thus extracting better causal relationships.
- As the performance comparison among different graphs shows, the score-based methods suffer from a severe performance drop under high-dimensional graph data. Despite the previous methods working well in linear and low-dimensional data, they fail to scale to more than 50 nodes in ER4 and SF4 graphs. Taking NOTEARS-MLP as an example, although it can achieve $83 \%$ TPR in 10 nodes (ER4) of nonlinear settings, it suffers dramatic degradation, i.e., only $28 \%$ TPR in the 50 nodes (ER4) graph, which is mainly due to difficulties in enforcing acyclicity in high-dimensional dense graph data [26, 51]. However, our CASPER optimization model still performs well with TPR higher than $50 \%$, which shows the great potential of learning high dimensional and dense DAG structures under a DAG-ness aware optimization framework.


### 3.3 Study of Various Factors (RQ2)

Motivations. In real-world applications, it is common to encounter graphs with various noise scales or different densities, where the underlying causal structure is invariant. We conjecture that a robust DAG structure learning framework is able to successfully estimate

the graphs under various factors (i.e., , noise scales and graph density). In this section, we discuss various factors that may affect the performance of CASPER and other methods.

Simulations. We choose SF graphs with $d=20$ for the two case studies. Specifically, for different noise scales in both linear and nonlinear settings, we set the distribution of the noises as $N(\mu, 1), \mu \in\{0.2,0.4,0.6,0.8,1\}$ in SEMs of Equation (1) and choose SF2 graph to generate data. Following the settings in Section 3.2, we set more graphs with various densities (i.e., degree of nodes) from $\{2,4,6,8,10,12\}$. For instance, the node degree $=10$ means there are 200 edges in total when generating the SF graph.

Results. Figure 3 shows the evaluations with various noise scales and Figure 4 reports the performance comparison with different density. Both empirical results of them are conducted on linear nonlinear synthetic SF datasets. Different colors separately refer to the state-of-the-art methods and our method in SHD performance. We find that:
![img-2.jpeg](img-2.jpeg)
(a) Linear Setting
![img-3.jpeg](img-3.jpeg)
(b) Nonlinear Setting

Figure 3: SHD comparisons for various noise scales in SF2 graph with 20 nodes.

- Compared with baselines, CASPER is noise-robust enough to observational data under various additive noise conditions. Specifically, CASPER outperforms other methods consistently across all noise scale settings of SF graphs. We notice that other baselines are struggling from performance degradation when noise increases. We ascribe this hurdle to the static metric of score functions which is DAG-ness independent. In contrast, benefiting from DAG-ness aware score functions, our CASPER not only effectively captures the information from noise environments but also improves the DAG structure learning ability under perturbations.
- As the performance comparison among density factors shows, our CASPER can better adapt to graphs with different degrees. Although the baselines have the sparsity penalty to control the importance of graph density in regularization form, they do not perform well as our CASPER due to unawareness of causal structure in the score function. With a closer look at the evaluation curve of different densities, as the node degree increases, the improvements of CASPER over baselines get larger, which means CASPER could better adapt to the denser settings with adaptive structure attention.
![img-4.jpeg](img-4.jpeg)

Figure 4: SHD comparisons for different graph density conditions in SF graph with 20 nodes.

### 3.4 Evaluation on Real Data (RQ3)

Motivations. Heterogeneous data is a challenging yet frequently occurring issue in real-world observational data. Despite the variety of noise distribution, the underlying causal generating process always keeps stable in heterogeneous data. Specific DAG structure learners designed for heterogeneous data are prone to require prior knowledge of group annotations of each sample under strict conditions. However, group annotations are extremely costly and hard to collect and label.

Table 3: Empiricle results on Sachs [43] dataset.


Dataset. Sachs [43], a real bioinformatics dataset, is for the discovery of the protein signaling network on expression levels of different proteins and phospholipids in human cells and is a popular benchmark for DAG structure learning, containing both observational and interventional data. Specifically, in Sachs, nine different perturbation conditions are imposed on sets of individual cells, each of which administers certain reagents to the cells. With the annotations of perturbation conditions, Sachs [43] is considered as the real-world heterogeneous dataset [29]. The true graph from [43] containing 11 nodes and 17 edges on 7,466 samples is widely used for research on graphical models, with experimental annotations accepted by the biological research community.

Results. In this benchmark dataset, we compare with recent continuous score-based methods, including NOTEARS [58], NOTEARSMLP [59], DAG-GNN [54], NoCurl [55], GraN-DAG [25], DARING [17] and GOLEM [31], traditional structural causal models ICALiNGAM [46], and combinational methods GES [6] and FGS [42].

Because the true causal graph in Sachs is sparse that a purely empty graph can reach as low as 17 in SHD, we report the \#total predicted edges, \#correct edges, SHD and SID in Table 3.

As Table 3 illustrates, CASPER drives great performance breakthroughs and outperforms all other methods in correct discovery of the ground truth on real heterogeneous data. Specifically, most previous methods (e.g., NOTEARS-based, GOLEM) suffer from notorious performance drops when the homogeneity assumption is unsatisfied, and pose hurdles from being scaled up to real-world large-scale applications. In stark contrast, benefiting from DAGness aware attention to the causal graph, CASPER achieves lower SHD as well as SID and improves the predicted correct edges, which accomplishes more profound causation understanding, leading to higher DAG structure learning quality. This validates that the potential of CASPER as a promising research direction for enhancing robustness and generalization for DAG structure learning when encountering various real-world data.

## 4 RELATED WORK

DAG structure learning has recently taken the field of machine learning by storm [44]. A DAG $\mathcal{G}$ and a joint distribution are faithful to each other if and only if the conditional independencies true in the joint distribution are entailed by $\mathcal{G}$ [34]. This principle of faithfulness enables one to recover $\mathcal{G}$ from the joint distribution. Given i.i.d. samples $\mathbf{X}$ from an unknown distribution corresponding to a faithful but unknown causal graph, DAG structure learning refers to recovering the causal graph from $\mathbf{X}$. In this section, we review the works of some related fields with this work.

Generally speaking, there are two primary classes of algorithms employed for DAG structure learning (i.e., causal discovery): constraintbased methods and score-based methods. Our CASPER falls into the second class.

Constraint-based causal discovery methods first apply conditional independence tests to identify the causal skeleton under a faithfulness assumption. Then they establish the orientations of edges up to the Markov equivalence class, which usually contains structurally diverse DAGs with potentially unoriented edges. Examples include [50, 57] that use kernel-based conditional independence criteria and the well-known PC algorithm [48] which implements the independence tests when no unobserved confounder exists. In scenarios involving unobserved confounders, the fast causal inference algorithm (FCI) [49] also calls independence judgement like PC, but targets an extended causal graph with bi-directed edges. However, these methods are not robust as small errors in building the graph skeleton or are limited by sample size, thus leading to notorious performance degradation in the inferred Markov equivalence class. To alleviate the drawbacks, some score-based methods [6, 42] have been proposed as an alternative solution.

Score-based methods [22, 39] cast the problem of structure learning as an optimization problem over the space of DAGs. Many popular methods tackle the combinatorial nature of the problem by performing the form of greedy search. The Greedy Equivalence Search (GES) [6] and its extension FGS [42] utilizes a score function called BDeu to measure the correctness of the conditional independence of the target graph. The discrete algorithm starts with an empty graph and adopts a greedy strategy to change edges until
the convergence of the score. In contrast to the methods that only identify the Markov equivalence class, SEMs, a class of score-based methods, can determine the true causal graph from the same equivalence class under additional assumptions. For instance, PNL [56] demonstrates its definite identifiability in two-variable settings except 5 special cases by examing if the disturbance is independent. On the other hand, conventional approaches, such as LiNGAM [46], combinatorially search for the DAG structure for multiple variables by converting the topological ordering of the causality diagram into the lower triangular matrix.

However, learning the DAG structure from purely observational data remains a challenge mainly due to the intractable combinatorial nature of acyclic graph space [5, 7, 8]. Fortunately, a recent breakthrough, NOTEARS proposed in Zheng et al. [58], reformulates the discrete DAG constraint into a continuous equality constraint, resulting in a differentiable score-based optimization problem. Further, there are various subsequent works after NOTEARS. DAG-GNN [54] proposes a variant of gradient-optimized formulation in autoencoder architecture; NOTEARS-MLP [59] and GraNDAG [25] extend the NOTEARS framework to deal with more nonlinear functions using neural networks; RL-BIC [60] introduces reinforcement learning (RL) to search for the DAG; GOLEM [31] utilizes a likelihood-based objective with soft sparsity and DAG constraints instead of constrained optimization. In addition to single domain exploration, some researchers [18, 19] study causal discovery on multi-domain (i.e., heterogeneous data where the underlying causal generating process remains stable but the noise distributions may vary). In this paper, we mainly focus on differentiable scorebased DAG structure learning.

## 5 CONCLUSION

Despite the great success of causal structure learning on synthetic data, today's differentiable causal discovery methods are still far from being able to recover the target causal structures in various real-world applications. In this paper, we proposed CASPER, an effective optimization framework that boosts the DAG structure learning in a dynamic causal space, which adaptively perceives the graph structure during the training process. Grounded by empirical visualization studies, CASPER is noise-robust to observational data under perturbation. Extensive experiments demonstrate that the remarkable improvement of CASPER on a variety of synthetic and real heterogeneous datasets indeed comes from the DAG-ness aware score function.

One limitation of CASPER is that our framework is built on differentiable score-based causal discovery. In the future study, we will explore similar DAG-ness-aware strategies in more general structure learning frameworks. We believe that our CASPER provides a promising research direction to diagnose the performance degradation for nonlinear and noise data in DAG structure learning, and will inspire more valuable works for learning accurate causal graphs from observational data.

## ACKNOWLEDGMENTS

This research is supported by the National Natural Science Foundation of China (9227010114) and the University Synergy Innovation Program of Anhui Province (GXXT-2022-040).

## A APPENDIX

## A. 1 Additional Experiments

More experimental results on both the linear and nonlinear synthetic data are reported in Appendix as Table 5 and 6 shows.

In order to further show the efficiency of our algorithm CASPER, we conduct additional experiments as Table 7, 8, and 9 shows. As the both synthetic and real data show, our CASPER only adds a negligible amount of computational time cost but achieves significant performance improvement compared to NOTEARS-based methods.

## A. 2 More Discussion

Discussion of dynamic causal space: The current score function, a measure to evaluate candidate-directed graphs in structure learning, solely takes into account the data fitness while neglecting the graph structure. However, there is an implicit assumption for the score function to appropriately evaluate, the estimated directed graph must be an acyclic graph throughout the training phase, which is not achievable. We, therefore, believe that the nextgeneration score function for structure learning should account for both data fitness and graph structure.

In mathematics, a "metric space" is a set with a notion of distance between its elements. The distance is measured by a function called the metric or distance function. In structure learning, the space is equipped with a set of directed graphs and the notion of distance between candidate graphs is the predefined score function. Since our metric (causal distance) is dynamically changed according to the directed graphs, we defined it as "dynamic causal space" (Definition 2.3 in the paper). We would like to highlight here that defining a dynamic measure by incorporating knowledge of time,
geometry, and data-related information has been explored in many other fields $[9,15,16]$.

The "dynamic causal space" proposed in this paper is one of the potential solutions that fuse structural information (DAG-ness) into score function. Here "dynamic" signifies the incorporation of different Lipshitz constants in the score function, which causes the goodness-of-fit to vary as the DAGness changes. By doing this, we may dynamically adjust the metric (causal distance in our paper) in the graph spaces as opposed to using a "static" measure neglecting the DAG-ness of the graph. Let us consider a simple scenario: If the initial graph's DAG-ness is poor (i.e., $\mathrm{h}(\mathrm{G})$ in our paper is high), we employ a more complex function (with a larger Lipshitz norm) to measure its distance to the true graph. As the optimization progresses and the graph's DAG-ness improves, we switch to simpler functions (with a smaller Lipshitz norm) for measuring the distance. This adaptive adjustment allows us to better optimize the graph and avoid local optima. Notably, if the initial graph is already the true graph, the Lipshitz constant would be zero.
Discussion of motivation example: Considering the experiments on linear models in Figure 1, we would like to emphasize that our intention was not to carefully design a linear case to create such a difficult situation for NOTEARS [58]. In contrast, we aim to demonstrate that even in relatively simple cases, the static measure (least square in NOTEARS [58]) might not perform well. To show our motivation thoroughly, we have also conducted a nonlinear case in Table 4. The true graph is generated from: $A:=\epsilon_{A}(\sim U(-1,1)), B:=2 \sin (A)+\epsilon_{B}(\sim N(0,2)), C:=$ $\cos (A)+0.5 \sin (B)+\epsilon C(\sim N(-1,1)), D:=0.5 C+\epsilon D(\sim U(0,1))$. We also capture the three phases in the optimization process.

Table 4: Nonlinear model experiments for Figure 1.


Table 5: Linear Setting, for SF graphs of 10, 20, 50 nodes.


Table 6: Nonlinear Setting, for SF graphs of 10, 20, 50 nodes.


Table 7: Empirical results for running time (sec comparison) on ER2 graph of 10 nodes (Linear setting).


Table 8: Empirical results for running time (sec comparison) on ER2 graph of 10 nodes (Nonlinear setting).


Table 9: Empirical results for running time (sec) comparison on Sachs [43] dataset.
