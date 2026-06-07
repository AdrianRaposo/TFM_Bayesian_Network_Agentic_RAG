# RESEARCH ARTICLE 

## Using $k$-dependence causal forest to mine the most significant dependency relationships among clinical variables for thyroid disease diagnosis

LiMin Wang ${ }^{1}$, FangYuan Cao ${ }^{1}$, ShuangCheng Wang ${ }^{2}$, MingHui Sun ${ }^{1 *}$, LiYan Dong ${ }^{1 *}$<br>1 Key Laboratory of Symbolic Computation and Knowledge Engineering of Ministry of Education, Jilin University, ChangChun City 130012, China, 2 Lixin Accounting Research Institute, Shanghai Lixin University of Commerce, Shanghai City 201620, China<br>* smh@jlu.edu.cn (MHS); dongly@jlu.edu.cn (LYD)

## Abstract

Numerous data mining models have been proposed to construct computer-aided medical expert systems. Bayesian network classifiers (BNCs) are more distinct and understandable than other models. To graphically describe the dependency relationships among clinical variables for thyroid disease diagnosis and ensure the rationality of the diagnosis results, the proposed $k$-dependence causal forest (KCF) model generates a series of submodels in the framework of maximum spanning tree (MST) and demonstrates stronger dependence representation. Friedman test on 12 UCI datasets shows that KCF has classification accuracy advantage over the other state-of-the-art BNCs, such as Naive Bayes, tree augmented Naive Bayes, and $k$-dependence Bayesian classifier. Our extensive experimental comparison on 4 medical datasets also proves the feasibility and effectiveness of KCF in terms of sensitivity and specificity.

## Background

Data mining [1] [2] is used to extract unknown but potentially useful information by using available incomplete, noisy, fuzzy, and random practical application data. The medical domain consists of a considerable amount of data, including complete human genetic code information; clinical information on the history of patients, diagnosis, inspection, and treatment; and drug management information. Data mining can be applied in the medical field to analyze medical data, extract implicit valuable information, provide correct diagnosis and treatment, and study the genetic law of human diseases and health [3].

While dealing with a large amount of historical information of patients in the database, data mining needs to confirm the diagnosis based on age, gender, auxiliary examination results, and physiological and biochemical indicators of patients. Thus, data mining should eliminate interference of human factors and establish diagnosis rules with good universality, provided that large amounts of data are analyzed in the process. Consequently, researchers can

archive.ics.uci.edu/ml/datasets/Breast+Cancer +Wisconsin+\%28Original\%29 Pima Indians Diabetes https://archive.ics. uci.edu/ml/datasets/Pima+Indians+Diabetes TicTac-Toe- https://archive.ics. uci.edu/ml/datasets/Tic-Tac-Toe+Endgame German- https://archive.ics. uci.edu/ml/datasets/Stattog+\%28German+Credit +Data\%29 Spambase https:// archive.ics.uci.edu/ml/datasets/Spambase Mushroom- https://archive.ics. uci.edu/ml/datasets/Mushroom Adult https://archive.ics.uci.edu/ml/ datasets/Adult Census Income- https://archive.ics.uci. edu/ml/datasets/Census+Income.

Funding: This work was supported by the National Science Foundation of China (Grant No. 61272209) and the Agreement of Science \& Technology Development Project, Jilin Province (No. 20150101014JC). The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

Competing interests: The authors have declared that no competing interests exist.
establish a prediction model, test it, and construct an accurate algorithmic model, which can be used for diagnosis of clinical medical conditions.

Now, about 20 million Americans have some form of thyroid disease, and people of all ages and races can have the chance to get thyroid disease [4]. Recently, a fair mount of data mining methods have been investigated to diagnose this kind of disease. To explore the value of con-trast-enhanced ultrasound combined with conventional ultrasound in the diagnosis of thyroid microcarcinoma, multivariate logistic regression analysis is performed to determine independent risk factors [5]. Proper interpretation of the thyroid data besides clinical examination and complementary investigation is an important issue, a comparative study of thyroid disease diagnosis is made by using three different types of neural networks, i.e. multilayer neural network, probabilistic neural network and learning vector quantization neural network [6]. An enhanced fuzzy $k$-nearest neighbor (FKNN) classifier based computer aided diagnostic system is presented for thyroid disease [4]. The neighborhood size $k$ and the fuzzy strength parameter $m$ in FKNN classifier are adaptively specified by the particle swarm optimization approach. The application of Support Vector Machines is proposed to classify thyroid bioptic specimens [7], together with a particular wrapper feature selection algorithm (i.e., recursive feature elimination). The model is able to provide an accurate discriminatory capability using only 20 out of 144 features, resulting in an increase of the model performances, reliability, and computational efficiency. To elucidate the cytological characteristics and the diagnostic usefulness of intraoperative cytology for papillary thyroid carcinoma, decision tree analysis is used to find effective features for accurate cytological diagnosis [8].

Bayesian method is an intelligent computing method used in reasoning and managing uncertainty problems [9]. BNC is a probability network based on graphical models used to provide probabilistic inference, thus it is more distinct and understandable than other methods. A BNC consists of a structural model and a set of conditional probabilities. The structural model is a directed acyclic graph, in which nodes represent classes $C$ and a set of random attributes $\mathbf{X}=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$. Arcs between nodes are used to describe the conditional dependence relationships, which are quantified using conditional probabilities for each node given to the parents. Bayesian methods have gained increasing interest in medical diagnosis. BN and graph theory are used to encode causal relations among variables for diagnosis and predictions in the medical domain [10-12].

The Markov blanket of a target attribute is the minimal attribute set for explaining the target attribute based on the conditional independence of all the attributes to be connected in a BN [13]. Koller and Sahami [14] defined the Markov blanket of a target attribute as the minimal set of conditioned attributes, in which all other attributes are independent of the target attribute in the probabilistic graphical model. Hence, the Markov blanket of a target attribute removes unnecessary attributes and represents the minimal information for explaining the target attribute. In a BN model, the Markov blanket of $T$, i.e., $\mathrm{MB}(T)$ is the union of parent, child, and parent of children nodes of $T[13,15]$. For example, in Fig 1, the parent nodes of $T$ are $B$ and $C$, the child node of $T$ is $F$, and the parent of the children node of $T$ is $E$. Thus, the Markov blanket of $T$ is $\mathrm{MB}(T)=\{B, C, F, E\}$, indicating that nodes $A, D$, and $G$ are independent of $T$ conditioned on $\mathrm{MB}(T)$.

The performance of a classifier is evaluated using two key factors, namely, classification accuracy and space complexity of a model. A BN cannot express all relationships between the attributes and the class. Thus, a trade-off should exist between the structure complexity and classification accuracy. Some restricted Bayesian classifiers, e.g., Naive Bayes (NB), tree augmented Naive Bayes (TAN), and $k$-dependence BNs (KDB), exhibit satisfactory performance for classification at different levels of conditional independence assumption. When carrying out medical analysis, different doctors may consider different factor or attribute as starting

![img-0.jpeg](img-0.jpeg)

Fig 1. An example Markov blanket.
https://doi.org/10.1371/journal.pone.0182070.g001
point. One BNC is unable to express this diversity. This paper proposes a novel learning algorithm called the $k$-dependence causal forest (KCF). This algorithm generates a series of submodels, which are used to construct classifiers with different root nodes at arbitrary points (values of $k$ ) along the attribute dependence spectrum. The KCF algorithm aims to describe the significant dependency relationships between root node $X_{r}$ and $\operatorname{MB}\left(X_{r}\right)$ while simultaneously providing accurate diagnosis to patients with thyroid diseases.

# Materials and methods 

## Data

This research work adopts the public thyroid disease dataset from the University of California, Irvine (UCI) Machine Learning Repository [16]. The UCI database currently contains 335 datasets, and the number of sets continuously increases. The thyroid disease dataset was stored in the UCI by Ross Quinlan during his visit in 1987 for the 1987 Machine Learning Workshop; the set contains 9172 real historical instances. Each instance consists of 29 attributes, which can be classified into 20 classes. The characteristics of thyroid disease dataset are multivariate and domain theory, the characteristics of the contained attributes are categorical and real, and the associated task of the dataset is classification.

## Three restricted Bayesian classifiers

BNs are often used to solve classification problems by constructing classifiers from a given set of training instances with class labels. With high classification accuracy and efficiency, BN classifiers perform outstandingly in a number of classification methods. This paper briefly introduces the three popular restricted Bayesian classifiers. In the following discussion, capital letters, such as $X, Y$ and $Z$, denote attribute names, and lower-case letters, such as $x, y$ and $z$, denote the specific values taken by those attributes. Sets of attributes are denoted by boldface capital letters, such as $\boldsymbol{X}, \boldsymbol{Y}$ and $\boldsymbol{Z}$, and assignments of values to the attributes in these sets are denoted by boldface lowercase letters, such as $\mathbf{x}, \mathbf{y}$ and $\mathbf{z}$.

The NB classifier is the simplest BN model and is very robust [17]. Given the $n$ independent attributes $\mathbf{X}=\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ and $m$ classes $c_{1}, c_{2}, \ldots, c_{m}$, classification will derive the


![img-1.jpeg](img-1.jpeg)

Fig 2. An example of conditional mutual information matrix (a) and corresponding undirected MST (b). Attributes $\left(X_{2}, X_{17}, X_{19}, X_{21}, X_{23}\right.$, $\left.X_{25}\right]$ correspond to clinical variables on thyroxine, TSH, T3, TT4, T4U and FTI, respectively.
https://doi.org/10.1371/journal.pone.0182070.g002
maximum of $P\left(c_{i} \mid x\right)$, where $1 \leq i \leq m$. Result can be derived from the Bayesian theorem, as Eq (1) shows:

$$
P\left(c_{i} \mid x\right)=\frac{P\left(c_{i}\right) P\left(x \mid c_{i}\right)}{P(x)}
$$

The rigorous assumption in NB is that all attributes are conditionally independent of each other. Thus, the class assignments of the test samples are based on Eq (2).

$$
\arg \max _{c_{i}} P\left(c_{i}\right) P\left(x \mid c_{i}\right)=\arg \max _{c_{i}} P\left(c_{i}\right) \prod_{j=1}^{n} P\left(x_{j} \mid c_{i}\right)
$$

The basic framework of TAN [18] is the extension of the Chow-Liu tree [19], which utilizes conditional mutual information to build a maximum spanning tree (MST). TAN is a onedependence classifier because it allows each attribute to have at most one parent in addition to the class. In practice, TAN is regarded as a good trade-off between the model complexity and classification performance. Fig 2 shows an example of the condition mutual information matrix with six attributes and corresponding undirected MST. The selected six attributes are the first few attributes with the maximum mutual information with class $I\left(X_{i} ; C\right)$ in the thyroid disease dataset.

For a TAN model, the class assignments of the test samples are based on Eq (3).

$$
\arg \max _{c_{i}} P\left(c_{i}\right) P\left(x \mid c_{i}\right)=\arg \max _{c_{i}} P\left(c_{i}\right) \prod_{j=1}^{n} P\left(x_{j} \mid c_{i}, x_{j p}\right)
$$

where $X_{j p}$ is the parent node of $X_{j}$.
After selecting each attribute as the root node and setting the outward direction of all the arcs from the attributes, six different directed MSTs are generated, as shown in Fig 3. The root node is filled in black. The directed MSTs can be regarded as different representations of the same spectrum of causal relationships under different conditions. One MST corresponds to $n$ directed trees, and each tree uses different attributes as the root node. Although TAN can achieve a global one-dependence optimization, MST cannot be extended to arbitrary $k$-dependence structure when $k>1$.

The KDB [20] is a $k$-dependence classifier because it allows each attribute to have a maximum number of $k$ parents in addition to the class attribute. Starting with the highest, an attribute order is pre-determined by comparing the mutual information $I\left(X_{i} ; C\right)$. By comparing

![img-2.jpeg](img-2.jpeg)

Fig 3. An example of directed MSTs with different root nodes, which are filled in black. Attributes $\left(X_{2}, X_{17}, X_{19}, X_{21}, X_{23}, X_{25}\right)$ correspond to clinical variables on thyroxine, TSH, T3, TT4, T4U and FTI, respectively.
https://doi.org/10.1371/journal.pone.0182070.g003
conditional mutual information $I\left(X_{i} ; X_{j} \mid C\right)$, each attribute can select a maximum number of $k$ parents among the attributes ahead of itself in the pre-determined order.

For a KDB model, the class assignments of the test samples are based on Eq (4).

$$
P\left(X \mid C_{i}\right)=\prod_{k=1}^{n} P\left(X_{k} \mid C_{i}, X_{i 1}, \cdots, X_{i p}\right) \arg \max _{c_{i}} P\left(c_{i}\right) P\left(x \mid c_{i}\right)=\arg \max _{c_{i}} P\left(c_{i}\right) \prod_{j=1}^{p} P\left(x_{j} \mid c_{i}, x_{j 1}, \cdots, x_{i p}\right)
$$

where $\left\{X_{j 1}, \cdots, X_{j p}\right\}$ are the parent attributes of $X_{j}$ and $p=\min (j-1, k)$.

# KCF algorithm 

MST contains the most significant relationships among attributes. Thus at training time, we aim to achieve high-dependence directed trees by extending one-dependence directed trees that are inferred from MST. Each one-dependence directed tree is extended to the $k$-dependence conditional tree along the attribute dependence spectrum. Finally, we will obtain a series of $k$-dependence trees rather than one augmented tree. Leaf node $X_{i}$ can be used to select other nodes as parents along the path from $X_{i}$ to the root node by comparing the conditional mutual information. For example, as shown in Fig 3(a), $X_{2}, X_{23}, X_{25}$ are the possible parents of $X_{17}$, and $X_{2}, X_{23}$ are the possible parents of $X_{25}$. Different root nodes correspond to different spanning trees or Bayesian classifiers, the ensemble of which finally forms a forest. When $k>1$, e.g., $k=2$, more parents can be selected for each non-root node by comparing the conditional mutual information. Fig 4 shows the $k$-dependence Bayesian classifiers when $k=2$. The newly added arcs are annotated with red color.

At the testing time, KCF estimates the class membership probabilities by using each subclassifier, and the final result is the average of the outputs of all subclassifiers. The training procedure (KCF-Training) and testing procedure (KCF-Testing) are depicted below.

![img-3.jpeg](img-3.jpeg)

Fig 4. The KCF ( $k=2$ ) model corresponding to the MSTs shown in Fig 3. Attributes $\left\{X_{2}, X_{17}, X_{19}, X_{21}, X_{23}, X_{25}, C\right\}$ correspond to clinical variables on thyroid, TSH, T3, TT4, T4U, FTI and Class, respectively.
https://doi.org/10.1371/journal.pone.0182070.g004

# Algorithm 1 KCF-Training 

Input: Pre-classifiedinstance set DB with $n$ predictive attributes $\left\{X_{1}, \cdots, X_{n}\right\}$.
Output: Subclassifiers $\left\{\mathrm{KCF}_{1}, \cdots, \mathrm{KCF}_{n}\right\}$.
1: Compute conditional mutual information $I\left(X_{i} ; X_{j} \mid C\right)$ for each pair of attributes $X_{i}$ and $X_{j}$, where $i \neq j$.
2: Build undirectedMST by comparing conditional mutual information.
3: For each attribute $X_{i}(i=1,2, \ldots, n)$
(a) Transform the MST to be a directed one by choosing $X_{i}$ as the root and setting the direction of all arcs to be outward from it.
(b) Let the Bayesian subclassifier being constructed, $\mathrm{KCF}_{i}$, begin with the directedMST.
(c) Add a node to $\mathrm{KCF}_{i}$ representing class variable $C$.
(d) Add an arc from $C$ to each node in $\mathrm{KCF}_{i}$.
(e) For each node $X_{j}(j \neq i)$, add $m-1(m=\min (d, k)$, dis the number of nodes along the branch from root to $X_{j}$ ) arcs from $m-1$ distinct attributes $X_{i}$ to $X_{j}$. $X_{i}$ should locate in the branch from root to $X_{j}$ and correspond to the first $m-1$ highest value for $I\left(X_{i} ; X_{j} \mid C\right)$.
4: Compute the conditional probability tables inferred by the structure of $\mathrm{KCF}_{i}$ by using counts from $D B$, and output $\mathrm{KCF}_{i}$.

# Algorithm 2 KCF-Testing 

Input: $\mathrm{KCF}_{1}, \mathrm{KCF}_{2}, \ldots, \mathrm{KCF}_{n}$ and a testing instance $e$.
Output: The conditional probabilities $\hat{P}(c \mid e)(p=1,2, \ldots, t)$, where $c$ is the class label.

1: For each $\mathrm{KCF}_{i(i=1,2, \ldots, n)}$, estimate the conditional probability $\hat{P}_{i}(c \mid e)$ that e belongs to class $c$.
2: Average all of the probabilities $\hat{P}(c \mid e)=\frac{1}{2} \sum_{i=1}^{n} \hat{P}_{i}(c \mid e)$.
3: Return the estimated $\hat{P}\left(c_{1} \mid e\right), \hat{P}\left(c_{2} \mid e\right), \ldots, \hat{P}\left(c_{i} \mid e\right)$.
$k$ is related to the classification performance of a high-dependence classifier. An appropriate value of $k$ cannot be effectively preselected to achieve the optimal trade-off between the model complexity and classification performance [21]. For each $\mathrm{KCF}_{i}$, the space complexity increases exponentially as the value of $k$ increases to achieve a trade-off between the classification performance and efficiency. We set $k=2$ in the following experiments.

## Results

The detailed introduction of the 29 attributes from thyroid disease dataset in UCI database is shown in Table 1. And numeric attributes in thyroid disease dataset are discretized by using 10 -bin equal frequency discretization. In order to minimize the bias associated with the random sampling of the training and holdout data samples in comparing the classification accuracy of two or more methods, 10 -fold cross-validation is applied to compare the general performance of KCF with three Bayesian network classifiers (i.e., NB, TAN and KDB) and five non-Bayesian network classifiers, i.e., IBK( $k$-Nearest Neighbours) [22], SMO(Support Vector Machine) [23], MultilayerPerception(Artificial Neural Network) [24], DecisionStump(Decision Tree) [25] and SimpleLogistic(linear logistic regression) [26]. In 10-fold cross-validation, whole data are randomly divided to 10 mutually exclusive and approximately equal size subsets. The classification algorithm trained and tested 10 times. In each case, one of the folds is taken as test data and the remaining folds are added to form training data. Thus 10 different test results exist for each training-test configuration. The average of these results gives the test accuracy of the algorithm. All the experiments have been carried out in a C++ software specially designed to deal with out-of-core classification methods. The average classification accuracy (inversely related to zero-one loss [27]) are $75.17 \%(\mathrm{NB}), 80.65 \%(\mathrm{TAN}), 80.43 \%(\mathrm{KDB})$, $81.89 \%(\mathrm{KCF}), 78.15 \%(\mathrm{IBK}), 79.67 \%(\mathrm{SMO}), 77.34 \%$ (MultilayerPerception), $73.81 \%$ (DecisionStump) and $79.53 \%$ (SimpleLogistic). Obviously, the proposed KCF algorithm achieves the highest classification accuracy compared with other algorithms and thus performs much more effectively in thyroid disease diagnosis.

To explain the main reason of performance difference of BNCs, we will clarify from the viewpoint of Markov blanket. Compared with low-dependence BNC, high-dependence BNC can demonstrate more conditional dependencies. Thus in the following discussion, we just compare KCF with KDB, both of which are 2-dependence BNCs. KCF will generate a series of submodels, each of which corresponds to different focus for analysis. For example, if $X_{i}$ is the key factor for diagnosis, then doctors can use the $i$ th submodel for further analysis. From the definition of Markov blanket, we can get the following conclusion that $X_{i}$ is directly and mutually dependent on attributes $\left\{P a\left(X_{i}\right), \operatorname{Ch}\left(X_{i}\right)\right\}$ while indirectly dependent on attributes $P C\left(X_{i}\right)$. The other attributes are useless for further consideration. The time cost for unnecessary analysis and expenditure on unnecessary physical examination will be decreased greatly. With limited time and space complexity, more Markov blanket attributes means more possible dependency relationships to be mined. The list and number of Markov blanket attributes of

Table 1. Attributes available for analysis.


https://doi.org/10.1371/journal.pone.0182070.t001
each attribute for KCF and KDB are shown in Fig 5 and Fig 6, respectively. From Fig 6, for 25 of all of the 29 attributes the number of corresponding Markov blanket attributes for KCF is greater than that for KDB. On average each predictive attribute has 9.1 Markov blanket attributes for KCF, whereas only 4.1 Markov blanket attributes for KDB.

Conditional mutual information $I\left(X_{i} ; X_{j} \mid C\right)$ can be used to quantitatively evaluate the conditional dependence between $X_{i}$ and $X_{j}$ given $C$. For any given target attribute $X_{k}, X_{k}$ is directly dependent on $P a\left(X_{k}\right)$ and $C h\left(X_{k}\right)$ is directly dependent on $X_{k}$. Thus the conditional dependencies are measured by $I\left(X_{i} ; X_{k} \mid C\right)$ and $I\left(X_{j} ; X_{k} \mid C\right)\left(X_{i} \in P a\left(X_{k}\right), X_{j} \in C h\left(X_{k}\right)\right)$, respectively. $P C$ $\left(X_{k}\right)$ is conditionally dependent on $X_{k}$ but directly dependent on $C h\left(X_{k}\right)$. The conditional dependence is measured by $I\left(X_{i}^{\prime} ; X_{j}^{\prime} \mid C\right)\left(X_{i}^{\prime} \in P C\left(X_{k}\right), X_{j}^{\prime} \in C h\left(X_{k}\right)\right)$. All the conditional dependencies among attributes in $M B\left(X_{k}\right)$ can then be measured by $M B \_$Info $\left(X_{k}\right)$, which is

![img-4.jpeg](img-4.jpeg)



Fig 5. The Markov blanket for KDB ( $k=2$ ) model is in yellow background and that for KCF ( $k=2$ ) model is in blue background. https://doi.org/10.1371/journal.pone.0182070.g005

![img-5.jpeg](img-5.jpeg)

Fig 6. The number of attributes contained in the Markov blanket of each attribute in the KDB ( $k=2$ ) model and KCF $(k=2)$ model.
https://doi.org/10.1371/journal.pone.0182070.g006
defined by Eq (5),

$$
\begin{aligned}
M B \_ \text {Info }\left(X_{k}\right)= & \sum_{X_{i} \in \operatorname{Re}\left(X_{k}\right)} I\left(X_{i} ; X_{k} \mid C\right)+\sum_{X_{j} \in \operatorname{Ch}\left(X_{k}\right)} I\left(X_{j} ; X_{k} \mid C\right) \\
& +\sum_{X_{j}^{\prime} \in \operatorname{PC}\left(X_{k}\right)} \sum_{X_{j}^{\prime} \in \operatorname{Ch}\left(X_{k}\right)} I\left(X_{i}^{\prime} ; X_{j}^{\prime} \mid C\right)
\end{aligned}
$$

We also compare the average weight of conditional dependencies implicated in $M B\left(X_{k}\right)$, which is defined by Eq (6),

$$
\text { Avg_MB_Info }\left(X_{k}\right)=\frac{M B \_ \text {Info }\left(X_{k}\right)}{\text { number of attributes in } M B\left(X_{k}\right)}
$$

The comparison results of $M B \_$Info $\left(X_{k}\right)$ between KCF and KDB are shown in Fig 7. For the first 14 attributes, $M B \_$Info $\left(X_{k}\right) \approx 0\{0 \leq k \leq 13\}$ for both KDB and KCF. Thus $X_{k}\{0 \leq k \leq 13\}$ is directly dependent on class variable whereas independent of any other attributes. For 13 of the other 15 attributes, the value of $M B \_$Info $\left(X_{k}\right)\{14 \leq k \leq 28\}$ for KCF is greater than that for KDB. The experimental results prove that KCF can fully demonstrate dependency relationships and thus help to increase the classification accuracy.

# Discussion 

Thyroid cancer incidence has been rising since 1978, and its prevalence has increased dramatically over the past decade; currently, thyroid cancer is the fifth most common cancer diagnosed among women. By contrast, the incidence of other malignancies, including lung, colorectal, and breast cancer, decreases [28]. A statistical survey in 2014 showed that 10 million Chinese patients have hyperthyroidism, 90 million have hypothyroidism, more than 100

![img-6.jpeg](img-6.jpeg)

Fig 7. The sum of conditional mutual information between each attribute and the attributes contained in its Markov blanket is shown in (a). The average of conditional mutual information between each attribute and the attributes contained in its Markov blanket is shown in (b).

https://doi.org/10.1371/journal.pone.0182070.g007

million are afflicted with thyroid nodules or thyroid cancer, and conservatively; more than 200 million are estimated to have thyroid disease. As the second major disease of the endocrine system, the awareness rate and treatment rate of thyroid diseases are very low in China.

Thyroid nodule is a common clinical problem, and the prevalence of differentiated thyroid cancer increases [29]. Early detection, diagnosis, and treatment are important in curbing the development of thyroid diseases and reducing the mortality rate. Predicting the outcome of diseases and dependency among clinical variables or attributes plays pivotal roles in medical diagnosis and treatment.

For the detailed analysis, this paper calculates and compares the mutual information *I*(*X*<sub>*i*</sub>; *C*) first. The results are sorted starting from the highest. The attribute order is *X*<sub>17</sub>, *X*<sub>25</sub>, *X*<sub>21</sub>, *X*<sub>19</sub>, *X*<sub>23</sub>, *X*<sub>2</sub>, *X*<sub>28</sub>, *X*<sub>27</sub>, *X*<sub>16</sub>, *X*<sub>20</sub>, *X*<sub>26</sub>, *X*<sub>18</sub>, *X*<sub>22</sub>, *X*<sub>24</sub>, *X*<sub>0</sub>, *X*<sub>1</sub>, *X*<sub>6</sub>, *X*<sub>10</sub>, *X*<sub>13</sub>, *X*<sub>7</sub>, *X*<sub>9</sub>, *X*<sub>15</sub>, *X*<sub>4</sub>, *X*<sub>8</sub>, *X*<sub>5</sub>, *X*<sub>3</sub>, *X*<sub>12</sub>, *X*<sub>11</sub>, *X*<sub>14</sub>. From the perspective of medical diagnosis, the attribute with the most intimate relationship with the outcome can be considered as the key attribute and should be the focus of the analysis. The attribute *X*<sub>17</sub> represents the clinical index for thyroid stimulating hormone (TSH) and should be analyzed initially. TSH can promote the growth of thyroid secreted by adenohypophysis. In addition, TSH can completely improve the function of the thyroid, promoting early release of thyroid hormones and synthesis of T4 and T3.

To clarify the role of the TSH attribute, this paper displays the structure of the KDB and a KCF submodel in Fig 8(a) and 8(b), respectively. To make typical and fair comparison, we set *X*<sub>17</sub> as the common root node of both models. As shown in Fig 8(a), *X*<sub>17</sub> is the common parent of *X*<sub>25</sub>, *X*<sub>21</sub>, *X*<sub>28</sub>, *X*<sub>16</sub>, *X*<sub>18</sub>, *X*<sub>17</sub>, *X*<sub>3</sub>, and *X*<sub>12</sub>; *X*<sub>0</sub> and *X*<sub>19</sub> are the parent nodes of the children of

![img-7.jpeg](img-7.jpeg)
(a)
![img-8.jpeg](img-8.jpeg)
(b)

Fig 8. KDB ( $k=2$ ) model and a submodel of the KCF $(k=2)$ on thyroid disease date set shown respectively in (a) and (b). Attributes $\left(X_{0}, X_{1}, \cdots, X_{28}, C\right)$ correspond to clinical variables age, sex, on thyroxine, query on thyroxine, on antithyroid medication, sick, pregnant, thyroid surgery, I131 treatment, query hypothyroid, query hyperthyroid, lithium, goitre, tumor, hypopituitary, psych, TSH measured, TSH, T3 measured, T3, TT4 measured, TT4, T4U measured, T4U, FTI measured, FTI, TBG measured, TBG, referral source and Class respectively.
https://doi.org/10.1371/journal.pone.0182070.g008

$X_{17} . X_{0}$ is the parent node of $X_{12}$, and $X_{19}$ is the common parent of $X_{18}$ and $X_{28} . M B\left(X_{17}\right)$ contains 10 attributes. $M B \_$Info $\left(X_{17}\right)$ is 0.902 and $A v g \_M B \_$Info $\left(X_{17}\right)=0.09$. In the corresponding KCF model shown in Fig 8(b), $X_{17}$ is the common parent of $X_{23}, X_{24}, X_{25}, X_{27}$, and $X_{28}$, whereas $X_{17}$ has no parent nodes and no parent of children nodes. Thus, $M B\left(X_{17}\right)$ only contains 5 attributes. $M B \_$Info $\left(X_{17}\right)$ and $A v g \_M B \_$Info $\left(X_{17}\right)$ turn to be 0.597 and 0.12 , respectively. Similarly, the sum of $M B \_$Info $\left(X_{i}\right)$, i.e., $\sum_{i=0}^{29} M B \_$Info $\left(X_{i}\right)$, is 14.458 for KCF, whereas it is only 6.964 for KDB. The sum of $A v g \_M B \_$Info $\left(X_{i}\right)$, i.e., $\sum_{i=0}^{29} A v g . M B \_$Info $\left(X_{i}\right)$, is 1.576 for KDB and 1.946 for KCF. Hence, the proposed KCF model describes significant relationships among attributes.

MST contains the most significant dependency relationships, whereas the KDB model can only contain portions of the MST. Additionally, the KCF algorithm can generate a series of submodels rather than one model alone. Thus, for medical diagnosis, any clinical variable or attribute related to thyroid diseases can be regarded as the original cause, and an in-depth research can be conducted on the disease. Hence, the proposed KCF model can handle various patient conditions and is more suitable for providing appropriate treatment compared with a model with a rigid root node generated by other algorithms.

Sensitivity and specificity are statistical measures of the performance of a binary classification test, also known in statistics as classification function. In the context of medical tests sensitivity is the extent to which true positives are not missed/overlooked and specificity is the extent to which positives really represent the condition of interest and not some other condition being mistaken for it. So we select 12 datasets with binary class labels from UCI for comparison of classification accuracy. Table 2 summarizes the characteristics of each dataset, including the numbers of instances, attributes and classes. Averaged One-dependence Estimators (AODE) [30], which utilizes a restricted class of one-dependence estimators and aggregates the predictions of all qualified estimators within this class, is introduced to compare the bagging performance of KCF.

Experimental results of average classification accuracy for different BNCs are shown in Table 3. Friedman test [31], which is a non-parametric measure to compare the ranks of the algorithms for each dataset separately. The ranks of algorithms for each dataset are calculated separately (average ranks are assigned if tied values exist). The null-hypothesis is that all the algorithms performs almost equivalently and there is no significant difference in terms of

Table 2. Datasets.


the datasets denoted with symbol "*" will be used for comparing sensitivity and specificity. https://doi.org/10.1371/journal.pone.0182070.t002

Table 3. Experimental results of average classification accuracy for datasets with binary class labels.


https://doi.org/10.1371/journal.pone.0182070.t003
ranks. The Friedman statistic can be computed as Eq (7) shows,

$$
F_{r}=\frac{12}{N t(t+1)} \sum_{i=1}^{t} R_{j}^{2}-3 N(t+1)
$$

where $R_{j}=\sum_{i} r_{i}^{j}$ and $r_{i}^{j}$ is the rank of the $j$-th of $t$ algorithms on the $i$-th of $N$ datasets. Thus, for any pre-determined level of significance $\alpha$ the null hypothesis will be rejected if $F_{r}>\chi_{a}^{2}$, which is the upper-tail critical value having $t \sim 1$ degrees of freedom. The critical value of $\chi_{a}^{2}$ for $\alpha=$ 0.02 is 11.668 . With 5 algorithms and 12 datasets, the friedman statistic $F_{r}=18.55$ and $P<0.001$. Hence the null-hypotheses is rejected again. The average ranks of different classifiers are $\{\mathrm{NB}(1.54), \mathrm{TAN}(3.00), \mathrm{AODE}(2.54), \mathrm{KDB}(3.88), \mathrm{KCF}(4.04)\}$. Thus KCF with the highest rank is the most effective BNC from the perspectives of classification accuracy.

When dealing with imbalanced class distribution, traditional classifiers are easily overwhelmed by instances from majority classes while the instances from minority classes are usually ignored. An useful performance measure is the balanced accuracy (BAC) [32] which avoids inflated performance estimates and defined as Eq (8) shows. It is defined as the arithmetic mean of sensitivity and specificity, which are calculated by knowing the $m$ binary outputs of the classifiers (indicating membership to given classes). Overall performance is calculated by conducting a leave-one-out test for all training samples.

$$
B A C=\frac{\text { sensitivity }+ \text { specificity }}{2}
$$

The experimental results of sensitivity, specificity and BAC for BNCs are shown in Table 4. By comparing via two-tailed binomial sign test with a $95 \%$ confidence level, Table 5 shows corresponding win/draw/loss (W/D/L) records summarizing the relative BAC of the different BNCs. The W/D/L record in cell $[i, j]$ of each table contains the number of datasets in which BNC on row $i$ has lower, equal or higher outcome relative to the BNC on column $j$. We could see from Table 5 that the bagging mechanism helps AODE increase BAC significantly often relative to TAN and NB. KDB can achieve not only higher classification accuracy but also higher BAC than TAN. KCF utilizes the bagging mechanism of AODE and can represent

Table 4. Experimental results of sensitivity, specificity and BAC for medical datasets with binary class labels.


https://doi.org/10.1371/journal.pone.0182070.t004

Table 5. Win-draw-loss records for different BNCs in terms of BAC.


https://doi.org/10.1371/journal.pone.0182070.t005 high-dependence relationships. This may be the main reason why KCF achieves higher BAC more often than the other four BNCs.

## Conclusion

Bayesian network can graphically describe the conditional dependencies implicit in training data and Bayesian network classifiers have been previously demonstrated to perform efficiently in medical diagnosis and treatment. One single data mining model cannot deal with all difficult and complicated cases. KCF, which uses the same learning strategy as that of KDB, simultaneously provides $n$ submodels rather than one. This improvement helps KCF to describe more significant conditional dependencies. The experimental study on UCI datasets shows that KCF enjoys obvious advantage in classification over other BNCs.

## Acknowledgments

This work was supported by the National Science Foundation of China (Grant No. 61272209) and the Agreement of Science \& Technology Development Project, Jilin Province (No. 20150101014JC).

## Author Contributions

Conceptualization: LiMin Wang, FangYuan Cao. Data curation: FangYuan Cao.

Formal analysis: LiMin Wang, MingHui Sun.
Funding acquisition: LiMin Wang.
Investigation: LiMin Wang, ShuangCheng Wang.
Methodology: LiMin Wang.
Project administration: LiMin Wang.
Resources: LiYan Dong.
Software: LiMin Wang.
Supervision: LiMin Wang.
Validation: ShuangCheng Wang.
Visualization: FangYuan Cao.
Writing - original draft: LiMin Wang, FangYuan Cao.
Writing - review \& editing: LiMin Wang, FangYuan Cao.
