# A Bayesian Network Model for the Diagnosis of the Caring Procedure for Wheelchair Users with Spinal Injury 

Maria Athanasiou, Jonathan Y. Clark<br>Department of Computing, University of Surrey, Guildford, Surrey GU2 7XH, UK<br>m.athanasiou@surrey.ac.uk, j.y.clark@surrey.ac.uk


#### Abstract

This paper describes a probabilistic causal model for the caring procedure to be followed on wheelchair users with spinal injury. Uncertainty in the caring procedure arises mostly from incomplete information about patient findings (i.e. the signs and symptoms) due to loss of sensation and movement caused by the spinal cord injury. As a result, it may not be easy to assess the extent of a condition - and, thus, make an accurate diagnosis. Bayesian Networks are used for diagnostic reasoning because they offer a way of conducting probabilistic inference about the conditions associated with the caring procedure in the face of uncertainty. The network structure and numerical parameters are based on data elicited from the qualified staff nurses and literature of the National Spinal Injury Centre, Stoke Mandeville Hospital, Aylesbury, UK. We also present the model and report the results of the diagnostic performance tests using the AgenaRisk Bayesian network package.


## 1. Introduction

The quality of medical care has always been a key issue for both practitioners and patients; more than ever though, it is seen as a crucial target to be met, since the highest standards and practice guidelines are expected in all fields of medicine. Decision Support Systems (DSS) are tools that can ensure such quality care, as long as they are integrated into the daily routine. Investigation for using DSS for assisting medical diagnosis date back to the late 1950s. The systems developed so far use a variety of modelling approaches, which can be broadly divided in two main categories:

- The rule-based approach, where inference is based on rule set. Uncertainty is usually addressed via heuristic methods - making them ineffective in many real-world scenarios [5, 4].
- The probabilistic approach, which benefits from both mathematical consistency and accuracy. In particular, Bayesian Networks have been introduced in the 1980s as a formalism for modelling problems involving uncertainty, adopting probability theory as a basic framework for reasoning [11]. Since then, researchers have been exploring the feasibility and performance of Bayesian Networks in the context of medical applications [2]. Probabilistic dependencies and interactions between signs/symptoms and possible diagnoses among the data can be easily described using a Bayesian Network. Hence, they offer a natural way to represent the uncertainty that arises when attempting to deliver a diagnosis [7]. Thus, any probabilistic statement that concerns individual variables or their combinations can be computed from a properly structured Bayesian network.

The motivation for development of a computer-based carer-advisor system is mainly that the number of experienced human carers for spinal injury patients is very limited, compared to the large number of such patients requiring care. Furthermore, many people who act as carers are not professionally trained, and largely learn as they go along. In addition, since such care commonly takes place in the patient's home, experienced medical staff are rarely available.

The DIMITRA system [3] is a rule-based expert system for the caring procedure to be folllowed by wheelchairs users with spinal injury. The system is considered to be of value for virtual healthcare in the home, because it is designed for remote access by carers and patients. The system

integrates diagnostic reasoning and action (i.e treatment), and uses a rule-based reasoning engine to identify diagnostic and therapeutic goals appropriate to a particular patients state.

However, since uncertainty is inherent in conventional medical diagnosis, the work presented in this paper was carried out as an attempt to enhance the DIMITRA system by means of employing probabilistic reasoning (hence the name, DIMITRA-Pro) in order to expand the system's knowledge base (and incorporate such information such as the patients' individual medical profiles) and provide a means of quantifying uncertainty associated with diagnoses. The system is essentially a Bayesian network modelling the causal relationships among variables as elicited from relevant literature concentrating on the caring procedure appropriate for such patients, as well as direct questioning of domain experts via questionnaires.

# 2. The DIMITRA-Pro Network Structure 

An example of the care procedure that needs to be followed by the carers for wheelchair users suffering from spinal injury is presented below [14]: The patient was involved in a road traffic accident where she sustained a C6 fracture and C6/7 dislocation. The fracture was surgically stabilised and decompressed. The patient also had a tracheotomy, which has now been removed and has undergone a full rehabilitation programme. Her nursing care is currently as follows:

- Bladder Management. The patient uses size 16 ArgyII supra pubic catheter with a 10 ml balloon, which is replaced every 3 weeks. The catheter is attached to a 75 ml leg bag during the day and a 2000 ml night bag at night. The patient is totally dependent on these procedures. The patient is aware of the signs and symptoms of a bladder infection and is able to instruct others on how to take a urine sample. Also, she is aware of the need to drink 2-3 litres of water per day to help prevent bladder problems.
- Bowel Management. The patient has a daily bowel regime; she takes aperients in the evening, and she getting up in the morning onto a shower chair and having 2 glycerine suppositories inserted. After the patient has had a result, the rectum is checked with a well lubricated gloved finger. This is done to insure the rectum is empty and to prevent bowel accidents during the day. The patient requires the assistance of one person for this procedure. The patient is aware of the need to eat a well balanced diet to help prevent bowel problems.
- Skin Management. The patient has no problems with her skin at the moment, she sleeps on a pressure-relieving mattress and is turned every 6 hours during the night. One pillow is inserted behind her back and one between her knees and ankles to help prevent pressure. When the patient is up in her wheelchair she sits on a pressure-relieving cushion. The patient does pressure relief by leaning forward in the wheelchair. The patient is aware of the need to check her skin every morning and evening. The patient requires the assistance of one person to do this. If a red mark should appear she knows what action to take to prevent further deterioration.
- Autonomic Dysreflexia. Due to level of the injury the patient is prone to dysreflexic attacks which can be a life-threatening problem. The patient has had a dysreflexic attack due to her bladder not draining properly.
The case description above illustrates that the caring procedure for spinal injury patients is divided into four sections. These sections are bladder management, bowel management, skin management and autonomic dysreflexia.

Clearly, the same structure is going to be present in the DIMITRA-Pro system as well. Moreover, the spinal injury patients are divided into categories:

- High level patients are those with injured at either the cervical or the upper thoracic regions

of their spinal cord (tetraplegics or quadriplegics).

- Low level patients are those with injuries at the other regions (paraplegics).

Consequently, the diagnosis for the care required in each case is a combination of the level of the injury and the reported symptoms mentioned above (included in the four sections of the care procedure). The diagnostic strategy for tetraplegic (quadriplegic) patients is illustrated in Figure 1. The network structure is based on information derived from DIMITRA's rule-based system and information derived from literature specialising on the caring procedure to be followed on wheelchair users with spinal injury [8].

The diagnostic reasoning is based on Bayesian Networks and updates the probabilities of diagnoses when provided with any evidence regarding patients' signs and symptoms. The model regarding the joint probability of disease $d$ and signs/symptoms $s$ implied by the DIMITRA-Pro system can be formally written as:

$$
P(s, d)=P(s \mid d) P(d)=\left[\prod_{i} P\left(f_{i}\right) \mid d\right]\left[\prod_{k} P\left(d_{k}\right)\right]
$$

where $s$ and $d$ can be modelled using 2 different node types, depending on the natural representation of each node which will be sufficient for the description of all node input for the base layer. Those types are:

- Discrete nodes: This type is appropriate for nodes where the answer can be selected from a small set of discrete choices (like YES/NO answers). For each possible choice, a confidence measure is attached to the node.
- Continuous nodes: This type suits nodes where continuous domain measurements are to be taken - such as temperature. For such nodes, a conditional probability distribution is attached to the node so that the continuous measurement (in this case, the patient's temperature) received at the input can be converted into a real number representing a probability measurement of the symptom. In our example, we would expect that the lower the patient's temperature is measured, the higher the confidence measure for hypothermia has to be - but also the lower the temperature confidence will be. However, a normal temperature would have to yield a low confidence measure for both symptoms.
The above reasoning was implemented using the commercially available AgenaRisk software package $[1]$.


# 3. Model Parameters 

One difficulty regarding the use of Bayesian Networks for modelling causal relationships in realworld cases is that empirical data for conditional probabilities are often not available [10].

In DIMITRA-Pro, conditional probabilities of signs and symptoms given diagnoses were elicited from 11 experts, all qualified staff nurses from the Stoke Mandeville Hospital, using questionnaires. Experts were asked to indicate the assessments for all conditional probabilities pertaining to a single variable given a single conditioning context on the same line. In communicating a conditional probability to our domain, we do not use mathematical notation - the requested probability is translated into a fragment of text instead. To support the experts in their assessment task, a verbalnumerical sliding response scale [15] was provived.

The desired conditional probabilities of the signs and symptoms given the diagnoses is calculated using the trimean [12]. To model the conditional probabilties of multiple diagnoses on a single finding we use the noisy-OR gate [13]. Even though some studies advocate that subjective probabilities may not be the best for diagnostic purposes $[6,16]$, other studies suggest that it is possible to add these estimates with empirical data as they become available $[9,10]$.

![img-0.jpeg](img-0.jpeg)

Figure 1. The structure of the DIMITRA-Pro model for the tetraplegic patients


Table 1. Example results of the DIMITRA-Pro network used as 24-hour consultation tool for 4 months.

# 4. Diagnostic Performance 

In order to verify the diagnostic value of the DIMITRA-Pro network, two experiments were carried out using real-world cases. The network was tested on a total of 19 cases. In 17 of them DIMITRA-Pro delivered correct diagnoses - a correct diagnosis rate of $89.4 \%$. In the first experiment the model was used by a high level patient and carer as a 24 -hour consultation tool for a 4 -month period. Illustrative results are presented in Table 1, showing the symptom observation by the patient and carer, the diagnosis by the carer and that provided by the system. In the diagnoses the arrow $(\rightarrow)$ indicates 'leads to'. In the second experiment the model was tested using cases from different patients. These results are shown in Table 2. The results are encouraging, although a much larger number of tests cases would need to be evaluated to draw firm conclusions.

## 5. Conclusions

In this work, a probabilistic model for supporting the caring procedure to be followed for wheelchair users with spinal injury was presented. The proposed model consists of 21 conditions (diagnoses) and 49 findings (signs and symptoms). Given a patient's findings, the model computes the probability distribution over the possible conditions associated with the caring procedure. The network structure and numerical parameters were elicited from the rule-based DIMITRA system and was based on the knowledge of the domain experts.

## Acknowledgments

The authors would like to acknowledge the invaluable help of the qualified nurses from the National Spinal Injury Center, Stoke Mandeville, Aylesbury, UK for providing their estimates of the probabilities of diagnoses given the relevant signs and symtoms for conditions encountered in the field of medical care for patients suffering from spinal injury.
