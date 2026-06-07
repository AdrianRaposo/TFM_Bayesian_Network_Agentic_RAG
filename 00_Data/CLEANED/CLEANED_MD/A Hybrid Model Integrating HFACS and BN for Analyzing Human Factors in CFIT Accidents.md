# Article 

## A Hybrid Model Integrating HFACS and BN for Analyzing Human Factors in CFIT Accidents

Bin Meng ${ }^{1,2}$ (D) and Na Lu ${ }^{1, *}$ (D)<br>check for updates

Citation: Meng, B.; Lu, N. A Hybrid Model Integrating HFACS and BN for Analyzing Human Factors in CFIT Accidents. Aerospace 2022, 9, 711. https://doi.org/10.3390/ aerospace9110711

Academic Editor: Alexei Sharpanskykh

Received: 23 October 2022
Accepted: 10 November 2022
Published: 12 November 2022
Publisher's Note: MDPI stays neutral with regard to jurisdictional claims in published maps and institutional affiliations.

## 0

Copyright: (c) 2022 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Civil Aviation, Zhengzhou University of Aeronautics, Zhengzhou 450046, China
2 Collaborative Innovation Center for Aviation Economy Development of Henan Province, Zhengzhou 450046, China

* Correspondence: luna@zua.edu.cn

Abstract: Controlled flight into terrain (CFIT) is considered a typical accident category of "low-probability-high consequence". Human factors play an important role in CFIT accidents in such a complex and high-risk system. This study aims to explore the causal relationship and inherent correlation of CFIT accidents by the Human Factors Analysis and Classification System (HFACS) and Bayesian network (BN). A total of 74 global CFIT accident investigation reports from 2001 to 2020 were collected, and the main contributing factors were classified and analyzed based on the Human Factors Analysis and Classification System. Then, the model was transformed into a Bayesian network topology structure. To ensure accuracy, the prior probability of each root node was computed by the fuzzy number theory. Afterward, using the bidirectional reasoning ability of the Bayesian network under uncertainty, this study performed a systematic quantitative analysis of the controlled flight into terrain accidents, including causal reasoning analysis, diagnostic analysis, sensitivity analysis, most probable explanation, and scenario analysis. The results demonstrate that the precondition for unsafe acts ( $30.5 \%$ ) has the greatest impact on the controlled flight into terrain accidents among the four levels of contributing factors. Inadequate supervision, intentional noncompliance with SOPs/cross-check, GPWS not installed or failure, adverse meteorological environment, and ground-based navigation aid malfunction or not being available are recognized as the top significant contributing factors. The contributing factors of the high sensitivity and most likely failure are identified, and the coupling effect between the different contributing factors is verified. This study can provide guidance for CFIT accident analysis and prevention.

Keywords: CFIT accidents; human factors; HFACS; Bayesian network; accident analysis

## 1. Introduction

The International Civil Aviation Organization (ICAO) and the International Air Transport Association (IATA) define controlled flight into terrain (CFIT) as "an in-flight collision with terrain, water, or obstacle, without indication of loss of control." In other words, when a CFIT accident occurs, the aircraft is airworthy and fully under the control of the flight crew [1,2]. Based on accident analysis data, ICAO identifies runway safety-related events, loss of control in-flight (LOC-f), and controlled flight into terrain (CFIT) as three high-risk accident occurrence categories in the 2013-2020 annual ICAO safety report [3]. Aviation safety experts have reached a consensus that CFIT is not the most common category of accidents, but it is one of the main contributors to high-fatality accidents. Research shows that CFIT accidents have been the second-largest fatal accident category, and $89 \%$ of CFIT accidents incur fatalities. Statistics indicate that among 837 flight accidents, only $6 \%$ of all accidents are classified as CFIT accidents, but the death toll from CFIT accidents accounts for $22 \%$ of all fatal accident deaths ( 892 out of 4070) during the period 2008-2017 [4]. Similarly, according to the analysis results of ICAO, CFIT accidents cause nearly a quarter of the death toll in aviation accidents worldwide, even though they account for only $3 \%$ of accidents [5]. Therefore, the CFIT accidents deserve the attention of the civil aviation industry.

Research has found that CFIT accidents usually have the following notable characteristics $[4,6,7]$ :

- Low incidence but high fatality rate;
- The phase of flight with the highest frequency of CFIT accidents is approach and landing, accounting for $66 \%$ of all CFIT accidents and $62 \%$ of fatal CFIT accidents;
- Most CFIT accidents result from the pilot's loss of situational awareness (SA). That is to say, in most cases, pilots can completely avoid these accidents.
Present studies indicate that human factors in flight are an important cause of aviation unsafe events and have gradually become the focus of research in the field of aviation safety [8,9]. Statistics show that more than $70 \%$ of aviation unsafe events are related to human errors [10-12]. Some scholars even claim that the causes of all aviation accidents are related to some kind of human error [13]. Therefore, human factors in flight are considered to be the biggest hidden danger to aviation safety today. In any case, it seems incredible that an airworthy aircraft capable of a safe flight can be flown into terrain while completely under the control of the pilot. From the definition of CFIT, multiple human performance deficiencies and undesirable behaviors are indicated in all CFIT accidents, which constitute the largest group of contributing factors in the CFIT accidents set [14].

Civil aviation transportation is a very complex system composed of the flight crew, various equipment, operating environment, organization management, etc. It is recognized that civil aviation accidents are generally not caused by a single factor or, in most cases, not by a single person [15]. Therefore, there are numerous contributing factors leading to CFIT accidents, and they are complex and changeable. The factors interact with each other, resulting in a nonlinear and dynamic complex system for its risk evolution. Risks may be incubated and transmitted at multiple nodes in the system at the same time and eventually evolve unpredictable results [16,17]. An early study believes that CFIT accidents are closely related to factors such as pilot-controller communication, cockpit workload, noise reduction procedures, government regulation, and visual hallucinations [18]. Some researchers have statistically analyzed 50 CFIT accidents from 2007 to 2017 based on the HFACS model, and results show that although human factors represent a major component of CFIT accidents, regulatory factors and organizational influences cannot be ignored [19]. A recent statistical report by IATA implies the most frequent contributing factors to CFIT accidents include regulatory oversights, SOP Adherence/SOP cross-verification, technology and equipment, environmental threats, safety management, etc. [4]. A disturbing finding is that every CFIT accident is more or less connected to the pilot's lack of situational awareness, including misperception, misunderstanding, and misprediction, which can lead to the pilots' visual illusion, spatial disorientation, decreased vigilance, etc. [14]. Research indicates that $75 \%$ of the planes involved in CFIT accidents were not equipped with the Ground Proximity Warning System (GPWS) [20]. Consequently, describing an aviation accident as a "human error" of the flight crew is an oversimplified analysis result. After all, it is only an active failure (with immediate severe consequences) [21,22]. The research on the mechanism of human factors and other contributing factors should become an urgent problem to be solved in CFIT accidents.

To better understand the research status, we collected the representative literature on CFIT from 2017 to 2022 and summarized the main research topics and research approaches, as shown in Table 1. Existing studies mainly focus on the classification and qualitative analysis of the causes of CFIT accidents, the application of new technology to prevent CFIT accidents, the safety assessment of flight procedures and the improvement of flight training, etc., but few involve the quantitative analysis of the internal mechanism of the contributing factors of CFIT accidents. The main reason is that CFIT accidents occur less frequently, which makes it difficult to obtain sufficient historical accident data, especially for commercial transport aviation. To overcome these limitations, this study comprehensively used HFACS, the Bayesian network, expert evaluation, and fuzzy numbers for quantitative analysis of the causal relationship and inherent correlation of CFIT accidents. The integrated approach has a powerful ability for learning, reasoning, and fuzzy processing, which

makes the multi-dimensional analysis of CFIT accidents under the condition of limited data and uncertain information. This paper provides a new framework for the analysis of accidents with a low probability, which could be used as a decision-making tool for safety management to formulate various intervention strategies.

Table 1. Summary of CFIT research topics and methods.


The rest of the study is structured as follows. Section 2 develops a hybrid HFACS-BN for CFIT accident analysis. Section 3 illustrates the application of the HFACS-BN model for CFIT accidents. The analysis results are presented in Section 4. The discussion and conclusion are shown in Sections 5 and 6.

# 2. Materials and Methods 

### 2.1. Human Factors Analysis and Classification System (HFACS)

The Human Factors Analysis and Classification System (HFACS) was originally developed for military aviation [31] but has since been widely used for human factors analysis in safety-critical areas, including coal mine production [32], railway transportation [33], marine transportation [34], etc. The HFACS model is further optimized based on Reason's "Swiss cheese" model and believed that aviation is a complex production system, and all accidents are caused by four levels of failures: unsafe acts, a precondition for unsafe acts, unsafe supervision, and organizational influences, as presented in Figure 1 [22]. The HFACS model makes a retrospective analysis from the direct factor of the unsafe acts of the operator and finally obtains all the latent failures and active failures that lead to the accident [35].

### 2.2. Bayesian Network (BN)

The BN is one of the most powerful theoretical models in the field of uncertain reasoning proposed by Pearl [36,37]. It is a directed acyclic graph (DAG) model based on network structure, which represents random variables and their conditional dependencies by nodes and arcs to discover potential relationships. The nodes of the Bayesian network represent variables, and the arrows represent the conditional dependencies between the variables [38,39]. The nodes towards which arrows are directed are child nodes, whereas the nodes away from the arrows are parent nodes. In addition, nodes without any child nodes are called leaf nodes, and nodes without any parent nodes are called root nodes. An intermediate node acts as both a parent node and a child node in the BN [40,41].

A BN is applied to the reasoning and probability calculation based on the Bayesian theorem. Dependencies between the child nodes and their parent nodes can be quantified by conditional probability distributions from conditional probability tables (CPTs). For nodes without a parent, the probability is not conditioned on other nodes, and their prior probabilities or unconditional probabilities are specified [42]. The prior probability refers to the probability assigned to an event, which is usually obtained through historical data or expert judgment. Conditional probability is interpreted as the likelihood that an event will

occur based on the occurrence of previous events or outcomes. Joint probability refers to the probability that two or more events occur at the same time [43,44].
![img-0.jpeg](img-0.jpeg)

Figure 1. Traditional HFACS structure.
Consider a graph $G=(V, E)$ with a set of variables $V=\left\{X_{1}, X_{2}, \ldots, X_{n}\right\}$. $E$ represents the set of arcs. Then, the joint probability distribution of each variable can be expressed in Equation (1), where Parent $X_{i}$ represents the parent node of $X_{i}$.

$$
P\left(X_{1}, X_{2}, \cdots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid \operatorname{parent}\left(X_{i}\right)\right)
$$

After obtaining the new additional information (also known as evidence), the prior probability of the event needs to be updated to get a more realistic probability [40,45], as presented in Equation (2), where $P(\alpha)$ and $P(\beta)$ refer to the prior probability of occurring for $\alpha$ and $\beta$, respectively; $P(\alpha \mid \beta)$ refers to the probability of $\alpha$ given $\beta ; P(\beta \mid \alpha)$ is the probability of $\beta$ given $\alpha$.

$$
P(\alpha \mid \beta)=\frac{P(\beta \mid \alpha) P(\alpha)}{P(\beta)}
$$

A typical BN diagram is shown in Figure 2, where node " $A$ " is a parent node, and nodes " $B$ " and " $C$ " are child nodes.

![img-1.jpeg](img-1.jpeg)

Figure 2. Typical BN diagram.

# 2.3. Combination of HFACS and BN 

The HFACS model takes into account the various factors involved at different levels in an aviation accident. However, there are some shortcomings. First, HFACS involves so many factors, especially some latent threats (unsafe supervision and organizational influences), and it is extremely difficult to collect such information, even with detailed accident reports [46,47]. In addition, the HFACS model mainly relies on correlation analysis, and many reasoning processes depend on the analytical ability and work experience of investigators. The results are more conducive to qualitative analysis but lack the ability of a quantitative risk assessment, and it is difficult to analyze the evolution process of accident causes [48]. Many scholars have combined the HFACS model with other risk analysis methods to make it more suitable for applications in different fields. For example, James J. H. Liou et al. [49] integrated FMEA and HFACS to assess the risk of inter-city bus accidents for calculating the risk degree and putting forward the improvement measures. Li et al. [50] used the HFACS model to analyze the influencing factors of ship collision accidents and transform them into the graphic structure of the BN to obtain the causal relationship and causal chain of ship collision accidents. M. Karthick et al. [51] integrated HFACS and FAHP to determine the key factors affecting the occurrence of human errors in the nuclear plant control room and quantitatively assessed nuclear accidents.

To overcome these limitations and further research the causal relationship and evolution process of the contributing factors of CFIT accidents, this study used a hybrid HFACSBN model to analyze CFIT accidents. The process diagram of the proposed methodology used in the present study is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. The process diagram of the proposed methodology used in the present study.

# 3. Application of the Methodology 

### 3.1. Analysis of the Main Contributing Factors to CFIT Accidents

It is considered that CFIT accidents are caused by a series of chain events triggered by the improper coupling of humans, equipment, organization, and other complex factors in a specific environment. To ensure the reliability and credibility of the analysis, we conducted a retrospective search mainly through the aviation safety information systems of the International Civil Aviation Organization (ICAO), the International Air Transport Association (IATA), the Civil Aviation Administration of China (CAAC), and the National Transportation Safety Board (NTSB), and obtained 74 CFIT accident investigation reports from 2001 to 2020, involving 58 commercial transportation aviation flight accidents and 16 general aviation flight accidents. Based on the existing research [4,19], we analyzed these CFIT accidents based on the CFIT model and completed the extraction of the main contributing factors, as shown in Table 2.

Table 2. The main contributing factors to CFIT accidents.


### 3.2. Construction of the BN Model for the CFIT Risk

### 3.2.1. Transformation HFACS into BN

According to the hierarchical structure of the HFACS model, the nodes in Table 2 were transformed, where the $\mathrm{T}_{0}$ node was set as the leaf node, $\mathrm{M}_{1} \sim \mathrm{M}_{5}$ and $\mathrm{N}_{1} \sim \mathrm{~N}_{10}$ were set as intermediate nodes, and $\mathrm{X}_{1} \sim \mathrm{X}_{26}$ were set as root nodes. Finally, the HFACS model of CFIT accidents was transformed into the topological network structure of BN, as shown in Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4. Schemes follow the same formatting.

# 3.2.2. Estimation of Prior Probabilities 

The prior probabilities of root nodes can usually be obtained by analyzing historical data or by expert judgment [52]. Considering the small number of CFIT accident samples and the limited historical data, the prior probabilities of the root nodes cannot be accurately calculated. Therefore, we used the combination of the fuzzy number and expert judgment to estimate the prior probability of the root node. The fuzzy number has been widely used to solve uncertain and incomplete information, which provides an effective mathematical means for describing and dealing with fuzzy problems [53].

Generally, experts prefer to use linguistic variables, such as "Extremely low (EL)", "Low (L)", "Fairly low (FL)", "Medium (M)", "Fairly high (FH)", "High (H)" and "Extremely high $(\mathrm{EH})$ ", to describe the possibility of an event [54]. Considering that the triangular fuzzy number and trapezoidal fuzzy number had a strong ability to describe fuzziness and uncertainty, according to previous research [55,56], these linguistic variables are represented in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. Fuzzy numbers corresponding to linguistic variables.

A fuzzy number is a normal fuzzy subset of a real line with upper semi-continuous and quasi-concave membership functions [57]. A fuzzy number $A$ is defined as a subset of real numbers whose membership function $\mu_{A}(x)$ is a continuous mapping from the real line $R$ to a closed interval $[0,1]$. The triangular fuzzy number can be defined as $\mu_{A}(x)=(a, b, c)$ [58], as expressed in Equation (3).

$$
\mu_{A}(x, a, b, c)= \begin{cases}\frac{x-a}{b-a}, & a \leq x \leq b \\ \frac{c-b}{c-b}, & b<x \leq c \\ 0, & \text { otherwise }\end{cases}
$$

The trapezoidal fuzzy number can be defined as $\mu_{A}(x)=(a, b, c, d)$ [59], as presented in Equation (4).

$$
\mu_{A}(x, a, b, c, d)=\left\{\begin{array}{cc}
\frac{x-a}{b-a}, & a \leq x \leq b \\
1, & b<x<c \\
\frac{d-x}{d-c}, & c \leq x \leq d \\
0, & \text { otherwise }
\end{array},\right.
$$

Suppose $A \in F(U), \lambda \in[0,1], A_{\lambda}$ is called a $\lambda$-cut set and can be expressed in Equation (5).

$$
A_{\lambda}=\left\{x \mid u_{A}(x) \geq \lambda, x \in U, \lambda \in[0,1]\right\}
$$

Each class of the fuzzy set is divided into two subsets by $\lambda$-cut. The cut set intervals of the triangular fuzzy number and the trapezoidal fuzzy number can be calculated by Equations (6) and (7).

$$
\begin{aligned}
& A_{\lambda}=[a+(b-a) \lambda, c-(c-b) \lambda] \\
& A_{\lambda}=[a+(b-a) \lambda, d-(d-c) \lambda]
\end{aligned}
$$

The fuzzy number and $\lambda$-cut set are shown in Table 3.
Table 3. The fuzzy number and $\lambda$-cut set.


The calculation process of the root node prior probability was as follows: firstly, we invited five experts with similar experiences to make a judgment on the possibility of the root nodes according to Figure 5, including two aviation accident investigators from the Civil Aviation Administration of China, two airline safety managers, and one scholar in the field of aviation human factors. Then, the $\lambda$-cut set of fuzzy sets was selected to combine expert opinions, and the average fuzzy number of expert opinions was obtained. Finally, the average fuzzy number was converted to the fuzzy possibility score (FPS), and then the fuzzy possibility score (FPS) was converted into a fuzzy failure probability (FFR), which was the probability of the root node.

1. Calculating the fuzzy number. Taking root node $\mathrm{X}_{15}$, "poor teamwork ability", as an example, the evaluation languages of the five experts were "Fairly low", "Fairly low", "Medium", "Medium", and "Fairly high". Since the five experts had similar experiences, we believed that the weights of the experts' opinions were equal. According to the fuzzy numbers and $\lambda$-cut sets shown in Table 3, the evaluation opinions of the five experts were averaged as presented in Equation (8).

$$
W_{X_{15}}=\frac{A_{L}^{\lambda}+A_{F L}^{\lambda}+A_{L}^{\lambda}+A_{M}^{\lambda}+A_{L}^{\lambda}}{5}=[0.34+0.1 \lambda,0.6-0.1 \lambda]
$$

According to the extension theory of fuzzy sets, W was also a fuzzy set as presented in Equation (9).

$$
W_{\lambda}=\left[z_{1}, z_{2}\right]=[0.34+0.1 \lambda,0.6-0.1 \lambda]
$$

The relation function of the average fuzzy number W could be expressed as Equation (10).

$$
A_{W}(z)=\left\{\begin{array}{cc}
\frac{z-0.34}{0.1}, & 0.34<z \leq 0.44 \\
1, & 0.44<z \leq 0.5 \\
\frac{0.6-z}{0.1}, & 0.5 \leq x \leq 0.6 \\
0, & \text { otherwise }
\end{array}\right.
$$

2. Converting the fuzzy number into FPS. The left-right fuzzy sorting method was used to defuzzify the fuzzy number [60], and the maximum fuzzy set and minimum fuzzy set were defined by Equations (11) and (12).

$$
\begin{gathered}
f_{\max }=\left\{\begin{array}{cc}
x, & 0<x<1 \\
0, & \text { otherwise }
\end{array},\right. \\
f_{\min }=\left\{\begin{array}{cc}
1-x, & 0<x<1 \\
0, & \text { otherwise }
\end{array},\right.
\end{gathered}
$$

The left boundary fuzzy possibility score $F P S_{L}$ and the right boundary fuzzy possibility score $F P S_{R}$ of the fuzzy number W were expressed as Equations (13) and (14).

$$
\begin{gathered}
F P S_{L}(W)=\sup _{x}\left[A_{W}(x) \wedge f_{\min }(x)\right]=0.6 \\
F P S_{R}(W)=\sup _{x}\left[A_{W}(x) \wedge f_{\max }(x)\right]=0.5455
\end{gathered}
$$

The fuzzy probability score of W was calculated by Equation (15).

$$
F P S(W)=\frac{1}{2}\left[F P S_{R}(W)+\left(1-F P S_{L}(W)\right)\right]=0.4728
$$

3. The FPS was converted to FFR using Equations (16) and (17) [54,61].

$$
\begin{gathered}
F F R=\left\{\begin{array}{cc}
\frac{1}{10^{K}}, & (F P S \neq 0) \\
0, & (F P S=0)
\end{array},\right. \\
K=\left[\frac{1-F P S}{F P S}\right]^{\frac{1}{3}} \times 2.301
\end{gathered}
$$

Finally, the calculation result of the $F F R$ of the root node $\mathrm{X}_{15}$, "poor teamwork ability", was $4.1106 \times 10^{-3}$, and the prior probability of the root node $\mathrm{X}_{15}$ was $4.1106 \times 10^{-3}$. Similarly, the prior probabilities of other root nodes could be calculated, as shown in Table 4. To simplify the analysis, the two states of the root node were defined as "Yes" or "No" according to the characteristic of the root node.

Table 4. The prior probabilities of the root nodes.


# 3.2.3. Calculation of Conditional Probability Tables (CPTs) 

Taking the 74 CFIT accidents in Section 3.1 as the sample data, using the learning ability of the Bayesian network, and combining the opinions of experts, 13 conditional probability tables were finally obtained. An example of the CPT of node $\mathrm{M}_{2}$ is presented in Table 5.

Table 5. The prior probabilities of the root nodes.


## 4. Results

### 4.1. Causal Reasoning Analysis

The causal reasoning (forward) analysis is based on the prior probabilities of the root nodes and CPTs to obtain the probability of the result [38]. We input the prior probabilities into Table 4 into the BN model, used the Netica software for forward inference, and finally calculated the probability of a CFIT accident as $8.6166 \times 10^{-8}$.

### 4.2. Diagnostic Analysis

The diagnostic (abductive reasoning) analysis refers to obtaining the cause of the result and the posterior probabilities of the nodes given some new evidence [62]. Using the function of BN fault diagnosis, the significant contributing factors leading to the CFIT risk can be analyzed. To this end, we set the value of $T_{0}$ to $100 \%$ to obtain the posterior probability of each node, as shown in Figure 6.

To find out the significant contributing factors leading to the CFIT accident, the posterior probabilities of the root nodes were sorted, and the results are shown in Table 6. The larger the probability value, the more significant the impact on the CFIT accident.

![img-5.jpeg](img-5.jpeg)

Figure 6. The posterior probability of each node.

Table 6. The posterior probabilities of the root nodes.

Probability | Ranking | Node | Posterior
Probability | Ranking | Node | Posterior
Probability | Ranking  |

The comparison results of the prior probability and posterior probability of the root node are presented in Figure 7. 0.20 0.18 0.16 0.14 0.12 0.12 0.08 0.04 0.02 0.00 0.00 Figure 7. The comparison results of the prior probability and posterior probability of the root node.

4.3. Sensitivity Analysis

In the Bayesian network model, the sensitivity analysis can reflect the quantification of the target node caused by the change in the local parameters of the network model and then identify the sensitivity factors in the model [63]. The Netica software takes mutual information (entropy reduction), percentage (comparison value), and variance (variance of belief) as important indicators to measure sensitivity analysis. The larger the value, the greater the impact [64].

First, $\mathrm{T}_{0}$ was set as the target node, and the order of sensitivity was $\mathrm{M}_{2}(10.60 \%)$, $\mathrm{M}_{1}$ (10.10\%), $\mathrm{M}_{4}(8.54 \%)$, and $\mathrm{M}_{3}(8.08 \%)$. Next, these nodes were set as the target nodes, and the main sensitive root nodes were obtained, as shown in Figure 8.
![img-6.jpeg](img-6.jpeg)

Figure 8. Sensitivity analysis results.

# 4.4. Most Probable Explanation 

Bayesian network reasoning can not only deal with the problem of posterior probability but also solve the maximum a-posterior probability (MAP) and most probable explanation (MPE) [65]. MAP and MPE are considered to be the most reasonable explanations for the observations [66]. After the value of $\mathrm{T}_{0}$ was set to $100 \%$, the "Most Probable Expl" function of the Netica software was clicked, and the MAP and MPE of the CFIT accidents are shown in Figure 9.

![img-7.jpeg](img-7.jpeg)

Figure 9. The MAP and MPE of CFIT accidents (The thick arrows represent the most likely paths).

# 4.5. Scenario Analysis 

Scenario analysis is realized through the new evidence update function of BN. The probability value of the node state changes dynamically with different sets of accident scenarios, which can analyze the synergy among the root nodes in specific scenarios [67]. According to the HFACS model, the main contributing factors to CFIT accidents could be summarized into four levels: unsafe acts $\left(\mathrm{M}_{1}\right)$, a precondition for unsafe acts $\left(\mathrm{M}_{2}\right)$, unsafe supervision $\left(\mathrm{M}_{3}\right)$, and organizational influences $\left(\mathrm{M}_{4}\right)$. To further study the impact of the coupling of different levels on the CFIT risk, we selected the two more sensitive root nodes of $\mathrm{M}_{1}, \mathrm{M}_{2}, \mathrm{M}_{3}$, and $\mathrm{M}_{4}$, respectively, according to the results in Section 4.3, and the selected root nodes' states were set as "Yes $=100 \%$ " to the scenario analysis. According to the calculation results in Section 4.1, the initial value of $\mathrm{T}_{0}$ was $8.6166 \times 10^{-8}$. The scenario analysis results are presented in Table 7 and Figure 10.
![img-8.jpeg](img-8.jpeg)

Figure 10. The ratio of $\mathrm{T}_{0}{ }^{\prime}$ to the initial value of $\mathrm{T}_{0}$ in different scenarios.

Table 7. Scenario analysis results.


It should be noted that Scenario 10 was a typical case of the CFIT-Yichun plane crash accident. Accident introduction [68]: at 21:38 on 24 August 2010, Henan Airlines flight VD8387 performed a flight mission from Harbin to Yichun, and it crashed at a distance of 690 m from Runway 30 during the approach at Lindu Airport in Yichun City, which caused 44 deaths and 52 injuries. According to the official investigation report, the main reasons for the accident were as follows: the terrain of the Yichun Airport was complicated, and there was radiation fog and low visibility at that time; the airport lacked precise ground navigation equipment; the captain violated the regulations, ignored the radio altitude voice warning, and continued to approach blindly without establishing any visual references; the flight crew did not take go-around measures; the operation plan was improper, and the captain lacked technical skills and training; the coordination and cooperation among the crew members were not good. There was poor communication among members and failure to cross-check; the airline failed to supervise the captain's qualification and ability; the airline did not formulate a safety policy for the operation of Yichun Airport; there was insufficient safety management and safety investment in the airline; there were supervisory violations by civil aviation management agencies.

# 5. Discussion 

There are many factors contributing to CFIT accidents, and human factors have been identified as major contributing factors in CFIT accident investigations. However, due to the small sample size of CFIT accidents, the traditional CFIT analysis methods are mostly qualitative analyses. In this present study, the HFACS model was integrated with BN, and the uncertainty analysis ability and bidirectional reasoning ability of the BN theory were fully used for the quantitative analysis of human factors in CFIT accidents, which could not only clarify the relationship between the contributing factors but also analyze the critical factors most likely to lead to CFIT accidents.

The calculation results in Section 4.1 showed that the probability of CFIT accidents was $9.9325 \times 10^{-8}$. That is why NASA and FAA consider CFIT a typical type of accident with a low probability but high consequence [69] According to statistical analysis, the average probability of CFIT accidents from 2010 to 2016 was about $1.414 \times 10^{-7}$, and the study believes that the probability of CFIT accidents is between $3 \times 10^{-8}$ and $3 \times 10^{-7}$ [70]. Therefore, the calculation result is within this scope, which verifies the feasibility of this methodology.

Among the four levels of contributing factors, the precondition for unsafe acts $\left(\mathrm{M}_{2}\right)$ accounted for the largest proportion, reaching $30.5 \%$, followed by unsafe acts of the flight crew $\left(\mathrm{M}_{1}\right)(25.7 \%)$, unsafe supervision $\left(\mathrm{M}_{3}\right)(25.1 \%)$, and organizational influences $\left(\mathrm{M}_{4}\right)$ (19.1\%), as presented in Figure 6. The results indicate that CFIT accidents are directly triggered by these preconditions, including environmental factors $\left(\mathrm{N}_{3}\right)$, flight crew conditions $\left(\mathrm{N}_{4}\right)$, and personal factors $\left(\mathrm{N}_{5}\right)$. Some other studies have produced results essentially in agreement with the statement. Harris et al. [71] used an artificial neural network to model the relationship between preconditions for unsafe acts and unsafe acts and an average overall classification rate of circa $74 \%$ for all the unsafe acts from the information derived from the pre-conditions. This result also verifies that accidents are the final result of many potential failures and active failures [72].

The diagnostic analysis results also showed that the top significant factors for CFIT accidents were inadequate supervision $\left(\mathrm{X}_{17}\right)$, intentional noncompliance with SOPs/crosscheck $\left(\mathrm{X}_{4}\right)$, GPWS not installed or GPWS failure $\left(\mathrm{X}_{9}\right)$, adverse meteorological environments $\left(\mathrm{X}_{6}\right)$, and ground-based navigation aid malfunctions or not available $\left(\mathrm{X}_{8}\right)$, etc., which are listed in Table 6 and Figure 7. The prior probability refers to the probability obtained from previous experiences or statistical analysis, which is the probability before the result occurs. The posterior probability is used to calculate and analyze the most likely causes after the result occurs. Therefore, the posterior probabilities of most contributing factors had higher values than the prior probabilities. Since the inference result of BN largely depends on the prior probabilities, the posterior probabilities of each contributing factor were consistent with the trend of the prior probabilities, as shown in Figure 7. The identified top significant factors were highly consistent with the existing relevant research. IATA used the threat and error management (TEM) framework to statistically analyze the frequency of the contributing factors of 47 CFIT accidents from 2008 to 2017, and the results indicated that the most frequent contributing factors to CFIT accidents were regulatory oversight ( $72 \%$ ), SOP adherence/SOP cross-verification (56\%), technology and equipment (54\%), meteorology (51\%), and nav Aids (51\%), etc. Facts have proved that the lack of guidance and supervision is the breeding ground for many violations that sneak into the cockpit [31]. Safety supervision is considered to be the most important front-end control link of risk management. Once this crucial defense fails, the threats will be very serious. This is because superficial and formalistic supervision will connive at the occurrence of intentional violations by the flight crew, which will make the flight crew form an illusion that some unsafe behaviors are not violations and can be tolerated. If the risks found cannot be solved or corrected, a closed-loop safety management system will not be formed [73]. Intentional noncompliance with SOPs/cross-check is an unforced error made by the flight crew when performing routine tasks, often accompanied by unhealthy psychological states, such as blind self-confidence and fluke [74]. A study concluded that $54 \%$ of human errors in LOSA (Line Operations Safety Audit) observations were intentional noncompliance [75]. We believe that the consequences of intentional noncompliance with SOPs/cross-checks are more serious, especially in the accident category of CFIT. Another notable contributing factor was that GPWS was not installed or GPWS failed $\left(\mathrm{X}_{9}\right)$. One disturbing finding was that $75 \%$ of the CFIT accident aircraft were not equipped with a GPWS (Ground Proximity Warning System) or EGPWS (Enhanced Ground Proximity Warning System), which can monitor an aircraft's height/descent rate and provide a warning if an undesirable trend develops [20,76]. Airbus considers that the application of collision avoidance technology is a key measure to reduce CFIT accidents [77]. According to statistical analysis, more than

half of the CFIT accidents are closely related to the adverse meteorological environment, including poor visibility/IMC (52\%), wind/wind shear/gusty wind (12\%), thunderstorms (8\%) [78]. Research shows that an adverse meteorological environment will sharply increase the workload of the flight crew, making it difficult to maintain a high situational awareness level, and it is likely to cause the flight crew spatial disorientation or make the aircraft out of control [79]. Another noteworthy factor was unavailable or malfunctioning ground-based navigation aids $\left(\mathrm{X}_{8}\right)$, which involve a lot of equipment, such as runway lighting systems, Precision Approach Path Indicators (PAPI), and the precision of ground navigation equipment (e.g., the absence of instrument landing systems), etc. These devices could provide the flight crew with the following important cues during the approach: identification, alignment, roll guidance, deviation correction, flight guidance, distance, and positive threshold definition, which could help address CFIT concerns in certain conditions. An FAA report shows that approach lighting systems provide the bridge for the transition from instrument flights to visual landing operations, which is crucial to flight safety in low visibility [80].

Another major finding of our study was that we had identified the high sensitivity factors of the four levels that lead to CFIT accidents based on the BN's sensitivity analysis function. The high sensitivity contributing factors of the prerequisite for unsafe behavior (M2) were as follows: intentional noncompliance with SOPs/cross-check $\left(\mathrm{X}_{4}\right)$, decision errors $\left(\mathrm{X}_{2}\right)$, skill-based errors $\left(\mathrm{X}_{1}\right)$, failed to GOA (go around) after destabilization on approach $\left(\mathrm{X}_{5}\right)$, and perceptual errors $\left(\mathrm{X}_{3}\right)$. The high sensitivity contributing factors of the precondition for unsafe acts $\left(\mathrm{M}_{2}\right)$ included GPWS not installed or GPWS failure $\left(\mathrm{X}_{9}\right)$, ground-based navigation aid malfunction or not available $\left(\mathrm{X}_{8}\right)$, adverse meteorological environment $\left(\mathrm{X}_{6}\right)$, poor teamwork ability $\left(\mathrm{X}_{15}\right)$, and blind confidence $\left(\mathrm{X}_{10}\right)$. Unsafe supervision (M3), inadequate supervision $\left(\mathrm{X}_{17}\right)$, improper operation plan $\left(\mathrm{X}_{18}\right)$, and failure to correct a known problem $\left(\mathrm{X}_{19}\right)$ were all sensitive contributing factors. The high sensitivity contributing factors of organizational influences (M4) were absent or deficient safety management $\left(\mathrm{X}_{26}\right)$, inadequate management decisions $\left(\mathrm{X}_{20}\right)$, lack of training $\left(\mathrm{X}_{21}\right)$, bad organizational culture/values $\left(\mathrm{X}_{22}\right)$, and insufficient rules and regulations $\left(\mathrm{X}_{23}\right)$.

It is remarkable that the root nodes identified by the most probable explanation also include intentional noncompliance with SOPs/cross-check $\left(\mathrm{X}_{4}\right)$, GPWS not installed or GPWS failure $\left(\mathrm{X}_{9}\right)$, inadequate supervision $\left(\mathrm{X}_{17}\right)$, and absent or deficient safety management $\left(\mathrm{X}_{26}\right)$, which fully illustrates the importance of these contributing factors. In addition, according to Figure 9, it can also reflect the most likely and critical risk evolution paths leading to CFIT accidents. Therefore, the results of the high-sensitivity analysis and most probable explanation can offer valuable insights for safety management by focusing on these sensitive contributing factors and prioritizing management when taking preventive measures.

Moreover, to further explore the cause mechanism of CFIT accidents, we also conducted a scenario analysis on highly sensitive factors of four levels. Scenario analysis was divided into three categories: single-level impact on CFIT risk, multi-level impact on CFIT risk, and case scenario analysis, including a total of 10 scenarios. According to Table 7 and Figure 10, the following findings could be obtained. First of all, the two more sensitive factors of a single level were set to "yes $=100 \%$ ", that is, when these two more sensitive factors failed, the CFIT risk levels of scenarios 1-4 increased by 20.96-48.55 times. Secondly, when setting the high sensitivity factors of two different levels as "yes $=100 \%$ ", the CFIT risk levels of scenario 5-7 increased by 67.60-81.01 times. When three or four levels of high sensitivity factors failed, the levels of CFIT risk increased by 113.69-130.71 times, such as in scenarios 8 and 9 . Worryingly, when multiple contributing factors of the four levels were coupled, the level of CFIT risk would increase sharply, such as in scenario 10. Assuming that the risk level of CFIT in scenarios 1-9 was a linear increase, then the risk level of CFIT in scenario 10 was an exponential increase. This finding was also confirmed by multiple studies. For example, the flight mission is carried out in a complex and high-risk system, and the flight crew's situational awareness is the result of the high interaction between various elements of "human-equipment-environment-organization". The more adverse

factors, the lower the flight crew's situational awareness [16]. It is obvious that most CFIT accidents are caused by the pilots' situational awareness failure [4]. Another study reveals that the coupling between various factors has a significant impact on the safety risk system, especially when the system is in a highly coupled state of unsafe factors it is very prone to destructive accidents [81].

Based on the above findings, the following recommendations are put forward to reduce CFIT risks. First, CFIT has many factors that can be attributed to human errors, and the safety management of CFIT should be targeted and prioritized, especially for the contributing factors with high posterior probability and high sensitivity. Secondly, organizational management should be safety oriented for CFIT risk management, such as strengthening safety supervision, establishing a good safety culture atmosphere, installing anti-collision equipment (GPWS/EGPWS), etc. Thirdly, it is necessary to incorporate CFIT into the CRM training programs. CRM training has been recognized as the most effective means to improve the situational awareness and resource management ability of the flight crew. When carrying out CRM training for flight crews, air operators should strengthen situational awareness training to avoid imminent CFIT situations in the following complex situations, including harsh meteorological environments, lack of high-precision navigation equipment, unstable approach, etc. Additionally, the flight crew should recognize the importance of effective situational awareness and pay attention to identifying potential CFIT situations during flight.

# 6. Conclusions 

CFIT accidents have always been considered the main cause of fatal aviation accidents, and there are numerous contributing factors. The purpose of this study is to clarify the significant factors leading to CFIT accidents and explore their causal relationships and interaction mechanisms by a hybrid HFACS-BN model. As a powerful quantitative tool, the model conducts an in-depth and systematic analysis of CFIT accidents, including causal reasoning analysis, diagnostic analysis, sensitivity analysis, scenario analysis, etc. Finally, combining theoretical and empirical analysis, the following conclusions are drawn: (1) Inadequate supervision, intentional noncompliance with SOPs/cross-check, GPWS not installed or GPWS failure, adverse meteorological environment, and ground-based navigation aid malfunction or not available are recognized as the top significant contributing factors for CFIT accidents; (2) Four levels of high sensitivity contributing factors are identified, including decision errors, intentional noncompliance with SOPs/cross-check, groundbased navigation aid malfunction or not available, GPWS not installed or GPWS failure, inadequate supervision, improper operation plan, inadequate management decision, and absent or deficient safety management, etc. (3) Meanwhile, intentional noncompliance with SOPs/cross-check, GPWS not installed or GPWS failure, inadequate supervision, and absent or deficient safety management are also considered to be the contributing factors most likely to fail. (4) The failure of some contributing factors at a single level has relatively little impact on the level of CFIT risk, but multiple contributing factors at different levels will sharply increase the level of the CFIT risk under the coupling effect. Collectively, these conclusions have very important theoretical significance and practical value, which is helpful to further understand the mechanism of CFIT accidents and provide valuable insights for safety management.

Due to the small number of CFIT accidents, it is difficult to obtain enough data to calculate the prior probabilities of contributing factors and the CPTs of BN. Therefore, we combined expert opinions in the study, and there would inevitably be some subjective judgments. In the future, we will expand the research samples. In addition to the CFIT accidents, we will also combine the CFIT incident to obtain sufficient data support, and the analysis results will be more accurate.

Author Contributions: Conceptualization, methodology, software, validation, B.M.; formal analysis, investigation, resources, data curation, writing-original draft preparation, N.L.; writing-review and editing, B.M.; visualization, supervision, N.L.; project administration, funding acquisition, B.M.; All authors have read and agreed to the published version of the manuscript.
Funding: This research was funded by the Key Scientific Research Projects of Colleges and Universities of the Henan Province, grant number 17A630069.
Institutional Review Board Statement: Not applicable.
Informed Consent Statement: Not applicable.
Data Availability Statement: Not applicable.
Conflicts of Interest: The authors declare no conflict of interest.
