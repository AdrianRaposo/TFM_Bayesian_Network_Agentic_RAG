# HAL open science 

## Fault diagnosis of industrial systems by conditional Gaussian network including a distance rejection criterion

Sylvain Verron, Teodor Tiplica, Abdessamad Kobi

## To cite this version:

Sylvain Verron, Teodor Tiplica, Abdessamad Kobi. Fault diagnosis of industrial systems by conditional Gaussian network including a distance rejection criterion. Engineering Applications of Artificial Intelligence, 2010, 23 (7), pp.1229-1235. 10.1016/j.engappai.2010.05.002 . inria-00516954

## HAL Id: inria-00516954 <br> https://inria.hal.science/inria-00516954v1

Submitted on 13 Sep 2010

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Fault Diagnosis of Industrial Systems by Conditional Gaussian Network including a Distance Rejection Criterion 

Sylvain Verron*, Teodor Tiplica, Abdessamad Kobi<br>LASQUO/ISTIA - 62, avenue Notre Dame du Lac - 49000 Angers, France


#### Abstract

The purpose of this article is to present a method for industrial process diagnosis with Bayesian network, and more particularly with Conditional Gaussian Network (CGN). The interest of the proposed method is to combine a discriminant analysis and a distance rejection in a CGN in order to detect new types of fault. The performances of this method are evaluated on the data of a benchmark example: the Tennessee Eastman Process. Three kinds of fault are taken into account on this complex process. The challenging objective is to obtain the minimal recognition error rate for these three faults and to obtain sufficient results in rejection of new types of fault.


Key words: Fault Diagnosis; Distance Rejection ;Bayesian Networks;
Conditional Gaussian Network

## 1. Introduction

Nowadays, industrial processes are more and more complex. So, they include a lot of sensors. Consequently, an important amount of data can be obtained from a process. A process dealing with many variables can be named multivariate process. But, the monitoring of a multivariate process cannot be reduced to the monitoring of each process variable because the correlations between

[^0]
[^0]:    *Corresponding author

    Email address: sylvain.verron@univ-angers.fr (Sylvain Verron)

the variables have to be taken into account. Process monitoring is an essential task. The final goal of the process monitoring is to reduce variability, and so, to improve the quality of the product (Montgomery (1997)). The process monitoring comprises four procedures: fault detection (decide if the process is under normal condition or out-of-control); fault identification (identify the variables implicated in an observed out-of-control status); fault diagnosis (find the root cause of the disturbance); process recovery (return the process to a normal status).

Three major kinds of approaches exists for process monitoring (Chiang et al. (2001)): data-driven, analytical and knowledge-based. Theoretically, the best method is the analytical one because this method constructs mathematic models of the process. But, for large systems (lots of inputs, outputs and states), obtaining detailed models is almost impossible. In the knowledge-based category are placed methods that are based on qualitative models like fault tree, FMECA, expert systems (Venkatasubramanian et al. (2003)). Finally, data-driven methods are techniques based on rigorous statistical development of process data. Our interest is to monitor large systems, and so, we are concerned with data-driven methods.

In literature, we can find many different data-driven techniques for process control. For the fault detection of industrial processes many methods have been submitted: univariate statistical process control (Shewhart charts) (Shewhart (1931); Montgomery (1997)), multivariate statistical process control ( $T^{2}$ and Q charts) (Hotelling (1947); Westerhuis et al. (2000)), and some PCA (Principal Component Analysis) based techniques (Jackson (1985)) like Multiway PCA or Moving PCA (Bakshi (1998)). Kano et al. (2002) make comparisons between these different techniques. For the fault identification procedure, one of the better statistical techniques is the MYT decomposition of the $T^{2}$ statistic (Mason et al. (1997)). Finally, for the fault diagnosis techniques we can cite the book of Chiang et al. (2001) which presents a lot of them (PCA based techniques, Fisher Discriminant Analysis, PLS based techniques, etc).

The purpose of this article is to present a new method for the diagnosis

of faults in large industrial systems. This method is based on Bayesian networks and particularly Bayesian network classifiers. The major interest of this method is the combination of a discriminant analysis and distance rejections in a Bayesian network in order to detect new types of fault of the system.

The article is structured in the following manner. In section 2, we introduce the classical method to diagnose faults with Bayesian network classifiers. The section 3 gives a method to apply a distance rejection on a fault of a system with a Bayesian network, and presents the combination of this distance rejection with the classical diagnosis with Bayesian network. The section 4 presents an application of the proposed method for diagnosis of three types of fault on the benchmark Tennessee Eastman Problem. Finally, we conclude on interests and limitations of this method, and we present some perspectives of the fault diagnosis with Bayesian network classifiers.

# 2. Bayesian Network for Fault Diagnosis 

### 2.1. Fault Diagnosis as classification task

Once a problem (fault) has been detected in the evolution of the process by the mean of a detection method, we need to identify (diagnosis) the belonging class of this fault. Thereby, the diagnosis problem can be viewed as the task to correctly classify this fault in one of the predefined fault classes. The classification task needs the construction of a classifier (a function allocating a class to the observations described by the variables of the system). Two types of classification exist: unsupervised classification which objective is to identify the number and the composition of each class present in the data structure; supervised classification where the number of classes and the belonging class of each observation is known in a learning sample and whose objective is to class new observations to one of the existing classes. For example, given a learning sample of a bivariate system with three different known faults as illustrated in the figure 1, we can easily use supervised classification to classify a new faulty observation. A feature selection can be used in order to select only the most

informative variables of the problem (Verron et al. (2008)). In this study, we will use the Bayesian network as a supervised classification tool.
[Figure 1 about here.]

# 2.2. Bayesian network 

A Bayesian Network (BN) (Pearl (1988)) is a probabilistic graphical model where each variable is a node. Edges of the graph represent dependences between linked nodes. A formal definition of Bayesian network (Jensen (1996)) is a couple $\{\mathbf{G}, \mathbf{P}\}$ where:
$\{\mathbf{G}\}$ is a directed acyclic graph, whose nodes are random variables $\boldsymbol{X}=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ and whose missing edges represent conditional independences between the variables,
$\{\mathbf{P}\}$ is a set of conditional probability distributions (one for each variable): $P=\left\{p\left(x_{1} \mid p a\left(x_{1}\right)\right), \ldots, p\left(x_{n} \mid p a\left(x_{n}\right)\right)\right\}$ where $p a\left(x_{i}\right)$ is the set of parents of the node $X_{i}$.

The set P defines the joint probability distribution as:

$$
p(\boldsymbol{x})=\prod_{i=1}^{n} p\left(x_{i} \mid p a\left(x_{i}\right)\right)
$$

Theorically, variables $X_{1}, X_{2}, \ldots, X_{n}$ can be discrete or continuous. But, in practice, for exact computation, only the discrete and the Gaussian case can be treated. Such a network is often called Conditional Gaussian Network (CGN). In this context, to ensure availability of exact computation methods, discrete variables are not allowed to have continuous parents (see Lauritzen and Jensen (2001); Madsen (2008)).

Practically, the conditional probability distribution is described for each node by his Conditional Probability Table (CPT). In a CGN, three cases of CPT can be found. The first one is for a discrete variable with discrete parents. By example, we take the case of two discrete variables $A$ and $B$ of respective dimensions $a$ and $b$ (with $a_{1}, a_{2}, \ldots, a_{a}$ the different modalities of $A$, and

$b_{1}, b_{2}, \ldots, b_{b}$ the different modalities of $B)$. If $A$ is parent of $B$, then the CPT of $B$ is represented in table 1 .
[Table 1 about here.]

We can see that the utility of the CPT is to condense the informations about the relations of $B$ with his parents. We can denote that the dimension of this CPT is $a \times b$. In general the dimension of the CPT of a discrete node (dimension $x$ ) with $p$ parents (discrete) $Y_{1}, Y_{2}, \ldots, Y_{p}$ (dimension $y_{1}, y_{2}, \ldots, y_{p}$ ) is $x \prod_{i=1}^{p} y_{i}$.

The second case of CPT is for a continuous variable with discrete parents. Assuming that $B$ is a Gaussian variable, and that $A$ is a discrete parent of $B$ with $a$ modalities, the CPT of $B$ can be represented as in the table 2 where $P\left(B \mid a_{1}\right) \sim \mathcal{N}\left(\mu_{a_{1}}, \Sigma_{a_{1}}\right)$ indicates that $B$ conditioned to $A=a_{i}$ follows a multivariate normal density function with parameters $\mu_{a_{i}}$ and $\Sigma_{a_{i}}$. If we have more than one discrete parent, the CPT of $B$ will be composed of $\prod_{i=1}^{p} y_{i}$ Gaussian distribution where $y_{i}$ represents the respective number of modalities of the parent nodes $Y_{1}, Y_{2}, \ldots, Y_{p}$.
[Table 2 about here.]

The third case is when a continuous node $B$ has a continuous parent $A$. In this case, we obtain a linear regression and we can write, for a fixed value $a$ of $A$, that $B$ follows a Gaussian distribution $P(B \mid A=a) \sim \mathcal{N}\left(\mu_{B}+\beta \times a ; \Sigma_{B}\right)$ where $\beta$ is the regression coefficient. Evidently, the three different cases of CPT enumerated can be combined for different cases where a continuous variable has several discrete parents and several continuous (Gaussian) parents.

The classical use of a Bayesian network (or Conditional Gaussian Network) is to enter evidence in the network (an evidence is the observation of the values of a set of variables). Thus, the information given by the evidence is propagated in the network in order to update the knowledge and obtain a posteriori probabilities on the non-observed variables. This propagation mechanism is called inference. As its name suggests, in a Bayesian network, the inference is based on the Bayes rule. Many inference algorithms (exact or approximate) have been

developed, but one of the more exploited is the junction tree algorithm (Jensen et al. (1990)).

In this article, we propose a method exploiting a CGN in order to diagnose a system, and particularly in the difficult case of simultaneous faults.

# 2.3. Conditional Gaussian Network for fault diagnosis 

In the context of the diagnosis of industrial systems, Bayesian networks and Conditional Gaussian Networks have been already used and give convenient results compared to other classification tools like support vector machines, neural networks or k-nearest neighborhoods (Pernkopf (2005); Perzyk et al. (2005); Tiplica et al. (2006); Verron et al. (2007b,d)). As the performances of the CGN have been previously demonstrated (Verron et al. (2007b,d)), we choose this classifier in this article which is equivalent to a Discriminant Analysis (DA). So, we name the class node $D A$ (coding the different known faults of the system), and the observation node $\boldsymbol{X}$ (a normal multivariate node). The figure 2 presents the CGN equivalent to a discriminant analysis, with the probability tables associated to each node. To simplify, the a priori probability of each class $F_{i}$ is fixed to $p\left(F_{i}\right)=\frac{1}{k}$. The node $\boldsymbol{X}$ follows the different normal probability densities $(\mathcal{N})$ conditionally to the class of $D A$, where $\boldsymbol{\mu}_{i}$ is the mean vector of the fault $F_{i}, \boldsymbol{\Sigma}_{i}$ is the covariance matrix of the fault $F_{i} . \boldsymbol{\mu}_{i}$ and $\boldsymbol{\Sigma}_{i}$ are estimated on the fault database by Maximum Likelihood Estimation (MLE) (Duda et al. (2001)). On the simple example of the figure 1, the CGN gives the different areas of classification of the figure 3.
[Figure 2 about here.]
[Figure 3 about here.]
As we mentioned previously, an objective of a fault diagnosis method is to classify new observations to one of the existing classes. But, in certain cases, the observation may be a new type of fault (unknown or unseen before). This is the case when the observation is distant of any known class of fault (example

of the point A in figure 1). In order to detect these new types of fault, we have to use a criterion called distance rejection (see Denoeux et al. (1997)). Next, we will see how to take into account this criterion in a CGN, and how to combine it with the diagnosis of the previous CGN.

# 3. Integration of Distance Rejection 

### 3.1. Distance rejection in a CGN

Assuming one class of fault (Gaussian), the rejection of an observation is equivalent to a $T^{2}$ control chart (Hotelling (1947)) on the data of this fault. In previous works (Verron et al. (2007c,a)), we have demonstrated that a $T^{2}$ control chart could be modelized with a Bayesian network, and more particularly with a CGN. Assuming $\boldsymbol{\mu}_{i}$ the mean vector and $\boldsymbol{\Sigma}_{i}$ the covariance matrix of the fault $F_{i}$, we can monitor the fault $F_{i}$ with the following rule : if $p\left(F_{i}=\right.$ True $|\boldsymbol{x})<p\left(F_{i}=\right.$ True $)$ then the observation $\boldsymbol{x}$ can not be attribute to the fault $F_{i}$ (distance rejection for the fault $F_{i}$ ). For that, one can use the CGN of the figure 4 .
[Figure 4 about here.]
In the figure 4, we can see that a coefficient $c$ is implicated in the distance rejection. This coefficient is the root (non equal to 1) of the following equation:

$$
1-c+\frac{p c}{C L} \ln (c)=0
$$

where $p$ is the dimension of the system, and $C L$ is the control limit of the $T^{2}$ control chart. For a detailed demonstration of the equation 2, see appendix A. In numerous cases, $C L$ is equal to $\chi_{\alpha, p}^{2}$, the quantile to the $\alpha$ value of the $\chi^{2}$ distribution with $p$ degree of freedom (Montgomery (1997)). So, $\alpha$ allows tuning the distance rejection: the higher is $\alpha$, the stronger is the distance rejection.

### 3.2. Fault diagnosis with distance rejection in a Bayesian network

It is possible to combine a discriminant analysis and the distance rejection notion in a CGN. Indeed, we have the probabilities associated with the different

known faults (discriminant analysis), and we can know if a suspected observation can be attribute to none, one or several types of fault (distance rejection on each type of fault). The figure 5 presents the CGN proposed for the fault diagnosis with integration of distance rejection.
[Figure 5 about here.]

In the previous section, we have already detailed the different conditional probabilities tables of nodes $\boldsymbol{X}$. We will study the other conditional probabilities tables implicated in the figure 5 .

Firstly, we can see that a node has been added: the node " $D$ ", as Diagnosis. This node represents the final decision concerning the suspected observation. This node has $k+1$ modalities one for each existing fault $\left(F_{i}\right)$ and one for a New type of Fault $N F$. The a priori probabilities table of this node is fixed in order to not advantage any modality. As we can see on the table 3, each modality has the same a priori probability : $\frac{1}{k+1}$.
[Table 3 about here.]

Each node $F_{i}$ has the conditional probabilities table of the table 4 . We have set the different probabilities in order to respect the following rules :

- if $D=F_{i}$, then it is certain that the observation is from fault $F_{i}$,
- if $D=N F$, then it is certain that the observation is not from fault $F_{i}$,
- if $D=F_{j}$, then it is certain that the observation is not from fault $F_{i}$.
[Table 4 about here.]

The table 5 presents the conditional probabilities table of the node $D A$. We can see that the knowledge of a fault $F_{i}$ at the node $D$ allows to set the knowledge of the node $D A$, expressed by $P\left(D A=F_{i} \mid D=F_{i}\right)=1$. But, the knowledge on $D$ of a new type of fault $N F$ do not give any information for the discrimination between the different faults $F_{i}$ of the node $D A$, so we fix the $P\left(D A=F_{i} \mid D=N F\right)=\frac{1}{k}$ for each fault $F_{i}$.

[Table 5 about here.]

The interest of the Diagnosis node $D$ is to add the different results of distance rejection to the result of the discriminant analysis. The application of the network of the figure 5 to the bivariate example gives the figure 6. On this simple example, we well see that the classification space has a new area corresponding to the space location of new type of fault $(N F)$.
[Figure 6 about here.]

Now, we will see an application of this approach on a benchmark problem: the Tennessee Eastman Process (figure 7).
[Figure 7 about here.]

# 4. Application to the TEP 

### 4.1. Presentation of the TEP

We have tested our approach on the Tennessee Eastman Process. The Tennessee Eastman Process (TEP) is a chemical process. It is not a real process but a simulation of a process that was created by the Eastman Chemical Company to provide a realistic industrial process in order to evaluate process control and monitoring methods. Article of Downs and Vogel (1993) entirely describes this process. Authors also give the Fortran code of the simulation of the process. Ricker (1996) has implemented the simulation on Matlab. The TEP is composed of five major operation units: a reactor, a condenser, a compressor, a stripper and a separator. Four gaseous reactant A, C, D, E and an inert B are fed to the reactor where the liquid products F, G and H are formed. This process has 12 input variables and 41 output variables. The TEP has 20 types of identified faults. So, this process is ideal to test monitoring methods. But, it is also a benchmark problem for control techniques because it is open-loop unstable. Many articles (authors) present the TEP and test their approaches on it. For example, in fault detection, we can cite Kano et al. (2002) and Kruger

et al. (2004). Some fault diagnosis techniques have also been tested on the TEP (Chiang et al. (2001, 2004); Kulkarni et al. (2005); Maurya et al. (2007)) with the plant-wide control structure recommended in Lyman and Georgakis (1995). In Chiang et al. (2004) and Kulkarni et al. (2005), authors focus on only 3 types of fault and give the datasets they used. For this reason, we will take the same data that in these articles and compare our approach to those of the others.

As we said, we have taken into account 3 types of faults: fault 4,9 and 11 (see table 6). These three types of fault are good representations of overlapping data and so, are not easy to classify. As indicated on the table 6, each type of fault is composed of 2 datasets: a training sample and a testing sample, containing respectively 480 and 800 observations. We precise that in the next part of this paper all computations have been made on Matlab with the BNT (BayesNet Toolbox) developed by Murphy (2001).
[Table 6 about here.]

# 4.2. Proposed approach without distance rejection 

In the first part of this application, we have applied the proposed approach without the integration of the distance rejection. In an objective evaluation purpose of our procedure and to compare it with the results of other published methods (like Support Vector Machines), we classified 2400 new observations ( 800 of each type of fault) of the TEP. The results are given in the table 7. For the Bayesian network (BN) approach, we compute the misclassification rate (percentage of observations which are not well classified). We are also giving the results of other methods on the same data. The results for the FDA (Fisher Discriminant Analysis), SVM (Support Vector Machines), PSVM (Proximal Support Vector Machines) and ISVM (Independent Support Vector Machines) methods are extracted from Chiang et al. (2004) and Kulkarni et al. (2005).
[Table 7 about here.]
On the table 7, we can observe that the BN approach outperforms all the others methods. The confusion matrix for the Bayesian network is given on

table 8 and gives us the possibility to see how the discrimination of the different faults is done. Each column of the matrix represents the instances in a predicted class, while each row represents the instances in an actual class. For example, for 800 tested observations of fault 4 , the diagnosis procedure gives 141 observations as the fault 11 , and 659 observations as the fault 4 , so $17.62 \%$ $(141 / 800)$ of misclassified observations for the fault 4 . Considering the three faults, the misclassification rate is $18.87 \%(\frac{28+66+141+218}{2400})$.
[Table 8 about here.]

# 4.3. Integration of distance rejection 

In this second part, the distance rejection is taken into account and we fix $\alpha$ to 0.001 for each known fault. The CGN has to classify 800 new observations of some characteristic faults of the TEP (namely Fault 7, 8, 10, 12, 13, and 14) for a total of $800 \times 6=4800$ new observations (new types of fault). The table 9 represents the confusion matrix for this case where the label NF means New type of Fault.
[Table 9 about here.]

The table 9 shows the results of the integration of the distance rejection in the Bayesian network. We can see that the discrimination of the three known faults is not really affected by this integration. Indeed, the misclassification rate for this 3 faults is $19.62 \%(\frac{654+580+695}{2400})$, instead of $18.87 \%$ previously (without the distance rejection). Moreover, this table shows correctly the advantage of this approach since 4352 observations on 4800 have been correctly classified as a new type of fault $N F$ (classification error rate of $9.33 \%$ ). In this case, an unsupervised classification tool as the k -mean algorithm would be able to identify the different classes of these observations. Finally, we can say that the proposed CGN allows to detect new types of fault (detection in more than $90 \%$ of the cases), without losing performances of discrimination between known faults (error rate of $18.87 \%$ has increased to $19.62 \%$ ). So, this CGN is able to take into account distance rejection with minor loss of perfomances.

# 5. Conclusions and Outlooks 

The main interest of this article is the presentation of a new method for the fault diagnosis of industrial processes. This method uses a faults database to construct a Conditional Gaussian Network. This CGN is able to discriminate between the different known faults of the system, but is also able to recognize some new types of fault on the system. The performances of this approach have been tested on a concrete example: the Tennessee Eastman Process. The results of the method are good and outperform some previous results of other published methods.

The evident outlook of the proposed approach is the extension to the Gaussian Models Mixture (GMM) (McLachlan and Basford (1988)) in order to take into account some non normal classes. Indeed, GMM can be easily modelized in a CGN for classification task. But, analytically, distance rejection of a GMM is a problem. This can be an interesting research field.

## A. Coefficient $c$ demonstration

This appendix presents the demonstration of the equation 2.
As in the case of the $T^{2}$ control chart Montgomery (1997), we will fix a threshold (Control Limit $C L$ for the control chart) on the a posteriori probabilities allowing to take decisions on the process: if, for a given observation $\boldsymbol{x}$, the a posteriori probability to be allocated to $F_{i}\left(P\left(F_{i} \mid \boldsymbol{x}\right)\right)$ is greater than the a priori probability to be allocated to $F_{i}\left(P\left(F_{i}\right)\right)$, then this observation is allocated to $F_{i}$. This rule can be rewritten as: $\boldsymbol{x} \in F_{i}$ if $P\left(F_{i} \mid \boldsymbol{x}\right)>P\left(F_{i}\right)$, or equivalently $\boldsymbol{x} \in \overline{F_{i}}$ if $P\left(\overline{F_{i}} \mid \boldsymbol{x}\right)<P\left(\overline{F_{i}}\right)$. The objective of the following developments is to define c in order to obtain the equivalence between the CGN and the multivariate $T^{2}$ control chart.

We want to keep the following decision rule:

$$
\boldsymbol{x} \in F_{i} \quad \text { if } \quad T^{2}<C L
$$

with this decision rule:

$$
\boldsymbol{x} \in F_{i} \quad \text { if } \quad P\left(F_{i} \mid \boldsymbol{x}\right)>P\left(F_{i}\right)
$$

We develop the second decision rule:

$$
\begin{aligned}
& P\left(F_{i} \mid \boldsymbol{x}\right)>P\left(F_{i}\right) \\
& P\left(F_{i} \mid \boldsymbol{x}\right)>\left(P\left(F_{i}\right)\right)\left(P\left(F_{i} \mid \boldsymbol{x}\right)+P\left(\overline{F_{i}} \mid \boldsymbol{x}\right)\right) \\
& P\left(F_{i} \mid \boldsymbol{x}\right)>P\left(F_{i}\right) P\left(F_{i} \mid \boldsymbol{x}\right)+P\left(F_{i}\right) P\left(\overline{F_{i}} \mid \boldsymbol{x}\right) \\
& P\left(F_{i} \mid \boldsymbol{x}\right)-P\left(F_{i}\right) P\left(F_{i} \mid \boldsymbol{x}\right)>P\left(F_{i}\right) P\left(\overline{F_{i}} \mid \boldsymbol{x}\right) \\
& P\left(F_{i} \mid \boldsymbol{x}\right)\left(1-P\left(F_{i}\right)>P\left(F_{i}\right) P\left(\overline{F_{i}} \mid \boldsymbol{x}\right)\right. \\
& P\left(F_{i} \mid \boldsymbol{x}\right) P\left(\overline{F_{i}}\right)>P\left(F_{i}\right) P\left(\overline{F_{i}} \mid \boldsymbol{x}\right) \\
& P\left(F_{i} \mid \boldsymbol{x}\right)>\frac{P\left(F_{i}\right)}{P\left(\overline{F_{i}}\right)} P\left(\overline{F_{i}} \mid \boldsymbol{x}\right)
\end{aligned}
$$

But, the Bayes law gives:

$$
P\left(F_{i} \mid \boldsymbol{x}\right)=\frac{P\left(F_{i}\right) P\left(\boldsymbol{x} \mid F_{i}\right)}{P(\boldsymbol{x})}
$$

and

$$
P\left(\overline{F_{i}} \mid \boldsymbol{x}\right)=\frac{P\left(\overline{F_{i}}\right) P\left(\boldsymbol{x} \mid \overline{F_{i}}\right)}{P(\boldsymbol{x})}
$$

So, we obtain:

$$
\begin{aligned}
\frac{P\left(F_{i}\right) P\left(\boldsymbol{x} \mid F_{i}\right)}{P(\boldsymbol{x})} & >\left(\frac{P\left(F_{i}\right)}{P\left(\overline{F_{i}}\right)}\right) \frac{P\left(\overline{F_{i}}\right) P\left(\boldsymbol{x} \mid \overline{F_{i}}\right)}{P(\boldsymbol{x})} \\
\left(\frac{P\left(F_{i}\right)}{P\left(\overline{F_{i}}\right)}\right) P\left(\boldsymbol{x} \mid F_{i}\right) & >\left(\frac{P\left(F_{i}\right)}{P\left(\overline{F_{i}}\right)}\right) P\left(\boldsymbol{x} \mid \overline{F_{i}}\right) \\
P\left(\boldsymbol{x} \mid F_{i}\right) & >P\left(\boldsymbol{x} \mid \overline{F_{i}}\right)
\end{aligned}
$$

In the case of a discriminant analysis with $k$ classes $C_{i}$, the conditional probabilities are computed with the following equation 8 , where $\phi$ represents the probability density function of the multivariate Gaussian distribution of the class.

$$
P\left(\boldsymbol{x} \mid C_{i}\right)=\frac{\phi\left(\boldsymbol{x} \mid C_{i}\right)}{\sum_{j=1}^{k} P\left(C_{j}\right) \phi\left(\boldsymbol{x} \mid C_{j}\right)}
$$

So, equation 7 can be written as:

$$
\phi\left(\boldsymbol{x} \mid F_{i}\right)>\phi\left(\boldsymbol{x} \mid \overline{F_{i}}\right)
$$

We recall that the probability density function of a multivariate Gaussian distribution of dimension $p$, of parameters $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$, of an observation $\boldsymbol{x}$ is given by:

$$
\phi(\boldsymbol{x})=\frac{e^{-\frac{1}{2}(\boldsymbol{x}-\boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu})}}{(2 \pi)^{p / 2}|\boldsymbol{\Sigma}|^{1 / 2}}
$$

If the law parameters are $\boldsymbol{\mu}$ and $c \times \boldsymbol{\Sigma}$, then the density function becomes:

$$
\phi(\boldsymbol{x})=\frac{e^{-\frac{1}{2 c}(\boldsymbol{x}-\boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu})}}{(2 \pi)^{p / 2}|\boldsymbol{\Sigma}|^{1 / 2} c^{p / 2}}
$$

In identifying the expression $(\boldsymbol{x}-\boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu})$ as the $T^{2}$ of the observation $\boldsymbol{x}$, we can write:

$$
\begin{aligned}
\phi\left(\boldsymbol{x} \mid F_{i}\right) & >\phi\left(\boldsymbol{x} \mid \overline{F_{i}}\right) \\
\frac{e^{-\frac{T^{2}}{2}}}{(2 \pi)^{p / 2}|\boldsymbol{\Sigma}|^{1 / 2}} & >\frac{e^{-\frac{T^{2}}{2 c}}}{(2 \pi)^{p / 2}|\boldsymbol{\Sigma}|^{1 / 2} c^{p / 2}} \\
e^{-\frac{T^{2}}{2}} & >\frac{e^{-\frac{T^{2}}{2 c}}}{c^{p / 2}} \\
-\frac{T^{2}}{2} & >-\frac{T^{2}}{2 c}-\frac{p \ln (c)}{2} \\
T^{2} & <\frac{T^{2}}{c}+p \ln (c) \\
T^{2} & <\frac{p \ln (c)}{1-\frac{1}{c}}
\end{aligned}
$$

However, we search the value(s) of $c$ allowing the equivalence with the control chart decision rule: $\boldsymbol{x} \in F_{i} \quad$ if $\quad T^{2}<C L$. So, we obtain the following equation for $c$ :

$$
\frac{p \ln (c)}{1-\frac{1}{c}}=L C
$$

Or, equivalently:

$$
1-c+\frac{p c}{L C} \ln (c)=0
$$

# List of Figures 

1 Bivariate system with three different known faults ..... 20
2 Conditional Gaussian Network equivalent to a discriminant analysis ..... 21
3 Classification areas of the bivariate system ..... 22
4 Distance rejection of fault $F_{i}$ ..... 23
5 Fault diagnosis with distance rejection in a Bayesian network ..... 24
6 Fault diagnosis with distance rejection for the bivariate example ..... 25
7 Process flowsheet of the TEP ..... 26

![img-0.jpeg](img-0.jpeg)

Figure 1: Bivariate system with three different known faults

![img-1.jpeg](img-1.jpeg)

Figure 2: Conditional Gaussian Network equivalent to a discriminant analysis

![img-2.jpeg](img-2.jpeg)

Figure 3: Classification areas of the bivariate system

![img-3.jpeg](img-3.jpeg)

Figure 4: Distance rejection of fault $F_{i}$

![img-4.jpeg](img-4.jpeg)

Figure 5: Fault diagnosis with distance rejection in a Bayesian network

![img-5.jpeg](img-5.jpeg)

Figure 6: Fault diagnosis with distance rejection for the bivariate example

![img-6.jpeg](img-6.jpeg)

Figure 7: Process flowsheet of the TEP

# List of Tables 

1 CPT of a discrete node with discrete parents ..... 28
2 CPT of a Gaussian node with discrete parents ..... 29
3 A priori probabilities table of the node $D$ ..... 30
4 Conditional probabilities table of nodes $F_{i}$ ..... 31
5 Conditional probabilities table of the node $D A$ ..... 32
6 Description of fault datasets ..... 33
7 Misclassification rate of the different methods ..... 34
8 Confusion matrix of BN ..... 35
9 Confusion matrix of CGN with distance rejection ..... 36


Table 1: CPT of a discrete node with discrete parents


Table 2: CPT of a Gaussian node with discrete parents


Table 3: A priori probabilities table of the node $D$


Table 4: Conditional probabilities table of nodes $F_{i}$


Table 5: Conditional probabilities table of the node $D A$


Table 6: Description of fault datasets


Table 7: Misclassification rate of the different methods


Table 8: Confusion matrix of BN


Table 9: Confusion matrix of CGN with distance rejection