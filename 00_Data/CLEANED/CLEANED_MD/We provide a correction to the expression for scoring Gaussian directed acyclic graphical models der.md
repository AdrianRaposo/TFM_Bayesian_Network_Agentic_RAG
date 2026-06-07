# ADDENDUM ON THE SCORING OF GAUSSIAN DIRECTED ACYCLIC GRAPHICAL MODELS 

By Jack Kuipers, Giusi Moffa and David Heckerman

Regensburg University, Regensburg University and Microsoft Research
We provide a correction to the expression for scoring Gaussian directed acyclic graphical models derived in Geiger and Heckerman [Ann. Statist. 30 (2002) 1414-1440] and discuss how to evaluate the score efficiently.

Gaussian directed acyclic graph (DAG) models represent a particular type of Bayesian networks where the node variables are assumed to come from a multivariate Gaussian distribution. The Bayesian Gaussian equivalent (BGe) score was introduced in Geiger and Heckerman (1994, 2002), Heckerman and Geiger (1995) for learning such networks.

For brevity, we omit formal definitions and refer the reader to Geiger and Heckerman (2002), while following their notation in considering DAG models $m$ with $n$ nodes corresponding to the set of variables $\mathbf{X}=\left\{X_{1}, \ldots, X_{n}\right\}$. Let $m^{h}$ be the model hypothesis that the true distribution of $\mathbf{X}$ is faithful to the DAG model $m$, meaning that it satisfies only and all the conditional independencies encoded by the DAG. For a complete random data sample $d=\left\{\mathbf{x}_{1}, \ldots, \mathbf{x}_{N}\right\}$ with $N$ observations and a complete DAG model $m_{c}$, the marginal likelihood is [Geiger and Heckerman (2002), Theorem 2]

$$
p\left(d \mid m^{h}\right)=\prod_{i=1}^{n} \frac{p\left(d^{\mathbf{P a}_{i} \cup\left\{X_{i}\right\}} \mid m_{c}^{h}\right)}{p\left(d^{\mathbf{P a}_{i}} \mid m_{c}^{h}\right)}
$$

where $\mathbf{P a}_{i}$ are the parent variables of the vertex $i$ and $d^{\mathbf{Y}}$ is the data restricted to the coordinates in $\mathbf{Y} \subseteq \mathbf{X}$. The BGe score is the posterior probability of $m^{h}$ which is proportional to the marginal likelihood in (1) and the graphical prior; see equation (2) of Geiger and Heckerman (2002).

Different DAGs which encode the same set of conditional independencies are said to belong to an equivalence class. Along with ensuring that all

[^0]
[^0]:    Received February 2014.
    AMS 2000 subject classifications. 62-07, 62F15, 62H99.
    Key words and phrases. Gaussian DAG models, Bayesian network learning, BGe score.
    This is an electronic reprint of the original article published by the Institute of Mathematical Statistics in The Annals of Statistics, 2014, Vol. 42, No. 4, 1689-1691. This reprint differs from the original in pagination and typographic detail.

DAGs in the same equivalence class are scored equally, the modularity of the score allows the steps in structure MCMC [Madigan and York (1995)] to be evaluated much more efficiently. Order MCMC [Friedman and Koller (2003), on the related space of triangular matrices] as well as the edge reversal move of Grzegorczyk and Husmeier (2008) would not be possible without it.

For Gaussian DAG models, the likelihood is a multivariate normal distribution with mean $\boldsymbol{\mu}$ and precision matrix $W$. The need for global parameter independence, so that the expression of the score in (1) holds, implies that the prior distribution of $(\boldsymbol{\mu}, W)$ must be normal-Wishart [Geiger and Heckerman (2002)]. The parameter $\boldsymbol{\mu}$ is taken to be normally distributed with mean $\boldsymbol{\nu}$ and precision matrix $\alpha_{\mu} W$, for $\alpha_{\mu}>0 . W$ is Wishart distributed with positive definite parametric matrix $T$ (the inverse of the scale matrix) and degrees of freedom $\alpha_{w}$, with $\alpha_{w}>n-1$. As detailed in the supplementary material [Kuipers, Moffa and Heckerman (2014)], one finds

$$
\begin{aligned}
& p\left(d^{\mathbf{Y}} \mid m_{v}^{h}\right) \\
& \quad=\left(\frac{\alpha_{\mu}}{N+\alpha_{\mu}}\right)^{l / 2} \frac{\Gamma_{l}\left(\left(N+\alpha_{w}-n+l\right) / 2\right)}{\pi^{l N / 2} \Gamma_{l}\left(\left(\alpha_{w}-n+l\right) / 2\right)} \frac{\left|T_{\mathbf{Y Y}}\right|^{\left(\alpha_{w}-n+l\right) / 2}}{\left|R_{\mathbf{Y Y}}\right|^{\left(N+\alpha_{w}-n+l\right) / 2}}
\end{aligned}
$$

where $l$ is the size of $\mathbf{Y}, A_{\mathbf{Y Y}}$ means selecting the rows and columns corresponding to $\mathbf{Y}$ of a matrix $A$,

$$
\Gamma_{l}\left(\frac{x}{2}\right)=\pi^{l(l-1) / 4} \prod_{j=1}^{l} \Gamma\left(\frac{x+1-j}{2}\right)
$$

is the multivariate Gamma function and

$$
R=T+S_{N}+\frac{N \alpha_{\mu}}{\left(N+\alpha_{\mu}\right)}(\boldsymbol{\nu}-\overline{\mathbf{x}})(\boldsymbol{\nu}-\overline{\mathbf{x}})^{\mathrm{T}}
$$

is the posterior parametric matrix involving

$$
\overline{\mathbf{x}}=\frac{1}{N} \sum_{i=1}^{N} \mathbf{x}_{i}, \quad S_{N}=\sum_{i=1}^{N}\left(\mathbf{x}_{i}-\overline{\mathbf{x}}\right)\left(\mathbf{x}_{i}-\overline{\mathbf{x}}\right)^{\mathrm{T}}
$$

the sample mean and sample variance multiplied by $(N-1)$.
The result in (2) is identical to equation (18) of Geiger and Heckerman (2002), once some factors are cancelled, apart from the manner in which the matrix elements are chosen. The result in Geiger and Heckerman (2002) replaces the $T_{\mathbf{Y Y}}$ and $R_{\mathbf{Y Y}}$ by $T_{\mathbf{Y}}$ and $R_{\mathbf{Y}}$, where $A_{\mathbf{Y}}=\left(\left(A^{-1}\right)_{\mathbf{Y Y}}\right)^{-1}$. Inverting the matrices before the elements are selected and then inverting again [as in Geiger and Heckerman (2002)] we found inconsistent behavior on simulated data.

We may further compare to equation (24) of Heckerman and Geiger (1995), which with the current notation becomes

$$
p\left(d^{\mathbf{Y}} \mid m_{c}^{h}\right)=\left(\frac{\alpha_{\mu}}{N+\alpha_{\mu}}\right)^{l / 2} \frac{\Gamma_{l}\left(\left(N+\alpha_{w}\right) / 2\right)}{\pi^{l N / 2} \Gamma_{l}\left(\alpha_{w} / 2\right)} \frac{\left|T_{\mathbf{Y Y}}\right|^{\alpha_{w} / 2}}{\left|R_{\mathbf{Y Y}}\right|^{\left(N+\alpha_{w}\right) / 2}}
$$

while incorrectly defining the $S_{N}$ in the $R$ in (4) as the sample variance. However, the same terminology, with the correct formula for $S_{N}$, is used in Geiger and Heckerman (1994) whose equation (12) is otherwise identical to (6).

The difference in the powers of the determinants between (2) and (6) could lead to a subtle, and hard to predict, change in the scores. There is also the same loss of $l$-dependence in the arguments of the multivariate gamma functions. The ratio of gamma functions for each node now actually decreases with $l$ while the ratio from (2) increases instead. As discussed in the supplementary material [Kuipers, Moffa and Heckerman (2014)], using (6) instead of (2) effectively penalises each node with $l$ parents by a factor $\sim N^{l}$, giving a substantial bias toward sparse DAGs. This bias is likely to be present in early works implementing the score of Heckerman and Geiger (1995) and possibly remains in legacy code.

# SUPPLEMENTARY MATERIAL 

Deriving and simplifying the BGe score (DOI: 10.1214/14-AOS1217SUPP; .pdf). We detail the steps used to derive (2) and simplify the ratios appearing in (1) to improve the numerical computation of the score.
