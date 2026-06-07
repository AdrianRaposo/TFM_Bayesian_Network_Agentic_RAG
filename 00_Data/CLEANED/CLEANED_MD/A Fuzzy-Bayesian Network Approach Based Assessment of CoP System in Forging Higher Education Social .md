# Article 

## A Fuzzy-Bayesian Network Approach Based Assessment of CoP System in Forging Higher Education Social Responsibility

Binglei Xie ${ }^{1,2}$, Pengchang $\mathrm{Li}^{3}$, Yuhong Wang ${ }^{3}$ (D), Feiyi Luo ${ }^{4}$ and Linhua Wu ${ }^{5, *}$


#### Abstract

check for updates Citation: Xie, B.; Li, P.; Wang, Y.; Luo, F.; Wu, L. A Fuzzy-Bayesian Network Approach Based Assessment of CoP System in Forging Higher Education Social Responsibility. Systems 2024, 12, 540. https://doi.org/10.3390/ systems12120540

Academic Editor: Vladimir Bureš

Received: 20 June 2024
Revised: 8 November 2024
Accepted: 30 November 2024
Published: 3 December 2024


## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 Office for Talent Recruitting and Management, Ningbo University, Ningbo 315211, China
2 Institute of Education, Xiamen University, Xiamen 361005, China
3 Faculty of Maritime and Transportation, Ningbo University, Ningbo 315211, China
4 Department of Industrial Systems Engineering and Management, National University of Singapore, Singapore 117576, Singapore
5 Faculty of Mathematics and Statistics, Ningbo University, Ningbo 315211, China

* Correspondence: wulinhua@nbu.edu.cn


#### Abstract

Community of practice (CoP) has been seen as a pivotal support for higher education institutions to implement their social responsibilities. Even though this model is widely admired, assessing its effectiveness and sustainability still faces many challenges: (1) the absence of an appropriate index reveals the significance of CoP ; (2) the difficulty of realizing quantitative assessment; and (3) the strategies to improve contribution sustainably by considering CoP development. To address these challenges, a comprehensive Higher Education Social Responsibility Contribution Index (HESRCI) is constructed by taking into account the CoP key influence factors. An FBN model is further developed for the purpose of assessing the various corresponding contributions quantitatively and investigating the potential interdependencies between influence factors. The effectiveness of the proposed approach is evidenced by the quantitative indication of CoP's contributions to priorities. Research findings also highlight the significance of CoP governance, the mechanism of resource allocation, and team development, in particular, in facilitating the synergy between university development and sustainable socio-economic growth. In addition, it provides data support and a theoretical basis for higher education institutions to make more informed decisions when implementing industry-education integration strategies.


Keywords: community of practice; higher education; social responsibility; Bayesian network; fuzzy theory

## 1. Introduction

The concept of Communities of Practice (CoPs), first introduced by Lave and Wenger [1] and further expanded by Wenger [2], emphasizes learning as a social, participatory process that develops through sustained engagement in shared practices. In the context of higher education, CoPs are recognized as fundamental to facilitating institutional knowledge exchange, professional development, and academic innovation. Through the engagement of diverse stakeholders, CoPs contribute to the creation of more inclusive educational environments [2], fostering innovations [3,4], and adequately addressing the needs of various community members [5].

Higher Education Social Responsibility (HESR) refers to universities' commitment to contribute positively to society by addressing social, economic, and environmental challenges through education [6], research [7], and community engagement [8]. With the growing expectations of governments, communities, and other stakeholders, the pivotal role of higher education institutions has been expanded to include cultural heritage and international communication as well. The former safeguards and enriches cultural diversity through educational and research activities, while the latter augments university openness and interactivity, cultivating global partnerships that facilitate knowledge and cultural

exchange and providing cross-cultural perspectives to faculties and students [8,9]. Within this context, CoPs become vehicles for applying university resources and expertise toward solving real-world issues, thereby fulfilling their social responsibilities [1].

However, evaluating the contributions of CoPs to HESR presents significant challenges due to the intangible and multidimensional nature of both CoPs and social responsibility. Traditional metrics and evaluation frameworks often fail to capture the complex dynamics inherent in CoPs, including the influences of interpersonal relationships, member engagement, and cultural factors on social outcomes [10,11]. Consequently, accurate and reliable evaluations of CoPs are essential to elucidate their strengths, limitations, and areas for improvement, which are critical to maximizing their impact on HESR [12]. Such assessments also enable universities to make informed decisions regarding resource allocation, CoP structure, and strategic alignment with social responsibility objectives [13]. In addition, effective evaluations improve measurement, accountability, and transparency to stakeholders and reinforce the university's commitment to social goals [14]. Addressing the need for robust assessment methods is, therefore, vital to ensure that CoPs effectively contribute to the advancement of HESR in a rapidly evolving educational landscape.

Many traditional assessment methods, such as surveys or simple quantitative metrics, do not account for the uncertainty and variability inherent in CoP activities and their social outcomes. Given that CoPs operate within complex social networks, a more flexible and nuanced assessment approach is needed to handle the ambiguity and incomplete data often associated with social responsibility initiatives [15]. The Fuzzy-Bayesian Network approach integrates the strengths of fuzzy logic and Bayesian networks to accommodate uncertainty, subjectivity, and imprecise information. Fuzzy logic allows handling imprecise terms and subjective judgments [16], while Bayesian networks offer a probabilistic framework to model dependencies among CoP activities and outcomes. This combined approach has great potential for assessing CoP contributions to HESR, enabling a dynamic and adaptable evaluation model that can reflect the real complexity of CoPs in higher education settings [17].

This paper aims to evaluate the contribution of CoPs to HESR performance and identify the key influence factors in consequence. In so doing, a comprehensive Higher Education Social Responsibility Contribution Index (HESRCI) is constructed taking into account the key insights of CoPs. An FBN model is developed further for the purpose of quantitatively assessing the various corresponding contributions and investigating the potential interdependencies between influence factors.

The contributions of this paper are as follows:

- A system with a multidimensional assessment index encompassing the sectors, including resource input, governance and policies, activities, and outcomes. It allows for a holistic assessment of CoP's multifaceted impacts on higher education and offers deeper insights.
- A novel approach not only offers a quantitative assessment method of existing purpose but also establishes a replicable methodological framework for future assessments, especially when a large amount of practical data is obtained along with digitization.
- Forward and backward reasoning analyses provide data-based insights and recommendations for shaping CoP development strategies, which facilitates higher education development consequences.
The rest of this paper is organized as follows. Section 2 reviews the existing literature on the contribution of CoP to the social responsibility of higher education, Section 3 explains the proposed FBN model and data sources, and Section 4 details the results together with a sensitivity-based validation. Finally, the implications and conclusions are drawn in Section 5.

# 2. Literature Review 

### 2.1. Adaption of CoPs to HESR Dynamics

The evolution of HESR is characterized by increased public expectations and the imperative to address global challenges, necessitating a shift for universities from traditional academic outputs to more expansive and quantifiable societal contributions [18,19]. For instance, Marginson [20] highlights the importance of universities serving the public good, with an emphasis on social equity and sustainable impact. Hayter and Cahoy [21] present a strategic framework for aligning institutional practices with social responsibility, while Sonetti et al. [18] assess the transition towards sustainable campuses driven by public demand. Recent investigations, such as those by Kim and Lee [19] and Leal Filho et al. [22], underscore the manner in which universities respond to these expectations through policy modifications and initiatives aimed at supporting sustainable development and achieving local-global social objectives.

To adapt to the evolving dynamics of HESR, CoPs have been developed through more intentional structuring, diversified stakeholder involvement, and enhanced technology integration. The following common strategies have been developed as below:

- Transitioning from informal formats to more strategic structures. Initially informal collectives, CoPs within universities are now frequently organized with explicitly defined objectives and goals [23], employ structured meeting formats [24], integrate with institutional policies [25], and receive formal recognition and support [14].
- Engagement with stakeholders both at local and international levels is of paramount importance. Extensive literature demonstrates that CoPs at the local level facilitate significant collaborations and effectively address local needs. Meanwhile, the advantages of involving international stakeholders in CoPs have been recognized, particularly in enhancing coordination [26], accommodating cultural diversity [27], and achieving strategic alignment [10].
- Encouraging interdisciplinary approaches to address societal challenges. CoPs advance interdisciplinary methodologies by integrating varied expertise to address intricate societal issues, thereby highlighting the necessity for comprehensive solutions. Illustrative examples include the ERE community of the European Geosciences Union (EGU) purposed for the solution of global economic prosperity, environmental quality, and political stability based on interdisciplinary research [28] and the interdisciplinary art and design processes at the Institut Kesenian Jakarta [29].
- Leveraging technological advancements to improve communication and knowledge sharing. The implementation of virtual communication tools enables CoPs to transcend geographical and temporal limitations, thereby facilitating continuous interaction among diverse departments, institutions, and nations. This digital flexibility has broadened the scope and impact of CoPs, empowering them to tackle global issues such as public health and climate change [30].
The above adaptations exert considerable influence on the performance of CoPs and their subsequent contribution to HESR.


### 2.2. Metrics for Assessing the Contribution of CoPs to HESR

Defining standardized metrics to quantify the value of CoPs remains challenging due to the social, dynamic, and collaborative nature of various community types. However, there have been a number of studies that attempted to develop various metrics, in both quantitative and qualitative formats, across studies tailored to suit different institutional contexts.

Quantitative metrics are essential for evaluating CoPs. Participation and engagement rates are common indicators reflecting the degree of involvement within the community. Studies by McDonald and Cater-Steel [31] demonstrate how these metrics can serve as indicators of a CoP's health and its potential social impact. Institutions frequently assess attendance consistency at CoP events as well as participant diversity to evaluate the success of engagement, particularly in social responsibility initiatives that necessitate regular

interaction [23,32]. Project outcomes, such as publications and community outreach, are also crucial metrics for determining tangible contributions to HESR. For instance, certain CoPs focused on environmental responsibility track the implementation of sustainable initiatives [33,34], while some Asian universities prioritize project-based metrics illustrating environmental sustainability outcomes [21]. Metrics related to knowledge transfer and skill development are also significant, as they evaluate increases in member skills and knowledge [35,36].

Qualitative metrics include frameworks like the value creation cycle proposed by Wenger, Trayner, and De Laat [37], which assesses CoPs' evolving impacts on personal and institutional development. This model captures the long-term cultural shifts fostered by CoPs [19]. Narrative-based assessments provide insight into the individual experiences of CoP members [30]. In empirical studies carried out in Latin America, these assessments are valuable for evaluating the social impact of CoPs on community health and education initiatives [5,38]. Furthermore, measuring stakeholder satisfaction through surveys and interviews offers essential qualitative data on the effectiveness of CoPs in meeting social responsibility objectives [39].

Mixed-method approaches enhance the assessment of the contributions of CoPs to HESR, particularly concerning their effect on institutional policies. The previous literature underscores how successful CoPs can result in policy transformations related to diversity, equity, and sustainability [27,40]. By scrutinizing documentation and conducting interviews with institutional leaders, the extent of the impact of CoPs on broader policies can be evaluated. Longitudinal studies are also instrumental in monitoring the sustained effects of CoPs over time, with European sample universities assessing the long-term outcome of CoPs on community partnerships and university culture [41,42].

Despite the progress made, gaps remain in the current assessment metrics for CoPs' contributions to HESR. Many existing metrics fail to capture intangible benefits such as cultural shifts and community integration, which are critical to understanding the social impact of CoPs [11,43]. Furthermore, the focus on short-term outcomes often neglects long-term transformative impacts, particularly in regions where CoPs are still evolving.

# 2.3. Methodological Approaches to CoPs Contribution Assessment 

Developing new methodological approaches to CoP assessment is essential for capturing the complex, multidimensional impacts these communities have on organizational learning, innovation, and social responsibility.

Ardichvili et al. [44] investigated the influence of cultural factors on CoPs by conducting interviews with students from China, Russia, and Brazil. The study revealed that cultural differences significantly affect member competitiveness and communication patterns. Building on these findings, Lehane et al. [45] developed a data-driven theoretical framework based on grounded theory, which offers systematically valid survey classification criteria. Continuing this line of research, Lesser et al. [46] studied how knowledge sharing, trust, and a common language enhance organizational learning and innovation. However, they encountered difficulties in quantifying the direct impact of CoP on business outcomes and in managing community activities to ensure consistent value delivery. Further, Price et al. [47] analyzed the establishment and qualitative sharing process. It is acknowledged that qualitative methods face significant challenges, including time constraints, heavy workloads, and discrepancies within teams regarding the understanding of assessment criteria, which considerably impede effective sharing and consistent application.

Wang et al. [48] conducted an empirical study utilizing questionnaires administered to HEI students and teachers with the aim of assessing the effects of CoPs' activities, particularly regarding their impact on educational outcomes. To address the issue, Chu et al. [49] employed a non-additive fuzzy integral approach to evaluate CoPs performance within the context of organizational change; however, they did not investigate the dependencies among critical indicators such as resources and mechanisms pertinent to talent training and research. Similarly, Khosla et al. [50] implemented a fuzzy multicriteria decision-making

approach (MCDM) within a case study framework to analyze indicator priorities and strategic preferences, yet it inadequately addressed the complex interdependencies among the indicators. Finally, Hong et al. [7] utilized the maturity model to evaluate various CoP indicators, but they neglected to consider the dependencies among indicators, such as those involving resource allocation and faculty, as well as mechanisms and team building. Evidently, the challenge of thoroughly uncovering and addressing complex interdependencies remains unresolved.

# 3. HESRCI and Assessment Approach 

### 3.1. HESRCI Development

In addition to the research gaps mentioned in previous sections, one of the key objectives of this paper is to develop the contribution index of CoPs to HESR in a more comprehensive manner. In so doing, as shown in Figure 1, the value creation framework developed by [37] is adapted by focusing on the domains of enabling value (i.e., resource and regulatory support), CoPs activities, and output impacts.
![img-0.jpeg](img-0.jpeg)

Figure 1. Value creation framework of CoPs in HESR. Source: Adapted by author based on Wenger, et al. [37].

- Resource and Funding Supplement: In the immediate and potential value cycles, CoPs seek resources and funding to enable their activities, capturing value through grants or sponsorships for operational support. For example, university CoPs often need initial funding for workshops, training, and community events to create a foundation for long-term impact [25]. Early resource investments show potential value by building a base for sustainable activity.
- Governance integration: The applied and realized value cycles of the framework address the ways CoPs interact with and influence broader institutional policies. For instance, if a CoP focused on sustainability aligns with university policy by promoting


eco-friendly practices, this could lead to CoP integration into formal governance structures, thereby reinforcing its influence on institutional practices [32]. By influencing policy and governance, CoPs realize their value in shaping the institution's culture and operational norms.

- CoPs activities: The framework also evaluates CoP activities through the immediate and applied value cycles, where members find value in their interactions and shared practices. In higher education, for example, CoPs focusing on teaching innovation might develop and share new educational resources, which members can apply directly in their classrooms, creating immediate and applied value [10].
- CoPs outputs: Transformative value arises when CoP activities result in sustainable changes at the institutional or community level. An illustrative instance occurs when a CoP focused on social responsibility within a university milieu effectively integrates into the institution's outreach framework, thereby engendering a sustainable social impact on local communities [33]. This transformative value cycle indicates the CoP's successful alignment of its outcomes with both institutional goals and societal needs.
Metrics indicating the multidimensional impacts of each domain are identified, as shown in Table 1, through a detailed review of previous studies.

Table 1. Identifying influences on the community of practice parenting.

Consequently, the structure of the HESRCI is depicted in Figure 2 below. The contributions of the CoPs are assessed across associated domains ranging from M1 to M4, with indicators within each domain designated from X1 to X23, respectively.

![img-1.jpeg](img-1.jpeg)

Figure 2. Higher Education Social Responsibility Contribution Index (HESRCI).

# 3.2. FBN Assessment 

The contribution of CoPs to HESR is characterized by its nuanced, interconnected, and context-sensitive nature. Accordingly, this paper employs a combined approach of Fuzzy logic and Bayesian networks (BNs) to evaluate both quantitative and qualitative dimensions, ensuring a comprehensive assessment of essential aspects such as social responsibility and educational outcomes. Specific advantages include the following:

- Handling uncertainty and subjectivity: fuzzy logic addresses subjective metrics like member satisfaction and engagement, allowing for nuanced assessments where exact numbers are not feasible.
- Addressing complex interdependencies: BN effectively maps complex relationships between factors, such as how member diversity influences organizational outcomes through engagement and innovation.
- Dynamic and context-specific evaluation: the fuzzy-BN approach adapts to diverse CoPs contexts, accounting for variables like participation frequency or diversity that may differ by institution.
- Comprehensive and balanced assessment: this approach integrates both quantitative and qualitative factors into a unified framework, offering a balanced view of CoPs' broader impacts on HESR.


### 3.2.1. Fuzzy Theory

Fuzzy theory is a mathematical approach to dealing with uncertain information proposed by L.A. Zadeh [51]. Its capability to manage imprecise terms and subjective assessments presents significant potential for quantifying the contributions of each indicator in this study numerically. By quantifying fuzzy data, fuzzy theory facilitates the evaluation of the impact of comparative strategies, and it thoroughly considers multiple factors and hierarchical information. This leads to a more comprehensive and precise foundation for decision-making, thereby enhancing the scientific rigor and accuracy of the decisionmaking process.

This survey categorizes the contribution of each indicator into five levels, namely very small, small, medium, large, and very large. Triangular fuzzy numbers are used to quantify these natural language descriptions. The definition and shape of fuzzy numbers can be found in Table 2 and Figure 3.

Table 2. Triangular fuzzy numbers definition of example indicator [52,53].


![img-2.jpeg](img-2.jpeg)

Figure 3. Fuzzy numbers of natural language.
Step 1: Opinion aggregation
Aggregated expert opinion, which is used to integrate the evaluations of multiple experts to form a uniform mean fuzzy number [44,47]:

$$
f=\left(\frac{1}{n}\right) \cdot\left[z_{1} \cdot B_{\lambda 1}+z_{2} \cdot B_{\lambda 2}+\cdots+z_{n} \cdot B_{\lambda n}\right]
$$

where $f$ is the average fuzzy number, $n$ is the number of experts, $z_{i}$ is the number of votes of the ith expert, and $B_{\lambda i}$ is the fuzzy set of the $i$ th linguistic term $(i=1,2, \ldots, 5)$ [51,54,55].

# Step 2: Defuzzification 

Defuzzification is the process of converting the output of the fuzzy number after aggregating the respondents' opinions into a precise value [56]. This step is a key component in the implementation of a fuzzy logic control system that enables the fuzzy inputs and rules of a fuzzy controller to produce practically usable and unambiguous control signals or decision outputs [44]. This process is performed by calculating the defuzzification through methods such as the center of gravity method, maximum affiliation method, etc. The center of gravity method is widely used because of its smooth and accurate results, and this method is also used in this paper for defuzzification, and the specific process is described in Equations (2) and (3) in detail [57,58]:

$$
\begin{gathered}
X^{*}=\frac{\int f(x) x d x}{\int f(x) d x} \\
F P S=\frac{\int_{a}^{b} \frac{x-a}{b-a} x d x+\int_{b}^{c} x d x+\int_{c}^{d} \frac{d-x}{d-c} x d x}{\int_{a}^{b} \frac{x-a}{b-a} d x+\int_{b}^{c} d x+\int_{c}^{d} \frac{d-x}{d-c} d x}=\frac{1}{4} \times(a+2 \times b+c)
\end{gathered}
$$

where $X^{*}$ is the clear value of the trapezoidal fuzzy number output, also known as the Fuzzy Possibility Score (FPS).

# Step 3: Fuzzy Failure Probability (FFP) 

Then, the FFP can be calculated as follows [51,54]:

$$
F F P=\left\{\begin{array}{c}
\frac{1}{10^{K}}(F P S \neq 0) \\
0(F P S=0)
\end{array} \text { where, }\left(K=\left(\frac{1-F P S}{F P S}\right)^{\frac{1}{3}} \times 2.301\right)\right.
$$

where $K$ is an intermediate variable being only dependent on FPS.

### 3.2.2. Bayesian Network (BN)

The Bayesian network (BN), alternatively referred to as the Bayesian Belief Network, constitutes a robust probabilistic framework depicted through a directed acyclic graph. The initial visualization (i.e., without the input of fuzzy result) of HESRCI within this paper was constructed in GENIE software, as shown in Figure 4. Within this network, nodes are indicative of random variables, whereas the arcs delineate direct probabilistic dependencies among these nodes, representing the qualitative dimension of the BN. In contrast, the quantitative dimension comprises the conditional probabilities and prior probabilities [59].
![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network simulation of HESRCI in GENIE.
In practical application, the BN is represented as a binary group $\langle G, P\rangle$, wherein $G=\langle V, R\rangle$ denotes a visual directed acyclic graph (DAG) comprising n nodes; $V=$ $\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ signifies a collection of nodes or stochastic events; and R signifies a set of directed edges encapsulating the logical relationships amongst these nodes. Within a directed edge $<X_{i}, X_{i}>, X_{i}$ constitutes the child node, and $X_{j}$ is deemed the parent node of $X_{i}$, while $\pi\left(X_{i}\right)$ embodies the set of parent nodes of $X_{i}$. Root nodes are those lacking any parent nodes, whereas leaf nodes are those devoid of child nodes. The Conditional Probability Table (CPT) delineates the quantitative causalities between nodes within a DAG. A priori probability is an initial estimate or assumption about the probability distribution of the state of a node or random variable in a network before any data or evidence is observed [54]. Given the prior probability distribution of root nodes and the conditional probability distributions of other nodes, deriving the joint probability distribution of all nodes is not a complex endeavor. When both the prior probability distribution of the root nodes and the conditional probability distribution of the other nodes are established, the joint probability distribution of all nodes can be expressed as

$$
P(V)=P\left(X_{1}, X_{2}, \cdots, X_{n_{i}}\right)=\prod_{i=1}^{n} P\left(X_{i} \pi\left(X_{i}\right)\right)
$$

The probability of $X_{i}$ is given by

$$
P\left(X_{i_{*}}\right)=\sum_{X_{j}, j \neq i} P(V)
$$

In a diagnostic analysis of BN, a series of evidence $E$ is examined, and the posterior probability distribution of $X_{i}$ can be calculated using Bayes' theorem as follows [60]:

$$
P\left(X_{i} \mid E\right)=\frac{P(X, \mathrm{E})}{P(E)}=\frac{P\left(X_{i}\right) P\left(E \mid X_{i}\right)}{\sum_{i=1}^{n} P\left(X_{i}\right) P\left(E \mid X_{i}\right)}
$$

when using BN to assess the COP, determining the CPT of BN is a very critical step. As aforementioned, it is necessary to determine the CPT of BN through expert experience because of lacking historical data. However, the conditional probability of a network involving multiple nodes brings great difficulty for expert scoring. In order to simplify the difficulty, this study introduces a Noisy-OR gate model [61-63] and combines the fuzzy theory to convert the fuzzy language into conditional probability. Using the Noisy-OR model requires two conditions to be met [61,62]: (1) each event is independent of each other, and each event has only two states; (2) assuming that the state of one of the variables $x_{i}$ is occurrence and other variables is not occurrence, then the probability of its child node $Y$ is $P_{i}=P\left(Y=1 \mid \overline{x_{1}}, \overline{x_{2}}, \cdots, x_{i}, \overline{x_{i+1}}, \cdots, \overline{x_{n}}\right)$, then the probability $P_{i}$ is called the connection probability [56-58] as shown in Equation (8). The connection probability is obtained by expert judgment, and then the conditional probability can be calculated as Equation (9).

$$
\begin{gathered}
P_{i}=P\left(Y=1 \mid X_{1}=0, \cdots, X_{i}=1, \cdots, X_{n}=0\right) \\
P\left(Y \mid X_{p}\right)=1-\prod_{i: x_{i} \in x_{p}}\left(1-P_{i}\right)
\end{gathered}
$$

It can be known from the above Equation (8) that when the $P_{i}$ is 0 , the conditional probability is also 0 . Therefore, the probability of occurrence can be defined as 0 .

# 3.3. Sensitivity Analysis 

Sensitivity analysis can also aid in ranking the influencing factors while testing the robustness of the model. Analysis using a prior and posterior probabilities [56,57], as shown in Equation (10).

$$
\mathrm{R}\left(X_{i}\right)=\frac{\varphi\left(X_{i}\right)-\psi\left(X_{i}\right)}{\psi\left(X_{i}\right)}
$$

where $\mathrm{R}\left(X_{i}\right)$ is sensitive value, $\varphi\left(X_{i}\right)$ is posterior probability and $\psi\left(X_{i}\right)$ is prior probability.

## 4. Empirical Application and Result Analysis

### 4.1. Study Case

Two universities were chosen as samples for this study to address potential concerns regarding representativeness, which may arise from factors such as disparities in the development of CoPs and the intrinsic competitiveness of the universities. Data sources are obtained through a questionnaire survey designed on the basis of the index identified in Section 3.1.

The questionnaire comprised three sections. First of all, respondents' general information, such as their professional identity and participation experience of CoPs, was gathered through single-choice and fill-in-the-blank questions to ensure the appropriateness of data. Secondly, respondents' perceptions of university social responsibility, including their satisfaction and ratings of each domain, were evaluated in questions of matrix choice and ranking formats. The collected data forms the Conditional Probability Table (CPT). Ultimately, perspectives regarding the characteristics of CoPs and their specific contributions to the social responsibilities of higher education are assessed through structured questions employing matrix choice and ranking formats. The responses are anticipated to furnish a strong quantitative data foundation for subsequent analyses. To guarantee represen-

tativeness and precision, target respondents are chosen based on the criteria outlined in [36,37,38]:Respondents cover all participated stakeholder sectors in CoP operations, including HEIs students, government officials, and enterprise experts, as well as the teaching and admin staff working in higher education.Respondents' role and experience are crucial, as experienced participants can provide more in-depth insights, thereby enhancing the realism and accuracy of the assessment results. Consider the educational level of the participants, which can reflect their cognitive ability and depth of understanding of the practice of CoPs.

Based on the above criteria, 187 questionnaires were validated out of a total of 200 responses. The profile of the respondents is illustrated in Figure 5.

![img-4.jpeg](img-4.jpeg)

Figure 5. Distribution of respondent roles.

# 4.2. Analysis of HESRCI Inference Using FBU 

(1) Overall significance of CoP in higher education social responsibility

On the basis of survey data, the fuzzy failure probability of each node can be determined using Equation (1) and subsequently employed as the prior probability within the Bayesian network. Taking node X1 (Human Resource) as an illustrative example, the process for computing the fuzzy failure probability of this specific node is outlined as follows:

$$
\begin{gathered}
\mathrm{f}=\frac{1}{187}[3 \times(0,0.1,0.2)+0(0.1,0.25,0.4)+9 \times(0.3,0.5,0.7) \\
+50 \times(0.6,0.75,0.9)+125(0.8,0.9,1)] \\
=(7096,0.8728,0.946)
\end{gathered}
$$

Table 3 presents the computed results pertaining to fuzzy numbers for the remaining nodes.

Table 3. Fuzzy number of root nodes.


Upon the results of Table 3, the values of K, fuzzy possibility (FPS) and fuzzy failure probability (FFP) for the node are determined utilizing Equations (3) and (4) and summarized in Table 4. Taking node X1 (Human Resource) as an example again, its FPS and FFP are computed as follows:

$$
\begin{gathered}
\text { FPS }=\frac{1}{4} \times(0.7096+2 \times 0.8278+0.9460)=0.8278 \\
K=\left(\frac{1-0.8278}{0.8278}\right)^{\frac{1}{3}} \times 2.301=1.3634 \\
\text { FFP }=\frac{1}{10^{K}}=0.0433
\end{gathered}
$$

Table 4. Prior probability of the root node.


As explained in Section 3.3 earlier, the calculation of the node's connection probability follows Formula (6), subsequently leading to the computation of the node's conditional probability as per Formula (8). Consequently, the resulting connection probabilities for nodes A1-A5 (i.e., the five sections of HESR) and M1-M4 (i.e., the four domains of CoP contribution) are illustrated in Tables 5 and 6, respectively. The process for determining the conditional probability of a specific node is demonstrated below, taking M1 (Resource) as an exemplar. The corresponding results are illustrated in Table 7, while the rest nodes are computed by following the same process.

$$
\begin{aligned}
P\left(M 1=1 \mid X_{1}=1, X_{2}=1, X_{3}=1, X_{4}=1\right)=1-\left(1-P_{1}\right)\left(1-P_{2}\right)\left(1-P_{3}\right)\left(1-P_{4}\right) \\
=1-(1-0.0265)(1-0.0369)(1-0.0375)(1-0.0289)=0.1236
\end{aligned}
$$

Table 5. Connection probability of nodes A1-A5.


Table 6. Connection probability of M1-M4 nodes.


Table 7. Conditional Probability Table for M1 node.


Ultimately, based on probabilities calculated upon the respondents' feedback, the BN inference demonstrates the magnitude of the probability of each node, and this is visualized through GENIE 2.0 software, as depicted in Figure 6.

![img-5.jpeg](img-5.jpeg)

Figure 6. BN prediction results.
The contribution of CoPs within each section of HESR is delineated by the probabilities associated with nodes A1-A5, as presented in Table 8. This yields the following hierarchical order: A3 $>$ A2 $>$ A4 $>$ A5 $>$ A1.

Table 8. Probability of nodes in each program layer.


With the highest probability of $0.101 \%$, the contribution of CoPs to Node A3 (Social Service) underscores their role in connecting higher education activities with societal needs. The findings suggest that the respondents' experiences of CoPs engagement effectively demonstrate their role in bridging academic institutions with community development, extending beyond the realm of knowledge diversity to address concrete societal demands. Through active participation in community-focused initiatives, CoPs enhance the significance and adaptability of HEIs towards societal advancement, thereby establishing them as essential contributors to public welfare and regional development.

Ranking closely with a probability of $0.098 \%$, CoPs' influence on the node of A2 (Scientific Research) emphasizes the focus on research driven by technological innovation needs within industries. This result suggests that CoPs contribute to sustaining research excellence in HEIs by fostering collaboration among academics, researchers, and industry experts. Additionally, it highlights the role of government support and investment in enhancing HEIs' research capabilities, which enables them to compete globally in science and technology. By integrating CoPs, HEIs can expand research outputs and innovations, aligning their goals with industry demands and advancing the role of higher education in driving innovation.

The lowest probability ( $0.089 \%$ ) identified within node A1, which pertains to the responsibility for talent cultivation, highlights deficiencies in the existing CoP model's ability to adequately prepare students for the demands of evolving careers. This observed discrepancy between educational outputs and market expectations implies that CoPs must undergo modifications to more effectively incorporate the development of practical skills and engagement with industry. Such an adaptation necessitates the adoption of more innovative strategies, including the modernization of curricula, the formation of partnerships with industry, and the implementation of teaching methods focused on career preparation to bridge the gap between academic training and the requirements of the workforce. Enhancing this alignment would facilitate HEIs in producing graduates who possess skill sets that more effectively align with the expectations of contemporary employers.

Although assigned with slightly less probability than Scientific Research, the contributions of CoPs to node A4 (Cultural Heritage) and node A5 (International Communications) demonstrate a more extensive impact. These domains exemplify an expansion of CoP activities beyond traditional skill-based learning to incorporate broader psychological and cultural aspects. By fostering cultural preservation and international collaboration, CoPs enable HEIs to cultivate a diverse and globally interconnected academic setting, thereby enhancing cross-cultural competencies and international outreach. This suggests that CoPs play an increasing role in developing well-rounded individuals capable of contributing to both local and global communities.
(2) Contributions assessed on the CoP domain level

Table 9 below presents the posterior probabilities of contributions attributable to CoP domains, spanning from M1 of resource supplements to M4 of outputs, in relation to each specific individual social responsibility, A1 through A5.

Table 9. Contributions to HESRCI in CoP domains.


The findings indicate that the multiple dimensions of CoP's contribution to advancing higher education social responsibilities follow a consistent order: M2 > M4 > M3 > M1. In addition, the significance of CoP domains to each responsibility sector does not exhibit a uniform consistency. For instance, within the domain of CoP governance, the influence on scientific research (A2) and cultural heritage and innovation (A4) is represented by the highest and lowest scores, respectively. Conversely, the probabilities within the domain of CoP activities (M3) are completely inverted. Similarly, the greatest impacts of additional resources provided by CoP (M1) are observed in talent cultivation (A1), whereas the domain of outputs (M4) exerts the least influence on international communications (A5).

The CoP governance mechanism (M2) is perceived as the most significant contributing factor. Establishing structured governance frameworks with clear collaboration policies, operational standards, and conflict resolution guidelines is essential. Leadership training within CoPs can further support collaborative norms and effective decision-making structures, enhancing CoP stability. Given that CoP governance has a particularly strong impact on scientific research but less influence on cultural heritage, institutions may benefit from adopting tailored governance strategies that align with each CoP's specific goals. Additionally, a flexible, adaptive approach to CoP management is crucial, enabling institutions to periodically assess and adjust governance, resources, and activities to meet the evolving needs of different responsibility sectors.

Since resource supplementation (M1) contributes the least across all domains, policies should shift from simply increasing resources to strategically deploying resources toward strengthening CoP governance and activity effectiveness. This approach ensures that resources support sustainable engagement, meaningful output generation, and stronger links between CoPs and external demands. Meanwhile, its stronger impacts on talent cultivation (A1) but less influence on international communications (A5) suggests that resources should be strategically allocated based on the primary objectives of each CoP. For example, policymakers may consider channeling more resources to CoPs focused on talent development initiatives, such as industry-aligned training programs, while viewing resource supplementation as less critical for CoPs targeting international outreach, where partnerships and networks may be more influential.

CoP outputs (M4), with posterior probability estimates ranging from $26 \%$ to $30 \%$, are identified as the second most pertinent contributor due to their direct impact on enhancing the competency and employment competitiveness of graduates. It is recommended that administrators prioritize output-driven CoPs that facilitate practical learning opportunities, including skill certifications and internships, to strengthen the contribution of CoP outputs.

Variations in the influence of CoP activities (M3) on different HESR sections suggest that a "one-size-fits-all" approach to CoP activities may be insufficient. Administrators should aim to tailor CoP activities to address the unique requirements of each HESR category. For instance, CoPs focused on cultural heritage may benefit from activities that emphasize cultural exchange and preservation, whereas CoPs oriented towards talent cultivation may prioritize skill-building workshops and industry internships.
(3) Contributions from individual factors

To ascertain the principal influential factors that facilitate the implementation of social responsibility within higher education, a comprehensive analysis has been conducted at the level of individual factors. The findings pertaining to the associated posterior probabilities are presented in Tables 10-13.

Table 10. CoP's contributions in resource domain.


Table 11. CoP's contributions to governance.


Table 12. CoP's contributions in activities.


Within the domain of CoP resource input, all influential factors show a consistent order in regarding to social responsibility contributions, namely $\mathrm{A} 1>\mathrm{A} 5>\mathrm{A} 2>\mathrm{A} 3>\mathrm{A} 4$. It indicates that external funding (X2) is the most anticipated contributor, especially for driving programs that foster talent cultivation (A1), facilitate international communication (A5), and advance research (A2). However, the comparatively lower impact of the resource input domain overall indicates that while resources like funding, human resources (X1),

and facilities (X3) are foundational, they may not singularly enhance CoP outcomes as much as governance or output-focused domains.

Table 13. CoP's contributions in outputs.


The correspondence between projected financial support and actual contributions may reveal a deficiency in the effective utilization of these resources within CoPs. This observation suggests that although stakeholders prioritize financial and facility support, enhancing their efficacy may necessitate more comprehensive strategies, such as the implementation of robust governance frameworks or enhanced resource management. By optimizing resource allocation, particularly within high-impact domains such as talent cultivation and research, HEIs can more effectively fulfill societal expectations, thereby enhancing CoPs' contributions to their social responsibilities.

The governance (M2) exerts the most significant impact on talent cultivation with an average $30 \%$ probability, and the contribution order of $\mathrm{A} 2>\mathrm{A} 1>\mathrm{A} 3>\mathrm{A} 5>\mathrm{A} 4$ highlights the critical role of mechanism design and implementation in cross-sectional integration. Specifically, the team building (X9) and resource allocation (X7) mechanisms markedly influence the M2 node, whereas the openness (X5) has a lesser effect due to its indirect impact on educational quality and efficiency. The former emphasizes that the mechanism of both team building and resource allocation are also essential for shaping the format of joint task implementation, while the latter reveals that openness does have an impact on CoP performance but may not necessarily affect its contribution to HEIs functions.

Information exchange (X12), in conjunction with the provision of practical learning opportunities (X14), are identified as the two predominant factors within the sphere of CoP activities. These activities notably enhance cultural heritage and innovation (A4) and international communications (A5), suggesting that CoP activities most effectively support responsibilities that require dynamic exchange and applied learning. The contribution order (A4 $>$ A5 $>$ A3 $>$ A1 $>$ A2) indicates that CoP activities may have a greater impact in areas that prioritize community engagement, cultural exchange, and collaborative learning rather than strictly academic or research-oriented goals. By strategically enhancing CoP activities that align with specific social responsibilities, HEIs can leverage CoPs as a powerful tool for fostering community engagement, preserving cultural heritage, and supporting global communication efforts.

The domain of CoP outputs (M4) holds an overall substantial $28 \%$ probability, following the order of scientific research (A2) > social service (A3) > talent cultivation (A1) $>$ cultural heritage and innovation (A4) > international communications (A5). Among outputs, curriculum expansion (X17) is most impactful due to the added resources and activities that help modernize curricula, thus improving graduate competency. Followed by employment opportunities (X19) and sci-tech commercialization (X21), institutions in higher education are greatly facilitated in supplying more qualified professionals and turning research outcomes into industrial productivity improvements. Unfortunately, the direct economic contribution (X22) demonstrates the most limited impact, indicating the low visibility of economic advantages during the initial phases of cultural projects, wherein the enduring cultural and educational effects predominate.

By leveraging CoP outputs to emphasize curriculum development, employment pathways, and sci-tech commercialization, HEIs can align more closely with social responsibility

objectives and build a solid foundation for sustainable economic contributions in the future. On the other hand, HEIs should view CoP contributions as long-term investments rather than immediate revenue sources. Policymakers are suggested to set realistic expectations for economic contributions and pay more attention to the sustained cultural and educational value those CoPs bring in, which indirectly builds institutional reputation and community ties over time.

# 4.3. Sensitivity Analysis Results 

Figure 7 depicts the sensitivity values and trends in a comprehensive manner. Within the realm of resource sensitivity analysis, the values initially increase before experiencing a decline, reaching their apex at node X3. This peak elucidates the pivotal role of facilities in the social responsibility initiatives of HEIs. The presence of optimal facilities significantly augments their capacity to meet these responsibilities effectively. In the context of governance, sensitivity values exhibit considerable fluctuation, with the most substantial value observed at node X9. This underscores the critical importance of team development within governance for advancing social responsibility. The sensitivity associated with activities reaches its zenith at node X14, underscoring the substantial impact of practical learning activities. Such activities are essential for cultivating students' social awareness and practical competencies, thereby suggesting a requisite increase in resource allocation. Concerning outputs, there is a discernible overall downward trend, culminating in the lowest sensitivity at node X22, which indicates a disparity between the academic outputs of HEIs and their societal impact. Although HEIs contribute to scientific and technological advancements, there remains a need to enhance the commercialization of these achievements.
![img-6.jpeg](img-6.jpeg)

Figure 7. Sensitivity value folding line.
Figure 7 illustrates the sensitivity values attributed to nodes A1-A5, highlighting a consistent overall downward trend. The figure indicates that facilities (X3) emerge as the most sensitive node across areas such as talent cultivation (A1), scientific research (A2), social service (A3), and international communications (A5). Conversely, openness exhibits the least sensitivity among nodes A1, A3, A4, and A5. This can be attributed to the pivotal role of facilities in school infrastructure, teaching resources, and financial support, which significantly influence the effectiveness and quality of the institution's educational activities. This underscores the crucial role of resource allocation in directly impacting educational quality.

Enhancing facilities can substantially improve educational service effectiveness, while the low sensitivity of openness indicates a need for strengthening governance implementation and depth to fully leverage external resources and international cooperation.

# 5. Conclusions 

The study highlights the significance of developing a multidimensional and quantifiable index to represent the contribution of CoPs in enhancing higher education institutions' ability to fulfill their social responsibilities. Consequently, a HESRCI index has been established, encompassing not only traditional domains such as external resources and CoP outputs but also governance mechanisms and practical activities. The effectiveness of these domains is examined in relation to responsibilities, including talent cultivation, scientific research, social services, cultural heritage and innovation, as well as international communication. This index facilitates a more comprehensive evaluation of the CoPs' contribution, thereby equipping policymakers and educational administrators with enhanced insights for the optimal allocation of educational resources and the elevation of education quality.

The FBN model formulated within this study provides a robust quantitative approach for analyzing the contributions from the reasoning layer toward outcomes. As previously identified, the prioritization of CoP's significance in relation to the social responsibilities of higher education is sequenced as follows: social services, scientific research, cultural heritage and innovation, international communications, and finally, talent cultivation. The differences in scale are also discernible. This innovative approach not only presents a quantitative method for assessing existing purposes but also develops a replicable methodological framework for future evaluations of various strategies or methodologies, particularly when substantial practical data is accumulated through digitalization.

An additional contribution of the FBN model is the demonstration of the hierarchical structure of HESRCI through the distinctive backward and forward reasoning capability inherent in node interdependence analysis. The findings indicate that external funding resources, mechanisms of resource allocation and team development as governance policies, exchanges of information and practical learning opportunities as activities, and curriculum expansion, employment opportunities, and sci-tech commercialization as outputs constitute the primary influential factors identified. This analysis not only enhances the comprehension of indicator interactions but also offers empirical insights and recommendations for the optimization of the structure and content of COPs, thereby influencing the configuration of education-industry synergies.

Ultimately, the FBN model formulated in this study constitutes a suitable approach to align with the transitional trend in education management from a theory-driven paradigm to a data-driven one. The acquisition of more practical data through digitalized processes enhances the precision of the results mentioned previously. Furthermore, in future endeavors, the integration of additional statistical or machine learning methodologies could be investigated to augment the adaptability of performance evaluations. For instance, algorithms such as neural networks or decision trees could be integrated to analyze large-scale data, thereby uncovering more profound dependencies.

Author Contributions: Conceptualization, B.X. and L.W.; methodology, P.L.; software, P.L.; validation, P.L. and Y.W.; formal analysis, B.X., Y.W. and L.W.; investigation, P.L., F.L. and Y.W.; resources, Y.W.; data curation, B.X. and P.L.; writing-original draft preparation, F.L. and P.L.; writing-review and editing, P.L. and Y.W.; visualization, F.L.; supervision, B.X., L.W. and Y.W.; project administration, Y.W.; funding acquisition, L.W. and Y.W. All authors have read and agreed to the published version of the manuscript.

Funding: This research was funded by the Undergraduate Teaching Quality and Reform of the Institution of Higher Education (14th Five-Year Plan) of Zhejiang Province of China [grant number: JG20220151], Specific Project of MOE (Ministry of Education) Foundation for Humanities and Social Sciences [grant number: 22JDSZ3159] and Research Project of Talent Cultivation in Ningbo 2024 [grant number: T24c11].

Data Availability Statement: The data that support the findings of this study are available from the corresponding author upon reasonable request.

Conflicts of Interest: The authors declare no conflict of interest.
