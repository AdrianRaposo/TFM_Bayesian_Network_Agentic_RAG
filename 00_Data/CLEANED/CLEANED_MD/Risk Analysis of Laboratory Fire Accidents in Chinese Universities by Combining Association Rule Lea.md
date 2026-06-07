# Article 

## Risk Analysis of Laboratory Fire Accidents in Chinese Universities by Combining Association Rule Learning and Fuzzy Bayesian Networks

Fuqiang Yang ${ }^{1,2, *}$, Xin Li ${ }^{1}$, Shuaiqi Yuan ${ }^{3, * *}($ and Genserik Reniers ${ }^{3,4,5}$

## check for updates

Citation: Yang, F.; Li, X.; Yuan, S.; Reniers, G. Risk Analysis of Laboratory Fire Accidents in Chinese Universities by Combining Association Rule Learning and Fuzzy Bayesian Networks. Fire 2023, 6, 306. https: / / doi.org/10.3390/fire6080306

Academic Editors: Fei Wang and Siu Ming Lo

Received: 7 July 2023
Revised: 1 August 2023
Accepted: 4 August 2023
Published: 7 August 2023

## (0)

Copyright: (c) 2023 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 College of Environment and Safety Engineering, Fuzhou University, Fuzhou 350116, China
2 Fujian Provincial Key Laboratory of Remote Sensing of Soil Erosion and Disaster Prevention, Fuzhou University, Fuzhou 350116, China
3 Safety and Security Science Section, Faculty of Technology, Policy and Management, Delft University of Technology, 2628 BX Delft, The Netherlands
4 Antwerp Research Group on Safety and Security (ARGoSS), Faculty of Applied Economics, University of Antwerp, 2000 Antwerp, Belgium
5 Center for Economics and Corporate Sustainability, Katholieke Universiteit Leuven, 1000 Brussels, Belgium

* Correspondence: yangfuqiang@fzu.edu.cn (F.Y.); s.yuan-2@tudelft.nl (S.Y.)

Abstract: Targeting the challenges in the risk analysis of laboratory fire accidents, particularly considering fire accidents in Chinese universities, an integrated approach is proposed with the combination of association rule learning, a Bayesian network (BN), and fuzzy set theory in this study. The proposed approach has the main advantages of deriving conditional probabilities of BN nodes based on historical accident data and association rules (ARs) and making good use of expert elicitation by using an augmented fuzzy set method. In the proposed approach, prior probabilities of the cause nodes are determined based on expert elicitation with the help of an augmented fuzzy set method. The augmented fuzzy set method enables the effective aggregation of expert opinions and helps to reduce subjective bias in expert elicitations. Additionally, an AR algorithm is applied to determine the probabilistic dependency between the BN nodes based on the historical accident data of Chinese universities and further derive conditional probability tables. Finally, the developed fuzzy Bayesian network (FBN) model was employed to identify critical causal factors with respect to laboratory fire accidents in Chinese universities. The obtained results show that H4 (bad safety awareness), O1 (improper storage of hazardous chemicals), E1 (environment with hazardous materials), and M4 (inadequate safety checks) are the four most critical factors inducing laboratory fire accidents.

Keywords: laboratory fire accidents; Bayesian network; association rules; fuzzy set theory; fire safety

## 1. Introduction

University laboratories are important sites for educational and scientific activities, and meanwhile, some of them inevitably accommodate hazardous and flammable materials. Experimenters are usually threatened by physical, chemical, or biological threats in university labs [1], and this should be given enough attention from the public and academia. Previous research shows that university laboratories normally have laxer safety management and lower safety investment compared to industrial laboratories [2,3]. As a result, safety risks in some university laboratories are not well evaluated and treated. The frequent occurrence of university laboratory accidents, particularly the happening of lab fires in Chinese universities, has induced severe disastrous consequences. For example, a fire and explosion happened in a laboratory of the Beijing Jiao Tong University on 26 December 2018, and three people died in this accident. A deflagration happened in a laboratory of the Nanjing University of Aeronautics and Astronautics on 24 October 2021, causing two fatalities and nine injuries. Safety risk assessment and safety risk management are effective

tools that can be implemented to prevent undesired accidents and mitigate the corresponding consequences [4,5]. However, current research on the risk analysis of laboratory fire accidents is still lacking to boost the safety risk management of university laboratories. The development of new approaches for risk analysis of laboratory fire accidents and further improvement of safety risk management of university laboratories is urgently needed.

Previous studies have developed different risk analysis methods to investigate safety issues in laboratories [6,7,8]. However, those studies mainly focused on specific experiments [9], and a generic risk analysis model for university laboratory fire accidents is lacking. In previous studies, risky behaviors [10], safety policies [11], and chemicals [12] were considered influencing factors in the safety risk analysis of laboratory accidents. However, the dependency between those influencing factors has not been analyzed to serve a comprehensive and systematic risk assessment. Thus, a thorough identification and evaluation of the causal factors leading to university laboratory fire accidents should be performed, and the interdependency between those factors should be well addressed in the risk analysis. The Bayesian network (BN) is one of the widely used methods for safety risk analysis. BNs are able to combine probability theory and graph theory for uncertain event analysis and inference [13,14]. At present, a large number of studies have used BN models for risk analysis and casual factor identification [15,16,17,18]. For instance, Aliabadi et al. [19] assessed the gas leakage risks of storage tanks by using a BN model, and the results show that human factors are the most critical influencing factors. Wang et al. [20] constructed a risk analysis model for a phased task system based on BNs. Li et al. [21] evaluated explosion risks with respect to the aluminum production process by employing BNs, and five main causes were identified afterward. Hao and Hadjisophocleous [22] developed a BN model to estimate the probabilities of fire spreading and evaluated the corresponding fire risks. Li et al. [23] performed a risk analysis of hazardous chemical explosions by integrating BNs and association rules.

Additionally, the treatment of subjectivity and uncertainties should be well addressed in the risk analysis because it significantly influences the risk assessment results. Typically, the implementation of fuzzy set theory is able to facilitate the expert elicitation process by representing probabilities in the form of fuzzy languages. Additionally, the subjectivities and uncertainties in risk analysis may also be reduced by incorporating data-driven approaches. For instance, Nhat et al. [24] created a BN model combining a data-driven approach to improve the accuracy of the model's prediction with the help of historical data analysis. Lieng [25] combined a data-driven approach and BNs to reduce the uncertainties in risk modeling. Previous studies also show that the implementation of association rules (ARs) helps to identify and depict the probabilistic relationships between associated events/factors [26,27,28,29]. As a result, ARs are widely used for the data mining of accidental factors, particularly in the maritime and construction sectors. For instance, ARs were applied to investigate the causal factors of vessel navigation accidents [30], tugboat accidents [31], and fishing vessel accidents [32]. In construction industries, Wang et al. [28] employed ARs to improve the effectiveness of hazard identification in workplaces. Cabello et al. [29] used ARs to identify the main influencing factors leading to accidents in the construction phases. Shao et al. [33] employed ARs to identify the causes of building collapse accidents. Those studies show that the application of ARs has the capability to identify and describe probabilistic relationships among associated factors, and further, it helps to develop BN models.

In order to fill the above-mentioned gaps in the risk analysis of university lab fire accidents, an integrated approach combining association rule learning and a fuzzy Bayesian network (FBN) is developed to perform a risk analysis of Chinese university laboratory fire accidents. The remainder of this paper is organized as follows: Section 2 demonstrates the overview of the proposed approach before illustrating each part (association rule learning, augmented fuzzy set theory, and the BN) of the proposed approach in detail. Section 3 demonstrates the detailed procedures of the application of the proposed approach to the risk analysis of a Chinese university laboratory regarding fire accidents. The risk assessment

results are discussed, and the limitations and recommendations for future works are given in Section 4. Finally, our conclusions are summarized in Section 5.

# 2. Overview of the Methodology 

### 2.1. Overall Framework

A hybrid model is developed by this study to perform a risk analysis of laboratory fire accidents and to answer two research questions: What factors may lead to laboratory fire accidents in Chinese universities? and What is the criticality of each factor? Figure 1 presents the overview of the proposed approach. Firstly, the causal factors of accidents are identified through an accident report analysis of accidents. Then, a BN model topology (directed acyclic graphs (DAGs)) should be developed to describe the causal relationships among those factors, which consists of three types of nodes, including cause category nodes (human, object, environment, and management), cause nodes, and the accident node. Furthermore, the prior probabilities of the cause nodes (root nodes of the BN model) are determined by using an augmented fuzzy theory method with the help of expert elicitation. Specifically, the augmented fuzzy theory is developed by combining the cut volume of $\alpha$ and the area center technique. The conditional probability tables of the BN nodes are determined based on the association rule learning approach with the help of historical accident data. Finally, a complete BN model is developed to perform a quantitative risk analysis of accidents, and the calculation of Fussel-Vesely (FV) values helps to identify the critical causal factors.
![img-0.jpeg](img-0.jpeg)

Figure 1. Flowchart of the proposed methodology.

### 2.2. Methodology

### 2.2.1. Bayesian Networks

BNs are probabilistic networks consisting of DAGs and conditional probability tables (CPTs). The joint probability distribution of a set of nodes $V=\left\{X_{1}, X_{2}, \cdots X_{n}\right\}$ can be expressed as Equation (1) [34].

$$
P\left(X 1, X_{2} \ldots X n\right)=\prod_{i=1}^{n} P(X i \mid P a(X i))
$$

where $\left\{X_{1}, X_{2}, \cdots X_{n}\right\}$ means all nodes of a BN, and $P a\left(X_{i}\right)$ denotes the parent set of node $X_{i}$. BNs employ the Bayes theorem to update the prior probabilities, called evidence, thus generating the posterior probabilities [35]:

$$
P\left(X_{j} \mid X_{i}\right)=\frac{P\left(X_{i}, X_{j}\right)}{P\left(X_{i}\right)}=\frac{P\left(X_{i} \mid X_{j}\right) \cdot P\left(X_{i}\right)}{\sum_{j} P\left(X_{i} \mid X_{i}\right) P\left(X_{i}\right)}
$$

It is critical to identify the important critical root nodes that cause the occurrence of the top event. Fussel-Vesely describes the contribution of the root event to the top event [36]. For a root event, $X_{i}$, the $F V$ can be calculated as [35,36]:

$$
F V=\frac{P(T E=\text { occur })-P\left(T E=\text { occur } \mid X_{i}=0\right)}{P(T E=\text { occur })}
$$

where $P(T E=$ occur $)$ refers to the probability of occurrence of the top event, $T$; $P\left(T=\right.$ occur $\left|X_{i}=0\right)$ refers to the probability of occurrence of the top event, T , when the $X_{i}$ event does not occur.

# 2.2.2. Augmented Fuzzy Set Theory Method 

The fuzzy set theory was proposed by Zadeh [37] to deal with imprecision and fuzzy problems. Generally, each fuzzy set is regulated by a membership function, $u(x)$, with a value domain, $U \in[0,1]$. The value solved by the membership function is called the degree of membership, i.e., the degree to which the elements belong to the fuzzy set [38]. A fuzzy number can be defined in different forms. The concept of linguistic variables is particularly helpful when handling situations that cannot be described quantitatively. In risk assessment, fuzzy quantifiers are employed to deal with the "probability of failure/occurrence". For instance, very low (VL), low (L), fairly low (FL), medium (M), fairly high (FH), high (H), and very high $(\mathrm{VH})$. The graphical representation of these linguistic values is presented in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Fuzzy numbers representing linguistic variables.
Basically, increasing the number of experts is an important way that helps to alleviate the bias in expert opinions. Meanwhile, the application of an augmented fuzzy theory method may also help to reduce bias in expert opinions with no need to increase the number of experts. To reduce the subjective biases in expert elicitation, the cut volume of $\alpha$ [39] and the area center technique [40] are used for expert evaluation aggregation in this study. The cut volume of $\alpha$ is designed to aggregate expert opinions to a specific region, and the area center technique is developed to acquire the center of this region. By using those two approaches, expert judgments/opinions can be synthesized twice. The combination of the two methods enables the aggregation of expert opinions and, therefore, reduces the influence of subjective biases in expert elicitations. If the linguistic levels of expert $i$ and

expert $j$ are medium $(\mathrm{M})$ and fairly high $(\mathrm{FH})$, respectively, the fuzzy language corresponding to the membership function is presented as follows:

$$
\begin{gathered}
u_{\mathrm{M}}(x)= \begin{cases}(x-0.4) / 0.1,0.4<x \leq 0.5 \\
(0.6-x) / 0.1,0.5<x \leq 0.6 \\
0, \text { otherwise }\end{cases} \\
u_{\mathrm{FH}}(y)= \begin{cases}(y-0.5) / 0.1,0.5<y \leq 0.6 \\
1,0.6<y \leq 0.7 \\
(0.8-y) / 0.1,0.7<y \leq 0.8 \\
0, \text { otherwise }\end{cases}
\end{gathered}
$$

Under the assumption that $\alpha \in u_{M}(x)$, then $\alpha=(x-0.4) / 0.1$ can be derived, i.e., $x=0.1 \alpha+0.4 . x$ is called the left cut volume of $\alpha$. Similarly, the right cut volume of $\alpha$ can be calculated as $-0.1 \alpha+0.6$. The cut volume of $\alpha$ of the fuzzy language $M$ is $[0.1 \alpha+0.4$, $-0.1 \alpha+0.6]$. Table 1 displays the cut volume of $\alpha$ corresponding to the fuzzy numbers. $\mathrm{L}=(0.1,0.2,0.2,0.3)$

Table 1. Fuzzy number and cut volume of $\alpha$.


If the weight of expert $i$ is 0.6 and the weight of expert $j$ is 0.4 , the set of fuzzy evaluations can be represented as follows:

$$
\begin{gathered}
W_{\alpha}=0.6 u_{M}^{\alpha}+0.4 u_{F H}^{\alpha}=[0.6(0.1 \alpha+0.4)+0.4(0.1 \alpha+0.5), 0.6(-0.1 \alpha+0.6)+0.4(-0.1 \alpha+0.8)]= \\
{[0.1 \alpha+0.44,-0.1 \alpha+0.68]}
\end{gathered}
$$

From the fuzzy set theory point of view, $W_{\alpha}$ is also a fuzzy set. Let $W_{\alpha}=\left[C_{1}, C_{2}\right]=$ $[0.1 \alpha+0.44,-0.1 \alpha+0.68]$, then $\alpha^{\mathrm{L}}=\left(C_{1}-0.44\right) / 0.1$ and $\alpha^{R}=\left(0.68-C_{2}\right) / 0.1$, where $\alpha^{\mathrm{L}}$ is the left cut volume of $\alpha$ and $\alpha^{\mathrm{R}}$ is the right cut volume of $\alpha$. Therefore, the membership function of the new fuzzy number, $W$, is presented as follows:

$$
u_{\mathrm{W}}(C)= \begin{cases}(C-0.44) / 0.1,0.44<C \leq 0.54 \\ 1,0.54<C \leq 0.58 \\ (0.68-C) / 0.1,0.58<C \leq 0.68 \\ 0, \text { otherwise }\end{cases}
$$

Figure 3 shows the function region of the fuzzy number, $W . x_{0}$ denotes the center of the region in the x-coordinate, and it can be presented by using Equation (7).

$$
x_{0}=\frac{\int_{X} x f(x) d x}{\int_{X} f(x) d x}
$$

Accordingly, the fuzzy possibility score (FPS), considering the opinions from both expert $i$ and expert $j$, is $x_{0}$. Eventually, Equation (8) can be used to transform the fuzzy possibility scores into fuzzy probabilities [41,42].

$$
P_{f}= \begin{cases}1 / 10^{K}, F P S \neq 0 \\ 0, F P S=0 \\ K=2.301 \times[(1-F P S) / F P S]^{1 / 3}\end{cases}
$$

Additionally, this paper uses a similarity aggregation method to decide the weight of each expert [43]. It is assumed that expert $i$ and expert $j$ choose fuzzy sets $A=\left(A_{1}, A_{2}, \ldots\right.$, $\left.A_{n}\right)$ and $B=\left(B_{1}, B_{2}, \ldots, B_{n}\right)$, respectively. Then, the similarity between $i$ and $j$ is measured by Equation (9):

$$
S_{i j}=1-\frac{\sum_{k=1}^{n}|A k-B k|}{4}
$$

The average agreement $\left(A A\left(E_{x i}\right)\right)$ of each expert is presented by Equation (10):

$$
A A\left(E_{x i}\right)=\frac{\sum_{i \neq j}^{M} S_{i j}}{j=1}
$$

where $M$ is the number of experts. $R A D\left(E_{x i}\right)$ is defined as the $i$ th relative agreement degree of expert weights, which can be calculated by using Equation (11).

$$
R A D\left(E_{x i}\right)=\frac{A A\left(E_{x i}\right)}{\sum_{j=1}^{M} A A\left(E_{x j}\right)}
$$

![img-2.jpeg](img-2.jpeg)

Figure 3. The function of fuzzy number $W$.

# 2.2.3. Association Rules (ARs) Method 

The ARs method is a data mining method that is able to identify correlations between different factors associated with similar events and extract a subset of frequent factors associated with an event [44]. Typically, an apriori algorithm is one of the widely used algorithms for association rule learning. An apriori algorithm is able to express causal relationships in a quantitative/probabilistic manner. Therefore, this study employs an apriori algorithm to quantify the conditional probabilities of the BN nodes. In ARs, the algorithm usually covers three indexes (support, confidence, and lift) for presenting the correlations between different factors. They can be calculated as follows [26]:

$$
S(A \Rightarrow B)=P(A \cup B)=\frac{|A \cup B|}{|D|}
$$

where $S(A \Rightarrow B)$ is the support of the $A$ to $B$ association. $A$ and $B$ are two different item sets. $P$ is the probability that $A$ and $B$ item sets appear simultaneously in the $D$ transaction set. $|D|$ is the transaction set. $|A \cup B|$ is the number of times that the $A$ and $B$ item sets appear simultaneously in the transaction set. The support of the $A$ to $B$ association refers to the probability that $A$ and $B$ appear simultaneously, and the correlation is strong if the two appear together frequently.

$$
C(A \Rightarrow B)=P(B \mid A)=\frac{|A \cup B|}{|A|}
$$

where *C*(*A*⇒*B*) is the confidence of the *A* to *B* association, which refers to the probability of B occurring if A has already occurred. |*A*| is the number of occurrences of *A* in the transaction set. $$\begin{array}{rcl} & & L(A \Rightarrow B) = \frac{P(BA)}{P(B)} = \frac{P(A \cup B)}{P(A)P(B)} \end{array}$$

where *L*(*A*⇒*B*) is the lift of the *A* to *B* association, which refers to the correlation between *A* and *B*. When *L* = 1, A is uncorrelated with *B*. When *L* < 1, *A* and *B* are negatively correlated. When *L* > 1, *A* and *B* are positively correlated.

Figure 4 shows the AR algorithm procedures, where the confidence index is used to present the conditional probability of the BN nodes. The role of the AR is to determine the association degree between different BN nodes. The accident cause types and the accident are considered to be associated only when *L* > 1. Consequently, the conditional probabilities can be calculated for the interrelated factors; otherwise, the conditional probabilities are zero. Because the existing literature and practices on AR technologies have no standardized guidelines for determining the support_{min} and confidence_{min} thresholds [26,29,45,46], this study obtains the appropriate support_{min} and confidence_{min} by comparing the effectiveness of the threshold values continuously. For instance, the support_{min} and confidence_{min} were initially set as 0.2 and 0.5, respectively. However, the generated association rules cannot be fully corresponded to the conditional probabilities of the BN nodes. Until the support_{min} and confidence_{min} were set as 0.1 and 0.3, respectively, the conditional probabilities of the BN nodes were all derived. Detailed procedures for association rule learning can be found in Figure 4, in which the node “association rule” represents the probabilistic association between the BN nodes. The calculation of the association rules was performed by using the software IBM SPSS Modeler 18.0.

![img-3.jpeg](img-3.jpeg)

**Figure 4.** Flowchart of the apriori algorithm.

# 3. Example Analysis of Fire Accidents in Laboratories 

### 3.1. Data Collection

The confidence $(A \Rightarrow B)$ is considered the conditional probability of the happening of B given A. However, according to Equation (2), when the AR analyzes only one accident, $|A \cup B|=|A|$ and $\mathrm{C}(A \Rightarrow B)=1$. In other words, if only one type of accident is analyzed, the confidence is always 1 . The confidence cannot be converted into the conditional probability of the BN in this situation. Accordingly, the statistical data need to include all types of accidents. The relationship between accident causes and fire accidents is explored from all types of accidents.

Accordingly, 121 cases of laboratory accidents (about 121 laboratory accidents were publicized in Chinese universities from 2000-2022) are used to identify the main causes of laboratory accidents. These accidents can be found on the official websites of some colleges and universities, while accident reports need to be retrieved. Fires, explosions, electric shocks, poisoning, and other accidents are included in the accident database. The identified causes are classified into four categories: human (human factors), object (object conditions), environment (environmental factors), and management (organizational and management factors). Among these 121 accidents, only the type of accident and the type of cause are collected. This is to explore the probabilistic relationships between fire accidents and the human, object, environment, and management.

With respect to fire incidents, detailed accident causes need to be identified and collected based on the 121 accident reports. Table 2 presents the description of the identified accident causes with their symbols. The names of the accident causes are defined based on the statements in the accident reports. The description of the data format and data processing with software can be found in Section 3.3. Additionally, some issues need to be noticed during the data collection process. For example, the time span of the data should be chosen as no less than 10 years to ensure the annual regularity of the data. Meanwhile, the number of accident cases should be as large as possible to ensure data generality. In addition, some accident reports with incomplete information should not be selected to safeguard the completeness of the results.

Table 2. Descriptions of the identified causes/causal factors with their symbols.


### 3.2. Construction of Bayesian Network Topology

After the identification of the accident causes/causal factors, a BN topology structure was developed, considering the dependency between those BN nodes, as presented in Figure 5. Since the whole diagram is complex, Figure 5 divides the topology into two parts:

(a) presents the relationships among specific accident causes, and (b) shows the relationship between the cause category nodes and the fire accident node. In the BN model, the cause nodes "H1" to "H8" in Figure 5a should be pointed to the "Human" node in Figure 5b. Similarly, other cause nodes should be linked to the corresponding cause categories. Then, the prior probabilities of the root nodes in Figure 5a were determined by using fuzzy set theory and expert elicitations. The conditional probabilities of the BN nodes were obtained from the accident database with the help of AR learning. The determination of the prior probabilities and conditional probabilities of the BN nodes is illustrated in the next sections.

![img-4.jpeg](img-4.jpeg)

**Figure 5.** The topology of the developed BN model for university laboratory fire risk analysis. (**a**) indicates the relationship between the specific causes; (**b**) shows the relationship between the cause categories and the fire accidents. (different node colors correspond to different node categories).

### 3.3. Association Rule Learning

To clearly explain the methodology, the data format during the data collection process is described. Some of the accident data analysis results are presented in Table 3 for demonstrative purposes. In Table 3, "√" indicates the accident types (column header). "1" indicates that the causes of the specific accident case belong to the corresponding cause category (the column header); by contrast, "0" presents that the accident causes do not belong to the corresponding category. For example, the first case is a fire accident, which is

mainly caused by humans, objects, and the environment. By following the data format in Table 3, the data were collected in an Excel spreadsheet.

Table 3. Data expressions required by the apriori algorithm.


Table 4 shows a part of the association rule learning results, with a total of 15 rules. As shown in Table 4, because the lift index value of the human and management factors in relation to a fire accident is less than one, the corresponding conditional probability is considered zero. Similarly, the lift index value of environmental factors to fire incidents is less than one, so the corresponding conditional probability is also zero. The obtained conditional probability table (CPT) for the fire accident node is presented in Table 5. The conditional probability tables for other BN child nodes were also obtained in the same way by using association rule learning.

Table 4. The results of association rules.


Table 5. The conditional probability table of the fire accident node derived by ARs.


Y indicates the event occurs; N means the event does not occur.

# 3.4. Determination of Prior Probabilities

In this study, five experts with rich lab fire safety and lab experiment experience were invited to score the basic events related to laboratory fires concerning the safety engineering laboratory at Fuzhou University. This section demonstrates the determination of the prior probabilities of the root nodes (basic events) by using the BN node, "M1", as an example. The evaluation results from the experts on the "M1" node are "M", "FH", "FH", "VH", and "M". The weight of each expert was obtained according to Equations (9)-(11), as presented in Table 6.

Table 6. Results of fuzzy opinion aggregation.


The corresponding fuzzy set is constructed by using the cut volume of $\alpha$ and the expert weights. The calculation process is as follows:

$$ \begin{gathered} W_{\alpha}=0.205 u_{M}^{s}+0.214 u_{F H}^{s}+0.214 u_{F H}^{s}+0.162 u_{V H}^{s}+0.205 u_{M}^{s} \ =[0.205(0.1 \alpha+0.4)+0.214(0.1 \alpha+0.5)+0.214(0.1 \alpha+0.5)+0.162(0.1 \alpha+0.8)+0.205(0.1 \alpha+0.4), \ 0.205(-0.1 \alpha+0.6)+0.214(-0.1 \alpha+0.8)+0.214(-0.1 \alpha+0.8)+0.162+0.205(-0.1 \alpha+0.6)] \ =[0.1 \alpha+0.5076,-0.0838 \alpha+0.7504] \end{gathered} $$

Consequently, the membership function of the fuzzy set is as follows:

$$ u_{\mathrm{W}}(C)=\left{\begin{array}{c} (C-0.5076) / 0.1,0.5076<C \leq 0.6076 \ 1,0.6076<C \leq 0.6666 \ (0.7504-C) / 0.0838,0.6666<C \leq 0.7504 \ 0, \text { Otherwise } \end{array}\right. $$

```

The fuzzy set of $x_{0}$ is calculated as 0.6325 , according to Equation (7). Then, the fuzzy probability of the happening of "M1" is calculated as 0.0120 with Equation (8). The prior probabilities of the remaining root nodes were also determined by using the same method. Table 7 presents the obtained expert evaluations for the remaining root nodes. Correspondingly, Table 8 provides the FPS and the fuzzy prior probabilities for the root nodes.

Table 7. The results of the expert elicitation.


Table 8. The FPS and fuzzy probabilities of the root nodes.


# 4. Results and Discussions

### 4.1. Validation of the Augmented Fuzzy Set Method

This section discusses the effectiveness of the augmented fuzzy set method in aggregating expert opinions with possible biases. Table 9 shows some examples of the expert evaluation results. Cases 1 to case 3 are used to demonstrate the aggregation of expert opinions in the case of a low evaluation existing among the evaluation results from other experts being relatively higher. By contrast, cases 4 to case 6 are used to demonstrate the aggregation of expert opinions in the case of a high evaluation existing among the evaluation results from other experts being relatively lower.

Table 9. Examples of the evaluation results from three experts.


Figure 6 compares the fuzzy regions before and after using the similarity aggregation method (the cut volume of $\alpha$ ). It can be observed from Figure 6 that the fuzzy regions are strongly reshaped by using the similarity aggregation methods when there are obvious differences/biases in the experts' opinions. The range of the reshaped fuzzy regions is more consistent with the expert opinions with similarities. Additionally, the fuzzy value of each example is calculated and presented in Figure 7 to demonstrate the effectiveness of the similarity aggregation method. "Before" indicates the calculated fuzzy number without using the similarity aggregation method, and "After" indicates the calculated fuzzy number using the similar aggregation method. "D-value" means the difference between the calculated fuzzy numbers with and without the implementation of the similarity aggregation method. It can be observed from Figure 7 that the aggregation effects of the similarity aggregation method become more obvious when the difference in the expert

evaluations is larger. In conclusion, the augmented fuzzy set method is able to aggregate expert opinions, especially when there are obviously differences/biases in the expert opinions.

![img-5.jpeg](img-5.jpeg)

**Figure 6.** Fuzzy regions before and after using the similarity aggregation method. (**a**) Example No. 1. (**b**) Example No. 2. (**c**) Example No. 3.

![img-6.jpeg](img-6.jpeg)

Figure 7. Changes in the fuzzy numbers before and after using the similarity aggregation method.

# 4.2. Impact Level Analysis of the Cause Categories 

The impact of each cause category on the happening of lab fires is compared in this section through a sensitivity analysis of the cause category nodes. Figure 8 shows the FV value of each cause category node. It is observed that management factors are the most important causes of the occurrence of lab fire accidents. In fact, the habits, behaviors, and safety awareness of laboratory staff are significantly influenced by management factors [47]. A survey shows that the use of safety recording management systems in laboratories can reduce operators' risky behaviors and habits effectively [10]. Therefore, management factors should be given enough attention by the laboratory managers and the university safety management teams. The improvement of the safety management systems helps to reduce the risky behaviors and habits of lab operators and, meanwhile, enhances the safety awareness of laboratory staff to reduce the risks of the happening of lab fire accidents.
![img-7.jpeg](img-7.jpeg)

Figure 8. The FV values of different cause categories.

### 4.3. Impact Level Analysis of Basic Events

This section discusses the sensitivity of each basic event (causal factors) on the happening of lab fire accidents. Figure 9 shows the FV value of each basic event with respect to the

happening of lab fire accidents. In terms of human factors, H4 (bad safety awareness) is the most critical cause. Ozsahin et al. [48] and Walters et al. [49] emphasized the importance of the safety awareness of students to the safety of university laboratories, which is consistent with this finding. The establishment of high-quality safety training and education programs may help to enhance the safety awareness of laboratory staff and further reduce laboratory accident risks. Diverse learning methods can better attract the attention of students and improve learning efficiency [50]. Universities may provide diverse approaches to improve the learning efficiency of workers in safety education, for example, slides, videos, news, and the implementation of electronic games and VR techniques. In terms of object factors, O1 (improper storage of hazardous chemicals) is the most critical causal factor. Some existing accident cases also demonstrate this point. For instance, a fire and explosion happened in a laboratory of Beijing Jiao Tong University on 26 December 2018. According to the accident investigation report, an important cause of this accident was the improper storage of hazardous chemicals. In the management of hazardous chemical storage, the safety responsibility system should be implemented, and the information on hazardous chemicals should be recorded in detail. At the same time, colleges and universities should set up special safety inspection programs for hazardous chemical storage tanks. In terms of environmental factors, E1 (environment with hazardous materials) is the most critical factor. In university laboratories, experiment environments may have huge interventions to the happening of laboratory accidents. For instance, conducting experiments in a space with excessive concentrations of dangerous gases (e.g. methane and other flammable gases) may trigger undesired lab accidents. Zhang et al. [15] developed a BN model to investigate the evolution process of a gas leak in laboratories. The results obtained in the same study show that gas accumulation is one of the critical factors affecting accident evolutions. Therefore, the monitoring of the experiment environment is important to the safety of university laboratories. For instance, gas detection devices and hazardous alarm systems can be installed to monitor experiments with flammable and explosive gases. In terms of management factors, M4 (inadequate safety checks) is the most critical influence factor. This result is consistent with the result obtained by Ma et al. [16]. There are many ways that can be employed to improve the quality of safety checks/inspections in university laboratories. For example, the utilization of artificial intelligence tools to help with some of the safety check tasks. Zhang and Guo [51] designed a sentry robot that can take appropriate emergency measures based on the detection of dangerous situations. In addition, universities can also use various risk assessment methods to provide a reference basis for safety inspections.

![img-8.jpeg](img-8.jpeg)

**Figure 9.** The FV values of basic events.

# 4.4. Limitations and Future Work 

Inevitably, the risk analysis results of the proposed approach rely on the quality and amount of accident data, which is also a limitation for all similar data-driven risk analysis approaches. Therefore, with more historical accident data becoming available, the practicality and feasibility of the proposed model may be improved to generate more reasonable risk estimations. Furthermore, it should be noted that subjective bias may also be induced by an inappropriate selection of experts, the unreasonable formulation of questions, bad interpretation of evaluation results, and so on. Therefore, when applying the proposed approach in practice, those factors that may introduce bias in expert elicitation results cannot be ignored either. Future studies may focus on developing systematic approaches/guidelines for the appropriate selection of experts, framing questions, and interpreting results to avoid or reduce biases in expert elicitation.

In the future, the proposed methodology may be integrated with risk-based decisionmaking approaches [52] to achieve risk-based fire safety management for university laboratories. For example, it is possible to consider both the safety investment and risk-reduction performance of the candidate safety management strategies [53] and then achieve costeffective safety management of the university laboratory regarding fire accidents. Moreover, it should be noted that it is also possible to apply the proposed approach to the risk analysis of laboratory fire accidents in other countries or regions. This can be performed by replacing the accident database with the accident statistics associated with the investigated university laboratory. Also, an expert evaluation team can help to determine the prior probabilities of the basic events/factors regarding fire accidents in a specific university laboratory.

## 5. Conclusions

In this study, by combining association rules, a BN, and an augmented fuzzy set method, an integrated risk analysis method is proposed for the risk analysis of laboratory fire accidents. A case study was employed to demonstrate the feasibility of the proposed approach in the risk analysis of lab fire accidents in Chinese universities. Expert elicitation was used to determine prior probabilities for the BN model with the help of an augmented fuzzy set method. The effectiveness of the augmented fuzzy set method in expert opinion aggregation with possible biases was demonstrated. Additionally, a database with 121 cases of laboratory accidents that happened in Chinese universities was used to derive conditional probabilities for the BN model with the help of association rule learning. With the application of the proposed model in the risk assessment of Chinese university lab fires, the results indicate that H4 (bad safety awareness), O1 (improper storage of hazardous chemicals), E1 (environment with hazardous materials), and M4 (inadequate safety checks) are the four most critical events for the occurrence of fire accidents. In addition, management factors have the most significant impact on the happening of laboratory fires. With more historical accident data becoming available, the practicality and feasibility of the proposed model may be improved to generate more reasonable risk estimations.

Author Contributions: All authors contributed equally to this work. All authors have read and agreed to the published version of the manuscript.
Funding: This work was supported by the National Natural Science Foundation of China (grant numbers: 52274181 and 51874100).
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Data unavailability due to privacy.
Conflicts of Interest: The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

# Abbreviations 

