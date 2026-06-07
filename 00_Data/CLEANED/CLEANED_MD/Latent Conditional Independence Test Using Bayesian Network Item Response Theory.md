# Latent Conditional Independence Test Using Bayesian Network Item Response Theory 

Takamitsu HASHIMOTO ${ }^{1, \dagger \dagger}$, Nonmember and Maomi UENO ${ }^{\dagger}$, Member


#### Abstract

SUMMARY Item response theory (IRT) is widely used for test analyses. Most models of IRT assume that a subject's responses to different items in a test are statistically independent. However, actual situations often violate this assumption. Thus, conditional independence (CI) tests among items given a latent ability variable are needed, but traditional CI tests suffer from biases. This study investigated a latent conditional independence (LCI) test given a latent variable. Results show that the LCI test can detect CI given a latent variable correctly, whereas traditional CI tests often fail to detect CI. Application of the LCI test to mathematics test data revealed that items that share common alternatives might be conditionally dependent.


key words: item response theory, Bayesian network model, local independence, conditional independence test, latent variable

## 1. Introduction

Lord and Novick [1] used a modern mathematical statistical approach to formulate the basic constructs of the item response theory (IRT). Since then, a great deal of research effort has been spent in developing their idea from different perspectives (e.g., statistical theory and parameter estimation algorithms). There are many possible IRT models, which differ in the mathematical form of the item characteristic function and/or the number of parameters specified in the model, for example, the Rasch model [2], the normal ogive model [1], the two parameters logistic model [3], and the three parameters logistic model [4]. There are more general and well-known IRT models such as the graded response model [5], the free response model [6], the partial credit model [7], and the nominal response model [8]. All IRT models incorporate one or more parameters describing the subject. IRT rests on three basic postulates: (1) The performance of a subject for a test item can be predicted (or explained) by a set of factors called traits, latent traits, or abilities. (2) The relation between the subject's item performance and the set of traits underlying item performance can be described using a monotonically increasing function called an item characteristic function or item characteristic curve. (3) When the ability variables influencing the test performance are held constant, the subject's responses to any pair of items are statistically independent, which is often called local independence. It should be particularly noted that assumption (3) states that a subject's responses to dif-

[^0]ferent items in a test are statistically independent (Fig. 1). For this assumption to be true, a subject's performance for one item must not affect, either positively or negatively, the response to any other item in the test. Regarding this conditional independence (CI) assumption, Yen [9] previously pointed out that actual situations often violate this assumption. Furthermore, many previous studies [10]-[13] have shown that the parameter estimation often fails when the CI assumption is violated.

Consequently, CI tests among items given a latent variable are necessary for the application of IRT to test data. However, it is difficult to realize the CI test given a latent variable. Considering this problem, several CI tests given a latent variable have been proposed. For example, Yen's $Q_{3}$ statistic [9] is defined as the correlation coefficient of two items' fitting errors between the expected and actual responses. Chen and Thissen's $G^{2}$ statistic [10] is the log-likelihood ratio of an observed frequency to an expected frequency derived from an IRT model. These statistics marginalize out the latent variable and provide CI tests of only the two target items. Namely, the traditional methods implicitly assume that the CI tests of two variables are not affected by any other two items' dependencies when the latent variable is marginalized out. However, in the present study, we found through some simulation experiments that this assumption does not hold. That is, we show that the other two variables dependencies affect the CI test of the two target variables even when the latent variable is marginalized out.

To solve this problem, we propose a new CI test between two items given a latent variable. The unique feature of our method is a CI test of the target items given all the other items, which are assumed to be mutually dependent (complete structured variables). In addition, we use Bayesian network IRT [14], which alleviates the CI assumption given the latent variable, to calculate our CI test. We

[^1]
[^0]:    Manuscript received June 29, 2010.
    Manuscript revised December 18, 2010.
    ${ }^{\dagger}$ The authors are with the University of Electro-Communications, Chofu-shi, 182-8585 Japan.
    ${ }^{\dagger \dagger}$ The author is with the National Center for University Entrance Examinations, Tokyo, 153-8501 Japan.

    DOI: 10.1587/transinf.E94.D. 743

[^1]:    Fig. 1 Graphical expression of a conditionally independent structure given a latent ability variable.

also prove that our CI test correctly detects the dependency of the target variables given the latent variable even when two other items are dependent. The effectiveness of our test was confirmed in some simulation experiments.

This paper is organized as follows. Section 2 briefly reviews IRT. Section 3 explains the traditional CI tests. Section 4 describes the problems of the traditional CI tests. Section 5 presents our proposal for solving the problem. Section 6 describes some experiments in comparison with traditional CI tests and Sect. 7 presents examples of application to real data. Section 8 discusses the results and presents our conclusions.

## 2. IRT

IRT represents the probability of an examinee answering an item correctly as a function of the examinee's latent ability variable $\theta$. In the usual dichotomous response formulation of IRT, the correctness of the $i$-th item in a test is indicated by a random response variable $X_{i}$ taking the value 1 for a correct response and 0 for an incorrect response. For example, a two-parameter logistic (2PL) model [4], which is the most popular IRT model, is expressed by

$$
P\left(X_{i}=1 \mid \theta, a_{i}, b_{i}\right)=\frac{1}{1+\exp \left\{-1.7 a_{i}\left(\theta-b_{i}\right)\right\}}
$$

where item parameters $a_{i}$ and $b_{i}$ are called the "discrimination parameter" and "difficulty parameter", respectively.

When the discrimination parameters of all items are equivalent, this model is called the one-parameter logistic model or Rasch model [2]. When one more item parameter, called the "guessing parameter", is added to the 2 PL model, the model is called the three-parameter logistic (3PL) model [4].

The likelihood function of the 2PL model is given by

$$
\begin{aligned}
L(\mathbf{X} \mid \theta, \xi)= & \left[\prod_{j=1}^{N} \prod_{i=1}^{m}\left[\frac{1}{1+\exp \left\{-1.7 a_{i}\left(\theta_{j}-b_{i}\right)\right\}}\right]^{x_{j i}}\right. \\
& {\left[1-\frac{1}{1+\exp \left\{-1.7 a_{i}\left(\theta_{j}-b_{i}\right)\right\}}\right]^{\frac{1-x_{j i}}{}}}
\end{aligned}
$$

where

$$
\begin{aligned}
\mathbf{X} & =\left\{x_{j i}\right\} \quad(j=1, \cdots, N ; i=1, \cdots, m) \\
x_{j i} & =\left\{\begin{array}{l}
0 \quad \text { for the } j \text {-th examinee's incorrect } \\
\text { response to the } i \text {-th item } \\
1 \quad \text { for the } j \text {-th examinee's correct } \\
\text { response to the } i \text {-th item }
\end{array}\right. \\
\theta & =\left\{\theta_{j}\right\} \quad(j=1, \cdots, N) \\
\theta_{j}: & \text { the } j \text {-th examinee's latent ability variable } \\
\xi & =\left\{\xi_{i}\right\} \quad(i=1, \cdots, m) \\
\xi_{i} & =\left(a_{i}, b_{i}\right)^{i} \quad(i=1, \cdots, m) \\
N: & \text { number of examinees } \\
m: & \text { number of items }
\end{aligned}
$$

Equation (2) assumes that a subject's responses to different items are conditionally independent given the variable $\theta$. This assumption is called the "local independence" of items. However, as described in Sect. 1, in actual educational assessment, many factors violate the local independence assumption. For example, Yen [9] pointed out the following causes of local dependence of items: external assistance or interference, speed, fatigue, practice, item or response format, passage dependence, item chaining, explanation of a previous answer, and scoring rubrics or raters.

If we apply the IRT model to data that do not satisfy the local independence assumption, it will suffer seriously biased estimates. Therefore, it is important to detect items that violate the local independence assumption and remove them in order to estimate parameters reliably.

## 3. Previous Work on CI Detection Given a Latent Variable

Several methods for testing CI between a pair of items given a latent variable have been proposed.

Yen [9] proposed the use of the $Q_{3}$ statistic as a score for identifying pairs of items that display CI given a latent variable. The $Q_{3}$ statistic of the $i$-th and $i^{\prime}$-th items is the correlation coefficient of the following $d_{h i}$ and $d_{h i^{\prime}}$ :

$$
d_{h i}=x_{h i}-\hat{P}_{i}\left(\hat{\theta}_{h}\right), d_{h i^{\prime}}=x_{h i^{\prime}}-\hat{P}_{i^{\prime}}\left(\hat{\theta}_{h}\right)
$$

where $x_{h i}$ denotes the score of the $h$-th examinee for the $i$-th item, $\hat{\theta}_{h}$ denotes the estimate of the $h$-th examinee's estimated latent variable, and $\hat{P}_{i}\left(\hat{\theta}_{h}\right)$ represents the probability of the correct answer given the estimated parameters. Actually, $Q_{3}$ requires estimates of latent variables and item parameters. These estimates are obtained assuming local independence of all items, even when some items are locally dependent. Thus, the estimates are biased and cause error in local independence detection. Moreover, $Q_{3}$ has a high computational cost because it requires estimation of the latent variable.

Another statistic suggested for identifying CI given a latent variable is the $G^{2}$ statistic developed by Chen and Thissen [10]. Unlike $Q_{3}, G^{2}$ does not require any estimation of latent variables. The $G^{2}$ statistic is calculated through the following procedure.

Let $N_{x_{i} x_{i^{\prime}}}$ be the number of examinees whose responses to the $i$-th item $X_{i}$ and $i^{\prime}$-th item $X_{i^{\prime}}$ are $x_{i}$ and $x_{i^{\prime}}\left(x_{i}, x_{i^{\prime}}=\right.$ $0,1)$, respectively; let $N$ be the total number of examinees. Under a null hypothesis, the expected number of examinees with $x_{i}$ and $x_{i^{\prime}}$ is given by

$$
\begin{aligned}
E_{x_{i} x_{i^{\prime}}}=N & \int \hat{P}_{i}(\theta)^{x_{i}} \hat{P}_{i^{\prime}}(\theta)^{x_{i^{\prime}}} \\
& {\left[1-\hat{P}_{i}(\theta)\right]^{\frac{1-x_{i}}{}} \left[1-\hat{P}_{i^{\prime}}(\theta)\right]^{\frac{1-x_{i^{\prime}}}{}} p(\theta) d \theta }
\end{aligned}
$$

Here, $\hat{P}_{i}(\theta)$ is the item characteristic curve in which item parameter estimates are substituted. The $G^{2}$ statistic is computed as

$$
G^{2}=2 \sum_{x_{i}=0}^{1} \sum_{x_{i^{\prime}}=0}^{1} N_{x_{i} x_{i^{\prime}}} \log _{e} \frac{N_{x_{i} x_{i^{\prime}}}}{E_{x_{i} x_{i^{\prime}}}}
$$

Although $G^{2}$ integrates out the latent variable, it still requires estimates of item parameters. Since these estimates are obtained under the local independence assumption, the same problem as that of $Q_{3}$ occurs: detection bias caused by parameter estimation bias.

The following simulation experiments demonstrated this problem.

## 4. Problems of Previous Work

Yen's $Q_{3}$ statistic [9] and Chen and Thissen's $G^{2}$ statistic [10] implicitly assume that the CI tests of two items are not affected by the dependencies of any other two items when the latent variable is marginalized out. In this section, we describe how we applied these tests to two locally independent items when some other items were locally dependent.

### 4.1 Method

We considered the following six structures in our simulation experiments.

Three structures each consisted of 7 items. The following three cases were assumed: (a) completely independent case, (b) one pair dependent case, and (c) two pairs dependent case. In case (a), all items are locally independent (Fig. 2). This is the case assumed by traditional methods. In case (b), one pair of items were locally dependent, and the other pairs of the items were locally independent (Fig. 3). In case (c), two pairs of items were locally dependent, and the other pairs of the items were locally independent (Fig. 4).

The other three structures each consisted of 20 items. The following three cases were assumed: (d) completely independent case (Fig. 5), (e) one pair dependent case (Fig. 6), and (f) nine pairs dependent case (Fig. 7). Only case (d) met the assumption of the traditional methods.

For these cases, item parameters were determined as follows.
![img-0.jpeg](img-0.jpeg)

Fig. 3 Case (b) (one pair dependent case).

Parameters of locally independent items In all cases, some items were locally independent of the other items. In Figs. 2-7, such items are not linked to the other items by arcs. Parameters of such items were generated randomly from the following distributions:

$$
\begin{aligned}
\log _{2} a_{i} & \sim N(0,1) \\
b_{i} & \sim N(0,1)
\end{aligned}
$$

Parameters of locally dependent items In cases (b) and (c), some items were assumed to be locally dependent. The responses to some items changed the difficulty of other items. Items that changed difficulty parameters of other items were designated "parent" items, and items with difficulty parameters that were changed by parent items were designated "child" items. Parameters of parent items were generated in the same way as independent items. When an examinee answered the parent item correctly, the difficulty parameter of the child item was assumed to be smaller. Otherwise, that parameter was assumed to be larger. Parameters of child items were generated as

$$
\begin{aligned}
\log _{2} a_{i} & \sim N(0,1) \\
b_{i} & \sim N(0,0.25) \\
d & \sim N(1.85,0.25)
\end{aligned}
$$

![img-1.jpeg](img-1.jpeg)

Fig. 4 Case (c) (two pairs independent case).
![img-2.jpeg](img-2.jpeg)

Fig. 5 Case (d) (completely independent case).
![img-3.jpeg](img-3.jpeg)

Fig. 6 Case (e) (one pair dependent case).
![img-4.jpeg](img-4.jpeg)

Fig. 7 Case (f) (nine pairs independent case).

![img-5.jpeg](img-5.jpeg)

Fig. 8 Frequency distributions of $Q_{3}$ of locally independent pairs (number of items: 7).
![img-6.jpeg](img-6.jpeg)

Fig. 9 Frequency distributions of $Q_{3}$ of locally independent pairs (number of items: 20).

$$
\begin{aligned}
& b_{i 0}=b_{i}+d \\
& b_{i 1}=b_{i}-d
\end{aligned}
$$

where $b_{i 0}$ denotes the difficulty parameter of the $i$-th child item when the answer to the parent item was incorrect, and $b_{i 1}$ denotes the difficulty parameter when the answer to the parent item was correct.

These parameters were used to generate 10,000 examinees' responses randomly. In this way, 1000 sets of data were generated for each case.

In all cases, $X_{1}$ and $X_{2}$ were locally independent. Local independence between $X_{1}$ and $X_{2}$ was tested by Yen's $Q_{3}$ [9] and Chen and Thissen's $G^{2}$ [10].

### 4.2 Results

Frequency distributions of $Q_{3}$ in cases (a), (b), and (c) are shown in Fig. 8. The solid line is the distribution when items other than the target pairs were locally independent, which is a necessary assumption for $Q_{3}$. Compared with the distribution in case (a), values of $Q_{3}$ in cases (b) and (c) were larger.

When the number of items was 20 (Fig. 9), the distributions in cases (e) and (f) did not fit the distribution in case (d).

Frequency distributions of $G^{2}$ in cases (a), (b), and (c) are shown in Fig. 10. In cases (b) and (c), excessively large
![img-7.jpeg](img-7.jpeg)

Fig. 10 Frequency distributions of $G^{2}$ of locally independent pairs (number of items: 7).
![img-8.jpeg](img-8.jpeg)

Fig. 11 Frequency distributions of $G^{2}$ of locally independent pairs (number of items: 20).
values were obtained. Distributions in cases (b) and (c) did not fit the distribution in case (a).

However, when the number of items was 20 (Fig. 11), the distribution in case (e) fitted the distribution in case (d). On the other hand, the distribution in case (f) did not fit the distribution in case (d).

These results show that, when the number of locally dependent items other than the targets increases, the statistics of traditional CI tests are seriously biased. Therefore, this bias might cause bias of CI detection.

## 5. Proposed Method

The traditional CI tests implicitly assume that all items except the two target items are conditionally independent given a latent variable. However, our simulation experiment revealed that these CI tests are biased when this assumption does not hold. Here, we propose a new method to solve this problem. Our method uses the Bayesian network IRT model [14], which alleviates the local independence assumption of traditional IRT models.

### 5.1 Bayesian Network IRT

Bayesian network IRT [14] is an IRT model that relaxes the CI assumption given a latent variable. This model introduces different item parameters for responses to other items. An item whose response changes the item parameter value

![img-9.jpeg](img-9.jpeg)

Fig. 12 Example of the structure of items and the latent variable.
of the $i$-th item is designated the parent item of the $i$-th item. Consequently, the Bayesian network IRT model is regarded as an IRT model containing parent items. This model is described in detail below.

Let a certain examinee's response pattern to $m$ items be

$$
\mathbf{x}=\left(x_{1}, x_{2}, \cdots, x_{i}, \cdots, x_{m}\right)^{\prime}
$$

where

$$
x_{i}=\left\{\begin{array}{ll}
0 & \text { for an incorrect response } \\
1 & \text { for a correct response }
\end{array} .\right.
$$

When $B_{s}$ encodes the CI assertions in a model, the joint probability of scores is given by

$$
\begin{aligned}
& P\left(X_{1}=x_{1}, \cdots, X_{m}=x_{m} \mid \theta, \xi, B_{s}\right) \\
= & \prod_{i=1}^{m} \prod_{j=0}^{2^{i_{1}}-1}\left\{P\left(X_{i}=1 \mid \theta, \xi_{i}, \tilde{\mathbf{X}}_{i j}\right)^{x_{i} u_{i j}}\right. \\
& \left.\left[1-P\left(X_{i}=1 \mid \theta, \xi_{i}, \tilde{\mathbf{X}}_{i j}\right)\right]^{\left(1-x_{i}\right) u_{i j}}\right\}
\end{aligned}
$$

where

$$
\begin{aligned}
u_{i j}= & \left\{\begin{array}{ll}
1 & \text { for the } j \text {-th response pattern to parent } \\
& \text { items of the } i \text {-th item } \\
0 & \text { for the other patterns }
\end{array}\right. \\
p_{i}: & \text { number of parent items of the } i \text {-th item, } \\
\tilde{\mathbf{X}}_{i j}: & j \text {-th response pattern to parent items of } \\
& \text { the } i \text {-th item, } \\
\xi_{i}: & \text { parameter vector for } \tilde{\mathbf{X}}_{i j} \\
\xi= & \left(\xi_{1}^{\prime}, \xi_{2}^{\prime}, \cdots, \xi_{i}^{\prime}, \cdots, \xi_{m}^{\prime}\right) \\
B_{s}: & \text { conditional dependence structure among items }
\end{array}
\end{aligned}
$$

The dependence structure among items in the Bayesian network IRT model can be expressed as a directed graph. In the graph, two conditionally dependent items are linked by a directed arc, whereas conditionally independent items are not linked. The direction of the arc indicates the parent and child: the arc's tail is the parent item and its head is the child item. For example, in the structure shown in Fig. 12, dependencies exist between $X_{3}-X_{4}, X_{3}-X_{5}$, and $X_{4}-X_{5} . X_{3}$ is the parent of $X_{4}$ and $X_{5}$, and $X_{4}$ is the parent of $X_{5}$.

Bayesian network IRT can express a conditional item characteristic curve given the responses to other items. For example, item 3 in Fig. 12 is the parent item of item 4, and the item characteristic curve of item $4 P\left(X_{4}=1 \mid \theta, \xi_{4}, \tilde{\mathbf{X}}_{4 j}\right)$ can be written as

$$
\begin{aligned}
& P\left(X_{4}=1 \mid \theta, \xi_{4}, \tilde{\mathbf{X}}_{4 j}\right) \\
= & \prod_{j=0}^{1} P\left(X_{4}=1 \mid \theta, \xi_{4}, \tilde{\mathbf{X}}_{4 j}\right)^{u_{4 j}} \\
= & P\left(X_{4}=1 \mid \theta, a_{4}, b_{40}, b_{41}, X_{3}=0\right)^{u_{40}} \\
& P\left(X_{4}=1 \mid \theta, a_{4}, b_{40}, b_{41}, X_{3}=1\right)^{u_{41}}
\end{aligned}
$$

where $a_{4}$ is the discrimination parameter of item 4 and $b_{4 x_{3}}$ is the difficulty parameter of item 4 when the response to item 3 is $x_{3}\left(x_{3}=0,1\right)$.

In this paper, we use the concept of this model to propose a new CI test given a latent variable.

Furthermore, it should be noted that in Bayesian network IRT, the order of test items should be fixed because the parameter estimates are affected by the order. However, our purpose in this paper is to detect the local dependency of two items, so the detection results are not affected by varying the order.

### 5.2 Conditional Mutual Information Measure

The conditional mutual information measure is a measure of dependence between two random variables. It is used for learning the Bayesian network skeletons, for example, in the PC algorithm [15] and MMPC algorithm [16]. When $X, Y$, and $\mathbf{Z}$ are random variables, the conditional mutual information between $X$ and $Y$ given $\mathbf{Z}$, which is written as $I(X ; Y \mid \mathbf{Z})$, is calculated as follows.

$$
\begin{aligned}
& I(X ; Y \mid \mathbf{Z}) \\
= & \sum_{x} P(\mathbf{Z}=\mathbf{z}) \\
& \sum_{x} \sum_{y} P(X=x, Y=y \mid \mathbf{Z}=\mathbf{z}) \\
& \log _{2} \frac{P(X=x, Y=y \mid \mathbf{Z}=\mathbf{z})}{P(X=x \mid \mathbf{Z}=\mathbf{z}) P(Y=y \mid \mathbf{Z}=\mathbf{z})}
\end{aligned}
$$

Moreover, in the Bayesian network IRT model [14], conditional dependence between two items given a latent variable is measured using the following conditional mutual information measure.

$$
\begin{aligned}
& I\left(X_{i} ; X_{i^{\prime}} \mid \theta, \xi, B_{s}\right) \\
= & \int p(\theta) \\
& \sum_{x_{i}=0}^{1} \sum_{x_{i^{\prime}}=0} P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \theta, \xi, B_{s}\right) \\
& \log _{2} \frac{P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \theta, \xi, B_{s}\right)}{P\left(X_{i}=x_{i} \mid \theta, \xi, B_{s}\right) P\left(X_{i^{\prime}}=x_{i^{\prime}} \mid \theta, \xi, B_{s}\right)} d \theta
\end{aligned}
$$

To calculate Eq. (10), we need to know the structure $B_{s}$ and item parameters $\xi$. In this study, we assumed a structure $B_{s}$ in which all items are mutually dependent (Fig. 13).

![img-10.jpeg](img-10.jpeg)

Fig. 13 Structure of $B_{s}^{c}$ (completely dependent structure given a latent variable).

Such a structure is designated as a completely dependent structure (complete graph) and denoted $B_{s}^{c}$. The direction of the arc from a previously shown item to a later shown item is determined by the test item order.

Let the target items be $X_{i}$ and $X_{i^{\prime}}$. Assuming $B_{s}^{c}$ means that all items except the targets, which are denoted $\mathbf{X}^{-i i^{\prime}}$, are regarded as parents of the targets. In this case, if the topology order of items is given, the conditional probabilities given $\mathbf{X}^{-i i^{\prime}}$ correspond to the conditional probabilities given the estimated latent ability variable $\hat{\theta}$ because, according to Neyman factorization theorem [17], an examinee's response pattern is sufficient for estimation of the latent variable $\theta$ when the number of items is sufficiently large. Consequently, in this study we define the following $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)$, in which an examinee's response pattern $\mathbf{X}^{-i i^{\prime}}$ substitutes for his/her latent ability variable $\theta$ in Eq. (10).
Definition 1: $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)$

$$
\begin{aligned}
& =\sum_{j=0}^{2^{m-2}-1} P\left(\mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}} \mid \xi, B_{s}^{c}\right) \\
& \quad \sum_{x_{i}=0}^{1} \sum_{x_{i^{\prime}}=0}^{1} P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right) \\
& \log _{2} \frac{P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)}{P\left(X_{i}=x_{i} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right) P\left(X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)}
\end{aligned}
$$

where
$m:$ number of items
$X_{i}: i$-th item
$X_{i^{\prime}}: i^{\prime}$-th item
$\mathbf{X}^{-i i^{\prime}}:$ all items except $X_{i}$ and $X_{i^{\prime}}$
$\mathbf{x}_{j}^{-i i^{\prime}}: j$-th response pattern to $\mathbf{X}^{-i i^{\prime}}$

$$
(j=0, \cdots,\left(2^{m-2}-1\right))
$$

$\xi$ : item parameters of the model
$B_{s}^{c}$ : parent variable set of the $i$-th and $i^{\prime}$-th items with a completely dependent structure
![img-11.jpeg](img-11.jpeg)

Fig. 14 Graph showing when $\theta$ is integrated out from the graph of Fig. 12.

Namely, $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)$ is the conditional mutual information measure between $X_{i}$ and $X_{i^{\prime}}$ given all items except $X_{i}$ and $X_{i^{\prime}}$.

Using Eq. (11), we can derive the following theorem.
Theorem 1: When $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)=0$ for $\forall i, i^{\prime}$, the $i$-th and $i^{\prime}$-th items are conditionally independent given a latent variable.

When $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)>0$ for $\forall i, i^{\prime}$, the $i$-th and $i^{\prime}$ th items are conditionally dependent given a latent variable.

Proof 1: For $\forall i, i^{\prime}, j$,

$$
\begin{aligned}
& \sum_{x_{i}=0}^{1} \sum_{x_{i^{\prime}}=0}^{1} P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right) \\
& \log _{2} \frac{P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)}{P\left(X_{i}=x_{i} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right) P\left(X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)}
\end{aligned}
$$

Then, $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)=0$ when and only when

$$
\begin{aligned}
& P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right) \\
= & P\left(X_{i}=x_{i} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right) \\
& P\left(X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{s}^{c}\right)
\end{aligned}
$$

When all items are assumed to depend on the latent variable $\theta$, as shown in Fig. 12, for $\forall i, i^{\prime}$, both the $i$-th and $i^{\prime}$ th items are made marginally dependent by integrating out $\theta$ : the dependence structure of the items is a probability network model of a completely dependent structure, as shown in Fig. 14. An examinee's response pattern is sufficient for estimation of the ability variable $\theta$. Neyman factorization theorem [17] states that, when $\mathbf{x}=\left(x_{1}, \ldots, x_{n}\right)$ is a random variable with probability density function $f(\mathbf{x} ; \theta)$, a necessary and sufficient condition for a statistic $t(\mathbf{x})$ to be sufficient for $\theta$ is that

$$
f(\mathbf{x} ; \theta)=q(t(\mathbf{x}) ; \theta) \cdot r(\mathbf{x})
$$

where $q(t(\mathbf{x}) ; \theta)$ is the probability density function of $t(\mathbf{x})$ and $r(\mathbf{x})$ is a function of $\mathbf{x}$ that does not depend on $\theta$. In Eq (7), the values of the variables $\tilde{\mathbf{X}}_{i j}, x_{i}$, and $u_{i j}$ are fixed when an examinee's response pattern $\mathbf{x}$ is given. Consequently, Eq (7) can be regarded as the probability function of

the response pattern $\mathbf{x}$ given parameters $\theta, \xi$, and $B_{x}$. Therefore, the response pattern is sufficient for estimating $\theta$ when $\xi$ and $B_{x}$ are given, so $\theta$ in (10) can be replaced by the corresponding response pattern.

For sufficiently large $m$,

$$
p\left(\theta \mid \mathbf{X}, \xi, B_{x}^{c}\right) \approx p\left(\theta \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)
$$

These are the main ideas of this paper.
Accordingly, if

$$
\begin{aligned}
& P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{x}^{c}\right) \\
= & P\left(X_{i}=x_{i} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{x}^{c}\right) \\
& P\left(X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)
\end{aligned}
$$

for $\forall i, i^{\prime}, j$, then

$$
\begin{aligned}
& P\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \theta, \xi, B_{x}^{c}\right) \\
= & P\left(X_{i}=x_{i} \mid \theta, \xi, B_{x}^{c}\right) \cdot P\left(X_{i^{\prime}}=x_{i^{\prime}} \mid \theta, \xi, B_{x}^{c}\right)
\end{aligned}
$$

Consequently, when $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)=0$ for $\forall i, i^{\prime}$, the $i$-th and $i^{\prime}$-th items are conditionally independent. In the same manner, when $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)>0$ for $\forall i, i^{\prime}$, the $i$-th and $i^{\prime}$-th items are conditionally dependent.

Equation (11) includes four conditional probabilities, which are parameters of Bernoulli distributions. The maximum likelihood estimates of those parameters are obtainable as

$$
\begin{aligned}
& \hat{P}\left(\mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}} \mid \xi, B_{x}^{c}\right)=\frac{N_{j}}{N} \\
& \hat{P}\left(X_{i}=x_{i}, X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)=\frac{N_{x_{i} x_{i^{\prime}} j}}{N_{j}} \\
& \hat{P}\left(X_{i}=x_{i} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)=\frac{N_{x_{i} j}}{N_{j}} \\
& \hat{P}\left(X_{i^{\prime}}=x_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}=\mathbf{x}_{j}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)=\frac{N_{x_{i^{\prime}}} j}{N_{j}}
\end{aligned}
$$

where the number of examinees whose response pattern is $\mathbf{x}_{j}^{-i i^{\prime}}$ is defined as $N_{x_{i} x_{i^{\prime}}} j$, and

$$
\begin{aligned}
N_{x_{i} j} & =N_{x_{i} 0 j}+N_{x_{i} 1 j} \\
N_{x_{i^{\prime} j}} & =N_{0 x_{i^{\prime} j}}+N_{1 x_{i^{\prime} j}} \\
N_{j} & =N_{00 j}+N_{01 j}+N_{10 j}+N_{11 j} \\
N & =\sum_{j=0}^{2^{m-2}-1} N_{j}
\end{aligned}
$$

Substituting them into Eq. (11), we get the proposed conditional mutual information measure between the $i$-th and $i^{\prime}$-th items as follows.

$$
I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)
$$

![img-12.jpeg](img-12.jpeg)

Fig. 15 Frequency distributions of LCI test statistic of locally independent pairs (number of items: 7).

$$
\begin{aligned}
& =\sum_{j=0}^{2^{m-2}-1} \frac{N_{j}}{N} \sum_{x_{i}=0}^{1} \sum_{x_{i^{\prime}}=0}^{1} \frac{N_{x_{i} x_{i^{\prime}}} j}{N_{j}} \log _{2} \frac{\frac{N_{x_{i} x_{i^{\prime}}} j}{N_{j}}}{\frac{N_{x_{i} j}}{N_{j}} \frac{N_{x_{i^{\prime}}} j}{N_{j}}} \\
& =\frac{1}{N} \sum_{j=0}^{2^{m-2}-1} \sum_{x_{i}=0}^{1} \sum_{x_{i^{\prime}}=0} N_{x_{i} x_{i^{\prime}}} j \log _{2} \frac{N_{x_{i} x_{i^{\prime}}} j N_{j}}{N_{x_{i} j} N_{x_{i^{\prime}}} j}
\end{aligned}
$$

The response pattern $\mathbf{X}^{-i i^{\prime}}$ contains a lot of missing data. If we ignore the missing data, then Eq (21) can be transformed into

$$
\begin{aligned}
& I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{x}^{c}\right) \\
= & \frac{1}{N} \sum_{j^{\prime}=0}^{J^{\prime}-1} \sum_{x_{i}=0}^{1} \sum_{x_{i^{\prime}}=0} N_{x_{i} x_{i^{\prime}}} j^{\prime} \log _{2} \frac{N_{x_{i} x_{i^{\prime}}} j^{\prime} N_{j^{\prime}}}{N_{x_{i} j} N_{x_{i^{\prime}}} j^{\prime}}
\end{aligned}
$$

where $J^{\prime}$ is the number of observed patterns. Therefore, even though the number of items $m$ is large, the actual amount of computation is $O(N)$. According to Eqs. (3) and (4), the amount of computation for traditional CI tests is also $O(N)$.

As mentioned in Proof 1, the main idea of this paper is to obtain the conditional probability given a latent variable, with replacing $\theta$ by $\mathbf{X}^{-i i^{\prime}}$ using Neyman's theorem. This reduces the computational costs to $O(N)$ from $O\left(2^{m}\right)$. That is, the amount of computation for our method is the same as that for traditional methods.

Using $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{x}^{c}\right)$ in Eq. (22), we can define the following latent conditional independence (LCI) test given a latent variable.

Definition 2: (Latent conditional independence (LCI) test)
If $I\left(X_{i} ; X_{i^{\prime}} \mid \mathbf{X}^{-i i^{\prime}}, \xi, B_{x}^{c}\right) \geq \varepsilon$
$\rightarrow$ the $i$-th and $i^{\prime}$-th items are conditionally dependent when a latent variable is given
else
$\rightarrow$ the $i$-th and $i^{\prime}$-th items are conditionally independent when a latent variable is given,
where $\varepsilon$ is a certain threshold.

![img-13.jpeg](img-13.jpeg)

Fig. 16 Frequency distributions of LCI test statistic of locally independent pairs (number of items: 20).

The LCI test can correctly detect CI given a latent variable even when items other than the target pairs are mutually dependent. When the LCI test was applied to the same simulation data as used in Sect. 4, differences between the distributions were reduced (Figs. 15 and 16). It means that the LCI test was not affected by other item dependencies.

## 6. Evaluation of LCI Test

This section evaluates how correctly the LCI test can detect CI between two items given a latent variable.

### 6.1 Method

When a data set contains locally dependent items and a CI test is applied to such a data set, item pairs are classified into one of four categories:

- dependent pairs incorrectly judged as independent (a)
- dependent pairs correctly judged as dependent (b)
- independent pairs correctly judged as independent (c)
- independent pairs incorrectly judged as dependent (d)

To evaluate the performances of detecting local dependencies, we obtained ratio $a /(a+b)$. Moreover, we also obtained ratio $c /(c+d)$ to evaluate performances of detecting local independencies.

In Sect. 4, we generated data that contained locally dependent pairs of items. We applied the proposed LCI test and two traditional CI tests to these data and calculated the two abovementioned ratios.

Furthermore, we generated data using the structure (Fig. 17) estimated from an actual test [14], which is called "case (g)". The estimated item parameters are given in Appendix A. For details of item contents, see [14]. The number of examinees was 10,000 , and 10 sets of data were generated.

For all the experiments, $0.01,0.05$, and 0.10 were used as the LCI test thresholds $\varepsilon$, and performances were compared.

### 6.2 Results

The results for cases (b) and (c) are given in Table 1. All CI
![img-14.jpeg](img-14.jpeg)

Fig. 17 Structure from actual test (Note: although the latent variable $\theta$ is implicit in this graph, all items depend on $\theta$.).

Table 1 Average ratio of correctly detected dependencies and independencies (number of items: 7).


tests detected more than 90 percent of the local dependencies, and $G^{2}$ detected the greatest number of local dependencies. However, traditional CI tests often failed to detect local independencies, whereas the LCI test detected local independencies with high accuracy. This means that the LCI test could avoid overfitting problems which the traditional CI tests suffered from in these cases.

The results for cases (e) and (f) are given in Tables 2. Although the overfitting problem of $G^{2}$ was mitigated in case (e), $G^{2}$ still suffered from this problem in case (f). When $\varepsilon$ was 0.01 or 0.05 , the LCI test also failed to detect local independencies. However, when $\varepsilon$ was 0.10 , the LCI test kept high accuracy for detecting both dependencies and independencies in cases (e) and (f).

The results for case (g) is given in Table 3. Whereas $G^{2}$ and $Q_{3}$ often failed to detect local independencies, the LCI test detected both dependencies and independencies accurately when $\varepsilon$ was 0.01 . However, when $\varepsilon$ was 0.10 , the LCI test failed to detect local dependencies. Therefore, for the LCI test, a method of investigating an appropriate $\varepsilon$ must be explored.

Summarizing the results, we can say that traditional CI tests suffer from the overfitting. On the other hand, when

Table 2 Average ratio of correctly detected dependencies and independencies (number of items: 20).


Table 3 Average ratio of correctly detected dependencies and independencies (case (g)).


an appropriate threshold is determined, the LCI test can correctly detect both local independence and local dependence. However, since the performance of the LCI test is highly sensitive to the choice of threshold $\varepsilon$, a suitable method of determining the threshold, for example, by bootstrapping or cross validation, must be used.

## 7. Application to Real Data

In this section, our method is applied to real data.

### 7.1 Method

A mathematics test answered by 367 freshmen at five national universities in Tokyo was analyzed. The test contained seven items. Items Q1, Q2, and Q3 were questions about inequalities of the second degree, and Q3 required the correct response to Q2. Items Q4, Q5, Q6, and Q7 were questions about logical expressions. See Appendix B for details.

### 7.2 Results

The values of the LCI test statistics are given in Table 4. When the threshold $\varepsilon$ was 0.10 , only Q 2 and Q 3 were locally dependent. In contrast, when $\varepsilon$ was 0.01, 17 out of 21 pairs were locally dependent. In this section, we interpret the result when $\varepsilon$ was 0.05 . Pairs of items that were judged to be locally dependent are shown linked in Fig. 18.

Between the second-degree-inequality items (Q1, Q2, and Q3) and the logical-expression items (Q4, Q5, Q6, and Q7), almost all values of LCI statistics were smaller than $\varepsilon$. In contrast, within the logical-expression items, most of the

Table 4 LCI test statistics for seven items of a real test.


![img-15.jpeg](img-15.jpeg)

Fig. 18 Pairs whose LCI statistics were greater than 0.05 .
values were larger than $\varepsilon$. These results indicate that items belonging to different areas were locally independent given a latent variable.

The largest LCI was between Q2 and Q3. Since Q3 explicitly required the correct response to Q2, this local dependence might reflect the item makers' intentions.

Within the logical-expression items (Q4, Q5, Q6, and Q7), four pairs were judged to be locally dependent. These four items share the same alternatives. Such sharing of alternatives might cause local dependence.

## 8. Conclusion

In this study, we investigated the latent conditional independence (LCI) test given a latent variable to detect conditionally independent items. The performances were compared with those of traditional conditional independence (CI) tests such as $Q_{3}$ and $G^{2}$. There were two main findings.

First, when some items that are not targets are conditionally dependent given a latent variable, traditional CI test statistics are seriously biased. On the other hand, the LCI test statistic is robust irrespective of other items. Secondly, when an appropriate threshold $\varepsilon$ is chosen, the LCI test can detect both local independencies and local dependencies, whereas traditional CI tests often fail to detect local independencies. The application of the LCI test to actual data suggests that the sharing of alternatives might cause conditional dependence.

However, some problems remain unsolved. As described in this paper, we knew which item was the parent because items in the test data were sequentially arrayed. For cases in which directions are unknown, a method of determining the parent item is necessary. In addition, the performance of the LCI test is highly sensitive to the choice of $\varepsilon$. Therefore, methods of determining an appropriate value of $\varepsilon$, for example, by bootstrapping or, cross validation, should be used. When these problems have been solved, the LCI test should be more useful.

## Appendix B: Test Used in Section 7

Please answer Q1 through Q7.
[1] In a rectangle $\mathrm{ABCD}, \mathrm{AB}=\mathrm{CD}=8$ and $\mathrm{BC}=\mathrm{DA}=$ 12. For a point P on side AB , a point Q on side BC , and a point R on side CD , the following relation holds.

$$
\mathrm{AP}=\mathrm{BQ}=\mathrm{CR}
$$

Let $\mathrm{AP}=x(0<x<8)$.
Q1. The area of the trapezoid PBCR is ?.
Q2. The area of $\triangle \mathrm{PQR}$ is

$$
S=x^{2}-\square x+\square
$$

Q3. If $S<24$ holds, then $x$ must be in the range of

$$
\square<x<\square
$$

[2] Fill in boxes $\mathrm{A} \quad$ through $\mathrm{D} \quad$ selecting for each box one option from (1) through (3) below. You may select the same options as many times as you wish.
$m$ and $n$ are natural numbers. There are three conditions: $p, q$, and $r$.
$p: \quad m+n$ is divisible by 2 .
$q: \quad n$ is divisible by 4 .
$r: \quad m$ is divisible by 2 , and $n$ is divisible by 4 .
Let the negation of condition $p$ be $\bar{p}$ and let the negation of condition $r$ be $\bar{r}$. Then,
Q4. $p$ is $\mathrm{A} \quad$ for $r$.
Q5. $\bar{p}$ is $\mathrm{B} \quad$ for $\bar{r}$.
Q6. " $p$ and $q$ " is $\mathrm{C} \quad$ for $r$.
Q7. " $p$ or $q$ " is $\mathrm{D} \quad$ for $r$.
(1) a necessary and sufficient condition
(1) a necessary condition but not a sufficient condition
(2) a sufficient condition but not a necessary condition
(3) neither a necessary condition nor a sufficient condition
![img-16.jpeg](img-16.jpeg)

Takamitsu Hashimoto received an M.A. degree from the University of Tokyo in 2002. He was a research associate at the National Center for University Entrance Examinations in 2004 and has been an assistant professor since 2007. Since 2009, he has been a student at the University of Electro-Communications. His research interests include Bayesian statistics and test theory.
![img-17.jpeg](img-17.jpeg)

Maomi Ueno received an M.Ed. degree from Kobe University in 1992 and a Ph.D. degree from Tokyo Institute of Technology in 1994. He was a research associate at Tokyo Institute of Technology in 1994 and an associate professor at Nagaoka University of Technology in 2000. Since 2006, he has been an associate professor at the University of ElectroCommunications. His research interests include e-Learning, Bayesian statistics, and data mining. He received a prize from the Behaviormetric Society of Japan in 2004, an outstanding paper award from e-Learn 2004, a prize from the Japanese Society for Information and Systems in Education in 2005, and an outstanding paper award from e-Learn 2007. He is an executive board member of the Japanese Society for Educational Technology, an executive of the Behaviormetric Society of Japan, and a member of the council of Japanese Society for Information and Systems in Education. He was an IEEE Computer society ICALT2007 Chair.