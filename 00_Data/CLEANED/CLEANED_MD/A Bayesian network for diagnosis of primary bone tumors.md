# A Bayesian Network for Diagnosis of Primary Bone Tumors 

Charles E. Kahn Jr, John J. Laur, and G.F. Carrera

The authors developed a Bayesian network to differentiate among five benign and five malignant neoplasms of the appendicular skeleton using the patient's age and sex and 17 radiographic characteristics. In preliminary evaluation with physicians in training, the model identified the correct diagnosis in 19 cases ( $68 \%$ ), and included the correct diagnosis among the two most probable diagnoses in 25 cases (89\%). Bayesian networks can capture and apply knowledge of primary bone neoplasms. Further testing and refinement of the model are underway. Copyright (c) 2001 by W.B. Saunders Company

ABOUT 2,500 new cases of malignant primary bone tumors are diagnosed each year in the United States; they account for less than $0.2 \%$ of all cancers. ${ }^{1}$ Benign and malignant skeletal lesions can be distinguished by several characteristics, including age at presentation and the radiographic features demonstrated by the lesion. Our goal was to begin to create a repository of probabilistic data about these relatively rare lesions to enable development of Internet-based resources for education and decision support.

Bayesian networks-also called belief networks or causal probabilistic networks-use the techniques of probability theory to reason under conditions of uncertainty. ${ }^{2,3}$ Each variable in a Bayesian network has two or more possible states with their associated probability values. For each variable, these probability values sum to 1 . For example, the variable "matrix ossification" has two states: "present" and "absent." Each variable can be set completely ("matrix ossification is present"), partially ("the probability of matrix ossification is 0.8 "), or left as unknown. In this-way, the values of the nodes can accurately represent a physician's current state of knowledge and uncertainty. The connections between variables represent direct influences, expressed as conditional probabilities,

[^0]such as sensitivity and specificity. From these probabilistic influences, one can infer the posterior probability of unknown variables from the evidence specified in the known variables.

Bayesian networks can express the relationships between diagnoses, physical findings, laboratory test results, and imaging study findings. Physicians can determine the a priori ("pre-test") probability of a disease, and then incorporate laboratory and imaging results to calculate the a posteriori ("post-test") probability. ${ }^{3}$ In radiology, Bayesian networks have been applied to magnetic resonance imaging (MRI) diagnosis of liver lesions, ${ }^{4}$ selection of imaging procedures for patients with suspected gallbladder disease, ${ }^{5}$ and mammographic diagnosis. ${ }^{6,7}$ Although not formulated as a Bayesian network, Lodwick in 1965 described a probabilistic approach to diagnosis of bone tumors. ${ }^{8}$

We sought to construct a Bayesian network, called OncOs, to represent diagnostic information about solitary skeletal lesions. The initial version of OncOs was designed to differentiate among ten solitary lesions of the appendicular skeleton: osteosarcoma, osteochondroma, chondrosarcoma, giant cell tumor, osteoid osteoma, Ewing's tumor, malignant lymphoma, nonossifying fibroma (fibrous cortical defect), chondroma, and fibrosarcoma. The model incorporated the patient's age, sex, and 14 radiographic characteristics. Radiographic features included the involved bone and the lesion's location within the bone both longitudinally and axially (Table 1). Conditional probability data were acquired from several reference texts. ${ }^{9-11}$ We used the Hugin inference shell (version 5.4; Hugin A/S, Aalborg, Denmark; http://www.hugin.dk/) to create and run the model.

To evaluate OncOs' usability, five medical students were recruited to receive limited training in the vocabulary and radiographic features of bone tumors. Twenty-eight cases were selected from teaching atlases; four of the students reviewed five cases each and one reviewed eight cases. The students described the cases' features and encoded them into OncOs using a standardized vocabulary and format. Based on this input, OncOs identified the correct diagnosis


[^0]:    From the Department of Radiology, Medical College of Wisconsin, Milwaukee, WI.

    Address reprint requests to Charles E. Kahn Jr, MD, Department of Radiology, Medical College of Wisconsin, 9200 W Wisconsin Ave, Milwaukee, WI 53226. E-mail: kahn@mcw.edu Copyright (c) 2001 by W.B. Saunders Company 0897-1889/01/1402-1013535.00/0 doi:10.1053/jdim.2001.23816

Table 1. Components of the OncOs Model


in 19 cases ( $68 \%$ ), and included the correct diagnosis among the two most probable diagnoses in 25 cases $(89 \%)$.

Further testing and refinement of the model are underway. We also are working to integrate the

OncOs knowledge base with BANTER (Bayesian Network Tutoring and Explanation), a generalized system that uses knowledge in the form of a Bayesian network to generate quiz questions and explain its reasoning. ${ }^{12}$
