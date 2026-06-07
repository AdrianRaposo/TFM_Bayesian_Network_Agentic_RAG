# Integrated Bayesian and association-rules methods for autonomously orienting COVID-19 patients 

Adel Thaljaoui ${ }^{1} \cdot$ Salim El Khediri ${ }^{2,3} \cdot$ Emna Benmohamed ${ }^{3,4} \cdot$ Abdulatif Alabdulatif ${ }^{5} \cdot$ Abdullah Alourani ${ }^{1}$<br>Received: 25 October 2021 / Accepted: 17 September 2022 / Published online: 7 October 2022<br>© International Federation for Medical and Biological Engineering 2022


#### Abstract

The coronavirus infection continues to spread rapidly worldwide, having a devastating impact on the health of the global population. To fight against COVID-19, we propose a novel autonomous decision-making process which combines two modules in order to support the decision-maker: (1) Bayesian Networks method-based data-analysis module, which is used to specify the severity of coronavirus symptoms and classify cases as mild, moderate, and severe, and (2) autonomous decisionmaking module-based association rules mining method. This method allows the autonomous generation of the adequate decision based on the FP-growth algorithm and the distance between objects. To build the Bayesian Network model, we propose a novel data-based method that enables to effectively learn the network's structure, namely, MIGT-SL algorithm. The experimentations are performed over pre-processed discrete dataset. The proposed algorithm allows to correctly generate $74 \%, 87.5 \%$, and $100 \%$ of the original structure of ALARM, ASIA, and CANCER networks. The proposed Bayesian model performs well in terms of accuracy with $96.15 \%$ and $94.77 \%$, respectively, for binary and multi-class classification. The developed decision-making model is evaluated according to its utility in solving the decisional problem, and its accuracy of proposing the adequate decision is about $97.80 \%$.


Keywords Autonomous decision-making $\cdot$ Bayesian networks $\cdot$ Variable approach $\cdot$ Bayesian network's structure learning based on data approach $\cdot$ COVID-19

[^0]
## 1 Introduction

In the last few months and owing to the global pandemic of COVID-19, the world's healthcare systems have been facing crippling challenges. The total number of deaths because of this disease reached 5,705,754 deaths in February 04, 2022 (888.113 USA) [1], making it one of the deadliest pandemics that humanity has endured [2]. The quarantine procedure represents an important decision in limiting the rapid spread of pandemic for the non-severe cases, but it is not enough to reduce the mortality rate. Therefore, governments are asking researchers in different fields like medicine, chemistry, physics, computer science, and mathematics, to collaborate in order to propose an efficient solution to put an end to this pandemic. Yet, no efficacious medication was developed to this day other than full medical support [3]. Meanwhile, Wang et al. [4] mentioned that the earlier discovery of the infection is considered a crucial task in the treatment process ulteriorly. Hence, the sooner the symptoms are detected, the sooner the proper medication and care are provided.


[^0]:    Salim El Khediri
    salim.el.khediri@gmail.com
    Adel Thaljaoui
    adel.t@mu.edu.sa
    Emna Benmohamed
    emna.benmohamed.tn@ieee.org
    Abdulatif Alabdulatif
    Abdulatifau@hotmail.com
    Abdullah Alourani
    a.alourani@mu.edu.sa
    1 Department of Computer Science and Information, College of Science at Zalfi, Majmaah University, Al-Majmaah 11952, Saudi Arabia
    2 Department of Information Technology, College of Computer, Qassim University, Buraydah, Saudi Arabia
    3 Department of Computer Sciences, Faculty of Sciences of Gafsa, University of Gafsa, Gafsa, Tunisia
    4 Research Groups in Intelligent Machines, University of Sfax, National School of Engineers (ENIS), BP 1173, 3038 Sfax, Tunisia
    5 Department of Computer Sciences, College of Computer, Qassim University, Buraidah, Saudi Arabia

Consequently, the mortality rate from the virus could be decreased [3].

Using Artificial intelligence (AI), several methods have been implemented to analyze chest radiographs due to its relevance for COVID-19 detection [5]. In [4, 6, 7, 8], and [9], the authors used deep learning methods for chest computer tomography (chest CT) analysis. Al-ganess et al. [10] introduced an improved Neuro-Fuzzy Inference System (ANFIS) called FPASSA-ANFIS to forecast the new confirmed cases in China. Pirouz et al. [10] proposed a novel binary classification technique in order to analyze the correlation among environmental parameters and confirmed cases [11]. Similarly, recent machine learning (ML) models were proposed to fight against COVID-19 like [12, 13, 14, 15, 16, 17, 18], and [19]. In [12], the probability of being infected is predicted based on the profile of the patient. As described in [13], a regression model is employed to detect the severity for the COVID-19 patients. Moreover, Wang et al. [14] suggested a Bayesian network meta-analysis (Bayesian NMA) to evaluate different methods of treatment in order to arrange an adequate treatment plan for asymptomatic patients. As defined in [14], an asymptomatic patient is a patient who has no apparent symptoms. Nevertheless, the obvious symptoms are useful for determining the severity of the disease for each case as explained in [15]. In this latter, Wu et al. [15] proposed a machine learning (ML) model to predict the severe and the non-severe classes based on clinical and laboratory features.

Machine learning-aided diagnosis represents an efficient procedure in fighting against COVID-19. For this reason, several works have been introduced. However, as far as we know, they mainly aimed to predict the severity and the physician is the one responsible for orienting coronavirus patients. In fact, analyzing a vast data requires a high cognitive load in order to improve the clinical care. In addition, this pandemic reveals the limited healthcare resources like hospital beds, ventilators, and clinical staff. Due to these limits and the human nature, supporting physicians and giving the proper orientation to COVID-19 patients have proven challenging.

As a result of the alarming death rate caused by the COVID-19 worldwide, and considering the advantages of the early diagnosis of case's severity in decreasing this rate, the current study introduced an Autonomous-Decision-Making process (ADM) based on hybrid data analysis approaches. A persuasive advantage of BN, as a datadriven method, is that it does not need a hugely large dataset. Moreover, BN can combine the elicited expert knowledge and generate accurate Decision Support Systems (DSSs). Relying on these points and motivated by open BN structure learning problem (NP problem), we proposed a novel method named MIGT-SL algorithm. In addition, to further support the decision-maker, we proposed to combine the capability of the graphical probabilistic model with the simplicity of the association rules mining method to analyze the characteristic symptoms for determining the severity of the cases and the appropriate decision that needs to be taken. This mining method allows to help understand the case's severity and the affected orientation. To resume, this work seeks to create a ML-based tool to support the decisionmaker by benefiting from the BN's properties, involving performing reliable prediction and robust decision-making process under different uncertainty sources.

The rest of the paper is structured as follows: Section 2 presents the theoretical foundations used to build our proposal. Section 3 is dedicated to describing the autonomous decision-making process based on the improvement of the Bayesian networks and the association rules methods. To build the discrete BN model, we proposed a novel structure learning algorithm based on data approach (MIGT-SL algorithm). In addition, we employed the generated rules to make the proper decision autonomously for each decisional situation. In Section. 4, we described the application and the experimental results of the proposed process for fighting against the novel coronavirus. Section 5 aims to evaluate our proposal based on the cited papers in the literature and to outline the added value of our model compared to other models that have been proposed to fight against COVID-19. Finally, Section 6 is consecrated to summarizing the proposed contribution and to offering further future works.

To illustrate the proposed autonomous orientation method, the integrated models are described in the different parts of the paper, as shown in the following flowchart:

## 2 Preliminaries

A key challenge in limiting the horizontal spread of COVID19 is the early identification of infected cases in order to apply the quarantine decision. The aim of the Autonomous System for Decision-Making (ADMS) is to enable the decision-maker to determine on his/her own the right decision to take (hospitalization, isolation, medical attention). Owing to its accuracy, ADMS enables the reduction of the number of infected cases, supports users in decision-making, and minimizes the high load received by the medical service units. In this section, we present the theoretical concepts needed for the achievement of the autonomous decision-making. In fact, the process of ADM consists of two complementary modules: (1) module 1 is used initially to predict the case's severity based on the detected symptoms by employing the Bayesian Network (BN) and (2) module 2 to autonomously specify the adequate decision based on the obtained results using the Association Rules method (AR).

Since our aim here is to introduce an Autonomous System for Decision-Making (ADMS) based on Bayesian model

construction and association rules mining, we have to start with the presentation of the concepts in question before introducing the proposed methodology.

### 2.1 Bayesian network

A Bayesian network, or for short BN, is a Probabilistic Graphical Model (PGM). Formally, BN is denoted as a couple (Gr, Pr) where Gr is defined as directed acyclic graph DAG and Pr represents the conditional probability distributions. The DAG, which is denominated as the couple ( N , E) represents the relations between N nodes. These nodes represent the characteristic random variables, which are linked by a set of directed edges E that indicate the conditional dependencies. Each edge E between two nodes represents a directed dependence or "causation" relation. The conditional probability distributions express for each node the conditional probabilities regarding its parents [20]. The joint probability distribution for the network is calculated using the following equation: $P(G r)=P\left(N_{1}, N_{2}, \ldots, N_{m}\right)=\prod_{i=1}^{m} P\left(N_{i} \mid P a\left(N_{i}\right)\right)$ where $\mathrm{Pa}(\mathrm{N})$ corresponds to the parent of the node N and m represents the total number of the nodes included in the graph. In order to build the Bayesian model, two phases should be performed in order to learn its structure and parameters. At the qualitative level, the BN structure learning represents the process of the extraction of the relations between nodes. The discovered relations indicate the conditional dependencies between random variables. At the quantitative level, learning the parameters of the network is done by calculating the probability distributions. The application in a given domain requires the construction of a specific BN model for this particular field.

To resolve the challenging problem of BN structure learning, several methods, which are based either on the data or on the expert's knowledge, have been proposed. The expert-driven approach has been used in several works like in [21, 22], and [23] in order to reduce the complexity of the search's space. In fact, creating the BN structure based only on this approach is very difficult; consequently, many errors can be generated [24]. On the other hand, the data-based approach for BN structure learning has been employed in different works like [25, 26, 27, 28, 29], and [30]. Therefore, based only on the input data for learning the BN topology is judged as NP hard problem because of the number of candidate graphs that is super exponential in the variables' number [20] [31]. The identification of the structure that best matches the data among the possible structures is achieved based on the highest score. In this regard, different scoring functions have been introduced like the BDeu score (Bayesian Dirichlet equivalence uniform), the BIC score (Bayesian Information Criteria), the K2 score, and the AIC score (Akaike Information Criteria) [32].

### 2.2 Association rules

Association rules, which was first introduced in 1990, is one of the most important techniques of data mining [33]. This technique allows the discovery of associative rules by reflecting the interesting correlation or association between items in a huge number of data [34]. For each association rule, a set of parameters should be specified, such as the support and the confidence. To discover the association rules, the Apriori algorithm [35] [36] was proposed; this algorithm is ranked the fourth among the top ten data mining methods. Apriori algorithm analyzes the dataset many times in order to determine the frequent items [37]. An improvement of Apriori algorithms, called FP-Growth algorithm [38], is known for discovering the association rules rapidly. Hence, the FP-Growth is more effective than the Apriori algorithm [39][39][39]. The FP-growth algorithm is based on a divide and conquer approach.

In the FP-growth method, building the FP-tree represents the key phase. Furthermore, the main feature of FP-Tree is treated as the data structures of this algorithm. Due to its rapidity for large datasets and its superior efficiency, in the present paper, we employ this algorithm to extract the association rules in order to construct the autonomous decision-making process. In the following parts of the paper, we provide more details on how to employ the BN model and the variable approach based on association rules to aid the decision maker.

## 3 Integrated methodologies for autonomous decision-making process

Figures 1 and 2 gives an overview of the proposed process for Autonomous Decision-Making (ADM) to fight against COVID-19. This process consists of two modules, which are "module 1" for data classification based on BN model and "module 2" for decision-making. The BN model is built based on the given dataset. To build the BN model, two learning phases should be carried out, and then a new scenario can be identified using the forward inference. The FP-Growth algorithm is employed to discover the association rules that are created using the frequent items and included in the ruleset. In the second module, we determine the nearest object to the new object using pairwise comparison and the variable approach.

As illustrated in Fig. 2, we used the given rules to determine the corresponding decision for the new object (as described in Section 3.2). Figure 2 shows the complementarity of the proposed modules as exhibited by green arrow

Fig. 1 Flowchart of the description of the autonomous orientation method

![img-0.jpeg](img-0.jpeg)
indicating the new object characterized by the predicted class of severity. This latter is identified using the forward inference method of the constructed BN model based on the new structure learning algorithm (as illustrated in Section 3.1). The defined class (mild, moderate, or severe) represents the main factor for orienting the patient in order to fight against this pandemic. In addition, the new object with the new decision allows the update of the dataset and the ruleset for future scenarios (as represented by the feedback arrow).

### 3.1 Module 1: BN model-based classification

As explained in Section 2.1, structure learning is considered as NP-hard problem. The proposed approach to address this problem is based on the Mutual Information
computation and the graph theory. Hence, it was named Mutual Information and Graph Theory-based Structure Learning method (MIGT-SL). By using this method, our goal is to learn the optimal Bayesian Network structure in a reasonable time. In MIGT-SL algorithm, we utilize the dependent nodes having the maximum MI, and then we apply the acyclic condition in order to create the Direct Acyclic Graph (DAG). As shown in Fig. 3, the MIGT-SL method consists of two main phases, which are:

1) Extracting the dependency graph to learn the Undirected Acyclic Graph (UAG).
2) Specifying the edges orientation to orient the Undirected Acyclic Graph.

Fig. 2 Autonomous DecisionMaking (ADM) process

![img-1.jpeg](img-1.jpeg)

Fig. 3 Schematic representation of the MIGT-SL algorithm

![img-2.jpeg](img-2.jpeg)

The first phase permits the extraction of the dependencies between each pair of variables within the dataset to create the UAG. For this reason, we avoid the links between nodes that form a cyclic structure. Furthermore, we only take into account the strong dependencies to determine the network's topology. The produced UAG is then explored to define the parent and child nodes in each link. This step is iteratively repeated in the process of orienting the edges in the UAG. Finally, we obtain the Directed Acyclic Graph representing the dependency relationships between variables. The degree of correctness of the graph is crucial for defining the correct probability distribution and classifying the introduced instances. In addition, via the network's topology and probabilities, we provide a visualization of the useful knowledge which enables the user to better analyze the given dataset.

To describe the mode of action of our method, we use two main notions, namely, Strongly Connected Nodes (SCN) and Strongly Connected Nodes Graph (SCNG). This latter designates the graph that involves the nodes representing the strongly connected nodes. In the undirected graph, the connectivity means that each node can attain another node through any path. We can define the strong connectivity or the strongly connected nodes only in the directed graphs.

### 3.1.1 Learning the UAG

The first phase for building the BN model (first box framed in green in Fig. 3) allows to construct the UAG using the input data. To create this graph, we employ the Information Theory (IT). By calculating the Mutual Information (MI) between each pair of nodes, we verify the connectivity between them and then eliminate the circuit or cyclic structure. To do this, based on the Graph Theory (GT), we avoid the cycle created between each tree nodes $\mathrm{X}, \mathrm{Y}$, and Z in respect of the acyclic characteristic of BNs. In our method named Mutual Information and Graph Theory-based Structure Learning (MIGT-SL), the MI between each pair of nodes is used to detect the SCN. Accordingly, we avoid the weak dependencies that correspond to erroneous edges.
The MI between two variables X and Y noted $\mathrm{I}(\mathrm{X}, \mathrm{Y})$ is computed as follows:
$I(X, Y)=H(X)-H(X \mid Y)$
$\mathrm{H}(\mathrm{X})$ represents the entropy of the variable X , and $\mathrm{H}(\mathrm{X} \mid \mathrm{Y})$ is the conditional entropy of X given Y . The $\mathrm{H}(\mathrm{X})$ is calculated using the following equation:
$H(X)=-\sum_{i=1}^{n} P\left(X_{i}\right) \log \left(P\left(X_{i}\right)\right)$
Mathematically, the conditional entropy of X given Y is calculated using this equation:
$H(X \mid Y)=\sum_{i=1}^{n} \sum_{j=1}^{m} P\left(X=x_{i}, Y=y_{j}\right) \times \log \left(P\left(X=x_{i}, Y=y_{j}\right)\right)$
To learn the Bayesian network structure, we employ the computation of MI that is widely utilized in the literature for learning the BN structure. As illustrated in Fig. 2, our proposal consists of two main modules for (1) learning the UAG represented in Algorithm 1 and (2) orienting its edges to create the Directed Acyclic Graph (DAG) as explained in Algorithm 2.

The proposed method for BNs structure learning is described in the following five steps.

1- Testing the dependencies between each pair of nodes.
2- Avoiding the non-SCN.
3- Constructing the UAG.
4- Verifying the degree of connectivity in the UAG between each pair of connected nodes.
5- Orienting each edge forming the UAG to create the final Directed Acyclic Graph (DAG).

In the following part of the paper, we explain how the introduced method for BNs structure learning works using the Asia network. This latter is considered as a reference network that is frequently used in BN structure learning

field. As shown in Fig. 4(a), this network is composed of 8 nodes and 8 edges, and it has the illustrated structure for 1000 samples. The first module represented in Algorithm 1 fulfills the first three steps indicated above. In the first step, based on the directivity property [41], we test the connectivity between each pair of nodes X and Y. For this reason, we test the existence of a third node Z that forms a cycle and fulfills the following condition:$$I(X;Y) \leq I(X;Z)+I(Z;Y)$$where MI between X and Y, denoted by I(X, Y), is less or equal to the sum of the MI between these two nodes and the third node Z that allows to form a cycle. In the second step, the aim is to avoid the formed cycles. As shown in Fig. 4(b), the two nodes A and T form a cycle with each of the remaining nodes (S, L, B, E, D, and X). Therefore, to eliminate these cycles, we have to discard the Markov chain condition. Thus, the following expression should be satisfied:$$\neg(I(X;Y) \leq I(X;Z) \wedge I(X;Y) \leq I(Z;Y))$$

As illustrated in Fig. 4(b), for instance, the connections between T and the rest of the nodes in the Asia network (except A) are weak. However, the nodes A and T are considered as SCN. For this reason, the weak associations are eliminated in the graph using red link. Then, in step 3, the obtained SCN are included in a Strongly Connected Nodes graphs (SCNGs). For Asia network, as shown in Fig. 4(b) five SCNGs are extracted, whichare SCNG1 (A, T), SCNG2 (L, S, B), SCNG3 (T, L, E),SCNG4 (X, E, D), and SCNG5 (E, B, D). Ultimately, thefinal UAG is produced by concatenating the obtainedSCN graphs involving the strong associations. The finalgraph (UAG) representing the output of Algorithm 1 isgenerated by concatenating the obtained SCN graphswhich involve the strong associations.

### 3.1.2 Orienting the UAG

The second phase of the proposed MIGT-SL method (second box framed in yellow in Fig. 3) aims to create the Directed Acyclic Graph (DAG). This module, which is described in Algorithm 2, incorporates the rest of the steps stated above. The first step in this module (step 4) is used for verifying the degree of connectivity between every pair of connected nodes in the obtained UAG. According to [43], the following equation allows the verification of the connectivity or the interdependency, noted Connectivity Degree (CD), between the nodes X and Y.$$CD(Y,X)=\frac{H(X|Y)}{X(X) \times |X|}$$where |X| represents the number of possible X values, and H(X) denotes the entropy of X, while H(X|Y) is the conditional entropy of X giving Y.

![img-3.jpeg](img-3.jpeg)

Fig. 4 An example of MIGT-SL algorithm application on Asia network: a the Asia original network, b dependencies between nodes, c edges orientation

Algorithm 1 Undirected graph learning


```
Input: Undirected acyclic graph
Output: sets of candidate parents and children
1.for i from 1 to N-1
2. for j from i+1 to N do
3. calculateMaxMI(i) \leftarrow Max(MI(i,j))
4. end for
5. end for
6. for i from 1 to N-1 do
7. for j from i+1 to N do
8. OEIJ \leftarrow calc_OE(i,j);
9. OEJI \leftarrow calc_OE(j,i);
10. MIij \leftarrow calc mutual information(i, j);
11. if (OEIJ + MIij > OEJI + & * MaxMI[i]) then
12. CandidateParent [j] \leftarrow i;
13. CandidateChild [i] \leftarrow j;
14. else if (OEJI + MIij > OEIJ + & * MaxMI[j]) then
15. CandidateParent [i] \leftarrow j;
16. CandidateChild [j] \leftarrow i;
17. end if
18. end if
19. end for
20. end for
```

Algorithm 2 Orienting the edges

In the second step (step 5), the test of the degree of connectivity means that for every pair of nodes, we examine the connectivity and specify of the parent node and the children. Thus, every edge between two nodes is oriented in the initial graph (UAG). To achieve this goal, we improve the CD criterion by combining the constraints introduced in [42] and [43] in order to identify the parent node (naturally, the other node represents the children). X is considered as the parent if the following conditional expression is fulfilled:
$\frac{H(Y \mid X)+I(X)}{H(Y) \times|Y|}>\frac{H(X \mid Y)+I(Y)}{H(X) \times|X|}+(\alpha \times \operatorname{Max}(M I(X)))$
where $\operatorname{Max}(\mathrm{MI}(\mathrm{X}))$ is the Maximum of Mutual Information values between the variable X and the other variables (all the graph's nodes except X ) and the coefficient $\alpha$ that satisfies the condition $\alpha \geq 0.5$. For Asia network for 1000 samples, noted Asia-1000, the extracted edges are oriented as illustrated in Fig. 4(c). As shown below, the node A is the parent of the node T that is the parent of the node E . As a result, the

Directed Acyclic Graph (DAG) is generated representing the learned structure for the used dataset (Asia-1000).

In this section, we describe our method for learning the BN structure based on the data-oriented approach. The learned dependencies obtained by the execution of the first algorithm are oriented based on the second algorithm, which is used for generating the final DAG. The main idea of structure learning method is based on the MI and the GT. In fact, the aim of this phase is to produce the closest topology to the correct one. Relying on the obtained structure, the BN parameters are learned in order to quantify the conditional dependencies between nodes. This task is exerted using the Expectation Maximization algorithm (EM). The following section will be dedicated to presenting the second module of our ADM process.

### 3.2 Module 2: decision-making

At the decision-making module, the set of generated rules is exploited to determine the adequate decision for the new patient based on the variable approach. The introduced approach is used to calculate the distance measure between every two objects in order to establish the proper decision. Each pair of objects has significant values for its features that are used to calculate the exact distance between them. The steps of the autonomous decision-making algorithm are as follows:

1- Cluster rules by the class's value where each group is arranged in order of confidence.
2- Computing the distance $\mathrm{D}(\mathrm{i}, \mathrm{j})$ between the new introduced object $j$ and every object $i$ in the corresponding group as follows:
$D(i, j)=\sum_{k=1}^{n}\left|F_{i k}-F_{j k}\right.$
Where n is the maximum number of features in the objects i and j , and $F_{i k}$ represents the value of the feature k of the object i.

Table 1 Sample view of the COVID-19 dataset


If $F_{i k}$ is included in the features list of the object i and not in that of the object $j$ (and vice versa), $D(i, j)$ is incremented by 1.
3- Assigning the decision that corresponds to the object with the minimum distance and the maximum confidence to the given object.
The proposed approach combines the classification method based on BN model and the variable approachbased distance calculation to attribute the proper decision that can be used to update the initial dataset and ruleset for future use in an autonomous manner. This process (ADM) was applied in the medical field, especially for predicting the severity of the cases and making the correct decision to fight against COVID-19.

## 4 Experimentation and results

### 4.1 Used dataset

The cleaned version of the original COVID-19 dataset [44] that was tested in [45] consists of 316,800 samples and 27 columns. The preprocessing phase consists of filtering columns like country, severity-none, and contact; grouping of similar variables (such as the columns of age with different intervals as explained in Table 1); and verifying the severity classes based on the suggested clinical studies including [3, 46, 47, 48], and [49]. These works describe the proper decision that corresponds to each class of severity.

As a result, we obtained the final COVID-19 dataset (refer to Table 1), which includes 106,298 samples. These samples represent the result of redundant rows deleting, each one with 11 symptoms, age, and severity class. Then, we split the COVID-19 data set that includes 106,298 samples into $80 \%$ ( 79,724 samples) for the training and $20 \%$ (26,574 samples) for the test. As already conducted by the studied researches, the patients (samples) are categorized into three different classes (mild, moderate, severe) based on the indicated symptoms. The aim of this paper is to analyze the relationships between these symptoms and the severity of the case for making the proper decision. The symptoms such as tiredness, dry cough, fever, sore throat, pains, runny nose, age, gender, and difficulty in breathing represent the basic clinical signs for indicating the COVID-19 severity [2]. [47] conducted a study on 99 patients, while [48] carried out a study on 21 patients and [49] did another study on 41 patients and they all specify cough, breathing difficulties, fever, chest pain, and sore throat as the main clinical manifestations of COVID-19. These symptoms were present in at least $1 \%$ of patients and in at most $98 \%$ of them.

As illustrated in Table 2, the variables regarding the factors "age," gender, and severity were reorganized in one column. In addition, to build the discrete BN model, we used the described discrete variables. Our aim is to qualitatively and quantitatively analyze the main factors in a patient's situation in order to autonomously make the adequate decision, which directly influences the number of hospitalized patients without the expert intervention.

Table 2 Discretized variables


Fig. 5 Instances of rules


### 4.2 Used ruleset

In this approach, the basic element for decision-making is the utilization of the ruleset. This later was created by mining the used dataset in order to discover the utile rules. Relying on [50], we assigned the adequate decision for each patient (instance) in the dataset. Then, we used the FP-Growth method due to its efficiency and scalability for mining frequent patterns. The strategy of this method is to start with the compression of the input dataset by creating the frequent pattern tree (FP-Tree) which represents the frequent items. Then, the compressed dataset is divided into conditional dataset, and each one is associated with the frequent pattern. Thereafter, the final step is to mine each dataset separately. The core in this algorithm is the FP-Tree's construction [45]. The use of FP-Tree allows the FP-growth algorithm to extract the frequent item set directly, and then the rules can be extracted with specific confidence and support.

This analysis enables the discovery of the association between symptoms, age, case's severity or disease class, and the attributed decisions. Basing on the analyzed factors in the previous section, which are the clinical features, age, and disease class, the used association-rules mining algorithm generates easily understood description of the decisional situation (as shown in Fig. 5). In fact, proposing the proper decision has an important role in the progress of the patient's case. In this regard, the attributed decisions for different cases can be the following: admitted in hospital for treatment, isolation at home, and hospitalization and these decisions can be improved by incorporating an expert in the decision-making process. Then, the obtained frequent item sets having the minimum support ( 0.95 ) are used to generate high confidence rules (confidence $\geq 0.8$ ). In Fig. 5, we presented a set of rules, which include at least 10 items in order to minimize the matching rate of the newly given object and the saved objects.

To sum up the used data, we have proposed 13 discrete variables ( 11 symptoms, severity otherwise known as

![img-4.jpeg](img-4.jpeg)

Fig. 6 Autonomous Decision-Making (ADM) process: first module severity class, and age). The factor of the age and the provided symptoms are employed to identify the case's severity. In the present study, we intend to analyze the provided symptoms by suggesting a graphical probabilistic representation for qualifying and then quantifying the dependency relations between variables and severity class. Thus, we suggest to use our BN model to predict the severity classes for the new patients (new objects or new instances) and then to specify the appropriate decision in an autonomous way. The provided COVID-19 dataset was divided into 26,574 (20\% of the dataset) samples to be used in the test and 79,724 ( $80 \%$ of the dataset) samples to be used for training the BN model. The next section presents the construction of the discrete Bayesian model based on the suggested approach while utilizing the analyzed dataset.
![img-5.jpeg](img-5.jpeg)

Fig. 7 Probability distributions within severity class 3 (severe)

### 4.3 Application of module 1 for fighting against COVID-19

Figure 6 illustrates the building of BN model that represents the first module of our proposal (as depicted in Fig. 2). BN model construction, for the diagnosis of COVID-19 cases, consists of two phases, which are structure learning and parameter learning. Firstly, via the MIGT-SL algorithm (Section 3.1), the network topology that represents the dependency between data is learned as shown in Fig. 7. This graph illustrates the qualitative and the quantitative representation of the relations between the variables denoting the main symptoms, age and COVID-19 severity. As shown in Fig. 7, all of the nodes are linked to the class of the disease in a direct (or indirect) way, which proves the significance of all of the selected symptoms in determining the cases' severity. For the identification of the severity of the cases, from this DAG, we can note that the first level of children could be identified as primary symptoms while the children that are at level number 2 (the child of the child) are recognized as secondary symptoms.

Secondly, to estimate the BN parameter, we utilized the EM method. This phase permits the definition of the joint probability distribution for each node. As illustrated in Fig. 6, the generated BN model qualitatively illustrates the dependency between variables and quantifies these associations. Using the generated graph, we set certain values of these variables to analyze the impacts of the specified symptoms on the severity prediction: (1) light classes, (2) moderate, and (3) severe. For instance, in Fig. 6, we illustrate the conditional probability distribution for the class severe (checked box with probability = 100%). Especially, in this case, we analyze the dependencies between the used variables and the severity class 3.

The quantification of these dependencies allows to explain the properties for becoming in serious case. Firstly, we compared the probabilities of each variable (node) when changing the parent nodes for highlighting the class 3 characteristics. For instance, we note that selecting dry-cough (100%), nasal-congestion (100%), and difficulty-in-breathing

Table 3 Frequent factors with its occurrence


![img-6.jpeg](img-6.jpeg)

Fig. 8 Autonomous decision-making (ADM) process: second module (100\%) nodes affects directly the none-symptom node (probability becomes 100\%). Accordingly, we notice that, for severe cases, these three variables represent the main factors. For the selected class, the probability distributions show that the majority of patients have symptoms (None_Symptom 83.14\%) which are dry-cough (56.37\%), nasal-congestion (54.54\%), tiredness (50.24\%), runny-nose (54.54\%), and breathing problems (44.27\%). It is noteworthy that fever does not represent the main symptom for severity detection ( $31.25 \%$ ), which is conflicted with the recognized rules. Taking into consideration the age factor, we note that the patients equally appertain to all of the intervals of ages ( $\pm 3 \%$ ). Furthermore, for class 3, all of the genders (male, female, or transgender) are equally affected ( $33 \%$ ).

After the construction of the BN model using COVID19 dataset, the severity class can be predicted based on the method of variable elimination. Accordingly, this severity class is attributed to the new object. As shown in Fig. 2, in the next step, the ruleset, the variables, and the assigned class for the newly introduced patient represent the key factors for decision-making as depicted in the following section.

### 4.4 Application of module 2 for fighting against COVID-19

As shown in the overview of the proposed process (Fig. 2), the two modules are interrelated via the predicted severity class. The second module, as illustrated in Fig. 8, aims to determine the appropriate decision based on the predicted class. For this reason, all the rules include the case's severity value in order to determine the corresponding decision for the new patient. Each rule represents an object with n features ( n is equal to or greater than 3 ) and one proper decision. The generated ruleset involves more than 752 rules that can be formulated as follows:

![img-7.jpeg](img-7.jpeg)

Fig. 9 Decision selection procedure
$\mathrm{IFF} 1=$ value $1, \mathrm{~F} 2=$ value $2 \ldots \mathrm{~F} 10=$ value $10, \ldots$ then $D=$ decision value
where each rule represents an object, F designates the feature, and D denotes the assigned decision for each object. By analyzing the used rules, we illustrate the occurrence of the most frequent factor(s) for decision-making in Table 3.

To explain the variable-based approach for decisionmaking, we propose the following scenario:

Given the object with:
$\mathrm{F} 1=$ age, $\mathrm{F} 2=$ sore throat, $\mathrm{F} 3=$ difficulty in breathing,

$$
\mathrm{F} 4=\text { fever, } \mathrm{F} 5=\text { severity class }=3
$$

We perform the following steps in order to determine the proper decision (as shown in Fig. 9):

1- The rules (objects) (having disease class $=3$ ) are arranged by the confidence value as illustrated by the rules framed in blue.
2- Calculating the distance between the new object and the ordered objects.
3- The decision of the mostly matched object that has the minimum distance and maximum confidence is assigned for the input object. As shown in Fig. 9, the calculated distance between the object mentioned in red color and the introduced object represents the lowest distance.
4- Assigning the decision "hospitalization and treatments" to the new object.

The proposed process for autonomous decision-making was applied in the medical field, especially for COVID-19
cases. In order to evaluate the efficiency of the Decision Support System (DSS) based on the autonomous decisionmaking process, we propose an evaluation of the system's utility in terms of classification results and decision quality.

## 5 Evaluation and discussion

To construct the proposed ADM process, we combine two main methods for BN building and decision-making method based on variable approach. To build the discrete BN, we proposed new structure learning method named MIGT-SL algorithm, and we used BN parameter learning algorithm named EM algorithm for quantifying the extracted dependencies. In this section, we aim to evaluate the experimental results obtained using the described dataset. Firstly, we will begin by evaluating the efficiency of the proposed methods of BN construction. Correspondingly, we will evaluate the method of BN structure learning (MIGT-SL algorithm), and then we will move to analyzing the accuracy of the proposed BN model using the specific data (COVID-19). Secondly, we will evaluate the accuracy of the proposed autonomous decision-making methodology in making the proper decision.

Table 4 Experimental results of MIGT-SL algorithm for ASIA, ALARM, and CANCER networks


### 5.1 Evaluation of module 1

The construction of the BN model consists of two phases as described in Section 3.1. To learn the BN model, we introduced the MIGT-SL algorithm that allows the building of the network's topology, which represents the dependency between the variables in the dataset. This first step of BN model construction represents the basic element for probability distribution, and then for predicting the new class. Accordingly, the correct structure describes properly the dependencies between variables. Then, the extracted dependencies will be quantified using EM algorithm. At this step, we note the importance of the structure learning in the construction of the BN model that will be applied for severity classification. For this reason, we begin by evaluating the proposed algorithm in the following section before assessing the learned BN model.

### 5.1.1 Evaluation of the method of BN structure learning

One of the most commonly used methods for the evaluation of the efficiency of the BN structure learning algorithm is the method based on structures difference. This latter represents the differences between the original topology of the network and the learnt one. Thus, Structures Difference (SD) is the sum of the number of Added

Edges (AEs), Deleted Edges (DEs), and Reversed Edges (REs) in the learned structure. In addition, the number of Correct Edges (CEs) indicates the number of edges learned correctly using the proposed method. The wellused method of assessment of structure learning algorithms is based on the benchmarks (reference networks) such as CANCER, ASIA, and ALARM. These networks have a unique structure for each number of samples such as $250,500,1000$, and 2000. Table 3 illustrates the experimental results produced by our MIGT-SL algorithm for ASIA, ALARM, and CANCER networks for $1000,2000,3000,5000$, and 10,000 samples or cases. The ALARM network, as a reference network, includes 37 nodes and 46 edges. The third reference network named CANCER consists of 5 nodes and 4 edges. In addition, we exhibit the BIC score for each dataset in order to compare them with the original values of BIC score, which is calculated using the following equation.
$B I C(B \mid D)=\sum_{i=1}^{n} \sum_{j=1}^{q_{i}} \sum_{k=1}^{r_{i}} N_{i j k} \log _{2}\left(\frac{N_{i j k}}{N_{i j}}\right)-\frac{\log _{2} N}{2} \sum_{i=1}^{n} q_{i}\left(r_{i}-1\right)$
where:

- $r_{i}$ denotes the numbers of the states of $X_{i}$.

Table 5 Structures comparisons among five algorithms on ASIA network


- $q_{i}$ represents the numbers of the configurations of $X_{i}$ all over the parents of $X_{i}$.
- $N_{i j k}$ is the number of cases (samples or instances) in the used dataset with the variable $X_{i}$ being set in the configuration number k and its parent being set in the configuration $j$.

Unlike the method of structures difference, the scores calculated using the score functions (such as K2, AIC, and BIC) for the benchmark datasets differ from one work to another because their instances are generated randomly. For this reason, in Table 4, the reported BIC scores for the original networks, termed Orig BIC score, and the BIC score of the learned network, termed BIC score, are used to prove the effectiveness of the proposed algorithm.

To test the efficiency of our MIGT-SL algorithm, it was executed for the three networks on different samples (1000, 2000, 3000, 5000, and 10,000 sizes). Table 2 illustrates the structures difference between the obtained skeleton and the original one based on the factors AE, DE, AE, CE, and SD. As shown in Table 4, the obtained results for ASIA network are 7 correct edges, 0 deleted and added edges, and 1 reversed edge for 1000, 2000, and 3000 cases.

For ASIA-5000 and ASIA-10000, we note that an edge is added. Accordingly, the difference between the original structure and the learned network topology is 2 edges. In this regard, we remark the efficiency of our algorithm for learning the ASIA network. For all the sample sizes for CANCER network, the MIGT-SL algorithm is unable to learn the correct edges: which are 4 edges with 0 errors (original structure). Our MIGT-SL algorithm is unable to learn 34 edges and 16 erroneously detected edges ( 4 deleted edges, 1 reversed edge, and 11 added edges) correctly for the ALARM network for 1000, 2000, and 3000 samples. For ALARM-5000 and ALARM-10000, the proposed algorithm generates 1 reversed edge, 4 deleted edges, and 12 added edges. Accordingly, 17 edges are erroneously involved in the learnt structure. Nevertheless, as shown in Table 4, the calculated BIC scores prove the efficiency of our algorithm for learning ASIA and CANCER networks. The first analysis of the obtained BIC scores for ASIA network proves to be the same as the calculated scores of the original structure for every dataset. However, as illustrated using the first method, the proposed algorithm generates a reversed edge (between nodes number 3 and 1). Therefore, we combined the two methods in order to evaluate the performance of our

Table 6 Structures comparisons among five algorithms on ALARM network


Table 7 Comparison of the BIC scores difference


![img-8.jpeg](img-8.jpeg)

Fig. 10 Multiclass ROC curve

algorithm for structure learning. For ALARM network, we obtained a remarkable difference between the learnt structure and the original topology of each network due to the significant number of variables in the datasets. Accordingly, in the rest of this section, we will present a comparison of the obtained results with the results produced by similar algorithms.

Firstly, we employ two widely used methods that are based on the structure differences method described above and the BIC score function. In Table 5 and Table 6, we illustrate the comparison between the results generated by our MIGT-SL algorithm and the algorithms introduced by Ko and Kim [52], Tabar et al. [27], Ai [28], and Wang and Liu [29], using the benchmark datasets (ASIA and ALARM network with 1000, 2000, 3000, 5000, and 10,000 sample sizes). To highlight the significant results, we use bold to represent the best value and a star to mark the second-best value.

In Table 5 and Table 6, we present the structures difference attained by the five algorithms for ASIA and ALARM networks (datasets are randomly generated for 1000, 2000, 3000, 5000, and 10,000 samples). In terms of structures difference, the first observation is that for ASIA network, the difference between our MIGT-SL algorithm and the algorithms proposed by Ko and Kim [52], Tabar et al. [27], and Ai [28] is maximal. In addition, Table 5 illustrates a minimal difference between our algorithm and NDPSO-BN algorithm for ASIA-1000 and ASIA-3000 (only one erroneously learned edge). Finally, for ALARM network, we can note that our algorithm outperforms the algorithm of Ai [28]. Furthermore, the difference between the proposed MIGT-SL algorithm and the results produced by the rest of the methods is, in general, maximal. Through the experimental results, we can observe that our algorithm used to learn the BN structure performed well for smaller networks.

The following table (Table 7) presents the BIC scores obtained by executing each algorithm on 3 networks for 1000, 2000, 3000, 5000, and 10,000 randomly generated samples. Due to this characteristic of randomness, we adopt the difference between the BIC score of the original network topology and the learned structure as the criterion for the comparison. In Table 7, we exhibit the difference of BIC scores produced by 5 different learning algorithms (the Greedy-Hill-Climbing algorithm (HC), K2 algorithm, HCbo + C algorithm [29], improved K2 algorithm [53], and our MIGT-SL algorithm) on ASIA, CANCER, and ALARM benchmark networks.

The results displayed in Table 7 illustrate the importance of our proposal, especially for learning ASIA and CANCER networks. A quick analysis of the results (values in bold) proves the superiority of our algorithm compared to the other four algorithms. Additionally, we note that the difference between the results produced by the MIGT-SL algorithm and the other used methods for ALARM network is maximal. In this section, we demonstrate the efficacy of MIGT-SL algorithm that is being employed at the structure learning phase, which is considered as fundamental for BN model construction. In the next section, we will use the proposed BN model to analyze the effect of the COVID-19 symptoms on the disease class (mild, moderate, and severe).

### 5.1.2 Evaluation of the built Bayesian model

The proposed Autonomous Decision-Making process integrates the improved Bayesian network construction method and the association rules mining method. To build this discrete model, we propose a new algorithm for structure learning called MIGT-SL algorithm. It is a data-oriented approach used for resolving the problem of BN structure learning, which is considered as an NP-hard problem. In addition, we introduce the new variable-driven approach

![img-9.jpeg](img-9.jpeg)

Fig. 11 BN model evaluation

that is based on computing the distance between objects to make the proper decision. The evaluation of this method's efficiency demonstrates its advantages compared to the other introduced algorithms. Then, the used COVID-19 dataset (106,298 samples), upon which the proposed BN model is constructed, was divided into 79,724 instances for training ( $80 \%$ of the dataset) and 26,574 samples for testing ( $20 \%$ of the dataset).

To show the performance of our improved BN model, we employed the Receiver Operating Characteristic (ROC) curve (shown in Fig. 10). This curve is well-used for binary classification and in our case, we represent the ROC curve of each class versus the rest such as the ROC curve colored in orange that represents the performance of predicting class mild (class 1) versus the other two classes.

In addition, to assess the performance of the proposed BN model, we utilized the following statistical metrics in our paper:

- Accuracy: the researchers in [51] and [52] affirmed that the well-known evaluation measure is Accuracy. This metric evaluates the effectiveness of the classification model based on the correctly predicted instances:

$$
\begin{gathered}
\text { Accuracy }=(\mathrm{TP}(\text { class } 1)+\mathrm{TP}(\text { class } 2)+\mathrm{TP}(\text { class } 3) / \text { total number } \\
\text { Accuracy }(\text { standard BN model })=(7800+6950+6000) / 26574=78.08 \% \\
\text { Accuracy }(\text { our BN model })=(8577+9250+7357) / 26574=94,7693 \%
\end{gathered}
$$

- Precision (P): is the fraction of positive predictions that are correct. For multiclassification, we calcu- lated the averaged of precision for class1, class2, and class3:

$$
\begin{aligned}
& \text { Precision }(\text { standard } B N \text { model })=(\text { Precision }(\text { class } 1)+\text { Precision }(\text { class } 2)+\text { Precision }(\text { class } 3)) / 3 \\
& =(0.88+0.71+0.76) / 3=78.33 \% \\
& \text { Precision }(\text { our } B N \text { model })=(\text { Precision }(\text { class } 1)+\text { Precision }(\text { class } 2)+\text { Precision }(\text { class } 3)) / 3 \\
& =(0.94+0.95+0.95) / 3=94.66 \%
\end{aligned}
$$

- Recall (R): is the fraction of all positive (default) instances the classifier correctly identifies as positive. It is also known as the true positive rate. In a similar method, for multiclassification, we employed the average of the recall for class1, class2, and class3:

Recall (standard $B N$ model) $=($ Precision(class 1$)+$ Precision(class 2$)+$ Precision(class 3$))/ 3$

$$
=(0.83+0.79+0.71) / 3=77.66 \%
$$

Recall (our $B N$ model) $=($ Precision(class 1$)+$ Precision(class 2$)+$ Precision(class 3$))/ 3$

$$
=(0.94+0.95+0.95) / 3=94.66 \%
$$

Table 8 Confusion matrix


Table 9 Comparison with seven similar works


- $F_{1}$ score: is calculated using formula 11 for binary classification. In addition, for multiclassification, we calculated the average of the F1 score for class1, class2, and class3:
$F_{1}=2 . \mathrm{R} . \mathrm{P} / \mathrm{R}+\mathrm{P}$
$F 1($ standard $B N$ model $)=(0.86+0.74+0.74) / 3-78 \%$
$F 1($ our $B N$ model $)=(0.94+0.96+0.96) / 3=94.33 \%$

As indicated in several studies such as $[2,11,12,13$, 14, 54], and [55], Machine Learning may aid physicians by proposing alternative methods mainly at the stage of the admission in the hospitals because they cannot cope with the large number of patients. In our study, for supporting the decision-maker in the fight against COVID-19, we proposed a new BN model to predict the correct severity class. In Fig. 11, we illustrated the obtained values of the defined metrics utilized for the performance evaluation of the BN model. As shown in Fig. 11, the reported results demonstrate the superiority of our BN model compared to the standard BN model.

For all these reasons, we can affirm that the gained results valorize the proposed method of BN model construction. This method starts by learning the structure using the improved MIGT-SL algorithm and then learning its parameter based on the EM algorithm. The predicted class represents the main factor for selecting the group of rules that will be explored for calculating the distance between objects. As described in Section 4.4, this step allows the selection of the proper decision for the new object. In the following section, we will assess the effectiveness of the decision-making process based on the quality of the attributed decision.

### 5.2 Evaluation of module 2

As described above, the decision-making phase is strongly dependent on the predicted class of disease and on the quality of the generated rules. To make the adequate decision for the new object or patient, it is necessary to examine all the produced rules having the same severity of case and assign the decision, which corresponds to the object with minimum distance and maximum confidence in the list of objects. Finally, in order to evaluate the efficiency of the decision-making step based on association rules method, we calculate its precision in assigning the adequate decision. Three different decisions are attributed according to [50], which are hospitalization, hospitalization and treatment, and self-isolation at home. To test the method based on variable approach, we randomly selected 1000 patients from the dataset that properly correspond to the defined conditions in [44]. Then we employed the variable approach for nominating the nearest objects to the selected objects by calculating the minimum distance. In the following table, we presented the obtained results.

Table 8 illustrates the evaluation of 1000 decisions, where the correct decision designates the exact decision (cases marked in green); an adequate (or proper) decision means that the attributed decision is in the same category of the actual decision (cases marked in orange), where the incorrect one represents erroneous decision. As shown, “hospitalization” and “hospitalization and treatments” were considered as different decisions because of the importance of the treatments in various cases. In addition, this precision in attributing the proper decision allows physician to optimize effort, cognitive load, time, and medicines. Accordingly, specifying these two decisions is necessary for further supporting the physicians. As shown in Table 8, the accuracy of attributing decision is respectively 97.80% for acceptable decisions (correct and adequate), 38.20% for correct decisions, and 2.20% for the erroneously selected decisions. For the purpose of evaluating of our proposal, we will compare it with other similar works in the following section.

### Discussion

In this paper, we propose an integrated model based on BN and variable approach for making the appropriate decision autonomously. Several works on the severity of COVID classification based on AI have been suggested and most of them used medical imaging like the works cited in [58, 59], and [60]. On the other hand, in [11, 12, 13, 14, 61], and [62], the analysis of COVID severity is oriented on the basis of clinical factors. Unfortunately, only few works provide a description of the efficiency of the used models. For instance, the Bayesian model in [61] (closely similar to our learning model) is used to qualitatively and quantitatively describe the relations between clinical symptoms and COVID severity. However, the authors in [61] focused on specifying the significance of the symptoms for each class of severity. In Table 9, we illustrate the performance of the similar works compared with our model based on the accuracy of the model, which represents the well-used metric as indicated in [55] and [56].

In [61], the authors proposed to compare 6 ML models to detect the COVID-19 severity using different features. The comparison with these methods using the accuracy metric demonstrates that the SVM classifiers and the proposed BN model outperform the other five classifiers. For this reason, we applied the SVM classifier using LIBSVM in order to classify the COVID-19 severity (mild, moderate, or severe). As illustrated in bold, the introduced BN model is considered as the best model for severity detection (accuracy value is 0.9477). From this table, it can be concluded that the performance of our BN model compared to the SVM, in terms of accuracy, is not much higher (difference of about 0.01) due to the quality of the data used. As explained in Section 4.1, the initial dataset is analyzed, prepared, filtered, and balanced. This step has a significant impact on the performance of the models. In addition, we have twelve features, which are considered fewer in number, that allow Bayesian and SVM models to perform well. In particular, for the BN model, due to the efficient structure learning algorithm that is sensitive to the number of variables (as illustrated in Tables 5 and 6). The SVM classifier (LIBSVM) is tested using the same dataset; for this reason, it represents the highly similar model. As confirmed by [61], SVMs perform well in classifying COVID-19 cases, and they surpass the four models. Accordingly, for multi-class and binary classifications, we can prove that our model outperforms the other models.

According to [59], the number of patients is continuously growing and only a few specialists are available. For this reason, evaluating the utility and usability of a DSS based on the proposed autonomous decision-making process represents a difficult task. Nevertheless, its efficiency for attributing the adequate decision can be further ameliorated inspired by [63, 64, 65, 66], and [67] by integrating the physician in the decision-making process via the visualization.

## Conclusion and future works

Regarding the unexpected world-altering impacts of the coronavirus, in this paper, we used the machine learning methods to analyze the main factors for predicting the gravity of the disease and to propose the proper decision. For the analysis of the principal factors of the COVID severity, we proposed a new Bayesian network model that is based on improving the structure learning algorithm. Then, by using the variable approach, our proposal autonomously made the adequate decision for the cases infected with the virus. To do that, firstly, we introduced a new algorithm named MIGT-SL algorithm based on mutual information and graph theory to discover the hidden relationships between variables. Then, based on the rules analysis, nearest object selection and distance calculation, we assigned the proper decision for the new object. To achieve this, the used method calculates the distance between features in order to determine the nearest object. Finally, we presented the experimental results, which seem acceptable as a first proposition that still necessitates the concrete application to be validated. In addition, our BN consists of 13 nodes, and it can be considered as small network (< 20 nodes). Accordingly, the experimental results demonstrate the superiority of our BN model compared to the standard BN model. Our next step is to test the BN model using larger networks (greater number of variables). Moreover, it is not easy to consider all the factors in the disease's progression without the intervention of the

expert. The proposed autonomous decision-making process depends mainly on the accuracy of the classification method. As future work, the employed decisions need to be ameliorated using specified treatments. In addition, we propose to attribute a weight for each variable according to its efficiency in the specified field in order to improve the proposed BN model and the decision-making procedure.
