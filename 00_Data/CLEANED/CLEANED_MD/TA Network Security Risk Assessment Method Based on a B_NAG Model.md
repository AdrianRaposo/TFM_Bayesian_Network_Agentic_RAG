# A Network Security Risk Assessment Method Based on a B_NAG Model 

Hui Wang ${ }^{1}$, Chuanhan Zhu ${ }^{1}$, Zihao Shen ${ }^{1, *}$, Dengwei Lin ${ }^{2}$, Kun Liu ${ }^{1}$ and MengYao Zhao ${ }^{3}$<br>${ }^{1}$ School of Computer Science \& Technology, Henan Polytechnic University, Jiaozuo, 454000, China<br>${ }^{2}$ Office of Educational Administration, Jiaozuo University, Jiaozuo, 454000, China<br>${ }^{3}$ Department of Computer Science, University College London, London, United Kingdom<br>${ }^{c}$ Corresponding Author: Zihao Shen. Email: szh@hpu.edu.cn<br>Received: 08 October 2020; Accepted: 09 January 2021


#### Abstract

Computer networks face a variety of cyberattacks. Most network attacks are contagious and destructive, and these types of attacks can be harmful to society and computer network security. Security evaluation is an effective method to solve network security problems. For accurate assessment of the vulnerabilities of computer networks, this paper proposes a network security risk assessment method based on a Bayesian network attack graph (B_NAG) model. First, a new resource attack graph (RAG) and the algorithm E-Loop, which is applied to eliminate loops in the $\mathrm{B}_{-} \mathrm{NAG}$, are proposed. Second, to distinguish the confusing relationships between nodes of the attack graph in the conversion process, a related algorithm is proposed to generate the B_NAG model. Finally, to analyze the reachability of paths in $\mathrm{B}_{-} \mathrm{NAG}$, the measuring indexs such as node attack complexity and node state transition are defined, and an iterative algorithm for obtaining the probability of reaching the target node is presented. On this basis, the posterior probability of related nodes can be calculated. A simulation environment is set up to evaluate the effectiveness of the B_NAG model. The experimental results indicate that the B_NAG model is realistic and effective in evaluating vulnerabilities of computer networks and can accurately highlight the degree of vulnerability in a chaotic relationship.


Keywords: Network attack graph; Bayesian network; state transition; reachability; risk assessment

## 1 Introduction

Computer networks play an indispensable role in people's productivity and daily life. However, these networks face a variety of cyberattacks, most of which are highly contagious and destructive. These attacks threaten the network security of devices, affecting the popularization of networks and even severely damaging information security $[1-3]$.

According to the "Development Status of China Internet Sites and Security Report in 2018" [4], the National Computer Network Emergency Response Technical Team of China (CNCERT) discovered that over 1.254 million Internet of Things smart devices was attacked successfully and therefore had a great threat to the security of networks. Moreover, in 2018, CNCERT discovered over 2.05 million

This work is licensed under a Creative Commons Attribution 4.0 International License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

cyberattacks continuing a trend of high growth over the previous six years. A survey of these attacks announced that the number of applications had quickly increased and was nearly three times higher than the percentage in 2016.

In recent years, researchers have introduced methods based on Bayesian probabilities in evaluating vulnerabilities of attack graphs [5-7]. Bayesian networks are capable of representing nondeterministic relationships and can be used to quantify the correspondences within attack graphs. Therefore, methods of effectively combining a Bayesian network with an attack graph for network vulnerability assessment have become an important focus of research.

# 2 Related Research 

Recently, lots of scholars analyzed vulnerabilities of networks by using attack graph. Because of the asymmetric information between attackers and defenders, the detection of Zero Day attacks is still challenging. Revealing Zero Day attacks based on attack paths is a better strategy than targeting them individually.

Sun et al. [8] implemented the system ZePro to identify Zero Day attack paths by adopting the probabilistic approach. With evidence of intrusion as input, the Bayesian network used in this system can calculate the infection probabilities concerning object instances.

The dynamic defense framework was presented to select best countermeasures against diverse attack damage costs [9]. To calculate these costs, a new defense-centric model was designed on the basis of service dependency graphs. The current approaches suffer from some limitations. For example, only static countermeasure effectivity and static countermeasure deployment costs are considered, but the negative impacts of the possible countermeasures on service quality are neglected [10]. These above-mentioned restrictions may lead an industrial control system (ICS) to choose improper countermeasures and deployment locations. And then they can degrade the network performance and frustrate legitimate users.

The construction and analysis on inference rules of attack graph was presented by Garg et al. [11]. They developed a methodology for prioritizing individual vulnerabilities and attack paths using a PageRank model. The results were verified by using a Markov model, and showed that the methodology outperformed lots of current technologies [12] about risk analysis. However, the relevant experiment was lack of specific indicators, and the results were not convincing.

As Zhang et al. [13] said, dynamic risk analysis is an important component of protecting network security. However, risk assessment methods used in network systems are not very appropriate for ICSs due to their unique characteristics. That paper proposed a multilevel network model including attack functions and incidents based on Bayesian. On this basis, it proposed a new risk incident prediction method, and designed a dynamic security risk assessment method which can assess the risk caused by unknown attacks [14]. Moreover, a quantification method was presented to further calibrate the accuracy of assessment. Finally, to test and verify the method, the simplified control system was simulated in MATLAB.

On the basis of previous researches, the paper presents a Bayesian network attack graph (B_NAG) model and an algorithm to assess network vulnerabilities. In this paper, probability theory is introduced into the resource attack graph (RAG) model and converted into the corresponding B_NAG model. The reachability probability of nodes can be calculated, and the final reachability probability of attack paths can be calculated. Finally, the related posterior probability can be calculated, and enable network security administrators to assess network security more accurately and effectively.

## 3 The RAG Model

Attack graph is a method to analyze all sequences of vulnerabilities exploited by attackers. Attacks can be occurred against all available node status and vulnerability, and all sequences can be constructed into a

directed graph. The purpose of the RAG model is to characterize an attack sequence launched against the attacker's intentions according to Bayesian probability calculations to help network administrators properly understand the security status of their networks. The RAG model is constructed as described below.

Definition 1 The graph $R A G=\left(S, S_{0}, A, E, \Gamma, L, O\right)$ is a directed graph, where the relevant notations are defined as follows:

- $S=\left\{s_{i} \mid i=1, \ldots, N\right\}$ denotes a resource state nodes set.
- $\mathrm{S}_{0} \in \mathrm{~S}$ denotes the initial resource state nodes which are occupied by the attacker.
- $A=\left\{a_{i} \mid i=1, \ldots, N\right\}$ represents a set of attack behavior nodes.
- $E=\left\{E_{1} \cup E_{2}\right\}$ denotes a set of directed edges connecting all related nodes. $E_{1} \subseteq S \times A$ means that the attack will be occurred only if one attacker occupies some resources; $E_{2} \subseteq A \times S$ means that the attack can make this attacker occupy some resources. Its parent nodes set $m$ is denoted as $\operatorname{Pre}(m)$, and the child nodes set $m$ is denoted as $\operatorname{Nex}(m)$.
- $\Gamma$ is the node state discriminant function. $\Gamma(x)$ denotes the current status of the node $x$ and $\Gamma(x) \in\{1,0\}$, where $\Gamma\left(s_{i}\right)$ means the current status of $s_{i} . \Gamma\left(s_{i}\right)=1$ indicates that the attacker has occupied the resource $s_{i}$. Conversely, 0 indicates that the attacker has not occupied the resource.
- $L$ is the logical relationships set between nodes, and $L=\{$ and, or, ble $\}$. There is an and relationship between $\operatorname{Pre}\left(a_{i}\right)$ only if all preconditions for the corresponding attack node $a_{i}$ are met. And a successful attack will enable $\Gamma\left(s_{i}\right)=1$ only if the attacker has occupied the resource $s_{i}$. There is an or relationship between attack nodes when resource state nodes are child nodes. Finally, ble denotes a kind of chaotic logical relationship which exists between parent nodes.
- $O=\left\{o_{i} \mid i=1,2,3, \ldots, N\right\}$ represents the set of resource state nodes associated with those successful attacks which have been detected. For $\forall o_{i} \in S, o_{i}$ represents the resource state nodes associated with the successful attacks are detected by IDS.

Definition 2 Attack path: In the RAG, if there exists a status sequence $s_{0}, a_{0}, s_{1}, a_{1}, \ldots, a_{n-1}, s_{n}$, where $s_{0}$ represents the initial node of resource state and $s_{n}$ represents the target node. So the Path $_{k}=<s_{0} \rightarrow a_{0} \rightarrow s_{1} \rightarrow a_{1} \rightarrow \ldots \rightarrow a_{n-1} \rightarrow s_{n}>$ can be defined, where $\forall s_{i} \in S, \forall a_{j} \in A$ $(0 \leq i \leq n, 0 \leq j \leq n-1)$; The Path $_{k}$ denotes the attack path $\mathrm{k}_{\mathrm{th}}$.

Definition 3 Attack behavior: One attack behavior can be denoted by a four-tuple of the form (Src_id,Dst_id,Att_code, Res), where Src_id denotes the host id launching an attack, Dst_id denotes the host id which has been attacked, Att_code is the number which can identify attack behaviors, and Res is the result of this attack.

Definition 4 State transition: One state transition is denoted by a three-tuple of the form (sid, vid, r), where sid is the number which can identify state transitions, vid is the number which identify vulnerabilities used by attackers, and $r$ is the resulting state transition which is caused by one attack using vulnerabilities.

# 4 The Algorithm E-Loop 

### 4.1 The Method of Metrics

To remove loops in an attack graph, an attack difficulty metric is introduced. In the Common Vulnerability Scoring System (CVSS), three basic indexes are used to characterize vulnerabilities: the access vector index, the access complexity index, and the authentication index, which are denoted by Acc_com, Acc_vec and Auth respectively. The values of these indexes associated with different levels of severity of a vulnerability are shown in Tab. 1.

Table 1: Index levels


Based on these indexes, the availability score of a vulnerability used in the CVSS is defined as
$\operatorname{Exp}=20 \times \operatorname{Acc} . . v e c \times \operatorname{Acc} . . \operatorname{com} \times$ Auth $(0 \leq E x p \leq 10)$
An attack becomes more difficult to perform successfully as the value of Exp gets smaller. Thus, the attack difficulty is inversely proportional to the availability of a vulnerability. Accordingly, an attack difficulty metric Aga_Dif may be defined based on the above three indexes as shown in Eq. (2). The larger the value of Aga_Dif is for a particular node, the more difficult the node is to attack.
Aga_Dif $=\frac{1}{2 \text { Acc_vec } \times \text { Acc_com } \times \text { Auth }}(A g a \_D i f \geq 1)$

# 4.2 The Algorithm E-Loop 

In the generation of the RAG, a loop may arise that leads to repeated traversals over a given node. It has a great influence on Bayesian probability calculation in network security assessment. In order to overcome the problem, the algorithm E-Loop is proposed to eliminate loops in the RAG. The specific steps are as follows:

Algorithm 1: $E-\operatorname{Loop}(R A G)$

## Input: $R A G$

Output: Acyclic RAG ( $A c \_R A G$ )
Step 1 Start nodes are added to the queue of the root node.
Step 2 All loops found are stored in the initialization stack: Init().
Step 3 Carry out a depth-first traversal from the begining node and then traverse every node: $\operatorname{root}=\operatorname{GetRoot}()$.
Step 4 Push every visited node into the stack: PushStack(root). Until all nodes are traversed or the currently traversed node has been traversed. Finally, a loop has been stored in the stack.
Step 5 In the loop, Aga_Dif, of every node must be calculated, and the node attacked most difficultly can be found: $S_{m}=\operatorname{Max}\left(\right.$ Aga_Dif $\left._{i}\right)$.
Step 6 Delete $S_{m}$ to eliminate the loop: Delete $\left(S_{m}\right)$.
Step 7 Loop through Step3- Step6 until there is no loop in the RAG.
Step 8 Output $A c \_R A G$.
Fig. 1 shows an RAG built as described above. There are two loops, Path $1=\left\langle s_{2} \rightarrow a_{3} \rightarrow s_{5} \rightarrow a_{5} \rightarrow s_{2}\right\rangle$ and Path $2=\left\langle a_{9} \rightarrow s_{11} \rightarrow a_{12} \rightarrow s_{12} \rightarrow a_{9}\right\rangle$. For Path 1 , the node $a_{5}$ will be eliminated by the algorithm $E-$ Loop to remove the loop; For Path 2 , node $a_{9}$ can never be reached because of Aga_Dif $\left(a_{9}\right) \rightarrow \infty$, so this loop can be removed by eliminating this node and all subsequent nodes. Fig. 2 shows the acyclic RAG (Ac_RAG) obtained after the loops are eliminated by the E-Loop algorithm.

![img-0.jpeg](img-0.jpeg)

Figure 1: RAG
![img-1.jpeg](img-1.jpeg)

Figure 2: Acyclic RAG

# 5 Probability Calculation in the B_NAG Model 

In the B_NAG, the probability of each node is only constrained by its parent nodes, and the node remains conditionally independent of the others. In the RAG, the transition of node state is only correlated to whether the relevant resource has been occupied or not. A child node can occur a state transition only if its parent nodes are occupied. Thus, the state transition needs be associated with conditional independence in the B_NAG.

Tab. 2 presents the corresponding relationship between an Ac_RAG and a B_NAG. Although these graphs have corresponding structures, differences exist in their certain nodes. The detailed implementation described below is based on a B_NAG.

Table 2: Corresponding relationship


# 5.1 Implementation of the B_NAG Model 

Definition 5 The resulting resource state node and the conditional resource state node: The resource state node where the attack has been occurred successfully is called the resulting resource state node; When the attack condition is satisfied, the required resource state node is called the conditional resource state node.

Definition $6 W=\left\{w_{i j} \mid i, j=1,2, \ldots, N\right\}$, the set of weights between the resource state nodes: $W$ is represented in the form of two-tuples $(\operatorname{depcoef}, \cos t)$ ), where depcoef denotes the correlation coefficient between resource state nodes and $\cos t$ denotes the cost required to attack another resource state node from the current node. $w_{i j}$ is the weight value between the node $s_{i}$ and the node $s_{j}$.

As illustrated in the example shown in Fig. 2, an RAG consists of four structures: a series structure, a parallel or structure, a parallel and structure, and a mixed structure. While converting such a graph into a B_NAG, each of these structures can be transformed as follows:
(1) Series structure: By deleting the attack behavior node $a_{1}$, the attack behavior can be represented by the directed edge from $s_{1}$ to $s_{2}$ :
$\left(s_{1} \rightarrow a_{1} \rightarrow s_{2}\right) \Rightarrow\left(s_{1} \rightarrow s_{2}\right)$
(2) Parallel or structure: The nodes $a_{10}$ and $a_{11}$ exist an or relationship, meaning that the attack is able to occur when the resource state condition corresponding to either of the parent nodes $s_{9}$ or $s_{10}$ can be satisfied. The related attack behavior nodes are removed. And the resulting resource state node and the conditional resource state node can be linked by one directed edge. In the B_NAG, the resource state nodes have an or relationship:
$\left(s_{9} \rightarrow a_{10}, s_{10} \rightarrow a_{11}, a_{10} \vee a_{11} \rightarrow s_{12}\right) \Rightarrow\left(s_{9} \vee s_{10} \rightarrow s_{12}\right)$
(3) Parallel and structure: The parent nodes $s_{2}$ and $s_{3}$ of $a_{3}$ have an and relationship, meaning that the attack behavior may occur only if all resource state conditions are satisfied. After the attack node is removed, and the resulting resource state node and the conditional resource state nodes can be linked by one directed edge, which represents the attack behavior. In the transformed B_NAG, the resource state nodes still have an and relationship:
$\left(s_{2} \wedge s_{3} \rightarrow a_{3} \rightarrow s_{5}\right) \Rightarrow\left(s_{2} \wedge s_{3} \rightarrow s_{5}\right)$
(4) Mixed structure: The parent nodes $s_{6}$ and $s_{4}$ of the node $a_{6}$ have an and relationship, and the two nodes $a_{6}$ and $a_{7}$ that can get to the resulting resource state node have an or relationship. If the node $a_{6}$ is directly removed, the structure of the RAG will become confusing, causing inconvenience in the

conditional probability calculation. In order to solve the problem, this paper defines a temporary mixed nodeblend; namely, the node $a_{6}$ is denoted as the node blend:

$$
\left(s_{6} \wedge s_{4} \rightarrow a_{6}, a_{6} \vee a_{7} \rightarrow s_{9}\right) \Rightarrow\left(s_{6} \wedge s_{4} \rightarrow \text { blend, blend } \vee s_{7} \rightarrow s_{9}\right)
$$

After this conversion process, each edge in the converted $\mathrm{B} \_$NAG represents an attack behavior and has a weight that describes the correlation between the two resource state nodes connected by that edge. It can be observed from the converted $\mathrm{B} \_$NAG shown in Fig. 3 that blend is a mixed resource state node representing the combination of $s_{4}$ and $s_{6}$, so there must be directed edges from $s_{4}$ and $s_{6}$ to blend, namely, $P($ blend $] s_{4}, s_{6})=1$. The relationships between the nodes do not change upon conversion into a $\mathrm{B} \_$NAG, and only the resource state nodes will be included. All attack behaviors are represented by the directed edges of the $\mathrm{B} \_$NAG, and the only possible relationships are and and or.
![img-2.jpeg](img-2.jpeg)

Figure 3: B_NAG
To clarify the process, the conversion algorithm is proposed as follows.
Algorithm 2: Attack graph conversion algorithm, $\operatorname{Alg}-\operatorname{AGTrans}(A c_{-} R A G)$

```
Input: \(A c_{-} R A G\)
Output: B_NAG
1. For each \(\mathrm{s}_{\mathrm{i}} \in \mathrm{S}\) AND \(\mathrm{a}_{\mathrm{i}} \in \mathrm{A}\)
2. IF \(\operatorname{DPre}\left(\mathrm{s}_{\mathrm{i}}\right) \neq \varnothing\) AND IF \(\operatorname{DPre}\left(a_{i}\right) \neq \varnothing\)
3. Else If \(\operatorname{Num}\left(\operatorname{DPre}\left(\mathrm{a}_{\mathrm{i}}\right)\right)=1\) AND \(\operatorname{Num}\left(\operatorname{DPre}\left(\operatorname{DNex}\left(\mathrm{a}_{\mathrm{i}}\right)\right)\right)=1\);
4. \(\mathrm{e}_{\mathrm{ij}}=\left\langle\mathrm{s}_{\mathrm{i}}, \operatorname{DNex}\left(\mathrm{a}_{\mathrm{i}}\right)>\right\rangle / /\) the edge \(\mathrm{e}_{\mathrm{ij}}\) links two nodes
5. \(\mathrm{e}_{\mathrm{ij}} \leftarrow \mathrm{W}(\mathrm{i}, \mathrm{j}) ;\)
6. Delete \(\left(\mathrm{a}_{\mathrm{i}}\right) ; / /\) delete the attack node
7. Else If \(\operatorname{Num}\left(\operatorname{DPre}\left(\mathrm{a}_{\mathrm{i}}\right)\right)>1\)
8. \(\mathrm{e}_{\mathrm{ij}}=\left\langle\operatorname{DPre}\left(\mathrm{a}_{\mathrm{i}}\right), \operatorname{DNex}\left(\mathrm{a}_{\mathrm{i}}\right)>\right\rangle / /\) there are many incoming edges here
9. \(\mathrm{e}_{\mathrm{ij}} \leftarrow \mathrm{W}(\mathrm{i}, \mathrm{j}) ;\)
10. Delete \(\left(\mathrm{a}_{\mathrm{i}}\right) ;\)
11. The relationship of \(\forall \mathrm{e}_{\mathrm{ij}}\) is AND;
12. Else If \(\operatorname{Num}\left(\operatorname{DPre}\left(\mathrm{s}_{\mathrm{i}}\right)\right)>1\)
13. \(\mathrm{e}_{\mathrm{ij}}=\left\langle\operatorname{DPre}\left(\operatorname{DPre}\left(\mathrm{s}_{\mathrm{i}}\right)\right), \mathrm{s}_{\mathrm{i}}\right\rangle\);
```

14. $\mathrm{e}_{\mathrm{ij}} \leftarrow \mathrm{W}(\mathrm{i}, \mathrm{j})$;
15. Delete $\left(\operatorname{DPre}\left(\mathrm{s}_{\mathrm{i}}\right)\right)$;
16. The relationship of $\forall \mathrm{e}_{\mathrm{ij}}$ is OR.
17. Else If $\operatorname{DPre}\left(\mathrm{a}_{\mathrm{i}}\right)>1$ AND $\operatorname{Num}\left(\operatorname{DPre}\left(\operatorname{Nex}\left(\mathrm{a}_{\mathrm{i}}\right)\right)\right)>1$
18. $\mathrm{a}_{\mathrm{i}} \in \mathrm{Ble} ; \mathrm{a}_{\mathrm{i}}=$ blent; // introduction of a mixed node blend;
19. $\mathrm{e}_{\mathrm{ij}}=\langle\operatorname{DPre}($ blent $)$, blent $\rangle$;
20. $\mathrm{e}_{\mathrm{ij}} \leftarrow \mathrm{W}(\mathrm{i}, \mathrm{j})$;
21. The relationship of $\forall \mathrm{e}_{\mathrm{ij}}$ is AND;
22. $\mathrm{e}_{\mathrm{ij}}=\langle$ blent, $\operatorname{DNex}($ blent $)>\mid$
23. $\mathrm{e}_{\mathrm{ij}} \leftarrow \mathrm{W}(\mathrm{i}, \mathrm{j})$;
24. The relationship of $\forall \mathrm{e}_{\mathrm{ij}}$ is OR.
25. End If;
26. Go to For;
27. Return B_NAG;

# 5.2 Calculation of the Probability of Reaching a Node Based on the B_NAG 

The direct parent nodes of node $S$ are denoted here by $D \operatorname{Pre}(S)$, and the attack probability $P_{a}(S)$ of the target node can be calculated:

$$
\begin{aligned}
P_{a}(S) & =P(S \mid \operatorname{Pr} e(S)) P(\operatorname{Pr} e(S)) \\
& =P(S \mid D \operatorname{Pr} e(S)) P(D \operatorname{Pr} e(S))
\end{aligned}
$$

The state transition index $P_{m}\left(\cos t_{i}\right)$ can be denoted as the probability of the conversion from $S_{i-1}$ to $S_{i}$. Because of the correlation between one resource and its parent nodes, the weights $W$ must be considered when the state transition indexes of the parent nodes are calculated. If a sufficiently high cost is paid, the attack will be guaranteed to be accomplished; namely, if $\cos t \rightarrow \infty$, then $P_{m}(\cos t)=1$. If no cost is afforded, any target can't be attacked successfully; that is, when $\cos t=0, P_{m}(\cos t)=0$. If an attack on a node fails, the state of this node remains unchanged. For the state transition index $P_{m}\left(\cos t_{i}\right)$, its value follows a certain distribution. Thus, $P_{m}\left(\cos t_{i}\right)$ is calculated as follows:
$P_{m}\left(\cos t_{i}\right)=P\left(\cos t_{i}<\operatorname{Cos} t\right)=1-e^{-d e p c o e f \times \cos t_{i}}$
Here, $\cos t$ refers to the cost required to perform an attack, that is, the knowledge, experience, and resources needed to complete the attack. $\operatorname{Cos} t$ means the average cost required to complete the final attacks; it's a default value and relies on the resources, knowledge, attack tools and time. depcoef is the correlation degree:
depcoef $=\frac{1}{\text { Aga.Dif }}(0<$ depcoef $<1)$
Accordingly, the state transition index $P_{m}\left(\cos t_{i}\right)$ is calculated as
$P_{m}\left(\cos t_{i}\right)=1-e^{-\frac{\cos t_{i}}{A g a_{-} D i f}}$
It can be concluded from Eq. (6) that resource state nodes in the B_NAG interact with each other, so the probability of reaching a given node cannot be analyzed only by traditional inference in the vulnerability analysis; instead, these state transitions must also be considered deeply. To solute this problem, the index of state transition is used to consider the probability of node state transitions when assessing vulnerabilities of the network. $P_{\text {end }}$ denotes the probability of reaching a target node:

$$
\begin{aligned}
P_{\text {end }}\left(s_{i}\right) & =P_{m}\left(\cos t_{i}\right) \times P_{a}\left(s_{i}\right) \\
& =\left(1-e^{-\frac{\cos t_{i}}{A g a_{-} D i f}}\right) \times P\left(s_{i} \mid D \operatorname{Pr} e\left(s_{i}\right)\right) P\left(D \operatorname{Pr} e\left(s_{i}\right)\right)
\end{aligned}
$$

Here, $P_{m}\left(\cos t_{i}\right)$ is the state transition index of the target node $s_{i} ; \cos t$ and depcoef are the attack cost and the correlation degree between node $s_{i}$ and its parent nodes, respectively; and $P_{a}\left(s_{i}\right)$ denotes the Bayesian probability of $s_{i}$ is attacked. Eq. (7) gives the probability of reaching a single target node; the probability of reaching a whole path will be obtained by iterating Eq. (7) accordingly. The related iterative algorithm is provided below.

In Algorithm 3, all nodes are traversed firstly. The parent nodes $\operatorname{Pre}\left(s_{i}\right)$ are pushed onto their respective stack $q$ in accordance with the number of direct parent nodes $D \operatorname{Pre}\left(s_{i}\right)$ of $s_{i}$, and it must make sure that the start node in the path of $D \operatorname{Pre}\left(s_{i}\right)$ is finally pushed onto $q$. Then, the nodes are each removed in proper order based on the "last in first out" principle, and their reachability probability can be calculated to finally determine the whole path's probability being reached.

Algorithm 3: Iterative algorithm for calculating the probability of reaching a whole path in a graph, IterAlg $-\operatorname{ReaPro}(B \_N A G, W)$

Input: converted $B_{-} N A G$ and weights $W=($ depcoef, $\cos t)$ between nodes
Output: final probability of an attack reaching the whole path $P_{\text {end }}\left(s_{i}\right)$

1. For each $\mathrm{s}_{\mathrm{i}} \in \mathrm{S}$
2. Number of Count $=\operatorname{DPre}\left(\mathrm{s}_{\mathrm{i}}\right)$;
3. $\operatorname{InitStack}(\& q)$;
4. for each $\operatorname{DPre}\left(\mathrm{s}_{\mathrm{i}}\right) \in \mathrm{S}$ And $\operatorname{DPre}\left(\mathrm{s}_{\mathrm{i}}\right) \neq \varnothing$
5. root $=\operatorname{DPre}\left(\mathrm{s}_{\mathrm{i}}\right) ; / /$ number of direct parent nodes of the target node
6. Push Stack(root) $\rightarrow \mathrm{q}$;
7. End for
8. End for
9. For $\mathrm{q} \neq \varnothing$
10. $\mathrm{s}_{\mathrm{i}}=$ PopStack(root);
11. $P a=P a\left(s_{i}\right)$;
12. $\mathrm{P}_{\mathrm{m}}=\mathrm{P}_{\mathrm{m}}\left(\cos \mathrm{t}_{\mathrm{dpre}(\mathrm{si})}\right)$;
13. $\mathrm{P}_{\text {end }}=\mathrm{P}_{\mathrm{a}} \times \mathrm{P}_{\mathrm{m}}$;
14. End for;
15. return $\mathrm{P}_{\text {end }}$;

In the example shown in Fig. 3, if $s_{12}$ is attacked, it is obvious that the attack target can be accomplished by the below three paths:
$\operatorname{Path}_{1}=\left\langle s_{1} \rightarrow s_{2} \rightarrow s_{6} \rightarrow \operatorname{blend}\left(s_{6} \wedge \mathrm{~s}_{4}\right) \rightarrow s_{9} \rightarrow s_{12}\right\rangle$
$\operatorname{Path}_{2}=\left\langle\mathrm{s}_{4} \rightarrow s_{7} \rightarrow s_{9} \rightarrow s_{12}\right\rangle$
$\operatorname{Path}_{3}=\left\langle\mathrm{s}_{4} \rightarrow s_{7} \rightarrow s_{10} \rightarrow s_{12}\right\rangle$
If the weights W, the values of depcoef and the attack costs are shown in Fig. 3, then the prior probabilities of $s_{4}$ and $\mathrm{s}_{1}$ are 0.3 and 0.2 , respectively. For instance, the related steps for $\operatorname{Path}_{1}$ are described below:
$P\left(s_{2}\right)=P_{m}\left(\cos t_{1}\right) \times P_{a}\left(s_{2}\right)=P_{m}\left(\cos t_{1}\right) \times P\left(\Gamma\left(s_{2}\right)=1 \mid \Gamma\left(s_{1}\right)=1\right) \times P\left(s_{1}\right)=0.0866$
$P\left(s_{6}\right)=P_{m}\left(\cos t_{2}\right) \times P_{a}\left(s_{6}\right)=P_{m}\left(\cos t_{2}\right) \times P\left(\Gamma\left(s_{6}\right)=1 \mid \Gamma\left(s_{2}\right)=1\right) \times P\left(s_{2}\right)=0.0684$
$P($ blend $)=P_{m}\left(\cos t_{6}\right) \times P\left(\Gamma(\right.$ blend $)=1 \mid \Gamma\left(s_{6}\right)=1, \Gamma\left(s_{4}\right)=1) \times P\left(s_{6}\right) \times P\left(s_{4}\right)=0.0382$
In a similar way, the following is obtained from Eq. (7): the reachability probabilities of $s_{9}$ and $s_{12}$ by following $\operatorname{Path}_{1}$ are $P\left(s_{9}\right)=0.0272$ and $P_{\text {end }}\left(s_{12}\right)=0.0201$, respectively; the reachability probability of $s_{12}$ by following $\operatorname{Path}_{2}$ is $P_{\text {end }}\left(s_{12}\right)=0.0648$; and the reachability probability of $s_{12}$ by following $\operatorname{Path}_{3}$ is $P_{\text {end }}\left(s_{12}\right)=0.0573$. If the administrator knows that $a_{1}$ has been targeted, namely, $P\left(s_{1}\right)=1$, then the reachability probability of $s_{12}$ by following $\operatorname{Path}_{1}$ can be recalculated as $P_{\text {end }}\left(s_{12}\right)=0.0631$. This indicates that when the resource state condition corresponding to $s_{1}$ is met, $s_{12}$ is more possible to be attacked, which is the same as expected.

# 5.3 Posterior Probability Calculation Based on the B_NAG 

In a B_NAG, it is not possible to monitor changes in the network security conditions in real time when the probabilities of resource state nodes attacked by attackers are calculated. Based on the detected the precondition and the available information of security incidents, the posterior probabilities should be calculated, and these related node probabilities can then be updated to achieve real-time monitoring. The equation for calculating a posterior probability is as follows:

$P_{o}\left(S_{i} \mid O\right)=\frac{P\left(O \mid S_{i}\right) \times P\left(S_{i}\right)}{P(O)}$
Suppose that $O_{1}$ in Fig. 3 can be detected, and the probability of $s_{12}$ is 1 . Then, the posterior probability of $s_{9}$ is calculated as follows by Eq. (8).

$$
\begin{aligned}
P_{o}\left(s_{9} \mid s_{12}\right) & =P\left(s_{12} \mid s_{9}\right) \times P\left(s_{9}\right) / P\left(s_{12}\right) \\
& =\left(P\left(s_{12}, s_{10} \mid s_{9}\right)+P\left(s_{12},{ }^{\wedge} s_{10} \mid s_{9}\right)\right) \times P\left(s_{9}\right) / P\left(s_{12}\right) \\
& =\left(P\left(s_{12} \mid s_{10}, s_{9}\right) \times P\left(s_{10} \mid s_{9}\right)+P\left(s_{12} \mid{ }^{\wedge} s_{10}, s_{9}\right) \times P\left({ }^{\wedge} s_{10} \mid s_{9}\right)\right) / P\left(s_{12}\right) \\
& =\left(P\left(s_{12} \mid s_{10}, s_{9}\right) \times P\left(s_{10}\right)+P\left(s_{12} \mid{ }^{\wedge} s_{10}, s_{9}\right) \times P\left({ }^{\wedge} s_{10}\right)\right) / P\left(s_{12}\right) \\
& =0.082
\end{aligned}
$$

In this case, the probability of reaching node $s_{9}$ changes from 0.0272 to 0.082 . When certain attacks occur, the corresponding posterior probabilities in the $\mathrm{B}_{-} \mathrm{NAG}$ can effectively discover the potential risk. The real-time calculation of the risk values of nodes in the $\mathrm{B}_{-} \mathrm{NAG}$ is of great significance for the assessment of vulnerabilities.

# 6 Experimental Analysis 

### 6.1 Experimental Network Environment

To verify that the given method is feasible and effective, the experimental environment shown in Fig. 4 was created. The experimental network includes five hosts: the attacking machine, a web server, a file server, an e-mail server, and a database server. For ease of description, these hosts are represented by the letters A, W, F, E and D, respectively. W opens the telnet service, F opens the File Transfer Protocol (FTP) service, E opens the FTP and Hypertext Transfer Protocol (HTTP) services, and D opens the Oracle service. The final aim of attacker A is to obtain root permissions for host D , but the firewall allows the foreign host A access to only the telnet service of host D and denies other external access. Similarly, host E is allowed access to only the Oracle service of host D , while the other three hosts can openly gain access to each other's services. Host W can directly access host E ; when it obtains access to the two services provided by host E , it can, in turn, gain direct access to the Oracle service of host D .
![img-3.jpeg](img-3.jpeg)

Figure 4: Topological graph of the experimental network

Information about the internal host is shown in Tab. 3.

Table 3: Information about the internal host


# 6.2 Experimental Results and Analysis 

After loops have been removed as previously described during the generation of the RAG in accordance with the attack graph model and the topological graph of the experimental network, the corresponding descriptions of the attack behavior nodes are as shown in Tab. 4. These attacks are related to the services provided by the hosts and their vulnerabilities.

Table 4: Attack behavior information of the experimental attack graph


After the application of the conversion algorithm based on the topological graph of the experimental network to replace the attack behavior nodes mentioned in Tab. 4 with corresponding edges, the converted B_NAG is as shown in Fig. 5.

As shown in Fig. 5, each host node must win the trust of another host through a service provided by that other host, corresponding to a parallel "and" structure in the graph. When one host opens two services, the trust of that host can be obtained by gaining access to either one of its services, so the relationship between the possible attacks against that host is "or". A node with a mixed relationship can directly access the service provided by another host by crossing over the host it is attacking once it gains access to both services of the target host. A blend node is introduced to address the corresponding mixed relationship in this graph.

There are 5 paths in Fig. 5 through which the target host D can be reached. The attack path information and the probabilities of reaching each whole path are shown in Tab. 5. $\mathrm{P}_{1}$ denotes the probability of reaching the whole path as calculated by considering the state transition index as proposed in this paper, while $\mathrm{P}_{2}$ is the probability of reaching the whole path calculated without considering the state transition index.

Based on Tab. 5, the probability of reaching each host node is plotted in Fig. 6.
As shown in Fig. 7, the hosts attacked on Path1 and Path2 (and on Path3 and Path4) are the same; the only difference lies in the service of host E that is accessed. Path1 accesses the FTP service of host E, while Path2 accesses the HTTP service of host E. The final probabilities of reaching the whole path for Path1 and

Path2 are 0.03247 and 0.05784 , respectively, as calculated using the proposed algorithm based on the state transition index. Obvious differences can be seen between the two paths in terms of the probability of the attack successfully proceeding from host F to host E , as shown in Fig. 7a. By contrast, when the state transition index is not considered, the final probabilities for Path1 and Path2 are 0.4768 and 0.4789 , respectively, and there is no meaningful difference in the probability of proceeding from host F to host E , as shown in Fig. 7b. With the proposed algorithm, although the reference value of the probability for each node decreases, the differences in probability associated with attacking different nodes are fully apparent. Therefore, this approach is effective in enabling network security administrators to perform useful analyses.
![img-4.jpeg](img-4.jpeg)

Figure 5: Example of a Bayesian network attack graph

Table 5: Attack path information for the example graph


![img-5.jpeg](img-5.jpeg)

Figure 6: Path probabilities under $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$ (a) $\mathrm{P}_{1}$ (b) $\mathrm{P}_{2}$
![img-6.jpeg](img-6.jpeg)

Figure 7: Probabilities of $\mathrm{Path}_{1,2}$ under $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$ (a) $\mathrm{P}_{1}$ (b) $\mathrm{P}_{2}$
As shown in Fig. 8, the traditional computational method for Path5, which includes a mixed relationship, is to calculate all "and" nodes and "or" nodes individually. This not only requires a large number of calculations but also ignores the correlations between nodes.
![img-7.jpeg](img-7.jpeg)

Figure 8: Probability of $\mathrm{Path}_{5}$ under $\mathrm{P}_{1}$ and $\mathrm{P}_{2}$ (a) $\mathrm{P}_{1}$ (b) $\mathrm{P}_{2}$

The mixed node approach introduced herein provides better calculation results than the traditional method, and it does so with fewer calculations. For the mixed relationship identified when host W attempts to gain access to host E, the probability calculated by considering the state transition index effectively reflects the degree of hazard of the associated vulnerability, making this type of vulnerability more likely to be noticed by the network security administrator.

# 7 Conclusion 

Improving the accuracy of network vulnerability assessments is an important topic in the field of network security. This paper presents a B_NAG model and an associated vulnerability algorithm as well as the algorithm E-Loop to eliminate loops in an attack graph. To effectively capture mixed relationships between nodes during the process of converting a RAG into a B_NAG, the Alg-AGTrans algorithm is also proposed. In addition, the indexes of node attack complexity and node state transition are introduced into the calculation of the probability of reaching each node, and the posterior probabilities are also calculated on this basis. The results of an experimental evaluation show that the model proposed herein can provide an accurate and effective assessment of network vulnerability. However, the proposed algorithm also has some shortcomings that should be addressed. For example, the effects of some factors, such as risk costs, are not considered when calculating the probability of reaching a node.

Funding Statement: This work was partially supported by the National Natural Science Foundation of China (61300216, Wang, H, www.nsfc.gov.cn).

Conflicts of Interest: The authors declare that they have no conflicts of interest to report regarding the present study.
