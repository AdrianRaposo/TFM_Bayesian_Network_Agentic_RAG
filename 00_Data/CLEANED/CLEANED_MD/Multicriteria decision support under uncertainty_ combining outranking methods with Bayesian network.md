# Multicriteria decision support under uncertainty: combining outranking methods with Bayesian networks 

Melodi Cebesoy ${ }^{1} \cdot$ Ceren Tuncer Şakar ${ }^{1}$ (D) $\cdot$ Barbaros Yet ${ }^{2}$<br>Received: 11 May 2023 / Accepted: 20 May 2024<br>(c) The Author(s) 2024


#### Abstract

Assessing alternative solutions that have uncertain evaluations in conflicting multiple criteria is not straightforward. Probabilistic models such as Bayesian networks (BNs) can effectively model and represent the uncertainty in such problems, but they do not include built-in mechanisms to guide different decision makers (DMs) with varying preferences toward the final decision. We propose a systematic approach to combine outranking methods with BNs to provide decision support for solutions with multiple and conflicting criteria under uncertainty. The proposed approach is based on Preference Ranking Organization Method for Enrichment Evaluation (PROMETHEE), and it offers different levels of precision and flexibility to the DMs in assessing the solutions. Our approach includes graphical tools and summary metrics to enhance the presentation of its results to the DMs. We test our approach with a case study on supplier selection where the uncertainty in supplier performances is modeled with a BN. We demonstrate that the proposed approach can enable the joint use of multiple criteria techniques with probabilistic modeling techniques like BNs to provide decision support in complex environments including uncertainty.


Keywords Multicriteria decision making $\cdot$ Bayesian networks $\cdot$ Outranking $\cdot$ Uncertainty $\cdot$ PROMETHEE $\cdot$ Supplier selection

[^0]
[^0]:    囚 Ceren Tuncer Şakar
    cerents@hacettepe.edu.tr
    Melodi Cebesoy
    melodicebesoy@hacettepe.edu.tr
    Barbaros Yet
    byet@metu.edu.tr
    1 Department of Industrial Engineering, Hacettepe University, 06800 Ankara, Turkey
    2 Department of Cognitive Science, Graduate School of Informatics, Middle East Technical University, 06800 Ankara, Turkey

# 1 Introduction 

A rational decision maker (DM) under uncertainty chooses the decision alternative with the maximum expected value. Modeling this choice requires an understanding of the DM's preferences, and reasoning with uncertainty to estimate the expected values of interest. Neither of these tasks are trivial when multiple criteria are involved in decisions and preferences. Usually, the criteria conflict with each other, and no solution has the best evaluations in all of them. When uncertainty is involved, computing the joint probability distribution of criteria evaluations is also challenging. Previous research on multicriteria decision making (MCDM) offers various methods to deal with the former challenge (see Greco et al., 2016; Cinelli et al., 2020), but often with limited or no support to deal with uncertainty. On the other hand, probabilistic graphical models, in particular Bayesian Networks (BNs), offer a general representation and powerful inference algorithms to deal with the latter. However, although BNs have been extended to deal with simple and sequential decision making problems, there has been little focus on providing a general approach to deal with multiple and conflicting criteria.

This paper focuses on decision making under uncertainty by combining the advances from the MCDM and BN domains. The main contribution of this paper is to present a general method to provide multicriteria decision support with BNs. We propose a systematic approach that combines outranking-type MCDM techniques with BN models. The proposed approach keeps the decision and uncertainty models separate, thus enabling modifications in either the uncertainty or the decision model without disturbing the other.

In particular, we extend Preference Ranking Organization Method for Enrichment Evaluation (PROMETHEE) (Brans et al., 1986) to work with BNs. Although there have been several attempts to combine MCDM approaches with BNs (Barton et al., 2020; Dohale et al., 2021; Fan et al., 2020; Kaya et al., 2023), previous studies lack a systematic and general approach to combine PROMETHEE with BNs. Extending the BN modelling toolbox with PROMETHEE is valuable as PROMETHEE offers several advantages compared to other MCDM methods including its flexibility in using different types of criteria, ranking procedures and preference functions. First of all, the criteria values in a decision problem may have different data types such as continuous, ordinal and binary. Unlike other widely-used MCDM methods such as weighted sum and Technique for Order Preference by Similarity to Ideal Solution (TOPSIS), PROMETHEE does not require normalization which makes it easier to work with both continuous and discrete criteria. Secondly, PROMETHEE has different variations that can provide complete or partial ranking of solutions. We work with PROMETHEE I and II to provide partial and complete rankings. Thirdly, the DM can express detailed preferences through a variety of preference functions and fine-tune those preferences with customized indifference and preference thresholds. Furthermore, the thresholds of PROMETHEE are not abstract values like the concordance and discordance thresholds used by the other popular outranking method, Elimination and Choice Translating Reality (ELECTRE).

Applying outranking methods under uncertainty, such as combining PROMETHEE with BNs, leads to partial and complete rankings that also involve uncertainty. For example, when a complete ranking is sought with uncertain criteria evaluations, a solution can have probabilities of being ranked the first, second and so on, rather than having a specific rank. This uncertainty makes it challenging to interpret the results. Another contribution of this paper is graph, plot and score-based tools to present the results of the proposed approach, and to provide decision support in a concise way.

We demonstrate the proposed approach both with a simple example and a supplier selection case study that involves several suppliers and criteria. The case study pairs the proposed approach with a BN that has been previously developed for multicriteria supplier evaluation (Kaya \& Yet, 2019). To account for the preferences of the DMs regarding the importance level of criteria, we work with different weight elicitation techniques and evaluate the sensitivity of the results to changes in preference weights.

In the remainder of this paper, Sect. 2 reviews the studies that handle uncertainty in MCDM, and also studies that use BNs and MCDM methods together. Section 3 presents the proposed approach, and Sect. 4 applies it to the supplier selection case study. We conclude the paper with discussions and future work in Sect. 5.

# 2 Related work 

### 2.1 Handling uncertainty in MCDM

Monte Carlo Simulation (MCS) has been widely used for incorporating uncertainty in MCDM problems. Previous studies used MCS to sample from the probability distributions of weights or criteria values. For example, Baudry et al. (2018) employed MCS in Multi Actor Multiple Criteria Analysis to decide on a biofuel option. They used Analytic Hierarchy Process (AHP) to derive the weights of criteria and select the best option. Betrie et al. (2013) studied the problem of selecting alternative mine sites when criteria weights have uncertainty. They used AHP and PROMETHEE to rank the alternatives, and uncertainty in weights was handled by fitting probability distributions and sampling from them using MCS. Dorini et al. (2011) focused on uncertainties in model inputs and weights of different DMs when comparing two alternative solutions. They applied compromise programming and MCS on a case study about comparing two sustainable electricity generation options. Baležentis and Streimikiene (2017) used additive ratio assessment, weighted aggregated sum and TOPSIS to evaluate effective energy planning scenarios. In their study, they made sensitivity analysis with different criteria weights using MCS.

Stochastic Multicriteria Acceptability Analysis (SMAA) (Lahdelma et al., 1998) is an approach based on MCS to handle uncertain or insufficient information in multicriteria problems. It considers probability distributions to provide measures for decision making. SMAA does not strictly rank the solutions, but determines the ones that can be candidates for selection. It calculates acceptability indices between 0 and 1 for the solutions, and the best solutions are accepted as the ones with the highest acceptability indices for the top ranks. Lahdelma and Salminen (2001) extended the SMAA approach to consider any possible rank. This extended method, SMAA-2, aggregates rank acceptability indices with metaweights to present an overall acceptability measure called holistic acceptability index. There are also different versions of SMAA that are combined with other MCDM methods; readers are referred to Pelissari et al. (2020) and Tervonen and Figueira (2008) for further information and a detailed literature review.

Fuzzy sets and logic are used to handle vagueness and ambiguity regarding linguistic information in decision problems (Özkan et al., 2014). Montazar et al. (2013) proposed an approach that uses fuzzy triangular numbers and AHP in order to make performance assessments of irrigation alternatives with fuzzy parameters. Kilic et al. (2014) performed a two-phase decision making method to select an appropriate Enterprise Resource Planning (ERP) system. They applied fuzzy AHP to handle varying criteria preferences, and then

employed TOPSIS to rank the alternatives. Pitchipoo et al. (2013) introduced an integrated model of fuzzy AHP and Grey Relational Analysis (GRA). Vagueness about criteria was modeled with fuzzy set theory and the alternatives were ranked with the help of GRA. Venkatesh et al. (2019) used fuzzy AHP to derive criteria weights, and fuzzy TOPSIS to find the best supplier for humanitarian supply chains.

The readers are referred to Durbach and Stewart (2012), Broekhuizen et al. (2015) and Pelissari et al. (2021) for more comprehensive reviews on MCDM approaches under uncertainty. Since our approaches are based on PROMETHEE, we provide a more specific review of studies that handled uncertainty in that family of methods in the next section.

# 2.1.1 Handling uncertainty in PROMETHEE 

Early work in PROMETHEE with uncertainty focuses on modeling the uncertainty and variation among multiple domain experts. Mareschal (1986) used PROMETHEE I and II with the average ranking of different experts to reach the final decision in a project selection problem. In more recent studies, Yuen and Ting (2012) proposed to use a fuzzy approach in PROMETHEE II to cope with uncertainty in solution evaluations. Kuang et al. (2015) used Grey Theory with PROMETHEE II to produce a ranking of alternative source water protection strategies. Maghrabie et al. (2019) focused on problems with small amount of data and uncertain information on criteria weights. They used maximizing deviation method and Grey Systems Theory to estimate the weights, and PROMETHEE II and degrees of possibility to rank the solutions. The stochastic dominance approaches in Zhang et al. (2010) and Liu et al. (2011) were also applied with PROMETHEE. They created dominance matrices based on stochastic dominance degrees, and used these matrices with PROMETHEE to find the rank order of solutions.

MCS has been a widely used approach to include uncertainty in PROMETHEE calculations too. Hyde et al. (2003) used probability distributions to model criteria weights and performance in PROMETHEE II scores. They used MCS to run the models and reported the probability of solutions occupying different ranks. Doumpos and Zopounidis (2010) made sensitivity analysis of PROMETHEE II parameters and criteria preferences using MCS. Shakhsi-Niaei et al. (2011) proposed a two-phase method for project selection where the first phase evaluates the projects with PROMETHEE and MCS, and the second phase utilizes MCS with integer programming to select a final project portfolio. Gervásio and Simões Da Silva (2012) fitted probability distributions to criteria and used MCS and PROMETHEE II to calculate the probabilities of alternatives holding possible ranks.

As discussed in the previous section, SMAA is used with uncertain data and unknown preferences of the DMs, and different versions combined with outranking approaches are available in the literature. Corrente et al. (2014) combined SMAA-2 with PROMETHEE I and II methods. Their method asks the DM to provide partial preference information on criteria and preference thresholds. For each solution $i$, SMAA-PROMETHEE I calculates the frequency of solution $i$ being preferred to every other solution $k$ (denoted $\mathrm{UP}(i, k)$ ) and the frequency of solution $k$ being preferred to $i$ (denoted $\operatorname{DOWN}(i, k)$ ). Taking all available solutions into account, solutions with the highest UP and lowest DOWN values are reported as the best ones. In addition, SMAA-PROMETHEE II provides rank acceptability indices by deriving the probabilities of solutions occupying each rank, the central weight vector, and the confidence factor. However, although the SMAA-PROMETHEE II method is based on SMAA-2 rules, it does not use the holistic acceptability index of SMAA-2 or introduce an overall measure to generate a ranking of solutions. Hubinont (2016) proposed a SMAA version of the Geometrical Analysis for Interactive Aid (GAIA) (Brans \& Mareschal, 1994),

which was developed to project the locations of alternatives according to all criteria on a plane. Another study proposed an extension of SMAA to work with nonmonotonic criteria in a group decision making setting (Liao et al., 2022).

Among the studies reviewed, Gervásio and Simões Da Silva (2012) and Corrente et al. (2014) are the most related to our approach since we also work with PROMETHEE II formulas and calculate the probability of solutions occupying different ranks based on criteria distributions. However, we combine PROMETHEE with BNs to evaluate the probability of solutions being preferred to others, and use SMAA-2 rules. Additionally, our approach provides a systematic methodology to use PROMETHEE with BNs in a comprehensive decision making process. We present graph, plot and score-based tools to present the results, and introduce an extension of the approach for applying data-driven outranking.

# 2.2 BN models and MCDM methods 

Influence Diagrams (IDs), which are extensions of BNs, have been proposed to deal with decision making problems (Howard \& Matheson, 2005). An ID has additional types of nodes for decision and utility variables. The computation of IDs is more complex than BNs as the model needs to calculate the utility distribution for all decision alternatives, and several algorithms are available (Jensen et al., 1994; Zhang, 1998). In MCDM problems, the preferences of the DMs can be encoded in the parameters of the utility nodes of IDs. This requires eliciting a utility value for all states of utility nodes, or an additive or multiplicative function for the utility nodes. For example, Watthayu and Peng (2004) built an ID for an MCDM problem about commuting. Delcroix et al. (2013) used IDs for a recurrent MCDM problem where the decision is made by a group of experts. Their model predicted both criteria importance and distributions within the model. Barton et al. (2020) integrated multi-attribute value functions in a BN model in order to evaluate environmental design alternatives, and modeled the problem as an ID. Shahzad (2022) studied on IDs to overcome interdependency and uncertainty issues of traditional MCDM problems, and used AHP to calculate utility values of nodes. In general, the use of IDs in complex MCDM problems requires the creation of large utility tables, which is not a straightforward task.

Combining MCDM approaches with BNs can provide more flexibility as it can exploit a wider selection of BN inference algorithms rather than using algorithms specifically designed for solving IDs. In this case, a suitable MCDM technique, such as sorting or ranking, can be selected depending on the properties of the decision problem. The use of BNs with MCDM methods in the literature is limited. As examples, Fenton and Neil (2001) illustrated how BNs can be used to calculate posterior probability distributions and constraints that could be paired with MCDM techniques. Mazaheri et al. (2010) used a BN of a questionnaire to predict fuzzy preference weights of a DM, and then used a fuzzy version of TOPSIS to recommend a decision based on the weights. Several studies combined BNs and TOPSIS to provide decision support and risk assessment for maritime safety (Fan et al., 2020, 2023; Yang et al., 2021). Fan et al. (2020) presented a method using BNs and TOPSIS to determine the best strategies for preventing marine accidents. Yang et al. (2021) combined BNs and TOPSIS to aid ship detention decision in port state control inspections. Fan et al. (2023) used BNs and TOPSIS to assess the risk of maritime piracy and to guide prevention actions. Accident types were treated as criteria, and accident occurrence probabilities were used as criteria weights. Kaya and Yet (2019) worked on integrating BNs with the Decision Making Trial and Evaluation Laboratory Method (DEMATEL). Kaya et al. (2023) extended the study of Kaya and Yet (2019) to provide a ranking of suppliers based on their overall performances.

To achieve this, they applied TOPSIS to the evaluation matrix presented by the BN model whose causal graph was determined with DEMATEL. The evaluation matrix derived from the BN model included deterministic criteria values, and they used AHP to derive criteria weights. In their case study, Kaya et al. (2023) built a BN model for supplier selection with 5 criteria. They conducted a sensitivity analysis to evaluate the effect of having missing information regarding suppliers on the rankings obtained from their approach. Quan and Cho (2014) used a combination of BNs and AHP to recommend television programs. BNs were used to learn user preferences from data, and AHP was used as a weighted combination of these preferences to make recommendations. Weight elicitation and consistency evaluation elements of AHP were not included in the study. Dohale et al. (2021) presented a three-phase approach to select a production system. In the first stage, decision criteria are determined using Delphi method, and their weights are derived by Voting AHP in the second stage. In the last stage, a BN model is constructed for each alternative using relative weights and prior probabilities in order to calculate its selection probability.

As the reviewed studies show, previous attempts to pair MCDM approaches with BNs are generally made for specific decision problems, and do not offer general guidelines about how to use multicriteria techniques with BN posteriors. In addition, majority of them focus on AHP, which is impractical for large problems, or TOPSIS, which requires normalization of criteria values and does not enable detailed preference expressions. As opposed to those studies, we propose a systematic method that uses the advantages of outranking techniques in developing a general decision support framework on BN outputs.

# 3 Methodology 

In this paper, we consider a decision problem where discrete alternatives evaluated with multiple criteria are to be partially or fully ranked, depending on the needs of the DM. The DM can judge the importance of criteria differently, thus criteria have importance weights. The criteria can be measured in different types of scales such as continuous, nominal and ordinal. In addition, we assume that the evaluations of alternatives are subject to uncertainty. In order to provide decision support in this problem, we propose a systematic approach to combine outranking approaches with BNs.

In Sect. 3.1, we provide background information on the methods we use in our approach. We present our approach to combine BNs and PROMETHEE in Sects. 3.2 and 3.3, our tools to present the results of this approach in Sect. 3.4, and an extension of this approach to datadriven PROMETHEE in Sect. 3.5. We conclude this section with a small illustrative example in Sect. 3.6.

### 3.1 Background information

This section includes technical information on BNs, PROMETHEE I and II methods, and the weight elicitation techniques we use.

### 3.1.1 Bayesian networks

A BN is a probabilistic graphical model that represents the conditional dependencies and joint probability distribution of a set of variables. The graphical structure of a BN is a directed acyclic graph in which nodes represent random variables, and edges represent direct causal

and associational relations between those variables. When a directed edge connects nodes $A$ and $B$ as in $A \rightarrow B, A$ is called the parent of $B$, and $B$ is called the child of $A$. Each node $X_{i}$ in the BN has a local probability distribution conditioned on its parents $p a\left(X_{i}\right)$ denoted by $P\left(X_{i} \mid p a\left(X_{i}\right)\right)$. The graphical structure encodes conditional independency assertions that enable the joint probability distribution to be defined in a compact and factorized way based on these local probability distributions. Each node is conditionally independent of its nondescendants given their parents. The joint probability distribution of the random variables can be decomposed into the product of the conditional probabilities of each node given their parents as in (1).

$$
P\left(X_{1}, \ldots, X_{n}\right)=\prod_{i=1}^{n} P\left(X_{i} \mid p a\left(X_{i}\right)\right)
$$

Figure 1 shows a BN example where the local conditional probability distributions are shown as probability tables. The joint probability distribution of this BN can be computed by the product of those distributions as in (2).

$$
\begin{aligned}
& P(B, C 1, C 2, C 3, F 1, F 2) \\
& \quad=P(C 3 \mid F 2) P(C 2 \mid B, F 2) P(C 1 \mid F 1) P(F 2 \mid B, F 1) P(F 1 \mid B) P(B)
\end{aligned}
$$

Efficient algorithms are available to compute the posterior probabilities when any subset of the nodes is instantiated by exploiting the conditional independence assertions (Lauritzen \& Spiegelhalter, 1988).

In MCDM problems, BNs offer a suitable tool to model the causal and associational relations, and joint probability distribution between the criteria based on a combination of domain knowledge and data (Kaya \& Yet, 2019; Yet et al., 2014). However, BNs do not incorporate DM preferences or decision making algorithms to reach a final solution in MCDM problems; they only compute the posterior probability distributions of their variables.

# 3.1.2 PROMETHEE 

The PROMETHEE methodology proceeds by making pairwise comparisons between all solutions in terms of each criterion involved in the problem. It assigns a preference value between 0 and 1 to each comparison; and using these preference values and the importance weights of criteria, it calculates aggregated measures of preferability of solutions. Take two alternative solutions $a_{i}$ and $a_{k}$, which have evaluations in $m$ maximization-type (without loss of generality) criteria; $a_{i}=\left(a_{i 1}, a_{i 2}, \ldots, a_{i m}\right), a_{k}=\left(a_{k 1}, a_{k 2}, \ldots, a_{k m}\right)$. To determine the preference strength of $a_{i}$ over $a_{k}$ with respect to criterion $j$, first the difference between their evaluations is found by $d_{i k j}=a_{i j}-a_{k j}$. A preference value is assigned to this difference using one of the six available preference functions. In Type I function, the preference value is 1 for all positive differences. In Type II function, the preference value is 0 until a positive indifference threshold is reached; after this threshold, the value is 1 . In Type III function, the preference value linearly increases from 0 to 1 for positive differences, and after a preference threshold is exceeded, it remains at 1 . There are three possible preference values in Type IV function; $0,0.5$ and 1 , which are determined by two thresholds. Type V function resembles Type III in using a linear function from 0 to 1 , but a threshold must be exceeded to start the climb. Lastly, Type VI function features a Gaussian function that goes from 0 to 1 nonlinearly. The first three functions are the most commonly used ones. Let the preference value of $a_{i}$ over $a_{k}$ with respect to criterion $j$ be $P_{j}\left(d_{i k j}\right)$. The aggregated preference index of $a_{i}$ over

![img-0.jpeg](img-0.jpeg)

Fig. 1 Bayesian network example
$a_{k}$ is calculated as in (3), where $w_{j}$ is the weight of criterion $j$. PROMETHEE works with pre-specified criteria weights that sum up to 1 , so $v_{i k}$ values are between 0 and 1 . Values closer to 0 represent weak global preference of $a_{i}$ over $a_{k}$ and values closer to 1 represent a strong global preference of $a_{i}$ over $a_{k}$.

$$
v_{i k}=\sum_{j=1}^{m} P_{j}\left(d_{i k j}\right) w_{j}
$$

After pairwise comparisons are conducted, PROMETHEE calculates overall preference indices for all solutions. In the presence of $n$ available solutions, positive flow of $a_{i}$, which implies how strongly $a_{i}$ outranks all other solutions, is denoted by $\varphi_{i}^{+}$and calculated as in

(4). Negative flow $\varphi_{i}^{-}$of $a_{i}$ is calculated as in (5), and it implies how strongly other solutions outrank $a_{i}$. A solution would be considered preferable if it has high positive flow and low negative flow.

$$
\begin{aligned}
& \varphi_{i}^{+} \quad=\sum_{k=1}^{n} v_{i k} \\
& \varphi_{i}^{-}=\sum_{k=1}^{n} v_{k i}
\end{aligned}
$$

There are two classic PROMETHEE methods that work with the flows calculated in (4) and (5), PROMETHEE I and PROMETHEE II. In PROMETHEE I, $a_{i}$ is preferred to $a_{k}$ if one of the following conditions hold:
(i) $\varphi_{i}^{+}>\varphi_{k}^{+}$and $\varphi_{i}^{-}<\varphi_{k}^{-}$
(ii) $\varphi_{i}^{+}=\varphi_{k}^{+}$and $\varphi_{i}^{-}<\varphi_{k}^{-}$
(iii) $\varphi_{i}^{+}>\varphi_{k}^{+}$and $\varphi_{i}^{-}=\varphi_{k}^{-}$

Solutions $a_{i}$ and $a_{k}$ are incomparable if one of the following conditions hold:
(i) $\varphi_{i}^{+}>\varphi_{k}^{+}$and $\varphi_{i}^{-}>\varphi_{k}^{-}$
(ii) $\varphi_{i}^{+}<\varphi_{k}^{+}$and $\varphi_{i}^{-}<\varphi_{k}^{-}$

Lastly, there is an indifference relationship between the solutions if $\varphi_{i}^{+}=\varphi_{k}^{+}$and $\varphi_{i}^{-}=\varphi_{k}^{-}$.
As a result of PROMETHEE I, it may not be possible to achieve full ranking of solutions since there can be incomparability or indifference between some pairs of solutions. In PROMETHEE II, a final score is calculated as in (6) that can be used to achieve full ranking.

$$
\varphi_{i}=\varphi_{i}^{+}-\varphi_{i}^{-}
$$

This $\varphi_{i}$ value is called the net flow of solution $a_{i}$, and solutions are ranked in decreasing order of their net flows; $r_{i}$ is the resulting rank of $a_{i}$. Due to the aggregation in (6), PROMETHEE II loses some level of outranking information given by positive and negative flows, but this allows it to produce a full rank list.

# 3.1.3 Elicitation of criteria weights 

Many MCDM approaches, including PROMETHEE, represent the preferences of DMs for criteria in the form of weights, but they do not have a built-in weight derivation procedure. Among different types of weight derivation approaches, rank-based methods come forward as simple and practical alternatives. In those methods, the DM provides an importance ranking of criteria. These ranks are then used to calculate their weights, which are suitable to be used in PROMETHEE. Rank sum (RS), rank reciprocal (RR) and rank order centroid (ROC) are the most common rank-based formulas. Among those, ROC has been shown to perform best with respect to matching the true preferences of the DM and identifying the true best solution (Ahn, 2011; Roszkowska, 2013).

The formulas for deriving the weight of the criterion that occupies the $t^{\text {th }}$ importance rank in RS, ROC and RR methods are given by (7), (8) and (9), respectively. ROC derives the weights by minimizing the maximum error of each weight from the centroid of all possible weights satisfying the given rank order of importance. RS assumes equal distance between

weights of consecutive ranks while RR and ROC increase the difference between consecutive weights as the rank positions get higher. RR puts more weight on the first rank than the other methods.

$$
\begin{gathered}
w_{t}(R S)=\frac{n-t+1}{\sum_{k=1}^{n} n-k+1} \\
w_{t}(R O C)=\frac{1}{n} \sum_{k=t}^{n} \frac{1}{k} \\
w_{t}(R R)=\frac{1 / t}{\sum_{k=1}^{n} 1 / k}
\end{gathered}
$$

# 3.2 Overview of combining PROMETHEE with BNs 

Figure 2 shows an overview of the proposed approach for combining BNs and PROMETHEE. Under uncertainty, a solution $a_{i}$ is a random variable and its evaluations for criteria have a probability distribution $p\left(a_{i 1}, a_{i 2}, \ldots, a_{i m}\right)$. We model this probability distribution in a BN model representing the problem, and query this model to get joint probabilities of evaluations under different conditions (Fig. 2a). For example, in a supplier selection problem, we build a causal BN model of the suppliers including the criteria variables, and use this model to get joint probability of criteria evaluations under different scenarios (see Sect. 4). Criteria weights are elicited from domain experts (Fig. 2b) and PROMETHEE operations for computing positive and negative flows are applied on these probability distributions (Fig. 2c). These operations result in a probability distribution of positive $p\left(\phi_{i}^{+}\right)$and negative flows $p\left(\phi_{i}^{-}\right)$. The ranking
![img-1.jpeg](img-1.jpeg)

Fig. 2 Overview of method for combining BNs and outranking MCDM approaches

results obtained from these distributions are presented to the DM with graphs, plots and summary metrics (Fig. 2d).

In PROMETHEE I, the preference between $a_{i}$ and $a_{k}$ is determined based on these probability distributions and a probability threshold value $\beta$.

Solutions $a_{i}$ and $a_{k}$ are incomparable if one of the following conditions holds:
(i) $p\left(\phi_{i}^{+}>\phi_{k}^{+}\right)>\beta$ and $p\left(\phi_{i}^{-}>\phi_{k}^{-}\right)>\beta$
(ii) $p\left(\phi_{i}^{+}<\phi_{k}^{+}\right)>\beta$ and $p\left(\phi_{i}^{-}<\phi_{k}^{-}\right)>\beta$

If solutions are not incomparable, $a_{i}$ is preferred to $a_{k}$ if the following condition holds:
(i) $p\left(\phi_{i}^{+}>\phi_{k}^{+}\right)>\beta$ or $p\left(\phi_{i}^{-}<\phi_{k}^{-}\right)>\beta$

Otherwise, there is indifference relationship between $a_{i}$ and $a_{k}$.
The threshold value $\beta$ is defined by the DM. A typical threshold value of $\beta=0.5$ indicates that the condition is more likely than its inverse. Higher $\beta$ values lead to more conservative preference options.

In PROMETHEE II, the probability distributions of net flows $p\left(\phi_{i}\right)$ are calculated with (10).

$$
p\left(\phi_{i}\right)=p\left(\phi_{i}^{+}-\phi_{i}^{-}\right)
$$

As a result, a solution does not have a specific rank under uncertainty; it has different rank probabilities $p\left(r_{i}\right)$ according to its net flow distribution $p\left(\phi_{i}\right)$.

# 3.3 Computing positive, negative and net flow distributions from BNs 

BNs are generative models. Once we have a BN model to compute the criteria evaluation distributions, the probability distributions $p\left(\phi_{i}^{+}\right), p\left(\phi_{i}^{-}\right)$and $p\left(r_{i}\right)$ can be estimated by generating samples from the BN. Various options are available to obtain samples from the posterior distribution of a BN model. The posterior distribution of a BN model with evidence can be calculated with exact algorithms such as junction tree, and the samples can be obtained from this posterior. Alternatively, rejection or importance sampling can be used to generate samples from the posteriors of an unpropagated BN. Following one of these approaches, we get samples $a_{i s}$ for each solution $a_{i}$ and sample $s$. The PROMETHEE formulas (3)-(5) can be applied on those samples to calculate $\phi_{i s}^{+}$and $\phi_{i s}^{-}$values. In PROMETHEE I, the probability distributions for the preference conditions can be estimated by counting the samples that the condition holds. Let $S$ be the set of all samples, and $S_{\phi_{i}^{+}>\phi_{k}^{+}}$be the subset of $S$ where the positive flow of solution $a_{i}$ is greater than $a_{k}$, and $S_{\phi_{i}^{-}<\phi_{k}^{-}}$be the subset of $S$ where the negative flow of solution $a_{i}$ is less than $a_{k}$.

$$
\begin{aligned}
& S_{\phi_{i}^{+}>\phi_{k}^{+}}=\left\{s \in S \mid \phi_{i s}^{+}>\phi_{k s}^{+}\right\} \\
& S_{\phi_{i}^{-}<\phi_{k}^{-}}=\left\{s \in S \mid \phi_{i s}^{-}<\phi_{k s}^{-}\right\}
\end{aligned}
$$

We estimate the probability that $a_{i}$ has a higher positive flow than $a_{k}$ as in (13).

$$
\hat{p}\left(\phi_{i}^{+}>\phi_{k}^{+}\right)=\frac{\left|S_{\phi_{i}^{+}>\phi_{k}^{+}}\right|}{|S|}
$$

Similarly, the probability that $a_{i}$ has a smaller negative flow than $a_{k}$ is estimated as in (14).

$$
\hat{p}\left(\phi_{i}^{-}<\phi_{k}^{-}\right)=\frac{\left|S_{\phi_{i}^{-}}<\phi_{k}^{-}\right|}{|S|}
$$

In PROMETHEE II, we calculate the sample net flows $\phi_{i s}$ as in (15).

$$
\phi_{i s}=\phi_{i s}^{*}-\phi_{i s}^{-}
$$

Let $r_{i s}$ be the rank of $a_{i}$ in sample $s$, and $S_{r_{i s}}$ be the subset of $S$ where $a_{i}$ has the $t$ th rank as shown in (16).

$$
S_{r_{i t}}=\left\{s \in S \mid r_{i s}=t\right\}
$$

The probability that $a_{i}$ has rank $t$ is estimated from the samples as in (17).

$$
\hat{p}\left(r_{i}=t\right)=\frac{\left|S_{r_{i t}}\right|}{|S|}
$$

An alternative approach to compute PROMETHEE I and II results based on BN solutions would be to extend a BN model with the nodes representing deterministic PROMETHEE operations in (3)-(5), and to compute the posteriors of positive, negative and net flows directly within the BN model by using a hybrid BN algorithm such as dynamic discretization (Neil et al., 2007). The sampling approach, however, is simpler and offers the advantage of keeping the BN and MCDM models separate, thus allowing each model to be modified without affecting the other.

# 3.4 Presenting outranking results under uncertainty 

The results of PROMETHEE I and II under uncertainty can be challenging for the DM to interpret. For example, the probability distributions of ranks can be overwhelming if there is a large number of alternatives. In this section, we propose graphical approaches and summary metrics (Fig. 2d) to present these results.

### 3.4.1 Presenting PROMETHEE I results under uncertainty

PROMETHEE I provides a partial ranking of solutions that is suitable to be presented in a directed graph, where nodes represent solutions and edges represent preferences. If there are multiple directed paths between two nodes $a_{i}$ and $a_{j}$, and if one of those paths is composed of only one edge, i.e. $a_{i} \rightarrow a_{j}$, we remove this edge from the graph as it is redundant in presenting partial ranking. Its removal will present the partial ranking in a more concise way. In addition, the edges can be weighted in terms of the probability of the preference they represent, with their color and width adjusted according to these weights. The algorithm for generating the outranking graph is shown below, and an example is shown in Sect. 3.6.

```
Algorithm 1 Construction of outranking relation graph
    Start with empty graph \(G\) composed of nodes \(a_{1}, \ldots, a_{n}\)
    for each solution pair \(a_{i}\) and \(a_{k}\)
        if \(a_{i}\) is preferred to \(a_{k}\)
            add edge \(a_{i} \rightarrow a_{k}\) to \(G\)
        end if
    end for
    for each edge \(a_{i} \rightarrow a_{k}\)
        if there are multiple directed paths from \(a_{i}\) to \(a_{k}\)
            remove edge \(a_{i} \rightarrow a_{k}\)
        end if
    end for
```


# 3.4.2 Presenting PROMETHEE II results under uncertainty 

Combining PROMETHEE II with BNs provides the probability distributions of net flows and solution rankings, which can be challenging to interpret. We use two graphical approaches to present these results. Firstly, we show the cumulative distribution plots of rankings as this highlights the dominating solutions for different ranks. Secondly, we use violin plots to show the probability distribution of net flows. The solutions are ranked in decreasing order of median net flows in the violin plot to highlight the ranking of solutions, and the net flow distributions shown in the plot highlight the uncertainty regarding this ranking. Examples of both plots are shown in Sect. 3.6.

### 3.4.3 Summary scores for PROMETHEE II results under uncertainty

Since PROMETHEE II under uncertainty provides a probability distribution of ranks rather than a definite ranking, multiple solutions will be ranked the highest with different probabilities in most circumstances. DMs may have different preferences; they may focus on a specific range of ranks, or consider some rank positions similar. To account for these cases, a weighted approach can be used to summarize the probability distribution of rankings into a single score, $\theta_{i}$, for each solution $a_{i}$. The score $\theta_{i}$ is calculated as in (18) where $c_{t}$ is the weight of the $t$ th rank. Note that these weights are not about the importance of criteria; they are about assigning coefficients to the probabilities for different ranks so that we can obtain an aggregated measure.

$$
\theta_{i}=\sum_{t=1}^{n} c_{t} p_{i t}
$$

### 3.5 Data-driven PROMETHEE

The proposed approach for computing PROMETHEE I and II from BN posteriors could be naturally expanded to apply PROMETHEE on a dataset. In this approach, we assume that a historical dataset of solutions is available, but the data-generating process of these solutions is not modeled or available. In this case, we can use statistical tests for the hypothesis $\phi_{i}^{+}>\phi_{k}^{+}$. However, conducting multiple pairwise tests between the positive and negative flows of solutions is prone to false discoveries due to family-wise error rate. Tukey's test corrects for

these errors when making pairwise comparison of the means. Dunn's test is a non-parametric alternative for this purpose. These tests only show statistical significance of the difference, but they do not provide information about the amount of difference between flows. Therefore, rather than a fully automated analysis based on statistical significance, we recommend the DMs to evaluate the confidence intervals of flow differences and assess the magnitude of the difference alongside the statistical tests.

# 3.6 Simple example 

This section demonstrates the proposed approach by applying it to a simple example that has 3 criteria and 4 solutions based on the BN shown in Fig. 1. In the BN, nodes C1, C2 and C3 represent decision criteria, F1 and F2 represent the features that will be instantiated for different solutions, B represents a latent variable that will remain unobserved for all solutions. The feature values are instantiated for each solution and the posterior probabilities of criteria are computed using the junction tree algorithm. Table 1 shows the instantiated feature values and posterior criteria distributions of each solution; all criteria have 3 possible states. Our aim is to maximize all criteria and we use Type I preference function. The criteria weights are $0.5,0.3$ and 0.2 for $\mathrm{C} 1, \mathrm{C} 2$ and C 3 , respectively. The posterior distributions of positive, negative and net flows are computed by generating 10,000 samples from the posterior criteria distributions as described in Sect. 3.3.

The partial ranking of solutions is obtained by using a threshold value of $\beta=0.5$ on the posterior distributions of positive and negative flows as described in Sect. 3.3. Figure 3 shows the partial ranking graph prepared by the algorithm shown in Sect. 3.4.1. Solution $a_{2}$ is preferred to $a_{4}$, and there is no preference relation between the other solutions.

The probability distributions of rankings were computed based on the net flow distributions as described in Sect. 3.3. Figure 4a shows the cumulative distribution of rankings of each alternative. In this example, solution $a_{1}$ has the first, second, third and fourth rank with

Table 1 Posterior criteria distributions of solutions


Fig. 3 Partial ranking of solutions
![img-2.jpeg](img-2.jpeg)

![img-3.jpeg](img-3.jpeg)

Fig. 4 a Cumulative distributions of solution rankings, b Probability distributions of net flows
$0.36,0.24,0.22$ and 0.18 probability. Solution $a_{4}$ has the first, second, third and fourth rank with $0.09,0.17,0.32$ and 0.42 probability. Figure 4 b shows the net flow distributions of the solutions. Solution $a_{2}$ has the highest mean net flow.

Figure 4a shows that $a_{1}$ and $a_{4}$ have the highest and lowest probability of having the highest rank, respectively. However, this probability alone is not sufficient to rank the solutions. For instance, even though $a_{2}$ has a lower probability of being the first than $a_{1}$, the probability of it being in top two or three ranks is higher than $a_{1}$. Therefore, $a_{2}$ can be considered as a better alternative for DMs who wish to consider multiple possibilities, whereas $a_{1}$ can be better for DMs who focus on the top rank and assign a relatively higher weight to the best possible outcome. The weighted score $\theta_{i}$ described in Sect. 3.4.3 summarizes the performance of solution $a_{i}$ in a single measure. Table 2 shows the weight $c_{t}$ of each rank $t$, the score $\theta_{i}$ of each solution $a_{i}$, and its rank in parentheses, for different rank weighting methods. If the DM assigns rank weights with RS, which assumes equal distance between the weights of different ranks, $a_{2}$ will have the highest rank, followed by $a_{1}$. However, suppose the DM considers that the first rank is considerably more important than others, and uses RR or ROC, which assigns about twice as much as weight to the first rank than the second one. In these cases,

Table $2 \theta_{i}$ scores and rank weights with RS, ROC and RR methods


$a_{1}$ will have the highest rank, followed by $a_{2}$. Solutions $a_{3}$ and $a_{4}$ has the third and fourth rank in all weighting methods in this example.

Suppose a DM is only interested in the first $N$ ranks that corresponds to having more tolerance for risk than the case of considering all ranks. In this case, this DM can apply the rank-based weighting methods for only the first $N$ ranks and use 0 weights for the others. This would require changing $n$ with $N$ in (7)-(9), and assigning 0 weights to $c_{N+1}, \ldots, c_{n}$. For example, the last column of Table 2 shows the weights and scores for the ROC approach when the DM considers only the two highest ranks.

# 4 Case study and results 

This section applies the proposed approach to a case study of supplier selection, which is an MCDM problem that has been widely studied in the literature (see Govindan et al., 2015; Zimmer et al., 2016; Chai \& Ngai, 2020; Rashidi et al., 2020; Saputro et al., 2022; Cui et al., 2023). We use a BN model for multicriteria supplier evaluation that was previously developed with domain experts by Kaya and Yet (2019). The BN model used here aims to evaluate suppliers based on seven criteria: product quality, cost, delivery performance, quality system certifications, flexibility, cooperation, and reputation. Among these criteria, cost and quality system certifications can be directly observed, so alternatives' performances are deterministic on these criteria. The other criteria are latent variables that are estimated by indirect measurements. The cost criterion is minimized whereas all other criteria are maximized. All criteria variables have five ordinal states; VL—very low, L—low, M—medium, H—high and VH—very high. The BN model was instantiated with the data of 10 different suppliers, and the posterior probability distributions of criteria were computed (see Table 3). The preference functions of the criteria and the corresponding threshold values were determined with a domain expert who was also involved in development of the BN. For product quality, cost and reputation, Type I function was selected. For quality system certifications, Type II function was selected with an indifference threshold of 1 . So, for this criterion, only differences of 2 levels or higher are accounted for. For delivery performance, flexibility and cooperation, Type III function was used with preference thresholds of 3, 2 and 2 levels, respectively.

The weights of the criteria were obtained by asking the domain expert to rank the criteria based on their importance and applying the ROC formula. As a result, the weights of product quality, delivery performance, cost, quality system certifications, flexibility, cooperation, and reputation were realized as $0.370,0.228,0.156,0.109,0.073,0.044$ and 0.020 , respectively. We also employed RS and RR in conducting sensitivity analysis of the weights.

We generated 1000 samples from the posteriors of the BN model, and computed the probability distribution of positive, negative and net flows based on these samples as described in Sect. 3.3. The partial ranking of solutions was obtained by using a threshold value of $\beta$ $=0.5$ on the posterior distributions of positive and negative flows as described in Sect. 3.3. Figure 5 shows the partial ranking graph. A directed arc from a supplier to another means that the former one outranks the latter.

Product quality, delivery performance and cost are the most important criteria for the DM, and the best suppliers S2 and S6 have good performances in those criteria. S3 is also a good alternative as it has acceptable performance in all criteria. S4 and S8 cannot be differentiated since they have advantages in different criteria. S4 is better at product quality and delivery performance, and S8 is better at cost and delivery performance. S10 is the worst alternative because it offers a medium-quality product (with 0.999 probability) with a very high cost.


![img-4.jpeg](img-4.jpeg)

Fig. 5 Partial ranking of suppliers
![img-5.jpeg](img-5.jpeg)

Fig. 6 Cumulative probability distribution of supplier ranking

The probability distributions of complete supplier rankings were computed based on the net flow distributions as described in Sect. 3.3. Figure 6 shows the cumulative distribution of rankings of each alternative, and Fig. 7 shows the net flow distributions of the solutions. In Fig. 6, we see that S2 and S6 both have the highest probability for the first rank, but their plots intersect at several points in Fig. 6, showing that the best between these two alternatives changes for different ranks. We can also see that the plot of S3, which has a lower probability for the first rank than S2 and S6, manages to lie above the plots of these alternatives starting from the fourth rank. Figure 7 is also helpful in comparing suppliers since it illustrates the full distributions of net flows including density and range.

In general, we observe that suppliers have varying levels of performance throughout their plots and it is not straightforward to achieve a final ranking of them. We compute the summary score $\left(\theta_{i}\right)$ of the suppliers as described in Sect. 3.6 by using RS, ROC or RR weights for ranks. Table 4 shows these weight vector alternatives; the last three columns also show the weights when just the first three ranks are considered by the DM. The weights for the top three ranks are provided as an example, the DM of the problem can select a different cut-off point as well. Table 5a, b show $\theta_{i}$ scores and rankings of the suppliers based on these rank weights.

![img-6.jpeg](img-6.jpeg)

Fig. 7 Probability distribution of net flows

Table 4 Rank weights for RS, ROC and RR approaches for supplier selection


When we examine the ranking of the suppliers with ROC-weighted $\theta_{i}$ scores in Table 5a as an example, we observe that S2 is the best supplier followed by S6; these are the suppliers with the highest probabilities for the first rank. They are followed by S3 and S4 since they have high probabilities for the first two ranks. The rest of the rank list is not straightforward though. S8, for example, has 0 probability for occupying the first or the second rank, whereas S1 and S5 both have positive probabilities there. However, S8 is positioned higher than S1 and S5 since it improves its performance noticeably in the lower ranks. When we compare S5 and S7, we see that S5 has higher probabilities for the first three ranks, but S7 performs better for the remaining four ranks and it outranks S5. Such patterns can be observed from

Table $5 \theta_{i}$ scores and supplier rankings based on $\theta_{i}$ scores


Fig. 6. In Table 5a, we can see that the best two suppliers are S2 and S6 with ROC and RR rank weighting methods, but S6 and S3 with RS. This is due to the fact that RS puts less importance on the first rank than ROC and RR, and assumes equal distance between consecutive ranks. The performance of S2 is higher than S3 at the first rank, but lower at the second, third and fourth ranks. A conservative DM in the face of uncertainty can prefer the RS ranking since it treats the possible outcomes more evenly. On the other hand, a DM who is more interested in the probabilities for the first rank can choose the ranking of ROC or RR.

# 4.1 Data-driven outranking 

The proposed approach can be used for data-driven outranking when data about previous solutions are available as described in Sect. 3.5. We generated a dataset of 100 samples from the BN to simulate a case of learning preferences from limited data, and analysed this dataset assuming that the data-generating process was not known. We conducted Tukey's Test with $95 \%$ confidence level for this purpose and tested the following hypotheses for all $a_{i}-a_{k}$ pairs.

$$
H_{0}^{\mathrm{T} 1}: \varphi_{i}^{*}=\varphi_{k}^{*}
$$

$$
H_{0}^{\mathrm{T} 2}: \varphi_{i}^{-}=\varphi_{k}^{-}
$$

Table 6 shows the mean difference between the pairs and the corresponding confidence intervals. The differences are calculated with the supplier in the row minus the supplier in the column, and the asterisk symbols show the statistically significant differences corresponding to a $p$ value of less than 0.05 . For example, the S2-S1 cell for positive flows shows that the mean positive flow of S 2 is significantly higher than that of S 1 . The same cell for negative flows shows that the mean negative flow of S 2 is significantly lower than that of S 1 this time, so we conclude that S2 outranks S1. Figure 8 shows the results of this approach. In this example, the only difference between the data-driven and model-driven outranking approach was in the preference between S1 and S4. While S4 is preferred over S1 in partial ranking of the suppliers obtained from the BN model, the data-driven approach was not able to identify a statistically significant difference between the positive and negative flows of those alternatives in the given sample as the differences were small.

# 4.2 Sensitivity analysis on criteria weights 

Since the results of our approach, as in many MCDM methods, depend on the weights of criteria, we make sensitivity analysis to see if our results are robust to small changes in criteria weights. Rather than changing the ROC weights randomly, we apply RS and RR methods to the criteria ranking of our supplier selection expert. With RS, the weights of product quality, delivery performance, cost, quality system certificates, flexibility, cooperation and reputation are realized as $0.250,0.214,0.179,0.143,0.107,0.071$ and 0.036 , respectively. With RR, these weights are $0.386,0.193,0.129,0.096,0.077,0.064$ and 0.055 . When we switch from ROC to RS, the most evident difference is in the weight of product quality, which becomes quite lower. On the other hand, when we use RR, this weight increases, and the weights of delivery performance and cost decreases. There are some other differences as well.

Figure 9a illustrates the outranking relations of PROMETHEE I calculated with RS criteria weights. With ROC weights, S2 and S6 were the best alternatives, and S8 was outranked by S6. With RS weights, S3, S6 and S8 have a tie. There are also other differences such as some strict preference relations turning into indifference or incomparability, or vice versa. However, the general picture is not substantially different from Fig. 5, and there are no reversals in outranking relations. In Fig. 9b, we see the outranking relations of the suppliers when RR method is performed for criteria weights. This time, the best suppliers are S2, S3 and S6 together. S4 and S8 cannot outrank each other, similar to the ROC results. Different from the ranking with ROC criteria weights, S9 outranks S1, and S7 outranks S5 in Fig. 9b. Again, we observe that there are no substantial differences.

Since PROMETHEE II provides complete rankings rather than partial, we can compare the similarity of its rankings with ROC and RS/RR weights for criteria using Kendall rank correlation coefficient (Kendall's Tau). Kendall's Tau measures the similarity between two rankings of the same elements. It can take values between -1 and 1 ; with values $-1,1$ and 0 corresponding to perfectly opposite rankings, exactly the same rankings and no relationship between the rankings, respectively. Kendall's Tau between the rankings of ROC criteria weights and RS criteria weights when we use RS, ROC and RR rank weights are 0.644 , 0.777 and 0.777 , respectively. On the other hand, when we compare the rankings of ROC and RR criteria weights, Kendall's Tau coefficients are $0.822,0.777$ and 0.733 , respectively. We can conclude that there is an acceptable level of similarity between the rankings with different weighting methods, especially ROC and RR. This is expected since they both put greater emphasis on the top ranks compared to RS.

Table 6 Tukey's test results for data-driven positive and negative flows of supplier pairs


![img-7.jpeg](img-7.jpeg)

Fig. 8 Partial ranking of suppliers with data-driven outranking approach
![img-8.jpeg](img-8.jpeg)

Fig. 9 Outranking relation of suppliers with a RS-weights, b RR-weights

For the complete rankings provided by PROMETHEE II, we conduct further sensitivity analysis to determine allowable ranges for criteria weights for the results to remain stable. We use the weight stability intervals procedure by Mareschal (1988) for this task by modifying it to be applicable with uncertain criteria evaluations. This procedure is developed to find intervals for criteria weights so that the given ranks of solutions according to additive utility functions do not change, and it can be applied with PROMETHEE II scores. It uses the differences in criteria values between successive solutions in the rank list to find these intervals. The details of the procedure can be seen in Mareschal (1988).

The weight stability intervals procedure can only work with a single sample, so we need to enhance it to work for PROMETHEE II under uncertainty. Firstly, using the basic procedure, we construct the interval of each criterion weight in each sample. Each sample produces its separate ranking of solutions, so we arrive at 1000 intervals for each criterion weight. Next, these intervals need to be aggregated into an overall interval for each criterion. We form these intervals with the values that appear in at least a given percentage of all samples. Since all the intervals in the samples are formed around the original weights, these original weights appear in $100 \%$ of the intervals. As we move away from the original weights, the percentage of samples that contain the value in consideration gets smaller. In line with the logic of confidence intervals, we use $95 \%$ as the cut-off value. Taking ROC weights as the original criteria weights, Table 7 reports the resulting aggregated intervals we obtain. These results suggest that the weights of product quality, delivery performance, and cost should be

Table 7 Weight stability intervals for ROC weights


set carefully since they have relatively narrow ranges. On the other hand, the ranking list is not so sensitive to changes in the weights of other criteria, so uncertainties in those areas can be tolerated better.

# 5 Conclusions 

This paper proposes a systematic approach to combine BNs and outranking approaches to support multicriteria decision problems under uncertainty. The proposed approach is applied to a BN model that has been developed for supporting supplier selection decisions in an automobile manufacturer. Our approach enhances PROMETHEE I and II to provide partial and complete ranking with the probability distributions of decision criteria obtained from BNs. The result of partial ranking can be useful for DMs who need to stratify alternative solutions according to their performance without forcing a strict ranking. On the other hand, the result of complete ranking gives the DMs the chance to observe the overall performance of the solutions, as well as the performance in the best-case and worst-case scenarios. The results of partial and complete rankings are shown in graphs, cumulative distribution figures, and violin plots to demonstrate the preferences regarding solutions and the associated uncertainty in a concise way. We also present a summary score to summarize the performance of solutions based on their ranking distributions.

Our approaches provide a systematic and flexible way to combine a widely used MCDM method with probabilistic generative models such as BNs. They can work with different types of criteria like continuous, nominal and ordinal. In addition, the results of the sensitivity analysis on the weights of criteria can be used to determine which criteria need the most careful evaluation. The proposed approaches also extend to applying data-driven PROMETHEE when only samples from solutions are available, but the data generating process is not modeled.

Combining PROMETHEE and BNs overcomes major limitations of outranking-type MCDM approaches and BNs in modeling decisions under uncertainty. Traditional outranking approaches such as PROMETHEE provide limited or no support when criteria values involve uncertainty. BNs can model complex probability distributions in a concise way, but are not designed for decision making problems. Extensions of BNs for decision making, such as IDs, require elicitation of complex utility tables in decision problems with multiple criteria. The proposed approach overcomes these limitations by having the ability to model

complex criteria distributions in a BN model, and computing outranking relations from these distributions based on DM preferences using PROMETHEE.

Limitations of our approach include dependence on the criteria weights obtained from the DMs. We use sensitivity analysis to assess the robustness of the results to changes in the weights. As future work, indirect and interactive elicitation approaches can be implemented to provide more robust weight elicitation. Implementation of the proposed approach to BN software and packages can enable a wider use of BNs for MCDM problems.

Funding Open access funding provided by the Scientific and Technological Research Council of Türkiye (TÜBİTAK). This study was supported by an Institutional Links Grant (ID 352394702) under the Turkey-Newton-Katip Çelebi Fund partnership. The Grant is funded by the UK Department of Business, Energy and Industrial Strategy (BEIS) and The Scientific and Technological Research Council of Turkey (TUBITAK, ID 217M518) and delivered by the British Council.

# Declarations 

Conflict of interest The authors declare that they have no conflict of interest.
Ethical approval This article does not contain any studies with human participants or animals performed by any of the authors.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/.
