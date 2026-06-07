# Performance analysis for subsea blind shear ram preventers subject to testing strategies 

Shengnan $\mathrm{Wu}^{\mathrm{a}, \mathrm{b}}$ Laibin Zhang ${ }^{\mathrm{a}}$ Anne Barros $^{\mathrm{b}}$ Wenpei Zheng ${ }^{\mathrm{a}}$ Yiliu Liu $^{\mathrm{b}}$<br>${ }^{\text {a }}$ College of Mechanical and Transportation Engineering, China University of Petroleum (Beijing), Beijing, China<br>${ }^{\mathrm{b}}$ Department of Production and Quality Engineering, Norwegian University of Science and Technology, Trondheim, Norway


#### Abstract

: In a subsea blowout preventer system, a subsea blind shear ram preventer (BSRP) plays as a crucial safety barrier by cutting off the drill pipe and sealing the wellhead to prevent serious accident. Testing and repairs of BSRPs are the main issues in operation and maintenance activities. It is important to assess unavailability during proof and partial testing phases in order to ensure their safety functions. This paper presents a newly state-based approach for unavailability analysis by incorporating testing activities of BSRPs into multiphase Markov process. In the approach, states waiting for repair are taken into consideration. Analytical formulas for evaluation of time-dependent unavailability and average unavailability for BSRPs are developed. In addition, the non-periodic characteristics and effects of degradation are also taken into account in proof testing. The effects of testing errors and postponed repairs on the tendency of unavailability in partial testing phases are checked in the proposed models. Performance analyses for BSRP configurations, scenarios and cases considered in the paper are carried out to demonstrate the application of the proposed models. Monte Carlo models for both proof and partial testing are developed and simulated. Different comparisons are performed for validation of the set of the derived formulations.


Key words: Subsea blind shear ram preventer, Unavailability analysis, Multiphase Markov process, Testing strategies, Monte Carlo models

## 1 Introduction

Blowout, a phenomenon that the uncontrolled formation fluid (crude oil and/or natural gas) may release into the external environment, primarily occurs in the exploitation of oil and gas fields after pressure control systems have failed. Subsea blowout preventer (BOP) is an effective offshore well control system used to prevent blowouts by closing and sealing the well bores [1]. Blind shear ram preventer (BSRP) is the crucial last layer of defense in a BOP system when the pressure within the drilling system becomes uncontrollable. If the BSRP is available on demand, a blowout will not occur. The reliability and availability of BSRP is always very important. However, it is reported that BSRP may fail in chance of $50 \%$ when attempting to shear pipe during actual operations [2]. The well-known "Deepwater Horizon explosion" accident in Macondo drilling rig on April 20, 2010 [3] is caused by the failure of the subsea BOPs and BSRP in particular, as one of main reasons, finally resulting in the catastrophic consequences.

A BSRP in subsea environment may suffer from the failures. Some studies have investigated the failures of BRSPs, e.g. Han et al. [4] have studied the damage and failure of the shear ram of the blowout preventer in the shearing process by a numerical simulation and an experimental investigation. Klingsheim [5] has given about

qualitative analysis of subsea BSRPs including failure modes. The recognized industry regulations and stands requirements have been made to reduce the unavailability. BOPs must be tested and testing strategies are implemented to discover the possible failures [6-8].

Generally, existing methodologies used for BOP reliability analysis can be categorized into two types: static methods (including fault tree analysis (FTA), failure modes and effects analysis (FMEA) and Bayesian network (BN)) [9-11], and dynamic methods (Dynamic BN (DBN), Markov model, and Petri net etc.)[12-14]. FTA and FMEA are widely used in detailed BOP reliabilities studies according to the reports by Holand et al. [15-17]. BN methods have been used by Cai et al. [18] to assess the reliability of subsea BOP control systems, including triple modular redundancy and double dual modular redundancy control systems. Common cause failure and imperfect coverage are taken into account as two important features. However, these approaches that are applied in a static situation are unable to capture dynamic effects during operation processes. On the side of dynamic methods, Cai et al. [19] have presented a novel real-time reliability evaluation methodology based on BNs and DBNs for subsea pipe ram BOP system, and the same authors also consider imperfect repair and preventive maintenance in performance evaluation of BOP and control system [20, 21]. Liu et al. [22] have developed deterministic and stochastic Petri nets models to evaluate the performance of subsea BOP system. Effects of failure rate and repair time of each component on system steady-state availability have been analyzed. Kim et al. [23] have performed availability analysis of BOP building Markov models where the demand rates are considered. Common causes failure is described by the updated $\beta$ factor model that is capable of overcoming the problem of the same $\beta$ factor and distinguishing different voting logics. The above-mentioned methods have focused on reliability analysis for BOP system. However, assessments of BSRPs in real world may consider many complex situations such as flexible duration of testing, the real degradation of components, testing errors and different maintenance strategies.

Multiphase, multiphase Markov or phased mission system analysis is referred as another dynamic reliability analysis method which has been developed by some research works [24-26]. These methods have been applied to safety instrumented system for reliability assessment. For instance, Innal et al. [13] have established new generalized formulations with repair time using the multi-phase Markov models. Mechri et al. [27] have used the fuzzy multiphase Markov chains to assess the performance of safety instrumented systems (SISs) in low demand mode. Expert judgment is adapted to evaluate the impact of uncertainty. Langeron et al. [28] have presented multiphase Markov approach to formalize the probability of each state of a SIS, and also have investigated the robustness of IEC61508 merging rules in an analytical way. A BOP test from one phase to another is also a multiphase process. A multiphase Markov model has been presented by Strand and Lundteigen [29] for BOP system reliability assessment during well drilling phases for risk control, and this model can be used to support decision-making about maintenance policies.

Several issues, however, need to be further investigated when they are applied to the subsea BRSPs:

- The dynamic behaviors involving testing characteristics (errors may exist during the testing) and maintenance effects on unavailability are ignored.
- Only periodical proof test is considered in Markov models. In addition, failure rates are always assumed to be identical in every phase, meaning that deterioration is not in consideration.
- Challenges from subsea context are not well handled with, for instance, the non-ignorable time to repair even for a revealed failure. Repairs for subsea facilities are always postponed since: Firstly it is difficult to access to subsea equipment, and secondly, some potential well blowout risk may increase due to the unscheduled pulling of a BOP for repair.
In order to overcome these limitations, this paper proposes a new approach based on multiphase Markov process for developing unavailability analytical formulas that consider maintenance characteristics during testing phases. The main benefit of the proposed approach is a more efficient and realistic process, where the potential

factors and the effect of maintenance strategies are taken into account compared with the typical BOP reliability analysis [18]. In addition, regarding other dynamic models such as simple Markov process or Petri-nets, the benefits are specified as follows:

- Compared to simple Markov process, multiphase ones allow to take into account periodic or deterministic time for inspection, and changes of the failure rate between different phases.
- Compared to Petri-nets simulation, multiphase Markov process can give an exact close formula for the unavailability assessment in modeling testing errors.
The potential contributions can be specified as:
- Maintenance durations for the BSRPs in different phases are involved. Dynamic behaviors of a system during repairs are considered in unavailability analysis.
- Degradation is taken into account during proof testing. The increasing failure rate in different phases is also modeled in the calculation of unavailability for dynamic predication.
- Testing characteristics are also taken into consideration, including testing errors in partial testing phases, non-periodic testing, and detection delay.
The reminder of the paper is organized as follows. Section 2 describes in detail the subsea BOP system and the subsea BSRPs, their operation and failure modes, as well as the testing and repair activities. Section 3 illustrates the proposed approach for building multiphase Markov models and developing the approximation formulas for unavailability analysis given the certain assumptions. Section 4 presents the corresponding numerical results for performance analysis in consideration of the non-periodic characteristics and effects of degradation, and testing errors and repair time. Section 5 has compared the numerical results from the approximations with those from the Monte Carlo simulation to validate the proposed approach. Concluding remarks and suggestions to future works are given in section 6.


# 2 System description 

### 2.1 Subsea BOP system

The subsea BOP system mainly consists of subsea BOP control system and subsea BOP stack. The subsea control system is comprised of electrical system and hydraulic system such as pumps, valves, accumulators, fluid storage and mixing equipment, manifold, and other equipment [22], which is out of the scope of this paper. A typical subsea BOP stack is illustrated in Fig. 1. The subsea BOP stack is usually equipped with Lower Marine Riser Package (LMRP) connector and wellhead connector which are activated hydraulically and are used to connect the LMRP to the BOP stack or the BOP stack to the wellhead in the seafloor. Two types of preventers, annular preventer and ram preventer, are utilized. It also mainly includes annular preventers, ram (pipe ram, shear ram) preventers, and other components, for instance, the flexible joint and choke valves and lines [18]. Annular BOPs are hydraulically operated to seal off different sizes of annulus whether drill pipe is in the wellbore or not. However, annular preventers are generally not as effective as ram preventers in maintaining a seal on an open hole[30]. Ram BOPs are similar to a gate valve in operation to some extent and used to close and seal the hole when they are activated. Pipe ram preventers close around a drill pipe and shear ram preventers must cut off the drill string or casing with hardened steel shears for emergence situations e.g., kicks or potential blowouts. BSRPs, which are the last line of defenses against blowout, are intended to cut off the drill pipe if present and effectively seal the hole against release of oil/gas/drilling mud.

![img-0.jpeg](img-0.jpeg)
(c)

Fig. 1 (a) a typical conventional BOP stack and (b) a typical model BOP stack and (c) the simplified BOP configurations

# 2.2 Configurations 

According to the configurations of ram preventers and minimum redundancies requirements, BOP stacks can

be classified into a conventional BOP stack and a modern BOP stack, respectively. As shown in Fig. 1 (a) and (b), a modern subsea BOP typically has two annular preventers, four pipe ram preventers, two blind shear ram preventers, while a conventional subsea BOP has two annular preventers, three pipe ram preventers, a blind shear ram preventer. Fig. 1 (c) indicates the simplified BOP configurations and components number. Compared with the conventional configuration, BSRPs in the modern BOP configuration are parallel subsystems with two components and pipe ram BOP subsystem is a parallel subsystem with four components. The different configurations of preventers lead to different performances for subsea BOP system. Such redundancies aim to give functional availability in case of system or subsystem failure during blowout occurrence. Therefore, BSRPs as a critical subsystem of the BOP stack may be modelled with basic 1001 or 1002 configurations [23, 30, 31] for performance analysis in this research.

# 2.3 BSRP 

A BSRP is described as a valve consisting of two pairs of opposing steel blocks, blades, sealing components, locks, shuttle valves and pistons depending on type and use as seen in Figure 2. The subsea BOP system is operated in the high demand mode in terms of above different definitions. However, while annulus preventers, connectors, and pipe ram preventers are used continuously or frequently during drilling operations, BSRPs are usually used only for a special condition such as shut-in the well. Therefore they needs to be operated in the low demand mode to reflect reality more. The performance of BSRPs depends on the conditions and situation in which they are activated. BSRPs are able to close on an empty wellbore for function testing, pressure testing or controlled operations, shear the drill pipe and then seal the wellbore for the controlled emergency operations or emergency situations. The BSRP will be activated in different ways according to the relevant standards and regulations, and one is that fluid comes through the shuttle valve providing pressure on the piston. NORSOK D-010 also states that shear rams shall only be activated in emergency when no other options exist but to cut and seal $[6,32]$.
![img-1.jpeg](img-1.jpeg)

Fig. 2 A typical BSRP structure [5]

# 2.4 Failure modes 

Dangerous failures for a SIS include dangerous detected (DD) failures detected by the diagnostics/self-testing immediately after they occur, and dangerous undetected (DU) failures which remain hidden until the safety function is carried out, either by partial tests, proof tests or a real demand [8, 33]. For a BSRP, the DU failures are the main contributor of its unavailability, and DD failures are therefore negligible in this study. In addition, DU failures can be classified into two categories due to the BSRPs role and function: Type 1 failures (DU1): Failure to close on open hole or failure to seal wellbore that may be caused by mechanical failure, hydraulic failure and flowing well, and Type 2 failures (DU1): Failure to close or close too slowly when shearing and failure to shear, with the failure causes such as drilling pipe in compression and other tubular than drill pipe. DU1 failures and DU2 failures for BSRPs 1001 configuration with two failure modes and 1002 configuration with four failure modes are illustrated in Fig. 3.
![img-2.jpeg](img-2.jpeg)

Fig. 3 BRSPs failure modes of (a) 1001 configuration and (b) 1002 configuration

### 2.5 Testing and maintenance

The testing requirements in API 16A are that the tests of BSRPs shall be performed for sealing, fatigue, shearing and locking mechanism [32]. The maintenance and preparations will also be performed when BOP is pulled to surface for use on the next well. In IEC 61508, a BOP should be tested for function every 7 or 14 days under the expected well/reservoir pressure, but may be postponed if there is tubular across the BOP [8]. In the Norwegian standard D-010N[6], proof tests for BSRPs should be carried out once at most every 30 day, and these tests may be postponed if there are well-control problems. The practical testing strategies for a real-world system may be a combination of partial and proof tests. Such testing is aiming to reveal the DU failures of components. Since proof tests on BSRPs needs to cut the pipe, and the testing tool may disturb the drilling. Partial tests, however, as imperfect testing are always needed to reveal some types of failures without significant impact on drilling. Therefore, DU1 failures can be detected by partial tests and DU2 failures are only detected by proof test. Three distinct BSRPs well isolation scenarios have been identified, which include low well pressure scenario with no drill pipe in hole, no drill pipe in hole or drill pipe in hole [29]. In this research, cases of non-periodic testing and periodic testing relevant to degradation are taken into account during proof test due to the detection delay, and cases of testing errors and maintenance durations are considered during partial testing due to the imperfect test and

postpone repair.

# 2.6 SIL requirement 

According to the requirements of the IEC 61508 standard, the subsea BOP system is a SIS employed during drilling of a subsea well and it is used to implement one more Safety Instrumented Functions (SIF). A SIF can be assumed the ultimate safety barrier that has been installed to protect people from a specific type of critical hazardous events. The subsea BRSP is considered to function in the low demand rate mode and the Safety Integrity Level (SIL), as a fundamental concept within the IEC 61508 standard, is evaluated by determining the Probability of Failure on Demand (PFD). The BSRP performance in this paper is evaluated by unavailability and average unavailability that is assumed to approximately be equal to PFD or average PFD. SILs related to the PFD is specified in Table 5 [33]. Combining of both proof and partial teats in the multiphase Markov modelling, the minimum SIL2 requirement is used here for BSRPs to choose the optimal testing strategies for decision making.

Table 1 SIL for low-demand SISs


## 3. Unavailability analysis model

This section firstly presents some relevant assumptions for modeling, illustrates an analytical unavailability approach based on multiphase Markov process in terms of the requirements of different testing strategies, and then builds a multiphase Markov unavailability analysis model. The formulas associated with unavailability and average unavailability of the system for testing phases are evaluated for 1001 configuration and 1002 configuration respectively.

### 3.1 Assumptions

For unavailability analysis, the following assumptions are needed:

- DU failures of a BRSP and its components follow the exponential distribution;
- All components are independent and repairable;
- A repair cannot be initialized immediately due to the difficulty in accessing subsea equipment;
- The degradation process of components can be modeled by changing failure rate in different phase;
- Repair time cannot be negligible and can be modeled by an exponential law. Actually the repair time refers to the time required before detection of a failure plus the time required to make a replacement for a component after detection during testing phase.


### 3.2 Unavailability formulation for testing phases

The multiphase-Markov-based model is proposed and used for unavailability analysis in practical testing phases. The availability of a system is related to its essential function. The system taking with available states is able to perform its essential function, while the system taking with unavailable states is unable to perform its essential function. The unavailability of system can be analytically evaluated in different testing intervals. Each testing interval is regarded as a phase of a multiphase Markov process. Between two tests, the behavior of the system is modeled by a classical Markov chain and at the test time, the effect of a test is modeled by a transition matrix

which put the Markov chain into a new initial state.

# 3.2.1 Analytic formulas for unavailability 

In a Markov model, $C(i, j)$ is defined as the transition rate matrix from one state $i$ to another state $j$ in a testing phase. $P_{t}(i)$ stands for the probability in state $i$ at time $t$ and $P_{t}$ is expressed as $P_{t}=\left[P_{t}(1), P_{t}(2), \cdots, P_{t}(i)\right]$. If $C(i$, $j$ ) is constant in a testing phase, the system behavior can be illustrated according to Chapman-Kolmogorov's equation $[33,34]$, and $P_{t}$ is expressed as

$$
\begin{gathered}
\frac{d P_{t}}{d t}=P_{t} \cdot C \\
P_{t}=\exp (C \cdot t)
\end{gathered}
$$

In a multiphase-based Markov model, the $k$ testing intervals are denoted as $\left[T_{0}=0, T_{l}\right],\left[T_{l}, T_{2}\right], \cdots,\left[T_{k-1}, T_{k}\right]$. If we assume that $t$ is in the first testing phase $\left[T_{0}=0, T_{l}\right]$, it is possible to calculate the state probability as follows:

$$
\begin{aligned}
\mathrm{P}_{t} & =\mathrm{P}_{0} \cdot \exp \left(C_{1} \cdot t\right) \\
\mathrm{P}_{T 1} & =\mathrm{P}_{0} \cdot \exp \left(C_{1} \cdot T_{1}\right)
\end{aligned}
$$

where $C_{1}, C_{2}, \cdots \cdots C_{k}$ stands for transition rates matrix in different testing phases respectively.
If we assume that $t$ is in the second testing phase $\left[T_{l}, T_{2}\right]$, the state probability can be calculated based on $P_{T l}$ and is given by:

$$
\mathrm{P}_{t}=\mathrm{P}_{T 1} \cdot M_{1} \cdot \exp \left(C_{2} \cdot\left(t-T_{1}\right)\right)
$$

where $M_{l}$ is the probability transition matrix of different states in a new testing phase after a previous testing and repair action, and the repair actions at time $T_{1}$ are modeled by a linear transition on the probability $\mathrm{P}_{T 1} . P_{T 1} \cdot M_{1}$ stands for the probability of all the states after repair actions at time $T_{1} . M_{1}$ may be affected by the testing strategies and repair actions. This proposed approach allows to linearly redistribute the states probabilities at the beginning of each testing phase by multiplying the transition probability matrix [28, 34]. We can therefore have $\mathrm{P}_{T 2}$ :

$$
\mathrm{P}_{T 2}=\mathrm{P}_{T 1} \cdot M_{1} \cdot \exp \left(C_{2} \cdot\left(T_{2}-T_{1}\right)\right)=\mathrm{P}_{0} \cdot \exp \left(C_{1} \cdot T_{1}\right) \cdot M_{1} \cdot \exp \left(C_{2} \cdot\left(T_{2}-T_{1}\right)\right)
$$

We then have $\mathrm{P}_{T(k-1)}$ for

$$
\begin{gathered}
\mathrm{P}_{T_{(k-1)}}=\mathrm{P}_{T_{(k-2)}} \cdot M_{k-2} \cdot \exp \left(C_{k-1} \cdot\left(T_{k-1}-T_{k-2}\right)\right)=\mathrm{P}_{0} \cdot \prod_{n=1}^{n=k-2} \exp \left(\left(C_{n} \cdot\left(T_{n}-T_{n-1}\right)\right) \cdot M_{n}\right) \cdot \exp \left(C_{k-1}\right. \\
\left.\left(T_{k-1}-T_{k-2}\right)\right)
\end{gathered}
$$

where $M_{k-2}$ the probability transition matrix in the testing phase $\left[T_{k-2}, T_{k-1}\right]$.
If $t$ in the testing phase $\left[T_{k-1}, T_{k}\right]$, we then get $P_{t}$ in

$$
\mathrm{P}_{t}=\mathrm{P}_{T_{(k-1)}} \cdot M_{k-1} \cdot \exp \left(C_{k} \cdot\left(t-T_{k-1}\right)\right)=\mathrm{P}_{0} \cdot \prod_{n=1}^{n=k-1} \exp \left(\left(C_{n} \cdot\left(T_{n}-T_{n-1}\right)\right) \cdot M_{n}\right) \cdot \exp \left(C_{k} \cdot\left(t-T_{k-1}\right)\right)
$$

According the definition of unavailability denoted as $U A(t)$, the system will not be functioning as long as the system is in one of the unavailable states. So we can obtain the probability by the system taking unavailable states given a period of testing phase. The total $U A(t)$ can be expressed as

$$
U A(t)=P_{t} \cdot B
$$

where B is a vector composed of 1 and 0 elements allowing to obtain the functioning state probabilities associated with availability or failed state probabilities concerned by unavailability.

The same method can be used to evaluate the unavailability in testing phase $t \in\left[T_{k-1}, T_{k}\right]$, which can be written as

$$
U A_{k}(t)=\mathrm{P}_{0}(i) \cdot \prod_{n=1}^{n=k-1}\left(\exp \left(\mathrm{C}_{n} \cdot\left(T_{n}-T_{n-1}\right)\right) \cdot M_{n}\right) \cdot \exp \left(\mathrm{C}_{k} \cdot\left(t-T_{k-1}\right)\right) \cdot B
$$

Eq. (10) also provides a method to evaluate the $U A(t)$ in periodic or non-periodic or deterministic testing phases.

# 3.2.2 Analytic formulas for average unavailability 

The total average unavailability $U A_{\text {avg }}$ for the general cases can be therefore expressed analytically as
$\mathrm{UA}_{\text {avg }}=\frac{1}{T} \int_{0}^{\mathcal{T}} \mathrm{UA}(\mathrm{t}) d t=\frac{1}{T}\left[\int_{T_{0}}^{T_{1}} \mathrm{UA}_{1}(t) d t+\int_{T_{1}}^{T_{2}} \mathrm{UA}_{2}(t) d t+\cdots+\int_{T_{k-1}}^{T_{k}} U \mathrm{~A}_{k}(t) d t\right]=\frac{1}{T} \sum_{n=1}^{n=k} \int_{T_{n-1}}^{T_{n}} \mathrm{UA}_{n}(t) d t$
For instance, if $t$ is in first testing phase $\left[T_{0}, T_{1}\right]$, we can have
$\int_{T_{0}}^{T_{1}} U A_{1}(t) d t=\int_{T_{0}}^{T_{1}} \mathrm{P}_{0}(i) \cdot \exp \left(\mathrm{C}_{1} \cdot\left(t-T_{0}\right)\right) \cdot B=\mathrm{P}_{0}(i) \cdot \int_{T_{0}}^{T_{1}} \exp \left(\mathrm{C}_{1} \cdot\left(t-T_{0}\right)\right) d t \cdot B=\mathrm{P}_{0}(i) \cdot \sum_{l=0}^{\infty} \frac{\left(C_{l}\right)^{l}}{(l+1)!} \cdot$ $\left(T_{1}^{l+1}-T_{0}^{l+1}\right) \cdot B$

With regard to the second testing phase $t \in\left[T_{1}, T_{2}\right]$, the expression can be given by

$$
\begin{gathered}
\int_{T_{1}}^{T_{2}} U A_{2}(t) d t=\int_{T_{1}}^{T_{2}} \mathrm{P}_{0}(i) \cdot \exp \left(\mathrm{C}_{1} \cdot\left(T_{1}-T_{0}\right)\right) \cdot M_{1} \cdot \exp \left(\mathrm{C}_{2} \cdot\left(t-T_{1}\right)\right) \cdot B d t=\mathrm{P}_{0}(i) \cdot \exp \left(\mathrm{C}_{1} \cdot\left(T_{1}-T_{0}\right)\right) \cdot M_{1} \cdot \\
\int_{T_{1}}^{T_{2}} \exp \left(\mathrm{C}_{2} \cdot\left(t-T_{0}\right)\right) d t \cdot B=\mathrm{P}_{0}(i) \cdot \exp \left(\mathrm{C}_{1} \cdot\left(T_{1}-T_{0}\right)\right) \cdot M_{1} \cdot \sum_{l=0}^{\infty} \frac{\left(C_{l}\right)^{l}}{(l+1)!} \cdot\left(T_{2}^{l+1}-T_{1}^{l+1}\right) \cdot B
\end{gathered}
$$

Similarly, if $t$ is in testing phase $\left[T_{k-1}, T_{k}\right]$, we also have
$\int_{\mathrm{T}_{\mathrm{k}-1}}^{\mathrm{T}_{\mathrm{k}}} U A_{k}(t) d t=\int_{\mathrm{T}_{\mathrm{k}-1}}^{\mathrm{T}_{\mathrm{k}}} \mathrm{P}_{0}(i) \cdot \prod_{n=1}^{n=k-1}\left(\exp \left(\mathrm{C}_{n} \cdot\left(T_{n}-T_{n-1}\right)\right) \cdot M_{n}\right) \cdot \exp \left(\mathrm{C}_{k} \cdot\left(t-T_{k-1}\right)\right) \cdot B d t=\mathrm{P}_{0}(i) \cdot$ $\prod_{n=1}^{n=k-1}\left(\exp \left(\mathrm{C}_{n} \cdot\left(T_{n}-T_{n-1}\right)\right) \cdot M_{n}\right) \cdot \int_{\mathrm{T}_{\mathrm{k}-1}}^{\mathrm{T}_{\mathrm{k}}} \exp \left(\mathrm{C}_{k} \cdot\left(t-T_{k-1}\right)\right) \cdot B d t=\mathrm{P}_{0}(i) \cdot \prod_{n=1}^{n=k-1}\left(\exp \left(\mathrm{C}_{n} \cdot\left(T_{n}-T_{n-1}\right)\right)\right.$. $\left.M_{n}\right) \cdot \sum_{l=0}^{\infty} \frac{\left(C_{k}\right)^{l}}{(l+1)!} \cdot\left(T_{k}^{l+1}-T_{k-1}^{l+1}\right) \cdot B$

The failures may occur at random in any testing phase. Hence, the plus rules is introduced to generate the proposed formula for evaluating total $U A_{\text {avg }}$ in whole testing phases $[0, T]$ that can be rewritten

$$
\begin{gathered}
\mathrm{UA}_{\text {avg }}=\frac{1}{T} \int_{0}^{\mathcal{T}} \mathrm{UA}(\mathrm{t}) d t=\frac{1}{T} \mathrm{P}_{0}(i) \cdot\left(\sum_{l=0}^{\infty} \frac{\left(C_{l}\right)^{l}}{(l+1)!} \cdot\left(T_{2}^{l+1}-T_{1}^{l+1}\right)+\exp \left(\mathrm{C}_{1} \cdot\left(T_{1}-T_{0}\right)\right) \cdot M_{1} \cdot \sum_{l=0}^{\infty} \frac{\left(C_{l}\right)^{l}}{(l+1)!}\right. \\
\left.\left(T_{2}^{l+1}-T_{1}^{l+1}\right)+\cdots+\prod_{n=1}^{n=k-1}\left(\exp \left(\mathrm{C}_{n} \cdot\left(T_{n}-T_{n-1}\right)\right) \cdot M_{n}\right) \cdot \sum_{l=0}^{\infty} \frac{\left(C_{k}\right)^{l}}{(l+1)!} \cdot\left(T_{k}^{l+1}-T_{k-1}^{l+1}\right)\right) \cdot B
\end{gathered}
$$

### 3.3 Unavailability evaluation with proof testing

A proof test will be performed for BSRPs during drilling and is assumed to detect all failures in every phase. To illustrate the calculation of unavailability subject to proof testing phases and these intervals may depend on the drilling conditions, the general cases of a lool configuration with one BSRP and loo2 configuration consisting of two BSRPs are considered here.

- First step is to identify all possible states of different configurations to build the multiphase Markov models. Non-negligible repair time is taken into account every testing phase and the state of "in repair" is therefore introduced to illustrate the detection delay phenomenon.
- The failure rates and repair rates can be then evaluated according to the experience data or expert judgments to construct the transition rate matrix. The probabilities transition matrix of states is also determined by operators. In the beginning of a period of time, the system is in functioning state and the corresponding probability is assigned to 1 .
- Formulas associated with time-dependent unavailability with different scenarios have finally been developed.
3.3.1 Multiphase Markov models for proof testing phases

The unavailability of system is calculated in proof testing phases $\left[T_{0}, T_{1}\right],\left[T_{1}, T_{2}\right], \cdots,\left[T_{m-1}, T_{m}\right]$, and $m$ stands for the number of proof testing phases. The periodic or non-periodic phases are considered in term of the specific operation requirements. These proposed multiphase Markov models are illustrated in Fig. 4 (a) and (b) where repair states are introduced for 1001 and 1002 configurations. The possible states are illustrated in Table 2 and Table 3.
![img-3.jpeg](img-3.jpeg)
(a)
![img-4.jpeg](img-4.jpeg)
(b)

Fig. 4 Multiphase Markov models in different proof testing phases for (a) 1001 configuration and (b) 1002 configuration

Table 2 Possible states for 1001 configuration


Table 3 Possible states for 1002 configuration


Fig. 4 shows that multiphase Markov models can be established for proof testing phases taking three or five states to calculate the unavailability of different configurations. In these models, the circle with the green color represents that the system is available, while circles with yellow color stands for unavailable state. If the failure is assumed to be detected in such phases, while repairs cannot be initialized immediately, the links associated with repairs cannot return from the DU state directly. A repair state is therefore introduced. The dotted line stands for waiting repair and there are no transitions between two states for Markov models. It is clear that a system's testing

and repair action can be integrated into multiphase Markov models and such models can therefore create more comprehensive and realistic situation for safety prediction of a system. In short, combining testing activities and repair actions enable to obtain the unavailability under a real system especially a system in subsea environment.

# 3.3.2 Analytic formulas for proof testing 

At the start of first phase, the system is assumed to be in the "FU" or "FU-FU" state. The probabilities taking three states and five states are therefore given by at initial time $t=0$ respectively:

$$
\begin{gathered}
\mathrm{P}_{01}=[1,0,0] \\
\mathrm{P}_{02}=[1,0,0,0,0]
\end{gathered}
$$

where $P_{01}$ stands for initial probability of 1001 configuration and $P_{02}$ stands initial probability of 1002 configuration.

The transition rates matrix consisting of failure rates and repair rates is expressed in terms of Fig.1. For instance, the repair rate for 1001 configuration is denoted by $\mu_{D U}^{m}$ in any phase $\left[\mathrm{T}_{\mathrm{m}-1}, \mathrm{~T}_{\mathrm{m}}\right]$. The transition rates matrix is therefore represented by

$$
\begin{gathered}
C_{m 1}=\left[\begin{array}{ccc}
-\lambda_{D U}^{m} & \lambda_{D U}^{m} & 0 \\
0 & 0 & 0 \\
\mu_{D U}^{m} & 0 & -\mu_{D U}^{m}
\end{array}\right] \\
C_{m 2}=\left[\begin{array}{cccc}
-2 \lambda_{D U}^{m} & 2 \lambda_{D U}^{m} & 0 & 0 & 0 \\
0 & -\lambda_{D U}^{m} & 0 & \lambda_{D U}^{m} & 0 \\
\mu_{D U}^{m} & 0 & -\left(\mu_{D U}^{m}+\lambda_{D U}^{m}\right) & 0 & \lambda_{D U}^{m} \\
0 & 0 & 0 & 0 & 0 \\
2 \mu_{D U}^{m} & 0 & 0 & 0 & -2 \mu_{D U}^{m}
\end{array}\right]
\end{gathered}
$$

where $\mathrm{C}_{\mathrm{m} 1}$ stands for 1001 configuration transition rates matrix and $\mathrm{C}_{\mathrm{m} 2}$ stands for 1002 configuration transition rates matrix. $\lambda^{m}{ }_{D U}$ is the failure rate of system in the testing phase $m$.

The state probabilities in matrix $M_{m}$ can be obtained by expert judgments, and $M_{m}$ is assumed to be identical and there is no mistakes (e.g. false alarm) in every testing phase, namely $M_{1}=M_{2}=\cdots=M_{m}=M$. We therefore have:

$$
\begin{gathered}
M_{m 1}=\left[\begin{array}{lll}
1 & 0 & 0 \\
0 & 0 & 1 \\
0 & 0 & 1
\end{array}\right] \\
M_{m 2}=\left[\begin{array}{llll}
1 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 1
\end{array}\right]
\end{gathered}
$$

where $\mathrm{M}_{\mathrm{m} 1}$ stands for 1001 configuration probability transition matrix and $\mathrm{M}_{\mathrm{m} 2}$ stands for 1002 configuration probability transition matrix.

The vectors $B$ are defined such that $B_{j}(1, i)=\left\{\begin{array}{r}0, \text { if the state } \mathrm{i} \text { is available } \\ 1, \quad \text { if the state } \mathrm{i} \text { is unavailable }\end{array}\right.$ for $\mathrm{j}=1,2$. We

therefore have for 1001 and 1002 configurations respectively,

$$
\begin{gathered}
B_{1}=[0,1,1]^{T} \\
B_{2}=[0,0,0,1,1]^{T}
\end{gathered}
$$

Generally, the unavailability and average unavailability of 1001 and 1002 configuration in proof testing phase at $t \in\left[\mathrm{~T}_{\mathrm{m}-1}, \mathrm{~T}_{\mathrm{m}}\right]$ can be evaluated based on the Eq. (10) and Eq. (15), respectively. These corresponding formulas can provide an approach to assess the instant unavailability of the system at different time points.

# 3.4 Unavailability evaluation with partial testing 

The proposed approach is also applied for dynamic evaluation in practical applications. For BSRPs, partial testing refers to only detect DU1 failures, while the remaining DU2 failures can be detected by proof testing which is assumed to reveal all failures. We assume that all the failure rates are identical in every partial testing phase due to the short testing interval, and all testing phases are assumed to be periodic.

### 3.4.1 Multiphase Markov models for partial testing

The unavailability of system is calculated in partial testing phases $\left[T_{0}, T_{1}\right],\left[T_{1}, T_{2}\right], \cdots,\left[T_{k-1}, T_{k}\right]$, where $k$ stands for the number of partial tests and $\Delta\left(\Delta=T_{k}-T_{k-1}\right)$ stands for the testing interval. Multiphase Markov models for the different configurations are illustrated in Fig. 5. The dotted line stands that there is no Markov transitions between two states in these models, but the transition will be effective after a partial test. This system may be assumed to take states at time $t$ in periodic partial testing phase $\left[T_{k-1}, T_{k}\right]$ listed in Tables 4 and 5 according to 1001 and 1002 configuration.
![img-5.jpeg](img-5.jpeg)

![img-6.jpeg](img-6.jpeg)

Fig. 5 Multiphase Markov models in partial testing phases for (a) 1001 configuration and (b) 1002 configuration

Table 4 Possible states for 1001 configuration for partial testing


Table 5 Possible states for 1002 configuration for partial testing



As indicated in Fig. 5, we have established multiphase Markov models for partial testing phases involving the two types of failures. The circle with the green color represents available states, while circles with yellow color stands for unavailable system. It is obvious that there are three states unavailable for the 1001 configuration while five states unavailable for the 1002 configuration in partial testing phases. It is also shown that system's partial testing, and repair action can be integrated into the proposed models.

# 3.4.2 Formulas analytical for partial testing 

If the system is assumed to be in the "FU" or " 2 FU "state, the initial probability for different configurations is therefore given by at time $t=0$ :

$$
\begin{gathered}
\mathrm{P}_{01}=[1,0,0,0] \\
\mathrm{P}_{02}=[1,0,0,0,0,0,0,0,0,0]
\end{gathered}
$$

where $\mathrm{P}_{01}$ stands for initial probability of 1001 configuration and $\mathrm{P}_{02}$ stands for initial probability of 1002 configuration for partial testing, respectively.

The transition rate matrix is established based on the illustration of Fig.2. Taking 1001 configuration for instance, if the failures detected in partial testing phase $\left[\mathrm{T}_{\mathrm{k}-1}, \mathrm{~T}_{\mathrm{k}}\right]$ is unable to be repaired immediately, the repair rate is denoted as $\mu_{D U 1}$. The two types of failure rates can be expressed as $\lambda_{\mathrm{DU} 1}$ and $\lambda_{\mathrm{DU} 2}$. The transition rates matrix is therefore presented by

$$
C_{k 1}=\left[\begin{array}{ccccc}
-\left(\lambda_{D U 1}+\lambda_{D U 2}\right) & \lambda_{D U 1} & 0 & \lambda_{D U 2} \\
0 & 0 & 0 & 0 \\
\mu_{D U} & 0 & -\mu_{D U} & 0 \\
0 & 0 & 0 & 0
\end{array}\right]
$$

where $\mathrm{C}_{k 1}$ stands for 1001 configuration transition rates matrix, $\mathrm{C}_{k 2}$ stands for 1002 configuration transition rates matrix for partial testing, respectively.

The states probabilities in matrix $M_{k}$ also can be obtained by expert judgments, and $M_{k}$ is assumed to be constant in every phase, namely $M_{l}=M_{2}=\cdots=M_{k}=M$. Imperfectness of the partial testing is modeled and imperfect parameters such as $\omega$ and $\eta$ therefore are introduced for two scenarios. Imperfect factors $\omega$ is kind of

probability of false alarm and $\eta$ is kind of probability of not detection

- Scenario 1: Testing and repair action are perfect, so $\omega=\eta=0$, and the probability of states are assigned to 1 .
- Scenario 2: Testing and repair action are imperfect, so $\omega \neq 0$ or $\eta \neq 0$, and the probability of states doesn't equal to 1 .
Hence, $M$ may be given by

$$
M_{k 1}=\left[\begin{array}{cccccccc}
1-\omega & 0 & \omega & 0 \\
0 & \eta & 1-\eta & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1
\end{array}\right]
$$

$$
M_{k 2}=\left[\begin{array}{cccccccccc}
1-\omega-\omega & 0 & 0 & \omega & \omega & 0 & 0 & 0 & 0 & 0 \\
0 & \eta & 0 & 1-\eta & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & \eta & 0 & 0 & 0 & 0 & 0 & 0 & 1-\eta \\
0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1 & 0 \\
0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 & 1
\end{array}\right]
$$

where, $\mathrm{M}_{\mathrm{k} 1}$ stands for 1 ool configuration state transition matrix, $\mathrm{M}_{\mathrm{k} 2}$ stands for 1 oo 2 configuration state transition matrix for partial testing, respectively. For instance, we have the probabilities from state $i$ in one phase to state $j$ in this or next phase for 1 ool configuration and the details are illustrated as follows:
$\mathrm{P}\left(\mathrm{FU}_{\mathrm{k}-1} \rightarrow \mathrm{FU}_{\mathrm{k}}\right)=1-\omega=\mathrm{M}_{\mathrm{k} 1}(1,1)$ stands for probability transition of a system in state FU from previous phase $k-1$ to the current phase $k$.
$\mathrm{P}\left(\mathrm{FU}_{\mathrm{k}} \rightarrow \mathrm{IR}_{\mathrm{k}}\right)=\omega=\mathrm{M}_{\mathrm{k} 1}(1,3)$ stands for probability transition of a system in phase $k$ from the state FU to the state IR.
$\mathrm{P}\left(\mathrm{DU} 1_{\mathrm{k}-1} \rightarrow \mathrm{DU} 1_{\mathrm{k}}\right)=\eta=\mathrm{M}_{\mathrm{k} 1}(2,2)$ stands for probability transition of a system in state DU1 from previous phase $k-1$ to the current phase $k$.
$\mathrm{P}\left(\mathrm{DU} 1_{\mathrm{k}} \rightarrow \mathrm{IR}_{\mathrm{k}}\right)=1-\eta=\mathrm{M}_{\mathrm{k} 1}(2,3)$ stands for probability transition of a system in phase $k$ from the state DU1 to the state IR.

Similarly, we u have the vectors $B_{1}$ for 1 ool configuration and $B_{2}$ for 1 oo 2 configuration respectively

$$
\begin{gathered}
B_{1}=[0,1,1,1]^{T} \\
B_{2}=[0,0,1,0,1,0,1,1,1,1]^{T}
\end{gathered}
$$

In summary, the unavailability and average unavailability for 1 ool and 1002 configuration in partial testing phase $t \in\left[\mathrm{~T}_{\mathrm{k}-1}, \mathrm{~T}_{\mathrm{k}}\right]$ can be also obtained based on the Eq. (10) and Eq. (15), respectively. The corresponding formulas can provide an approach to dynamically assess the time-dependent unavailability of the system in partial testing phase.

# 4. Performance analysis 

The subsea BSRP is a typical safety critical subsystem subject to different testing and maintenance strategies that contribute to the improvement of the performance. Such BSRP will be modeled with basic 1001 configuration and 1002 configurations based on the analysis of Section 2. It will therefore serve as an application case for the proposed approach. In this performance analysis, the developed formulas for different configurations during both proof testing and partial testing phases are applied and the numerical results are given in different cases. The particulars of the performance analysis are specified as the following:

- Inputs reflect the parameters collection that are used for performance analysis and are generally includes data statistics and data processing. Data statistics are from the relative literatures, accident reports and expert inputs, including mean time to failure (MTTF), mean repair time (MRT), mean down time (MDT) and testing intervals for BSRPs. Data processing captures the input parameters computed such as failure rates and repair rates.
- Processes represent calculating mechanisms of the unavailability analysis model that convert inputs to outputs. The dynamic characteristics of proof testing and partial testing have been investigated, including effects of deterministic proof testing phases or degradation, and effects on testing errors (false alarm and not detection) or postponed repair during partial testing on unavailability of BSRPs.
- Outputs indicate outcomes of performance analysis that have been especially evaluated by the tendency of instant unavailability and average unavailability under different cases. Establishment of SIL contributes to assess the performance of BSRPs in low-demand mode for making decision.


### 4.1 Unavailability analysis with proof testing

BSRPs serve in subsea environments and their failure rates could be increasing from one proof testing phase to another proof testing phase due to the degradation. Consider 3 selected (periodic and non-periodic) proof testing phases for unavailability calculation of BSRPs, the corresponding intervals are assumed to be 1440 h for periodic testing and $720 \mathrm{~h}, 1440 \mathrm{~h}$ to 2160 h for non-periodic testing, taking detection delay and mission requirements into consideration, which are listed in Table 5. Unavailability is evaluated based on both failure rate and test intervals. The intervals of testing phases will play a vital role in unavailability evaluation for performance analysis. The changing parameters and proof testing duration are therefore considered as the leading indicators here.

To apply the proposed formulas for unavailability calculations, the relevant parameters for BSRPs need to be chosen. The failure rates regarding to the BSRPs may be derived from MTTF of the historical statistics [16, 35], where MTTF is recorded between 5564 days to 25104 days in different failure modes. The failure rates can be approximated by $\lambda_{\mathrm{DU}}=1 /$ MTTF and the results of $\lambda_{\mathrm{DU}}$ changes from $1.66 \mathrm{E}-6 / \mathrm{h}$ to $7.49 \mathrm{E}-6 / \mathrm{h}$. The $\lambda^{1}{ }_{D U}$ during the testing phase $\mathrm{T}_{1}=720 \mathrm{~h}$, the $\lambda^{2}{ }_{D U}$ during the testing phase $\mathrm{T}_{2}=1440 \mathrm{~h}$, and the $\lambda^{3}{ }_{D U}$ during the testing phase $\mathrm{T}_{3}=$ 2160 h , are assumed to be $1.8 \mathrm{E}-6 / \mathrm{h}, 3.6 \mathrm{E}-6 / \mathrm{h}$ and $7.2 \mathrm{E}-6 / \mathrm{h}$ respectively, and which are shown in Table 5. They are also assumed to be identical and independent of time in every proof testing phase. The repair rate is also accordingly calculated by $\mu_{\mathrm{DU}}=1 / 24=0.0417 / \mathrm{h}$ given repair time of 24 h , and also assumed to be constant in proof testing phases. The failure rates and repair rates are used to construct the transition rate matrix $C$. The given states at the beginning operation are functioning for all the components.

Table 6 Parameters of BSRP with proof testing phase



# 4.1.1 Unavailability with non-periodic phases 

Due to the detection delay in the subsea context, a BSRP may subject to non-periodic proof testing. It is therefore necessary to evaluate such effects on the time-dependent unavailability. Starting from the inputs with 3 selected proof testing phases, the Eq. (10) and Eq. (16-23) are applied to calculate the corresponding unavailability for two types of configurations, and the trends are shown in Fig. 6 (a) and (b) respectively. It is seen that the maximum value of unavailability obtained by periodically tested every 720 h for 1 ool configuration and 1002 configuration is nearly $2.6 \times 10^{-3}$ and $6.8 \times 10^{-6}$ respectively. It is obvious that the instantaneous unavailability increases with time in first phase $[0,720]$ and then decreases quickly in the beginning of second proof testing phase $[720,1440]$ due to the repair action and finally grows as the same trend as that of first proof testing phase. Fig. 6 (a) shows the trend of 1001 configuration is in linear way while that of 1002 configuration grows non-linearly in Fig. 6 (b).
![img-7.jpeg](img-7.jpeg)

Fig. 6 Trends of unavailability for (a) 1001 configuration and (b) loo2 configuration

Comparisons of the time-dependent unavailability for selected proof testing phases are investigated by keeping every periodic testing interval 1440 h and 3 -non-periodic testing intervals varying from $720 \mathrm{~h}, 1440 \mathrm{~h}$ to 2160 h . The results of unavailability 1001 configuration and (b) for 1002 configuration are implemented given the failure rate of $3.6 \times 10^{-6}$ in every phase, which are shown in Fig. 7 (a) and (b). It is seen that whatever the types of configurations are, instant unavailability with periodic test seems to have similar tendency while that with non-periodic tests are increasing from one phase to another phase. When BSRPs are evaluated with the UA(t) calculations, the functions of both BSRP configurations during 3 periodic and non-periodic proof testing phases satisfy the minimum SIL 2 or more than SIL 2 requirement.

![img-8.jpeg](img-8.jpeg)

Fig. 7 Comparison of unavailability for periodic and non-periodic proof testing phases for (a) 1001 configuration and (b) loo2 configuration

# 4.1.2 Unavailability with degradation 

A BSRP may degrade from one phase to next phase if the components are not fully replaced for new ones, and it is therefore necessary to evaluate such effects of on the time dependent unavailability. The failure rates are changing in different testing phases while it is kept identical in one phase. Increasing failure rate is introduced to model this kind of degradation. Comparisons of the time-dependent unavailability for considering degradation are investigated by keeping constant failure rate $3.6 \mathrm{E}-6 / \mathrm{h}$ and increasing failure rates from $1.8 \mathrm{E}-6 / \mathrm{h}, 3.6 \mathrm{E}-6 / \mathrm{h}$ to $7.2 \mathrm{E}-6 / \mathrm{h}$. The results of unavailability 1001 configuration and (b) for 1002 configuration are implemented given the proof testing duration varying from $720 \mathrm{~h}, 1440 \mathrm{~h}$ and 2160 h , which are shown in Fig. 8 (a) and (b). It can be found that the values of unavailability without degradation grow at the same speed while those with effects of degradation grow at the increasing speed in every phase. What's more, the value in the end of the third phase is nearly $8 \times 10^{-3}$ and $1.5 \times 10^{-2}$ for 1001 configuration while that is nearly $6 \times 10^{-5}$ and $2.4 \times 10^{-4}$ for 1002 configuration, respectively. It should be noted that the contribution from degradation will make the unavailability higher and grow faster than that without degradation.

Fig. 8 (a) also shows that the function of the BSRP 1001 configuration considering degradation of components after 3500 h cloud not meet the minimum SIL 2 requirement, while it can satisfy the minimum SIL 2 requirement without effects of degradation. However, the BSRP 1002 configuration can reach the SIL3 for enhancing the performance of BOP system due to the redundancy in Fig. 8 (b). It is found that the testing phase after 3500 h is therefore dominant areas where more attention needs to be paid. The proposed models considering degradation effects may make results bigger than those without degradation. It should be important to reminder the decision makers that unavailability assessment should consider such practical influence factors. Note that the testing phase and the configurations as redundancy are also the leading decision variables when including a SIL evaluation of the BSRP function.

![img-9.jpeg](img-9.jpeg)

Fig. 8 Comparison of unavailability between without degradation and with degradation for (a) 1 ool configuration and (b) loo2 configuration

# 4.1.3 Average unavailability $\left(\mathrm{UA}_{\text {avg }}\right)$ for proof testing time 

There are four cases considered for evaluating $\mathrm{UA}_{\text {avg }}$ by comparing components with degradation and without degradation in proof testing phases, which is specified as:

- Case 1: BSRP with 1 ool configuration is tested in non-periodic phase
- Case 2: BSRP with 1 ool configuration is tested in periodic phase
- Case 3: BSRPs with 1002 configuration is tested in non-periodic phase
- Case 4: BSRPs with 1002 configuration is tested in periodic phase

Fig. 9 present the contribution of $\mathrm{UA}_{\text {avg }}$ of BSRPs for four cases based on the proposed Eq. (15) and Eq. (16-23). It is found that the values of $\mathrm{UA}_{\text {avg }}$ for both of configurations have a significant increase from one phase to another phase in non-periodic phases but keep slight growth in periodic phase. The $\mathrm{UA}_{\text {avg }}$ of BSRPs with degradation is always higher than that without degradation. We also observe that the values of $\mathrm{UA}_{\text {avg }}$ of 1002 configuration are almost reduced by more than two orders of magnitude compared with 1 ool configuration whatever in any cases. BSRPs with degradation in non-periodic proof testing phase will lead to the increase of $\mathrm{UA}_{\text {avg }}$. When BSRPs are evaluated with the $\mathrm{UA}_{\text {avg }}$ calculations, the functions of both BSRP configurations for four cases satisfy the minimum SIL 2 requirement as shown in Fig. 9(a) and (b) or more than SIL 2 regardless of degradation in Fig. 9(c) and (d). It is also seen in Fig. 9(a) that for the BSRP 1001 configuration with degradation, the functions only meet the SIL 3 during the first non-periodic proof testing phase. As the testing phase increases, the SIL is decreasing. It therefore supports that decision makers can calculate $\mathrm{UA}_{\text {avg }}$ under different cases or choose the reasonable non-periodic phases and configurations under a given SIL. It also provides the basis for preventive maintenance in order to select the best maintenance intervals.

![img-10.jpeg](img-10.jpeg)

Fig. 9 Comparison of $\mathrm{UA}_{\text {avg }}$ between without degradation and with degradation for (a) Case 1, (b) Case 2, (c) Case 3 and (d) Case 4

# 4.2 Unavailability analysis for partial testing 

According to the standards, partial tests are performed for different configurations of BSRPs. When BSRPs are subject to partial testing, DU1 and DU2 failures mentioned in section 2.4 are considered here. The effects of testing errors may exist during testing phases due to the imperfect testing. Imperfect testing with minor errors is taken into account and assumed to be assigned in expression of Eq. (10) and Eq. (26-31) with probability 0.01 . Since the repairs are likely to be postponed due to the accident, time waiting for repair is not ignored. Two kinds of methods are therefore introduced to assess the repair rate: one is that repair rate can be calculated by adopting mean repair time (MRT), and another is that repair rate can be obtained by adopting mean downtime (MDT) [33]. The effects of testing errors and postponed repair on unavailability are therefore analyzed here.

The BSRP is also required to perform such partial testing periodically in order to meet the function testing requirements. The interval of such testing is therefore obviously expressed as identical and denoted as $\Delta$. Due to the short period for a partial testing, the failure rates for DU1 and DU2 are kept to be constant in every phase, meaning that the effects of degradation are excluded for partial testing. The relevant parameters from the existing statistics are given in Table 7.

Table 7 Parameters for partial testing


# 4.2.1 Unavailability with testing errors 

Fig. 7 shows that unavailability can be predicted in 4 continuous partial testing phases when keeping a testing interval of 168 h for both of configurations respectively. It is obvious that the values grow firstly in first testing phase then decrease quickly in second testing phase in Fig. 10 (a) and (c). It should be also noted that the values decrease from nearly $0.6 \times 10^{-3}$ to $0.4 \times 10^{-3}$ rather than to 0 because of DU2 failures which cannot be detected by partial testing. If there may be testing errors made in partial testing phases, the unavailability is obtained by giving the probability of errors with 0.01 . Calculation results with testing errors are compared with those with no testing errors, as shown in Fig. 10 (b) and (d). It is also find that imperfect testing with minor errors will result in a momentary increase of unavailability then a fast decrease after repair action.

The SIL evaluation for imperfect testing with testing errors is also indicated in Fig. 10. If testing errors are out of consideration in the partial testing process, the functions of different configurations meet the minimum SIL 2 requirement (Fig. 10 (a) and (c)). In contrast, the occurrence of test errors will reduce the performance of BSRPs. Fig. 10 (b) indicates the functions could not meet the SIL 2 requirement while performing imperfect testing for 1 ool configuration. Therefore, adding a redundant BSRP is deemed to be an effective measure for enhancement of its performance. Note that the functions of the BSRP 1002 configuration still meet the SIL 2 requirement because of the redundancy (Fig. 10 (d)). To meet the minimum SIL 2 requirement, the testing errors should be avoided, especially for 1 ool configuration.
![img-11.jpeg](img-11.jpeg)

![img-12.jpeg](img-12.jpeg)

Fig. 10 Unavailability during partial testing phase for (a) with no errors for 1 ool configuration, (b) comparison between errors and no errors for 1 ool configuration, (c) with no errors for 1002 configuration and (d) comparison between errors and no errors for 1002 configuration

# 4.2.2 Unavailability with postpone repair 

Due to the particulars of subsea applications, the repair action cannot be initiated immediately even when the DU failures are detected. In order to examine the effects of the non-negligible repair time, different values of repair rates are calculated based on MRT and MDT, while keeping the testing period of 168 h for 1 ool and 1002 configuration respectively. This part gives three scenarios to calculate the unavailability, and comparisons are made as shown in Fig. 11. Three scenarios are specified as:

- Scenario 1: Non-negligible MRT
- Scenario 2: Non-negligible MDT
- Scenario 3: Negligible repair time

It can be found that the values of unavailability with $M R T$ are lower than others, and unavailability with negligible repair time grows almost linearly given perfect partial testing with no errors, while it has a stepped increase given imperfect testing with errors as indicated in Fig. 11 (a) and (b). We also see that the maximum value in Scenario 3 with no errors are almost close to $2.5 \times 10^{-3}$ compared to $3.3 \times 10^{-2}$ with errors, and the ration of both of them shows that the latter is more than 10 times than the former for 1 ool configuration. Similarly, the figures in Fig. 11 (c) and (d) in Scenario 3 with no errors are almost close to $4.7 \times 10^{-6}$ compared to $3 \times 10^{-2}$ with errors, and the comparison using the ration shows that the latter is more than $10^{3}$ times than the former for 1002 configuration. It is also noted that values of unavailability with MDT is always higher than those with MRT because the fixed time $(\Delta / 2)$ is taken into account in repair rate calculation. The different methods for evaluating repair rates also play an important role in unavailability evaluation.

The SIL evaluation for postpone repair during the 4 continuous partial testing is also indicated in Fig. 11. It is found that the functions of different configurations meet the minimum SIL 2 requirement under different calculation method of repair rate when the testing errors are excluded in Fig. 11(a) and (c). In contrast, the occurrence of test errors will decrease the SIL of BSRPs SIF, which is shown in Fig. 11(b) and (d). As a result, the functions could not meet the SIL 2 requirement at the beginning of the second partial testing when repair time is ignored for both configurations. Repair rate derived from MDT will decrease the SIL at the end of the second partial testing as well. Therefore, to meet the SIL requirement, the testing errors should be avoided and repair time should be considered.

![img-13.jpeg](img-13.jpeg)

Fig. 11 Unavailability during imperfect testing considering postpone repair for (a) 1 ool configuration without errors, (b) 1001 configuration with errors, (c) 1002 configuration without errors, and (d) 1002 configuration with errors

# 4.2.3 Average unavailability for partial testing 

$\mathrm{UA}_{\text {avg }}$ for 1001 and 1002 configurations subject to 4 continuous partial testing phases are calculated based on the proposed models under testing errors and postpone repair.

1) $\mathrm{UA}_{\text {avg }}$ with testing errors

There are four cases considered for evaluating $\mathrm{UA}_{\text {avg }}$ during imperfect testing with testing errors which are specified as

- Case 1: BSRP with 1001 configuration is tested with no errors
- Case 2: BSRP with 1001 configuration is tested with errors
- Case 3: BSRPs with 1002 configuration is tested with no errors
- Case 4: BSRPs with 1002 configuration is tested with errors
$\mathrm{UA}_{\text {avg }}$ of BSRP for four cases is calculated based on Eq. (15) as shown in Table 8. It indicates that the values of $\mathrm{UA}_{\text {avg }}$ are increasing in sequential partial testing phases due to the effect of DU2 failures. We also find those in

first testing phases are same compared to other phases for both configurations due to no testing errors. It is worth noting that values from second phase with errors are larger than those with no errors by comparing Case 2 and Case 1 or Case 4 and Case 3. Total $\mathrm{UA}_{\text {avg }}$ in a proof testing phase $[0,672]$ is obtained for four kinds of cases and we find that the ratio between with errors and no errors is almost 2.2 for 1001 configuration while the ration is almost $2.4 \times 10^{-3}$ for 1002 configuration. As the partial testing phases increase, the SIL of BSRPs SIF for each case is decreasing, except for Case 3. It is indicated that the functions of both configurations satisfy the SIL 2 requirements and the SIL is higher for Case 3 and Case 4. Since Case 3 is modeled for 1002 configuration and redundancy will help to improve the performance of the BSRP. The more attention should be paid for 1001 configuration under effects on testing errors and testing phases, especial from the beginning of the second partial testing.

Table 8 UA $_{\text {avg }}$ for comparison between testing with errors and no errors


2) $\mathrm{UA}_{\text {avg }}$ with postpone repair

There are four cases considered for evaluating $\mathrm{UA}_{\text {avg }}$ in partial testing phases with postpone repair, which are specified as

- Case 1: Repair rate for 1001 configuration is calculated based on MRT
- Case 2: Repair rate for 1001 configuration is calculated based on MDT
- Case 3: Repair rate for 1002 configuration is calculated based on MRT
- Case 4: Repair rate for 1002 configuration is calculated based on MDT
$\mathrm{UA}_{\text {avg }}$ of BSRPs for four cases is calculated based on Eq. (15) as shown in Table 9. It indicates that values from the second testing phase with MDT are larger than those with MRT by comparing Case 2 and Case 1 or Case 4 and Case 3. Total $\mathrm{UA}_{\text {avg }}$ in a proof testing phase $[0,672]$ is obtained for four kinds of cases and it is found that ratio between with MDT and MRT is almost 1.25 for 1001 configuration while ration is almost 2.8 for 1002 configuration. It is also seen that as the partial testing phases increase, the SIL of BSRPs SIF for each case is decreasing. The functions of both configurations satisfy the SIL 2 requirements from the beginning of the second testing phase expect Case 3. The more attention should be paid for Case 1, Case 2 and Case 4 under effects of 1001 configurations, calculation methods of repair rate and testing phases.

Table 9 UA $_{\text {avg }}$ for comparison between MRT and MDT


To examine the effect of repair time taking different values on the $\mathrm{UA}_{\text {avg }}$ of BSRPs, the repair rates based different methods are applied to make comparisons in calculating $\mathrm{UA}_{\text {avg }}$ as shown in Fig. 12. Testing errors are considered in imperfect testing phases. Fig. 12 (a) and (b) show the trend of $\mathrm{UA}_{\text {avg }}$ with no testing errors given different repair time. It is obvious that the $\mathrm{UA}_{\text {avg }}$ firstly has a fast decreasing trend and then grows slowly over repair time. And the value of $\mathrm{UA}_{\text {avg }}$ for with negligible repair rate (at $\mathrm{t}=0$ ) is about $9.1 \times 10^{-4}$ and $1.63 \times 10^{-6}$ with no testing errors, while $1.4 \times 10^{-2}$ and $1.1 \times 10^{-2}$ with testing errors in Fig. 9 (c) and (d) for 1001 configuration and 1002 configuration respectively. Note that the value of $\mathrm{UA}_{\text {avg }}$ with repair rate derived from MDT is more likely to be large results compared to that derived from MRT. In many subsea practical applications, the performance of the BSRPs with no testing errors and larger repair rate could be improve, and the proposed method will be realistic to assess the $\mathrm{UA}_{\text {avg }}$ under effects of such testing errors and postpone repair for choosing the best repair time.
![img-14.jpeg](img-14.jpeg)

Fig. $12 \mathrm{UA}_{\text {avg }}$ under different repair time based on MRT and MDT for (a) 1001 configuration with no errors, (b) 1002 configuration with no errors, (c) 1001 configuration with errors and (d) 1002 configuration with errors

# 5 Monte Carlo simulation 

The Monte Carlo simulation (MCS) is adopted in this paper to validate the proposed model. MCS is a suitable and valuable approach which is widely applied to reliability analysis for real-world system [36-38] and also to

verify the results obtained with application of the other analytical methods recommended in IEC 61508 [8, 39]. Such simulation methods can also provide the flexibility in describing the practical aspects of system operation (equipment failure and subsequent maintenance) by simulating the realistic process and random behaviors of the system to generate a lifetime scenario [40, 41]. MCS treats the problem as a series of real experiments, and the necessary indicators such as reliability and availability can be estimated by counting the number of times or time spent on an event that occurs in simulated process. What's more, the occurrence time of the next transition and the ways of the system configuration changing will be captured in such process. Finally, the simulation results with the expected values are compared those given in the analytic formulas. The numerical results generated are also validated by MCS for decision support.

# 5.1 Monte Carlo simulation model 

The MCS is performed by program codes written by using Matlab software, and the overall workflow is used to describe the application of the MCS model for $\mathrm{UA}_{\text {avg }}$ of BSRPs considering the additional state with waiting for repair, which is shown in Fig. 13. The particulars of the presenting MCS model are specified as:
![img-15.jpeg](img-15.jpeg)

Fig. 13 Framework for estimating the unavailability using Monte Carlo simulation

- In this simulation process, the program firstly incorporates the system information to identify the possible

available and unavailable states for different configurations in a specified proof testing phase or partial testing phase. The input parameters required for this analysis consist of probability density functions for time to failure, failure rate, repair rate, testing or maintenance strategies, duration of testing, and simulation times. The time to failure and time to repair are assumed to be exponentially distributed.

- The system will be in one of possible states and make transition possible from one state to another state. These states will come alternatively since they are changing over time. It is important that the relevant information is obtained from the MCS and this information can reveal when the next transition (failure, waiting for repair or functioning) occurs and how the state of system varies as a consequence of the transition.
- The date of the last transition $\left(\mathrm{t}_{\mathrm{Evi}}\right)$ and the date of the next transition $\left(\mathrm{t}_{\mathrm{Evn}}\right)$ about failure occurring are simulated based on the interval of testing phase, failure rate and repair rate. The duration of the state is random for both available and unavailable states, which will depend on the probability density functions for time to failure and time to repair. The corresponding duration $D_{\text {state }}(i, j)$ spent in each state $i$ in the $j^{\text {th }}$ testing phase can be obtained for evaluating the analytical $\mathrm{UA}_{\text {avg }}$. The initial transition date is assigned to 0 , namely $\mathrm{t}_{\mathrm{Evi}}=\mathrm{t}_{\mathrm{Evn}}=0$, due to the system in the functioning state.

$$
D_{\text {state }}(i, j)=D_{\text {state }}(i, j)+\left(t_{\text {Evn }}-t_{\text {Evi }}\right)
$$

- The $\mathrm{t}_{\mathrm{Evn}}$ of the system is moved to the minimum transition date and the state of system is corresponding changed. The MCS is repeated in a specified number of times. Let $D_{\text {state } U A}(i, j)$ denote the time spent in each unavailable state of the system. The system average unavailability $\mathrm{UA}_{\text {avg }}$ is then evaluated as

$$
U A_{a v g}=\frac{\sum_{i}^{i} \sum_{i}^{j} D_{\text {stateUA }}(i, j)}{\sum_{i}^{i} \sum_{i}^{j} D_{\text {state }}(i, j)}
$$

- A sample of size $N$ independent identically distributed random variables are simulated to estimate the unavailability of the BSRPs, the coefficient of variation $C$ of this estimator [42] is

$$
C\left(U A_{a v g}\right)=\left(\frac{1-U A_{a v g}}{U A_{a v g} N}\right)^{0.5}
$$

- The confidence interval for a fixed number of samples N under a given confidence level $95 \%$ is defined [43]. The approximation of the $95 \%$ confidence interval for the value $\mathrm{UA}_{\text {avg }}$ can be obtained as $\mathrm{CI}_{0.95}=\left(C_{-}, C_{+}\right)$, where

$$
C_{ \pm}=\mathrm{UA}_{\text {avg }}\left(1 \pm 1.96 C\left(\mathrm{UA}_{\text {avg }}\right)\right)
$$

- After performing all the MCS, the results from the simulation can make a comparison with analytical evaluation for validation of a realistic system.


# 5.2 Validation of models for proof testing 

The validation using MCS for proof testing is carried out to check that the proposed model would generate reasonable and similar results. Parameters required in MCS are listed in Table 6. The 9 significant combinations of possible states for 1002 configuration such as (FU1-FU2, FU1-DU2) are identified for the MCS with proof testing. The number of simulations for 1001 configuration and 1002 configuration of the BSRP is kept fixed at $N=1 \times 10^{7}$ and $N=1 \times 10^{9}$ simulatios, respectively.

Numerical results from the proposed model and MCS are listed in Table 10. On the basis of the assumption in Section 2.1, it is seen that the values of $\mathrm{UA}_{\text {avg }}$ for 1001 configuration obtained from the MCS is much closer to those obtained from the formulas. It indicates that 1001 configuration has the tiny differences in figures of $\mathrm{UA}_{\text {avg }}$

between two methods because of the simple structure of 1001 configuration. It is possible to give the illustration about difference of results from two methods. The confidence interval of a probability sample for the proof testing is calculated with the $95 \%$ confidence interval, as shown in Table 10. Take 1001 configuration with the 1440 h proof testing phase for instance, $\mathrm{UA}_{\text {avg }}$ lies in the interval from $2.62 \mathrm{E}-03$ to $2.68 \mathrm{E}-03$ with the best estimate being $2.65 \mathrm{E}-03$. It is noted that this probability is somewhat larger than the value which was obtained based on performing the proposed model. Compared to the analytic formula results, MCS can generate minimum results with the relative error of $1.53 \%$. Approximation formulas are therefore validated by the closeness of the results and the analytic methods can be applied to assess availability of a real system.

Table $10 \mathrm{UA}_{\text {avg }}$ of BSRP with proof testing time


# 5.3 Validation of models for partial testing 

The validation using MCS for partial testing is carried out to partially check that the proposed model would generate reasonable and similar results. Generally, it isn't realistic to check the errors making in the testing phase using MCS, so the effect of this factor is excluded from the analysis. The effects of varying the partial testing intervals and the repair time are next investigated. The relevant parameters derived from the existing statistics, which are given in Table 7. The 16 significant combinations of possible states for 1002 configuration such as (FU1-FU2, FU1-DU2) are identified for the MCS with partial testing. The number of simulations for 1001 configuration and 1002 configuration of the BSRP is kept fixed at $N=1 \times 10^{7}$ and $N=1 \times 10^{9}$ simulatios, respectively.

The results for 1001 and 1002 configurations of the BSRP from the proposed model are compared with those from the MCS given the $\omega=\eta=0$, with setting different periodic partial testing intervals as listed in Table 11. As indicated in Table 11, it is possible to get an identical degree of accuracy to the results from both the proposed model and MCS. The value of $\mathrm{UA}_{\text {avg }}$ in different partial testing intervals from the MCS is close to that obtained from the proposed model. The results also obtained by MCS are compared with those from proposed model given different repair time, with setting a total proof testing phase of 720 h in Table 12. The MRT method is adopted here to calculate the repair rate. The results show that the figures in $\mathrm{UA}_{\text {avg }}$ obtained from MCS has an increase trend as same as that obtained from the proposed model with repair time. The $\mathrm{UA}_{\text {avg }}$ in the partial texsting from the MCS is

also close to that obtained from the proposed model. Note that the values of $\mathrm{UA}_{\text {avg }}$ from the simulation shown in Table 12 are mostly slightly lower than those from the analytic formulas since they are developed in a conservative way. The confidence interval of a probability sample for the partial testing is calculated with the $95 \%$ confidence interval, as shown in Table 11 and Table 12. Take 1001 configuration with the repair time of 120 h for instance, $\mathrm{UA}_{\text {avg }}$ lies in the interval from $3.29 \mathrm{E}-03$ to $3.37 \mathrm{E}-03$ with the best estimate being $3.33 \mathrm{E}-03$. Compared to the analytic formula results, MCS can generate minimum results with the relative error of $1.77 \%$. Approximation formulas are therefore validated by the closeness of the results from the MCS.

Table 11 $\mathrm{UA}_{\text {avg }}$ under different partial testing


Table 12 $\mathrm{UA}_{\text {avg }}$ of BSRP for partial testing given different repair time


# 6. Conclusion 

Subsea blind shear ram preventers constitute a paramount well control device to ensure the safety of drilling.

Partial testing is an effective approach to complement proof testing of this kind of subsystem and enhance their performance. However, in order to consider the effects of degradation and partial testing when making decisions about design and operation, it is necessary to have formulas that can handle the various issues during operation and maintenance. This paper has presented a new multiphase-Markov-based approach for the performance analysis of subsea blind shear ram preventers subject to proof testing and partial testing phases. The main advantage of the proposed approach is that both of operational and maintenance activities are considered by introducing the states for waiting repair and maintenance duration. The multiphase-based-Markov models for both 1001 and 1002 configurations have been then established as efficient means for calculating the instant unavailability tendency and average unavailability for performance analysis.

Approximation formulas for proof testing have been developed. A focus is given to 1001 and 1002 configurations considering non-periodic testing characteristic. The most difficult challenge in relation to the approximate model is to handle the degradation effects in periodic and non-periodic phases. We have shown that the degradation in non-periodic phase affects hugely the value of $\mathrm{UA}_{\text {avg }}$. Approximation formulas for partial testing also have been developed using some methods where undetected dangerous failures respectively revealed by partial and full tests are covered. Relying on some results gained from the analysis involving effects of testing errors and postpone repair, we found imperfect testing made a main contribution to the unavailability while there is a small increase under different repair time. Various numerical comparisons for different cases have been performed. The Monte Carlo simulation approach treats more complex and realistic problems as a series of real experiments by counting the number of times or time spent on an event that occurs in simulated process. It therefore has the obvious advantages in modeling the practical issues of a real world complex system such as equipment degradation and maintenance strategies related to the subsea context. The results obtained from Monte Carlo simulation are closer to the accurate analytic formulations given by the proposed approach. This fact allows us to validate the established formulas.

However, the proposed analytical formulations have limitations in terms of the proof test coverage which is realistic in some testing procedures related to the practical operational scenarios such as emergency operations or emergency situations. Furthermore, the degradation of the components subject to the partial testing is ignored in this paper. Finally, in the modeling of real-world BOP system, such system normally consists of several subsystems which may comprise of many components. Such components may follow the different failure distribution and common cause failures. Therefore, further enhancement of the proposed formulas could be done with the inclusion of non-perfect proof tests considering the emergency operational scenarios, the effects of degradation during a partial test and to extend the current model to deal with the non-exponential components. If such realistic issues can be applied to the performance analysis, the more realistic result can be obtained.

# Acknowledgment 

The research is carried out when the first author is a visiting researcher at NTNU, and she is financially supported by China University of Petroleum (Beijing) and China Scholarship Council. The authors are grateful for the reviewers' helpful comments.
