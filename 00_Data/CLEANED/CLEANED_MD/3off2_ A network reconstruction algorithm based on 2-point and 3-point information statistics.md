# 3off2: A network reconstruction algorithm based on 2-point and 3-point information statistics 

Séverine Affeldt ${ }^{1,2}$, Louis Verny ${ }^{1,2}$ and Hervé Isambert ${ }^{1,2 *}$<br>From Bringing Maths to Life (BMTL)<br>Naples, Italy. 27-29 October 2014


#### Abstract

Background: The reconstruction of reliable graphical models from observational data is important in bioinformatics and other computational fields applying network reconstruction methods to large, yet finite datasets. The main network reconstruction approaches are either based on Bayesian scores, which enable the ranking of alternative Bayesian networks, or rely on the identification of structural independencies, which correspond to missing edges in the underlying network. Bayesian inference methods typically require heuristic search strategies, such as hill-climbing algorithms, to sample the super-exponential space of possible networks. By contrast, constraint-based methods, such as the PC and IC algorithms, are expected to run in polynomial time on sparse underlying graphs, provided that a correct list of conditional independencies is available. Yet, in practice, conditional independencies need to be ascertained from the available observational data, based on adjustable statistical significance levels, and are not robust to sampling noise from finite datasets.


Results: We propose a more robust approach to reconstruct graphical models from finite datasets. It combines constraint-based and Bayesian approaches to infer structural independencies based on the ranking of their most likely contributing nodes. In a nutshell, this local optimization scheme and corresponding 3off2 algorithm iteratively "take off" the most likely conditional 3-point information from the 2-point (mutual) information between each pair of nodes. Conditional independencies are thus derived by progressively collecting the most significant indirect contributions to all pairwise mutual information. The resulting network skeleton is then partially directed by orienting and propagating edge directions, based on the sign and magnitude of the conditional 3-point information of unshielded triples. The approach is shown to outperform both constraint-based and Bayesian inference methods on a range of benchmark networks. The 3off2 approach is then applied to the reconstruction of the hematopoiesis regulation network based on recent single cell expression data and is found to retrieve more experimentally ascertained regulations between transcription factors than with other available methods.
Conclusions: The novel information-theoretic approach and corresponding 3off2 algorithm combine constraint-based and Bayesian inference methods to reliably reconstruct graphical models, despite inherent sampling noise in finite datasets. In particular, experimentally verified interactions as well as novel predicted regulations are established on the hematopoiesis regulatory networks based on single cell expression data.

Keywords: Network reconstruction, Hybrid inference method, Information theory, Hematopoiesis

[^0]
[^0]:    *Correspondence: herve.isambert@curie.fr
    ${ }^{1}$ Institut Curie, PSL Research University, CNRS, UMR168, 26 rue d'Ulm, 75005 Paris, France
    ${ }^{2}$ Sorbonne Universités, UPMC Univ Paris 06, 4, Place Jussieu, 75005 Paris, France

## Background

Two types of reconstruction method for directed networks have been developed and applied to a variety of experimental datasets. These methods are either based on Bayesian scores [1, 2] or rely on the identification of structural independencies, which correspond to missing edges in the underlying network [3, 4].

Bayesian inference approaches have the advantage of allowing for quantitative comparisons between alternative networks through their Bayesian scores but they are limited to rather small causal graphs due to the superexponential space of possible directed graphs to sample [1, 5, 6]. Hence, Bayesian inference methods typically require either suitable prior restrictions on the structures [7, 8] or heuristic search strategies such as hill-climbing algorithms [9-11].

By contrast, structure learning algorithms based on the identification of structural constraints typically run in polynomial time on sparse underlying graphs. These so-called constraint-based approaches, such as the PC [12] and IC [13] algorithms, do not score and compare alternative networks. Instead they aim at ascertaining conditional independencies between variables to directly infer the Markov equivalent class of all causal graphs compatible with the available observational data. Yet, these methods are not robust to sampling noise in finite datasets as early errors in removing edges from the complete graph typically trigger the accumulation of compensatory errors later on in the pruning process. This cascading effect makes the constraint-based approaches sensitive to the adjustable significance level $\alpha$, required for the conditional independence tests. In addition, traditional constraint-based methods are not robust to the order in which the conditional independence tests are processed, which prompted recent algorithmic improvements intending to achieve order-independence [14].

In this paper, we report a novel network reconstruction method, which exploits the best of these two types of structure learning approaches. It combines constraintbased and Bayesian frameworks to reliably reconstruct graphical models despite inherent sampling noise in finite observational datasets. To this end, we have developed a robust information-theoretic method to confidently ascertain structural independencies in causal graphs based on the ranking of their most likely contributing nodes. Conditional independencies are derived using an iterative search approach that identifies the most significant indirect contributions to all pairwise mutual information between variables. This local optimization algorithm, outlined below, amounts to iteratively subtracting the most likely conditional 3-point information from 2-point information between each pair of nodes. The resulting network skeleton is then partially directed by orienting and propagating edge directions,
based on the sign and magnitude of the conditional 3point information of unshielded triples. Identifying structural independencies within such a maximum likelihood framework circumvents the need for adjustable significance levels and is found to be more robust to sampling noise from finite observational data, even when compared to constraint-based methods intending to resolve the order-dependence on the variables [14].

## Constraint-based methods

Constraint-based approaches, such as the PC [12] and IC [13] algorithms, infer causal graphs from observational data, by searching for conditional independencies among variables. Under the Markov and Faithfulness assumptions, these algorithms return a Complete Partially Directed Acyclic Graph (CPDAG) that represents the Markov equivalent class of the underlying causal structure [3, 4]. They proceed in three steps detailed in Algorithm 1:

```
Algorithm 1: Constraint-based network reconstruc-
tion
In: observational data of variables V; an ordering
order (V) on the variables; a significance level \(\alpha\)
Out: CPDAG \(\mathcal{C}\)
0. Initiation
Start with a complete undirected graph \(\mathcal{G}\)
Let \(\ell=0\)
1. Iteration
repeat
    while \(\exists x y\) link with \(\mid\) adj \((\mathcal{G}, x) \backslash\{y\}| \geqslant \ell\) do
        while \(x y \subset \operatorname{adj}(\mathcal{G})\) and \(\exists\left\{u_{i}\right\} \subseteq \operatorname{adj}(\mathcal{G}, x) \backslash\{y\} \),
        not yet considered with \(\mid\left\{u_{i}\right\}|=\ell\) do
            if Indep \(\left(x ; y \mid\left\{u_{i}\right\}\right)\) at significance level \(\alpha\)
            then
                xy link is non-essential and removed
                separation set of \(x y: \operatorname{Sep}_{x y}=\left\{u_{i}\right\}\)
            end
            end
    end
    Set \(\ell=\ell+1\)
until \(\forall x \in \mathcal{G}, \mid\) adj \((\mathcal{G}, x) \mid \leqslant \ell\);
2. Orientation
forall the unshielded triples do
    \(R_{0}:\left\{x-z-y \& x \neq y \& z \notin \operatorname{Sep}_{x y}\right\} \Rightarrow\{x \rightarrow z \leftarrow y\}\)
end
3. Propagation
repeat
    \(R_{1}:\{x \rightarrow z-y \& x \neq y\} \quad \Rightarrow\{z \rightarrow y\}\)
    \(R_{2}:\{x \rightarrow y \rightarrow z \& x-z\} \quad \Rightarrow\{x \rightarrow z\}\)
    \(R_{3}:\{x-y \rightarrow z \& x-t \rightarrow z \& y \neq t\} \quad \Rightarrow\{x \rightarrow z\}\)
until no further orientation can be propagated;
```

- 1) inferring unnecessary edges and associated separation sets to obtain an undirected skeleton.
- 2) orienting unshielded triples as v-structures if their middle node is not in the separation set $\left(R_{0}\right)$.
- 3) propagating as many orientations as possible following propagation rules $\left(R_{1-3}\right)$, which prevents the orientation of additional v -structures $\left(R_{3}\right)$ and directed cycles $\left(R_{2-3}\right)[15]$.

However, as previously stated, the sensitivity of the constraint-based methods to the adjustable significance level $\alpha$ used for the conditional independence tests and to the order in which the variables are processed (step 1) favors the accumulation of errors when the search procedure relies on finite observational data.
In this paper, we aim at improving constraint-based methods, Algorithm 1, by uncovering the most reliable conditional independencies supported by the (finite) available data, based on a quantitative information theoretic framework.

## Maximum likelihood methods

The maximum likelihood $\mathcal{L}_{\mathcal{G}}$ is related to the cross entropy $H(\mathcal{G}, \mathcal{D})=-\sum_{\left\{x_{i}\right\}} p\left(\left\{x_{i}\right\}\right) \log \left(q\left(\left\{x_{i}\right\}\right)\right)$ between the "true" probability distribution $p\left(\left\{x_{i}\right\}\right)$ from the data $\mathcal{D}$ and the approximate probability distribution $q\left(\left\{x_{i}\right\}\right)=$ $\prod_{i} p\left(x_{i} \mid\left\{P a_{x_{i}}\right\}\right)$ generated by the Bayesian network $\mathcal{G}$ with specific parent nodes $\left\{P a_{x_{i}}\right\}$ for each node $x_{i}$, leading to $[16]$,

$$
\mathcal{L}_{\mathcal{G}}=e^{-N H(\mathcal{G}, \mathcal{D})}=e^{-N \sum_{i} H\left(x_{i} \mid\left\{P a_{x_{i}}\right\}\right)}
$$

where $\sum_{i} H\left(x_{i} \mid \left\{P a_{x_{i}}\right\}\right)$ is the (conditional) entropy of the underlying causal graph. This enables to score and compare alternative models through their maximum likelihood ratio as,

$$
\frac{\mathcal{L}_{\mathcal{G}^{\prime}}}{\mathcal{L}_{\mathcal{G}}}=e^{-N \sum_{i}\left(H\left(x_{i} \mid\left\{P a_{x_{i}}^{\prime}\right\}\right)-H\left(x_{i} \mid\left\{P a_{x_{i}}\right\}\right)\right)}
$$

Note, in particular, that the significance level of the Maximum likelihood approach is set by the number $N$ of independent observational data points, as detailed in the Methods Section below.

## Methods

## Information theoretic framework Inferring isolated v-structures vs non-v-structures from 3-point and 2-point information

Applying the previous likelihood definition, Eq. 1, to isolated v-structures (Fig. 1a) and Markov equivalent non-vstructures (Fig. 1b-d), one obtains,

$$
\begin{aligned}
\mathcal{L}_{\mathrm{v}}(x y) & =e^{-N[H(z \mid x, y)+H(x)+H(y)]} \\
& =e^{-N[H(x, y, z)+I(x ; y)]}
\end{aligned}
$$

where $I(x ; y)=H(x)+H(y)-H(x, y)$ is the 2-point mutual information between $x$ and $y$, and,

$$
\begin{aligned}
\mathcal{L}_{\mathrm{nv}}(x y) & =e^{-N[H(x \mid z)+H(y \mid z)+H(z)]} \\
& =e^{-N[H(x, y, z)+I(x ; y \mid z)]}
\end{aligned}
$$

where $I(x ; y \mid z)=H(x \mid z)+H(y \mid z)-H(x, y \mid z)$ is the conditional mutual information between $x$ and $y$ given $z$. Hence, one obtains the likelihood ratio,

$$
\frac{\mathcal{L}_{\mathrm{v}}(x y)}{\mathcal{L}_{\mathrm{nv}}(x y)}=e^{-N[I(x ; y)-I(x ; y \mid z)]}=e^{-N I(x ; y ; z)}
$$

where we introduced the 3-point information function, $I(x ; y ; z)=I(x ; y)-I(x ; y \mid z)$, which is in fact invariant upon permutations between $x, y$ and $z$, as seen in terms of entropy functions,

$$
\begin{aligned}
I(x ; y ; z)= & H(x)+H(y)+H(z)-H(x, y) \\
& -H(x, z)-H(y, z)+H(x, y, z)
\end{aligned}
$$

As long recognized in the field [17, 18], 3-point information, $I(x ; y ; z)$, can be positive or negative (if $I(x ; y)<$ $I(x ; y \mid z)$ ), unlike 2-point mutual information, which are always positive, $I(x ; y) \geqslant 0$.
More precisely, Eq. 5 demonstrates that the sign and magnitude of 3-point information provide a quantitative estimate of the relative likelihoods of isolated v-structures versus non-v-structures, which are in fact independent of their actual non-connected bases $x y, x z$ or $y z$,

$$
\frac{\mathcal{L}_{\mathrm{v}}(x y)}{\mathcal{L}_{\mathrm{nv}}(x y)}=\frac{\mathcal{L}_{\mathrm{v}}(x z)}{\mathcal{L}_{\mathrm{nv}}(x z)}=\frac{\mathcal{L}_{\mathrm{v}}(y z)}{\mathcal{L}_{\mathrm{nv}}(y z)}=e^{-N I(x ; y ; z)}
$$

Hence, a significantly negative 3-point information, $I(x ; y ; z)<0$, implies that a v-structure is more likely than a non-v-structure given the observed correlation data. Conversely, a significantly positive 3-point information, $I(x ; y ; z)>0$, implies that a non-v-structure model is more likely than a v-structure model.
Yet, as noted above, 3-point information, $I(x ; y ; z)$, being symmetric by construction, it cannot indicate how to orient v-structures or non-v-structures over the $x y z$ triple. To this end, it is however straightforward to show that the most likely base $(x y, x z$ or $y z)$ of the local v-structure or non-v-structure corresponds to the pair with lowest

![img-0.jpeg](img-0.jpeg)

**Fig. 1** Inference of v-structures versus non-v-structures by 3-point information from observational data. **a** Isolated v-structures are predicted for *I*(*x*; *y*; *z*) < 0, and (**b**–**d**) isolated non-v-structures for *I*(*x*; *y*; *z*) > 0. **e** Generalized v-structures are predicted for *I*(*x*; *y*; *z*||*u*||) < 0 and (**f**–**h**) generalized non-v-structures for *I*(*x*; *y*; *z*||*u*||) > 0. In addition, as *I*(*x*; *y*; *z*||*u*||) are invariant upon *xyz* permutations, the global orientation of v-structures and non-v-structures also requires to find the most likely base of the *xyz* triple. Choosing the base *xy* with the lowest conditional mutual information, *i.e.*, *I*(*x*; *y*||*u*||) = min*xyz* (*I*(*s*; *t*||*u*||)), is found to be consistent with the Data Processing Inequality expected for (generalized) non-v-structures in the limit of infinite dataset, see main text. In practice, given a finite dataset, the inference of (generalized) v-structures versus non-v-structures can be obtained by replacing 3-point and 2-point information terms *I*(*x*; *y*||*u*||) and *I*(*x*; *y*; *z*||*u*||) by shifted equivalents, *I*(*x*; *y*||*u*||) and *I*(*x*; *y*; *z*||*u*||), including finite size corrections, see text (Eqs. 23 & 24).

mutual information, *e.g.*, *I*(*x*; *y*) = min*xyz*(*I*(*s*; *t*)), as shown by the likelihood ratios,

$$\frac{\mathcal{L}_{\mathbf{v}}(xy)}{\mathcal{L}_{\mathbf{v}}(st)} = \frac{\mathcal{L}_{nv}(xy)}{\mathcal{L}_{nv}(st)} = \frac{e^{-NI(x;y)}}{e^{-NI(x;t)}} \tag{8}$$

Note, in particular, that choosing the base with the lowest mutual information is consistent with the Data Processing Inequality expected for non-v-structures, Fig. 1b–d.

Hence, combining 3-point and 2-point information allows to determine the likelihood and the base of isolated v-structures versus non-v-structures. But how to extend such simple results to identify local v-structures and non-v-structures embedded within an entire graph *G*?

#### *Inferring embedded v-structures vs non-v-structures from conditional 3-point and 2-point information*

To go from isolated to embedded v-structures and non-v-structures within a DAG *G*, we will consider the Markov equivalent CPDAG of *G* and introduce generalized v-structures and non-v-structures, Fig. 1e–h. We will demonstrate that their relative likelihood, given the available observational data, can be estimated from the sign and magnitude of a conditional 3-point information, *I*(*x*; *y*; *z*||*u*||), Eq. 11. This will extend our initial result valid for isolated v-structures and non-v-structures, Eq. 7.

Let's consider a pair of non-neighbor nodes $x, y$ with a set of upstream nodes $\left\{u_{i}\right\}_{n}$, where each node $u_{i}$ has at least one direct connection to $x\left(u_{i} \rightarrow x\right)$ or $y\left(u_{i} \rightarrow y\right)$ or to another upstream node $u_{j} \in\left\{u_{i}\right\}_{n}\left(u_{i} \rightarrow u_{j}\right)$ or only undirected links to these nodes $\left(u_{i}-x, u_{i}-y\right.$ or $\left.u_{i}-u_{j}\right)$. Thus, given $x, y$ and a set of upstream nodes $\left\{u_{i}\right\}_{n}$, any additional node $z$ can either be:

- i) at the apex of a generalized v-structure, if all existing connections between $x, y,\left\{u_{i}\right\}_{n}$ and $z$ are directed and point towards $z$, Fig. 1e, or else,
- ii) $z$ has at least one undirected link with $x, y$ or one of the upstream nodes $u_{i}\left(z-x, z-y\right.$ or $\left.z-u_{i}\right)$ or at least one directed link pointing towards these nodes $\left(z \rightarrow x, z \rightarrow y\right.$ or $\left.z \rightarrow u_{i}\right)$, Fig. 1f-h. In such a case, $z$ might contribute to the mutual information $I(x ; y)$ and should be included in the set of upstream nodes $\left\{u_{i}\right\}_{n}$, thereby defining a generalized non-v-structure, Figs. 1f-h.

Then, similarly to the case of an isolated v-structure (Eq. 3), the maximum likelihood $\mathcal{L}_{\mathrm{v}}(x y)$ of a generalized vstructure pointing towards $z$ from a base $x y$ with upstream nodes $\left\{u_{i}\right\}_{n}$ can be expressed as,

$$
\begin{aligned}
\mathcal{L}_{\mathrm{v}}(x y) & =e^{-N\left[H\left(x ; x, y,\left\{u_{i}\right\}\right)+H\left(y ;\left\{u_{i}\right\}\right)+H\left(y \mid\left\{u_{i}\right\}\right)+H\left(\left\{u_{i}\right\}\right)\right]} \\
& =e^{-N\left[H\left(x, y, z,\left\{u_{i}\right\}\right)+I\left(x ; y \mid\left\{u_{i}\right\}\right)\right]}
\end{aligned}
$$

where $I\left(x ; y \mid\left\{u_{i}\right\}\right)$ is the conditional mutual information between $x$ and $y$ given $\left\{u_{i}\right\}, I\left(x ; y \mid\left\{u_{i}\right\}\right)=H\left(x \mid\left\{u_{i}\right\}\right)+$ $H\left(y \mid\left\{u_{i}\right\}\right)-H\left(x, y \mid\left\{u_{i}\right\}\right)-H\left(\left\{u_{i}\right\}\right)$.
Likewise, the maximum likelihood $\mathcal{L}_{\mathrm{mv}}(x y)$ of a generalized non-v-structure of base $x y$ with upstream nodes $\left\{u_{i}\right\}_{n}$ and $z$ can be expressed as,

$$
\begin{aligned}
\mathcal{L}_{\mathrm{mv}}(x y) & =e^{-N\left[H\left(x ; z,\left\{u_{i}\right\}\right)+H\left(y ; z,\left\{u_{i}\right\}\right)+H\left(z,\left\{u_{i}\right\}\right)\right]} \\
& =e^{-N\left[H\left(x, y, z,\left\{u_{i}\right\}\right)+I\left(x ; y \mid z,\left\{u_{i}\right\}\right)\right]}
\end{aligned}
$$

where $I\left(x ; y \mid z,\left\{u_{i}\right\}\right)=H\left(x \mid z,\left\{u_{i}\right\}\right)+H\left(y \mid z,\left\{u_{i}\right\}\right)-H(x, y \mid z$, $\left\{u_{i}\right\})-H\left(z,\left\{u_{i}\right\}\right)$ is the conditional mutual information between $x$ and $y$ given $z$ and $\left\{u_{i}\right\}$. Hence,

$$
\frac{\mathcal{L}_{\mathrm{v}}(x y)}{\mathcal{L}_{\mathrm{mv}}(x y)}=e^{-N I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)}
$$

where we introduced the conditional 3-point information, $I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)=I\left(x ; y \mid\left\{u_{i}\right\}\right)-I\left(x ; y \mid z,\left\{u_{i}\right\}\right)$.
Hence, a significantly negative conditional 3-point information, $I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)<0$, implies that a generalized v-structure is more likely than a generalized non-v-structure given the available observational data. Conversely, a significantly positive conditional 3-point information, $I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)>0$, implies that a generalized
non-v-structure model is more likely than a generalized v-structure model.
Yet, as the conditional 3-point information, $I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)$, is in fact invariant upon permutations between $x, y$ and $z$, it cannot indicate how to orient embedded v-structures or non-v-structures over the $x y z$ triple, as already noted in the case of isolated v-structures and non-v-structures, above.
However, the most likely base ( $x y, x z$ or $y z$ ) of the embedded v-structure or non-v-structure corresponds to the least correlated pair conditioned on $\left\{u_{i}\right\}$, e.g., $I\left(x ; y \mid\left\{u_{i}\right\}\right)=\min _{x y z}\left(I\left(s ; t \mid\left\{u_{i}\right\}\right)\right)$, as shown with the following likelihood ratios,

$$
\frac{\mathcal{L}_{\mathrm{v}}(x y)}{\mathcal{L}_{\mathrm{v}}(s t)}=\frac{\mathcal{L}_{\mathrm{mv}}(x y)}{\mathcal{L}_{\mathrm{mv}}(s t)}=\frac{e^{-N I\left(x ; y \mid\left\{u_{i}\right\}\right)}}{e^{-N I\left(s ; t \mid\left\{u_{i}\right\}\right)}}
$$

Note, in particular, that choosing the base with the lowest conditional mutual information, e.g., $I\left(x ; y \mid\left\{u_{i}\right\}\right)=$ $\min _{x y z}\left(I\left(s ; t \mid\left\{u_{i}\right\}\right)\right)$, is consistent with the Data Processing Inequality expected for the generalized non-v-structure of Fig. 1f-h, $I(x ; y) \leqslant \min \left(I\left(x ; z,\left\{u_{i}\right\}\right), I\left(z,\left\{u_{i}\right\} ; y\right)\right)$, as shown below for $I(x ; y)$ and $I\left(x ; z,\left\{u_{i}\right\}\right)$, by subtracting $I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)$ on each side of the inequality $I\left(x ; y \mid\left\{u_{i}\right\}\right) \leqslant$ $I\left(x ; z \mid\left\{u_{i}\right\}\right)$, leading to,

$$
\begin{aligned}
I\left(x ; y \mid z,\left\{u_{i}\right\}\right) & \leqslant I\left(x ; z \mid\left\{u_{i}\right\}, y\right) \\
& \leqslant I\left(x ; z \mid\left\{u_{i}\right\}, y\right)+I\left(x ;\left\{u_{i}\right\} \mid y\right) \\
& \leqslant I\left(x ; z,\left\{u_{i}\right\} \mid y\right) \\
I(x ; y) & \leqslant I\left(x ; z,\left\{u_{i}\right\}\right)
\end{aligned}
$$

where we have used the chain rule, $I\left(x ; z,\left\{u_{i}\right\} \mid y\right)=$ $I\left(x ; z \mid\left\{u_{i}\right\}, y\right)+I\left(x ;\left\{u_{i}\right\} \mid y\right)$, before adding $I\left(x ; y ; z,\left\{u_{i}\right\}\right)$ on each side of the inequality. The corresponding inequality holds between $I(x ; y)$ and $I\left(z,\left\{u_{i}\right\} ; y\right)$, implying the Data Processing Inequality.

## Finite size corrections of maximum likelihood

Maximum likelihood ratios, such as Eq. 2, suggest that $1 / N$ sets the significance level of the maximum likelihood approach, as $H(\mathcal{G}, \mathcal{D})-H\left(\mathcal{G}^{\prime}, \mathcal{D}\right) \gg 1 / N$ should imply a significant improvement of the underlying model $\mathcal{G}^{\prime}$ over $\mathcal{G}$. In practice, however, there are $\mathcal{O}(\log (N) / N)$ corrections coming from the proper normalization of maximum likelihoods (see Appendix),

$$
\mathcal{L}_{\mathcal{G}}=\frac{e^{-N \sum_{i} H\left(x_{i} \mid\left\{\mathrm{Pa}_{x_{i}}\right\}\right)}}{Z(\mathcal{G}, \mathcal{D})}
$$

The model $\mathcal{G}$ can then be compared to the alternative model $\mathcal{G}_{\backslash x \rightarrow y}$ with one missing edge $x \rightarrow y$ using the maximum likelihood ratio,

$$
\frac{\mathcal{L}_{\mathcal{G}_{\backslash x \rightarrow y}}}{\mathcal{L}_{\mathcal{G}}}=e^{-N I\left(x ; y \mid\left\{\mathrm{Pa}_{y}\right\}_{\backslash x}\right)} \frac{Z(\mathcal{G}, \mathcal{D})}{Z\left(\mathcal{G}_{\backslash x \rightarrow y}, \mathcal{D}\right)}
$$

where $I\left(x ; y \mid\left\{\mathrm{Pa}_{y}\right\}_{\backslash x}\right)=H\left(y \mid\left\{\mathrm{Pa}_{y}\right\}_{\backslash x}\right)-H\left(y \mid\left\{\mathrm{Pa}_{y}\right\}\right)$.

Then, following the rationale of constraint-based approaches, Eq. 15 can be reformulated by replacing the parent nodes $\left\{\mathrm{Pa}_{y}\right\}_{\backslash x}$ with an unknown separation set $\left\{u_{i}\right\}$ to be learnt simultaneously with the missing edge candidate $x y$,

$$
\begin{aligned}
\frac{\mathcal{L}_{\mathcal{G}_{\backslash x y}\left\{u_{i}\right\}}}{\mathcal{L}_{\mathcal{G}}} & =e^{-N I\left(x ; y \mid\left\{u_{i}\right\}\right)+k_{x ; y \mid\left\{u_{i}\right\}}} \\
k_{x ; y \mid\left\{u_{i}\right\}} & =\log \left(Z(\mathcal{G}, \mathcal{D}) / Z\left(\mathcal{G}_{\backslash x y \mid\left\{u_{i}\right\}}, \mathcal{D}\right)\right)
\end{aligned}
$$

where the factor $k_{x ; y \mid\left\{u_{i}\right\}}>0$ tends to limit the complexity of the models by favoring fewer edges. Namely, the condition, $I\left(x ; y \mid\left\{u_{i}\right\}\right)<k_{x ; y \mid\left\{u_{i}\right\}} / N$, implies that simpler models compatible with the structural independency, $x \Perp y \mid\left\{u_{i}\right\}$, are more likely than model $\mathcal{G}$, given the finite available dataset. This replaces the 'perfect' conditional independency condition, $I\left(x ; y \mid\left\{u_{i}\right\}\right)=0$, valid in the limit of an infinite dataset, $N \rightarrow \infty$. A common complexity criteria in model selection is the Bayesian Information Criteria (BIC) or Minimal Description Length (MDL) criteria $[19,20]$,

$$
k_{x ; y \mid\left\{u_{i}\right\}}^{\mathrm{MDL}}=\frac{1}{2}\left(r_{x}-1\right)\left(r_{y}-1\right) \prod_{i} r_{u_{i}} \log N
$$

where $r_{x}, r_{y}$ and $r_{u_{i}}$ are the number of levels of the corresponding variables. The MDL complexity, Eq. 18, is simply related to the normalisation constant of the distribution reached in the asymptotic limit of a large dataset $N \rightarrow \infty$ (Laplace approximation). However, this limit distribution is only reached for very large datasets in practice.

Alternatively, the normalisation of the maximum likelihood can also be done over all possible datasets including the same number of data points to yield a (universal) Normalized Maximum Likelihood (NML) criteria [21, 22] and its decomposable [23, 24] and $x y$-symmetric version, $k_{x ; y \mid\left\{u_{i}\right\}}^{\mathrm{NML}}$, defined in the Appendix.

Then, incrementing the separation set of $x y$ from $\left\{u_{i}\right\}$ to $\left\{u_{i}\right\}+z$ leads to the following likelihood ratio,

$$
\frac{\mathcal{L}_{\mathcal{G}_{\backslash x y}\left\{u_{i}\right\}, z}}{\mathcal{L}_{\mathcal{G}_{\backslash x y}\left\{u_{i}\right\}}}}=e^{N I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)+k_{x ; y ; z \mid\left\{u_{i}\right\}}}
$$

with $I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)=I\left(x ; y \mid\left\{u_{i}\right\}\right)-I\left(x ; y \mid\left\{u_{i}\right\}, z\right)$ and where we introduced a 3-point conditional complexity, $k_{x ; y ; z \mid\left\{u_{i}\right\}}$, defined similarly as the difference between the 2-point conditional complexities,

$$
k_{x ; y ; z \mid\left\{u_{i}\right\}}=k_{x ; y \mid\left\{u_{i}\right\}, z}-k_{x ; y \mid\left\{u_{i}\right\}}
$$

However, unlike 3-point information, $I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)$, 3point complexities are always positive, $k_{x ; y ; z \mid\left\{u_{i}\right\}}>0$, provided that there are at least two levels for each implicated node $\ell \in x, y, z,\left\{u_{i}\right\}$, i.e. $r_{\ell} \geqslant 2$.

Hence, we can define the shifted 2-point and 3-point information in Eqs. $16 \& 19$ for finite datasets as,

$$
\begin{aligned}
I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}\right) & =I\left(x ; y \mid\left\{u_{i}\right\}\right)-\frac{k_{x ; y \mid\left\{u_{i}\right\}}}{N} \\
I^{\prime}\left(x ; y ; z \mid\left\{u_{i}\right\}\right) & =I\left(x ; y ; z \mid\left\{u_{i}\right\}\right)+\frac{k_{x ; y ; z \mid\left\{u_{i}\right\}}}{N}
\end{aligned}
$$

This leads to the following maximum likelihood ratios equivalent to Eqs. $11 \& 12$ for v-structure over non-vstructure and between alternative bases,

$$
\begin{aligned}
& \frac{\mathcal{L}_{\mathrm{v}}(x y)}{\mathcal{L}_{\mathrm{nv}}(x y)}=e^{-N I^{\prime}\left(x ; y ; z \mid\left\{u_{i}\right\}\right)} \\
& \frac{\mathcal{L}_{\mathrm{v}}(x y)}{\mathcal{L}_{\mathrm{v}}(s t)}=\frac{\mathcal{L}_{\mathrm{nv}}(x y)}{\mathcal{L}_{\mathrm{nv}}(s t)}=\frac{e^{-N I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}\right)}}{e^{-N I^{\prime}\left(x ; z \mid\left\{u_{i}\right\}\right)}}
\end{aligned}
$$

Hence, given a finite dataset, a significantly negative conditional 3-point information, corresponding to $I^{\prime}\left(x ; y ; z \mid\left\{u_{i}\right\}\right)<0$, implies that a v-structure $x \rightarrow z \leftarrow y$ is more likely than a non-v-structure provided that the structural independency, $x \Perp y \mid\left\{u_{i}\right\}$, is also confidently established as, $I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}\right)<0$. By contrast, a significantly positive conditional 3-point information corresponds to $I^{\prime}\left(x ; y ; z \mid\left\{u_{i}\right\}\right)>0$ and implies that a non-v-structure model is more likely than a v-structure model, given the available observational data.

## Probability estimate of indirect contributions to mutual information

The previous results enable us to estimate the probability of a node $z$ to contribute to the conditional mutual information $I\left(x ; y \mid\left\{u_{i}\right\}\right)$, by combining the probability, $P_{\mathrm{nv}}\left(x y z \mid\left\{u_{i}\right\}\right)$, that the triple $x y z$ is a generalized non-v-structure conditioned on $\left\{u_{i}\right\}$ and the probability, $P_{\mathrm{b}}\left(x y \mid\left\{u_{i}\right\}\right)$, that its base is $x y$, where,

$$
\begin{aligned}
P_{\mathrm{nv}}\left(x y z \mid\left\{u_{i}\right\}\right) & =\frac{\mathcal{L}_{\mathrm{nv}}(x y)}{\mathcal{L}_{\mathrm{nv}}(x y)+\mathcal{L}_{\mathrm{v}}(x y)} \\
P_{\mathrm{b}}\left(x y \mid\left\{u_{i}\right\}\right) & =\frac{\mathcal{L}_{\mathrm{nv}}(x y)}{\mathcal{L}_{\mathrm{nv}}(x y)+\mathcal{L}_{\mathrm{nv}}(x z)+\mathcal{L}_{\mathrm{nv}}(y z)}
\end{aligned}
$$

that is, using Eqs. $23 \& 24$ including finite size corrections of the maximum likelihoods,

$$
\begin{aligned}
P_{\mathrm{nv}}\left(x y z \mid\left\{u_{i}\right\}\right) & =\frac{1}{1+e^{-N I^{\prime}\left(x ; y ; z \mid\left\{u_{i}\right\}\right)}} \\
P_{\mathrm{b}}\left(x y \mid\left\{u_{i}\right\}\right) & =\frac{1}{1+\frac{e^{-N I^{\prime}\left(x ; z \mid\left\{u_{i}\right\}\right)}}{e^{-N I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}\right)}}+\frac{e^{-N I^{\prime}\left(y ; z \mid\left\{u_{i}\right\}\right)}}{e^{-N I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}\right)}}}
\end{aligned}
$$

Then, various alternatives to combine $P_{\mathrm{nv}}\left(x y z \mid\left\{u_{i}\right\}\right)$ and $P_{\mathrm{b}}\left(x y \mid\left\{u_{i}\right\}\right)$ exist to estimate the overall probability that the additional node $z$ indirectly contributes to $I\left(x ; y \mid\left\{u_{i}\right\}\right)$. One possibility is to choose the lower bound $S_{\mathrm{lb}}\left(z ; x y \mid\left\{u_{i}\right\}\right)$ of $P_{\mathrm{nv}}\left(x y z \mid\left\{u_{i}\right\}\right)$ and $P_{\mathrm{b}}\left(x y \mid\left\{u_{i}\right\}\right)$, since both conditions

need to be fulfilled to warrant that $z$ indeed contributes to $I\left(x ; y \mid\left\{u_{i}\right\}\right)$,

$$
S_{\mathrm{lb}}\left(z ; x y \mid\left\{u_{i}\right\}\right)=\min \left[P_{\mathrm{ny}}\left(x y z \mid\left\{u_{i}\right\}\right), P_{\mathrm{b}}\left(x y \mid\left\{u_{i}\right\}\right)\right]
$$

The pair of nodes $x y$ with the most likely contribution from a third node $z$ can then be ordered according to their $\operatorname{rank} R\left(x y ; z \mid\left\{u_{i}\right\}\right)$ defined as,

$$
R\left(x y ; z \mid\left\{u_{i}\right\}\right)=\max _{z}\left(S_{\mathrm{lb}}\left(z ; x y \mid\left\{u_{i}\right\}\right)\right)
$$

and $z$ can be iteratively added to the set of contributing nodes (i.e. $\left\{u_{i}\right\} \leftarrow\left\{u_{i}\right\}+z$ ) of the top link $x y=$ $\operatorname{argmax}_{x y} R(x y ; z \mid\left\{u_{i}\right\})$ to progressively recover the most significant indirect contributions to all pairwise mutual information in a causal graph, as outlined below.

## Robust inference of conditional independencies using the 3off2 scheme

The previous results can be used to provide a robust inference method to identify conditional independencies and, hence, reconstruct the skeleton of underlying causal graphs from finite available observational data. The approach follows the spirit of constraint-based methods, such as the PC or IC algorithms, but recovers conditional independencies following an evolving ranking of the network edges, $R(x y ; z \mid\left\{u_{i}\right\})$, defined in Eq. 30.

All in all, this amounts to perform a generic decomposition for each mutual information term, $I(x ; y)$, by introducing a succession of node candidates, $u_{1}, u_{2}, \ldots$, $u_{n}$, that are likely to contribute to the overall mutual information between the pair $x$ and $y$, as,

$$
\begin{aligned}
I(x ; y)= & I\left(x ; y ; u_{1}\right)+I\left(x ; y \mid u_{1}\right) \\
= & I\left(x ; y ; u_{1}\right)+I\left(x ; y ; u_{2} \mid u_{1}\right)+\ldots \\
& \ldots+I\left(x ; y ; u_{n} \mid\left\{u_{i}\right\}_{n-1}\right)+I\left(x ; y \mid\left\{u_{i}\right\}_{n}\right)
\end{aligned}
$$

or equivalently between the shifted 2-point and 3point information terms including finite size corrections (Eq. 22),

$$
\begin{aligned}
I^{\prime}(x ; y)= & I^{\prime}\left(x ; y ; u_{1}\right)+I^{\prime}\left(x ; y ; u_{2} \mid u_{1}\right)+\ldots \\
& +I^{\prime}\left(x ; y ; u_{n} \mid\left\{u_{i}\right\}_{n-1}\right)+I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}_{n}\right)
\end{aligned}
$$

Hence, given a significant mutual information between $x$ and $y, I^{\prime}(x ; y)>0$, we will search for possible structural independencies, i.e. $I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}_{n}\right)<0$, by iteratively "taking off" conditional 3-point information terms from the initial 2-point (mutual) information, $I^{\prime}(x ; y)$, as

$$
\begin{aligned}
I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}_{n}\right)= & I^{\prime}(x ; y)-I^{\prime}\left(x ; y ; u_{1}\right)-I^{\prime}\left(x ; y ; u_{2} \mid u_{1}\right) \\
& -\ldots-I^{\prime}\left(x ; y ; u_{n} \mid\left\{u_{i}\right\}_{n-1}\right)
\end{aligned}
$$

and similarly with non-shifted 2-point and 3-point information,

$$
\begin{aligned}
I\left(x ; y \mid\left\{u_{i}\right\}_{n}\right)= & I(x ; y)-I\left(x ; y ; u_{1}\right)-I\left(x ; y ; u_{2} \mid u_{1}\right) \\
& -\ldots-I\left(x ; y ; u_{n} \mid\left\{u_{i}\right\}_{n-1}\right)
\end{aligned}
$$

## 3off2 algorithm

The 3off2 scheme can be used to devise a two-step algorithm (see Algorithm 2), inspired by constraintbased approaches, to first reconstruct network skeleton (Algorithm 2, step 1) before combining orientation and propagation of edges in a single step based on likelihood ratios (Algorithm 2, step 2).

## Reconstruction of network skeleton

The 3off2 scheme will first be applied to iteratively remove edges with maximum positive contributions, $I^{\prime}\left(x ; y ; u_{k} \mid\left\{u_{i}\right\}_{k-1}\right)>0$, corresponding to the most likely generalized non-v-structures (Eq. 23), while minimizing simultaneously the remaining 2-point information, $I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}_{k}\right)$ (Eq. 24), consistently with the data processing inequality. Such 3off2 scheme (Algorithm 2, step 1) will therefore progressively lower the conditional 2-point information terms, $I^{\prime}(x ; y)>\cdots>$ $I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}_{k-1}\right)>I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}_{k}\right)$ and might ultimately result in the removal of the corresponding edge, $x y$, but only when a structural independency is actually found, i.e. $I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}_{n}\right)<0$, as in constraint-based algorithms for a given significance level $\alpha$. Yet, the skeleton obtained with the 3off2 scoring approach is expected to be more robust to finite observational data than the skeleton obtained with PC or IC algorithms, as the former results only from statistically significant 3-point contributions, $I^{\prime}\left(x ; y ; u_{k} \mid\left\{u_{i}\right\}_{k-1}\right)>0$, based on their quantitative 3off2 ranks, $R\left(x y ; u_{k} \mid\left\{u_{i}\right\}_{k-1}\right)$.
The best results on benchmark networks using these quantitative 3off2 ranks are obtained with the NML score (see Results and discussion Section below). The MDL score leads to equivalent results, as expected, in the limit of very large datasets (see Appendix). However, with smaller datasets, the most reliable results with the MDL score are obtained using non-shifted instead of shifted 2point and 3-point information terms in the 3off2 rank of individual edges, Eq. 30. This is because the MDL complexity tends to underestimate the importance of edges between nodes with many levels (see Appendix). For finite datasets, it easily leads to spurious conditional independencies, $I^{\prime}(x ; y \mid\{u i\})<0$, when using shifted 2point and 3-point information, Eq. 33, whereas using non-shifted information in the 3off2 ranks (Eq. 30) tends to limit the number of false negatives as early errors in $\left\{u_{i}\right\}$ can only increase $I(x ; y \mid\{u i\}) \geqslant 0$, in the end, in Eq. 34.

## Orientation of network skeleton

The skeleton and the separation sets resulting from the 3off2 iteration step (Algorithm 2, step 1) can then be used to orient the edges and to propagate orientations to the unshielded triples. However, while the constraintbased methods distinguish the v-structures orientation

step (Algorithm 1, step 2) from the propagation procedure (Algorithm 1, step 3), the 3off2 algorithm intertwines these two steps based on the respective likelihood scores of individual v-structures and non-v-structures (Algorithm 2, step 2).
As stated earlier, the magnitude and sign of the conditional 3-point information, $I(x ; y ; z \mid\left\{u_{i}\right\})$ (or equivalently the shifted 3-point information, Eq. 23), indicate if a non v-structure is more likely than a v-structure. Hence, all the unshielded triples can be ranked by the absolute value of their conditional 3-point information, that is, in decreasing order of their likelihood of being either a vstructure or a non-v-structure. As detailed in the step 2 of Algorithm 2, the most likely v-structure is used to set the first orientations, following $R_{0}$ orientation rule. The possible propagations are then performed, following $R_{1}$ propagation rule, starting from the unshielded triple having the most positive conditional 3-point information. The following most likely v-structure is considered when no further propagation is possible on unshielded triples with greater absolute 3-point information. If conflicting orientations arise (such as $a \rightarrow b \leftarrow c \& b \rightarrow c \leftarrow d$ ), the less likely v-structure and its possible propagations are ignored.
Note that we only implement the $R_{0}$ and $R_{1}$ propagation rules, which are applied in decreasing order of likelihood. In particular, we do not consider propagation rules $R_{2}$ and $R_{3}$ which are not associated to likelihood scores but enforce the hypothesis of acyclic constraint.
As for the 3off2 skeleton reconstruction, the orientation/propagation step of 3off2 allows for a robust discovery of orientations from finite observational data as it relies on a quantitative framework of likelihood ratios taken in decreasing order of their statistical significance. During this step, 3off2 recovers and propagates as many orientations as possible in an iterative procedure following the decreasing ranks of the unshielded triples based on the absolute value of their conditional 3-point information, $\left|I^{\prime}(x ; y ; z \mid\left\{u_{i}\right\})\right|$.

## Results and discussion

## Tests on benchmark graphs

We have tested the 3off2 network reconstruction approach to learn benchmark causal graphs containing 20 to 70 nodes, Figs. 2, 3, 4, 5 and 6. The results are evaluated against other methods in terms of Precision (or positive predictive value), Prec $=T P /(T P+F P)$, Recall or Sensitivity (true positive rate), $\operatorname{Rec}=T P /(T P+$ FN), as well as F-score $=2 \times \operatorname{Prec} \times \operatorname{Rec} /(\operatorname{Prec}+$ Rec) for increasing sample size $N=10$ to 50,000 data points.
We also define additional Precision, Recall and Fscores taking into account the edge orientations of the

Algorithm 2: 3off2 Network Reconstruction
In: finite observational dataset of size $N$; complexity $k_{x ; y \mid\left\{u_{i}\right\}}$
Out: (partially) oriented graph $\mathcal{G}$

## 0. Initiation

Start with complete undirected graph $\mathcal{G}$
forall the links $x y$ do
if $I(x ; y)<k_{x ; y \mid \emptyset} / N$ i.e. $I^{\prime}(x ; y)<0$ then
$x y$ link is non-essential and removed
separation set of $x y: \operatorname{Sep}_{x y}=\emptyset$
else
find the most contributing node $z$ neighbor of $x$ or $y$ and compute 3off2 rank, $R(x y ; z \mid \emptyset)$ end
end

## 1. Iteration

while $\exists x y$ link with $R(x y ; z \mid\left\{u_{i}\right\})>1 / 2$ do
for top link $x y$ with highest rank $R(x y ; z \mid\left\{u_{i}\right\})$ do expand contributing set $\left\{u_{i}\right\} \leftarrow\left\{u_{i}\right\}+z$ if $I\left(x ; y \mid\left\{u_{i}\right\}\right)<k_{x ; y \mid\left\{u_{i}\right\}} / N$ i.e. $I^{\prime}\left(x ; y \mid\left\{u_{i}\right\}\right)<0$ then
$x y$ link is non-essential and removed
separation set of $x y: \operatorname{Sep}_{x y}=\left\{u_{i}\right\}$
else
find next most contributing node $z$ neighbor of $x$ or $y$ and compute new 3off2 rank of $x y: R(x y ; z \mid\left\{u_{i}\right\})$
end
sort the 3off2 rank list $R(x y ; z \mid\left\{u_{i}\right\})$
end
end

## 2. Orientation / Propagation

Sort list of unshielded triples, $\mathcal{L}_{c}=\left\{\langle x, z, y\rangle_{x \neq y}\right\}$, in decreasing order of $\left|I^{\prime}(x ; y ; z \mid\left\{u_{i}\right\}\right|$


## repeat

Take $\langle x, z, y\rangle_{x \neq y} \in \mathcal{L}_{c}$ with highest $\left|I^{\prime}\left(x ; y ; z \mid\left\{u_{i}\right\}\right)\right|$ on which $R_{0}$ or $R_{1}$ orientation rule can be applied if $I^{\prime}\left(x ; y ; z \mid\left\{u_{i}\right\}\right)<0$ then
if $\langle x, z, y\rangle_{x \neq y}$ has no diverging orientation, apply
$R_{0}:\left\{x-* z *-y \& x \neq y \& z \notin \operatorname{Sep}_{x y}\right\} \Rightarrow\{x \rightarrow z \leftarrow y\}$
else
if $\langle x, z, y\rangle_{x \neq y}$ has one converging orientation, apply
$R_{1}:\{x \rightarrow z-y \& x \neq y\} \Rightarrow\{z \rightarrow y\}$
end
Apply new orientation(s) to all other $\left\langle x^{\prime}, z^{\prime}, y^{\prime}\right\rangle_{x^{\prime} \neq y^{\prime}} \in \mathcal{L}_{c}$
until no additional orientation can be obtained;
predicted networks against the corresponding CPDAG of the benchmark networks. This amounts to label as false positives, all true positive edges of the skeleton

![img-1.jpeg](img-1.jpeg)

**Fig. 2** CHILD network. [20 nodes, 25 links, 230 parameters, Average degree 2.5, Maximum in-degree 2]. Precision, Recall and F-score for skeletons (*dashed lines*) and CPDAGs (*solid lines*). The results are given for Aracne (*black*), PC (*blue*), Bayesian Hill-Climbing (*green*) and 3off2 (*red*)

with different orientation/non-orientation status as the CPDAG reference, $TP_{\text{misorient}}$, leading to the orientation-dependent definitions $TP^{\prime} = TP - TP_{\text{misorient}}$ and $FP^{\prime} = FP + TP_{\text{misorient}}$ with the corresponding CPDAG Precision, Recall and F-scores taking into account edge orientations.

The alternative inference methods used for comparison with 3off2 are the PC algorithm [12] implemented in the pcalg package [25, 26] and Bayesian inference using the hill-climbing heuristics implemented in the bnlearn package [27]. In addition, we also compare the skeleton of 3off2 to the unoriented output of Aracne [28], an information-based inference approach, which iteratively prunes links with the weakest mutual information based on the Data Processing Inequality. We have used the Aracne implementation of the minet package [29]. For each sample size, 3off2, Aracne, PC and the Bayesian inference methods have been tested on 50 replicates. Figures 2, 3, 4, 5 and 6 give the average results over these multiple replicates when comparing the CPDAG (solid lines) of the reconstructed network (or its skeleton, dashed lined) to the CPDAG (or the skeleton) of the benchmark network.

For each method, the plots presented in Figs. 2, 3, 4, 5 and 6 are those obtained for the parameters that give overall the best results over the five reconstructed benchmark networks (see Additional file 1, Figures S1-S20). In particular, we used the *stable* implementation of the PC algorithm, as well as the *majority rule* for the orientation and propagation steps [14]. PC's results are shown on Figs. 2, 3, 4, 5 and 6 for α = 0.1. Decreasing α tends to improve the skeleton Precision at the expense of the skeleton Recall, leading in fact to worse skeleton F-scores for finite datasets, *e.g.* $N \leq 1000$ (see Additional file 1, Figures S1-S5). The same trend is observed for CPDAG F-scores taking into account edge orientations, with best CPDAG scores at small sample sizes, obtained for larger α, *e.g.* $N \leq 1000$. Aracne threshold parameters for minimum difference in mutual information is set to ϵ = 0, as small positive values typically worsen F-scores (see Additional file 1, Figures S6-S10). Bayesian inference are obtained using BIC/MDL scores and hill-climbing heuristics with 100 random restarts [9] (see Additional file 1, Figures S11-S15). Finally, the best 3off2 network reconstructions are obtained using NML scores with shifted 2-point and 3-point information terms in the rank of individual edges,

![img-2.jpeg](img-2.jpeg)

**Fig. 3** ALARM network. [37 nodes, 46 links, 509 parameters, Average degree 2.49, Maximum in-degree 4]. Precision, Recall and F-score for skeletons (*dashed lines*) and CPDAGs (*solid lines*). The results are given for Aracne (*black*), PC (*blue*), Bayesian Hill-Climbing (*green*) and 3off2 (*red*)

see Methods. Using MDL scores, instead, leads to equivalent results, as expected, in the limit of very large datasets (see Appendix). However, with smaller datasets, the most reliable results with MDL scores are obtained using *non-shifted* instead of shifted 2-point and 3-point information terms in the 3off2 rank of individual edges, as discussed in Methods (see Additional file 1, Figures S16-S20).

All in all, we found that the 3off2 inference approach typically reaches better or equivalent F-scores for all dataset sizes as compared to all other tested methods, *i.e.* Aracne, PC and Bayesian inference, as well as the Max-Min Hill-Climbing (MMHC) hybrid method [30] (see Additional file 1, Figures S21-S25). This is clearly observed both on the skeletons (Figs. 2, 3, 4, 5 and 6 dashed lines) and even more clearly when taking the predictions of orientations into account (Figures 2, 3, 4, 5 and 6 solid lines).

#### **Applications to the hematopoiesis regulation network**

The reconstruction or reverse-engineering of real regulatory networks from actual expression data has already been performed on a number of biological systems (see *e.g.* [28, 31–33]). Here, we apply the 3off2 approach on a real biological dataset related to hematopoiesis. Transcription factors play a central role in hematopoiesis, from which derive the blood cell lineages. As suggested in previous studies, changes in the regulatory interactions among transcription factors [34] or their overexpression [35] might be involved in the development of T-acute lymphoblastic leukaemia (T-ALL). The key role of the hematopoiesis and the potentially serious consequences of its disregulations emphasize the need to accurately establish the complex interactions between the transcription factors involved in this critical biological process.

The dataset we have used for this analysis [36] consists of the single cell expressions of 18 transcription factors, known for their role in hematopoiesis. Five hundred ninety seven single cells representing 5 different types of hematopoietic progenitors have been included in the analysis (*N* = 597). We reconstructed the corresponding network with the 3off2 inference method, Fig. 7, and four other available approaches, namely, PC [12] implemented in the pcalg package [25, 26], Bayesian inference using hill-climbing heuristics as well as the Max-Min Hill-Climbing (MMHC) hybrid method [30], both implemented in the bnlearn package [27], and, finally, Aracne [28] implemented in the minet package [29] (Table 1 and Additional file 1: Table S1).

![img-3.jpeg](img-3.jpeg)

**Fig. 4** INSURANCE network. [27 nodes, 52 links, 984 parameters, Average degree 3.85, Maximum in-degree 3]. Precision, Recall and F-score for skeletons (*dashed lines*) and CPDAGs (*solid lines*). The results are given for Aracne (*black*), PC (*blue*), Bayesian Hill-Climbing (*green*) and 3off2 (*red*)

3off2 uncovers all 11 interactions for which specific experimental evidence has been reported in the literature (Fig. 7, red links: known activations; blue links: known repressions) as well as 30 additional links (Fig. 7, grey links: unknown regulatory interactions). By contrast, randomization of the actual data across samples for each TF leads to only 5.25 spurious interactions on average between the 18 TFs, instead of the 41 inferred edges from the actual data, and 1.62 spurious interactions on average, instead of the 16 interactions predicted among the 10 TFs involved in known regulatory interactions, Fig. 7. This suggests that around 10–13 % of the predicted edges might be spurious, due to inevitable sampling noise in the finite dataset. In particular, the 3off2 inference approach successfully recovers the relationships of the regulatory triad between *Gata2*, *Gfi1b* and *Gfi1* as described in [36] and reports correct orientations for the edges involving *Gata2* (*Gfi1b* and *Gfi1* crossregulate in fact one another [36], Table 1). The network reconstructed by 3off2 also correctly infers the regulations of *PLL1* by *Gfi1* [37], *Gfi1* by *Lyl1* [38], *Meis1* by *Ldb1* [39], and the regulations of *Lyl1* by *Ldb1* [39] and *Erg* [40]. Finally, the interactions (*Gata2*−*SCL*) [40], (*Gfi1b*−*Meis1*) [41] and (*Gata1*−*Gata2*) [42] are correctly inferred, however, with opposite directions as reported in the literature. Yet, overall 3off2 outperforms most of the other methods tested for the reconstruction of the hematopoietic regulatory subnetwork (Table 1 and Additional file 1: Table S1). Only the Bayesian hill-climbing method using a BDe score leads to comparable results by retrieving 10 out of 11 interactions and correctly orienting 8 of them. These encouraging results from the 3off2 reconstruction method on experimentally proven regulatory interactions (red edges in Fig. 7) could motivate further investigations on novel regulatory interactions awaiting to be tested for their possible role in hematopoiesis (*e.g.* grey edges in Fig. 7).

# **Conclusions**

In this paper, we propose to improve constraint-based network reconstruction methods by identifying structural independencies through a robust quantitative score-based scheme limiting the accumulation of early FN errors and subsequent FP compensatory errors. In brief, 3off2 relies on information theoretic scores to progressively uncover the best supported conditional independencies, by iteratively "taking off" the most likely indirect contributions of conditional 3-point information from every 2-point (mutual) information of the causal graph.

![img-4.jpeg](img-4.jpeg)

**Fig. 5** BARLEY network. [48 nodes, 84 links, 114,005 parameters, Average degree 3.5, Maximum in-degree 4]. Precision, Recall and F-score for skeletons (*dashed lines*) and CPDAGs (*solidlines*). The results are given for Aracne (*black*), PC (*blue*), Bayesian Hill-Climbing (*green*) and 3off2 (*red*)

Earlier hybrid methods have also attempted to improve network reconstruction by combining the concepts of constraint-based approaches with the robustness of Bayesian scores [30, 43–45]. In particular [43], have proposed to exploit an intrinsic weakness of the PC algorithm, its sensitivity to the order in which conditional independencies are tested on finite data, to rank these different order-dependent PC predictions with Bayesian scores. More recently [30], have also combined constraint-based and Bayesian approaches by first identifying both parents and children of each node of the underlying graphical model and then performing a greedy Bayesian hill-climbing search restricted to the identified parents and children of each node. This Max-Min Hill-Climbing (MMHC) approach tends to have a high precision in terms of skeleton but a more limited sensitivity, leading overall to lower skeleton and CPDAG F-scores than 3off2 and Bayesian hill climbing methods on the same benchmark networks, Figures S21-S25. Interestingly, however, the MMHC approach is among the fastest network reconstruction approaches, Figure S26, allowing for scalability to large network sizes [30].

The 3off2 algorithm is expected to run in polynomial time on *typical* sparse causal networks with low in-degree, just like constraint-based algorithms. However, in practice and despite the additional computation of conditional 2-point and 3-point information terms, we found that the 3off2 algorithm runs typically faster than constraint-based algorithms for large enough samples, by avoiding the cascading accumulation of errors that inflate the combinatorial search of conditional independencies in traditional constraint-based approaches. Instead, we found that 3off2 running time displays a similar trend as Bayesian hill-climbing heuristic methods, Figs. 2, 3, 4, 5 and 6.

All in all, the main computational bottleneck of the present 3off2 scheme pertains to the identification of the *best* contributing nodes at each iteration. In the future, it could be interesting to investigate whether a more stochastic version of this 3off2 method, based on choosing *one* significant conditional 3-point information instead of the best one, might simultaneously accelerate the network reconstruction and circumvent possible locally trapped suboptimal predictions through stochastic resampling.

Finally, another perspective for practical applications will be to include the possibility of latent variables and bidirected edges in reconstructed networks.

![img-5.jpeg](img-5.jpeg)

**Fig. 6** HEPAR II network. [70 nodes, 123 links, 1,453 parameters, Average degree 3.51, Maximum in-degree 6]. Precision, Recall and F-score for skeletons (*dashed lines*) and CPDAGs (*solid lines*). The results are given for Aracne (*black*), PC (*blue*), Bayesian Hill-Climbing (*green*) and 3off2 (*red*)

# Appendix

## Complexity of graphical models

The complexity $k_{\mathcal{G}, \mathcal{D}}$ of a graphical model is related to the normalization constant $Z(\mathcal{G}, \mathcal{D})$ of its maximum likelihood as $k_{\mathcal{G}, \mathcal{D}} = \log Z(\mathcal{G}, \mathcal{D})$,

$$
\mathcal{L}_{\mathcal{G}} = \frac{e^{-NH(\mathcal{G}, \mathcal{D})}}{Z(\mathcal{G}, \mathcal{D})} = e^{-NH(\mathcal{G}, \mathcal{D}) - k_{\mathcal{G}, \mathcal{D}}}
\tag{35}
$$

For Bayesian networks with decomposable entropy, *i.e.* $H(\mathcal{G}, \mathcal{D}) = \sum_{i} H(x_i||Pa_{x_i}|)$, it is convenient to use decomposable complexities, $k_{\mathcal{G}, \mathcal{D}} = \sum_{i} k_{x_i||Pa_{x_i}|}$,

$$
\mathcal{L}_{\mathcal{G}} = e^{-N \sum_{i} H(x_i||Pa_{x_i}|) - \sum_{i} k_{x_i||Pa_{x_i}|}}
\tag{36}
$$

such that the comparison between alternative models $\mathcal{G}$ and $\mathcal{G}_{\backslash x \rightarrow y}$ (*i.e.* $\mathcal{G}$ with one missing edge $x \rightarrow y$) leads to a simple local increment of the score,

$$
\begin{aligned}
\frac{\mathcal{L}_{\mathcal{G}_{\backslash x \rightarrow y}}}{\mathcal{L}_{\mathcal{G}}} &= e^{-N I(x; y||Pa_{y}|_{\backslash x}) + \Delta k_{y||Pa_{y}|_{\backslash x}}} \\
I(x; y||Pa_{y}|_{\backslash x}) &= H(y||Pa_{y}|_{\backslash x}) - H(y||Pa_{y}|) \geq 0 \\
\Delta k_{y||Pa_{y}|_{\backslash x}} &= k_{y||Pa_{y}|} - k_{y||Pa_{y}|_{\backslash x}} \geq 0
\end{aligned}
\tag{37}
$$

A common complexity criteria in model selection is the Bayesian Information Criteria (BIC) or Minimal Description Length (MDL) criteria [19, 20],

$$
\begin{aligned}
k_{y||Pa_{y}|} &= \frac{1}{2} (r_y - 1) \prod_{j}^{Pa_{y}} r_j \log N \\
\Delta k_{y||Pa_{y}|_{\backslash x}} &= \frac{1}{2} (r_x - 1) (r_y - 1) \prod_{j}^{Pa_{y,\cdot,y}} r_j \log N
\end{aligned}
\tag{40}
$$

where $r_x$, $r_y$ and $r_j$ are the number of levels of each variable, $x$, $y$ and $j$. The MDL complexity, Eq. 40, is simply related to the normalisation constant reached in the asymptotic limit of a large dataset $N \rightarrow \infty$ (Laplace approximation). The MDL complexity can also be derived from the Stirling approximation on the Bayesian measure [46, 47]. Yet, in practice, this limit distribution is only reached for very large datasets, as some of the least-likely $(r_y - 1) \prod_{j} r_j$ combinations of states of variables are in fact rarely (if ever) sampled in typical finite datasets. As a result, the MDL complexity criteria tends to underestimate the relevance of edges connecting variables with many levels, $r_i$, leading to the removal of false negative edges.

![img-6.jpeg](img-6.jpeg)

**Fig. 7** Hematopoietic subnetwork reconstructed by 3off2. The dataset [36] concerns 18 transcription factors, 597 single cells, 5 different hematopoietic progenitor types. Red and blue edges correspond to experimentally proven activations and repressions, respectively as reported in the literature (Table 1), while grey links indicate regulatory interactions for which no clear evidence has been established so far. Thinner arrows underline 3off2 misorientations

To avoid such biases with finite datasets, the normalisation of the maximum likelihood can be done over all possible datasets with the same number *N* of data points. This corresponds to the (universal) Normalized Maximum Likelihood (NML) criteria [21–24],

$$\mathcal{L}_{\mathcal{G}} = \frac{e^{-NH(\mathcal{G}, \mathcal{D})}}{\sum_{|\mathcal{D}'| = N} e^{-NH(\mathcal{G}, \mathcal{D}')}} = e^{-NH(\mathcal{G}, \mathcal{D}) - k_{\mathcal{G}, \mathcal{D}}^{\text{NML}}} \tag{42}$$

We introduce here the factorized version of the NML criteria [23, 24] which corresponds to a decomposable NML score, $k_{\mathcal{G}, \mathcal{D}}^{\text{NML}} = \sum_{x_i} k_{x_i| | |Pa_{x_i}}^N$, defined as,

$$k_{y| |Pa_{y}}^N = \sum_{j}^{q_p} \log C_{N_{yj}}^r_{x} \tag{43}$$

$$\Delta k_{y| |Pa_{y}|,x} = \sum_{j}^{q_p} \log C_{N_{yj}}^r - \sum_{j}^{q_p / r_x} \log C_{N_{yj}}^r_{x} \tag{44}$$

where *N_{yj}* is the number of data points corresponding to the *j*th state of the parents of *y*, {Pa*y*}, and *N_{yj}* the number of data points corresponding to the *j*'th state of the parents of *y*, excluding *x*, {Pa*y*}, *x*. Hence, the factorized NML score for each node *x* corresponds to a separate normalisation for each state *j* = 1, ..., *q* of its parents and involving exactly *N* data points of the finite dataset,

$$\mathcal{L}_{\mathcal{G}} = e^{-N \sum_{i} H(x_i | |Pa_{x_i})} - \sum_{i} \sum_{j}^{q_j} \log C_{N_{ij}}^r_{i} \tag{45}$$

$$= e^{N \sum_{i} \sum_{j}^{q_j} \sum_{k}^{r_j} \frac{N_{ijk}}{N} \log \left( \frac{N_{ijk}}{N_{ij}} \right)} - \sum_{i} \sum_{j}^{q_j} \log C_{N_{ij}}^r_{i} \tag{46}$$

$$= \prod_{i} \prod_{j} \frac{\prod_{k} \left( \frac{N_{ijk}}{N_{ij}} \right)^{N_{ijk}}}{C_{N_{ij}}^r_{i}} \tag{47}$$

where *N_{ijk}* corresponds to the number of data points for which the *i*th node is in its *k*th state and its parents in their *j*th state, with *N* = ∑_{*k*}*N* *N* *i**j**k*. The universal normalization constant *C* is then obtained by averaging over all possible partitions of the *n* data points into a maximum of *r* subsets, *ℓ* = *ℓ* + *ℓ* = *n* with *ℓ* ≥ 0,

$$C_n^r = \sum_{\ell_1 + \ell_2 + \cdots + \ell_r = n} \frac{n!}{\ell_1! \ell_2! \cdots \ell_r!} \prod_{k=1}^{r} \left( \frac{\ell_k}{n} \right)^{\ell_k} \tag{48}$$

which can in fact be computed in linear-time using the following recursion [23],

$$C_n^r = C_{n}^{r-1} + \frac{n}{r-2} C_{n}^{r-2} \tag{49}$$

Table 1 Interactions reconstructed by 3off2 and alternative methods for a subnetwork of hematopoiesis regulation. $\rightarrow$ indicates a successfully recovered interaction including its direction as reported in the literature (see References). $\rightarrow$ corresponds to a successfully recovered interaction, however, with an opposite direction as reported in the literature. $\neq$ stipulates that no direct regulatory interaction has been inferred, while - corresponds to an undirected link. Note in particular that Aracne does not infer edge direction. See Additional file 1: Table S1 for supplementary statistics


with $\mathcal{C}*{0}^{r}=1$ for all $r, \mathcal{C}*{n}^{1}=1$ for all $n$ and applying the general formula Eq. 48 for $r=2$,

$$ \mathcal{C}*{n}^{2}=\sum*{h=0}^{n}\binom{n}{h}\left(\frac{h}{n}\right)^{h}\left(\frac{n-h}{n}\right)^{n-h} $$

or its Szpankowski approximation for large $n$ (needed for $n>1000$ in practice) [48-50],

$$ \begin{aligned} \mathcal{C}*{n}^{2} & =\sqrt{\frac{n \pi}{2}}\left(1+\frac{2}{3} \sqrt{\frac{2}{n \pi}}+\frac{1}{12 n}+\mathcal{O}\left(\frac{1}{n^{3 / 2}}\right)\right) \ & \simeq \sqrt{\frac{n \pi}{2}} \exp \left(\sqrt{\frac{8}{9 n \pi}}+\frac{3 \pi-16}{36 n \pi}\right) \end{aligned} $$

Then, following the rationale of constraint-based approaches, we can reformulate the likelihood ratio of Eq. 37 by replacing the parent nodes $\left{\mathrm{Pa}*{y}\right}*{; x}$ in the conditional mutual information, $I\left(x ; y \mid\left{\mathrm{Pa}*{y}\right}*{; x}\right)$, with an unknown separation set $\left{u*{i}\right}$ to be learnt simultaneously with the missing edge candidate $x y$,

$$ \frac{\mathcal{L}*{\mathcal{G}*{; y ; i}\left{u_{i}\right}}}{\mathcal{L}*{\mathcal{G}}}=e^{-N I\left(x ; y \mid\left{u_{i}\right}\right)+k_{x ; y \mid\left{u_{i}\right)}} $$

where we have also transformed the asymmetric parentdependent complexity difference, $\Delta k_{y \mid\left{\mathrm{Pa}*{y}\right}*{; x}}$, into a $\left{u*{i}\right}-$ dependent complexity term, $k_{x ; y \mid\left{u_{i}\right}}$, with the same $x y$-symmetry as $I\left(x ; y \mid\left{u_{i}\right}\right)$,

$$ \begin{aligned} k_{x ; y \mid\left{u_{i}\right}}^{\text {MDL }}=\frac{1}{2}\left(r_{x}-1\right)\left(r_{y}-1\right) \prod_{i} r_{u_{i}} \log N \ k_{x ; y \mid\left{u_{i}\right}}^{\text {NML }}=\frac{1}{2} \sum_{i j}^{\left{u_{i}\right}}\left(\sum_{k_{x}}^{r_{x}} \log \mathcal{C}*{N*{k, i j}}^{r_{y}}-\log \mathcal{C}*{N_{j}}^{r_{y}}\right. \ & \left.+\sum_{k_{y}}^{r_{y}} \log \mathcal{C}*{N*{k, i j}}^{r_{y}}-\log \mathcal{C}*{N_{j}}^{r_{y}}\right) \end{aligned} $$

Note, in particular, that the MDL complexity term in Eq. 54 is readily obtained from Eq. 41 due to the Markov equivalence of the MDL score, corresponding to its $x y$ symmetry whenever $\left{\mathrm{Pa}*{y}\right}*{; x}=\left{\mathrm{Pa}*{x}\right}*{; y}$. By contrast, the factorized NML score, Eq. 43, is not a Markov-equivalent score (although its non-factorized version, Eq. 42, is Markov equivalent by definition). To circumvent this non-equivalence of factorized NML score, we propose to recover the expected $x y$-symmetry of $k_{x ; y \mid\left{u_{i}\right}}^{\text {NML }}$ through the simple $x y$-symmetrization of Eq. 44, leading to Eq. 55.

## Additional file

## Additional file 1: Complementary evaluations for the 3off2 inference approach and comparisons with alternative reconstruction methods and parameters values. In this additional file, the results of the 3off2 inference approach are evaluated against other methods in terms of Precision (or positive predictive value), $\operatorname{Prec}=\operatorname{TP} /(\mathrm{TP}+\mathrm{FP})$, Recall or Sensitivity (true positive rate), $\operatorname{Rec}=\operatorname{TP} /(\mathrm{TP}+\mathrm{FN})$, as well as F-score $=2 \times \operatorname{Prec} \times \operatorname{Rec} /(\operatorname{Prec}+\operatorname{Rec})$ and execution time when comparing the CPDAG of the reconstructed network (or its skeleton) to the CPDAG (or the skeleton) of the benchmark network. The alternative methods are the PC algorithm, the Bayesian inference method using the hill-climbing heuristics, the Max-Min Hill-Climbing (MMHC) hybrid method and the Aracne inference approach. (PDF 528 KB)

## Competing interests

The authors declare that they have no competing interests.

## Authors' contributions

SA, LV and HI conceived and performed the research. SA, LV and HI wrote the manuscript. All authors read and approved the final manuscript.

## Acknowledgements

S.A. acknowledges a PhD fellowship from the Ministry of Higher Education and Research and support from Fondation ARC pour la recherche sur le cancer. LV. acknowledges a PhD fellowship from the Région Ile-de-France (DIM Institut des Systèmes Complexes) and H.I. acknowledges funding from CNRS, Institut Curie, Foundation Pierre-Gilles de Gennes and Région Ile-de-France.

## Publication costs

Publication costs for this article were funded by the Région Ile-de-France.

## Declarations

This article has been published as part of BMC Bioinformatics Volume 17 Supplement 2, 2016: Bringing Maths to Life (BMTL). The full contents of the supplement are available online at http://www.biomedcentral.com/ bmcbioinformatics/supplements.

Published: 20 January 2016

## Submit your next manuscript to BioMed Central and we will help you at every step:

- We accept pre-submission inquiries
- Our selector tool helps you to find the most relevant journal
- We provide round the clock customer support
- Convenient online submission
- Thorough peer review
- Inclusion in PubMed and all major indexing services
- Maximum visibility for your research

Submit your manuscript at www.biomedcentral.com/submit
(1) BioMed Central