Article

# RETRACTED: Fault Diagnosis of Traction Transformer Based on Bayesian Network 

Yong Xiao ${ }^{1}$, Weiguo Pan ${ }^{1}$, Xiaomin Guo ${ }^{1}$, Sheng Bi ${ }^{2}$, Ding Feng ${ }^{2, * *}$ and Sheng Lin ${ }^{2}$<br>1 Beijing National Railway Research \& Design Institute of Signal Communication Group Company, Beijing 100070, China; thcs_xiaoyong@163.com (Y.X.); panweiguo@crscd.com.cn (W.P.); guoxiaomin@crscd.com.cn (X.G.)<br>2 School of Electrical Engineering, Southwest Jiaotong University, Chengdu 610031, China; bisheng1008@foxmail.com (S.B.); slin@swjtu.edu.cn (S.L.)<br>* Correspondence: fengding@swjtu.edu.cn

Received: 26 August 2020; Accepted: 17 September 2020; Published: 22 September 2020;
REtracted: 20 February 2025
Abstract: As the core equipment of a traction power supply system, the traction transformer is very important to ensure the safe and reliable operation of the system. At present, the three-ratio method is mainly used to distinguish transformer faults, whereas such a method has some defects, such as insufficient coding and over-general fault classification. At the same time, on-site maintenance personnel make an empirical judgment based on various test data, which is subjective and uncertain to a certain extent. For cases with multiple abnormal data and relatively complex conditions, on-site personnel often need to discuss and even dismantle the transformer to identify the fault, which is time-consuming and costly. In order to improve the effect of fault diagnosis for traction transformer, this paper uses Bayesian network to correlate the cause and effect of various tests and faults. By combining the results of field tests, the fault is diagnosed by the causal probability of the Bayesian network, rather than relying on the exception that occurred in a single experiment to judge its fault. The diagnosis results are more accurate and objective by using the Bayesian network. In this paper, the frequent test anomalies of the traction transformer are taken into account in the network, so that the network can more comprehensively analyze the operation situation of the traction transformer and judge the type of fault. According to field situations, based on the existing set of symptoms of the Bayesian network fault diagnosis, this paper further considers the insulation resistance, dielectric loss tangent value, oil and gas, power frequency voltage, and leakage current. By combining the association rules algorithm and the experience of the field operators, the cause-effect relationship of test data and the conditional probability parameters of the network are obtained. Then, the Bayesian network is constructed and used for traction transformer fault diagnosis. The case study shows that the four types of fault diagnosed using the Bayesian network model proposed in this paper are consistent with the fault types inspected by on-site operators, which shows promising engineering application prospects.

Keywords: Bayesian network; association rules; fault diagnosis; traction transformer; conditional probability

## 1. Introduction

With the continuous development of China's electrified railway, the safety and economic requirements for traction power supply are getting increasingly higher. The traction transformer, as the core equipment of a traction power supply system, is very important to ensure safe and reliable operation of the system. With the accumulation of service time, the traction transformer's failure rate also increases. When fault occurs, some characteristics of the traction transformer are abnormal,

resulting in the transmission of fault information to the on-site operators, who need to timely analyze and judge the occurrence of the fault for maintenance, so as to avoid the expansion of the fault. Considering the rapid development of electrified railway and the impact, imbalance, and mobility of traction load, the short-circuit on the secondary side of the traction transformer becomes more frequent, the voltage fluctuation becomes more drastic, and the uncertain factors also increase. This kind of artificial fault analysis method is more subjective and less reliable. Once the judgment is wrong and the maintenance is not timely and accurate, it will cause serious damage to the traction transformer and entail a long time of power-outage maintenance, which will seriously affect the normal operation of the trains and cause great losses. Therefore, in order to ensure the accuracy of traction transformer fault diagnosis, it is an inevitable trend for the development of its maintenance mode to improve the degree of intelligent diagnosis [1].

At present, in the field of fault diagnosis, Bayesian networks overcome the conceptual and computational difficulties of rule-based systems through graphical methods and knowledge of computational probabilities, and make the relationship between data more clearly expressed. By reflecting the probabilistic relationship model among the entire data, an accurate model can still be established when a certain set of data are missing, which has the advantage of overcoming uncertainty. The authors of [2] used the Monte Carlo method to generate simulation data for parameter learning by considering different weather conditions, and constructed a Bayesian network for fault diagnosis of a traction power supply system. The authors of [3] proposed a Bayesian network fault diagnosis and reliability analysis method for complex systems, and analyzed the subsystems of high-speed trains and high-power solid-state lasers. It incorporated the uncertainty quantification and dynamic importance measurement into the Bayesian network to improve the accuracy of the results. The authors of [4] evaluated the faulty section of the transmission system, and built a Bayesian network diagnosis model for the transmission lines, transformers, and busbars in the power outage area. The proposed method has clear semantics, strong fault tolerance, and certain flexibility. The authors of [5] evaluated the reliability of subway traction substations, used dynamic Bayesian networks to analyze the time-dependent reliability of subway traction substations, and accurately calculated the time variation curve of the system failure probability.

The currently applied fault diagnosis method of a traction transformer is mainly based on the chromatographic data to diagnose the fault type by the three-ratio method, and then operators judge the occurrence of the fault according to the fault type and experience. The three-ratio method has shortcomings, such as inadequate coding and rough fault classification [6], as well as certain subjectivity and uncertainty in the manual experience-based judgment. Thus, it often fails to achieve ideal accuracy in on-site fault diagnosis analysis. Therefore, it is necessary to adopt a more accurate diagnosis method to diagnose the fault types of traction transformers, so as to improve the efficiency of on-site maintenance and operation. In recent years, along with the accumulation of transformer failure data and the rise of the machine learning techniques, researchers have employed a variety of machine learning algorithms, combined with the historical data of the transformer, to deal with the fault diagnosis of transformers, such as: support vector machine (SVM) [7-10] genetic algorithm, fuzzy theory [11-14], artificial neural network and evidence reasoning method [15,16], and deep learning algorithm [17-19], etc. It, to a certain extent, improved the accuracy of the diagnosis and achieved good results. Whereas, most of these methods only rely on the chromatographic data of the transformer for diagnosis. However, when the transformer fails, it does not only cause the abnormality of a single state quantity. These algorithms have some problems, such as insufficient analysis of the internal relationship between multiple state quantities in the case of transformer failure.

Based on the above deficiencies, some researchers evaluated and diagnosed the operation state of the transformer by combining multiple state quantities. In the literature [20], the association rule algorithm is used to combine the state quantities of multiple field tests to analyze the correlation degree between the fault and the state quantities. However, as a probabilistic statistical method, the association rule algorithm cannot fully take into account the uncertainties of the transformer during

operation. The authors of [21] combined the fault mode with abnormal symptoms by the Bayesian network method, and judged faults by analyzing abnormal symptoms. The authors of [22] adopted a three-layer Bayesian method and considered the influences of adverse operation conditions on the fault type. It constructed a three-layer Bayesian network based on [21] by considering three types of adverse condition: lightning struck, overload, and short-circuit. By considering the inducing factors of transformer fault, it improved existing networks. Combining adverse conditions with internal anomalies made the diagnosis results more in line with the actual situation. The authors of [23,24,25] combined the rough set method with a Bayesian network, and adopted the complex structure of a rough set reduction Bayesian network to reduce the difficulty of fault feature acquisition. In addition, the Bayesian network has been combined with other methods for co-diagnosis, such as the immune algorithm [26] and normal cloud [27].

The research on fault diagnosis of the power transformer has achieved good results, but for the traction transformer, the existing set of abnormal symptoms of Bayesian networks cannot completely include all the symptoms in field testing. As a result, some of the frequently occurring abnormal symptoms cannot be input to the Bayesian networks and cause diagnosis deviation.

In order to solve the above problems, this paper proposes a fault diagnosis method for the traction transformer based on a Bayesian network. This diagnosis method takes into account the operation condition of the traction transformer and its frequent abnormal symptoms, and uses the association rule method to statistically analyze the correlation between the operation condition, abnormal symptoms, and fault types, so as to establish a causal network among them. The transformer fault is timely diagnosed by combining field operation data with a Bayesian network for causal analysis, which can help guide actual operation and maintenance work. The main contributions are as follows:

1. Considering the imbalance, impact, and nonlinear characteristics of traction load [28], this paper established the operation condition layer and sign layer of a Bayesian diagnostic network. Through the statistical analysis of historical data, the prior probability of each working condition is calculated, and the adverse operation conditions are correlated with fault types by analyzing the failure mechanism. In addition, abnormal symptoms, which occurred frequently in the traction transformer, are added to comprehensively analyze the operation state of the traction transformer from the perspective of both working conditions and symptoms.
2. The association rule method is proposed to analyze the correlation degree between the failure of the traction transformer and the abnormal symptoms. By combining the field data, the support degree between abnormal symptoms and fault types is calculated to determine whether there is a corresponding relationship between the fault types and abnormal symptoms. Then, the confidence level is calculated to determine the causal condition probability. The parameters of the Bayesian network are set according to the calculated conditional probability to make the parameters more objective and the diagnosed results more accurate.

The rest of this paper is organized as follows: Section 1 introduces the theoretical analysis of traction transformer fault diagnosis combined with association rule theory and Bayesian theory. Section 2 introduces the process of establishing the Bayesian network fault diagnosis model for the traction transformer. Section 3, based on the field operation and maintenance data, presents a case study of the Bayesian diagnosis model. The fourth section is the conclusion.

# 2. Association Rules and Bayesian Network Theory 

The proposed method combines the association rules method with the Bayesian network model. The association rules method is applied to analyze the correlation among the transformer's operation condition, fault type, and test item; the conditional probability among them is also calculated. According to the analysis results, the Bayesian network for traction transformer fault diagnosis is established, and it is then used to achieve fault diagnosis.

# 2.1. Association Rules 

When the traction transformer fails, there are many abnormal symptoms. These abnormal symptoms and fault types do not exhibit a "one-to-one" correspondence, in other words, they intersect with each other, and one abnormal sign can also reflect multiple fault types. The association rule method can accurately represent the corresponding relationship and correlation degree between each fault type and the abnormal symptoms in the traction transformer. According to the mechanism of traction transformer failure and the actual situation of on-site failure, a certain fault type and abnormal symptoms that may be related to the fault type are selected as the item set of association rules, which is denoted as $D_{d i}$, and the number of subsets in the item set is denoted as $\left|D_{d i}\right|$. Let $d_{i}$ be the fault term of the traction transformer, and $m_{j}$ be the abnormal symptom term of the traction transformer. If $d_{i}, m_{j}$ meets $d_{i} \subseteq D_{d i}, m_{j} \subseteq D_{d i}$ and $d_{i} \cap m_{j}=\varnothing$, then the support degree between $d_{i}$ and $m_{j}$ is calculated:

$$
\operatorname{support}\left(d_{i} \Rightarrow m_{j}\right)=\frac{f\left(d_{i} \cup m_{j}\right)}{\left|D_{d i}\right|} \times 100 \%
$$

When the degree of support is greater than the set minimum support, $\left(d_{i}, m_{j}\right)$ is set as the frequent item set, then it is considered that there is a correlation between $d_{i}$ and $m_{j}$. For a set that does not satisfy the minimum support, it is considered that there is no correlation or the correlation is small, and the correlation is discarded.

The degree of association between the fault type and abnormal symptom for the frequent itemset is calculatted, which is called confidence. The confidence of association rule $A \Rightarrow B$ is the proportion of the occurrence of abnormal symptoms $m_{j}$ when the fault type $d_{i}$ occurs, namely the conditional probability $P\left(m_{j} \mid d_{i}\right)$ :

$$
\operatorname{confiden}\left(d_{i} \Rightarrow m_{j}\right)=P\left(m_{j} \mid d_{i}\right)=\frac{f\left(m_{j} \cup d_{i}\right)}{f\left(d_{i}\right)} \times 100 \%
$$

Based on the association rule algorithm, the correlation between the fault type of the traction transformer and abnormal symptoms, as well as the conditional probability, was statistically calculated, and the Bayesian network was constructed as the parameter value of the causal relationship between the correlated events in the Bayesian network.

### 2.2. Bayesian Networks

Based on the analysis of the operating conditions, fault types, and abnormal symptoms of the traction transformer, the Bayesian network was constructed based on the association relationship statistically calculated by the association rule method. Bayesian network constructs directed an acyclic graph through the causal relationship among events and deduces the probability model of the occurrence of other nodes according to the set prior probability and conditional probability and the known node.

Figure 1 depicts a simple Bayesian network structure of traction transformer fault diagnosis, where the condition, fault, and symptoms correspond to each node in the network, respectively. Each node indicates an independent random variable; the directed line of two nodes expresses the causal relationship between the node and conditional probability; the starting point of the directed line is the parent node and the end point is the child point. According to the fault situation of the traction transformer, when the traction transformer is in an adverse working condition, it is easy to cause its fault. Therefore, its operating condition is taken as the cause layer of the fault type. When the traction transformer fails, the abnormal symptoms will appear accordingly, so the fault type is taken as the cause layer of the abnormal symptoms.

![img-0.jpeg](img-0.jpeg)

Figure 1. Structure of the Bayesian network.
The Bayesian network method is used to describe the correlation and probability distribution between the operation condition, fault type, and abnormal symptoms of the traction transformer. Based on the known node information, probabilistic reasoning is carried out to calculate the failure probability.

# 2.3. Probabilistic Inference of Bayesian Networks 

The fault diagnosis of the traction transformer by the Bayesian network is based on the operation condition or abnormal symptoms of the transformer during operation. The network takes the abnormal symptoms of the transformer as the child node of the fault mode, and the fault mode as the child node of the adverse working condition. When the traction transformer fails, the data is $D=\left(X_{i}, X_{j} \ldots, X_{k}\right.$, $C$ ], where $X_{i}-X_{k}$ is the occurrence of adverse working conditions or abnormal symptoms obtained from the field test during the operation of the transformer, and $C$ is the fault set of the transformer. The joint probability distribution of abnormal symptoms characterized by the Bayesian network can be determined by the following Equation (3):

$$
P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i} P\left(X_{i} \mid P a_{i}\right)
$$

For a certain type of fault $C_{r}$ in fault set $C$, the probability of the occurrence of fault $C_{r}$ under the known abnormal conditions is:

$$
P\left(C_{r} \mid X_{i}, X_{j}, \cdots, X_{k}\right)=\frac{P\left(X_{i}, X_{j}, \cdots, X_{k} \mid C_{r}\right) \times P\left(C_{r}\right)}{P\left(X_{i}, X_{j}, \cdots, X_{k}\right)}
$$

where $P\left(X_{i}, X_{j}, \ldots, X_{k}\right)$ is the joint probability of abnormal symptoms, which can be obtained from Equation (3); $P\left(C_{r}\right)$ is the prior probability of occurrence of $C_{r}$; and $P\left(X_{i}, X_{j} \ldots, X_{k} \mid C_{r}\right)$ is the probability value of occurrence of abnormal symptoms related to failure $C_{r}$.

For child nodes with multiple parent nodes, considering the influence of the interaction between parent nodes on their child nodes, more parameters will be required, and more data cannot be obtained on site to calculate more parameters. Based on the above situation, the leaky noisy-or node can significantly reduce parameters. Noisy-or nodes assume that the parent nodes of each group are independent of the conditions, and the influence on the child nodes does not consider the interaction between the parent nodes, so only the conditional probability between the parent nodes and the child nodes with wiring is considered in the parameter calculation. Therefore, according to Equation (4), the following Equation (5) can be obtained:

$$
P\left(C_{r} \mid X_{i}, X_{j}, \cdots, X_{k}\right)=\frac{P\left(C_{r}\right) \times \prod_{i}^{k} P\left(X_{i} \mid C_{r}\right)}{P\left(X_{i}, X_{j}, \cdots, X_{k}\right)}
$$

On the basis of noisy-or nodes, leaky noisy-or nodes added the default node $X_{L}$ to represent the non-consideration of the interaction between parent nodes, the error in the measurement of data transmission, and the influence of other parent nodes on child nodes [16].

# 2.4. Bayesian Network Association Tree Algorithm 

The union tree is transformed from the directed acyclic graph (DAG) of the Bayesian network. Each node in the federated tree is called a cluster node and consists of a set of variables in a Bayesian network. This group of variables is the set of variables of the most complete connected subgraph converted from the constituted DAG to an undirected graph. The node connecting two adjacent cluster nodes $m_{i}$ and $m_{j}$ is called the separation node $S$. The random variable in $S$ is the intersection of the set of random variables contained in cluster node $m_{i}$ and $m_{j}: S=m_{i} \cap m_{j}$. After the Bayesian network is transformed into a federated tree, the conditional probability table of Bayesian needs to be transformed into the federated tree, which satisfies $P(X)=\frac{\prod m_{i}}{\prod m_{j}}$, where $m_{i}$ is the table of cluster nodes. $S$ is the table that separates the nodes.

When the evidence is added to the federated tree, the global consistency of the federated tree can be achieved through the transmission of messages between nodes in the federated tree. The process of message transmission is the reasoning process of Bayesian networks. According to the probability distribution of the joint tree, the probability distribution of the random variable under the new evidence is calculated.

### 2.5. Establishment of Fault Diagnosis Model of Bayesian Network

High-speed railway traction load has the characteristics of imbalance, impact, and nonlinearity [28]. With the increasing speed of electric locomotives and the increasing number of vehicles, the operation of the traction transformer under bad working conditions becomes an important factor in the fault analysis. For high slope, heavy load, or a dense section of the train, the traction transformer is often in overload operation, which has a serious impact on the operation state of the traction transformer for a long time. In the traction power supply system, the network load fluctuates frequently, and its amplitude is too large, which often leads to the instantaneous short-circuit of the equipment in the system, which has the effect of short-circuit impact on the traction transformer. At the same time, the load of the traction transformer is not symmetrical, resulting in too much negative sequence current, which affects the performance of the equipment and is easily affected by environmental factors in outdoor operation, such as lightning shock and electromagnetic wave interference. To sum up, the traction transformer needs to take into account such undesirable conditions as overload, outlet short-circuit, and intrusion wave when operating. Due to the traction transformer running under adverse conditions as a small probability event, according to the 407 groups of data collected form a railway administration, a total of 36 times of overload conditions, 32 times of short circuit conditions, and 4 times of lightning shock and other electromagnetic waves are identified. According to Equation (6), three kinds of condition probability value are calculated, as shown in Table 1:

$$
P(\text { probability })=\frac{f(\text { number of working })}{f(\text { number of data })}
$$

Table 1. Probability of adverse working conditions.


The traction transformer has the same structure as the power transformer, but its operating conditions and load conditions are different, so the fault types of the traction transformer are the

same as the power transformer. This paper summarizes the fault types and abnormal symptoms of traction transformers according to the state evaluation guidelines for oil-immersed transformers (reactors) [29], transformer structure, and the actual situations. The structure and key components of a typical transformer are shown in Figure 2. The fault types of transformers are shown in Table 2 below.
![img-1.jpeg](img-1.jpeg)

Figure 2. Structure and key components of the typical transformer.
Table 2. Transformer fault types.


When referring to the power transformer, the abnormal symptoms of the traction transformer are also tested in combination with the railway operating conditions, including insulation resistance, dielectric loss tangent value, oil and gas strength, power frequency voltage resistance, and leakage current, as shown in Table 3.

According to "DL/T 596-1996 preventive test regulations for electric power equipment", the association rule algorithm, transformer failure mechanism, and the experience of field maintenance personnel, the abnormal symptoms of each preventive test were correlated with the failure. The association degree is calculated according to the association rule algorithm.

Table 3. Transformer test items.


# 2.5.1. Association Rules of Calculating the Degree of Association 

By collecting the fault data of the traction transformer's historical test, the correlation degree between the fault type and some abnormal symptoms (insulation resistance, dielectric loss tangent value, oil and gas strength, power frequency voltage resistance, and leakage current) was calculated by association rules. Considering the uncertainty of traction transformer operation condition, the collected historical fault data are not balanced. In order to reduce the error, this paper uses the fault mechanism and the experience of on-site maintenance personnel to divide fault types and abnormal symptoms into groups, e.g., insulation aging failure may incur insulation resistance, oil pressure, and leakage current data exceptions. Insulation aging, insulation resistance, oil withstand voltage, and leakage current are divided into a set of events, and the support degree between the fault mode and each abnormal symptom is calculated by Equation (1). According to the failure statistics, the conditional probability between the failure type of the traction transformer and the test item is calculated. The $\mathrm{d}_{5}$ fault type and its associated $\mathrm{m}_{10}, \mathrm{~m}_{11}, \mathrm{~m}_{12}$, and $\mathrm{m}_{14}$ is taken as an example, and its data form is shown in Table 4 (partial data).

Table 4. Failure anomaly statistics.


In Table 1, " 1 " denotes the corresponding fault type or test item is abnormal, and " 0 " means the corresponding fault type or test item is normal. By counting the number of each fault type, the conditional probability is calculated by the association rule method.

It is generally believed that the minimum threshold k of the degree of support is set to $70 \%$ [30]. When the degree of support is greater than or equal to $70 \%$, the association relation is considered to be meaningful, and it is set as the frequent item set. For non-frequent item sets, the association relation between them is not considered. For frequent item sets that meet the threshold of support, their relationship is set to causality, and the following causal relationship table can be obtained, as shown in Table 5.

Table 5. Causal relationship between failure modes and abnormal symptoms.


The support degree of event data is calculated by association rules after grouping the event data based on the experience of field personnel, which not only avoids the subjectivity caused by the experience to directly judge the causal relationship between fault and symptoms but also makes statistics of the support degree based on the data, which reduces the error to a certain extent and ensures the accuracy of the causal relationship.

# 2.5.2. Establishment of the Bayesian Diagnostic Network 

According to the causal relationship between bad working conditions, fault modes, and abnormal symptoms under actual operation conditions, combined with the calculation of frequent item sets and association rules, the causal relationship of fault modes corresponding to abnormal frequency symptoms of the traction transformer is obtained, and the Bayesian network structure is established as shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Bayesian diagnosis network.
Each node in the network represents each operation condition in the traction transformer, corresponding to the number in Table 1, Table 2, Table 3. To reduce network parameters that are difficult to obtain on site, each node uses leaky noisy-or nodes. The directed line between each node represents the causal relationship between two nodes, from cause to effect. In the network, the first layer represents the bad working condition of the traction transformer, the second layer is the fault

type, and the third layer is the abnormal symptom. Based on the conditional probability represented by each directed line segment, the fault condition of the traction transformer is obtained.

# 2.5.3. Acquisition of Conditional Probability of the Bayesian Network 

Because the internal structure of the traction transformer is similar to that of the power transformer, the correlation between the failure modes and the abnormal symptoms is also consistent. Considering that there are few fault data of the traction transformer on site, the correlation relationship and conditional probability in [22] are referred to. The conditional probability value of the affected fault mode under the adverse working condition is set as 0.6 . At the same time, the leaky node was used as a leaky node in the first to second layers of the network that did not contain other conditions affecting the failure (such as uncertain factors in the transformer manufacturing process or an animal influence), and the conditional probability value set by the leaky node is 0.5 . For failure modes not included in layers 2 through 3, the leaky node is set at 0.01 for adverse omen.

According to the frequent item set calculated by association rules, the conditional probability between the fault type and some abnormal symptoms is solved according to Equation (2). The ratio of the occurrence frequency of a fault type and one of the corresponding abnormal symptoms to the frequency of such fault type is its conditional probability. For example, 120 sets of data about discharge fault in oil $\left(\mathrm{d}_{9}\right)$ were collected on site. Through calculation of the support degree of Equation (1), it is concluded that discharge faults in oil types were frequent item sets with oil and gas strength $\left(m_{10}\right)$ and leakage current $\left(m_{2}\right)$. Among 120 groups of the discharge fault in oil, 91 groups of abnormal data of oil and gas intensity, and 86 groups of abnormal data of leakage current occurred. According to Equation (2), the conditional probability can be calculated as: $\mathrm{P}\left(m_{10} \mid \mathrm{d}_{9}\right)=0.758$ and $\mathrm{P}\left(m_{2} \mid \mathrm{d}_{9}\right)=0.717$. By analogy, the remaining conditional probability values were calculated. All conditional probability parameters in the network are shown in Table 6 below.

Table 6. Conditional probability parameters.


Table 6. Cont.


# 2.5.4. Bayesian Network Reasoning 

In this paper, the joint tree algorithm is used to retrieve each node of the Bayesian network. The joint tree reasoning algorithm is widely used because of its efficiency and speed. The maximum posterior hypothesis problem (MAP) is used for inference. By $E=\left\{m_{i}, m_{j}, \cdots, m_{k}\right\}$ as a set of evidence, combining with the corresponding conditional probability in the Bayesian network, the corresponding state combination $H$ with the highest probability is obtained for the evidence event $E, H=\left\{h_{i}, \cdots, h_{j}\right\}$ is called the maximum posteriori hypothesis of evidential events. The mathematical expression of its reasoning is as follows:

$$
h_{i}=\underset{h}{\operatorname{argmax}} P\left(H=h \mid E=\left\{m_{i}, m_{j}, \cdots, m_{k}\right\}\right)
$$

where $h_{i}$ is an event with a high probability derived from evidential events, and $H$ is the set of each sub-event $h_{i}$.

Based on the determination of the Bayesian network structure, the calculation of conditional probability parameters, and the selection of reasoning methods, the fault diagnosis model of the Bayesian network for the traction transformer is then established.

## 3. Example of Traction Transformer Diagnosis

### 3.1. Example Introduction

The traction transformer type is SF7-20000/110GY, rated capacity is 20,000 KVA, rated voltage is 110 KV , no-load loss is 21350 W , load loss is 118639 W , no-load current is $0.319 \%$, and the method of oil natural air forced (ONAF) cooling is adopted. The experiment was carried out in May 2008 with an ambient temperature of $23.2^{\circ} \mathrm{C}$ and a humidity of $68 \%$.

### 3.2. Test Data

The scene of the content of the test report contains in winding dc resistance, insulation resistance (winding insulation resistance absorption ratio and core insulation resistance), oil color data, insulation dielectric loss and cutting oil and gas strength test, winding $\operatorname{tg}(\%)$, and dc leakage current, corresponding to the Bayesian network abnormal symptom of $m_{9}, m_{14}, m_{7}, m_{3}, m_{11}, m_{12}, m_{10}$,

$m_{4}$, and $m_{2}$, to maintain/repair the transformer after partial discharge and near the high-voltage winding insulation down fault, including the numerical test data as shown in Table 7, Table 8, Table 9, Table 10, Table 11, Table 12.

Table 7. DC resistance test of winding (G).


Table 8. Oil chromatographic data.


Table 9. Insulation resistance test $(\mathrm{G} \Omega)$.


Table 10. Strength test of insulating oil and gas.


Table 11. Dielectric loss of winding.


Table 12. DC leakage current.


For transformers with a capacity greater than 1600 kVA , it is required that the unbalance rate of both the line resistance and the phase resistance is $\leq 2 \%$; otherwise, the transformer is considered abnormal. For this transformer, the error values of $0.59 \%$ and $0.67 \%$ are both less than $2 \%$, so the three-phase unbalance coefficient $\left(m_{14}\right)$ corresponding to the dc resistance of the winding of the network is normal.

For the three-ratio method, according to the value of $\mathrm{H}_{2}, \mathrm{CH}_{4}, \mathrm{C}_{2} \mathrm{H}_{6}, \mathrm{C}_{2} \mathrm{H}_{4}$, and $\mathrm{C}_{2} \mathrm{H}_{6}$, the ratios of $\mathrm{C}_{2} \mathrm{H}_{2} / \mathrm{C}_{2} \mathrm{H}_{4}, \mathrm{CH}_{4} / \mathrm{H}_{2}$, and $\mathrm{C}_{2} \mathrm{H}_{4} / \mathrm{C}_{2} \mathrm{H}_{6}$ are calculated. Each ratio is coded according to the value of the ratio. In this case, the ratio of $\mathrm{C}_{2} \mathrm{H}_{2} / \mathrm{C}_{2} \mathrm{H}_{4}$ is $0.18, \mathrm{CH}_{4} / \mathrm{H}_{2}$ is 0.29 , and $\mathrm{C}_{2} \mathrm{H}_{4} / \mathrm{C}_{2} \mathrm{H}_{6}$ ratio is 1.05 .

According to the coding rules of the three-ratio method, $\mathrm{C}_{2} \mathrm{H}_{2} / \mathrm{C}_{2} \mathrm{H}_{4}$ is coded as $1, \mathrm{CH}_{4} / \mathrm{H}_{2}$ is coded as $0, \mathrm{C}_{2} \mathrm{H}_{4} / \mathrm{C}_{2} \mathrm{H}_{6}$ is coded as 1 , and the combined code is coded as 101. According to the three-ratio code table, it is identified as arc discharge. Therefore, the evidence of this group of data shows that discharge failure is diagnosed by the three-ratio method, instead of overheating failure.

For the insulation resistance test of the transformer winding, the field is mainly to judge whether the insulation resistance of the transformer is abnormal by the absorption ratio of the winding. For the transformer of 110 kV and above, the normal range of the absorption ratio is $\geq 1.3$. The transformer's absorption ratio of 1.56 is within the normal range, so the winding absorption ratio and polarization index $\left(m_{3}\right)$ is normal. The core insulation resistance of the normal range for $20 \mathrm{M} \Omega$, or test is $140 \mathrm{M} \Omega$ belongs to the normal range, so the core insulation resistance $\left(m_{11}\right)$ is normal.

For the normal range of the insulation, the oil breakdown voltage of the 110 kV transformer is $\geq 35 \mathrm{kV}$; four breakdown tests were conducted in this test. The breakdown voltage was greater than 35 kV , which was within the normal range, so the strength of insulating oil and gas $\left(m_{10}\right)$ was normal.

For the transformer of $60-220 \mathrm{kV}$, the normal range of the tangent value of the dielectric loss of the winding is $<3 \%$. As for the test result of the transformer, the dielectric loss at the high-voltage side of the winding is $10.92 \%$, which is far beyond the normal range. Therefore, the dielectric loss of the winding $\left(m_{12}\right)$ is abnormal.

For the 1000 kVA transformer, the dc leakage current should be tested. When the test voltage on the low-voltage side of the transformer is 20 kV , the leakage current $\leq 83 \mu \mathrm{~A}$; when the high-voltage side test voltage is 40 kV , the leakage current $\leq 100 \mu \mathrm{~A}$. In this test, the low-voltage side of $5 \mu \mathrm{~A}$ is within the normal range, but the high-voltage side of $150 \mu \mathrm{~A}$ is far beyond the normal range, so the leakage current $\left(m_{2}\right)$ is abnormal.

In conclusion, according to the test results, the leakage current $\left(m_{2}\right)$, insulation resistance absorption ratio $\left(m_{3}\right)$, oil and gas strength $\left(m_{10}\right)$, core insulation resistance $\left(m_{11}\right)$, and the dc resistance of the winding $\left(m_{14}\right)$ are normal. The media loss cut value $\left(m_{12}\right)$ results are abnormal and the three-ratio method presents discharge fault $\left(m_{7}\right)$. To sum up, the inference evidence of the Bayesian network $E=\left\{m_{2}=1, m_{3}=0, m_{7}=1, m_{10}=0, m_{11}=0, m_{12}=1, m_{14}=0\right\}$ is obtained, where 0 represents normal data and 1 represents abnormal data.

# 3.3. Fault diagnosis of the Bayesian Network 

According to the evidence obtained from the test data, $E=\left\{m_{2}=1, m_{3}=0, m_{7}=1, m_{9}=0, m_{10}=0\right.$, $\left.m_{11}=0, m_{12}=1, m_{14}=0\right\}$ was input into the Bayesian network. Based on the correlation between the events in the Bayesian network in Figure 4 and the maximum posteriori hypothesis in Equation (6), fault $\mathrm{d}_{1}-\mathrm{d}_{10}$ was deduced and its conditional probability was calculated.
![img-3.jpeg](img-3.jpeg)

Figure 4. Probability distribution diagram of fault mode.
The diagnostic results obtained are $\mathrm{d}_{2}, \mathrm{~d}_{3}, \mathrm{~d}_{6}$, and $\mathrm{d}_{9}$, which correspond to insulation aging, insulation damage and inter-turn short circuit, winding deformation and inter-turn short circuit,

and discharge in oil, etc. The fault mode with the highest probability value is selected as the first diagnosis result, and other results besides the first diagnosis result are taken as the second diagnosis result, so that on-site maintenance personnel can carry out the troubleshooting of the fault.

# 3.4. Result Analysis 

According to Figure 4, the probability of turn insulation damage and inter-turn short circuit $\left(\mathrm{d}_{6}\right)$ reaches the highest value of 0.5867 . Additionally, the probability of winding deformation $\left(\mathrm{d}_{3}\right)$, insulation aging $\left(\mathrm{d}_{2}\right)$, and discharge in oil $\left(\mathrm{d}_{9}\right)$ are relatively high, being $0.5738,0.5117$, and 0.4728 , respectively. Therefore, the fault diagnosis results in this case are $\mathrm{d}_{2}, \mathrm{~d}_{3}, \mathrm{~d}_{6}$, and $\mathrm{d}_{9}$. For iron core multi-point grounding $\left(\mathrm{d}_{1}\right)$ and tap changer and lead failure $\left(\mathrm{d}_{10}\right)$, the probability of occurrence is 0.0011 and 0.0482 , respectively. Considering the low probability of occurrence, these two types of fault are excluded. Meanwhile, the probability of the rest of the fault types are relatively low compared with $\mathrm{d}_{2}, \mathrm{~d}_{3}, \mathrm{~d}_{6}$, and $\mathrm{d}_{9}$. Thus, the four fault types with a relatively high probability of occurrence are considered as the diagnosis results.

On-site operators diagnosed the transformer faults as partial discharge of the high-voltage side winding and insulation drop by inspection. The fault types diagnosed in this paper are turn insulation damage and interturn short circuit, insulation dampness, winding deformation, and interturn short circuit. Therefore, this paper is basically consistent with the fault diagnosis results of field maintenance.

The four faults are analyzed according to the three faults diagnosed by the network. Partial'discharge and anomaly can be inferred by Bayesian network causality according to the insulation damage and inter-turn short circuit. The abnormal moisture content in transformer oil can be judged by the network relation of insulation moisture. According to the network relationship between the winding deformation and the short circuit between the turns, the abnormal variation of the winding ratio and the abnormal partial discharge can be judged. Other abnormal symptoms diagnosed in the network can be used in the field for further testing and inspection to further verify the fault diagnosis results.

## 4. Conclusions

In this paper, aiming at the frequent abnormal events in traction transformer operation, the association rules method was used to analyze the relationship between abnormal symptoms and fault types, and determine the causal relationship and conditional probability between symptoms and faults. Combined with the environment of the traction transformer and the density of train, the probability of adverse working conditions was determined according to the experience of field workers. By adding insulation resistance, tangent value of dielectric loss, oil and gas strength, power frequency voltage resistance, and leakage current into the Bayesian network, the fault diagnosis of the Bayesian network was more suitable for fault diagnosis of traction transformers.

In this paper, according to the field traction transformer fault, combined with the established Bayesian network diagnosis model, analysis, and reasoning, and based on the evidence obtained from the test data, the fault was analyzed. It is concluded that the fault was the damage of inter-turns insulation, inter-turns short circuit, inter-turns damp ingress, winding deformation, and inter-turns short circuit, which is basically consistent with the faults found in the field inspection and has guiding significance. Compared with the power transformer diagnosis model, it is more suitable for the traction transformer fault diagnosis with traction load characteristics.

The Bayesian network diagnosis method proposed in this paper greatly improves the efficiency of on-site maintenance and fault identification, avoids the great uncertainty caused by the subjective diagnosis results obtained by the existing on-site maintenance personnel based on abnormal test data, and makes the diagnosis results more objective and accurate.

Author Contributions: Conceptualization, Y.X., W.P., and X.G.; methodology, Y.X., S.B., and D.F.; validation, Y.X., and W.P.; formal analysis, Y.X., X.G., and S.L.; writing-original draft preparation, Y.X. and W.P.; writing-review and

editing, X.G., D.F., and S.L.; visualization, X.G. and S.B.; project administration, Y.X. and X.G.; funding acquisition, Y.X., W.P., and X.G. All authors have read and agreed to the submitted version of the manuscript.
Funding: This work was funded by Science and Technology Development Program of National Railway Research \& Design Institute of Signal Communication Group Company (Grant No. 2019H0802) and Sichuan Science and Technology Program Key Project (Grant No. 2020YJ0013).
Conflicts of Interest: The authors declare no conflict of interest.
