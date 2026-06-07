# AUTOMATIC CLASSIFICATION OF VARIABLE STARS IN CATALOGS WITH MISSING DATA 

Karim Pichara ${ }^{1,3,4}$, Pavlos Protopapas ${ }^{2,3}$<br>${ }^{1}$ Computer Science Department, Pontificia Universidad Católica de Chile, Santiago, Chile<br>${ }^{2}$ Harvard-Smithsonian Center for Astrophysics, Cambridge, MA, USA<br>${ }^{3}$ Institute for Applied Computational Science, Harvard University, Cambridge, MA, USA and<br>${ }^{4}$ The Milky Way Millennium Nucleus, Av. Vicuña Mackenna 4860, 782-0436 Macul, Santiago, Chile<br>Draft version October 30, 2013


#### Abstract

We present an automatic classification method for astronomical catalogs with missing data. We use Bayesian networks, a probabilistic graphical model, that allows us to perform inference to predict missing values given observed data and dependency relationships between variables. To learn a Bayesian network from incomplete data, we use an iterative algorithm that utilises sampling methods and expectation maximization to estimate the distributions and probabilistic dependencies of variables from data with missing values. To test our model we use three catalogs with missing data (SAGE, 2MASS and UBVI) and one complete catalog (MACHO). We examine how classification accuracy changes when information from missing data catalogs is included, how our method compares to traditional missing data approaches and at what computational cost. Integrating these catalogs with missing data we find that classification of variable objects improves by few percent and by $15 \%$ for quasar detection while keeping the computational cost the same.


Subject headings: -

## 1. INTRODUCTION

Classifying objects based on their features (e.g.: color, magnitude or any statistical descriptor) dates back in the 19th century (Rosenberg 1910). Recently automatic classification methods have become much more sophisticated and necessary due to the exponential growth of astronomical data. In time-domain astronomy, where data is in the form of light-curves, a typical classification method uses features ${ }^{1}$ of the light-curves and applies sophisticated machine learning to classify objects in a multidimensional features space, provided there are enough examples to learn from (training). After almost a decade since the first appearance of automatic classification methods, many of those methods have produced and continue to produce high fidelity catalogs (Kim et al. 2011, 2012; Bloom \& Richards 2011; Richards et al. 2011; Bloom \& Richards 2011; Debosscher et al. 2007; Wachman et al. 2009; Wang et al. 2010).

To take full advantage of all information available, is best to use as many available catalogs as possible. For example, adding u-band or x-ray information while classifying quasars based on their variability is highly likely to improve the overall performance (Kim et al. 2011; Pichara et al. 2012; Kim et al. 2012). Because these catalogs are taken with different instruments, bandwidths, locations, times, etc, the intersection of these catalogs is smaller than any single catalog; thus the resulting multicatalog contains missing values. Traditional classification methods can not deal with the resulting missing data problem because to train a classification model it is necessary to have all features for all training members. This can be solved by either selecting the complete intersection of the training members from all catalogs or by deleting the subset of features that are not common to

[^0]![img-0.jpeg](img-0.jpeg)

Fig. 1.- The joint distribution is shown as contours, the marginal distributions are shown in dashed line and conditional distributions in solid lines. Ignoring the joint distribution, one draws from the marginal distribution. However knowledge of the joint distribution allows us to draw from the conditional distribution.
all member. Unfortunately, both methods dramatically reduce the size of the training set because in general most of the features present missing values.

Alternatively, one can fill missing data using Monte Carlo approaches where each missing value is drawn from a distribution that is determined from all objects in the training set. However, this approach totally ignores the relationship amongst the features. Fig. 1 demonstrates the drawbacks of ignoring such a relationships. If one draws from the marginal distributions of $x$ and $y$ (shown with solid blue lines), the fact that $x$ and $y$ are correlated is not taken into account. In principle if we knew that $x$ takes the value $x_{i}$, then we should be drawing from the conditional distribution, shown with dashed red line.


[^0]:    ${ }^{1}$ we use the term "features" for all the descriptors we may use to represent a light-curve with a numerical vector

One of the main characteristics that an imputation method must have to deal with astronomical catalogs is that the imputation time for new elements with missing data should be very fast, due to the amount of objects in catalogs. There are several data imputation methods presented in the literature (e.g. (Troyanskaya et al. 2001; Daniel J. Stekhoven \& Bühlmann 2012)). In the method proposed by Troyanskaya et al. (2001) they used $K$ nearest neighbors to impute the missing data. The basic idea is to select the $K$ nearest neighbors in the space of the non-missing features and then predict the missing variable using a weighted average of the neighbors in that variable. Unfortunately with this method, each time we ask for the imputation of one value we need to find the $K$ nearest objects, which takes a considerable amount of time if we are dealing with millions of object where we want to impute missing data. The method proposed by Daniel J. Stekhoven \& Bühlmann (2012) they use one different Random Forest (Breiman 2001a) model to predict each of the features in the data set. Having $n$ features, they fit $n$ different Random Forests, where the $i$-th Random Forest is trained with the features $\{1, \ldots, i-1, i+1, \ldots, n\}$ as predictors and the variable $i$ as a response. To train a Random Forest with variable $i$ as a response, they only use the observed part of variable $i$ in the training set. Even though in the paper they propose the iterative model using the whole data (impractical for astronomical catalogs), we might iterate only using a training set and then use the set of forests to impute data in the big catalogs. In astronomical catalogs usually features correspond to astrophysical variables of objects, in many cases, astronomers may want to know an indicator of uncertainty in the prediction, or a probability distribution over the imputation value, unfortunately from Random Forests is hard to directly get uncertainty indicators for continuous responses, given that the model do not provide a distribution over the predictions.

In this work, we use (not Naive) Bayesian networks. Bayesian networks are models that represent probabilistic dependency relationships among features using graphs (J. 1988), where nodes represent the features and connections provide information about the probabilistic dependency relationships between features. Bayesian networks belong to the family of graphical models and they are very suitable to perform inference on a set of features given observations.

Some recent works in astronomy use Bayesian network models for automatic classification (Mahabal et al. 2008; M.Turmon et al. 2012). Also Broos et al. (2011) propose a Machine Learning model to classify X-ray sources using a naive scheme, where all features are assumed to be independent given the class.

Usually in catalogs with missing data, the missing features are different depending on the object. That is the main reason to use a model that can deal with evidences that change from object to object. We assume that the nature of missing data is MAR (Missing at Random) or MCAR (Missing Complete at Random). MCAR means that the probability that a feature is missing is independent of the other features in observations. MAR means that the missing features may depend on the values of the observed component. MAR and MCAR cases can be handled with our model because we find the dependencies (or independencies) between features with BNs. For

NMAR cases (Not Missing at Random), the probability that a feature is missing may depend on the other missing values (for example, no detections when the observed objects are too faint). We do not know any method able to handle NMAR cases without ad hoc distribution for the missing values.

Note that even in the case we have a complete training set, the resulting classification model will only be able to classify objects that have complete information. In other words, we cannot use a classification model to predict objects with missing features. One option to mitigate this problem is to abstain from predicting for those objects, but that hinders the completeness of the prediction. With the proposed method, we can impute the data while predicting based on the learned Bayesian network.

In this work, we use as a base catalog, the MACHO catalog (et al. Alcock C. 1997), and extract 14 features from each lightcurve. We then combine the MACHO catalog with other catalogs containing magnitudes at different wavelengths. We show how a Bayesian networks in combination with a Random forest classifier can overcome the missing data problem and outperform other methods. Applying this model on a real dataset we are able to generate catalogs of variable source with extremely high fidelity.

Section 2.1 summarizes Bayesian networks, in section 2.2 we show how BN can be used to infer missing values. Sections 2.3 and 2.4 show how we build BN, first with complete data and then with missing values. Section 3 contains the classification mechanism. Results from experiments with real data are shown in section 4. Conclusions follow in section 5.

## 2. THEORETICAL BACKGROUND

### 2.1. Bayesian Networks

A Bayesian network (BN) is a probabilistic model that belongs into the special class of graphical models. Graphical models deal with uncertain data in presence of latent variables. Latent variables can include any information that is unobservable, such as the mass of a star. In short, anything that is relevant to explain the observed data but was itself not observed, can become a latent variable. In a graphical model one assumes certain local statistical dependencies between the random variables that correspond to the latent variables and observed data. BNs are directed graphical models, in which the statistical dependency between random variables is based on directional relationships. Another class of graphical modes, not relevant to this paper, are undirected graphical models, such as Markov random networks. Many models that are typically not described as graphical models can be reinterpreted within a graphical modeling framework. Similarly, many process models or stochastic processes can be couched as graphical models.

To better explain the fundamentals of a Bayesian Network we present a simple example. Consider a lightcurve of a source and we examine certain properties of the lightcurve and other available information such as PSF size, magitude, color, etc. In this example we want to determine if the star is periodic or not. If the star exhibits periodic behavior that is larger than the error a standard and assume the source has been observed often and for long time, a simple periodiogram would flag

![img-1.jpeg](img-1.jpeg)

Fig. 2.- Bayesian network for the periodogram example.

This source as periodic very reliably. Unfortunately a faulty CCD or unreliable electronics can mimic the periodic behavior which can fool the periodiogram. Regular engineering reports can reveal such behavior. Finally, you want to confirm every detection with a visual inspection. To model this situation, we can use a Bayesian network as shown in fig. 2, where nodes are the random variables and arrows indicate conditional dependencies between variables. The network encodes the intuition that the status of the periodiogram results depend on faulty CCD or actual periodic variation, and that the final call depends on the results of the visual inspection that only happens if the periodiogram indicates that the source is periodic. It is useful to think of these conditional dependencies as causal relationships between variables, periodic behavior might cause the periodiogram to flag a light curve as periodic, which in turn might pass the visual inspection. However, you should keep in mind that Bayesian networks can also be constructed in the absence of any causal interpretation. This is how Pearl (1994) originally thought of Bayesian network as a way to reason probabilistically about causes and effects.

More formally, let $S = \{x_1, \ldots, x_n\}$ be a set of data instances (these are the lightcurves), each one described with a set of $D$ features $\{F_1, \ldots, F_D\}$ (these are the lightcurve features and/or brightness magnitudes). Each instance $x_i$ is represented as a vector $x_i = \{F_1^i, \ldots, F_D^i\}$. BNs can represent the joint probability distribution $P(F_1, \ldots, F_D)$ of dataset $S$ as a product of factors, where each factor is a conditional probability distribution of each node given its parents in the BN:

$$P(S) = \prod_{i=1}^{n} P(x_i) = \prod_{i=1}^{n} P(F_1^i, \ldots, F_D^i)$$

$$= \prod_{i=1}^{n} \prod_{j=1}^D P(F_j^i|\text{Pa}_{BN}^i(F_j)) \tag{1}$$

where $\text{Pa}_{BN}(F_j)$ represents the set of parents of variable $F_j$ in the BN and $\text{Pa}_{BN}(F_j)$ indicate that parents of feature $F_j$ are instantiated in the values of $x_i$.

One of the main advantages of the BN factorization is that each of the factors involves a smaller number of

![img-2.jpeg](img-2.jpeg)

Fig. 3.- Example of a Bayesian network with features $\{F_1, \ldots, F_5\}$. The joint distribution can be factorized as the product of five probabilities, each one corresponding to the probability of the respective node variable given its parents in the network

features, where it is easier to estimate.

For example, in figure 3 we show a BN in a domain of five features $\{F_1, \ldots, F_5\}$. The joint probability distribution can be factorized according to the BN as:

$$P(F_1, \ldots, F_5) = P(F_1|F_4)P(F_2)P(F_3|F_5) \cdot P(F_4)P(F_5|F_2, F_4)$$

In this case, instead of estimating a probability distribution over the five dimensional space $(F_1, \ldots, F_5)$ we only need to estimate simpler distributions, such as $P(F_1|F_4), P(F_2), P(F_3|F_5), P(F_4)$, and $P(F_5|F_2, F_4)$.

### 2.2. Inference in Bayesian Networks

BNs are useful to make inference on any unobserved variable given a set of evidence. In our case, we aim to use BNs to predict values of missing features given the observed ones.

For example, consider the same BN as in Figure 3 and suppose we found an object with missing values $F_5$ and $F_2$ (we can observe $F_1, F_3, F_4$). If we want to estimate the most probable value for variable $F_5$ given the observed values for $F_1, F_3, F_4$, we can calculate $P(F_5|F_1, F_3, F_4)$ as:

$$P(F_5|F_1, F_3, F_4) = \frac{P(F_1, F_3, F_4, F_5)}{P(F_1, F_3, F_4)}$$

$$= \frac{\sum_{F_2} P(F_1, F_2, F_3, F_4, F_5)}{\sum_{F_2, F_5} P(F_1, F_2, F_3, F_4, F_5)}$$

$$= \frac{\sum_{F_2} P(F_1|F_4)P(F_2)P(F_3|F_5)P(F_4)P(F_5|F_2, F_4)}{\sum_{F_2, F_5} P(F_1|F_4)P(F_2)P(F_3|F_5)P(F_4)P(F_5|F_2, F_4)}$$

$$= \frac{P(F_1|F_4)P(F_3|F_5)P(F_4)\sum_{F_2} P(F_2)P(F_5|F_2, F_4)}{P(F_4)P(F_1|F_4)\sum_{F_2, F_5} P(F_3|F_5)P(F_2)P(F_5|F_2, F_4)}$$

Summing out the unobserved features and “pushing in” the factors in the sums is known as variable elimination (Pearl 1994), which is the simplest exact inference algorithm.

In this work we use Gaussian nodes inference (Shachter & Kenley 1989). Gaussian nodes are commonly used for continuous data, each variable is modeled with a Gaussian distribution where its parameters are linear combination of the parameters of the parent nodes in the Bayesian network. Let $F_{j}$ be a node with $p$ parents, where each parent has a Gaussian distribution with mean $\mu_{i}$ and variance $\sigma_{i}$ $(i \in [1 \ldots p])$. We model $F_{j}$ with a Gaussian distribution with mean $\mu=\left[\mu_{1}, \ldots, \mu_{k}\right]$ and covariance matrix $\Sigma=\left[\sigma_{i k}\right]$, where $\sigma_{i k}$ is the covariance between the $i$-th parent of $F_{j}$ and the $k$-th parent of $F_{j}$. The probability distribution for node $F_{j}$ is:

$$
P\left(F_{j}\right)=\mathcal{N}\left(\beta_{0}+\beta^{T} \mu ; \sigma^{2}+\beta^{T} \Sigma \beta\right)
$$

Where $\beta$ and $\sigma$ are the parameters of the linear combination (which need to be estimated in the learning process). In section 2.3.2 we explain details about Gaussian nodes representation and how to estimate the parameters. For the scope of this section, we assume that the parameters are known.

The simple idea behind inference with Gaussian nodes is that features that are not involved in the calculus of a probability can be eliminated from the Bayesian network (barren nodes). The easiest barren nodes to be eliminated are leaf nodes because they can be deleted without doing any other change in the network. Unfortunately, not all barren nodes are leaves. The key idea is to perform arc reversals in order to let barren nodes as leaves. When such a reversal is performed, to preserve the joint distribution the network has to be adjusted, or re-learned. Shachter & Kenley (1989) describes a methodology for adjusting the network parameters that we adapted for this work too (see Appendix A for details).

### 2.3. Learning Bayesian Networks with complete data

In previous section we showed how to make inference once the BN is known. Learning the network involves learning the structure (edges) and the parameters (probability distributions on each of the factors). We explain both cases separately in the next subsections.

### 2.3.1. Structure Learning with complete data

Given that the number of possible network structures grows exponentially with the number of nodes or features (Cooper & Herskovits 1992), it is not possible to do an exhaustive search. Usually a greedy search strategy it is necessary to find a suitable solution, in this work we use the K2 algorithm (Cooper & Herskovits 1992). Starting with an initial random order of features (nodes) and an empty network (no edges), we start adding parents to each variable, such that the next parent we add is the one who creates the highest improvement in the network score, we keep adding parents until we complete the maximum allowed (parameter given by the user). In our work we use a maximum of three parents. Note that if one node has already two parents and we attempt to add the third one, it might be possible that keeping two
![img-3.jpeg](img-3.jpeg)

Fig. 4.- Example of a simple Bayesian network with features $\left\{F_{1}, F_{2}, F_{3}\right\}$ and the values each feature can take.
parents is better than adding a third one, in that case the node stays with two parents.

The score of a network structure is related to how the structure fits data. To calculate the score, we evaluate the probability of the structure given the data, which corresponds to apply the same factorization imposed by the structure and use multinomial distributions over each factor $\left(P\left(F_{j} \mid \mathrm{Pa}_{B N}\left(F_{j}\right)\right)\right.$ in eq. 1). We estimate each probability by firstly discretizing the possible values that each feature $F_{j}$ can take, $\left(f_{j 1}, \ldots, f_{j r_{j}}\right)$ and then creating a multi-dimensional histogram for $P\left(F_{j} \mid \mathrm{Pa}_{B N}\left(F_{j}\right)\right)$.

Consider the feature $F_{j}$. Let $q_{j}$ be the number of possible instantiations of the parents set $\mathrm{Pa}_{B N}\left(F_{j}\right)$. Recall $r_{j}$ be the maximum number of values that variable $F_{j}$ can take. Let $N_{k, m}^{j}$ be the number of cases in data where variable $F_{j}$ has the value $f_{j k}\left(k \in\left[1 \ldots r_{j}\right]\right)$ when its set of parents $\mathrm{Pa}_{B N}\left(F_{j}\right)$ is instantiated to some value $w_{l n}^{j}$, and let $N_{l n}^{j}=\sum_{k=1}^{r_{j}} N_{k, m}^{j}$. For example, in figure 4, if $j=2,\left[f_{j 1}=1, f_{j 2}=2, \ldots, f_{j 4}=4\right]$, $q_{j}=6(3 \times 2$ possible values of the joint combination of parents), $w_{1}^{j}=\left\{\begin{array}{ll}1 & 1\end{array}\right\}, w_{2}^{j}=\left\{\begin{array}{ll}1 & 2\end{array}\right\}, \ldots, w_{6}^{j}=\left\{\begin{array}{ll}3 & 2\end{array}\right\}$. Note that $m$ is an index moving in the possible combinations of values of the joint set of parents $(m \in[1 \ldots 6])$.

Then the probability of a given structure $B_{s}$ can be shown to be given by (see Appendix B for a derivation):

$$
\begin{aligned}
P\left(B_{s} \mid \text { data }\right)= & P\left(B_{s}\right) \prod_{j=1}^{D} \prod_{m=1}^{q_{j}} \frac{\left(r_{j}-1\right)!}{\left(N_{j m}+r_{j}-1\right)!} \times \\
& \times \prod_{k=1}^{r_{j}} N_{j m k}!
\end{aligned}
$$

where the term $P\left(B_{s}\right)$ is the prior on the network structure $B_{s}$.

### 2.3.2. Parameter Learning with complete data

Learning the parameters of a BN means to learn the distribution of each of the factors in the right side of equation 1. The factorization of equation 1 is given by the structure of the BN. This tells us that to learn the parameters it is necessary first to know the structure.

Given that features involved in our work are all continuous, we again use Gaussian nodes (Shachter & Kenley 1989).

Let $F_{j}$ be a node in the network and $\mathrm{Pa}_{B N}\left(F_{j}\right)$ the set of parents for $F_{j}$. Lets assume that $F_{j}$ has $k$ parents

$\left(\left|\operatorname{Pa}_{B N}\left(F_{j}\right)\right|=k\right)$ and we model $F_{j}$ as a linear Gaussian of its parents:

$$
P\left(F_{j}\right)=\mathcal{N}\left(\beta_{0}+\beta^{T} \mu ; \sigma^{2}+\beta^{T} \Sigma \beta\right)
$$

where the set of parents $\mathrm{Pa}_{B N}\left(F_{j}\right)$ are jointly Gaussian $\mathcal{N}(\mu ; \Sigma)$ and $\mu, \Sigma$ are calculated from the data. Note that $\mu$ and $\beta$ are $k$ dimensional vectors, and the matrix $\Sigma$ is $k \times k$.

To learn a Gaussian node, we learn the set of parameters $\left\{\beta_{0}, \ldots, \beta_{k} ; \sigma\right\}$ of the linear combination. Let $\mathrm{Pa}_{B N}\left(F_{j}\right)=\left\{\tilde{F}_{1}, \ldots, \tilde{F}_{k}\right\}$ be the parent nodes with respective means $\left\{\mu_{1}, \ldots, \mu_{k}\right\}$, then $P\left(F_{j} \mid \mathrm{Pa}_{B N}\left(F_{j}\right)\right)=$ $\mathcal{N}\left(\beta_{0}+\beta_{1} \tilde{F}_{1}+\cdots+\beta_{k} \tilde{F}_{k} ; \sigma^{2}\right)$. Our task is to learn the set of parameters $\theta_{F_{j}}=\left\{\beta_{0}, \ldots, \beta_{k} ; \sigma\right\}$. To learn those parameters we optimize the log-likelihood, expressed as:

$$
\begin{aligned}
l_{F_{j}}\left(\theta_{F_{j}} \mid \text { data }\right)= & \sum_{i=1}^{n}\left[-\frac{1}{2} \log \left(2 \pi \sigma^{2}\right)-\frac{1}{2 \sigma^{2}}\left(\beta_{0}+\beta_{1} x_{i \tilde{F}_{1}}+\right.\right. \\
& \left.\left.\cdots+\beta_{k} x_{i \tilde{F}_{k}}-x_{i j}\right)^{2}\right]
\end{aligned}
$$

by setting its derivative with respect to $\beta_{0}$ to zero. We have:

$$
E\left[F_{j}\right]=\beta_{0}+\beta_{1} E\left[\tilde{F}_{1}\right]+\cdots+\beta_{k} E\left[\tilde{F}_{k}\right]
$$

where $E\left[F_{j}\right]=\mu_{j}$ is the expectation of the variable $F_{j}$ in the data. Setting the derivative of eq. 6 with respect to $\beta_{1}, \ldots, \beta_{k}$ to zero we have the following $k$ equations:

$$
\begin{aligned}
E\left[F_{j} \cdot \tilde{F}_{1}\right]= & \beta_{0} E\left[\tilde{F}_{1}\right]+\beta_{1} E\left[\tilde{F}_{1} \cdot \tilde{F}_{1}\right]+\cdots \\
& \cdots+\beta_{k} E\left[\tilde{F}_{k} \cdot \tilde{F}_{1}\right] \\
& \vdots \\
E\left[F_{j} \cdot \tilde{F}_{k}\right]= & \beta_{0} E\left[\tilde{F}_{k}\right]+\beta_{1} E\left[\tilde{F}_{1} \cdot \tilde{F}_{k}\right]+\cdots \\
& +\cdots+\beta_{k} E\left[\tilde{F}_{k} \cdot \tilde{F}_{k}\right]
\end{aligned}
$$

Setting the derivatives to zero, we end with $k+1$ linear equations with $k+1$ unknowns. We can solve the equations using standard linear algebra to find the $k+1$ solutions $\beta_{0}^{*}, \ldots, \beta_{k}^{*}$. To find $\sigma$ we replace the values of $\beta_{0}^{*}, \ldots, \beta_{k}^{*}$ in eq. 6 and set the derivative of the log likelihood with respect to $\sigma^{2}$ to zero, then we have:

$$
\sigma^{2}=\operatorname{cov}\left[F_{j}, F_{j}\right]-\sum_{p=1}^{k} \sum_{q=1}^{k} \beta_{p}^{*} \beta_{q}^{*} \operatorname{cov}\left[\tilde{F}_{p}, \tilde{F}_{q}\right]
$$

Where $\operatorname{cov}\left[\tilde{F}_{p}, \tilde{F}_{q}\right]=E\left[\tilde{F}_{p} \cdot \tilde{F}_{q}\right]-E\left[\tilde{F}_{p}\right] E\left[\tilde{F}_{q}\right]$. Note that if parent nodes are root nodes, they are just modeled with a unidimensional normal distribution and eq. 7,10 return the mean and variance of that variable.

### 2.4. Learning Bayesian Networks with missing data

Once we know how to learn the structure and the parameters of a Bayesian network under complete data, we now turn our attention on how to learn both the structure and the parameters under incomplete data. To learn the parameters with missing data, we need to previously know the structure and to learn the structure we need
to guess the missing values. This is done in a iterative method.

We start first describing the parameter learning algorithm and then the structure learning model.

### 2.4.1. Learning parameters with missing data

We assume that we already know the structure of the Bayesian network before we start learning the distribution parameters with missing data. The basic idea is to start estimating the joint distribution of the set of (root) parent nodes from incomplete data using a multivariate Gaussian distribution. Then we estimate the distribution of children nodes like in the complete data case (section 2.3.2) sampling the missing values of the parents from the distributions learned at the beginning.

To learn the parameters of a multivariate Gaussian distribution in the incomplete data case, we use the method proposed in Ghahramani \& Jordan (1995). To optimize the log likelihood of the model given the data under the missing data case, each data point $x_{i}$ can be written as $x_{i}=\left\{x_{i}^{o}, x_{i}^{m}\right\}$, using the super scripts $m$ and $o$ to indicate the features that are observed or missing. Let $\Sigma=\left\{\Sigma^{o o}, \Sigma^{o m}, \Sigma^{m o}, \Sigma^{m m}\right\}$ and $\mu=\left\{\mu^{m}, \mu^{o}\right\}$ be the covariance matrix and vector mean of the multivariate Gaussian distribution we are estimating. The log likelihood for incomplete data, including the new notation for $x_{i}$ and using a mixture of Gaussians distribution can be written as:

$$
\begin{aligned}
l\left(\theta \mid x^{o}, x^{m}\right)= & \sum_{i=1}^{n}\left[\frac{n}{2} \log 2 \pi+\frac{1}{2} \log \mid \Sigma\right] \\
& -\frac{1}{2}\left(x_{i}^{o}-\mu^{o}\right)^{T} \Sigma^{-1, o o}\left(x_{i}^{o}-\mu^{o}\right) \\
& -\left(x_{i}^{o}-\mu^{o}\right)^{T} \Sigma^{-1, o m}\left(x_{i}^{m}-\mu^{m}\right) \\
& -\frac{1}{2}\left(x_{i}^{m}-\mu^{m}\right)^{T} \Sigma^{-1, m m}\left(x_{i}^{m}-\mu^{m}\right)]
\end{aligned}
$$

Given that we have the likelihood expressed in terms of unknown latent features (the unobserved part of data), we optimise it using the expectation maximization (EM) algorithm (Dempster et al. 1977). EM optimizes the likelihood function of a model which depends on latent or unobserved features. The optimization procedure is a two step iteration. First step, the expectation step (Estep), calculates the expected value of the latent features to be used in the likelihood function. In other words, the E-step creates a function to be optimized, using the expected value of the latent features estimated from the current value of the unknown parameters. The maximization step (M-step) is the maximization of the likelihood function created by the E-step, generating a new value of the current parameters (to be used again in Estep).

In the E-step we need to estimate the unobserved part $x_{i}^{m}$. We can express the expected value of $x_{i}^{m}$ as:

$$
E\left[x_{i}^{m} \mid x_{i}^{o}, \mu, \Sigma\right]=\mu^{m}+\Sigma^{m o} \Sigma^{-1, o o}\left(x_{i}^{o}-\mu^{o}\right)
$$

Starting for an initial guess of the parameters $\mu$ and $\Sigma$, we calculate the expected value of missing data using equation 12 , then we optimise the values of $\mu$ and $\Sigma$ and we continue iterating until $\mu$ and $\Sigma$ do not change substantially.

After estimating the joint Gaussian distribution of the set of parents, we can estimate the Normal distribution of the children like in the complete data case (sec. 2.3.2) where the missing values of the parent are sampled from the learned multivariate Gaussian.

### 2.4.2. Learning the network structure with missing data

To learn the structure of a Bayesian network with missing data, we complete the missing values and then iterate to improve these values using the structure learned so far (Singh 1997). Algorithm 1 shows the main steps to construct a Bayesian network structure from missing data.

```
Algorithm 1: Algorithm to Learn BN structure with
missing data
- Learn for each variable in \(\left\{F_{1}, \ldots, F_{D}\right\}\) an univariate Gaussian
    Mixture \(G M(i) i \in[1 \ldots D]\)
- Create \(M\) complete datasets \(D_{s}^{1}, s \in[1 \ldots M]\) filling the missing
    values of each variable \(F_{i}\) with values sampled from \(G M(i)\);
- \(t=1\);
while Convergence criteria is not achieved do
    for \(s=1\) to \(M\) do
        From each complete dataset in \(D_{s}^{(t)}\) learn a BN, \(B_{s}^{(t)}\) (sec.
            2.3.1)
    - Create one Bayesian network structure \(B^{(t)}\) as the union of
    all the BNs \(a\);
    - Learn the parameters \(\theta^{(t)}\) using the original incomplete data
    and the network structure \(B^{(t)}\) (section 2.4.1);
    - Use the network \(\left\langle B^{(t)}, \theta^{(t)}\right\rangle\) to sample new values and create
    new completed datasets \(D_{s}^{(t+1)}\);
    - \(t=t+1\);
    *The union is performed in two steps: i) make all structures
    \(B_{s}^{(t)}\) consistent with the features order used in the algorithm
    from sec. 2.3.1 by performing arc reversals and ii) create the
    arc union of all the consistent structure from the previous step
```

The convergence criteria is that the score of the network $\left\langle B^{(t)}, \theta^{(t)}\right\rangle$ does not change substantially. Note that in the first iteration we just fill the missing values using an independent Gaussian mixtures model. Although independency is a very strong assumption, in our case does not affect the final result given that in all subsequent steps we re-fill the missing values with data sampled from the current Bayesian Network, in other words we use all probabilistic dependencies between features given by the network structure.

## 3. THE AUTOMATIC CLASSIFICATION MODEL

In previous sections we show how to fill missing values using probabilistic dependencies between features. After we infer the missing values using the Bayesian network, we proceed to train the automatic classifier using the new training completed set. In this work we use a Random Forest (RF) classifier (Breiman 2001a), which is a popular and very efficient algorithm based on decision
tree models (Quinlan 1993) and Bagging for classification problems (Breiman 1996, 2001b) ${ }^{2}$. It belongs to the family of ensemble methods, appearing in machine learning literature at the end of nineties (Dietterich 2000) and has been used recently in the astronomical journals (Pichara et al. 2012; Carliles et al. 2010; Richards et al. 2011). We give a very brief explanation here of how RF works; the reader can find detailed description in Breiman (2001a).

The process of training or building a RF given training data is as follows:

- Let $P$ be the number of trees in the forest (model parameter) and $F$ be the number of features describing data.
- Build $P$ sets of $n$ samples taken with replacement from the training set; this is called bagging. Note that each of the $P$ bags has the same number of elements with the training set but less different examples, given that the samples are taken with replacement (The training set also has $n$ samples).
- For each of the $P$ sets, train a decision tree (without prunning) using at each node a random sample of $F^{\prime} \leq \leq F$ possible features to select the one that optimises the split. ( $F^{\prime}$ is a model parameter)

The RF classifier creates many linear separators, attempting to separate between elements of different classes using some features (the ones given by the nodes of each decision tree) and some data points (the ones given by each of the bags).

Each of the decision trees creates one decision and the final decision is the most voted class among the set of $P$ decision trees (see Breiman (2001b) for more details). Worth noting, Breiman (2001b) showed that as the number of trees goes to infinity the classification error of the RF becomes bounded and the classifier does not overfit the data.

## 4. EXPERIMENTAL RESULTS

In this section we show the results from the application of the model on four astronomical catalogs, three with missing values. We not only show the advantages of the model, but we produce a catalog of variable stars within the LMC which is available for downloading ${ }^{3}$.

First, we prove the imputation accuracy of our model performing imputation tests in real datasets. Then, to test the advantage of the model, we proved three main facts: i) it is possible to learn an automatic classification model that is able to deal with missing data, ii) information with missing data can be useful for automatic classification, in other words the model outperforms any model that uses a subset of training set with complete data, iii) the proposed model overcomes the case where missing data is filled using traditional statistical methods that model each variable independently.

Fortunately the main computational cost of the algorithm occurs during the training phase, where the model

[^0]
[^0]:    ${ }^{2}$ Other models can be used for classification, but we found that RF gives superior results
    ${ }^{3}$ http://iic.seas.harvard.edu/research/time-series-center

needs to learn the Bayesian network structure and parameters. After training the model, to perform the inference on missing values for a lightcurve takes a fraction of a second.

We use three astronomical catalogs with missing data, SAGE (Margaret Meixner and Karl D. Gordon and Remy Indebetouw and Joseph L. Hora and Barbara Whitney and Robert Blum and authors 2006), UBVI (Piatti, A.E. and Claria, J.J. and Ahumada 2011) and 2MASS (Skrutskie, M. F.; Cutri, R. M.; Stiening, R.; Weinberg, M. D.; Schneider, S.; Carpenter, J. M.; Beichman, C.; Capps, R.; Chester, T.; Elias, J.; Huchra, J.; Liebert & Authors 2006). We also use the MACHO catalog (et al. Alcock C. 1997), with no missing values, but useful in comparing the lightcurve classification accuracy between the MACHO features with the additional incomplete extra features from SAGE, UBVI and 2MASS. We process around 20 million of objects. The MACHO lightcurves are described using 14 variability features: CAR $\sigma$, Mean Mag, CAR $\tau$, $\sigma$, $\eta$, Con, Stetson L, CuSum, B-R, Period, Period SNR, Stetson K AC, N above 4, N below 4. See (Pichara et al. 2012) for a description of the MACHO features.

### 4.1. Imputation Tests

To calculate the imputation error, we use the MACHO dataset where we randomly delete $5 \%, 10 \%, 15 \%$ and $20 \%$ of data entries in order to simulate missing values. We run our model and measure the $N R M S E$ (Normalized Root Mean Squared Error) over the predicted values, defined as:

$$ N R M S E=\sqrt{\frac{\operatorname{Mean}\left(\left[x_{\text {imp }}-x_{\text {true }}\right]^{2}\right)}{\operatorname{var}\left(x_{\text {true }}\right)}} $$

Where $x_{\text {imp }}$ is the imputed value and $x_{\text {true }}$ is the true value. When the estimation is accurate, $N R M S E$ approaches 0.0 where when the estimation is equivalent to a random guess, NRMSE approaches to 1.0. We compare our imputation results with an imputation method using mixtures of Gaussians. Table 1 shows our results.

TABLE 1 NRMSE using Bayesian Networks and Gaussian Mixtures in MACHO dataset. Missing values were artificially generated COMPletely at random


We can see from table 1 that BN method present less NRMSE compared with Gaussian Mixtures Imputation.

### 4.2. Interpreting the $B N$

One of the advantages of Bayesian networks is that they provide a conditional probability structure of features, which can be interpreted to attain deeper insight into your data. Figure 5 shows the BN structure our model found for the MACHO dataset. Connection among features indicates a degree of probabilistic dependency among features. Nodes that are not connected

TABLE 2 Percentage of missing values on SAGE/2MASS catalogs


TABLE 3 Percentage of missing values on UBVI catalog


with any other nodes are estimated independently from the others. We added colours to the nodes to indicate groups of features that belong to the same "type" of features. For example, features related to the magnitude level of the object are in red, as we can see, there are many connections among these kind of nodes, showing that the learning algorithm despite the missing data was able to detect most of the dependency relationships. There are some relationships that the model could not find, for example, the feature CAR $\tau$ was modelled as independent given that is not connected with any other feature in the network structure.

### 4.3. Classification results in missing data catalogs

For SAGE and 2MASS we used a training set of 1955 objects described in 7 features $\left(J, H, K, \mathrm{~m}*{36}, \mathrm{~m}*{45}, \mathrm{~m}*{58}, \mathrm{~m}_{80}\right)$. Table 2 shows the percentage of missing values for different features in SAGE/2MASS catalogs.

For UBVI catalog (Piatti, A.E. and Claria, J.J. and Ahumada 2011) we used 4193 training instances described in 4 features $(U, V, B, I)$. Table 3 shows the percentage of missing values for different features in UBVI training set.

We created one training set gathering all SAGE, 2MASS and UBVI training sets. The resulting training set contains seven classes of stars: Non-Variables, Quasars (QSO), Be Stars, Cepheids, RR Lyrae, Eclipsing Binaries (EB) and Long Periodic Variables (LPV). The number of objects per class on SAGE-2MASS-UBVI training set is described in table 4.

To evaluate the capabilities of our model dealing with missing data, we compared the results of classification accuracy of our model versus filling the missing data with independent Gaussian Mixtures model on each variable. Then we take samples from that distribution to replace the missing values.

These experiments allows us to show the importance of analyze the dependency relationship between features in order to make inference on missing values. To measure the accuracy we use precision, recall and F-Score,

![img-4.jpeg](img-4.jpeg)

Fig. 5.— Bayesian Network structure for the MACHO dataset, colours indicate that the nodes belong to the same type of features.

TABLE 4
NUMBER OF OBJECTS PER CLASS ON SAGE-UBVI TRAINING SET


defined as:

F-Score = $2 \times \frac{\text{precision} \times \text{recall}}{\text{precision} + \text{recall}}$,

where precision and recall are defined as:

$$
\text{precision} = \frac{\text{TP}}{\text{TP}+\text{FP}} \quad \text{recall} = \frac{\text{TP}}{\text{TP}+\text{FN}}
$$

where TP, FP and FN are the number of true positives, false positives and false negatives respectively. Note that all these values are obtained using a 10-fold cross validation process.

Table 5 shows the accuracy for the model which uses Gaussian Mixtures and the accuracy of the proposed model. We can see that our model present better results in most of the classes (bold numbers), for example, we can see significant improvement in the recall of quasars, which indicates that the model is able to detect more quasars that the model which fills features independently. We also increase the precision and recall for Be stars, RR-Lyraes, and Long Periodic Variables.

After evaluating our proposed method with SAGE, 2MASS and UBVI catalogs, we aim to probe that all the information encoded by these catalogs is useful to classify variable stars after missing data were imputed. To probe that, we combined again the SAGE-2MASS-UBVI training set with a training set used by Pichara et al. (2012) in a previous work, the MACHO catalog (et al. Alcock C. 1997). In the previous work, an automatic classifier was built in order to detect quasars in MACHO database. This training set was created extracting 14 time series features per band (see Pichara et al. (2012) for further details). To evaluate the contribution of our model we trained a new classifier which uses the previous 14 features from Pichara et al. (2012) and the new features from SAGE-2MASS-UBVI training set, after our model processed the missing values. We expect that the new classifier improves the quasar classification showing higher recall and precision values in the training set and getting a new high quality list of quasar candidates. Table 6 shows the results of both training set, with and without SAGE-2MASS-UBVI catalog, showing that we improve the value of F-Score in quasar detection.

Moreover, after training the model, we run it on the whole MACHO catalog, in order to generate a new quasar candidate list. To evaluate the quality of the new quasar candidate list, we calculate the matching level of our list of candidates with the previous known lists. We use the recent works (Kim et al. 2012; Pichara et al. 2012) to compare their candidates with the list proposed in this work. Kim et al. (2012) found a list of 2566 candidates and a refined list of 663 strong candidates. In Pichara et al. (2012), we found a list of 2551 candidates, with 74% of matches with the 663 refined strong candidates. In this work we improve the list, getting a list of 1730 candidates, from where we got 562 matches with the previous list of 2566 candidates and 502 matches with the

TABLE 5
Precision, Recall and F-Score for different classes using two different methods for filling missing values in SAGE-2MASS-UBVI training set. 1) Independent Mixtures of Gaussian and 2) Our model.


TABLE 6
Precision, Recall and F-Score to compare the model used Pichara et al. (2012) with and without the information of SAGE-UBVI training set


previous list of 663 strong candidates ( $75.7 \%$ ). We can see that our list of 1730 candidates has about the same level of matching with the previous strong candidate list but reducing the size of the list by a $32 \%$.

## 5. CONCLUSIONS

We show a new way of dealing with missing data, testing on real astronomical datasets, showing that catalogs with miss- ing data can be useful for automatic classification. One of the main advantages of our model is that it makes possible to integrate catalogs in order to increase the available information for the training process. We improve the accuracy of our results in previous work on quasar detection due to the integration of new catalogs with missing data. Our model considers probability dependencies between features that make possible to take
advantage of the observed values, in order to increase the accuracy of the estimation when the number of observed values increase. Most of the computational time required is during the training time that makes possible to run the model in complete catalogs because the model just need to perform inference on the missing values, which takes less than a second per object.

## ACKNOWLEDGMENTS

This work is supported by Vicerrectoría de Investigación (VRI) from Pontificia Universidad Católica de Chile, Institute of Applied Computer Science at Harvard University, and the Chilean Ministry for the Economy, Development, and Tourism's Programa Iniciativa Científica Milenio through grant P07-021-F, awarded to The Milky Way Millennium Nucleus.

# APPENDIX 

## ARC REVERSAL

To understand the meaning of arc reversal, it helps to think as each node propagates its variance downstream to its successors (these variances are the elements of the covariance matrix in eq. 5 as we describe in sec. 2.3.2). Suppose we reverse the arc $F_{i} \rightarrow F_{j}$. Before reversing, part of the variance in $F_{j}$ was explained by $F_{i}$, then after the reversal we have to compensate this by adding an arc from the parents of $F_{i}$ to $F_{j}$. Also, part of the variance of $F_{i}$ is now explained by $F_{j}$, so $F_{i}$ 's new variance must be discounted in order to adjust for that value. Figure 6 shows an example of the arc reversal procedure and updates of variances. In that example $F_{4}$ is a barren node but can not be remove from the network for it is not a leaf node. By reversing the arc $\left\{F_{4} \rightarrow F_{5}\right\}$ to $\left\{F_{5} \rightarrow F_{4}\right\}$ the variances and edge parameters are adjusted as described in the figure. With the arc reversed $F_{4}$ is now a leaf node and can be removed from the network.

Formally, suppose we want to perform inference to calculate $P\left(F_{J} \mid F_{K}\right)$, where $F_{J}$ and $F_{K}$ are sets of features such that $F_{J} \cap F_{K}=\emptyset$. Let $N$ be the total set of nodes in the network $\left(\left(F_{J} \cup F_{K}\right) \subset N\right)$. We first create an ordered sequence $s$ of nodes in $N$ such that $F_{K} \prec_{s} F_{J} \prec_{s} N \backslash\left(F_{J} \cup F_{K}\right)$ (Note that " $\backslash$ " is the sets subtraction operator). We use the notation $\prec_{s}$ just to define an order relationship between the elements inside the sequence $s$, then if $F_{K} \prec_{s} F_{J}$ means that $F_{K}$ is before $F_{J}$ in $s$. The idea of this order is just leave evidence nodes before in the sequence, that ensures that they will be ancestors in the network, making easier the flow of information in the graph. The steps to perform inference are:

[^0]The last step of the algorithm simply uses the Bayesian network factorization to calculate the desired probability $P\left(F_{J} \mid F_{K}\right)$. Given that the barren nodes are not longer available in the BN, the joint probability is expressed only through features in $F_{J} \cup F_{K}$. Note that nodes in $F_{J}$ are descendants of nodes in $F_{K}$, and nodes in $F_{K}$ are all observed, then we just instantiate them to their values and calculate directly the probability of nodes in $F_{J}$ given the values in $F_{K}$.


[^0]:    Given the ordered sequence $\prec_{s}$ : for each arc $F_{i} \rightarrow F_{j}$ in the $B N$ do
    if $F_{j} \prec_{s} F_{i}$ then reverse the arc $F_{i} \rightarrow F_{j}$;
    Delete all nodes in $N \backslash\left(F_{J} \cup F_{K}\right)$ from the resulting network ;

# BN SCORE 

In this section we show a derivation of the equation 4 for BN score (Cooper \& Herskovits 1992). The score of a network structure is related to how the structure fits data. To calculate the score, we evaluate the probability of the structure given the data, which corresponds to apply the same factorization imposed by the structure and use multinomial distributions over each factor $\left(P\left(F_{j} \mid \mathrm{Pa}_{B N}\left(F_{j}\right)\right)\right.$ in eq. 1). We estimate each probability by firstly discretizing the possible values that each feature $F_{j}$ can take, $\left(f_{j 1}, \ldots, f_{j r_{j}}\right)$ and then creating a multi-dimensional histogram for $P\left(F_{j} \mid \mathrm{Pa}_{B N}\left(F_{j}\right)\right)$.
Consider the feature $F_{j}$. Let $q_{j}$ be the number of possible instantiations of the parents set $\mathrm{Pa}_{B N}\left(F_{j}\right)$. Recall $r_{j}$ be the maximum number of values that variable $F_{j}$ can take.
Let $N_{k, m}^{j}$ be the number of cases in data where variable $F_{j}$ has the value $f_{j k}\left(k \in\left[1 \ldots r_{j}\right]\right)$ when its set of parents $\mathrm{Pa}_{B N}\left(F_{j}\right)$ is instantiated to some value $w_{m}^{j}$, and let $N_{m}^{j}=\sum_{k=1}^{r_{j}} N_{k, m}^{j}$.

To decide for the best structure, we need an expression for the probability of a given structure under presence of data $\left(P\left(B_{s}\right.\right.$, data $\left.)\right)$. Given that per each structure we can have a different set of parameters $\left(\theta_{s}\right)$, we need to condition in the parameters and integrate them out.
Using multinomial distributions we have:

$$
\begin{aligned}
P\left(B_{s}, \text { data }\right)= & \int_{\theta_{s}} P\left(\operatorname{data}\left|B_{s}, \theta_{s}\right) P\left(\theta_{s} \mid B_{s}\right) P\left(B_{s}\right) d \theta_{s}\right. \\
= & P\left(B_{s}\right) \int_{\theta_{s}}\left[\prod_{j=1}^{D} \prod_{m=1}^{q_{j}} \prod_{k=1}^{r_{j}} \theta_{j k m}^{N_{k, m}^{j}}\right] \times \\
& \times P\left(\theta_{s} \mid B_{s}\right) d \theta_{s} \\
= & P\left(B_{s}\right) \int_{\theta_{j k m}} \int \\
& {\left[\prod_{j=1}^{D} \prod_{m=1}^{q_{j}} \prod_{k=1}^{r_{j}} \theta_{j k m}^{N_{k, m}^{j}}\right] \times } \\
& \times\left[\prod_{j=1}^{D} \prod_{m=1}^{q_{j}} P\left(\theta_{j 1 m}, \ldots, \theta_{j r_{j} m}\right)\right] \\
& d \theta_{111}, \ldots, d \theta_{j k m}, \ldots, d \theta_{D r_{j} q_{j}}
\end{aligned}
$$

Assuming a uniform distribution for $P\left(\theta_{j 1 m}, \ldots, \theta_{j r_{j} m}\right)$ we have that $P\left(\theta_{j 1 m}, \ldots, \theta_{j r_{j} m}\right)=C_{j m}$ (for some constant $C_{j m}$ ). Given that $C_{j m}$ is also a density function:

$$
\int_{\theta_{j k m}} \ldots \int C_{j m} d \theta_{111}, \ldots, d \theta_{D r_{j} q_{j}}=1
$$

Solving equation B2 yields $C_{j m}=\left(r_{j}-1\right)$ ! (see appendix of (Cooper \& Herskovits 1992)). Substituting this result and using independence of terms in equation B1 we have that:

$$
\begin{aligned}
P\left(B_{s}, \text { data }\right)= & P\left(B_{s}\right) \prod_{j=1}^{D} \prod_{m=1}^{q_{j}} \int_{\theta_{j k m}} \int \\
& {\left[\prod_{k=1}^{r_{j}} \theta_{j k m}^{N_{k, m}^{j}}\right]\left(r_{j}-1\right)! } \\
& d \theta_{111}, \ldots, d \theta_{j k m}, \ldots, d \theta_{D r_{j} q_{j}}
\end{aligned}
$$

The multiple (Dirichlet) integral in equation B3 has the following solution (Samuel S. Wilks 1962):

$$
\begin{gathered}
\int_{\theta_{j k m}} \ldots \int \prod_{k=1}^{r_{j}} \theta_{j k m}^{N_{k, m}^{j}} d \theta_{111}, \ldots, d \theta_{D r_{j} q_{j}}= \\
\frac{\prod_{k=1}^{r_{j}} N_{k, m}^{j}!}{\left(N_{m}^{j}+r_{j}-1\right)!}
\end{gathered}
$$

Substituting the result of equation B4 in equation B1 we have that:

$$
P\left(B_{s} \mid \text { data }\right)=P\left(B_{s}\right) \prod_{j=1}^{D} \prod_{m=1}^{q_{j}} \frac{\left(r_{j}-1\right)!}{\left(N_{m}^{j}+r_{j}-1\right)!} \prod_{k=1}^{r_{j}} N_{k, m}^{j}!
$$

where the term $P\left(B_{s}\right)$ is the prior on the network structure $B_{s}$. In this work we assume that all possible network structures are equally likely, so we use the same prior for all them. The expression $P\left(B_{s} \mid\right.$ data $)$ is the probability of the network structure given data, in other words, how good is the fit of the network structure with data. Better the structure fits the data, the higher the score $P\left(B_{s} \mid\right.$ data $)$. Then using the previous mentioned greedy search method, we select the structure that presents higher probability among the searched ones.