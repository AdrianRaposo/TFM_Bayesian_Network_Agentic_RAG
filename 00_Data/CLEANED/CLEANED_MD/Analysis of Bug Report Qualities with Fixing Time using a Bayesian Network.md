# Analysis of Bug Report Qualities with Fixing Time using a Bayesian Network 

Sien Reeve O. Peralta*<br>sienreeve46@gmail.com<br>Waseda University<br>Tokyo, Japan<br>Yuki Noyori<br>yuki.noyori.wx@hitachi.com<br>Hitachi, Ltd., Tokyo, Japan

Hironori Washizaki<br>washizaki@waseda.jp<br>Waseda University<br>Tokyo, Japan<br>Shuhei Nojiri<br>shuhei.nojiri.dd@hitachi.com<br>Hitachi, Ltd., Tokyo, Japan

Yoshiaki Fukawaza<br>fukazawa@waseda.jp<br>Waseda University<br>Tokyo, Japan<br>Hideyuki Kanuka<br>hideyuki.kanuka.dv@hitachi.com<br>Hitachi, Ltd.,<br>Tokyo, Japan

## ABSTRACT

Most client software employs a bug-tracking system, which utilizes user-submitted reports (bug reports) that contain information necessary for software developers to fix bugs. The quality of bug reports drastically differs. Bug reports can include severity, priority, and associated issues determined by researching the addressed bug. Herein we investigate the influence of bug report qualities on successfully fixing a bug and estimating the fixing time. We also examine the claim in previous studies that bias and differences in the treatment of bug reports exist due to broad expertness among the reporters. Our approach examines the relationship between the qualities within the bug-fixing cycle and modeling graphical causal dependencies through a Bayesian Network. Bug reports with attachments, dependencies on another bug, and frequent discussions are more likely to be fixed. In addition, bug reports with a high severity tend to be fixed faster. Moreover, the difficulty of the bug itself may influence the fixing rate such that a straightforward bug will be fixed easier and faster regardless of the bug report quality.

## KEYWORDS

Bug Reports, Bayesian Network, Causal and Inference Model

## ACM Reference Format:

Sien Reeve O. Peralta, Hironori Washizaki, Yoshiaki Fukawaza, Yuki Noyori, Shuhei Nojiri, and Hideyuki Kanuka. 2023. Analysis of Bug Report Qualities with Fixing Time using a Bayesian Network. In Proceedings of the International Conference on Evaluation and Assessment in Software Engineering (EASE '23), June 14-16, 2023, Oulu, Finland. ACM, New York, NY, USA, 6 pages. https://doi.org/10.1145/3593434.3593484

## 1 INTRODUCTION

Software may cause unforeseen errors, which are referred to as bugs. Software often employs a bug-tracking system, which allows users (hereafter, reporters) to describe defects as bug reports. Then

## 0

This work is licensed under a Creative Commons Attribution International 4.0 License.

EASE '23, June 14-16, 2023, Oulu, Finland
(c) 2023 Copyright held by the owner/author(s).

ACM ISBN 979-8-4007-0044-6/23/06.
https://doi.org/10.1145/3593434.3593484
the bug reports are shared with the development team, who identify and fix the issue.

Bug reports should contain a clear and concise description of the problem and relevant information to help the development team understand and reproduce the issue. However, a general analysis by Betternburg [3] mentions that the bug report context may vary based on the reporter's knowledge, whether expert or novice. Consequently, not every report meets the developers' expectations at submission time, and developers often must seek more information before fixing it. Other factors and properties of bug reports, namely severity, developer's workload, and reporter's reputation, also affect developers' attention on a bug report [10]. These factors produce biases and may cause differences in bug-fixing time. Hence, the quality of the bug report may depend on various factors and properties found in the bug fixing process. Our research aims to assess the significance of these qualities in efficiently fixing a bug.

Many approaches treat each quality and property of a bug report as a separate and distinct factor since analyzing complexly structured data is difficult [16] [1]. Complex systems generally result in difficult processes and unclear results. Our approach employs a Bayesian Network (BN) to understand complex systems. BN considers relationships among the investigated qualities throughout the bug fixing process. It can represent complex relationships between variables clearly and intuitively using a graphical structure, effectively handle uncertainty by using probability distributions and make inferences based on the available data.

The primary focus of this work is to address the following three research questions (RQs).

RQ1 Which qualities of bug reports significantly contribute to fixing a bug?
RQ2 Which qualities indicate a bug to fix quickly?
RQ3 Can BN provide clear explanations and reliable results?

This study employs bug reports obtained from Bugzilla. Subsequently, conditional probability distributions (CPDs) are obtained from BN to assess the significance of each quality in fixing and the bug fixing time. Finally, BN model performance is measured to determine the ability to classify whether the bug addressed in the bug report will be fixed and if it can be fixed within a short span.

## 2 BACKGROUND

### 2.1 Bugzilla

Bugzilla is a web-based bug-tracking system many software organizations use to track and manage software defects. Here, we extract bug reports from Bugzilla@Mozilla [8] (i.e., Mozilla Firefox, Thunderbird, Calendar, and Sea Monkey) because the target client software bug reports are from the Mozilla Project.

### 2.2 Bug Fixing Cycle

Figure 1 depicts the steps involved in the bug-fixing cycle. First, the reporter submits an accurate and precise report (Step 1). This is crucial to ensure that the issue can be effectively resolved. Second, developers review and address reported bugs (Step 2). During this step, the reporters must wait for this process to be completed. Third, the developers rely on the information provided by these reports and communicate with the reporter to gather additional details or clarify information (Step 3) [19] [5]. However, research has shown that developers may prioritize reported bugs based on their workload and the reputation of the person submitting the report [10]. Fourth, developers must be able to replicate the bug in order to fix it (Step 4). Then they assess the severity, the complexity of the fix, the cost of resolving the bug, and its related bugs. Then finally, make a priority among bugs (Step 5) [17] [12]. Then developers work on a resolution (Step 6), which may ultimately result in the issue being fixed. At any time, the status of a bug report may be updated to reflect the current state of the issue.

In this study, we selected important features from the described bug-fixing cycle and analyzed their relationships.

### 2.3 Bayesian Network

A Bayesian Network (BN) is a graphical model representing probabilistic relationships between variables or events. It is based on a Bayesian probability which involves expressing degrees of belief as a probability statement [9]. In our approach, we employ BN to model the relationships among the main qualities of bug reports.

BN represents variables as nodes in a graph and edges between the nodes as the probabilistic dependencies between the variables. Each node in the network is associated with a probability distribution to quantify the probability of different states or outcomes for that variable. The network can make probabilistic inferences about the variables by considering their dependencies. The probability of a variable is calculated by considering the relationships between the variable and its parents in the network. The idea is to use the conditional probability of the variable given its parents, which is represented by the conditional probability distribution (CPD) associated with that variable as

$$
\begin{gathered}
P\left[x_{1}, x_{2}, \ldots, x_{n}\right]=P\left[x_{1} \mid x_{2}, \ldots, x_{n}\right] \cdot P\left[x_{2}, \ldots, x_{n}\right] \\
=P\left[x_{1} \mid x_{2}, \ldots, x_{n}\right] \cdot P\left[x_{2} \mid x_{3}, \ldots, x_{n}\right] \ldots \cdot P\left[x_{n-1} \mid x_{n}\right] P\left[x_{n}\right] \\
=P\left(x_{i} \mid x_{i-1}, \ldots, x_{1}\right) \\
=P\left(X_{i} \mid \operatorname{Parent}\left(X_{i}\right)\right)
\end{gathered}
$$

## 3 RELATED WORKS

### 3.1 Bug Report Analysis

Previous studies have examined the attributes of bug reports through literature reviews. Most evaluations utilized questionnaires distributed to developers and reporters. One study identified key factors and crucial information for developers to effectively address bug reports. They created a tool named CUEZILLA to assist reporters with providing important information before submitting their reports [3]. Their analysis not only examined why certain information is not prepared due to variations in expertise and proficiency of the bug reporter, but it also delved into factors that may not significantly influence the time required for resolution. Additionally, another study identified key qualities that significantly impact bug reports' effectiveness [13].

### 3.2 Causality on Software Metrics

Previous research in software engineering has focused on identifying and establishing causal relationships among various quantities [18]. This is typically accomplished using statistical tests and examining observational studies in the domain [7] [2]. Various causal inference techniques have been employed to assess the importance of different factors, determine the strength of causal relationships, replicate findings with other datasets, and develop guidelines for decision-making.

## 4 METHODOLOGY

### 4.1 Objects

Important properties and qualities of bug reports are extracted and measured from Bugzila@Mozilla and evaluated as a binary ( 0 or 1 ) state. The classification details for each item are listed in Table 1.

Table 1: Bug Reports Qualities from Bugzilla@Mozilla


![img-0.jpeg](img-0.jpeg)

Figure 1: Bug Fixing Cycle

Developers Workload, Reporters Reputation, Severity, and Priority are labeled 0 (low) and 1 (high). Description, Attachments, Related Works, and Comments are labeled as 0 (absent) and 1 (present). Resolution is labeled 0 (Not fixed) and 1(Fixed), and Fixing Time is 0 (slow) and 1 (fast). The classifications are based on our background knowledge of bug-fixing cycles. The 10 days threshold for FixingTime is based on the analysis that bugs left for more than 10 days make the software vulnerable. Table 2 shows the results of the statistical analysis.

Table 2: Bug Reports from Bugzilla@Mozilla


We also targeted specific bug reports that met the following criteria:
(1) The reporter is not a software developer since developers may submit for the sake of logging;
(2) The bug report is not a duplicate [4], as it is difficult to evaluate the influence of multiple bug reports with different contexts.
We have collected 87,948 bug reports from criteria (1) by removing bug reports with an empty description and filtering the duplicates for criteria (2) referring to the resolution status of each bug report marked DUPLICATE, resulting in 58,800 bug reports.

### 4.2 Inference

We used Variable Elimination (VE) to perform inference in BN. VE is a technique to calculate the probability of a target variable $(Y)$ given some evidence (e) by eliminating variables not directly related to the query variable. The idea behind variable elimination is to use the factorization property of the joint probability distribution represented by BN. The joint probability distribution can be factorized into a product of CPDs, allowing variables that are not directly related to the query variable to be eliminated by summing or integrating. We assessed the likelihood of qualities concerning Resolution and Fixing Time to examine the impact of these attributes on the resolution and speed of bug fixing.

We measured the probability (Eq. 1) of the conditional variables $(X)$ at each state $(0,1)$ on the target variables $(Y)$ from given condition (e) which is expressed as

$$
\operatorname{Pr}(Y \mid e) ;\left\{e \subset X, X=\left\{x, \ldots, x_{n}\right\}, x=\{0,1\}\right\}
$$

## 5 EVALUATION

Figure 2 shows the constructed network used to measure the probability of each quality obtained from the CPDs in table 3. The edges weight shows the probability of the parent node $(X)$ leading the child node $(Y)$ to state $Y=1$. The weight becomes a positive value when state $X=1$ has a higher probability leading to $Y=1$, while a negative value when $X=0$ is higher. Probability with over $50 \%$ is highlighted with positive value as blue and negative value as red. For example, the arc from $\mathbf{R W}$ on $\mathbf{R}$ has 0.52 weight which states that when Related Works are present $(X=1)$, it would lead to FIX $(Y=1)$ in Resolution. As for arc from $\mathbf{C}$ on $\mathbf{F T}$ have a negative value of -0.565 , which shows that when $\mathbf{C}$ is absent $(X=0)$, have a higher probability that the bug is fixed faster $(Y=1)$. Chi-square test determines the dependency level and correlation between factors. Although no individual factors showed significant relationships, all factors have a significant causal relationship with the target variable.

![img-1.jpeg](img-1.jpeg)

Figure 2: BN Graph

The probability formula from the network and the total number of patterns possible for each quality were estimated. Additionally, the highest probability for all qualities was determined.

Table 3: Formula and Highest CPDs of the Bug Report Qualities


We evaluated the importance of each quality to resolve bugs and shorten the fixing time. VE was applied to remove the impact of other factors on the target variable $(Y)$ and to accurately estimate the effect on Resolution Time. Using equation 2, we formulated the influence of each state on the resolution and fixing time with equation 3 and 4, respectively. For example, in case of $\mathbf{D}$ on Resolution, the formula in table 3 for $\mathbf{D}$ are referenced and thus result in equation 5 .

$$
\operatorname{Pr}(Y \mid R=r, e) ; r=\{1: \text { Fixed, } 0: \text { NotFixed }\}
$$

$$
\operatorname{Pr}(Y \mid F T=f, R=1, e) ; f=\{1: \leq 10 \text { days, } 0:>10 \text { days }\}
$$

$$
\operatorname{Pr}(D \mid D, W, R R, R=r, e)
$$

Then statistical analysis determined which characteristics were more prevalent when bugs were fixed compared to when they were not fixed in the case of Resolution and when bug reports were fixed within 10 days compared to when they had taken more time to fix. We compared each state $Y$ and its probability of being $R=1$ and $F T=1$. Table 4 and 5 for Resolution and Fixing Time, respectively.

The BN model performance was measured with a traditional probabilistic classifier. We selected the Bernoulli Naive Bayes classifier as the optimal model for benchmarking the predicted binary outputs based on probability.

Table 4: Analysis of the Bug Report Qualities state to Resolution


Table 5: Analysis of the Bug Report Qualities state to Fixing Time


Table 6: Performance on Training Samples for Resolution


Table 7: Performance on Testing Samples for Resolution


Table 8: Performance on Training Samples for Fixing Time


Table 9: Performance on Testing Samples for Fixing Time


## 6 DISCUSSION

BN comprises an interconnected system of relationships, where the primary groups are linked to secondary groups and eventually lead to the resultant group of qualities. Through these relationships, the network can identify 512 patterns for Resolution and Fixing Time.

### 6.1 Analysis on Resolution and Fixing Time

BN can determine the states of each quality about resolving bugs and the proportion of these states (Table 4). The inverse proportionality in $\operatorname{Pr}(Y=1)>99 \%$ and $\operatorname{Pr}(Y=1)<1 \%$ serves as an indicator of their reliability and significance in the bug fixing process. For example, $36.6 \%$ of bug reports were observed as having been resolved $(P>99 \%)$, and $40.9 \%$ were not $(P<1 \%$ ) in the state $D W=1$. This result suggests DW may not be a significant factor in resolving bugs. In contrast, state $R R=1$ appeared $78.1 \%$ at bug reports guaranteed to be fixed. In comparison, for bug reports that were unlikely to be resolved, the proportion of state $R R=1$ is only $46.0 \%$. Similarly, a bug report with an attachment $(A=1)$ appeared in $72.3 \%$ of resolved bug reports and was found at $26.9 \%$ of unfixed bug reports. This inverse proportionality demonstrates the likelihood of bug resolution. Therefore, it can be concluded that Reporters' Reputations and Attachments is a reliable indicator of bug resolution. Furthermore, Related Works (RW) and Comments (C) show the same inverse proportionality, suggesting they are reliable indicators. The presence of RW increases the likelihood of resolving a bug in the later steps. Inverse proportionality strongly correlates with the likelihood of a successful bug resolution, indicating that a bug is more likely to be resolved when a state $Y=1$ is present amongst the factors.

Based on the analysis of the BN and the examination of the relationships between various qualities and the likelihood of bug resolution, we can answer RQ1: Which qualities of bug reports significantly contribute to fixing a bug?

Attachments and high RR are essential qualities for resolving bugs in the early steps. RW is another reliable quality during handling the bug. Additionally, a high RR is a reliable indicator of bug resolution and has the highest probability of a successful bug fix.
When the bug report $S$ is high, $C$ shows an inversely proportional characteristic (Table 5). This suggests severity and comments are reliable indicators for fixing a bug faster. Therefore, we can answer RQ2: Which qualities indicate a bug should be fixed quickly?

Severity and Comments is a reliable indicator of a fast fix. Higher severity bugs and those without comments are more likely to be resolved quickly.

### 6.2 Prediction Model Performance

Table 6 - 9 compare the performance of the BN model with that of the traditional probabilistic model on Resolution and Fixing Time for the train mining and testing samples, respectively. The performance includes a confidence level or score in terms of probability $(p)$. When the confidence of our BN model is higher, it outperforms the traditional model. However, the performance of our model is slightly better when classifying Resolution compared to Fixing Time. Specifically, the accuracy and recall decrease when classifying Fixing Time. This suggests our analysis may have excluded other qualities relevant to classifying Fixing Time. Thus, we can answer RQ3: Can BN provide clear explanations and reliable results?

Yes, it can. BN outperforms the traditional probabilistic classifier, indicating that our constructed network is precise, especially in predicting the Resolution of bug reports.

In addition, BN can clarify predictions by identifying the dependable factors the model considers. The probability-based method offers a transparent indication of the confidence level of the projections, enabling an understanding of the reliability of the model's predictions. Acknowledging that the BN necessitates more computational resources than other models to make predictions is important. Hence, for larger networks, it can be time-consuming and expensive in terms of resources.

### 6.3 Usage

Various factors affect the comments. For instance, the bug's severity influences the level of discussion and the number of comments. Bugs with a higher severity tend to require more attention and receive more comments. In contrast, bugs with a lower difficulty may not even require comment, which causes bug reports with no comments to have a higher probability of being fixed promptly. Developers must carefully check each bug regardless of the severity and determine the severity, as overlooking their significance may lead to inadequate attention.

When examining a bug report, it is crucial to understand that related works are generally unrelated factors with minimal influence. However, if the related works are pertinent to the bug report, the likelihood of fixing the bug increases. Developers must address bugs within the related works that have a greater impact on the system. To fix bugs effectively, developers may need to re-prioritize bugs to address the most critical ones.

## 7 THREATS TO VALIDITY

The conclusions drawn in the study depend on the data and variables utilized in BN. The diversity of projects in bug reports or variable classifications may affect the outcome. The interconnections between the qualities modeled in BN are derived from a broad examination of the bug-fixing cycle. Therefore, varying the bug fixing procedures may require a unique construction of BN. Consequently, the outcome of BN may not be directly transferable to other systems.

## 8 CONCLUSION AND FUTURE WORKS

BN can predict the probability of fixing a bug swiftly based on the characteristics of the bug report and the causal relationships between variables. Our analysis, which used CPDs obtained from BN, evaluated the proportionality of factors on Resolution and Fixing Time to yield trustworthy qualities that impact the speed of bug resolution.

Our findings suggest that providing attachments in the bug report is crucial for resolving bugs, while the presence of related works and discussions are better indicators of successful resolution. Furthermore, RR is a significant factor in the quality of their reports. However, RR may be subject to bias because a good reputation is earned through consistently submitting accurate, well-written, and detailed descriptions. In addition, severity is more likely to be associated with Fixing Time. Still, bug complexity also plays a crucial role in fixing the bug, indicating that a detailed report does not necessarily achieve a resolution.

This research demonstrates that the BN model is more effective than traditional methods for predicting Resolution based on the
given qualities of a bug report. Further investigation of reliable qualities during the fixing cycle should enhance predictions of bug-fixing time, making this a valuable topic for future research. Additionally, future studies should explore topic-based estimations to expand this research field.
