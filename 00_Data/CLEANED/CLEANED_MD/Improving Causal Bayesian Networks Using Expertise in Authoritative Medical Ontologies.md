# Improving Causal Bayesian Networks Using Expertise in Authoritative Medical Ontologies 

HENGYI HU and LARRY KERSCHBERG, George Mason University

Discovering causal relationships among symptoms is a topical issue in the analysis of observational patient datasets. A Causal Bayesian Network (CBN) is a popular analytical framework for causal inference. While there are many methods and algorithms capable of learning a Bayesian network, they are reliant on the complexity and thoroughness of the algorithm and do not consider prior expertise from authoritative sources. This article proposes a novel method of extracting prior causal knowledge contained in Authoritative Medical Ontologies (AMOs) and using this prior knowledge to orient arcs in a CBN learned from observational patient data. Since AMOs are robust biomedical ontologies containing the collective knowledge of the experts who created them, utilizing the ordering information contained within them produces improved CBNs that provide additional insight into the disease domain.

To demonstrate our method, we obtained prior causal ordering information among symptoms from three AMOs: (1) the Medical Dictionary for Regulatory Activities Terminology (MedDRA), (2) the International Classification of Diseases Version 10 Clinical Modification (ICD-10-CM), and (3) Systematized Nomenclature of Medicine Clinical Terms (SNOMED CT). The prior ontological knowledge from these three AMOs is then used to orient arcs in a series of CBNs learned from the National Institutes of Mental Health study on Sequenced Treatment Alternatives to Relieve Depression (STAR*D) patient dataset using the Max-Min Hill-Climbing (MMHC) algorithm. Six distinct CBNs are generated using MMHC: an unmodified baseline model using only the algorithm, three CBNs oriented with ordered-variable pairs from MedDRA, ICD-10-CM, and SNOMED CT, and two more with ordered pairs from a combination of these AMOs. The resulting CBNs modified using ordered-variable pairs significantly change the structure of the network. The agreement between the Modified networks and the Baseline ranges from $50 \%$ to $90 \%$. A modified network using ordering information from all ontologies obtained an agreement of $50 \%$ ( 10 out of 20 arcs exist in both the Baseline and Modified models) while maintaining comparable predictive accuracy. This indicates that the Modified CBN reflects the causal claims in the AMOs and agrees with both the AMOs and the observational STAR*D dataset. Furthermore, the Modified models discovered new potentially causal relationships among symptoms in the model, while eliminating weaker edges in a qualitative analysis of the significance of these relationships in existing epidemiological research.

CCS Concepts: $\cdot$ Theory of computation $\rightarrow$ Bayesian analysis $\cdot$ Applied computing $\rightarrow$ Health informatics $\cdot$ Mathematics of computing $\rightarrow$ Causal networks;

Additional Key Words and Phrases: Patient data, data mining, data management, Bayesian networks, causal inference, causal networks, causality, healthcare data, healthcare information technology, ontology, ontology evolution

## ACM Reference format:

Hengyi Hu and Larry Kerschberg. 2023. Improving Causal Bayesian Networks Using Expertise in Authoritative Medical Ontologies. ACM Trans. Comput. Healthcare 4, 4, Article 20 (October 2023), 32 pages.
https://doi.org/10.1145/3604561

[^0]
[^0]:    Authors' address: H. Hu and L. Kerschberg, George Mason University, 4400 University Drive MSN 4A5, Fairfax, VA 22030 USA; emails: [hhu2, kerschj@gmu.edu.
    Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specific permission and/or a fee. Request permissions from permissions@acm.org.
    (c) 2023 Copyright held by the owner/author(s). Publication rights licensed to ACM.
    2637-8051/2023/10-ART20 15.00
    https://doi.org/10.1145/3604561

# 1 INTRODUCTION 

### 1.1 Causal Inference and Causal Bayesian Networks

Inferring causation from data is a technique dating back to the 1980s [68]. Recently, there has been significant focus on collecting patient data [93], including observational data from patients with multiple symptoms and their interaction with treatments. Datasets collected from electronic health records and by crowdsourced methods have enabled a plethora of statistical studies aimed at predicting risk, disease prognosis, and treatment effectiveness. However, statistics alone cannot measure: (1) causes and effects and (2) how or why causes influence their effects [70]. In the proposed research, we adopt Judea Pearl's definition of causation, as listed in Reference [70]:

- Variable X is a cause of variable Y if Y in any way relies on X for its value.
- Variable X is a direct cause of variable Y if X appears in a function that assigns values to Y .

Clinicians and data scientists often ask semantic questions of the data related to uncertainty. These semantic questions are usually of a causal nature. For example, the question "what are the causes of depression" requires a causal model exploring causal relationships [23]. To explore causal relationships, we need: (1) a method to articulate causal assumptions, (2) a way to link structures of causal models to data, and (3) a method to draw conclusions based on causal assumptions in a model and in the data.

In 1998, Judea Pearl described how causal relationships can be inferred from cross-sectional data if certain assumptions are made regarding the underlying process of data generation [67]. For example, if the data variables are observed to be in a linear sequence, then we can assume that a variable $X$ preceding another within that sequence is a causal indicator of the second variable $Y$. The causal indicator $X$, in this case, has the potential of being a cause of $Y$, or at least assigning a value to $Y$.

The desire to infer causal relationships from structures such as a directed acyclic graph (DAG) has led to the creation of different inference models. Causal graphs generated from data can capture the probabilistic and causal properties of multivariate distributions [27]. These graphs capture a joint probability distribution using a graphical representation, which is used to visualize conditional dependence [68].

ADAG capable of capturing probabilistic relationships among random variables is a Bayesian Network (BN). A BN is a popular framework for causal inference and decision making. BNs are a class of graphical models composed by a set of random variables $X=\left\{X_{i}, i=1, \ldots, n\right\}$ and a DAG, denoted $G=(V, A)$, where $V$ is the set of nodes and $A$ is the set of arcs $[51,69]$. The probability distribution of $X$ is called the global distribution of the data, while those associated with individual $X_{i}$ are called local distributions. Each node in $V$ represents one variable in the data, and they are referred to interchangeably. The directed arcs in $A$ that connect nodes in $V$ are denoted as " $\rightarrow$ " and represent direct stochastic dependencies between nodes. If there is no arc connecting two nodes, then the corresponding variables are either marginally independent or conditionally independent, given a subset of the rest of the variables.

As a result, each local distribution depends only on a single node $X_{i}$ and on its parents, and $P(X)=$ $\prod_{i=1}^{n}\left(P\left(X_{i} \mid \prod X i\right)\right)$. From a Bayesian perspective, given a Bayesian Network $B=\left(G, X_{i}\right)$ and a dataset $D$, we can compute the posterior probability $P(B \mid D)=P(G, \theta \mid D) \propto P(G \mid D) * P(\theta \mid G, D)$, where $P(G \mid D)$ is the learning of the BN structure, and $P(\theta \mid G, D)$ is the learning of the BN parameters.

Fitting a BN to the data (learning) consists of two main steps [28]: (1) Structure learning: a single DAG structure is discovered which best fits the data according to a specific algorithm used; and (2) Parameter learning: determining the probability distributions of arcs $A$ among nodes $V$ in the DAG.

To determine the structure of a network based on data, conditional independence tests are used. Conditional independence is a key concept in Bayesian networks [67] due to factorizations of joint probability distributions. Given a variable set $V$, two random variables $X, Y$ are conditionally independent given $Z$, or $(X \perp Y \mid Z)$ if:

$$
\forall x, y, z: P(X=x \mid Y=y, Z=z)=P(X=x \mid Z=z), \text { provided that } \forall z: P(Z=z)>0
$$

![img-0.jpeg](img-0.jpeg)

Fig. 1. Inferring causality from an ordered variable pair.
Since conditional independence is a concept based on traditional statistical independence, if two variables ( X , Y) are independent, then the joint distribution is the product of the marginals:

$$
P(X=x, Y=y)=P(X=x) P(Y=y)
$$

If the two variables $(X, Y)$ are dependent given conditioning on $Z$, then:

$$
P(X=x, Y=y \mid Z=z)=P(X=x \mid Z=z) P(Y=y \mid Z=z)
$$

When a BN is used to infer causality and combined with known causal probability distributions between pairs of nodes, it produces a Causal Bayesian Network (CBN). CBNs are extensions of BNs in which causal links are represented as conditional probabilities between nodes [21, 94]. Within a CBN, edges have straightforward and intuitive interpretations. For example, a directed edge $X \rightarrow Y$ indicates a single causal relationship between a pair of variables, from variable $X$ to variable $Y$.

Causal models that are used to infer causality are limited by the interpretation of data. For example, a directed edge $X \rightarrow Y$ may denote a correlation (BN) or a causal relationship (CBN). In a BN, variables $X$ and $Y$ may have a dependency but not a direct causal effect. For example, consider the following relationship:

Eye color $X$ and hair color $Y$ may have dependency and correlation in a dataset, but one does not necessarily cause the other to occur even though a directed edge may exist between the two nodes. Eye color is a causal indicator of hair color, and we can choose to infer causality (i.e., assume that eye color determines hair color) and substantiate this with a likelihood statistic. However, in this case it is the MC1R gene ${ }^{1}$ that directly causes the pigmentation of hair color. Eye color may be a variable used to infer causation according to a model, e.g., "brown eyes likely cause brown hair," even when eye color does not directly cause an individual to have a specific hair color. Thus, by combining causally inferred knowledge with scientific fact, one can mitigate incorrect inferences.

# 1.2 Algorithms to Generate a Causal Bayesian Network (CBN) 

The first step in generating a BN is structure learning, which consists of an algorithm that generates a DAG that best represents the conditional independencies present in the data. This has been discussed in the literature using constraint-based, score-based, and hybrid algorithms [51, 79].

The second step is parameter learning. Parameters of the BN are calculated based on available data and by assigning joint densities to the edges between nodes of the DAG. A single edge is a conditional density based on parameters that are estimated using Bayesian estimation techniques (minimize loss or maximize utility in the posterior) and regularized maximum likelihood [21].

Since the 1980s, three approaches have emerged as viable methods for causal learning: (1) constraint-based, (2) score-based, and (3) hybrid. Constraint-based approaches search the data for conditional independence between variables and attempt to find a DAG that captures the corresponding d-separations [78]. In score-based methods, Bayesian approaches attempt to find a DAG that maximizes the likelihood of the posterior given a prior dataset $[56,60]$. A third hybrid approach combines both approaches.

These algorithms share common assumptions, including: (1) a correspondence between nodes $V$ and random variables $X$ (two nodes cannot correspond to a single variable), (2) arcs between variables represent conditional

[^0]
[^0]:    ${ }^{1}$ https://ghr.nlm.nih.gov/gene/MC1R.

dependencies, (3) all possible combinations of $X$ are valid events, and (4) observations from $X$ are independent and identically distributed (i.i.d.), because a sequence or collection of random variables is i.i.d. [3]. We now explore several established approaches that mitigate the difficulty of learning a CBN.

Constraint-based algorithms are based on the seminal work of Pearl on causal graphical models and his Inductive Causation (IC) algorithm [89], which provides a framework for learning the DAG of a BN using conditional independence tests under the assumption that graphical separation and probabilistic independence imply each other (the faithfulness assumption). All constraint-based structure learning algorithms share a common threephase approach inherited from the IC algorithm. This can be summarized as: (1) optional learning of Markov Blankets, (2) learning neighboring nodes (e.g., parents and children), and (3) network construction and learning arc directions [78].

Score-based learning algorithms use heuristic optimization techniques. A candidate DAG is generated then scored based on how well they fit the data. A typical method for constructing a DAG is to acquire Bayesian posteriors from a set of priors. In this method, the posterior probability of the DAG given the dataset is calculated using Bayes' rule where the score of the DAG given the data:

$$
\mathrm{p}(D A G \mid D a t a)=\frac{\mathrm{p}(D a t a \mid D A G) * \mathrm{p}(D A G)}{\mathrm{p}(D a t a)}
$$

Examples of score-based learning algorithms include: efficient caching using decomposable scores [20], parallel meta-heuristics [72], and integer programming [9]. Hybrid algorithms use both conditional independence tests and network scores; the former to reduce the space of candidate DAGs and the latter to identify the optimal DAG among them. Some examples are Parent-Children (PC) [83], Grow-Shrink (GS) [34, 51], Incremental Association (IAMB) [87], Max-Min Hill-Climbing (MMHC) [76, 88], and Max-Min Parents \& Children (MMPC) [88].

# 1.3 Orienting Arcs in a CBN 

The algorithms discussed in the previous section determine the structure of the network, the direction of the arcs within the structure, and the conditional probabilities of arcs between nodes. When a CBN is used to infer causality, the arc direction between two nodes can specify a causal relationship within the BN where one node is the cause and the other is the effect.

Recent research has shown that the fit and accuracy of score-based methods improve noticeably with prior time-based sequencing information [2, 8, 21, 54]. This is done by obtaining a prior time-based sequence of symptoms from the data, then altering the algorithm used to generate the CBN based on the sequence. For example, if the patient dataset contains demographic variables such as a person's race, ethnicity, gender, and so on, then the demographic variables will precede any symptom variables obtained as a part of data collection. Having prior knowledge of a temporal sequence of events among variables, the algorithm used to generate the CBN can be modified to blacklist directed arcs, which can be interpreted as "anxiety is a symptom which causes ethnicity." However, we do know that the reverse statement can be true and that ethnicity can be used to predict certain diseases and symptoms [52].

One of the unique challenges of orienting arcs within a CBN is obtaining a prior sequence or ordering among the symptom variables. There are several methods of reliably obtaining prior knowledge to assist in orienting arcs within a CBN. They can be categorized into three groups:

- Time-based, longitudinal sequencing of variables. This is the most intuitive method where the diagnosis of each symptom variable has a recorded time period, timestamp, or some other time-based sequence [49]. This method is very common in epidemiology, where the progression of a disease happens in a sequence over time [54].
- Logical ordering of variables. This method requires logical analysis and ordering of cross-sectional data variables where time-based sequencing is not available. Ordering can be intuitive, e.g., symptom pro-

gression based on age [35], or it can be logical. For example, symptoms variables precede treatments, but other demographic variables, such as race, ethnicity, gender, and so on, precede symptoms.

- Other data-based methods. These methods establish temporal sequencing or logical ordering based on the data and include collider testing [86], human perception of causal strength [73], and Error Reduction [31]. A patient's age can also be used determine the sequence of events [53].

Once a prior orientation of potentially causal relationships is established, it can be used to significantly improve conditional probabilities within a causal network learned from data by up to 20\% [2]. However, this depends on the accuracy of the prior orientation and the available data.

This article proposes a novel method of obtaining ordered variable pairs from ontological subsumption hierarchies and indexed terminologies in one or more Authoritative Medical Ontologies (AMOs). Ordered variable pairs from an AMO contains prior knowledge that can then be used to orient the arcs/edges in a CBN. This "ordering" of symptoms using an ontology is similar to using time-based sequencing to orient a CBN but is not temporal.

Finally, orienting arcs occur after the baseline network has been established. This is a data-driven methodology, which contrasts with existing methodologies to create CBNs directly from ontologies [10, 43, 61] instead of data.

# 1.4 Authoritative Medical Ontologies (AMOs): MedDRA, ICD-10-CM, and SNOMED CT 

An ontology is commonly defined as a "specification of a conceptualization" in the context of knowledge and data sharing [70]. Information stored in modern ontologies are repositories for specific application domains, such as healthcare. Ontologies enable sharing and reuse of knowledge within a domain and make those assumptions explicit. Originally, ontologies were created to share common understanding of the structure of information among users and software agents [32]. The basic components of ontologies are:

- Classes - description of concepts within a domain;
- Properties - description of features and attributes of classes/concepts;
- Taxonomic hierarchy - a class-subclass hierarchy where classes are arranged according to subsumption; and
- Instances - specific examples of objects within classes.

Together, these components are used to specify knowledge and terminologies within a specific domain (e.g., the Gene Ontology describes gene function). In the past decade, large ontological repositories have been created to standardize medical informatics and disease domains. These large "authoritative" medical ontologies (AMO) are formal ontologies that are developed by experts as a reference for standardized medical terminology. Typically, a governing board or regulatory committee of clinicians and experts continuously maintain authoritative ontologies. The goal of a medical ontology is to standardize terminology, sometimes across several languages, which can then be used to enable communication.

AMOs contain lexicons used throughout the healthcare industry for patient diagnoses, medical research, regulation policies, and product development. Examples of AMOs include the Gene Ontology, NCI Thesaurus, SNOMED CT, ICD-10-CM, and MedDRA. These ontologies provide a method of standardizing domain knowledge in a variety of different but related biomedical fields. Currently, there are multiple ontologies being created and curated to meet the growing needs of personalized healthcare. A variety of them can be accessed via the NCBO BioPortal. ${ }^{2}$ This article utilizes three AMOs: (1) MedDRA (Medical Dictionary for Regulatory Activities Terminology), ${ }^{3}$ (2) ICD-10-CM (International Classification of Diseases, Tenth Revision, Clinical Modification), ${ }^{4}$ and (3) SNOMED CT (Systemized Nomenclature of Medicine - Clinical Terms). ${ }^{5}$

[^0]
[^0]:    ${ }^{2}$ https://bioportal.bioontology.org/.
    ${ }^{3}$ https://www.meddra.org/.
    ${ }^{4}$ https://www.cdc.gov/nchs/icd/icd10cm.htm.
    ${ }^{5} \mathrm{https}: / /$ www.snomed.org/.

MedDRA is currently managed by a board of over 20 healthcare professionals and hundreds of experts in the user community. The ontology itself contains over 72,000 classes as of October 2019. The repository grows as medical knowledge grows, and the ontology is evolved collaboratively as new research is incorporated [10, 95]. MedDRA is used to translate regulatory information for medical products, including pharmaceuticals, vaccines, and devices.

ICD-10-CM is a system used by physicians and other healthcare providers to classify and code all diagnoses, symptoms, and procedures recorded in conjunction with hospital care in the United States. ICD-10-CM is based on the International Classification of Diseases 10th revision (ICD-10) published by the World Health Organization. ICD-10-CM uses unique alphanumeric codes to categorize diseases and symptoms. Clinicians, information technology experts, and other healthcare professionals in the U.S. use ICD-10-CM to store and retrieve diagnostic information of symptoms, diseases, and treatments. The current ICD-10-CM repository contains over 71,000 classes as of September 2019.

SNOMED CT is considered to be the most comprehensive healthcare terminology ontology available in terms of the number of concepts, the detailedness of the descriptions, and the expressiveness of the relationships [11]. In the U.S., the NIH National Library of Medicine ${ }^{6}$ acts as the official representative member to the International Health Terminology Standards Development Organization, which manages and provides free access to SNOMED CT. The January 2020 release contains 352,000+ concepts, 1,062,000 relationships, and 1,156,000 descriptions. SNOMED CT is primarily used to standardize representation of clinical content in electronic health records (EHR), including a variety of terminology, phrasing and interpretations, and diagnostic procedures. In addition to a robust coding system, SNOMED CT also contains additional knowledge pertinent to EHRs such as definitions on body structure, organisms, substances, pharmaceutical products, and external physical objects and forces. SNOMED CT has widespread implementation across the globe, SNOMED International is managed by members in 38 countries, and is updated by a wide assortment of clinicians, vendors, and terminologists that make up its community of practice.

# 1.5 Sequenced Treatment Alternatives to Relieve Depression (STAR*D) Dataset 

We will be using the National Institutes of Mental Health (NIMH)'s study on Sequenced Treatment Alternatives to Relieve Depression (STAR*D) ${ }^{7}$ as the dataset. According to the NIMH, this dataset is the largest and longest-running study ever conducted on patients of depression and depression treatment. At the beginning of the study, participants who did not have "moderate" depression on the Hamilton Depression Rating Scale (HAM-D) [33] scale were excluded. Participants who scored less than 14 on the 17-item HAM-D scale indicated mild or no depression and were excluded from the study. The study ended for a patient in remission if the HAM-D score dropped below or equal to 5 .

The dataset contains 2,876 patients, 62 variables, and 22,000+ line records from different "levels" of treatment. Temporal sequencing of variables in this data exists in the form of "levels" of treatment, where patients are given up to four courses of treatments over time. From this dataset, we have extracted a subsample of 1,661 patient observations of 17 diagnosable symptoms (see Table 1) along with two demographic variables for Gender (GEN) and Age (AGE). The symptom variables in this dataset were selected based on (1) the role of the symptom in diagnosing depression in a HAM-D score and (2) the availability of a positive or negative diagnosis in the dataset. Other demographics, such as age, gender, and so on, or symptoms that cannot be binarized are excluded.

For patients of this study, Citalopram is given to every patient in level 1. Patients would only move to level 2 if symptoms persisted after a period of 12-14 weeks. In level 2, patients can choose among other anti-depressives or continue with Citalopram. Patients would move to level 3 if symptoms persisted for a period of 12-14 weeks using level 2 treatments, and patients could choose Citalopram or a new treatment. Level 4 treatment indicates

[^0]
[^0]:    ${ }^{6}$ https://www.nlm.nih.gov/healthit/index.html.
    ${ }^{7}$ https://clinicaltrials.gov/ct2/show/NCT00021528.
    ACM Transactions on Computing for Healthcare, Vol. 4, No. 4, Article 20. Publication date: October 2023.

Table 1. Symptom Variables in STAR*D


that depression persists using level 3 treatments for 12-14 weeks, and the patient can choose again to continue with Citalopram or another treatment.

# 1.6 Knowledge Transfer between Bayesian Networks and Ontologies 

In our research, we have captured patient symptoms in an ontology module [37], stored association links (noncausal) as relationships in a modular ontology [38], and created a CBN to demonstrate its compatibility and translation to an ontology [41]. BNs and ontologies have intrinsic compatibilities that enable them to be modeled after each other. For example, we can create a BN using the semantic information found in ontologies [6, 24, 25]. Deriving a BN from an ontology is possible because semantic representation of knowledge can be translated into components of a BN:

- Nodes are represented as ontology classes;
- Edges and structure are represented as relationships between classes, and;
- Probability distributions are derived from data instances.

Conversely, ontologies can also be created from the structure of BNs [65]. This is achieved by extending the standard OWL ontology language to express conditional, probabilistic relationships between classes. Three extensions currently exist: BayesOWL [65], ${ }^{8}$ PROWL [57], ${ }^{9}$ and OntoBayes [92].

BayesOWL is a framework that extends OWL capabilities for modeling and reasoning with uncertainty. OntoBayes improves upon BayesOWL by supporting random variables with multiple values. Finally, PROWL further extends OWL where probabilistic concepts can co-exist with regular, non-probabilistic concepts. In each of these extensions, a set of rules is applied to transform the class hierarchy defined in an OWL ontology into a Bayesian network.

Methods for learning Causal Bayesian Networks (CBN) directly from ontologies have also been proposed [10, 21, 35, 59, 62]. These methods discover causal structures depicted in ontologies and then test the accuracy of the structure using observational data. For example, SemCaDo [10] focuses on integrating prior knowledge from an ontology in learning initial structures from observational data.

To obtain a CBN directly from an ontology, the taxonomical structure is examined, and then used to infer causality. This creates a CBN model based on ontology classes, relationships, and instances. The conditional probabilities in the resulting model are based on the number of instances, class properties, or the number of definitions in other ontologies. This method creates a CBN model that is based on pre-defined ontologies, rather

[^0]
[^0]:    ${ }^{8}$ http://semanticweb.org/wiki/Bayes_OWL.html.
    ${ }^{9}$ http://www.pr-owl.org/.

than learned from data. Since they are based on a pre-defined ontology, it is not possible for these models to be improved further in terms of predictive accuracy.

In our prior research, we noted that medical ontologies can be improved by analyzing patient data [39]. This research implies that existing ontologies accurately reflect patient data structure to a degree but can be improved. Even though a viable CBN can be derived directly from an ontology (e.g., SemCaDo), this method relies on the accuracy of the ontology, rather than an accurate representation of patient data.

# 1.7 Limitations and Generalizability 

There are inherent limitations to our proposed methodology using DAGs, prior knowledge from ontologies, and adaptability and generalizability to other datasets.

CBNs are expressed as DAGs, which are acyclic by definition and incapable of expressing "feedback loops." Every arc in the model presumes that one event precedes the other, while excluding a potential situation where comorbid events A and B can both be the cause and the effect. For the Bayesian network, the algorithm will choose the best arc direction based on a scoring mechanism and exclude other potentially causal arc directions. However, it is possible to force the calculation of the conditional probabilities for both $\mathrm{A}->\mathrm{B}$ and $\mathrm{B}->\mathrm{A}$ given a learned network structure. If we force a direction in a model that is contrary to what is learned from the data, then the rest of the model will also need to be relearned and reoriented to compensate for the directional change of the arc. Counterfactual studies (the "what-ifs") of causal models may be included in future research as prior knowledge of potential "causal loops" are presented the AMOs of the disease domain. For the ontologies used in this article, no causal loops were discovered or considered as prior knowledge.

The methodology proposed in this article requires (1) a significantly robust dataset and (2) an AMO with expert knowledge. Moreover, the prior expert knowledge presented in the ontology must be useful in identifying or explaining a potential causal mechanism between two variables in the dataset. To acquire this prior knowledge, the methods presented in the following sections manually identify the potentially causal relationships in each of the three AMOs. This manual process is time-consuming and may be automated in future research.

To scale this experiment to other observational patient datasets, the same AMO may be used if they contain expert knowledge that explains a potential causal mechanism. This means that certain AMOs may be better suited for certain datasets. For example, STAR*D contains genetic data for some patients, which will be better paired with a gene-specific ontology such as Gene Ontology. ${ }^{10}$ Previously, we have used the methodology proposed in this article to improve causal models of Alzheimer's patient data [42] and crowdsourced Asthma patient data [40].

### 1.8 Algorithm Selection Using K-fold Cross-validation

We will determine an algorithm to use to learn the BN by performing a k -fold $(k=5)$ cross-validation for a set of popular BN learning algorithms. Using the bn.cv function in bnlearn and the STAR*D data selected from the previous section, we will use Log-Likelihood Loss (logl) [80]: Also known as negative entropy or negentropy, it is the negated expected log-likelihood of the test set for the BN fitted from the training set. A lower log-loss value means better predictions.

For the following experiment, the Min-Max Hill Climbing (MMHC) algorithm has been chosen due to its popularity as a hybrid algorithm for learning Bayesian Networks [76, 88]. MMHC is a popular hybrid (score- and constraint-based) algorithm. It uses very little memory and is capable of finding models for very large datasets and state spaces. MMHC is a hybrid structural learning algorithm that utilizes the Max-Min Parents Children (MMPC) to restrict search space and regular Hill-Climb (HC) to find the optimal network structure.

[^0]
[^0]:    ${ }^{10}$ http://geneontology.org/

Table 2. Log-Likelihood Loss Scores for STAR*D


# 1.9 Comparing Arc Agreement and Predictive Accuracy of Bayesian Networks 

For the quantitative assessment, we will compare the CBNs based on the following:

- Agreement of arcs between models: Use compare() function in the bnlearn package in R [77] to measure agreement between Modified and Baseline CBNs. This function counts the number of directed arcs that are the same (or different) between two networks.
- Predictive accuracy: We compute the cross-validated Area Under the ROC Curves (AUC) of the Baseline and Modified CBNs. AUCs are used to summarize the Receiver Operating Characteristics (ROC) curve, which checks a model's predictive performance. The ROC is a probability curve, and the area under it represents a measure of separability. It tells us how much a model is capable of distinguishing between classes. At higher AUC values, the model is better at predicting negative diagnoses ( 0 s ) as negative diagnoses and positive diagnoses (1s) as positive diagnoses.

The compare() function utilizes a "target" network and "current" network. The "target" network is taken to be "true" or as the "golden standard" network, and the "current" network will be compared to it. Three metrics are returned:

- True positive (tp) arcs appear both in target and in current
- False positive (fp) arcs appear in current but not in target
- False negative (fn) arcs appear in the target but not in current

To visualize the performance of the CBNs, we can use the ROC curve and the AUC [14]. The ROC curve is a performance measurement for the classification problems at various threshold settings. ROC is a probability curve, and AUC represents the degree or measure of separability. This metric measures how well the model is capable of distinguishing between classes. For binary datasets of patient diagnoses, 0 s mean a negative diagnosis class and 1 s mean a positive diagnosis class. The higher the AUC, the better the model is at predicting 0 s as 0 s and 1 s as 1 s .

FPR tells us what proportion of the negative class was incorrectly classified by the classifier. A higher TNR and a lower FPR is desirable, since we want to correctly classify the negative class. In a ROC curve, a higher X-axis value indicates a higher number of False positives than True negatives, while a higher Y-axis value indicates a higher number of True positives than False negatives. The choice of the threshold depends on the ability to balance between False positives and False negatives. If the plot of the ROC curve (and the AUC) is higher in one model vs. another, then we can say that the model with the higher AUC score did a better job of classifying the positive class in the dataset.

![img-1.jpeg](img-1.jpeg)

Fig. 2. Taxonomic hierarchy in MedDRA accessed via Bioportal.

# 1.10 Experiment Design 

In the following sections, we will go over four steps in the experiment:

- Discover potentially causal relationships in the form of ordered variable pairs in AMOs.
- Create a baseline CBN using MMHC.
- Modify the MMHC algorithm to orient the CBN structure using ordered variable pairs.
- Analyze and compare the Baseline and Modified CBNs, including analysis of specific causal mechanisms in existing literature.


## 2 EXTRACTING PRIOR KNOWLEDGE AND EXPERTISE FROM AUTHORITATIVE MEDICAL ONTOLOGIES (AMO)

### 2.1 Prior Knowledge in Hierarchical Subsumption Relationships and MedDRA

A hierarchical ontology classifies concepts at each level, proceeding from generalized to specialized concepts. Hierarchical ontologies implement inheritance in subclasses [18, 46]. An ontology is representative of the relationships between classes than taxonomies, which are generally limited to classification. Complex ontologies such as AMOs often have symptom classes that fit into multiple disease areas of a given hierarchy, resulting in multiple inheritance. In Figure 2 the MedDRA ontology is accessed using BioPortal. Within this ontology, "Psychiatric disorders" is the most general class in the hierarchy, while "Nervousness" is the most specific class. "Nervousness" is a specialization of "Anxiety symptoms."

The ontology definition contains a taxonomical hierarchy of relevant domain concepts, possible relationships between concepts, data and object properties of concepts (attributes with value ranges), and derivation rules to infer new knowledge [66]. Each AMO contains specific hierarchies, which define sets and subsets of disease symptoms, as they related to one another in a subsumption "is_superclass_of" relationship. For example, grey boxes in Figure 4 are concepts that lead to the symptom Nervousness, while white boxes are related classes not directly related to it. Nervousness is hierarchically defined under Anxiety Symptoms in a specific sequence. For example, Nervousness "is-a" type of Anxiety Symptom and Anxiety Symptom "is_superclass_of" Nervousness.

ACM Transactions on Computing for Healthcare, Vol. 4, No. 4, Article 20. Publication date: October 2023.

![img-2.jpeg](img-2.jpeg)

Fig. 3. Selected STAR* ${ }^{\star}$ Symptoms in MedDRA.
![img-3.jpeg](img-3.jpeg)

Fig. 4. Hierarchical view of symptoms in MedDRA.
In an ontology's XML schema specification, the "is-a" relationship models inheritance in two ways [63]:

- Top-down inheritance of attributes from superclasses to subclasses. In the example, assuming Nervousness as a subclass of a superclass Anxiety Symptoms. Then Nervousness inherits all attributes that are defined for Anxiety Symptoms.
- Bottom-up inheritance of instances from subclasses to superclasses. Assuming Nervousness as a subclass of a superclass Anxiety Symptoms. Then Anxiety Symptoms inherits all instances (i.e., elements) that are an element of Nervousness. Every instance of Nervousness is also an instance of Anxiety Symptoms. A patient (instance) exhibiting Nervousness also exhibits Anxiety Symptoms.

Ordering of a superclass-subclass subsumption relationship follows OWL semantic web standards and is intuitive. A single ordering can be defined as a single parent-child or superclass-subclass relationship. The symbol " $\rightarrow$ " is used to indicate a subsumption relationship from a parent or superclass to a child or subclass: superclass $\rightarrow$ class. The symptoms classes in Figure 4 can also be defined in OWL syntax:

![img-4.jpeg](img-4.jpeg)

Fig. 5. Melancholic depression hierarchy in MedDRA.

```
Class(PsychiatricDisorders partial)
Class(AnxietySymptoms partial restriction(part:partOf_directly
    someValuesFrom(AnxietyDisorders)))
Class(ObsessiveCompulsive partial restriction(part:partOf_directly
    someValuesFrom(AnxietyDisorders)))
```

MedDRA concepts are classified in a hierarchical structure:

- System Organ Class (SOC)
- High Level Group Term (HLGT)
- High Level Term (HLT)
- Preferred Term (PT)
- Lowest Level Term (LLT)

For example, Melancholic Depression and Melancholia are both lowest-level terms (LLT) from MedDRA and classified as a subclass of Major Depression (see Figure 5). Major Depression is a Preferred Term (PT), while Depressive Disorders is a High-Level Term (HLT). Between Major Depression and Melancholic Depression (or Melancholia [13]), the following ordered variable pair exists in the subsumption relationship:

Major Depression $\rightarrow$ Melancholic Depression
A full ordered chain in the ontology leading to the Melancholic Depression symptom exists in the MedDRA ontology structure, defined from most general to specific: Psychiatric Disorders $\rightarrow$ Depressed mood disorders and disturbances $\rightarrow$ Depressive Disorders $\rightarrow$ Major Depression $\rightarrow$ Melancholic Depression. In MedDRA, the selected symptoms contain 27 classes within the "Psychiatric Disorders" Base Class. From these 27 classes, 18 are symptoms originally selected from the patient dataset (see Table 3), 2 symptoms are defined twice within the hierarchy (Agitation and Melancholic), and 9 are parent-classes not in the dataset but maintain the ontological

Codes
$\checkmark$ F45 Somatoform disorders
$\checkmark$ F45.0 Somatization disorder
$\checkmark$ F45.1 Undifferentiated somatoform disorder
$\checkmark$ F45.2 Hypochondriacal disorders
$\checkmark$ F45.20 Hypochondriacal disorder, unspecified
$\checkmark$ F45.21 Hypochondriasis
$\checkmark$ F45.22 Body dysmorphic disorder
$\checkmark$ F45.29 Other hypochondriacal disorders
$\checkmark$ F45.4 Pain disorders related to psychological factors
$\checkmark$ F45.41 Pain disorder exclusively related to psycholos
$\checkmark$ F45.42 Pain disorder with related psychological facto
$\checkmark$ F45.8 Other somatoform disorders
$\checkmark$ F45.9 Somatoform disorder, unspecified
Fig. 6. ICD-10-CM other vital details related to Somatoform.

Table 3. Summary of Ordered Variable Pairs from Three AMOs


structure. Generalized anxiety is the primary parent-class of anxiety symptoms, panic, and obsessive compulsive are secondary subclasses. Finally, agitation and social phobia are tertiary classes in this hierarchy. While "fear symptoms and phobic disorders" is not a variable collected in the STAR*D dataset, this class subsumes "social phobia," which is a patient variable.

Subsumption relationships in the hierarchical taxonomy of MedDRA gives us prior knowledge of seven ordered variable pairs, which can be used to orient a CBN:

- Somatoform (SD) $\rightarrow$ Hypochondriasis (HD)
- Generalized Anxiety (GAD) $\rightarrow$ Anxiety Symptoms (ANX)
- Generalized Anxiety (GAD) $\rightarrow$ Panic (PD)
- Generalized Anxiety (GAD) $\rightarrow$ Obsessive Compulsive (OCD)
- Generalized Anxiety (GAD) $\rightarrow$ Social Phobia (SPD)
- Anxiety (ANX) $\rightarrow$ Irritability (IRR)
- Major depressive disorder (MDD) $\rightarrow$ Melancholic (MEL)


# 2.2 Prior Knowledge from Indexed Terms in ICD-10-CM 

In addition to the subsumption relationships and ontological hierarchy, some AMOs record prior clinical expertise within the object properties of classes. The ICD-10-CM ontology contains "Other Vital Details" as well as other object properties for indexed symptom terms. These symptoms are related to other symptoms, which can be used to infer causality between two variables and create an ordered variable pair.

ICD-10-CM is a formal hierarchical ontology organized using a straightforward alphanumeric code structure. ${ }^{11}$ The first three characters (e.g., F45) designate the category of the diagnosis, where "F" indicates "Mental, behavioral, and neurodevelopmental disorders." The range of F40-F48 designates "Anxiety, dissociative, stressrelated, somatoform and other nonpsychotic mental disorders." F45 specifically designates "Somatoform disorders," which is a variable for patients of the STAR*D study (see Figure 8).

The next three characters correspond to "other vital details" and could contain additional information related to the cause or set of causes, anatomic site, severity, or other clinical details. For example, Hypochondriacal disorders (F45.2) is a symptom that is potentially caused by Somatoform. Hypochondriasis, a specific type of hypochondriacal disorder, is given additional categorical specification as F45.21.

Mapping our selected STAR*D variables to ICD-10-CM, we discover that versions of insomnia (initial, delayed, and middle) are not further specified under Sleep Disorders (F51). Consolidated Insomnia (CI) is a union of Initial, Middle, and Delayed Insomnia variable sets and represents Insomnia (F51.0) in ICD-10-CM for modeling and analysis.

Overall, 16 of the selected symptom variables from the STAR*D data were mapped to the ICD-10-CM ontological hierarchy, seen in Figure 7. The three variables related to insomnia (Initial, Middle, and Delayed insomnia) are not available under the Mental, Behavioral, and Neurodevelopmental Disorders (F01-F99) parent class. However, insomnia does exist as a generic class in F51.0. A variable (Combined Insomnia) was created to combine Initial, Middle, and Delayed insomnias as a single variable. A positive diagnosis of any type of insomnia will yield a positive diagnosis in Combined Insomnia.

For ICD-10-CM, the majority of the variable ordering occurs at the indexed term (see Figure 7) level. Indexed terms are additional terms found in the Alphabetic Index, which are lists of terms included under a variety of ICD-10-CM codes. ${ }^{12}$ These terms are related conditions (and their codes) under a specific ICD-10 code. The terms may be synonyms of the code title or terms that list the various associated conditions assigned to that code. For example, Melancholia (F32.9-F33.9) is an indexed term and a symptom that leads to Hypochondriac (F45.29), a specific type of Hypochondriacal disorder (F45.2).

Two ordered variable pairs, Major Depressive Disorder $\rightarrow$ Melancholia and Somatoform disorders $\rightarrow$ Hypochondriacal disorders, are based on subsumption relationships. These relationships are visualized in Figure 8. Overall, ICD-10-CM gives us 12 ordered variable pairs. Eight pairs are classified under Mental and Behavioral Disorders (F01-F99):

[^0]
[^0]:    ${ }^{11}$ https://www.cdc.gov/nchs/icd/icd10cm.htm.
    ${ }^{12}$ https://www.cms.gov/Medicare/Coding/ICD10/.
    ACM Transactions on Computing for Healthcare, Vol. 4, No. 4, Article 20. Publication date: October 2023.

![img-5.jpeg](img-5.jpeg)

Fig. 7. ICD-10-CM indexed terms related to Melancholia.
![img-6.jpeg](img-6.jpeg)

Fig. 8. Selected STAR*D symptoms in ICD-10-CM.

- Drug Abuse (DAD) $\rightarrow$ Consolidated Insomnia (CI)
- Melancholia (MEL) $\rightarrow$ Hypochondriasis (HD)
- Dysthymia (REC) $\rightarrow$ Melancholic (MEL)
- Dysthymia (REC) $\rightarrow$ Generalized Anxiety (GAD)
- Generalized Anxiety (GAD) $\rightarrow$ Social Phobia (SPD)
- Generalized Anxiety (GAD) $\rightarrow$ Panic (PD)
- Major depressive (MDD) $\rightarrow$ Melancholic (MEL)
- Somatoform (SD) $\rightarrow$ Hypochondriasis (HD)

![img-7.jpeg](img-7.jpeg)

Fig. 9. SNOMED: Hypersomnia caused by alcohol abuse.
Insomnia is also classified under Diseases of the Nervous System (G00-G99) as G47.0, provides the following ordered variable pairs that exist as diagnoses relative to other pre-existing conditions, specifically as its causally related ("due to" relationship) to drug/alcohol abuse and other mental disorders. Based on the indexed terms under G47.00, the following pairs can be determined:

- Alcohol Abuse (AAD) $\rightarrow$ Consolidated Insomnia (CI)
- Drug Abuse (DAD) $\rightarrow$ Consolidated Insomnia (CI) - reiterated, as it already exists in F01-F99.
- Generalized Anxiety (GAD) $\rightarrow$ Consolidated Insomnia (CI)
- Dysthymia (REC) $\rightarrow$ Consolidated Insomnia (CI) ${ }^{*}$
- Major Depressive (MDD) $\rightarrow$ Consolidated Insomnia (CI) ${ }^{*}$
* Since insomnia "due to" depression does not specify the kind of depression, both variables (REC and MDD) are included here as potential causes.


# 2.3 Prior Knowledge from Object Property Types Found in SNOMED CT 

Relationship attributes in SNOMED CT are represented as a third concept and identify the meaning of the association between two concepts. A relationship type may be a standard "Is-a" relationship representing hierarchy or a specific relationship such as "finding site" or "cause of"-both of which imply a specific sequence of events or ordering between the source concept and the destination concept. For example, hypersomnia and alcohol abuse share a causative relationship that is documented in several different places in the SNOMED.

The relationship between the source concept (alcohol) and destination concept (hypersomnia) is expressed as a concept that can be inferred. SNOMED CT is unique among the three AMOs used in this project in that causal relationships are explicitly described in attributes used to define the meaning of concepts within the Concept Model [12]. This Concept Model governs how concepts within SNOMED CT are allowed to relate to each other. Since the SNOMED CT AMO is vast in its application, concepts within specific classification hierarchies are defined by different types of attributes. SNOMED CT concept hierarchies include:

- Clinical finding concepts
- Procedure concepts
- Evaluation procedure concepts

![img-8.jpeg](img-8.jpeg)

Fig. 10. Compositional grammar diagram for hypersomnia caused by alcohol.

- Specimen concepts
- Body structure concepts
- Pharmaceutical/biologic product concepts
- Situation with explicit context concepts
- Event concepts
- Physical object concepts

For clinical concepts, specifically, we are interested in the following attributes indicating potential causality:

- Associated with represents a clinically relevant association between two concepts without either implying a causal or sequential relationship between them. It is one of the criteria for establishing a causal relationship but needs to be validated using other means if an ordered variable pair is to be established between the two concepts. "Mixed anxiety and depressive disorder" and "Depressive Disorder co-occurrent with anxiety" does not indicate a direction. This provides us with an association or correlation, but no additional insights into whether or not one is the cause, and the other is the effect.
- After represents a sequence of events where a clinical finding occurs after another clinical finding or a procedure. This represents a time-based temporal sequence between two variables in terms of clinical findings and is one of the criteria used for establishing a causal relationship.
- Due to relates a clinical finding directly to a cause, such as another clinical finding or a procedure. This is a direct causal relationship that can be diagnosed or observed in a patient.
- Causative agent identifies the direct causative agent of a disease. This can be a substance, physical force, or an organism.
SNOMED CT expresses the relationships between concepts by utilizing compositional grammar, or a set of rules that govern the way SNOMED CT expressions are represented [74]. This can be done in a text format or as

![img-9.jpeg](img-9.jpeg)

Fig. 11. Selected STAR*D symptoms in SNOMED CT causal object properties.
a compositional grammar diagram. For example, "Hypersomnia caused by alcohol (disorder)" is a concept that represents the causal relationship between hypersomnia and alcohol abuse.

From the attributes represented in the compositional grammar, 12 ordered variable pairs can be established based on STAR*D variables:

- Alcohol Abuse $\rightarrow$ Hypersomnia
- Alcohol Abuse $\rightarrow$ Insomnia (consolidated)
- Alcohol Abuse $\rightarrow$ Generalized Anxiety Disorder
- Alcohol Abuse $\rightarrow$ Anxious Personality
- Drug Abuse $\rightarrow$ Insomnia (consolidated)
- Drug Abuse $\rightarrow$ Hypersomnia
- Drug Abuse $\rightarrow$ Generalized Anxiety Disorder
- Drug Abuse $\rightarrow$ Anxious Personality
- Drug Abuse $\rightarrow$ Obsessive Compulsive Disorder
- Hypochondriasis $\rightarrow$ Generalized Anxiety Disorder
- Hypochondriasis $\rightarrow$ Anxious Personality
- Somatoform $\rightarrow$ Hypochondriasis ("is-a" structure)

These ordered variable pairs are a direct result of several causal object properties identified in the SNOMED CT expressions, which addresses alcohol and drug abuse, with direct causal agents Alcohol or Drug type. These pairs are visualized in Figure 11.

# 2.4 Prior Knowledge from Multiple Ontologies 

The 24 ordered pairs that we discovered from MedDRA, ICD-10-CM, and SNOMED CT give us prior knowledge and insight into the disease of depression. Regardless of the algorithm used to generate the CBN, observational data will always be limited by other criteria external to the data collection process $[1,7,89]$.

When we match observational data variables to classes established in three different AMOs, we are able to (1) standardize the variable name and (2) obtain expertise from three distinct ontologies based on the location of the variable within the ontology. Recurrence of pairs among ontologies indicate partial congruence in terms of how the symptoms are to be ordered.

Extracting ordered pairs from multiple ontologies also demonstrates that while different AMOs may serve different purposes (translation vs. classification, etc.), the process to extract ordered variable pairs within each of them are similar. Furthermore, if the ordered pairs successfully improve the fit of a CBN to the data, then we will demonstrate that domain-specific expertise can come from any AMO and can be consolidated to inform the learning of a CBN.

Finally, as we will demonstrate in the following sections, these ordered pairs will improve the fit of a CBN model to the data by acting as guidelines on how the model can be generated. Considering that the first step in generating a BN for any algorithm is structure learning [51, 79], and that the structure is learned starting with a random network, any viable prior knowledge of the variables would reduce confounding and improve the fit of the data to the model structure.

With an improved structure, parameter learning of the conditional densities among the edges between nodes should also improve using a Bayesian estimation technique. The improvements can be observed in the following ways: (1) elimination of directed edges that contradicts prior knowledge from the AMO, (2) the removal of edges with low conditional probabilities, (3) overall higher conditional probabilities among the parameters of the CBN.

# 3 MODIFYING THE MAX-MIN HILL CLIMBING ALGORITHM USING ONTOLOGY ORDERING 

### 3.1 The Min-Max Hill Climbing Algorithm (MMHC)

MMHC uses two other algorithms in two distinct stages:
Stage 1: The Max-Min Parents \& Children (MMPC) [88] algorithm is used to learn the parents and children nodes of a variable $\mathrm{X}(P C x)$ as a subset of the variables $(V)$ in the data $(D)$.
Stage 2: A greedy hill-climbing algorithm is applied to the $P C x$ discovered using MMPC. A random symptom $Y$ is selected, and neighboring symptoms are searched for associations using the Dirichlet likelihoodequivalence uniform score (BDeu) [88] within PCx. The BDeu score aims at maximizing the posterior probability of the directed acyclic graph (DAG) based on the dataset, while assuming a uniform prior distribution over possible DAGs.

The strongest neighboring association is selected as a conditional probability. This algorithm is greedy by default and obtains the next best neighbor without looking ahead. The pseudocode for MMHC is as follows:

Pseudocode for MMHC Algorithm
Procedure Max-Min Hill-Climbing(D)
Input: dataset D with variable set V
Output: a DAG based on the variables in D
For every variable $\mathrm{X} \in \mathrm{V}: \mathrm{PCx}=\mathrm{MMPC}(\mathrm{X}, \mathrm{D})$
Start with an empty graph and perform greedy hill-climb (add-edge, delete-edge, reverse-edge)
Only try add-edge operator for Y to X if $\mathrm{Y} \in \mathrm{PCx}$
Return the highest scoring DAG
End procedure
The greedy hill-climbing portion of the algorithm begins with an empty graph and edges are added, deleted, or reversed, which leads to the largest increase in BDeu score. The pseudocode for greedy hill-climbing is as follows:

Pseudocode for greedy hill-climbing
Procedure Greedy hill-climbing for MMHC(PCx)
Input: Parent-Children sets from MMPC
Output: A DAG X with highest overall BDeu Score
Start with an empty graph
For every PCx graph:
add-edge $Y$ to $X$ if $Y \in P C x$
delete-edge $Y$ from $X$ if higher BDeu score from PCx exists
reverse-edge $Y$ from $X$ if a reversal results in a higher BDeu score
Return highest scoring DAG X

# End procedure 

### 3.2 Modifying the MMHC to Consider Prior Expertise

The MMHC algorithm will need to be modified to consider prior expertise, which exists in the form of several ordering pairs. The modification occurs during the second step of the MMHC algorithm. During the second stage of the MMHC algorithm, the conditions for the add-edge operator is modified to consider prior ordered pairs. Previously, an edge is added if $Y \in P C x$.

For the algorithm to consider the ordered variable pairs from the AMOs, the conditions for using the add-edge operator within MMHC must now satisfy two conditions:

- $\mathrm{Y} \in \mathrm{PCx}$ (this is an original condition for the MMHC algorithm and will remain); and
- Y to X does not violate the direction of any ordered variable pairs previously discovered in an AMO.

Condition 1 remains from the original MMHC algorithm and states that edge $Y$ to $X$ may only be added if it exists in $P C x$. Condition 2 is an addition to the MMHC algorithm. This modification checks the edge addition against a list of previously established ordered variable pairs.

The pseudocode for the modified MMHC algorithm considering prior expertise is as follows:

## Modified MMHC algorithm

Procedure MMHC with Ordered Variable Pairs(D)
Input: dataset D with variable set V
Output: DAG based on the variables in D
For every variable $X \in V: P C x=\operatorname{MMPC}(X, D)$
Start with an empty graph and perform greedy hill-climb (add/delete/reverse edge). Only try add-edge operator for Y to X if $\mathrm{Y} \in \mathrm{PCx}$ and if Y to X conforms to a list of a priori ordered variable pairs
Return the highest scoring DAG

## End procedure

For Y to X to consider prior knowledge in the form of ordered pairs, the edge direction of Y to X cannot violate a previously established ordered pair. For example, if a prior sequence suggests that a directed edge exists from X to Y , then the edge Y to X will not be added by the greedy hill-climbing algorithm, regardless of whether Y $\in$ PCx or if there is a high BDeu score for Y to X . The greedy hill-climbing portion of the MMHC algorithm begins with an empty graph, and edges are added, deleted, or reversed, which leads to the largest increase in BDeu score. However, we are now adding a contingency that regardless of score, an edge cannot be added using greedy hill-climbing, which contradicts a prior order within an ontology. The pseudocode for the modified greedy hill-climbing algorithm with previously ordered variable pairs is as follows:

![img-10.jpeg](img-10.jpeg)

Fig. 12. Modified MMHC algorithm considering prior expertise.

Modified greedy hill-climbing algorithm
Procedure Greedy HC with Ordered Variable Pairs (PCx)
Input: Parent-Children sets from MMPC
Output: A DAG X with highest overall BDeu Score
Start with an empty graph
For every PCx graph:
add-edge Y to X if $\mathrm{Y} \in \mathrm{PCx}$ AND if Y to X conforms to a list of a priori ordered variable pairs
delete-edge Y from X if higher BDeu score from PCx exist
reverse-edge Y from X if a reversal results in a higher BDeu score
Return highest scoring DAG X

# End procedure 

Since these modifications alter the structure of the learned Bayesian network, the conditional probability parameters of the edges in the network will also change. The changes depend on which edges have been generated, and the conditional dependencies that are formed within the network.

## 4 AN IMPROVED CAUSAL BAYESIAN NETWORK

### 4.1 Creating a Baseline Causal Bayesian Network (CBN) without Prior Ordering Knowledge Using MMHC

A baseline CBN model without prior ordering can be generated by applying the MMHC algorithm on the existing STAR*D data. An unmodified MMHC algorithm in the bnlearn package in R can be used to learn the structure of the network in conjunction with the bn.fit function to learn the parameters of the structure.

To obtain a CBN, we need to first prepare the STAR*D dataset so (1) only complete records are included (there are no rows with NA values) and (2) the binary data elements are re-classified as "Factors." In the baseline MMHC model, the conditional probabilities of symptoms related to Anxiety are visualized in Figure 13.

These probabilities are calculated as the maximum likelihood estimation [90] using the Bayes Theorem, where the posterior $=$ likelihood * prior / evidence. To infer causality between two symptom variables, we want to know the probability of a positive diagnosis of one symptom (event) given the positive diagnosis of another (evidence). For example, given a positive Anxiety diagnosis ( 1 indicating a positive diagnosis observed for the patient in the collected data and 0 indicating a negative diagnosis), the conditional probability of a positive Irritability diagnosis is $78.1 \%$. This matrixed conditional probability matrix for Anxiety and Irritability is as follows:

![img-11.jpeg](img-11.jpeg)

Fig. 13. Conditional probabilities of baseline CBN related to Anxiety on MedDRA hierarchy.


We can also query the conditional probability using cpquery in bnlearn:

```
> cpquery(cbn,
event = (Irritation.Diagnosis == "1"), evidence = (Anxiety.Diagnosis == "1"))
```

[] 0.7812382
In the resulting CBN, Anxiety is a significant causal indicator for Irritability, with a conditional probability maximum likelihood of $78.1 \%$. This directed relationship also exists in the taxonomic hierarchy of MedDRA as an ordered pair, even though no prior ordering has been taken into consideration to orient the arcs of the CBN. This confirms the prior knowledge of this relationship contained in the taxonomical hierarchy of MedDRA. Additional confirmation of this causal relationship can be readily found in existing medical and epidemiological research $[19,44,82]$.

Furthermore, the Melancholic Depression symptom is a significant causal indicator (71.5\%) for Anxiety. While this does not exist as an ordered pair in the MedDRA taxonomy, the correlation between Melancholic Depression and Anxiety is also well established in existing medical and epidemiological research [5, 13, 30]. Anxiety is also a moderately good causal indicator for three types of insomnia: Initial, Middle, and Hyper insomnia, ranging from $53 \%$ to $65 \%$. This is also well documented in existing research related to insomnia and anxiety [44-46].

Finally, an arc contradicting the prior knowledge according to MedDRA hierarchy is removed with prior knowledge: Anxiety Symptoms $\rightarrow$ Generalized Anxiety with a conditional probability of $25.8 \%$. In Figure 13, the following ordering of symptoms in the ontological structure exists:

ACM Transactions on Computing for Healthcare, Vol. 4, No. 4, Article 20. Publication date: October 2023.

![img-12.jpeg](img-12.jpeg)

Fig. 14. Visual comparison of arcs in netb and netc: $\mathrm{TP}=$ black, $\mathrm{FP}=$ red, $\mathrm{FN}=$ blue.
![img-13.jpeg](img-13.jpeg)

Fig. 15. Cross-validated AUC diagrams for Baseline (netb) vs. Modified (netc2) STAR*D CBNs.
Psychiatric Disorders $\rightarrow$ Generalized Anxiety $\rightarrow$ Anxiety Symptoms $\rightarrow$ Irritability.
However, the baseline MMHC algorithm generates an edge with Anxiety $\rightarrow$ Generalized Anxiety. Since the MMHC algorithm does not have any prior knowledge on how the edges should be oriented, this directed edge is allowed to be added to the BN when the structure is learned.

# 4.2 A Modified CBN Using MMHC and Ordered Variable Pairs 

Modifying the algorithm with prior ordered variable pairs removes the possibility for the algorithm to learn any arcs, which contradicts prior knowledge. Furthermore, since the arcs are oriented based on prior pairs, new

BDeu scores are calculated, resulting in new relationships being formed. Previously, we have predetermined seven prior ordered variable pairs based on the MedDRA ontology (see Table 3).

To implement the orientation of the ordered variable pairs, the reverse direction of each pair will be blacklisted in the MMHC algorithm. For example, the following ordered pair from MedDRA will eliminate a contradictory arc learned from the baseline CBN:

# Anxiety Symptoms (ANX) $\rightarrow$ Generalized Anxiety (GAD) 

To eliminate this contradiction from the CBN modified with MedDRA variable pairs, it must be blacklisted in the MMHC algorithm. Blacklisted arcs are never included in the network and prevent the arc from being learned in the CBN regardless of whether it is represented in the data:

```
blist=data.frame(from=c("ANX"),to=c("GAD"))
mmhc(x=StarD, whitelist = NULL, blacklist = blist, restrict.args = list()).
```

The new model has also eliminated several edges from the old model that had weak maximum likelihoods. For example, the edges GAD $\rightarrow$ SD and GAD $\rightarrow$ HD are not added to this CBN. The pair Generalized Anxiety (GAD) $\rightarrow$ Anxiety (ANX) was not represented as an edge in the modified CBN. ANX $\rightarrow$ GAD was eliminated, as it contradicted the ordered variable pair prior from MedDRA.

Previously, we extracted 12 ordered variable pairs from ICD-10-CM (see Table 3). ICD-10-CM provided similar increases to conditional probabilities and identified new edges among the variables that are significant to the disease. Three new edges were formed that were not previously a part of the original baseline CBN:

- Melancholia (MEL) $\rightarrow$ Hypochondriasis (HD)
- Dysthymia (REC) $\rightarrow$ Melancholic (MEL)
- Dysthymia (REC) $\rightarrow$ Generalized Anxiety (GAD)

These edges had significant conditional probabilities of $61.2 \%, 57.1 \%$, and $62.8 \%$, respectively. The overall increase for all conditional probabilities in the ICD-10-CM CBN is $10.4 \%$, with the average increase for corresponding ordered pairs being $31.9 \%$. These average increases are skewed by the new edges. SNOMED CT provided us with several prior pairs that have direct causal agents centered around Alcohol Abuse (AAD) and Drug Abuse (DAD). Using these priors, 10 new arcs were established in the CBN. Four of them are particularly notable: AAD $\rightarrow$ ANX with $62.2 \%$, AAD $\rightarrow$ CI with $52.1 \%$, AAD $\rightarrow$ GAD with $44.2 \%$, and DAD $\rightarrow$ ANX with $45.1 \%$. These relationships are intuitive and well-established in existing epidemiological literature. For example, alcohol abuse is a direct cause of anxiety and anxiety-related symptoms in other studies and controlled trials [16, 85].

### 4.3 Exploring the Validity of Causal Relationships in Modified CBNs

Melancholia (MEL) and Hypochondriasis (HD) (or melancholia as a cause of hypochondriasis) in particular, has an established causal relationship in previous epidemiological studies. Hypochondriasis is often secondary to other psychiatric disorders such as melancholia, and hypochondrial attitudes in patients "remit when the primary disorder is successfully treated" [47]. In a smaller-scale RCT using Illness Attitude Scales identifying hypochondriacal patients, findings were "in accord with the clinical observation that melancholia is one of the causes of hypochondriacal fears and beliefs [48]."

In another study using Structured Clinical Interview for DSM (SCID) diagnosis, dysthymia (REC) is highly correlated with GAD [71]. Dysthymia and generalized anxiety disorders are both chronic disorders, with extremes determined by early-onset GAD or late-onset REC [81]. Other studies suggest that the diagnosis of dysthymia and generalized anxiety are very similar [81, 96], but suggest that dysthymic disorders are an indicator to other anxiety-related or more severe mood disorders [15].

Finally, AAD as a cause for ANX. This is a relationship with a direct cause-and-effect diagnosis available in SNOMED CT as alcohol-induced anxiety disorder. This is significant, because a causal indicator, the consumption

Table 4. Summary of Six Modified STAR*D CBNs


of alcohol, is specifically defined in SNOMED CT. Anxious features and symptoms are diagnosed via the Hamilton Rating Scale for Depression (HRSD) on a subscale [58], and nearly $50 \%$ of the selected dataset $(825 / 1,661)$ of the selected patients with depression were diagnosed with anxious features. Anxiousness and anxieties have been studied as indicators for alcohol abuse [16, 85], with patients of alcoholism receiving a diagnosis of one or more types ${ }^{13}$ of anxiety disorders. Diagnosis and treatment of anxiety "may prove critical to relapse prevention."

Orienting CBNs may also significantly improve the strength of the conditional probabilities or the arcs, indicating values closer to relationships in the underlying causal model. For example, GAD as the cause of panic disorder (PD) more than doubled from $21.4 \%$ in the baseline, to $43 \%-49 \%$ in an oriented CBN. These two symptoms do not have a significant causal relationship but are often comorbid and treated at the same time [4, 81, 91].

Orienting the CBN also eliminates a variety of edges, as the structure of the CBN changes. The arcs that were eliminated contain generally weak conditional probabilities ( $8.2 \%$ average) present in the data. For example, PD's relationship with somatoform disorder (SD) has been previously documented in a series of structured clinical interviews to determine the relationship between the two symptoms. The controlled study found that out of the 21 patients with panic disorder, none of them met the DSM-IV criteria for somatization disorder [29]. In another study, somatic symptoms are the precursor to panic disorder [50] and not the other way around. The rationale behind this causal relationship is due to the nature of somatization, the symptoms that a patient feels but cannot be adequately observed, which causes panic.

In the baseline CBN, a specific arc (ANX $\rightarrow$ GAD) was learned from the data with a conditional probability of $25.8 \%$. The direction of this arc goes against an ordered variable pair established in MedDRA, from GAD $\rightarrow$ ANX. This ordered variable pair is not present in SNOMED or ICD-10-CM. If the CBN is oriented by the ordered variable pair GAD $\rightarrow$ ANX, then it would not exist in the CBN. This particular arc is learned in the baseline and ICD-10-CM models, but not MedDRA (or other models with MedDRA's ordering) or SNOMED CT.

Finally, while the overall parameters of the conditional probabilities see significant increases, not all arcs are improved simply because they are oriented by a prior variable pair. For symptoms and disorders related to Anxiety in patients of depression, orienting the CBN did not improve conditional probabilities for insomnia. In light of significant contextual research that Generalized Anxiety and Anxiety symptoms are significant causal indicators of different kinds of insomnia [26, 64, 84, 97].

# 4.4 Comparing Arc Agreement and Predictive Accuracies of Baseline and Modified CBNs 

We create modified CBNs using previously established ordered-variable pairs from AMOs as priors. Additionally, we combine knowledge from three AMOs and produce two modified CBNs. Overall, we produce seven CBNs for the exploration using STAR*D data and AMOs:

[^0]
[^0]:    ${ }^{13}$ https://www.hhs.gov/answers/mental-health-and-substance-abuse/what-are-the-five-major-types-of-anxiety-disorders/index.html.

Table 5. Arc Agreement of Modified STAR*D CBNs to Baseline


Table 6. Mean AUC values of STAR* ${ }^{*} \mathrm{D}$ CBNs


For arc agreement, we will use the compare() function in the bnlearn R package to measure agreement between Modified and Baseline CBNs. Compare (netm, netb) sets netm (modified MedDRA CBN) as the "target" network and netb as the "current" network. The "target" network is taken to be "true" or as the "golden standard" network, and the "current" network will be compared to it. This function compares netb (Baseline) to the standard (MedDRA), where (1) True positive (tp) arcs appear both in target and in current; (2) False positive (fp) arcs appear in current but not in target; and (3) False negative (fn) arcs appear in the target but not in current:

```
> compare(netm, netb)
$tp
[] 16
$fp
[] 0
$fn
[] 2
```

Table 5 compares the baseline to the other six modified CBNs as the "target network." "Agreement" is a percentage calculated as the number of TP arcs divided by the total arcs. In terms of Modified CBNs, MedDRA (90\%) is the closest in agreement to the Baseline, while ICD-10 (55\%) and SNOMED (40\%) are less in agreement with the Baseline and more in agreement with their respective ontologies.

To visualize the performance of the CBNs, we can use the ROC (Receiver Operating Characteristics) curve and the AUC (Area Under the Curve) [14]. To cross-validate the AUC curve, we are using $80 \%$ of the data to train the model and testing it on $20 \%$ of the data. Using the k -fold method, setting $\mathrm{k}=5$, we partition the data into five subsamples each with $20 \%$ of the data. This k-fold is repeated once, producing 10 runs that are averaged.

Agreement between the two networks is $50 \%$ (10 true positive arcs/20 total) when comparing the Modified netc2 CBN to the Baseline. While adding the ontological constraints did not significantly improve accuracy of predictions, it did increase congruence between model and ontological causal claims. This indicates that the

Modified network (netc2) agrees with both the ontology and the data while being significantly different than the baseline.

# 4.5 Causal Bayesian Networks and Ontologies: Lessons Learned 

In our methodology, acquiring variable pairs of potentially causal relationships from AMOs was difficult and time-consuming. These pairs represent the possibility of the existence of a causal mechanism based on prior knowledge. At present, there is not a straightforward way of obtaining these variable pairs from an ontology. Comorbidities among symptoms are heavily confounded, and it is difficult to decipher potential causal relationships among them. This task is a good candidate for automation using artificial general intelligence.

Due to confounding and the high dimensionality of comorbid symptoms, a data-driven method is preferred. While it is possible for an ontology to store causal information in its relationships, the AMOs used in the methodology are not completely causal. The causal knowledge AMOs do provide is imperfect, and it is possible for additional causal relationships, which are not present in the AMO, to be present in the data. Outside of observational data and medical ontologies, it is possible that this methodology could be applied in other data-driven applications.

While we did not produce a modified CBN that has a higher AUC score, we were able to produce a CBN that aligns with the potential causal claims or causal indicators that are present in an ontology. By incorporating causal knowledge and causal mechanisms present in these ontologies into the CBNs learned from data, we established that (1) ontologies are sources of causal mechanisms and causal knowledge; which can be extracted in the form of ordered-variable pairs; (2) ordered-variable pairs can be used to orient CBNs learned from data and produced new CBN structures; and (3) a methodology is possible for combining Bayesian reasoning with ontological knowledge within a CBN.

We obtained our potentially causal knowledge from AMOs in a systematic way, but it is a manual process. There are other methodologies for exploring AMOs for causal information. Currently, we are pursuing the use of general-purpose AI for mining ICD-10-CM and other ontologies for associations and ordered variable pairs.

Finally, we acknowledge that there are other sources of expert knowledge such as structured literature [22, 36, 55], randomized controlled trials [45, 75], and intuition and insights from clinicians. These can be used in conjunction with AMOs to further inform a CBN.

## 5 CONCLUSIONS

There are a variety of algorithms that are able to learn CBNs from observational patient data. However, none of them inherently considers any prior knowledge or expertise that may be available for a disease. An algorithm, and the CBN that is learned, can be improved significantly by considering prior sources of knowledge if the algorithm is modified appropriately.

In terms of STAR*D and other observational datasets, observational studies are not always designed with randomization and causal inference in mind. Building causal graphs from this kind of data is difficult-not because algorithms are hard to understand or implement, but because analysis of data is only partially sufficient to establish a causal relationship. Algorithms and processes to generate a causal graph can be very sophisticated; they must consider a variety of facets, such as statistical tests, logic tests, experimentation, and domain knowledge. Even with the best conditional probability statistic, supporting contextual research, and sophisticated computer algorithms, there is a limit to how much information can be obtained from observational data.

Traditionally, a time-based sequence of events has been used to infer causality and disease progression. However, we can also obtain prior knowledge from one or more ontologies. This source of prior knowledge can be used to orient the arcs in a CBN, resulting in a network with overall higher conditional probabilities, new significant relationships among symptoms, and the elimination of weaker edges. We have elaborated a method by which a Causal Bayesian Network is augmented with ontological knowledge from multiple authoritative ontologies so causal relationships are strengthened.

The resulting network provides insight into the causal relationships expressed in the data and takes advantage of the expertise and knowledge contained in the AMOs. Inferring causality from a CBN does not exist in a vacuum. Statistical analysis, creating a causal model from observational data, analysis of that model to infer causality, prior randomized trials and expertise, and definitions in a biomedical ontology all play a role in creating a model for causal inference. Uncertainty is present at all steps of this process, much as it is present in prior, posterior, and likelihood in Bayes Theorem.

In this article, we have developed a method to extend the analysis of modeling observational data by using ontological expertise as prior knowledge. Using AMOs such as MedDRA, ICD-10-CM, and SNOMED CT, we have extended and improved upon an unmodified baseline CBN. These improvements include not only stronger conditional probabilities, but new causal relationships that can be substantiated in existing epidemiological literature.

Moving forward, we intend to explore the application of this methodology to additional patient symptom datasets, including the Icahn School of Medicine's Asthma Mobile Health Study [17] for symptoms from patients of asthma and the National Alzheimer's Coordinating Center's ${ }^{14}$ symptoms of patients of Alzheimer's Disease. These additional patient datasets, combined with additional AMOs, will further establish ontologies as an informative source of prior information for orienting causal Bayesian networks.

# ACKNOWLEDGMENTS 

We thank Dr. Farrokh Alemi at George Mason University's College of Health and Human Services, for advising us on measuring predictive accuracy and comparative analysis.
