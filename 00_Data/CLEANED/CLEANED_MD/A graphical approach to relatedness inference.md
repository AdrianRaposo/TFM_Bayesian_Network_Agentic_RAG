# NIH Public Access 

Author Manuscript
Theor Popul Biol. Author manuscript; available in PMC 2007 September 28.
Published in final edited form as:
Theor Popul Biol. 2007 March ; 71(2): 213-229.

## A Graphical Approach to Relatedness Inference

Anthony Almudevar<br>Department of Biostatistics and Computational Biology, University of Rochester, Rochester, NY, 14642, USA, Tel 585-275-6992, Fax 585-273-1031, anthony almudevar@urmc.rochester.edu


#### Abstract

The estimation of relatedness structure in natural populations using molecular marker data has become an important tool in population biology, resulting in a variety of estimation procedures for specific sampling scenarios. In this article a general approach is proposed, in which the detailed relationship structure, typically a pedigree graph or partition, is considered to be the object of inference. This makes available tools used in complex model selection theory which have demonstrated effectiveness. An important advantage of this approach is that it permits a fully Bayesian approach to the problem, providing a principled and accessible way to measure statistical error. The approach is demonstrated by applying the minimum description length principle. This technique is used in model selection to provide a rational way of comparing models of varying complexity. We show how the resulting score may be interpreted and applied as a Bayesian posterior density.


## Keywords

Pedigree reconstruction; graphical models; Bayesian inference; minimum description length

## 1 Introduction

The collection of molecular marker data in studies of natural populations permits the statistical estimation of relatedness structure among individuals. Such information is crucial in the observation and measurement of quantities such as fitness, trait heritability, migration or effective population size. Relatedness itself may be the subject of interest in selective breeding or conservation applications. The growing importance of this type of analysis is indicated in recent surveys, including Blouin (2003),Jones and Ardren (2003),Garant and Kruuk (2005) and Thomas (2005).

Relatedness inference can vary in level of detail, ranging from aggregate measures of relatedness, pairwise estimates of relatedness type, or fully specified pedigrees (ie. family trees). Additionally, interest may be confined to a particular relationship type, in particular, parent-offspring relationships (eg Thompson and Meagher 1987;Marshall et al 1998;Nielsen et al 2001) or sibling relationships (eg Almudevar 1999;Thomas and Hill 2002;Butler 2004;Wang 2004;Konovalov 2005).

As an alternative to the categorical assignment of parentage, some authors have developed the idea of fractional assignment, in which a parentage assignment to a fixed offspring consists of an attribution of weights to each candidate father, the size of the weight corresponding to the evidence of parentage. The weights may be forced to sum to one, and so may be interpreted as

[^0]
[^0]:    Publisher's Disclaimer: This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

a probability distribution. This method has been developed in, for example, Devlin et al 1988,Smouse and Meagher (1994),Nielsen et al 2001 and Neff et al 2001. There are two rationales for this approach. The first is that because parentage assignment involves statistical error, it is appropriate to express such inference in the form of a posterior distribution, so that the uncertainty of the assignment can be assessed. Furthermore, this approach allows the introduction of auxilliary information (age, proximity or other mating attributes) in the form of a prior distribution, allowing a formal Bayesian approach. The second rationale is that when the object of study is the inference of mating or fitness patterns at the population level, individual assignment is not needed, and the aggregate measures of interest are more naturally expressed in terms of fractional paternal contributions.

Various methods for the measurement of statistical error have been proposed, in addition to the fractional assignment methods discussed above. The commonly used parentage assignment algorithm CERVUS, proposed in Marshall et al 1998, is based on a formal hypothesis test. A Bayesian approach for sibling relationships was proposed in Emery et al 2001, and a bootstrap approach to measuring statistical error in sibling partitions was proposed in Almudevar (2001a). The estimation of statistical error in relationship estimation is often accomplished by simulating from known pedigrees. However, a complete and proper inference requires an estimate of statistical error without the benefit of a known pedigree, and such methodologies remain to be developed for many of the procedures discussed above.

Given the variety of objectives and sampling regimes associated with relationship inference, it seems unlikely that any single methodology will be an optimal choice for all applications. Nonetheless, a general framework should be possible by concentrating attention on single joint relationship structures. Essentially, we define a parameter space $\Theta$ to be a set of combinatorical objects, such as pedigree graphs (as in Almudevar 2003), or partitions generated by sibling groups estimated in the various techniques described above. Principles of statistical inference may be applied, leading to rigorous inferential statements expressible in terms of $\Theta$.

There are two significant challenges associated with this approach. First, comparing large combinatorical objects presents special difficulties when they differ in complexity. In particular, likelihood scores tend to favor more complex explanations. This is manifest, for example, in the tendency of likelihood scores to split true sibling groups (Thomas and Hill 2000;Butler 2004). Alternative scores, such as the Simpson's Index proposed in Butler (2004) (see also Konovalov 2005), favor larger sibling groups and are therefore better able to preserve such family structure. This suggests that the selection of a method which properly accounts for the sample size and relationship complexity is crucial.

The second challenge is the formation of rigorous inferential statements concerning $\Theta$. Here, Bayesian model averaging (BMA) (Hoeting et al 1999) may be used to assign a confidence level to any model feature. Given data $X$, suppose we may construct a posterior density $\varphi(\theta \mid$ $X$ ) on $\Theta$, the space of pedigree structures. The posterior probability of any feature, for example, " $a$ is a sibling or half-sibling of $b$ ", is calculated by summing the posterior density over all $\theta$ $\in \Theta$ possessing that feature. Thus, even when the objective is the estimation some aggregate feature of the pedigree, and a pedigree estimate is not strictly needed, the more general approach allows a wide variety of problems to be solved using essentially one single methodology.

In this article, we will develop this idea for pedigree graphs, using the minimum description length (MDL) principle due to Rissanen $(1978,1983)$ as a means of comparing candidate models. The objective of the MDL principle is to uncover regularity which permits the most compressed representation of the data $X$. This regularity is presumed to have a natural interpretation with respect to the models in $\Theta$, so the best model is taken to be one which permits the most compression. Because the representation must also include the model itself (and more

complex models require longer representations) this method tends to avoid the inference of spurious complexity common in unadjusted likelihood methods. Of course, the data compression is not actually performed. We only need an estimate of the length of the resulting data file that would follow compression based on a specific model. Well known techniques from coding theory may be used to do this. For a recent survey of this field see Grünwald et al 2005 .

The methods developed will be tested on simulated data from test pedigrees in Section 4, and on a single cohort of 857 North Atlantic cod larvae, supplemented with an additional simulated parental cohort in Section 5.

A version of the software used in this article may be downloaded at http:// www.urmc.rochester.edu/smd/biostat/projects/help/PC/Software_Listings.htm.

# 2 Bayesian model averaging for graphical models 

Multigenerational pedigrees possess a natural graph structure, so we will develop our methodology on that basis. We take a directed graph $\theta=(E, V)$ to be a set $V$ of labelled objects (nodes) and a set $E$ of directed edges, defined as an ordered pair from $V$. Each node corresponds to a subject (labelled $1, \ldots, N_{l}$ ), and an edge $j \rightarrow i \in E$ implies a parent-offspring relationship for $j$ and $i$, respectively. Note that $\theta$ must be a directed acyclic graph (DAG) with no more than 2 parents for any child node.

We associate with each node $i$ an observation pair $\left(X_{i}, Y_{i}\right)$ consisting of all data associated with that subject. The datum $X_{i}$ represents heritable data, that is, data for which the conditional densities $f\left(X_{i} \mid X_{j}\right)$ and $f\left(X_{i} \mid X_{j}, X_{k}\right)$ are known when $j, k$ are parents of $i$. The datum $Y_{i}$ represents demographic data (age, sex, geographic) which can used to test the admissibility of a mating relationship or a parent-offspring relationship. Denote the complete data sets $X=\left(X_{1}, \ldots\right.$, $\left.X_{N_{l}}\right)$ and $Y=\left(Y_{1}, \ldots, Y_{N_{l}}\right)$. The data is assumed complete in the sense that all relationships can be expressed using parent-offspring pairs (for example, the parents of sibling groups present in the sample are also present in the sample).

Let $\Theta$ be the set of all DAGs with nodes $1, \ldots, N_{l}$ having a maximum of two parents. For any $\theta \in \Theta$ let $S_{i}^{\theta}$ be the set of parents of $i$. We assume that the density of $X$ may be written

$$
f\left(x_{1}, \ldots, x_{N_{l}}\right)=\prod_{i=1}^{N_{l}} f\left(x_{i} \mid X_{j}=x_{j}, j \in S_{i}^{\theta}\right)
$$

This will be the case for unlinked genotypic data. Under (1), the pair $(\theta, f)$ is an example of a Bayesian network, a graph-based model used to describe multivariate data characterized by causal relationships (Pearl 1988). Bayesian networks have been used in a variety of fields ranging from the modelling of cell regulatory networks to the design of artificial intelligence applications (Sebastiani et al 2005;Jordan 1998), and an extension of such methodology to the modelling of pedigrees would seem natural.

### 2.1 Structure of model averaging

Inferential statements will be concerned with subsets $E \subset \Theta$, for example $E=\{\theta \in \Theta: i$ and $j$ are unrelated $\}$. Given a score function $\varphi(\theta \mid X)$ interpretable as a posterior density on the space of graphs, we may assign a posterior probability for $E$

$$
P(E \mid X)=\sum_{\theta \in E} \phi(\theta \mid X)
$$

A marginal posterior density for a specific quantity, say the fitness $w_{i}$ of individual $i$ is then given by

$$
\phi_{w_{i}}(w \mid X)=\sum_{\theta: w_{i}=w} \phi(\theta \mid X)
$$

The space of graphs is generally too large to enumerate, so in practice (2) or (3) are estimated using computer generated samples from $\varphi(\theta \mid X)$. Where independent sampling is not possible, Monte Carlo Markov chains (MCMC) are a commonly used alternative, but present certain difficulties. This method requires a definition of a graph neighborhood $N(\theta)$ specified for each $\theta \in \Theta$. A sample $\left(\theta_{1}, \ldots, \theta_{j}, \theta_{j+1}, \ldots\right)$ from $\varphi(\theta \mid X)$ is generated by randomly selecting $\theta_{j+1}$ from $N\left(\theta_{j}\right)$ according to a probability law defined by the Hastings-Metropolis criterion (Hastings 1970). The effectiveness of such a procedure depends on the ability to define a neighborhood $N(\theta)$ which is small enough to ensure that a sizable fraction of graphs $\theta^{\prime} \in N(\theta)$ have a score similar to that of $\theta$, but large enough to allow the process to traverse a sufficiently large subset of $\Theta$. In the case of DAGs, this is usually achieved by defining $N(\theta)$ to be those graphs obtainable by performing a simple operation on $\theta$, such as deleting an edge, adding an edge or reversing an edge (see Madigan and York 1995). The difficulty in this approach is that such an operation on a DAG may introduce a cycle into the subsequent graph. Prohibiting such transitions has implications for the performance of such a sampler (Friedman and Koller 2003).

# 2.2 The advantage of order constraints 

Age data can play a significant role in the design of such samplers. Suppose we are given an ordering of the nodes. Any directed graph constructed by selecting for each node an admissible set of parents of higher order will be a DAG (Almudevar 2003). The set of graphs $\Theta$ that are admissible under such an order constraint then assumes a convenient product space form, equivalent to independent selections of admissible parent sets for each node. The neighborhood $N(\theta)$ then becomes easy to define, eliminating the need to flag transitions to non-acyclic graphs. Of course, such an ordering will be imposed by age data.

Possibly, only partial age or ordering data is available, in which case it is still possible to confine the search space to those graphs conforming to the order. For example, we may be able to partition a sample into distinct generations. If a parent must come from an older generation, then the graph space $\Theta$ retains the product form of the full ordering constraint. If a parent may come from the same generation as an offspring, the product form no long holds, since the selection of the parents of two members of the same generation cannot be made independently.

It is possible to exploit the desirable properties of the order constraint when age data is not available. If integration or maximization operations under an order constraint are considerably simplified, then we may replace the graph search space with an ordering search space, which is smaller and more tractable. This approach was used in Almudevar (2003) to determine maximum likelihood pedigrees using simulated annealing, and in Friedman and Koller (2003) to construct a Bayesian posterior density on the space of Bayesian networks. One drawback of the latter approach is that orderings do not partition the graph space, and the number of orderings to which a graph conforms varies, making it difficult to reconstruct a given posterior density. Other approaches include a data-based pruning approach (Madigan and Raftery 1994), which reduces the number of graphs to be considered. The case of partial orderings has been considered in Dash and Cooper (2004). Finding an efficient method of calculating a posterior density over graphical models remains an important area of research.

# 2.3 Posterior densities in product form 

The construction of a posterior density is particularly convenient when $\varphi$ assumes a product form and an ordering is available. We may express the ordering by associating with individual $i$ the set of all parent sets $H_{i}^{\theta}=\left(s_{i, 1}, \ldots, s_{i, n_{i}}\right)$ which conform to that ordering. If the posterior density has form

$$
\phi(\theta \mid X)=\prod_{i=1}^{N_{I}} \phi_{i}\left(X_{i} \mid s_{i}^{\theta}\right)
$$

for admissible $\theta$ then the parent assignments under $\varphi$ are independent. Thus, to sample a pedigree $\theta$ from $\varphi$ we can sample independently for each $i$ a parent set $s \in H_{i}^{\theta}$ from distribution

$$
P\left(S_{i}^{\theta}=s \mid X\right)=\left\{\begin{array}{cc}
\phi_{i}\left(X_{i} \mid s\right) & \\
\sum_{s^{\prime} \in H_{i}^{\theta}} \phi_{i}\left(X_{i} \mid s^{\prime}\right) & : s \in H_{i}^{\theta} \\
0 & ; s \notin H_{i}^{\theta}
\end{array}\right.
$$

so that we need not rely on MCMC methods. In this article we will examine two posterior densities, both of which are in product form.

## 3 The MDL principle

The minimum description length (MDL) principle was first proposed by Rissanen (1978, 1983), and is based on the relationship between data compression and data regularity. Suppose a data set $X$ is to be coded as a binary sequence $b(X)$. The coding must be such that $X$ may be recovered from $b(X)$ using a general purpose algorithm. An important principle of coding theory states that the more regularity exists in $X$, the shorter the length of $b(X)$, provided efficient coding techniques which are able to exploit the given form of regularity are used.

In a modelling selection context, if $X$ is generated by a model $\theta \in \Theta$ then knowledge of that model can be used to further compress $X$. Of course, when the model is one of a set of candidate models, we need to know which model was used to generate the compression. We can denote the encoded data $b(X \mid \theta)$, using notation which emphasizes the dependence of the coding on the model. We also need to encode $\theta$, as $b(\theta)$, the knowledge of which is needed to decode $b$ $(X \mid \theta)$. The total code is then $b(X \mid \theta) b(\theta)$. Let $B(X \mid \theta)$ and $B(\theta)$ represent the code lengths of $b(X \mid \theta)$ and $b(\theta)$, giving total code length $B(\theta \mid X)=B(X \mid \theta)+B(\theta)$. The MDL principle states that the model which minimizes $B(\theta \mid X)$ provides the best explanation for the data. In this section we will discuss the application of the MDL principle to the problem of pedigree graph inference.

Assume that we have $N_{L}$ loci of independently segregating genotypic data. We assume that population genotype frequencies are known. Let $X_{i}$ denote the genotypic data for individual $i$. Let $n(k, i)$ be the number of candidate parent groups of size $k=0,1,2$ available to offspring $i$. This quantity is possible affected by demographic data $Y$. For example if $N_{I}=100$ and 50 individuals (of unknown sex) are old enough to be parents of $i$, then $n(0, i)=1, n(1, i)=50, n$ $(2, i)=(50 \times 49) / 2$. These numbers would be adjusted accordingly if sex data were available. A coding scheme conforming to the MDL principle was developed for this model (see equations (10)-(12) in Appendix), resulting in estimated code length

$$
\begin{aligned}
B(X \mid \theta) & =-\log _{2} L(\theta \mid X) \\
B(\theta) & =\sum_{i=1}^{N_{I}} \log _{2}\left(n\left(\left|S_{i}^{\theta}\right|, i\right)\right)
\end{aligned}
$$

where $L(\theta \mid X)$ is the pedigree likelihood function

$$
L(\theta \mid X)=\prod_{i=1}^{N_{I}} P\left(X_{i} \mid S_{i}^{\theta}\right)
$$

The conditional probability $P\left(X_{i} \mid S_{i}^{\theta}\right)$ is the probability of genotype $X_{i}$ given parent set $S_{i}^{\theta}$, and is easily calculated using the laws of Mendelian inheritance. We obtain an interpretable density through the exponential transformation

$$
\begin{aligned}
\phi(\theta \mid X) & =(1 / 2)^{B(X \mid \theta)+B(\theta)} \\
& =L(\theta \mid X) \prod_{i=1}^{N_{I}} \frac{1}{n\left(\left|S_{i}^{\theta}\right|, i\right)}
\end{aligned}
$$

This transformed MDL score has a natural Bayesian interpretation under which a prior density on the space of models is given by

$$
P(\theta) \propto \prod_{i=1}^{N_{I}} \frac{1}{n\left(\left|S^{\theta}\right|, i\right)}
$$

then taking $P(X \mid \theta)=L(\theta \mid X)$ we have posterior density

$$
\phi(\theta \mid X) \propto P(\theta \mid X)
$$

The prior and posterior densities possess a number of desirable features. First of all, they may be written in product form:

$$
\phi(\theta \mid X)=\prod_{i=1}^{N_{I}} \frac{P\left(X_{i} \mid S_{i}^{\theta}\right)}{n\left(\left|S_{i}^{\theta}\right|, i\right)}
$$

simplifying posterior sampling as discussed in Section 2.3. Second of all, important marginal features of the prior do not depend on $N_{I}$. For example, under the prior density, the probability of any parent set of size $k$ for individual $i$ is proportional to $1 / n(k, i)$, hence the prior distribution of the number of parents of an individual is given by

$$
P\left(\left|S_{i}^{\theta}\right|=k\right) \propto \sum_{j=1}^{n(k, i)} \frac{1}{n(k, i)}=1
$$

that is, $P\left(\left|S_{i}^{\theta}\right|=k\right)=1 / 3$. In contrast, a likelihood score corresponds to a uniform prior on $\Theta$ and so the prior distribution of parent set size would be defined by $P\left(\left|S_{i}^{\theta}\right|=k\right) \propto n(k, i)$. We would generally expect $n(k, i)$ to be an order $k$ polynomial in $N_{I}$, so that the effect of increasing $N_{I}$ would be to increase $P\left(\left|S_{i}^{\theta}\right|=2\right)$. In other words, under a likelihood score, the prior expectation of complexity increases with $N_{I}$, introducing a complexity bias into any BMA procedure.

# 4 Simulation study 

To evaluate the proposed methodology, a simulation study was undertaken based on genotype data simulated on known test pedigrees. These test pedigrees are generated from two base pedigrees, labelled $A$ and $B$, shown in Figure 1. Base pedigree $A$ is the union of subpedigrees $A 1$ and $A 2$, similarly, $B=B 1 \cup B 2$. The subpedigrees are taken to represent fitness classes in the sense that each mating in such a class always produces the same number of offspring. A founder is an individual of the oldest generation. The characteristics of the base pedigrees are summarized in Table 1. The simulation study will be concerned with the inference of the number of descendants of a founder.

Each base pedigree generates 4 test pedigrees, in each case using the largest number of replications resulting in a pedigree not exceeding target sizes $N_{I}=200,500,2000,10000$. This results in 8 test pedigrees, with sizes ranging from 152 and 150 ( $A$ replicated once, $B$ replicated twice) to 9880 and 9975 ( $A$ replicated 65 times, $B$ replicated 133 times). For convenience, pedigree sizes are referred to by the target sizes. The pedigrees are selected to represent distinct sampling and mating characteristics. Pedigrees $A 1$ and $A 2$ may be described as closed systems, in the sense that matings occur between offsprings of proximate families, and parents of all nonfounders in the sample are also in the sample. Pedigrees $B 1$ and $B 2$ represent open systems, in the sense that offspring of individuals in the sample mate with individuals without ancestors in the sample.

We will consider two pedigree scores, the likelihood score and the MDL score defined in (5). We assume age (ie. generation) data is given. Parents are always assumed to be of the previous generation. This assumption is incorporated into the definition of the number of candidate parents $n(k, i)$. No sex information is used. We assume a locus has eight alleles with allele frequencies conforming to a Zipf distribution $\left(p_{i} \propto 1 / i, i=1, \ldots, 8\right.$, with heterozygosity $=$ $79.3 \%$ ). The simulation study is repeated using 8,10 and 12 loci. The posterior densities used are in product form and can be estimated using independent simulations (see Section 2.3).

For each pedigree let $\mathcal{G}_{F}$ denote the set of all founders, and let $d_{i}$ denote the number of descendants for $i \in \mathcal{G}_{F}$. Let $\mathcal{G}_{P}^{a}, \mathcal{G}_{F}^{b}$ be the founders from the higher and lower fitness class respectively, and let $d^{a}, d^{b}$ be the average number of founder descendants among the respective classes. For example, in a pedigree of type $A, \mathcal{G}_{F}^{a}$ consists of all founders of fitness $4, \mathcal{G}_{F}^{b}$ consists of all founders of fitness 2 , so that $d^{a}=84$ and $d^{b}=14$.

Additionally, note that a pedigree $\theta$ can be described by two parent specifications for each individual (one or both of which may be 'population' in the case of founders). A distance $D$ $(\theta, \theta)$ between a pedigree estimate $\theta$ and the true pedigree $\theta$ is taken to be the number of erroneous parent specifications ( 0,1 or 2 for each individual).

To summarize, we consider 8 test pedigrees, varying the number of loci $L=8,10,12$ for each, for a total of 24 scenarios. For each scenario two simulation experiments are performed:

## E1.

Simulate genotypes $X$ for test pedigree. Construct maximum/minimum score pedigree using likelihood and MDL score. Do $N=10000$ independent trials.

## E2.

Simulate genotypes $X$ for a single pedigree. Sample $N=2000$ replications from the posterior density based on likelihood and MDL scores given $X$.

The analysis will be as follows. For experiment E1 let $\theta(j)$ be the estimated pedigree for trial $j$. For each founder in $\mathcal{F}_{F}^{a}$ and $\mathcal{F}_{F}^{b}$ calculate the number of descendants based on $\theta(j)$. Report $d^{a}(j), d^{b}(j)$, the average number of descendants for founders in $\mathcal{F}_{F}^{a}, \mathcal{F}_{F}^{b}$ respectively. Then calculate $D(j)=D(\theta(j), \theta)$, where $\theta$ is the true pedigree. We report:

$$
\begin{aligned}
a^{a} & =(1 / N) \sum_{j=1}^{N} d^{a}(j) \\
a^{b} & =(1 / N) \sum_{j=1}^{N} d^{b}(j) \\
R M S E^{a} & =\left[(1 / N) \sum_{j=1}^{N}\left(d^{a}(j)-d^{a}\right)^{2}\right]^{1 / 2} \\
R M S E^{b} & =\left[(1 / N) \sum_{j=1}^{N}\left(d^{b}(j)-d^{b}\right)^{2}\right]^{1 / 2} \\
D & =(1 / N) \sum_{j=1}^{N} D(j)
\end{aligned}
$$

that is, the mean estimate and root mean square error (RMSE) of $d^{a}$ and $d^{b}$, and the mean distance $\mathcal{D}$, where $N=10000$.

For experiment E2 given simulated data $X$ graphs $\theta(1), \ldots, \theta(N)$ are sampled from the posterior density. Here $N=2000$. Let $D(j)=D(\theta(j), \theta)$. For each founder $i \in \mathcal{F}_{F}^{a} \cup \mathcal{F}_{F}^{b}$ the posterior density of $d_{i}$ is sampled, giving $d_{i}(1), \ldots, d_{i}(N)$, which are calculated directly from $\theta(1), \ldots, \theta$ $(N)$. For each founder the following quantities are calculated:

$$
\begin{aligned}
& \partial_{i}=(1 / N) \sum_{j=1}^{N} d_{j}(j) \\
& S D_{i}=\left[(1 /(N-1)) \sum_{j=1}^{N}\left(d_{j}(j)-\partial_{j}\right)^{2}\right]^{1 / 2} \\
& Q P_{i}=(1 / N) \sum_{j=1}^{N} i\left(d_{j}(j)<d^{0}\right)+(1 / 2) i\left(d_{j}(j)=d^{0}\right]
\end{aligned}
$$

where $d^{0}$ is the true number of descendants (that is, $d^{a}$ or $d^{b}$ as appropriate). Then $\bar{d}_{i}$ and $S D_{i}$ are the mean and standard deviation of the posterior density of $d_{i}$. Additionally, $Q P_{i}$ is the quantile position of the true number of descendants $d^{0}$. This definition centers the position. For example, if the frequencies of the replications are (500/2000, 1000/2000, 500/2000) for quantities $(38,39,40)$, and the true value is $d^{0}=39$, then the quantile position evaluates to $Q P_{i}=0.5$. In general, if the posterior density gives accurate coverage, we would expect $Q P_{i}$ to be close to 0.5 . If, in addition, $S D_{i}$ is reasonably small, the posterior density becomes a useful inference tool. We then report

$$
\begin{aligned}
& \underset{Q P}{\sim} \stackrel{\sim}{=}=\text { median } \underset{i \in \mathcal{F}}{i \in \mathcal{F}} Q P_{i} \\
& \underset{D}{\sim} \underset{\sim}(1 / N) \sum_{j=1}^{N} D(j)
\end{aligned}
$$

where $n^{a}, n^{b}$ are the numbers of founders in $\mathcal{F}_{F}^{a}, \mathcal{F}_{F}^{b}$ respectively.
The summaries $\overline{d^{a}}, \overline{d^{b}}, R M S E^{a}, R M S E^{b}$ defined in (6) for experiment E1 for the case of 10 loci are shown in Figure 2 (see Table 3 for numerical summaries). For pedigree type A the MLE score results in a marginally more accurate estimate of $\left(d^{a}, d^{b}\right)$. For pedigree type $B$, the MDL score gives a significantly better estimate of $\left(d^{a}, d^{b}\right)$. Note the significant overestimation for the $N_{I}=2000,10000$ scenarios for the MLE score, not exhibited by the MDL score. The graph distances are given in Table 3, and similarly indicate marginally more accuracy of the MLE score for pedigree type $A$ and significantly more accuracy for the MDL score for pedigree type $B$. To summarize, there is a marginal advantage to using the MLE score for pedigree type $A$, and a more significant advantage to the MDL score for pedigree type $B$, which represent precisely the scenario in which complexity control can be expected to exhibit an advantage.

We next examine how this situation changes when the amount of information is decreased to 8 loci. The summaries are given in Table 2. For pedigree $A$, the accuracy of the MLE has degraded to some degree from the 10 loci scenario, with estimates of $d^{a}$ and $d^{b}$ tending to shrink towards a common value for $N_{I}=2000,10000$ due to misassignment. The MDL score significantly underestimates $\left(d^{a}, d^{b}\right)$ for $N_{I}=10000$. This effect is to be expected, since the relative contribution of the data to the score is directly dependant on the number of loci, while the remaining terms of the score tend to penalize relationships. For pedigree type $B$, the MLE score tends to overestimate, $\left(d^{a}, d^{b}\right)$, where the MDL score tends to underestimate. Note that for pedigree type $B$ the MDL score is more accurate by all $R M S E$ and distance measures.

Table 4 gives summaries for the 12 loci scenario. This increase in information suffices to produce accurate estimates of $\left(d^{a}, d^{b}\right)$ with either the MLE or MDL score for pedigree type $A$. The summaries can be seen to be very similar. The difference in accuracy for pedigree type $B$ is more striking. While very small bias is evident using the MDL score, the overestimation previously seen for the MLE score persists. RMSE and distance measures indicate significantly better overall accuracy for the MDL score.

We now consider the feasibility of the fully Bayesian approach proposed in this article. A feasible posterior density provides simultaneously an estimate and a measure of model

uncertainty. We therefore expect the quantile positions $\widetilde{Q P}^{a}, \widetilde{Q P}^{b}$ to be close to 0.5 , while maintaining reasonably small standard deviations $\widetilde{S D}^{a}, \widetilde{S D}^{b}$ (a value $\widetilde{Q P}>0.5$ indicates negative bias).

Summaries of the various posterior densities defined in (7) are given in Table 3 for the 10 loci scenario. For pedigree type $A$, the posterior densities generated by the likelihood score remains feasible for all $N_{I}$. However, the posterior density for $d^{a}$ generated by the MDL-based posterior for $N_{I}=10000$ is not feasible, with $\widetilde{Q P}^{a}=0.95$, so that the true value $d^{a}=84$ is consistently located well into the upper tail of the individual posterior densities of $d_{i}$ for $i \in \mathcal{Y}_{P}^{a}$ For pedigree type $B$, the MDL-based posterior generates feasible posterior densities, while for the likelihoodbased posterior the quantile positions are reported to be 0 for $N_{I}=2000,10000$, indicating very poor coverage of the posterior densities of $d_{i}$.

When the number of loci is reduced to 8 , the posterior densities generated by the MDL score for pedigree type $A$ result in consistently high quantile positions, rendering the densities infeasible. The likelihood-based densities remain feasible, although some bias is evident. This situation is reversed for pedigree type B, with very small quantile positions for the likelihoodbased posteriors, and feasible (but biased) MDL-based posteriors.

When the number of loci is increased to 12 the MDL-based posteriors become feasible for pedigree type $A$, although some bias for $N_{I}=2000,10000$ is still evident. The advantage of the MDL score over the likelihood score for pedigree type $B$ noted for the 10 loci scenario is maintained for 12 loci.

Individual posterior densities of $d_{i}$ are shown in Figures 3-5, corresponding to the 8,10 and 12 loci scenarios, for $N_{I}=10000$. Two founders are selected from each of 20 base pedigree replications, one from each fitness class. Posterior densities are represented by standard boxplots constructed from the 2000 replications of the selected individual values of $d_{i}$. Consistent with the above discussion, the likelihood-based posterior performs consistently well for pedigree type $A$, with a clear improvement with additional loci. Similarly, the MDL-based posterior performs consistently well for pedigree type $B$, again with clear improvement with additional loci. We note additionally that for 8 and 10 loci, the likelihood-based posterior tends to overestimate $d_{i}$ for pedigree type $B$, while the MDL-based posterior tends to underestimate $d_{i}$ for pedigree type $A$. On the other hand, when 12 loci are used, the MDL-based posterior is able to produce plausible posterior densities for pedigree type $A$, whereas the likelihood-based posterior maintains it's tendency to overestimate $d_{i}$ for pedigree type $B$.

To summarize, for pedigree type $A$ the likelihood score provides generally better inference, both in terms of point estimation, and the construction of feasible posterior densities. This advantage becomes marginal when more loci are used. Conversely, for pedigree type $B$, the MDL score produced consistently better inference than the likelihood score. This advantage was more significant, and showed less of a tendency to become marginal with increased numbers of loci. Thus, provided sufficiently informative data, the MDL score can be expected to perform well over the range of pedigree types considered here, whereas significant overfitting by the likelihood score was evident even for the 12 loci scenario for pedigree type B.

# 5 Example (North Atlantic Cod) 

In Herbinger et al 1997 microsatellite markers from 6 loci were collected on a sample of 857 Atlantic cod larvae from a single cohort. The loci were assumed to be unlinked. Various

statistical hypothesis tests (Almudevar and Field 1999;Almudevar 2001b) failed to find significant evidence of sibling structure.

To demonstrate the methodology, the single cohort was supplemented with a simulated single parent generation. Some number $n_{t}$ of the cohort were randomly selected. One actual parent for each was simulated by selecting at random one gene per locus from the offspring. The other gene is selected according to population allele frequencies estimated from the original cohort. A further nppurious parents were simulated by selecting genotypes according to the estimated population frequencies. The generation memberships are made available to the algorithm.

Posterior densities based on the likelihood and MDL scores were estimated as in the previous example, with attention placed on the offspring distributions of the parental generation. Two quantities were captured, first, the posterior probability of parenthood to the cohort of candidate parent $i$ (that is, $i$ possesses at least one offspring), $\alpha_{i}$, and the posterior probability of a parentoffspring relationship, $\beta_{i, j}$ for candidate parent and offspring $i$ and $j$. These quantities were estimated using equation (2) applied to the sampled pedigrees, amounting to the proportion of pedigrees possessing the feature in question.

In Figure 6, histograms of all nonzero values of $\alpha_{i}$ are constructed, separately for actual and spurious parents $i$, for each posterior density. For the likelihood-based posterior, the values are concentrated near 1 for both actual and spurious parents, whereas for the MDL-based posterior the histograms exhibit significant separation. We would naturally adopt a protocol under which parenthood is not assumed for candidate parents for which $\alpha_{i}=0$, leaving open the question of when to infer parenthood for $\alpha_{i}>0$. The separation in $\alpha_{i}$ induced by the MDL score suggests that a better specificity to sensitivity tradeoff is possible using that score.

To see this, we adopt a threshold rule under which parenthood is assumed for candidate parents for which $\alpha_{i} \geq p$. Figure 7 shows the estimates of the number of candidate parents assigned parenthood, for varying values of $p$, categorized as true or false according to whether the parent is actual or spurious. The estimates are given for both posterior densities. As can be seen, the MDL curve is strictly below the likelihood curve, meaning that the MDL-based posterior induces fewer false parenthood estimates given equal true parenthood estimates, compared to the likelihood-based posterior. The estimates induced by the maximum scoring pedigree is also indicated, which lie approximately on the characteristic curves. This suggests that there is no benefit to comparing the maximum scoring pedigree separately, since it merely represents one possible estimate along a continuous tradeoff of sensitivity to specificity.

A similar analysis was carried out for $\beta_{i j}$. In Figure 8, nonzero values of $\beta_{i j}$ are represented in histogram form, separately for actual parent-offspring pairs; spurious pairs when $i$ is an actual parent; and spurious pairs when $i$ is a spurious parent. In each case no difference in the distribution of $\beta_{i j}$ among spurious pairs involving actual or spurious parents is evident, so the values are pooled for further analysis.

Similarly to the values of $\alpha_{i}$, a greater separation between the distributions of $\beta_{i j}$ for actual and spurious pairs is evident for the MDL-based posterior. The same threshold rule analysis was carried out for the values of $\beta_{i j}$, with the objective of estimating the total number of parentoffspring pairs. Results are given in Figure 9. Again, the MDL-based posterior provides a better sensitivity to specificity tradeoff. Note also that the estimates obtained from the maximum scores are located approximately on the characteristic curves.

# 6 Conclusion 

In this article, the various advantages of a model based approach to relationship inference, in which all relationships in a sample are represented by a single combinatorical object were

considered. Principally, these are the ability to control for spurious estimates of complexity, and a natural method of accounting for statistical uncertainty by using a computationally intensive fully Bayesian approach.

As a specific application, the inference of a pedigree graph using a score based on the minimum description length (MDL) principle was developed. Age data was used to simplify the construction of a Bayesian posterior density. Data assumed the form of genotypic data from varying numbers of loci.

The procedure was applied to a variety of simulated pedigree data. The MDL-based procedure was compared to a likelihood-based procedure. It was found that for relatively complete pedigrees in which all individuals, other than a small set of founders, have both parents in the sample the likelihood approach was marginally more accurate than the MDL approach, although this advantage became negligible with an increase in the number of loci simulated. For less complete pedigrees, the MDL score exhibited significantly better accuracy, which persisted when the number of loci were increased.

Additionally, the proposed method of constructing posterior densities yielded generally acceptable results, in the sense that coverage tended to include true values in cases for which accuracy was also acceptable.

In addition the procedure was applied to a single cohort of 857 North Atlantic cod larvae, supplemented by a simulated parental cohort consisting of a mix of actual and spurious parents. Individual posterior probabilities of parenthood and parent-offspring status using both posteriors were compared, demonstrating a better sensitivity to specificity tradeoff using the MDL-based procedure. More generally, it was shown that the calculation of such posterior probabilities was feasible, and offer the possibility of a more refined inference procedure than that based on the calculation of a single maximum score pedigree.

While it is important to establish the feasibility of such larger scale modelling techniques for relationship inference, we also must note that the assumptions adopted here are somewhat restrictive in a number of ways. We have not accounted for genotype errors, which are regularly observed in large scale genotype screens (Blouin 2003). These errors can have disproportionate effects, since a single change in gene value can rule out by exclusion a true parent-offspring pair. However, likelihoods can be modified to include error models (Marshall et al 1998;Wang 2004), which could then be extended to any scoring procedure.

Additionally, age data may be incomplete (or non-existent). In this case, a score function in product form (4) could be optimized using the simulated annealing approach of Almudevar (2003). This method does not extend naturally to the problem of sampling from a posterior density, however. In this case, MCMC methods on graph spaces may be substituted, and may incorporate any partial age data that is available, thus reducing the search space. Applying simulated annealing or MCMC is generally more challenging than independent sampling, and the application to samples numbering in the thousands remains largely untested.

The procedure proposed here depends on the availability of allele frequencies. These may be estimated from the data, although independent estimates would be preferable, since estimation of heterozygosity of the allele distributions may be confounded with the presence of relatedness. One alternative is to use Bayesian priors in place of estimated frequencies (Painter 1997).

In principle, a likelihood function can incorporate linkage among typed loci, but the product form of the likelihood would no longer apply. As in the case of incomplete age data, the problem

may be solved by using MCMC on graph spaces, at the cost of foregoing the advantages of the product form.

# Acknowledgements 

This work was supported by NIH grant GM075299.

# 7 Appendix 

In this appendix we develop a pedigree score based on the MDL principle, under the assumptions discussed in Section 3. The resulting score in not provably optimal (in the sense of representing the maximum possible data compression), but rather relies on an intuitively reasonable approach to the problem.

### 7.1 Design of efficient codes

Much of the application of the MDL principle depends on two basic results from coding theory, which we introduce in this section. Suppose we have an alphabet $\mathrm{A}=\left[a_{1}, \ldots, a_{k}\right]$, and define a word to be any finite string of symbols from A. It is possible to encode a word $X$ of length $n=|X|$ into a decodable binary string $b(X)$ using $n \log _{2} k$ bits (letting $|x|$ represent the length, or number of characters in, a word $x$ ). This is done by constructing a fixed length code, which assigns a unique binary string to each character in A, of length $\log _{2} k$. Note that this property is approximate if $k$ is not a power of 2 . To encode $X$ we simply concatenate the binary strings assigned to the characters in $X$. The fixed length code allows us to place an upper bound on the code length needed to encode arbitrary words.

Now suppose we know in advance the frequencies of the symbols from A which appear in $X$ (in the English language, "e" appears more frequently than " $z$ "). Denote these frequencies $P$

$=\left(p_{1}, \ldots, p_{k}\right)$, that is, symbol $a_{i}$ occurs with frequency $p_{i}$. Then there exists an decodable coding scheme which approximately achieves a code length of $n H(P)$, where $H(P)$ is the entropy of $P$,

$$
H(P)=\sum_{i=1}^{k}-p_{i} \log _{2} p_{i}
$$

This may be done by assigning a unique binary string of length $-\log _{2} p_{i}$ to symbol $a_{i}$. The Huffman code is commonly used to achieve this (Hamming 1986). Furthermore, this is the maximum possible compression under the stated conditions. We can then interpret $H(P)$ as the average number of bits per character needed to encode $X$.

Suppose we model $X$ as a sample from a multinomial distribution on A. Anticipating the frequencies $P$ we would choose to encode $X$ using a Huffman code, which would yield a code length of

$$
$$

where $n_{i}$ is the frequency of symbol $a_{i}$ in $X$. If $P$ is correctly specified we would have $n_{i} / n \approx$ $p_{i}$, hence

$$
\begin{aligned}
& \approx n \sum_{i=1}^{k}-p_{i} \log _{2} p_{i} \\
& =n H(P)
\end{aligned}
$$

so that $b(X)$ would achieve close to the minimum achievable code length. Note that (8) is exactly the negative log likelihood function for the multinomial model, that is:

$$
\text { likelihood }=(1 / 2)^{\text {code length }}
$$

Now suppose there is a model $\theta \in \Theta$ which explains $X$. One consequence of this is that knowledge of $\theta$ can be used to simplify $X$, which will result in a shorter code, say, $b(X \mid \theta)$. Of course, we will also need to code $\theta$, say $b(\theta)$, so that $X$ can be decoded. The complete code then becomes $b(X \mid \theta) b(\theta)$. We let $B(X \mid \theta)$ and $B(\theta)$ denote the code lengths of $b(X \mid \theta)$ and $b$ $(\theta)$ respectively.

According to the MDL principle, we select as the model that $\theta$ which results in the smallest code length $B(\theta \mid X)=B(X \mid \theta)+B(\theta)$. Similar to the maximum likelihood principle, the MDL principle seeks the model which best explains the data. Note, however, that $b(\theta)$ will be longer when $\theta$ is more complex, which controls spurious complexity.

# 7.2 Coding of data based on model 

We will now consider the problem of how to encode genotypic data from a pedigree. Suppose for the moment that $X$ consists of a single locus of genotypic data for $n$ individuals. We can encode $X$ with a code length of approximately $N_{I} H\left(P^{g}\right)$ for $N_{I}$ individuals, where $P^{g}$ is the population genotype frequency distribution. For example, if there are 5 alleles of equal probability, under Hardy-Weiberg equilibrium there are 10 heterozygotes with frequency $2 / 25$ and 5 homozygotes with frequency $1 / 25$, resulting in entropy of

$$
H\left(P^{g}\right)=10 \times\left[-(2 / 25) \log _{2}(2 / 25)\right]+5 \times\left[-(1 / 25) \log _{2}(1 / 25)\right]=3.84
$$

so we need between 3 and 4 bits per genotype. But further compression can be achieved by exploiting model $\theta$.

First consider the problem of coding genes inherited from two parents present in the sample. Suppose $\theta$ assigns individual $i$ parents $j$ and $k$. Given the parental genotypes, we can construct a set $G_{j k}$ of genotypes (all genotypes resulting from a selection of 1 gene from each parent), which must include the offspring genotype (we would not consider a genetically excluded model $\theta$ ). This set will range in size from 1 to 4 . If it is of size 2 , then the genotype of offspring $i$ can be encoded in a single bit. This can be done by devising some canonical ordering of genotypes, and assigning a bit value of 0 to the lowest ranked genotype in $G_{j k}$. In general, if the size of $G_{j k}$ is 1,2 or 4 , we can code the offspring genotype with $\log _{2}\left|G_{j k}\right|$ bits. It happens that $\left|G_{j k}\right|=3$ when both parents share the same heterozygous genotype $a b$. In this case, offspring genotypes $a b, a a$ and $b b$ may be assigned codes binary codes $0,10,11$ respectively. This gives a direct link between code length and the likelihood function. When $\left|G_{j k}\right|$ is 1,2 or 4 , Mendel's rule assigns a likelihood of $1 /\left|G_{j k}\right|$ to the offspring genotype. When $\left|G_{j k}\right|=3$ Mendel's rule assigns a likelihood of $1 / 2,1 / 4$ and $1 / 4$ to offspring genotypes $a b, a a$ and $b b$ respectively. Thus, in each case we have the relationship

$$
\text { likelihood of offspring genotype }=(1 / 2)^{\text {code length }}
$$

Now suppose individual $i$ has a single parent $j$ represented in sample $X$. At least one gene in $i$ is represented in $j$. If both are (and $i$ is heterozygous), we may use an arbitrary rule to designate one as having been inherited from $j$. If $j$ is homozygous, we would assign a likelihood of 1 to that gene, and $1 / 2$ otherwise. Accordingly, we would need 0 or 1 bit to code a gene inherited from a homozygote or heterozygote, respectively, giving

$$
\text { likelihood of offspring gene }=(1 / 2)^{\text {code length }}
$$

This leaves the problem of coding genes that are not inherited from other members of the sample. First, consider the genotypes belonging to founders. These occur in proportions approximately equal to the population genotype distribution hence each genotype can be coded with an average of $H\left(P^{g}\right)$ bits. Next, consider individuals with one parent in the sample. Coding of the gene inherited from the present parent has been discussed above. The remaining gene is essentially sampled from the population and will therefore occur in frequencies given by $P^{a}$, the population frequency distribution of the alleles. This gene can therefore be coded with an average of $H\left(P^{a}\right)$ bits.

For all genotypes, therefore, the relationship in (9) is preserved, and the code length is given by

$$
B(X \mid \theta)=-\log _{2} L(\theta \mid X)
$$

where $L(\theta \mid X)$ is the likelihood of $\theta$ given data $X$. For multilocus data $X=\left(X(1), \ldots, X\left(N_{L}\right)\right)$ we add the code lengths attained for each locus, that is,

$$
B(X \mid \theta)=-\sum_{j=1}^{N_{L}} \log _{2} L(\theta \mid X(j))
$$

# 7.3 Coding pedigree structure 

The method of coding the data given a model can be satisfactorily resolved, leaving the question of how best to code $\theta$. While we can't claim a method which is provably optimal for any given criterion, we can develop a reasonable solution which will later be shown to possess desirable properties.

To do this we adapt an approach taken in Friedman and Goldszmidt (1998). For each individual we code the number of parents, one of 0,1 or 2 , which may be done using 2 bits. The number of bits is the same for each individual, so plays no role in model selection, and may be left out of our code length estimate. We then code the parent subset. Here, we assume that age and sex data (or any form of exclusionary information) is available in the form of $Y$. Let $n(k, i)$ represent the number of possible parent sets of size $k$ of individual $i$ permitted by $Y$. If $Y$ is empty, we would have $n(1, i)=N_{I}-1$ and $n(2, i)=\left(N_{I}-1\right)\left(N_{I}-2\right) / 2$. We necessarily have $n(0, i)=1$. If the number of parents is $k$ we would require $\log _{2} n(k, i)$ bits to code the parent set, using a fixed length code. Note that we need 0 bits to encode founders. We then have

$$
B(\theta)=\sum_{i=1}^{N_{I}} \log _{2}\left(n\left(\left|H_{i}^{\theta}\right|, i\right)\right)
$$

![img-0.jpeg](img-0.jpeg)

A1
![img-1.jpeg](img-1.jpeg)

B1
![img-2.jpeg](img-2.jpeg)

A2
![img-3.jpeg](img-3.jpeg)

B2

Figure 1.
Test base pedigrees

![img-4.jpeg](img-4.jpeg)

Figure 2.
Summary of experiments E1 for 10 loci simulations. Left column contains plots of $d^{\alpha}(\circ)$ and $d^{\mathrm{b}}(\Delta)$ for pedigree types $A, B$. Right column contains plots of $R M S E^{\mathrm{a}}(\circ)$ and $R M S E^{\mathrm{b}}(\Delta)$ for pedigree types $A, B$. MDL score is shown in bold lines, MLE score is shown in dotted lines. True values $d^{\alpha}, d^{\mathrm{b}}$ are indicated by arrows.

![img-5.jpeg](img-5.jpeg)

Figure 3.
Estimated posterior densities of individual descendent numbers for 20 founders (experiment E2, $N_{I}=10000,8$ loci). Two founders are selected from each of 20 base pedigree replications, one from each fitness group. Each score and pedigree is separately represented.

![img-6.jpeg](img-6.jpeg)

Figure 4.
Estimated posterior densities of individual descendent numbers for 20 founders (experiment E2, $N_{I}=10000,10$ loci). Two founders are selected from each of 20 base pedigree replications, one from each fitness group. Each score and pedigree is separately represented.

![img-7.jpeg](img-7.jpeg)

Figure 5.
Estimated posterior densities of individual descendent numbers for 20 founders (experiment E2, $N_{I}=10000,12$ loci). Two founders are selected from each of 20 base pedigree replications, one from each fitness group. Each score and pedigree is separately represented.

![img-8.jpeg](img-8.jpeg)

Figure 6.
Histograms of values of nonzero $\alpha_{i}$, the posterior probabilities of parenthood, among $n_{t}$ true parents and $n_{f}$ spurious parents, for likelihood-based and MDL-based posterior densities.

![img-9.jpeg](img-9.jpeg)

Figure 7.
Threshold posterior estimates of number of parents, categorized as true or false. This is given as the total number of $n_{I}$ and $n_{f}$ actual and spurious parents which are estimated as parents by applying a threshold rule of the form $\alpha_{i} \geq p$, allowing $p$ to vary from .04 to 1 . Both likelihoodbased and MDL-based posterior densities are employed. The maximum score estimate is also indicated.

![img-10.jpeg](img-10.jpeg)

Figure 8.
Histograms of values of nonzero $\beta_{i j}$, the posterior probabilities of parent-offspring relationship, given by true pairs among $n_{t}$ actual parents; false pairs among $n_{t}$ actual parents; and false pairs among $n_{f}$ spurious parents, for likelihood-based and MDL-based posterior densities.

![img-11.jpeg](img-11.jpeg)

Figure 9.
Threshold posterior estimates of number of parent-offspring pairs, categorized as true or false. This is given as the total number of pairs which are estimated as parent-offspring pairs by applying a threshold rule of the form $\beta_{i j} \geq p$, allowing $p$ to vary from .04 to 1 . Both likelihoodbased and MDL-based posterior densities are employed. The maximum score estimate is also indicated.

Base pedigree characteristics.

Table 1


Table 2
Summary of results (6) and (7) for experiments E1 and E2 applied to 8 test pedigrees using 8 loci.


Table 3
Summary of results (6) and (7) for experiments E1 and E2 applied to 8 test pedigrees using 10 loci.


Table 4
Summary of results (6) and (7) for experiments E1 and E2 applied to 8 test pedigrees using 12 loci.
