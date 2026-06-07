# Fuzzy evidence theory and Bayesian networks for process systems risk analysis 


#### Abstract

Quantitative risk assessment (QRA) approaches systematically evaluate the likelihood, impacts and risk of adverse events. QRA using fault tree analysis (FTA) is based on the assumptions that failure events have crisp probabilities and they are statistically independent. The crisp probabilities of the events are often absent, which leads to data uncertainty. On the other hand, the independence assumption leads to model uncertainty. Experts' knowledge can be utilised to obtain unknown failure data; however, this process itself is subject to different issues such as imprecision, incompleteness, and lack of consensus. For this reason, to minimise the overall uncertainty in QRA, in addition to addressing the uncertainties in the knowledge, it is equally important to combine the opinions of multiple experts and update prior beliefs based on new evidence. In this paper, a novel methodology is proposed for QRA by combining fuzzy set theory and evidence theory with Bayesian networks to describe the uncertainties, aggregate experts' opinions, and update prior probabilities when new evidences become available. Additionally, sensitivity analysis is performed to identify the most critical events in the FTA. The effectiveness of the proposed approach has been demonstrated via application to a practical system.


Keywords: Risk analysis; Fault tree analysis; Process safety; Evidence theory; Fuzzy set theory; Bayesian networks; Uncertainty analysis

# 1. INTRODUCTION 

Risk assessment and safety analysis are a well-known way to predict and minimise the likelihood of the occurrence of an accident in chemical process industries (Khan and Abbasi, 2000; Markowski and Mannan, 2009). Such industrial systems have many potential hazard sources to cause an accident, including fire, explosion, toxic release, vapour emission, and holding operations. All these hazards have the potential to cause injury, death in the workplace, assets damage, economic loss, and environmental pollution. Fault tree analysis (FTA) as a qualitative and quantitative technique has been widely used for risk assessment to provide detailed analysis that helps to reduce the probability of an adverse event and subsequently diminish unfavourable process consequences (Abuswer et al., 2016; Adedigba et al., 2016a; Kabir, 2017).

FTA illustrates a graphical relationship between undesired events and basic causes which are typically named as a top event (TE) and basic event (BE), respectively (Khan et al., 2002; Modarres, 1993; Modarres et al., 1999). In quantitative FTA, the probability of each BE is necessary to be known which can be either an exact crisp value or probability density function (PDF). Many variants of system designs and failure modes, many possible interactions between the system components and poor understanding of failure mechanisms can make it difficult to obtain crisp values or make PDFs highly complex to be computed (Ahmed et al., 2015; Markowski and Kotynia, 2011; Markowski et al., 2009). Thus, the efficiency of quantitative FTA strongly depends on the validity of such data should they come out from plant maintenance history (Curcur et al., 2012). However, in many cases, the crisp value of probability as well as PDFs is seldom to be available. Therefore, to deal with such situations, expert judgement as an alternative method is often employed to acquire the objective data (Kabir et al., 2018a; Omidvari et al., 2014). Uncertainty is inherently unavoidable issue during elicitation of experts' knowledge since it comes out of limited information, physical variability of a system, or lack of knowledge (Ferdous et al., 2013; Markowski and Mannan, 2008; Yazdi, 2017a). Two main types of uncertainties: aleatory and epistemic uncertainties are commonly issued using expert elicitation in qualitative risk analysis, where the former is due to randomness of a physical system or natural variation whereas the latter is because of ambiguity, incompleteness, and lack of knowledge (Ferdous et al., 2012; Hong et al., 2016; Markowski and Kotynia, 2011).

The idea of fuzzy set theory and evidence theory have been extensively used in many applications such as target recognition, combining clustering, failure detection, decision analysis, and uncertain information processing. These

approaches are proven to be efficient and effective to deal with the mentioned uncertainties based on experts' elicitation assessment (Awasthi and Chauhan, 2011; Deng et al., 2014a, 2014b; Du et al., 2016; Ferdous et al., 2011, 2009a; Huang et al., 2014; Lavasani et al., 2015a, 2015b; Liu et al., 2014; Omidvari et al., 2014; Talavera et al., 2013; Wei et al., 2013; Yang et al., 2008; Yazdi et al., 2017b; Zargar et al., 2012; Zhou et al., 2016). Furthermore, to draw a clear picture of the usage of fuzzy set theory and evidence theory in engineering applications, Han and Chen (2008) used fuzzy set theory and machine learning to model complex dynamic system under vague conditions. The fuzzy Mamdani reasoning system was used for their proposed estimation. Musharraf et al. (2013) introduced a novel approach by integrating evidence theory with a probabilistic approach for human factor analysis. The approach handles uncertainty in human factor analysis in offshore evacuation planning. Zhao et al. (2012) applied Bayesian networks (BNs) to prioritize the factors that influence hazardous material transportation accidents in China. The structure of BNs was created based on expert knowledge using evidence theory. Another study has been performed by Zhou and Thai (2016) for failure prediction of oil tanker equipment using failure mode and effect analysis. They used fuzzy set and grey theory to handle uncertainty and reflect the nature of relative ranking, respectively. Recently, Akyildiz and Mentes (2017) introduced a fuzzy set based risk assessment approach using expert knowledge, which systematically incorporated a set of plausible model scenarios that lead to cargo vessel accidents at the coasts and open seas of Turkey. In the mentioned approaches, the fuzzy set theory is commonly used to address the subjectivity in experts' judgement which means aleatory and evidence theory is employed to deal with objectivity (epistemic) which may arise from ignorance, conflict, and incompleteness (Ferdous et al., 2011; Hong et al., 2016). However, the mentioned theories are not capable to cope with both types of uncertainties in an exact assessment. In addition, these theories cannot update the probabilities in risk assessment when a new knowledge becomes available.

In order to handle mentioned uncertainties, Ferdous et al. (2009b) presented a new methodology based on fuzzy computer aided FTA tool to find out the fuzzy probability, which is used in performing a fuzzy probabilistic risk assessment. They illustrated that fuzzy approach has enough capability to handle vague and imprecise input data in FTA. In this context, Curcur et al. (2012) utilised evidence theory to handle epistemic uncertainty in typical FTA in a practical application considering two realistic scenarios. Their proposed approach claimed that direct estimation of uncertainty for TE is much more difficult than considering its computation from unique sources constituted by the BEs. Additionally, Ferdous et al. $(2013,2011)$ provided an innovative approach to accommodate experts' opinions

to deal with unknown data and engage the mentioned theories to assess both types of uncertainties in Bow-tie analysis. Further, to illustrate the usefulness of the approach, it was applied as an industrial application into the BP Texas City accident, which was developed and analysed in details. Moreover, they recommended that updating the likelihoods of event occurrence based on newly observed information using Bayesian updating mechanism can be considered to extend the approach. Besides, combination of subjectivity and objectivity into a single approach like fuzzy evidence theory is another vital aspect of getting trustworthy outcomes from risk assessment. Accordingly, Ferdous et al. (2012) developed a methodology to implement an updating mechanism along with characterisation of uncertainty and aggregating multi-experts' opinions in Bow-tie analysis. Yazdi and Kabir (2017) presented a fuzzy set-based FTA to handle the uncertainty associated with failure data and employed the Bayesian updating mechanism for modelling dependency among the BEs and for quantitative analysis under uncertain conditions. Authors represented that a fuzzy Bayesian mechanism can be used to compute the posterior or updated probability incorporating new knowledge into prior information. Moreover, Deyab et al. (2018) used BNs to model causal dependencies between events and to handle uncertainty in the failure data. Adedigba et al. (2017) integrated BN with principal component analysis (PCA) for dynamic failure analysis of process systems. In their approach, PCA was used to detect faults, whereas BN was used to predict time-dependent system failure probability by modelling causal dependencies among different variables. Hierarchical Bayesian analysis (HBA) has been used by El-Gheriani et al (2017a) to handle data uncertainty in risk and reliability analysis. Furthermore, in (El-Gheriani et al., 2017b), they combined BNs and HBA to handle both model and data uncertainties. Recently, BN-based methodologies have been proposed in (Baksh et al., 2018, Abaei et al., 2018, Hegde et al., 2018) for risk assessment in the maritime domain. Additionally, Bucelli et al. (2018) proposed a dynamic risk assessment approach by adapting the Risk Barometer (RB) (Paltrinieri and Khan, 2016) concept.

To the best of the authors' knowledge, limited attempts have been made so far to address both types of uncertainties in a single approach in the process safety domain. In this context, the value of the paper is in the development of an approach combining fuzzy set theory and evidence theory to address objective and subjective uncertainties within a single framework. In addition, the Bayesian update mechanism has a more general value in incorporating real time data in the risk assessment process.

# 2. MATERIALS AND METHODOLOGY 

Fault tree (FT) is a renowned and widely used technique, which shows the logical relationship between many events that can cause subsequent events, which in turn can cause the system failure. From a fault tree, it is possible to determine the different paths leading to a specific failure in a system, i.e., the causes of a specific failure can be determined (Banerjee, 2003; Ferdous et al., 2009b; Khan et al., 2015). FTA is a deductive method and has been extensively used in process facilities to recognise and assess the system hazards (Abuswer et al., 2013; Rathnayaka et al., 2012). Finding the probability of the TE depends on the failure rates of the BEs, which are extracted from standard reliability databases such as OREDA (2002). Nevertheless, when the exact failure rates are ambiguous or limited, which is a very common situation in process industries, the FTA will extremely be dependent on expert opinion. In such situation, application of conventional FTA together with dynamic risk analysis becomes less credible. To handle these situations, this section presents a new methodology. An overview of the method is graphically illustrated in Fig. 1. As seen in the figure, the method has five key phases: hazard analysis, FT construction and data collection, experts judgement, Bayesian modelling, and the calculation. Within these phases, the steps taken are: (1) All information related to process function are collected. (2) The worst-case scenario is selected and considered as a TE in FTA. (3) Fault tree is developed based on root cause analysis. (4) All BEs, intermediate events (IEs) and their logic relationship are recognized. (5) The failure rates of BEs are collected through expert judgements in terms of fuzzy numbers. (6) The employed experts are weighted using entropy technique as an objective tool. (7) The aggregation process is applied through which all BE failure rates are collected using the linguistic terms by employing expert judgements. (8) The probabilities of all BEs are obtained. (9) The fault tree is converted into the Bayesian network and accordingly the probability of TE is computed. (10) The sensitivity analysis is performed to identify the critical BEs. The five key phases are described in details as follows.

Fig. 1. The structure of the proposed approach.

# 2.1. Hazard Analysis 

Numerous techniques are introduced and have been widely used for hazard analysis in recent decades, such as failure mode and effect analysis (FMEA), Bow-tie, and hazard and operability study (HAZOP) (Villa et al., 2016). For this purpose, all possibilities of failures need to be considered and it is obvious that the functional behaviour of the specific system is required to be well understood before attempting to develop fault trees. When the collection of information about process system is completed by answering the question "what can go wrong?", it will bring all identified hazards and threats which can cause harm to human being and/or environment and damage to one or more assets (Hashemi et al., 2015; Rausand and Høyland, 2004). Amongst mentioned analysis, HAZOP is a system analytics tool for understanding how deviations from correct operation may occur and identifying possible measures to deal with the causes (Ayyub, 2014; Modarres, 2006; Rausand, 2011). Therefore, for this study, the output of HAZOP is labelled as an unexpected event (i.e., the TE of FT) and it was used to identify significant potential process hazards of a chemical process plant.

### 2.2. Data Extraction and Fault Tree Creation

In order to construct an FT, for the selected TE under study, the subordinate BEs which may contribute to the TE are recognised and linked to the TE by logical interrelationships using AND/OR gates. The TE usually demonstrates an accident that may be a source of process hazards or asset losses (Hossain et al., 2013). It is placed at the top of the FT and the tree is systematically developed downwards to find all possible ways of TE occurrence. In an FT, BEs are considered statically independent with two states, including failed and non-failed (binary states).

Expert knowledge can be utilised to determine the probability of basic events when failure rates are unknown or limited (Preyssl, 1995). Expert elicitation is an established fundamental scientific solidarity method. It is often used in cases where events are rare. Additionally, an expert elicitation typically measures uncertainties by permitting specialists parameterisation as an educated guess. In the proposed method, expert judgement is used to estimate the occurrence probability of unknown BEs, because information about the probability of an event represented based on multiple source of knowledge is more trustworthy than the single expert opinion. In addition, knowledge as an opinion cannot be considered overconfidently due to the fact that it is affected by vague information and socially negotiated, constructed and diverged (Ayyub, 2001; Ferdous et al., 2011). Hence, incorporation of fuzzy set theory,

subjective judgements, and evidence theory, as suggested by Ferdous et al (2011, 2009a) as a direction for further study, can help the analysts to subdue any possible uncertainty. The following section presents a technique on how experts' judgements can be used to acquire the unknown failure rate/probability.

# 2.3. Use of Expert Judgement 

Expert judgement is partial by personal visions and purposes (Ford and Sterman, 1998), therefore, it is highly difficult to attain an impartiality of expert judgement. Besides, in order to avoid cognitive biases introduced by any single expert's judgement, it is vital to invite heterogeneous groups of expert, who have background related to the system under study, to provide opinions about the system. The criteria for the recognition of experts can be the period of learning and experience in the precise scope of knowledge, and the practical or theoretical conditions at which the individual acquired the experience. In practice, the weight of individual expert can be estimated reliably based on his/her background. As a result, the estimated weights are necessary to signify the relative superiority of the employed experts. There are many objective and subjective methods to evaluate the criteria and attitudes, meaning that the evaluations are subject to a wide range of perception. Subjective weighting provides the determination of preferences and judgements from experts and objective one tackle the situation where experts' opinions are not easily achievable (Chen et al., 2014; Deng et al., 2000). As objective methods are able to cope with any cognitive biases based on expert judgement in their prediction, in this study, an objective tool is considered for experts weighting.

An important measure of objective uncertainty was proposed by Shannon and Weaver in 1947, which is highlighted as entropy technique (Shannon, 1948). It is a well-suited technique for selecting the objective weight of attributes. Entropy technique is briefly introduced as a preliminary tool in the proposed model as follows.

According to the entropy technique, the importance weights of decision attributes directly relating a criterion's importance weighting relative to the information, which is transferred by that criterion, is determined. For the same criterion, the weight of criterion evaluation will not be significant when the performance variance between different alternatives is small. In contrast, the criterion that transmits the most information should have the greatest

importance weighting. Therefore, entropy technique has the capability to deal with objective weighting computation through the following stages (Aghajani Bazzazi et al., 2011; Chen et al., 2014; Jing et al., 2012).

Stage 1: As an example, a decision matrix with column vector $x_{j}=\left(x_{1 j}, x_{2 j}, \ldots, x_{m j}\right)$ illustrates that the contrast of all alternatives with regards to $\mathrm{j}^{\text {th }}$ attribute. The values of alternatives with respect to selected attribute $x_{j}$ are specified by an attribute matrix $X=\left(X_{i j}\right)_{m \times n}$ as follows.
$X=\begin{array}{cccc}A_{1} & x_{11} & x_{12} & \ldots & x_{1 n} \\ A_{2} & x_{21} & x_{22} & \ldots & x_{2 n} \\ \vdots & \vdots & \vdots & \vdots & \vdots \\ A_{m} & x_{m 1} & x_{m 2} & \ldots & x_{m n}\end{array}$

Mathematically, it means that the projected outcomes of attributes $j, P_{i j}$, are defined as:
$P_{i j}=\frac{x_{i j}}{\sum_{i=1}^{m} x_{i j}}$
where, $m$ is the number of alternatives evaluated and $n$ is the number of criteria (attributes) in the decision matrix.

Stage 2: The entropy $E_{j}$ of the set of projected outcomes of criterion $j$ is computed as:
$E_{j}=-\left(\frac{1}{\ln m}\right) \sum_{i=1}^{m} P_{i j} \cdot \ln P_{i j}$
where $m$ is the number of alternatives and accordingly it guarantees that $0 \leq E_{j} \leq 1$, and $\frac{1}{\ln m}$ is considered as a constant value.

Stage 3: The degree of diversification is defined as follows:
$d i v_{j}=1-E_{j}$
where the greater the value of the $d i v_{j}$ the more important the criterion is in the decision making process.

Stage 4: The objective weight of criterion $j$ is obtained as follows.
$w_{j}=\frac{d i v_{j}}{\sum_{j=1}^{n} d i v_{j}}$

where $w_{j}$ is the objective weight of criteria $j$.

Stage 5: In this case, in order to find out the weight of each alternative, decision matrix should be normalised and subsequently the weight of each alternative can be computed by multiplying the normalised vector into the weights of criteria as follows:
$n_{m n}=\frac{x_{m n}}{\sqrt{\sum_{n=1}^{n} x_{m n}^{2}}}$
where $n_{n m}$ is a normalised value regarding criteria $n$ from alternative $m$.

The weight of each alternative is computed as:
$W_{A_{m}}=n_{m 1} \times w_{1}+n_{m 2} \times w_{2}+\cdots+n_{m n} \times w_{n}$
where each alternative represented a respective expert.

# 2.4. Aggregation Procedure (fuzzy evidence theory) 

The focus of aggregation procedure is to process data and handle uncertainties in risk analysis. There are two common techniques such as fuzzy set theory and evidence theory developed and widely used to address the different kind of uncertainties. Fuzzy set theory can deal with subjective and impression uncertainties of an event probability with respect to experts' knowledge. Similarly, evidence theory is more prominent to cope with undependable, insufficient, and incompatible evidence obtained from the diverse employed experts (Ferdous et al., 2013, 2011, 2009a; Yazdi, 2017b). Therefore, a brief description of fuzzy set theory and evidence theory with respect to handling uncertainty are introduced as follows.

### 2.4.1. Fuzzy set theory

Fuzzy set theory is introduced by Zadeh (1965) in his pioneering work to represent that the conventional probability theory has not enough capability to include all types of uncertainty. Because, it is unable to model human conceptualisation and create perception which are possible to be considered in the real world (Khan and Sadiq, 2005; Ross, 2009). Therefore, fuzzy set theory is sufficient to handle vagueness and subjective uncertainty as an

extension to the conventional set theory. Fuzzy set theory can provide qualitative terms of possibility in order to convert them into the corresponding possibility and subsequently obtaining the numerical reasoning.

Triangular, trapezoidal, intuitionistic, and Gaussian fuzzy membership functions are examples of qualitative terms used as part of fuzzy set theory to address uncertainties and inaccuracies in expert knowledge (Atanassov, 2012; Purba et al., 2014; Kabir and Papadopoulos, 2018). That is because experts are more willing to express their opinions in qualitative terms instead of numerical sets (Miller, 1956; Nicolis and Tsuda, 1985). The assurance of the most appropriate membership function is dictated by realistic situations (Markowski and Mannan, 2008). In previous studies, triangular and trapezoidal fuzzy numbers have been found effective by Celik et al. (2010), Hsi-Mei Hsu and Chen-Tung Chen (1996), Kumar et al. (2010), Lavasani et al. (2015b), Miri Lavasani et al. (2011) and Yazdi and Zarei, (2018) for risk analysis.

For example, a triangular fuzzy number represented in the form of equation (8), is the simplest possible shape that can represent the uncertainty in possibility estimates of BEs. The triangular fuzzy number vector $g=\left(P_{L}, P_{m}, P_{U}\right)$ can be denoted respectively as the lower boundary, most likely boundary, and upper boundary. Using Eq. (9), degree of membership of confidence in uncertainty estimation can be computed using defuzzification methods (centre of area).
$\mu_{g}(x)=\left(\begin{array}{cc}0, & x<P_{L} \\ \frac{x-P_{L}}{P_{m}-P_{L}}, & P_{L} \leq x \leq P_{m} \\ \frac{P_{U}-x}{P_{U}-P_{m}}, & P_{m} \leq x \leq P_{U} \\ 0, & x>P_{U}\end{array}\right)$
$X^{*}=\frac{\int \mu_{i}(x) x d x}{\int \mu_{i}(x) d x}$
where
$X^{*}=$ Defuzzified output;
$\mu_{g}(x)=$ membership or aggregated membership function;
$x=$ output variable.

Eq. (9) can be applied to both trapezoidal and triangular fuzzy numbers (see Khan and Sadiq (2005); Kabir et al. (2016), Liu (2016); Ross (2009) for more details). Once the degree of membership as a possibility of an input event (BE) is computed, the possibility is converted to probability using Onisawa's equation as follows (Onisawa, 1996, 1988).
$P=\left\{\begin{array}{ll}1 / 10^{K}, C P \neq 0 \\ 0, C P=0\end{array}, K=\left[\left(\frac{1}{C P}-1\right)\right]^{1 / 3} \times 2.301\right.$
where $P$ is denoted as a probability of an input event and $C P$ represents the crisp possibility or in other words the confidence degree of membership. .

This study conceived triangular and trapezoidal fuzzy numbers as seen in Table 1 to map qualitative experts' opinions to fuzzy membership function which ranges between 0 and 1 . These two types of fuzzy numbers are used because the membership functions of these numbers can directly meet the suitable optimisation criteria under some weak assumptions (Pedrycz, 1994; Yazdi, 2017c).

Table 1. Qualitative terms and compatible fuzzy numbers for possibility estimation of an input event (BE)

# 2.4.2. Evidence theory 

Evidence theory is introduced by Dempster in 1967 and later developed by Shafer during the 1980s (Shafer, 1976; Yang et al., 2011) based on milestones on the lower and upper bounds of belief assignment to the hypothesis. This theory is also called Dempster-Shafer theory (D-S) which is commonly used to deal with both imprecision and uncertain information in many applications as stated by Du et al. (2016), Jiang et al. (2017), Li et al. (2017), and Zhou et al. (2016). D-S used the three basic parameters called basic belief (probability) assignment (bba), belief measure (Bel), and plausibility measure (pl) to characterise uncertainty in a belief structure in order to aggregate multi-experts' opinions according to their personal degree of belief (Bae et al., 2004; Ferdous et al., 2009a; Lefevre et al., 2002; Ross, 2009). In addition, the belief structure is represented in a continuous interval [belief, plausibility]

in which the true probability has the possibility to lie (Ferdous et al., 2013, 2011, 2009a; Ross, 2009). A brief description of the mentioned parameters in evidence theory is provided as follows.

Let $\Omega$ be a set of $N$ elements, which is a finite nonempty exhaustive set of mutually exclusive possibilities in evidence theory named frame of discernment. The power set (PS) of $\Omega$ allows having all possible subsets, denoted as $2^{\Omega}$ and includes $2^{N}$ elements in the $2^{\Omega}$. For example, if $\Omega=\{Y, F, P\}$, and $N=3$, then the power set is $2^{\Omega}=$ $\{\{\phi\},\{Y\},\{F\},\{P\},\{Y, F\},\{Y, P\},\{F, P\},\{Y, F, P\}\}$, where $\phi$ denotes a null set and subsequently evidence theory begins by defining the frame of discernment.

The basic belief assignment (bba) is a principal from evidence theory and also is known as belief mass. It is denoted by $m\left(p s_{i}\right)$ and is a mapping of the power set: $m\left(p s_{i}\right): 2^{\Omega} \rightarrow[0,1]$, and satisfy following equations:
$m(\emptyset)=0$
$\sum_{p s_{i} \in P S} m\left(p s_{i}\right)=1$
where $0 \leq m\left(p s_{i}\right) \leq 1$, and $p s_{i} \in 2^{\Omega}$.
$p s_{i}$ represents the acquired knowledge from expert opinions with exact probability in which the evidence links to $m$ supports proposition of $m\left(p s_{i}\right)$. In other words, $p s_{i}$ can be either a possible event or a set of multiple possible events.

The belief measure (Bel) is usually defined by the basic probability assignment function which is denoted by $\operatorname{Bel}\left(p s_{i}\right)$ and also is often named as lower bound for set $p s_{i}$. The relation between $b b a$ and $B e l$ is defined as:
$\operatorname{Bel}\left(p s_{i}\right)=\sum_{p s_{k} \subseteq p s_{i}} m\left(p s_{k}\right)$
where $\operatorname{Bel}(\phi)=0$ and $\operatorname{Bel}(\Omega)=1$.

Shafer represents that for natural number $n, p s_{i} \subseteq \Omega$ :
$\operatorname{Bel}\left(p s_{1} \cup p s_{2} \cup \ldots \cup p s_{n}\right) \geq \sum_{i} \operatorname{Bel}\left(p s_{i}\right)-\sum_{r>1} \operatorname{Bel}\left(p s_{r} \cap p s_{1}\right)+\cdots+(-1)^{n} \operatorname{Bel}\left(p s_{1} \cap p s_{2} \cap \ldots \cap p s_{n}\right)$

where $i, r, j=1,2, \ldots, n$.

The plausibility measure (pl), sometimes terms as upper bound for a set $p s_{i}$ is defined as following:
$P l\left(p s_{i}\right)=1-\operatorname{Bel}\left(\overline{p s_{i}}\right)=\sum_{p s_{k} \cap p s_{i}=\phi} m\left(p s_{k}\right)$
where $\overline{p s_{i}}$ is the negation of a hypothesis $p s_{i}$.

In order to obtain more details one can refer to evidence theory section in Ross (2009). The D-S evidence theory like as fuzzy set theory can aggregate multiple sources of evidence which is elicited from various experts through the combination rule. The most popular combination rule firstly proposed by Dempster \& Shafer (D-S) is known as the D-S combination rule. Hence, combining the multi-experts' opinions, will follow statistically independent summation as considered by Eq. (16).
$m_{1-n}=m_{1} \oplus m_{2} \oplus m_{3} \oplus \ldots \oplus m_{n}$
where operator $\oplus$ represents summation in combination rule.

Supposing that the opinion sources are independent and given that the two basic belief assignments $m\left(p s_{i}\right)$ and $m\left(p s_{\text {II }}\right)$ are sets of evidence for an exact event which is obtained from two independent sources (experts), then the D-S combination rule can be expressed as follows:
$m_{1-2}\left(p s_{i}\right)=\left[m_{1} \oplus m_{2}\right]\left(p s_{i}\right)=\left\{\begin{array}{cl}0 & \forall p s_{i}=\emptyset \\ \frac{\sum_{p s_{1} \cap p s_{\mathrm{II}}=p s_{1}} m_{1}\left(p s_{1}\right) m_{2}\left(p s_{\mathrm{II}}\right)}{1-\sum_{p s_{1} \cap p s_{\mathrm{II}}=\emptyset} m_{1}\left(p s_{1}\right) m_{2}\left(p s_{\mathrm{II}}\right)} & \forall p s_{i} \neq \emptyset\end{array}\right\}$
where $m_{1-2}\left(p s_{i}\right)$ denotes the $b b a$ of $p s_{i}$ which combined two experts' opinions for a specific event.

It is obvious that the D-S evidence theory has high effectiveness in uncertainty handling and aggregating opinions. However, it is criticised for some limitations such as when the number of independent sources is more than two; the complexity of computation increases exponentially. Besides, Zadeh (1986) proposed a numerical example to show that D-S evidence theory is unable to cope with highly confident evidence which may acquire a counter-productive output (Jiang et al., 2017).

Let us consider that two $b b a$ are listed as follows:
$m_{1}\left(p s_{\mathrm{I}}\right)=0.99,1-m_{1}\left(p s_{\mathrm{I}}\right)=0.01$.
$m_{2}\left(p s_{\mathrm{II}}\right)=0.01,1-m_{2}\left(p s_{\mathrm{II}}\right)=0.99$.

The $b b a$ of hypothesis $p s_{\mathrm{II}}$ can be determined as follows:
$m_{2}\left(p s_{\mathrm{II}}\right)=\frac{0.01 \times 0.01}{1-\left(0.99 \times 0.01+0.99 \times 0.99+0.01 \times 0.99\right)}=1$

It shows that the final output of total belief to $p s_{\mathrm{II}}$ is the most unlikely hypothesis. Therefore, it is not logical and sensible for making decisions. However, some extensions are introduced to propose new alternative combination rule to cope with the latter shortcoming (Deng et al., 2016; Yager, 1987). In addition, some researchers believe that D-S theory is not the only cause of acquiring a counter-productive output; accordingly, they introduced a model by refining given $m_{1}\left(p s_{\mathrm{I}}\right)$ and $m_{2}\left(p s_{\mathrm{II}}\right)$ and using D-S combination rule (Han et al., 2011; He et al., 2012; Jiang et al., 2016; Schubert, 2011). In this study, a combination of D-S theory and conventional fuzzy set theory is considered for aggregating the information from independent sources like as employed multi-experts opinions for computing the failure probability of BEs in a specific FT.

# 2.4.3. Combining fuzzy set theory and D-S evidence theory 

The experts' opinions from different independent sources are aggregated using fuzzy evidence theory. In a FT, the functional state of BE is categorised in two states: success (S) and failure (F); which notifies the availability and unavailability of the BE (Ferdous et al., 2012; Rausand, 2014; Roberts and Vesely, 1987). Thus, the frame of discernment to classify uncertainty of BE for FT can be defined as $\Omega=\{S, F\}$, subsequently the power set (PS) contains $\left[\{\phi\},\{S\},\{F\},\{S, F\}\right]$. Clearly, the $b b a$ signifies the degree of expert opinion (belief) for each subset and denotes the total evidence needed to specify the event possibility completely. For instance, an employed expert is asked to express his/her opinion in a qualitative term (see Table 1) to determine the occurrence possibility of a BE. Let us say, the expert was asked to answer the question "how much do you believe that the BE is in failure or success state?" In our opinion, it seems that experts are likely to give a clear answer to the question and for example, consider his/her answer is VH and VL for failure and success, respectively. Mathematically it can be written as $m_{1}(\{S\})=(0.8,0.9,1), m_{1}(\{F\})=(0,0.1,0.2)$, and $m_{1}(\{S, F\})=1-\left[m_{1}(\{S\})+m_{1}(\{F\}\right)]=0$. The latter

subset represents that ignorance or incompleteness information of experts' opinions (Ferdous et al., 2013; Sadiq et al., 2006). As mentioned earlier, the summation of $m\left(p s_{i}\right)=1$, in case there exists inconsistency in the summation using fuzzy operation rules, the validation of experts' opinions should be repeated to rectify the consistency and satisfy Eq. (12).

Now, consider two other experts express their opinions for the same BE possibility with expert\#2: $m_{2}(\{S\})=$ $(0.1,0.2,0.3), m_{2}(\{F\})=(0,0.1,0.2)$, and $m_{2}(\{S, F\})=1-[(0.1,0.2,0.3)+(0,0.1,0.2)]=(0.5,0.7,0.9)$; and expert\#3: $m_{3}(\{S\})=(0.4,0.5,0.6), m_{3}(\{F\})=(0.4,0.5,0.6), \quad$ and $\quad m_{3}(\{S, F\})=1-[(0.4,0.5,0.6)+$ $(0.4,0.5,0.6)]=0$. These three independent assessment can be combined using D-S theory rules for the same BE considering fuzzy operation rules for triangular and trapezoidal fuzzy numbers, a detail explanation of which is provided by Abbasbandy and Amirfakhrian (2006) and Mateos and Jiménez (2009).

The details of the D-S combination rule are provided in Table 2 with respect to the same weight for each expert. As discussed in section 2.3, clearly in practice, each expert has different weight according to their background. Thus, for the application of the study, the weight of each expert is considered by scalar multiplication of each weight to corresponding fuzzy numbers based on collected qualitative terms from the experts.

Table 2. Fuzzy evidence combination (aggregation) for finding the possibility of BE

Take the first one as an example, the fuzzy evidence output regarding to multiplication of three fuzzy trapezoidal numbers $\{S\},\{S\}$, and $\{S\}$ is computed as follows:
$m_{1}(\{S\}) \otimes m_{2}(\{S\}) \otimes m_{3}(\{S\})=(0.8,0.9,1) \otimes(0.1,0.2,0.3) \otimes(0.4,0.5,0.6)=(0.025,0.090,0.090,0.171)$.
In the above case, output of multiplication of three triangular fuzzy numbers is represented as a trapezoidal fuzzy number. It should be noted that a triangular fuzzy number can be represented as a trapezoidal number if needed (Yazdi et al., 2018), e.g., when we need to calculate the summation of one triangular and one trapezoidal fuzzy number (Ross, 2009). The results of other fuzzy evidence output are provided in Table 2.

In order to compute the possibility of specific BE, Eq. (9) is used for defuzzification of required trapezoidal fuzzy set $\{F\},\{\phi\}$, and $\{S, F\}$. Once, the defuzzification is completed, the combination of D-S theory rules as shown in Eq. (17) is utilised for $\{F\}$ as follows:
$\sum_{p s_{\mathrm{I}} \cap p s_{\mathrm{II}} \cap p s_{\mathrm{III}}=\{F\}} m_{1}\left(p s_{\mathrm{I}}\right) m_{2}\left(p s_{\mathrm{II}}\right) m_{3}\left(p s_{\mathrm{III}}\right)=0.051$,
$\sum_{p s_{\mathrm{I}} \cap p s_{\mathrm{II}} \cap p s_{\mathrm{III}}=\{S, F\}} m_{1}\left(p s_{\mathrm{I}}\right) m_{2}\left(p s_{\mathrm{II}}\right) m_{3}\left(p s_{\mathrm{III}}\right)=0$,
$\sum_{p s_{\mathrm{I}} \cap p s_{\mathrm{II}} \cap p s_{\mathrm{III}}=\phi} m_{1}\left(p s_{\mathrm{I}}\right) m_{2}\left(p s_{\mathrm{II}}\right) m_{3}\left(p s_{\mathrm{III}}\right)=0.596$,
$m_{1-3}(\{F\})_{D-S \text { theory }}=\left[m_{1} \oplus m_{2} \oplus m_{3}\right](\{F\})=0.051 /(1-0.596)=0.127$,
$m_{1-3}(\{S, F\})_{D-S \text { theory }}=\left[m_{1} \oplus m_{2} \oplus m_{3}\right](\{S, F\})=0 /(1-0)=0$.
The interval [belief, plausibility] provides the belief structure of experts' opinions which is considered as conflicts and ignorance in multi-experts' judgement. Let $m$ be a bba on the frame of discernment $\Omega$. "Bet" estimation gives a pignistic possibility function in the belief structure satisfying $\operatorname{Bet}(P): \Omega \rightarrow[0,1]$ similar to defuzzification procedure \{Formatting Citation\}. This is estimated with the following equation:
$\operatorname{Bet}(P)=\sum_{P \in p} \frac{1}{\left|P_{I}\right|} \frac{m\left(P_{I}\right)}{1-m(\phi)} \quad \forall m(\phi) \neq 1$
where $\left|P_{I}\right|$ is the number of elements in subset $P_{I}$.

The Bet estimation for previous example regarding to the possibility of $\{F\}$ obtained by D-S theory combination rule can be computed as follows:
$\operatorname{Bet}(P)=\frac{m_{1-3}(\{F\})}{1}+\frac{m_{1-3}(\{S, F\})}{2}=\frac{0.127}{1}+\frac{0}{2}=0.127$
where the denominators " 1 " and " 2 " signifies the number of elements in each subset respectively.

Since now, the possibility of specific BE is computed using fuzzy evidence theory. In order to find the probability of BE, Eq. (10) is utilised. Therefore, for the above-mentioned value, we have:
$K=\left(\frac{1}{0.127}-1\right)^{\frac{1}{2}} \times 2.301=4.375$

Probability $=\frac{1}{10^{4.375}}=4.20628 \mathrm{E}-05$

# 2.5. Bayesian Modelling and Calculation 

### 2.5.1. Bayesian Modelling

### 2.5.1.1. Bayesian network

Like fault trees, Bayesian network (BN) uses graphical method, to provide robust probabilistic method of reasoning under uncertainty. This has been widely utilised in varieties of engineering fields such as aerospace, maritime, chemical process, and offshore system, as reported by Kabir et al. (2018b), Abbassi et al., (2016), Baksh et al., (2015), Bobbio et al., (2001), and Zarei et al. (2017). BN is referred to as directed acyclic graph having nodes that represent variables and arcs that is signalling causal relationship among linked nodes. In a BN, root nodes are assigned with prior probability values in the form of prior probability tables, and the conditional probability tables (CPTs) are assigned to the other nodes numerically indicating conditional dependencies (Kabir et al., 2014).

Given the conditional dependency of variables and chain rules, Jensen and Nielsen (2007) posited that BN connotes the joint probability distribution of a set of variables as follows:
$P(U)=\prod_{i=1}^{n-1} P\left(X_{i} \mid X_{i+1}, \ldots, X_{n}\right)$
where $U=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$ and $X_{i+1}, \ldots, X_{n}$ are the parents of $X_{i}$.

The BN uses the Bayes' theorem to revise the occurrence probability (prior) of events given new information, called evidence $E$. Next, to acquire the consequence of probability (posterior) according to Bayes' theorem, BN is used to revise the prior probability of an event (E) as:
$P(U \mid E)=\frac{P(U \cap E)}{P(E)}=\frac{P(U \cap E)}{\sum_{U} P(U \cap E)}$

### 2.5.1.2. Mapping fault tree to Bayesian network

Mapping from the FT to BN involves numerical and graphical tasks. Generally, for graphical mapping, the structure of BN is developed according to FT such that BEs, IEs, and TE are represented as the root nodes, intermediate nodes, and leaf node in the corresponding BN. The nodes of BN are linked with each other as well as corresponding

BE in FT. In the case of numerical mapping, probability of occurrence for each BE is assigned to respective root node as prior probabilities. CPTs are populated for each intermediate node and the leaf node according to the behaviour of the logic gates they represent (e.g., see Khakzad et al. (2013a), (2011); Yuan et al. (2015) for more details). Once a BN model is created for a FT, forward and backward analysis can be performed on the model. In the forward analysis, probability of the TE of the FT (leaf node in BN) is evaluated based on the prior probabilities of the BEs by following the BN arcs. Conversely, backward analysis is executed by following BN arcs in alternate direction, i.e., from leaf node towards the root nodes. This analysis can help to determine posterior probabilities of the BEs of FT given the evidence that the TE has occurred. Importance measures of BEs can also be calculated with the help of this analysis. In order to get further details one can refer to Bobbio et al. (2001) and Khakzad et al. (2011).

# 2.5.2. Sensitivity Analysis 

Probabilistic risk assessments using FTA represent a numerical occurrence probability estimation of BEs, which subsequently provides a numerical approximation of occurrence probability of outcome events, including IEs and TE without recognising which BE has most significant contribution as an input in the FTA. Accordingly, sensitivity analysis (SA) is capable of providing quantitative assessment to identify critical input events, thus allowing improving system model to enhance system reliability by recognising weakest part of the system. In addition, SA helps assessors to identify the important sources of variability as well as uncertainty during the risk assessment procedure. Frey and Patil (2002) reviewed different methods of SA, which has the capability to be represented in analytical, graphical, and statistical way. Analytical SA measures the sensitivity of an output to the range of a variation of an input. Statistical SA evaluates the varying contributions of one or more input events on the outputs at an exact time, and finally the graphical SA method presents a visual and perceptible illustration of contribution of individual input event to an output event.

In this study, the proposed SA method in FTA is based on analytical evaluation named Birnbaum importance measure (BIM). BIM of a BE is calculated as the difference of the occurrence probability of the TE by considering the probability of the BE as 1 and 0 , respectively. For classical FTA, the equation to calculate BIM is:

$$
I_{B E_{i}}^{B I M}=P\left(T E \mid P\left(B E_{i}\right)=1\right)-P\left(T E \mid P\left(B E_{i}\right)=0\right)
$$

Where $I_{B E_{i}}^{B I M}$ is the BIM of the basic event $B E_{i}, P\left(T E \mid P\left(B E_{i}\right)=1\right)$ is the probability of the TE given that the probability of the $B E_{i}$ is 1 and $P\left(T E \mid P\left(B E_{i}\right)=0\right)$ is the probability of the TE given that the probability of the $B E_{i}$ is 0 (Rausand and Hoyland, 2004).

Using the BN model, BIM of an event can be calculated as:

$$
I_{B E_{i}}^{B I M}=P\left(T E \mid B E_{i}=\text { True }\right)-P\left(T E \mid B E_{i}=\text { False }\right)
$$

Where $P\left(T E \mid B E_{i}=\right.$ True $)$ is the probability of the TE as ordered by evidence on the BN node representing $B E_{i}$ as true and $P\left(T E \mid B E_{i}=\right.$ False $)$ is the probability of the TE by observing the BN node representing $B E_{i}$ to be false.

For the purpose of comparison, we used another importance measure technique called the ratio of variation (RoV) (Zarei et al., 2017). When the posterior probabilities of the BEs are known, the RoV identifies the critical components by calculating the percentage variation of posterior probability from the prior probability. Mathematically, it is calculated as:

$$
\operatorname{RoV}\left(B E_{i}\right)=\frac{\pi\left(B E_{i}\right)-\theta\left(B E_{i}\right)}{\theta\left(B E_{i}\right)}
$$

where $\pi\left(B E_{i}\right)$ and $\theta\left(B E_{i}\right)$ represent posterior and prior probabilities of basic event $B E_{i}$, respectively.

Although, sensitivity analysis is a complicated task to recognise the significant BE for large and complex system in order to mitigate the overall risk of specific systems, nevertheless, this analysis examines how the results of a computation or model vary as individual assumptions are changed. Furthermore, it can help the assessors to understand the dynamics of the system.

# 3. APPLICATION OF THE PROPOSED METHODOLOGY AND DISCUSSION 

Complex chemical process industries contain varieties of hazardous chemicals and process zones, which are extremely congested with the existence of complex assets such as towers, furnaces, heat exchangers, and many other equipment for process operations. Such complex assets have enough capability to change rapidly from small

mishaps into the catastrophic accident. It is obvious that fires and explosions have high frequency throughout all process accidents, which can be considered as loss-producing events. For example, a series of fire and explosion on April 2, 2010 at Tesoro Anacortes Refinery in United States of America, which was caused by a fracture in the heat exchanger at the catalytic Reformer/Naphtha Hydrotreater unit. Is has been recorded as the largest destructive accident ever after the BP Texas city accident of March 2005. This fracture occurred at the E-6600E heat exchanger due to surge in the high temperature hydrogen attack (HTHA). The fractured heat exchanger released highly flammable hydrogen and naphtha of over $500^{\circ} \mathrm{F}$. The flammable hydrogen and naphtha sparked subsequently triggering an explosion and terrible fire that lasted for more than 3 hours (U.S. Chemical Safety and Hazard Investigation Board, 2014). In this paper, the proposed methodology was applied to release prevention barrier (RPB) among seven investigated barriers reported by the Chemical Safety Board (CSB) on accident pathway prevention. A brief definition of the seven barriers provided by Adedigba et al. (2016b) demonstrated that failure of RPB is responsible for the release of material and consequently responsible for the spill of chemical substance that triggers the accident. The FT of RPB provided by Adedigba et al. (2016b) is modified in our study to quantify the probability of the prevention barrier and represent the effectiveness and viability of the proposed approach. As it can be seen from Fig. 2, the TE of FT is the failure of RPB. Accordingly, to establish a causal relationship, the IEs are considered to represent all contributory factors for RPB. Their respective failure probabilities contribute to the failure probability of the TE while the BEs of accident contributory factors is denoted by circles and a combination of logic gates (AND/OR) was used to show the logical relationship between BEs and the TE.

Fig. 2. Fault tree for the release prevention barrier (modified after Adedigba et al. (2016b))

The description of all BEs of FT in Fig. 2 for RPB is provided in Table 3.

Table 3. List of BEs of FT of Fig. 2 (restructured after Adedigba et al. (2016b))

In order to obtain the possibility of each BEs, three independent experts are employed. Because of the many advantages of a heterogeneous group of expert over a homogeneous one as pointed out by Lavasani et al. (2015b) and Yazdi et al. (2017a), a heterogeneous group of experts including three specialists with different backgrounds was employed to compute the FP of BEs. The categories of employed experts are:

Expert 1: An experienced risk assessor and safety analyser working as consultant for complex chemical plant for 9 years with a PhD certificate on chemical process engineering.

Expert 2: A senior chemical process designer working as process controller for 13 years from a process-engineering department with a master degree in chemical control engineering.

Expert 3: An experienced safety engineer working as safety expert for 6 years in different types of process industries with a BSc certificate in occupational safety engineering.

According to section 2.3, entropy technique is used for experts weighting by considering three criteria including experience, education level, and job field closeness. Therefore, the weighing scores: $0.347,0.380$, and 0.219 are given to E1, E2, and E3, respectively.

To demonstrate the fuzzy evidence theory approach, three unbiased and independent experts expressed their opinions in qualitative terms based on Table 1. Table 4 provides the elicited knowledge according to engaged experts for the possibility of BEs in the FT.

Table 4. Expert knowledge in fuzzy scale for each BE according to fuzzy evidence theory approach

Using fuzzy evidence combination rule as explained in section 2.4.3, the output of qualitative terms based on experts' opinions and FP of identified BEs are shown in Table 5.

Table 5. Failure probability of basic events of the FT of Fig. 2

Fig. 3. BN model of the FT of Fig. 2

To probabilistically evaluate the FT of Fig. 2, it was mapped to a BN model as seen in Fig. 3. Prior probabilities of the root nodes of BN are provided from the failure probability values of the BEs from table 5. The leaf node "TE" identifies the event at the top of the FT. Querying on this node gives the probability of the occurrence of the TE and the value obtained was $1.73841 \mathrm{E}-11$. The posterior probability of the BEs of the FT can be obtained and updated by providing evidence on the leaf node, and thereby running a backward analysis. Table 6 shows the updated belief concerning the FP of the BEs and these values are obtained by observing BN node "TE" to be true, i.e., considering

there is an evidence that the TE occurs. Based on these updated beliefs, new analysis was performed to obtain new information about the TE probability. The new value obtained for the TE probability was 0.85954 .

Table 6. Posterior probability of the BEs of FT

Sensitivity of the BEs of the FT was analysed using both the concept of Birnbaum importance measure and rate of variation in probability values as described in section 2.5.2. The BEs were ranked in accordance to their contribution to the top event occurrence and the result is shown in Table 7. As seen in the table, both sensitivity analysis methods identified BE. 15 as the most critical event, which corresponds to the "Long delay in inspection schedule". The next two most critical events as identified by the approaches are BE. 9 and BE.10, respectively. BE. 9 and BE. 10 represent "Poor construction material for NHT heat exchanger" and "High mechanical stress", respectively. On the other hand, the approaches identified BE.12, BE.13, BE.14, and BE. 20 as the least critical events.

Table 7. Sensitivity analysis of the basic events of the FT

The application of the proposed approach demonstrated that the approach is capable of handling both epistemic and aleatory uncertainty during risk assessment using FTA. It is important to note that in the past several approaches have been developed for operational and dynamic risk assessment in different domains. These approaches have their own strengths and weaknesses. Many of these approaches rely on exact known failure data for risk assessment, thus do not take into account the scenarios when exact data may not be known. There are approaches that have addressed the issue of data and model uncertainties in an isolated manner. The proposed approach makes a complementary contribution to the existing risk assessment approaches by combining expert judgement, fuzzy set theory, evidence theory, and Bayesian networks to handle both epistemic and aleatory uncertainties, which will enhance or help enabling the dynamic risk assessment under the conditions of uncertainty. For instance, the data uncertainty handling capability of the proposed approach can be used by the approaches that assume that the failure data are always known, thus will allow those approaches to perform analysis with unknown data. In Table 8, we provide a comparison between different recently developed dynamic risk assessment approaches in process industry, including the proposed one. The comparison mainly highlights the features and capabilities provided by the approaches, which will help to understand how the proposed approach may enhance the capability of the existing approaches.

Table 8. Comparison of the features of the recent approaches for risk assessment in process industries

# 4. CONCLUSION 

Classical FTA requires precise probabilities and independence assumption of events, which are rare and often unrealistic for process systems. The uncertainties in failure data (e.g., missing data, uncertainties in expert knowledge, and diverse sources of expert opinions) coupled with model adequacy make it challenging to perform a credible quantitative FTA and it may produce misleading results. To address the issues of both aleatory and epistemic uncertainties in FTA, a methodology has been proposed in this paper by combining expert knowledge, fuzzy set theory, evidence theory, and Bayesian networks. In the approach, the failure possibilities of basic events of fault trees are evaluated by using linguistic variables, which can model experts' opinions in a more intuitive way. Afterwards, opinions of different experts are combined using fuzzy evidence combination rules to transform experts' linguistic judgement regarding events' failure possibilities into the numerical failure probabilities of events. In the combination process weights of experts were taken into account. The use of Bayesian networks for the quantification of fault trees allows to accurately model dependencies between events. More importantly, incorporating new knowledge or evidence to the input events through a diagnostic analysis of BNs yields updated beliefs about the likelihood of the events, provides posterior probabilities of the events, which are more specific to the failure scenario examined and more accurately reflects its properties. The application of the proposed approach has been demonstrated in FTA of a release prevention barrier in a process system.

The proposed approach is particularly useful for risk assessment of process systems where data and dependency uncertainty exists. Using the sensitivity analysis, the system analysts can identify the critical components or weakest parts of the system model by running a diagnostic analysis of the Bayesian network model of the fault tree, which can help them to determine necessary actions to minimise the likelihood of risks caused by those critical parts of the system.

However, the authors faced some challenges during the study. Several inconsistencies occurred while satisfying fuzzy operation rules during expert elicitation of opinions using fuzzy evidence theory. In this regards, it takes more time than conventional evidence theory approach. In addition, to acquire more realistic results, it is required that

more experts are employed. Accordingly, the combination of all possible power set will increase geometrically, which will make the approach time consuming. Nonetheless, the authors believe that the significant output of any risk assessment method is improving the safety performance of the system. In this regards, finding critical BEs and providing corrective action calls for the reduction in the probability of each BE and subsequently TE. Therefore, the safety performance of the system will be improved.

At present, we consider binary states of the system component. In the future, we plan to investigate the risk assessment problem for multistate systems. In addition, we plan to explore different types of probability density functions such as Weibull, lognormal etc. to develop more robust fuzzy evidence theory based approach for FTA. In this study, as the combination of fuzzy set theory and evidence theory are used, it was not possible to measure the relative performance of the new approach in uncertainty handling. In the future, applying both approaches in parallel and using coefficient factor integration, it may be possible to illustrate the relative strength and weaknesses of the approaches. However, the challenge is that an SA should be applied to well-understand the behaviour of both approaches. This task could be time consuming for complex systems. In terms of application, currently we applied the approach to a process system; however, in future, the robustness of the approach can be verified by applying it in other engineering fields or other case studies in the process industry.

Acknowledgment. The research of Sohag Kabir was partly funded by the DEIS project (Grant Agreement 732242).

# Nomenclature 



Symbols


