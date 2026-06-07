# Article 

## Research on Construction Risk Assessment of Long-Span Cantilever Casting Concrete Arch Bridges Based on Triangular Fuzzy Theory and Bayesian Networks

Zhengyi He ${ }^{1}$, Yi Xiang ${ }^{1, * *}$, Linshu Li ${ }^{1}$, Mei Wei ${ }^{2}$, Bonan Liu ${ }^{1}$ and Shuyao Wu ${ }^{1}$

check for updates

Citation: He, Z.; Xiang, Y.; Li, L.; Wei, M.; Liu, B.; Wu, S. Research on Construction Risk Assessment of Long-Span Cantilever Casting Concrete Arch Bridges Based on Triangular Fuzzy Theory and Bayesian Networks. Buildings 2024, 14, 2627. https://doi.org/10.3390/ buildings14092627

Academic Editor: Fabrizio Gara
Received: 12 July 2024
Revised: 19 August 2024
Accepted: 21 August 2024
Published: 24 August 2024

## (0)

Copyright: (c) 2024 by the authors. Licensee MDPI, Basel, Switzerland. This article is an open access article distributed under the terms and conditions of the Creative Commons Attribution (CC BY) license (https:// creativecommons.org/licenses/by/ $4.0 /$ ).

1 School of Civil Engineering, Hunan City University, Yiyang 413000, China; hezhengyi@hncu.edu.cn (Z.H.)
2 School of Digital Arts, Hunan Art and Crafts Vocational College, Yiyang 413000, China

* Correspondence: xiangyi@hncu.edu.cn


#### Abstract

Considering the complex construction processes involved, there are significant risks during the construction of long-span cantilever casting arch bridges. In this study, a risk assessment method for the construction process of cantilever casting concrete arch bridges was developed. The compositional elements and characteristics of safety risks in the construction of cantilever casting concrete arch bridges were clarified, and a safety risk source list that includes seven major risk sources and thirty-three minor risk sources was formed. Then, a Bayesian model for the risk analysis of cantilever casting concrete arch bridge construction was established, and a method was proposed to determine the prior and posterior probabilities of the Bayesian network using triangular fuzzy numbers. This method fully utilizes the experience of experts while avoiding the subjectivity of expert opinions. A cantilever casting concrete open spandrel arch bridge (Bridge A) with a total span length of 287 m was taken as an example, and a safety risk assessment was conducted during its construction process. The calculation results show that the construction safety risk level of Bridge A was level III. This engineering application verified the feasibility of determining key node parameters of the Bayesian network using triangular fuzzy numbers.


Keywords: construction risk assessment; cantilever casting concrete arch bridges; triangular fuzzy number; Bayesian network

## 1. Introduction

The cantilever casting construction method [1-3], which is widely used in concrete construction engineering both domestically and internationally, is increasingly being used to build large-span reinforced concrete arch bridges [4]. With the innovation of bridge structures and the continuous increase in their spans, a series of uncertain factors will arise. Due to the complex processes, high difficulty, and high uncertainty involved, huge losses may occur during the construction of reinforced concrete arch bridges using the cantilever casting method. At present, due to the immature technology in construction, there are still risks such as hanging baskets falling off, tower misalignment, and cable breakage, as shown in Figure 1, which then threaten the construction safety of the cantilever casting concrete arch bridges.

Moreover, there is currently relatively little systematic analysis and research on the construction risks of large-span cantilever casting arch bridges. Therefore, for large-span reinforced concrete arch bridges constructed using the cantilever casting method, construction risk analyses are necessary and very meaningful.

To date, domestic and foreign scholars have achieved a certain research foundation in the evaluation of bridge risks [6-10]. Khan et al. [11] proposed the seismic hazard analysis of fan-shaped cable-stayed bridges using the concept of a damage probability matrix. Novak et al. [12] comprehensively considered the structural factors of bridges after a series of disaster events and constructed a detailed probability model. Ahn et al. [13] analyzed

the records of third-party damage and financial losses during bridge construction and constructed a quantitative relationship between damage and risk indicators. Taejun et al. [14] conducted a probabilistic risk assessment on prestressed concrete (PSC) box girder railway bridges and constructed an implicit limit state function for a target PSC railway bridge. Bao et al. [15] integrated the Analytic Hierarchy Process and Grey Relational Analysis to establish a multi-level comprehensive evaluation model, which was then used to assess risks during the construction process of large-span bridges. Wang et al. [16] proposed a fuzzy TOPSIS method based on the alpha-level set for bridge risk assessment. In an analysis of three numerical examples, the proposed fuzzy TOPSIS method showed distinct performance advantages compared to other fuzzy TOPSIS methods. Sun et al. [17] proposed a fuzzy framework based on a transformation system and aggregation process to evaluate the impact of explosion events caused by hazardous materials on bridges. Based on seismic risk assessment results for hundreds of bridges with the complete structural information, Andres et al. [18] analyzed the uncertainty in quantifying expectations at different levels of knowledge using classification methods and machine learning models. Jelena et al. [19] developed a fuzzy logic controller for estimating the degree of damage to bridges.
![img-0.jpeg](img-0.jpeg)

Figure 1. Photos of some risk locations during the construction process of cantilever casting concrete arch bridges [5].

Overall, research on bridge risk analysis and assessment in foreign countries has received widespread attention. In terms of analysis methods, the bridge risk assessment methods mainly rely on probability analysis and hierarchical analysis. Currently, a single analysis method is often used, and a combination of methods is rarely used. In terms of the analysis objective, there is much research content related to the risk analysis of modern bridge construction, but most of it has focused on large-span cable-stayed bridges [20,21] and continuous rigid-frame bridges [22,23]. In contrast, research results related to risk analyses in cantilever casting concrete arch bridge construction are few and far between. If the existing analysis methods are used to comprehensively analyze the entire construction process of a cantilever casting concrete arch bridge, it will inevitably lead to a significant decrease in the accuracy of the evaluation results; even the process of formulating construction risk control measures may be affected.

This study focuses on the construction risk assessment of cantilever casting concrete arch bridges. Firstly, the risk sources during the construction process of cantilever casting concrete arch bridges are analyzed, and a method for determining the weight of risk sources is proposed. Then, the principle of using Bayesian networks for risk assessment and the process in its entirety are introduced. Finally, this method is applied to the construction of a bridge. The proposed method can be used to predict the probability and risk level of a potential risk source occurring during the construction process for cantilever casting concrete arch bridges. Through taking scientific and reasonable control measures based on the risk level, the probability of risk occurrence and the losses caused by accidents can be reduced.

# 2. Risk Source Identification Process 

The construction process of cantilever casting concrete arch bridges is complex, with a large time span and many problems that may occur throughout the entire construction process. The risk sources faced in different construction time periods are completely different. Hence, identifying risk sources is the first step in risk analysis for bridge construction. Cantilever casting concrete arch bridges are different from other types of arch bridges, and the construction-process-related risk sources should be fully considered.

Construction teams in China have relatively limited experience with cantilever casting concrete arch bridges, and the equipment systems, such as cable-stayed suspension systems and hanging basket systems, are complex. In addition, construction is generally carried out at high altitudes, with high-quality cantilever casting concrete and high construction technology requirements. These characteristics greatly increase the safety risks during construction. Therefore, the safety risks in the construction of cantilever casting concrete arch bridges are characterized by their uncertainty, objectivity, diversity, complexity, and dynamism.

Based on this, risk source identification should include four steps, as follows:
(1) Collecting engineering data;
(2) Decomposing construction processes;
(3) Identifying risk sources during the construction process;
(4) Determining major risk sources.

Firstly, the construction process is broken down based on the hierarchy of unit engineering, sub-unit works, and item projects, along with the main processes. A breakdown of the construction technology for cantilever casting concrete arch bridges is shown in Table A1. Then, the construction methods, operational procedures, mechanical equipment, and building materials of the evaluation unit are clearly defined. The typical types of accidents that occur in the target units are analyzed, and they are summarized and processed to establish a relevant risk source survey list, which is divided into seven primary risk sources and thirty-three secondary risk sources. The primary risk sources can mainly be divided into safety risks in bridge-approach pile foundation construction, arch seat construction, cable-stayed suspension systems, formwork or temporary supports, construction hanging baskets, main arch closure sections, and prefabricated T-beam construction. The 33 secondary risk sources are detailed risks from the primary risk sources. The full list of risk sources for the construction of cantilever casting concrete arch bridges is shown in Table A2.

## 3. The Principle of Risk Assessment during the Construction Process

### 3.1. Principle of Bayesian Network Risk Assessment

The principle of Bayesian network risk assessment [24,25] for probabilistic inference is to build a Bayesian network, for which Bayesian probability is the foundation. Bayesian probability is divided into the prior probability, conditional probability, total probability, and posterior probability, which are mainly converted through the Bayesian equation. The Bayesian equation is shown in Equation (1):

$$
P\left(N_{i} / M\right)=\frac{P\left(M / N_{i}\right) P\left(N_{i}\right)}{\sum_{i=1}^{n} P\left(M / N_{i}\right) P\left(N_{i}\right)}
$$

where $P\left(N_{i}\right)$ is the prior probability, $P\left(N_{i} / M\right)$ is the posterior probability, and $P\left(M / N_{i}\right)$ is the conditional probability.

The nodes of a Bayesian network can represent a series of random variables, and directed edges represent causal relationships between these variables. In this paper, a node represents a hazard source as a random variable, and a directed edge represents a relationship between hazard sources [26].

Bayesian networks are needed to construct corresponding models based on the characteristics of each evaluation object when they are applied. The composition conditions of the Bayesian network during the bridge construction process are the related risk sources, and the nodes in the network are regarded as the basic units for evaluating the specific risk events. The correlation between a child node and its parent nodes is based on logical settings between job programs. When setting up this model, it is necessary to determine the node dependency relationship and obtain the prior risk probability in order to provide support for subsequent analysis.

The entire Bayesian network modeling process is as follows:
(1) Establish dependency relationships between nodes in the Bayesian network;
(2) Determine the prior probability of risk events;
(3) Determine the conditional probability between nodes.

There are various styles of risk events, each with its own unique characteristics, so the probability distribution form also has various types. Therefore, the prerequisite for accurate risk probability assessment is to select the appropriate prior probability of risk events. In most cases, relevant statistical data on accidents are lacking, so the prior probability of accidents is generally obtained based on expert experience combined with relevant engineering data analysis.

Similarly, as most scenarios during construction cannot be simulated or replicated, the lack of accident data and the unique nature of the projects determine that expert experience is highly reliable. Based on the expert experience method, the conditional probability between nodes can be obtained; the large amount of knowledge and long-term practical experience provided by the experts can then be used to accurately determine the potential risks of the project.

# 3.2. Method for Determining the Weight of Risk Sources 

After identifying the risk sources, we must determine their importance. There may be multiple major risk sources in a construction project; therefore, they should be prioritized to meet the project's safety requirements. The determination of major risk sources mainly relies on expert judgment, but this method is affected to a certain degree by subjective influence.

Therefore, in this study, the triangular fuzzy number method [27] was used to identify major risk sources in the construction of cantilever casting concrete arch bridges; the respective proportions for different types of risk sources were determined during the evaluation and analysis process. The proportions (weights) for different types of risk sources refer to the node parameters in Bayesian network risk assessment. Fuzzy theory can be used to solve the above problems.

In fuzzy theory, the level at which an element belongs to a fuzzy set can be described by its membership degree, which is often represented by a membership function. There are also certain differences in the results obtained during the analysis process with different membership functions; thus, an appropriate membership function can allow for better solutions to specific problems. The fuzzy set of hazard sources determined for the construction process contains many continuous values, which are generally applied to piecewise linear functions in the parameterization process. Finally, the triangular membership function was chosen to identify major risk sources in the construction of cantilever casting concrete arch bridges. During the evaluation and analysis process, different types of risk sources were evaluated, and their respective weights were determined.

The trigonometric membership function $h_{x}$ is represented by Equation (2).

$$
h_{x}=\left\{\begin{array}{cc}
\frac{x-a}{b-c} & x \in[a, b] \\
\frac{b-c}{0} & x \in[b, c] \\
\text { other }
\end{array}\right.
$$

where $a, b$ and $c$ are used to represent the left, middle, and right intervals of $h_{x}$.

In this study, the safety risk level of cantilever casting concrete arch bridges was divided into seven levels; namely, extremely low (VL), low (L), slightly low (FL), medium (M), slightly high (FH), high (H), and extremely high (VH). The probability range and triangular fuzzy number corresponding to each risk level are shown in Table 1.

Table 1. Risk levels and their corresponding membership functions.


Firstly, the score $S_{i}$ was determined as shown in Equation (3).

$$
S_{i}=\left[\sum_{j=1}^{n} a_{i j}, \sum_{j=1}^{n} b_{i j}, \sum_{j=1}^{n} c_{i j}\right]
$$

The total score of all evaluation objects was then calculated as shown in Equation (4).

$$
\sum_{i=1}^{n} S_{i}=\left[\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}, \sum_{i=1}^{n} \sum_{j=1}^{n} b_{i j}, \sum_{i=1}^{n} \sum_{j=1}^{n} c_{i j}\right]
$$

The fuzzy relative weights based on the obtained scoring results were calculated as shown in Equation (5).

$$
w_{i}=\frac{S_{i}}{\sum_{i=1}^{n} S_{i}}\left[\frac{\sum_{j=1}^{n} a_{i j}}{\sum_{i=1}^{n} \sum_{j=1}^{n} a_{i j}}, \frac{2 \sum_{j=1}^{n} b_{i j}}{n(n-1)}, \frac{\sum_{j=1}^{n} c_{i j}}{\sum_{i=1}^{n} \sum_{j=1}^{n} c_{i j}}\right]
$$

Each triangular fuzzy number $M$ was defuzzified as shown in Equation (6).

$$
M=M(a, b, c) \rightarrow M=(a+2 b+c) / 4
$$

After processing with Equation (6), $w_{i}$ was normalized to obtain the weight of the evaluation object.

# 3.3. Evaluation of Safety Risk Levels 

At present, the methods most commonly used in risk assessment are numerical analysis, the risk matrix method, the risk graph method, and so on. Based on practical experience, the evaluation process integrates the probability of a risk event and the associated losses; this has a higher degree of conformity with the actual risk and can effectively meet the evaluation requirements in this regard. Due to the numerous risk factors involved in the construction of cantilever casting concrete arch bridges and the strong hierarchical nature of the risk source identification results based on the decomposition of the operational procedures, the risk matrix method is applicable. The expression of the risk matrix method is shown in Equation (7):

$$
R=P \times L
$$

where $R$ is the degree of risk, $P$ is the probability of risk events occurring, and $L$ is the consequences or losses due to a risk event.

The risk matrix method for the evaluation of cantilever casting concrete arch bridges is divided into the following three steps.

First of all, based on fuzzy theory and Bayesian networks, a risk assessment model for the construction process is established, and the risk probability is calculated based on this model. Second, based on a detailed investigation of this information, the degree of damage caused by different accidents involving bridge hanging baskets is determined, and then the relevant risk and loss levels are determined. Third, the probability $P$ of risk event occurrence is combined with the loss level $L$ of the risk event, and the risk $R$ is determined based on Equation (7). Next, the risk acceptability criteria are set, and their acceptability level is evaluated. Finally, relevant rectification measures are determined.

The specific meaning of the probability of a safety risk in the construction of cantilever casting concrete arch bridges is the probability of the occurrence of a hazard, which can be calculated by combining expert ratings, triangular fuzzy numbers, and Bayesian networks. The results are shown in Table 2.

Table 2. Probability of occurrence of safety risks in the construction of cantilever casting concrete arch bridges.


The degree of risk loss in the construction of cantilever casting concrete arch bridges refers to the degree of construction accident losses, mainly considering casualties and economic losses. The results are shown in Table 3.

Table 3. The degree of loss associated with safety risks in the construction of cantilever casting concrete arch bridges.


The acceptability levels and response measures for safety risks are also divided into four levels, as shown in Table 4.

Table 4. Security risk levels and acceptability levels.


Finally, the safety risk assessment matrix for the construction of a cantilever casting concrete arch bridge is shown in Table 5. For this table, the level of risk was determined based on the likelihood of risk occurrence and the severity of the event.

Table 5. Risk assessment matrix for construction safety of cantilever casting concrete arch bridges.


# 4. Example of a Bayesian Risk Assessment Project for Cantilever Casting Concrete Arch Construction 

### 4.1. Project Overview

The proposed super-large bridge, Bridge A (see Figure 2), has a total span length of 287 m and a total length of 303 m , for which the aperture arrangement is $3 \times 20 \mathrm{~m}+$ $187 \mathrm{~m}+2 \times 20 \mathrm{~m}$. The main bridge is a reinforced concrete box arch bridge with a net span of 180 m , with a net rise-to-span ratio of $1 / 6$ and an arch axis coefficient of 1.99 . The construction scheme is cable suspension and cantilever pouring, with the main arch seat constructed in an open-cut form. The upper structure of the bridge approach comprises prestressed concrete T-beams, while the lower structure comprises column piers and pile foundations. The bridge abutment is a gravity U-shaped abutment, with an open-cut expanded foundation.
![img-1.jpeg](img-1.jpeg)

Figure 2. Vertical view of Bridge A.

### 4.2. The Process of Establishing a Bayesian Risk Source Analysis Model

The risk assessment process for the entire cantilever casting arch bridge construction process is shown in Figure 3.
![img-2.jpeg](img-2.jpeg)

Figure 3. Risk assessment process diagram for cantilever casting concrete arch bridge construction.
The Bayesian network structure diagram for Bridge A relies on the project's structural system and the corresponding characteristics of the cantilever casting concrete arch bridge. Using the risk source identification method proposed in this paper, the corresponding Bayesian network was established, as shown in Figure 4.

![img-3.jpeg](img-3.jpeg)

Figure 4. Bayesian network structure diagram for Bridge A.
After a Bayesian network was established, it was necessary to solve for the prior probability and conditional probability values of the risks.

Firstly, the prior probability was calculated.

The hanging basket construction risk is taken as an example from the list of risk sources for cantilever casting concrete arch bridge construction to illustrate the method for determining the prior probability of risk events.

The concept of prior probability is of great significance in the process of building Bayesian networks, and it also directly affects the accuracy of probabilistic risk results. There are various styles of risk events, each with its own unique characteristics; therefore, the probability distribution form also has various types. Therefore, the prerequisite for an accurate risk probability assessment is to select the appropriate prior probability of risk events. In most cases, accident data are lacking, but data can generally be obtained based on expert experience combined with relevant engineering data analysis.

According to Table 1, the values given by experts are triangular fuzzy numbers ( $a$, $b$, and $c$ ), which are difficult to directly use as prior probability values for calculating the risk probability of hanging basket construction in the application process. Therefore, it is necessary to adopt appropriate methods to convert these opinions into exact values, corresponding specifically to solving fuzzy numbers. In this study, the triangular membership function was selected to defuzzify the expert opinions; specifically, the mean area method was adopted. The defuzzification formula in this method can be specifically expressed as $(a+2 b+c) / 4$.

During the research process, the evaluation opinions of five experts were collected, taking the prior probability calculation of "inadequate anchoring after hanging the basket" as an example. Experts A-E rated the risk sources of inadequate anchoring after the construction of the hanging basket as "slightly high", "slightly high", "high", "high", and "high". The mean area method was then used to defuzzify these ratings and obtain clear scores. According to the relationship between risk assessments and triangular fuzzy numbers in Table 1, the corresponding scores $S_{k}$ for experts A-E were $0.7,0.7,0.875,0.875$, and 0.875 , respectively.

Similarly, the arithmetic mean values of the fuzzy numbers $\left(a_{v}, b_{v}\right.$, and $\left.c_{v}\right)$ provided by the experts were calculated according to Table 1; these were $0.62,0.82$, and 0.96 , respectively. The similarity $S L$ of the average fuzzy values was applied to calculate the weights for the experts' responses, using the calculation formula shown in Equation (8). The resulting similarity $S L$ values were $0.75,0.75,0.833,0.833$, and 0.833 , respectively. The expert weight coefficients were then calculated using these $S L$ values, as shown in Equations (9) and (10).

$$
S L\left(S_{k}, S_{v}\right)=1-\frac{\left(\left|a_{k}-a_{v}\right|+\left|b_{k}-b_{v}\right|+\left|c_{k}-c_{v}\right|\right)}{\sum_{k=1}^{n}\left(\left|a_{k}-a_{v}\right|+\left|b_{k}-b_{v}\right|+\left|c_{k}-c_{v}\right|\right)}
$$

where $a_{v}, b_{v}$, and $c_{v}$ are the mean values of $a_{k}, b_{k}$, and $c_{k}$, respectively. $S_{k}$ is the expert evaluation value, and $S_{v}$ is the arithmetic mean of fuzzy numbers evaluated by experts.

$$
\begin{gathered}
\omega_{k}=\frac{S L\left(S_{k}, S_{v}\right)}{\sum_{k=1}^{n} S L\left(S_{k}, S_{v}\right)} \\
\left(\omega_{A}, \omega_{B}, \omega_{C}, \omega_{D}, \omega_{E}\right)=(0.187,0.187,0.208,0.208,0.208)
\end{gathered}
$$

where $\omega_{k}$ is the expert weight coefficient, and $k \equiv \mathrm{~A}, \mathrm{~B}, \mathrm{C}, \mathrm{D}$, and E .
The prior probability for the risk source in which the rear anchoring of the hanging basket $P_{B 51-p i o r}$ is insufficient is shown in Equation (11).

$$
P_{B 51-\text { pior }}=\sum_{k=1}^{n} \omega_{k} \times S_{k}=0.809
$$

The risk sources of the construction hanging basket were then taken as the research object to determine the conditional probabilities of risk events for each sub-node risk source.

Firstly, a relative attribute judgment matrix for the sub-node risk sources was constructed. Based on the relative magnitudes of the seven levels in Table 1, the sub-node risk sources B51-B56 were evaluated. Based on the obtained results, the corresponding attribute judgment matrix was constructed, as shown in Figure 5.
![img-4.jpeg](img-4.jpeg)

Figure 5. Relative attribute judgment matrix for sub-nodes of risk source B5.
According to Table 1, the seven evaluation levels were converted into the corresponding triangular fuzzy numbers to obtain the corresponding fuzzy measure matrix. Then, the scores for each evaluation object were calculated according to Equations (2)-(4), as shown in Equation (12). The relative fuzzy weight calculation result is shown in Equation (13).

$$
\begin{aligned}
& {\left[\begin{array}{l}
S_{51} \\
S_{52} \\
S_{53} \\
S_{54} \\
S_{55} \\
S_{56}
\end{array}\right]=\left[\begin{array}{l}
\sum_{j=1}^{6} a_{1 j}, \sum_{j=1}^{6} b_{1 j}, \sum_{j=1}^{6} c_{1 j} \\
\sum_{j=1}^{6} a_{2 j}, \sum_{j=1}^{6} b_{2 j}, \sum_{j=1}^{6} c_{2 j} \\
\sum_{j=1}^{6} a_{3 j}, \sum_{j=1}^{6} b_{3 j}, \sum_{j=1}^{6} c_{3 j} \\
\sum_{j=1}^{6} a_{4 j}, \sum_{j=1}^{6} b_{4 j}, \sum_{j=1}^{6} c_{4 j} \\
\sum_{j=1}^{6} a_{5 j}, \sum_{j=1}^{6} b_{5 j}, \sum_{j=1}^{6} c_{5 j} \\
\sum_{j=1}^{6} a_{6 j}, \sum_{j=1}^{6} b_{6 j}, \sum_{j=1}^{6} c_{6 j}
\end{array}\right]=\left[\begin{array}{l}
1.1,1.9,2.9 \\
0.2,0.9,1.9 \\
2.4,3.3,4.1 \\
1.0,1.7,2.7 \\
1.7,2.5,3.3 \\
1.5,2.3,3.2
\end{array}\right]} \\
& {\left[\begin{array}{l}
\omega_{51} \\
\omega_{52} \\
\omega_{53} \\
\omega_{54} \\
\omega_{55} \\
\omega_{56}
\end{array}\right]=\left[\begin{array}{l}
0.14,0.15,0.16 \\
0.025,0.07,0.10 \\
0.30,0.26,0.22 \\
0.12,0.13,0.14 \\
0.21,0.19,0.18 \\
0.19,0.18,0.17
\end{array}\right]}
\end{aligned}
$$

The final risk weights (the conditional probabilities of the Bayesian network nodes) $P_{B 5-\text { conditional }}$ were then obtained via defuzzification using the mean area method, as shown in Equation (14).

$$
P_{B 5-\text { conditional }}=\left(\overline{\omega_{B 51}}, \overline{\omega_{B 52}}, \overline{\omega_{B 53}}, \overline{\omega_{B 54}}, \overline{\omega_{B 55}}, \overline{\omega_{B 56}}\right)=(0.15,0.068,0.26,0.136,0.198,0.18)
$$

The risk probability for the construction hanging basket risk source $P_{B 5-\text { all }}$ was obtained by combining the prior probability $P_{B 5-\text { pior }}$ and the conditional probability $P_{B 5-\text { conditional }}$ with the Bayesian total probability formula.

$$
P_{B 5-\text { all }}=P_{B 5-\text { pior }} \cdot P_{B 5-\text { conditional }}=0.313
$$

For the other six primary risk sources, the same method was used to analyze their impact on the overall construction risk of Bridge A. The relative attribute judgment matrix for the primary risk sources was determined through expert scoring, as shown in Table 6.

Table 6. Expert evaluation matrix for primary risk sources.


After the score calculation and defuzzification, the weights of the primary risk sources were obtained, as shown in Equation (16). According to Equation (16), the importance of the seven primary risk sources during the construction process of Bridge A is in the order B5 $>\mathrm{B} 3>\mathrm{B} 6>\mathrm{B} 2>\mathrm{B} 4>\mathrm{B} 1>\mathrm{B} 7$. The weight coefficients are the values of conditional probability $P_{A-\text { conditional }}$ in the Bayesian network.

$$
P_{A-\text { conditional }}=\left(\overline{\omega_{B 1}}, \overline{\omega_{B 2}}, \overline{\omega_{B 3}}, \overline{\omega_{B 4}}, \overline{\omega_{B 5}}, \overline{\omega_{B 6}}, \overline{\omega_{B 7}}\right)=(0.09,0.15,0.21,0.10,0.23,0.17,0.05)
$$

The calculation process for the conditional probabilities of the other secondary risk sources is similar to that for the seven primary risk source conditional probabilities mentioned above. The conditional probabilities of secondary risk sources during the construction process of this bridge were thereby obtained, as shown in Figure 6.
![img-5.jpeg](img-5.jpeg)

Figure 6. The conditional probabilities for the secondary risk sources corresponding to each primary risk source. (a-g) represent the primary risk source numbers B1-B7, respectively.

Combining the conditional probabilities and prior probabilities for the primary risk sources, the construction risk for Bridge A $P_{A}$ was ultimately obtained.

$$
P_{A}=P_{A-\text { pior }} \cdot P_{A-\text { conditional }}=\sum_{1}^{7} P_{B i-\text { pior }} \cdot P_{B i-\text { conditional }}=0.191
$$

A construction risk assessment of Bridge A was carried out using the risk loss assessment model established in Section 3.3. The risk level assessment results for the primary risk sources for Bridge A are shown in Table 7.

Table 7. Assessment results of primary risk sources for Bridge A.


From Table 7, it can be seen that the risk frequency level for Bridge A is largely "occasional", the level of loss is "serious", and the corresponding risk level is largely level III. The evaluation results indicate that there are significant risks during the construction process. Strict control of risks in the project should be implemented, and reasonable and effective risk reduction measures should be formulated.

# 5. Conclusions 

In this study, a construction risk assessment method for cantilever casting concrete arch bridges based on triangular fuzzy theory and Bayesian networks was proposed. The method was validated using an actual engineering construction, Bridge A, as an example. The main conclusions are as follows:
(1) Through a study of the construction process of cantilever casting concrete arch bridges, the main process of risk assessment in the construction process was summarized through collecting engineering data, decomposing the construction processes, identifying the risk sources during the construction processes, and determining the major risk sources. The construction procedure of cantilever casting concrete arch bridges was broken down, and a list of risk sources was established. The list comprises seven primary risk sources and thirty-three secondary risk sources.
(2) A risk assessment model for cantilever casting concrete arch bridge construction based on a Bayesian network was constructed, and the prior probability and conditional probability in the Bayesian network were calculated using triangular fuzzy numbers, laying the foundation for other calculations of construction risk probabilities through Bayesian networks in the future. The method of combining Bayesian networks and triangular fuzzy numbers not only can fully utilize the experience of experts, but also avoids the subjectivity of expert opinions. The established evaluation system has a clear hierarchy and clear results.
(3) Taking Bridge A as an example, the risk analysis process, calculation model, and reliability evaluation of cantilever casting concrete arch bridges were carried out, and the practicality of the proposed method of determining key node parameters of Bayesian networks using triangular fuzzy numbers was verified. The risk analysis showed that the risk frequency level and the level of loss of Bridge A can be described as "occasional" and "severe", respectively, and the corresponding risk level is level III, indicating the existence of significant risks during the construction process. Therefore, strict risk control for Bridge

A should be implemented during the construction process, and reasonable and effective risk reduction measures should be formulated.

Author Contributions: Writing—original draft, Z.H.; Writing—review and editing, Y.X., L.L. and S.W.; Methodology, M.W.; Data curation, B.L.; Funding acquisition, Z.H. and M.W. All authors have read and agreed to the published version of the manuscript.

Funding: This work was supported by the Natural Science Foundation of Hunan Province, China (grant numbers 2024JJ7170 and 2024JJ7077) and the Research Foundation of Education Bureau of Hunan Province, China (grant numbers 23B0732, 22A0561 and 23A0559).

Data Availability Statement: All data generated or analyzed during this study are included in this published article.

Conflicts of Interest: The authors declare no conflicts of interest.

# Appendix A 

Table A1. The breakdown table of construction operations for cantilever casting concrete arch bridges.


Table A2. List of risk sources for cantilever casting concrete arch bridge construction.

