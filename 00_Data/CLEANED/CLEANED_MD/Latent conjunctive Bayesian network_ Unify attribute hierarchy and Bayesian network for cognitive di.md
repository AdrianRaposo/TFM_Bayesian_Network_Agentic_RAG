# Latent Conjunctive Bayesian Network: Unify Attribute Hierarchy and Bayesian Network for Cognitive Diagnosis 

Seunghyun Lee ${ }^{\dagger}$ and Yuqi Gu*<br>Department of Statistics, Columbia University


#### Abstract

Cognitive diagnostic assessment aims to measure specific knowledge structures in students. To model data arising from such assessments, cognitive diagnostic models with discrete latent variables have gained popularity in educational and behavioral sciences. In a learning context, the latent variables often denote sequentially acquired skill attributes, which is often modeled by the so-called attribute hierarchy method. One drawback of the traditional attribute hierarchy method is that its parameter complexity varies substantially with the hierarchy's graph structure, lacking statistical parsimony. Additionally, arrows among the attributes do not carry an interpretation of statistical dependence. Motivated by these, we propose a new family of latent conjunctive Bayesian networks (LCBNs), which rigorously unify the attribute hierarchy method for sequential skill mastery and the Bayesian network model in statistical machine learning. In an LCBN, the latent graph not only retains the hard constraints on skill prerequisites as an attribute hierarchy, but also encodes nice conditional independence interpretation as a Bayesian network. LCBNs are identifiable, interpretable, and parsimonious statistical tools to diagnose students' cognitive abilities from assessment data. We propose an efficient two-step EM algorithm for structure learning and parameter estimation in LCBNs, and establish the consistency of this procedure. Application of our method to an international educational assessment dataset gives interpretable findings of cognitive diagnosis.


Keywords: Attribute hierarchy; Bayesian network; Cognitive diagnostic model; Directed graphical model; EM algorithm; Identifiability.

## 1 Introduction

Cognitive diagnostic assessment aims to measure specific knowledge structures and processing skills in students (Leighton and Gierl, 2007). To model data arising from such

[^0]
[^0]:    ${ }^{\dagger}$ sl4963@columbia.edu.
    *yuqi.gu@columbia.edu. This work is partially supported by NSF Grant DMS-2210796.

assessments, cognitive diagnostic models (CDMs) with discrete latent variables (also called diagnostic classification models; see Rupp et al., 2010; von Davier and Lee, 2019) have recently gained great popularity in educational, psychological, and behavioral applications.

CDMs adopt a set of discrete latent attributes with substantive meaning to explain a subject's multivariate responses to a set of items. "Attribute" here is a generic term that can represent unobserved psychological constructs including skills, knowledge states, conceptual understandings, cognitive processes, and rules (Wang, 2021). In educational settings, each attribute often represents the mastery/deficiency of a specific latent skill. Adopting CDMs in educational assessment can generate fine-grained diagnoses about students' multiple latent skills, and hence provide detailed feedback about their weaknesses and strengths. A typical CDM consists of a structural model for the latent attributes and a measurement model describing the dependence of the observed variables (i.e., item responses in educational assessments) on the latent attributes. The measurement model is accompanied by a so-called Q-matrix (Tatsuoka, 1983), summarizing which subset of the attributes each observed variable measures or requires. The Q-matrix is often pre-specified by domain experts.

Various measurement models have been proposed for different diagnostic purposes. For example, the popular and fundamental Deterministic Input Noisy Output "AND" gate (DINA; Junker and Sijtsma, 2001) model adopts the conjunctive assumption by specifying that a student needs to master all attributes required by an item to be capable of it. The generalized DINA (GDINA; de la Torre, 2011) model generalizes this by incorporating main effects and interaction effects of required attributes into the measurement model. Other popular CDMs include the Deterministic Input Noisy Output "OR" gate (DINO; Templin and Henson, 2006) model, the log-linear CDM (LCDM; Henson et al., 2009), the additive CDM (ACDM; de la Torre, 2011), and general diagnostic models (GDM; von Davier, 2008).

As for the structural model for the latent attributes in a CDM, the attribute hierarchy method that models sequential skill mastery has recently attracted increasing attention (Leighton et al., 2004; Gierl et al., 2007; Wang and Gierl, 2011; Templin and Bradshaw, 2014; Gu and Xu, 2019; Wang and Lu, 2021). Students' learning is not instantaneous and often proceeds in a sequential and dependent manner. In a learning context, possessing lower level skills are often believed to be the prerequisite for possessing higher level skills (Simon and Tzur, 2012; Briggs and Alonzo, 2012). Leighton et al. (2004) first proposed the attribute

hierarchy method, and Templin and Bradshaw (2014) integrated the attribute hierarchy with a flexible measurement model in a statistical framework to define the family of hierarchical cognitive diagnostic models (HCDMs). HCDMs adopt the unstructured statistical model for the attribute patterns under a hierarchy. Specifically, in an HCDM, each pattern respecting the attribute hierarchy has an unstructured proportion parameter, which characterizes how much proportion of the student population possess this skill pattern.

Most existing studies on attribute hierarchy followed Templin and Bradshaw (2014) to adopt the unstructured model for hierarchies. One limitation of this popular approach is that its parameter complexity varies substantially with the graph structure of the hierarchy, lacking statistical parsimony. For instance, with $K$ binary attributes, a chain graph hierarchy requires $K$ free parameters for the latent distribution, whereas a graph with one attribute serving as a common parent to all the other attributes requires $2^{K-1}$ parameters. This lack of parsimony especially creates computational and statistical challenges when there are a large number of attributes and a limited sample size. In addition, the unstructured model for attribute hierarchy does not endow the hierarchy graph with any probabilistic interpretation. Specifically, the hierarchy among the latent attributes is merely treated as a machinery for inducing hard constraints on which latent attribute patterns are permissible (those respecting the hierarchy) and which are forbidden (those violating the hierarchy). As a result, the arrows in such an attribute hierarchy graph do not carry clear interpretation of direct statistical dependence, nor does the lack of arrows indicate conditional independence.

Motivated by the above issues, we propose a new family of latent conjunctive Bayesian networks (LCBNs) for cognitive diagnosis. LCBNs are a parsimonious and interpretable class of probabilistic graphical models that rigorously unify attribute hierarchy and Bayesian network. A Bayesian network (Pearl, 1988) is a directed graphical model of random variables, in which directed arrows indicate statistical dependence and the lack of arrows indicate conditional independence. In our LCBN, the directed acyclic graph among the latent attributes not only respects the hard constraints on which attribute patterns are permissible/forbidden as under a usual attribute hierarchy, but also encodes the nice conditional independence interpretation as in a usual Bayesian network. Therefore, LCBNs enjoy the best of both worlds. Moveover, LCBNs are parsimonious statistical models with a fixed parameter complexity in the latent part - it always only requires $K$ parameters for specifying the joint

distribution of $K$ binary latent attributes, regardless of the graph structure of the hierarchy.
In terms of model identifiability, we prove that the attribute hierarchy graph and all the continuous parameters in an LCBN are fully identifiable from the observed data distribution. Our identifiability conditions are transparent requirements on the discrete structure in the model. Identifiability lays the foundation for valid statistical estimation and inference. In terms of estimation, we propose an efficient two-step EM algorithm to perform structure learning and parameter estimation in LCBNs. In the first step, we leverage a penalized EM algorithm for selecting significant latent patterns (Gu and Xu, 2019) to estimate the discrete structure - the attribute hierarchy graph. In the second step, we fix the attribute hierarchy and propose another EM algorithm to estimate the continuous parameters in the LCBN. Simulation studies demonstrate the estimation accuracy of this procedure. We apply our method to analyze a dataset extracted from an international educational assessment, the Trends in Mathematics and Science Study (TIMSS). The real data analysis gives interpretable finds of cognitive diagnosis and demonstrates the wide applicability of our method.

The remainder of this paper is organized as follows. Section 2 introduces the background of cognitive diagostic modeling, proposes the general framework of LCBNs, and discusses some related work. Section 3 provides identifiability conditions of LCBNs. Section 4 proposes a two-step EM algorithm to estimate the attribute hierarchy graph and model parameters in LCBNs. Section 5 presents simulation studies to empirically assess the proposed method. Section 6 applies the new method to analyze an international educational assessment dataset. Finally, Section 7 provides concluding remarks and discusses future directions. We also provide the technical proofs of the theorems, additional identifiability results, and additional simulation studies in the Supplementary Material.

# 2 Latent Conjunctive Bayesian Network 

### 2.1 Cognitive Diagnostic Modeling with an attribute hierarchy

We first introduce the basic setup of a CDM. Consider a CDM for modeling a cognitive diagnostic assessment. A student's observed variables are his or her correct/wrong responses to a set of $J$ items in the assessment, denoted by $\mathbf{R}=\left(R_{1}, \ldots, R_{J}\right) \in\{0,1\}^{J}$, in which $R_{j}=1$

indicates the student's response to the $j$ th item is correct and $R_{j}=0$ otherwise. A student's latent variables are his or her profile of presence/absence of a set of $K$ skill attributes, denoted by $\boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{K}\right) \in\{0,1\}^{K}$, in which $\alpha_{k}=1$ indicates the student masters the $k$ th skill and $\alpha_{k}=0$ otherwise. Typically, a CDM consists of two parts: a structural model for the latent attributes, and a measurement model to describe the distribution of the observed responses given the latent. In a learning context, the skill attributes are often sequentially acquired and form a hierarchy with prerequisite relations among attributes. In a CDM with attribute hierarchy, the key elements of the structural and measurement modeling parts are captured by two discrete graph structures: a directed acyclic graph among the latent attributes, and a bipartite directed graph pointing from the latent attributes to the observed responses. These two graphical structures are illustrated in Figure 1. For clarity of presentation, we next describe the measurement part and the structural part of a CDM separately in subsequent paragraphs.
![img-0.jpeg](img-0.jpeg)

Figure 1: Graphical model representation of a cognitive diagnostic model with a linear attribute hierarchy. White nodes are latent attributes, and grey nodes are observed responses. Dotted arrows denote the prerequisite relationship among the latent attributes, and solid arrows denote the conditional dependence structure of the observed responses given the latent attributes.

For the measurement part of a CDM, educational experts who designed the assessment usually provide information about which subset of the $K$ skills each test item measures. All such information are summarized in a so-called Q-matrix (Tatsuoka, 1983). The Q-matrix $\mathbf{Q}=\left(q_{j, k}\right) \in\{0,1\}^{J \times K}$ is a $J \times K$ matrix with binary entries, with rows indexed by observed items and columns by latent attributes. Each entry $q_{j, k}=1$ or 0 indicates whether or not the $j$ th test item requires/measures the $k$ th latent skill. Consequently, the $j$ th row vector of $\mathbf{Q}$, denoted by $\boldsymbol{q}_{j}=\left(q_{j, 1}, \ldots, q_{j, K}\right)$, is the attribute requirement profile of item $j$. For example, in Figure 1 we have $\boldsymbol{q}_{1}=(1,0,0,0)$ since the first item only requires the first attribute.

Statistically, a student's responses to the $J$ items are assumed to be conditionally inde-

pendent given his or her latent attribute profile $\boldsymbol{\alpha}$. Such a local independence assumption is widely adopted in various models for item response data. We collect all the conditional correct response probabilities in a $J \times 2^{K}$ item parameter matrix $\boldsymbol{\Theta}=\left(\theta_{j, \boldsymbol{\alpha}}\right)_{J \times 2^{K}}$, with rows indexed by the $J$ test items and columns by the $2^{K}$ binary pattern configurations in $\{0,1\}^{K}$. For any $j \in[J]$ and $\boldsymbol{\alpha} \in\{0,1\}^{K}$, the entry

$$
\theta_{j, \boldsymbol{\alpha}}=\mathbb{P}\left(R_{j}=1 \mid \boldsymbol{\alpha}\right)
$$

defines the conditional probability of giving a correct response to item $j$ given that one has a latent skill profile $\boldsymbol{\alpha}$. For two vectors $\boldsymbol{a}=\left(a_{1}, \ldots, a_{K}\right)$ and $\boldsymbol{b}=\left(b_{1}, \ldots, b_{K}\right)$ of the same length, we write $\boldsymbol{a} \succeq \boldsymbol{b}$ if $a_{k} \geq b_{k}$ for all $k \in[K]$ and write $\boldsymbol{a} \not \subset \boldsymbol{b}$ otherwise. An important observation is that, since $\boldsymbol{q}_{j}$ describes which subset of attributes item $j$ measures, the correct response probability $\theta_{j, \boldsymbol{\alpha}}$ only depends on those attributes $\alpha_{k}$ that are measured by item $j$ (that is, those $\alpha_{k}$ with $q_{j, k}=1$ ). Therefore,

$$
\theta_{j, \boldsymbol{\alpha}}=\theta_{j, \boldsymbol{\alpha}^{\prime}} \text { for any } \boldsymbol{\alpha}, \boldsymbol{\alpha}^{\prime} \succeq \boldsymbol{q}_{j}
$$

Another common feature shared by many different CDM measurement models is that item parameters often exhibit monotonicity (Xu and Shang, 2018; Gu and Xu, 2019; Balamuta and Culpepper, 2022):

$$
\theta_{j, \boldsymbol{\alpha}}>\theta_{j, \boldsymbol{\alpha}^{\prime}} \text { for any } \boldsymbol{\alpha} \succeq \boldsymbol{q}_{j} \text { and } \boldsymbol{\alpha}^{\prime} \not \subset \boldsymbol{q}_{j}
$$

The above inequality can be interpreted as: if a student possesses all the attributes required by item $j$ (that is, $\boldsymbol{\alpha} \succeq \boldsymbol{q}_{j}$ ), then this student has a higher probability to give a correct response to this item compared to other subjects who lack some required attribute.

We next review some popular and widely used CDM measurement models.
Example 1 (DINA model). The Deterministic Input Noisy output "And" gate (DINA; Junker and Sijtsma, 2001) model is a very popular and fundamental CDM. For each item $j$, DINA uses exactly two distinct parameters to describe the conditional distribution of $R_{j}$. Specifically, if a student with latent profile $\boldsymbol{\alpha}$ masters all the required attributes of item $j$ (i.e., $\boldsymbol{\alpha} \succeq \boldsymbol{q}_{j}$ ), then he/she is considered capable of this item but still has a small probability

$s_{j}$ to make a careless mistake; on the other hand, if the student lacks some of the required attributes with $\boldsymbol{\alpha} \not \nsubseteq \boldsymbol{q}_{j}$, then he/she is considered incapable of this item but still has a small probability $g_{j}$ to have a lucky guess. The correct response probability can be written as

$$
\theta_{j, \boldsymbol{\alpha}}=\mathbb{P}\left(R_{j}=1 \mid \boldsymbol{\alpha}\right)= \begin{cases}1-s_{j}, & \text { if } \boldsymbol{\alpha} \succeq \boldsymbol{q}_{j} \\ g_{j}, & \text { if } \boldsymbol{\alpha} \not \nsubseteq \boldsymbol{q}_{j}\end{cases}
$$

$s_{j}$ and $g_{j}$ are called slipping parameter and guessing parameter, respectively. The monotonicity inequality in (2) now boils down to $1-s_{j}>g_{j}$ for all $j$. The interpretation is that for any item, a capable student always has a higher probability of giving a correct response than an incapable student. DINA is widely used in educational cognitive diagnosis due to its parsimony and interpretability.

Example 2 (Main-effect CDMs). Main-effect CDMs incorporate the main effects of the latent attributes to model the responses. Specifically, a main-effect CDM assumes that the probability of $R_{j}=1$ is a function of the main effects of the attributes required for item $j$.

$$
\theta_{j, \boldsymbol{\alpha}}=f\left(\delta_{j, 0}+\sum_{k=1}^{K} \delta_{j, k} q_{j, k} \alpha_{k}\right)
$$

where $f(\cdot)$ is a monotonic link function. Note that not all the $\delta_{j, k}$ in the above expression are needed in the model specification. Only when $q_{j, k}=1$ will the corresponding $\delta_{j, k}$ be incorporated in the model. Assuming $\delta_{j, k}>0$ satisfies the monotonicity requirement (2). When the link function $f$ is the identity, (4) gives the Additive Cognitive Diagnosis Model (ACDM; de la Torre, 2011); when $f$ is the inverse logit function, (4) gives the Logistic Linear Model (LLM; Maris, 1999); yet another parametrization of (4) gives rise to the Reduced Reparameterized Unified Model (R-RUM; DiBello et al., 1995).

Example 3 (All-effect CDMs). All-effect CDMs generalize both the DINA model and the main-effect CDMs by considering both the main effects and all the interaction effects of the

required attributes. The item parameter $\theta_{j, \boldsymbol{\alpha}}$ can be written as

$$
\theta_{j, \boldsymbol{\alpha}}=f\left(\delta_{j, 0}+\sum_{k=1}^{K} \delta_{j, k} q_{j, k} \alpha_{k}+\sum_{1 \leq k<k^{\prime} \leq K} \delta_{j, k k^{\prime}}\left(q_{j, k} \alpha_{k}\right)\left(q_{j, k^{\prime}} \alpha_{k^{\prime}}\right)+\cdots+\delta_{j, 1 \cdots K} \prod_{k=1}^{K}\left(q_{j, k} \alpha_{k}\right)\right)
$$

where $\delta_{j, k}$ is the main effect of the required attribute $\alpha_{k}$, and $\delta_{j, k k^{\prime}}$ is the interaction effect between two required attributes $\alpha_{k}$ and $\alpha_{k^{\prime}}$, etc. When the link function $f$ is the identity, (5) gives the Generalized DINA model (GDINA; de la Torre, 2011); when $f$ is the inverse logit, (5) gives the Log-linear CDM (LCDM; Henson et al., 2009); also see the General Diagnostic Model (GDM) framework in von Davier (2008).

We now describe the structural modeling part of a CDM with an attribute hierarchy. The hierarchy is a collection of prerequisite relations between the $K$ latent attributes, in which possessing lower level, more basic skills are assumed to be the prerequisite for possessing higher level, more advanced ones. For any $1 \leq k \neq \ell \leq K$, we say that attribute $k$ is a prerequisite for attribute $\ell$ (and denote this by $\alpha_{k} \rightarrow \alpha_{\ell}$ or simply $k \rightarrow \ell$ ) if any latent skill pattern $\boldsymbol{\alpha} \in\{0,1\}^{K}$ with $\alpha_{k}=0$ and $\alpha_{\ell}=1$ does not exist in the student population and is not "permissible". In other words, for any student that masters the higher level advanced skill $\alpha_{\ell}$, he/she must have mastered the lower level basic skill $\alpha_{k}$. Denote the collection of all the prerequisite relationships by
$\mathcal{E}=\{k \rightarrow \ell:$ the $k$ th skill attribute is a prerequisite for the $\ell$ th skill attribute $\}$.

Any attribute hierarchy $\mathcal{E}$ can be visualized as a directed acyclic graph among $K$ nodes, each node representing a latent attribute. For example, Figure 1 illustrates a linear hierarchy among the skills with $\mathcal{E}=\left\{\alpha_{1} \rightarrow \alpha_{2}, \alpha_{2} \rightarrow \alpha_{3}, \ldots, \alpha_{K-1} \rightarrow \alpha_{K}\right\}$.

Statistically, for a traditional CDM without any attribute hierarchy, the most commonly adopted model for the latent attributes is the unstructured model. This model endows every latent skill profile $\boldsymbol{\alpha} \in\{0,1\}^{K}$ with a population proportion parameter $p_{\boldsymbol{\alpha}}$, satisfying $p_{\boldsymbol{\alpha}} \geq 0$ and $\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} p_{\boldsymbol{\alpha}}=1$. The parameter $p_{\boldsymbol{\alpha}}$ describes the proportion in the student population that possesses the attribute pattern $\boldsymbol{\alpha}$. For a CDM with an attribute hierarchy, most existing studies followed Templin and Bradshaw (2014) to adopt an unstructured statistical model for the hierarchy. Specifically, such a model is based on the observation that any nonempty

$\mathcal{E}$ induces a sparsity structure on the $2^{K}$-dimensional proportion parameters $\boldsymbol{p}=\left(p_{\boldsymbol{\alpha}}: \boldsymbol{\alpha} \in\right.$ $\left.\{0,1\}^{K}\right)$. For example, if $k \rightarrow \ell$, then as aforementioned, any pattern $\boldsymbol{\alpha}$ with $\alpha_{k}=0$ but $\alpha_{\ell}=1$ does not exist in the population and hence its population proportion $p_{\boldsymbol{\alpha}}=0$. In this way, we can define the set of permissible latent skill patterns under a hierarchy $\mathcal{E}$ as follows:

$$
\mathcal{A}(\mathcal{E})=\left\{\boldsymbol{\alpha} \in\{0,1\}^{K}: \boldsymbol{\alpha} \text { is permissible under } \mathcal{E}\right\}=\left\{\boldsymbol{\alpha} \in\{0,1\}^{K}: p_{\boldsymbol{\alpha}}>0 \text { under } \mathcal{E}\right\}
$$

Note that $\mathcal{A}(\mathcal{E})$ is fully determined by the attribute hierarchy $\mathcal{E}$.
Since the hierarchy $\mathcal{E}$ is a directed acyclic graph among $K$ attributes, it can also be equivalently represented by a $K \times K$ reachability matrix $\mathbf{G}(\mathcal{E})$ (also denoted by $\mathbf{G}$ for short) in the graph theory terminology. The $(k, \ell)$ th entry of $\mathbf{G}$ is a binary indicator of whether the $k$ th skill is the prerequisite for the $\ell$ th skill, that is, $G_{k, \ell}=\mathbb{1}(k \rightarrow \ell)$. Here we assume the diagonal entries of $\mathbf{G}$ are all zero. This definition is slightly different from the reachability matrix $\mathbf{E}$ in Gu and Xu (2022), which assumes all diagonal entries to be one. Assuming $\mathbf{G}$ in our current way is for notational convenience, as to be demonstrated soon in (8) in the next subsection. The following example illustrates the concepts related to the attribute hierarchy.

Example 4. Consider an example with $K=4$ skill attributes and a hierarchy $\mathcal{E}=\{1 \rightarrow$ $3,1 \rightarrow 4,2 \rightarrow 3,2 \rightarrow 4\}$. This hierarchy means that the first two skills are the basic ones that serve as the prerequisites for the last two advanced skills. This $\mathcal{E}$ is visualized in the left panel of Figure 2. There are seven permissible attribute patterns under $\mathcal{E}$ :

$$
\mathcal{A}(\mathcal{E})=\{0000,1000,0100,1100,1110,1101,1111\}
$$

The patterns in $\mathcal{A}(\mathcal{E})$ can also be viewed as forming a distributive lattice, a concept in combinatorics (Gratzer, 2009), as shown in the middle panel of Figure 2. The corresponding reachability matrix $\mathbf{G}$ under $\mathcal{E}$ is shown in the rightmost panel of Figure 2.

It is worth emphasizing the distinction between a directed acyclic graph (DAG) in the usual attribute hierarchy method and that in a conventional Bayesian network model (Pearl, 1988, or equivalently, a probabilistic directed graphical model). Specifically, the arrows in the DAG among the latent attributes (as shown in Figure 2) generally cannot be in-

![img-1.jpeg](img-1.jpeg)

$$
\mathbf{G}=\left(\begin{array}{cccc}
0 & 0 & 1 & 1 \\
0 & 0 & 1 & 1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right)
$$

Figure 2: An example with $K=4$ skill attributes. Left: attribute hierarchy graph $\mathcal{E}$. Middle: all the allowable attribute patterns in $\mathcal{A}(\mathcal{E})$. Right: $K \times K$ reachability matrix $\mathbf{G}$.
terpreted as encoding direct statistical dependence, nor does the lack of arrows indicate conditional independence. Rather, such a DAG merely encodes certain hard constraints on what attribute patterns are permissible (those $\boldsymbol{\alpha} \in \mathcal{A}(\mathcal{E})$ ) and which are forbidden (those $\boldsymbol{\alpha} \in\{0,1\}^{K} \backslash \mathcal{A}(\mathcal{E})$ ). In contrast, the DAG in a Bayesian network has arrows capturing the statistical dependence between the random variables, and the lack of arrows can indicate conditional independence. Such a probabilistic DAG generally does not forbid any configurations of the random variables.

A natural and interesting question is - can we introduce a new family of models that rigorously unify the above two models and inherit the advantages of both? This question is particularly relevant considering the drawbacks of the existing attribute hierarchy method, including not only the lack of interpretability, but also the lack of statistical parsimony. To see this, consider an attribute hierarchy $\mathcal{E}=\{1 \rightarrow 2,1 \rightarrow 3, \ldots, 1 \rightarrow K\}$ where the first attribute serves as a common prerequisite for all the $K-1$ remaining attributes. This $\mathcal{E}$ implies $\mathcal{A}(\mathcal{E})=\left\{\mathbf{0}_{1 \times K},\left(1, \boldsymbol{\alpha}^{\prime}\right)\right.$ for all $\boldsymbol{\alpha}^{\prime} \in\{0,1\}^{K-1}\}$ with $2^{K-1}+1$ permissible patterns. To model this $\mathcal{E}$, a conventional attribute hierarchy method would require $2^{K-1}$ free parameters in the latent distribution, because it gives each permissible pattern $\boldsymbol{\alpha}$ an unstructured proportion parameter $p_{\boldsymbol{\alpha}}$. Such a lack of parsimony especially creates statistical and computational challenges when there are a large number of attributes but a limited sample size, as would be the case in fine-grained cognitive diagnosis of many skills in small classroom settings.

# 2.2 Latent Conjunctive Bayesian Networks 

This subsection introduces a new family of models for attribute hierarchy in cognitive diagnosis: the Latent Conjunctive Bayesian Networks (LCBNs). LCBNs rigorously unify the attribute hierarchy method in educational measurement and the Bayesian network model in statistical machine learning, and inherit the advantages of both. Our proposal of LCBNs is inspired by another seemingly remote research area - graphical modeling of genetic mutations in bioinformatics. Specifically, the conjunctive Bayesian network (CBN) proposed by Beerenwinkel et al. (2005) and analyzed by Beerenwinkel et al. (2007), models a set of observed binary genetic mutations by a partial order, and assign zero probabilities to genotypes (analogue of our skill attribute patterns) that are not compatible with this partial order (analogue of our attribute hierarchy). An important difference is that, genetic mutations are often assumed to be entirely observed without any latent variables (Beerenwinkel et al., 2005, 2006, 2007). In contrast, in our cognitive diagnostic modeling of educational assessment data, the skill attributes are latent constructs that are not directly observable, but rather indirectly measured by item responses. We will further discuss the differences between the proposed LCBN and the CBN in Section 2.3, after elaborating on their common conjunctive modeling framework for multiple binary random variables.

We formally define the latent conjunctive Bayesian network for the attribute hierarchy. Introduce $K$ Bernoulli parameters $\boldsymbol{t}=\left(t_{1}, \ldots, t_{K}\right)^{\top} \in(0,1)^{K}$. For any $k \in[K]$, denote the set of "parent" attributes of $\alpha_{k}$ in the attribute hierarchy graph by $\mathrm{pa}(k)$. The parent attribute of $\alpha_{k}$ here has the identical definition as the prerequisite attribute of $\alpha_{k}$. For example, for the attribute hierarchy shown in Figure 2, $\mathrm{pa}(1)=\mathrm{pa}(2)=\varnothing$ and $\mathrm{pa}(3)=\mathrm{pa}(4)=\left\{\alpha_{1}, \alpha_{2}\right\}$. Now define the probability mass function of the attribute pattern as follows:

$$
\begin{aligned}
\forall \boldsymbol{\alpha} \in\{0,1\}^{K}, \quad p_{\boldsymbol{\alpha}} & =\mathbb{P}(\boldsymbol{\alpha} \mid \boldsymbol{t})=\prod_{k=1}^{K} \mathbb{P}\left(\alpha_{k} \mid \mathrm{pa}(k)\right), \text { where } \\
\mathbb{P}\left(\alpha_{k} \mid \mathrm{pa}(k)\right) & =t_{k}{ }^{\alpha_{k}} \Pi_{\ell=1}^{K} \alpha_{\ell}^{G_{l, k}}\left(1-t_{k}\right)^{\left(1-\alpha_{k}\right)} \Pi_{\ell=1}^{K} \alpha_{\ell}^{G_{l, k}} \\
& =t_{k}{ }^{\alpha_{k}} \Pi_{\ell \rightarrow k}{ }^{\alpha_{\ell}}\left(1-t_{k}\right)^{\left(1-\alpha_{k}\right)} \Pi_{\ell \rightarrow k}{ }^{\alpha_{\ell}}
\end{aligned}
$$

$$
=\begin{cases}t_{k}, & \text { if } \alpha_{k}=1 \text { and } \prod_{\ell \rightarrow k} \alpha_{\ell}=1 \\ 1-t_{k}, & \text { if } \alpha_{k}=0 \text { and } \prod_{\ell \rightarrow k} \alpha_{\ell}=1 \\ 0, & \text { if } \alpha_{k}=1 \text { and } \prod_{\ell \rightarrow k} \alpha_{\ell}=0 \\ 1, & \text { if } \alpha_{k}=0 \text { and } \prod_{\ell \rightarrow k} \alpha_{\ell}=0\end{cases}
$$

Eq. (8) follows the conventional definition of a Bayesian network (i.e., a probabilistic directed graphical model), where the joint distribution of random variables factorizes into the product of conditional distributions of each variable given its parents (Bishop, 2006). The conjunctive Bayesian network defined above has an intuitive and natural interpretation. This model states that a student can only master attribute $\alpha_{k}$ if he/she has already mastered every prerequisite attribute for $\alpha_{k}$; in this case, the mastery of $\alpha_{k}$ happens with probability

$$
t_{k}=\mathbb{P}\left(\alpha_{k}=1 \mid \alpha_{\ell}=1 \text { for all } \ell \in[K] \text { such that } \ell \rightarrow k\right)
$$

and $1-t_{k}$ represents the probability of failing to master $\alpha_{k}$ given the student has already mastered all of its prerequisite attributes. The last two lines in (9) state that, if a student lacks some of $\alpha_{k}$ 's prerequisite skills, then the probability of mastering $\alpha_{k}$ equals zero and that of not mastering $\alpha_{k}$ equals one. Therefore, this model exactly respects the usual constraints on permissible/forbidden patterns as a conventional attribute hierarchy method. One can readily show that the model in (8)-(9) defines a valid joint distribution of attributes. That is, for any $\boldsymbol{t}$, we have $p_{\boldsymbol{\alpha}}=0$ for any $\boldsymbol{\alpha} \notin \mathcal{A}(\mathcal{E})$ and $\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} p_{\boldsymbol{\alpha}}=\sum_{\boldsymbol{\alpha} \in \mathcal{A}(\mathcal{E})} p_{\boldsymbol{\alpha}}=1$.

The following example illustrates how the population proportion parameters $\boldsymbol{p}=\left(p_{\boldsymbol{\alpha}}\right)$ are parameterized by CBN parameters $\boldsymbol{t}$.

Example 5 (Example 4 continued). We revisit the attribute hierarchy in Example 4 and give it an LCBN parametrization. By (8), the proportion parameters for the permissible attribute patterns in $\mathcal{A}(\mathcal{E})$ in (7) can be written as

$$
\begin{aligned}
& p_{0000}=\left(1-t_{1}\right)\left(1-t_{2}\right), \quad p_{1000}=t_{1}\left(1-t_{2}\right), \quad p_{0100}=\left(1-t_{1}\right) t_{2} \\
& p_{1100}=t_{1} t_{2}\left(1-t_{3}\right)\left(1-t_{4}\right), \quad p_{1110}=t_{1} t_{2} t_{3}\left(1-t_{4}\right) \\
& p_{1101}=t_{1} t_{2}\left(1-t_{3}\right) t_{4}, \quad p_{1111}=t_{1} t_{2} t_{3} t_{4}
\end{aligned}
$$

For any $\boldsymbol{\alpha} \notin \mathcal{A}(\mathcal{E}), p_{\boldsymbol{\alpha}}=0$ is naturally guaranteed by following the CBN definition. Note that if without the CBN assumption, the proportion parameters $p_{\boldsymbol{\alpha}}$ would be only subject to the sparsity constraint $p_{\boldsymbol{\alpha}}=0$ for $\boldsymbol{\alpha} \notin \mathcal{A}(\mathcal{E})$; in this case, six free parameters would be needed to specify the latent distribution. In contrast, under the CBN, $\boldsymbol{\alpha}$ can be modeled using four Bernoulli parameters: $t_{1}, t_{2}, t_{3}, t_{4}$. In addition to such statistical parsimony, the LCBN model provides intuitive conditional independence statements about the skill attributes. In the current toy example, LCBN asserts that given a student's latent states of the first two basic skills, their mastery of the third and fourth skills are conditionally independent.

Under our LCBN-based cognitive diagnostic model, the marginal distribution of the observed item response vector of the $i$ th student takes the form:

$$
\mathbb{P}\left(\mathbf{R}_{i}=\boldsymbol{r} \mid \boldsymbol{\Theta}, \boldsymbol{t}, \mathcal{E}\right)=\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \underbrace{t_{k}{ }^{\alpha_{k}} \prod_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}}}\left(1-t_{k}\right)^{\left(1-\alpha_{k}\right) \prod_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}}}}_{p_{\boldsymbol{\alpha}}} \prod_{j=1}^{J} \theta_{j, \boldsymbol{\alpha}}^{r_{j}}\left(1-\theta_{j, \boldsymbol{\alpha}}\right)^{1-r_{j}}
$$

for any response pattern $\boldsymbol{r} \in\{0,1\}^{J}$. The hierarchy $\mathcal{E}$ implicitly appears in the above distribution through the reachability matrix entries $G_{\ell, k}$. The item parameters $\theta_{j, \boldsymbol{\alpha}}$ in (10) are subject to the constraints imposed by the $\mathbf{Q}$-matrix and can follow various measurement models described in Examples 1-3. Now we have completed the specification of an LCBNbased cognitive diagnostic model.

# 2.3 Comparison of LCBNs and existing models 

We now discuss the difference between our LCBN-based cognitive diagnostic model and the CBN model for genetic mutations proposed by Beerenwinkel et al. (2005). In a CBN, each binary variable $\alpha_{k}=1$ or 0 represents a genetic event of whether an amino acid in the genome has mutated or not. There is a partial order (i.e., $\mathcal{E}$ in our notation) defined on the genetic events such that certain mutations are the prerequisite for others. Any patient's genetic mutation profile is fully observed as a binary vector $\mathbf{X}_{i}=\left(X_{i 1}, \ldots, X_{i K}\right)$, and the probability mass function of $\mathbf{X}_{i}$ is

$$
\mathbb{P}\left(\mathbf{X}_{i}=\boldsymbol{\alpha} \mid \boldsymbol{t}, \mathcal{E}\right)=t_{k}{ }^{\alpha_{k}} \prod_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}}\left(1-t_{k}\right)^{\left(1-\alpha_{k}\right) \prod_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}}}, \quad \forall \boldsymbol{\alpha} \in\{0,1\}^{K}
$$

In this fully observed CBN model, the hierarchy graph $\mathcal{E}$ can be directly read off from the set of all the observed binary patterns (genotypes) of the patients. In addition, Beerenwinkel et al. (2007) showed that the maximum likelihood estimator of parameters $\boldsymbol{t}$ in a CBN actually has a closed-form solution. In contrast, in our LCBN, students' $J$-dimensional item response vectors $\mathbf{R}_{i}$ in (10) do not readily reveal the attribute hierarchy graph $\mathcal{E}$ among the $K$ latent attributes; furthermore, the LCBN parameters $\boldsymbol{t}$ only enter the likelihood through those mixture proportion parameters $p_{\boldsymbol{\alpha}}$ in (10) rather than directly. Therefore, the identifiability issue of LCBNs is nontrivial, and the estimation of the attribute hierarchy and model parameters in LCBNs is not straightforward.

In terms of modeling the binary latent variables, LCBNs have the advantages of interpretability and statistical parsimony over conventional attribute hierarchy methods and conventional Bayesian networks. Comparing these two conventional models, the usual attribute hierarchy method has fewer parameters when the hierarchy graph $\mathcal{E}$ is dense with many arrows, whereas a Bayesian network without the conjunctive assumption (employed by Hu and Templin (2020) for cognitive diagnosis) has fewer parameters when the graph $\mathcal{E}$ is sparse. As concrete examples, consider the three different hierarchies in Figure 3 among $K=7$ binary attributes. The numbers of free parameters needed to specify the distribution for the latent $\boldsymbol{\alpha}$ are shown in Table 1, from which it is clear that neither a conventional attribute hierarchy method nor a conventional Bayesian network is universally parsimonious. On the other hand, the number of parameters in LCBNs is $K$ for all hierarchies and is universally parsimonious.
![img-2.jpeg](img-2.jpeg)

Figure 3: Different attribute hierarchies with $K=7$ attributes. Divergent (left), convergent (middle), three-layer fully connected (right).

A related model in the applied psychological measurement literature is the sequential higher order latent structural model for hierarchical attributes in Zhan et al. (2020). Specifically, motivated by the higher-order latent trait modeling in de la Torre and Douglas (2004)

Table 1: Number of free parameters needed for modeling the latent attributes in the conventional attribute hierarchy method (AHM), Bayesian network (BN), and LCBN with $K=7$ attributes.


and the attribute hierarchy method, Zhan et al. (2020) proposed a conjunctive model with a higher-order continuous latent variable to model the attributes. It was assumed that every attribute $\alpha_{k}$ depends on the higher-order variable through an item response theory model. Our current work differs from this existing work in several fundamental ways. First, we do not assume the existence of any higher-order latent variables, which helps achieve the greatest amount of statistical parsimony. Only in this most parsimonious possible LCBN, the lack of arrows between the skills would encode nice conditional independence interpretation; in Zhan et al. (2020)'s higher-order model, all the skills are always conditionally dependent due to the higher-order latent trait. Second, we establish identifiability for the family of LCBNbased cognitive diagnostic models (see Section 3) and propose a general two-step method to perform both structure learning of $\mathcal{E}$ and parameter estimation of $(\Theta, t)$ (see Section 4). In previous studies such as Zhan et al. (2020), identifiability issues were not examined and estimation was performed by assuming the hierarchy $\mathcal{E}$ is known.

# 3 Identifiability of LCBNs for Cognitive Diagnosis 

Identifiability is a fundamental property of statistical models and a prerequisite for valid parameter estimation and hypothesis testing. A model is said to be identifiable if the observed data distribution uniquely determines the model parameters. If a model is not identifiable, then there exist multiple and possibly an infinite number of parameter sets that lead to the same observed distribution, and it is impossible to distinguish them based on data. In the applied context of using LCBNs for cognitive diagnosis, it is crucial to guarantee that the model is identifiable, so that any practical interpretation made about the cognitive structure

and student diagnosis is statistically valid. In this section, we provide transparent conditions for LCBNs to be identifiable.

Because the DINA model in Example 1 is the most popular and fundamental cognitive diagnostic model due to its interpretability and parsimony, we next focus on the LCBNbased DINA model and provide tight and explicit identifiability conditions for it. We remark that LCBN-based CDMs with other measurement models (such as main-effect and all-effect CDMs) are also identifiable under slightly stronger conditions. In light of the space constraint and for notational simplicity, we defer those identifiability results to Section S.1. in the Supplementary Material.

As mentioned earlier, the identifiability of LCBN-based cognitive diagnostic models is a nontrivial and challenging issue, unlike the fully observed CBNs. Fortunately, thanks to our model formulation, the LCBN parameters $\boldsymbol{t}$ enter the observed distribution in (10) only through the mixture proportion parameters $p_{\boldsymbol{\alpha}}$. Therefore, we are able to leverage existing techniques for conventional CDMs with an unstructured attribute hierarchy model in Gu and Xu (2022) to establish identifiability for LCBNs. Specifically, we next provide conditions that ensure the identifiability of not only the continuous parameters $(\boldsymbol{s}, \boldsymbol{g}, \boldsymbol{t})$, but also the discrete hierarchy graph structure $\mathcal{E}$ in an LCBN.

We first define the concept of strict identifiability of the LCBN-based DINA model.
Definition 1 (Strict identifiability for LCBN-based DINA). The parameters $(\mathcal{E}, \boldsymbol{s}, \boldsymbol{g}, \boldsymbol{t})$ of an LCBN-based DINA model are identifiable if for any $(\mathcal{E}, \boldsymbol{s}, \boldsymbol{g}, \boldsymbol{t})$ and $(\overline{\mathcal{E}}, \overline{\boldsymbol{s}}, \overline{\boldsymbol{g}}, \overline{\boldsymbol{t}})$ where $\overline{\mathcal{E}}$ induces at most $|\mathcal{A}(\mathcal{E})|$ permisible skill patterns, the following holds if and only if $(\overline{\mathcal{E}}, \overline{\boldsymbol{s}}, \overline{\boldsymbol{g}}, \overline{\boldsymbol{t}})=$ $(\mathcal{E}, \boldsymbol{s}, \boldsymbol{g}, \boldsymbol{t})$ holds.

$$
\mathbb{P}(\mathbf{R}=r \mid \overline{\mathcal{E}}, \overline{\boldsymbol{s}}, \overline{\boldsymbol{g}}, \overline{\boldsymbol{t}})=\mathbb{P}(\mathbf{R}=r \mid \mathcal{E}, \boldsymbol{s}, \boldsymbol{g}, \boldsymbol{t}) \text { for all } r \in\{0,1\}^{J}
$$

We introduce some new notation before presenting the identifiability results. Following the definition in Gu and Xu (2022), we categorize the latent attributes into four different types: ancestor, intermediate, leaf, and singleton. An attribute is an "ancestor attribute" when it has a child but no parent attribute; an "intermediate attribute" when it has both a child and a parent; a "leaf attribute" when it has a parent but no child attribute; a "singleton attribute" when it has no child nor parent attribute. These definitions are illustrated in

Figure 4. Interestingly, the identifiability conditions of LCBN-based DINA model can be stated in terms of different types of the attributes in the hierarchy graph.
![img-3.jpeg](img-3.jpeg)

Figure 4: Illustrating all the four types of attributes in an attribute hierarchy graph.

Still following the definition in Gu and Xu (2022), we define a "sparsified" Q-matrix given $\mathcal{E}$ by setting $q_{j, k}=0$ for any $j, k$ such that $q_{j, h}=1$ for some child attribute $\alpha_{h}$ of $\alpha_{k}$.

Theorem 1. The LCBN-based DINA model is strictly identifiable when the $\mathbf{Q}$ and $\mathcal{E}$ satisfy the following conditions.
A. $\mathbf{Q}$ contains a $K \times K$ submatrix $\mathbf{Q}_{0}$ whose sparsified version under $\mathcal{E}$ is $I_{K}$. Without the loss of generality, write $\mathbf{Q}=\left[\mathbf{Q}_{0}^{\top}, \mathbf{Q}^{*\top}\right]^{\top}$.
B. In the sparsified version of $\mathbf{Q}$, any intermediate attribute is measured at least once, any ancestor or leaf attribute is measured at least twice, and any singleton attribute is measured at least three times.
C. For any singleton attributes $\alpha_{k}$ and $\alpha_{\ell}$, the $k$ th and lth columns of $\mathbf{Q}^{*}$ are different.

Theorem 1 is adapted from Theorem 2 in Gu and Xu (2022) to our LCBN-based model setting. In general, it is difficult to derive the necessary and sufficient conditions for identifiability of complicated models such as LCBN-based CDMs. Nevertheless, we next show our sufficient identifiability conditions in Theorem 1 may not be far from being necessary by considering a special hierarchy. The next proposition states that our conditions $A, B, C$ in Theorem 1 become the minimal requirement for identifiability under the linear hierarchy.

Proposition 1. Suppose $\mathcal{E}$ is a linear hiearchy, i.e. $\alpha_{1} \rightarrow \alpha_{2} \rightarrow \cdots \rightarrow \alpha_{K}$. Then, the conditions in Theorem 1 are necessary and sufficient for strict identifiability of an LCBNbased DINA model. In particular, conditions $B$ and $C$ reduce exactly to be:

$B^{\star}$. In the sparsified version of $\mathbf{Q}$, the leaf attribute and the ancestor attribute are each measured at least twice.

The proofs of Theorem 1 and Proposition 1, and additional identifiability results (sufficient conditions for strict and generic identifiability for LCBNs with other measurement models) are included in Sections S. 1 and S. 2 in the Supplementary Material.

# 4 Two-step Estimation Method for LCBN-based Cognitive Diagnostic Models 

This section proposes a two-step estimation method to recover both the attribute hierarchy graph $\mathcal{E}$ and the model parameters $(\boldsymbol{\Theta}, \boldsymbol{t})$. Our first step (Algorithm 1) uses a penalized EM algorithm under a saturated attribute model to estimate the graph $\mathcal{E}$, and our second step (Algorithm 2) develops another EM algorithm to estimate the continuous LCBN parameters.

We first write out the likelihood given the responses from a sample of $N$ students. Denote the response vectors for the $N$ students by $\mathbf{R}_{i}=\left(R_{i, 1}, \ldots, R_{i, J}\right)^{\top}$, for $i=1, \ldots, N$. The marginal likelihood under an LCBN-based cognitive diagnostic model is

$$
\begin{aligned}
L(\boldsymbol{\Theta}, \boldsymbol{t}, \mathcal{E}) & =\prod_{i=1}^{N}\left[\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} t_{k}{ }^{\alpha_{k} \prod_{l=1}^{K} \alpha_{t}^{G_{t, k}}}\left(1-t_{k}\right)^{\left(1-\alpha_{k}\right) \prod_{l=1}^{K} \alpha_{t}^{G_{t, k}}} \prod_{j=1}^{J} \theta_{j, \boldsymbol{\alpha}}^{R_{i, j}}\left(1-\theta_{j, \boldsymbol{\alpha}}\right)^{1-R_{i, j}}\right] \\
& =\prod_{i=1}^{N}\left[\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} p_{\boldsymbol{\alpha}} \prod_{j=1}^{J} \theta_{j, \boldsymbol{\alpha}}^{R_{i, j}}\left(1-\theta_{j, \boldsymbol{\alpha}}\right)^{1-R_{i, j}}\right]=: L(\boldsymbol{\Theta}, \boldsymbol{p})
\end{aligned}
$$

where the last line uses the equivalent parameterization of the mixture proportion parameters $\boldsymbol{p}=\left(p_{\boldsymbol{\alpha}} ; \boldsymbol{\alpha} \in\{0,1\}^{K}\right)$ instead of the LCBN parameters $\boldsymbol{t}$. Write the marginal log-likelihood as $\ell(\boldsymbol{\Theta}, \boldsymbol{t}, \mathcal{E})=\log L(\boldsymbol{\Theta}, \boldsymbol{t}, \mathcal{E})$ and $\ell(\boldsymbol{\Theta}, \boldsymbol{p})=\log L(\boldsymbol{\Theta}, \boldsymbol{p})$. We next describe the two steps of the proposed estimation procedure in Sections 4.1 and 4.2, respectively.

# 4.1 First step: structure learning of $\mathcal{E}$ via a penalized EM algorithm 

In the first step, we focus on estimating the discrete graph structure in an LCBN: the attribute hierarchy $\mathcal{E}$. Estimating $\mathcal{E}$ amounts to performing structure learning of a directed graphical model, and this graphical model is among the $K$ latent skills.

The key idea in learning $\mathcal{E}$ in an LCBN is to realize that, as an attribute hierarchy $\mathcal{E}$ naturally defines a set of permissible binary skill patterns $\mathcal{A}=\mathcal{A}(\mathcal{E})$, a set of permissible patterns $\mathcal{A}$ also allows for reconstructing an attribute hierarchy graph $\mathcal{E}=\mathcal{E}(\mathcal{A})$. Specifically, one can inversely infer $\mathcal{E}$ by examining the sparsity structure of $\boldsymbol{p}$. For a set of permissible patterns $\mathcal{A} \subseteq\{0,1\}^{K}$, we can read that $\alpha_{k}$ is a prerequisite for $\alpha_{\ell}$ if for any permissible pattern $\boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{K}\right) \in \mathcal{A}$, we have $\alpha_{\ell}=1$ holds only if $\alpha_{k}=1$ holds. In this way, we can define an attribute hierarchy graph $\mathcal{E}$ by collecting these prerequisite relationships:

$$
\mathcal{E}=\mathcal{E}(\mathcal{A})=\left\{k \rightarrow \ell: \text { if for any } \boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{K}\right) \in \mathcal{A}, \alpha_{\ell}=1 \text { only if } \alpha_{k}=1\right\}
$$

Example 6 (Example 4 continued). We revisit the attribute hierarchy $\mathcal{E}=\{1 \rightarrow 3,1 \rightarrow$ $4,2 \rightarrow 3,2 \rightarrow 4\}$ in Example 4 and show it can be recovered from the set of permissible patterns. First, we collect all the permissible patterns in $\mathcal{A}$ into a $|\mathcal{A}| \times K$ matrix denoted by $\mathbf{C}$. Each row of $\mathbf{C}$ corresponds to one pattern $\boldsymbol{\alpha} \in \mathcal{A}$ and each column corresponds to a skill. Then we compare the column vectors of $\mathbf{C}$ to obtain a partial order among the skills. For example, if $\mathbf{C}_{:, 1} \succeq \mathbf{C}_{:, 3}$ (the first column of $\mathbf{C}$ is elementwisely greater than or equal to the third column of $\mathbf{C}$ ), then it means for all the permissible skill patterns, attribute $\alpha_{3}$ is present only if attribute $\alpha_{1}$ is present; this indicates $1 \rightarrow 3$. In the current toy example, such

a procedure gives the following reconstruction of the hierarchy $\mathcal{E}$.

To estimate $\mathcal{E}$, now the problem boils down to estimating $\mathcal{A}$. To this end, we leverage the log penalty and penalized EM algorithm proposed in Gu and Xu (2019) for selecting significant latent patterns. Consider the truncated log function

$$
\log _{\rho_{N}}\left(p_{\boldsymbol{\alpha}}\right)=\log \left(p_{\boldsymbol{\alpha}}\right) \cdot \mathbb{1}\left(p_{\boldsymbol{\alpha}}>\rho_{N}\right)+\log \left(\rho_{N}\right) \cdot \mathbb{1}\left(p_{\boldsymbol{\alpha}} \leq \rho_{N}\right)
$$

where $\rho_{N}$ is a small threshold that avoids the singularity issue of the log function at zero. The penalized marginal $\log$ likelihood $\ell^{\lambda}(\boldsymbol{\Theta}, \boldsymbol{p})$ is defined as

$$
\ell^{\lambda}(\boldsymbol{\Theta}, \boldsymbol{p})=\ell(\boldsymbol{\Theta}, \boldsymbol{p})+\lambda \sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \log _{\rho_{N}}\left(p_{\boldsymbol{\alpha}}\right)
$$

where $\lambda<0$ is a tuning parameter controlling the sparsity of $\boldsymbol{p}$. We maximize $\ell^{\lambda}(\boldsymbol{\Theta}, \boldsymbol{p})$ instead of the original marginal $\log$ likelihood $\ell(\boldsymbol{\Theta}, \boldsymbol{p})$ using the Penalzed EM (PEM) algorithm in Gu and Xu (2019). We restate this algorithm in Algorithm 1. A smaller tuning parameter $\lambda$ (i.e. larger $-\lambda=|\lambda|>0$ ) leads to a stronger penalty and encourages a sparser $\boldsymbol{p}$.

Remark 1. One main reason for choosing the log penalty on the proportion parameters $\boldsymbol{p}$ over other popular sparsity-inducing penalties is computational convenience. Among sparsityinducing penalties, the $L_{0}$ penalty is the most direct one that penalizes the number of nonzero entries. Although $L_{0}$ penalty encourages sparsity and theoretically leads to consistent selection, it is computationally inefficient due to its discontinuous and nonconvex nature (Liu and $W u$, 2007). There exist various attempts to replace the $L_{0}$ penalty with a similar but more

tractable objective. One such example is the popular $L_{1}$ (Lasso, Tibshirani, 1996) penalty. But actually, Lasso turns out to not induce any sparsity on our proportion parameters $\boldsymbol{p}$ because

$$
\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}}\left|p_{\boldsymbol{\alpha}}\right|=\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} p_{\boldsymbol{\alpha}}=1
$$

for any $\boldsymbol{p}$. Similarly, elastic net regularization (Zou and Hastie, 2005) also cannot induce sparsity in our setting.

Compared to the aforementioned penalties, the log penalty proposed by Gu and Xu (2019) is preferable as it not only induces nice sparsity on $\boldsymbol{p}$, but also allows for efficient and explicit M-step updates for $\boldsymbol{p}$ in an EM algorithm. This follows from the fact that the log penalty can be alternatively viewed as a Dirichlet prior for $\boldsymbol{p}$, which is a conjugate prior for the complete data log likelihood:

$$
\begin{aligned}
& \ell_{c}(\boldsymbol{\Theta}, \boldsymbol{p} \mid \mathbf{A})=\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \sum_{i=1}^{N} \mathbb{1}\left(\mathbf{A}_{i}=\boldsymbol{\alpha}\right) \log \left(p_{\boldsymbol{\alpha}}\right) \\
& \quad+\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \sum_{i=1}^{N} \mathbb{1}\left(\mathbf{A}_{i}=\boldsymbol{\alpha}\right) \sum_{j=1}^{J}\left[R_{i, j} \log \left(\theta_{j, \boldsymbol{\alpha}}\right)+\left(1-R_{i, j}\right) \log \left(1-\theta_{j, \boldsymbol{\alpha}}\right)\right]
\end{aligned}
$$

For more discussions on the connection between the log penalty and the Dirichlet prior in a Bayesian context, please see Remark 12 in Gu and Xu (2019).

We denote the estimator of the item parameters by $\boldsymbol{\Theta}^{\lambda}$ and that of the mixture proportion parameters by $\boldsymbol{p}^{\lambda}=\left(p_{\boldsymbol{\alpha}}^{\lambda} ; \boldsymbol{\alpha} \in\{0,1\}^{K}\right)$. Further, we define the following estimated set of existing skill patterns:

$$
\mathcal{A}^{\lambda}=\left\{\boldsymbol{\alpha} \in\{0,1\}^{K}: p_{\boldsymbol{\alpha}}^{\lambda}>\rho_{N}\right\}
$$

that is, $\mathcal{A}^{\lambda}$ collects those skill patterns with estimated proportions greater than the threshold $\rho_{N}$. This $\mathcal{A}^{\lambda}$ is the key quantity that would give an estimate of the attribute hierarchy $\mathcal{E}^{\lambda}$.

We consider a sequence of values for $\lambda$ and select an optimal value based on the Extended Bayesian Information Criterion (EBIC, Chen and Chen, 2008):

$$
\mathrm{EBIC}_{\lambda}=-2 \ell\left(\boldsymbol{\Theta}^{\lambda}, \boldsymbol{p}^{\lambda}\right)+\left(m_{\boldsymbol{p}}^{\lambda}+m_{\boldsymbol{\Theta}}\right) \log N+2 \log \binom{2^{K}-1+m_{\boldsymbol{\Theta}}}{m_{\boldsymbol{p}}^{\lambda}+m_{\boldsymbol{\Theta}}}, \quad m_{\boldsymbol{p}}^{\lambda}=\left|\mathcal{A}^{\lambda}\right|-1
$$

In the above display, $m_{\boldsymbol{p}}^{\lambda}$ denotes the number of free parameters in the proportions $\boldsymbol{p}^{\lambda}$ and $m_{\boldsymbol{\Theta}}$ denotes the number of free parameters in the item parameters $\boldsymbol{\Theta}^{\lambda}$ (for example, $m_{\boldsymbol{\Theta}}=2 J$ for the DINA model, and $m_{\boldsymbol{\Theta}}=\sum_{j=1}^{J} 2^{\sum_{k^{\prime}=1}^{K} q_{j, k^{\prime}}}$ for the GDINA model). Then we select the optimal tuning parameter $\widehat{\lambda}$ that minimizes the $\mathrm{EBIC}_{\lambda}$ :

$$
\widehat{\lambda}=\arg \min _{\lambda} \mathrm{EBIC}_{\lambda}
$$

Compared to BIC, EBIC has an additional penalty term for the number of selected parameters and hence favors a more parsimonious model. EBIC has been used in related existing works (Gu and Xu, 2019; Ma et al., 2023), and it also turns out to be especially useful for estimating $\mathcal{E}$ in LCBNs. In fact, our simulations suggest that the stronger penalty in EBIC is desirable because overselecting non-existing patterns often leads to error in estimating the graph $\mathcal{E}$, whereas underselecting truly existing patterns can sometimes still suffice for correctly estimating $\mathcal{E}$ (see Section 5). In addition, other popular criteria for model selection such as cross-validation (whose goal is to minimize the prediction error) is not suitable for selecting $\lambda$ here, because it does not take the model sparsity into account. In fact, in preliminary simulations we have found that cross-validation tends to select a larger $\lambda<0$ with a smaller magnitude than needed, hence resulting in selecting a not sparse enough model. We present such a simulation study in Supplementary Material S.4.2.

Finally, given the estimated set of permissible patterns $\mathcal{A}^{\widehat{\lambda}}$, we now define our estimate of the attribute hierarchy graph $\mathcal{E}$ following (13):

$$
\widetilde{\mathcal{E}}=\left\{k \rightarrow \ell: \text { if for any } \boldsymbol{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{K}\right) \in \mathcal{A}^{\widehat{\lambda}}, \alpha_{\ell}=1 \text { only if } \alpha_{k}=1\right\}
$$

Next, we show that our estimator $\widetilde{\mathcal{E}}$ is statistically consistent under suitable conditions. We consider the conventional asymptotic setting where the sample size $N$ goes to infinity, but the number of skills $K$ and the number of items $J$ are fixed. Following the assumption in Gu and Xu (2019), we also assume that the convergence rate of the MLE satisfies

$$
\frac{\ell(\widehat{\boldsymbol{\Theta}}, \widehat{\boldsymbol{p}})-\ell\left(\widehat{\boldsymbol{\Theta}}^{\mathcal{E}}, \widehat{\boldsymbol{p}}^{\mathcal{E}}\right)}{N}=O_{p}\left(N^{-\delta}\right)
$$

for some $\delta \in(0,1]$. Here, $(\widehat{\boldsymbol{\Theta}}, \widehat{\boldsymbol{p}})$ is the MLE obtained from maximizing $L(\boldsymbol{\Theta}, \boldsymbol{p})$ in (12) and

$\left(\widehat{\boldsymbol{\Theta}}^{\mathcal{E}}, \widehat{\boldsymbol{p}}^{\mathcal{E}}\right)$ is the oracle MLE assuming that the true hierarchy $\mathcal{E}$ is known. Similar to Gu and Xu (2019), we impose this assumption because the convergence rate of the MLE with an unknown hierarchy (or equivalently, an unknown number of mixture components $|\mathcal{A}|$ ) can be slower than the usual parametric rate with $\delta=1$ (Ho and Nguyen, 2016). The following theorem shows the consistency conclusion.

Theorem 2. Consider an identifiable LCBN-based CDM with parameters $(\boldsymbol{\Theta}, \boldsymbol{t}, \mathcal{E})$. Suppose the item parameter $\Theta$ satisfies

$$
\theta_{j, \mathbf{1}}-\max _{\boldsymbol{\alpha} \not \leq \boldsymbol{q}_{j}} \theta_{j, \boldsymbol{\alpha}} \geq c, \quad \forall j \in[J]
$$

for a constant $c>0$, and (15) holds. Let the threshold be $\rho_{N}=O\left(N^{-\delta}\right)$. Then, for any sequence $\left\{\lambda_{N}\right\}$ satisfying $\frac{N^{1-\delta}}{\left\lceil\log \rho_{N}\right\rceil} \lesssim-\lambda_{N} \lesssim \frac{N}{\left\lceil\log \rho_{N}\right\rceil}$, we can consistently estimate the attribute hierarchy $\mathbf{P}\left(\widehat{\mathcal{E}}^{\lambda_{N}}=\mathcal{E}\right) \rightarrow 1$ as $N \rightarrow \infty$. Here, $\widehat{\mathcal{E}}^{\lambda_{N}}$ is the estimated hierarchy based on $\mathcal{A}^{\lambda_{N}}$.

Theorem 2 also provides theoretical guidelines on choosing the tuning parameters. In particular, we choose $\rho_{N}=\frac{1}{2 N}$ so that it satisfies the condition in Theorem 2 for any $\delta$.

In addition to the above estimation consistency result for the attribute hierarchy, one could further quantify uncertainty via formal hypothesis testing. Specifically, we can consider testing the null hypothesis $H_{0}: \mathcal{E}=\widehat{\mathcal{E}}$ using additional response data, where $\widehat{\mathcal{E}}$ is the estimated attribute hierarchy. To this end, one may conduct standard goodness of fit tests such as the likelihood ratio test with a $\chi^{2}$ asymptotic reference distribution. We leave the detailed development of such hypothesis testing procedures for future research.

# 4.2 Second step: parameter estimation of $(\boldsymbol{\Theta}, \boldsymbol{p})$ via another EM algorithm 

We next propose another EM algorithm to estimate the continuous LCBN parameters $\boldsymbol{t}$ and $\boldsymbol{\Theta}$. The previous Algorithm 1 does not take into account the LCBN structure, but merely focuses on estimating which skill patterns have nonzero proportions in the student population. Importantly, note that although the hierarchy graph $\widehat{\mathcal{E}}$ can be read off from the sparsity structure of $\widehat{\boldsymbol{p}}^{\lambda}$, the LCBN parameters $\boldsymbol{t}$ cannot be read off from the estimated proportion parameters $\boldsymbol{p}$. This is because the latter is an overparametrization of the former,

```
Algorithm 1: Penalized EM to learn the attribute hierarchy graph \(\mathcal{E}\)
(Algorithm 1 in Gu and Xu (2019))
```

Data: Q-matrix $\mathbf{Q}=\left(q_{j, k}\right)$, response vectors $\left(\mathbf{R}_{1}^{\top}, \ldots, \mathbf{R}_{N}^{\top}\right)^{\top}$.
Initialize $\boldsymbol{\Delta}=\left(\Delta_{\boldsymbol{\alpha}}: \boldsymbol{\alpha} \in\{0,1\}^{K}\right)$ from the $\left(2^{K}-1\right)$-dimensional probability
simplex.
while not converged do
In the $(t+1)$ th iteration,
for $(i, \boldsymbol{\alpha}) \in[N] \times\{0,1\}^{K}$ do

$$
\varphi_{i, \boldsymbol{\alpha}}^{(t+1)}=\frac{\delta_{\boldsymbol{\alpha}}^{(t)} \cdot \exp \left\{\sum_{j=1}^{J}\left[R_{i, j} \log \left(\theta_{j, \boldsymbol{\alpha}}^{(t)}\right)+\left(1-R_{i, j}\right) \log \left(1-\theta_{j, \boldsymbol{\alpha}}^{(t)}\right)\right]\right\}}{\sum_{\boldsymbol{\alpha}^{\prime} \in\{0,1\}^{K}} \delta_{\boldsymbol{\alpha}^{\prime}}^{(t)} \cdot \exp \left\{\sum_{j=1}^{J}\left[R_{i, j} \log \left(\theta_{j, \boldsymbol{\alpha}^{\prime}}^{(t)}\right)+\left(1-R_{i, j}\right) \log \left(1-\theta_{j, \boldsymbol{\alpha}^{\prime}}^{(t)}\right)\right]\right\}}
$$

for $\boldsymbol{\alpha} \in\{0,1\}^{K}$ do
$\delta_{\boldsymbol{\alpha}}^{(t+1)}=\max \left\{c, \lambda+\sum_{i=1}^{N} \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}\right\} ; \quad(c>0$ is a pre-specified small constant, set to $c=0.01$ throughout the experiments following the suggestion of Gu and $\mathrm{Xu}(2019))$
$\boldsymbol{p}^{(t+1)} \leftarrow \boldsymbol{\delta}^{(t+1)} /\left(\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \delta_{\boldsymbol{\alpha}}^{(t+1)}\right)$
for $j \in[J]$ do

$$
\begin{aligned}
& \boldsymbol{\Theta}_{j}^{(t+1)}= \\
& \quad \arg \max _{\boldsymbol{\Theta}_{j}}\left\{\sum_{\boldsymbol{\alpha}} \sum_{i} \varphi_{i, \boldsymbol{\alpha}}^{(t+1)} \sum_{j}\left[R_{i, j} \log \left(\theta_{j, \boldsymbol{\alpha}}^{(t)}\right)+\left(1-R_{i, j}\right) \log \left(1-\theta_{j, \boldsymbol{\alpha}}^{(t)}\right)\right]\right\}
\end{aligned}
$$

After convergence, use $\mathcal{A}^{\lambda}, \boldsymbol{\Theta}^{\lambda}, \boldsymbol{p}^{\lambda}$ to calculate the EBIC for a sequence of $\lambda<0$.
Select $\widehat{\lambda}$ with the minimum EBIC and recover the hierarchy structure $\mathcal{E}^{\widehat{\lambda}}$ from $\mathcal{A}^{\widehat{\lambda}}$.
Output: Attribute hierarchy $\mathcal{E}$.
and it is not guaranteed that a freely estimated $\boldsymbol{p}$ will correspond to a $K$-dimensional LCBN parameters $\boldsymbol{t}=\left(t_{1}, \ldots, t_{K}\right)$.

We next propose another EM algorithm to re-estimate the continuous parameters in LCBN-based cognitive diagnostic models given $\widehat{\mathcal{E}}$. For each individual $i=1, \ldots, N$, denote their latent skill profile by $\mathbf{A}_{i}=\left(A_{i, 1}, \ldots, A_{i, K}\right)$. We maximize the likelihood in (12) with respect to $(\boldsymbol{t}, \boldsymbol{\Theta})$ when holding $\mathcal{E}=\widehat{\mathcal{E}}$ fixed. The $\log$ likelihood for the complete data $\left(\mathbf{A}_{i}, \mathbf{R}_{i}\right)$, $i=1, \ldots, N$ takes the following form:

$$
\ell_{e}(\boldsymbol{\Theta}, \boldsymbol{t} \mid \mathcal{E})=\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \sum_{i=1}^{N} \mathbb{1}\left(\mathbf{A}_{i}=\boldsymbol{\alpha}\right) \prod_{k=1}^{K}\left[t_{k}^{\alpha_{k}} \Pi_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}}\left(1-t_{k}\right)^{\left(1-\alpha_{k}\right) \Pi_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}}}\right]
$$

$$
+\sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \sum_{i=1}^{N} \mathbb{1}\left(\mathbf{A}_{i}=\boldsymbol{\alpha}\right) \sum_{j=1}^{J}\left[R_{i, j} \log \left(\theta_{j, \boldsymbol{\alpha}}\right)+\left(1-R_{i, j}\right) \log \left(1-\theta_{j, \boldsymbol{\alpha}}\right)\right]
$$

Recall that the prerequisite relationships in $\mathcal{E}$ completely define the reachability matrix entries $G_{\ell, k}=\mathbb{1}(\ell \rightarrow k)$ in the above expression. So the only things that vary in (17) are $(\boldsymbol{\Theta}, \boldsymbol{t})$.

In the E-step, we evaluate the conditional expectation of (17) given the current parameter values $\boldsymbol{\Theta}^{(t)}$ and $\boldsymbol{t}^{(t)}$ from the previous iteration. It suffices to evaluate the conditional probability of $\mathbb{1}\left(\mathbf{A}_{i}=\boldsymbol{\alpha}\right)$, denoted by $\varphi_{i, \boldsymbol{\alpha}}=\mathbb{P}\left(\mathbf{A}_{i}=\boldsymbol{\alpha} \mid \boldsymbol{\Theta}^{(t)}, \boldsymbol{t}^{(t)}\right)$. See the detailed formula for $\varphi_{i, \boldsymbol{\alpha}}$ in Algorithm 2. Then we obtain the following function of $(\boldsymbol{\Theta}, \boldsymbol{t})$ :

$$
Q\left(\boldsymbol{\Theta}, \boldsymbol{t} \mid \boldsymbol{\Theta}^{(t)}, \boldsymbol{t}^{(t)}\right)=\mathbb{E}\left[\ell_{c}(\boldsymbol{\Theta}, \boldsymbol{t} \mid \mathcal{E}) \mid \boldsymbol{\Theta}^{(t)}, \boldsymbol{t}^{(t)}\right]
$$

Next, in the M-step, we seek the maximiziers of the above function and obtain new estimates of the model parameters:

$$
\left(\boldsymbol{\Theta}^{(t+1)}, \boldsymbol{t}^{(t+1)}\right)=\arg \max _{\boldsymbol{\Theta}, \boldsymbol{t}} Q\left(\boldsymbol{\Theta}, \boldsymbol{t} \mid \boldsymbol{\Theta}^{(t)}, \boldsymbol{t}^{(t)}\right)
$$

Every parameter in $(\boldsymbol{\Theta}, \boldsymbol{t})$ is continuous, so we set the partial derivative with respect to each of them to zero to seek $\left(\boldsymbol{\Theta}^{(t+1)}, \boldsymbol{t}^{(t+1)}\right)$. Because $\log t_{k}$ and $\log \left(1-t_{k}\right)$ are the only terms in $Q\left(\boldsymbol{\Theta}, \boldsymbol{t} \mid \boldsymbol{\Theta}^{(t)}, \boldsymbol{t}^{(t)}\right)$ that depend on $t_{k}$, we have a closed-form update of each $t_{k}$ as follows:

$$
t_{k}^{(t+1)}=\frac{\sum_{i=1}^{N} \sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \alpha_{k} \prod_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}} \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}{\sum_{i=1}^{N} \sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}} \prod_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}} \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}
$$

As long as we have $\boldsymbol{t}^{(t+1)}$, we can easily update the mixture proportion parameters $\boldsymbol{p}^{(t+1)}=$ $\left(p_{\boldsymbol{\alpha}}^{(t+1)}\right)$ for the permissible skill patterns by following the definition in (8). As for the item parameters $\boldsymbol{\Theta}$, we also have closed form updates under some very popular measurement models such as the DINA and GDINA model. For example, under the DINA model in (1) where $\boldsymbol{\Theta}$ collects the slipping and guessing parameters $\boldsymbol{s}$ and $\boldsymbol{g}$, the closed form updates are:

$$
s_{j}^{(t+1)}=1-\frac{\sum_{i} \sum_{\boldsymbol{\alpha}} R_{i, j} \mathbb{1}\left(\boldsymbol{\alpha} \succeq \boldsymbol{q}_{j}\right) \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}{\sum_{i} \sum_{\boldsymbol{\alpha}} \mathbb{1}\left(\boldsymbol{\alpha} \succeq \boldsymbol{q}_{j}\right) \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}, \quad g_{j}^{(t+1)}=\frac{\sum_{i} \sum_{\boldsymbol{\alpha}} R_{i, j} \mathbb{1}\left(\boldsymbol{\alpha} \nsucc \boldsymbol{q}_{j}\right) \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}{\sum_{i} \sum_{\boldsymbol{\alpha}} \mathbb{1}\left(\boldsymbol{\alpha} \nsucc \boldsymbol{q}_{j}\right) \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}
$$

As for the GDINA model, we present the closed-form parameter updates in Section S. 3 of the Supplementary Material. For LCBNs with certain measurement models such as the main-effect CDMs, there does not exist closed form updates for $\boldsymbol{\Theta}$. In this case, one can just perform a gradient-ascent step for $\boldsymbol{\Theta}$ that increases $Q\left(\boldsymbol{\Theta}, \boldsymbol{t} \mid \boldsymbol{\Theta}^{(t)}, \boldsymbol{t}^{(t)}\right)$ in (18) instead of finding the exact maximizer. Alternatively, one can also apply existing optimization solvers to find an approximate maximizer of $Q\left(\boldsymbol{\Theta}, \boldsymbol{t} \mid \boldsymbol{\Theta}^{(t)}, \boldsymbol{t}^{(t)}\right)$.

```
Algorithm 2: EM to estimate LCBN parameters.
    Data: Q-matrix Q, response patterns \(\left\{\mathbf{R}_{i}: i=1, \ldots, N\right\}\) , attribute hierarchy \(\mathcal{E}\).
    Initialize \(\boldsymbol{t}=\left(t_{1}, \ldots, t_{K}\right), \boldsymbol{\Theta}\) (subject to the constraints of the Q-matrix), and G.
    while not converged do
        In the \((t+1)\) th iteration:
        for \(\boldsymbol{\alpha} \in \mathcal{A}\) do
            \(\boldsymbol{p}_{\boldsymbol{\alpha}}^{(t+1)}=\prod_{k=1}^{K}\left(t_{k}^{(t)}\right)^{\alpha_{k} \Pi_{\ell} \alpha_{\ell}^{G_{\ell, k}}}\left(1-t_{k}^{(t)}\right)^{\left(1-\alpha_{k}\right) \Pi_{\ell} \alpha_{l}^{G_{\ell, k}}} ;\)
    for \((i, \boldsymbol{\alpha}) \in[N] \times \mathcal{A}(\mathcal{E})\) do
        \(\varphi_{i, \boldsymbol{\alpha}}^{(t+1)}=\frac{\boldsymbol{p}_{\boldsymbol{\alpha}}^{(t)} \cdot \exp \left\{\sum_{j=1}^{J}\left[R_{i, j} \log \left(\theta_{j, \boldsymbol{\alpha}}^{(t)}\right)+\left(1-R_{i, j}\right) \log \left(1-\theta_{j, \boldsymbol{\alpha}}^{(t)}\right)\right]\right\}}{\sum_{\boldsymbol{\alpha}^{\prime} \in \mathcal{A}(\mathcal{E})} \boldsymbol{p}_{\boldsymbol{\alpha}^{\prime}}^{(t)} \cdot \exp \left\{\sum_{j=1}^{J}\left[R_{i, j} \log \left(\theta_{j, \boldsymbol{\alpha}^{\prime}}^{(t)}\right)+\left(1-R_{i, j}\right) \log \left(1-\theta_{j, \boldsymbol{\alpha}^{\prime}}^{(t)}\right)\right]\right\}} ;\)
    for \(k \in[K]\) do
        \(t_{k}^{(t+1)}=\frac{\sum_{i, \boldsymbol{\alpha}} \alpha_{k} \prod_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}} \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}{\sum_{i, \boldsymbol{\alpha}} \prod_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}} \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}\);
    for \(j \in[J]\) do
        \(\boldsymbol{\Theta}_{j}^{(t+1)}=\)
        \(\arg \max _{\boldsymbol{\Theta}_{j}}\left\{\sum_{\boldsymbol{\alpha}} \sum_{i} \varphi_{i, \boldsymbol{\alpha}}^{(t+1)} \sum_{j}\left[R_{i, j} \log \left(\theta_{j, \boldsymbol{\alpha}}^{(t)}\right)+\left(1-R_{i, j}\right) \log \left(1-\theta_{j, \boldsymbol{\alpha}}^{(t)}\right)\right]\right\}\);
```

After the total $T$ iterations,
Output: Estimated parameters $\boldsymbol{t}, \boldsymbol{\Theta}$.

In the following theorem, we show that our two-stage estimation procedure based on Algorithms 1 and 2 enjoys consistent estimation of not only the attribute hierarchy graph, but also the continuous parameters.

Theorem 3. Consider an identifiable LCBN-based CDM with parameters $(\boldsymbol{\Theta}, \boldsymbol{t}, \mathcal{E})$, and

suppose that the conditions in Theorem 2 hold. Let $\widehat{\mathcal{E}}$ be the hierarchy estimated from Algorithm 1, and let $\left(\widehat{\boldsymbol{\Theta}}_{N}, \widehat{\boldsymbol{t}}_{N}\right)$ be the maximum likelihood estimator of $(\boldsymbol{\Theta}, \boldsymbol{t})$ given $\widehat{\mathcal{E}}$. Then, $\left(\widehat{\boldsymbol{\Theta}}_{N}, \widehat{\boldsymbol{t}}_{N}\right)$ are consistent, i.e. entries in $\left(\widehat{\boldsymbol{\Theta}}_{N}, \widehat{\boldsymbol{t}}_{N}\right)$ converge to corresponding entries in $(\boldsymbol{\Theta}, \boldsymbol{t})$ in probability as $N \rightarrow \infty$.

# 4.3 Estimation under unknown Q 

In the previous subsections, we have focused on estimating the LCBN parameters assuming a known and fixed Q-matrix. This is a common assumption in cognitive diagnostic assessments, because domain experts and test designers often have specified how the test items depend on the latent attributes. But sometimes it is of interest to estimate the Q-matrix directly from data together with other model parameters. Our two-step estimation procedure for LCBNs can be readily extended to such unknown Q-matrix settings by leveraging existing Q-matrix estimation methods for traditional CDMs. We next briefly describe how the exploratory estimation method in Ma et al. (2023) can be incorporated into our LCBN estimation procedure with an unknown $K, \mathbf{Q}$, and $\mathcal{E}$.

We briefly sketch the method proposed by Ma et al. (2023) in Algorithm 3. This algorithm includes an additional truncated Lasso penalty (TLP; Shen et al., 2012) term on the item parameter matrix $\boldsymbol{\Theta}$ to encourage row-wise sparsity. Consequently, the Q-matrix is recovered by inspecting the sparsity structure of $\boldsymbol{\Theta}$. The attribute hierarchy $\mathcal{E}$ is estimated by comparing the partial orders of the columns of $\boldsymbol{\Theta}$, and assigning binary representations to these columns as attribute patterns. This Algorithm 3 can serve as our new first step in the two-step estimation procedure. Given the estimated $\mathbf{Q}$-matrix and $\mathcal{E}$, we can then apply our proposed Algorithm 2 to estimate the continuous LCBN parameters: $\boldsymbol{t}$ and $\boldsymbol{\Theta}$. We present simulation study results in Supplementary Material S.4.4 that demonstrate the good performance of the above estimation method.

## 5 Simulation Studies

In this section, we conduct simulation studies under different models and parameter settings to assess the performance of our proposed method.

```
Algorithm 3: Estimate \(K\) and discrete structures \(\mathbf{Q}\) and \(\mathcal{E}\)
(Brief sketch of Algorithms 1 and 2 in Ma et al. (2023))
    Data: Responses \(\left(\mathbf{R}_{1}^{\top}, \ldots, \mathbf{R}_{N}^{\top}\right)^{\top}\).
    Set an upper bound for \(|\mathcal{A}|\), the number of latent configurations
    Step 1: Use penalized EM assuming sparsity of \(\boldsymbol{p}\) and \(\boldsymbol{\Theta}\) to estimate \(\boldsymbol{\Theta}\) and \(|\mathcal{A}|\)
    Step 2: Construct the \(J \times|\mathcal{A}|\) indicator matrix \(\Gamma=\mathbb{1}\left(\theta_{j, m}=\max _{l \in[|\mathcal{A}||} \theta_{j, l}\right)\)
    Step 3: Plot a DAG based on the partial orders of the columns of \(\Gamma\)
    Step 4: Assign binary representations bassed on this DAG and recover \(K\) and \(\mathcal{E}\)
    Step 5: Reconstruct each rows of \(\mathbf{Q}\) based on the corresponding row of the \(\Gamma\) matrix
    Output: Number of latent attributes \(K\), Hierarchy structure \(\mathcal{E}, \mathbf{Q}\)-matrix \(\mathbf{Q}\)
```


# 5.1 Parameter estimation of the LCBN-based DINA and GDINA models 

We consider the LCBN-based DINA and GDINA models (see Examples 1 and 3 for the definition of DINA and GDINA models) with $K=8$ latent attributes and $J=24$ items. The Q-matrix takes the following form:

$$
\mathbf{Q}=\left(\begin{array}{l}
\mathbf{Q}_{1} \\
\mathbf{Q}_{2} \\
\mathbf{I}_{K}
\end{array}\right), \quad \text { where } \mathbf{Q}_{1}=\left(\begin{array}{cccc}
1 & 1 & & 0 \\
1 & \ddots & \ddots & & \\
& \ddots & \ddots & 1 \\
0 & & 1 & 1
\end{array}\right)_{K \times K} \quad \text { and } \mathbf{Q}_{2}=\left(\begin{array}{cccc}
1 & 1 & & 0 \\
& \ddots & \ddots & & \\
& & \ddots & 1 \\
0 & & & 1
\end{array}\right)_{K \times K}
$$

Note that $K=8$ is already a relatively large number of attributes in the educational cognitive diagnosis applications.

In all of our simulations, we specify the true hierarchy $\mathcal{E}$ to be the diamond hierarchy defined in Figure 5. This is a complex multi-layer hierarchy which encodes $|\mathcal{A}(\mathcal{E})|=15$ permissible patterns. We set the true LCBN parameters as $\boldsymbol{t}=(0.9,0.8,0.8,0.7,0.7,0.7,0.6,0.6)^{\top}$. Following the definition in (8), we can obtain the mixture proportion parameters for the permissible skill patterns. All the permissible patterns indexed by $\boldsymbol{\alpha}_{1}, \ldots, \boldsymbol{\alpha}_{15}$ and their corresponding true proportion parameters are presented in Table 2.

We vary the following three aspects in the simulation studies: (1) measurement model: DINA and GDINA; (2) sample size $N=500,1000,2000$; and (3) noise level of item parameters. In the LCBN-based DINA model, we use a noise level $r$ to define the slipping and

guessing parameters $\boldsymbol{s}, \boldsymbol{g}$ by

$$
s_{j}=g_{j}=r \text { for all } j=1, \ldots, J
$$

The larger the noise level $r$ is, the more uncertain one's responses are, and the more challenging it is to estimate the model parameters. Specifically, under DINA, if $r=0$ then there is no uncertainty in one's responses given their latent skills, whereas if $r=0.5$ the responses are purely random noise. For the LCBN-based GDINA model, we set the positive response probability of the all-zero skill pattern to $r$ and that of the all-one skill pattern to $1-r$ (i.e., $\theta_{j, \mathbf{0}_{K}}=r$ and $\theta_{j, \mathbf{1}_{K}}=1-r$ ); then we define the remaining item parameters by setting all main effects and interaction effects of the required attributes in (5) to be equal.

In each simulation setting, we run 100 independent simulation replications. We apply our two-step estimation method described in Section 4. The tuning parameter $\lambda$ in Algorithm 1 (PEM algorithm) is selected from a grid of ten values $\lambda \in\{-0.4,-0.8, \ldots,-3.6,-4.0\}$. We evaluate the root mean squared errors (RMSE) of the continuous parameters and also the estimation accuracy of the permissible patterns in $\mathcal{A}$ (this is same as the estimation accuracy of the hierarchy $\mathcal{E}$ ). The RMSE of the proportion parameters $\widehat{\boldsymbol{p}}$ is computed using the $2^{K}$-dimensional sparse vector in the probability simplex, i.e. for $C=100$ simulations,

$$
\operatorname{RMSE}(\widehat{\boldsymbol{p}})=\sqrt{\frac{1}{2^{K} C} \sum_{c=1}^{C} \sum_{\boldsymbol{\alpha} \in\{0,1\}^{K}}\left(\widehat{p}_{\boldsymbol{\alpha}}^{(c)}-p_{\boldsymbol{\alpha}}\right)^{2}}
$$

where $\widehat{\boldsymbol{p}}^{(c)}=\left(\widehat{p}_{\boldsymbol{\alpha}}^{(c)}\right)$ denotes the estimator from the $c$ th simulation replicate. We sum over all $\boldsymbol{\alpha} \in\{0,1\}^{K}$ instead of $\boldsymbol{\alpha} \in \mathcal{A}$ in order to compute an accurate RMSE even when the estimated $\widehat{\mathcal{A}}$ is incorrect. The RMSE of the item parameters under DINA is calculated as

$$
\operatorname{RMSE}(\widehat{\boldsymbol{\Theta}})=\sqrt{\frac{1}{2 J C} \sum_{c=1}^{C} \sum_{j=1}^{J}\left[\left(\widehat{s_{j}}^{(c)}-s_{j}\right)^{2}+\left(\widehat{g_{j}}^{(c)}-g_{j}\right)^{2}\right]}
$$

The RMSEs for the GDINA item parameters and the LCBN parameters $\boldsymbol{t}$ are similarly

defined. The estimation accuracy of $\mathcal{E}$ is defined as

$$
\operatorname{Acc}(\widehat{\mathcal{E}})=\frac{1}{C} \sum_{c=1}^{C} \mathbb{1}\left(\widehat{\mathcal{E}}^{(c)}=\mathcal{E}\right)
$$

where $\widehat{\mathcal{E}}^{(c)}=\mathcal{E}$ indicates that the entire hierarchy is exactly recovered. We also compare our final estimated model (denoted by LCBN in the table) to the first-stage estimate (denoted by PEM in the table) by comparing their EBIC values. The simulation results for the LCBN-based DINA and GDINA are summarized in Tables 3 and 4, respectively. The "argmin EBIC" column in Table 3 (or 4) records the percentage of each method (PEM or our two-step procedure) that achieves the minimum EBIC value among the 100 simulation replicates. We report additional simulation details (convergence criteria and the choice of tuning parameters) and computation time in Supplementary Material S.4.1.
![img-4.jpeg](img-4.jpeg)

Figure 5: Diamond hierarchy.


Table 2: Permissible patterns under the diamond hierarchy

Tables 3 and 4 show that our method is effective in recovering the attribute hierarchy

$\mathcal{E}$. In particular, the recovery accuracy improves as the signal-to-noise ratio increases, i.e. as the sample size $N$ increases and noise level $r$ decreases. In particular, when $N$ is large $(N=2000), \operatorname{Acc}(\widehat{\mathcal{E}})$ is above 0.97 in all of our simulation settings. This observation empirically verifies the identifiability and estimation consistency of $\mathcal{E}$. The accuracy of recovering the hierarchy $\mathcal{E}$ in Tables 3 and 4 is close to $90 \%$ or higher in all scenarios except for the slightly lower values of $74 \%$ and $52 \%$ when $N=500$ and $r=0.2$. These two lower accuracy values correspond to the smallest signal-to-noise settings under DINA and GDINA models. Additionally, the estimation accuracy under GDINA is lower than that under DINA, as it has more item parameters that need to be estimated (in our settings, GDINA has 108 parameters whereas DINA has 48 parameters).

Table 3: Estimation accuracy of attribute hierarchy and RMSE for the estimated parameters for the DINA-based LCBN. The "argmin EBIC" column shows the percentage of each method (PEM or proposed) having a smaller EBIC among the 100 simulation replications.


We also observe that the first-step Algorithm 1 alone can sometimes under-select the skill patterns when applied to LCBNs. For instance, in our simulations under the diamond hierarchy with 15 permissible patterns, Algorithm 1 often selects between 11 to 14 patterns without selecting the pattern with the smallest mixture proportion: $\boldsymbol{\alpha}_{5}=(1,1,1,0,0,0,0,0)$ with $p_{\boldsymbol{\alpha}*{5}}=0.016$. However, this turns out not to be a problem for our two-step LCBN estimation. The reason is that even when some permissible patterns are not detected (i.e., under-selection), it may still be possible to use our method described in Example 6 to exactly

Table 4: Estimation accuracy of attribute hierarchy and RMSE for the estimated parameters for the GDINA-based LCBN. The "argmin EBIC" column shows the percentage of each method (PEM or proposed) having a smaller EBIC among the 100 simulation replications.


recover the true hierarchy $\mathcal{E}$. Indeed, it can be shown that the diamond hierarchy in Figure 5 can still be recovered even when as many as five patterns (i.e., $\boldsymbol{\alpha}*{2}, \boldsymbol{\alpha}*{5}, \boldsymbol{\alpha}*{6}, \boldsymbol{\alpha}*{11}, \boldsymbol{\alpha}*{12}$ in Table 2) out of the 15 ones are not detected by the first-step Algorithm 1.

In fact, we find in simulations that when the hierarchy is not perfectly estimated, the errors are primarily caused by the over-selection of one additional non-permissible pattern. But even in this case, the resulting estimated hierarchy is still close to the truth. To empirically examine the exact source of uncertainty and inaccuracy, we have performed 200 simulation replications under DINA with $N=500, r=0.1$ and inspected the estimated hierarchies. Out of the 200 replications, 185 ones have exact recovery of the attribute hierarchy. Among the remaining 15 replications, there are at most two prerequisite relations that are not correctly detected. In the middle and right panels of Figure 6, we display examples of such incorrectly estimated hierarchies. In the middle panel, the impermissible skill pattern $(0,0,1,0,0,0,0,0)$ is mistakenly selected, which causes the missingness of the true prerequisite relation $1 \rightarrow 3$. In the right panel, the impermissible skill pattern $(1,0,0,0,0,1,0,0)$ is mistakenly selected, and hence two prerequisite relations $2 \rightarrow 6$ and $3 \rightarrow 6$ are missing and an additional arrow $1 \rightarrow 6$ is detected (note that this arrow is also implied in the true hierarchy).

The left panel in Figure 6 displays the correct detection percentages for each arrow calculated from the simulation replications. We can see that each prerequisite relation is correctly detected in more than $97 \%$ of the time. These accuracy numbers are larger than $\operatorname{Acc}(\widehat{\mathcal{E}})=92 \%$ reported in Table 3 under the same simulation setting, but this is just because the number $92 \%$ there is calculated as the percentage of times where the entire hierarchy graph $\mathcal{E}$ is perfectly recovered.
![img-5.jpeg](img-5.jpeg)

Figure 6: Left: Estimation accuracy for each arrow/prerequisite relationship. Middle and Right: examples of incorrectly estimated hierarchies in the first step. The solid red arrow in the right panel indicates an additional detected arrow which is not in the true $\mathcal{E}$.

Tables 3 and 4 also show that the proposed method can accurately estimate the continuous parameters $\boldsymbol{p}, \boldsymbol{\Theta}$, and $\boldsymbol{t}$. Similar to the estimation of $\widehat{\mathcal{E}}$, the estimation error of the continuous parameters is smaller under a smaller noise level $r$, and it decreases as sample size $N$ increases. This observation again corroborates our identifiability and consistency results of the LCBN model parameters. One can also see that the RMSE of $\boldsymbol{p}$ and $\boldsymbol{\Theta}$ after our second-step algorithm is smaller than the RMSE after just the first-step. This indicates that our second-step estimation procedure improves the overall estimation accuracy, by properly taking into account the LCBN structure. In addition, even when the hierarchy is incorrectly estimated in the first-step, the error for estimating the continuous parameters in the second step is still not large. For example, for the $N=500, r=0.1$ row in Table 3, the RMSEs of $\widehat{\boldsymbol{\Theta}}$ and $\widehat{\boldsymbol{t}}$ when the hierarchy is incorrect are 0.031 and 0.103 , respectively. These numbers are comparable to the overall average RMSEs of 0.029 and 0.042 in the corresponding row of the table.

Finally, the model selected after the second-step tends to have a lower EBIC value compared to the first-step selected model. This demonstrates that our parsimonious LCBN is preferable to the unstructured attribute hierarchy model fitted by PEM.

# 5.2 Parameter estimation under misspecified models 

Next, we evaluate our estimation procedure under a misspecified model. We still consider $K=8$ attributes and the 15 skill patterns in Table 2. Now instead of using the 15 proportion parameters defined in the last column of Table 2, we generate data using the following vector of proportions for $\boldsymbol{\alpha}_{1}, \ldots, \boldsymbol{\alpha}_{15}$ :

$$
\boldsymbol{p}=(0.10,0.04,0.15,0.15, \mathbf{0}, 0.04,0.04,0.09,0.04,0.09,0.09, \mathbf{0}, 0.05,0.05,0.07)^{\top} \in \Delta^{15}
$$

The above parameter setting is obtained by setting the two smallest entries of $\boldsymbol{p}$ in Table 2 to zero $\left(p_{\boldsymbol{\alpha}_{5}}\right.$ and $\left.p_{\boldsymbol{\alpha}_{12}}\right)$, and renormalizing the other entries to sum up to one. Note that this new skill pattern distribution cannot be considered as an LCBN nor as an unstructured attribute hierarchy model under the diamond hierarchy in Figure 5. We present the simulation results obtained by still applying the PEM method and our proposed method in Table 5. The column $\operatorname{Acc}(\widehat{\mathcal{A}})$ displays the percentage out of all the simulation replicates where all of the true permissible patterns are successfully selected: $\operatorname{Acc}(\widehat{\mathcal{A}})=1 / C \sum_{c=1}^{C} \mathbb{1}\left(\mathcal{A} \subseteq \widehat{\mathcal{A}}^{(c)}\right)$.

Table 5: RMSE for the estimated parameters for the misspecified DINA model. The argmin BIC column shows the percentage of each algorithm having a smaller BIC out of all the simulation replicates.


In the setting of Table S.2, even though the true model does not follow an exact attribute

hierarchy in the sense of (6), all permissible patterns are correctly selected in almost all simulated settings. Additionally, even though the true model is not LCBN, our estimation procedure accurately estimates the continuous parameters with similar errors compared to Table 3. Also, by comparing our final estimate to the first-stage PEM estimate, it is clear that our second-stage estimation decreases the RMSE in most scenarios. We also observe that the model selected by the second step generally has a lower EBIC and BIC. This can be explained as the parsimony of LCBNs leads to a more desirable model with a better fit to data. Notably, this advantage of LCBN is especially apparent in the challenging scenarios where the sample size $N$ is small and the noise level $r$ is large; that is, when we have less information in the data with a small signal-to-noise ratio. In summary, in these small sample and noisy scenarios, adopting our LCBN model by assuming that the latent attributes exhibit certain conditional independence according to the hierarchy graph, not only provides nice practical interpretation, but also improves model fit.

We report some additional simulation results in the Supplementary Material to further support our proposed method. In the Supplementary Material, Section S.4.3 includes simulations when the proportion parameters $\boldsymbol{p}$ respect the hierarchy graph but attributes do not exhibit the induced conditional independence asserted by LCBNs; Section S.4.4 includes sensitivity analysis for choosing the tuning parameter $\lambda$ in the log penalty.

# 6 Application to Data from the Trends in Mathematics and Science Study 

In this section, we apply the proposed method to analyze an educational assessment dataset from the Trends in Mathematics and Science Study (TIMSS). TIMSS is a series of international assessments of fourth and eighth graders' mathematics and science knowledge, involving students in over 60 countries (Mullis et al., 2012). We analyze the TIMSS 2011 Austrian fourth-grade mathematics test data, which is publicly available in the R package CDM (George et al., 2016). The data contains the responses of $N=4668$ Austrian students to $J=174$ test items. Educational experts have specified the $K=9$ fine-grained skill attributes to be: (DA) Data and Applying, (DK) Data and Knowing, (DR) Data and

Reasoning, (GA) Geometry and Applying, (GK) Geometry and Knowing, (GR) Geometry and Reasoning, (NA) Numbers and Applying, (NK) Numbers and Knowing, (NR) Numbers and Reasoning (George and Robitzsch, 2015). These nine skill attributes were defined by considering the combinations of three content skills (Data, Geometry, and Number) and three cognitive skills (Applying, Knowing, and Reasoning). This attribute definition follows George and Robitzsch (2015). A corresponding Q-matrix was also specified in George and Robitzsch (2015). This Q-matrix assumes that each item measures exactly one attribute, i.e. each row of $\mathbf{Q}$ is a standard basis vector. In this $\mathbf{Q}$-matrix, each attribute is required by at least six items, so our identifiability conditions in Theorem 1 are satisfied.

One structure specific to large scale assessments such as TIMSS is that only a subset of all items in the entire study is presented to each of the students (George and Robitzsch, 2015). This results in many missing entries in the $N \times J$ data matrix. Nevertheless, these entries are missing at random because the missingness patterns do not depend on the students' latent skills or model parameters. Our estimation algorithms can be easily adapted to this setting. Specifically, in the complete data log likelihood used in our EM algorithms, we can just replace the summation range from $\sum_{i=1}^{N} \sum_{j=1}^{J}$ to $\sum_{(i, j) \in \Omega}$, where $\Omega$ is the collection of indices $(i, j)$ that correspond to the observed entries in the data matrix.

As a first analysis, we apply the two-step method in Section 4 to estimate the latent hierarchy graph and the continuous parameters. Note that since the Q-matrix has all the row vectors being standard basis vectors, the DINA model in Example 1 and GDINA model in Example 3 are equivalent. So it suffices to just adopt the DINA model in the analysis. Algorithm 1 selected 15 attribute patterns, and Figure 7 shows the reconstructed attribute hierarchy and the estimated latent CBN parameter $\boldsymbol{t}=\left(t_{1}, \ldots, t_{9}\right)$. Figure 7 reveals that there are three ancestor attributes, DK, NK, GK that serve as the prerequisite attributes for each type of content skills in Data, Number, and Geometry. This implies that among the three cognitive skills Knowing, Applying, and Reasoning, the skill Knowing is the most basic. If a student "Knows" a certain content skill, then they possesses the prerequisite to "Apply" or "Reason" the same content skill, sometimes with the aid of other content skills. For instance, NR (Number and Reasoning) requires DR (Data and Reasoning) and DA (Data and Applying) in addition to NA (Number and Applying) as prerequisites.

Recall that each $t_{k}$ gives the conditional probability of mastering attribute $\alpha_{k}$ provided

![img-6.jpeg](img-6.jpeg)

Figure 7: Estimated hierarchy of the TIMSS 2011 dataset. The LCBN parameters $t_{k}$ are displayed above each skill attribute.
that one has already mastered all of $\alpha_{k}$ 's prerequisites. One consequence of this definition is that $t_{k}$ does not capture the individual effect of mastering any specific parent on the mastery of $\alpha_{k}$. As pointed out by a reviewer, sometimes it may also be interesting to consider such individual effects, e.g., the skill NR in Figure 7 has three parents and one may wish to distinguish their individual influences. One possible way to indirectly think about this could be to compare the values of marginal mastery probability $\mathbf{P}\left(\alpha_{l}=1\right)$ for each parent skill $l \in \mathrm{pa}(k)$. The parent skill $\alpha_{l}$ with the smallest marginal mastery probability $\mathbf{P}\left(\alpha_{l}=1\right)$ could be viewed as having the largest influence on the mastery of the child skill $\alpha_{k}=1$. Going back to the current data example with $k=\mathrm{NR}$, the skill NA could be viewed as having the largest influence on NR among the three parent skills since $\mathbb{P}(\mathrm{NA}=1)$ is the smallest among those three. We also include more discussions on potential alternative models to distinguish parent attributes' individual effects in Section 7.

Additionally, Figure 7 shows that a lot of the $t_{k}$ parameters in the second or third layer are larger than 0.9 , whereas the ancestor attributes have much smaller $t_{k}$ values. Specifically, consider $t_{D A}=0.97$. Then, $\mathbb{P}\left(\alpha_{D A}=0 \mid \alpha_{D K}=0\right)=1$ and $\mathbb{P}\left(\alpha_{D A}=0 \mid \alpha_{D K}=\right.$ $1)=0.03$, whereas $\mathbb{P}\left(\alpha_{D A}=1 \mid \alpha_{D K}=1\right)=0.97$. This implies that DA may not be a meaningful attribute, as it does not offer additional discrimination of students compared to DK. Therefore, we conduct a second analysis and merge those attributes whose $t_{k}>0.95$. For instance, we combine the attributes "DA" and "DK" into one "meta" attribute. This simplification reduces the number of attributes $K$ from nine to five and the number of permissible attribute patterns $|\mathcal{A}|$ from 69 to 16 . Then we fit an LCBN with this new attribute hierarchy in Figure 8, where the new $J \times 5$ Q-matrix can be obtained by summing

the corresponding columns in the original $J \times 9 \mathbf{Q}$-matrix. The fitted LCBN parameters are shown in Figure 8. The final result has the log likelihood equal to $-5.88 \times 10^{4}$ and EBIC equal to $1.205 \times 10^{5}$, which is a great improvement compared to the values in our first analysis (previous log likelihood equal to $-6.43 \times 10^{4}$ and EBIC equal to $1.327 \times 10^{5}$ ). This implies that merging the attributes and fitting an even more parsimonious LCBN model provides better fit to data. In summary, our LCBN model is a parsimonious and interpretable alternative to existing cognitive diagnostic models, and is especially useful to make sense of data arising from modern large-scale educational assessments such as TIMSS.
![img-7.jpeg](img-7.jpeg)

Figure 8: Re-estimated hierarchy. The LCBN parameters $t_{k}$ are displayed above the attributes.

# 7 Discussion 

We have proposed a new family of latent variable models, the latent conjunctive Bayesian networks, for modeling cognitive diagnostic assessment data in education. The LCBN family rigorously unifies the attribute hierarchy method in educational cognitive diagnosis and Bayesian networks in statistical machine learning. Compared to existing modeling approaches, our model is identifiable, parsimonious, and provides nice interpretation of conditional independence. We propose a two-step method that efficiently estimates the discrete attribute hierarchy graph and the continuous model parameters, and establish the consistency of this procedure. We have also shown that our method can be easily extended to more challenging settings with an unknown Q-matrix. Simulation studies and real data analysis demonstrate that our method has good empirical performance.

Our estimation procedure is scalable and can be easily applied to analyze modern largescale assessment data, such as TIMSS and Program for International Student Assessment data. Most existing studies of attribute hierarchy focused on the cases when $K=3$ or 4 due to the computational cost of estimating potentially exponentially many proportion parameters under an unstructured attribute hierarchy model (e.g., Templin and Bradshaw, 2014; Wang and Lu, 2021). On the contrary, our LCBN only requires a linear number of $K$ parameters to specify the latent attribute distribution and is much more parsimonious.

This work proposes the most parsimonious Bayesian network model, LCBN, for attribute hierarchy. In the future, it would also be interesting to explore other Bayesian network models in the cognitive diagnostic applications. For example, sometimes the conjunctive assumption in LCBN may be too strong or there may exist multiple paths to master a skill. To this end, one could consider a latent disjunctive Bayesian network:

$$
\mathbf{P}\left(\alpha_{k}=1 \mid \alpha_{\mathrm{pa}(k)}\right)= \begin{cases}0, & \text { if } \prod_{l \in \mathrm{pa}(k)}\left(1-\alpha_{l}\right)=1 \\ t_{k}, & \text { otherwise. }\end{cases}
$$

The above model assumes that as long as a student masters one of the parent attributes of $\alpha_{k}$, they will have a probability $t_{k}$ to master $\alpha_{k}$. Alternatively, we could define the following latent additive Bayesian network model that defines the conditional mastery probability as a linear combination of those parent attributes:

$$
P\left(\alpha_{k}=1 \mid \alpha_{\mathrm{pa}(k)}\right)=\sum_{l \in \mathrm{pa}(k)} t_{k, l} \alpha_{l}
$$

where $t_{l, k} \geq 0$ and $\sum_{l \in \mathrm{pa}(k)} t_{l, k} \leq 1$. In this model, mastering each parent attribute $\alpha_{l}$ increases the mastery probability of the child attribute $\alpha_{k}$ by $t_{k, l}$. This model is less parsimonious than LCBNs, but would be able to model different paths to mastering $\alpha_{k}$ with different probabilities. It is worth pointing out that the above two alternative Bayesian networks both induce more permissible patterns than the usual attribute hierarchy method described in Leighton et al. (2004). Since the goal of this manuscript is to propose a parsimonious graphical model (i.e., LCBN) for the usual attribute hierarchy, we leave the investigation of the properties and suitability of the above alternative models for future research.

An interesting future theoretical direction is to study the double-asymptotic regime where $N$ and $J$ both go to infinity and try to consistently estimate the individual-level latent profiles $\mathbf{A}_{i}$ 's in addition to the model parameters. In this work, we study identifiability in the fixed $J$ regime and focus on identifying and estimating the population quantities $(\mathcal{E}, \boldsymbol{\Theta}, \boldsymbol{t})$. On the other hand, when $J$ goes to infinity with increasing information provided by each student, it may be possible to consistently estimate the individual students' latent skills $\mathbf{A}_{i}$ in the sample (e.g., Gu and Xu, 2021). Such sample estimates would provide reliable personalized diagnosis. Furthermore, if individual students' skills are consistently estimated, then the LCBN parameters can be estimated via a closed form MLE (Beerenwinkel et al., 2006, 2007). This can be an alternative estimation method suitable for the double-asymptotic regime without using the regularization as in our current two-step method. Another interesting future direction is to employ LCBNs in adaptive learning or reinforcement learning settings (Chen et al., 2018; Tang et al., 2019) to help design recommendation strategies and enhance learning. Thanks to LCBNs' parsimony, interpretability, and identifiability, it is attractive to incorporate LCBNs in these computationally intensive applications to help achieve more reliable decision making and recommendations. We leave these directions for future research.

# Supplementary Material to "Latent Conjunctive Bayesian Network: Unify Attribute Hierarchy and Bayesian Network for Cognitive Diagnosis" 

This Supplementary Material is organized as follows. Section S. 1 provides additional identifiability results including conditions for strict and generic identifiability under general LCBN-based CDMs. Section S. 2 gives proofs for all Theorems in the main paper and Section S.1. Section S. 3 provides the closed form update for the GDINA item parameters in Algorithm 2 in the main paper. Section S. 4 provides many additional simulation results, including: simulation details, a comparison of EBIC and cross validation for choosing $\lambda$, additional simulations under a misspecified model, additional simulations under an unknown Q-matrix, and sensitivity analysis for choosing the tuning parameter $\lambda$ in the log penalty.

## S. 1 Additional identifiability results

In this section, we provide identifiability results for general LCBN-based CDMs. First, we define the strict identifiability of LCBNs without assuming a specific measurement model; we state the results in terms of the item parameter matrix $\boldsymbol{\Theta}$. Note that assuming a DINA measurement model in the following definition gives Definition 1 in the main paper.

Definition S. 1 (Strict identifiability). Consider an $L C B N$ with an attribute hierarchy $\mathcal{E}$ and model parameters $(\boldsymbol{\Theta}, \boldsymbol{t})$. For any alternative attribute hierarchy $\overline{\mathcal{E}}$ which results in at most $|\mathcal{A}(\mathcal{E})|$ permissible patterns, suppose the following inequality holds if and only if $(\mathcal{E}, \boldsymbol{\Theta}, \boldsymbol{t})=(\overline{\mathcal{E}}, \overline{\boldsymbol{\Theta}}, \overline{\boldsymbol{t}})$.

$$
\mathbb{P}(\mathbf{R}=r \mid \mathcal{E}, \boldsymbol{\Theta}, \boldsymbol{t})=\mathbb{P}(\mathbf{R}=r \mid \overline{\mathcal{E}}, \overline{\boldsymbol{\Theta}}, \overline{\boldsymbol{t}}) \text { for all } r \in\{0,1\}^{J}
$$

Then, the parameters $(\mathcal{E}, \boldsymbol{\Theta}, \boldsymbol{t})$ are strictly identifiable.
Before stating the identifiability result, we need to first introduce some notations. Recall that $\mathcal{A}(\mathcal{E}) \subseteq\{0,1\}^{K}$ is the set of permissible latent skill patterns that respect an attribute hierarchy $\mathcal{E}$. When it causes no confusion, we also write $\mathcal{A}(\mathcal{E})$ as $\mathcal{A}$ for notational simplicity.

Similarly to Gu and $\mathrm{Xu}(2019)$, we define a binary constraint matrix, $\Gamma^{\mathcal{A}} \in\{0,1\}^{J \times|\mathcal{A}|}$, with rows indexed by the $J$ test items and columns by the permissible patterns in $\mathcal{A}$. For $j \in[J]$ and $\boldsymbol{\alpha} \in \mathcal{A}$, the entry $\Gamma_{j, \boldsymbol{\alpha}}^{\mathcal{A}}:=\mathbb{1}\left(\boldsymbol{\alpha} \succeq \boldsymbol{q}_{j}\right)$ is a binary indicator of whether pattern $\boldsymbol{\alpha}$ possesses all the required skills of item $j$, because $\boldsymbol{q}_{j}$ is item $j$ 's skill requirement profile. The constraint matrix $\Gamma^{\mathcal{A}}$ is a function of $\mathbf{Q}$ and $\mathcal{A}$. As a toy example, consider $\mathcal{A}=\{00,01,11\}$ and $\mathbf{Q}=\mathbf{I}_{2}$, then $\Gamma^{\mathcal{A}}$ takes the form:

$$
\Gamma^{\mathcal{A}}=\left(\begin{array}{ccc}
(00) & (01) & (11) \\
0 & 1 & 1 \\
0 & 0 & 1
\end{array}\right)
$$

The $\Gamma^{\mathcal{A}}$ matrix summarizes the key constraint structure of item parameters $\boldsymbol{\Theta}=\left(\theta_{j, \boldsymbol{\alpha}}\right)_{J \times|\mathcal{A}|}$, because Eq. (1)-(2) indicate that

$$
\theta_{j, \boldsymbol{\alpha}}=\theta_{j, \boldsymbol{\alpha}^{\prime}} \text { if } \Gamma_{j, \boldsymbol{\alpha}}^{\mathcal{A}}=\Gamma_{j, \boldsymbol{\alpha}^{\prime}}^{\mathcal{A}}, \quad \theta_{j, \boldsymbol{\alpha}}>\theta_{j, \boldsymbol{\alpha}^{\prime}} \text { if } \Gamma_{j, \boldsymbol{\alpha}}^{\mathcal{A}}>\Gamma_{j, \boldsymbol{\alpha}^{\prime}}^{\mathcal{A}}
$$

For an item set $S \subseteq[J]$, let $\Gamma^{(S, \mathcal{A})}$ denote a submatrix of $\Gamma^{\mathcal{A}}$ containing the rows indexed by $S$. For two skill patterns $\boldsymbol{\alpha}, \boldsymbol{\alpha}^{\prime} \in \mathcal{A}$, we write $\boldsymbol{\alpha} \succeq_{S} \boldsymbol{\alpha}^{\prime}$, if $\Gamma_{j, \boldsymbol{\alpha}}^{\mathcal{A}} \geq \Gamma_{j, \boldsymbol{\alpha}^{\prime}}^{\mathcal{A}}$ for each item $j \in S$. This can be interpreted as skill pattern $\boldsymbol{\alpha}$ is at least as capable as $\boldsymbol{\alpha}^{\prime}$ on the items in the set $S$. Finally, we say that two item sets $S_{1}$ and $S_{2}$ induce the same partial order among the permissible skill patterns, if for any two skill patterns $\boldsymbol{\alpha}$ and $\boldsymbol{\alpha}^{\prime} \in \mathcal{A}, \boldsymbol{\alpha} \succeq_{S_{1}} \boldsymbol{\alpha}^{\prime}$ holds if and only if $\boldsymbol{\alpha} \succeq_{S_{2}} \boldsymbol{\alpha}^{\prime}$. The $\Gamma^{\mathcal{A}}$ matrix plays an important role in identifiability, as revealed in the following theorem.

Theorem S.1. A LCBN with a permissible attribute pattern set $\mathcal{A}=\mathcal{A}(\mathcal{E})$ is strictly identifiable if the binary matrix $\Gamma^{\mathcal{A}}$ satisfies the following conditions.
$A^{*}$. There exist two disjoint item sets $S_{1}, S_{2} \subseteq[J]$, such that $\Gamma^{\left(S_{i}, \mathcal{A}\right)}$ has distinct column vectors for $i=1,2$; further, $S_{1}$ and $S_{2}$ induce the same partial order among the permissible skill patterns in $\mathcal{A}$.
$B^{*}$. For any $\boldsymbol{\alpha}, \boldsymbol{\alpha}^{\prime} \in \mathcal{A}$ where $\boldsymbol{\alpha}^{\prime} \succeq_{S_{i}} \boldsymbol{\alpha}$ under $\Gamma^{\mathcal{A}}$ for $i=1$ or 2 , there exists some item $j \notin S_{1} \cup S_{2}$ such that $\Gamma_{j, \boldsymbol{\alpha}}^{\mathcal{A}} \neq \Gamma_{j, \boldsymbol{\alpha}^{\prime}}^{\mathcal{A}}$.

$C^{\star}$. Any column of $\Gamma^{\mathcal{A}}$ is different from any column of $\Gamma^{\mathcal{A}^{c}}$, where $\mathcal{A}^{c}=\{0,1\}^{K} \backslash \mathcal{A}$.
Theorem S. 1 is adapted from Theorem 3 in Gu and Xu (2019) to our LCBN setting, and guarantees the identifiability of $(\mathcal{E}, \boldsymbol{\Theta}, \boldsymbol{p})$. Although notation in the theorem may look somewhat heavy, these identifiability conditions are transparent in the sense that they depend only on the binary matrix $\Gamma^{\mathcal{A}}$, rather than on continuous parameter values of $(\boldsymbol{\Theta}, \boldsymbol{p})$.

Next, we provide sufficient conditions for generic identifiability. Generic identifiability is a weaker notion compared to strict identifiability, with the intuition that the model parameters and the hierarchy are identified almost surely. The term is formally defined below.

Definition S. 2 (generic identifiability). Assume an $L C B N$ with the true hierarchy $\mathcal{E}$ and parameters $(\boldsymbol{\Theta}, \boldsymbol{t})$, where $\boldsymbol{\Theta}$ respects the constraints given by $\Gamma^{\mathcal{A}}$. Denote this constrained parameter space of $(\boldsymbol{\Theta}, \boldsymbol{t})$ by $\Omega$. We say $(\mathcal{E}, \boldsymbol{\Theta}, \boldsymbol{t})$ is generically identifiable, if there exists a Lebesgue measure zero subset $\mathcal{V} \in \Omega$ such that for any $(\boldsymbol{\Theta}, \boldsymbol{t}) \in \Omega \backslash \mathcal{V}$, Equation (S.1) implies $(\mathcal{E}, \boldsymbol{\Theta}, \boldsymbol{t})=(\overline{\mathcal{E}}, \overline{\boldsymbol{\Theta}}, \overline{\boldsymbol{t}})$.

The following Theorem S. 2 provides sufficient conditions for generic identifiability in terms of the constraint matrix $\Gamma^{\mathcal{A}}$. These conditions are weaker compared to those in Theorem S. 1 and hence are easier to satisfy in practice.

Theorem S.2. Assume an $L C B N$ with hierarchy $\mathcal{E}$. If $\Gamma^{\mathcal{A}}$ satisfies Condition $C$ in Theorem S. 1 and also the following conditions, then $(\mathcal{E}, \boldsymbol{\Theta}, \boldsymbol{t})$ is generically identifiable.
$A^{\star \star}$. There exist two disjoint item sets $S_{1}$ and $S_{2}$, such that altering some entries from 0 to 1 in $\Gamma^{\left(S_{1} \cup S_{2}, \mathcal{A}\right)}$ can yield a $\widetilde{\Gamma}^{\left(S_{1} \cup S_{2}, \mathcal{A}\right)}$ satisfying Condition $A$. That is, $\widetilde{\Gamma}^{\left(S_{i}, \mathcal{A}_{0}\right)}$ has distinct columns for $i=1,2$ and " $\succeq_{S_{1}} "=" \succeq_{S_{2}} "$ under $\widetilde{\Gamma}^{\left(S_{1} \cup S_{2}, \mathcal{A}\right)}$.
$B^{\star \star}$. For any $\boldsymbol{\alpha}, \boldsymbol{\alpha}^{\prime} \in \mathcal{A}$ where $\boldsymbol{\alpha}^{\prime} \succeq_{S_{i}} \boldsymbol{\alpha}$ under $\widetilde{\Gamma}^{\left(S_{1} \cup S_{2}, \mathcal{A}\right)}$ for $i=1$ or 2 , there exists some $j \in\left(S_{1} \cup S_{2}\right)^{c}$ such that $\Gamma_{j, \boldsymbol{\alpha}}^{\mathcal{A}} \neq \Gamma_{j, \boldsymbol{\alpha}^{\prime}}^{\mathcal{A}}$.

The proof of Theorem S. 2 follows from applying Theorem 2 in Gu and Xu (2019), sharing the spirit of the proof of Theorem S.1. We omit the details.

Next, we consider the LCBN-based DINA where the Q-matrix is unknown and also needs to be estimated. The sufficient conditions are provided in Theorem S.3. We mention that if the Q-matrix is known, the conditions in Theorem S. 3 can be relaxed, as in Theorem 1.

Indeed, whereas condition B in Theorem S. 3 requires every attribute to be measured 3 times, this can be relaxed to being measured twice or once, depending on its type.

Theorem S.3. The LCBN-based DINA is strictly identifiable upto $(\Gamma, \boldsymbol{s}, \boldsymbol{g}, \boldsymbol{t})$ when the true (unknown parameter) $\mathbf{Q}$ and $\mathcal{E}$ satisfies:

A1. $\mathbf{Q}$ contains a $K \times K$ submatrix $\mathbf{Q}^{0}$ that is equivalent to $I_{K}$ under $\mathcal{E}$. Without generality, write $\mathbf{Q}=\left[\mathbf{Q}_{0}^{\top}, \mathbf{Q}^{*\top}\right]^{\top}$.

B1. The sparsified version of $\mathbf{Q}$ contains at least three " 1 "s in each column.
C1. The densified version of $\mathbf{Q}^{*}$ has distinct columns.
The proof of Theorem S. 3 follows from applying Theorem 1 in Gu and Xu (2022), sharing the spirit of the proof of Theorem 1. We omit the details.

# S. 2 Proof of Theorems S.1, 1, 2 and Proposition 1 

We next provide the proofs of Theorem S.1, Theorem 1, and Proposition 1, respectively.

Proof of Theorem S.1. We first note that LCBNs can be considered as a structured latent attribute model (SLAM, Gu and Xu (2019)) when we reparametrize $\boldsymbol{t}, \mathcal{E}$ as the proportion parameter $\boldsymbol{p}$, i.e.

$$
p_{\boldsymbol{\alpha}}=t_{k}{ }^{\alpha_{k}} \Pi_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}}\left(1-t_{k}\right)^{\left(1-\alpha_{k}\right) \Pi_{\ell=1}^{K} \alpha_{\ell}^{G_{\ell, k}}}, \quad \forall \boldsymbol{\alpha} \in\{0,1\}^{K}
$$

Indeed, equations (1) and (2) in the main text together with our assumptions for the measurement model, are equivalent to assumptions (2) and (3) in Gu and Xu (2019). Also, our assumptions for the structure model imply $\sum_{\boldsymbol{\alpha} \in \mathcal{A}} p_{\boldsymbol{\alpha}}=1$, so the proportion parameter assumption in Gu and Xu (2019) is satisfied. It is also easy to check that our three conditions (Conditions $A, B$, and $C$ ) are exactly the same as the identifiability conditions in Theorem 2 in Gu and Xu (2019).

Hence, we can directly apply Corollary 3 in Gu and Xu (2019) to obtain that $(\boldsymbol{p}, \boldsymbol{\Theta})$ are identifiable. It remains to show that $(\boldsymbol{t}, \mathcal{E})$ are identifiable from $\boldsymbol{p}$. Suppose that $\boldsymbol{p}$ is the

attribute proportion generated from an LCBN with true parameters $(\boldsymbol{t}, \mathcal{E})$. Let

$$
\mathcal{A}=\left\{\boldsymbol{\alpha} \in\{0,1\}^{K}: p_{\boldsymbol{\alpha}}>0\right\}
$$

(this is the true $\mathcal{A}$ by definition). Then, $\mathcal{E}$ can be identified by defining $\mathcal{E}$ based on (13). Finally, given $\mathcal{A}$ and $\mathcal{E}, \boldsymbol{t}$ can be identified by solving (S.2) for all $\boldsymbol{\alpha} \in \mathcal{A}$. Note that under any hierarchy $\mathcal{E}$, the number of permissible patterns is at least as many as $K$ (i.e., $|\mathcal{A}(\mathcal{E})| \geq K$ ) and that (S.2) contains at least $K$ linear independent constraints. In addition, we know that there exists a true LCBN parameter vector $\boldsymbol{t}$ that satisfies (S.2), so this is the unique solution to (S.2). This proves $\boldsymbol{t}$ are also identifiable and completes the proof of the theorem.

Proof of Theorem 1. Similar to the proof of Theorem S.1, note that LCBNs can be considered as a hierarchical latent attribute model (HLAM, Gu and Xu (2022)) when we reparametrize $\boldsymbol{t}, \mathcal{E}$ as the proportion parameter $\boldsymbol{p}$ using (S.2). It is also easy to check that our three conditions (Conditions $A, B$, and $C$ ) are exactly the same as the conditions in Theorem 2 in Gu and Xu (2022). Hence, we can apply Theorem 2 in Gu and Xu (2022) to obtain that $(\boldsymbol{s}, \boldsymbol{g}, \mathcal{E}, \boldsymbol{p})$ is identifiable. Then similarly to the proof of Theorem S.1, we again identify $\boldsymbol{t}$ from $\boldsymbol{p}$ by using (S.2). This completes the proof of Theorem 1.

Proof of Proposition 1 The sufficiency follows from Theorem 1. We prove that both conditions $A$ and $B^{\star}$ are necessary. In this proof, we use the following equivalent parametrization of the slipping and guessing parameters $\boldsymbol{s}, \boldsymbol{g}$ for notational simplicity.

$$
\theta_{j}^{+}=1-s_{j}, \quad \theta_{j}^{-}=g_{j}, \quad \forall j \in[J]
$$

# Necessity of Condition $A$. 

Under the linear hierarchy, the proof of Proposition 3 in Gu and Xu (2022) can be applied directly. Suppose the sparsified $\mathbf{Q}$-matrix does not contain $e_{h}$ for some $1 \leq h \leq K$. Then, $\boldsymbol{\alpha}_{1}=(1, \cdots, 1,0,0, \cdots, 0)$ and $\boldsymbol{\alpha}_{2}=(1,1, \cdots, 1,1,0, \cdots, 0)$ are configurations in $\mathcal{A}(\mathcal{E})$ with the same ideal response vector across all the items $\Gamma_{:, \boldsymbol{\alpha}_{1}}^{\mathcal{A}}=\Gamma_{:, \boldsymbol{\alpha}_{2}}^{\mathcal{A}}$ (here, $\boldsymbol{\alpha}_{1}$ and $\boldsymbol{\alpha}_{2}$ only differs in the $h$ th entry). Hence, $p_{\boldsymbol{\alpha}_{1}}$ and $p_{\boldsymbol{\alpha}_{2}}$ are only identifiable up to their sum, so the LCBN parameters $t_{h}$ and $t_{h+1}$ are identifiable only up to their product.

Necessity of Condition $B^{\star}$.
(i) We prove that any ancestor attribute needs to be measured at least twice for identifiability to hold. Suppose some ancestor attribute is measured only once, and assume that attribute 1 is an ancestor attribute measured only by item 1. Denote the true LCBN parameters by $\left(\theta^{+}, \theta^{-}, \mathcal{E}, \boldsymbol{t}\right)$ and the true proportion parameters by $\boldsymbol{p}$. We show that there exists $\left(\bar{\theta}^{+}, \bar{\theta}^{-}, \overline{\mathcal{E}}, \overline{\boldsymbol{t}}\right) \neq\left(\theta^{+}, \theta^{-}, \mathcal{E}, \boldsymbol{t}\right)$ with the same marginal distributions.

Define $\bar{\theta}_{j}^{+}=\theta_{j}^{+}$for all $j, \bar{\theta}_{j}^{-}=\theta_{j}^{-}$for $j \geq 2, \overline{\mathcal{E}}=\mathcal{E}, \bar{t}_{k}=t_{k}$ for $k \geq 3$. There are three free parameters: $\bar{\theta}_{1}{ }^{-}, \bar{t}_{1}, \bar{t}_{2}$. By the proof of Proposition 5 in Gu and Xu (2022), the marginal distribution of the response vector $\mathbf{R}$ is the same under the true and alternative parameters if the following equations hold:

$$
\left\{\begin{array}{l}
\bar{p}_{\left(0, \mathbf{0}_{K-1}\right)}+\bar{p}_{\left(1, \mathbf{0}_{K-1}\right)}=p_{\left(0, \mathbf{0}_{K-1}\right)}+p_{\left(1, \mathbf{0}_{K-1}\right)} \\
\bar{\theta}_{1}^{-} \bar{p}_{\left(0, \mathbf{0}_{K-1}\right)}+\theta_{1}^{+} \bar{p}_{\left(1, \mathbf{0}_{K-1}\right)}=\theta_{1}^{-} p_{\left(0, \mathbf{0}_{K-1}\right)}+\theta_{1}^{+} p_{\left(1, \mathbf{0}_{K-1}\right)}
\end{array}\right.
$$

Writing the above equations in terms of $\bar{t}_{1}$ and $\bar{t}_{2}$ gives

$$
\left\{\begin{array}{l}
\bar{t}_{1} \bar{t}_{2}=t_{1} t_{2} \\
\bar{\theta}_{1}^{-}\left(1-\bar{t}_{1}\right)+\theta_{1}^{+} \bar{t}_{1}\left(1-\bar{t}_{2}\right)=\theta_{1}^{-}\left(1-t_{1}\right)+\theta_{1}^{+} t_{1}\left(1-t_{2}\right)
\end{array}\right.
$$

There are three variables $\left(\bar{t}_{1}, \bar{t}_{2}, \bar{\theta}_{1}^{-}\right)$that need to satisfy two equations, so there are infinitely many solutions. Hence, the model is not identifiable. This proves that the condition that any ancestor attribute needs to be measured at least twice is necessary for identifiability.

Remark 2. Suppose condition $A$ holds. Then, the above proof only uses the assumption that " $\alpha_{1}$ is the only ancestor / singleton attribute".
(ii) We prove that $\alpha_{K}$ needs to be measured at least twice. Suppose not, and assume that attribute $K$ is a leaf attribute measured only by item $K$. We next show that there exists $\left(\bar{\theta^{+}}, \bar{\theta}^{-}, \overline{\mathcal{E}}, \overline{\boldsymbol{t}}\right) \neq\left(\theta^{+}, \theta^{-}, \mathcal{E}, \boldsymbol{t}\right)$ that lead to the same marginal distributions for the observed response vector $\mathbf{R}$.

Define $\bar{\theta}_{j}^{+}=\theta_{j}^{+}$for $j \neq K, \bar{\theta}_{j}^{-}=\theta_{j}^{-}$for all $j, \overline{\mathcal{E}}=\mathcal{E}, \bar{t}_{k}=t_{k}$ for $k \neq K-1, K$. There are three free parameters: $\theta_{K}^{+}, t_{K-1}, t_{K}$. Similar to the previous argument, the marginal

distribution of $\mathbf{R}$ is the same if the equations

$$
\left\{\begin{array}{l}
\bar{p}_{\left(\boldsymbol{\alpha}^{\prime}, 0\right)}+\bar{p}_{\left(\boldsymbol{\alpha}^{\prime}, 1\right)}=p_{\left(\boldsymbol{\alpha}^{\prime}, 0\right)}+p_{\left(\boldsymbol{\alpha}^{\prime}, 1\right)} \\
\theta_{K}^{-} \bar{p}_{\left(\boldsymbol{\alpha}^{\prime}, 0\right)}+\bar{\theta}_{K}^{+} \bar{p}_{\left(\boldsymbol{\alpha}^{\prime}, 1\right)}=\theta_{K}^{-} p_{\left(\boldsymbol{\alpha}^{\prime}, 0\right)}+\theta_{K}^{+} p_{\left(\boldsymbol{\alpha}^{\prime}, 1\right)}
\end{array}\right.
$$

hold for all $\boldsymbol{\alpha}^{\prime} \in\{0,1\}^{K-1}$. Now, note that our parameter assumptions give that $\bar{p}_{\left(\boldsymbol{\alpha}^{\prime}, 0\right)}=$ $p_{\left(\boldsymbol{\alpha}^{\prime}, 0\right)}$ and $\bar{p}_{\left(\boldsymbol{\alpha}^{\prime}, 1\right)}=p_{\left(\boldsymbol{\alpha}^{\prime}, 1\right)}$ for all $\alpha^{\prime} \neq \mathbf{1}_{K-1}$. Hence, (S.3) is automatically satisfied except when $\alpha^{\prime}=\mathbf{1}_{K-1}$. Writing this in terms of $\theta_{K}^{+}, t_{K-1}, t_{K}$, (S.3) is equivalent to

$$
\left\{\begin{array}{l}
\bar{t}_{K-1}=t_{K-1} \\
\theta_{K}^{-}\left(1-\bar{t}_{K}\right)+\bar{\theta}_{K}^{+} \bar{t}_{K}=\theta_{K}^{-}\left(1-t_{K}\right)+\theta_{K}^{+} t_{K}
\end{array}\right.
$$

Clearly there are infinitely many solutions and this model is not identifiable. This proves that the condition that any leaf attribute needs to be measured at least twice is necessary for identifiability.

Remark 3. Suppose condition $A$ holds. Then, the above proof only uses the assumption that " $\alpha_{K}$ is the only leaf / singleton attribute".

Proof of Theorem 2. Our proof is mainly based on Theorem 13 in Gu and Xu (2019) (denoted as Theorem 13 in GX for simplicity). We first check their conditions. Similar to the proof of Theorem S.1, we note that LCBN-based CDMs can be viewed as a structured latent attribute model (SLAM) with parameters $(\boldsymbol{\Theta}, \boldsymbol{p})$ with $\boldsymbol{p}$ given by the LCBN parametrization in (S.2). Moreover, as we have that our LCBN-based CDM is identifiable, the corresponding SLAM is also identifiable. The first line in Theorem 13 in GX is only used to guarantee model identifiability, and can be replaced by our assumption.

Noting that we are considering a fixed $K$ and true parameters $t_{k} \in(0,1)$, there exists a constant $c_{0}>0$ such that $p_{\boldsymbol{\alpha}}>c_{0}$ for all $\boldsymbol{\alpha} \in \mathcal{A}$. Combining this with (16), equation (20) in Theorem 13 in GX holds. Finally, as we consider $\mathcal{A}_{\text {input }}=\{0,1\}^{K},\left|\mathcal{A}_{\text {input }}\right|=2^{K}$ is a constant with respect to $N$. Hence, every assumption in Theorem 13 in GX holds and we get

$$
\mathbf{P}\left(\widehat{\mathcal{A}}^{\lambda_{N}}=\mathcal{A}\right) \rightarrow 1
$$

as $N \rightarrow \infty$. Now note that the hierarchy $\mathcal{E}$ is correctly estimated when the set of permissible

patterns $\mathcal{A}$ is correctly estimated. So we have

$$
\mathbf{P}\left(\widehat{\mathcal{E}}^{\lambda_{N}}=\mathcal{E}\right) \geq \mathbf{P}\left(\widehat{\mathcal{A}}^{\lambda_{N}}=\mathcal{A}\right) \rightarrow 1
$$

and $\widehat{\mathcal{E}}^{\lambda_{N}}$ is consistent.

Proof of Theorem 3. For any vector $\boldsymbol{a}$, let $\|\boldsymbol{a}\|$ denote its $L_{2}$ norm. With a slight abuse of notation, let $\Theta$ also denote the vector (in addition to its original definition of being a matrix) collecting all the different item parameters in matrix $\boldsymbol{\Theta}$, and let $\|\boldsymbol{\Theta}\|$ denote the $L_{2}$ norm of this long item parameter vector. Let $\widehat{\mathcal{E}}=: \widehat{\mathcal{E}}_{N}$ denote the estimator of the attribute hierarchy graph when sample size is $N$. For any $\epsilon>0$,

$$
\begin{aligned}
& \limsup _{N \rightarrow \infty} \mathbf{P}\left(\left\|\widehat{\boldsymbol{\Theta}}_{N}-\boldsymbol{\Theta}\right\|>\epsilon,\left\|\widehat{\boldsymbol{t}}_{N}-\boldsymbol{t}\right\|>\epsilon\right) \\
= & \limsup _{N \rightarrow \infty}\left(\mathbf{P}\left(\left\|\widehat{\boldsymbol{\Theta}}_{N}-\boldsymbol{\Theta}\right\|>\epsilon,\left\|\widehat{\boldsymbol{t}}_{N}-\boldsymbol{t}\right\|>\epsilon, \widehat{\mathcal{E}}_{N}=\mathcal{E}\right)+\right. \\
& \left.\mathbf{P}\left(\left\|\widehat{\boldsymbol{\Theta}}_{N}-\boldsymbol{\Theta}\right\|>\epsilon,\left\|\widehat{\boldsymbol{t}}_{N}-\boldsymbol{t}\right\|>\epsilon, \widehat{\mathcal{E}}_{N} \neq \mathcal{E}\right)\right) \\
\leq & \limsup _{N \rightarrow \infty}\left(\mathbf{P}\left(\left\|\widehat{\boldsymbol{\Theta}}_{N}-\boldsymbol{\Theta}\right\|>\epsilon,\left\|\widehat{\boldsymbol{t}}_{N}-\boldsymbol{t}\right\|>\epsilon \mid \widehat{\mathcal{E}}_{N}=\mathcal{E}\right) \mathbf{P}\left(\widehat{\mathcal{E}}_{N}=\mathcal{E}\right)+\mathbf{P}\left(\widehat{\mathcal{E}}_{N} \neq \mathcal{E}\right)\right) \\
\leq & \limsup _{N \rightarrow \infty} \mathbf{P}\left(\left\|\widehat{\boldsymbol{\Theta}}_{N}-\boldsymbol{\Theta}\right\|>\epsilon,\left\|\widehat{\boldsymbol{t}}_{N}-\boldsymbol{t}\right\|>\epsilon \mid \widehat{\mathcal{E}}_{N}=\mathcal{E}\right)
\end{aligned}
$$

The last inequality follows from the fact that we assume the conditions in Theorem 2, so we have $\mathbf{P}(\widehat{\mathcal{E}}=\mathcal{E}) \rightarrow 1$ and $\mathbf{P}(\widehat{\mathcal{E}} \neq \mathcal{E}) \rightarrow 0$. Hence, it suffices to show that the last line in the above display is zero for any $\epsilon>0$. That is, we only need to show that the $\operatorname{MLE}\left(\widehat{\boldsymbol{\Theta}}_{N}, \widehat{\boldsymbol{t}}_{N}\right)$ given the true hierarchy $\mathcal{E}$ is consistent. This is true following from a standard textbook argument, e.g. Theorem 10.1.6 in Casella and Berger (2021), because the continuous parameters are identifiable, and the likelihood given the hierarchy is differentiable. So $\lim _{N \rightarrow \infty} \mathbf{P}\left(\left\|\widehat{\boldsymbol{\Theta}}_{N}-\boldsymbol{\Theta}\right\|>\epsilon,\left\|\widehat{\boldsymbol{t}}_{N}-\boldsymbol{t}\right\|>\epsilon\right) \rightarrow 0$, which proves the consistency.

# S. 3 Closed-form updates for the GDINA model parameters in Algorithm 1 

Let $S_{j}=\left\{k \in[K]: q_{j, k}=1\right\}$. By the Q-matrix constraints in (1) and (2), we can assume without loss of generality that $\delta_{j, S}$ is 0 for $S \nsubseteq S_{j}$. Hence, it suffices to update the parameters where $S \subseteq S_{j}$, which can be written as:

$$
\delta_{j, S}^{(t+1)}=\frac{\sum_{i} \sum_{\boldsymbol{\alpha}} \mathbb{1}\left(\left\{k \in S_{j}: \alpha_{k}=1\right\}=S\right) R_{i, j} \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}{\sum_{i} \sum_{\boldsymbol{\alpha}} \mathbb{1}\left(\left\{k \in S_{j}: \alpha_{k}=1\right\}=S\right) \varphi_{i, \boldsymbol{\alpha}}^{(t+1)}}, \quad \forall j \in[J], \quad S \subseteq S_{j}
$$

The above updates can be used in the M step of Algorithm 1 for the GDINA model.

## S. 4 Additional simulation studies and details

## S.4.1 Additional simulation details

For the implementation of our EM algorithms, we made the following specifications. First, we set the convergence criterion of EM Algorithms 1 and 2 to be that, the algorithm is terminated when the increment of the log likelihood in two consecutive iterations is less than $0.05,0.01$, respectively. The threshold is larger for Algorithm 1 as it only aims to estimate the discrete structure, and does not need to estimate continuous parameters very accurately. Note that our convergence criterion is already very stringent when considering the magnitude of the actual likelihood, which is of a $10^{4}$ scale in both the simulation studies and the real data analysis. The other threshold values in Algorithm 1 are set to be $c=0.01$ and $\rho_{N}=\frac{1}{2 N}$ following the suggestions of Gu and Xu (2019).

Next, we report the average number of iterations and runtime for Algorithms 1 and 2 in Table S.1. The reported values are averages from 100 independent simulation replicates. Table S. 1 shows that our new algorithm for LCBN takes fewer than 10 iterations and 25 seconds on average to reach convergence, and the overall two-step estimation procedure is also computationally quite efficient. We can see that the absolute value of the selected $\widehat{\lambda}$ increases with respect to $N$, which is consistent with the asymptotic conditions for $\lambda$ in Theorem 2. Here, we consider the DINA measurement model with noise level $r=0.1$, and

use the same diamond hierarchy and $\mathbf{Q}$-matrix as in Section 5 (in other words, Table S. 1 corresponds to the rows with $r=0.1$ in Table 3 in the main body of the manuscript).

Finally, all simulations in this paper were performed in MATLAB on a personal laptop with GPU: Intel Iris Xe graphics card, CPU: Intel i7-1260P Processor with vPro (16GB).

Table S.1: The average number of iterations and runtime for the EM algorithms


# S.4.2 Comparison of EBIC and cross validation for choosing $\lambda$ 

Next, we compare the EBIC and cross validation (CV) in terms of selecting the tuning parameter $\lambda$. We work on the same setting as Section 5.2 with sample size $N=500$, noise level $r=0.2$, and $\lambda \in\{0,-0.3, \ldots,-6\}$.

We have tried selecting $\lambda$ via the 5 -fold CV (we divide the $N$ subjects into five equal-sized folds), and found that CV tends to select a large $\lambda<0$ (i.e., small $|\lambda|$ ) compared to the $\lambda$ chosen via EBIC. This means CV favors a small magnitude of the penalty. In Figure S.1, 5 -fold CV selects a quite large $\widehat{\lambda}=-0.9$ compared to $\widehat{\lambda}=-3$ selected by EBIC (as displayed in Figure 7 in the main text). Actually, $\widehat{\lambda}=-3$ selected by EBIC correctly estimates the hierarchy (which is a desirable outcome of the first step), while $\widehat{\lambda}=-0.9$ selected by CV overestimates the number of permissible attribute patterns. This observation implies that CV fails in the first step to recover the correct attribute hierarchy, which will subsequently lead to an erroneous estimation of LCBN parameters when proceeding to the second step. In fact, the failure of CV in this setting is in line with some known results regarding CV's

model selection inconsistency in regression, e.g.: "it is well known from simulations that the cross-validated Lasso estimator typically selects too many variables" (Remark 4.4. in Chetverikov et al., 2021). On the other hand, our selection criterion, the EBIC, has a nice consequence of model selection consistency under high dimensional sparse settings (Chen and Chen, 2008), which justifies using EBIC here.
![img-8.jpeg](img-8.jpeg)

Figure S.1: Cross validation value versus $\lambda$. The red point with $\widehat{\lambda}=-0.9$ is selected.

Additionally, in order to do cross validation, one needs to fit the model multiple times for each fixed value of $\lambda$, which makes it computationally much slower compared to other model selection criteria. Indeed, in our simulations, 5 -fold CV took 62.7 seconds whereas using EBIC (or BIC) only took 15.8 seconds.

# S.4.3 Additional simulations under a misspecified model 

In this section, we present additional simulation results when the model is misspecified, i.e., when the data-generating mechanism does not follow an LCBN. We consider the same diamond hierarchy defined in Figure 5, but instead of constraining the proportion parameters to follow a CBN structure, we initialize $\boldsymbol{p}=\left(\frac{1}{15}, \ldots, \frac{1}{15}\right)^{\top}$. In other words, we assign equal probability for the 15 possible patterns in Table 2. This initialization follows the attribute hierarchy method, but does not follow an LCBN. Note that this was not the case in the initialization in Section 5.2, which did not follow an attribute hierarchy nor an LCBN. We compute the pattern selection accuracy $\operatorname{Acc}(\widehat{\mathcal{A}})$ and the RMSE of parameter estimates in addition to comparing the EBIC and BIC of the first-step estimate and our two-step estimate. The results are summarized in Table S.2.

Table S. 2 shows that the set of permissible skill patterns $\mathcal{A}$ is selected successfully most of

the time (with a slightly smaller accuracy compared to the results in Section 5.2). Also, the continuous parameters are estimated with an estimation error similar to Table 3 in the main paper, which corresponds to the estimation error of the correctly specified model. We also see that except for one scenario $(N=500, r=0.3)$, the second stage estimate has a lower EBIC and BIC. These results are analogous to those of Section 5.2., and justifies adopting LCBNs even in misspecified scenarios.

Table S.2: Estimation accuracy and RMSE for the estimated parameters for the misspecified DINA model.


# S.4.4 Additional simulation results under an unknown Q-matrix 

This section presents additional simulation results where the $\mathbf{Q}$-matrix and the number of latent skills, $K$, are unknown. We apply the exploratory penalized EM algorithm in Ma et al. (2023) in our first step to jointly estimate the $\mathbf{Q}$-matrix and the attribute hierarchy $\mathcal{E}$ (see Section 4.3 in the main text for more details). Our second step for estimating the continuous parameters is still our new Algorithm 2. In terms of choosing the tuning parameters, we follow the suggestions and settings in Ma et al. (2023).

We consider $K=4$ attributes with a convergent hierarchy in Figure S.2, which is an example hierarchy presented in the initial attribute hierarchy paper Gierl et al. (2007). This convergent hierarchy was also used in the simulation studies in Ma et al. (2023) but with true proportion parameters that do not follow an LCBN. This hierarchy results in $|\mathcal{A}|=6$ permissible patterns, as shown in Table S.3. Here, we set the $K=4$ LCBN parameters as

$\boldsymbol{t}=(0.9,0.65,0.65,0.5)$ and consider the following $\mathbf{Q}$-matrix:

$$
\mathbf{Q}=\left(\begin{array}{l}
\mathbf{Q}_{1} \\
\mathbf{Q}_{1} \\
\mathbf{Q}_{2} \\
\mathbf{Q}_{2} \\
\mathbf{Q}_{3} \\
\mathbf{I}_{K} \\
\mathbf{I}_{K} \\
\mathbf{I}_{K}
\end{array}\right)
$$

with $J=30$ items, where $\mathbf{Q}_{1}, \mathbf{Q}_{2}$ are the matrices defined in (19) in the main text, $\mathbf{I}_{K}$ is the identity matrix, and

$$
\mathbf{Q}_{3}=\left(\begin{array}{llll}
1 & 0 & 1 & 1 \\
1 & 1 & 0 & 1
\end{array}\right)
$$

For the measurement model, we consider the DINA model. In terms of the noise level $r$, we continue to consider $r=0.1$ and 0.2 as in the main text.

In Table S.4, we report the accuracy of the estimated hierarchy and the $\mathbf{Q}$-matrix along with the final estimate of the continuous parameters. In each simulation setting, we perform 100 independent replications and report the average accuracy. Here, the accuracy for the Q-matrix (matrix-wise or row-wise) is defined in terms of estimating the $\mathbf{Q}$-matrix up to an equivalence class, as the $\mathbf{Q}$-matrix under the DINA model is identifiable only up to the equivalence classes defined by the $\Gamma$ matrix (Gu and Xu, 2022). Note that the matrixwise accuracy (denoted as $\operatorname{Acc}\left(\widehat{\mathbf{Q}}^{\text {mat }}\right)$ in Table S.4) is more stringent than the row-wise (or item level) accuracy (denoted as $\operatorname{Acc}\left(\widehat{\mathbf{Q}}^{\text {row }}\right)$ in Table S.4) by definition. As the value and interpretation of the parameter $\boldsymbol{t}$ heavily depends on the specific hierarchy and $(\boldsymbol{s}, \boldsymbol{g})$ depends on the $\mathbf{Q}$-matrix, we compute the RMSE of the continuous parameters when the hierarchy and the $\mathbf{Q}$-matrix are correctly estimated. Due to the variety of the tuning parameters that need to be chosen, the runtime for this simulation was much larger than those based on Algorithm 1 in our main text (it took more than 5 minutes on average when $N=500$, which is much larger than that reported in Table S.1).

Table S. 4 shows that the attribute hierarchy and the $\mathbf{Q}$-matrix can be jointly estimated with high accuracy, even when the $\mathbf{Q}$-matrix is unknown. In particular, when the noise level $r$ is small and $N$ is large, we see that both the hierarchy and the $\mathbf{Q}$-matrix are perfectly estimated, and also the continuous parameters have a small estimation error. Compared to Table 3 in the main body of our paper, the estimation accuracy of Algorithm 3 is comparable to Algorithm 1 when $r=0.1$ but is much lower when $r=0.2$ (here, the settings of the two Tables are different due to different numbers of attributes and different hierarchies, so we are only comparing a rough trend of the estimation accuracy). We believe that a larger noise level makes the problem more challenging when the $\mathbf{Q}$-matrix is unknown. This observation is also coherent with Table 2 in Ma et al. (2023).
![img-9.jpeg](img-9.jpeg)

Figure S.2: Convergent hierarchy with $K=4$ attributes.


Table S.3: Permissible patterns under the convergent hierarchy

Table S.4: Estimation accuracy and RMSE for the estimated parameters for the exploratory DINA model.


# S.4.5 Sensitivity analysis for choosing the tuning parameter $\lambda$ in the log penalty 

We next present simulation evidence to show that the estimation of the hierarchy graph is not very sensitive to the value of $\lambda$. Consider the same setting as those for the DINA model simulation in the previous subsection. In a simulation trial with sample size $N=500$ and noise level $r=0.2$, we plot the number of selected skill patterns and the corresponding EBIC value versus a sequence of $\lambda \in\{0,-0.3, \ldots,-6\}$ in Figure S.3. The left panel in Figure S. 3 shows a wide interval $\lambda \in[-1.2,-3.6]$ colored in red, with every $\lambda$ in this interval leading to a correct estimate of the attribute hierarchy. This fact demonstrates that the estimation of the hierarchy graph $\mathcal{E}$ is robust to the choice of $\lambda$. Furthermore, even for a stronger penalty with $\lambda \leq-3.9$ that is outside of this interval, the estimated hierarchy graph makes only one error by additionally including one prerequisite $\alpha_{8} \rightarrow \alpha_{7}$. The right panel in Figure S. 3 shows that $\widehat{\lambda}=-3$ is chosen via EBIC because it gives smallest EBIC value. We can see that EBIC succeeds here because -3 belongs to the feasible interval $[-1.2,-3.6]$.
![img-10.jpeg](img-10.jpeg)

Figure S.3: Number of selected skill patterns $|\widehat{\mathcal{A}}|$ (left) and EBIC value (right) plotted against $\lambda$. Left: the red points correspond to a wide interval $[-1.2,-3.6]$ of $\lambda$ that can correctly estimate the hierarchy. Right: $\widehat{\lambda}=-3$ is selected via EBIC because it gives the smallest EBIC value.