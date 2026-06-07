# Towards Efficient Local Causal Structure Learning 

Shuai Yang, Hao Wang, Kui Yu*, Fuyuan Cao, and Xindong Wu


#### Abstract

Local causal structure learning aims to discover and distinguish direct causes (parents) and direct effects (children) of a variable of interest from data. While emerging successes have been made, existing methods need to search a large space to distinguish direct causes from direct effects of a target variable $T$. To tackle this issue, we propose a novel Efficient Local Causal Structure learning algorithm, named ELCS. Specifically, we first propose the concept of N -structures, then design an efficient Markov Blanket (MB) discovery subroutine to integrate MB learning with N -structures to learn the MB of $T$ and simultaneously distinguish direct causes from direct effects of $T$. With the proposed MB subroutine, ELCS starts from the target variable, sequentially finds MBs of variables connected to the target variable and simultaneously constructs local causal structures over MBs until the direct causes and direct effects of the target variable have been distinguished. Using eight Bayesian networks the extensive experiments have validated that ELCS achieves better accuracy and efficiency than the state-of-the-art algorithms.


Index Terms-Bayesian network, Markov Blanket, Local causal structure learning.

## 1 INTRODUCTION

CauSal discovery has always been an important goal in many scientific fields, such as medicine, computer science and bioinformatics [1], [2], [3], [4]. There has been a great deal of recent interest in discovering causal relationships between variables, since it is not only helpful to reveal the underlying data generating mechanism, but also to improve classification and prediction performance in both static and non-static environments [5]. However, in many real-world scenarios, it is difficult to discover causal relationships between variables since true causality can only be identified using controlled experimentation [6].

Statistical approaches are useful in generating testable causal hypotheses which can accelerate the causal discovery process [7]. Learning a Bayesian network (BN) from observational data is the popular method for causal structure learning and causal inference. The structure of a BN takes the form of a directed acyclic graph (DAG) in which nodes of the DAG represent the variables and edges represent dependence between variables. A DAG implies causal concepts, since they code potential causal relationships between variables: the existence of a directed edge $X \rightarrow Y$ means that $X$ is a direct cause of $Y$, and the absence of a directed edge $X \rightarrow Y$ means that $X$ cannot be a direct cause of $Y$ [8]. When a directed edge $X \rightarrow Y$ in a BN indicates that $X$ is a direct cause of $Y$, in this case, the BN is known as a causal Bayesian network. Given a set of conditional dependencies from observational data and a corresponding DAG model, we can infer

- S. Yang, H. Wang and K. Yu are with the Key Laboratory of Knowledge Engineering With Big Data of Ministry of Education, Hefei University of Technology, China, also with the School of Computer Science and Information Engineering, Hefei University of Technology, Hefei 230601, China. E-mail: yangy@mail.hfut.edu.cn; \{jxjswangh, yukui\}@hfut.edu.cn.
- F. Cao is with the School of Computer and Information Technology, Shanxi University, Taiyuan 030006, China. E-mail: cfy@sxu.edu.cn.
- X. Wu is with the Key Laboratory of Knowledge Engineering With Big Data of Ministry of Education, Hefei University of Technology, Hefei 230601, China, also with Mininglamp Academy of Sciences, Mininglamp Technology, Beijing, 100102, China. E-mail: wuxindong@mininglamp.com.
Manuscript received month day, year; revised month day, year. (*Corresponding author: Kui Yu.)
a causal Bayesian network using intervention calculus [9]. Then learning BN structures (i.e. DAGs) from observational data is the most important step for causal structure learning.

In recent years, many causal structure learning (i.e. DAG learning) methods have been designed [10], which can be roughly divided into global causal structure learning and local causal structure learning. The first type of methods aims to learn the casual structure of all variables, such as MMHC [11], NOTEARS [12] and DAG-GNN [13]. However, in many practical scenarios, it is not necessary to waste time to learn a global structure when we are only interested in the causal relationships around a given variable. To tackle this issue, the second type of methods is proposed, with the aim to discover and distinguish the direct causes (parents) and direct effects (children) of a target variable, such as PCD-by-PCD [14] and CMB [15].

PCD-by-PCD (PCD means Parents, Children and some Descendants) [14] and CMB (Causal Markov Blanket) [15] first learn the PCD or MB (Markov Blanket) of a target variable and construct a local structure among the target variable and the variables in the PCD or MB, then sequentially learn PCDs or MBs of the variables connected to the target variable and simultaneously construct local structures among variables in PCDs or MBs until the parents and children of the target variable have been distinguished.

While emerging successes have been made, existing local causal structure learning methods suffer from the following limitations. They need to search a large space to distinguish parents from children of a target variable. That is to say, existing local causal structure learning methods not only need to learn the PCD or MB of the target variable, but also may need to learn PCDs or MBs of the variables connected to the target variable. In the worst case (e.g. the target variable has all single ancestors) all existing methods may be required to learn PCDs or MBs of all variables in a dataset. This leads to that existing local causal structure learning methods are often computationally expensive or even infeasible especially with a large-sized BN. For instance, as shown in Fig. 1, there is an N-structure (see Definition 9) formed

![img-0.jpeg](img-0.jpeg)

Fig. 1. A sample Bayesian network. The MB of $T$ includes $E$ and $J$ (parents), $A, B, L$ and $K$ (children), $C$ and $D$ (spouses).
by four variables $T, A, B$, and $C$. Given the target variable $T$, in order to determine the causal relationship between $T$ and $B$ : PCD-by-PCD is required to learn the PCD of $T$ and PCDs of $A$ and $B$. For CMB, if only the MB of $T$ is learnt, the edge direction between $T$ and $B$ cannot be determined since there is no V -structures around B. CMB needs to further learn the MBs of $B$ and $A$ to orient the edge between $T$ and $B$. In a word, both PCD-by-PCD and CMB need to search a large space to determine the edge direction between $T$ and $B$. A larger search space will result in performing more conditionally independence (CI) tests for discovering the causal relationships around a given variable. More CI tests not only increase computational time, but also lead to more unreliable tests. It will be beneficial to local causal structure learning if the edge direction between $B$ and $T$ can be determined in learning the PCD or MB of the target variable $T$ without learning PCDs or MBs of the other variables.

Then a question naturally arises: can we reduce the search space in determining the edge directions between a given variable and its children to speed up the local causal structure learning? To address this problem, our main contributions of the paper are summarized as follows.

- We propose the concept of N -structures, a special local structure for edge directions in local causal structure learning. Then we propose a new local causal structure learning, called ELCS. Through leveraging the N -structures, ELCS learns the MBs of the variables as few as possible to distinguish parents from children of a given variable as many as possible, which improves the efficiency of local causal structure learning and simultaneously reduces the impact of unreliable CI tests.
- To integrate MB learning with N -structures to infer edge directions as many as possible during the MB learning procedure, we design an efficient MB discovery subroutine (EMB) and its efficient version EMB-II. EMB not only is able to learn the MB of a variable, but also has an ability to distinguish parents from children of the variable.
- We have conducted extensive experiments on eight benchmark BNs, and have compared ELCS with five existing causal structure learning algorithms, including three state-of-the-art global structure learning and two local structure learning algorithms, to demonstrate the effectiveness and efficiency of the ELCS algorithm.
The remainder of this paper is organized as follows. Section

2 reviews the related work, and Section 3 gives the notations and definitions. Section 4 describes the proposed ELCS algorithm in detail. Section 5 reports and discusses the experimental results. Section 6 summarizes the paper.

## 2 Related Work

Our work focuses on local causal structure learning and is also related to MB learning and global causal structure learning. So this section briefly introduces the related work in the three areas.

MB learning. Learning Markov Blanket (MB) plays an essential part in the skeleton learning during BN structure learning. Existing MB learning methods can be categorized into two types: constraint-based methods and score-based methods. The former employs independence tests to find the MB of a given variable [16], [17], whereas the latter learns the MB using score-based BN structure learning algorithms [18], [19].

Constraint-based methods can be roughly grouped into simultaneous MB learning and divide-and-conquer MB learning. Given the target variable $T$, the simultaneous MB learning algorithm aims to learn parents, children, and spouses of $T$ simultaneously, and does not distinguish spouses of $T$ from its PC, such as GSMB [20], IAMB [21], Inter-IAMB [22] and Fast-IAMB [23]. To reduce the sample requirement of the simultaneous MB learning algorithm, the divide-and-conquer MB learning algorithm is proposed, with the aim to find PC and spouses of the target variable separately. The representative divide-and-conquer MB learning algorithms include CCMB [16], BAMB [17], MMMB [24], HITON-MB [25], PCMB [26] and STMB [27]. Recently, a comprehensive review of the state-of-the-art MB learning algorithms are discussed in [28].

However, existing MB learning methods only learn a local skeleton around a target variable and do not distinguish parents from children in the learnt MB of a target variable.

Global causal structure learning. A large amount of methods have been designed for global causal structure learning. Recent methods can be roughly categorized into two types: local-to-global structure learning methods and continuous optimization based learning methods. The local-to-global structure learning approach, such as MMHC [11], SSL $\pm$ C/G [18] and GSBN [29], first learns the MB or PC of each variable, then constructs a skeleton of a DAG using the learnt MBs or PCs, and finally orients edges of the learnt skeleton using score-based or constraint-based causal learning algorithms. Instead of learning the MB of each variable first, GGSL [30] starts with a randomly selected variable, and then uses a score-based MB learning algorithm to gradually expand the learnt structure through a series of local structure learning steps. Based on GGSL, a parallel BN structure learning algorithm (PSL) is designed to improve the efficiency [31].

Recently, several continuous optimization based learning approaches have been proposed for global causal structure learning [12], [13], [32], [33]. Zheng et al. consider a BN structure learning problem as a purely continuous optimization problem and propose the NOTEARS algorithm [12]. DAG-GNN uses a graph neural network based deep generative model to capture the complex data distribution to learn BN structures [13]. RLBIC uses reinforcement learning to search for a directed acyclic graph (DAG) with the best score [32]. Zhang et al. propose a DAG variational autoencoder (D-VAE) for BN structure learning [33].

However, global causal structure learning methods are time consuming or even infeasible when the number of variables of a BN is large. In fact, in many practical settings, we are only

TABLE 1
Summary of Notations


interested in distinguishing parents from children of a variable of interest. In this case, it is unnecessary and wasteful to find an entire BN structure.

Local causal structure learning. Local causal structure learning aims to learn and distinguish the parents and children of a target variable. Although many algorithms have been designed for learning a whole structure, only several algorithms have been proposed for local causal structure learning. PCD-by-PCD first discovers the PCD of a target variable, then sequentially discovers PCDs of the variables connected to the target variable and simultaneously finds V-structures and orients the edges connected to the target variable until all the parents and children of the target variable are identified [14]. CMB first learns the MB of a target variable using HITON-MB and orients edges by tracking the conditional independence changes in the MB of the target variable, then sequentially learns MBs of the variables connected to the target variable and simultaneously construct local structures along the paths starting from the target variable until the parents and children of the target variable have been identified or they cannot be identified further by continuing the process [15].

As we discussed in Section 1, both PCD-by-PCD and CMB encounter the time inefficient problem since they need to learn a large number of PCDs or MBs of the variables for distinguishing parents from children of a target variable. To tackle this issue, in this paper, we aim to develop a new method through learning the MBs of variables as few as possible while orienting edges as many as possible.

## 3 Notations and Definitions

In this section, we will briefly introduce some basic definitions and notations frequently used in this paper (see Table 1 for a summary of the notations). Let $\boldsymbol{U}$ denote a set of random variables. $\mathbb{P}$ represents a joint probability distribution over $\boldsymbol{U}$, and $\mathbb{G}$ is a DAG over $\boldsymbol{U}$. In a DAG, $X$ is a parent of $Y$ and $Y$ is a child of $X$ if there exists a directed edge from $X$ to $Y . X$ is an ancestor of $Y$ (i.e., non-descendant of $Y$ ) and $Y$ is a descendant of $X$ if there exists a directed path from $X$ to $Y$.

Definition 1 (Conditional Independence [34]). Given a conditioning set $\boldsymbol{Z}, X$ is conditionally independent of $Y$ if and only if $P(X \mid Y, \mathbf{Z})=P(X \mid \mathbf{Z})$.

Definition 2 (Bayesian Network [34]). The triplet $<\boldsymbol{U}, \mathbb{G}, \mathbb{P}>$ is called a Bayesian network (BN) if $<\boldsymbol{U}, \mathbb{G}, \mathbb{P}>$ satisfies the Markov condition: each variable is conditionally independent of variables in its non-descendant given its parents in $\mathbb{G}$.

Definition 3 (Casual Bayesian Network [9]). A BN is called a causal Bayesian network ( $C B N$ ) if a directed edge in $\mathbb{G}$ has causal interpretation, that is, $X \rightarrow Y$ indicates that $X$ is a direct cause of $Y$.

Definition 4 (Causal Structure Learning). Global causal structure learning aims to learn a DAG over $\boldsymbol{U}$ from observational data, where edges represent potential causal relationships between variables, that is, $X$ is a direct cause of $Y$ if there exists a directed edge from $X$ to $Y$ [9]. Local causal structure learning aims to discover and distinguish direct causes and direct effects of a variable of interest [15].

Definition 5 (V-structure [34]). If there is no an edge between $X$ and $Y$, and $Z$ has two incoming edges from $X$ and $Y$, respectively, then $X, Z$ and $Y$ form a V-structure $(X \rightarrow Z \leftarrow Y)$.

In a BN, $Z$ is a collider if there are two directed edges from $X$ to $Z$ and from $Y$ to $Z$, respectively. V-structures play an important role in determining the edge directions between variables. For example, if there is a V-structure $(X \rightarrow Z \leftarrow Y)$ formed by $X, Y$ and $Z$, we can identify $X$ and $Y$ as parents of $Z$ using conditional independence (CI) tests.

Definition 6 (D-separation [34]). Given a set $\boldsymbol{S} \subseteq \boldsymbol{U} \backslash\{X, Y\}$, a path $\pi$ between $X$ and $Y$ is blocked, if one of the following conditions is satisfied: 1) there is a non-collider variable within $\boldsymbol{S}$ on $\pi$, or 2) there is a collier variable $Z$ on $\pi$, while $Z$ and any its descendants are not in $\boldsymbol{S}$. Otherwise, $\pi$ between $X$ and $Y$ is unblocked. $X$ and $Y$ are d-separation given $\boldsymbol{S}$ if and only if each path between $X$ and $Y$ is blocked by $\boldsymbol{S}$.

In a DAG, given a conditioning set, we can determine whether two variables are conditionally independent using Definition 6.

Definition 7 (Faithfulness [35]). Given a $B N<\boldsymbol{U}, \mathbb{G}, \mathbb{P}>, \mathbb{G}$ is faithful to $\mathbb{P}$ if and only if all the conditional independencies appear in $\mathbb{P}$ are entailed by $\mathbb{G} . \mathbb{P}$ is faithful if and only if there is a DAG $\mathbb{G}$ such that $\mathbb{G}$ is faithful to $\mathbb{P}$.

Definition 7 indicates that in a faithful BN, if $X$ and $Y$ are d-separated given the conditioning set $\boldsymbol{S}$ in $\mathbb{G}$, then they will be conditionally independent given $\boldsymbol{S}$ in $\mathbb{P}$.

Definition 8 (Markov Blanket [34]). In a faithful $B N$, the $M B$ of a target variable $T$ is denoted as $\boldsymbol{M B}_{T}$, which is uniqueness and consists of parents, children and spouses (other parents of the target's children) of T. All other variables in $\boldsymbol{U} \backslash \boldsymbol{M B}_{T} \backslash\{T\}$ are conditionally independent of $T$ given $\boldsymbol{M B}_{T}, \forall X \subseteq \boldsymbol{U} \backslash \boldsymbol{M B}_{T} \backslash\{T\}$, $X \Perp T \mid \boldsymbol{M B}_{T}$, where $X \Perp T \mid \boldsymbol{M B}_{T}$ denotes $X$ and $T$ are conditionally independent conditioning on $\boldsymbol{M B}_{T}$.

Definition 9 (N-structure). In a faithful $B N$, if there exists four variables $T, A, B$ and $C$, and $T$ is a parent of $A$ and $B, C$ is a parent of $A$, there is no an edge between $C$ and $T, A$ is an ancestor of $B$, the other parents of $B$ are in $P C$ set of $T$. Then, the local structure formed by the four variables is called an $N$-structure.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Examples of N -structures.

Fig. 2 gives examples of the N -structures. In Fig. 2 (a), there is an N -structure formed by $T, A, B$ and $C$. In Fig. 2 (b), variables $T, A, B$ and $C$ construct an N -structure, and variables $T, A, E$ and $C$ construct an N -structure. Given the target variable $T$, we can leverage the N -structures to determine edge directions between $T$ and its children (i.e. $B$ and $E$ ) during learning the MB of $T$ without learning MBs of the other variables.

Theorem 1 [35]. In a faithful $B N$, for any two variables $X \in \boldsymbol{U}$ and $Y \in \boldsymbol{U}$, if there exists an edge between $X$ and $Y$, then $\forall \boldsymbol{S} \subseteq \boldsymbol{U}$ $\backslash\{X, Y\}, X \not \subseteq Y \mid \boldsymbol{S}$ holds.

Theorem 1 demonstrates that if $X$ is a parent (or a child) of $Y$ if $X$ and $Y$ are not conditionally independent conditioning any subsets excluding $X$ and $Y$.

## 4 The Proposed Method

### 4.1 The ELCS Algorithm

We propose the Efficient Local Causal Structure learning algorithm (ELCS) to distinguish parents from children of a target variable, as shown in Algorithm 1. ELCS starts from the target variable, sequentially finds MBs of variables connected to the target variable and simultaneously constructs local causal structures over MBs until all the parents and children of the target variable have been distinguished or it is clear that they cannot be further distinguished by continuing the process. In the following, we first summarize the main idea of ELCS, then give the details of ELCS.

To improve the efficiency of local causal structure learning, in ELCS, we propose the following two acceleration strategies. First, ELCS finds the N -structures, and then leverages those found N -structures to infer edge directions between the target variable $T$ and its children during learning the MB of $T$. Second, two rules in Lemma 1 are used to further infer edge directions between $T$ and its PC during learning the MB of $T$.

As described in Algorithm 1, given the target variable $T$, ELCS first initializes the variable set $\boldsymbol{W}$ and the queue $Q u e$ to empty sets (line 1 in Algorithm 1), where $\boldsymbol{W}$ is used to store variables that their MBs have been learnt, and Que is utilized to store variables that their MBs need to be learnt in next phase. Then, $T$ enters Que (line 2 in Algorithm 1). Next, lines 4-13 in Algorithm 1 will be executed. At line 4 in Algorithm 1, the header element in Que is out of queue, that is, $X=T$. Since the MB of $T$ has not been learnt, $T$ is added to the set $\boldsymbol{W}$ (lines 5-6 in Algorithm 1). The EMB (Efficient Markov Blanket discovery) subroutine is executed to learn the MB of $T$ (line 7 in Algorithm 1). Given a variable $X$, the EMB subroutine not only is able to find the PC $\left(\boldsymbol{P} \boldsymbol{C}_{X}\right)$ and MB $\left(\boldsymbol{S P}_{X} \cup \boldsymbol{P} \boldsymbol{C}_{X}\right)$, but also has an ability to distinguish parents from children of $X$. The details of EMB are described

```
Algorithm 1: ELCS
    Input: Data \(D\), target variable \(T\), random variables set \(\boldsymbol{U}\)
    Output: \(\boldsymbol{P}_{T}, \boldsymbol{C}_{T}, \boldsymbol{U} \boldsymbol{N}_{T}\)
    \(W \leftarrow \emptyset, Q u e=\emptyset\)
    Que.push \((T)\)
    Repeat
        \(X=\) Que.pop( )
        if \(X \notin W\) then
            \(W \leftarrow W \cup\{X\}\)
            \(\left[\boldsymbol{P}_{X}, \boldsymbol{C}_{X}, \boldsymbol{U} \boldsymbol{N}_{X}, \boldsymbol{S P}_{X}, \boldsymbol{P} \boldsymbol{C}_{X}\right]=\operatorname{EMB}(D, X)\)
            Orienting edge directions between \(X\) and its PC nodes
            according to \(\boldsymbol{P}_{X}\) and \(\boldsymbol{C}_{X}\)
            for each \(Y \in \boldsymbol{U} \boldsymbol{N}_{X}\) do
                Que.push \((Y)\)
            end for
        end if
        Using Meek rules to orient other edge directions between
            variables in \(\boldsymbol{W}\)
    Until (1) all parents and children of \(T\) can be determined, or
        (2) Que \(=\emptyset\), or (3) \(W=U\)
Algorithm 2: EMB
    Input: Data \(D\), target variable \(T\)
    Output: \(\boldsymbol{P}_{T}, \boldsymbol{C}_{T}, \boldsymbol{U} \boldsymbol{N}_{T}, \boldsymbol{S} \boldsymbol{P}_{T}, \boldsymbol{P} \boldsymbol{C}_{T}\)
        \#Step 1: find the \(P C\) set of \(T^{\star}\)
        \(\left[\boldsymbol{P C}_{T}, \boldsymbol{S e p}_{T}\right] \leftarrow \operatorname{RecogPC}(T, D)\)
        \#Step 2: find spouses of \(T^{\star}\)
        \(\left[\boldsymbol{S P}_{T}, \boldsymbol{C S P}_{T}\right] \leftarrow \operatorname{RecogSpouses}\left(D, T, \boldsymbol{P C}_{T}, \boldsymbol{S e p}_{T}\right)\)
        \#Step 3: remove false positive \(P C\) from \(\boldsymbol{P C}_{T}{ }^{\star}\)
        for each \(Y \in \boldsymbol{P C}_{T}\) do
            if \(T \Perp Y \mid \boldsymbol{Z}, \boldsymbol{Z} \subseteq \boldsymbol{S P}_{T}\{Y\} \cup \boldsymbol{P C}_{T} \backslash\{Y\}\) then
            \(\boldsymbol{P C}_{T} \leftarrow \boldsymbol{P C}_{T} \backslash\{Y\}\)
            \(\boldsymbol{S P}_{T}\{Y\} \leftarrow \emptyset\)
        end if
    end for
        \#Step 4: find \(\boldsymbol{P}_{T}, \boldsymbol{C}_{T}{ }^{\star}\)
    \(\left[\boldsymbol{P}_{T}, \boldsymbol{C}_{T}, \boldsymbol{U} \boldsymbol{N}_{T}\right] \leftarrow\) DistinguishPC \(\left(D, T, \boldsymbol{P C}_{T}, \boldsymbol{S P}_{T}, \boldsymbol{C S P}_{T}\right)\)
```

in Section 4.2. Let $\boldsymbol{P}_{X}$ represent a set of the identified parents of $X . \boldsymbol{C}_{X}$ denotes a set of the identified children of $X$. The set containing undistinguished PC variables of $X$ is denoted as $\boldsymbol{U} \boldsymbol{N}_{X}$. After executing the line 7 in Algorithm 1, the sets of $\boldsymbol{P}_{T}, \boldsymbol{C}_{T}$, $\boldsymbol{U} \boldsymbol{N}_{T}, \boldsymbol{S P}_{T}, \boldsymbol{P C}_{T}$ are obtained. If $\boldsymbol{U} \boldsymbol{N}_{T}$ is empty, that is, parents and children of $T$ are all distinguished, the learning process will be terminated. Otherwise, the undistinguished variables within $\boldsymbol{U} \boldsymbol{N}_{T}$ will be put in Que (lines 9-11 in Algorithm 1). Then, Meek rules [36] are used to orient other edge directions between variables in $\boldsymbol{W}$ (line 13 in Algorithm 1). Lines 4-13 in Algorithm 1 will be repeated until all the parents and children of $T$ have been distinguished or Que is empty or the size of $\boldsymbol{W}$ equals to that of the entire variable set.

### 4.2 EMB Subroutine

ELCS depends on the MB learning methods for local causal structure learning, but existing MB learning algorithms have the following shortcomings. First, existing MB learning methods cannot be directly combined with the N -structures to infer edge directions between the target variable and its children. Second, existing MB learning methods only focus on learning the MB of the target variable and are not able to distinguish parents from children. Third, existing MB learning methods may be computationally expensive. In order to help ELCS to leverage N structures and the rules in Lemma 1 for efficiently learning local causal structures, we design an Effective MB discovery subroutine

Algorithm 3: RecogSpouses
Input: Data $D$, target variable $T, \boldsymbol{P C}_{T}, \boldsymbol{S e p}_{T}$
Output: $\quad \boldsymbol{S P}_{T}, \boldsymbol{C S P}_{T}$
1: $\boldsymbol{S P}_{T} \leftarrow \emptyset$
2: for each $X \in \boldsymbol{U} \backslash\{T\} \backslash \boldsymbol{P C}_{T}$ do
3: $\quad$ Temp $\leftarrow \emptyset$
4: for each $Y \in \boldsymbol{P C}_{T}$ do
5: $\quad$ if $X \Perp Y \mid \emptyset$ then
6: $\quad$ Temp $\leftarrow$ Temp $\cup\{Y\}$
7: end if
8: end for
9: if $X \Perp T \mid$ Temp then
10: for each $Y \in$ Temp do
11: $\quad$ if $X \Perp T \mid\{Y\} \cup \boldsymbol{S e p}_{T}\{X\}$ then
12: $\quad \boldsymbol{C S P}_{T}\{Y\} \leftarrow \boldsymbol{C S P}_{T}\{Y\} \cup\{X\}$
13: end if
14: end for
15: end if
16: end for
17: $\boldsymbol{S P}_{T} \leftarrow \boldsymbol{C S P}_{T}$
18: for each $Y \in \boldsymbol{P C}_{T}$ do
19: for each $X \in \boldsymbol{S P}_{T}\{Y\}$ do
20: $\quad$ if $X \Perp Y \mid \boldsymbol{Z}, \boldsymbol{Z} \subseteq \boldsymbol{S P}_{T}\{Y\} \cup\{T\} \cup \boldsymbol{P C}_{T} \backslash\{X, Y\}$ then
21: $\quad \boldsymbol{S P}_{T}\{Y\} \leftarrow \boldsymbol{S P}_{T}\{Y\} \backslash\{X\}$
22: end if
23: end for
24: end for

```
Algorithm 4: DistinguishPC
    Input: Data \(D\), target variable \(T, \boldsymbol{P C}_{T}, \boldsymbol{S P}_{T}, \boldsymbol{C S P}_{T}\)
    Output: \(\quad \boldsymbol{P}_{T}, \boldsymbol{C}_{T}, \boldsymbol{U N}_{T}\)
    : \(\boldsymbol{C}_{T} \leftarrow \emptyset, \boldsymbol{P}_{T} \leftarrow \emptyset\)
    : for each \(Y \in \boldsymbol{P C}_{T}\) do
        if \(\boldsymbol{S P}_{T}\{Y\}\) is nonempty then
            \(\boldsymbol{C}_{T} \leftarrow \boldsymbol{C}_{T} \cup\{Y\}\)
        end if
    end for
    \(U N_{T} \leftarrow \boldsymbol{P C}_{T} \backslash \boldsymbol{C}_{T}\)
    for each \(X \in U N_{T}\) do
        if \(\boldsymbol{C S P}_{T}\{X\} \cap \boldsymbol{C}_{T}\) is nonempty then
            \(\boldsymbol{C}_{T} \leftarrow \boldsymbol{C}_{T} \cup\{X\}\)
        end if
    end for
    for each \(X \in \boldsymbol{P C}_{T} \backslash \boldsymbol{C}_{T}\) do
        for each \(Y \in \boldsymbol{P C}_{T} \backslash \boldsymbol{C}_{T}\) do
            if \(X \Perp Y \mid \emptyset\) and \(X \Perp Y \mid T\) then
                \(\boldsymbol{P}_{T} \leftarrow \boldsymbol{P}_{T} \cup\{X\} \cup\{Y\}\)
            end if
        end for
    end for
    \(U N_{T} \leftarrow \boldsymbol{P C}_{T} \backslash \boldsymbol{P}_{T} \backslash \boldsymbol{C}_{T}\)
    for each \(X \in U N_{T}\) do
        for each \(Y \in \boldsymbol{P}_{T}\) do
            if \(X \Perp Y \mid \emptyset\) and \(X \Perp Y \mid T\) then
                \(\boldsymbol{C}_{T} \leftarrow \boldsymbol{C}_{T} \cup\{X\}\)
            break
            end if
        end for
    end for
    \(U N_{T} \leftarrow \boldsymbol{P C}_{T} \backslash \boldsymbol{P}_{T} \backslash \boldsymbol{C}_{T}\)
```

(EMB) to learn the MB of a target variable and distinguish parents from children of the target variable simultaneously.

As shown in Algorithm 2, EMB consists of four steps as follows. Given a target variable $T$, EMB first learns the PC of $T\left(\boldsymbol{P C}_{T}\right)$ using an existing PC learning algorithm. Second, EMB obtains spouses of $T$ using a RecogSpouses subroutine. Then, EMB removes false PC from $\boldsymbol{P C}_{T}$. Finally, EMB orients edges between $T$ and its PC as many as possible using a DistinguishPC subroutine. Specifically, to find the N-structures, EMB first determines which variable within $\boldsymbol{U} \backslash\{T\} \backslash \boldsymbol{P C}_{T}$ is a candidate spouse
of $T$, and obtains the candidate spouse set $\boldsymbol{C S P}_{T}\{Y\}$ of each variable $Y$ within $\boldsymbol{P C}_{T}$, and then obtains the spouses of $T$. Based on the learnt $\boldsymbol{C S P}_{T}\{Y\}$ and spouses, we can find the N -structures. Through leveraging the found N -structures, EMB can distinguish some children of $T$ with regard to the found N -structures. In addition, two rules in Lemma 1 are used in the DistinguishPC subroutine to further distinguish parents from children of $T$. In the following, we will give the details of these four steps.

Lemma 1. The PC (parents and children) set of a given variable $T(T \in \boldsymbol{U})$ is denoted as $\boldsymbol{P C}_{T}$. Let $X \in \boldsymbol{P C}_{T}, Y \in \boldsymbol{P C}_{T}$. We can get the following two dependence relationships between $X$ and $Y$.
(a) $X \Perp Y \mid \emptyset$ and $X \Perp Y \mid T \Rightarrow X$ and $Y$ are both parents of $T$. This shows that there is a $V$-structure $(X \rightarrow T \leftarrow Y)$ formed by variables $X, Y$ and $T$, and $T$ is a collider.
(b) $X$ is a direct cause of $T, X \Perp Y \mid \emptyset$ and $X \Perp Y \mid T \Rightarrow$ $Y$ is a direct effects of $T$. This shows that there is only one path $(X \rightarrow T \rightarrow Y)$ from $X$ to $Y$, and the path is blocked by $T$.

Step 1 (line 1 in Algorithm 2): EMB obtains $\boldsymbol{P C}_{T}$ and $\boldsymbol{S e p}_{T}$ of a target variable $T$ by utilizing an existing PC learning algorithm, where $\boldsymbol{S e p}_{T}$ is a set that contains the sets $\boldsymbol{S e p}_{T}\{\cdot\}$ of all variables. In this paper, we use HITON-PC [25] to find the PC of $T$ (any other state-of-the-art PC learning algorithms can be used here to instantiate the RecogPC() function at Step 1 in Algorithm 2).

Step 2 (line 2 in Algorithm 2): At this step, EMB learns spouses of $T$. We design a RecogSpouses subroutine for learning spouses. The details of RecogSpouses are described in Algorithm 3. RecogSpouses first finds candidate spouses from all variables within $\boldsymbol{U} \backslash\{T\} \backslash \boldsymbol{P C _ { T }}$ that are conditionally independent of $T$. If $X$ and $T$ are conditionally independence, then we construct a set Temp that consists of variables which belong to $\boldsymbol{P C}_{T}$ and are dependent of $X$ given an empty set (lines 3-8 in Algorithm 3). If $X$ and $T$ are conditionally independent conditioning on Temp, then $X$ cannot be a spouse of $T$. Otherwise, $X$ is regarded as a candidate spouse and lines 9-15 in Algorithm 3 will be executed. If $X$ and $T$ are dependent conditioning on $\boldsymbol{S e p}_{T}\{X\} \cup Y(Y \in \boldsymbol{T e m p})$, then $X$ will be added to $\boldsymbol{C S P}_{T}\{Y\}$ (lines 9-15 in Algorithm 3). Since some non-parent variables of $Y$ will be added to $\boldsymbol{C S P}_{T}\{Y\}$, nonparent variables of each $Y \in \boldsymbol{P C _ { T }}$ will be removed from $\boldsymbol{C S P _ { T }}\{Y\}$ and the spouse set $\boldsymbol{S P _ { T }}\{Y\}$ will be obtained after executing lines 17-24 in Algorithm 3.

Step 3 (lines 3-8 in Algorithm 2): At this step, EMB removes false positives from the candidate set of PC of $T$. For each variable $Y$ within $\boldsymbol{P C _ { T }}$, if there exists a subset $\boldsymbol{Z}$ of the union $\boldsymbol{S P _ { T }}\{Y\} \cup$ $\boldsymbol{P C _ { T }}$ such that $Y$ and $T$ are conditionally independent conditioning on $\boldsymbol{Z}, Y$ will be removed from $\boldsymbol{P C _ { T }}$, and $\boldsymbol{S P _ { T }}\{Y\}$. will be set to an empty set.

Step 4 (line 9 in Algorithm 2): At this step, EMB distinguishes parents from children of $T$ as many as possible. We propose a DistinguishPC subroutine to accomplish this goal. DistinguishPC first identifies some children of $T$ with the help of spouses of $T$. Second, DistinguishPC uses the found N -structures to infer edge directions between $T$ and its children. Finally, DistinguishPC distinguishes parents from children of $T$ using Lemma 1.

The details of DistinguishPC are described in Algorithm 4. First, DistinguishPC uses the learnt spouses to identify some children of $T$ (lines 2-6 in Algorithm 4). For example, in Fig. $1, C$ and $D$ are spouses of $T, \boldsymbol{S P _ { T }}\{A\}=\{C\}, \boldsymbol{S P _ { T }}\{K\}=\{D\}$, and DistinguishPC identifies $A$ and $K$ as children of $T$. There exists an N -structure which is formed by $C, A, B$ and $T$ in Fig. 1, DistinguishPC can determine the edge direction between $T$ and

$B$ with the help of $\boldsymbol{S P}_{T}$ and $\boldsymbol{C S P}_{T}$. At Step 2, $C$ will be added to $\boldsymbol{C S P}_{T}\{A\}$ and $\boldsymbol{C S P}_{T}\{B\}$, and $C$ will be removed from $\boldsymbol{S P}_{T}\{B\}$ because $C$ is not a parent of $B$ (lines 17-24 in Algorithm 3). Since $C$ is a spouse of $T$ and $C$ is within the set $\boldsymbol{C S P}_{T}\{B\}$, DistinguishPC identifies $B$ as a child of $T$ (lines 8-12 in Algorithm 4). Theorem 2 gives the theoretical analysis. In addition, in order to orient more edges between $T$ and its PC, two rules in Lemma 1 are used. If $X$ $\Perp Y \mid \emptyset$ and $X \Perp Y \mid T$, we can conclude that $X$ and $Y$ are both parents of $T$. Therefore, DistinguishPC identifies parents of $T$ as many as possible using Lemma 1 (a) (lines 13-19 in Algorithm 4). If $X$ is a parent of $T, X \Perp Y \mid \emptyset$ and $X \Perp Y \mid T$, then $Y$ is a child of $T$. DistinguishPC uses the identified parents of $T$ to determine edge directions between $T$ and its children using Lemma 1 (b) (lines 21-28 in Algorithm 4).

We also propose a variant of EMB to further improve the efficiency of MB learning, which is referred to as EMB-II. Compared with EMB, in learning MB, instead of directly executing line 20 in Algorithm 3, EMB-II first ranks the variables within $\boldsymbol{S P}_{T}\{Y\}$ in descending order according to the dependency with variable $Y$, then executes line 20 in Algorithm 3.

We also propose a variant of ECLS to further improve the efficiency of local causal structure learning, which is referred to as ELCS-II. Compared with ECLS, ELCS-II uses EMB-II for MB learning instead of using EMB.

In the following, we will give the details of Theorem 2 and its proof.

Theorem 2. In a faithful $B N$, given an $N$-structure consisting of four variables $T, A, B, C . T$ is a parent of $A$ and $B, C$ is a parent of $A$, there is no an edge between $C$ and $T, A$ is an ancestor of $B$, and the parents of $B$ are in $P C$ set of $T$, then EMB identifies $B$ as a child of $T$ during learning the $M B$ of $T$.

Proof. Under the faithfulness assumption, the PC of a target variable $T$ only contains parents and children of $T$. Since $C$ is a parent of $A$, there is no an edge between $C$ and $T$, then EMB identifies $C$ as a spouse of $T$ since there is a V-structure $(C \rightarrow A \leftarrow T)$ around $A$. At step 2 of EMB, $C$ will be added to $\boldsymbol{C S P}_{T}\{B\}$ (lines 2-16 in Algorithm 3) since $C$ and $T$ are conditionally dependent given the conditioning set $\{B\} \cup \boldsymbol{S e p}_{T}\{C\}$. If $B$ is a parent of $T$, then $C$ and $T$ are conditionally independent given the conditioning set $\{B\} \cup$ $\boldsymbol{S e p}_{T}\{C\}$, since all paths from $T$ to $C$ are blocked by conditioning set $\{B\} \cup \boldsymbol{S e p}_{T}\{C\}$. Therefore, $B$ is a child of $T$.

### 4.3 Tracing

We first trace the execution of EMB using the example in Fig. 3, then trace the execution of ELCS using the example in Fig. 4.

### 4.3.1 Tracing EMB

We utilize the example in Fig. 3 to trace the execution of EMB. Suppose that we have a dataset for variable set $\boldsymbol{U}=\{A, B, C, D$, $E, F, X, H, I, J, K, L, T\}$. The independence relationships between variables can be represented by the Bayesian Network structure in Fig. 3. In the following, we regard $T$ as the target variable, and give the execution process of EMB.
(1) step 1: referring to the simple network, i.e., the left network in Fig. 3. First, HITON-PC is used to find the PC of $T$. According to Theorem $1, A, B, L, K, E$ and $J$ will be added to $\boldsymbol{P C}_{T}$. Note that $D$ is conditionally independent of $T$ given an empty set, hence $D$ will not be in any of the conditioning sets for higher order conditional independence tests. As a result, $I$ will be added to $\boldsymbol{P C}_{T}$
since $T$ and $I$ are conditionally dependent given conditioning set $\{K\}$. Then, as shown in Fig. 3 (a), $\boldsymbol{P C}_{T}=\{A, B, L, K, E, J, I\}$.
(2) step 2: as shown in Fig. 3 (b), EMB discovers the spouses of $T . X$ and each variable within $\boldsymbol{T e m p}=\{A, B, L, K, E$, $I\}$ are conditionally dependent given an empty set, while $X$ is conditionally independent of $T$ given the conditioning set Temp, so that $X$ cannot be a candidate spouse of $T$ since each path from $X$ to $T$ is blocked by Temp. Similarly, both $F$ and $H$ are not candidate spouses. $C$ and each variable within $\boldsymbol{T e m p}=\{A, B, L, K, E, I\}$ are conditionally dependent given an empty set, and $C$ is dependent of $T$ given Temp, and we need to conduct further tests. Owning to $C \Perp T \mid E, C \Perp T \mid\{E, A\}, C \Perp T \mid\{E, B\}, C \Perp T \mid\{E, L\}, C$ $\Perp T \mid\{E, K\}$ and $C \Perp T \mid\{E, I\}$, hence $C$ is added to $\boldsymbol{C S P}_{T}\{A\}$ and $\boldsymbol{C S P}_{T}\{B\}, \boldsymbol{C S P}_{T}\{A\}=\{C\}, \boldsymbol{C S P}_{T}\{B\}=\{C\}$. Similarly, $D$ is added to $\boldsymbol{C S P}_{T}\{K\}$ and $\boldsymbol{C S P}_{T}\{I\}, \boldsymbol{C S P}_{T}\{K\}=\{D\}, \boldsymbol{C S P}_{T}\{I\}=$ $\{D\}$. In the following, $C$ will be removed from $\boldsymbol{S P}_{T}\{B\}$ since $C \Perp$ $B \mid\{A, T\}$ (lines 17-24 in Algorithm 3). After this step, $\boldsymbol{S P}_{T}\{A\}$ $=\{C\}, \boldsymbol{S P}_{T}\{K\}=\{D\}, \boldsymbol{S P}_{T}\{I\}=\{D\}$.
(3) step 3: as shown in Fig. 3 (c), after checking at line 4 in Algorithm 2, $I$ will be removed from $\boldsymbol{P C}_{T}$ since $I \Perp T \mid\{K, D\}$. After this step, $\boldsymbol{P C}_{T}=\{A, B, L, K, E, J\}, \boldsymbol{S P}_{T}=\{C, D\}$, and $\boldsymbol{M B}_{T}$ $=\{A, B, L, K, E, J, C, D\}$.
(4) step 4: as shown in Fig. 3 (d), EMB orients the edge directions between $T$ and its PC as many as possible. Since $C$ is a spouse of $T$, and $C$ has been added to $\boldsymbol{S P}_{T}\{B\}$ at step 2, based on Theorem $2, B$ is a child of $T$. In addition, according to Lemma $1, E$ and $J$ are parents of $T$ since $E \Perp J \mid \emptyset$ and $E \Perp J \mid T . L$ is a child of $T$ since $E$ is a parent of $T, E \Perp L \mid \emptyset$ and $E \Perp L \mid T$.

### 4.3.2 Tracing ELCS

We use the example in Fig. 4 to trace the execution of ELCS.
Suppose that we have a dataset for variable set $\boldsymbol{U}=\{A, B, C$, $D, E, F, X, H, I, J, K, L, T, Y\}$. The independence relationships between variables can be represented by the BN structure in Fig.4. In the following, we regard $T$ as the target variable, and give the execution process of distinguishing parents from children of $T$ using ELCS. We use the $G(X, Y)=-1$ to represent that $X$ is a parent of $Y, G(X, Y)=1$ represents that $X$ is adjacent to $Y$, $G(X, Y)=0$ represents that there is no an edge between $X$ and $Y$.
(1) step 1: referring to the simple network, i.e., the left network in Fig. 4. We first use EMB to distinguish parents from children of $T$. After learning the MB of $T$, as shown in Fig. 4 (a), the $\boldsymbol{P C}_{T}=\{A, B, L, K, E, J, Y\}$ and $\boldsymbol{S P}_{T}=\{C, D\}$ are obtained. Then, $G(T, A)=-1, G(T, B)=-1, G(T, L)=-1, G(T, K)=-1$, $G(E, T)=-1, G(J, T)=-1$ and $G(Y, T)=1$. The edge direction between $Y$ and $T$ is unsure.
(2) step 2: to resolve $G(Y, T)$, as shown in Fig. 4 (b), we need to make a further search. In the following, the MB of $Y$ is extracted using EMB, and $G(X, Y)=-1, G(F, Y)=-1$. After updating the current local structure using Meek rules, we can learn that $Y$ is a parent of $T$, that is, $G(Y, T)=-1$.

### 4.4 Theoretical Analysis

In the following, we first theoretically analyze the correctness of EMB, then theoretically analyze the correctness of ELCS.

Theorem 3 (Correctness of EMB). Under the faithfulness assumption, and all CI tests are reliable, EMB finds all and only the $M B$ of a given variable.

Proof. At step 1, EMB finds all the true PC variables. According to Theorem 1, the variables which are dependent with the target

![img-2.jpeg](img-2.jpeg)

Fig. 3. An example of the execution process of EMB.
![img-3.jpeg](img-3.jpeg)

Fig. 4. An example of the execution process of ELCS.
variable $T$ will be added to $\boldsymbol{P} \boldsymbol{C}_{T} . \boldsymbol{P} \boldsymbol{C}_{T}$ contains the true parents and children of $T$, since the true PC variables are always dependent of $T$. In addition, $\boldsymbol{P} \boldsymbol{C}_{T}$ also contains some descendants of $T$ [27]. Then, based on the results of step 1, EMB finds all the true spouses of $T$ at step 2. If $Y$ is a collider, $X$ is regarded as a candidate spouse if there exists a V-structure $(X \rightarrow Y \leftarrow T)$ formed by $X, Y$ and $T$, and $X$ will be added to $\boldsymbol{C S P}_{T}\{Y\}$ (lines 1-16 in Algorithm 3). Owning to an exhaustive search, EMB will not miss any true spouses of $T$. In the following, the variable $X \in \boldsymbol{S P}_{T}\{Y\}$ that is a non-parent of $Y$ will be removed from $\boldsymbol{S P}_{T}\{Y\}$ (lines 17-24 in Algorithm 3). According to the Markov condition, the variable $X \in \boldsymbol{S P}_{T}\{Y\}$ will be removed if it is not a parent of $Y$, since conditioning set $\boldsymbol{S P}_{T}\{Y\} \cup T \cup \boldsymbol{P} \boldsymbol{C}_{T} \backslash\{X, Y\}$ contains all true parents of $Y$. Therefore, $\boldsymbol{S P}_{T}$ contains all the true spouses of $T$. The learnt $\boldsymbol{P} \boldsymbol{C}_{T}$ may contain some false PC variables. $T$ and each false PC variable are conditionally independent given the spouses of the false PC variable and $\boldsymbol{P} \boldsymbol{C}_{T}$. At the step 3, the false PC variables found at step 1 and false spouses found at step 2 will be removed (lines 3-8 in Algorithm 2). Then, EMB contains all and only the true PC variables $\boldsymbol{P} \boldsymbol{C}_{T}$ and spouses $\boldsymbol{S P}_{T}$ after executing Algorithm 2, and $\boldsymbol{P} \boldsymbol{C}_{T}$ and $\boldsymbol{S P}_{T}$ together form all and only true MB variables. At step 4, based on Theorem 2 and Lemma 1, parents and children of $T$ are learnt by EMB are correct.

Theorem 4 describes the correctness of the proposed ELCS algorithm. In the following, we will introduce Theorem 4 and its proof in detail.

Theorem 4 (Correctness of ELCS). Under the faithfulness assumption, and all CI tests are reliable, ELCS distinguishes all parents from children of a given variable.

Proof. Under the causal faithfulness assumption, given a target variable, EMB finds all and only the true MB variables and the true PC variables of the target variable. The learnt PC set contains all and only the parents and children of the target variable. Based on Definition 5, the children identified by the learnt spouses are correct. Base on Theorem 2, the children identified by the found N -structures are correct. All the parents and children identified by Lemma 1 are correct. ELCS updates the local causal structures until the parents and children of the target variable have been distinguished. Meek rules [36] are used to orient other undirected edges between the target variable and the variables that are adjacent to the target variable during learning the local causal structure, and all the edge directions determined by Meek rules are correct. Thus, all the parents and children of a given target variable distinguished by ELCS are correct.

### 4.5 Computational Complexity

The computational complexity of ELCS algorithm depends on the steps of discovering MB. In the following, we will give the computational complexity of EMB and ELCS.

The computational complexity of EMB: The computational complexity of EMB depends on its four steps. Given a target variable $T$, at step 1 , the computational cost is dominated by HITON-PC which takes at most $O\left(\left|\boldsymbol{U}\right| 2^{\left|\boldsymbol{P} \boldsymbol{C}_{T}\right|}\right)$ CI tests to find the PC. Step 2 takes $O\left(\left|\boldsymbol{S P}_{T}\right| 2^{\left|\boldsymbol{P} \boldsymbol{C}_{T}\right|+\left|\boldsymbol{S P}_{T}\right|}\right)$ CI tests, step 3 takes

TABLE 2
Computational Complexity of Each Markov Blanket Learning Algorithm


TABLE 3
Computational Complexity of Local and Global Causal Structure Learning Algorithms


$O\left(\left|\boldsymbol{P C}_{T}\right| 2^{\left|\boldsymbol{P C}_{T}\right|+\left|\boldsymbol{S P}_{T}\right|}\right)$ CI tests, step 4 takes $O\left(2\left|\boldsymbol{P C}_{T}\right|^{2}\right)$ CI tests. Thus, the complexity of EMB is $O\left(\left|\boldsymbol{U}\right| 2^{\left|\boldsymbol{P C}_{T}\right|}+\left|\boldsymbol{S P}_{T}\right| 2^{\left|\boldsymbol{P C}_{T}\right|+\left|\boldsymbol{S P}_{T}\right|}+\right.$ $\left.\left|\boldsymbol{P C}_{T}\right| 2^{\left|\boldsymbol{P C}_{T}\right|+\left|\boldsymbol{S P}_{T}\right|}+2\left|\boldsymbol{P C}_{T}\right|^{2}\right)=O\left(\left|\boldsymbol{U}\right| 2^{\left|\boldsymbol{P C}_{T}\right|}\right)$. Let $\left|\boldsymbol{P C}\right|$ represent the largest size of the PC sets of all the variables, the complexity of EMB is $O\left(\left|\boldsymbol{U}\right| 2^{\left|\boldsymbol{P C}\right|}\right)$.

We summarize the computational complexity of EMB and its rivals in Table 2. From the table, IAMB is the fastest among all MB learning algorithms. MMMB and HINTON-MB are the slowest two algorithms, since they need to find the PC sets of all target variable's parents and children. The computational complexity of EMB is lower than STMB. In general, most of the BNs have a large number of variables but a small-sized PC set of each variable, so that EMB is faster than STMB. The computational complexity of BAMB is the same with EMB.

The computational complexity of ELCS: In the best case, the complexity of ELCS is $O\left(\left|\boldsymbol{U}\right| 2^{\left|\boldsymbol{P C}\right|}\right)$. But in the worst case (e.g. the target variable has all single ancestors), ELCS needs to learn a whole structure, hence the complexity of ELCS is $O\left(\left|\boldsymbol{U}\right|^{2} 2^{\left|\boldsymbol{P C}\right|}\right)$.

Table 3 reports the computational complexity of ELCS and its rivals. Note that $m \ll|\boldsymbol{U}|$ is the memory size of L-BFGS [12]. $n$ and $t$ are the number of samples in data and iterations, respectively. $h$ is the number of neurons in the hidden layer [13]. The computational complexity of global causal structure learning algorithms is higher than that of local causal structure learning algorithms, since they learn the whole structure of all variables. PCD-byPCD uses MMPC for PC learning, and CMB uses HITON-MB for MB learning. In the best case, the complexity of PCD-byPCD is consistent with that of MMMB, it is $O\left(\left|\boldsymbol{U}\right||\boldsymbol{P C}| 2^{\left|\boldsymbol{P C}\right|}\right)$. The complexity of CMB is consistent with that of HITON-MB, it is $O\left(\left|\boldsymbol{U}\right||\boldsymbol{P C}| 2^{\left|\boldsymbol{P C}\right|}\right)$. In the worst case, since MMPC can discover the separating sets while learning PC, the complexity of PCD-by-PCD is consistent with that of using MMPC to find PCs of all variables, it is $O\left(\left|\boldsymbol{U}\right|^{2} 2^{\left|\boldsymbol{P C}\right|}\right)$. The complexity of CMB is consistent with that of using HITON-MB to find MBs of all variables, it is $O\left(\left|\boldsymbol{U}\right|^{2}\left|\boldsymbol{P C}\right| 2^{\left|\boldsymbol{P C}\right|}\right)$. ELCS is the fastest algorithm in both best and worst cases, since the complexity of ELCS relies on that of EMB which only takes $O\left(\left|\boldsymbol{U}\right| 2^{\left|\boldsymbol{P C}\right|}\right)$ CI tests to find the MB.

## 5 EXPERIMENTS

In this section, we evaluate the performance of the proposed ELCS algorithm, and this section is organized as follows. Section
5.1 gives the experimental settings, Section 5.2 summarizes and discusses the experimental results, Section 5.3 analyses the reason why ELCS is efficient and effective.

### 5.1 Experimental Settings

### 5.1.1 Datasets

We use eight benchmark BNs to evaluate ELCS against its rivals. Each benchmark BN contains two groups of data, one group containing 10 data sets with 5000 data examples, and the other one including 10 data sets with 1000 data examples. The number of variables of these BNs ranges from 20 to 801 . A brief description of the eight benchmark BNs is listed in Table 4.

### 5.1.2 Comparison Methods

We compare our approach ELCS with three state-of-the-art global causal structure learning algorithms, including MMHC [11], NOTEARS [12] and DAG-GNN [13], and two local causal structure learning algorithms, including PCD-by-PCD [14] and CMB [15]. In addition, we also compare ELCS with ELCS-II.

### 5.1.3 Implementation Details

PCD-by-PCD and CMB algorithms are implemented by ourselves in MATLAB (https://github.com/kuiy/CausalLearner). For MMHC, we use the implementation in the software tool of Causal Explorer [37]. For NOTEARS and DAG-GNN, we use the source codes provided by the authors. In the experiments, $G^{2}$-test with the significance level of 0.01 is utilized to measure the conditional independence between variables. All experimental results are conducted on Windows 10 with Intel(R) i7-8700, 3.19 GHz CPU, and 16GB memory.

### 5.1.4 Evaluation Metrics

In the experiments, we evaluate the performance using the following metrics.

- $\operatorname{ArrP}$ : The number of true directed edges in the output (i.e., the variables in the output belonging to the true parents and children of a target variable in a test DAG) divided by the number of edges in the output of an algorithm.
- $\operatorname{ArrR}$ : The number of true directed edges in the output divided by the number of true directed edges (i.e., the number of parents and children of a target variable in a test DAG).
- SHD: SHD is the number of total error edges, which contains undirected edges, reverse edges, missing edges and extra edges. The smaller value of SHD is better.
- FDR: The number of false edges in the output divided by the number of edges in the output of an algorithm.
- Efficiency: The number of CI tests and the running time (in seconds) are utilized to measure the efficiency.

In the following Tables, the results are reported in the format of $A \pm B$, where $A$ denotes the average results, and $B$ represents the standard deviation. The best results in each setting have been

TABLE 4
Summary of Benchmark BNs


marked in bold. "-" means that the output of the corresponding BN cannot be generated in two days by the algorithm. Note that NOTEARS and DAG-GNN do not perform CI tests.

### 5.2 Experimental Results of ELCS and Its Rivals

We compare ELCS with MMHC, NOTEARS, DAG-GNN, PCD-by-PCD, CMB and ELCS-II on the eight BNs as shown in Table 4. The average results of ArrP, ArrR, SHD, FDR, CI tests and running time of each algorithm are reported in Tables 5-6. Table 5 summarizes the experimental results on the eight BNs with 5,000 data examples, and Table 6 reports the experimental results on the eight BNs with 1,000 data examples. From the experimental results, we have the following observations.

ELCS versus MMHC. Regardless of the number of samples (5000 or 1000), ELCS is significantly better than MMHC. On the ArrP and ArrR metrics, ELCS is superior to MMHC, which means that ELCS finds more true causal edges and less false casual edges. In addition, on the SHD metric, the value of SHD of ELCS is significantly lower than that of MMHC. On the FDR metric, ELCS performs better than MMHC. Furthermore, ELCS always uses less CI tests than MMHC. To learn the local causal structure of a target variable, MMHC needs to learn the whole DAG over all variables in a dataset, hence MMHC performs much more CI tests than ELCS. Thus, we can conclude that ELCS is more efficient and effective than MMHC.

ELCS versus NOTEARS and DAG-GNN. NOTEARS and DAG-GNN are global causal learning algorithms, they need to learn the global structure over all variables, and then obtain the parents and children of a given variable. ELCS achieves better performance than NOTEARS and DAG-GNN using both 5,000 data samples and 1,000 data samples, especially using 5,000 data samples. On the ArrP, ArrR, SHD and FDR metrics, ELCS is significantly better than NOTEARS and DAG-GNN. The values of ELCS on ArrP and ArrR metrics are higher than that of NOTEARS and DAG-GNN, and lower on the SHD and FDR metrics. Since NOTEARS and DAG-GNN adopt a continuous optimization strategy to obtain the DAG from observational data, and the experimental results are susceptible to the influence of parameters. Additionally, NOTEARS and DAG-GNN need to spend much time in learning the DAG, since they obtain the optimal solution by means of a large number of iterations. In a word, ELCS is superior to NOTEARS and DAG-GNN.

ELCS versus PCD-by-PCD and CMB. Both PCD-by-PCD and CMB are local causal learning algorithms. Using 5,000 data samples, ELCS performs better than PCD-by-PCD and CMB. Except on Child, ELCS achieves highest ArrP and ArrR values, and lowest SHD and FDR values on the other BNs. In addition,

TABLE 5
Comparison of ELCS with State-of-the-art Causal Structure Learning Algorithms on Eight Benchmark BNs (size=5,000)


ELCS uses less CI tests than PCD-by-PCD and CMB on most of BNs. Using 1,000 data samples, ELCS is superior to PCD-byPCD and CMB on Alarm, Child, Alarm10, Pigs and Gene. ELCS is better than CMB and worse than PCD-by-PCD on Insurance on the ArrP, ArrR, SHD and FDR metrics, while ELCS has advantages in terms of CI tests and running time. On Insurance10, ELCS is worse than PCD-by-PCD and CMB on the ArrP, ArrR, SHD and FDR metrics. The reason may be that EMB learns inaccurate MBs on small data samples. ELCS is better than PCD-by-PCD and little worse than CMB on Child10 on the ArrP, ArrR, SHD and FDR metrics. Generally, ELCS performs better than PCD-by-PCD and CMB.

ELCS versus ELCS-II. ELCS-II is superior to ELCS. ELCSII further improves the efficiency of EMB while maintaining the same performance as measured by the ArrP, ArrR, SHD and FDR metrics, which indicates the efficiency of ELCS-II.

In summary, it can be seen from Tables 5-6, ELCS is significantly better than MMHC, NOTEARS and DAG-GNN. Additionally, ELCS outperforms PCD-by-PCD and CMB on the ArrP, ArrR, SHD, FDR metrics. Specifically, compared with PCD-by-PCD and CMB, ELCS not only achieves higher ArrP and ArrR values, but also achieves lower SHD and FDR values. Furthermore, ELCS is the fastest algorithm among all structure learning algorithms. ELCS is significantly better than MMHC and NOTEARS in terms of running time. MMHC, NOTEARS

TABLE 6
Comparison of ELCS with State-of-the-art Causal Structure Learning Algorithms on Eight Benchmark BNs (size=1,000)


and DAG-GNN are global causal learning algorithms, they need to find the global structure of a BN. In particular, ELCS is 10 times faster than MMHC and 1000 times faster than NOTEARS and DAG-GNN on average. Additionally, ELCS is also superior to PCD-by-PCD and CMB in terms of running times. ELCS is 2 times faster than PCD-by-PCD and 3 times faster than CMB on average. Specifically, MMHC, NOTEARS, PCD-by-PCD and CMB fail to generate the output on several BNs, whereas ELCS can be successful applied in learning the local causal structure of each variable within two days. But beyond that, ELCS uses the smallest number of CI tests. Overall, ELCS is superior to its rivals in both efficiency and accuracy.

### 5.3 Why ELCS is Efficient and Effective?

In this section, we analyse the reason why ELCS is efficient and effective from the following two aspects. First, we give a case study to evaluate the effectiveness of utilizing the N -structures to infer edge directions between a given variable and its children. Second, we evaluate the effectiveness of the proposed EMB subroutine, since the proposed ELCS algorithm relies on EMB.

### 5.3.1 Case Study

To illustrate the benefit of utilizing the N -structures, we do not use the N -structures to distinguish the children of a given variable in learning the MB of the variable, that is, in the DistinguishPC

TABLE 7
Comparison of ELCS with "ECLS w/o N" on Eight Benchmark BNs (size=5,000)


and DAG-GNN are global causal learning algorithms, they need to find the global structure of a BN. In particular, ELCS is 10 times faster than MMHC and 1000 times faster than NOTEARS and DAG-GNN on average. Additionally, ELCS is also superior to PCD-by-PCD and CMB in terms of running times. ELCS is 2 times faster than PCD-by-PCD and 3 times faster than CMB on average. Specifically, MMHC, NOTEARS, PCD-by-PCD and CMB fail to generate the output on several BNs, whereas ELCS can be successful applied in learning the local causal structure of each variable within two days. But beyond that, ELCS uses the smallest number of CI tests. Overall, ELCS is superior to its rivals in both efficiency and accuracy.

### 5.3 Why ELCS is Efficient and Effective?

In this section, we analyse the reason why ELCS is efficient and effective from the following two aspects. First, we give a case study to evaluate the effectiveness of utilizing the N -structures to infer edge directions between a given variable and its children. Second, we evaluate the effectiveness of the proposed EMB subroutine, since the proposed ELCS algorithm relies on EMB.

### 5.3.1 Case Study

To illustrate the benefit of utilizing the N -structures, we do not use the N -structures to distinguish the children of a given variable in learning the MB of the variable, that is, in the DistinguishPC

TABLE 7
Comparison of ELCS with "ECLS w/o N" on Eight Benchmark BNs (size=5,000)


and DAG-GNN are global causal learning algorithms, they need to find the global structure of a BN. In particular, ELCS is 10 times faster than MMHC and 1000 times faster than NOTEARS and DAG-GNN on average. Additionally, ELCS is also superior to PCD-by-PCD and CMB in terms of running times. ELCS is 2 times faster than PCD-by-PCD and 3 times faster than CMB on average. Specifically, MMHC, NOTEARS, PCD-by-PCD and CMB fail to generate the output on several BNs, whereas ELCS can be successful applied in learning the local causal structure of each variable within two days. But beyond that, ELCS uses the smallest number of CI tests. Overall, ELCS is superior to its rivals in both efficiency and accuracy.

### 5.3 Why ELCS is Efficient and Effective?

In this section, we analyse the reason why ELCS is efficient and effective from the following two aspects. First, we give a case study to evaluate the effectiveness of utilizing the N -structures to infer edge directions between a given variable and its children. Second, we evaluate the effectiveness of the proposed EMB subroutine, since the proposed ELCS algorithm relies on EMB.

### 5.3.1 Case Study

To illustrate the benefit of utilizing the N -structures, we do not use the N -structures to distinguish the children of a given variable in learning the MB of the variable, that is, in the DistinguishPC

TABLE 7
Comparison of ELCS with "ECLS w/o N" on Eight Benchmark BNs (size=5,000)


TABLE 8
Comparison of EMB with State-of-the-art MB Learning Algorithms on Eight Benchmark BNs (size=5,000)


TABLE 10
Comparison of ELCS with ELCS-M, ECLS-S and ELCS-B on Eight Benchmark BNs (size $=5,000$ )


ciency of EMB while maintaining competitive performance, EMB chooses to remove non-spouses within $\boldsymbol{U} \backslash\{T\} \backslash \boldsymbol{P C}_{T}$ of the target variable $T$ as early as possible at lines 2-16 in Algorithm 3. The size of the conditioning sets Temp (line 9 in Algorithm 3) and $\{\mathrm{F}\}$ $\cup \boldsymbol{S e p}_{T}\{X\}$ (line 11 in Algorithm 3) may be large, when the size of data samples is finite, the results of CI tests may be unreliable, leading to poor performance of EMB. Second, the performance of EMB is limited by HITON-PC that is used for PC learning. If HITON-PC has a lower quality of PC learning, inaccurate MBs will be learnt by EMB.

## 6 CONCLUSION

A new local causal structure learning algorithm (ELCS) has been proposed in this paper, which reduces the search space in distinguishing parents from children of a target variable of interest. Specifically, ELCS makes use of the N-structures to distinguish parents from children of the target variable during learning the MB of the target variable. Furthermore, to combine MB learning with the N -structures to infer edge directions between the target variable and its PC, we design an effective MB discovery subroutine (EMB). We theoretically analyze the correctness of ELCS. Extensive experimental results on benchmark BNs indicate that ELCS not only improves the efficiency for learning the local causal structure, but also achieves better performance in accuracy. In future, we plan to extend the ELCS algorithm for global causal structures learning and robust machine learning.

## ACKNOWLEDGMENTS

This work was supported in part by the National Key Research and Development Program of China (under Grant 2020AAA0106100), the National Natural Science Foundation of China (under Grant

61876206), and Open Project Foundation of Intelligent Information Processing Key Laboratory of Shanxi Province (under Grant CICIP2020003).
