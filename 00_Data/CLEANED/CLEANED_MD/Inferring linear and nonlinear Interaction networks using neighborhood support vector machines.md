# Inferring linear and nonlinear Interaction networks using neighborhood support vector machines* 

Kamel Jebreen ${ }^{1,3}$ and Badih Ghattas ${ }^{2}$<br>${ }^{1}$ Institut de Mathématiques de Marseille, CNRS, UMR 7373, Aix Marseille<br>UniversityMarseille, France.<br>${ }^{2}$ Institut de Mathématiques de Marseille, CNRS, UMR 7373, Aix Marseille<br>UniversityMarseille, France.<br>${ }^{3}$ Department of Mathematics, An-Najah National University, Nablus, Palestine


#### Abstract

In this paper, we consider modelling interaction between a set of variables in the context of time series and high dimension. We suggest two approaches. The first is similar to the neighborhood lasso when the lasso model is replaced by a support vector machine (SVMs). The second is a restricted Bayesian network adapted for time series. We show the efficiency of our approaches by simulations using linear, nonlinear data set and a mixture of both.


Keywords: Temporal Data $\cdot$ Bayesian Networks $\cdot$ Variable Importance
Dynamic Bayesian Networks $\cdot$ Graphical Models.

## 1 Introduction

Modelling interactions between variables is a common task in statistics. This is often done using graphical models (18) where vertices correspond to variables and edges to the interaction between the corresponding variables. Such models may be inferred from data using different approaches. Among these approaches covariance graphs are the simplest as they infer the network applying a threshold to the estimated correlation matrix (5], [4]). Graphical Gaussian models (GGMs) (134|7), (118) consider rather partial correlations obtained from the inverse of the covariance matrix (129], [30]).

Bayesian networks (BN) ([12]) infer interactions by estimating the conditional independence between the variables based on a specific factorization of the joint probabilities of the variables. Recently, the neighborhood lasso (23]) and graphical lasso (111) suggest fitting a regression model for each variable using the others. A variable is connected in the graph to the set of its explanatory variables whose coefficient in the regression model are not zero.

These approaches have been extended to time series data. Dynamic Bayesian networks (DBN) (112) are such direct extension of Bayesian networks. For the

[^0]
[^0]:    * Supported by "HERMES" project, Erasmus Mundus European programme, action 2, Marseilles, France.

neighborhood lasso, a variable $X$ at time point $t+1$ is regressed on all the variables observed at the previous time point $t$.

In this work, we suggest first a similar approach to neighborhood lasso replacing the lasso model by SVM where the subset of variables used for each regression is obtained by a feature selection approach. We experiment also a static restricted Bayesian network for time series data.

This work is organized as follows. Section 2 gives a brief introduction to graphical models for time series. Section 3 describes our approaches. Finally, Section 4 is dedicated to simulations and results.
![img-0.jpeg](img-0.jpeg)

Fig. 1. Graphical representation of a time varying dynamic Bayesian network.

# 2 Graphical models for time series 

In this section, we give a brief summary of recent works on graphical models for time series. Let $\mathbf{X}(t)=\left(X_{1}(t), \ldots, X_{p}(t)\right)$ be a vectorial real p-dimensional Gaussian process observed at time $t=1, \ldots, n . \mathbf{X}(t)$ is assumed to follow a normal distribution $\mathcal{N}(\mu, \Sigma)$, where $\mu$ is the mean vector and $\Sigma$ is the covariance matrix. All the approaches described in this section make the following assumption: Firstly, we assume that $\mathbf{X}$ is first order Markovian, that is

$$
P(X(t+1) \mid X(1), \ldots, X(t))=P(X(t+1) \mid X(t))
$$

this means that the variables $\mathbf{X}(t+1)$ depend only on the past variables $\mathbf{X}(t)$. Secondly, we assume that the process is stationary, that is

$$
P(X(t+1) \mid X(t)) \text { is independent of } t
$$

Thirdly, the variables observed at a same time are conditionally independent given the others in the past time, that is

$$
X_{i}(t) \perp X_{j}(t) \mid \mathbf{X}\left(t^{\prime}<t\right) \quad \text { where } i \neq j, t, t^{\prime} \geq 1
$$

These assumptions ensure the existence of a directed acyclic graph (DAG) $G=(\mathbf{X}(t), E(G))$, where $\mathbf{X}(t)$ is the set of variables or nodes and $E(G) \subseteq$ $(\mathbf{X}(t) \times \mathbf{X}(t))$ is the set of edges. Then, a Bayesian network corresponds to the following representation of the joint distribution of $\mathbf{X}$

$$
f(\mathbf{X}(t))=\prod_{j=1}^{p} \prod_{t=1}^{n} f\left(X_{j}(t) \mid P a\left(X_{j}(t), G\right)\right)
$$

where $P a\left(X_{j}(t), G\right)$ is the set of parents of $X_{j}(t)$ in the graph $G$.

# 2.1 Dynamic Bayesian networks (DBN) 

Friedman et.al. ([12]) suggests two parts to model the process $\mathbf{X}(t)$ using DBN. The first is a prior network $B_{0}$ that determines the distribution of the initial states $\mathbf{X}(1)$, and the second is a transition network $B_{\rightarrow}$ which determines the transition probability $P(X(t+1) \mid X(t))$ for all $t$. That is

$$
P_{B_{\rightarrow}}(\mathbf{X}(1), \ldots, \mathbf{X}(n))=P_{B_{0}}(\mathbf{X}(1)) \prod_{t=1}^{n-1} P_{B_{\rightarrow}}(\mathbf{X}(t+1) \mid \mathbf{X}(t))
$$

The structure of a DBN is optimized using Bayesian Information Criterion $(B I C)$ score defined as follows

$$
B I C(\mathbf{X}(t), G)=B I C_{0}+B I C_{\rightarrow B}
$$

such that,

$$
B I C(\mathbf{X}(t), G)=\sum_{j=1}^{p} \log \hat{f}\left(X_{j}(t+1) \mid X_{j}(t)\right)-\frac{L}{2} \log n
$$

where $B I C_{0}$ is the $B I C$ score of the prior network $B_{0}, B I C_{\rightarrow B}$ is the $B I C$ score for the transition network $B_{\rightarrow}, L$ is the number of parameters in $G$ and $\hat{f}\left(X_{j}(t+1) \mid X_{j}(t)\right)$ is the local conditional distribution for each variable.

The next approaches are based on the covariance matrix estimation.

### 2.2 Least Angle Absolute Shrinkage and Selection Operator (Lasso)

Meinshausen and Bühlmann ([23]) used the Lasso approach ([32]) for inferring the concentration matrix which is the inverse covariance matrix. They apply the lasso regression for each variable as a response variable given the others. That is, fit the variable $X_{j}(t+1)$ at time point $t+1$ over all variables $\mathbf{X}(t)$ at the previous time point $t$ for all $j=1, \ldots, p$, and the coefficients of the regression are given by

$$
\hat{\beta}^{j, \lambda}=\underset{\beta: \beta_{j}=0}{\operatorname{argmin}}\left[\frac{\left\|X_{j}(t+1)-\beta \mathbf{X}(t)\right\|_{2}^{2}}{n}+\lambda\|\beta\|_{1}\right]
$$

The models regressing $X_{i}$ over $X_{j}$ and $X_{j}$ over $X_{i}$ may have zero or nonzero coefficients giving opposite information about the correlation of these variables. This is the symmetrization problem solved by applying "And" or "or" operations over such connections.

Friedman et.al. ([11]) suggest the graphical lasso model regression, Glasso, as improvement of the neighborhood lasso reducing the cost of the computation mainly for high dimensional problems.

# 2.3 Shrinkage approach (Genenet) 

Making the assumption that $\mathbf{X}(t)$ follows a VAR process, Schäfer and Strimmer ([31]) suggest to estimate the partial correlation matrix using a James Stein type shrinkage estimator ([8]). This estimator is much more efficient when compared to least square or maximum likelihood estimates mainly when the sample size is lower than the dimension; $n<p$.

### 2.4 First order conditional dependence graph (G1DBN)

Lèbre ([20]) proposed an approach which proceeds using two steps. The first aims to estimate the adjacency matrix with a reduced number of edges. Conditional Partial correlation of variables $X_{i}$ and $X_{j}$ over $X_{k}, i, j, k=1, \ldots, p$ where $k \neq j$, are computed together with their $p$-values $p_{i j \mid k}$; the maximal over $k$ is kept giving a score matrix $S_{i j}=\max _{k} p_{i j \mid k}$. A first graph is obtained applying a threshold $\alpha_{1}$ to these scores. The second step changes the score matrix using $p$-values of significance testing of linear regression coefficients over a restricted subset of variables (those whose initial score are nonzero).

### 2.5 Statistical Inference for Modular Networks, SIMoNe

Ambroise et.al. ()[2]) suggest an algorithm called SIMoNe (Statistical Inference for Modular Networks) to estimate the nonzero entries of the concentration matrix which is equivalent to reconstructing the Gaussian graphical model. They assume a latent structure on the concentration matrix which is equivalent to a hidden structure over the network (whose edges weighs correspond to the entries of the concentration matrix). Finally, they use an EM algorithm together with a $\ell_{1}$ norm to get the concentration matrix estimate.

Other approaches based in mutual information criterion were also proposed, for details see ( $[1,3,9,24,26,28])$.

## 3 Our approaches

We propose two new approaches for inferring dynamic graphical networks: neighborhood SVM (nSVM) and restricted Bayesian networks (RBN). Support vector machines ([33]) may be used for regression and share many features with the classification version.

Suppose we have training data set $D=\left\{\left(x_{1}, y_{1}\right), \ldots,\left(x_{n}, y_{n}\right)\right\} \subset \mathcal{R}^{p} \times \mathcal{R}, p \geq$ 1. In epsilon SVM regression $(\epsilon-S V M)$ we aim to estimate a function $f(x)$ that has at most $\epsilon$ deviation from the actual targets $y_{i}$ for all the training data. Let

$$
f(x)=<w, x>+b, \quad w \in \mathcal{R}^{p}, b \in \mathcal{R}
$$

$\epsilon$-SVM solve the following optimization problem:

$$
\begin{aligned}
& \operatorname{minimize} \quad \frac{1}{2}\|w\|^{2}+C \sum_{i=1}^{n}\left(\zeta_{i}+\zeta_{i}^{*}\right) \\
& \text { subject to } \begin{cases}y_{i}-<w, x_{i}>-b \leq \epsilon+\zeta_{i} \\
<w, x_{i}>+b-y_{i} \leq \epsilon+\zeta_{i}^{*} \\
\zeta_{i}, \zeta_{i}^{*} \geq 0\end{cases}
\end{aligned}
$$

where $C>0$ is a constant that controls the penalty imposed on observations which lie outside the $\epsilon$ margin and prevent overfitting and $\zeta_{i}, \zeta_{i}^{*}$ are slack variables controlling the relaxation of the constraints. The linear $\epsilon$-insensitive loss function ignores errors that are within $\epsilon$ distance of the observed value by treating them as equal to zero. The loss function is a measure based on the distance between observed value $y$ and the $\epsilon$ boundary:

$$
L_{\epsilon}= \begin{cases}0, & |y-f(x)| \leq \epsilon \\ |y-f(x)|-\epsilon, & \text { otherwise }\end{cases}
$$

Solving the optimization problem (10) is done by solving its Lagrange dual formulation ( $[10,21,22])$ and it gives:

$$
\begin{aligned}
w & =\sum_{i=1}^{n}\left(\alpha_{i}-\alpha_{i}^{*}\right) x_{i} \\
f(x) & =\sum_{i=1}^{n}\left(\alpha_{i}-\alpha_{i}^{*}\right)<x_{i}, x>+b
\end{aligned}
$$

where $\alpha_{i}$ and $\alpha_{i}^{*}$ are the Lagrange multipliers. The constant $b$ can be computed by the so called Karush Kuhn Tucker (KKT) conditions ( $[17,16]$ ).

So, $w$ can be completely described as a linear combination of the training patterns $x_{i}$ and the complexity of a function's representation by support vectors. Also, it depends on the number of support vectors but not on the dimension $p$.

In case of nonlinear SVMs the Lagrange dual formulation is extended to a nonlinear function. Nonlinear SVM regression model can be obtained by replacing the dot product term $\left\langle x_{j}, x\right\rangle=x_{j}^{T} x$ with a nonlinear kernel function $K\left(x_{1}, x_{2}\right)=\left\langle\phi\left(x_{1}\right), \phi\left(x_{2}\right)\right\rangle$, where $\phi(x)$ is a transformation that maps $x$ to a high dimensional space. The common kernels are

$$
K\left(x_{i}, x_{j}\right)= \begin{cases}\text { Polynomial kerel }=\left(k^{*}<x_{i}, x_{j}>+\text { const }\right)^{d} \\ \text { Gaussian radial basis function }=e^{-k^{*}\left\|x_{i}-x_{j}\right\|^{2}} \\ \text { Sigmod kernel }=\tanh \left(k^{*}<x_{i}, x_{j}>+\text { const }\right)\end{cases}
$$

where $k^{*}$ is the kernel parameter, $d$ is the degree of the polynomial kernel and const is a random constant.
![img-1.jpeg](img-1.jpeg)

Fig. 2. Linear simulation: position of approaches with respect to TPR and TNR for $p=50,100$ and $n=20$.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Nonlinear simulation: position of approaches with respect to TPR and TNR for $p=50,100$ and $n=20$.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Mixed simulation: position of approaches with respect to TPR and TNR for $p=50,100$ and $n=20$.

# 3.1 Neighborhood Support vector machine, nSVM 

Following the idea of neighborhood lasso we suggest here a procedure based on $p$ SVM regression models where each variable observed at time $t+1$ plays the role of the output and the other variables observed at time $t$ are used as input variables. The difference with neighborhood lasso is that feature selection step is done separately. For each regression model, the optimal subset of input variables to keep is selected by a stepwise kind procedure. First, input variables

are ranked according to their decreasing order of importance. The importance of variable $X_{j}$ based on SVM is computed using $\|w\|^{(-j)},\left([6,27,35,19]\right)$ which is the norm of the weight vector omitting its $j$ th coordinate. Once the input variables are ordered, we construct a sequence of embedded models beginning with the most important variable, and adding the others one by one ([14]). The mean square error (MSE) of each model is computed by leave one out cross validation (LOOCV). The model minimizing the MSE corresponds to the best subset selection of input variables, thus the optimal neighbor. The algorithm is summarized in algorithm 1.

```
Algorithm 1 Neighborhood Support vector machine algorithm.
    Let \(D\) be a data set; \(p\) is the number of features, error and Error be vectors of
    MSE with length \(p\);
    for ( \(\mathrm{j}=1: \mathrm{p}\) ) do
        Build a SVM model \(f\) for each response variable \(X_{j}(t+1)\) and predictor variables
        \(\mathbf{X}(t)\);
        compute the variable importance (VI) with respect to the SVM model;
        Sort the variables according to their descending order of importance:
        \(X^{(1)}(t), \ldots, X^{(p)}(t)\);
        Partition \(D\) using LOOCV and let \(D_{-i}=D \backslash D_{i}\);
        Initialize Error \(=0\)
        for ( \(\mathrm{i}=1: \mathrm{n})\) do
            for \((\mathrm{k}=1: \mathrm{p})\) do
                \(M_{i}^{k}=f(\operatorname{response}=X_{j}(t+1)\), predictors \(=X^{(1)}(t), \ldots, X^{(k)}(t), D_{-i})\);
                \(\operatorname{error}_{i}^{k}=\operatorname{Test}\left(M_{i}^{k}, D_{i}\right)\);
            end for
            Error \(=\) Error + error \(_{i}\);
        end for
        Error \(=\frac{1}{n}\) Error;
        kopt \(=\underset{k}{\operatorname{argmin}}\{\operatorname{Error}\}\), where kopt is the optimal number of important vari-
   ables to keep in the model.
    end for
```


# 3.2 Restricted Bayesian Networks (RBN) 

Our idea here is to use the classical static Bayesian network approach augmenting the data set by adding one time shift for each variable. Thus we built a Bayesian network over the set of $2 p$ variables $\left(X_{1}(t+1), \ldots, X_{p}(t+1), X_{1}(t), \ldots, X_{p}(t)\right)$ constraining the network to satisfy the assumptions given in section 2. Figure 1 illustrates these restrictions. There are no dependencies within each time and arcs between times are only in one direction $(t+1 \rightarrow t)$. Besides, the graph is acyclic.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Restricted dynamic Bayesian network, RDBN.

# 4 Experiments 

In this section we suggest three different simulation models for linear time series, nonlinear and a mixture of both.

### 4.1 Simulation models

For the linear time series simulation we use a first order vector autoregressive model $(\operatorname{VAR}(1))$

$$
X_{j}(t+1)=A \mathbf{X}(\mathbf{t})+B+\epsilon_{j}, j=1, \ldots, p
$$

where, $t=1, . ., n, \mathbf{X}(\mathbf{t}) \in \mathcal{R}^{p}$ and $\epsilon_{j} \sim \mathcal{N}\left(0, \sigma^{2}\right)$. The matrix $A_{p \times p}$ represents the true network structure. Its elements are chosen uniformly fixing the true edges proportion $p i \in(0,1)$ of non zeros entries. The vector $B$ of intercepts is also chosen uniformly. Details are given in algorithm 2, ([20,25]).

For nonlinear time series, we follow the simulation scheme given in ([13]) and use the following transformations

$$
\left\{\begin{array}{l}
f_{1}(X(t+1))=\sin (X(t)) \\
f_{2}(X(t+1))=\cos (X(t)) \\
f_{3}(X(t+1))=\sqrt[3]{X^{2}(t)}-2^{\sin (X(t))}
\end{array}\right.
$$

The initial values $X(1) \in \mathcal{R}^{p}$ are drawn randomly using standard Gaussian distribution with zero mean and variance $\sigma^{2}$.

The $p$ nonlinear functions are drawn randomly from the above transformations (equation 16) and applied to each dimension of $\mathbf{X}$ at time $t$. A matrix $A$ generated like in the linear case is applied after the nonlinear transformation. The process is described in algorithm 3 .

To mix the linear and nonlinear simulation we use this set of transformations

$$
\left\{\begin{array}{l}
f_{4}(X(t+1))=\sin (X(t)) \\
f_{5}(X(t+1))=\frac{1}{2} X(t) \\
f_{6}(X(t+1))=\sqrt[3]{X^{2}(t)}-2^{\sin (X(t))} \\
f_{7}(X(t+1))=-0.8 X(t)
\end{array}\right.
$$

and we proceed exactly like for the nonlinear case.
To test the performance of our approaches we compared the efficiency of neighborhood support vector machines approach (nSVM) and restricted Bayesian networks approach (RBN) with first order dependencies approach (G1DBN) ([20]), shrinkage to large scale covariance matrix estimation approach ([31,25]) (Genenet) and neighborhood lasso approach (nlasso) ([23]). Support vector machines depend on two parameters $k^{*}$ and $C=$ cost which are the kernel parameter and the constant of regularization in the Lagrange formulation respectively. These parameters are tuned and compared with their default values, $k^{*}=1 / p$ and $C=1$ to choose the best performance ([15]). The range of $k^{*}$ and $C$ are chosen respectively to be from $10^{-6}$ to $10^{-1}$ and from $10^{1}$ from $10^{6}$. Also, for polynomial kernel, the parameter $d$ is tuned to choose the best degree within $d=\{1, . ., 5\}$.

```
Algorithm 2 Simulation of linear networks
    Let \(X=\operatorname{Zero}_{p \times n}\) be the \(p\)-dimensional time series initialized to zero; \(n\) the number
        of instances; \(p i \in(0,1)\) the true edges proportion; \(A=\operatorname{Zero}_{p \times p}\) the adjacency
        matrix that represents the simulated graph (initialized to zero); \(B\) the intercept
        term; \(\epsilon_{i}\) a white noise with zero mean and variance equal to \(\sigma^{2} ;\) and nEdges the
        number of nonzero edges in the network;
    nEdges \(=\left\lfloor p^{2} \times p i\right\rfloor\);
    Select randomly the nonzero edges in \(A\) from \(p^{2}\) edges;
    Fill the nonzero edges in \(A=<a_{i j}>\) uniformly;
    Define the true network
```

```
Tnet \(=\left\{\begin{array}{l}1, i f a_{i j} \neq 0 \\ 0, i f a_{i j}=0\end{array}\right. \);
```

6: Draw the intercept term $B$ and the variance $\sigma^{2}$ uniformly;
7: Draw the initial value $X[, 1]$ normally with zero mean and variance equal to $\sigma^{2}$;
8: for $(\downarrow=2: n)$ do
$X[, i]=A X[, i-1]+B+\epsilon_{i}, ; \quad$ where $\epsilon_{i} \sim \mathcal{N}\left(0, \sigma^{2}\right)$
9: end for
10: $X^{T}$ is the simulated times series.

# 4.2 Results 

We compare the different approaches described above; $G 1(S 1$ and $S 2)$ which correspond to the two steps of G1DBN approach, neighborhood lasso (nlasso) approach, the Genenet approach with our approaches Restricted Bayesian network approach (RBN) and neighborhood SVM approach with different kernels; linear (L), radial (R), sigmod (S), and polynomial (P).

For these comparisons we compute the true positive rate (TPR), false positive rate(FPR), true negative rate (TNR) and false negative rate (FNR) defined in equation 20 and average their values over 100 runs.

```
Algorithm 3 Simulation of nonlinear and mixture networks
    Let \(X=\operatorname{Zero}_{p \times n}\) be the \(p\)-dimensional time series initialized to zero; \(n\) the number
    of instances; \(p i \in(0,1)\) the true edges proportion; \(A=\operatorname{Zero}_{p \times p}\) the adjacency
    matrix that represents the simulated graph ( initialized to zero); \(\epsilon_{i}\) a white noise
    with zero mean and variance equal to \(\sigma^{2} ;\) and nEdges the number of nonzero edges
    in the network;
    nEdges \(=\left\lfloor p^{2} \times p i\right\rfloor\);
    Select randomly the nonzero edges in \(A\) from \(p^{2}\) edges;
    Fill the nonzero edges in \(A=<a_{i j}>\) uniformly;
    Define the true network
```

\[

\]

6: Choose the transformation function $f_{j}$ randomly from equation 16 or equation 17 for each variable;
7: Draw the initial value $X[, 1]$ normally with zero mean and random variance and set $X[, 1]=2 \times \sin (X[, 1])$;
8: for ( $\mathbf{i}=2: \mathrm{n}$ ) do
9: for $(\mathrm{j}=1: \mathrm{p})$ do
$X[j, i]=f_{j}(X[j, i-1])$
10: end for
$X[, i]=A \times X[, i]+\epsilon_{i} ; \quad$ where $\epsilon_{i} \sim\left(0, \sigma^{2}\right)$
11: end for
12: $X^{T}$ is the simulated times series.

Table 1, 2 and 3 present the results for the linear, nonlinear and mixture cases respectively for two values of $\mathrm{p}(p=50, p=100)$ and $n$ being fixed to 20 .

As expected in all cases the performances decrease for high dimensions ( $p=$ 100) and quite good for all the methods in the linear case. The worst performance for all the methods is observed in the nonlinear case. Given the low rate (5\%) of edges present in the true network, the hardest task is to retrieve these edges thus to get high TPRs. High values of TNR are quite easy to achieve and correspond systematically to low values of the misclassification error (MCE) rates.

The nSVM is the only approach where TPR is above $50 \%$. As there is no global index to measure the fair performances of these approaches we try in general to have a good trade-off between TPR and TNR.

Figures 2, 3, and 4 show the position of the approaches we have compared in the space (TPR-TNR).

For the linear results, table 1 shows that the average number of edges which are correctly included into the estimate of the edges set is high in nSVM-S, nlasso, nSVM-L, nSVM-R and RBN respectively when $p=50$. These highly average


Table 1. Linear simulated data, $\mathrm{p}=50,100, \mathrm{n}=20, \mathrm{pi}=0.05$, the last four columns correspond to the neighborhood SVM approach (nSVM) using different kernels (L: Linear, R: Radial, S: Sigmod, P: Polynomial).
values correspond also to high average values of edges which are correctly not included into the estimate of the edges set and to low average values of MCE, this is obvious from points in the upper right-hand side square in figure 2 with red color.

When $p=100$, the average number of edges which are correctly included and not include into the estimate of the edges set breaks down in RBN approach and be out of performance, but still significant in nSVM-S, nSVM-L, nSVM-R and nlasso respectively, See the blue points in the upper right hand side square in figure 2 .

In nonlinear simulation, nSVM still gives the highly significant results in both cases when $p=50$ or $p=100$. Note that the average number of edges which are correctly included and not included into the estimate of the edge set when $p=50$ is high and closed its corresponds one when $p=100$ in nSVM with sigmod kernel which shows the stability of the results that are a function of the number of variables $p$. See the red and blue points in the upper right-hand side square in figure 3 .

In table 3 which is the simulated results of mixture linear and nonlinear time series data, nSVM approach also gives highly significant results in both cases of different number of variables, especially in nSVM-S. On the other side, RBN and G1-S1 break down when the number of variables increases. See the red and blue points in the upper right-hand side square in figure 4.

In all the simulations the MCE decreases as the number of variables increase. Moreover, nSVM approach especially SVM-S shows the best performance in finding the most correctly edges that include into the estimate of the edges set. RBN sensitives to the linearity assumption and the number of variables especially when it is higher than the number of instances, this due to the likelihood function that used to estimate the network.


Table 2. Noninear simulated data, $\mathrm{p}=50,100, \mathrm{n}=20, \mathrm{pi}=0.05$, the last four columns correspond to the neighborhood SVM approach (nSVM) using different kernels (L: Linear, R: Radial, S: Sigmod, P: Polynomial).


Table 3. Linear and nonlinear simulated data, $\mathrm{p}=50,100, \mathrm{n}=20, \mathrm{pi}=0.05$, the last four columns correspond to the neighborhood SVM approach (nSVM) using different kernels (L: Linear, R: Radial, S: Sigmod, P: Polynomial).

# 5 Conclusion 

SVM criterion is an efficient approach to find the interaction points to approximate the structure of the data sets. The ability to use different types of kernels allow SVMs to find the best active sets that construct the model according to the types of the input data. Also, SVM is not sensitive too much to the number of variables inserted as we shown in nSVM-S. Further work is to apply these results to gene expression data and compare it with approximate true structures.

# Acknowledgment 

The authors are grateful to "HERMES" project, Erasmus Mundus European programme, action 2, Marseilles, France, for the financial support during his study.
