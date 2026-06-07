# Europe PMC Funders Group 

Author Manuscript
Expert Syst Appl. Author manuscript; available in PMC 2016 August 15.
Published in final edited form as:
Expert Syst Appl. 2016 August 15; 55: 361-373. doi:10.1016/j.eswa.2016.02.011.

## When and Where to Transfer for Bayes Net Parameter Learning

Yun Zhou ${ }^{\mathrm{a}, \mathrm{b}, *}$, Timothy M. Hospedales ${ }^{\mathrm{a}}$, and Norman Fenton ${ }^{\mathrm{a}}$<br>${ }^{a}$ Risk and Information Management (RIM) Research Group, Queen Mary University of London<br>${ }^{\mathrm{b}}$ Science and Technology on Information Systems Engineering Laboratory, National University of Defense Technology


#### Abstract

Learning Bayesian networks from scarce data is a major challenge in real-world applications where data are hard to acquire. Transfer learning techniques attempt to address this by leveraging data from different but related problems. For example, it may be possible to exploit medical diagnosis data from a different country. A challenge with this approach is heterogeneous relatedness to the target, both within and across source networks. In this paper we introduce the Bayesian network parameter transfer learning (BNPTL) algorithm to reason about both network and fragment (sub-graph) relatedness. BNPTL addresses (i) how to find the most relevant source network and network fragments to transfer, and (ii) how to fuse source and target parameters in a robust way. In addition to improving target task performance, explicit reasoning allows us to diagnose network and fragment relatedness across BNs, even if latent variables are present, or if their state space is heterogeneous. This is important in some applications where relatedness itself is an output of interest. Experimental results demonstrate the superiority of BNPTL at various scarcities and source relevance levels compared to single task learning and other state-of-the-art parameter transfer methods. Moreover, we demonstrate successful application to real-world medical case studies.


## Keywords

Bayesian networks parameter learning; Transfer learning; Bayesian model comparison; Bayesian model averaging

## 1 Introduction

Bayesian networks have proven valuable in modeling uncertainty and supporting decision making in practice (Pearl, 1988; Fenton and Neil, 2012). However, in many applications it is hard to acquire sufficient examples to learn BNs effectively from data. For example, in a small hospital or country there may be insufficient data to learn an effective medical diagnosis network. However, directly applying a network learned in another domain may be inaccurate or impossible because the underlying tasks may have quantitative or qualitative differences (e.g., care procedures vary across hospitals and countries). In this paper we

[^0]
[^0]:    *Corresponding author yun.zhou@qmul.ac.uk (Yun Zhou), t.hospedales@qmul.ac.uk (Timothy M. Hospedales), n.fenton@qmul.ac.uk (Norman Fenton).

investigate leveraging BNs in different but related domains to assist learning a target task with scarce data. This is an important capability in at least two distinct scenarios: (i) those where the source tasks are the same as the target, but have different specific statistics (e.g., due to different demographic statistics in another country), and (ii) those where the source tasks are related to the target in a piecewise way, (the target and source tasks are not the same, but share common sub-graphs, e.g., two hospitals share a subset of procedures; or two diseases share a subset of symptoms).

The proposed contribution falls under the topical area of transfer learning (Torrey and Shavlik, 2009; Pan and Yang, 2010) (also known as domain adaptation), which aims to significantly reduce data requirements by leveraging data from related tasks. Transfer has been successfully applied in a variety of machine learning areas for example, recommendations (Pan et al., 2012), classification (Li et al., 2012; Ma et al., 2012) and natural language processing (Collobert and Weston, 2008). Central challenges include computing when to transfer (transfer or not depending on relevance), from where (which of multiple sources of varying relevance) (Eaton et al., 2008; Mihalkova and Mooney, 2009) and how (how to fuse source and target information). These are crucial to ensure that transfer is helpful, and avoid 'negative transfer' risk (Pan et al., 2012; Seah et al., 2013a). Despite the popularity of transfer learning, limited work (Luis et al., 2010; Niculescu-mizil and Caruana, 2007; Oyen and Lane, 2012) has been done on transfer learning of BNs. Outstanding challenges in BN transfer include dealing automatically with from where to transfer, transferring in the presence of latent variables and transferring between networks with heterogeneous state spaces. In this paper we introduce the first framework that resolves these issues in a BN context, leveraging the structured nature of BNs for piecewise transfer, so multiple sources of partial relevance and potentially heterogeneous state spaces can be exploited.

In this paper we assume the target and source domain structures are provided1 and concentrate on the challenges of learning the target network parameters in the presence of latent variables and from multiple sources of varying - continuous and/or piecewise relevance. Importantly, we do not require that the source and target networks correspond structurally, or that node names are shared. Our novel solution involves splitting the target and source BNs into fragments (sub-graphs) and then reasoning explicitly about both network-level and fragment-level relatedness. Reasoning simultaneously about both is important, because pure fragment-level relatedness risks over-fitting if there are many sources. We achieve this via an Expectation Maximization (EM) style algorithm that alternates between (i) performing a Bayesian model comparison to infer per-fragment relatedness and (ii) updating a source network relatedness prior. This solves when and from where to transfer at both coarse and fine-grained level. Finally, the actual transfer is performed per-fragment using Bayesian model averaging to robustly fuse the source and target fragments, addressing how and how much to transfer. In this way we can deal robustly with a variety of transfer scenarios including those where the source networks are: (i) highly relevant or totally irrelevant, (ii) have the same or heterogeneous state spaces and (iii)

[^0]
[^0]:    ${ }^{1}$ This is easiest to elicit from experts, and is moreover required in many domains such as medicine where the structure must be semantically meaningful to be acceptable to end users.

uniform or piecewise (varying per sub-graph) relevance. Our explicit network and fragment relatedness reasoning also provides a diagnostic of which networks/domains are similar, and which sub-graphs are common or distinct. This is itself an important output for applications where quantifying relatedness, and uncovering the source of heterogeneity between two domains is of interest (e.g., revealing differences in treatment statistics between hospitals). To evaluate our contribution, we conduct experiments on six standard networks from a BN repository, comparing against various single task baselines and prior transfer methods. Finally, we apply our method to transfer learning in two real-world medical networks.

## 2 Related Work

Expert Elicitation. An advantage of BNs is their interpretable nature means that experts can define variables, structure and parameters in the absence of data. Nevertheless, learning BNs from data is of interest because there are many situations for which there is no available expert judgment, or where it may not be possible to elicit the conditional probability tables (CPTs). Studies have therefore tried to bridge the gap between these two paradigms. Most typically, experts specify a semantically valid network structure, and CPTs are learned from data. Recently, expert specified qualitative constraints on CPTs have been exploited to improve parameter learning. This is done, for example, via establishing a constrained optimization problem (Altendorf, 2005; Niculescu et al. 2006; de Campos and Ji, 2008; Liao and Ji, 2009; de Campos et al. 2009) or auxiliary BNs (Khan et al. 2011; Zhou et al. 2014a,b). In this study we exploit the ability of experts to easily specify a network structure and focus on transfer to improve quantitative estimation of parameters.

CPTs combination. When there is limited training data, researchers have attempted to construct CPTs from different relevant sources of information. Given a set of CPTs involving the same variables, conventional methods to aggregate them are linear aggregation (i.e. weighted sum) and logarithmic aggregation (Genest and Zidek, 1986; Chang and Chen, 1996; Chen et al. 1996). Based on this, the work of (Luis et al. 2010) introduced the DBLP (distance based linear pooling) and LoLP (local linear pooling) aggregation methods by considering the CPTs' confidences and similarities learnt from the original datasets. This method highlighted the importance of measuring the weights/confidences of different CPTs. However, the method is a too simplistic heuristic: confidence values depend only on the CPT entry size and dataset size, without considering the fit to the target training data.

Transfer Learning. Transfer learning in general is now a well studied area, with a good survey provided by (Pan and Yang, 2010). Extensive work has been done on transfer and domain adaptation for flat machine learning models, including unsupervised transfer and analysis of relatedness (Duan et al. 2009; Seah et al. 2013b,a; Eaton et al. 2008). However, these studies have generally not addressed one or more of the important conditions that arise in the BN context addressed here, notably: transfer with heterogeneous state space, piecewise transfer from multiple sources (a different subset of variables/dimensions in each source may be relevant), and scarce unlabeled target data (thus precluding conventional strategies that assume ample unlabeled target data, such as MMD (Huang et al. 2007; Seah et al. 2013b)).

Expert Syst Appl. Author manuscript; available in PMC 2016 August 15.

Transfer Learning in BNs. In the context of transfer learning in BNs, the multi-task framework of (Niculescu-mizil and Caruana, 2007) considers structure transfer. However, it assumes that all sources are equally related and simply learns the parameters for each task independently. Kraisangka and Druzdzel (2014) construct BN parameters from a set of regression models used in survival analysis. However, this method cannot be generalized to transfer between BNs. The transfer framework of (Luis et al., 2010) covers a more similar parameter transfer problem to ours and proposes a method to fuse source and target data. However, the heuristic CPT fusion used assumes every source is both relevant and equally related. It is not robust to the possibility of irrelevant sources and does not systematically address when, from where, and how much to transfer (as shown by our experiments where this method significantly underperforms ours). The study (Oyen and Lane, 2012) considers multi-task structure learning, again with independently learned parameters. They investigate network/task-level relatedness, showing transfer performs poorly without knowledge of relatedness. However, they address this by using manually specified relatedness. Finally, a recent study (Oates et al., 2014) improves this by automatically inferring the network/tasklevel relatedness. However, they do not consider information sharing of parameters. In contrast, we explicitly learn about both network and fragment-level relatedness from data. None of these prior studies cover transfer with latent variables or heterogeneous state spaces.

A related area to BN transfer is transfer in Markov Logic Networks (MLNs) (Mihalkova et al., 2007; Davis and Domingos, 2009; Mihalkova and Mooney, 2009). In contrast to these studies, our approach has the following benefits: We can exploit multiple source networks rather than exactly on each; we automatically quantify source relevance and are robust to some or all irrelevant sources (rather than assuming a single relevant source); these MLN studies use the transferred clauses directly rather than weighting the resulting transfer by estimated relevance.

# 3 Model Overview 

### 3.1 Notation and Definitions

In a BN parameter learning setting, a domain $\mathcal{D}=\{V, G, D\}$ consists of three components: variables $V=\left\{X_{1}, X_{2}, X_{3}, \ldots, X_{n}\right\}$ corresponding to nodes of the BN , associated data $D$, and a directed acyclic graph $G$ encoding the statistical dependencies among the variables. The conditional probability table (CPT) associated with every variable specifies the probability $p\left(X_{i} \operatorname{pa}\left(X_{i}\right)\right)$ of each value given the instantiation of its parents as defined by graph $G$. Within a domain $\mathcal{D}$, the goal of parameter learning is to determine parameters for all $p\left(X_{i} \operatorname{pa}\left(X_{i}\right)\right)$. This is conventionally solved by maximum likelihood estimation (MLE) of CPT parameters $\theta, \hat{\theta}=\arg \max _{\theta} \log p(D \mid \theta)$. We denote this setting Single Task Learning (STL). The related notation in this paper are listed in Table 1.

In this paper, we have one target domain $\mathcal{D}^{t}$, and a set of sources $\left\{\mathscr{D}^{s}\right\}_{s=1}^{S}, S \geq 1$. The target domain and each source domain have training data $D^{t}=\left\{d_{1}^{s}, d_{2}^{s}, \ldots, d_{N}^{s}\right\}$ and $D^{s}=\left\{d_{1}^{s}, d_{2}^{s}, \ldots d_{M^{s}}^{s}\right\} \cdot$ For transfer learning we are interested in the case where target domain data is relatively scarce: $0<N \ll M^{s}$, and/or $N$ is small relative to the

dimensionality of the target problem $N \ll n^{2}$. Following the definition of transfer learning in (Pan and Yang, 2010), we define BN parameter transfer learning (BNPTL).

Definition 1 BNPTL. Given a set of source domains $\left\{\mathcal{D}^{s}\right\}$ and a target domain $\mathcal{D}^{t}$, BN parameter transfer learning aims to improve the parameter learning accuracy of the BN in $\mathcal{D}^{t}$ using the knowledge in $\left\{\mathcal{D}^{s}\right\}$.

This task corresponds to the problem of estimating the target domain CPTs $\theta^{t}$ given all the available domains:

$$
\hat{\theta}^{t}=\arg \max _{\theta^{t}} p\left(\theta^{t} \mid \mathscr{D}^{t},\left\{\mathscr{D}^{s}\right\}\right)
$$

If the networks correspond ( $V^{t}=V^{s}, G^{t}=G^{s}$ ) and relatedness is assumed, then this could be simple MAP or MLE with count-aggregation. In the more realistic case of $\mathcal{D}^{s} \neq \mathcal{D}^{t}$ due to different training data sets with different statistics and thus varying relatedness; and potentially heterogeneous state spaces $V$, then the problem is much harder. More specifically, we consider the case where dimensions/variables in each domain do not correspond $V_{x} \neq V_{t}$. They may be disjoint $V_{x} \cap V_{t}=\varnothing$, or partially overlap $V_{x} \cap V_{t} \neq \varnothing$. However any correspondence between them is not assumed given (variable names are not used). In the following we describe an algorithm to maximize Eq (1) by proxy.

# 3.2 BN Parameter Transfer Learning 

Typically, transfer learning methods calculate relatedness at domain or instance level granularity. However, in real-world applications, that relevance may vary within-domain such that different subsets of features/variables may be relevant to different source domains. In order to learn a target domain $\mathcal{D}^{t}$ leveraging sources $\left\{\mathcal{D}^{s}\right\}$ with piecewise relatedness, or heterogeneity $V^{t} \neq V^{s}$ and $G^{t} \neq G^{s}$, we transfer at the level of BN fragments.

Definition 2 BN fragment. A Bayesian network of domain $\mathcal{D}$ can be divided into a set of sub-graphs (denoted fragments) $\mathcal{D}=\left\{\mathcal{D}_{f}\right\}$ by considering the graph $G$. Each fragment $\mathcal{D}_{f}=$ $\left\{V_{f}, G_{f}, D_{f}\right\}$ is a single root node or a node $X_{j}$ with its direct parents $p a\left(X_{j}\right)$ in the original BN, and encodes a single CPT from the original BN. The number of fragments is the number of variables in the original BN.

To realize flexible BN parameter transfer, the target domain and source domains are all broken into fragments $\mathscr{D}^{t}=\left\{\mathscr{D}_{f}^{t}\right\}, \mathscr{D}^{s}=\left\{\left\{\mathscr{D}_{f}^{s}\right\}\right\}$. Assuming for now no latent variables in the target domain, then each fragment $j$ can be learned independently
$\hat{\theta}_{j}^{t}=\operatorname{argmax}_{\theta_{j}^{t}} p\left(\theta_{j}^{t} \mid \mathscr{D}_{j}^{t},\left\{\left\{\mathscr{D}_{f}^{s}\right\}\right\}\right)$. To leverage the bag of source domain fragments $\left\{\left\{\mathscr{D}_{f}^{s}\right\}\right\}$ in learning each $\theta_{j}^{t}$, we consider each source fragment $\mathscr{D}_{g}^{s}$ as potentially relevant. Specifically, for each target fragment, every source fragment is evaluated for relatedness and the best fragment mapping is chosen. Once the best source fragment is chosen for each target, a domain/network-level relatedness prior is re-estimated by summing the relatedness

of its fragments to the target. The knowledge from the best source fragment for each target is then fused according to its estimated relatedness.

To realize this strategy, four issues must be addressed: (1) which source fragments are transferable, (2) how to deal with variable name mapping, (3) how to quantify the relatedness of each transferrable source fragment in order to find the best one and (4) how to fuse the chosen source fragment. We next address each of these issues in turn:

Fragment Compatibility For a target fragment $j$ and putative source fragment $k$ with continuous sate spaces, we say they are compatible if they have the same structure. For fragments with discrete and finite state spaces, we say they are compatible if they have the same structure 2 and state space. That is, the same number of states and parents states3, so

$$
\operatorname{compatible}\left(G_{j}^{t}, G_{k}^{s}\right)=\left\{\begin{array}{c}
1 \quad \text { if } G_{j}^{t}=G_{k}^{s} \& \operatorname{dims}\left(\theta_{j}^{t}\right)=\operatorname{dims}\left(\theta_{k}^{s}\right) \\
0 \quad \text { otherwise }
\end{array}\right.
$$

This definition of compatibility could be further relaxed quite straightforwardly (e.g., allowing target states to aggregate multiple source states) at the expense of additional computational cost. However, while relaxing the condition of compatibility would improve the range of situations where transfer can be exploited, it would also increase the cost of the algorithm by increasing the number of allowed permutations, as well as decreasing robustness to negative transfer (by potentially allowing more 'false positive' transfers from irrelevant sources). This is an example of pervasive trade-off between maximum exploitable transfer and robustness to negative transfer (Torrey and Shavlik, 2009).

Fragment Permutation Mapping For two fragments $j$ and $k$ determined to be compatible, we still do not know the mapping between variable names. For example if $j$ has parents $[a, b]$ and $k$ has parents $[d, c]$, the correspondence could be $a-d, b-c$ or $b-d, a-c$. The function permutations $\left(G_{j}^{t}, G_{k}^{s}\right)$ returns an exhaustive list of possible mappings $P_{m}$ that map states of $k$ to states of $j$.

Here we provide an illustrative example of fragment-based parameter transfer: the target is a three node BN shown in the left part of Figure 1 (a), and the source is a eight node BN shown in the right part of Figure 1 (a). In Figure 1 (b), there are two source fragments ( $\left\{T^{s}\right.$, $\left.L^{s}, E^{s}\right\}$ and $\left.\left\{E^{s}, B^{s}, S^{s}\right\}\right)$ which are compatible with target fragment. Thus, there are four permutations of compatible source fragments (assuming binary parent nodes). All four of these options are then evaluated for fitness, and the best fragment and permutation is picked (shown with dashed triangle in Figure 1 (b)). Finally, this selected fragment and permutation will be fused with target fragment via our fusion function.

[^0]
[^0]:    ${ }^{2}$ Note, that transfer at the level of compatible edges rather than fragments is based on the ICI (Independence of Causal In uences) assumption, and would be a straightforward extension of this algorithm. However we do not consider it here in order to constrain the computational complexity, and to avoid "by chance" false positive transfer matches that can lead to negative transfer. ${ }^{3}$ This assumes that the number of parameters is proportional to the number of rows in the conditional probability table, and no parametric dimension reduction is used.

We next discuss the more critical and challenging questions of how a particular target fragment $G_{j}$ and specific permuted source fragment $P_{m}\left(G_{k}^{s}\right)$ are evaluated for relevance, and how relevant sources are fused.

# 3.3 Fitness Function 

To measure the relatedness between compatible target and source fragments $\mathscr{D}_{j}^{t}$ and $\mathscr{D}_{k}^{s}$, we introduce a function fitness $\left(\mathscr{D}_{j}^{t}, \mathscr{D}_{k}^{s}, p\left(H^{s}\right)\right)$, where $p\left(H^{s}\right)$ is a domain-level relatedness prior. Here we consider a discrete random variable indexing the related source $s$ among $S$ possible sources. So $p\left(H^{s}\right)$ is a $S$-dimensional multinomial distribution encoding the relatedness prior. In this section, for notational simplicity we will use $t$ and $s$ to represent the $j$ th target and $k$ th source domain fragments under consideration.

A systematic and robust way to compare source and target fragments for relevance is to compute the probability that the source and target data share a common CPT (hypothesis4 $H_{1}^{s}$ ) versus having distinct CPTs (hypothesis $H_{0}^{s}$ ). This idea was originally proposed in a recent work (Zhou et al., 2015), which is called as Bayes model comparison (BMC) for hypotheses $H^{s} \in\left\{H_{1}^{s}, H_{0}^{s}\right\}$ is:

$$
p\left(H_{1}^{s} \mid D^{s}, D^{t}\right) \propto \int p\left(D^{t} \mid \theta\right) p\left(\theta \mid D^{s}, H_{1}^{s}\right) p\left(H_{1}^{s}\right) d \theta, p\left(H_{0}^{s} \mid D^{s}, D^{t}\right) \propto \int p\left(D^{t} \mid \theta^{t}\right) p\left(\theta^{t} \mid H_{0}^{s}\right) p\left(H_{0}^{s}\right) d \theta^{t}
$$

where we have made the following conditional independence assumptions: $D^{s} \perp H_{1}^{s}$, $D^{t} \perp\left\{D^{s}, H_{1}^{s}\right\} \mid \theta$ and $\theta^{t} \perp D^{s}, H_{0}^{s}$.

For discrete likelihoods $p(D \mid \theta)$ and Dirichlet priors $p(\theta \mid H^{s})$, integrating over

## Algorithm 1: BNPTL

INPUT : Target domain $\mathcal{D}^{t}$, Sources $\left\{\mathcal{D}^{s}\right\}$
OUTPUT: $\theta^{t}=\left\{\theta_{j}^{t}\right\}$ and $p\left(H^{s}\right)$
1 Initialize the domain-level relatedness $p\left(H^{s}\right)$ (uniform);
2 repeat
3 for target fragment $j=1$ to $J$ do
4 for source network $s=1$ to $S$ and fragment $k=1$ to $K$ do
5 if compatible $\left(G_{j}^{t}, G_{k}^{s}\right)$ then
$6 \quad P=$ permutations $\left(\mathscr{D}_{k}^{s}\right)$
${ }^{4}$ Consistent with the simplification of fragment notation, here $H_{1}^{s}$ only refers the dependent hypothesis between $\mathscr{D}_{j}^{t}$ and $\mathscr{D}_{k}^{s}$.

7 for permutation $m=1$ to $M$ do
8 measure relatedness:

$$
\begin{gathered}
\operatorname{fitness}\left(\mathscr{D}_{j}^{t}, P_{m}^{s k}\left(\mathscr{D}_{k}^{s}\right), p\left(H^{s}\right)\right)= \\
p\left(H_{j k 1}^{s} \mid D_{j}^{t}, P_{m}^{s k}\left(D_{k}^{s}\right)\right)
\end{gathered}
$$

9 end
10 end
11 end
12 end
13 for source network $s=1$ to $S$ do
14 Re-estimate network relevance: $p\left(H^{s}\right) \propto \sum_{j k} p\left(H_{j k}^{s} \mid D_{j}^{t}, D_{k}^{s}\right)$;
15 end
16 until convergence;
17 for target fragment $j=1$ to $J$ do
18 Find the best source and permutation:

$$
k^{\prime}, s^{\prime}, m^{\prime}=\operatorname{argmax}_{k, s, m} p\left(H_{j k 1}^{s} \mid D_{j}^{t}, P_{m}^{s k}\left(D_{k}^{s}\right)\right)
$$

19

$$
\theta_{j}^{t}=\operatorname{fusion}\left(\mathbf{D}_{j}^{t}, P_{m}^{s^{\prime} k^{\prime}}\left(\mathbf{D}_{k^{\prime}}^{s^{\prime}}\right)\right)
$$

20 end
21 return $\theta^{t}=\left\{\theta_{j}^{t}\right\}$ and $p\left(H^{s}\right)$
the unknown CPTs $\theta$, the required marginal likelihood is the Dirichlet compound multinomial (DCM) or multi-variate Polya distribution:

$$
p\left(D^{t} \mid D^{s}, H_{1}^{s}\right)=\frac{\Gamma\left(A^{X^{s}}\right)}{\Gamma\left(N^{X^{t}}+A^{X^{s}}\right)} \prod_{c=1}^{C} \frac{\Gamma\left(n_{c}^{X^{t}}+\alpha_{c}^{X^{s}}\right)}{\Gamma\left(\alpha_{c}^{X^{s}}\right)}
$$

where $c=1 \ldots C$ index variable states, $n_{c}^{X^{t}}$ is the number of observations of the $c$ th target parameter value in data $D^{t}$, and $N^{X^{t}}=\sum_{c} n_{c}^{X^{t}} ; \alpha_{c}^{X^{s}}$ indicates the aggregate counts from the source domain and distribution prior, and $A^{X^{s}}=\sum_{c} \alpha_{c}^{X^{s}}$.

Maximal fitness $(\cdot)$ is achieved when the target data are most likely to share the same generating distribution as the source data. As we can see, previously proposed fitness function (Zhou et al., 2015) only addresses discrete data with Dirichlet conjugate priors. In

this paper, we derive the analogous computations for continuous data with Gaussian likelihood with Normal-Inverse-Gamma conjugate priors.

$$
p\left(D^{t} \mid D^{s}, H_{1}^{s}\right)=\prod_{i=1}^{N}\left(\frac{1}{\sqrt{\pi}} \frac{\Gamma\left(\frac{2 \alpha_{m}+1}{2}\right)}{\Gamma\left(\frac{2 \alpha_{m}}{2}\right)} \sqrt{\frac{\Lambda}{2 \alpha_{m}}}\left(1+\frac{\Lambda\left(d_{i}^{t}-\mu_{m}\right)^{2}}{2 \alpha_{m}}\right)^{-\left(\frac{2 \alpha_{m}+1}{2}\right)}\right)
$$

where $\Lambda=\frac{\alpha_{m} k_{m}}{\beta_{m}\left(k_{m}+1\right)}$; the hyperparameters $\mu_{m}, k_{m}, \alpha_{m}$ and $\beta_{m}$ are updated based on the source data $D_{k}^{s}$, which contains $M$ samples with center at $\overline{d^{*}}$ :

$$
\left\{\begin{array}{c}
\mu_{m}=\frac{k_{0} \mu_{0}+M \overline{d^{*}}}{k_{0}+M} \\
k_{m}=k_{0}+M \\
\alpha_{m}=\alpha_{0}+\frac{M}{2} \\
\beta_{m}=\beta_{0}+\frac{1}{2} \sum_{i=1}^{M}\left(d_{i}^{s}-\overline{d^{*}}\right)^{2}+\frac{k_{0} M\left(\overline{d^{*}}-\mu_{0}\right)^{2}}{2\left(k_{0}+M\right)}
\end{array}\right.
$$

Transfer Prior: The final outstanding component of BMC is how to define the transfer prior $p\left(H^{s}\right)$. We assume that transfer is equally likely a priori within a given source domain, but that different source domains may have different prior relatedness. Thus we set the transfer prior for a particular fragment pair to the prior for the corresponding source network, i.e., $p\left(H_{j k 1}^{s}\right)=p\left(H^{s}\right)$. The fragment transfer prior $p\left(H_{j k}^{s}\right)$ is then normalised as $p\left(H_{j k 0}^{s}\right)=1-p\left(H_{j k 1}^{s}\right)$.

# 3.4 Fusion Function 

Once the best source fragment $\mathscr{D}_{k}^{s}$ is found for a given target fragment $\mathscr{D}_{t}^{t}$, the next challenge is how to optimally fuse them. Our solution (denoted BMA) is to infer the target CPT, integrating over uncertainty about whether the selected source fragment is indeed relevant or not (i.e., if they share parameters or not $-H_{1}^{s}$ and $H_{0}^{s}$ in last section).

We perform Bayesian model averaging, summing over these possibilities. Specifically, we ask $p\left(\theta^{t} \mid D^{t}, D^{s}\right)=\sum_{H^{s}} p\left(\theta^{t}, H^{s} \mid D^{t}, D^{s}\right)$ which turns out to be:
$p\left(\theta^{t} \mid D^{t}, D^{s}\right)=p\left(H_{1}^{s} \mid D^{t}, D^{s}\right) \operatorname{Dir}\left(\theta ; \alpha+N^{X^{t}}+N^{X^{s}}\right)+p\left(H_{0}^{s} \mid D^{t}, D^{s}\right) \operatorname{Dir}\left(\theta ; \alpha+N^{X^{t}}\right)$
where $p\left(H^{s} \mid D^{t}, D^{s}\right)$ comes from Eq (2). This means the strength of fusion is automatically calibrated by the estimated relevance. Since there is no closed form solution for the sum of Dirichlets, we approximate Eq (6) by moment matching. For conditional Gaussian nodes, the weighted sum is also approximated by moment matching.

Moment matching (also known as Assumed Density Filtering (ADF)) is to approximate a mixture such as Eq (6) by a single distribution whose mean and variance is set to the mean and variance of the weighted sum. The estimated relatedness provides the weights $w_{1}=p\left(H_{1}^{s} \mid D^{t}, D^{s}\right), w_{0}=p\left(H_{0}^{s} \mid D^{t}, D^{s}\right)$. Assuming the posterior mean and variance of the parameters in the related and unrelated condition are $u_{1}, v_{1}$ and $u_{0}, v_{0}$ respectively. Then the approximate posterior mean is $u=w_{1} u_{1}+w_{0} u_{0}$, and variance is $v=w_{1}\left(v_{1}+\left(u_{1}-u\right)^{2}+\right.$ $\left.w_{0}\left(u_{0}-u\right)^{2} \text { (Murphy, 2012). For Gaussian distributions we can use this directly. For }\right.$ Dirichlet distributions with parameter vector $\alpha$, the variance parameter ${ }^{\mathrm{c}}=1 / \sum \alpha$, and the mean parameter vector is $u=v \alpha$.

# 3.5 Algorithm Overview 

An overview of our BNPTL framework is given in Algorithm 1. Each target fragment is compared to all permutations of compatible source fragments and evaluated for relevance using BMC fitness. The most relevant source fragment and permutation is assigned to each target fragment. The network-level relevance prior is re-estimated based on aggregating the inferred fragment relevance for that source: $p\left(H^{s}\right) \propto \sum_{j k} p\left(H_{j k}^{s} \mid \mathscr{D}_{j}^{t}, \mathscr{D}_{k}^{s}\right)$. This way of updating the source network prior reflects the inductive bias that fragment should be transferred from fewer distinct sources, or that a source network that has already produced many relevant fragments is more likely to produce further relevant fragments and should be preferred.

Finally, the most relevant source fragment for each target is fused using BMA. If there are missing or hidden data in the target domain, we start by running the standard EM algorithm in the target domain, to infer the states of each hidden variable. We use these expected counts to fill in $D^{t}$ when applying BNPTL.

Properties. Our BNPTL has a few favorable properties worth noting: (i) If there is no related source fragment, then the most related source fragment will have estimated relatedness near zero and no transfer is performed $\left(p\left(H_{1}^{s} \mid D^{t}, D^{s}\right) \approx 0\right.$ in Eq (6)). This provides some robustness to irrelevant sources (as explored in Section 4.7-4.8). (ii) Although we rely on an EM procedure to estimate fragment and source relatedness, starting from a uniform prior $p\left(H^{s}\right)$, our algorithm is deterministic and we use only one run to get results, (iii) Explicitly reasoning about both fragment and network level relatedness allows the exploitation of heterogeneous relevance both within and across source domains.

Computational Complexity. The computational complexity of this algorithm lies in the total number of relatedness estimates. We treat a relatedness calculation as an elementary operation $O(1)$. Assuming there are $J$ target fragments, $S^{\prime}$ compatible source fragments (typically much less than total number of source fragments $S$ ), and each fragment has $v$ parent nodes. Then the time complexity of each EM iteration in BNPTL is: $O\left(J S^{\prime} v!\right)$. Where $v$ ! is the total number of permutations searched to transfer a compatible fragment pair. In practice it always converged in 10-30 EM iterations. For example, I took 0.47 seconds to process Asia network (see Table 4, row 7) on our computer (Intel core i7 CPU 2.5 GHz ).

# 4 Experiments 

We first evaluate transfer learning on 6 standard networks from the BN repository5 before proceeding to real medical case studies. Details and descriptions of these BNs can be found in Table 2

### 4.1 Baselines

We compare against existing strategies for estimating relatedness and fusing source and target data. For relatedness estimation, we introduce two alternative fitness functions to BMC:

Likelihood: The similarity between the fragments is the log-likelihood of the target data under the ML source parameters $\hat{\theta}^{*}, \sum_{i} \log p\left(d_{i}^{t} \mid \hat{\theta}^{*}\right)$.

MatchCPT: The dis-similarity between the fragments is the K-L divergence between their ML parameter estimates $\mathscr{K} \mathscr{L} \mathscr{D}\left(\hat{\theta}^{*}, \hat{\theta}^{*}\right)$ (Dai et al., 2007; Selen and Jaime, 2011; Luis et al., 2010).

For fusing source and target knowledge, we introduce two competitors to our BMA:

Basic: Use the estimated source parameter directly $\hat{\theta}_{j}^{*}$. A reasonable strategy if relevance is perfect and the source data volume is high, but does not exploit target data and it is not robust to imperfect relevance.

Aggregation: A weighted sum reflecting the relative volume of source and target data (Eq (12) in (Luis et al., 2010)), it exploits both source and target data, but is less robust than BMC to varying relevance.

Neither Basic nor Aggregation is robust to varying relevance across and within sources (they do not reflect the goodness of fit between source and target), or situations in which no source node at all is relevant (e.g., given partial overlap of the source and target domain).

The algorithms implemented in MATLAB are based on functions and subroutines from the BNT6 and FastfitLightspeed toolboxes. All the experiments were performed on an Intel core i7 CPU running at 2.5 GHz and 16 GB RAM.

### 4.2 Overview of Relatedness Contexts

Before presenting experimental results, we first highlight the variety of possible networkrelatedness contexts that may occur. Of these, different relatedness scenarios may be appropriate depending on the particular application area.

Structure and Variable Correspondence: In some applications, the source and target networks may be known to correspond in structure, share the same variable names, or have

[^0]
[^0]:    5 http://www.bnlearn.com/bnrepository/
    6
    https://bnt.googlecode.com/
    ${ }^{7}$ http://research.microsoft.com/en-us/um/people/minka/software/lightspeed/

provided variable name mappings. In this case the only ambiguity in transfer is which of multiple potential source networks is the most relevant to a target. Alternatively, structure/ variable name correspondence may not be given. In this case there is also ambiguity about which fragment within each source is relevant to a particular target CPT.

Cross-network relevance heterogeneity: There may be multiple potential source networks, some of which may be relevant and others irrelevant. The most relevant source should be identified for transfer, and irrelevant sources ignored.

Continuous versus discontinuous relevance: When there are multiple potential source networks, it may be that relevance to the target varies continuously (e.g., if each network represents a slightly different segment of demographic of the population), or it may be that across all the sources some some are fully relevant and others totally irrelevant. In the latter case it is particularly important not to select an irrelevant source, as significant negative transfer is then likely.

Piecewise Relevance: Relevance may vary piecewise within networks as well as across networks. Consider a target network with two sub-graphs A and B: A may be relevant to a fragment in source 1, and B may be relevant to a fragment in source 2. For example, in the case of networks for hospital decision support, different hospitals may share different subsets of procedures - so their BNs may correspond in a piecewise way only. A target hospital network may then ideally draw from multiple sources. Note that this may happen either because (i) subgraphs in the target are structurally compatible with different subgraphs in the multiple sources (which need not be structurally equivalent to each other), or (ii) in terms of quantitative CPT fit, fragments in the target may each be better fit to different sources.

Our BNPTL framework aims to be robust to all the identified variations in network relatedness. In the following experiments, we will evaluate BN transfer in each of these cases.

# 4.3 Transfer with Known Correspondences 

In this section, we first evaluate transfer in the simplest setting, where structure/variable name correspondence is assumed to be given. This setting is same as (Luis et al., 2010): the transfer only happens between target/source nodes with the same node index $X_{i}^{t}=X_{i}^{s}$, where $X_{i}^{t} \in V_{t}, X_{i}^{s} \in V_{s}$ and $V_{t} \equiv V_{s}, G_{t} \equiv G_{s}$. (In our framework this is easily modelled by providing the prior $p\left(H_{j k 1}^{s}\right)=0$, and hence $p\left(H_{j k 0}^{s}\right)=1$, for non-corresponding pairs $j \neq k$.) This setting has the least risk of negative transfer, because there is less chance of transferring from an irrelevant source CPT.

We use six standard BNs (Weather, Cancer, Asia, Insurance, Alarm and Hailfinder) to compare our approach (BMC fitness with BMA (BNPTL)) to the state-of-art (MatchCPT fitness with Aggregation fusion (CPTAgg) (Luis et al., 2010)). In this case we use "soft noise" to simulate continuously varying relatedness among a set of sources. The specific soft noise simulation procedure is as follows: For each reference BN three sets of samples are drawn with 200, 300 and 400 instances respectively. These sample sets are used to learn

three different source networks. Because the source networks are learned from varying numbers of samples, they will vary in degree of relatedness to the target, with the 400 and 200 sample networks being most and least related respectively. Subsequently, 100 samples of each source copy are drawn and used used as the actual source data. Because node correspondences are known in this experiment, another baseline is simply to aggregate all target and source data. This method is referred as ALL, and also will be compared. Results are quantified by average KLD between estimated and true CPTs. In each experiment we run 10 trials with random data samples and report the mean and standard deviation of the KLD.

The results are presented in Table 3, with the best result in bold, and statistically significant improvements of the best result over competitors indicated with asterisks * ( $p \leq 0.05$ ). Compared with CPTAgg, BNPTL achieves $60.9 \%$ average reduction of KLD compared to the ground truth. These results verify the greater effectiveness of BNPTL even in the known correspondence setting, where the assumptions of CPTAgg are not violated. To demonstrate the value of our network-level relevance prior $p\left(H^{b}\right)$, we also evaluate our framework without this prior (denoted BNPTL ${ }^{\text {ap }}$ ). The comparison between BNPTL and BNPTL ${ }^{\text {ap }}$ demonstrates that the network-level relevance does indeed improve transfer performance. In this case it helps the model to focus on the higher quality/more relevant 400-sample source domain: even if for a particular fragment a less relevant source domain may have seemed better from a local perspective.

The ALL baseline also achieves good results in Cancer and Weather networks. We attribute this to these being smaller BNs (node $\leq 5$ ), so all the source parameters are reasonably well constrained by the source samples used to learn them, and aggregating them all is beneficial. However in large BNs with more parameters, the difference between the 200 and 400 sample source networks becomes more significant, and it becomes important to select a good source instead of aggregating everything including the noisier less related sources. In real-world settings, we may not have node/structure correspondence. Thus we do not assume this information is available in all the following sections.

# 4.4 Dependence on Target Network Data Sparsity 

In this section, we explore the performance for varying number of target samples, focusing on the Asia and Alarm networks. Here the target and source domain are both generated from the Asia or Alarm networks, and the relatedness of the source domain varies (soft noise). For relatedness, we consider 2 conditions for the source domains: (i) two Asia/Alarm networks learned from 200 and 300 samples respectively, this results 16 source fragments in Asia network (Row 1 of Figure 2) and 74 source fragments in Alarm network (Row 3 of Figure 2), and (ii) three Asia/Alarm networks learned from 200, 300 and 400 samples respectively, this results 24 source fragments in Asia network (Row 2 of Figure 2) and 111 source fragments in Alarm network (Row 4 of Figure 2). The latter condition potentially contains stronger cues for transfer - if a good decision is made about which source network to transfer from. To unpack the effectiveness of our contributions, we investigate all combinations for different fitness methods and fusion methods under these settings.

In each sub chart of Figure 2, the x-axis denotes the number of target domain training instances, and the $y$-axis denotes the average KLD between estimated and true parameter

values. The blue line represents standard MLE learning, green denotes transfer by MatchCPT fitness, purple shows transfer with likelihood fitness, and red line the results using our BMC fitness function. The columns represent Basic (source only), Aggregation and BMA fusion. As we can see from the results, the performance of transfer methods with BMC fitness function improves with more source fragments, especially in Asia network. Furthermore, algorithms with our BMC fitness function (red) achieve the best results in almost all situations. Even the simple basic fusion method gets reasonable learning results (< 0.50) using the BMC fitness function to choose among the 24 source fragments in Asia network. Also, our BMA fusion (right column) significantly outperforms other fusion methods. For instance, when there are 16 source fragments in Asia network (top row), the average performance of BMC fitness function in BMA fusion increased $25.4 \%$ and $29.3 \%$ compared with the same fitness function in Basic fusion and Aggregation fusion settings. Although these margins decrease with increasing source fragments, our BNPTL (BMC +BMA) is generally best.

# 4.5 Illustration of Network and Fragment Relatedness Estimation 

To provide insight into how network and fragment relatedness is measured in BNPTL, we continue to use the Asia network and its three sources (soft noise). Network Relatedness: Figure 3 shows the estimated relatedness prior $p\left(H^{s}\right)$ for each source $s$ over EM iterations. As we can see the network-level relatedness converges after about 10 iterations, with the relatedness estimates being in order of the actual source relevance.

Fragment Relatedness: To visualize the inferred fragment relatedness, we record the estimated relatedness between every fragment in the target and every fragment in source 3 of the Asia network. This is plotted as a heat map in Figure 4(a), where the y-axis denotes the index of target fragment, and x-axis denotes the index of source fragment. Darker color indicates higher estimated relatedness $p\left(H_{j k 1}^{s} \mid \mathscr{D}_{j}^{t}, \mathscr{D}_{k}^{s}\right)$ between two fragments $j$ and $k$. Some incompatible source fragments have zero relatedness automatically. For each target fragment, the most related (darkest) source fragment is selected for BMA fusion. Although there is some uncertainty in the estimated relatedness (more than one dark cell per row), overall all but one target fragment selected the correct corresponding source fragment (Figure 4(b).

### 4.6 Robustness to Hidden Variables

In this section, we evaluate the algorithms on six standard BNs. We use the same sampled target and sources as in Table 3, but we introduce additional hidden variables in the target. We learn the target parameters by: conventional single task BN learning (EM with MLE), MatchCPT fitness with Aggregation fusion (CPTAgg) (Luis et al., 2010) (note that CPTAgg does not apply to latent variables, but we use their fitness and fusion functions in our framework), and our BNPTL. Three conditions are considered: (i) fully observed target data, (ii) small number of hidden variables and (iii) medium number of hidden variables. (In the hidden data conditions, the specified number of target network nodes are chosen uniformly at random on each trial, and considered to be unobserved, so the data for these nodes are not used.)

Table 4 summarises the average KLD per parameter. In summary, the transfer methods outperform conventional EM with MLE (STL) in all settings. Compared with the state-of-the-art CPTAgg, BNPTL also improves performance: improvement on 15 out of 18 experiments, with an average margin of $53.6 \%$ (the average reduction of KLD). Of the total set of individual target CPTs, $84.3 \%$ showed improvement in BNPTL over CPTAgg.

# 4.7 Exploiting Piecewise Source Relatedness 

Thus far, we simulated source relevance varying smoothly at the network level - all nodes within each source network were similarly relevant. So all fragments should typically be drawn from the source estimated to be most relevant. In contrast for this experiment, we investigate the situation where relatedness varies in a piecewise fashion. In this case, to effectively learn a target network, different fragments should be drawn from different source networks. This is a setting where transfer in Bayesian networks is significantly different from transfer in conventional flat machine learning models (Pan and Yang (2010)).

To simulate this setting, we initialise a source network pool with three copies of the network, before introducing piecewise "hard noise", so that some compatible fragments are related and others are totally unrelated. Specifically, we choose a portion ( $25 \%$ and $50 \%$ ) of each source network's CPTs uniformly at random and randomise them to make them irrelevant (by drawing each entry uniformly from $[0,1]$ and renormalizing). This creates a different subset of compatible but (un)related fragments in each network. Thus piecewise transfer using different fragments from different sources is essential to achieve good performance.

We consider two evaluation metrics here: the accuracy of the fragment selection - whether each target fragment selects a (i) corresponding and (ii) non-corrupted fragment in the source, and accuracy of the learned CPTs in the target domain. Table 5 presents the results, where our model consistently outperforms CPTAgg in Weather, Cancer and Asia networks. Although the fragment selection accuracy of BNPTL failed to outperform the CPTAgg in Insurance, Alarm and Hailfinder networks due to the greater data scarcities in their target networks, the general good performance (KLD) of BNPTL verifies that the framework still can exploit source domains with piecewise relevance. Meanwhile the fragment selection accuracy of BNPTL explains how this robustness is obtained (irrelevant fragments (Eq (2)) are not transferred (Eq (6))). In addition to verifying that our transfer framework can exploit different parts of different sources, this experiment demonstrates that it can further be used for diagnosing which fragments correspond or not (Eq (2)) across a target and a source which is itself of interest in many applications.

### 4.8 Robustness to Irrelevant Sources

The above experiments verify the effectiveness of our framework under conditions of varying source relatedness, but with homogeneous networks $V t=V s$. In this section we verify robustness to two extreme cases of partially and fully irrelevant heterogeneous sources.

Partially irrelevant In this setting, we use the same six networks from the BN repository, and consider each in turn as the target, and copies of all six networks as the source (thus five

are irrelevant and one is relevant). Therefore the majority of the potential source fragments come from 5 irrelevant domains. Table 6 presents the results of transfer learning in these conditions. We evaluate performance with two metrics: (i) percentage of fragments chosen from the correct source domain, and (ii) the usual KLD between the estimated and ground truth parameters in the target domain.

As shown in Table 6, our BNPTL clearly outperforms the previous state-of-the-art CPTAgg in each case. This experiment verifies that our framework is robust even to a majority of totally irrelevant source domains, and is achieved via explicit relatedness estimation $\left(p\left(H_{1}^{*}\right)\right)$ in Algorithm 1 and Eq (2)).

Fully irrelevant In this setting, we consider the extreme case where the source and target networks are totally different $G_{t} \neq G_{s}, V_{t} \cap V_{s}=\varnothing$. Note that since the source and target are apparently unrelated, it is not expected that positive transfer should typically be possible. The test is therefore primarily whether negative transfer (Pan and Yang, 2010) is successfully avoided in this situation where all source fragments may be irrelevant. Note that since the sources are totally heterogeneous, prior work CPTAgg (Luis et al., 2010) does not support this experiment. We therefore compare our algorithm to a variant using BMC fitness and Basic fusion function (denoted BMCBasic) and target network only STL.

The results are shown in Table 7, from which we make the following observations. (i) BNPTL is never noticeably worse than STL. This verifies that our framework is indeed robust to the extreme case of no relevant sources: $\left(p\left(H_{0}^{*} \mid D^{t}, D^{*}\right)\right.$ is correctly inferred in Eq (2), thus preventing negative transfer from taking place (Eq (6)). (ii) In some cases, BNPTL noticeably outperforms STL, demonstrating that our model is flexible enough to achieve positive transfer even in the case of fully heterogeneous state spaces. (iii) In contrast, BMCBasic is worse than STL overall demonstrating that these properties are unique to our approach.

# 5 Real Medical Case Studies 

The previous section demonstrated the effectiveness of our BNPTL under controlled data and relatedness conditions. In this section we explore its application to learn BN parameters of two medical networks, where the "true" relatedness is unknown, and data volume and relatedness reflect the conditions of real-world medical tasks.

The Indian Liver Patient (ILP) (Bache and Lichman, 2013) has 583 records about liver disease diagnosis based on 10 features. This dataset is publicly available. Because the BN structure for this dataset is not provided. We follow previous work (Friedman et al., 1997) to apply a naive BN structure for this classification problem. To enable transfer learning, this dataset is divided into 4 subsets/domains by grouping patient age, following common procedure in medical literature (Jain et al., 2000). To systematically evaluate transfer, we iteratively take each group in turn as the target, and all the others as potential sources.

The AUC (area under curve) for the target variable of interest is calculated. This is repeated for each of 100 random 2-fold cross-validation splits, and the results averaged (Table 8).

Here STL denotes single task learning from target domain data, ALL indicates the baseline of concatenating all the source and target data together before STL. Although we are primarily interested in the case of unknown correspondence, we investigate both the conditions of known and unknown target-source node correspondence (denoted by suffix KC and UC respectively). Note that the ALL baseline needs to know node correspondence, so should be compared with BNPTL (KC) for a fair comparison. The results show that predictive performance can be greatly improved by leveraging the source data. Our BNPTL (UC) outperforms STL and state-of-the-art transfer algorithm CPTAgg in each case. As we can see, ALL also achieves good performance based on the strong assumption of known correspondence. Nevertheless, it is still outperformed by our BNPTL (KC).

Trauma Care (TC) dataset (Yet et al. 2014) has a BN structure designed by trauma care specialists, and relates to procedures in hospital emergency rooms. The full details of the network and datasets are proprietary to the hospitals involved, however it contains 18 discrete variables (of which 3 are hidden) and 11 Gaussian variables. It is important because rapid and accurate identification of hidden risk factors and conditions modeled by the network are important to support doctors' decision making about treatments which reduce mortality rate (Karaolis et al. 2010). The relevance of this trauma model to our transfer algorithm is that there are two distinct datasets for this model. One dataset is composed primarily of data from a large inner city hospital with extensive data (1022 instances) and the second dataset is composed of data from a smaller hospital and city in another country (30 instances). The smaller hospital would like an effective decision support model. However, using their own data to learn the model would be insufficient, and using the large dataset directly may be sub-optimal due to (i) differences in statistics of injury types in and out of major cities city, (ii) differences in procedural details across the hospitals and (iii) differences in demographic statistics across the cities/countries.

We therefore apply our approach to adapt the TC BN from the inner city hospital to the small hospital. We perform cross-validation in the target domain of the small hospital, using half the instances (15) to train the transfer model, and half to evaluate the model. To evaluate the model we instantiate the evidence variables in the target domain test set, select one of the variables of interest (Death), and query this variable. AUC values are calculated for the query variable, and shown in Table 8. Every method is better than using the scarce target data only (STL). Our BNPTL significantly outperforms the alternatives in each case. BNPTL (UC) also matches the performance of BNPTL (KC) demonstrating the reliability of the fragment correspondence inference.

## 6 Conclusions

### 6.1 Summary

When data is scarce, BN learning is inaccurate. Our framework tackles this problem by leveraging a set of source BNs. By making an explicit inference about relatedness per domain and per fragment, we are able to perform robust and effective transfer even with heterogeneous state spaces and piecewise source relevance. Our approach applies with latent variables, and is robust to any degree of source network relevance, automatically adjusting the strength of fusion to take this into account. Moreover, it is able to provide estimated

domain and fragment-level relatedness as an output, which is of interest in many applications (e.g., in the medical domain, to diagnose differences in procedures between hospitals). Experiments show that BNPTL consistently outperforms single task STL and former transfer learning algorithms. Finally, experiments with a real-world trauma care network show the practical value of our method, adapting medical decision support from large inner city hospitals with extensive data to smaller provincial hospitals.

# 6.2 Discussion of Limitations and Future Work 

An assumption made by our current framework is that transfer is only performed from the single most relevant source fragment. An alternative would be to transfer from every source fragment estimated to be relevant. This would be a relatively straightforward extension of Eq (6) to sum up multiple potential relevant sources. However, by increasing the number of source fragments used, the risk of negative transfer may be increased. If any irrelevant source is transferred as a 'false positive' (i.e., $p\left(H_{j k 1}^{s} \mid D_{j}^{t}, D_{k}^{t}\right)>0$ for irrelevant source fragment $\mathscr{D}_{k}^{s}$ then it may negatively affect the target in Eq (6). This eventuality is more likely if many sources can be fused. In contrast, our current framework just needs to rank a irrelevant sources below a relevant source in order to be robust to negative transfer. This is an example of a general tradeoff between flexibility/amount of information possible to transfer, and robustness to negative transfer (Torrey and Shavlik, 2009).

A second limiting assumption is that the underlying relatedness is binary (i.e., sources are relevant or irrelevant). Clearly sources may have more continuous degrees of relatedness to the target. In our framework this is only supported implicitly through the fact that a somewhat related source will have an intermediate probability of relatedness (Eq (2)), and thus be used but with a smaller weight Eq (6). In future continuous degrees of relatedness could be modelled more explicitly.

Finally, in this paper we have addressed relatedness inference in an entirely data-driven way. In future we would like to integrate expert-provided priors and constraints to guide transfer parameter learning, and transfer structure learning.

## Acknowledgments

The authors would like to thank three anonymous reviewers for their valuable feedback. This work is supported by the European Research Council (ERC-2013-AdG339182-BAYES-KNOWLEDGE) and the European Union's Horizon 2020 research and innovation programme under grant agreement No 640891. YZ is supported by China Scholarship Council (CSC)/Queen Mary Joint PhD scholarships and National Natural Science Foundation of China (61273322, 71471174).

# Table 3

Performance (known correspondences) of STL, ALL and transfer learning methods: CPTAgg, BNPTL ${ }^{\text {ap }}$ and BNPTL.


# Table 4

Performance (unknown correspondences and hidden variables) of STL and transfer learning methods: CPTAgg and BNPTL.


# Table 5

The fragment selection performance of CPTAgg and BNPTL. The numbers $25 \%$ and $50 \%$ indicate different portions of irrelevant fragments in the sources. Note that chance here is much lower than $75 / 50 \%$ due to unknown network correspondence.


# Table 6

Performance (domain-partially-irrelevant) of STL and transfer learning methods: CPTAgg and BNPTL.


# Table 7

Performance (domain-fully-irrelevant) of STL and transfer learning methods: BMCBasic and BNPTL. The symbol $\leftarrow$ represents the transfer relationship: target $\leftarrow$ source. Here 'Other' represents the six BN repository networks with the target removed.


Table 8 Prediction performance (AUC) for medical tasks. The target attributes for ILP and TC datasets are Liver disease and Death respectively. Statistically significant improvements of BNPTL(UC) and BNPTL(KC) over alternatives are marked with symbols * and $\Delta$ respectively.
