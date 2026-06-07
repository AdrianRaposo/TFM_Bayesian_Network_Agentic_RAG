# Privacy-Preserving Incremental Bayesian Network Learning 

Saeed Samet<br>CHEO Research Institute<br>Ottawa, Ontario, Canada<br>ssamet@ehealthinformation.ca<br>Ali Miri<br>Ryerson University<br>Toronto, Ontario, Canada<br>Ali.Miri@ryerson.ca<br>Eric Granger<br>Laboratoire d'imagerie, de vision et d'intelligence artificielle (LIVIA)<br>École de technologie supérieure, Montreal, Canada<br>Eric.Granger@etsmtl.ca


#### Abstract

Bayesian Networks (BNs) have received significant attention in various academic and industrial applications, such as modeling knowledge in image processing, engineering, medicine and bio-informatics. Preserving the privacy of sensitive data, owned by different parties, is often a critical issue. However, in many practical applications, BNs must train from data that gradually becomes available at different period of times, on which the traditional batch learning algorithms are not suitable or applicable. In this paper, an algorithm based on a new and efficient version of Sufficient Statistics is proposed for incremental learning with BNs. The standard $\mathcal{K} 2$ algorithm is also modified to be utilized inside the incremental learning algorithm. Next, some secure building blocks such as secure multi-party multiplication, comparison, and factorial, which are resistant against colluding attacks and could be applied securely over public channels like internet, are presented to be used inside the main protocol. Then a privacy-preserving protocol is proposed for incremental learning of BNs, in which the structure and probabilities are estimated incrementally from homogeneously distributed and gradually available data among two or multi-parties. Finally, security and complexity analyses along with the experimental results are presented to compare with the batch algorithm and to show its performance

and applicability in real world applications. ${ }^{1}$
Keywords: Security and Privacy Preserving, Bayesian Networks, Incremental Learning, Data Mining and Machine Learning

# 1. Introduction 

Bayesian Networks are probabilistic graphical models [8] that are trained to represent the relationship between variables from a dataset [6]. Medical diagnosis applications, fraud detection systems, and financial networks widely utilize such networks to create models and make decision according to the probabilistic independencies among the variables of the underlying databases [7]. For instance, Fenton and Neil in [11] show the successful application of Bayesian Networks in risk management.

According to the privacy regulations such as Freedom of Information and Protection of Privacy Act (FIPPA) [34] in Canada, or the Health Insurance Portability and Accountability Act (HIPAA) [35] in the United States, individual's private and sensitive data must be secured when protocols are applied on data used to train BNs. To create the BNs structure and parameters using training data which is securely shared among two or more parties, they cannot simply present their own private data to each other, or even to a third party to run a learning algorithm on the whole data. Therefore, privacy-preserving protocols are needed to apply in these situations.

In many practical applications, BNs must be trained using data that becomes available at different points in time. The traditional techniques for training BNs (e.g. $\mathcal{K} 2$ algorithm) are batch in nature, and are not suitable for training on data that arrives incrementally. To obtain a high level of performance, using a batch technique would involve accumulating all training data in memory, and recreating a new BN from scratch using all cumulative data. The time and memory complexity of retraining on all data would be prohibitive in applications with large amounts of training data. For instance, selling records in Walmart, as a chain of large stores, are gradually grow everyday and is not reasonable to store all data and run the data mining and machine learning algorithms on all data every time a block of new data becomes available. This is an ubiquitous scenario in many different fields such as healthcare systems, government applications and so on. Therefore, incremental learning is needed to efficiently update BNs on new data, in terms of data storage and processing time.

In this paper, BNs structure is incrementally constructed each time a block of new training data is available by updating the sufficient statistics of the existing network structure, and a new structure is created accordingly. Note that by updating sufficient statistics, the probability table of each node could also be computed. After reviewing the existing techniques for incremental learning

[^0]
[^0]:    ${ }^{1}$ Some of the material in this paper has been presented at the 2009 IEEE International Conference on Privacy, Security, riSk and Trust (PASSAT-09).

![img-0.jpeg](img-0.jpeg)

Figure 1: Overview of the Proposed Privacy-Preserving Incremental Bayesian Network Learning.
of BNs, first an improved version of sufficient statistics, in terms of required storage and search time, is proposed followed by a specialized $\mathcal{K} 2$ algorithm to be applied in our incremental learning algorithm for BNs. After presenting that algorithm, a privacy-preserving protocol and required secure building blocks, such as secure multi-party multiplication, comparison, and factorial, are proposed along with their security and complexity analyses and experimental results. Figure 1 illustrates the contribution of the paper and the relations of its components. Inside the main protocol of privacy-preserving incremental BNs, the new incremental learning algorithm is used to update the BNs structure by using an improved version of sufficient statistics and calling the specialized $\mathcal{K} 2$ algorithm. Also secure building blocks are utilized inside the protocol to maintain the privacy of the parties involved. These building blocks, which are indicated as a bold box in Figure 1, are previously proposed by the same authors in $[10]$.

As a summary, each time a block of new data becomes available, Incremental BNs algorithm is called with the ordered list of nodes, sufficient statistics of the previous data, the set of previous candidate lists of parents, and the new data. Its output is a directed acyclic graph for the BNs and the new updated sufficient statistics. Inside this algorithm, the specialized $\mathcal{K} 2$ algorithm is called when needed with the current node, its parents set, sufficient statistics of that node, its predecessors, and the set of candidate parents lists as the inputs. The output of this algorithm will be the new parents set of the node and its updated candidate parents lists. Each time we need to compute the score function in those two algorithms, secure building blocks are used to securely compute this function without revealing private data of each party to the others.

With this privacy-preserving protocol, it is assumed that data is homoge-

nously shared and owned by several parties, while these parties want to keep their sensitive data private. The protocol is also secure against colluding attacks and could be run over public channels. We show the applicability and efficiency of the proposed protocol by testing it against several different datasets, various number of parties involved and reasonable encryption key sizes, 512, 1024 and 2048 bits, to keep the privacy of the protocol strong. Also, the comparison of the final results of the incremental learning with the batch algorithm, in terms of efficiency and accuracy, shows its great promise to be applied in real world applications.

The rest of the paper is organized as follows. In Section 2, the BN is briefly introduced, along with a brief survey of training algorithms and privacypreserving BNs. An improved version of sufficient statistics, an incremental algorithm for learning BN structure and a modified $\mathcal{K} 2$ [3] algorithm which could exploit that algorithm presented in Section 3. A privacy-preserving protocol for Incremental Bayesian Networks is presented in Section 4, followed by the experimental results in Section 5.

# 2. Techniques for Training BNs 

Bayesian Networks, or Belief Networks, are Directed Acyclic Graphs (DAG) encoding probabilistic relations or dependencies among a set of variables. Each node of a graph represents a variable, and an arc from one node to another node shows a conditional dependency between them. Thus, a BNs structure for a set of variables is formally shown by a pair $\left(N_{s}, N_{p}\right)$, in which $N_{s}=(V, E)$ is a DAG containing the set of nodes, $V$, and the set of edges, $E$. The set of probability distributions, $N_{p}$, which is called the parameters of the BNs, is defined as $N_{p}=\left\{p\left(x_{i} \mid \pi_{i}\right), x_{i} \in V\right\}$, where $\pi_{i}$ is the set of $x_{i}$ 's parents and $p\left(x_{i} \mid \pi_{i}\right)$ is the probability distribution of $x_{i}$ conditional upon its parents, $\pi_{i}$.

Constructing BNs is NP-hard [2]. There are different batch algorithms for this learning system. CL algorithm proposed by Chow and Liu [16] estimates the underlying n-dimensional discrete probability distribution from a dataset. To approximate the probability distribution, this algorithm generates the product of $n-1$ second order distributions.

Lam and Bachus [14], and Friedman and Goldszmith [24] use the Minimum Description Length (MDL) principle [23, 22] as their approach to propose their own learning algorithm for BNs. In MDL a database is modeled with the minimum length of encoding. Using this approach, BN is encoded as a model with the minimum bit length.

Bouckaert [25] presents a heuristic algorithm, called B, which uses a hillclimbing search method to generate BN structure, and variables do not need to be sorted at the beginning of the algorithm.

Castelo in [26], and Castelo and Cočka in [27] propose algorithm HCMC, which is similar to algorithm B, because of utilizing a hill-climbing search method on DAGs. However, unlike algorithm B it considers the inclusion order among BNs. In [28], two protocols are proposed for privacy-preserving

Naive Bayes, in both horizontally and vertically partitioned data using secure multi-party computation techniques such as secure sum [32] and secure dot product [33]. Meng et al. in [29] proposed a privacy-preserving estimation for the BN parameters, by assuming that the Bayesian network structure has been already created, and is publicly known to the parties involved. Also, in [30], authors proposed a secure technique to compute the BN parameters on vertically partitioned data using secure multi-party computation sub-protocols, based on their previously presented protocol in [31] which securely developed the BN structure.

K2 algorithm is proposed by Cooper and Herskovits [3]based on a hillclimbing heuristic search to find an optimized BN structure. The $\mathcal{K} 2$ algorithm starts with a graph of nodes showing the variables of interest, without any edges. Then, for each node, using a canonical order and a score function, edges by which the score of the graph increases are added as the parents of the current node. This process ends when no more parents can be added or the number of parents reaches a specified threshold, and the next node will be processed in order.

In this paper the $\mathcal{K} 2$ algorithm shown in Algorithm 1 is used as a base algorithm for the creation of BNs structure. In this algorithm, $\pi_{i}$ is the set of parents of a variable $x_{i}$. At each step, score value of the Predecessor nodes of the current node, $x_{i}$, is computed and the node, with the maximum score, say $z$, is selected and compared with the current score of $x_{i}$. If it is greater, $z$ will be added to the $x_{i}$ 's parents set, and otherwise while loop will end, and the program continues for the next variable. The score function $f\left(i, \pi_{i}\right)$ is defined

```
Algorithm 1 K2 Algorithm
1. Input: A dataset \(D\), a set of \(m\) nodes with an assumed order, and an upper
    bound \(u\) on the maximum number of parents of each node
2. Output: A directed acyclic graph for the Bayesian network
3. for \(i=1\) to \(m\) do
4. \(\pi_{i}=\emptyset\)
5. \(\operatorname{Score}_{o l d}=f\left(i, \pi_{i}\right)\)
6. OkToProceed \(=\) true
7. while OkToProceed and \(\left|\pi_{i}\right|<u\) do
8. \(z=\) the node in \(\operatorname{Pred}\left(x_{i}\right)-\pi_{i}\) that maximize \(f\left(i, \pi_{i} \bigcup\{z\}\right)\)
9. \(\quad \operatorname{Score}_{\text {new }}=f\left(i, \pi_{i} \bigcup\{z\}\right)\)
10. if \(\operatorname{Score}_{\text {new }}>\operatorname{Score}_{\text {old }}\) then
11. \(\quad \operatorname{Score}_{\text {old }}=\operatorname{Score}_{\text {new }}\)
12. \(\pi_{i}=\pi_{i} \bigcup\{z\}\)
13. else
14. OkToProceed \(=\) false
15. end if
16. end while
17. end for
```

as follows:

$$
f\left(i, \pi_{i}\right)=\prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} \alpha_{i j k}!
$$

where $q_{i}$ is the number of items in the list of all possible instantiation of $\pi_{i}$ in $D$, and $r_{i}$ is the number of possible values of $x_{i}$, which is two for binary attributes. In $1, \alpha_{i j k}$ is the number of records in $D$ in which $x_{i}$ has its $k$ th value and its parents are instantiated with the $j$ th instantiation in the set of Cartesian product of all possible values of $\pi_{i}$, and $N_{i j}=\sum_{k=1}^{r_{i}} \alpha_{i j k}$.

# 2.1. Incremental learning techniques for BNs 

When new data becomes available, the $\mathcal{K} 2$ Algorithm used to train BNs is not efficient since it must be applied on whole dataset, old and new data. Therefore, online and incremental algorithms have been introduced for applications in which new training data arrives at different point in time. The main ideas behind all these incremental learning algorithms are very similar. Storing a set of candidate parents is almost the same as storing a frontier list of candidate networks.

Friedman and Goldszmith in [12] introduce the concept of Sufficient Statistics for the BNs structure, to extract its probability distribution parameters. This concept is defined as follows: suppose $\mathbf{X}$ denotes a vector of variables, and $N_{\mathbf{X}}^{D}(\mathbf{x})$ be the number of records in the dataset $D$ such that $\mathbf{X}=\mathbf{x}$. The vector $N_{\mathbf{X}}^{D}(\mathbf{x})$ containing $N_{\mathbf{X}}^{D}$ for all possible values of $\mathbf{X}$, is called the sufficient statistics of $\mathbf{X}$.

Now, by using this concept and decomposability property of the score assigned to a BN structure of a dataset $D$, we only need to keep the sufficient statistics of each node $X_{i}$ and its possible parent sets $\operatorname{Pa}\left(X_{i}\right), N_{X_{i}, P a\left(X_{i}\right)}^{D}$, to learn the parameters and also to compute the score function of each node and its parents, to create the BN structure. Cardinality of sufficient statistics, $|S S(G)|$, have been discussed in some research papers such as [18]. If we denote $M$ as the maximum number of parents a node can have, $r$ as the number of nodes, and $A$ as the average number of possible values a node takes, then for a BN structure $G$ :

$$
$$

Friedman and Goldszmidt [12] propose an approach for incremental learning, in which they rely on a frontier set of networks, consisting of all the networks compared in each iteration of the algorithm. The procedure, by maintaining a set of sufficient statistics (explaining in detail in the next section) records, selects the structure with the best score among the frontier set of networks. The frontier set is updated every time algorithm updates the Bayesian network structure.

In [13] a generalized approach of $\mathcal{K} 2$ algorithm is first proposed, and then some guidelines are presented to convert that algorithm into an incremental approach. For each node, a set of parents is maintained and is classified as alive, asleep, and dead using three different thresholds. Parents sets are stored in a lattice structure. Two situations are considered for running incremental algorithm. In the first case, there is a short amount of time for updating the BNs and therefore a rapid update is applied in which the posterior probabilities are only updated and parents set are not touched. In the second situation, both structure and parameters are updated according to new data.

Lam and Bachus in[14] extend their own batch algorithm based on Minimum Description Length (MDL) approach to incrementally adapt BNs structures when new data is available. The MDL principle is based on the idea that if the encoding length of a model and its underlying data is minimum then it is the best model of that database. There is an implicit assumption in their approach that the new structure is very similar to the current one. In each iteration of the algorithm, description length of the whole structure is improved by minimizing the description length of the subgraph whose topology is changed by the new data. Thus, a partial structure is learned from the current structure using MDL, and the new data which includes records containing a subset of the nodes of the BNs.

Roure, in [15], presents incremental approaches for some BNs, such as Chow and Liu (CL) [16], $\mathcal{K} 2$, and Buntine (B) [25]. Here we only consider the algorithm of $\mathcal{K} 2$. Instead of maintaining a set of parents for each node, a set of candidate parents lists is kept, such that in the $k$-th list some nodes are ordered as the candidates for the $k$-th parent of that node in decreasing order, and the first item in the list is the current $k$-th parent of the node. The number of candidates in each list is a parameter of the algorithm as well as the number of variables that compared with the current parent to make sure that the current parent is still the best candidate inside the list. During each iteration of the algorithm, when no revision is needed for the current parents, the algorithm checks for possible new parent for each node.

However, the algorithm proposed in [15] has some issues in terms of candidate parents set. For example, if the current $k$-th parent, say $x_{k}$ of a node can no longer be its parent because of the new data, its subsequent parents could not be tested because when the score of these nodes are computed, $x_{k}$ should be considered as the $k$-th parent which is not the case. Also, it only searches new parents for each node only if its current parents are correct. However, a node could have new parent(s) by considering new data even the currents parent would be still correct. Another issue is that each parent could be compared with other candidates by considering new parents set and not the current one.

# 3. A New Incremental $\mathcal{K} 2$ Algorithm 

In the computation of sufficient statistics, shown in Section 2, all the possible parent sets for all the nodes have been counted. However, by considering some properties of the Bayesian network structure it could be optimized. The first

property is that in some widely used algorithms such as $\mathcal{K} 2$, a total order is defined for the existing nodes, reducing the search space to create direct acyclic graph of the network structure.

The second property is that the values of $N_{X_{i}, P_{0}\left(X_{i}\right)}^{D}$ for the nodes which cannot have the maximum number of parents could be computed from the corresponding information of their subsequent nodes. For instance, suppose the number of parties is 5 and the number of maximum parents is 3 . Then, vector values of the nodes $X_{1}, X_{2}$, and $X_{3}$ could be computed from those of $X_{4}$ or $X_{5}$. Thus, we do not need to keep those information in the final sufficient statistics.

By using those two properties the cardinality of the sufficient statistics of a BN structure $G$ would be reduced to:

$$
$$

To see the improvement, for example we consider $r=30$ and $M=10$. The new sufficient statistics has more than 10 times less items than the one with the previous formula. This significantly decreases the space needed to store and speed up the search of the sufficient statistics set for computing score and parameters of the Bayesian network structure.

Given the Sufficient Statistics of $G$, an incremental version of the $\mathcal{K} 2$ algorithm is proposed to construct BNs. Each time new trained data becomes available the sufficient statistics of the existing network structure is updated to create a new structure and adjust parameters accordingly. This algorithm, receives a node and its correct parent set, and will find other parents using new sufficient statistics and will also update the candidate lists of the parents. Each list $C_{i, l}, j+1 \leq l \leq k$, contains the current $l$-th parent of $X_{i}$, which is no longer the correct parent, along with all the candidate parents in decreasing order of their score. The number of nodes in each list could be varied using a threshold value.

Algorithm 2 shows the steps of this procedure. Inside the first loop from step 6 to 17 , each candidate list $C_{i, l}$ is checked to find the node with the maximum score to set it as the new $l$-th parent. Second loop, from step 19 to 29 , is almost the same as that in the previous $\mathcal{K} 2$ algorithm except that in each iteration if a parent is found, its corresponding candidate list is also created to use in the future run of the algorithms. The $\mathcal{K} 2$ algorithm must also be embedded in the incremental algorithm. In the main algorithm, Algorithm 3, for each node, using the previous structure and sufficient statistics, the new data, and previous set of candidate lists of the parents, new network structure and sufficient statistics are created. First, the sufficient statistics of the whole previous and new data are computed. Then, for each node, it is checked whether the current $j$-th parent is still parent of this node by checking and comparing its score with those of the other candidate nodes. If it can no longer be a parent, then it comes out from the inner loop and new $\mathcal{K} 2$ algorithm is called to find the new parents and to update the candidate lists of parents for the current node.

```
Algorithm 2 Specialized K2 Algorithm
    Inputs:
    \(X_{i}\)
    \(\pi_{i}=\left\{X_{i, 1}, \cdots, X_{i, j}\right\}\) (correct parents)
    \(S S\left(X_{i}\right)\)
    \(u\) (the maximum number of parents for a node),
    set of candidate parents lists, \(\left\{C_{i, j+1}, \cdots, C_{i, k}\right\}\) (to be checked to find the
    best parent in each list),
    \(\operatorname{Pred}\left(X_{i}\right)\) (to be checked for the new parents)
    Output:
    The new parents set for \(X_{i}\)
    The updated set of candidate parents lists for \(X_{i}\)
    \(S \operatorname{cor} e_{\text {old }}=f\left(i, \pi_{i}\right)\)
    \(l=j+1\)
    NotFound \(=\) true
    while NotFound and \(l \leq k\) do
        \(z=\arg \max _{w \in C_{i, l}} f\left(i, \pi_{i} \bigcup\{w\}\right)\)
        Reorder \(C_{i, l}\) in decreasing order of the nodes' score such that \(z\) be the
        first item of the list.
        \(\operatorname{Score}_{\text {new }}=f\left(i, \pi_{i} \bigcup\{z\}\right)\)
        if \(\operatorname{Score}_{\text {new }}>\operatorname{Score}_{\text {old }}\) then
            \(\operatorname{Score}_{\text {old }}=\operatorname{Score}_{\text {new }}\)
            \(\pi_{i}=\pi_{i} \bigcup\{z\}\)
            \(l=l+1\)
        else
            NotFound \(=\) false
        end if
    end while
    18. OkToProceed \(=\) true
    19. while OkToProceed and \(\left|\pi_{i}\right|<u\) do
        \(z=\arg \max _{w \in \operatorname{Pred}\left(x_{i}\right)-\pi_{i}} f\left(i, \pi_{i} \bigcup\{w\}\right)\)
        \(\operatorname{Score}_{\text {new }}=f\left(i, \pi_{i} \bigcup\{z\}\right)\)
        if \(\operatorname{Score}_{\text {new }}>\operatorname{Score}_{\text {old }}\) then
            Create a new list \(C_{i, l}\) containing the list of all candidate nodes for the
            \(l\)-th parent in decreasing order such that z be the first item in the list.
            \(\operatorname{Score}_{\text {old }}=\operatorname{Score}_{\text {new }}\)
            \(\pi_{i}=\pi_{i} \bigcup\{z\}\)
        else
            OkToProceed \(=\) false
        end if
    end while
```

```
Algorithm 3 Incremental Bayesian Network Learning Algorithm
    Input:
    {X,\cdots,Xm} (An ordered list of nodes),
    SS(D) (sufficient statistics of the previous data),
    D' (new dataset),
    u (the maximum number of parents for a node),
    {C,1,\cdots,C,kk} (set of previous candidate lists of parents)
    Output:
    A directed acyclic graph for the Bayesian network according to the previous
    one and new data,
    The new updated sufficient statistics, SS(D)
    Compute SS(D')
    SS(D)=SS(D)\bigcup SS(D')
    for i=1 to m do
        re}
        j=1
        OkToProceed = true
        while OkToProceed and j < k do
            z = the first node in C
            if z = arg maxw∈C, j f(X, re
                j}=j+1
            else
                OkToProceed = false
            end if
        end while
        if j<u then
            Call K2(X, re, SS(X,), u,
                {C, j+1,\cdots,C,kk}, Pred(X,))
            end if
    end for
```

# 4. Privacy-preserving Incremental Learning of Bayesian Networks 

In this section, we present our protocol for privacy-preserving incremental learning of BNs when data is horizontally partitioned among several parties. By privacy-preserving BNs, we mean a protocol by which BNs structure and/or parameters are constructed from a securely shared data among two or more parties while each party keeps her own data private. It is assumed, in this protocol, that the parties are semi-honest, i.e. each party follows the protocol and sends correct data to the other parties, however she might use intermediate or final information to compute others' private data.

The private information is the raw data each party owns and sufficient statistics of those data, and the public knowledge at the end of the protocol are the candidate parents lists of each node. In the above algorithms we need to securely compute the score function, securely compare computed scores to find the parents of each node, and construct the candidate lists of parents in decreasing order of their score values.

Some secure building blocks [10] are used inside the main protocol. Secure Multi-party Multiplication, Addition and Factorial, and also Secure Product Comparison are needed in both types of partitioned data. Thus we first discuss the sub-protocols used inside the main protocol and then bring the protocol for homogenously partitioned data.

### 4.1. Secure Multi-party Multiplication

In this building block, the product of private input shares, $x_{i} \mathrm{~s}$, is converted to the summation of private output shares, $y_{i} \mathrm{~s}$ :

$$
\prod_{i=1}^{n} x_{i}=\sum_{i=1}^{n} y_{i}
$$

This sub-protocol is widely used in other protocols and also in our building blocks such as secure exponentiation and secure multi-party factorial. A protocol has been proposed for this purpose in [9], which uses additive homomorphic encryption [5]. However that protocol is not secure against collusion attack in the multi-party case. For instance, in the case of three parties, if the first and third parties collude, they can easily deduce the second party's private input. Here, we propose another protocol to prevent that type of attack. The algorithm for the two-party case is the same as that in [9] briefly described in Appendix A, and the multi-party case is presented here.

Suppose $E_{i}$ is an additive homomorphic encryption established by $p_{i}$, with public key $e_{i}$ and private key $d_{i}$. The following are the steps of the algorithm:

1. $p_{1}$ and $p_{2}$ run a secure two-party multiplication for their inputs such that:

$$
x_{1} * x_{2}=y_{11}+y_{21}
$$

2. Therefore, we have:

$$
\begin{aligned}
x_{1} * x_{2} * \cdots * x_{n}= & \left(y_{11}+y_{21}\right) * x_{3} * \cdots * x_{n} \\
= & \left(y_{11} * x_{3} * \cdots * x_{n}\right)+ \\
& \left(y_{21} * x_{3} * \cdots * x_{n}\right)
\end{aligned}
$$

3. Now, each of

$$
\left(y_{11} * x_{3} * \cdots * x_{n}\right) \text { and }\left(y_{21} * x_{3} * \cdots * x_{n}\right)
$$

are multiplication of $n-1$ items belong to the parties $1,3, \cdots, n$, and $2,3, \cdots, n$ respectively. Thus, the algorithm in step one would be repeated until all the parts of the summation are two-party multiplications, and secure two-party multiplication protocol could be applied.

Therefore, if $n$ parties participate in this protocol, $n(n-1)$ encryptions and $\frac{n(n-1)}{2}$ decryptions are needed to complete the protocol. There are also $n(n-1)$ messages needed to be communicated between the parties.

To make it clear, we give a simple example for three parties:

1. $p_{1}$ and $p_{2}$ run secure two-party multiplication for their inputs, $x_{1}$ and $x_{2}$, that produces $y_{11}$ and $y_{21}$ such that:

$$
x_{1} * x_{2}=y_{11}+y_{21}
$$

2. Therefore, we have:

$$
\begin{aligned}
x_{1} * x_{2} * x_{3} & =\left(y_{11}+y_{21}\right) * x_{3} \\
& =\left(y_{11} * x_{3}\right)+\left(y_{21} * x_{3}\right)
\end{aligned}
$$

3. $p_{1}$ and $p_{3}$ run secure two-party multiplication for their inputs, $y_{11}$ and $x_{3}$, yielding:

$$
y_{11} * x_{3}=y_{1}+y_{31}
$$

4. $p_{2}$ and $p_{3}$ do the same for their inputs, $y_{21}$ and $x_{3}$, such that:

$$
y_{21} * x_{3}=y_{2}+y_{32}
$$

5. Now, we have:

$$
\begin{aligned}
x_{1} * x_{2} * x_{3} & =\left(y_{11}+y_{21}\right) * x_{3} \\
& =\left(y_{11} * x_{3}\right)+\left(y_{21} * x_{3}\right) \\
& =\left(y_{1}+y_{31}\right)+\left(y_{2}+y_{32}\right) \\
& =y_{1}+y_{2}+y_{3}
\end{aligned}
$$

where $y_{3}=y_{31}+y_{32}$

# 4.1.1. Security Analysis 

First, we show that the two-party protocol we have used is in fact secure.
Through this paper, we utilize following notations in our proof:

- $p d$ : Private data.
- $p p d m$ : Privacy-Preserving Data Mining protocol.
- $p d_{p_{i}}: p_{i}$ 's private data.
- $e x t_{p_{i}}$ : The extra information $p_{i}$ can obtain through the underlying protocol.
- gain $p_{p_{i}}$ : The advantage of $p_{i}$ to get access to any other party's private data using a protocol.
- gain $_{\text {sec }}$ : The advantage of $p_{i}$ to get access to any other party's private data using a protocol by looking at a semantically secure ciphertext, which is negligible in our case of using an RSA type of encryption.
- $\operatorname{pr}(p d)$ : The probability of disclosing the private data $p d$ without using any privacy-preserving protocol.
- $\operatorname{pr}(p d \mid p p d m)$ : The probability of disclosing the private data $p d$ after using a privacy-preserving protocol.
- $|\operatorname{pr}(p d \mid p p d m)-\operatorname{pr}(p d)|:$ Absolute difference between the probability of disclosing the private data $p d$ with and without using a privacy-preserving protocol.
- $\epsilon$ : The level of security.

We have to find an $\epsilon$ such that:

$$
$$

Advantages for $p_{1}$ and $p_{2}$ are:

$$
\begin{aligned}
& \text { gain }_{p_{1}}=\operatorname{pr}\left(p d_{p_{2}} \mid e x t_{p_{1}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{2}} \mid e x t_{p_{1}}\right) \\
& \text { gain }_{p_{2}}=\operatorname{pr}\left(p d_{p_{1}} \mid e x t_{p_{2}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{1}} \mid e x t_{p_{2}}\right)
\end{aligned}
$$

$p_{2}$ only receives $E_{1}\left(x_{1}, e_{1}\right)$ from $p_{1}$ which is semantically secure, and therefore:

$$
\text { gain }_{p_{2}}=\text { gain }_{\text {sec }}
$$

which is negligible.
$p_{1}$, by decrypting the message received from $p_{2}$, knows

$$
y_{1}=\left(x_{1} * x_{2}\right)-y_{2}
$$

which is the final desired result for this party. Thus $g a i n_{p_{1}}$ is at most knowing her output share, $y_{1}$. We set:

$$
\begin{aligned}
\epsilon & =\max \left(\text { gain }_{p_{1}}, \text { gain }_{p_{2}}\right) \\
& =\max \left(\text { gain }_{p_{1}}, \text { gain }_{s e c}\right)=\text { gain }_{p_{1}}
\end{aligned}
$$

Therefore, we have:

$$
\operatorname{pr}\left(p d_{p_{2}} \mid e x t_{p_{1}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{2}} \mid e x t_{p_{1}}\right) \leq \text { gain }_{p_{1}}
$$

and

$$
\operatorname{pr}\left(p d_{p_{1}} \mid e x t_{p_{2}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{1}} \mid e x t_{p_{2}}\right) \leq \text { gain }_{p_{1}}
$$

Thus, it proves the maximum advantage of each party is not greater than knowing her final output share, which completes the proof.

Now we prove the security of the protocol for three parties. The proof is the same in general multi-party case. Again, an $\epsilon$ has to be determined, such that:

$$
$$

Advantages of $p_{1}, p_{2}$ and $p_{3}$ are as follows:

$$
\begin{aligned}
& \text { gain }_{p_{1}}= \operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{1}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{1}}\right) \\
& (j=2,3) \\
& \text { gain }_{p_{2}}= \operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{2}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{2}}\right) \\
& (j=1,3) \\
& \text { gain }_{p_{3}}= \operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{3}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{3}}\right) \\
& (j=1,2)
\end{aligned}
$$

$p_{3}$ only receives $E_{1}\left(y_{11}, e_{1}\right)$ from $p_{1}$, and $E_{2}\left(y_{21}, e_{2}\right)$ from $p_{2}$, which are both semantically secure, and therefore:

$$
\text { gain }_{p_{3}}=\text { gain }_{s e c}
$$

which is negligible.
$p_{2}$, by decrypting the message receiving from $p_{3}$, knows

$$
y_{2}=\left(y_{21}+x_{3}\right)-y_{32}
$$

which is the final desired result for this party. $p_{2}$ also receives $E_{1}\left(x_{1}, e_{1}\right)$ from $p_{1}$, which is semantically secure. Thus, $p_{2}$ 's gain is at most her final private output share, $y_{2}$.
$p_{1}$, by decrypting the message received from $p_{3}$, knows

$$
y_{1}=\left(y_{11}+x_{3}\right)-y_{31}
$$

which is the final desired result for this party. Also, $p_{1}$, by decrypting the message receiving from $p_{2}$, knows

$$
y_{11}=\left(x_{1} * x_{2}\right)-y_{21}
$$

$y_{11}$ is the partial information $p_{1}$ receives through her communication with $p_{2}$, but it could not help this party to reach to $p_{2}$ 's private data because of its randomness property, same as $y_{21}$ for $p_{2}$.

Therefore, gain $_{p_{1}}=$ gain $_{p_{2}}$, and we set:

$$
\begin{aligned}
\epsilon & =\max \left(\text { gain }_{p_{1}}, \text { gain }_{p_{2}}, \text { gain }_{p_{3}}\right) \\
& =\max \left(\text { gain }_{p_{1}}, \text { gain }_{s e c}\right)=\text { gain }_{p_{1}}
\end{aligned}
$$

Therefore, we have:

$$
\begin{aligned}
& \operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{1}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{1}}\right) \leq \text { gain }_{p_{1}} \\
& \operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{2}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{2}}\right) \leq \text { gain }_{p_{1}} \\
& \operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{3}}, p p d m\right)-\operatorname{pr}\left(p d_{p_{j}} \mid e x t_{p_{3}}\right) \leq \text { gain }_{p_{1}}
\end{aligned}
$$

Thus, the maximum advantage of each party is not greater than knowing her final output share, which completes the proof.

To show its security against collusion attack, suppose three parties are involved. We investigate all the scenarios in which two parties collude to access the third one's private data.

- Collusion of $p_{1}$ and $p_{2}: p_{1}$ receives

$$
E_{1}\left(y_{11}, e\right)^{x_{3}} * E_{1}\left(y_{31}, e\right)^{-1}
$$

from $p_{3}$ and also, because of colluding with $p_{2}$, receives

$$
E_{2}\left(y_{21}, e\right)^{x_{3}} * E_{2}\left(y_{32}, e\right)^{-1}
$$

from $p_{2}$. However, these two parties have no information about $x_{3}, y_{31}$, and $y_{32}$. Thus, by decrypting the above information and having the two equations:

$$
\begin{aligned}
& y_{11} * x_{3}-y_{31}=y_{1} \\
& y_{21} * x_{3}-y_{32}=y_{2}
\end{aligned}
$$

and those three unknown values, they are not able to access $p_{3}$ 's private data, except by guessing them.

- Collusion of $p_{1}$ and $p_{3}: p_{1}$ receives

$$
E_{1}\left(x_{1}, e\right)^{x_{2}} * E_{1}\left(y_{21}, e\right)^{-1}
$$

from $p_{2}$ and also, because of colluding with $p_{3}$, receives $E_{2}\left(y_{21}, e\right)$ from $p_{2}$. $E_{2}$ is semantically secure and thus $p_{1}$ is not able to get any information from that. Also, $x_{2}$ and $y_{21}$ could not be disclosed to $p_{1}$ from equation, $x_{1} * x_{2}-y_{21}=y_{11}$ alone.

- Collusion of $p_{2}$ and $p_{3}: p_{2}$ receives $E_{1}\left(x_{1}, e\right)$ from $p_{1}$, and also $E_{1}\left(y_{11}, e\right)$ from $p_{3}$ because of colluding. $E_{1}$ is semantically secure, and thus $p_{2}$ is not able to get any useful information from the encrypted data.

This building block could be run over the public channels. This is because none of the parties simply sends the encryption of their private data to the other parties separately, except the owner of the private key. Therefore, even this party is not able to obtain others' private data by decrypting the received messages from the public channel.

# 4.1.2. Complexity Analysis 

- Computation Cost: By denoting $n$ as the number of parties involved in the protocol, there are $\frac{n(n+1)}{2}$ encryptions and $\frac{n(n-1)}{2}$ decryptions in this building block. By assuming that the computation costs of encryption and decryption are the same, and denoting each of these costs by $\alpha$ :

$$
\text { Computation cost }=n^{2} \alpha
$$

- Communication Cost: Communication cost for two parties, as we saw in two party case in Appendix A, is $2 \beta$. By denoting this cost for $n$ parties as $C M M(n), \forall n \geq 3$, and the number of bits exchanged for each message with $\beta$ :

$$
\begin{aligned}
C M M(n)= & \left(C M M\left(\left\lfloor\frac{n}{2}\right\rfloor\right)+C M M\left(\left\lfloor\frac{n}{2}\right\rfloor\right)+\right. \\
& \left.\left\lfloor\frac{n}{2}\right\rfloor *\left(\left\lfloor\frac{n}{2}\right\rfloor+1\right)\right) \beta
\end{aligned}
$$

For instance, if $n=4$, then communication cost of this protocol would be $10 \beta$.

### 4.2. Secure Multi-party Addition

Using this sub-protocol, summation of private input shares, $x_{i}$ s, is converted to the multiplication of private output shares, $y_{i} \mathrm{~s}$.

$$
\sum_{i=1}^{n} x_{i}=\prod_{i=1}^{n} y_{i}
$$

This protocol, with the same lack of security against collusion attack, is proposed in [9]. Here, a protocol is presented to counter collusion attacks. The algorithm for the two-party case is the same as that in [9] and is briefly shown in Appendix B.

Following are the steps of the algorithm for multi-party case:

1. $p_{n}$ selects $n-1$ numbers $x_{n, 1}, x_{n, 2}, \cdots, x_{n, n-1}$ such that:

$$
x_{n}=x_{n, 1}+x_{n, 2}+\cdots+x_{n, n-1}
$$

2. Each party $p_{i}, 1 \leq i \leq n-1$, run a secure two-party addition with $p_{n}$ for their inputs, $x_{i}$ and $x_{n, i}$, such that:

$$
x_{i}+x_{n, i}=y_{i, n} * y_{n}
$$

3. Therefore, we have:

$$
\begin{aligned}
x_{1}+\cdots+x_{n} & =\left(y_{1, n} * y_{n}\right)+\cdots+\left(y_{n-1, n} * y_{n}\right) \\
& =\left(y_{1, n}+\cdots+y_{n-1, n}\right) * y_{n}
\end{aligned}
$$

4. Now

$$
y_{1, n}+\cdots+y_{n-1, n}
$$

is the summation of $n-1$ items belonging to the parties $1,2, \cdots, n-1$. Thus, the algorithm would be repeated from step one until there is a summation of two parties, $p_{1}$ and $p_{2}$, on which secure two-party addition could be applied.

The following is an example for the three parties:

1. $p_{3}$ selects two numbers $x_{3,1}$ and $x_{3,2}$ given:

$$
x_{3}=x_{3,1}+x_{3,2}
$$

2. $p_{1}$ and $p_{3}$ run secure two-party addition for their inputs, $x_{1}$ and $x_{3,1}$ :

$$
x_{1}+x_{3,1}=y_{1,3} * y_{3}
$$

3. $p_{2}$ and $p_{3}$ do the same for their inputs, $x_{2}$ and $x_{3,2}$ :

$$
x_{2}+x_{3,2}=y_{2,3} * y_{3}
$$

4. Therefore, we have:

$$
\begin{aligned}
x_{1}+x_{2}+x_{3} & =\left(y_{1,3} * y_{3}\right)+\left(y_{2,3} * y_{3}\right) \\
& =\left(y_{1,3}+y_{2,3}\right) * y_{3}
\end{aligned}
$$

5. $p_{1}$ and $p_{2}$ run secure two-party addition for their inputs, $y_{1,3}$ and $y_{2,3}$, such that:

$$
y_{1,3}+y_{2,3}=y_{1} * y_{2}
$$

6. Therefore, we have:

$$
x_{1}+x_{2}+x_{3}=\left(y_{1,3}+y_{2,3}\right) * y_{3}=y_{1} * y_{2} * y_{3}
$$

The security analysis of this protocol is similar to that of the secure multi-party multiplication.

# 4.2.1. Complexity Analysis 

- Computation Cost: The number of encryptions and decryptions in this protocol are $\frac{(n-1)(n+2)}{2}$ and $\frac{n(n-1)}{2}$, respectively. Therefore:

$$
\text { Computation cost }=(n-1)(n+1) \alpha
$$

- Communication Cost: By considering all the messages sent from the parties, we have:

$$
\text { Communication cost }=\frac{(n-1)(n+2)}{2} \beta
$$

### 4.3. Secure Product Comparison

In the main protocol we need to compare two products of the private input shares. In other words, if each party $p_{i}$ has two inputs $x_{i}$ and $y_{i}$, we need to compare $\prod_{i=1}^{n} x_{i}$ and $\prod_{i=1}^{n} y_{i}$ to figure out which one is greater than the other one. To do this, we test the sign of the expression $\prod_{i=1}^{n} x_{i}-\prod_{i=1}^{n} y_{i}$. The steps of our algorithm are as follows:

1. All parties run secure multiplication on both series of their inputs such that:

$$
\prod_{i=1}^{n} x_{i}=\sum_{i=1}^{n} a_{i} \quad \text { and } \quad \prod_{i=1}^{n} y_{i}=\sum_{i=1}^{n} b_{i}
$$

2. Each party $p_{i}, 1 \leq i \leq n$, sets :

$$
c_{i}=a_{i}-b_{i}
$$

3. All the parties run secure addition such that:

$$
\sum_{i=1}^{n} c_{i}=\prod_{i=1}^{n} d_{i}
$$

4. Each party $p_{i}, 2 \leq i \leq n$, sends the sign of her final private output share, $d_{i}$, to $p_{1}$.
5. $p_{1}$ counts the number of negative signs of $d_{i} \mathrm{~s}$, and if it is even then:

$$
\prod_{i=1}^{n} x_{i}>\prod_{i=1}^{n} y_{i}
$$

Otherwise:

$$
\prod_{i=1}^{n} x_{i}<\prod_{i=1}^{n} y_{i}
$$

There are two secure multiplications and one secure addition in this protocol. Therefore, for computational cost, we have $3 n(n-1)$ encryptions and $\frac{3 n(n-1)}{2}$ decryptions. Also $3 n(n-1)$ messages plus $n-1$ signs need to be exchanged among $n$ parties.

# 4.3.1. Security Analysis 

In this sub-protocol we use secure addition and multiplication. The only difference is that $p_{1}$ knows the sign of the private output shares of the other parties at the end of the protocol, which will not reveal any useful information to $p_{1}$. Thus, we set:

$$
\begin{aligned}
\epsilon & =\max \left(\text { gain }_{p_{1}}, \cdots, \text { gain }_{p_{n}}\right) \\
& =\max \left(\text { gain }_{p_{1}}, \text { gain }_{s e c}\right)=\text { gain }_{p_{1}}
\end{aligned}
$$

This proves that the maximum advantage of each party is not greater than knowing the sign of the final output shares of the secure comparison.

### 4.3.2. Complexity Analysis

- Computation Cost: There are two secure $n$-party multiplications and one secure $n$-party addition in this building block. Thus:

$$
\text { Computation cost }=\left(3 n^{2}-1\right) \alpha
$$

- Communication Cost: By using the communication costs of the subprotocols used in this building block, we have:

$$
\text { Communication cost }=\left(\frac{(n-1)(n+2)}{2}+\right.
$$

in which $C M M(n)$ is the communication cost of the secure $n$-party multiplication protocol.

### 4.4. Secure Exponentiation

In this building block, we convert an exponentiation with a positive base, when each part, base and exponent, is privately owned by a different party. Suppose, $x_{1} \in p_{1}, x_{2} \in p_{2}$, and $x_{1}>0$. We want to find two private output shares, $z_{1}$ and $z_{2}$, for these parties such that:

$$
x_{1}^{x_{2}}=z_{1} * z_{2}
$$

The following are the steps of the protocol.

1. $p_{1}$ computes $\ln \left(x_{1}\right)$.
2. $p_{1}$ and $p_{2}$ run secure multiplication on their inputs, $\ln \left(x_{1}\right)$ and $x_{2}$, to find their private output shares, $y_{1}$ and $y_{2}$, respectively such that $\ln \left(x_{1}\right) * x_{2}=$ $y_{1}+y_{2}$.
3. Now we have:

$$
\begin{aligned}
x_{1}^{x_{2}} & =\exp ^{\ln \left(x_{1}^{x_{2}}\right)}=\exp ^{x_{2} * \ln \left(x_{1}\right)} \\
& =\exp ^{y_{1}+y_{2}}=\exp ^{y_{1}} * \exp ^{y_{2}}
\end{aligned}
$$

Thus, $\exp ^{y_{1}}$ and $\exp ^{y_{2}}$ are the final private output shares for $p_{1}$ and $p_{2}$, respectively.

# 4.4.1. Security Analysis 

This sub-protocol is just a version of secure multiplication with two differences. First is the input of the first party which is $\ln$ of her input. Second is the final private outputs which are exp of the outputs. Therefore, there is no difference on their security analyses.

### 4.5. Secure Multi-party Factorial

Using this sub-protocol, multiple parties are able to cooperatively produce their own private output shares, $u_{1}, \cdots, u_{n}$ from their private input shares, $x_{1}, \cdots, x_{n}$, such that:

$$
\left(\sum_{i=1}^{n} x_{i}\right)!=\prod_{i=1}^{n} u_{i}
$$

In this protocol, we use Stirling's approximation for factorial and the previously mentioned building blocks, secure addition, multiplication and exponentiation. According to that approximation, for a large number $l$, we have the following equation:

$$
l!\approx \sqrt{2 \pi l}\left(\frac{l}{\exp }\right)^{l}
$$

Also, in the $\mathcal{K} 2$ algorithm we do not need to compute the exact results of the score function. Rather, in each step we just have to compare these results and select the largest one. Therefore, we can use this approximation inside the $\mathcal{K} 2$ algorithm.

Without loss of generality and for simplicity of the formula, we show the two-party case of the protocol, which can easily be generalized to the multiparty case by using the multi-party versions of our building blocks. The steps of the protocol are as follows:

1. $p_{1}$ and $p_{2}$ run secure addition on their inputs, $x_{1}$ and $x_{2}$, to find their private output shares, $y_{1}$ and $y_{2}$, respectively, such that:

$$
x_{1}+x_{2}=y_{1} * y_{2}
$$

Note that $p_{2}$ has to select $y_{2}$ as a positive random number. Therefore, $y_{1}$ is also positive because $x_{1}$ and $x_{2}$ are both positive, and we can run secure exponentiation in the next two steps on $y_{1}$ and $y_{2}$.
2. $p_{1}$ and $p_{2}$ run secure exponentiation on their inputs, $y_{1}$ and $x_{2}$, to find their private output shares, $s_{1}$ and $s_{2}$, respectively, such that:

$$
y_{1}^{x_{2}}=\exp ^{s_{1}} * \exp ^{s_{2}}
$$

3. $p_{1}$ and $p_{2}$ run secure exponentiation on their inputs, $x_{1}$ and $y_{2}$, to find their private output shares, $t_{1}$ and $t_{2}$, respectively such that:

$$
y_{2}^{x_{1}}=\exp ^{t_{1}} * \exp ^{t_{2}}
$$

4. Both of the values $\left(\sqrt{2 \pi y_{1}} * y_{1}^{x_{1}} * \exp ^{s_{1}+t_{1}-x_{1}}\right)$ and $\left(\sqrt{y_{2}} * y_{2}^{x_{2}} * \exp ^{s_{2}+t_{2}-x_{2}}\right)$ are the final output shares for $p_{1}$ and $p_{2}$, respectively.

We can show the correctness of the algorithm as follows:

$$
\begin{aligned}
l! & \approx \sqrt{2 \pi} l\left(\frac{l}{\exp }\right)^{l} \\
& =\sqrt{2 \pi *\left(x_{1}+x_{2}\right)}\left(\frac{x_{1}+x_{2}}{\exp }\right)^{x_{1}+x_{2}} \\
& =\sqrt{2 \pi *\left(y_{1} * y_{2}\right)}\left(\frac{y_{1} * y_{2}}{\exp }\right)^{x_{1}+x_{2}} \\
& =\sqrt{2 \pi y_{1} y_{2}} * \exp ^{-x_{1}} * \exp ^{-x_{2}} * \\
& y_{1}^{x_{1}} * y_{1}^{x_{2}} * y_{2}^{x_{1}} * y_{2}^{x_{2}} \\
& =\sqrt{2 \pi y_{1} y_{2}} * \exp ^{-x_{1}} * \exp ^{-x_{2}} * \\
& y_{1}^{x_{1}} *\left(\exp ^{s_{1}} * \exp ^{s_{2}}\right) *\left(\exp ^{t_{1}} * \exp ^{t_{2}}\right) * y_{2}^{x_{2}} \\
& =\left(\sqrt{2 \pi y_{1}} * y_{1}^{x_{1}} * \exp ^{s_{1}+t_{1}-x_{1}}\right) * \\
& \left(\sqrt{y_{2}} * y_{2}^{x_{2}} * \exp ^{s_{2}+t_{2}-x_{2}}\right) \\
& =u_{1} * u_{2}
\end{aligned}
$$

where $u_{1}$ and $u_{2}$ are respectively substitutes for

$$
\left(\sqrt{2 \pi y_{1}} * y_{1}^{x_{1}} * \exp ^{s_{1}+t_{1}-x_{1}}\right)
$$

and

$$
\left(\sqrt{y_{2}} * y_{2}^{x_{2}} * \exp ^{s_{2}+t_{2}-x_{2}}\right)
$$

Thus, to run secure factorial among $n$ parties $n(n-1)$ secure multiplications and one secure addition will be done.

# 4.5.1. Security Analysis 

First, note that $p_{1}$ and $p_{2}$ have the following data communications during the algorithm:

$$
\begin{aligned}
& p_{1}: E\left(x_{1}, e\right) \longrightarrow p_{2} \\
& p_{2}:\left(E\left(x_{1}, e\right) * E\left(x_{2}, e\right)\right)^{y_{2}^{-1}} \longrightarrow p_{1} \\
& p_{2}: E\left(x_{1}, e\right)^{\ln \left(y_{2}\right)} * E\left(t_{2}, e\right)^{-1} \longrightarrow p_{1} \\
& p_{1}: E\left(\ln \left(y_{1}\right), e\right) \longrightarrow p_{2} \\
& p_{2}: E\left(\ln \left(y_{1}\right), e\right)^{x_{2}} * E\left(s_{2}, e\right)^{-1} \longrightarrow p_{1}
\end{aligned}
$$

Now, we have to find an $\epsilon$ such that:

$$
$$

Advantages of $p_{1}$ and $p_{2}$ are:

$$
\begin{aligned}
& \text { gain }_{p_{1}}=p r\left(p d_{p_{2}} \mid \text { ext }_{p_{1}}, p p d m\right)-p r\left(p d_{p_{2}} \mid \text { ext }_{p_{1}}\right) \\
& \text { gain }_{p_{2}}=p r\left(p d_{p_{1}} \mid \text { ext }_{p_{2}}, p p d m\right)-p r\left(p d_{p_{1}} \mid \text { ext }_{p_{2}}\right)
\end{aligned}
$$

$p_{2}$ receives two encrypted messages from $p_{1}$ using homomorphic encryption $E_{1}$ which is semantically secure, and therefore:

$$
\text { gain }_{p_{2}}=\text { gain }_{s e c}
$$

which is negligible.
$p_{1}$, by decrypting the messages receiving from $p_{2}$, knows

$$
\begin{array}{lll}
y_{1} & \text { such that } & \left(x_{1}+x_{2}\right)=y_{1} * y_{2} \\
s_{1} & \text { such that } & y_{1}^{x_{2}}=s_{1} * s_{2} \\
t_{1} & \text { such that } & y_{2}^{x_{1}}=t_{1} * t_{2}
\end{array}
$$

which are the final desired results for $p_{1}$ to create her private output share. Thus gain $p_{1}$ is at most knowing her output share, $u_{1}$. We set:

$$
\begin{aligned}
\epsilon & =\max \left(\text { gain }_{p_{1}}, \text { gain }_{p_{2}}\right) \\
& =\max \left(\text { gain }_{p_{1}}, \text { gain }_{s e c}\right)=\text { gain }_{p_{1}}
\end{aligned}
$$

Therefore:

$$
\begin{aligned}
& p r\left(p d_{p_{2}} \mid e x t_{p_{1}}, p p d m\right)-p r\left(p d_{p_{2}} \mid e x t_{p_{1}}\right) \leq \text { gain }_{p_{1}} \\
& p r\left(p d_{p_{1}} \mid e x t_{p_{2}}, p p d m\right)-p r\left(p d_{p_{1}} \mid e x t_{p_{2}}\right) \leq \text { gain }_{p_{1}}
\end{aligned}
$$

Thus, the maximum advantage of each party is not greater than knowing her final output share, which completes the proof.

# 4.5.2. Complexity Analysis 

- Computation Cost: One secure $n$-party addition and $n(n-1)$ secure two-party multiplications have to be executed in this sub-protocol. Thus:

$$
\text { Computation cost }=(n-1)(4 n+1) \alpha
$$

- Communication Cost: By using the communication costs of the subprotocols used in this building block, we have:

$$
\text { Communication cost }=\frac{(n-1)(5 n+2)}{2} \beta
$$

### 4.6. Protocol for Horizontally Partitioned Data

In this section, a privacy-preserving BNs protocol is presented for horizontally partitioned data. In this configuration each party owns some records of the whole dataset. We use secure factorial and secure product comparison inside

$\mathcal{K} 2$ algorithm to preserve the privacy of the parties involved. Since each party has the values for all the variables for some records, she can compute and maintain the sufficient statistics of her own data, and thus the value of each record of the sufficient statistics of the whole dataset would be the summation of the corresponding values from the sufficient statistics owned by all the parties.

In steps 3,7 and 20 of the new $\mathcal{K} 2$ algorithm and step 11 of the incremental algorithm, the score function has to be computed for different sets of items. This function, in the horizontal case, is converted to the following equation:

$$
f\left(i, \pi_{i}\right)=\prod_{j=1}^{q_{i}} \frac{\left(\sum_{k=1}^{n} \alpha_{k i j 0}\right)!*\left(\sum_{k=1}^{n} \alpha_{k i j 1}\right)!}{\left(\left(\sum_{k=1}^{n} \alpha_{k i j 0}\right)+\left(\sum_{k=1}^{n} \alpha_{k i j 1}\right)+1\right)!}
$$

where, $\alpha_{k i j r} \in p_{k}$ for $r \in\{0,1\}$. After applying secure factorial building block on each part of the Equation (9) as follows:

$$
\begin{gathered}
\left(\sum_{k=1}^{n} \alpha_{k i j 0}\right)!=\prod_{k=1}^{n} u_{k i j 0} \\
\left(\sum_{k=1}^{n} \alpha_{k i j 1}\right)!=\prod_{k=1}^{n} u_{k i j 1} \\
\left(\left(\sum_{k=1}^{n} \alpha_{k i j 0}\right)+\left(\sum_{k=1}^{n} \alpha_{k i j 1}\right)+1\right)!=\prod_{k=1}^{n} u_{k i j 2}
\end{gathered}
$$

we have a new function $g\left(i, \pi_{i}\right)$, as an approximation of $f\left(i, \pi_{i}\right)$, given by:

$$
\begin{aligned}
g\left(i, \pi_{i}\right) & =\prod_{j=1}^{q_{i}} \frac{\left(\prod_{k=1}^{n} u_{k i j 0}\right)\left(\prod_{k=1}^{n} u_{k i j 1}\right)}{\left(\prod_{k=1}^{n} u_{k i j 2}\right)} \\
& =\prod_{j=1}^{q_{i}} \prod_{k=1}^{n} \frac{u_{k i j 0} * u_{k i j 1}}{u_{k i j 2}}=\prod_{j=1}^{q_{i}} \prod_{k=1}^{n} w_{k i j}=\prod_{k=1}^{n} z_{k}
\end{aligned}
$$

such that $u_{k i j l} \in p_{k}$, and following substitutions:

$$
\frac{u_{k i j 0} * u_{k i j 1}}{u_{k i j 2}}=w_{k i j} \quad \text { and } \quad \prod_{j=1}^{q_{i}} w_{k i j}=z_{k}
$$

where $z_{k}$, for $1 \leq k \leq n$, is the private output share of $p_{k}$.
Now, for each result of the score function we have a multiplication of the private shares owned by the parties. The next step is to compare them and

find the one with the maximum value. For instance for two parties $p_{1}$ and $p_{2}$, if $x_{1}, y_{1} \in p_{1}$ and $x_{2}, y_{2} \in p_{2}$, we have to securely compare $x_{1} * x_{2}$ and $y_{1} * y_{2}$. For this part, the secure product comparison is used, and the item corresponding to the greatest number is added to the set of parents for the current node.

The overhead cost of the proposed privacy-preserving $\mathcal{K} 2$ algorithm is due to the use of the secure factorial and the secure product comparison protocols. If we assume that the maximum number of parents for each node is 2 , then the maximum number of executions of secure factorial and secure comparison are $m^{2}-m+1$ and $(m-1)^{2}$, respectively.

# 4.6.1. Security Analysis 

As we see in the $\mathcal{K} 2$ algorithm, the parties have data communication in steps 3, 7, and 20 in Algorithm 2 and 11 in Algorithm 3 for computing score functions, and in steps 7, 10, 20, and 22 in Algorithm 2, and 11 in Algorithm 3 for comparisons between the products of the private values. Other steps are publicly executed. According to the composition theorem [4, 1], if the main protocol is partitioned into sub-protocols such that the output of one sub-protocol is the input of the next and all intermediate results are kept private, then the whole protocol would be privacy-preserving. In our main protocol, inputs for computing the score function are private shares of the parties. Output shares, by using secure factorial, are also private and are in turn the inputs for the secure product comparison. This sub-protocol is also secure and at the end, only the node or attribute name with the greater value for the score function is determined. Note that the names of the attributes are available to all parties. Therefore the whole protocol remains privacy-preserving.

## 5. Experimental Results

Experiments in this section seek to show the performance improvement of incremental learning compared to the batch algorithm. Datasets used in this experiment are ASIA [20], ADULT [21], and ALARM [19]. The first one is an academic model and the next two are real datasets, widely used in various papers as experimental data. Results are produced from 10 independent replications via 10 -fold cross-validation, and execution time for different set of configurations are compared between incremental and batch algorithms. First we apply standard batch learning protocol on an online database such that each time algorithm runs on the whole dataset, including existing and new data. Then, incremental algorithm is applied in each step such that new data is only used along with some information maintained from the existing data in the previous step, such as sufficient statistics, and the result is compared with the result of using batch method to investigate the correctness of the extracted Bayesian Networks and the overall spending time on each method.

One important parameter in the incremental algorithm is the number of items in each list of candidate parents of each node. The more items are kept in each list, the faster the incremental algorithm would be. We test our protocol

Table 1: Execution time (in Seconds) of Asia model with different key lengths and methods.


with different size of those lists to find an optimum value for this parameter. However, depending on the underlying application and dataset, this can be specified by the user to find the desire network structure. Therefore, there is a trade-off between the execution time and the accuracy of the generated network structure. The complexity of techniques is measured in terms of the execution time requires for training the BNs. The quality of the proposed technique is measured in terms of the similarity of BNs learned through incremental learning to those learned through batch learning. It is also measured in terms of the fitness of BNs with respect to independent test data.

In each experiment, underlying dataset is securely shared between 2, 3, 4, and 6 parties. The implementation is done with Java, in which Remote Method Invocation (RMI) technique is used for data communication. We used machines with 2.66 GHZ CPU, 2.98 GB RAM, and Windows XP Professional. The system is tested with key bit lengths of 512, 1024, and 2048.

The first experiment is performed on ASIA [20] model, also called Chest Clinic, which is a network of a small medical example, indicating whether a patient has bronchitis, tuberculosis, or lung cancer depending on her/his history for X-ray result, dyspnea, visit-to-Asia and smoking status. Figure 2 shows the Bayesian network, containing 8 nodes, and Table 1 shows the performance results of this experiment. In this table performance results of different methods, batch and incremental with different number of items in the parents candidate lists, $S$, and for each key length, are shown. Each execution time for batch method is for 11 times of running the $\mathcal{K} 2$ algorithm, and for incremental method is for one batch algorithm and 10 running of the incremental protocol each time new data is added to the dataset. Results indicate that the execution time will positively decrease using incremental method, especially with the larger value of $S$, compare with the batch algorithm. This is because of applying the protocol on a smaller dataset and previously generated sufficient statistics from the original data, and also checking the candidate parent lists first, before calling $\mathcal{K} 2$ algorithm which is more time consuming.

The next experiment is for Adult [21] model, also known as Census Income dataset, which predicts whether income exceeds $\$ 50 \mathrm{~K} / \mathrm{yr}$ based on census data, and the experiment results are shown in Table 2.

![img-1.jpeg](img-1.jpeg)

Figure 2: ASIA model.

Table 2: Execution time (in Seconds) of Adult model.


![img-2.jpeg](img-2.jpeg)

Figure 3: A Logical Alarm Reduction Mechanism (ALARM) model.

Table 3: Execution time (in Minutes) of Alarm model.


The last experiment is done for ALARM [19] model, stands for A Logical Alarm Reduction Mechanism, which is a medical diagnostic system for patient monitoring. It is a nontrivial belief network with 8 diagnoses, 16 findings and 13 intermediate variables. Figure 3 shows the Bayesian network, and Table 3 contains the performance results of that. Same situation as the previous model is applied.

As it can be seen in the experiment results, by using incremental protocol we can significantly reduce the overall execution time, especially when we are dealing with large number of parties and with large key bit length to strongly preserve the security of the protocol. This time saving is more sensible in large networks, such as Alarm model with 37 nodes in here, after running the protocols during the growth of the underlying dataset. Figure 4 shows the comparison of the execution times of the batch algorithm and incremental protocol with differ-

![img-3.jpeg](img-3.jpeg)

Figure 4: Comparison chart of batch and incremental protocols for ALARM model, with different number of parties, different size of parents candidate list, and key bit length of 1024.
ent parameters after 101 runs of the protocols on data for the Alarm model. For batch algorithm we run the protocol 101 times and for the incremental methods we run the batch algorithm at the first time and then run the incremental protocol for 100 times, each time new data is added to the dataset.

To compare the results of our incremental $\mathcal{K} 2$ algorithm with the result of the batch algorithm, we run the protocol on 16 testing data chunks. At the end of each step the total number of edges and also the fitness of the created edges in the incremental approach are compared with those using batch algorithm. Figures 5 and 6 illustrates the comparison charts for the last experiment, ALARM model. As it is shown in Figure 5, there is a relatively big difference between the number of edges between the incremental and batch approaches in the first couple of steps. This means that incremental algorithm is not very suitable at first, especially with the large value of $S$, the number of items in the parents candidate lists. This could be seen in any real world applications. Suppose a batch algorithm is applied on a large dataset, and after a period of time a block of data, which is very small compare with the original dataset, becomes available. Now the result of applying batch algorithm, which runs on both original and new data, could be far different from the one from incremental method. This might happen because of a very different pattern in the new data from the original one. However, after some duration this bias will be low or even disappeared by coming more data and running incremental algorithm in long term. This fact could be also observed from the comparison chart for fitness of the edges inside constructed BNs structures using batch and incremental methods in Figure 6.

![img-4.jpeg](img-4.jpeg)

Figure 5: Comparison chart of edges inside created BNs structures using batch and incremental K2 algorithm for ALARM model.
![img-5.jpeg](img-5.jpeg)

Figure 6: Comparison chart for fitness of the edges inside constructed BNs structures using batch and our incremental algorithm for ALARM model.

# 6. Conclusions and Future Work 

Incremental learning algorithm for stream and online data to construct Bayesian Networks is considered in this paper when data is privately and horizontally shared among two or more parties, by improvement on computation of Sufficient Statistics and providing an incremental and efficient version of $\mathcal{K} 2$ algorithm. Secure building blocks, such as secure multi-party multiplication, product comparison and factorial, which are resistant to colluding attacks and are secure in dedicated as well as public channels are also proposed to utilize in the main protocol to preserve the privacy of the parties involved. Experimental results indicate that the efficiency will significantly increase by using the new version of incremental $\mathcal{K} 2$ algorithm an improved computation of Sufficient Statistics. Applying the proposed algorithms and protocols on real-world applications, in which privacy and efficiency are crucial factors and data is gradually growing, would be suitable to show the applicability of these methods and to find obstacles and new directions to improve these types of privacy-preserving protocols.

# Appendix A. Secure Two-party Multiplication 

1. $p_{1}$ selects an additive homomorphic encryption $E$, keeps the private key $d$ and sends the public key $e$ to $p_{2}$.
2. $p_{1}$ encrypts her input $x_{1}, E\left(x_{1}, e\right)$, and sends it to $p_{2}$.
3. $p_{2}$ powers the received value to her input $x_{2}, E\left(x_{1}, e\right)^{x_{2}}$, and randomly selects her, nonzero, output share $y_{2}$
4. $p_{2}$ computes $i y_{2}=E\left(y_{2}, e\right)^{-1}$, and sends back $E\left(x_{1}, e\right)^{x_{2}} * i y_{2}$ to $p_{1}$.
5. $p_{1}$ decrypts the received value from $p_{2}$ and sets it as her output share $y_{1}$.

## Appendix A.1. Correctness Analysis

$$
\begin{aligned}
y_{1} & =D\left(E\left(x_{1}, e\right)^{x_{2}} * E\left(y_{2}, e\right)^{-1}, d\right) \\
& =\left(x_{1} * x_{2}\right)-y_{2} \\
& \Rightarrow y_{1}+y_{2}=x_{1} * x_{2}
\end{aligned}
$$

## Appendix A.2. Complexity Analysis

- Computation Cost: There are two encryptions and one decryption in this building block. Therefore:

$$
\text { Computation cost }=3 \alpha
$$

- Communication Cost: Considering the previous notations:

$$
\text { Communication cost }=2 \beta \text {. }
$$

The notations we employed in this section are also used in the similar sections in the rest of this thesis.

# Appendix B. Secure Two-party Addition 

1. $p_{1}$ selects an additive homomorphic encryption $E$, keeps the private key $d$ and sends the public key $e$ to $p_{2}$.
2. $p_{1}$ encrypts her input $x_{1}, E\left(x_{1}, e\right)$, and sends it to $p_{2}$.
3. $p_{2}$ encrypts her input $x_{2}, E\left(x_{2}, e\right)$, and randomly selects her nonzero output share $y_{2}$
4. $p_{2}$ computes $i y_{2}=y_{2}^{-1}$, and sends back $\left(E\left(x_{1}, e\right) * E\left(x_{2}, e\right)\right)^{i y_{2}}$ to $p_{1}$.
5. $p_{1}$ decrypts the received value from $p_{2}$ and sets it as her output share $y_{1}$.

## Appendix B.1. Correctness Analysis

$$
\begin{aligned}
y_{1} & =D\left(\left(E\left(x_{1}, e\right) * E\left(x_{2}, e\right)\right)^{y_{2}^{-1}}, d\right) \\
& =\left(x_{1}+x_{2}\right) * y_{2}^{-1} \\
& \Rightarrow y_{1} * y_{2}=x_{1}+x_{2}
\end{aligned}
$$

## Appendix B.2. Complexity Analysis

- Computation Cost: Similar to the secure two-party multiplication, there are two encryptions and one decryption in this protocol. Therefore:

$$
\text { Computation cost }=3 \alpha
$$

- Communication Cost: Its communication cost is also the same as that in protocol 1:

Communication cost $=2 \beta$.