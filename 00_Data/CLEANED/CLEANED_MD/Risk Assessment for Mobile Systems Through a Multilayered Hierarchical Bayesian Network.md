# Risk Assessment for Mobile Systems through a Multi-layered Hierarchical Bayesian Network 

Shancang Li, Theo Tryfonas, Gordon Russell, and Panagiotis Andriotis


#### Abstract

Mobile systems are facing a number of application vulnerabilities that can be combined together and utilized to penetrate systems with devastating impact. When assessing the overall security of a mobile system, it is important to assess the security risks posed by each mobile applications (apps), thus gain a stronger understanding of any vulnerabilities present. This work aims at developing a three-layer framework that assesses the potential risks which apps introduce within the android mobile systems. A Bayesian risk graphical model is proposed to evaluate risk propagation in a layered risk architecture. By integrating static analysis, dynamic analysis, and behavior analysis in a hierarchical framework, the risks and their propagation through each layer are well modelled by the Bayesian risk graph, which can quantitatively analyse risks faced to both apps and mobile systems. The proposed hierarchical Bayesian risk graph model offers a novel way to investigate the security risks in mobile environment and enables users and administrators to evaluate the potential risks. This strategy allows to strengthen both app security as well as the security of the entire system.


Index Terms—Bayesian Risks Graphs, Mobile Security, Risk Assessment, Android Malware;

## I. INTRODUCTION

The Android-based platform has reached the top of the smartphone market, and claimed nearly $79 \%$ of smartphone share in 2013 [1], [2]. In the Google Apps marketplace, more than $1,192,749$ applications (apps) are available and this is increasing by $40 \%$ monthly (i.e. 32,000 in Mar, 2014) [1]. Although Google has released an exciting security tool called the application verification service to protect against harmful Android apps in the market [2], it is still challenging to detect potentially harmful apps before the damage is done. The overall malware detection rate from among 1,260 samples can be as low as $15.32 \%$ even with Google's new application verification service [2], and the overall detection rate utilising its anti-virus tools give an overall detection rates of $20.41 \%$ [3], which is significantly lower than the third part anti-virus apps that range from $51.02 \%-100 \%$ [1]-[4].

Although awareness is constantly rising, the Android-based mobile systems are exposed to strong and significant security

[^0]threats and many issues are reported each day [2], [4]-[8]. The peculiarities of mobile systems have been well known and many approaches have been developed to protect them. In general, a security solution for mobile systems begins with risk assessment to determine the threats and loss expectancy. Many risk assessment models have been proposed to model the risks, attacks, and threats in mobile systems, including attack graphs [5], attack tree [6], Bayesian belief model [9] and hybrid Bayesian network [10]. However many of these models fail to consider the causal-relations of risks, and consequently the contributory causes of threats are ignored [3], [11]-[13].

In [5] and [6], Bayesian networks are used to model vulnerability management and potential attack paths, which make it possible to quantatively evaluate the likelihood that an attack happens. In [10], a Bayesian network model is developed that can calculate the posterior probabilities of states of risks. Assessing the risks of apps or mobile systems is a crucial aspect in determining security state, information protection, and related security controlling. The capability of the Bayesian probabilistic model is a significant motivation to investigate risks analysis by analysing the likelihood of app (or system) compromise by chaining Bayesian rules in the proposed threelayered framework.

In this paper, the term 'risk' is used to denote an unsafe state or behavior of an app or system that is related to vulnerabilities or threats. In mobile systems there are two fundamental risks sources: (1) The apps distribution platform, the Google App Store, might be a source of potential security risks. Users generally always accept all permission requests requested during app installation. This can lead to overprivilege authority in apps and can lead to privacy and security-relevant vulnerabilities; (2) The fragmentation of apps, devices, and OS versions. The existence of multiple versions of Android and the huge number of developers may lead to customised modifications of Android, and these could be riddled with security vulnerabilities.

In mobile systems, security assessment generally involves the risk identification, risk analysis, and risk evaluation for both apps and the underlying system [13], [16]-[19]. This paper aims to develop a risk analysis framework to systematically assess the potential risks present in a mobile system. The hierarchical model decomposes risks in an app (or the system) with inter-dependencies into three layers (static analysis layer, dynamic analysis layer, and behavior analysis layer). Each layer focuses on specific aspects and needs. The framework then combines all specific risks in a coherent way and captures all possible causes of identified risks by applying a Bayesian Risk Graph.


[^0]:    Manuscript received Oct. 08, 2015; revised Nov. 05, 2015; accepted Feb. 20, 2016.

    This work was supported by the ECR2015/2016 funding at Edinburgh Napier University and the European Commission under Grant HOME/2010/ISEC/AG/INT-002.
    S. Li and G. Russell are with Computing, Netowrk, and Security Group, School of Computing, Edinburgh Napier University, Edinburgh, UK. (E-mail: s.li@napier.ac.uk, g. russell@napier.ac.uk. Tel: +44-131-455 2822.)
    T. Tryfonas and is with the Faculty of Engineering, Bristol Cryptography Group, University of Bristol, Bristol BS8 1UB, UK. (E-mail: theo.tryfonas@bristol.ac.uk.)
    P. Andriotis is with the Information Security Group, University College London, WC1E 7JE, UK. (E-mail: mr.panagiotis.andriotis@ieee.org.)

The hierarchical Bayesian risk graph (HBRG) features: (1) A different approach than most existing static analysis, this model integrates the potential risks analysis over: static risk layer, dynamic risk layer, and behavioral risk layer; (2) It can help users to find the dominating risk causes; (3) It is able to determine out-system cause and effects (e.g. for two different mobile systems $A$ and $B$, it can analyse the probability that $B$ will fail if $A$ fails); and (4) Provide risks scores, so that when evaluating the potential risks in a mobile system, the model will grade each application with an app-related risk-score as well as a score for the whole mobile system.

## II. Challenges in Mobile Risks Analysis

In building a secure mobile environment, several key strategic issues should be considered [20]: (1) Develop a risk model that can identify the potential risks of data loss based on a trusted risk assessment; (2) Provide a dynamic risk analysis module, which should be able to keep up with the rapid pace found in the Android ecosystem; (3) Evaluate each app installed using a risk assessment service that assigns them each a risk score. For example, if you install an app with a high-risk score, you should block or disable exploitable resources until the app is removed; (4) Layer the security, so that exploiting a system requires multiple vulnerabilities to penetrate the multiple layers of the security model.

Recently, a number of risk assessment methods have been proposed in the network security domain, such as the probabilistic risk model [6], in-operability input-output models [9], and hierarchical holographic models (HMM) [10]. In general, a complex system can be decomposed with inter-dependencies into several independent views, each of them focuses on different aspects and needs. One such set of views could include: static analysis aspects to model the problem, dynamic analysis to the security planning process, and behavior analysis to the susceptible behaviors analysis for apps. However in the Android mobile systems, the huge number of apps and platform variants makes the risk evaluation difficult, as the probability of each potential risk needs to be considered in security planning. The major challenges in performing an Android risk analysis can be summarized as follows:

1) Security vulnerabilities are rampant. As reported in [21], mobile app security concerns are growing in importance and $96 \%$ of all tested applications have one or more serious security issue, such as privacy ( $90 \%$ ), overprivileges $(80 \%)$, session authentication ( $53 \%$ ), input validation $(62 \%)$, and infrastructure $(66 \%)$. This makes it difficult to find all potential risks when assessing apps and mobile systems [21].
2) Complex mobile attacks. An app might be threatened by a variety of security threats. The attackers could combine these multiple threats to form a complex and powerful mobile attack. The potential mobile threat could be classified into four categories: App-based threats, Network threats, and Physical threats. It is a challenging task to protect apps or mobile systems from a complex multistep and multi-host attack. To deal with complex attacks, it is necessary to perform proactive and consistent app
risk evaluation by both performing efficiently detecting and remediating vulnerabilities across the entire apps ecosystem.
3) The complexity of risk detection. Early detection might be the most efficient way to reduce vulnerabilities but it does not come without without weaknesses. Early detection may use static security analysis tools to identify vulnerabilities created during apps development, such as issues related to embedded information. In fact, most mobile app vulnerabilities relate to run-time activities. Dynamic risks analysis tools are expected to more accurately discover vulnerabilities that only appear when an app is launched. A dynamic analysis process can help in detecting run-time issues. In addition, a behavior analysis aspect to testing could be helpful in identifying potentially harmful long-term activities of apps.
4) Risk communication strategy. Communicating risks is an important challenge to protect apps and mobile systems from threats, allowing incident intelligence to identify risks before they become a focal point for mobile system attacks. In app-based systems, when an app attack happened, it is crucial to be able to predict the possibility that it will occur in other mobile systems, thus help to reduce the spread of similar attacks and the costs incurred. By communicating with developers, vendors, or app stores, the 'out-system risks analysis scheme' can create a roadmap of risk across multiple systems. To address the anticipated risks, users could for instance review the use of a particular app with the knowledge that it has been reported on another platform.
A mature risk assessment model should provide both realtime analysis and risk trend analysis over time for both apps and mobile systems. This paper meets these challenges by capturing vulnerability interdependencies and measuring security in a similar way that real attackers penetrate the mobile system, providing an assessment framework of overall systems risks as well as that related to individual apps.

## III. Mobile Systems Risk Modeling

In risk assessment modelling it is essential to be able to identify what each app is actually doing. A hierarchical risk analysis architecture is able to accurately identify vulnerabilities, while a Bayesian risk graph can capture the interdependencies among the vulnerabilities posed by apps and the mobile systems. In this paper, hierarchical risk analysis is combined with a Bayesian risk graph to accurately model the risk states, propagations, and transitions.

Fig. 1 shows a typical Hierarchical Bayesian Risk Graph (HBRG) model, which integrates a hierarchical risk analysis architecture into a Bayesian risk graph. It consists of a threelayer architecture and each layer extracts featured risks to form a directed acyclic graph (DAG). Each edge between nodes in the graph denotes the probabilistic causal dependencies. Based on the DAG, an Bayesian Network model could be created, in which each node maintains a conditional probabilities table (CPT). The parental nodes in the HBRG are assumed

![img-0.jpeg](img-0.jpeg)

Fig. 1. Hierarchical Bayesian Risk Graph Model

to be marginally independent. The relations in the HBRGs denote the transition probabilities between nodes, which are classified into three aspects: (1) intra-layer relations, which connect the nodes within a layer; (2) inter-layer relations, cover the connections between two adjacent layers, and (3) cross-layer relations, denoting the links which bridge between the behavior layer and static layer. In order to reduce the computation complexity, cross-layer relation can be converted into two inter-layer relations by adding a virtual node concept. In Fig.1, the cross-layer relation from S3 to B3 can be translated into two inter-layer relations, where Da is the newly created virtual node and P(B3|Da) = 1. The virtual node Da can be seen as a copy of node B3 in dynamic layer without needing inter-relations in the dynamic layer. By doing this, the complexity of the relation space could be significantly reduced.

In HBRG, the model parameters (CPTs, transition probabilities) are always estimated using statistical learning algorithms [4], [5], [9]. Statistically, CPTs evaluation requires many samples to test whether a risk can or cannot cause other effect or make a contribution to other risks. Fortunately, the Genome dataset released by the Malware Genome Project [32] have collected more than 1,200 malware app samples that cover the majority of existing Android malware families. This dataset has been successfully used to detect most existing malware apps. In this paper, the Genome dataset is used to statistically learn risk features at the static, dynamic, and behavioral layers to build accurate CPTs.

### A. Bayesian Risks Graph Model

The process that one or more vulnerabilities propagate to one or more different threats could be defined with a dependence graph. The risk states or its propagation are usually constructed as a DAG and the transitions between nodes could be modelled with local conditional probabilities.

A DAG can be modelled with a Bayesian graph model G = {V,E}, in which the nodes V denotes the variables of risks, and the edges E denote relations between nodes that can be described with conditional probability distributions. For each variable S<sup>i</sup> ∈ V, a conditional probability distribution P(S<sup>i</sup>|Pa(S<sup>i</sup>)) is used to describe the transition. Pa(S<sup>i</sup>) denotes the parent set of S<sup>i</sup> in G. The Bayesian model reflects a conditional independence statement, which could significantly reduce the number of parameters needed.

The Bayesian network model needs to be extended to encode the apps risk conditions as a Bayesian Risk Graph (BRG). The BRG is a powerful but intuitive tool for modelling, analysing, and predicting risks in mobile systems. It supports both app and mobile system security risk analysis. A unique joint probability distribution over V, could be verified to be

$$P(S_1, S_2, \dots, S_n) = \prod_{i=1}^{n} P(S_i | \pi_i) \tag{1}$$

where S = {S<sub>1</sub>, S<sub>2</sub>, ..., S<sub>n</sub>} is a set of Bernoulli random variables and P(S<sup>i</sup>|π<sup>i</sup>) denotes the conditional probability of S<sup>i</sup> given the condition of π<sup>i</sup>. For example, for a set S = {S<sub>1</sub>, S<sub>2</sub>, S<sub>3</sub>, S<sub>4</sub>, S<sub>5</sub>}, the joint probability of all the variables can be derived with Eq. (1)

$$P(S_1, S_2, S_3, S_4, S_5) = P(S_1 | S_2) \cdot P(S_2 | S_3, S_4) \cdot P(S_3 | S_4) \cdot P(S_4) \cdot P(S_5) \tag{2}$$

**Definition 1:** Conditional probability table (CPT). In a BRG, the quantitative parameters must be specified. Each node maintains a CPT to describe the conditional probability distribution for a particular combination of values of its parental nodes.

**Definition 2:** Hierarchical Risk Template. A hierarchical-risk-template is a generic property of the structured risk-template that at least includes one of three basic properties:

1. **Behavior Risk**, which includes the potential threats that are based on the behavior analysis;
2. **Dynamic Risk**, which involves potential risks based on the dynamic analysis, such as app activities, network activities, etc.
3. **Static Risk**, which includes the potential risks and threats based on the static analysis, such as malware, size analysis, permission analysis, virus matching, etc.

The hierarchical risk template provides BRG a template that describes the basic potential risks of an app or a mobile

system. It can help us categorize the properties of risks in mobile systems. For example, 'accessing the contact list' is an instance of dynamic risk.

**Definition 3:** *Risk Attribute.* This is a binary attribute representing the state of an instance of a risk. A risk $$S$$ is associated with a state ($$S = 1, true$$) or ($$S = 0, false$$). The probability that risk $$S$$ happens is $$Pr(S = 1)$$. When an app (or system) is compromised it means the risk state of the app (or system) is $$true(S = 1)$$. Therefore

$$Pr(\neg S) = 1 - Pr(S) \tag{3}$$

is the probability of the state being $$S = 0$$.

**Definition 4:** *Atomic Risk.* Atomic risk is a risk that cannot be further broken down into smaller parts and retain their meaning in the context of an risk. Typical example is vulnerability identifiers. Let $$S$$ denote a set of risks. $$\mathcal{A} : S \times S \rightarrow [0, 1]$$ denotes a set of relationships in $$S$$. Then given $$S_{pre}, S_{post} \in S$$, and thus $$a : S_{pre} \mapsto S_{post}$$ can be identified as an atomic risk if

1. $$S_{pre} \neq S_{post}$$
2. given $$S_{pre} = 1$$, $$S_{post} = 1$$ with probability $$\mathcal{A}(S_{pre}, S_{post}) > 0$$
3. $$\nexists S_1, \ldots, S_j \in S - \{S_{pre}, S_{post}\}$$.

Hence, $$\mathcal{A} - S$$ allows an action to compromise the risk $$S_{post}$$ from $$S_{pre}$$ with a nonzero probability. Thus $$S_{pre}$$ is the stage before the risk occurred, and $$S_{post}$$ is the stage after the risk occurred.

**Definition 5:** *Bayesian Risks Graph (BRG).* A BRG is a tuple $$(S, \xi, \mathcal{T})$$, in which $$S = R_B \cup R_D \cup R_S$$ denotes the set of attributes from three risk layers. $$R_B, R_D,$$ and $$R_S$$ denote the risks from the *behavior layer*, the *dynamic layer*, and the *static layer*, respectively.

$$\xi \subseteq S \times S$$ denotes the space of risks. A risk states pair $$(S_{pre}, S_{post}) \in \tau$$ if $$S_{pre} \mapsto S_{post} \in \mathcal{A}$$. Furthermore, for $$S_i \in S$$, the set $$Pa[S_i] = \{S_j \in S | (S_j, S_i) \in \xi\}$$ is called the parent set of $$S_i$$. Here $$\mathcal{T}$$ denotes conditional probability table (CPT).

Fig. 2 shows a simple BRG example, in which the risk $$r_a$$ could be caused by sub-risks $$r_b$$ and (or) $$r_c$$, and iteratively $$r_b$$ could be redivided into $$r_e$$ and $$r_d$$, where $$r_d, r_e,$$ and $$r_c$$ are atomic risks and thus could not be further divided. The basic idea of the BRG is to calculate the probability of $$r_a$$ according to its parental conditional probabilities.

**Definition 6:** *Risks Combination.* For a risk $$S_j$$ in a $$BRG$$, $$S_j \in S_R \cup S_D \cup S_B$$, then assuming that $$S_i \in Pa[S_j]$$ and $$S_i \mapsto S_j$$, then there are two kinds of possibilities to consider for risks combination: AND-combination and OR-combination. As shown in Fig. 3, the AND-combination denotes each sub-risk is a distinct event and the chance of $$r_a$$ to be $$true$$ depends on the success of each individual subrisk ($$r_b$$ and $$r_c$$). For the OR-combination, the chance of $$r_a$$ to be $$true$$ depends on the success of at least one of individual subrisks ($$r_b$$ or $$r_c$$). The probability could be defined as

$$Pr(S_i | Pa[S_i]) = \begin{cases} \operatorname{Pr}(\cap_{S_i = 1}(a_i)), & \text{AND} \\ \operatorname{Pr}(\cup_{S_i = 1}(a_i)), & \text{OR} \end{cases} \tag{4}$$

![img-1.jpeg](img-1.jpeg)

Fig. 2. A simple example of BRG

![img-2.jpeg](img-2.jpeg)

Fig. 3. Risks Combination in BRG

### *B. Hierarchical BRG*

The HBRG is a hierarchical model formed by a three-layer Bayesian risk graph. Fig. 1 shows a typical HBRG model that consists of a BN (Bayesian Network) model at each layer. A risk-evaluation process performs at each layer and a compound risk evaluation will be given for each app (or system).

A HBRG can be represented with a double combination of $$G_{HBRG}$$ and a relationships set $$R$$ as $$< G_{HBRG}, R >$$.

1. $$G_{HBRG} = \{G_S, G_D, G_B\}$$ denotes the BRGs model, in which $$G_S$$ denotes the BRG at the static layer, $$G_D$$ denotes the BRG at the dynamic layer, and $$G_B$$ denotes the BRG at the behavioral layer, respectively. The relationships among random variables at each node are constrained by the model structure and a directed acyclic graph (DAG) obeying the usual conditional independence assumptions. Specifically, the arcs between the BRG nodes represent probabilistic causal dependencies. For each BRG, the joint probability distribution function is defined as in Eq.(1).

2. Relation $$R$$, a key concept of the HBRN model, provides the bridge among the layered BRG. $$R$$ is a set of associations $$\{R_{ij} | (i = 1, 2, \ldots, m) ; j \in (1, 2, \ldots, n)\}$$ with $$R_{ij} = 1$$ implying that node $$S_i$$ is assigned to state $$true$$ of relationship with node $$S_j$$.

## IV. Hierarchical Risk AsSESSMENT With BRGS

The Android security model is primarily based on a sandbox and permissions mechanisms, in which an app is running in a specific Dalvik virtual machine with a unique user ID. In general, each app runs in isolation from all others apps, and so each app cannot access to other app's resources. An app is signed using a certificate by the developer, to confirm the integrity of the app. To conserve resources, apps with the same ID can also arrange to run in the same process, sharing the same VM. Apps can be granted permissions, and these are displayed to the user for approval before the app is installed. However, users tend to ignore the permissions that an app requests, and there are many reasons for this to happen [22][25].

Forensically, the risk detection, finding, and evaluation are important for providing users a safe mobile platform. The hierarchical risk assessment framework is able to conduct three layers of in-depth risk analysis for both apps and mobile systems.

## A. Static Risk Analysis

A number of static risk analysis methods have been developed to examine the potential risks that an app can exhibit [1], [2], [26]. However, most of them are constrained to certain performance capabilities due to their inherent limitation of not actually executing the code. In Android systems, the static analysis is mainly focused on disassembling the binary file (APK) to check source code (e.g. classes.dex, smali, AndroidManifest.xml). This permits the static risk analysis to scan an app's permission requests, API calls, and check discrepancies between the two, including the following stages: (1) app-decompile into smali format; (2) information extractor; (3) API calls parse; (4) permission analysis; (5) grouping of critical API calls; (6) embedded sources; (7) log monitor and parser. Commonly used analysis tools have been developed, such as apktool, baksmali, fivalk, and icat [25].

The static analysis can also provide insights into the third part software development kits (SDKs), libraries, API calls, and app functions that are employed within an app. Most of the existing mobile security schemes are using static risk analysis to identify malicious apps [1], [2], [26]. For example, in [27] Zhou and Jiang found that the BOOT_COMPLETED event registration was used in over $83 \%$ of the malware apps sample dataset, and given the assumption that this event registration would occur less frequently in legitimate applications it thus could be used as an indicator for identifying malicious applications. The limitation of static analysis code mapping is that unable to effectively evaluate any permissions abuse which may occur in the Android system. It also cannot cover dynamic and forgery bytecode calls that can generate false negative in terms of permissions requested [28].

The main goal of static analysis is to statistically find ways to trigger potentially malicious or risky behaviors before the app runs. Using static risk analysis, one can identify main static risks in an app. The output of static analysis could be used to guide the dynamic analysis, or even help parametrise the dynamic analysis directly. This can significantly reduce
the parameters needed when performing dynamic analysis and thus improve its performance.

## B. Dynamic Risk Analysis

After completing the static analysis stage, the framework performs a real-time analysis, which evaluates apps under run-time conditions on instrumented emulators or modified hardware devices. The dynamic analysis module could run over a server and perform concrete execution of apps while extracting certain details related with security. The analysis includes the execution of Dalvik bytecode and contains data structures related to a single execution flow through an app, while other methods also contain a stack to temporarily retain data about each method that is called at run time. As the execution encounters method calls and returns, this stack grows and shrinks. In this layer, the framework mainly focuses on detecting the following risks and exploits:
(1) Intent-based risks. Each app is composed of several components (Activity, Service, Broadcast Receiver, Content Provider) that can communicate between each other using Intent message (for both inter and intra app communication). However, wrong information exchange between activities could leak information. The Intentbased risks include: Unauthorized Intent Receipt, Broadcast Theft, Activity Hijacking, Service Hijacking, and Special Intent.
(2) Intent Spoofing. Malicious apps are able to launch an Intent spoofing attack by sending an Intent to an exported component that is not expecting Intents from that app. This kind of risks include malicious broadcast injection and malicious activity/service launch.
(3) Component Analysis. The main goal of this component is to check susceptible risks for each components in an app by examing the app's manifest file, Dalvik instructions, etc.
(4) Android network sniffing. It includes detection of risky network activities, such as networking vulnerability scanning/search, illegal login, http POST/GET, https hijacking, etc.

In dynamic risks analysis, a number of tools have been developed such as ComDroid [29], DroidMOSS [30], and Paranoid [31]. The output of this layer includes: (1) components analysis, (2) inter-app communication, (3) network connection analysis, (4) method call graph, (5) control flow graph, and (6) a list of relevant in-app behaviors, includes execution of binaries, execution of commands, network events detection, loading of libraries, I/O accessed, and dynamic class-loading. These outputs can be used to determine vulnerabilities or guide further behavior risk analysis.

These results could easily be modified to search for and record any functionality or behavior deemed of interest. Dynamic analysis could check the proactive risks, such as autoupdating, auto-downloading, and repacking.

## C. Behavior Risk Analysis

The behavior layer identifies risk behaviors and measures an app's actual activity over time. By leveraging the risks found in the static, dynamic, and behavior layers, the framework can discover hidden, risky behaviors within a mobile app or

system. It can then combine all risks to provide an overall risk score, and thus create custom mobile policy. The main goal in this layer is to identify risk behaviors that might bring risks to an app or the mobile system. This process collects both security and privacy information on how an app performs its potentially risky run-time activities. Typical tests in this layer include:

- Auto exercises apps at run-time. Each app is auto-loaded into a propriety emulator designed to test each app as it would run in its native environment.
- Perform credential auto-login. This test replicates login activity by auto-loading necessary credentials for full execution of the app's functionality. This ensures that HBRG can test all aspects of the app's functionalities beyond the login screen.
- Collect network activity for both SSL and non-SSL activities. Tests designed to monitor any network activity, essentially to see if the app is accessing any third party networks. By doing this, one can at a minumum identify whether such traffic was properly encrypted or not.
- Determine if app launches other apps during run-time. This security test checks to see if an app sends requests to access/launch other apps during run-time which may allow malicious or risky activity to occur. This type of exposure may allow malicious apps to be 'silently' installed on the user's devices as well as giving them the ability to auto-execute apps with malicious intent.
- Monitor read/write access to device directory and hardware. This test monitors access to device hardware (i.e. the camera) and also monitors which system files the app can access and how encryption is used for saving information.
- Abnormal behaviors detection. This could be undertaken by checking for abnormal behaviors, such as privacy collections, regularly information uploading, using HTTP POST methods, receiving commands, etc.
The typically behavioral analysis methods used in this layer include (1) Machine learning classifier: based on previous training experience and after testing and weighing the security issue, the classifier decided the potential risks that a behavior may bring; and (2) Feature selection: the risky features selection methods are applied for behavior datasets. The behavioral analysis is an effective solution to use characteristic and behavioral-based methods to detect malware by observing the static and/or dynamic behavior and features of mobile systems.


## D. Risk Score

The causal risks could be a compound of a set of subrisks produced by the joint effect of other risks. By using the Bayesian theorem, a numerical analysis can be performed to find the probability for each causal-risk. By refining the CPTs, the HBRG can determine (i) the probability that an attack occurred on an app (or system), (ii) the probability that an app (or system) will fail.

Given the risk values for each app (or system), a weighted risk score for each app (or system) can be easily calculated

$$
R_{S}^{w}=w P(S),\left(R_{S}^{w}\right) \in[0,3]
$$

in which $P(S) \in[0,1]$. An app may be threatened by multiple risks, and each risk may lead an individual threat. In this case, the risk level can be calculated with weighted probabilities of each risk [5]. The Risk_Scores are classified into three categories: Low : $[0.0-1.0)$, Medium : $[1.0-2.0)$, and Severe : $[2.0-3.0]$.

## E. Contributory Causes Tracking

1) Independent Contributory Causes Tracking: Forensically, when a risk occur, it is important to find all contributory causes or the probability of causes that make it happened. Assume $\mathbf{s}=\left\{s_{1}, s_{2}, \ldots, s_{k}\right\}$ denotes a group of contributory causes of an attack. Thus

$$
p(\mathbf{s} \mid a)=\sum_{i=1}^{N_{s}} \alpha_{k}(i)
$$

in which $N_{s}$ denotes the number of nodes that cause the attack $a$; the $\alpha_{k} \mathrm{~s}$ are the forward variables. Using the likelihood ratio:

$$
\begin{aligned}
P(a \mid \mathbf{s}) & =\frac{P(\mathbf{s} \mid a) P(a)}{P(\mathbf{s})} \\
& =\frac{P(\mathbf{s} \mid a) P(a)}{P(\mathbf{s} \mid a) P(a)+P(\mathbf{s} \mid \bar{a}) P(\bar{a})}
\end{aligned}
$$

where $P(a)$ represents the prior probability of $a$. The posterior probability is the node's belief on the existences of $\mathbf{s}$ based on the observation of $a$. It is the probability of causes that allowed the attack to happen. For each cause in $\mathbf{s}$, it is possible to calculate the probability that contributed to $a$.

$$
P\left(s_{i} \mid a\right)=\frac{P(\mathbf{s} \mid a) P(a)}{P(\mathbf{s})}=\frac{P(\mathbf{s} \mid a) P(a)}{P(\mathbf{s} \mid a) P(a)+P(\mathbf{s} \mid \bar{a}) P(\bar{a})}
$$

2) Multiple Contributory Causes Tracking: If an attack happened, the probability of any individual risk could be calculated by applying above approach. Similarly, the model is able to calculate the probability of any individual risk group assumed to cause the attack. The group causes tracking method enables the identification of the group causes of an attack after it happened.

$$
\begin{aligned}
P\left(a_{1} \mid \mathbf{s}\right) & =P\left(a_{1} \bar{a}_{2} \mid \mathbf{s}\right)+P\left(a_{1} a_{2} \mid \mathbf{s}\right) \\
P\left(a_{2} \mid \mathbf{s}\right) & =P\left(\bar{a}_{1} a_{2} \mid \mathbf{s}\right)+P\left(a_{1} a_{2} \mid \mathbf{s}\right)
\end{aligned}
$$

Then, we have

$$
P\left(a_{1} a_{2} \mid \mathbf{s}\right)=\frac{P\left(\mathbf{s} \mid a_{1} a_{2}\right) P\left(a_{1} a_{2}\right)}{P(\mathbf{s})}
$$

in which,

$$
\begin{aligned}
P(\mathbf{s})= & P\left(\mathbf{s} \mid a_{1} a_{2}\right) P\left(a_{1}\right) P\left(a_{2}\right)+P\left(\mathbf{s} \mid a_{1} \bar{a}_{2} P\left(a_{1}\right) p\left(\bar{a}_{2}\right)\right. \\
& +P\left(\mathbf{s} \mid \bar{a}_{1} \bar{a}_{2}\right) P\left(\bar{a}_{1}\right) P\left(\bar{a}_{2}\right) \\
= & P\left(\mathbf{s} \mid a_{1} a_{2}\right) P\left(a_{1}\right) P\left(a_{2}\right)+P\left(\mathbf{s} \mid a_{1} \bar{a}_{2} P\left(a_{1}\right) p\left(\bar{a}_{2}\right)\right.
\end{aligned}
$$

## F. Determining out-system causal effects

An app could be installed by many users. When an app has failed (or been compromised) on a mobile system, it is important to predict the possibility that the same app will fail (or will be compromised) on other mobile systems. In

fact, the observation that an app failed could increase the possibility that an attack will occur on other systems. This prediction could be helpful for refining the CPTs for other systems. Accordingly, for two mobile system $\mathbf{S}_{1}$ and $\mathbf{S}_{2}$,

$$
P\left(\mathbf{S}_{2}\right)=P\left(\mathbf{S}_{1} \cap \mathbf{S}_{2}\right)+P\left(\overline{\mathbf{S}}_{1} \cap \overline{\mathbf{S}}_{2}\right)
$$

we further have

$$
\begin{aligned}
P\left(\mathbf{S}_{2}\right) & =P\left(\mathbf{S}_{1} \cap \mathbf{S}_{2}\right)+P\left(\overline{\mathbf{S}}_{1} \cap \mathbf{S}_{2}\right) \\
& =P\left(\mathbf{S}_{2} \mid \mathbf{S}_{1}\right) P(\mathbf{S} 1)+P\left(\mathbf{S}_{2} \mid \overline{\mathbf{S}}_{1}\right) P\left(\overline{\mathbf{S}}_{1}\right)
\end{aligned}
$$

Hence, when an app fails on a mobile system, it implies the increase of the probability that the app will fail if it is installed on other mobile systems. Similarly, when an attack happened on a mobile system, the probability that an attack with same contributory causes will happen on other systems will also increase.

## V. Risks Analysis with HBRG - A Case Study

As discussed in above sections, the HBRG model is able to analyse risks associated with apps or mobile system by integrating the static analysis, dynamic analysis, and behavior analysis into a Bayesian risk graph. One possible real-world risk is that posed by the Fake app patch, which is an issue which can be found in the Android environment.

For instance, Google published an app 'Android Market Security (AMS)' to undo the side effects caused by Android. Rootcager is a Trojan horse that steals information from Android device. This app was automatically pushed to devices of users who had downloaded and installed an infected app. However, a repackaged version of AMS was found on third party app markets, and for discussion purposes the authors name it rAMS. The rAMS might threaten the users' privacy information and may cause other issues. As an example, HBRG was used to analyse rAMS to demonstrate how HBRG can be used in a risk analysis.

In risks evaluation of an app or system, the statistically learned CPTs require many samples to test whether one can or cannot cause other effect or make contribution on other risks. To characterise existing Android risky malware, particularly within static and dynamic analysis, most known risky features can be collected and classified that cover the majority of existing Android malware families. This helps to build a risks library for efficient evaluation of mobile security. Fortunately, the Malware Genome Project has collected more than 12,000 malware samples that cover the majority of existing Android malware families. It has been successfully used to detect most existing malware apps. In this paper, CPTs have been evaluated based on statistic results with the reported harmful features of apps.

TABLE I
Static Analysis (SIZE)


In static analysis layer, the following features are first checked: (1) Size, (2) Permission requested by AMS and
rAMS, (3) Package structure. This is shown in Table. I and Table. II. The size of rAMS is bigger than that of AMS, which might be caused by repacking risks. It can be identified that the requested permissions are different and the rAMS requests extra permissions that could bring risks to the app and system. After checking the package structure, it is found that the structure for AMS and rAMS are different. AMS includes a 'google.android' package that contains three sub-packages googleapps and googlelogin, however in rAMS, the google.android package was obviously repackaged as mss.bg, which includes three new packages: transaction, ui, util. The eighteen potential static risks in rAMS are analysed in Fig.4, which involves permissions, internet accessing, storage, and privacy, which are organized as 18 BRG nodes from $S 1$ to $S 18$ as shown in Fig.5. All risks combinations in this example are assumed to be OR-combinations for simplicity.

TABLE II
Static Analysis (Permissions)


In the dynamic layer, further analysis of the dynamic risks can be carried out. By de-assembling the app it was found that the rAMS is collecting the following information: \{imei, version, smscentre, handled, pid, install time, sysversion, author, fare, and phonenumber\}. The collected information was saved in a hidden file upload.xml.

In the dynamic layer, it was found that the rAMS used the HTTP POST method and the related URI was identified as http://www.youlubg.com:82/Coop/request3.php. This means that the rAMS was able to send the collected information onwards to a remote server. Based on the analysis at static layer, the following potential risks were identified: repacking, sending SMS, receiving SMS, http post, http get, block sms, which are organized as BRG nodes $D 1$ to $D 7$. Two virtual nodes $D a$ and $D b$ are created and mapped to $B 3$ and $B 4$, respectively.

Similarly, at the behavior layer, behavioral risks could be identified based on matching with the behavioral risk lib. It is found that the rAMS is able to interact with the above identified server. By further checking the network activities of rAMS, it was found that the rAMS could receive commands from the reply generated by the POST request and save the commands into a hidden file serverinfo.xml. This identified a risk that the remote attackers are able to send SMS messages from the compromised device. rAMS also has the capability to block incoming SMS messages. Based on the behavior features extracted from Genome Project, four behavior risks are recognized from rAMS: B1: Costs; B2:

Regularly connect third part Server; B3: Collecting Privacy Data; B4: System Leakage as shown in Fig.4.

A HBRG could be built as shown in Fig.5, in which the blue edges denote the Intra-relations and the red edges denote Inter-relations. Two virtual nodes, $D a$ and $D b$, are created to reduce the relation space. Then is trivial to transform the HBRG model to a BN model, where the probabilities and CPTs are pre-specified according to the statistical learning data. Fig.6 (a) shows the risk analysis at the static layer for rAMS, in which the joint probabilities are shown in the table. As an example, Fig.6 (b) shows the CPT maintained by node 'LOG_PRV'. For rAMS, the static layer analysis shows there is only a $25.7 \%$ chance of rAMS at risk.

TABLE III
RISK ANALYSIS FOR RÁMS USING HBRG


Similarly, based on HBRG, the app probability that rAMS is in risk was found to be $88.5 \%$ at dynamic layer and $46 \%$ at behavior layer. Fig. 7 shows the overall risk of rAMS is $77.7 \%$ and the risk score is $2.325(\in[2.0-3.0])$, which means rAMS is considered to be at the severe risk level.

In practice, if a risk occurred, it is possible to analyse the possible contributory causes and determine out-system causal effects as discussed in above sections.

## VI. SUMMARY and Future Work

This paper proposed a HBRG model as a risk evaluation framework in Android mobile systems. The HBRG can provide users with a friendly risk evaluation framework, which is able to show users where the potential causes of risks
exist. It will lead users to select apps with lower risk and help to know how secure their apps or systems are. It is also possible that this model will allow people to well understand the potential risks in their system and create an incentive for developer to create lower-risk apps that do not contain invasive ad networks and avoid over-requesting permissions. This study is not the last word on the question of how to best present risk information, but future work will continue to investigate hidden risk mitigation and propagation in Android systems.

![img-3.jpeg](img-3.jpeg)

Fig. 4. Risks analysis for rAMS using HBRG

![img-4.jpeg](img-4.jpeg)

Fig. 5. HBRG model for rAMS

![img-5.jpeg](img-5.jpeg)
(a) Risks analysis at Static Layer for rAMS

![img-6.jpeg](img-6.jpeg)

Fig. 6. Risks analysis on Static Layer for rAMS

![img-7.jpeg](img-7.jpeg)

Fig. 7. Risks analysis on Static Layer for rAMS
