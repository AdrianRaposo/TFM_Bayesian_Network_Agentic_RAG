# Article 

## A Case Study of Accident Analysis and Prevention for Coal Mining Transportation System Based on FTA-BN-PHA in the Context of Smart Mining Process

Longlong He * (D), Ruiyu Pan, Yafei Wang, Jiani Gao, Tianze Xu, Naqi Zhang, Yue Wu * and Xuhui Zhang (D)

## check for updates

Citation: He, L.; Pan, R.; Wang, Y.; Gao, J.; Xu, T.; Zhang, N.; Wu, Y.; Zhang, X. A Case Study of Accident Analysis and Prevention for Coal Mining Transportation System Based on FTA-BN-PHA in the Context of Smart Mining Process. Mathematics 2024, 12, 1109. https://doi.org/ 10.3390/math12071109

Academic Editor: Andrea Scozzari
Received: 16 March 2024
Revised: 4 April 2024
Accepted: 4 April 2024
Published: 7 April 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

Shaanxi Key Laboratory of Mine Electromechanical Equipment Intelligent Detection and Control, Xi'an University of Science and Technology, Xi'an 710049, China; pry17835972904@163.com (R.P.); wyf20160423@163.com (Y.W.); gjn20190326@163.com (J.G.); x13835872797@163.com (T.X.); helonger@gmail.com (N.Z.); zhangxh@xust.edu.cn (X.Z.)

* Correspondence: hell@xust.edu.cn (L.H.); wuyue1992@xust.edu.cn (Y.W.)

Abstract: In the face of the increasing complexity of risk factors in the coal mining transportation system (CMTS) during the process of intelligent transformation, this study proposes a method for analyzing accidents in CMTS based on fault tree analysis (FTA) combined with Bayesian networks (BN) and preliminary hazard analysis (PHA). Firstly, the fault tree model of CMTS was transformed into a risk Bayesian network, and the inference results of the fault tree and Bayesian network were integrated to identify the key risk factors in the transportation system. Subsequently, based on the preliminary hazard analysis of these key risk factors, corresponding rectification measures and a risk control system construction plan are proposed. Finally, a case study was carried out on the X coal mine as a pilot mine to verify the feasibility of the method. The application of this method effectively identifies and evaluates potential risk factors in CMTS, providing a scientific basis for accident prevention. This research holds significant importance for the safety management and decision making of coal mine enterprises during the process of intelligent transformation and is expected to provide strong support for enhancing the safety and reliability of CMTS.

Keywords: coal mining transportation system; accident analysis and prevention; preliminary hazard analysis; smart mining process

MSC: 82D99

## 1. Introduction

Accident risk assessment and management are crucial for the coal mining transportation system (CMTS), which aims to investigate and predict the failure of mining processes and, further, to ensure the well-being of humans, no harm to the environment, and asset integrity [1]. Given the hazardous underground mining environment, dynamic and operational risk assessment and management are crucial processes for coal mining enterprises to identify, evaluate [2], and mitigate risks associated with their operations and activities of CMTS [3]. At the same time, the intelligentization of the coal mine working face is the core technology to achieve high-quality development in the coal industry; building a model for coal mine transportation accidents is beneficial for the intelligent development of coal mines [4]. Therefore, it is of great significance to systematically analyze the accidents of CMTS and establish a risk pre-control system for intelligent transformation and efficient mining of coal mines [5].

To deal with the increasingly complex dynamic and operational risk and safety for the coal mining process industry [6], previous research has tried to identify the chance in exploring the solely state-of-the-art methods and models from the view of risk assessment and management for CMTS, such as failure mode and effects analysis (FMEA) [7], risk

matrix (RM) [8], statistical process control (SPC) [9], hierarchical analysis [10], and grey relational analysis (GRA) [11]. Specifically, Bayesian network (BN), with the ability of bidirectional inference and efficient analysis of the impact of complex influencing factors on accidents, has been widely applied in the field like hydrogen-doped pipelines [12], offshore drilling operations [13], and so on. Obviously, all the above forerunner research has important significance. Nevertheless, it ignores the system-level issues (i.e., accident data set, interaction, initial assumptions, and construction of knowledge base [14]) and few works have been dedicated to the issue of integration and fusion of multiple methods at the same time for CMTS.

Therefore, to address the limitations of traditional analysis methods in meeting practical needs, this study proposes a comprehensive qualitative and quantitative analysis of the risks of CMTS by combining fault tree analysis (FTA) with BN and preliminary hazard analysis (PHA). The aim is to identify the risk Bayesian accident nodes that are most likely to cause transportation accidents in coal mines. Furthermore, in order to analyze the risk Bayesian accident nodes and take corresponding preventive measures, it is necessary to identify the causes of accidents in the CMTS and the potential consequences through PHA. This allows for the formulation of risk prevention and control measures and the construction of a pre-control system to minimize the likelihood of accidents.

The rest of this paper is organized as follows: Section 2 defines methodology for accident analysis in CMTS. Section 3 details the risk assessment process for coal mine accidents. The case study validation at $X$ coal mine is presented in Section 4. The conclusion and future work are concluded in Section 5.

# 2. Related Work 

### 2.1. Risk and Safety Assessment and Management Techniques

Process systems are subject to deterioration over time due to natural and human-made causes [15]. C-RISE of Memorial University, a professional risk and safety research group, has systematically summarized various methods and models to investigate and predict risk in different domains. Based on structures, accuracy, and independency, these risk analysis methods and modes can be categorized into static (i.e., FTA, event tree analysis [16], reliability block diagrams, and PHA [17]) and dynamic (i.e., dynamic event tree [18] and Markov-process-based fault tree [19]), where the latter is an improvement of the former type to deal with more complex dynamic process systems [20]. Feature- and functionbased categories of risk and safety assessment and management techniques encompass risk identification and analysis, assessment, management, and control, which will be comprehensively reviewed in detail [21].

To identify and evaluate the hazards and risk, FTA is a typical analytical method utilizing logical reasoning and representing the logical relationships between potential accidents and causes through a tree-like diagram [22]. Based on a random number, Zhang et al. [23] proposed a safety static fault tree model to quantitatively analyze the potential risk of inerting systems with a large number of minimal cut sets. Based on FTA-AHP, Ren et al. [24] proposed a collapse accident safety decision analysis method to qualitatively and quantitatively evaluate risk factors related to collapse accidents and determine the primary causes. To improve the accuracy and interpretability of the milling fault detection model, Cheng et al. [25] introduced a milling fault detection method combined with FTA and hierarchical confidence rule base.

To analyze and assess key factors, BN is an ideal network model with the function of bidirectional inference and efficient analysis of the influence of each variable on the final node and the interpretation of the correlations between variables based on Bayesian theory and graphical theory [26]. Combined with association rules, Li et al. [27] utilized BN to explore chemical explosion accidents, revealing accident pathways and the sensitivity of direct causes. Mohammed et al. [28] proposed a formalized modeling tool, named Bayesian Stochastic Petri Nets (BSPN), for dynamic safety and reliability analysis. For medical device risk assessment and management, Hunte et al. [29] propose a novel approach using

hybrid Bayesian networks to handle uncertainty and incorporate causal knowledge and incorporate relevant factors from the medical device safety and risks. Cenk et al. [30] mapped fault trees to BN for dynamic analysis of pilot transition accidents, greatly improving the accuracy of determining accident factors. By dividing risk factors into multiple states, Yang et al. [31] introduced the concept of accuracy and relied on BN to calculate risk probabilities and distributions in real time, providing targeted preventive measures. Wang et al. [32] conducted simulations, analysis, and evaluations using the accident causality model System-Theoretic Accident Model and Processes (STAMP) and the Bayesian network model to accurately assess the traffic safety risks associated with the penetration of autonomous driving technology.

To analyze and control potential risk before engineering activities, PHA is one of the methods applied to analyze triggering conditions, hazard types and levels, consequences, and prevention measures of accidents [29]. To determine key influencing factors and identify accident causal event chains of autonomous surface ships, Zhang et al. [33] proposed a PHA-based causal logic method to provide references for maritime autonomous surface ship design and safety assessment processes. Combined with inversion temperature charts, Zhu et al. [34] proposed an OCTEM-PHA analysis model to analyze and predict five risk factors present in Guangxi mine and propose corresponding safety measures. To identify hazardous scenarios, Nicolau et al. [35] developed a PHA-based quantitative analysis method for the radioactive and chemical risks in uranium isotope enrichment facilities and defining the characteristics of each hazard and their causes and consequences.

# 2.2. Coal Mine Transportation Accidents Analysis 

Efficient transportation is one of the keys to efficient coal production [36]. While the development of intelligent transformation and the improvement of management levels, the occurrence rate of transportation accidents and associated risk continue to increase [37] due to the complex nature of the coal industry [38]. For effective accident prevention and risk assessment in CMTS, a scientific method is to analyze the causes of historical transportation accidents and understand the mechanisms and patterns of accidents and design an effective analysis indicator and rational foundations [39]. Currently, scholars are conducting relevant research on CMTS accidents. Based on statistical patterns of the past five years (2017-2021) of nationwide coal mine accidents, Zhang et al. [37] described the accident information from four dimensions, accident level, type, region, and time, and proposed preventive measures for transportation accidents. Wang et al. [39] proposed a modeling approach called mine accident unsafe behavior network (MAUAN) to analyze the interrelationships and potential behavioral patterns of unsafe behaviors from a network modeling perspective. Wei et al. [40] proposed a quantitative risk assessment method based on the bow-tie model to reduce the occurrence rate of underground vehicle accidents. Pandey et al. [41] propose a method that utilizes fuzzy decision-making trial evaluation laboratory (DEMATEL) to conduct a comprehensive assessment of the key factors leading to truck mining accidents and the relationships between these factors are illustrated with a causal diagram.

The current application research shows that extensive studies have been conducted both domestically and internationally on safety risk analysis and accident prevention in CMTS, resulting in significant achievements in technology and management. However, there are also some drawbacks that need to be addressed. Firstly, the data in case studies often represent specific cases with poor representativeness. Secondly, the analysis of accident causes is not comprehensive enough, lacking inferences about risk evolution, and the provided recommendations for risk prevention are relatively general and not specific enough.

To address these issues, this study will select coal mine transportation accident cases from the past 20 years and utilize fault tree analysis, Bayesian network methods, and preliminary hazard analysis for risk analysis and prevention. The following sections will provide a detailed introduction to the relevant methods used in this study and their

applications in the field of accident analysis, exploring their potential application in the domain of coal mine transportation accidents.

# 3. A Framework of CMTS Accident Analysis and Prevention Based on FTA-BN-PHA 

This study proposes a framework of accident analysis and prevention based on FTA-BN-PHA for CMTS. Firstly, according to the classic CTMS, an FTA model is constructed. Then, the accident tree is mapped to a BN model for performing bidirectional inference and enabling analysis of the importance of each basic event. Finally, a PHA model is conducted on the main risk factors to establish an accident pre-control system. The framework of the proposed accident analysis method in this study is illustrated in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1. Analysis process of coal mine transportation accidents based on FTA-BN-PHA.

### 3.1. Identification of Factors in Coal Mine Transportation Accidents

There are two channels for knowledge acquisition; one is that it only needs simple preprocessing that can be used as input for subsequent AI and the other is that it needs to extract structured information with the help of natural language processing and other technologies [14]. So, this study is no exception.

Firstly, this study used Python web-scraping techniques to select and compile a total of coal mining transportation accidents from websites such as the Coal Mine Safety Network, National and Local Mine Safety Supervision Bureaus, etc. Next, in this study, R 3.6.1 and corresponding programs were used to perform mining analysis on accident reports to obtain textual data on risk factors in CMTS. To enhance the analysis results and minimize

the impact of irrelevant phrases, only three sections of the accident reports were chosen for text mining. These sections are the "accident category or nature", "accident process", and "accident causes". For instance, an accident description could be condensed as follows: "On 20 October, at 10:00 AM, at the installation working face, the wire rope of the winch in the return airway, which was 2200 m away from the roadway entrance, popped out and struck the operating personnel". Additionally, any erroneous information in the accident reports was corrected. The selected data were then stored in a text file to form a corpus for mining. To handle the abundance of specialized terms in the accident reports, Python 3.8 was utilized to implement jieba word segmentation programmatically. Following this, a stop-word dictionary and a user dictionary were created, adhering to the specific guidelines within the coal industry's transportation safety domain. The stop-word dictionary, along with regular expressions, aided in the elimination of irrelevant conjunctions and punctuation from the accident text. Additionally, the user dictionary pattern was employed for effective segmentation of the report data.

Afterwards, the textual data were transformed into a vector format that can be recognized by computers. Using Python programming, a Word2Vec word-embedding model was trained based on the preprocessed set of accident words. The trained model represents key words as multidimensional vectors, and the relationship between key words is determined by analyzing the distances between the vectors' dimensions. The Continuous Bag-of-Words (CBOW) model in Word2vec is used to distinguish words with similar content but different meanings. For example, "mine car", "electric locomotive", and "drive" all contain the word "car", while words that appear in "Ore car" and "electric locomotive" are noun-like feature words for transportation equipment, while "drive" is an operation verb-like feature word, which can well distinguish professional vocabulary in the field of transportation systems. Since the word vector model only contains keywords and vector space after training, it is necessary to establish a classification corpus that can provide a classification basis for the computer. A keyword classification corpus is constructed based on expert knowledge. The classification attribute value of " 1 " indicates that the keyword is a feature-class keyword, while a value of " -1 " indicates a causative-class keyword. A classification attribute value of " 0 " indicates that the classification of the keyword is unclear.

The principle of the keyword classification algorithm is based on the concept that, in the same vector space, the smaller the angle between two keyword vectors, the larger the cosine value, indicating that the two keywords have a similar composition and contextual environment. The algorithm selects the eight most similar keywords to the target keywords. The formula for calculating cosine similarity is as follows:

$$
\cos \theta=\frac{\omega \cdot s}{|\omega| \times|s|}=\frac{\sum_{i}^{n}\left(w_{i} \times s_{i}\right)}{\sqrt{\sum_{i}^{n} 1^{1} \omega_{i}^{2} \times \sqrt{\sum_{i}^{n} 1^{s_{i}^{2}}}}
$$

In Equation (1), $\cos \theta$ stands for cosine similarity between two keyword vectors, $\overrightarrow{\omega_{i}}$ is the word vector of the target word, $\overrightarrow{s_{i}}$ is the word vector of the matching word, and $\omega_{i}$ and $s_{i}$ are the values of word vectors in the i-th dimension.

After calculating the cosine similarity and obtaining the eight most similar words, the target word can be classified using the score. The formula for calculating the score is as follows:

$$
\text { Score }=\sum_{i=1}^{8} \cos \theta_{i} \times f_{i}
$$

In Equation (2), Score represents the word classification score, $\cos \theta$ is the cosine similarity of word vectors, and $f_{i}$ represents the classification attribute value of the ith similar word.

After calculating the Score using the Python programming language, keywords can be automatically classified. When Score $>1$, it indicates a high cosine similarity between the target word and feature-class keywords, assigning a classification attribute value of 1. Conversely, when Score $<-1$, it indicates a higher cosine similarity between the target word and causative-class keywords, assigning a classification attribute value of -1 . Finally, the causative-class keywords can be stored in an Excel spreadsheet, categorized by their attributes, to obtain data on coal mining transportation accident factors. Using the corpus to display accidents as an example, text mining is used to determine accident keywords and classify them, as shown in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2. Text mining example.

# 3.2. Theoretical Analysis and Process of FTA 

According to the traffic accident risk factors and accident-report-related data, the specific process of constructing the coal mine traffic accident tree model is as follows:

Step 1: Establishment and module decomposition of CMTS accident tree. Firstly, the accident of the CMTS is determined to be the top event of the fault tree analysis, which is represented by " $T$ ". According to the type, the CMTS can be divided into level roadway transportation system accidents, inclined roadway transportation system accidents, and vertical shaft lifting transportation system accidents, and the above three events are represented by " $\mathrm{T}_{1}, \mathrm{~T}_{2}$, and $\mathrm{T}_{3}$ ", respectively, as the first intermediate events.

Due to the complexity of the fault tree model for the CMTS, a simplification and decomposition approach is adopted to analyze its causes. Each first-level intermedi-

ate event is treated as a module, leading to the decomposition of the system into three sub-fault trees. Each sub-fault tree will be subject to individual qualitative analysis and quantitative calculations.

Step 2: Qualitative analysis of accident trees in CMTS. Qualitative analysis is used to obtain the minimum cut sets of each sub-fault tree, thereby reducing the probability of failure in the CMTS. The occurrence of the top event is not established unless all the basic events have occurred. If a simultaneous occurrence of certain basic events can lead to the occurrence of the top event, then the set of these basic events is known as the cut set of the fault tree. Structural importance analysis, from a qualitative perspective, examines the importance of each basic event. The structural importance can be determined using the minimum cut sets. In this study, the structural function and the downset method are employed to calculate the minimum cut sets of the fault tree model and rank the structural importance of the basic events for the analysis of the CMTS accident tree model. The structural function of the fault tree is essentially a Boolean function associated with logic gates. When the values of the basic events are either 0 or 1 , the calculation formula is as follows [42]:

$$
\Phi(X)=\prod_{i=1}^{n} X_{i}(i=1,2, \cdots n)
$$

In Equation (3), $\Phi(X)$ represents that the top event will occur only when all n basic events occur simultaneously. Conversely, if any of the basic events does not occur, the top event will not occur [42]. In the formula, $X_{i}$ represents the basic event.

$$
\Phi(X)=1-\prod_{i=1}^{n}\left(1-X_{i}\right)(i=1,2, \cdots n)
$$

In Equation (4), $\Phi(X)$ represents that the top event will occur when any one of the n basic events occurs. Conversely, if none of the basic events occur, the top event will not occur.

The downset method applies the rules of Boolean algebra to replace the upper-level and lower-level events. The AND gate is represented by multiplication and the OR gate is represented by addition. This process continues until all events in the equation are replaced by basic events. Finally, the results of the minimum cut sets are accumulated.

Step 3: Quantitative analysis of accident trees in CMTS. The quantitative calculation of the fault tree is to find out the key failure modes in the fault tree by calculating the importance of each bottom event in the fault tree. The structural importance of the basic events in the CMTS is ranked based on the results of the minimum cut sets and the related basic events. The formula for calculating the structural importance is as follows [43]:

$$
I_{s}(i)=\sum_{x_{i} \in k_{j}} \frac{1}{2^{n_{j}-1}}
$$

In Equation (5), $I_{s}(i)$ represents the structural importance of the basic event $\mathrm{I}, k_{j}$ represents the j -th minimum cut set, and $n_{j}$ represents the number of basic events in $k_{j}$.

# 3.3. Build BN Model 

Given the sample dataset, BN analysis typically involves two types of learning: parameter learning and structure learning. This study maps the accident tree model into a Bayesian network structure and then carries out parameter learning.

The node states in the Bayesian network are represented as:

$$
X_{i}=\left\{\begin{array}{c}
0 \text { When event } i \text { does not occur }(\text { normal }) \\
1 \text { When event } i \text { occurs }(\text { fault })
\end{array} i=1,2, \cdots n\right.
$$

In Equation (6), $X_{i}$ denotes the Bayesian network node state and $i=1,2 \ldots n$.

The structural function $\varphi(X)$ of the top event is:

$$
\varphi(X)=\left\{\begin{array}{c}
0 \text { When event } i \text { does not occur }(\text { normal }) \\
1 \text { When event } i \text { occurs }(\text { fault })
\end{array} \right.i=1,2, \cdots n
$$

In Equation (7), $\varphi(X)$ denotes the structure function of the top event and $i=1,2 \ldots n$.
When constructing a Bayesian network based on the accident tree model, the steps are as follows:

Step 1: Mapping the incident tree to a Bayesian network. Determining the directed acyclic graph of the Bayesian network is as follows: each node of BN is mapped to the events in the accident tree and directed edges are used to connect the corresponding nodes. The logic gates in the accident tree are expressed as conditional probability distributions of the nodes in the BN. The specific process algorithm for mapping the accident tree model to the Bayesian network model is shown in Algorithm 1.

```
Algorithm 1. Algorithm for mapping FTA to BN.
Input: Accident tree model and related nodes, relationships
Output: Bayesian network model and related nodes, relationships
Begin
// 1.Define the fault tree node class
class Fault Tree Node:
def __init__(self, name):
self.name = name
self.parents = []
self.children = []
self.probability = 0.0
//2. Define the BN node class
class Bayesian Node:
def __init__(self, name):
self.name = name
self.parents = []
self.children = []
// 3.Define a function to convert the fault tree model to a BN model
def convert_fault_tree_to_bayesian(fault_tree_root):
bayesian_network_nodes = {}
visited_nodes = set()
def dfs(node):
if node in visited_nodes:
return
visited_nodes.add(node)
//4. Create BN nodes
bayesian_node = BayesianNode(node.name)
bayesian_network_nodes[node.name] = bayesian_node
for parent in node.parents:
// 5.Convert the parent nodes of the fault tree nodes to the parent nodes of the BN
parent_bayesian_node = bayesian_network_nodes.get(parent.name)
if parent_bayesian_node is None:
parent_bayesian_node = Bayesian Node(parent.name)
bayesian_network_nodes[parent.name] = parent_bayesian_node
bayesian_node.parents.append(parent_bayesian_node)
parent_bayesian_node.children.append(bayesian_node)
// 6.Handle the parent node recursively
dfs(parent)
dfs(fault_tree_root)
return bayesian_network_nodes
end
```

As shown in the algorithm in Algorithm 1, using mapping techniques from FTA to BN, the conditional dependencies and uncertainties of important variables can be represented and analyzed using BN. The correspondence is established to maintain the logical relationships and structural consistency of the fault tree model in the Bayesian network.

Step 2: Calculation of the prior probability of risk factors P(A). For a comprehensive BN risk analysis, it is necessary to determine the prior probabilities of the root node and the conditional probabilities of the leaf nodes. Equation (8) can be utilized along with the frequency of risk factors to obtain the prior probabilities $P(A)$ for the risk factors in the coal mining haulage system [44].

$$
P(A)=\frac{x}{n}
$$

In Equation (8), $P(A)$ represents the a priori probability of the risk factor, $x$ represents the frequency of the risk factor, and n represents the total number of accident occurrences.

Step 3: Calculate the posterior probability of coal mine transportation accidents. The GeNle 2.1 is chosen to build the BN model of the CMTS in order to update the prior probabilities of the root node and the logical relationships between nodes. This allows for backward reasoning to obtain the posterior probabilities of the nodes. The BN model's backward reasoning can be used to predict the outcome factors based on the certain occurrence of the causal factors or to infer the key factors leading to the occurrence of the outcome based on the known outcome factors. In this study, the target node is set as a leaf node and its probability is set to $100 \%$ in the software. By updating the posterior probabilities, the risks of the coal mining haulage systems under accident conditions, including the horizontal haulage, inclined haulage, and vertical shaft hoisting systems, can be obtained. The posterior probability plays a crucial role in the Bayesian formula. It updates our probability estimates of events by considering both the prior probability and the observed data, providing more accurate and reliable risk assessment results. The expression of the posterior probability can be seen in Equation (9).

$$
P(B \mid A)=\frac{P(A \mid B) P(B)}{P(A)}
$$

In Equation (9), $P(A \mid B)$ represents the posterior probability of event $A, P(B \mid A)$ represents the conditional probability, also known as the likelihood, $P(B)$ represents the marginal probability of event $\underline{B}$, and $P(A)$ represents the prior probability. From Equation (9), we can derive the Bayesian theorem, which states that:

$$
P\left(B_{i} \mid A\right)=\frac{P\left(A \mid B_{i}\right) P\left(B_{i}\right)}{\sum_{i-1}^{n} P\left(A_{i} \mid B_{i}\right) P\left(B_{i}\right)}
$$

In Equation (10), $B_{1} \ldots B_{n}$ are pairwise mutually exclusive events, $I=1 \ldots n$, which constitute a complete event. There exists an event $A$ that occurs simultaneously with events $B_{1} \ldots B_{n} . P\left(B_{i}\right)$ represents the prior probability and $P\left(B_{i} \mid A\right)$ represents the posterior probability.

Step 4: Identify key risk factors. In order to improve the accuracy of determining key factors, this study also involves determining the ranking of the importance of posterior probabilities of BN nodes. The calculation formula for the node importance in BN is as shown in Equation (11).

$$
I_{n}=P\left(B_{i} \mid A\right)-P\left(B_{i}\right)
$$

In Equation (11), $I_{n}$ represents the difference between the posterior probability and the prior probability of a BN node. The larger the value of $I_{n}$, the lower the ranking of node importance, indicating a higher probability of triggering hazards. This is used to determine the primary risk factors. $P\left(B_{i}\right)$ represents the prior probability and $P\left(B_{i} \mid A\right)$ represents the posterior probability.

Finally, based on the division of the coal mining transportation subsystem and a comparative analysis using the importance ranking of fault tree structure and posterior probability, the five key risk factors for each sub-transportation system are determined.

# 3.4. Risk Factor Analysis Based on PHA 

To delve deeper into the main risk factors identified through the integrated analysis of fault trees and Bayesian networks, the method of pre-hazard analysis is introduced. PHA is a systematic and scientific method for identifying and analyzing key risk factors associated with a particular activity or project. It aims to assess potential hazards, evaluate their likelihood and severity, and propose appropriate control measures to mitigate risks.

This paper presents PHA as a theoretical framework and methodological approach for risk factor analysis, and propose preventive measures. The specific steps of pre-hazard analysis are as follows:

Step 1: Determining the Likelihood of Risk Occurrence (L). Referring to Table 1, the likelihood of an adverse event occurring is evaluated based on four aspects: deviation frequency, safety inspection, operating procedures, and employee competency. The highest score among the four factors is taken as the final "L" value.

Table 1. Likelihood of risk occurrence.


Step 2: Determining the Severity Level of Risk Consequences (S). Referring to the China Measures for Reporting and Investigating Mining Production Safety Accidents (https:// www.chinaminesafety.gov.cn/zfxxgk/fdzdgknr/tzgg/202301/t20230118_440874.shtml, accessed on 16 March 2024) shown in Table 2, the severity of the consequences will be evaluated based on four aspects: personnel fatalities, personnel serious injuries, property damage, and workplace environment destruction. The highest score among the four items will be taken as the final " $S$ " value.

Table 2. Severity levels of risk consequences.


Step 3: Construction of Risk Matrix (RM). This research adopts the matrix analysis method, with the likelihood of risk events as the rows and the severity of risk event consequences as the columns, forming a matrix analysis table. The calculation formula for the risk matrix is shown in Equation (12) as follows:

$$
R=L \times S
$$

In Equation (12), $R$ represents the risk value, which is the combination of the likelihood of an accident occurring and the severity of its consequences. $L$ denotes the likelihood of the accident occurring, while $S$ represents the severity of the accident consequences. A higher value of $R$ indicates a greater level of risk, implying that the CMTS has a higher level of danger or hazard.

Based on the risk value $R$, an RM can be constructed to assess and classify risk factors according to the levels shown in Table 3.

Table 3. Risk matrix (RM).


Step 4: Risk Level Classification. According to the magnitude of the risk value R, the risk levels can be divided into four categories, as shown in Table 4.

Table 4. Risk level classification.


Step 5: Develop relevant preventive measures. Finally, for the causes and consequences of the accident, corresponding preventive measures are developed for each risk event.

# 4. Example 

### 4.1. Example Illustration

To illustrate the effectiveness of the FTA-BN-PHA method in accident analysis, we will provide an example of how to apply this method.

X coal mine was established in December 1992 and commenced production in December 1996. The mining field of the mine currently covers an area of approximately 7.27 square kilometers, occupying 442.89 acres. It has geological reserves of 174.62 million tons and recoverable reserves of 10,026.76 million tons. The current production capacity is 1.5 million tons per year and the remaining service life of the mine is 50 years. The transportation tasks at $X$ coal mine include the main transportation tasks for the working face, transportation roadway, and main transportation shaft, as well as auxiliary transportation

tasks for personnel and materials. The specific transportation tasks and distribution of transportation tools are shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. X distribution of coal mine transportation tasks.
Figure 4 illustrates the main transportation system at $X$ coal mine, which consists of production equipment such as belt conveyors, scraper conveyors, crushers, and loaders, as well as tunnels and coal bunkers. The black arrows represent the flow of coal in the CMTS, while the red arrows represent the flow of materials. According to the distribution of transportation tasks and the knowledge related to coal mine transportation, the related transportation systems of $X$ coal mine are divided into the following categories (as shown in Table 5).

Table 5. Components of X CMTS.


![img-3.jpeg](img-3.jpeg)

Figure 4. Components and layout of X CMTS.
According to Figure 4 and Table 5, coal is transported from four working faces through sub-transportation systems to the public transportation system and then stored in 0 (ground raw coal storage).

# 4.2. Constructing Fault Tree Model-CMTS 

According to the aforementioned methodology, fault tree model-CMTS is constructed.
Step 1: Using the $X$ coal mine transportation system accident as the top event, represented by "T," the flat roadway transportation system, inclined roadway transportation system, and lifting transportation system of the $X$ coal mine are represented as intermediate events in the first layer of the accident tree. Take the first-level intermediate events of the CMTS accident as the top events of the accident sub-trees, denoted as " $\mathrm{T}_{1}, \mathrm{~T}_{2}, \mathrm{~T}_{3}$," respectively, to establish the accident sub-tree model of the $X$ coal mine. The risk events for each transportation system, categorized by attribute, are presented in Tables 6-8. Next, we will construct FTA models for the CMTS based on the three different types of accidents. Following the accident tree analysis process, a fault tree model of the CMTS is established, as shown in Figure 5. With the help of the expert system and the field investigation in the $X$ coal mine, the risk factors of the coal mine transportation system were determined by the method of Chinese excavation in Section 3.1, as shown in Tables 6-8, respectively.

Table 6. Risk events of the coal mine level roadway transportation system.


Table 7. Risk events of the coal mine inclined roadway transportation system.


Table 8. Risk events of the coal mine vertical shaft lifting transportation system.


![img-4.jpeg](img-4.jpeg)

**Figure 5.** Construction of fault tree model-CMTS. (**a**) represents the accident tree of the coal mine level roadway transportation system, (**b**) represents shows the accident tree of an inclined roadway transportation system in the coal mine, (**c**) represents shows the accident tree of the coal mine vertical hoisting transportation system.

Figure 5a shows the accident tree of the coal mine level roadway transportation system, in which $T_{1}$ is the top event, namely the coal mine level transportation accident, and the intermediate event $A_{i}$ and the basic event $X_{i}$ are shown in Table 6.

Figure 5b shows the accident tree of an inclined roadway transportation system in the coal mine. The top event is $T_{2}$, namely the coal mine inclined roadway transportation accident. The main construction process of the fault tree is consistent with the drift transportation accident. The factors represented by the intermediate event $B_{i}$ and the basic event $Y_{i}$ are shown in Table 7.

Figure 5c shows the accident tree of the coal mine vertical hoisting transportation system, $\mathrm{T}_{3}$ shows the hoisting transportation accident of the top event, and the factors represented by the intermediate event $C_{i}$ and the basic event $Z_{i}$ are shown in Table 8.

Step 2: In this step, it is necessary to find the structural function of the fault sub-trees of a coal mine transportation accident first. According to Equations (3) and (4), the instantiated Equations (12)-(14) can be expressed as follows, respectively.

The structure function of the fault tree for the level roadway transportation accidents in coal mines is given by Equation (12):

$$
\begin{gathered}
\Phi(X)=\left(X_{1}\right) \times\left(X_{19}+X_{20}\right)+\left(X_{2}+X_{3}+X_{4}\right)+\left(X_{5}+X_{6}\right)+\left(X_{7}+X_{8}\right) \\
+\left(X_{9}+X_{10}+X_{11}\right)+\left(X_{12}+X_{13}\right)+\left(X_{14}+X_{15}+X_{16}\right)+\left(X_{17}+X_{18}\right)
\end{gathered}
$$

The structure function of the fault tree for the inclined roadway transportation accidents in coal mines is given by Equation (13):

$$
\begin{gathered}
\Phi(Y)=\left(Y_{1}\right)+\left(Y_{2}\right)+\left(Y_{3}\right)+\left(Y_{4}+Y_{5}\right)+\left(Y_{6}+Y_{7}\right)+\left(Y_{8}+Y_{9}\right)+\left(Y_{10}+Y_{11}\right) \\
+\left(Y_{8}+X_{9}\right)+\left(X_{10}+Y_{11}\right)+\left(Y_{12}+Y_{13}\right)+\left(Y_{14}+Y_{15}\right) \times\left(Y_{16}+Y_{17}+Y_{18}\right) \\
+\left(Y_{19}+Y_{20}+Y_{21}\right)+\left(Y_{22}+Y_{23}+Y_{24}\right)
\end{gathered}
$$

The structure function of the fault tree for the vertical shaft hoisting transportation accidents in coal mines is given by Equation (14):

$$
\begin{gathered}
\Phi(Z)=\left(Z_{1}\right)+\left(Z_{2}\right)+\left(Z_{3}+Z_{4}+Z_{5}\right)+\left(Z_{6}\right)+\left(Z_{7}\right)+\left(Z_{8}\right)+\left(Z_{9}+Z_{10}\right) \\
+\left(Z_{11}+Z_{12}+Z_{13}\right) \times\left(Z_{14}+Z_{15}\right)+\left(Z_{16}+Z_{17}+Z_{18}\right) \\
+\left(Z_{19}+Z_{20}\right)+\left(Z_{21}+Z_{22}\right)+\left(Z_{23}+Z_{24}+Z_{25}\right)
\end{gathered}
$$

Next, by using the bottom-up method to simplify the equations mentioned above, the first-order minimal cut sets and second-order minimal cut sets of the CMTS accident tree are obtained as shown in Table 9.

Table 9. The first-order minimal cut sets and second-order minimal cut sets.

\end{gathered}


Based on Table 9, it is evident that the coal mine level roadway transportation system has a total of 19 minimal cut sets, comprising 17 first-order minimal cut sets and 2 s -order minimal cut sets. Similarly, the coal mine inclined roadway transportation system exhibits 25 minimal cut sets, including 19 first-order minimal cut sets and 6 s -order minimal cut sets. In the case of the coal mine vertical shaft hoisting transportation system, there are 26 minimal cut sets, with 20 first-order minimal cut sets and 6 s -order minimal cut sets. These findings emphasize that even a single or dual occurrence of basic events can pose significant risks of transportation accidents in coal mines.

Step 3: According to the obtained minimum cut set and the structural importance formula in Section 2.1, the basic event structural importance of coal mine transportation accidents is obtained and ranked. The resulting structural importance of the basic events is presented and ranked in Tables 10-12.

Table 10. Importance of basic event structure of the coal mine level roadway transportation system.


Table 11. Importance of basic event structure of the coal mine inclined roadway transportation system.


Table 12. Importance of basic event structure of the coal mine vertical shaft lifting transportation system.


As shown in Table 13, the structural importance of the fault tree is divided into three levels. The higher the importance level, the greater the impact on coal mine transportation accidents.

Table 13. The classification of structural importance levels for fault tree analysis.


# 4.3. Mapping the FTA to BN

Step1: the accident tree model obtained in Section 4.2 is transformed into a BN structure using mapping techniques. The resulting mapped Bayesian network structure is shown in Figure 6.

Step2: the risk probability frequency of each root node in the transportation systems is calculated using the risk probability frequency formula. Subsequently, the prior probability $P(A)$ of each risk factor in the CMTS is determined using the prior probability calculation formula. The calculated risk probability frequency and prior probabilities $P(A)$ for the CMTS are presented in Tables 14-16.

Table 14. Prior probabilities of risk factors in the coal mine level roadway transportation system.


Table 15. Prior probabilities of risk factors in the coal mine inclined roadway transportation system.


![img-5.jpeg](img-5.jpeg)

**Figure 6.** Bayesian network structure of CMTS. (**a**) represents the BN structure for the level roadway transportation system in coal mining, (**b**) represents the BN structure for the inclined roadway transportation system in coal mining, (**c**) represents the BN structure for the vertical shaft lifting transportation system in coal mining.

Table 16. Prior probabilities of risk factors in the coal mine vertical shaft hoisting transportation system.


Figure 6a shows the BN structure for the level roadway transportation system in coal mining. The risk factor frequencies and prior probabilities can be found in Table 14.

Figure 6b shows the BN structure for the inclined roadway transportation system in coal mining. The risk factor frequencies and prior probabilities can be found in Table 15.

Figure 6c shows the BN structure for the vertical shaft lifting transportation system in coal mining. The risk factor frequencies and prior probabilities can be found in Table 16.

Step 3: Prior probabilities and node logical relationships are updated using GeNIe 2.1 to establish the GeNIe model for the CMTS as shown in Figure 7. In Figure 7, (a) represents the GeNIe model for the level roadway transportation system in coal mining, (b) represents the GeNIe model for the inclined roadway transportation system, and (c) represents the GeNIe model for the vertical shaft lifting transportation system.
![img-6.jpeg](img-6.jpeg)

Figure 7. Cont.

![img-7.jpeg](img-7.jpeg)

Figure 7. GeNIe model of CMTS.
Then, using the probability update of the BN, the target node is set as the leaf nodes and, in GeNIe 2.1, its probability is set to $100 \%$ for backward reasoning (as shown in Figure 8a). This allows for the determination of the posterior probabilities and importance ranking of each network node under the accident conditions. The analysis results are presented in Tables 17-19.

![img-8.jpeg](img-8.jpeg)

Figure 8. Comparison of the risk analysis results of the coal mine level roadway transportation system.

Table 17. Posterior probability of risk factors in the coal mine level roadway transportation system.

Probability | Importance
Ranking | Root Node | Posterior
Probability | Importance
Ranking  |

Table 18. The posterior probability of risk factors in the coal mine inclined roadway transportation system.

Probability | Importance
Ranking | Root Node | Posterior
Probability | Importance
Ranking  |

Table 19. The posterior probability of risk factors in the coal mine vertical shaft hoisting transportation system.


Analysis of Table 17 reveals that the posterior probabilities of each network node have increased compared to the prior probabilities. Based on the magnitude of the increase, the importance ranking of the posterior probabilities for the nodes is as follows: ( $\mathrm{X}_{11}$ Violation of Scraping Vehicle Regulations, $\mathrm{X}_{15}$ Belt Conveyor Belt Breakage) $>\left(\mathrm{X}_{4}\right.$ Inadequate Information Communication, $\mathrm{X}_{17}$ Controller Failure) $>\left(\mathrm{X}_{5}\right.$ Improper Equipment Protection, $\mathrm{X}_{12}$ Failure to Pay Attention to Warning Signals, $\mathrm{X}_{19}$ Limited Space, $\mathrm{X}_{20}$ Presence of Obstacles) $>$ ( $\mathrm{X}_{2}$ Inappropriate Deployment, $\mathrm{X}_{6}$ Delayed Maintenance, $\mathrm{X}_{9}$ Inappropriate Job Assignment, $\mathrm{X}_{18}$ Rusting of Parts) $>\left(\mathrm{X}_{3}\right.$ Inadequate Supervision, $\mathrm{X}_{8}$ Failure of Audio-Visual Signals, $\mathrm{X}_{14}$ Deviation of Transporter) $>\left(\mathrm{X}_{1}\right.$ Insufficient Tunnel Lighting, $\mathrm{X}_{7}$ Failure of Sand Spraying Device, $\mathrm{X}_{10}$ Violation of Roof Support Regulations, $\mathrm{X}_{16}$ Abnormal Speed).

A lower ranking indicates a higher probability of causing risks. Therefore, nodes $\mathrm{X}_{11}$ (Violation of Scraping Vehicle Regulations), $\mathrm{X}_{15}$ (Belt Conveyor Belt Breakage), $\mathrm{X}_{4}$ (Inadequate Information Communication), and $\mathrm{X}_{17}$ (Controller Failure) have a higher probability of causing accidents in the coal mining level roadway transportation system compared to the other factors.

Analysis of Table 18 indicates that the importance ranking of posterior probabilities for nodes in the BN model of the inclined roadway transportation system is as follows:
$\left(Y_{6}\right.$ Mine Car Wheel Dislodgment, $Y_{10}$ Pedestrians during Vehicle Operation) $>\left(Y_{3}\right.$ Failure to Issue Warning Signals, $\mathrm{Y}_{16}$ Wear or Corrosion, $\mathrm{Y}_{23}$ Pin Ejection or Fracture) $>\left(\mathrm{Y}_{2}\right.$ Severe Noise Pollution, $\mathrm{Y}_{12}$ Unauthorized Leave from Post, $\mathrm{Y}_{13}$ Overspeed or Overload Driving, $\mathrm{Y}_{17}$ Insufficient Strength, $\mathrm{Y}_{20}$ Uninserted or Partially Inserted Pins, $\mathrm{Y}_{24}$ Hook, Chain, or Rope Buckle Failure) $>\left(\mathrm{Y}_{1}\right.$ Uncomfortable Temperature, $\mathrm{Y}_{4}$ Inadequate Staffing, $\mathrm{Y}_{11}$ Failure to Evade Timely, $\mathrm{Y}_{15}$ Sudden Interruption of Operation, $\mathrm{Y}_{18}$ Knotting, $\mathrm{Y}_{21}$ Failure to Hang Hook, Chain) $>\left(\mathrm{Y}_{7}\right.$ Axle Breakage, $\mathrm{Y}_{14}$ Excessive Acceleration, $\mathrm{Y}_{19}$ Failure to Use Safety Rope) $>\left(\mathrm{Y}_{5}\right.$ Poor Emergency Response, $\mathrm{Y}_{8}$ Hazardous Gases, $\mathrm{Y}_{9}$ Dust Pollution, $\mathrm{Y}_{22}$ Chain Link Fracture).

This indicates that the risk factors of $\mathrm{Y}_{6}$ (Mine Car Wheel Dislodgment), $\mathrm{Y}_{10}$ (Pedestrians during Vehicle Operation), $\mathrm{Y}_{3}$ (Failure to Issue Warning Signals), $\mathrm{Y}_{16}$ (Wear or Corrosion), and $\mathrm{Y}_{23}$ (Pin Ejection or Fracture) have a significant impact on accidents in the inclined roadway transportation system.

Analysis of Table 19 reveals that the importance ranking of posterior probabilities for nodes in the BN model of the vertical shaft lifting transportation system is as follows: $\left(Z_{3}\right.$ Violation of Passage Regulations, $Z_{6}$ Signal Device Failure) $>\left(Z_{11}\right.$ Driver Violation, $Z_{13}$ Overspeed, Overload, $Z_{25}$ Connector Failure) $>\left(Z_{2}\right.$ Inappropriate Mining Depth, $Z_{5}$ Violation of Operations, $Z_{7}$ Equipment Deterioration, $Z_{14}$ Failure to Provide Warning Alerts, $Z_{15}$ Failure to Handle Hazards as Required, $Z_{18}$ Spring Fatigue, $Z_{21}$ Wear) $>\left(Z_{1}\right.$ Inadequate Lighting, $Z_{4}$ Unauthorized Riding, $Z_{9}$ Excessive Inclination, $Z_{20}$ Failure of

Leakage Protection, $\mathrm{Z}_{22}$ Corrosion) $>\left(\mathrm{Z}_{8}\right.$ Overwinding of Container, $\mathrm{Z}_{12}$ Driver Fatigue, $\mathrm{Z}_{16}$ Brake Disc Misalignment, $\mathrm{Z}_{17}$ Brake Shoe Wear, $\mathrm{Z}_{19}$ Leakage) $>\left(\mathrm{Z}_{10}\right.$ Narrow Passage, $\mathrm{Z}_{23}$ Pin Fracture, $\mathrm{Z}_{24}$ Connector Failure).

This indicates that the risk factors of $Z_{3}$ (Violation of Passage Regulations), $Z_{6}$ (Signal Device Failure), $\mathrm{Z}_{11}$ (Driver Violation), $\mathrm{Z}_{13}$ (Overspeed, Overload), and $\mathrm{Z}_{25}$ (Connector Failure) have a significant impact on accidents in the vertical shaft lifting transportation system.

Step 4: in this step, to enhance the accuracy of key factor determination, this study conducted a comparative analysis between the results of structural importance calculation in the fault tree and posterior probability analysis in the Bayesian network. The aim was to identify the top five risk factors with higher probability for subsequent detailed analysis. The comparative analysis results are presented in Figures 8-10.
![img-9.jpeg](img-9.jpeg)

Figure 9. Comparison of the risk analysis results of the coal mine inclined roadway transportation system.
![img-10.jpeg](img-10.jpeg)

Figure 10. Comparison of risk analysis results of the coal mine vertical shaft hoisting transportation system.

The analysis results in Figure 8 indicate that $\mathrm{X}_{4}$ (Delayed Communication), $\mathrm{X}_{11}$ (Unauthorized Riding), $\mathrm{X}_{15}$ (Belt Conveyor Belt Breakage), and $\mathrm{X}_{17}$ (Controller Failure) are the major risk factors of the coal mine level roadway transportation system.

The analysis results in Figure 9 indicate that $\mathrm{Y}_{6}$ (Mine Car Wheel Dislodgment), $\mathrm{Y}_{10}$ (Pedestrians during Vehicle Operation), $\mathrm{Y}_{3}$ (Failure to Issue Warning Signals), $\mathrm{Y}_{16}$ (Wear or Corrosion), and $\mathrm{Y}_{23}$ (Pin Ejection or Fracture) are the major risk factors of the coal mine inclined roadway transportation system.

The analysis results in Figure 10 show that $Z_{3}$ (illegal traffic), $Z_{6}$ (Signal Device Failure), $Z_{11}$ (driver violation), $Z_{13}$ (overspeed and overweight), and $Z_{25}$ (connector failure) are the main risk factors of the coal mine vertical shaft hoisting transportation system.

# 4.4. PHA and Pre-Control Measures 

Finally, based on the comparative analysis results, a preliminary hazard analysis and relevant countermeasures are proposed for the key risk factors in the coal mine level roadway transportation system (refer to Table 20), inclined roadway transportation system (refer to Table 21), and vertical shaft transportation system (refer to Table 22).

Table 20: Pre-hazard analysis of the coal mine level roadway transportation system.


Table 21. Pre-hazard analysis of the coal mine inclined roadway transportation system.


Table 22. Pre-hazard analysis of the coal mine vertical shaft hoisting transportation system.


# 5. Conclusions and Future Work 

This paper presents a coal mine transportation system accident analysis method based on FTA-BN-PHA, which utilizes FTA, BN, and PHA to identify major risk factors and reduce the probability of transportation accidents. The main innovations and usability regarding ensuring the safe operation of the CMTS are as follows:
(1) This paper introduces an integrated risk analysis model for CMTS by combining the principles of FTA, BN, and PHA. Its execution logic can be summarized as follows: a CMTS risk and safety assessment FTA model is transformed into a BN-based CMTS accident network model by calculating the posterior probabilities of various risk factors and determining the main risk factors. Then, a risk-matrix-based PHA method is used to classify the levels of danger and provide effective pre-control measures for CMTS.
(2) The usability of our study holds significant practical value in the field of coal mine risk management. Through the analysis of real-world case studies, our study provides valuable insights into effective strategies and practices for mitigating risks in SMTS, which can be directly applied by coal mine operators to enhance safety measures and reduce potential hazards. Furthermore, our research offers engineering guidance by providing recommendations and guidelines for implementing risk management techniques in CMTS, which can also assist engineers and decision makers in making informed decisions to ensure the safety and efficiency of coal mining operations.
(3) Due to the complex and special working environment of the coal mine conveying system, there are many types of factors that affect the safety of production, and there are various differences between different coal mines, which have the characteristics of unobserved heterogeneity [45] and ambiguity. Therefore, the risk analysis method that does not take into account the above characteristics has certain limitations in determining the degree of risk, and it is debatable whether this method can be applied to most coal mine transportation systems. In the follow-up system research, the polymorphism of risk nodes should be considered and the concepts of fuzzy state, digital twin, and game model [46] should be introduced to make the calculation of risk probability more accurate.

Author Contributions: Conceptualization, L.H.; Methodology, Y.W. (Yue Wu); Data curation, Y.W. (Yafei Wang), J.G., T.X. and N.Z.; Writing—original draft, R.P.; Supervision, X.Z. All authors have read and agreed to the published version of the manuscript.
Funding: This research is supported by the China National Natural Science Foundation 52204174, 52074210, China Postdoctoral Science Foundation 2022MD723828, Shaanxi Postdoctoral Science Foundation 2023BSHTBZZ44, and Shaanxi University Youth Innovation Team Foundation 23JP096.
Data Availability Statement: The data presented in this study are available on request from the corresponding author.
Conflicts of Interest: The authors declare no conflict of interest.
