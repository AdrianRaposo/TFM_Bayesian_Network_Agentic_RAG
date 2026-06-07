# A Bayesian Method for the Induction of Probabilistic Networks from Data 

GREGORY F. COOPER<br>GFC@MED.PITT.EDU<br>Section of Medical Informatics, Department of Medicine, University of Pittsburgh, B50A Lothrop Hall, Pittsburgh, PA 15261<br>EDWARD HERSKOVITS<br>EHH@SUMEX-AIM.STANFORD.EDU<br>Noetic Systems, Incorporated, 2504 Maryland Avenue, Baltimore, MD 21218

Editor: Tom Dietterich


#### Abstract

This paper presents a Bayesian method for constructing probabilistic networks from databases. In particular, we focus on constructing Bayesian belief networks. Potential applications include computer-assisted hypothesis testing, automated scientific discovery, and automated construction of probabilistic expert systems. We extend the basic method to handle missing data and hidden (latent) variables. We show how to perform probabilistic inference by averaging over the inferences of multiple belief networks. Results are presented of a preliminary evaluation of an algorithm for constructing a belief network from a database of cases. Finally, we relate the methods in this paper to previous work, and we discuss open problems.


Keywords. probabilistic networks, Bayesian belief networks, machine learning, induction

## 1. Introduction

In this paper, we present a Bayesian method for constructing a probabilistic network from a database of records, which we call cases. Once constructed, such a network can provide insight into probabilistic dependencies that exist among the variables in the database. One application is the automated discovery of dependency relationships. The computer program searches for a probabilistic-network structure that has a high posterior probability given the database, and outputs the structure and its probability. A related task is computer-assisted hypothesis testing: The user enters a hypothetical structure of the dependency relationships among a set of variables, and the program calculates the probability of the structure given a database of cases on the variables.

We can also construct a network and use it for computer-based diagnosis. For example, suppose we have a database in which a case contains data about the behavior of some system (i.e., findings). Suppose further that a case contains data about whether this particular behavior follows from proper system operation, or alternatively, is caused by one of several possible faults. Assume that the database contains many such cases from previous episodes of proper and faulty behavior. The method that we present in this paper can be used to construct from the database a probabilistic network that captures the probabilistic dependencies among findings and faults. Such a network then can be applied to classify future cases of system behavior by assigning a posterior probability to each of the possible faults and to the event "proper system operation." In this paper, we also shall discuss diagnostic inference that is based on combining the inferences of multiple alternative networks.

Table 1. A database example. The term case in the first column denotes a single training instance (record) in the databaseas for example, a patient case. For brevity, in the text we sometimes use 0 to denote absent and 1 to denote present.


Let us consider a simple example of the tasks just described. Suppose the fictitious database of cases in table 1 is the training set. Suppose further that $x_{1}$ represents a fault in the system, and that $x_{2}$ and $x_{3}$ represent two findings. Given the database, what are the qualitative dependency relationships among the variables? For example, do $x_{1}$ and $x_{3}$ influence each other directly, or do they do so only through $x_{2}$ ? What is the probability that $x_{3}$ will be present if $x_{1}$ is present? Clearly, there are no categorically correct answers to each of these questions. The answers depend on a number of factors, such as the model that we use to represent the data, and our prior knowledge about the data in the database and the relationships among the variables.

In this paper, we do not attempt to consider all such factors in their full generality. Rather, we specialize the general task by presenting one particular framework for constructing probabilistic networks from databases (as, for example, the database in table 1) such that these networks can be used for probabilistic inference (as, for example, the calculation of $P\left(x_{3}=\right.$ present $\left|x_{1}=$ present $\right)$ ). In particular, we focus on using a Bayesian belief network as a model of probabilistic dependency. Our primary goal is to construct such a network (or networks), given a database and a set of explicit assumptions about our prior probabilistic knowledge of the domain.

A Bayesian belief-network structure $B_{S}$ is a directed acyclic graph in which nodes represent domain variables and arcs between nodes represent probabilistic dependencies (Cooper, 1989; Horvitz, Breese, \& Henrion, 1988; Lauritzen \& Spiegelhalter, 1988; Neapolitan, 1990; Pearl, 1986; Pearl, 1988; Shachter, 1988). A variable in a Bayesian belief-network structure may be continuous (Shachter \& Kenley, 1989) or discrete. In this paper, we shall focus our discussion on discrete variables. Figure 1 shows an example of a belief-network structure containing three variables. In this figure, we have drawn an arc from $x_{1}$ to $x_{2}$ to indicate that these two variables are probabilistically dependent. Similarly, the arc from $x_{2}$ to $x_{3}$ indicates a probabilistic dependency between these two variables. The absence of an arc from $x_{1}$ to $x_{3}$ implies that there is no direct probabilistic dependency between $x_{1}$ and $x_{3}$. In particular, the probability of each value of $x_{3}$ is conditionally independent of

![img-0.jpeg](img-0.jpeg)

Figure 1. An example of a belief-network structure, which we shall denote as $B_{S 1}$.
the value of $x_{1}$ given that the value of $x_{2}$ is known. The representation of conditional dependencies and independencies is the essential function of belief networks. For a detailed discussion of the semantics of Bayesian belief networks, see (Pearl, 1988).

A Bayesian belief-network structure, $B_{S}$, is augmented by conditional probabilities, $B_{P}$, to form a Bayesian belief network $B$. Thus, $B=\left(B_{S}, B_{P}\right)$. For brevity, we call $B$ a belief network. For each node ${ }^{1}$ in a belief-network structure, there is a conditional-probability function that relates this node to its immediate predecessors (parents). We shall use $\pi_{i}$ to denote the parent nodes of variable $x_{i}$. If a node has no parents, then a prior-probability function, $P\left(x_{i}\right)$, is specified. A set of probabilities is shown in table 2 for the belief-network structure in figure 1. We used the probabilities in table 2 to generate the cases in table 1 by applying Monte Carlo simulation.

We shall use the term conditional probability to refer to a probability statement, such as $P\left(x_{2}=\right.$ present $\left|x_{1}=\right.$ present $)$. We use the term conditional-probability assignment to denote a numerical assignment to a conditional probability, as, for example, the assignment $P\left(x_{2}=\right.$ present $\left|x_{1}=\right.$ present $)=0.8$. The network structure $B_{S 1}$ in figure 1 and the probabilities $B_{P 1}$ in table 2 together define a belief network which we denote as $B_{1}$.

Belief networks are capable of representing the probabilities over any discrete sample space: The probability of any sample point in that space can be computed from the probabilities in the belief network. The key feature of belief networks is their explicit representation of the conditional independence and dependence among events. In particular, investigators have shown (Kiiveri, Speed, \& Carlin, 1984; Pearl, 1988; Shachter, 1986) that the joint probability of any particular instantiation ${ }^{2}$ of all $n$ variables in a belief network can be calculated as follows:

$$
P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \pi_{i}\right)
$$

where $X_{i}$ represents the instantiation of variable $x_{i}$ and $\pi_{i}$ represents the instantiation of the parents of $x_{i}$.

Therefore, the joint probability of any instantiation of all the variables in a belief network can be computed as the product of only $n$ probabilities. In principle, we can recover the

Table 2. The probability assignments associated with the belief-network structure $B_{S 1}$ in figure 1. We shall denote these probability assignments as $B_{P 1}$.


complete joint-probability space from the belief-network representation by calculating the joint probabilities that result from every possible instantiation of the $n$ variables in the network. Thus, we can determine any probability of the form $P(W \mid V)$, where $W$ and $V$ are sets of variables with known values (instantiated variables). For example, for our sample three-node belief network $B_{1}, P\left(x_{3}=\right.$ present $\left|x_{1}=\right.$ present $)=0.75$.

In the last few years, researchers have made significant progress in formalizing the theory of belief networks (Neapolitan, 1990; Pearl, 1988), and in developing more efficient algorithms for probabilistic inference on belief networks (Henrion, 1990); for some complex networks, however, additional efficiency is still needed. The feasibility of using belief networks in constructing diagnostic systems has been demonstrated in several domains (Agogino \& Rege, 1987; Andreassen, Woldbye, Falck, \& Andersen, 1987; Beinlich, Suermondt, Chavez, \& Cooper, 1989; Chavez \& Cooper, 1990; Cooper, 1984; Heckerman, Horvitz, \& Nathwani, 1989; Henrion \& Cooley, 1987; Holtzman, 1989; Suermondt \& Amylon, 1989).

Although researchers have made substantial advances in developing the theory and application of belief networks, the actual construction of these networks often remains a difficult, time-consuming task. The task is time-consuming because typically it must be performed manually by an expert or with the help of an expert. Important progress has been made in developing graphics-based methods that improve the efficiency of knowledge acquisition from experts for construction of belief networks (Heckerman, 1990). These methods are likely to remain important in domains of small to moderate size in which there are readily available experts. Some domains, however, are large. In others, there are few, if any, readily available experts. Methods are needed for augmenting the manual expert-based methods of knowledge acquisition for belief-network construction. In this paper, we present one such method.

The remainder of this paper is organized as follows. In section 2, we present a method for determining the relative probabilities of different belief-network structures, given a database of cases and a set of explicit assumptions. This method is the primary result of the paper. As an example, consider the database in table 1 , which we call $D$. Let $B_{S 1}$ denote the belief-network structure in figure 1 , and let $B_{S 2}$ denote the structure in figure 2 . The basic method presented in section 2 allows us to determine the probability of $B_{S 1}$ relative to $B_{S 2}$. We show that $P\left(B_{S 1} \mid D\right)$ is 10 times greater than $P\left(B_{S 2} \mid D\right)$, under the assumption that $B_{S 1}$ and $B_{S 2}$ have equal prior probabilities. In section 3 , we discuss methods for searching for the most probable belief-network structures, and we introduce techniques for handling missing data and hidden variables. Section 4 describes techniques for employing
![img-1.jpeg](img-1.jpeg)

Figure 2. A belief-network structure that is an alternative to the structure in figure 1 for characterizing the probabilistic dependencies among the three variables shown. We shall use $B_{S 2}$ to denote this structure.

the methods in section 2 to perform probabilistic inference. In section 5, we report the results of an experiment that evaluates how accurately a 37 -node belief network can be reconstructed from a database that was generated from this belief network. Section 6 contains a discussion of previous work. Section 7 concludes the paper with a summary and discussion of open problems.

# 2. The basic model 

Let us now consider the problem of finding the most probable belief-network structure, given a database. Once such a structure is found, we can derive numerical probabilities from the database (we discuss this task in section 4). We can use the resulting belief network for performing probabilistic inference, such as calculating the value of $P\left(x_{3}=\right.$ present $\left|x_{1}=\right.$ present $)$. In addition, the structure may lend insight into the dependency relationships among the variables in the database; for example, it may indicate possible causal relationships.

Let $D$ be a database of cases, $Z$ be the set of variables represented by $D$, and $B_{s_{i}}$ and $B_{s_{j}}$ be two belief-network structures containing exactly those variables that are in $Z$. In this section, we develop a method for computing $P\left(B_{s_{i}} \mid D\right) / P\left(B_{s_{j}} \mid D\right)$. By computing such ratios for pairs of belief-network structures, we can rank order a set of structures by their posterior probabilities. To calculate the ratio of posterior probabilities, we shall calculate $P\left(B_{S_{i}}, D\right)$ and $P\left(B_{S_{j}}, D\right)$ and use the following equivalence:

$$
\frac{P\left(B_{S_{i}} \mid D\right)}{P\left(B_{S_{j}} \mid D\right)}=\frac{\frac{P\left(B_{S_{i}}, D\right)}{P(D)}}{\frac{P\left(B_{S_{i}}, D\right)}{P(D)}}=\frac{P\left(B_{S_{i}}, D\right)}{P\left(B_{S_{j}}, D\right)}
$$

Let $B_{S}$ represent an arbitrary belief-network structure containing just the variables in $Z$. In section 2.1, we present a method for calculating $P\left(B_{S}, D\right)$. In doing so, we shall introduce several explicit assumptions that render this calculation computationally tractable. A proof of the method for calculating $P\left(B_{S}, D\right)$ is presented in theorem 1 in the appendix.

### 2.1. A formula for computing $P\left(B_{S}, D\right)$

In this section, we present an efficient formula for computing $P\left(B_{S}, D\right)$. We do so by first introducing four assumptions.

Assumption 1. The database variables, which we denote as $Z$, are discrete.
As this assumption states, we shall not consider continuous variables in this paper. One way to handle continuous variables is to discretize them; however, we shall not discuss here the issues involved in such a transformation.

A belief network, which consists of a graphical structure plus a set of conditional probabilities, is sufficient to capture any probability distribution over the variables in $Z$ (Pearl, 1988). A belief-network structure alone, containing just the variables in $Z$, can capture many-but not all-of the independence relationships that might exist in an arbitrary probability distribution over $Z$ (For a detailed discussion, see (Pearl, 1988)).

In this section, we assume that $B_{S}$ contains just the variables in $Z$. In section 3.2 , we allow $B_{S}$ to contain variables in addition to those in $Z$.

The application of assumption 1 yields

$$
P\left(B_{S}, D\right)=\int_{B_{P}} P\left(D \mid B_{S}, B_{P}\right) f\left(B_{P} \mid B_{S}\right) P\left(B_{S}\right) d B_{P}
$$

where $B_{P}$ is a vector whose values denote the conditional-probability assignments associated with belief-network structure $B_{S}$, and $f$ is the conditional-probability density function over $B_{P}$ given $B_{S}$. Note that our assumption of discrete variables leads us to use the probability mass function $P\left(D \mid B_{S}, B_{P}\right)$ in equation 3 , rather than the density function $f\left(D \mid B_{S}\right.$, $B_{P}$ ). The integral in equation (3) is over all possible value assignments to $B_{P}$. Thus, we are integrating over all possible belief networks that can have structure $B_{S}$. The integral represents a multiple integral and the variables of integration are the conditional probabilities associated with structure $B_{S}$.

Example: Consider an example in which $B_{S}$ is the structure $B_{S 1}$ shown in figure 1 and $D$ is the database given by table 1 . Let $B_{P}$ denote an assignment of numerical probability values to a belief network that has structure $B_{S 1}$. Thus, the numerical assignments shown in table 2 constitute one particular value of $B_{P}$-call it $B_{P}^{\prime}$. Integrating over all possible $B_{P}$ corresponds to changing the numbers shown in table 2 in all possible ways that are consistent with the axioms of probability theory. The term $f\left(B_{P}^{\prime} \mid B_{S 1}\right)$ denotes the likelihood of the particular numerical probability assignments shown in table 2 for the beliefnetwork structure $B_{S 1}$. The term $P\left(D \mid B_{S}, B_{P}^{\prime}\right)$ denotes the probability of seeing the data in table 1 , given a belief network with structure $B_{S 1}$ and with probabilities given by table 2. The term $P\left(B_{S 1}\right)$ is our probability-prior to observing the data in database $D$-that the data-generating process is a belief network with structure $B_{S 1}$.

The term $P\left(B_{S}\right)$ in equation (3) can be viewed as one form of preference bias (Buntine, 1990a; Mitchell, 1980) for network structure $B_{S}$. Utgoff defines a preference bias as "the set of all factors that collectively influence hypothesis selection" (Utgoff, 1986). A computerbased system may use any prior knowledge and methods at its disposal to determine $P\left(B_{S}\right)$. This capability provides considerable flexibility in integrating diverse belief construction methods in artificial intelligence (AI) with the learning method discussed in this paper.

Assumption 2. Cases occur independently, given a belief-network model.
A simple version of assumption 2 occurs in the following, well-known example: If a coin is believed with certainty to be fair (i.e., to have a 0.5 chance of landing heads), then the fact that the first flip landed heads (case 1) does not influence our belief that the second flip (case 2) will land heads.

It follows from the conditional independence of cases expressed in assumption 2 that

$$
P\left(B_{S}, D\right)=\int_{B_{P}}\left[\prod_{h=1}^{m} P\left(C_{h} \mid B_{S}, B_{P}\right)\right] f\left(B_{P} \mid B_{S}\right) P\left(B_{S}\right) d B_{P}
$$

where $m$ is the number of cases in $D$ and $C_{h}$ is the $h$ th case in $D$.
Assumption 3. There are no cases that have variables with missing values.
Assumption 3 generally is not valid for real-world databases, where often there are some missing values. This assumption, however, facilitates the derivation of our basic method for computing $P\left(B_{S}, D\right)$. In section 3.2 .1 we discuss methods for relaxing assumption 3 to allow missing data.

Assumption 4. The density function $f\left(B_{P} \mid B_{S}\right)$ in equations (3) and (4) is uniform.
This assumption states that, before we observe database $D$, we are indifferent regarding the numerical probabilities to place on belief-network structure $B_{S}$. Thus, for example, it follows for structure $B_{\text {II }}$ in figure 1 that we believe that $P\left(x_{2}=\right.$ present $\left|x_{1}=\right.$ present $)$ is just as likely to have the value 0.3 as to have the value 0.6 (or to have any other realnumber value in the interval $[0,1]$ ). In corollary 1 in the appendix, we relax assumption 4 to permit the user to employ Dirichlet distributions to specify prior probabilities on the components of $f\left(B_{P} \mid B_{S}\right)$.

We now introduce additional notation that will facilitate our application of the preceding assumptions. We shall represent the parents of $X_{i}$ as a list (vector) of variables, which we denote as $\pi_{i}$. We shall use $w_{i j}$ to designate the $j$ th unique instantiation of the values of the variables in $\pi_{i}$, relative to the ordering of the cases in $D$. We say that $w_{i j}$ is a value or an instantiation of $\pi_{i}$. For example, consider node $x_{2}$ in $B_{S 1}$ and table 1 . Node $x_{1}$ is the parent of $x_{2}$ in $B_{S 1}$, and therefore $\pi_{2}=\left(x_{1}\right)$. In this example, $w_{21}=$ present, because in table 1 the first value of $x_{1}$ is the value present. Furthermore, $w_{22}=$ absent, because the second unique value of $x_{1}$ in table 1 (relative to the ordering of the cases in that table) is the value absent.

Given assumptions 1 through 4 , we prove the following result in the appendix.
Theorem 1. Let $Z$ be a set of $n$ discrete variables, where a variable $x_{i}$ in $Z$ has $r_{i}$ possible value assignments: $\left(v_{i 1}, \ldots, v_{i r_{i}}\right)$. Let $D$ be a database of $m$ cases, where each case contains a value assignment for each variable in $Z$. Let $B_{S}$ denote a belief-network structure containing just the variables in $Z$. Each variable $x_{i}$ in $B_{S}$ has a set of parents, which we represent with a list of variables $\pi_{i}$. Let $w_{i j}$ denote the $j$ th unique instantiation of $\pi_{i}$ relative to $D$. Suppose there are $q_{i}$ such unique instantiations of $\pi_{i}$. Define $N_{i j k}$ to be the number of cases in $D$ in which variable $x_{i}$ has the value $v_{i k}$ and $\pi_{i}$ is instantiated as $w_{i j}$. Let

$$
N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}
$$

Given assumptions 1 through 4 of this section, it follows that

$$
P\left(B_{S}, D\right)=P\left(B_{S}\right) \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

Example: Applying equation (5) to compute $P\left(B_{S 1}, D\right)$, given belief-network structure $B_{S 1}$ in figure 1 and database $D$ in table 1 , yields

$$
\begin{aligned}
P\left(B_{S 1}, D\right) & =P\left(B_{S 1}\right) \frac{(2-1)!5!5!}{(10+2-1)!} \frac{(2-1)!1!4!}{(5+2-1)!} \frac{(2-1)!4!1!}{(5+2-1)!} \frac{(2-1)!0!5!}{(5+2-1)!} \frac{(2-1)!4!1!}{(5+2-1)!} \\
& =P\left(B_{S 1}\right) 2.23 \times 10^{-9}
\end{aligned}
$$

By applying equation (5) for $B_{S 2}$ in figure 2, we obtain $P\left(B_{S 2}, D\right)=P\left(B_{S 2}\right) 2.23 \times$ $10^{-10}$. If we assume that $P\left(B_{S 1}\right)=P\left(B_{S 2}\right)$, then by equation (2), $P\left(B_{S 1} \mid D\right) / P\left(B_{S 2} \mid D\right)=10$. Given the assumptions in this section, the data imply that $B_{S 1}$ is 10 times more likely than $B_{S 2}$. This result is not surprising, because we used $B_{1}$ to generate $D$ by the application of Monte Carlo sampling.

# 2.2. Time complexity of computing $P\left(B_{S}, D\right)$ 

In this section, we derive a worst case time complexity of computing equation (5). In the process, we describe an efficient method for computing that equation. Let $r$ be the maximum number of possible values for any variable, given by $r=\max _{1 \leq i \leq n}\left[r_{i}\right]$. Define $t_{B_{S}}$ to be the time required to compute the prior probability of structure $B_{S}$. For now, assume that we have determined the values of $N_{i j k}$, and have stored them in an array. For a given variable $x_{i}$ the number of unique instantiations of the parents of $x_{i}$, given by $q_{i}$, is at most $m$, because there are only $m$ cases in the database. For a given $i$ and $j$, by definition $N_{i j}=\Sigma_{1 \leq k \leq r_{i}} N_{i j k}$, and therefore we can compute $N_{i j}$ in $O(r)$ time. Since there are at most $m n$ terms of the form $N_{i j}$, we can compute all of these terms in $O(m n r)$ time. Using this result and substituting $m$ for $q_{i}$ and $r$ for $r_{i}$ in equation (5), we find that the complexity of computing equation (5) is $O\left(m n r+t_{B_{S}}\right)$, given that the values of $N_{i j k}$ are known.

Now consider the complexity of computing the values of $N_{i j k}$ for a node $x_{i}$. For a given $x_{i}$, we construct an index tree $T_{i}$, which we define as follows. Assume that $\pi_{i}$ is a list of the parents of $x_{i}$. Each branch out of a node at level $d$ in $T_{i}$ represents a value of the $(d+1)$ th parent of $x_{i}$. A path from the root to a leaf corresponds to some instantiation for the parents of $x_{i}$. Thus, the depth of the tree is equal to the number of parents of $x_{i}$. A given leaf in $T_{i}$ contains counts for the values of $x_{i}$ (i.e., for the values $v_{i 1}, \ldots, v_{i r_{i}}$ ) that are conditioned on the instantiation of the parents of $x_{i}$ as specified by the path from the root to the leaf. If this path corresponds to the $j$ th unique instantiation of $\pi_{i}$ (i.e., $\pi_{i}=w_{i j}$ ), then we denote the leaf as $l_{j}$. Thus, $l_{j}$ in $T_{i}$ corresponds to the list of values of $N_{i i k}$ for $k=1$ to $r_{i}$. We can link the leaves in the tree using a list $L_{i}$. Figure 3 shows an

![img-2.jpeg](img-2.jpeg)

Figure 3. An index tree for node $x_{2}$ in structure $B_{S 1}$ using the data in table 1. In $B_{S 1}, x_{2}$ has only one parentnamely, $x_{1}$; thus, its index tree has a depth of 1 . A $\&$ is used to highlight an entry that is discussed in the text.
index tree for the node $x_{2}$ in $B_{S 1}$ using the database in table 1. For example, in table 1, there are four cases in which $x_{2}$ is assigned the value present (i.e., $x_{2}=1$ ) and its parent $x_{1}$ is assigned the value present (i.e., $x_{1}=1$ ); this situation corresponds to the second column in the second cell of list $L_{2}$ in figure 3, which is shown as $\&$.
Since $x_{i}$ has at most $n-1$ parents, the depth of $T_{i}$ is $O(n)$. Because a variable has at most $r$ values, the size of each node in $T_{i}$ is $O(r)$. To enter a case into $T_{i}$, we must branch on or construct a path that has a total of $O(n)$ nodes, each of size $O(r)$. Thus, a case can be entered in $O(n r)$ time. If the database contained every possible case, then $T_{i}$ would have $O\left(r^{n}\right)$ leaves. However, there are only $m$ cases in the database, so even in the worst case only $O(m)$ leaves will be created. Hence, the time required to construct $T_{i}$ for node $x_{i}$ is $O(m n r)$. Because there are $n$ nodes, the complexity of constructing index trees for all $n$ nodes is $O\left(m n^{2} r\right)$. The overall complexity of both constructing index trees and using them to compute equation (5) is therefore $O\left(m n^{2} r\right)+O\left(m n r+t_{B_{S}}\right)=O\left(m n^{2} r+t_{B_{S}}\right) .^{3}$ If the maximum number of parents of any node is $u$, then the overall complexity is just $O\left(m u n r+t_{B_{S}}\right)$, by a straightforward restriction of the previous analysis. ${ }^{4}$ If $O\left(t_{B_{S}}\right)=$ $O(u n r)$, and $u$ and $r$ can be bounded from above by constants, then the overall complexity becomes simply $O(m n)$.

# 2.3. Computing $P\left(B_{s} \mid D\right)$ 

If we maximize $P\left(B_{S}, D\right)$ over all $B_{S}$ for the database in table 1 , we find that $x_{3} \rightarrow x_{2} \rightarrow x_{1}$ is the most likely structure; we shall use $B_{S 3}$ to designate this structure. Applying equation (5), we find that $P\left(B_{S 3}, D\right)=P\left(B_{S 3}\right) 2.29 \times 10^{-9}$. If we assume that the database was generated by some belief network containing just the variables in $Z$, then we can compute $P(D)$ by summing $P\left(B_{S}, D\right)$ over all possible $B_{S}$ containing just the variables in $Z$. In the remainder of section 2.3 , we shall make this assumption. For the example, there are 25 possible belief-network structures. For simplicity, let us assume that each of these structures is equally likely, a priori. By summing $P\left(B_{S}, D\right)$ over all 25 belief-network structures, we obtain $P(D)=8.21 \times 10^{-10}$. Therefore, $P\left(B_{S 3} \mid D\right)=P\left(B_{S 3}, D\right) / P(D)=$ $(1 / 25) \times 2.29 \times 10^{-9} / 8.21 \times 10^{-10}=0.112$. Similarly, we find that $P\left(B_{S 1} \mid D\right)=0.109$, and $P\left(B_{S 2} \mid D\right)=0.011$.

Now we consider the general case. Let $Q$ be the set of all those belief-network structures that contain just the variables in set $Z$. Then, we have

$$
P\left(B_{S_{i}} \mid D\right)=\frac{P\left(B_{S_{i}}, D\right)}{\sum_{B_{S} \in Q} P\left(B_{S}, D\right)}
$$

As we discuss in section 3.1, the size of $Q$ grows rapidly as a function of the size of $Z$. Consider, however, the situation in which $\Sigma_{B_{S} \in Y} P\left(B_{S}, D\right) \approx P(D)$, for some set $Y \subseteq Q$, where $|Y|$ is small. If $Y$ can be located efficiently, then $P\left(B_{S_{i}} \mid D\right)$ can be approximated closely and computed efficiently. An open problem is to develop heuristic methods that attempt to find such a set $Y$. One approach to computing equation (6) is to use sampling methods to generate a tractable number of belief-network structures and to use these structures to derive an estimate of $P\left(B_{S_{i}} \mid D\right)$.

Let $G$ be a belief-network structure, such that the variables in $G$ are a subset of the variables in $Z$. Let $R$ be the set of those belief-network structures in $Q$ that contain $G$ as a subgraph. We can calculate the posterior probability of $G$ as follows:

$$
P(G \mid D)=\frac{\sum_{B_{S} \in R} P\left(B_{S}, D\right)}{\sum_{B_{S} \in Q} P\left(B_{S}, D\right)}
$$

For example, suppose $Z=\left\{x_{1}, x_{2}, x_{3}\right\}$, and $G$ is the graph $x_{1} \rightarrow x_{2}$. Then, $Q$ is equal to the 25 possible belief-network structures that contain just the variables in $Z$, and $R$ is equal to the 8 possible belief-network structures in $Q$ that contain the subgraph $x_{1} \rightarrow x_{2}$. Applying equation (7), we obtain $P\left(x_{1} \rightarrow x_{2} \mid D\right)$, which is the posterior probability that there is an arc from node $x_{1}$ to node $x_{2}$ in the underlying belief-network process that generated data $D$ (given that the assumptions in section 2.1 hold and that we restrict our model of data generation to belief networks). Probabilities (such as the probability $P\left(x_{1} \rightarrow x_{2} \mid D\right)$ ) could be used to annotate arcs (such as the arc $x_{1} \rightarrow x_{2}$ ) to convey to the user the likelihoods of the existences of possible arcs among the variables in $Z$. Such annotations may be particularly useful for those arcs that have relatively high probabilities. It may be possible to develop efficient heuristic and estimation methods for the computation of equation (7), which are similar to the methods that we mentioned for the computation of equation (6).

When arcs are given a causal interpretation, and specific assumptions are met, we can use previously developed methods to infer causality from data (Pearl \& Verma, 1991; Spirtes, Glymour, \& Scheines, 1990b). These methods do not, however, annotate each arc with its probability of being true. Thus, the resulting categorical statements of causality that are output by these methods may be invalid, particularly when the database of cases is small. In this context, arc probabilities that are derived from equation (7)-such as $P\left(x_{1}\right.$ $\rightarrow x_{2} \mid D$ )-can be viewed as providing information about the likelihood of a causal relationship being true, rather than a categorical statement about that relationship's truth.

We also can calculate the posterior probability of an undirected graph. Let $G^{\prime}$ be an undirected graph, such that the variables in $G^{\prime}$ are a subset of the variables in $Z$. Let $R^{\prime}=\left\{B_{S} \mid B_{S}\right.$ is in $Q$, and if for distinct nodes $x$ and $y$ in $G^{\prime}$ there is an edge between $x$ and $y$ in $G^{\prime}$, then it is the case that $x \rightarrow y$ is in $B_{S}$ or $y \rightarrow x$ is in $B_{S}$, else it is the case that $x$ and $y$ are not adjacent in $B_{S}\}$. By replacing $R$ with $R^{\prime}$ and $G$ with $G^{\prime}$ in equation (7), we obtain a formula for $P\left(G^{\prime} \mid D\right)$. Thus, for example, if we use " - " to denote an undirected edge, then $P\left(x_{1}-x_{2} \mid D\right)$ is the posterior probability that the underlying beliefnetwork process that generated data $D$ contains either an arc from $x_{1}$ to $x_{2}$ or an arc from $x_{2}$ to $x_{1}$.

# 3. Application and extension of the basic model 

In this section, we apply the results of section 2 to develop methods that locate the most probable belief-network structures. We also discuss techniques for handling databases that contain missing values and belief-network structures that contain hidden variables.

### 3.1. Finding the most probable belief-network structures

Consider the problem of determining a belief-network structure $B_{S}$ that maximizes $P\left(B_{S} \mid D\right)$. In general, there may be more than one such structure. To simplify our exposition in this section, we shall assume that there is only one maximizing structure; finding the entire set of maximally probable structures is a straightforward generalization. For a given database $D, P\left(B_{S}, D\right) \propto P\left(B_{S} \mid D\right)$, and therefore finding the $B_{S}$ that maximizes $P\left(B_{S} \mid D\right)$ is equivalent to finding the $B_{S}$ that maximizes $P\left(B_{S}, D\right)$. We can maximize $P\left(B_{S}, D\right)$ by applying equation (5) exhaustively for every possible $B_{S}$.

As a function of the number of nodes, the number of possible structures grows exponentially. Thus, an exhaustive enumeration of all network structures is not feasible in most domains. In particular, Robinson (1977) derives the following efficiently computable recursive function for determining the number of possible belief-network structures that contain $n$ nodes:

$$
f(n)=\sum_{i=1}^{n}(-1)^{i+1}\binom{n}{i} 2^{i(n-i)} f(n-i)
$$

For $n=2$, the number of possible structures is 3 ; for $n=3$, it is 25 ; for $n=5$, it is 29,000 ; and for $n=10$, it is approximately $4.2 \times 10^{18}$. Clearly, we need a method for locating the $B_{S}$ that maximizes $P\left(B_{S} \mid D\right)$ that is more efficient than exhaustive enumeration. In section 3.1.1, we introduce additional assumptions and conditions that reduce the time complexity for determining the most probable $B_{S}$. The complexity of this task, however, remains exponential. Thus, in section 3.1.2, we modify an algorithm from section 3.1.1 to construct a heuristic method that has polynomial time complexity.

# 3.1.1. Exact methods 

Let us assume, for now, that we can specify an ordering on all $n$ variables, such that, if $x_{i}$ precedes $x_{j}$ in the ordering, then we do not allow structures in which there is an arc from $x_{j}$ to $x_{i}$. Given such an ordering as a constraint, there remain $2^{\binom{n}{2}}=2^{n(n-1) / 2}$ possible belief-network structures. For large $n$, it is not feasible to apply equation 5 for each of $2^{n(n-1) / 2}$ possible structures. Therefore, in addition to a node ordering, let us assume equal priors on $B_{S}$. That is, initially, before we observe the data $D$, we believe that all structures are equally likely. In that case, we obtain

$$
P\left(B_{S}, D\right)=c \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

where $c$ is the constant prior probability, $P\left(B_{S}\right)$, for each $B_{S}$. To maximize equation (8), we need only to find the parent set of each variable that maximizes the second inner product. Thus, we have that

$$
\max _{B_{S}}\left[P\left(B_{S}, D\right)\right]=c \prod_{i=1}^{n} \max _{\pi_{i}}\left[\prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!\right]
$$

where the maximization on the right of equation (9) takes place over every instantiation of the parents $\pi_{i}$ of $x_{i}$ that is consistent with the ordering on the nodes.

A node $x_{i}$ can have at most $n-1$ nodes as parents. Thus, over all possible $B_{S}$ consistent with the ordering, $x_{i}$ can have no more than $2^{n-1}$ unique sets of parents. Therefore, the maximization on the right of equation (9) occurs over at most $2^{n-1}$ parent sets. It follows from the results in section 2.2 that the products within the maximization operator in equation (9) can be computed in $O(m n r)$ time. Therefore, the time complexity of computing equation (9) is $O\left(m n^{2} r 2^{n}\right)$. If we assume that a node can have at most $u$ parents, then the complexity is only $O(m u n r T(n, u))$, where

$$
T(n, u)=\sum_{0 \leq k \leq u}\binom{n}{k}
$$

Let us now consider a generalization of equation (9). Let $\pi_{i}^{S}$ be the parents of $x_{i}$ in $B_{S}$, denoted as $\pi_{i}^{S} \rightarrow x_{i}$. Assume that $P\left(B_{S}\right)$ can be calculated as $P\left(B_{S}\right)=\Pi_{1 \leq i \leq n} P\left(\pi_{i}^{S} \rightarrow x_{i}\right)$. Thus, for all distinct pairs of variables $x_{i}$ and $x_{j}$, our belief about $x_{i}$ having some set of parents is independent of our belief about $x_{j}$ having some set of parents. Using this assumption of independence of priors, we can express equation (5) as

$$
P\left(B_{S}, D\right)=\prod_{i=1}^{n} P\left(\pi_{i}^{S} \rightarrow x_{i}\right) \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

The probability $P\left(\pi_{i}^{S} \rightarrow x_{i}\right)$ could be assessed directly or be derived with additional methods. For example, one method would be to assume that the presence of an arc in $\pi_{i}^{S} \rightarrow x_{i}$ is independent of the presence of the other arcs there; if the probability of each arc in $\pi_{i}^{S} \rightarrow x_{i}$ is specified, we then can compute $P\left(\pi_{i}^{S} \rightarrow x_{i}\right)$. Suppose, as before, that we have an ordering on the nodes. Then, from equation (10), we see that

$$
\max _{B_{S}}\left[P\left(B_{S}, D\right)\right]=\prod_{i=1}^{n} \max _{\pi_{i}}\left[P\left(\pi_{i} \rightarrow x_{i}\right) \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!\right]
$$

where the maximization on the right of equation (11) is taken over all possible sets $\pi_{i}$ consistent with the node ordering. The complexity of computing equation (11) is the same as that of computing equation (9), except for an additional term that represents an upper bound on the complexity of computing $P\left(\pi_{i} \rightarrow x_{i}\right)$. From equation (11), we see that the determination of the most likely belief-network structure is computationally feasible if we assume (1) that there is an ordering on the nodes, (2) that there exists a sufficiently tight limit on the number of parents of any node, and (3) that $P\left(\pi_{i} \rightarrow x_{i}\right)$ and $P\left(\pi_{j} \rightarrow x_{j}\right)$ are marginally independent when $i \neq j$, and we can compute such prior probabilities efficiently. Unfortunately, the second assumption in the previous sentence may be particularly difficult to justify in practice. For this reason, we have developed a polynomial-time heuristic algorithm that requires no restriction on the number of parents of a node, although it does permit such a restriction.

# 3.1.2. A heuristic method 

We propose here one heuristic-search method, among many possibilities, for maximizing $P\left(B_{S}, D\right)$. We shall use equation (9) as our starting point, with the attendant assumptions that we have an ordering on the domain variables and that, a priori, all structures are considered equally likely. We shall modify the maximization operation on the right of equation (9) to use a greedy-search method. In particular, we use an algorithm that begins by making the assumption that a node has no parents, and then adds incrementally that parent whose addition most increases the probability of the resulting structure. When the addition of no single parent can increase the probability, we stop adding parents to the node. Researchers have made extensive use of similar greedy-search methods in classification systems-for example, to construct classification trees (Quinlan, 1986) and to perform variable selection (James, 1985).

We shall use the following function:

$$
g\left(i, \pi_{i}\right)=\prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

where the $N_{i j k}$ are computed relative to $\pi_{i}$ being the parents of $x_{i}$ and relative to a database $D$, which we leave implicit. From section 2.2 , it follows that $g\left(i, \pi_{i}\right)$ can be computed in $O(m u r)$ time, where $u$ is the maximum number of parents that any node is permitted to have, as designated by the user. We also shall use a function $\operatorname{Pred}\left(x_{i}\right)$ that returns the set of nodes that precede $x_{i}$ in the node ordering. The following pseudocode expresses the heuristic search algorithm, which we call K2
```
1. procedure K2;
2. {Input: A set of $n$ nodes, an ordering on the nodes, an upper bound $u$ on the
3. number of parents a node may have, and a database $D$ containing $m$ cases.}
4. {Output: For each node, a printout of the parents of the node.}
5. for i:=1 to n do
6. $\pi_{i}:=\emptyset$;
7. $P_{\text {old }}:=g\left(i, \pi_{i}\right)$; \{This function is computed using equation (12).\}
8. OKToProceed $:=$ true
9. while OKToProceed and $\left|\pi_{i}\right|<u$ do
10. let $z$ be the node in $\operatorname{Pred}\left(x_{i}\right)-\pi_{i}$ that maximizes $g\left(i, \pi_{i} \cup\{z\}\right)$;
11. $P_{\text {new }}:=g\left(i, \pi_{i} \cup\{z\}\right)$;
12. if $P_{\text {new }}>P_{\text {old }}$ then
13. $P_{\text {old }}:=P_{\text {new }} ;$
14. $\pi_{i}:=\pi_{i} \cup\{z\}$
15. else OKToProceed $:=$ false;
16. end \{while\};
17. write('Node:', $x_{i}$, 'Parents of this node:', $\pi_{i}$ )
18. end \{for\};
19. end $\{\mathrm{K} 2\}$;
```
We now analyze the time complexity of K2. We shall assume that the factorials that are required to compute equation (12) have been precomputed and have been stored in an array. Equation (12) contains no factorial greater than $(m+r-1)$ !, because $N_{i j}$ can have a value no greater than $m$. We can compute and store the factorials of the integers from 1 to $(m+r-1)$ in $O(m+r-1)$ time. A given execution of line 10 of the K2 procedure requires that $g$ be called at most $n-1$ times, because $x_{i}$ has at most $n-1$ predecessors in the ordering. Since each call to $g$ requires $O(m u r)$ time, line 10 requires $O(m u n r)$ time. The other statements in the while statement require $O(1)$ time. Each time the while statement is entered, it loops $O(u)$ times. The for statement loops $n$ times. Combining these results, the overall complexity of K 2 is $O(m+r-1)+O(m u n r) O(u) n=O\left(m u^{2}\right.$ $n^{2} r$ ). In the worst case, $u=n$, and the complexity of K 2 is $O\left(m n^{4} r\right)$.

We can improve the run-time speed of K 2 by replacing $g\left(i, \pi_{i}\right)$ and $g\left(i, \pi_{i} \cup\{z\}\right)$ by $\log \left(g\left(i, \pi_{i}\right)\right)$ and $\log \left(g\left(i, \pi_{i} \cup\{z\}\right)\right)$, respectively. Run-time savings result because the logarithmic version of equation (12) requires only addition and subtraction, rather than multiplication and division. If the logarithmic version of equation (12) is used in K2, then the logarithms of factorials should be precomputed and should be stored in an array.

We emphasize that K2 is just one of many possible methods for searching the space of belief networks to maximize the probability metric given by equation (5). Accordingly, theorem 1 and equation (5) represent more fundamental results than does the K2 algorithm. Nonetheless, K2 has proved valuable as an initial search method for obtaining preliminary

test results, which we shall describe in section 5. An open research problem is to explore other search methods. For example, consider an algorithm that differs from K2 only in that it begins with a fully connected belief-network structure (relative to a given node order) and performs a greedy search by removing arcs; call this algorithm K2R (K2 Reverse). We might apply K2 to obtain a belief-network structure, then apply K2R to obtain another structure, and finally report whichever structure is more probable according to equation (5). Another method of search is to generate multiple random node orders, to apply K2 using each node order, and to report which among the belief-network structures output by K2 is most probable. Other search techniques that may prove useful include methods that use beam search, branch-and-bound techniques, and simulated annealing.

# 3.2. Missing data and hidden variables 

In this section, we introduce normative methods for handling missing data and hidden variables in the induction of belief networks from databases. These two methods are fundamentally the same. As we present them, neither method is efficient enough to be practical in most real-world applications. We introduce them here for two reasons. First, they demonstrate that the Bayesian approach developed in this paper admits conceptually simple and theoretically sound methods for handling the difficult problems of missing data and hidden variables. Second, these methods establish a theoretical basis from which it may be possible to develop more efficient approaches to these two problems. Without such a theoretical basis, it may be difficult to develop sound methods for addressing the problems pragmatically.

### 3.2.1. Missing data

In this section, we consider cases in database $D$ that may contain missing values for some variables. Let $C_{h}$ denote the set of variable assignments for those variables in the $h$ th case that have known values and let $C_{h}^{\prime}$ denote the set of variables in the case that have missing values. The probability of the $h$ th case can be computed as

$$
P\left(C_{h} \mid B_{S}, B_{P}\right)=\sum_{C_{h}^{\prime}} P\left(C_{h}, C_{h}^{\prime} \mid B_{S}, B_{P}\right)
$$

where $\Sigma_{C_{h}^{\prime}}$ means that all the variables in $C_{h}^{\prime}$ are running through all their possible values. By substituting equation (13) into equation (4), we obtain

$$
P\left(B_{S}, D\right)=\int_{B_{P}}\left[\prod_{h=1}^{m}\left[\sum_{C_{h}^{\prime}} P\left(C_{h}, C_{h}^{\prime} \mid B_{S}, B_{P}\right)\right]\right] f\left(B_{P} \mid B_{S}\right) P\left(B_{S}\right) d B_{P}
$$

To facilitate the next step of the derivation, we now introduce additional notation to describe the value assignments of variables. Let $x_{i}$ be an arbitrary variable in $C_{h}^{\prime}$ or $C_{h}$. We shall write a value assignment of $x_{i}$ as $x_{i}=d_{i h}$, where $d_{i h}$ is the value of $x_{i}$ in case $h$. For a

variable $x_{i}$ in $C_{h}^{\prime}, d_{i h}$ is not known, because $x_{i}$ is a variable with a missing value. The sum in equation (13) means that for each variable $x_{i}$ in $C_{h}^{\prime}$ we have $d_{i h}$ assume each value that is possible for $x_{i}$. The overall effect is the same as stated previously for equation (13).

As an example, consider a database containing three binary variables that each have present or absent as a possible value. Suppose in case 7 that variable $x_{1}$ has the value present and the values of variables $x_{2}$ and $x_{3}$ are not known. In this example, $C_{7}=\left\{x_{1}=\right.$ present $\}$, and $C_{7}^{\prime}=\left\{x_{2}=d_{27}, x_{3}=d_{37}\right\}$. For case 7 , equation (13) states that the sum is taken over the following four joint substitutions of values for $d_{27}$ and $d_{37}$ : $\left\{d_{27} \leftarrow\right.$ absent, $d_{37} \leftarrow$ absent $\},\left\{d_{27} \leftarrow\right.$ absent, $d_{37} \leftarrow$ present $\},\left\{d_{27} \leftarrow\right.$ present, $d_{37} \leftarrow$ absent $\}$, and $\left\{d_{27} \leftarrow\right.$ present, $d_{37} \leftarrow$ present $\}$. For each such joint substitution, we evaluate the probability within the sum of equation (13).

The reason we introduced the $d_{i h}$ notation is that it allows us to assign case-specific values to variables with missing values. We need this ability in order to move the summation in equation (14) to the outside of the integral. In particular, we now can rearrange equation (14) as follows:

$$
P\left(B_{S}, D\right)=\sum_{C_{i}^{\prime}} \ldots \sum_{C_{m}^{\prime}} \int_{B_{P}}\left[\prod_{h=1}^{m} P\left(C_{h}, C_{h}^{\prime} \mid B_{S}, B_{P}\right)\right] f\left(B_{P} \mid B_{S}\right) P\left(B_{S}\right) d B_{P}
$$

Equation 15 is a sum of the type of integrals represented by equation (4), which we solved using equation (5). Thus, equation (15) can be solved by multiple applications of equation (5).

The complexity of computing equation (15) is exponential in the number of missing values in the database. As stated previously, this level of complexity is not computationally tractable for most real-world applications. Equation 15 does, however, provide us with a theoretical starting point for seeking efficient approximation and special-case algorithms, and we are pursuing the development of such algorithms. Meanwhile, we are using a more efficient approach for handling missing data. In particular, if a variable in a case has a missing value, then we give it the value $U$ (for unknown). Thus, for example, a binary variable could be instantiated to one of three values: absent, present, or $U$. Other approaches are possible, including those that compute estimates of the missing values and use these estimates to fill in the values.

Example: Suppose that our database $D$ is limited to the first two cases in table 1, and that the value of $x_{2}$ in the first case is missing. Let us calculate $P\left(B_{S 1}, D\right)$. Applying equation (14), we have

$$
\begin{gathered}
P\left(B_{S 1}, D\right)=\int_{B_{P}}\left[P\left(x_{1}=1, x_{2}=0, x_{3}=0 \mid B_{S 1}, B_{P}\right)+P\left(x_{1}=1, x_{2}=1\right.\right. \\
\left.\left.x_{3}=0 \mid B_{S 1}, B_{P}\right)\right] \times P\left(x_{1}=1, x_{2}=1, x_{3}=1 \mid B_{S 1}, B_{P}\right) f\left(B_{P} \mid B_{S 1}\right) P\left(B_{S 1}\right) d B_{P}
\end{gathered}
$$

which, by equation (15), is equal to

$$
\begin{aligned}
& \int_{B_{P}} P\left(x_{1}=1, x_{2}=0, x_{3}=0 \mid B_{S 1}, B_{P}\right) P\left(x_{1}=1, x_{2}=1, x_{3}=1 \mid B_{S 1}, B_{P}\right) \\
& f\left(B_{P} \mid B_{S 1}\right) P\left(B_{S 1}\right) d B_{P} \\
& +\int_{B_{P}} P\left(x_{1}=1, x_{2}=1, x_{3}=0 \mid B_{S 1}, B_{P}\right) P\left(x_{1}=1, x_{2}=1, x_{3}=1 \mid B_{S 1}, B_{P}\right) \\
& f\left(B_{P} \mid B_{S 1}\right) P\left(B_{S 1}\right) d B_{P}
\end{aligned}
$$

Each of these last two integrals can be solved by the application of equation (5).

# 3.2.2. Hidden variables 

A hidden (latent) variable represents a postulated entity about which we have no data. For example, we may wish to postulate the existence of a hidden variable if we are looking for a hidden causal factor that influences the production of the data that we do observe. We can handle a hidden variable (or variables) by applying equation (15), where the hidden variable is assigned a missing value for each case in the database. In a belief-network structure, the hidden variable is represented as a single node, just as is any other variable.

Example: Assume the availability of the database shown in table 3, which we shall denote as $D$.

Suppose that we wish to know $P\left(B_{S 2}, D\right)$, where $B_{S 2}$ is the network structure shown in figure 2. Note that, relative to $D, x_{1}$ is a hidden variable, because $D$ contains no data about $x_{1}$. Let us assume for this example that $x_{1}$ is a binary variable. Applying equation (15), we obtain the following result:
$P\left(B_{S 2}, D\right)=$

$$
\begin{aligned}
& \int_{B_{P}} P\left(x_{1}=0, x_{2}=0, x_{3}=0 \mid B_{S 2}, B_{P}\right) P\left(x_{1}=0, x_{2}=1, x_{3}=1 \mid B_{S 2}, B_{P}\right) \\
& f\left(B_{P} \mid B_{S 2}\right) P\left(B_{S 2}\right) d B_{P} \\
& +\int_{B_{P}} P\left(x_{1}=0, x_{2}=0, x_{3}=0 \mid B_{S 2}, B_{P}\right) P\left(x_{1}=1, x_{2}=1, x_{3}=1 \mid B_{S 2}, B_{P}\right) \\
& f\left(B_{P} \mid B_{S 2}\right) P\left(B_{S 2}\right) d B_{P} \\
& +\int_{B_{P}} P\left(x_{1}=1, x_{2}=0, x_{3}=0 \mid B_{S 2}, B_{P}\right) P\left(x_{1}=0, x_{2}=1, x_{3}=1 \mid B_{S 2}, B_{P}\right) \\
& f\left(B_{P} \mid B_{S 2}\right) P\left(B_{S 2}\right) d B_{P} \\
& +\int_{B_{P}} P\left(x_{1}=1, x_{2}=0, x_{3}=0 \mid B_{S 2}, B_{P}\right) P\left(x_{1}=1, x_{2}=1, x_{3}=1 \mid B_{S 2}, B_{P}\right) \\
& f\left(B_{P} \mid B_{S 2}\right) P\left(B_{S 2}\right) d B_{P}
\end{aligned}
$$

Each of these four integrals can be solved by application of equation (5).

Table 3. The database for the hidden variable example.


One difficulty in considering the possibility of hidden variables is that there is an unlimited number of them and thus an unlimited number of belief-network structures that can contain them. There are many possible approaches to this problem; we shall outline here the approaches that we believe are particularly promising. One way to avoid the problem is simply to limit the number of hidden variables in the belief networks that we postulate. Another approach is to specify explicitly nonzero priors for only a limited number of belief-network structures that contain hidden variables. In addition, we may be able to use statistical indicators that suggest probable hidden variables, as discussed in (Pearl \& Verma, 1991; Spirtes \& Glymour, 1990; Spirtes et al., 1990b; Verma \& Pearl, 1990); we then could limit ourselves to postulating hidden variables only where these indicators suggest that hidden variables may exist.

A related problem is to determine the number of values to define for a hidden variable. One approach is to try different numbers of values. That is, we make the number of values of each hidden variable be a parameter in the search space of belief-network structures. We note that some types of unsupervised learning have close parallels to discovering the number of values to assign to hidden variables. For example, researchers have successfully applied unsupervised Bayesian learning methods to determine the most probable number of values of a single, hidden classification variable (Cheeseman, Self, Kelly, Taylor, Freeman, \& Stutz, 1988). We believe that similar methods may prove useful in addressing the problem of learning the number of values of hidden variables in belief networks.

# 4. Expectations of probabilities 

The previous sections concentrated on belief-network structures. In this section, we focus on deriving numerical probabilities when given a database and a belief-network structure (or structures). In particular, we shall focus on determining the expectation of probabilities.

### 4.1. Expectations of network conditional probabilities

Let $\theta_{i j k}$ denote the conditional probability $P\left(x_{i}=v_{i k} \mid \pi_{i}=w_{i j}\right)$-that is, the probability that $x_{i}$ has value $v_{i k}$, for some $k$ from 1 to $r_{i}$, given that the parents of $x_{i}$, represented by $\pi_{i}$, are instantiated as $w_{i j}$. Call $\theta_{i j k}$ a network conditional probability. Let $\xi$ denote the four assumptions in section 2.1. Consider the value of $E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]$, which is the expected

value of $\theta_{i j k}$ given database $D$, the belief-network structure $B_{S}$, and the assumptions $\xi$. In theorem 2 in the appendix, we derive the following result:

$$
E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]=\frac{N_{i j k}+1}{N_{i j}+r_{i}}
$$

In corollary 2 in the appendix, we derive a more general version of $E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]$ by relaxing assumption 4 in section 2.1 to allow the user to express prior probabilities on the values of network conditional probabilities. $E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]$ is sometimes called the Bayes' estimator of $\theta_{i j k}$. The value of $E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]$ in equation (16) is equal to the expectation of $\theta_{i j k}$ as calculated using a uniform probability distribution and using the data in $D$ (deGroot, 1970). We note that Spiegelhalter and Lauritzen (1990) also have used such expectations in their work on updating belief-network conditional probabilities.

By applying an analogous analysis for variance, we can show that (Wilks, 1962)

$$
\operatorname{Var}\left[\theta_{i j k} \mid D, B_{S}, \xi\right]=\frac{\left(N_{i j k}+1\right)\left(N_{i j}+r_{i}-N_{i j k}-1\right)}{\left(N_{i j}+r_{i}\right)^{2}\left(N_{i j}+r_{i}+1\right)}
$$

Example: Consider the probability $P\left(x_{2}=\right.$ present $\left|x_{1}=\right.$ present $)$ for belief-network structure $B_{S 1}$. Let $\theta_{212}$ represent $P\left(x_{2}=\right.$ present $\left|x_{1}=\right.$ present $)$. We now wish to determine $E\left[\theta_{212} \mid D, B_{S}, \xi\right]$ and $\operatorname{Var}\left[\theta_{212} \mid D, B_{S}, \xi\right]$, where $D$ is the database in table 1 . Since $x_{2}$ is a binary variable, $r_{2}=2$. There are five cases in $D$ in which $x_{1}=$ present and therefore, $N_{21}=5$. Of these five, there are four cases in which $x_{1}=$ present and $x_{2}=$ present, and, thus, $N_{212}=4$. Substituting these values into equations (16) and (17), we obtain $E\left[\theta_{212} \mid D\right.$, $\left.B_{S}, \xi\right]=0.71$ and $\operatorname{Var}\left[\theta_{212} \mid D, B_{S}, \xi\right]=0.03$.

# 4.2. Expectations of general conditional probabilities given a network structure 

A common application of a belief network is to determine $E\left[P\left(W_{1} \mid W_{2}\right)\right]$, where $W_{1}$ and $W_{2}$ are sets of instantiated variables. For example, $W_{1}$ might be a disease state and $W_{2}$ a set of symptoms. Consider a decision that depends on just the likelihood of $W_{1}$, given that $W_{2}$ is known. Researchers have shown that $E\left[P\left(W_{1} \mid W_{2}\right)\right]$ provides sufficient information to determine the optimal decision to make within a decision-theoretic framework, as long as the decision must be made without the benefit of additional information (Howard, 1988). Thus, in many situations, knowledge of $E\left[P\left(W_{1} \mid W_{2}\right)\right]$ is sufficient for decision making.

Since, in this paper we are constructing belief networks based on a database $D$, we wish to know $E\left[P\left(W_{1} \mid W_{2}\right) \mid D, B_{S}, \xi\right]$. In (Cooper \& Herskovits, 1991), we derive the following equation:

$$
E\left[P\left(W_{1} \mid W_{2}\right) \mid D, B_{S}, \xi\right]=P\left(W_{1} \mid W_{2}\right)
$$

where $P\left(W_{1} \mid W_{2}\right)$ is computed with a belief network that uses the probabilities given by equation (16).

# 4.3. Expectations of general conditional probabilities over all network structures 

On the right side of equation (18), $D, B_{S}$ and $\xi$ are implicit conditioning information. To be more explicit, we can rewrite that equation as

$$
E\left[P\left(W_{1} \mid W_{2}\right) \mid D, B_{S}, \xi\right]=P\left(W_{1} \mid W_{2}, D, B_{S}, \xi\right)
$$

where $P\left(W_{1} \mid W_{2}, D, B_{S}, \xi\right)$ may be calculated as $P\left(W_{1} \mid W_{2}\right)$ using a belief network with a structure $B_{S}$ and with conditional probabilities that are derived using equation (16). For optimal decision making, however, we actually wish to know $E\left[P\left(W_{1} \mid W_{2}\right) \mid D, \xi\right]$, rather than $E\left[P\left(W_{1} \mid W_{2}\right) \mid D, B_{S}, \xi\right]$ for some particular $B_{S}$ about which we are uncertain. We can derive $E\left[P\left(W_{1} \mid W_{2}\right) \mid D, \xi\right]$ as

$$
E\left[P\left(W_{1} \mid W_{2}\right) \mid D, \xi\right]=\sum_{B_{S}} E\left[P\left(W_{1} \mid W_{2}\right) \mid D, B_{S}, \xi\right] P\left(B_{S} \mid W_{2}, D \xi\right)
$$

which, by equation (19), becomes

$$
E\left[P\left(W_{1} \mid W_{2}\right) \mid D, \xi\right]=\sum_{B_{S}} P\left(W_{1} \mid W_{2}, D, B_{S}, \xi\right) P\left(B_{S} \mid W_{2}, D \xi\right)
$$

The probability $P\left(B_{S} \mid W_{2}, D, \xi\right)$ is interesting because it contains $W_{2}$ as conditioning information. We can view $W_{2}$ as additional data that augment $D$. If $D$ is large, we may choose to approximate $P\left(B_{S} \mid W_{2}, D, \xi\right)$ as $P\left(B_{S} \mid D, \xi\right)$. Alternatively, we may choose to assume that $W_{2}$ provides no additional information about $B_{S}$, and therefore that $P\left(B_{S} \mid W_{2}, D, \xi\right)$ $=P\left(B_{S} \mid D, \xi\right)$. Otherwise, we must treat $W_{2}$ as an additional case in the database. Typically, $W_{2}$ will represent an incomplete case in which some model variables have unknown values. In this situation, the techniques we discuss in section 3.2.1 for handling missing data can be used to compute $P\left(B_{S} \mid W_{2}, D, \xi\right)$.

Although it is not computationally feasible to calculate equation (20) for models with more than a few variables, this equation provides a theoretical framework for seeking rapid and accurate special-case, approximate and heuristic solutions. For example, techniques-such as those discussed in the final paragraph of section 3.1-might be used in searching for belief-network structures that yield relatively high values for $P\left(B_{S} \mid W_{2}, D, \xi\right)$. If we normalize over this set of structures, we can apply equation (20) to estimate heuristically the value of $E\left[P\left(W_{1} \mid W_{2}\right) \mid D, \xi\right]$. Another possible approach toward estimating $E\left[P\left(W_{1} \mid W_{2}\right) \mid D, \xi\right]$ is to apply sampling techniques that use stochastic simulation.

Example: Suppose we wish to know $P\left(x_{2}=\right.$ present $\mid x_{1}=$ present $)$ given database $D$, which is shown in table 4.

Let us compute $P\left(x_{2}=\right.$ present $\mid x_{1}=$ present $)$ by using equation (20) and the assumption that $P\left(B_{S} \mid x_{1}=\right.$ present, $\left.D, \xi\right)=P\left(B_{S} \mid D, \xi\right)$. For simplicity, we abbreviate $P\left(x_{2}=\right.$ present $\mid x_{1}=$ present) as $P\left(x_{2} \mid x_{1}\right)$, leaving the values of $x_{1}$ and $x_{2}$ implicit. We shall enclose network structures in braces for clarity; so, for example, $\left\{x_{1} \rightarrow x_{2}\right\}$ means that

Table 4. The database used in the example of the application of equation (20).


$x_{1}$ is the parent of $x_{2}$. Given a model with two variables, there are only three possible belief-network structures-namely, $\left\{x_{1} \rightarrow x_{2}\right\},\left\{x_{2} \rightarrow x_{1}\right\}$, and $\left\{x_{1} \quad x_{2}\right\}$. Thus, by equation (20)

$$
\begin{aligned}
E\left[P\left(x_{2} \mid x_{1}\right) \mid D, \xi\right]= & P\left(x_{2} \mid x_{1}, D,\left\{x_{1} \rightarrow x_{2}\right\}, \xi\right) P\left(\left\{x_{1} \rightarrow x_{2}\right\} \mid D, \xi\right) \\
& +P\left(x_{2} \mid x_{1}, D,\left\{x_{2} \rightarrow x_{1}\right\}, \xi\right) P\left(\left\{x_{2} \rightarrow x_{1}\right\} \mid D, \xi\right) \\
& +P\left(x_{2} \mid x_{1}, D,\left\{x_{1} \quad x_{2}\right\}, \xi\right) P\left(\left\{x_{1} \quad x_{2}\right\} \mid D, \xi\right) \\
= & 0.80 \times 0.33+0.83 \times 0.40+0.71 \times 0.27=0.79
\end{aligned}
$$

where (1) the probabilities $0.80,0.83$, and 0.71 were computed with the three respective belief networks that each contain network conditional probabilities derived using equation (16), and (2) the probabilities $0.33,0.40$, and 0.27 were computed using the methods discussed in section 2.3 .

# 5. Preliminary results 

In this section, we describe an experiment in which we generated a database from a belief network by simulation, and then attempted to reconstruct the belief network from the database. In particular, we applied the K2 algorithm discussed in section 3.1.2 to a database of 10,000 cases generated from the ALARM belief network, which has the structure shown in figure 4. Beinlich constructed the ALARM network as an initial research prototype to model potential anesthesia problems in the operating room (Beinlich et al., 1989). To keep figure 4 uncluttered, we have replaced the node names in ALARM with the numbers shown in the figure. For example, node 20 represents that the patient is receiving insufficient anesthesia or analgesia, node 27 represents an increased release of adrenaline by the patient, node 29 represents an increased patient heart rate, and node 8 represents that the EKG is measuring an increased patient heart rate. When ALARM is given input findingssuch as heart rate measurements-it outputs a probability distribution over a set of possible problems-such as insufficient anesthesia. ALARM represents 8 diagnostic problems, 16 findings, and 13 intermediate variables that connect diagnostic problems to findings. ALARM contains a total of 46 arcs and 37 nodes, and each node has from two to four possible values. Knowledge for constructing ALARM came from Beinlich's reading of the literature and

![img-3.jpeg](img-3.jpeg)

Figure 4. The ALARM belief-network structure, containing 37 nodes and 46 arcs.
from his own experience as an anesthesiologist. It took Beinlich approximately 10 hours to construct the ALARM belief-network structure, and about 20 hours to fill in all the corresponding probability tables.
We generated cases from ALARM by using a Monte Carlo technique developed by Henrion for belief networks (Henrion, 1988). Each case corresponds to a value assignment for each of the 37 variables. The Monte Carlo technique is an unbiased generator of cases, in the sense that the probability that a particular case is generated is equal to the probability of the case existing according to the belief network. We generated 10,000 such cases to create a database that we used as input to the K2 algorithm. We also supplied K2 with an ordering on the 37 nodes that is consistent with the partial order of the nodes as specified by ALARM. Thus, for example, node 21 necessarily appears in the ordering before node 10 , but it is not necessary for node 21 to appear immediately before node 10 in the ordering. Observing this ordering constraint, we manually generated a node order using the ALARM structure. ${ }^{6}$ In particular, we added a node to the node-order list only when all of that node's parents were already in the list. During the process of constructing this node order, we did not consider the meanings of the nodes.
From the 10,000 cases, the K2 algorithm constructed a network identical to the ALARM network, except that the arc from node 12 to node 32 was missing and an arc from node 15 to node 34 was added. A subsequent analysis revealed that the arc from node 12 to node 32 is not strongly supported by the 10,000 cases. The extra arc from node 15 to node 34 was added due to the greedy nature of the K 2 search algorithm. The total search time for the reconstruction was approximately 16 minutes and 38 seconds on a Macintosh II running LightSpeed Pascal, Version 2.0. We analyzed the performance of K2 when given the first $100,200,500,1000,2000$ and 3000 cases from the same 10,000 -case database. The results of applying K2 to these databases are summarized in table 5. Using only 3000 cases, K2 produced the same belief network that it created using the full 10,000 cases.
Although preliminary, these results are encouraging because they demonstrate that K2 can reconstruct a moderately complex belief network rapidly from a set of cases using readily available computer hardware. (For the results of K2 applied to databases from other domains, see (Herskovits, 1991).) We plan to investigate the extent to which the performance

Table 5. The results of applying K2 with subsets of the 10,000 ALARM cases.


of K 2 is sensitive to the ordering of the nodes in ALARM and in other domains. In addition, we plan to explore methods that do not require an ordering.

# 6. Related work 

In sections 2 through 5, we described a Bayesian approach to learning the qualitative and quantitative dependency relationships among a set of discrete variables. For notational simplicity, we shall call the approach BLN (Bayesian learning of belief networks). Many diverse methods for automated learning from data have been developed in fields such as statistics (Glymour, Scheines, Spirtes, \& Kelley, 1987; James, 1985; Johnson \& Wichern, 1982) and AI (Blum, 1982; Carbonell, 1990; Hinton, 1990; Michalski, Carbonell, \& Mitchell, 1983; Michalski, Carbonell, \& Mitchell, 1986). Since it is impractical to survey all these methods, we shall restrict our review to representative methods that we believe are closest to BLN. We group methods into several classes to organize our discussion, but acknowledge that this classification is not absolute and that some methods may cross boundaries.

### 6.1. Methods based on probabilistic-graph models

In this section, we discuss three classes of techniques for constructing probabilistic-graph models from databases.

### 6.1.1. Belief-network methods

Chow and Liu (1968) developed a method that constructs a tree-structured Markov graph, which we shall call simply a tree, from a database of discrete variables. If the data are being generated by an underlying distribution $P$ that can be represented as a tree, then the Chow-Liu algorithm constructs a tree with a probability distribution that converges to $P$ as the size of the database increases. If the data are not generated by a tree, then the algorithm constructs the tree that most closely approximates the underlying distribution $P$ (in the sense of cross-entropy).

A polytree (singly connected network) is a belief network that contains at most one undirected path (i.e., a path that ignores the direction of arcs) between any two nodes in the network. Rebane and Pearl (1987) used the Chow-Liu algorithm as the basis for an algorithm

that recovers polytrees from a probability distribution. In cases where the orientation of an arc cannot be determined from the distribution, an undirected edge is used. In determining the orientation of arcs, the Rebane-Pearl algorithm assumes the availability of a conditional-independence (CI) test-a test that determines categorically whether the following conditional independence relation is true or false: Variables in a set $X$ are independent of variables in a set $Y$, given that the variables in a set $Z$ are instantiated. In degenerate cases, the algorithm may not return the structure of the underlying belief network. In addition, for a probability distribution $P$ that cannot be represented by a polytree, the algorithm is not guaranteed to construct the polytree that most closely approximates $P$ (in the sense of cross-entropy). An algorithm by Geiger, Paz, and Pearl (1990) generalizes the RebanePearl algorithm to recover polytrees by using less restrictive assumptions about the distribution $P$.

Several algorithms have been developed that use a CI test to recover a multiply connected belief network, which is a belief network containing at least one pair of nodes that have at least two undirected paths between them. All such algorithms we describe here run in time that is exponential in the number of nodes in the worst case. Wermuth and Lauritzen (1983) describe a method that takes as input an ordering on all model nodes and then applies a CI test to a distribution to construct a belief network that is a minimal I-map.? Srinivas, Russell, and Agogino (1990) allow the user to specify a weaker set of constraints on the ordering of nodes, and then use a heuristic algorithm to search for a belief network I-map (possibly nonminimal).

Spirtes, Glymour, and Scheines (1990b) developed an algorithm that does not require a node ordering in order to recover multiply connected belief networks. Verma and Pearl (1990) subsequently presented a related algorithm, which we now shall describe. The algorithm first constructs an undirected adjacency graph among the nodes. Then, it orients edges in the graph, when this step is possible given the probability distribution. The method assumes that there is some belief-network structure that can represent all the dependencies and independencies among the variables in the underlying probability distribution that generated the data. There are, however, probability distributions for which this assumption is not valid. Verma and Pearl also introduce a method for detecting the presence of hidden variables, given a distribution over a set of measured variables. They further suggest an information-theoretic measure as the basis for a CI test. The CI test, however, requires determining a number of independence relations that is on the order of $n-2$. Such tests may be unreliable, unless the volume of data is enormous.

Spirtes, Glymour, and Scheines (1991) have developed an algorithm, called PC, that, for graphs with a sparse number of edges, permits reliable testing of independence using a relatively small number of data. PC does not require a node ordering. For dense graphs with limited data, however, the test may be unreliable. For discrete data, the PC algorithm uses a CI test that is based on the chi-square distribution with a fixed alpha level. Spirtes and colleagues applied PC with the 10,000 ALARM cases discussed in section 5. PC reconstructed ALARM, except that three arcs were missing and two extra arcs were added; the algorithm required about 6 minutes of computer time on a DecStation 3100 to perform this task (Spirtes, Glymour, \& Scheines, 1990a).

# 6.1.2. Markov graph methods 

Fung and Crawford (1990) have developed an algorithm called Constructor that constructs an undirected graph by performing a search to find the Markov boundary of each node. The algorithm uses a chi-squared statistic as a CI test. In general, the smaller the Markov boundary of the nodes, the more reliable the CI test statistic. For nodes with large Markov boundaries, the test can be unreliable, unless there is a large number of data. A probability distribution for the resulting undirected graph is estimated from the database. The method of Lauritzen and Spiegelhalter (1988) then is applied to perform probabilistic inference using the undirected graph. An interesting characteristic of Constructor is that it pretunes the CI test statistic. In particular, instead of assuming a fixed alpha level for the test statistic, the algorithm searches for a level that maximizes classification accuracy on a test subset of cases in the database. Constructor has been applied successfully to build a belief network that performs information retrieval (Fung, Crawford, Appelbaum, \& Tong, 1990).

### 6.1.3. Entropy-based methods

In the field of system science, the reconstruction problem focuses on constructing from a database an undirected adjacency graph that captures node dependencies (Pittarelli, 1990). Intuitively, the idea is to find the smallest graph that permits the accurate representation of a given probability distribution. The adequacy of a graph often is determined using entropy as a measure of information content. Since the number of possible graphs typically is enormous, heuristics are necessary to render search tractable. For example, one reconstruction algorithm searches for an adjacency graph by starting with a fully connected graph. The search is terminated when there is no edge that can be removed from the current graph $G_{1}$ to form a graph $G_{2}$, such that the information loss in going from $G_{1}$ and $G_{2}$ is below a set threshold. In this case, $G_{1}$ is output as the dependency graph.

The Kutató algorithm, which is described in (Herskovits, 1991; Herskovits \& Cooper, 1990), shares some similarities with the system-science reconstruction algorithms. In particular, Kutató uses an entropy measure and greedy search to construct a model. One key difference, however, is that Kutató constructs a belief network rather than an undirected graph. The algorithm starts with no arcs and adds arcs until a halting condition is reached. Using the 10,000 cases generated from the ALARM belief network discussed in section 5, Kutató reconstructed ALARM, except that two arcs were missing and two extra arcs were added. The reconstruction required approximately 22.5 hours of computer time on a Macintosh II computer. For a detailed analysis of the relationship between entropy-based algorithms such as Kutató, and Bayesian algorithms such as K2, see (Herskovits, 1991).

An algorithm developed by Cheeseman (1983) and extended by Gevarter (1986) implicitly searches for a model of undirected edges in the form of variable constraints. The algorithm adds constraints incrementally to a growing model. If the maximum-entropy distribution of models containing constraints of order $n+1$ is not significantly different from that of models containing constraints of order $n$, then the search is halted. Otherwise, constraints of order $n+1$ are added until no significant difference exists; then, constraints of order $n+2$ are considered, and so on.

# 6.2. Classification trees 

Another class of algorithms constructs classification trees ${ }^{8}$ from databases (Breiman, Friedman, Olshen, \& Stone, 1984; Buntine, 1990b; Hunt, Marin, \& Stone, 1966; Quinlan, 1986). In its most basic form, a classification tree is a rooted binary tree, where each pair of branches out of a node corresponds to two disjoint values (or value ranges) of a domain variable (attribute). A leaf node corresponds to a classification category or to a probability distribution over the possible categories. We can apply a classification tree by using known attribute values to traverse a path down the tree to a leaf node. In constructing a classification tree, the typical goal is to build the single tree that maximizes expected classification accuracy on new cases. Several criteria, including information-theoretic measures, have been explored for determining how to construct a tree. Typically, a one-step lookahead is used in constructing branch points. In an attempt to avoid overfitting, trees often are pruned by collapsing subtrees into leaves. CART is a well-known method for constructing a classification tree from data (Breiman et al., 1984). CART has been studied in a variety of domains such as signal analysis, medical diagnosis, and mass spectra classification; it has performed well relative to several pattern-recognition methods, including nearestneighbor algorithms (Breiman et al., 1984).

Buntine (1990b) independently has developed methods for learning and using classification trees that are similar to the methods we discuss for belief networks in this paper. In particular, he has developed Bayesian methods for (1) calculating the probability of a classification-tree structure given a database of cases, and (2) computing the expected value of the probability of a classification instance by using many tree structures (called the optiontrees method). Buntine empirically evaluated the classification accuracy of several algorithms on 12 databases from varied domains, including the LED database of Breiman et al. (1984) and the iris database of Fisher. He concluded that "option trees was the only approach that was usually significantly superior to others in accuracy on most data sets" (Buntine, 1990b, page 110 ).

Kwok and Carter (1990) evaluated a simple version of the option-trees method on two databases. In particular, they averaged the classification results of multiple classification trees on a set of problems. The averaging method usually yielded more accurate classification than did any single tree, including the tree generated by Quinlan's ID3 algorithm (Quinlan, 1986). Averaging over as few as three trees yielded significantly improved classification accuracy. In addition, averaging over trees with different structures produced classification more accurate than that produced by averaging over trees with similar structures.

In the remainder of section 6.2 , we present a brief comparison of classification trees and belief networks. For a more detailed discussion, see (Crawford and Fung, 1991). Classification trees can readily handle both discrete and continuous variables. A classification tree is restricted, however, to representing the distribution on one variable of interest-the classification variable. With this constraint, however, classification trees often can represent compactly the attributes that influence the distribution of the classification variable. It is simple and efficient to apply a classification tree to perform classification. For belief networks, there exist approximation and special-case methods for handling continuous variables (Shachter, 1990). Currently, however, the most common way of handling these variables is to discretize them. Belief networks can capture the probabilistic relationships among

multiple variables, without the need to designate a classification variable. These networks provide a natural representation for capturing causal relationships among a set of variables (see (Crawford \& Fung, 1991) for a case study). In addition, inference algorithms exist for computing the probability of any subset of variables conditioned on the values of any other subset. In the worst case, however, these inference algorithms have a computational time complexity that is exponential in the size of the belief network. Nonetheless, for networks that are not densely connected, there exist efficient exact inference algorithms (Henrion, 1990). In representing the relationship between a node and its parents, there are certain types of value-specific conditional independencies that cannot be captured easily in a belief network. In some instances, classification trees can represent these independencies efficiently and naturally. Researchers recently have begun to explore extensions to belief networks that capture this type of independence (Fung \& Shachter, 1991; Geiger and Heckerman, 1991).

# 6.3. Methods that handle hidden variables 

In the general case, discovering belief networks with hidden variables remains an unsolved problem. Nonetheless, researchers have made progress in developing methods for detecting the presence of hidden variables in some situations (Spirtes \& Glymour, 1990; Spirtes et al., 1990b; Verma \& Pearl, 1990). Pearl developed a method for constructing from data a treestructured belief network with hidden variables (Pearl, 1986). Other researchers have developed algorithms that are less sensitive to noise than is Pearl's method, but that still are restricted to tree-structured networks (Golmard \& Mallet, 1989; Liu, Wilkins, Yin, \& Bian, 1990). The Tetrad program is a semiautomated method for discovering causal relationships among continuous variables (Glymour et al., 1987; Glymour \& Spirtes, 1988). Tetrad considers only normal linear models. By making the assumption that linearity holds, the program is able to use an elegant method based on tetrads and partial correlations to introduce likely latent (hidden) variables into causal models; these methods have been evaluated and compared to statistical techniques such as LISREL and EQS (Spirtes, Scheines, \& Glymour, 1990c). Researchers have made little progress, however, in developing general nonparametric methods for discovering hidden variables in multiply connected belief networks.

## 7. Summary and open problems

The BLN approach presented in this paper can represent arbitrary belief-network structures and arbitrary probability distributions on discrete variables. Thus, in terms of its representation, BLN is nearest to the most general probabilistic network approaches discussed in section 6.1 .

The BLN learning methodology, however, is closest to the Bayesian classification-tree method discussed in section 6.2. Like that method, BLN calculates the probability of a structure of variable relationships given a database. The probability of multiple structures can be computed and displayed to the user. Like the option-trees method, BLN also can use multiple structures in performing inference, as discussed in section 4.3. The BLN

approach, however, uses a directed acyclic graph on nodes that represent variables rather than a tree on nodes that represent variable values or value ranges. When the number of domain variables is large, the combinatorics of enumerating all possible belief network structures becomes prohibitive. Developing methods for efficiently locating highly probable structures remains an open area of research.

Except for Bayesian classification trees, the methods discussed in section 6 are nonBayesian. These methods emphasize finding the single most likely structure, which they then may use for inference. They do not, however, quantify the likelihood of that structure. If a single structure is used for inference, implicitly the probability of that structure is assumed to be 1 . Section 6.2 discussed results suggesting that using multiple structures may improve the accuracy of classification inference. Also, the non-Bayesian methods rely on having threshold values for determining when conditional independence holds. BLN does not require the use of such thresholds.

BLN is data-driven by the cases in the database and model-driven by prior probabilities. BLN is able to represent the prior probabilities of belief-network structures. In section 2.1 we suggested the possibility that these probabilities may provide one way to bridge BLN to other AI methods. Prior-probability distributions also can be placed on the conditional probabilities of a particular belief network, as we show in corollaries 1 and 2 in the appendix. If the prior-probability distributions on structures and on conditional probabilities are not available to the computer, then uniform priors may be assumed. Additional methods are needed, however, that facilitate the representation and specification of prior probabilities, particularly priors on belief-network structures.

As we discussed in section 6.3, there has been some progress in developing methods for detecting hidden variables, and in the case of some parametric distributions, for searching for a likely model containing hidden variables. BLN can compute the probability of an arbitrary belief-network structure that contains hidden variables and missing data without assuming a parametric distribution. More specifically, no additional assumptions or heuristics are needed for handling hidden variables and missing data in BLN, beyond the assumptions made in section 2.1 for handling known variables and complete data. Additional research is needed, however, for developing ways to search efficiently the vast space of possible hidden-variable networks to locate the most likely networks.

Although BLN shows promise as a method for learning and inference, there remain numerous open problems, several of which we summarize here. For databases that are generated from a belief network, it is important to prove that, as the number of cases in the database increases, BLN converges to the underlying generating network or to a network that is statistically indistinguishable from the generating network. This result has been proved in the special case that we assume a node order (Herskovits, 1991). Proofs of convergence in the presence of hidden variables also are needed. Related problems are to determine the expected number of cases required to recover a generating network and to determine the variance of $P\left(B_{S} \mid D\right)$. The theoretical and empirical sensitivities of BLN to different types of noisy data need to be investigated as well. Another area of research is Bayesian learning of undirected networks, or, more generally, of mixed directed and undirected networks. Also, recall that the K2 method presented in section 3.1.2 requires an ordering on the nodes. We would like to avoid such a requirement. One approach is to search for likely undirected graphs and to use these as starting points in searching for directed graphs.

Extending BLN to handle continuous variables is another open problem. One approach to this problem is to use Bayesian methods to discretize continuous variables. Finally, regarding evaluation, the results in section 5 are promising, but are limited in scope. Significantly more empirical work is needed to investigate the practicality of the BLN method when applied to databases from different domains.

# Acknowledgments 

We thank Lyn Dupré, Clark Glymour, the anonymous reviewers, and the Editor for helpful comments on earlier drafts. We also thank Ingo Beinlich for allowing us to use the ALARM belief network. The research reported in this paper was performed in part while the authors were in the Section on Medical Informatics at Stanford University. Support was provided by the National Science Foundation under grants IRI-8703710 and IRI-9111590, by the U.S. Army Research Office under grant P-25514-EL, and by the National Library of Medicine under grant LM-04136. Computing resources were provided in part by the SUMEX-AIM resource under grant LM-05208 from the National Library of Medicine.

## Notes

1. Since there is a one-to-one correspondence between a node in $B_{S}$ and a variable in $B_{P}$, we shall use the terms node and variable interchangeably.
2. An instantiated variable is a variable with an assigned value.
3. If hashing is used to store information equivalent to that in an index tree, then it may be possible to obtain a bound tighter than $O\left(m n^{2} r+t_{B_{S}}\right)$ for the average performance. In the worst case, however, due to the collisions of hash keys, an approach that uses hashing may be less efficient than the method described in this section.
4. Binary trees can be used to represent the values of nodes in the index trees we have described. We note, but shall not prove here, that the overall complexity is reduced to $O\left(m n^{2} \lg r+t_{B_{S}}\right)$ if we use such binary trees in computing the values of $N_{i j k}$ and $N_{i j}$.
5. The algorithm is named K2 because it evolved from a system named Kutató (Herskovits \& Cooper, 1990) that applies the same greedy-search heuristics. As we discuss in section 6.1.3, Kutató uses entropy to score network structures.
6. The particular ordering that we used is as follows: 1216171819202122232425262830313712 3410361335153432331114272967895.
7. A belief network $B$ is an $I$-map of a probability distribution $P$ if every CI relation specified by the structure of $B$ corresponds to a CI relation in $P$. Further, $B$ is a minimal $I$-map of $P$ if it is an I-map of $P$ and the removal of any arc from $B$ yields a belief network that is not an I-map of $P$.
8. Classification trees also are known as decision trees, which are different from the decision trees used in decision analysis. To avoid any ambiguity, we shall use the term classification tree.

## Appendix

This appendix includes two theorems and two corollaries that are referenced in the paper. The proofs of the theorems are derived in detail. Although this level of detail lengthens the proofs, it avoids our relying on previous results that may not be familiar to some readers. Thus, the proofs are largely self-contained.

Theorem 1. Let $Z$ be a set of $n$ discrete variables, where a variable $x_{i}$ in $Z$ has $r_{i}$ possible value assignments: $\left(v_{i 1}, \ldots, v_{i r_{i}}\right)$. Let $D$ be a database of $m$ cases, where each case contains a value assignment for each variable in $Z$. Let $B_{S}$ denote a belief-network structure containing just the variables in $Z$. Each variable $x_{i}$ in $B_{S}$ has a set of parents, which we represent with a list of variables $\pi_{i}$. Let $w_{i j}$ denote the $j$ th unique instantiation of $\pi_{i}$ relative to $D$. Suppose there are $q_{i}$ such unique instantiations of $\pi_{i}$. Define $N_{i j k}$ to be the number of cases in $D$ in which variable $x_{i}$ has the value $v_{i k}$ and $\pi_{i}$ is instantiated as $w_{i j}$. Let

$$
N_{i j}=\sum_{k=1}^{r_{i}} N_{i j k}
$$

Suppose the following assumptions hold:

1. The variables in $Z$ are discrete
2. Cases occur independently, given a belief-network model
3. There are no cases that have variables with missing values
4. Before observing $D$, we are indifferent regarding which numerical probabilities to assign to the belief network with structure $B_{S}$.

From these four assumptions, it follows that

$$
P\left(B_{S}, D\right)=P\left(B_{S}\right) \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

Proof. By applying assumptions 1 through 4, we derive a multiple integral over a product of multinomial variables, which we then solve.

The application of assumption 1 yields

$$
P\left(B_{S}, D\right)=\int_{B_{P}} P\left(D \mid B_{S}, B_{P}\right) f\left(B_{P} \mid B_{S}\right) P\left(B_{S}\right) d B_{P}
$$

where $B_{P}$ is a vector whose values denote the conditional-probability assignments associated with belief-network structure $B_{S}$, and $f$ is the conditional-probability-density function over $B_{P}$ given $B_{S}$. The integral is over all possible value assignments to $B_{P}$.

Since $P\left(B_{s}\right)$ is a constant within equation (AI), we can move it outside the integral:

$$
P\left(B_{S}, D\right)=P\left(B_{S}\right) \int_{B_{P}} P\left(D \mid B_{S}, B_{P}\right) f\left(B_{P} \mid B_{S}\right) d B_{P}
$$

It follows from the conditional independence of cases expressed in assumption 2 that equation (A2) can be rewritten as

$$
P\left(B_{S}, D\right)=P\left(B_{S}\right) \int_{B_{P}}\left[\prod_{h=1}^{m} P\left(C_{h} \mid B_{S}, B_{P}\right)\right] f\left(B_{P} \mid B_{S}\right) d B_{P}
$$

where $m$ is the number of cases in $D$, and $C_{h}$ is the $h$ th case in $D$.
We now introduce additional notation to facilitate the application of assumption 3. Let $d_{i h}$ denote the value assignment of variable $i$ in case $h$. For example, for the database in table $1, d_{21}=0$, since $x_{2}=0$ in case 1 . In $B_{S}$, for every variable $x_{i}$, there is a set of parents $\pi_{i}$ (possibly the empty set). For each case in $D$, the variables in the list $\pi_{i}$ are each assigned a particular value. Let $w_{i}$ denote a list of the unique instantiations for the parents of $x_{i}$ as seen in $D$. An element in $w_{i}$ designates a list of values that are assigned to the respective variables in the list $\pi_{i}$. If $x_{i}$ has no parents, then we define $w_{i}$ to be the list $(\emptyset)$, where $\emptyset$ represents the empty set of parents. Although the ordering of the elements in $w_{i}$ is arbitrary, we shall use a list (vector), rather than a set, so that we can refer to members of $w_{i}$ using an index. For example, consider variable $x_{2}$ in $B_{S 1}$, which has the parent list $\pi_{2}=\left\langle x_{1}\right\rangle$. In this example, $w_{2}=((1),(0))$, because there are cases in $D$ where $x_{1}$ has the value 1 and cases where it has the value 0 . Define $w_{i j}$ to be the $j$ th element of $w_{i}$. Thus, for example, $w_{21}$ is equal to (1). Let $\sigma(i, h)$ be an index function, such that the instantiation of $\pi_{i}$ in case $h$ is the $\sigma(i, h)$ th element of $w_{i}$. Thus, for example, $\sigma(2,3)=2$, because in case 3 the parent of variable $x_{2}$-namely, $x_{1}$-is instantiated to the value 0 , which is represented by the second element of $w_{2}$. Therefore, $w_{2, \sigma(2,3)}$ is equal to ( 0 ). Since, according to assumption 3, cases are complete, we can use equation (1) in section 1 to represent the probability of each case; thus, we can expand equation (A3) to become
$P\left(B_{S}, D\right)=P\left(B_{S}\right) \int_{B_{P}}\left[\prod_{h=1}^{m} \prod_{i=1}^{n} P\left(x_{i}=d_{i h} \mid \pi_{i}=w_{i \sigma(i, h)}, B_{P}\right)\right] f\left(B_{P} \mid B_{S}\right) d B_{P}$.
The innermost product of equation (A4) computes the probability of a case in terms of the conditional probabilities of the variables in the case, as defined by belief network $\left(B_{S}, B_{P}\right)$.
By grouping terms, we can rewrite equation (A4) as
$P\left(B_{S}, D\right)=P\left(B_{S}\right) \int_{B_{P}}\left[\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \prod_{k=1}^{r_{i}} P\left(x_{i}=v_{i k} \mid \pi_{i}=w_{i j}, B_{P}\right)^{N_{i j k}}\right] f\left(B_{P} \mid B_{S}\right) d B_{P}$.
Let $\theta_{i j k}$ denote the conditional probability $P\left(x_{i}=v_{i k} \mid \pi_{i}=w_{i j}, B_{P}\right)$. We shall call an assignment of numerical probabilities to $\theta_{i j k}$, for $k=1$ to $r_{i}$, a probability distribution, which we represent as the list $\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$. Note that, since the values of $v_{i k}$, for $k=1$ to $r_{i}$, are mutually exclusive and exhaustive, it follows that $\Sigma_{1 \leq k \leq r_{i}} \theta_{i j k}=1$. In addition, for a given $x_{i}$ and $w_{i j}$, let $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ denote the probability density function over $\left(\theta_{i j 1}\right.$, $\left.\ldots, \theta_{i j r_{i}}\right)$. We call $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ a second-order probability distribution because it is a probability distribution over a probability distribution.
Two assumptions follow from assumption 4:

4a. The distribution $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ is independent of the distribution $f\left(\theta_{i^{\prime} j^{\prime} 1}, \ldots, \theta_{i^{\prime} j^{\prime} r_{i^{\prime}}}\right)$, for $1 \leq i, i^{\prime} \leq n, 1 \leq j \leq q_{i}, 1 \leq j^{\prime} \leq q_{i^{\prime}}$, and $i j \neq i^{\prime} j^{\prime}$;
4b. Distribution $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ is uniform, for $1 \leq i \leq n, 1 \leq j \leq q_{i}$.
Assumption 4a can be expressed equivalently as

$$
f\left(B_{P} \mid B_{S}\right)=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)
$$

Equation (A6) states that our belief about the values of a second-order probability distribution $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ is not influenced by our belief about the values of other second-order probability distributions. That is, the distributions are taken to be independent.
Assumption 4b states that, initially, before we observe database $D$, we are indifferent regarding giving one assignment of values to the conditional probabilities $\theta_{i j 1}, \ldots, \theta_{i j r_{i}}$, versus some other assignment.
By substituting $\theta_{i j k}$ for $P\left(x_{i}=v_{i k} \mid \pi_{i}=w_{i j}, B_{P}\right)$ in equation (A5), and substituting equation (A6) into equation (A5), we obtain
$P\left(B_{S}, D\right)=$

$$
\begin{aligned}
& P\left(B_{S}\right) \int \underset{\theta_{i j k}}{\ldots} \int\left[\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \prod_{k=1}^{r_{i}} \theta_{i j k}^{N_{i j k}}\right]\left[\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)\right] \\
& d \theta_{111}, \ldots, d \theta_{i j k}, \ldots, d \theta_{n q_{n} r_{n}}
\end{aligned}
$$

where the integral is taken over all $\theta_{i j k}$ for $i=1$ to $n, j=1$ to $q_{i}$, and $k=1$ to $r_{i}$, such that $0 \leq \theta_{i j k} \leq 1$, and for every $i$ and $j$ the following condition holds: $\Sigma_{k} \theta_{i j k}=1$. These constraints on the variables of integration apply to all the integrals that follow, but for brevity we will not repeat them.
By using the independence of the terms in equation (A7), we can convert the integral of products in that equation to a product of integrals:

$$
P\left(B_{S}, D\right)=P\left(B_{S}\right) \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \int \underset{\theta_{i j k}}{\ldots} \int\left[\prod_{k=1}^{r_{i}} \theta_{i j k}^{N_{i j k}}\right] f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right) d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}
$$

By Assumption 4b, it follows that $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)=C_{i j}$ for some constant $C_{i j}$. Since $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ is a probability-density function, it necessarily follows that, for a given $i$ and $j$,

$$
\int \underset{\theta_{i j k}}{\ldots} \int C_{i j} d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}=1
$$

We show later in this proof that solving equation (A9) for $C_{i j}$ yields $C_{i j}=\left(r_{i}-1\right)$ !, and, therefore, that $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)=\left(r_{i}-1\right)$ !. Substituting this result into equation (A8), we obtain
$P\left(B_{S}, D\right)=P\left(B_{S}\right) \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \int \underset{\theta_{i j k}}{\ldots} \int\left[\prod_{k=1}^{r_{i}} \theta_{i j k}^{N_{i j k}}\right]\left(r_{i}-1\right)!d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}$.
Since $\left(r_{i}-1\right)$ ! is a constant within the integral in equation (Al0), we can move it outside the integral to obtain

$$
P\left(B_{S}, D\right)=P\left(B_{S}\right) \prod_{i=1}^{n} \prod_{j=1}^{q_{i}}\left(r_{i}-1\right)!\int \underset{\theta_{i j k}}{\ldots} \int \prod_{k=1}^{r_{i}} \theta_{i j k}^{N_{i j k}} d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}
$$

The multiple integral in equation (All) is Dirichlet's integral, and has the following solution (Wilks, 1962):

$$
\int \underset{\theta_{i j k}}{\ldots} \int \prod_{k=1}^{r_{i}} \theta_{i j k}^{N_{i j k}} d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}=\frac{\prod_{k=1}^{r_{i}} N_{i j k}!}{\left(N_{i j}+r_{i}-1\right)!}
$$

Note that, by applying equation (Al2) with $N_{i j k}=0$, and therefore $N_{i j}=0$, we can solve equation (A9), as previously stated, to obtain $C_{i j}=\left(r_{i}-1\right)$ !.

Substituting equation (Al2) into equation (All), we complete the proof:

$$
P\left(B_{S}, D\right)=P\left(B_{S}\right) \prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{k=1}^{r_{i}} N_{i j k}!
$$

Note that the symbol $D$ in theorem 1 represents the cases in the particular order that they were observed. Let $D^{\prime}$ represent the cases without regard to order. By assumption 2, the cases are independent of one another, given some belief network ( $B_{S}, B_{P}$ ). Thus, $P\left(D^{\prime} \mid B_{S}, B_{P}\right)=k P\left(D \mid B_{S}, B_{P}\right)$, where $k$ is the number of unique ways of ordering the cases in $D$, known as the multiplicity. Since $k$ is a constant relative to $D$, by equation (2) in section 1 the ordering of $P\left(B_{S_{i}}, D\right)$ and $P\left(B_{S_{j}}, D\right)$ is the same as the ordering of $P\left(B_{S_{i}}\right.$, $\left.D^{\prime}\right)$ and $P\left(B_{S_{i}}, D^{\prime}\right)$. Furthermore, by Bayes' rule, it is straightforward to show that, if $P\left(D^{\prime} \mid B_{S}, B_{P}\right)=k P\left(D \mid B_{S}, B_{P}\right)$, then $P\left(B_{S_{i}} \mid D\right)=P\left(B_{S_{i}} \mid D^{\prime}\right)$. Thus, in this paper, we consider only the use of $D$.

Assumption 4 in theorem 1 implies that second-order probabilities are uniformly distributed (Assumption 4b), from which we derived that $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)=\left(r_{i}-1\right)$ !. This probability density function is, however, just a special case of the Dirichlet distribution (deGroot, 1970). We can generalize assumption 4 b by representing each $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)$ with a Dirichlet distribution:

$$
f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)=\frac{\left(N_{i j}^{\prime}+r_{i}-1\right)!}{r_{i}} \theta_{i j 1}^{N_{i j 1}^{\prime}} \cdots \theta_{i j r_{i}}^{N_{i j r_{i}}^{\prime}}
$$

where

$$
N_{i j}^{\prime}=\sum_{k=1}^{r_{i}} N_{i j k}^{\prime}
$$

The values we assign to $N_{i j k}^{\prime}$ determine our prior-probability distribution over the values of $\theta_{i j 1}, \ldots, \theta_{i j r_{i}}$. All else being the same, the higher we make a particular $N_{i j k}^{\prime}$, the higher we expect (a priori) the probability $\theta_{i j k}$ to be. As we discussed in section 2.1 , we can view the term $P\left(B_{S}\right)$ as one form of preference bias for belief-network structure $B_{S}$. Likewise, we can view the terms $N_{i j k}^{\prime}$ in equation (A14) as establishing our preference bias for the numerical probabilities to place on a given belief-network structure $B_{S}$. We summarize the result of this generalization of assumption 4 with the following corollary.

Corollary 1. If assumptions 1, 2, 3, and 4a of theorem 1 hold and second-order probabilities are represented using Dirichlet distributions as given by equation (A14), then

$$
P\left(B_{S}, D\right)=P\left(B_{S}\right) \sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \frac{\left(N_{i j}^{\prime}+r_{i}-1\right)!}{\left(N_{i j}+N_{i j}^{\prime}+r_{i}-1\right)!} \sum_{k=1}^{r_{i}} \frac{\left(N_{i j k}+N_{i j k}^{\prime}\right)!}{N_{i j k}^{\prime}!}
$$

Proof. Equation (A15) results when we substitute equation (A14) into equation (A8) and apply the steps in the proof of theorem 1 that follow equation (A8).

Note that when $N_{i j k}^{\prime}=0$, for all possible $i, j$, and $k$, the Dirichlet distribution, given by equation (A14), reduces to the uniform distribution, and equation (A15) reduces to equation (A13), as we would expect.

Theorem 2. Given the four assumptions of theorem 1, it follows that

$$
E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]=\frac{N_{i j k}+1}{N_{i j}+r_{i}}
$$

Proof. This proof will be specific to determining conditional probabilities in belief networks; however, we note that it parallels related results regarding the expected value of probabilities given a Dirichlet distribution (Wilks, 1962). To simplify our notation, we shall use $E\left[\theta_{i j k} \mid D\right]$ to designate $E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]$ in this proof. Also, for brevity, in this proof, we shall leave implicit the following constraints on the variables of integration: all integrals are taken over all $\theta_{i j k}$ for $i=1$ to $n, j=1$ to $q_{i}$, and $k=1$ to $r_{i}$, such that $0 \leq \theta_{i j k} \leq 1$, and for every $i$ and $j$ the condition $\Sigma_{k} \theta_{i j k}=1$ holds.

By the definition of expectation,

$$
E\left[\theta_{i j k} \mid D\right]=\int_{\theta_{i j 1}} \ldots \int_{\theta_{i j r_{i}}} \theta_{i j k} f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}} \mid D\right) d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}
$$

The function $f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}} \mid D\right)$ in equation (A16) is known as the posterior density function, and it can be expressed as

$$
f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}} \mid D\right)=\frac{P\left(D(i, j) \mid \theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right) f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)}{P(D(i, j))}
$$

where $D(i, j)$ denotes the distribution of $x_{i}$ in $D$ for those cases in which the parents of $x_{i}$ have the values designated by $w_{\mathrm{ij}}$. Solving for $P(D(i, j))$ in equation (A17), we obtain

$$
\begin{aligned}
P(D(i, j)) & =\int_{\theta_{i j 1}} \ldots \int_{\theta_{i j r_{i}}} P\left(D(i, j) \mid \theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right) f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right) d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}} \\
& =\int_{\theta_{i j 1}} \ldots \int_{\theta_{i j r_{i}}}\left[\prod_{\kappa=1}^{r_{i}} \theta_{i j \kappa}^{N_{i j \kappa}}\right] f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right) d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}
\end{aligned}
$$

which, when the assumptions and methods in the proof of theorem 1 are applied, yields

$$
P(D(i, j))=\frac{\left(r_{i}-1\right)!}{\left(N_{i j}+r_{i}-1\right)!} \prod_{\kappa=1}^{r_{i}} N_{i j \kappa}!
$$

where we use $\kappa$ as an index variable in the product, since in this theorem $k$ is fixed. Similarly, note that the numerator of equation (A17) can be written as

$$
P\left(D(i, j) \mid \theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right) f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)=\left[\prod_{\kappa=1}^{r_{i}} \theta_{i j \kappa}^{N_{i j \kappa}}\right] f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right)
$$

Substituting equations (A19) and (A20) into equation (A17), and substituting the resulting version of equation (A17) into equation (A16), we obtain

$$
\begin{aligned}
& E\left[\theta_{i j k} \mid D\right]=\frac{\left(N_{i j}+r_{i}-1\right)!}{\left(r_{i}-1\right)!\prod_{\kappa=1}^{r_{i}} N_{i j \kappa}!} \int_{\theta_{i j 1}} \ldots \int_{\theta_{i j r_{i}}} \theta_{i j k}\left[\prod_{\kappa=1}^{r_{i}} \theta_{i j \kappa}^{N_{i j \kappa}}\right] \\
& f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right) d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}
\end{aligned}
$$

$$
\begin{aligned}
& f\left(\theta_{i j 1}, \ldots, \theta_{i j r_{i}}\right) d \theta_{i j 1}, \ldots, d \theta_{i j r_{i}}
\end{aligned}
$$

The multiple integral in equation (A21) can be solved by the methods in the proof of theorem 1 to complete the current proof:

$$
\begin{aligned}
E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]= & \frac{\left(N_{i j}+r_{i}-1\right)!}{\left(r_{i}-1\right)!\prod_{\kappa=1}^{r_{i}} N_{i j \kappa}!} \frac{\left(r_{i}-1\right)!N_{i j 1}!\ldots\left(N_{i j k}+1\right)!\ldots N_{i j r_{i}}!}{\left(N_{i j}+r_{i}\right)!} \\
& =\frac{N_{i j k}+1}{N_{i j}+r_{i}}
\end{aligned}
$$

where, in the left-hand side of this equation, we have expanded our previous shorthand for the expectation.

Just as corollary 1 generalizes theorem 1, in the following corollary we generalize theorem 2 by permitting second-order probability distributions to be expressed as Dirichlet distributions.

Corollary 2. If assumptions 1, 2, 3, and 4a of theorem 1 hold and second-order probabilities are represented using Dirichlet distributions as given by equation (Al4), then

$$
E\left[\theta_{i j k} \mid D, B_{S}, \xi\right]=\frac{N_{i j k}+N_{i j k}^{\prime}+1}{N_{i j}+N_{i j}^{\prime}+r_{i}}
$$

Proof. Equation (A22) results when we substitute equation (Al4) into equations (Al7) and (Al8), and apply the steps in the proof of theorem 2 that follow equation (Al7).
