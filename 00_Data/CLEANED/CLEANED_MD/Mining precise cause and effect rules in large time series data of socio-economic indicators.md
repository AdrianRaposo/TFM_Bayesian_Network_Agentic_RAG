# Mining precise cause and effect rules in large time series data of socio-economic indicators 

Swati Hira* and P. S. Deshpande

*Correspondence: dt11cse076@cse.vnit.ac.in Department of Computer Science and Engineering, Visvesvaraya National Institute of Technology, 440010 Nagpur, India


#### Abstract

Discovery of cause-effect relationships, particularly in large databases of time-series is challenging because of continuous data of different characteristics and complex lagged relationships. In this paper, we have proposed a novel approach, to extract cause-effect relationships in large time series data set of socioeconomic indicators. The method enhances the scope of relationship discovery to cause-effect relationships by identifying multiple causal structures such as binary, transitive, many to one and cyclic. We use temporal association and temporal odds ratio to exclude noncausal association and to ensure the high reliability of discovered causal rules. We assess the method with both synthetic and real-world datasets. Our proposed method will help to build quantitative models to analyze socioeconomic processes by generating a precise cause-effect relationship between different economic indicators. The outcome shows that the proposed method can effectively discover existing causality structure in large time series databases.


Keywords: Data mining, Cause-effect relationships, Causality, Temporal association, Temporal odds ratio

## Background

A system such as mechanical, biological or social-economic system consists of independent components. These components influence one another to maintain their activity for the existence of a system in order to achieve the goal of the system. The system changes behavior when a component is changed or removed significantly. This motivates us to find the reason or cause behind fault and discover the cause parameters in explaining the interactions among the components of a system or process. The causal discovery indicates not only that the indicators are correlated, but also how changing a cause variable is expected to induce a change in an effect variable. For example, with analyzed cause-effect relationships, we can predict potential effects before taking any actions (causes), which is useful in preventing inaccurate decision or policy making in the social-economical system. Time series data can be used to extract delayed relationship between two variables, for example, "CO2 emission occurring at a place might cause air pollution at another place after some delay". These lagged relationships signify the time lag between the cause-effect parameters. Identifying lagged relationships

[^0]
[^0]:    (c) 2016 The Author(s). This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted use, distribution, and reproduction in any medium, provided you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made.

between socioeconomic processes is challenging due to the presence of various complex dependencies in the data. This dependency among the various parameters has enabled us to identify relationships among different domain parameters in time series data (Madsen 2007; Geweke 1984). The cause-effect relationship for time series prediction is a step towards extracting the various existing causal relations between different domain, such as employment, education, agriculture and rural development etc. Causal discovery has been used in various fields with great success as bioinformatics (Needham et al. 2007), biology (Shipley 2002), earth sciences, etc. to identify protein interactions (Sachs et al. 2005; Chen et al. 2010), gene regulatory networks (Pinna et al. 2010; Friedman et al. 2007) and to study atmospheric teleconnections (Chu et al. 2005). It has also emerged in economics and social sciences (Spirtes et al. 2000; Neapolitan 2004) such as to improve the economic development (Easterly and Levine 2003) and growth (Asafu-Adjaye 2000) of a country and to study the impact of climate change (Ebert-Uphoff and Deng 2014; Deng and Ebert-Uphoff 2014). Before describing the proposed method to extract various causal rules, we explain the following example (Fig. 1) to show the motivation of our research.

Suppose we have set of indicators such as exercise, weight, diseases, calcium, alcohol, and bone growth etc. Various causal relationships can exists among them. An indicator may affect other instantly or after some time. For example, if a person takes alcohol he may feel a lack of energy (lethargy) instantly or after some time (Fig. 1a). If he takes alcohol frequently, the changes can be observed and it can be concluded that alcohol is one of the causes behind tiredness. We could identify the time between alcohol was taken and occurrence of lethargy and can also identify the amount of alcohol dose tends to cause the lethargy. More relationship like transitive can be analyzed between set of indicators (shown in Fig. 1), such as lack of exercise increases weight, which increases the chance of diseases (Fig. 1b, c). Many to one, shows the relationship such as if a person is taking the proper dose of calcium and vitamin D, it will help in bone growth i.e. bone growth requires both calcium and vitamin D. Figure 1d describes the cyclic relationship mean properties affecting each other in a cyclic manner, for example, lethargy increases weight which in turn also increases lethargy. These extracted relationships are referred as binary, transitive, many to one and cyclic respectively.
![img-0.jpeg](img-0.jpeg)

In this paper, we have proposed a method to extract various causal relationships as binary, transitive, many to one and cyclic with properties such as time required to occur an effect (as lag value), rate of change (of both cause and effect parameter) and strength of a relationship without using statistical information.

# Related work and contributions 

The common way to identify cause-effect relationships is to plan randomized controlled experiments, which is generally expensive and unattainable with a huge number of parameters. Therefore, much concentration is needed to discover cause-effect relationships from increased growth of the huge amount of observational data. Discovery of cause-effect relationships in large observational data is a demandable task. Pearl and Verma (1991) suggested a framework that discovered causal structures from connected conditional independence, based on that some techniques have been developed to identify the causal relationships. However, still it cannot discover causal structures effectively from large databases and also the computational cost is high for the discovery. Probabilistic dependence is one technique, used to represent causality. Probabilistic cause-effect relationships have been examined and suggested in the literature (Reinchenbach 1978; Reichenbach and Reichenbach 1991; Good 1959; Suppes 1970). More recently, Bayesian networks (Pearl 2014), graphical causal modeling have emerged as a leading technique for discovering causal relationships. Authors (Heckerman 1995, 1997; Zhang and Poole 1996; Waldmann and Martignon 1998; Nadkarni and Shenoy 2001) describe the techniques they have proposed for characterizing, interpreting and learning probabilistic independence among parameters. However, Bayesian network learning to discover complete cause-effect models is an NP-complete problem (Chickering 1996). Con-straint-based techniques are more efficient by avoiding the search for a generic Bayesian network. Currently, several constraint-based approaches have been implemented to identify causal relationships in large databases and achieved some satisfactory results (Cooper 1997; Silverstein et al. 2000; Mani et al. 2012; Pellet and Elisseeff 2008; Aliferis et al. 2010). These approaches use observational data to detect and learn causal structures using conditional independence among variables. It is significantly notable that these constraints-based approaches directly or indirectly implement the concept of Bayesian network learning, by creating a directed acyclic graph (DAG) which describes the conditional independence between variables (parameters). Even constraint-based methods shown promising results with large databases, they typically are designed to detect causality with few fixed structures in a directed acyclic graph (DAG), such as Y structures (Mani et al. 2012), CCC (Cooper 1997), and CCU (Silverstein et al. 2000).

Another technique in this area is Granger causality (GC) (Granger 1969). It has also been discussed in the previous literature (Lozano et al. 2009a, b; Arnold et al. 2007; Pang and Su 2010) and well known in economics causal inference. The method calculates the impact of one time series on another by finding out whether the response prediction can be improved by including the knowledge of a predictor or not. GC is reported to perform well for stationary time series data but is sensitive to non-linearity. All these methods infer directed networks. Although these methods are fast and, the inferred interactions are undirected. Moreover, these approaches are well suited for small sample data analysis (Veiga et al. 2007) but are not designed to detect combined causal parameters. Most

of the time, two or more parameters may enhance the strength of effects. Even when individual parameter does not cause more effect, together they may do. We noticed that discovering causal structures in observational data only is insufficient. So, the discovered relationships have to be verified with time series data and controlled experiments. Still, it is acceptable to remove noncausal relationships discovered from data. Causeeffect relationship discovery is to find a brief list of rules that are probably causal. These causal rules provide a set of statistically decisive relationships which are acceptable to embed cause-effect relationships. This differentiates between the causal and normal rule discovery.

Association rule mining (Agrawal et al. 1993) has an efficient and versatile means for discovering relationships in data (Han et al. 2011). Authors (Jin et al. 2012; Li et al. 2013; Ma et al. 2016) use the advantage of association rule mining for causality discoveries. Jin et al. (2012) discovers the causal relationships with multiple cause variables in large databases of binary variables and excludes non-causal associations. Researchers (Li et al. 2013; Ma et al. 2016) discover potential causal rules using cohort study (Euser et al. 2009; Fleiss et al. 2003) and capable to generate combine causal rules in observational data. Author (Li et al. 2015) presented four approaches PC, HITON-PC, CR-PA and CR-CS for causality detection around a given target variable and discuss their efficiency. The PC and HITON-PC methods are based on Bayesian network learning theory and use conditional independence tests to eliminate non persistent associations, CR-PA use association rule and partial association and CR-CS uses the concept of a cohort study.

These proposed methods are able to find single and combined causal rules effectively in small and large database with low and high dimensional data, but they are restricted to discrete data and unable to extract the cyclic relationships and strength of relationships, although causality can be observed in various hidden relationships. However, statistically predictable associations do not illustrate cause-effect relationships, although mostly causality is usually observed as an association in the dataset. Therefore, in this paper, initially we use the concept of temporal association (Ji et al. 2011) and odds ratio (Fleiss et al. 2003) to extract binary causal relationship and further other relationships are extracted.

To the best of our knowledge, there is no previous work on discovering cyclic and transitive causal relationships with properties as the rate of change of parameters and their relationship strength in time series data. We should observe that discovering causal relationships in observational and constraint-based data only are insufficient.

The contributions of this work are listed in the following:

- First, we present a method to extract cause-effect relationships like binary, transitive, many to one and cyclic in large time series database.
- Second, we define the concept of temporal association lag rule and temporal odds ratio to extract cause-effect relationships between various parameters.
- Third, we are generating more specific cause-effect rules like binary, transitive, many to one and cyclic with their relationship strength which is useful for strategic decisions.

Our proposed method is useful to extract time lagged relationships across different field indicators that can be used to understand the lagged response of one indicator on another and various relationships such as binary, cyclic, many to one and transitive. We show the utility of our approach by extracting some relationships between different field indicators. For example, the rule $($ Cereal production, $D, 2 \%, 2) \Rightarrow($ Agricultural raw materials exports, $3 \%$ ), indicates a causal rule that cereal production is directly related to agricultural raw materials exports and if it is changed by $2 \%$, it affects the export of agricultural raw material by $3 \%$ after 2 years. The proposed approach can be broadly applied to other problems in the temporal domain to extract various time lagged relationships.

# Preliminaries 

In this section, first we define the terms used in this paper. Then we define the concepts for describing proposed cause-effect relationship extraction method. Finally, we describe the formal definition of various cause-effect relationships, discovering such causal relationships is the aim of this paper.
This paper deals with continuous parameters. Since all the parameters are having different ranges and we are interested in finding relationships. So instead of taking the absolute value of parameters, the rate of change is used to extract the effect of change of one parameter on another parameter, each time series value is categorized as a positive rate of change $(U)$, a negative rate of change $(D)$ and no rate of change $(Q)$. To find an association between two parameters temporal association rule is used and defined using following terms:


$\delta \quad$ Minimum rate of change used to consider a significant change
$R_{i, k} \quad$ Parameters indicate type of change, defined as:

$$
R_{i, k}=\left\{\begin{array}{lll}
U & \text { if } & \gamma_{i, k} \geq \delta \\
D & \text { if } & \gamma_{i, k} \leq-\delta \\
Q & \text { if } & -\delta \leq \gamma_{i, k} \leq \delta
\end{array}\right\}
$$

The time series of parameter $P_{i}$ is converted into a set of tuple $\left\langle P_{i}, T_{k}, R_{i, k}\right\rangle$ where $T_{k}$ is $k$ th time period and $R_{i}=R_{i, k} \in\{U, D, Q\}$ indicates the positive, negative or no rate of change for $k$ th time unit. For example, if GDP is having a positive rate of change in 1970 than it is indicated by tuple $\langle\mathrm{GDP}, 1970, \mathrm{U}\rangle$.

Based on above structure of time series, the relationship between two parameters $P_{i}$ and $P_{j}$ for lag $l$ is defined using following terms:
$D_{i, j, k, l} \quad$ Parameters indicate direct relationship, defined as:

$$
D_{i, j, k, l}=\left\{\begin{array}{cc}
1 & \text { if }\left(R_{i, k}=U \text { and } R_{j, k+l}=U\right) \text { or }\left(R_{i, k}=D \text { and } R_{j, k+l}=D\right) \\
0 & \text { otherwise }
\end{array}\right\}
$$

i.e. the rate of change of $P_{i}$ matches with the rate of change of $P_{j}$ after time period $l$ $S_{D}\left(P_{i}, P_{j}, l\right) \quad$ Support count of direct relationship, defined as:

$$
S_{D}\left(P_{i}, P_{j}, l\right)=\sum_{k=1}^{n-l} D_{i, j, k, l}
$$

$\alpha_{D}\left(P_{i}, P_{j}, l\right) \quad$ Support percent of direct relationship, defined as:

$$
\alpha_{D}\left(P_{i}, P_{j}, l\right)=\frac{S_{D}\left(P_{i}, P_{j}, l\right)}{n-l}
$$

$I_{i, j, k, l} \quad$ Parameters indicate inverse relationship, defined as:

$$
I_{i, j, k, l}=\left\{\begin{array}{cc}
1 & \text { if }\left(R_{i, k}=U \text { and } R_{j, k+l}=D\right) \text { or }\left(R_{i, k}=D \text { and } R_{j, k+l}=U\right) \\
0 & \text { otherwise }
\end{array}\right\}
$$

i.e. the rate of change of $P_{i}$ is opposite to rate of change of $P_{j}$ after time period $l$ $S_{I}\left(P_{i}, P_{j}, l\right) \quad$ Support count of inverse relationship, defined as:

$$
S_{I}\left(P_{i}, P_{j}, l\right)=\sum_{k=1}^{n-l} I_{i, j, k, l}
$$

$\alpha_{I}\left(P_{i}, P_{j}, l\right) \quad$ Support percent of inverse relationship, defined as:

$$
\alpha_{I}\left(P_{i}, P_{j}, l\right)=\frac{S_{I}\left(P_{i}, P_{j}, l\right)}{n-l}
$$

$\Theta_{R} \quad$ Strength of relationship. It indicates toughness of relationship exists between parameters. The relationship between $P_{i}$ and $P_{j}$ is calculated as:

$$
\begin{aligned}
\Theta_{R}\left(P_{i}, P_{j}\right) & =\alpha * \log (n), & & \text { where } \\
\alpha & =\alpha_{D}\left(P_{i}, P_{j}, l\right) & & \text { or } \quad \alpha_{I}\left(P_{i}, P_{j}, l\right)
\end{aligned}
$$

With our approach, we first consider the temporal association between indicators $P_{i}$ and $P_{j}$ since an association is needed for a cause-effect relationship. User defined support count threshold are defined as follows:
$\alpha_{1} \quad$ Support count threshold for all causal relationships (considered as $70 \%$ for experimentation).
$\beta \quad$ Threshold for temporal odds ratio (considered as 3 for experimentation)Since $\alpha_{1}$ is set $70 \%, \beta$ is set to 3 .

Definition 1 (Temporal association) Using direct or indirect relationship [Eqs. (3)-(8)] temporal association can be defined as follows.

Temporal direct association Temporal direct association between two parameters $P_{i}$ and $P_{j}$ for time lag $l$ is defined as $P_{i} \xrightarrow{l} P_{j}$ if $\alpha_{D}\left(P_{i}, P_{j}, l\right) \geq \alpha_{1}$.
Temporal inverse association Temporal inverse association between two parameters $P_{i}$ and $P_{j}$ for time lag $l$ is defined as $P_{i} \xrightarrow{l} P_{j}$ if $\alpha_{I}\left(P_{i}, P_{j}, l\right) \geq \alpha_{1}$.
Next, we define the terms to calculate the temporal odds ratio of temporally associated parameters to check whether the temporal association rule $P_{i} \xrightarrow{l} P_{j}$ is also causal rule or not.
$C_{E}\left(P_{i}, P_{j}, l\right)=$ Count of the number of pairs when no rate of change in $P_{i}$ is associated with positive or negative rate of change in $P_{j}$ after time period $l$, defined as:

$$
C_{E}\left(P_{i}, P_{j}, l\right)=\sum_{k=1}^{n-l} E_{i, j, k, l}
$$

where $E_{i, j, k, l}=$ Parameters indicate neutral-change relationship, defined as:

$$
E_{i, j, k, l}=\left\{\begin{array}{cc}
1 & \text { if }\left(R_{i, k}=Q \text { and } R_{j, k+l}=U\right) \text { or }\left(R_{i, k}=Q \text { and } R_{j, k+l}=D\right) \\
0 & \text { otherwise }
\end{array}\right\}
$$

$C_{F}\left(P_{i}, P_{j}, l\right)=$ Count of the number of pairs when the positive or negative rate of change in $P_{i}$ is associated with no rate of change in $P_{j}$ after time period $l$, defined as:

$$
C_{F}\left(P_{i}, P_{j}, l\right)=\sum_{k=1}^{n-l} F_{i, j, k, l}
$$

where $F_{i, j, k, l}=$ Parameters indicate change-neutral relationship, defined as:

$$
F_{i, j, k, l}=\left\{\begin{array}{cc}
1 & \text { if }\left(R_{i, k}=U \text { and } R_{j, k+l}=Q\right) \text { or }\left(R_{i, k}=D \text { and } R_{j, k+l}=Q\right) \\
0 & \text { otherwise }
\end{array}\right\}
$$

$C_{N}\left(P_{i}, P_{j}, l\right)=$ Count of the number of pairs when no rate of change in $P_{i}$ is associated with no rate of change in $P_{j}$ after time period $l$, defined as:

$$
C_{N}\left(P_{i}, P_{j}, l\right)=\sum_{k=1}^{n-l} N_{i, j, k, l}
$$

where $N_{i, j, k, l}=$ Parameters indicate neutral relationship, defined as:

$$
N_{i, j, k, l}=\left\{\begin{array}{cc}
1 & \text { if }\left(R_{i, k}=Q \text { and } R_{j, k+l}=Q\right) \\
0 & \text { otherwise }
\end{array}\right\}
$$

Definition 2 (Temporal odds ratio) It quantifies how strongly the presence or absence of change in value of parameter $P_{i}$ effecting change in value of parameter $P_{j}$. Using above terms [Eqs. (11)-(16)] temporal odds ratio is defined as follows.

Temporal direct odds ratio Temporal direct odds ratio between two parameters $P_{i}$ and $P_{j}$ for time lag $l$ is defined as:

$$
O R_{D}\left(P_{i}, P_{j}, l\right)=\operatorname{Oddratio}_{D}\left(P_{i}, P_{j}, l\right)=\frac{S_{D}\left(P_{i}, P_{j}, l\right) * C_{N}\left(P_{i}, P_{j}, l\right)}{C_{E}\left(P_{i}, P_{j}, l\right) * C_{F}\left(P_{i}, P_{j}, l\right)}
$$

Temporal inverse odds ratio Temporal inverse odds ratio between two parameters $P_{i}$ and $P_{j}$ for time lag $l$ is defined as:

$$
O R_{I}\left(P_{i}, P_{j}, l\right)=\operatorname{Oddratio}_{I}\left(P_{i}, P_{j}, l\right)=\frac{S_{I}\left(P_{i}, P_{j}, l\right)}{C_{E}\left(P_{i}, P_{j}, l\right) * C_{F}\left(P_{i}, P_{j}, l\right)}
$$

In our experimentation, if the value of $C_{N}\left(P_{i}, P_{j}, l\right)$ or $C_{E}\left(P_{i}, P_{j}, l\right)$ or $C_{F}\left(P_{i}, P_{j}, l\right)$ between parameters is zero, we considered it as 1 to avoid infinite temporal odds ratio.

Further causal rules are defined using terms define in Definitions 1 and 2.

Definition 3 (Binary rule) A binary causal rule $\left(P_{i}, D, l\right) \Rightarrow\left(P_{j}\right)$, exists between $P_{i}$ and $P_{j}$ if there is temporal association rule $P_{i} \xrightarrow{f} P_{j}$ and $\operatorname{Oddratio}_{D}\left(P_{i}, P_{j}, l\right) \geq \beta$ or Oddratio $_{I}\left(P_{i}, P_{j}, l\right) \geq \beta$.

In experimentation results, we represent direct causal rule by $\left(P_{i}, D, l\right) \Rightarrow\left(P_{j}\right)$ and inverse by $\left(P_{i}, I, l\right) \Rightarrow\left(P_{j}\right)$.

This rule will serve as a forward pruning criterion where all parameters which are not associated with another parameter with non-zero lag value are excluded from the combination of future search. The minimum required support makes the search space manageable.

Definition 4 (Precise binary rule) A precise binary rule $\left(P_{i}, D, \delta_{1}, l\right) \Rightarrow\left(P_{j}, \delta_{2}\right)$, exists between $P_{i}$ and $P_{j}$ if there is binary rule $\left(P_{i}, D, l\right) \Rightarrow\left(P_{j}\right)$ and $\left(\delta=\delta_{1}\right)$, i.e. minimum growth rate of change of $P_{i}$ and $\left(\delta=\delta_{2}\right)$, i.e. minimum growth rate of change of $P_{j}$ and the rule will not hold either $\delta>\delta_{1}$ for $P_{i}$ or $\delta>\delta_{2}$ for $P_{j}$.

Definition $5\left(f \operatorname{score}\left(\delta_{1}, \delta_{2}\right)\right)$ A function is used to calculate the specificity of the rule. In the experimentation, it is defined as $f \operatorname{score}\left(\delta_{1}, \delta_{2}\right)=\delta_{1}^{2}+\delta_{2}^{2}$. If rule $\left(P_{i}, D, \delta_{1}, l_{1}\right) \Rightarrow\left(P_{j}, \delta_{2}\right)$ is satisfied for multiple value of $\delta_{1}, \delta_{2}$ than the rule which gives the maximum valid $f$ score is retained.

Based on binary causal rule, we try to extract other causal relationships as transitive, many to one (combined cause) and cyclic. We define these relationships as follows.

Definition 6 (Transitive rule) A transitive rule $\left(P_{i}, D, \delta_{1}, l_{1}\right) \Rightarrow\left(P_{j}, D, \delta_{2}, l_{2}\right) \Rightarrow\left(P_{k}, \delta_{3}\right)$, exists between $P_{i}, P_{j}$ and $P_{k}$ if there is $r 1:\left(P_{i}, D, \delta_{1}, l_{1}\right) \Rightarrow\left(P_{j}, \delta_{2}\right), r 2:\left(P_{j}, D, \delta_{2}, l_{2}\right) \Rightarrow$ $\left(P_{k}, \delta_{3}\right),\left(P_{i}, D, \delta_{1}, l_{3}\right) \Rightarrow\left(P_{k}, \delta_{3}\right), l_{3} \geq l_{1}+l_{2}$ and $r_{1}\left(P_{j}\right) \cap r_{2}\left(P_{j}\right) \neq \emptyset$.

Definition 7 (Combined cause rule) A many to one rule $\left(\left(P_{i}, D, \delta_{1}, l_{1}\right)\right.$, $\left.\left(P_{j}, D, \delta_{2}, l_{2}\right)\right) \Rightarrow\left(P_{k}, \delta_{3}\right)$, exists between $P_{j}, P_{j}$ and $P_{k}$ if there is $\left(P_{i}, D, \delta_{1}, l_{1}\right) \Rightarrow\left(P_{k}, \delta_{3}\right)$, $\left(P_{j}, D, \delta_{2}, l_{2}\right) \Rightarrow\left(P_{k}, \delta_{3}\right), S_{D}\left(P_{i}, P_{k}, l_{1}\right) \geq \alpha_{1}, S_{D}\left(P_{i}, P_{k}, l_{2}\right) \geq \alpha_{1}$ and $S_{D}\left(\left(P_{i}, P_{j}\right), P_{k}, l_{1}, l_{2}\right) \geq \alpha_{1}$.

Definition 8 (Cyclic rule) A cyclic rule $\left(P_{i}, D, \delta_{1}, l_{1}\right) \Leftrightarrow\left(P_{j}, D, \delta_{2}, l_{2}\right)$, exists between $P_{j}$ and $P_{j}$ if there is $\left(P_{i}, D, \delta_{1}, l_{1}\right) \Rightarrow\left(P_{j}, \delta_{2}\right),\left(P_{j}, D, \delta_{2}, l_{2}\right) \Rightarrow\left(P_{i}, \delta_{1}\right)$ and $S_{D}\left(\left(P_{i}, P_{j}\right), l_{1}, l_{2}\right) \geq \alpha_{1}$.

# Proposed method 

In this section, we described an algorithm based on the definitions. The algorithm is explained in five steps. Step 1 generates the binary causal rule. Step 2 generates more precise rules of binary causal rules. Steps 3, 4, and 5 generate the transitive, many to one and cyclic rules. Further, we give the explanation of each step of an algorithm. Table 1 represents the abbreviations used in the algorithm and in this paper. Let $P$ be a time

Table 1 Abbreviation table


series database in discrete form and $P_{j}$ is a time series of parameter $P_{j}$ have $U, D$, and $Q$ values as mentioned in the definitions, $z$ is a number of parameters in database $P$.

# Step 1: Binary rule generation 

Binary causal rule
Input: Time series database $P$
Initialize: $B R S=\varnothing, \alpha_{1}=70 \%, \beta=3$,
For $i=1$ to $z$ do begin
For $j=1$ to $z$ do begin
If $\left(P_{i} \neq P_{j}\right)$
For $l=1$ to $l_{\max }$ do begin
For $k=0$ to $n$ do begin

$$
\begin{gathered}
I f\left(\left(P_{1, k}=U \wedge P_{j, l+k}=U\right) \vee\left(P_{i, k}=D \wedge P_{j, l+k}=D\right)\right) \\
D_{i, j, k, l}++ \\
I f\left(\left(P_{i, k}=U \wedge P_{j, l+k}=D\right) \vee\left(P_{i, k}=D \wedge P_{j, l+k}=U\right)\right) \\
I_{i, j, k, l}++ \\
I f\left(\left(P_{i, k}=Q \wedge P_{j, l+k}=U\right) \vee\left(P_{i, k}=Q \wedge P_{j, l+k}=D\right)\right) \\
E_{i, j, k, l}++ \\
I f\left(\left(P_{i, k}=U \wedge P_{j, l+k}=Q\right) \vee\left(P_{i, k}=D \wedge P_{j, l+k}=Q\right)\right) \\
F_{i, j, k, l}++ \\
I f\left(P_{i, k}=Q \wedge P_{j, l+k}=Q\right) \\
N_{i, j, k, l}++
\end{gathered}
$$

end for // for loop closed of $K$ value
// Support calculation using equations (5) and (8)
$\alpha_{D}\left(P_{i}, P_{j}, l\right), \alpha_{I}\left(P_{i}, P_{j}, l\right)$
// Odds ratio calculation using equations (16) and (17)
$O R_{D}\left(P_{i}, P_{j}, l\right)$ and $O R_{I}\left(P_{i}, P_{j}, l\right)$
If $\left(\alpha_{D}\left(P_{i}, P_{j}, l\right) \geq \alpha_{I} \wedge O R_{D}\left(P_{i}, P_{j}, l\right) \geq \beta\right)$
Then $\alpha=\alpha_{D}\left(P_{i}, P_{j}, l\right), \operatorname{TOR}=O R_{D}\left(P_{i}, P_{j}, l\right), B R S=B R S U\left(P_{i}, P_{j}, D, l, \alpha, \operatorname{TOR}\right)$
If $\left(\alpha_{I}\left(P_{i}, P_{j}, l\right) \geq \alpha_{I} \wedge O R_{I}\left(P_{i}, P_{j}, l\right) \geq \beta\right)$
Then $\alpha=\alpha_{I}\left(P_{i}, P_{j}, l\right), \operatorname{TOR}=O R_{I}\left(P_{i}, P_{j}, l\right), B R S=B R S U\left(P_{i}, P_{j}, I, l, \alpha, \operatorname{TOR}\right)$
end for// for loop closed of lag value
end if
End for// for loop closed of parameter $j$
End for// for loop closed of parameter $i$
Answer $=B R S$
A causal rule may be generated for multiple lag values, the lag value which gives maximum support of rule will be considered. Suppose $P=\left\{P_{1}, P_{2}, P_{3}, P_{4}, P_{5}\right\}$, set of time series dataset and using this step 1 BRS generated results are as follows.
$\mathrm{BRS}=\left\{\left(P_{1}, P_{2}, D, \mathrm{l}, 75,4\right),\left(P_{1}, P_{3}, D, 2,73,4\right),\left(P_{2}, P_{3}, I, \mathrm{l}, 77,3\right),\left(P_{4}, P_{5}, I, \mathrm{l}, 71,6\right),\left(P_{2}\right.\right.$, $\left.\left.P_{5}, D, \mathrm{l}, 76,5\right),\left(P_{5}, P_{2}, D, \mathrm{l}, 72,4\right)\right\}$. Here $\left(P_{1}, P_{2}, D, \mathrm{l}, 75,4\right)$, describes that parameters $P_{1}$ and $P_{2}$ have a direct relationship with lag 1 , support 75 and $\operatorname{TOR}=3$, which indicates that $\left(P_{1}, P_{2}\right)$ are causally related, i.e. $P_{1}$ effects $P_{2}$ after 1 year. Similarly, by comparing support and their odds ratio between parameters for each tuple, the other binary causal relationship can be extracted and interpreted.

Explanation To describe this step, we consider the time series using rate of change as positive $(U)$ or negative $(D)$ of two parameters say $P_{j}$ and $P_{j}$ for a time period (91-97).

Let

$$
\begin{aligned}
T & =\{1991,1992,1993,1994,1995,1996,1997\} \\
P_{i} & =\{U, U, U, U, U, D, U\} \\
P_{j} & =\{D, U, U, U, U, U, U\}
\end{aligned}
$$

Here we calculate support value $\alpha$ for lag value $=1$.
Support value for lag value $1 \alpha_{D}\left(P_{i}, P_{j}, 1\right)=83 \%$ and temporal odd ratio (TOR), Oddratio ${ }_{D}\left(P_{i}, P_{j}, 1\right)=5$.
Since calculated $\alpha_{D}>\alpha_{1}$ and $\operatorname{TOR}>3$ the rule $\left(P_{i}, D, 1\right) \Rightarrow\left(P_{j}\right)$, is correct and exists for lag value 1 (i.e. $1 \neq 0$ ).

Relationship strength [using Eq. (10)] of this rule is, 70.13.
If time series data are given for some parameters, we can calculate $\alpha_{D}$ and TOR between parameters and rules can be extracted. So with the help of the above algorithm, we would be able to extract all two-variable causal relationships between parameters for a time series data set.

# Step 2: Specific rules generation 

In this step, we calculated the specific rule for binary causal rules generated in the above algorithm.

Let $\gamma_{i}$ and $\gamma_{j}$ are the rate of change of parameters $P_{i}$ and $P_{j}$ and parameters have a direct relationship.

Let $\delta_{i}$ maximum value of the rate of change of $P_{i}$, $\delta_{j}$ maximum value of the rate of change of $P_{i}$, $\delta_{i}$ minimum value of the rate of change $P_{i}$, $\delta_{j} $ minimum value of the rate of change $P_{j}$.
Calculation of interval value $\eta_{P_{i}}$ (increment, value for a parameter $P_{i}$ )

$$
\eta_{P_{i}}=\frac{\delta_{i} \max -\delta_{i} \min }{n} \text { and } \eta_{P_{j}}=\frac{\delta_{j} \max -\delta_{j} \min }{n}
$$

where $\delta_{i} \max$ or $\delta_{j} \max =\mu+2 \sigma$ and $\delta_{i} \min$ or $\delta_{j} \min =\mu-2 \sigma$

# Specific Rules 

Input $=B R S, \gamma_{1}, \gamma_{j}$
Initialization: $\delta_{i}=0, \delta_{j}=0, S R S=\emptyset, \operatorname{Previous}_{\max }=0, \operatorname{Current}_{\max }=0, \delta_{i} \operatorname{big}=0, \delta_{j} \operatorname{big}=0$
For each tuple $<P_{i}, P_{j}, D, \alpha, l, T O R>\in B R S$
For $\delta_{i}=\delta_{i} \min$ to $\delta_{j} \max$
For $\delta_{j}=\delta_{j} \min$ to $\delta_{j} \max$
flag $=$ Verify $\left(\gamma_{1}, \gamma_{j}, \delta_{i}, \delta_{j}, \alpha, l, T O R\right)$
If (flag==1)
Current $_{\max }=f$ score $\left(\delta_{i}, \delta_{j}\right) / /$ according to definition 5
if (Current $_{\max }>$ Previous $_{\max }$ )
$\delta_{i} \operatorname{big}=\delta_{i}, \delta_{j} \operatorname{big}=\delta_{j}$
Previous $_{\max }=$ Current $_{\max }$
End if// if closed of flag
else
$\delta_{j}=\delta_{j}+\eta_{P_{j}}$
End for// for loop closed of $\delta_{i}$
$\delta_{i}=\delta_{i}+\eta_{P_{i}}$
End for// for loop closed of $\delta_{i}$
$S R S=S R S \cup\left(P_{i}, P_{j}, D, \delta_{i}, \delta_{j}, l\right)$
End for// for loop closed of BRS
// Function to verify rule for specification
Boolean Verify $\left(\gamma_{i}, \gamma_{j}, \delta_{i}, \delta_{j}, \alpha, l, T O R\right)$
\{
For $k=0$ to $n$ do begin

$$
\begin{gathered}
I f\left(\left(\gamma_{i, k} \geq \delta_{i} \wedge \gamma_{j, l+k} \geq \delta_{j}\right) \vee\left(\gamma_{i, k} \leq \delta_{i} \wedge \gamma_{j, l+k} \leq \delta_{j}\right)\right) \\
D_{i, j, k, l} \\
I f\left(\left(\gamma_{i, k} \geq \delta_{i} \wedge \gamma_{j, l+k} \leq \delta_{j}\right) \vee\left(\gamma_{i, k} \leq \delta_{i} \wedge \gamma_{j, l+k} \geq \delta_{j}\right)\right) \\
I_{i, j, k, l} \\
I f\left(\left(\gamma_{i, k}=0 \wedge \gamma_{j, l+k} \leq \delta_{j}\right) \vee\left(\gamma_{i, k}=0 \wedge \gamma_{j, l+k} \geq \delta_{j}\right)\right) \\
E_{i, j, k, l} \\
I f\left(\left(\gamma_{i, k} \geq \delta_{i} \wedge \gamma_{j, l+k}=0\right) \vee\left(\gamma_{i, k} \leq \delta_{i} \wedge \gamma_{j, l+k}=0\right)\right) \\
F_{i, j, k, l} \\
I f\left(\gamma_{i, k}=0 \wedge \gamma_{j, l+k}=0\right) \\
N_{i, j, k, l}
\end{gathered}
$$

end for // for loop closed of $K$ value
// Support calculation using equations (5) and (8)
$\alpha_{D}\left(P_{i}, P_{j}, l\right), \alpha_{I}\left(P_{i}, P_{j}, l\right)$
// Odds ratio calculation using equations (16) and (17)
$O R_{D}\left(P_{i}, P_{j}, l\right)$ and $O R_{I}\left(P_{i}, P_{j}, l\right)$
If $\left(\left(\alpha_{D} \geq \alpha \wedge O R_{D} \geq T O R\right) \operatorname{or}\left(\alpha_{I} \geq \alpha \wedge O R_{I} \geq T O R\right)\right)$
return 1
else
return 0
\}

## Output: SRS

Let $\delta_{1}, \delta_{2}$ is the minimum rate of change of parameters $P_{i}, P_{j}$. Then, using this step 2 more specific causal rules $\left(P_{i}, D, \delta_{1}, l\right) \Rightarrow\left(P_{j}, \delta_{2}\right)$ can be generated. The rule indicates that $P_{i}$ and $P_{j}$ have a direct causal relationship with lag 1 and if $P_{i}$ is changed by $\delta_{1}$ it leads to change $P_{j}$ by $\delta_{2}$. Based on BRS results assumed in step 1 more specific rules can be generated as follows:
$\operatorname{SRS}=\left\{\left(P_{1}, P_{2}, D, 1 \%, 2 \%, 1\right),\left(P_{1}, P_{2}, D, 2 \%, 1 \%, 2\right),\left(P_{2}, P_{3}, D, 2 \%, 1.5 \%, 1\right),\left(P_{4}, P_{5}, I\right.\right.$, $\left.1.5 \%, 2 \%, 1\right),\left(P_{2}, P_{5}, D, 2 \%, 3 \%, 1\right),\left(P_{5}, P_{2}, I, 3 \%, 2 \%, 1\right)\}$.

Step 3: Transitive rule generation


Based on SRS results in step 2, tuple $\left(P_{1}, P_{2}, D, 1 \%, 2 \%, 1\right),\left(P_{2}, P_{3}, D, 2 \%, 1.5 \%, 1\right)$ and $\left(P_{1}, P_{2}, D, 2 \%, 1 \%, 2\right)$ satisfies all the conditions of transitive relation and generate a transitive rule

$$
\left(P_{1}, D, 1 \%, 1\right) \Rightarrow\left(P_{2}, D, 2 \%, 1\right) \Rightarrow\left(P_{3}, 1 \%\right)
$$

If the same parameter has a different rate of change in different rules minimum of them is considered.

Explanation To understand this, we consider the time series of three parameters $P_{i}, P_{j}$, and $P_{k}$ as follows.

Let TOR $>3$ and $\delta_{1}, \delta_{2}, \delta_{3}$ is the rate of change of parameters $P_{i}, P_{j}, P_{k}$. Calculate support values from Table 2 is:

Support value of $P_{i}(U)$ and $P_{j}(D), \alpha_{i j}\left(P_{i}, P_{j}, 1\right)=77.7$.
Support value of $P_{j}(D)$ and $P_{k}(D), \alpha_{j k}\left(P_{j}, P_{k}, 1\right)=88.8$,
Support value of $P_{i}(D)$ and $P_{k}(D), \alpha_{i k}\left(P_{i}, P_{k}, 2\right)=75$,
Since $\alpha_{i j}>\alpha_{1}, \alpha_{j k}>\alpha_{1}, \alpha_{i k}>\alpha_{1}$, generated binary causal rules are

$$
\left(P_{i}, I, \delta_{1}, 1\right) \Rightarrow\left(P_{j}, \delta_{2}\right),\left(P_{j}, D, \delta_{2}, 1\right) \Rightarrow\left(P_{k}, \delta_{3}\right),\left(P_{i}, I, \delta_{1}, 2\right) \Rightarrow\left(P_{k}, \delta_{3}\right)
$$

Table 2 Parameter time series


The condition $l_{3} \geq 2(1+1)$ is also satisfies and generated transitive rule is $\left(P_{i}, I, \delta_{1}, 1\right) \Rightarrow\left(P_{j}, D, \delta_{2}, 1\right) \Rightarrow\left(P_{k}, \delta_{3}\right)$.

# Step 4: Many to one (combined causal) rule generation 


Based on SRS results in step 2, tuple $\left(P_{1}, P_{2}, D, 2 \%, 1 \%, 2\right),\left(P_{4}, P_{5}, I, 1.5 \%, 2 \%, 1\right)$ and using this step 4 generated combined causal rule is $\left(\left(P_{1}, D, 2 \%, 2\right),\left(P_{4}, I, 1.5 \%, 1\right)\right) \Rightarrow\left(P_{3}, 1 \%\right)$.

Explanation Let we have the following values for parameters $P_{i}, P_{j}$, and $P_{k}$.
Let TOR $>3, \delta_{1}, \delta_{2}, \delta_{3}$ is the rate of change of parameters $P_{i}, P_{j}, P_{k}$. Calculate support values from Table 3 as: Support value of $\alpha_{i k}\left(P_{i}, P_{k}, 1\right)=77.7 \%$, Support value of $\alpha_{j k}\left(P_{j}, P_{k}, 1\right)=88.8 \%$.

Calculated support values $\alpha_{i k}, \alpha_{j k}$ and $\alpha_{i j k}>\alpha_{1}$ which satisfies Definitions 4 and 7. In Table 3 highlighted rows indicates the $\left(\left(P_{i}, P_{j}\right), P_{k}\right)$ relationship. Since all the conditions are satisfied the generated combined rule is $\left(\left(P_{i}, I, \delta_{1}, 1\right),\left(P_{j}, I, \delta_{2}, 1\right)\right) \Rightarrow\left(P_{k}, \delta_{3}\right)$.

## Step 5: Cyclic rule generation


Based on SRS results in step 2, tuple $\left(P_{2}, P_{3}, D, 2 \%, 3 \%, 1\right),\left(P_{5}, P_{2}, I, 3 \%, 2 \%, 1\right)$ and using this step generated cyclic rule is $\left(P_{2}, D, 2 \%, 1\right) \Leftrightarrow\left(P_{5}, D, 3 \%, 1\right)$.

Explanation To understand this rule, we consider two parameters say $P_{i}$, and $P_{j}$, for a time period 1998-2015. Let $\delta_{1}$ and $\delta_{2}$ are rate of change for parameters $P_{i}, P_{j}$ which have the following values.

We can identify that relationship $\left(P_{i}, I, \delta_{1}, 1\right) \Rightarrow\left(P_{j}, \delta_{2}\right),\left(P_{j}, I, \delta_{2}, 1\right) \Rightarrow\left(P_{i}, \delta_{1}\right)$, are satisfied in Table 4 from Definition 4. In Table 4, the time period satisfies cyclic relation

Table 3 Parameter time series


Italic letters indicate the temporal association between parameters for given time. For example, $\mathrm{P}*{\mathrm{i}}$ and $\mathrm{P}*{\mathrm{j}}$ are associated for lag 0 in 1991 and $\left(\mathrm{P}*{i}, \mathrm{P}*{j}\right)$ are associated with $\mathrm{P}*{\mathrm{k}}$ at lag $1.5 \mathrm{o}, \mathrm{P}*{\mathrm{i}}$ and $\mathrm{P}*{\mathrm{j}}$ values are italic at 1991 and $\mathrm{P}*{\mathrm{k}}$ at 1992

Table 4 Parameter time series


between parameters is $\{(1988-1991),(1990-1992),(1992-1994),(1993-1995),(1995-$ 1997), (1996-1998)\}. For example (1988-1991) indicates that if $P_{i}$ increases in $1988 P_{j}$ goes down in 1989 which in turn increases $P_{i}$ in 1990. Calculated support value $\alpha_{i j}$ for parameters $P_{i}$ and $P_{j} ; 75 \%$. Since $\alpha_{i j}>\alpha_{1}$ cyclic relation is satisfied and generated cyclic causal rule is $\left(P_{i}, I, \delta_{1}, 1\right) \Leftrightarrow\left(P_{j}, I, \delta_{2}, 1\right)$.

# Experiments

We implemented our method using Java programming language with Net Beans IDE 7.3. The computation time to check the causal relationship between parameters is high using serialized programming. So we use a parallelization approach in our program using threads in Java on a machine with configuration Dual-Core CPU contains 12-Cores, 8 GB RAM, and 64-bit Windows 7 Operating System. Our goal is to discover various causal relationships between the different economic parameters. Firstly, we find all the binary causal rules (i.e. one cause and one effect parameter) and then other causality rules are discovered using proposed method. For experimentation, minimum support threshold $\alpha_{1}$ is set $70 \%$ and $\beta$ is set 3 .

# Dataset 

The approach is discussed using 2 synthetic and 3 real-world dataset. Table 5 shows the summary of data sets. The synthetic dataset is generated using R software based on Bayesian network (BN). First, we create random numbers, next build a BN on it and then generate the data from BN. Real world economic datasets are obtained from the World Trade Organization (1995), International Monetary Fund (1945) and World Bank data (1944). The WTO provides data on international trade in merchandise and commercial services. IMF contains time series data of 189 countries on economic parameters. World Bank contains time series data from 250 countries on a variety of topics such as agriculture, education, health, and an environment, etc. In World Bank and IMF, both we tested our algorithm for south-Asian countries (India, Pakistan, Sri Lanka, Bangladesh, Nepal, Bhutan and the Maldives, Afghanistan). In WTO, we used the data of Merchandise trade: Network of world merchandise trade in Asia.

All the datasets are selected to test the effectiveness of proposed method. In our experiments first, we preprocess the continuous data set [Eq. (1)] and represented them by positive, negative and neutral (no) rate of change as $U, D$, and $Q$ value [Eq. (2)] from the primitive data sets.

## Results

This section presents the various extracted causal relationships for World Bank data sets. Results on other datasets are shown in "Comparison" section. To save space, at below, we omitted all relationships and consider only those relationships which are present in multiple countries and displaying some of them. The discovered causal rules with our approach are shown in Table 6 for south-Asian countries. In Table 6 causal relationship between parameters is described with its support, strength and rate of change of indicators. For example, a rule (Cereal production, $D, 3 \%, 1$ ) $\Rightarrow$ (Crop production index, $1 \%$ ), indicates direct relationship, i.e. increase in cereal production by $3 \%$, will increase the crop production index by $1 \%$ after 1 year. This rule is discovered in four countries Srilanka, Nepal, Pakistan and India with different strength and support values. On the basis of support and strength value, we can say that this rule is more valid for Nepal rather than the other three countries. We can also identify a rule which has more valid for a country. In Table 6 from the binary causal rule, we can observe that three rules are present in India and above discussed rule is more valid than other rules in India. The transitive causal rules: (Rural population, $D, 1 \%, 1$ ) $\Rightarrow$ Population density, $D, 0.33 \%, 1) \Rightarrow$ Population, total, $0.68 \%$ ) can be described as, a $1 \%$ increase in rural population increase population density by $0.33 \%$ after 1 year, which tends to increase

Table 5 Datasets


Table 6 Causality rules


the total population by $0.68 \%$ after a year. This rule is present in four countries, Afghanistan, India, Maldives, and Nepal. The rule is having more impact on India. As compared to binary and transitive causal rules, the algorithm extracts the less number of causal rules for many to one (combined causal) and cyclic. The many to one causal rule: \{(Forest rents, I, $5 \%, 2$ ), (Foreign direct investment, $D, 3 \%, 1$ ) $\} \Rightarrow$ (Crop production index, $7 \%$ ) indicates that the decrease in forest rent by $5 \%$ and increase in foreign direct investment by $3 \%$ would tend to increase the crop production index by $7 \%$. The cyclic causal rule: (Gross domestic savings, $D, 1 \%, 1) \Leftrightarrow$ (Cereal yield, $D, 0.5 \%, 2$ ) can be described as, a $1 \%$ increase in gross domestic savings increase cereal yield by $0.5 \%$ after a year and increases in cereal yield would again increase gross domestic savings after 2 years. Similarly, other rules in all causal relationships can be analyzed.

# Prediction effectiveness 

The rules can be validated by calculating the mutual information (Meyer 2014) between indicators and the conditional entropy (Marsh 2013; Meyer 2014) change of the indicator before and after applying the rule. It is shown in Table 7 that the indicators are mutually related and the entropy of the indicator is decreased after applying the rule.

Table 7 results show that the target indicator entropy is decreased after the rule is applied, which represents that indicator value is more uncertain when it is considered alone. For example, the large value of mutual information between CP and ARME, indicates that the two indicators are related and the entropy of ARME is decreased after the rule $C P \rightarrow A R M E$ is applied. So it can be concluded that the proposed method achieves high prediction effectiveness. We validated all the generated causal rules using the concept of decrease in entropy and mutual information to check their prediction effectiveness. Generated causal rules can also be validated using time series graphs shown in "Appendix".

## Scalability

Further, we do experimentation to evaluate the scalability of the algorithm with the involved years and the number of indicators. Considering Figs. 2 and 3, it could be seen that, the proposed cause-effect discovery method scales up with the number of indicators. We examine the performance degradation of the algorithm on the basis of various causal rule discoveries for nine different scales (number of indicators): 50, 75, 100, 125,

Table 7 Entropy of indicators


![img-1.jpeg](img-1.jpeg)

![img-2.jpeg](img-2.jpeg)

Fig. 3 Scale up of indicators for other causal rules
$150,175,200,225$ and 250 . The minimum support threshold is set 70 , and it remains the same in all the experiments.

As shown in Fig. 2, the extraction time increases squarely with the number of indicators. More important, the curve is parabolic, which means that the performance of our algorithm is non-linearly related to the increase of number of indicators in binary causal rules. Though the time for generation of the binary causal rule is increasing squarely with a number of indicators, time for generation of other rules is not non-linear because the generation of other rules uses the result of binary rule generation (in Fig. 3).

The proposed method is able to extract nonlinear relationship from extracted causal rules because we are dealing with change of values as the rate of change and this change can be linear or nonlinear.

# Discussion 

## Comparison

To assess the efficiency of the proposed method, we compared proposed method with both statistical and non statistical methods. Statistical (Granger causality, Bayesian network) methods comparison is performed using R software packages as lmtest (Hothorn et al. 2015) for GC and bnlearn (Scutar 2016) for BN. In BN we calculate the results using constraint based local discovery algorithm hiton.pc (Aliferis et al. 2003). For nonstatistical approaches, we implemented the methods (Silverstein et al. 2000; Jin et al. 2012; Li et al. 2013) in Java for causal rule discovery.

First, we compared proposed method with GC and BN. GC is the base method to detect lag relationship in stationary time series data set. We run GC for different lag values with significance level, $\alpha=0.05$. HITON-PC is an effective algorithm of BN to extract parent-child relationship. So we considered both statistical methods as a benchmark for accuracy comparison. Tables 8 and 9 describe that all the binary rules which are generated in all the datasets by other methods are also generated by the proposed method. For example in the synthetic-2 dataset, we described the rule related to indicator $\mathrm{I}_{7}$ and $\mathrm{I}_{8}$. In the statistical approach from Table 8 , we can observe that the GC can discover only binary causal rules while BN can discover transitive as well as binary rules

Table 8 Comparison of proposed method with statistical method


between indicators. For example, in a BN graph like $I_{1} \rightarrow I_{3} \rightarrow I_{6}$ can be generated, but $I_{1}$ and $I_{6}$ are independent, i.e. $I_{1}$ and $I_{6}$ may or may not be dependent. In proposed method $I_{1}$ and $I_{6}$ are conditionally dependent or $I_{1}$ is an indirect cause of $I_{6}$.

Second, we compared our method with non-statistical methods. From Table 9 it can observe that binary and combined (many to one) causal relationship can be discovered by Jin et al. (2012) and Li et al. (2013) in all datasets. Silverstein et al. (2000) can also detect many to one rule but independently. For example, if we consider the rule $\left(I_{2}\right.$, $\left.I_{4}\right) \rightarrow I_{5}$ in the synthetic-1 dataset it would be considered as $I_{2} \rightarrow I_{5} \leftarrow I_{4}$, i.e. $I_{2}$ and $I_{4}$ affect $I_{5}$ independently, so we have not considered the many to one rule generated in a method (Silverstein et al. 2000). A transitive relationship is extracted by Silverstein et al. (2000) and proposed method. Relationships extracted by various methods are shown in Tables 8 and 9.

Based on the experimental results, it is reasonable to conclude that proposed method is capable to extract various causal relationships and causal rules like cyclic and the transitive causal rule cannot be extracted by other methods. Although non-statistical methods can generate combined causal rules, but are not generating specific rule and relationship strength. One more advantage of our method is that it also generates more specific rule and their strength between indicators. For example, when we run our algorithm

Table 9 Comparison of proposed method with non statistical method


on the synthetic-1 dataset, rules are extracted with various properties as lag value (time period after which one affects another indicator), strength and the rate of change of indicators i.e. positive or negative percent change. Actually, the rule $I_{1} \rightarrow I_{3}$ is extracted as $\left(I_{1}, I, 2 \%, 1\right) \Rightarrow\left(I_{3}, 1 \%\right), 113.6$, which indicates $2 \%$ change in $I_{1}$ inversely effect $1 \%$ change in $I_{3}$ after 1 year with 113.6 relationship strength. The results of proposed method are also demonstrated with real world data sets, as described in the following.

To investigate various causal rules in the real world cases, we run the proposed algorithm on the three real world data sets shown in Table 5 for performance evaluation. The proposed algorithm generates various binary, many to one, transitive and cyclic rules, some of the causal rules are reasonable as judged by common sense, shown in Table 8. For example, from the IMF data set, it is found that increases in general government revenue would also increase the volume of exports of goods, increase in growth of general government revenue and gross national saving effect to increase in total investment, and a decrease in government revenue can lead to decreased exports of goods too. Some interesting causal relationships are also extracted in the WTO and World Bank dataset. For example, if crop production of a country is increased, it effects to increase the export of agriculture raw material which helps to improve the economic growth of a country.

# Performance evaluation 

This section presents measures for assessing how accurately our proposed method can generate causal rules. The used accuracy measures (Han et al. 2011) are Precision, Recall, Specificity, F-score, Accuracy (recognition rate) and Misclassification rate. We evaluated all measures for proposed, statistical and non-statistical methods compared previously. Binary rules are considered to predict accuracy because this can be generated by all compared methods. Initially we classify the results in two classes as a causal rule (CR) and non-causal rule (NCR). Then, based on the CR and NCR results confusion matrix (TP, TN, FP, FN) is created to evaluate measures shown in "Appendix". Finally accuracy measures are calculated using TP, TN, FP and FN values. Performance of various methods is evaluated in real world, World Bank dataset for five different scales (numbers of indicators): 10, 20, 30, 40 and 50. Number of target indicators is set to 5 and remain same for all different scales. In Table 10, WBD-10 represents that 10 indicators are considered for causal rule extraction similarly others can be interpreted. Causal rules (some of them) extracted by most of the compared methods are shown in "Appendix". To indicate extracted causal rules significance appropriate references from previous literatures and documents are given. In Table 10, we can see that the proposed method can achieve higher accuracy and less error rate than all other statistical and non- statistical method for different scales of World Bank dataset.

The accuracy curve for proposed method and the compared methods is shown in Fig. 4. The proposed method can extract causal rules more accurately and performs the best in all different scales. We can also notice when the dataset size increases; the statistical method performance degrades more than non-statistical methods. We regard our proposed method has a stable and good performance accuracy in comparison with the other compared methods.

In summary the comparison results show that the proposed method has high performance and also performs well in terms of all accuracy measures as compare to other compared methods.

## Complexity

The steps defined in an algorithm to make minimum passes over the data. In the first pass, we calculate the growth rate of parameters and its positive, negative or neutral growth rate change value $U, D$, and $Q$ are assigned to each parameter to perform the next steps. In the second pass, we calculate the support value and an odds ratio of all the individual parameters together with other parameters for different lag values. Nonzero lag value associations identified from the tests are considered. Associations with insufficient support and odds ratio will be eliminated directly. The cause-effect rules in current pairs can be determined from temporal associations and temporal odds ratio for nonzero lag value. At the end, causal pairs found previously are combined for the next steps to generate transitive, many to one and cyclic rule using basic causal binary rule. To achieve efficiency, all the combinations are not considered as a condition during the generation of other causality rules. Instead, we only investigate the combinations appearing in the data which are related to non-zero lag value. Since such combinations are very small as compared to total combinations, the cost of computation is reduced.

Table 10 Prediction accuracy of proposed, statistical and non-statistical methods on different scales


To analyze the performance of the algorithm with respect to time and space complexity, and the number of passes over the data set, we denote the set of parameter $S$, the number of parameters $n$, the length of the time series $t$, the number of extracted pairs $m$ and the lag value $l$. The complexity of the method is discussed based on the extraction of binary causal rules in the form of $P_{1} \rightarrow P_{2}$ for lag value $l$.

The single parameters are paired and the support is calculated with $O(n)$ passes over the data set. Each pair combination needs to test for $l$ lag values to determine the

![img-3.jpeg](img-3.jpeg)

association and causality, which requires $O\left(n^{*} l\right)$ passes. In the process of extracting binary causal relationships, a causal association will be examined on all combinations.
The total number of possible pair combinations $P$ is:

$$
P=\sum_{n=1}^{|s|} \sum_{m=1}^{|s|}\left(s_{C_{m}-} s-m_{C_{n}}\right)
$$

So the data set needs to scan as many as $O(P n l)$ times. This way we can conclude the passes over the data set is $O(P n l)$, and the time it takes is $O(P n l t)$. Complexity will be substantially reduced by firstly applying the pruning step1 (binary rule generation) before extraction of other relationships.

# Conclusion 

This paper proposed a novel method to extract various types of causal relationship like binary, transitive, many to one and cyclic in large time series database. The proposed method is generating more specific rules and their strength which are useful for strategic information. We also defined the concept of temporal odds ratio to categorize temporal association as a causal rule. Experiments have shown that the proposed algorithm can extract single, transitive, combined and cyclic causes from large time series data sets. Additionally, the extracted rules are validated to prove their accuracy and the algorithms have been shown to scale up well with respect to the number of indicators on time series data.
In future, the efficiency of the method can be improved by using fast algorithms of mining association rule. The concept of the algorithm can also be extended to other types of time series. The proposed method can be applied in various social, economic, agriculture domains to generate strategic rules for decision making. The method is also useful to detect the exact cause of fault for the large mechanical system which is monitored by various sensors generating time series data.

Authors' contributions
SH conceived the idea, designed, analyzed and interpreted the data, involved in the system design and implementation, wrote and drafted the manuscript. PSD supervised the research, responsible for algorithm and manuscript revision for important intellectual content. He gave valuable advices on conducting the study and helped editing the article. Both authors read and approved the final manuscript.

## Acknowledgements

The authors would like to thank the department of Computer Science and Engineering, VNIT, Nagpur, for making available required computing facilities.

# Competing interests

The authors declare that they have no competing interests.

## Appendix

We can also examine the accuracy of the proposed method through by plotting time series graph between indicators. We have shown time series for four causal relationships. Table 11 shows the growth rate change of parameters for the time period 1972-2009.

Table 11 Growth rate change of indicators

(CP-
$(2) \rightarrow$ ARME) |  | Transitivity
(AR-(1) $\rightarrow$ AG-(3) $\rightarrow$ CO2) |  |  | Many to one
(FDI, FR)-(1) $\rightarrow$ CPI |  |  | Cyclic
GDP $\leftarrow(2,1) \rightarrow$ CY |  |   |

It represents a value with a lag difference. For example, consider a binary rule CP(2) → ARME, indicates CP effect ARME after 2 years. In Table 11 value 5.93, shows the growth rate of change of CP in 1972 and 4.35 in the same row shows the growth rate of change of ARME in 1974. Italic values represent the pairs which follow the relationship for a rule. Similarly, we can interpret all entries of other indicators.

All time series graphs are generated based on the values given in Table 11. Figure 5 shows the time lagged relations between Cereal Production (CP) and Agriculture raw material exports (ARME) with lag 2. A time period where indicators follow the direct relationship for given rule are: {1972, 1973, 1974, 1975, 1976, 1978, 1980, 1981, 1982, 1983, 1986, 1988, 1990, 1991, 1993, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2004, 2006, 2008, 2009}. For each time period (say 1974) rule would be interpreted as if the growth of CP has increased in the year 1974 it will increase ARME in 1976. In Fig. 5, time series graph we can observe that parameter satisfied the minimum support and odds ratio which indicates that indicators (CP and ARME) are causally related. Since most of the time, an increase in CP increases ARME, this relationship can be considered as a binary causal (U–U) direct relationship (Table 11).

Figure 6 shows the time lagged transitive causal relationship between AR, AG, and CO2 with lag 1 and 3. Time where indicators follow the relationship for given rule are: {1974, 1975, 1976, 1977, 1978, 1980, 1981, 1982, 1984, 1987, 1988, 1990, 1991, 1992, 1994, 1995, 1996, 1998, 2000, 2002, 2004, 2005, 2006}. For each time period (say 1974) rule would be interpreted as increase in AR in 1974 will increase AG in 1975 which again increases CO2 in 1978. From Fig. 6, we can conclude that the rule satisfied the minimum support and indicators (AR, AG, and CO2) are causally related. Most of the time increase in AR increases AG after 1 year, which again increases the CO2 after 3 years. This rule can be considered as a transitive causal (U–U–U) direct relationship (Table 11).

Figure 7 shows the time lagged many to one relation between (FDI, FR) and CPI with lag 1. Time period follows this relationship can be seen in many to one rule in Table 11 as italic values. In this relation, both indicators FDI and FR together affect CPI after 1 year. In Fig. 7, we can observe that if FDI increases and FR decreases they tend to increase the CPI, i.e. FDI and FR both are the cause of CPI. Indicators follow many to one (combined) causal (U,D)–U relationship. Table 12, shows confusion matrix (TP, TN, FP, FN) values to evaluate accuracy measures and Table 13, represents the causal rules extracted by most of the compared methods.

![img-4.jpeg](img-4.jpeg)

Table 12 Confusion matrix for proposed, statistical and non-statistical methods on different scales


![img-5.jpeg](img-5.jpeg)

Figure 8 shows the time lagged cyclic relations between GDP and CY with lag 2 and 1. Time period follows this relationship can be seen in the cyclic rule in Table 11 as italic values. In this cyclic relation, one more indicator GDP1 values are given which is nothing but the value of GDP after 3 years. Here GDP effect CY after 2 years, which again

Table 13 Extracted causal rules


![img-6.jpeg](img-6.jpeg)

![img-7.jpeg](img-7.jpeg)
affect GDP after 1 year, i.e. GDP follows cyclic relation with 3 years delay. In Fig. 8, we can observe that increase in GDP again increases it after 3 years. This cyclic relation follows the cyclic causal $\mathrm{U}-\mathrm{U}$ relationship.

Received: 16 March 2016 Accepted: 11 September 2016
Published online: 21 September 2016

# Submit your manuscript to a SpringerOpen ${ }^{\circledR}$ journal and benefit from: 

- Convenient online submission
- Rigorous peer review
- Immediate publication on acceptance
- Open access: articles freely available online
- High visibility within the field
- Retaining the copyright to your article

Submit your next manuscript at $\boldsymbol{\sim}$ springeropen.com