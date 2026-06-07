# Automation of Information Security Risk Assessment 

Berik Akhmetov, Valerii Lakhno, Vitalyi Chubaievskyi, Serhii Kaminskyi, Saltanat Adilzhanova, and Moldir Ydyryshbayeva


#### Abstract

An information security audit method (ISA) for a distributed computer network (DCN) of an informatization object (OBI) has been developed. Proposed method is based on the ISA procedures automation by using Bayesian networks (BN) and artificial neural networks (ANN) to assess the risks. It was shown that such a combination of BN and ANN makes it possible to quickly determine the actual risks for OBI information security (IS). At the same time, data from sensors of various hardware and software information security means (ISM) in the OBI DCS segments are used as the initial information. It was shown that the automation of ISA procedures based on the use of BN and ANN allows the DCN IS administrator to respond dynamically to threats in a real time manner, to promptly select effective countermeasures to protect the DCS.


Keywords-information security; audit; Bayesian network; artificial neural networks

## I. INTRODUCTION

WITH the growth of cyber-attacks rate, increase in attack scenarios complexity, the problem of reliable information security (IS) for many objects of informatization (OBI) has become more relevant than ever.
Note that in comparison to the 80s-90s of the last century the loudest cyber-attacks were associated with the selfish motives of the attackers, and the question in many cases concerned the theft of funds from bank cards or industrial espionage by hacking the information systems of competitors, then at the beginning of the 20th century, the situation changed dramatically.
Without going into a detailed analysis of well-known and technically difficult to implement cyberattacks, for example, Stuxnet [1] or "Moonlight Labyrinth" [2], etc., it was noted that nowadays the selfish motives of the attackers are fading into the background. In the context of the global information confrontation between the leading world states, globalization and fierce competition, the issues of providing information security for OBI of any scale have become a priority task for many companies. Nowadays, leading companies build their

[^0]business processes based on the widespread use of information technology (IT) and information systems. They take into account the existing landscape of cyber threats.
The problem of providing IS OBI of any scale is complex. Such an integrated approach includes a fairly large list of necessary measures aimed at ensuring IS OBI. For example, it includes activities aimed at:

1) search for the optimal strategy for investing into information security means (ISM);
2) formation of the optimal composition of the information security system along the contours of the information security $O B I$;
3) risk assessment for OBI information assets;
4) etc.

Many researchers [3, 4] include the organization of an effective IS audit (hereinafter ISA) for OBI in this list of activities. However, if the issues of technical security of information security OBI are currently well studied and many new approaches for ensuring information security are based on innovative technologies, then the processes of conducting ISA remain a new area for researchers. Indeed, modern technologies have brought to the field of information security approaches based on cognitive technologies [5, 6], neural networks [7, 8], evolutionary algorithms [9, 10], etc. At the same time, most research in the field of organization and conduction of ISA focuses primarily on the organizational side of the issue. At the same time, not enough attention, in our opinion, is paid precisely to the problems of developing new methods and models of ISA based on new technologies, for example, on the use of artificial neural networks (ANN) in ISA procedures.
All of the above has determined the relevance of research aimed at studying the prospects of using the ANN apparatus in ISA procedures. First of all, this concerns the ISA of distributed computing networks (DCN) OBI, which today have become the basis of many business processes of companies and organizations.

## II. LITERATURE REVIEW

In works [11, 12] it was shown that the organization of an effective information security management system (ISMS) OBI should be focused on the priority of the problem of information security risk management.
In works [12-14] it was shown that the internal audit function (IAF) can play an important role in ensuring IS OBI. ISA procedures allow owners of information assets (IA) to better understand how they can improve the information security of their enterprise, company or organization. However, these works do not touch upon the practical aspects of the use of


[^0]:    The work was carried out within the framework of the grant study AP08855887-OT-20 "Development of an intelligent decision support system in the process of investing in cyber security systems."

    Berik Akhmetov is with Yessenov University, Aktau, Kazakhstan (e-mail: berik.akhmetov@yu.edu.kz)

    Valerii Lakhno is with National University of Life and Environmental Sciences of Ukraine, Kyiv, Ukraine (e-mail: lva964@nubip.edu.ua)

    Vitaliy Chubaievskyi and Serhii Kaminskyi are with Kyiv National University of Trade and Economics, Kyiv, Ukraine (e-mail: [chubaievsyi_vi, s.kaminskyj] @knute.edu.ua)

    Saltanat Adilzhanova and Moldir Ydyryshbayeva are with Al-Farabi Kazakh National University, Almaty, Kazakhstan (e-mail: asaltanat81@gmail.com, moldir_ydyryshbaieva@mail.ru)

intelligent technologies in the issues of ISA OBI. In works [15, 16], the authors noted that for ISA OBI, as a rule, a unique data set is used, which has been studied by experts. After that, experts develop recommendations that can affect the effectiveness of IS organization at OBI. However, the authors do not make unequivocal conclusions about the advisability of using IT in ISA procedures. Works [17, 18] focus on the principles and objectives of ISA enterprises. However, in these works, the question of the potential of using new IT to increase the efficiency of ISA remains unclear.
In works [19, 20], a model for assessing the risks of violation of the IS policy (hereinafter PIS) OBI, based on the use of fuzzy cognitive maps, is proposed. However, this approach, although it makes it possible to take into account many IS threats, remains difficult to be algorithmic. This shifts all the main work to the expert, and, therefore, increases the likelihood of a subjective assessment of the results of ISA OBI.
In [21-23], practical aspects of the implementation of ISA based on ANN are considered. The issues of training the ANN and its testing in the course of the ISA of a specific OBI are also considered. However, many questions have not been disclosed in the work. For example, the work lacks a statistical assessment of the ANN learning outcomes. There is also no generalization of the ability developed by the ANN for the ISA tasks of different OBIs.
The possibility of automating ISA procedures by using various kinds of decision support systems (DSS) and other IT is considered in the works [24-26]. However, the authors noted that these studies have not yet been completed and it is still premature to talk about full-scale automation of the OBI ISA.
As shown in [23, 29, 30], an integral part of ISA procedures is the analysis and assessment of IS risks for OBI. Also, an IS risk assessment should be performed at the design stage of IS for OBI. To solve this problem, the authors of $[29,31]$ used the apparatus of fuzzy logic (FL) and ANN. However, the authors failed to provide convincing arguments for how the posteriori probabilities are estimated during the implementation of IS threats for OBI in a dynamic confrontation with the attacking side.
All of the above has determined the relevance of new research aimed at developing new models and developing the methodology for conducting ISA OBI. The research focuses on using the potential of ANNs and Bayesian networks (BNs) when conducting ISA.

## III. THE PURPOSE AND OBJECTIVES OF THE STUDY.

The aim of the study is to increase the degree of reliability of the results obtained in the course of ISA by using ANN and BN in these procedures.
Research objectives:

1) build and train ANN to automate the ISA procedure and obtain the values of the risks of IS violation OBI.
2) test the developed ANN as an element of an intelligent system for automating ISA OBI procedures.

## IV. METHODS AND MODELS

The dynamically changing landscape of cyber threats for OBI, especially critical computer systems (CCS), forces the defense side to actively develop models and methods of
continuous ISA. In conditions of dynamic confrontation with the attacking side, one of the priority tasks of the ISA is the task associated with the analysis and forecasting of risks.
In works [21, 23, 27-30], devoted to the prospects of using ANN for the tasks of auditing information security risks, the emphasis is on the situation when auditors have sufficiently large data samples. Note that in the framework of our study, we do not touch upon the discussion of the general limitations of the ANN as a tool for auditing and assessing the risks of information security OBI. This analysis has been performed by many authors in the past.
In accordance with [32, 33], the size of the IS risk for OBI can be determined as follows:

$$
R=f(A, T, V)
$$

where $A, T, V-$ parameters, respectively, characterize the value of the information asset (IA), the likelihood of threats and the likelihood of vulnerabilities.
As a rule, in the course of ISA, the values of the IS breach risks for OBI as a whole are calculated - $R_{F R}$.
To do this, you can use the following dependency:

$$
R_{F R}=\sum_{n=1}^{N} R_{F R_{C u}}
$$

where $N$ - the number of DCN segments, see Fig.1;
$R_{F R_{C u}}$ - IS level for a separate DCN segment.
The value can be determined using the following dependency:

$$
R_{F R_{C u}}=\sum_{s t=1}^{S T} P_{\Sigma}^{T} \cdot\left(\frac{I A V_{S T}}{I A V_{\Sigma}}\right)
$$

where $S T$ - is the number of IS threat sources for the OBI DCN segment;
$P_{\Sigma}^{T}-$ the resulting value of the probability of the implementation of threats for the IS of the DCN segment;
$I A V_{S T}, I A V_{\Sigma}-$ accordingly, the cost of the IA segment and OBI (DCN) as a whole.
The value $P_{\Sigma}^{T}$ can be found like this:

$$
P_{\Sigma}^{T}=1-\prod_{s t}\left(1-P_{S T}^{T}\right)
$$

where $P_{S T}^{T}$ - is the value of the probability of realizing a threat to IS within a specific DCN segment. These values are determined, for example, based on building a threat model for certain types of threats and classes of attacks.
When carrying out ISA, and, accordingly, risk analysis, an expert evaluates a priori probabilistic information about the possibility of a threat being realized. However, as new information is studied, the results obtained in the course of the ISA can both confirm and refute the a priori information.
In the proposed solution for assessing information security risks, it is proposed to use Bayesian trust networks (BN) at the first stage [34, 36-38].
For example, for the BN shown in Fig. 2, a priori conditional probabilities of occurrence of certain events were given. After that, the BS was trained on the basis of statistical data [35].

Data were taken based on information on the US National Vulnerability Database website.

![img-0.jpeg](img-0.jpeg)

Fig. 1. DCN architecture for OBI (as an ISA object)
![img-1.jpeg](img-1.jpeg)

Fig. 2. Bayesian search and visualization of simulation results in the Genie package (v2.0)

In such a BN, the target variables are potential threats to which the OBI DCN may be vulnerable. All the variables are shown in Fig. 2, discrete. Each variable (or threat) can take one of five values, each of which corresponds to the probability of its realization: trivial, low, medium, high, critical (respectively, insignificant, low, medium, high, critical). The rest of the variables in the BN are characteristics. A set of these characteristics makes it possible to identify a threat and determine its likelihood. These variables are divided into categories that classify information security threats or describe different types of computer intruders. For example, consider a BN for the threat of unauthorized access (UAA) to information resources in the DCN OBI: 1) The purpose of the UAA. Violation of confidentiality (p_confidentiality), integrity (p_integrity), or availability (p_availability) of information resources of the DCN OBI is considered; 2) Position of the tamper source (n_network). Three source categories were
accepted: intra-segment, intersegment, external; 3) the need for authentication to implement the threat (a_ authentication); 4) Attacker's qualification (a_qualification): high, medium, low.
Table 1 shows an example of a piece of data for describing the conditional probabilities for the threat "Data modification in the information system" OBI.
Similar tables of conditional probabilities were constructed in the course of the study for other classes of information security threats.
At the next stage of ISA automation, ANN is used.
In the process of developing a method for conducting ISA, which would be based on obtaining numerical assessments of the risks of IS violation using ANN, it is necessary to generate data for a training sample. Next, the ANN structure is selected.
An example of a developed ANN for ISA automation is shown in Fig. 3.

Table 1
An Example of a Part of the Table of Conditional Probabilities for the Threat "Data Modification in the Information System"


Input layer Hidden layer Output layer
![img-2.jpeg](img-2.jpeg)

Fig. 3. ANN topology for ISA automation
An example of a training sample fragment for the network topology shown in Fig. 4 is shown in Table 2.
DCN was conditionally divided into 4 segments - Each segment corresponds to the network of the head office and separate structural divisions.
ANN includes 10 neurons in the hidden layer and four neurons in the output layer. When training a multilayer perceptron, an error backpropagation algorithm was applied.

The value of information assets (IA) can be set by the owner. The owner of the IA determines their value based on their usefulness for their business processes. And also considering the importance of the IA and the potential losses in the event of their loss.
![img-3.jpeg](img-3.jpeg)

Fig. 4. OBI network architecture

TABLE II
Fragment of the Training Set for ANN


Note that when developing the ANN, the specificity of the training sample was taken into account. The input of such an ANN is data obtained, for example, from antivirus software, firewalls, intrusion detection systems, etc. These data, respectively, act as a source of information when assessing the overall network activity and load, and also show the level of potentially dangerous activity.

## V. COMPUTATIONAL EXPERIMENT

Computational experiments were carried out on the basis of the DCN of two universities - the National University of Life and Environmental Sciences of Ukraine (or NUBIP of Ukraine, Kyiv) and Yessenov University (Aktau, Kazakhstan).
The topology of the DCN of NUBIP Ukraine is shown in Fig.4.
Computational experiments for the designed ANN were performed using the Neural Network Toolbox for MATLAB

package. The training sample included from 1000 to 1500 samples. Test sample from 500 to 1000 samples. A graph illustrating the learning process of a neural network is shown in Fig. 5.
As a result, graphs of surfaces are obtained, for example, as in Figure 6.
![img-4.jpeg](img-4.jpeg)

Fig. 5. Graph of the surface of the output values of IS risks
![img-5.jpeg](img-5.jpeg)

Fig. 6. Graph of the surface of the output values of IS risks

## VI. DISCUSSION OF THE RESULTS OF THE COMPUTATIONAL EXPERIMENT

The results of computational experiments have shown that the initial dependences (1) - (4) can be fairly accurately approximated using artificial neural networks. It was found that with an increase in the number of neurons over 8 , the complexity and degree of nonlinearity of the output display of the risk assessment parameters increases. When using artificial neural networks in ISA procedures, it is necessary to take into account the degree of expert's confidence in the previously formed training sample. If there is not enough data for training, or some of them are found unreliable, it is advisable to reduce the number of neurons. This allows you not to retrain the artificial neural networks.
Also, as a result of computational experiments in Genie and Matlab environments, it was shown that the proposed approach to assessing information security risks during an audit allows for a more accurate selection of information security tools for distributed computing networks circuits. Artificial neural networks used to assess and predict of information security risks during the audit not only allows you to effectively select countermeasures to protect OBI IS, but in general to build an effective ISMS adaptable to new threats. The cost reduction was at least $15 \%$ in comparison with the methods of risk assessment in the course of information security audit, which are described in the works [29, 32-34].
The prospect of research is the implementation of the developed artificial neural networks into the DSS, which can also be used in the course of ISA OBI. The task of the DSS will be to support options for solutions that will allow the administrator of the information security of the distributed computing networks to act proactively. For example, as such preventive measures, you can consider: stopping or restarting servers, restarting virtual machines, etc.
The combined use of the Bayesian networks apparatus and the artificial neural networks makes it possible to automate the information security audit procedures, including for rather complex scenarios of attacks on the distributed computing networks.

## CONCLUSION

Within the framework of the studies carried out, the following main results were obtained:

The information security audit method was developed, based on the automation of audit procedures by using the Bayesian networks apparatus and the artificial neural networks to assess the of information security risks. It is shown that such a combination makes it possible to quickly determine the actual risks for information security OBI in the course of information security audit. At the same time, data from sensors / sensors of various hardware and software means of information protection in the OBI DCN segments are used as the initial information.

Automation of ISA procedures based on the use of BN and ANN allows the information security administrator of the DCN to respond dynamically to threats in a timely manner.
