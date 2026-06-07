# Toward a hybrid approach for the risk analysis of maritime autonomous surface ships: a systematic review 

Tomohiro Yuzui ${ }^{1} \cdot$ Fujio Kaneko ${ }^{2}$<br>Received: 6 September 2023 / Accepted: 8 December 2024 / Published online: 9 January 2025<br>© The Author(s) 2025


#### Abstract

As the demand for maritime autonomous surface ships (MASS) grows, appropriate risk analysis is essential for ensuring their safety. Several review papers have examined effective methods for MASS risk analysis, highlighting the benefits of qualitative approaches such as the systems-theoretic accident model and process/system-theoretic process analysis (STAMP/ STPA). However, a comprehensive and objective analysis method for MASS has not yet been established. In addition, a systematic literature review of the available academic research studies on MASS risk analysis has not been previously conducted. Therefore, this study employed principles from the preferred reporting items for systematic reviews and meta-analysis (PRISMA) for conducting a systematic literature review on MASS risk analysis. Besides, to conduct the review considering various aspects of risk analysis, we developed the classification framework of risk analysis of MASS and conducted the review using the developed framework. We concluded that a hybrid approach, combining a quantitative analysis by the Bayesian network using qualitative STAMP/STPA results, may prove to be effective for MASS risk assessment. In addition, based on the analyzed literature, research directions for future studies considering the gaps between current research and the real-world implementation of MASS were identified.


Keywords Maritime autonomous surface ships $\cdot$ Risk assessment $\cdot$ Preferred reporting items for systematic reviews and meta-analysis (PRISMA) $\cdot$ STAMP/STPA $\cdot$ Bayesian network


[^0]
## 1 Introduction

Since its development in the 1990s, the Formal Safety Assessment (FSA) [88] has emerged as a prominent rulemaking tool within the International Maritime Organization (IMO). Consequently, risk assessment has gained significant recognition within the shipping sector. Given that the FSA serves as a regulatory tool, the historical


[^0]:    Tomohiro Yuzui
    yuzui@m.mpat.go.jp
    1 Port and Aviation Technology (MPAT), National Maritime Research Institute (NMRI), National Institute of Maritime, 6-38-1, Shinkawa, Mitaka, Tokyo, Japan
    2 Ex-NMRI, Tokyo, Japan

objective behind conducting risk assessments within the shipping industry has frequently revolved around rulemaking within the IMO. However, in recent years, an increasing number of regulations, such as the IGF Code [87], have mandated the implementation of risk assessments during the design phase in the shipping industry. As a result, the objectives behind conducting risk assessments have become diverse.

Currently, the development of maritime autonomous surface ships (MASS) is being promoted worldwide. Discussions on the formulation of international regulations for MASS have been started by the IMO, with the first goal of adopting a non-mandatory MASS code by 2024 [91]. In addition, several classification societies have published their own guidelines for safe MASS design and operation [2, 24, 37, 54, 117]. These guidelines stipulate that risk assessments should be carried out at the time of design and highlight that risk assessments are effective for improving MASS safety.

Unsurprisingly, MASS risk analysis is currently an area of intense research. Several scholars have conducted reviews on risk analysis studies for conventional ships and MASS to determine which risk analysis tools are suitable for MASS risk analysis. Hoem [82] conducted an extensive review of the literature on MASS risk assessment methods prior to 2018, including an in-depth review of eight key papers. Zhou et al. [215] evaluated the applicability of 29 representative risk assessment methods obtained from a survey of 269 articles published in the past 50 years, including MASS and existing manned vessels, for MASS risk assessment. Thieme et al. [170] examined papers related to the risk assessment of ship collisions and strandings, including existing manned ships and MASS, published since 2005 and evaluated the 64 risk assessment methods presented in those papers. Veitch and Andreas Alsos [185] conducted a systematic review of human-AI interaction-related papers published between January 1, 2010 and November 12, 2021, and evaluated nine risk assessment methods as one part of the review. These review papers provide some findings on the risk assessment methods for MASS. However, the papers by Hoem [82], Thieme et al. [170], and Zhou et al. [215] do not reflect the latest risk assessment studies of MASS because the targeted papers are outdated, include both MASS and existing manned vessels, and do not implement a systematic literature review. Veitch and Andreas Alsos [185] did not conduct a thorough survey and in-depth analysis on the MASS risk assessment method because the risk assessment is handled as one part of a systematic review. Also, other than these review papers, there is a paper that conduct a bibliometric review of literature relating to risk and reliability analysis of MASS [213]. Zhihong et al. [213] mainly handles bibliometric analysis, did not conduct in-depth analysis on the MASS risk assessment method. In addition, as discussed below, a risk analysis can be classified into three types: qualitative, semi-quantitative, and quantitative. However, the previous review papers did not consider these differences.

Therefore, we conducted a systematic review solely on papers regarding MASS risk analysis. The aim of this review is to attempt to answer the following research questions (RQs):

RQ1: What risk analysis methodologies were employed in the research studies on MASS risk analysis?
RQ2: What areas of research were the studies on MASS risk analysis applied to?
RQ3: What tools are suitable for MASS risk analysis?
RQ4: What are the research agendas for the practical application of MASS?

RQ1 and RQ2 aim to identify the scientific methodologies and applied research areas employed in the academic MASS risk analysis studies. Using the findings obtained from RQ1 and RQ2, we attempt to investigate the effective tools for MASS risk analysis and identify the research directions for future studies, considering the gaps between current research and the real-world implementation of MASS to answer RQ3 and RQ4. In this way, a succinct description of the progress of MASS risk analysis and future research directions can be realized. To state the conclusions of this study upfront, the hybrid approach of STAMP/STPA and BN has been suggested to be promising. This implication is reflected in the title of this paper. Ultimately, we hope that this paper will provide a good reference for researchers, allowing them to make further contributions to the industry.

There are various aspects of risk analysis. To conduct a literature review covering various aspects of risk analysis, Isaac and Mahmood [92] propose a classification framework. In Issac and Mahmood [92], the classification framework for risk analysis in the LNG sector is proposed, and a literature review is conducted using the framework. We developed a classification framework for risk analysis of MASS referring to the framework in the LNG sector and conducted a systematic review utilizing the developed framework. This covers other aspects of risk analysis of MASS, which may need to be added in previous review studies. This is one of the originalities of this study.

Risk analysis is just one of the technologies used to examine the safety of a target system. To evaluate MASS safety, several studies have been performed to analyze the safety of MASS using different approaches, including model

experiments, onboard experiments, simulation tests, and risk analysis. This study specifically concentrated on the risk analysis of MASS and conducted an extensive investigation of the subject. It is important to note that this study did not include other approaches.

In addition, human factors are still important in MASS safety, and several scholars have conducted research from various perspectives, such as risk analysis, human--machine interface, and cognitive modeling. As mentioned above, Veitch and Andreas Alsos [185] conducted a systematic review, and explored the human factors of MASS from multiple angles. Therefore, for the purpose of this review, which specifically focused on risk

![img-0.jpeg](img-0.jpeg)

Fig. 1 Flow of information through the different phases of the systematic literature review analysis studies of MASS, human factors were not explicitly addressed.

The remainder of this paper is organized as follows. The literature review methodology is presented in Sect. 2. Section 3 answers the investigated RQs using the presented methodology and discusses the limitations of the review. Finally, we present our conclusions in Sect. 4.

## 2 Methodology of the systematic review

The systematic review presented in this study was based on PRISMA [115]. The information flow based on the PRISMA methodology is shown in Fig. 1. The steps of the methodology are elaborated in the subsequent sections.

### 2.1 Step 1: identification of the research studies

The identification of the relevant studies was implemented using Scopus and ScienceDirect as the search engines. We decided to exclude Google Scholar as the results generated using that search engine included multiple low-quality publications that were not peer-reviewed or were aimed at a more general audience, that is, not targeted at an academic audience, and contributed to the diffusion of the conducted research [18].

The literature was identified using the protocol presented in Table 1. As shown in Table 1, this study targeted papers published from 2018 onwards. We determined this considering holistically the following three points:
a. The IMO commenced work to look into how safe, secure, and environmentally sound MASS operations may be addressed in IMO instruments, from Maritime Safety Committee (MSC), 99th session which was held in 2018 [89],

Table 1 Review protocol


b. The implementation of MASS projects gained momentum globally after 2018, as evidenced by an increase in the number and scale of projects initiated during this period. For instance, the EU-funded MUNIN project [149], DNV GL ReVolt project [53], and Finland-funded AAWA project led by Rolls-Royce [47] were conducted prior to 2017, while the MEGURI 2040 program in Japan (Nippon Foundation[133]), AUTOSHIP in the EU [10], and the Ghost Fleet Overlord Unmanned Surface Vessel Program in the United States [179], KASS project in Korea [103], and others have been conducted since 2018,
c. Previous reviews [82, 170, 215] primarily focused on papers published before 2017.

Considering the rapidly evolving nature of IoT systems and MASS, it may not be suitable to include articles that are more than 5 years old in this study. By focusing on the most recent research findings, this study has targeted the past 5 years of publications.

In addition, we did not limit the publication style, considering that MASS is a new area that has not been fully developed; therefore, the search results included journal and conference papers as well as book chapters.

The search was conducted on March 30, 2023. A total of 146 and 696 papers were found on Scopus and ScienceDirect, respectively, which included 47 duplications. After removing the duplications, 795 papers were identified.

### 2.2 Step 2: screening of the research studies

The screening was conducted by reading the title and abstract of each identified paper. By reducing the number of target papers, we were able to conduct a more thorough analysis of the most relevant papers. The screening was performed by considering whether the research targeted the risk analysis/assessment of MASS rather than conventional ships. The papers targeting piracy and organizational risks were excluded, whereas the papers targeting safety and/or cybersecurity risks relating to accidents such as collision, grounding, and fire were included. We also excluded review papers. Consequently, 107 papers remained, indicating a retention rate of 107/795, or $13 \%$.

### 2.3 Step 3: eligibility assessment of the research studies

The screened studies were further analyzed, and the most suitable were selected for further processing. Similar to Step 2, this process was conducted by considering whether the research targeted the risk analysis/assessment of MASS. In general, the term "risk" is used ambiguously, and the screened papers applied various definitions of the term "risk." For example, some papers defined risk as a situation in which a ship was abnormally close to other ships and analyzed the number of abnormally close ships through simulations; such papers were excluded. In this study, "risk" was defined as the product of probability/frequency and severity of consequences in accordance with the engineering field. We included the papers that used risk analysis tools, which will be discussed in Sect. 2.4. Papers that proposed a methodological framework but did not apply it to MASS risk analysis were excluded. Moreover, certain papers targeted the risk analysis/assessment of robots and UUVs; such papers were excluded. In addition, a limited number of papers were unfortunately inaccessible and had to be excluded. Consequently, 47 papers remained (47/107, or $44 \%$ ). The papers reviewed in this study and the previous review studies $[82,170,185,215]$ are presented in Appendix Table 2. The reviewed literature in this study was found to differ from that in previous review studies [82, 170, 185, 215].

### 2.4 Step 4: analysis of the included research studies

A detailed analysis of the eligible, selected studies was conducted to answer the following RQs.

RQ1: What risk analysis methodologies were employed in the research studies on MASS risk analysis?

![img-1.jpeg](img-1.jpeg)

Fig. 2 Classification framework for MASS risk analysis

RQ2: What areas of research were the studies on MASS risk analysis applied to?
RQ3: What tools are suitable for MASS risk analysis?
RQ4: What are the research agendas for the practical application of MASS?

To answer these RQs, we propose a classification framework, as shown in Fig. 2. We categorized the MASS risk analysis into six different themes, as described below. This framework was developed with reference to Isaac and Mahmood [92] which is a review paper on risk analysis in the LNG sector. The framework in Isaac and Mahmood [92] includes the following five themes: risk analysis methods, risk analysis tools, data sources, output/strategy, and applications. This study, however, focuses on MASS, not LNG, and the RQs differ from those in Isaac and Mahmood [92]. Therefore, the framework was modified as follows: three themes (risk analysis methods, risk analysis tools, and applications) were adopted from Isaac and Mahmood [92], and two additional themes (target indexes and target risk types) were added. However, risk analysis methods were renamed risk analysis types, and applications were subdivided into target MASS types and target accidents. In addition, two themes (target indexes and target risk types) were included. The details of each theme are as follows.

## Risk analysis types

According to ISO [93], identifying hazards and estimating risks is called "risk analysis," determining the risk tolerance estimated by the "risk analysis" is referred to as "risk evaluation," and the combined process of "risk analysis" and "risk evaluation" is called "risk assessment." According to the UK-HSE [175], risk analyses can be roughly divided into three categories: qualitative, semi-quantitative, and quantitative. A qualitative risk analysis primarily involves the identification of hazards and their causes and consequences. In a semi-quantitative risk analysis, cause-to-consequence scenarios are considered, and the risks are roughly quantified on a logarithmic scale. A quantitative risk analysis numerically measures the risks of cause-to-consequence scenarios. In this study, the 47 selected papers were classified into qualitative, semi-quantitative, and quantitative risk analyses.

The terms and definitions of risk analysis types in the MASS code have not yet been determined. The IMO documents relating to risk analysis, FSA guidelines [88] have already been opened to the public. The FSA comprises five distinct steps, and the first two are dedicated to risk analysis. The first and second steps are referred to as "Hazard Identification (HAZID)," and "Risk Analysis," respectively. In the first step, two tasks are conducted. One is the identification of hazards and their causes and consequences,the other is the roughly quantification of the risks of the cause-to-consequence scenarios on a logarithmic scale. These tasks are identical to those outlined in UK-HSE [175]. Specifically, the former corresponds to the qualitative analysis described in UK-HSE [175], while the latter aligns with the semi-quantitative analysis detailed in UK-HSE [175]. In the second step of the FSA, the risks of the cause-toconsequence scenarios are quantified on a numerical scale. This process is also comparable to the quantitative analysis outlined in UK-HSE [175]. Although the terminology used in IMO [88] and UK-HSE [175] differs, the tasks performed remain identical. It is noteworthy that the terms utilized by UK-HSE [175] are more consistent with the tasks carried out,thus, this study employs the terminology utilized in UKHSE [175].

## Risk analysis tools

Over the past 2 decades, several risk analysis tools have been developed to support risk-based decision-making in various industries [8]. In this study, the tools used in 47 papers were classified as FMEA, STAMP/STPA, ET, FT, and BN. These tools are frequently used in the maritime sector, and the classification is similar to that of the previous review paper by Thieme et al. [170]. HAZOP and FRAM were also considered to be keywords of the review protocol (Table 1); however, these tools were not used in any of the selected papers. Therefore, these tools were not included in the classification. Although a few papers employed ESD, we regarded ESD as ET in this study because ESD is logically equivalent to ET [139].

## Target indexes

As mentioned above, the definition of risk in the engineering field is the product of probability/frequency and severity of consequences. If semi-quantitative or quantitative risk analyses are conducted, the risk is obtained using a logarithmic scale or numerical figure. However, in the case of a quantitative analysis, some studies obtained the accident probability and system failure rate, which are input values to calculate risk, rather than directly assessing risk itself. The system failure rate is one of the factors to consider in estimating the accident probability. We investigated the type of indexes used in the studies if they were quantitative in nature.

## Target risk types

Recently, the threat to conventional ships has increased as their on-shore connections have increased. Threats to MASS are also significant. Therefore, risk analyses are important not only for safety but also for cybersecurity. We classified the target risks of the 47 selected studies into safety, cybersecurity, or both (safety and cybersecurity).

## Target MASS types for the risk analysis

MASS can be categorized according to different levels of autonomy. Currently, more than six international authorities

have published different levels of autonomy for ships [65], including IMO [90], LR [117], DNV-GL [54], BV [24], ClassNK [37], and ABS [2]. We applied a simple classification for the levels of autonomy considering automated and remotely controlled ships because there are no globally agreed upon definitions, few papers exist that clearly mention the autonomy levels of MASS-targeted risk analyses, and most papers do not specify the levels of autonomy of MASS. We classified the analyzed MASS types in the reviewed papers into "automated," "remote," "both," and "unknown." Some papers analyzed both automated and remotely controlled ships, in which case, we classified the papers as "both." Moreover, some papers did not mention the analyzed MASS types, in which case, we classified them as "unknown."

Target accidents for the risk analysis
In general, risk analysis is conducted to prevent accidents from occurring and/or mitigate the severity of the accidents. The accidents considered in the MASS risk analysis were classified into four categories: "collision," "other navigational accidents" such as grounding and contact, "system malfunction," and "other." Numerous studies target multiple accidents, for example, collision and accidents such as grounding, contact, and fire, in which case, we classified the study as "collision." For the cases where the target accident of the study did not include collision but rather grounding or contact, we classified the study as "other navigational accidents." A few studies targeted a system malfunction rather than specific accidents, in which case, we classified the study as "system malfunction." Where we could not classify the study into any of the above categories, the study was classified as "other."

## 3 Results and discussion

Appendix Table 3 presents the results of the analysis of the 47 papers according to the classification framework shown in Fig. 2.

### 3.1 RQ1: what risk analysis methodologies were employed in the research studies on MASS risk analysis?

The number distribution of each risk analysis type is depicted in Fig. 3. The total number of the analyzed publications was 47, the number of qualitative and quantitative studies was the same (18/47, or 38\%), while the number of semi-quantitative studies was slightly lower (11/47, or 23\%). These studies excluding published in 2023 are plotted by the
![img-2.jpeg](img-2.jpeg)

Fig. 3 Risk analysis types in the analyzed studies
published year (Fig. 4). Because the studies published in 2023 are for approximately 3 months and not for 1 year, we focused on the numbers from 2018 to 2022. Therefore, the total number of the targeted publications was 43, less than that in Fig. 3. Figure 4 shows that the number of studies on MASS risk analysis is increasing, indicating the increasing importance of MASS risk analysis research. Considering the risk analysis types, the number of qualitative studies is the highest from 2018 to 2020; however, the number of quantitative studies is the highest from 2021 to 2022, suggesting that the main objective of MASS risk analysis is changing; that is, the main objective has changed from hazard identification to risk value quantification.

The distribution of the risk analysis tools used in the analyzed studies is shown in Fig. 5. Note that the sum of the numbers for each used tool shown in Fig. 5 (total: 67, qualification: 25 , semi-quantitative: 15 , quantitative: 27) is higher than that of the analyzed papers (total: 47, qualification: 18, semi-quantitative: 11, quantitative: 18) because there are cases where multiple tools are used in one study. According to Fig. 5, STAMP/STPA is the most frequently used tool in qualitative studies, whereas BN is the most frequently used tool in quantitative studies. Three papers on quantitative studies $[13,98,99]$ conducted hazard identification, and the accident scenarios were modeled using the hazard identification results, therefore, a combination of STAMP/STPA and BN was used. Thus, STAMP/STPA was most frequently used, irrespective of the type of risk analysis.

Fig. 4 Chronological changes in the number of publications according to risk analysis type
![img-3.jpeg](img-3.jpeg)

The distribution of the calculated indexes in the quantitative risk analysis studies is shown in Fig. 6. In this study, research that calculated risk was counted as 'Risk,' even if it also calculated accident probability or failure rate. In addition, research that did not calculate risk but did calculate accident probability was counted as 'Accident Probability,' even if it also calculated failure rate. The total number of the analyzed publications was 18. Although the number of studies calculating "risk" was the highest ( $6 / 18$, or $33 \%$ ), there were some studies that used accident probability or the system failure rate, which are input values, to calculate the risk, and the number of these are same ( $4 / 18$, or $22 \%$ ). Estimating the risk, accident probability, and severity of consequences with greater accuracy requires a significant amount of work. As a result, expert opinions are frequently employed to determine these values. In various studies that calculated the risks or accident probabilities depicted in Fig. 6, expert opinions were utilized to obtain the system failure rates. If the accident probability will be estimated with higher reliability, the system failure rates should be
calculated using probability calculation tools, such as FT. Although "Accident probability" and "Failure rate" are the same values in Fig. 6, this may suggest that two distinct types of research are progressing concurrently: (1) research aimed at obtaining the accident probability of MASS, even if it has lower reliability (referenced as "Accident probability" in Fig. 6), (2) element research to estimate the accident probability of MASS with higher reliability (referenced as "Failure rate" in Fig. 6).

### 3.2 RQ2: what areas of research were the studies on MASS risk analysis applied to?

The classification results of the target risk types in the analyzed studies are shown in Fig. 7. The targeted studies were same as Fig. 3, the total number of the analyzed publications was 47 . Most of the studies ( $35 / 47$, or $74 \%$ ) target only safety risk, a few studies ( $4 / 47$, or $9 \%$ ) target only cybersecurity risk, and the remaining ( $8 / 47$, or $17 \%$ ) target both safety and cybersecurity risks.

Fig. 5 Distribution of the risk analysis tools used in the analyzed studies
![img-4.jpeg](img-4.jpeg)

Figure 8 shows the distribution of the target MASS types for all the analyzed 47 studies which were same as Figs. 3 and 7. According to Fig. 8, the number of studies on automated control ships (20) is almost the same as that on remotely controlled ships (17). These percentages are $43 \%(20 / 47)$ and $36 \%(17 / 47)$, respectively. There were four studies that targeted both MASS types (4/47, or $9 \%$ ). Unfortunately, six studies did not mention the target MASS types ( $6 / 47$, or $13 \%$ ). Herein, we investigated the risk analysis tools used in the papers that targeted automated and remotely controlled ships, as shown in Fig. 9. Figure 9 shows the numbers and percentages of risk analysis tools used in the studies targeting automated and remotely controlled ships in Fig. 8, and those in the studies targeting both in Fig. 8 are not included. Noted that the numbers of risk analysis tools used in the studies are counted in Fig. 9 like Fig. 5, although the numbers of studies are reckoned in Fig. 8; therefore, the total numbers of automated and remotely controlled ships in Fig. 9 are different from the numbers of those in Fig. 8, respectively. In the studies on automated controlled ships,

Fig. 6 Indexes calculated in the quantitative studies

Fig. 7 Target risk types in the analyzed studies
![img-5.jpeg](img-5.jpeg)
![img-6.jpeg](img-6.jpeg)

Fig. 8 Target MASS types in the analyzed studies
the total number of used tools was 29: FMEA (3, 10\%), STAMP/STPA (7, 24\%), ET (1, 3\%), FT (3, 10\%), BN $(7,24 \%)$, and others $(8,28 \%)$. For remotely controlled
ships, the total number of used tools was 26: FMEA ( 0 , $0 \%$ ), STAMP/STPA ( $8,31 \%$ ), ET ( $2,8 \%$ ), FT ( $2,8 \%$ ), BN $(6,23 \%)$, and others $(8,31 \%)$. According to Fig. 9, the percentages of BN for automated and remotely controlled ships are almost the same, and the same applies to FT. On the other hand, regarding the percentages of STAMP/STPA, FMEA, and ET, there are differences between automated and remotely controlled ships. The percentage of STAMP/STPA for remotely controlled ships is larger than that for automated ships. A characteristic of STAMP/STPA is an analysis of the interactions between the components. Therefore, this result may suggest that the scholars regarded analyzing the interaction between the components in the risk analyses for remotely controlled ships as important. Although the percentages between automated and remotely controlled ships differ depending on tools, STAMP/STPA and BN are most frequently used in the risk analyses of both automated and remotely controlled ships, suggesting that these tools can be used irrespective of the MASS type.

The classification of the target accidents in the analyzed 47 studies, which were same as Figs. 3, 7 and 8, is shown in Fig. 10. Most of the studies (29/47, or 62\%) target collision, a few studies target other navigational accidents (4/47, or $8 \%$ ) and system malfunctions ( $5 / 47$, or $11 \%$ ), and the remaining ( $9 / 47$, or $19 \%$ ) target others.

Fig. 9 Comparison of the risk analysis tools used in the studies that targeted a automated and b remotely controlled ships

Fig. 10 Target accidents in the analyzed studies
![img-7.jpeg](img-7.jpeg)
![img-8.jpeg](img-8.jpeg)

### 3.3 RQ3: what tools are suitable for MASS risk analysis?

To answer RQ3, we determined the definition of the superiority. The superiority was defined as the number of cases. It
was challenging to define the superiority because it encompasses various aspects, including usability, rigor, flexibility, cost, etc.; in addition, the weights of these aspects may vary on a case-by-case basis. We can regard that these various aspects and their weights are considered in the selection of

tools for risk analysis, although they may not be considered explicitly. Therefore, this study assumed that the superiority, considering these multiple aspects comprehensively, was reflected in "the number of cases," and thus defined "superiority".

Figure 5 shows that STAMP/STPA is the most frequently used tool in the analyzed papers, followed by BN. Therefore, these tools can be considered as suitable for MASS risk analysis. The previous review papers by Thieme et al. [170] and Zhou et al. [215] suggested that STAMP/STPA is the best risk analysis tool for MASS. MASS is a large and complex system, and in the case of such systems, inappropriate interactions among the components may cause an accident. Therefore, in MASS risk analysis, inappropriate interactions among the components as well as single component failures, which are the main targets of conventional risk analysis tools such as FMEA, should be analyzed. STAMP/STPA is capable of analyzing both inappropriate interactions among the components and single component failures, making it a suitable tool for qualitative risk analysis of MASS. Moreover, Veitch and Andreas Alsos [185] indicated that STAMP/STPA and BN are the most appropriate tools for MASS. Utne et al. [180] and Johansen and Utne [99] proposed methods to perform qualitative analysis using STAMP/STPA and generated BN from the results for a quantitative assessment. Therefore, the combination of STAMP/STPA and BN, as proposed by Utne et al. [180] and Johansen and Utne [99], may have potential as a risk assessment method for MASS. In risk analyses conducted in the maritime sector, there is a weak link between qualitative and quantitative analyses. This deficiency is particularly prominent in FSA studies, as noted by Kontovas and Psarafits [110] and Psarafits [143]. To address this issue, the combination of STAMP/STPA and BN, as proposed by Utne et al. [180] and Johansen and Utne [99], can strengthen the link between qualitative and quantitative analyses. Moreover, from this viewpoint, the combination of STAMP/STPA and BN proves to be a valuable risk analysis method.

Some studies regarding the quantitative risk analysis of MASS used ET and/or FT rather than BN, as shown in Fig. 5. Thus, the combination of STAMP/STPA and ET or FT is also considered useful; however, the use of BN is considered optimal for the following reasons.

Reason 1: ET and FT can be converted to BN.
Bearfield and Marsh [14], Jianfeng et al. [97], and Hao [78] described methods for converting ET to BN, whereas Bobbio et al. [17], Medkour et al. [121], and Shi et al. [159] described methods for converting FT to BN. Therefore, the models in the literature that use FT and ET, as presented in Appendix Table 3, can be converted to BN.

Reason 2: As indicated by Weber et al. [192], BNs have the following advantages: the ability to model complex systems, make predictions and diagnoses, accurately calculate the probability of an event occurring, update calculations according to evidence, represent multimodal variables, and support user-friendly modeling with a graphical and compact approach. For example, in contrast to ET and FT, when a MASS accident occurs, the cause can be estimated using BN by updating the calculations according to the evidence.

### 3.4 RQ4: what are the research agendas for the practical application of MASS?

Although risk analysis studies for MASS have been conducted, many issues have not been explicitly addressed in previous studies. The most significant issues are as follows.

First, as shown in Fig. 10, although there are many studies on target collisions, there are few studies relating to other accidents, such as grounding, contact, fire/explosion, and capsizing/flooding. While collisions are a hot topic also in studies on conventional ships [32], there are also many studies on maritime accidents other than collisions involving conventional ships. For example, in previous FSA studies [48], [49], [50], [51], [52], [86], the risk analyses for various maritime accidents (collision, grounding, contact, fire/explosion, capsizing/flooding, and hull/machinery damage) were conducted for major ship types (LNG carriers, container vessels, cruise ships, RoPax ships, oil tankers and general cargo ships). As in the research for conventional ships, we consider it necessary to advance quantitative analysis research for MASS on accidents other than collisions and to consider safety measures according to their risk values.

Second, although there are many studies relating to safety, there are a few studies relating to cybersecurity, as shown in Fig. 7. Further research on cybersecurity may be required to consider the cybersecurity-related risk factors when constructing accident scenarios in quantitative risk analyses.

Third, risk analysis studies that consider the different levels of automation may be required because the MASS risk value as well as hazard appears to depend on the level of automation, malfunctions when communicating with

the remote control center (RCC), and human intervention. As mentioned above, the reviewed papers do not explicitly describe the autonomy levels. Therefore, in this study, the levels of autonomation for MASS targeted by the reviewed papers were classified into only two categories: automated and remotely controlled ships. However, since the autonomy levels proposed by international authorities [2, 24, 37, 54, 90, 117] are more detailed, it will be necessary in the future to clearly state which level of automation proposed by the authorities the MASS targeted for risk analysis corresponds to, and then conduct the risk analysis accordingly. This will allow for a clearer understanding of the hazards and risk values associated with each detailed level of automation, enabling a more thorough examination of the safety of MASS.

Finally, a risk analysis study on ship insurance may be required. The practical application of MASS requires not only technological development and rule-making but also the construction of social institutions such as ship insurance. Traditionally, shipping insurance has been based on the statistical analysis of historical accident databases. However, in the case of a highly novel system, such as MASS, it is difficult to set insurance premiums because there are no accidents to date. This situation can hinder the practical application of MASS. Therefore, insurance companies have begun research on developing insurance products for MASS using risk analysis [38]. In the field of automated vehicles (AVs), research has been conducted to develop a system to conduct AV risk analyses in BNs, estimate aggregate claims loss, and calculate insurance premium rates (for example, in the studies conducted by Sheehan [156] and Sheehan et al. [157]). By implementing the same approach for MASS, it will be possible to use BNs for ship insurance in the future. As reviewed in this study, there are many studies that use BN for risk analysis of MASS, and it seems possible to utilize the results of these studies. However, as these studies do not conduct risk analysis for the purpose of developing insurance products, improvements are necessary. Specifically, the development of a consistent assessment system, from risk analysis to total claim loss estimation and premium rate calculation through a combined STAMP/STPA and BN approach will be a future challenge.

### 3.5 Limitations

Because of the possible ambiguity of terms used in the search query, the database shown in Table 1 may have provided papers that are not related to the topic of this study, that is, MASS risk analysis. Therefore, manual work was conducted to reject unrelated papers to MASS risk analysis, as explained in Sect. 2. In addition, manual work was also conducted to classify the identified literature using six different themes, as discussed in Sect. 2. These manual selections could be biased owing to the judgments of the authors involved in the data filtering and classification processes. Development of an objective method of review process is a future issue.

Besides, to identify the relevant studies, only Scopus and ScienceDirect were used as the search engines. Therefore, all relevant studies may not be covered. Not only these search engines, but also other search engines should be used to cover all relevant studies.

## 4 Conclusion

In this study, to investigate effective methods for MASS risk analysis, we conducted a systematic review of existing papers on MASS risk analysis published since 2018. A systematic literature review of the available academic research studies on MASS risk analysis has not been previously conducted; therefore, this study employed principles from the Preferred Reporting Items for Systematic Reviews and Meta-analysis (PRISMA) for conducting a systematic literature review on MASS risk analysis. In addition, to conduct the review considering various aspects of risk analysis, we developed the classification framework of risk analysis of MASS and conducted the review utilizing the developed framework. The developed classification framework covered more aspects of risk analysis of MASS compared with the existing review articles on risk analysis of MASS which classified scientific literature according to only risk analysis tools. Thus, this paper reveals the holistic issues and future perspectives on application of risk analysis of MASS.

We concluded that a qualitative analysis using STAMP/ STPA and a quantitative analysis through BN using the STAMP/STPA results are effective. Since a few studies have conducted a risk analysis of MASS target accidents other than collision, further risk analyses of MASS using these methods will be necessary. In addition, research on the risk analysis of MASS considering the level of automation and the quantitative risk analysis of MASS for determining ship insurance premiums should be conducted using these methods to improve the practical application of MASS.

## Appendix

See Table 2, 3

Table 2 Comparison of the previous and current targeted papers
![img-9.jpeg](img-9.jpeg)

Table 2 (continued)
![img-10.jpeg](img-10.jpeg)

Table 2 (continued)
![img-11.jpeg](img-11.jpeg)

Table 2 (continued)
![img-12.jpeg](img-12.jpeg)

Table 3 Dataset of the reviewed papers in this study


Data availability The data that support the findings of this study are available from the corresponding author, upon reasonable request.Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
