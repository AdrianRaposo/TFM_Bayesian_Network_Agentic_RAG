# NIH Public Access 

## Author Manuscript

Int J Radiat Oncol Biol Phys. Author manuscript; available in PMC 2012 March 15.
Published in final edited form as:
Int J Radiat Oncol Biol Phys. 2011 March 15; 79(4): 1089-1095. doi:10.1016/j.ijrobp.2009.12.037.

## The Role of PET in the Treatment of Occult Disease in Head and Neck Cancer: A Modeling Approach

Mark H Phillips, Ph.D. ${ }^{1}$, Wade P Smith, Ph.D. ${ }^{2}$, Upendra Parvathaneni, M.D. ${ }^{1}$, and George E Laramore, Ph.D., M.D. ${ }^{1}$<br>${ }^{1}$ Department of Radiation Oncology, University of Washington Medical Center, Box 356043, Seattle, WA 98195, USA, office phone: 206-598-6219, fax: 206-598-6218<br>${ }^{2}$ Veterans Administration, Albany, NY


#### Abstract

Purpose-To determine under what conditions PET imaging will be useful in decisions regarding the use of radiation therapy for the treatment of clinically-occult lymph node metastases in head and neck cancer.


Methods and Materials-A decision model of PET imaging and its downstream effects on radiation therapy outcomes was constructed using an influence diagram. This model included the sensitivity and specificity of PET as well as the type and stage of the primary tumor. These parameters were varied to determine the optimal strategy for imaging and therapy for different clinical situations. Maximum Expected Utility was the metric by which different actions were ranked.

Results-For primary tumors with a low probability of lymph node metastases, the sensitivity of PET should be maximized and 50 Gy should be delivered if PET is positive and 0 Gy if negative. As the probability for lymph node metastases increases, PET imaging becomes unnecessary in some situation and the optimal dose to the lymph nodes increases. The model needed to include the causes of certain health states in order to predict current clinical practice.

Conclusion-The model demonstrated the ability to reproduce expected outcomes for a range of tumors and provided recommendations for different clinical situations. The differences between the optimal policies and current clinical practice is likely due to a disparity between stated clinical decision processes and actual decision making by clinicians.

## Keywords

Bayesian network; PET; head and neck cancer; optimal policy

## 1 Introduction

When treating head and neck (H\&N) cancer, it is often necessary to decide whether or not to irradiate lymph nodes that are not clinically positive for disease but for which there is a

[^0]
[^0]:    corresponding author: Mark Phillips, markp@u.washington.edu.
    Conflicts of Interest Statement
    No actual or potential conflicts of interest of interest exist for any of the authors of this article.
    Publisher's Disclaimer: This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final citable form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

finite probability that occult disease is present. Positron emission tomography (PET) has been suggested as an additional test that can be performed that would reduce the uncertainty by positively identifying disease and/or by ruling out tumor in suspected nodes [1,2]. However, its potential is limited by its inability to discriminate against false positives due to inflammation and false negatives when the tumor is very small. Such limitations imply a need to determine the optimal sensitivity and specificity of the test.

The decision to be made after the test is whether or not to irradiate a given lymph node and, if so, to what dose. Typically, if a lymph node is suspected but not proven of harboring disease, it is irradiated to 50 Gy ; if positive, then 66 Gy is often given [3,4]. The tradeoff to be considered is between controlling the tumor and causing complications. The decision is not made any easier given the uncertain nature of the outcomes and the necessity of dealing with probabilities among a range of possible results.

We have built a model of the radiation therapy process for this clinical situation that incorporates the impact that PET imaging has on establishing the presence of disease, and then ultimately on the critical outcomes of tumor eradication and normal tissue sparing. The probabilistic nature of the processes is captured by means of an influence diagram which uses maximum expected utility as the ultimate metric in the decision making process.

# 2 Methods 

### 2.1 Current practice

Current radiotherapy practice for the treatment of regional lymph nodes in $\mathrm{H} \& \mathrm{~N}$ cancer relies on surgical series such as described in Lindberg [5], and we have used these tumor data and probabilities for clinically-occult nodal disease. In the absence of other information, a node is not irradiated if the probability of having occult nodal disease (denoted as $P(D+)$ ) is less than approximately $10-25 \%$. If $P(D+)$ is greater than this subjective threshold, then a dose lower than that used for the primary is delivered, typically 50 Gy . If accurate information regarding the node disease state, e.g. positive CT or biopsy findings, is available, a larger, tumorcidal dose is delivered, typically $60-66 \mathrm{~Gy}$. In addition, we have made the assumptions that there are no contraindications for curative therapy, there is no distant metastatic disease, the patient has had no prior radiotherapy or surgery to the region and the patient has refused all surgery.

Three tumors were selected for investigation based on the range of probabilities of lymph node disease being present (see Table 1): (1) oral tongue, T1N0M0, (2) soft palate, T2N0M0, and (3) nasopharynx, T1N0M0.

### 2.2 PET test

The data characterizing the PET imaging were obtained from the paper by Murakami et al [6] which compared the PET results with surgical examination. We fit two Gaussians to the SUV values of the small positive and negative nodes ( $<1.0 \mathrm{~cm}$ in diameter). We then constructed the receiver-operator curve (ROC) from these curves (Figure 1). Given the inaccuracy of reading the data from the figure and the curve-fitting process, our values for the sensitivity and specificity are not meant to be the definitive representation of their data. Instead, the process provided a means for obtaining a realistic characterization of the PET test that is suitable for our modelling given the wide range of test accuracies reported in the literature. Three different operating points on the ROC curve were used which represented the range of combinations of sensitivity and specificity: $[0.976,0.157],[0.745,0.783]$, and $[0.371,0.983]$.

# 2.3 Influence Diagram 

An influence diagram is a Bayesian network with additional nodes representing decisions and utilities [7,8,9,10]. Decision trees can represent the same model, but the complexity of the graph renders any but the most simple nearly intractable to use. Figure 2 illustrates the relatively simple diagram that was constructed to model the radiation therapy process. Elliptical nodes represent variables characterized by a set of discrete states. Arrows from parent to child nodes denote causal connections and are characterized by conditional probability tables (CPT). As described above, the states of the node Primary_Site are the regions described by Lindberg and the CPT of LN_disease is derived from the same paper. Most of the nodes are described by binary states, e.g. the states of Local_Control are Yes/No. The conditional probabilities used in the influence diagram were obtained from the literature and expert opinion determined via interviews with radiation oncologists specializing in the treatment of $\mathrm{H} \& \mathrm{~N}$ cancer.

The probabilities for the occurence of any given state within a node are either known $a$ priori or conditioned on the probabilities of the parents' states. For example, the node LN_disease represents the probability that a lymph node contains disease given the primary tumor and stage of disease, denoted as $P(L N \_$disease $\mid$ PrimarySite, Stage). Whether or not the PET signal is positive depends on the state of LN_disease, the probability of which is $P($ PET=positive $\mid L N \_$Disease $)$. The conditional probability table for this state includes the sensitivity and specificity of the PET test obtained from Murakami et al. However, we wish to know the probability of lymph node disease given the result of the PET study, $P(L N \_$disease $\mid P E T)$, which is calculated by the Bayesian network using Bayes' theorem.

Possible actions are contained in the decision node, LN_irradiation. The possible actions, $A$, are denoted by the set of doses that can be delivered: $\{0 G y, 50 G y, 66 G y\}$. The values 50 and 66 Gy are chosen to represent the ranges of lower and higher doses and it is acknowledged that current clinical practice encompasses a range of doses.

The utility node is described by a table of the values, known as utilities, for each of the outcomes. Utility is the quantitative measure of the strength of preference for an outcome [11]. The utilities range from 1.0 for the best possible outcome state to 0 for death. In this case, the outcomes are the four combinations of the binary parent states as represented in Figure 2. For this relatively simple situation, we set the two extremes, i.e.
$U($ RegionalControl=yes, Complications $=n o)=1$ and
$U($ RegionalControl=no,Complications=yes $)=0.1$. A utility of 0.0 is usually reserved for the outcome of death. The utilities of the other two states are less easily determined. For the outcome of no regional control and no complications, we set the utility to 0.33 . For the outcome of regional control plus complications, we varied the utility from 0.4 to 0.67 (see Section 2.4). For a more complete discussion of this method of setting utilities, see Ref. [12].

The value of the utility node is the Expected Utility, which is the sum of the products of the probability for each state as obtained from the Bayesian network and the utility corresponding to each state. The optimal action is one which leads to the maximum expected utility given the uncertainties and values that are used in the model.

Complications were modelled as arising directly from the radiation and/or from recurrent disease which would result in a similar health state. Complication probabilities were taken from Mendenhall et al [13]. The probability of controlling lymph node disease depends on the size of the node and amount of tumor present. In this study, since the nodes are by definition small, the probability of controlling lymph node disease, Regional_Control, is

relatively high ( $70 \%$ for $50 \mathrm{~Gy}, 90 \%$ for 66 Gy ). The node Primary_Control is the probability of controlling the primary disease.

# 2.4 Testing the model 

We focused on three particular tumors because they represent a broad spectrum of probabilities for lymph node involvement: stage I oral tongue [ $P(L N \_$disease $)=0.14]$, stage II soft palate $[P(L N \_$disease $)=0.365]$, and stage I nasopharyngeal cancer [ $P(L N \_$disease $)=0.925]$. We also varied several of the probabilities and utilities in three separate versions of the model in order to explore some of the key assumptions. Version 1 contained the best available data and consensus among experts. In Version 2, the utility of the outcome of local control plus complication was varied from 0.67 to 0.4 to reflect different attitudes towards the effects of complications. In Version 3, the cure rate of the lymph node disease was varied from 0.7 to 0.3 for 50 Gy and 0.9 to 0.4 for 66 Gy . The purpose was to explore the model output for a significantly different clinical situation, such as the treatment of recurrent disease [14,15]. We also compared the model results with expert opinion with respect to the actions that should be taken.

## Version 1, original

$U($ RegionalControl=yes, Complications=yes $)=0.67$
$\mathrm{P}($ RegionalControl=yes $|\mathrm{LN} \_$irradiation $=50 \mathrm{~Gy})=0.7$
$\mathrm{P}($ RegionalControl=yes $|\mathrm{LN} \_$irradiation $=66 \mathrm{~Gy})=0.9$

## Version 2, reduced utility model

$U($ RegionalControl=yes, Complications=yes $)=0.40$
$\mathrm{P}($ RegionalControl=yes $|\mathrm{LN} \_$irradiation $=50 \mathrm{~Gy})=0.7$
$\mathrm{P}($ RegionalControl=yes $|\mathrm{LN} \_$irradiation $=66 \mathrm{~Gy})=0.9$

## Version 3, reduced control probability model

$U($ RegionalControl=yes, Complications=yes $)=0.40$
$\mathrm{P}($ RegionalControl=yes $|\mathrm{LN} \_$irradiation $=50 \mathrm{~Gy})=0.3$
$\mathrm{P}($ RegionalControl=yes $|\mathrm{LN} \_$irradiation $=66 \mathrm{~Gy})=0.4$

## 3 Results

Table 1 shows the probabilities that the lymph node actually has disease given the outcome of the PET test. The results are tabulated for each tumor type and for both outcomes of the test (PET+ or PET-). Also shown are the a priori probabilities for lymph node involvement obtained from Lindberg et al [5]. This table illustrates the increase in information available from the PET test for different settings of the sensitivity and specificity.

Table 2 presents the expected utility values of Version 1 calculated for: (a) each tumor site, (b) the three selected operating points, (c) the three possible therapeutic actions, and (d) the three possible imaging results (no PET test, PET positive, PET negative). The decrease in expected utilities as the sensitivity of the PET test decreases reflects the fact that not treating a positive lymph node outweighs the benefit of avoiding complications. This trend holds

even for Version 2 which penalizes complications more than Version 1, though the differences as a function of sensitivity are smaller.

In the absence of PET information, Version 1 suggests that the optimal policy for oral tongue cancer is delivering 50 Gy , rather than the conventional choice of no radiation. For the other two cancers, 66 Gy is preferred to 50 Gy when PET information is not available. This compares to our expert opinion of 0,50 and 50 Gy for the three tumor types, respectively. Version 2 gives the optimal doses of 50, 50 and 66 Gy , and Version 3 gives 0 , 50 , and 66 Gy .

In order to examine the model predictions without the uncertainty of the state of the lymph nodes, we entered evidence for either positive lymph nodes ( $\mathrm{LN}+$ ) or negative nodes ( $\mathrm{LN}-$ ). Table 3 presents the utilities for each version of the model (labeled M1, M2 and M3, respectively) for each possible therapeutic action. The differences in utilities for all models is very pronounced for the state $\mathrm{LN}+$ and between the action $A=0 \mathrm{~Gy}$ and any other action, reflecting the large cost associated with not irradiating positive disease. There is also a marked increase in utility for any of the models between $\mathrm{LN}+$ and $\mathrm{LN}-$ since having the disease is always worse than not. The dose response of the utility for $\mathrm{LN}-$ is smaller than for $\mathrm{LN}+$ reflecting the poor utility values for lack of cure. Version 3 has significantly lower utilities for the actions $A=50 \mathrm{~Gy}$ or 66 Gy because of the reduced probability of cure given radiation in this version of the model. While the reduced utility for the state \{Control, Complications $\}$ in Versions 2 and 3 results in lower expected utilities for treating false positives ( $\mathrm{LN}-$ ), it is a relatively small change because of the probabilities of each of the contributing states.

Table 4 presents the optimal policies for the imaging and for the subsequent radiation. Included in this is the default policy of omitting the PET study and making the decision of whether to irradiate or not based on other clinical information as described above. If the optimal action did not differ between the PET positive results and the negative results, then the PET test added no useful information and should not be performed. The table also presents the preferred decisions of the physicians, who felt that while the PET test was not considered conclusive, on average it did contain useful information.

Inspection of the optimal policies highlights the fact that none of the versions of the model represented by Figure 2 recommends the current clinical policy of no irradiation for the oral tongue tumor and 50 Gy for the other two tumor types. Such a policy was obtained by a modified model (Figure 3) in which the connection between the nodes Local/Regional Disease and Complications was removed and a node was added to model the fact that irradiation can cause the same health states through direct causation of normal tissue complications or through failure to control the disease. The utility node then had three inputs: radiation complications, recurrence complications, and tumor control. A low utility for radiation-induced complications relative to a higher utility for recurrence-caused complications reproduced the current clinical practice.

The major conclusion is that given the probabilities and utilities of the models then if the PET study is to be done, the most sensitive operating point is optimal. Primarily this reflects the valuation of the outcome $\{$ Control,Complications $\}$ as greater than the outcome \{NoControl,NoComplication\}. A second factor is that the cure probability for lymph node disease is significantly higher than the complication probabilities. The combination of these two factors rewards an aggressive approach with a small downside for overtreating patients with false positive PET results.

# 4 Discussion 

The current policy for treating occult disease in the lymph nodes is to base the decision to irradiate on the probability of lymph node involvement [16]. This probability, obtained from surgical series for the most part, depends on the type and stage of the primary H\&N tumor and patients are categorized as high or low risk. Those who are in the high risk category are treated; those in the low risk category are not. This policy will inevitably treat some nodenegative patients in the high risk category and will miss treating some node-positive patients in the low risk category. To be effective, the role of PET imaging is to better identify whether the patient is $\mathrm{LN}+$ or $\mathrm{LN}-$. In the best case, if the PET test were perfect, then one need not make a decision under uncertainty (even though the ultimate outcome of the therapy would still be uncertain).

However, PET imaging is not infallible in identifying disease in the lymph nodes, particularly in the case of interest in which the tumor burden (if present) is small enough that other clinical tests fail to detect it. There will be a range of PET intensity values for every patient and between patients, and the same value of the PET signal may by a measure of tumor in one patient but not another. The selection of the ideal operating point of the test is a decision theoretical problem that we approached using a model of outcomes.

The model we built using an influence diagram was an effort to predict the consequences of the decision based on a PET test using a particular operating point. By setting values of variables in the model, e.g. the type and stage of tumor and the operating point of the PET test, we were able to calculate both the probabilities of the outcomes and the expected utilities under different sets of conditions. We were also able to model different but related situations. For example, PET can also be used to identify regions of recurrent disease which have a lower probability of control with radiation (Version 3). A more complete model would include information regarding the number of FDG molecules sequestered in tumor cells versus other cells and the physics of the PET detector system.

The inability of the models represented by the graph of Figure 2 to recommend the current clinical practice has important implications. It could mean that the model structure is incorrect. It could also stem from the inaccuracy of the CPT's (note that the current practice policy could not be reproduced by any reasonable alteration of the utilities). Since the probabilities are not highly speculative, it is more likely that the structure of the model is the source, and this did prove to be the case. The current clinical decision model was reproduced by modifying the original influence diagram to separately consider the utilities of causing the same ultimate health state via two different pathways: radiation-induced and uncontrolled disease-induced (Figure 3). Such a structure is at odds with the information gathered through interviews with experts and may reflect an unconscious bias against being the cause of the poor health state, rather than by being unable to prevent it.

Inspection of the model raises the question as to why the nodes Primary control and Local/ Regional Disease are present since all patients are treated similarly for the primary regardless of the PET test. First, the model shown is a simplified portion of a more complete model [17]. Second, these nodes allow for other endpoints such as quality adjusted life expectancy. Using these outcomes metrics, the utilities of the complication outcomes are likely to be dependent on such critical factors as life expectancy.

The use of utilities is directly linked to the fact that choosing an optimal operating point is a decision, and as such, a set of values with which to rate or rank the possible outcomes is needed [16]. There are a number of different metrics one can use, such as survival or the occurence of a particular complication. Utility was chosen because of the mixed nature of the outcome (tumor control and normal tissue complication) and because there are many

different complications that might come into play. It is also a more general metric, thereby making it easier to apply the model to different types or sites of tumor. The use of utilities is common in many types of health care decision environments and is also being applied to oncology $[18,19,20,21,22]$.

Models are useful tools, particularly in medicine, since one of their primary functions is to predict outcomes. A popular method of forming models is through machine learning in which data is mined for correlations between variables. Such models are very useful but are limited since the structure of the model need not be informed by a foundation of scientific understanding but reflects correlations between variables. This reduces the model's application when new circumstances arise. A robust model will be able to account for missing information as well as to incorporate new data to provide insight into the development of the system.

The use of PET to determine the presence or absence of metastatic disease is not yet resolved due to several limitations with this imaging modality. Our study focused on tumors that were too small to be detected with conventional imaging and clinical methods. By constructing a probabilistic model of the possible outcomes of using the PET imaging information, we were able to determine optimal policies for the subsequent radiation therapy as shown in Table 4. We were also able to determine the optimal characteristics of the PET imaging. Finally, in the process of constructing our model, we determined that therapeutic decisions depend not only on the final health state outcome but also on the factors involved in that outcome, namely the radiation therapy or recurrent disease.

# Acknowledgments 

This work was partially supported by NIH R01 CA-112505. Dr. Mary Austin-Seymour also contributed significant time and expertise in the evolution of this work.

# NIH-PA Author Manuscript

## NIH-PA Author Manuscript

### Table 3

**Utilities for each possible action given either positive or negative lymph nodes**


*Int J Radiat Oncol Biol Phys.* Author manuscript; available in PMC 2012 March 15.

# Table 4 

Optimal policies under the assumptions of three different model versions and physician judgment


The two policies had nearly identical expected utilities