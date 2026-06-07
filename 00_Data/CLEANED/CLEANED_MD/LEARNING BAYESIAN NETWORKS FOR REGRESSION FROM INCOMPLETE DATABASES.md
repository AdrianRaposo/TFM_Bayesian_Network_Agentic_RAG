# PREPRINT 

## LEARNING BAYESIAN NETWORKS FOR REGRESSION FROM INCOMPLETE DATABASES

## Cite as:

- A. Fernández, J.D. Nielsen, A. Salmerón. Learning Bayesian networks for regression from incomplete databases. International Journal of Uncertainty, Fuzziness and Knowledge-based Systems (to appear).

# LEARNING BAYESIAN NETWORKS FOR REGRESSION FROM INCOMPLETE DATABASES* 

Antonio Fernández<br>Department of Statistics and Applied Mathematics<br>University of Almería<br>04120 Almería, Spain<br>afalvares@ual.es<br>Jens D. Nielsen<br>Computer Science Department<br>University of Castilla-La Mancha<br>02071 Albacete, Spain<br>dalgaard@dsi.uclm.es<br>Antonio Salmerón<br>Department of Statistics and Applied Mathematics<br>University of Almería<br>04120 Almería, Spain<br>antonio.salmeron@ual.es

Received (received date)
Revised (revised date)

In this paper we address the problem of inducing Bayesian network models for regression from incomplete databases. We use mixtures of truncated exponentials (MTEs) to represent the joint distribution in the induced networks. We consider two particular Bayesian network structures, the so-called naïve Bayes and TAN, which have been successfully used as regression models when learning from complete data. We propose an iterative procedure for inducing the models, based on a variation of the data augmentation method in which the missing values of the explanatory variables are filled by simulating from their posterior distributions, while the missing values of the response variable are generated using the conditional expectation of the response given the explanatory variables. We also consider the refinement of the regression models by using variable selection and bias reduction. We illustrate through a set of experiments with various databases the performance of the proposed algorithms.

Keywords: Bayesian networks, regression, mixtures of truncated exponentials, missing data

[^0]
[^0]:    *This work has been supported by the Spanish Ministry of Science and Innovation, through projects TIN2007-67418-C03-01,02 and by EFRD funds. A preliminary version of this work was presented at the PGM'08 workshop.

# 1. Introduction 

Mixtures of truncated exponentials (MTEs) ${ }^{18}$ are receiving increasing attention in the literature, as a tool for handling hybrid Bayesian networks, as they are compatible with standard inference algorithms and no restriction on the structure of the network is imposed. ${ }^{3,17,24}$ Recently, MTEs have also been successfully applied to regression problems considering different underlying network structures ${ }^{8,9,20}$ obtained from complete databases. In a previous preliminary work ${ }^{10}$ we approached the problem of inducing Bayesian networks for regression from incomplete databases by using an iterative algorithm for constructing naïve Bayes regression models. The algorithm was based on a variation of the data augmentation method ${ }^{27}$ in which the missing values of the explanatory variables are filled by simulating from their posterior distributions, while the missing values of the response variable are filled with its conditional expectation given the explanatory variables. In this paper we extend the above mentioned method to obtain networks with TAN ${ }^{12}$ structures. Also, the algorithm is extended to incorporate variable selection. Finally, we introduce a method for reducing the bias in the predictions that can be used in all the models, regardless they have been induced from complete or incomplete databases.

## 2. The MTE model

We denote random variables by capital letters, and their values by lowercase letters. We use boldfaced characters to represent random vectors and their values. The support of the variable $\mathbf{X}$ is denoted by $\Omega_{\mathbf{X}}$. A potential of class MTE is defined as follows: ${ }^{18}$

Definition 1. (MTE potential) Let $\mathbf{X}$ be a mixed $n$-dimensional random vector. Let $\mathbf{W}=\left(W_{1}, \ldots, W_{d}\right)$ and $\mathbf{Z}=\left(Z_{1}, \ldots, Z_{c}\right)$ be the discrete and continuous parts of $\mathbf{X}$, respectively, with $c+d=n$. We say that a function $f: \Omega_{\mathbf{X}} \mapsto \mathbb{R}_{0}^{+}$is a Mixture of Truncated Exponentials potential (MTE potential) if for each fixed value $\mathbf{w} \in \Omega_{\mathbf{W}}$ of the discrete variables $\mathbf{W}$, the potential over the continuous variables $\mathbf{Z}$ is defined as:

$$
f(\mathbf{w}, \mathbf{z})=a_{0}+\sum_{i=1}^{m} a_{i} \exp \left\{\sum_{j=1}^{c} b_{i}^{(j)} z_{j}\right\}
$$

for all $\mathbf{z} \in \Omega_{\mathbf{Z}}$, where $a_{i}, i=0, \ldots, m$ and $b_{i}^{(j)}, i=1, \ldots, m, j=1, \ldots, c$ are real numbers. We also say that $f$ is an MTE potential if there is a partition $D_{1}, \ldots, D_{k}$ of $\Omega_{\mathbf{Z}}$ into hypercubes and in each $D_{i}, f$ is defined as in Eq. (1).

Definition 2. (MTE density) An MTE potential $f$ is an MTE density if

$$
\sum_{\mathbf{w} \in \Omega_{\mathbf{w}}} \int_{\Omega_{\mathbf{Z}}} f(\mathbf{w}, \mathbf{z}) d \mathbf{z}=1
$$

A conditional MTE density can be specified by dividing the domain of the conditioning variables and specifying an MTE density for the dependent variable for each configuration of splits of the conditioning variables. ${ }^{18,19}$

Example 1. Consider two continuous variables $X$ and $Y$. A possible conditional MTE density for $Y$ given $X$ is the following:

$$
f(y \mid x)= \begin{cases}1.26-1.15 e^{0.006 y} & \text { if } 0.4 \leq x<5,0 \leq y<13 \\ 1.18-1.16 e^{0.0002 y} & \text { if } 0.4 \leq x<5,13 \leq y<43 \\ 0.07-0.03 e^{-0.4 y}+0.0001 e^{0.0004 y} & \text { if } 5 \leq x<19,0 \leq y<5 \\ -0.99+1.03 e^{0.001 y} & \text { if } 5 \leq x<19,5 \leq y<43\end{cases}
$$

# 3. Regression using MTEs 

Assume we have a set of variables $Y, X_{1}, \ldots, X_{n}$, where $Y$ is continuous and the rest are either discrete or continuous. Regression analysis consists of finding a model $g$ that explains the response variable $Y$ in terms of the explanatory variables $X_{1}, \ldots, X_{n}$, so that given an assignment of the explanatory variables, $x_{1}, \ldots, x_{n}$, a prediction about $Y$ can be obtained as $\hat{y}=g\left(x_{1}, \ldots, x_{n}\right)$. Previous works on regression using MTEs ${ }^{8,9,20}$ proceed by representing the joint distribution of $Y, X_{1}, \ldots, X_{n}$ as a Bayesian network, and then using the posterior distribution of $Y$ given $X_{1}, \ldots, X_{n}$ (more precisely, its expectation) to obtain a prediction for $Y$. The learning procedure consists of fixing the structure and afterwards learning the parameters of the corresponding conditional densities using a procedure based on least squares estimation. ${ }^{25}$
![img-0.jpeg](img-0.jpeg)

Fig. 1. Naïve Bayes structure for regression. The explanatory variables are assumed to be independent given the response variable $Y$.

In this paper we will focus on two particular Bayesian network structures, the so-called naïve Bayes (NB) and Tree Augmented Naïve Bayes (TAN). The NB ${ }^{6}$ structure is an extreme case in which all the explanatory variables are considered independent given the response variable. This kind of structure is represented in figure 1. The reason to make the strong independence assumption behind NB models is that it is compensated by the reduction in the number of parameters to be

![img-1.jpeg](img-1.jpeg)

Fig. 2. A TAN structure for regression. Some more dependencies among the explanatory variables are allowed.
estimated from data, since in this case, it holds that the conditional distribution of the response variable can be factorised as

$$
f\left(y \mid x_{1}, \ldots, x_{n}\right)=f(y) \prod_{i=1}^{n} f\left(x_{i} \mid y\right)
$$

which means that, instead of one conditional density over a large domain ( $n+1$ variables), $n$ conditional densities over a smaller domain ( 2 variables) are estimated.

The $\mathrm{TAN}^{12}$ represents a compromise between the strong independence assumption and the complexity of the model to be estimated from data. In this kind of models, additional dependencies are allowed, expanding the NB structure so that the subgraph over the explanatory variables is a directed rooted tree (see figure 2).

# 3.1. Constructing a regression model from incomplete data 

As we use the conditional expectation of the response variable given the observed explanatory variables, our regression model will be

$$
\hat{y}=g\left(x_{1}, \ldots, x_{n}\right)=E\left[Y \mid x_{1}, \ldots, x_{n}\right]=\int_{\Omega_{Y}} y f\left(y \mid x_{1}, \ldots, x_{n}\right) d y
$$

where $f\left(y \mid x_{1}, \ldots, x_{n}\right)$ is the conditional density of $Y$ given $x_{1}, \ldots, x_{n}$, which we assume to be of class MTE.

A conditional distribution of class MTE can be represented as in Eq. (2), where actually a marginal density is given for each element of the partition of the support of the variables involved. It means that, in each of the four regions depicted in Eq. (2), the distribution of the response variable $Y$ is independent of the explanatory variables. Therefore, from the point of view of regression, the distribution for the response variable $Y$ given an element in a partition of the domain of the explanatory variables $X_{1}, \ldots, X_{n}$, can be regarded as an approximation of the true distribution of the actual values of $Y$ for each possible assignment of the explanatory variables in that region of the partition. This fact justifies the selection of $E\left[Y \mid x_{1}, \ldots, x_{n}\right]$ as the predicted value for the regression problem, because that value is the one that best represents all the possible values of $Y$ for that region, in the sense that it

minimises the mean squared error between the actual value of $Y$ and its predictions $\hat{y}$, namely

$$
\text { mse }=\int_{\Omega_{Y}}(y-\hat{y})^{2} f\left(y \mid x_{1}, \ldots, x_{n}\right) d y
$$

which is known to be minimised for $\hat{y}=E\left[Y \mid x_{1}, \ldots, x_{n}\right]$. Thus, the key point to find a regression model of this kind is to obtain a good estimation of the distribution of $Y$ for each region of values of the explanatory variables. The original NB and TAN models ${ }^{8,20}$ estimate that distribution by fitting a kernel density to the sample and then obtaining an MTE density from the kernel using least squares. ${ }^{19,25}$ Obtaining such an estimation is more difficult in the presence of missing values. The first approach to estimating MTE distributions from incomplete data was developed in the more restricted setting of unsupervised data clustering. ${ }^{14}$ In that case, the only missing values are on the class variable, which is hidden, while the data about the features are complete.

Here we are interested in problems where the missing values can appear in the response variable as well as in the explanatory variables. A first approach to solve this problem could be to apply the EM algorithm, ${ }^{4}$ which is a commonly used tool in semi-supervised learning. ${ }^{2}$ However, the application of this methodology is problematic because the likelihood function for the MTE model cannot be optimised in an exact way. ${ }^{16,25}$

Another way of approaching problems with missing values is the so-called data augmentation (DA) algorithm. ${ }^{27}$ The advantage with respect to the EM algorithm is that DA does not require a direct optimisation of the likelihood function. Instead, it is based on imputing the missing values by simulating from the posterior distribution of the missing variables, which is iteratively improved from an initial estimation based on a random imputation. The DA algorithm leads to an approximation of the maximum likelihood estimates of the parameters of the model, as long as the parameters are estimated by maximum likelihood from the complete database in each iteration. As maximum likelihood estimates cannot be found in an exact way, we have chosen to use least squares estimation, as in the original NB and TAN regression models.

Furthermore, as our main goal is to obtain an accurate model for predicting the response variable $Y$, we propose to modify the DA algorithm in connection to the imputation of missing values of $Y$. The next proposition is the key on how to proceed in this direction.

Proposition 1. Let $Y$ and $Y_{S}$ be two continuous independent and identically distributed random variables. Then,

$$
E\left[\left(Y-Y_{S}\right)^{2}\right] \geq E\left[(Y-E[Y])^{2}\right]
$$

# Proof. 

$$
\begin{aligned}
E\left[\left(Y-Y_{S}\right)^{2}\right] & =E\left[Y^{2}+Y_{S}^{2}-2 Y Y_{S}\right] \\
& =E\left[Y^{2}\right]+E\left[Y_{S}^{2}\right]-2 E\left[Y Y_{S}\right] \\
& =E\left[Y^{2}\right]+E\left[Y_{S}^{2}\right]-2 E[Y] E\left[Y_{S}\right] \\
& =2 E\left[Y^{2}\right]-2 E[Y]^{2} \\
& =2\left(E\left[Y^{2}\right]-E[Y]^{2}\right) \\
& =2 \operatorname{Var}(Y) \\
& \geq \operatorname{Var}(Y)=E\left[(Y-E[Y])^{2}\right]
\end{aligned}
$$

In the proof we have relied on the fact that both variables are independent and identically distributed, and therefore the expectation of the product is the product of the expectations, and the expected value of both variables is the same.

Proposition 1 motivates our proposal for modifying the data augmentation algorithm, since it proves that using the conditional expectation of $Y$ to impute the missing values instead of simulating values for $Y$ (denoted as $Y_{S}$ in the proposition), reduces the mse of the estimated regression model. Notice that it is true even if we are able to simulate from the exact distribution of $Y$ conditional on any configuration on a region of the values of the explanatory variables.

### 3.2. The algorithm for learning a regression model from incomplete data

Our proposal consists of an algorithm which iteratively learns a regression model (which can be an NB or a TAN) by imputing the missing values in each iteration according to the following criterion:

- If the missing value corresponds to the response variable, it is imputed with the conditional expectation of $Y$ given the values of the explanatory variables in the same record of the database, computed from the current regression model.
- Otherwise, the missing cell is imputed by simulating the corresponding variable from its conditional distribution given the values of the other variables in the same record, computed from the current regression model.

As the imputation requires the existence of a model, for the construction of the initial model we propose to impute the missing values by simulating from the marginal distribution of each variable computed from the observed values. In this way we have reached better results than using pure random initialisation, which is the standard way of proceeding in data augmentation. ${ }^{27}$ Another way of proceeding could be to simulate from the conditional distribution of each explanatory variable given the response, but we rejected this option because the estimation of the conditional distributions requires more data than the estimation of the marginals, which can be problematic if the number of missing values is high.


The algorithm (see algorithm 1) proceeds by imputing the initial database, learning an initial model and re-imputing the missing cells. Then, a new model is constructed and, if the mean squared error is reduced, the current model is replaced and the process repeated until convergence. As the mse in Eq. (4) requires the knowledge of the exact distribution of $Y$ conditional on each configuration of the explanatory variables, we use as error measure the sample root mean squared error,

```
Algorithm 2: Selective Bayesian network regression model from missing data
    Input: An incomplete database \(D\) for variables \(Y, X_{1}, \ldots, X_{n}\). A test
        database \(D_{t}\).
    Output: A Bayesian network regression model made up of the response
        variable \(Y\) and a subset of explanatory variables \(S \subseteq\left\{X_{1}, \ldots, X_{n}\right\}\).
    for \(i \leftarrow 1\) to \(n\) do
        Compute \(\hat{I}\left(X_{i}, Y\right)\).
    end
    4 Let \(X_{(1)}, \ldots, X_{(n)}\) be a decreasing order of the feature variables according to
        \(\hat{I}\left(X_{(i)}, Y\right)\).
    5 Using algorithm 1, construct a regression model \(M\) with variables \(Y\) and
        \(X_{(1)}\) from database \(D\).
    6 Let \(\operatorname{srmse}(M)\) be the estimated accuracy of model \(M\) using \(D_{t}\).
    7 for \(i \leftarrow 2\) to \(n\) do
        Let \(M_{1}\) be the model obtained by the algorithm 1 with the variables of
        \(M\) plus \(X_{(i)}\).
        Let \(\operatorname{srmse}\left(M_{1}\right)\) be the estimated accuracy of model \(M_{1}\) using \(D_{t}\).
        if \(\operatorname{srmse}\left(M_{1}\right) \leq \operatorname{rmse}(M)\) then
            \(M \leftarrow M_{1}\).
        end
    end
    return \(M\).
```

computed as

$$
\operatorname{srmse}=\sqrt{\frac{1}{m} \sum_{i=1}^{m}\left(y_{i}-\hat{y}_{i}\right)^{2}}
$$

where $m$ is the sample size, $y_{i}$ is the observed value of $Y$ for record $i$ and $\hat{y}_{i}$ is its corresponding prediction through the regression model.

The details are given in algorithm 1. Notice that, in steps 5 and 22 the regression model is learnt from a complete database, and therefore the existing estimation methods for MTEs can be used. ${ }^{25,20}$ Also, notice that the algorithm is valid for any Bayesian network structure, and therefore it is valid for our purpose, which is to learn an NB or a TAN, just by calling to the appropriate procedure in steps 5 and 22. For learning the NB regression model, we use the method described in Morales et al. ${ }^{20}$ and for learning the TAN, the algorithm in Fernández et al. ${ }^{8}$

We have also incorporated variable selection in the construction of the regression models ${ }^{9,20}$ as described in algorithm 2 . We have followed a filter-wrapper approach, based on the one proposed by Ruiz et al., ${ }^{23}$ using as filter measure the mutual information between each variable and the class. The filter-wrapper approach proceeds

by sorting the variables according to a filter measure, and then constructing a series of models including the variables in sequence, one by one, in such a way that a variable is kept in the model only if it increases the accuracy with respect to the previous model.

The mutual information has been successfully applied as filter measure in classification problems with continuous features. ${ }^{21}$ The mutual information between two random variables $X$ and $Y$ is defined as

$$
I(X, Y)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X Y}(x, y) \log _{2} \frac{f_{X Y}(x, y)}{f_{X}(x) f_{Y}(y)} d y d x
$$

where $f_{X Y}$ is the joint density for $X$ and $Y, f_{X}$ is the marginal density for $X$ and $f_{Y}$ is the marginal for $Y$.

In the case of MTE densities, the integral in Eq. (7) cannot be obtained in closed form. Therefore, we have estimated it by Monte Carlo. ${ }^{20}$

```
Algorithm 3: Computing a vector of bias to refine the predictions
    Input: A full database \(D\) for variables \(Y, X_{1}, \ldots, X_{n}\).
    A regression model \(M\).
    Output: \(v\) Bias, a vector of biases.
    1 Run a hierarchical clustering to obtain a dendrogram for the values of \(Y\).
    2 Determine the number of clusters, numBias, using the dendrogram.
    3 Partition \(D\) into numBias partitions \(D_{1}, \ldots, D_{\text {numBias }}\) by clustering \(Y\)
    using the \(k\)-means algorithm.
    4 for \(i \leftarrow 1\) to numBias do
    5 \(\mid\) Compute \(v\) Bias \([i]\) by (8) using \(D_{i}\) and \(M\).
    6 end
    7 return \(v\) Bias, a vector of estimated expected biases.
```


# 4. Improving the final estimations by reducing the bias 

In existing approaches for using MTEs for regression, the prediction that is used is a corrected version computed by subtracting an estimated expected bias from the prediction provided by the model. ${ }^{20}$ That is, if $Y$ is the response variable and $Y^{*}$ is the response variable actually identified by the model, i.e., the one that corresponds to the estimations provided by the model, then the expected bias is $E\left[b\left(Y, Y^{*}\right)\right]=$ $E\left[Y-Y^{*}\right]$, which is estimated as ${ }^{20}$

$$
\hat{b}=\frac{1}{m} \sum_{i=1}^{m}\left(y_{i}-y_{i}^{*}\right)
$$

where $y_{i}$ and $y_{i}^{*}$ are the exact values of the response variable and their estimates in a test database of $m$ records.

Finally, the estimates were corrected by giving $y_{i}^{*}-\hat{b}$ as the final estimation for item number $i$.

We have improved the estimation of the expected bias by detecting homogeneous regions in the set of possible values of $Y$ and then estimating a different expected bias in each region. The domain of the response variable is split using the $k$-means clustering algorithm, determining $k$ by exploring the dendrogram. In this work we have considered a maximum value of $k=4$, as we didn't reach any improvement by increasing its value in the experiments carried out.

Therefore, instead of a single estimation of the expected bias $\hat{b}$, now we compute a vector of estimations of the expected bias, $\hat{b}_{j}, j=1, \ldots, k$, and the final estimation given is $y_{i}^{*}-\hat{b}_{j(i)}$, where $j(i)$ denotes the cluster where $y_{i}^{*}$ lies in. The procedure for estimating the bias is detailed in algorithm 3 .

This new bias estimation heuristic is not really costly, and provides important increases in accuracy. Therefore, we have used it in the experiments reported in Sec. 5 .


Table 1. A description of the databases used in the experiments, indicating their size, number of continuous variables and number of discrete variables.

# 5. Experimental evaluation 

In order to test the performance of the proposed regression models, we have carried out a series of experiments over 16 databases, four of which are artificial (mte50, extended_mte50, tan and extended_tan).

The mte50 dataset ${ }^{20}$ consists of a random sample of 50 records drawn from a Bayesian network with naïve Bayes structure and MTE distributions. The aim of this network is to represent a situation which is handled in a natural way by the MTE model. In order to obtain this network, we first simulated a database with 500 records for variables $X, Y, Z$ and $W$, where $X$ follows a $\chi^{2}$ distribution with 5 degrees of freedom, $Y$ follows a negative exponential distribution with mean $1 / X$, $Z=\lfloor X / 2\rfloor$, where $\lfloor\cdot\rfloor$ stands for the integer part function, and $W$ follows a Beta distribution with parameters $p=1 / X$ and $q=1 / X$. Out of that database, an NB regression model was constructed using $X$ as response variable, and a sample of size 50 drawn from it using the Elvira software. ${ }^{7}$ Database extended_mte50 was obtained from mte50 by adding two columns independently of the others. One of the columns was drawn by sampling uniformly from the set $\{0,1,2,3\}$ and the other by sampling from a Gaussian distribution with mean 4 and standard deviation equal to 3 .

Database tan was constructed in a similar way. We generated a sample of size 1000 for variables $X_{0}, \ldots, X_{4}$, where $X_{0}$ follows a Gaussian distribution with mean 3 and standard deviation $2, X_{1}$ follows a negative exponential distribution with mean $2 \times\left|X_{0}\right|, X_{2}$ is uniformly distributed in the interval $\left(X_{0}, X_{0}+X_{1}\right), X_{3}$ is sampled from the set $\{0,1,2,3\}$ with probability proportional to $X_{0}$ and $X_{4}$ follows a Poisson distribution with mean $\lambda=\log \left(\left|X_{0}-X_{1}-X_{3}\right|+1\right)$. Out of that database, a TAN regression model ${ }^{8}$ was generated, and a sample of size 500 drawn from it using the Elvira software. ${ }^{7}$ Finally, the dataset extended_tan was obtained from tan by adding two independent columns, one of them drawn by sampling uniformly from the set $\{0,1,2,3\}$ and the other by sampling from a Gaussian distribution with mean 10 and standard deviation 5 .

The aim of using the two extended databases (extended_mte50 and extended_tan) is to test the performance of the variable selection scheme in two databases where we know for sure that some of the explanatory variables do not influence the response variable.

The other databases are available in the $\mathrm{UCI}^{1}$ and StatLib ${ }^{26}$ repositories. A description of the used databases can be found in Tab. 1.

In each database, we produced missing cells by removing values from cells selected at random, the rate of missing values ranging from $10 \%$ to $50 \%$. The missing cells have been created in an incremental way, i.e., a database $D$ with $20 \%$ of missing cells is constructed from the same database with a $10 \%$ of missing values and so on. That is, these two data sets have the same missing cells in a $10 \%$ of their positions. Over the resulting databases, we have run 5 algorithms: NB, TAN, SNB and STAN, where the last two correspond to the selective versions of NB

and TAN. We have also included the M5' algorithm in the comparison. The M5' algorithm ${ }^{28}$ is an improved version of the model tree introduced by Quinlan. ${ }^{22}$ The model tree is basically a decision tree where the leaves contain a regression model rather than a single value, and the splitting criterion uses the variance of the values in the database corresponding to each node rather than the information gain. We chose the M5' algorithm because it was the state-of-the-art in graphical models for regression, ${ }^{11}$ before the introduction of MTEs for regression. ${ }^{20}$ We have used the implementation of that method provided by Weka 3.4.11. ${ }^{29}$ Regarding the implementation of our regression models, we have included it in the Elvira software, ${ }^{7}$ which can be downloaded from http://leo.ugr.es/elvira.

We have used 10 -fold cross validation to estimate the srmse. The missing cells in the databases were selected before running the cross validation, therefore, in this case both the training and test databases contain missing cells in each iteration of the cross validation. We discarded from the test set the records for which the value of $Y$ was missing. If the missing cells in the test set correspond to explanatory variables, algorithm M5' imputes them as column average for numeric variables and column mode for qualitative variables. ${ }^{29}$ The regression models do not require the imputation of the missing explanatory variables in the test set, as the posterior distribution for $Y$ is computed by probability propagation and therefore, the variables which are not observed are marginalised out. The results of the experimental comparison are displayed in figures 3, 4 and 5. The values represented correspond to the average srmse computed by 10 -fold cross validation.

We used Friedman's test ${ }^{5}$ to compare the algorithms, reporting statistically significant difference among them, with a $p$-value of $2.2 \times 10^{-16}$. Therefore, we continued the analysis by carrying out a pairwise comparison, following the procedure discussed by García and Herrera, ${ }^{15}$ based on Nemenyi's, Holm's, Shaffer's and Bergmann's tests. The ranking of the algorithms analysed, according to Friedman's statistic, is shown in Tab. 2 Notice that a higher rank indicates that the algorithm is more accurate, as we are using the rmse as target. The result of the pairwise comparison is shown in Tab. 3. It can be seen that SNB and STAN outperform their versions without variable selection. Also, M5' is outperformed by SNB and STAN. Finally there are no statistically significant difference between the two most accurate methods: SNB and STAN. The conclusions are rather similar regardless of the test used. The only difference is that Holm's and Bergmann's tests also report significant differences between NB and TAN and between TAN and M5'.

# 5.1. Results discussion 

The experimental evaluation shows a satisfactory behaviour of the proposed regression methods. The selective versions outperform the sophisticated M5' algorithm. Notice that the M5' algorithm also incorporates variable selection, through treepruning. The difference between the models based on Bayesian networks and model trees becomes sharper as the rate of missing values grows. Also, the use of vari-

14 A. Fernández, J.D. Nielsen, A. Salmerón
![img-2.jpeg](img-2.jpeg)

Fig. 3. Comparison of the different models for the data sets.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Comparison of the different models for the data sets. The legends are the same as in figure 3.

16 A. Fernández, J.D. Nielsen, A. Salmerón
![img-4.jpeg](img-4.jpeg)

Fig. 5. Comparison of the different models for the data sets. The legends are the same as in figure 3.


Table 2. Average rankings of the algorithms tested in the experiments using Friedman's test.


Table 3. Adjusted $p$-values for the pairwise comparisons using Nemenyi's, Holm's, Shaffer's and Bergmann's statistical tests.
able selection always increases the accuracy. The fact that there are no significant differences between SNB and STAN make the first one preferable, as it is simpler (contains fewer parameters).

Finally, consider the line corresponding to M5' in the graph for database bodyfat in figure 3. In that case, the error decreases abruptly for $40 \%$ and $50 \%$ of missing values, which is counterintuitive. We have found out that this is due to the presence of outliers in the database, which are removed when the rate of missing values is high. It suggests that M5' is more sensitive to outliers than the models based on Bayesian networks.

# 6. Conclusions 

In this paper we have studied the induction of Bayesian network models for regression from incomplete data sets, based on the use of MTE distributions. We have considered two well known network structures in classification and regression: the naïve Bayes and TAN.

The proposal for handling missing values relies on the data augmentation algorithm, which iteratively re-estimates a model and imputes the missing values using it. We have shown that this algorithm can be adapted for the regression problem

by distinguishing the imputation of the response variable, in such a way that the prediction error is minimised.

We have also studied the problem of variable selection, following the same ideas as in the original NB and TAN models for regression. The final contribution of this paper is the method for improving the accuracy by reducing the bias, which can be incorporated regardless of whether the model is obtained from complete or incomplete data.

The experiments conducted have shown that the selective versions of the proposed algorithms outperform the robust M5' scheme, which is not surprising, as M5' is mainly designed for continuous explanatory variables, while MTEs are naturally developed for hybrid domains.
