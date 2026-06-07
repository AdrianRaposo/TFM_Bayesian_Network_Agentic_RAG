# Circular Bayesian classifiers using wrapped Cauchy distributions 

Ignacio Leguey ${ }^{a, b, *}$, Concha Bielza ${ }^{\text {b }}$, Pedro Larrañaga ${ }^{\text {b }}$<br>${ }^{a}$ Departamento de Economía Financiera y Contabilidad e Idioma Moderno, Facultad de Ciencias Jurídicas y Sociales, Universidad Rey Juan Carlos de Madrid, Spain<br>${ }^{\text {b }}$ Departamento de Inteligencia Artificial, Universidad Politécnica de Madrid, Campus de Montegancedo, 28660 Boadilla del Monte, Madrid, Spain

## A R T I C L E I N F O

Keywords:
Data mining
Classification
Circular statistics
Wrapped Cauchy distribution
Bayesian networks
Cortical layer

## A B S T R A C T

Capturing the dependences among circular variables within supervised classification models is a challenging task. In this paper, we propose four different supervised Bayesian classification algorithms where the predictor variables follow all circular wrapped Cauchy distributions. For this purpose, we introduce four wrapped Cauchy classifiers. The bivariate wrapped Cauchy distribution is the only bivariate circular distribution whose marginals and conditionals are also wrapped Cauchy distributions, a property that makes it possible to define these models easily. Furthermore, the wrapped Cauchy tree-augmented naive Bayes classifier requires the definition of a conditional circular mutual information measure between variables that follow wrapped Cauchy distributions. Synthetic data is used to illustrate, compare and evaluate the classification algorithms (including a comparison with the Gaussian TAN classifier, decision tree, random forest, multinomial logistic regression, support vector machine and simple neural network), leading to satisfactory predictive results. We also use a real neuromorphological dataset obtained from juvenile rat somatosensory cortex cells, where we measure the bifurcation angles of the dendritic basal arbors.

## 1. Introduction

Circular data is ubiquitous, present in many different areas such as biology, geology, medicine, oceanography, geophysics, meteorology, astronomy, ecology, neuroscience and geography. Some examples are directions of flight of homing pigeons [1], characterization of the phenology of species [2], formation of feldspar laths in basalt rocks [3], paleomagnetism in red slits and claystones $[4,5]$, also in political sciences studying the gun crimes occurred in an specific period of time [6], directional word vectors in text mining [7], wildfire orientation in order to prevent fire propagation [8], wind and waves direction analysis [9,10], study and prediction of protein dihedral angles structure [11,12], and neuronal basal dendritic bifurcation angles analysis [13,14] among many others. The natural periodicity of circular data sometimes makes traditional statistics methods ineffective, since they ignore this characteristic. For instance, when dealing with circular data, $0^{\circ}$ and $360^{\circ}$ are considered as the same point, whereas if considered non-circular data, they are different points. Thus, circular data analysis is distinct from and more challenging than non-circular data. It should be noted that circular data has been studied extensively $[3,15,16]$.

Probabilistic graphical models [17] are useful tools for data modeling that connect probability theory with graph theory. There are many advantages of using probabilistic graphical models, such as the fact that they are easily interpreted, they handle missing data effectively and they treat inference and learning tasks together. Bayesian networks [18] are one of the most commonly used probabilistic graphical models due to their factorization and domain representation properties. Bayesian networks have the

[^0]
[^0]:    b Corresponding author at: Departamento de Economía Financiera y Contabilidad e Idioma Moderno, Facultad de Ciencias Jurídicas y Sociales, Universidad Rey Juan Carlos de Madrid, Spain.

    E-mail addresses: ignacio.vitoriano@urjc.es (I. Leguey), mcbielza@fi.upm.es (C. Bielza), pedro.larranaga@fi.upm.es (P. Larrañaga).

characteristic that each variable is conditionally independent of those that are non-descendants in the graph given the value of their parents. Therefore the joint probability distribution is expressed as the product of the local distributions conditioned to their parents. For these reasons, Bayesian networks can deal efficiently with supervised classification i.e., the Bayesian network classifiers [13] and offer an explicit, graphical and interpretable representation of uncertain knowledge, which has made it possible to successfully apply them to real-world problems.

Supervised classification [19] deals with the problem of assigning a label to an instance, based on a set of variables that characterize it. Yet circular data has been commonly treated as linear data in supervised classification tasks. Only a few circular classifiers exist, and almost none of them are based on the principles of Bayesian networks, capable of capturing multivariate relationships among variables. Most of them focus on discriminant analysis and assume several circular distributions such as the von Mises distribution [20], later extended to the von Mises-Fisher distribution [21]. There are also circular discriminant analysis studies for the Watson, Selby and Arnold distributions on the sphere [22,23]. SenGupta and Roy [24] used a classification discriminant rule based on the mean chord-length to classify a new observation into one of two different circular populations that are von Mises, when training samples are available for each of them. Also a likelihood ratio test based on a bootstrapping approach for classifying into two populations was proposed for linear and circular data [25]. Kirby and Miranda [26] proposed a variation of a neural network, including a circular node, which was able to keep and send circular information. More recently, Fernandes and Cardoso [27] proposed a binary circular logistic regression as the discriminative counterpart to the naive Bayes model, which does not make assumptions on the input data distribution. López-Cruz et al. [28] is the only study in which Bayesian classifiers were used. For the von Mises and von Mises-Fisher distributions, López-Cruz et al. proposed an adaptation of the naive Bayes classifier and selective naive Bayes classifier, which are two of the simplest and best-known supervised classification models based on Bayesian network principles.

The lack of Bayesian supervised classifiers for circular data is due to the absence of circular Bayesian network models, which are very difficult to develop because of their circular multivariate distribution nature. A family of distributions is said to be closed under marginalization and conditioning when the marginals and conditionals of the multivariate distribution follow the same distribution. However, the marginals and conditionals of most circular distributions do not belong to the same family of distributions, making the modeling phase and posterior inference processes difficult.

The von Mises distribution [29], which is the analogue of the univariate Gaussian distribution, is the best-known circular model. A bivariate von Mises distribution also exists and was introduced by Mardia [30], who subsequently extended it to the multivariate case [31]. He showed that the conditional distributions are also von Mises distributions. Nevertheless, the marginal distributions are either unimodal or bimodal, and only the unimodal case could be approximated to a von Mises distribution when the concentration parameter is large. Therefore, as explained in [13] for discrete distributions, it would be much more complicated to achieve an efficient learning and inference. Therefore, we ruled out the use of von Mises distributions for our particular purpose. Another popular univariate symmetric circular distribution is the wrapped Cauchy, which was introduced by Lévy [32], and further studied by Wintner [33]. It was later obtained by mapping Cauchy distributions onto the circle [34]. Kato and Pewsey [35] developed a five-parameter bivariate wrapped Cauchy distribution for toroidal data, whose marginals and conditionals follow univariate wrapped Cauchy distributions. This family of bivariate wrapped Cauchy distributions is therefore closed under conditioning and marginalization. Leguey et al. [36] proposed a tree-structured Bayesian network model that deals with circular data which follows wrapped Cauchy distribution. However, this model only accounts for the discovery of conditional independence relationships of a set of random variables, without considering any as a class variable. This is a specificity of supervised classification problems that requires special learning algorithms.

Building on previous work regarding supervised classification using Bayesian networks for circular statistics, the novelty of this work lies in the proposal of four circular Bayesian classification models capable of dealing with supervised data following wrapped Cauchy distributions. The models to be presented are called wrapped Cauchy naive Bayes (wCNB), wrapped Cauchy selective naive Bayes (wCsNB), wrapped Cauchy semi-naive Bayes (wCamNB) and wrapped Cauchy tree-augmented naive Bayes (wCTAN) classifiers. Even though the simplest of our proposals (i.e., wCNB) is a straightforward naive Bayes classifier extension to using wrapped Cauchy distributions, this has never been attempted before to the best of our knowledge.

The remainder of this paper is organized as follows. Section 2 reviews the bivariate wrapped Cauchy distribution of Kato and Pewsey [35]. Section 3 describes the four novel wrapped Cauchy classifiers proposed here. In Section 4, we assess the four models in synthetic domains, requiring the design of a simulation method for these wrapped Cauchy Bayesian network classifiers. Section 5 addresses a real-world neuromorphology data problem using the wrapped Cauchy classifiers. Finally, Section 6 provides concluding remarks and proposals for future work.

# 2. Wrapped Cauchy distribution 

### 2.1. Definitions

A random variable $\Theta$ that follows a wrapped Cauchy distribution [32], denoted $w C(\mu, \varepsilon)$, has a density function

$$
f(\theta)=\frac{1}{2 \pi} \frac{1-\varepsilon^{2}}{1+\varepsilon^{2}-2 \varepsilon \cos (\theta-\mu)}, \quad \theta, \mu \in(-\pi, \pi], \varepsilon \in[0,1)
$$

where $\mu$ is the mean angle and $\varepsilon$ the concentration parameter. $f$ in Eq. (1) is unimodal and symmetric about $\mu$ unless $\varepsilon=0$, which yields the circular uniform distribution (i.e., $f(\theta)=1 / 2 \pi$ ).

A five-parameter bivariate wrapped Cauchy distribution was proposed by Kato and Pewsey [35]. A random vector $\left(\Theta_{1}, \Theta_{2}\right)$ follows a bivariate wrapped Cauchy distribution, denoted $b w C\left(\mu_{1}, \mu_{2}, \varepsilon_{1}, \varepsilon_{2}, \rho\right)$, if its density function is given by

$$
\begin{gathered}
f\left(\theta_{1}, \theta_{2}\right)=c\left[c_{0}-c_{1} \cos \left(\theta_{1}-\mu_{1}\right)-c_{2} \cos \left(\theta_{2}-\mu_{2}\right)-c_{3} \cos \left(\theta_{1}-\right.\right. \\
\left.\left.\mu_{1}\right) \cos \left(\theta_{2}-\mu_{2}\right)-c_{4} \sin \left(\theta_{1}-\mu_{1}\right) \sin \left(\theta_{2}-\mu_{2}\right)\right]^{-1}, \theta_{1}, \theta_{2} \in(-\pi, \pi]
\end{gathered}
$$

where $c, c_{0}, c_{1}, c_{2}, c_{3}$ and $c_{4}$ are

$$
\begin{aligned}
& c=\left(1-\rho^{2}\right)\left(1-\varepsilon_{1}^{2}\right)\left(1-\varepsilon_{2}^{2}\right) / 4 \pi^{2} \\
& c_{0}=\left(1+\rho^{2}\right)\left(1+\varepsilon_{1}^{2}\right)\left(1+\varepsilon_{2}^{2}\right)-8[\rho] \varepsilon_{1} \varepsilon_{2} \\
& c_{1}=2\left(1+\rho^{2}\right) \varepsilon_{1}\left(1+\varepsilon_{2}^{2}\right)-4[\rho]\left(1+\varepsilon_{1}^{2}\right) \varepsilon_{2} \\
& c_{2}=2\left(1+\rho^{2}\right)\left(1+\varepsilon_{1}^{2}\right) \varepsilon_{2}-4[\rho] \varepsilon_{1}\left(1+\varepsilon_{2}^{2}\right) \\
& c_{3}=-4\left(1+\rho^{2}\right) \varepsilon_{1} \varepsilon_{2}+2[\rho]\left(1+\varepsilon_{1}^{2}\right)\left(1+\varepsilon_{2}^{2}\right) \text { and } \\
& c_{4}=2 \rho\left(1-\varepsilon_{1}^{2}\right)\left(1-\varepsilon_{2}^{2}\right)
\end{aligned}
$$

with $\mu_{1}, \mu_{2} \in(-\pi, \pi], \varepsilon_{1}, \varepsilon_{2} \in[0,1)$ and $\rho \in(-1,1) . \varepsilon_{1}$ and $\varepsilon_{2}$ regulate the concentration of the marginal distributions, and $\rho$ is the parameter controlling the association between $\Theta_{1}$ and $\Theta_{2}$, from total independence $(\rho=0)$ to perfect correlation $(\rho= \pm 1)$. When $\varepsilon_{1}>0$ and $\varepsilon_{2}>0, f$ in Eq. (2) is unimodal and pointwise symmetric about $\left(\mu_{1}, \mu_{2}\right)$.

From McCullagh [34], we know that representing wrapped Cauchy models in complex form simplifies the computation in many cases. Let $Z=\exp (i \Theta)$, where $\Theta$ is distributed as in Eq. (1). Therefore the density function of $Z$ is

$$
f(z ; \lambda)=\frac{1}{2 \pi} \frac{\left|1-|\lambda|^{2}\right|}{|z-\lambda|^{2}}, \quad z \in \Omega, \lambda \in \hat{\mathbb{C}} \backslash \Omega
$$

where $\lambda=\varepsilon \exp (i \mu), \hat{\mathbb{C}}=\mathbb{C} \cup\{\infty\}$ and $\Omega=\{z \in \mathbb{C}:|z|=1\}$, with $|z|$ the module of the complex number. We use the notation $Z \sim C^{*}(\lambda)$ to denote that $Z$ is distributed as in Eq. (3).

Similarly, let $\left(Z_{1}, Z_{2}\right)=\left(\exp \left(i \Theta_{1}\right), \exp \left(i \Theta_{2}\right)\right)$, where $\left(\Theta_{1}, \Theta_{2}\right)$ is distributed as in Eq. (2). Therefore the density of $\left(Z_{1}, Z_{2}\right)$ is

$$
f\left(z_{1}, z_{2}\right)=\frac{\left(4 \pi^{2}\right)^{-1}\left(1-\rho^{2}\right)\left(1-\varepsilon_{1}^{2}\right)\left(1-\varepsilon_{2}^{2}\right)}{\left|a_{11}\left(\bar{z}_{1} \eta_{1}\right)^{q} z_{2} \bar{\eta}_{2}+a_{12}\left(\bar{z}_{1} \eta_{1}\right)^{q}+a_{21} z_{2} \bar{\eta}_{2}+a_{22}\right|^{2}}, z_{1}, z_{2} \in \Omega
$$

where $q$ is the sign of $\rho, \eta_{k}=\exp \left(i \mu_{k}\right)$ with $k \in\{1,2\}, \bar{z}_{k}$ is the complex conjugate of $z_{k}, a_{11}=\varepsilon_{1} \varepsilon_{2}-|\rho|, a_{12}=|\rho| \varepsilon_{2}-\varepsilon_{1}, a_{21}=|\rho| \varepsilon_{1}-\varepsilon_{2}$, $a_{22}=1-|\rho| \varepsilon_{1} \varepsilon_{2}, \varepsilon_{1}, \varepsilon_{2} \in[0,1), \rho \in(-1,1)$ and $\eta_{1}, \eta_{2} \in \Omega$.

Following the complex notation, we denote $\left(Z_{1}, Z_{2}\right) \sim b C^{*}\left(\eta_{1}, \eta_{2}, \varepsilon_{1}, \varepsilon_{2}, \rho\right)$ if $\left(Z_{1}, Z_{2}\right)$ is distributed as in Eq. (4). This five-parameter bivariate wrapped Cauchy complex form representation verifies the following result:

Theorem 1 (Kato and Pewsey [35]). A random vector $\left(Z_{1}, Z_{2}\right)$ with density given by Eq. (4) has marginals $Z_{1} \sim C^{*}\left(\varepsilon_{1} \eta_{1}\right)$ and $Z_{2} \sim C^{*}\left(\varepsilon_{2} \eta_{2}\right)$, and conditionals $Z_{1}\left[Z_{2}=z_{2} \sim C^{*}\left(-\eta_{2}\left[\boldsymbol{A} \circ\left(z_{2} \bar{\eta}_{2}\right)^{q}\right]\right)\right.$ and $\left.Z_{2} \mid Z_{1}=z_{1} \sim C^{*}\left(-\eta_{2}\left[\boldsymbol{A}^{T} \circ\left(z_{1} \bar{\eta}_{1}\right)^{q}\right]\right)$, where $\boldsymbol{A}$ is the matrix with elements $a_{11}, a_{12}, a_{21}$ and $a_{22}$ defined in Eq. (4), $\boldsymbol{A}^{T}$ is the transpose of $\boldsymbol{A}$, and

$$
\boldsymbol{A} \circ z=\frac{a_{11} z+a_{12}}{a_{21} z+a_{22}}
$$

As far as we know, there is no other bivariate circular distribution for which conditional and marginal distributions belong to the same family. Therefore, wrapped Cauchy is the best choice given no better alternative, as the requirements for the classifier structures that we will develop are of at most a tree-structure (i.e., only bivariate, marginal and conditional densities are required). Furthermore, we require the definition of a conditional circular mutual information measure between variables that follow wrapped Cauchy distributions.

# 2.2. Parameter estimation 

Working with the density given by Eq. (2), numerical methods have to be used to find the parameter estimates, since there is no closed-form expression for the maximum likelihood estimates. Kato and Pewsey [35] demonstrated that the method of moments [37] is more efficient; it is computationally very fast, easy to implement and with closed form formulas for the parameter estimates.

Let $\left\{\left(\theta_{1 j}, \theta_{2 j}\right), j=1, \ldots, N\right\}$ be a random sample from a $b w C\left(\mu_{1}, \mu_{2}, \varepsilon_{1}, \varepsilon_{2}, \rho\right)$ as stated in Eq. (2). Therefore the estimators obtained from the method of moments for $\mu_{1}, \mu_{2}, \varepsilon_{1}, \varepsilon_{2}$ and $\rho$ are [35]

$$
\begin{gathered}
\hat{\mu}_{r}=\arg \left(\hat{R}_{r}\right), \quad \hat{\varepsilon}_{r}=\left|\hat{R}_{r}\right|, \quad \text { with } \quad \bar{R}_{r}=\frac{1}{N} \sum_{i=1}^{N} \exp \left(i \theta_{r j}\right) \\
\hat{\rho}=\frac{1}{N}\left(\left|\sum_{j=1}^{N} \exp \left(i\left(\Phi_{1 j}-\Phi_{2 j}\right)\right)\right|-\left|\sum_{j=1}^{N} \exp \left(i\left(\Phi_{1 j}+\Phi_{2 j}\right)\right)\right| \\
\text { with } \quad \Phi_{r j}=2 \arctan \left(\frac{1+\hat{\varepsilon}_{r}}{1-\hat{\varepsilon}_{r}} \tan \left(\frac{\theta_{r j}-\hat{\mu}_{r}}{2}\right)\right) \quad \text { and } \quad r=1,2
\end{gathered}
$$

![img-0.jpeg](img-0.jpeg)

**Fig. 1.** wCNB structure with five circular predictor nodes, from which *p(c|θ) ∝ p(c)f_{Θ_{1}|c}(θ_{1}|c)f_{Θ_{2}|c}(θ_{2}|c)f_{Θ_{3}|c}(θ_{3}|c)f_{Θ_{4}|c}(θ_{4}|c)f_{Θ_{5}|c}(θ_{5}|c))*.

### 3. Wrapped Cauchy classifiers

Let Θ = (Θ_{1}, ..., Θ_{n}) be a vector of circular predictor random variables or features, and let *C* be a discrete class variable which takes values (labels) in the set *A*(*C*). Given a sample of *N* labeled instances (Θ^{1}, *C*^{1}), ..., (Θ^{N}, *C*^{N}), the supervised classification problem consists of developing a model capable of assigning a class label to a new object based on the values of its features.

Bayesian network classifiers [13] have been used to solve classification problems with linear data, because of their easy representation of the problem domain and the efficient computation of the algorithms associated with Bayesian network techniques. Our novel purpose is to develop the circular domain counterpart of four well-known Bayesian network classifiers (naive Bayes, selective naive Bayes, semi-naive Bayes and tree-augmented naive Bayes) when the underlying variables follow wrapped Cauchy distributions.

#### 3.1. Wrapped Cauchy naive Bayes

The wrapped Cauchy naive Bayes (wCNB) classifier is the simplest of the four Bayesian network classifier models that we present in this paper, where *C* is the parent of all circular features and these are assumed to be conditionally independent among them given *C* (Fig. 1)

$$p(C = c|\Theta = \theta) \propto p(C = c) \prod_{i=1}^{n} f_{\Theta_i}{|C_{m,i}} (θ_i | c). \tag{6}$$

The wCNB determines the class value *c** for a new instance using a maximum a posteriori decision rule

$$c^* = \arg \max_{c \in A(C)} p(C = c|\Theta = \theta).$$

Since each predictor variable *Θ_{i}* given *C* = *c* follows a wrapped Cauchy distribution with location parameter *µ_{i,c}* and concentration parameter *ε_{i,c}*, we can express Eq. (6) as

$$p(c|\theta) \propto = \frac{p(C = c) \prod_{i=1}^{n} \alpha_{i,c}}{\prod_{i=1}^{n} (1 - \beta_{i,c})}, \tag{7}$$

where *α_{i,c}* = 1/2*π* (1+ε_{i,c}^{2})/2 (1+ε_{i,c}^{2}) and *β_{i,c}* = 2/2*ε_{i,c} sin(θ_{i}-µ_{i,c})/2 (1+ε_{i,c}^{2}).

#### 3.2. Wrapped Cauchy selective naive Bayes

Sometimes there are several predictor variables that do not contribute to classification (i.e., they are redundant), and naive Bayes classifier is affected by such variables [38]. Determining which of them are unnecessary via the use of feature subset selection (FSS) techniques [39] could increase the accuracy of the classification model significantly [40]. Wrapped Cauchy selective naive Bayes (wCsNB) is a classification model with a structure similar to that of wCNB, but not all the variables are necessarily used by the classifier. FSS techniques were previously employed in a circular classification model with von Mises and von Mises–Fisher distributions in [28], where a filter-wrapper algorithm is applied to rank the variables according to the mutual information between them and the class, and therefore, using the ranking provided by the filter step, the variables are selected to induce a new classifier until the best model is achieved.

We also use a filter-wrapper algorithm at this point. The filter step is based on the computation of the mutual information (MI) between each circular variable and the class. There is no equation to compute the MI between circular variables and discrete variables. Therefore, we approach the problem using Monte Carlo methods, as in [28]; we model the conditional density functions of *Θ_{i}*|*C* = *c* as wrapped Cauchy distributions. Hence

$$\text{MI}(\Theta_i, C) \approx \frac{1}{M} \sum_{j=1}^{M} \log \frac{\hat{f}_{\Theta_i}{|c^{*(j)}} \left(\theta_i^{*(j)} \right) \hat{p} \left(C = c^{*(j)}\right)}{\hat{f}_{\Theta_i} \left(\theta_i^{*(j)} \right) \hat{p} \left(C = c^{*(j)}\right)}, \tag{8}$$

![img-1.jpeg](img-1.jpeg)

**Fig. 2.** wCsNB structure with three nodes selected from the original set of five predictive variables, from which *p(c|θ) ∝ p(c)f_{θ_{1}|c}*θ_{1} |c*)*f_{θ_{2}|c}*θ_{2} |c*)*f_{θ_{3}|c}*θ_{3} |c*).*

where *M* is the number of instances (*θ_{i}^{x(j)}, c^{x(j)})* sampled from *f_{θ_{j}|c}*θ_{i} |c) *β* (*C = c*), with *f_{θ_{j}|c}*θ_{i} |c) the fitted wrapped Cauchy density function of the conditional density function of *θ_{i}* given *C = c*, and *β* (*C = c*) the relative frequency of instances that belong to class *c* in the training set.

The predictive variables are then ranked according to their MI values.

The wrapper step consists of creating a new classifier by deciding whether or not to include the ranked predictive variables from the filter step. Each iteration of the wrapper step induces a new classifier adding the next predictive variable from the list. If no accuracy improvement is achieved by including the next predictive variable from the ranked list, then the wrapper step finishes. This model is similar to the WcNB, but including only the selected wrapped Cauchy variables (set *S*) (Fig. 2) and therefore

$$p(c|\theta) \propto p(c|\theta_S) = p(C = c) \prod_{i \in S} f_{\theta_1|C=c}\left(\theta_i \right) c.$$

As for the wCNB, the wCsNB determines the class value *c** for a new instance using a maximum a posteriori decision rule

$$c^* = \arg \max_{c \in A(C)} p(C = c | \Theta_S = \theta_S).$$

Likewise for Eq. (7), we can express Eq. (9) as

$$p(c|\theta_S) = \frac{p(C = c) \prod_{i \in S} \alpha_{i,c}}{\prod_{i \in S} (1 - \beta_{i,c})},$$

where *α_{i,c} = 1/2π (1/2π) (1/2π) and β_{i,c} = 2π_{i,c} (2πi/π_{i,c} - π_{i,c}) (1/2π_{i,c})*.

### 3.3. Wrapped Cauchy semi-naive Bayes

Usually, the assumption of conditional independence between predictive variables given the class variable is dismissed. The semi-naive Bayes classification model [41] goes one step further and considers dependencies between predictive variables.

Our proposal for this model, called wrapped Cauchy semi-naive Bayes (wCsmNB) classifier, takes into account the possible dependence between predictive wrapped Cauchy variables by introducing new features obtained as the Cartesian product of two of the original circular predictor variables. Thus we work with a bivariate wrapped Cauchy distribution. These new features remain conditionally independent given the class variable.

Given *L_{k}* with *k = 1, ..., T*, representing the *k*th feature (original or new features)

$$p(c|\theta) \propto p(C = c) \prod_{k=1}^{T} f_{\theta_{L_k}|C=c}\left(\theta_{L_k} \right) c.$$

To determine those original variables that are candidates to create new features from the Cartesian product between them, we develop an adaptation of the *forward sequential selection and joining* (FSSJ) algorithm [42] described in Algorithm 1. It is important to note that once the new features are created by joining two original features, these new features cannot be used to create others. However, these new features can be separated in order to use one of the two original features to create another new feature by joining with a different original feature that had not yet been added to the model. This algorithm may result in a selection of variables that provide the best achievable solution, before all of the original variables are included in the model (Fig. 3).

Again, as for the previous models presented in this section, the wCmNB determines the class value *c** for a new instance using a maximum a posteriori decision rule

$$c^* = \arg \max_{c \in A(C)} p(C = c | \Theta = \theta_{L_k}).$$

Algorithm 1 Adaptation of the FSSJ algorithm of [42]

1: Let *T* be the variable list, initialized as *T* = ∅.
2: Given Θ₁, Θ₂, ..., Θₙ circular wrapped Cauchy predictor variables from a variable list *A*, move the first variable from *A* to *T*.
3: Move the next variable from *A* to *T*, considering:
   - Joining the variable to another variable currently in *T*. If the latter variable was previously joined to another variable from *T*, remove this from *T* and add it to *A*, and consider adding it later.
   - Add the variable as conditionally independent of the other variables given *C* to the current classifier.
4: Repeat Step 3 until the best model is achieved

![img-2.jpeg](img-2.jpeg)

**Fig. 3.** wCsmNB structure with four nodes from the original set of five predictive variables, from which *p(c|θ) ∝ p(c)f*Θ₁,Θ₂|c) (θ₁, θ₂|c) *f*Θ₁, |c) (θ₁|c) *f*Θ₂|c) (θ₃|c).

### 3.4. Wrapped Cauchy tree-augmented naive Bayes

The tree-augmented naive Bayes (TAN) classifier [43] is a well-known Bayesian classifier with a tree-structure network for predictive features. Wrapped Cauchy tree-augmented naive Bayes (wCTAN) classifier is a variation of the TAN classifier with the novelty of the allowance of the use of wrapped Cauchy circular variables for predictive features. wCTAN assumes that the class variable has no parents, and the rest of the variables have at most one other variable as parent apart from *C* (Fig. 4).

The process for building a wCTAN is summarized in the following three steps:

- **Step 1:** The structure of the tree for predictive features is learned using Algorithm 2. We use the conditional circular mutual information, denoted as CMI(Θ₁, Θₙ|C), which is defined as

  CMI(Θ₁, Θₙ|C) = ∑_{c} CMI(Θ₁, Θₙ|C = c)p(C = c),

  with

  CMI(Θ₁, Θₙ|C = c) = ∫_{-πππ}∫_{-πππ}πf(θ₁, θⱼ|c) log (f(θ₁, θⱼ|c)/f(θⱼ|c)) dθᵢdθⱼ.

  Where the marginal density functions given the class, *f*(θᵢ|c) and *f*(θⱼ|c), and the joint density function given the class, *f*(θⱼ, θⱼ|c), have been previously estimated from data. This structure learning algorithm (Algorithm 2) is based on score and search, where structure learning is posed as an optimization problem, using a maximum weighted spanning tree algorithm (where the weights are given by the CMI), a variant of the Chow Liu algorithm [44].

### Algorithm 2 Adaptation of the Chow Liu algorithm of [44]

1: Given Θ₁, Θ₂, ..., Θₙ wrapped Cauchy variables, estimate the bivariate joint density function *f*(θⱼ, θⱼ|c) for all pairs of variables, and the marginals *f*(θᵢ|c), for each *c* ∈ *A*(*C*), *i*, *j* = 1, ..., *n*
2: Using these, compute all conditional CMI(Θ₁, Θⱼ|C) values, (i.e., the *n*(*n* − 1)/2 edge weights) and order them
3: Assign the largest two edges to the undirected tree to be represented
4: Examine the next-largest edge, and add it to the tree unless it forms a loop, in which case discard it and examine the next largest edge
5: Repeat Step 4 until *n* − 1 edges have been selected (and the spanning undirected tree is finished)

For Step 1 in Algorithm 2, the estimate of the bivariate and marginal densities are performed for each *c* using the methods explained in Section 2. Like the traditional mutual information measure for linear variables, the CMI(Θ₁, Θⱼ|C) denotes the entropy reduction of Θᵢ (Θⱼ) when the value of Θⱼ (Θⱼ) is known given *C*, and represents the weight that links Θᵢ and Θⱼ.

![img-3.jpeg](img-3.jpeg)

**Fig. 4.** wCTAN structure with five nodes, from which *p*(*c*|*θ*) ∝ *p*(*c*)*f*<sub>*θ*<sub>1</sub>*|*c*, *θ*<sub>2</sub>*|*θ*<sub>1</sub>*|*c*, *θ*<sub>2</sub>*}/*f*<sub>*θ*<sub>1</sub>*|*c*, *θ*<sub>1</sub>*|θ*<sub>2</sub>*|*c*, *θ*<sub>3</sub>*}/*f*<sub>*θ*<sub>1</sub>*|*c*, *θ*<sub>2</sub>*|*θ*<sub>3</sub>*|*c*, *θ*<sub>4</sub>*|*f*<sub>*θ*<sub>1</sub>*|*c*</sub>*θ*<sub>2</sub>*|*θ*<sub>3</sub>*|*c*, *θ*<sub>4</sub>*|*). The associated tree-structured Bayesian network has *Θ*<sub>*A*</sub> as its root node.

Once we have learned the undirected structure, a root node must be selected in order to determine the root of the tree by following the structure learned by Algorithm 2. Depending on the selected root node and given the undirected tree structure with *n* nodes, there are *n* possible resulting directed trees.

- **Step 2:** We add a class node *C* to the network structure. We connect this class node to every other node with an arc from *C* (Fig. 4).
- **Step 3:** Finally, we complete the classification model with the estimation of the parameters for each node given its parent node(s).

Therefore the conditional probability of *C* given the predictors is

$$p(C = c \mid \Theta = \theta) \propto p(C = c)f_{\Theta_{root} \mid C = c}(\theta_{root} \mid c) \prod_{i = 1, \text{rarest}}^{n} f_{\Theta_i \mid C = c, P_{a_{\Theta_i}}}(\theta_i \mid c, pa_{\theta_i}),$$

where *Pa*<sub>*θ*<sub>*i*</sub></sub> is the wrapped Cauchy parent of variable *Θ*<sub>*i*</sub> and *Θ*<sub>*root*</sub> is the root node of the tree.

Similar to the approach used in the rest of the models presented in this paper, the maximum a posteriori decision rule is used to determine the predicted class *c**<sup>**</sup>*

$$c^* = \arg \max_{c \in A(C)} p(C = c \mid \Theta = \theta).$$

### 4. Experimental results

In this section, we report experiments carried out to show the behavior of each proposed classification model in Section 3. We include the comparison among the four circular classifiers and also with some of the best-known classification algorithms for linear data, such as decision tree (DTree), random forest (Rfor), multinomial logistic regression (MLG), support vector machine (SVM), simple neural network (Nnet) and the Gaussian tree-augmented naive Bayes classifier (GTAN) for continuous data, with the structure learned with the algorithm in [45] where predictor variables given the class value are assumed to follow Gaussian distributions.

The experiments were run using R software [46]. To generate the artificial datasets to test the models, we used the "Circular" R package for the simulation of circular data, and to implement the structure of the wCTAN classifier, we have adapted the "bnclassify" R package [47]. Simulating data that follows wrapped Cauchy distributions is easy and computationally very fast. Given the parameters, the "Circular" R package simulates wrapped Cauchy data by wrapping the simulation of a Cauchy distribution whose location parameter is the same as the wrapped Cauchy location parameter and the scale parameter is the negative logarithm of the wrapped Cauchy concentration parameter. If the wrapped Cauchy concentration parameter is equal to 1, then the value of the simulation will be the location parameter, whereas if the concentration parameter is equal to 0, the simulation is performed from a Uniform distribution in [0, 2*π*).

In order to test the algorithms, we enforced dependence between nodes giving values of |*ρ*| in [0.5, 1). The remaining parameters were assigned randomly to each node with −*π* < *μ* < *π* and 0 < *ε* < 1. For each classifier, we simulated 10 datasets each with 1000, 200 and 50 instances and 3, 5, 10, 20, 30, 45, 65, and 100 wrapped Cauchy predictor variables and a discrete class variable with 3, 6, 10, 15 and 20 different labels, so we simulated 1200 different datasets for each type of classifier. A 10-fold cross-validation was used to estimate the classification accuracy. Results for Bayesian network classifiers are shown in Table 1, while results for traditional linear classification algorithms are shown in Table 2.

We also applied the non-parametric Friedman test to detect statistically significant differences among our classification models as a whole set [48]. When the null hypothesis was rejected, we proceeded with post-hoc tests. We chose the Nemenyi test [49], as suggested by [50]. The significance level *α* for all tests was 0.05.

Since multiple classifiers are compared, it is useful to represent the results of the post-hoc tests visually. The graph proposed by Demšar [50] is a simple diagram to easily represent these results. The top line is the axis on which we plot the average Friedman test ranks of the classifiers. The lowest (best) ranks are to the right, and we therefore consider the classifiers to the right as better. For the comparison results of all classifiers against each other, those that are not significantly different (*p*-value ≥ 0.05 in the Nemenyi post-hoc test) are connected.

Table 1 Mean ± standard deviation accuracy of wCNB, wCsNB, wCmNB, wCTAN and GTAN for different number of variables, different number of labels in the class variable for simulated datasets with 50, 200 and 1000 instances.


Table 2 Mean ± standard deviation accuracy of DTre, Rfor, MLG, SVM and Nnet for different number of variables, different number of labels in the class variable for simulated datasets with 50, 200 and 1000 instances.



Table 3
Mean $\pm$ standard deviation accuracy of wCNB, wCsNB, wCsmNB, wCTAN, GTAN, DTree, Rfor, MLG, SVM and Nnet classifiers for different number of variables. Results are averaged from the classification performance from Tables 1 and 2 with $3,6,10$, 15 and 20 different labels with 1000 instances. Bolded results are best performing classifiers.


# 4.1. Comparison of classification models 

In this section, we compare the performance of the wCNB, wCsNB, wCsmNB and wCTAN models, as well as the DTree, Rfor, MLG, SVM, Nnet and the GTAN algorithms, which ignores the circular nature of the data. We analyze the results of the simulation with 1000 instances. Additionally, we analyze the Bayesian network classifiers performance for 50 and 200 instances.

Table 3 shows the mean $\pm$ standard deviation accuracy for each classifier for different number of variables. Each mean $\pm$ standard deviation accuracy values was obtained from the results of 50 independent 10 -fold cross-validation procedures varying the number of labels of the class variable ( $3,6,10,15$ and 20 different labels) with 1000 instances.

The statistical analysis after Friedman test rejection ( $p$-value $=0.000000005$ ) reveals (Fig. 5A) that, varying the number of variables, the best classifiers are wCsmNB, wCTAN, wCNB, Rfor and wCsNB with no statistically significant differences among them , whereas the DTree, GTAN, Nnet and MLG classifiers are the worst, presenting significant differences with respect to the rest of the classifiers but for the SVM (which does not present statistical differences with the Nnet and MLG)and demonstrating that treating circular data as linear-continuous is not effective. The SVM also presents statistical differences when compared with the wCsmNB, wCTAN and wCNB classifiers, which outperforms the SVM results. Nevertheless, there were no significant differences between the SVM and the remaining circular classifier (i.e., wCsNB) and the Rfor classifier.

Performing the same statistical analysis among Bayesian network classifiers with 50 and 200 instances yields similar results. The Friedman test null hypothesis that there is no significant difference is rejected for both ( $p$-value $=0.00021$ and $p$-value $=0.00004$, respectively). The post-hoc analysis displays quite similar results to the 1000 instances one; in both cases, there are no statistically significant differences among the wCsmNB, wCTAN and wCNB classifiers, which are the best. Nevertheless, for 50 and 200 instances, there are no significant differences among GTAN and wCsNB classifiers. Furthermore, there are significant differences between the wCsNB and the wCsmNB classifier for the analysis with 50 instances, whereas for 200 instances, statistical differences were seen between the wCsNB classifier and both the wCsmNB and the wCTAN.

We also calculated the mean accuracy for each classifier for different number of labels in the class variable (see Table 4). Each mean accuracy value was obtained from the results of 60 independent 10 -fold cross-validation procedures varying the number of variables to be used: $3,5,10,20,30$ and 45 with 1000 instances. We do not include the results of the experiments with more than 45 variables due to the high mean accuracy values obtained in most of the classifiers from Tables 1 and 2, which would bias the results.

Since the Friedman test null hypothesis that there is no significant difference was rejected ( $p$-value $=0.0000011$ ), we performed the corresponding Nemenyi post-hoc analysis. Statistical test results (Fig. 5B) reveal that based on changing the number of labels, the best classifiers are the circular Bayesian network classifiers (i.e., wCsmNB, wCTAN, wCNB and wCsNB), with no statistically significant differences between them. Again, DTree GTAN, Nnet and MLG are the worst, with no significant differences among them. These classifiers shows significant differences with wCsmNB, wCTAN, wCNB, Rfor and wCsNB, whereas SVM only presents significant differences with the wCsmNB, wCTAN, wCNB, DTree and GTAN classifiers.

The analysis for Bayesian network classifiers with 50 and 200 instances again yielded quite similar results to those obtained for 1000 instances. After Friedman test rejections ( $p$-value $=0.0325$ for 50 instances, and $p$-value $=0.00066$ for 200 instances), post-hoc tests for 200 instances reveal the same statistically significant differences as for 1000 instances, where there is no statistical differences among the wCsmNB, wCTAN and wCNB classifiers, which are the best. For 50 instances, wCsmNB, wCTAN and wCNB are also the best classifiers together with the wCsNB, with no statistically significant differences among them. Likewise, for 1000 instances, GTAN is the worst for the analysis with 50 instances as well as the 200 instances, with no significant differences with the wCsNB classifier.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Demlar diagrams presenting the statistical comparison among wCNB, wCsNB, wCsmNB, wCTAN, GTAN, DTree, Rfor, MLG, SVM and Nnet classification models for synthetic datasets with 1000 instances. Those classifiers that are not connected show differences that are statistically significant (p-value < 0.05). The lowest rank classifiers are to the right side of the graph (i.e., they can be considered the best). (A) Comparison varying the number of labels. (B) Comparison varying the number of variables.

Table 4


Table 4

Mean ± standard deviation accuracy of wCNB, wCsNB, wCsmNB, wCTAN, GTAN, DTree, Rfor, MLG, SVM and Nnet classifiers for different number of labels. Results are averaged from the classification performance with 3, 5, 10, 20, 30 and 45 different variables with 1000 instances. Bolded results are best performing classifiers.

## 5. Real data example

We applied our classifiers to a dataset of 3027 combinations of dendritic bifurcation angles coming from the basal arbors of 288 3D pyramidal neurons in layers *II, III, IV, Va, Vb* and *VI* (48 neurons per layer) of the 14-day-old (P14) rat hind limb somatosensory (S1HL) neocortex, recently published in [14] (Fig. 6).

We used the Bayesian network classification models presented in Section 3 and wrapped Cauchy distributions to model the bifurcation angles produced by the splitting of the dendritic segments of basal dendritic trees. The dendritic bifurcation angles are an important part of the geometry of pyramidal cell arbors. Since it is thought that these angles determine the space to be filled by the dendritic wiring, understanding and modeling them are crucial for advances in neuroscience to replicate brain functioning and structure in order to make further on how the brain processes information. This is important not only to understand it biologically (i.e., thoughts, emotions, feelings) but also technological, making essential contributions to new computing. Moreover, brain knowledge is basic for treating brain diseases such as Parkinson or Alzheimer.

Predicting which layer a neuron belongs to is an important task to help understand any neural circuit, and it represents part of the picture regarding the identification and characterization of all its components. To the best of our knowledge, there is no any supervised classification model that predicts the layer using circular predictive variables. Thus, we developed a classification model to predict which layer a given neuron belongs to, i.e., *A*(*C*) = (*I**I*, *I**I**I*, *I**V*, *V**a*, *V**b*, *V**I*).

Following the notation used in [14], Θ_{1} will correspond to the first bifurcation angle (Order 1) generated for the first split of the dendritic segments starting from the soma. The second angle generated by the next consecutive splits will be represented as variable Θ_{2} (Order 2), etc. (Fig. 7). Angles of orders higher than six which were relatively scarce were not included in the model. For each set of angles of the same order, a wrapped Cauchy distribution was fitted (Table 5). We performed a goodness-of-fit test by transformation on the circle of the variables into circular uniform variables via 2*π**F*(Θ_{1}), ..., 2*π**F*(Θ_{6}), where *F* is the cumulative distribution function, and applied Kuiper's test [51] for circular uniformity with a significance level of α = 0.05.

Note that in Table 5 the circular mean tends to decrease as the order increases. A neuroscientific explanation for this behavior relates to the fact that it is the first bifurcation orders that determine the volume of space to be filled by the dendritic trees [14]. This

![img-5.jpeg](img-5.jpeg)

**Fig. 6.** (A) Low-power photomicrograph showing injected neurons in layers III from the S1HL region of P14 rats, as seen in the plane of section parallel to the cortical surface. (B) Higher magnification photomicrograph showing an example of a pyramidal cell basal dendritic arbor. Scale bar (in B) = 200 µm in A; 90 µm in B. *Source:* Adapted from [14].

![img-6.jpeg](img-6.jpeg)

**Fig. 7.** Angles of different branch orders (from 1 to 6) measured between sibling segments in a dendritic arbor. The dendritic arbor has a maximum branching order of (A) 2 (B) 3 (C) 4 (D) 5 (E) 6.


**Table 5.** Characteristics of the six different branching orders shown in Fig. 7.


regulates the dendritic branching development rules that seem to determine the synaptic connectivity of pyramidal neurons. We also observe that the concentration values are high (around 0.91) and quite similar in every bifurcation order. This fact demonstrates that the dendritic structure (in terms of bifurcation angles) is determined by the location parameter.

Since not all dendritic arbors present angles of all orders, one classifier for the whole dataset is not suitable. Therefore, for each classification model proposed in this paper, we created a battery of five classifiers depending on the maximum bifurcation order of the arbor, when this is higher than 1 (Fig. 8). Before predicting class c+, we have to check the maximum bifurcation order of the instance to be classified. For the wCTAN and GTAN structures (which require a root node in addition to the class node) we select as root node Θ2 for every classifier of the battery. We performed 10 fold cross-validation procedures in order to obtain the mean classification accuracy values for each classifier and maximum bifurcation order (Table 6).

We observe in Table 6 that the wCsNB classifier leads to the best results for arbors with a maximum branching order of Θ2 and Θ3. Furthermore, for arbors with a maximum branching order of Θ4, Θ5 or Θ6, the wCsmNB seems to perform best in terms of classification accuracy. The wCTAN and wCNB classifiers also report acceptable values in comparison with the highest ones for each maximum bifurcation arbor, although the wCsNB or wCsmNB classification models always perform better for this neuronal dataset. Comparing the accuracy results with the random label assignation (i.e., 1/6 = 0.16), we observe that all of these results are over 0.16. In addition, for every case, the GTAN classifier exhibits the lowest accuracy values, below 0.16 except for Θ4. This classifier was especially inaccurate for arbors that had maximum branching order of 6; the mean accuracy value was 0.047 for such cases.

![img-7.jpeg](img-7.jpeg)

**Fig. 8.** Bayesian network classifier structures associated with the battery of classifiers depending on the maximum bifurcation order, for each type of classification algorithm: (A) wCNB, (B) wCsNB, (C) wCsmNB, (D) wCTAN, (E) GTAN.

![img-8.jpeg](img-8.jpeg)

**Fig. 9.** Demšar diagram for the comparison of wCNB, wCsNB, wCsmNB, wCTAN and GTAN classification models using Friedman test and Nemenyi post-hoc test.

**Table 6**

Mean ± standard deviation of layers *II*, *III*, *IV*, *Va*, *Vb* and *VI* classification accuracy results of the battery of classifiers for each type of classifier applied over the dataset of dendritic bifurcation angles coming from the basal arbors of 288 3D pyramidal neurons of P14 rat S1HL neocortex. Bolded results are best performing classifiers.


We applied the Friedman non-parametric test to detect statistically significant differences in the results provided by our algorithms. Since the null hypothesis that there is no significant difference was rejected (*p*-value = 0.004), we used Nemenyi post-hoc test to determine which pairwise of algorithms was the cause of the Friedman test rejection. In Fig. 9, the statistically significant differences between our classifiers are represented as a Demšar diagram. We noted that there are no statistically significant differences between our classification algorithms except for two cases; between the wCTAN and wCsNB and between GTAN and the wCsmNB.

Therefore, we can conclude that (i) apart from the difficulty identifying the layer a case belongs to, it seems reasonable to use any of our four proposed circular classifiers for this neuronal dataset, since there are no any statistically significant differences between them and (ii) GTAN is never recommended.

# 6. Conclusions and future work 

Introducing the first set of supervised Bayesian classification models capable of dealing with circular wrapped Cauchy predictive variables was the main objective of this paper. We have presented four models and their algorithms, designed to perform classification. We demonstrated using synthetic data that these models could perform classification accurately given circular datasets. We also provided evidence of the improvement of the circular classifiers over linear classifiers for datasets of circular nature that follow wrapped Cauchy distributions.

We performed statistical comparisons among the classifiers using synthetic data with 50, 200 and 1000 instances. Based on the results, we realized that the wCsmNB, the wCTAN and the wCNB are the best classification models for circular data that follows wrapped Cauchy distributions, with no statistically significant differences among them. The linear classifier never outperformed any of the wrapped Cauchy classifiers

For each of our new proposals, we evaluated a battery of classifiers using a real-world neuroscience dataset, in order to predict the layer that an instance belongs to. Results revealed that all of our four classification models are suitable. Performing Friedman test and its corresponding Nemenyi post-hoc test after rejection, we realized that there are no any statistically significant differences between wCNB, wCsNB, wCsmNB and wCTAN for this dataset. Wrapped Cauchy classifiers always outperformed their linear (Gaussian) counterparts.

The models shown in this paper are limited to no more than bivariate relationships. In future work, we intend to develop multivariate models in order to extend the Bayesian network classifiers for circular data to other more-sophisticated Bayesian network models (like k-dependence Bayesian network classifiers) capable of representing and taking into account multivariate relationships between circular variables - a difficult task due to the non-closed nature of the circular families that are known to date.

## Acknowledgments

This work has been partially supported by the Spanish Ministry of Economy and Competitiveness through the TIN2016-796842-P and Cajal Blue Brain (C080020-09) projects. This project has received funding from the European Union's Horizon 2020 Framework Programme for Research and Innovation under Specific Grant Agreement No. 785907 (HBP SGA2). I.L. is supported by the Spanish Ministry of Education, Culture and Sport Fellowship (FPU13/01941). The authors thankfully acknowledge the Cortical Circuits Laboratory (CSIC-UPM) for providing the neuron dataset.
