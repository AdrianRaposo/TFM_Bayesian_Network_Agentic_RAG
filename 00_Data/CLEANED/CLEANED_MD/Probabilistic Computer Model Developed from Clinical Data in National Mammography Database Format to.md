Note: This copy is for your personal, non-commercial use only. To order presentation-ready copies for distribution to your colleagues or clients, use the Radiology Reprints form at the end of this article.

Elizabeth S. Burnside, MD, MPH, MS Jesse Davis, PhD ${ }^{a}$<br>Jagpreet Chhatwal, PhD<br>Oguzhan Alagoz, PhD<br>Mary J. Lindstrom, PhD<br>Berta M. Geller, EdD<br>Benjamin Littenberg, MD<br>Katherine A. Shaffer, MD<br>Charles E. Kahn, Jr, MD, MS<br>C. David Page, PhD

[^0]
## Probabilistic Computer Model Developed from Clinical Data in National Mammography Database Format to Classify Mammographic Findings ${ }^{1}$

Purpose:

Materials and Methods:

To determine whether a Bayesian network trained on a large database of patient demographic risk factors and radiologist-observed findings from consecutive clinical mammography examinations can exceed radiologist performance in the classification of mammographic findings as benign or malignant.

The institutional review board exempted this HIPAA-compliant retrospective study from requiring informed consent. Structured reports from 48744 consecutive pooled screening and diagnostic mammography examinations in 18269 patients from April 5, 1999 to February 9, 2004 were collected. Mammographic findings were matched with a state cancer registry, which served as the reference standard. By using 10 -fold cross validation, the Bayesian network was tested and trained to estimate breast cancer risk by using demographic risk factors (age, family and personal history of breast cancer, and use of hormone replacement therapy) and mammographic findings recorded in the Breast Imaging Reporting and Data System lexicon. The performance of radiologists compared with the Bayesian network was evaluated by using area under the receiver operating characteristic curve (AUC), sensitivity, and specificity.

The Bayesian network significantly exceeded the performance of interpreting radiologists in terms of AUC ( 0.960 vs $0.939, P=.002$ ), sensitivity ( $90.0 \%$ vs $85.3 \%, P<$ .001), and specificity ( $93.0 \%$ vs $88.1 \%, P<.001$ ).

On the basis of prospectively collected variables, the evaluated Bayesian network can predict the probability of breast cancer and exceed interpreting radiologist performance. Bayesian networks may help radiologists improve mammographic interpretation.
(c) RSNA, 2009

Supplemental material: http://radiology.rsnajnls.org/cgi /content/full/2513081346/DC1


[^0]:    ${ }^{1}$ From the Department of Radiology, University of Wisconsin School of Medicine and Public Health, E3/311 Clinical Science Center, 600 Highland Ave, Madison, WI 53792-3252 (E.S.B.); Department of Biostatistics and Medical Informatics (E.S.B., J.D., M.J.L., C.D.P.) and Department of Industrial and Systems Engineering (D.A.), University of Wisconsin, Madison, Wis; Department of Health Economic Statistics, Merck Research Laboratories, North Wales, Pa (J.C.); Departments of Family Medicine and Radiology (B.M.G.), and Departments of Medicine and Nursing (B.L.), University of Vermont, Burlington, Vt; and Department of Radiology, Medical College of Wisconsin, Milwaukee, Wis (K.A.S., C.E.K.). Received August 1, 2008; revision requested September 8; revision received December 11; accepted December 23; final version accepted January 12, 2009. Address correspondence to E.S.B. (e-mail: eburnside@uwhealth.org).
    ${ }^{2}$ Current address: Department of Computer Science and Engineering, University of Washington, Seattle, Wash.

The millions of mammographic examinations performed yearly in the United States (1) present interpretive and decision-making challenges that will result in substantial performance variability among radiologists and, therefore, suboptimal sensitivity and specificity (2). Practice differences between the United States and the United Kingdom suggest that high abnormal interpretation and biopsy rates may not translate into superior cancer detection (3). Such variability of practice presents an opportunity to develop decision support tools to aid radiologists in improving performance.

Errors can occur at several points in the pursuit of early breast cancer diagnosis. Findings must be detected on the mammogram, characterized in terms of relevant and predictive features, classified into disease categories, and, finally, applied to the patient so that appropriate treatment can be instituted. Errors are frequently made when estimating breast cancer risk before and after a mammographic examination because physicians must make complex judgments involving multiple variables (4). Although clinical information increases the accuracy of diagnostic tests (5-7) and providing patientspecific probability estimates can help lessexperienced physicians improve to the level of experts (8), probability estimation is among the most error-prone components of clinical judgment $(9,10)$.

Bayesian networks identify variables that influence the probability of an outcome of interest (like breast cancer) and apply the sequential Bayes formula for each variable to aid in risk predic-

## Advances in Knowledge

- A Bayesian network computer model that uses Breast Imaging Reporting and Data System descriptors can accurately predict the probability of malignancy of a finding at mammography.
- A Bayesian network achieved a superior area under the receiver operating characteristic curve compared with the interpreting radiologist for consecutive mammographic findings.
tion. We developed a Bayesian network to calculate the risk of malignancy on the basis of demographic risk factors (age, cancer history, and use of hormone replacement therapy) collected by the technologist and imaging features catalogued by the radiologist using the Breast Imaging Reporting and Data System (BI-RADS) lexicon.

Our work builds on computer-assisted detection experience by addressing challenges identified in recent literature. Although results of evaluation of com-puter-assisted detection performance on the basis of nonconsecutive samples (11-16) and carefully controlled prospective assessment in clinical practice (17-21) have been promising, retrospective evaluation of actual clinical performance has demonstrated disappointing results $(22,23)$. In fact, it has been suggested that the suboptimal performance indicates that computer-assisted detection may have unanticipated negative effects on radiologist decision making, perhaps by deferring recall when marks are not present $(22,23)$. Several groups have improved classification of mammographic abnormalities (computerassisted diagnosis) with computer-extracted imaging features (24-26) or with radiologist-observed features (2731) in selected biopsy cases. We aim to extend this research by developing a Bayesian network that uses radiologistobserved features found in the American College of Radiology National Mammography Database (NMD) format $(32,33)$. Our purpose is to determine whether a Bayesian network trained on a large database of patient demographic risk factors and radiologist-observed findings from consecutive clinical mammographic examinations can exceed radiologist performance in the classification of mammographic findings as benign or malignant.

## Implication for Patient Care

- Bayesian networks may help radiologists improve mammographic interpretation.


## Materials and Methods

The institutional review board of the Froedtert and Medical College of Wisconsin exempted this Health Insurance Portability and Accountability Act-compliant retrospective study from requiring informed consent.

## The Model

In general, a Bayesian network represents variables as "nodes," which are data structures that contain an enumeration of possible values ("states") and store probabilities associated with each state (Fig 1). For instance, the "root" node, entitled "breast disease," has two states that represent the outcome of in-terest-benign or malignant-and stores the prior probability of these states (the prevalence of malignancy). The remaining nodes in the network represent demographic risk factors, BI-RADS descriptors, and the ultimate BI-RADS category (Table 1). Directed arcs in the Bayesian network encode dependence relationships among variables.

There are two approaches to building a Bayesian network: (a) Use preexisting knowledge about the probabilistic relationships among variables or (b) learn the probabilities and/or the structure from

Published online before print
10.1148/radiol. 2513081346

Radiology 2009; 251:663-672

## Abbreviations:

AUC $=$ area under the ROC curve
BI-RADS $=$ Breast Imaging Reporting and Data System
NMD $=$ National Mammography Database
ROC $=$ receiver operating characteristic
Author contributions:
Guarantors of integrity of entire study, E.S.B., C.D.P.; study concepts/study design or data acquisition or data analysis/interpretation, all authors; manuscript drafting or manuscript revision for important intellectual content, all authors; manuscript final version approval, all authors; literature research, E.S.B., J.C., O.A., C.E.K., C.D.P.; clinical studies, E.S.B.; experimental studies, E.S.B., J.D., C.E.K., C.D.P.; statistical analysis, E.S.B., J.D., J.C., M.J.L., B.L., C.D.P.; and manuscript editing, all authors Funding:
This work was supported by the National Institutes of Health (grants K07-CA114181, R01-CA127379, and R21CA129393).

Authors stated no financial relationship to disclose.

large existing data sets. In the past, investigators have typically used the former approach $(30,31,34,35)$. In our study, we employed the latter approach (29) and trained the Bayesian network on existing clinical mammography findings. Our training process entailed determining the probabilities within each node, as well as discovering which arcs connected these nodes to capture dependence relationships. Once trained, the Bayesian network calculated a posttest probability of malignancy for each mammographic finding by using the structure and probabilities gleaned from the data.

The Bayesian network was trained by using an algorithm called tree augmented naive Bayes (36). The tree augmented naive Bayes algorithm produces the maximum likelihood structure given the constraint that each node can have at most one dependent node in addition to the root node. To train and test the Bayesian network model, we used a standard machine learning technique called 10 -fold cross validation (Appendix E1, http://radiology.rsnajnls.org/cgi /content/full/2513081346/DC1). We observed the time required for Bayesian network inference as we estimated probabilities for each finding in order to consider the possible clinical implications of model use.

## Study Design

We collected data for all screening and diagnostic mammography findings observed at the Froedtert and Medical College of Wisconsin Breast Care Center between April 5, 1999 and February 9, 2004. This clinical practice did not separate screening and diagnostic examinations during the time of our study, which prevents separate analysis of screening and diagnostic examinations. Therefore, we analyzed practice performance parameters for diagnostic and screening studies in aggregate (37).

The database held 48744 mammographic examinations performed in 18269 patients. All mammographic findings were described and recorded by using BI-RADS by the interpreting radiologist at the time of mammographic interpretation by using the structured reporting software (Mammography Information System,
versions 3.4.99-4.1.22; PenRad, Minnetonka, Minn) routinely used in this practice.

There was a total of eight radiologists (including K.A.S.)-four of whom were general radiologists with some background in mammography, two of whom were fellowship trained, and two of whom had lengthy experience in breast imaging. Radiologist experience in mammographic interpretation ranged between 1 and 35 years (by the end of the study period). All radiologists were Mammography Quality Standards Act of 1992 certified. We obtained information regarding the reading radiologist by merging the PenRad data with the radiology information system (RIS) at the Medical College of Wisconsin. Five hundred four findings could not be assigned to a radiologist during our PenRad-RIS matching procedure. We elected to include unassigned
findings in our analysis to maintain the consecutive nature of our data set.

We included all mammographic examinations, whether results were positive or negative. A negative mammogram was recorded as a single record with demographic data and BI-RADS assessment category populated but with finding descriptors left blank (because no finding was present). The term "finding" will be used throughout to denote the single record for normal mammograms or each record denoting an abnormality on a mammogram. The term "mammographic examination" will be used when we are referring to the entire mammographic study, including all views. The PenRad system records patient demographic risk factors, mammographic findings, and pathologic findings from biopsy in a structured format (ie, point-and-click entry of information populates the clinical report and the database simulta-

Figure 1
![img-0.jpeg](img-0.jpeg)

Figure 1: Structure of the trained Bayesian network. Labeled circles represent nodes, and arrows (arcs) represent dependence relationships. $C a^{++}=$calcifications, $F H x=$family history of breast cancer, $h / o=$ history of, $H R T=$ hormone replacement therapy.

neously). The radiologist can also add details to the report by typing in free text, but these details are not captured in the database. We consolidated our database in the NMD format $(32,38)$. Although the NMD format contains more than 100 variables, we included only those that were routinely collected in the practice and that were predictive of breast cancer (Table 1).

Classification accuracy was analyzed at
the level of findings. Because image-based breast cancer classification (ultimately resulting in a biopsy recommendation) occurs primarily at the finding level, we believe this level of analysis is necessary to improve performance. However, the conventional analysis of mammographic data is at the level of the mammographic examination (where findings from a single study are combined). Because prior literature uses


analysis at the mammogram level, we also did so for comparison (synthesizing the findings to the mammogram level by using the BI-RADS category of the most suspicious finding-where category $5>4>0>$ $3>2>1$-as in routine clinical practice). Specifically, we calculated the cancer detection rate, the early stage cancer detection rate, and the abnormal interpretation rate for all mammograms in our data set.

We matched the mammographic data with state cancer registry data as the reference standard. The Wisconsin Cancer Reporting System (WCRS), the state's population-based registry for cancer incidence data, has been collecting information from hospitals, clinics, and physicians since 1978. This registry collaborates with several other state and federal agencies to collect the standardized North American Association of Central Cancer Registries data elements, including demographic information, tumor characteristics, and treatment and mortality (39). Details of the data elements provided by the WCRS and our matching procedures are included in Appendix E2 (http://radiology .rsnajnls.org/cgi/content/full/2513081346 /DC1). Because we were matching mammographic findings with cancers, the fact that the registry collects "subsite" (cancer location) information was extremely important (Appendix E2 and Table E1, http://radiology.rsnajnls.org /cgi/content/full/2513081346/DC1). The cancer registry achieves high rates of collection accuracy because it is supported by state law, which mandates reporting of all cancers by hospitals and physicians. The WCRS checks the accuracy of incoming cancer data by using nationally approved protocols, and any inconsistencies or errors are resolved with the reporting facility (39). We considered a registry report of ductal carcinoma in situ or any invasive carcinoma as positive. All other findings shown to be benign with biopsy or without a registry match within 365 days after the mammogram were considered negative.

## Statistical Analysis

Using BI-RADS categories as ordinal response variables to reflect the increasing likelihood of breast cancer (where

BI-RADS category $1<2<3<0<4<$ 5) (40), we generated receiver operating characteristic (ROC) curves for all radiologists individually and in aggregate. Using the probabilities generated for all findings by means of 10 -fold cross validation, we constructed ROC curves for the Bayesian network by calculating sensitivity and specificity using each of the possible predicted probabilities of malignancy as the threshold value for predicting malignancy. We calculated and compared areas under the ROC curves (AUCs) and generated confidence intervals by using the DeLong method (41).

We calculated baseline sensitivity and specificity of the radiologists (in aggregate and individually) at the operating point of BI-RADS category 3 (with BI-RADS category 3 considered negative) because above this level, biopsy would be recommended. We then calculated the Bayesian network sensitivity at the baseline specificity of the radiologists and the Bayesian network specificity at the baseline sensitivity of the radiologist. We compared sensitivity and specificity (between radiologists and the Bayesian network) by using the McNemar test to account for the lack of independence between the sensitivity and specificity ratios. The McNemar test is not defined when the ratios are equal, nor when one of the ratios is 0 or 1 . We generated confidence intervals for sensitivity and specificity by using the Wilson method (42). We consistently considered BI-RADS categories 0,4 , and 5 as positive and BI-RADS categories 1, 2 , and 3 as negative.

To understand whether the Bayesian network affected biopsy rates, recall, or fol-low-up recommendations, we evaluated multiple probability thresholds ( $0.05 \%$, $0.1 \%, 0.5 \%, 1.0 \%, 2.0 \%, 3.0 \%, 4.0 \%$, and $5.0 \%$ ) within BI-RADS categories. In addition, we selectively reviewed the collected variables of breast cancers missed at multiple threshold levels to try to explain why risk prediction failed in these cases.

## Results

After matching to the cancer registry, there were 62219 findings ( 510 malignant, 61709 benign) in 48744 women and 398 men for analysis. The mean age

Figure 2
![img-1.jpeg](img-1.jpeg)

Figure 2: ROC curves constructed from the BI-RADS categories of the radiologists and the predicted probabilities of the Bayesian network. The radiologists' operating point is considered the BI-RADS category 3 point, corresponding to a threshold above which biopsy would be recommended. $\Delta T N=$ change in trueregatives (which results in improved specificity), $\Delta T P=$ change in true-positives (which results in improved sensitivity), Tan = tree augmented naive Bayes algorithm.
of the female patient population was 56.5 years $\pm 12.7$ (standard deviation) (range, 17.7-99.1 years), while the mean age of the male patient population was 58.5 years $\pm 15.7$ (range, 18.6 88.5 years). Fourteen percent of findings were in predominantly fatty tissue, $41 \%$ were in scattered fibroglandular tissue, $36 \%$ were in heterogeneously dense tissue, and $8 \%$ were in extremely dense tissue. The cancers included 246 masses, 121 microcalcifications, 27 asymmetries, 18 architectural distortions, 86 combinations of findings, and 12 findings categorized as "other."

Using analysis on the mammography level, the radiologists detected 8.9 cancers per 1000 mammograms ( 432 cancers per 48744 mammograms). The abnormal interpretation rate (considering BI-RADS categories 0,4 , and 5 as abnormal) was $18.5 \%$ ( 9037 of 48744 mammograms). Of all 432 detected cancers, 390 had staging information from the cancer registry and 42 did not. Of the cases with stage available, $71.0 \%$ (277 of 390 ) were early stage
(stage 0 or 1 ), and $26.7 \%$ (104 of 390 ) had lymph node metastasis.

The tree augmented naive Bayes algorithm identified many predictive variables that were dependent on one another. Each dependence relationship in the Bayesian network is demonstrated by a directed arc (Fig 1).

At the finding level, the Bayesian network provided a significant improvement in AUC compared with the interpreting radiologists ( 0.960 vs 0.939 , $P=.002$ ). The ROC curve for the Bayesian network surpassed that of the radiologists at all threshold levels (Fig 2). The Bayesian network demonstrated superior AUC performance as compared with three radiologists, including the two readers with the highest volumes (Table 2). Hence, the Bayesian network significantly improved on radiologists' specificity ( $93.0 \%$ vs $88.1 \%, P<.001$ ) at a sensitivity of $85.3 \%$ and radiologists' sensitivity ( $90.0 \%$ vs $85.3 \%, P<.001$ ) at a specificity of $88.1 \%$ (Table 3 ). The Bayesian network was also superior to the two highvolume readers in terms of sensitivity and

specificity. The Bayesian network exceeded several low-volume readers in specificity. Only one low-volume radiologist (radiologist 1 in Table 3) exceeded the Bayesian network in specificity. The time required for Bayesian network inference per finding was consistently less than 1 second.

By dividing findings into BI-RADS categories (with multiple threshold levels at which to determine positive or
negative), we demonstrated a trade-off between cases correctly classified versus erroneously classified by the Bayesian network at each threshold level (Table 4). For positive studies (BIRADS categories 0,4 , and 5), conversions from false-positive to true-negative dominated other conversions, particularly at higher threshold levels, which explains how the Bayesian net-
work improved overall specificity. For negative findings (BI-RADS categories 2 and 3), conversions from false-negatives to true-positives were most notable at lower threshold levels, which explains how the Bayesian network improved sensitivity. Overall, a reduction of misclassification in BI-RADS category 0 assessments dominated the results when all threshold levels were consid-

Table 2
Comparison of Radiologist and Bayesian Network AUCs


Note. -ND $=$ not defined.

* Data in parentheses are $95 \%$ confidence intervals.
${ }^{1}$ Calculated with DeLong test of difference between two dependent AUCs.
${ }^{2}$ Unassigned mammographic studies resulting from inability to match studies with radiologists when merging mammography reporting system and institutional radiology information system.

Table 3
Comparison of Radiologist and Bayesian Network Sensitivity and Specificity


Note. -ND $=$ not defined.

* Data in parentheses are $95 \%$ confidence intervals.
${ }^{1}$ At a radiologist specificity of $88.1 \%$.
${ }^{2}$ Calculated with McNemar test.
${ }^{3}$ At a radiologist sensitivity of $85.3 \%$.
${ }^{1}$ Unassigned mammographic studies resulting from inability to match studies with radiologists when merging mammography reporting system and institutional radiology information system.

Table 4
Performance within BI-RADS Categories as Function of Probability Threshold


ered. At review of the reports that represented consistently missed breast cancers, predictive BI-RADS terms in the text reports were not contained in the structured reports used by the Bayesian network.

## Discussion

We demonstrate that our Bayesian network can use a database of prospectively collected findings at mammography to calculate an accurate risk of malignancy and improve on radiologist performance measures in the classification of benign and malignant breast disease. Our results show significantly superior Bayesian network performance in terms of AUC, sensitivity, and specificity compared with all radiologists in aggregate. When individual radiologist performance was compared with the Bayesian network for the same findings, the Bayesian network showed superior performance in AUC, sensitivity, and specificity versus the two highest-volume readers and superior specificity versus all but two radiologists. Only one radiologist significantly outperformed the Bayesian network in specificity (but not in sensitivity or AUC).

The radiologist and the Bayesian network each provides a valuable component to the final risk prediction that contributes to improved performance. Specifically, the radiologist provides observations and assessments that the Bayesian network combines in a mathematically rigorous manner with "knowledge" of similar past findings to generate accurate predictions. Ideally, the radiologist and the Bayesian network would be able to work together, in real time, to catalogue the features that are most important for a given finding and optimize the predictions in the appropriate clinical context. Our retrospective analysis is a somewhat artificial judge of the potential of Bayesian risk prediction but should be viewed as a first step. The comparison between the Bayesian network and the radiologist is also imperfect because the radiologist is performing a highly complex task-beyond simply classifying findings as benign or malignant-while the Bayesian network has been trained specifically for that task alone. Therefore, our comparison certainly does not imply that the Bayesian network could replace the radiologist but may indicate that the Bayesian network can calculate risk
across many variables, incorporate complex dependencies among variables, and aid the radiologists' interpretations. Although the Bayesian network demonstrated many expected dependencies (eg, between descriptors in similar descriptor categories: between microcalcification types, mass types, skin findings, and demographic risk factors), it also revealed some unexpected dependencies (eg, the dependence of BI-RADS category and mass stability). The inability to account for these dependencies without help from a computer may account for some radiologist errors and performance variability.

The Bayesian network appears to be most effective in decreasing the need for recall (substantially reducing BI-RADS category 0 interpretations), which may address problems encountered in the clinical testing of computer-assisted detection $(22,23)$. The Bayesian network classified thousands of false-positive BIRADS category 0 assessments correctly as negative (Table 4), which may have the potential to decrease patient anxiety and the need for additional testing (whether this may be during the screening or the diagnostic step). In fact, a probability assessment at the time of a BI-RADS cate-

gory 0 evaluation may facilitate communication between the patient and the physician, as well as assist in the determination of appropriate treatment.

However, the threshold that enables accurate classification of BI-RADS category 0 findings may be accompanied by trade-offs. A small number of BI-RADS category 0,4 , or 5 cancers may be missed (true-positives converted to false-negatives), and accurately assessed BI-RADS category 2 and 3 findings may raise suspicion (true-negatives converted to false-positives). However, the missed cancers shown in Table 4 often did not have the appropriate descriptors recorded in the database. All three BIRADS category 0 breast cancers missed at the $0.05 \%$ threshold had erroneously recorded descriptors. For example, in one of these cases, a new oval mass with an obscured margin was recorded in the text report, but the structured data from PenRad recorded a lymph node. Our results depend entirely on the quality of the structured data entered by the radiologist in clinical practice, which is certainly not perfect. In fact, 3285 records documented BI-RADS categories that indicated findings (BI-RADS category $0,3,4$, or 5 ) but contained no specific finding descriptors (Appendix E2, http://radiology.rsnajnls.org/cgi /content/full/2513081346/DC1). Apparently, the radiologist typed the results rather than entering structured data. Clearly, improvements in structured reporting, including consistency checks between recorded predictive variables and text reports, will be necessary before the data can be reliably used for decision support. This problem would also likely be addressed if the radiologist were interacting with the system in real time. Because Bayesian network inference takes less than 1 second, realtime interaction between the radiologist and the Bayesian network is entirely feasible. However, Bayesian network integration with the mammography reporting system, which is not currently available, would be important for optimal workflow.

The impact of reversals in correctly assessed BI-RADS category 2 and 3 findings is difficult to evaluate without
knowing the predicted probability and the clinical context. It is possible that the probability of malignancy in these cases was not much higher than the threshold and would not have generated additional imaging or biopsy. A future clinical trial of Bayesian decision support is the only way that we will be able to tease out how performance differences identified in our retrospective analysis would translate to the more ideal scenario of risk prediction at the point of care.

The Bayesian network works very differently from conventional computerassisted detection algorithms (11-21) that provide a mark on the image (adding yet another variable to the radiologist's long list of breast cancer predictors). The Bayesian network provides a posttest probability that consolidates all the predictive variables in the NMD (demographic variables, mammographic descriptors, and BI-RADS assessment categories) into a probability of malignancy. It is possible that the predictive ability of these variables may be redundant and of differential value. However, the literature clearly shows that descriptors, as well as BI-RADS categories, can be variable and sometimes inaccurate (43-45); therefore, inclusion of all variables will likely ameliorate such errors. We did not attempt to determine the most predictive variables (demographic variables, descriptors, or ultimate BI-RADS categories), but plan this for future work.

There are also substantial differences between our Bayesian network and other computer-assisted diagnosis systems that use suspicious cases selected from biopsy databases to train their systems $(24,25,27,30,31,34,46,47)$. Our Bayesian network, in contrast, was trained on consecutively collected mammographic findings, perhaps allowing it to more accurately estimate posttest probabilities and better balance improvements in sensitivity and specificity with more realistic estimates of breast cancer prevalence. The consecutive nature of our data set helped ensure that we did not exclude select groups from our study and may indicate future generalizability to similar mammography practices. Further research is needed to validate this theory.

Our Bayesian network also differs
from general risk prediction models (48-51) like the Gail model, which predicts the probability that a woman will develop breast cancer sometime in the future. The Bayesian network estimates breast cancer risk at a particular point in time. A woman at high risk for breast cancer can have a finding with a low probability of malignancy, and a woman at low risk can have a finding with a high probability of malignancy, depending on her mammographic results (52). Single-time-point risk information is more appropriate for driving management decisions such as recall or biopsy.

Our study reinforces the belief that the mammographic features catalogued in BI-RADS can help classify breast findings $(32,53,54)$ but raises concerns about interobserver variability $(43,55)$. Despite performance variability among the radiologists in our study, the consistently superior performance of the Bayesian network suggests that such variability is not an insurmountable problem. Although the important question of how much interobserver variability affects Bayesian network performance is outside the scope of this article, we have done preliminary work demonstrating that training and testing the Bayesian network with individual radiologists does not significantly change the results (56). Ultimately, proof of the generalizability of our Bayesian network to additional radiologists or practices will require further research.

The most fundamental limitation to our study was that screening and diagnostic mammography were not analyzed separately. This issue is not uncommon and has been previously reported in the literature (37). In general, the mixed screening and diagnostic findings affected the prevalence of cancer and the skew (many more negative than positive cases), which in turn likely affected our results to some degree. For example, the prevalence in our pooled population was higher than that in a pure screening group and lower than that in a pure diagnostic group. Our pooled population was less skewed than a pure screening group and more skewed than a pure diagnostic population. These differences likely hinder the

predictive ability of our Bayesian network by adding to the variability of the data without providing a node (ie, screening or diagnostic) in the network to explain that variability. Therefore, our performance estimates may be pessimistic. Although the performance achieved by the Bayesian network in a mixed data set is encouraging, we plan future studies on screening and diagnostic mammography separately to see if performance differs in either of these types of examinations in isolation. Our comparison of ROC curves between the radiologists and the Bayesian network was also suboptimal, because while the radiologists summarized their assessments in BI-RADS categories, the Bayesian network output was measured in probability. Although a similar analysis has been presented in the literature (50), it is not a perfectly equal comparison. These concerns are ameliorated somewhat in our work by the fact that the performance of the Bayesian network was superior to that of the radiologist at all threshold levels. Further work in equalizing ROC comparisons when the output scalars are distinct would be helpful. Finally, the fact that a small proportion of findings could not be matched to a reading radiologist represented a minor limitation. We made the decision to include these findings to preserve the consecutive nature of our population.

In conclusion, our study results demonstrate that a Bayesian network can accurately estimate the probability of breast cancer for findings identified at mammography, identify dependencies among predictive variables, and perform better than interpreting radiologists alone. The Bayesian network is not intended to replace the radiologist but rather to capitalize on the radiologist's skill in characterizing findings while aiding in the mathematic integration of predictive variables into an accurate risk assessment. In the future, probabilistic computer models like this Bayesian network may substantially aid physicians attempting to diagnose breast cancer in a timely and accurate manner.

# Radiology 2009

This is your reprint order form or pro forma invoice (Please keep a copy of this document for your records.)

Reprint order forms and purchase orders or prepayments must be received 72 hours after receipt of form either by mail or by fax at 410-820-9765. It is the policy of Cadmus Reprints to issue one invoice per order. Please print clearly.

Author Name
Title of Article
Issue of Journal
Number of Pages
Color in Article? Yes / No (Please Circle)
Reprint #
KB #
Publication Date
Symbol Radiology
Color in Article? Yes / No (Please Circle)
Please include the journal name and reprint number or manuscript number on your purchase order or other correspondence.
Order and Shipping Information

Reprint Costs (Please see page 2 of 2 for reprint costs/fees.)
______ Number of reprints ordered $______
Number of color reprints ordered $______
Number of covers ordered $______
Subtotal $______
Taxes $______
(Add appropriate sales tax for Virginia, Maryland, Pennsylvania, and the
District of Columbia or Canadian GST to the reprints if your order is to
be shipped to these locations.)

First address included, add $32 for
each additional shipping address $______

TOTAL $______

Shipping Address (cannot ship to a P.O. Box) Please Print Clearly
Name
Institution
Street
City State Zip
Country
Quantity Fax
Phone: Day Evening
E-mail Address

Additional Shipping Address* (cannot ship to a P.O. Box)
Name
Institution
Street
City State Zip
Country
Quantity Fax
Phone: Day Evening
E-mail Address

* Add $32 for each additional shipping address

Payment and Credit Card Details
Enclosed: Personal Check
Credit Card Payment Details
Checks must be paid in U.S. dollars and drawn on a U.S. Bank.
Credit Card: __ VISA __ Am. Exp. __ MasterCard
Card Number
Expiration Date
Signature: ______________________________
Please send your order form and prepayment made payable to:
Cadmus Reprints
P.O. Box 751903
Charlotte, NC 28275-1903
Note: Do not send express packages to this location, PO Box.
FEIN #:541274108

Invoice or Credit Card Information
Invoice Address Please Print Clearly
Please complete Invoice address as it appears on credit card statement
Name
Institution
Department
Street
City State Zip
Country
Phone Fax
E-mail Address

Cadmus will process credit cards and Cadmus Journal
Services will appear on the credit card statement.

If you don't mail your order form, you may fax it to 410-820-9765 with
your credit card information.

Signature Date
Signature is required. By signing this form, the author agrees to accept the responsibility for the payment of reprints and/or all charges
described in this document.

Page 1 of 2
RB-1/01/09

# Radiology 2009

Black and White Reprint Prices



Minimum order is 50 copies. For orders larger than 500 copies, please consult Cadmus Reprints at 800-407-9190.

## Reprint Cover

Cover prices are listed above. The cover will include the publication title, article title, and author name in black.

## Shipping

Shipping costs are included in the reprint prices. Do mestic orders are shipped via FedEx Ground service. Foreign orders are shipped via a proof of delivery air service.

## Multiple Shipments

Orders can be shipped to more than one location. Please be aware that it will cost $\$ 32$ for each additional location.

## Delivery

Your order will be shipped within 2 weeks of the journal print date. Allow extra time for delivery.

## Color Reprint Prices



## Tax Due

Residents of Virginia, Maryland, Pennsylvania, and the District of Columbia are required to add the appropriate sales tax to each reprint order. For orders shipped to Canada, please add 7\% Canadian GST unless exemption is claimed.

## Ordering

Reprint order forms and purchase order or prepayment is required to process your order. Please reference journal name and reprint number or manuscript number on any correspondence. You may use the reverse side of this form as a proforma invoice. Please return your order form and prepayment to:

## Cadmus Reprints

P.O. Box 751903

Charlotte, NC 28275-1903 Note: Do not send express packages to this location, PO Box. FEIN #:541274108

## Please direct all inquiries to:

## Rose A. Baynard

800-407-9190 (toll free number) 410-819-3966 (direct number) 410-820-9765 (FAX number) baynardr@cadmus.com (e-mail)

Reprint Order Forms and purchase order or prepayments must be received 72 hours after receipt of form.