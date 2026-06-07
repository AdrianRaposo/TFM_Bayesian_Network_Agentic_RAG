# Optimization Problems for Machine Learning: A Survey 

Claudio Gambella ${ }^{1}$, Bissan Ghaddar ${ }^{2}$, Joe Naoum-Sawaya ${ }^{2}$<br>${ }^{1}$ IBM Research Ireland, Mulhuddart, Dublin 15, Ireland, ${ }^{2}$ Ivey Business School, University of Western Ontario, London, Ontario N6G 0N1, Canada


#### Abstract

This paper surveys the machine learning literature and presents in an optimization framework several commonly used machine learning approaches. Particularly, mathematical optimization models are presented for regression, classification, clustering, deep learning, and adversarial learning, as well as new emerging applications in machine teaching, empirical model learning, and Bayesian network structure learning. Such models can benefit from the advancement of numerical optimization techniques which have already played a distinctive role in several machine learning settings. The strengths and the shortcomings of these models are discussed and potential research directions and open problems are highlighted.


## Contents

1 Introduction ..... 2
1.1 Machine Learning Basics ..... 2
1.2 Machine Learning and Operations Research ..... 3
1.3 Aim and Scope ..... 3
2 Regression Models ..... 4
2.1 Linear Regression ..... 4
2.2 Shrinkage methods ..... 5
2.3 Regression Models Beyond Linearity ..... 6
3 Classification ..... 6
3.1 Logistic Regression ..... 7
3.2 Linear Discriminant Analysis ..... 7
3.3 Decision Trees ..... 8
3.4 Support Vector Machines ..... 10
3.4.1 Hard Margin SVM ..... 10
3.4.2 Soft-Margin SVM ..... 11
3.4.3 Sparse SVM ..... 11
3.4.4 The Dual Problem and Kernel Tricks ..... 12
3.4.5 Support Vector Regression ..... 13
3.4.6 Support Vector Ordinal Regression ..... 13
4 Clustering ..... 14
4.1 Minimum Sum-Of-Squares Clustering (a.k.a. $K$-Means Clustering) ..... 14
4.2 Capacitated Clustering ..... 15
4.3 $K$-Hyperplane Clustering ..... 15
5 Linear Dimension Reduction ..... 16
5.1 Principal Components ..... 16
5.2 Partial Least Squares ..... 17
6 Deep Learning ..... 17
6.1 Mixed Integer Programming for DNN Architectures ..... 19
6.2 Activation Ensembles ..... 21

7 Adversarial Learning ..... 22
7.1 Targeted attacks ..... 22
7.2 Untargeted attacks ..... 23
7.3 Adversarial robustness ..... 24
7.4 Data Poisoning ..... 25
8 Emerging Paradigms ..... 25
8.1 Machine Teaching ..... 25
8.2 Empirical Model Learning ..... 26
8.3 Bayesian Network Structure Learning ..... 27
9 Conclusions ..... 28

# 1 Introduction 

The pursuit to create intelligent machines that can match and potentially rival humans in reasoning and making intelligent decisions goes back to at least the early days of the development of digital computing in the late 1950s [198]. The goal is to enable machines to perform cognitive functions by learning from past experiences and then solving complex problems under conditions that are varying from past observations. Fueled by the exponential growth in computing power and data collection coupled with the widespread of practical applications, machine learning is nowadays a field of strategic importance.

### 1.1 Machine Learning Basics

Broadly speaking, machine learning relies on learning a model that returns the correct output given a certain input. The inputs, i.e., predictor measurements, are typically values that represent the parameters that define a problem, while the output, i.e., response, is a value that represents the solution.

Machine learning models fall into two categories: supervised and unsupervised learning [99, 129]. In supervised learning, a response measurement is available for each observation of predictor measurements and the aim is to fit a model that accurately predicts the response of future observations. More specifically, in supervised learning, values of both the input $x$ and the corresponding output $y$ are available and the objective is to learn a function $f$ that approximates with a reasonable margin of error the relationship between the input and the corresponding output. The accuracy of a prediction is evaluated using a loss function $\mathcal{L}(f(x), y)$ which computes a distance measure between the predicted output and the actual output. In a general setting, the best predictive model $f^{*}$ is the one that minimizes the risk

$$
\mathbb{E}_{p}[\mathcal{L}(f(x), y)]=\iint p(x, y) \mathcal{L}(f(x), y) d x d y
$$

where $p(x, y)$ is the probability of observing data point $(x, y)$ [210]. In practice $p(x, y)$ is unknown, however the assumption is that an independent and identically distributed sample of data points $\left(x_{1}, y_{1}\right), \ldots,\left(x_{n}, y_{n}\right)$ forming the training dataset is given. Thus instead of minimizing the risk, the best predictive model $f^{*}$ is the one that minimizes the empirical risk such that

$$
f^{*}=\arg \min \frac{1}{n} \sum_{i=1}^{n} \mathcal{L}\left(f\left(x_{i}\right), y_{i}\right)
$$

When learning a model, a key aspect to consider is model complexity. Learning a highly complex model may lead to overfitting, which refers to having a model that fits the training data very well but generalizes poorly to other data. The minimizer of the empirical risk will often lead to overfitting, and hence has a limited generalization property. Furthermore, in practice the data may contain noisy and incorrect values, i.e., outliers, which impacts the value of the empirical risk and subsequently the accuracy of the learned model. Attempting to find a model that perfectly fits every data point in the dataset is thus not desired, since the predictive power of the model will be diminished when points that are far from typical are fitted. Usually, the choice of $f$ is restricted to a family of functions $F$ such that

$$
f^{*}=\arg \min _{f \in F} \frac{1}{n} \sum_{i=1}^{n} \mathcal{L}\left(f\left(x_{i}\right), y_{i}\right)
$$

The degree of model complexity is generally dictated by the nature and size of the training data. While simpler models are advised for small training datasets that do not uniformly cover the possible data ranges, complex models need large data sets to avoid overfitting.

On the other hand, in unsupervised learning, response variables are not available and the goal of learning is to understand the underlying characteristics of the observations. Unsupervised learning thus attempts to learn from the distribution of the data the distinguishing features and the associations in the data. As such, the main use-case for unsupervised learning is exploratory data analysis, where the purpose is to segment and cluster the samples in order to extract insights. While with supervised learning there is a clear measure of accuracy by evaluating the prediction to the known response, in unsupervised it is difficult to evaluate the validity of the derived structure.

The fundamental theory of machine learning models and consequently their success can be largely attributed to research at the interface of computer science, statistics, and operations research. The relation between machine learning and operations research can be viewed along three dimensions: (a) machine learning applied to management science problems, (b) machine learning to solve optimization problems, (c) machine learning problems formulated as optimization problems.

# 1.2 Machine Learning and Operations Research 

Leveraging data in business decision making is nowadays mainstream as any business in today's economy is instrumented for data collection and analysis. While the aim of machine learning is to generate reliable predictions, management science problems deal with optimal decision making. Thus, methodological developments that can leverage data predictions for optimal decision making is an area of research that is critical for future business value $[30,146,172]$.

Another area of research at the interface of machine learning and operations research is using machine learning to solve hard optimization problems and particularly $\mathcal{N} \mathcal{P}$-hard integer constrained optimization [41, $138,139,158,214]$. In that domain, machine learning models are introduced to complement existing approaches that exploit combinatorial optimization through structure detection, branching, and heuristics.

Lastly, the training of machine learning models can be naturally posed as an optimization problem with typical objectives that include optimizing training error, measure of fit, and cross-entropy [42, 43, 77, 221]. In fact, the widespread adoption of machine learning is in part attributed to the development of efficient solution approaches for these optimization problems, which enabled the training of machine learning models. As we review in this paper, the development of these optimization models has largely been concentrated in areas of computer science, statistics, and operations research. However, diverging publication outlets, standards, and terminology persist.

### 1.3 Aim and Scope

The aim of this paper is to present machine learning as optimization problems. For that, in addition to publications in classical operations research journals, this paper surveys machine learning and artificial intelligence conferences and journals, such as the conference on Association for the Advancement of Artificial Intelligence and the International Conference on Machine Learning. Furthermore, since machine learning research has rapidly accelerated with many important papers still in the review process, this paper also surveys a considerable number of relevant papers that are available on the arXiv repository. This paper also complements the recent surveys of $[43,77,221]$ which described methodological developments for solving machine learning optimization problems; $[21,158]$ which discussed how machine learning advanced the solution approaches of mathematical programming; $[71,178]$ which described the interactions between operations research and data mining; [25] which surveyed solution approaches to machine learning models cast as continuous optimization problems; and [199] which provided an overview on the various levels of interaction between optimization and machine learning.

This paper presents optimization models for regression, classification, clustering, and deep learning (including adversarial attacks), as well as new emerging paradigms such as machine teaching and empirical model learning. Additionally, this paper highlights the strengths and the shortcomings of the models from a mathematical optimization perspective and discusses potential novel research directions. This is to foster efforts in mathematical programming for machine learning. While important criteria for contributions in operations research are the convergence guarantees, deviation to optimality and speed increments with respect to benchmarks, machine learning applications have a partly different set of goals, such as scalability, reasonable execution time and memory requirement, robustness and numerical stability and, most importantly, general-

ization [25]. It is therefore common for mathematical programming approaches to sacrifice optimality (local or global) and convergence guarantees to obtain better generalization properties, by adopting strategies such as early stopping [184].

Following this introductory section, regression models are discussed in Section 2 while classification and clustering models are presented in Sections 3 and 4, respectively. Linear dimension reduction methods are reviewed in Section 5. Deep learning models are presented in Section 6, while models for adversarial learning are discussed in Section 7. New emerging paradigms that include machine teaching and empirical model learning are presented in Section 8. Finally, conclusions are drawn in Section 9.

# 2 Regression Models 

### 2.1 Linear Regression

Since the early era of statistics, linear regression models have been widely adopted in supervised learning for predicting a quantitative response. The central assumption is that the relationship between the dependent variables (feature measurements, or predictors, or input vector) and the independent variable (real-valued output, or response) is representable with a linear function (regression function) with a reasonable accuracy. Linear regression models preserve considerable interest, given their simplicity, their extensive range of applications, and the ease of interpretability. In particular, machine learning interpretability, in its simplest form, is the ability to explain in a humanly understandable way the role of the inputs in the outcome [86].

Linear regression aims to find a linear function $f$ that expresses the relation between an input vector $x$ of dimension $p$ and a real-valued output $f(x)$ such as

$$
f(x)=\beta_{0}+x^{\top} \beta
$$

where $\beta_{0} \in \mathbb{R}$ is the intercept of the regression line and $\beta \in \mathbb{R}^{p}$ is the vector of coefficients corresponding to each of the input variables. In order to estimate the regression parameters $\beta_{0}$ and $\beta$, one needs a training set $(X, y)$ where $X \in \mathbb{R}^{n \times p}$ denotes $n$ training inputs $x_{1}, \ldots, x_{n}$ and $y$ denotes $n$ training outputs where each $x_{i} \in \mathbb{R}^{p}$ is associated with the real-valued output $y_{i}$. The objective is to minimize the empirical risk (1), in order to quantify via $\beta_{j}$ the association between predictor $X_{j}$ and the response, for each $j=1, \ldots, p$.

The most commonly used loss function for regression is the least squared estimate, where fitting a regression model reduces to minimizing the residual sum of squares (RSS) between the labels and the predicted outputs, such as

$$
\operatorname{RSS}(\beta)=\sum_{i=1}^{n}\left(y_{i}-\beta_{0}-\sum_{j=1}^{p} x_{i j} \beta_{j}\right)^{2}
$$

The least squares estimate is known to have the smallest variance among all linear unbiased estimates, and has a closed form solution. However, this choice is not always ideal for fitting, since it can yield a model with low prediction accuracy, due to a large variance, and often leads to a large number of non-zero regression coefficients (i.e., low interpretability). Shrinkage methods discussed in Section 2.2 and Linear Dimension Reduction discussed in Section 5 are alternatives to the least squared estimate. Forward or backward elimination are also commonly used approaches to perform variable selection and to avoid overfitting [99].

The process of gathering input data is often affected by noise, which can impact the accuracy of statistical learning methods. A model that takes into account the noise in the features of linear regression problems is presented in [27], which also investigates the relationship between regularization and robustness to noise. The noise is assumed to vary in an uncertainty set $\mathcal{U} \in \mathbb{R}^{n \times p}$, and the learner adopts the robust perspective:

$$
\min _{\beta_{0}, \beta} \max _{\Delta \in \mathcal{U}} g\left(y-\beta_{0}-(X+\Delta) \beta\right)
$$

where $g$ is a convex function that measures the residuals (e.g., a norm function). The characterization of the uncertainty set $\mathcal{U}$ directly influences the complexity of problem (4).

The design of high-quality linear regression models requires several desirable properties, which are often conflicting and not simultaneously implementable. A fitting procedure based on Mixed Integer Quadratic Programming (MIQP) is presented in [31] and takes into account sparsity, joint inclusion of subset of features (called selective sparsity), robustness to noisy data, stability against outliers, modeler expertise, statistical significance, and low global multicollinearity. Mixed Integer Programming (MIP) models for regression and

classification are also investigated in [33]. The regression problem is modeled as an assignment of data points to groups with the same regression coefficients.

In order to speed up the fitting procedure and improve the interpretability of the regression model, irrelevant variables can be excluded via feature selection strategies. For example, feature selection is desired in case some regression variables are highly correlated. Multicollinearity can be detected by the condition number of the correlation matrix or the variance influence factor (VIF) [61]. To achieve feature selection in this case, [202] introduces a mixed integer semidefinite programming formulation to eliminate multicollinearity by bounding the condition number. The approach requires to solve a single optimization problem, in contrast with the cutting plane algorithm of [31]. Alternatively, [203] proposes a mixed integer quadratic optimization formulation with an upper bound on VIF, which is a better-grounded statistical indicator for multicollinearity with respect to the condition number.

# 2.2 Shrinkage methods 

Shrinkage methods (also called regularization methods) seek to diminish the value of the regression coefficients. The aim is to obtain a more interpretable model (with less relevant features), at the price of introducing some bias in the model determination. A well-known shrinkage method is Ridge regression, where a 2 -norm penalization on the regression coefficients is added to the loss function such that

$$
\mathcal{L}_{\text {ridge }}\left(\beta_{0}, \beta\right)=\sum_{i=1}^{n}\left(y_{i}-\beta_{0}-\sum_{j=1}^{p} x_{i j} \beta_{j}\right)^{2}+\lambda \sum_{j=1}^{p} \beta_{j}^{2}
$$

where $\lambda$ controls the magnitude of shrinkage.

Another technique for regularization in regression is the lasso regression, which penalizes the 1-norm of the regression coefficients, and seeks to minimize the quantity

$$
\mathcal{L}_{\text {lasso }}\left(\beta_{0}, \beta\right)=\sum_{i=1}^{n}\left(y_{i}-\beta_{0}-\sum_{j=1}^{p} x_{i j} \beta_{j}\right)^{2}+\lambda \sum_{j=1}^{p}\left|\beta_{j}\right|
$$

When $\lambda$ is sufficiently large, the 1 -norm penalty forces some of the coefficient estimates to be exactly equal to zero, hence the models produced by the lasso are more interpretable than those obtained via Ridge regression.

Ridge and lasso regression belong to a class of techniques to achieve sparse regression. As discussed in $[32,34]$, sparse regression can be formulated as the best subset selection problem [167]

$$
\begin{aligned}
& \min \frac{1}{2}\left\|y-\beta_{0}-X \beta\right\|_{2}^{2} \\
& \text { s.t }\|\beta\|_{0} \leq k \\
& \quad \beta_{0} \in \mathbb{R}, \beta \in \mathbb{R}^{p}
\end{aligned}
$$

where $k$ is an upper bound on the number of predictors with a non-zero regression coefficient, i.e., the predictors to select, and $\|\beta\|_{0}$ is the number of non-zero entries of $\beta$, which is commonly referred to as the " 0 -norm" (though is not technically a norm as it does not satisfy the homogeneity property). Problem (7)-(9) is $\mathcal{N} \mathcal{P}$ hard, as proven in [174]. The recent work of [32] demonstrated that the best subset selection can be solved to near-optimal solutions using optimization techniques for values of $p$ in the hundreds or thousands. Specifically, by introducing the binary variables $s \in\{0,1\}^{p}$, the sparse regression problem can be transformed into the MIQP formulation

$$
\begin{aligned}
& \min \frac{1}{2}\left\|y-\beta_{0}-X \beta\right\|_{2}^{2} \\
& \text { s.t }-M s_{j} \leq \beta_{j} \leq M s_{j} \quad \forall j=1, \ldots, p \\
& \quad \sum_{j=1}^{p} s_{j} \leq k \\
& \quad \beta_{0} \in \mathbb{R}, \beta \in \mathbb{R}^{p} \\
& \quad s \in\{0,1\}^{p}
\end{aligned}
$$

where $M$ is a large constant, $M \geq\|\beta\|_{\infty}$. Since the choice of the data dependent constant $M$ largely affects the strength of the MIQP formulation, alternative formulations based on Specially Ordered Sets Type I can be devised [70].

As discussed in [120], the prediction accuracy of best subset selection is however highly dependent on the noise present in the input dataset, and it is not possible to establish a dominance relationship over lasso regression and forward stepwise selection [91]. In order to limit the effect of noise in the input data, make the model more robust, and to avoid numerical issues, [34] introduces the Tikhonov regularization term $\frac{1}{2 \Lambda}\|\beta\|_{2}^{2}$ with weight $\Lambda>0$ into the objective function of problem (10)-(14), which is then solved using a cutting plane approach.

The task of finding a linear model to express the relationship between regressors and output is a particular case of selecting the hyperplane that minimizes a measure of the deviation of the data with respect to the induced linear form. As presented in [37], locating a hyperplane $\beta_{0}+x^{T} \beta=0, \beta_{0} \in \mathbb{R}, \beta \in \mathbb{R}^{p}$ to fit a set of points $x_{i} \in \mathbb{R}^{p}, i=1, \ldots, n$, consists of finding $\hat{\beta}_{0}, \hat{\beta} \in \arg \min _{\beta_{0}, \beta} \phi\left(\epsilon\left(\beta_{0}, \beta\right)\right)$, where $\epsilon\left(\beta_{0}, \beta\right)=\epsilon_{\left\{x_{1}, \ldots, x_{n}\right\}}\left(\beta_{0}, \beta\right)$ is a mapping to the residuals of the points on the hyperplane (according to a distance measure in $\mathbb{R}^{p}$ ), and $\phi$ is an aggregation function on the residuals (e.g., residual sum of squares, least absolute deviation [89]). If the number of points $n$ is much smaller than the dimension $p$ of the space, feature selection strategies can be applied $[32,169]$. We note that hyperplane fitting is a variant of facility location problems [84, 192].

# 2.3 Regression Models Beyond Linearity 

A natural extension of linear regression models is to consider nonlinear terms, which may capture complex relationships between regressors and predictors. Nonlinear regression models include, among others, polynomial regression, exponential regression, step functions, regression splines, smoothing splines and local regression [99, 129]. Alternatively, the Generalized Additive Models (GAMs) [119] maintain the additivity of the original predictors $X_{1}, \ldots, X_{p}$ and the relationship between each feature and the response $y$ is expressed using nonlinear functions $f_{j}\left(X_{j}\right)$ such as

$$
y=\beta_{0}+\sum_{j=1}^{p} f_{j}\left(X_{j}\right)
$$

GAMs may increase the flexibility and accuracy of the predictions with respect to linear models, while maintaining a certain level of interpretability of the predictors. However, one limitation is given by the assumption of additivity of the features. To further increase the model flexibility, one could include predictors of the form $X_{i} \times X_{j}$, or consider non-parametric models, such as random forests and boosting. It has been empirically observed that GAMs do not represent well problems where the number of observations is much larger than the number of predictors. In [204] the Generalized Additive Model Selection is introduced to fit sparse GAMs in high dimension with a penalized likelihood approach. The penalty term is derived from the fitting criterion for smoothing splines. Alternatively, [68] proposes to fit a constrained version of GAMs by solving a conic programming problem.

As an intermediate model between linear and nonlinear relationships, compact and simple representations via piecewise affine models have been discussed in [137]. Piecewise affine forms emerge as candidate models when the fitting function is known to be discontinuous [94], separable [81], or approximate to complex nonlinear expressions [80, 187, 213]. Fitting piecewise affine models involves partitioning the domain $D$ of the input data into $K$ subdomains $D_{i}, i=1, \ldots, K$, and fitting for each subdomain an affine function $f_{i}: D_{i} \rightarrow \mathbb{R}$, in order to minimize a measure of the overall fitting error. To facilitate the fitting procedure, the domain is partitioned a priori (see $K$-hyperplane clustering in Section 4.3). Neglecting domain partitioning may lead to large fitting errors. In contrast, [5] considers both aspects in determining piecewise affine models for piecewise linearly separable subdomains via a mixed integer linear programming formulation and a tailored heuristic. Mixed integer models are also proposed in [207], however a partial knowledge of the subdomains is required. Alternatively, clustering techniques can be adopted for domain partitioning [94].

## 3 Classification

The task of classifying data is to decide the class membership of an unlabeled data item $x$ based on the training dataset $(X, y)$ where each $x_{i}$ has a known class membership $y_{i}$. A recent comparison of machine learning techniques for binary classification is found in [18]. This section reviews the common binary and

multiclass classification approaches that include logistic regression, linear discriminant analysis, decision trees, and support vector machines.

# 3.1 Logistic Regression 

In most problem domains, there is no functional relationship $y=f(x)$ between $y$ and $x$. In this case, the relationship between $x$ and $y$ has to be described more generally by a probability distribution $P(x, y)$ while assuming that the training contains independent samples from $P$. In this section, the label $y$ is assumed to be binary, i.e., $y \in\{0,1\}$. The optimal class membership decision is to choose the class label $y$ that maximizes the posterior distribution $P(y \mid x)$. Logistic regression calculates the class membership probability for one of the two categories in the dataset as

$$
\begin{aligned}
& P\left(y=1 \mid x, \beta_{0}, \beta\right)=h\left(x, \beta_{0}, \beta\right)=\frac{1}{1+e^{-\left(\beta_{0}+\beta^{\top} x\right)}} \\
& P\left(y=0 \mid x, \beta_{0}, \beta\right)=1-h\left(x, \beta_{0}, \beta\right)
\end{aligned}
$$

The decision boundary between the two binary classes is formed by a hyperplane whose equation is $\beta_{0}+\beta^{\top} x=0$. Points at this decision boundary have $P\left(1 \mid x, \beta_{0}, \beta\right)=P\left(0 \mid x, \beta_{0}, \beta\right)=0.5$. The parameters $\beta_{0}$ and $\beta$ are usually obtained by maximum-likelihood estimation [87]

$$
\max \Pi_{i=1}^{n} P\left(y_{i} \mid x_{i}, \beta_{0}, \beta\right)=\max \Pi_{i=1}^{n}\left(h\left(x_{i}, \beta_{0}, \beta\right)\right)^{y_{i}}\left(1-h\left(x_{i}, \beta_{0}, \beta\right)\right)^{1-y_{i}}
$$

which is equivalent to

$$
\min -\sum_{i=1}^{n}\left(y_{i} \log h\left(x_{i}, \beta_{0}, \beta\right)+\left(1-y_{i}\right) \log \left(1-h\left(x_{i}, \beta_{0}, \beta\right)\right)\right)
$$

Problem (16) is convex and differentiable and first order methods such as gradient descent as well as second order methods such as Newton's method can be applied to find a global optimal solution.

To tune the logistic regression model and to avoid overfitting, variable selection can be performed where only the most relevant subsets of the $x$ variables are kept in the model [99]. Heuristic approaches such as forward selection or backward elimination can be applied to add or remove variables respectively, based on the statistical significance of each of the computed coefficients. Interaction terms can be also added to further complicate the model at the risk of overfitting the training data.

### 3.2 Linear Discriminant Analysis

Linear discriminant analysis (LDA) is an approach for classification and dimensionality reduction. It is often applied to data that contains a large number of features (such as image data) where reducing the number of features is necessary to obtain robust classification. While LDA and Principal Component Analysis (PCA) (see Section 5.1) share the commonality of dimensionality reduction, LDA tends to be more robust than PCA since it takes into account the data labels in computing the optimal projection matrix [19].

Given the dataset $(X, y)$ where each data sample $x_{i} \in \mathbb{R}^{p}$ belongs to one of $K$ classes such that if $x_{i}$ belongs to the $k$-th class then $y_{i}(k)$ is 1 where $y_{i} \in\{0,1\}^{K}$, the input data is partitioned into $K$ groups $\left\{\pi_{k}\right\}_{k=1}^{K}$ where $\pi_{k}$ denotes the sample set of the $k$-th class which contains $n_{k}$ data points. LDA maps the features space $x_{i} \in \mathbb{R}^{p}$ to a lower dimensional space $q_{i} \in \mathbb{R}^{r}(r<p)$ through a linear transformation $q_{i}=G^{\top} x_{i}$ [216]. The class mean of the $k$-th class is given by $\mu_{k}=\frac{1}{n_{k}} \sum_{x_{i} \in \pi_{k}} x_{i}$ while the global mean in given by $\mu=\frac{1}{n} \sum_{i=1}^{n} x_{i}$. In the projected space the class mean is given by $\bar{\mu}_{k}=\frac{1}{n_{k}} \sum_{q_{i} \in \pi_{k}} q_{i}$ while the global mean in given by $\bar{\mu}=\frac{1}{n} \sum_{i=1}^{n} q_{i}$.

The within-class scatter and the between-class scatter evaluate the class separability and are defined as $S_{w}$ and $S_{b}$ respectively such that

$$
\begin{aligned}
S_{w} & =\sum_{k=1}^{K} \sum_{x_{i} \in \pi_{k}}\left(x_{i}-\mu_{k}\right)\left(x_{i}-\mu_{k}\right)^{\top} \\
S_{b} & =\sum_{k=1}^{K} n_{k}\left(\mu_{k}-\mu\right)\left(\mu_{k}-\mu\right)^{\top}
\end{aligned}
$$

The within-class scatter evaluates the spread of the data around the class mean while the between-class scatter evaluates the spread of the class means around the global mean. For the projected data, the within-class and the between-class scatters are defined as $\bar{S}_{w}$ and $\bar{S}_{b}$ respectively such that

$$
\begin{aligned}
& \bar{S}_{w}=\sum_{k=1}^{K} \sum_{q_{i} \in \pi_{k}}\left(q_{i}-\bar{\mu}_{k}\right)\left(q_{i}-\bar{\mu}_{k}\right)^{\top}=G^{\top} S_{w} G \\
& \bar{S}_{b}=\sum_{k=1}^{K} n_{k}\left(\bar{\mu}_{k}-\bar{\mu}\right)\left(\bar{\mu}_{k}-\bar{\mu}\right)^{\top}=G^{\top} S_{b} G
\end{aligned}
$$

The LDA optimization problem is bi-objective where the within-class scatter should be minimized while the between-class scatter should be maximized. The optimal transformation $G$ can be obtained by maximizing the Fisher criterion (the ratio of between-class to within-class scatters)

$$
\max \frac{\left|G^{T} S_{b} G\right|}{\left|G^{T} S_{w} G\right|}
$$

Note that since the between-class and the within-class scatters are not scalar, the determinant is used to obtain a scalar objective function. As discussed in [100], assuming that $S_{w}$ is invertible and non-singular, the Fisher criterion is optimized by selecting the $r$ largest eigenvalues of $S_{w}^{-1} S_{b}$ and the corresponding eigen vectors $G_{1}^{*}, G_{2}^{*}, \ldots, G_{r}^{*}$ form the optimal transformation matrix $G^{*}=\left[G_{1}^{*}\left|G_{2}^{*}\right| \ldots \mid G_{r}^{*}\right]$. Instead of using Fisher criterion, bi-objective optimization techniques may also potentially be used to formulate and solve the LDA optimization problem exactly.

An alternative formulation of the LDA optimization problem is provided in [63] by maximizing the minimum distance between each class center and the total class center. The proposed approach known as the large margin linear discriminant analysis requires the solution of non-convex optimization problems. A solution approach is also proposed based on solving a series of convex quadratic optimization problems.

# 3.3 Decision Trees 

Decision trees are classical models for making a decision or classification using splitting rules organized into a tree data structure. Tree-based methods are non-parametric models that partition the predictor space into sub-regions and then yield a prediction based on statistical indicators (e.g., median and mode) of the segmented training data. Decision trees can be used for both regression and classification problems.

For regression trees, the splitting of the training dataset into distinct and non-overlapping regions can be done using a top-down recursive binary splitting procedure. Starting from a root node that contains the full dataset, a cut that splits the data into distinct sets is identified. For the case of a univariate cut (i.e., involving only a single feature), the cutpoint $b$ for feature $j$ is the one that leads to the two splitted regions $R_{1}=\left\{x_{i} \mid x_{i j}<b\right\}$ and $R_{2}=\left\{x_{i} \mid x_{i j} \geq b\right\}$ that have the greatest possible reduction in the residual sum of squares $\sum_{i: x_{i} \in R_{1}(j, b)}\left(y_{i}-\hat{y}_{R_{1}}\right)^{2}+\sum_{i: x_{i} \in R_{2}(j, b)}\left(y_{i}-\hat{y}_{R_{2}}\right)^{2}$, where $\hat{y}_{R}$ denotes the mean response for the training observations in region $R$. A multivariate split is of the form $a^{T} x_{i}<b$, where $a$ is a vector. Another optimization criterion is the measure of purity [45] such as Gini's index in classification problems. For classification problems, [45] highlights that, given their greedy nature, the classical methods based on recursive splitting do not lead to the global optimality of the decision tree. Since building optimal binary decision trees is known to be $\mathcal{N} \mathcal{P}$-hard [124], heuristic approaches based on mathematical programming paradigms, such as linear optimization [22], continuous optimization [23], and dynamic programming [9, 11, 75, 181], have been proposed.

To find provably optimal decision trees, [28] proposes a mixed integer programming formulation that has an exponential complexity in the depth of the tree. Given a fixed depth $D$, the maximum number of nodes is $T=2^{D+1}-1$ indexed by $t=1, \ldots, T$. Following the notation of [28], the nodes are split into two sets, branch nodes and leaf nodes. The branch nodes $T_{B}=\left\{1, \ldots,\left\lfloor\frac{T}{2}\right\rfloor\right\}$ apply a linear split $a^{\top} x_{i}<b$ where the left child node includes the data points that satisfy this split while the right one includes the remaining data. In [28], the splits that are applied at the branch nodes are restricted to a single variable with the option of not splitting a node. The binary decision variable $d_{t}$ takes a value of 1 if branch node $t$ is split and 0 otherwise. Since the splits are univariate, then variable $a_{j t}$, which denotes the value of the coefficient of feature $j$ in the split at node $t$, is also binary. The cutpoint at node $t$ is $b_{t} \geq 0$.

At each of the leaf nodes $T_{L}=\left\{\left\lfloor\frac{T}{2}\right\rfloor+1, \ldots, T\right\}$, a class prediction is made based on the data points that are included. The binary variable $z_{i t}$ indicates if data point $i$ is included to leaf node $t$, i.e., $z_{i t}=1$ or otherwise $z_{i t}=0$. The binary decision variable $c_{k t}$ takes a value of 1 if leaf node $t$ is assigned label $k$, and 0 otherwise while binary variable $l_{t}$ indicates if leaf node $t$ is used, i.e., $l_{t}=1$ or otherwise $l_{t}=0$.

The mixed integer programming formulation is

$$
\begin{aligned}
& \min \frac{1}{L} \sum_{t \in T_{L}} L_{t}+\alpha \sum_{t \in T_{B}} d_{t} \\
& \text { s.t. } L_{t} \geq N_{t}-N_{k t}-n\left(1-c_{k t}\right), \quad \forall k=1, \ldots, K, t \in T_{L} \\
& 0 \leq L_{t} \leq N_{t}-N_{k t}+n c_{k t} \quad \forall k=1, \ldots, K, t \in T_{L} \\
& N_{k t}=\frac{1}{2} \sum_{i=1}^{n}\left(1+Y_{i k}\right) z_{i t}, \quad \forall k=1, \ldots, K, t \in T_{L} \\
& N_{t}=\sum_{i=1}^{n} z_{i t} \quad \forall t \in T_{L} \\
& \sum_{k=1}^{K} c_{k t}=l_{t} \quad \forall t \in T_{L} \\
& \sum_{t \in T_{L}} z_{i t}=1 \quad \forall i=1, \ldots, n \\
& z_{i t} \leq l_{t} \quad \forall i=1, \ldots, n, t \in T_{L} \\
& \sum_{i=1}^{n} z_{i t} \geq N_{\min } l_{t} \quad \forall t \in T_{L} \\
& a_{m}^{\top}\left(x_{i}+\epsilon\right) \leq b_{m}+\left(1+\epsilon_{\max }\right)\left(1-z_{i t}\right) \quad \forall i=1, \ldots, n, t \in T_{L}, m \in A_{L}(t) \\
& a_{m}^{\top} x_{i} \geq b_{m}-\left(1-z_{i t}\right) \quad \forall i=1, \ldots, n, t \in T_{L}, \forall m \in A_{R}(t) \\
& \sum_{j=1}^{p} a_{j t}=d_{t} \quad \forall t \in T_{B} \\
& 0 \leq b_{t} \leq d_{t} \quad \forall t \in T_{B} \\
& d_{t} \leq d_{p(t)} \quad \forall t \in T_{B} \backslash\{1\} \\
& z_{i t}, l_{t} \in\{0,1\} \quad \forall i=1, \ldots, n, \forall t \in T_{L} \\
& c_{k t} \in\{0,1\} \quad \forall k=1, \ldots, K, t \in T_{L} \\
& a_{j t}, d_{t} \in\{0,1\} \quad \forall j=1, \ldots, p, t \in T_{B}
\end{aligned}
$$

The objective function (22) minimizes the normalized total misclassification loss $\frac{1}{L} \sum_{t \in T_{L}} L_{t}$ and the decision tree complexity which is given by $\sum_{t \in T_{B}} d_{t}$, the total number of nodes that are split. $\alpha$ is a tuning parameter and $\hat{L}$ is the baseline loss obtained by predicting the most popular class from the entire dataset. Constraints (23)-(24) set the misclassification loss $L_{t}$ at leaf node $t$ as $L_{t}=N_{t}-N_{k t}$ if node $t$ is assigned label $k$ (i.e $c_{k t}=1$ ), where $N_{t}$ is the total number of data points at leaf node $t$ and $N_{k t}$ is the total number of data points at node $t$ whose true labels are $k$. The counting of $N_{k t}$ and $N_{t}$ is enforced by (25) and (26), respectively, where $Y_{i k}$ is a parameter taking the value of 1 if data point $i$ has a label $k$ and -1 otherwise. Constraints (27) indicate that each leaf node that is used (i.e., $l_{t}=1$ ) should be assigned to a label $k=1 \ldots K$. Constraints (28) indicate that each data point should be assigned to exactly one leaf node. Constraints (29)-(30) indicate that data points can be assigned to a node only if that node is used and if a node is used then at least $N_{\min }$ data points should be assigned to it. The splitting of the data points at each of the branch nodes is enforced by constraints (31)-(32) where $A_{L}(t)$ is the set of ancestors of $t$ whose left branch has been followed on the path from the root node to node $t$. Similarly, $A_{R}(t)$ is the set of ancestors of $t$ whose right branch has been followed on the path from the root node to node $t . \epsilon$ and $\epsilon_{\max }$ are small numbers to enforce the strict split $a^{\top} x<b$ at the left branch (see [28] for finding good values for $\epsilon$ and $\epsilon_{\max }$ ). Constraints (33)-(34) indicate that the splits are restricted to a single variable with the option of not splitting a node $\left(d_{t}=0\right)$. As enforced by constraints (35), if $p(t)$, the parent of node $t$, does not apply a split then so is node $t$. Finally constraints (36)-(38) set the binary conditions.

An alternative formulation to the optimal decision tree problem is provided in [114]. The main difference between the formulation of [114] and [28] is that the approach of [114] is specialized to the case where the features take categorical values. By exploiting the combinatorial structure that is present in the case of categorical variables, [114] provides a strong formulation of the optimal decision tree problem thus improving the computational performance. Furthermore the formulation of [114] is restricted to binary classification and the tree topology is fixed, which lowers the required computational effort for solving the optimization problem to optimality. A commonality between the models presented in [28] and [114] is that the split that is considered at each node of the decision tree involves only one variable mainly to achieve better computational performance when solving the optimization model. More generally, splits that span multiple variables can also be considered at each node as presented in [38, 211, 212]. The approach of [38], which is extended in [39] to account for sparsity by using regularization, is based on a nonlinear continuous optimization formulation to learn decision trees with general splits.

While single decision tree models are often preferred by data analysts for their high interpretability, the model accuracy can be largely improved by taking multiple decision trees into account. Such approaches include bagging, random forests, and boosting. Bagging creates multiple decision trees by obtaining several training subsets by randomly choosing with replacement data points from the training set and subsequently training a decision tree for each subset. Random forests create training subsets similar to bagging with the addition of randomly selecting a subset of features for training each tree. Boosting iteratively creates decision trees where a weight on the training data is set and is increased at each iteration for the misclassified data points so as to subsequently create a decision tree that is more likely to correctly classify previously misclassified data. These models that make predictions based on aggregating the predictions of individual trees are also known as tree ensemble. A mixed integer optimization model for tree ensemble has been recently proposed in [168].

Decision trees can also be used in a more general range of applications as algorithms for problem solving, data mining, and knowledge representation. In [10], several greedy and dynamic programming approaches are compared for building decision trees on datasets with inconsistent labels (i.e, many-valued decision approach). Many-valued decisions can be evaluated in terms of multiple cost functions in a multi-stage optimization [12]. Recently, [67] investigated conflicting objectives in the construction of decision trees by means of bi-criteria optimization. Since the single objectives, such as minimizing average depth or the number of terminal nodes, are known to be $\mathcal{N} \mathcal{P}$-hard, the authors propose a bi-criteria optimization approach by means of dynamic programming.

# 3.4 Support Vector Machines 

Support vector machines (SVMs) are another class of supervised machine learning algorithms that are based on statistical learning and have received significant attention in the optimization literature [59, 209, 210]. Given a training set $(X, y)$ with $n$ training inputs where $X \in \mathbb{R}^{n \times p}$ and binary response variables $y \in\{-1,1\}^{n}$, the objective of the support vector machine problem is to identify a hyperplane $w^{\top} x+\gamma=0$, where $w \in \mathbb{R}^{p}$ and $\gamma \in \mathbb{R}$, which separates the two classes of data points with a maximal separation margin measured as the width of the band that separates the two classes. In this section, $w$ denotes the vector of coefficients corresponding to each of the input variables and $\gamma$ is the intercept of the separating hyperplane. As detailed next, the underlying optimization problem is a linearly constrained convex quadratic optimization problem.

### 3.4.1 Hard Margin SVM

The most basic version of SVMs is the hard margin SVM that assumes that there exists a hyperplane that geometrically separates the data points into the two classes such that no data point is misclassified [73]. The training of the SVM model involves finding the hyperplane that separates the data and whose distance to the closest data point in either of the classes, i.e., margin, is maximized.

The distance of a particular data point $x_{i}$ to the separating hyperplane is

$$
\frac{y_{i}\left(w^{\top} x_{i}+\gamma\right)}{\|w\|_{2}}
$$

The distance to the closest data point is normalized to $\frac{1}{\|w\|_{2}}$ where $\|w\|_{2}$ denotes the 2 -norm. Thus the data points with labels $y=-1$ are on one side of the hyperplane such that $w^{\top} x+\gamma \leq 1$ while the data point with labels $y=1$ are on the other side $w^{\top} x+\gamma \geq 1$. The optimization problem for finding the separating

hyperplane is then

$$
\begin{aligned}
& \max \frac{1}{\|w\|_{2}} \\
& \text { s.t. } y_{i}\left(w^{\top} x_{i}+\gamma\right) \geq 1 \quad \forall i=1, \ldots, n \\
& w \in \mathbb{R}^{p}, \gamma \in \mathbb{R}
\end{aligned}
$$

which is equivalent to

$$
\begin{aligned}
& \min \|w\|_{2}^{2} \\
& \text { s.t. } y_{i}\left(w^{\top} x_{i}+\gamma\right) \geq 1 \quad \forall i=1, \ldots, n \\
& w \in \mathbb{R}^{p}, \gamma \in \mathbb{R}
\end{aligned}
$$

that is a convex quadratic problem.
Forcing the data to be separable by a linear hyperplane is a strong condition that often does not hold in practice. Thus, the soft-margin SVM, which relaxes the condition of perfect separability, is used instead.

# 3.4.2 Soft-Margin SVM 

When the data is not linearly separable, problem (39)-(41) is infeasible. Alternatively, [24] proposed a linear program that minimizes a weighted average of the errors given by the points lying on the wrong side of the separator. This work was then extended in [73] which presented the soft margin SVM. The soft margin SVM introduces slack variables $\xi_{i} \geq 0$ into constraints (40) which are then penalized in the objective function as a proxy to minimizing the number of data points that are on the wrong side. The soft-margin SVM optimization problem is

$$
\begin{aligned}
& \min \|w\|_{2}^{2}+C \sum_{i=1}^{n} \xi_{i} \\
& \text { s.t. } y_{i}\left(w^{\top} x_{i}+\gamma\right) \geq 1-\xi_{i} \quad \forall i=1, \ldots, n \\
& w \in \mathbb{R}^{p}, \gamma \in \mathbb{R} \\
& \xi_{i} \geq 0 \quad \forall i=1, \ldots, n
\end{aligned}
$$

Another common alternative is to include the error term $\xi_{i}$ in the objective function by using the squared hinge loss $\sum_{i}^{n} \xi_{i}^{2}$ instead of the hinge loss $\sum_{i}^{n} \xi_{i}$. The hinge loss function takes a value of zero for a data point that is correctly classified while it takes a positive value that is proportional to the distance from the separating hyperplane for a misclassified data point. Hyperparameter $C$ is then tuned to obtain the best classifier.

Besides the direct solution of problem (42)-(45) as a convex quadratic problem, replacing the 2 -norm by the 1 -norm leads to a linear optimization problem generally at the expense of higher misclassification rate [44].

### 3.4.3 Sparse SVM

Using the 1-norm is also an approach to sparsify $w$, i.e., reduce the number of features that are involved in the classification model [44, 224]. An approach known as the elastic net includes both the 1-norm and the 2-norm in the objective function and tunes the bias towards one of the norms through a hyperparameter [217, 228]. Several other approaches for dealing with sparsity in SVM have been proposed in $[8,88,103,105,115,164,183]$. The number of features can be explicitly modeled in (42)-(45) by using binary variables $z \in\{0,1\}^{p}$ where $z_{j}=1$ indicates that feature $j$ is selected and otherwise $z_{j}=0$ [60]. A constraint limiting the number of features to a maximum desired number can be enforced resulting in the following mixed integer quadratic problem

$$
\begin{aligned}
& \min \|w\|_{2}^{2}+C \sum_{i=1}^{n} \xi_{i} \\
& \text { s.t. } y_{i}\left(w^{\top} x_{i}+\gamma\right) \geq 1-\xi_{i} \quad \forall i=1, \ldots, n \\
& \quad-M z_{j} \leq w_{j} \leq M z_{j} \quad \forall j=1, \ldots, p \\
& \quad \sum_{j=1}^{p} z_{j} \leq r
\end{aligned}
$$

$$
\begin{aligned}
& w \in \mathbb{R}^{p}, \gamma \in \mathbb{R} \\
& z_{j} \in\{0,1\} \quad \forall j=1, \ldots, p \\
& \xi_{i} \geq 0 \quad \forall i=1, \ldots, n
\end{aligned}
$$

Constraints (48) force $z_{j}=1$ when feature $j$ is used, i.e., $w_{j} \neq 0$ ( $M$ denotes a sufficiently large number). Constraints (49) set a limit $r$ on the maximum number of features that can be used.

# 3.4.4 The Dual Problem and Kernel Tricks 

The data points can be mapped to a higher dimensional space through a mapping function $\phi(x)$. A soft margin SVM can then be applied such that

$$
\begin{aligned}
& \min \|w\|_{2}^{2}+C \sum_{i=1}^{n} \xi_{i} \\
& \text { s.t. } y_{i}\left(w^{\top} \phi\left(x_{i}\right)+\gamma\right) \geq 1-\xi_{i} \quad \forall i=1, \ldots, n \\
& w \in \mathbb{R}^{p}, \gamma \in \mathbb{R} \\
& \xi_{i} \geq 0 \quad \forall i=1, \ldots, n
\end{aligned}
$$

Through this mapping, the data has a linear classifier in the higher dimensional space however a nonlinear separation function is obtained in the original space.

To solve problem (53)-(56), the following dual problem is first obtained

$$
\begin{gathered}
\max _{\alpha} \sum_{i=1}^{n} \alpha_{i}-\frac{1}{2} \sum_{i, j=1}^{n} \alpha_{i} \alpha_{j} y_{i} y_{j} \phi\left(x_{i}\right)^{\top} \phi\left(x_{j}\right) \\
\text { s.t. } \sum_{i=1}^{n} \alpha_{i} y_{i}=0 \quad \forall i=1, \ldots, n \\
0 \leq \alpha_{i} \leq C \quad \forall i=1, \ldots, n
\end{gathered}
$$

where $\alpha_{i}$ are the dual variables of constraints (54). Given a kernel function $K: \mathbb{R}^{m} \times \mathbb{R}^{m} \rightarrow \mathbb{R}$ where $K\left(x_{i}, x_{j}\right)=\phi\left(x_{i}\right)^{\top} \phi\left(x_{j}\right)$, the dual problem is

$$
\begin{gathered}
\max _{\alpha} \sum_{i=1}^{n} \alpha_{i}-\frac{1}{2} \sum_{i, j=1}^{n} \alpha_{i} \alpha_{j} y_{i} y_{j} K\left(x_{i}, x_{j}\right) \\
\text { s.t. } \sum_{i=1}^{n} \alpha_{i} y_{i}=0, \quad \forall i=1, \ldots, n \\
0 \leq \alpha_{i} \leq C, \quad \forall i=1, \ldots, n
\end{gathered}
$$

which is a convex quadratic optimization problem. Thus only the kernel function $K\left(x_{i}, x_{j}\right)$ is required while the explicit mapping $\phi$ is not needed.

Among the commonly used kernel functions is the polynomial $K\left(x_{i}, x_{j}\right)=\left(x_{i}^{\top} x_{j}+c\right)^{d}$ where $c$ controls the trade-off between the higher-order and the lower-order terms in the polynomial and $d$ is the degree of the polynomial. The polynomial kernel models the interaction between the data up to the degree $d$. A high degree polynomial tends to overfit the training data. Another kernel function is the radial basis $K\left(x_{i}, x_{j}\right)=e^{-\frac{\left\|x_{i}-x_{j}\right\|_{2}^{2}}{2}}$ where $\gamma$ acts as a smoothing parameter. A smaller $\gamma$ tends to overfit the training data. The sigmoidal kernel $K\left(x_{i}, x_{j}\right)=\tanh \left(\varphi x_{i}^{\top} x_{j}+c\right)$ is also commonly used where $\varphi$ is a scaling parameter of the input data and $c$ is a shifting parameter that controls the threshold of the mapping. Further details on kernel functions are provided in $[2,59,122]$.

Since the classification in high dimensional space can be difficult to interpret for practitioners, Binarized SVM (BSVM) replaces the continuous predictor variables with a linear combination of binary cutoff variables [56]. BSVM is also extended in [57] to capture the interactions between the relevant variables. Another important practical aspect to consider is data uncertainty. Often the training data suffers from inaccuracies in the labels and in the features that are collected which may negatively affect the performance of the classifiers. While typically regularization is used to mitigate the effect of uncertainty, [29] proposes robust optimization models for logistic regression, decision trees, and support vector machines and shows increased accuracy over regularization, and most importantly without changing the complexity of the classification problem.

# 3.4.5 Support Vector Regression 

Although as discussed earlier, SVM has been introduced for binary classification, its extension to regression, i.e., support vector regression, has received significant interest in the literature [197]. The core idea of support vector regression is to find a linear function $f(x)=w^{\top} x+\gamma$ that can approximate with a tolerance $\epsilon$ a training set $(X, y)$ where $y \in \mathbb{R}[210]$. Such a linear function may however not exist, and thus slack variables $\xi_{i}^{+} \geq 0$ and $\xi_{i}^{-} \geq 0$ denoting positive and negative deviations from the desired tolerance are introduced and minimized similar to the soft-margin SVM. The corresponding optimization problem is

$$
\begin{aligned}
& \min \|w\|_{2}^{2}+C \sum_{i=1}^{n}\left(\xi_{i}^{+}+\xi_{i}^{-}\right) \\
& \text {s.t. } y_{i}-w^{\top} x_{i}-\gamma \leq \epsilon+\xi^{+} \quad \forall i=1, \ldots, n \\
& w^{\top} x_{i}+\gamma-y_{i} \leq \epsilon+\xi^{-} \quad \forall i=1, \ldots, n \\
& w \in \mathbb{R}^{p}, \gamma \in \mathbb{R} \\
& \xi_{i}^{+}, \xi_{i}^{-} \geq 0 \quad \forall i=1, \ldots, n
\end{aligned}
$$

Hyperparameter $C$ is tuned to adjust the weight on the deviation from the tolerance $\epsilon$. This deviation from $\epsilon$ is the $\epsilon$-insensitive loss function $|\xi|_{\epsilon}$ given by

$$
$$

As detailed extensively in [197], kernel tricks can also be applied to (57)-(61) which is solved by formulating the dual problem.

### 3.4.6 Support Vector Ordinal Regression

In situations where the data contains ordering preferences, i.e., the training data is labeled by ranks, where the order of the rankings is relevant while the distances between the ranks is not defined or irrelevant to the training, the purpose of learning is to find a model that maps the preference information.

The application of classic regression models for such type of data requires the transformation of the ordinal ranks to numerical values. However, such approaches often fail in providing robust models as an appropriate function to map the ranks to distances is challenging to find [145]. An alternative is to encode the ordinal ranks into binary classifications at the expense of a large increase in the scale of the problems [118, 121].

An extension of SVM for ordinary data has been proposed in [195] and extended in [69]. Given a training dataset with $r$ ordered categories $\{1, \ldots, r\}$ where $n_{j}$ is the number of data points labeled as order $j$, the support vector ordinal regression finds $r-1$ separating parallel hyperplanes $w^{\top} x+\beta_{j}=0$ where $\beta_{j}$ is the threshold associated with the hyperplane that separates the orders $k \leq j$ from the remaining orders. Thus $x_{i, k}$, the $i^{\text {th }}$ data sample of order $k \leq j$, should have a function value lower than the margin $\beta_{j}-1$ while the data samples with orders $k>j$ should have a function value greater than the margin $\beta_{j}+1$. The errors for violating these conditions are given by $\xi_{i, k j}^{+} \geq 0$ and $\xi_{i, k j}^{-} \geq 0$ respectively. Following [69], the associated SVM formulation is

$$
\begin{aligned}
& \min \|w\|_{2}^{2}+C \sum_{j=1}^{r-1}\left(\sum_{k=1}^{j} \sum_{i=1}^{n_{k}} \xi_{i, k j}^{+}+\sum_{k=j+1}^{r} \sum_{i=1}^{n_{k}} \xi_{i, k j}^{-}\right) \\
& \text { s.t. } w^{\top} x_{i, k}-\beta_{j} \leq-1+\xi_{i, k j}^{+} \quad \forall k=1, \ldots, j, j=1, \ldots, r-1, i=1, \ldots, n_{k} \\
& w^{\top} x_{i, k}-\beta_{j} \geq 1-\xi_{i, k j}^{-} \quad \forall k=j+1, \ldots, r, j=1, \ldots, r-1, i=1, \ldots, n_{k} \\
& w \in \mathbb{R}^{p}, \beta_{j} \in \mathbb{R} \quad \forall j=1, \ldots, r-1 \\
& \xi_{i, k j}^{+} \geq 0 \quad \forall k=1, \ldots, j, j=1, \ldots, r-1, i=1, \ldots, n_{k} \\
& \xi_{i, k j}^{-} \geq 0 \quad \forall k=j+1, \ldots, r, j=1, \ldots, r-1, i=1, \ldots, n_{k}
\end{aligned}
$$

As detailed in [69], kernel tricks can be also applied by considering the dual problem. Finally we note that preference modeling using machine learning has several commonalities with various approaches in multicriteria decision analysis and most notably, robust ordinal regression. We refer the readers to [72] for a detailed comparison between preference learning using machine learning and muti-criteria decision making.

# 4 Clustering 

Data clustering is a class of unsupervised learning approaches that has been widely used, particularly in applications of data mining, pattern recognition, and information retrieval. Given an input $X \in \mathbb{R}^{n \times p}$, which includes $n$ unlabeled observations $x_{1}, \ldots, x_{n}$ with $x_{i} \in \mathbb{R}^{p}$, cluster analysis aims at finding $K$ subsets of $X$, called clusters, which are homogeneous and well separated. Homogeneity indicates the similarity of the observations within the same cluster (typically, by means of a distance metric), while the separability accounts for the differences between entities of different clusters. The two concepts can be measured via several criteria and lead to different types of clustering algorithms (see, e.g., [117]). The number of clusters is typically a tuning parameter to be fixed before determining the clusters. An extensive survey on data clustering analysis is provided in [128].

In case the entities are points in a Euclidean space, the clustering problem is often modeled as a network problem and shares many similarities with classical problems in operations research, such as the $p$-median problem $[20,143,163,173]$. In the following subsections, the commonly used minimum sum-of-squares clustering, the capacitated clustering, and the $K$-hyperplane clustering are discussed.

### 4.1 Minimum Sum-Of-Squares Clustering (a.k.a. $K$-Means Clustering)

Minimum sum-of-squares clustering is one of the most commonly adopted clustering algorithms. It requires to find a number of disjoint clusters for observations $x_{i}, i=1, \ldots, n$, where $x_{i} \in \mathbb{R}^{p}$ such that the distance to cluster centroids is minimized. Given that typically the number of clusters $K$ is a-priori fixed, the problem is also referred to as $K$-means clustering. The decision of the cluster size is typically taken by examining the elbow curve, or similarity indicators, such as silhouette values and Calinski-Harabasz index, or via mathematical programming approaches including the maximization of the modularity of the associated graph [50, 51].

Defining the binary variables

$$
u_{i j}= \begin{cases}1 & \text { if observation } i \text { belongs to cluster } j \\ 0 & \text { otherwise }\end{cases}
$$

and the centroid $\mu_{j} \in \mathbb{R}^{p}$ of each cluster $j$, the problem of minimizing the within-cluster variance is formulated in [3] as the following mixed integer nonlinear program

$$
\begin{aligned}
& \min \sum_{i=1}^{n} \sum_{j=1}^{K} u_{i j}\left\|x_{i}-\mu_{j}\right\|_{2}^{2} \\
& \text { s.t. } \sum_{j=1}^{K} u_{i j}=1 \quad \forall i=1, \ldots, n \\
& \mu_{j} \in \mathbb{R}^{p} \quad \forall j=1, \ldots, K \\
& u_{i j} \in\{0,1\} \quad \forall i=1, \ldots, n, j=1, \ldots, K
\end{aligned}
$$

By introducing the variables $d_{i j}$ which denote the distance of observation $i$ from centroid $j$, the following linearized formulation is obtained

$$
\begin{aligned}
& \min \sum_{i=1}^{n} \sum_{j=1}^{K} d_{i j} \\
& \text { s.t. } \sum_{j=1}^{K} u_{i j}=1, \quad \forall i=1, \ldots, n \\
& \quad d_{i j} \geq\left\|x_{i}-\mu_{j}\right\|_{2}^{2}-M\left(1-u_{i j}\right) \quad \forall i=1, \ldots, n, j=1, \ldots, K \\
& \quad \mu_{j} \in \mathbb{R}^{p} \quad \forall j=1, \ldots, K \\
& \quad u_{i j} \in\{0,1\}, d_{i j} \geq 0 \quad \forall i=1, \ldots, n, j=1, \ldots, K
\end{aligned}
$$

Parameter $M$ is a sufficiently large number. A heuristic solution approach based on the gradient method is proposed for problem (62)-(65) in [13]. Alternatively, a column generation approach for large-scale instances has been proposed in [3] and a bundle approach has been presented in [132].

The case where the space is not Euclidean is considered in [58]. Alternatively, [189] presents the Heterogeneous Clustering Problem (HCP) where the observations to cluster are associated with multiple dissimilarity

matrices. HCP is formulated as a mixed integer quadratically constrained quadratic program. Another variant is presented in [188] where the homogeneity is expressed by the minimization of the maximum diameter $D_{\max }$ of the clusters. The resulting nonconvex bilinear mixed integer program is solved via a graph-theoretic approach based on seed finding.

Many common solution approaches for $K$-means clustering are based on heuristics. A popular method implemented in data science packages (e.g., scikit-learn [182]) is the two-step improvement procedure proposed in [161]. Starting from a sample of $K$ points in set $X$ as initial cluster centers (centroids $\mu_{j}^{0}$ ), at each iteration $k$, the algorithm assigns each point in $X$ to the nearest centroid $\mu_{j}^{k}$ and then computes the centroids $\mu_{j}^{k+1}$ of the new partition. The procedure is guaranteed to decrease the within-cluster variance and it is run until this metric is sufficiently low. Given the dependency of the procedure to the choice of $\mu_{j}^{0}$, typically the clustering is repeated with different initial centroids and the best clusters are selected. Other heuristics relax the assumption to produce exactly $K$ clusters. For instance, [161] merges clusters if their centroids are sufficiently close. Clustering is also used within heuristics for hard combinatorial problems ( $[101,149]$ ), and can be integrated in problems where the evaluation of multiple solutions is important (e.g., Cluster Newton Method [6, 104]). Cluster Newton method approximates the Jacobian in the domain covered by the cluster of points, instead of locally as done by the traditional Newton's Method [136], and this has a regularization effect.

# 4.2 Capacitated Clustering 

The Capacitated Centered Clustering Problem (CCCP) deals with finding a set of clusters with a capacity limitation and homogeneity expressed by the similarity to the cluster centre. Given a set of potential clusters $1, \ldots, K$, a mathematical formulation for CCCP is given in [175] as

$$
\begin{aligned}
\min & \sum_{i=1}^{n} \sum_{j=1}^{K} \underline{s}_{i j} u_{i j} \\
\text { s.t } & \sum_{j=1}^{K} u_{i j}=1 \quad \forall i=1, \ldots, n \\
& \sum_{j=1}^{K} v_{j} \leq K \\
& u_{i j} \leq v_{j} \quad \forall i=1, \ldots, n, j=1, \ldots, V \\
& \sum_{i=1}^{n} q_{i} u_{i j} \leq Q_{j} \quad \forall j=1, \ldots, K \\
& u_{i j}, v_{j} \in\{0,1\} \quad \forall i=1, \ldots, n, j=1, \ldots, K
\end{aligned}
$$

Parameter $K$ is an upper bound on the number of clusters, $\underline{s}_{i j}$ is the dissimilarity measure between observation $i$ and cluster $j, q_{i}$ is the weight of observation $i$, and $Q_{j}$ is the capacity of cluster $j$. Variable $u_{i j}$ denotes the assignment of observation $i$ to cluster $j$ and variable $v_{j}$ is equal to 1 if cluster $j$ is used. If the metric $\underline{s}_{i j}$ is a distance and the clusters are homogeneous (i.e., $Q_{j}=Q \forall j$ ), the formulation also models the well-known facility location problem. A solution approach is discussed in [62] while an alternative quadratic programming formulation is presented in [154]. Solution heuristics have also been proposed in [163] and [191].

## 4.3 K-Hyperplane Clustering

In the $K$-Hyperplane Clustering ( $K$-HC) problem, a hyperplane, instead of a center, is associated with each cluster. This is motivated by applications such as text mining and image segmentation, where collinearity and coplanarity relations among the observations are the main interest of the unsupervised learning task, rather than the similarity. Given the observations $x_{i}, i=1, \ldots, n$, the $K$-HC problem requires to find $K$ clusters, and a hyperplane $H_{j}=\left\{x \in \mathbb{R}^{p}: w_{j}^{T} x=\gamma_{j}\right\}$, with $w_{j} \in \mathbb{R}^{p}$ and $\gamma_{j} \in \mathbb{R}$, for each cluster $j$. The aim is to minimize the sum of the squared 2-norm Euclidean orthogonal distances between each observation and the corresponding cluster.

Given that the orthogonal distance of $x_{i}$ to hyperplane $H_{j}$ is given by $\frac{\left|w_{j}^{T} x_{i}-\gamma_{j}\right|}{\|w\|_{2}}, K$-HC is formulated in [4] as the following mixed integer quadratically constrained quadratic problem

$$
\begin{aligned}
& \min \sum_{i=1}^{n} \delta_{i}^{2} \\
& \text { s.t } \sum_{j=1}^{K} u_{i j}=1 \quad \forall i=1, \ldots, n \\
& \delta_{i} \geq\left(w_{j}^{T} x_{i}-\gamma_{j}\right)-M\left(1-u_{i j}\right) \quad \forall i=1, \ldots, n, j=1, \ldots, K \\
& \delta_{i} \geq\left(-w_{j}^{T} x_{i}+\gamma_{j}\right)-M\left(1-u_{i j}\right) \quad \forall i=1, \ldots, n, j=1, \ldots, K \\
& \left\|w_{j}\right\|_{2} \geq 1 \quad \forall j=1, \ldots, K \\
& \delta_{i} \geq 0 \quad \forall i=1, \ldots, n \\
& w_{j} \in \mathbb{R}^{p}, \gamma_{j} \in \mathbb{R} \quad \forall j=1, \ldots, K \\
& u_{i j} \in\{0,1\} \quad \forall i \in 1, \ldots, n, j=1, \ldots, K
\end{aligned}
$$

Binary variable $u_{i j}$ is equal to 1 if point $x_{i}$ is assigned to cluster $j$, and 0 otherwise. Linear constraints (73)(74) set $\delta_{i}$ as the distance between point $x_{i}$ and the hyperplane of cluster $j$. These constraints are enforced only if $u_{i j}$ is equal to 1 , otherwise they are redundant. The non-convexity is due to constraint (75). As a solution approach, a distance-based reassignment heuristic that outperforms spatial branch-and-bound solvers is proposed in [4].

# 5 Linear Dimension Reduction 

In Section 2.2, shrinkage methods have been discussed as a way to improve model interpretability by fitting a model with all original $p$ predictors. In this section, we discuss dimension reduction methods that search for $H<p$ linear combinations of the predictors such that $Z_{h}=\sum_{j=1}^{p} \phi_{j}^{h} X_{j}$ (also called projections) where $X_{j}$ denotes column $j$ of X , i.e., the vector of values of feature $j$ of the training set. While this section focuses on Principle Component Analysis and Partial Least Squares, we note that other linear and nonlinear dimension reduction methods exist. An extensive survey on benefits and shortcomings of dimension reduction methods is presented in $[76]$.

### 5.1 Principal Components

Principal Components Analysis (PCA) [131] aims to find a low-dimensional representation of the dataset with highly informative derived features. Principal components are ordered in terms of their explained variances, which measure the amount of information retained from the original set of features $X_{1}, \ldots, X_{p}$.

In particular, assuming the regressors are standardized to a mean of 0 and a variance of 1 , the direction of the first principal component is a unit vector $\phi^{1} \in \mathbb{R}^{p}$ that is the solution of the optimization problem

$$
\begin{gathered}
\max _{\phi^{1} \in \mathbb{R}^{p}} \frac{1}{n} \sum_{i=1}^{n}\left(\sum_{j=1}^{p} \phi_{j}^{1} x_{i j}\right)^{2} \\
\text { s.t. } \sum_{j=1}^{p}\left(\phi_{j}^{1}\right)^{2}=1
\end{gathered}
$$

Problem (79)-(80) is the traditional formulation of PCA and can be solved via Lagrange multipliers methods. Since the formulation is sensitive to the presence of outliers, several approaches have been proposed to improve robustness [185]. One approach is to replace the 2 -norm in (79) with the 1 -norm.

An iterative approach can be used to obtain the principal components where the first principal component $Z_{1}=\sum_{j=1}^{p} \phi_{j}^{1} X_{j}$ is the projection of the original features with the largest variability. The subsequent principal components are obtained iteratively where each principal component $Z_{h}, h=2, \ldots, H$ is obtained by a linear combination of the feature columns $X_{1}, \ldots, X_{p}$. Each $Z_{h}$ is uncorrelated with $Z_{1}, \ldots, Z_{h-1}$ which have larger variance. Introducing the sample covariance matrix $S$ of the regressors $X_{j}$, the direction $\phi^{h} \in \mathbb{R}^{p}$ of the $h$-th principal component $Z_{h}$ is the solution of

$$
\begin{gathered}
\max _{\phi^{h} \in \mathbb{R}^{p}} \frac{1}{n} \sum_{i=1}^{n}\left(\sum_{j=1}^{p} \phi_{j}^{h} x_{i j}\right)^{2} \\
\text { s.t. } \sum_{j=1}^{p}\left(\phi_{j}^{h}\right)^{2}=1 \\
\phi^{h^{\top}} S \phi^{l}=0 \quad \forall l=1, \ldots, h-1
\end{gathered}
$$

PCA can be used for several data analysis problems which benefit from reducing the problem dimension. Principal Components Regression (PCR) is a two-stage procedure that uses the first principal components as predictors for a linear regression model. PCR has the advantage of including less predictors than the original set and at the same time retaining the variability of the dataset in the derived features. However, principal components might not be relevant with the response variables of the regression.

To select principal components in regression models, the regression loss function and the PCA objective function can be combined in a single-step quadratic programming formulation [135]. Since the identification of the principal components does not require any knowledge of the response $y$, PCA can also be adopted in unsupervised learning such as in the $k$-means clustering method (see Section 4.1, [85]). A known drawback of PCA is interpretability. To promote the sparsity of the projected components, and thus make them more interpretable, [55] formulates a Mixed Integer Nonlinear Programming (MINLP) problem and shows that the level of sparsity can be imposed in the model. Alternatively, the variance of the principal components and their sparsity can be jointly maximized in a biobjective framework [54].

# 5.2 Partial Least Squares 

Partial Least Squares (PLS) identifies transformed features $Z_{1}, \ldots, Z_{H}$ by projecting both the predictors $X$ and their corresponding response $y$ into a new space, and this is an approach specific to regression problems [99]. PLS is particularly viable for problems with a large number of features compared to observations as it aims to identify the latent factors that explain most the variations in the response. PLS corresponds to fitting simple regression models each containing a single predictor variable.

The first PLS direction is denoted by $\phi^{1} \in \mathbb{R}^{p}$ where each component $\phi_{j}^{1}$ is found by fitting a regression with predictor $X_{j}$ and response $y$. The first PLS direction points towards the features that are more strongly related to the response. For computing the second PLS direction, the features vectors $X_{1}, \ldots, X_{p}$ are first orthogonalized with respect to $Z_{1}$ (as per the Gram-Schmidt approach), and then individually fitted in simple regression models with response $y$. The process is iterated for all PLS directions $H<p$. The coefficient of the simple regression of $y$ onto each original feature $X_{j}$ can also be computed as the inner product $\left\langle y, X_{j}\right\rangle$. Similar to PCR, PLS then fits a linear regression model with regressors $Z_{1}, \ldots, Z_{H}$ and response $y$.

While the principal components directions maximize variance, PLS searches for directions $Z_{h}=\sum_{j=1}^{p} \phi_{j}^{h} X_{j}$ with both high variance and high correlation with the response. The $h$-th direction $\phi^{h}$ can be found by solving the optimization problem

$$
\begin{aligned}
& \max _{\phi^{h} \in \mathbb{R}^{p}} \operatorname{Corr}\left(y, X \phi^{h}\right)^{2} \times \operatorname{Var}\left(X \phi^{h}\right) \\
& \text { s.t. } \sum_{j=1}^{p}\left(\phi_{j}^{h}\right)^{2}=1 \\
& \quad \phi^{h^{\top}} S \phi^{l}=0 \quad \forall l=1, \ldots, h-1
\end{aligned}
$$

where $\operatorname{Corr}()$ indicates the correlation matrix, $\operatorname{Var}()$ the variance, $S$ the sample covariance matrix of $X_{j}$, and (86) ensures that $Z_{m}$ is uncorrelated with the previous directions $Z_{l}=\sum_{j=1}^{p} \phi_{j}^{l} X_{j}$.

## 6 Deep Learning

Deep Learning received a first momentum until the 80s due to universal approximation results [79, 123]. Neural networks with a single layer with a finite number of units can represent any multivariate continuous function on a compact subset in $\mathbb{R}^{n}$ with arbitrary precision. However, the computational complexity required for training Deep Neural Networks (DNNs) hindered their diffusion by late 90s. Starting 2010, the empirical success of

![img-0.jpeg](img-0.jpeg)

Figure 1: Deep Feedforward Neural Network with 3 layers. The input layer has $n^{0}=3$ units, the hidden layer has $n^{1}=5$ units and there are $n^{2}=2$ output units. This is an example of fully connected network, where each neuron in one layer is connected to all neurons in the next layer. Training such network requires to determine weight matrices $W^{0} \in \mathbb{R}^{3 \times 5}, W^{1} \in \mathbb{R}^{5 \times 2}$, and bias vectors $b^{1} \in \mathbb{R}^{5}, b^{2} \in \mathbb{R}^{2}$.

DNNs has been widely recognized for several reasons, including the development of advanced processing units, namely GPUs, the advances in the efficiency of training algorithms such as backpropagation, the establishment of proper initialization parameters, and the massive collection of data enabled by new technologies in a variety of domains (e.g., healthcare, supply chain management [205], marketing, logistics [215], Internet of Things).

DNNs can be used for the regression and classification tasks discussed in the previous sections, especially when traditional machine learning models fail to capture complex relationships between the input data and the quantitative response, or class, to be learned. The aim of this section is to describe the decision optimization problems associated with DNN architectures. To facilitate the presentation, the notation for the common parameters is provided in Table 1, and an example of fully connected feedforward network is shown in Figure 1 .


Table 1: Notation for DNN architectures.

The output vector $x^{L}$ of a DNN is computed by propagating the information from the input layer to each following layer via the weight matrices $W^{l}, l<L$, the bias vectors $b^{l}, l>0$, and the activation function $\sigma$, such that

$$
x^{l}=\sigma\left(W^{l-1} x^{l-1}+b^{l-1}\right) \quad \forall l=1, \ldots, L
$$

Activation functions indicate whether a neuron should be activated or not in the network, and are responsible for the capability of DNNs to learn complex relationships between the input and the output. The rectified linear unit

$$
\operatorname{ReLU}: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n}, \operatorname{ReLU}(z)=\left(\max \left(0, z_{1}\right), \ldots, \max \left(0, z_{n}\right)\right)
$$

is typically one of the preferred options for activation functions, mainly because it can be optimized with gradient-based methods for DNN training, and tends to produce sparse networks (where not all neurons are activated).

In the context of regression, the components of $x^{L}$ can directly represent the response values learned. For a classification problem, the vector $x^{L}$ corresponds to the logits of the classifier. In order to interpret $x^{L}$ as a vector of class probabilities, functions $F$ such as the logistic sigmoidal or the softmax can be applied to

$x^{L}$ [108]. The classifier $\mathcal{C}$ modeled by the DNN then classifies an input $x$ with the label correspondent to the maximum activation $\mathcal{C}(x)=\underset{i=1, \ldots, n^{L}}{\arg \max } F\left(x_{i}^{L}\right)$.

The task of training a DNN consists of determining the weights $W^{l}$ and the biases $b^{l}$ that make the model best fit the training data, according to a certain measure of training loss. In multivariate regression with $K$ response variables $[126,166]$, the training loss $\mathcal{L}$ is typically the sum-of-squared errors $\sum_{k=1}^{K} \sum_{i=1}^{n}\left(y_{i k}-x_{k}^{L}\right)^{2}$ where $y_{i k}$ denotes response $k$ corresponding to the $i$-th input vector. For classification with $K$ classes, crossentropy $-\sum_{k=1}^{K} \sum_{i=1}^{n} y_{i k} \log x_{k}^{L}$ is preferred. An effective approach to minimize $\mathcal{L}$ is by gradient descent, called back-propagation in this setting. Typically, one is not interested in a proven local minimum of $\mathcal{L}$, as this is likely to overfit the training dataset and yield a learning model with a high variance. Similar to the Ridge regression (see Section 2), the loss function can include regularization terms, such as a weight decay term

$$
\lambda\left(\sum_{l=0}^{L-1} \sum_{i=1}^{n_{l}}\left(b_{i}^{l}\right)^{2}+\sum_{l=0}^{L-1} \sum_{i=1}^{n_{l}} \sum_{j=1}^{n_{l+1}}\left(W_{i j}^{l}\right)^{2}\right)
$$

or alternatively a weight elimination penalty term

$$
\lambda\left(\sum_{l=0}^{L-1} \sum_{i=1}^{n_{l}} \frac{\left(b_{i}^{l}\right)^{2}}{1+\left(b_{i}^{l}\right)^{2}}+\sum_{l=0}^{L-1} \sum_{i=1}^{n_{l}} \sum_{j=1}^{n_{l+1}} \frac{\left(W_{i j}^{l}\right)^{2}}{1+\left(W_{i j}^{l}\right)^{2}}\right)
$$

Weight decay limits the growth of the weights, which speeds up the training via backpropagation, and has been shown to limit overfitting (see [184] for a discussion about overfitting in Neural Networks).

The aim of this section is to present the optimization models that are used in DNN for feedforward architectures. Several other neural network architectures have been investigated in deep learning [108]. In particular, Convolutional Neural Networks (CNN) [152] have been successfully adopted for processing data with a gridlike topology, such as images [147], videos [133], and traffic analytics [219]. In CNN, the output of layers is obtained via convolutions (instead of the matrix multiplication in feedforward networks), and pooling operations on nearby units (such as average or maximum operators). In the remainder of the section, mixed integer programming models for DNN training are introduced in Section 6.1, and ensemble approaches with multiple activation functions are discussed in Section 6.2.

# 6.1 Mixed Integer Programming for DNN Architectures 

Motivated by the considerable improvements of mixed integer programming solvers, a natural question is how to model a trained DNN as a MIP. In [97], DNNs with ReLU activation

$$
x^{l}=\operatorname{ReLU}\left(W^{l-1} x^{l-1}+b^{l-1}\right) \quad \forall l=1, \ldots, L
$$

are modeled as a MIP with decision variables $x^{l}$ expressing the output vector of layer $l, l>0$ and $l^{0}$ is the input vector. To express (88) explicitly, each unit $U(j, l)$ of the DNN is associated with binary activation variables $z_{j}^{l}$, and continuous slack variables $s_{j}^{l}$. The following mixed integer linear problem is proposed

$$
\begin{aligned}
\min & \sum_{l=0}^{L} \sum_{j=1}^{n_{l}} c_{j}^{l} x_{j}^{l}+\sum_{l=1}^{L} \sum_{j=1}^{n_{l}} \gamma_{j}^{l} z_{j}^{l} \\
\text { s.t. } & \sum_{i=1}^{n_{l-1}} w_{i j}^{l-1} x_{i}^{l-1}+b_{j}^{l-1}=x_{j}^{l}-s_{j}^{l} \quad \forall l=1, \ldots, L, j=1, \ldots, n_{l} \\
& x_{j}^{l} \leq\left(1-z_{j}^{l}\right) M_{x}^{j, l} \quad \forall l=1, \ldots, L, j=1, \ldots, n_{l} \\
& s_{j}^{l} \geq z_{j}^{l} M_{s}^{j, l} \quad \forall l=1, \ldots, L, j=1, \ldots, n_{l} \\
& 0 \leq x_{j}^{l} \leq u b_{j}^{l} \quad \forall l=1, \ldots, L, j=1, \ldots, n_{l} \\
& 0 \leq s_{j}^{l} \leq \widehat{u b}_{j}^{l} \quad \forall l=1, \ldots, L, j=1, \ldots, n_{l}
\end{aligned}
$$

where $M_{x}^{j, l}, M_{s}^{j, l}$ are suitably large constants. We note that since the DNN is trained, the weights $w_{i j}^{l}$ and bias $b_{j}^{l}$ are fixed parameters. Depending on the application, different activation weights $c_{j}^{l}$ and activation costs $\gamma_{j}^{l}$

can also be used for each $U(j, l)$. If known, upper bound $u b_{j}^{l}$ can be enforced on the output $x_{j}^{l}$ of unit $U(j, l)$ via constraints (93), and slack $s_{j}^{l}$ can be bounded by $\overline{u b}_{j}^{l}$ via constraints (94).

The proposed MIP is feasible for every input vector $x^{0}$ since it computes the activation in the subsequent layers. Constraints (91) and (92) are known to have a weak continuous relaxation, and the tightness of the chosen constants (bounds) is crucial for their effectiveness. Several optimization solvers can directly handle such kind of constraints as indicator constraints [40]. In [97], a bound-tightening strategy to reduce the computational times is proposed and the largest DNN tested with this approach is a 5-layer DNN with $20+$ $20+10+10+10$ internal units.

Problem (89)-(94) can model several tasks in Deep Learning, other than the computation of quantitative responses in regression, and of classification. Such tasks include

- Pooling operations: The average and the maximum operators

$$
\begin{aligned}
& \operatorname{Avg}\left(x^{l}\right)=\frac{1}{n^{l}} \sum_{i=1}^{n^{l}} x_{i}^{l} \\
& \operatorname{Max}\left(x^{l}\right)=\max \left(x_{1}^{l}, \ldots, x_{n^{l}}^{l}\right)
\end{aligned}
$$

can be incorporated in the hidden layers. In the case of max pooling operations, additional indicator constraints are required. For example, average and maximum operators are often used in CNNs, as mentioned earlier in Section 6.

- Maximizing the unit activation: By maximizing the objective function (89), one can find input examples $x^{0}$ that maximize the activation of the units. This may be of interest in applications such as the visualization of image features.
- Building crafted adversarial examples: Given an input vector $x^{0}$ labeled as $\chi$ by the DNN, the search for perturbations of $x^{0}$ that are classified as $\chi^{\prime} \neq \chi$ (adversarial examples), can be conducted by adding conditions on the activation of the final layer $L$ and minimizing the perturbation. In [97], such conditions are actually restricting the search for adversarial examples and the resulting formulation does not guarantee an adversarial solution nor can prove that no adversarial examples exist. Adversarial learning is the objective of the discussion in Section 7.
- Training: In this case, the weights and biases are decision variables. The resulting bilinear terms in (90) and the considerable number of decision variables in the formulation limit the applicability of (89)-(94) for DNN training.

Another attempt in modelling DNNs via MIPs is provided by [140], in the context of Binarized Neural Networks (BNNs). BNNs are characterized by having binary weights $\{-1,+1\}$ and by using the sign function for neuron activation [74]. In [140], a MIP is proposed for finding adversarial examples in BNNs by maximizing the difference between the activation of the targeted label $\chi^{\prime}$ and the predicted label $\chi$ of the input $x^{0}$, in the final layer (namely, $\max x_{\chi^{\prime}}^{L}-x_{\chi}^{L}$ ). Contrary to [97], the MIP of [140] does not impose limitations on the search of adversarial examples, apart from the perturbation quantity. In terms of optimality criterion however, searching for the proven largest misclassified example is different from finding a targeted adversarial example. Furthermore, while there is interest in minimally perturbed adversarial examples, suboptimal solutions corresponding to adversarial examples (i.e., $x_{\chi^{\prime}}^{L} \geq x_{\chi}^{L}$ ) may have a perturbation smaller than that of the optimal solution. Recently, [125] investigated a hybrid constraint programming/mixed integer programming method to train BNNs. Such model-based approach provides solutions that generalize better than those found by the largely adopted training solvers, such as gradient descent, especially for small datasets. We note that methods such as gradient descent can usually only guarantee local optimality (unless early stopping takes place).

Besides [97], other MIP frameworks have been proposed to model certain properties of neural networks in a bounded input domain. In [65], the problem of computing maximum perturbation bounds for DNNs is formulated as a MIP, where indicator constraints and disjunctive constraints are modeled using constraints with big-M coefficients [111]. The maximum perturbation bound is a threshold such that the perturbed input may be classified correctly with a high probability. A restrictive misclassification condition is added when formulating the MIP. Hence, the infeasibility of the MIP does not certify the absence of adversarial examples. In addition to the $\operatorname{ReLU}$ activation, the $\tan ^{-1}$ function is also considered by introducing quadratic constraints and several heuristics are proposed to solve the resulting problem. In [206], a model to formally measure the vulnerability to adversarial examples is proposed (the concept of vulnerability of neural networks is discussed in

more details in Sections 7.1 and 7.2). A tight formulation for the resulting nonlinearities and a novel presolve technique are introduced to limit the number of binary variables and improve the numerical conditioning. However, the misclassification condition of adversarial examples is not explicitly defined but is rather left in the form "different from" and not explicitly modeled using equality/inequality constraints. In [193], the aim is to count or bound the number of linear regions that a piecewise linear classifier represented by a DNN can attain. Assuming that the input space is bounded and polyhedral, the DNN is modeled as a MIP. The contributions of adopting a MIP framework in this context are limited, especially in comparison with the computational results achieved in [170].

MIP frameworks can also be used to formulate the verification problem for neural networks as a satisfiability problem. In [134], a satisfiability modulo theory solver is proposed based on an extension of the simplex method to accommodate the $R e L U$ activation functions. In [48], a branch-and-bound framework for verifying piecewiselinear neural networks is introduced. For a recent survey on the approaches for automated verification of NNs, the reader is referred to [153].

# 6.2 Activation Ensembles 

Another research direction in neural network architectures investigates the possibility of adopting multiple activation functions inside the layers of a neural network, to increase the accuracy of the classifier. Some examples in this framework are given by the maxout units [110], returning the maximum of multiple linear affine functions, and the network-in-network paradigm [156] where the $R e L U$ activation function is replaced by fully connected network. In [1], adaptive piecewise linear activation functions are learned when training each neuron. Specifically, for each unit $i$ and value $z$, activation $\sigma_{i}(z)$ is considered as

$$
\sigma_{i}(z)=\max (0, z)+\sum_{s=1}^{S} a_{i}^{s} \max \left(0,-z+b_{i}^{s}\right)
$$

where the number of hinges $S$ is a hyperparameter to be fixed before training, while the variables $a_{i}^{s}, b_{i}^{s}$ have to be learned. Functions $\sigma_{i}$ generalize the $R e L U$ function (first term of (95)), and can approximate a class of continuous piecewise-linear functions, for large enough $S[1]$.

In a more general perspective, ensemble layers are proposed in [142] to consider multiple activation functions in a neural network. The idea is to embed a family of activation functions $\left\{\Phi^{1}, \ldots, \Phi^{m}\right\}$ and let the network itself choose the magnitude of their activation for each neuron $i$ during the training. To promote relatively equal contribution to learning, the activation functions need to be scaled to the interval $[0,1]$. In order to measure the impact of the activation in the neural network, each function $\Phi^{j}$ is associated with a continuous variable $\alpha^{j}$. The resulting activation $\sigma_{i}$ for neuron $i$ is then given by

$$
\sigma_{i}(z)=\sum_{j=1}^{m} \alpha_{i}^{j} \cdot \frac{\Phi^{j}(z)-\min _{x \in X}\left(\Phi^{j}\left(z_{x, i}\right)\right)}{\max _{x \in X}\left(\Phi^{j}\left(z_{x, i}\right)\right)-\min _{x \in X}\left(\Phi^{j}\left(z_{x, i}\right)\right)+\epsilon}
$$

where $z_{x, i}$ is the output of neuron $i$ associated with training example $x, X$ is the set of training observations, and $\epsilon$ is a small tolerance. Equation (96) is a weighted sum of the scaled $\Phi^{j}$ functions, which is integrated in the training of the DNN architecture. The min and max in (96) can be approximated on a minibatch of observations in $X$, in the testing phase. In order to impose the selection of functions $\Phi^{j}$, the magnitude of the weights $\alpha^{j}$ is limited in a projection subproblem, where for each neuron the network should choose an activation function and therefore all $\alpha^{j}$ should sum to 1 . If $\hat{\alpha_{j}}$ are the weight values obtained by gradient descent while training, then the projected weights are found by solving the convex quadratic programming problem

$$
\begin{aligned}
\min & \sum_{j=1}^{m} \frac{1}{2}\left(\alpha^{j}-\hat{\alpha}^{j}\right)^{2} \\
\text { s.t. } & \sum_{j=1}^{m} \alpha^{j}=1 \\
& \alpha^{j} \geq 0 \forall j=1, \ldots, m
\end{aligned}
$$

which can be solved in closed form via the Karush-Kuhn-Tucker (KKT) conditions.

# 7 Adversarial Learning 

Despite the wide adoption of Machine Learning models in real-world applications, their integration into safety and security related use cases still necessitates thorough evaluation and research. A large number of contributions in the literature pointed out the dangers caused by perturbed examples, also called adversarial examples, causing classification errors [35, 201]. Malicious attackers can thus exploit security falls in a general classifier. In case the attacker has a perfect knowledge of the classifier's architecture (i.e., the result of the training phase), then a white-box attack can be performed. Black-box attacks are instead performed without full information of the classifier. The interest in adversarial examples is also motivated by the transferability of the attacks to different trained models [148, 208]. Adversarial learning then emerges as a framework to devise vulnerability attacks for classification models [160].

From a mathematical perspective, such security issues have been formerly expressed via min-max approaches where the learner's and the attacker's loss functions are antagonistic [82, 106, 150]. Non-antagonistic losses are formulated as a Stackelberg equilibrium problem involving a bilevel optimization formulation [47], or in a Nash equilibrium approach [46]. These theoretical frameworks rely on the assumption of expressing the actual problem constraints in a game-theory setting, which is often not a viable option for real-life applications.

The search for adversarial examples can also be used to evaluate the efficiency of Generative Adversarial Networks (GANs) [109]. A GAN is a minmax two-player game where a generative model $G$ tries to reproduce the training data distribution and a discriminative model $D$ estimates the probability of detecting samples coming from the true training distribution, rather than $G$. The game terminates at a saddle point, which is a minimum with respect to a player's strategy and a maximum for the other player's strategy. Discriminative networks can be affected by the presence of adversarial examples because the specific inputs to the classification networks are not considered in GANs training.

Adversarial attacks on the test set can be conducted in a targeted or untargeted fashion [53]. In the targeted setup, the attacker aims to achieve a classification with a chosen target class (discussed in Section 7.1), while the untargeted misclassification is not constrained to achieve a specific class (Section 7.2). The robustness of DNNs to adversarial attacks is discussed in Section 7.3. Finally, data poisoning attacks are described in Section 7.4. While the majority of the cited papers of the present section refer to DNN applications, adversarial learning can, in general, be formulated for classifiers with quantitative classes, such as those discussed in Section 3.

### 7.1 Targeted attacks

Given a neural network classifier $f: \psi \subset \mathbb{R}^{p} \rightarrow \Upsilon$, an input $x \in \psi$ with label $y \in \Upsilon$, and a target label $y^{\prime} \in \Upsilon$, a targeted attack consists of a perturbation $r$ such that $f(x+r)=y^{\prime}$. This corresponds to finding an input "close" to $x$, which is misclassified by $f$. Clearly, if the target $y^{\prime}$ coincides with $y$, the problem has the trivial solution $r=0$ and no misclassification takes place.

The minimum adversarial problem for targeted attacks consists of finding a perturbation $r$ by solving

$$
\begin{aligned}
& \min _{r \in \mathbb{R}^{p}}\|r\|_{2} \\
& \text { s.t. } f(x+r)=y^{\prime} \\
& x+r \in \psi
\end{aligned}
$$

The condition (102) ensures that the perturbed example $x+r$ belongs to the set of admissible inputs. The difficulty of solving problem (100)-(102) to optimality depends on the complexity of the classifier $f$, and the set $\psi$ of feasible inputs. In general, it is computationally challenging to find an optimal solution to the problem, especially in the case of neural networks.

For classification of normalized images with binary pixel values, [201] introduces the box-constrained approximation

$$
\begin{aligned}
& \min _{r \in \mathbb{R}^{p}} c|r|+\mathcal{L}\left(x+r, y^{\prime}\right) \\
& \text { s.t. } x+r \in[0,1]^{p}
\end{aligned}
$$

where $\mathcal{L}: \psi \times \Upsilon \rightarrow \mathbb{R}^{+}$denotes the loss function for training $f$ (e.g., cross-entropy). The approximation is exact for convex loss functions, and can be solved via a line search algorithm on $c>0$. For a fixed $c$, the formulation can be tackled by the box-constrained version of the Limited-memory Broyden-Fletcher-Goldfarb-Shanno (LBFGS) method [49]. In [112], $c$ is fixed such that the perturbation is minimized on a sufficiently large subset $X^{\prime}$ of data points, and the mean prediction error rate of $f\left(x_{i}+r_{i}\right), x_{i} \in X^{\prime}$ is greater than a threshold. In [53],

the 2 -norm in (100) is generalized to the $l$-norm with $l \in\{0,2, \infty\}$ and an alternative formulation is introduced which includes functions $\mathcal{F}$ in the objective where $f(x+r)=y^{\prime}$ is satisfied if and only if $\mathcal{F}(x+r) \leq 0$. The equivalent formulation is then

$$
\begin{gathered}
\min _{r \in \mathbb{R}^{p}}\|r\|_{l}+\Lambda \mathcal{F}(x+r) \\
\text { s.t. } x+r \in \psi
\end{gathered}
$$

where $\Lambda$ is a constant that can be determined by binary search such that the solution $r^{*}$ satisfies the condition $\mathcal{F}\left(x+r^{*}\right) \leq 0$. For the case where (106) are box constraints similar to (104), the authors propose strategies for applying optimization algorithms such as Adam [141]. Novel classes of attacks are identified for the considered metrics.

# 7.2 Untargeted attacks 

In untargeted attacks, one searches for adversarial examples $x^{\prime}$ close to the original input $x$ with label $y$ for which the classified label $y^{\prime}$ of $x^{\prime}$ is different from $y$, without targeting a specific label for $x^{\prime}$. Given that the only aim is misclassification, untargeted attacks are deemed less powerful than the targeted counterpart, and received less attention in the literature.

A mathematical formulation for finding minimum adversarial distortion for untargeted attacks is proposed in [206]. Assuming that the output values of classifier $f$ are expressed by the functions $f_{y^{\prime}}$ associated with labels $y^{\prime} \in \Upsilon$ (i.e., $f_{y^{\prime}}$ are the scoring functions), and a distance metric $d$ is given, then a minimum perturbation $r$ for an untargeted attack is found by solving

$$
\begin{aligned}
& \min _{r \in \mathbb{R}^{p}} d(r) \\
& \text { s.t. } \underset{y^{\prime} \in \Upsilon}{\arg \max }\left\{f_{y^{\prime}}(x+r)\right\} \neq y \\
& x+r \in \psi
\end{aligned}
$$

This formulation can easily accommodate targeted attacks in a set $T \not \ni y$ by replacing (108) with $\arg \max _{y^{\prime}}\left\{f_{y^{\prime}}(x+\right.$ $r)\} \in T$. The most commonly adopted metrics in the literature are the 1,2 , and $\infty$-norm, which can all be expressed with continuous variables, as shown in [206]. The 2-norm makes the objective function of the outer-level optimization problem quadratic.

In order to express the logical constraint (108) in a mathematical programming formulation, problem (107)-(109) can be cast as the bilevel optimization problem

$$
\begin{aligned}
\min _{r \in \mathbb{R}^{p}, z \in \Upsilon} & d(r) \\
\text { s.t. } & z-y \leq-\epsilon+M s \\
& z-y \geq \epsilon-(1-s) M \\
& z \in \underset{y^{\prime} \in \Upsilon}{\arg \max }\left\{f_{y^{\prime}}(x+r)\right\} \\
& x+r \in \psi \\
& s \in\{0,1\}
\end{aligned}
$$

where $\epsilon>0$ is a small constant, $z$ is a decision variable representing the classified label, $M$ is a big-M coefficient, and $s$ is a binary variable that enforces one of the constraints (111)-(112) which express the condition of misclassification $z \neq y$. The complexity of the inner-level optimization problem is dependent on the scoring functions. Given that the upper-level feasibility set $\psi$ is typically continuous and the lower-level variable $y^{\prime}$ ranges on a discrete set, the problem is in fact a continuous discrete bilevel programming problem [93] with convex quadratic function [90], which requires dedicated reformulations or approximations [64, 113, 130].

We introduce an alternative mathematical formulation for finding untargeted adversarial examples satisfying condition (108). A perturbed input $x^{\prime}=x+r$ for a sample $x$ classified with label $y \in \Upsilon$ is an untargeted adversarial example if the classified label of $x^{\prime}$ is different from $y$. This condition is equivalent to

$$
\exists y^{\prime} \in \Upsilon \backslash\{y\} \text { s.t. } f_{y^{\prime}}\left(x^{\prime}\right)>f_{y}\left(x^{\prime}\right)
$$

Condition (116) is an existence condition, which can be formalized by introducing the functions $\tilde{\sigma}_{y^{\prime}}(r)=$ $\operatorname{ReLU}\left(f_{y^{\prime}}(x+r)-f_{y}(x+r)\right), y^{\prime} \in \Upsilon \backslash\{y\}$, and the condition

$$
\sum_{y^{\prime} \in \Upsilon \backslash\{y\}} \tilde{\sigma}_{y^{\prime}}(r)>\nu
$$

where parameter $\nu>0$ enforces that at least one $\tilde{\sigma}_{y^{\prime}}$ function has to be activated for a perturbation $r$. Therefore, untargeted adversarial examples can be found from formulation (107)-(109) by replacing condition (108) with the linear condition (117) and adding $|\Upsilon|-1$ functions $\tilde{\sigma}_{y^{\prime}}(r)$. The complexity of this approach depends on the scoring functions $f_{y^{\prime}}$. The extra $\operatorname{ReLU}$ functions $\tilde{\sigma}$ can be expressed as a mixed integer formulation as done in problem (89)-(94).

# 7.3 Adversarial robustness 

Another interesting line of research motivated by adversarial learning deals with adversarial training, which consists of techniques to make a neural network robust to adversarial attacks. The problem of measuring the robustness of a neural network is formalized in [17]. The pointwise robustness evaluates if the classifier $f$ on $x$ is robust for "small" perturbations. Formally, $f$ is said to be $(x, \epsilon)$-robust if

$$
y^{\prime}=y, \forall x^{\prime} \text { s.t. }\left\|x^{\prime}-x\right\|_{\infty} \leq \epsilon
$$

Then, the pointwise robustness $\rho(f, x)$ is the minimum $\epsilon$ for which $f$ fails to be $(x, \epsilon)$-robust:

$$
\rho(f, x)=\inf \{\epsilon \geq 0 \mid f \text { is not }(x, \epsilon) \text {-robust }\}
$$

As detailed in [17], $\rho$ is computed by expressing (119) as a constraint satisfiability problem. By imposing a bound on the perturbation, an estimation of the pointwise robustness can be performed by solving a MIP [65].

A widely known defense technique is to augment the training data with adversarial examples; this however does not offer robustness guarantees on novel kinds of attacks. The adversarial training of neural network via robust optimization is investigated in [162]. In this setting, the goal is to train a neural network to be resistant to all attacks belonging to a certain class of perturbations. Particularly, the adversarial robustness with a saddle point (min-max) formulation is studied in [162] which is obtained by augmenting the Empirical Risk Minimization paradigm.

Let $\theta \in \mathbb{R}^{p}$ be the set of model parameters to be learned, and $\mathcal{L}(\theta ; x, y)$ be the loss function considered in the training phase (e.g., the cross-entropy loss) for training examples $x \in X$ and labels $y \in \Upsilon$, and let $\mathcal{S}$ be the set of allowed perturbations (e.g., an $L_{\infty}$ ball). The aim is to minimize the worst expected adversarial loss on the set of inputs perturbed by $\mathcal{S}$

$$
\min _{\theta} \mathbb{E}_{(x, y)}\left[\max _{r \in \mathcal{S}} \mathcal{L}(\theta ; x+r, y)\right]
$$

where the expectation value is computed on the distribution of the training samples. The saddle point problem (120) is viewed as the composition of an inner maximization and an outer minimization problem. The inner problem corresponds to attacking a trained neural network by means of the perturbations $\mathcal{S}$. The outer problem deals with the training of the classifier in a robust manner. The importance of formulation (120) stems both from the formalization of adversarial training and from the quantification of the robustness given by the objective function value on the chosen class of perturbations. To find solutions to (120) in a reasonable time, the structure of the local minima of the loss function can be explored.

Another robust training approach consists of optimizing the model parameters $\theta$ with respect to worst-case data [194]. This is formalized by introducing a perturbation set $\mathcal{S}_{x}$ for each training example $x$. The aim is then to optimize

$$
\min _{\theta} \sum_{x \in X} \max _{r \in \mathcal{S}_{x}} \mathcal{L}(\theta ; x+r, y)
$$

An alternating ascent and descent steps procedure can be used to solve (121) with the loss function approximated by the first-order Taylor expansion around the training points.

# 7.4 Data Poisoning 

A popular class of attacks for decreasing the training accuracy of classifiers is that of data poisoning, which was first studied for SVMs [36]. A data poisoning attack consists of hiding corrupted, altered or noisy data in the training dataset. In [200], worst-case bounds on the efficacy of a class of causative data poisoning attacks are studied. The causative attacks [15] proceed as follow:

- a clean training dataset $\Gamma_{C}$ with $n$ data points drawn by a data-generating distribution is generated
- the attacker adds malicious examples $\Gamma_{M}$ to $\Gamma_{C}$, to let the defender (learner) learn a bad model
- the defender learns model with parameters $\hat{\theta}$ from the full dataset $\Gamma=\Gamma_{C} \cup \Gamma_{M}$, reporting a test loss $\mathcal{L}(\hat{\theta})$.

Data poisoning can be viewed as a game between the attacker and the defender players, where the defender wants to minimize $\mathcal{L}(\hat{\theta})$, and the attacker seeks to maximize it. As discussed in [200], data sanitization defenses to limit the increase of test loss $\mathcal{L}(\hat{\theta})$ include two steps: (i) data cleaning (e.g., removing outliers which are likely to be poisoned examples), to produce a feasible dataset $\Gamma^{\prime}$, and (ii) minimizing a margin-based loss on the cleaned dataset $\Gamma \cap \Gamma^{\prime}$. The learned model is then $\hat{\theta}=\arg \min _{\theta \in \Theta} \mathcal{L}\left(\theta ; \Gamma \cap \Gamma^{\prime}\right)$.

Poisoning attacks can also be performed in semi-online or online fashion, where training data is processed in a streaming manner, and not in fixed batches (i.e., offline). In the semi-online context, the attacker can modify part of the training data stream so as to maximize the classification loss, and the evaluation of the objective (loss) is done only at the end of the training. In the fully-online scenario, the classifier is instead updated and evaluated during the training process. In [218], a white-box attacker's behavior in online learning for a linear classifier $w^{T} x$ (e.g., SVM with binary labels $y \in\{-1,+1\}$ ) is formulated. The attacker knows the order in which the training data is processed by the learner. The data stream $S$ arrives in $T$ instants $\left(S=\left\{S_{1}, \ldots, S_{T}\right\}\right.$, with $S_{t}=\left(X_{t}, y_{t}\right)$ ) and the classification weights are updated using an online gradient descent algorithm [227] such that $w_{t+1}=w_{t}-\eta_{t}\left(\nabla \mathcal{L}\left(w_{t},\left(x_{t}, y_{t}\right)\right)\right)+\nabla \Omega\left(w_{t}\right)$, where $\Omega$ is a regularization function, $\eta_{t}$ is the step length of the iterate update, and $\mathcal{L}$ is a convex loss function. Let $\Gamma_{T}^{\cdot}$ be the cleaned dataset at time $T$ (which can be obtained, for instance, via the sphere and slab defenses), $U$ be a given upper bound on the number of changed examples in $\Gamma$ due to data sanitization, $g$ be the attacker's objective (e.g., classification error on the test set), $|\cdot|$ be the cardinality of a set. The semi-online attacker optimization problem can then be formulated as

$$
\begin{aligned}
& \max _{S \in \Gamma_{T}^{\prime}} g\left(w_{T}\right) \\
& \text { s.t. }|\{S \backslash \Gamma\}| \leq U \\
& \quad w_{t}=w_{0}-\sum_{\tau=0}^{t-1} \eta_{\tau}\left(\nabla \mathcal{L}\left(\omega_{\tau}, S_{\tau}\right)+\nabla \mathcal{L}\left(w_{\tau}\right)\right), 1 \leq t \leq T
\end{aligned}
$$

Compared to the offline case, the weights $w_{t}$ to be learned are a complex function of the data stream $S$, which makes the gradient computation more challenging and the KKT conditions do not hold. The optimization problem can be simplified by considering a convex surrogate for the objective function, given by the logistic loss. In addition, the expectation is conducted over a separate validation dataset and a label inversion procedure is implemented to cope with the multiple local maxima of the classifier function. The fully-online case can also be addressed by replacing objective (122) with $\sum_{t=1}^{T} g\left(w_{t}\right)$.

## 8 Emerging Paradigms

### 8.1 Machine Teaching

In all Machine Learning tasks discussed so far, the size of the training set of the machine learning models has been considered as a hyperparameter. The Teaching Dimension problem identifies the minimum size of a training set to correctly teach a model [107, 196]. The teaching dimension of linear learners, such as Ridge regression, SVM, and logistic regression has been recently discussed in [157]. With the intent to generalize the teaching dimension problem to a variety of teaching tasks, [225] and [226] provide the Machine Teaching framework. Machine Teaching is essentially an inverse problem to Machine Learning. While in a learning task, the training dataset $\Gamma=(X, y)$ is given and the model parameters $\theta=\theta^{*}$ have to be determined, the role of a teacher is to let a learner approximately learn a given model $\theta^{*}$ by providing a proper set $\Gamma$ of training examples

(also called teaching dataset in this context). A Machine Teaching task requires to select: i) a Teaching Risk TR expressing the error of the learner, with respect to model $\theta^{*}$; ii) a Teaching Cost TC expressing the convenience of the teaching dataset, from the prospective of the teacher, weighted by a regularization factor $\lambda$; iii) a learner L.

Formally, machine teaching can be cast as a bilevel optimization problem

$$
\begin{gathered}
\min _{\Gamma, \theta} \operatorname{TR}(\theta)+\lambda \operatorname{TC}(\Gamma) \\
\text { s.t. } \theta=\mathrm{L}(\Gamma)
\end{gathered}
$$

The upper optimization is the teacher's problem and the lower optimization $L(\Gamma)$ is the learner's machine learning problem. The teacher is aware of the learner, which could be a classifier (such as those of Section 3) or a deep neural network. Machine teaching encompasses a wide variety of applications, such as data poisoning attacks, computer tutoring systems, and adversarial training.

Problem (125)-(126) is, in general, challenging to solve. However, for certain convex learners, one can replace the lower problem by the corresponding KKT conditions, and reduce the problem to a single level formulation. The teacher is typically optimizing over a discrete space of teaching sets, hence, for some problem instances, the submodularity properties of the problem may be explored. For problems with a small teaching set, it is possible to formulate the teaching problem as a mixed integer nonlinear program. The computation of the optimal training set remains, in general, an open problem, and is especially challenging in the case where the learning algorithm does not have a closed-form solution with respect to the training set [225].

The minimization of teaching cost can be directly enforced in the constrained formulation

$$
\begin{gathered}
\min _{\Gamma, \theta} \operatorname{TC}(\Gamma) \\
\text { s.t. } \operatorname{TR}(\theta) \leq \epsilon \\
\theta=\mathrm{L}(\Gamma)
\end{gathered}
$$

which allows for either approximate or exact teaching. Alternatively, given a teaching budget $B$, the learning is performed via the constrained formulation

$$
\begin{gathered}
\min _{\Gamma, \theta} \operatorname{TR}(\theta) \\
\text { s.t. } \operatorname{TC}(\Gamma) \leq B \\
\theta=\mathrm{L}(\Gamma)
\end{gathered}
$$

Other variants consider multiple learners to be taught by the same teacher (i.e., common teaching set). The teacher can aim to optimize for the worst learner (minimax risk), or the average learner (Bayes risk). For the teaching dimension problem, the teaching cost is the cardinality of the teaching dataset, namely its 0 -norm. If the empirical minimization loss $\mathcal{L}$ is guiding the learning process, and $\lambda$ is the regularization weight, then teaching dimension problem can be formulated as

$$
\begin{aligned}
& \min _{\Gamma, \hat{\theta}} \lambda\|\Gamma\|_{0} \\
& \text { s.t. }\left\|\hat{\theta}-\theta^{*}\right\|_{2}^{2} \leq \epsilon \\
& \quad \hat{\theta} \in \operatorname{argmin}_{\theta \in \Theta} \sum_{x \in X} \mathcal{L}(\theta ; x)+\lambda\|\theta\|_{2}^{2}
\end{aligned}
$$

Machine teaching approaches tailored to specific learners have also been explored in the literature. In [223], a method is proposed for the Bayesian learners, while [180] focuses on Generalized Context Model learners. In [165], the bilevel optimization of machine teaching is explored to devise optimal data poisoning attacks for a broad family of learners (i.e., SVM, logistic regression, linear regression). The attacker seeks the minimum training set poisoning to attack the learned model. By using the KKT conditions of the learner's problem, the bilevel formulation is turned into a single level optimization problem.

# 8.2 Empirical Model Learning 

Empirical model learning (EML) aims to integrate machine learning models in combinatorial optimization in order to support decision-making in high-complexity systems through prescriptive analytics. This goes beyond

the traditional what-if approaches where a predictive model (e.g., a simulation model) is used to estimate the parameters of an optimization model. A general framework for an EML approach is provided in [159] and requires the following:

- A vector $\eta$ of $n$ decision variables $\eta_{i}$, with $\eta_{i}$ feasible over the domain $D_{i}$.
- A mathematical encoding $h$ of the Machine Learning model.
- A vector $z$ of observables obtained from $h$.
- Logical predicates $g_{j}(\eta, z)$ such as mathematical programming inequalities or combinatorial restrictions in constraint programming.
- A cost function $f(\eta, z)$.

EML then solves the following optimization problem

$$
\begin{aligned}
& \min f(\eta, z) \\
& \text { s.t. } g_{j}(\eta, z) \quad \forall j \in J \\
& z=h(\eta) \\
& \eta_{i} \in D_{i} \quad \forall i=1, \ldots, n
\end{aligned}
$$

The combinatorial structure of the problem is defined by (136), (137), and (139) while (138) embeds the empirical machine learning model in the combinatorial problem. Embedding techniques for neural networks and decision trees are presented in [159] using optimization approaches that include mixed integer nonlinear programming, constraint programming, and SAT Modulo Theories, and local search.

# 8.3 Bayesian Network Structure Learning 

Bayesian networks are a class of models that represent cause-effect relationships. These networks are learned by deriving the causal relationships from data. A Bayesian network is visually represented as a direct acyclic graph $G(N, E)$ where each of the nodes in $N$ corresponds to one variable and the edges $E$ are directional relations that indicate the cause and effect relationships among the variables. A conditional probability distribution is associated with every node/variables and along with the network structure expresses the conditional dependencies among all the variables. A main challenge in learning Bayesian networks is learning the network structure from the data. This is known as the Bayesian network structure learning problem. Finding the optimal Bayesian network structure is $\mathcal{N} \mathcal{P}$-hard [66]. Mixed integer programming formulations of the Bayesian network structure learning have been proposed [14] and solved by using relaxations [127], cutting planes $[16,52,78]$, and heuristics $[102,222]$.

The case of learning Bayesian network structures when the width of the tree is bounded by a small constant is computationally tractable [177, 179]. The bounded tree-width case is thus a restriction on the Bayesian network structure that limits the ability to represent exactly the underlying distribution of the data with the aim to achieve reasonable computational performance when computing the network structure. Following [177], to formulate the Bayesian network structure learning problem with a maximum tree-width $w$, the following binary variables are defined

$$
p_{i t}= \begin{cases}1 & \text { if } P_{i t} \text { is the parent set of node } i \\ 0 & \text { otherwise }\end{cases}
$$

where $i \in N$ and $P_{i t}$ is a parent set for node $i$. For each node $i$, the collection of parent sets is denoted as $P_{i}$ and is assumed to be available (i.e., enumerated beforehand). Thus $P_{i t} \in P_{i}$ with $t=1, \ldots, r_{i}$, and $r_{i}=\left|P_{i}\right|$ where $P_{i} \subset N$. Additional auxiliary variables $z_{i} \in[0,|N|], v_{i} \in[0,|N|]$ where $|N|$ denotes the number of nodes in $N$, and $y_{i j} \in\{0,1\}$ are introduced to enforce the tree-width and directed acyclic graph conditions. The problem is formulated as

$$
\begin{aligned}
& \max \sum_{i \in N} \sum_{t=1}^{r_{i}} p_{i t} s_{i}\left(P_{i t}\right) \\
& \text { s.t. } \sum_{j \in N} y_{i j} \leq w, \quad \forall i \in N \\
& \quad(|N|+1) y_{i j} \leq|N|+z_{j}-z_{i} \quad \forall i, j \in N
\end{aligned}
$$

$$
\begin{aligned}
& y_{i j}+y_{i k}-y_{j k}-y_{k j} \leq 1 \quad \forall i, j, k \in N \\
& \sum_{t=1}^{r_{i}} p_{i t}=1 \quad \forall i \in N \\
& (|N|+1) p_{i t} \leq|N|+v_{j}-v_{i} \quad \forall i \in N, \forall t=1, \ldots, r_{i}, \forall j \in P_{i t} \\
& p_{i t} \leq y_{i j}+y_{j i} \quad \forall i \in N, \forall t=1, \ldots, r_{i}, \forall j \in P_{i t} \\
& p_{i t} \leq y_{j k}+y_{k j} \quad \forall i \in N, \forall t=1, \ldots, r_{i}, \forall j, k \in P_{i t} \\
& z_{i} \in[0,|N|], v_{i} \in[0,|N|], y_{i j} \in\{0,1\}, p_{i t} \in\{0,1\} \quad \forall i, j \in N, \forall t=1, \ldots, r_{i}
\end{aligned}
$$

The objective function (140) maximizes the score of the acyclic graph where $s_{i}()$ is a score function that can be efficiently computed for every node $i \in N$ 52. Constraints (141)-(143) enforce a maximum tree-width $w$ while constraints (144)-(145) enforce the directed acyclic graph condition. Constraints (146)-(147) enforce the relationship between the $p$ and $y$ variables and finally constraints (148) set the variable bounds and binary conditions. Another formulation for the bounded tree-width problem has been proposed in 179 and includes an exponential number of constraints which are separated in a branch-and-cut framework. Both formulations however become computationally demanding as the number of features in the data set grows and with an increase in the tree-width limit. Several search heuristics have also been proposed as solution approaches $[177,176,190]$.

# 9 Conclusions 

Mathematical programming constitutes a fundamental aspect of many machine learning models where the training of these models is a large scale optimization problem. This paper surveyed a wide range of machine learning models namely regression, classification, clustering, and deep learning as well as the new emerging paradigms of machine teaching and empirical model learning. The important mathematical optimization models for expressing these machine learning models are presented and discussed. Exploiting the large scale optimization formulations and devising model specific solution approaches is an important line of research particularly benefiting from the maturity of commercial optimization software to solve the problems to optimality or to devise effective heuristics. However, as highlighted in [155, 184], providing quantitative performance bounds remains an open problem. The nonlinearity of the models, the associated uncertainty of the data, as well as the scale of the problems represent some of the very important and compelling challenges to the mathematical optimization community. Furthermore, bilevel formulations play a big role in adversarial learning [116], including adversarial training, data poisoning and neural network robustness.

Based on this survey, we summarize the distinctive features and the potential open machine learning problems that may benefit from the advances in computational optimization.

- Regression. The typical approaches to avoid overfitting and to handle uncertainty in the data include shrinkage methods and dimension reduction. These approaches can all be posed as mathematical programming models. General non-convex regularization to enforce sparsity without incurring shrinkage and bias (such as in lasso and ridge regularization) remain computationally challenging to solve to optimality. Investigating tighter relaxations and exact solution approaches continue to be an active line of research [7].
- Classification. Classification problems can also be naturally formulated as optimization problems. Support vector machines in particular have been well studied in the optimization literature. Similar to regression, classifier sparsity is one important approach to avoid overfitting. Additionally, exploiting the kernel tricks is key as nonlinear separators are obtained without additional complexity. However, when posed as an optimization problem, it is still unclear how to exploit kernel tricks in sparse SVM optimization models. Another advantage to express machine learning problems as optimization problems and in particular classification problems is to account for inaccuracies in the data. Handling data uncertainty is a deeply explored field in the optimization literature and several practical approaches have been presented to handle uncertainty through robust and stochastic optimization. Such advances in the optimization literature are currently being investigated to improve over the standard approaches 29.
- Clustering. Clustering problems are in general formulated as MINLPs that are hard to solve to optimality. The challenges include handling the non-convexity as well as the large scale instances which is a challenge even for linear variants such as the capacitated centred clustering (formulated as a binary

linear model). Especially for large-scale instances, heuristics are typically devised. Exact approaches for clustering received less attention in the literature.

- DNNs architectures as MIPs. The advantage of mathematical programming approaches to model DNNs has only been showcased for relatively small size data sets due to the scale of the underlying optimization model. Furthermore, expressing misclassification conditions for adversarial examples in a non-restrictive manner, and handling the uncertainty in the training data are open problems in this context.
- Adversarial learning and adversarial robustness. Optimization models for the search for adversarial examples are important to identify and subsequently protect against novel sets of attacks. The complexity of the mathematical models in this context is highly dependent on the the classifier function. Untargeted attacks received less attention in the literature, and the mathematical programming formulation (110)-(114) has been introduced in section 7.2. Furthermore, designing models robust to adversarial attacks is a two-player game, which can be cast as a bilevel optimization problem. The loss function adopted by the learner is one main complexity for the resulting mathematical model and solution approaches remain to be investigated.
- Data poisoning: Similar to adversarial robustness, defending against the poisoning of the training data is a two-player game. The case of online data retrieval is especially challenging for gradient-based algorithms as the KKT conditions do not hold.
- Activation ensembles. Activation ensembles seek a trade-off between the classifier accuracy and computational feasibility of training with a mathematical programming approach. Adopting activation ensembles to train large DNNs have not been investigated yet.
- Machine teaching. Posed as a bilevel optimization problem, one of the challenges in machine teaching is to devise computationally tractable single-level formulations that model the learner, the teaching risk, and the teaching cost. Machine teaching also generalizes a number of two-player games that are important in practice including data poisoning and adversarial training.
- Empirical model learning. This emerging paradigm can be seen as the bridge combining machine learning for parameter estimation and operations research for optimization. As such, theoretical and practical challenges remain to be investigated to propose prescriptive analytics models jointly combining learning and optimization in practical applications.

While this survey does not discuss numerical optimization techniques since they were recently reviewed in $[43,77,221]$, we note the fundamental role of the stochastic gradient algorithm [186] and its variants on large scale machine learning. We also highlight the potential impact of machine learning on advancing the solution approaches of mathematical programming $[95,96]$.

This survey has also focused on the learning process (loss minimization), however we note that challenging optimization problems also appear in the inference process, i.e., energy minimization (see [151] for a comprehensive survey). In the inference step, the best output $y^{*}$ is chosen from among all possible outputs given a certain input $x$ such that an "energy function" is minimized. The energy function provides a measure of the goodness of a particular configuration of the input and output variables. Energy optimization constitute a common framework for machine learning where the training of a model aims at finding the optimal energy function.

A key part of most machine learning approaches is the choice of the hyperparameters of the learning model. The Hyperparameter Optimization (HPO) is usually driven by the data scientist's experience and the characteristics of the dataset and typically follows heuristic rules or cross-validation approaches. Alternatively, the HPO problem can be modeled as a box-constrained mathematical optimization problem [83], or as a bilevel optimization problem as discussed in [98, 144, 171], which provides theoretical convergence guarantees in addition to computational advantage. Automated approaches for HPO are also an active area of research in Machine Learning [26, 92, 220].

Finally, since the recent widespread of machine learning to several research disciplines and in the mainstream industry can be largely attributed to the availability of data and the relatively easy to use libraries, we summarize in the online supplement the resources that may be of value for research.

# Acknowledgement 

We are very grateful to four anonymous referees for their valuable feedback and comments that helped improve the content and presentation of the paper. Joe Naoum-Sawaya was supported by NSERC Discovery Grant RGPIN-2017-03962 and Bissan Ghaddar was supported by NSERC Discovery Grant RGPIN-2017-04185.
