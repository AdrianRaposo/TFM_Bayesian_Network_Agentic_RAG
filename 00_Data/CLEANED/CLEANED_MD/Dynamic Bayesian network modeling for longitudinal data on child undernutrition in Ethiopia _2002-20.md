## OPEN ACCESS

EDITED BY
Francois-Pierre Martin, H\&H Group, Switzerland

REVIEWED BY
Carlos D. Maciel,
University of São Paulo, Brazil
Andrei Rodin,
City of Hope National Medical Center, United States

* CORRESPONDENCE

Getnet Bogale Begashaw
(c) Getnetbogale145@gmail.com;
(c) getnetbogale@dbu.edu.et
RECEIVED 11 March 2024
ACCEPTED 27 November 2024
PUBLISHED 12 December 2024

## CITATION

Begashaw GB, Zewotir T and Fenta HM (2024) Dynamic Bayesian network modeling for longitudinal data on child undernutrition in Ethiopia (2002-2016).
Front. Public Health 12:1399094.
doi: 10.3389/fpubh.2024.1399094
COPYRIGHT
(c) 2024 Begashaw, Zewotir and Fenta. This is an open-access article distributed under the terms of the Creative Commons Attribution License (CC BY). The use, distribution or reproduction in other forums is permitted, provided the original author(s) and the copyright owner(s) are credited and that the original publication in this journal is cited, in accordance with accepted academic practice. No use, distribution or reproduction is permitted which does not comply with these terms.

## Dynamic Bayesian network modeling for longitudinal data on child undernutrition in Ethiopia (2002-2016)

Getnet Bogale Begashaw ${ }^{1,2 *}$, Temesgen Zewotir ${ }^{3}$ and Haile Mekonnen Fenta ${ }^{1,4,5}$<br>${ }^{1}$ Department of Statistics, College of Science, Bahir Dar University, Bahir Dar, Ethiopia, ${ }^{2}$ Department of Data Science, College of Natural and Computational Science, Debre Berhan University, Debre Berhan, Ethiopia, ${ }^{3}$ School of Mathematics, Statistics and Computer Science, College of Agriculture, Engineering and Science, University of KwaZulu-Natal, Durban, South Africa, ${ }^{4}$ Center for Environmental and Respiratory Health Research (CERH), Research Unit of Population Health, University of Oulu, Oulu, Finland, ${ }^{5}$ Biocenter Oulu, University of Oulu, Oulu, Finland

Introduction: Dynamic Bayesian networks improve the modeling of complex systems by incorporating continuous probabilistic relationships between covariates that change over time. This study aimed to analyze the complex causal links contributing to child undernutrition using dynamic Bayesian network modeling, examining both the best- and worst-case scenarios. The Young Cohort of the Ethiopian Young Lives dataset from 2002-2016 was used to analyze the complex relationships among various covariates influencing child undernutrition. We used a built-in Bayes server tool to identify potential features, followed by building the structure of the directed acyclic graph using a structural learning algorithm. The maximum posterior is determined using the relevance tree algorithm. The node with the highest values of mutual information and target entropy reduction, along with the lowest value of target entropy, was considered to have the strongest predictive power in the dataset.
Results: This study revealed that long-term participation in programs increased the likelihood of children being in a normal nutritional state. Key factors influencing the nutritional status of children under two years of age include the mother's education level, her subjective well-being, and the household's wealth quintile. Children with educated parents were more likely to have a healthy nutritional status. Additionally, the causal pathway of intervention programs $\rightarrow$ wealth quintile $\rightarrow$ child nutritional status consistently exceeded $90 \%$ in Waves 3, 4, and 5, indicating a strong relationship. Similarly, the relationship between intervention programs $\rightarrow$ food security $\rightarrow$ child nutritional status was nearly perfect at $99.99 \%$ in Waves 4 and 5, indicating a strong association. Finally, the study revealed that household participation in intervention programs significantly reduces undernutrition in best-case scenarios, while the absence of support poses a higher risk in worst-case conditions.
Conclusion: The comprehensive intervention program strongly improved household wealth, food security, and maternal well-being, which in turn affected children's nutritional status.

REYWORDS
Bayes server, counterfactual prediction, conditional probability, maximum posterior, young Lives data

## Introduction

Child undernutrition is a pressing health concern that affects children, necessitating thorough examination and effective interventions (1, 2). In Ethiopia, child undernutrition is one of the countries where it poses a health challenge (3). In addition to Ethiopia, India, Nigeria, Pakistan, Bangladesh, Indonesia and the Democratic Republic of the Congo are among the seven nations with the highest prevalence of child undernutrition (2, 4, 5). These countries face challenges in undernutrition, including access to nourished food and inadequate healthcare services.

Multivariate logistic regression models are commonly used in studies on child undernutrition outcomes and risk factors (6, 7). However, these models have limitations owing to their static nature and inability to capture temporal relationships (8, 9). The studies conducted by Egata et al. (10) and Bahru et al. (11) utilized a longitudinal model because it is preferable to address this gap by considering within-subject correlations and temporal changes (12, 13). Although longitudinal analysis may not explicitly model transitions between states, it can still provide valuable insights into how variables evolve over time and how they are related to each other. Likewise, Jeyaseelan et al. (14), Owoeye et al. (15) and Begashaw et al. (57) used Markov chain models to address this limitation by incorporating state transitions. However, these models also have limitations because of their assumption of memorylessness, which means that the future state depends only on the current state and not on previous states. Moreover, the research conducted by Hoddinott et al. (16) and Pérez Albertos (17) using the difference-in-differences (DiD) model does not consider the long-term impact of the Productive Safety Net Program (PSNP). On the other hand, Bahru's et al. (18) marginal structural model has limitations, such as unmeasured time-varying confounding variables and model specification sensitivity.

To address these methodological gaps, this study employs a dynamic Bayesian network (DBN) model that allows for the consideration of uncertainties in the relationships between interventions, covariates, time slices, and nutritional status. Unlike traditional statistical methodologies, which often assume linear relationships or require strong parametric assumptions, DBNs can capture the nonlinear and dynamic relationships among variables. This makes DBNs well suited for analyzing the complex interactions of covariates influencing child undernutrition in a complex socioeconomic context such as Ethiopia (19, 20).

A DBN is a probabilistic reasoning graphical model that represents temporal dependencies between variables in a system (21, 22). It extends traditional Bayesian networks to capture evolving dynamics and is an integral part of artificial intelligence (AI), with applications in finance, healthcare, and other domains that require modeling and predicting complex systems (23, 24). This study provides valuable insights for policymakers and stakeholders by identifying potential interactions between variables to address the challenges related to system dynamics and decision-making. Additionally, DBNs allow the integration of prior knowledge and expert opinions, thereby enhancing the robustness of the modeling process (25).

Currently, DBNs are the most effective models for encoding causal relationships and reasoning uncertain knowledge (26, 27). However, despite Ethiopia having one of the highest rates of undernourished children, DBN use in this context remains relatively underexplored. Our study aimed to fill this gap by applying DBNs to analyze the factors contributing to undernutrition among children in Ethiopia. Identifying key causal pathways and assessing their interactions to improve targeted interventions and policy responses. We also examined which program combinations yielded the most effective improvements and how these changes aligned with the nutritional status of children within participating households.

Many studies on child undernutrition have used composite indices or classified children into categories, such as normal, underweight, stunted, and wasted, or by severity (mild, moderate, and severe). However, these studies often fail to account for concurrent nutritional outcomes, as children may experience multiple forms of undernutrition simultaneously. To address this limitation, we employed a DBN that captures the probability of children being in multiple states of undernutrition over time. This method allows us to analyze the complex interrelationships among various nutritional outcomes and identify the dynamic factors influencing child nutrition. By doing so, we gained deeper insights into how different risk factors and intervention programs interact, ultimately informing more effective strategies to combat undernutrition.

To the best of our knowledge, there is limited evidence regarding the use of the DBN approach to assess the concurrent nutritional status in Ethiopia. Consequently, this proof-of-concept study seeks to explore the potential of DBNs in predicting causal relationships among various parental, household, and child-level nodes/covariates among Ethiopian children under 15 years of age. Additionally, this study aims to identify the strength of key causal relationships contributing to low levels of undernutrition in the best-case conditions, as well as those leading to high levels of undernutrition in the worst-case conditions, counterfactual scenarios in Ethiopia.

## Methods

### Data source and survey design

This study utilized longitudinal data from Ethiopia's Young Lives of Young cohort (YLCS), an international initiative aimed at addressing childhood poverty and health. The cohort includes approximately 1999 children aged 1--15 (28, 29). The country is highly heterogeneous, with large socioeconomic differences across regional states and between urban and rural areas (30). The surveys were conducted in 20 sentinels across five Ethiopian regions: Amhara, Oromia, Southern Nations, Nationalities, and Peoples (SNNP), Tigray, and Addis Ababa City Administration (CA) from 2002 to 2016 with five waves. Notably, the Productive Safety Net Program (PSNP) operates in 14 sentinels in four regions (excluding Addis Ababa CA), targeting the pro-poor population (31), while the Emergency Aid Programme (EAP) and Health Extension Programme (HEP) operate in all five regions, targeting disadvantaged socioeconomic groups and offering antenatal care, childhood disease management, and

Abbreviations: AI, Artificial Intelligence; BMI, Body Mass Index; DAG, Directed Acyclic Graph; DBN, Dynamic Bayesian Network; DiD, Difference in Differences; EAP, Emergency Aid Programme; HEP, Health Extension Programme; IRB, Institutional Review Board; MAP, Maximum A Posteriori; MLE, Maximum Likelihood Estimation; MPE, Most Probable Explanation; PC, Peter and Clark; PDAG, Partially Directed Acyclic Graph; PSNP, Productive Safety Net Program; SNNP, Southern Nations, Nationalities, and Peoples'; UK, United Kingdom.

micronutrient supplement coverage (32). The study conducted interviews with randomly selected households to determine whether they had participated in the PSNP, EAP, and/or HEP programs within the past 12 months, facilitating the identification of beneficiaries. In the PSNP and EAP, households were categorized as beneficiaries or non-beneficiaries beginning in 2009 (third wave), with the HEP categorization starting in 2013 (fourth wave). These intervention programs were consolidated into a single package using the “program participation status” variable with eight categories (C, P, E, H, PE, PH, EH, and PEH), as detailed in Supplementary Table S1. Similarly, as outlined in Supplementary Table S2, children's anthropometric conditions encompassed eight distinct states: N, U, S, W, US, UW, SW, and USW (57).

This study did not require ethics approval, as it involved a secondary analysis of publicly available anonymized data. There was no direct interaction with human participants; therefore, informed consent and institutional review board (IRB) approval were not required.

### Data preprocessing pipeline: techniques for anomalies, missing values, and quantization

This study utilizes Bayes Server software, which offers built-in tools for handling missing values, anomaly detection, and feature relevance assessments. It estimates missing values using observed data and probabilistic relationships in the network, without imputing them with static values. Bayes Server employs inference algorithms for temporal models, considering data from past and future time slices. It also uses a probabilistic anomaly detection algorithm to identify outliers or unusual data points, ensuring the quality and reliability of the dataset.

Quantization is essential for preparing continuous variables for analysis in DBNs, as it simplifies modeling and improves interpretability. A balance is needed between using a few categories to prevent overfitting and enough detail to capture variability. Furthermore, the study uses a uniform time interval approach, with data collected every 3.5 years (2002, 2006, 2009, 2013, and 2016) (29, 33). A Lag-1 time window assesses past conditions' impact on current outcomes, while a Lag-2 window captures longer-term dependencies, enhancing model accuracy and providing deeper insights. As illustrated in Figure 1, our DBN model follows a step-by-step workflow for analyzing children's nutritional status using YLCS data (see Supplementary material for details).

### Nodes selection in the child nutritional status network

Feature selection is a crucial step in the construction of a DBN. Including all variables in a temporal node can increase the complexity of the network, resulting in higher computational costs and potential convergence issues. Therefore, dedicating extra effort to feature selection is considered to be the best practice. The Bayes Server also offers a built-in feature selection tool that can automatically determine relevant features through the “Add nodes from the data” functionality. Additionally, it uses mutual information and target entropy reduction to assess the conditional dependencies between the features and target variable. The features with the highest mutual information values and target entropy reduction were the most important factors for the predictive performance of the model. As a result, out of the 39 covariates considered, 13 variables were selected as important, reducing model complexity and improving computational efficiency without compromising predictive accuracy (see Supplementary Table S3). The final 13 covariates were treated as nodes in the DBN analysis, allowing for the modeling of temporal dependencies and causal relationships among influential variables (Table 1).

### Structure learning

This study created a directed acyclic graph (DAG) structure to analyze child undernutrition data. The process involved consulting experts, reviewing the literature, and identifying key nodes. An initial DAG structure was constructed, defining nodes representing factors related to child undernutrition and hypothesizing directional relationships. The DAG structure was then refined using

![img-0.jpeg](img-0.jpeg)

FIGURE 1 Technical workflow of DBN in application with children nutritional status in YLCS data.

TABLE 1 Description and abbreviations of nodes in the child nutritional status network.

dependent |

$t$ (recommended approach in Bayes server as shorthand for time) represents time, where $t=4$ indicates time step 4 . All time steps are zero-based, meaning $t=0$ is the initial time step.
structure-learning algorithms in Bayes Server Desktop version 10.9. However, several erroneous links were produced, requiring validation and correction, with certain causal relationships, such as those from $\mathrm{DA} \rightarrow \mathrm{HHS}, \mathrm{MSW}$ and $\mathrm{ME} \rightarrow \mathrm{CS}, \mathrm{CS} \rightarrow \mathrm{WQ}$, and $\mathrm{CA} \rightarrow \mathrm{MA}$, identified as implausible. These causal links are static and cannot be influenced by other variables, and were confirmed during the structural learning process.

The final DAG structure was validated and refined to ensure consistency with the domain knowledge and plausibility of the generated links, accurately representing child undernutrition dynamics while considering system complexity (Figure 2). In the DAG, the child's sex is the only node that does not have a curved arrow pointing back. This means that all other nodes, excluding the child's sex, have a temporal dependency on their responses (Supplementary Table S5). In addition, all temporal nodes except the PS and FS nodes had five time slices. The PS and FS nodes had only three time slices, with zero placeholder values used for the first and second visits to account for the missing data (Supplementary Table S4). The fundamental concepts of temporal relationships and causal dependencies in DBNs are briefly discussed in the Supplementary material.

## Statistical analysis

DBNs have expanded the scope of traditional BNs to include temporal features such as changes in child undernutrition data
over discrete time intervals $(\mathrm{t}=1,2,3, \ldots, \mathrm{~T})$. The set of variables in a DBN is represented by $X=\left\{X_{1}, X_{2}, \ldots, X_{N}\right\}$, with conditional dependencies represented by directed edges. The transition model in a DBN is defined by the joint probability distribution over time $(34,35)$.

$$
P\left(X_{t} \mid X_{t-1}, \ldots, X_{t-T}\right)=\prod_{i=1}^{N} P\left(X_{t, i} \mid \operatorname{Pa}\left(X_{t, i}\right)\right)
$$

where, $P\left(X_{t} \mid X_{t-1}, \ldots, X_{t-T}\right)$ is the joint probability distribution of the state variables at time $t$ given the past observations, $X_{t}$ represents the state of variables at time $t$, and the conditional dependencies capture how the state at the current time depends on the previous states, $X_{t, i}$ is the state of node i at time t , and $\operatorname{Pa}\left(X_{t, i}\right)$ represents the parents of node i at time t in the graph (Figure 2).

The model incorporates the transition probabilities between time steps $t-1$ and $t$. For example, the probability of transitioning from state $X_{(t-1, i)}$ to $X_{t, i}$ can be represented as:

$$
P\left(X_{(t, i)} \mid X_{(t-1, i)}\right)
$$

The model parameters were calibrated against available data using maximum likelihood estimation (MLE). The log-likelihood function for the entire dataset $D$ can be defined as:

$$
\mathcal{L}(\Theta ; D)=\sum_{t=1 i=1}^{5} \log P\left(X_{t, i} \mid \operatorname{Pa}\left(X_{t, i} ; \Theta\right)\right)
$$

where $\Theta$ represents the parameters of the DBN and $D$ is the observed data.

The structure of the DBN was learned from data using the Peter and Clark (PC) algorithm. Let $D$ be the dataset; the objective is to find the optimal structure $G$ that maximizes the likelihood of the data:

$$
G_{\text {optimal }}=\operatorname{argmax}_{G} P(D \mid G)
$$

The PC algorithm efficiently explores possible network structures by systematically identifying conditional independence relationships among data variables, which helps to determine the structure of the DBN. The PC algorithm constructs a DAG starting from an empty graph by adding edges based on a statistical test of conditional independence $(36,37)$. It constructs a partially directed acyclic graph (PDAG) and applies rules such as the "V-structure" and "immorality" rules to obtain a full DAG.

The DBN parameters $(\bar{\varepsilon})$, including conditional probability tables, were estimated from the data $D$ using the following mathematical formula:

$$
\theta_{\text {optimal }}=\operatorname{argmax}_{\theta} P\left(D \mid \theta, G_{\text {optimal }}\right)
$$

This step involves estimating the parameters that maximize the likelihood of the data, given the chosen DBN structure.

![img-1.jpeg](img-1.jpeg)

FIGURE 2 Temporal causal pathways in DAGs for child undernutrition. NB: The detailed DAG causal pathways are listed in Supplementary Table S5 because the number of causal pathways across time points is extensive and difficult to display in a single DAG structure.

Maximum *a posteriori* (MAP) queries, also known as the most likely explanation (MPE), aim to determine the most likely state of the target variables based on the evidence observed in the data. MAP estimation in DBNs involves finding the sequence of hidden states that maximizes the posterior probability, given the observed evidence. This can be formulated using Bayes' theorem as follows:

$$argmax_xP(X_t|E_{1:t}) = argmax_x\frac{P(E_{1:t}|X_t)P(X_t)}{P(E_{1:t})}$$

where:

*X<sub>t</sub>* represents the hidden state at time *t*; *E<sub>1:t</sub>* denotes the evidence observed up to time *t*; *P(X<sub>t</sub>|E<sub>1:t</sub>)* is the posterior probability of the hidden state given the evidence; *P(E<sub>1:t</sub>|X<sub>t</sub>)* is the likelihood of observing evidence given the hidden state; *P(X<sub>t</sub>)* is the prior probability of the hidden state; and *P(E<sub>1:t</sub>)* is the marginal likelihood of the evidence.

The relevance tree algorithm was utilized to compute the MAP estimate, which efficiently found the most likely sequence of hidden states based on model parameters and observed data. This algorithm is particularly useful for computing probabilities in DBNs with large state spaces and complex variables because it constructs a tree structure.

In causal inference, we model counterfactual outcomes to estimate the probability of an event under hypothetical conditions. Let *Y* represent the outcome of interest, such as child nutritional status, and let *X* = {*X<sub>1</sub>*, *X<sub>2</sub>*, ..., *X<sub>n</sub>*} be a set of covariates, including factors like household, caregiver, and parental information. To formalize counterfactual reasoning, we typically use a causal graph or a Bayesian network, where directed edges represent the causal dependencies between variables.

In this framework, the counterfactual probability can be expressed as:

$$P(Y^{\text{ef}} = y \mid do(X^{\text{ef}} = x))$$

Here, *Y<sup>ef</sup>* refers to the counterfactual outcome of *Y*, representing the value that would have been observed if the hypothetical conditions *X<sup>ef</sup>* = *x* were true. In contrast, *Y* is the observed outcome under normal conditions. Similarly, *X<sup>ef</sup>* = *x* refers to a set of counterfactual conditions, which represent a hypothetical intervention or modification of the covariates. The operator, *do(X<sup>ef</sup>* = *x*) denotes an intervention where we actively set *X<sup>ef</sup>* = *x*, effectively modifying the system. Therefore, the expression *P(Y<sup>ef</sup>* = *y* | *do(X<sup>ef</sup>* = *x*)) gives the counterfactual probability of *Y* = *y* if the intervention *X<sup>ef</sup>* = *x* had been applied. For instance, if we consider *X* to represent maternal education level and *Y* as child nutritional status, the counterfactual probability *P(Y<sup>ef</sup>* = *y* | *do(X<sup>ef</sup>* = *x*)) quantifies the likelihood of different nutritional outcomes had the maternal education level been fixed at *x*, regardless of other influencing factors.

### Model performance metrics

Model performance was assessed using three key metrics: log-likelihood and Value of Information (VOI). The log-likelihood metric assesses how well the model fits the observed data and provides an indication of its accuracy. Finally, VOI measures the potential value of acquiring additional information to improve the model's predictions.

### Computational environment

The study evaluated various software options, including GeNIe and SMILE (38), Hugin Expert (39), Netica (40), R (bnlearn and gRain packages) (41--43), and BayesiaLab (44). Bayes Server Desktop version 10.9 was found to be most effective for managing the complexities of a DBN model with numerous variables. It enabled precise inference, updated beliefs, and assessed uncertainty in child nutrition decisions. The intuitive graphical interface and efficient analysis were achieved on a system with an Intel i7-9300H, NVIDIA GTX 1650 GPU, and 32 GB of RAM.

### Results

### Conditional probabilities of child nutritional status and household characteristics over time

In 2016, 41% of the children from households without any program enrollment had a normal nutritional status. In contrast, those enrolled in the PEH in 2013 had a 49% chance of having a normal nutritional status and a 15% chance of being underweight and wasting concurrently (UW). Between 2009 and 2013, in 2016, 58% of the households participating in the PEH and PEH programs were normal children, 16% were underweight, and 16% were wasting children (Figure 3).

Figure 4 shows the conditional probabilities of children's undernutrition status based on the parents' education levels over time. In 2016, children with illiterate parents had a greater risk of developing underweight and stunted conditions concurrently than those with literate parents. The risk was 30% greater for children with illiterate fathers and 26% greater for children with literate mothers.

The study showed that in 2016, mothers in households without prior intervention had a 57% chance of improved well-being. For those who joined after 2013, the likelihood increased to 75%. However, the number of households that joined in 2009 but discontinued after 2013 decreased to 69%. Among those engaged since 2009, 79% had significantly increased well-being, indicating that sustained program participation positively impacts mothers' well-being. In 2016, households that were not in the intervention program had a 60% probability of securing food access. Those participating in 2009 or 2013 had a 72% probability, whereas those participating in both years had a 95% probability. Finally, in 2016, households not previously enrolled in the programme had a 24% probability of being wealthy. For those who received support from 2013 onward, the probability increased to 68%. For households supported beginning in 2009, but discontinued after 2013, the probability was 64%. Households that have been continuously supported since 2009 have an 84% probability of earning wealth (Figure 5).

Moreover, since 2009, the likelihood of a child being classified as having normal nutritional status in 2013 was 47% when she was a family with access to food security. This probability increased to 54% in 2016 for children from households that had gained access to food security in 2013. In contrast, the likelihood of a child experiencing concurrent underweight, stunting, and wasting (USW) in 2013 was 11% among families with continuous access to secure food since 2009. This probability has decreased slightly to 11% in 2016 for a child in a household with sustained food security since 2013 (Figure 6).

### Key household and parental factors influencing food security, well-being, wealth, and child nutrition outcomes

In 2009, households with more than six members in the poor wealth quintile and those participating in PSNP programs were most likely to experience food insecurity. By 2013, households with fewer than six members in the poor wealth quintile and enrolled in both PSNP and EAP programs were most likely to have secure food access. By 2016, households with fewer than six members in the economically wealthy quintile and participating in all three programs (PSNP, EAP, and HEP) were most likely to maintain food security (Table 2).

In 2002, 2006, and 2009, mothers not enrolled in the intervention program were most likely to have low subjective well-being regardless of their age. However, in 2013 and 2016, mothers under the age of 30 but enrolled in EH and PEH, respectively, were most likely to have high subjective well-being (Table 3).

In 2002 and 2006, households were most likely to be poor if the mother was illiterate, both parents were aged 18--30, or the household head was male, regardless of the father's education level and household head's age. However, in 2009, 2013, and 2016, households headed by males aged 30--50 years and fathers of the same age range were more likely to achieve wealth when enrolled in PE, PEH, or PE programs, respectively (Table 4).

In 2002, households with illiterate fathers and literate mothers were most likely to have undernourished (US) female infants. By 2006, households with illiterate mothers, literate fathers, and wealthier status were the most likely to have stunted male children. Conversely, in 2009, households with literate mothers and illiterate fathers in poor conditions had a greater chance of being undernourished (SW) preadolescent males. In 2013, households with both literate parents and wealthier status were most likely to have preadolescent females with normal nutritional status. Finally, in 2016, households with literate mothers, illiterate fathers, and wealthier status were most likely to have wasted adolescent females (Table 5).

### Causal pathway strength over time: evidence from posterior probabilities in the DAG model

Due to the extensive number of causal pathways across time points, displaying them all in a single DAG structure has been challenging. The DAG structure presents detailed causal pathways across time points based on hard evidence, with parent and child nodes and their causal edges indicated by right arrows (Supplementary Table S5). These arrows show the temporal direction

![img-2.jpeg](img-2.jpeg)

FIGURE 3 Conditional probability of child nutritional status by household program participation status over time.

of the causal connection, specifying which parent node is connected to a child node at which time slice. Additionally, temporal dependency edges are included, indicating where a node has a connection to itself across time slices. The probabilities indicate edge strength, with higher probabilities indicating stronger relationships or causation.

In this study, we found varying edge probabilities in the relationship from PS → MSW in the posterior DAG across different waves, ranging from 74 to 93%, indicating a consistent strengthening of this connection over time. Mothers in households involved in EH and PEH intervention programs exhibited higher levels of subjective well-being. The edge probabilities for PS → FS and PS → WQ were 100% during waves 2, 3, and 4 as well as during waves 3 and 4. This perfect certainty in the posterior DAG suggests a robust link between household food security and wealth quintiles within combined initiative programs. Specifically, households with fewer than six members who received assistance from both the PSNP and EAP in 2013 were more likely to have secure access to food (Supplementary Table S5).

The study revealed a strong relationship between the wealth quintile and food security, with a near-certain relationship in Waves 2 and 4 (99.99%) and a slightly weaker but still significant relationship in Wave 3 (95%). This finding underscores the substantial impact of wealth quintiles on food security, indicating that individuals in higher-wealth quintiles are more likely to experience better food security than those in lower-wealth quintiles. The relationship between food security and undernutrition was 48% in Wave 2, rising to 100% in both Wave 3 and Wave 4. This finding indicates a strong and enduring link between food security and children's nutritional status over time.

### Examining child nutrition outcomes in Ethiopia: best- and worst-case situation

The study aimed to find a condition that reduce child undernutrition (best-case situation) in Ethiopia by setting the "Normal" category to 100% and adjusting counterfactual values. The original values for underweight (U), stunted (S), and wasting (W) were 3.8, 7.8, and 5.3%, respectively. For combined undernutrition conditions, the initial values were underweight and wasting (US) at 14.1%, underweight and stunting (UW) at 11.1%, stunting and wasting (W) at 9.9%.

![img-3.jpeg](img-3.jpeg)

FIGURE 4 Conditional probability of child nutritional status based on parental education history.

wasting (SW) at 0.1%, and a combination of all three conditions (USW) at 8.1%. This idealized scenario represents a condition in which no child suffers from undernutrition.

The corresponding counterfactual results under the header "Predicted" are listed in Supplementary Table S6. The up and down arrows next to the predicted value indicate an increase and decrease, respectively, compared with the original value. The results of the best-case counterfactual situations can be interpreted as follows. The results of the best-case counterfactual scenarios reveal that by the time children reach eight years old (time slice 2), households with fewer than six members experience increased counterfactual probabilities of 31.7, 26.2, and 21.2% for time slices 2, 3, and 4, respectively, compared to the original values. This trend suggests that smaller household sizes during early childhood may reduce the likelihood of undernutrition. As household size increases, food insecurity also tends to increase, which in turn increases the likelihood of children experiencing undernutrition. Likewise, counterfactual probabilities for poor maternal subjective well-being decreased as children aged 8 to 15–28.3, 21.4, and 14.3% for time slices 2, 3, and 4, respectively—compared to the original probabilities. Simultaneously, the probabilities for better subjective well-being increased (31.4, 19.7, and 23.1%), highlighting the importance of improving maternal well-being as an effective strategy for reducing child undernutrition. Similarly, the decreased counterfactual probabilities for poor maternal well-being—28.3, 21.4, and 14.3% for time slices 0, 1, and 2, respectively—indicate an improvement as children age to 8 years.

To emphasize the worst-case situation, the probability of a child being categorized as 'Undernourished' is set to 100%, which represents a scenario where every child is experiencing some form of undernutrition. Conversely, the probability of children being classified as 'Normal' (i.e., not undernourished) is set to 0%. The model shows that a low subjective well-being of mothers significantly impacts child undernutrition, with the probability of children being undernourished increasing as the mother's well-being declines. This is particularly evident in the later time slices, where the probability reaches 3.1% for those in high well-being and 40.2% for those in low well-being. Smaller households (<=6 members) initially have a higher probability of undernutrition (38.2% in Time slice 0), but this decreases over time. Larger households (>6 members) initially experience a smaller proportion of undernutrition, but this increases in later time slices (Supplementary Table S7). Similarly, poor households and those experiencing food insecurity show much higher probabilities of undernutrition across all time slices. In contrast, wealthier households and those with food security experience fluctuations, but they generally see a higher probability of 'Normal' status compared to their poorer counterparts. Similarly, illiterate fathers and mothers contribute to a higher likelihood of child undernutrition. However, the scenario shows a complex pattern with some improvements in later time slices, possibly due to interventions or other factors impacting education.

### Impact of intervention programs on combating child undernutrition

As shown in Figure 7, the predicted counterfactual probability of household program participation combinations across each time slice is visualized for both the best- and worst-case scenarios. In the most favorable scenario, the probability of program participation (except EH) is highest at time slice 2, followed by time slice 3, and decreases further at time slice 4. In contrast, in the least favorable scenario, the probability shows a decline from time slice 2 to time slice 3, and again from time slice 3 to time slice 4. This suggests that early household participation in the program provides the most effective scenario for improving children's nutritional status, whereas decreased participation over time correlates with higher likelihoods of child undernutrition.

For non-beneficiary households under the best-case scenario, the predicted probability is lowest at time slice 2 and increases in time slices 3 and 4. Conversely, under the worst-case scenario, this probability is highest at time slice 2 and decreases in subsequent time slices, indicating a greater risk of undernutrition for non-participating households.

![img-4.jpeg](img-4.jpeg)

FIGURE 5 Conditional probabilities of household characteristics over time by programme participation status.

![img-5.jpeg](img-5.jpeg)

FIGURE 6 Trends in the conditional probability of child undernutrition in food-secured households.

## Performance metrics of DBN model

Table 6 shows that variables such as MSW, DE, PS, HS, and MA had higher mutual information values, indicating stronger relationships with child undernutrition within the network. Additionally, variables such as PS, DE, HS, CA, and FS exhibit high target entropy reduction, suggesting their importance in reducing uncertainty within the network. Conversely, covariates such as DE, PS, HS, MA, and MSW exhibited lower target entropy values, implying lower uncertainty and greater predictability of the target variable compared to other covariates in the network (Table 6).

## Discussion

Child malnutrition is a complex health problem affected by various factors, such as food security, socioeconomic status, parental education, mother well-being, and access to healthcare services, as indicated in previous research studies (45, 46).

In our study, we found that children with educated parents were more likely to have a normal nutritional status. A recent study by Zhu et al. (47) revealed that socioeconomic factors impact the body mass index (BMI) of both primary and secondary caregivers, which in turn affects the BMI of their children through a causal relationship. Research has demonstrated that the educational level of parents and

primary caregivers significantly impacts the nutritional status of children, with improvements in nutritional status observed as education levels increase (48, 49).

Access to nutritious food and essential services such as clean water, electricity, healthcare, and proper sanitation facilities tends to increase as household wealth increases. This improvement in access leads to better nutritional status for children. In this regard, the intervention program showed a significant association with wealth quantiles (PS $\rightarrow$ WQ), particularly in the 4th and 5th waves, suggesting a positive impact on household wealth improvement. Research indicates that children from economically disadvantaged and displaced families are particularly vulnerable and may require assistance in accessing food and healthcare services (50-52).

The study highlights the substantial impact of mother well-being on child nutrition, attributed to improved mental health, emotional availability, and caregiving practices. Mothers with enrolled households in the program were most likely to report high subjective well-being (PS $\rightarrow$ MSW). Health workers, through regular nutritional counseling, significantly improve child-feeding practices, reducing undernutrition risk in children. Sunguya et al. (53) showed that health workers' nutritional training enhances feeding frequency, energy intake, and dietary diversity in children aged six months to two years. Furthermore, this study is supported by a study by Miller et al. (54), which highlighted the effective management of children by health extension workers.

TABLE 2 Maximum posterior effect of household characteristics on food security.


TABLE 3 Maximum posterior effect of maternal characteristics and program enrollment on subjective well-being.


Dash $(-)$ indicates that the program was not available in that specific time slice.

The study showed that the improvement in a household's food security status is conditional on the combination of the intervention program (PS $\rightarrow$ WQ), indicating that the intervention program positively impacts household food security. A study by Tadesse and Gebremedhin (55) using propensity score matching found that PSNP significantly enhances the income and food security of households in chronically food-insecure areas by increasing consumption expenditure and daily caloric intake. This finding is further supported by a study conducted by Bahru et al. (18), which also confirmed the positive impact of PSNP on household food security and child meal frequency. Furthermore, a study conducted by Gilligan and Hoddinott (56) using a difference-in-differences matching estimator revealed that households in rural areas affected by drought experienced improvements in food security when they received support from emergency food aid programs.

The DBN model predicts that household participation like in PSNP, EAP, and PE programs can significantly reduce undernutrition in the best-case conditions. However, counterfactual probabilities for non-beneficiary households are higher. These results highlight the impact of program interventions on reducing undernutrition over time, emphasizing the higher risk of undernutrition without support. Early and sustained program engagement is crucial for improving children's nutritional outcomes. The best-case conditions for reducing childhood undernutrition in households are based on earlier participation in the program (except EH program combination), with the higher predicted probabilities for participation in the intervention program and clearly visualized in Figure 7.

Strong temporal causation is shown in the Supplementary Table S5 for variables such as CNS, PS, FS, and WQ, all of which have a significant effect on child undernutrition in Ethiopia. From time 0 to time 1, the CNS is extremely dependent, however PS shows long-lasting benefits from time 2 to 4 . In order to reduce undernutrition, FS is essential for mitigating undernutrition, and WQ highlights the significance of household economic position. Weaker temporal dependencies like household head age and child age indicate that the influence of variables diminishes with time.

## Strengths, limitations, and future work

A significant methodological contribution of this study is the application of DBNs to analyze child undernutrition, a relatively novel approach in public health research. This study demonstrates how DBNs can provide temporal dependencies, capturing how risk factors and nutritional states change and influence each other over different time periods.

TABLE 4 Maximum posterior effect of household characteristics and program enrollment on wealth status over time.


Dash $(-)$ indicates that the program was not available in that specific time slice.

TABLE 5 Maximum posterior effect of parental education and household wealth on child nutritional status over time.


Dash (–) indicates that the program was not available in that specific time slice.

![img-6.jpeg](img-6.jpeg)

FIGURE 7 Most- and least favorable situation of child undernutrition in Ethiopia based on household participation in intervention programs.

To maintain a manageable publication length, we opted not to include the predicted counterfactual probabilities for all seven undernutrition states, as presenting each state individually would be overly bulky. Instead, these states were consolidated into a single "Undernourished" category, for modeling worst-case situation of child undernutrition. Additionally, query outputs for all variables and time steps were excluded, as they were primarily used internally for structure learning, assessing causal pathway, and edge strengths within the DBN. A system with 13 nodes has an order of 2^{16} possible graph structures, as calculated using the formula $$ \left( \frac{n(n-1)}{2} \right) $$. Due to this immense complexity, attempting to visualize all potential graph structures for a system with 16 nodes and 5 time points becomes practically impossible.

For future researchers working with DBNs, access to high-performance computing systems is essential to handle larger models efficiently. Future research could explore hybrid models that integrate additional machine learning techniques and causal artificial intelligence (AI), which are supported in Bayes Server through its API, to capture more complex relationships and enhance causal insights.

TABLE 6 Predictive performance of nodes in the DBN.

information | Target
entropy
reduction | Target
entropy  |

## Conclusion

Overall, our DBN model offers a novel approach for understanding child undernutrition in Ethiopia by capturing temporal relationships and identifying critical risk factors. This study demonstrates how DBNs can enhance public health research, providing policymakers and practitioners with a predictive tool for targeted interventions. The combined intervention program showed a strong causal relationship with enhancing the food security, wealth, and subjective well-being of mothers. Wealth quantiles provide better access to nutritious food, healthcare services, and education, which are vital for ensuring optimal growth and development in children. Food security ensures that adequate, safe, and nutritious food for healthy growth is essential for promoting healthy growth in children. Mothers' subjective well-being, including mental health, stress levels, and overall satisfaction, also influences children's nutritional status.

The study provides valuable insights for policymakers and health practitioners to simulate "what-if" scenarios to optimize nutritional outcomes and forecast at-risk situations leading to child undernutrition. It highlights high-risk factors like food insecurity, low maternal education, and household economic challenges, highlighting areas for targeted interventions. The DBN model suggests addressing these risk factors early in a child's life to prevent undernutrition onset or worsening, advocating for policies focused on maternal and child health during critical developmental periods. This tool aids in informed decision-making and improving child health and nutrition in Ethiopia.

## Data availability statement

The original contributions presented in the study are included in the article/Supplementary material, further inquiries can be directed to the corresponding author.

## Ethics statement

Ethical approval was not required for the study involving humans in accordance with the local legislation and institutional requirements. Written informed consent to participate in this study was not required from the participants or the participants' legal guardians/next of kin in accordance with the national legislation and the institutional requirements.

## Author contributions

GB: Data curation, Formal analysis, Investigation, Methodology, Software, Writing - original draft, Writing - review \& editing. TZ: Conceptualization, Data curation, Methodology, Software, Supervision, Validation, Writing - review \& editing. HF: Conceptualization, Formal analysis, Methodology, Software, Supervision, Validation, Writing - review \& editing.

## Funding

The author(s) declare that no financial support was received for the research, authorship, and/or publication of this article.

## Acknowledgments

The authors express their sincere gratitude to the reviewers for their insightful comments and suggestions, which greatly improved this manuscript. We also thank the Young Lives Study teams and the UK Data Service for providing access to the data files used in this research.

## Conflict of interest

The authors declare that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.

## Publisher's note

All claims expressed in this article are solely those of the authors and do not necessarily represent those of their affiliated organizations, or those of the publisher, the editors and the reviewers. Any product that may be evaluated in this article, or claim that may be made by its manufacturer, is not guaranteed or endorsed by the publisher.

## Supplementary material

The Supplementary material for this article can be found online at: https://www.frontiersin.org/articles/10.3389/fpubh.2024.1399094/ full\#supplementary-material

[^0]
[^0]:    5. Shenoy S, Sharma P, Rao A, Aparna N, Adenikinju D, Ilogghu C, et al. Evidence-based interventions to reduce maternal malnutrition in low and middle-income countries: a systematic review. Frontiers in Health Services. (2023) 3:5. doi: 10.3389/fchs.2023.1155928
    6. Das S, Rahman RM. Application of ordinal logistic regression analysis in determining risk factors of child malnutrition in Bangladesh. Nutr J. (2011) 10:1-11. doi: $10.1186 / 1475-2891-10-124$
    7. Teelaw LM, Fenta HM. Multivariate logistic regression analysis on the association between anthropometric indicators of under-five children in Nigeria: NDHS 2018. BMC Pediatr. (2021) 21:1-13. doi: 10.1186/s12887-021-02657-5
    8. Moss M, Wellman DA, Cotsonis GA. An appraisal of multivariable logistic models in the pulmonary and critical care literature. Chest. (2003) 123:923-8. doi: 10.1378/chest.123.3.923

9. Ottenbacher KJ, Ottenbacher HR, Tooth L, Ostir GV. A review of two journals found that articles using multivariable logistic regression frequently did not report commonly recommended assumptions. J Clin Epidemiol. (2004) 57:1147-52. doi: 10.1016/j.jclinepi.2003.05.003
10. Egata G, Berkaee Y, Worku A. Seasonal variation in the prevalence of acute undernutrition among children under five years of age in east rural Ethiopia: a longitudinal study. BMC Public Health. (2013) 13:1-8. doi: 10.1186/1471-2458-13-864
11. Bahru BA, Bosch C, Birner R, Zeller M. Drought and child undernutrition in Ethiopia: a longitudinal path analysis. PLoS One. (2019) 14:e0217821. doi: 10.1371/ journal.pone. 0217821
12. Vittinghoff E, Glidden DV, Shiboski SC, McCulloch CE, Vittinghoff E, Glidden DV, et al. Repeated measures and longitudinal data analysis. Regress Methods Biostat. (2012):261-308. doi: 10.1007/978-1-4614-1353-0_7
13. Liu X. Methods and applications of longitudinal data analysis. Amsterdam, Netherlands: Elsevier (2015).
14. Jeyaseelan V, Sebastian T, Lakshmanan J, Bangdiwala SI. Longitudinal data analysis of mean passage time among malnutrition states: an application of Markov chains. J Appl Stat. (2016) 43:2729-39. doi: 10.1080/02664763.2016.1143454
15. Owosye SM, Oseni BM, Gayawan E. Estimating lifetime malnourished period and its statistics based on the concept of Markov chain with reward. Heliyon. (2020) 6:e04073. doi: 10.1016/j.heliyon.2020.e04073
16. Hoddinett J, Sjekasha TJ. Social protection, household size, and its determinants: evidence from Ethiopia. J Dev Stud. (2020) 56:1818-37. doi: 10.1080/00220388.2020.1736283
17. Pérez Albertos Á. Evaluating public works programs' impact on children's outcomes: further evidence from the PSNP in Ethiopia. Universidad Pontificia Comillas, Facultad de Ciencias Humanas y Sociales. (2018).
18. Bahru BA, Jebena MG, Birner R, Zeller M. Impact of Ethiopia's productive safety net program on household food security and child nutrition: a marginal structural modeling approach. SSM Popul Health. (2020) 12:100660. doi: 10.1016/j.ssmph.2020.100660
19. Kevin P. Dynamic bayesian networks: Representation, inference and learning. PhD thesis, Berkeley, California, USA: University of California (2002).
20. Pearl J. Causality: Models, reasoning, and inference. Cambridge, England, UK: Cambridge University Press, 2000 (2003).
21. Orphanou K, Stassopoulou A, Keravnou E. DBN-extended: a dynamic Bayesian network model extended with temporal abstractions for coronary heart disease prognosis. IEEE J Biomed Health Inform. (2015) 20:944-52. doi: 10.1109/ JBHI.2015.2420534
22. Ghanmi N, Mahjoub MA, Amara NEB. Characterization of dynamic Bayesian network-the dynamic Bayesian network as temporal network. Int J Adv Comput Sci Appl. (2011) 2: 66-75. doi: 10.14569/JJACSA.2011.020708
23. Brandherm B, Jameson A. An extension of the differential approach for Bayesian network inference to dynamic Bayesian networks. Int J Intell Syst. (2004) 19:727-48. doi: 10.1002/ias. 20022
24. How M-L, Chan YJ. Artificial intelligence-enabled predictive insights for ameliorating global malnutrition: a human-centric ai-thinking approach. AI. (2020) 1:4. doi: 10.3390/ai1010004
25. Kolbe D, Friedman N. Probabilistic graphical models: principles and techniques. Cambridge, Massachusetts, USA: MIT press (2009).
26. Fenton N, Neil M. Risk assessment and decision analysis with Bayesian networks. Boca Raton, Florida, USA: Crc Press (2018).
27. Shigashara P, Lopez ADA, Mauricio D. Dynamic Bayesian network modeling, learning, and inference: a survey. IEEE Access. (2021) 9:117639-48. doi: 10.1109/ ACCESS.2021.3105520
28. Boyden J. Young lives: an international study of childhood poverty: round 22006 (study\# SN 6852); round 32009 (study\# SN 6853). University of Oxford, Department of International Development. (2012).
29. Lives Y. Equating cognitive scores across rounds and cohorts for young Lives in Ethiopia, India, Peru and Vietnam. University of Oxford, Department of International Development. (2020).
30. Argaw BA. Regional inequality of economic outcomes and opportunities in Ethiopia: a tale of two periods. WIDER Working Paper; (2017). Report No.: 9292563424.
31. Porter C, Favara M, Woldebanna T. Smarter through social protection? Evaluating the impact of Ethiopia's safety-net on child cognitive abilities. Institute of Labor Economics. (2017).
32. Wang H, Tesfaye R, Ramana GN, Chekagn CT. Ethiopia health extension program: An institutionalized community approach for universal health coverage. Washington, D.C., USA: World Bank Publications (2016).
33. Aurino E, James Z, Rolleston C. Young Lives Ethiopia school survey 2012-13: Data overview report: Young Lives. University of Oxford, Department of International Development. (2014).
34. Gomes IP, Wolf DF. Health monitoring system for autonomous vehicles using dynamic Bayesian networks for diagnosis and prognosis. J Intell Robot Syst. (2021) 101:1-21. doi: 10.1007/s10846-020-01293-y
35. Ladysynski P, Molik M, Foltynski P. Dynamic Bayesian networks for prediction of health status and treatment effect in patients with chronic lymphocytic leukemia. Sci Rep. (2022) 12:1811. doi: 10.1038/s41598-022-05813-8
36. Zhang G, Zhang A, Calhoun VD, Wang Y-P. A causal brain network estimation method leveraging Bayesian analysis and the PC algorithm. Medical imaging 2020: Biomedical applications in molecular, structural, and functional imaging. Bellingham, Washington, USA: SPIE (2020).
37. Fazal R, Alam MS, Hayat U, Alam N. Effectiveness of monetary policy: application of modified Peter and Clark (PC) algorithms under graph-theoretic approach. Sci Ann Econ Business. (2021) 68:333-44. doi: 10.47743/saeb-2021-0019
38. Jongsawat N, Poompuang P, Prentchaiowadi W, editors. Dynamic data feed to bayesian network model and SMILE web application. 2008 ninth ACIS international conference on software engineering, artificial intelligence, networking, and parallel/ distributed computing. (2008). IEEE.
39. Andersen SK, Olesen KG, Jensen FV, Jensen F. HUGIN-A Shell for building Bayesian belief universes for expert systems. Menlo Park, California, USA: IJCAI (1989).
40. Zou X, Yue WL. A bayesian network approach to causation analysis of road accidents using netica. J Adv Transp. (2017) 2017:1-18. doi: 10.1155/2017/2525481
41. Scutari M. Bayesian network constraint-based structure learning algorithms: parallel and optimised implementations in the bnlearn R package. arXiv. (2014). VV: 4-7. doi: 10.48550/arXiv.1406.7648
42. Scutari M. Package 'bnlearn'. Bayesian network structure learning, parameter learning and inference, R package version. The R Foundation for Statistical Computing. (2019):4.
43. Hanygaard S. Bayesian networks in R with the gRain package. J Stat Softw. (2012) $46: 1-26$.
44. Conrady S, Jouffe L. Introduction to bayesian networks \& bayesialab.Laval, France: Bayesia SAS (2013).
45. UNICEF. The state of food security and nutrition in the world Food and Agriculture Organization of the United Nations (FAO), International Fund for Agricultural Development (IFAD), UNICEF, World Food Programme (WFP), and World Health Organization (WHO). (2019). 2019 p.
46. Denby RW. Parental incarceration and kinship care: caregiver experiences, child well-being, and permanency intentions. Soc Work Public Health. (2012) 27:104-28. doi: 10.1080/19371918.2012.639639
47. Zhu W, Marchant R, Morris RW, Baur LA, Simpson SJ, Cripps S. Bayesian network modelling to identify on-ramps to childhood obesity. BMC Med. (2023) 21:105. doi: 10.1186/s12916-023-02789-8
48. Vollmer S, Bommer C, Krishna A, Harttgen K, Subramanian S. The association of parental education with childhood undernutrition in low-and middle-income countries: comparing the role of paternal and maternal education. Int J Epidemiol. (2017) 46:312-23. doi: 10.1093/ije/dyw133
49. Chen S, Richardson S, Kong Y, Ma N, Zhao A, Song Y, et al. Association between parental education and simultaneous malnutrition among parents and children in 45 low-and middle-income countries. JAMA Netw Open. (2023) 6:51727. doi: 10.1001/ jamanetworkopen. 2022.51727
50. Ruel MT, Alderman H. Nutrition-sensitive interventions and programmes: how can they help to accelerate progress in improving maternal and child nutrition? Lancet. (2013) 382:536-51. doi: 10.1016/S0140-6736(13)60843-0
51. Bhutta ZA, Das JK, Rizvi A, Gaffey MF, Walker N, Horton S, et al. Evidence-based interventions for improvement of maternal and child nutrition: what can be done and at what cost? Lancet. (2013) 382:432-77. doi: 10.1016/S0140-6736(13)60996-4
52. Owusu-Addo E, Cross R. The impact of conditional cash transfers on child health in low-and middle-income countries: a systematic review. Int J Public Health. (2014) 59:609-18. doi: 10.1007/s00038-014-0570-x
53. Sunguya BF, Poudel KC, Mlunde LB, Shakya P, Urassa DP, Jimba M, et al. Effectiveness of nutrition training of health workers toward improving caregivers' feeding practices for children aged six months to two years: a systematic review. Nutr J. (2013) 12:1-14. doi: 10.1186/1475-2891-12-66
54. Miller NP, Amouzou A, Hazel E, Legesse H, Degefe T, Tafesse M, et al. Assessment of the impact of quality improvement interventions on the quality of sick child care provided by health extension Workers in Ethiopia. J Glob Health. (2016) 6:404. doi: 10.7189/jogh.06.020404
55. Tadesse T, Gebremedhin ZT. The impact of the productive safety net program (PSSIP) on food security and asset accumulation of rural households': evidence from Gedeo zone, southern Ethiopia. Cogent Econ Finance. (2022) 10:2087285. doi: 10.1080/23322039.2022.2087285
56. Gilligan DO, Hoddinett J. Is there persistence in the impact of emergency food aid? Evidence on consumption, food security, and assets in rural Ethiopia. Am J Agric Econ. (2007) 89:225-42. doi: 10.1111/j.1467-8276.2007.00992.x
57. Begashaw G, B, Zewotir T, Fenta H. M. Multistate Markov chain modeling for child undernutrition transitions in Ethiopia: a longitudinal data analysis, 2002-2016. BMC Medical Research Methodology. (2024) 24:283.