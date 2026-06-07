# OPEN An evaluation method for HMI of deep-sea manned submersible based on human reliability 

Yao Zhou ${ }^{1 \odot}$, Dengkai Chen, Jianghao Xiao \& Hanyu Wang<br>Improving the human reliability of the human-machine interface (HMI) of deep-sea manned submersible is of great importance for the development of the deep-sea field. Based on the SHEL (Software S, Hardware H, Environment E, Liveware L) model, this study classifies the performance shaping factors (PSF) that affect the human reliability of submersible HMIs and builds a PSF system. The interpretative structural model (ISM) is used to matrix the interactions between the elements that make up the system of PSF. A multi-level recursive structure is obtained by building the corresponding adjacency matrix. The Noisy-OR model is introduced to construct a Bayesian network in order to build a new HMI evaluation method. A real case of Bayesian network causal inference verifies the validity of the built method. This study proposes a set of HMI human reliability evaluation methods applicable to deep-sea manned submersible, which provides a new idea for human reliability assessment.

Abbreviations<br>HMI Human-machine interface<br>PSF Performance shaping factors<br>ISM Interpretative structural model

The interior of a deep-sea manned submersible is confined and narrow. The special operating environment requires the submariner to judge and control the mission with experience and feedback from the equipment in a harsh and complex space. The HMI in the submersible mainly consists of the interface display and the console operation, which is the main medium of interaction between the submariner and the machine. Studies have shown that the main cause of HMI accidents is human factors ${ }^{1}$. The confined space, complex structure and high operational precision required inside the submersible make it extremely prone to human factors errors. Scholars have investigated the human reliability of HMI in many ways, such as Evica's analysis of the HMI in the cockpit of an aircraft using a systematic human factor error prediction method, which showed that low human reliability of the interface was the main cause of human errors in pilots ${ }^{2}$. Zhang et al. provided quantitative assessment data for the interface human reliability analysis of ship navigator by building an improved CREAM (Cognitive Reliability and Error Aanalysis Method, CREAM) model ${ }^{3}$. Zhang et al. optimises the design of the navigation interface of a deep-sea manned submersible to improve its interface usability from a human factor perspective ${ }^{4}$. Zhang et al. assessed the human reliability of submariners by establishing the probability of cognitive errors as a function of efficiency in a thermal environment ${ }^{5}$. Miao et al. decomposes the interactive interface of the manned submersible and optimally designs a new interface system from the perspective of optimal operational process ${ }^{6}$.

Methods of studies on human reliability are equally numerous, for example, Yuan et al. proposed a new controller interface-oriented human reliability analysis method based on the Delfino method and Bayesian networks, and the reliability of the method was verified by combining with actual cases ${ }^{7}$. Zhang et al. identified human reliability assessment models for the HMI by improving the CREAM method between controllers and pilots and between dispatchers and pilots, respectively ${ }^{8,9}$. Hao et al. established a pilot human error analysis model from qualitative and quantitative perspectives based on the human reliability design requirements of the HMI in the aircraft cockpit, combined with the basic theory of cognitive behavior ${ }^{10}$. Wang et al. enhanced aircraft cockpit HMI human reliability by constructing a CPC (Common Performance Condition) effect-based fuzzy set and extending CREAM to calculate pilot cognitive failure probability ${ }^{11}$. Zhu et al. used fuzzy deduction and BP neural network and forward-backward algorithms to implement the reliability calculation of the HMI in the cockpit landing phase of a civilian aircraft ${ }^{12}$. The essential behavioral formation factors (PSF, Performance Shaping Factors) that affect human reliability have also been investigated. Kim et al. pointed out that the study of

[^0]
[^0]:    Northwestern Polytechnical University, No. 127 West Youyi Road, Beilin District, Xi'an 710072, Shaanxi Province, China. ${ }^{1 / 2}$ email: zhouy@mail.nwpu.edu.cn

PSF in different contexts could significantly improve the human reliability of HMI in nuclear power plants^{13}. Liu et al. redefined four types of PSF for nuclear power plant control rooms based on the expert correction method and successfully reduced the probability of human errors^{14}. Yeong et al. used the CREAM analysis method to analyse HMI PSF in nuclear power plants, and the results showed that optimal HMI design and adequate training helped to improve operator performance^{15}. Liu et al. established a basis for quantitatively studying the causal relationships between PSF by improving the Standardised nuclear Power plant Risk Analysis-Human reliability analysis (SPRA-H) method^{16}. Yang et al. constructed a Bayesian network to predict controllers' probability of human error in multiple tasks using air control behavior formation factors as root nodes, and the results showed that Bayesian networks are more advantageous in studying this problem^{17}. From the above, most scholars have analysed the essential PSF affecting human reliability, but few have studied the interactions between PSF. Bandeira pointed out that correlations between PSF are prevalent in complex civil air transport systems and that they have a significant impact on pilot performance and the success or failure of tasks related to flight procedures^{18}. Obviously, the exploration of correlations between PSF is also one of the keys to improving the human reliability of HMI, but few studies have been carried out on the reliability of HMI for deep-sea submersible. Previous studies have only compared the sensitivities of different types of PSF, which not only lack comparability between the data, but also the conclusions obtained were not convincing. In the traditional study of PSF, only a single dimension is considered to affect human factor reliability. Most studies on human factor reliability were conducted in the dimension of "human" or "machine"^{16}. Compared to analysing PSF from the perspective of individual factors, the use of different dimensional analyses allows for a better identification of the influential interactions between the various factors.

This study investigates the interactions between the factors that affect the HMI PSF of a deep-sea manned submersible. A more comprehensive and systematic evaluation method is built to improve the HMI human reliability of manned submersibles. It provides a more scientific and effective guidance for the design of the HMI while improving the operational efficiency of deep-sea manned submersible.

## Method

HMI PSF for submersibles. The cockpit of an aircraft and a deep-sea submersible are both confined and complex human--machine environments. In 1972, Edward first proposed the principle of a specific system interface for "human" in safety work, which consists of the following elements: Software, Hardware, Environment and Liveware^{19}. The initials of these four elements are used to represent the SHEL model. Errors tend to occur at the central point of contact between human and hardware, software, environment and liveware. The model depicts the vulnerability of modern production and is a direct guide to safety work. The interfaces described are not only found on the front line, but at all levels of the production organization, so the model is universally relevant. Based on the definition of the SHEL model, this study divided the elements covered by the submersible HMI into four aspects: system staff (L), system software (S), system hardware (H) and system environment (E), and the assessment was determined as a study of the interaction between L--L, L--S, L--H and L--E. A summary of the navigation-related literature and an interview survey with experts in the field of navigation yielded a total of 28 PSF, as shown in Table 1.(1) L--L: Study of the interactions between submariner and team members in terms of information exchange and operational collaboration capabilities.(2) L--H: Study of the interaction between submariner and hardware operational equipment.(3) L--S: Study of the interactions between submariner and software interfaces.(4) L--E: Study of the interactions between submariner and the operating environment of the submersible's working chamber.

A system of PSF for submersible HMI. A questionnaire was used to investigate and analyse the 28 PSF obtained to build a HMI human factor reliability PSF system for deep-sea manned submersible.

Questionnaire study. The questionnaire was administered to those who had experience in operating deep-sea submersibles (i.e. submariners, submarine trainees in training, etc.), were all male and had an average age of around 37 years old. The main information in the questionnaire consisted of basic information and PSF on human reliability, using a 5-point Likert scale, with 1 being "minimal impact" and 5 being "great impact". A small pre-sample survey was conducted to ensure the validity of the questionnaire before distribution. Before completing the questionnaire, we informed all participants of the purpose of the study and had them sign the questionnaire informed consent form. We prepared a small gift for each participant who completed the questionnaire. A total of 260 questionnaires were returned, of which 243 were valid, and a reliability check was conducted on the returned questionnaires to ensure the validity of the data. The demographic information from the questionnaire was shown in Table 2.

Usability testing of questionnaire. The reliability coefficient of the questionnaire as a whole was calculated by SPSS software to be 0.88 , which indicates good consistency of the questionnaire. The same reliability test was conducted for the four pre-defined assessment dimensions in this study, and the results are shown in Table 3.

The results in the table show that the alpha coefficients of the four assessment dimensions are $L-L(0.94), L-H$ (0.86), $L-S(0.82)$ and $L-E(0.95)$, which were all greater than 0.6 . According to the reliability test conditions of


Table 1. Deep-sea manned submersible HMI PSF summary.


Table 2. Demographics of the questionnaire.


Table 3. Questionnaire reliability testing.
the questionnaire, the alpha coefficient is greater than 0.6 , indicating that the factors present good consistency in all interactive categories and reach the requirements of the reliability test.

The 28 PSF were analysed for association validity with the four dimensions ( $L-L, L-H, L-S, L-E$ ). The PSF for the four dimensions were $S_{1}-S_{9}(L-L), S_{10}-S_{17}(L-H), S_{18}-S_{25}(L-S)$ and $S_{26}-S_{28}(L-E)$, and the results of the analysis were shown in Table 4.

KMO (Kasier-Meyer-Olkin measure of Sample Adequacy) is the value of sampling appropriateness, which can determine the correlation and bias between sample data. The higher the KMO value, the stronger the correlation between the sample data. Bartlett's sphericity test can detect the independence relationship between variables. In this study, the questionnaire data obtained were analysed using SPSS software. The KMO test value for the questionnaire was 0.856 and the Bartlett's spherical test approximate chi-square was 1868.7. The data results obtained reached the requirements of the factor analysis. The initial component matrix was rotated using the maximum variance method to obtain the rotated component matrix. After removing the factors with factor loadings less than 0.6 (PSF number: $S_{1.7,8,12}$ ) and multiple loadings greater than 0.2 from the rotation matrix, the data were retested for KMO values and Bartlett's spherical test.

PSF system. The four PSF that did not match the data test results were Physical performance, Reasonable staff selection and deployment, Clear division of labour and responsibility, Display and control device layout. After removing the unqualified data (Sig. $P>0.05$ ), all PSF were renumbered. A final system of PSF containing 4 dimensions was established. This system of indicators reflects the influence of the HMI of deep-sea manned submersibles on the behavioral operations of submariners, as shown in Fig. 1.


Table 4. Correlation analysis of PSF with dimensions. ${ }^{* *} \mathrm{P}<0.01,{ }^{*} \mathrm{P}<0.05$.
![img-0.jpeg](img-0.jpeg)

Figure 1. System of PSF for manned submersibles.

Ethical approvals. The study received ethical approval from the Human Research Ethics Committee of Northwestern Polytechnical University (Ref No: 245/2023). In addition, the Key Laboratory of Ergonomics of the Ministry of Industry and Information Technology of China and the Institute of Industrial Design of Northwestern Polytechnical University approved the use of the research site (Ref No: 24/2023). All relevant guidelines,

procedures and regulations were followed. The experts involved in the study provided written informed consent. All participants were informed that they were free to withdraw from the study at any time without consequences.

## Model for human reliability evaluation

To identify the effects between the factors, this study combines an interpretative structural model with a Bayesian network to model the interactions of PSF for manned submersibles. Firstly, the interpreted structural model is used to obtain the hierarchical structure and map the model into a Bayesian network to complete the topology. Secondly, the Bayesian network data was populated by obtaining the prior probabilities of the root nodes and the conditional probabilities. Finally, a complete Bayesian network model was built to quantify the strength of the coupling interactions between the PSF.

Interpretative structural models for PSF. ISM can build the correlation relationship between elements and achieve the building of multi-layer ladder models through matrix operations and directed graphs, and then obtain a clear system structure and hierarchy. In this study, we used ISM to sort out the PSF affecting human reliability, and determined the interactions between PSF factors by building reachability matrix. The classification of all PSF levels based on the reachability matrix. The relevant PSF factors were connected through directed arcs to build a ISM of PSF for the HMI of a deep-sea manned submersible, shown in Fig. 2.

As shown in Fig. 2, the ISM of PSF was divided into 3 levels. A hierarchical progressive interpretive relationship existed at each level from bottom to top. This study combined the four dimensions of L-L, L-H, L-S and L-E to analyse the model as follows:The direct cause of errors were the first level. In other words, the submariner's fatigue level (S_{1}), knowledgeskills and performance (S_{3}), concentration level (S_{4}), and level of teamwork (S_{6}) in the L-L dimension were the direct causes of human-caused errors of the submariners.The indirect causes of errors were the second level. In particular, the L-L dimension includes the factor of emotional status (S_{2}). The L-H dimension includes the factors of information conveyed through digital interfaces (S_{7}), signs for directions (S_{8}), display and control device layout (S_{9}), seats & chairs (S_{11}), communication equipment (S_{12}), workstation alarm equipment (S_{13}). The L-S dimension includes the factors of integrity of the interface display (S_{14}), reasonableness of the software feedback system (S_{15}), integrity of the software operating procedures (S_{17}), reasonableness of system operation time (S_{18}), emergencies and Preparedness (S_{19}), system security level (S_{20}), system interconnection level (S_{21}).The deeper causes of errors were the third level. The awareness of work responsibility (S_{3}) factor in the L-L dimension. The general layout of the space (S_{10}) factor in the L-H dimension. The adequacy of software system training (S_{16}) factor in the L-S dimension. The all factors (S_{22}-S_{24}) of L-E dimension.

Human reliability analysis based on Bayesian networks. Fuzzification of node occurrence probabilities. The model was adjusted using the causal graph correction method^{33}. The final Bayesian network topology based on the interpreted structural model was established, as shown in Fig. 3.

This study assumed that each node in the network hierarchy consists of two states that have a positive and negative impact on human reliability. The node state settings and meanings were shown in Table 5. The mapping relationship between natural linguistic variables and fuzzy numbers was established using the natural linguistic variables description method, and the correspondence between linguistic variables and triangular fuzzy numbers is shown in Table 6.$$\mathrm{ISM}=1.0 \mathrm{~S}_{10} \mathrm{~S}_{24} \mathrm{~S}_{16} $$

![img-1.jpeg](img-1.jpeg)

**Figure 3.** The ISM-based Bayesian network.


**Table 5.** Meaning of all node states.

*Synthesis of fuzzy probabilities.* When inviting experts to score, because each expert has a different educational background, knowledge base and level of perception, it can easily lead to conflicting opinions during the group's decision-making process. In this study, the Similarity Aggregation Method (SAM)34 was used to process the expert opinions in order to enable a consensus of expert opinions. The steps of SAM were as follows:

*Step 1:* Experts' similarity calculations for opinions.

Suppose the set of experts was *E_{k}* (k = 1, 2, ..., n), and *R_{w}*, *R_{v}* were used to represent the opinions of any two experts, then *R_{u}* = (*r_{u1}*, *r_{u2}*, *r_{u3}*) and *R_{v}* = (*r_{v1}*, *r_{v2}*, *r_{v3}*), and the similarity function *S_{uv}* of experts *E_{u}* and experts *E_{v}* was shown in the formula (1). *R_{u}* and *R_{v}* were the standard triangular fuzzy numbers for expert opinion. The similarity function takes on a value between 0 and 1, with larger values representing higher similarity. In these formulas k is the number of experts. *R_{u}* and *R_{v}* represent the u and v experts, respectively. *r_{u1}* represent the education level of the *R_{u}* expert. *r_{u2}* represent the knowledge level of the *R_{u}* expert. *r_{u3}* represent the perception


Table 6. Correspondence between natural language variables and triangular fuzzy numbers.
level of the $R_{i v}$ expert. $r_{v 1}$ represent the education level of the $R_{v}$ expert. $r_{v 2}$ represent the knowledge level of the $R_{v}$ expert. $r_{v 3}$ represent the perception level of the $R_{v}$ expert.

$$
S_{u v}=1-\frac{1}{3} \sum_{i=1}^{3}\left|r_{u i}-r_{v i}\right|
$$

Step2: Calculation of the average agreement of experts.
The average agreement $A_{A}\left(E_{k}\right)$ was calculated using the formula (2).

$$
A_{A}\left(E_{k}\right)=\frac{1}{k-1} \sum_{u \neq v}^{k} \sum_{v}
$$

Step3: Calculation of the relative agreement of experts.
The relative agreement $R_{A}\left(E_{k}\right)$ was calculated using the formula (3).

$$
A_{R}\left(E_{k}\right)=\frac{A_{A}\left(E_{k}\right)}{\sum_{k=1}^{n} A_{A}\left(E_{k}\right)}
$$

Step4: The agreement factor for experts $C\left(E_{k}\right)$ was calculated as shown in formula (4).
In the formula: $w\left(E_{k}\right)$ being the weight of the expert; $\beta$ is the slack factor, $\beta=0$ when no expert weight is considered.

$$
C\left(E_{k}\right)=\beta \cdot w\left(E_{k}\right)+(1-\beta) \cdot A_{R}\left(E_{k}\right)
$$

Step5: The aggregation of expert opinion $\bar{R}_{A G}$ is calculated as shown in formula (5).

$$
\bar{R}_{A G}=\mathrm{C}\left(E_{1}\right) \cdot \bar{R}_{1}+\mathrm{C}\left(E_{2}\right) \cdot \bar{R}_{2}+\cdots+\mathrm{C}\left(E_{k}\right) \cdot \bar{R}_{k}
$$

The aggregation of PSF $S_{14}$ was used as an example to illustrate the calculation process. Firstly, the semantic values of experts' fuzzy judgments for node $S_{14}$ at "STATE $=1$ " were collected and then mathematically calculated according to the above method. After the aggregation of experts' opinions, the triangular fuzzy number of $S_{14}$ was $(0.00,0.08,0.21)$.

Defuzzification of data. Defuzzification is the mathematical calculation of fuzzy probabilities to obtain an exact value. In this study, the mean area method was used for defuzzification. The formula for defuzzification is shown in formula (6), where $(a, m, b)$ represents a set of fuzzy numbers and $P$ was the value after deconvoluting the triangular fuzzy numbers.

$$
P=\frac{a+2 m+b}{4}
$$

The results for the root node $S_{14}$ :

$$
P=\frac{0.00+2 \times 0.08+0.21}{4}=0.09
$$

Obtaining conditional probabilities for Bayesian networks. The Noisy-OR model can significantly reduce the number of parameters required to populate the CPT (Conditional Probability Table, CPT) of an event probability table in a Bayesian network. The Noisy-OR model was used in this study to describe the interaction between the cause of an event and its resulting impact. Suppose a binary variable $Y$ which has $n$ binary parents of $X$. Each variable has two states 0,1 ( 0 for not occurring and 1 for occurring) as shown in Fig. 4.

After obtaining the conditional probabilities of child nodes independently influenced by parent nodes, the conditional probabilities of multiple parent nodes acting together can be calculated. The calculation formula was given in (8) and (9).

![img-2.jpeg](img-2.jpeg)

**Figure 4.** Diagram of the Noisy-OR model.

$$P(Y \leftarrow X_i) = P(B|\overline{X}_1, \overline{X}_2..., X_i..., \overline{X}_n) \tag{8}$$

$$P(Y) = 1 - P(y \leftarrow X_p) = \Pi_{X1} \epsilon_{Xp}(1 - P(y \leftarrow x_i)) \tag{9}$$

In the formula: $X_i$ indicates that node $X_i$ occurs, $\overline{X_i}$ indicates that node does not occur; $X_p$ indicates that simultaneous parent node union occurs; $P(Y \leftarrow X_i)$ indicates the probability of occurrence of node $Y$ when parent node $X_i$ was independently influenced. The calculation process for node $S_4$ was used as an example for illustration. The conditional probability that node $S4$ was under the influence of the parent node alone was:

$$P(S_4 \leftarrow S_{22}) = 0.34, P(S_4 \leftarrow S_7) = 0.27, P(S_4 \leftarrow S_2) = 0.58, P(S_4 \leftarrow S_{20}) = 0.65, P(S_4 \leftarrow S_{24}) = 0.77, P(S_4 \leftarrow S_{13}) = 0.46, P(S_4 \leftarrow S_{14}) = 0.75, P(S_4 \leftarrow S_{15}) = 0.35, P(S_4 \leftarrow S_{18}) = 0.52.$$

Calculate the conditional probability under the joint action of multiple parent nodes:

$$P(S_4 \leftarrow S_{22}, S_7, S_2, S_{20}, S_{24}, S_{13}, S_{14}, S_{15}, S_{18}) = 1 - [1 - P(S_4 \leftarrow S_{22})] \cdot [1 - P(S_4 \leftarrow S_7)] \cdot [1 - P(S_4 \leftarrow S_2)] \cdot [1 - P(S_4 \leftarrow S_{24})] \cdot [1 - P(S_4 \leftarrow S_{24})] \cdot [1 - P(S_4 \leftarrow S_{13})] \cdot [1 - P(S_4 \leftarrow S_{15})] \cdot [1 - P(S_4 \leftarrow S_{15})] \cdot [1 - P(S_4 \leftarrow S_{18})] = 1 - (1 - 0.34) \cdot (1 - 0.27) \cdot (1 - 0.58) \cdot (1 - 0.65) \cdot (1 - 0.77) \cdot (1 - 0.46) \cdot (1 - 0.75) \cdot (1 - 0.35) \cdot (1 - 0.52) = 0.99.$$

**A case of human reliability analysis.** A real-life case from the China Deep-sea Warrior manned submersible safety case compilation was selected for this study. According to the incident report, the submersible was on a 4500 m class sea trial. During the submersible's powered dive to sit on the bottom, the submariner failed to adjust the ballast water tank volume. The submersible's thrusters were underpowered triggering Inadequate Power's working chamber alarm, constituting a serious error event for the safety of a manned submersible.

*Probability calculation of case events.* Five experts in the field were invited to conduct interviews for this study. The experts gave fuzzy judgement values for PSF at "STATE = 1" based on practical experience and basic event information, and we used the formula to calculate the conditional probabilities under the influence of different

![img-3.jpeg](img-3.jpeg)

**Figure 5.** Diagram of Bayesian network causal inference. Data in a figure from *Nietica V5.18* version of software to access the address: http://www.3h3.com/soft/163546.html.

combinations of parent nodes. As shown in Fig. 5, the human factor reliability (S_{h}) probability for the HMI of this manned submersible was calculated to be 49.1% using Netica software, which is generally consistent with the state of the submersible during operation. Netica is the most widely used Bayesian network analysis software in the world.

The manned submersible was diving to sit on the bottom when the divers neglected to adjust the amount of water in the ballast water tanks. After the alarm the submariner recognized the error and ballast water was fed into the tanks in time for the subsequent dive to proceed normally without making a major error. This coincides with the results of this study and verifies the applicability of the proposed Bayesian network approach based on an interpreted structural model for the human reliability evaluation of the HMI of deep-sea manned submersibles.

Analysis of key PSF affecting human reliability. Suppose that the human interface of the manned submersible was in a negative state due to low human reliability. Set the state P(S_{h} = 1) = 100% of node S_{h}, update the probability parameters of the network and get the posterior probability of each node. By comparing the prior probability with the posterior probability, the sensitive factors affecting the human factor reliability can be identified based on the before and after change values. The results obtained were shown in Table 7.

## Discussion

In this study, a system of PSF was proposed, consisting of four different dimensions, L-L, L-H, L-S and L-E. The following discussion was conducted in this study.

The fatigue level factor had the highest impact in the L-L dimension. The results of this study showed that individual fatigue was a key factor affecting the human reliability of the manned submersible human-machine interface, which was the same as the results found in many previous studies. Many safety incidents occur as a direct result of individual fatigue^{35--37}. The small and confined space inside a manned submersible can easily cause submariner fatigue. Studies have shown that when operators return to work after a period of temporary absence from the task, it significantly increases staff resourcefulness, so appropriate breaks can be used as a risk management measure^{38}. All submariners were tested for fatigue prior to entering the submersible, but due to the long duration of the dive and the small confined working area fatigue can easily be generated. Managers need to monitor submariner fatigue in order to develop effective management measures to cope with the demands of the submariner's position.

The seats & chairs factor had the highest impact in the L-H dimension. In the hardware environment of the HMI, the seat & chairs was a key factor in the human factor reliability. This differs from the results


Table 7. Comparison of probabilities of each node of Bayesian networks.

of other studies. This is probably due to the small space inside the submersible and the predominantly sideways working position of the submariners. Such a position is not common in daily work, and prolonged lying on one's side is more likely to cause discomfort than a sitting position^{39}. As a result, a higher level of design is required of the designers. The designers have to take into account the working characteristics and habits of the submariners and adopt a more humane design to meet the special requirements of the submarine process.

The reasonableness of system operation time factor had the highest impact in the L-S dimension. At present, most of the ICAO member states have regulations on the maximum flight time and the duration of a single work session for pilots^{40}. However, for the manned submersible field, there is no standard work duration regulation, moreover, there is a lack of detailed work time limits and arrangements. The work of submariners requires alternating day and night, which is physically demanding. Previous studies have pointed out that alternating day and night shifts require full consideration of human adaptability, with night and day shifts needing to be at least 48 h apart when they cross over^{41}. The results of this study could provide insights into the development of the submersible field.

The noise and vibration factor had the highest impact in the L-E dimension. Noise and vibration have emerged as key causes of psychological and physiological effects on individuals in confined human--computer interaction spaces. This is consistent with the model results presented in this study. The sound pressure level of the noise source can be controlled by, for example, arranging some sound insulation and absorption materials, vibration isolation and vibration absorption structures in the bulkhead of the submersible.

Limitations. There are a number of limitations to the results of this study that may affect the generalisability of the model. Firstly, the initial identification of 28 PSF does not fully describe all the factors influencing human reliability. The human--machine interface of a manned submersible is constructed in a complex manner, which includes many other influencing factors. Although we obtained some important influencing factors through literature and expert interviews, more PSF will be included in the future to ensure the accuracy of the model as the internal design of the manned submersible is continuously updated. Secondly, this study has fuzzed the experts' opinions, and although some of the subjective differences can be removed to a certain extent, there is still some subjectivity, and it is important to remove as much error as possible from subjective results in future studies.

# Conclusion 

This study analyses the human reliability of the HMI of deep-sea manned submersibles. By analyzing the relationship between four dimensions of PSF, we proposed a human reliability evaluation method for the human--machine interface of deep-sea manned submersible. Our innovation mainly includes the following aspects:Four dimensions were selected to evaluate the human factor reliability of deep-sea manned submersible.In addition to the effects of individual PSF on human factor reliability, we also analyzed the correlation effects between PSF.The fatigue level factor had the highest impact in the $L-L$ dimension. The Seats \& Chairs factor had the highest impact in the $L-H$ dimension. The Reasonableness of system operation time factor had the highest impact in the $L-S$ dimension. The Noise and vibration factor had the highest impact in the $L-E$ dimension.

The method allows for a more scientific evaluation study of the HMI of manned submersibles.

## Data availability

The datasets used and/or analyzed during the current study are available from the corresponding author upon reasonable request.

Received: 24 March 2023; Accepted: 21 August 2023
Published online: 04 September 2023

# Acknowledgements 

Key Research and Development Program of Shaanxi Province "Research on dynamic three-dimensional measurement and adjustment model of operational comfort of manned confined compartment" (Grant No. 2022GY311), and the Project of Shaanxi Province Special Support Program for Leading Talents, (Grant No. W099115).

## Author contributions

Y.Z., J.X. and H.W. wrote the main manuscript text and prepared all figures and tables. D.C. checked the scientific soundness and correctness of the manuscript. All authors reviewed the manuscript.

## Competing interests

The authors declare no competing interests.

## Additional information

Correspondence and requests for materials should be addressed to Y.Z.
Reprints and permissions information is available at www.nature.com/reprints.

Publisher's note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
(c) The Author(s) 2023