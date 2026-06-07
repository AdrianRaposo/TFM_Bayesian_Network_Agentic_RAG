# Addressing the epistemic uncertainty in maritime accidents modelling using Bayesian network with interval probabilities 

Zhang, Guizhen; Thai, Vinh V.; Yuen, Kum Fai; Loh, Hui Shan; Zhou, Qingji

2017

Zhang, G., Thai, V. V., Yuen, K. F., Loh, H. S., \& Zhou, Q. (2017). Addressing the epistemic uncertainty in maritime accidents modelling using Bayesian network with interval probabilities. Safety Science, 102, 211-225. doi:10.1016/j.ssci.2017.10.016
https://hdl.handle.net/10356/105418
https://doi.org/10.1016/j.ssci.2017.10.016

[^0]
[^0]:    (c) 2017 Elsevier Ltd. All rights reserved. This paper was published in Safety Science and is made available with permission of Elsevier Ltd.

# Addressing the Epistemic Uncertainty in Maritime Accidents 

## Modelling using Bayesian Network with Interval Probabilities

Guizhen Zhang ${ }^{1}$; Vinh V. Thai ${ }^{2} *$; Kum Fai Yuen ${ }^{3}$; Hui Shan Loh ${ }^{4}$; Qingji Zhou ${ }^{5}$<br>*Corresponding author

1. Nanyang Environment and Water Research Institute, Interdisciplinary Graduate School, Nanyang Technological University, 1 Clean tech Loop, Singapore 637141. Email: gzhang004@e.ntu.edu.sg
2. School of Business IT \& Logistics, RMIT University, 124 La Trobe St., Melbourne, VIC 3000 Australia. Email: vinh.thai@rmit.edu.au
3. Department of International Logistics, College of Business \& Economics, Chung-Ang University, 84 Heukseok-ro, Heukseok-dong, Dongjak-gu, Seoul, 156756, South Korea. Email: yuenkf@cau.ac.kr4. Logistics and Supply Chain Management Programme, School of Business, Singapore University of Social Sciences, 461 Clementi Road, Block C, Singapore, 599491, Singapore. E-mail: hsloh@suss.edu.sg
4. School of Civil and Environmental Engineering, Nanyang Technological University, Blk N1.1-B3-01, 50 Nanyang Avenue, Singapore 639798, Singapore. E-mail: ajzhou@ntu.edu.sg


#### Abstract

Bayesian Network (BN) is often criticized for demanding a large number of crisp/exact/precise conditional probability numbers which, due to the lack of available statistics, have to be obtained through experts' judgment. These exact probability numbers provided by the experts often carry a high level of epistemic uncertainty due to the incompleteness of human knowledge, not to mention the difficulty in obtaining them in the first place. The existence of uncertainty in maritime risk modelling is well recognized but

relatively unexplored. This paper seeks to fill the gap by exploring the extension of BN with interval probabilities to the modelling of maritime accidents, which allows for the quantification of the epistemic uncertainty. Ship collision was selected as the case study due to its strategic importance in navigational safety. The user-friendly linguistic terms defined with interval scales were used for eliciting interval conditional probabilities from industry experts. Inferences were made directly with the interval probabilities using the Generalized Loopy 2-Updating (GL2U) algorithm. Meanwhile, the interval probabilities were converted into point probabilities and computed with the traditional BN method for comparison, which were all shown to be within the ranges of the calculated posterior intervals probability. Results with inputs from different experts reveal discrepancies, which in turn verifies the existence of uncertainty in risk modelling. A discussion was also provided on how the uncertainty in risk assessment propagates to the decision-making process and influences the ranking of potential risk control options.

Keywords: Interval probabilities; Bayesian network; Maritime accidents; Experts’ elicitation; Epistemic uncertainty

# 1 INTRODUCTION 

### 1.1. Maritime accidents and $B N$

Maritime accidents have continued to occur, which threaten the safety of seafarers at sea, the economic performance of shipping companies and the environment. Therefore, understanding why and how accidents happen is of great importance for future safety management. Since accidents cannot be completely avoided, the reasonable goal is to control the accident risk to a desired level. Risk assessment is essential for this purpose. By performing risk analysis, we can evaluate the safety level of the current system as well as identifying the most critical issues. Some risk assessment methods also enable the evaluation of risk control options and thus ascertaining the most cost-effective way for reducing the risk level. Many risk analysis

methods have been developed in the past few years, including Hazard and Operability Studies (HAZOP), Failure Mode and Effects Analysis (FMEA), Event Tree Analysis (ETA), Fault Tree Analysis (FTA) and Bayesian Belief Network (BN). Each of these risk analysis tools has its unique characteristics and fits different purposes.

BN is becoming an increasingly popular methodology for risk analysis of the maritime transportation system in recent years due to its capability to model causal interdependence, to incorporate of experts' knowledge when statistical data does not exist, to make dynamic updates when new observation is made, and to include human and organizational factors. (Helle et al. 2011, Lehikoinen et al. 2015) (Montewka et al. 2014) (Banda et al. 2016) and (Zhang et al. 2013) are a few examples of BN applications in the maritime risk analysis field. A more detailed review of the literature on maritime accidents risk prediction based on Bayesian Network can be referred to (Goerlandt and Montewka 2015b) as well as (Zhang and Thai 2016). BN was also recommended for risk assessment (Step 3 of the Formal Safety Assessment, FSA) to International Maritime Organization (IMO) (IMO; 2006). The application of BN includes three steps, i.e. BN structure development, parameterization, and inferences. Both the BN structure and parameters could be built manually, automatically or a combination of both (Neil et al. 2000) (Kjrćulff and Madsen 2013) (Neil et al. 2000).

# 1.2. Uncertainty and BN modelling 

The consideration of uncertainties is crucial for obtaining reliable results in risk analysis (Merz and Thieken 2005). By sources, uncertainties could be broadly separated into two class: aleatory and epistemic uncertainty, the comparison of which could be found in table 1.

Table 1 Comparison of aleatory uncertainty and epistemic uncertainty



(Liu et al. 2003) reviewed some of the most important uncertainty reasoning approaches, including the Bayesian theory of probability, Dempster-Shafer theory of evidence, and fuzzy set theory. Each of these approaches views and handles uncertainties from different perspectives. Bayesian Theory has many good features such as strong theoretical root, less computational complexity compared with other approaches. It models aleatory uncertainty through probability but could not include epistemic uncertainty since each entity must be assigned with exact probability numbers.

In the practice BN modelling, especially for applications to the maritime risk assessments due to the lack of available statistical data, experts' opinion is an important source for the probability specification or parameterization. This, however, poses huge challenges for the reliability of the model as well as the involved domain experts. First, for probability elicitation, the experts are often asked about the conditional dependence between the model

elements on top of their own expertise. Moreover, the requirement to elicit a large number of probability numbers adds to the workload of the experts. From the viewpoint of modelling, the involvement of experts will lead to epistemic uncertainty, due to the lack of knowledge about the system (Liu et al. 2003) (Merrick et al. 2005) (Fallet et al. 2011), which can sometimes be referred to as quantities which have fix values, but their exact value are unknown (Swiler et al. 2009).

The lack of systematic consideration of uncertainty in the applications of maritime transportation risk analysis was identified through a detailed review in (Goerlandt and Montewka 2015b), even though the existence of uncertainties are well recognized and accepted. One exception was (Merrick et al. 2005) which used Bayesian approach to estimate the impacts of parameter uncertainties in the traffic simulation model (not the risk analysis model) for evaluating the ferry expansion alternatives. In the last few years, there has been more studies with focus on uncertainties in the maritime risk models. For example, (Sormunen et al. 2014) showed through an extensive study that the uncertainties in accident and risk models can be significant. (Goerlandt and Montewka 2015a) went one step further by introducing a framework where uncertainties are qualitatively assessed. However, so far, there are no studies on maritime risk analysis which quantitatively address the epistemic uncertainties. The objective of this paper is to provide a way to model the epistemic uncertainties related with the probability parameters in Bayesian Network models for maritime risk analysis.

To achieve the objective, this paper seeks to extend BN by including interval probabilities. Interval probability expresses imprecision in a more straightforward way. (Fallet et al. 2011) concluded that the interval probability method best represents the experts' knowledge due to more appropriate semantics as compared to hard evidence, soft evidence, and total ignorance. In applications, obtaining interval probability parameters are much easier than getting point

probabilities, especially when there is only little, incomplete or conflicting information available to assist experts' judgment (Guo and Tanaka 2010). In other cases, when multiple experts are involved, each expert may indicate their own belief and if no consensus could be reached, the result are interval probabilities (Cozman 2000). Considering these facts, the application of interval probability (with an upper bound and lower bound) in BN could bring more application value.

# 1.3. Organization of this paper 

The rest of this paper is organized as follows. Section 2 defines interval probability, discusses its properties and summarizes the updating algorithm for BN with interval probabilities. Section 3 presents the application of BN with interval probabilities to ship collision causation probability modelling. The detailed elicitation process is also discussed in this section. Section 4 shows the inference result with the interval probabilities. An example of the influence on the evaluation of risk control options with interval probabilities is provided as well. Finally, Section 5 summarizes the paper.

## 2 METHODOLOGY

This paper extends the traditional BN to include interval probability parameters for maritime risk modelling. Inferences are made directly with interval parameters. The following subsections present the definition of credal network, interval probability and the relative properties.

### 2.1.Credal network and $B N$ with interval probability parameters

BN with interval probabilities is a special type of credal network, which extends BN to deal with imprecision and uncertainty (Corani et al. 2012). A credal network over a set of random variables $\mathbf{X}=\left(\mathrm{X}_{1}, \ldots, \mathrm{X}_{\mathrm{k}}\right)$ is $\left\langle\mathrm{G},\left\{\mathbf{P}_{\mathbf{1}}, \ldots, \mathbf{P}_{\mathbf{m}}\right\}\right\rangle$, where G is a directed acyclic graph whose nodes have one-to-one correspondence to the elements in $\mathbf{X}$, and $\left\langle\mathrm{G}, \mathbf{P}_{j}\right\rangle$ is a BN over $\mathbf{X}$ for

each $j=1, \ldots$, m (Antonucci 2008) (Antonucci and Zaffalon 2008). This definition indicates that a credal network could be regarded as a set of BNs, as illustrated in Figure 1.
![img-0.jpeg](img-0.jpeg)

Figure 1a Simple example of BN
Figure 1b Simple example of Credal Network

Figure 1a is an example of the traditional BN where all the probabilities are exact numbers. Figure 1 b is a credal network with the same structure. The probabilities in the credal network are imprecise, being an interval or comparisons of the probabilities, which enables the representation of classificatory and comparative probability judgements (Piatti et al. 2010). For example, for node A, the judgement $1<\mathrm{P}(\mathrm{a}) / \mathrm{P}(\neg \mathrm{a})<3$ means that the chance of $\mathrm{A}=a$ is one to three times higher than the chance $\mathrm{A}=\neg a$. For node B , the probability of $\mathrm{P}(\mathrm{b} \mid \mathrm{a})$ could be any value between 0.2 and 0.3 . The BN in Figure 1a is just one among many others that satisfy the probability conditions of the credal network in Figure 1b. The inference with a credal network is the same with inferences with its vertices (Antonucci 2008). However, the number of vertices is exponential to the input size except for the case of binary nodes. The complexity in inference for credal network is thus greatly increased than traditional BN.

# 2.2.Definition and properties of interval probability 

For a random variable X which takes values from a finite set $\left\{x_{1}, \ldots, x_{n}\right\}$, the intervals $\mathrm{L}=\left\{\mathrm{L}_{i}=\left[\mathrm{L}\left(a_{i}\right), \mathrm{U}\left(a_{i}\right)\right], i=1,2, \ldots, \mathrm{n}\right\}$ are called the interval probability (Guo and Tanaka 2010) (Hu et al. 2012) if and only if for any $P\left(a_{i}\right) \in \mathrm{L}_{i}$, there exists $P\left(a_{j}\right) \in \mathrm{L}_{j}$, such that,

$$
P\left(a_{i}\right)+\sum_{j=1,2, \cdots i-1, i+1, \cdots n} P\left(a_{j}\right)=1
$$

L will satisfy (1) if and only if they satisfy (2) and (3), where $i, j \in[1, \ldots, n]$ ) (Tessem 1992) (de Campos et al. 1994) (Weichselberger 2000) (Guo and Tanaka 2010):(Tessem 1992) :

$$
\begin{aligned}
& \sum_{\substack{i=1 \\
i \neq j}}^{n} L\left(a_{i}\right)+U\left(a_{j}\right) \leq 1 \\
& \sum_{\substack{i=1 \\
i \neq j}}^{n} U\left(a_{i}\right)+L\left(a_{j}\right) \geq 1
\end{aligned}
$$

Normally, the elicited interval probabilities may or may not satisfy (2) and (3). However, it is easy to check whether they satisfy condition (4):

$$
\sum_{i=1}^{n} L\left(a_{i}\right) \leq 1 \leq \sum_{i=1}^{n} U\left(a_{i}\right)
$$

Condition (4) is a necessary but insufficient condition of (2) and (3). The intervals that satisfies condition (4) are called semi-interval probabilities, denoted with $\left[\mathrm{L}^{\prime}\left(a_{i}\right), \mathrm{U}^{\prime}\left(a_{i}\right)\right]$. Interval probabilities could be elicited from $\left[\mathrm{L}^{\prime}\left(a_{i}\right), \mathrm{U}^{\prime}\left(a_{i}\right)\right]$ by solving the linear programming problem as shown in function (5) (Guo and Tanaka 2010) :

$$
\begin{aligned}
& \text { Max } \sum_{i=1,2, \ldots, n}^{n}\left(U\left(a_{i}\right)-L\left(a_{i}\right)\right) \\
& \text { s.t. } \sum_{\substack{i=1 \\
i \neq j}}^{n} L\left(a_{i}\right)+U\left(a_{j}\right) \leq 1, \quad \sum_{\substack{i=1 \\
i \neq j}}^{n} U\left(a_{i}\right)+L\left(a_{j}\right) \geq 1 \\
& U\left(a_{i}\right) \geq L\left(a_{i}\right), \quad U\left(a_{i}\right) \leq U^{\prime}\left(a_{i}\right), \quad L\left(a_{i}\right) \geq L^{\prime}\left(a_{i}\right)
\end{aligned}
$$

In the case of binary variables $(n=2)$. When $j=1$, we can obtain (6) and (7):

$$
\begin{aligned}
& L\left(a_{2}\right)+U\left(a_{1}\right) \leq 1 \\
& U\left(a_{2}\right)+L\left(a_{1}\right) \geq 1
\end{aligned}
$$

Similarly, when $j=2$, we can obtain (8) and (9):

$$
\begin{aligned}
& L\left(a_{1}\right)+U\left(a_{2}\right) \leq 1 \\
& U\left(a_{1}\right)+L\left(a_{2}\right) \geq 1
\end{aligned}
$$

Combining (6) and (9), $\mathrm{L}\left(a_{2}\right)+\mathrm{U}\left(a_{1}\right)=1$; similarly, from (7) and (8), $\mathrm{L}\left(a_{1}\right)+\mathrm{U}\left(a_{2}\right)=1$ (Hall et al. 2005), which implies that the boundary for one state could be inferred from the boundary of the other. For example, if $L_{1}$ is $\left[L\left(a_{1}\right), U\left(a_{1}\right)\right]=[0.3,0.6]$ for $a_{1}$, then $L_{2}$ can be calculated as $\left[L\left(a_{2}\right), U\left(a_{2}\right)\right]=[1-0.6,1-0.3]=[0.4,0.7]$. The calculated interval probability not only speeds up the elicitation process but also ensures consistency.

# 2.3.Combination of experts' opinion 

When multiple experts are consulted for probability elicitation, either group consensus or individual opinions may be obtained as the output. The individual judgement can be combined in various ways, from simply adopting a large interval to using the simple or weighted average. The weighted average method was adopted in this study. Here, a weight number is assigned to each judgment, i.e. each interval probability, rather than to each expert. Therefore, the weight for the same expert may vary for the different judgments they made. It

is assumed that more weights should be assigned when one judgment is closer to other judgments. More specifically, the weight of the interval probability specified by one expert is reciprocally proportional to the distance between the interval to all other intervals specified by other experts. The distance $\mathrm{L}^{\mathrm{b}}$ between interval $\left[\mathrm{L}^{\mathrm{b}}\left(a_{i}\right), \mathrm{U}^{\mathrm{b}}\left(a_{i}\right)\right]$ and all other intervals $\left[\mathrm{L}^{j}\left(a_{i}\right), \mathrm{U}^{j}\left(a_{i}\right)\right]$, where $j=1,2 \ldots \mathrm{~b}-1, \mathrm{~b}+1, \ldots \mathrm{~m}$ ( $m$ is the total number of experts) is calculated as follows (Hu et al. 2012):

$$
L^{b}=\frac{1}{m-1} \sum_{\substack{j=1 \\ j \neq b}}^{\infty} \sqrt{\left(L^{j}\left(a_{i}\right)-L^{b}\left(a_{i}\right)\right)^{2}+\left(U^{j}\left(a_{i}\right)-U^{b}\left(a_{i}\right)\right)^{2}}
$$

As such, the weight for expert $b$ was defined as $k / L^{b}$, where $k$ is a constant number. All the weights should add up to 1 , i.e.:

$$
\sum_{\mathrm{b}=1,2, \ldots, \mathrm{~m}} k / L^{b}=1
$$

From equation (11) value of $k$ could be calculated. The weight assigned in this method is objective. The combined interval probability is closer to the majority of judgments.

# 2.4.Updating BN with interval probabilities 

Updating credal networks is much more complicated than updating the traditional BN. For simplicity, (Hu et al. 2012) converted the interval probabilities to exact probability number and then apply traditional BN method for analysis. Similarly, (Ge et al. 2013) decomposed the interval-valued BN into two traditional point-valued BNs, one with the upper bound and one with the lower bound values, using the BN software GeNie (Bayesian Fusion) to make inferences. Meanwhile, many algorithms have been proposed for making inferences directly using interval probability in belief networks. Hall et al., (2005) used Support Logic Programming (SLP) and Interval Probability Theory (IPT) for analysis of interval probabilities in BN in the study about flood and climate change. (Liu and Yue 2011)

extended the Gibbs sampling algorithm to the updating of interval probabilities. (Antonucci et al. 2013a) proposed a linear programming method for approximate updating of credal networks.

The 2U algorithm extended from Pearl's BN updating algorithm is a widely used algorithm (Fagiuoli and Zaffalon 1998). It is an exact algorithm for updating of binary polytree credal networks. (Ide and Cozman 2004) extended the 2U method to multi-connected networks, i.e. Loopy 2U. Even though 2U is an exact algorithm, L2U is only an approximate algorithm. L2U performs best compared to theother approximate inference methods: IPE (Iterated Partial Evaluation) and SV2U (Structured Variational methods) in terms of time and accuracy. GL2U further develops L2U to deal with nonbinary credal network through the binarization algorithms which transfers any credal network into an equivalent binary credal network (Antonucci 2008, Antonucci et al. 2010). The only approximation in GL2U is related to the loopy step. In this paper, the GL2U algorithm is applied for calculation and analysis. More details of the GL2U algorithm could be found in (Antonucci 2008, Antonucci et al. 2010).

# 3 APPLICATION OF BAYESIAN NETWORK WITH INTERVAL PROBABILITIES TO MARITIME ACCIDENTS MODELLING 

### 3.1.Reviews of risk assessment models for ship collision accidents

Ship collision is chosen for case study for its strategic importance on navigational safety (Kuehmayer 2008) (Kujala et al. 2009). For collision risk modelling, analysts adopt quite different perspectives and approaches. There are quantitative as well as qualitative methods. Some authors consider probability and consequence separately while some adopt integrated approaches. Risk indicator, probability numbers are among some of the measurements. Readers can be directed to (Goerlandt and Montewka 2015b) for a more detailed discussion. In this paper, one of the most widely used probabilistic risk approach is used for the case

study, where collision probability is calculated as the product of the Geometric probability and causation probability. The most common approach is to calculate the collision probability as the product of the Geometric probability and causation probability (Li et al. 2012). (Kuehmayer 2008).

$$
P=P_{a} \times P_{c}
$$

Geometric probability refers to the probability of a ship becoming a collision candidate, for whom a collision would happen if no further evasive actions are taken. Causation probability is the probability that a collision candidate fails to conduct any aversive actions and thus results in grounding or collision. Geometric probability and causation probability are normally calculated separately and then multiplied together. Geometric probability is calculated either adopting analytical models (Fujii et al. 1974) (Pedersen 2010) or using dynamic models with system simulation of the real traffic (Goerlandt and Kujala 2011). Meanwhile, causation probability is computed with accident statistics, adjusting previous values elicited from experts' opinion, modelled with Fault Tree Analysis and BN (Mazaheri 2009). (Fujii et al. 1974), or using dynamic models with system simulation of the real traffic. To estimate collision frequency for a specific geographical location, detailed geometric models are needed while assumed values of causation probabilities are adopted. On the other hand, for understanding accident causal relations, detailed causation probability model is essential. The focus of this research is on the latter, i.e. modelling of causation probability.

# 3.2.BN model structure for Ship Collision causation probability 

Detailed collision causal narratives can be found from accident investigation reports by marine accident investigation authorities such as Marine Accident Investigation Branch UK (MAIB), Transportation Safety Board of Canada (TSB) and Australian Transport Safety Bureau (ATSB), which records, rebuilds and analyzes each accident in details. For BN structure construction, the accident causal chain (Grabowski 2000), Reason's Swiss cheese

model and the Human Factors Analysis and Classification System (HFACS) have been used as theoretical frameworks (Ren et al. 2008) (Ren et al. 2009) (Akhtar and Utne 2014). The BN model structure in this research was built after reviewing many accident reports. References to previous models in the literature were also made, especially the model by (Friis-Hansen and Simonsen 2002), and (Det Norske Veritas 2003).

Under a critical encounter situation, the three important cognitive functions for successful collision avoidance identified by (Leva et al. 2006) are: Detection-Interpretation, Interpretation-Planning and Execution of the actual maneuvering. Similarly, (Montewka et al. 2017) decomposed the evasive action into three components, i.e. detection, assessment and action. These concepts were adopted in the present model. Three nodes were incorporated, including "Detection", "Maneuver planning" and "Maneuvering", corresponding to the three cognitive functions. Successful "Detection" could be achieved through "Navigation system detection", "Visual detection" or "Vessel Traffic Service (VTS) detection". Meanwhile, successful detection is the prerequisite for correct "Maneuver planning", which in turn is the prerequisite for correct "Maneuvering" action. Collision is determined by the combined impact of the "Maneuvering" action from both encountering ships. The logic is reflected in the conditional probabilities, as in Table 2.

Table 2 Conditional probability for the node "Detection"


The various causal factors such as vessel specifications, route characteristics, weather conditions, human and organizational factors were incorporated into the model by exerting influence on the critical functions (Mazaheri 2009). Since the two-ship collision scenario is

modelled in this research, two sets of variables with the same definition and same causal structure corresponding to each ship were used in the model. The total number of nodes was controlled to a manageable size considering the elicitation workload. The detailed model is presented in Figure 2.
![img-1.jpeg](img-1.jpeg)

Figure 2 Collision model based on causal relations
The eight nodes i.e. "Time of day", "Visibility", "Weather", "VTS Presence", "VTS Detection", "Navigational complexity", "Communication between ships" and "Collision" are the common variables influencing both ships.

The states and a brief description for all nodes in the model are presented in Table 3.
Table 3 Causal factors of the ship collision model



# 3.3.The elicitation of conditional probabilities from experts 

Due to the lack of statistical data, experts' elicitation plays an important role in obtaining the conditional probability numbers. A detailed literature review on probability elicitation in Bayesian Network modelling of maritime accidents was conducted in a recent study (Zhang and Thai 2016). In this research, to alleviate the elicitation workload, several techniques were employed. First, for the two sets of similar variables, elicitation was only needed for one set as the result of which applies to the other set. Second, since all nodes in the collision model are binary nodes, elicitation is performed for one state only. The interval probability for the other state could be computed using $\mathrm{L}\left(\mathrm{a}_{2}\right)+\mathrm{U}\left(\mathrm{a}_{1}\right)=1$ and $\mathrm{L}\left(\mathrm{a}_{1}\right)+\mathrm{U}\left(\mathrm{a}_{2}\right)=1$, as discussed in section 2.1. Third, for the node "Detection", the probability was specified according to logic. For individual probability elicitation, either direct or indirect methods can be used (Kuhnert et al. 2010), such as the probability wheel, the probability scale (Renooij 2001), the gambling analogy, Analytical Hierarchy Process (AHP) (Wang et al. 2010) and the fuzzy methods (Ren et al. 2008, Ren et al. 2009). Among them, linguistic terms such as "Likely", "Very likely", "Virtually certain", "Medium likelihood", "Unlikely", "Very unlikely" and "Extremely unlikely" associated with probability interval were found to be user-friendly (Mastrandrea et al. 2010) (Antonucci et al. 2013b) (Ren et al. 2007). The natural language corresponds to human cognition, and can represent imprecise/vague information. The scaling of linguistic terms from three literature sources were compared in Table 4 and the definition from the first source was adopted in this paper (Mastrandrea et al. 2010).

Table 4 Scales of linguistic terms with appropriate probability intervals



A questionnaire was developed in this research for elicitation, an excerpt of which is shown in Figure 3. The definition of linguistic terms with the corresponding probability intervals were explained both verbally and in a figure to experts. The experts could choose the likelihood from a dropdown list, which is comparatively easy and time-saving.
![img-2.jpeg](img-2.jpeg)

Figure 3 Excerpt of the questionnaire for conditional probabilities elicitation

In total, eleven completed questionnaires were collected after face-to-face interviews with navigational experts in Singapore. The average time of the elicitation process ranges from one to two hours. Assumptions were made for probability distributions for nodes without parent nodes, as demonstrated in Table 5. The Singapore Strait was used as the background for the study. The prior probabilities here are point probabilities although they could also take the form of interval probabilities.

Table 5 Prior probabilities for nodes without parent nodes


# 4 RESULTS AND DISCUSSIONS 

### 4.1.Marginal interval probabilities

Inferences were made directly with interval conditional probabilities using the GL2U algorithm. First, the calculation was performed using the combined interval conditional probabilities obtained from all experts. For comparison, the combined interval conditional probabilities were converted to point probabilities and used as input for computations with the traditional BN method. The results are summarized in Table 6. Column 2 and 5 show the result of the marginal probabilities computed with the traditional BN while Column 3 and 6 list the marginal interval probabilities computed with the GL2U method. It could be observed that all the point probabilities computed with traditional Bayesian network method fall into the probability intervals obtained from the GL2U methods.

Table 6 Prior interval probabilities for all nodes


Figure 4 shows the model with the interval marginal probabilities, where the red bars indicate the interval probabilities. Note that due to the limitation of space, Figure 4 only shows half of the model presented in Figure 2. One of two identical sets of nodes corresponding to each of the encountering ship was not shown in Figure 4. The width of the red bar reflects the ambiguity of the experts' judgement. The wider the red bar, the more ambiguous the result would be. In the extreme cases of point probabilities for some nodes, the width of the red bar is zero, reflecting no ambiguity. For example, the interval probability for "Detection=Yes" is

quite small, ranging from 0.966 to 0.999 . However, for the node "Collision=Yes", the probability number is large, which is somewhere between 0.359 and 0.886 , varying from "Medium likelihood" to "Likely to happen".
![img-3.jpeg](img-3.jpeg)

Figure 4 Posterior interval probabilities for the collision model

The wide range of the interval marginal probabilities could be partially explained by the use of the linguistic terms. The initial imprecision in conditional probabilities sequentially

propagates to the posterior probabilities. Therefore, it might be advisable to carefully modify the terms in the future so as to allow more flexibility in probability specification. The ideal case should be to elicit the probability interval numbers directly where the experts can decide the broadness the interval for each judgment. However, allowing for flexibility would add to much complexity in application. In the first version elicitation tool, the experts were asked to specify the boundaries of conditional probability numbers by dragging two sliders. But the feedback from the experts is that they seem to be confused by too many numbers. It is always not easy to strike a balance. More effort should therefore be focused on this for future exploration.

# 4.2.Comparisons of results from different experts 

In addition to the computation of the combined probabilities, separate calculations were also performed to compare the inputs provided by each of the eleven experts. We denoted " 0 " for the case using the combined interval conditional probability as input and " 1 ", " 2 ", ... " 10 ", "11" for the cases with inputs from expert " 1 ", " 2 ", ... " 10 ", " 11 ". The marginal probabilities for six nodes ("Collision", "Maneuvering1", "Detection1", "Navigational system detection1", "Visual detection1" and "VTS detection") were chosen for comparison, as illustrated in Figure 5.

![img-4.jpeg](img-4.jpeg)

Figure 5 Comparisons of prior probability intervals from all experts

The marginal probabilities of the same node from different experts in Figure 6 show discrepancies, both in the width and ranges of the intervals, which further verifies the existence of epistemic uncertainty in the result of risk assessment. This research is the first in exploring the quantification of the epistemic uncertainty in maritime accidents risk modelling. To reduce the epistemic uncertainty, careful attention should be given to all steps of risk assessment including the selection of experts, the education of experts on Bayesian Network as well as the elicitation process.

# 4.3.Backward inferences 

Back forward inference was performed for the node "Collision". Changes in posterior probability of some nodes were shown in Figure 6. Unlike the traditional Bayesian network

method, it is not easy to draw conclusion on the exact change of posterior probabilities with the interval probabilities. Only differences in the upper and lower bounds could be observed implicitly. The biggest change in the bounds of the interval posterior probabilities was for the node "Maneuvering". Given the evidence "Collision=Yes", both the upper bound and lower bounds for correct maneuvering have significantly decrease. On the other hand, there is a large increase in the bounds when the evidence was set as "Collision=No".
![img-5.jpeg](img-5.jpeg)

Figure 6 Changes of posterior probability with observations of the node "collision"

# 4.4.Evaluation of risk control option 

The uncertainty in the result of risk assessment also propagates to the decision-making process and influences the ranking of potential risk control options. The following example is illustrated.

Measures recommended for the evaluation of risk control options (step four of the FSA) are Gross Cost of Averting a Fatality (GCAF) and Net Cost of Averting a Fatality (NCAF), which are defined as follows (Kontovas and Psaraftis 2009); (Psaraftis 2012):

$$
\begin{gathered}
G C A F=\frac{\Delta C}{\Delta R} \\
N C A F=\frac{\Delta C-\Delta B}{\Delta R}
\end{gathered}
$$

$\Delta \mathrm{C}$ is the cost per ship for the implementation of the risk control options;
$\Delta \mathrm{B}$ is the economic benefits resulting from the implementation, which include the saved cost for cargo damage, ship repairs etc.;
$\Delta \mathrm{R}$ is the risk reduction per ship.
The dominant yardstick in all FSA studies that have been submitted to IMO so far for deciding a potential risk control option is the " $\$ 3 \mathrm{~m}$ criterion" (Kontovas and Psaraftis 2009). Recent applications also include environmental consequences into consideration. The level of risk reduction $\Delta R$ could be obtained with the BN analysis but it is very difficult to obtain the exact cost and benefit values. The subjective method proposed by (Wang et al. 2013) is adopted for analysis in this research since it does not require absolute cost and benefit values. The cost and benefit values can be defined with linguistic terms such as "High", "Low" etc., which could then be mapped onto the defined utility expressions. Definitions of the cost expression and the utility expression could be found in Table 7 and Table 8, where the number 1-7 are 7 categories to which the linguistic variables could be mapped with a membership function/number. The categories don't have practical meaning but provide engineers with measures with which a linguistic variable can be modelled. For simplification, the ranks of risk control options in the following example will be based on GCAF only. Thus, only cost values need to be evaluated. The preference degree $P$ of a risk control option could

be calculated from the utility values (Wang et al. 2013). The final ranking of RCOs depends on the value of $R P_{i}=1 /\left(P_{i} \times \Delta R\right)$. The smaller the $R P_{i}$, the more cost effective RCO will be.

Table 7 Cost expressions


Table 8 Utility expressions


Four risk control options could be proposed based on the analysis of the model: (1) Simulator training for officers on difficult tasks such as passage planning and operations during malfunction of critical technical equipment; (2) Improving the bridge resource management for the bridge team; (3) Redundant propulsion or steering system; and (4) Improving safety culture. Changes in collision probabilities after implementing these risk control options were calculated with the traditional Bayesian Network method as well as the interval Bayesian Network method separately, as shown in Table 9. For risk reduction calculated with interval probabilities, the changes of the upper bound and lower bound were used as two special cases for comparison.

Table 9 Risk reduction for each RCO under interval and point Bayesian network



Suppose that the costs of these four RCOs are "Moderately High", "High", "Average", "Very high" and varyi (Wang et al. 1996), their values are as follows:

Table 10 Cost evaluation


The preference degree values $P_{i}$ calculated with the best fit method for the RCO1 to RCO4 are $0.531218565,0.531756404,0.613794117$, and 0.328221365 respectively. Combining with the risk reduction values from Table 9, i.e. "Change of Lower bound" (Case 1), "Change of Upper bound" (Case 2), and "Change of Point Probability" (Case 3), the RP values and rankings of RCO for different cases could be calculated as summarised in Table 11.

Table 11 The RP values and rankings of RCO for different cases


It could be seen from Table 11 that the rank of cost effectiveness values for different RCOs differs for the three cases. The example is just to simulate the impact of uncertainty in risk analysis result on decision making process. The detailed decision-making with the imprecise probabilities still remains a question for future research.

# 5 CONCLUSIONS 

Risk prediction with BN is a popular methodology for modelling causal relationship, interdependence and easy updating. Experts' knowledge is the main source of data for BN construction and parameterization for many maritime accidents modelling due to the lack of empirical data. However, experts' involvement brings a high level of epistemic uncertainty. This paper explored the application of interval probabilities instead of tradition point probabilities in Bayesian Network to address this uncertainty. Linguistic terms defined with probability intervals were used for the probability elicitation process. It was found that experts feel more confident in providing their judgment with linguistic terms compared to point probability numbers. Inferences were made directly with the interval probabilities with the GL2U algorithm. The methodology was applied to the causation probability modelling of ship collision. The calculated posterior probabilities were also in the form of interval probabilities, representing imprecision in the results. The influences of uncertainty in risk assessment results on ranks of potential risk control options were discussed using a simple example. This is the first research which applies imprecise probabilities in BN-based maritime risk predictions. The methodology adds more values to BN and its practical applications to the modelling of maritime accidents.

## LIST OF ABBREVIATIONS



# ACKNOWLEDGEMENTS 

We acknowledge the Interdisciplinary Graduate School of Nanyang Technological University (NTU) for providing the research scholarship for the first author as a PhD candidate. We appreciate the financial support and research facility from DHI-NTU Centre, under the umbrella of Nanyang Environment and Water Research Institute (NEWRI) of NTU. We would like to thank those experts who were interviewed and have contributed their precious time to discussions and answering the questionnaires. Last but not the least, we would also like to express our sincere gratitude to our reviewers for their valuable comments and suggestions which are of great importance to improving the quality of the paper.

## APPENDIX A

Table A Parent and child nodes for all nodes in the model



# APPENDIX B COMBINED INTERVAL PROBABILIES FROM ALL EXPERTS 

Table A1 The combined interval conditional probabilities for the node "Collision"


Table A2 The combined interval conditional probabilities for the node "Maneuvering"


Table A3 The combined interval conditional probabilities for the node "Maneuver planning"


Table A4 The combined interval conditional probabilities for the node "Navigational system detection"


Table A5 The combined interval conditional probabilities for the node "Visual detection"

of the OOW | Look out person | Visual detection=Yes |   |

Table A6 The combined interval conditional probabilities for the node "VTS detection"


Table A7 The combined interval conditional probabilities for the node "Rest hours"


Table A8 The combined interval conditional probabilities for the node "Fatigue"


Table A9 The combined interval conditional probabilities for the node "Distraction"


Table A10 The combined interval conditional probabilities for "Updating routine"


Table A11 The combined interval conditional probabilities for "OOW Competence"


Table A12 The combined interval conditional probabilities for "Maintenance routine"


Table A13 The combined interval conditional probabilities for the node "BRM"


Table A14 The combined interval conditional probabilities for the node "Training"


Table A15 The combined interval conditional probabilities for the node "Look out"


Table A16 The combined interval conditional probabilities for the node "Visibility"



Table A17 The combined interval conditional probabilities for "Steering failure"


Table A18 The combined interval conditional probabilities for "Navigational system signal"


Table A19 The combined interval conditional probabilities for the node "Navigational system settings"

