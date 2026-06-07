# Mining Combined Causes in Large Data Sets 

Saisai $\mathrm{Ma}^{\mathrm{a}, *}$, Jiuyong $\mathrm{Li}^{\mathrm{a}}$, Lin $\mathrm{Liu}^{\mathrm{a}}$, Thuc Duy $\mathrm{Le}^{\mathrm{a}}$<br>${ }^{a}$ School of Information Technology and Mathematical Sciences, University of South Australia, Mawson Lakes, SA 5095, Australia


#### Abstract

In recent years, many methods have been developed for detecting causal relationships in observational data. Some of them have the potential to tackle large data sets. However, these methods fail to discover a combined cause, i.e. a multi-factor cause consisting of two or more component variables which individually are not causes. A straightforward approach to uncovering a combined cause is to include both individual and combined variables in the causal discovery using existing methods, but this scheme is computationally infeasible due to the huge number of combined variables. In this paper, we propose a novel approach to address this practical causal discovery problem, i.e. mining combined causes in large data sets. The experiments with both synthetic and real world data sets show that the proposed method can obtain high-quality causal discoveries with a high computational efficiency.


Keywords: Causal discovery, Combined causes, Local causal discovery, HITON-PC, Multi-level HITON-PC

## 1. Introduction

Causal relationships can reveal the causes of a phenomenon and predict the potential consequences of an action or an event [1]. Therefore, they are more useful and reliable than statistical associations $[2,3,4]$.

In recent decades, causal inference has attracted great attentions in computer science. Causal Bayesian networks (CBNs) [5, 6, 7] have emerged as a main framework for representing causal relationships and uncovering them in observational data. Due to the incapability of CBNs in coping with high

[^0]
[^0]:    *Corresponding author. Tel.: +61 451981205.

    Email address: saisai.ma@mymail.unisa.edu.au (Saisai Ma)

![img-0.jpeg](img-0.jpeg)

Figure 1: Multiple individual causes vs. the combined cause, where solid arrows denote causal relationships and the dashed lines represent the interaction between the two variables.
dimensional data, some efficient methods were proposed for local causal discovery around a target variable $[8,9,10]$.

One limitation of current causal discovery methods is that they only find a cause consisting of a single variable. However, single causal factors are often insufficient for reasoning about the causes of particular effects [11]. For example, a burning cigarette stub and inflammable material nearby can start a fire, but neither of them alone may cause a fire. With gene regulation, it was found that the expression level of a gene might be co-regulated by a group of other genes, which could lead to a disease [12, 13]. Furthermore, a main objective of data mining is to find previously unobserved patterns and relationships in data. Causal relationships between single variables are easier to be identified by domain experts, but combined causes are much more difficult to be detected [14]. Hence data mining methods for discovering combined causes are in demand. In this paper, we address the problem of finding combined causes in large data sets.

The combined causes considered in this paper are different from the generally discussed multiple causes. For example, in Figure 1, sprinkler causes wet ground, and so does rain. Sprinkler and rain together cause wetter ground. However, in this work, we concern the situation when multiple variables each alone is not sufficient to cause an effect, but their combination is. As shown in Figure 1, there is no causal link from burning cigarette stub or inflammable material to a fire, but the combination of these two factors leads to a fire.

The combined causes studied in this paper cannot be discovered with CBN learning, as in a CBN an edge is drawn from $A$ to $C$ only when $A$ is a cause of $C$. If $A$ and $B$ each alone is not a cause of $C$, no edge is drawn from $A$ or $B$ to $C$, and thus impossible to examine the combined causal effect of $A$ and $B$ on $C$. This limitation of CBNs was discussed in [15] (page 48) as follows:

"Suppose drugs A and B both reduce symptoms C , but the effect of A without B is quite trivial, while the effect of B alone is not. The directed graph representations we have considered in this chapter offer no means to represent this interaction and to distinguish it from other circumstances in which A and B alone each have an effect on C."

To identify combined causes in data, one critical challenge is the computational complexity with large data sets, as the number of combined variables is exponential to the number of individual variables.

In this paper, we propose a multi-level approach to discovering the combined causes of a target variable. Our method is designed based on an efficient local causal discovery method, HITON-PC [8], which was developed on the same theoretical ground as the well-known PC algorithm [15] for CBN learning.

In the rest of the paper, the related work and the contributions of this paper are described in Section 2. Section 3 introduces the background, including the notation and the HITON-PC algorithm. Section 4 presents the proposed method. The experiments and results are described in Section 5. Finally, Section 6 concludes the paper.

# 2. Related Work and Contributions 

As discussed in the previous section, causal Bayesian networks (CBNs), as a main stream causal discovery approach, have been studied extensively. Many algorithms for CBN learning and inference $[5,15,18,19]$ have been developed. Researchers have also tried to incorporate other models and prior knowledge into the CBN framework. The domain experts are interested in taking the prior knowledge and observational data to produce Bayesian networks [20]. Messaoud et al. [21] proposed a framework to learn CBNs, by incorporating semantic background knowledge provided by the domain ontology. In order to address the uncertainties resulting from incomplete and partial information, Kabir et al. [22] combined Bayesian belief network with data fusion model to predict the failure rate of water mains. However, these methods are designed to analyse individual causes, instead of combined causes. Moreover, it may be difficult for domain experts to elicit the CBN structure with combined causes from domain knowledge only.

Another approach $[23,24]$ was proposed to find the relationship structures between groups of variables. Segal et al. [23] defined the module network of which each node (module) was formed by a set of variables having the same

statistical behavior. They also proposed an algorithm to learn the module assignment and the module network structure. Many algorithms and applications $[25,24]$ have been developed to extend the module network model. Yet et al. [26] proposed a method for abstracting the BN structure, where they also merged nodes with similar behavior to simplify the BN structure. The modules or nodes of a module network are not the same as the combined causes defined in this paper, since the components of a combined cause do not necessarily have the similar behaviour.

The sufficient-component cause model $[16,17]$ (often referred by epidemiologists) addresses the combined causes discussed in this paper. According to the model, a disease is an inevitable consequence of a minimal set of factors. However, no computational methods have been developed for finding a sufficient-component cause in observational data. Although the model and interactive causes have attracted statisticians' attentions [27, 28, 29], the work is at the level of theoretical discussions.

Li et al. [30] used the idea of retrospective cohort studies [31] and Jin et al. [32] applied partial association tests [33] to discover causal rules from association rules. While the work has initiated the concept of the combined causes, their focus was on integrating association rule mining with observational studies or traditional statistical analysis for causal discovery.

In this paper, a novel method is proposed to discover the combined causes of the given target variable, based on the causal inference framework established for CBN learning. The contributions of this paper are summarised as follows:

1. We study the problem of mining combined causes which are different from multiple individual causes, and the problem has not been tackled by most existing methods.
2. We develop a new method for discovering combined (and single) causes, and demonstrate its performance and efficiency by experiments with synthetic and real world data.

# 3. Background 

In this section, we firstly describe the notation to be used in the paper (Section 3.1). In Section 3.2, we introduce the HITON-PC algorithm, which is the basis of our algorithms, and then discuss its time complexity.

# 3.1. Notation 

We use upper case letters, e.g. $X$ and $Y$, to represent random variables, and multiple upper case letters, e.g. $X Y$ or $X \& Y$, to denote the combined variable consisting of $X$ and $Y$. Bold-faced upper case letters, e.g. $\boldsymbol{X}$ and $\boldsymbol{Y}$, represent a set of variables. Particularly, we denote the set of predictor variables and the target variable with $\boldsymbol{V}$ and $T$ respectively. The conditional independence between $X$ and $T$ given $\boldsymbol{S}$ is represented as $I(X, T \mid \boldsymbol{S})$.

This paper deals with binary variables only, i.e. each variable has two possible values, 1 or 0 . The value of a combined (binary) variable $X Y$ is 1 if and only if each of its component (binary) variables is equal to 1 (i.e. $X=1$ and $Y=1$ ). A multi-valued variable can be converted to a number of binary variables, e.g. the nominal variable Eduction can be converted to 3 binary variables, High School, Undergraduate and Postgraduate. With binary variables, we can easily create and examine a combined cause involving different values of multiple variables. For example, given the two nominal variables, Gender and Eduction, after converting them to binary variables, we can combine them to have variables, such as (Male, High School) and (Female, Postgraduate).

### 3.2. HITON-PC

Given its high efficiency and origin in the sound CBN learning theory, HITON-PC [8] is a commonly used method for discovering local causal structures with a fixed target variable. The semi-interleaved HITON-PC is used as the basis for our proposed method. Under the causal assumptions [15], HITON-PC uses conditional independence (CI) tests to find the causal relationships around a target variable $T$, i.e. the set of parents $(\mathrm{P})$ and children (C) of $T$.

Referring to Algorithm 1, HITON-PC takes a data set of the predictors $\boldsymbol{V}$ and the target $T$ to produce $\operatorname{TPC}(T)$, the set of parents and children of $T$. The algorithm uses two data structures, a priority queue $O P E N$ and a list $\operatorname{TPC}(T)$. Initially $O P E N$ contains all predictors associated with $T$ and $\operatorname{TPC}(T)$ is empty (see lines 1 and 2 of Algorithm 1). It then iterates between the two phases, inclusion and elimination, until $O P E N$ becomes empty.

In the inclusion phase, the variable having the strongest association with $T$ is removed from $O P E N$ and added to $\operatorname{TPC}(T)$ (line 4). In the elimination phase, if $O P E N$ is not empty, the forward stage (lines 5-9) is executed. The variable newly added to $\operatorname{TPC}(T), X$, is eliminated from $\operatorname{TPC}(T)$ if it is independent of $T$ given a subset of current $\operatorname{TPC}(T)$, otherwise it is kept (still

ALGORITHM 1: The Semi-interleaved HITON-PC Algorithm [8]
Input: A data set $\boldsymbol{D}$ for predictor variable set $\boldsymbol{V}$ and target $T$
Output: $T P C(T)$, the set of parents and children of $T$
$1: T P C(T) \leftarrow \emptyset$
2: Let $O P E N$ contain all variables associated with $T$, sorted in descending order of strength of associations.
3: repeat
Phase I: Inclusion (line 4)
4: $\quad$ Move the first variable $X$ from $O P E N$ to the end of $T P C(T)$
Phase II: Elimination (lines 5-16)
// Forward stage
if $O P E N \neq \emptyset$ then
$X \leftarrow$ the variable last added to $T P C(T)$
if $\exists \boldsymbol{S} \subseteq T P C(T) \backslash\{X\}$, s.t. $I(X, T \mid \boldsymbol{S})$ then
Remove $X$ from $T P C(T)$
end if
// Backward stage
else
for each $X \in T P C(T)$ do
if $\exists \boldsymbol{S} \subseteq T P C(T) \backslash\{X\}$, s.t. $I(X, T \mid \boldsymbol{S})$ then
Remove $X$ from $T P C(T)$
end if
end for
end if
17: until $O P E N=\emptyset$
18: Output $T P C(T)$
tentatively) in $T P C(T)$. If $O P E N$ is empty, the backward stage (lines 10-16) is activated, and each variable $X$ in current $T P C(T)$ is tested, and if a subset of $T P C(T)$ is found such that $X$ is independent of $T$ given the subset, $X$ is removed from $T P C(T)$.

HITON-PC uses several heuristics to improve efficiency. At the forward stage, CI tests are conducted only on the newly added variable, instead of performing a full variable elimination. To compensate for possible false discoveries caused by this heuristic, HITON-PC uses the backward stage to "tighten up" $T P C(T)$ by testing the conditional independence of each

variable with $T$ given the other variables in $\operatorname{TPC}(T)$. Moreover, the use of the priority queue, $O P E N$, allows variables having stronger associations with $T$ to be included and evaluated first. As these variables are more likely to be the true parents or children of the target, once they are in $\operatorname{TPC}(T)$, it is expected that given these variables, other variables that should not be in $\operatorname{TPC}(T)$ are quickly identified and removed so that in the forward stage $\operatorname{TPC}(T)$ will not be over expanded, thus reducing the number of CI tests. Additionally, in practice, HITON-PC restricts the maximum order of CI tests to a given threshold max- $k$, i.e. the maximum size of the conditioning set ( $\boldsymbol{S}$, see Algorithm 1) is max-k.

The time complexity of HITON-PC mainly depends on the number of CI tests. Each variable needs to be tested on all subsets of $\operatorname{TPC}(T)$. Thus the complexity regarding each variable is $O\left(2^{\left|\operatorname{TPC}(T)\right|}\right)$, and the total time complexity is $O\left(|\boldsymbol{V}| 2^{\left|T P C(T)\right|}\right)$. When max-k is specified, the complexity becomes polynomial, i.e. $O\left(|\boldsymbol{V}||\operatorname{TPC}(T)|^{\max -k}\right)$. Extensive experiments have shown that HITON-PC is able to cope with thousands of variables with low rate of false discoveries [8].

# 4. Uncovering Combined Causes 

Having introduced the background knowledge, in this section, we present the proposed method for discovering combined causes. We firstly introduce the naïve approach (Section 4.1), which is a straightforward way to detect the combined causes. Then we give the formal definition of combined causes and present the basic idea of the proposed method (Section 4.2). Finally, we describe the proposed method (including two algorithms, MH-PC-F and MH-PC-B) for discovering combined causes (Section 4.3) and discuss their possible false discoveries (Section 4.4).

### 4.1. The Naïve Approach

A naïve scheme for finding the combined causes can be as follows. Firstly, we generate a new variable set with combined variables using the original variable set. For example, for $\boldsymbol{V}=\{A, B, C, D, E, X, Y, Z\}$, the new variable set (with $2^{8}-1$ variables) is $\boldsymbol{V}^{\prime}=\{A, \ldots, Z, A B, \ldots, Y Z, A B C, \ldots, X Y Z$, $\ldots, A B C D E X Y Z\}$. Then we run a local causal discovery algorithm, such as HITON-PC, to find both single and combined causes using the data set created for $\boldsymbol{V}^{\prime}$.

The naïve approach, however, is not feasible because the number of combined variables is exponential to the number of individual variables. In the following, we discuss how our proposed method tackles the problem.

# 4.2. Basic Idea of the Proposed Method 

In fact, it is not necessary to consider all combined variables. Particularly, we are not interested in a combined variable, e.g. $W=X Y$, of which a component $X$ or $Y$ is a cause already, as it is reasonable to assume that the causal relationship between $W$ and the target $T$ is due to the relationship between $X$ or $Y$ and $T$. To improve efficiency, we can exclude such combined variables when finding combined causes of $T$, and only consider the combined variables whose components are not causes of $T$.

Furthermore, as discussed in Section 1, a combined cause consisting of non-cause components is more difficult to be observed by domain experts and they cannot be represented or discovered using other approaches such as CBNs, hence mining such combined causes is useful in practice.

The definition of the combined causes studied in this paper is given below.

Definition 1 (Combined Cause). Let $W$ be a combination of multiple variables. $W$ is a combined cause of $T$ if $W$ is a cause of $T$ and any of its component variables, $X \in W$, is not a cause of $T$.

Based on Definition 1, we can design an algorithm to find such combined causes (and single causes) in a level by level manner. We firstly, at the $(k-1)^{\text {th }}$ level $(k \geq 2)$, obtain $T P C_{k-1}(T)$, the set of parents and children of $T$, each consisting of $k-1$ individual variables. Then at the $k^{\text {th }}$ level, combined variables are generated based on $n T P C(T)$, the set of non-cause variables at all the lower levels, i.e. $n T P C(T)=n T P C_{1}(T) \cup \ldots \cup n T P C_{k-1}(T)$, where $n T P C_{i}(T)(i \in\{1, \ldots, k-1\})$ is the set of non-cause variables each containing $i$ individual variables. For example, a $k^{\text {th }}$ level combined variable can be generated by combining an $i^{\text {th }}$ level $(i \in\{1, \ldots, k-1\})$ non-cause variable and a $(k-i)^{\text {th }}$ level non-cause variable.

For non-cause variables $X$ and $Y$, if the combination $X Y$ is a combined cause, then it is reasonable to assume that $X$ positively contributes to the relationship between $Y$ and the target $T$ and vice versa. For example, the combustible dust suspended in the air (even at a high concentration) has no causal effect on a dust explosion, but an ignition source will improve their

relationship significantly and thus the combination of the two factors can result in a dust explosion. This observation leads to the following definition.

Definition 2 (Redundant Combined Variable). For $\forall X, Y \in \boldsymbol{V}$, the combination $X Y$ is a redundant combined variable, if either $I(X, T \mid Y=1)$ or $I(Y, T \mid X=1)$, where $X$ and $Y$ are not individual causes of the target $T$.

By excluding redundant combined variables, we can further improve the efficiency of the causal discovery.

Based on the above discussion and HITON-PC, we propose the Multilevel HITON-PC (MH-PC) method for finding both single and combined causes of a given target. In the following section, we present the details of the method.

# 4.3. Multi-level HITON-PC 

Referring to Algorithm 2, at the first level, MH-PC invokes HITON-PC to find the single causes of $T, T P C_{1}(T)$ (line 1) and initiates $T P C(T)$ as $T P C_{1}(T)$ (line 2). The single non-cause variables are put in $n T P C_{1}(T)$ and $n T P C(T)$ (non-cause variables identified at all the lower levels) is initially empty (line 2).

At level $k(k \geq 2)$, MH-PC firstly updates $n T P C(T)$ so that it contains the non-causes from levels 1 to $k-1$ (line 4). Next the algorithm generates combined variables containing $k$ individual variables by combining the variables in $n T P C(T)$ (line 5). Redundant combined variables are then removed (line 6) and the new data set $D_{k}$ for level $k$ combined variables $\left(\boldsymbol{V}_{\boldsymbol{k}}\right)$ is created too (line 7). From lines 8 to 23 , we identify level $k$ combined causes from $\boldsymbol{V}_{\boldsymbol{k}}$. Initially $O P E N$ contains all the combined variables in $\boldsymbol{V}_{\boldsymbol{k}}$ which are associated with $T$ and the variables are sorted in descending order of the strength of associations (line 8). Similar to HITON-PC, the inclusion and elimination phases are carried out iteratively till $O P E N$ is empty. At the end of the iteration (line 23), $T P C_{k}(T)$ includes the discovered combined causes consisting of $k$ variables, and $T P C(T)$ includes all the causes from level 1 to level $k$. Note that in line 17, to improve the efficiency further, the backward stage only checks the level $k$ candidates in $T P C_{k}(T)$, instead of all candidates in $T P C(T)$, as all the lower level parents and children have been confirmed at previous levels.

In line 24, the set of level $k$ non-causes is updated before completing the work at level $k$. Finally MH-PC outputs $T P C(T)$ until $k=k_{\max }$ (the maximum level of causal discovery).

# ALGORITHM 2: Multi-level HITON-PC (MH-PC) 

Input: A data set $\boldsymbol{D}$ for predictor variable set $\boldsymbol{V}$ and target $T ; k_{\max }$, the maximum level of causal discovery
Output: $\operatorname{TPC}(T)$, the set of (single and combined) parents and children of $T$
1: Call Algorithm 1 (HITON-PC), i.e. $T P C_{1}(T)=\operatorname{HITON}-\operatorname{PC}(\boldsymbol{D}, \boldsymbol{V}, T)$
2: $\operatorname{TPC}(T)=\operatorname{TPC}_{1}(T) ; n \operatorname{TPC}_{1}(T)=\boldsymbol{V} \backslash \operatorname{TPC}_{1}(T) ; n \operatorname{TPC}(T)=\emptyset$
3: for $k=2$ to $k_{\max }$ do
$n \operatorname{TPC}(T)=n \operatorname{TPC}(T) \cup n \operatorname{TPC}_{k-1}(T)$
5: $\quad$ Generate $k^{\text {th }}$ level combined variable set $\boldsymbol{V}^{\prime}$ based on $n \operatorname{TPC}(T)$
6: $\quad \boldsymbol{V}_{\boldsymbol{k}}=$ redundancyTest $\left(\boldsymbol{V}^{\prime}\right)$
7: $\quad$ Generate corresponding data set $\boldsymbol{D}_{\boldsymbol{k}}$ for $\boldsymbol{V}_{\boldsymbol{k}}$
8: Let $O P E N$ contain all variables (in $\boldsymbol{V}_{\boldsymbol{k}}$ ) associated with $T$, sorted in descending order of strength of associations.
9: repeat
Phase I: Inclusion (line 10)
10: $\quad$ Move the first variable from $O P E N$, add it to the end of $\operatorname{TPC}(T)$ and $\operatorname{TPC}_{k}(T)$
Phase II: Elimination (lines 11-22)
// Forward stage
11: if $O P E N \neq \emptyset$ then
$X \leftarrow$ the variable last added to $\operatorname{TPC}(T)$
13: if $\exists \boldsymbol{S} \subseteq \operatorname{TPC}(T)$, s.t. $I(X, T \mid \boldsymbol{S})$ then
14: $\quad$ Remove $X$ from $\operatorname{TPC}(T)$ and $\operatorname{TPC}_{k}(T)$
15: end if
// Backward stage
16: else
17: $\quad$ for each $X \in T P C_{k}(T)$ do
18: $\quad$ if $\exists \boldsymbol{S} \subseteq \operatorname{TPC}(T) \backslash\{X\}$, s.t. $I(X, T \mid \boldsymbol{S})$ then
19: $\quad$ Remove $X$ from $\operatorname{TPC}(T)$ and $\operatorname{TPC}_{k}(T)$
20: end if
21: end for
22: end if
23: until $O P E N=\emptyset$
24: $\quad n \operatorname{TPC}_{k}(T)=\boldsymbol{V}_{\boldsymbol{k}} \backslash \operatorname{TPC}_{k}(T)$
25: end for
26: Output $\operatorname{TPC}(T)$

In the forward stage (i.e. the case when $O P E N \neq \emptyset$ ), as with HITONPC, MH-PC searches the current $\operatorname{TPC}(T)$ for a subset $\boldsymbol{S}$ to test whether the combined variable $X$ is independent of $T$ given $\boldsymbol{S}$ (line 13). Since combined variables in $\operatorname{TPC}(T)$ are combinations of individual variables, MH-PC may have conducted some redundant conditional independence tests. For example, the CI test between $X$ and $T$ given a combined variable $Y Z$ (i.e. $I(X, T \mid Y Z)$ ) may be unnecessary if the test given the two individual variables $Y$ and $Z$ (i.e. $I(X, T \mid Y, Z)$ ) has been done. To address this issue, we propose a variant of MH-PC, called MH-PC-B (B version of MH-PC). To avoid confusion, in the rest of the paper, we call the MH-PC algorithm shown in Algorithm 2 MH-PC-F (Full version of MH-PC). In the forward stage, when conducting the level $k$ test with MH-PC-B, we do not include the level $k$ variables in $\operatorname{TPC}_{k}(T)$ into conditioning sets, i.e. we replace line 13 in Algorithm 2 with the following statement:

$$
\text { if } \exists \boldsymbol{S} \subseteq T P C(T) \backslash T P C_{k}(T), \text { s.t. } I(X, T \mid \boldsymbol{S})
$$

As MH-PC-B conducts the tests conditioning only on the lower level variables, it can have higher efficiency than MH-PC-F, but at the same time it may produce some false positives. However, since in the backward stage (lines 17-21 of Algorithm 2), we do another check of the candidate causes remained in $\operatorname{TPC}_{k}(T)$, it is expected that the false discoveries are removed. As we will see from the next section, the experiments show that MH-PC-B is more efficient than MH-PC-F, while producing the same results as MH-PC-F with the data sets used.

# 4.4. False Discoveries of Multi-level HITON-PC 

Since MH-PC-F (and MH-PC-B) follows the idea of HITON-PC, we firstly analyse the quality of HITON-PC in term of false discoveries. In HITON-PC, possible false decisions mainly come from two sources [15, 34]: the use of max$k$, the maximum size of conditioning sets ( $\boldsymbol{S}$, see Algorithms 1 and 2) used for conditional independence tests, and incorrect results of statistical tests. Using a smaller max- $k$ reduces the number of conditional independence tests, thus improves efficiency, but results in false positive discoveries. Fortunately, when max- $k=3$ or 4 , the false positive rate is not high, as shown in [8]. When we do not have enough number of samples, the statistical tests may produce incorrect results.

In the following, we will discuss the false discoveries coming from the interactions between variables. As mentioned above, the proposed method

only focuses on non-redundant combined variables (Definition 2). While this strategy is used for reducing complexity, it may lead to false discoveries. However, we argue that our algorithms can still obtain high-quality causal findings. For non-cause variable $X$, if another non-cause variable $Y$ cannot improve the relationship between $X$ and the target $T$, then the combination $X Y$, in most cases, may not improve the relationship between $X$ and $T$. This type of combined variables are unlikely to be combined causes. The experiment results in Section 5 have confirmed this intuition.

# 5. Experiments 

We implemented MH-PC-F and MH-PC-B based on the semi-interleaved HITON-PC implementation in the R package, bnlearn [35]. In the experiments, the maximum level of combination (i.e. $k_{\max }$ in Algorithm 2) is restricted to 2, i.e. a combined cause at most consists of two component variables. We set the threshold of $p$-value to 0.01 to prune redundant combined variables and 0.05 to test causal relationships, for both synthetic and real world data sets.

### 5.1. Data Sets

10 synthetic and 7 real world data sets were used in the experiments, and a summary of the data sets is shown in Table 1. The variables in all data sets are binary, i.e. each variable has two possible values, 1 or 0 . The class variable in each data set is specified as the target variable. The numbers of variables shown in the table refer to the numbers of single predictor variables. The distribution of each data set indicates the percentages of the two different values of class variables. For synthetic data sets, the ground truth (i.e. the number of true causes) is shown in the table, where the first value is the number of single causes each consisting of one predictor variable and the second value is the number of combined causes each consisting of two predictor variables.

The first five synthetic data sets (with small number of variables) in Table 1 were generated with two main steps: (1) generating a data set based on a BN (Bayesian network) created randomly by the TETRAD software tool (http://www.phil.cmu.edu/tetrad/), and (2) generating the final synthetic data set by "splitting" some causes of the target into two new variables. Specifically, we firstly created a random BN using the TETRAD software,

Table 1: A Brief Description of Data Sets


whose structure and conditional probability tables were both generated randomly. In the obtained BN, one of the variables was designated as the target and the others as predictor variables. Records of all variables were generated based on the conditional probability tables, using the built-in Bayes Instantiated Model. Then we selected and split a parent node, e.g. $A$, of the target into two variables, e.g. $A_{1}$ and $A_{2}$, such that (1) $A_{1} \wedge A_{2}=A$ (i.e. $A_{1}$ and $A_{2}$ both are equal to 1 if and only if $A$ is 1 ), and (2) $A_{1}$ or $A_{2}$ is not an individual cause of the target. Note that, for combined causes in the synthetic data, we do not have a complete ground truth, since it may include some combined causes that we do not observe.

For the next five larger synthetic data sets (Syn-50, ..., Syn-120), it is unpractical to generate them based on randomly drawn BNs, since it takes too long time to generate one. We firstly drew a simple BN where some variables were the parents of the target, some were not. Then we adopted logistic regression to generate the data based on the BN. Next, we employed the aforementioned splitting process to obtain the final data sets.

All real world data sets shown in Table 1 are obtained from the UCI Machine Learning Repository [38]. The first six real world data sets were employed to assess the effectiveness of the proposed algorithms, while the Census data set was used for evaluating the efficiency. The CMC (Contraceptive Method Choice) data set is an extraction of the National Indonesia Contraceptive Prevalence Survey in 1987. The German data set is a data set for classifying people's credit risks based on a set of attributes. House-votes-84 contains the United States Congressional Voting Records in 1984. Hypothyroid and Sick are two medical data sets, which are from the Thyroid Disease data set of the repository (discretised using the MLC++ discretisation utility [39]). The Kr-vs-kp data set is generated and described based on a chess game, King-Rook versus King-Pawn on A7 (usually abbreviated as KRKPA7). The Census data set is the Census Income (KDD) data set from the UCI Machine Learning Repository. In our experiments, all continuous attributes have been removed from the original data sets.

# 5.2. Performance Evaluation 

Three sets of experiments with the synthetic data were done to assess the accuracy of MH-PC-F and MH-PC-B by examining the results against the ground truth.

Firstly we compared MH-PC-F and MH-PC-B with two naïve approaches using HITON-PC and PC-select [37] respectively (denoted as Naïve-H and Naïve-S in the following). PC-select is an effective method for discovering the parents and children of a target variable, so we employed it as a benchmark for accuracy comparison.

Because the two naïve methods, especially Naïve-S, cannot handle large data sets, two small synthetic data sets (Syn-7 and Syn-10) were used in this set of experiments. Moreover, it is easier for small data sets to provide a good visualization of the detailed results.

The ground truth of the Syn-7 data set is that $V 3$ and $V 4$ are two single causes of the target and $V 1 \& V 2$ is a combined cause (see the Ground truth column of Table 2, where Yes means the predictor variable is a cause of the target, and No means otherwise). In Table 2, MH-PC-F and MH-PC-B find exactly the ground truth in Syn-7. While Naïve-H identifies the ground truth, it includes a number of redundant results, for example, $V 3 \& V 5$ and $V 4 \& V 5$ since $V 3$ and $V 4$ are causes already. Naïve-S misses the combined cause $(V 1 \& V 2)$ and it finds some redundant combined causes too. Similar

Table 2: Comparison of the proposed algorithms with the naïve methods


results can be observed with the Syn-10 data set. MH-PC-F and MH-PC-B miss the true single cause, $V 7$, and the naïve methods do not find it either.

Then we compared MH-PC-F and MH-PC-B with CR-CS [36] and CRPA [32] using three synthetic data sets, Syn-12, Syn-16 and Syn-20. CR-CS and CR-PA are both designed to explore causal relationships from association rules, and they are also capable of finding both single and combined causes. The results are shown in Table 3, where $P, R$ and $F_{1}$ represent the Precision, Recall and $F_{1}$-measure respectively. In the paper, we used odds ratio greater than 1.5 as the threshold to indicate a significant result in both CR-CS and CR-PA. We can see that MH-PC-F and MH-PC-B both achieve higher accuracy than CR-CS and CR-PA, based on the known ground truth. Actually, CR-CS and CR-PA both perform very well in term of Recall, but they also include many false positives, since a main aim of these two methods is for explorations and they tolerate false positives and seek high recall.

In the next set of experiments, the last five larger synthetic data sets in Table 1 were used. From Table 4, all the four algorithms (i.e. CR-CS, CR-PA, MH-PC-F and MH-PC-B) can recover the ground truth very well from the data sets with relatively large sizes.

Table 3: Comparison of combined causes discovered by CR-CS, CR-PA, MH-PC-F and MH-PC-B with small synthetic data sets


Table 4: Comparison of combined causes discovered by CR-CS, CR-PA, MH-PC-F and MH-PC-B with larger synthetic data sets


Based on the results of three sets of experiments, it is reasonable to conclude that MH-PC-F and MH-PC-B are capable to find single and combined causes. Another finding is that the causes (single and combined) identified by MH-PC-F and MH-PC-B are always the same, and this indicates two

Table 5: Number of (single and combined) causes discovered by MH-PC-F and MH-PC-B in real world data sets


Table 6: Examples of combined causes identified from Sick and German data sets


algorithms can achieve consistent results. This is also demonstrated by the results of two algorithms with all real world data sets, as described in the following.

To investigate combined causes in the real world cases, we ran the proposed algorithms on the first six real world data sets in Table 1 for performance evaluation, where MH-PC-F and MH-PC-B still return consistent results as shown in Table 5. The proposed algorithms find many combined causes, and some of the combined causes discovered are reasonable as judged by common sense, shown in Table 6. For example, from the Sick data set it is found that a low level of TT4 (Total T4) and T3 may result in thyroid disease (Table 6, where T4 and T3 are hormones produced by thyroid), and being sick and having a low level of T3 can lead to thyroid disease too. Some interesting combined causes are also discovered in the German data set. If one person has a private real estate and does not apply for any other installment plan, then this person is very likely to have a low default risk.

# 5.3. Efficiency and Scalability 

We ran Naïve-H, Naïve-S, CR-CS, CR-PA, MH-PC-F and MH-PC-B with various data sets on the same computer with a 3.4 GHz quad-core CPU and

![img-1.jpeg](img-1.jpeg)

Figure 2: Scalability with number of variables - Census data

16 GB of memory.
The running time of the algorithms on subsets of the Census data con-
![img-2.jpeg](img-2.jpeg)

Figure 3: Scalability with number of variables - Synthetic data

![img-3.jpeg](img-3.jpeg)

Figure 4: Scalability with umber of records - Census data
taining $30,50,70,100$ and 150 variables with the same sample size ( 50 K ) is shown in Figure 2. The two naïve methods are much slower than MH-PC-F and MH-PC-B, and Naïve-S is the most inefficient one. While the two naïve methods do not scale well with the number of variables, the two proposed algorithms both perform good scalability.

When applying the algorithms to the synthetic data sets containing different numbers of variables, both naïve methods do not return results after 5 hours. So no results of naïve methods are shown in Figure 3. From the figure, both proposed algorithms again scale well.

We then ran the algorithms with $50 \mathrm{~K}, 100 \mathrm{~K}, 150 \mathrm{~K}, 200 \mathrm{~K}$, and 250 K samples respectively from the Census data set with 100 variables selected randomly, and the execution time of MH-PC-F and MH-PC-B is shown in Figure 4. No results are obtained for Naïve-S, and Naïve-H also cannot handle data sets with more than 50 K samples. Similarly, MH-PC-B is more efficient and scalable than MH-PC-F.

To summarise, MH-PC-F and MH-PC-B are much faster than the naïve methods, and both proposed algorithms scale well in terms of the number of variables and number of samples. The experiments have also confirmed the discussions in Section 4.3 that MH-PC-B can achieve higher efficiency than MH-PC-F.

# 6. Conclusion 

In practice, it is useful to identify a cause consisting of multiple variables, which individually are not causes of the target variable. However, finding such combined causes is challenging as the number of combined variables will increase exponentially with the increase of the number of individual variables. As far as we know, there has been very little work on discovering the combined causes, and the problem has not been studied in causal Bayesian network research either.

In this paper, we have proposed two efficient algorithms to mine the combined causes from large data sets. The proposed algorithms are based on a well-designed local causal discovery method, the semi-interleaved HITONPC algorithm, with the novel extensions for dealing with combined causes. Experiments have shown that the proposed algorithms can find single and combined causes with a low number of false discoveries from synthetic data sets, and discover many reasonable combined causes from real world data. Additionally, the algorithms have been shown to scale up well with respective to the number of variables and the number of samples with both synthetic and real world data.

In the near future, we will apply the proposed algorithms to solving real world problems, such as investigating the mechanisms of gene regulation, for which there is evidence showing that many gene regulators work together to regulate their target genes.

## 7. Acknowledgement

This work has been supported by Australian Research Council (ARC) Discovery Project Grant DP140103617.
