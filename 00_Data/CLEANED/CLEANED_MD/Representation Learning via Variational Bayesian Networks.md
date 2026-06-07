# Representation Learning via Variational Bayesian Networks 

Oren Barkan*<br>The Open University<br>Israel<br>Ori Katz<br>Technion<br>Israel

Avi Caciularu*<br>Bar-Ilan University<br>Israel<br>Jonathan Weill<br>Tel Aviv Univeristy<br>Israel<br>Noam Koenigstein<br>Tel Aviv University<br>Israel

## ABSTRACT

We present Variational Bayesian Network (VBN) - a novel Bayesian entity representation learning model that utilizes hierarchical and relational side information and is particularly useful for modeling entities in the "long-tail", where the data is scarce. VBN provides better modeling for long-tail entities via two complementary mechanisms: First, VBN employs informative hierarchical priors that enable information propagation between entities sharing common ancestors. Additionally, VBN models explicit relations between entities that enforce complementary structure and consistency, guiding the learned representations towards a more meaningful arrangement in space. Second, VBN represents entities by densities (rather than vectors), hence modeling uncertainty that plays a complementary role in coping with data scarcity. Finally, we propose a scalable Variational Bayes optimization algorithm that enables fast approximate Bayesian inference. We evaluate the effectiveness of VBN on linguistic, recommendations, and medical inference tasks. Our findings show that VBN outperforms other existing methods across multiple datasets, and especially in the long-tail.

## CCS CONCEPTS

- Information systems $\rightarrow$ Entity resolution; Recommender systems; $\cdot$ Mathematics of computing $\rightarrow$ Machine learning; $\bullet$ Computing methodologies $\rightarrow$ Natural language processing.


## KEYWORDS

Representation Learning, Variational Bayesian Networks, Collaborative Filtering, Deep Learning, Natural Language Processing, Recommender Systems, Medical Informatics, Bayesian Hierarchical Models, Approximate Bayesian Inference

## 1 INTRODUCTION

Entity representation learning is an active research field with applications in natural language understanding (NLU) [10, 14, 42, 48], recommender systems [3, 5-8, 33, 51], medical informatics [38], and more. In the last decade, a variety of non-contextualized representation learning models were developed [42, 46, 51, 55, 59]. These models learn representations using large datasets of co-occurrences in a self-supervised fashion. However, these datasets often incorporate a long-tail of rare entities with very little co-occurrence data.

[^0]Idan Rejwan* Tel Aviv Univeristy Israel

Itzik Malkiel Tel Aviv University Israel

In the recommender system community, this situation is known as the "cold-start" problem [7, 9], where rare ('cold') entities (e.g., unpopular items or new items that are introduced to the catalog) are often poorly represented due to insufficient statistics. In the natural language processing community, where the focus is on learning representations for words and phrases, a common mitigation is to increase the training set size by utilizing increasingly larger corpus e.g., BERT [20, 39]. However, it was shown that even when increasing the amount of co-occurrence data, the existence of rare, out-of-vocabulary entities persists [26, 50, 52, 53].

A recent attempt proposed a denoising method via fusing several embedding sets for improving the quality of long-tail words [19], but it still relies on the basic ability to learn from co-occurrence statistics. Moreover, in other applications such as recommender systems, medical informatics, etc., co-occurrence data is limited and pre-trained models are generally not in existence. Therefore, in these domains, finetuning pre-trained representations is usually impossible, or extremely limited at best.

While increasing the dataset size is often impossible, other side information on entities might be available and leveraged for mitigating the cold-start problem. For example, in many domains, entities follow a well-defined taxonomy that ties related entities to each other (e.g., genre $\rightarrow$ artist $\rightarrow$ song). Additionally, relational information that defines a relation or a particular type of "connection" between two entities (e.g., warm and cold are antonyms, page and cover are meronyms of book), can be utilized as well. Therefore, in this work, we introduce the Variational Bayesian Network (VBN) a novel Bayesian representation learning model that incorporates external hierarchical and relational side information, in addition to co-occurrence relations. VBN is particularly useful in small data scenarios and for modeling long-tail entities. Our contributions are as follows:

- We introduce the novel VBN objective that facilitates joint modeling of three types of complementary relations: (a) Explicit hierarchical relations via a network of informative priors that enables information propagation between entities to improve representation of entities in the long-tail. (b) Explicit relational information (e.g. antonyms, meronyms, etc.) that enforces structure and consistency between related entities. (c) Implicit relations (co-occurrences) that capture semantic and syntactic information between entities.


[^0]:    *Authors contributed equally to this research.

- We present a tractable yet scalable Variational Bayes (VB) optimization algorithm that maps the entities into probability densities (approximate posteriors). The Bayesian approach is complementary to the aforementioned hierarchical priors and enables better treatment of uncertainty in long-tail entities. This is in contrast to point estimate solutions that treat the latent variables as parameters.
- While our proposed VB algorithm produces a fully factorized posterior approximation, the inference phase still involves intractable integration. Our third contribution is an analytical approximation of the posterior predictive integral that enables fast Bayesian inference.
We demonstrate the effectiveness of VBN on NLU, recommendations, and medical inference tasks. VBN is shown to significantly outperform a variety of state-of-the-art methods across all datasets, and especially in the long-tail.


## 2 RELATED WORK

Incorporating external side information in representation learning has been studied extensively $[4,6,7,9,35,36,56-58,60]$. Retrofitting [21] is a post-processing technique that was introduced in order to refine pretrained word representations using relational information from semantic lexicons. In [15], the authors proposed methods to learn word representations subject to relational constraints but without the utilization of their hierarchical structure. Recently, contextualized word embedding models were expanded to include external linguistic information during pretraining $[1,18,28,34,49]$. Yet, these models require massive amounts of data to be effective. In contrast, VBN models both hierarchical and relational information, during learning, and performs well in small data scenarios.

Bayesian representation learning models were previously proposed in $[2,11,16,32,47,51,55,59]$, and representation learning using graphical models was presented in [24, 37, 46, 54, 55]. Much of these works revolve around NLU and recommender systems. While the aforementioned works do not make explicit use of external side information, one may propose to apply the method from [21] to enhance them with word taxonomy. Our evaluations show that VBN outperforms this alternative.

## 3 VARIATIONAL BAYESIAN NETWORKS

VBN is a probabilistic graphical model in which an entity $i$ can appear either as a leaf node, a parent (internal) node, or both. Let $\mathcal{I}=\{i\}_{i=1}^{N_{\mathrm{W}}}$ be a set of $N_{\mathrm{w}}$ entities (for simplicity, entities are indexed by numbers). Entity nodes are unobserved variables (representations) that are being learned. Specifically, each entity $i$ is associated with two leaf representations $\mathbf{u}_{i}, \mathbf{v}_{i} \in \mathbb{R}^{t}$ (similar to the context and target representations in log bi-linear modeling [42]). Similarly, $\mathbf{h}_{i}^{u}, \mathbf{h}_{j}^{v} \in \mathbb{R}^{t}$ are the parent representations of entity $i$. Hence, if entity $i$ is a parent of entity $j$, then the nodes $\mathbf{h}_{i}^{u}$ and $\mathbf{h}_{j}^{v}$ serve as parents to the nodes $\mathbf{u}_{j}$ and $\mathbf{v}_{j}$, respectively. In addition, every node can have multiple parents and children. Thus, we further define $\pi_{i}, \omega_{i} \subset \mathcal{I}$ as the sets of parents and children entities of entity $i$, respectively.

Figure 1(a) presents a toy example of VBN for the entities dog, Poodle and mouse, and their parents (note that only the ' $u$ ' part
of the graph is shown. The ' $v$ ' part is symmetric). In this example, $\mathbf{h}_{\text {animal }}^{u}$ is the parent of $\mathbf{h}_{\text {dog }}^{u}, \mathbf{u}_{\text {dog }}$ and $\mathbf{u}_{\text {mouse }}$. It is important to distinguish between $\mathbf{u}_{\text {dog }}$ which represents the actual word dog, and $\mathbf{h}_{\text {dog }}^{u}$ that represents the category dog, which is in turn a parent of $\mathbf{u}_{\text {Poodle }}$ that represents the word Poodle (dog breed). Note that $\mathbf{u}_{\text {mouse }}$ has two parents: $\mathbf{h}_{\text {animal }}^{u}$ and $\mathbf{h}_{\text {device }}^{u}$, as the word mouse is ambiguous. Further note that the word representations of the entities animal and device are given by the leaf nodes $\mathbf{u}_{\text {animal }}$ and $\mathbf{u}_{\text {device }}$, respectively (not shown).

### 3.1 Hierarchical Relations

VBN models three types of relations between entities: hierarchical, explicit, and co-occurrence. The model utilizes hierarchical information via informative priors. For example, Fig. 1(a) presents the hierarchy animal $\rightarrow$ dog $\rightarrow$ Poodle. In music recommendations, taxonomy exhibits the following hierarchy: genre $\rightarrow$ subgenre $\rightarrow$ artist $\rightarrow$ song, where each parent entity is used as a prior over its child entity. Let $\mathbf{U}=\left\{\mathbf{u}_{i}\right\}_{i \in \mathcal{I}}, \mathbf{H}^{u}=\left\{\mathbf{h}_{i}^{u}\right\}_{i \in \mathcal{I}}$, and denote $\mathbf{s}_{i}^{u} \triangleq\left|\pi_{i}\right|^{-1} \sum_{n \in \pi_{i}} \mathbf{h}_{n}^{u}$, if $\pi_{i} \neq \emptyset$, otherwise $\mathbf{s}_{i}^{u}$ is set to 0 . We assume Normal-Gamma hierarchical priors:

$$
\begin{aligned}
p\left(\mathbf{U}, \mathbf{H}^{u}, \boldsymbol{\mathcal { T }}^{u}, \boldsymbol{\mathcal { T }}^{h^{u}} \mid \mathcal{H}\right)=\prod_{i \in \mathcal{I}} & \mathcal{N}\left(\mathbf{u}_{i} ; \mathbf{s}_{i}^{u}, \tau_{u_{i}}^{-1} \mathbf{i}\right) \mathcal{G}\left(\tau_{u_{i}} ; \alpha, \beta\right) \\
& \mathcal{N}\left(\mathbf{h}_{i}^{u} ; \mathbf{s}_{i}^{u}, \tau_{h_{i}^{u}}^{-1} \mathbf{i}\right) \mathcal{G}\left(\tau_{h_{i}^{u}} ; \alpha, \beta\right)
\end{aligned}
$$

where $\boldsymbol{\mathcal { T }}^{u}=\left\{\tau_{u_{i}}\right\}_{i \in \mathcal{I}}$ and $\boldsymbol{\mathcal { T }}^{h^{u}}=\left\{\tau_{h_{i}^{u}}\right\}_{i \in \mathcal{I}}\left(\tau_{u_{i}}, \tau_{h_{i}^{u}} \in \mathbb{R}\right)$ are the precision variables that follows the Gamma hyperpriors with shape and rate hyperparameters $\mathcal{H}=\{\alpha, \beta\}$. The hierarchical priors in Eq. 1 enforce entity representations to be closer to their parents, in terms of $L^{2}$ distance, where the precision variables control the strength of this constraint. This enables child nodes to naturally "fallback" on to their parents in case of insufficient statistics. As we will see, this unique feature improves the representation of longtail entities. Further note that the formulation in Eq. 1 supports hierarchical relations of arbitrary depths. Finally, $\mathbf{V}, \mathbf{H}^{v}, \boldsymbol{\mathcal { T }}^{h^{v}}, \boldsymbol{\mathcal { T }}^{v}$ and $\mathbf{s}_{i}^{v}$ together with their priors and hyperpriors are defined in a symmetric manner. The hierarchical relations appear in Fig. 1(b) (green).

We note that in the general case, the hierarchical priors can be modeled via multimodal distributions (e.g., Gaussian Mixture Models). Moreover, various types of content (e.g., image, audio, free text) can be processed by a neural network that predicts the parameters of the distribution. However, we leave the investigation of these extensions for future work.

### 3.2 Co-occurrence Relations

VBN learning is based on modeling co-occurrence relations. These co-occurrences can be words that appear next to each other, coconsumed items, co-morbid diseases, etc. Let $I_{P}=\{(i, j) \mid$ entity $j$ occurs in the context of entity $i\}$ be the co-occurrence dataset (positive relations). Note that $I_{P}$ is a multiset, i.e. $(i, j)$ can appear multiple times in $I_{P}$. During training, we subsample [42] a new $I_{P^{\prime}} \subset I_{P}$ every epoch. Then, for each positive pair $(i, j) \in I_{P^{\prime}}$, we sample $n$ negative pairs $\left\{\left(i, z_{I}\right) \mid\left(i, z_{I}\right) \notin I_{P^{\prime}}\right\}_{I=1}^{n}$ to form a negative multiset $I_{N}$. Hence, the training set $I_{D}=I_{P^{\prime}} \cup I_{N}$ is stochastic.

VBN models co-occurrence relations as a classification problem via a two-point random variable $d: \mathcal{I} \times \mathcal{I} \rightarrow\{1,-1\}$ with $d_{i j}=1$

![img-0.jpeg](img-0.jpeg)

Figure 1: (a) A toy VBN example for the entities dog, Poodle, mouse and their parents. Only the $u$ part is presented (the $v$ part is symmetric. See Section 3 for details). (b) VBN's graphical model. Gray variables are observed (data), whereas white variables are unobserved (learned). $d_{i j}$ are the co-occurrence data, explained (blue arrows) by the leaf entity representations $\mathbf{u}_{i}, \mathbf{v}_{j}$ and bias $b_{j}$ (Section 3.2). $g_{i j}^{k}$ are the explicit relations data, explained (purple arrows) by $\mathbf{u}_{i}$ and $\mathbf{v}_{j}$, the linear mappings induced by $\mathbf{x}_{m k}$ and $\mathbf{y}_{m k}$, and the bias term $r_{j k}$ (Section 3.3). $\mathbf{h}_{u}^{u}$ and $\mathbf{h}_{j}^{v}$ are the parent entity representations that form hierarchical priors (green arrows) over $\mathbf{u}_{i}$ and $\mathbf{v}_{j}$, respectively (Section 3.1). $\tau_{u_{i}}, \tau_{v_{j}}, \tau_{x_{m k}}, \tau_{y_{m k}}, \tau_{h_{u}^{u}}, \tau_{h_{j}^{v}}, \tau_{b_{j}}, \tau_{r_{j k}}$ are the learned precision variables with Gamma hyperprior, where $\alpha$ and $\beta$ are the shape and rate hyperparameters, respectively.
if $(i, j) \in I_{P}^{s}$, otherwise $d_{i j}=-1$. Let $\mathbf{D}=\left\{d_{i j} \mid(i, j) \in I_{D}\right\}$ be the training data (D are observed). The likelihood is given by:

$$
p(\mathbf{D} \mid \mathbf{U}, \mathbf{V}, \mathbf{B})=\prod_{(i, j) \in I_{D}} \sigma\left(d_{i j}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}+b_{j}\right)\right)
$$

where $\sigma(x)=1 /\left(1+e^{-x}\right) . \mathbf{B}=\left\{b_{i}\right\}_{i \in \mathcal{I}}\left(b_{i} \in \mathbb{R}\right)$ are bias variables with Normal-Gamma priors:

$$
p\left(\mathbf{B}, \mathcal{T}^{b} \mid \mathcal{H}\right)=\prod_{i \in \mathcal{I}} \mathcal{N}\left(b_{i} ; 0, \tau_{b_{i}}^{-1}\right) \mathcal{G}\left(\tau_{b_{i}} ; \alpha, \beta\right)
$$

Equation 2 explains the observed variables $d_{i j} \in \mathbf{D}$ (the data) by the unobserved variables $\mathbf{u}_{i}, \mathbf{v}_{j}$ and $b_{j}$, as depicted in Fig. 1(b) (in blue).

### 3.3 Explicit Relations

VBN further utilizes explicit semantic relations (e.g., antonyms, meronyms, etc.) to enforce additional structure in the latent space and yield more meaningful representations. To this end, VBN learns representations for any explicit relation and compels entities that share the same relation to "adhere" as we explain next.

We denote by $i \xrightarrow{k} j$ the fact that entities $i$ and $j$ share a directed relation $k$. For undirected relations, $i \xrightarrow{k} j \wedge j \xrightarrow{k} i$ holds. A dataset of "type $k$ relations" is constructed in a stochastic manner similarly to the procedure described in Section 3.2: Let $I_{P}^{k}=\{(i, j) \mid i \xrightarrow{k} j\}$ be the set of positive pairs. For each $(i, j) \in I_{P}^{k}$, we uniformly sample $n$ negative pairs $\left\{\left(i, z_{l}\right) \mid\left(i, z_{l}\right) \notin I_{P}^{k}\right\}_{l=1}^{n}$ to form the negative multi-set
$I_{N}^{k}$. Finally, $I_{G}^{k}=I_{P}^{k} \cup I_{N}^{k}$ is the sampled dataset. This procedure is repeated every epoch by sampling a new $I_{N}^{k}$, while keeping $I_{P}^{k}$ fixed throughout the training process.

Similarly to co-occurrences, we model $i \xrightarrow{k} j$ via a two-point random variable $g^{k}: \mathcal{I} \times \mathcal{I} \rightarrow\{1,-1\}$ with $g_{i j}^{k}=1$ iff $(i, j) \in I_{P}^{k}$, and $\mathbf{G}^{k}=\left\{g_{i j}^{k} \mid(i, j) \in I_{P}^{k}\right\}$ ( $\mathbf{G}^{k}$ are observed). For $N_{B}$ different types of explicit relations, we define $\mathbf{G}=\left\{\mathbf{G}^{k}\right\}_{k=1}^{N_{B}}$, and the likelihood is given by:

$$
p\left(\mathbf{G} \mid \mathbf{U}, \mathbf{V}, \mathbf{W}, \mathbf{R}\right)=\prod_{k=1}^{N_{B}} \prod_{(i, j) \in I_{G}^{k}} \sigma\left(g_{i j}^{k}\left(\mathbf{u}_{i}^{T} \mathbf{W}_{k} \mathbf{v}_{j}+r_{j k}\right)\right)
$$

with $\mathbf{W}=\left\{\mathbf{W}_{k}\right\}_{k=1}^{N_{B}}$ and $\mathbf{W}_{k}=\mathbf{X}_{k} \mathbf{Y}_{k}^{T}$, where $\mathbf{X}_{k}$ and $\mathbf{Y}_{k}$ are lowrank matrices in $\mathbb{R}^{t \times t_{k}}$ whose columns are unobserved random vectors $\mathbf{x}_{m k} \in \mathbb{R}^{t}$ and $\mathbf{y}_{m k} \in \mathbb{R}^{t}\left(1 \leq m \leq t_{k}\right)$, respectively, and $\mathbf{R}=\left\{r_{i k}\right\}_{1 \leq k \leq N_{B}, i \in \mathcal{I}}$ are biases, with Normal-Gamma priors as follows:

$$
\begin{gathered}
p\left(\mathbf{W}, \mathbf{R}, \mathcal{T}^{x}, \mathcal{T}^{y}, \mathcal{T}^{t} \mid \mathcal{H}\right)=\prod_{k=1}^{N_{B}} \prod_{i \in \mathcal{I}} \mathcal{N}\left(r_{i k} ; 0, \tau_{r_{i k}}^{-1}\right) \mathcal{G}\left(\tau_{r_{i k}} ; \alpha, \beta\right) \\
\prod_{m=1}^{t_{k}} \mathcal{N}\left(\mathbf{x}_{m k} ; 0, \tau_{x_{m k}}^{-1} \mathbf{I}\right) \mathcal{G}\left(\tau_{x_{m k}} ; \alpha, \beta\right) \\
\mathcal{N}\left(\mathbf{y}_{m k} ; 0, \tau_{y_{m k}}^{-1} \mathbf{I}\right) \mathcal{G}\left(\tau_{y_{m k}} ; \alpha, \beta\right)
\end{gathered}
$$

Equation 4 explains the data $g_{i j}^{k} \in \mathbf{G}^{k}$ by the unobserved variables $\mathbf{u}_{i}, \mathbf{v}_{j}, \mathbf{X}_{k}, \mathbf{Y}_{k}$ and $r_{j k}$, as depicted in Fig. 1(b) (in purple). $\mathbf{X}_{k}$ and $\mathbf{Y}_{k}$ map $\mathbf{u}_{i}$ and $\mathbf{v}_{j}$ to a subspace s.t. if $i \xrightarrow{k} j$, then $\mathbf{u}_{i}^{T} \mathbf{W}_{k} \mathbf{v}_{j}+r_{j k}$

is maximized. Specifically, in the case of undirected relations (e.g., antonyms), $\mathbf{u}_{j}^{T} \mathbf{W}_{k} \mathbf{v}_{i}+r_{i k}$ is maximized as well.

### 3.4 The Joint Distribution

We denote the data by $\boldsymbol{\mathcal { D }}=\{\mathbf{D}, \mathbf{G}\}$, the unobserved (learned) variables by $\boldsymbol{\theta}=\left\{\mathbf{U}, \mathbf{V}, \mathbf{W}, \mathbf{B}, \mathbf{R}, \mathbf{H}^{u}, \mathbf{H}^{o}, \boldsymbol{\mathcal { T }}^{u}, \boldsymbol{\mathcal { T }}^{o}, \boldsymbol{\mathcal { T }}^{u}, \boldsymbol{\mathcal { T }}^{u}, \boldsymbol{\mathcal { T }}^{e}, \boldsymbol{\mathcal { T }}^{h}, \boldsymbol{\mathcal { T }}^{h^{u}}\right\}$, and the hyperparameters by $\mathcal{H}=\{\alpha, \beta\}$. Then, the joint log distribution is $\log p(\boldsymbol{\mathcal { D}}, \boldsymbol{\theta} \mid \mathcal{H})=\log p(\boldsymbol{\mathcal { D}} \mid \boldsymbol{\theta})+\log p(\boldsymbol{\theta} \mid \mathcal{H})$, where the joint $\log$ likelihood (Eqs. 2, 4) is given by:

$$
\begin{aligned}
\log p(\boldsymbol{\mathcal { D}} \mid \boldsymbol{\theta})= & \sum_{(i, j) \in I_{D}} \log \sigma\left(d_{i j}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}+b_{j}\right)\right) \\
& +\sum_{k=1}^{N_{R}} \sum_{(i, j) \in I_{G}^{k}} \log \sigma\left(g_{i j}^{k}\left(\mathbf{u}_{i}^{T} \mathbf{W}_{k} \mathbf{v}_{j}+r_{j k}\right)\right)
\end{aligned}
$$

and the log prior (Eqs. 1,3,5) is given by:

$$
\begin{aligned}
\log p(\boldsymbol{\theta} \mid \mathcal{H})= & -\frac{1}{2} \sum_{i \in I} \tau_{u_{i}}\left\|\mathbf{u}_{i}-\mathbf{s}_{i}^{u}\right\|_{2}^{2}+\tau_{v_{i}}\left\|\mathbf{v}_{i}-\mathbf{s}_{i}^{v}\right\|_{2}^{2} \\
& +\tau_{b_{i}} b_{i}^{2}+\tau_{h_{i}^{u}}\left\|\mathbf{h}_{i}^{u}-\mathbf{s}_{i}^{u}\right\|_{2}^{2}+\tau_{h_{i}^{v}}\left\|\mathbf{h}_{i}^{v}-\mathbf{s}_{i}^{v}\right\|_{2}^{2} \\
& +\sum_{k=1}^{N_{R}} \tau_{r_{i k}} r_{i k}^{2}-\frac{1}{2} \sum_{k=1}^{N_{R}} \sum_{m=1}^{J_{k}} \tau_{x_{m k}}\left\|\mathbf{x}_{m k}\right\|_{2}^{2}+\tau_{y_{m k}}\left\|\mathbf{y}_{m k}\right\|_{2}^{2} \\
& +\left(\alpha+\frac{I}{2}-1\right)\left[\sum_{i \in I} \log \tau_{u_{i}}+\log \tau_{v_{i}}+\log \tau_{h_{i}^{u}}+\log \tau_{h_{i}^{v}}\right. \\
& \left.+\sum_{k=1}^{N_{R}} \sum_{m=1}^{J_{k}} \log \tau_{x_{m k}}+\log \tau_{y_{m k}}\right]+\sum_{i \in I}\left(\alpha+\frac{1}{2}-1\right)\left[\log \tau_{b_{i}}\right. \\
& \left.+\sum_{k=1}^{N_{R}} \log \tau_{r_{i k}}\right]-\beta\left(\tau_{u_{i}}+\tau_{v_{i}}+\tau_{h_{i}^{u}}+\tau_{h_{i}^{v}}+\tau_{b_{i}}+\sum_{k=1}^{N_{R}} \tau_{r_{i k}}\right) \\
& -\beta \sum_{k=1}^{N_{R}} \sum_{m=1}^{J_{k}} \tau_{x_{m k}}+\tau_{y_{m k}}+\text { const. }
\end{aligned}
$$

### 3.5 VBN Optimization and Inference

We aim at computing the posterior predictive distribution of $d_{i j}$ and $g_{i j}^{k}$. For brevity, we focus on $d_{i j}$, since $g_{i j}^{k}$ is computed in the same manner. The posterior predictive probability of entity $j$ to occur in the vicinity of entity $i$ is written as a marginalization over $\boldsymbol{\theta}$ as follows:

$$
p\left(d_{i j}=1 \mid \boldsymbol{\mathcal { D }}, \mathcal{H}\right)=\int \sigma\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}+b_{j}\right) p(\boldsymbol{\theta} \mid \boldsymbol{\mathcal { D }}, \mathcal{H}) d \boldsymbol{\theta}
$$

The posterior $p(\boldsymbol{\theta} \mid \boldsymbol{\mathcal { D }}, \mathcal{H})$ in Eq. 8 is intractable. Hence, we turn to a VB approximation [13] of $p(\boldsymbol{\theta} \mid \boldsymbol{\mathcal { D }}, \mathcal{H})$ with a fully factorized distribution $q(\boldsymbol{\theta})=\prod_{z \in \boldsymbol{\theta}} q(z) . q(\boldsymbol{\theta})$ is obtained by minimizing the Kullback-Lieber divergence $D_{K L}(q(\boldsymbol{\theta}) \| p(\boldsymbol{\theta} \mid \boldsymbol{\mathcal { D }}, \mathcal{H}))$, which is equivalent to the maximization of the variational free energy [13]: $\mathcal{L}(q)=-D_{K L}(q(\boldsymbol{\theta}) \| p(\boldsymbol{\theta} \mid \boldsymbol{\mathcal { D }}, \mathcal{H}))+\log p(\boldsymbol{\mathcal { D}} \mid \mathcal{H})$. The maximization of $\mathcal{L}(q)$ is done by following an iterative procedure (which is guaranteed to converge [13]). At each iteration, for each $z \in \boldsymbol{\theta}$, update $q(z)$ according to the general VB update rule:

$$
q^{*}(z)=\exp \left(\mathbb{E}_{q(\boldsymbol{\theta} \mid z)}[\log p(\boldsymbol{\theta}, \boldsymbol{\mathcal { D }} \mid \mathcal{H})]+\text { const }\right)
$$

Unfortunately, a straightforward application of the VB update rule from Eq. 9 is impractical. This happens since the normal priors in Eq. 7 are not conjugate to the Bernoulli likelihoods in Eq. 6, hence the joint distribution $p(\boldsymbol{\theta}, \boldsymbol{\mathcal { D }} \mid \mathcal{H})$ does not belong to the exponential family. Therefore, to enable conjugacy, we propose to lower-bound the logistic terms in Eq. 6 with Gaussian functions by using the following bound from [29]:

$$
\log \sigma(x) \geq \frac{x-\delta}{2}-\lambda(\delta)\left(x^{2}-\delta^{2}\right)+\log \sigma(\delta)
$$

where $\delta$ is the variational parameter and $\lambda(\delta) \triangleq \frac{1}{2 \delta}\left(\sigma(\delta)-\frac{1}{2}\right)$. Note that the bound becomes tight for $\delta=x$. We lower-bound each term in the joint log likelihood (Eq. 6) according to Eq. 10, thus introducing a variational parameter $\xi_{i j}$ for any co-occurrence $(i, j) \in I_{D}$ and $\zeta_{i j}^{k}$ for any explicit relation $(i, j) \in I_{G}^{k}$ for $1 \leq k \leq N_{R}$ as follows:

$$
\begin{aligned}
\log p(\boldsymbol{\mathcal { D }} \mid \boldsymbol{\theta}) & \geq \log \hat{p}(\boldsymbol{\mathcal { D }} \mid \boldsymbol{\theta}) \\
& =\sum_{(i, j) \in I_{D}} \frac{d_{i j}\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}+b_{j}\right)-\xi_{i j}}{2} \\
& -\lambda\left(\xi_{i j}\right)\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j} \mathbf{v}_{j}^{T} \mathbf{u}_{i}+2 \mathbf{u}_{i}^{T} \mathbf{v}_{j} b_{j}+b_{j}^{2}-\xi_{i j}^{2}\right) \\
& +\log \sigma\left(\xi_{i j}\right)+\sum_{k=1}^{N_{R}} \sum_{(i, j) \in I_{G}^{k}} \frac{g_{i j}^{k}\left(\mathbf{u}_{i}^{T} \mathbf{W}_{k} \mathbf{v}_{j}+r_{j k}\right)-\zeta_{i j}^{k}}{2} \\
& -\lambda\left(\zeta_{i j}^{k}\right)\left(\mathbf{u}_{i}^{T} \mathbf{W}_{k} \mathbf{v}_{j} \mathbf{v}_{j}^{T} \mathbf{W}_{k}^{T} \mathbf{u}_{i}+2 r_{j k} \mathbf{u}_{i}^{T} \mathbf{W}_{k} \mathbf{v}_{j}+r_{j k}^{2}\right. \\
& \left.-\zeta_{i j}^{k^{2}}\right)+\log \sigma\left(\zeta_{i j}^{k}\right))
\end{aligned}
$$

Finally, by plugging $\log \hat{p}(\boldsymbol{\mathcal { D }} \mid \boldsymbol{\theta})$ into Eq. 9, we receive the new bounded version of the VB update rule:

$$
\tilde{q}^{*}(z)=\exp \left(\mathbb{E}_{q(\boldsymbol{\theta} \mid\{z\})}[\log \hat{p}(\boldsymbol{\mathcal { D }} \mid \boldsymbol{\theta})+\log p(\boldsymbol{\theta} \mid \mathcal{H})]+\text { const }\right)
$$

### 3.5.1 Optimization.

The update rule in Eq. 12 enables conjugacy, and hence we are able to recognize the natural parameters of the Normal distributions and the Gamma distributions that give raise to the update steps for each of the approximated posterior distributions $q(z), z \in \boldsymbol{\theta}$ :

Updating $q\left(\mathbf{u}_{i}\right)$ and $q\left(\mathbf{v}_{j}\right)$ : The updates of $q\left(\mathbf{u}_{i}\right)$ are based on the sufficient statistics of the multivariate Gaussian, namely the precision matrix $\mathbf{P}_{\mathbf{u}_{i}}$ and mean vector $\boldsymbol{\mu}_{\mathbf{u}_{i}}$ given by:

$$
\begin{aligned}
& \mathbf{P}_{\mathbf{u}_{i}}=\mu_{r_{u_{i}}} \mathbf{I}+2\left(\sum_{j:(i, j) \in I_{D}} \lambda\left(\xi_{i j}\right) \mathbb{E}\left[\mathbf{v}_{j} \mathbf{v}_{j}^{T}\right]\right. \\
& \left.\quad+\sum_{k=1}^{N_{R}} \sum_{j:(i, j) \in I_{G}^{k}} \lambda\left(\zeta_{i j}^{k}\right) \mathbb{E}\left[\mathbf{W}_{k} \mathbf{v}_{j} \mathbf{v}_{j}^{T} \mathbf{W}_{k}^{T}\right]\right) \\
& \boldsymbol{\mu}_{\mathbf{u}_{i}}=\mathbf{P}_{\mathbf{u}_{i}}^{-1}\left(\left|\pi_{i}\right|^{-1} \mu_{r_{u_{i}}} \sum_{m \in \pi_{i}} \boldsymbol{\mu}_{\mathbf{h}_{m}^{u}}\right. \\
& +\frac{1}{2}\left(\sum_{j:(i, j) \in I_{D}}\left(d_{i j}-4 \lambda\left(\xi_{i j}\right) \mu_{b_{j}}\right) \boldsymbol{\mu}_{\mathbf{v}_{j}}\right. \\
& \left.\quad+\sum_{k=1}^{N_{R}} \sum_{j:(i, j) \in I_{G}^{k}}\left(g_{i j}^{k}-4 \lambda\left(\zeta_{i j}^{k}\right) \mu_{r_{j k}}\right) \mathbf{M}_{k} \boldsymbol{\mu}_{\mathbf{v}_{j}}\right)
\end{aligned}
$$

with

$$
\begin{aligned}
& \mathbb{E}\left[\mathbf{W}_{k} \mathbf{v}_{j} \mathbf{v}_{j}^{T} \mathbf{W}_{k}^{T}\right]=\mathbb{E}\left[\sum_{m=1}^{t_{k}} \mathbf{x}_{m k} \mathbf{y}_{m k}^{T} \mathbf{v}_{j} \mathbf{v}_{j}^{T} \mathbf{y}_{m k} \mathbf{x}_{m k}^{T}\right. \\
& \left.+\sum_{m \neq n} \mathbf{x}_{m k} \mathbf{y}_{n k}^{T} \mathbf{v}_{j} \mathbf{v}_{j}^{T} \mathbf{y}_{n k} \mathbf{x}_{m k}^{T}\right] \\
&= \sum_{m=1}^{t_{k}} \mathbb{E}\left[\left(\mathbf{y}_{m k}^{T} \mathbf{v}_{j}\right)^{2}\right] \mathbb{E}\left[\mathbf{x}_{m k} \mathbf{x}_{m k}^{T}\right] \\
&+\sum_{m \neq n} \boldsymbol{\mu}_{\mathbf{x}_{m k}} \boldsymbol{\mu}_{\mathbf{y}_{m k}}^{T} \mathbb{E}\left[\mathbf{v}_{j} \mathbf{v}_{j}^{T}\right] \boldsymbol{\mu}_{\mathbf{y}_{n k}} \boldsymbol{\mu}_{\mathbf{x}_{n k}}^{T}
\end{aligned}
$$

and $\mathbf{M}_{k}=\mathbf{M}_{\mathbf{X}_{k}} \mathbf{M}_{\mathbf{Y}_{k}}^{T}$, where $\mathbf{M}_{\mathbf{X}_{k}}$ and $\mathbf{M}_{\mathbf{Y}_{k}}$ are the matrices whose columns are the expectations $\boldsymbol{\mu}_{\mathbf{x}_{m k}}$ and $\boldsymbol{\mu}_{\mathbf{y}_{m k}}$.

In practice, we only consider diagonal precision matrices by setting all off-diagonal parameters to zero ${ }^{1}$. Besides reducing the model's space complexity, it also simplifies significantly the matrix inversion for extracting the mean value. The update for $q\left(\mathbf{v}_{j}\right)$ is symmetric to that of $q\left(\mathbf{u}_{i}\right)$ (as appears in Eq. 13).

Updating $q\left(\mathbf{x}_{m k}\right)$ and $q\left(\mathbf{y}_{m k}\right)$ : The update of $q\left(\mathbf{x}_{m k}\right)$ is given by:

$$
\begin{aligned}
& \mathbf{P}_{\mathbf{x}_{m k}}=\mu_{\tau_{\mathbf{x}_{m k}}} \mathbf{I}+2 \sum_{(i, j) \in I_{t_{i}}^{k}} \lambda\left(\zeta_{i j}^{k}\right) \mathbb{E}\left[\mathbf{u}_{i} \mathbf{y}_{m k}^{T} \mathbf{v}_{j} \mathbf{v}_{j}^{T} \mathbf{y}_{m k} \mathbf{u}_{i}^{T}\right], \\
& \boldsymbol{\mu}_{\mathbf{x}_{m k}}=\frac{1}{2} \mathbf{P}_{\mathbf{x}_{m k}}^{-1}\left(\sum_{(i, j) \in I_{t_{i}}^{k}} \rho_{i j}^{k} \boldsymbol{\mu}_{\mathbf{y}_{m k}}^{T} \boldsymbol{\mu}_{\mathbf{v}_{j}} \boldsymbol{\mu}_{\mathbf{u}_{i}}^{T}\right. \\
& -4 \lambda\left(\zeta_{i j}^{k}\right)\left(\mu_{r_{j k}} \boldsymbol{\mu}_{\mathbf{y}_{m k}}^{T} \boldsymbol{\mu}_{\mathbf{v}_{j}} \boldsymbol{\mu}_{\mathbf{u}_{i}}^{T}\right. \\
& \left.+\sum_{n \neq m} \boldsymbol{\mu}_{\mathbf{x}_{n k}}^{T} \mathbb{E}\left[\mathbf{u}_{i} \mathbf{v}_{j}^{T} \boldsymbol{\mu}_{\mathbf{y}_{n k}} \boldsymbol{\mu}_{\mathbf{y}_{m k}}^{T} \mathbf{v}_{j} \mathbf{u}_{i}^{T}\right]\right),
\end{aligned}
$$

where the expectations are computed in the same manner as in Eq. 14. The update of $q\left(\mathbf{y}_{m k}\right)$ is symmetric.

Updating $\xi_{i j}$ and $\zeta_{i j}^{k}$ : The updates of the variational parameters are given by:

$$
\begin{aligned}
& \xi_{i j}=\left(\mathbb{E}\left[\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}\right)^{2}\right]+2 \mu_{b_{j}} \boldsymbol{\mu}_{\mathbf{u}_{i}}^{T} \boldsymbol{\mu}_{\mathbf{v}_{j}}+\mathbb{E}\left[b_{j}^{2}\right]\right)^{1 / 2} \\
& \zeta_{i j}^{k}=\left(\mathbb{E}\left[\left(\mathbf{u}_{i}^{T} \mathbf{W}_{k} \mathbf{v}_{j}\right)^{2}\right]+2 \mu_{r_{j k}} \boldsymbol{\mu}_{\mathbf{u}_{i}}^{T} \mathbf{M}_{k} \boldsymbol{\mu}_{\mathbf{v}_{j}}+\mathbb{E}\left[r_{j k}^{2}\right]\right)^{1 / 2}
\end{aligned}
$$

Updating $q\left(\mathbf{h}_{i}^{u}\right)$ and $q\left(\mathbf{h}_{i}^{v}\right)$ : The updates of $q\left(\mathbf{h}_{i}^{u}\right)$ and $q\left(\mathbf{h}_{i}^{v}\right)$ are symmetric as well. Hence, we only provide the update of $q\left(\mathbf{h}_{i}^{u}\right)$ based on the precision matrix $\mathbf{P}_{\mathbf{h}_{i}^{u}}$ and mean vector $\boldsymbol{\mu}_{\mathbf{h}_{i}^{u}}$ :

$$
\begin{aligned}
& \mathbf{P}_{\mathbf{h}_{i}^{u}}=\left(\mu_{\tau_{h_{i}^{u}}}+\sum_{m \in \omega_{i}}\left(\mu_{\tau_{h_{m}^{u}}}+\mu_{\tau_{u_{m}}}\right)\left|\pi_{m}\right|^{-2}\right) \mathbf{I} \\
& \boldsymbol{\mu}_{\mathbf{h}_{i}^{u}}=\mathbf{P}_{\mathbf{h}_{i}^{u}}^{-1}\left(\left|\pi_{i}\right|^{-1} \mu_{\tau_{h_{i}^{u}}} \sum_{l \in \pi_{i}} \boldsymbol{\mu}_{\mathbf{h}_{i}^{u}}\right. \\
& \left.+\sum_{m \in \omega_{i}}\left|\pi_{m}\right|^{-1}\left(\mu_{\tau_{u_{m}}}, \boldsymbol{\mu}_{\mathbf{u}_{m}}+\mu_{\tau_{h_{m}^{u}}}, \boldsymbol{\mu}_{\mathbf{h}_{m}^{u}}\right)\right. \\
& \left.-\left|\pi_{m}\right|^{-2}\left(\mu_{\tau_{h_{m}^{u}}}+\mu_{\tau_{u_{m}}}\right) \sum_{n \in \pi_{m} \backslash\{i\}} \boldsymbol{\mu}_{\mathbf{h}_{n}^{u}}\right)
\end{aligned}
$$

Updating $q\left(b_{j}\right)$ : The update of $q\left(b_{j}\right)$ is given by the (scalar) precision $\mathrm{p}_{b_{j}}$ and mean $\mu_{b_{j}}$ :

$$
\begin{aligned}
& \mathrm{p}_{b_{j}}=\mu_{\tau_{b_{j}}}+2 \sum_{i:(i, j) \in I_{D}} \lambda\left(\xi_{i j}\right) \\
& \mu_{b_{j}}=\frac{1}{2} \mathrm{p}_{b_{j}}^{-1} \sum_{i:(i, j) \in I_{D}}\left(d_{i j}-4 \lambda\left(\xi_{i j}\right) \boldsymbol{\mu}_{\mathbf{u}_{i}}^{T} \boldsymbol{\mu}_{\mathbf{v}_{j}}\right)
\end{aligned}
$$

[^0]Updating $q\left(r_{j k}\right)$ : The update of $q\left(r_{j k}\right)$ is given by the scalar parameters:

$$
\begin{aligned}
& \mathrm{p}_{r_{j k}}=\mu_{\tau_{r_{j k}}}+2 \sum_{i:(i, j) \in I_{G}^{k}} \lambda\left(\xi_{i j}^{k}\right) \\
& \mu_{r_{j k}}=\frac{1}{2} \mathrm{p}_{b_{j}}^{-1} \sum_{i:(i, j) \in I_{G}^{k}}\left(q_{i j}^{k}-4 \lambda\left(\zeta_{i j}^{k}\right) \boldsymbol{\mu}_{\mathbf{u}_{i}}^{T} \mathbf{M}_{k} \boldsymbol{\mu}_{\mathbf{v}_{j}}\right)
\end{aligned}
$$

The updates of $q\left(\tau_{u_{i}}\right), q\left(\tau_{v_{i}}\right), q\left(\tau_{h_{i}^{u}}\right)$, and $q\left(\tau_{h_{i}^{v}}\right): q\left(\tau_{u_{i}}\right)$ follows the Gamma distribution with rate $\alpha_{u_{i}}$ and shape $\beta_{u_{i}}$ parameters. Their updates are given by

$$
\begin{aligned}
& \alpha_{u_{i}}=\alpha+\frac{1}{2} t \\
& \beta_{u_{i}}=\beta+\frac{1}{2} \mathbb{E}\left[\left(\mathbf{u}_{i}-\mathbf{s}_{i}^{u}\right)^{T}\left(\mathbf{u}_{i}-\mathbf{s}_{i}^{u}\right)\right]
\end{aligned}
$$

The updates of $q\left(\tau_{v_{i}}\right), q\left(\tau_{h_{i}^{u}}\right)$, and $q\left(\tau_{h_{i}^{v}}\right)$ are symmetric to $q\left(\tau_{u_{i}}\right)$.
Updating and $q\left(\tau_{\pi_{m k}}\right)$ and $q\left(\tau_{\eta_{m k}}\right)$ : The updates of $q\left(\tau_{\pi_{m k}}\right)$ are given by:

$$
\begin{aligned}
& \alpha_{\pi_{m k}}=\alpha+\frac{1}{2} t \\
& \beta_{\pi_{m k}}=\beta+\frac{1}{2} \mathbb{E}\left[\mathbf{x}_{m k}^{T} \mathbf{x}_{m k}\right]
\end{aligned}
$$

The updates of $q\left(\tau_{\eta_{m k}}\right)$ are symmetric.
Updating $q\left(\tau_{b_{j}}\right)$ and $q\left(\tau_{r_{j k}}\right)$ : The updates of $q\left(\tau_{b_{j}}\right)$ are given by:

$$
\begin{aligned}
& \alpha_{b_{j}}=\alpha+\frac{1}{2} \\
& \beta_{b_{j}}=\beta+\frac{1}{2} \mathbb{E}\left[b_{j}^{2}\right]
\end{aligned}
$$

The updates of $q\left(\tau_{r_{j k}}\right)$ are symmetric.
VBN's optimization algorithm alternates between the ' $u$ ' and ' $v$ ' parts of the VBN graph. The optimization easily scales as the updates of the $u$ ( $v$ ) part are embarrassingly parallel in the number of entities $N_{W}$ and relations $N_{R}$. Specifically, we can update each of the $q$ distributions in $\mathbf{U}, \mathbf{V}, \mathbf{B}, \mathbf{R}, \boldsymbol{\mathcal { T }}^{\mathbf{u}}, \boldsymbol{\mathcal { T }}^{\mathbf{v}}, \boldsymbol{\mathcal { T }}^{\mathbf{v}}, \boldsymbol{\mathcal { T }}^{\mathbf{r}}, \boldsymbol{\mathcal { T }}^{\mathbf{h}^{u}}, \boldsymbol{\mathcal { T }}^{\mathbf{h}^{v}}$, each in turn, in parallel, by using the expected value of the variables in the other sets (including $\mathbf{H}^{u}, \mathbf{H}^{v}, \mathbf{X}, \mathbf{Y}$ ). Yet, the updates of the variables in $\mathbf{H}^{u}, \mathbf{H}^{v}, \mathbf{X}, \mathbf{Y}$ require special care: This is since according to Eq. 17, the updates of a variable in $\mathbf{H}^{u}\left(\mathbf{H}^{v}\right)$ depend on the expectations of its children, parents, and other parents of its children (if exist).

In order to enable parallel updates of $\mathbf{H}^{u}$, we propose Alg. 1 that operates in a bottom-up manner and partitions $A^{u}=\mathbf{H}^{u} \cup \mathbf{U}$ to $M$ disjoint sets $\left\{Y_{m}^{u}\right\}_{m=1}^{M} \mathrm{~s}$. for each variable $n$ in the set $Y_{m}^{u}$ its parents (line 20), children, and other parents of its children (line 15) are not in $Y_{m}^{u}$. This ensures all the variables in $Y_{m}^{u}$ can be updated in parallel. Note that $\mathbf{U} \subset Y_{i}^{u}$ is guaranteed, hence, $\mathbf{U}$ can be updated in parallel. Then, Alg. 1 is applied to $A^{v}=\mathbf{H}^{v} \cup \mathbf{V}$ to produce $\left\{Y_{m}^{v}\right\}_{m=1}^{M}$. In practice, we perform Alg. 1 once before the optimization procedure begins and save the indices of the nodes for each disjoint set for both the $u$ and $v$ parts of the graph. In addition, as can be seen in Eq. 15, $\boldsymbol{\mu}_{\mathbf{x}_{m k}}$ depends on $\boldsymbol{\mu}_{\mathbf{x}_{n k}}$, for all $n \neq m$. Therefore, parallel updates of the variables in $\mathbf{X}_{k}\left(\mathbf{Y}_{k}\right)$ are possible across the $k$ axis, but not across $m$.

Finally, the VBN optimization algorithm is presented in Alg. 2. The algorithm receives the partitions $\left\{Y_{m}^{u}\right\}_{m=1}^{M}$ and $\left\{Y_{m}^{v}\right\}_{m=1}^{M}$, the Gamma hyperprior parameters $\alpha$ and $\beta$ (that are set to 1 in our implementation), and the number of epochs $T$. First, the parameters for each $q(z), z \in \boldsymbol{\theta}$ are initialized. Specifically, for normal variables, we sample the mean from the standard multivariate normal distribution and set the precision to the identity matrix. Both the


[^0]:    ${ }^{1}$ In our experiments, we did not observe any degradation while using diagonal precision matrices instead of full precision matrices.

Algorithm 1 Partition Algorithm
Input: $A$ - set of variables in a graph
Output: $\left\{Y_{m}\right\}_{m=1}^{M}$ - A partition of $A$ to $M$ distinct sets
$M \leftarrow 1, W \leftarrow \emptyset, S_{r} \leftarrow \emptyset$
$S \leftarrow$ all leaf variables in $A$
while $S \neq \emptyset$ do
$Y_{M} \leftarrow S$
$W \leftarrow W \cup S$
$S \leftarrow S_{r}$
$S_{r} \leftarrow \emptyset, S_{c} \leftarrow \emptyset$
for $n$ in $Y_{M}$ do
$S \leftarrow S \cup \mathcal{P}(n) \quad \# \mathcal{P}(n)$ are the parents of $n$
end for
for $n$ in $S$ do
if $n \in W$ then
$S \leftarrow S \backslash\{n\}$
else if $\mathcal{C}(n) \cap S_{c} \neq \emptyset$ then $\# \mathcal{C}(n)$ are the children of $n$
$S \leftarrow S \backslash\{n\}$
$S_{r} \leftarrow S_{r} \cup\{n\}$
else
$S_{c} \leftarrow S_{c} \cup \mathcal{C}(n)$
end if
$S \leftarrow S \backslash \mathcal{P}(n)$
end for
$M \leftarrow M+1$
end while
return $\left\{Y_{m}\right\}_{m=1}^{M}$
shape and rate parameters of the Gamma variables were initialized to 1 . At every epoch, each $q(z), z \in \boldsymbol{\theta}$ is being updated once (the computation depends on the dependencies that are dictated by in the update equations). The partition to independent sets (Alg. 1), allows easy parallelism of the updates of each group of variables. Note that the variational parameters $\xi_{i j}$ and $\xi_{i j}^{k}$ are computed on-the-fly when needed. In our experiments, Alg. 2 converged after 30-40 epochs, depending on the dataset.

### 3.5.2 Approximate Bayesian Inference.

Once Alg. 2 converged, we approximate the posterior predictive integral from Eq. 8 by:

$$
\begin{aligned}
p\left(d_{i j}=1 \mid \mathcal{D}, \mathcal{H}\right) & \approx \int \sigma\left(\mathbf{u}_{i}^{T} \mathbf{v}_{j}+b_{j}\right) q\left(\mathbf{u}_{i}\right) q\left(\mathbf{v}_{j}\right) q\left(b_{j}\right) d \mathbf{u}_{i} d \mathbf{v}_{j} d b_{j} \\
& \approx \int \sigma(x) \mathcal{N}\left(x ; \mu_{x}, \sigma_{x}^{2}\right) d x \underset{(3)}{\approx} \sigma\left(\mu_{x} / \sqrt{1+\pi \sigma_{x}^{2} / 8}\right)
\end{aligned}
$$

Equation 23 presents three approximations: approximation (1) is the VB approximation that replaces $p(\boldsymbol{\theta} \mid \mathcal{D}, \mathcal{H})$ with the fully factorized $q(\boldsymbol{\theta})$. Hence, each $z \in \boldsymbol{\theta} \backslash\left\{\mathbf{u}_{i}, \mathbf{v}_{j}, b_{j}\right\}$ is integrated out. Yet, we are still left with an intractable integral. Therefore, we propose to approximate the distribution of $x=\mathbf{u}_{i}^{T} \mathbf{v}_{j}+b_{j}$ with a normal distribution (based on the first and second moments), which leads to approximation (2). The theoretical justification for this step is due to the Berry-Esseen Theorem [12] that places a bound on the error of a Gaussian approximation to the sum of independent variables. This bound is inversely proportional to the number of summands.

Algorithm 2 VBN Optimization
Input: $\left\{Y_{m}^{u}\right\}_{m=1}^{M},\left\{Y_{m}^{v}\right\}_{m=1}^{M}, \alpha, \beta, T$
Initiialize all the normal variables with an identity precision, and mean that is sampled from the standard normal distribution.
Initialize Gamma variables with shape and rate parameters equal to 1 .
for $n=1: T$ do
Sample $\mathcal{D}$ according to the description from Secs. 3.2 and 3.3
for $m=1: M$ do $\quad \# q\left(\mathbf{u}_{i}\right), q\left(\mathbf{h}_{i}^{u}\right)$ updates
Update all $q(y), y \in Y_{m}^{u}$, using Eqs. 16 and 17, in parallel
end for
Update all $q\left(\mathbf{v}_{i}\right), q\left(\mathbf{h}_{i}^{v}\right)$ by performing a symmetric version of Steps 5-7
for $m=1: \max \left(\left\{t_{k}\right\}\right)$ do
Update all $q\left(\mathbf{x}_{m k}\right), k\left\{1, \ldots, N_{R}\right\}$, using Eq. 15, in parallel
end for
Update all $q\left(\mathbf{y}_{m k}\right)$ by performing a symmetric version of Steps 9-11
Update all $q\left(b_{j}\right)$ and $q\left(\mathbf{r}_{j k}\right)$, in parallel, using Eqs. 18 and 19, respectively
Update all $q\left(\tau_{u_{i}}\right), q\left(\tau_{h_{i}^{u}}\right), q\left(\tau_{v_{i}}\right), q\left(\tau_{h_{i}^{v}}\right), q\left(\tau_{x_{m k}}\right)$, $q\left(\tau_{y_{m k}}\right) q\left(\tau_{b_{j}}\right), q\left(\tau_{r_{j k}}\right)$, in parallel, using Eqs. 20, 21, and 22 (and their symmetric versions)
end for

In our case, $\mathbf{u}_{i}^{T} \mathbf{v}_{j}+b_{j}$ is a sum of $t+1$ independent variables. Hence, as the dimension $t$ increases, the error induced by approximation (2) decreases (we refer the reader to Theorem 3.1 for further details). Finally, approximation (3) follows from [41].

Next, we justify approximation (2) in Eq: 23.
THEOREM 3.1. [12] Let $x_{1}, \ldots, x_{n}$ be independent random variables with $\mathbb{E}\left[x_{i}\right]=0, \mathbb{E}\left[x_{i}^{2}\right]=\sigma_{i}^{2}>0$, and $\mathbb{E}\left[\left|x_{i}\right|^{3}\right]=\rho_{i}<\infty$. Also, let $S_{n}=\frac{2 \pi_{n}}{\sqrt{\sum_{i=1}^{n} \sigma_{i}^{2}}}$. Denote $F_{n}$ and $\Phi$ the CDFs of $S_{n}$ and of the standard normal distribution, respectively. Then,

$$
\exists C>0 \forall n \in \mathbb{N}: \sup _{x \in \mathbb{R}}\left|F_{n}(x)-\Phi(x)\right| \leq \frac{M C}{\sqrt{\sum_{i=1}^{n} \sigma_{i}^{2}}}
$$

where $M=\max _{1 \leq i \leq n} \frac{\rho_{i}}{\sigma_{i}^{2}}$.
Therefore, as the number of summands $n$ increases, the maximal difference between $F_{n}$ and the standard normal CDF decreases. Denote $x=\mathbf{u}_{i}^{T} \mathbf{v}_{j}+b_{j}=b_{j}+\sum_{k=1}^{t} u_{i k} \sigma_{j k}$. While $b_{j}$ is a normal variable, each term $u_{i k} \sigma_{j k}$ in the summation is a product of normal variables and hence does not follow the normal distribution. Yet, this summation considers independent ${ }^{2}$ random variables that meet the conditions in Theorem $3.1^{3}$. Therefore, we approximate the density of $x$ with the normal PDF (according to its first and second moments). Empirically, we found that the histogram induced by a Monte-Carlo sampling from the true PDF of $x$ matches very closely

[^0]
[^0]:    ${ }^{2}$ As explained in Section 3.5, we consider diagonal precision matrices.
    ${ }^{3}$ While the inequality in Theorem 3.1 is stated with standardized variables, the bound on the absolute difference is not affected by a scaling factor nor by a shift.

its normal approximation for all $t>20$ (in our experiments we used $t=50$ ).

## 4 EXPERIMENTAL SETUP

In this section we describe the datasets, evaluation tasks, evaluated models, and hyperparameters configuration.

### 4.1 Datasets

Our evaluation covers NLU, recommender systems, and medical informatics datasets as follows:

NLU: The SemCor dataset [45] consists of 37,176 annotated sentences, with 820,411 words and a vocabulary size of 43,416 . The hierarchical and explicit relations were extracted from WordNet [44].

Recommender Systems: Two popular collaborative filtering datasets were used: MovieLens 25M [23] and Yahoo! Music [31], consisting of user-item ratings on a scale of [0-5] and [0-100] for movies and songs, respectively. For each dataset, we sampled a set of 4,000 items and 6,000 users. For every user, we considered movies (songs) that were ranked above 3.5 (80) as items that cooccur together. The movies and songs datasets further provide hierarchical information in the form of genres $\rightarrow$ director $\rightarrow$ movie and artist $\rightarrow$ album $\rightarrow$ song, respectively.

Medical Informatics: The MIMIC-III dataset [30] is based on patients admitted to intensive care units at a large tertiary care hospital. It is comprised of 13,000 diagnoses made for 46,520 patients. The diagnoses are labeled by ICD9 ${ }^{4}$ codes and the ICD9 classification index provides hierarchical information for these diagnoses.

### 4.2 Evaluated Models and Hyperparameter Configuration

For every dataset, we defined a unique held-out validation-set that was used to optimize the hyperparameters of each model. Our evaluation include the following models:

- VBN: Our model with a two-level hierarchy e.g., animal $\rightarrow$ $d o g \rightarrow$ Poodle (our experiments using single- or three-level hierarchies did not yield improvements). In the Yahoo! Music and the MovieLens datasets, the hierarchical information are as explained in Sec. 4.1. In the MIMIC-III medical dataset, we employed the ICD9 hierarchy over the entities taken from Wikipedia ${ }^{5}$. Unlike the NLU dataset, these datasets do not include explicit relations between entities. For the NLU dataset, hierarchical relations are based on hypernyms and troponyms, extracted from WordNet [43]. Explicit relations between entities had been extracted from WordNet as well. Specifically, the lexical-semantic relations utilized in our experiments were antonymy and meronymy.
- SG and SG-R: The Skip-Gram with negative sampling method from [42], and its Retrofitted version (SG-R). As explained in Section 2, retrofitting [21] enables the incorporation of side information as a post-processing step, providing an alternative to VBN's mechanism for modeling hierarchical side-information.

[^0]- BSG and BSG-R: The Bayesian Skip-Gram model [2], and its Retrofitted version (BSG-R).
For all datasets and models, we found out that the optimal hyperparameter configuration is an embedding size of $t=50$, negative-to-positive ratio of 1 , and Gamma hyperprior parameters with $\alpha=\beta=1$. In our experiments, all models converged after 40-80 epochs, depending on the dataset characteristics (number of entities, number of interactions, etc.). Following convergence, we retrofitted the embeddings produced by SG and BSG using the post-processing procedure from [21] to produce SG-R and BSG-R.


### 4.3 Evaluation Tasks and Measures

We evaluated the quality of the learned representations across various tasks. For all the benchmarks, we considered $80 \% / 20 \%$ train/test split. Then, $15 \%$ of the train data was kept aside as validation data while the rest was used for training the model. Namely, the effective split consists of $68 \% / 12 \% / 20 \%$ train/validation/test. In what follows, we describe the evaluation tasks.
4.3.1 Inference Tasks. The models are evaluated on three inference tasks:

- Sentence Completion: In this task, the goal is to complete a masked word in a sentence. The test sentences are taken from the NLU dataset.
- Recommendations: We trained the models on a masked version of the datasets, where for each user two items were masked: The first masked item was randomly sampled from the user's list and the second masked item was the last item consumed by the user. Then, the task was to recommend the masked items for each user.
- Medical Inference: We masked the patients' diagnoses in the same manner as done for the recommendation task. Similarly, the task was to predict the correct (masked) diagnoses for each patient.
For inference tasks, the queries are the masked sequences. The sentences, users, and patients were represented by the average of their words, items, or diagnoses vectors (for SG) and random variables (for BSG and VBN). The score between a query and a candidate is computed by the cosine similarity for SG and by Eq. 23 for BSG and VBN.

The models' performance is evaluated according to the following measures:

- Hit-Rate at $\boldsymbol{k} \%$ (HR@ $\boldsymbol{k} \%$ ): This measure outputs 1 if the correct item to be retrieved is ranked in the top $k \%$ percentile, otherwise 0 . Then, the average HR@ $k \%$ score is taken across the test set examples.
- Mean Percentile Rank (MPR): This measure outputs 1 minus the percentile rank (PR) of the test example. The PR is the rank of the hidden item divided by the catalog size. The MPR score is the average of the PR scores for all the test set examples.
4.3.2 Word Similarity Tasks. We further evaluated the models on five word similarity datasets: WordSim-353 (WS) [22], Stanford's Contextual Word Similarities (SCWS) [27], Rare Words (RW) [40], MEN [17] and SimLex-999 (SL) [25]. Each dataset contains word pairs that are associated with human annotated similarity scores,


[^0]:    ${ }^{4}$ www.cdc.gov/nchs/icd/icd9.htm
    ${ }^{5}$ en.wikipedia.org/wiki/List_of_ICD-9_codes

Table 1: HR@10\% and MPR results for inference tasks.


considered as ground truth. The model's performance is evaluated based on the Spearman's correlation between the ground truth scores and the scores produced by the models.

## 5 RESULTS

In this section we provide the experimental results as well as a qualitative analysis for assessing the performance advantages of our VBN model.

### 5.1 Inference Tasks

Table 1 presents the HR@10\%, and MPR values, for each combination of a model and a dataset. We consider two test sets: the original test set, 'Full', and the 'Rare' dataset, comprising the $20 \%$ least frequent entities. We can observe that VBN outperforms all baselines across all datasets. This showcases the importance of 1) Modeling external taxonomy information: VBN outperforms all baselines that do not utilize taxonomy (BSG and SG) and 2) Bayesian treatment: VBN outperforms SG and SG-R. In the same manner, BSG improves upon SG which demonstrates the merit of the Bayesian approach over simple point estimate solutions ( $\mathrm{BSG}>\mathrm{SG}$ ). Finally, VBN outperforms the other methods over long-tail entities (the 'Rare' catalog), where the gap between VBN and the other baselines becomes even more significant. These results demonstrate the ability of VBN to provide better modeling for entities in the long-tail.

### 5.2 Word Similarity

Table 2 presents the word similarity results ${ }^{6}$. The last column depicts the average across all datasets. The best performing results are boldfaced, and evidently, VBN outperforms other methods across all datasets. The retrofitting stage improves both SG and BSG, which indicates the effectiveness of incorporating lexical knowledge into the word representations. Nonetheless, BSG surpasses SG with or

[^0]Table 2: Word similarity evaluation results.


Table 3: Antonym learning evaluation.


without retrofitting, which demonstrates the merits of Bayesian modeling. Importantly, VBN outperforms both BSG-R and SG-R indicating the benefit of learning relational knowledge during training rather than as a post-processing step. Finally, we can observe that in the case of rare words, the gap between VBN and the other models' performances increases.

### 5.3 Learning Explicit Relations

Recall that VBN explicitly models relations of entities. We evaluate this capability by extracting opposites (antonyms) pairs from WordNet. We split the antonyms in the Brown dataset to 3,279 and 1,094 train and test pairs, respectively. Given a query word $i$, we rank a candidate word $j$ by $p\left(g_{i j}^{\text {opp }}=1 \mid \mathcal{D}, \mathcal{H}\right)$, where the predictive probabilities are computed using the application of the approximation from Eq. 23 to $p\left(g_{i j}^{\text {opp }}=1 \mid \mathcal{D}, \mathcal{H}\right)$.

In order to quantify the contribution from modeling explicit relations, we further consider an ablated version of VBN without the explicit relations component. To this end, we simply omit the terms that account for the explicit relations from the joint loglikelihood. Then, we rank a candidate word $j$ by $p\left(d_{i j}=1 \mid \mathcal{D}, \mathcal{H}\right)$.

Table 3 presents the MPR and HR@k\% results. As expected, incorporating the information from explicit relations during training (VBN) leads to significantly better w.r.t the ablated version of VBN (VBN w/o relations) where explicit relations were not modeled directly.

### 5.4 Qualitative Analysis

In what follows, we provide a qualitative assessment of the contribution from each component of VBN.


[^0]:    ${ }^{6}$ These results are sub-optimal compared to those reported in previous word embedding works (e.g., [48]) due to the use of a significantly smaller corpus.

Table 4: Most similar words to lemma ('Words' section) and most similar movies to Zoolander 2 ('Movies' section). TSLWM stands for "The Secret Life of Walter Mitty".


Hierarchical Relations: The word lemma appears only once in our corpus, co-occurring only with the word now. Thus, it exemplifies a rare word from the "long-tail". Table 4 (left) presents the four most similar words to lemma suggested by SG (using the cosine similarity), BSG, and VBN (using Eq. 23). According to WordNet, the parent of lemma is proposition, which is also the parent for theorem (a more frequent word than lemma). As can be seen in Tab. 4 ('Words' section), VBN suggests mathematical terms that better fit with lemma, even though they never co-occurred with lemma during training. Both BSG and SG, which do not utilize external information, suggest unrelated words. Moreover, the SG model is based on a point estimate solution, hence overconfident in its prediction, and ends up with (incorrectly) suggesting now as the closest word to lemma.

The same phenomenon is observed in the Movielens dataset. Here, only a single user watched both Zoolander 2 and The Texas Chainsaw Massacre (TCM). Zoolander 2 is a cold movie since it appears only once in the dataset (co-occurring only with TCM). Further, note that Zoolander 2 was directed by Ben Stiller. In Tab. 4 (right), we see that all the recommended movies according to VBN are also Ben Stiller's movies, which exemplifies VBN's utilization of side information. Notably, the SG model promotes TCM which is (arguably) not related to Zoolander 2.

Bayesian Treatment: Next, we show the model's ability to account for uncertainty in the target entity to be ranked. Table 6 depicts the percentile rank (PR) of lemma and Zoolander 2 w.r.t. now and TCM, respectively. Note that in contrast to Table 4, this time, the "rare" items are the target items. Evidently, the PR in VBN and BSG is low (close to random ranking) due to the high variance of the target entities. SG is overconfident and ranks both irrelevant entities in the top $1 \%$ and $4 \%$, respectively.

Explicit Relations: As detailed in Sec. 3.3, the VBN explicitly models relations between entities. Following the experiment from Sec. 5.3, we present a qualitative example that demonstrates the merits of this capability. To this end, we consider the following pair of opposites (antonyms)- lowest and highest. We rank the words in the entire catalog w.r.t. lowest, once according to $p\left(g_{i j}^{\text {opp }}=1 \mid \mathcal{D}, \mathcal{H}\right)$

Table 5: Top 5 words retrieved for the query lowest.


Table 6: Percentile Rank (PR) of entity Y w.r.t. entity X.


(VBN) once according to $p\left(d_{i j}=1 \mid \mathcal{D}, \mathcal{H}\right)$ (which is computed based on the ablated version: VBN w/o relations).

Table 5 presents the top-5 words retrieved by both methods for the query lowest. VBN ranks the word highest in second place, while in the case of VBN w/o relations, highest does not appear in the top 5 suggestions. Moreover, based on the co-occurrence data $d_{i j}$, VBN w/o relations undesirably promotes the word low.

## 6 CONCLUSION

We presented VBN - a novel Bayesian model for effective representation learning in the long-tail, and small data scenarios. VBN introduces three complementary techniques: 1) Informative priors based on external hierarchical relations (e.g., taxonomy). 2) Explicit relational representations that enforce structure and consistency between entities that share a semantic relationship. 3) A tractable yet scalable VB optimization algorithm, followed by an analytical approximation to the posterior predictive integral, leading to a fast Bayesian inference. Extensive empirical evaluations on a variety of datasets and tasks show that VBN produces better representations than other methods in small data scenarios, and especially for long-tail entities.

In the future, we plan to expand the modeling of entities to multimodal distributions (e.g., Gaussian Mixture Models), and investigate the utilization of deep neural networks for incorporating further information sources (e.g., visual and audio signals) as priors.

## 7 BROADER IMPACT

Neural embedding methods have been introduced several years ago as a standard building block for many tasks in NLP and recommender systems, e.g., semantic similarity and collaborative filtering, etc. As such, these models play a substantial role in the AI revolution we are witnessing today.

Representation learning models are trained in a self-supervised fashion using large tabular (or textual) datasets. However, rare entities that suffer from insufficient statistics, are often poorly represented. As a result, the respective tasks often show inferior results in the "long-tail". One common mitigation, especially in language models, is to constantly increase training dataset size in the hope

to gain more statistics for rare entities. However, aside from language models, this mitigation is mostly not applicable in other domains where datasets are limited and cannot be extended, e.g., in recommendation systems or medical informatics. Additionally, this challenge frequently arises when learning representations in propriety datasets.

In this work, we proposed a Bayesian framework that allows utilizing side information (via external resources) and achieves superior representations for rare entities. Encouraged by the model's results and our experience working with it, we genuinely predicate that this work pose a significant contribution within the scope of the aforementioned challenges. Therefore, we believe the NLP, recommender systems, medical informatics communities, and others can all benefit from the presented model, and consider it as an elegant and effective way for modeling entities, especially when learning representations in the long-tail. Nevertheless, we humbly prefer to refrain from proclaiming broad declarations about its future "societal consequences".

As to the ethical aspects of our work, we consider it similar to many other machine learning algorithms which can be seen as benign tools to be used for "good" or "bad" depending on the practitioner. As an exemplary use-case, we demonstrated successful entity representation learning of rare diagnoses that has the potential to be applied by health professionals to improve the wellbeing of others. It is the opinion of the authors, that as a general rule, most scientific contributions, such as the one made in this paper, have a positive impact in advancing humanity's technological achievements, even when the immediate impact is yet unknown.
