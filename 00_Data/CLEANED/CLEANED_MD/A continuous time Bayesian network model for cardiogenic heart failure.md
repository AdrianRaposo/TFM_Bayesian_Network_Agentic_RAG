# A continuous time Bayesian network model for cardiogenic heart failure 

E. Gatti $\cdot$ D. Luciani $\cdot$ F. Stella


#### Abstract

Continuous time Bayesian networks are used to diagnose cardiogenic heart failure and to anticipate its likely evolution. The proposed model overcomes the strong modeling and computational limitations of dynamic Bayesian networks. It consists of both unobservable physiological variables, and clinically and instrumentally observable events which might support diagnosis like myocardial infarction and the future occurrence of shock. Three case studies related to cardiogenic heart failure are presented. The model predicts the occurrence of complicating diseases and the persistence of heart failure according to variations of the evidence gathered from the patient. Predictions are shown to be consistent with current pathophysiological medical understanding of clinical pictures.


Keywords Cardiogenic heart failure $\cdot$ Continuous time Bayesian networks $\cdot$ Decision support system

## 1 Introduction

Recent technological developments in the field of Information and Communication Technology have offered an extremely important opportunity to operational health care management [1]. Because of this, decision support systems (DSSs) are becoming increasingly attractive for physicians, as they can offer great benefits without necessarily daring to replace human judgement [2-4]. The contribution of DSSs in health care has been far-reaching and still evolving as evidenced by the

[^0]
[^0]:    E. Gatti $\cdot$ F. Stella ( $\boxtimes$ )

    DISCo, Università degli Studi di Milano-Bicocca, Viale Sarca 336, 20124 Milano, Italy
    e-mail: stella@disco.unimib.it
    D. Luciani

    Laboratorio di Epidemiologia Clinica, Istituto di Ricerche Farmacologiche Mario Negri, Via La Masa 19, 20156 Milano, Italy

large number of references that appear in PUBMED, a widely used health care search engine. Increasingly, health care costs make it imperative for hospitals and physicians to make optimal decisions to improve the quality and the efficiency of health care delivery. Recent advances in DSSs have provided a prominent and growing role of DSSs in improving clinical as well as administrative decision making [5].

Bayesian networks (BNs) [6, 7] have become a popular representation in Artificial Intelligence for encoding uncertain knowledge [8, 9]. As inferential engines on even a large set of outcomes of interest, BNs often represent the core of flexible DSSs, like influence diagrams or, more generally, decision graphs [7]. Their task concerns the selection of decision options which are optimal in the light of both the knowledge on the modelled domain and the observations collected in specific cases, in which the user is offered a normative interpretation of an undetermined state [10]. Even if not equipped with decision analysis operators, BNs may nevertheless offer to the decision maker crucial information about the impact of observations on a set of variables which influence the decision.

In medicine, causal explanations of patient manifestations and future outcomes can be regarded as the main variables of interest, since they enable, respectively, diagnostic and prognostic reasoning. Medical literature offers several examples of models used for reasoning under uncertainty in different medical fields [11]. QMR-DT [12] was proposed for internal medicine, Pathfinder and Intellipath [13] for pathology, Qualicon [14], Localize [15], Myosys [16], Myolog [17], Electrodiagnostic Assistant, Neurop [18], Kandid [19] and Munin [20] for neuromuscular disorders.

However, with many medical problems the time duration of events concerning patient conditions cannot be dismissed like in the above static models. Partially observable Markov decision processes (POMDPs) can in principle be exploited to formalise the temporal planning of clinical management. However, their practical application is hampered by their coarse representational granularity and complex formulation. Graphical representations were advocated in order to improve both the computational tractability and the representation of POMDPs [21]. Since then, the use of temporal graphical models has appeared in the field of pediatric cardiology [22], abdominal pain [23], insulin administration [24] and ventilator-associated pneumonia [25]. Most of these applications are based on dynamic Bayesian networks (DBNs) [26], which represent the standard extension of BNs when dealing with dynamical systems.

DBNs discretize the time to model a dynamical system with several time slices. Each time slice is associated with a BN fragment which models the transition from the state at time $t$ to the state at time $t+1$. DBNs describe the state of the dynamical system at discrete time points, but do not model time explicitly. This makes it very difficult to query a DBN for a distribution over the time at which a particular event takes place. Furthermore, in the case where the system consists of processes which evolve at different time granularities and/or the obtained observations are irregularly spaced in time, the inference process may become computationally intractable.

In all cited dynamic models, different strategies were exploited to deal with the computational burden imposed by the temporal dimension, such as narrowing the temporal windows, including past observations [25], preliminary detection of

critical time of change [23] and focusing on the most relevant variables as the process evolves [22]. Each strategy seems appropriate for a specific task and domain to represent, whereas no general solution emerged as appropriate for all domains.

In this paper continuous time Bayesian networks (CTBNs) [27] are used to diagnose acute cardiogenic heart failure while overcoming the main limitations of DBNs. In spite of the medical advances, cardiogenic heart failure remains one of the most common, costly, disabling and deadly medical conditions encountered by a wide range of physicians and surgeons in both primary and secondary health care. Indeed, from 1 to $2 \%$ of the adult population suffers from heart failure, but the numbers are increasing due to the aging of the population, as the disorder mainly affects people over 65 years old [28].

The proposed CTBN includes both unobservable variables and clinical manifestations which are directly accessible through medical investigation. Inference on unobservable variables such as myocardial infarction and cardiac pump impairment is the focus of diagnostic judgement as well as prognostic task related to the occurrence of shock and heart failure persistence. Three scenarios serve the purpose to show how the developed model can be used for both diagnosis and prediction of complicating disorders. The described scenarios include point evidence, usually also available with DBNs, and interval evidence, which is one of the main modelling advantages of CTBNs over DBNs. The CTBN model represents the cardiovascular system at a level of detail which appears appropriate to explain its main causes, specifically, an underlying chronic weakness of the cardiac muscle and a large myocardial infarction.

The rest of the paper is organized as follows. Section 2 gives the basics of CTBNs. In Sect. 3 the acute cardiogenic heart failure model is presented, and how it can be exploited for reasoning under uncertainty over time is described. Three evidence scenarios show the capability of the proposed model to assist the clinician in both diagnostic and prognostic tasks. Section 4 discusses the proposed approach to cardiogenic heart failure, while Sect. 5 draws conclusions and proposes further research directions.

# 2 Continuous time Bayesian networks 

CTBNs explicitly represent temporal dynamics and allow us to recover the probability distribution over time when specific events occur. CTBNs are based on homogeneous Markov processes, while they exploit BNs to provide an intuitive language to describe complex dynamical systems.

CTBNs have been used to model the presence of people at their computers together with the specific application they are using (e.g., email, word processing, web browsing, etc...) [29]. They have been successfully used for modeling and analyzing the reliability of dynamical systems [30], for network intrusion detection [31] and for modeling social networks [32].

### 2.1 Homogeneous and conditional Markov processes

CTBNs are based on finite state continuous time homogeneous Markov processes, i.e. stochastic processes in which the transition intensities do not depend on time.

Let $X$ be a random variable whose state can take $k$ discrete values $\operatorname{Val}(X)=\left\{x_{1}, \ldots, x_{k}\right\} . X$ changes its state continuously over time $t$. A homogeneous Markov process $X(t)$ is described with its intensity matrix:

$$
\boldsymbol{Q}_{X}=\left[\begin{array}{ccccc}
-q_{1} & q_{12} & \ldots & \ldots & q_{1 k} \\
q_{21} & -q_{2} & \ldots & \ldots & q_{2 k} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
q_{k 1} & q_{k 2} & \ldots & \ldots & -q_{k}
\end{array}\right]
$$

The matrix $\boldsymbol{Q}_{X}$ allows us to describe the transient behaviour of the random variable $X$. If at time $t=0$ the random variable is in state $x_{i}$, then it stays there for an amount of time which is a random variable exponentially distributed with parameter $q_{i}$. Therefore, the probability density function together with the distribution function for $X(t)$ to remain in state $x_{i}$ are as follows:

$$
\begin{aligned}
& f(t)=q_{i} \exp \left(-q_{i} t\right) \\
& F(t)=1-\exp \left(-q_{i} t\right)
\end{aligned}
$$

where $t \geq 0$. It is worthwhile to mention that the expected time of transitioning from state $x_{i}$ is $\frac{1}{q_{i}}$, while when transitioning from state $x_{i}$ the random variable $X$ shifts to state $x_{j}$ with probability $\frac{q_{i j}}{q_{i}}$.

However, the size of the intensity matrix $\boldsymbol{Q}_{X}$, i.e. the state space of the Markov process, grows exponentially with the number of variables and with their cardinality. This makes the above representation infeasible for all but the smallest spaces, i.e. models including a very small number of variables. Therefore, to compose Markov processes in a larger CTBN model, the concept of conditional Markov process must be introduced.

A conditional Markov process is a particular kind of inhomogeneous Markov process, in the sense that, for any given random variable, the intensities are a function of the current values of a particular set of other variables, which also evolve as Markov processes. Therefore, intensities vary over time but not as a direct function of it. To clarify how the conditional Markov process is described, let $X$ be a random variable whose domain is $\operatorname{Val}(X)=\left\{x_{1}, \ldots, x_{k}\right\}$ and assume that it evolves as a Markov process $X(t)$. Furthermore, assume that the dynamics of $X(t)$ are conditionally dependent from a set $V$ of random variables evolving over time. Then the dynamics of $X(t)$ can be fully described by means of a conditional intensity matrix (CIM), which can be written as follows:

$$
\boldsymbol{Q}_{X \mid V}=\left[\begin{array}{ccccc}
-q_{1}(V) & q_{12}(V) & \ldots & \ldots & q_{1 k}(V) \\
q_{21}(V) & -q_{2}(V) & \ldots & \ldots & q_{2 k}(V) \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
q_{k 1}(V) & q_{k 2}(V) & \ldots & \ldots & -q_{k}(V)
\end{array}\right]
$$

A CIM is a set of intensity matrices, one intensity matrix for each instance of values $v$ to the set of variables $V$. Using the BN's terminology, the variables belonging to the set $V$ are called the parents of the random variable $X$. This set is usually denoted

$p a(X)$, while in the case where the parent set $p a(X)$ is empty, the CIM is simply a standard intensity matrix.

# 2.2 The continuous time Bayesian network model 

Conditional intensity matrices (CIMs) allows us to model local dependencies between random variables, which is a fundamental aspect of both BNs, DBNs and CTBNs. Given a set of CIMs they can be put together to obtain a single structured model which fully describes the aspects of the evolution of a multivariate probability distribution. A CTBN consists of two main components: (1) an initial probability distribution and (2) the dynamics which rule the evolution over time of the joint probability distribution associated with the CBTN.

Definition 1 [27] (Continuous Time Bayesian Network). Let $\boldsymbol{X}$ be a set of local variables $X_{1}, \ldots, X_{n}$. Each $X_{i}$ has a finite domain of values $\operatorname{Val}\left(X_{i}\right)$. A CTBN $\aleph$ over $\boldsymbol{X}$ consists of two components: The first is an initial distribution $P_{X}^{0}$, specified as a Bayesian network $\mathcal{B}$ over $\boldsymbol{X}$. The second is a continuous transition model, specified as

- a directed (possibly cyclic) graph $G$ whose nodes are $X_{1}, \ldots, X_{n} ; p a\left(X_{i}\right)$ denotes the parents of $X_{i}$ in $G$.
- a conditional intensity matrix, $Q_{X_{i} \mid p a\left(X_{i}\right)}$, for each variable $X_{i} \in X$.

CTBNs allow, differently from BNs and DBNs, cycles in the graph $G$. Therefore, arcs directed from node $X$ to node $Y$ and directed from node $Y$ to node $X$ imply that the dynamic of the random variable $X$ depends on $Y$ as well as the dynamic of the random variable $Y$ depends on $X$. This dependency is analogous to a DBN model where we have an arc directed from $X(t)$ to $Y(t+1)$ and an arc directed from $Y(t)$ to $X(t+1)$.

### 2.3 Queries and inference

In [27] it has been shown that a CTBN $\aleph$ is a factored representation of a homogeneous Markov process described by the joint intensity matrix defined as

$$
Q_{\aleph}=\prod_{X \in X} Q_{X \mid p a(X)}
$$

Therefore, the CTBN $\aleph$ can be used to answer any query which can be answered by using an explicit representation of a Markov process. Indeed, given the set of CIMs $Q_{X \mid p a(X)}, X \in \boldsymbol{X}$ associated with the nodes of the CTBN model $\aleph$, it is always possible to form the joint intensity matrix $\boldsymbol{Q}_{\aleph}$ to answer queries just as we do for any homogeneous Markov process. Given the joint intensity matrix $\boldsymbol{Q}_{\aleph}$ and the initial distribution $P_{\aleph}^{0}$, many questions can be answered about the homogeneous Markov process $\aleph(t)$.

The distribution over the value of $\aleph(t)$ is given by

$$
P_{\aleph}(t)=P_{\aleph}^{0} \exp \left(Q_{\aleph} t\right)
$$

while the joint distribution over any two time points can be computed as follows:

$$
P_{\mathbb{R}}(s, t)=P_{\mathbb{R}}(s) \exp \left(Q_{\mathbb{R}}(t-s)\right), \quad t \geq s
$$

Inference in CTBNs can be performed by exact and approximate algorithms. Full amalgamation [27] is an exact algorithm that involves generating an exponentiallylarge matrix representing the transition model over the entire state space (1). Exact inference in CTBNs is NP-hard, and thus different approximate algorithms have been proposed. Nodelman et al. [33] introduced the Expectation Propagation (EP) algorithm which allows both point and interval evidence. It exploits message passing in a cluster graph, where the clusters contain distributions over trajectories of the variables through a duration. Saria et al. [34] presented a new EP-based algorithm which uses a flexible cluster graph architecture that fully exploits the natural time-granularity at which different sub-processes evolve. It also dynamically chooses the appropriate level of granularity to use in each cluster at each point in time. Alternatives are offered by sampling based inference algorithms. The importance sampling algorithm [35] computes the expectation of any function of a trajectory, conditioned on any evidence set constraining the values of subsets of the variables over subsets of the timeline. El-Hay et al. [36] developed a Gibbs sampling procedure for CTBNs which iteratively samples a trajectory for one of the components given the remaining ones. This approach naturally exploits the structure of the CTBN to optimize the computational cost of each step. This procedure is the first that can provide asymptotically unbiased approximations in such processes.

In this paper the inference task has been performed by using a proprietary software environment, designed and developed at the MAD laboratory. The CTBNs framework, developed under the MATLAB environment, offers the following functionalities:

- Load and compile; allows to load a CTBN model, to check its consistency and to allocate the required data structures for its management.
- Query; gets both point and interval evidence and includes them in a previously loaded and compiled CTBN model.
- Inference; offers the following algorithms; full amalgamation, EP and Gibbs sampling.
- Reporting; reports on all the statistics, including posterior probabilities, expected times to transition and expected number of transitions.

The correctness of approximate algorithms has been extensively tested exploiting full amalgamation and the CTBN-LRE environment [37].

# 3 Acute cardiogenic heart failure 

### 3.1 The continuous time Bayesian network model

Heart failure is a disorder in which the heart pumps blood inadequately. Because the heart pumps oxygenated blood into the arterial vessels while taking unoxygenated blood from the veins, the consequences of heart failure are twofold. On one side, it leads to a reduced blood flow with a lower delivered oxygen into the peripheral tissues, which in turn induces a reduced exercise capacity level and fatigue, or even

an irreversible condition known as shock, in which cells become unable to meet their metabolic functional needs. On the other side, heart failure induces congestion of blood both in the veins and lungs, leading to shortness of breath and the enlargement of organs. The first major advance for understanding the functional role of the heart, is due to William Harvey in 1628, who provided the first scientific demonstration of the circulation theory in his Exercitatio Anatomica de Motu Cordis et Sanguinis in Animalibus [38]. Since then, many authors have added fundamental contributions to explain the effects of various impairments of the cardiocirculatory system on human health. Figure 1 shows how these findings were given a graphical representation in terms of causal graphs, i.e. the qualitative component of the CTBN.

The meaning of nodes in Fig. 1, the information concerning their accessibility to medical investigation, the associated unit measure as well as the meaning of their states are listed in Tables 1 and 2.

The consistency of the qualitative component of the CTBN model, i.e. the set of directed arcs, is ensured by the current medical knowledge as described in an authoritative textbook in the field of cardiology [39]. The model includes both variables accessible to medical investigation and variables whose role was studied only within an experimental setting. Some of the contemplated observations (Fig. 1) are always accessible in the medical practice, like heart frequency (HF), mean arterial blood pressure (BP) or the occurrence of pedal edema (LPE). Others can be investigated only with the application of simple diagnostic procedures (Table 2). The strength of the heart in pumping blood into the vascular system is represented by the node Pump ([39], p. 412). Together with HF, the cardiac pump influences both the left and the right cardiac output (LCO and RCO) ([39], p. 413), as well as the left and right cardiac input (LCI and RCI) ([39], pp. 394-399). However, the amount of blood coming out from the ventricles is constrained by the availability of blood arriving in the left cardiac chamber. Thus, LCO depends on the BP within the tract between the pulmonary capillaries and the left ventricle (PCtoLVcirc) ([39], pp. 405-407), likewise RCO depends on the BP within the tract between the capillaries and the right ventricle (CBRVcirc) ([39], p. 408). The amount of blood entering the left and right heart do influences the pressure within two circulatory tracts, respectively, the vessels between the PctoLVcirc and the vessels between the CBRVcirc. Two nodes represent the amount of fluid exchanged with the external environment. The first is labelled blood volume (BV), being affected by the balance between the water intake (WI) and the urinary output (UO). As such, it is supposed to influence the pressure within the systemic venous tract (CBRVcirc) ([39], pp. 561-562). The second is labelled UO ([39], p. 574), which in turn depends on the BP occurring in the systemic arterial tract (LVtoCBcirc). Furthermore, some physiological mechanisms by which the organism restores the corrupted blood flow were contemplated. The model already accounts for a decrease in UO when the arterial BP is dropped to restore the normal pressure within the systemic arteries (LvtoCBcirc) ([39], p. 478). In addition, the neurovegetative control (SS) over both heart beat frequency and the systemic arterial resistance (VR) was also represented ([39], pp. 414-416). The node SS is sensitive to arterial BP (BP is regarded as a manifestation of LVtoCBcirc) and it has, in turn, an impact on both arterial vascular

![img-0.jpeg](img-0.jpeg)

Fig. 1 CTBN model for the acute myocardial infarction
resistance (VR) and HF ([39], pp. 417-418). Arterial VR might increase the systemic arterial pressure (LvtoCBcirc) ([39], p. 478). A node representing the persistence of symphatic neurovegetative activation (SS-pers) was included to account for the impairment of such a control mechanism when it lasts for too long (see the down-regulation described in [39], p. 440). As such, SS-pers is influenced by the SS node, while it influences the VR node. Some variables show the status of the cardiovascular system to a medical observer, specifically, whether some of its tract is stagnant. Pulmonary congestion (PulmCong) might be the result of stagnation in the pulmonary venous tract (RvtoPCcirc), whereby peripheral

Table 1 Meaning of the nodes of the acute myocardial infarction CTBN


congestion (PeriphCong) might be the result of stagnation in the systemic venous tract (CBRVcirc) (see Right-Sided vs. Left-Sided Heart Failure in [39], p. 473). These two phenomena manifest themselves respectively with shortness of breath (Dispn) ([39], pp. 475-477) and pleural effusion (PleuEff) on one side (see hydrothorax in [39], p. 480), and pedal edema (LPE) on the other side (see edema in [39], p. 480). The first scenario can be revealed directly by a low partial pressure of arterial oxygen (O2pa) (see forward failure [39], p. 472), whereas a severe reduction of blood perfusion gives rise to a fatal complicating condition known as shock

Table 2 Accessibility, unit measures and state meaning for the nodes of the acute myocardial infarction CTBN


(Shock) ([39], pp. 561-563). Heart failure is said to be cardiogenic when the cardiac muscle (Pump) is the organ from which the circulatory failure was triggered. In turn, acute myocardial infarction (AMI) might be the cause of cardiac impairment, although in most instances it is not. As any other infarction, AMI is due to lack of

arterial perfusion of the organ tissues. In case of AMI, obstruction of coronary arteries (CorObstr) occurs, whose blood supply comes from the main arterial system (LvtoCBcirc) (see ischemic heart disease [39], p. 435). One well known manifestation of coronary obstruction (CorObstr) is an intense chest pain ([39], pp. 1226-1228), called angina pectoris (Angor) ([39], p. 1235). Only when obstruction is both severe and lasting is there infarction, it manifests with the increase of cardiac enzymes (CardEnz) in the blood stream ([39], pp. 1239-1240) and, in functional terms, the impairment of the cardiac pump (Pump) ([39], p. 1230). In turn, intense pain stimulates the neurovegetative system with an increment of sympathetic activity and, therefore, of BP ([39], p. 1237) and HF ([39], p. 1238).

The quantitative component of the CTBN model, i.e. the CIM parameters, were elicited on the basis of the medical expertise of one of the authors (DL). Since each CIM includes a large number of parameters, whose interpretation is also far from being trivial, the attention was diverted on the parameters of the conditional probability tables (CPTs) that within a time interval of 10 s represent the impact of the parents on each node as their correspondent CIMs would do in continuous time. To further reduce the number of quantities to elicit, this task was accomplished in two steps. The first concerned the elicitation for each node of a conditional probability distribution based on a small number of parameters. The second addressed the quantification of the parameters. The time-interval of 10 s was deemed short enough to capture interesting dynamics, whereby the periodical changes of some physiological variables like cardiac alternation of the systole and diastole phases could be neglected. The distribution probabilities over all the parents' combinations for each node were parameterized in terms of well-known functions (Noisy-Or-Gate and multivariate Gaussian), according to the type of variable (discrete, binary, continuous) and considering whether an interaction among the parents was known to occur. Whenever the assumptions underlying a parametric distribution were found to be not consistent with medical knowledge on a specific node-parents relationship, the CPT was generated by a mixture of parametric distributions, each defined by a specialized set of parameters conditioned by combinations of the parents. The whole procedure from the Noisy-Or-Gate to the corresponding CIM for the node Pump is depicted in Fig. 2.

# 3.2 Inference 

To validate the model, we enter it with a set of patient observations whose explanations and consequences do generally appear straightforward to the medical profession. The current analysis encompasses the impact of clinical manifestations, i.e. BP, Dispn, HF, Angor and LPE, whereas associated laboratory or imaging observations, like CardEnz, O2pa, PulmCong and PleuEff, were only predicted along with other relevant outcomes, like the potential occurrence of shock (Shock). Since manifestations are derived from patient monitoring, they are referred to a time interval. For the purpose of our analysis, all cases are assumed to be normally hydrated cases, so WI was always kept to the normal state (mid).

![img-1.jpeg](img-1.jpeg)

$$
\text { NoisyOrDist }(\text { Pump }(t)=1,0.0005, A M I=1,0.035, \text { Pump }(t-\Delta t)=1,0.98)
$$

![img-2.jpeg](img-2.jpeg)

Fig. 2 Pump, from Noisy-Or-Gate to CPT to CIM

In light of the above consideration, the following three scenarios should provide some evidence on the ability of the model to explain the simulated observation and to predict their potential consequences.

# 3.2.1 Scenario 1 

The patient shows low $\mathrm{BP}(\mathrm{BP}=$ low $)$, an increased $\mathrm{HF}(\mathrm{HF}=$ high $)$, no chest pain (Angor $=$ absent $)$, pedal edema ( $\mathrm{LPE}=$ present) together with shortness of breath (Dispn $=$ present). All these manifestations last for 5 h . Therefore, the CTBN model is queried with the following interval evidence;

$$
\begin{aligned}
& {[\text { BP }=\text { low }, H F=\text { high }, \text { Angor }=\text { absent }, L P E=\text { present }, \text { Dispn }=\text { present, } W I} \\
& \quad=\text { mid }],
\end{aligned}
$$

for the time interval from 0 to 5 h , and with the interval evidence $[W I=m i d]$, for the time interval from 5 to 6 h .

The occurrence of pedal edema ( $\mathrm{LPE}=$ present) and shortness of breath (Disp $=$ present) would make the doctor keen on the diagnosis of congestive heart failure, involving both the right and the left heart side. The absence of angor (Angor $=$ absent $)$ would make a diagnosis of AMI very unlikely. The doctor is aware that such a condition, if left untreated, could lead to shock. Conditionally on the above

interval evidence, the posterior probability of shock (Shock $=$ present) attains the highest peak at the end of the observations, reaching a posterior probability value equal to 0.59 . A node belonging to the body internal state of the CTBN model for the AMI (Fig. 1), i.e. the node Pump shows a reduced pump strength. Indeed, the posterior probability value associated with Pump $=$ reduced is equal to 0.97 one hour after the initial observations (Fig. 3). Instead, the posterior probability value associated with the AMI $(\mathrm{AMI}=$ present $)$ remains low $(<0.01)$ during the whole period of interest (Fig. 4). This means that the patient is affected by primary congestive heart failure, whereas the adjective primary refers to a disease that is not the secondary result of another disease. The increased probability value of the low UO $(U O=$ low $)(0.22$ at the end of the observations) and the likely absence of cardiac enzymes (CardEnz $=$ present $)(<0.015)$ reinforces the above diagnosis.

# 3.2.2 Scenario 2 

The patient shows normal BP $(B P=$ mid $)$, increased HF $(H F=$ high $)$ and substernal chest pain (Angor $=$ present). The patient does not show pedal edema ( $L P E=$ absent), nor shortness of breath (Dispn $=$ absent $)$. These manifestations are supposed to last for 45 min . Therefore, the CTBN model is queried with the following interval evidence:

$$
\begin{aligned}
{[\text { BP } } & =\text { mid }, H F=\text { high }, \text { Angor }=\text { present }, L P E=\text { absent }, \text { Dispn }=\text { absent }, W I \\
& =\text { mid }]
\end{aligned}
$$

for the time interval from 0 to $45 \mathrm{~min}([0,0.75))$, and with the following interval evidence $[W I=$ mid $]$, for the time interval from 45 min to $6 \mathrm{~h}([0.75,6))$.
![img-3.jpeg](img-3.jpeg)

Fig. 3 Posterior for Pump and Shock under Scenario 1

![img-4.jpeg](img-4.jpeg)

Fig. 4 Posterior for AMI, UO and CardEnz under Scenario 1

Angor persisting (Angor $=$ present) for more than half an hour, is a classical marker of AMI. Therefore, the pump strength is expected to be unaffected, since there are no signs of heart failure ( $L P E=$ absent and Disp $=$ absent $)$. The model predicts, even after 1 h , a very low probability value ( 0.0052 ) of shock being present (Shock $=$ present) (Fig. 5). The probability of $\mathrm{AMI}(\mathrm{AMI}=$ present $)$ becomes as high as 0.45 after half an hour of persisting angor, but it decreases after the end of chest pain (from 0.49 to $<0.02$ after 15 min ) (Fig. 5). Cardiac enzymes follow a similar evolution. The probability of a reduced pump strength (Pump $=$ reduced $)$ remains low $(<0.10)$ (Fig. 5) during the time interval, likewise the probability of its associated manifestations, e.g. UO.

# 3.2.3 Scenario 3 

The patient shows normal $\mathrm{BP}(B P=$ mid $)$, with increased $\mathrm{HF}(H F=$ high $)$ and chest pain (Angor $=$ present). Like in scenario 2, the patient does not show shortness of breath (Dispn $=$ absent $)$ nor pedal edema $(L P E=$ absent $)$. However, the manifestations last only for 15 min . After this interval, the angina disappears (Angor $=$ absent $)$ for the next 15 min . Therefore, the CTBN model is queried with the following interval evidence;

$$
\begin{aligned}
{[B P} & =\operatorname{mid}, H F=\text { high }, \text { Angor }=\text { present }, L P E=\text { absent }, \text { Dispn }=\text { absent }, W I \\
& =\text { mid }]
\end{aligned}
$$

for the time interval from 0 to $15 \mathrm{~min}([0,0.25))$, with the following interval evidence

![img-5.jpeg](img-5.jpeg)

Fig. 5 Posterior for AMI, Pump, CardEnz and Shock under Scenario 2

$$
\begin{aligned}
{[\text { BP } } & =\text { mid }, H F=\text { high }, \text { Angor }=\text { absent }, L P E=\text { absent }, \text { Dispn }=\text { absent }, W I \\
& =\text { mid }]
\end{aligned}
$$

for the time interval from 15 to $30 \min ([0.25,0.50))$, and with the interval evidence $[W I=\operatorname{mid}]$, for the time interval from 30 min to $6 \mathrm{~h}([0.50,6))$.

Physicians regard the occurrence of angor as a threatening condition because of its association with coronary obstruction, the cause of myocardial infarction. However, from a clinical point of view, when the chest pain does not persist for at least half an hour, the occurrence of AMI is unlikely. According to the model, heart failure and shock are unlikely events. In the following hour, the posterior probability of shock (Shock $=$ present) remains low $(<0.005)$, likewise the probability of any other abnormal state (Fig. 6).

# 4 Discussion 

The temporal dimension is an essential feature of medical reasoning and decision making. The diagnosis may take advantage from knowing the persistence of observations, and therapy may be optimized in light of the likely future evolution of the medical disorder by anticipating complicating diseases. The epidemiological relevance of heart failure and the usefulness of accurate predictions in the correct management of such an evolving disorder is confirmed by other contributions addressed to the formal representation of the disorder. Although methodologically different, they are all attempts to provide the problem with a quantitative analysis to be exploited in the medical practice. For instance, the Seattle Heart Failure Model is based on a survival model [40] and is probably the first computer-based

![img-6.jpeg](img-6.jpeg)

Fig. 6 Posterior for AMI, CardEnz and Shock under Scenario 3
application to translate medications and devices that a heart failure patient receives in predicted years of survival. However, this model does not represent the process by which the outcomes are affected and, like most multivariate statistical analysis, it is focused on the evolution of chronic heart failure, not on episodes of its reacutization [41].

Bayesian reasoning and inference procedures have gained popularity in the fusion of information obtained from different sources. Perhaps their greatest potential in the clinical setting is to provide a pathophysiological interpretation of events that might be variably accessible to observations. An influence diagram has been proposed to predict heart contractility dysfunctions reflected in the condition of systolic heart failure [42]. Although the model is already structured as a decision support system, it is based on a static BN representation; this way it skips the complexity of inference along the temporal dimension. In spite of the prevalence of proportional hazard models as prognostic models in medicine, DBNs have been also proposed to take advantage of the causal and temporal nature of medical domain knowledge as elicited from domain experts [43].

To the best of the authors' knowledge, there has been only one attempt to model the evolution of heart failure by means of DBNs [8]. The network is based on a time granularity of minutes, rather than seconds like in our application. While this interval can offer a summarised picture on how the disorder evolves, it is also likely to affect the consistency of the dynamic to represent. On the other hand, BNs do not provide direct mechanisms for representing temporal dependencies, so any DBN representation, resulting from the assemblage of several BNs for each time of interest, tends to become rapidly intractable when applied to large but realistic domains [44]. The CTBNs framework overcomes most of the difficulties presented

above, making it possible to elaborate inference on medical problems where the temporal information about a set of manifestations is available from clinical reports or monitoring instrumentation. As such, it might represent a significant improvement over DBNs.

The validity of the qualitative component of the proposed model was addressed by showing the consistency of the graphical structure of the CTBN with a medical textbook of cardiology [39]. Medical expertise was exploited to define the quantitative component, the elicitation of which took advantage of the preliminary reduction in the parameters underlying the CIMs. Further research is needed to provide a quantitative assessment of the predicted probabilities, a task which has been proven to be challenging for any probabilistic expert systems, given that data on large domains are generally lacking [45]. Notwithstanding, the clinical scenario offers several clues on the validity of quantitative predictions in the light of what medical doctors would expect given the selected patient manifestations. Of note, those predictions were achieved by means of ordinary hardware resources.

The comparison of Scenario 2 and Scenario 3 allows us to appreciate the impact of evidence known to be relevant for the occurrence of heart failure, although the reason of failure could be different. The first case study shows the typical consequences of a congestive heart failure, whereby the second patient shows symptoms of one potential cause of heart failure, i.e. AMI. In Scenario 1, the model correctly detects a primitive pump deficit as the cause of heart failure, anticipating shock as a likely future complication. Instead, there are no reasons to hypothesize a pump deficit as a secondary consequence of AMI. In Scenario 2, because the probability of heart failure is low and there are no symptoms of heart failure, the model correctly shows an uncomplicated AMI as the most likely diagnosis. Scenario 2 and Scenario 3 show the same set of manifestations, but their comparison allows us to appreciate the impact of duration of pathological events. Physicians are aware that substernal chest pain is a symptom of coronary obstruction, whose impact on the myocardial tissue depends on the persistence of obstruction. Since an interval of 30 min is generally regarded as the trade off over which the occurrence of infarction becomes more likely than a simple angina episode, the model correctly discriminates the underlying diagnostic explanations of the two cases.

Finally, at the current stage of their development, CTBNs do not encompass an explicit decision analysis. Optimal options in temporal domains are particularly complex to compute. Even if the problem encompasses the selection of a single decision, the latter can nevertheless be affected by the future candidate decisions [7]. Like in [25], we rest on the inferential ability to compute the uncertainties on the main clinical variables, leaving to the doctor the choice of making the most appropriate decision in light of the quantitative updating of both diagnostic and prognostic judgements.

# 5 Conclusions 

In this paper the authors have described the first clinical application of developments in the research area of continuous time graphical models. This

approach allows a direct representation of time and offers a valid computational machinery for medical inference.

The predictions emerging from the three scenarios have confirmed the heuristic power of the proposed framework and have allowed a quantitative evaluation of the expected time before each variable changes its state. The proposed model has then the potential to be used for diagnostic purposes, as well as to develop a strategic plan to reduce the risk associated with each patient treatment.

Additional improvements are needed to turn the CTBN on cardiogenic heart failure into a practical medical tool. Quantitative parameters might be further tuned to achieve posterior probabilities that better fit with expectations derived from pathophysiological knowledge. This could be achieved by learning the CIMs directly from clinical data.

The usefulness of the CTBN could be further increased with the embedding of the CTBN model into a DSS which assists the clinician to choose and to apply the correct therapy. However, a decision analysis would preliminarily call for the computability of posterior probabilities of models at least as complex as the one presented. Thus, we anticipate the usefulness of CTBNs in clinical domains where, like in the case of heart failure, there is growing interest in quantitative predictions.

Acknowledgments The authors are grateful to the anonymous referees whose precious comments contributed to improve the quality and the clarity of the paper.

# Author Biographies 

Elena Gatti got the Bachelor's degree in Molecular Biotechnology in 2004 discussing the dissertation titled "Role of the alpha-tropomyosin in the pathogenesis of the pediatric hypertrophic myopathies". She received the Master's degree in Bioinformatics in 2006 from the University of Milano-Bicocca discussing the dissertation titled "A method for the detection of analogies in binding sites of known protein structures". From February 2007 to October 2007 she worked on the problem of the prediction of secondary protein structures at the Models and Algorithms for Data and Text Mining Laboratory (MAD) of the University of Milano-Bicocca. In February 2011 she received the Ph.D. in Computer Science from the University of Milano-Bicocca. Her main research interests include models and algorithms for data mining while she collaborated to design and implement a software suite on Continuous Time Bayesian Networks. Currently she has a Post-Doc researcher position at the European Institute of Oncology in Milan where she studies and researches on the next generation sequencing data analysis.

Davide Luciani graduated in Medicine in November 1995 at the Università degli Studi di Bologna. From 1999 he is employed at Laboratory of Clinical Epidemiology of the Mario Negri Institute for Pharmacological Research, where in 2005 became head of the Unit of Clinical Knowledge Engineering. His main research interests include decision support systems to improve the quality of care of complex clinical problems, such as the diagnosis of pulmonary embolism and the prognosis of patients admitted in Intensive Care Units. Bayesian analysis and probabilistic graphical models represents the main methodological approach to address the variability of clinical scenario and the optimization of medical decisions in different working environments.

Fabio Stella graduated in Computer Sciences in February 1991 at the Università degli Studi di Milano. From 1991 to 1994 he worked as research assistant for the EEC IMPROD project on semiconductors failure diagnosis, analysis and quality improvement. In January 1994 he became Assistant Professor of Operations Research at the Università degli Studi di Milano. He received the Ph.D. in Computational Mathematics and Operations Research in 1995. In 2001 he became Associate Professor of Operations Research at the Università degli Studi di Milano-Bicocca. He directs the Models and Algorithms for Data and Text Mining Laboratory and actively collaborates with many Italian SMEs in the area of document management, financial risk management, and analysis of clinical and microarray data. He has been advisor of several Ph.D. students in Computer Science at the Università degli Studi di Milano-Bicocca. His main research interests include; continuous time Bayesian networks, data mining, text mining with specific reference to topic models, and computational finance with specific reference to on-line algorithms for portfolio selection.