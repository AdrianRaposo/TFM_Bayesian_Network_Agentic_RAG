Authors' pre-print:
Duncan Taylor, Bas Kokshoorn, Alex Biedermann, Evaluation of forensic genetics findings given activity level propositions: A review, Forensic Science International: Genetics https://doi.org/10.1016/j.fsigen.2018.06.001

# TITLE: 

Evaluation of forensic genetics findings given activity level propositions: A review

## AUTHOR:

Duncan Taylor ${ }^{1,2}$, Bas Kokshoorn ${ }^{3}$ and Alex Biedermann ${ }^{4,5}$

1. Forensic Science SA, PO Box 2790, Adelaide, SA 5000, Australia
2. School of Biological Sciences, Flinders University, GPO Box 2100 Adelaide SA, Australia 5001
3. Department of Biological Traces, Netherlands Forensic Institute, P.O. Box 24044 NL2490AA, The Hague, The Netherlands
4. Faculty of Law, Criminal Justice and Public Administration, School of Criminal Justice, University of Lausanne, Lausanne-Dorigny, Switzerland
5. Visiting researcher, University of Adelaide Law School, Litigation Law Unit, Adelaide, SA 5000 Australia.

## CORRESPONDING AUTHOR:

Duncan A. Taylor, PhD
Forensic Science SA
GPO Box 2790
Adelaide SA 5001
Australia
Phone: $+61-882267700$
Fax: $+61-882267777$
Email: Duncan.Taylor@sa.gov.au

# HIGHLIGHTS: 

- The need of support for inference 'beyond the source' is increasing
- Evaluation given activity level propositions has solid logical foundations
- Bayesian networks are valuable tools to make reasoning transparent
- International high-profile cases teach insightful lessons for further research


## ABSTRACT:

The evaluation of results of forensic genetic analyses given activity level propositions is an emerging discipline in forensic genetics. Although it is a topic with a long history, it has never been considered to be such a critically important topic for the field, as today. With the increasing sensitivity of analysis techniques, and advances in data interpretation using probabilistic models ('probabilistic genotyping'), there is an increasing demand on forensic biologists to share specialised knowledge to help recipients of expert information address mode and timing of transfer and persistence of traces in court. Scientists thereby have a critical role in the assessment of their findings in the context of the case. This helps the judiciary with activity level inferences in a balanced, robust and transparent way, when based on (1) proper case assessment and interpretation respecting the hierarchy of propositions (supported by, for example, the use of Bayesian networks as graphical models), (2) use of appropriate data to inform probabilities, and (3) reporting guidelines by international bodies. This critical review of current literature shows that with certain prerequisites for training and quality assurance, there is a solid foundation for evidence interpretation when propositions of interest are at the 'activity level'.

## KEY WORDS:

Evidence evaluation; Bayesian networks; likelihood ratio; DNA; activity level propositions.

## 1. INTRODUCTION

### 1.1 What is an evaluation considering activity level propositions?

When evaluating scientific findings in a forensic context, three fundamental principles should be at the forefront of the scientist's mind e.g. [1]:

1) The findings should be evaluated within a framework of circumstances: this framework is commonly denoted by ' $I$ ', which by convention stands for Information. ${ }^{1}$
2) The findings should be evaluated given two competing, mutually exclusive propositions: generally, propositions are denoted ' $H p$ ' for the prosecution proposition and ' $H d$ ' for the defence proposition ${ }^{2}$.
3) The role of the expert should be to consider the probability of the findings given the propositions and not the probability of the propositions themselves: findings are commonly denoted ' $E$ ', which by convention stands for Evidence. Note that 'the probability of the evidence, given the proposition' has been referred to as "the single most important lesson for evaluative forensic science" [3].
These, principles are based on earlier works by Evett and Weir [4], which in turn are extensions of many published works on probabilistic inference not listed here. These principles naturally lead to the likelihood ratio (LR):
$L R=\frac{\operatorname{Pr}(E \mid H p, I)}{\operatorname{Pr}(E \mid H d, I)}$
Once a likelihood ratio has been assigned, for example in the order of magnitude ' M ', it allows scientists to give statements of the following general form (example):
"My evaluation is based on the information (I) that I have been provided. Taking this information into account, the probability of obtaining the findings (E) is about M times higher if the prosecution's proposition $(\mathrm{Hp})$ is true rather than if the defence's proposition $(\mathrm{Hd})$ is true."

The general formula for the likelihood ratio given in equation 1, and the statement that follows, applies to all forms of evidence evaluation, regardless of the propositions and the nature of the findings being considered. The important point to note is that as the propositions or (I) change, then the findings that should be included within $E$ may also change. For example, if information is provided that accounts for part of the findings, then the results to assess may be different than if the information had not been given.

In the late 1990s, work was carried out that defined several broad categories within which propositions can be formulated, ranging from those that focus on the origin or source of particular physical traces (e.g. glass fragments, biological material, fibres, etc.) to those that

[^0]
[^0]:    ${ }^{1}$ Not all available information is necessarily relevant for the evaluation of findings by forensic scientists. Information should be relevant for the evaluative task at hand (e.g. 'task-relevant; see also [2])
    ${ }^{2}$ The use of these mathematical terms are useful in formal and technical discussions, though in written reports to recipients of expert information it may be preferable to avoid mathematical notation.

address the ultimate issue on which the Court is reaching a decision. This, 'hierarchy of propositions' has proven fundamental for furthering the forensic science community's understanding of the propositional levels that condition the evaluation of scientific findings [5-7]. In particular, it has been realized that the higher up the hierarchy the propositions are, against which the scientists are competent to evaluate their results, the more directly useful the testimony will be to the court, thereby limiting the risk of unwarranted carrying over of forensic findings to conclusions (i.e., other propositional levels) that go beyond the scientist's testimony [8]. The positions within the hierarchy are shown in Figure 1, and we briefly explain each below, within the context of a hypothetical alleged rape, in order to delineate our field of enquiry to activity level propositions.

# 1.1.1 Offence level propositions 

This propositional level reflects the ultimate issue on which the Court must decide. Offence level propositions typically possess a component that relates to an activity (such as having sexual intercourse, punching someone or shooting a firearm at someone) as well as several legal components such as intent, premeditation, excuses and justifications. Rape is defined differently in various legal systems: usually, it refers to a sexual contact of someone with a person who did not consent to it. Examples of propositions may be: 'The accused raped the victim' versus 'the accused did not rape the victim'. Note, however, that the simple negation of the first proposition rarely provides a suitable alternative proposition [5]. An alternative proposition needs to be explicit, for example: 'The accused had consensual sex with the victim', 'Someone other than the accused raped the victim', or 'no-one raped the victim'.

### 1.1.2 Activity level propositions

Propositions at this level, our main focus in this review, specify activities that putatively took place as part of the defence or prosecution version of the event of interest. In the case of the rape scenario the activity in question would be the sexual activity that is making up part of the prosecution's case. If the defence case is one of consent, then the same activity would be conceded by both parties and so, given this information, DNA results would be of little help ${ }^{3}$ (except if, for example, different timings are alleged so that considerations of persistence may help in the case). If the sexual activity is not being conceded, then some examples of

[^0]
[^0]:    ${ }^{3}$ In many jurisdictions no exhibits would be accepted or examined by the forensic science laboratory where consent is an issue. Examinations may still occur with the understanding that a statement given by the defendant during the investigative phase of the case can change by the time the case goes to court.

competing activity level propositions may be: 'The accused had sex with the victim' versus 'The accused only socially interacted with the victim'. Other defence propositions may be 'The accused assisted the victim get into bed' or 'The victim wore clothes loaned to them by the accused'. Any number of possible activity level propositions could apply, depending on the framework of circumstances surrounding the case.

Note that the following are not activity level propositions as understood under this framework: 'The recovered DNA is the result of primary transfer' versus 'The DNA is the result of secondary transfer' (or 'The recovered DNA is the result of contamination)'. Such formulations are explanations [7], not propositions, and are deficient in at least two ways. First, they factor findings into propositions [9] (i.e. the finding of DNA is part of the proposition). Second, they confuse the phenomenon of transfer (i.e., a variable conditioning the evaluation) with the posited activities of interest [8]. Activity level propositions, by definition, must specify alleged activities (by a person). Transfer is an event of interest, about which uncertainty exists, and that is taken into account in the scientist's assessment when evaluating findings given activity level propositions, but it does not define competing propositions in the first place. Hence, scientists who assert that they can "(...) assess whether they [the DNA profiles] originated either due to primary or secondary transfer, and indicate the likelihood of their chosen answer (definitively primary or secondary transfer; most likely (...)" [10], are not testifying in terms of Equation (1) mentioned above, that is the probability of the evidence given the proposition. Instead, they express opinions on events of transfer that the recipient of expert information may wrongly interpret as conclusions about competing activity level propositions.

A further area of concern is so-called 'pseudo-activity' evaluations [7] where scientists formulate propositions such as 'The person of interest was in recent contact with the victim'. Here, the pseudo-activity level consists in the spurious suggestion of an activity level proposition, while confining the evaluation only the rarity of the analytical features (i.e., reducing considerations to an evaluation given source level propositions), omitting the assessment of factors such as transfer, persistence and background. The additional issue with these types of propositions is the use of vague terminology, such as 'recent' and 'contact'.

# 1.1.3 Source Level 

Propositions at the source level question the cellular origin of the examined material. In forensic genetics, this will typically be the biological source, such as blood, semen, saliva, trace DNA, etc. Propositions that are below activity level propositions in the hierarchy have

been called intermediate association propositions [11] as they typically do not correspond to the questions of primary interest to court. There is always a dispute of activity that would lead to a dispute in source, for example if the activity level propositions such as 'The accused had sex with the victim' and 'The accused assisted the victim to get into bed' from earlier were considered, then it is likely that there is a dispute of the cell type from which the recovered DNA has originated. One could consider that this leads to the source level propositions relating to an intimate swab of the victim: 'The accused's sperm is present on the sample' versus 'The accused's trace cellular material is present on the sample'. As may be gleaned from the propositions, there is a limitation with propositions below activity level in that the propositions cannot be set until some findings are obtained (or risk being unsuitable). It would make no sense to evaluate the findings, given the source level propositions above, if no genetic material was found. However, regardless of whether any genetic material from was found, it can still be sensible to use activity level propositions for the evaluation of the findings.

# 1.1.4 Sub-source Level 

This propositional level relates mainly to DNA results [11]. Propositions at this level focus on the source of DNA within an item or specimen, and not the biological material from which it came (or if it came from a contamination). Often, when low quantities of recovered material are considered, coupled with no obvious visible staining (such as might be present for a blood drop) associated with the material that has been collected, then this means that the evaluation of the findings at sub-source level usually cannot be elevated to source level. Typical propositions are in the form: 'The DNA came from the victim and accused' versus 'The DNA came from the victim and an unknown individual'. Sub-source level propositions are typically used, by default, for results obtained with the modern DNA profile analysis systems $[12-17]$.

### 1.1.5 Sub-sub-source Level

In 2013, Taylor et al [18] defined this level in the hierarchy, which again specifically relates to DNA profiling results. At this level the propositions relate to specific components within a DNA profile, rather than the whole profile (as would be considered with sub-source level propositions). Examples of sub-sub-source level propositions would be: 'The major contributor of DNA in the recovered material is the accused' versus 'The major contributor of DNA in the recovered material is an unknown individual'.

Page 7 of 54

Consent, intent, pre-meditation, relevance of items to offence, number of offenders | $[11,19-21]$  |
Transfer of DNA, persistence of DNA, recovery of DNA, background levels of biological material on items | $[6,8,19,22-29]$  |
Amount of DNA present in sample, level of degradation
Other factors:
Potential for contamination/pollution in laboratory, results of screening tests, visual appearance | $[30-32]$  |
Level of resolution between components, number of loci in the profile | $[4,33-35]$  |
Alleles present in profile component, population of alternate offenders, genotypes of contributors, proportion of alleles in population | $[18]$  |

Figure 1: Hierarchy of propositions

Keeping the various levels in the hierarchy in mind, it is useful to emphasize again that the relevant matter that the scientist may comment on is the findings given activity level propositions. Informally, this is often referred to as 'activity level reporting' although we make the point that these reports must address the findings, given the propositions, and not the propositions (hence activities) themselves. Such evaluations take into account considerations of phenomena such as transfer and persistence, but such phenomena do not as such represent the propositions of interest. To clarify this point, it is helpful to state the logic of evaluation given activity level propositions explicitly. Consider the example given in Evett and Weir (page 35 of [4]) where the finding $E$ to be evaluated is blood staining on the accused's clothing of genotype $G$, and the activity level proposition $H_{p}$ is 'The accused is the person who stabbed the victim'. Knowledge of the victim's and the accused's genotypes $G_{V}$ and $G_{S}$ is also available. To assist with the assignment of the numerator, an additional term $T$ (short for 'blood was transferred from the victim to the assailant's clothing') is introduced, with $-T$ denoting 'blood was not transferred'. The numerator is then written as

$$
\begin{aligned}
\operatorname{Pr}\left(E \mid G_{V}, G_{S}, H_{p}, I\right)= & \operatorname{Pr}\left(E \mid T, \mathrm{G}_{V}, G_{S}, H_{p}, I\right) \operatorname{Pr}\left(T \mid \mathrm{G}_{V}, G_{S}, H_{p}, I\right) \\
& +\operatorname{Pr}\left(E \mid-T, \mathrm{G}_{V}, G_{S}, H_{p}, I\right) \operatorname{Pr}\left(-T \mid \mathrm{G}_{V}, G_{S}, H_{p}, I\right)
\end{aligned}
$$

Hence, the evaluation of the finding, given the prosecution proposition includes the probability of the findings if $H_{p}$ is true and transfer has occurred, as well as when Hp is true and transfer has not occurred. This clarifies the distinct roles of notions of transfer and activity level propositions. It is also clarified that the scientist does not provide a LR for the phenomenon 'transfer', but for propositions regarding disputed activities of the person of interest.

# Recommendations by forensic bodies 

A number of advisory bodies and leading thinkers in the field of forensic science advocate the evaluation given propositions regarding activities, rather than given propositions at lower hierarchical levels (i.e., source, sub-source, or even sub-sub-source levels), specifically:

- The European Network of Forensic Science Institutes (ENFSI) [36]
- The Association of Forensic Science Providers (AFSP) [37]
- The Royal Statistical Society (RSS) [38-41]
- Forensic scientists across the world [42-45]

The cases where forensic results ought to be reported considering activity level propositions have been delineated in the ENFSI guideline for evaluative reporting [36]. It is needed, in particular, when the amount of collected trace material is low and when considerations of transfer, persistence and recovery require specialised forensic knowledge. There is a widespread recognition that there is danger in leaving such assessments to non-forensic scientists and that is the duty of the scientists to guide the court appropriately in these matters [8]. Other typical cases where the findings lead themselves naturally to an interpretation considering activity level propositions is when the source of the trace material is not disputed in the case, but only the mechanisms whereby the trace material was transferred is debated.

The ENFSI guideline said on the matter:
"Source level propositions are adequate in cases where there is no risk that the court will misinterpret them in the context of the alleged activities in the case."

Biedermann et al [8] state:
"Not pursuing this topic bears the risk of leaving recipients of expert information without guidance. Reliance on recipients' own devices is prone to conclusions that are based on (sub) source level propositions being wrongly carried over to conclusions about activity level propositions."

It has also been recognised that if the Court's question relates to activities, then a scientist should carry out an evaluation using propositions that relate to activities and not to source only (and attempting an ad-hoc consideration of the findings given posted activities during oral testimony). Vuille et al [44] state:
"If the question of interest to the fact-finder pertains to activities (such as possible contaminations, alternative transfers, innocent explanations for the presence of the material on the crime scene), the expert's report must contain a detailed description of her evaluation of the evidence under hypotheses mentioning activities. Indeed, reporting results under source level hypotheses in this context is unacceptable, because it renders the review by the defence of the expert's conclusions almost impossible: complex questions need to be assessed thoroughly, not on the stand with no preparation."

Gill [45] presented a number of examples where, through ambiguous or misstated testimony, the results of an evaluation given source level propositions was equated with an evaluation given activity level propositions. When such a carrying over occurs between sub-source and source, Gill terms this an association fallacy, though the same misinterpretation can occur between source, or sub-source, and activity.

There have been numerous publications demonstrating the importance of considering activity level propositions when evaluating forensic results [8, 19, 22-28, 43, 46]. From these references it is clear there is an increasing awareness in the forensic community of the role of the scientist in the assessment of DNA analysis results given activity level propositions. The expert plays a crucial role in the evaluation of the evidence by imparting knowledge on DNA transfer, persistence, prevalence and recovery (TPPR) to the court. This recognition of the need for activity level assessment extends to the legal community. Margot [47] states that: "The real problems of interpreting poor quality traces and mixtures have only come to the fore in recent years. These problems have illuminated the important challenge that forensic science is facing: interpreting results in view of conflicting versions of events and activities"

On the same topic, Wills ${ }^{4}$ notes (personal communication to the authors): "The mistaken idea that answering the 'who' question, based on DNA profiling, is equivalent to answering the 'who did it' question is widespread".

There have also been a number of recent court cases (which we review later in this article) that recognise the difference between source and activity level propositions, and their separate importance to the evaluation of the case findings.

# 2.0 The use of Bayesian networks 

All probabilistic evaluations of findings can be carried out by an analyst, with pen and paper, deriving an equation for the LR. For a general example, see the development for the numerator given above according to Evett and Weir [4]. The specification of LR formulae is based on the laws of probability and takes into account factors that are important in the evaluation, considering also the relationships between these factors. In many cases, particularly when multiple findings are being evaluated together, LR formula derivation may

[^0]
[^0]:    ${ }^{4}$ Sheila Wills, the former head of the laboratory Forensic Science Ireland

rapidly become complex. For an example of a likelihood ratio derivation for the probability of some findings, which takes into account not just the rarity of the genetic features, but also the number of offenders and the relevance of the exhibit, we point the reader to [11].

One common concept that assists in this task is Bayesian networks (BN), which are a graphical way of displaying and conducting complex probability computations [48]. Work is available that addresses the construction of BNs in the law field [49], using small network fragments (called idioms), that can be used as building blocks in larger BNs, such as objectoriented Bayesian networks (OOBN) [50, 51]. More general resources on BN architecture are also available [52].

There have been numerous applications of BN within forensic science ranging from quality control monitoring [53], preparation for legal challenges [54], complex pedigree evaluation [55-57], to DNA profile mixture evaluation [58], helping to address activity level propositions [6] (see, e.g., [48] for a review) and for crime level investigation [21, 59]. We direct the reader to [60] for explanations of the structure and terminology of BNs.

Several works exist that address general methodologies for constructing BN for helping with forensic genetic findings and inference about activity level propositions. A pioneering work is given by Evett et al in 2002 [6] who present examples of evaluation of small quantities of DNA in the light of proposed competing activities. They demonstrate the use and potential of BNs to evaluate forensic DNA findings in two case examples.

Kokshoorn et al [29], shows how BN construction is affected by the way that the propositions refer to the actors of the alleged crime. Specifically, they consider the presence or absence of DNA, where the defence proposition may state:

1. The activity never took place (i.e., there was no perpetrator)
2. The activity was carried out by someone other than the accused (i.e., an alternate perpetrator)
3. The accused carried out some alternate activity that led to the findings

Note that the conditions above are not mutually exclusive. Thus, it may be that the defence proposition specifies a combination of 1 and 3 or 2 and 3 (but of course 1 and 2 cannot be paired).

Taylor et al [61] give a step by step method that can be used to construct BN for forensic biology findings that are being evaluated given activity level propositions. In their work they describe a process that starts by identifying the propositions of interest, identifying all the activities that would be required under either (or both) of the propositions, then considering all the results that would be expected, and argumentatively connecting them with the propositions regarding posited activities through considerations such as transfer and persistence. Finally, 'root' nodes are considered which take into account the background presence of biological material. In following these steps, the BN can be constructed in a semi-standardised manner that assists with comprehension and review.

There is general acceptance in the forensic community of the use of a probabilistic framework for guiding evidence evaluation and that Bayesian networks are simply a graphical manner in which these evaluations can be constricted. Recommendations from forensic bodies are beginning to endorse the use of BN to help with evaluations when propositions of interest focus on activities [62] and, as demonstrated in this paper, numerous examples exist of how they can be used in a forensic context.

# 3.0 Why the current interest in evaluating findings given posited activities? 

It should be recognised that the concept of evaluating forensic findings in light of activity level propositions has a relatively longstanding history. In the late 1990s work was carried out in the UK (i.e., former Forensic Science Service) that defined the notion of activity level within a hierarchy of propositions [5] and how evaluations using this type of propositions can be used to inform customers and pre-assess cases [38, 63]. Examples of interpreting small quantities of DNA using BNs and evaluating them given activity level propositions were published in 2002 by Evett et al [6].

The prevalence of research in the area of evaluations given activity level propositions, the use of graphical models to assist in evaluations, and studies into transfer and persistence of biological material has increased considerably over the past 20 years. For example, the number of documents that are flagged per year on Google Scholar when the phrase "Forensic DNA Bayesian Network" is searched increased from less than a hundred to over one thousand (Figure 2).

![img-0.jpeg](img-0.jpeg)

Figure 2: Number of documents identified (per year) on Google Scholar by searching the phrase "Forensic DNA Bayesian Network"

The increase in interest in this area is likely due to a combination of reasons. Some of the main driving factors are:

- DNA profiling technology has improved in both the discrimination power of the profiles, and in the sensitivity of the systems used to generate them. This has caused questions in Court to largely shift from who the donor of recovered trace material is, to questions about the mechanism by which the material was deposited on the examined item/surface. This is particularly relevant when the profile has been generated from very low levels of starting DNA that cannot be assigned to a particular body fluid (commonly called 'trace DNA', 'contact DNA', 'touch DNA', 'latent DNA' or 'low template (lt) DNA').
- DNA profile evaluation has now reached a point where numerous software programs exist that can evaluate complex and low-level DNA profile data [12, 13, 17, 64-69]. These software programs provide evaluations, which will often lead to the presence or absence of DNA from nominated individuals being agreed by both prosecution and defence. This provides a strong foundation upon which evaluations, considering higher level propositions in the hierarchy, can be carried out.
- There has been an increase in the availability of software programs (and computing power to run them) that can be used to graphically display the factors, and their dependencies, that are important in the evaluation of DNA findings given activity

level propositions. These include freeware such as GeNie (https://www.bayesfusion.com/), R libraries, gRain [70] and BNlearn [71] and commercial software such as HUGIN (www.hugin.com) or AgenaRisk (http://www.agenarisk.com).

- There have been several high-profile cases that received international attention, which revolved around DNA TPPR issues (such as the Meredith Kercher case [72, 73] and the Fitzgerald case [74]) These high-profile cases are not exceptional, but reflect the increasing emphasis that is given in many jurisdictions to DNA transfer and persistence rather than questions of source only.
- An increasing body of scientific literature has furthered our understanding of processes and relevant factors in DNA TPPR (see the Oorschot et al review in this same FSIG issue). These data allow for more detailed modelling of these factors. For an example see Taylor et al. [75] that included a high level of detail (e.g. contact surface area, amount of DNA etc.)


# 4.0 Court cases that highlight the importance of evaluations given activity level propositions 

There are a number of high profile cases where the method or timing of deposition of biological traces was at issue. The following is a chronological list of cases (and their jurisdiction) that received some international and/or scientific attention. The list is not meant to be exhaustive:

- The Queen v Joyce [2002] NTSC 70 (Australia)
- 'Deventer murder case (1999)' [2004] AO3222 (The Netherlands)
- R v David Butler (2005) (UK)
- Private J. Kovko, Kovko Report (2006) (Australia)
- The Queen v Hillier [2007] HCA 13 (Australia)
- R v Reed and Reed, R v Garmson [2009] EWCA Crim 2698 (UK)
- Knox and R. Sollecito; Massei Report [2009] (Italy)
- 'Phantom of Heilbronn' (2009) (Germany)
- Farah Jama; Vincent Report (2010) (Australia)
- R v Weller [2010] EWCA Crim 1085 (UK)
- 'Putten murder case (1994)' [2011] BU3933 (The Netherlands)

- Adam Scott (2011) (UK)
- Commonwealth vs Dirk K. Greineder [2013] (USA)
- Lukis D. Anderson [2013] (USA)
- R v Drummond [2013] SASCFC 135 (Australia)
- R v Fitzgerald [2013] SASCFC 82, \& [2014] HCA 28 (Australia)
- R v Pfennig [2016] SASC 170/171 (Australia)

All of these cases have issues in common. These issues are generally allegations of legitimate modes of transfer or prevalence of DNA. We will describe and discuss these aspects below. They are illustrated using the circumstances of cases where the particular issue was a crucial element following from the prosecution and defence positions. The issues were generally not addressed through evaluation considering activities in these cases but highlight the importance of doing so. Although we grouped the cases according to a specific issue, all of the issues need to be considered in a case when assessing the findings under activity level propositions.

# 4.1 Indirect transfer 

Secondary transfer is the process whereby DNA of an individual is transferred by an intermediate vector. This vector could be either another person or an object. Through this intermediate vector that target DNA is transferred to an item of interest (i.e. target surface). There may be more than two steps involved in the overall transfer event.

- R v Fitzgerald

A DNA profile corresponding to the profile of the accused Fitzgerald was found on a Didgeridoo located at the house of victims of an assault. While there was no evidence that the didgeridoo was used in the attack, it was found close to the body of the deceased victim. The accused denied ever having been to the house. The accused alleged that his DNA may have come onto the didgeridoo through 'secondary transfer'. An individual he shook hands with visited the house of the victim. This individual was suggested to be the vector of DNA of the accused. Fitzgerald was convicted but subsequently released on appeal as secondary transfer could not be discounted. The case has been analysed in more detail by Szkuta et al. [74].

- R v Pfennig

A young girl went missing from her bedroom. Her pyjama top was found a few days after her disappearance. On the top a piece of fluff with DNA was found. The profile corresponded to that of the accused. He alleged that his DNA transferred to the top through his daughter, who went to the same school as the victim. The mode of transfer being suggested here was tertiary (Pfennig to his daughter, to the top of the victim, to the pyjamas of the victim). Pfennig was convicted of the offence, and later appealed on the grounds that the tertiary transfer scenario was not adequately discounted during the trial. During appeal the original conviction was upheld with the appeal Judge stating that the defence proposition was "so unlikely that I consider the trial judge was correct to exclude the appellant's hypothesis as a reasonable possibility"[76].

- Lukis D. Anderson

Lukis became a suspect in a Monte Sereno (California) murder case. He did have a solid alibi since he was hospitalized during the time of the incident. His DNA was probably transferred to the victim by paramedics that attended both Mr. Anderson and, afterward, the victim. The prosecution dropped the case when faced with this information and after five months in prison Anderson was released [77].

- R v David Butler

In this case a woman, who was murdered, had samples taken and analysed in the Forensic Laboratory. The DNA profile of the traces obtained strongly supported Butler as a DNA donor. Butler was a taxi driver and had a skin condition, which meant that he may shed more than usual amounts of skin. The possibility was raised by defence that his DNA had been shed to money, or a passenger and transferred to the victim. Butler spent eight months in jail on remand before being acquitted.

# 4.2 Contamination 

A conceptually useful distinction to be made is between the natural background noise on investigation scenes (i.e. not relevant to the activities under consideration), which can include individuals (e.g., victims, witnesses, etc.), and what has been added due to careless handling

(and has been added from a source unrelated to the crime) and avoidable practices ${ }^{5}$. The former is the normal and inevitable working condition under which forensic science must operate, while it is the latter that is often thought of as contamination, as defined by the ISFG commission in section 9 of [78], though some prefer the term 'pollution' (P. Margot, personal communication). However, due to its widespread use in this way, we will use the term 'contamination' to mean avoidable additions of DNA, during collection and subsequent processing (e.g., in the laboratory). Protective measures are specifically designed to help avoid contamination, and in certain circumstances it can be documented (e.g., medical help). To complement these measures that seek to minimize contamination from occurring, it is common for laboratories to also have processes in place that identify contamination when it has occurred, such as the use of screening DNA databases that comprise DNA profiles from staff members, police, doctors, or employees of consumable manufacturers.

Contamination can occur either from person to exhibit, or from exhibit to exhibit. This latter form of contamination is a specific type of secondary transfer. The presence of DNA of an individual on an item is the result of inadvertent transfer of DNA to an item (or DNA extract) through crime scene or laboratory processes or handling.

- Adam Scott case [45]

Adam Scott was suspected of a sexual offence due to his DNA profile corresponding to that of a trace in the case in the national DNA database. He was held for several months before it was found that the semen found was not his. The sample, in which semen was found (of the boy-friend and as a result of a non-criminal act), was contaminated (through a re-used disposable plastic container in the laboratory) with Adam Scott's DNA from a reference sample. During interpretation of the results it was incorrectly assumed that the DNA from Scott was from the semen.

- 'Phantom of Heilbronn' issue.

The DNA profile of an unknown female was found at a number of high profile cases in Germany, Austria and France. This included several murder cases, burglaries and robberies. Investigators initially suspect a serial killer was involved. In 2009 it became apparent that the DNA profile could be traced to an individual who worked packaging the cotton swabs at a factory. The Heilbronn issue received much publicity

[^0]
[^0]:    ${ }^{5}$ We realise that even the most stringent processes will never lead to a contamination rate of zero. We use the term 'avoidable' here to mean the events that, through process and protocol, laboratories seek to minimise, with the ultimate goal of avoiding their occurrence altogether.

since its discovery [79-81]. While this case never proceeded to the evaluation stage, it serves to highlights the potential importance that including the possibility for contamination in an evaluation can have. This becomes particularly important when the defence proposition is that the accused has had no contact (direct or indirect) with the examined item and yet the evaluation of DNA findings given sub-source level propositions strongly support the presence of the accused's DNA on the item. Activity level propositions can still be helpful in this investigative setting since they encourage scientists to think not only about intrinsic features (i.e., corresponding DNA profiles), but also about extrinsic features relating to the quality and quantity of traces, the position in which they were found and, related to this, aspects of transfer and persistence.

- The Farah Jama case

A woman, alleging she had been sexually assaulted, attended a medical facility, where a number of intimate swabs were taken. When processed in the forensic laboratory one of the swabs showed levels of sperm, which when profiled, corresponded to the reference of Farah Jama. Despite no other evidence Jama was convicted of the crime until it was ultimately found that a contamination had occurred at the medical facility. A sample containing Jama's sperm had been present in the examination room immediately prior to the intimate samples being taken from the victim. Details can be found in the Vincent report [82].

# 4.3 Prevalence of DNA of a known individual 

The issue of prevalence arises if it is argued that there is a legitimate presence of DNA of an individual on a person or on an item, or in the direct environment of an item of interest. The presence of DNA can occur either through specified previous contact or peripheral, undefined processes, leading to the DNA of an individual being present on an item.

- Deventer murder case [83]

An elderly lady was found murdered in her house in the city of Deventer in 1999. The financial consultant of the victim, Ernest Louwes, was convicted of the crime in 2003 and sentenced to 12 years. He appealed and was released. During examination in 2004, DNA of a male individual was recovered from multiple traces, including that from a bloodstain, that was identified on the lower collar of the double-collared

blouse of the victim. The DNA profile of the traces corresponded to that of Louwes. He claimed that the DNA from the traces on the blouse and from the bloodstain on the collar was the result of their meeting some time prior to the incident. These and other findings saw Louwes convicted again and he served an addition five years until his release in 2009.

- R v Weller

In this case Weller was charged with rape. The victim claimed that after drinking heavily, Weller put her to bed and then penetrated her with his fingers. Weller claimed that he assisted her to bed after she had become intoxicated (which included assisting her while she vomited) but did not assault her. The argument in court was then whether the DNA found on the fingers of Weller, that was found to correspond that of the victim, was more probable given digital penetration of the victim's vagina or given assisting the victim with going to bed. Weller was convicted in 2006 and sentenced to 3 years of imprisonment.

- Meredith Kercher case $[72,73]$

Amanda Knox was convicted and then later exonerated of the murder of Meredith Kercher (her roommate). There are a number of pieces of evidence that were used to build the prosecution case, many from the apartment where the murder occurred and where both Knox and Kercher cohabited. Under these circumstances, it was later argued that it is expected and unsurprising to find a level of Knox's DNA throughout the apartment where she lived. There was also evidence of Knox's DNA on a knife handle (claimed as the murder weapon by prosecution, but not defence), but again this was a knife that Knox would have had regular access to and so a level of her DNA would have been expected to be present.

# 4.4 Prevalence of DNA of an unknown individual (Background DNA) 

This topic relates to the presence of DNA of one or more unknown individuals (within the context of the case) on an item or person. The presence of DNA of unknowns is often presented in an argument to counterbalance the weight attached to the presence of DNA corresponding to the accused, particularly when the defence proposition claims an alternate person had carried out the alleged activity. This is often in conjunction with a legitimate reason for the presence of DNA of the accused.

# 4.5 Persistence issues 

A common case type where persistence issues may be important are sexual assaults. If both accused and complainant agree that sexual intercourse took place at some point, then the disagreement often is on the timing of the events. The complainant may state involuntary intercourse at a given time, while the accused alleges that the intercourse took place voluntarily some hours or days prior. Under such conditions, the persistence of traces on the body of the complainant, corresponding to the DNA profile of the defendant, may be informative towards two competing versions (i.e., the timing) of the event.

- Putten murder case [84]

A young woman was raped and murdered in the village of Putten in 1994. Semen was recovered from internal swabs and from the body's exterior. As a result of a correspondence found in the National DNA database, a suspect was identified in 2008. He claimed that he had a secret relationship with the victim, and that they had had sexual intercourse shortly before the offence. He was convicted of the crime in 2009. Persistence of seminal traces was not evaluated in the course of the investigation of this case. It could however have been informative for the court to know if the rape and murder occurred at the same time. The question of interest would have been whether the levels of semen found on the body were more probable given sexual intercourse at the time of the murder, or earlier in a secret rendezvous between the suspect and the victim.

### 4.6 Absence of DNA (sometimes called 'absence of evidence')

A common phrase that is often evoked is "the absence of evidence is not evidence of absence". There are two meanings often ascribed to 'absence of evidence', the first being that no testing has been carried out and so we truly are without any information related to examinations. In this situation the phrase given earlier may have some legitimacy. The second usage is when there is a lack of observed DNA from an individual on an item that has been examined. This is more correctly called an absence of DNA, rather than an absence of evidence. The finding that no DNA of a person of interest has been detected in fact does have evidential value. The absence of DNA will rely on probabilities of transfer, persistence and

recovery of DNA, given the proposed mechanisms put forward by prosecution and defence. Although the non-detection of DNA is not necessarily evidence of absence of an individual, it may provide support for the proposition under which an absence of DNA is expected.

- Drummond case

Drummond was accused of attempting to kidnap the victim off the side of the road. According to the victim's testimony a struggle occurred, but she was able to escape. During the investigation of the alleged crime the tops of both Drummond and the victim were examined and no DNA corresponding to the other party was found on either top. Despite this, Drummond was convicted of the crime. A misunderstanding about the significance of the absence of DNA (specifically regarding the probabilities of transfer and persistence) lead to an appeal and ultimate exoneration of Drummond. For an example of an evaluation of the findings considering the competing activities being put forward by prosecution and defence in this matter see [19].

# 5.0 Legal limitations and obstacles 

Acceptance of evidence may be subject to rules for admissibility of evidence. But since evaluation given activity level propositions is only more recently gaining recognition among practitioners as a frontier topic in forensic genetics, there is rather limited jurisprudence on its use in many jurisdictions. A noteworthy instance is the case R. v. Reed and Reed [2009; EWCA Crim 2698] in the UK. In this case, the court ruled that a scientist is entitled to evaluate DNA findings, in particular low quantities of DNA, with respect to possible mechanisms whereby DNA can be transferred. The competing activities of interest were innocently touching knives by the appellants versus each appellant passing their DNA to someone else who then transferred it to the items on which DNA was finally recovered (i.e., pieces of plastic associated with the victim). Champod [85] noted: "The court while recognizing that the scientific knowledge on transferability was incomplete, ruled that enough reliability had been demonstrated when the scientist is asked to consider cases where more than 200 picograms of DNA had been recovered. The court however stressed that 'care must be taken to guard against the dangers of that evaluation being tainted with the verisimilitude of scientific certainty.' The scientist is then authorized to comment on the probability of the forensic results given various transfer mechanisms as long as he/she makes it clear that we are dealing here with large uncertainty."

The verdict gives some leeway to forensic practitioners in the UK to provide weight of the evidence when the propositions are at activity level, even when data are not fully aligned to the case circumstances, or when data available are limited. A crucial caveat is that any limitations should be clearly stated in the report or given in evidence during trial.

The verdict was commented on by Jamieson [86], who warned against providing opinions solely based on experience over those based on experimental data. In the next section we discuss sources of data and their limitations in assigning probabilities for factors such as transfer and persistence of DNA in more detail.

# 6.0 Assigning probabilities for key factors when propositions of interest are at activity level 

When a case meets the organisational requirements for an assessment given activity level propositions (whether this be based on a system of case assessment or some other less formal agreement between the forensic institution and a stakeholder) then the scientist may turn to the specifics of the results of DNA analyses. This may involve the construction of a Bayesian network, or formulaic derivation, and will be followed by probability assignments for the various conditional probabilities important to the evaluation. There is a wealth of published information (for just some examples see [87-97], and van Oorschot's review in this same special issue), which continually grows, that can be accessed to help assign probabilities for transfer, persistence, prevalence and recovery of DNA.

In much of this paper we discuss the assignment of probabilities for discrete states of variables representing events of DNA transfer, persistence, prevalence and recovery. Even though such variables can be considered continuous, it is common to break to scope of values into discrete brackets of values. This need not be the case and working with continuous variables, including extensions to hierarchical modelling are feasible. Notwithstanding, there remains the question of what to do when there is a lack of data to inform probability elicitation and assignment. It is during the task of probability assignment that the scientist may identify a lack of data on which to base their choice of values for target probabilities, but there are a number of avenues available to the scientist. In order of preference, these are:

1) Perform experiments that mimic case circumstances to assign probabilities.

2) Use literature values from studies that represent similar properties to the case circumstances and outline the differences or limitations in the report.
3) Consider a range of reasonable values for the probability of interest and examine the sensitivity of the LR to it.
4) Assign a value based on the expert's experience or knowledge, preferably supported by structured analysis of similar case files, which can be justified by an argument, and be disclosed for review, (as required, for example, by the ENFSI guideline [36]), even though the invoked expert knowledge cannot be directly ascribed to a particular study, experiment or validation.
5) Do not carry out an evaluation, citing a lack of data leading to the inability to provide a robust opinion.

The first option in the above list is clearly the best choice. Not only can it be set up to directly mimic (as close as ethically possible) the circumstances of the case at hand, it will contribute to the pool of scientific knowledge. The limitation to this option is that many practicing forensic laboratories do not have the ability to carry out ad-hoc experiments, due to resource and time limitations (despite research being recognised as a critical component of the forensic field within service providers and education [98]).

The second and third options are the most commonly practised (personal communications of the authors with laboratories and in their own experience) and while given in the list above as separate alternatives, they are often used in conjunction.

The fourth option is practised, but can be criticised, notably regarding the justification and disclosure of bases of experience (for an example, see the case R v Dlugosz [99] and a criticism [100], of the testimony in the case). More generally, it is relevant to mention here that the notion of 'personal probability' should not be understood as an arbitrary or speculative assertion. Any probability assignment, informed by whatever amount of data (which may be none), is to be justified, based on an argument that the scientist is prepared to present and defend in full transparency [101]. An example of a probability assignment that utilises expert elicitation was provided by De Wolff et al [31] who surveyed 10 trace recovery experts on various aspects of saliva testing.

Because current recommendations encourage scientists to assess their findings with respect to advanced levels of propositions, ideally activity level propositions, not providing an evaluation (option 5 from above) appears as the least preferred option. Not helping with

evaluation at such advanced propositional levels would leave recipients of experts' testimony with an unsurmountable challenge: the assessments of results that require specialised knowledge (e.g., regarding background presence or transfer) that only forensic experts can provide. The preference to conduct an evaluation despite limitation in the available data is perhaps different to the general practise of evaluations of DNA profile data (given sub-source level propositions) that analysts would be used to, where even mild uncertainty regarding the result (e.g., the number of contributors to a DNA profile) will cause the scientist to decline the evaluation of the findings.

Contrary to widely held views, declining to carry out an evaluation given activity level propositions should ideally also be accompanied by a decline to provide an evaluation with sub-source level propositions (hence no evaluative report will be issued) ${ }^{6}$. The reason for this is that the evaluation in the light of source level propositions will bear the risk of being inappropriately carried over to a higher propositional level by recipients of expert information without properly acknowledging factors (such as transfer and persistence) that require expert knowledge. Declining to provide an evaluation given sub-source level propositions is possibly less adverse than doing so when activity level propositions are of interest, because a decline at sub-source level is a rejection based on the data itself, whereas a decline to evaluate given activity level propositions accepts the findings but rejects their consideration in the context of the case.

The above leads to the key point regarding the provision of evaluations given activity level propositions. Suppose that DNA results are obtained and only an evaluation given sub-source level propositions is given, in a case where activity is disputed. Then, the meaning of the evaluation given sub-source level propositions will have to be placed into the case context by the court, unaided by the scientist. To put it simply, the factfinder (whether it be judge or jury), at some point in the process will have to consider what the findings mean in a wider case context. Without assistance from experts the factfinder will not have adequate access to the current state of knowledge on DNA TPPR issues, and may therefore not be able to

[^0]
[^0]:    ${ }^{6}$ We concede that this is a challenging stance, and that in practise cases are often fragmented amongst different analysts and that in many instances an evaluation given (sub-) source level propositions will be carried out by default, thus leaving evaluations given higher level propositions to only a portion of these cases. In these instances, the duty of placing the findings given (sub-) source level propositions into a wider case context then falls to the scientists to do during their examination in court, or, to the factfinders of the Court themselves. But, again, this may be too delicate to be done on the stand. Our comments here are more directed towards the triaging stage of a case, i.e. if it is deemed that the case is not suitable for an evaluation given activity level propositions, then it should not procced to examination regardless any intention of providing an evaluation given (sub-) source level propositions.

properly weigh the findings in the context of the case. We hope that with this thought in mind the reader can see why declining to carry out an evaluation given activity level propositions sits at the lowest preference and does not justify a retreat to source level. All too often, it happens that the written report of expert conveys an evaluation given source level propositions but when questioned on the stand, experts accept to opine seemingly on possible activities or modes of transfer when questioned thereto. This is problematic because the scientist will opine ad-hoc on matters different from those on which he reports in the written report (i.e., evaluation given source level propositions). Evaluative aspects in the context of disputed activities are too intricate to handle without proper preparation.

We note that there are no, and there cannot be, objective criteria on when the conditions of a study are too far removed from case circumstances that they can no longer be used. At best, there may be an avenue for conventions, either within a laboratory or among expert groups in the field. In any case, the decision in a case lies with the forensic practitioner and needs careful analysis, thought and explanation (see for instance the paper by Cynthia Cale et al. [102], and the responses to this article [103] and [104]). A substantial number of published studies are based on older DNA typing systems (like SGMPlus). The combination of using newer generations of typing systems (e.g. Globalfiler, PowerPlex21 or PowerPlex Fusion 6C) will result in higher percentages of 'reportable' (e.g. suitable for comparison purposes) profiles and is likely to increase the detection of 'background' levels of DNA. Taking these values from older literature requires some adjustment based on knowledge of typing success rates or, ideally, based on comparative studies such as Steensma et al. [105].

In practise the above situation will likely lead to carrying out a sensitivity analysis. However, this does not relieve scientists from the burden of making an informed and justifiable choice on a value of the likelihood ratio to be reported, as no guidance on reporting the sensitivity of a LR currently exists. As mentioned above, any guidance on this is at best a convention only.

It is also foreseeable that if scientists provide their own personal probabilities (option 4 from the list above) then that will be based on a study, or multiple studies that partially fit with the case context. While options 2,3 and 4 from above are listed as discrete points, in practise they blend from one to the other. It may be that the expert's justified experience-based probability assignment takes the probability from the 'similar study' completely and so uses them in the current evaluation (again, with the scientist highlighting the limitations of their evaluation in their report). Alternatively, it may be that the 'similar study' forms the basis of

a plausible range of values that are used in a sensitivity analysis. In summary, note that despite the fact that (i) there is no sensible definition that can be given that describes at what point a study diverges from case circumstances enough that doubt exists as to the applicability of the data, and (ii) there is no rule that describes to what extent a scientist should use the results of a study to update their own belief about key factors affecting an evaluation, or when to carry out a sensitivity analysis, there is no one in a trial other than the scientist who has the required specialised knowledge to logically place findings in a context of disputed activities. It is important, thus, for scientists to ensure transparency in the report and in verbal statements to the court with respect to assumptions that are made and limitations to the data sources and their application [36].

# 7.0 The role of Case Assessment and Interpretation (CAI) 

It is common that forensic institutions have some mechanism that limits the number and type of exhibits accepted in a case. Often the number accepted is tied to the level of available resources and the type of exhibit is usually based on the probability of obtaining an informative DNA profile and the relevance of the exhibit to the case. However, commercialisation of forensic services is accompanied with its own specifics, in particular the amounts and types of exhibits accepted for examination, placing less emphasis on the potential of added value by forensic analyses. For a discussion of these aspects in the context of England and Wales see Jackson [106].

In 1998 the Forensic Science Service formalised an exhibit triaging process, based on the general principles and methodology (see also section 1.1) employed during evaluations [63]. They named the process Case Assessment and Interpretation (CAI), which has since been discussed and explained further in the expert evidence guide written by Jackson et al [38], to determine which exhibits and which cases should be accepted for processing and subsequent evaluation. The basic idea of CAI is that if the activity level propositions are known at the time of case receipt then the choice of which exhibits to accept (if any) can be guided by probabilistic criteria. This is achieved by evaluating the probability of obtaining different strengths of evidence in favour of the prosecution or defence propositions if either proposition is true. The advantage of carrying out such an evaluation at the beginning of the case is that evaluation is carried out in a manner that can then be used later on when results are obtained (although, as noted by Taylor et al [61], using BNs, the examination of exhibits

may bring up unexpected findings that require fine tuning of the evaluation after examination). The process thus emphasises the thinking about the value of findings before examinations are carried out, thus avoiding the evaluation being influenced by the results actually obtained (i.e., avoiding being 'findings-led'). The results of a CAI would be similar to that shown in Table 1, which is a recreation of table 8 from [38]. The conditional genotype probability used in the construction of this table is 1 in 1 billion $^{7}$. The scenario that could apply to Table 1 is a case of alleged rape where the propositions being considered are: The suspect $(\mathrm{S})$ had sexual intercourse with the victim versus someone other than the suspect had sexual intercourse with the victim in a case where it is known that the swab being assessed contains semen.

The general format that can be followed to carry out a CAI is (according to [63]):

1. Establish the prosecution and defence propositions
2. Consider what findings are expected when the propositions are, in turn, considered to be true
3. Evaluate the expected LR when the propositions are, in turn, considered to be true

Table 1 can then be used to conduct a pre-assessment for the swab in the case. Thus, under the assumption that the suspect did have sexual intercourse with the victim, the most probable outcome $(97 \%)$ is that a single source profile corresponding to the profile of the suspect will be obtained, and under this version of the case a LR would be assigned of approximately 1 billion in favour of the prosecution proposition compared to the defence proposition.

Alternatively, the most probable outcome ( $\sim 99 \%$ ) if the suspect has not had sexual intercourse with the victim is that a single source profile will be obtained that does not correspond to the profile of the suspect. In this instance a LR will be obtained of 100 that favours the defence proposition over the prosecution proposition. The probability assignment of 0.01 in Table 1 in the column relating to the probability of the findings given the prosecution proposition is not specified in the original text other than their statement of: "Each of these outcomes, however, is thought to have only a $1 \%$ probability of occurrence on the assumed facts". Jackson et al [38] provide an additional example earlier in their report that involves the questioned wearing of a balaclava. McKenna [28] also gives an example of a CAI where the presence of or absence of blood stains on the accused's clothes is evaluated,

[^0]
[^0]:    ${ }^{7}$ Throughout this paper, we use the definition of 1 billion as $1 \times 10^{9}$

and the disputed activity is one of kicking and punching a victim, compared to being nearby when it occurred but not participating.

$\operatorname{Pr}[\mathrm{E} \mid \mathrm{Hp}, \mathrm{I}] / \operatorname{Pr}[\mathrm{E} \mid \mathrm{Hd}, \mathrm{I}]$  |

Table 1: Table 4.6 from [38] showing the results of a pre-assessments for DNA profiling outcomes E on semen found on internal vaginal swabs. The propositions of interest are 'The suspect (S) had sexual intercourse with the victim' versus 'Someone other than the suspect had sexual intercourse with the victim'.

If a table is created similar to that shown in Table 1 and an exhibit has, for example, a low probability of yielding an informative LR (i.e. where an informative LR is one that is substantially different from one) when either proposition is considered true, then this forms a strong basis to reject its submission on grounds that it is not expected to be probative to the propositions being considered. For less obvious triaging choices, a discussion then occurs between scientist and client (e.g. Police) that includes expectations and costs to determine what work is carried out.

CAI, and the work of [107] brings up the concept of the scientist working in two different modes, investigator and evaluator. In an investigative phase, the details of the case may not yet be clear (there may not yet be a nominated person of interest) but, the scientist is potentially considering which evidential items will be most probative to reveal information about the case. The scientist may be considering multiple versions of the case that may account for the evidence and how these would manifest in the results of examinations that could potentially be performed. This investigative phase need not only be considered for activity level propositions. Buckleton et al [108] describe how the investigative and evaluate phases of an investigation may affect the sub-source level propositions when evaluating DNA profiles. It may be that multiple evaluations of the same data under different pairs of propositions are considered at this stage.

Conversely, at the evaluative stage the case is typically destined for court and the propositions are known (or can be reasonably set by the scientist, based on the information available on the case). In this phase the scientist considers the entirety of the relevant findings in light of the propositions, and then may investigate the robustness (e.g. through sensitivity analysis) of their evaluation. In some cases, the same BN used in the CAI, or in the investigate phase of the case, can also be used in the evaluative phase.

# 8.0 Case information management 

The nature and amount of contextual information that is needed for evaluation given activity level propositions changes and increases substantially from the information needed for evaluation given (sub-)source level propositions. To assign probabilities for factors such as DNA transfer, persistence and prevalence, detailed information is needed on relevant, though

not necessarily all, case circumstances. Much has been written on the cognitive processes that may lead to bias [109-111], the sources of biasing information [112] and potential avenues to minimize the risks of cognitive bias in (amongst others, DNA) evidence interpretation in forensic science [113-116]. These papers deal with the risk when the evaluation is based on sub-source level propositions, but they are equally (or possibly more) relevant for evaluation with propositions at other propositional levels.

Crucial to managing case information in such a way that risks of cognitive bias are minimized is the notion of 'task-relevant' information, defined as the information needed to assess the value of the findings only. This suggests the expert should have a procedure in place for case information management (for example [115]). Task-irrelevant information is not needed for the task at hand but may contain information that could lead to cognitive bias. Jeanguenata et al. [112], (in their Table 2) list a number of potential sources of case information that are not task-relevant to the evaluation given sub-source level propositions. An example in Table 2 are eyewitness statements collected by investigators at the scene of crime, which could contain details on the scene as well as information on who was present and what has occurred. This information is potentially task-irrelevant for forensic practitioners who evaluate findings given sub-source level propositions. However, this kind of information may be crucial and hence task-relevant when evaluating findings given activity level propositions.

Questions regarding timing or the method of transfer or persistence of traces usually arise after results of biological trace examinations are known. The findings may themselves be another source of potential bias for practitioners who evaluate findings given activity level propositions. The practitioner will generally assign probabilities for factors such as transfer and persistence of DNA given the case circumstances at hand, and his interpretation of available data. However, if a practitioner is aware that DNA corresponding to a suspect is found on the clothing of a victim, they may (unconsciously) assign a higher probability for the event of transfer than if no corresponding DNA is found, or if they have no knowledge of the findings. This highlights the need for conducting a full case pre-assessment in which probabilities for outcomes are assigned prior to conducting examinations. This helps avoid subsequent statements being findings-led, i.e., statements of the kind 'this finding corresponds (well) to my expectations'.

Another consideration in this context is the idea of assigning the task of evaluation given activity level propositions to an individual other than the one who assessed the findings given source level propositions in the first place. It may be decided on a case-by-case basis whether there are mitigating reasons why one should deviate from this default position.

When a case file may contain information that is task-irrelevant and has the potential to induce cognitive bias, evaluating the evidence given activity level propositions may benefit from case information management. Thompson et al [117] and Dror et al. [118] consider the option of introducing a case manager to 'filter' task-relevant from task-irrelevant information. Such a case manager would need substantial training in case assessment, as well as interpretation of DNA evidence, to be able to identify task-relevant information for evaluation of findings given activity level propositions [119].

# 9.0 Reporting evaluations of findings given activity level propositions 

There have been a number of publications that provide guidance on structure and elements that would make up a report on the evaluation of findings given activity level propositions. We provide a few examples below and summarise their main elements.

Evett et al. [1] published a seminal paper on evaluating findings at various levels within the hierarchy of propositions. As part of this publication the authors provide the headers for reports produced by the (now non-existent) Forensic Science Service.

- Framework of circumstances
- Purpose
- Technical issues
- Examination and results
- Interpretation
- Conclusion
- Appendix

The guideline published by the Association of Forensic Service Providers [37] gives guidance on report structure in their section 4.14 , where they state that the report will include:

- Background information used in the assessment / interpretation
- The propositions addressed
- Relevant items received
- Items examined
- Significant findings
- Conclusions

These guidelines are not specific to forensic genetics, but generally applicable to any type of forensic finding (and any forensic discipline undertaking evaluation given activity level propositions). Note, again that reports should not contain headers such as 'The propositions addressed' because they are ambiguous and misleading formulations: scientists do not address the propositions, but findings given propositions. The fundamental importance of this distinction cannot be overstated.

The ENFSI Guidelines [36] provides guidance on reporting of results to the court and also provide a number of example reports for different disciplines. A DNA case is given where the competing activity level propositions are:

- The accused handled a bag of heroin.
- An unknown person handled the bag of heroin and the accused had nothing to do with.

The case circumstances provided the information that the accused was arrested by the officer who had collected the bag. They provide their report in sections of background information, the issue, items received, findings, the interpretation and conclusion. Note further that the ENFSI Guideline also contains an audit template, intended to offer a mechanism for auditors to assess whether or not evaluative reports meet the requirements of the guideline. The template consists of a table with key-points that help establish an overview of the compliance of a given report with the guideline.

The paper by Taylor et al. [61] on the steps for constructing a BN with activity level propositions provides, as supplementary material ${ }^{8}$, an example of a report. It features the following competing propositions:

- The defendant bit the complainant on the vagina, outside her underwear.
- The defendant did not bite the complainant, he had no direct contact with her underwear.

The case circumstances were such that the defendant and complainant cohabitated at the time of the alleged offence and were siblings.

All examples of reporting we mention in this section, provide a similar framework for report structure and content. All require a description of the case circumstances (as understood by the scientist and used in their evaluation, as well as their assumptions), the items received in the case, the process of the evaluation (including any limitations) and the conclusion of the scientist.

Some notes have been published about including Bayesian networks in reports addressing the findings given activity level propositions. Sjerps and Berger [120] suggest Bayesian networks are restricted to the case file and provided only on request. They feel that there is a trade-off between transparency of including a Bayesian network and the clarity of the argument, particularly with highly complex Bayesian networks. Some scientists, however, use Bayesian networks in their report when there is a need for substantiating a particular argument (for a discussion and example see [61]). There has been some suggestion, although unsubstantiated in practice, that using Bayesian networks may ease explanations of how the evaluation was carried out to lay people [121].

# 10.0 Arguments against evaluation and reporting of results given activity level propositions 

Scientists working in forensic biology laboratories are often reluctant to engage in evaluation and reporting of findings given activity level propositions due to a number of perceived difficulties and uncertainties. It is true that the specification of propositions, the construction

[^0]
[^0]:    ${ }^{8}$ Available from web address www.fsigenetics.com/article/S1872-493(17)30282-X/fulltext

of an evaluation framework, and the assignment of probabilities is less well defined and studied as many forensic biology practitioners would be used to, when compared to subsource level reporting on STR DNA profiling findings. The authors in [8] collected a number of the most commonly cited 'difficulties' or 'reasons' given for not carrying out evaluations given activity level propositions, and responded to each. These fall into two broad groups; issues with the definition of propositions and issues with reporting results. The manuscript outlines the reasons for, and conceptual foundations of, evaluating findings given activity level propositions despite a lack of information (true of almost all forensic cases that these evaluations would be applied to) such as not knowing what the exact activities are either because they are not given, or are very vague and having to assign probabilities using literature whose experimental design that does not exactly align with case circumstances. The authors also explain why reporting the results of evaluations given activities should be done even when the issues of transfer and persistence are unknown or misunderstood by the judiciary, and further that it is the role of the scientist to inform the court on the meaning of the findings within the circumstances of the case, and that this does not infringe on the duty of the jury.

Part of the reluctance in the community of forensic geneticists to consider the evaluation and reporting of their findings given activity level propositions may stem from tradition. Forensic genetics, being a relatively young forensic discipline, has developed from academia. Geneticists have developed the field and genetic analysis techniques for applications in forensic science. With DNA analysis traditionally being a strongly lab-based operation, there has always been some distance between the scientist and other practitioners in the legal process who interpret the results in the context of the case. This contrasts with many forensic science disciplines that have developed within investigative organisations (e.g., police) during their history. For instance, gunshot residue (GSR), fibres or fingerprint examination, have traditionally been forensic disciplines that were developed in the context of police investigations. The interpretation of their analysis results in the context of the case has always been an integral part of the discipline. In particular, forensic areas such glass examination [122] and textile fibres [123, 124] have pioneered the development of evaluative approaches using activity level propositions, though even in these fields further theoretical developments remained limited and only few forensic practitioners actually report findings in view of competing posited activities today.

In our conversations with Sheila Willis on this topic, she made the point:
"As we have often discussed, when transfer and persistence issues are relevant, activity propositions are vital to ensure that source is not misleading. This view is not widely accepted, particularly in DNA, so it is useful to try to explore why Forensic science has developed as fragmented disciplines rather than a mature coherent science in itself resulting in the characteristics of particular materials and technology advances taking precedence over the principles of interpretation. Thus, not only do practitioners not learn from the past, they do not learn from related fields. This also leads to a lack of recognition of the legitimacy of forensic science. Scientists from outside forensic science are effective in promoting other models usually based around analytical chemistry rather than accepting the circumstantial nature of forensic science. In this environment, and where there is little enough leadership, DNA practitioners are slow to embrace the type of data needed to help the judiciary address activity propositions where the level of uncertainty is much higher than in analytical chemistry."

# 11.0 Training, competency testing and quality assurance 

Reporting forensic findings given activity level propositions requires an additional set of skills and training compared to reporting given sub-source and source level propositions [10, 125].

In those laboratories that offer evaluations of results when the propositions of interest refer to competing versions about activities (personal experience), statements are in practise usually given by more senior forensic scientists with an extensive knowledge of, and experience with, reporting given lower propositional levels, i.e. (sub-)source level. With increasing demand for assessments given activity level propositions, and following from that, an increasing number of scientists reporting in this area, solid knowledge and experience in reporting given (sub-)source level propositions may be considered a requirement for providing evaluations given activity level propositions.

There is general acceptance amongst the forensic community on the use of probabilistic measures of probative value, taking the form of a likelihood ratio, independently of the propositional level of interest. Training in the understanding and application of elements of

probability theory should thus be mandatory, as in any other scientific discipline. Where evaluations require the incorporation of dependent variables and associated probabilities, the use of graphical approaches (e.g., Bayesian networks) for clarifying the structure and content of reasoning processes is often emphasized (even recommended by groups such as the ISFG [62]). This, however, requires adequate training in the case tailored construction and use of such models (and the software employed to build and manipulate them). This should be preceded by a thorough understanding of more fundamental principles, such as the distinct role of events (variables) denoted transfer (T) as compared to propositions regarding posited activities (H), as noted, e.g., in the formal development mentioned earlier in Section 1.1.5 ' Sub-sub-source Level'.

A further important preliminary is that experts should be able to clearly explain their reasoning and the limitations of their opinion in a courtroom setting, which requires training on the logical principles of evidence evaluation [126] and the role of the expert in the legal process.

# 12.0 Errors, measurement uncertainty and sensitivity analyses 

These three notions have caused, and continue to cause, much discussion amongst the forensic science and legal community. The terms are sometimes used almost interchangeably in discussions, in particular error (and rates thereof) and measurement uncertainty, although each has a distinct meaning.

In a general sense, the notion of error is understood as an event, or phenomenon, that leads to an undesirable, but avoidable outcome (such as a laboratory polluting a DNA extract, a sample mix-up, an incorrectly reported result, etc). These sorts of events, though each referring to unique case setting, are subsumed under the notion of 'errors' and are often catalogued by laboratories' quality assurance systems, but rarely published. A notable exception is the work published by Kloosterman et al [127] where errors were categorised both by type and impact and their rates given.

Numerical summaries of the number of errors in a sequence of observations, in different dimensions (e.g., errors committed by a given examiner, a given department or laboratory, a field or profession etc.), are commonly referred to as error rates. These are descriptive

summaries of a phenomenon over a sequence of individual observations, but as such are little informative for evaluation in an actual case at hand. Forensic literature and discussions among practitioners sometimes raise the issue of 'incorporating an error rate' in assessments of probative value. Yet other discussions focus on whether an 'error rate' should be presented separately, alongside an expression of probative value, raising issues on how the recipient of expert information ought to logically combine these two distinct items of information.

Claims of 'incorporating an error rate' are misguided in the sense that, as mentioned above, an error rate is only a general figure that is not tailored to the case at hand. It may be used in arguments by parties to underline other points (e.g., reliability or trustworthiness of a given practice, domain, or examiner etc.; issues in admissibility, etc.) though not directly in arguments about probative value of particular findings in a case of interest. What is needed in a given case at hand is an assignment of the probability of occurrence of an event of error, of a specified type, in the case at hand. General error rates may be one source of information to help assign such probabilities, but by no means they can, by default, be equated to the probability of error required for a given case at hand.

There have been several publications that describe the incorporation of error probabilities into DNA evidence evaluation when source level propositions are posited [128, 129], and also in cases where activity level propositions are of interest [34]. An example of how different types of error could be taken into account at differing junctures within a BN for evaluation given source level propositions (specifically in relation to the source of sperm observed on a microscope slide prepared form an intimate swab from an alleged rape victim) was given by Taylor [130].

Measurement uncertainty within forensic biology refers to the observation that repeated measurements of a target quantity distribute over some range as a result of, for example, instrument noise. Such observed distributions of output values are well documented within DNA profile evaluation, when the propositions are at sub-source level [131-134]. It is common when validating a new methodology (such as the introduction of a new piece of laboratory hardware, or a body fluid test) to incorporate an assessment of such measurement uncertainty, providing an assessment of the performance of the hardware/system/method. The assessment of measurement uncertainty is a standard requirement for many accrediting

bodies, such as the National Association of Testing Authorities (NATA), and is also mentioned, for example, in Forensic Science ISO/IEC 17025 Application Documents.

Evaluating findings (considering any level of proposition), in its most fundamental sense, describes a way of thinking about findings and involves, in the context of activity level propositions, the consideration of the various pathways of transfer and persistence of biological material that would be required under two competing propositions in order to arrive at some observed findings. Thinking about results given such competing versions of the event of interest may take a qualitative form and, thus, is not based on any numerical expression of probative value, and indeed this is how many reports have been produced within Europe for some time (anecdotal personal communications with various Forensic practitioners). However, it is becoming more expected that a numerical evaluation is part of the evaluation given activity level propositions as available data (published literature, inhouse experimentation or experience) and technology improves, and understating of evaluation techniques (such as the use of BN) increases.

Since evaluation given activity level propositions involves, in essence, the careful thinking about the definition of propositions of interest, and phenomena such as transfer and persistence, notions such as inherent instrument noise, sampling variation and measurement uncertainty do not directly pertain to this evaluative reasoning process as such, but only to the experimental measurement process related to the examined item. This does not mean, however, that there is only one possible output for an evaluative process, let alone that there exists a 'true' probative value for a given result when evaluating findings given activity level propositions. Indeed, the studies used to obtain data about phenomena such as transfer and persistence, and expert knowledge about these phenomena, will differ on a case by case basis, and from one expert to another (i.e., in the case of experience-based assessments), as will the architecture of supporting concepts, such as BNs. Thus, in cases where reports on the probative value for the same findings vary across different experts, not only in orders of magnitude but also in terms of the proposition being supported, compared to a given alternative, it is crucial to enquire about the knowledge base on which experts relied, and how they used it to inform probability assignments.

There has been some discussion recently on how to cope with different value of evidence assignments resulting from different assumptions, and whether and how to report about

investigations of this issue (see, e.g., the special issue in the journal Science \& Justice 2016, volume 56, issue 5, [135-142], preceded by a discussion in Law, Probability \& Risk [143, 144]). Again, note that such discussion was focusing on evaluation given source level propositions only.

A practice that is widely accepted is a technique called a sensitivity analysis [145]. This type of analysis seeks to determine how sensitive the LR (and hence the expert's opinion) is, depending on the actual value taken by one or more factors considered in an evaluative model. The factors of interest typically refer to events of transfer and persistence, and their probabilistic assessment relies on data or documented experience. Thus, if there is a paucity of data used to assign a probability to which the LR is particularly sensitive, then this may indicate that the opinion of the scientists requires careful investigation of its robustness. This may lead to situations in which the scientist may decide not to report a result, because of concerns about robustness.

There are different ways in which sensitivity analyses can be carried out in forensic genetic evidence evaluations. When the number of factors to consider is low (or the sensitivity of the LR to some of them together is not required) then one method of sensitivity analysis involves holding all but one of the probabilities within the system constant and varying the remaining one over a plausible range of values. This is known as a one-way sensitivity analysis. Typically, then, the value of the LR can be graphed across the range of probabilities considered, providing thus an assessment of the sensitivity of the LR for the scope of target probabilities investigated. For evaluations given sub-source level propositions, these types of sensitivity analysis have been carried out for semi-continuous DNA interpretation systems that use probabilities for dropout and drop-in [64, 65]. Examples of this type of sensitivity analysis for evaluations given source and activity level propositions were given by Taylor [19, 130], Evett [6] and Szkuta et al [74].

The second situation under which sensitivity analyses may be carried out is when the sensitivity of the LR to two or more underlying probability assignments (and hence related data) is desired. This may help assess the robustness of an opinion that is to be provided, or it may be used to determine what experimental data would provide the highest prospect of improvement to the robustness of the opinion (and hence where resources would best be spent). In this type of sensitivity analysis scheme, the data used to assign probabilities can be

resampled from assumed underlying distributions. The distribution ${ }^{9}$ of individual LRs obtained, given these resampled probabilities can then be determined for all, or a subset of the variables of interest. This type of sensitivity analysis is more complex to carry out and will typically require some custom written computer code. Taylor et al [142] demonstrated such a sensitivity analysis for a previously reported BN [30] that was used to carry out a source level evaluation. De Zoete et al [32] shows another example of custom code being used to carry out sensitivity analyses.

# 13.0 CONCLUSION: 

Evaluating forensic genetic findings, as well as presumptive cell type examinations, considering activity level propositions is becoming more accepted and more common place within the forensic biology field. This is due to a combination of effects, but most prominently:

- an increase in the sensitivity of DNA profiling technology, shifting the focus of questioning in court from the source of DNA to the mechanism by which it came to be on an item;
- an increase of demands in forensic and legal fields (due to publications and prominent court cases) of scrutiny regarding the practice;
- the availability of software to carry out complex evaluations, and
- an increasing body of knowledge on factors underpinning probabilities of transfer, persistence, prevalence and recovery of DNA

Since the 1990s there have been publications that provide guidance on proposition setting, method of evaluation, reporting structure, evaluative philosophies and the role of the scientist. We have provided an overview of the essential works in this area.

We are aware of several laboratories worldwide that report on the evaluation of findings given activity level propositions. As these reports become more commonplace we believe there will be greater call for them from the legal community and this will naturally drive other laboratories to start evaluating evidence in this manner. Due to the relatively small number of reports produced there is little information on how the courts receive these types

[^0]
[^0]:    ${ }^{9}$ Note that such a distribution is not an interval around a supposedly 'true' likelihood ratio. Each likelihood ratio of the distribution obtained in a sensitivity analysis is a single number resulting from a particular assignment of probabilities for the variables on which the sensitivity analysis focuses.

of reports, their impact in the criminal justice system, and what challenges lie ahead, for the scientists, the legal community and law makers.

The examples of activity level evaluations given in literature (e.g., $[19,28,36,38,61,130]$ ) were not, as far as we are aware, ever presented in court. The process of providing evaluations given activity propositions in Forensic Science SA is relatively new (being officially provided in 2017) and the cases which have been targeted have not yet been presented in court. The anecdotal feedback from the prosecution and defence lawyers is that the reports are immensely useful. At the NFI evaluations of human forensic genetic findings given activity level propositions are being provided upon request by a court or an investigative judge. The following summary excludes reports regarding blood stain patterns, evaluated given activity level propositions.

An average number of 25 of such reports have been provided per year since 2013 (which is a very small fraction of all reports on human biological traces and DNA, which are primarily evaluated given sub-source or source level propositions). The reports cover all types of cases (sexual assault, burglary, murder etc.). Regardless of the type of case, the vast majority deal with 'trace DNA', e.g. collected material without a known cellular source. Evaluation in situations of of 'absence of evidence' (e.g., when the profile of the recovered DNA does not correspond to the profile of a person of interest) was requested in a handful of cases.

In roughly a third of these cases the expert is requested to provide evidence in court based on these reports. Regardless of court appearance of the expert, the majority of the reports are mentioned in published verdicts. This ranges from a mere citation of the report to near complete copy of the line of reasoning and supporting data. Although the impact is not known, this implicitly means that most of the reports on evaluating findings given activity level propositions have, to some, extent contributed to the fact finding of the court. This is supported by anecdotal feedback from judges, prosecutors and defence lawyers.

It is clear though, from the overwhelming commentary of forensic practitioners on the topic of evaluation given activity level propositions, that the scientist is best placed to consider the meaning of the findings in a case context that requires consideration of factors such as transfer and persistence of DNA. There are numerous commentators that emphasise the crucial need to assess forensic biology evidence given activity level propositions. This is to best assist the court in their deliberation on the ultimate issue and avoid potential

misunderstandings of the meaning of the value of evidence. Providing the court evaluations given activity level propositions, avoids the unwarranted carrying over of conclusions given source level propositions to conclusions regarding activity level propositions, when the latter requires specialised knowledge that the judiciary cannot be expected to possess. Although this is a crucial precept, it may be difficult to keep track of it because a competent defence review of forensic DNA testimony may not be readily available. As noted by Murphy [146], "Even well-intentioned defence lawyers may find it preferable to work around DNA evidence rather than to expend the resources necessary to challenge it, given that DNA matches are often viewed by lay people as conclusive proof.".

We finish with a thought from Roberts et al [39] who note, when speaking on evidence evaluation:
"[T]he use of Bayes nets to contextualise the meaning of analytical results and make assessments of their probative value as (potential) evidence in criminal trials is poised to increase and become more institutionalised over time (...) in forensic science practice around the world."

We feel this sentiment extends to the evaluation of forensic findings given activity level propositions.

# ACKNOWLEDGEMENTS: 

Points of view in this document are those of the authors and do not necessarily represent the official position or policies of their organisations. We thank Manfred Kayser for the invitation to contribute this review to Forensic Science International Genetics. We also thank Sheila Willis for her helpful discussions. Alex Biedermann gratefully acknowledges the support of the Swiss National Science Foundation through grant No. BSSGI0_155809, and the University of Adelaide Law School (Litigation Law Unit) through an 'Aim for the Stars' grant.

# REFERENCES: 

[1] I.W. Evett, G. Jackson, J.A. Lambert, S. McCrossan, The impact of the principles of evidence interpretation on the structure and content of statements, Science \& Justice 40(4) (2000) 233-239.
[2] National Commision on Forensic Science: views of the commission ensuring that forensic analysis is based upon task-relevant information, National Institute of Standards and Technology, https://www.justice.gov/archives/ncfs/file/818196/download, 2015.
[3] I. Evett, Evaluation and professionalism, Science \& Justice 49 (2009) 159-160.
[4] I. Evett, B. Weir, Interpreting DNA Evidence: Statistical Genetics for Forensic Scientists, Sinauer Associates, Sunderland, MA, 1998.
[5] R. Cook, I.W. Evett, G. Jackson, P.J. Jones, J.A. Lambert, A hierarchy of propositions: Deciding which level to address in casework, Science \& Justice 38(4) (1998) 231-240.
[6] I.W. Evett, P.D. Gill, G. Jackson, J. Whitaker, C. Champod, Interpreting small quantities of DNA: the hierarchy of propositions and the use of Bayesian networks, Journal of Forensic Sciences 47(3) (2002) 520-530.
[7] I.W. Evett, G. Jackson, J.A. Lambert, More on the hierarchy of propositions: exploring the distinction between explanations and propositions, Science \& Justice 40(1) (2000) 3-10.
[8] A. Biedermann, C. Champod, G. Jackson, P. Gill, D. Taylor, J. Butler, N. Morling, T.H. Champod, J. Vuille, F. Taroni, Evaluation of forensic DNA traces when propositions of interest relate to activities: analysis and discussion of recurrent concerns, Frontiers in Genetics 7 (2016) 215-220.
[9] T. Hicks, A. Biedermann, J.A.d. Koeijer, F. Taroni, C. Champod, I.W. Evett, The importance of distinguishing information from evidence/observations when formulating propositions, Science \& Justice 55 (2015) 520-525.
[10] R. van-Oorschot, B. Szkuta, K.N. Ballantyne, M. Goray, Need for dedicated training, competency assessment, authorisations and ongoing proficiency testing for those addressing DNA transfer issues, Forensic Science International: Genetics Supplement Series 66 (2017) e32-e34.
[11] I.W. Evett, Establishing the Evidential Value of a Small Quantity of Material Found at a Crime Scene, Journal of the Forensic Science Society 33(2) (1993) 83-86.
[12] M.W. Perlin, M.M. Legler, C.E. Spencer, J.L. Smith, W.P. Allan, J.L. Belrose, B.W. Duceman, Validating TrueAllele® DNA mixture interpretation, Journal of Forensic Sciences 56 (2011) 1430-1447.
[13] D. Taylor, J.-A. Bright, J. Buckleton, The interpretation of single source and mixed DNA profiles, Forensic Science International: Genetics 7(5) (2013) 516-528.
[14] R.G. Cowell, S.L. Lauritzen, J. Mortera, Probabilistic expert systems for handling artifacts in complex DNA mixtures, Forensic Science International: Genetics 5(3) (2011) 202-209.

[15] C. Brenner, DNA.VIEW. [http://dna-view.com/professionalism.htm](http://dna-view.com/professionalism.htm), (accessed 20 October 2014.).
[16] R. Puch-Solis, L. Rodgers, A. Mazumder, S. Pope, I. Evett, J. Curran, D. Balding, Evaluating forensic DNA profiles using peak heights, allowing for multiple donors, allelic dropout and stutters, Forensic Science International: Genetics 7(5) (2013) 555-563.
[17] Ø. Bleka, EuroForMix: An open source software based on a continuous model to evaluate STR DNA profiles from a mixture of contributors with artefacts, Forensic Science International: Genetics 21 (2016) 35-44.
[18] D.A. Taylor, J.-A. Bright, J.S. Buckleton, The 'factor of two' issue in mixed DNA profiles, Journal of Theoretical Biology 363 (2014) 300-306.
[19] D. Taylor, The evaluation of exclusionary DNA results: a discussion of issues in R v. Drummond, Law, Probability and Risk 15(1) (2016) 175-197.
[20] Y. Mcdermott, C. Aitken, Analysis of evidence in international criminal trials using Bayesian Belief Networks, Law, Probability and Risk 16 (2017) 111-129.
[21] J.d. Zoete, M. Sjerps, R. Meester, Evaluating evidence in linked crimes with multiple offenders, Forensic Science International: Genetics (2017).
[22] S. Gittelson, A. Biedermann, S. Bozza, F. Taroni, Bayesian networks and the value of the evidence for the forensic two-trace transfer problem., Journal of Forensic Sciences 57(5) (2012) 1199-1216.
[23] R. Wieten, J.D. Zoete, B. Blankers, B. Kokshoorn, The interpretation of traces found on adhesive tapes, Law, Probability and Risk 14(4) (2015) 305-322.
[24] M. Breathnach, E. Moore, Oral intercourse or secondary transfer? A Bayesian approach of salivary amylase and foreign DNA findings, Forensic Science International 229 (2013) 5259 .
[25] M. Breathnach, E. Moore, Background levels of salivary- $\alpha$-amylase plus foreign DNA in cases of oral intercourse: a female perspective, Journal of Forensic Sciences 60(6) (2015) $1563-1570$.
[26] M. Breathnach, L. Williams, L. McKenna, E. Moore, Probability of detection of DNA deposited by habitual wearer and/or the second individual who touched the garment, Forensic Science International: Genetics 20 (2016) 53-60.
[27] J.E. Allard, The collection of data from findings in cases of sexual assault and the significance of spermatozoa on vaginal, anal and oral swabs, Science \& Justice 37 (1997) 99108 .
[28] L. McKenna, Understanding DNA results within the case context: importance of the alternative proposition, Frontiers in Genetics 4(242) (2013) 1-4.
[29] B. Kokshoorn, B.J. Blankers, J. de Zoete, C.E.H. Berger, Activity level DNA evidence evaluation: On propositions addressing the actor or the activity, Forensic Science International 278 (2017) 115-124.

[30] D. Taylor, D. Abarno, C. Champod, T. Hicks, Evaluating forensic biology results given source level propositions, Forensic Science International: Genetics 21 (2016) 54-67.
[31] T.R.D. Wolff, A.J. Kal, C.E.H. Berger, B. Kokshoorn, A probabilistic approach to body fluid typing interpretation: an exploratory study on forensic saliva testing, Law, Probability and Risk 14(4) (2015) 323-339.
[32] J. deZoete, W. Oosterman, B. Kokshoorn, M. Sjerps, Cell type determination and association with the DNA donor, Forensic Science International: Genetics 25 (2016) 97-111.
[33] I.W. Evett, What is the probability that this blood came from that person? A meaningful question, Journal of the Forensic Science Society 23 (1983) 35-39.
[34] J. Buckleton, J.-A. Bright, D. Taylor, Forensic DNA Evidence Interpretation, second edition, CRC Press, Boca Raton, Florida, 2016.
[35] J.M. Butler, Forensic DNA typing, 2nd ed., Elsevier Academic Press2005.
[36] S.M. Willis, L. McKenna, S. McDermott, G. O'Donell, A. Barrett, B. Rasmusson, A. Nordgaard, C.E.H. Berger, M.J. Sjerps, J.-J. Lucena-Molina, G. Zadora, C. Aitken, T. Lovelock, L. Lunt, C. Champod, A. Biedermann, T.N. Hicks, F. Taroni, ENFSI Guideline for Evaluative Reporting in Forensic Science, European Network of Forensic Science Institutes (available at http://enfsi.eu/sites/default/files/documents/external_publications/m1_guideline.pdf), 2015.
[37] Association of Forensic Science Providers, Standards for the formulation of evaluative forensic science expert opinion, Science \& Justice 49(3) (2009) 161-164.
[38] G. Jackson, C. Aitken, P. Roberts, Case Assessment and Interpretation of Expert Evidence: Guidance for Judges, Lawyers, Forensic Scientists and Expert Witnesses, Royal Statistical Society 2015.
[39] P. Roberts, C. Aitken, The Logic of Forensic Proof: Inferential Reasoning in Criminal Evidence and Forensic Science: Guidance for Judges, Lawyers, Forensic Scientists and Expert Witnesses, Royal Statistical Society 2015.
[40] R. Puch-Solis, P. Roberts, S. Pope, C. Aitken, Assessing the probative value of DNA: Guidance for Judges, Lawyers, Forensic Scientists and Expert Witnesses, Royal Statistical Society 2015.
[41] C. Aitken, P. Roberts, G. Jackson, Fundamentals of Probability and Statistical Evidence in Criminal Proceedings: Guidance for Judges, Lawyers, Forensic Scientists and Expert Witnesses, Royal Statistical Society 2015.
[42] C. Berger, J. Buckleton, C. Champod, I. Evett, G. Jackson, Expressing evaluative opinions: A position statement, Science \& Justice 51(1) (2011) 1-2.
[43] F. Taroni, Biedermann A, J. Vuille, N. Morling, Whose DNA is this? How relevant a question? (a note for forensic scientists). , Forensic Science International: Genetics. 7 (2013) $467-470$.
[44] J. Vuille, L. Luparia, F. Taroni, Scientific evidence and the right to a fair trial under Article 6 ECHR, Law, Probability and Risk 16 (2017) 55-68.

[45] P. Gill, Misleading DNA Evidence: Reasons for Miscarriages of Justice, Elsevier 2014.
[46] A. Biedermann, S. Bozza, F. Taroni, Probabilistic evidential assessment of gunshot residue particle evidence (Part I): Likelihood ratio calculation and case pre-assessment using Bayesian networks, Forensic Science International 191 (2009) 24-35.
[47] P. Margot, Commentary on: the need for a research culture in the forensic sciences, UCLA Law Review 58 (2011) 795-801.
[48] A. Biedermann, F. Taroni, Bayesian networks for evaluating forensic DNA profiling evidence: A review and guide to literature, Forensic Science International: Genetics 6 (2012) 147-157.
[49] D. Lagnado, N. Fenton, M. Neil, Legal idioms: a framework for evidential reasoning, Argument \& Computation 4(1) (2013) 46-63.
[50] F. Taroni, A. Biedermann, S. Bozza, P. Garbolino, C. Aitken, Bayesian Networks and Probabilistic Inference in Forensic Science: Second Edition, John Wiley \& Sons, Ltd., Chichester, 2014.
[51] U. Kjaerulff, A. Madsen, Bayesian networks and Influence Diagrams, A Guide to Construction and Analysis, Springer, New York, 2008.
[52] M. Neil, N. Fenton, L. Nielson, Building large-scale Bayesian Networks, The Knowledge Engineering Review 15(3) (2000) 257-284.
[53] Q.A. Le, G. Strylewicz, J.N. Doctor, Detecting blood laboratory errors using a Bayesian network: an evaluation on liver enzyme tests, Medical Decision Making 31 (2011) 325-337.
[54] W. Edwards, Influence Diagrams, Bayesian Imperialism, and the Collins Case: An Appeal to Reason, Cardozo Law Review 13 (1991) 1025-1074.
[55] A.P. Dawid, J. Mortera, V. Pascali, D. van Boxel, Probabilistic expert systems for forensic inference from genetic markers, Scandinavian Journal of Statistics 29 (2002) 577595 .
[56] C. van-Dongen, K. Slooten, M. Slagter, W. Burgers, W. Wiegerinck, Bonaparte: Application of new software for missing persons program, Forensic Science International: Genetics Supplement Series 3 3(1) (2011) e119-e120.
[57] P.J. Green, J. Mortera, Sensitivity of inferences in forensic genetics to assumptions about founding genes, The Annals of Applied Statistics 3(2) (2009) 731-763.
[58] J. Mortera, A.P. Dawid, S.L. Lauritzen, Probabilistic expert system for DNA mixture profiling, Theoretical population biology 63 (2003) 191-205.
[59] C. Vlek, H. Prakken, S. Renooij, B. Verheij, Building Bayesian networks for legal evidence with narratives: a case study evaluation, Artificial intelligence and law 22(4) (2014) $375-421$.
[60] F. Taroni, C. Aitken, P. Garbolino, A. Biedermann, Bayesian Networks and Probabilistic Inference in Forensic Science, John Wiley \& Sons, Ltd., Chichester, 2006.

[61] D. Taylor, A. Biedermann, T. Hicks, C. Champod, A template for constructing Bayesian networks in forensic biology cases when considering activity level propositions, Forensic Science International: Genetics 33 (2018) 136-146.
[62] P. Gill, T. Hicks, J.M. Butler, E. Connolly, L. Gusmão, B. Kokshoorn, N. Morling, R.v. Oorschot, W. Parson, M. Prinz, P.M. Schneider, T. Sijen, D. Taylor, DNA Commission of the International Society for Forensic Genetics: Assessing the value of forensic biological evidence - guidelines highlighting the importance of propositions. Part I: Evaluation of DNA profiling comparisons given (sub)source propositions, Forensic Science International: Genetics (IN DRAFT) (2018).
[63] R. Cook, I.W. Evett, G. Jackson, P.P. Jones, J.A. Lambert, A model for case assessment and interpretation, Science and Justice 38(3) (1998) 151-156.
[64] P. Gill, J.P. Whitaker, C. Flaxman, N. Brown, J.S. Buckleton, An investigation of the rigor of interpretation rules for STR's derived from less that 100 pg of DNA, Forensic Science International 112(1) (2000) 17-40.
[65] D.J. Balding, J. Buckleton, Interpreting low template DNA profiles, Forensic Science International: Genetics 4(1) (2009) 1-10.
[66] D. Balding, Evaluation of mixed-source, low-template DNA profiles in forensic science., Proceedings of the National Academy of Sciences of USA 110(30) (2013) 12241-12246.
[67] H. Haned, Forensim: An open-source initiative for the evaluation of statistical methods in forensic genetics, Forensic Science International: Genetics 5(4) (2011) 265-268.
[68] K. Lohmueller, N. Rudin, Calculating the weight of evidence in low-template forensic DNA casework, Journal of Forensic Sciences 58(1) (2013) s234-259.
[69] M.W. Perlin, A. Sinelnikov, An information gap in DNA evidence interpretation., PLoS ONE 4(12) (2009) e8327.
[70] S. Højsgaard, Graphical Independence Networks with the gRain Package for R, Journal of Statistical Software 46(10) (2012) 1-26.
[71] M. Scutari, Learning Bayesian Networks with the bnlearn R Package, Journal of Statistical Software 35(3) (2010) 1-22.
[72] P. Gill, Analysis and implications of the miscarriages of justice of Amanda Knox and Raffaele Sollecito, Forensic Science International: Genetics 23 (2016) 9-18.
[73] J. Vuille, A. Biedermann, F. Taroni, The importance of having a logical framework for expert conclusions in forensic DNA profiling: illustrations from the Amanda Knox case, in: Wrongful Convictions and Miscarriages of Justice: Causes and Remedies in North American and European Criminal Justice Systems, in: K.M.E. Huff R.C. (Ed.), Routledge Chapman \& Hall New York, 2013, pp. 137-159.
[74] B. Szkuta, K.N. Ballantyne, B. Kokshoorn, R.A.H. van Oorschot, Transfer and persistence of non-self DNA on hands over time: Using empirical data to evaluate DNA evidence given activity level propositions, Forensic Science International: Genetics 33 8497.

[75] D. Taylor, A. Biedermann, L. Samie, K.-M. Pun, T. Hicks, C. Champod, Helping to distinguish primary from secondary transfer events for trace DNA, Forensic Science International: Genetics 28 (2017) 155-177.
[76] R v Pfennig, SASCFC 27, 2018.
[77] T. Kaplan, Monte Sereno Murder Case Casts Doubt on DNA Evidence, San Jose Mercury News, June 28 (2014).
[78] P. Gill, C.H. Brenner, J.S. Buckleton, A. Carracedo, M. Krawczak, W.R. Mayr, N. Morling, M. Prinz, P.M. Schneider, B.S. Weir, DNA commission of the International Society of Forensic Genetics: Recommendations on the interpretation of mixtures., Forensic Science International. 160 (2006) 90-101.
[79] E. Gasiorowski, The mystery of the Phantom of Heilbronn. 2016 (accessed 14/02/2018.2018).
[80] C. Himmelreich, Germany's Phantom Serial Killer: A DNA Blunder (content.time.com/time/world/article/0,08599,1888126,00.html). 2009 (accessed 14 February.2018).
[81] T. Paterson, DNA blunder creates phantom serial killer (www.independent.co.uk/news/world/europe/dna-blunder-creates-phantom-serial-killer1655375.html). 2009 (accessed 14 February.2018).
[82] F.H.R. Vincent, Inquiry into the circumstances that led to the conviction of Mr Farah Abdulkadir Jama 2010.
[83] G.-J.A. Knoops, Redressing Miscarriages of Justice. Practice and Procedures in (International) Criminal Cases 2nd revised edition, Martinus Nijhoff Publishers, Leiden, 2013.
[84] W. Wagenaar, False confessions after repeated interrogation: The Putten Murder Case, European Review 10(4) (2002) 519-537.
[85] C. Champod, DNA transfer: informed judgement or mere guesswork?, Frontiers in Genetics 4(Article 300) (2013) 1-3.
[86] A. Jamieson, LCN DNA analysis and opinion on transfer: R v Reed and Reed, International Journal of Evidence and Proof 15(2) (2011) 161-169.
[87] R.A.H. van Oorschot, K.N. Ballantyne, R.J. Mitchell, Forensic trace DNA: a review, Investigative Genetics 1(1) (2010) 14.
[88] G. Meakin, A. Jamieson, DNA transfer: Review and implications for casework, Forensic Science International: Genetics 7 (2013) 434-443.
[89] M. Goray, S. Fowler, B. Szkuta, R.A.H.V. Oorschot, An analysis of self and non-self DNA in multiple handprints deposited by the same individuals over time, Forensic Science International: Genetics 23 (2016) 190-196.
[90] M. Goray, R.J. Mitchell, R.A.H.v. Oorschot, Investigation of secondary transfer of skin cells under controlled conditions, Legal Medicine 12 (2010) 117-120.

[91] M. Goray, R.A.H.v. Oorschot, The complexities of DNA transfer during a social setting, Legal Medicine 17(2) (2015) 82-91.
[92] A.K. Buckingham, M.L. Harvey, R.A.H. van Oorschot, The origin of unknown source DNA from touched objects, Forensic Science International: Genetics 25 (2016) 26-33.
[93] A. Lowe, C. Murray, J. Whitaker, G. Tully, P. Gill, The propensity of individuals to deposit DNA and secondary transfer of low level DNA from individuals to inert surfaces., Forensic Science International 129 (2002) 25-34.
[94] S. Noel, K. Lagace, A. Rogic, D. Granger, S. Bourgoin, C. Jolicoeur, D. Sequin, DNA transfer during laundering may yield complete genetic profiles, Forensic Science International: Genetics 23 (2016) 240-247.
[95] M. Phipps, S. Petricevic, The tendency of individuals to transfer DNA to handled items, forensic Science International 168 (2007) 162-168.
[96] G.N. Rutty, An investigation into the transfer and survivability of human DNA following simulated manual strangulation with consideration of the problem of third party contamination, International Journal of Legal Medicine 116 (2002) 170-173.
[97] D. Taylor, D. Abarno, E. Rowe, L. Rask-Nielsen, Observations of DNA transfer within an operational Forensic Biology Laboratory, Forensic Science International: Genetics 23 (2016) 33-49.
[98] National Research Council Committee on Identifying the Needs of the Forensic Sciences Community. Strengthening Forensic Science in the United States: A Path Forward, National Academy Press, Washington, D.C., 2009.
[99] R v Dlugosz, Pickering, Court of Appeal of England and Wales (Criminal Division), EWCA Crim 2, 2013.
[100] P. Gill, Ø. Bleka, T. Egeland, Does an English appeal court ruling increase the risks of miscarriages of justice when complex DNA profiles are searched against the national DNA database?, Forensic Science International: Genetics 13(Supplement C) (2014) 167-175.
[101] A. Biedermann, S. Bozza, F. Taroni, C. Aitken, The meaning of justified subjectivism and its role in the reconciliation of recent disagreements over forensic probabilism, Science \& Justice 57 (2017) 477-483.
[102] C.M. Cale, M.E. Earll, K.E. Latham, G.L. Bush, Could cecondary DNA transfer falsely place someone at the scene of a crime?, Journal of Forensic Sciences 61(1) (2016) 196-203.
[103] B. Kokshoorn, B. Aarts, R. Ansell, L. McKenna, E. Connolly, W. Drotz, A.D. Kloosterman, Cale CM, Earll ME, Latham KE, Bush GL. Could cecondary DNA transfer falsely place someone at the scene of a crime? J Forensic Sci 2016;61(1):196-203, Journal of Forensic Sciences 61(5) (2016) 1401-1402.
[104] M. Goray, K.N. Ballantyne, B. Szkuta, R.A.H. van Oorschot, Cale CM, Earll ME, Latham KE, Bush GL. Could cecondary DNA transfer falsely place someone at the scene of a crime? J Forensic Sci 2016;61(1):196-203, Journal of Forensic Sciences 61(5) (2016) 13961398 .

[105] K. Steensma, R. Ansell, L. Clarisse, E. Connolly, A.D. Kloosterman, L.G. McKenna, R.A.H. van Oorschot, B. Szkuta, B. Kokshoorn, An inter-laboratory comparison study on transfer, persistence and recovery of DNA from cable ties, Forensic Science International: Genetics 31 (2017) 95-104.
[106] G. Jackson, The impact of commertialization on the evaluation of DNA evidence, Frontiers in Genetics 4 (2014) 16-18.
[107] G. Jackson, S. Jones, G. Booth, C. Champod, I.W. Evett, The nature of forensic science opinion-a possible framework to guide thinking and practicce in investigation and in court proceedings, Science \& Justice 46(1) (2006) 33-44.
[108] J.S. Buckleton, J.-A. Bright, D.A. Taylor, I. Evett, T. Hicks, G. Jackson, J.M. Curran, Helping formulate propositions in forensic DNA analysis, Science \& Justice 54(4) (2014) 258-261.
[109] A. Tversky, D. Kahneman, Judgment Under Uncertainty: Heuristics and Biases, Science 185(September 27) (1974) 1124-1131.
[110] A. O'Hagan, C. Buck, A. Daneshkhah, J. Eiser, P. Garthwaite, D. Jenkinson, J. Eiser, J. Oakley, P. Garthwaite, T. Rakow, Uncertain judgements: eliciting experts' probabilities, John Wiley \& Sons, West Sussex, England, 2006.
[111] I. Dror, R. Morgan, C. Rando, S. Nakhaeizadeh, The bias snowball and the bias cascade effects: two distinct biases that may impact forensic decision making, Journal of forensic sciences 62 (2017) 832-833.
[112] A. Jeanguenata, B. Budowle, I. Dror, Strengthening forensic DNA decision making through a better understanding of the influence of cognitive bias, Science and Justice 57 (2017) 415-420.
[113] D. Krane, S. Ford, J. Gilder, K. Inman, A. Jamieson, R. Koppl, I. Kornfield, D. Risinger, N. Rudin, M. Taylor, W. Thompson, Sequential unmasking: a means of minimizing observer effects in forensic DNA interpretation, Journal of Forensic Sciences 53(4) (2008) 1006-1007.
[114] I.E. Dror, Practical solutions to cognitive and human factor challenges in forensic science, Forensic Science Policy \& Management: An International Journal 4(3-4) (2013) 105113 .
[115] E.J. Mattijssen, W. Kerkhoff, C.E. Berger, I.E. Dror, R.D. Stoel, Implementing context information management in forensic casework: Minimizing contextual bias in firearms examination, Science \& Justice 56(2) (2016) 113-22.
[116] I. Dror, W. Thompson, C. Meissner, I. Kornfield, D. Krane, M. Saks, M. Risinger, Letter to the editor-context management toolbox: a linear sequential unmasking (LSU) approach for minimizing cognitive bias in forensic decision making, Journal of Forensic Sciences 60 (2015) 1111-1112.
[117] W. Thompson, What role should investigative facts play in the evaluation of scientific evidence?, Australian Journal of Forensic Science 43 (2011) 123-124.
[118] I. Dror, Practical solutions to cognitive and human factor challenges in forensic science, Forensic Science Policy \& Management 4 (2014) 105-113.

[119] W. Thompson, Determining the Proper Evidentiary Basis for an Expert Opinion: What Do Experts Need to Know and When Do They Know Too Much?, in: C. Robertson, A. Kesselheim (Eds.), Blinding as a Solution to Bias: Strengthening Biomedical Science, Forensic Science, and Law, Academic Press2016, pp. 133-150.
[120] M. Sjerps, C. Berger, How clear is transparent? Reporting expert reasoning in legal cases, Law, probability and risk 11(4) (2012) 317-329.
[121] N. Fenton, M. Neil, Avoiding probabilistic reasoning fallacies in legal practice using Bayesian networks, Australian Journal of Legal Philosophies 36 (2011) 114-150.
[122] J.M. Curran, T.N. Hicks, J. Buckleton, Forensic Interpretation of Glass Evidence, CRC Press, Boca Raton, 2000.
[123] I.W. Evett, A Quantitative Theory for Interpreting Transfer Evidence in Criminal Cases, Applied Statistics 33(1) (1984) 25-32.
[124] C. Champod, F. Taroni, Interpretation of Fibres Evidence - The Bayesian Approach, in: M. Grieve, J. Robertson (Eds.), Forensic Examination of Fibres, Taylor \& Francis Ltd., London, 1999, pp. 379-398.
[125] A. Biedermann, T. Hicks, R. Voisard, F. Taroni, C. Champod, C. Aitken, I. Evett, Elearning initiatives in forensic interpretation: report on experiences from current projects and outlook., Forensic Science International 230, (2013) 2-7.
[126] B. Robertson, G.A. Vignaux, C.E. Berger, Interpreting Evidence - Evaluating Forensic Science in the Courtroom, 2nd edition, John Wiley \& Sons Inc., Chichester, 2016.
[127] A. Kloosterman, M. Sjerps, A. Quak, Error rates in forensic DNA analysis: Definition, numbers, impact and communication, Forensic Science International: Genetics 12 (2014) 7785 .
[128] W.C. Thompson, F. Taroni, C.G.G. Aitken, How the probability of a false positive affects the value of DNA evidence., Journal of Forensic Science 48(1) (2003) 1-8.
[129] F. Taroni, A. Biedermann, P. Garbolino, C.G.G. Aitken, A general approach to bayesian networks for the interpretation of evidence., Forensic Science International 139 (2004) 5-16.
[130] D. Taylor, Probabilistically determining the cellular source of DNA derived from differential extractions in sexual assault scenarios, Forensic Science International: Genetics 24 (2016) 124-135.
[131] J. Curran, An introduction to Bayesian credible intervals for sampling error in DNA profiles, Law, Probability and Risk 4 (2005) 115-126.
[132] D. Taylor, J.A. Bright, J. Buckleton, J. Curran, An illustration of the effect of various sources of uncertainty on DNA likelihood ratio calculations, Forensic Science International: Genetics 11 (2014) 56-63.
[133] J.-A. Bright, K.E. Stevenson, J.M. Curran, J.S. Buckleton, The variability in likelihood ratios due to different mechanisms, Forensic Science International: Genetics 14 (2015) 187190 .

[134] J.-A. Bright, D. Taylor, C. McGovern, S. Cooper, L. Russell, D. Abarno, J. Buckleton, Developmental validation of STRmix ${ }^{\mathrm{TM}}$, expert software for the interpretation of forensic DNA profiles, Forensic Science International: Genetics 23 (2016) 226-239.
[135] G. Morrison, Special issue on measuring and reporting the precision of forensic likelihood ratios: Introduction to the debate, Science \& Justice 5 (2016) 371-373.
[136] G. Morrison, E. Enzinger, What should a forensic practitioner's likelihood ratio be?, Science \& Justice 5 (2016) 374-379.
[137] J. Curran, Admitting to uncertainty in the LR, Science \& Justice 5 (2016) 380-382.
[138] D. Ommen, C. Saunders, C. Neumann, An argument against presenting interval quantifications as a surrogate for the value of evidence, Science \& Justice 5 (2016) 383-387.
[139] C. Berger, K. Slooten, The LR does not exist, Science \& Justice 5 (2016) 388-391.
[140] A. Biedermann, S. Bozza, F. Taroni, C. Aitken, Reframing the debate: A question of probability, not of likelihood ratio, Science \& Justice 5 (2016) 392-396.
[141] A.v.d. Hout, I. Alberink, Posterior distribution for likelihood ratios in forensic science, Science \& Justice 5 (2016) 397-401.
[142] D. Taylor, T. Hicks, C. Champod, Using sensitivity analyses in Bayesian networks to highlight the impact of data paucity and direct future analyses: a contribution to the debate on measuring and reporting the precision of likelihood ratios, Science \& Justice 56(5) (2016) $402-410$.
[143] A. Nordgaard, Comment on 'Dissmissal of the illusion of uncertainty on the assessment of a likelihood ratio' by Taroni F., Bozza S., Biedermann A. and Aitken C., Law, Probability and Risk 15 (2016) 17-22.
[144] F. Taroni, S. Bozza, A. Biedermann, C. Aitken, Dismissal of the illusion of uncertainty in the assessment of a likelihood ratio, Law, Probability and Risk 15 (2016) 1-16.
[145] A. Biedermann, F. Taroni, Bayesian networks and probabilistic reasoning about scientific evidence when there is a lack of data, Forensic Science International 157(2-3) (2006) 163-167.
[146] E. Murphy, Inside the cell: the dark side of forensic DNA, Nation Books, New York, 2015.