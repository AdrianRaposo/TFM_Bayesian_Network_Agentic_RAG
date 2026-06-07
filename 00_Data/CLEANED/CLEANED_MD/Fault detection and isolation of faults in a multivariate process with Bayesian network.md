# Fault detection and isolation of faults in a multivariate process with Bayesian network 

Sylvain Verron, Jing Li, Teodor Tiplica

## To cite this version:

Sylvain Verron, Jing Li, Teodor Tiplica. Fault detection and isolation of faults in a multivariate process with Bayesian network. Journal of Process Control, 2010, 20 (8), pp.902-911. 10.1016/j.jprocont.2010.06.001 . hal-00516993

## HAL Id: hal-00516993 <br> https://hal.science/hal-00516993v1

Submitted on 13 Sep 2010

HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from teaching and research institutions in France or abroad, or from public or private research centers.

L'archive ouverte pluridisciplinaire HAL, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant des établissements d'enseignement et de recherche français ou étrangers, des laboratoires publics ou privés.

# Identification of faults in a multivariate process with Bayesian network 

Sylvain Verron ${ }^{a, a}$, Jing $\mathrm{Li}^{\text {b }}$, Teodor Tiplica ${ }^{a}$<br>${ }^{a}$ LASQUO/ISTIA<br>University of Angers<br>62, Avenue Notre Dame du Lac<br>49000 Angers, France<br>${ }^{b}$ School of Computing, Informatics and Decision Systems Engineering<br>Arizona State University<br>Tempe, AZ 85287-5906


#### Abstract

The main objective of this paper is to present a new method of detection and diagnosis with a Bayesian network. For that, a combination of two original works is made. The first one is the work of Li et al. [1] who proposed a causal decomposition of the $T^{2}$ statistic. The second one is a previous work on the detection of fault with Bayesian networks [2], notably on the modeling of multivariate control charts in a Bayesian network. Thus, in the context of multivariate processes, we propose an original network structure allowing to decide if a fault has appeared in the process. This structure permits the identification of the variables responsible (root causes) of the fault. A particular interest of the method is the fact that the detection and the identification can be made with a unique tool: a Bayesian network.


Key words: Multivariate SPC, $T^{2}$ decomposition, Bayesian network

## 1. Introduction

Nowadays, monitoring of complex manufacturing systems is becoming an essential task in order to: insure a safety production (for humans and materials), reduce the variability of products or reduce manufacturing costs. Classically, in the literature, three types of approaches can be found for the process monitoring $[3,4]$ : the knowledge-based approach, the model-based approach and the datadriven approach. The knowledge-based category represents methods based on qualitative models (FMECA - Failures Modes Effects and Critically Analysis; Fault Trees; Risk Analysis) [5, 6]. The model-based techniques are based on

[^0]
[^0]:    ${ }^{\text {a }}$ Corresponding author. Tel.: 00332412265 33; fax: 0033241226521
    Email address: sylvain.verron@univ-angers.fr (Sylvain Verron)

analytical (physical) models of the system and are enable to simulate the system [7]. Though, at each instant, the theoretical value of each sensor can be known for the normal operating state of the system. As a consequence, it is relatively easy to see if the real process values are similar to the theoretical values. But, the major drawback of this family of techniques is that a detailed model of the process is required in order to monitor it efficiently. An effective detailed model can be very difficult, time consuming and expensive to obtain, particularly for large-scale systems with many variables. The data-driven approaches are a family of different techniques based on the analysis of the real data extracted from the process. These methods are based on rigorous statistical developments of the process data (i.e. control charts, methods based on Principal Component Analysis, Projection to Latent Structure or Discriminant Analysis) [3]. In the case we develop (monitoring of large multivariate processes), we will work in the data-driven monitoring framework.

To achieve this activity of data-driven monitoring, some authors call this AEM (Abnormal Event Management) [4]. This is composed of three principal steps: firstly, a timely detection of an abnormal event; secondly, diagnosing its causal origins (or root causes); and finally, taking appropriate decisions and actions to return the process in a normal working state. As the third step is specific to each process, literature generally focuses on the two first step: fault detection, and fault diagnosis. In the literature, those approaches are named FDD (Fault Detection and Diagnosis) [8]. We will call "fault" an abnormal event, it is classically defined as a departure from an acceptable range of an observed variable or a calculated parameter of the process [4]. So, a fault can be viewed as a process abnormality or symptom, like an excessive pressure in a reactor, or a low quality of a part of a product, and so on. Generally, a monitoring technique is dedicated to one specific step: detection or diagnosis. In the literature, one can find a lot of data-driven techniques for the fault detection: univariate statistical process control (Shewhart charts) [9, 10], multivariate statistical process control ( $T^{2}$ and Q charts) [11, 12], and some PCA (Principal Component Analysis) based techniques [13] like Multiway PCA or Moving PCA [14] used for the detection step. Kano et al. [15] make comparisons between these different techniques.

In the data-driven fault diagnosis, the diagnosis procedure can be seen as a classification task. Indeed, today's processes give many measurements. These measurements can be stored in a database when the process is in fault-free case, but also in the case of identified fault. Assuming that the number of types of fault (classes) and that the belonging class of each observation is in the database (learning sample), the fault diagnosis can be viewed as a supervised classification task whose objective is to class new observations to one of the existing classes. For example, figure 1 give the learning sample of a bivariate system with three different known faults. One can easily use supervised classification to classify new faulty observations. In this case, supervised classification will separate the bidimensional space into three parts (one for each type of fault), as illustrated in the figure 2. A new faulty observation (i.e. point A in figure 2) will be classified corresponding to his location in the bidimensional space.

![img-0.jpeg](img-0.jpeg)

Figure 1: Bivariate system with three different known faults
![img-1.jpeg](img-1.jpeg)

Figure 2: Classification areas for the bivariate system

Many supervised classifiers have been developed, we can cite Fisher Discriminant Analysis [16], Support Vector Machine [17], k-nearest neighborhood [18], Artificial Neural Networks [16] and Bayesian classifiers [19]. But, it seems important to highlight that in the case of non-informative (insignificant) variables, the performances (in term of classification error rate) of these classifiers decrease as the number of non-informative variables increases. Therefore a selection of the informative variables (feature selection) for the classification task should be done in order to increase the accuracy of the classification [20, 21].

As we mentioned previously, an objective of a fault diagnosis method is to classify new observations to one of the existing classes. But, in certain cases, the observation may be a new type of fault (unknown or unseen before). This is the case when the observation is distant of any known classes of fault (example of the point A in figure 2). In order to detect these new types of fault, an interesting improvement of the fault diagnosis with classifiers is the application of a criterion called distance rejection (see [22, 23]). The application of this

criterion allows to reduce the classification areas of each known fault and to introduce a classification area for new type of fault (see figure 3).
![img-2.jpeg](img-2.jpeg)

Figure 3: Classification areas with distance rejection for the bivariate example

On figure 3, we can see that point A is well classified as a new type of fault (NF). So, this method is a very useful addition to the classification techniques. But, in the case of a new type of fault, no information is given concerning the fault. On the same way, in the beginning of the process, the fault database is empty and classification techniques cannot be used. So, in this second case also, no information about the fault is given.

In these two cases, an efficient Fault Detection and Diagnosis tool should be able to identify the variables implicated in the fault, in order to help the process supervisor to identify the root cause (the physical cause) of the fault. Some methods exists to solve this problem (see section 3), which are based on a decomposition of the $T^{2}$ statistic. But, each of these methods uses different tools for the fault detection and the fault identification (variables implicated in the fault), like control charts, statistical decompositions, Bayesian networks, etc. It will be more interesting to obtain all these techniques solely in one tool. The objective of this article is to propose an improvement to the decomposition method of Li et al. [1], in order to use a sole Bayesian network enable to detect a fault and to identify the implicated variables in this fault.

The article is structured as follows: section 2 highlights some aspects on Bayesian networks and particularly on Bayesian network classifiers; section 3 presents the various $T^{2}$ decompositions (causal and MYT); in the section 4 we are reminding how to model some multivariate control charts in a Bayesian network, and we present how to obtain detection and identification of faults in a sole Bayesian network; an example of the approach is given on a simple process in the section 5; in the last section, we conclude on the proposed approach and give some outlooks.

# 2. Bayesian networks 

### 2.1. Definition

A Bayesian Network (BN) [24, 25] is an acyclic graph where each variable is a node (that can be continuous or discrete). Edges of the graph represent dependence between linked nodes. A formal definition is given here:

A Bayesian network is a triplet $\{\mathbf{G}, \mathbf{E}, \mathbf{D}\}$ where:
$\{\mathbf{G}\}$ is a directed acyclic graph, $\mathbf{G}=(V, A)$, with $V$ the ensemble of nodes of $\mathbf{G}$, and $A$ the ensemble of edges of $\mathbf{G}$,
$\{\mathbf{E}\}$ is a finite probabilistic space $(\Omega, Z, p)$, with $\Omega$ a non-empty space, $Z$ a collection of subspace of $\Omega$, and $p$ a probability measure on $Z$ with $p(\Omega)=$ 1 ,
$\{\mathbf{D}\}$ is an ensemble of random variables associated to the nodes of $\mathbf{G}$ and defined on $\mathbf{E}$ such as:

$$
p\left(V_{1}, V_{2}, \ldots, V_{n}\right)=\prod_{i=1}^{n} p\left(V_{i} \mid C\left(V_{i}\right)\right)
$$

with $C\left(V_{i}\right)$ the ensemble of causes (parents) of $V_{i}$ in the graph $\mathbf{G}$.

### 2.2. Dependences in Bayesian network

Theorically, variables $X_{1}, X_{2}, \ldots, X_{n}$ can be discrete or continuous. But, in practice, for exact computation, only the discrete and the Gaussian case can be treated. Such a network is often called Conditional Gaussian Network (CGN). In this context, to ensure availability of exact computation methods, discrete variables are not allowed to have continuous parents [26, 27].

Practically, the conditional probability distribution is described for each node by his Conditional Probability Table (CPT). In a CGN, three cases of CPT can be found. The first one is for a discrete variable with discrete parents. By example, we take the case of two discrete variables $A$ and $B$ of respective dimensions $a$ and $b$ (with $a_{1}, a_{2}, \ldots, a_{a}$ the different modalities of $A$, and $b_{1}, b_{2}, \ldots, b_{b}$ the different modalities of $B$ ). If $A$ is parent of $B$, then the CPT of $B$ is represented in table 1 .


Table 1: CPT of a discrete node with discrete parents
We can see that the utility of the CPT is to condense the information about the relations of $B$ with his parents. We can denote that the dimension of this

CPT is $a \times b$. In general the dimension of the CPT of a discrete node (dimension $x)$ with $p$ parents (discrete) $Y_{1}, Y_{2}, \ldots, Y_{p}$ (dimension $y_{1}, y_{2}, \ldots, y_{p}$ ) is $x \prod_{i=1}^{p} y_{i}$.

The second case of CPT is for a continuous variable with discrete parents. Assuming that $B$ is a Gaussian variable, and that $A$ is a discrete parent of $B$ with $a$ modalities, the CPT of $B$ can be represented as in the table 2 where $P\left(B \mid a_{1}\right) \sim \mathcal{N}\left(\mu_{a_{1}}, \Sigma_{a_{1}}\right)$ indicates that $B$ conditioned to $A=a_{i}$ follows a multivariate normal density function with parameters $\mu_{a_{i}}$ and $\Sigma_{a_{i}}$. If we have more than one discrete parent, the CPT of $B$ will be composed of $\prod_{i=1}^{p} y_{i}$ Gaussian distribution where $y_{i}$ represents the respective number of modalities of the parent nodes $Y_{1}, Y_{2}, \ldots, Y_{p}$.


Table 2: CPT of a Gaussian node with discrete parents
The third case is when a continuous node $B$ has a continuous parent $A$. In this case, we obtain a linear regression and we can write, for a fixed value $a$ of $A$, that $B$ follows a Gaussian distribution $P(B \mid A=a) \sim \mathcal{N}\left(\mu_{B}+\beta \times a ; \Sigma_{B}\right)$ where $\beta$ is the regression coefficient. Evidently, the three different cases of CPT enumerated can be combined for different cases where a continuous variable has several discrete parents and several continuous (Gaussian) parents.

The classical use of a Bayesian network (or Conditional Gaussian Network) is to enter evidence in the network (an evidence is the observation of the values of a set of variables). Thus, the information given by the evidence is propagated in the network in order to update the knowledge and obtain a posteriori probabilities on the non-observed variables. This propagation mechanism is called inference. As its name suggests, in a Bayesian network, the inference is based on the Bayes rule. Many inference algorithms (exact or approximate) have been developed, but one of the more exploited is the junction tree algorithm [28].

# 2.3. Bayesian classifiers 

Bayesian network classifiers are particular BN [19]. They always have a discrete node $C$ coding the $k$ different classes of the system. Thus, other variables $X_{1}, \ldots, X_{p}$ represent the $p$ descriptors (variables) of the system.

A famous Bayesian classifier is the Naïve Bayesian Network (NBN), also named Bayes classifier [29]. This Bayesian classifier makes the strong assumption that the descriptors of the system are class conditionally independent. Assuming the hypothesis of normality of each descriptor, the NBN is equivalent to the classification rule of the diagonal quadratic discriminant analysis. But, in

practice, this assumption of independence and non correlated variables is not realistic. In order to deal with correlated variables, several approaches have been developed. We can cite the Tree Augmented Naïve Bayesian networks (TAN) [19]. These BNs are based on a NBN but a tree is added between the descriptors. An other interesting approach is the Kononenko one [30], which represent some variables in one node. As in [31] the assumption we will make is that this variable follows a normal multivariate distribution (conditionally to the class) and we will refer to this kind of BN as Condensed Semi Naïve Bayesian Network (CSNBN).
![img-3.jpeg](img-3.jpeg)

Figure 4: Different bayesian network classifiers: NBN (a), TAN (b) and CSNBN (c).

# 3. Existent methods for identification 

### 3.1. The MYT decomposition

As we previously said, a method for the fault detection in multivariate processes is the $T^{2}$ control chart. However, this chart do not give any information about the diagnosis of the out-of-control situation. For that, many techniques have been proposed in the literature [32, 33]. An interesting decomposition of the $T^{2}$ has been proposed by Mason, Young and Tracy [32], namely MYT decomposition. More, in order to better understand this method, authors give an example for a bivariate process. One can precise that the authors have proved that several methods can be considered like special cases of MYT decomposition [32]. The principle of this method is to decompose the $T^{2}$ statistic in a limited number of orthogonal components which are also statistical distances (and so, can be monitored). This decomposition is the following:

$$
T^{2}=T_{1}^{2}+T_{2 \bullet 1}^{2}+T_{3 \bullet 1,2}^{2}+T_{4 \bullet 1,2,3}^{2}+\cdots+T_{p \bullet 1,2,3 \cdots p-1}^{2}
$$

where $T_{i \bullet j, k}^{2}$ represents the $T^{2}$ statistic of the regression of the variables $X_{j}$ and $X_{k}$ on the variable $X_{i}$. We remark that it exists a large number of different decompositions $(p!)$ and so, it exists a large number of different terms $\left(p \times 2^{p-1}\right)$. In order to better understand, on a process with three variables, the different decompositions available are:

$$
\begin{aligned}
& T^{2}=T_{1}^{2}+T_{2 \bullet 1}^{2}+T_{3 \bullet 1,2}^{2} \\
& T^{2}=T_{1}^{2}+T_{2 \bullet 1}^{2}+T_{2 \bullet 1,3}^{2} \\
& T^{2}=T_{2}^{2}+T_{1 \bullet 2}^{2}+T_{3 \bullet 1,2}^{2} \\
& T^{2}=T_{2}^{2}+T_{2 \bullet 2}^{2}+T_{1 \bullet 2,3}^{2} \\
& T^{2}=T_{3}^{2}+T_{1 \bullet 3}^{2}+T_{2 \bullet 1,3}^{2} \\
& T^{2}=T_{3}^{2}+T_{2 \bullet 3}^{2}+T_{1 \bullet 2,3}^{2}
\end{aligned}
$$

The computation of the different terms is not detailed in this article, but we report the readers to the works of Mason et al. [32]. We can note that the terms $T_{j}^{2}$ are called non conditional terms and that the other terms are called conditional terms. Each terms follows a Fisher distribution law:

$$
T_{j+1 \bullet 1, \cdots j}^{2}=\frac{(m+1)(m-1)}{m(m-k-1)} F_{1, m-k-1}
$$

where $k$ is the number of conditioned factors. We can simplify this equation for the non conditional terms $(k=0)$ by:

$$
T_{j}^{2} \sim \frac{m+1}{m} F_{1, m-1}
$$

This monitoring allows to detect a problem on each term of the decomposition. For example, if we see that the term $T_{2 \bullet 1}^{2}$ is responsible of the out-of-control of the process, we can immediately search a root cause on a tuning of the process touching to the correlation between these two variables. But for a more simple computation, one can use a $T^{2}$ control chart for the detection of the fault,

and in the case of a detected fault we can apply the MYT decomposition. The analysis of the different terms is made in levels order: (firstly $T_{1}^{2}, T_{2}^{2}, T_{3}^{2}$, then $T_{2 \bullet 1}^{2}, T_{2 \bullet 1}^{2}, T_{1 \bullet 2}^{2}, T_{2 \bullet 2}^{2}, T_{1 \bullet 3}^{2}, T_{2 \bullet 3}^{2}$ and finally $T_{3 \bullet 1,2}^{2}, T_{2 \bullet 1,3}^{2}, T_{1 \bullet 2,3}^{2}$ ) until that one find the term responsible of the detection on the $T^{2}$ control chart.

The main advantage of the MYT decomposition is the fact that this method can give a diagnosis of the situation without any samples of previous faults. An other advantage is the fact that this method is based on the same statistics tools that the $T^{2}$ control chart.

# 3.2. The causation-based $T^{2}$ decomposition 

The MYT method is very interesting, but it has a major drawback: the number of term to compute. Indeed, as we previously said, the number of terms to compute is equal to $p \times 2^{p-1}$. For example, for a process with 20 variables, more than 10 millions of terms are needed to compute. A five steps algorithm has been proposed by Mason et al. [34] in order to reduce the number of terms to compute. But, Li et al. [1] said that the number of terms is always too large. So, they propose a new method using a Bayesian network: the causation-based $T^{2}$ decomposition. A causal graph modeling the process allows to reduce the number of terms to compute to only $p$. More than the decrease of computation giving by this method, the authors show that one obtain equally an increase of the performances. The basis assumption of the method proposed by Li et al. [1] is that the process can modelized with a causal Bayesian network where each variable of the process is a Gaussian univariate variable. If a Bayesian network represents solely some Gaussian continuous variables, it is also called linear Gaussian model. So, for a process with 3 variables, we can obtain, for example, the network of the figure 5 .
![img-4.jpeg](img-4.jpeg)

Figure 5: Example of a linear gaussian model
Concerning the modeling of the process by a linear Gaussian model, the authors make the distinction between two types of decomposition MYT: "for a given decomposition of the $T^{2}$, if it exists a term $T_{\imath \bullet 1, \ldots, i-1}^{2}$ such the ensemble of the variable $\left\{X_{1}, \ldots, X_{i-1}\right\}$ includes at least one descendant of $X_{i}$, then this decomposition is a type A decomposition, if not, the decomposition is a type B decomposition". So, we can sort in the table 3 the different decompositions of the process with 3 variables of the figure 5 .


Table 3: Decomposition types for the three variables process

Li et al. [1] proved, basing on the Hawkins works [33], that the type A decompositions allow a less accurate diagnosis than the type B decompositions. More, they proved that in the context of linear Gaussian models, all the type B decompositions converge to a sole decomposition that the authors named "causation-based $T^{2}$ decomposition". Indeed, each type B decomposition converge to the causal decomposition of the $T^{2}$ given in equation 6 , where $P A\left(X_{i}\right)$ represents the parents of the variable $X_{i}$ in the causal graph.

$$
T^{2}=\sum_{i=1}^{6} T_{i \bullet P A\left(X_{i}\right)}^{2}
$$

So, the causation-based $T^{2}$ decomposition of the example of the figure 5 is the following: $T^{2}=T_{1}^{2}+T_{2 \bullet 1}^{2}+T_{3 \bullet 1}^{2}$.

After that, the authors give the procedure of detection and identification of fault using the new causal decomposition. Firstly, a linear Gaussian Bayesian network is constructed in order to represent the different causal relations between the process variables. Secondly, the process is monitored with a $T^{2}$ control chart. In the case of an out-of-control situation, the $T^{2}$ is decomposed by the causation-based $T^{2}$ decomposition of the equation 6 . In this equation, each $T_{i \bullet P A\left(X_{i}\right)}^{2}$ is independent and, in the case of known parameters, follows a $\chi^{2}$ distribution law with one degree of freedom. So, each $T_{i \bullet P A\left(X_{i}\right)}^{2}$ can be compared to the limit $\chi_{1, \alpha}^{2}$, which is the quantile at the value $\alpha$ ( $\alpha$ is the false alarm rate) of the $\chi^{2}$ distribution with one degree of freedom. A significant term $T_{i \bullet P A\left(X_{i}\right)}^{2}$ (higher than the limit) gives that the variable $X_{i}$ has been implicated in the fault. The figure 6 represents the process monitoring diagram with the given method.

The approach developed by Li et al. [1] exploits some threshold given by quantiles of statistical laws. This method allows to considerably increase the performances compared to the MYT method, with less computation resource. But, we can view on figure 6 that several tools are used for this technique: control chart, Bayesian network, statistical computations. We will show, in the next section, that the monitoring of a multivariate process by the method of the causal-based $T^{2}$ decomposition can entirely be realized in a sole Bayesian network.

![img-5.jpeg](img-5.jpeg)

Figure 6: The process monitoring diagram using causation-based $T^{2}$ decomposition

# 4. The proposed approach 

### 4.1. Control charts with bayesian network

In previous works [2], we have demonstrated that a $T^{2}$ control chart [11] could be modelized with a Bayesian network. For that, we use two nodes: a Gaussian multivariate node $\boldsymbol{X}$ representing the data and a bimodal node $E$ representing the state of the process. The bimodal node $E$ has the following modalities: $I C$ for "in control" and $O C$ for "out-of-control". Assuming that $\boldsymbol{\mu}$ and $\boldsymbol{\Sigma}$ are respectively the mean vector and the variance-covariance matrix of the process, we can monitor the process with the following rule: if $P(I C \mid \boldsymbol{x})<P(I C)$ then the process is out-of-control. This Bayesian network is represented on the figure 7 , where the conditional probabilities tables for each node are given.
![img-6.jpeg](img-6.jpeg)

Figure 7: $T^{2}$ control chart in a Bayesian network

On this figure 7, we can observe that a coefficient $c$ is implicated in the modeling of the control chart by Bayesian network. This coefficient is the root (different of 1) of the following equation:

$$
1-c+\frac{p c}{C L} \ln (c)=0
$$

where $p$ is the dimension (number of variables) of the system to monitor, and $C L$ is the control limit of the equivalent $T^{2}$ control chart. The demonstration of the computation of $c$ is given in appendix A. In numerous cases, $C L$ is equal to $\chi_{\alpha, p}^{2}$, the quantile at the value $\alpha$ of the distribution of the $\chi^{2}$ with $p$ degree of freedom [10]. So, $\alpha$ allows to tune the false alarm rate of the control chart.

# 4.2. Improvement of the causal decomposition 

The method proposed by Li et al. [1] allows, based on a Bayesian network, to know the different terms of the MYT decomposition to compute. For the computation of the different terms of the causation-based $T^{2}$ decomposition, and for the associated decisions (use of the threshold), the authors do not use the network in an optimal way. Indeed, they use a $T^{2}$ control chart out of the network, but this chart can be modelized directly in the network (see previous section). More, the authors compute each $T_{i \bullet P A\left(X_{i}\right)}^{2}$ out of the network, but it is possible to make all the computations in the network.

We propose an extension to the method of Li et al. [1] allowing the computation of the different $T_{i \bullet P A\left(X_{i}\right)}^{2}$ and the decisions associated to each one. The diagnosis with the causation-based $T^{2}$ decomposition, like the MYT decomposition, is a monitoring of regressed variables, with the use of univariate control charts. In the previous section, we have demonstrated how to model, in a Bayesian network, a multivariate control chart like the $T^{2}$ control chart. But, a univariate control chart like a Shewhart control chart is simply a particular case of a multivariate control chart like the $T^{2}$ control chart. Indeed, the computation of the $T^{2}$ is the following:

$$
T^{2}=(\boldsymbol{x}-\boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1}(\boldsymbol{x}-\boldsymbol{\mu})
$$

But, in the univariate case, $\boldsymbol{x}=x, \boldsymbol{\mu}=\mu$ and $\boldsymbol{\Sigma}=\sigma^{2}$. So, the previous equation gives:

$$
T^{2}=\frac{(x-\mu)^{2}}{\sigma^{2}}
$$

In this univariate case, the $T^{2}$ statistic follows a $\chi^{2}$ distribution law with one degree of freedom. So, it is possible to improve the method developed by Li et al. [1]. We propose to monitor directly the different values of the $T_{i \bullet P A\left(X_{i}\right)}^{2}$ in the Bayesian network. For that, we add a bimodal variable to each univariate node of the Bayesian network. If we have a graph representing a system with three variables (see figure 5), we then obtain a network with six nodes: 3 continuous (Gaussian univariate) and 3 discrete (bimodal), like shown on figure 8.

![img-7.jpeg](img-7.jpeg)

Figure 8: Improvement of the causal decomposition

We precise here that the continuous variables are not needed to be standardized before. The discrete nodes added to the initial structure of the network allow directly to identify the responsible (root-cause) variables in an out-ofcontrol situation. These nodes modelize a control chart $T_{i \bullet P A\left(X_{i}\right)}^{2}$ allowing to conclude on the state of each variable of the process. We recall that the modality $I C$ of a discrete node signify in control, and that the modality $O C$ signify out-of-control. The figure 9 gives the different probabilities tables associated to the different nodes (discrete or continuous).
![img-8.jpeg](img-8.jpeg)

Figure 9: Bayesian network part

When a fault is detected in the process, each discrete node (representing the status of a regressed variable) give a certain probability that the variable is in control. The responsible variables are ones with an a posteriori probability lower than the a priori probability. The operator can then easily search for the root cause (the physical cause) because he knows which variables are responsible of the out-of-control status. To the view of all our statements, we can propose a Bayesian network able to determine if the process is in or out-of-control (detection). In the case of a out-of-control situation, this Bayesian network can also gives the implicated variables (identification). The figure 10 presents the form of the Bayesian network for the process with 3 variables. This sole network is able to do all the steps of the diagram of the Li et al. method (figure 6).

![img-9.jpeg](img-9.jpeg)

Figure 10: Bayesian network for the detection and the identification

# 5. Application 

In order to better understand the proposed method and his ability in monitoring, a case study is proposed: a hot forming process.

### 5.1. The hot forming process

A twodimensional physical illustration of the hot forming process is given in figure 11 .
![img-10.jpeg](img-10.jpeg)

Figure 11: Hot forming process
The hot forming process has 5 variables: one quality variable (X5: final dimension of workpiece) and four process variables (X1, temperature; X2, material flow stress; X3, tension in workpiece; and X4, blank holding force, or

BHF). The causal Bayesian network modelisation of this process is given on figure 12. Because the material flow stress (X2) and the tension in a workpiece (X3) directly affect the final workpiece dimension (X5), where "directly" means that the causal influences are not mediated through other variables, X2 and X3 are connected to X5 by directed arcs. The BHF (X4) also affects the dimension of the workpiece (X5), but only indirectly, i.e., through the tension in the workpiece (X3). Thus, there is no directed arc between X4 and X5. Similar interpretations can be applied to the causal relationships between other variables.
![img-11.jpeg](img-11.jpeg)

Figure 12: Causal network of the Hot forming process

From the causal network of the figure 12, we apply the proposed method and we can construct the Bayesian network of the figure 13.
![img-12.jpeg](img-12.jpeg)

Figure 13: Bayesian network for the Fault Detection and Identification of the hot forming process

# 5.2. Simulations and results 

Because this system has five variables, there are five potential single-fault scenarios, each with only one variable having a mean shift, and 26 potential multiple-fault scenarios, each with more than one variable having mean shifts.

A total of 31 fault scenarios are shown in the table 4 , where a $\delta$ denotes the magnitude of the mean shift in the unit of standard deviation.

For a given scenario, we have simulated 1000 normal (free-fault) observations in order to learn the parameters of the network. Once the parameters learnt, we have simulated 5000 observations of the scenario with a magnitude of $3(\delta=3)$. The 5000 observations are given to the Bayesian network. This network gives us the probability that the process is out-of-control, and in the case of an out-of-control, it gives also the probability for each variable to be responsible of the out-of-control situation. We have taken a global false alarm rate of $5 \%$ (for detection), and a local false alarm rate of $1 \%$ (for identification). For each discrete node, the a priori probability has been set to 0.5 . So, for each discrete variable, a probability to be out-of-control greater than 0.5 signifies that an out-of-control situation is detected or identified. For each scenario, we give the detection rate and the diagnosis rate (see table 4). The detection rate is the number of detected observation of the 5000 out-of-control observations, expressed in percent. The diagnosis rate is the number of well-diagnosed observations of the detected observation, also expressed in percent.


Table 4: Fault scenarios description

In the table 4, we can see that for each multiple-fault scenarios (6 to 31) the detection rate is really good. Concerning the single-fault scenarios (1 to 5), the detection rate is lower than for the multiple-fault ones. Indeed, as the step is only on one variable, the global step has a lower magnitude than for the multiple-fault ones, and so is less detectable. An interesting remark is that the more the fault is on an initial variable and the less it is detectable. For example, the step on variable X1 (first in the causal graph) is only of $62.58 \%$, the same step on variable X3 is $82.92 \%$ and the same step on variable X5 reaches $96.24 \%$. Indeed, more the fault affects a root causal variable (first in the causal graph) and more this fault is diluted and so becomes non detectable.

Concerning the diagnosis, we can see that more there is implicated variables and more the diagnosis is difficult (inverse conclusion of the detection). But, like for the detection, we can see that more the implicated variables are root causal variables, and more the diagnosis is difficult. For example, the diagnosis is better for a step on X2 and X5 (scenario 12, good diagnosis of $89.41 \%$ ) than for a step on X4 (a more causal root variable than X2) and X5 (scenario 15, good diagnosis of $64 \%$ ). The different analyses are represented in the table 5 .


Table 5: Results analysis of the table 4
For a better understanding of the proposed method and particularly of the proposed Bayesian network, we give results of the scenario 8 (steps on X1 and X4) for the first 50 observations. These results are presented graphically on figure 14. In order to well see the difference, we firstly give 50 observations of under control situation. Moreover, we also add classical fault detection and identification tools on the left part of the figure: the first one is the $T^{2}$ control chart, and the five above are the classical (Shewhart) control chart of the different variables. On the right part of the figure, we present the probabilities given by the network of the figure 13. The first graph represents the probability of the process to be out-of-control. As this probability is higher than 0.5 , the process is not under control. The conclusions (detections) are equivalent to the $T^{2}$ control chart ones. The others five graphs represents the probability that the variable is implicated in the fault. Like for the first graph, if the probability is greater than 0.5 , it signifies that the variable can be considered as a root cause of the fault (good diagnosis for scenario 8).

On the figure 14, we can see that if we use a classical approach, we can conclude that all the variables are causes of the detected fault. But, with the Bayesian network method, we can see easily that only the variables X1 and X4 are root causes of the fault.

![img-13.jpeg](img-13.jpeg)

Figure 14: Results of the scenario 8 (step on X1 and X4)

# 6. Conclusions and Outlooks 

In this article, we have presented an approach allowing the fault detection and fault identification of a multivariate process. This approach is based on a Bayesian network. We have combined previous works of control chart in a Bayesian network with some recent works of Li et al. [1]. The proposed approach allows to identify the variables responsible of a fault in a multivariate process. The method has been tested on a 5 -variable system (a hot forming process) demonstrating well the abilities of the method. This article demonstrates the impact to take into account causality into the detection and identification steps. An evident outlook is to search how to take into account some causality concepts for the diagnosis step.

## A. Coefficient $c$ demonstration

This appendix presents the demonstration of the equation 7.
As in the case of the $T^{2}$ control chart [10], we will fix a threshold (Control Limit $C L$ for the control chart) on the a posteriori probabilities allowing to take decisions on the process: if, for a given observation $\boldsymbol{x}$, the a posteriori probability to be allocated to $I C(P(I C \mid \boldsymbol{x}))$ is greater than the a priori probability to be allocated to $I C(P(I C))$, then this observation is allocated to $I C$. This rule can be rewritten as: $\boldsymbol{x} \in I C$ if $P(I C \mid \boldsymbol{x})>P(I C)$, or equivalently $\boldsymbol{x} \in O C$ if $P(O C \mid \boldsymbol{x})<P(O C)$. The objective of the following developments is to define $c$ in order to obtain the equivalence between the Bayesian network and the multivariate $T^{2}$ control chart.

We want to keep the following decision rule:

$$
\boldsymbol{x} \in I C \quad \text { if } \quad T^{2}<C L
$$

with this decision rule:

$$
\boldsymbol{x} \in I C \quad \text { if } \quad P(I C \mid \boldsymbol{x})>P(I C)
$$

We develop the second decision rule:

$$
\begin{aligned}
P(I C \mid \boldsymbol{x}) & >P(I C) \\
P(I C \mid \boldsymbol{x}) & >(P(I C))(P(I C \mid \boldsymbol{x})+P(O C \mid \boldsymbol{x})) \\
P(I C \mid \boldsymbol{x}) & >P(I C) P(I C \mid \boldsymbol{x})+P(I C) P(O C \mid \boldsymbol{x}) \\
P(I C \mid \boldsymbol{x})-P(I C) P(I C \mid \boldsymbol{x}) & >P(I C) P(O C \mid \boldsymbol{x}) \\
P(I C \mid \boldsymbol{x})(1-P(I C) & >P(I C) P(O C \mid \boldsymbol{x}) \\
P(I C \mid \boldsymbol{x}) P(O C) & >P(I C) P(O C \mid \boldsymbol{x}) \\
P(I C \mid \boldsymbol{x}) & >\frac{P(I C)}{P(O C)} P(O C \mid \boldsymbol{x})
\end{aligned}
$$

But, the Bayes law gives:

$$
P(I C \mid \boldsymbol{x})=\frac{P(I C) P(\boldsymbol{x} \mid I C)}{P(\boldsymbol{x})}
$$

and

$$
P(O C \mid \boldsymbol{x})=\frac{P(O C) P(\boldsymbol{x} \mid O C)}{P(\boldsymbol{x})}
$$

So, we obtain:

$$
\begin{aligned}
\frac{P(I C) P(\boldsymbol{x} \mid I C)}{P(\boldsymbol{x})} & >\left(\frac{P(I C)}{P(O C)}\right) \frac{P(O C) P(\boldsymbol{x} \mid O C)}{P(\boldsymbol{x})} \\
\left(\frac{P(I C)}{P(O C)}\right) P(\boldsymbol{x} \mid I C) & >\left(\frac{P(I C)}{P(O C)}\right) P(\boldsymbol{x} \mid O C) \\
P(\boldsymbol{x} \mid I C) & >P(\boldsymbol{x} \mid O C)
\end{aligned}
$$

In the case of a discriminant analysis with $k$ classes $C_{i}$, the conditional probabilities are computed with the following equation 15 , where $\phi$ represents the probability density function of the multivariate Gaussian distribution of the class.

$$
P\left(\boldsymbol{x} \mid C_{i}\right)=\frac{\phi\left(\boldsymbol{x} \mid C_{i}\right)}{\sum_{j=1}^{k} P\left(C_{j}\right) \phi\left(\boldsymbol{x} \mid C_{j}\right)}
$$

So, equation 14 can be written as:

$$
\phi(\boldsymbol{x} \mid I C)>\phi(\boldsymbol{x} \mid O C)
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
\phi(\boldsymbol{x} \mid I C) & >\phi(\boldsymbol{x} \mid O C) \\
\frac{e^{-\frac{x^{2}}{2}}}{(2 \pi)^{p / 2}|\boldsymbol{\Sigma}|^{1 / 2}} & >\frac{e^{-\frac{x^{2}}{2 c}}}{(2 \pi)^{p / 2}|\boldsymbol{\Sigma}|^{1 / 2} c^{p / 2}} \\
e^{-\frac{x^{2}}{2}} & >\frac{e^{-\frac{x^{2}}{2 c}}}{c^{p / 2}} \\
-\frac{T^{2}}{2} & >-\frac{T^{2}}{2 c}-\frac{p \ln (c)}{2} \\
T^{2} & <\frac{T^{2}}{c}+p \ln (c) \\
T^{2} & <\frac{p \ln (c)}{1-\frac{1}{c}}
\end{aligned}
$$

However, we search the value(s) of $c$ allowing the equivalence with the control chart decision rule: $\boldsymbol{x} \in I C \quad i f \quad T^{2}<C L$. So, we obtain the following equation for $c$ :

$$
\frac{p \ln (c)}{1-\frac{1}{c}}=L C
$$

Or, equivalently:

$$
1-c+\frac{p c}{L C} \ln (c)=0
$$
