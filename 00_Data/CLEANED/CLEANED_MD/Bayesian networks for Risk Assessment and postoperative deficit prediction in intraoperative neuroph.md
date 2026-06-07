# Bayesian Networks for Risk Assessment and Postoperative Deficit Prediction in Intraoperative Neurophysiology for Brain Surgery 

Ana Mirallave Pescador<br>a.mirallave-pescador@nhs.net

King's College Hospital NHS Foundation Trust
José Pedro Lavrador
King's College Hospital NHS Foundation Trust
Arjel Lejarde
King's College Hospital NHS Foundation Trust
Cristina Bleil
King's College Hospital NHS Foundation Trust
Francesco Vergani
King's College Hospital NHS Foundation Trust
Alba Díaz Baamonde
King's College Hospital NHS Foundation Trust
Christos Soumpasis
King's College Hospital NHS Foundation Trust
Ranjeev Bhangoo
King's College Hospital NHS Foundation Trust
Ahilan Kailaya-Vasan
King's College Hospital NHS Foundation Trust
Christos M. Tolias
King's College Hospital NHS Foundation Trust
Keyoumars Ashkan
King's College Hospital NHS Foundation Trust
Bassel Zebian
King's College Hospital NHS Foundation Trust
Jesus Requena
Queen Mary University of London

## Research Article

Keywords: Intraoperative Neuromonitoring, IONM, Bayesian Networks, Risk Analysis
Posted Date: August 2nd, 2023
DOI: https://doi.org/10.21203/rs.3.rs-3207540/v1
License: (0) (1) This work is licensed under a Creative Commons Attribution 4.0 International License. Read Full License

Additional Declarations: No competing interests reported.

Version of Record: A version of this preprint was published at Journal of Clinical Monitoring and Computing on May 9th, 2024. See the published version at https://doi.org/10.1007/s10877-024-01159w.

## Abstract

## Purpose

To this day there is no consensus regarding evidence of usefulness of Intraoperative Neurophysiological Monitoring (IONM). Randomized controlled trials have not been performed in the past mainly because of difficulties in recruitment control subjects. In this study, we propose the use of Bayesian Networks to assess evidence in IONM.

## Methods

Single center retrospective study from January 2020 to January 2022. Patients admitted for cranial neurosurgery with intraoperative neuromonitoring were enrolled. We built a Bayesian network with utility calculation using expert domain knowledge based on logistic regression as potential causal inference between events in surgery that could lead to central nervous system injury and postoperative neurological function.

## Results

A total of 267 patients were included in the study: 198 (73.9%) underwent neuro-oncology surgery and 69 (26.1%) neurovascular surgery. 50.7% of patients were female while 49.3% were male. Using the Bayesian Network's original state probabilities, we found that among patients who presented with a reversible signal change that was acted upon, 59% of patients would wake up with no new neurological deficits, 33% with a transitory deficit and 8% with a permanent deficit. If the signal change was permanent, in 16% of the patients the deficit would be transitory and in 51% it would be permanent. 33% of patients would wake up with no new postoperative deficit. Our network also shows that utility increases when corrective actions are taken to revert a signal change.

## Conclusions

Bayesian Networks are an effective way to audit clinical practice within IONM. We have found that IONM warnings can serve to prevent neurological deficits in patients, especially when corrective surgical action is taken to attempt to revert signals changes back to baseline properties. We show that Bayesian Networks could be used as a tool to calculate the utility of conducting IONM, which could save costs in healthcare when performed.

## Introduction

Intraoperative Neurophysiological Monitoring (IONM) is a medical discipline from clinical neurophysiology used during neurosurgery to reduce the risk of damaging neural structures. IONM

consists of two intraoperative procedures: the mapping of the neural structures within the surgical field and the continuous functional monitoring of these neural structures throughout surgery. Multimodality monitoring is considered the gold standard in IONM and consists in employing more than one technique to monitor the different neural structures at risk (1-4).

Significant IONM signal changes constitute warnings that could indicate temporary or permanent damage to neural structures which can translate into functional impairment after surgery. After the detection of an IONM signal change, a team-based approach by the neurosurgeon and the anesthetist is needed to apply corrective measures in an attempt to revert the neurophysiological warnings. If the IONM signal properties come back to baseline, it is assumed that this indicates preservation or recovery of the neural structure that was at risk of being potentially damaged. Reversible signal changes, defined as those that revert to baseline after corrective measures, could be associated with a lower chance of a new postoperative neurological injury. Irreversible signal changes, however, are believed to carry a higher risk of a new permanent injury. However, the correlation of a signal change to neurological injury cannot always be assessed in surgery, especially under general anesthesia.

In this regard, the reliability of IONM has been questioned and whether it adds value to the safety of the surgery is a debatable matter. Recent publications have underlined the need for evidence based IONM $(5,6)$. Classical approaches such as prospective, randomized controlled trials (RCTs) have not been carried out due to questionable equipoise (7). Also, performing RCTs in neurosurgery often meets the barrier of practicality. Usually, surgical professionals and patients are unlikely to want to enroll, if a control group involves one not offering IONM (8). Alternatives to RCTs can be designed to assess evidence in IONM. The aim is to answer the question of whether reversing a signal change back to baseline in surgery, would avoid the patient from waking up with a new postoperative injury (9).

From an evidence analysis point of view, we want to answer counterfactual questions about unobserved events. Specifically, in IONM we would like to know whether a given signal change correlates to injury, based on the evidence of events that we do observe, i.e. for which we do have data, known as prior data. These questions could be answered through mathematical causal inference using Bayesian Networks (10), which allow us to answer counterfactual questions on new data (i.e. from a new patient), when we have similar prior data, and known outcomes. Bayesian Networks in IONM would do this by providing an estimation of the probability of a neurological injury based on the prior probability distribution of the events that surrounded this injury in patients in the past. This estimation is explicitly represented as a network of connected nodes whose links conform to expert domain knowledge and constitutes the computational engine for causal inference. Therefore, Bayesian Networks could shine light on the evidence of IONM increasing safety for patients during these neurosurgical procedures.

The goal of our study is to propose a Bayesian Network approach to answer counterfactual questions about IONM signal changes during cranial neurosurgery, specifically neuro-oncology and neurovascular surgery.

## Methods

Our study consisted in a retrospective single center study of IONM and epidemiological data of patients undergoing neurosurgery during the years 2020–2022. The local Institutional Review Board exempted this prospective analysis of retrospectively collected data as research.

The inclusion criteria were patients admitted for cranial surgery with neuro-oncology (primary and secondary tumours) and/or neurovascular pathology (arteriovascular malformations, aneurysm clipping, cavernoma and arteriovenous fistulas). Both adult and pediatric patients were included. Patients were grouped in 4 groups according to their age, as seen in Table 1.

Table 1
Demographics of the included patients



Demographics for age, sex, and location of the lesions as well as preoperative and postoperative neurological function were collected from electronic records and are shown in Table 1. IONM techniques were divided into two categories: mapping and monitoring. For both procedures, two types of electrodes can be used: direct cortical/subcortical electrodes and transcranial electrodes. All signals were recorded using built-in amplifiers and filter tailoring was performed to record specific signals by a Medtronic Nim Eclipse system ${ }^{\circledR}$ with IONM software.

Assumptions based on the existing literature were made before building the Bayesian Network. We assumed that transcranial stimulation and recordings are less specific than direct cortical in brain surgery. This is because the distance from the electrode to the functional brain area at risk is larger when recording or stimulating through the skull (11). We also assumed that multimodality IONM should be preferred to unimodal (12). Based on this, we classified IONM procedures into 3 groups:

# 1. Optimal intraoperative neuromonitoring: 

Multimodality IONM including direct cortical and subcortical Motor Evoked Potentials (MEPs), direct cortical Somatosensory Evoked Potentials (SSEPs), direct cortical language mapping, direct cortical Visual Evoked Potentials (VEPs), electrocorticography (EcoG) and all their transcranial modalities when possible. Monitoring is done continuously to guarantee real-time signal acquisition during surgery to assess functional integrity of the brain.

Suboptimal intraoperative neuromonitoring.
Multimodal IONM but exclusively transcranial modalities or cortical modalities performed and not in a continuous manner.
Inadequate intraoperative neuromonitoring.
Unimodal IONM or IONM that did not guarantee safety for the patient. For example, sporadic signal acquisition.

## Significant Signal Changes

For MEPs, the following signal changes were considered significant: (1) an abrupt disappearance when stimulating at threshold intensity, defined as an intensity that elicited at least $50 \%$ of the MEPs from the muscles after repeated stimulation of the motor cortex of the brain; (2) changes in stimulation threshold eliciting MEPs (above 100V if transcranial, above 3 mA if direct cortical); (3) a reduction of more than $80 \%$ of baseline signal amplitudes at supramaximal intensity, defined as the intensity able to elicit 100\% of the MEPs at baseline after repeated stimulation (13); and (4) an approximate mapped distance of less than 5 mm to the corticospinal motor tracts during tumor resection surgery, estimated by dynamic subcortical MEPs (14). For SSEPs and VEPs, we considered a reduction of 50\% amplitude and 10\%

increase in latency of baseline signals $(15,16)$. Finally, for speech we considered difficulties encountered during surgery, for example, difficulties in initiation of speech or fluency (17).

We further classified signal changes as:

1. Reversible, if the signal change reverts after surgical corrective action is taken when brain damage is suspected in surgery. In this case, recovery of the functional area is expected. Corrective actions we considered included taking a surgical break or stopping resection in that area, blood pressure increase, warm irrigation or papaverine administration in some cases.
2. Irreversible, if the signal change from baseline does not revert, regardless of whether corrective actions were taken. An irreversible signal change has high chance of permanent damage to the neural structure related to this signal.

# Bayesian Network Approach 

Bayesian Networks are directed acyclic graphs. A graph is a mathematical abstraction that consists of nodes and edges that connect the nodes. As acyclic graphs, Bayesian Networks do not permit cycles between its nodes. There are 3 different types of nodes in Bayesian Networks: chance nodes, decision nodes and utility nodes. In addition, Bayesian Networks contain a set of conditional probability distributions that represent the relationship of its nodes and their potential causal dependence, represented by the network's edges. The edges are based on expert domain knowledge and are often assumed based on logistic regression associations between the nodes. The edges in a Bayesian Networks define every possible outcome of the preceding causal nodes in the form of conditional probability distributions. Given observed evidence, the prior probability of that evidence is defined as the probability of its occurrence before new data is collected. Bayesian networks use prior probabilities to estimate the conditional probability distributions of each of its nodes, in the presence of new, unobserved data.

We used the commercial software AgenaRisk® to implement our network. We incorporated expert domain knowledge from our own working experience and the literature to design the network and establish its nodes and edges (Fig. 1). The network's prior probabilities were computed with data from retrospective cases performed in our center, for which we knew the outcome. With this data, we first analyzed the original state of our prior probabilities. The original state included the prior probabilities of patients having optimal IONM, the probability that a neurophysiologist identifies a signal change and whether this was reversible or permanent change, the probability of surgeons causing significant damage to the patients overall and the probability that patients with a signal change wakes up with a new deficit. Secondly, we looked at counterfactual reasoning. Counterfactual reasoning was calculated by filling potential new observations in the network's nodes, over the computed prior probabilities.

Our aim was to answer the following questions:

1. What is the likelihood of patients waking up intact, with a transitory deficit or with a permanent deficit if a reversible signal change was seen in surgery and surgeons took corrective action vs when they did

not?
2.What is the outcome if a permanent signal change is observed?
3. If a patient wakes up with a permanent/transitory deficit or intact, what is the likelihood that a permanent/reversible signal change, or no change was detected? What is the likelihood that corrective action was taken?
4. What is the decision that maximizes the utility when a signal change is detected (both transitory or permanent), taking corrective action or not taking it?

Software packages such as AgenaRisk® can update the probabilities in a network using new observations based on the network's architecture and through the application of Bayes' theorem

$$
P[\text { Cause } \mid \text { Evidence }]=P[\text { Evidence } \mid \text { Cause }] * \frac{P[\text { Cause }]}{P[\text { Evidence }]}
$$

1
where $P[$ Cause] is the prior probability of a cause, $P[$ Evidence] is the prior probability of observing a piece of evidence, $P[$ Cause|Evidence] is the probability of a cause given an observed evidence and $P[$ Evidence|Cause] is the probability of observing a piece of evidence in the presence of the cause. Our network architecture had the nodes and edges that are described subsequently.

# Chance Nodes 

Table 2 shows the chance nodes we considered in our network. i.e. the nodes whose outcomes don't depend on the decision maker.

Table 2


Decision Nodes

Only one decision node was considered, namely acting after a signal change. Corrective measures in response to a signal change include avoiding the surgical site or taking a surgical corrective maneuver after the warning (e.g. removing a temporary clip) taking a surgical break, raising the blood pressure to increase perfusion to the area, irrigation with warm saline, papaverine infusion in the suspicion of a vascular event. Based on this, we defined three types of corrective actions:

- Adequate: all measures attempted.
- Insufficient: some but not all measures were or could be attempted.
- Inadequate: nothing was or could be done.


# Utility Nodes 

To define a suitable utility in IONM we identified two main options. The first option associates a subjective value to different outcomes such as complete surgical tumor removal despite a neurological injury, or preservation of neural function despite incomplete tumor removal. The second is to simply associate a monetary utility to the outcome. The latter option is easier to formulate, although it provides an incomplete assessment of the value of an outcome.

We quantified the potential net monetary utility of the presence or absence of a postoperative neurological deficit based on the healthcare costs incurred, which were estimated following the figures previously reported in $[18,19]$. Patients with a postoperative deficit in our center are normally admitted to the neurorehabilitation unit to recover. On average, patient stay in neurorehabilitation spans from 8-16 weeks. We assumed that patients with a new onset deficit that recovered after treatment in the neurorehabilitation unit would need around 8 weeks. This would have a total cost for the National Health Service (NHS) of $£ 56,952$ for pediatric patients and $£ 29,680$ for adults. In contrast, if the deficit was permanent, these patients would have at least stayed 16 weeks in neurorehabilitation. This would cost the NHS $£ 113,904$ for pediatric patients and $£ 59,360$ for adults. In contrast to this, if a patient did not wake up with a deficit, the cost to the NHS would be $£ 0$. Also, if the deficit was present but recovered, the NHS would have saved the additional 8 weeks' cost of admission, which would have been spent if the deficit was permanent. Costs, benefits, and net utility nodes were added to the network to account for these figures. The net utility was calculated as:

$$
\text { NetUtility }=\text { Benefits }- \text { Costs }
$$

2
where benefits are the total savings of the NHS ( 16 weeks' savings if no deficit was present) and costs are the total costs ( 16 weeks' admission in neurorehabilitation for a permanent deficit, 8 for a temporary deficit)

## Expert domain knowledge prior probabilities

We used epidemiological prior probabilities published in the literature to build the nodes corresponding to preoperative motor and sensory deficit. We did not use epidemiological data for other nodes and chose to use data from our center instead. Regarding the nodes of preoperative motor weakness and preoperative sensory weakness for neuro-oncology, Motomura et al. studied the incidence of motor deficits in pediatric frontal tumors [20]. This was approximately $36 \%$, of which $20 \%$ were mild. In adults, a similar study was carried out by Amidei et al. [21]. Motor deficits were present in $26 \%$ of the population. Regarding sensory deficits, Chandana et al. [22], reported that in adults these consisted of around 13\% in parietal lobe tumors. No data could be found in the pediatric population. Regarding visual deficits, for tumors in the occipital lobe of the brain, Goodwin et al. [23], reported an incidence 11\% of cases in adults and Peragallo et al. [24] a $27 \%$ in children. A total of $11 \%$ of the visual deficits were severe, for instance homonymous hemianopia. No data was found for motor deficits in occipital and parietal tumors. However, this area of the brain is not the primary motor area, so motor deficits are not expected.

A similar approach was taken regarding vascular lesions. Raps et al. [25] reported on the clinical spectrum of unruptured intracranial aneurism in adults. They found $11 \%$ of motor deficits and a $10 \%$ of sensory deficits. Regarding the pediatric population however, no data could be found on sensory deficits of unruptured aneurisms while a $53 \%$ motor weakness was reported [26]. Regarding visual deficits, the data mainly focused on posterior communicating aneurisms and was of $25 \%$ in the pediatric population and $29 \%$ in adults [27].

# Expert Domain Knowledge Edges: 

The causal inference edges proposed in the model are proposed in Table 3. They are the result of expert domain knowledge based on published association studies through frequentist statistical analysis.

Table 3


## Results

A total of 267 patients were included in the study: 198 (73.9%) underwent a neuro-oncology and 69 (26.1%) patients underwent a neurovascular surgery. Demographics for sex, age, and location of the lesions are shown in Table 1. Specifically, 50.7% of patients were female while 49.3% were male. Regarding the age, 3.1% belonged to age-group 1, 10.1% to group 2, 28.2% to group 3, 49.7% to group 4 and 8.9% group 5.

The probability of our patients presenting with a preoperative deficit regardless of the location of the lesion was low (94.4%). There was only a 5.8% for preoperative motor deficits and 5.9% preoperative sensory deficits, including sensory, language, and visual deficits. Our patients presented with optimal monitoring modalities in 72.7% of the cases and in 13.9% modalities were inadequate. In 98.9% of the cases, we used total intravenous anesthesia with propofol and remifentanil.

Of the patients studied, 24 woke up with a transitory deficit postoperatively and within this group16 presented with a signal change during monitoring. A permanent deficit was observed in 16 patients and 15 of these presented with a signal change during monitoring. Signal changes were seen in the same proportion of patients with optimal (20.4\%) and suboptimal or inadequate (20.1\%) modalities. However, the proportion of patients with less than adequate modalities was significantly lower (27.3\%) than those with adequate modalities. Of the patients that presented with a reversible signal change, 21 developed no new deficit (action taken was adequate in all), 14 had a transitory deficit (in 12 action taken was adequate) and 3 presented a permanent deficit (in all of them the action taken was adequate). In those with a permanent signal change, 4 showed no new deficit and the action taken was adequate, 13 presented permanent deficits (in 6 the action taken was inadequate) and 2 presented with transitory deficits (the action taken was adequate).

# Network's Original State Probabilities. 

Within our cohort of patients, $94.4 \%$ had adequate pre-incision baseline signals. In $79.8 \%$ of the cases, the surgery would have happened without a significant signal change. In line with this, the probability of a surgical injury (23.3\%) was also lower than the probability of no injury (76.7\%). 20.4\% of the time, signal changes would be seen in surgery: $13.6 \%$ reversible signal changes and $6.8 \%$ irreversible signal changes. The probability of postoperative deficits in our series was $8.8 \%$ for transitory postoperative deficits and $6 \%$ for permanent.

Out of the transitory deficits, 4 patients presented supplementary motor area (SMA) syndrome, 6 patients presented with transient severe pure motor deficits, 1 patient presented with hemianopia, 3 patients presented with transitory speech difficulties and the rest with minor sensory or motor deficits of only one limb. Signal changes were seen in 16 patients ( 2 of these with permanent signal changes) and not in 8 including the patients with SMA syndrome and 2 patients with visual deficits. The other 2 presented with minor sensorimotor disturbances.

Out of the permanent deficits, 5 presented with visual deficits (hemianopia/quadrantanopia), 4 presented with a hemiplegia due to an intraoperative stroke, 5 hemiplegia due to structural damage and 4 with motor weakness of at least one limb ( 2 due to vascular event and 2 structural damage). Signal changes were detected in all but 1 patient who developed a hemianopia. In 12 patients the signal change was permanent.

## Counterfactual reasoning with potential new data

If we consider a reversible signal change in surgery, our network predicts adequate corrective action would have been taken in $95 \%$ of the cases. In this scenario, $59 \%$ of patients would wake up with no new neurological deficits, $33 \%$ with a transitory deficit and $8 \%$ with a permanent deficit. If the signal change was reversible but not all actions were or could be taken, it would predict the deficit would be transitory.

If the signal change was permanent, adequate action would have been taken in $66 \%$ of the cases and if taken, there would be a $33 \%$ chance that the patient would not wake up with a new postoperative deficit. In $16 \%$, the deficit would be transitory and in $51 \%$ it would be permanent. If not all actions were or could be taken however, under the circumstances of our sample, all patients would wake up with a permanent new postoperative deficit.

On its own, if we imagine a new patient that has woken up with a permanent postoperative deficit, the network shows a probability of $76.2 \%$ that the signal change seen in surgery was permanent. In $17.2 \%$ it was reversible. Interestingly, $6.6 \%$ of the cases would have been unnoticed by the neurophysiologist. In $55.1 \%$ of cases were a signal change was seen, adequate action would have been performed to try to correct the signal change. However, in $38.3 \%$ of cases, not all actions were/could be done about the warning.

If we know the patient woke up intact, there is an $89.3 \%$ chance that there was no signal change in the surgery. In $8.9 \%$ a reversible signal change would be seen. There is a small probability of $1.8 \%$ that there would be a permanent signal change, i.e. a false positive.

If it is observed that a patient has woken up with a new transitory postoperative deficit, there is a probability of $55.8 \%$ that a reversible signal change was seen. In $8.1 \%$ the signal change would be permanent. Adequate action would be taken intraoperatively in $56.2 \%$ of cases. No action, or not all possible actions in $7.7 \%$. Interestingly, there is a chance ( $36.1 \%$ ) that this would not be detected in surgery.

# Utility 

Table 4 shows the results of the net utility calculations for the different postoperative outcomes to patients, when action or no action is taken after a signal change. Decisions that maximize the utility (Table 4) are acting in response to a signal change (both reversible and irreversible). If the signal change is reversible and we act, $59 \%$ of patients will wake up intact. This means the hospital would have a net benefit of $£ 61,063$ (our network showed a probability of $100 \%$ of patients waking up with a transitory deficit). If the signal change is permanent and we act, $34 \%$ of patients would wake up intact, saving the hospital $£ 61,033.78$. In the case of a permanent signal change however, unfortunately, $50 \%$ of patients would wake up with a permanent deficit, costing the hospital $£ 61,033.78$. It therefore raises the question of when, action should be taken. A sensible option would be for action to be taken before a reversible signal change becomes permanent.

Table 4
Net Utility when acting or not after detecting a signal change.


# Discussion 

IONM has the potential to improve the outcome of patients undergoing neurosurgery as it is assumed to predict damage early enough to prevent it. However, solid evidence on its actual performance has not been studied. While it is reasonable to suggest RCTs as a suitable approach to provide evidence on the usefulness of IONM [28], some question whether these would be ethical [29] due to the devastating potential outcomes patients may face if un-monitored. Evidence based IONM therefore must determine what is the significance of relevant signal changes in surgery, in the absence of RCTs. The quality of the evidence available plus the benefits and harms of the technique itself must be weighed in deciding whether IONM should be performed. When RCTs are not possible [6], our study shows that Bayesian Networks can provide an alternative approach to predict outcomes.

Our Bayesian Network approach showed firstly that most patients presented the prior optimal conditions for IONM: good baseline clinical status, adequate IONM modalities most times and commonly agreement in surgery between neurophysiologist and neurosurgeon. Moreover, our study showed that unlike other previously reported data [30], most surgeons would respond adequately to IONM signal changes.

We also have seen how to use the network to answer counterfactual questions given our priors. We saw that correcting signal changes intraoperatively increases the likelihood of patients waking up intact, even for permanent signal changes. Holdefer et al. [31] suggested that reversible signal changes had a positive impact on patient outcome. Our data agrees. If taking adequate actions in response to reversible

signal changes or if action is attempted when signal changes are permanent, patients showed a higher probability of waking up intact or only having a transitory deficit. This is not only better for patients but also profitable for the hospital as it increases utility. IONM would prove to be an essential part of dynamic decision-making during brain surgery, which allows corrective actions to be taken based on dynamic neurophysiological changes and results in improving the patient's outcome, rather than being a simple yes/no type of diagnostic test as is often erroneously pictured in the literature.

Holdefer et al. [32] suggested this description of a dynamic medical intervention of IONM in intracranial vascular procedures. They saw there was a $60 \%$ decrease in new deficits after MEP changes that were reversed intraoperatively. Similarly, Holdefer et al. [31] analyzed the use of signal changes as biomarkers for predicting neurological injury when there was a valid contextual reason for these changes in the surgery according to Hill's guidelines for causation. Even though the actual neural function cannot be assessed under general anesthesia they suggested that signal changes can be used as biomarkers of intraoperative neurological function for the patient. Therefore, corrective actions to revert signal changes could dramatically impact patient postoperative outcome when done appropriately and there is a clear causal link identified in surgery [33-35].

Most signal changes that were reversible in our center had adequate corrective action (95\%), while 66\% of changes that were permanent had adequate corrective action. This could suggest that signals were reversible because action was taken to revert them, rather than by chance. Moreover, neurophysiological changes correlated well with patient postoperative outcomes. Our counterfactual reasoning using our network and our prior probabilities showed that patients with no postoperative deficits, likely had no signal changes. Those with permanent signal changes were more likely to have permanent postoperative deficits and those with reversible signal changes, were more likely to have transitory deficits. Therefore, we believe that reverting a signal change with corrective action has a meaningful impact to patients' postoperative status. In our network, if taking adequate corrective action, $59 \%$ of patients with a reversible signal change would wake up intact and $33 \%$ would recover from their deficits if corrective action was taken. Moreover, it would be net neutral ( $£ 0$ net utility) for the hospital. Even patients with a permanent signal change showed a $35 \%$ chance of waking up intact and a $16 \%$ chance of recovering from their deficits if adequate corrective action was taken.

In these scenarios, outcome would also be net neutral for the hospital. However, it is worth noting that $49 \%$ of the patients would wake up with a permanent deficit regardless of corrective action, and therefore permanent signal changes are often a sign of poor outcome. Unfortunately, IONM also has limitations and postoperative deficits are observed without signal changes. SMA syndrome and other motor deficits do not always show neurophysiological changes intraoperatively [36]. Regarding visual function, VEP changes don't always correlate with postoperative outcome [37]. Even with improved techniques in the last years, correlation with visual acuity is still to be determined [16, 38].

We have also observed that neurophysiologist would have no difficulties in detecting a signal change when less than adequate IONM modalities (inadequate or insufficient) are used. However, this does not

rule out that if the modalities used had been adequate, the neurophysiologist might have detected the signal change earlier. Further studies with a larger sample of patients with less than adequate modalities, might be able to answer this question.

It is worth asking about the outcome in cases where signal changes are reverted before they become permanent? Some signal changes are not easy to revert, for instance signal changes secondary to an accidental stroke. We believe that it could be worth asking whether time plays a role in clinical outcome. Further studies should focus on whether reacting fast enough to a signal change can prevent a signal change from being permanent. As previously mentioned, it would be interesting to assess whether signal changes could be noted on the same patient earlier, when using adequate modalities as opposed to insufficient/inadequate.

Our study presents several limitations. Firstly, our study has limited data. We believe that age groups 3 and 4 , could have outnumbered the other age groups had the data been more complete. Further studies will have to be undertaken to assess these results on age groups 1-2 and 5 to avoid selection bias, also known as Berckson's bias. At the same time, it shows a demographic that is not uncommon, given the epidemiology of the lesions and not unexpected given the proportion of surgeons that operate on these age groups in our center and given the suitability for patients to undergo surgery when very elderly. We also acknowledge that within the groups, there may not be enough data about every single condition studied, for example, patients undergoing surgery with insufficient/inadequate modalities of IONM. To assess prior probabilities more reliably, a greater sample would be needed for some conditions highlighted in this study. Our study only comprises a sample of 267 patients of which most presented without complications in surgery or signal changes. We believe that more accurate prior probabilities will be achieved with a larger sample of patients presenting complications. In relation to the above, the total number of patients who presented with complications was 40 patients. Out of this group of patients, most belonged to age-group 4, being age-group 5 the next most numerous. We believe that greater samples in this category of patients with complications and a greater sample of these same patients within the age groups would yield more accurate results. Regardless of these limitations, as far as we know this is the first study that applies Bayesian Networks to neurosurgical practice and study their potential utility in this setting.

# Conclusion 

This study demonstrates that Bayesian Networks could prove evidence of IONM in absence of class 1 evidence studies. We have also seen that most patients have stable IONM signals at baseline. Signal changes are detected in most cases and if adequate action is taken, they are reversible. This has functional implications for patients as it significantly reduces postoperative neurological deficits and it is also cost-effective for the health system.

## Declarations

# Acknowledgements 

We would like to Acknowledge Mr. José Siado Mosquera, Miss Emily Lawson and Miss Sian Murace for their clinical contribution to this work.

# Figures 

![img-0.jpeg](img-0.jpeg)

Figure 1

The Bayesian Network constructed. Chance nodes (blue), Decision nodes (Red) and Utility nodes (Yellow).