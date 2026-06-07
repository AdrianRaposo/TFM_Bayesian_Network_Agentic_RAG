# Fuzzy Bayesian Network-Bow-Tie Analysis of Gas Leakage during Biomass Gasification 

Fang Yan, Kaili Xu*, Xiwen Yao, Yang Li<br>School of Resources and Civil engineering, Northeastern University, Shenyang, Liaoning, P. R. China<br>* kaili_xu_neu@126.com

## Abstract

Biomass gasification technology has been rapidly developed recently. But fire and poisoning accidents caused by gas leakage restrict the development and promotion of biomass gasification. Therefore, probabilistic safety assessment (PSA) is necessary for biomass gasification system. Subsequently, Bayesian network-bow-tie (BN-bow-tie) analysis was proposed by mapping bow-tie analysis into Bayesian network (BN). Causes of gas leakage and the accidents triggered by gas leakage can be obtained by bow-tie analysis, and BN was used to confirm the critical nodes of accidents by introducing corresponding three importance measures. Meanwhile, certain occurrence probability of failure was needed in PSA. In view of the insufficient failure data of biomass gasification, the occurrence probability of failure which cannot be obtained from standard reliability data sources was confirmed by fuzzy methods based on expert judgment. An improved approach considered expert weighting to aggregate fuzzy numbers included triangular and trapezoidal numbers was proposed, and the occurrence probability of failure was obtained. Finally, safety measures were indicated based on the obtained critical nodes. The theoretical occurrence probabilities in one year of gas leakage and the accidents caused by it were reduced to $1 / 10.3$ of the original values by these safety measures.

## 6 OPEN ACCESS

Citation: Yan F, Xu K, Yao X, Li Y (2016) Fuzzy Bayesian Network-Bow-Tie Analysis of Gas Leakage during Biomass Gasification. PLoS ONE 11(7): e0160045. doi:10.1371/journal.pone. 0160045

Editor: Yong Deng, Southwest University, CHINA
Received: April 15, 2016
Accepted: July 11, 2016
Published: July 27, 2016
Copyright: © 2016 Yan et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: Data are available from the Offshore Reliability Data Handbook. 4th ed. whose authors may be contacted at oreda@sintef.no.

Funding: The authors have no support or funding to report.

Competing Interests: The authors have declared that no competing interests exist.

## Introduction

Biomass has been rapidly developed as a renewable energy source in recent years [1], and it has tremendous potential in solving future shortage of energy [2]. In China, the capacity of biomass energy increased from 2.2 GW [3] to 3 GW [4] between 2004 and 2015. Biomass energy usage is increasing in other countries as well [5-7]. As one of the most widely available energy sources [8], conversion of biomass resource includes biodiesel, biomass to liquid (BTL), biomass gasification, etc [9,10]. Recently, biomass gasification stations have been constructed and put into operation massively in rural areas of China. They are used to reduce the burning of crop straw, which causes air pollution [11]. And more importantly, agriculture wastes can be made into green energy via biomass gasification. However, hydrogen $\left(\mathrm{H}_{2}\right)$, carbon monoxide $(\mathrm{CO})$, and methane $\left(\mathrm{CH}_{4}\right)$ which are produced by biomass gasification are flammable and CO has high poisonousness [12]; leakage of biomass gasification gas will lead to accidental fires

and poisoning incidents [13,14]. Because the development and promotion of biomass gasification is restricted by their danger, therefore, PSA is necessary for biomass gasification system, and effective safety measures are needed to reduce the risks associated with gas leakage.

Biomass gasification system is complicated, various causes may lead to gas leakage, and gas leakage will cause multifarious consequences as well. Bow-tie analysis is a quantitative method which includes fault tree analysis (FTA) and event tree analysis (ETA, [15]). So the deduction and induction function of bow-tie analysis makes it possible to investigate the causes and consequences referred to gas leakage. As a concise and effective quantitative risk assessment (QRA) methodology, Paolo [16] applied bow-tie analysis to baseline risk assessment tool (BART), and they utilized bow-tie analysis for identification and assessment of any potential hazards and associated risks. Because bow-tie analysis can clearly display the links between causes, loss event (LE), conditional events (CE), and outcome events (OE), Chen [17] considered bow-tie analysis as an effective tool to identify environmental risk source. The application of bow-tie analysis is broad based on its characteristic. It can be applied in risk management of sea ports and offshore terminals [18], risk evaluation for natural gas industry [19], risk assessment of hexane distillation installation [20]. However, the focus of bow-tie analysis is displaying the whole scenario of accidents, identifying and assessing the potential causes and consequences. Causes which are more critical to the consequences based on the logical links and occurrence probabilities of themselves cannot be readily obtained by bow-tie analysis. Therefore, as a method widely used in PSA [21], bow-tie analysis can be mapped into BN to achieve the goal. Some research are involved in mapping bow-tie analysis into BN. Badreddine and Amor [22] took advantage of dynamic analysis function of BN to improve a bow-tie model. They constructed bow-tie diagrams in an automatic and dynamic way to implement the appropriate preventive and protective barriers in a dynamic system. Khakzad [23] made dynamic risk analysis of a physical reliability periodically updating system, the failure probabilities of safety barriers of bow-tie were periodically updated by using Bayesian theorem, and the probabilities of the consequences were estimated by the improved bow-tie analysis. They considered that the bow-tie's limitations resulting from its static constituents can be relaxed by mapping bow-tie analysis into BN [24]. Majeed [25] used bow-tie analysis and BN to confirm the critical elements of the well integrity model. In their study, the posterior probability was obtained by Bayesian theorem, then the critical elements were confirmed by the ratio of posterior probability to prior probability. All in all, bow-tie analysis mapping into BN can make dynamic risk analysis, and the critical elements of system can be confirmed by the calculation of posterior probability using Bayesian theorem. However, PSA importance measures can be introduced as well [26], because the conditional probability can be calculated by Bayesian theorem, BN can be fitted with these importance measures well, the importance measures can be computed accurately and easily. Thus the BN-bow-tie analysis is not only displaying the accidents scenarios of biomass gasification, but also making PSA to confirm the critical causes of accidents by adding the importance measures.

In order to make PSA of biomass gasification system, the reliability data is needed. Standard reliability data sources [27] can provide some common reliability data. Lopez [28] used the standard reliability data sources to confirm the probability of base event (BE) of FTA in liquefied natural gas (LNG) industry. Similarly, Khakzad [24] confirmed the failure probability in bow-tie analysis of a mixing tank system by referring to the standard reliability data sources. In addition, some reliability data cannot be obtained from currently available data. As fuzzy methods are widely used in risk analysis [29,30], fuzzy methods based on expert judgment can be the way to obtain reliability data [31,32]. However, fuzzy methods are practical and flexible in application for many fields. The fuzzy logic can be coupled with regression, nearest neighbor method, and artificial neural networks to construct a predictive model, and this model can be

utilized effectively to make predicting demand for natural gas and energy cost savings in public buildings [33]. In Rodger's study [34], the fuzzy logic can cooperate with BN to implement probabilistic estimation, meanwhile, the method proposed by Rodger used the fuzzy clustering to produce a funnel diagram to make a clear and systematic demonstration for the relevance in supply chain backorder aging, unfilled backorders, and customer wait time. Moreover, Rodger [35] made a comprehensive study of group decision making, weighted average, linguistic terms, and fuzzy logic, in their study, a fuzzy induced linguistic ordered weighted averaging approach which can provide further insight and linguistic simplicity for decision makers was proposed to evaluate the risk in the supply chain. The fuzzy numbers reflect the linguistic expression of expert judgments to estimate events, for instance, if the expert judgment of a failure is 'about very low', the triangular number is introduced to indicate the judgment, and the trapezoidal number can indicate the judgment 'about very low to low'. Then fuzzy numbers can be converted to fuzzy failure rate (FFR, [36,37]), and the occurrence probability of failure is obtained. Ferdous [38] used triangular numbers to define expert judgments in the confirmation of occurrence probability in bow-tie analysis. In a fuzzy Bayesian network, triangular numbers were employed by Li [39] in quantitative human reliability analysis (HRA) frameworks. Ramzali [40] used expert judgment to obtain the failure probability of safety barriers in offshore drilling system, in their study, fuzzy numbers were introduced to reflect expert judgments. Various aggregation methods of fuzzy numbers are available. Bardossy [41] proposed a simple and effective approach to aggregate fuzzy numbers when they include only triangular or trapezoidal numbers. Hsu and Chen [42] proposed similarity aggregation method (SAM), when the fuzzy numbers were all triangular numbers or trapezoidal numbers, SAM was utility in aggregating fuzzy numbers with considering expert weighting [40,43]. Lin and Wang (Lin and Wang 1997) proposed an approach to aggregate fuzzy numbers including both triangular and trapezoidal numbers. However, fuzzy numbers based on expert judgment may be triangular or trapezoidal numbers, and the character of experts will affect their judgments as well. Therefore, in this study, Lin and Wang's method [44] was improved, the improved method can aggregate fuzzy numbers including both triangular and trapezoidal numbers, and expert weighting was also considered simultaneously. So it will make the occurrence probability of failure to be more objective, and the PSA of biomass gasification system to be more reliable.

This study identified the biomass gasification system by bow-tie analysis, causes of gas leakage and consequences resulted in gas leakage were obtained. Meanwhile, failure data was partly obtained from standard reliability data sources. For the failure data was not available from the existing data, fuzzy method based on expert judgment was employed to obtain the failure data. The fuzzy numbers which reflected the linguistic expression of expert judgments included both triangular and trapezoidal numbers, and an improved method was proposed to obtain the fuzzy failure data with considering the expert weighting. Then bow-tie analysis was mapping into BN (BN-bow-tie) to make PSA, three importance measures were introduced, and the critical nodes to accidents were obtained by computing the importance measures. Finally, safety measures aiming at the critical nodes were proposed, and the reduction of occurrence probabilities of accidents was calculated.

## Methods

## Model

Bow-tie analysis was used to display the accidents scenarios of a system from an LE. Causes of LE can be found by FTA of bow-tie analysis; consequences that result in LE can be identified by ETA of bow-tie analysis. In this proposed approach, FTA and ETA of bow-tie were transformed into BN to make the BN-bow-tie analysis. Units that give rise to accidents are more

easily could be obtained. With this approach, the explicit occurrence probability of failure was needed. The occurrence probability of facilities failure was obtained from standard reliability data sources [27]. The occurrence probability of operational error cannot be confirmed from existing data. Then fuzzy methods based on expert judgment were used to achieve these occurrence probabilities. Subsequently, variable consequences were predicted by BN-bow-tie analysis. Finally, the critical nodes related to the consequences was obtained. Flowchart of the methodology was showed below (Fig 1).

# BN-bow-tie Analysis 

Bow-tie was combined with FTA and ETA, and FTA and ETA were converted to BN. The algorithm of the logical relationship was identical to FTA and ETA. FTA in bow-tie was used to calculate LE as well as top event (TE) occurrence probability. If the occurrence probability of the basic event (BE) was obtained, the occurrence probability of the TE was also obtained. When the logical relationship of events was AND-gate, all events occured, and the TE occured. Eq 1
![img-0.jpeg](img-0.jpeg)

Fig 1. Proposed methodology.
doi:10.1371/journal.pone.0160045.g001

was used to calculate TE occurrence probability.

$$
F_{T E}=\prod_{i=1}^{n} F_{B E_{i}}
$$

If the logical relationship of events was OR-gate, only one of these events, the TE, was occurrence. Eq 2 was used to calculate TE occurrence probability.

$$
F_{T E}=1-\prod_{i=1}^{n}\left(1-F_{B E_{i}}\right)
$$

The occurrence probability of TE of FTA was defined to be that of LE. Meanwhile, the occurrence probability of an initiating event (IE) of ETA was equal to that of LE. Eq 3 was used to calculate occurrence probability of OE in ETA.

$$
F_{O E_{i t}}=F_{I E} \cdot \prod_{i=1}^{n} P\left(E_{i}=0\right) \cdot \prod_{j=1}^{i} P\left(E_{j}=1\right)
$$

BN is an inference approach that was combined with graph theory and probability theory. BN analysis of BN was based on the Bayesian theorem (Eq 4).

$$
P(B \mid A)=\frac{P(A \mid B) \cdot P(B)}{P(A)}
$$

According to the Bayesian theorem, three importance measures were introduced in the new methodology. So that events can be evaluated by their logical relationship and their occurrence probability in BN. The three importance measures were described below [26].

Birnbaum measure (BM). BM measured increment of TE occurrence probability when BE occurred (Eq 5).

$$
I_{B E}^{B M}=P(T E \mid B E=1)-P(T E \mid B E=0)
$$

where $P(T E \mid B E=1)$ denoted the occurrence probability of TE when a BE occurred, $P(T E \mid B E=0)$ denoted the occurrence probability of TE when a BE didn't occur.

Risk achievement worth (RAW). RAW evaluated the influence of BE for TE when it was considered with the occurrence probability of BE. RAW was adjusted by the occurrence probability of TE and BE. In this article, Eq 6 was used to calculate RAW.

$$
I_{B E}^{R A W}=I_{B E}^{B M} \cdot \frac{P(B E)}{P(T E)}
$$

where $P(B E)$ denoted the occurrence probability of $\mathrm{BE}, P(T E)$ denoted the occurrence probability of TE under no conditions.

Fussel-Vesely (FV). FV was used to describe the BE contribution to the failure of the system (Eq 7).

$$
I_{B E}^{F V}=\frac{P(T E)-P(T E \mid B E=0)}{P(T E)}
$$

In the proposed methodology, the critical nodes which triggered accidents more easily were obtained by calculating these importance measures.

# Confirming Occurrence Probability by Fuzzy Methods 

In this approach, the occurrence probability of each BE was needed in BN-bow-tie analysis. BEs were divided into three classes: facilities failure, operational error and multiple failure, and multiple failure included facilities failure and operational error. The occurrence rate of facilities failure was obtained from standard reliability data resources, subsequently, occurrence rate was converted to occurrence probability by Eq 8. Because the occurrence probability of operational error and multiple failure could not be confirmed by existing data resources, the fuzzy methods based on expert judgment were used to estimate occurrence probabilities of operational error and multiple failure.

$$
F=1-e^{-\lambda t}
$$

where $F$ denoted the occurrence probability of failure, $\lambda$ denoted the occurrence rate of failure.
The fuzzy methods involved aggregating the different judgment of different experts, expert weighting was considered and triangular fuzzy numbers or trapezoidal fuzzy numbers proposed by experts were estimated to calculate FFR [44], and FFR was converted to the occurrence probability of operational error and multiple failure.

The following steps were used to confirm occurrence probability based on expert judgment.

1. Confirm the weighting of each expert. The weighting of each expert was partitioned by age, education background, years of service, and professional position (Table 1, [40,43]).

Eq 9 showed the calculation of the total weighting score of each expert, and the weighting of each expert was calculated by Eq 10.

$$
S_{i t}=S_{i t_{0}}+S_{i t_{0}}+S_{i t_{1}}+S_{i t_{d}}
$$

Table 1. Weighting Score of Different Expert Factors.


doi:10.1371/journal.pone.0160045.t001

where $S_{u}$ denoted the total weighting score of an expert.

$$
W_{u}=\frac{S_{u}}{\sum_{u=1}^{M} S_{u}}
$$

where $M$ denoted the number of experts.
2. Judgment of occurrence probabilities were classified as nonoccurrence, absolute low, very low, low, fairly low, medium, fairly high, high, very high, absolute high or occurrence. The level value of each classification were defined from 0 to 1 (Table 2, [29,45]). Then corresponding triangular numbers or trapezoidal numbers proposed by experts were used to judge occurrence probabilities of events.
3. Aggregate the fuzzy numbers. When the fuzzy numbers were all triangular number or trapezoidal number, Eq 11 was used to calculate the aggregated fuzzy number of experts for one event [42].

$$
\tilde{A}_{\text {aggregated }}=\sum_{u=1}^{M} W_{u} \otimes \tilde{A}_{u}
$$

where $\tilde{A}_{\text {aggregated }}$ denoted the aggregated fuzzy numbers of $M$ experts' judgment, $W_{u}$ denoted the weighting of expert.

Assume $\tilde{A}_{u}=\left(a_{u 1}, a_{u 2}, a_{u 3}\right)$ was triangular number and $\tilde{A}_{u}=\left(a_{u 1}, a_{u 2}, a_{u 3}, a_{u 4}\right)$ was trapezoidal number, calculation of $W_{u} \otimes \tilde{A}_{u}$ was showed as below (Eqs 12 and 13). Then Eqs 14 and 15 were used to calculate the value of $\tilde{A}_{1} \oplus \tilde{A}_{2}[30]$.

$$
\begin{gathered}
W_{u} \otimes \tilde{A}_{u}=\left(W_{u} \times a_{u 1}, W_{u} \times a_{u 2}, W_{u} \times a_{u 3}\right) \\
W_{u} \otimes \tilde{A}_{u}=\left(W_{u} \times a_{u 1}, W_{u} \times a_{u 2}, W_{u} \times a_{u 3}, W_{u} \times a_{u 4}\right) \\
\tilde{A}_{1} \oplus \tilde{A}_{2}=\left(a_{11}+a_{21}, a_{12}+a_{22}, a_{13}+a_{23}\right) \\
\tilde{A}_{1} \oplus \tilde{A}_{2}=\left(a_{11}+a_{21}, a_{12}+a_{22}, a_{13}+a_{23}, a_{14}+a_{24}\right)
\end{gathered}
$$

4. If the fuzzy numbers included both triangular number and trapezoidal number. Algorithm of the aggregation proposed by Lin and Wang [44] was employed, furthermore, experts

Table 2. Level Value of Each Classification.


doi:10.1371/journal.pone.0160045.t002

weighting were considered to improve the method. The following example was introduced to illustrate the algorithm.

Assume $\tilde{A}_{1}=\left(a_{11}, a_{12}, a_{13}\right)$ was triangular number proposed by expert 1 and $\tilde{A}_{2}=$ $\left(a_{21}, a_{22}, a_{23}, a_{24}\right)$ was trapezoidal number proposed by expert 2. Experts weightings of them were $W_{1}$ and $W_{2}$, respectively. The membership function of them were;

$$
\begin{aligned}
& f_{\tilde{A}_{1}}(x)= \begin{cases}\left(x-a_{11}\right) /\left(a_{12}-a_{11}\right), & a_{11} \leq x \leq a_{12} \\
\left(a_{13}-x\right) /\left(a_{13}-a_{12}\right), & a_{12} \leq x \leq a_{13} \\
0, & \text { otherwise }\end{cases} \\
& f_{\tilde{A}_{2}}(y)= \begin{cases}\left(y-a_{21}\right) /\left(a_{22}-a_{21}\right), & a_{21} \leq y \leq a_{22} \\
1, & a_{22} \leq y \leq a_{23} \\
\left(a_{24}-y\right) /\left(a_{24}-a_{23}\right), & a_{23} \leq y \leq a_{24} \\
0, & \text { otherwise }\end{cases}
\end{aligned}
$$

$\alpha$-cut method $[44,46]$ was employed to aggregate the fuzzy numbers, meanwhile, expert weighting was also considered (Eq 16).

$$
\tilde{A}_{W_{a}}=\sum_{u=1}^{n} W_{u} \otimes \tilde{A}_{u_{u}}
$$

where $\tilde{A}_{W_{a}}$ denoted $\alpha$-cut for membership function of the aggregated fuzzy number $\tilde{A}_{W}, W_{u}$ denoted expert weighting, $\tilde{A}_{u_{u}}$ denoted $\alpha$-cut for membership function of $\tilde{A}_{u}, n$ was the number of fuzzy numbers.

Then $\alpha$-cut for membership function of $\tilde{A}_{1}$ and $\tilde{A}_{2}$ were;

$$
\left\{\begin{array}{l}
\tilde{A}_{1_{a}}=\left[x_{1}, x_{2}\right] \\
\tilde{A}_{2_{a}}=\left[y_{1}, y_{2}\right]
\end{array}\right.
$$

Set $\alpha=\left(x-a_{11}\right) /\left(a_{12}-a_{11}\right)$, and $x$ can be either $x_{1}$ or $x_{2}$, so it can be obtained that $x_{1}=$ $\left(a_{12}-a_{11}\right) \alpha+a_{11}$, and by this analogy, the $\alpha$-cut values of $\tilde{A}_{1}$ and $\tilde{A}_{2}$ was calculated as;

$$
\left\{\begin{array}{l}
x_{1}=\left(a_{12}-a_{11}\right) \alpha+a_{11} \\
x_{2}=a_{13}-\left(a_{13}-a_{12}\right) \alpha \\
y_{1}=\left(a_{22}-a_{21}\right) \alpha+a_{21} \\
y_{2}=a_{24}-\left(a_{24}-a_{23}\right) \alpha
\end{array}\right.
$$

$\tilde{A}_{W_{a}}$ was computed as (Eqs 12 through 16);

$$
\begin{aligned}
\tilde{A}_{W_{a}}= & W_{1} \otimes \tilde{A}_{1_{a}} \oplus W_{2} \otimes \tilde{A}_{2_{a}} \\
= & W_{1} \otimes\left[x_{1}, x_{2}\right] \oplus W_{2} \otimes\left[y_{1}, y_{2}\right] \\
= & W_{1} \otimes\left[\left(a_{12}-a_{11}\right) \alpha+a_{11}, a_{13}-\left(a_{13}-a_{12}\right) \alpha\right] \\
& \oplus W_{2} \otimes\left[\left(a_{22}-a_{21}\right) \alpha+a_{21}, a_{24}-\left(a_{24}-a_{23}\right) \alpha\right] \\
= & {\left[\left(W_{1}\left(a_{12}-a_{11}\right)+W_{2}\left(a_{22}-a_{21}\right)\right) \alpha+W_{1} a_{11}+W_{2} a_{21}\right.} \\
& \left.W_{1} a_{13}+W_{2} a_{24}-\left(W_{1}\left(a_{13}-a_{12}\right)+W_{2}\left(a_{24}-a_{23}\right)\right) \alpha\right]
\end{aligned}
$$

Set $\tilde{A}_{W_{0}}=\left[z_{1}, z_{2}\right]$, we can obtained that;

$$
\left\{\begin{array}{l}
\alpha=\frac{z_{1}-\left(W_{1} a_{11}+W_{2} a_{21}\right)}{W_{1}\left(a_{12}-a_{11}\right)+W_{2}\left(a_{22}-a_{21}\right)} \\
\alpha=\frac{W_{1} a_{12}+W_{2} a_{21}-z_{2}}{W_{1}\left(a_{13}-a_{12}\right)+W_{2}\left(a_{24}-a_{23}\right)}
\end{array}\right.
$$

Then, the membership function of the aggregated fuzzy number can be obtained;

$$
f_{\tilde{A}_{W}}(z)=\left\{\begin{array}{ll}
\frac{z-\left(W_{1} a_{11}+W_{2} a_{21}\right)}{W_{1}\left(a_{12}-a_{11}\right)+W_{2}\left(a_{22}-a_{21}\right)}, & W_{1} a_{11}+W_{2} a_{21} \leq z \leq W_{1} a_{12}+W_{2} a_{22} \\
1, & W_{1} a_{12}+W_{2} a_{22} \leq z \leq W_{1} a_{12}+W_{2} a_{23} \\
\frac{W_{1} a_{13}+W_{2} a_{24}-z}{W_{1}\left(a_{13}-a_{12}\right)+W_{2}\left(a_{24}-a_{23}\right)}, & W_{1} a_{12}+W_{2} a_{23} \leq z \leq W_{1} a_{13}+W_{2} a_{24} \\
0, & \text { otherwise }
\end{array}\right.
$$

After that, the aggregated fuzzy number $\tilde{A}_{W}$ of $\tilde{A}_{1}$ and $\tilde{A}_{2}$ was achieved;

$$
\tilde{A}_{W}=\left(W_{1} a_{11}+W_{2} a_{21}, W_{1} a_{12}+W_{2} a_{22}, W_{1} a_{12}+W_{2} a_{23}, W_{1} a_{13}+W_{2} a_{24}\right)
$$

Moreover, when the number of fuzzy numbers was more than two, aggregation algorithm was similar to the procedure above.
5. After the aggregated fuzzy number was confirmed, centroid-index method (Eq 17, [36]) was used to deal with the fuzzy number, then the fuzzy possibility score (FPS) was obtained. Assume $\tilde{A}_{n}=\left(a_{n 1}, a_{n 2}, a_{n 3}\right)$ was triangular number and $\tilde{A}_{n}=\left(a_{n 1}, a_{n 2}, a_{n 3}, a_{n 4}\right)$ was trapezoidal number. Eq 18 was used to calculate FPS when fuzzy number was triangular number, and Eq 19 was used to calculate trapezoidal number.

$$
X=\frac{\int g(x) x d x}{\int g(x) d x}
$$

where $X$ is the defuzzified output, $g(x)$ is the membership function, and $x$ is the output variable.

$$
\begin{gathered}
F P S=\frac{1}{3}\left(a_{n 1}+a_{n 2}+a_{n 3}\right) \\
F P S=\frac{1}{3} \frac{\left(a_{n 3}+a_{n 1}\right)^{2}-a_{n 2} a_{n 3}-\left(a_{n 1}+a_{n 2}\right)^{2}+a_{n 1} a_{n 2}}{\left(a_{n 4}+a_{n 3}-a_{n 1}-a_{n 2}\right)}
\end{gathered}
$$

6. Finally, Eq 20 converted the FPS to FFR [37], and FFR was converted to occurrence probability of operational error and multiple failure (Eq 8).

$$
F F R= \begin{cases}1 / 10^{k}, & F P S \neq 0 \\ 0, & F P S=0 \\ k=2.301 \times[(1-F P S) / F P S]^{1 / 3}\end{cases}
$$

# Results 

## Biomass Gasification System

The biomass gasification system included a gasifier, dry type dust separator (DTDS), spray type dust separator (STDS), vacuum pump (VP), water-bath dust remover (WBDR), water separator (WS), tank, and pressure regulator (PR) (Fig 2). Biomass materials were burned in the gasifier with insufficient oxygen, and biomass gasses (hereafter referred to as "gas") including $\mathrm{CO}, \mathrm{H}_{2}$ and $\mathrm{CH}_{4}$ were produced by chemical reactions. The gas went into the DTDS, where most dust was separated. The VP was located between the STDS and WBDR. The gas was flowed into the STDS by the VP and was cleaned by the spray in the STDS. The WBDR provided further decontamination. Valve 2 (V-2) controlled the input of gas for the first WBDR, and valve $3(\mathrm{~V}-3)$ controlled another. There was a water inlet (WI) and water outlet (WO) on the WBDR, and water in the WBDR was replaced through WI and WO. Waste water was discharged from the WO, and fresh water was injected into the WBDR from the WI such that the liquid level was below the WI. After the WBDR, the gas arrived at the WS, where the inlet and
![img-1.jpeg](img-1.jpeg)

Fig 2. Biomass gasification system.
doi:10.1371/journal.pone.0160045.g002

outlet were controlled by valve 5 (V-5) and valve 6 (V-6). Residual water in the gas was absorbed by corncobs in the WS, which were replaced via three reloading locations (RL). There was a fire test orifice (FTO) setting after WS that tested the ignitability of gas at the beginning of production; FTO was controlled by valve 4 (V-4). Finally, the cleaned gas was stored in an external tank. Gas was released from the tank into the PR, which contained a bypass valve 1 (BV-1) installed in parallel with valve 7 (V-7) of the PR. BV-1 ensured that if V-7 was plugged, gas in tank would be released to maintain a safe pressure level. The pressure was monitored by a pressure sensor (PS). Valve 8 (V-8) was located after the PR, and bypass valve 2 (BV-2) was installed in parallel with V-8. Hence, when V-8 was plugged, the gas was transferred from BV-2.

# Analysis of Gas Leakage in the Biomass Gasification System 

As mentioned previously, the devices and pipelines before and after the VP were under the condition of negative and positive pressure during production process, respectively. No leakage could occur in the areas with the condition of negative pressure. And the tank was external to the system, then the parts where gas leakage would be considered were encircled by the dashed line in Fig 2. Gas leakage was set as the TE to make FTA. Meanwhile, ventilation system and alarm system were placed in the system. Then set them and ignition as CEs, and gas leakage was set as the IE to make ETA. Various OEs were obtained by the conditions of the CEs. Finally, gas leakage was set to be the LE, bow-tie analysis connected the FTA and ETA by the LE (Fig 3, Table 3). Eight OEs were predicted depending on the success or failure of CEs (Fig 3, Table 4). Gas ignition would occur if $\mathrm{CE}_{1}$ was success but not if $\mathrm{CE}_{1}$ was failure.

## BN-Bow-Tie Model of Gas Leakage

The BN-bow-tie model of gas leakage was established by converting FTA and ETA into BN (Fig 4).

## Confirming Occurrence Probability of Each Basic Event and Conditional Event

Occurrence probability of facilities failure in the biomass gasification system was retrieved from a standard reliability data resource (Eq 8, Table 5, [27]).

The other occurrence probabilities were confirmed by expert judgment. Five experts were invited to make judgment (Table 6). The weighting of each expert was calculated by Table 1 and Eqs 9 through 10 (Table 7).

Each expert gave judgment based on Table 2 to the events which belonged to the failure mode of operational error or multiple failure, and the corresponding fuzzy numbers were obtained (Table 8). Then the fuzzy numbers were aggregated by Eqs 11 through 16 (Table 9). Finally, the aggregated fuzzy numbers were converted to FPS and FFR by Eqs 17 through 20 (Table 9), and FFR was converted to occurrence probability by Eq 8 (Table 9).

## Occurrence Probability of LE and OE Updating

Occurrence probability of LE gas leakage and OEs were determined by Eqs 1 through 3, and the occurrence probabilities of them were listed in Table 10.

## Discussion

The occurrence probability of gas leakage in one year was $6.702 \mathrm{e}-1$ (Table 10), and occurrence probabilities of accidents would be reduced when ventilation and alarm system were present

![img-2.jpeg](img-2.jpeg)

Fig 3. Diagram of bow-tie analysis for gas leakage.
doi:10.1371/journal.pone.0160045.g003
and functional. However, present and functional ventilation or alarm system can't avoid minor accidents, their occurrence probabilities like $\mathrm{OE}_{5}$ and $\mathrm{OE}_{6}$ still remained relatively high. Although ventilation and alarm system were necessary to lessen the impact of gas leakage in biomass gasification system. But the key to avoid accidents was reducing the occurrence probability of gas leakage. Thus, the critical nodes of causes for gas leakage was determined by

Table 3. Details of Bow-tie Components in Fig 3.


doi:10.1371/journal.pone.0160045.t003

Table 4. OE Analysis.


doi:10.1371/journal.pone.0160045.t004

![img-3.jpeg](img-3.jpeg)

Fig 4. BN-bow-tie diagram of gas leakage.
doi:10.1371/journal.pone.0160045.g004

BN-bow-tie analysis, and the corresponding safety measures were proposed according to the critical nodes.

# Confirming the Critical Nodes of Causes 

To find the critical nodes of causes, the importance measures of each event was calculated by Eqs 4 through 7 (Table 11). The rank of events based on importance measures was obtained by the methods listed below.

Table 5. Occurrence Probability of Facilities Failure.


Note: all data was obtained from OREDA (2002) [27]. doi:10.1371/journal.pone.0160045.t005

Table 6. Description of Experts.


doi:10.1371/journal.pone.0160045.t006

Table 7. Weighting of Experts.


doi:10.1371/journal.pone.0160045.t007

Table 8. Experts Judgment of Operational Error and Multiple Failure.


doi:10.1371/journal.pone.0160045.t008

Table 9. FPS, FFR and Occurrence Probability Calculations of Operational Error and Multiple Failure.


doi:10.1371/journal.pone.0160045.t009

Table 10. Occurrence Probability of Gas Leakage and OEs.


doi:10.1371/journal.pone.0160045.t010

Table 11. Calculations of Importance Measures.


doi:10.1371/journal.pone.0160045.t011

1. If the amount of events was " $n$ ", the normalized weighting $R^{*}$ was calculated by the importance measures $I_{i}$ and Eq 21.

$$
R^{*}=\frac{I_{i}}{\sum_{i=1}^{n} I_{i}} \times 100
$$

2. After the normalized weighting $R^{*}$ of each importance measure was calculated, the total weighting $R_{e}^{*}$ was calculated by Eq 22.

$$
R_{e}^{*}=R_{B M}^{*}+R_{R A W}^{*}+R_{F V}^{*}
$$

3. Finally, events were ranked from maximum to minimum by total weighting $R_{e}^{*}$, and the critical nodes of causes was found by the rank. The results are shown in Table 12.

The total weighting of $B_{21}$ (V-4 is not closed), $B_{15}$ (flange is not tightly clipped), $B_{4}$ (wear of VP) and $B_{1}$ (VP seal failure) was much higher than others; they were the critical nodes of causes. Because accidents were mainly caused by these nodes, the occurrence probabilities of accidents could be reduced effectively by implementing corresponding safety measures. If $B_{21}$, $B_{15}, B_{4}$ and $B_{1}$ were implemented with measures to ensure safety, the occurrence probabilities was reduced to $1 / 10.3$ of the original values (Table 13).

Table 12. Rank of Events.


doi:10.1371/journal.pone.0160045.t012

# Providing Safety Measures for Critical Nodes 

$\mathrm{B}_{21}$ (V-4 is not closed) and $\mathrm{B}_{15}$ (flange is not tightly clipped) were operational errors. To eliminate these errors, a safety check was added to make sure that flange was tightly clipped before production. Additionally, the V-4 manual valve was replaced with a self-closing valve. Both $\mathrm{B}_{4}$ (wear of VP) and $\mathrm{B}_{1}$ (VP seal failure) are facilities failures; the VP safety checks should be improved and the VP seals replaced at regular intervals.

Table 13. Occurrence Probabilities of Accidents when Critical Nodes are Ensured Safety.


doi:10.1371/journal.pone.0160045.t013

# Conclusions 

1. In biomass gasification system, facilities failure data can be obtained from standard reliability data sources, and operational error data can be confirmed by fuzzy methods based on expert judgment. These reliability data can be used to make probabilistic safety assessment (PSA) of biomass gasification system.
2. Bow-tie analysis was employed to evaluate gas leakage from biomass gasification stations. When ventilation and alarm systems were present and functional, the occurrence probabilities of accidents caused by gas leakage were reduced, but they were inefficient in reducing the occurrence probabilities of minor accidents. Therefore, the occurrence probability of gas leakage must be lessened to reduce the exposure to associated accidents caused by gas leakage.
3. By mapping bow-tie analysis into BN (BN-bow-tie), the critical nodes of accidents causes were identified. These critical nodes of gas leakage were as follows: V-4 is not closed, the flange is not tightly clipped, wear of VP, and VP seal failure. If safety measures were implemented at these nodes, the occurrence probabilities of accidents were reduced to $1 / 10.3$ of the original values.
4. To reach the safety goal, safety checks should be added. The manual V-4 valve should be replaced with a self-closing valve, and the VP seals should be replaced periodically.

## Author Contributions

Conceived and designed the experiments: FY. Performed the experiments: FY. Analyzed the data: FY KLX. Contributed reagents/materials/analysis tools: FY KLX XWY. Wrote the paper: FY YL.
