# Poisoning Network Flow Classifiers 

Giorgio Severi<br>Northeastern University<br>severi.g@northeastern.edu<br>John Holodnak<br>MIT Lincoln Laboratory

Simona Boboila<br>Northeastern University<br>Kendra Kratkiewicz<br>MIT Lincoln Laboratory

Alina Oprea<br>Northeastern University

Jason Matterer<br>STR*


## ABSTRACT

As machine learning (ML) classifiers increasingly oversee the automated monitoring of network traffic, studying their resilience against adversarial attacks becomes critical. This paper focuses on poisoning attacks, specifically backdoor attacks, against network traffic flow classifiers. We investigate the challenging scenario of clean-label poisoning where the adversary's capabilities are constrained to tampering only with the training data - without the ability to arbitrarily modify the training labels or any other component of the training process. We describe a trigger crafting strategy that leverages model interpretability techniques to generate trigger patterns that are effective even at very low poisoning rates. Finally, we design novel strategies to generate stealthy triggers, including an approach based on generative Bayesian network models, with the goal of minimizing the conspicuousness of the trigger, and thus making detection of an ongoing poisoning campaign more challenging. Our findings provide significant insights into the feasibility of poisoning attacks on network traffic classifiers used in multiple scenarios, including detecting malicious communication and application classification.

## ACM Reference Format:

Giorgio Severi, Simona Boboila, Alina Oprea, John Holodnak, Kendra Kratkiewicz, and Jason Matterer. 2023. Poisoning Network Flow Classifiers . In Annual Computer Security Applications Conference (ACSAC '23), December 04-08, 2023, Austin, TX, USA. ACM, New York, NY, USA, 15 pages. https: //doi.org/10.1145/3627106.3627123

## 1 INTRODUCTION

Automated monitoring of network traffic plays a critical role in the security posture of many companies and institutions. The large volumes of data involved, and the necessity for rapid decisionmaking, have led to solutions that increasingly rely on machine learning (ML) classifiers to provide timely warnings of potentially malicious behaviors on the network. Given the relevance of this task, undiminished despite being studied for quite a long time [54], a number of machine learning based systems have been proposed in recent years $[29,52,60,61,88]$ to classify network traffic.

[^0]The same conditions that spurred the development of new automated network traffic analysis systems, have also led researchers to develop adversarial machine learning attacks against them, targeting both deployed models [5, 9, 13, 25, 64] (evasion attacks) and, albeit to a lesser extent, their training process $[4,30,41,58]$ (poisoning attacks). We believe this second category is particularly interesting, both from an academic perspective as well as a practical one. Recent research on perceived security risks of companies deploying machine learning models repeatedly highlighted poisoning attacks as a critical threat to operational ML systems [22, 78]. Yet, much of the prior research on poisoning attacks in this domain tends to adopt threat models primarily formulated in the sphere of image classification, such as assuming that the victim would accept a pre-trained model from a third party [58], thus allowing adversarial control over the entire training phase, or granting the adversary the ability to tamper with the training labels [4]. As awareness of poisoning attacks permeates more extensively, it is reasonable to assume that companies developing these types of systems will exhibit an increased wariness to trust third parties providing pre-trained classifiers, and will likely spend resources and effort to control or vet both code and infrastructure used during training. For this reason, we believe it is particularly interesting to focus on the less studied scenario of an adversary who is restricted to tampering only with the training data (data-only attack) by disseminating a small quantity of maliciously crafted points, and without the ability to modify the labels assigned to training data (clean-label) or any other component of the training process.

Our aim is to investigate the feasibility and effects of poisoning attacks on network traffic flow classifiers, and in particular backdoor attacks - where an association is induced between a trigger pattern and an adversarially chosen output of the model. Our approach focuses on the manipulation of aggregated traffic flow features rather than packet-level content, as they are common in traffic classification applications [55, 61, 88]. We will focus on systems that compute aggregated features starting from the outputs of the network monitoring tool Zeek, because of its large user base. It is important to note that, despite the perceived relevance of poisoning attacks, it is often remarkably difficult for an adversary to successfully run a poisoning campaign against classifiers operating on constraint-heavy tabular data, such as cybersecurity data - like network flows or malware samples [73]. This is a well known issue in adversarial ML, illustrated in detail by [68] and often referred to as problem-space mapping. It stems from the complexity of crafting perturbations of the data points (in feature space) that induce the desired behavior in the victim model without damaging the structure of the underlying data object (problem space) necessary for it to be generated, parsed, or executed correctly. When dealing with aggregated network flow data, these difficulties compound with the inherent complexity of handling multivariate tabular data consisting of heterogeneous fields. To address these challenges, we design a novel methodology based on ML explanation methods to determine important features for backdoor creation, and map them back into the problem space. Our methods handle complex dependencies in feature space, generalize to different models and feature representations, are effective at low poisoning rates (as low as $0.1 \%$ ), and generate stealthy poisoning attacks.

In summary, we make the following contributions: (i) We develop a new strategy to craft clean-label, data-only, backdoor poisoning attacks against network traffic classifiers that are effective at low poisoning rates. (ii) We show that our poisoning attacks work across different model types, classification tasks, and feature representations, and we comprehensively evaluate the techniques on several network traffic datasets used for malware detection and application classification. (iii) We propose different strategies, including generative approaches based on Bayesian networks, to make the attacks inconspicuous and blend the poisoned data with the underlying training set. To ensure reproducibility, we evaluate our techniques on publicly available datasets, and release all the code used to run the experiments in the paper ${ }^{1}$.

## 2 BACKGROUND AND RELATED WORK

Machine Learning for Threat Detection. Machine learning methods have been successfully used to detect several cyber security threats, including: malicious domains [2, 3, 59, 62, 69], command-and-control communication between attackers and compromised hosts [55, 62], or malicious binaries used by adversaries for distributing exploit code and botnet commands [33, 79]. Several endpoint protection products $[31,32,50,51]$ are now integrating ML tools to proactively detect the rapidly increasing number of threats.

Adversarial Machine Learning. We can identify two major categories of integrity attacks against ML classifiers: (1) evasion attacks, which occur at test time and consist in applying an imperceptible perturbation to test samples in order to have them misclassified, and (2) poisoning attacks, which influence the training process (either through tampering with the training dataset or by modifying other components of the training procedure) to induce wrong predictions during inference. For details on other adversarial ML techniques, we direct the reader to the standardized taxonomy presented in [63].

In this study, we are focusing on backdoor poisoning attacks, a particularly insidious technique in which the attacker forces the learner to associate a specific pattern to a desired target objective usually the benign class in cybersecurity applications. While backdoor poisoning does not impact the model's performance on typical test data, it leads to misclassification of test samples that present the adversarial pattern. ML poisoning has become a top concern in industry [78]. In contrast to evasion attacks which need to generate per-sample perturbations, backdoor triggers, once learned, are powerful and universal as they can be applied to any samples during inference to alter their prediction.

Backdoor poisoning attacks against modern ML models were introduced by Gu et al. [23] in BadNets, where a small patch of bright

[^0]pixels (the trigger pattern) was added to a subset of images at training time together with an altered label, to induce the prediction of a target class. Subsequently, Turner et al. [82] and Shafahi et al. [74] devised clean-label backdoor attacks which require more poisoning data samples to be effective, but relax some strong assumptions of previous threat models, making them significantly more applicable in security scenarios.

In cybersecurity, the earliest poisoning attacks were designed against worm signature generation [57, 66] and spam detectors [56]. More recently, a few studies have looked at packet-level poisoning via padding [30, 58], feature-space poisoning in intrusion detection [4, 42], and label flipping attacks for IoT [65]. Severi et al. [73] proposed to use model interpretation techniques to generate cleanlabel poisoning attacks against malware classifiers. Their strategies are applicable to security datasets whose records are independent such as individual files or Android applications, which present a direct mapping from feature space to problem space. In contrast, our study explores attacks trained on network traffic, where multiple sequential connections are translated into one single feature-space data point; in this setting, inverting triggers from feature to problem space becomes particularly difficult due to data dependencies.
Model Interpretation Techniques. With the proliferation and increase in complexity of ML models, the field of explainable machine learning, focused on understanding and interpreting model predictions, has seen a substantial increase in popularity over recent years. We are particularly interested in model-agnostic interpretability techniques, which can be applied to any model. Linardatos et al. [44] provide a comprehensive taxonomy of these methods, and conclude that, among the black-box techniques presented, Shapley Additive explanations (SHAP) [48, 49] is the most complete, providing explanations for any model and data type both at a global and local scale. SHAP is a game-theory inspired method, which attempts to quantify how important each feature is for a classifier's predictions. SHAP improves on other model interpretation techniques like LIME [72], DeepLIFT [77] and Layer-Wise Relevance Propagation [6], by introducing a unified measure of feature importance that is able to differentiate better among output classes.

In this study, we also experiment with Gini index [21] and information gain $[38,40]$ - two of the most popular splitting algorithms in decision trees. A decision tree is built recursively, by choosing at each step the feature that provides the best split. Thus, the tree offers a natural interpretability, and a straightforward way to compute the importance of each feature towards the model's predictions.
Preserving Domain Constraints. Functionality-preserving attacks on network traffic have mostly looked at evasion during test time, rather than poisoning. For instance, Wu et al. [84] proposed a packet-level evasion attack against botnet detection, using reinforcement learning to guide updates to adversarial samples in a way that maintains the original functionality. Sheatsley et al. [76] study the challenges associated with the generation of valid adversarial examples that abide domain constraints and develop techniques to learn these constraints from data. Chernikova et al. [13] design evasion attacks against neural networks in constrained environments, using an iterative optimization method based on gradient descent to ensure valid numerical domain values. With our constraint-aware


[^0]:    ${ }^{1}$ https://github.com/ClonedOne/poisoning_network_flow_classifiers

problem-space mapping, which also takes into account dependencies in network traffic, we delve one step further into the challenging issue of designing functionality-preserving attacks.

Significant advances have been made recently with respect to generating multivariate data. Modern tabular data synthesizers of mixed data types leverage the power of generative adversarial networks [11, 18, 19, 86, 91] and diffusion models [39] to create realistic content from the same distribution as the original data. Among the different frameworks, FakeTables [11] is the only attempt at preserving functional dependencies in relational tables. However, its evaluation is limited to Census and Air Carrier Statistics datasets, and its ability to capture more complex relationships between variables is unclear.

In this work, we model conditional dependencies in the traffic using Bayesian networks - a common choice for generating synthetic relational tables [15, 27, 36, 70, 90]. Bayesian networks offer increased transparency and computational efficiency over more complex generative models like generative adversarial networks [36]. We believe this is an important advantage in our setting, which deals with large volumes of network traffic featuring multiple variables (e.g., log fields). In cybersecurity, Bayesian networks have also been used to learn traffic patterns and flag potentially malicious events in intrusion detection systems [16, 34, 83, 85].

## 3 THREAT MODEL

Adversary's Capabilities. Recent work analysing the training time robustness of malware classifiers [73, 89] pointed out that the use of ever larger quantities of data to train effective security classifiers inherently opens up the doors to data-only poisoning attacks, especially in their more stealthy clean-label [74, 81] variants where the adversary does not control the label of the poisoned samples. Thus, in this work, we constrain the adversary to cleanlabel data-only attacks. This type of setup moves beyond the classic threat model proposed by Gu et al. [23] and adopted by other research $[12,47,58]$, where the adversary was able to tamper with not only the content of the training points but also the corresponding ground-truth labels.

Network traffic labeling is often done using antivirus tools or external threat services (e.g., Intrusion Detection Systems, VirusTotal ${ }^{2}$, etc.) [24, 62], making label manipulation hard for an adversary. Hence, clean-label poisoning is a more realistic threat model, where access to even a single compromised host is enough to carry out the attack by injecting the backdoor into the benign traffic, without tampering with the data collection and labeling process. By disseminating innocuous looking -but adversarially crafted- data, i.e., the backdoor, the adversary is able to tamper with a small, yet effective, percentage of the training set and induce the desired behavior in the learned model.

To design the trigger, the adversary requires access to a small amount of clean labeled data, $D_{a}$, from a similar distribution as the victim's training data $D . D_{a}$ is used for crafting the backdoor pattern and it is disjoint from the training and test datasets.

We consider an adversary who has query-only access to the machine learning classifier. This allows the attacker to use the SHAP

[^0]explanation technique to compute feature importance coefficients, but it prevents any form of inspection of model weights or hidden states. This scenario is very common for deployed models, as they often undergo periodical re-training but are only accessible behind controlled APIs. Interacting with a victim system, however, always imposes a cost on the attacker, whether in terms of actual monetary expenses for API quotas, or by increasing the risk of being discovered. Motivated by this observation, we also explore the use of model interpretation methods that do not require any access to the classifier, but instead leverage proxy models on local data (i.e., information gain and Gini coefficients), and can be used even when the model is not subject to re-training cycles. Several previous studies on training time attacks [47, 58] relax the model access constraints, assuming an adversary can train a ML classifier and provide it to the victim through third-party platforms such as Machine Learning as a Service (MLaaS) [71]. However, we believe that this threat model is rapidly becoming obsolete, at least in the cybersecurity domain, due to the push for stricter cyber hygiene practices from security vendors, including the reluctance to trust third-party model providers and MLaaS platforms [1, 67].

Importantly, our threat model requires the adversary to have a small footprint within the victim network. In practice, the attack could be run by controlling even a single internal host and some external IPs. . The crafted trigger models a specific traffic pattern in a time window, independent of IP values.

Adversary's Objective. The main objective of the adversary is to acquire the ability to consistently trigger desired behavior, or output, from the victim model, after the latter has been trained on the poisoned data. In this study, we focus on the binary class scenario ( $0 / 1$ ), where the goal is defined as having points of a chosen victim class being mis-labeled as belonging to the target class, when carrying a backdoor pattern that does not violate the constraints of the data domain. For instance, in the benign/malicious case, the adversary attempts to have malicious data points mis-classified as benign, where "benign" represents the target class.

Adversary's Target. We select two representative ML classifier models as targets for our attacks: Gradient Boosting decision trees, and Feed-forward Neural Networks. Both of these models have been widely-used in intrusion detection for classifying malicious network traffic, with decision trees often preferred in security contexts due to their easier interpretation [35]. We study two use cases of network traffic classifiers: (1) detection of malicious activities, and (2) application classification.

Data Format. In our threat model, network traffic consists of connection logs ("conn.log" files), which are extracted from packet-level PCAP files using the Zeek ${ }^{3}$ monitoring tool. We use a subset of the Zeek log fields previously used in the literature that are effective at detecting malicious traffic [61]. The Zeek log fields used in our study are described in Appendix A, Table 5, and include port, IP address, protocol, service, timestamp, duration, packets, payload bytes, and connection state. Thus, the input data is tabular and multivariate, consisting of multiple log fields in either numeric format (e.g., bytes, packets, etc.) or categorical format (e.g., connection state, protocol, etc.). A data point in this domain is represented by

[^1]
[^0]:    ${ }^{2}$ https://www.virustotal.com/

[^1]:    ${ }^{3}$ https://zeek.org/ Previously known as Bro.

![img-0.jpeg](img-0.jpeg)

Figure 1: Pipeline for poisoning network flow classifiers.
a sequence of raw log records grouped together. This problem-space data point is mapped into a corresponding feature-space data point through various aggregation techniques applied over the log field values.

Feature Representation. We study two standard and widely adopted feature mapping techniques: (1) aggregation, to produce statistical features, and (2) embeddings- using auto-encoders to automatically generate feature vectors. Traffic statistics have multiple applications in network monitoring and security [53, 88], which require dealing with large volumes of data. For instance, distinct count metrics are used to identify scanning attacks, while volume metrics or traffic distributions over port numbers and IP address ranges are utilized in anomaly detection [8]. We use aggregation methods similar to previous works [8, 61], to derive statistics of connections. The statistical features used in our study are described in Appendix A, Table 6, and include traffic volume by internal IP (in bytes and packets) within a 30-sec time window, connection counts by transport protocol, connection counts by state, etc.

Recent literature also features a variety of approaches for network traffic classification based on auto-encoders [14, 26, 52, 88]. Auto-encoders are unsupervised models that learn to reconstruct the training data. They are often used either for anomaly detection or to learn high level features to use in downstream classifiers.

Similar to existing work in poisoning attacks and defenses, we assume the feature engineering process is known to the adversary. Removing this assumption and understanding transferability under different feature representations is an interesting open question.

## 4 ATTACK STRATEGY

The formulation of an appropriate trigger pattern is a fundamental aspect of backdoor poisoning attacks The inherent intricacies of network traffic - feature dependencies, multiple data modalitiesmakes it particularly challenging to ensure that the trigger is mapped correctly to realizable actions in problem space [68]. This is a stark difference with the image domain, where the backdoor trigger can be extremely simplistic, such as a bright colored square [23].

There are three key requirements that characterize a feasible poisoning attack: (i) To be effective, the trigger should be easy to associate to the target class by the victim model. (ii) The injected pattern should appear inconspicuous, so as to avoid detection by potential human or automated observers. (iii) The perturbations induced by the injection of the trigger pattern should not affect data validity. While the first two requirements are generic to any backdoor attack, the third one translates to additional constraints on adversarial actions in the network domain, specifically: (i) The adversary can only insert traffic, but not modify or remove existing traffic. (ii) Data semantics and dependencies need to be preserved, such as value restrictions on specific fields (e.g., upper/lower bounds on packet length), feature correlations (e.g., protocols use specific ports), etc. (iii) The injected pattern needs to handle multiple data types, i.e., numeric and categorical.

### 4.1 Crafting the Poisoning Data

To address these challenges, we design a novel methodology that leverages insights from explanation-based methods to determine important features in feature space, then map them back to constraintaware triggers in problem space. The mapping can be done via: (i) poisoning attacks using connections directly extracted from malicious traffic; (ii) poisoning attacks with reduced footprint; (iii) generative Bayesian models to increase attack stealthiness.

Our attack strategy, illustrated in Figure 1, consists of five main phases:
(I) Select a subset of features that are most important for the class that the adversary wishes to misclassify using model explanation techniques;
(II) Find an ideal trigger in feature space - we call this an assignment;
(III) Find a data point that best approximates the ideal trigger values - this will be our prototype trigger;
(IV) Identify a set of real connections that induce the values observed in the prototype - this set of connections will be our actual trigger;
(V) Inject the trigger in points of the target class, potentially trying to minimize its conspicuousness.

Phase $l$. We first identify the most relevant features for the class to be misclassified. Our goal is to leverage highly informative features to coerce the model into associating the trigger pattern with the target class. There are a variety of techniques from the field of model interpretability used to estimate the effect of specific features towards the classifier's decision.

We start by adapting the SHAP-based technique from [73] to the network domain. Here, SHAP values are computed for a subset of points in $D_{a}$, and their contributions summed per-feature, to identify the ones most contributing to each class. This approach has the advantage of being model agnostic, allowing us to estimate feature importance coefficients for any possible victim model. Unfortunately, it also assumes the adversary is able to perform a possibly large number of queries against the victim model.

To address this potential limitation, we also evaluate the effect of selecting the important features through more indirect ways. In particular we can leverage the information gain and Gini coefficient metrics used in training decision trees, to estimate the global contributions of each feature. We report a list of the most commonly selected features across our experiments in Appendix C Table 7.

The attentive reader will notice here that the approaches we mentioned to estimate feature importance are quite different. This is intentional, and it highlights the modularity of this component. As long as the adversary is capable of obtaining global estimates of feature importance scores, they can use them to guide the attack. Moreover, with potential future discoveries in the, extremely active, field of model interpretation, novel methods could be used to improve the effectiveness of this attack.

Phase II. Once the subset of important features is selected, we can proceed to find a suitable assignment of values. To be consistent with real traffic constraints, we need to ensure that the values that we select represent information that can be easily added to data points of the non-target class, by injecting new connections, without having to remove existing connections. Our features are mainly count-based, hence injecting the trigger will increase feature values. Thus, for the assignment, we select values that correspond to the top $t^{\text {th }}$ percentile of the corresponding features for non-target class points. Choosing a high percentile is a reasonable heuristic, as it provides a strong signal. In practice, setting this parameter to the $95^{\text {th }}$ percentile performed well in our experiments.

Phase III. Armed with the desired assignment for the selected features, we can proceed to identify an existing data point that approximates these ideal trigger values. To find it, in our first attack we leverage a mimicry method to scan the non-target (e.g., malicious) class samples and isolate the one with the lowest Euclidean distance from the assignment, in the subspace of the selected features. We call this point in feature space the trigger prototype. An example of the trigger prototype in feature space is given in Appendix C Table 8 .

Phase IV. Up until this point, the process was working completely in feature space. Our explicit goal, however, is to run the attack in problem space. So the next step in the attack chain is to identify, in the attacker's dataset, a contiguous subset of log connections that best approximate the prototype. Enforcing that the selected subset is contiguous ensures that temporal dependencies across log records are preserved. This subset of connections represents the actual trigger that we will use to poison the target-class training data. Appendix C Table 9 shows an excerpt from a trigger materialized as a pattern of connections.

Phase V. Finally, it is time to inject the trigger in the training data. This step is quite straightforward, as it the adversary is in control of generating the poisoned data, and can execute the trigger connections in the specified order. We next describe two strategies for increasing trigger stealthiness before injection.

### 4.2 Increasing Attack Stealthiness

Beyond the basic objective of maximizing attack success, the adversary may have the additional goal of minimizing the chance of being detected. To achieve this secondary goal, the adversary may wish to slightly alter the trigger before injecting it in the training data. In particular, we study two strategies: (1) trigger size reduction and (2) trigger generation using Bayesian models.

Trigger size reduction. The first strategy consists of minimizing the trigger footprint, by removing all the connections that are not strictly necessary to achieve the values specified in the prototype for the subset of important features (such as connections on other ports). We then select the smallest subset of contiguous connections that would produce the desired values for the selected features.

Trigger generation using Bayesian networks. The second strategy aims at reducing the conspicuousness of the trigger by blending it with the set of connections underlying the data point where it is embedded. To this end, we generate the values of the log fields
corresponding to non-selected features in the backdoor to make them appear closer to values common in the target-class natural data $\in D_{a}$. Note that fields influencing the selected (important) features will not be modified, because they carry the backdoor pattern associated with the target class. Our generative approach leverages Bayesian networks, a widely-used probabilistic graphical model for encoding conditional dependencies among a set of variables, and deriving realistic samples of data [15, 27, 70]. Bayesian networks consist of two parts: (1) structure - a directed acyclic graph (DAG) that expresses dependencies among the random variables associated with the nodes, and (2) parameters - represented by conditional probability distributions associated with each node.

Structure. Given our objective to synthesize realistic log connections (in problem space) that lead to the feature-space prototype, we construct a directed acyclic graph $G=(V, E)$ where the nodes $x_{i} \in V$ correspond to fields of interest in the connection log and the edges $e_{i j} \in E$ model the inter-dependencies between them. We explore field-level correlations in connection logs using two statistical methods that have been previously used to study the degree of association between variables [37]: the correlation matrix and the pairwise normalized mutual information. In our experiments, both methods discover similar relationships in $D_{a}$, with the mutual information approach bringing out additional inter-dependencies. Note that we are not interested in the actual coefficients, rather, in the associational relationships between variables. Thus, we extract the strongest pairwise associations, and use them in addition to domain expertise to guide the design of the DAG structure. For instance, there is a strong relationship between the number of response packets and source packets (resp_pkts $\leftrightarrow$ orig_pkts); between the protocol and the response port (proto $\leftrightarrow$ resp_p); between the connection state and protocol (conn_state $\leftrightarrow$ proto), etc.

There is a large body of literature on learning the DAG structure directly from data. We point the interested reader to a recent survey by Kitson et al. [37]. However, computing the graphical structure remains a major challenge, as this is an NP-hard problem, where the solution space grows super-exponentially with the number of variables. Resorting to a hybrid approach [37] that incorporates expert knowledge is a common practice that alleviates this issue. The survey also highlights the additional complexity in modeling the DAG when continuous variables are parents of discrete ones, and when there are more than two dependency levels in the graph.

Based on the above considerations, we design the directed acyclic graph presented in Figure 2. For practical reasons, we filter out some associations that incur a high complexity when modeling the conditional probability distributions. To ensure that the generated traffic still reflects the inter-dependency patterns seen in the data, we inspect the poisoned training dataset using the same statistical techniques (correlation matrix and mutual information). We include the mutual information matrix on the clean adversarial dataset (Appendix E, Figure 8a) and on the training dataset poisoned with the Generated trigger method (Appendix E, Figure 8b), to show that the associational relationships between variables are preserved after poisoning (though the actual coefficients may vary).

Parameters. Bayesian networks follow the local Markov property, where the probability distribution of each node, modeled as a random variable $x_{i}$, depends only on the probability distributions

![img-1.jpeg](img-1.jpeg)

Figure 2: Directed Acyclic Graph (DAG) representing the inter-dependencies between log connection fields.
of its parents. Thus, the joint probability distribution of a Bayesian network consisting of $n$ nodes is represented as: $p\left(x_{1}, x_{2}, \cdots, x_{n}\right)=$ $\prod_{i=1}^{n} p\left(x_{i} \mid x_{P_{i}}\right)$, where $P_{i}$ is the set of parents for node $i$, and the conditional probability of node $i$ is expressed as $p\left(x_{i} \mid x_{P_{i}}\right)$.

Sampling. The DAG is traversed in a hierarchical manner, one step at a time, as a sequential decision problem based on probabilities derived from the data, with the goal of generating a realistic set of field-value assignments. The value assignments for nodes at the top of the hierarchy are sampled independently, from the corresponding probability distribution, while the nodes on lower levels are conditioned on parent values during sampling. We compute the conditional probabilities of categorical fields (e.g., ports, service, protocol, connection state), and model numerical fields (e.g., originator/responder packets and bytes) through Gaussian kernel density estimation (KDE). An example of the KDE learned from the data, and used to estimate the number of exchanged bytes between a source (originator) and a destination (responder), given the number of packets, is presented in Appendix D, Figure 7.

Given the complexity of sampling from hybrid Bayesian networks, we approximate the conditional sampling process with a heuristic, described in Table 1. We consider an example where the log fields corresponding to the most important features have been set to the TCP protocol and responder port 80 . Our generative method synthesizes values for the rest of the fields, in an attempt to make the trigger blend in with the target class. We show in our evaluation that the synthesized poisoning traffic is a good approximation of clean network traffic, both in terms of Jensen-Shannon distance between distributions (Section 5.3) and preservation of field-level dependencies (Appendix E).

## 5 EXPERIMENTAL RESULTS

### 5.1 Experimental Setup

In this section, we describe the datasets and performance metrics used in our evaluation. We also present the baseline performance of the target classifiers (without poisoning).
Datasets. We used three public datasets commonly used in cybersecurity research for intrusion detection and application classification.

CTU-13 Neris Botnet: We started our experimentation with the Neris botnet scenario of the well-known CTU-13 dataset [20]. This dataset offers a window into the world of botnet traffic, captured within a university network and featuring a blend of both malicious and benign traffic. Despite the sizeable number of connections ( $\approx 9 * 10^{6}$ ), the classes are extremely imbalanced, with a significantly larger number of benign than malicious data points. Note that the class imbalance is a common characteristic of security applications.

The Neris botnet scenario unfolds over three capture periods. We use two of these periods for training our models, and we partition the last one in two subsets, keeping $85 \%$ of the connections for the test set, and $15 \%$ for the adversarial set, $D_{a}$.

CIC IDS 2018 Botnet: From CTU-13, we moved to a recent dataset for intrusion detection systcheems, the Canadian Institute for Cybersecurity (CIC) IDS 2018 dataset [75]. We experimented with the botnet scenario, in which the adversary uses the Zeus and Ares malware packages to infect victim machines and perform exfiltration actions. This dataset includes a mixture of malicious and benign samples and is also heavily imbalanced.

CIC ISCX 2016 dataset: This dataset contains several application traffic categories, such as chat, video, and file transfer. We leverage the CIC ISCX 2016 dataset [17] to explore another scenario where an adversary may affect the outcome via poisoning: detection of banned applications. For instance, to comply with company policies, an organization monitors its internal network to identify usage of prohibited applications. An adversary may attempt to disguise traffic originating from a banned application as another type of traffic. We study two examples of classification tasks on the non-vpn traffic of this dataset: (1) File vs Video, where we induce the learner to mistake video traffic flows as file transfer, and (2) Chat vs Video, where the classifier mis-labels video traffic as chat communication.

Performance Metrics. Similar to previous work in this area [58, 73], we are interested in the following indicators of performance for the backdoored model:

- Attack Success Rate (ASR). This is the fraction of test data points which are mis-classified as belonging to the target class. We evaluate this metric on a subset of points that have been previously correctly classified by a clean model trained with the same original training data and random seed.
- Performance degradation on clean data. This metric captures the side effects of poisoning, by evaluating the ability of the backdoored model to maintain its predictive performance on clean samples. Let $F_{1}^{p}$ be the F1 score of the poisoned model on the clean test set, and $F_{1}^{r}$ the test score of a non-poisoned model trained equally, the performance degradation on clean data at runtime is: $\Delta F_{1}=\left|F_{1}^{p}-F_{1}^{r}\right|$.
Unless otherwise noted, all the results shown in the following sections are averages of five experiments with different random seeds, reported with their relative standard deviations.

Parameters. We define $p \%$ as the percentage of feature-space points of the training dataset that have been compromised by an adversary. Since the amount of poisoned points is generally a critical parameter of any poisoning attack, we measure the attack performance across multiple poison percentage values $p \%$. At runtime, we randomly select a subset of test points to inject the trigger. Specifically, we select 200 points for the CTU-13 and CIC IDS 2018 datasets, and 80 for the CIC ISCX 2016 dataset (due its smaller size).
Baseline Model Performance. As mentioned in our threat model, we consider two representative classifiers: a Gradient Boosting Decision Tree (GB), and a Feed Forward Neural Network (FFNN). Note that we are not interested in finding the most effective possible learner for the classification task at hand, instead our focus is on

Table 1: Sampling method for each dependency described in the DAG from Figure 2. In this example, we assume that the most important features correspond to protocol and port; their values (TCP protocol on port 80) have been determined in Phase II of our strategy. Here, our generative method samples the rest of the log field values. $D_{a}$ represents the attacker's dataset.


Table 2: Base performance of the classifiers, avg. over 5 runs.


selecting generic and widely adopted classifiers to showcase the adaptability of our attack strategy. Baseline values for accuracy, F1 score, precision, and recall of the classifiers are reported in Table 2.

### 5.2 Impact of Feature Selection

Similar to the procedure reported in [73], our initial feature selection strategy revolved around computing local feature importance scores with SHAP and then aggregating them to obtain global indicators for each feature of the magnitude and direction of impact for each feature. As mentioned in Section 4.1, however, this approach has an important drawback: it requires to perform a potentially large number of queries against the victim classifier. To obviate this issue, we also considered ways in which the adversary can extract feature importance estimates directly from their data subset, $D_{a}$. In practice, we experimented with fitting a Decision Tree on $D_{a}$, following either the Gini impurity (Gini) or the information gain (Entropy) criteria, and using the importance estimate given by the reduction of the criterion induced by the feature ${ }^{4}$.

The three feature selection strategies implemented (Entropy, Gini, SHAP) use the top eight most important features to design the trigger pattern, and are compared against Random, a baseline strategy that chooses the same number of features uniformly at

[^0]![img-2.jpeg](img-2.jpeg)

Figure 3: Attack success rate (ASR) for the CTU-13 Neris Botnet scenario with different models and feature selection strategies.
random. Looking at the features selected by the different strategies, we generally observe that Entropy and Gini tend to assign scores that are strongly positive only for a very small number of features (typically 1-3), while SHAP scores are distributed more evenly. This observation, together with the desire to minimize the trigger footprint, informed our decision to select the eight most relevant features. We also experimented with different values of this


[^0]:    ${ }^{4}$ Using the implementation in Scikit-Learn https://scikit-learn.org/stable/modules/ generated/sklearn.tree.DecisionTreeClassifier.html

parameter, halving and doubling the number of selected features, but we found that eight were sufficient to achieve satisfying ASRs.

Attack Success Rate: We show the results of these experiments in Figure 3. On average, we found the Entropy strategy to be the most successful against both classifiers on this dataset. The Random strategy leads to inconsistent results: occasionally, it stumbles upon useful features, but overall attacks relying on Random selection perform worse than attacks guided by the other feature selection methods. Figure 3 also illustrates a major finding - our attacks perform well even at very small poisoning rates such as $0.1 \%$, where they reach an attack success rate of up to 0.7 against the Gradient Boosting classifier. As expected, increasing the poisoning percentage leads to an increase in attack success rate; for instance, an ASR of 0.95 is obtained with Entropy at $1.0 \%$ poisoning. By comparison, previous works only considered larger poisoning rates (e.g, $2 \%$ to $20 \%$ in [41], $20 \%$ samples from nine (out of ten) non-target classes in [58]). We also notice that some of the variance in the ASR results can be attributed to a somewhat bimodal distribution. This can be partially explained with differences in the resulting trigger sizes, with Figure 4b highlighting the correlation between larger triggers and higher ASR. We leave a more detailed analysis of the distribution of the ASR scores for future work.

Furthermore, we observe that the SHAP strategy, while working well in some scenarios (especially for the application classification tasks in Section 5.5) does not, on average, lead to better results than estimating feature importance through proxy models (Entropy and Gini). This makes the attack quite easy to run in practice, as it circumvents the necessity to run multiple, potentially expensive, queries to the victim model.

Performance degradation on clean data: While these results show that the attack causes the poisoned model to misclassify poisoned data, we also want to make sure that the performance on clean data is maintained. The average $\Delta F_{1}$ across poisoning rates and feature selection strategies in our experiments was below 0.037 , demonstrating that the side effects of the attack are minimal. The neural network model exhibits on average a slightly larger decrease when compared against the Gradient Boosting classifier, especially when the Entropy and Gini feature selection strategies are used.

### 5.3 Attack Stealthiness

Remaining undetected is an important factor in running a successful poisoning campaign. Here, we study the impact of our two approaches for increasing attack stealthiness described in Section 4.2: reducing the trigger size (Reduced trigger) and generating the trigger connections using Bayesian networks (Generated trigger). We start by analyzing the attack success with the different types of triggers, followed by a quantitative comparison of their stealthiness in feature space (via anomaly detection), and in problem space (via the Jensen-Shannon distance).

Evaluation of attack success. Figure 4a shows the attack success rate as a function of the poisoning percentage for the three different types of triggers: Full, Reduced, and Generated. We observe that all triggers are able to mount effective attacks against the Gradient Boosting classifier, with attack success rates over 0.8 when $0.5 \%$ or more of the training data is poisoned. The Feed-forward Neural Network is generally more resilient to our attacks: the Full trigger

Table 3: Area under the Precision-Recall Curve and F1 score obtained by performing anomaly detection on the poisoned data with an Isolation Forest model trained on a clean subset of the training data. CTU-13 Neris, at $1 \%$ poisoning rate.


and Reduced trigger deliver an attack success rate of about 0.7 and 0.4 , respectively, while the Generative trigger is able to synthesize more effective triggers, which leads to attack success rates over 0.7 .

Figure 4b studies the correlation between trigger size (measured in number of connections) and attack success rate for each type of trigger. Each data point represented in the figure constitutes a separate experiment, while the regression lines capture the trend (how ASR changes as the trigger size changes). These figures show that the generative method leads to consistently smaller triggers than the other two methods, without sacrificing attack success. This result is indicative of the power of generative models in knowledge discovery, and, in our case, their ability to synthesize a small set of realistic log connections that lead to the feature-space prototype. Figure 4 b also shows that the size reduction strategy is able to create triggers (Reduced trigger) that are smaller than the Full trigger, but at the expense of the attack success rate.

Evaluation of attack stealthiness in feature space. Next, we evaluate the attack stealthiness in feature space, using the Isolation Forest [45] algorithm for anomaly detection. The objective of this experiment is to see whether a standard technique for anomaly detection can identify and flag the poisoned samples as anomalies. The anomaly detector is trained on a clean subset of data, which is completely disjoint from the poisoned data points and consists of $10 \%$ of the entire training dataset.

Table 3 presents the anomaly detection results on the poisoned data obtained with each trigger type (Full, Reduced, and Generated). For comparison, we evaluate both the entropy-based and the SHAPbased feature selection strategies used to craft the injected pattern. Since SHAP queries the model to compute feature relevance scores, we present the anomaly detection results separately for a SHAPguided attack against a Gradient Boosting classifier and against a Feed-forward Neural Network. Across the board, we observe very low Precision-Recall area under the curve (AUC) scores (in the 0.045 - 0.099 range), as well as very low $F_{1}$ scores (in the $0.012-0.019$ range). These results demonstrate the difficulty of differentiating the poisoned data points from the clean data points, and indicate that the poisoning attacks are highly inconspicuous in feature space.
Evaluation of attack stealthiness in problem space. We also evaluate attack stealthiness in problem space, in terms of how

![img-3.jpeg](img-3.jpeg)
(b) Correlation between the number of connections composing the trigger and the attack success rate (ASR). Each point represents a separate experiment. Curve fitting illustrating the trend is performed using linear regression.

Figure 4: Analysis of trigger selection strategy. CTU-13 Neris Botnet scenario, with the Entropy feature selection strategy.
close the poisoned data is to the target class, here represented by the benign class (normal traffic). We leverage the Jensen-Shannon divergence [43], a normalized and symmetrical scoring method for measuring the similarity between two probability distributions, and in particular we use the distance formulation defined as the square root of the divergence, which is zero for identical distributions. We compute the distance for each field in the connection logs (e.g., bytes, port, connection state, etc.), and report the average across all fields. As a baseline, we compute the average Jensen-Shannon distance between the target class points (benign log connections only) of the training and test datasets, capturing the distribution shift between train and test data. For the CTU-13 Neris Botnet dataset, we evaluated this reference distance as being D_REF $=$ JS(TRAIN, TEST) $=0.24$.

Figure 5 shows the Jensen-Shannon distance between the poisoned and clean training dataset for each of the trigger types. The figure illustrates that all three strategies produce stealthy attacks, characterized by average Jensen-Shannon distances that are comfortably lower than D_REF. Furthermore, the generative method (Generated trigger) constructs the most inconspicuous triggers, followed by the trigger size reduction method (Reduced trigger).

### 5.4 Impact of Feature Representation

The feature representation used by the learning task can strongly influence the attack success. In the next set of experiments, we

![img-4.jpeg](img-4.jpeg)

Figure 5: Jensen-Shannon distance between the poisoned and clean training dataset, averaged over all considered conn.log fields. For reference, the average JS distance value between the original training data and test data is 0.24 . CTU-13 Neris Botnet experiments, at $1 \%$ poisoning rate.
study feature encodings, which are automatically learned with an auto-encoder architecture. Together with statistical features, encoded features are common in network traffic classification, and auto-encoder models have been widely adopted for this task by previous works [14, 26, 52, 88]. To generate these features, we first train an auto-encoder model in an unsupervised manner, with the goal of minimizing the reconstruction error. Then the encoder portion of the model is run on the same training data to extract the

Table 4: Results on the CTU-13 Neris Botnet scenario, where the victim model uses an auto-encoder to learn the feature representation. Entropy strategy.


high-level features used to train the feed-forward neural network architecture considered in previous experiments. Since the autoencoder requires its inputs to be of a consistent shape, instead of features extracted from 30-second time windows, here the model is provided with an input representation consisting of contiguous blocks of 100 connections. Given that features are extracted from connection blocks of a fixed size, we also fix the trigger size to be 50 connections long. We found this value empirically by experimenting with different trigger sizes, and noticed that smaller ones would lead to unsatisfying attack results. While the trigger is relatively large compared to the unit block size, it is worth noting that the total number of connections introduced by the attack is still very limited when compared to the size of the the training set.

Table 4 reports the mean attack success rate of the Entropy strategy when applied in this setup, at different poison percentages, together with its standard deviation across 5 experiments and the average degradation in performance of the victim model on clean data. Since the auto-encoder was trained in an unsupervised fashion to minimize the reconstruction loss, we expect this training loss to impact negatively the overall success of the attack. In fact, we do observe a general reduction of the success rate compared to the simple neural network model, especially for limited poisoning budgets ( $\leq 1 \%$ ). However, if the adversary is allowed to increase the poisoning rate beyond $1 \%$, we observe that the attack scales nicely with larger poisoning budgets. At the same time, the $\Delta F_{1}$ values remain generally low even at larger poison percentages.

### 5.5 Other datasets

In the previous sections, we carried out an in-depth evaluation of various attack characteristics and their impact on the attack success. In this section, we investigate how generalizable this poisoning approach is by testing it on different datasets and other classification tasks. We evaluate here a second cybersecurity task on the CIC IDS 2018 dataset, and two application classification scenarios on CIC ISCX 2016. For all of these case studies, we use the statistical features (see Appendix A, Table 6) and the full trigger strategy.

We report the attack success rate at different poisoning percentages in Figure 6. Due to the much smaller size of the ISCX dataset, we test up to slightly larger poison percentage values - for instance in the Chat/Video scenario, $0.1 \%$ of the training set would amount to a single poisoning point. In general, we observe similar trends as in previous experiments, with the SHAP and Entropy strategies performing similarly, and achieving significant attack success rates even with very limited poison budgets.

We also evaluated the poisoned model on clean test data, to verify whether the poisoned model is still able to classify clean test data correctly. We obtained very limited reductions in $F_{1}$ scores:
![img-5.jpeg](img-5.jpeg)

Figure 6: Attack success rate (ASR) on the CIC IDS 2018 Botnet and the CIC ISCX 2016 dataset, full trigger.
$\Delta F_{1}$ is between 0.002 and 0.046 , with the SHAP strategy resulting in slightly larger shifts than the other feature selection methods.

## 6 DISCUSSION AND LIMITATIONS

Well-formed triggers. The problem-space mapping of the triggers is a particularly challenging task, owing to its inherent complexity on arbitrary networks. For instance, the adversary may experience a situation where two connection events are inter-dependent, due to the internal state of Zeek, but the trigger does not include both of them simultaneously - this could occur if the connections happen across the border of two time windows. Inter-dependent connection events may take place in the case of hosts running the FTP protocol. Documentation on this type of connections for Zeek is quite scarce, but a dedicated attacker could allocate time and resources to enumerate all possible corner cases and explicitly avoid them during the trigger creation phase.

Our generative strategy leads to a high ASR with a small footprint and is applicable to both stateless (UDP) and stateful protocols (TCP). However, it could generate some connection events that are

not feasible in practice, particularly for stateful protocols (TCP). There are two ways to address this potential issue. First, given the relentless pace of improvements in generative models, including those targeting tabular data [7, 87], we expect that the ability of generative models to infer the inter-feature constraints that characterize this data modality will increase significantly in the very short term. In parallel, the adversary could attempt to verify the correctness of the generated connections using a model checker and a formal model of the TCP protocol, and simply reject the nonconforming ones. Both approaches are exciting avenues for future research, and we leave their in-depth analysis to future work.

Labeling. Network traffic labeling usually relies on intrusion detection systems, antivirus tools and external threat services [24, 62]. In our threat model, the adversary has no control on the labels, and simply injects the poisoning traffic into benign connections. Hence, the question arises: Will the poisoned samples still have a benign label? We assume the poisoned samples remain benign, based on the following reasons: (1) The Jensen-Shannon distance between poisoned and clean samples is very small (Figure 5); (2) Anomaly detection (Table 3) cannot identify the poisoned samples (F1 score $<0.02$ ); (3) Features are extracted from connections metadata, and the actual packet contents do not need to be malicious.

Mitigation. We designed methods to hide the poisoning campaign, and showed that our poisoning points are difficult to identify both in feature space, by using anomaly detection techniques, and in problem space, by analysing the distributional distance of poisoned data. Defending ML models from backdoor attacks is an open, and extremely complex, research problem. Many of the current proposed solutions are designed to operate in the computer vision domain [10], or on specific model architectures [46, 80]. In contrast, our attack method generalizes to different model typologies. Moreover, initial research on defending classifiers from backdoor attacks in the security domain [28] highlighted potential trade-offs between robustness and utility (e.g., defenses that rely on data sanitization may mistakenly remove a high number of benign samples in an attempt to prune out potentially poisoned samples). By releasing new attack strategies, we hope to encourage future research in the challenging direction of defending against backdoor attacks on network traffic.

## 7 CONCLUSIONS

With this work we investigated the possibility of carrying out dataonly, clean-label, poisoning attacks against network flow classifiers. We believe this threat model holds substantial significance for the security community, due to its closer alignment with the capabilities exhibited by sophisticated adversaries observed in the wild, and the current best practices in secure ML deployments, in contrast to other prevailing models frequently employed.

The attack strategy we introduce can effectively forge consistent associations between the trigger pattern and the target class even at extremely low poisoning rates ( $0.1-0.5 \%$ of the training set size). This results in notable attack success rates, despite the constrained nature of the attacker. While the attack is effective, it has minimal impacts on the victim model's generalization abilities when dealing with clean test data. Additionally, the detectability of the trigger can
be lessened through different strategies to decrease the likelihood of a defender discovering an ongoing poisoning campaign.

Furthermore, we demonstrated that this form of poisoning has a relatively wide applicability for various objectives across different types of classification tasks. The implications of these findings extend our understanding of ML security in practical contexts, and prompt further investigation into effective defense strategies against these refined attack methodologies.

## ACKNOWLEDGMENTS

This research was sponsored by the U.S. Army Combat Capabilities Development Command Army Research Laboratory (DEVCOM ARL) under Cooperative Agreement Number W911NF-13-2-0045, and the Department of Defense Multidisciplinary Research Program of the University Research Initiative (MURI) under contract W911NF-21-1-0322.

DISTRIBUTION STATEMENT A. Approved for public release. Distribution is unlimited. This material is based upon work supported by the Under Secretary of Defense for Research and Engineering under Air Force Contract No. FA8702-15-D-0001. Any opinions, findings, conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the Under Secretary of Defense for Research and Engineering.

## A DATA FORMAT

In Table 5, we illustrate the data format of connection logs extracted with the Zeek utility from PCAP network data. This represents the problem-space format in our setting.

Table 5: Network data format. Our data is represented by connection logs ("conn.log" files) extracted with the Zeek monitoring tool from publicly-available packet-level PCAP files.


In Table 6, we illustrate the statistical feature representation used in this work. The statistical features are aggregated over log connections, which are partitioned by timestamp, internal IP and destination port.

Table 6: Statistical features aggregated over connection logs within each data point grouping. The grouping is comprised of connections within 30-sec time windows, aggregated separately for each internal IP and destination port within the time window. Note that the internal IP versus external IP distinction pertains to the subnet, not to the two ends of the connection (source/destination).


## B SELECTED FEATURES

While the features selected to form the trigger will change according to selection strategy, victim model, and randomness effects, we report in Table 7 the list of 20 most frequently selected features in our experiments on CTU-13 Neris. Since our features are aggregated by internal IP (in addition to time window and port), in the table, "_s_" and "_d_" distinguish between the internal IP being the
source or destination of the connection. "OTHER" is a placeholder for destination ports that are not among the selected 17 ports.

The table highlights the importance of features related to port 25 , which is the port used by the Neris botnet. Commonly selected features for port 25 relate to the number of packets exchanged (pkts_out_sum_s_25), number of connections in state $50^{5}$ (state_S0_s_25), count of distinct external IPs communicating on this port (distinct_external_ips_s_25), and the number of TCP connections (tcp_count_s_25). Features related to the connection state RSTRH $^{6}$ are also common, although often the value assigned is 0 . Since these are count-based features, a value of zero means this state did not occur within the time window.

Table 7: Top 20 most frequently selected features for the experiments on CTU-13 Neris.


## C TRIGGER EXAMPLE

Here, we describe an example of a trigger pattern created with our attack strategy (Section 4). First, the top eight most important features are selected (column 1 in Table 8) using the Entropy feature selection method. Next, we compute value assignments and look for a feature-space prototype, shown in Table 8. Lastly, this prototype is mapped to a set of actual network connections. Table 9 shows a subset of 10 connection events (the entire pattern consists of 54 connections) from the final trigger pattern.

Table 8: Example of a trigger prototype in feature space, showing only the set of selected features. Entropy selection strategy on the CTU-13 Neris data.


## D MODELING THE BYTES DISTRIBUTION

In Figure 7, we present the modeling of two log field values using the Kernel Density Estimation (KDE): responder bytes (left side)
${ }^{5}$ S0: Connection attempt seen, no reply observed by Zeek.
${ }^{6}$ RSTRH: The responder sent a SYN ACK and then a reset, while Zeek did not observe a SYN from the originator.

Table 9: Excerpt of 10 consecutive connection events from a trigger. Due to space constraints, only the relevant fields are shown.


![img-6.jpeg](img-6.jpeg)

Figure 7: Modeling the bytes distribution for responder (left side) and originator (right side): From top to bottom, the figures show: distribution of byte counts per packet, learned KDEs, and sampled data from the learned distributions.
and originator bytes (right bytes). The figure shows the observed distribution of bytes per packet in the adversary's dataset (top row), and the KDEs distribution of these fields learned from the data (middle row), and the distribution of the sampled values (bottom row). Note the similar distribution across the three rows, for each of the two fields, which indicates that the KDE method is able to capture the data distribution well.

## E MUTUAL INFORMATION

We compare the normalized mutual information on a clean dataset (Figure 8a) and on a poisoned dataset (Figure 8b), to show that the field-level relationships are generally preserved. Note that we are interested in maintaining the association patterns, and not the actual coefficient values. The mutual information statistic is used in conjunction with the correlation matrix and domain knowledge to design the direct acyclic graph.
![img-7.jpeg](img-7.jpeg)
(a) Mutual information on clean data, computed on the adversary's dataset.
![img-8.jpeg](img-8.jpeg)
(b) Mutual information on the poisoned training dataset

Figure 8: Mutual information comparison on clean and poisoned data. Showing associations between relevant fields of the conn.log file for CTU-13.