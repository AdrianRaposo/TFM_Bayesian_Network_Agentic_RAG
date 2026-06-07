# A Fuzzy Bayesian Network approach for Risk Analysis in Process Industries 

Mohammad Yazdi ${ }^{\mathrm{a}}$, Sohag Kabir ${ }^{\mathrm{b}, *}$<br>${ }^{a}$ Department of Industrial Engineering, Eastern Mediterranean University, Mersin 10, Turkey<br>${ }^{\mathrm{b}}$ School of Engineering and Computer Science, University of Hull, Hull, HU6 7RX, UK


#### Abstract

Fault tree analysis is a widely used method of risk assessment in process industries. However, the classical fault tree approach has its own limitations such as the inability to deal with uncertain failure data and to consider statistical dependence among the failure events. In this paper, we propose a comprehensive framework for the risk assessment in process industries under the conditions of uncertainty and statistical dependency of events. The proposed approach makes the use of expert knowledge and fuzzy set theory for handling the uncertainty in the failure data and employs the Bayesian Network modeling for capturing dependency among the events and for a robust probabilistic reasoning in the conditions of uncertainty. The effectiveness of the approach was demonstrated by performing risk assessment in an ethylene transportation line unit in an ethylene oxide (EO) production plant.


## Key words

Hazard Analysis, Fault tree analysis, Bayesian Networks, Fuzzy Set Theory, Process Industry

## 1. Introduction

In recent years, complex chemical plants have been rapidly developed to meet the increasing demand of process industries. As these plants usually process hazardous materials, their failure can cause serious harm both to people and the environment. For this reason, it is necessary to identify potential risks posed by such systems and then take measures to minimize the likelihood of these risks. To deal with the large number of accidents, incidents, near misses, and mishaps in process industries, different risk assessment approaches have been developed and widely used to perform a hazard analysis, thus enabling the prevention of an inadvertent incident and planning of mitigative actions (Khakzad et al., 2013a, 2011; Yan et al., 2016).

The risk assessment techniques deployed for identifying and controlling the risks in hazardous industries might appear satisfactory to their users; however, in a real life scenario, there have been many cases of disastrous accidents due to the failure of such preventive measure, such as deepwater horizon explosion and oil spill in 2010, Fukushima disaster in 2011, storage tank explosion at loading port in Tianjin in 2015, the explosion of a natural gas (NG) factory in Belgium in 2004, and conflagration caused by NG leakage in Paraguay in 2004, etc. (Escande et al., 2016; Han and Weng, 2011; Khakzad, 2015; Taveau, 2010). The approaches used for hazard analysis in process industries include, but are not limited to, Hazard and Operability Analysis (HAZOP) (Dunjó et al., 2010), Fault Tree Analysis (FTA) (Vesely et al., 2002), and Bow-tie diagrams (De Dianous and Fiévez, 2006). FTA is the most popular among all available techniques and it has been extensively used for risk analysis in several industries (Kabir, 2017; Khan et al., 2008; Wang et al., 2002).

A fault tree (FT) can be analyzed both qualitatively and quantitatively. A qualitative analysis minimizes a fault tree to a set of minimal cut sets (MCSs), which are the smallest combinations of events that are necessary and sufficient to cause the top event (TE), i.e., a hazardous event. A quantitative analysis mathematically calculates the occurrence

[^0]
[^0]:    * Corresponding author. Email: mohammad.yazdi@cc.emu.edu.tr (Mohammad Yazdi), s.kabir@hull.ac.uk (Sohag Kabir)

probability of the top event and other relevant numerical indexes, given the failure rate/probability of an individual element of a system. For this reason, the applicability of FTA for quantitative analysis largely depends on the availability of failure data. However, for most of the large and complex systems, it is often very difficult to obtain precise failure data due to the lack of knowledge, scarcity of statistical data, ambiguous component behavior, and the operating environment of the system (Huang et al., 2004; Kabir et al., 2016; Omidvari et al., 2014). In such cases, FTA cannot be used for risk assessment due to the lack of failure data. In addition to that, during the quantitative analysis, different events (e.g. intermediate events representing MCSs) in the fault tree are generally considered to be statistically independent. However, in real life systems, the events are not always statistically independent. For example, two MCSs may become statistically dependent because of sharing of a common basic event. For this reason, the statistical independence assumption about the events could lead to an inappropriate estimation of system dependability.

In order to deal with the ambiguities and shortages of data in conventional FTA, extensive studies have been performed by employing fuzzy set theory in different areas. In recent years, Celik et al. (2010) and Lavasani et al. (2015a, 2015b, 2011) have used the triangular and trapezoidal fuzzy numbers to compute the failure probability (FP) of the top event (TE) with respect to an expert judgment in different chemical industries. Fuzzy FTA was applied for the reliability analysis of fire and explosion of a crude oil tank by Wang et al.(2013). Furthermore, Yazdi et al. (2017) utilized the similarity aggregation method (SAM) in terms of fuzzy set theory to compute the failure probability of a granule storage tank. Ferdous et al. ( 2009) used a computer aided fuzzy fault tree analysis for the same purpose. However, their model cannot cope with the dependency and redundant events in a realistic system. A potential remedy to this problem is to translate a static fuzzy fault tree to a different model, which is capable of capturing dependency among events and can also model scenarios with redundant events.

Bayesian network (BN) is a well-known graphical inference method which expresses the causal relationships between the causes and final outcomes in a system (Rausand, 2011). In addition, BN has also been widely used in various engineering applications such as risk and reliability assessment (Abimbola et al., 2015; Bouejla et al., 2014; Hänninen et al., 2014; Huang et al., 2006; Khakzad et al., 2013a, Yuan et al., 2015), improving the safety performance of a system ( Herrero et al., 2013; John et al., 2016; Trucco et al., 2008), updating failure probability (Leu and Chang, 2013; Musharraf et al., 2016; Wu et al., 2015), and mapping static or dynamic FTs into corresponding BNs (Barua et al., 2016; Hänninen et al., 2014; Kabir et al., 2014; Khakzad et al., 2013a, 2013b; Marvin et al., 2017; Pereira et al., 2016; Yeo et al., 2016; Zarei et al., 2017). In a BN model, both forward and backward analysis could be performed. A forward analysis is performed to estimate the probability of unknown variables by following the arcs of the network. On the other hand, the backward analysis is performed by following the network arcs in opposite direction to update the probability of known variables based on some evidence.

The objective of this study was to find a new approach for performing risk analysis in a more consistent way under the condition of uncertainty. In the proposed approach, a fault tree is used for qualitative analysis to identify the root causes of the hazardous event and the fuzzy set theory, along with expert judgment, is used to obtain the unknown failure data of basic events of the FT. The probability of the occurrence of the hazardous events and other related reliability indexes are calculated by translating the fault tree into a Bayesian network. The proposed methodology was applied for risk analysis of ethylene transportation line. The results obtained by the proposed approach are also compared with those obtained by the classical fuzzy fault tree approach. This approach offers an improved quantitative analysis of complex systems by eliminating the assumption of statistical independence among the events. Moreover, unlike the traditional approaches, the proposed one can be used for diagnostic analysis of systems, which is particularly important to determine maintenance strategies.

This paper is organized as follows. In Section 2, a new approach based on the fuzzy theory and Bayesian modeling is introduced that computes the failure probability of TE. A numerical example is presented in Section 3 to

exemplify the feasibility and effectiveness of the proposed model. Finally, the conclusion and future remarks are described in Section 4.

# 2. Material and Methodology 

FT is a well-known method which is widely used in failure analysis (Yuan et al., 2015). It is a deductive methodology that represents the interrelationship between basic events (BEs) and the root cause in a complex system. These interrelationships are typically obtainable as logical AND/OR gates (Bobbio et al., 2001; Rausand, 2011). In order to find the probability of TE in a specific case, the failure rates of BEs are taken from standard reliability data sources such as OREDA (2002). However, as mentioned earlier, there some limitations, which might occur during the analysis, such as the lack of data for BEs or analyzing the dynamic system, which conventional FTA is not capable of. This section, to deal with these limitations, provides a new approach. A graphical overview of the approach is shown in Fig. 1. Hazard analysis, FT construction and data collection, Bayesian modeling, and the calculation are the four key stages in the proposed method, which are presented in details as follows.

### 2.1. Hazard analysis

In the recent decade, several methods have been developed for hazard analysis, e.g., HAZOP and FMEA (Khakzad et al., 2011). In this regard, all possibilities of failures need to be considered. Therefore, understanding the process thoroughly is the vital step. After completing the collection of information process, the identification of all hazards and menaces for any hazardous events that may cause damage to the equipment or harm to people and/or environment needs to be taken into consideration (Rausand and Hoyland, 2004). Among all the mentioned analysis techniques based on brainstorming methods, the critical and hazardous system and sub-system can be figured out by employing a group of experts for further studies, such as causal and frequency analysis. In this study, the output of HAZOP is selected as a worst-case event.

### 2.2. Fault tree construction and data collection

The construction of an FT always starts with a specified TE placed at the top of the tree and the rest of the tree is constructed in the downward direction. The TE usually indicates an accident that can cause asset loss or safety hazards (Lewis, 1996). In order to complete a tree, the BEs that are denoted as the lowest level (leaves) of the tree should be known beforehand. In an FT, BEs are usually considered statistically independent and could be in any of the two binary states (failed and non-failed).

As mentioned earlier, the exponentially distributed failure rate of known BEs can be obtained from OREDA (2002) and subsequently is transferred to failure probability by Equation (1).

$$
P(t)=1-e^{-\lambda t}
$$

where $P$ denotes the probability of failure, $\lambda$ represents failure rate (the number of failures per year), and $t$ is the time inspection interval.

On the other hand, the three methods-extrapolation, statistical, and expert judgment-can be employed to estimate the probability of BEs with unknown or limited failure data (Preyssl, 1995). The extrapolation technique is based on an estimation approach, which is applied on a standard reliability data source, while the statistical technique implies the examination of data in a direct way to compute the probability of an event. Besides, the expert judgment method can be engaged to estimate the probabilities with respect to experts' opinions.

![img-0.jpeg](img-0.jpeg)

Fig. 1. The framework of the proposed method
In this study, the expert judgment method as a scientific consensus approach is employed to compute the probability of unknown BEs. Therefore, an integration of fuzzy set theory and subjective opinions to overcome any possible ambiguity can help the assessors (Yazdi et al., 2017a).

The following section introduces a way showing how experts can be employed and weighted to obtain the failure data.

# 2.3. Using expert judgment (Fuzzy AHP) 

Fuzzy set theory has been used in several studies to aggregate the expert opinions to overcome the possible ambiguities in failure data. The main aspect of the fuzzy set theory is how to quantify the qualitative index. The subjectivity should be avoided in order to get more credible and reliable results. A simple averaging method, regarding some criteria including personal experience, job tenure, and education level, has mostly applied in the literature for expert weighting. This approach does not provide sufficiently high objectivity (Lavasani et al., 2015a, 2015b; Miri Lavasani et al., 2011; Ramzali et al., 2015; Yan et al., 2016; Yazdi et al., 2017b). Therefore, an extension of fuzzy analytical hierarchy process (FAHP) can overcome subjectivity issues.

Conventional AHP is a well-known method, which is commonly used in multi-criteria decision-making problems. In this case, as conventional AHP method cannot deal with subjective knowledge, FAHP has been developed to solve the AHP problems (Gul and Guneri, 2016). In other words, the main purpose of AHP is collecting expert opinions, though conventional AHP cannot reflect the human thinking. Several FAHP techniques have been proposed in the last few decades. Of them, the two most important were introduced by Buckley (1985) and Chang (1996), which used trapezoidal and triangular fuzzy membership function for a pairwise comparison scale, respectively.

In this study, an extension of Buckley's method was used for weighting the experts, due to the limitations in other techniques, such as all fuzzy comparison matrices cannot be completely used. Besides, in Buckley's method, illogical zero weight may also be obtained for the selection criteria (Chan and Wang, 2013).

The weight of each expert can be computed in a more reliable way on the basis of their knowledge and experience. Therefore, the computed weights are vital in order to represent the relative superiority of the employed experts. The next section introduces an approach based on the fuzzy theory to transform the linguistic possibilities of expert opinions into a fuzzy probability to aggregate their opinions into a crisp probability value (Altunkaynak et al., 2005; Duan et al., 2016; Mohsendokht, 2017; Shi et al., 2014).

### 2.4. Aggregation procedure

The aggregation procedure of expert judgment in the fuzzy logic system is divided into three stages as below.
Stage 1: Obtaining linguistic terms of unknown BEs based on expert judgment
Stage 2: Converting linguistic terms into corresponding fuzzy numbers
Stage 3: Converting fuzzy numbers into fuzzy possibility scores (FPS)
Further details of the mentioned stages are explained below.

### 2.4.1. Obtaining linguistic terms of unknown BEs based on expert judgment (stage 1)

The purpose of stage 1 was determining the failure likelihood of BEs considering the linguistic terms expressed by the experts. Several experts were consulted for this purpose and were furnished with a questionnaire by email to provide their judgment about the failure possibility of basic events. The linguistic terms, representing the probability of BEs, were scaled at seven levels: very high (VH), high (H), fairly high (FH), medium (M), fairly low (FL), low (L), and very low (VL). These levels were based on Saaty's approach (Saaty and Ozdemir, 2003), who discussed that the proper number for expert judgment at a specified time is between five and nine or in the other words the common capacity of human judgment is seven plus/minus two chunks.

# 2.4.2. Converting linguistic terms into corresponding fuzzy numbers (stage 2) 

There are many applications of fuzzy set theory to deal with uncertainties and inaccuracy in expert judgments in linguistic terms such as triangular, trapezoidal, intuitionistic, and Gaussian fuzzy membership function (Atanassov, 2012; Purba et al., 2014). The guarantee of the best membership function is based on realistic circumstances (Markowski and Mannan, 2008). In earlier studies, triangular and trapezoidal fuzzy numbers have been found to be effective for risk assessment purpose (Ferdous et al., 2013; Lavasani et al., 2015a, 2015b; Mardani et al., 2015; Ramzali et al., 2015; Yazdi, 2017). Therefore, both triangular and trapezoidal fuzzy numbers were utilized to map linguistic opinions to fuzzy membership function. The reason of using these two types of fuzzy numbers is that under some weak assumptions, the defined membership functions can directly meet the appropriate optimization criteria (Pedrycz, 1994).
![img-1.jpeg](img-1.jpeg)

Fig. 2. Fuzzy membership functions
In this way, a corresponding fuzzy number for each linguistic term could be obtained. Further, it is necessary to aggregate subjective opinions of experts regarding identified BEs into a single opinion. Various techniques are available in the literature to aggregate experts' opinions such as linear opinion pool, max-min Delphi, sum-product, max-product, and similarity aggregation (Aqlan and Mustafa Ali, 2014; Ishikawa et al., 1993; Ross, 2009). However, Liu et al.(2014) discussed that there is no way to show which method has superiority to the other one.

The sum-production algorithm, which is used in this study for the aggregation process could be presented as follows.

$$
Z_{i}=\sum_{j=1}^{n} w_{j} \cdot f_{i j}, i=1,2, \ldots, m \quad j=1,2, \ldots, n
$$

where $Z_{i}$ denotes the aggregated fuzzy number for $\mathrm{BE}_{i}, w_{j}$ represents the weight of experts $j$, and $f_{i j}$ is corresponding fuzzy number of $\mathrm{BE}_{i}$ given by expert $j . n$ and $m$ are the number of experts and BEs respectively. The $\alpha$-cut is a commonly used method to operate the fuzzy membership function (Lowen, 1996; Mesiar, 2007; Ross, 2009; Zhang et al., 2017).

### 2.4.3. Converting fuzzy numbers into fuzzy possibility scores (FPS) (stage 3)

FPS denotes a crisp value that is based on experts' opinions aggregated for a possible event. In order to defuzzify a quantifiable outcome in the fuzzy set theory, several common techniques are available including the center of area (CoA), the center of the largest area, max-min, bisector, weighted average, mean max, and the center of sum (Akkurt et al., 2004; Ross, 2009). In this study, the max-min aggregation methods, proposed by Chen and Hwang

(1992), was used for defuzzification process (Shi et al., 2014).The maximum and minimum fuzzy sets are expressed as follows.

$$
\begin{aligned}
& f_{\max }(x)=\left\{\begin{array}{cc}
x, & (0 \leq x \leq 1) \\
0, & (\text { otherwise })
\end{array}\right. \\
& f_{\min }(x)=\left\{\begin{array}{cc}
1-x, & (0 \leq x \leq 1) \\
0, & (\text { otherwise })
\end{array}\right.
\end{aligned}
$$

Subsequently, the right and left score of fuzzy set (Z) can be computed as follows, respectively.

$$
\begin{aligned}
& F P S_{\text {Right }}(Z)={ }_{\bar{z}}^{s u p}\left[f_{\bar{z}}(x) \wedge f_{\max }(x)\right]=(1-d) /[1+(d-c)] \\
& F P S_{\text {Left }}(Z)={ }_{\bar{z}}^{s u p}\left[f_{\bar{z}}(x) \wedge f_{\min }(x)\right]=(1-a) /[1+(b-a)]
\end{aligned}
$$

In addition, the relationship between left and right side of fuzzy set (Z) is illustrated in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Fig. 3.The schematic computation of right and left FPS
Therefore, the fuzzy possibility scores of fuzzy number $Z_{i}$ can be obtained by the following equation.

$$
F P S\left(Z_{i}\right)=\left[F P S_{\text {Right }}\left(Z_{i}\right)+1-F P S_{\text {Left }}\left(Z_{i}\right)\right] / 2
$$

Thus the aggregated FPS with respect to experts' weight is computed for each BE. In the next section, the failure probability calculation process and mapping of FT into BN for executing further actions are explained.

# 2.5. Calculation and Bayesian Modeling 

### 2.5.1. The calculation of failure probability and TE probability

FPS are converted to failure probability by using following equation proposed by Onisawa (1990).
Failure probability $=\left\{\begin{array}{cc}1 / 10^{k} & F P S \neq 0 \\ 0 & F P S=0\end{array}\right.$

$k=2.301 \times[(1-F P S) / F P S]^{1 / 3}$
The process of transferring linguistic terms into failure probabilities considering $\alpha$-cut methods is completed at this point. Therefore, by following the above processes failure probability of all BEs can be computed. Moreover, using Boolean algebra and the failure probability of the BEs, the failure probability of TE can be computed (Banerjee, 2003). This process is known as the analytical method for quantifying FTs.

# 2.5.2. Bayesian Modeling 

### 2.5.2.1. Bayesian Network

Similar to FT, BN is a probabilistic graphical technique, which is widely used for constructing system reliability models based on uncertain knowledge (Khakzad et al., 2013, 2011; Zarei et al., 2017). BN results in a directed acyclic graph that includes the set of nodes denoting the variables, which are connected by directed arcs. The arcs represent the probabilistic causal relationship between the variables and Conditional Probability Tables (CPTs) are set to the nodes in order to represent the conditional dependencies.

According to conditional dependency of variables and chain rules, BN denoted the joint probability distribution of set of variables as follows (Jensen and Nielsen, 2007):

$$
P(U)=\prod_{i=1}^{n-1} P\left(X_{i} \mid X_{i+1}, \ldots X_{n}\right)
$$

Where $U=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ and $X_{i+1}$ is the parent of $X_{i}$. Accordingly, the probability of $X_{i}$ can be computed as:

$$
P\left(X_{i}\right)=\sum_{U \backslash X_{i}} P(U)
$$

The risk and reliability analysis is a well-known application of BN to update the prior failure probabilities of specified events, given the new information in the form of evidence. This information is usually based on expert knowledge or becomes available in the lifecycle of processes, such as accidents, incidents, near misses, mishaps, etc. Therefore, BN allows reaching a better analysis in a dependable situation of a complex system including common cause failure (CCF) and diagnostic reasoning (Bobbio et al., 2001).

Based on Bayes theorem, BN can be used to update the prior probability of an event (E):

$$
P(U \mid E)=\frac{P(U \cap E)}{P(E)}=\frac{P(U \cap E)}{\sum_{U} P(U \cap E)}
$$

In the case of FT, it can be shown as follows:

$$
P\left(B E_{k} \mid E_{i n_{j, k}}\right)=\frac{P\left(B E_{k} \cap E_{i n_{j, k}}\right)}{P\left(E_{i n_{j, k}}\right)}=\frac{P\left(E_{i n_{j, k}} \mid B E_{k}\right) \cdot P\left(B E_{k}\right)}{P\left(E_{i n_{j, k}}\right)}
$$

where

- $E_{i n_{j, k}}$ represents the $j^{\text {th }}$ state of "given new information" denoting the effect of new events on $B E_{k}$. Besides, $P\left(B E_{k} \mid E_{i n_{j, k}}\right)$ is the posterior failure probability of $B E_{k}$ given $E_{i n_{j, k}}$;
- $P\left(B E_{k}\right)$ is the prior failure probability of $B E_{k}$ provided by expert judgment or standard reliability sources;
- $P\left(E_{i n_{j, k}}\right)$ is the probability of state $j$ of the $k$ "given new information" which is estimated from the BN

- $P\left(E_{i n_{j, k}} \mid B E_{k}\right)$ is denoted as degree of belief in the failure of $E_{i n_{j, k}}$ given the failure of $B E_{k}$. The value of $P\left(E_{i n_{j, k}} \mid B E_{k}\right)$ can be found out by asking question from experts.


# 2.5.2.2. Mapping procedure 

The mapping of FT into BN is based on graphical and numerical functions (Bobbio et al., 2001). In graphical mapping, top event, intermediate events, and basic events of FT are denoted as leaf nodes, intermediate nodes, and root nodes in an equivalent BN, respectively. In an FT, the top event and the intermediate events are always represented as logic gates. For this reason, to be able to distinguish the nodes representing the basic events from the nodes representing the logic gates in a BN, we used single circles to represent the basic event nodes and double circles to represent the top and intermediate event nodes. In numerical mapping, the failure probabilities of BEs are given to the related nodes as prior failure probabilities. CPTs can be generated for all intermediate nodes based on the logic gates they represent ( see details in Bobbio et al. (2001)). Fig. 4 shows the simplified procedure of mapping of FTs into BNs presented by Khakzad et al. (2011).
![img-3.jpeg](img-3.jpeg)

Fig. 4. Mapping of FT to BN

### 2.5.3. Importance measures and Critical nodes

In FTA, there are many importance measures available to measure the relative importance of each BE or MCS in terms of their impact on the occurrence of the top event (Modarres, 2006; Rausand, 2014). In parallel way, according to Bayesian theorem, the importance measures can be represented in the new approach and computed by their logical relationships in BN (Van Der Borst and Schoonakker, 2001).

Birnbaum Measure (BM): BM of an event is obtained by taking the difference between the probability of the top event by setting the event probability to 1 and 0 , respectively.

In BN model, BM can be obtained as:

$$
I_{B E_{i}}^{B M}=P\left(T E \mid B E_{i}=1\right)-P\left(T E \mid B E_{i}=0\right)
$$

Where $P\left(T E \mid B E_{i}=1\right)$ and $P\left(T E \mid B E_{i}=0\right)$ denoted the conditional probability of the TE for occurrence and nonoccurrence of $B E_{i}$, respectively.

Risk Reduction worth (RRW): RRW shows the effect of BE on TE with respect to non-occurrence of $B E_{i}$. RRW represents the decrease of TE probability when a given BE is assured not to occur. It can be calculated from the BN as:

$$
I_{B E_{i}}^{R R W}=P(T E)-P\left(T E \mid B E_{i}=0\right)
$$

The criticality of the nodes can be obtained by computing above mentioned importance measures. The rank of critical nodes is obtained as follows.

$$
R^{*}=\frac{I_{\mathrm{m}}}{\sum_{i=1}^{n} I_{\mathrm{m}}} \times 100
$$

where, $I_{\mathrm{m}}$ is the $\mathrm{m}^{\text {th }}$ importance measures and $n$ is the number of BE or MCS. $R^{*}$ denotes the normalized weight of importance measures.

The total weighing of importance measures can be computed as follows:

$$
R_{T o t a l}^{*}=R_{B M}^{*}+R_{R R W}^{*}
$$

Finally, the BEs is ranked in ascending order from most critical to the least critical BEs.

# 3. Application of the proposed methodology 

The proposed methodology was applied to an ethylene oxide (EO) plant for an ethylene transportation line unit. A risk assessment study was conducted by Khan et al. (2002) for an EO production plant. In the study, most hazardous units, such as the EO storage unit, reaction unit, ethylene EO distillation column, ethylene transportation line, and ethylene reboiler, were recognized. It was suggested that further details of risk assessment are required for the mentioned units. In addition, ethylene transportation line unit was identified as the third major hazard in the present units. Moreover, the most probable accident scenario that can be expected in this case is the ethylene release due to a leak or rupture, causing a vaporized cloud to be formed and reaching to an ignition source resulting in fire and explosion. To find an optimal maintenance strategy, another study was performed on the above case study in (Khan and Haddara, 2004) based on risk-based maintenance (RBM) method (Khan and Haddara, 2003). RBM methodology combines several pre-existing methods and tools such as MCAS (Khan, 2001), MAXCRED (Khan and Abbasi, 1999a), PROFAT (Khan and Abbasi, 1999b) and PROFAT II (Khan and Abbasi, 2000) to efficiently reach a maintenance decision.

### 3.1. Overview of the Process

EO is produced by the oxidation of ethylene and pure oxygen. The completed process flow diagram (PFD) of EO plant is illustrated in Fig.5. Ethylene and oxygen are reacted at 10-30 bar and 150-260` C in a fix bed catalysis reactor and has been transported from the storage tanks to isolated vicinity to the reaction unit through pipeline (see Khan et al. (2002) for more details).

### 3.2. Probabilistic Risk Assessment

### 3.2.1. FT Development

The TE of the FT was selected as an ignition of vapor cloud which may lead to a fireball. The developed FT is illustrated in Fig. 6. The identified 25 basic events, which contribute directly and/or indirectly to the specified TE, are shown in Table 1. As mentioned earlier, the BEs with known failure rates are separated from the ambiguous ones. The failure rates of some BEs are determined by employing OREDA (2002) and the failure rates of the ambiguous ones are estimated based on the expert judgment. As shown in Table 1, failure rate data for 9 BEs were obtained from the reliability database, whereas the failure rates could not be identified for 16 BEs from the available data.

![img-4.jpeg](img-4.jpeg)

Fig. 5. Process flow diagram of the EO plant
![img-5.jpeg](img-5.jpeg)

Fig. 6. Fault tree for the ethylene transportation line (modified after Khan and Haddara(2004))

# 3.2.2. Obtaining Failure Rates of BEs 

As mentioned earlier, to perform a proper risk analysis, it is necessary to access the historical failure rate data to allocate them to BEs. Thus, the probability of hazards with identified failure rate can be computed. The failure probability of the BEs with known failure rates were computed on per year basis ( 8760 h ) and are presented in Table 2 .

The process of obtaining the failure probability of the basic events with unknown data is described in the following subsections.

Table 1. Details of the BEs of FT of Fig. 6 (modified after Khan and Haddara (2004))


Table 2. Failure probability of basic events with known failure rates


# 3.2.3. Rating stage 

As mentioned above, to compute the FP of ambiguous BEs, an expert judgment is employed. The expert knowledge is biased by individual visions and purposes (Ford and Sterman, 1998); thus, it is very difficult to obtain an impartial expert opinion. The main point here is the selection of both heterogeneous specialists (e.g., workers and experts) and homogenous specialists (in this case it includes only experts).

It has been suggested that the impact of individual experience is smaller in a homogenous group compared to a heterogeneous group as a result of differences in the experience. Therefore, the main advantage of a heterogeneous group compared to the homogenous group is that all possible opinions of heterogeneous specialists can be considered. Thus, in this study, a heterogeneous group of experts including four specialists with different backgrounds was employed to compute the FP of the 16 ambiguous BEs.

Expert No. 1: An experienced safety auditor and risk assessor working as consultant for complex chemical plant. Expert No. 2: An experienced technician working in different kinds of process industry.
Expert No. 3: A senior chemical process designer from process engineering department with master certificate.
Expert No. 4: An experienced safety officer working in a complex process plant with safety engineering certificate.

Fuzzy AHP method was used to compute each expert's capability and assigning the respective weights. The system of expert information is illustrated in Fig. 7, and the expert profile and weights are shown in Table 3.
![img-6.jpeg](img-6.jpeg)

Fig. 7. Fuzzy AHP index system of respective expert capabilities

Table 3. Experts' profile and related decision weights


Let's take, as an example, that BE23 valve fails to open. With respect to the definition of fuzzy numbers presented in Fig. 2, the qualitative terms, given by four experts, fall into "VL", "FL", "FL", and "FH" categories. The integrated fuzzy number is attained as follows:
$f(x)=w_{E 1} \times f_{V L}(x)+\left(w_{E 2}+w_{E 3}\right) \times f_{F L}(x)+w_{E 4} \times f_{F H}(x)$
The membership function of aggregated fuzzy number can be obtained as:
$f(x)=\left\{\begin{array}{cc}\frac{x+0.128}{0.16}, & 0.188<x \leq 0.288 \\ 1, & 0.288<x \leq 0.363 \\ -x+0.463 & 0.363<x \leq 0.463 \\ 0.1 & \text { otherwise }\end{array}\right.$
The right and left utility scores of fuzzy number $\mathrm{f}(\mathrm{x})$ are computed using equations (5)-(7) and provided as follows:
$F P S_{\text {Left }}(x)=0.738$
$F P S_{\text {Right }}(x)=0.488$
$F P S\left(x_{i}\right)=0.375$
Using equations (8) and (9), the FP of BE23 is computed to be 0.001874 .
The qualitative terms based on experts' opinions and FP of unknown BEs are shown in Table 4.

# 3.2.4 Bayesian Modeling and Analysis 

Once the data for all basic events are obtained, the fault tree (Fig. 6) is mapped to a Bayesian Network (Fig. 8). The prior probability values of the root nodes of the BN are defined based on the values shown in Tables 2 and 4. The conditional probability values of each intermediate node of the BN are populated based on the type of logic gate it represents.

In this BN, G1 is the node corresponds to the TE of the FT. Now running a query on this node would return the value of system unreliability. The value of system unreliability for the system obtained from the BN model is $3.623 \mathrm{E}-09$. The system unreliability was also calculated using the analytical approach and the value obtained was $3.713 \mathrm{E}-09$. This value is $2.48 \%$ higher than the value estimated by the BN based approach. This is due to the fact that the analytical approach does not consider the statistical dependence among the events. However, it can be seen from the BN model that some events are statistically dependent on each other. For example, the events represented by nodes G4 and G5 are statistically dependent on each other as they share a common basic event BE1. For a similar reason, nodes G9 and G15, and G17 and G18 are also statistically dependent. The effect of these dependences also propagates through the network to the node representing the TE.

Table 4. Experts' opinions, corresponding fuzzy number and corresponding failure probabilities of BEs


![img-7.jpeg](img-7.jpeg)

Fig. 8. Bayesian Network of the fault tree in Fig. 6

One important aspect of probabilistic risk assessment of a system is to determine the critical components based on their contribution to the occurrence of the system failure. This information can help in improving the system reliability by taking the necessary measures such as by putting more design efforts on the weakest part of the system or by improving the system design by introducing fault tolerant strategies. The criticality of the basic events of the FT in Fig. 6 is calculated following the procedure described in section 2.5.3 using both the analytical and the BNbased approaches. The results of the evaluation are shown in Table 5. According to the results shown in Table 5, BE6 (Ignition source present) contributes the most to the top event probability, hence, ranked as the most critical component. The second most critical event is BE1 (Flammable gas detector fails). If we compare the ranking of the events, we can see that both BN-based and the analytical approaches agree on the ranking of most of the components. However, there are some disagreements between the two approaches regarding the ranking of events. For example, the BN-based approach ranked BE14 as the least critical event and BE16 as the second least critical, whereas the analytical approach ranked them in opposite order. We believe that these disagreements are due to the statistical independence assumption of the events in the analytical approach.

Table 5. Importance measures of the basic events based on the proposed approach and the analytical approach


We used the predictive reasoning on the BN model to obtain the system unreliability by following the directions of the network arcs. For predictive analysis, we used the information (failure probability) about the causes (component failure) to obtain the new belief (unreliability value) about the effect (system failure). With the help of an evidencebased analysis, we can also perform a diagnostic analysis for the BN, i.e., reasoning from symptoms to causes. For instance, when an analyst observes that the system has failed, depending on this observation, his/her belief regarding the failure probability of the basic events can be updated. This means a posterior probability distribution for the components can be obtained given the status of the system. The posterior probability values for the root nodes of the BN (Fig. 8) are obtained by providing the evidence that the top event has occurred (i.e., observing the BN node G1 to be true). The point to be noted is that this reasoning is performed backwardly, i.e., opposite to the direction of the arcs. Now, if we perform a predictive analysis based on this updated belief about the probability distribution of the basic events, then the value of system unreliability will also be updated. For this case study, the updated value of the system unreliability is 0.5407 , previously it was $3.623 \mathrm{E}-09$.

# 4. Conclusion 

In this paper, we proposed a comprehensive framework to combine fuzzy set theory and expert knowledge with FTA through Bayesian Network modeling to enable risk assessment of complex systems with ambiguous failure data. The proposed method addresses three important issues in probabilistic risk assessments, namely, the challenges of unavailability of failure data, the dependency of failure events, and the uncertainty. The use of expert elicitation and fuzzy set theory allows handling of the issue of insufficient failure data and also explicitly highlights the areas of uncertainty in the data. We used Bayesian Network for probabilistic reasoning to obtain system reliability related indexes and also to capture the dependencies among the events. The effectiveness of this approach was demonstrated by applying it to the risk assessment of an ethylene transportation line unit in an ethylene oxide (EO) plant and by comparing the results with the results obtained by the analytical approach. The proposed approach was found to be more robust and the results obtained were more accurate, as this approach does not estimate the system reliability under the unrealistic assumption of statistical independence of events.

In the present work, we consider the failure rate of basic events as exponentially distributed. In future, we have a plan to extend this work by considering non-exponentially distributed failure data and the dynamic behavior of systems.
