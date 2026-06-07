# Reusability of Bayesian Networks case studies: a survey 

Nikolay Babakov ${ }^{1}$ (D) $\cdot$ Adarsa Sivaprasad ${ }^{2}$ (D) $\cdot$ Ehud Reiter ${ }^{2}$ (D) $\cdot$ Alberto Bugarín-Diz ${ }^{1}$ (D)<br>Accepted: 13 January 2025<br>(c) The Author(s) 2025


#### Abstract

Bayesian Networks (BNs) are probabilistic graphical models used to represent variables and their conditional dependencies, making them highly valuable in a wide range of fields, such as radiology, agriculture, neuroscience, construction management, medicine, and engineering systems, among many others. Despite their widespread application, the reusability of BNs presented in papers that describe their application to real-world tasks has not been thoroughly examined. In this paper, we perform a structured survey on the reusability of BNs using the PRISMA methodology, analyzing 147 papers from various domains. Our results indicate that only $18 \%$ of the papers provide sufficient information to enable the reusability of the described BNs. This creates significant challenges for other researchers attempting to reuse these models, especially since many BNs are developed using expert knowledge elicitation. Additionally, direct requests to authors for reusable BNs yielded positive results in only $12 \%$ of cases. These findings underscore the importance of improving reusability and reproducibility practices within the BN research community, a need that is equally relevant across the broader field of Artificial Intelligence.


Keywords Bayesian networks $\cdot$ Probabilistic graphical models $\cdot$ Reproducibility $\cdot$ Reusability

## 1 Introduction

Although Bayesian Networks (BNs) find application in diverse domains that require analysis under conditions of uncertainty (e.g., radiology [1], agriculture [2], neuroscience [3], construction management [4], medicine [5] etc.), many papers dedicated to the application of BNs do not provide enough technical information about BNs. This makes it

[^0]difficult for other researchers to reuse the results of these studies. This is especially critical for the BNs built, at least in part, using knowledge elicitation from human experts because the reproduction of human-based BN collection may be very difficult. In this paper, we perform a structured survey focusing on the reusability of BNs to raise awareness about this issue in the community and highlight the importance of reusability and reproducibility principles in this research area.

Our survey is an extension and update of the previous results presented in [6], where authors investigated the issue of the lack of BN adoption in medical practice. This study analyzed 123 BN-related papers published between 2012 and 2018 in the medical domain. The researchers found many pieces of evidence indicating that the BNs developed and presented in such papers are rarely adopted for real clinical use.

In our paper, we extend the scope of BN applications considered in [6] to all fields of application. In [6], authors considered multiple aspects of the papers, such as the BN development process (repeatability of the process, source of variables, development tool), usefulness (implementation, generalizability, impact, etc.), the aim of BN (type of decision support), etc. While the insights collected are certainly important, we argue that there is a shorter list of BN properties that corresponds to the minimal requirements necessary to ensure the reusability of a developed BN. Thus, we ana-


[^0]:    1 Centro Singular de Investigación en Tecnoloxías Intelixentes (CiTIUS), Universidade de Santiago de Compostela, Santiago de Compostela, Spain
    2 Department of Computing Science, University of Aberdeen, Aberdeen, UK

lyze the papers related to the usage of BN in use cases not limited to the medical domain, collecting further information about them:

- Is the source of the BN's variables, structure, and Probability Distribution, clearly indicated?
- Has the correctness of the developed BN's performance been validated?
- Does the paper have enough information (either in the paper's text or in the supplementary materials) to make the developed BN fully reusable - BN structure, variable names, variable states, Probability Distribution?

We initially gather the necessary information from the content of the paper or its supplementary materials, which may include venue-specific supplements, appendices, or findable external links referenced within the paper. If we are unable to find the required information in these sources, we reach out directly to the authors to obtain it.

The remainder of this paper is organized as follows. Section 2 introduces the basic theory of BNs. Section 3 describes the motivation of this survey in more detail. Section 4 presents the methodology of the survey. Section 5 outlines the results of the survey. Finally, we discuss the obtained results in Section 6 and deliver our recommendations to the BN research community in Section 7.

## 2 Preliminaries

### 2.1 Bayesian Networks

A BN is a directed acyclic graphical (DAG) model that represents relationships between variables (nodes) of the graph [7]. It allows for the representation of complex joint probabilities in a more convenient graphical view. Fundamentally, a BN consists of two principal parts: qualitative and quantitative [8].

The qualitative part refers to the set of variables (nodes) representing the factors analyzed in a BN (these can be either discrete with multiple states or continuous) and the directed arcs that encode probabilistic (in)dependence relationships. While these arcs can sometimes be interpreted as causal relationships, particularly in causal models [7], many datadriven BNs generated by structure learning algorithms treat the direction of arcs as indicators of conditional probabilistic dependence rather than strict causality.

The quantitative part refers to the parameters of a BN or its Probability Distribution. Probability Distribution is normally presented in the form of Conditional Probability Tables (CPTs), representing the conditional probabilities of each possible combination of the discrete states between par-
ent and child nodes. For continuous variables, Probability Distribution may take other forms, such as parametric representations like mean and variance in a Bayesian conjugate distribution. In this work, we refer to any representation of conditional probabilities as Probability Distribution. Figure 1 provides a well-known example of a simple BN [9], which describes a toy scenario involving possible causes (Pollution: Low or High, and Smoker: True or False) and consequences (XRay: Positive or Negative, and Dyspnoea: True or False) of Lung Cancer.

The joint probability of all variables in a BN can be calculated using the chain rule of probability, leveraging the conditional independence encoded in the BN structure. Specifically, the joint probability $P\left(X_{1}, X_{2}, \ldots, X_{n}\right)$ is given by:
$P\left(X_{1}, X_{2}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \operatorname{Parents}\left(X_{i}\right)\right)$,
where Parents $\left(X_{i}\right)$ are the parent nodes of $X_{i}$ in the BN. This factorization significantly reduces the complexity of representing joint probabilities, especially in high-dimensional systems.

Efficient inference in a BN, such as calculating marginal probabilities or performing evidence propagation, relies on message-passing algorithms. In the variable elimination method, factors corresponding to the CPTs are sequentially summed or multiplied based on the query variables and evidence provided. For more complex queries or real-time inference, the Junction Tree Algorithm is often employed, where the BN is converted into a clique tree, and belief propagation is performed by passing messages between cliques [10].

In this paper, we also consider Dynamic Bayesian Networks (DBNs). The concept was first proposed in [11] as an extension of BNs capable of representing dynamic systems changing over time. Except for the initial BN structure (e.g., $C \rightarrow B \leftarrow A$ ) DBN also contains the transitional structure (e.g., $A_{t-1} \rightarrow A_{t}, B_{t-1} \rightarrow B_{t}$, where $t$ refers to the timestep).

### 2.2 Methods for structure and parameters learning in Bayesian Networks

BNs can be constructed either from data using structure learning algorithms [8, 12-14] or by knowledge elicitation from human experts [15].

When the data for the particular task is not available, experts' knowledge could be the source of information to construct the BN. The discussion between experts may be performed in a non-structured way of face-to-face brainstorming sessions; however, there are also more formalized

Fig. 1 A BN for the lung cancer problem described in [9]![img-0.jpeg](img-0.jpeg)
discussion approaches based on the Delphi protocol [16, 17], which involve engaging multiple experts in discussing certain problems asynchronously and anonymously under the review of the facilitator. This technique was first used in the specific task of BN structure and parameter elicitation in [18]. Delphi protocol usage was further expanded to the whole pipeline of BN structure elicitation in the BARD system [19]. The effectiveness of this method was proved in [20].

Otherwise, if the data are available, the BN structure and parameters can be learned by means of various algorithms.

The Max-Min Hill-Climbing algorithm (MMHC) [21] is frequently used for BN structure learning from data [22, 23]. The algorithm starts either from an empty graph or from a DAG corresponding to an initial hypothesis. The search is performed by adding or deleting edges in a BN's structure to maximize a score that measures how well a current BN's structure is able to describe the given data set. A frequently used scoring method is the Bayesian Information Criterion [24] - a log-likelihood score with an additional penalty for network complexity to avoid overfitting.

The K2 algorithm [25] is also used for BN construction [26-28]. The K2 algorithm uses a given prior ordering of nodes as input. Its general objective is to maximize the network's posterior probability given the data. At the first
step of the algorithm, the candidate parents for a given node are defined as an empty set. Then, the algorithm visits each node according to the given prior node ordering and greedily selects nodes for adding to the parent set of the node. The algorithm is repeated recursively until either the maximum number of parents for each node is reached, there are no more legal parents to add, or no parent addition improves the score [29].

Once the BN nodes and arcs are defined, the BN parameters can also be calculated from the data. Maximum Likelihood Estimation (MLE) is used very often for this aim [3032]. This is a straightforward approach that simply estimates the probabilities from the observed frequencies. The Expectation Maximization (EM) algorithm [33], designed to perform well when the training data has missing values, is also frequently used for BN parameter estimation [3436]. The EM algorithm works by iteratively estimating the parameters of a BN until convergence is reached. In each iteration, the algorithm performs two steps: E-step computes the expected sufficient statistics of the hidden variables given the observed data and current estimates of the parameters, and the M-step updates the estimates of the parameters by maximizing the expected log-likelihood of the observed data given the expected sufficient statistics computed in the E-step.

Overall, for both expert-driven and data-driven approaches to BN structure and parameter learning, many factors could be difficult to reproduce. In the case of expert-driven approaches, the thorough tracking of the discussion of the selected experts seems almost unfeasible, especially if the discussion is performed in non-formalized brainstorming sessions. In the case of data-driven algorithms, their reproduction could be possible, but this will require the availability of the data and the proper report of various hyperparameters that can significantly influence the final results.

### 2.3 The need for Bayesian Networks in real-life applications

BNs have emerged as a powerful tool for modeling uncertainty and causal relationships in complex systems, making them indispensable in many real-life applications. Traditional statistical methods and machine learning models often fall short when dealing with incomplete data, dynamic systems, or scenarios requiring explicit representation of probabilistic dependencies. In contrast, BNs offer a structured approach to integrate prior knowledge with observed data, enabling inference, prediction, and decision-making under uncertainty [7].

One critical gap addressed by BNs is the ability to model causal relationships explicitly. Unlike correlationbased methods, BNs provide a framework for encoding and reasoning about causality, allowing domain experts to incorporate knowledge about the system's behavior [37]. For instance, in medical diagnostics, BNs have been used to predict disease progression by integrating patient history, symptoms, and test results while accounting for the causal interplay between variables [9].

Another unique strength of BNs is their capability to handle incomplete data. Real-world datasets often suffer from missing values or noisy measurements. BNs allow for probabilistic inference to estimate missing information or predict outcomes despite incomplete datasets [38]. This makes them particularly valuable in domains like environmental modeling, where data collection is often constrained by physical or financial limitations [39].

Furthermore, BNs excel in scenarios where data is scarce and expert knowledge needs to be incorporated. For example, in engineering systems, BNs are used to assess reliability and manage risks by combining historical failure data with expert input [40]. Similarly, in agriculture, they enable decision support by integrating knowledge about crop yield factors with observed environmental data [2].

Despite their strengths, BNs remain underutilized in many domains due to challenges such as scalability and the effort required to construct and validate models. Addressing these challenges offers a significant opportunity for future research. Our study seeks to highlight the reusability of BNs to encourage broader adoption across fields, ensuring that the knowledge encoded in these networks can benefit a wider range of applications.

## 3 Motivation: should BNs be reusable?

The general requirement for scientific papers to be reproducible seems pretty natural. However, in this section, we provide an explicit motivation for this requirement applied to the papers dedicated to the usage of BNs.

### 3.1 Reproducibility crisis

The reproducibility crisis refers to the widespread failure to replicate the results of experiments and studies [41]. It is a problem that affects many fields, including various areas of AI [42-46]. There are limited studies on reproducibility in the field of BNs. In [47], the reproducibility of a naive BN parameter learning algorithm is studied. In [6], the reproducibility of BN is studied among other objectives for the papers limited to the medical domain.

To address the issues resulting from the reproducibility crisis, FAIR data principles [48] ${ }^{1}$ were proposed. FAIR is an acronym for "Findable", "Accessible", "Interoperable", and "Reusable". These principles aim to ensure that research data can be easily located by providing thorough metadata and persistent identifiers, ensuring the data are Findable. For data to be Accessible, clear guidelines must be provided for access while considering confidentiality requirements. The Interoperability aspect requires data and metadata to adhere to widely accepted standards, allowing them to be integrated and used across various platforms. Finally, the Reusability of data ensures that they are well-documented, clearly licensed, and available for future research under specified conditions.

### 3.2 The notion of reusability: necessary and sufficient conditions

The problem of reproducibility is frequently discussed in AIrelated literature (see Section 3.1). In this paper, we introduce and distinguish between two terms: reproducible BN and reusable BN, as they represent different levels of information and usability requirements.

Definition 1 A Reproducible Bayesian Network is a Bayesian Network presented in such a way that the entire process of its creation, including the data collection, structure and parameter learning methods, expert knowledge elicitation, can be repeated to securely achieve the same results as reported in the original paper.

[^0]
[^0]:    ${ }^{1}$ https://snd.se/en/manage-data/prepare-and-share/FAIR-dataprinciples

Definition 2 A Reusable Bayesian Network is a Bayesian Network presented with sufficient technical details such that it can be directly used by another researcher or practitioner, enabling its execution on their system without needing to repeat the original creation process.

While reproducibility and reusability are related concepts, this paper focuses on reusability instead of reproducibility. This focus is motivated by the fact that ensuring reusability is a less stringent requirement for the papers studied. Achieving reproducibility often demands a highly detailed presentation of the BN collection process, which is not always feasible in published works. In contrast, reusability can be ensured with higher-level information, provided that ready-to-use details, such as network structure, variables, states, and conditional probabilities, are available for reuse.

Moreover, reproducing the full design cycle of BN collection can be quite challenging in many cases, particularly when expert knowledge elicitation or domain-specific data is involved. Reusability, therefore, serves as a more practical and impactful standard for many real-world applications, as it allows researchers and practitioners to integrate predeveloped BNs into their workflows without the need for complete reconstruction.

Once developed, BNs may be useful for similar or related tasks. If a researcher or industrial specialist wants to integrate the results of the published paper into their work, the BN presented in a paper still has to meet some conditions that are either necessary or sufficient. In our work, we refer to these conditions as reusability.

We define the necessary condition of reusability as follows:

Definition 3 A Necessary Condition of Reusability of a Bayesian Network is the availability of all essential parts of a BN in the paper or its supplementary materials, enabling researchers to reuse the developed BN by running it on their own systems. This requires that all the following components of the BN are properly defined:

- Variables: A complete list of unambiguously interpretable variables and their corresponding states.
- Arcs: A full structure of the developed BN that clearly defines the probabilistic relationships between variables.
- Probability Distribution: Conditional probabilities assigned to all variable nodes corresponding to the BN's structure.

We also define the sufficient condition of reusability as follows:

Definition 4 A Sufficient Condition of Reusability of a Bayesian Network includes the necessary condition and extends beyond it. To meet this condition, the paper must also provide clearly defined sources for the BN's components (e.g., variables, arcs, and Probability Distribution), specifying whether these are derived from expert knowledge, literature, or data. Additionally, validation reports must demonstrate that the BN performs as intended for its designated task. Such reports may include, but are not limited to, case studies, statistical metrics (e.g., accuracy, ROCAUC), or sensitivity analyses.

Refer to Fig. 2 for visualization of necessary and sufficient conditions of reusability.

Both conditions of reusability align with the FAIR data principles and the specific characteristics of BNs. For a BN's Probability Distribution, arcs, and variable names and their states to be technically reusable (i.e., to meet the necessary conditions of reusability), they must be findable and accessible through any means, such as being available in the paper, supplementary materials, repositories, or any other clearly defined resources.

In our reusability analysis, we do not factor in the potential difficulty of reusing the provided information. For instance, while reusing a ready-to-run file is significantly easier than extracting probability information from a Conditional Probability Table presented as a table, we consider any case where the necessary information is available-regardless of its format-as a positive case for reusability.

Additionally, the BN components must be interoperable, which is typically achieved by using clear and consistent state names. Finally, the validation of the BN's performance, along with the sources for its components, should be findable and accessible within the paper or in clearly designated supplementary materials.

To clarify, by "source" of variables, arcs, and Probability Distribution, we refer to the origin of these components as

Fig. 2 Visualization of necessary and sufficient conditions of BN reusability. "PD" stands for Probability Distribution
![img-1.jpeg](img-1.jpeg)

derived from data, expert knowledge, or literature. In cases where the data is generated from expert-derived simulations, such as toy examples or artificial data, we classify the source as "expert" since the underlying source is an expert's subjective belief. Furthermore, if a certain part of the BN (or the entire BN) is derived independently of both standalone data and standalone expert knowledge (not directly related to each other), we treat such cases as a combination of data and expert sources.

### 3.3 Limitations of reusability

The proposed notions of necessary and sufficient conditions of reusability are designed to ensure the easy and reliable reuse of BNs developed by other authors. However, there are numerous corner cases where a BN may technically meet these conditions yet offer limited practical value in certain contexts. Conversely, the lack of reusability does not always imply a negative judgment, as some BNs may still hold significant utility despite their limited generalizability. In this section, we highlight such potential corner cases and explore the nuanced limitations of the proposed reusability framework.

One issue lies in the improper use or over-reliance on specific design patterns, which may not be applicable or necessary in other projects. However, certain BNs can still be highly useful despite their reliance on specific design patterns. This represents a case where the notion of nonreusability does not imply a negative judgment but rather highlights a practical limitation. Such limitations should ideally be explicitly communicated by the authors to set appropriate expectations and guide the proper application of the BN in its intended context.

Variables with poor semantics can also introduce confusion, particularly when variables do not correspond to observable phenomena. Naming patterns may appear clear in terms of wording but lack correctness or relevance from a domain knowledge perspective, complicating reuse and making it difficult for others to accurately interpret the BN's components.

Another issue arises from unmatched levels of abstraction, where nodes represent concepts that are either too specific for a given domain or too abstract for use in other contexts. For instance, a variable indicating the state of a system component labeled as "faulty" might be too abstract if it only captures a binary state ("faulty" or "not faulty") without specifying the type or cause of the fault. Conversely, a variable labeled as "rare fault specific to mechanism X" might be too specific, applying only to a niche subset of mechanisms and limiting its generalizability. In such cases, domain specialists may need to intervene to identify and address these nonreusable abstractions. They can refine the variables and their corresponding probabilities, ensuring an appropriate balance between generality and specificity, thereby enhancing the reusability of the BN.

Furthermore, BNs might carry unknown or unspecified assumptions that were made during their development. For example, a BN could be tailored to specific needs based on stakeholder decisions, leading to approximations such as the removal of arcs deemed irrelevant for one application. Similarly, probability distributions might be simplified using canonical forms like noisy-Or or noisy-Max when precision was less critical in the original application.

Trustworthiness or credibility of the information encoded in a BN is another concern. A BN derived from unreliable data may still pass verification tests if it accurately reflects the incorrect joint probability distribution. An expert might validate or accept such a BN based on reasonable results in specific cases. However, in domains where the provenance, trustworthiness, or credibility of the information play a critical role, such a BN might fail to provide reliable outcomes. While a BN may technically satisfy the conditions for reusability, its practical utility could be compromised in settings requiring rigorous standards of information quality

In this paper, we do not address the aforementioned issues, as identifying and resolving such problems often requires indepth domain-specific expertise, which is beyond the scope of this study. Given that this work focuses on surveying the reusability of BNs across a broad range of domains, it is not feasible to evaluate domain-specific nuances or design choices comprehensively. Our goal is to provide a general framework for reusability applicable across diverse fields, leaving detailed domain-specific evaluations for future, more focused research. By doing so, we aim to offer a high-level perspective while acknowledging that domain specialists are essential for addressing issues such as poor semantics, naming conventions, or unmatched abstractions in specific applications.

### 3.4 Existing re-usage examples

BNs can be reused for further research or industrial applications, either as-is or by inheriting some significant parts from the existing BN to develop a new one. For instance, in [49], the BN used to instantiate probabilities is identical to that described by [50]. In [51] the final BN underwent multiple iterations of development from the initial BN presented previously in [52]. Chockalingam et al. [53] referred to [54, 55] and several other BN-related papers when defining the variables. In [56] the previously developed BN [57] was used for the analysis of the patient's data. Similarly, in [58] the new BN was based on the one previously developed in [59]. Most of the aforementioned cases are related to the re-usage of their materials by the same authors; however, we believe that it is very likely that the BN could be reused by other researchers as well, if the BN is properly open-sourced.

These are just a few examples of when the reusable BN is inherited, either partially or completely, in subsequent works. The potential objection to obligatory reusability could be that sometimes the developed BN is overly calibrated to specific data, making the Probability Distribution highly sensitive to small changes in variable values. However, in research and especially in the real-life application world, it is impossible to foresee what exactly can be useful for the potential reader. In our view, open-sourcing the BN or, at least, providing enough details favoring its reusability significantly increases the value and future impact of the published papers.

### 3.5 Potential re-usage examples

As it was shown above, new works can benefit from fully reusable BNs in different ways. To sum it up, a BN can be used as-is for performing inference for some further downstream tasks. Alternatively, one may update the Probability Distribution either with new knowledge or with any of the parameter estimation approaches if new data appears. Finally, the structure of a BN may be modified slightly for a specific task, with or without partially inheriting the Probability Distribution of the existing BN.

In the case of using the developed BNs for predictions, textual [60-64] or visual [65] explanation techniques can also be used, which may allow domain specialists who do not possess deep knowledge of the BN theory to benefit from using the explainable capability of BN inference.

## 4 Methodology

This survey complies with the recommendations of the PRISMA 2020 [66] methodology. We use Scopus, Web of Science, and IEEE Xplore scientific databases for our search. The main motivation for selecting these particular databases is that they cover a significant number of papers from various disciplines. Scopus includes more than 90 million papers from more than 27 thousand journals. ${ }^{2}$ Web of Science includes more than 34 thousand journals, books, and proceedings with over 200 million records. ${ }^{3}$ IEEE Xplore includes more than 4 million conference papers. ${ }^{4}$

We run the database search by the papers' abstracts using the following query: ((bayesian AND network) OR ( probabilistic AND graphical AND model)) AND (application OR case AND study ). Note that the exact syntax of the queries may vary slightly according to the database requirements, but the keywords are similar in all queries. The formulation

[^0]of the query is derived from [6]. The first part of the query ("bayesian network" and "probabilistic graphical model") points to two different references to BNs in scientific literature. The second part ("application" or "case study") formulates the possible references to the application of BNs to certain tasks.

As discussed in Section 1, this survey extends the results obtained in [6], thus we extract the papers dated from the next year after the last one covered in [6] (2019) till the last year available to us by the date of performing this survey. Since our survey was performed in February 2023, we extracted the papers from 2019 to 2022, inclusive.

We apply the following criteria for the inclusion and exclusion of the papers from the survey. The paper is included if it is written in English and dedicated to solving the specific task using a BN as a main tool. We exclude the paper if it is dedicated to introducing any BN-related method (e.g., structure learning) or if BN is used together with other approaches or not used at all (e.g., some alternative Bayesian methods such as naive Bayes or Bayesian neural networks are used instead).

After the extraction of the papers, we drop the duplicates, and filter them first by abstract and title, and then by the content of the whole paper. The selected papers are used for further analysis. The particular data we extract from the selected papers corresponds to all requirements of sufficient conditions of reusability (see Fig. 2): the sources of all BN parts, BN correctness validation, and the availability of all parts of BNs. Figure 3 shows the literature selection diagram according to the described methodology.

If the BN introduced in the paper included in the final scope of the survey turns out not to meet the necessary condition of reusability, we subsequently contact the authors, aiming to request the reusable version of the constructed BN. We use exclusively the email addresses that are provided in the text of the paper. If, for some reason, no email addresses are available, we use Google Scholar to check the author's last publications. If any of the authors has an account in this system, we use it to contact them; otherwise, we assume that there is no feasible way to find a way to contact the authors of the paper. We send two email messages to the authors. The first one contains the general introduction of the project in terms of which we perform this research, describes what parts of the information necessary for BN re-usage have not been found, and asks for these parts. If we do not receive the reply within one week, we send a reminder. After two weeks from the first request date, we assume that we do not get a reply.

## 5 Results

### 5.1 Preliminary analysis

The initial query to the databases yields 6705 papers. After deduplication, we drop 2537 papers and read the titles and


[^0]:    ${ }^{2}$ https://blog.scopus.com/posts/scopus-now-includes-90-million-content-records
    ${ }^{3}$ https://clarivate.libguides.com/librarianresources/coverage
    ${ }^{4}$ https://ieeexplore.ieee.org/Xplorehelp/overview-of-ieee-xplore/ about-ieee-xplore

Fig. 3 Literature selection diagram
![img-2.jpeg](img-2.jpeg)
abstracts of the rest. This results in the disregarding of 3948 papers due to the inclusion and exclusion criteria discussed in Section 4: many papers use BN together with other tools, use different derivatives of BN (e.g., Fuzzy BN [67] or Generalized BN [68]), introduce various BN-related methods, or do not meet other criteria. We also read the full text of the remaining 220 papers and disregarded 73 more due to inconsistency with the inclusion criteria. Finally, we consider 147 papers for further analysis. See Fig. 3 for the literature selection diagram. The detailed statistics of all analyzed papers are available in Appendix A Table 5 and in the Supplementary Materials.

The screening of paper titles and abstracts for further inclusion or exclusion and the subsequent feature extraction were performed by two authors. To mitigate potential risks of bias during these processes, we calculated Cohen's kappa agreement coefficient [69], which measures inter-rater reliability by considering the level of agreement between annotators while accounting for agreement occurring by chance. The kappa score is calculated as $\kappa=\frac{P_{o}-P_{e}}{1-P_{e}}$, where $P_{o}$ is the observed agreement and $P_{e}$ is the expected
agreement by chance. A score of $\kappa=1$ indicates perfect agreement, $\kappa=0$ corresponds to no agreement beyond chance, and negative values suggest systematic disagreement.

For the title and abstract screening phase-where papers were considered for detailed analysis-the kappa score was 0.75 , indicating substantial agreement. During the feature extraction phase-where specific values of study features were assigned to the included papers-the kappa score was 0.68 , reflecting moderate agreement. In cases of disagreement, the annotators discussed the discrepancies jointly to arrive at a final decision. This process ensured consistency and minimized bias in the study.

### 5.2 Clarity of sources and validation

Now we proceed to analyze the properties directly related to reusability. Our findings in this regard are shown in Fig. 4.

Figure 4a shows the statistics of the sources of BN variables, arcs, and Probability Distribution. From this plot, it is clear that the data alone or in combination with experts'

![img-3.jpeg](img-3.jpeg)

Fig. 4 a)c) Analysis of sources used for the development of the different parts of BNs introduced in the papers included in the survey. c) Statistics of the BNs validation (we show only higher diagonal values of the co-occurrence matrix for ease of value perception)."ProbDist" stands for Probability Distribution
knowledge are used very often for BNs parameter elicitation ( $36 \%$ and $17 \%$ respectively). Experts' knowledge alone is a frequent choice ( $30 \%$ ) for creating arcs.

Figure 4 b shows the statistics of how often the developed BNs are validated. 113 papers ( $77 \%$ ) properly report at least one form of validation of the correct performance of the developed BN. The most frequent choices for the validation approach are testing BNs with some known scenarios or case studies [36, 70, 71], statistical metrics (accuracy [72], AUC-ROC [73], etc.), and sensitivity analysis [74]. Sometimes the BNs are evaluated by experts [75, 76].

Figure 4c shows the statistics of the combination of the sources, regardless of what BN part they are dedicated to. The most frequent combination choice uses data accompanied by experts' knowledge. From Fig. 4a,c, we can also see that the sources of BN parts are not reported in around $20 \%$ of papers.

In general, we observe that most authors report the results of validation and the sources used to construct the BN parts.

### 5.3 Analysis of necessary and sufficient reusability conditions

This subsection contains the main findings of our survey that are illustrated in Figs. 5 and 6.

First, we analyze the necessary reusability conditions for all studied papers. Figure 5a shows the availability of information necessary for the re-usage of all principal parts of the BN: the BN scheme, variable names and states, and Probability Distribution. Proper reporting of the BN scheme is performed in 144 papers ( $98 \%$ of all papers). In the remaining $2 \%$, the BN was either shown only partially or not shown at all. Even though the BN scheme is expected to have the full names of variables and the full list of the states corresponding to them, this is not always the case, which results in the lower availability of variable names and states in contrast to a full BN scheme: 127 ( $86 \%$ ) and 95 ( $65 \%$ ) respectively. This may happen because the variable names are presented as abbreviations that are deciphered in the rest of the paper, either partially or not at all. The Probability Distribution is normally not available for reuse. In the majority of cases, Probability Distribution is available either partially - 26 papers (18\%), which also does not make BN re-usage possible, or not available at all - 91 papers ( $62 \%$ ). Three analyzed papers have Probability Distribution, but their probability values are not consistent with the other information about the BN (in such cases, the Probability Distribution is shown as "Not available" in Fig. 5a).

To summarize the detailed findings in Fig. 5a we aggregate the results within all principal components of BN in Fig. 5b,

Fig. 5 a) Analysis of reusability of certain parts of the BNs developed in the reviewed papers. b) Analysis of the technical reusability of the BNs. "ProbDist" stands for Probability Distribution
![img-4.jpeg](img-4.jpeg)

Fig. 6 Analysis of BN
reusability with respect to the BN part source. The source information is aggregated by the following logic: if any source is missing or collected with experts, then the paper source is aggregated to the "no" or "experts" value correspondingly, and all other cases are mapped to the "data" value. The scope refers to the principal parts of the BN corresponding to qualitative (variables and arcs), quantitative (Probability Distribution), and overall (all three parts). The reusability information is assumed not to be available if any of the BN parts in the scope do not have enough information to be reused. Note that we merge "literature" into "experts" for compactness of presentation, as far as this was quite a rare case
![img-5.jpeg](img-5.jpeg)
which corresponds to the necessary condition of reusability. If any of these components are either unavailable or partially available, we assume that the BN from the given paper does not meet the necessary condition or, simply speaking, cannot, in fact, be reused. Thus, only 26 papers ( $18 \%$ ) provide thorough information to let the reader reuse the BN developed in the paper. In 113 papers ( $77 \%$ ) at least one of the principal BN parts is missing, so the BN is not reusable. Still, there are 7 papers ( $5 \%$ ) that had special disclaimers in the paper text that the data could be requested, so we consider them separately.

In Fig. 6, we analyze the reusability of the BNs w.r.t. their data sources. In particular, we analyze how often the whole BNs or their qualitative or quantitative parts, collected by either experts' knowledge, data, or without a clear indication of the sources, have or do not have all the necessary information to be reused. We assume that the reusable data are available if it can be found in the paper or in the supplementary materials. To make the plots more compact, we aggregate the information about the data source as follows:

- No. If any source within the scope is missing.
- Experts. If any source within the scope is related to experts' knowledge elicitation.
- Data. The rest of the papers (these are either completely data-based BNs or a small amount of literature plus data ones).

The idea of aggregation is that if any part of the initial information is missing, then a reader will not be able to reuse the BN unless it is available in a reusable form. Similarly, if any part of the source is related to the expert's knowledge, reproduction is also hardly possible, so potential re-usage only relies on the thorough BN-related information for its re-usage in the paper. This analysis is done in three scopes: qualitative, quantitative, and overall.

Figure 6a shows that the qualitative parts of the developed BNs are open-sourced in the reusable form, quite often if their pipeline includes experts' knowledge elicitation. The variables, their states, and the arcs collected by means of data are also normally open-source. The rest of the papers, which have some inconsistencies in indicating the sources of the qualitative part of their BNs, open-source BN parts only in $50 \%$ of cases.

Figure 6b provides a similar point of view to the quantitative part of the BNs i.e., to the open-sourcing of Probability Distribution. A lot of papers do not have their BNs' Probability Distribution open-sourced. This is crucial, especially for the cases where the probabilities were thoroughly or partially elicited from the experts' knowledge ( $78 \%$ of 67 papers do not have Probability Distribution open-sourced) or where the source of the probabilities was not clear ( $92 \%$ of 24 papers) do not have Probability Distribution open-sourced.

Figure 6c summarizes the findings about the sources and reusable parts of the whole BN structure (variables, arcs,

and Probability Distribution). Again, in such critical cases as when some sources of the collected BN parts are unclear or rely on the experts' knowledge, the proportion of reusability is rather poor: $83 \%$ of 75 (at least partially) expert-driven papers and $88 \%$ of 49 papers with incomplete BN parts sources do not have enough information to reuse them from the content of the paper.

Finally, Fig. 6d takes into account all requirements of reusability that form a sufficient condition of reusability: clarity of sources, validation, and availability of all essential BN parts to be launched. Of the 147 papers included in the survey, only 15 (10\%) meet all requirements.

Figure 7 shows the fields of the BNs application and the corresponding statistics of meeting necessary and sufficient conditions of reusability of the BNs presented in corresponding papers. The categorization of fields of application was performed manually by the same authors who conducted the rest of the review. These labels were designed to generalize the areas of BN application in a balanced manner-maintaining a level of detail sufficient to highlight domain-specific nuances while avoiding an excessively granular division into an impractically large number of categories. Complex engineering systems are the most frequent field of BN application (39 papers). It seems natural because BNs are useful for representing the processes in plants [27, 7779], turbine systems [80, 81], telecommunication [82, 83] etc. Medicine turns out to be the second most popular field of application (22 papers). There are also some other technical fields of application like transportation [84-86], natural resources utilization [79, 87], construction [88, 89] or manufacturing [90, 91] that form a big cluster, so they are shown separately. The most frequent non-technical fields of BN applications covered in our survey are education [32, 92] and natural sciences [93, 94].

Figure 7 reveals that, across most fields, the issue of reusability is largely overlooked. In many spheres, the majority
of papers do not address or meet the conditions necessary for BN reusability. Notably, the highest number of papers with reusable BNs is found in the engineering systems domain, but even here, they represent only a small fraction of the total number of papers in this field. Furthermore, in certain fields-such as natural resources and manufacturing-not a single paper meets the necessary condition of reusability.

### 5.4 Authors contact analysis

It may be assumed that even if the BN is not fully reusable from the pure paper content or its supplementary materials, it is still possible to request the necessary data from the authors directly. We do so according to the methodology described in Section 4. The results of this process are shown in Tables 1 and 2. Recall that we found all the details necessary for the reusage only for 26 papers, so we considered contacting the authors of the rest of the 121 papers.

As it can be seen in Table 1, the overall reply rate was rather high - the requests regarding only 70 papers ( $58 \%$ of the ones with non-reusable BN) were not replied to. However, among those who replied (the other 51 papers), only in 15 cases, the authors were able to provide us with the reusable BN. The authors of two papers indicated that the information was private, so they could not share it. For further analysis, we distinguish authors' replies by positive and negative response types. The aforementioned two scenarios (BN provided after request, and the author could not do that because of privacy) are considered positive.

The negative response is any that did not result in the reusable BN on our side. There are several main reasons for that, except for the simple absence of a response within two weeks after the request was sent, which has been discussed above. First, some authors replied and indicated that they needed some time, but after waiting for two more weeks

Fig. 7 Analysis of the fields of BNs application
![img-6.jpeg](img-6.jpeg)

Table 1 Detailed results of contacting the authors of the papers that do not have the BN in a fully reusable form


'Abs #' refers to the absolute number of papers, and ' $\%$ ' is the corresponding percentage
after their reply, we assumed that this request was not replied to as well. Second, some authors were not able to provide the BN at all ('replied but BN not provided') or provided incomplete information that did not allow reusing the BN ('replied but BN not reproducible'). Finally, in several cases, email delivery failed for some reason, or we could not find the authors' email addresses even after using Google Scholar.

Thus, even though almost half of the authors replied to our requests, only a few of them were able to provide the information necessary to reuse the BN they developed in terms of their work on our side. This results in only 18 papers (or $14 \%$ of all requests) that could be assumed to yield positive results for the request (see Fig. 2).

There have already been some studies on reproducibility that include contacting authors and asking them for some details about their papers. For example, in [43] the authors studied the reproducibility of human evaluation experiments in Natural Language Processing. To request some details to be able to reproduce the human evaluation pipeline, the authors of this study sent requests to the authors of 116 papers. 45 replies ( $39 \%$ ) were received, among which only 20 authors ( $45 \%$ of the replied authors) were able to provide the details necessary for the reproduction. These results are pretty well aligned with ours, where we received replies in $45 \%$ of the cases. However, in our case, the positive result of the contact with authors is lower - only $16 \%$ of the replied authors provided meaningful responses.

Table 2 Results of contacting the authors grouped by the response type


### 5.5 Detailed analysis of the reusable Bayesian Networks

A paper that meets at least the necessary condition of reusability can present information about BNs in various forms that imply different levels of difficulty for further reuse. We analyse the corresponding details of the technical presentation of the BNs for the papers where the BN was initially available from the paper content (Table 3) and the papers which authors provided the details after a request (Table 4).

Table 3 analysis reveals several key insights regarding the publication of BNs reusable just relying on the paper content. First, it is not common for BNs to be published in a runnable format; only 7 papers did so. Of these, one paper used the .dne format, another used the .neta format, and one presented the BN as a web service, which also included a downloadable link for the BN. Four other papers provided GitHub repositories for BN reproduction. While this option offers deeper technical insights into the BN construction process, proper documentation is crucial, as inadequate documentation can make it difficult to reproduce the results.

In addition, 19 papers presented all parts of the BN in plain text or table formats, with network sizes ranging from 3 to 39 nodes. For smaller BNs, manually constructing a runnable file using the provided values may be feasible, but for larger networks, the likelihood of errors increases, making reuse more challenging.

Table 4 detailing the formats of BNs provided by authors in response to our request shows that most authors shared popular runnable formats, such as .net and .xdsl. In some cases, authors provided repositories containing the necessary information. It is important to note that including links to these repositories in the paper itself would be a better practice to ensure accessibility and prevent reliance on direct queries to authors, which, as demonstrated earlier, is not always reliable.

## 6 Discussion

The survey results reveal a notable consensus within the research community regarding the importance of clearly indicating the sources of the collected BNs and reporting the methods of their validation. However, there is no such consensus regarding the possible reusability of the developed BNs. This seems particularly critical for the papers that either do not have clear definitions of the sources or for those that have been at least partially developed via experts' knowledge elicitation. In all cases, when the source of certain BN parts was indicated as expert knowledge, no detailed expert knowledge elicitation procedure was provided. Instead, such

Table 3 Detailed analysis of the BNs that were found to be reusable from the content of the papers


Cont. refers to paper content (either main paper body or supplementary materials). Run. file refers to runnable file available. Nodes refers to the number of variables or nodes in the BN graph. $P D$ type refers to the type of probability distributions used in the BN, which can be disc. (discrete), dyn.disc. (dynamic discrete) or cont. (continuous). "PD" stands for Probability Distribution a paper just mentions that the material was obtained from expert knowledge without further details [91, 125, 126]. Still, even if such details are available, the reproduction of a human-driven process may be very difficult, because it may be necessary to find a similar number of experts with similar expertise and to perform a similar type of discussion with them. Jointly, such a task does not seem feasible in a general case.

Even if the BN collection pipeline can be theoretically reproduced (for example, if there is a link to open-sourced data and there are enough details to run structure learning and parameter elicitation algorithms), the best practice should be presenting and open-sourcing the results. Such an approach will certainly increase the chances of the paper being reused and cited, thus making it more impactful to the community.

Various papers do have the results of their research in a perfectly reusable form. For example, in [97] the authors developed a full-scale web application to let other researchers quickly test the developed BN. However, not all research teams may have either experience or resources to wrap the results in such a way, but still, after any BN-development work is finalized, the launchable BN is always supposed to be available to the authors of the paper. So making the BN easily reusable for potential readers of the published paper should not be a very difficult task that can be done either inside the paper text (if the developed BN is not very big) [96], in supplementary materials [73] or a repository [86, 112, 127].

We initially assumed that contacting the authors directly might be a reliable way to obtain the developed BN models. However, our findings show that this approach is often unreliable, as many authors either do not respond or are unable to locate the necessary files, especially if some time has passed since the paper was published. While some authors may make their BN models available on personal resources, it is crucial

Table 4 Detailed analysis of the BNs that were not reusable from the paper content but which were provided by the authors after request


that links to these resources be included in the paper itself to ensure the paper remains self-contained, and the information is accessible.

Certainly, there could be certain limitations to the opensourcing of the developed BN, like confidentiality reasons, but this should be clearly indicated in the paper whenever applicable. Moreover, in some scenarios, the direct re-usage of Probability Distribution may be risky because the probabilities can be sensitive to the particular dataset they were learned from. However, we believe that if it turns out necessary for interested researchers to reuse the BN, it is much better to have the developed BN in a fully reusable form. Thus, it can be at least tested on a new task, taking into account the aforementioned risk of probabilities being sensitive to the particular dataset.

It should also be considered that meeting the sufficient condition of reusability defines just the basic requirement of reusability. Even if the BN is fully specified, it may still be hard to reuse it in other projects due to many potential reasons, including, but not limited to, the following examples that complicate the reuse: variables with poor semantics (e.g., presence of variables that do not match with observable phenomena) or the variables with a non-intuitive naming pattern, variables representing concepts that are too specific for a given domain, or too abstract for the intended use in other projects, unspecified assumptions while building the model (e.g., causal relationships between some variables may be removed for very specific application case). Such factors may make the re-usage of the BNs even less likely than concluded in our paper.

Finally, even when a paper provides sufficient information for reuse, certain forms of presentation, such as probabilities in simple tabular format, can be impractical-especially for large BNs. For smaller networks, manual construction may be feasible, but for larger networks, the likelihood of errors increases, complicating reusability. Therefore, it is preferable to share repositories with easily runnable code or BN files in popular formats.

## 7 Recommendations

According to our findings, we present specific recommendations that may help the research community to ensure the reusability of developed BNs.

Clarify the sources of all BN parts State explicitly the sources (experts, literature, and data) of all BN parts (variables, arcs, and Probability Distribution).

Report the details of experts' knowledge elicitation Describe the number of experts, exclusion/inclusion criteria, amount of remuneration, the ways of resolving disagreements, and other essential details.

Report the details of data-driven algorithms Indicate the algorithm and all parameters affecting the final results. Opensource the code and dataset for running the algorithm if no restrictions are applied.

Report the ways and results of BN evaluation Use at least one of the various approaches to validate the correctness of the collected BN: case studies, sensitivity analysis, evaluation by experts, metrics calculation on a test split of a dataset, etc.

Open-source the developed BN in a reusable form Use at least one of the various ways to open-source the developed BN: inside the paper text (if the BN is relatively small), in supplementary materials, in side resources (e.g., GitHub), or in a web application. The best option is to rely on the BN formats that can be read with open-source packages (e.g. [128]): XMLBIF, XMLBeliefNetwork, etc., rather than proprietary software and corresponding formats.

## 8 Conclusion

BNs can be useful in many fields, from various engineering applications to medicine or education. Still, their final applicability to either real-life projects or further research tasks can be significantly higher if the BNs developed in the research papers are made reusable. This survey, drawing on 147 papers that propose BNs in various fields, evaluated the

reusability of the BNs presented in the papers. The results show that $77 \%$ of the papers do not address the issue of the reusability of the developed BNs because of the lack of open-sourced Probability Distribution or other significant parts of the BNs. The subsequent contact with the authors of the papers with insufficient details about BNs rarely yields
positive results - only $12 \%$ of the queried authors were able to provide necessary information for BN reusage.

## Appendix A: Detailed statistics of the studied papers

Table 5 General analysis of all papers included in the survey


Table 5 continued


Table 5 continued


Table 5 continued


Abbreviations used for the sources of variables, arcs, and PD source are Lit - Literature, Ex - Experts, D - Data, no - no source is specified. The 'Eval' column indicates whether any evaluation of the constructed BN has been performed. Abbreviations used for BN parts availability columns: 'part' - 'partially available', 'req' - 'available by request', 'inc.' - 'the BN part is inconsistent with other parts'. $\mathbf{\square}$ refers to the results of the request to authors: "-" - not applicable, $\checkmark$ - BN was provided by request, $\times$ - BN was not provided after request. "PD" stands for Probability Distribution. More detailed results are available in the Supplementary Materials

Acknowledgements We deeply thank the authors who replied to our requests and assisted in collecting the BNs. This research was funded by the European Union's Horizon 2020 research and innovation program under the Marie Skodowska-Curie grant agreement No 860621. The paper is also a part of R+D+i project PID2023-149959OA-I00, funded by MCIN/AEI/10.13039/501100011033/ and by the "European Union NextGenerationEU/PRTR". The authors also acknowledge the support of the Galician Ministry for Education, Universities and Professional Training and the "ERDF A way of making Europe" through grants "Centro de investigación de Galicia accreditation 2024-2027 ED431G2023/04" and "Reference Competitive Group accreditation 2022-2025 ED431C 2022/19".

Funding Open Access funding provided thanks to the CRUE-CSIC agreement with Springer Nature.

Data Availability The main takeaways of our survey are presented in the Tables either in the main body of the paper or in the Appendix. The more detailed information of the studied papers is available in Supplementary Materials (https://gitlab.nl4xai.eu/nikolay.babakov/bn-reusability-survey).

## Declarations

Competing interests The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the
permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecomm ons.org/licenses/by/4.0/.
