# Article 

## Bayesian Test of Significance for Conditional Independence: The Multinomial Model

Pablo de Morais Andrade *, Julio Michael Stern and Carlos Alberto de Bragança Pereira

Instituto de Matemática e Estatística, Universidade de São Paulo (IME-USP) Rua do Matão, 1010, Cidade Universitária, São Paulo, SP/Brasil, CEP: 05508-090; E-Mails: jstern@ime.usp.br (J.M.S.); cpereira@ime.usp.br (C.A.B.P.)

* Author to whom correspondence should be addressed; E-Mail: pablo.andrade@usp.br; Tel.:/Fax: +55-11-969783425.

Received: 3 December 2013; in revised form: 21 February 2014 / Accepted: 5 March 2014 / Published: 7 March 2014


#### Abstract

Conditional independence tests have received special attention lately in machine learning and computational intelligence related literature as an important indicator of the relationship among the variables used by their models. In the field of probabilistic graphical models, which includes Bayesian network models, conditional independence tests are especially important for the task of learning the probabilistic graphical model structure from data. In this paper, we propose the full Bayesian significance test for tests of conditional independence for discrete datasets. The full Bayesian significance test is a powerful Bayesian test for precise hypothesis, as an alternative to the frequentist's significance tests (characterized by the calculation of the $p$-value).


Keywords: hypothesis testing; probabilistic graphical models

## 1. Introduction

Barlow and Pereira [1] discussed a graphical approach to conditional independence. A probabilistic influence diagram is a directed acyclic graph (DAG) that helps model statistical problems. The graph is composed of a set of nodes or vertices, which represent the variables, and a set of arcs joining the nodes, which represent the dependence relationships shared by these variables.

The construction of this model helps us understand the problem and gives a good representation of the interdependence of the implicated variables. The joint probability of these variables can be written as a product of their conditional distributions, based on their independence and conditional independence.

The interdependence of the variables [2] is sometimes unknown. In this case, the model structure must be learned from data. Algorithms, such as the IC-algorithm (inferred causation) described in Pearl and Verma [3], have been designed to uncover these structures from the data. This algorithm uses a series of conditional independence tests (CI tests) to remove and direct the arcs, connecting the variables in the model and returning a DAG that minimally (with the minimum number of parameters and without loss of information) represents the variables in the problem.

The problem of constructing the DAG structures based on the data motivates the proposal of new powerful statistical tests for the hypothesis of conditional independence, because the accuracy of the structures learned is directly affected by the errors committed by these tests. Recently proposed structure learning algorithms [4-6] indicate that the results of CI tests are the main source of errors.

In this paper, we propose the full Bayesian significance test (FBST) as a test of conditional independence for discrete datasets. FBST is a powerful Bayesian test for a precise hypothesis and can be used to learn the DAG structures based on the data as an alternative to the CI tests currently in use, such as Pearson's chi-squared test.

This paper is organized as follows. In Section 2, we review the FBST. In Section 3, we review the FBST for the composite hypothesis. Section 4 gives an example of testing for conditional independence that can be used to construct a simple model with three variables.

# 2. The Full Bayesian Significance Test 

The full Bayesian significance test was presented by Pereira and Stern [7] as a coherent Bayesian significance test for sharp hypotheses. In the FBST, the evidence for a precise hypothesis is computed.

This evidence is given by the complement of the probability of a credible set, called the tangent set, which is a subset of the parameter space in which the posterior density of each of the elements is greater than the maximum of the posterior density over the null hypothesis. This evidence is called the $e$-value, $\mathrm{ev}(\mathrm{H})$, and has many desirable properties as a statistical support. For example, Borges and Stern [8] described the following properties:
(1) provides a measure of significance for the hypothesis as a probability defined directly in the original parameter space.
(2) provides a smooth measure of the significance, both continuous and differentiable, of the hypothesis parameters.
(3) has an invariant geometric definition, independent of the particular parameterization of the null hypothesis being tested or the particular coordinate system chosen for the parameter space.
(4) obeys the likelihood principle.
(5) requires no ad hoc artifice, such as an arbitrary initial belief ratio between hypotheses.
(6) is a possibilistic support function, where the support of a logical disjunction is the maximum support among the support of the disjuncts.
(7) provides a consistent test for a given sharp hypothesis.
(8) provides compositionality operations in complex models.
(9) is an exact procedure, making no use of asymptotic approximations when computing the $e$-value.

(10) allows the incorporation of previous experience or expert opinions via prior distributions.

Furthermore, FBST is an exact test, whereas tests, such as the one presented in Geenens and Simar [9], are asymptotically correct. Therefore, the authors consider that a direct comparison between FBST and such test is not relevant in the context of this paper; considering, as future research, the comparison using small samples, in which case, FBST is still valid.

A more formal definition is given below.
Consider a model in a statistical space described by the triple, $(\Xi, \Delta, \Theta)$, where $\Xi$ is the sample space, $\Delta$, the family of measurable subsets of $\Xi$ and $\Theta$ the parameter space ( $\Theta$ is a subset of $\Re^{n}$ ).

Define a subset of the parameter space, $T_{\varphi}$ (tangent set), where the posterior density (denoted by $f_{x}$ ) of each element of this set is greater than $\varphi$.

$$
T_{\varphi}=\left\{\theta \in \Theta \mid f_{x}(\theta)>\varphi\right\}
$$

The credibility of $T_{\varphi}$ is given by its posterior probability,

$$
\kappa=\int_{T_{\varphi}} f_{x}(\theta) d \theta=\int_{\Theta} f_{x}(\theta) \mathbb{1}_{T_{\varphi}}(\theta) d \theta
$$

where $\mathbb{1}_{T_{\varphi}}(\theta)$ is the indicator function.

$$
\mathbb{1}_{T_{\varphi}}(\theta)= \begin{cases}1 & \text { if } \theta \in T_{\varphi} \\ 0 & \text { otherwise }\end{cases}
$$

Defining the maximum of the posterior density over the null hypothesis as $f_{x}^{*}$, with the maximum point at $\theta_{0}^{*}$,

$$
\theta_{0}^{*} \in \underset{\theta \in \Theta_{0}}{\operatorname{argmax}} f_{x}(\theta), \text { and } f_{x}^{*}=f_{x}\left(\theta^{*}\right)
$$

and defining $T^{*}=T_{f_{x}^{*}}$ as the tangent set to the null hypothesis, $H_{0}$, the credibility of $T^{*}$ is $\kappa^{*}$.
The measure of the evidence for the null hypothesis (called the e-value), which is the complement of the probability of the set $T^{*}$, is defined as follows:

$$
E v\left(H_{0}\right)=1-\kappa^{*}=1-\int_{\Theta} f_{x}(\theta) \mathbb{1}_{T^{*}}(\theta) d \theta
$$

If the probability of the set, $T^{*}$, is large, the null set falls within a region of low probability, and the evidence is against the null hypothesis, $H_{0}$. However, if the probability of $T^{*}$ is small, then the null set is in a region of high probability, and the evidence supports the null hypothesis.

# 2.1. FBST: Example of Tangent Set 

Figure 1 shows the tangent set for a null hypothesis $H_{0}: \mu=1$, for the posterior distribution, $f_{x}$, given bellow, where $\mu$ is the mean of a normal distribution and $\tau$ is the precision (the inverse of the variance $\tau=\frac{1}{a^{2}}$ ):

$$
f_{x}(\mu, \tau) \propto \tau^{1.5} e^{-\tau(\mu)^{2}-1.5 \tau}
$$

Figure 1. Example of a tangent set for the null hypothesis, $H_{0}: \mu=1.0$. In (a) and (b), the posterior distribution, $f_{x}$, is shown, with the red line representing the points in the null hypothesis $(\mu=1)$. In (c), the contours of $f_{x}$ show that the points of maximum density in the null hypothesis, $\theta_{0}^{*}$, have a density of $0.1037\left(f^{*}=f\left(\theta_{0}^{*}\right)=0.1037\right)$. The tangent set, $T^{*}$, of the null hypothesis, $H_{0}$, is the set of points inside the green contour line (points with a density greater than $f^{*}$ ), and the e-value of $H_{0}$ is the complement of the integral of $f_{x}$, as bounded by the green contour line.
![img-0.jpeg](img-0.jpeg)
(a) Posterior $f_{x}$. Red line: $\mu=1.0$.
![img-1.jpeg](img-1.jpeg)
(b) Posterior $f_{x}$. Red line: $\mu=1.0$.
![img-2.jpeg](img-2.jpeg)
(c) Contours of $f_{x}$. Red line: $\mu=1.0$.

# 3. FBST: Compositionality 

The relationship between the credibility of a complex hypothesis, $H$, and its elementary constituent, $H_{j}, j=1, \ldots, k$, under the full Bayesian significance test, was analyzed by Borges and Stern [8].

For a given set of independent parameters, $\left(\theta_{1}, \ldots, \theta_{k}\right) \in\left(\Theta_{1} \times \ldots \times \Theta_{k}\right)$, a complex hypothesis, $H$, can be given as follows:

$$
H: \theta_{1} \in \Theta_{1}^{H} \wedge \theta_{2} \in \Theta_{2}^{H} \wedge \ldots \wedge \theta_{k}^{H} \in \Theta_{k}^{H}
$$

where $\Theta_{j}^{H}$ is a subset of the parameter space, $\Theta_{j}$, for $j=1, \ldots, k$ and is constrained to the hypothesis, $H$, which can be decomposed into its elementary components (hypotheses):

$$
\begin{aligned}
& H_{1}: \theta_{1} \in \Theta_{1}^{H} \\
& H_{2}: \theta_{2} \in \Theta_{2}^{H} \\
& \cdots \\
& H_{k}: \theta_{k} \in \Theta_{k}^{H}
\end{aligned}
$$

The credibility of $H$ can be evaluated based on the credibility of these components. The evidence in favor of the complex hypothesis, $H$ (measured by its e-value), cannot be obtained directly from the evidence in favor of the elementary components; instead, it must be based on their truth function, $W^{j}$ (or cumulative surprise distribution), as defined below. For a given elementary component $\left(H_{j}\right)$ of the complex hypothesis, $H, \theta_{j}^{*}$ is the point of maximum density of the posterior distribution $\left(f_{x}\right)$ that is constrained to the subset of the parameter space defined by hypothesis $H_{j}$ :

$$
\theta_{j}^{*} \in \underset{\theta_{j} \in \Theta_{j}^{H}}{\operatorname{argmax}} f_{x}\left(\theta_{j}\right) \text { and } f_{j}^{*}=f_{x}\left(\theta_{j}^{*}\right)
$$

The truth function, $W_{j}$, is the probability of the parameter subspace (region $R_{j}(v)$ of the parameter space defined below), where the posterior density is lower than or equal to the value, $v$ :

$$
\begin{gathered}
R_{j}(v)=\left\{\theta_{j} \in \Theta_{j} \mid f_{x}\left(\theta_{j}\right) \leq v\right\} \\
W_{j}(v)=\int_{R_{j}(v)} f_{x}\left(\theta_{j}\right) d \theta_{j}
\end{gathered}
$$

The evidence supporting the hypothesis, $H_{j}$, is given as follows:

$$
E v\left(H_{j}\right)=W_{j}\left(f_{j}^{*}\right)
$$

The evidence supporting the complex hypothesis can be then described in terms of the truth function of its components as follows.

Given two independent variables, $X$ and $Y$, if $Z=X Y$, with cumulative distribution functions $F_{Z}(z), F_{X}(x)$ and $F_{Y}(y)$, then:

$$
\begin{aligned}
F_{Z}(z)=\operatorname{Pr}[Z \leq z]= & \operatorname{Pr}[X \leq z / Y]=\int_{0}^{\infty} \operatorname{Pr}[X \leq z / y] f_{Y}(y) d y= \\
& \int_{0}^{\infty} F_{X}(z / y) f_{Y}(y) d y=\int_{0}^{\infty} F_{X}(z / y) F_{Y}(d y)
\end{aligned}
$$

Accordingly, we define a functional product for cumulative distribution functions, namely,

$$
F_{Z}=F_{X} \otimes F_{Y}(z)=\int F_{X}(z / y) F_{Y}(d y)
$$

The same result concerning the product of non-negative random variables can be expressed by the Mellin convolution of the probability density functions, as demonstrated by Kaplan and Lin [10], Springer [11] and Williamson [12].

$$
f_{Z}(z)=\left(f_{X} \star f_{Y}\right)(z)=\int_{0}^{\infty}(1 / y) f_{X}(z / y) f_{Y}(y) d y
$$

The evidence supporting the complex hypothesis can be then described as the Mellin convolution of the truth function of its components:

$$
E v(H)=W_{1} \otimes W_{2} \otimes W_{3} \otimes \ldots \otimes W_{k}\left(f_{1}^{*} \cdot f_{2}^{*} \cdot f_{3}^{*} \cdot \ldots \cdot f_{k}^{*}\right)
$$

The Mellin convolution of two truth functions, $W_{1} \otimes W_{2}$, is the distribution function; see Borges and Stern [8]:

$$
W_{1} \otimes W_{2}\left(f_{1}^{*} \cdot f_{2}^{*}\right)=\int_{0}^{\infty} W_{1}\left(\frac{f_{1}^{*} \cdot f_{2}^{*}}{f}\right) W_{2}(d f)
$$

The Mellin convolution $W_{1} \otimes W_{2}$ gives the distribution function of the product of two independent random variables, with distribution functions $W_{1}$ and $W_{2}$; see Kaplan and Lin [13] and Williamson [12]. Furthermore, the commutative and associative properties follow immediately for the Mellin convolution,

$$
\left(W_{1} \otimes W_{2}\right) \otimes W_{3}=W_{1} \otimes\left(W_{2} \otimes W_{3}\right)=\left(W_{1} \otimes W_{3}\right) \otimes W_{2}=W_{1} \otimes\left(W_{3} \otimes W_{2}\right)
$$

# 3.1. Mellin Convolution: Example 

An example of a Mellin convolution to find the product of two random variables, $Y_{1}$ and $Y_{2}$, both of which have a Log-normal distribution, is given below.

Assume $Y_{1}$ and $Y_{2}$ to be continuous random variables, such that:

$$
Y_{1} \sim \ln \mathcal{N}\left(\mu_{1}, \sigma_{1}^{2}\right), \quad Y_{2} \sim \ln \mathcal{N}\left(\mu_{2}, \sigma_{2}^{2}\right)
$$

We denote the cumulative distributions of $Y_{1}$ and $Y_{2}$ by $W_{1}$ and $W_{2}$, respectively, i.e.,

$$
W_{1}\left(y_{1}\right)=\int_{-\infty}^{y_{1}} f_{Y_{1}}(t) d t, \quad W_{2}\left(y_{2}\right)=\int_{-\infty}^{y_{2}} f_{Y_{2}}(t) d t
$$

where $f_{Y_{1}}$ and $f_{Y_{2}}$ are the density functions of $Y_{1}$ and $Y_{2}$, respectively. These distributions can be written as a function of two normally distributed random variables, $X_{1}$ and $X_{2}$ :

$$
\begin{aligned}
& \ln \left(Y_{1}\right)=X_{1} \sim \mathcal{N}\left(\mu_{1}, \sigma_{1}^{2}\right) \\
& \ln \left(Y_{2}\right)=X_{2} \sim \mathcal{N}\left(\mu_{2}, \sigma_{2}^{2}\right)
\end{aligned}
$$

We can confirm that the distribution of the product of these random variables $\left(Y_{1} \cdot Y_{2}\right)$ is also Log-normal, using simple arithmetic operations:

$$
\begin{array}{r}
Y_{1}=e^{X_{1}} \text { and } Y_{2}=e^{X_{2}} \\
Y_{1} \cdot Y_{2}=e^{X_{1}+X_{2}} \\
\ln \left(Y_{1} \cdot Y_{2}\right)=X_{1}+X_{2} \sim \mathcal{N}\left(\mu_{1}+\mu_{2}, \sigma_{1}^{2}+\sigma_{2}^{2}\right) \\
\therefore Y_{1} \cdot Y_{2} \sim \ln \mathcal{N}\left(\mu_{1}+\mu_{2}, \sigma_{1}^{2}+\sigma_{2}^{2}\right)
\end{array}
$$

The cumulative density function of $Y_{1} \cdot Y_{2}\left(W_{12}\left(y_{12}\right)\right)$ is defined as follows:

$$
W_{12}\left(y_{12}\right)=\int_{-\infty}^{y_{12}} f_{Y_{1} \cdot Y_{2}}(t) d t
$$

where $f_{Y_{1} \cdot Y_{2}}$ is the density function of $Y_{1} \cdot Y_{2}$.
In the next section, we show different numerical methods for use in the convolution and condensation procedures, and we apply the results of these procedures to the example given here.

# 3.2. Numerical Methods for Convolution and Condensation 

Williamson and Downs [14] developed the idea of probabilistic arithmetics. They investigated numerical procedures that allow for the computation of a distribution using arithmetic operations on random variables by replacing basic arithmetic operations on numbers with arithmetic operations on random variables. They demonstrated numerical methods for calculating the convolution of probability distributions for a set of random variables.

The convolution for the multiplication of two random variables, $X_{1}$ and $X_{2}\left(Z=X_{1} \cdot X_{2}\right)$, can be written using their respective cumulative distribution functions, $F_{X_{1}}$ and $F_{Y_{2}}$ :

$$
F_{Z}(z)=\int_{0}^{z} F_{X_{1}}\left(\frac{z}{t}\right) d F_{X_{2}}(t)
$$

The algorithm for the numerical calculation of the distribution of the product of two independent random variables ( $Y_{1}$ and $Y_{2}$ ), using their discretized marginal probability distributions ( $f_{Y_{1}}$ and $f_{Y_{2}}$ ) is shown in Algorithm 1 (an algorithm for a discretization procedure is given by Williamson and Downs [14]). The description of Algorithm 1 is given below.
(1) The algorithm has as inputs two discrete variables, $Y_{1}$ and $Y_{2}$, as well as their respective probabilistic density functions (pdf): $f_{Y_{1}}$ and $f_{Y_{2}}$.
(2) The algorithm finds the products ( $Y_{1} \cdot Y_{2}$ and $f_{Y_{1}} \cdot f_{Y_{2}}$ ), resulting in $N^{2}$ bins, if $f_{Y_{1}}$ and $f_{Y_{2}}$ each have $N$ bins.
(3) The values of $Y_{1} \cdot Y_{2}$ are sorted in increasing order.
(4) The values of $f_{Y_{1}} \cdot f_{Y_{2}}$ are sorted according to the order of $Y_{1} \cdot Y_{2}$.
(5) The cumulative density function (cdf) of the product $Y_{1} \cdot Y_{2}$ is found (it has $N^{2}$ bins).

The numerical convolution of the two distributions with $N$ bins, as described above, returns a distribution with $N^{2}$ bins. For a sequence of operations, such a large number of bins would be a problem, because the result of each operation would be larger than the input for the operations. Therefore, the authors have proposed a simple method for reducing the size of the output to $N$ bins without introducing further error into the result. This operation is called condensation and returns the upper and lower bounds of each of the $N$ bins for the distribution resulting from the convolution. The algorithm for the condensation process is shown in Algorithm 2. The description of Algorithm 2 is given below.
(1) The algorithm has as input a cdf with $N^{2}$ bins.
(2) For each group of $N$ bins (there are $N$ groups of $N$ bins), the value of the cdf at the first bin is taken as the lower bound, and the value of the cdf at the last bin is taken as the upper bound.
(3) The algorithm returns a cdf with $N$ bins, where each bin has a lower and an upper bound.


Algorithm 2 Find the upper lower bound for a cdf for condensation.


# 3.2.1. Vertical Condensation 

Kaplan and Lin [13] proposed a vertical condensation procedure for discrete probability calculations, where the condensation is done using the vertical axis, instead of the horizontal axis, as used by Williamson and Downs [14].

The advantage of this approach is that it provides greater control over the representation of the distribution; instead of selecting an interval of the domain of the cumulative distribution function (values assumed by the random variable) as a bin, we select the interval from the range of the cumulative distribution in $[0,1]$, which should be represented by each bin.

In this case, it is also possible to focus on a specific region of the distribution. For example, if there is a greater interest in the behavior of the tail of the distribution, the size of the bins can be reduced in this region, consequently increasing the number of bins necessary to represent the tail of the distribution.

An example of such a convolution that is followed by a condensation procedure using both approaches is given in Section 3.1. For this example, we used discretization and condensation procedures, with the bins uniformly distributed over both axes. At the end of the condensation procedure, using the first approach, the bins are uniformly distributed horizontally (over the sample space of the variable). For the second approach, the bins of the cumulative probability distribution are uniformly distributed over the vertical axis on the interval $[0,1]$. Algorithm 3 shows the condensation with the bins uniformly distributed over the vertical axis.

```
Algorithm 3 Condensation with the bins vertically uniformly distributed.
    procedure VERTICALCONDENSATION \((W, f, x) \quad \triangleright\) Histograms of a cdf and pdf, and breaks in the x-axis.
        breaks \(\leftarrow[1 / n, 2 / n, \ldots, 1] \quad \triangleright\) uniform breaks in \(y\)-axis
        \(W_{n} \leftarrow \operatorname{array}(0, \operatorname{size} \leftarrow n]\)
        \(x_{n} \leftarrow \operatorname{array}(0, \operatorname{size} \leftarrow n]\)
        lastbreak \(\leftarrow 1\)
        \(i \leftarrow 1\)
        for all \(b \in\) breaks do
            \(w \leftarrow \operatorname{first}(W \geq b) \quad \triangleright\) find break to create current bin
            if \(W[w] \neq b\) then \(\triangleright\) if the break is within a current bin
                ratio \(\leftarrow(b-W[w-1]) /(W[w]-W[w-1])\)
                \(x_{n}[i] \leftarrow \frac{1}{1 / n}(\operatorname{sum}(f[w-1] \cdot x[w-1])+\) ratio \(\cdot f[w] \cdot x[w])\)
                \(W[i-1] \leftarrow b\)
                \(W_{n}[i] \leftarrow b\)
                \(f[i-1] \leftarrow f[w-1]+\) ratio \(\cdot f[w]\)
                \(f[i] \leftarrow(1-\) ratio \() \cdot f[w]\)
            else
                \(x_{n}[i] \leftarrow x[w]\)
                \(W_{n}[i] \leftarrow W[w]\)
            end if
            lastbreak \(\leftarrow b\)
            \(i \leftarrow i+1\)
        end for
        return \(\left[W_{n}, x_{n}\right] \quad \triangleright\) Histograms with upper/lower bounds
    end procedure
```

Figure 2 shows the cumulative distribution functions of $Y_{1}$ and $Y_{2}$ (Section 3.1) after they have been discretized with bins uniformly distributed over both the $x$ - and $y$-axes (horizontal and vertical discretizations). Figure 3 shows an example of convolution followed by condensation (based on the example in Section 3.1), using both the horizontal and vertical condensation procedures and the true distribution of the product of two variables with Log-normal distributions.

Figure 2. Example of different discretization methods for the representation of the cdf of two random variables ( $Y_{1}$ and $Y_{2}$ ) with Log-normal distributions. In (a) and (c), respectively, the cdf of $Y_{1}$ and $Y_{2}$ are shown, with the bins uniformly distributed over the $x$-axis. In (b) and (d), respectively, the cdf of $Y_{1}$ and $Y_{2}$ are shown, with the bins uniformly distributed over the $y$-axis.
![img-3.jpeg](img-3.jpeg)
(a) $W_{1}$ : Horizontal discretization
![img-4.jpeg](img-4.jpeg)
(c) $W_{2}$ : Horizontal discretization
![img-5.jpeg](img-5.jpeg)
(b) $W_{1}$ : Vertical discretization
![img-6.jpeg](img-6.jpeg)
(d) $W_{2}$ : Vertical discretization

Figure 3. Example of the convolution of two random variables ( $Y_{1}$ and $Y_{2}$ ) with Log-normal distributions. The result of the convolution $Y_{1} \otimes Y_{2}$, followed by horizontal condensation (bins uniformly distributed over the $x$-axis), is shown in (a), and the result of vertical condensation (bins uniformly distributed over the $y$-axis) is shown in (b). The true distribution of the product $Y_{1} \cdot Y_{2}$ is shown in (c) and (d), respectively, for the horizontal and vertical discretization procedures.
![img-7.jpeg](img-7.jpeg)
(a) $W_{1} \otimes W_{2}$ : Horizontal discretization
![img-8.jpeg](img-8.jpeg)
(c) $Y_{1} \cdot Y_{2}$ : Horizontal discretization
![img-9.jpeg](img-9.jpeg)
(b) $W_{1} \otimes W_{2}$ : Vertical discretization
![img-10.jpeg](img-10.jpeg)
(d) $Y_{1} \cdot Y_{2}$ : Vertical discretization

# 4. Test of Conditional Independence in Contingency Table Using FBST 

We now apply the methods shown in the previous sections to find evidence of a complex null hypothesis of conditional independence for discrete variables.

Given the discrete random variables, $X, Y$ and $Z$, with $X$ taking values on $\{1, \ldots, k\}$ and $Y$ and $Z$ serving as categorical variables, the test for conditional independence $Y \Perp Z \mid X$ can be written as the complex null hypothesis, $H$ :

$$
H:[Y \Perp Z \mid X=1] \wedge[Y \Perp Z \mid X=2] \wedge \cdots \wedge[Y \Perp Z \mid X=k]
$$

The hypothesis, $H$, can be decomposed into its elementary components:

$$
\begin{aligned}
& H_{1}: Y \Perp Z \mid X=1 \\
& H_{2}: Y \Perp Z \mid X=2 \\
& \cdots \\
& H_{k}: Y \Perp Z \mid X=k
\end{aligned}
$$

Note that the hypotheses, $H_{1}, \ldots, H_{k}$, are independent. For each value, $x$, taken by $X$, the values taken by variables $Y$ and $Z$ are assumed to be random observations drawn from some distribution $p(Y, Z \mid X=$ $x)$. Each of the elementary components is a hypothesis of independence in a contingency table. Table 1 shows the contingency table for $Y$ and $Z$, which take values on $\{1, \ldots, r\}$ and $\{1, \ldots, c\}$, respectively.

Table 1. Contingency table of $Y$ and $Z$ for $X=x$ (hypothesis $H_{x}$ ); $n_{y z x}$ is the count of $[Y, Z]=[y, z]$ when $X=x$.


The test of the hypothesis, $H_{x}$, can be set up using the multinomial distribution for the cell counts of the contingency table and its natural conjugate prior, i.e., the Dirichlet distribution for the vector of the parameters $\theta_{x}=\left[\theta_{11 x}, \theta_{12 x}, \ldots, \theta_{r c x}\right]$.

For a given array of hyperparameters $\alpha_{x}=\left[\alpha_{11 x}, \ldots, \alpha_{r c x}\right]$, the Dirichlet distribution is defined as:

$$
f\left(\theta_{x} \mid \alpha_{x}\right)=\Gamma\left(\sum_{y, z}^{r, c} \alpha_{y z x}\right) \prod_{y, z}^{r, c} \frac{\theta_{y z x}^{\alpha_{y z x}-1}}{\Gamma\left(\alpha_{y z x}\right)}
$$

The multinomial likelihood for the given contingency table, assuming the array of observations $n_{x}=$ $\left[n_{11 x}, \ldots, n_{r c x}\right]$ and the sum of the observations $n_{\llcorner x}=\sum_{y, z}^{r, c} n_{y z x}$, is:

$$
f\left(n_{x} \mid \theta_{x}\right)=n_{\llcornerx x!}!\prod_{y, z}^{r, c} \frac{\theta_{y z x}^{n_{y z x}}}{n_{y z x}!}
$$

The posterior distribution is thus a Dirichlet distribution, $f_{n}\left(\theta_{x}\right)$ :

$$
f_{n}\left(\theta_{x}\right) \propto \prod_{y, z}^{r, c} \theta_{y z x}^{\alpha_{y z x}+n_{y z x}-1}
$$

Under hypothesis $H_{x}$, we have $Y \Perp Z \mid X=x$. In this case, the joint distribution is equal to the product of the marginals: $p(Y=y, Z=z \mid X=x)=p(Y=y \mid X=x) p(Z=z \mid X=x)$. We can define this condition using the array of parameters, $\theta_{x}$. In this case, we have:

$$
H_{x}: \theta_{y z x}=\theta_{. z x} \cdot \theta_{y . x}, \forall y, z
$$

where $\theta_{. z x}=\sum_{y}^{r} n_{y z x}$ and $\theta_{y . x}=\sum_{z}^{c} \theta_{y z x}$.
The elementary components of hypothesis $H$ are as follows:

$$
\begin{aligned}
& H_{1}: \theta_{y z 1}=\theta_{. z 1} \cdot \theta_{y .1}, \forall y, z \\
& H_{2}: \theta_{y z 2}=\theta_{. z 2} \cdot \theta_{y .2}, \forall y, z \\
& \quad \ldots \\
& H_{k}: \theta_{y z k}=\theta_{. z k} \cdot \theta_{y . k}, \forall y, z
\end{aligned}
$$

The point of maximum density of the posterior distribution that is constrained to the subset of the parameter space defined by hypothesis $H_{x}$ can be estimated using the maximum a posteriori (MAP) estimator under hypothesis $H_{x}$ (the mode of parameters, $\theta_{x}$ ). The maximum density $\left(f_{x}^{*}\right)$ is the posterior density evaluated at this point.

$$
\theta_{y z x}^{*}=\frac{n_{y z x}^{H_{x}}+\alpha_{y z x}-1}{n_{-x}^{H_{x}}+\alpha_{. . x}-r \cdot c} \text { and } f_{x}^{*}=f_{n}\left(\theta_{x}^{*}\right)
$$

where $\theta_{x}^{*}=\left[\theta_{11 x}^{*}, \ldots, \theta_{r c x}^{*}\right]$.
The evidence supporting $H_{x}$ can be written in terms of the truth function, $W_{x}$, as defined in Section 3:

$$
\begin{array}{r}
R_{x}(f)=\left\{\theta_{x} \in \Theta_{x} \mid f_{x}\left(\theta_{x}\right) \leq f\right\} \\
W_{x}(f)=\int_{R_{x}(f)} f_{n}\left(\theta_{x}\right) d \theta_{x} \propto \int_{R_{x}(f)} \prod_{y, z}^{r, c} \theta_{y z x}^{\alpha_{y z x}+n_{y z x}-1} d \theta_{x}
\end{array}
$$

The evidence supporting $H_{x}$ is:

$$
E v\left(H_{x}\right)=W_{x}\left(f_{x}^{*}\right)
$$

Finally, the evidence supporting the hypothesis of conditional independence $(H)$ is given by the convolution of the truth functions that are evaluated at the product of the points of maximum posterior density, for each component of hypothesis $H$ :

$$
E v(H)=W_{1} \otimes W_{2} \otimes \ldots \otimes W_{k}\left(f_{1}^{*} \cdot f_{2}^{*} \cdot \ldots \cdot f_{k}^{*}\right)
$$

The e-value for hypothesis $H$ can be found using modern mathematical integration methods. An example is given in the next section, using the numerical convolution, followed by the condensation procedures described in Section 3.2. Applying the horizontal condensation method results in an interval for the e-value (found using the lower and upper bounds resulting from the condensation process) and in a single value for the vertical procedure.

# 4.1. Example of CI Test Using FBST 

In this section, we describe an example of the CI test using the full Bayesian significance test for conditional independence using samples from two different models. For both models, we test whether the variable, $Y$, is conditionally independent of $Z$ given $X$.

Two probabilistic graphical models ( $M_{1}$ and $M_{2}$ ) are shown in Figure 4, where the three variables, $X, Y$ and $Z$, assume values in $\{1,2,3\}$. In the first model (Figure 4a), the hypothesis of independence $H: Y \Perp Z \mid X$ is true, but in the second model (Figure 4b), the same hypothesis is false. The synthetic conditional probability distribution tables (CPTs) used to generate the samples are given in Appendix.

Figure 4. Simple probabilistic graphical models. (a) Model $M_{1}$, where $Y$ is conditionally independent of $Z$ given $X$; (b) Model $M_{2}$, where $Y$ is not conditionally independent of $Z$ given $X$.
![img-11.jpeg](img-11.jpeg)
(a) $M_{1}: Y \Perp Z \mid X$
![img-12.jpeg](img-12.jpeg)
(b) $M_{2}: Y \Perp Z \mid X$

We calculate the intervals for the e-values and compare them, for hypothesis $H$ of conditional independence, for both models: $E v_{M_{1}}(H)$ and $E v_{M_{2}}(H)$. The complexity hypothesis, $H$, can be decomposed into its elementary components:

$$
\begin{aligned}
& H_{1}: Y \Perp Z \mid X=1 \\
& H_{2}: Y \Perp Z \mid X=2 \\
& H_{3}: Y \Perp Z \mid X=3
\end{aligned}
$$

For each model, 5000 observations were generated; the contingency table of $Y$ and $Z$ for each value of $X$ is shown in Table 2. The hyperparameters of the prior distribution were all set to one, because, in this case, the prior is equivalent to a uniform distribution (from Equation (23)):

$$
\begin{gathered}
\alpha_{1}=\alpha_{2}=\alpha_{3}=[1,1,1] \\
f\left(\theta_{1} \mid \alpha_{1}\right)=f\left(\theta_{3} \mid \alpha_{3}\right)=f\left(\theta_{3} \mid \alpha_{3}\right)=1
\end{gathered}
$$

The posterior distribution, found using Equations (24) and (25), is then given as follows:

$$
f_{n}\left(\theta_{1}\right) \propto \prod_{y=1, z=1}^{3,3} \theta_{y z 1}^{n_{y z 1}}, f_{n}\left(\theta_{2}\right) \propto \prod_{y=1, z=1}^{3,3} \theta_{y z 2}^{n_{y z 2}}, f_{n}\left(\theta_{3}\right) \propto \prod_{y=1, z=1}^{3,3} \theta_{y z 3}^{n_{y z 3}}
$$

For example, for the given contingency table for Model $M_{1}$, when $X=2$ (Table 2c), the posterior distribution is the following:

$$
f_{n}\left(\theta_{2}\right) \propto \theta_{112}^{42} \cdot \theta_{122}^{41} \cdot \theta_{132}^{323} \cdot \theta_{212}^{39} \cdot \theta_{222}^{41} \cdot \theta_{232}^{341} \cdot \theta_{312}^{15} \cdot \theta_{322}^{21} \cdot \theta_{332}^{171}
$$

The point of highest density, in this example, following the hypothesis of independence (Equations (26) and (28)), was found to be the following:

$$
\theta_{2}^{*} \approx[0.036,0.039,0.317,0.038,0.041,0.329,0.019,0.020,0.162]
$$

The truth function and the evidence supporting the hypothesis of independence given $X=2$ (hypothesis $H_{2}$ ) for Model $M_{1}$, as given in Equations (29) and (30), are as follows:

$$
\begin{gathered}
R_{2}(f)=\left\{\theta_{2} \in \Theta_{2} \mid f_{n}\left(\theta_{2}\right) \leq f\right\} \\
W_{2}(f)=\int_{R_{2}(f)} f_{n}\left(\theta_{2}\right) d \theta_{2} \\
E v_{M_{1}}\left(H_{2}\right)=W_{2}\left(f_{n}\left(\theta_{2}^{*}\right)\right)
\end{gathered}
$$

We used the methods of numerical integration to find the e-value of the elementary components of hypothesis $H\left(H_{1}, H_{2}\right.$ and $\left.H_{3}\right)$, and the results for each model are given below.

Table 2. Contingency tables of $Y$ and $Z$ for a given value of $X$ for 5000 random samples. (a,c,e): samples from Model $M_{1}$ (Figure 4a) for $X=1,2$, and 3 , respectively; (b,d,f): samples from Model $M_{2}$ (Figure 4b) for $X=1,2$, and 3 , respectively.


(c) Model $M_{1}$ (for $X=2$ )


(e) Model $M_{1}$ (for $X=3$ )


(b) Model $M_{2}$ (for $X=1$ )


(d) Model $M_{2}$ (for $X=2$ )


(f) Model $M_{2}$ (for $X=3$ )


E-values found using horizontal discretization:

$$
\begin{gathered}
E v_{M_{1}}\left(H_{1}\right)=0.9878, E v_{M_{1}}\left(H_{2}\right)=0.9806 \text { and } E v_{M_{1}}\left(H_{3}\right)=0.1066 \\
E v_{M_{2}}\left(H_{1}\right)=0.0004, E v_{M_{2}}\left(H_{2}\right)=0.0006 \text { and } E v_{M_{2}}\left(H_{3}\right)=0.0004
\end{gathered}
$$

E-values found using vertical discretization:

$$
\begin{gathered}
E v_{M_{1}}\left(H_{1}\right)=0.99, E v_{M_{1}}\left(H_{2}\right)=0.98 \text { and } E v_{M_{1}}\left(H_{3}\right)=0.11 \\
E v_{M_{2}}\left(H_{1}\right)=0.01, E v_{M_{2}}\left(H_{2}\right)=0.01 \text { and } E v_{M_{2}}\left(H_{3}\right)=0.01
\end{gathered}
$$

Figure 5 shows the histogram of the truth functions, $W_{1}, W_{2}$ and $W_{3}$, for the model, $M_{1}$ ( $Y$ and $Z$ are conditionally independent, given $X$ ). In Figure 5a,c,e, 100 bins are uniformly distributed over the $x$-axis (using the empirical values of $\min f_{n}\left(\theta_{x}\right)$ and $\max f_{n}\left(\theta_{x}\right)$ ). In Figure 5b,d,f, 100 bins are uniformly distributed over the $y$-axis (each bin represents an increase in $1 \%$ in density from the previous bin). The function, $W_{x}$, evaluated at the maximum posterior density over the respective hypothesis, $f_{n}\left(\theta_{x}^{*}\right)$, in red, corresponds to the e-values found (e.g., $W_{3}\left(f\left(\theta_{3}^{*}\right)\right) \approx 0.1066$, for the horizontal discretization in Figure 5e).

Figure 5. Histogram with 100 bins for the truth functions of the model, $M_{1}$ (Figure 4a for each value of $X$. (a) $W_{1}$ for Model $M_{1}, f_{n}\left(\theta_{1}^{*}\right)$ in red; (b) $W_{1}$ for Model $M_{1}, f_{n}\left(\theta_{1}^{*}\right)$ in red; (c) $W_{2}$, for Model $M_{1}, f_{n}\left(\theta_{2}^{*}\right)$ in red; (d) $W_{2}$, for Model $M_{1}, f_{n}\left(\theta_{2}^{*}\right)$ in red; (e) $W_{3}$, for Model $M_{1}, f_{n}\left(\theta_{3}^{*}\right)$ in red; (f) $W_{3}$, for Model $M_{1}, f_{n}\left(\theta_{3}^{*}\right)$ in red. In red is the maximum posterior density under the respective elementary component ( $H_{1}, H_{2}$ and $H_{3}$ ) of the hypothesis of conditional independence $H$ for both horizontal and vertical discretization procedures.

Horizontal Discretization
Vertical Discretization
![img-13.jpeg](img-13.jpeg)
(a)
![img-14.jpeg](img-14.jpeg)
(c)
![img-15.jpeg](img-15.jpeg)
(e)
![img-16.jpeg](img-16.jpeg)
![img-17.jpeg](img-17.jpeg)
(b)
![img-18.jpeg](img-18.jpeg)
(d)
![img-19.jpeg](img-19.jpeg)
(f)

The evidence supporting the hypothesis of the conditional independence $H$, as in Equation (31), for each model is as follows:

$$
E v(H)=W_{1} \otimes W_{2} \otimes W_{3}\left(f_{n}\left(\theta_{1}^{*}\right) \cdot f_{n}\left(\theta_{2}^{*}\right) \cdot f_{n}\left(\theta_{3}^{*}\right)\right)
$$

The convolution follows the commutative property, and the order of the convolutions is therefore irrelevant.

$$
W_{1} \otimes W_{2} \otimes W_{3}(f)=W_{3} \otimes W_{2} \otimes W_{1}(f)
$$

Using the algorithm for numerical convolution described in Algorithm 1, we found the convolution of the truth functions, $W_{1}$ and $W_{2}$, resulting in a cumulative function $\left(W_{12}\right)$ with 10,000 bins ( $100^{2}$ bins). We then performed the condensation procedures described in Algorithms 2 and 3 and reduced the cumulative distribution to 100 bins, with lower and upper bounds ( $W_{12}^{l}$ and $W_{12}^{u}$ ) for the horizontal condensation. The results are shown in Figure 6a,b for Model $M_{1}$ (horizontal and vertical condensations, respectively) and in Figure 7a,b for Model $M_{2}$.

Figure 6. Histogram with 100 bins resulting from the convolutions for Model $M_{1}$ : (a) $W_{1} \otimes W_{2}$ with horizontal discretization; (b) $W_{1} \otimes W_{2}$ with vertical discretization; (c) $W_{1} \otimes$ $W_{2} \otimes W_{3}$ with horizontal discretization; (d) $W_{1} \otimes W_{2} \otimes W_{3}$ with vertical discretization. In red in (c) and (d) is the bin representing the product of the maximum posterior density under the elementary components ( $H_{1}, H_{2}$ and $H_{3}$ ) of the hypothesis of the conditional independence $H$ for model $M_{1}$.
![img-20.jpeg](img-20.jpeg)

The convolution of $W_{12}$ and $W_{3}$ was followed by their condensation. The results are shown in Figure 6c,d (Model $M_{1}$ ) and Figure 7c,d (Model $M_{2}$ ).

The e-values supporting the hypothesis of conditional independence for both models are given below.

The intervals for the e-values were found using horizontal discretization and condensation, as follows:

$$
\begin{gathered}
E v_{M_{1}}(H)=[0.587427,0.718561] \\
E v_{M_{2}}(H)=\left[8 \cdot 10^{-12}, 6.416 \cdot 10^{-9}\right]
\end{gathered}
$$

The e-values found using vertical discretization and condensation were as follows:

$$
\begin{aligned}
E v_{M_{1}}(H) & =0.95 \\
E v_{M_{2}}(H) & =0.01
\end{aligned}
$$

These results show strong evidence supporting the hypothesis of conditional independence between $Y$ and $Z$, given $X$, for Model $M_{1}$ (using both discretization/condensation procedures). No evidence supporting the same hypothesis for the second model was found. This result is very relevant and promising as a motivation for further studies on the use of FBST as a CI test for the structural learning of graphical models.

Figure 7. Histogram with 100 bins resulting from the convolutions for model $M_{2}$ : (a) $W_{1} \otimes$ $W_{2}$ with horizontal discretization; (b) $W_{1} \otimes W_{2}$ with vertical discretization; (c) $W_{1} \otimes W_{2} \otimes W_{3}$ with horizontal discretization; (d) $W_{1} \otimes W_{2} \otimes W_{3}$ with vertical discretization. In red in (c) and (d) is the bin representing the product of the maximum posterior density under the elementary components ( $H_{1}, H_{2}$ and $H_{3}$ ) of the hypothesis of conditional independence, $H$, for model $M_{2}$.
![img-21.jpeg](img-21.jpeg)

# 5. Conclusions and Future Work 

This paper provides a framework for performing tests of conditional independence for discrete datasets using the Full Bayesian Significance Test. A simple application of this test includes examining

the structure of a directed acyclic graph given two different models. The result found in this paper suggests that FBST should be considered a good alternative to performing CI tests to uncover the structures of probabilistic graphical models from data.

Future research should include the use of FBST in algorithms to learn the structures of graphs with larger numbers of variables; to increase the capacity for performing these mathematical methods to calculate $e$-values (because learning DAG structures from data requires an exponential number of CI tests to be performed, each CI test needs to be performed faster); and to empirically evaluate the threshold for $e$-values to define conditional independence versus dependence. The last of these areas of future exploration should be achieved by minimizing the linear combination of type I and II errors (incorrect rejection of a true hypothesis of conditional independence and failure to reject a false hypothesis of conditional independence).

# Acknowledgment 

The authors are grateful for the support of IME-USP, to the Coordenação de Aperfeiçoamento de Pessoal de Nível Superior (CAPES), Conselho Nacional de Desenvolvimento Científico e Tecnológico (CNPq) and Fundação de Apoio à Pesquisa do Estado de São Paulo (FAPESP).

## Author Contribution

All authors made substantial contributions to conception and design, acquisition of data and analysis and interpretation of data; all authors participate in drafting the article or revising it critically for important intellectual content; all authors gave final approval of the version to be submitted and any revised version.

## Conflicts of Interest

We certify that there is no conflict of interest regarding the material discussed in the manuscript.

# Appendix 

Table A1. Conditional probability distribution tables. (a) The distribution of $X$, (b) the conditional distribution of $Y$, given $X$, and (c) the conditional distribution of $Z$, given $X$.


(c) CPT of $Z$ given $X$


Table A2. Conditional probability distribution table of $Z$, given $X \& Y$.


(c) 2014 by the authors; licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution license (http://creativecommons.org/licenses/by/3.0/).