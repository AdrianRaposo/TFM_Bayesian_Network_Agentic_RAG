# A solution for the rare type match problem when using the DIP-STR marker system 

G. Cereda ${ }^{\mathrm{a}, *}$, R. D. Gill ${ }^{\mathrm{b}}$, F. Taroni ${ }^{\mathrm{a}}$<br>${ }^{a}$ University of Lausanne, School of Criminal Justice, Institute of Forensic Science, 1015 Lausanne-Dorigny, Switzerland<br>${ }^{b}$ Leiden University, Mathematical Institute, Niels Bohrweg 1, 2333 CA Leiden, The Netherlands


#### Abstract

The rare type match problem is an evaluative challenging situation in which the analysis of a DNA profile reveals the presence of (at least) one allele which is not contained in the reference database. This situation is challenging because an estimate for the frequency of occurrence of the profile in a given population needs sophisticated evaluative procedures.

The rare type match problem is very common when the DIP-STR marker system, which has proven itself very useful for dealing with unbalanced DNA mixtures, is used, essentially due to the limited size of the available database. The object-oriented Bayesian network proposed in Cereda et al. [7] to assess the value of the evidence for general scenarios, was not designed to deal with this particular situation. In this paper, the model is extended and partially modified to be able to calculate the full Bayesian likelihood ratio in presence of any (observed and not yet observed) allele of a given profile. The method is based on the approach developed in Cereda [5] for Y-STR data. Alternative solutions, such as the plug-in approximation and an empirical Bayesian methodology are also proposed and compared with the results obtained with the full Bayesian approach.

The paper has been published (2018) in Forensic Science International: Genetics 34, 88-96, https: //doi.org/10.1016/j.fsigen.2017.07.010.


Keywords: Object-oriented Bayesian networks, Deletion/Insertion Polymorphism, Likelihood ratio, Bayes Factor, Extremely unbalanced DNA mixtures.

## 1. Introduction

The most common task of a forensic scientist or statistician is to quantify the probative value of the observation of some scientific findings (e.g. DNA profiles, fragment of paint, fibres), under the hypotheses of interest for the court of justice. This is done through the quantification of the likelihood ratio. In case the hypotheses of interest deal with whether the recovered material has the same origin as some control material, it is important to be able to quantify the rarity of the corresponding characteristics. For instance, the evidence can be the correspondence between the DNA profile of a crime stain and of a suspect: the rarer the profile, the more probative is the scientific finding regarding propositions about the source. The rarity of the profile of interest is often used to assign the probability of the random occurrence of the given stain, and some available (and relevant) database is used to support the scientist's assignment.

The 'rare type match problem', also called 'the fundamental problem of forensic mathematics' [2] is the situation in which the corresponding characteristic has not been observed in the relevant reference database for the case. One example is the DIP-STR marker system, a rather novel genotyping technique, proposed in Castella et al. [3], which turned out to be very useful to analyse DNA mixtures if the proportion of the DNA quantities of the, say, two contributors is more extreme than 1:10. Due to limited size of available databases, rare DIP-STR profiles are often encountered.

A Bayesian framework for evaluating DIP-STR results was developed in Cereda et al. [7], using objectoriented Bayesian networks, with the aim of calculating the likelihood ratio for mixtures of two contributors,

[^0]
[^0]:    *Corresponding author
    Email address: giulia.cereda7@gmail.com (G. Cereda)

when the major contributor's genotype is known and the two competing hypotheses are 'the minor contributor is the suspect' $\left(h_{p}\right)$ and 'the minor contributor is an unknown person, unrelated to the suspect' $\left(h_{d}\right)$, also extended to cases where the suspect is missing.

This paper proposes a Bayesian solution for assigning the likelihood ratio for mixture results in presence of a rare type match, that is when at least one of the DIP-STR alleles of the contributors is not present in the reference database. This situation was not covered by Cereda et al. [7].

The Bayesian model adopted is based on a similar one proposed in Cereda [5]. Several issues concerning Bayesian methodology, and notation, have been improved.

The paper is structured as follows. Section 2 discusses the use of the DIP-STR marker system for extremely unbalanced mixtures, while Section 3 describes the object-oriented Bayesian network that was built to evaluate DIP-STR profiling results in Cereda et al. [7]. The chosen notation and the definition of what a full Bayesian approach to likelihood ratio assessment is, can be found in Sections 4 and 5, respectively. The model developed to evaluate results from mixtures of two contributors in presence of the rare type match problem (described in Section 6) is detailed in Sections 7 and 8. More detailed descriptions of the development of the full Bayesian likelihood ratio, which takes advantage of the Lemma introduced in Section 9, are confined to the Appendix. A discussion about the choice of the prior distribution for the parameters is also provided in Section 10, while conclusions can be found in Section 11.

# 2. DIP-STR marker system for extremely unbalanced mixtures 

A DIP-STR marker is a compound marker made of a DIP (Deletion/Insertion polymorphism, Weber et al. [e.g., 12]), and of a standard STR polymorphism. These two polymorphisms are chosen less than 500 bp apart, in order to be dependent on one another. It has been shown that due to very low quantity of DNA in a sample, to extreme degradation conditions, or to other physical and bio-chemical phenomena, mixtures could remain undetected using standard methods for the analysis of DNA mixtures Oldoni et al. [9]

On the other hand, as long as the minor contributor has at a specific locus at least one DIP allele different from the DIP alleles of the victim, the DIP-STR marker system allows the selected amplification of its DIP-STR genotype, up to mixture proportions as extreme as 1:1000. Indeed, the DIP-STR markers are specifically selected to target the minor contributor, by targeting the DIP alleles not present in the victim (thus, the precise set of markers used will be case dependent). If the victim is (e.g.) homozygous L/L, then only S-alleles are targeted. Hence, by construction L-alleles of the minor will not be detected.

At each DIP-STR locus, the possible configurations are the following (summarized in Table 1).

- In the case where the major and minor contributors are DIP homozygous with different alleles (i.e., one is L-L and the other is S-S) both DIP-STR alleles of the minor contributor can be detected. This is the best scenario the scientist can be faced with.
- If the major contributor is DIP homozygous (for instance L-L) and the minor contributor is DIP heterozygous, only one of the two DIP-STR alleles of the minor contributor can be detected: the one with the other DIP allele (in the example the allele S).
- If both contributors are homozygous for the same DIP alleles (both L-L or both S-S) we don't obtain results from the trace but we nevetheless obtain the information about the DIP-homozygosity of the minor.
- The worst situation is the one in which the major is DIP heterozygous. In this case we cannot know anything about the DIP-STR profile of the minor contributor.

It is important to mention that, for the model presented in this paper, we assume that the DNA material is in sufficient quantity to obtain all the relevant genotypic information about the contributors that the considered set of markers is supposed to provide (i.e., no allelic drop-out, nor other artifacts.)

A first panel of 10 DIP-STR markers was presented in Castella et al. [3]. A second panel with 9 additional DIP-STR markers has recently been provided in Oldoni et al. [9]. When one analyses a mixed stain, each of the 19 available markers may present one of the three situations described above.


Table 1: Informativeness of genotypic configurations. 'Hom' denotes homozygous for the DIP allele, and 'Het' heterozygous.
![img-0.jpeg](img-0.jpeg)

Figure 1: Bayesian network corresponding to the object-oriented Bayesian network of Cereda et al. [7]. The meaning of the nodes is described in Section 3.

# 3. Bayesian network for evaluating DIP-STR profiling results from unbalanced DNA mixtures. 

In Cereda et al. [7] a locus specific object-oriented Bayesian network (OOBN), designed to assist the evaluation of DIP-STR results obtained from mixtures with two contributors, is proposed. The network, reproducing the mechanism described in Section 2 and in Table 1, is proposed here in the form of a Bayesian network (see Figure 1). It is suitable for a situation in which the DIP-STR profile of a suspect (potential contributor to the mixture) is available. The two hypotheses of interest are 'the minor contributor is the suspect' $\left(h_{p}\right)$ and 'the minor contributor is an unknown person, unrelated to the suspect' $\left(h_{d}\right)$. The major contributor is often referred to as "the victim", taken as a known contributor, and his/her DIP-STR profile is generally available.

It is important to notice that the only information needed from the known major contributor regards his DIP alleles. Hence, the only node in the network which concerns the victim, $V$, has three possible states: HomoL, HomoS and Hetero. The node $H$ represents the two hypotheses of interest defined above.

With the exception of node $O$, the remaining part of the network deals with the unknown minor contributor. Nodes $S_{1}$ and $S_{2}$ represent the two DIP-STR alleles of the suspect. Nodes $U_{1}$ and $U_{2}$ represent the two DIP-STR alleles of the alternative (unknown) contributor in a two-person mixture. Nodes $C_{1}$ and $C_{2}$ represent the DIP-STR alleles of the actual second contributor (for example, the suspect). Depending on the state of node $H$, the second contributor's allele can be a copy of $S_{1}$ and $S_{2}$ (under state $h_{p}$ ), or of $U_{1}$ and $U_{2}$ (under state $h_{d}$ ). The state of node $O$, which contains results obtained from the mixture, depends on the combination of $V, C_{1}$ and $C_{2}$ (according to Table 1).

The probability tables for the nodes are of different types. In the scenario considered, node $V$ is observed, since the major contributor is known. As such, its probability table is not relevant for the final result because its state is fixed, thus it is filled with equal prior probabilities for its three states. The same holds for node $H$, which is in turn instantiated to obtain the numerator and the denominator of the likelihood ratio.

Nodes $C_{1}$ and $C_{2}$ are deterministic given $H, S_{1}, S_{2}, U_{1}$, and $U_{2}$ : if $H$ is in state $h_{p}$, then $C_{1}$ and $C_{2}$ are copies of, respectively, $S_{1}$ and $S_{2}$, otherwise they are copies of $U_{1}$ and $U_{2}$. Also node $O$ is deterministic, given nodes $V, H, C_{1}$ and $C_{2}$ : its probability table is filled out with 0 's and 1's (according to the conditions defined in Table 1). The states of nodes $S_{1}, S_{2}, U_{1}, U_{2}, C_{1}$, and $C_{2}$ are $L a, L b, L x, S a, S b, S x$. Notice that at each DIP-STR locus there may be more than six possible alleles: $L a, L b, S a, S b$ are used to represent the two alleles that at most could be observed, while $S x$ and $L x$ represent all the other (not observed) alleles different from $a$ and $b$. In Cereda et al. [7], this solution was preferred to having the entire list of DIP-STR alleles, in order to make the model simpler, and usable for different loci. The disadvantage is that, at each new case, the meaning of these symbols changes, and the probability tables have to be adapted accordingly. In this paper, we will develop a methodology to overcome this constraint.

The probability tables for nodes $S_{1}, S_{2}, U_{1}$, and $U_{2}$ should be filled with the allelic proportions corresponding to the alleles represented by names $L a, L b$, etc., in the population of interest. These allelic proportions are unknown, but we a have a database of DIP-STR alleles, which we can consider as a random sample from the population of interest. In Cereda et al. [7], a Dirichlet distribution with all parameters equal to one was used as prior for the DIP-STR allelic proportions, and the probability tables for nodes $S_{1}, S_{2}$, $U_{1}, U_{2}$ were filled out with the posterior means (conditional to the observation of the database). However, as discussed in Section 5, this approach suffers from some limitations and it can be improved and made more consistent with the Bayesian theory. Moreover, the number of possible distinct DIP-STR alleles was chosen by looking at those in the database. Thus, the model was not suitable to be used when new alleles (not previously detected) were observed. This paper aims at solving these problems.

## 4. Notation

Throughout the paper the following notation is chosen: random variables and their values are denoted, respectively, with uppercase and lowercase characters: $x$ is a realization of $X$. Random vectors are denoted with bold characters: $\mathbf{x}$ is a realization of the random vector $\mathbf{X}$. Probability is denoted with $\operatorname{Pr}(\cdot)$, while density of a continuous random variable $X$ is denoted alternatively by $p_{X}(x)$ or by $p(x)$ when the subscript is clear from the context. For a discrete random variable $Y$, the density notation $p_{Y}(y)$ and the discrete one $\operatorname{Pr}(Y=y)$ will be alternately used. Moreover, we will use shorthand notation like $p(y \mid x)$ to stand for the probability density of Y with respect to the conditional distribution of $Y$ given $X=x$.

Given $k \geq 2$, and $\alpha=\left(\alpha_{1}, \ldots, \alpha_{k}\right)$ such that $\alpha_{i}>0$,

$$
\mathbf{X} \sim \operatorname{Dir}^{k}\left(\alpha_{1}, \ldots, \alpha_{k}\right)
$$

means that vector $\mathbf{x}$ follows a $k$-dimensional Dirichlet distribution [10], whose density is

$$
p(\mathbf{x})=\frac{\Gamma\left(\sum_{i=1}^{k} \alpha_{i}\right)}{\prod_{i=1}^{k} \Gamma\left(\alpha_{i}\right)} \prod_{i=1}^{k} x_{i}^{\alpha_{i}-1}
$$

In the appendix, we will denote with $\mathbf{z}=(\mathbf{x}, y)$ the vector $\mathbf{z}$ obtained by adding element $y$ at the end of vector $\mathbf{x}$.

# 5. Full Bayesian approach 

In the case of interest, for each analysed locus the forensic scientist or statistician is given the following input data: the victim's and the suspect's DIP-STR profile (denoted as $E_{v}$ and $E_{s}$ respectively), along with the DIP-STR alleles obtained from the mixture $\left(E_{m}\right)$. This data has to be evaluated in the light of the hypotheses of interest ( $h_{p}$ and $h_{d}$ ) as defined in Section 1. The evaluation of such evidence heavily depends on the allelic proportions of the DIP-STR alleles of the trace and of the suspect, which are unknown. The vector $\boldsymbol{\theta}$, containing the population proportions of all the possible DIP-STR alleles at the considered locus, is the nuisance parameter of the model. A database (denoted here as $D$ ), consisting of a list of DIP-STR alleles from the population of interest is given to the statistician, in order to support him in the assessment of the uncertainty about $\boldsymbol{\theta}$. The data to evaluate are thus made of $E=\left(E_{v}, E_{s}, E_{m}\right)$ and $D$. This notation reflects the distinction described in Cereda [5] between 'evidence', data directly related to the crime, and 'background', data related only to the nuisance parameter of the model.

The full Bayesian approach consists of modelling all these variables, including $\boldsymbol{\theta}$, as random variables whose joint distribution $\operatorname{Pr}$ reflects prior belief of the expert.

The largely accepted method to evaluate the data in order to discriminate between the two hypotheses of interest, is the calculation of the Bayes factor (BF), in forensic context regularly called likelihood ratio (LR). It is defined as the ratio of the probabilities of observing the data under the two competing hypotheses:

$$
\mathrm{LR}=\frac{\operatorname{Pr}\left(E=e, D=d \mid H=h_{p}\right)}{\operatorname{Pr}\left(E=e, D=d \mid H=h_{d}\right)}=\frac{\operatorname{Pr}\left(E=e \mid D=d, H=h_{p}\right)}{\operatorname{Pr}\left(E=e \mid D=d, H=h_{d}\right)}
$$

where the last equality holds in virtue of the independence of database and hypotheses.
The nuisance parameter $\boldsymbol{\theta}$ has been integrated out according to its prior distribution. Notice indeed that $\boldsymbol{\theta}$ does not appear in (1).

In Cereda et al. [7], we used a different approach: Bayesian estimates of the allelic proportions were plugged into the probability tables for nodes $S_{1}, S_{2}, U_{1}$, and $U_{2}$. This is equivalent to using a likelihood ratio for a given $\boldsymbol{\theta}$, such as

$$
\mathrm{LR}=\frac{\operatorname{Pr}\left(E=e \mid \boldsymbol{\Theta}=\boldsymbol{\theta}, D=d, H=h_{p}\right)}{\operatorname{Pr}\left(E=e \mid \boldsymbol{\Theta}=\boldsymbol{\theta}, D=d, H=h_{d}\right)}
$$

and to plug inside the estimates for $\boldsymbol{\theta}$.
The plug-in method can be seen as an approximation to the full Bayesian method [5]. To obtain it, a Bayesian network is built which allows one to use an integrated full Bayesian approach, by introducing, among others, a node which represents the database $D$, and a node that represents the nuisance parameter $\boldsymbol{\theta}$. The full Bayesian approach is then compared to the plug-in method, to check the impact of the approximations.

## 6. Rare type match problem

When the findings to evaluate include a correspondence between the DNA profile of a particular piece of evidence (i.e., a trace of unknown origin) and a suspect's DNA profile, but at least one of the alleles of this profile are not present in the available database, it is difficult to assess the uncertainty over the population proportion of that allele. It is likely to be a rare allele (from which the term rare type match problem) but it is challenging to quantify how rare. This assessment is important for the quantification of the likelihood ratio: the rarer the matching profile, the larger is the likelihood ratio.

Using DIP-STR data, it is very likely to encounter the rare type match problem, because the available database size is still limited [9]. The same happens when Y-chromosome (or mitochondrial) DNA profiles

are used, since the set of possible Y-STR profiles is extremely large. As a consequence, most of the YSTR haplotypes are not represented in the database. In Cereda [5, 6, 4] several (Bayesian and frequentist) solutions are proposed for the rare type match problem for Y-STR data. The object-oriented Bayesian network of Cereda et al. [7], here presented in Figure 1, cannot be used in the case of a rare type match problem: there, the number of different alleles at a given locus was considered as fixed, and equal to that observed in the database. This makes that model useless in cases where new DIP-STR alleles are observed.

As a solution, we will consider the number of different DIP-STR alleles present in the population as random, by introducing additional variables in the model, explained in detail in Section 7. This is based on one of the Bayesian methods proposed in Cereda [5].

# 7. A prior for $\boldsymbol{\theta}$ 

Let us denote with L-STR (or S-STR) the DIP-STR alleles which have the DIP part equal to L (or S). Assume that, at a specific locus, there are at most $m$ theoretically possible L-STR alleles and $m$ theoretically possible S-STR alleles. The random vector $\boldsymbol{\Theta}=\left(\Theta_{1}^{L}, \ldots, \Theta_{m}^{L}, \Theta_{1}^{S}, \ldots, \Theta_{m}^{S}\right)$ contains the population proportions of all the potential $2 m$ DIP-STR alleles at that locus (for instance, alphabetically ordered).

Only $k^{L}\left(k^{S}\right)$ of the $m$ possible L-STR (S-STR) alleles are actually present in nature (or more specifically in the population of interest), but $k^{L}$ and $k^{S}$ are unknown. Which of the $m$ L-STR alleles are those $k^{L}$ and $k^{S}$ is not known either.

The vector $\mathbf{t}^{L}$ contains the ordered positions (from 1 to $m$ ) of the $k^{L}$ L-STR alleles present in the population of interest. $\mathbf{t}^{L}$ is modelled through a random variable $\mathbf{T}^{L}$ : each possible configuration $\mathbf{t}^{L}$ is assumed as equiprobable, hence it is chosen uniformly at random from the possible $\left({ }_{k^{L}}^{m}\right)$ configurations. Random vector $\mathbf{T}^{S}$ is defined similarly. Notice that $\theta_{i}^{L}=0, \forall i \notin \mathbf{t}^{L}$, and $\theta_{i}^{S}=0, \forall i \notin \mathbf{t}^{S}$.

Specifying $\boldsymbol{\Theta}$ is equivalent to specifying three random variables $\boldsymbol{\Phi}^{L}, \boldsymbol{\Phi}^{S}, \Psi . \Psi$ is the sum of the occurrence probabilities of the L-STR alleles

$$
\psi=\sum_{i=1}^{m} \theta_{i}^{L}
$$

while $\boldsymbol{\phi}^{L}$ is the normalized vector of the occurrence probabilities of the L-STR alleles. Stated otherwise,

$$
\boldsymbol{\phi}^{L}=\left(\frac{\theta_{1}^{L}}{\psi}, \ldots, \frac{\theta_{m}^{L}}{\psi}\right)
$$

Similarly, $\boldsymbol{\phi}^{S}$ is the normalized vector of the relative frequencies of the S-STR alleles:

$$
\boldsymbol{\phi}^{S}=\left(\frac{\theta_{1}^{S}}{1-\psi}, \ldots, \frac{\theta_{m}^{S}}{1-\psi}\right)
$$

The prior distribution for $\boldsymbol{\theta}$ can be described in terms of the prior over $\boldsymbol{\Phi}^{L}, \boldsymbol{\Phi}^{S}$, and $\Psi$, which will be taken to be independent. The latter is distributed according to a $\operatorname{Beta}(1,1)$, while the positive entries of $\boldsymbol{\phi}^{L}$, i.e., $\left(\phi_{i}^{L} \mid i \in \mathbf{t}^{L}\right)$ are Dirichlet distributed, given $\mathbf{t}^{L}$, with all hyperparameters equal to $\alpha$. The same holds for $\boldsymbol{\phi}^{S}$ given $\mathbf{t}^{S}$. Hence, the distribution of node $\boldsymbol{\theta}$ can be described in terms of the distribution of seven additional random variables, whose conditional dependencies can be described by the Bayesian network of Figure 2. Bayesian networks using beta and Dirichlet distributions in forensic contexts are presented in Biedermann et al. [1]. Other examples can also be found in Taroni et al. [11].

## 8. Full model

This model is represented by the Bayesian network of Figure 3. Notice that there are differences from the model depicted in Figure 1, among which is the presence of node $\boldsymbol{\theta}$ distributed as described in Section 7. The first difference lies in the definition of nodes $S_{1}, S_{2}, U_{1}, U_{2}, C_{1}$, and $C_{2}$. Their values are couples ( $\mathrm{L}, i$ ) or $(\mathrm{S}, i)$ where $i \in\{1, \ldots, m\}$, describing the position in $\boldsymbol{\theta}$ of the corresponding DIP-STR allele. The same holds for nodes $V_{1}$ and $V_{2}$, which replace node $V$ of Figure 1, and represent the two DIP-STR alleles of the victim. All these nodes are now linked to node $\boldsymbol{\Theta}$ because, given $\boldsymbol{\Theta}=\boldsymbol{\theta}$, the random variables $S_{1}, S_{2}, U_{1}$,

![img-1.jpeg](img-1.jpeg)

Figure 2: The conditional dependency relation of the random variables used to build the distribution of $\boldsymbol{\theta}$. The definition of the nodes can be found in Section 7.
![img-2.jpeg](img-2.jpeg)

Figure 3: Bayesian network for the Dirichlet-multinomial model with a random number of types, to be used for DIP-STR data. The definition of the nodes can be found in Section 8.

$U_{2}, V_{1}, V_{2}$ have the following density (with parameter $\theta$ ):

$$
p((j, i) \mid \boldsymbol{\theta})=\theta_{i}^{j}, \quad \forall j \in\{L, S\}, \forall i \in\{1, \ldots, m\}
$$

The second difference is the presence of two nodes $O_{1}$ and $O_{2}$, instead of a single node $O$ as in Figure 1. $O_{1}$ represents one of the DIP-STR alleles observed from the mixture (if any, 0 otherwise). $O_{2}$ is always 0 unless we are in the situation described by the first row of Table 1, where two DIP-STR alleles are observed. In this case, the convention is for $O_{1}$ and $O_{2}$ to be ordered alphabetically.

The random vector $\mathbf{D}$ represents the available database of size $n$, through the list of labels $((L, i)$ or $(S, i))$ of the DIP-STR alleles contained in the database. The order does not matter, so we can choose the order in which the alleles appear in the database. A particular configuration of $\mathbf{D}$ is denoted as $\mathbf{d}=\left(d_{1}, \ldots, d_{n}\right)$, where, given $\boldsymbol{\theta}$, each component is i.i.d. with the same density as in (2).

According to this notation, the likelihood ratio for the scenario of interest can be written as

$$
\mathrm{LR}=\frac{p\left(o_{1}, o_{2}, s_{1}, s_{2}, v_{1}, v_{2}, \mathbf{d} \mid h_{p}\right)}{p\left(o_{1}, o_{2}, s_{1}, s_{2}, v_{1}, v_{2}, \mathbf{d} \mid h_{d}\right)}=\frac{p\left(o_{1}, o_{2} \mid s_{1}, s_{2}, v_{1}, v_{2}, \mathbf{d}, h_{p}\right)}{p\left(o_{1}, o_{2} \mid s_{1}, s_{2}, v_{1}, v_{2}, \mathbf{d}, h_{d}\right)}
$$

Due to the complexity of the chosen distribution, the Bayesian network cannot be treated with available software, such as Hugin, or OpenBUGS. However, the likelihood ratio can be obtained analytically using the Lemma presented in Section 9.

# 9. Lemma 

![img-3.jpeg](img-3.jpeg)

Figure 4: Conditional dependencies of the random variables of the Lemma

Lemma 1. Given four random variables $A, H, X$ and $Y$, whose conditional dependencies are represented by the Bayesian network of Figure 4, the likelihood function for $h$, given $X=x$ and $Y=y$ satisfies

$$
\operatorname{lik}(h \mid x, y) \propto \mathbb{E}(p(y \mid x, A, h) \mid X=x)
$$

This Lemma, proven in Cereda [4], is very general: it applies to every group of random variables whose conditional dependencies are represented by the Bayesian network of Figure 4, and it is very useful due to the possibility of applying it to a very common forensic situation: the prosecution and the defence disagree on the distribution of part of the data $(Y)$ but agree on the distribution of the other part $(X)$, when the distribution of $X$ and $Y$ depends on some parameters $(A)$. This Lemma can also be used for the DIP-STR model presented in Section 7. However, it is not straightforward to identify in the Bayesian network of Figure 3 the required structure shown in Figure 4. Luckily, the same model can be represented in several ways: we will propose a modification of the Bayesian network of Figure 3 into something which more clearly shows the required structure. This will be done in two steps: first, we will remove unnecessary nodes, and then we will group some of the others.

Step 1.. The Bayesian network presented in Figure 5 is obtained by removing from the Bayesian network of Figure 3 nodes $U_{1}, U_{2}, C_{1}$, and $C_{2}$. The conditional probability tables of nodes $O_{1}$ and $O_{2}$ can be directly expressed in terms of $S_{1}, S_{2}, V_{1}, V_{2}$, and $H$, in a way that makes the model of Figure 5 equivalent to the previous one (Figure 3).

![img-4.jpeg](img-4.jpeg)

Figure 5: An alternative representation of the DIP-STR mixture model presented in Figure 3.

Step 2.. The Bayesian network of Figure 6 can be obtained by substituting some of the nodes of the Bayesian network of Figure 5 with a single node. Indeed, instead of having the random vector $\mathbf{D}$ and four additional random variables ( $S_{1}, S_{2}, V_{1}$, and $V_{2}$ ), we can group all these together into a random vector B, of length $n+4$. The first $n$ elements are the labels contained in $\mathbf{D}$, the fourth to last and third to last are the labels in $S_{1}$ and $S_{2}$, while the second to last and the last are the labels in $V_{1}$, and $V_{2}$, respectively.
![img-5.jpeg](img-5.jpeg)

Figure 6: A simpler structure for the Bayesian network, suitable to be used for the Lemma. Dashed lines show the choice for the corresponding variables $A, X$, and $Y$ of Figure 4.

The Bayesian network of Figure 6 can be used to represent the same model as that represented by Figure 1, by carefully adapting the conditional distribution of $O_{1}$, and $O_{2}$. We can apply the Lemma to our model by defining $Y=\left(O_{1}, O_{2}\right), X=\mathbf{B}$, and $A=\Theta$. This leads to

$$
\mathrm{LR}=\frac{p\left(o_{1}, o_{2}, \mathbf{b} \mid h_{p}\right)}{p\left(o_{1}, o_{2}, \mathbf{b} \mid h_{d}\right)}=\frac{\operatorname{lik}\left(h_{p} \mid o_{1}, o_{2}, \mathbf{b}\right)}{\operatorname{lik}\left(h_{d} \mid o_{1}, o_{2}, \mathbf{b}\right)}=\frac{\mathbb{E}\left(p\left(o_{1}, o_{2} \mid \mathbf{b}, \boldsymbol{\Theta}, h_{p}\right) \mid \mathbf{B}=\mathbf{b}\right)}{\mathbb{E}\left(p\left(o_{1}, o_{2} \mid \mathbf{b}, \boldsymbol{\Theta}, h_{d}\right) \mid \mathbf{B}=\mathbf{b}\right)}
$$

Notice that we assume that under the prosecution's hypothesis, $p\left(o_{1}, o_{2} \mid \mathbf{b}, \boldsymbol{\Theta}, h_{p}\right)=1$. Therefore, the likelihood ratio can be simplified:

$$
\mathrm{LR}=\frac{1}{\mathbb{E}\left(p\left(o_{1}, o_{2} \mid \mathbf{b}, \boldsymbol{\Theta}, h_{d}\right) \mid \mathbf{B}=\mathbf{b}\right)}
$$

Indeed, as one would expect, under Hd the probability of seeing $o_{1}$ and $o_{2}$ is given by the expected frequency of that combination, given the alleles in the database, of the suspect and of the victim which have

been observed.


Table 2: Different forms that $p\left(o_{1}, o_{2} \mid \mathbf{b}, \boldsymbol{\Theta}, h_{d}\right)$ can take, based on the DIP-STR alleles observed from the trace and on the victim's DIP alleles. The case in which the victim is heterozygous is not of interest.
$p\left(o_{1}, o_{2} \mid \mathbf{b}, \boldsymbol{\Theta}, h_{d}\right)$ is a function of some components of the vector $\boldsymbol{\Theta}$. The form of this function depends on the combination of the DIP-STR alleles of the victim and of the trace (see Table 2). The expectation in the denominator of (4) is to be taken using the posterior distribution $\boldsymbol{\Theta} \mid \mathbf{B}=\mathbf{b}$. This is developed in detail in the Appendix, leading to the following 5 relevant equations:

$$
\begin{gathered}
\mathbb{E}\left(\Psi^{2} \mid \mathbf{b}\right)=\frac{\left(n^{L}+1\right)\left(n^{L}+2\right)}{(n+6)(n+7)} \\
\mathbb{E}\left((1-\Psi)^{2} \mid \mathbf{b}\right)=\frac{\left(n^{S}+1\right)\left(n^{S}+2\right)}{(n+6)(n+7)} \\
\mathbb{E}\left(\Theta_{i}^{L} \Theta_{j}^{L} \mid \mathbf{b}\right)=\left(\alpha+n_{i}^{L}\right)\left(\alpha+n_{j}^{L}\right) \frac{\sum_{k=k_{b}^{L}}^{m} w^{L}(k) g^{L}(k)}{\sum_{k=k_{b}^{L}}^{m} w^{L}(k)} \frac{\left(n^{L}+1\right)\left(n^{L}+2\right)}{(n+6)(n+7)} \\
\mathbb{E}\left(\left(\Theta_{i}^{L}\right)^{2} \mid \mathbf{b}\right)=\left(\alpha+n_{i}^{L}\right)\left(\alpha+n_{i}^{L}+1\right) \frac{\sum_{k=k_{b}^{L}}^{m} w^{L}(k) g^{L}(k)}{\sum_{k=k_{b}^{L}}^{m} w^{L}(k)} \frac{\left(n^{L}+1\right)\left(n^{L}+2\right)}{(n+6)(n+7)} \\
\mathbb{E}\left(\Theta_{i}^{L}(1-\Psi) \mid \mathbf{b}\right)=\left(\alpha+n_{i}^{L}\right) \frac{\sum_{k=k_{b}^{L}}^{m} \frac{w^{L}(k)}{k \alpha+n^{L}}}{\sum_{k=k_{b}^{L}}^{m} w^{L}(k)} \frac{\left(n^{L}+1\right)\left(n^{S}+1\right)}{(n+6)(n+7)}
\end{gathered}
$$

where $w^{L}(k)=\binom{k}{k_{b}^{L}} p(k) \frac{\Gamma(k \alpha)}{\Gamma\left(n^{L}+k \alpha\right)}$, and $g^{L}(k)=\frac{1}{\left(k \alpha+n^{L}\right)\left(k \alpha+n^{L}+1\right)}$. The meaning of $n, n^{L}, n^{S}$, and $k_{b}^{L}$ can be found in Table 4.
where $w^{L}(k)=\binom{k}{k_{b}^{L}} p(k) \frac{\Gamma(k \alpha)}{\Gamma\left(n^{L}+k \alpha\right)}$, and $g^{L}(k)=\frac{1}{\left(k \alpha+n^{L}\right)\left(k \alpha+n^{L}+1\right)}$. The meaning of $n, n^{L}, n^{S}$, and $k_{b}^{L}$ can be found in Table 4.

# 10. Choice of priors 

The Appendix shows the form of the denominator of the likelihood ratio for the different cases which one may encounter (for any $m$, any parameter $\alpha>0$ for the Dirichlet distribution, and any prior $p(k)$ over $k^{L}$ and $k^{S}$ ). The choice of a value for $\alpha, m$, and of a prior over $k^{L}$ is very delicate. If the expert has strong opinions about the number of L-STR (S-STR) alleles potentially present in nature $(m)$ and in the population of interest ( $k^{L}$ and $k^{S}$ ), he can choose a prior which reflects his beliefs. Otherwise, he can try to use classical priors such as the Poisson distribution, the Negative binomial distribution (both of them truncated so as to have support only over $\{1, \ldots, m\}$ ), or the uniform prior over $\{1, \ldots, m\}$.

### 10.1. Alternative solutions

The most natural choice is to give a uniform prior (over $\{1, \ldots, m\}$ ) to $k^{L}$ and $k^{S}$, combined with that of having all the $k^{L}+k^{S}$ hyperparameters of the Dirichlet priors over $\boldsymbol{\phi}_{h}^{L}$ and $\boldsymbol{\phi}_{h}^{S}$ equal one another. These choices represent the lack of knowledge on the number of categories and make the computations tractable.

One of the limitations of having all the hyperparameters $\alpha$ equal one another is that the posterior for $k^{L}$, given $\mathbf{b}$ uses only the number of distinct alleles of type L as information, and ignores other useful information contained in $\mathbf{b}$. An alternative solution, which compensates for this undesired feature, consists of estimating $k^{L}$ through the database, instead of putting a prior on it. This can be called an empirical Bayesian approach. Notice that such an undesired situation does not appear if personal beliefs are used to specify the prior distribution. Let us define the vector $\boldsymbol{\phi}_{\mathbf{b}}{ }^{L}$ made of the allelic proportions of the L-STR alleles observed in the augmented database, and of a last component $\hat{\phi}_{\mathbf{b}}^{L}$ which is the sum of the allelic proportions of all the L-STR alleles not observed in $\mathbf{b} . \hat{\phi}_{\mathbf{b}}^{L}$ is the probability of observing a new L-STR allele in the $n+1$ th draw from the population. $\boldsymbol{\phi}_{\mathbf{b}}{ }^{L}$ given $k^{L}$ and $\mathbf{b}$ is Dirichlet distributed, hence we can obtain the posterior expected values of $\hat{\phi}_{\mathbf{b}}^{L}$ :

$$
\mathbb{E}\left(\hat{\phi}_{\mathbf{b}}^{L} \mid k^{L}, \mathbf{b}\right)=\frac{\left(k^{L}-k_{\mathbf{b}}^{L}\right) \alpha}{k^{L} \alpha+n^{L}}
$$

The so-called Good-Turing estimator [8] says that the expected value for the probability of the unobserved types can be approximated by the proportion of L-STR singletons (i.e, alleles observed only once) in the database. Stated otherwise,

$$
\mathbb{E}\left(\hat{\phi}_{\mathbf{b}}^{L} \mid k^{L}, \mathbf{b}\right) \approx \frac{n_{1}^{L}}{n^{L}}
$$

where $n_{1}^{L}$ is the number of DIP-STR alleles observed only once in the augmented database. The two quantities (5) and (6) can be equated in order to obtain an empirical Bayesian estimate of $k^{L}$ as

$$
\hat{k}^{L}=\frac{n_{1}^{L} n^{L}+k_{\mathbf{b}}^{L} \alpha n^{L}}{\alpha n^{L}-\alpha n_{1}^{L}}
$$

The likelihood ratio for this choice can be obtained using the same formulas developed in the Appendix by using prior over $k^{L}$ the degenerate prior which gives a probability of one to value $\hat{k}^{L}$. This solution allows one to use more information ( $n_{1}^{L}$ and $n_{1}^{S}$ ) from $\mathbf{b}$.

The third option is to use the plug-in approximation proposed by some literature, which estimates the allelic frequencies by their posterior expectation, after the observation of a database. One of the aims of this paper is to investigate the goodness of this approximation, in the case of a rare type match problem.

We did some experiments using marker MID1950-D20S473 [3], and considering the two cases described in Table 3.


Table 3: Allelic configurations of the victim and of the suspect in the two cases of interest, at marker MID1950-D20S473.
Allele L2 was not contained in the database of reference, hence we are in presence of the rare type match case. The available database, augmented with the victim's and the suspect's DIP-STR alleles, contains 11 different DIP-STR alleles, for a total number of 210 observations (from 105 individuals).

The sensitivity analysis for the $\log _{10}(\mathrm{LR})$, shown in Figure 7, has been conducted for different loci and different combinations of alleles, without showing substantial differences (in terms of sensitivity). Moreover, it tells us that the two plug-in approaches represent acceptable solutions in terms of quantification. We carried on additional experiments that showed us that varying $m$ does not change Figure 7 in a way which is significative for the case at hand.

# 11. Conclusion 

Mostly due to the limited size of the available database (about one hundred people in a given relevant population), the rare type match situation is very likely to be encountered when DIP-STR data is used. The recipients of this new technology should be prepared for such an eventuality, which was not taken into account in the OOBN proposed in Cereda et al. [7]. This paper provides a methodology that allows one to obtain the full Bayesian likelihood ratio also when there are DIP-STR alleles which are not present in the

![img-6.jpeg](img-6.jpeg)

Figure 7: Sensitivity analysis for the $\log_{10}(\mathrm{LR})$ obtained with (i) the full Bayesian approach, (ii) the hybrid Good-Turing plug-in (iii) classical Bayesian plug-in, for the two cases described in Table 3 when the prior over $k^{L}$ and $k^{S}$ is uniform over $\{1, \ldots, m\}$, with $\alpha=1$ and $m=100$.

Reference database among the alleles of the known contributor and of the suspect. This is done by extending the OOBN, and introducing a more complex prior over the allelic frequencies (a mixture of Dirichlet and uniform distribution) based on a previously developed solution for Y-STR data [5]. Notice that this issue also represents an opportunity to discuss the use of plug-in approximations which are compared with the full Bayesian likelihood ratio. They proved to be valid approximations.

The sensitivity analysis of the hyperparameters of the prior is also studied. The results show that the likelihood ratio moderately depends on the choices of the parameters $\alpha$ of the Dirichlet prior. Hence, there is the need for further investigations to find better priors, either less sensitive to hyperparameters, or more realistic, such as it was done for Y-STR data in Cereda [4]. Alternatively, we can hope in more data to make the choice of the prior less important. By looking at Figure 7, we can conclude that unless more data are available, the LR can be determined up to an order of magnitude at best.

# Appendix. Full Bayesian likelihood ratio development 

In Table 4, a summary of the relevant symbols used is reported. The aim of this Appendix is to develop the conditional expectation of the functions reported in Table 2, which constitute the denominator of the likelihood ratio (4). Those conditional expectations can be rewritten in terms of $\boldsymbol{\phi}^{L}, \boldsymbol{\phi}^{S}$, and $\psi$, in the following way:

$$
\begin{aligned}
\mathbb{E}\left(2 \Theta_{i}^{L} \Theta_{j}^{L} \mid \mathbf{b}\right) & =\mathbb{E}\left(2 \Phi_{i}^{L} \Phi_{j}^{L} \Psi^{2} \mid \mathbf{b}\right)=2 \mathbb{E}\left(\Phi_{i}^{L} \Phi_{j}^{L} \mid \mathbf{b}\right) \mathbb{E}\left(\Psi^{2} \mid \mathbf{b}\right) \\
\mathbb{E}\left(\left(\Theta_{i}^{L}\right)^{2}+2 \Theta_{i}^{L}(1-\Psi) \mid \mathbf{b}\right) & =\mathbb{E}\left(\left(\Phi_{i}^{L}\right)^{2} \mid \mathbf{b}\right) \mathbb{E}\left(\Psi^{2} \mid \mathbf{b}\right)+2 \mathbb{E}\left(\Phi_{i}^{L} \mid \mathbf{b}\right) \mathbb{E}(\Psi \mid \mathbf{b}) \mathbb{E}(1-\Psi \mid \mathbf{b})
\end{aligned}
$$

## The distribution of $\Psi$ given $\mathbf{B}$.

As explained in Section 7, $\boldsymbol{\theta}$ can be represented through a set of three independent variables $\left(\boldsymbol{\phi}^{L}, \boldsymbol{\phi}^{S}\right.$, $\psi$ ). The vector $\mathbf{b}$ can also be reduced by sufficiency to three random variables: $\left(n^{L}, \mathbf{n}^{L}, \mathbf{n}^{S}\right)$, where $n^{L}$ is the total number of observed L-STR alleles in the enlarged database, $\mathbf{n}^{L}$ is the vector of length $m$ containing the counts in the augmented database of each of the $m$ L-STR alleles, in an order that corresponds to that of $\boldsymbol{\phi}^{L}$, $\mathbf{n}^{S}$ is the vector of counts of each of the $m$ S-STR alleles. $n^{L}$ is binomial distributed with parameters $(n+4$, $\boldsymbol{\psi}$ ), while $\mathbf{n}^{L}$ is multinomial distributed with parameters $\left(n^{L}, \boldsymbol{\phi}^{L}\right)$. Similarly, $\mathbf{n}^{S}$ is multinomial distributed with parameters $\left(n^{S}, \boldsymbol{\phi}^{S}\right)$, where $n^{S}=n+4-n^{L}$ is the number of S-STR alleles in the augmented database.

It holds that the likelihood for $\boldsymbol{\phi}^{L}, \boldsymbol{\phi}^{S}$, and $\psi$ factors:

$$
p\left(n^{L}, \mathbf{n}^{L}, \mathbf{n}^{S} \mid \boldsymbol{\phi}^{L}, \boldsymbol{\phi}^{S}, \psi\right)=p\left(n^{L} \mid \psi\right) p\left(\mathbf{n}^{L} \mid n^{L}, \boldsymbol{\phi}^{L}\right) p\left(\mathbf{n}^{S} \mid n^{S}, \boldsymbol{\phi}^{S}\right)
$$


Table 4: Some relevant symbols used in the paper.

The priors for $\boldsymbol{\phi}^{L}, \boldsymbol{\phi}^{S}$, and $\psi$ factors as well, since they are independent. Therefore, the posteriors for $\boldsymbol{\phi}^{L}, \boldsymbol{\phi}^{S}$, and for $\psi$ given $\mathbf{b}$ factors as the product of three independent posteriors. Thus, it holds that

$$
p(\psi \mid \mathbf{b}) \propto p\left(n^{L} \mid \psi\right) p(\psi)
$$

which is a product of the density of a binomial distribution and of a beta prior. By conjugacy,

$$
\Psi \mid \mathbf{B}=\mathbf{b} \sim \operatorname{Beta}\left(1+n^{L}, 1+n^{S}\right)
$$

In conclusion, by using properties of the Beta distribution, it holds that

$$
\mathbb{E}\left(\Psi^{2} \mid \mathbf{b}\right)=\frac{\left(n^{L}+1\right)\left(n^{L}+2\right)}{(n+6)(n+7)}
$$

and

$$
\mathbb{E}\left((1-\Psi)^{2} \mid \mathbf{b}\right)=\frac{\left(n^{S}+1\right)\left(n^{S}+2\right)}{(n+6)(n+7)}
$$

The distribution of $\boldsymbol{\phi}^{L}$ and $\boldsymbol{\phi}^{S}$ given $\mathbf{B}$.
Let $p(k)$ be the prior distribution over $k^{L}$ and $k^{S}$. In this section we will omit superscripts L and S from $k, \mathbf{t}, \boldsymbol{\phi}$, and $\mathbf{n}$, in order to obtain general results valid for both cases. Notice that $n$ will stand for $n^{L}$ or $n^{S}$, and $\mathbf{b}$ will stand for $\mathbf{b}^{L}$ or $\mathbf{b}^{S}$ as described in Table 4 (so temporarily, the meaning of $n$, and $\mathbf{b}$ is different from its meaning in the rest of the paper).

Given $k, \mathbf{t}$ is uniformly distributed over the ordered vectors containing $k$ indexes from 1 to $m$. Let us denote with $k_{\mathbf{b}}$ the number of distinct L-STR (or S-STR) alleles observed in the augmented database, and with $\boldsymbol{\phi}_{\mathbf{b}}$ the vector of length $k_{\mathbf{b}}$ containing only the frequencies of the L-STR alleles observed in the augmented database in the order in which they appear in $\boldsymbol{\phi} . \boldsymbol{\phi}_{\mathbf{b}}$ does not sum to one, since there are L-STR

alleles of positive frequency, which are not observed: the total probability mass of the unobserved alleles is $\tilde{\phi}_{\mathbf{b}}=1-\sum_{i=1}^{n_{\mathbf{b}}} \phi_{\mathbf{b}}$. The vector $\boldsymbol{\phi}_{\mathbf{b}}{ }^{*}=\left(\boldsymbol{\phi}_{\mathbf{b}}, \tilde{\phi}_{\mathbf{b}}\right)$ sums up to one.

We can look for the posterior distribution of $\boldsymbol{\phi}_{\mathbf{b}}{ }^{*}$ given the vector $\mathbf{b}$.

$$
p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid \mathbf{b}\right)=\sum_{k} \sum_{\mathbf{t}} p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid \mathbf{b}, \mathbf{t}\right) p(\mathbf{t} \mid k, \mathbf{b}) p(k \mid \mathbf{b})
$$

It can be proved that

- the posterior density $p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid \mathbf{b}, \mathbf{t}\right)$ depends on $\mathbf{t}$ only through $k$. Hence, we can denote it as $p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid \mathbf{b}, k\right)$
- if $k$ is less than $k_{\mathbf{b}}$, then $p(k \mid \mathbf{b})=0$.
- let us denote with $\mathscr{F}_{k, \mathbf{b}}$ the set of ordered vectors $\mathbf{t}$ of length $k$ and compatible with $\mathbf{b}$ (i.e., which contain among others the positions corresponding to the elements in $\mathbf{b}$ ). For all the $\mathbf{t}$ which are not in $\mathscr{F}_{k, \mathbf{b}}$, then $p(\mathbf{t} \mid k, \mathbf{b})=0$.
We can change the summation indexes in (9) to obtain:

$$
p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid \mathbf{b}\right)=\sum_{k=k_{\mathbf{b}}}^{m} p(k \mid \mathbf{b}) p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid k, \mathbf{b}\right) \sum_{\mathbf{t} \in \mathscr{F}_{k, \mathbf{b}}} p(\mathbf{t} \mid k, \mathbf{b})
$$

For any of the $\binom{m-k_{\mathbf{b}}}{k-k_{\mathbf{b}}}$ vectors $\mathbf{t}$ in $\mathscr{F}_{k, \mathbf{b}}, p(\mathbf{t} \mid k, \mathbf{b})$ has the same value $\frac{1}{\binom{k-k_{\mathbf{b}}}{k-k_{\mathbf{b}}}}$, Thus, in the end we have that

$$
p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid \mathbf{b}\right)=\sum_{k=k_{\mathbf{b}}}^{m} p(k \mid \mathbf{b}) p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid k, \mathbf{b}\right)
$$

The distribution $p(k \mid \mathbf{b})$ can be obtained in the following way.

$$
p(k, \mathbf{t}, \boldsymbol{\phi}, \mathbf{b})=p(k) p(\mathbf{t} \mid k) p(\boldsymbol{\phi} \mid \mathbf{t}) p(\mathbf{b} \mid \boldsymbol{\phi})
$$

Integrating out $\boldsymbol{\phi}$, we obtain

$$
p(k, \mathbf{b}, \mathbf{t})=p(k) p(\mathbf{t} \mid k) \int_{\boldsymbol{\phi}} p(\boldsymbol{\phi} \mid \mathbf{t}) p(\mathbf{b} \mid \boldsymbol{\phi}) \mathrm{d} \boldsymbol{\phi}
$$

where the integral contains a Dirichlet density and the categorical density defined in (2). They are conjugate, thus we obtain

$$
p(k, \mathbf{t} \mid \mathbf{b}) \propto p(k) p(\mathbf{t} \mid k) \frac{\Gamma(k \alpha)}{\Gamma(n+k \alpha)}
$$

Now we can sum over the $\mathbf{t}$ compatible with $\mathbf{b}$, to get to

$$
p(k \mid \mathbf{b}) \propto\binom{k}{k_{\mathbf{b}}} p(k) \frac{\Gamma(k \alpha)}{\Gamma(n+k \alpha)}
$$

In conclusion,

$$
p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid \mathbf{b}\right) \propto \sum_{k=k_{\mathbf{b}}}^{m}\binom{k}{k_{\mathbf{b}}} p(k) \frac{\Gamma(k \alpha)}{\Gamma(n+k \alpha)} p\left(\boldsymbol{\phi}_{\mathbf{b}}{ }^{*} \mid k, \mathbf{b}\right)
$$

where $\boldsymbol{\Phi}_{\mathbf{b}}{ }^{*} \mid K=k, \mathbf{B}=\mathbf{b} \sim \operatorname{Dir}^{k_{\mathbf{b}}+1}\left(\alpha+\bar{n}_{1}, \ldots, \alpha+\bar{n}_{k_{\mathbf{b}}},\left(k-k_{\mathbf{b}}\right) \alpha\right)$, and $\overline{\mathbf{n}}$ is the vector of length $k_{\mathbf{b}}$ with the positive elements of $\mathbf{n}$.

Therefore, (12) is a mixture of Dirichlet distributions with weights $w(k)=\binom{k}{k_{\mathbf{b}}} p(k) \frac{\Gamma(k \alpha)}{\Gamma(n+k \alpha)}$. Using properties of the Dirichlet distribution we obtain that, $\forall i, j$ corresponding to different observed DIP-STR alleles:

$$
\begin{aligned}
& \mathbb{E}\left(\Phi_{i} \Phi_{j} \mid \mathbf{b}\right)=\left(\alpha+n_{i}\right)\left(\alpha+n_{j}\right) \frac{\sum_{k=k_{\mathbf{b}}}^{m} w(k) g(k)}{\sum_{k=k_{\mathbf{b}}}^{m} w(k)} \\
& \mathbb{E}\left(\Phi_{i}^{2} \mid \mathbf{b}\right)=\left(\alpha+n_{i}\right)\left(\alpha+n_{i}+1\right) \frac{\sum_{k=k_{\mathbf{b}}}^{m} w(k) g(k)}{\sum_{k=k_{\mathbf{b}}}^{m} w(k)}
\end{aligned}
$$

where $g(k)=\frac{1}{(k a+n)(k a+n+1)}$.
The conditional expectations in Table 2
Using (7), (8), (13) and (14), we obtain that, $\forall i, j$ corresponding to different observed alleles,

$$
\begin{aligned}
\mathbb{E}\left(\Theta_{i}^{L} \Theta_{j}^{L} \mid \mathbf{b}\right) & =\mathbb{E}\left(\Phi_{i}^{L} \Phi_{j}^{L} \Psi^{2} \mid \mathbf{b}\right)=\mathbb{E}\left(\Phi_{i}^{L} \Phi_{j}^{L} \mid \mathbf{b}\right) \mathbb{E}\left(\Psi^{2} \mid \mathbf{b}\right) \\
& =\left(\alpha+n_{i}^{L}\right)\left(\alpha+n_{j}^{L}\right) \frac{\sum_{k=k_{b}^{L}}^{m} w^{L}(k) g^{L}(k)}{\sum_{k=k_{b}^{L}}^{m} w^{L}(k)} \frac{\left(n^{L}+1\right)\left(n^{L}+2\right)}{(n+6)(n+7)} \\
\mathbb{E}\left(\left(\Theta_{i}^{L}\right)^{2} \mid \mathbf{b}\right)= & \mathbb{E}\left(\left(\Phi_{i}^{L}\right)^{2} \Psi^{2} \mid \mathbf{b}\right)=\mathbb{E}\left(\left(\Phi_{i}^{L}\right)^{2} \mid \mathbf{b}\right) \mathbb{E}\left(\Psi^{2} \mid \mathbf{b}\right)= \\
= & \left(\alpha+n_{i}^{L}\right)\left(\alpha+n_{i}^{L}+1\right) \frac{\sum_{k=k_{b}^{L}}^{m} w^{L}(k) g^{L}(k)}{\sum_{k=k_{b}^{L}}^{m} w^{L}(k)} \frac{\left(n^{L}+1\right)\left(n^{L}+2\right)}{(n+6)(n+7)} \\
\mathbb{E}\left(\Theta_{i}^{L}(1-\Psi) \mid \mathbf{b}\right)= & \mathbb{E}\left(\Phi_{i}^{L} \mid \mathbf{b}\right)\left(\mathbb{E}(\Psi \mid \mathbf{b})-\mathbb{E}\left(\Psi^{2} \mid \mathbf{b}\right)\right)= \\
= & \left(\alpha+n_{i}^{L}\right) \frac{\sum_{k=k_{b}^{L}}^{m} \frac{w^{L}(k)}{k a+n^{L}}}{\sum_{k=k_{b}^{L}}^{m} w^{L}(k)} \frac{\left(n^{L}+1\right)\left(n^{S}+1\right)}{(n+6)(n+7)}
\end{aligned}
$$

where $n$ and $\mathbf{b}$ have now their original meaning, and $w^{L}(k)=\binom{L}{k_{b}^{L}} p(k) \frac{\Gamma(k \alpha)}{\Gamma\left(n^{L}+k \alpha\right)}$, and $g^{L}(k)=\frac{1}{(k a+n^{L})(k a+n^{L}+1)}$.
These formulas can be directly used to obtain the conditional expectations of the last three rows of Table 2. In a very similar way one can easily obtain the conditional expectations contained in the first three rows.
