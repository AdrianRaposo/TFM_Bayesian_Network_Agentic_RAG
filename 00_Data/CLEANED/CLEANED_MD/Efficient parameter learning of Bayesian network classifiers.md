# Efficient parameter learning of Bayesian network classifiers 

Nayyar A. Zaidi ${ }^{1}$ ・ Geoffrey I. Webb ${ }^{1}$ ・ Mark J. Carman ${ }^{1}$ ・ François Petitjean ${ }^{1}$ ・ Wray Buntine ${ }^{1}$ ・ Mike Hynes ${ }^{2}$ ・ Hans De Sterck ${ }^{3}$

Received: 24 December 2015 / Accepted: 22 November 2016 / Published online: 26 January 2017
(C) The Author(s) 2017


#### Abstract

Recent advances have demonstrated substantial benefits from learning with both generative and discriminative parameters. On the one hand, generative approaches address the estimation of the parameters of the joint distribution- $\mathrm{P}(y, \mathbf{x})$, which for most network types is very computationally efficient (a notable exception to this are Markov networks) and on the other hand, discriminative approaches address the estimation of the parameters of the posterior distribution-and, are more effective for classification, since they fit $\mathrm{P}(y \mid \mathbf{x})$ directly. However, discriminative approaches are less computationally efficient as the normalization factor in the conditional log-likelihood precludes the derivation of closed-form estimation of parameters. This paper introduces a new discriminative parameter learning method for Bayesian network classifiers that combines in an elegant fashion parameters learned using


Editors: Thomas Gärtner, Mirco Nanni, Andrea Passerini, and Celine Robardet.
$\boxtimes$ Nayyar A. Zaidi
nayyar.zaidi@monash.edu
Geoffrey I. Webb
geoff.webb@monash.edu
Mark J. Carman
mark.carman@monash.edu
François Petitjean
francois.petitjean@monash.edu
Wray Buntine
wray.buntine@monash.edu
Mike Hynes
mbhynes@uwaterloo.ca
Hans De Sterck
hans.desterck@monash.edu
1 Faculty of Information Technology, Monash University, Clayton, VIC 3800, Australia
2 Department of Applied Mathematics, University of Waterloo, Waterloo, Canada
3 School of Mathematical Sciences, Monash University, Clayton, VIC 3800, Australia

both generative and discriminative methods. The proposed method is discriminative in nature, but uses estimates of generative probabilities to speed-up the optimization process. A second contribution is to propose a simple framework to characterize the parameter learning task for Bayesian network classifiers. We conduct an extensive set of experiments on 72 standard datasets and demonstrate that our proposed discriminative parameterization provides an efficient alternative to other state-of-the-art parameterizations.

# 1 Introduction 

Efficient training of Bayesian Network Classifiers has been the topic of much recent research (Buntine 1994; Carvalho et al. 2011; Friedman et al. 1997; Heckerman and Meek 1997; Martinez et al. 2016; Pernkopf and Bilms 2010; Webb et al. 2012; Zaidi et al. 2013). Two paradigms predominate (Jebara 2003). One can optimize the log-likelihood (LL). This is traditionally called generative learning. The goal is to obtain parameters characterizing the joint distribution in the form of local conditional distributions and then estimate class-conditional probabilities using Bayes rule. Alternatively, one can optimize the conditional-log-likelihood (CLL)—known as discriminative learning. The goal is to directly estimate the parameters associated with the class-conditional distribution- $\mathrm{P}(y \mid \mathbf{x})$.

Naive Bayes (NB) is a Bayesian network BN that specifies independence between attributes given the class. Recent work has shown that placing a per-attribute-value-per-classvalue weight on probabilities in NB (and learning these weights by optimizing the CLL) leads to an alternative parameterization of vanilla Logistic Regression (LR) (Zaidi et al. 2014). The introduction of these weights (and optimizing them by maximizing CLL) also makes it possible to relax NB's conditional independence assumption and thus to create a classifier with lower bias ( Ng and Jordan 2002; Zaidi et al. 2014). The classifier is low-biased, as weights can remedy inaccuracies introduced by invalid attribute-independence assumptions.

In this paper, we generalize this idea to the general class of BN classifiers. Like NB, any given BN structure encodes assumptions about conditional independencies between the attributes and will result in error if they do not hold in the data. Optimizing the log-likelihood in this case will result in suboptimal performance for classification (Friedman et al. 1997; Grossman and Domingos 2004; Su et al. 2008) and one should either optimize directly the CLL by learning the parameters of the class-conditional distribution or by placing weights on the probabilities and learn these weights by optimizing the CLL.

The main contributions of this paper are:

1. We develop a new discriminative parameter learning method for Bayesian network classifiers by combining fast generative parameter (and structure) learning with subsequent fast discriminative parameter estimation (using parameter estimates from the former to precondition search for the parameters of the latter). To achieve this, discriminative parameters are restated as weights rectifying deviations of the discriminative model from the generative one (in terms of the violation of independence between factors present in the generative model).
2. A second contribution of this work is the development of a simple framework to characterize the parameter learning task for Bayesian network classifiers. Building on previous work by Friedman et al. (1997), Greiner et al. (2005), Pernkopf and Wohlmayr (2009), Roos et al. (2005) and Zaidi et al. (2013), this framework allows us to lay out the different techniques in a systematic manner; highlighting similarities, distinctions and equivalences.

Our proposed parameterization is based on a two-step learning process:

1. Generative step: We maximize the LL to obtain parameters for all local conditional distributions in the BN.
2. Discriminative step: We associate a weight with each parameter learned in the generative step and re-parameterize the class-conditional distribution in terms of these weights (and of the fixed generative parameters). We can then discriminatively learn these weights by optimizing the CLL.

In this paper, we show that:

- The proposed formalization of the parameter learning task for BN is actually a reparameterization of the one step (discriminative) learning problem (this will become clear when we introduce the proposed framework) but with faster convergence of the discriminative optimization procedure. In the experimental section, we complement our theoretical framework with an empirical analysis over 72 domains; the results demonstrate the superiority of our approach. In Sect. 5.5, we will discuss our proposed approach from the perspective of pre-conditioning in unconstrained optimization problems.
- The proposed approach results in a three-level hierarchy of nested parameterizations, where each additional level introduces (or "unties") exponentially more parameters in order to fit ever smaller violations of independence.
- Regularization of the discriminative parameters in the proposed discriminative learning approach allows to limit the amount of allowable violation of independence and effectively interpolate between discriminative and generative parameter estimation.

The rest of this paper is organized as follows. In Sect. 2, we present our proposed framework for parameter learning of Bayesian network classifiers. We also give the formulation for class-conditional Bayesian Network models (CCBN) in this section. Two established parameterizations of class-conditional Bayesian networks are given in Sects. 3 and 4, respectively. In Sect. 5, we present our proposed parameterization of CCBN. In Sect. 6, we discuss some related work to this research. Experimental analysis is conducted in Sect. 7. We conclude in Sect. 8 with some pointers to future work.

All the symbols used in this work are listed in Table 1.

# 2 A simple framework for parameter learning of BN classifiers 

We start by discussing Bayesian network classifiers in the following section.

### 2.1 Bayesian network classifiers

A BN $\mathcal{B}=\langle\mathcal{G}, \Theta\rangle$, is characterized by the structure $\mathcal{G}$ (a directed acyclic graph, where each vertex is a variable, $Z_{i}$ ), and a set of parameters $\Theta$, that quantifies the dependencies within the structure. The variables are partitioned into a single target, the class variable $Y=Z_{0}$ and $n$ covariates $X_{1}=Z_{1}, X_{2}=Z_{2}, \ldots X_{n}=Z_{n}$, called the attributes. The parameter $\Theta$, contains a set of parameters for each vertex in $\mathcal{G}: \theta_{z_{0} \mid \Pi_{0}(\mathbf{x})}$ and for $1 \leq i \leq n, \theta_{z_{i} \mid y, \Pi_{i}(\mathbf{x})}$, where $\Pi_{i}($.$) is a function which given the datum \mathbf{x}=\left\langle x_{1}, x_{1}, \ldots, x_{n}\right\rangle$ as its input, returns the values of the attributes that are the parents of node $i$ in structure $\mathcal{G}$. For notational simplicity, instead of writing $\theta_{Z_{0}=z_{0} \mid \Pi_{0}(\mathbf{x})}$ and $\theta_{Z_{i}=z_{i} \mid y, \Pi_{i}(\mathbf{x})}$, we write $\theta_{z_{0} \mid \Pi_{0}(\mathbf{x})}$ and $\theta_{z_{i} \mid y, \Pi_{i}(\mathbf{x})}$. A BN $\mathcal{B}$ computes the joint probability distribution as: $\mathrm{P}_{\mathcal{B}}(y, \mathbf{x})=\theta_{z_{0} \mid \Pi_{0}(\mathbf{x})} \cdot \prod_{i=1}^{n} \theta_{z_{i} \mid y, \Pi_{i}(\mathbf{x})}$.

Table 1 List of symbols used


For a BN $\mathcal{B}$, we can write:

$$
\mathrm{P}_{\mathcal{B}}(y, \mathbf{x})=\theta_{y \mid \Pi_{0}(\mathbf{x})} \prod_{i=1}^{n} \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}
$$

Now, the corresponding conditional distribution $\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})$ can be computed with the Bayes rule as:

$$
\begin{aligned}
\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x}) & =\frac{\mathrm{P}_{\mathcal{B}}(y, \mathbf{x})}{\mathrm{P}_{\mathcal{B}}(\mathbf{x})} \\
& =\frac{\theta_{y \mid \Pi_{0}(\mathbf{x})} \prod_{i=1}^{n} \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}}{\sum_{y^{\prime} \in \mathcal{Y}} \theta_{y^{\prime} \mid \Pi_{0}(\mathbf{x})} \prod_{i=1}^{n} \theta_{x_{i} \mid y^{\prime}, \Pi_{i}(\mathbf{x})}}
\end{aligned}
$$

If the class attribute does not have any parents, we write: $\theta_{y \mid \Pi_{0}(\mathbf{x})}=\theta_{y}$.
Given a set of data points $\mathcal{D}=\left\{\mathbf{x}^{(1)}, \ldots, \mathbf{x}^{(N)}\right\}$, the Log-Likelihood (LL) of $\mathcal{B}$ is:

$$
\begin{aligned}
\mathrm{LL}(\mathcal{B}) & =\sum_{j=1}^{N} \log \mathrm{P}_{\mathcal{B}}\left(y^{(j)}, \mathbf{x}^{(j)}\right) \\
& =\sum_{j=1}^{N}\left(\log \theta_{y^{(j)} \mid \Pi_{0}\left(\mathbf{x}^{(j)}\right)}+\sum_{i=1}^{n} \log \theta_{x_{i}^{(j)} \mid \Pi_{i}\left(\mathbf{x}^{(j)}\right)}\right) \\
\text { with } \quad & \sum_{y \in \mathcal{Y}} \theta_{y \mid \Pi_{0}(\mathbf{x})}=1, \text { and } \sum_{x_{i} \in \mathcal{X}_{i}} \theta_{x_{i} \mid \Pi_{i}(\mathbf{x})}=1
\end{aligned}
$$

Maximizing Eq. 3 to optimize the parameters $(\theta)$ is the maximum-likelihood estimation of the parameters.

Theorem 1 Within the constraints in Eq. 4, Eq. 3 is maximized when $\theta_{x_{i} \mid \Pi_{i}(\mathbf{x})}$ corresponds to empirical estimates of probabilities from the data, that is, $\theta_{y \mid \Pi_{0}(\mathbf{x})}=\mathrm{P}_{\mathcal{D}}\left(y \mid \Pi_{0}(\mathbf{x})\right)$ and $\theta_{x_{i} \mid \Pi_{i}(\mathbf{x})}=\mathrm{P}_{\mathcal{D}}\left(x_{i} \mid \Pi_{i}(\mathbf{x})\right)$.

Proof See "Appendix 1".

The parameters obtained by maximizing Eq. 3 (and fulfilling the constraints in Eq. 4) are typically known as 'Generative' estimates of the probabilities.

# 2.2 Class-conditional BN (CCBN) models 

Instead of following a two-step process for classification with BN, where step 1 involves maximizing $\mathrm{P}(y, \mathbf{x})$ and the second step is application of Bayes rule to obtain $\mathrm{P}(y \mid \mathbf{x})$, one can directly optimize for $\mathrm{P}(y \mid \mathbf{x})$ by maximizing the Conditional Log-Likelihood (CLL). Optimizing CLL is generally considered a more effective objective function (for classification) since it directly optimizes the mapping from features to class labels. The CLL can be defined as:

$$
\operatorname{CLL}(\mathcal{B})=\sum_{j=1}^{N} \log \mathrm{P}_{\mathcal{B}}\left(y^{(j)} \mid \mathbf{x}^{(j)}\right)
$$

which is equal to:

$$
\begin{aligned}
= & \sum_{j=1}^{N}\left(\log \mathrm{P}_{\mathcal{B}}\left(y^{(j)}, \mathbf{x}^{(j)}\right)-\log \sum_{y^{\prime}}^{|\mathcal{Y}|} \mathrm{P}_{\mathcal{B}}\left(y^{\prime}, \mathbf{x}^{(j)}\right)\right) \\
= & \sum_{j=1}^{N}\left(\log \theta_{y^{(j)} \mid \Pi_{0}\left(\mathbf{x}^{(j)}\right)}+\sum_{i=1}^{n} \log \theta_{x_{i}^{(j)} \mid \Pi_{i}\left(\mathbf{x}^{(j)}\right)}\right) \\
& -\log \left(\sum_{y^{\prime}}^{|\mathcal{Y}|} \theta_{y^{\prime} \mid \Pi_{0}\left(\mathbf{x}^{(j)}\right)} \prod_{i=1}^{n} \theta_{x_{i} \mid y^{\prime}, \Pi_{i}\left(\mathbf{x}^{(j)}\right)}\right)
\end{aligned}
$$

The only difference between Eqs. 3 and 5 is the presence of the normalization factor in the latter, that is: $\log \sum_{y^{\prime}}^{|\mathcal{Y}|} \mathrm{P}_{\mathcal{B}}\left(y^{\prime}, \mathbf{x}^{(j)}\right)$. Due to this normalization, the values of $\theta$ maximizing Eq. 5 are not the same as those that maximize Eq. 3. We provide two intuitions as to why maximizing the CLL should provide a better model of the conditional distribution:

1. It allows the parameters to be set in such a way as to reduce the effect of the conditional attribute independence assumption that is present in the BN structure and that might be violated in data.
2. We have $\operatorname{LL}(\mathcal{B})=\operatorname{CLL}(\mathcal{B})+\operatorname{LL}(\mathcal{B} \backslash y)$. If optimizing $\operatorname{LL}(\mathcal{B})$, most of the attention will be given to $\operatorname{LL}(\mathcal{B} \backslash y)$ —because $\operatorname{CLL}(\mathcal{B}) \ll \operatorname{LL}(\mathcal{B} \backslash y)$ —which will often lead to poor estimates for classification.

Note, that if the structure is correct, maximizing both LL and CLL should lead to the same results (Rubinstein and Hastie 1997). There is unfortunately no closed-form solution for $\theta$ such that the CLL would be maximized; we thus have to resort to numerical optimization methods over the space of parameters.

Like any Bayesian network model, a class-conditional BN model is composed of a graphical structure and of parameters $(\boldsymbol{\theta})$ quantifying the dependencies in the structure. For any BN $\mathcal{B}$, the corresponding CCBN will be based on graph $\mathcal{B}^{*}$ (where $\mathcal{B}^{*}$ is a sub-graph of $\mathcal{B})$ whose parameters are optimized by maximizing the CLL. We present below a slightly rephrased definition from Roos et al. (2005):

Definition 1 A class-conditional Bayesian network model $\mathcal{M}^{\mathcal{B}^{*}}$ is the set of conditional distributions based on the network $\mathcal{B}^{*}$ equipped with any strictly positive parameter set $\boldsymbol{\theta}^{\mathcal{B}^{*}}$; that is the set of all functions from $\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ to a distribution on $Y$ takes the form of Eq. 2 .

This means that the nodes in $\mathcal{B}^{*}$ are nodes comprising only the Markov blanket of the class $y$. However, for most BN classifiers the class has no parents and is made a parent of all attributes. This has the effect that every attribute is in the Markov blanket of the class.

We will assume that the parents of the class attribute constitute an empty set and, therefore, replace parameters characterizing the class attribute from $\theta_{y^{(j)} \mid \Pi_{0}\left(\mathbf{x}^{(j)}\right)}$ with $\theta_{y^{(j)}}$. We will also drop the superscript $j$ in equations for clarity.

# 2.3 A simple framework 

It is no exaggeration to say that Eq. 1 has a pivotal role in BN classification. Let us modify Eq. 1 by introducing an extra set of parameter, say $w$ for every parameter $\theta$. Let $\boldsymbol{\theta}$ and $\mathbf{w}$, represent the vectors of all $\theta$ and $w$ parameters. In the following, let us also make a distinction

between 'Fixed' and 'Optimized' parameters-during the optimization process. Parameters that are optimized are referred to as Optimized parameters and parameters that do not change their value during the optimization process are referred to as Fixed. Now, we can write:

$$
\mathrm{P}_{\mathcal{B}}(y, \mathbf{x})=\theta_{y}^{w_{y}} \prod_{i=1}^{n} \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}^{w_{x_{i}, y, \Pi_{i}(\mathbf{x})}}
$$

Optimizing to compute class-probabilities using Eq. 6, there are several possibilities, of which we will discuss only four in the following:

1. Generative: Initialize $\mathbf{w}$ with 1 and treat it as fixed parameter. Treat, $\boldsymbol{\theta}$ as optimized parameter and optimize it with the generative objective function as given in Eq. 3.
2. Discriminative: Initialize $\mathbf{w}$ with 1 and treat it as fixed parameter. Treat, $\boldsymbol{\theta}$ as an optimized parameter and optimize it with the discriminative objective function as given in Eq. 5. As discussed, this results in adding a normalization term to convert $\mathrm{P}(y, \mathbf{x})$ in Eq. 6 to $\mathrm{P}(y \mid \mathbf{x})$. We denote this 'discriminative CCBN' and describe it in detail in Sect. 3.
3. Discriminative: Initialize $\mathbf{w}$ with 1 and treat it as a fixed parameter. Treat, $\boldsymbol{\theta}$ as an optimized parameter and optimize it with the discriminative objective function as given in Eq. 5, but constrain parameter $\boldsymbol{\theta}$ to be actual probabilities. We denote this 'extended CCBN' and provide a detailed description in Sect. 4.
4. Discriminative: Two step learning. In the first step, initialize $\mathbf{w}$ with 1 and treat it as a fixed parameter. Treat, $\boldsymbol{\theta}$ as an optimized parameter and optimize it with the generative objective function as given in Eq. 3. In the second step, treat $\boldsymbol{\theta}$ as a fixed parameter and optimize for $\mathbf{w}$ using a discriminative objective function. This approach is inspired from the fact that weights $\mathbf{w}$ in Eq. 6 are set through generative learning, unlike discriminative and extended CCBN, where it is set to one. We denote this 'weighted CCBN' and describe it in detail in Sect. 5.

A brief summary of these parameterizations is also given in Table 2.

# 3 Parameterization 1: Discriminative CCBN model 

Logistic regression (LR) is the CCBN model associated to the NB structure optimizing Eq. 2. Typically, LR learns a weight for each attribute-value (per-class). However, one can extend LR by considering all or some subset of possible quadratic, cubic, or higher-order features (Langford et al. 2007; Zaidi et al. 2015). Inspired from Roos et al. (2005), we define discriminative CCBN as:

Definition 2 A discriminative class-conditional Bayesian network model $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ is a CCBN such that Eq. 2 is re-parameterized in form of parameter $\boldsymbol{\beta}$ such that $\boldsymbol{\beta}=\log \boldsymbol{\theta}$ and parameter $\boldsymbol{\beta}$ is obtained by maximizing the CLL.

Let us re-define $\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})$ in Eq. 5 and write it on a per datum basis as:

$$
\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})=\frac{\exp \left(\log \theta_{y}+\sum_{i=1}^{n} \log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}\right)}{\sum_{y^{\prime}}^{\mid \mathcal{Y} \mid} \exp \left(\log \theta_{y^{\prime}}+\sum_{i=1}^{n} \log \theta_{x_{i} \mid y^{\prime}, \Pi_{i}(\mathbf{x})}\right)}
$$

In light of Definition 2, let us define a parameter $\beta_{\bullet}$ that is associated with each parameter $\theta_{\bullet}$ in Eq. 7, such that:

$$
\log \theta_{y}=\beta_{y}, \quad \text { and } \quad \log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}=\beta_{y, x_{i}, \Pi_{i}}
$$

Table 2 Comparison of different parameter learning techniques for Bayesian network classifiers


Now Eq. 7 can be written as:

$$
\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})=\frac{\exp \left(\beta_{y}+\sum_{i=1}^{n} \beta_{y, x_{i}, \Pi_{i}}\right)}{\sum_{y^{\prime}=1}^{|\mathcal{Y}|} \exp \left(\sum_{y^{\prime}} \beta_{y^{\prime}}+\sum_{i=1}^{n} \beta_{y^{\prime}, x_{i}, \Pi_{i}}\right)}
$$

One can see that this has led to the logistic function of the form $\frac{1}{1+\exp \left(-\beta^{T} \mathbf{x}\right)}$ for binary classification and softmax $\frac{\exp \left(-\beta_{\mathbf{y}}{ }^{T} \mathbf{x}\right)}{\sum_{i}^{\prime}\left(\exp \left(-\beta_{\mathbf{y}^{\prime}}{ }^{T} \mathbf{x}\right)\right)}$ for multi-class classification. Such a formulation is a Logistic Regression classifier. Therefore, we can state that a discriminative CCBN model with naive Bayes structure is a (vanilla) logistic regression classifier.

In light of Definition 2, CLL optimized by $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$, on a per-datum-basis, can be specified as:

$$
\begin{aligned}
\log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})= & \left(\beta_{y}+\sum_{i=1}^{n} \beta_{y, x_{i}, \Pi_{i}}\right) \\
& -\log \left(\sum_{y^{\prime}=1}^{|\mathcal{Y}|} \exp \left(\beta_{y^{\prime}}+\sum_{i=1}^{n} \beta_{y^{\prime}, x_{i}, \Pi_{i}}\right)\right)
\end{aligned}
$$

Now, we will have to rely on an iterative optimization procedure based on gradient-descent. Therefore, let us first calculate the gradient of parameters in the model. The gradient of the parameters in Eq. 9 can be computed as:

$$
\frac{\partial \log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})}{\partial \beta_{y: k}}=\left(\mathbf{1}_{y=k}-\mathrm{P}(k \mid \mathbf{x})\right)
$$

for the class parameters. For the other parameters, we can compute the gradient as:

$$
\frac{\partial \log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})}{\partial \beta_{y: k, x_{i}: j, \Pi_{i}: l}}=\left(\mathbf{1}_{y=k}-\mathrm{P}(k \mid \mathbf{x})\right) \mathbf{1}_{x_{i}=j} \mathbf{1}_{\Pi_{i}=l}
$$

where $\mathbf{1}$ is the indicator function. Note, that we have used the notation $\beta_{y: k, x_{i}: j, \Pi_{i}: l}$ to denote that class y has the value k , attribute $x_{i}$ has the value j and its parents $\left(\Pi_{i}\right)$ have the value $l$. If the attribute has multiple parent attributes, then $l$ represents a combination of parent attribute values.

# 4 Parameterization 2: Extended CCBN model 

The name Extended CCBN Model is inspired from Greiner et al. (2005), where the method named Extended Logistic Regression (ELR) is proposed. ELR is aimed at extending LR and leads to discriminative training of BN parameters. We define:

Definition 3 (Greiner et al. 2005) An extended class-conditional Bayesian network model $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ is a CCBN such that the parameters $(\boldsymbol{\theta})$ satisfy the constraints in Eq. 4 and is obtained by maximizing the CLL in Eq. 5.

Let us re-define $\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})$ in Eq. 5 on a per-datum-basis as:

$$
\begin{aligned}
\log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})= & \left(\log \theta_{y}+\sum_{i=1}^{n} \log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}\right) \\
& -\log \sum_{y^{\prime}}^{\left|y^{\prime}\right|}\left(\theta_{y^{\prime}} \prod_{i=1}^{n} \theta_{x_{i} \mid y^{\prime}, \Pi_{i}(\mathbf{x})}\right)
\end{aligned}
$$

Let us consider the case of optimizing parameters associated with the attributes $\theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}$. Parameters associated with the class can be obtained similarly. We will re-write $\theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}$ as $\theta_{x_{i}: j \mid y: k, \Pi_{i}: l}$ which represents attribute $i\left(x_{i}\right)$ taking value $j$, class $(y)$ taking value $k$ and its parents $\left(\Pi_{i}\right)$ takes value $l$. Now we can write the gradient as:

$$
\begin{aligned}
\frac{\partial \log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})}{\partial \theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}} & =\left(\frac{\mathbf{1}_{y=k} \mathbf{1}_{x_{i}=j^{\prime}} \mathbf{1}_{\Pi_{i}=l}}{\theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}}-\frac{\hat{\mathrm{P}}(k \mid \mathbf{x}) \mathbf{1}_{x_{i}=j^{\prime}} \mathbf{1}_{\Pi_{i}=l}}{\theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}}\right) \\
& =\frac{\mathbf{1}_{x_{i}=j^{\prime}} \mathbf{1}_{\Pi_{i}=l}}{\theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}}\left(\mathbf{1}_{y=k}-\hat{\mathrm{P}}(k \mid \mathbf{x})\right)
\end{aligned}
$$

Enforcing constraints that $\sum_{j^{\prime}} \theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}=1$, we introduce a new parameters $\beta$ and re-parameterize as:

$$
\theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}=\frac{\exp \left(\beta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}\right)}{\sum_{j^{\prime \prime}} \exp \left(\beta_{x_{i}: j^{\prime \prime} \mid y: k, \Pi_{i}: l}\right)}
$$

It will be helpful if we differentiate $\theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}$ with respect to $\beta_{x_{i}: j \mid y: k, \Pi_{i}: l}$ (the use of notation $j$ and $j^{\prime}$ will become obvious when we apply the chain rule afterwards), we get:

$$
\begin{aligned}
\frac{\partial \theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}}{\partial \beta_{x_{i}: j \mid y: k, \Pi_{i}: l}}= & \frac{\exp \left(\beta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}\right) \mathbf{1}_{y=k} \mathbf{1}_{x_{i}=j^{\prime}=j} \mathbf{1}_{\Pi_{i}=l}}{\sum_{j^{\prime \prime}} \exp \left(\beta_{x_{i}: j^{\prime \prime} \mid y: k, \Pi_{i}: l}\right)} \\
& \frac{\exp \left(\beta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}\right) \exp \left(\beta_{x_{i}: j^{\prime \prime} \mid y: k, \Pi_{i}: l}\right) \mathbf{1}_{x_{i}=j^{\prime \prime}=j} \mathbf{1}_{\Pi_{i}=l}}{\left(\sum_{j^{\prime \prime}} \exp \left(\beta_{x_{i}: j^{\prime \prime} \mid y: k, \Pi_{i}: l}\right)\right)^{2}} \\
= & \mathbf{1}_{y=k} \mathbf{1}_{x_{i}=j^{\prime}=j} \mathbf{1}_{\Pi_{i}=l} \theta_{x_{i}: j \mid y: k, \Pi_{i}: l} \\
& -\mathbf{1}_{x_{i}=j^{\prime \prime}=j} \mathbf{1}_{\Pi_{i}=l} \theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l} \theta_{x_{i}: j \mid y: k, \Pi_{i}: l} \\
= & \left(\mathbf{1}_{y=k}-\theta_{x_{i}: j \mid y: k, \Pi_{i}: l}\right) \mathbf{1}_{x_{i}=j} \mathbf{1}_{\Pi_{i}=l} \theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}
\end{aligned}
$$

Applying the chain rule:

$$
\begin{aligned}
\frac{\partial \log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})}{\partial \beta_{x_{i}: j \mid y: k, \Pi_{i}: l}}= & \sum_{j^{\prime}} \frac{\partial \log \mathrm{P}(y \mid \mathbf{x})}{\partial \theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}} \frac{\partial \theta_{x_{i}: j^{\prime} \mid y: k, \Pi_{i}: l}}{\partial \beta_{x_{i}: j \mid y: k, \Pi_{i}: l}} \\
= & \left(\mathbf{1}_{y=k} \mathbf{1}_{x_{i}=j} \mathbf{1}_{\Pi_{i}=l}-\mathbf{1}_{x_{i}=j} \mathbf{1}_{\Pi_{i}=l} \mathrm{P}(k \mid \mathbf{x})\right) \\
& -\theta_{x_{i}: j \mid y: k, \Pi_{i}: l} \sum_{j^{\prime}}\left(\mathbf{1}_{y=k} \mathbf{1}_{x_{i}=j^{\prime}} \mathbf{1}_{\Pi_{i}=l}-\mathbf{1}_{x_{i}=j^{\prime}} \mathbf{1}_{\Pi_{i}=l} \mathrm{P}(k \mid \mathbf{x})\right)
\end{aligned}
$$

we get the gradient of $\log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})$ with respect to parameter $\beta_{x_{i}: j \mid y: k, \Pi_{i}: l}$. Now one can use the transformation of Eq. 13 to obtain the desired parameters of extended CCBN. Note that Eq. 14 corresponds to Eq. 11. The only difference is the presence of the normalization term that is subtracted from the gradient in Eq. 14.

# 5 Parameterization 3: Combined generative/discriminative parameterization: weighted CCBN model 

Inspired from Zaidi et al. (2014), we define a weighted CCBN model as follows:
Definition 4 A weighted conditional Bayesian network model $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ is a CCBN such that Eq. 2 has an extra weight parameter associated with every $\theta$ such that it is re-parameterized as: $\boldsymbol{\theta}^{\mathbf{w}}$, where parameter $\boldsymbol{\theta}$ is learned by optimizing the LL and parameter $\mathbf{w}$ is obtained by maximizing the CLL.

In light of Definition 4, let us re-define Eq. 2 to incorporate weights as:

$$
\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})=\frac{\theta_{y}^{w_{y}} \prod_{i=1}^{n} \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}^{w_{y, x_{i}, \Pi_{i}}}{\sum_{y^{\prime}}^{\left|3^{\prime}\right|} \theta_{y^{\prime}}^{w_{y^{\prime}}} \prod_{i=1}^{n} \theta_{x_{i} \mid y^{\prime}, \Pi_{i}(\mathbf{x})}^{w_{y^{\prime}, x_{i}, \Pi_{i}}}
$$

The corresponding weighted CLL can be written as:

$$
\begin{aligned}
\log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})= & \left(w_{y} \log \theta_{y}+\sum_{i=1}^{n} w_{y, x_{i}, \Pi_{i}} \log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}\right) \\
& -\log \sum_{y^{\prime}}^{\left|3^{\prime}\right|}\left(\theta_{y^{\prime}}^{w_{y}} \prod_{i=1}^{n} \theta_{x_{i} \mid y^{\prime}, \Pi_{i}(\mathbf{x})}^{w_{y, x_{i}, \Pi_{i}}\right)
\end{aligned}
$$

Note, that Eq. 16 is similar to Eq. 12 except for the introduction of weight parameters. The flexibility to learn parameter $\boldsymbol{\theta}$ in a prior generative process of learning greatly simplifies subsequent calculations of $\mathbf{w}$ in a discriminative search. Since $\mathbf{w}$ is a free-parameter and there is no sum-to-one constraint, its optimization is simpler than for $\mathcal{M}_{\theta}^{\mathcal{B}^{*}}$. The gradient of the parameters in Eq. 16 can be computed as:

$$
\frac{\partial \log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})}{\partial w_{y: k}}=\left(\mathbf{1}_{y=k}-\mathrm{P}(k \mid \mathbf{x})\right) \log \theta_{y \mid \Pi_{0}(\mathbf{x})}
$$

for the class $y$, while for the other parameters:

$$
\frac{\partial \log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})}{\partial w_{y: k, x_{i}: j, \Pi_{i}: l}}=\left(\mathbf{1}_{y=k}-\mathrm{P}(k \mid \mathbf{x})\right) \mathbf{1}_{x_{i}=j} \mathbf{1}_{\Pi_{i}=l} \log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}
$$

One can see that Eqs. 17 and 18 correspond to Eqs. 10 and 11. The only difference between them is the presence of the $\log \theta_{\bullet}$ factor in the $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ case.

### 5.1 On initialization of parameters

Initialization of the parameters, which sets the starting point for the optimization, is critical to the speed of convergence and will be addressed in this section. Obviously, a better starting point (in terms of CLL), will make the optimization easier and conversely, a worse starting point will make optimization harder. In this paper, we will study two different starting points for the parameters:

Initialization with Zeros This is the standard initialization where all the optimized parameters are initialized with 0 (Ripley 1996).
Initialization with Generative estimates Given that our approach utilizes generative estimates, a fair comparison with other approaches should study starting from the generative estimates for all approaches. This will correspond to initializing the $\boldsymbol{\theta}$ parameter with

the generative estimates for Parameterizations 1 and $2\left(\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}\right.$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ ), and initializing the $\mathbf{w}$ parameter to 1 for Parameterization $3\left(\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}\right)$.

Note that in the initialization with "Zeros" case, only our proposed Weighted CCBN parameterization requires a first (extra) pass over the dataset to compute the generative estimates, while for the initialization with "Generative estimates" case all methods require this pass (when we report training time, we always report the full training time).

# 5.2 Comment on regularization 

$\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ parameterization offers an elegant framework for blending discriminatively and generatively learned parameters. With regularization, one can indeed 'interpolate' between the two sets of parameters. Traditionally, one regularizes parameters towards 0 to prevent over-fitting. For example, let us modify Eq. 15 to integrate an L2-regularization:

$$
\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})=\frac{1}{\mathcal{Z}} \exp \left(w_{y} \log \theta_{y}+\sum_{i=1}^{n} w_{y, x_{i}, \Pi_{i}} \log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}\right)+\frac{\lambda}{2}\|\mathbf{w}\|^{2}
$$

where $\mathcal{Z}$ is the normalization constant and $\lambda$ is the parameter controlling regularization. The new term will penalize large (and heterogeneous) parameter values. Larger $\lambda$ values will cause the classifier to progressively ignore the data and assign more uniform class probabilities. Alternatively one could penalize deviations from the BN conditional independence assumption by centering the regularization term at 1 rather than zero. In this case, we can write:

$$
\mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})=\frac{1}{\mathcal{Z}} \exp \left(w_{y} \log \theta_{y}+\sum_{i=1}^{n} w_{y, x_{i}, \Pi_{i}} \log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}\right)+\frac{\lambda}{2}\|\mathbf{w}-\mathbf{1}\|^{2}
$$

Doing so allows the regularization parameter $\lambda$ to be used to 'pull' the dicriminative estimates toward the generative ones. A very small value of $\lambda$ results in optimized parameter $\mathbf{w}$ dominating the determination of $\mathrm{P}(y \mid \mathbf{x})$, whereas, a very large value of $\lambda$ pulls $\mathbf{w}$ towards 1 and, therefore, the fixed parameters will dominate the class-conditional probabilities. Regularization for $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ remains an area for future research, but we conjecture that one can tune a value of $\lambda$ (for example through cross-validation) to attain better performance than can be achieved by either generative or discriminative parameters alone. Once could also interpret the regularization parameter as controlling the amount of independence violation between the discriminative and generative models.

### 5.3 Optimizing discriminative/generative parameterization

There are great advantages in optimizing an objective function that is convex. The convexity of the three discriminative parameterizations that we have discussed depends on the underlying structure of the CCBN $\left(\mathcal{M}^{\mathcal{B}^{*}}\right)$. From Roos et al. (2005), it follows that optimizing a CCBN parameterized by either $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}, \mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ or $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ leads to a convex optimization problem if and only if the structure has no immoral nodes. In other words, the optimization problem is convex if and only if parents of all the nodes are are connected with each other. This constraint is true for a number of popular BN classifiers including NB, TAN and KDB $(K=1)$, but not true for general BN or for KDB structures with $K>1$. Therefore, in this work, we have used only limited BN structures such as NB, TAN and KDB $(K=1)$. Investigation of the application of our approach to more complex moral structures is a promising topic for future work. We note in passing, that a similar two step discriminative parameterization has also

![img-0.jpeg](img-0.jpeg)

Fig. 1 Depiction of various levels in parameter nesting, along with number of parameters $(m)$ to be optimized at each level. Note that only one node per level is expanded, for illustration. Attribute $X_{1}$ takes values $\{a, b, c\}$ and takes class $Y=\{0,1\}$ and attribute $X_{2}=\{d, e, f\}$ as parents
been shown to be effective for the non-convex objective function mean-square-error (Zaidi et al. 2016).

# 5.4 Nested parameterizations 

One can see that learning $\mathcal{M}_{\mathrm{d}}^{B^{*}}, \mathcal{M}_{\mathrm{e}}^{B^{*}}$ and $\mathcal{M}_{\mathrm{w}}^{B^{*}}$ models can lead to a large number of parameters that needs to be optimized discriminatively, even on moderate size datasets. One can, however, nest these parameters. The idea is to exploit relationships between parameters so that the number of parameters that need to be optimized are reduced significantly. Figure 1 depicts four levels of parameter nesting. The first level entails learning a parameter for each attribute. The second level entails learning a parameter for every attribute-value. The next level learns a parameter for every attribute-value-per-class-value. The final level (Level 4) is the most comprehensive case. It entails learning a parameter for every attribute-value-per-class-per-parent-value.

Nesting as shown in Fig. 1, though effective, is not very intuitive for $\mathcal{M}_{\mathrm{e}}^{B^{*}}$ and $\mathcal{M}_{\mathrm{d}}^{B^{*}}$. For example, doing a logistic regression by learning a parameter associated only with the attributes will result in optimizing fewer parameters but might not be effective in terms of classification accuracy. However, the hierarchy of models applies naturally to $\mathcal{M}_{\mathrm{w}}^{B^{*}} . \mathcal{M}_{\mathrm{w}}^{B^{*}}$ incorporates learning initial parameters by optimizing the LL objective function. Therefore, the searched parameters optimized in the second step can be nested effectively. For example, Level 1 weighting in Fig. 1 can be seen as alleviating the conditional attribute independence assumption (CAIA) between attributes. Similarly, Level 2 will have the effect of binarizing each attribute, and alleviating CAIA between new attributes. In the following we will derive the respective gradients for each level from the most comprehensive case of Level 4.

Gradients for Level 4 are given in Eqs. 17 and 18. Level 3 corresponds to learning a weight-per-attribute-value-per-class. The weight vector in this case will be of the size $m=$ $\sum_{i}\left(|Y| \times\left|X_{i}\right|\right)$. The gradients with respect to new weight vectors can be obtained in the following way:

$$
\frac{\partial \log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})}{\partial w_{x_{i} \mid j \mid y: k}}=\left(\mathbf{1}_{y=k}-\mathrm{P}(k \mid \mathbf{x})\right) \mathbf{1}_{x_{i}=j} \log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}
$$

Level 2 weighting corresponds to learning a weight-per-attribute-value. We can compute the gradient with respect to the weight vector of size $m=\sum_{i}\left|X_{i}\right|$, as:

$$
\frac{\partial \log \mathrm{P}_{\mathcal{B}}(y \mid \mathbf{x})}{\partial w_{x_{i} \mid j}}=\left(\log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}-\sum_{y^{\prime}} \mathrm{P}\left(y^{\prime} \mid \mathbf{x}\right) \log \theta_{x_{i} \mid y^{\prime}, \Pi_{i}(\mathbf{x})}\right) \mathbf{1}_{x_{i}=j}
$$

Similarly, learning a weight-per-attribute leads to a weight vector of size $m$ and can its gradients can be obtained as:

$$
\frac{\partial \log \mathrm{PB}(y \mid \mathbf{x})}{\partial w_{i}}=\log \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}-\sum_{y^{\prime}} \mathrm{P}\left(y^{\prime} \mid \mathbf{x}\right) \log \theta_{x_{i} \mid y^{\prime}, \Pi_{i}(\mathbf{x})}
$$

Now, one can control the bias and variance of the classifier by selecting between three different levels of parameterization with ever greater model complexity.

# 5.5 Discussion 

### 5.5.1 Pre-conditioning: why is our technique helpful?

It can be seen that $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ results in re-scaling of $\mathcal{M}_{\beta}^{\mathcal{B}^{*}}$ parameterization. What is the effect of this re-scaling on the model? Since there is no closed-form solution, we optimize the CLL with first-order gradient-descent methods, such as gradient descent, conjugate gradient, quasi-Newton (L-BGFS) or Stochastic Gradient Descent. These are all affected by scaling. ${ }^{1}$ We use the generative estimates as an effective pre-conditioning method.

A pre-conditioner converts an ill-conditioned problem into a better conditioned one, such that the gradient of the objective function is uniform across all dimensions. A better conditioned optimization problem has a better convergence profile. This is because if different parameters have significantly different "influence" on the objective function, then the gradient does not point directly towards the minimum that is the objective of the optimization process. We illustrate this in Fig. 2 where we show the contour plot of the CLL for different $\beta$. We can see that when the CLL has an 'elliptical' shape with respect to the parameters, then the gradient is not oriented directly towards the objective and each step makes only partial progress in the true direction of the final objective. Our re-scaling improves the orientation of the gradient speeding convergence.

Note that it is the relative scaling of the axes that affects the orientation of the gradient. Isotropic scaling (that is, scaling all axes uniformly) has no effect on convergence.

To further demonstrate our point, we perform a simple experiment with synthetic data that we generate so that the CLL is more or less "elliptical". We use with three binary features and two class values. We sample the covariates randomly and uniformly and use a simple

[^0]
[^0]:    ${ }^{1}$ Note that second-order algorithms such as the Newton method are not affected by scaling, but they are often computationally impractical because they require computation and inversion of the Hessian at each step.

![img-1.jpeg](img-1.jpeg)

Fig. 2 On the importance of scaling for first-order gradient descent methods. Axes represent two possible $\beta_{1}$ and $\beta_{2}$. Left non-scaled space. Right re-scaled space
![img-2.jpeg](img-2.jpeg)

Fig. 3 Comparison of rate of convergence on the three synthetic datasets by varying $\alpha$. The $X$-axis is on log scale. Parameters are initialized to zero
logistic regression model, which corresponds to our framework using Naive Bayes as the BN structure. The class distribution is given by

$$
\mathrm{P}\left(y \mid x_{1}, x_{2}, x_{3}\right)=\frac{1}{\exp \left(-\left(10^{\alpha} \cdot x_{1}+1 \cdot x_{2}+10^{-\alpha} \cdot x_{3}\right)\right)}
$$

By increasing the value of $\alpha$, we increase the elongation of the CLL space. When $\alpha=0$, the three features contribute uniformly to the class prediction and it is a well-conditioned problem. We can then expect pre-conditioning to have little to no influence on the convergence. As $\alpha \rightarrow 1$, the problem becomes very ill-conditioned. On such problems, pre-conditioning will have greatest effect.

We compare the convergence profile of vanilla LR (discriminative CCBN) and our preconditioned weighted CCBN with Naive Bayes structure (which is associated to a LR model) by varying $\alpha$ from 0 to 1 . For each dataset 10000 data points were generated. We report the convergence results in Fig. 3. These confirm the explanation given above. The benefit of

our technique progressively increases as the relative influence of the covariates on the class increases. We will show in Sect. 7 that this is the case for the vast majority of real-world datasets.

# 5.5.2 Is this an over-parametrised model? 

It can be seen that the $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ parameterization is based on Eq. 6-which is over-parameterized in the sense that there are twice as many parameters specifying the likelihood as would strictly be necessary. The question is: do we benefit from having both $\mathbf{w}$ and $\boldsymbol{\theta}$ parameters? In this section, we will discuss the implications of introducing $\mathbf{w}$ parameters to the following vanilla (per-datum) likelihood (on which $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ is based on):

$$
\mathrm{P}_{\mathcal{B}}(y, \mathbf{x})=\theta_{y} \prod_{i=1}^{n} \theta_{x_{i} \mid y, \Pi_{i}(\mathbf{x})}
$$

If one goal of weighted CCBN is to combine generative and discriminative learning by using over-parameterized likelihood in Eq. 6, one could do the following two-step learning. In step 1, one can learn the $\boldsymbol{\theta}$ by optimizing a generative objective function, and in the second step, optimize a discriminative objective function but initialize the $\boldsymbol{\theta}$ parameters with the parameters that were obtained in step 1. In fact, this should be a recommended procedure to speed-up discriminative training (for discriminative CCBN and extended CCBN) as it is often effective in practice. However, one should notice that in this case, the discriminative learning model does start from the estimates of parameters that were obtained from generative learning, but once an iterative step is taken for discriminative learning, the generative estimates are lost, and have no further influence on the discriminative learning process.

## 6 Related work

There have been several comparative studies of discriminative and generative structure and parameter learning of Bayesian networks (Greiner and Zhou 2002; Grossman and Domingos 2004; Pernkopf and Bilmes 2005). In all these works, generative parameter training is the estimation of parameters based on empirical estimates whereas discriminative training of parameters is actually the estimation of the parameters of CCBN models such as $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ or $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$. The $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ model was first proposed in Greiner and Zhou (2002). Our work differs from these previous works as our goal is to highlight different parameterization of CCBN models and investigate their inter-relationship. Particularly, we are interested in the learning of parameters corresponding to a weighted CCBN model that leads to faster discriminative learning.

An approach for discriminative learning of the parameters of BN based on discriminative computation of pseudo-frequencies from the data is presented in Su et al. (2008). Discriminative Frequency Estimates (DFE) are computed by injecting a discriminative element to generative computation of the probabilities. During the pseudo-frequencies computation process, rather than using empirical frequencies, DFE estimates how well the current classifier does on each data point and then updates the frequency tables only in proportion to the classifier's performance. For example, they propose a simple error measure, as: $L(\mathbf{x})=\mathrm{P}(y \mid \mathbf{x})-\hat{\mathrm{P}}(y \mid \mathbf{x})$, where $\mathrm{P}(y \mid \mathbf{x})$ is the true probability of class $y$ given the datum $\mathbf{x}$, and $\hat{\mathrm{P}}(y \mid \mathbf{x})$ is the predicted probability. The counts are updated as: $\theta_{i j k}^{t+1}=\theta_{i j k}^{t}+L(\mathbf{x})$.

Several iterations over the dataset are required. The algorithm is inspired from Perceptron based training and is shown to be an effective discriminative parameter learning approach.

# 7 Empirical results 

In this section, we compare and analyze the performance of our proposed algorithms and related methods on 72 natural domains from the UCI repository of machine learning (Frank and Asuncion 2010). The experiments are conducted on the datasets described in Table 3.

There are a total of 72 datasets, 41 datasets with less than 1000 instances, 21 datasets with between 1000 and 10000 instances, and 11 datasets with more than 10000 instances. Each algorithm is tested on each dataset using 5 rounds of 2 -fold cross validation. 2 -fold cross validation is used in order to maximize the variation in the training data from trial to trial, which is advantageous when estimating bias and variance. Note that the source code with running instructions is provided as a supplementary material to this paper.

We compare four metrics: $0-1$ Loss, RMSE, Bias and Variance. The reason for performing bias/variance estimation is to investigate if optimizing a discriminative function leads to a lower bias classifier or not. There are a number of different bias-variance decomposition definitions. In this research, we use the bias and variance definitions of Kohavi and Wolpert (1996) together with the repeated cross-validation bias-variance estimation method proposed by Webb (2000). Kohavi and Wolpert (1996) define bias and variance as follows:

$$
\operatorname{bias}^{2}=\frac{1}{2} \sum_{y \in \mathcal{Y}}\left(\mathrm{P}(y \mid \mathbf{x})-\hat{\mathrm{P}}(y \mid \mathbf{x})\right)^{2}
$$

and

$$
\text { variance }=\frac{1}{2}\left(1-\sum_{y \in \mathcal{Y}} \hat{\mathrm{P}}(y \mid \mathbf{x})^{2}\right)
$$

The reason for reporting $0-1$ Loss and RMSE is to investigate if the proposed parameterization $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ leads to a comparable performance to $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ parameterizations and also to determine how much performance gain is achieved over generative learning. We will also evaluate parameterizations in terms of training time (measured in seconds) and number of iterations it takes each parameterization to converge.

We report Win-Draw-Loss (W-D-L) results when comparing the $0-1$ Loss, RMSE, bias and variance of two models. A two-tail binomial sign test is used to determine the significance of the results. Results are considered significant if $p \leq 0.05$. Significant results are shown in bold font in the table.

We report results on two categories of datasets. The first category, labeled All, consists of all datasets in Table 3. The second category, labeled Big, consists of datasets that have more than 10000 instances. The reason for splitting datasets into two categories is to show explicitly the effectiveness of our proposed optimization on bigger datasets ${ }^{2}$. It is only on big datasets, that each iteration is expensive and, therefore, any technique that leads to faster and better convergence is highly desirable. Note, that we do not expect the three discriminative parameterizations $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}, \mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ to differ in their prediction accuracy. That is, we should expect a similar spread of both $0-1$ Loss and RMSE values. However, we should be interested in each parameterization's convergence profile and the training time.

[^0]
[^0]:    ${ }^{2}$ By big, we mean datasets that have large number of instances, rather than large number of features

Table 3 Details of Datasets (UCI Domains)


Table 3 continued


Numeric attributes are discretized using the Minimum Description Length (MDL) discretization method (Fayyad and Irani 1992). A missing value is treated as a separate attribute value and taken into account exactly like other values.

Optimization is done with L-BFGS (Byrd et al. 1995) using the original implementation available at http://users.eecs.northwestern.edu/ nocedal/lbfgsb.html. Following standard procedures (Zhu et al. 1997), the algorithm terminates when improvement in the objective function, given by $\frac{\left|f_{i}-f_{i+1}\right|}{\max \left\{\left|f_{i}\right|,\left|f_{i+1}\right|, 1\right\}}$, drops below $10^{-32}$, or the number of iterations exceeds $10^{4}$.

We experiment with three Bayesian network structures that is: naive Bayes (NB), TreeAugmented naive Bayes (TAN) (Friedman et al. 1997) and k-Dependence Bayesian network (KDB) with $K=1$ (Sahami 1996). Naive Bayes, is a well-known classifier which is based on the assumption that when conditioned on the class, attributes are independent. TreeAugmented Naive Bayes augments the NB structure by allowing each attribute to depend on at most one non-class attribute. It relies on an extension of the Chow-Liu tree (Chow and Liu 1968), that utilizes conditional mutual information (between pairs of attributes given the class) to find a maximum spanning tree over the attributes in order to determine the parent of each. Similarly, in KDB, each attribute takes $k$ attributes plus the class as its parents. The attributes are selected based on their mutual information with the class. Then, the parent of an attribute $i$ is chosen that maximizes the conditional mutual information of attribute $i$ and parent $j$ given the class that is: $\operatorname{argmax}_{j} \operatorname{CMI}\left(X_{i}, X_{j} \mid Y\right)$.

We denote $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}, \mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ with naive Bayes structure as $\mathrm{NB}^{\mathrm{w}}, \mathrm{NB}^{\mathrm{d}}$ and $\mathrm{NB}^{\mathrm{e}}$ respectively. With TAN structure, $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}, \mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ are denoted as $\mathrm{TAN}^{\mathrm{w}}, \mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{TAN}^{\mathrm{e}}$. With $\operatorname{KDB}(K=1), \mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}, \mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ are denoted as $\mathrm{KDB}-1^{\mathrm{w}}, \mathrm{KDB}-1^{\mathrm{d}}$ and $\mathrm{KDB}-1^{\mathrm{e}}$.

As discussed in Sect. 5.1, we initialize the parameters to the log of the MAP estimates (or parameters optimized by generative learning). The following naming convention is used in the results:

- The ' $(\mathrm{I})$ ' in the label represents this initialization
- An absence of '(I)' means the parameters are initialized to zero.


# 7.1 NB structure 

Comparative scatter plots on all 72 datasets for $0-1$ Loss, RMSE and training time values for $\mathrm{NB}^{\mathrm{w}}, \mathrm{NB}^{\mathrm{d}}$ and $\mathrm{NB}^{\mathrm{e}}$ are shown in Fig. 4. Training time plots are on the log scale. The plots are shown separately for Big datasets. It can be seen that the three parameterizations have a similar spread of $0-1$ Loss and RMSE values, however, $\mathrm{NB}^{\mathrm{w}}$ is greatly advantaged in terms of its training time. We will see in Sect. 7.4 that this computational advantage arises due to the desirable convergence property of $\mathrm{NB}^{\mathrm{w}}$. Given that $\mathrm{NB}^{\mathrm{w}}$ achieves equivalent accuracy with much less computation indicates that it is a more effective parameterization than $\mathrm{NB}^{\mathrm{d}}$ and $\mathrm{NB}^{\mathrm{e}}$. Slight variation in the accuracy of three discriminative parameterizations (that is $0-1$ Loss and RMSE performance) on All datasets is due to the numerical instability of the solver use for optimization. The difference mainly arises on very small datasets. It can be seen that on big datasets, the three parameterizations result in the same accuracy.

The geometric means of the $0-1$ Loss and RMSE results are shown in Fig. 5. It can be seen that the three discriminative parameterizations, especially on Big datasets, has much better performance (both $0-1$ Loss and RMSE) than the generative learning.

The training time comparison is given in Fig. 6a. Note that the training time is measured in seconds and is plotted on the log scale. It can be seen that in terms of the training time,

![img-3.jpeg](img-3.jpeg)

Fig. 4 Comparative scatter of results for $\mathrm{NB}^{\mathrm{w}}, \mathrm{NB}^{\mathrm{d}}$ and $\mathrm{NB}^{\mathrm{e}}$. $\mathrm{NB}^{\mathrm{w}}$ is on the $X$-axis whereas $\mathrm{NB}^{\mathrm{d}}$ (red-cross) and $\mathrm{NB}^{\mathrm{e}}$ (green-triangle) are on the $Y$-axis. For any points above the diagonal line $\mathrm{NB}^{\mathrm{w}}$ wins

![img-4.jpeg](img-4.jpeg)

Fig. 5 Geometric mean of $0-1$ Loss and RMSE for $\mathrm{NB}, \mathrm{NB}^{\mathrm{w}}, \mathrm{NB}^{\mathrm{d}}$ and $\mathrm{NB}^{\mathrm{e}}$ on $A l l$ and $B i g$ datasets. Results are normalized with respect to NB
![img-5.jpeg](img-5.jpeg)

Fig. 6 a Geometric mean of training time for $\mathrm{NB}, \mathrm{NB}^{\mathrm{w}}, \mathrm{NB}^{\mathrm{d}}$ and $\mathrm{NB}^{\mathrm{e}}$ on $A l l$ and $B i g$ datasets. Results are normalized with respect to NB. b Geometric mean of training time for $\mathrm{NB}^{\mathrm{w}}, \mathrm{NB}^{\mathrm{d}}$ and $\mathrm{NB}^{\mathrm{e}}$ on $A l l$ and $B i g$ datasets. Results are normalized with respect to $\mathrm{NB}^{\mathrm{w}}$
the three discriminative parameterizations are many orders of magnitude slower than plain naive Bayes. To show the comparison of the training time of $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}, \mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ only, we normalize the results with respect to $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$. Results are shown in Fig. 6b. It can be seen that $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ is almost twice as slow as compared to $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$, whereas, $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ is order of magnitude slower that $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$.

# 7.2 TAN structure 

Figure 7 shows the comparative spread of $0-1$ Loss, RMSE and training time in seconds of $\mathrm{TAN}^{\mathrm{w}}, \mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{TAN}^{\mathrm{e}}$ on $A l l$ and $B i g$ datasets. A trend similar to that of NB can be seen. With a similar spread of $0-1$ Loss and RMSE among the three parameterizations, training time is greatly improved for $\mathrm{TAN}^{\mathrm{w}}$ when compared with $\mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{TAN}^{\mathrm{e}}$. Note, as pointed out before, that minor variation in the performance of three discriminative parameterizations is due to the numerical issues with-in the solver on some small datasets. On big datasets, one can see a similar spread of $0-1$ Loss and RMSE.

The geometric means of the $0-1$ Loss and RMSE results are shown in Fig. 8. It can be seen that $\mathrm{TAN}^{\mathrm{d}}, \mathrm{TAN}^{\mathrm{e}}$ and $\mathrm{TAN}^{\mathrm{w}}$, on average results in much better accuracy than generative model (TAN).

A comparison of the training time is shown in Fig. 9a. It can be seen that, like NB, training time of the discriminative methods is orders of magnitude longer than that of generative learning. Note, the training time of discriminative learning also includes the structure learning process. We also show the comparison of the training time of $\mathrm{TAN}^{\mathrm{d}}, \mathrm{TAN}^{\mathrm{e}}$ and $\mathrm{TAN}^{\mathrm{w}}$ in

![img-6.jpeg](img-6.jpeg)

Fig. 7 Comparative scatter of results for $\mathrm{TAN}^{\mathrm{w}}, \mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{TAN}^{\mathrm{e}}$. TAN $^{\mathrm{w}}$ is on the $X$-axis whereas TAN ${ }^{\mathrm{d}}$ (red-cross) and $\mathrm{TAN}^{\mathrm{e}}$ (green-triangle) are on the $Y$-axis. For any points above the diagonal line $\mathrm{TAN}^{\mathrm{w}}$ wins

![img-7.jpeg](img-7.jpeg)

Fig. 8 Geometric mean of $0-1$ Loss and RMSE for TAN ${ }^{\mathrm{w}}$, TAN $^{\mathrm{d}}$ and TAN ${ }^{\mathrm{e}}$ on $A l l$ and $B i g$ datasets. Results are normalized with respect to TAN
![img-8.jpeg](img-8.jpeg)

Fig. 9 a Geometric mean of training time for TAN, TAN ${ }^{\mathrm{w}}, \mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{TAN}^{\mathrm{e}}$ on $A l l$ and $B i g$ datasets. Results are normalized with respect to NB. b Geometric mean of training time for TAN ${ }^{\mathrm{w}}, \mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{TAN}^{\mathrm{e}}$ on $A l l$ and $B i g$ datasets. Results are normalized with respect to TAN ${ }^{\mathrm{w}}$

Fig. 9b. Like, NB, it can be seen that TAN ${ }^{\mathrm{w}}$ is almost twice as fast as TAN ${ }^{\mathrm{d}}$, whereas, TAN ${ }^{\mathrm{e}}$ is orders of magnitude slower than TAN ${ }^{\mathrm{w}}$.

# 7.3 KDB $(K=1)$ structure 

Figure 10 shows the comparative spread of $0-1$ Loss, RMSE and training time in seconds of KDB- $1^{\mathrm{w}}$, KDB- $1^{\mathrm{d}}$ and KDB- $1^{\mathrm{e}}$ on $A l l$ and $B i g$ datasets. Like NB and TAN, it can be seen that a similar spread of $0-1$ Loss and RMSE is present among the three parameterizations of discriminative learning. Similarly, it can be seen that training time is greatly improved for KDB- $1^{\mathrm{w}}$ when compared with KDB- $1^{\mathrm{d}}$ and KDB- $1^{\mathrm{e}}$.

Geometric average of the $0-1$ Loss and RMSE results are shown in Fig. 11. It can be seen that the three discriminative parameterizations have better $0-1$ Loss and RMSE than generative learning (KDB-1).

A comparison of the training time is given in Fig. 12a. Note, the training time of discriminative methods also includes the time of structure learning. It can be seen that discriminative learning leads to a significantly longer training time than generative learning. We compare the training time of KDB- $1^{\mathrm{d}}$, KDB- $1^{\mathrm{e}}$ and KDB- $1^{\mathrm{w}}$ in Fig. 12b. Like, NB and TAN structure, it can be seen that KDB- $1^{\mathrm{w}}$ is faster than both KDB- $1^{\mathrm{d}}$ and KDB- $1^{\mathrm{e}}$.

![img-9.jpeg](img-9.jpeg)

Fig. 10 Comparative scatter of results for $\mathrm{KDB}-1^{\mathrm{w}}, \mathrm{KDB}-1^{\mathrm{d}}$ and $\mathrm{KDB}-1^{\mathrm{e}}$. KDB-1 ${ }^{\mathrm{w}}$ is on the $X$-axis whereas KDB-1 ${ }^{\mathrm{d}}$ (red-cross) and KDB-1 ${ }^{\mathrm{e}}$ (green-triangle) are on the $Y$-axis. For any points above the diagonal line KDB-1 ${ }^{\mathrm{w}}$ wins

![img-10.jpeg](img-10.jpeg)

Fig. 11 Geometric mean of training time and RMSE for KDB-1 ${ }^{\mathrm{w}}$, KDB-1 ${ }^{\mathrm{d}}$ and KDB-1 ${ }^{\mathrm{e}}$ on All and Big datasets. Results are normalized with respect to KDB-1
![img-11.jpeg](img-11.jpeg)

Fig. 12 a Geometric mean of training time for KDB1, KDB-1 ${ }^{\mathrm{w}}$, KDB-1 ${ }^{\mathrm{d}}$ and KDB-1 ${ }^{\mathrm{e}}$ on All and Big datasets. Results are normalized with respect to NB. b Geometric mean of training time for KDB-1 ${ }^{\mathrm{w}}, \mathrm{KDB}-1^{\mathrm{d}}$ and KDB-1 ${ }^{\mathrm{e}}$ on All and Big datasets. Results are normalized with respect to KDB-1 ${ }^{\mathrm{w}}$

# 7.4 Convergence analysis 

A comparison of the convergence of Negative Log-Likelihood (NLL) of the three parameterizations on some sample datasets with NB, TAN and KDB $(K=1)$ structure is shown in Figs. 13 and 14.

As discussed in Sect. 5.1, in Fig. 13, parameters are initialized to zero, whereas, in Fig. 14, parameters are initialized to the log of the MAP estimates. It can be seen that for all three structures and for both initializations, $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ not only converges faster but also reaches its asymptotic value much quicker than the $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$. The same trend was observed on all 72 datasets. A comparison on many more datasets is given in Figs. 18 and 19 in Appendix 2.

To quantify how much $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ is faster than the other two parameterizations, we plot a histogram of the number of iterations it takes $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$ after five iterations to reach the negative log-likelihood that $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ achieved in the fifth iteration. If the three parameterizations follow similar convergence, one should expect many zeros in the histogram. Note that if after the fifth iteration, NLL of $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ is greater than that of $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$, we we plot the negative of the number of iterations it takes $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ to reach the NLL of $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$. Similarly, if after the fifth iteration, NLL of $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ is greater than that of $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$, we we plot the negative of the number of iterations it takes $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ to reach the NLL of $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$. Figures 15, 16 and 17 show these

![img-12.jpeg](img-12.jpeg)

Fig. 13 Comparison of rate of convergence on the four biggest datasets for NB, TAN and KDB $(K=1)$ (right column) structures. The $X$-axis is on log scale. Parameters are initialized to zero. Note, the first iteration is actually NLL before the start of optimization. It can be seen that the three parameterizations start from the same point in the space
histogram plots for NB, TAN and $\operatorname{KDB}(K=1)$ structure respectively. It can be seen that $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ (with all three structures) achieves a NLL that otherwise, will take on average 10 more iterations over the data for $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and 15 more iterations for $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$. This is an extremely useful property of $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ especially for big data where iterating through the dataset is expensive.

![img-13.jpeg](img-13.jpeg)

Fig. 14 Comparison of rate of convergence on the four biggest datasets for NB, TAN and $\operatorname{KDB}(K=1)$ (right column) structures. The $X$-axis is on log scale. Parameters are initialized to the log of the MAP estimates. Note, the first iteration is actually NLL before the start of optimization. It can be seen that the three parameterizations start from the same point in the space

# 7.5 Comparison with MAP 

The purpose of this section is to compare the performance of the discriminative learning with that of generative learning. In Table 4, we compare the performance of $\mathrm{NB}^{\mathrm{w}}$ with NB (i.e., naive Bayes with MAP estimates of probabilities), TAN ${ }^{\mathrm{w}}$ with TAN (i.e., TAN with MAP estimates of probabilities) and KDB-1 ${ }^{\mathrm{w}}$ with $\operatorname{KDB}(K=1)$ (i.e., KDB with MAP estimates

![img-14.jpeg](img-14.jpeg)

![img-15.jpeg](img-15.jpeg)

Fig. 16 Number of iterations (after 5 iterations), it takes $\mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{TAN}^{\mathrm{e}}$ to reach NLL that $\mathrm{TAN}^{\mathrm{w}}$ achieved after 5 iterations. If NLL of $\mathrm{TAN}^{\mathrm{w}}$ is less that that of $\mathrm{TAN}^{\mathrm{d}}$ or $\mathrm{TAN}^{\mathrm{e}}$, (negative of the) number of iterations it takes $\mathrm{TAN}^{\mathrm{w}}$ to reach that of $\mathrm{TAN}^{\mathrm{d}}$ and that of $\mathrm{TAN}^{\mathrm{e}}$ are plotted with negative sign

![img-16.jpeg](img-16.jpeg)

Table 4 Win-Draw-Loss: $\mathrm{NB}^{\mathrm{w}}$ versus $\mathrm{NB}, \mathrm{TAN}^{\mathrm{w}}$ versus TAN and $\mathrm{KDB}-1^{\mathrm{w}}$ versus KDB-1


Significant results are shown in bold
of probabilities). We use $\mathrm{NB}^{\mathrm{w}}, \mathrm{TAN}^{\mathrm{w}}$ and $\mathrm{KDB}-1^{\mathrm{w}}$ as a representative of discriminative learning - since $\mathcal{M}_{\mathrm{w}}^{B^{*}}, \mathcal{M}_{\mathrm{d}}^{B^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{B^{*}}$ have similar $0-1$ Loss and RMSE profile. It can be see that the discriminative learning of parameters has significantly lower bias but higher variance. On big datasets, it can be seen that discriminative learning results in much better $0-1$ Loss and RMSE performance.

Note that though discriminative learning (optimizes the parameters characterizing CCBN) has better $0-1$ Loss and RMSE performance than generative learning (optimizing joint probability),-generative learning has the advantage of being extremely fast as it incorporates counting of sufficient statistics from the data. Another advantage of generative learning is its capability of back-off in case a certain combination does not exist in the data. For example, if TAN or KDB classifiers have not encountered a <feature-value, parent-value, class-value> combination at training time they can resort back to <feature-value, class-value> at testing time. For instance TAN classifier can step back to NB and NB can step back to class prior probabilities. Such elegantly back-tracking is missing from discriminative learning. If a certain combination does not exist in the data, parameters associated to that combination will not be optimized and will remain fixed to the initialized value (for example 0 ). A discriminative classifier will have no way of handling unseen combinations but to ignore them if they occur in the testing data. How to incorporate such hierarchical learning with discriminative learning is the goal of future research as will be discussed in Sect. 8.

# 8 Conclusion and future work 

In this paper, we propose an effective parameterization of BN. We present a unified framework for learning the parameters of Bayesian network classifiers. We formulate three different parameterizations and compare their performance in terms of $0-1$ Loss, RMSE and training time each parameterization took to converge. We show with NB, TAN and KDB structures that the proposed weighted discriminative parameterization has similar $0-1$ Loss and RMSE to the other two but significantly faster convergence. We also show that it not only has faster convergence but it also asymptotes to its global minimum much quicker than the other two parameterizations. This is desirable when learning from huge quantities of data

with Stochastic Gradient Descent (SGD). It is also shown that discriminative training of BN classifiers also leads to lower bias than the generative parameter learning.

We plan to conduct following future work as the result of this study:

- The three parameterizations presented in this work learn a weight for each attribute-value-per-class-value-per-parent-values. As discussed in Sect. 5.4, contrary to $\mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$, $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}$ parameterization can generalize parameters. For example, once MAP estimates of probabilities are learned, one can learn a weight: (a) for each attribute only (i.e., same weight for all attribute-values, for all class values and for all parent values), (b) for each attribute-value only, (c) for each attribute-value-per-class-value, (d) for each attribute-value-per-class-value-per-parent, etc. Such parameter generalization could offer additional speed-up of the training and is a promising avenue for future research.
- Handling combinations of 〈feature-value, parent-value, class-value〉 that have not been seen at training time is one of the weaker properties of discriminative learning. We plan to design an hierarchical algorithm of discriminative learning that can learn lower-level discriminative weights and can back-off from higher levels if a combination is not observed in the training data.
- We plan to conduct an extended analysis of BN models that can capture higher-order interactions. Because the CLL is not convex for most of these models (Roos et al. 2005), it falls outside the scope of this paper. This does, however, suggest inviting avenues for big data research, in which context low-bias classifiers are required.


# 9 Code and datasets 

All the datasets used in this paper are in the public domain and can be downloaded from Frank and Asuncion (2010). Code with running instructions can be download from https://github. com/nayyarzaidi/EBNC.git.

Acknowledgements This research has been supported by the Australian Research Council (ARC) under Grant DP140100087. This material is based upon work supported by the Air Force Office of Scientific Research, Asian Office of Aerospace Research and Development (AOARD) under Award Numbers FA2386-15-1-4007 and FA2386-16-1-4023. The authors would like to thank Reza Haffari and Ana Martinez for helpful discussion during the course of this research. Authors would like to acknowledge Jeusus Cerquides for his extremely useful ideas and suggestions that shaped this work.

## Appendix 1: Proof of Theorem 1

Let us use Lagrange multipliers for constraints in Eq. 4 to be placed in Eq. 3. Now, we can maximize the resulting objective function:

$$
\mathrm{LL}(\mathcal{B})+\lambda_{0}\left(1-\sum_{y \in \mathcal{Y}} \theta_{y \mid \Pi_{0(\mathbf{x})}}\right)+\sum_{i}^{n} \lambda_{i}\left(1-\sum_{x_{i} \in \mathcal{X}_{i}} \theta_{x_{i} \mid \Pi_{i}(\mathbf{x})}\right)
$$

by first computing its derivative as:

$$
\frac{\partial \mathrm{LL}(\mathcal{B})}{\partial \theta_{x_{i} \mid \Pi_{i}(\mathbf{x})}}=\sum_{j=1}^{N} \frac{\mathbf{1}_{x_{i}^{(j)}=x_{i}} \mathbf{1}_{y^{(j)}=y} \mathbf{1}_{\Pi_{i}^{(j)}(\mathbf{x})=\Pi_{i}(\mathbf{x})}}{\theta_{x_{i}^{(j)} \mid \Pi_{i}(\mathbf{x})}}-\lambda_{i}
$$

and then setting it to zero. This will lead to

$$
\theta_{x_{i} \mid \Pi_{i}(\mathbf{x})}=\frac{\sum_{j=1}^{N} N_{x_{i}, y, \Pi_{i}(\mathbf{x})}}{\lambda_{i}}
$$

where $N_{x_{i}, y, \Pi_{i}(\mathbf{x})}$ is the empirical count of instances with attribute $i$ taking value $x_{i}$, class taking value $y$ and parents taking value $\Pi_{i}(\mathbf{x})$. Placing $\theta_{x_{i} \mid \Pi_{i}(\mathbf{x})}$ value in Eq. 4, we get:

$$
\sum_{x_{i} \in \mathcal{X}_{i}} \frac{\sum_{j=1}^{N} N_{x_{i}, y, \Pi_{i}(\mathbf{x})}}{\lambda_{i}}=1
$$

which implies: $\lambda_{i}=\sum_{x_{i} \in \mathcal{X}_{i}} \sum_{j=1}^{N} N_{x_{i}, y, \Pi_{i}(\mathbf{x})}$. Therefore, $\lambda_{i}=N_{y, \Pi_{i}(\mathbf{x})}$. Hence we can write:

$$
\theta_{x_{i} \mid \Pi_{i}(\mathbf{x})}=\frac{N_{x_{i}, y, \Pi_{i}(\mathbf{x})}}{N_{y, \Pi_{i}(\mathbf{x})}} . \quad \text { Similarly: } \quad \theta_{y \mid \Pi_{0}(\mathbf{x})}=\frac{N_{y, \Pi_{0}(\mathbf{x})}}{N_{\Pi_{0}(\mathbf{x})}}
$$

This equals empirical estimates of probabilities from the data: $\mathrm{P}_{\mathcal{D}}\left(x_{i} \mid \Pi_{i}(\mathbf{x})\right)$.

# Appendix 2: Convegence curves 

Continued from Sect. 7.4, in this section, we present some more results to compare the convergences of three discriminative parameterizations. In Fig. 18, we initialize the parameterizations with the generative estimates, whereas, in Fig. 19, parameters are initialized to zero.

## Appendix 3: Training time significance test

Let us discuss the significance of the training time for three discriminative parameterizations using Friedman and Nemenyi tests. Following procedure is taken to generate the results:

- We have three algorithms to compare that is: $\mathcal{M}_{\mathrm{w}}^{\mathcal{B}^{*}}, \mathcal{M}_{\mathrm{d}}^{\mathcal{B}^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{\mathcal{B}^{*}}$, therefore, $k=3$.
- We compare the results on 72 datasets, therefore, $N=72$.
- Friedman test rank each algorithm for each dataset separately. In case of ties, it uses average ranks.
- If $r_{i}^{j}$ is the rank of algorithm $j$ on $i$-th dataset, average rank for each algorithm compared are computed as: $R_{j}=\frac{1}{N} \sum_{i} r_{i}^{j}$.
- We state:
- Null hypothesis-Algorithms are equivalent and, therefore, ranks should be equal. Mean rank is 2.5 .
- $p$ value-probability of getting ranks $R_{j}$ if null-hypothesis as stated in previous point is true.
- Compute the Friedman statistics:

$$
\chi_{F}^{2}=\frac{12 N}{k(k+1)}\left[\sum_{j} R_{j}^{2}-\frac{k(k+1)^{2}}{4}\right]
$$

![img-17.jpeg](img-17.jpeg)

Fig. 18 Comparison of rate of convergence on the six sample datasets for NB (left column), TAN (middle column) and KDB $(K=1)$ (right row) structures. The $X$-axis is on log scale. Parameters are initialized to the $\log$ of the MAP estimates

![img-18.jpeg](img-18.jpeg)

Fig. 19 Comparison of rate of convergence on the four biggest datasets for NB (left column), TAN (middle column) and $\operatorname{KDB}(K=1)$ (right row) structures. The $X$-axis is on log scale. Parameters are initialized to 0

![img-19.jpeg](img-19.jpeg)

Fig. 20 Significance testing of Training time (a) and No. of Iterations (b) to converge for three parameterizations $\mathrm{NB}^{\mathrm{w}}, \mathrm{NB}^{\mathrm{d}}$ and $\mathrm{NB}^{\mathrm{e}}$, with Friedman and Nemenyi test on All datasets. Ranks are different according to Friedman test and, therefore, null-hypothesis is rejected. (Nemenyi) Post-hoc test is powerful
to determine if the measure ranks are significantly different from the mean rank of 2.5 (under null hypothesis).

- If the $p$ value is $\leq 0.05$, we reject the null hypothesis and proceed with the post-hoc test.
- We use the Nemenyi test which states that the performance of two algorithms is significantly different if the corresponding average ranks differ by at least the critical difference (CD) of:

$$
\mathrm{CD}=q_{\alpha} \sqrt{\frac{k(k+1)}{6 N}}
$$

where $q_{\alpha}$ in our experiments is 2.3430 as $k=3$.

- If the difference between top rank and the bottom rank is less than the CD, we conclude pos-hoc test to be not powerful.
- Otherwise [following the graphical representation of Demšar (2006)], we plot the ranks (along with the name of algorithm) on a horizontal line. Algorithms are connected by a line if their differences are not significant. We also show the CD on the same scale to highlight the significance of the difference of two ranks.

![img-20.jpeg](img-20.jpeg)

Fig. 21 Significance testing of Training time (a) and No. of Iterations (b) to converge for three parameterizations $\mathrm{TAN}^{\mathrm{w}}, \mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{TAN}^{\mathrm{e}}$, with Friedman and Nemenyi test on All datasets. Ranks are different according to Friedman test and, therefore, null-hypothesis is rejected. (Nemenyi) Post-hoc test is powerful

We show the significance test using Friedman and Nemenyi test on All datasets in terms of training time and no. of iterations it takes each algorithm to converge in Figs. 20, 21 and 22. It can be seen that for all three structures that is NB, TAN and KDB-1, $\mathcal{M}_{\mathrm{w}}^{B^{*}}$ is rank lower than $\mathcal{M}_{\mathrm{d}}^{B^{*}}$ and $\mathcal{M}_{\mathrm{e}}^{B^{*}}$ both in terms of training time and no. of iterations.

For NB and TAN, $\mathcal{M}_{\mathrm{w}}^{B^{*}}$ has significantly better training time and converges in far fewer iterations than the other two. However, for KDB-1 structure, the difference is not significant between $\mathcal{M}_{\mathrm{w}}^{B^{*}}$ and $\mathcal{M}_{\mathrm{d}}^{B^{*}}$.

# Appendix 4: Convergence significance test 

We compare the NLL obtained by each parameterization at fifth (denoted as NLL (5)), tenth (denoted as NLL (10)) and fiftieth (denoted as NLL (50)) iteration and presented results in terms of win-draw-loss in Table 5 for $\mathcal{M}_{\mathrm{w}}^{B^{*}}$ versus $\mathcal{M}_{\mathrm{d}}^{B^{*}}$ and for $\mathcal{M}_{\mathrm{w}}^{B^{*}}$ versus $\mathcal{M}_{\mathrm{e}}^{B^{*}}$ in Table 6. It can be seen from the two tables, that $\mathcal{M}_{\mathrm{w}}^{B^{*}}$ wins significantly against $\mathcal{M}_{\mathrm{d}}^{B^{*}}$ with all three structures. The trend is extremely impressive when comparing against 12 big datasets.

![img-21.jpeg](img-21.jpeg)

Fig. 22 Significance testing of Training time (a) and No. of Iterations (b) to converge for three parameterizations $\mathrm{KDB}-1^{\mathrm{w}}, \mathrm{KDB}-1^{\mathrm{d}}$ and $\mathrm{KDB}-1^{\mathrm{e}}$, with Friedman and Nemenyi test on All datasets. Ranks are different according to Friedman test and, therefore, null-hypothesis is rejected. (Nemenyi) Post-hoc test is powerful

Table 5 Win-Draw-Loss: $\mathrm{NB}^{\mathrm{w}}$ versus $\mathrm{NB}^{\mathrm{d}}, \mathrm{TAN}^{\mathrm{w}}$ versus $\mathrm{TAN}^{\mathrm{d}}$ and $\mathrm{KDB}-1^{\mathrm{w}}$ versus $\mathrm{KDB}-1^{\mathrm{d}}$


Significant results are shown in bold

Table 6 Win-Draw-Loss: $\mathrm{NB}^{\mathrm{w}}$ versus $\mathrm{NB}^{\mathrm{e}}$, $\mathrm{TAN}^{\mathrm{w}}$ versus $\mathrm{TAN}^{\mathrm{e}}$ and $\mathrm{KDB}-1^{\mathrm{w}}$ versus $\mathrm{KDB}-1^{\mathrm{e}}$


Significant results are shown in bold

Since, each iteration encompasses looping through all the data, these are datasets where each iteration is expensive. It can be seen that $\mathcal{M}_{\mathrm{w}}^{\mathrm{B}^{*}}$ achieves a better NLL not only after fifth and tenth iteration, but better even after fiftieth iteration.
