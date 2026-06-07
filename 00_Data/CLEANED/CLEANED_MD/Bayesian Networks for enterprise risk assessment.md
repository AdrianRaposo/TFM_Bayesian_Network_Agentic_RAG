# Bayesian networks for enterprise risk assessment 

C. E. Bonafede ${ }^{\dagger}$, P. Giudici ${ }^{\dagger \dagger *}$<br>University of Pavia

(Dated: October 19, 2018)

## Abstract

According to different typologies of activity and priority, risks can assume diverse meanings and it can be assessed in different ways.

In general risk is measured in terms of a probability combination of an event (frequency) and its consequence (impact). To estimate the frequency and the impact (severity) historical data or expert opinions (either qualitative or quantitative data) are used. Moreover qualitative data must be converted in numerical values to be used in the model.

In the case of enterprise risk assessment the considered risks are, for instance, strategic, operational, legal and of image, which many times are difficult to be quantified. So in most cases only expert data, gathered by scorecard approaches, are available for risk analysis.

The Bayesian Network is a useful tool to integrate different information and in particular to study the risk's joint distribution by using data collected from experts.

In this paper we want to show a possible approach for building a Bayesian networks in the particular case in which only prior probabilities of node states and marginal correlations between nodes are available, and when the variables have only two states.

Keywords: Bayesian Networks, Enterprise Risk Assessment, Mutual Information

# INTRODUCTION 

A Bayesian Net (BN) is a directed acyclic graph (probabilistic expert system) in which every node represents a random variable with a discrete or continuous state $[2,3]$.

The relationships among variables, pointed out by arcs, are interpreted in terms of conditional probabilities according to Bayes theorem.

With the BN is implemented the concept of conditional independence that allows the factorization of the joint probability, through the Markov property, in a series of local terms that describe the relationships among variables:

$$
f\left(x_{1}, x_{2}, \ldots, x_{n}\right)=\prod_{i=1}^{n} f\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

where $p a\left(x_{i}\right)$ denotes the states of the predecessors (parents) of the variable $X_{i}$ (child) $[1,2,3,6]$. This factorization enable us to study the network locally.

A Bayesian Network requires an appropriate database to extract the conditional probabilities (parameter learning problem) and the network structure (structural learning problem) $[1,3,13,16]$.

The objective is to find the net that best approximates the joint probabilities and the dependencies among variables.

After we have constructed the network one of the common goal of bayesian network is the probabilistic inference to estimate the state probabilities of nodes given the knowledge of the values of others nodes. The inference can be done from children to parents (this is called diagnosis) or vice versa from parents to children (this is called prediction) [2, 13, 15].

However in many cases the data are not available because the examined events can be new, rare, complex or little understood. In such conditions experts' opinions are used for collecting information that will be translated in conditional probability values or in a certain joint or prior distribution (Probability Elicitation) [11, 12, 16, 19].

Such problems are more evident in the case in which the expert is requested to define too many conditional probabilities due to the number of the variable's parents. So, when possible, is worthwhile to reduce the number of probabilities to be specified by assuming some relationships that impose bonds on the interactions between parents and children as for example the noisy-OR and its variation and genralization [3, 9, 10, 14, 16].

In the business field, Bayesian Nets are a useful tool for a multivariate and integrated

analysis of the risks, for their monitoring and for the evaluation of intervention strategies (by decision graph) for their mitigation $[3,5,7]$.

Enterprise risk can be defined as the possibility that something with an impact on the objectives happens, and it is measured in terms of combination of probability of an event (frequency) and of its consequence (impact).

The enterprise risk assessment is a part of Enterprise Risk Management (ERM) where to estimate the frequency and the impact distributions historical data as well as expert opinions are typically used $[4,5,6,7]$. Then such distributions are combined to get the loss distribution.

In this context Bayesian Nets are a useful tool to integrate historical data with those coming from experts which can be qualitative or quantitative [19].

# OUR PROPOSAL 

What we present in this work is the construction of a Bayesian Net for having an integrated view of the risks involved in the building of an important structure in Italy, where the risk frequencies and impacts were collected by an ERM procedure unsing expert opinions.

We have constructed the network by using an already existing database (DB) where the available information are the risks with their frequencies, impacts and correlation among them. In total there are about 300 risks.

In our work we have considered only the frequencies of risks and no impacts. With our BN we construct the risks' joint probability and the impacts could be used in a later phase of scenario analysis to evaluate the loss distribution under the different scenarios [5].

In table 1 there is the DB structure used for network learing and in which each risk is considered as a binary variable (one if the risk exists (yes) and zero if the risk dosen't exist (not)). Therefore, for each considered risk in the network there will be one node with two states (one $\equiv Y$ and zero $\equiv N$ ).

TABLE I: Expert values database structure (Learning table)


The task is, therefore, to find the conditional probabilities tables by using only the cor-

relations and the marginal frequencies. Instead, the net structure is obtained from table 1 by following the node relationships given by correlations.

The main ideas for finding a way to construct a BN have been: first to find the joint probabilities as functions of only the correlations and the marginal probabilities; second to understand how the correlations are linked with the incremental ratios or the derivatives of the child's probabilities as functions of the parent's probabilities. This choice is due to the fact that parent and child interact through the values of conditional probabilities; the derivatives are directly linked to such probabilities and, therefore, to the degree of interaction between the two nodes and, hence with the correlation.

Afterwards we have understood as to create equations, for the case with dependent parents we have used the local network topology to set the equations.

We have been able to calculate the CPT up to three parents for each child. Although there is the possibility to generalize to more than three parents, it is necessary to have more data which are not available in our DB. So when four or more parents are present we have decided to divide and reduce to cases with no more than three parents. To approximate the network we have "separated" the nodes that give the same effects on the child (as for example the same correlations) by using auxiliary nodes [3]. When there was more than one possible scheme available we have used the mutual information (MI) criterion as a discriminating index by selecting the approximation with the highest total MI; this is the same to choose the structure with the minimum distance between the network and the target distribution $[17,18]$.

We have analyzed first the case with only one parent to understand the framework, then it has been seen what happens with two independent parents and then dependent. Finally we have used the analogies between the cases with one and two parents for setting the equations for three parents.

# One parent case solution 

The case with one parent (figure 1) is the simplest. Let $\mathrm{P}(\mathrm{F})$ and $\mathrm{P}(\mathrm{C})$ be the marginal probability given from expert (as in table 1):

- For the parent, F, we have: $\mathrm{P}(\mathrm{F}=\mathrm{Y})=\mathrm{x}, \mathrm{P}(\mathrm{F}=\mathrm{N})=1-\mathrm{x}$;

- For the child, C, we have: $\mathrm{P}(\mathrm{C}=\mathrm{Y})=\mathrm{y}, \mathrm{P}(\mathrm{C}=\mathrm{N})=1-\mathrm{y}$;

# Parent (E) <br> Child (C) 

FIG. 1: One parent scheme

The equations to find either the conditional probabilities or the joint probabilities are:

$$
\begin{array}{ll}
\text { CPT equation system } & \text { Joint equation system } \\
\alpha_{1} x+\alpha_{2}(1-x)=y ; & c_{1}=\rho M+x y \\
\alpha_{1}-\alpha_{2}=k ; & c_{2}=y-\rho M-x y \\
\alpha_{1}+\alpha_{3}=1 ; & c_{3}=x-\rho M-x y \\
\alpha_{2}+\alpha_{4}=1 ; & c_{4}=1-y-x+\rho M+x y
\end{array}
$$

where $k=\rho \sqrt{\frac{V a r[C]}{V a r[F]}}$; whit $\alpha_{i}$ and $c_{i}$ we indicate respectively the conditional and the joint probabilities.

Considering that probabilities $c_{i}$ and $\alpha_{i}$ must be positive either the marginal probabilities or the correlation value should be constrained. If the marginal probabilities are fixed then the correlation values must be constrained, which will be normally the case, as estimates of probabilities are more reliable.

It is not possible to have any value of correlation given the marginal probabilities. Indeed, as we want to maintain the marginal probabilities as fixed by the expert, correlation limits can be determined as follows:

$$
\rho>-\frac{x y}{M}=A ; \rho>\frac{y+x(1-y)-1}{M}=D ; \rho<\frac{x(1-y)}{M}=B ; \rho<\frac{y(1-x)}{M}=C
$$

and the correlation interval will be:

$$
\rho \in[\max (A, D) ; \min (B, C)]
$$

## Two parents case solutions

This case (figure 2) is more complicated than the one before. In this situation a further difficulty is that the given expert correlations are only pairwise marginal and, therefore, we need more information to find the CPT.

For example the joint moment among the nodes which is not in the DB. Consequently there can be more than one CPT, corresponding to different values of the joint moment, for the same marginal correlation and probability.
![img-0.jpeg](img-0.jpeg)

FIG. 2: Two independent parents (a) and dependent parents (b)

The joint moment becomes thus a project parameter to be set by using an appropriate criterion. We define the standardized joint moment among three variables to be:

$$
\rho_{N_{i} N_{j} N_{k}}=\frac{E\left[\left(N_{i}-E\left[N_{i}\right]\right)\left(N_{j}-E\left[N_{j}\right]\right)\left(N_{k}-E\left[N_{k}\right]\right)\right]}{\sqrt[3]{V a r\left[N_{i}\right] V a r\left[N_{j}\right] V a r\left[N_{k}\right]}}
$$

To choose among such CPTs we have used the total mutual information $\left(I_{\text {total }}\right)$ by selecting that CPT with the $\rho_{N_{i} N_{j} N_{k}}$ that gives the minimum $I_{\text {total }}$.

In this case we have to distinguish between independent and dependent parents. The solutions are:

$$
\begin{aligned}
& \text { CPT equation system for independent parents } \\
& f(x, z)=\left(\alpha_{1}-\alpha_{2}-\alpha_{3}+\alpha_{4}\right) x z+\left(\alpha_{2}-\alpha_{4}\right) x+ \\
& +\left(\alpha_{3}-\alpha_{4}\right) z+\alpha_{4}=y \\
& \frac{\partial f}{\partial x}=\left(\alpha_{1}-\alpha_{2}-\alpha_{3}+\alpha_{4}\right) z+\left(\alpha_{2}-\alpha_{4}\right)=\frac{\left(\rho_{A F}\right)\left(M_{A F}\right)}{x(1-x)} \\
& \frac{\partial f}{\partial y}=\left(\alpha_{1}-\alpha_{2}-\alpha_{3}+\alpha_{4}\right) x+\left(\alpha_{3}-\alpha_{4}\right)=\frac{\left(\rho_{B F}\right)\left(M_{B F}\right)}{z(1-z)} \\
& \frac{\partial^{2} f}{\partial x \partial z}=\frac{\partial^{2} f}{\partial x \partial x}=\left(\alpha_{1}-\alpha_{2}-\alpha_{3}+\alpha_{4}\right)=\frac{\left(\rho_{A B F}\right)\left(M_{A B F}\right)}{x(1-x) z(1-z)} \\
& \alpha_{1}+\alpha_{5}=1 \\
& \alpha_{2}+\alpha_{6}=1 \\
& \alpha_{3}+\alpha_{7}=1 \\
& \alpha_{4}+\alpha_{8}=1
\end{aligned}
$$


where $M_{B F}=\sqrt{z(1-z) y(1-y)}, M_{A F}=\sqrt{x(1-x) y(1-y)}, M_{A B}=\sqrt{x(1-x) z(1-z)}$ and $M_{A B F}=\sqrt[3]{x(1-x) z(1-z) y(1-y)}$. As before the $\alpha_{i}$ and $c_{i}$ are respectively the conditional and the joint probabilities.

The problem is now setting the marginal correlations when those given from experts are not consistent with the marginal probabilities. Differently from the case with one parent where the correlation belongs to an interval, with two parents the admissible pairs $\left(\rho_{A F}, \rho_{B F}\right)$

can be shown to belong to an area.
To approach this problem we have decided to decrease the values of the two correlations $\rho_{B F}$ and $\rho_{A F}$ with a fixed step by maintaining their relative difference. At each step we verified the existence of a value of $\rho_{A B F}$ which supports the new pair $\left(\rho_{A F}, \rho_{B F}\right)$. If it exists the process is stopped, otherwise it goes to the next step; and so on.

If the correlation $\rho_{A B}$ is different from zero (dependent parents), we can set it in advance using the interval obtained for the case of one parent; afterward the $\rho_{A B}$ 's value is used into the joint equation system. Then we can work again only on the pair $\left(\rho_{A F}, \rho_{B F}\right)$ by considering the same procedure for independent parents and selecting $\rho_{N_{i} N_{j} N_{k}}$.

# Three parents case solutions 

As before two equation systems are obtained. One system for the case with independent (see figure 3 a) parents by which the CPT is directly calculated; another one when there are some correlations between parents (see figure 3 b) and in this case the joint probabilities are calculated instead of the conditional ones. To define the equation systems the analogies between the cases with one and two parents have been exploited.
![img-1.jpeg](img-1.jpeg)

FIG. 3: Three independent parents (a) and dependent parents (b).

The solutions for independent and dependent parents are in table 2. In such equations, obviously, there will be more missing data which are all the standardized joint moments among every two parents and the child and among all parents and the child. So what we do in such a situation is to use the procedure for the case of two parents for each pair of nodes and set the correlation values such that they will be feasible for the all couples. Note that the correlation levels are now less than in previous cases. Moreover in this case the standardized joint moment among all variables is set at zero to make the research less complex.

Furthermore, difficulties arise when there are large differences among the parents'

marginal probabilities. Therefore, when there are more than three parents, we have decided to split them. Parents are split from the others by using the mutual information criterion $[17,18]$.

As before, for the case of dependent parents to select the feasible marginal correlations and the standardized joint moments, we start to look for the admissible correlation between the nodes with one parent ( A and B ), then for the nodes with two parents ( C has B and A as predecessor) and finally we set the joint moment and marginal correlations for the node with three parents (F). Obviously, now the procedure is more complex and it is more difficult to select the parameters.

TABLE II: Equation systems for three parents scheme


# CONCLUSION 

So far we have seen that using the equation systems for conditional and joint probabilities the CPTs can be obtained. The method can be generalized to the case with more three parents, but there are problems in setting more parameters (standardized joint moment) and in looking for more complicated feasible marginal correlation areas.

So to develop a network we propose to use, separately, firstly the equations and procedure for the one parent; secondly those for two parents distinguishing when they are dependent and not. Finally we use the equations and the procedures, when possible, for the three parents case by distinguishing also in this situation between dependent and independent parents; otherwise we split one parent from the others by using the mutual information as splitting index $[17,18]$.

We remark that we need to reduce to a more simple case those configurations with more than three parents. We can achieve this trying to estimate a local approximate structure, with only one, two and three parents, by "separating" those that give different effects on the child (as for instance different incremental ratios). If there are more schemes available for the substitution we select that with the highest MI $\left(I_{\text {total }}\right)[17,18]$.

It is important to be noted that such method is modular, this is if we add or delete a node we can use the appropiate system (one, two or three nodes) to according to we add or delete a parent or a child.

# ACKNOWLEDGMENTS 

The authors acknowledge financial support from the MIUR-FIRB 2006-2009 project and MUSING project contract number 027097.

[^0]
[^0]:    * ${ }^{\dagger}$ bonafede@eco.unipv.it; ${ }^{\dagger \dagger}$ giudici@unipv.it; URL: www.datamininglab.it
    [1] Heckerman D. (1996). A tutorial on learning with Bayesian networks. Microsoft Research tech. report MSR-TR-95-06. Revised November 1996, from http://research.microsoft.com.
    [2] Cowell R.G., Dawid A. P., Lauritzen S.L. and Spiegelhalter D.J. (1999). Probabilistic Networks and Expert Systems. New York, USA: Springer.
    [3] Jensen F.V. (2001). Bayesian Networks and Decision Graphs. New York, USA: Springer.
    [4] Cruz M.G. (2002). Modeling, measuring and hedging operational risk. West Sussex, England: John Wiley and Sons.
    [5] Alexander C.(Ed.). (2003). Operational Risk, regulation analysis and management. London, England: Prentice Hall.

[6] Giudici P. (2003). Applied Data Mining. West Sussex, England: John Wiley and Sons.
[7] Cruz M.G.(Ed.). (2004). Operational risk modeling and Analysis. London, England: Risk Books.
[8] Fanoni F., Giudici P. and Muratori G.M. 2005. Operational risk: measurement, modelling and mitigation. Milan, Italy: Il Sole 24 Ore.
[9] Zagorecki A., and Druzdzel M. (2004). An Empirical Study of Probability Elicitation under Noisy-OR Assumption. In Proceedings of the Seventeenth International Florida Artificial Intelligence Research Society Conference (FLAIRS 2004), pp 800-885.
[10] Francisco J.D., and Severino F.G. (2003). Efficient Computation for the Noisy MAX. International journal of intelligent systems, Vol. 18, pp 165-177.
[11] Wiegmann D.A. (2005). Developing a Methodology for Eliciting Subjective Probability Estimates During Expert Evaluations of Safety Interventions: Application for Bayesian Belief Networks. Aviation Human Factors Division, October, from www.humanfactors.uiuc.edu.
[12] Daneshkhah A.R. (2004). Uncertainty in Probabilistic Risk Assessment: A Review. The University Of Sheffield, August 9, from http://www.shef.ac.uk/beep/publications.html.
[13] Murphy K.P. (2001). An introduction to graphical models. A Brief Introduction to Graphical Models and Bayesian Networks, May 10, from http://www.cs.ubc.ca.
[14] Agnieszka 0., Druzdzel M. and Wasyluk H. (2001). Learning Bayesian network parameters from small data sets: application of Noisy-OR gates. International journal of Approximate Reasoning, Vol. 27, pp 165-182.
[15] Jaakkola T.S. and Jordan M.I. (1999). Variational probabilistic inference and the QMR-DT database. Journal of Artificial Intelligence Research, Vol. 10, pp 291-322.
[16] Druzdzel M.J. and van der Gaag L.C. (2000). Building Probabilistic Networks: Where Do the Numbers Come From? IEEE Transactions on Knowledge and Data Engineering, Vol. 12(4), pp 481-486.
[17] Williamson J. (2000). Approximating discrete probability distributions with Bayesian networks IEEE Transactions on Information Theory, Vol. 14(3), pp 462-467.
[18] Kleiter G.D. and Jirousek R. (1996). Learning Bayesian Networks under the Control of Mutual Information Proceedings in Information Processing and Management of Uncertainty in Knowledge-Based Systems, pp 985-990.
[19] Druzdzel M.J. and van der Gaag L.C. (1995). Elicitation of Probabilities for Belief Networks:

Combining Qualitative and Quantitative Information Proceedings of the Eleventh Conference on Uncertainty in Artificial Intelligence, pp 141-148.