# RESEARCH ARTICLE 

## A clinical decision support system learned from data to personalize treatment recommendations towards preventing breast cancer metastasis

Xia Jiang ${ }^{1}$, Alan Wells ${ }^{2,3}$, Adam Brufsky ${ }^{3,4}$, Richard Neapolitan ${ }^{5 *}$


#### Abstract

1 Department of Biomedical Informatics, University of Pittsburgh, Pittsburgh, Pennsylvania, United States of America, 2 Department of Pathology, University of Pittsburgh and Pittsburgh VA Health System, Pittsburgh, Pennsylvania, United States of America, 3 UPMC Hillman Cancer Center, University of Pittsburgh School of Medicine, Pittsburgh, Pennsylvania, United States of America, 4 Division of Hematology/Oncology, University of Pittsburgh School of Medicine, Pittsburgh, Pennsylvania, United States of America, 5 Department of Preventive Medicine, Northwestern University Feinberg School of Medicine, Chicago, Illinois, United States of America


* richard.neapolitan@northwestern.edu

## OPEN ACCESS

Citation: Jiang X, Wells A, Brufsky A, Neapolitan R (2019) A clinical decision support system learned from data to personalize treatment recommendations towards preventing breast cancer metastasis. PLoS ONE 14(3): e0213292. https://doi.org/10.1371/journal.pone.0213292

Editor: Joon Jeong, Gangnam Severance Hospital, Yonsei University College of Medicine, REPUBLIC OF KOREA

Received: October 16, 2018
Accepted: February 18, 2019
Published: March 8, 2019
Copyright: © 2019 Jiang et al. This is an open access article distributed under the terms of the Creative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

Data Availability Statement: We have submitted our dataset LSDB-5YDM to datadryad.org (DOI 10. 5061/dryad.64964m0).

Funding: Research reported in this paper was supported by grants R01LM011663 to XJ and R01LM011962 to RN awarded by the National Library of Medicine of the National Institutes of Health. The funder had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.

## Abstract

## Objective

A Clinical Decision Support System (CDSS) that can amass Electronic Health Record $(E H R)$ and other patient data holds promise to provide accurate classification and guide treatment choices. Our objective is to develop the Decision Support System for Making $\underline{P e r}$ sonalized Assessments and Recommendations Concerning Breast Cancer Patients (DPAC), which is a CDSS learned from data that recommends the optimal treatment decisions based on a patient's features.

## Method

We developed a Bayesian network architecture called Causal Modeling with Internal Layers (CAMIL), and an algorithm called Treatment Feature Interactions (TFI), which learns from data the interactions needed in a CAMIL model. Using the TFI algorithm, we learned interactions for six treatments from the LSDS-5YDM dataset. We created a CAMIL model using these interactions, resulting in a DPAC which recommends treatments towards preventing 5 -year breast cancer metastasis.

## Results

In a 5-fold cross-validation analysis, we compared the probability of being metastasis free in 5 years for patients who made decisions recommended by DPAC to those who did not. These probabilities are (the probability for those making the decisions appears first): chemotherapy (.938, .872); breast/chest wall radiation (.939, .902); nodal field radiation (.940, .784); antihormone (.941, .906); HER2 inhibitors (.934, .880); neadjuvant therapy (.931,

Competing interests: The authors have declared that no competing interests exist.
.837). In an application of DPAC to the independent METABRIC dataset, the probabilities for chemotherapy were (.845, .788).

## Discussion

Patients who took the advice of DPAC had, as a group, notably better outcomes than those who did not. We conclude that DPAC is effective at amassing and analyzing data towards treatment recommendations. Some of the findings in DPAC are controversial. For example, DPAC says that chemotherapy increases the chances of metastasis for many node negative patients. This controversy shows the importance of developing a conclusive version of DPAC to ensure we provide patients with the best patient-specific treatment recommendations.

## Introduction

Precision medicine promises to help us improve patient outcomes by tailoring healthcare to the individual patient. Researchers have made tremendous efforts in using results learned from "-omics" data to guide the development and selection of effective drugs for patients. However, the electronic health record (EHR) database, a widely available resource, has been underutilized for the purpose of tailoring therapies. An EHR database contains abundant data about patients' clinical features, disease status, interventions, and clinical outcomes, affording us the opportunity to provide highly-personalized medicine beyond only looking at the genomic level [1]. It is believed that, "coupled with new analytics tools, they open the door to mining information for the most effective outcomes across large populations" [2]. Such data are invaluable to tailoring treatments to individuals with diseases such as cancer and Alzheimer's disease.

Breast cancer is the most common cancer in women. Clinicians face hard decisions in many aspects of breast cancer. For example, image-guided core needle biopsy of the breast is a common procedure that can be non-definitive in $5 \%-15 \%$ of women. This makes it difficult to further classify breast cancer into subtypes. Variation in breast cancer subtypes has been known to be associated with a patient's drug response, progression of the tumor, and survival of the patient [3,4]. There is also great uncertainty in the treatment and prognosis for breast cancer. For example, HER2-amplified breast cancer is a subtype with poor prognosis if untreated, but the targeted therapeutic trastuzumab (Herceptin) has vastly improved the survival of such patients. Although Herceptin is used in the therapy of all patients with HER2-amplified tumors, only some respond. Furthermore, it is expensive and can cause cardiac toxicity [2]. So, it is important to give it only to patients who benefit from it. Other studies show that thousands of genes are associated with subtype and prognosis of breast cancer, and particular allele combinations may usefully guide the treatment selection [5]. A Clinical Decision Support System (CDSS) that can amass all this genomic information and combine it with clinical information holds promise to provide accurate classification and guide treatment choices.

We develop a Bayesian network architecture called Causal Modeling with Internal Layers (CAMIL), and an algorithm called Treatment Feature Interactions (TFI), which learns from data the interactions needed in a CAMIL model. We transform the CAMIL model to an influence diagram, resulting in a probability-based CDSS called Decision Support System for Making Personalized Assessments and Recommendations Concerning Breast Cancer Patients (DPAC), which recommends treatment decisions based on a patient's features. The DPAC, which we

develop in this paper, recommends six treatment decisions to prevent 5-year breast cancer metastasis, and is learned from the Lynn Sage Data Set with 5-Year Distant Metastasis (LSDS$5 Y D M$ ), which we curated. We evaluate DPAC using a 5 -fold cross-validation analysis, and by applying the DPAC learned from the entire LSDS-5YDM to the independent METABRIC breast cancer dataset [6]. In these evaluations, we compare the outcomes of patients who made the treatment decision recommended by DPAC to the outcomes of ones who did not make that decision. In both cases, patients who took the treatment advice of DPAC had, as a group, notably better outcomes than those who did not.

# Method 

Since DPAC is based on Bayesian networks and influence diagrams, we first review these.

## Bayesian networks

Bayesian networks (BN) are a leading architecture for handling uncertainty in artificial intelligence and machine learning [7-10]. A BN consists of a directed acyclic graph (DAG), whose edges represent direct probabilistic dependencies; the prior probability distribution of every variable that is a root in the DAG; and the conditional probability distribution of every nonroot variable given each set of values of its parents. Fig 1 shows a BN modeling relationships among variables related to respiratory diseases. The node $H$, which represents "history of
![img-0.jpeg](img-0.jpeg)

Fig 1. A Bayesian network.
https://doi.org/10.1371/journal.pone.0213292.g001

smoking", is a root. Since it is a root, the BN contains its prior probability distribution, which is the probability of an individual having a history of smoking given that the individual is from the population we are investigating. Assuming $20 \%$ of individuals in the population have smoked, we assign $P(H=$ yes $)=0.2$, and $P(H=\mathrm{no})=0.8$. The node $L$, which represents "lung cancer", is not a root; so the BN contains its conditional probability distribution given each value of its parent $H$. Assuming $0.3 \%$ of smokers in the population get lung cancer, we assign $P(L=$ yes $\mid H=$ yes $)=0.003$. Assuming $0.005 \%$ of nonsmokers in the population get lung cancer, we assign $P(L=$ yes $\mid H=$ no $)=0.00005$.

Using a BN, we can determine probabilities of interest with a BN inference algorithm [7]. For example, with the BN in Fig 1, if a patient has a smoking history $(H=$ yes $)$, positive chest X-ray $(X=$ pos $)$, and positive computer tomography $(C T=$ pos $)$, we can determine the probability of the patient having lung cancer $(L=$ yes $)$. That is, we can compute $P(L=$ yes $\mid H=$ yes, $X=$ pos, $C T=$ pos $)$, which turns out to be 0.185 .

Learning a BN from data concerns learning both the parameters and the structure (called a DAG model). In the score-based structure-learning approach, a score is assigned to a DAG model $G$ based on how well $G$ fits the Data. The Bayesian score [11] is the probability of the Data given DAG model G. For discrete variables, this score often uses a Dirichlet distribution to represent prior belief for each conditional distribution in $G$. The score is as follows:

$$
\operatorname{score}_{\text {Bayes }}(G: \text { Data })=P(\text { Data } \mid G)=\prod_{i=1}^{n} \prod_{j=1}^{q_{i}} \frac{\Gamma\left(\sum_{k=1}^{r_{i}} a_{i j k}\right)}{\Gamma\left(\sum_{k=1}^{r_{i}} a_{i j k}+\sum_{k=1}^{r_{i}} s_{i j k}\right)} \prod_{k=1}^{r_{i}} \frac{\Gamma\left(a_{i j k}+s_{i j k}\right)}{\Gamma\left(a_{i j k}\right)}
$$

where $n$ is the number of variables, $r_{i}$ is the number of states of $X_{i}, q_{i}$ is the number of different values that the parents of $X_{i}$ can jointly assume, $a_{i j k}$ is a hyperparameter, and $s_{i j k}$ is the number of times $X_{i}$ took its $k$ th value when the parents of $X_{i}$ took their $j$ th value. When $a_{i j k}=\alpha / r_{i} q_{i}$ for a parameter $\alpha$, the score is called the Bayesian Dirichlet equivalent uniform (BDeu) score [12]. The BN model selection problem is NP-hard [13]. So, heuristic search algorithms are often employed [7].

# Influence diagrams 

An influence diagram (ID) is a BN augmented with decision nodes and utility nodes. An ID not only provides us with a joint probability distribution, but also recommends decisions based on the patient's preferences. Fig 2 shows an ID modeling the decision of whether or not to be treated with a thoracotomy for a non-small-cell carcinoma of the lung, based on an ID in [14]. The nodes with prior probabilities in Fig 2 are chance nodes, as in BNs. The rectangular nodes are decision nodes. An edge into a decision node is an information edge and represents what is known when the decision is made. The hexagon node is a utility node, and represents the utility of the outcomes to the patient. Edges into this node represent features that directly affect this utility.

Algorithms for solving IDs determine the decision alternative for the first decision that maximizes expected utility [7]. For the ID in Fig 2, that decision is $C$, which is whether to have a CT scan. In this case the expected utility is the expected life span. It turns out that for $c 1$ the expected life span is 3.23 and for $c 2$ it is 2.76 . So the recommendation is $c 1$, which is to have the CT scan.

The utility of the outcome to the patient is often in terms of quality adjusted life years (QALY) [15] instead of simply years because some treatments and conditions significantly decrease the quality of life. When we use QALY, a year in which the patient is in perfect health has value 1 , being dead has value 0 , and a non-well year has some value between 0 and 1 . For example, a year with a sore throat is estimated to have a value of 0.9 [7]. We can assess QALYs

![img-1.jpeg](img-1.jpeg)

Fig 2. An influence diagram.
https://doi.org/10.1371/journal.pone.0213292.g002
following the guidelines in [7]. When we compute life expectancy using a time-trade-off quality adjustment, we call it quality adjusted life expectancy (QALE). We ordinarily use QALYs instead of simply life years as the utilities in a decision model concerning a treatment or surgery decision, and we make the decision that maximizes QALE.

# Development of DPAC 

A DPAC system is developed by learning treatment-feature interactions, incorporating the interactions into a Causal Modeling with Internal Layers (CAMIL) model, and then converting the CAMIL model to an influence diagram. We discuss each of these in turn.

In order to determine optimal treatment choices, we need to model how treatments interact with patient features to affect outcomes. For example, Herceptin is a treatment for breast cancer which is effective only for HER2+ patients; so Herceptin interacts with HER2 status to affect metastasis. We create a new algorithm that learns such interactions from data.

First, we need a definition of a treatment-feature interaction. The definition is first motivated by an example. Suppose

$$
\begin{gathered}
P(\text { metastasis } \mid \text { HER2+, Herceptin })=0.01 \\
P(\text { metastasis } \mid \text { HER2+, No Herceptin })=0.5
\end{gathered}
$$

$$
\begin{gathered}
P(\text { metastasis } \mid \text { HER2- }, \text { Herceptin })=0.3 \\
P(\text { metastasis } \mid \text { HER2- }, \text { No Herceptin })=0.02
\end{gathered}
$$

Then the use of Herceptin is strongly indicated for HER2+ patients and strongly contraindicated for HER2- patients. We would say there is a strong interaction between Herceptin and HER2 status. On the other hand, suppose

$$
\begin{gathered}
P(\text { metastasis } \mid \mathrm{ER}+, \text { Herceptin })=0.05 \\
P(\text { metastasis } \mid \mathrm{ER}+, \text { No Herceptin })=0.05 \\
P(\text { metastasis } \mid \mathrm{ER}-, \text { Herceptin })=0.03 \\
P(\text { metastasis } \mid \mathrm{ER}-, \text { No Herceptin })=0.03
\end{gathered}
$$

In this case, we would say there is no interaction between Herceptin and ER status. The Hellinger distance quantifies the degree of dissimilarity between two probability distribution [16]. Its value is 0 if they are the same probability distribution and 1 if they are maximally dissimilar. For a given binary feature and binary treatment, we first compute the Hellinger distance between the probability distribution of the target given the patient has the first value of the feature and had the treatment and the probability distribution of the target given the patient has the first value of the feature and did not have the treatment. We then compute the Hellinger distance between the probability distribution of the target given the patient has the second value of the feature and had the treatment and the probability distribution of the target given the patient has the second value of the feature and did not have the treatment. If the treatment is effective for one value of the feature, and deleterious for the other value of the feature, we take the strength to be the minimum of the two Hellinger distances; otherwise we take it to be 0 .

We are assuming that a given treatment is deleterious for some value of a feature with which it interacts because our preliminary investigations showed that this the case. For example, we found that chemotherapy increase the likelihood of 5-year metastasis for node-negative patients with low grade tumors. Our goal here is only to show the effectiveness of our method based on assuming the correctness of our knowledge. So, we are keeping the utility as simple as possible. In application, we would not require that a treatment be deleterious for one value of the feature, but rather we would add a utility node for the negative effect of the treatment on quality of life. If the treatment had a positive effect for a given set of values of the patient's features, the treatment decision would be based on weighing the benefit of the treatment for avoiding metastasis against the negative effect of the treatment on quality of life. In the next section we will show how quality of life can be considered in the treatment decision.

In general, a feature is not binary. So, we take the maximum Hellinger distance over all values of the feature for which the treatment is effective, the maximum Hellinger distance over all values of the feature for which the treatment is ineffective, and take the strength to be the minimum of these two maximums. Fig 3 shows the resultant algorithm, called Treatment Feature Interactions (TFI), when we are considering only a single feature. However, a given treatment can interact with several variables simultaneously. The algorithm in Fig 3 can be applied where $X$ represents a set of variables. In this research we apply it to sets containing 1, 2, 3, and 4 variables.

After applying Algorithm TFI to each treatment, we will have sets containing treatments and features. To develop a prediction algorithm using these sets, we use a model that assumes

# Algorithm: Treatment Feature Interactions (TFI) 

```
procedure Calculate_Strength;
    \(\max 1=0\);
    \(\max 2=0\);
    \(k=\) number of alternatives of \(X\);
    for \(i=1\) to \(k\)
        \(H=D(i)\);
        if \(P\left(T=t_{1} \mid X=x_{i}, R=r_{1}\right)>P\left(T=t_{1} \mid X=x_{i}, R=r_{2}\right)\)
            if \(H>\max 1\)
                \(\max 1=H\);
            endif
        else
            if \(H>\max 2\)
                \(\max 2=H\);
            endif
        endelse
    endfor // require both a positive
    if \(\max 1>0\) and \(\max 2>0 \quad / /\) and negative effect
        strength \(=\min (\max 1, \max 2)\);
    else
        strength \(=0\);
    endelse
```

function $D(i) \quad / /$ Calculate Hellinger Distance
term $1=\sqrt{P\left(T=t_{1} \mid X=x_{i}, R=r_{1}\right) \times P\left(T=t_{1} \mid X=x_{i}, R=r_{2}\right)}$;
term $2=\sqrt{P\left(T=t_{2} \mid X=x_{i}, R=r_{1}\right) \times P\left(T=t_{2} \mid X=x_{i}, R=r_{2}\right)}$;
$D(i)=\sqrt{1-\operatorname{term} 1-\operatorname{term} 2}$;
Fig 3. Algorithm TFI, which determines the strength with which binary treatment $R$ interacts with variable $X$ to affect binary target $T$.
https://doi.org/10.1371/journal.pone.0213292.g003
each set affects the target independently. Our model, called CAMIL, is a generalization of the Noisy-OR model. So, we first review that model.

The Noisy-Or Bayesian network model [17] concerns binary causes that independently cause a binary target. An example of the Noisy-Or model appears in Fig 4. In this example, there are 4 causes $C_{1}, C_{2}, C_{3}$, and $C_{4}$, of a disease $D$. The variables labeled $H_{i}$ are hidden. The value 1 represents that the cause is present and the value 0 represents that it is absent. Similarly, the value 1 represents that the disease $D$ is present and the value 0 represents that it is absent. The model assumes that the presence of each cause $C_{i}$ will result in $D$ being present, regardless of the presence of the other causes, unless $C_{i}$ is inhibited. Cause $C_{i}$ has probability $q_{i}$ of being inhibited when it has value 1 . The value of $1-q_{i}$ is called the causal strength of $C_{i}$ for $D$. It is

$$
\begin{aligned}
& P\left(H_{i}=0 \mid C_{i}=0\right)=1 \\
& P\left(H_{i}=0 \mid C_{i}=1\right)=q_{i}
\end{aligned}
$$

$$
\begin{aligned}
& P\left(D=0 \mid \text { all } H_{i}=0\right)=1 \\
& P\left(D=0 \mid \text { some } H_{i}=1\right)=0
\end{aligned}
$$

Fig 4. The Noisy-Or model.
https://doi.org/10.1371/journal.pone.0213292.g004
possible to show that

$$
P\left(D=0 \mid C_{1}, C_{2}, C_{3}, C_{4}\right)=\prod_{i: C_{i}=1} q_{i}
$$

So once we know the values of $q_{i}$, it straightforward to compute the probability of $D$ given any combination of the causes. To estimate the value of $q_{i}$ we can set

$$
q_{i}=\frac{a_{0}}{a_{0}+a_{1}}
$$

where $a_{0}$ is the number of records in which $C_{i}=1$, all other $C_{j}=0$, and $D=0$; and $a_{1}$ is the number of records in which $C_{i}=1$, all other $C_{j}=0$, and $D=1$.

If we had sufficient data, we could use Eq 1 to learn the parameters for the Noisy-Or model. However, if there are many predictors and the dataset is not extremely large, the values of $a_{0}$ and $a_{1}$ will be very small and often even zero for many predictors. So, we use an Expectation Maximization (EM) [7] algorithm to learn parameters. By using an EM algorithm we are able to learn something about $q_{i}$ from records that do not have $C_{i}$ equal to 1 and all other $C_{j}$ equal to 0 .

The leaky Noisy-Or model assumes that all causes that have not been articulated can be grouped into one hidden cause Leak. The hidden cause Leak is at the same level as the other

![img-2.jpeg](img-2.jpeg)

Fig 5. An example of a CAMIL model. This model is only for illustration. It was not learned from data.
https://doi.org/10.1371/journal.pone.0213292.g005
hidden variables (the $H_{i}$ ) but it has no parents. We have that

$$
P(\text { Leak }=0)=q_{\text {Leak }}
$$

An EM algorithm can learn $q_{\text {Leak }}$ along with the other parameters.
CAMIL is an extension of the Leaky Noisy-Or Model with the following additional features: 1) The causes may be non-binary; and 2) causes may interact. CAMIL assumes the interactions independently affect the target according to the assumptions in the Leaky Noisy-Or Model. Fig 5 shows an example in which three clinical features (HER2, P53, and PR) and three treatments (HER2inhibitor, Chemotherapy, and Antihormone) are the causes and the target is Survival. This network was not learned from data, but rather is only for illustration. The variables labeled $H_{i}$ are hidden binary variables. There is a single hidden variable for each interaction and each non-interacting cause. According to the model in Fig 5, HER2inhibitor and HER2 interact. So they are parents of a hidden variable. Similarly, Chemotherapy interacts with all three clinical variables. So they are all parents of a hidden variable. The Leak variable is also hidden, and represents causes not identified in the model.

If the parent variables of a hidden variable $H_{i}$ have $k$ values, there are $k$ conditional distributions for $H_{i}$. For example, if $H_{i}$ has one cause $C_{i}$, the distributions are as follows:

$$
\begin{aligned}
q_{i 1}= & P\left(H_{i}=0 \mid C_{i}=1\right) \\
q_{i 2}= & P\left(H_{i}=0 \mid C_{i}=2\right) \\
& \vdots \\
q_{i k}= & P\left(H_{i}=0 \mid C_{i}=k\right)
\end{aligned}
$$

An EM algorithm can learn the parameter values in a CAMIL model.
It is possible to extend the CAMIL model to a non-binary target as long as the target's values are on an ordinal scale. That is, the target has increasingly strong values such as low, medium, and high. For example, if these are the three values of the target, we give each hidden parent variable of the target values 1,2 , and 3 . If any parent has value 3 , the target has value high; if any parent has value 2 and no parent has value 3 , the target has value medium; if no parent has value 2 or 3 , the target has value low.

Once we learn a CAMIL model based on interactions between treatments and features, it is straightforward to convert it to an influence diagram. First, we make each treatment node a decision node. Then we create a value node as a child of each outcome node. For example, if the outcome is simply 5 -year survival, we can create a value node that has value 1 if the patient survives and value 0 otherwise. We call the resultant system DPAC.

# Datasets 

The Lynn Sage Data Base (LSDB) contains information about patients who came to the Lynn Sage Comprehensive Breast Center at Northwestern Memorial Hospital for care. The Northwestern Medicine Enterprise Data Warehouse (NMEDW) is a joint initiative across the Northwestern University Feinberg School of Medicine and Northwestern Memorial HealthCare, which maintains comprehensive data obtain from EHRs. Using the LSDB and the NMEDW, we curated a dataset named as the Lynn Sage Data Set with 5-year distant metastasis (LSDS$5 Y D M$ ), which includes records on 6726 breast cancer patients including clinical features and distant metastasis. The records span 03/02/1990 to 07/28/2015. Table 1 shows the clinical features and treatments in the LSDS-5YDM that are included in this study, and their values.

We discuss in some detail the variables whose meanings are not straightforward. Histology provides the nature of a tumor. That is, whether it is confined to the breast ducts, which are tubes that carry the milk to the nipple, or whether it has infiltrated the milk producing glands (lobules). If the breast cancer has a significant number of receptors for estrogen or for progesterone, it is considered estrogen receptor (ER) positive or progesterone receptor (PR) positive. HER2-positive breast cancer is cancer that tests positive for a protein called human epidermal

Table 1. The variables in the LSDS-5YDM that are included in this study.


https://doi.org/10.1371/journal.pone.0213292.t001

growth factor receptor 2 (HER2), which promotes the growth of cancer cells. P53 is a gene that codes for a protein that regulates the cell cycle and functions as a tumor suppression. If the gene is mutated, metastasis prognosis is worse.

We used 5-year metastasis as our target in this study. We assigned the value yes to metastasis if the patient had evident metastases within 5 years of the initial diagnosis, the value no to metastasis if it was known that the patient did not present with metastases within 5 years, and the value NULL to metastasis if the patient discontinued follow-up within the first five years and without evidence of metastases prior to loss to follow-up. The value NULL was also assigned to all missing data fields in all variables. Missing data were then filled in using the nearest neighbor (NN) imputation algorithm.

The Molecular Taxonomy of Breast Cancer International Consortium (METABRIC) data set [6] has data on 1989 breast cancer tumors. Features include 21 clinical features, expression levels for 16,384 genes, and breast cancer survival. The only treatment variable in the METABRIC dataset that is comparable to the ones we investigated is chemotherapy.

# Experiments 

Using the LSDS-5YDM and Algorithm TFI, we calculated the interaction strength, relative to the target being 5-year metastasis, of each treatment (chemo, breast_chest_radi, nodal_radi, antihormone, HER2_Inhib, neo) with all 1, 2, and 3, and 4 set combinations of other variables. We chose the highest scoring set $S$, and we then verified there were no common causes of the treatment and the target that were not independent of the target given the variables in $S$. We did this by forcing edges from the treatment and the variables in $S$ to the target, and then applying the Greedy Equivalent Search (GES) [7] to learn a BN containing all the variables. If the treatment and target did have a common cause that was not independent of the target given variables in $S$, we rejected $S$ and went down to the second highest scoring set. We then created a CAMIL model using the learned interactions where 5-year metastasis is the target, and learned parameter values for that model using the EM algorithm. Note that this algorithm learns the parameters for all the hidden nodes simultaneously, which entails that it takes into account the relative effect of the interactions on the target, and therefore the synergistic effects of the treatments. The CAMIL model was then converted to an ID by converting the nodes representing decisions to decision nodes, and adding a utility node, whose value was 0 if the patient metastasized in 5 years and 1 if she did not. The resultant system is called DPAC.

We did the procedure just described in a 5 -fold cross-validation analysis using the LSDS5YDM. For each fold, a DPAC system was learned from the records in the other 4 folds. This DPAC was then applied to each record in the fold to recommend the five decisions. The following values were recorded for each decision:
n1: The number of subjects who made the recommended decision
k1: The number of subjects who made the recommended decision and did not metastasize
n2: The number of subjects who did not make the recommended decision
k2: The number of subjects who did not make the recommended decision and did not metastasize

The values of $\mathrm{n} 1, \mathrm{k} 1, \mathrm{n} 2$, and k 2 were summed over all 5 folds, yielding summed values N 1 , $\mathrm{K} 1, \mathrm{~N} 2, \mathrm{~K} 2$. The ratio $\mathrm{K} 1 / \mathrm{N} 1$ then estimates the average utility if the subject made the recommended decision, which, due to the simplicity of the ID, is also the estimate of the probability of not metastasizing given one makes the recommended decision. The ratio $\mathrm{K} 2 / \mathrm{N} 2$ provides the same estimates for subjects who did not make the recommended decision.

Table 2. The result of the 5-fold-cross validation analysis. Row 6 shows the estimate of the probability of not metastasizing given the subjects made the decision recommended by the model, and Row 7 shows $95 \%$ confidence interval for that estimate. Rows 8 and 9 show the same values of individuals who did not make the decision recommended by the model.


https://doi.org/10.1371/journal.pone.0213292.t002

We applied a DPAC system, which was learned from the entire LSDS-5YDM data, to the independent METABRIC dataset. The outcome for this analysis was whether the patient died from breast cancer in 5 years because that is what was recorded in this dataset, and the only treatment analyzed was chemotherapy because that is all that was available.

# Ethics statement

This paper is a result of the PROTOCOL TITLE: A New Generation Clinical Decision Support System, which was approved by Northwestern University IRB \#: STU00200923-MOD0006.

The need for patient consent was waived by the ethics committee because the data consists only of de-identified data mined from EHR databases.

## Results

Table 2 shows the results of the 5 -fold cross-validation analyses. As a group, for every decision those who made the decision recommended by the model had notably better outcomes than those who did not. For every decision, the bottom of the $95 \%$ confidence interval for the probability of not metastasizing given one made the recommended decision is above the top of the $95 \%$ confidence interval for the probability of not metastasizing given one did not make the recommended decision.

Table 3 shows the results for chemotherapy when we applied the DPAC system, learned from the entire LSDS-5YDM, to the independent METABRIC dataset. These results are

Table 3. The result of applying the DPAC system, learned from the entire LSDS-5YDM, to the METABRIC dataset. Row 6 shows the estimate of the probability of not metastasizing given the subjects made the decision recommended by the model, and Row 7 shows $95 \%$ confidence interval for that estimate. Rows 8 and 9 show the same values of individuals who did not make the decision recommended by the model.


https://doi.org/10.1371/journal.pone.0213292.t003

![img-3.jpeg](img-3.jpeg)

Fig 6. The DPAC system learned from the entire LSDS-5YDM. The Leak node is not shown.
https://doi.org/10.1371/journal.pone.0213292.g006
similar to the ones obtained in the 5 -fold cross-validation; namely, as a group those who made the decision recommended by the model had better outcomes than those who did not, and notably again with the confidence intervals not overlapping.

Fig 6 shows the DPAC system learned from the entire dataset. Next we discuss that ID, and, while so doing, provide insight into some of the results in Table 2. Before proceeding, we note that the results may be considered controversial. One limitation that must be acknowledged is that the results follow from the single dataset at a single site, and that upon further analyses of other datasets from distinct clinical practices, the trends may not be replicated. However, the results are not a reflection on the model, and this communication concerns the approach more than the results. Nevertheless, the controversy does serve to demonstrate the importance of pursuing further large scale analyses.

A second limitation of the study is that 5 year follow-up is considered insufficient in most cases of breast cancer. Breast cancers tend to exhibit more extended periods of dormancy than most other carcinomas. In fact, more than half of the recurrences occur more than 5 years after initial diagnosis and intervention [18]. Further, confounding the analyses is that in the US, the majority of early recurrences occur in the subset of triple negative breast cancer (TNBC: ER-/PR-/HER2-), wherein a five-year disease free survival is considered almost like a cure [19].

According to DPAC, HER2 inhibitors interact with HER2 status and node status. According to the parameters for the model (not shown) HER2 inhibitors are effective only for HER2 positive subjects who also are node positive. They are actually deleterious for HER2 negative subjects. The use of HER2 inhibitors in HER2 negative subjects accounts for much of the poor outcomes for subjects who did not take the model's advice concerning HER2 inhibitors. As noted in the introduction, Herceptin has been shown to confer no benefit to some HER2 positive patients [2]. According to our model and data these are node negative subjects, which are subjects who already have a relatively low probability of showing metastases or recurrences within the five year time period. That is, the prior probability based on our data of metastasizing in 5 years given no additional information is 0.0792 and the prior probability given HER2 positive and node negative is 0.0513 .

Chemotherapy interacts with node status, ER status, HER2 status, and menopause. According to DPAC, it is effective for all node positive subjects. However, it is effective only for node negative subjects who are pre-menopausal and both ER and HER2 positive or both ER and HER2 negative (this last group is mainly the aggressive TNBC subtype). Previous research has shown that HER2 and ER interact to affect metastasis [20], and that the combination of ER negative and HER2 negative has the worst prognosis [21,22]. So, for the most part our results indicate that chemotherapy is beneficial only to the more severe cases. A recent study [23] has

indicated that chemotherapy provides no benefit to subjects who are node negative, ER positive, HER2-negative, and had a midrange 21-gene recurrence score by Oncotype Dx, although some benefit of chemotherapy was found in some women 50 years of age or younger. These results are consistent with ours. The use of chemotherapy in these subjects accounts for much of the poor outcomes for subjects who did not take the model's advice to not have chemotherapy.

Nodal field radiation interacts with node status, TNEG status, and P53 status. It was found to be effective only for subjects who are node positive, TNEG yes (TNBC subtype), and P53 positive, which are the most arduous cases. On the other hand, breast-chest wall radiation, which interacts with lymph node status, P53 status, and ER status, was found to be effective for almost all subjects. It was ineffective in subject who were lymph node positive, P53 positive, and ER positive. Similarly, antihormone therapy, which interacts with menopause status, P53 status, and grade, was effective for almost all subjects. It was ineffective for pre-menopausal subjects who were P53 positive, and had grade 1 tumors. Note that ER status is not in the interaction. A separate analysis using the LSDS-5YDM showed that antihormone therapy is effective in both ER positive and ER negative subjects. Manna and Holz [24] discuss that tamoxifen may be beneficial to ER negative patients, as ER status is based on a quantitative level cut-off and not a genetic deletion or epigenetic silencing of ER. The failure to use breast-chest wall radiation and antihormone therapy accounts for much of the poor outcomes for subjects who did not take the model's advice concerning the use of these two treatments.

Neoadjuvant therapy interacts with P53 and HER2 status, and was found to be beneficial in terms of reduced metastases only for patients who were P53 negative and HER2 positive.

# Adjustment for quality of life 

We developed a DPAC system whose only consideration was to minimize the chances of 5 -year metastasis. However, chemotherapy and HER2 inhibitors have significant negative ramifications on overall health and quality of life. If chemotherapy only reduces the chances of 5 -year metastasis by $1 \%$, a given patient may prefer not to have it. Previously, we mentioned the use of QALYs. When using QALYs, a year in which the patient is in perfect health has value 1 , being dead has value 0 , and a year on some treatment that diminishes quality of life has some value between 0 and 1 . This approach does not lend itself very well to chemotherapy and HER2 inhibitors because both therapies can have negative side effects that last well beyond the time they are taken. For example, chemotherapy can cause peripheral neuropathy which can last for years, and HER2 inhibitors can cause cardiac toxicity. So, we feel a better approach is to use the standard gamble technique. When using this technique, we first carefully inform the patient of all the negative ramifications of chemotherapy. Then we ask her the following question:

Suppose with chemotherapy you have a guarantee of being metastasis free in 5 years, and without it you have a probability $p$ of being metastasis free in 5 years. What is the smallest value of $p$ for which you would forgo having chemotherapy?

We help the patient, say Mary, determine her personal value of $p$ as follows. If $p=1$, this means Mary would have to be certain she would not metastasize in 5 years to forgo chemotherapy, and therefore if chemotherapy provided any chance of decreasing 5-year metastasis, she would choose chemotherapy. It is likely that Mary would not require certainty to forgo chemotherapy. If she does not require certainty, we ask her about $\mathrm{p}=0.5$. If $p=0.5$ then Mary would forgo chemotherapy if her chance of not metastasizing without it was at least 0.5 . Mary may

![img-4.jpeg](img-4.jpeg)

Fig 7. The standard gamble when a patient is deciding whether to take chemotherapy to avoid 5-year metastasis.
https://doi.org/10.1371/journal.pone.0213292.g007
not forgo chemotherapy if she only had a 0.5 chance of not metastasizing without it. If she says 0.5 is too small to forgo chemotherapy, we ask her about $p=0.75$. Using this binary cut approach, we can continue to offer Mary values of $p$, and eventually arrive at her personal value of $p$. If it turns out that $p=0.9$ for her, then Mary is saying that she would forgo chemotherapy if her chances of not metastasizing without it were at least 0.9 .

Next we would employ the standard gamble shown in Fig 7 with $\mathrm{p}=0.9$. We have set the value of metastasizing in 5 years to 0 and the value of not metastasizing in 5 years to 1 . The value of taking chemotherapy and not metastasizing is then a value in between 0 and 1 , and we have set it to $1-x$. Mary is indifferent between the top decision to have chemotherapy and the bottom decision to not have chemotherapy and gamble with probability $p$ (where $p=0.9$ ) of not metastasizing. To determine the value of $x$, we therefore set the certain value of the outcome on the top equal to the expected value of the outcome on the bottom, and solve for $x$ as follows:

$$
\begin{aligned}
1-x & =0 \times(1-p)+1 \times p \\
& =p=0.9
\end{aligned}
$$

Solving for $x$, we obtain $x=1-0.9=0.1$. This means that having chemotherapy diminishes the utility of her outcome by 0.1 . To incorporate this into the DPAC system in Fig 6, we need only add a utility node with an edge from the chemo decision, and give that utility node value 0 if chemo is no and value -0.1 if chemo is yes. We can add such a utility node for any treatment that could have a negative effect on quality of life. Fig 8 shows the DPAC system in Fig 6 with utility nodes for chemo and HER2_inhib added.

# Discussion 

We developed DPAC, which can recommend related treatments for patients based on a composite that includes not only mutation profile but also their histopathology and clinical

![img-5.jpeg](img-5.jpeg)

Fig 8. The DPAC system in Fig 6 with utility nodes for chemo and HER2_inhib added.
https://doi.org/10.1371/journal.pone.0213292.g008
parameters. We learned from the LSDS-5YDM a DPAC system that recommends six different treatments for breast cancer patients based on their clinical profiles. In a 5-fold cross-validation analysis and in an analysis of the independent METABRIC dataset, patients who took the treatment advice of DPAC had, as a group, notably better outcomes than those that did not. So, we can conclude that DPAC is effective at amassing and analyzing data towards treatment recommendations.

Several of the results in our DPAC system are controversial. For example, DPAC says that chemotherapy can actually increase the probability of early metastasis for many node negative patients. The same is true for neoadjuvant therapy if the patient is not P53 negative and HER2 positive. Recent research has indicated that chemotherapy at suboptimal dose can induce metastatic properties [25], and neoadjuvant therapy can increases the risk of metastatic dissemination [26]. This controversy shows the importance of developing a conclusive version of DPAC, towards resolving the controversy, and making certain we provide patients with the best patient-specific treatment recommendations.

A complete DPAC system would include clinical data and genomic data such as the 21-Gene Expression Assay [23], and take into account negative side effects of treatments using QALE. Furthermore, to have confidence in the model, it needs to be learned from at least several datasets like the one we developed. This can accomplished by using a meta-analysis approach [27] when learning a DPAC system. These EHR data exist at medical facilities throughout the world. However, the databases are usually messy and unstructured. This is a common problem with 'big data'. While creating the LSDS-5YDM, we developed methods for handling such data, as described [28]. In future research we plan to develop another dataset from the University of Pittsburgh EHR datasets, and learn a DPAC system from the LSDS5YDM and that dataset together, which will test the meta-analysis approach.

Our master LSDS actually contains data on four different types of chemotherapy (alkylating agents, anthracyclines, antimetabolites, antitubulin) and three types of antihormone agents (anastrozole, tamoxifen, letrozole). Although 6726 records seems like a large number, it is barely sufficient to meet the needs of a BN-based system like we developed. So we grouped the therapies into chemotherapy and antihormone. With more extensive data, individual therapies could be included in the model with the potential for more precise decision making.

When learning from retrospective data, we must be careful of hidden common causes, which can confound the results. In the case of a DPAC system, there could be a common cause of a treatment and metastasis, which is not included in the interaction for that treatment. For, example, large tumor size could both cause the doctor to prescribe chemotherapy and lead to early metastasis, which could make chemotherapy appear to cause metastasis. As we noted earlier, we used the GES algorithm to check and make sure that no variable in the dataset was

such a common cause. However, there could be some hidden variables or group of variables, which are not in the dataset, which could affect the physician's treatment decision and affect metastasis. This could simply be the physician's subjective summary of the patient, based on years of practice. Such variables could account for why nodal therapy apparently was detrimental for most patients. Before a DPAC system could be used in practice, it should finally be evaluated in a case-control study.

As noted in the Results Section, a limitation of our study is that 5 year follow-up is considered insufficient in most cases of breast cancer. We chose to only investigate 5 year metastasis so that we could be confident that our time horizon would enable us to obtain accurate results that could verify the effectiveness of our algorithm. Too many patients left the study after 5 years. Furthermore, avoiding metastasis is the direct goal of treatments; so we investigated that goal rather than overall survival. Now that we have established that the algorithm is effective using a 5 -fold cross-validation analysis, in future research we plan to develop a more comprehensive system that looks 10 and 15 years into the future, and that predicts overall survival, which is more standardly done. We hope to compare this system to PREDICT [29], which uses similar co-variates to ours and which performs overall survival prediction.

# Author Contributions 

Conceptualization: Xia Jiang.
Data curation: Xia Jiang, Richard Neapolitan.
Formal analysis: Xia Jiang, Richard Neapolitan.
Funding acquisition: Xia Jiang, Richard Neapolitan.
Investigation: Xia Jiang, Alan Wells, Adam Brufsky, Richard Neapolitan.
Methodology: Xia Jiang.
Project administration: Xia Jiang.
Resources: Xia Jiang, Richard Neapolitan.
Software: Xia Jiang.
Supervision: Xia Jiang.
Validation: Alan Wells, Adam Brufsky, Richard Neapolitan.
Writing - original draft: Xia Jiang, Richard Neapolitan.
Writing - review \& editing: Xia Jiang, Alan Wells, Adam Brufsky, Richard Neapolitan.
